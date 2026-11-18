// Categories, documents (articles, troubleshooting, FAQs, SOPs, policies, guides), templates, feedback
import { Router } from 'express';
import { all, get, run, tx, nowIso, parseJson, getSetting } from '../db.js';
import { can, canPublishDoc } from '../permissions.js';
import { h, bad, forbidden, notFound, audit, str, oneOf, sanitizeHtml, slugify, PRIORITIES, DOC_STATUSES } from '../util.js';
import { markDirty } from '../search.js';

const r = Router();
const DOC_TYPES = ['article', 'troubleshooting', 'faq', 'sop', 'policy', 'guide'];
const SCOPE_OF = { article: 'kb', troubleshooting: 'kb', faq: 'kb', sop: 'sop', policy: 'policy', guide: 'communication' };
const SCOPES = ['kb', 'template', 'sop', 'policy', 'communication'];
const PUBLIC_SECTION_BLOCKLIST = ['internal'];

const userMap = () => new Map(all('SELECT id, name FROM users').map((u) => [u.id, u.name]));

// ================= Categories =================
r.get('/categories', h((req, res) => {
  const scope = oneOf(req.query.scope, SCOPES, 'kb');
  const cats = all('SELECT * FROM categories WHERE scope = ? ORDER BY sort, name', scope);
  const showAll = can(req.user, 'docs.read_unpublished');
  const table = scope === 'template' ? 'templates' : 'documents';
  const counts = new Map(all(`SELECT category_id, COUNT(*) n FROM ${table} WHERE ${showAll ? "status != 'archived'" : "status = 'published'"} GROUP BY category_id`).map((x) => [x.category_id, x.n]));
  const typeCounts = scope === 'kb'
    ? all(`SELECT category_id, type, COUNT(*) n FROM documents WHERE ${showAll ? "status != 'archived'" : "status = 'published'"} GROUP BY category_id, type`)
    : [];
  const tree = cats.filter((c) => !c.parent_id).map((c) => {
    const subs = cats.filter((s) => s.parent_id === c.id).map((s) => ({ ...s, count: counts.get(s.id) || 0, types: Object.fromEntries(typeCounts.filter((t) => t.category_id === s.id).map((t) => [t.type, t.n])) }));
    const own = counts.get(c.id) || 0;
    const types = {};
    for (const t of typeCounts) if (t.category_id === c.id || subs.some((s) => s.id === t.category_id)) types[t.type] = (types[t.type] || 0) + t.n;
    return { ...c, subcategories: subs, count: own + subs.reduce((a, s) => a + s.count, 0), types };
  });
  res.json(tree);
}));

r.post('/categories', h((req, res) => {
  if (!can(req.user, 'categories.manage')) throw forbidden();
  const b = req.body || {};
  const scope = oneOf(b.scope, SCOPES, null);
  if (!scope) throw bad('Invalid scope.');
  const name = str(b.name, 120);
  if (!name) throw bad('Name is required.');
  const parent = b.parent_id ? get('SELECT * FROM categories WHERE id = ? AND scope = ?', Number(b.parent_id), scope) : null;
  if (b.parent_id && (!parent || parent.parent_id)) throw bad('Subcategories can only be created under a top-level category.');
  const slug = slugify(b.slug || name);
  if (get('SELECT id FROM categories WHERE scope = ? AND slug = ? AND parent_id IS ?', scope, slug, parent?.id ?? null)) throw bad('A category with this name already exists here.');
  const now = nowIso();
  const maxSort = get('SELECT MAX(sort) m FROM categories WHERE scope = ? AND parent_id IS ?', scope, parent?.id ?? null)?.m ?? 0;
  const info = run('INSERT INTO categories(scope,parent_id,slug,name,name_am,description,icon,sort,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?)',
    scope, parent?.id ?? null, slug, name, str(b.name_am, 120), str(b.description, 500), str(b.icon, 40), maxSort + 1, now, now);
  audit(req, 'category.create', 'category', info.lastInsertRowid, { scope, name });
  markDirty();
  res.status(201).json(get('SELECT * FROM categories WHERE id = ?', Number(info.lastInsertRowid)));
}));

