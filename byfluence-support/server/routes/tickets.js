import { Router } from 'express';
import { all, get, run, tx, nowIso, parseJson } from '../db.js';
import { can, canViewTicket, canUpdateTicket } from '../permissions.js';
import {
  h, bad, forbidden, notFound, audit, str, oneOf, dueDate, slaFor,
  PRIORITIES, TICKET_STATUSES, OPEN_STATUSES, CHANNELS,
} from '../util.js';

const r = Router();

const MANUAL_STATUSES = ['new', 'open', 'under_review', 'waiting_customer', 'waiting_seller', 'in_progress'];
const CLOSE_TYPES = ['resolved', 'duplicate', 'spam', 'no_response', 'withdrawn', 'out_of_scope', 'other'];

// ---------- helpers ----------
export function addEvent(ticketId, type, data = {}, userId = null, occurredAt = null) {
  const now = nowIso();
  run('INSERT INTO ticket_events(ticket_id,type,data,user_id,occurred_at,created_at) VALUES (?,?,?,?,?,?)',
    ticketId, type, JSON.stringify(data), userId, occurredAt || now, now);
  run('UPDATE tickets SET updated_at = ? WHERE id = ?', now, ticketId);
}

function loadTicket(id) {
  const t = get('SELECT * FROM tickets WHERE id = ? OR number = ?', Number(id) || -1, String(id));
  if (!t) throw notFound('Ticket not found.');
  return t;
}

function userName(id) {
  if (!id) return null;
  return get('SELECT name FROM users WHERE id = ?', id)?.name || null;
}

export function serializeTicket(t, users, cats) {
  const now = Date.now();
  const isOpen = OPEN_STATUSES.includes(t.status);
  const overdue = isOpen && t.due_at && new Date(t.due_at).getTime() < now;
  const u = (id) => (id ? users.get(id) || null : null);
  const c = (id) => (id ? cats.get(id) || null : null);
  return {
    ...t,
    customer_notified: !!t.customer_notified,
    is_demo: !!t.is_demo,
    linked_docs: parseJson(t.linked_docs, []),
    tags: parseJson(t.tags, []),
    assignee: u(t.assignee_id),
    creator: u(t.created_by),
    category: c(t.category_id),
    subcategory: c(t.subcategory_id),
    is_open: isOpen,
    overdue: !!overdue,
  };
}

export function lookups() {
  const users = new Map(all('SELECT id, name, role, department FROM users').map((u) => [u.id, { ...u }]));
  const cats = new Map(all("SELECT id, name, slug, parent_id FROM categories WHERE scope = 'kb'").map((c) => [c.id, { ...c }]));
  return { users, cats };
}

function nextNumber() {
  const row = get("SELECT MAX(CAST(SUBSTR(number, 5) AS INTEGER)) n FROM tickets");
  return `BYF-${String((row?.n || 10000) + 1).padStart(5, '0')}`;
}

function assertView(req, t) { if (!canViewTicket(req.user, t)) throw forbidden('This ticket is not in your queue.'); }
function assertUpdate(req, t) { if (!canUpdateTicket(req.user, t)) throw forbidden('Only the assigned employee or a supervisor can change this ticket.'); }

function validateCategory(categoryId, subcategoryId) {
  const cat = categoryId ? get("SELECT * FROM categories WHERE id = ? AND scope = 'kb' AND parent_id IS NULL", Number(categoryId)) : null;
  if (categoryId && !cat) throw bad('Unknown issue category.');
  const sub = subcategoryId ? get("SELECT * FROM categories WHERE id = ? AND scope = 'kb'", Number(subcategoryId)) : null;
  if (subcategoryId && (!sub || sub.parent_id !== cat?.id)) throw bad('Subcategory does not belong to the selected category.');
  return { category_id: cat?.id ?? null, subcategory_id: sub?.id ?? null };
}

function validEmail(e) { return !e || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e); }
function validPhone(p) { return !p || /^[+\d][\d\s-]{6,19}$/.test(p); }

