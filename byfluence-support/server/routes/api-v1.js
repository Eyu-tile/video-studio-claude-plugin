// Read-only knowledge API for the future AI assistant (Telegram bot) and other integrations.
// Authenticated with API keys (Settings → Integrations). Exposes ONLY published, AI-visible
// documentation. Internal notes, drafts, tickets and customer data are never returned.
import { Router } from 'express';
import { all, get, run, tx, nowIso, parseJson, getSetting } from '../db.js';
import { apiKeyAuth } from '../auth.js';
import { h, bad, notFound, htmlToText, str, oneOf, dueDate, CHANNELS } from '../util.js';
import { searchAll } from '../search.js';
import { addEvent } from './tickets.js';

const r = Router();
const HIDDEN_SECTIONS = new Set(['internal']);
const SYSTEM = { id: 0, role: 'agent' }; // permission context for search (published only)

function publicDoc(d, { full = true } = {}) {
  const sections = parseJson(d.sections, []).filter((s) => !HIDDEN_SECTIONS.has(s.key));
  const features = getSetting('features', []);
  const docFeatures = parseJson(d.features, []).map((k) => {
    const f = features.find((x) => x.key === k);
    return { key: k, status: f?.status || 'unconfirmed', verified: !!f?.verified };
  });
  return {
    id: d.slug, type: d.type, title: d.title, summary: d.summary, url_path: `/kb/${d.slug}`,
    audience: d.audience, suggested_priority: d.priority, escalation_department: d.department,
    tags: parseJson(d.tags, []), related: parseJson(d.related, []), templates: parseJson(d.templates, []),
    features: docFeatures,
    // When policy_pending is true the assistant must not state a rule — it should hand off to a human.
    policy_pending: !!d.policy_pending,
    requires_human_if: d.policy_pending ? 'Any question about refunds, timelines, fees or exceptions covered by a pending policy.' : null,
    updated_at: d.updated_at, version: d.version,
    ...(full ? { sections: sections.map((s) => ({ key: s.key, label: s.label, text: htmlToText(s.html) })) } : {}),
  };
}

const published = "status = 'published' AND ai_visible = 1";

r.get('/kb/search', apiKeyAuth('kb:read'), h((req, res) => {
  const q = String(req.query.q || '').slice(0, 300);
  if (!q.trim()) throw bad('q is required');
  const limit = Math.min(Number(req.query.limit) || 5, 20);
  const kinds = ['article', 'troubleshooting', 'faq', 'policy', 'guide'];
  const { results } = searchAll(SYSTEM, q, { kinds, limit: limit * 3 });
  const slugs = results.map((x) => x.slug);
  const docs = slugs.length ? all(`SELECT * FROM documents WHERE ${published} AND slug IN (${slugs.map(() => '?').join(',')})`, ...slugs) : [];
  const bySlug = new Map(docs.map((d) => [d.slug, d]));
  res.json({
    query: q,
    results: results.filter((x) => bySlug.has(x.slug)).slice(0, limit).map((x) => ({ score: x.score, ...publicDoc(bySlug.get(x.slug), { full: req.query.full === '1' }) })),
  });
}));

r.get('/kb/docs/:slug', apiKeyAuth('kb:read'), h((req, res) => {
  const d = get(`SELECT * FROM documents WHERE ${published} AND slug = ?`, req.params.slug);
  if (!d) throw notFound();
  res.json(publicDoc(d));
}));

r.get('/kb/faqs', apiKeyAuth('kb:read'), h((req, res) => {
  res.json(all(`SELECT * FROM documents WHERE ${published} AND type = 'faq' ORDER BY title`).map((d) => publicDoc(d)));
}));

r.get('/kb/templates', apiKeyAuth('kb:read'), h((req, res) => {
  const rows = all("SELECT t.*, c.slug category FROM templates t LEFT JOIN categories c ON c.id = t.category_id WHERE t.status = 'published' ORDER BY t.name");
  res.json(rows.map((t) => ({ id: t.slug, name: t.name, category: t.category, channel: t.channel, style: t.style, message_en: t.content_en, message_am: t.content_am, usage_notes: t.usage_notes, updated_at: t.updated_at })));
}));

r.get('/kb/escalation', apiKeyAuth('kb:read'), h((req, res) => {
  res.json({
    departments: getSetting('departments', []).map((d) => ({ key: d.key, name: d.name, level: d.level, description: d.description })),
    features: getSetting('features', []).map((f) => ({ key: f.key, name: f.name, status: f.status, verified: !!f.verified })),
    rules: [
      'Never ask for passwords, OTP codes, PINs or card numbers.',
      'Never promise refunds, timelines, fees or outcomes that are not in a published policy.',
      'Hand off to a human for account-specific investigation, payments, refunds, verification, disputes, fraud and any policy_pending topic.',
    ],
  });
}));

// Ticket creation from an authorized integration (e.g. the AI assistant handing off to a human)
r.post('/tickets', apiKeyAuth('tickets:create'), h((req, res) => {
  const b = req.body || {};
  const title = str(b.title, 200);
  const customer_name = str(b.customer_name, 120);
  const description = str(b.description, 10000);
  if (!title || !customer_name || !description) throw bad('title, customer_name and description are required');
  const cat = b.category ? get("SELECT id FROM categories WHERE scope = 'kb' AND parent_id IS NULL AND slug = ?", String(b.category)) : null;
  const sub = cat && b.subcategory ? get("SELECT id FROM categories WHERE parent_id = ? AND slug = ?", cat.id, String(b.subcategory)) : null;
  const priority = oneOf(b.priority, ['low', 'medium', 'high'], 'medium'); // integrations cannot open critical tickets
  const now = nowIso();
  const out = tx(() => {
    const n = (get("SELECT MAX(CAST(SUBSTR(number, 5) AS INTEGER)) n FROM tickets")?.n || 10000) + 1;
    const number = `BYF-${String(n).padStart(5, '0')}`;
    const info = run(`INSERT INTO tickets(number,title,description,category_id,subcategory_id,priority,status,channel,customer_name,customer_ref,customer_email,customer_phone,account_type,language,order_ref,consultation_ref,transaction_ref,reported_at,due_at,created_at,updated_at)
      VALUES (?,?,?,?,?,?,'new',?,?,?,?,?,?,?,?,?,?,?,?,?,?)`, number, title, description, cat?.id ?? null, sub?.id ?? null, priority, oneOf(b.channel, CHANNELS, 'telegram'),
      customer_name, str(b.customer_ref, 80), str(b.customer_email, 200), str(b.customer_phone, 30), oneOf(b.account_type, ['buyer', 'seller'], 'buyer'), oneOf(b.language, ['am', 'en'], 'am'),
      str(b.order_ref, 80), str(b.consultation_ref, 80), str(b.transaction_ref, 120), now, dueDate(now, priority), now, now);
    const id = Number(info.lastInsertRowid);
    addEvent(id, 'created', { number, priority, via: `integration:${req.apiKey.name}`, conversation_summary: str(b.conversation_summary, 5000) }, null);
    return { id, number };
  });
  res.status(201).json({ ticket: out.number });
}));

export default r;
