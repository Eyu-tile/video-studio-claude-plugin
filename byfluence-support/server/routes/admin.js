// Auth, users, settings, announcements, training, audit log, backups, API keys
import { Router } from 'express';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { db, all, get, run, tx, nowIso, parseJson, getSetting, setSetting, DATA_DIR } from '../db.js';
import { can, ROLES } from '../permissions.js';
import {
  COOKIE, hashPassword, verifyPassword, validatePassword, createSession, destroySession, publicUser,
  loginThrottle, loginFailed, loginSucceeded, createApiKey,
} from '../auth.js';
import { h, bad, forbidden, notFound, audit, str, oneOf, sanitizeHtml, DEFAULT_SLA } from '../util.js';
import { markDirty, DEFAULT_SYNONYMS } from '../search.js';
import { snapshot } from './content.js';

export const pub = Router();   // no auth required
const r = Router();            // auth required

const secureCookie = process.env.NODE_ENV === 'production' && process.env.COOKIE_SECURE !== 'false';

// ================= Auth =================
pub.post('/auth/login', h((req, res) => {
  const email = str(req.body?.email, 200)?.toLowerCase();
  const password = String(req.body?.password || '');
  if (!email || !password) throw bad('Enter your email and password.');
  const key = `${email}|${req.ip}`;
  const wait = loginThrottle(key);
  if (wait) return res.status(429).json({ error: `Too many attempts. Try again in ${wait} seconds.` });
  const u = get('SELECT * FROM users WHERE email = ?', email);
  if (!u || !u.active || !verifyPassword(password, u.password_hash)) {
    loginFailed(key);
    audit({ ip: req.ip, user: u ? { id: u.id } : null }, 'auth.login_failed', 'user', email);
    throw bad('Email or password is incorrect.');
  }
  loginSucceeded(key);
  const { token, expires } = createSession(u.id, req);
  run('UPDATE users SET last_login_at = ? WHERE id = ?', nowIso(), u.id);
  res.cookie(COOKIE, token, { httpOnly: true, sameSite: 'strict', secure: secureCookie, expires: new Date(expires), path: '/' });
  audit({ ip: req.ip, user: u }, 'auth.login', 'user', u.id);
  res.json({ user: publicUser(get('SELECT * FROM users WHERE id = ?', u.id)) });
}));

pub.post('/auth/logout', h((req, res) => {
  destroySession(req.cookies?.[COOKIE]);
  res.clearCookie(COOKIE, { path: '/' });
  res.json({ ok: true });
}));

r.get('/auth/me', h((req, res) => res.json({ user: publicUser(req.user) })));

r.patch('/me', h((req, res) => {
  const b = req.body || {};
  const prefs = { ...parseJson(req.user.preferences, {}), ...(b.preferences && typeof b.preferences === 'object' ? b.preferences : {}) };
  const name = 'name' in b ? str(b.name, 100) : req.user.name;
  if (!name) throw bad('Name is required.');
  run('UPDATE users SET name = ?, preferences = ? WHERE id = ?', name, JSON.stringify(prefs), req.user.id);
  res.json({ user: publicUser(get('SELECT * FROM users WHERE id = ?', req.user.id)) });
}));

r.post('/me/password', h((req, res) => {
  const { current, next } = req.body || {};
  if (!verifyPassword(String(current || ''), req.user.password_hash)) throw bad('Current password is incorrect.');
  const err = validatePassword(next);
  if (err) throw bad(err);
  if (current === next) throw bad('Choose a new password different from the current one.');
  run('UPDATE users SET password_hash = ?, must_change_password = 0 WHERE id = ?', hashPassword(next), req.user.id);
  // Revoke other sessions
  run('DELETE FROM sessions WHERE user_id = ? AND token_hash != ?', req.user.id, crypto.createHash('sha256').update(req.cookies[COOKIE]).digest('hex'));
  audit(req, 'user.password_change', 'user', req.user.id);
  res.json({ ok: true });
}));

// ================= Users =================
r.get('/users', h((req, res) => {
  const full = can(req.user, 'users.manage');
  const rows = all(`SELECT * FROM users ${full ? '' : 'WHERE active = 1'} ORDER BY active DESC, name`);
  res.json(rows.map((u) => {
    const p = publicUser(u);
    delete p.permissions;
    if (!full) { delete p.last_login_at; delete p.must_change_password; delete p.preferences; }
    return p;
  }));
}));