r.patch('/categories/:id', h((req, res) => {
  if (!can(req.user, 'categories.manage')) throw forbidden();
  const c = get('SELECT * FROM categories WHERE id = ?', Number(req.params.id));
  if (!c) throw notFound();
  const b = req.body || {};
  const name = 'name' in b ? str(b.name, 120) : c.name;
  if (!name) throw bad('Name is required.');
  run('UPDATE categories SET name = ?, name_am = ?, description = ?, icon = ?, sort = ?, updated_at = ? WHERE id = ?',
    name, 'name_am' in b ? str(b.name_am, 120) : c.name_am, 'description' in b ? str(b.description, 500) : c.description,
    'icon' in b ? str(b.icon, 40) : c.icon, 'sort' in b ? Number(b.sort) || 0 : c.sort, nowIso(), c.id);
  audit(req, 'category.update', 'category', c.id, { name });
  markDirty();
  res.json(get('SELECT * FROM categories WHERE id = ?', c.id));
}));

r.delete('/categories/:id', h((req, res) => {
  if (!can(req.user, 'categories.manage')) throw forbidden();
  const c = get('SELECT * FROM categories WHERE id = ?', Number(req.params.id));
  if (!c) throw notFound();
  const ids = [c.id, ...all('SELECT id FROM categories WHERE parent_id = ?', c.id).map((x) => x.id)];
  const ph = ids.map(() => '?').join(',');
  const used = get(`SELECT (SELECT COUNT(*) FROM documents WHERE category_id IN (${ph})) + (SELECT COUNT(*) FROM templates WHERE category_id IN (${ph})) + (SELECT COUNT(*) FROM tickets WHERE category_id IN (${ph}) OR subcategory_id IN (${ph})) n`, ...ids, ...ids, ...ids, ...ids).n;
  if (used) throw bad(`This category is still used by ${used} document(s), template(s) or ticket(s). Move them first.`);
  run('DELETE FROM categories WHERE id = ?', c.id);
  audit(req, 'category.delete', 'category', c.id, { name: c.name });
  res.json({ ok: true });
}));

// ================= Documents =================
function catPath(categoryId) {
  if (!categoryId) return [];
  const c = get('SELECT id, slug, name, name_am, parent_id, scope FROM categories WHERE id = ?', categoryId);
  if (!c) return [];
  const p = c.parent_id ? get('SELECT id, slug, name, name_am, parent_id, scope FROM categories WHERE id = ?', c.parent_id) : null;
  return p ? [p, c] : [c];
}

function serializeDoc(d, users) {
  return {
    ...d,
    sections: parseJson(d.sections, []),
    tags: parseJson(d.tags, []),
    related: parseJson(d.related, []),
    templates: parseJson(d.templates, []),
    features: parseJson(d.features, []),
    policy_pending: !!d.policy_pending,
    ai_visible: !!d.ai_visible,
    created_by_name: users?.get(d.created_by) || null,
    updated_by_name: users?.get(d.updated_by) || null,
  };
}

function canSeeDoc(user, d) {
  if (d.status === 'published') return true;
  return can(user, 'docs.read_unpublished');
}

r.get('/docs', h((req, res) => {
  const { type, category, status, q, tag, sort = 'title', limit = 500, pending } = req.query;
  const where = [];
  const p = [];
  if (type) { const ts = String(type).split(',').filter((t) => DOC_TYPES.includes(t)); if (ts.length) { where.push(`d.type IN (${ts.map(() => '?').join(',')})`); p.push(...ts); } }
  if (category) {
    const ids = [Number(category), ...all('SELECT id FROM categories WHERE parent_id = ?', Number(category)).map((x) => x.id)];
    where.push(`d.category_id IN (${ids.map(() => '?').join(',')})`); p.push(...ids);
  }
  if (!can(req.user, 'docs.read_unpublished')) where.push("d.status = 'published'");
  else if (status && status !== 'all') { where.push('d.status = ?'); p.push(status); }
  else if (!status) where.push("d.status != 'archived'");
  if (pending === '1') where.push('d.policy_pending = 1');
  if (tag) { where.push('d.tags LIKE ?'); p.push(`%"${String(tag).replace(/[%_"]/g, '')}"%`); }
  if (q) { const like = `%${String(q).replace(/[%_]/g, '')}%`; where.push('(d.title LIKE ? OR d.summary LIKE ? OR d.slug LIKE ?)'); p.push(like, like, like); }
  const order = { title: 'd.title COLLATE NOCASE', updated: 'd.updated_at DESC', views: 'd.views DESC', created: 'd.created_at DESC' }[sort] || 'd.title';
  const rows = all(`SELECT d.id, d.slug, d.type, d.title, d.summary, d.category_id, d.status, d.priority, d.audience, d.department, d.policy_pending, d.features, d.tags,
      d.version, d.views, d.helpful_yes, d.helpful_no, d.updated_at, d.updated_by, d.created_at,
      c.name category_name, c.parent_id category_parent_id, pc.name parent_category_name
    FROM documents d LEFT JOIN categories c ON c.id = d.category_id LEFT JOIN categories pc ON pc.id = c.parent_id
    ${where.length ? 'WHERE ' + where.join(' AND ') : ''} ORDER BY ${order} LIMIT ?`, ...p, Math.min(Number(limit) || 500, 2000));
  const users = userMap();
  res.json(rows.map((d) => ({ ...d, policy_pending: !!d.policy_pending, features: parseJson(d.features, []), tags: parseJson(d.tags, []), updated_by_name: users.get(d.updated_by) || null })));
}));

