// Escalations, follow-ups and attachments
import { Router } from 'express';
import multer from 'multer';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { all, get, run, tx, nowIso, parseJson, UPLOAD_DIR } from '../db.js';
import { can, canViewTicket, canUpdateTicket } from '../permissions.js';
import { h, bad, forbidden, notFound, audit, str, OPEN_STATUSES } from '../util.js';
import { addEvent } from './tickets.js';

const r = Router();

// ===== Escalations =====
r.get('/escalations', h((req, res) => {
  const { status = 'active', level, department, mine } = req.query;
  const where = [];
  const p = [];
  if (status === 'active') where.push("e.status IN ('open','in_progress')");
  else if (status && status !== 'all') { where.push('e.status = ?'); p.push(status); }
  if (level) { where.push('e.level = ?'); p.push(Number(level)); }
  if (department) { where.push('e.department = ?'); p.push(String(department)); }
  if (mine === '1') { where.push('(e.assignee_id = ? OR e.created_by = ?)'); p.push(req.user.id, req.user.id); }
  if (!can(req.user, 'escalations.manage') && !can(req.user, 'tickets.view_all')) {
    where.push('(e.assignee_id = ? OR e.created_by = ? OR t.assignee_id = ?)'); p.push(req.user.id, req.user.id, req.user.id);
  }
  const rows = all(`SELECT e.*, t.number, t.title, t.priority, t.status ticket_status, t.customer_name, t.assignee_id ticket_assignee_id
    FROM escalations e JOIN tickets t ON t.id = e.ticket_id ${where.length ? 'WHERE ' + where.join(' AND ') : ''}
    ORDER BY CASE e.status WHEN 'open' THEN 0 WHEN 'in_progress' THEN 1 ELSE 2 END, e.level DESC, e.created_at ASC LIMIT 500`, ...p);
  const users = new Map(all('SELECT id, name, role FROM users').map((u) => [u.id, { ...u }]));
  const now = Date.now();
  res.json(rows.map((e) => ({
    ...e, assignee: users.get(e.assignee_id) || null, creator: users.get(e.created_by) || null, decider: users.get(e.decided_by) || null,
    followup_overdue: ['open', 'in_progress'].includes(e.status) && e.expected_followup_at && new Date(e.expected_followup_at).getTime() < now,
  })));
}));

function loadEscalation(req) {
  const e = get('SELECT * FROM escalations WHERE id = ?', Number(req.params.id));
  if (!e) throw notFound('Escalation not found.');
  const t = get('SELECT * FROM tickets WHERE id = ?', e.ticket_id);
  const allowed = can(req.user, 'escalations.manage') || e.assignee_id === req.user.id;
  return { e, t, allowed };
}

r.patch('/escalations/:id', h((req, res) => {
  const { e, t, allowed } = loadEscalation(req);
  if (!allowed && !(e.created_by === req.user.id && canUpdateTicket(req.user, t))) throw forbidden('Only a supervisor or the person handling the escalation can update it.');
  if (!['open', 'in_progress'].includes(e.status)) throw bad('This escalation is already finished.');
  const b = req.body || {};
  const sets = [];
  const vals = [];
  const data = { escalation_id: e.id };
  if (b.progress) { sets.push('progress = ?'); vals.push(str(b.progress, 3000)); data.progress = str(b.progress, 3000); }
  if (b.status && ['open', 'in_progress'].includes(b.status) && b.status !== e.status) { sets.push('status = ?'); vals.push(b.status); data.status = b.status; }
  if ('assignee_id' in b) {
    if (!can(req.user, 'escalations.manage')) throw forbidden('Only supervisors can reassign escalations.');
    const a = b.assignee_id ? Number(b.assignee_id) : null;
    sets.push('assignee_id = ?'); vals.push(a); data.assignee_name = a ? get('SELECT name FROM users WHERE id = ?', a)?.name : 'Unassigned';
  }
  if (b.expected_followup_at) { sets.push('expected_followup_at = ?'); vals.push(new Date(b.expected_followup_at).toISOString()); data.expected_followup_at = new Date(b.expected_followup_at).toISOString(); }
  if (!sets.length) throw bad('Nothing to update.');
  tx(() => {
    run(`UPDATE escalations SET ${sets.join(', ')}, updated_at = ? WHERE id = ?`, ...vals, nowIso(), e.id);
    addEvent(e.ticket_id, 'escalation_updated', data, req.user.id);
  });
  audit(req, 'escalation.update', 'escalation', e.id, data);
  res.json({ ok: true });
}));