// ---------- list ----------
r.get('/', h((req, res) => {
  const { view = 'all', q, status, priority, category, assignee, from, to, channel, sort = 'updated', page = 1, pageSize = 50 } = req.query;
  const where = [];
  const p = [];
  const me = req.user.id;
  if (!can(req.user, 'tickets.view_all')) { where.push('(t.assignee_id = ? OR t.created_by = ? OR t.assignee_id IS NULL)'); p.push(me, me); }
  const open = `t.status IN (${OPEN_STATUSES.map(() => '?').join(',')})`;
  switch (view) {
    case 'mine': where.push('t.assignee_id = ?'); p.push(me); break;
    case 'unassigned': where.push('t.assignee_id IS NULL', open); p.push(...OPEN_STATUSES); break;
    case 'open': where.push(open); p.push(...OPEN_STATUSES); break;
    case 'overdue': where.push(open, 't.due_at < ?'); p.push(...OPEN_STATUSES, nowIso()); break;
    case 'high': where.push(open, "t.priority IN ('high','critical')"); p.push(...OPEN_STATUSES); break;
    case 'all': break;
    default: if (TICKET_STATUSES.includes(view)) { where.push('t.status = ?'); p.push(view); }
  }
  if (status) { const s = String(status).split(',').filter((x) => TICKET_STATUSES.includes(x)); if (s.length) { where.push(`t.status IN (${s.map(() => '?').join(',')})`); p.push(...s); } }
  if (priority) { const s = String(priority).split(',').filter((x) => PRIORITIES.includes(x)); if (s.length) { where.push(`t.priority IN (${s.map(() => '?').join(',')})`); p.push(...s); } }
  if (category) { where.push('t.category_id = ?'); p.push(Number(category)); }
  if (channel) { where.push('t.channel = ?'); p.push(String(channel)); }
  if (assignee === 'none') where.push('t.assignee_id IS NULL');
  else if (assignee) { where.push('t.assignee_id = ?'); p.push(Number(assignee)); }
  if (from) { where.push('t.reported_at >= ?'); p.push(new Date(from).toISOString()); }
  if (to) { where.push('t.reported_at < ?'); p.push(new Date(new Date(to).getTime() + 864e5).toISOString()); }
  if (req.query.escalated === '1') where.push('EXISTS (SELECT 1 FROM escalations e WHERE e.ticket_id = t.id)');
  if (req.query.overdue === '1') { where.push(open, 't.due_at < ?'); p.push(...OPEN_STATUSES, nowIso()); }
  if (req.query.demo === '0') where.push('t.is_demo = 0');
  if (q) {
    const like = `%${String(q).trim().replace(/[%_]/g, '')}%`;
    where.push('(t.number LIKE ? OR t.title LIKE ? OR t.customer_name LIKE ? OR t.customer_email LIKE ? OR t.customer_phone LIKE ? OR t.order_ref LIKE ? OR t.transaction_ref LIKE ? OR t.consultation_ref LIKE ? OR t.customer_ref LIKE ? OR t.description LIKE ?)');
    p.push(like, like, like, like, like, like, like, like, like, like);
  }
  const order = {
    updated: 't.updated_at DESC',
    created: 't.reported_at DESC',
    oldest: 't.reported_at ASC',
    priority: "CASE t.priority WHEN 'critical' THEN 0 WHEN 'high' THEN 1 WHEN 'medium' THEN 2 ELSE 3 END, t.due_at ASC",
    due: 'CASE WHEN t.due_at IS NULL THEN 1 ELSE 0 END, t.due_at ASC',
  }[sort] || 't.updated_at DESC';
  const w = where.length ? `WHERE ${where.join(' AND ')}` : '';
  const size = Math.min(Math.max(Number(pageSize) || 50, 1), 500);
  const off = (Math.max(Number(page) || 1, 1) - 1) * size;
  const total = get(`SELECT COUNT(*) n FROM tickets t ${w}`, ...p).n;
  const rows = all(`SELECT t.*, (SELECT COUNT(*) FROM followups f WHERE f.ticket_id = t.id AND f.status = 'pending') pending_followups
                    FROM tickets t ${w} ORDER BY ${order} LIMIT ? OFFSET ?`, ...p, size, off);
  const { users, cats } = lookups();
  res.json({ total, page: Number(page) || 1, pageSize: size, tickets: rows.map((t) => serializeTicket(t, users, cats)) });
}));