r.get('/docs/:slug', h((req, res) => {
  const d = get('SELECT * FROM documents WHERE slug = ?', req.params.slug);
  if (!d || !canSeeDoc(req.user, d)) throw notFound('Article not found or not published.');
  if (req.query.view !== '0') {
    run('UPDATE documents SET views = views + 1 WHERE id = ?', d.id);
    run(`INSERT INTO doc_views(user_id, entity_type, entity_id, viewed_at) VALUES (?,?,?,?)
         ON CONFLICT(user_id, entity_type, entity_id) DO UPDATE SET viewed_at = excluded.viewed_at`, req.user.id, 'doc', d.id, nowIso());
  }
  const users = userMap();
  const doc = serializeDoc(d, users);
  const relSlugs = doc.related;
  const showAll = can(req.user, 'docs.read_unpublished');
  const related = relSlugs.length ? all(`SELECT slug, title, type, status, summary FROM documents WHERE slug IN (${relSlugs.map(() => '?').join(',')})`, ...relSlugs).filter((x) => showAll || x.status === 'published') : [];
  // Also docs that link to this one
  const backlinks = all("SELECT slug, title, type, status FROM documents WHERE related LIKE ? AND slug != ? LIMIT 10", `%"${d.slug}"%`, d.slug).filter((x) => showAll || x.status === 'published');
  const tplSlugs = doc.templates;
  const templates = tplSlugs.length ? all(`SELECT slug, name, channel, style, status FROM templates WHERE slug IN (${tplSlugs.map(() => '?').join(',')})`, ...tplSlugs).filter((x) => showAll || x.status === 'published') : [];
  const relatedTemplates = all("SELECT slug, name, channel, style, status FROM templates WHERE related LIKE ? AND status = 'published' LIMIT 10", `%"${d.slug}"%`);
  for (const t of relatedTemplates) if (!templates.some((x) => x.slug === t.slug)) templates.push(t);
  const featureDefs = getSetting('features', []);
  const features = doc.features.map((k) => featureDefs.find((f) => f.key === k) || { key: k, name: k, status: 'unconfirmed' });
  const versions = get("SELECT COUNT(*) n FROM versions WHERE entity_type = 'doc' AND entity_id = ?", d.id).n;
  const openFeedback = get("SELECT COUNT(*) n FROM doc_feedback WHERE document_id = ? AND status = 'open' AND kind IN ('outdated','suggestion')", d.id).n;
  const departments = getSetting('departments', []);
  res.json({ doc, path: catPath(d.category_id), related, backlinks, templates, features, versions, open_feedback: openFeedback, department: departments.find((x) => x.key === d.department) || null });
}));

function cleanSections(sections) {
  if (!Array.isArray(sections)) throw bad('Sections are invalid.');
  return sections.slice(0, 60).map((s, i) => {
    const label = str(s.label, 120) || `Section ${i + 1}`;
    return { key: str(s.key, 60) || slugify(label).replace(/-/g, '_'), label, html: sanitizeHtml(s.html || '') };
  });
}