r.post('/users', h((req, res) => {
  if (!can(req.user, 'users.manage')) throw forbidden();
  const b = req.body || {};
  const name = str(b.name, 100);
  const email = str(b.email, 200)?.toLowerCase();
  if (!name || !email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) throw bad('Name and a valid email are required.');
  if (get('SELECT id FROM users WHERE email = ?', email)) throw bad('A user with this email already exists.');
  const role = oneOf(b.role, Object.keys(ROLES), null);
  if (!role) throw bad('Choose a role.');
  const temp = `Byf-${crypto.randomBytes(5).toString('hex')}9`;
  const info = run('INSERT INTO users(name,email,password_hash,role,department,title,active,must_change_password,created_at) VALUES (?,?,?,?,?,?,1,1,?)',
    name, email, hashPassword(temp), role, str(b.department, 40) || 'support_l1', str(b.title, 100), nowIso());
  audit(req, 'user.create', 'user', info.lastInsertRowid, { email, role });
  res.status(201).json({ user: publicUser(get('SELECT * FROM users WHERE id = ?', Number(info.lastInsertRowid))), temporary_password: temp });
}));

r.patch('/users/:id', h((req, res) => {
  if (!can(req.user, 'users.manage')) throw forbidden();
  const u = get('SELECT * FROM users WHERE id = ?', Number(req.params.id));
  if (!u) throw notFound();
  const b = req.body || {};
  if (u.id === req.user.id && (('role' in b && b.role !== 'admin') || b.active === false)) throw bad('You cannot remove your own administrator access.');
  const role = 'role' in b ? oneOf(b.role, Object.keys(ROLES), u.role) : u.role;
  if (u.role === 'admin' && (role !== 'admin' || b.active === false)) {
    const admins = get("SELECT COUNT(*) n FROM users WHERE role = 'admin' AND active = 1").n;
    if (admins <= 1) throw bad('At least one active administrator is required.');
  }
  run('UPDATE users SET name = ?, role = ?, department = ?, title = ?, active = ? WHERE id = ?',
    'name' in b ? str(b.name, 100) || u.name : u.name, role, 'department' in b ? str(b.department, 40) : u.department,
    'title' in b ? str(b.title, 100) : u.title, 'active' in b ? (b.active ? 1 : 0) : u.active, u.id);
  if (b.active === false) run('DELETE FROM sessions WHERE user_id = ?', u.id);
  audit(req, 'user.update', 'user', u.id, { role, active: b.active });
  res.json({ user: publicUser(get('SELECT * FROM users WHERE id = ?', u.id)) });
}));

r.post('/users/:id/reset-password', h((req, res) => {
  if (!can(req.user, 'users.manage')) throw forbidden();
  const u = get('SELECT * FROM users WHERE id = ?', Number(req.params.id));
  if (!u) throw notFound();
  const temp = `Byf-${crypto.randomBytes(5).toString('hex')}9`;
  run('UPDATE users SET password_hash = ?, must_change_password = 1 WHERE id = ?', hashPassword(temp), u.id);
  run('DELETE FROM sessions WHERE user_id = ?', u.id);
  audit(req, 'user.reset_password', 'user', u.id);
  res.json({ temporary_password: temp });
}));

// ================= Settings =================
const SETTING_KEYS = ['sla', 'departments', 'features', 'quick_links', 'search_synonyms', 'support_info', 'training', 'placeholders'];
const SETTING_DEFAULTS = { sla: DEFAULT_SLA, search_synonyms: DEFAULT_SYNONYMS, training: { pass_score: 80 } };

r.get('/settings', h((req, res) => {
  const out = {};
  for (const k of SETTING_KEYS) out[k] = getSetting(k, SETTING_DEFAULTS[k] ?? null);
  out.roles = ROLES;
  res.json(out);
}));