// Counts per view (for tabs)
r.get('/counts', h((req, res) => {
  const me = req.user.id;
  const scope = can(req.user, 'tickets.view_all') ? '1=1' : '(assignee_id = ? OR created_by = ? OR assignee_id IS NULL)';
  const sp = can(req.user, 'tickets.view_all') ? [] : [me, me];
  const rows = all(`SELECT status, COUNT(*) n FROM tickets WHERE ${scope} GROUP BY status`, ...sp);
  const out = Object.fromEntries(TICKET_STATUSES.map((s) => [s, 0]));
  let total = 0;
  for (const x of rows) { out[x.status] = x.n; total += x.n; }
  const ph = OPEN_STATUSES.map(() => '?').join(',');
  out.all = total;
  out.mine = get(`SELECT COUNT(*) n FROM tickets WHERE assignee_id = ? AND status IN (${ph})`, me, ...OPEN_STATUSES).n;
  out.unassigned = get(`SELECT COUNT(*) n FROM tickets WHERE assignee_id IS NULL AND status IN (${ph})`, ...OPEN_STATUSES).n;
  out.overdue = get(`SELECT COUNT(*) n FROM tickets WHERE ${scope} AND status IN (${ph}) AND due_at < ?`, ...sp, ...OPEN_STATUSES, nowIso()).n;
  res.json(out);
}));

// ---------- create ----------
r.post('/', h((req, res) => {
  if (!can(req.user, 'tickets.create')) throw forbidden();
  const b = req.body || {};
  const title = str(b.title, 200);
  const customer_name = str(b.customer_name, 120);
  if (!title || title.length < 5) throw bad('Issue title is required (at least 5 characters).');
  if (!customer_name) throw bad('Customer name is required.');
  if (!str(b.description, 10000)) throw bad('Please describe the issue.');
  if (!validEmail(str(b.customer_email))) throw bad('Customer email looks invalid.');
  if (!validPhone(str(b.customer_phone))) throw bad('Customer phone number looks invalid.');
  const { category_id, subcategory_id } = validateCategory(b.category_id, b.subcategory_id);
  const priority = oneOf(b.priority, PRIORITIES, 'medium');
  const reported_at = b.reported_at ? new Date(b.reported_at).toISOString() : nowIso();
  if (Number.isNaN(new Date(reported_at).getTime()) || new Date(reported_at).getTime() > Date.now() + 60e3) throw bad('Date reported cannot be in the future.');
  let assignee_id = b.assignee_id ? Number(b.assignee_id) : req.user.id;
  if (assignee_id !== req.user.id && !can(req.user, 'tickets.assign')) assignee_id = req.user.id;
  if (b.assignee_id === null || b.assignee_id === 'none') assignee_id = null;
  if (assignee_id && !get('SELECT id FROM users WHERE id = ? AND active = 1', assignee_id)) throw bad('Assignee not found.');
  const now = nowIso();
  const linked = Array.isArray(b.linked_docs) ? b.linked_docs.slice(0, 20).map(String) : [];
  const id = tx(() => {
    const number = nextNumber();
    const info = run(`INSERT INTO tickets(number,title,description,category_id,subcategory_id,priority,status,channel,customer_name,customer_ref,customer_email,customer_phone,account_type,language,order_ref,consultation_ref,transaction_ref,assignee_id,created_by,reported_at,due_at,linked_docs,tags,created_at,updated_at)
      VALUES (?,?,?,?,?,?,'new',?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)`,
      number, title, str(b.description, 10000), category_id, subcategory_id, priority, oneOf(b.channel, CHANNELS, 'telegram'),
      customer_name, str(b.customer_ref, 80), str(b.customer_email, 200), str(b.customer_phone, 30),
      oneOf(b.account_type, ['buyer', 'seller', 'both', 'guest'], 'buyer'), oneOf(b.language, ['am', 'en'], 'am'),
      str(b.order_ref, 80), str(b.consultation_ref, 80), str(b.transaction_ref, 120), assignee_id, req.user.id, reported_at,
      dueDate(reported_at, priority), JSON.stringify(linked), JSON.stringify(Array.isArray(b.tags) ? b.tags.slice(0, 10) : []), now, now);
    const tid = Number(info.lastInsertRowid);
    addEvent(tid, 'reported', { channel: oneOf(b.channel, CHANNELS, 'telegram') }, null, reported_at);
    addEvent(tid, 'created', { number, priority }, req.user.id);
    if (assignee_id) addEvent(tid, 'assigned', { to: assignee_id, to_name: userName(assignee_id) }, req.user.id);
    if (str(b.internal_note, 5000)) addEvent(tid, 'note', { text: str(b.internal_note, 5000) }, req.user.id);
    for (const slug of linked) {
      const d = get('SELECT title FROM documents WHERE slug = ?', slug);
      if (d) addEvent(tid, 'doc_linked', { slug, title: d.title }, req.user.id);
    }
    return tid;
  });
  const t = get('SELECT * FROM tickets WHERE id = ?', id);
  audit(req, 'ticket.create', 'ticket', t.number, { priority, category_id });
  const { users, cats } = lookups();
  res.status(201).json(serializeTicket(t, users, cats));
}));