function docPayload(b, existing) {
  const type = existing ? existing.type : oneOf(b.type, DOC_TYPES, null);
  if (!type) throw bad('Invalid document type.');
  const title = 'title' in b ? str(b.title, 200) : existing?.title;
  if (!title || title.length < 3) throw bad('Title is required.');
  let category_id = 'category_id' in b ? (b.category_id ? Number(b.category_id) : null) : existing?.category_id ?? null;
  if (category_id) {
    const c = get('SELECT scope FROM categories WHERE id = ?', category_id);
    if (!c || c.scope !== SCOPE_OF[type]) throw bad('Category does not match this document type.');
  }
  const list = (v, max = 30) => (Array.isArray(v) ? v.map((x) => String(x).trim()).filter(Boolean).slice(0, max) : []);
  return {
    type, title, category_id,
    summary: 'summary' in b ? str(b.summary, 600) || '' : existing?.summary || '',
    sections: 'sections' in b ? JSON.stringify(cleanSections(b.sections)) : existing?.sections || '[]',
    tags: 'tags' in b ? JSON.stringify(list(b.tags)) : existing?.tags || '[]',
    related: 'related' in b ? JSON.stringify(list(b.related)) : existing?.related || '[]',
    templates: 'templates' in b ? JSON.stringify(list(b.templates)) : existing?.templates || '[]',
    features: 'features' in b ? JSON.stringify(list(b.features)) : existing?.features || '[]',
    audience: 'audience' in b ? oneOf(b.audience, ['buyer', 'seller', 'both', 'internal'], 'both') : existing?.audience || 'both',
    priority: 'priority' in b ? oneOf(b.priority, PRIORITIES, 'medium') : existing?.priority || 'medium',
    department: 'department' in b ? str(b.department, 40) : existing?.department ?? null,
    policy_pending: 'policy_pending' in b ? (b.policy_pending ? 1 : 0) : existing?.policy_pending ?? 0,
    ai_visible: 'ai_visible' in b ? (b.ai_visible ? 1 : 0) : existing?.ai_visible ?? 1,
  };
}

export function snapshot(entityType, row, userId, summary) {
  run('INSERT INTO versions(entity_type, entity_id, version, snapshot, change_summary, user_id, created_at) VALUES (?,?,?,?,?,?,?)',
    entityType, row.id, row.version, JSON.stringify(row), summary || null, userId, nowIso());
}

r.post('/docs', h((req, res) => {
  if (!can(req.user, 'docs.edit')) throw forbidden();
  const b = req.body || {};
  const p = docPayload(b, null);
  let status = oneOf(b.status, ['draft', 'review', 'published'], 'draft');
  if (status === 'published' && !canPublishDoc(req.user, p.type)) status = 'review';
  let slug = slugify(b.slug || p.title);
  if (!slug) throw bad('Could not derive a URL slug from the title.');
  let n = 1;
  while (get('SELECT id FROM documents WHERE slug = ?', slug)) slug = `${slugify(b.slug || p.title)}-${++n}`;
  const now = nowIso();
  const id = tx(() => {
    const info = run(`INSERT INTO documents(slug,type,title,category_id,summary,sections,tags,related,templates,features,audience,priority,department,policy_pending,ai_visible,status,version,created_by,updated_by,created_at,updated_at,published_at)
      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,1,?,?,?,?,?)`, slug, p.type, p.title, p.category_id, p.summary, p.sections, p.tags, p.related, p.templates, p.features,
      p.audience, p.priority, p.department, p.policy_pending, p.ai_visible, status, req.user.id, req.user.id, now, now, status === 'published' ? now : null);
    const row = get('SELECT * FROM documents WHERE id = ?', Number(info.lastInsertRowid));
    snapshot('doc', row, req.user.id, str(b.change_summary, 300) || 'Created');
    return row.id;
  });
  audit(req, 'doc.create', 'doc', slug, { type: p.type, status });
  markDirty();
  res.status(201).json(serializeDoc(get('SELECT * FROM documents WHERE id = ?', id)));
}));