r.put('/settings/:key', h((req, res) => {
  if (!can(req.user, 'settings.manage')) throw forbidden();
  const key = req.params.key;
  if (!SETTING_KEYS.includes(key)) throw notFound('Unknown setting.');
  const v = req.body?.value;
  if (v === undefined) throw bad('Missing value.');
  // Light validation per key
  if (key === 'sla') {
    for (const p of ['critical', 'high', 'medium', 'low']) {
      const x = v[p];
      if (!x || !(x.first_response_minutes > 0) || !(x.resolution_hours > 0)) throw bad(`SLA for ${p} must have positive first response minutes and resolution hours.`);
    }
  }
  if (key === 'departments' && (!Array.isArray(v) || v.some((d) => !d.key || !d.name || ![1, 2, 3, 4].includes(Number(d.level))))) throw bad('Each department needs key, name and level 1–4.');
  if (key === 'features' && (!Array.isArray(v) || v.some((f) => !f.key || !f.name || !['live', 'beta', 'planned', 'unavailable', 'unconfirmed'].includes(f.status)))) throw bad('Each feature needs key, name and a valid status.');
  if (key === 'search_synonyms' && (!Array.isArray(v) || v.some((g) => !Array.isArray(g)))) throw bad('Synonyms must be a list of groups.');
  const before = getSetting(key, null);
  setSetting(key, v, req.user.id);
  audit(req, 'settings.update', 'setting', key, { before, after: v });
  if (key === 'search_synonyms') markDirty();
  res.json({ ok: true, value: v });
}));

// ================= Announcements =================
r.get('/announcements', h((req, res) => {
  const manage = can(req.user, 'announcements.manage');
  const scope = req.query.scope === 'all' && manage ? 'all' : 'active';
  const now = nowIso();
  const rows = all(`SELECT a.*, u.name author_name, EXISTS(SELECT 1 FROM announcement_reads r WHERE r.announcement_id = a.id AND r.user_id = ?) is_read,
      (SELECT COUNT(*) FROM announcement_reads r WHERE r.announcement_id = a.id) read_count
    FROM announcements a LEFT JOIN users u ON u.id = a.author_id
    ${scope === 'active' ? "WHERE a.status = 'published' AND (a.expires_at IS NULL OR a.expires_at > ?)" : ''}
    ORDER BY a.pinned DESC, COALESCE(a.published_at, a.created_at) DESC`, req.user.id, ...(scope === 'active' ? [now] : []));
  const total = get('SELECT COUNT(*) n FROM users WHERE active = 1').n;
  res.json(rows.map((a) => ({ ...a, is_read: !!a.is_read, pinned: !!a.pinned, is_demo: !!a.is_demo, expired: !!(a.expires_at && a.expires_at <= now), team_size: total })));
}));

function annPayload(b, ex) {
  const title = 'title' in b ? str(b.title, 200) : ex?.title;
  if (!title) throw bad('Title is required.');
  const expires = 'expires_at' in b ? (b.expires_at ? new Date(b.expires_at).toISOString() : null) : ex?.expires_at ?? null;
  if (expires && Number.isNaN(new Date(expires).getTime())) throw bad('Invalid expiration date.');
  return {
    title,
    body: 'body' in b ? sanitizeHtml(b.body) : ex?.body || '',
    priority: 'priority' in b ? oneOf(b.priority, ['normal', 'important', 'critical'], 'normal') : ex?.priority || 'normal',
    kind: 'kind' in b ? oneOf(b.kind, ['update', 'policy', 'feature', 'incident', 'maintenance', 'instruction'], 'update') : ex?.kind || 'update',
    status: 'status' in b ? oneOf(b.status, ['draft', 'published', 'archived'], 'published') : ex?.status || 'published',
    pinned: 'pinned' in b ? (b.pinned ? 1 : 0) : ex?.pinned ?? 0,
    expires_at: expires,
  };
}

r.post('/announcements', h((req, res) => {
  if (!can(req.user, 'announcements.manage')) throw forbidden();
  const p = annPayload(req.body || {}, null);
  const now = nowIso();
  const info = run('INSERT INTO announcements(title,body,priority,kind,status,pinned,author_id,published_at,expires_at,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
    p.title, p.body, p.priority, p.kind, p.status, p.pinned, req.user.id, p.status === 'published' ? now : null, p.expires_at, now, now);
  audit(req, 'announcement.create', 'announcement', info.lastInsertRowid, { title: p.title, priority: p.priority });
  markDirty();
  res.status(201).json({ id: Number(info.lastInsertRowid) });
}));

r.put('/announcements/:id', h((req, res) => {
  if (!can(req.user, 'announcements.manage')) throw forbidden();
  const a = get('SELECT * FROM announcements WHERE id = ?', Number(req.params.id));
  if (!a) throw notFound();
  const p = annPayload(req.body || {}, a);
  const now = nowIso();
  run('UPDATE announcements SET title=?, body=?, priority=?, kind=?, status=?, pinned=?, expires_at=?, published_at = COALESCE(published_at, CASE WHEN ? = \'published\' THEN ? END), updated_at=? WHERE id = ?',
    p.title, p.body, p.priority, p.kind, p.status, p.pinned, p.expires_at, p.status, now, now, a.id);
  if (req.body?.mark_unread_for_all) run('DELETE FROM announcement_reads WHERE announcement_id = ?', a.id);
  audit(req, 'announcement.update', 'announcement', a.id, { status: p.status });
  markDirty();
  res.json({ ok: true });
}));

