#!/usr/bin/env node
// Initialize the database: admin account, settings, taxonomy, all Markdown content, demo data.
//   npm run seed                 first-time setup (refuses if users already exist)
//   npm run seed -- --reset      DELETE the database and start over
//   npm run seed -- --no-demo    skip demo users/tickets/announcements
//   npm run seed -- --content    re-import Markdown content into an existing database
//                                (updates seeded docs/templates/modules that nobody edited in the app)
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const args = new Set(process.argv.slice(2));
const { db, all, get, run, tx, nowIso, setSetting, ROOT, DB_PATH, DATA_DIR } = await import('../db.js');
const { hashPassword } = await import('../auth.js');
const { DEFAULT_SLA } = await import('../util.js');
const { DEFAULT_SYNONYMS } = await import('../search.js');
const { splitBlocks, parseBlock, parseQuiz, list } = await import('../content/parse.js');
const { walk, checkFiles } = await import('../content/check.js');
const { md, mdList, plain } = await import('./markdown.js');
const demo = await import('./demo.js');

const CONTENT = path.join(ROOT, 'content');
const tax = JSON.parse(fs.readFileSync(path.join(CONTENT, 'taxonomy.json'), 'utf8'));
const log = (...a) => console.log(' ', ...a);

if (args.has('--reset')) {
  const tables = all("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'").map((t) => t.name);
  db.exec('PRAGMA foreign_keys = OFF');
  for (const t of tables) db.exec(`DELETE FROM "${t}"`);
  db.exec('PRAGMA foreign_keys = ON');
  fs.rmSync(path.join(DATA_DIR, 'uploads'), { recursive: true, force: true });
  fs.mkdirSync(path.join(DATA_DIR, 'uploads'), { recursive: true });
  console.log('Database cleared.');
}

const contentOnly = args.has('--content');
const hasUsers = get('SELECT COUNT(*) n FROM users').n > 0;
if (hasUsers && !contentOnly) {
  console.error('The database already has users. Use `npm run seed -- --content` to re-import content, or `npm run seed -- --reset` to start over (deletes everything).');
  process.exit(1);
}

// ---------- validate content ----------
const files = walk(CONTENT);
const check = checkFiles(files);
if (check.errors.length) {
  console.warn(`Content has ${check.errors.length} format error(s); affected blocks may be skipped:`);
  for (const e of check.errors.slice(0, 20)) console.warn('   ', e);
}

const now = nowIso();
let adminId;
let adminPassword = null;

// ---------- users & settings ----------
if (!contentOnly) {
  tx(() => {
    const email = (process.env.ADMIN_EMAIL || 'admin@byfluence.local').toLowerCase();
    adminPassword = process.env.ADMIN_PASSWORD || `Byf-${crypto.randomBytes(6).toString('hex')}7`;
    const info = run('INSERT INTO users(name,email,password_hash,role,department,title,active,must_change_password,created_at) VALUES (?,?,?,?,?,?,1,?,?)',
      process.env.ADMIN_NAME || 'System Administrator', email, hashPassword(adminPassword), 'admin', 'management', 'Administrator',
      process.env.ADMIN_PASSWORD ? 0 : 1, now);
    adminId = Number(info.lastInsertRowid);
    setSetting('departments', tax.departments);
    setSetting('features', tax.features);
    setSetting('placeholders', tax.placeholders);
    setSetting('sla', DEFAULT_SLA);
    setSetting('search_synonyms', DEFAULT_SYNONYMS);
    setSetting('training', { pass_score: 80 });
    setSetting('support_info', {
      _note: 'Official channels are not yet confirmed. Fill these in — templates use {{support_channel}}.',
      telegram: '', email: '', phone: '', website: 'https://byfluence.com', hours: '', timezone: 'EAT (UTC+3)',
    });
    setSetting('quick_links', [
      { label: 'Registration issues', icon: 'user-plus', to: '/kb/c/registration' },
      { label: 'Login problems', icon: 'key-round', to: '/kb/c/account-access' },
      { label: 'Payment issues', icon: 'credit-card', to: '/kb/c/payments' },
      { label: 'Refund requests', icon: 'undo-2', to: '/kb/c/refunds-disputes' },
      { label: 'Consultation booking', icon: 'video', to: '/kb/c/consultations' },
      { label: 'Seller verification', icon: 'badge-check', to: '/kb/c/seller-account' },
      { label: 'Order complaints', icon: 'package', to: '/kb/c/physical-products' },
      { label: 'Seller payouts', icon: 'wallet', to: '/kb/c/payouts' },
    ]);
    // Categories
    for (const [scope, cats] of Object.entries(tax.scopes)) {
      cats.forEach((c, i) => {
        const p = run('INSERT INTO categories(scope,parent_id,slug,name,name_am,description,icon,sort,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?)',
          scope, null, c.slug, c.name, c.name_am || null, c.description || null, c.icon || null, i + 1, now, now);
        (c.subcategories || []).forEach((s, j) => run('INSERT INTO categories(scope,parent_id,slug,name,description,sort,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?)',
          scope, Number(p.lastInsertRowid), s.slug, s.name, s.description || null, j + 1, now, now));
      });
    }
  });
  log('Admin account, settings and categories created.');
} else {
  adminId = get("SELECT id FROM users WHERE role = 'admin' ORDER BY id LIMIT 1").id;
}