// ---------- detail ----------
r.get('/:id', h((req, res) => {
  const t = loadTicket(req.params.id);
  assertView(req, t);
  const { users, cats } = lookups();
  const events = all('SELECT * FROM ticket_events WHERE ticket_id = ? ORDER BY occurred_at ASC, id ASC', t.id)
    .map((e) => ({ ...e, data: parseJson(e.data, {}), user: e.user_id ? users.get(e.user_id) || null : null }));
  const escalations = all('SELECT * FROM escalations WHERE ticket_id = ? ORDER BY created_at DESC', t.id)
    .map((e) => ({ ...e, assignee: users.get(e.assignee_id) || null, creator: users.get(e.created_by) || null, decider: users.get(e.decided_by) || null }));
  const followups = all('SELECT * FROM followups WHERE ticket_id = ? ORDER BY due_at ASC', t.id)
    .map((f) => ({ ...f, assignee: users.get(f.assignee_id) || null, overdue: f.status === 'pending' && new Date(f.due_at) < new Date() }));
  const attachments = all('SELECT id, filename, mime, size, uploaded_by, created_at FROM attachments WHERE ticket_id = ? ORDER BY created_at DESC', t.id)
    .map((a) => ({ ...a, uploader: users.get(a.uploaded_by) || null }));
  const linked = parseJson(t.linked_docs, []);
  const docs = linked.length ? all(`SELECT slug, title, type FROM documents WHERE slug IN (${linked.map(() => '?').join(',')})`, ...linked) : [];
  // Possible duplicates: other open tickets from the same customer contact
  const dupes = all(`SELECT id, number, title, status FROM tickets WHERE id != ? AND (
      (customer_email IS NOT NULL AND customer_email = ?) OR (customer_phone IS NOT NULL AND customer_phone = ?) OR (customer_ref IS NOT NULL AND customer_ref = ?))
      ORDER BY created_at DESC LIMIT 5`, t.id, t.customer_email, t.customer_phone, t.customer_ref);
  const sla = slaFor(t.priority);
  res.json({
    ticket: serializeTicket(t, users, cats), events, escalations, followups, attachments, docs,
    customer_history: dupes, sla,
    permissions: { update: canUpdateTicket(req.user, t), assign: can(req.user, 'tickets.assign'), reopen: can(req.user, 'tickets.reopen') || canUpdateTicket(req.user, t) },
  });
}));