r.post('/announcements/:id/read', h((req, res) => {
  run('INSERT OR IGNORE INTO announcement_reads(announcement_id, user_id, read_at) VALUES (?,?,?)', Number(req.params.id), req.user.id, nowIso());
  res.json({ ok: true });
}));
r.post('/announcements/read-all', h((req, res) => {
  const now = nowIso();
  for (const a of all("SELECT id FROM announcements WHERE status = 'published'")) run('INSERT OR IGNORE INTO announcement_reads(announcement_id, user_id, read_at) VALUES (?,?,?)', a.id, req.user.id, now);
  res.json({ ok: true });
}));

// ================= Training =================
r.get('/training', h((req, res) => {
  const rows = all(`SELECT m.id, m.slug, m.number, m.title, m.duration, m.objectives, m.status, m.updated_at,
      p.status progress, p.best_score, p.attempts, p.completed_at, json_array_length(m.quiz) questions
    FROM training_modules m LEFT JOIN training_progress p ON p.module_id = m.id AND p.user_id = ?
    ${can(req.user, 'training.edit') ? '' : "WHERE m.status = 'published'"} ORDER BY m.number`, req.user.id);
  res.json({ modules: rows.map((m) => ({ ...m, objectives: parseJson(m.objectives, []) })), pass_score: getSetting('training', { pass_score: 80 }).pass_score });
}));

r.get('/training/team', h((req, res) => {
  if (!can(req.user, 'training.view_team')) throw forbidden();
  const modules = all("SELECT id, number, title FROM training_modules WHERE status = 'published' ORDER BY number");
  const users = all('SELECT id, name, role FROM users WHERE active = 1 ORDER BY name');
  const prog = all('SELECT * FROM training_progress');
  res.json({ modules, users: users.map((u) => ({ ...u, progress: Object.fromEntries(prog.filter((p) => p.user_id === u.id).map((p) => [p.module_id, { status: p.status, best_score: p.best_score, attempts: p.attempts, completed_at: p.completed_at }])) })) });
}));

r.get('/training/:slug', h((req, res) => {
  const m = get('SELECT * FROM training_modules WHERE slug = ?', req.params.slug);
  if (!m) throw notFound();
  const quiz = parseJson(m.quiz, []);
  const editing = req.query.edit === '1' && can(req.user, 'training.edit');
  const p = get('SELECT * FROM training_progress WHERE user_id = ? AND module_id = ?', req.user.id, m.id);
  const prev = get('SELECT slug, title FROM training_modules WHERE number < ? ORDER BY number DESC LIMIT 1', m.number);
  const next = get('SELECT slug, title FROM training_modules WHERE number > ? ORDER BY number ASC LIMIT 1', m.number);
  res.json({
    module: { ...m, objectives: parseJson(m.objectives, []), sections: parseJson(m.sections, []), quiz: editing ? quiz : quiz.map((q) => ({ question: q.question, options: q.options })) },
    progress: p || null, prev, next, pass_score: getSetting('training', { pass_score: 80 }).pass_score,
  });
}));

r.post('/training/:slug/start', h((req, res) => {
  const m = get('SELECT id FROM training_modules WHERE slug = ?', req.params.slug);
  if (!m) throw notFound();
  run("INSERT OR IGNORE INTO training_progress(user_id, module_id, status, attempts, started_at) VALUES (?,?,'in_progress',0,?)", req.user.id, m.id, nowIso());
  res.json({ ok: true });
}));