const catId = (scope, slug, sub) => {
  const c = get('SELECT id FROM categories WHERE scope = ? AND slug = ? AND parent_id IS NULL', scope, slug);
  if (!c) return null;
  if (!sub) return c.id;
  return get('SELECT id FROM categories WHERE parent_id = ? AND slug = ?', c.id, sub)?.id ?? c.id;
};
const SCOPE_OF = { article: 'kb', troubleshooting: 'kb', faq: 'kb', sop: 'sop', policy: 'policy', guide: 'communication' };

// ---------- content ----------
let docs = 0, tpls = 0, mods = 0, skipped = 0, kept = 0;
const errorIds = new Set(check.errors.map((e) => (e.match(/\[([^\]]+)\]/) || [])[1]).filter(Boolean));

function upsert(table, slug, row, entityType) {
  const ex = get(`SELECT * FROM ${table} WHERE slug = ?`, slug);
  if (ex) {
    // Never overwrite something an employee edited in the app.
    const edited = get('SELECT COUNT(*) n FROM versions WHERE entity_type = ? AND entity_id = ? AND user_id IS NOT NULL AND change_summary NOT LIKE ?', entityType, ex.id, 'Imported%').n;
    if (edited) { kept++; return null; }
    const cols = Object.keys(row);
    run(`UPDATE ${table} SET ${cols.map((c) => `${c} = ?`).join(', ')}, version = version + 1, updated_at = ? WHERE id = ?`, ...cols.map((c) => row[c]), now, ex.id);
    const fresh = get(`SELECT * FROM ${table} WHERE id = ?`, ex.id);
    run('INSERT INTO versions(entity_type, entity_id, version, snapshot, change_summary, user_id, created_at) VALUES (?,?,?,?,?,?,?)', entityType, ex.id, fresh.version, JSON.stringify(fresh), 'Imported from seed content (update)', null, now);
    return ex.id;
  }
  const cols = Object.keys(row);
  const info = run(`INSERT INTO ${table}(slug, ${cols.join(', ')}, version, created_at, updated_at) VALUES (?, ${cols.map(() => '?').join(', ')}, 1, ?, ?)`, slug, ...cols.map((c) => row[c]), now, now);
  const id = Number(info.lastInsertRowid);
  const fresh = get(`SELECT * FROM ${table} WHERE id = ?`, id);
  run('INSERT INTO versions(entity_type, entity_id, version, snapshot, change_summary, user_id, created_at) VALUES (?,?,?,?,?,?,?)', entityType, id, 1, JSON.stringify(fresh), 'Imported from seed content', null, now);
  return id;
}

