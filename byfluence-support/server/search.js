// Global search: an in-memory MiniSearch index (BM25 + fuzzy + prefix) over all
// documentation, templates, announcements and training, plus SQL lookups for tickets.
// Synonyms (editable in Settings) expand customer phrasing into knowledge-base terms.
import MiniSearch from 'minisearch';
import { all, getSetting, parseJson, nowIso } from './db.js';
import { htmlToText } from './util.js';
import { can, canViewTicket } from './permissions.js';

export const DEFAULT_SYNONYMS = [
  ['no show', 'no-show', "didn't join", 'did not join', 'didnt join', 'absent', "didn't come", 'did not attend', 'never showed', 'not show up'],
  ['meeting link', 'meet link', 'google meet', 'link', 'zoom', 'meeting url', 'ሊንክ'],
  ['payment', 'paid', 'pay', 'money', 'deducted', 'charged', 'debited', 'transaction', 'ክፍያ', 'ገንዘብ', 'ከፈልኩ'],
  ['refund', 'money back', 'return money', 'reimburse', 'ተመላሽ', 'ገንዘቤን'],
  ['cancel', 'cancellation', 'cancelled', 'canceled', 'call off', 'ሰርዝ'],
  ['reschedule', 'change time', 'move booking', 'postpone', 'another time'],
  ['login', 'log in', 'sign in', 'signin', "can't access", 'cannot access', 'ግባ'],
  ['password', 'forgot password', 'reset password', 'passcode', 'ይለፍ ቃል'],
  ['otp', 'verification code', 'code', 'sms code', 'one time password', 'ኮድ'],
  ['withdrawal', 'withdraw', 'payout', 'cash out', 'get paid', 'earnings', 'transfer to bank'],
  ['compromise', 'hacked', 'stolen account', 'unauthorized access', 'someone logged in', 'takeover'],
  ['fraud', 'scam', 'fake', 'cheat', 'stolen', 'ማጭበርበር'],
  ['delivery', 'shipping', 'courier', 'deliver', 'not arrived', 'ማድረስ'],
  ['error', 'bug', 'broken', 'not working', 'crash', 'glitch', "doesn't work"],
  ['booking', 'appointment', 'session', 'reservation', 'consultation', 'ቀጠሮ', 'ምክክር'],
  ['seller', 'consultant', 'expert', 'professional', 'vendor', 'coach', 'ሻጭ', 'አማካሪ'],
  ['buyer', 'customer', 'client', 'ገዢ'],
  ['slow', 'loading', 'lag', 'takes long', 'not loading'],
  ['verification', 'verify', 'kyc', 'id check', 'identity'],
  ['pending', 'stuck', 'processing', 'waiting', 'not confirmed'],
  ['duplicate', 'twice', 'double charged', 'charged two times', 'two payments'],
  ['damaged', 'broken item', 'cracked', 'defective'],
  ['wrong item', 'wrong product', 'different item', 'not what i ordered'],
  ['download', 'file', 'ebook', 'pdf', 'digital'],
  ['suspended', 'blocked', 'banned', 'restricted', 'disabled'],
  ['time zone', 'timezone', 'wrong time', 'ethiopian time', 'local time', 'eat'],
];

const STOP = new Set(['the', 'a', 'an', 'is', 'are', 'was', 'i', 'my', 'me', 'to', 'of', 'and', 'or', 'for', 'in', 'on', 'it', 'but', 'with', 'how', 'do', 'does', 'can', 'what', 'why', 'customer', 'user', 'please', 'help']);

let index = null;
let dirty = true;
let builtAt = null;

