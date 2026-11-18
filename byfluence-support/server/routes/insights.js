// Dashboard, reports, search endpoints
import { Router } from 'express';
import { all, get, run, nowIso, parseJson, getSetting } from '../db.js';
import { can } from '../permissions.js';
import { h, forbidden, OPEN_STATUSES, TICKET_STATUSES } from '../util.js';
import { searchAll, suggest, indexInfo } from '../search.js';
import { lookups, serializeTicket } from './tickets.js';

const r = Router();
const ph = (arr) => arr.map(() => '?').join(',');

// ================= Dashboard =================
r.get('/dashboard', h((req, res) => {
  const now = nowIso();
  const me = req.user.id;
  const o = OPEN_STATUSES;
  const count = (sql, ...p) => get(sql, ...p).n;
  const byStatus = Object.fromEntries(TICKET_STATUSES.map((s) => [s, 0]));
  for (const x of all('SELECT status, COUNT(*) n FROM tickets GROUP BY status')) byStatus[x.status] = x.n;
  const total = Object.values(byStatus).reduce((a, b) => a + b, 0);
  const avgRes = get(`SELECT AVG((julianday(resolved_at) - julianday(reported_at)) * 24) h, COUNT(*) n FROM tickets WHERE resolved_at IS NOT NULL AND resolved_at >= ?`,
    new Date(Date.now() - 30 * 864e5).toISOString());
  const avgFirst = get(`SELECT AVG((julianday(first_response_at) - julianday(reported_at)) * 1440) m FROM tickets WHERE first_response_at IS NOT NULL AND reported_at >= ?`,
    new Date(Date.now() - 30 * 864e5).toISOString());
  const stats = {
    total,
    open: count(`SELECT COUNT(*) n FROM tickets WHERE status IN (${ph(o)})`, ...o),
    new: byStatus.new,
    under_review: byStatus.under_review,
    waiting_customer: byStatus.waiting_customer,
    waiting_seller: byStatus.waiting_seller,
    escalated: byStatus.escalated,
    in_progress: byStatus.in_progress,
    reopened: byStatus.reopened,
    resolved: byStatus.resolved,
    closed: byStatus.closed,
    high_priority: count(`SELECT COUNT(*) n FROM tickets WHERE status IN (${ph(o)}) AND priority IN ('high','critical')`, ...o),
    critical: count(`SELECT COUNT(*) n FROM tickets WHERE status IN (${ph(o)}) AND priority = 'critical'`, ...o),
    overdue: count(`SELECT COUNT(*) n FROM tickets WHERE status IN (${ph(o)}) AND due_at < ?`, ...o, now),
    unassigned: count(`SELECT COUNT(*) n FROM tickets WHERE status IN (${ph(o)}) AND assignee_id IS NULL`, ...o),
    mine_open: count(`SELECT COUNT(*) n FROM tickets WHERE status IN (${ph(o)}) AND assignee_id = ?`, ...o, me),
    created_today: count('SELECT COUNT(*) n FROM tickets WHERE reported_at >= ?', new Date(new Date().setHours(0, 0, 0, 0)).toISOString()),
    avg_resolution_hours: avgRes?.h != null ? Math.round(avgRes.h * 10) / 10 : null,
    avg_resolution_sample: avgRes?.n || 0,
    avg_first_response_minutes: avgFirst?.m != null ? Math.round(avgFirst.m) : null,
    demo_tickets: count('SELECT COUNT(*) n FROM tickets WHERE is_demo = 1'),
  };
  const { users, cats } = lookups();
  const visible = can(req.user, 'tickets.view_all') ? '1=1' : '(assignee_id = ? OR created_by = ? OR assignee_id IS NULL)';
  const vp = can(req.user, 'tickets.view_all') ? [] : [me, me];
  const recent = all(`SELECT * FROM tickets WHERE ${visible} ORDER BY reported_at DESC LIMIT 8`, ...vp).map((t) => serializeTicket(t, users, cats));
  const urgent = all(`SELECT * FROM tickets WHERE ${visible} AND status IN (${ph(o)}) AND (priority IN ('critical','high') OR due_at < ?)
    ORDER BY CASE priority WHEN 'critical' THEN 0 WHEN 'high' THEN 1 ELSE 2 END, due_at ASC LIMIT 8`, ...vp, ...o, now).map((t) => serializeTicket(t, users, cats));
  const followups = all(`SELECT f.*, t.number, t.title, t.priority FROM followups f JOIN tickets t ON t.id = f.ticket_id
    WHERE f.status = 'pending' AND f.assignee_id = ? ORDER BY f.due_at ASC LIMIT 10`, me).map((f) => ({ ...f, overdue: new Date(f.due_at) < new Date() }));
  const teamFollowupsOverdue = count("SELECT COUNT(*) n FROM followups WHERE status = 'pending' AND due_at < ?", now);
  const docs = all(`SELECT slug, title, type, status, updated_at, version FROM documents WHERE status = 'published' ORDER BY updated_at DESC LIMIT 6`);
  const announcements = all(`SELECT a.id, a.title, a.priority, a.published_at, a.pinned, a.kind, u.name author,
      EXISTS(SELECT 1 FROM announcement_reads r WHERE r.announcement_id = a.id AND r.user_id = ?) is_read
    FROM announcements a LEFT JOIN users u ON u.id = a.author_id
    WHERE a.status = 'published' AND (a.expires_at IS NULL OR a.expires_at > ?)
    ORDER BY a.pinned DESC, CASE a.priority WHEN 'critical' THEN 0 WHEN 'important' THEN 1 ELSE 2 END, a.published_at DESC LIMIT 5`, me, now)
    .map((a) => ({ ...a, is_read: !!a.is_read, pinned: !!a.pinned }));
  const escalationsOpen = count("SELECT COUNT(*) n FROM escalations WHERE status IN ('open','in_progress')");
  const myEscalations = count("SELECT COUNT(*) n FROM escalations WHERE status IN ('open','in_progress') AND assignee_id = ?", me);
  const training = get(`SELECT (SELECT COUNT(*) FROM training_modules WHERE status = 'published') total,
    (SELECT COUNT(*) FROM training_progress WHERE user_id = ? AND status = 'completed') done`, me);
  const quick = getSetting('quick_links', []);
  const gaps = can(req.user, 'reports.view')
    ? all(`SELECT LOWER(query) q, COUNT(*) n, MAX(created_at) last FROM search_log WHERE results = 0 AND created_at >= ? GROUP BY LOWER(query) ORDER BY n DESC LIMIT 6`, new Date(Date.now() - 30 * 864e5).toISOString())
    : [];
  const feedbackOpen = can(req.user, 'feedback.manage') ? count("SELECT COUNT(*) n FROM doc_feedback WHERE status = 'open' AND kind IN ('outdated','suggestion')") : 0;
  const reviewQueue = can(req.user, 'docs.read_unpublished') ? count("SELECT COUNT(*) n FROM documents WHERE status = 'review'") : 0;
  res.json({ stats, recent, urgent, followups, team_followups_overdue: teamFollowupsOverdue, docs, announcements, escalations_open: escalationsOpen, my_escalations: myEscalations, training, quick_links: quick, search_gaps: gaps, feedback_open: feedbackOpen, review_queue: reviewQueue });
}));