r.post('/training/:slug/submit', h((req, res) => {
  const m = get('SELECT * FROM training_modules WHERE slug = ?', req.params.slug);
  if (!m) throw notFound();
  const quiz = parseJson(m.quiz, []);
  const answers = Array.isArray(req.body?.answers) ? req.body.answers : [];
  if (answers.length !== quiz.length || answers.some((a) => a == null)) throw bad('Answer every question before submitting.');
  const results = quiz.map((q, i) => ({ correct: Number(answers[i]) === q.answer, answer: q.answer, explanation: q.explanation }));
  const score = quiz.length ? Math.round((results.filter((x) => x.correct).length / quiz.length) * 100) : 100;
  const pass = getSetting('training', { pass_score: 80 }).pass_score;
  const passed = score >= pass;
  const now = nowIso();
  run("INSERT OR IGNORE INTO training_progress(user_id, module_id, status, attempts, started_at) VALUES (?,?,'in_progress',0,?)", req.user.id, m.id, now);
  run(`UPDATE training_progress SET attempts = attempts + 1, best_score = MAX(COALESCE(best_score, 0), ?),
       status = CASE WHEN ? THEN 'completed' ELSE status END, completed_at = CASE WHEN ? AND completed_at IS NULL THEN ? ELSE completed_at END
       WHERE user_id = ? AND module_id = ?`, score, passed ? 1 : 0, passed ? 1 : 0, now, req.user.id, m.id);
  audit(req, 'training.submit', 'training', m.slug, { score, passed });
  res.json({ score, passed, pass_score: pass, results });
}));

r.put('/training/:slug', h((req, res) => {
  if (!can(req.user, 'training.edit')) throw forbidden();
  const m = get('SELECT * FROM training_modules WHERE slug = ?', req.params.slug);
  if (!m) throw notFound();
  const b = req.body || {};
  const title = str(b.title, 200) || m.title;
  const sections = Array.isArray(b.sections) ? b.sections.slice(0, 30).map((s) => ({ key: str(s.key, 60) || 'section', label: str(s.label, 120) || 'Section', html: sanitizeHtml(s.html) })) : parseJson(m.sections, []);
  const objectives = Array.isArray(b.objectives) ? b.objectives.map((o) => str(o, 300)).filter(Boolean).slice(0, 15) : parseJson(m.objectives, []);
  let quiz = parseJson(m.quiz, []);
  if (Array.isArray(b.quiz)) {
    quiz = b.quiz.slice(0, 40).map((q, i) => {
      const options = (q.options || []).map((o) => str(o, 300)).filter(Boolean);
      const answer = Number(q.answer);
      if (!str(q.question, 500) || options.length < 2 || !(answer >= 0 && answer < options.length)) throw bad(`Question ${i + 1} needs text, at least 2 options and a correct answer.`);
      return { question: str(q.question, 500), options, answer, explanation: str(q.explanation, 1000) || '' };
    });
  }
  tx(() => {
    run('UPDATE training_modules SET title = ?, duration = ?, objectives = ?, sections = ?, quiz = ?, status = ?, version = version + 1, updated_by = ?, updated_at = ? WHERE id = ?',
      title, Number(b.duration) || m.duration, JSON.stringify(objectives), JSON.stringify(sections), JSON.stringify(quiz), oneOf(b.status, ['draft', 'published', 'archived'], m.status), req.user.id, nowIso(), m.id);
    snapshot('training', get('SELECT * FROM training_modules WHERE id = ?', m.id), req.user.id, str(b.change_summary, 300) || 'Edited');
  });
  audit(req, 'training.update', 'training', m.slug);
  markDirty();
  res.json({ ok: true });
}));

// ================= Audit log =================
r.get('/audit', h((req, res) => {
  if (!can(req.user, 'audit.view')) throw forbidden();
  const { user, action, entity, from, to, page = 1 } = req.query;
  const w = [];
  const p = [];
  if (user) { w.push('a.user_id = ?'); p.push(Number(user)); }
  if (action) { w.push('a.action LIKE ?'); p.push(`${String(action).replace(/[%_]/g, '')}%`); }
  if (entity) { w.push('(a.entity_type = ? OR a.entity_id = ?)'); p.push(String(entity), String(entity)); }
  if (from) { w.push('a.created_at >= ?'); p.push(new Date(from).toISOString()); }
  if (to) { w.push('a.created_at < ?'); p.push(new Date(new Date(to).getTime() + 864e5).toISOString()); }
  const where = w.length ? `WHERE ${w.join(' AND ')}` : '';
  const total = get(`SELECT COUNT(*) n FROM audit_log a ${where}`, ...p).n;
  const rows = all(`SELECT a.*, u.name user_name FROM audit_log a LEFT JOIN users u ON u.id = a.user_id ${where} ORDER BY a.id DESC LIMIT 100 OFFSET ?`, ...p, (Math.max(Number(page), 1) - 1) * 100);
  res.json({ total, rows: rows.map((x) => ({ ...x, details: parseJson(x.details, {}) })) });
}));