function build() {
  const ms = new MiniSearch({
    idField: 'uid',
    fields: ['title', 'tags', 'summary', 'body'],
    storeFields: ['uid', 'kind', 'eid', 'slug', 'title', 'summary', 'status', 'category', 'subtype', 'extra'],
    processTerm: (t) => {
      const term = t.toLowerCase();
      return STOP.has(term) ? null : term;
    },
    tokenize: (s) => s.split(/[\s\-–—_.,;:!?()[\]{}"'/\\|<>@#$%^&*+=~`፡።፣፤፥፦]+/u).filter(Boolean),
    searchOptions: {
      boost: { title: 4, tags: 3, summary: 2, body: 1 },
      fuzzy: (term) => (term.length > 4 ? 0.2 : term.length > 3 ? 0.1 : false),
      prefix: (term, i, terms) => i === terms.length - 1 && term.length > 2,
      combineWith: 'OR',
    },
  });
  const cats = new Map(all('SELECT id, name, parent_id FROM categories').map((c) => [c.id, c]));
  const catName = (id) => {
    const c = cats.get(id);
    if (!c) return null;
    const p = c.parent_id ? cats.get(c.parent_id) : null;
    return p ? `${p.name} → ${c.name}` : c.name;
  };
  const docs = [];
  for (const d of all('SELECT id, slug, type, title, summary, sections, tags, status, category_id, priority, audience FROM documents')) {
    const sections = parseJson(d.sections, []);
    docs.push({
      uid: `doc:${d.id}`, kind: d.type, eid: d.id, slug: d.slug, title: d.title, summary: d.summary, status: d.status,
      category: catName(d.category_id), subtype: d.type,
      extra: { priority: d.priority, audience: d.audience },
      tags: parseJson(d.tags, []).join(' '),
      body: sections.filter((s) => s.key !== 'internal').map((s) => htmlToText(s.html)).join('\n').slice(0, 20000),
    });
  }
  for (const t of all('SELECT id, slug, name, channel, style, content_en, content_am, usage_notes, tags, status, category_id FROM templates')) {
    docs.push({
      uid: `tpl:${t.id}`, kind: 'template', eid: t.id, slug: t.slug, title: t.name, status: t.status,
      summary: `${t.channel} · ${t.style}`, category: catName(t.category_id), subtype: t.channel,
      extra: { channel: t.channel, style: t.style },
      tags: parseJson(t.tags, []).join(' '),
      body: `${t.content_en}\n${t.content_am}\n${t.usage_notes}`,
    });
  }
  for (const a of all("SELECT id, title, body, priority, status, expires_at FROM announcements WHERE status != 'archived'")) {
    docs.push({ uid: `ann:${a.id}`, kind: 'announcement', eid: a.id, slug: String(a.id), title: a.title, status: a.status, summary: htmlToText(a.body).slice(0, 180), category: 'Announcements', subtype: a.priority, extra: { priority: a.priority, expires_at: a.expires_at }, tags: '', body: htmlToText(a.body) });
  }
  for (const m of all('SELECT id, slug, number, title, objectives, sections FROM training_modules')) {
    docs.push({ uid: `trn:${m.id}`, kind: 'training', eid: m.id, slug: m.slug, title: `Module ${m.number}: ${m.title}`, status: 'published', summary: parseJson(m.objectives, []).slice(0, 2).join(' · '), category: 'Training Center', subtype: 'module', extra: {}, tags: '', body: parseJson(m.sections, []).map((s) => htmlToText(s.html)).join('\n').slice(0, 20000) });
  }
  ms.addAll(docs);
  index = ms;
  dirty = false;
  builtAt = nowIso();
}

export function markDirty() { dirty = true; }
export function ensureIndex() { if (dirty || !index) build(); return index; }
export function indexInfo() { ensureIndex(); return { documents: index.documentCount, builtAt }; }

function synonymsList() {
  return getSetting('search_synonyms', DEFAULT_SYNONYMS);
}

/** Expand the query using synonym groups: if any phrase of a group appears, add the group's terms. */
export function expandQuery(query) {
  const ql = ` ${query.toLowerCase()} `;
  const extra = new Set();
  for (const group of synonymsList()) {
    if (group.some((p) => ql.includes(` ${p.toLowerCase()} `) || (p.length > 4 && ql.includes(p.toLowerCase())))) {
      for (const p of group) for (const w of p.split(/\s+/)) if (w.length > 2 && !STOP.has(w)) extra.add(w);
    }
  }
  return [...extra];
}

const KIND_ORDER = ['article', 'troubleshooting', 'faq', 'template', 'sop', 'policy', 'guide', 'announcement', 'training'];

/**
 * Search everything the user may see.
 * @param {object} user
 * @param {string} query
 * @param {{kinds?: string[], limit?: number, includeUnpublished?: boolean}} opts
 */
export function searchAll(user, query, opts = {}) {
  const ms = ensureIndex();
  const q = String(query || '').trim();
  if (!q) return { results: [], tickets: [], expanded: [] };
  const limit = Math.min(opts.limit || 40, 100);
  const showUnpublished = opts.includeUnpublished && can(user, 'docs.read_unpublished');
  const kinds = opts.kinds?.length ? new Set(opts.kinds) : null;
  const expanded = expandQuery(q);
  const filter = (r) => {
    if (kinds && !kinds.has(r.kind)) return false;
    if (r.kind === 'announcement') return r.status === 'published';
    if (r.status === 'archived') return false;
    if (r.status !== 'published' && !showUnpublished) return false;
    return true;
  };
  const primary = ms.search(q, { filter });
  const scores = new Map(primary.map((r) => [r.uid, r]));
  if (expanded.length) {
    for (const r of ms.search(expanded.join(' '), { filter, fuzzy: false, prefix: false })) {
      const prev = scores.get(r.uid);
      if (prev) prev.score += r.score * 0.35;
      else scores.set(r.uid, { ...r, score: r.score * 0.35 });
    }
  }
  // Bonus when all original terms appear in the title
  const terms = q.toLowerCase().split(/\s+/).filter((t) => t.length > 2 && !STOP.has(t));
  for (const r of scores.values()) {
    const tl = r.title.toLowerCase();
    if (terms.length && terms.every((t) => tl.includes(t))) r.score *= 1.6;
    if (r.kind === 'article' || r.kind === 'troubleshooting') r.score *= 1.1;
  }
  const results = [...scores.values()].sort((a, b) => b.score - a.score).slice(0, limit).map((r) => ({
    kind: r.kind, id: r.eid, slug: r.slug, title: r.title, summary: r.summary, category: r.category, status: r.status,
    extra: r.extra, score: Math.round(r.score * 100) / 100, match: Object.keys(r.match || {}).slice(0, 6),
  }));

  // Tickets: exact-ish lookup by number, customer, email, phone, refs, title
  let tickets = [];
  if (!kinds || kinds.has('ticket')) {
    const like = `%${q.replace(/[%_]/g, '')}%`;
    tickets = all(`SELECT id, number, title, status, priority, customer_name, customer_email, customer_phone, assignee_id, created_by, updated_at
                   FROM tickets WHERE number LIKE ? OR customer_name LIKE ? OR customer_email LIKE ? OR customer_phone LIKE ?
                   OR order_ref LIKE ? OR transaction_ref LIKE ? OR consultation_ref LIKE ? OR customer_ref LIKE ? OR title LIKE ?
                   ORDER BY updated_at DESC LIMIT 30`, like, like, like, like, like, like, like, like, like)
      .filter((t) => canViewTicket(user, t)).slice(0, 10)
      .map((t) => ({ kind: 'ticket', id: t.id, number: t.number, title: t.title, status: t.status, priority: t.priority, customer_name: t.customer_name }));
  }
  return { results, tickets, expanded };
}

/** Instant suggestions: top titles only. */
export function suggest(user, query) {
  const { results, tickets } = searchAll(user, query, { limit: 8 });
  return { results: results.slice(0, 8), tickets: tickets.slice(0, 4) };
}

export { KIND_ORDER };
