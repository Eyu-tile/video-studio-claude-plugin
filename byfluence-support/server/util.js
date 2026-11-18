import sanitizeHtmlLib from 'sanitize-html';
import { run, nowIso, getSetting } from './db.js';

/** Sanitize rich-text HTML coming from the editor. */
export function sanitizeHtml(html) {
  return sanitizeHtmlLib(String(html || ''), {
    allowedTags: ['h1', 'h2', 'h3', 'h4', 'p', 'br', 'hr', 'strong', 'b', 'em', 'i', 'u', 's', 'code', 'pre', 'blockquote',
      'ul', 'ol', 'li', 'a', 'img', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'div', 'span', 'label', 'input', 'mark'],
    allowedAttributes: {
      a: ['href', 'target', 'rel'],
      img: ['src', 'alt', 'title', 'width', 'height'],
      div: ['class', 'data-callout', 'data-type'],
      span: ['class'],
      ul: ['data-type'],
      li: ['data-type', 'data-checked'],
      input: ['type', 'checked', 'disabled'],
      th: ['colspan', 'rowspan', 'colwidth'],
      td: ['colspan', 'rowspan', 'colwidth'],
      code: ['class'],
      pre: ['class'],
      p: ['class'],
    },
    allowedSchemes: ['http', 'https', 'mailto', 'tel'],
    allowedSchemesByTag: { img: ['http', 'https', 'data'] },
    allowedClasses: { div: ['callout', /^callout-[a-z]+$/], span: [/^ph$/], code: [/^language-/], p: [/.*/] },
    transformTags: { a: sanitizeHtmlLib.simpleTransform('a', { rel: 'noopener noreferrer', target: '_blank' }) },
  });
}

/** Strip HTML to plain text (for search indexing / AI API). */
export function htmlToText(html) {
  return sanitizeHtmlLib(String(html || '').replace(/<\/(p|li|h\d|tr|div|blockquote)>/g, '$&\n').replace(/<br\s*\/?>/g, '\n'), { allowedTags: [], allowedAttributes: {} })
    .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&nbsp;/g, ' ')
    .replace(/\n{3,}/g, '\n\n').trim();
}

export function audit(req, action, entityType, entityId, details = {}) {
  run('INSERT INTO audit_log(user_id, action, entity_type, entity_id, details, ip, created_at) VALUES (?,?,?,?,?,?,?)',
    req?.user?.id ?? null, action, entityType ?? null, entityId == null ? null : String(entityId), JSON.stringify(details), req?.ip ?? null, nowIso());
}

export class HttpError extends Error {
  constructor(status, message) { super(message); this.status = status; }
}
export const bad = (msg) => new HttpError(400, msg);
export const forbidden = (msg = 'You do not have permission to do this.') => new HttpError(403, msg);
export const notFound = (msg = 'Not found.') => new HttpError(404, msg);

/** Wrap an async/sync route handler so thrown errors become JSON responses. */
export const h = (fn) => (req, res, next) => {
  try {
    const r = fn(req, res, next);
    if (r && typeof r.catch === 'function') r.catch(next);
  } catch (e) { next(e); }
};

export const str = (v, max = 5000) => (v == null ? null : String(v).trim().slice(0, max) || null);
export const oneOf = (v, list, fallback) => (list.includes(v) ? v : fallback);
export const PRIORITIES = ['low', 'medium', 'high', 'critical'];
export const DOC_STATUSES = ['draft', 'review', 'published', 'archived'];
export const TICKET_STATUSES = ['new', 'open', 'under_review', 'waiting_customer', 'waiting_seller', 'escalated', 'in_progress', 'resolved', 'closed', 'reopened'];
export const OPEN_STATUSES = TICKET_STATUSES.filter((s) => !['resolved', 'closed'].includes(s));
export const CHANNELS = ['telegram', 'email', 'chat', 'phone', 'sms', 'website', 'other'];

export const DEFAULT_SLA = {
  _note: 'Internal targets only — not customer guarantees. Default values are placeholders until management approves them.',
  approved: false,
  critical: { first_response_minutes: 30, resolution_hours: 8 },
  high: { first_response_minutes: 60, resolution_hours: 24 },
  medium: { first_response_minutes: 240, resolution_hours: 72 },
  low: { first_response_minutes: 480, resolution_hours: 120 },
};

export function slaFor(priority) {
  const sla = getSetting('sla', DEFAULT_SLA);
  return sla[priority] || DEFAULT_SLA[priority] || DEFAULT_SLA.medium;
}

export function dueDate(fromIso, priority) {
  const { resolution_hours } = slaFor(priority);
  return new Date(new Date(fromIso).getTime() + resolution_hours * 3600e3).toISOString();
}

export function slugify(s) {
  return String(s).toLowerCase().normalize('NFKD').replace(/[^\w\s-]/g, '').trim().replace(/[\s_]+/g, '-').replace(/-+/g, '-').slice(0, 80);
}