// ---------- update fields ----------
const EDITABLE = ['title', 'description', 'channel', 'customer_name', 'customer_ref', 'customer_email', 'customer_phone', 'account_type', 'language', 'order_ref', 'consultation_ref', 'transaction_ref'];
r.patch('/:id', h((req, res) => {
  const t = loadTicket(req.params.id);
  const b = req.body || {};
  const claiming = 'assignee_id' in b && Number(b.assignee_id) === req.user.id && t.assignee_id == null;
  if (!claiming) assertUpdate(req, t);
  if (['closed'].includes(t.status) && Object.keys(b).some((k) => k !== 'assignee_id')) throw bad('Closed tickets are read-only. Reopen the ticket to change it.');
  const sets = [];
  const vals = [];
  const changed = [];
  tx(() => {
    for (const k of EDITABLE) {
      if (!(k in b)) continue;
      let v = str(b[k], k === 'description' ? 10000 : 200);
      if (k === 'title' && (!v || v.length < 5)) throw bad('Issue title is required (at least 5 characters).');
      if (k === 'customer_name' && !v) throw bad('Customer name is required.');
      if (k === 'customer_email' && !validEmail(v)) throw bad('Customer email looks invalid.');
      if (k === 'customer_phone' && !validPhone(v)) throw bad('Customer phone number looks invalid.');
      if (k === 'channel') v = oneOf(v, CHANNELS, t.channel);
      if (k === 'language') v = oneOf(v, ['am', 'en'], t.language);
      if (k === 'account_type') v = oneOf(v, ['buyer', 'seller', 'both', 'guest'], t.account_type);
      if ((t[k] ?? null) !== v) { sets.push(`${k} = ?`); vals.push(v); changed.push(k); }
    }
    if ('category_id' in b || 'subcategory_id' in b) {
      const c = validateCategory(b.category_id ?? t.category_id, b.subcategory_id ?? null);
      if (c.category_id !== t.category_id || c.subcategory_id !== t.subcategory_id) {
        sets.push('category_id = ?', 'subcategory_id = ?'); vals.push(c.category_id, c.subcategory_id); changed.push('category');
      }
    }
    if ('priority' in b && b.priority !== t.priority) {
      const p = oneOf(b.priority, PRIORITIES, null);
      if (!p) throw bad('Invalid priority.');
      sets.push('priority = ?', 'due_at = ?');
      vals.push(p, dueDate(t.reopen_count && t.updated_at ? t.reported_at : t.reported_at, p));
      addEvent(t.id, 'priority_changed', { from: t.priority, to: p, reason: str(b.reason, 500) }, req.user.id);
    }
    if ('assignee_id' in b) {
      const to = b.assignee_id == null || b.assignee_id === '' ? null : Number(b.assignee_id);
      if (to !== t.assignee_id) {
        if (!claiming && !can(req.user, 'tickets.assign') && to !== req.user.id) throw forbidden('Only supervisors can assign tickets to other employees.');
        if (to && !get('SELECT id FROM users WHERE id = ? AND active = 1', to)) throw bad('Assignee not found.');
        sets.push('assignee_id = ?'); vals.push(to);
        addEvent(t.id, 'assigned', { from: t.assignee_id, from_name: userName(t.assignee_id), to, to_name: userName(to) }, req.user.id);
      }
    }
    if (changed.length) addEvent(t.id, 'updated', { fields: changed }, req.user.id);
    if (sets.length) run(`UPDATE tickets SET ${sets.join(', ')}, updated_at = ? WHERE id = ?`, ...vals, nowIso(), t.id);
  });
  audit(req, 'ticket.update', 'ticket', t.number, { fields: changed, priority: b.priority, assignee_id: b.assignee_id });
  const { users, cats } = lookups();
  res.json(serializeTicket(get('SELECT * FROM tickets WHERE id = ?', t.id), users, cats));
}));

// ---------- status ----------
r.post('/:id/status', h((req, res) => {
  const t = loadTicket(req.params.id);
  assertUpdate(req, t);
  const to = req.body?.status;
  if (!MANUAL_STATUSES.includes(to)) {
    if (to === 'escalated') throw bad('Use "Escalate" to escalate a ticket so the reason and department are recorded.');
    if (to === 'resolved') throw bad('Use "Resolve" — root cause, actions and resolution must be recorded.');
    if (to === 'closed') throw bad('Use "Close ticket" so the closing reason is recorded.');
    if (to === 'reopened') throw bad('Use "Reopen" and record why the issue is not resolved.');
    throw bad('Invalid status.');
  }
  if (['resolved', 'closed'].includes(t.status)) throw bad('This ticket is resolved/closed. Reopen it first.');
  if (t.status === 'escalated' && get("SELECT COUNT(*) n FROM escalations WHERE ticket_id = ? AND status IN ('open','in_progress')", t.id).n && !can(req.user, 'escalations.manage')) {
    throw bad('This ticket has an open escalation. It moves on when the escalation is decided.');
  }
  if (to === t.status) return res.json({ ok: true });
  run('UPDATE tickets SET status = ?, updated_at = ? WHERE id = ?', to, nowIso(), t.id);
  addEvent(t.id, 'status_changed', { from: t.status, to, reason: str(req.body?.reason, 500) }, req.user.id);
  audit(req, 'ticket.status', 'ticket', t.number, { from: t.status, to });
  res.json({ ok: true });
}));