tx(() => {
  for (const file of files) {
    for (const block of splitBlocks(fs.readFileSync(file, 'utf8'))) {
      const d = parseBlock(block);
      const id = d.meta.id;
      if (!id || !d.title || errorIds.has(id)) { skipped++; continue; }
      const sec = Object.fromEntries(d.sections.map((s) => [s.key, s.body]));
      if (d.kind === 'doc') {
        const type = d.meta.type;
        const scope = SCOPE_OF[type];
        if (!scope) { skipped++; continue; }
        const sections = d.sections.filter((s) => s.key !== 'summary').map((s) => ({
          key: s.key, label: s.label,
          // Customer-facing responses keep line breaks exactly (copy-ready)
          html: /^(response|short|followup|answer)_(en|am)$/.test(s.key) ? md(s.body.replace(/\n(?!\n)/g, '  \n')) : md(s.body),
        }));
        upsert('documents', id, {
          type, title: d.title, category_id: catId(scope, d.meta.category, d.meta.subcategory),
          summary: plain(sec.summary || (sec.answer_en || '').split('\n')[0] || '').slice(0, 600),
          sections: JSON.stringify(sections), tags: JSON.stringify(list(d.meta.tags)), related: JSON.stringify(list(d.meta.related)),
          templates: JSON.stringify(list(d.meta.templates)), features: JSON.stringify(list(d.meta.features)),
          audience: d.meta.audience || 'both', priority: d.meta.priority || 'medium', department: d.meta.department || null,
          policy_pending: d.meta.policy_pending === 'yes' ? 1 : 0, ai_visible: d.meta.audience === 'internal' ? 0 : 1,
          status: 'published', created_by: adminId, updated_by: adminId, published_at: now,
        }, 'doc');
        docs++;
      } else if (d.kind === 'template') {
        upsert('templates', id, {
          name: d.title, category_id: catId('template', d.meta.category), channel: d.meta.channel || 'any', style: d.meta.style || 'standard',
          subject_en: sec.subject_en ? plain(sec.subject_en) : null, subject_am: sec.subject_am ? plain(sec.subject_am) : null,
          content_en: plain(sec.message_en || ''), content_am: plain(sec.message_am || ''), usage_notes: md(sec.usage_notes || ''),
          tags: JSON.stringify(list(d.meta.tags)), related: JSON.stringify(list(d.meta.related)), status: 'published',
          created_by: adminId, updated_by: adminId,
        }, 'template');
        tpls++;
      } else if (d.kind === 'module') {
        const sections = d.sections.filter((s) => !['objectives', 'quiz'].includes(s.key)).map((s) => ({ key: s.key, label: s.label, html: md(s.body) }));
        upsert('training_modules', id, {
          number: Number(d.meta.number) || 0, title: d.title, duration: Number(d.meta.duration) || null,
          objectives: JSON.stringify(mdList(sec.objectives)), sections: JSON.stringify(sections), quiz: JSON.stringify(parseQuiz(sec.quiz)),
          status: 'published', updated_by: adminId,
        }, 'training');
        mods++;
      }
    }
  }
});
log(`Content: ${docs} documents, ${tpls} templates, ${mods} training modules imported${skipped ? `, ${skipped} skipped (errors)` : ''}${kept ? `, ${kept} kept (edited in app)` : ''}.`);