r.post('/escalations/:id/decide', h((req, res) => {
  const { e, allowed } = loadEscalation(req);
  if (!allowed) throw forbidden('Only a supervisor or the person handling the escalation can record its decision.');
  if (!['open', 'in_progress'].includes(e.status)) throw bad('This escalation already has a decision.');
  const decision = str(req.body?.decision, 5000);
  const cancel = req.body?.cancel === true;
  if (!decision || decision.length < 10) throw bad('Record the final decision (at least 10 characters).');
  const now = nowIso();
  tx(() => {
    run('UPDATE escalations SET status = ?, decision = ?, decided_by = ?, decided_at = ?, updated_at = ? WHERE id = ?',
      cancel ? 'cancelled' : 'decided', decision, req.user.id, now, now, e.id);
    addEvent(e.ticket_id, cancel ? 'escalation_cancelled' : 'escalation_decided', { escalation_id: e.id, level: e.level, department: e.department, decision }, req.user.id);
    const stillOpen = get("SELECT COUNT(*) n FROM escalations WHERE ticket_id = ? AND status IN ('open','in_progress')", e.ticket_id).n;
    const t = get('SELECT status FROM tickets WHERE id = ?', e.ticket_id);
    if (!stillOpen && t.status === 'escalated') {
      run("UPDATE tickets SET status = 'in_progress', updated_at = ? WHERE id = ?", now, e.ticket_id);
      addEvent(e.ticket_id, 'status_changed', { from: 'escalated', to: 'in_progress', reason: 'Escalation decision recorded' }, req.user.id);
    }
  });
  audit(req, cancel ? 'escalation.cancel' : 'escalation.decide', 'escalation', e.id, { decision });
  res.json({ ok: true });
}));

// ===== Follow-ups =====
r.get('/followups', h((req, res) => {
  const scope = req.query.scope === 'all' && can(req.user, 'tickets.view_all') ? 'all' : 'mine';
  const status = req.query.status || 'pending';
  const p = [];
  let w = 'WHERE 1=1';
  if (status !== 'all') { w += ' AND f.status = ?'; p.push(status); }
  if (scope === 'mine') { w += ' AND f.assignee_id = ?'; p.push(req.user.id); }
  const rows = all(`SELECT f.*, t.number, t.title, t.priority, t.status ticket_status, t.customer_name FROM followups f JOIN tickets t ON t.id = f.ticket_id ${w} ORDER BY f.due_at ASC LIMIT 300`, ...p);
  const users = new Map(all('SELECT id, name FROM users').map((u) => [u.id, u.name]));
  const now = Date.now();
  res.json(rows.map((f) => ({ ...f, assignee_name: users.get(f.assignee_id) || null, overdue: f.status === 'pending' && new Date(f.due_at).getTime() < now })));
}));

r.patch('/followups/:id', h((req, res) => {
  const f = get('SELECT * FROM followups WHERE id = ?', Number(req.params.id));
  if (!f) throw notFound();
  const t = get('SELECT * FROM tickets WHERE id = ?', f.ticket_id);
  if (f.assignee_id !== req.user.id && !canUpdateTicket(req.user, t)) throw forbidden();
  const b = req.body || {};
  if (b.status && ['done', 'cancelled'].includes(b.status)) {
    if (f.status !== 'pending') throw bad('Follow-up is already finished.');
    run('UPDATE followups SET status = ?, completed_at = ?, completed_by = ? WHERE id = ?', b.status, nowIso(), req.user.id, f.id);
    addEvent(f.ticket_id, b.status === 'done' ? 'followup_done' : 'followup_cancelled', { followup_id: f.id, reason: f.reason, note: str(b.note, 1000) }, req.user.id);
  } else if (b.due_at) {
    const due = new Date(b.due_at);
    if (Number.isNaN(due.getTime())) throw bad('Invalid date.');
    run('UPDATE followups SET due_at = ? WHERE id = ?', due.toISOString(), f.id);
    addEvent(f.ticket_id, 'followup_rescheduled', { followup_id: f.id, from: f.due_at, to: due.toISOString() }, req.user.id);
  } else throw bad('Nothing to update.');
  res.json({ ok: true });
}));

// ===== Attachments =====
const ALLOWED = {
  'image/png': '.png', 'image/jpeg': '.jpg', 'image/webp': '.webp', 'image/gif': '.gif',
  'application/pdf': '.pdf', 'text/plain': '.txt',
};
const MAX_MB = Number(process.env.MAX_UPLOAD_MB || 10);
const upload = multer({
  storage: multer.diskStorage({
    destination: UPLOAD_DIR,
    filename: (_req, file, cb) => cb(null, crypto.randomBytes(16).toString('hex') + (ALLOWED[file.mimetype] || '.bin')),
  }),
  limits: { fileSize: MAX_MB * 1024 * 1024, files: 5 },
  fileFilter: (_req, file, cb) => {
    if (ALLOWED[file.mimetype]) cb(null, true);
    else cb(new Error(`File type not allowed (${file.mimetype}). Allowed: PNG, JPG, WEBP, GIF, PDF, TXT.`));
  },
});