r.put('/docs/:slug', h((req, res) => {
  if (!can(req.user, 'docs.edit')) throw forbidden();
  const d = get('SELECT * FROM documents WHERE slug = ?', req.params.slug);
  if (!d) throw notFound();
  const b = req.body || {};
  if (b.expected_version && Number(b.expected_version) !== d.version) {
    throw Object.assign(bad(`Someone else saved a newer version (v${d.version}) while you were editing. Reload to see their changes before saving.`), { status: 409 });
  }
  const p = docPayload(b, d);
  const changeSummary = str(b.change_summary, 300);
  if (!changeSummary) throw bad('Add a short summary of what you changed.');
  // Editing published policy content without approval rights sends it back to review.
  let status = d.status;
  if (d.status === 'published' && !canPublishDoc(req.user, d.type)) status = 'review';
  const now = nowIso();
  tx(() => {
    run(`UPDATE documents SET title=?, category_id=?, summary=?, sections=?, tags=?, related=?, templates=?, features=?, audience=?, priority=?, department=?, policy_pending=?, ai_visible=?,
         status=?, version=version+1, updated_by=?, updated_at=? WHERE id = ?`,
      p.title, p.category_id, p.summary, p.sections, p.tags, p.related, p.templates, p.features, p.audience, p.priority, p.department, p.policy_pending, p.ai_visible,
      status, req.user.id, now, d.id);
    snapshot('doc', get('SELECT * FROM documents WHERE id = ?', d.id), req.user.id, changeSummary);
  });
  audit(req, 'doc.update', 'doc', d.slug, { version: d.version + 1, summary: changeSummary, status });
  markDirty();
  res.json(serializeDoc(get('SELECT * FROM documents WHERE id = ?', d.id)));
}));

r.post('/docs/:slug/status', h((req, res) => {
  const d = get('SELECT * FROM documents WHERE slug = ?', req.params.slug);
  if (!d) throw notFound();
  const to = oneOf(req.body?.status, DOC_STATUSES, null);
  if (!to) throw bad('Invalid status.');
  if (!can(req.user, 'docs.edit')) throw forbidden();
  if (['published', 'archived'].includes(to) && !canPublishDoc(req.user, d.type)) {
    throw forbidden(d.type === 'policy' ? 'Only administrators can publish or archive policies.' : 'You cannot publish documents.');
  }
  if (d.status === to) return res.json({ ok: true });
  const now = nowIso();
  tx(() => {
    run('UPDATE documents SET status = ?, version = version + 1, updated_by = ?, updated_at = ?, published_at = CASE WHEN ? = \'published\' THEN ? ELSE published_at END WHERE id = ?',
      to, req.user.id, now, to, now, d.id);
    snapshot('doc', get('SELECT * FROM documents WHERE id = ?', d.id), req.user.id, `Status: ${d.status} → ${to}${req.body?.note ? ` — ${str(req.body.note, 200)}` : ''}`);
  });
  audit(req, 'doc.status', 'doc', d.slug, { from: d.status, to });
  markDirty();
  res.json({ ok: true });
}));

r.get('/docs/:slug/versions', h((req, res) => {
  if (!can(req.user, 'docs.read_unpublished')) throw forbidden();
  const d = get('SELECT id FROM documents WHERE slug = ?', req.params.slug);
  if (!d) throw notFound();
  const users = userMap();
  res.json(all("SELECT id, version, change_summary, user_id, created_at, snapshot FROM versions WHERE entity_type = 'doc' AND entity_id = ? ORDER BY version DESC, id DESC", d.id)
    .map((v) => ({ ...v, user_name: users.get(v.user_id) || 'System', snapshot: serializeDoc(parseJson(v.snapshot, {})) })));
}));

r.post('/docs/:slug/restore/:versionId', h((req, res) => {
  if (!can(req.user, 'docs.edit')) throw forbidden();
  const d = get('SELECT * FROM documents WHERE slug = ?', req.params.slug);
  if (!d) throw notFound();
  const v = get("SELECT * FROM versions WHERE id = ? AND entity_type = 'doc' AND entity_id = ?", Number(req.params.versionId), d.id);
  if (!v) throw notFound('Version not found.');
  const s = parseJson(v.snapshot, null);
  if (!s) throw bad('Version data is corrupted.');
  const status = d.status === 'published' && !canPublishDoc(req.user, d.type) ? 'review' : d.status;
  const now = nowIso();
  tx(() => {
    run(`UPDATE documents SET title=?, category_id=?, summary=?, sections=?, tags=?, related=?, templates=?, features=?, audience=?, priority=?, department=?, policy_pending=?, ai_visible=?,
         status=?, version=version+1, updated_by=?, updated_at=? WHERE id = ?`,
      s.title, s.category_id, s.summary, s.sections, s.tags, s.related, s.templates, s.features, s.audience, s.priority, s.department, s.policy_pending, s.ai_visible ?? 1, status, req.user.id, now, d.id);
    snapshot('doc', get('SELECT * FROM documents WHERE id = ?', d.id), req.user.id, `Restored version ${v.version}`);
  });
  audit(req, 'doc.restore', 'doc', d.slug, { restored_version: v.version });
  markDirty();
  res.json({ ok: true });
}));