// ---------- demo data ----------
if (!contentOnly && !args.has('--no-demo')) {
  const DEMO_PASSWORD = process.env.DEMO_PASSWORD || 'Demo-pass-2026';
  const U = { admin: adminId };
  tx(() => {
    for (const u of demo.DEMO_USERS) {
      const info = run('INSERT INTO users(name,email,password_hash,role,department,title,active,must_change_password,created_at) VALUES (?,?,?,?,?,?,1,0,?)',
        u.name, u.email, hashPassword(DEMO_PASSWORD), u.role, u.department, u.title, now);
      U[u.key] = Number(info.lastInsertRowid);
    }
  });
  const depts = new Map(tax.departments.map((d) => [d.key, d]));
  const { DEFAULT_SLA: SLA } = await import('../util.js');
  const due = (iso, p) => new Date(new Date(iso).getTime() + SLA[p].resolution_hours * 3600e3).toISOString();
  const kbCat = (slug) => get("SELECT id FROM categories WHERE scope = 'kb' AND slug = ? AND parent_id IS NULL", slug)?.id ?? null;
  const kbSub = (cat, slug) => get('SELECT id FROM categories WHERE parent_id = ? AND slug = ?', kbCat(cat), slug)?.id ?? null;
  let n = 10000;
  const ev = (tid, type, data, uid, at) => run('INSERT INTO ticket_events(ticket_id,type,data,user_id,occurred_at,created_at) VALUES (?,?,?,?,?,?)', tid, type, JSON.stringify(data), uid ?? null, at, at);

  function createTicket(spec) {
    const reported = new Date(Date.now() - spec.daysAgo * 864e5);
    const at = (m) => new Date(reported.getTime() + m * 60e3).toISOString();
    const assignee = spec.assignee ? U[spec.assignee] : null;
    const creator = assignee || U.a1;
    const number = `BYF-${String(++n).padStart(5, '0')}`;
    const c = spec.customer;
    const info = run(`INSERT INTO tickets(number,title,description,category_id,subcategory_id,priority,status,channel,customer_name,customer_ref,customer_email,customer_phone,account_type,language,order_ref,consultation_ref,transaction_ref,assignee_id,created_by,reported_at,due_at,linked_docs,is_demo,created_at,updated_at)
      VALUES (?,?,?,?,?,?,'new',?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,1,?,?)`, number, spec.title, spec.description, kbCat(spec.cat), kbSub(spec.cat, spec.sub), spec.priority, spec.channel,
      c.name, `USR-${1000 + n}`, c.email || null, c.phone || null, c.type, c.lang, spec.refs?.order || null, spec.refs?.consultation || null, spec.refs?.transaction || null,
      assignee, creator, reported.toISOString(), due(reported.toISOString(), spec.priority), JSON.stringify(spec.docs || []), at(0), at(0));
    const tid = Number(info.lastInsertRowid);
    ev(tid, 'reported', { channel: spec.channel }, null, at(0));
    ev(tid, 'created', { number, priority: spec.priority, demo: true }, creator, at(2));
    if (assignee) ev(tid, 'assigned', { to: assignee, to_name: get('SELECT name FROM users WHERE id = ?', assignee).name }, creator, at(2));
    for (const slug of spec.docs || []) {
      const d = get('SELECT title FROM documents WHERE slug = ?', slug);
      if (d) ev(tid, 'doc_linked', { slug, title: d.title }, creator, at(3));
    }
    let status = 'new';
    let firstResponse = null;
    let lastEsc = null;
    const setStatus = (to, m, reason) => { ev(tid, 'status_changed', { from: status, to, reason }, assignee || creator, at(m)); status = to; };
    let lastAt = at(3);
    for (const [m, action, p] of spec.flow || []) {
      const when = at(m);
      if (new Date(when) > new Date()) continue; // never create future events
      lastAt = when;
      const who = assignee || creator;
      switch (action) {
        case 'comm': {
          const party = p.party || 'customer';
          ev(tid, 'communication', { direction: p.direction, channel: p.channel || spec.channel, summary: p.summary, party, template: p.template || null }, p.direction === 'inbound' && m === 0 ? null : who, when);
          if (p.direction === 'outbound' && party === 'customer' && !firstResponse) firstResponse = when;
          if (status === 'new' && p.direction !== 'inbound') setStatus('open', m, 'First contact recorded');
          break;
        }
        case 'status': setStatus(p, m); break;
        case 'note': ev(tid, 'note', { text: p }, who, when); break;
        case 'escalate': {
          const exp = p.inMinutes ? at(m + p.inMinutes) : null;
          const e = run(`INSERT INTO escalations(ticket_id,level,department,reason,assignee_id,created_by,status,progress,expected_followup_at,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)`,
            tid, p.level, p.dept, p.reason, U[p.assignee] || null, who, p.progress ? 'in_progress' : 'open', p.progress || null, exp, when, when);
          lastEsc = { id: Number(e.lastInsertRowid), ...p };
          ev(tid, 'escalated', { escalation_id: lastEsc.id, level: p.level, department: p.dept, department_name: depts.get(p.dept)?.name, reason: p.reason, assignee_id: U[p.assignee] || null, assignee_name: p.assignee ? get('SELECT name FROM users WHERE id = ?', U[p.assignee]).name : null, expected_followup_at: exp, from_status: status }, who, when);
          if (p.progress) ev(tid, 'escalation_updated', { escalation_id: lastEsc.id, progress: p.progress, status: 'in_progress' }, U[p.assignee] || who, at(m + 20));
          run('UPDATE tickets SET escalation_level = MAX(escalation_level, ?) WHERE id = ?', p.level, tid);
          status = 'escalated';
          if (exp) run("INSERT INTO followups(ticket_id,due_at,reason,assignee_id,status,created_by,created_at) VALUES (?,?,?,?,'pending',?,?)", tid, exp, `Escalation follow-up (level ${p.level})`, who, who, when);
          break;
        }
        case 'decide': {
          const decider = U[lastEsc.assignee] || U.sup;
          run("UPDATE escalations SET status = 'decided', decision = ?, decided_by = ?, decided_at = ?, updated_at = ? WHERE id = ?", p, decider, when, when, lastEsc.id);
          run("UPDATE followups SET status = 'done', completed_at = ?, completed_by = ? WHERE ticket_id = ? AND status = 'pending' AND reason LIKE 'Escalation follow-up%'", when, decider, tid);
          ev(tid, 'escalation_decided', { escalation_id: lastEsc.id, level: lastEsc.level, department: lastEsc.dept, decision: p }, decider, when);
          setStatus('in_progress', m, 'Escalation decision recorded');
          break;
        }
        case 'followup': {
          const dueAt = at(m + p.inMinutes);
          const f = run("INSERT INTO followups(ticket_id,due_at,reason,assignee_id,status,created_by,created_at) VALUES (?,?,?,?,'pending',?,?)", tid, dueAt, p.reason, who, who, when);
          ev(tid, 'followup_set', { followup_id: Number(f.lastInsertRowid), due_at: dueAt, reason: p.reason, assignee_id: who, assignee_name: get('SELECT name FROM users WHERE id = ?', who).name }, who, when);
          break;
        }
        case 'resolve':
          run('UPDATE tickets SET root_cause = ?, actions_taken = ?, resolution = ?, customer_notified = ?, resolved_at = ? WHERE id = ?', p.root_cause, p.actions, p.resolution, p.notified ? 1 : 0, when, tid);
          ev(tid, 'resolved', { root_cause: p.root_cause, actions_taken: p.actions, resolution: p.resolution, customer_notified: p.notified, from_status: status }, who, when);
          run("UPDATE followups SET status = 'cancelled' WHERE ticket_id = ? AND status = 'pending'", tid);
          status = 'resolved';
          break;
        case 'close': {
          const [type, note] = Array.isArray(p) ? p : [p, null];
          run("UPDATE tickets SET closed_at = ?, close_reason = ? WHERE id = ?", when, type, tid);
          run("UPDATE followups SET status = 'cancelled' WHERE ticket_id = ? AND status = 'pending'", tid);
          ev(tid, 'closed', { close_type: type, note, was_resolved: status === 'resolved' }, who, when);
          status = 'closed';
          break;
        }
        case 'reopen':
          ev(tid, 'reopened', { reason: p, previous_status: status }, who, when);
          run('UPDATE tickets SET resolved_at = NULL, closed_at = NULL, close_reason = NULL, reopen_count = reopen_count + 1, due_at = ? WHERE id = ?', due(when, spec.priority), tid);
          status = 'reopened';
          break;
        case 'csat':
          run('UPDATE tickets SET csat = ? WHERE id = ?', p, tid);
          ev(tid, 'csat', { score: p }, who, when);
          break;
        default: break;
      }
    }
    run('UPDATE tickets SET status = ?, first_response_at = ?, updated_at = ? WHERE id = ?', status, firstResponse, lastAt, tid);
  }

  tx(() => {
    // History first (older numbers)
    demo.HISTORY.forEach(([title, cat, sub, priority, channel], i) => {
      const daysAgo = 14 + ((i * 7) % 16) + (i % 3) * 0.3;
      const agent = ['a1', 'a2', 'a3', 'pay'][i % 4];
      const durMin = { critical: 120, high: 300, medium: 900, low: 600 }[priority] * (1 + (i % 4) * 0.6);
      createTicket({
        title, cat, sub, priority, channel, daysAgo, assignee: agent,
        customer: { name: `Demo customer ${i + 1}`, phone: `0900000${300 + i}`, type: cat.startsWith('sel') || cat === 'payouts' || cat === 'listings' ? 'seller' : 'buyer', lang: i % 3 ? 'am' : 'en' },
        description: `${title}. (Historical demo ticket for reporting.)`,
        flow: [
          [0, 'comm', { direction: 'inbound', summary: 'Customer contacted support.' }],
          [5 + (i % 5) * 9, 'comm', { direction: 'outbound', summary: 'First response sent.' }],
          [durMin, 'resolve', { root_cause: 'See ticket description.', actions: 'Followed the knowledge base article.', resolution: 'Issue resolved and confirmed by customer.', notified: true }],
          [durMin + 30, 'close', 'resolved'],
          ...(i % 3 === 0 ? [] : [[durMin + 31, 'csat', 3 + (i % 3)]]),
        ],
      });
    });
    for (const spec of [...demo.DEMO_TICKETS].sort((a, b) => b.daysAgo - a.daysAgo)) createTicket(spec);
    // Announcements
    for (const a of demo.DEMO_ANNOUNCEMENTS) {
      const pub = new Date(Date.now() - a.daysAgo * 864e5).toISOString();
      const exp = a.expiresInDays ? new Date(Date.now() + a.expiresInDays * 864e5).toISOString() : null;
      run("INSERT INTO announcements(title,body,priority,kind,status,pinned,author_id,published_at,expires_at,is_demo,created_at,updated_at) VALUES (?,?,?,?,'published',?,?,?,?,1,?,?)",
        a.title, a.body, a.priority, a.kind, a.pinned, adminId, pub, exp, pub, pub);
    }
    // Some demo search history (powers "knowledge gaps")
    for (const [q, r] of [['seller didnt join', 6], ['refund pending', 4], ['telebirr not working', 3], ['change seller bank account', 2], ['vat receipt', 0], ['how to export invoice pdf', 0], ['bulk upload products', 0]]) {
      run('INSERT INTO search_log(user_id, query, results, created_at) VALUES (?,?,?,?)', U.a1, q, r, new Date(Date.now() - Math.random() * 5 * 864e5).toISOString());
    }
    // Training progress for demo agents
    const mods2 = all('SELECT id, number FROM training_modules ORDER BY number');
    const progress = { a1: 10, a2: 6, a3: 3, pay: 7, tns: 8, sup: 10 };
    for (const [k, count] of Object.entries(progress)) {
      for (const m of mods2.slice(0, count)) {
        run("INSERT INTO training_progress(user_id,module_id,status,best_score,attempts,started_at,completed_at) VALUES (?,?,'completed',?,?,?,?)",
          U[k], m.id, 80 + ((m.number * 7 + count) % 21), 1 + (m.number % 2), now, now);
      }
    }
  });
  log(`Demo data: ${demo.DEMO_USERS.length} employees, ${demo.HISTORY.length + demo.DEMO_TICKETS.length} tickets, ${demo.DEMO_ANNOUNCEMENTS.length} announcements (all marked DEMO).`);
  log(`Demo employee password: ${DEMO_PASSWORD}  (supervisor@byfluence.local, dawit@byfluence.local, meron@…, yonas@…, payments@…, safety@…)`);
}

if (!contentOnly) {
  console.log('\n✔ Database ready:', DB_PATH);
  console.log(`  Administrator: ${get("SELECT email FROM users WHERE role='admin' ORDER BY id LIMIT 1").email}`);
  if (adminPassword && !process.env.ADMIN_PASSWORD) console.log(`  Temporary password: ${adminPassword}   (you will be asked to change it on first login)`);
} else console.log('\n✔ Content re-imported.');