// Verify magic bytes so a renamed executable cannot pass as an image/pdf
function sniffOk(filePath, mime) {
  const fd = fs.openSync(filePath, 'r');
  const buf = Buffer.alloc(12);
  fs.readSync(fd, buf, 0, 12, 0);
  fs.closeSync(fd);
  const hex = buf.toString('hex');
  switch (mime) {
    case 'image/png': return hex.startsWith('89504e47');
    case 'image/jpeg': return hex.startsWith('ffd8ff');
    case 'image/gif': return hex.startsWith('47494638');
    case 'image/webp': return hex.startsWith('52494646') && buf.slice(8, 12).toString() === 'WEBP';
    case 'application/pdf': return hex.startsWith('25504446');
    case 'text/plain': return !buf.includes(0);
    default: return false;
  }
}

function handleUpload(req, res, next) {
  upload.array('files', 5)(req, res, (err) => {
    if (err) return res.status(400).json({ error: err.code === 'LIMIT_FILE_SIZE' ? `File too large (max ${MAX_MB} MB).` : err.message });
    next();
  });
}

function saveFiles(req, { ticketId = null, documentId = null, purpose }) {
  const out = [];
  for (const f of req.files || []) {
    if (!sniffOk(f.path, f.mimetype)) { fs.rmSync(f.path, { force: true }); throw bad(`"${f.originalname}" does not look like a valid ${f.mimetype} file.`); }
    const info = run('INSERT INTO attachments(ticket_id,document_id,purpose,filename,stored_name,mime,size,uploaded_by,created_at) VALUES (?,?,?,?,?,?,?,?,?)',
      ticketId, documentId, purpose, path.basename(f.originalname).slice(0, 180), f.filename, f.mimetype, f.size, req.user.id, nowIso());
    out.push({ id: Number(info.lastInsertRowid), filename: f.originalname, mime: f.mimetype, size: f.size, url: `/api/files/${Number(info.lastInsertRowid)}` });
  }
  return out;
}

r.post('/tickets/:id/attachments', handleUpload, h((req, res) => {
  const t = get('SELECT * FROM tickets WHERE id = ? OR number = ?', Number(req.params.id) || -1, String(req.params.id));
  if (!t) throw notFound();
  if (!canUpdateTicket(req.user, t)) { for (const f of req.files || []) fs.rmSync(f.path, { force: true }); throw forbidden(); }
  if (!req.files?.length) throw bad('Choose at least one file.');
  const saved = saveFiles(req, { ticketId: t.id, purpose: 'evidence' });
  for (const a of saved) addEvent(t.id, 'attachment', { attachment_id: a.id, filename: a.filename, size: a.size, description: str(req.body?.description, 300) }, req.user.id);
  audit(req, 'attachment.upload', 'ticket', t.number, { files: saved.map((s) => s.filename) });
  res.status(201).json(saved);
}));

// Images inside documentation (any editor)
r.post('/docs/images', handleUpload, h((req, res) => {
  if (!can(req.user, 'docs.edit') && !can(req.user, 'announcements.manage')) { for (const f of req.files || []) fs.rmSync(f.path, { force: true }); throw forbidden(); }
  if (!req.files?.length) throw bad('Choose an image.');
  for (const f of req.files) if (!f.mimetype.startsWith('image/')) { fs.rmSync(f.path, { force: true }); throw bad('Only images can be inserted into documents.'); }
  res.status(201).json(saveFiles(req, { purpose: 'doc-image' }));
}));

// Authenticated file download — never served statically
r.get('/files/:id', h((req, res) => {
  const a = get('SELECT * FROM attachments WHERE id = ?', Number(req.params.id));
  if (!a) throw notFound();
  if (a.ticket_id) {
    const t = get('SELECT * FROM tickets WHERE id = ?', a.ticket_id);
    if (!t || !canViewTicket(req.user, t)) throw forbidden();
  }
  const p = path.join(UPLOAD_DIR, path.basename(a.stored_name));
  if (!fs.existsSync(p)) throw notFound('File is missing from storage.');
  res.setHeader('Content-Type', a.mime);
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('Cache-Control', 'private, max-age=3600');
  res.setHeader('Content-Disposition', `${a.mime.startsWith('image/') || a.mime === 'application/pdf' ? 'inline' : 'attachment'}; filename="${encodeURIComponent(a.filename)}"`);
  if (a.ticket_id) audit(req, 'attachment.view', 'attachment', a.id, { ticket_id: a.ticket_id });
  fs.createReadStream(p).pipe(res);
}));

r.delete('/files/:id', h((req, res) => {
  const a = get('SELECT * FROM attachments WHERE id = ?', Number(req.params.id));
  if (!a) throw notFound();
  if (!can(req.user, 'tickets.update_all')) throw forbidden('Only supervisors can delete evidence files.');
  run('DELETE FROM attachments WHERE id = ?', a.id);
  fs.rmSync(path.join(UPLOAD_DIR, path.basename(a.stored_name)), { force: true });
  if (a.ticket_id) addEvent(a.ticket_id, 'attachment_removed', { filename: a.filename }, req.user.id);
  audit(req, 'attachment.delete', 'attachment', a.id, { filename: a.filename, ticket_id: a.ticket_id });
  res.json({ ok: true });
}));

export default r;
export { OPEN_STATUSES, parseJson };