// ================= Reports =================
r.get('/reports', h((req, res) => {
  if (!can(req.user, 'reports.view')) throw forbidden();
  const to = req.query.to ? new Date(new Date(req.query.to).getTime() + 864e5) : new Date(Date.now() + 1000);
  const from = req.query.from ? new Date(req.query.from) : new Date(to.getTime() - 30 * 864e5);
  const F = from.toISOString();
  const T = to.toISOString();
  const demo = req.query.include_demo === '0' ? 'AND t.is_demo = 0' : '';
  const one = (sql, ...p) => get(sql, ...p);
  const created = one(`SELECT COUNT(*) n FROM tickets t WHERE reported_at >= ? AND reported_at < ? ${demo}`, F, T).n;
  const resolved = one(`SELECT COUNT(*) n FROM tickets t WHERE resolved_at >= ? AND resolved_at < ? ${demo}`, F, T).n;
  const closed = one(`SELECT COUNT(*) n FROM tickets t WHERE closed_at >= ? AND closed_at < ? ${demo}`, F, T).n;
  const reopened = one(`SELECT COUNT(*) n FROM ticket_events e JOIN tickets t ON t.id = e.ticket_id WHERE e.type = 'reopened' AND e.occurred_at >= ? AND e.occurred_at < ? ${demo}`, F, T).n;
  const firstResp = one(`SELECT AVG((julianday(first_response_at) - julianday(reported_at)) * 1440) m, COUNT(*) n FROM tickets t WHERE first_response_at IS NOT NULL AND reported_at >= ? AND reported_at < ? ${demo}`, F, T);
  const resTime = one(`SELECT AVG((julianday(resolved_at) - julianday(reported_at)) * 24) h, COUNT(*) n FROM tickets t WHERE resolved_at >= ? AND resolved_at < ? ${demo}`, F, T);
  const escalatedTickets = one(`SELECT COUNT(DISTINCT e.ticket_id) n FROM escalations e JOIN tickets t ON t.id = e.ticket_id WHERE t.reported_at >= ? AND t.reported_at < ? ${demo}`, F, T).n;
  const overdueNow = one(`SELECT COUNT(*) n FROM tickets t WHERE status IN (${ph(OPEN_STATUSES)}) AND due_at < ? ${demo}`, ...OPEN_STATUSES, nowIso()).n;
  const breached = one(`SELECT COUNT(*) n FROM tickets t WHERE resolved_at >= ? AND resolved_at < ? AND resolved_at > due_at ${demo}`, F, T).n;
  const csat = one(`SELECT AVG(csat) a, COUNT(csat) n FROM tickets t WHERE csat IS NOT NULL AND reported_at >= ? AND reported_at < ? ${demo}`, F, T);
  const byCategory = all(`SELECT COALESCE(c.name, 'Uncategorized') name, COUNT(*) n FROM tickets t LEFT JOIN categories c ON c.id = t.category_id WHERE reported_at >= ? AND reported_at < ? ${demo} GROUP BY c.id ORDER BY n DESC`, F, T);
  const topIssues = all(`SELECT COALESCE(s.name, c.name, 'Uncategorized') name, c.name category, COUNT(*) n FROM tickets t LEFT JOIN categories c ON c.id = t.category_id LEFT JOIN categories s ON s.id = t.subcategory_id
    WHERE reported_at >= ? AND reported_at < ? ${demo} GROUP BY t.category_id, t.subcategory_id ORDER BY n DESC LIMIT 10`, F, T);
  const byPriority = all(`SELECT priority name, COUNT(*) n FROM tickets t WHERE reported_at >= ? AND reported_at < ? ${demo} GROUP BY priority`, F, T);
  const byChannel = all(`SELECT channel name, COUNT(*) n FROM tickets t WHERE reported_at >= ? AND reported_at < ? ${demo} GROUP BY channel ORDER BY n DESC`, F, T);
  const byStatus = all(`SELECT status name, COUNT(*) n FROM tickets t WHERE 1=1 ${demo} GROUP BY status`);
  const byEscalationDept = all(`SELECT e.department name, COUNT(*) n FROM escalations e JOIN tickets t ON t.id = e.ticket_id WHERE e.created_at >= ? AND e.created_at < ? ${demo} GROUP BY e.department ORDER BY n DESC`, F, T);
  // Daily series
  const days = [];
  for (let d = new Date(F.slice(0, 10)); d < to && days.length < 370; d = new Date(d.getTime() + 864e5)) days.push(d.toISOString().slice(0, 10));
  const cMap = new Map(all(`SELECT substr(reported_at,1,10) d, COUNT(*) n FROM tickets t WHERE reported_at >= ? AND reported_at < ? ${demo} GROUP BY d`, F, T).map((x) => [x.d, x.n]));
  const rMap = new Map(all(`SELECT substr(resolved_at,1,10) d, COUNT(*) n FROM tickets t WHERE resolved_at >= ? AND resolved_at < ? ${demo} GROUP BY d`, F, T).map((x) => [x.d, x.n]));
  const series = days.map((d) => ({ date: d, created: cMap.get(d) || 0, resolved: rMap.get(d) || 0 }));
  // Agents
  const agents = all(`SELECT u.id, u.name, u.role,
      (SELECT COUNT(*) FROM tickets t WHERE t.assignee_id = u.id AND t.status IN (${ph(OPEN_STATUSES)}) ${demo}) open_now,
      (SELECT COUNT(*) FROM tickets t WHERE t.assignee_id = u.id AND t.status IN (${ph(OPEN_STATUSES)}) AND t.due_at < ? ${demo}) overdue_now,
      (SELECT COUNT(*) FROM ticket_events e JOIN tickets t ON t.id = e.ticket_id WHERE e.type = 'resolved' AND e.user_id = u.id AND e.occurred_at >= ? AND e.occurred_at < ? ${demo}) resolved,
      (SELECT AVG((julianday(t.resolved_at) - julianday(t.reported_at)) * 24) FROM tickets t WHERE t.assignee_id = u.id AND t.resolved_at >= ? AND t.resolved_at < ? ${demo}) avg_resolution_hours,
      (SELECT COUNT(*) FROM escalations e JOIN tickets t ON t.id = e.ticket_id WHERE e.created_by = u.id AND e.created_at >= ? AND e.created_at < ? ${demo}) escalations,
      (SELECT COUNT(*) FROM ticket_events e JOIN tickets t ON t.id = e.ticket_id WHERE e.type = 'reopened' AND t.assignee_id = u.id AND e.occurred_at >= ? AND e.occurred_at < ? ${demo}) reopened,
      (SELECT AVG(t.csat) FROM tickets t WHERE t.assignee_id = u.id AND t.csat IS NOT NULL AND t.reported_at >= ? AND t.reported_at < ? ${demo}) csat
    FROM users u WHERE u.active = 1 ORDER BY u.name`, ...OPEN_STATUSES, ...OPEN_STATUSES, nowIso(), F, T, F, T, F, T, F, T, F, T);
  res.json({
    range: { from: F, to: T },
    summary: {
      created, resolved, closed, reopened, overdue_now: overdueNow, resolved_after_target: breached,
      avg_first_response_minutes: firstResp.m != null ? Math.round(firstResp.m) : null, first_response_sample: firstResp.n,
      avg_resolution_hours: resTime.h != null ? Math.round(resTime.h * 10) / 10 : null, resolution_sample: resTime.n,
      escalation_rate: created ? Math.round((escalatedTickets / created) * 1000) / 10 : null, escalated_tickets: escalatedTickets,
      csat_avg: csat.a != null ? Math.round(csat.a * 100) / 100 : null, csat_count: csat.n,
    },
    byCategory, topIssues, byPriority, byChannel, byStatus, byEscalationDept, series,
    agents: agents.map((a) => ({ ...a, avg_resolution_hours: a.avg_resolution_hours != null ? Math.round(a.avg_resolution_hours * 10) / 10 : null, csat: a.csat != null ? Math.round(a.csat * 10) / 10 : null })),
  });
}));