// ---------- notes & communications ----------
r.post('/:id/notes', h((req, res) => {
  const t = loadTicket(req.params.id);
  assertView(req, t);
  const text = str(req.body?.text, 5000);
  if (!text) throw bad('Note cannot be empty.');
  addEvent(t.id, 'note', { text }, req.user.id);
  res.status(201).json({ ok: true });
}));

r.post('/:id/communications', h((req, res) => {
  const t = loadTicket(req.params.id);
  assertUpdate(req, t);
  const b = req.body || {};
  const summary = str(b.summary, 5000);
  if (!summary) throw bad('Summarize what was communicated.');
  const direction = oneOf(b.direction, ['outbound', 'inbound', 'attempt'], 'outbound');
  const channel = oneOf(b.channel, CHANNELS, t.channel);
  const occurred = b.occurred_at ? new Date(b.occurred_at).toISOString() : nowIso();
  if (new Date(occurred).getTime() > Date.now() + 60e3) throw bad('Communication time cannot be in the future.');
  tx(() => {
    addEvent(t.id, 'communication', { direction, channel, summary, party: oneOf(b.party, ['customer', 'seller', 'department'], 'customer'), template: str(b.template, 120) }, req.user.id, occurred);
    if (direction === 'outbound' && !t.first_response_at && (b.party || 'customer') === 'customer') run('UPDATE tickets SET first_response_at = ? WHERE id = ?', occurred, t.id);
    if (t.status === 'new' && direction !== 'inbound') {
      run("UPDATE tickets SET status = 'open' WHERE id = ?", t.id);
      addEvent(t.id, 'status_changed', { from: 'new', to: 'open', reason: 'First contact recorded' }, req.user.id);
    }
  });
  res.status(201).json({ ok: true });
}));

r.post('/:id/links', h((req, res) => {
  const t = loadTicket(req.params.id);
  assertView(req, t);
  const slug = str(req.body?.slug, 120);
  const d = slug && get('SELECT slug, title FROM documents WHERE slug = ?', slug);
  if (!d) throw bad('Article not found.');
  const linked = parseJson(t.linked_docs, []);
  if (!linked.includes(slug)) {
    linked.push(slug);
    run('UPDATE tickets SET linked_docs = ? WHERE id = ?', JSON.stringify(linked), t.id);
    addEvent(t.id, 'doc_linked', { slug, title: d.title }, req.user.id);
  }
  res.json({ ok: true, linked });
}));