// ================= Backup / data =================
r.get('/admin/backup', h((req, res) => {
  if (!can(req.user, 'backup.download')) throw forbidden();
  const dir = path.join(DATA_DIR, 'backups');
  fs.mkdirSync(dir, { recursive: true });
  const file = path.join(dir, `byfluence-support-${new Date().toISOString().replace(/[:.]/g, '-')}.db`);
  db.exec(`VACUUM INTO '${file.replace(/'/g, "''")}'`);
  audit(req, 'backup.download', 'system', null, { file: path.basename(file) });
  res.download(file, path.basename(file));
}));

r.get('/admin/export', h((req, res) => {
  if (!can(req.user, 'backup.download')) throw forbidden();
  const out = {
    exported_at: nowIso(),
    categories: all('SELECT * FROM categories'),
    documents: all('SELECT * FROM documents'),
    templates: all('SELECT * FROM templates'),
    training_modules: all('SELECT * FROM training_modules'),
    settings: all('SELECT key, value FROM settings'),
  };
  audit(req, 'export.content', 'system');
  res.setHeader('Content-Disposition', `attachment; filename="byfluence-support-content-${nowIso().slice(0, 10)}.json"`);
  res.json(out);
}));

r.get('/admin/stats', h((req, res) => {
  if (!can(req.user, 'settings.manage')) throw forbidden();
  const size = fs.existsSync(path.join(DATA_DIR, 'byfluence-support.db')) ? fs.statSync(path.join(DATA_DIR, 'byfluence-support.db')).size : 0;
  res.json({
    db_bytes: size,
    counts: Object.fromEntries(['users', 'documents', 'templates', 'tickets', 'ticket_events', 'attachments', 'announcements', 'audit_log'].map((t) => [t, get(`SELECT COUNT(*) n FROM ${t}`).n])),
    demo: { tickets: get('SELECT COUNT(*) n FROM tickets WHERE is_demo = 1').n, announcements: get('SELECT COUNT(*) n FROM announcements WHERE is_demo = 1').n },
  });
}));

r.delete('/admin/demo-data', h((req, res) => {
  if (!can(req.user, 'tickets.delete_demo')) throw forbidden();
  if (req.body?.confirm !== 'DELETE DEMO DATA') throw bad('Type DELETE DEMO DATA to confirm.');
  const out = tx(() => ({
    tickets: run('DELETE FROM tickets WHERE is_demo = 1').changes,
    announcements: run('DELETE FROM announcements WHERE is_demo = 1').changes,
  }));
  audit(req, 'demo.delete', 'system', null, out);
  markDirty();
  res.json(out);
}));

// ================= API keys (AI assistant / integrations) =================
r.get('/admin/api-keys', h((req, res) => {
  if (!can(req.user, 'apikeys.manage')) throw forbidden();
  res.json(all('SELECT k.id, k.name, k.prefix, k.scopes, k.created_at, k.last_used_at, k.revoked_at, u.name created_by_name FROM api_keys k LEFT JOIN users u ON u.id = k.created_by ORDER BY k.id DESC')
    .map((k) => ({ ...k, scopes: parseJson(k.scopes, []) })));
}));
r.post('/admin/api-keys', h((req, res) => {
  if (!can(req.user, 'apikeys.manage')) throw forbidden();
  const name = str(req.body?.name, 100);
  if (!name) throw bad('Name the key (e.g. "Telegram AI assistant").');
  const scopes = (Array.isArray(req.body?.scopes) ? req.body.scopes : ['kb:read']).filter((s) => ['kb:read', 'tickets:create'].includes(s));
  if (!scopes.length) throw bad('Choose at least one scope.');
  const k = createApiKey();
  run('INSERT INTO api_keys(name, key_hash, prefix, scopes, created_by, created_at) VALUES (?,?,?,?,?,?)', name, k.hash, k.prefix, JSON.stringify(scopes), req.user.id, nowIso());
  audit(req, 'apikey.create', 'apikey', k.prefix, { name, scopes });
  res.status(201).json({ key: k.raw, prefix: k.prefix });
}));
r.delete('/admin/api-keys/:id', h((req, res) => {
  if (!can(req.user, 'apikeys.manage')) throw forbidden();
  run('UPDATE api_keys SET revoked_at = ? WHERE id = ?', nowIso(), Number(req.params.id));
  audit(req, 'apikey.revoke', 'apikey', req.params.id);
  res.json({ ok: true });
}));

export default r;