// ================= Search =================
r.get('/search', h((req, res) => {
  const q = String(req.query.q || '').slice(0, 200);
  const kinds = req.query.kinds ? String(req.query.kinds).split(',') : null;
  const out = searchAll(req.user, q, { kinds, limit: Number(req.query.limit) || 40, includeUnpublished: req.query.unpublished === '1' });
  if (q.trim() && req.query.log !== '0') run('INSERT INTO search_log(user_id, query, results, created_at) VALUES (?,?,?,?)', req.user.id, q.trim(), out.results.length + out.tickets.length, nowIso());
  res.json(out);
}));

r.get('/search/suggest', h((req, res) => {
  res.json(suggest(req.user, String(req.query.q || '').slice(0, 200)));
}));

r.get('/search/meta', h((req, res) => {
  const recent = all('SELECT query, MAX(created_at) at FROM search_log WHERE user_id = ? GROUP BY LOWER(query) ORDER BY at DESC LIMIT 8', req.user.id).map((x) => x.query);
  const popular = all("SELECT slug, title, type, views FROM documents WHERE status = 'published' ORDER BY views DESC LIMIT 8");
  const mine = all(`SELECT d.slug, d.title, d.type FROM doc_views v JOIN documents d ON d.id = v.entity_id AND v.entity_type = 'doc' WHERE v.user_id = ? AND d.status = 'published' ORDER BY v.viewed_at DESC LIMIT 6`, req.user.id);
  res.json({ recent, popular, recently_viewed: mine, index: indexInfo() });
}));

r.get('/search/gaps', h((req, res) => {
  if (!can(req.user, 'reports.view')) throw forbidden();
  res.json(all(`SELECT LOWER(query) q, COUNT(*) n, MAX(created_at) last FROM search_log WHERE results = 0 GROUP BY LOWER(query) ORDER BY n DESC, last DESC LIMIT 100`));
}));

export default r;
export { parseJson };