r.delete('/docs/:slug', h((req, res) => {
  if (!can(req.user, 'docs.delete')) throw forbidden();
  const d = get('SELECT * FROM documents WHERE slug = ?', req.params.slug);
  if (!d) throw notFound();
  if (d.status !== 'archived') throw bad('Archive the document before deleting it permanently.');
  tx(() => {
    snapshot('doc', d, req.user.id, 'Deleted permanently');
    run('DELETE FROM documents WHERE id = ?', d.id);
  });
  audit(req, 'doc.delete', 'doc', d.slug, { title: d.title });
  markDirty();
  res.json({ ok: true });
}));

// Feedback ("Was this helpful?", "Report outdated", "Suggest an edit")
r.post('/docs/:slug/feedback', h((req, res) => {
  const d = get('SELECT * FROM documents WHERE slug = ?', req.params.slug);
  if (!d || !canSeeDoc(req.user, d)) throw notFound();
  const kind = oneOf(req.body?.kind, ['helpful', 'not_helpful', 'outdated', 'suggestion'], null);
  if (!kind) throw bad('Invalid feedback.');
  const comment = str(req.body?.comment, 2000);
  if (['outdated', 'suggestion'].includes(kind) && !comment) throw bad('Please describe what should change.');
  run('INSERT INTO doc_feedback(document_id,user_id,kind,comment,status,created_at) VALUES (?,?,?,?,?,?)', d.id, req.user.id, kind, comment, ['helpful', 'not_helpful'].includes(kind) ? 'done' : 'open', nowIso());
  if (kind === 'helpful') run('UPDATE documents SET helpful_yes = helpful_yes + 1 WHERE id = ?', d.id);
  if (kind === 'not_helpful') run('UPDATE documents SET helpful_no = helpful_no + 1 WHERE id = ?', d.id);
  res.status(201).json({ ok: true });
}));

r.get('/feedback', h((req, res) => {
  if (!can(req.user, 'feedback.manage')) throw forbidden();
  const status = req.query.status || 'open';
  const rows = all(`SELECT f.*, d.slug, d.title, d.type, u.name user_name FROM doc_feedback f JOIN documents d ON d.id = f.document_id LEFT JOIN users u ON u.id = f.user_id
    WHERE f.kind IN ('outdated','suggestion','not_helpful') ${status === 'all' ? '' : 'AND f.status = ?'} ORDER BY f.created_at DESC LIMIT 300`, ...(status === 'all' ? [] : [status]));
  res.json(rows);
}));

r.patch('/feedback/:id', h((req, res) => {
  if (!can(req.user, 'feedback.manage')) throw forbidden();
  const status = oneOf(req.body?.status, ['open', 'done', 'dismissed'], null);
  if (!status) throw bad('Invalid status.');
  run('UPDATE doc_feedback SET status = ?, resolved_by = ?, resolved_at = ? WHERE id = ?', status, req.user.id, nowIso(), Number(req.params.id));
  res.json({ ok: true });
}));

// ================= Templates =================
const CH = ['telegram', 'email', 'chat', 'sms', 'phone', 'any'];
const STY = ['short', 'standard', 'detailed', 'formal', 'friendly'];

function serializeTpl(t, users) {
  return { ...t, tags: parseJson(t.tags, []), related: parseJson(t.related, []), updated_by_name: users?.get(t.updated_by) || null };
}

r.get('/templates', h((req, res) => {
  const { category, channel, style, language, q, status } = req.query;
  const where = [];
  const p = [];
  if (!can(req.user, 'docs.read_unpublished')) where.push("t.status = 'published'");
  else if (status && status !== 'all') { where.push('t.status = ?'); p.push(status); }
  else if (!status) where.push("t.status != 'archived'");
  if (category) { where.push('t.category_id = ?'); p.push(Number(category)); }
  if (channel) { where.push("(t.channel = ? OR t.channel = 'any')"); p.push(String(channel)); }
  if (style) { where.push('t.style = ?'); p.push(String(style)); }
  if (language === 'am') where.push("t.content_am != ''");
  if (language === 'en') where.push("t.content_en != ''");
  if (q) { const like = `%${String(q).replace(/[%_]/g, '')}%`; where.push('(t.name LIKE ? OR t.content_en LIKE ? OR t.content_am LIKE ? OR t.tags LIKE ?)'); p.push(like, like, like, like); }
  const users = userMap();
  const rows = all(`SELECT t.*, c.name category_name FROM templates t LEFT JOIN categories c ON c.id = t.category_id ${where.length ? 'WHERE ' + where.join(' AND ') : ''} ORDER BY c.sort, t.name COLLATE NOCASE`, ...p);
  res.json(rows.map((t) => serializeTpl(t, users)));
}));