// ---------- escalation ----------
r.post('/:id/escalations', h((req, res) => {
  const t = loadTicket(req.params.id);
  if (!can(req.user, 'tickets.escalate')) throw forbidden();
  assertUpdate(req, t);
  if (['resolved', 'closed'].includes(t.status)) throw bad('Reopen the ticket before escalating.');
  const b = req.body || {};
  const level = Number(b.level);
  if (![2, 3, 4].includes(level)) throw bad('Choose escalation level 2, 3 or 4.');
  const dept = get("SELECT value FROM settings WHERE key = 'departments'");
  const departments = parseJson(dept?.value, []);
  if (!departments.some((d) => d.key === b.department)) throw bad('Choose the department to escalate to.');
  const reason = str(b.reason, 3000);
  if (!reason || reason.length < 10) throw bad('Explain why the issue is being escalated (at least 10 characters).');
  const assignee = b.assignee_id ? Number(b.assignee_id) : null;
  if (assignee && !get('SELECT id FROM users WHERE id = ? AND active = 1', assignee)) throw bad('Assignee not found.');
  const expected = b.expected_followup_at ? new Date(b.expected_followup_at).toISOString() : null;
  const now = nowIso();
  const eid = tx(() => {
    const info = run(`INSERT INTO escalations(ticket_id,level,department,reason,assignee_id,created_by,status,expected_followup_at,created_at,updated_at)
                      VALUES (?,?,?,?,?,?,'open',?,?,?)`, t.id, level, b.department, reason, assignee, req.user.id, expected, now, now);
    const id = Number(info.lastInsertRowid);
    run("UPDATE tickets SET status = 'escalated', escalation_level = MAX(escalation_level, ?), updated_at = ? WHERE id = ?", level, now, t.id);
    addEvent(t.id, 'escalated', { escalation_id: id, level, department: b.department, reason, assignee_id: assignee, assignee_name: userName(assignee), expected_followup_at: expected, from_status: t.status }, req.user.id);
    if (expected) {
      run("INSERT INTO followups(ticket_id,due_at,reason,assignee_id,status,created_by,created_at) VALUES (?,?,?,?,'pending',?,?)",
        t.id, expected, `Escalation follow-up (level ${level})`, t.assignee_id || req.user.id, req.user.id, now);
    }
    return id;
  });
  audit(req, 'ticket.escalate', 'ticket', t.number, { level, department: b.department, escalation_id: eid });
  res.status(201).json({ ok: true, id: eid });
}));

// ---------- follow-ups ----------
r.post('/:id/followups', h((req, res) => {
  const t = loadTicket(req.params.id);
  assertUpdate(req, t);
  const b = req.body || {};
  const due = new Date(b.due_at);
  if (Number.isNaN(due.getTime())) throw bad('Choose a follow-up date and time.');
  const reason = str(b.reason, 1000);
  if (!reason) throw bad('Add a follow-up reason.');
  const assignee = b.assignee_id ? Number(b.assignee_id) : (t.assignee_id || req.user.id);
  if (assignee !== req.user.id && !can(req.user, 'tickets.assign') && assignee !== t.assignee_id) throw forbidden('Only supervisors can assign follow-ups to others.');
  const info = run("INSERT INTO followups(ticket_id,due_at,reason,assignee_id,status,created_by,created_at) VALUES (?,?,?,?,'pending',?,?)",
    t.id, due.toISOString(), reason, assignee, req.user.id, nowIso());
  addEvent(t.id, 'followup_set', { followup_id: Number(info.lastInsertRowid), due_at: due.toISOString(), reason, assignee_id: assignee, assignee_name: userName(assignee) }, req.user.id);
  res.status(201).json({ ok: true });
}));

// ---------- resolve / close / reopen ----------
r.post('/:id/resolve', h((req, res) => {
  const t = loadTicket(req.params.id);
  assertUpdate(req, t);
  if (['resolved', 'closed'].includes(t.status)) throw bad('Ticket is already resolved.');
  const b = req.body || {};
  const root_cause = str(b.root_cause, 3000);
  const actions_taken = str(b.actions_taken, 5000);
  const resolution = str(b.resolution, 5000);
  if (!root_cause || !actions_taken || !resolution) throw bad('Root cause, actions taken and final resolution are all required before resolving.');
  if (typeof b.customer_notified !== 'boolean') throw bad('Confirm whether the customer has been notified.');
  const openEsc = get("SELECT COUNT(*) n FROM escalations WHERE ticket_id = ? AND status IN ('open','in_progress')", t.id).n;
  if (openEsc) throw bad('This ticket has an open escalation. Record the escalation decision (or cancel it) before resolving.');
  const at = b.resolved_at ? new Date(b.resolved_at).toISOString() : nowIso();
  tx(() => {
    run(`UPDATE tickets SET status = 'resolved', root_cause = ?, actions_taken = ?, resolution = ?, customer_notified = ?, resolved_at = ?, updated_at = ? WHERE id = ?`,
      root_cause, actions_taken, resolution, b.customer_notified ? 1 : 0, at, nowIso(), t.id);
    addEvent(t.id, 'resolved', { root_cause, actions_taken, resolution, customer_notified: b.customer_notified, evidence: str(b.evidence, 2000), from_status: t.status }, req.user.id, at);
    run("UPDATE followups SET status = 'cancelled' WHERE ticket_id = ? AND status = 'pending' AND ? = 1", t.id, b.cancel_followups ? 1 : 0);
  });
  audit(req, 'ticket.resolve', 'ticket', t.number, { customer_notified: b.customer_notified });
  res.json({ ok: true });
}));

