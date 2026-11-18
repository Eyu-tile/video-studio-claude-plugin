export const STATUS = {
  new: { label: 'New', tone: 'sky' },
  open: { label: 'Open', tone: 'blue' },
  under_review: { label: 'Under Review', tone: 'violet' },
  waiting_customer: { label: 'Waiting for Customer', tone: 'amber' },
  waiting_seller: { label: 'Waiting for Seller', tone: 'orange' },
  escalated: { label: 'Escalated', tone: 'red' },
  in_progress: { label: 'In Progress', tone: 'indigo' },
  resolved: { label: 'Resolved', tone: 'green' },
  closed: { label: 'Closed', tone: 'gray' },
  reopened: { label: 'Reopened', tone: 'pink' },
};
export const STATUS_ORDER = ['new', 'open', 'under_review', 'waiting_customer', 'waiting_seller', 'escalated', 'in_progress', 'reopened', 'resolved', 'closed'];
export const MANUAL_STATUSES = ['new', 'open', 'under_review', 'waiting_customer', 'waiting_seller', 'in_progress'];

export const PRIORITY = {
  critical: { label: 'Critical', tone: 'red' },
  high: { label: 'High', tone: 'orange' },
  medium: { label: 'Medium', tone: 'blue' },
  low: { label: 'Low', tone: 'gray' },
};

export const DOC_TYPES = {
  article: { label: 'Article', plural: 'Knowledge Base', path: '/kb' },
  troubleshooting: { label: 'Troubleshooting Guide', plural: 'Troubleshooting Guides', path: '/troubleshooting' },
  faq: { label: 'FAQ', plural: 'Customer FAQs', path: '/faqs' },
  sop: { label: 'SOP', plural: 'Support SOPs', path: '/sops' },
  policy: { label: 'Policy', plural: 'Policies & Guidelines', path: '/policies' },
  guide: { label: 'Communication Guide', plural: 'Customer Communication', path: '/communication' },
};

export const DOC_STATUS = {
  draft: { label: 'Draft', tone: 'gray' },
  review: { label: 'Under Review', tone: 'amber' },
  published: { label: 'Published', tone: 'green' },
  archived: { label: 'Archived', tone: 'slate' },
};

export const CHANNELS = {
  telegram: 'Telegram', email: 'Email', chat: 'Live chat', phone: 'Phone', sms: 'SMS', website: 'Website form', other: 'Other', any: 'Any channel',
};

export const FEATURE_STATUS = {
  live: { label: 'Live', tone: 'green' },
  beta: { label: 'Beta', tone: 'sky' },
  planned: { label: 'Planned — not live', tone: 'violet' },
  unavailable: { label: 'Unavailable', tone: 'red' },
  unconfirmed: { label: 'Unconfirmed', tone: 'amber' },
};

export const ROLE_LABEL = { admin: 'Administrator', supervisor: 'Supervisor', agent: 'Support Agent' };

const rtf = typeof Intl !== 'undefined' ? new Intl.RelativeTimeFormat('en', { numeric: 'auto' }) : null;
export function relTime(iso) {
  if (!iso) return '—';
  const diff = (new Date(iso).getTime() - Date.now()) / 1000;
  const abs = Math.abs(diff);
  const pick = abs < 60 ? [Math.round(diff), 'second'] : abs < 3600 ? [Math.round(diff / 60), 'minute'] : abs < 86400 ? [Math.round(diff / 3600), 'hour'] : abs < 86400 * 30 ? [Math.round(diff / 86400), 'day'] : abs < 86400 * 365 ? [Math.round(diff / (86400 * 30)), 'month'] : [Math.round(diff / (86400 * 365)), 'year'];
  if (abs < 45) return diff < 0 ? 'just now' : 'in a moment';
  return rtf ? rtf.format(pick[0], pick[1]) : new Date(iso).toLocaleString();
}

export function dateTime(iso, opts = {}) {
  if (!iso) return '—';
  return new Date(iso).toLocaleString('en-GB', { day: 'numeric', month: 'short', year: opts.year === false ? undefined : 'numeric', hour: '2-digit', minute: '2-digit', hour12: true, timeZone: 'Africa/Addis_Ababa' }) + (opts.tz === false ? '' : ' EAT');
}
export function dateOnly(iso) {
  if (!iso) return '—';
  return new Date(iso).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'Africa/Addis_Ababa' });
}

/** Ethiopian local clock (hour − 6) for a given ISO time, e.g. "3:00 (ቀን)". */
export function ethiopianClock(iso) {
  if (!iso) return '';
  const d = new Date(iso);
  const parts = new Intl.DateTimeFormat('en-GB', { hour: 'numeric', minute: '2-digit', hour12: false, timeZone: 'Africa/Addis_Ababa' }).formatToParts(d);
  const h = Number(parts.find((p) => p.type === 'hour').value);
  const m = parts.find((p) => p.type === 'minute').value;
  const eh = ((h + 6) % 12) || 12;
  const period = h >= 6 && h < 18 ? 'ቀን' : 'ማታ';
  return `${eh}:${m} ${period} (Ethiopian time)`;
}

export function hours(h) {
  if (h == null) return '—';
  if (h < 1) return `${Math.round(h * 60)} min`;
  if (h < 48) return `${Math.round(h * 10) / 10} h`;
  return `${Math.round((h / 24) * 10) / 10} days`;
}
export function minutes(m) {
  if (m == null) return '—';
  if (m < 60) return `${m} min`;
  return hours(m / 60);
}

export function bytes(n) {
  if (n < 1024) return `${n} B`;
  if (n < 1024 ** 2) return `${(n / 1024).toFixed(0)} KB`;
  return `${(n / 1024 ** 2).toFixed(1)} MB`;
}

export function toLocalInput(iso) {
  const d = iso ? new Date(iso) : new Date();
  const off = d.getTimezoneOffset();
  return new Date(d.getTime() - off * 60e3).toISOString().slice(0, 16);
}

export const initials = (name = '') => name.split(/\s+/).filter(Boolean).slice(0, 2).map((p) => p[0]).join('').toUpperCase();

/** Fill {{placeholders}} in text */
export function fillPlaceholders(text, values) {
  return (text || '').replace(/{{\s*([a-z_]+)\s*}}/g, (m, k) => (values[k] ? values[k] : m));
}
export function placeholdersIn(...texts) {
  const out = new Set();
  for (const t of texts) for (const m of (t || '').matchAll(/{{\s*([a-z_]+)\s*}}/g)) out.add(m[1]);
  return [...out];
}

export function downloadCsv(filename, rows) {
  if (!rows.length) return;
  const cols = Object.keys(rows[0]);
  const esc = (v) => `"${String(v ?? '').replace(/"/g, '""')}"`;
  const csv = [cols.join(','), ...rows.map((r) => cols.map((c) => esc(r[c])).join(','))].join('\n');
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob(['﻿' + csv], { type: 'text/csv;charset=utf-8' }));
  a.download = filename;
  a.click();
  URL.revokeObjectURL(a.href);
}