r.get('/templates/:slug', h((req, res) => {
  const t = get('SELECT t.*, c.name category_name FROM templates t LEFT JOIN categories c ON c.id = t.category_id WHERE t.slug = ?', req.params.slug);
  if (!t || (t.status !== 'published' && !can(req.user, 'docs.read_unpublished'))) throw notFound();
  const rel = parseJson(t.related, []);
  const related = rel.length ? all(`SELECT slug, title, type FROM documents WHERE status = 'published' AND slug IN (${rel.map(() => '?').join(',')})`, ...rel) : [];
  res.json({ template: serializeTpl(t, userMap()), related });
}));

function tplPayload(b, ex) {
  const name = 'name' in b ? str(b.name, 160) : ex?.name;
  if (!name) throw bad('Template name is required.');
  const content_en = 'content_en' in b ? String(b.content_en || '').slice(0, 10000) : ex?.content_en || '';
  const content_am = 'content_am' in b ? String(b.content_am || '').slice(0, 10000) : ex?.content_am || '';
  if (!content_en.trim() && !content_am.trim()) throw bad('Add the message in at least one language.');
  let category_id = 'category_id' in b ? (b.category_id ? Number(b.category_id) : null) : ex?.category_id ?? null;
  if (category_id && get('SELECT scope FROM categories WHERE id = ?', category_id)?.scope !== 'template') throw bad('Invalid template category.');
  const list = (v) => (Array.isArray(v) ? v.map((x) => String(x).trim()).filter(Boolean).slice(0, 20) : []);
  return {
    name, content_en, content_am, category_id,
    channel: 'channel' in b ? oneOf(b.channel, CH, 'any') : ex?.channel || 'any',
    style: 'style' in b ? oneOf(b.style, STY, 'standard') : ex?.style || 'standard',
    subject_en: 'subject_en' in b ? str(b.subject_en, 200) : ex?.subject_en ?? null,
    subject_am: 'subject_am' in b ? str(b.subject_am, 200) : ex?.subject_am ?? null,
    usage_notes: 'usage_notes' in b ? String(b.usage_notes || '').slice(0, 5000) : ex?.usage_notes || '',
    tags: 'tags' in b ? JSON.stringify(list(b.tags)) : ex?.tags || '[]',
    related: 'related' in b ? JSON.stringify(list(b.related)) : ex?.related || '[]',
  };
}

r.post('/templates', h((req, res) => {
  if (!can(req.user, 'templates.edit')) throw forbidden();
  const p = tplPayload(req.body || {}, null);
  let slug = `tpl-${slugify(req.body?.slug || p.name)}`.replace(/^tpl-tpl-/, 'tpl-');
  let n = 1;
  const base = slug;
  while (get('SELECT id FROM templates WHERE slug = ?', slug)) slug = `${base}-${++n}`;
  const status = oneOf(req.body?.status, ['draft', 'review', 'published'], 'draft');
  const now = nowIso();
  const id = tx(() => {
    const info = run(`INSERT INTO templates(slug,name,category_id,channel,style,subject_en,subject_am,content_en,content_am,usage_notes,tags,related,status,version,created_by,updated_by,created_at,updated_at)
      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,1,?,?,?,?)`, slug, p.name, p.category_id, p.channel, p.style, p.subject_en, p.subject_am, p.content_en, p.content_am, p.usage_notes, p.tags, p.related, status, req.user.id, req.user.id, now, now);
    const row = get('SELECT * FROM templates WHERE id = ?', Number(info.lastInsertRowid));
    snapshot('template', row, req.user.id, 'Created');
    return row.id;
  });
  audit(req, 'template.create', 'template', slug);
  markDirty();
  res.status(201).json(serializeTpl(get('SELECT * FROM templates WHERE id = ?', id)));
}));