r.post('/:id/close', h((req, res) => {
  const t = loadTicket(req.params.id);
  assertUpdate(req, t);
  if (t.status === 'closed') throw bad('Ticket is already closed.');
  const b = req.body || {};
  const type = oneOf(b.close_type, CLOSE_TYPES, null);
  if (!type) throw bad('Choose a closing reason.');
  const note = str(b.note, 2000);
  if (t.status !== 'resolved') {
    if (type === 'resolved') throw bad('This ticket has not been resolved. Resolve it first (record root cause and resolution), or choose another closing reason.');
    if (!note || note.length < 15) throw bad('Closing an unresolved ticket requires a documented explanation (at least 15 characters).');
  }
  const openEsc = get("SELECT COUNT(*) n FROM escalations WHERE ticket_id = ? AND status IN ('open','in_progress')", t.id).n;
  if (openEsc) throw bad('Decide or cancel the open escalation before closing.');
  tx(() => {
    run("UPDATE tickets SET status = 'closed', closed_at = ?, close_reason = ?, updated_at = ? WHERE id = ?", nowIso(), type, nowIso(), t.id);
    run("UPDATE followups SET status = 'cancelled' WHERE ticket_id = ? AND status = 'pending'", t.id);
    addEvent(t.id, 'closed', { close_type: type, note, was_resolved: t.status === 'resolved' }, req.user.id);
  });
  audit(req, 'ticket.close', 'ticket', t.number, { close_type: type, was_resolved: t.status === 'resolved' });
  res.json({ ok: true });
}));

r.post('/:id/reopen', h((req, res) => {
  const t = loadTicket(req.params.id);
  if (!can(req.user, 'tickets.reopen') && !canUpdateTicket(req.user, t)) throw forbidden();
  if (!['resolved', 'closed'].includes(t.status)) throw bad('Only resolved or closed tickets can be reopened.');
  const reason = str(req.body?.reason, 2000);
  if (!reason || reason.length < 10) throw bad('Explain why the ticket is being reopened.');
  const now = nowIso();
  tx(() => {
    run(`UPDATE tickets SET status = 'reopened', reopen_count = reopen_count + 1, resolved_at = NULL, closed_at = NULL, close_reason = NULL,
         due_at = ?, assignee_id = COALESCE(assignee_id, ?), updated_at = ? WHERE id = ?`, dueDate(now, t.priority), req.user.id, now, t.id);
    addEvent(t.id, 'reopened', { reason, previous_status: t.status, previous_resolution: t.resolution }, req.user.id);
  });
  audit(req, 'ticket.reopen', 'ticket', t.number, { reason });
  res.json({ ok: true });
}));

r.post('/:id/csat', h((req, res) => {
  const t = loadTicket(req.params.id);
  assertUpdate(req, t);
  const score = Number(req.body?.score);
  if (!(score >= 1 && score <= 5)) throw bad('Score must be 1–5.');
  run('UPDATE tickets SET csat = ? WHERE id = ?', score, t.id);
  addEvent(t.id, 'csat', { score, comment: str(req.body?.comment, 1000) }, req.user.id);
  res.json({ ok: true });
}));

r.delete('/:id', h((req, res) => {
  const t = loadTicket(req.params.id);
  if (!can(req.user, 'tickets.delete_demo')) throw forbidden();
  if (!t.is_demo) throw bad('Real customer tickets cannot be deleted. Close them instead (history is retained for audit).');
  run('DELETE FROM tickets WHERE id = ?', t.id);
  audit(req, 'ticket.delete_demo', 'ticket', t.number);
  res.json({ ok: true });
}));

export default r;