r.put('/templates/:slug', h((req, res) => {
  if (!can(req.user, 'templates.edit')) throw forbidden();
  const t = get('SELECT * FROM templates WHERE slug = ?', req.params.slug);
  if (!t) throw notFound();
  const b = req.body || {};
  if (b.expected_version && Number(b.expected_version) !== t.version) throw Object.assign(bad('Someone else saved a newer version. Reload before saving.'), { status: 409 });
  const p = tplPayload(b, t);
  const status = 'status' in b ? oneOf(b.status, DOC_STATUSES, t.status) : t.status;
  tx(() => {
    run(`UPDATE templates SET name=?, category_id=?, channel=?, style=?, subject_en=?, subject_am=?, content_en=?, content_am=?, usage_notes=?, tags=?, related=?, status=?,
         version=version+1, updated_by=?, updated_at=? WHERE id = ?`, p.name, p.category_id, p.channel, p.style, p.subject_en, p.subject_am, p.content_en, p.content_am,
      p.usage_notes, p.tags, p.related, status, req.user.id, nowIso(), t.id);
    snapshot('template', get('SELECT * FROM templates WHERE id = ?', t.id), req.user.id, str(b.change_summary, 300) || 'Edited');
  });
  audit(req, 'template.update', 'template', t.slug, { status });
  markDirty();
  res.json(serializeTpl(get('SELECT * FROM templates WHERE id = ?', t.id)));
}));

r.get('/templates/:slug/versions', h((req, res) => {
  if (!can(req.user, 'docs.read_unpublished')) throw forbidden();
  const t = get('SELECT id FROM templates WHERE slug = ?', req.params.slug);
  if (!t) throw notFound();
  const users = userMap();
  res.json(all("SELECT id, version, change_summary, user_id, created_at, snapshot FROM versions WHERE entity_type = 'template' AND entity_id = ? ORDER BY version DESC, id DESC", t.id)
    .map((v) => ({ ...v, user_name: users.get(v.user_id) || 'System', snapshot: serializeTpl(parseJson(v.snapshot, {})) })));
}));

r.post('/templates/:slug/restore/:versionId', h((req, res) => {
  if (!can(req.user, 'templates.edit')) throw forbidden();
  const t = get('SELECT * FROM templates WHERE slug = ?', req.params.slug);
  if (!t) throw notFound();
  const v = get("SELECT * FROM versions WHERE id = ? AND entity_type = 'template' AND entity_id = ?", Number(req.params.versionId), t.id);
  const s = v && parseJson(v.snapshot, null);
  if (!s) throw notFound('Version not found.');
  tx(() => {
    run(`UPDATE templates SET name=?, category_id=?, channel=?, style=?, subject_en=?, subject_am=?, content_en=?, content_am=?, usage_notes=?, tags=?, related=?, version=version+1, updated_by=?, updated_at=? WHERE id = ?`,
      s.name, s.category_id, s.channel, s.style, s.subject_en, s.subject_am, s.content_en, s.content_am, s.usage_notes, s.tags, s.related, req.user.id, nowIso(), t.id);
    snapshot('template', get('SELECT * FROM templates WHERE id = ?', t.id), req.user.id, `Restored version ${v.version}`);
  });
  audit(req, 'template.restore', 'template', t.slug, { version: v.version });
  markDirty();
  res.json({ ok: true });
}));

r.delete('/templates/:slug', h((req, res) => {
  if (!can(req.user, 'docs.delete')) throw forbidden();
  const t = get('SELECT * FROM templates WHERE slug = ?', req.params.slug);
  if (!t) throw notFound();
  if (t.status !== 'archived') throw bad('Archive the template before deleting it permanently.');
  run('DELETE FROM templates WHERE id = ?', t.id);
  audit(req, 'template.delete', 'template', t.slug);
  markDirty();
  res.json({ ok: true });
}));

// Record that a template was copied (usage stats; optionally onto a ticket timeline)
r.post('/templates/:slug/used', h((req, res) => {
  const t = get('SELECT id, name, slug FROM templates WHERE slug = ?', req.params.slug);
  if (!t) throw notFound();
  run('UPDATE templates SET usage_count = usage_count + 1 WHERE id = ?', t.id);
  res.json({ ok: true });
}));

export default r;
export { PUBLIC_SECTION_BLOCKLIST, serializeDoc };
