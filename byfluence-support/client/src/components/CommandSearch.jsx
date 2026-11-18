import { useEffect, useMemo, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { useNavigate } from 'react-router-dom';
import { Search, FileText, Wrench, HelpCircle, MessageSquareText, ListChecks, Scale, MessagesSquare, Megaphone, GraduationCap, Ticket, Clock, TrendingUp, CornerDownLeft, Loader2 } from 'lucide-react';
import { api } from '../lib/api.js';
import { STATUS } from '../lib/format.js';
import { Badge, cx } from './ui.jsx';

export const KIND_META = {
  article: { label: 'Article', icon: FileText, path: (r) => `/kb/${r.slug}` },
  troubleshooting: { label: 'Troubleshooting', icon: Wrench, path: (r) => `/kb/${r.slug}` },
  faq: { label: 'FAQ', icon: HelpCircle, path: (r) => `/faqs?open=${r.slug}` },
  template: { label: 'Template', icon: MessageSquareText, path: (r) => `/templates/${r.slug}` },
  sop: { label: 'SOP', icon: ListChecks, path: (r) => `/kb/${r.slug}` },
  policy: { label: 'Policy', icon: Scale, path: (r) => `/kb/${r.slug}` },
  guide: { label: 'Communication', icon: MessagesSquare, path: (r) => `/kb/${r.slug}` },
  announcement: { label: 'Announcement', icon: Megaphone, path: (r) => `/announcements#a${r.id}` },
  training: { label: 'Training', icon: GraduationCap, path: (r) => `/training/${r.slug}` },
  ticket: { label: 'Ticket', icon: Ticket, path: (r) => `/tickets/${r.number}` },
};

export default function CommandSearch({ open, onClose }) {
  const [q, setQ] = useState('');
  const [res, setRes] = useState(null);
  const [meta, setMeta] = useState(null);
  const [loading, setLoading] = useState(false);
  const [active, setActive] = useState(0);
  const inputRef = useRef(null);
  const nav = useNavigate();

  useEffect(() => {
    if (!open) { setQ(''); setRes(null); setActive(0); return; }
    inputRef.current?.focus();
    api('/search/meta').then(setMeta).catch(() => {});
  }, [open]);

  useEffect(() => {
    if (!open || !q.trim()) { setRes(null); return; }
    const c = new AbortController();
    setLoading(true);
    const t = setTimeout(() => {
      api(`/search/suggest?q=${encodeURIComponent(q)}`, { signal: c.signal }).then((r) => { setRes(r); setActive(0); }).catch(() => {}).finally(() => setLoading(false));
    }, 120);
    return () => { clearTimeout(t); c.abort(); };
  }, [q, open]);

  const items = useMemo(() => {
    if (!q.trim()) {
      const out = [];
      (meta?.recent || []).slice(0, 5).forEach((r) => out.push({ type: 'recent', label: r, go: () => setQ(r) }));
      (meta?.popular || []).slice(0, 5).forEach((d) => out.push({ type: 'popular', label: d.title, kind: d.type, go: () => nav(KIND_META[d.type]?.path(d) || `/kb/${d.slug}`) }));
      return out;
    }
    const out = [];
    (res?.tickets || []).forEach((t) => out.push({ type: 'result', kind: 'ticket', label: `${t.number} · ${t.title}`, sub: `${t.customer_name} · ${STATUS[t.status]?.label}`, go: () => nav(`/tickets/${t.number}`) }));
    (res?.results || []).forEach((r) => out.push({ type: 'result', kind: r.kind, label: r.title, sub: r.category || r.summary, go: () => nav(KIND_META[r.kind]?.path(r) || '/') }));
    out.push({ type: 'all', label: `See all results for “${q}”`, go: () => nav(`/search?q=${encodeURIComponent(q)}`) });
    return out;
  }, [q, res, meta, nav]);

  if (!open) return null;
  const choose = (i) => { const it = items[i]; if (!it) return; if (it.type !== 'recent') onClose(); it.go(); };

  return createPortal(
    <div className="fixed inset-0 z-50 flex items-start justify-center p-3 sm:pt-[10vh]">
      <div className="absolute inset-0 bg-slate-900/45" onClick={onClose} />
      <div className="relative w-full max-w-2xl surface rounded-2xl border border-base shadow-2xl animate-in overflow-hidden" role="dialog" aria-label="Search">
        <div className="flex items-center gap-3 px-4 h-14 border-b border-base">
          {loading ? <Loader2 className="size-5 text-brand-500 animate-spin" /> : <Search className="size-5 text-muted" />}
          <input ref={inputRef} autoFocus value={q} onChange={(e) => setQ(e.target.value)} placeholder="Describe the customer's problem… e.g. “seller didn't join meeting”"
            className="flex-1 bg-transparent outline-none text-[15px] placeholder:text-muted"
            onKeyDown={(e) => {
              if (e.key === 'ArrowDown') { e.preventDefault(); setActive((a) => Math.min(a + 1, items.length - 1)); }
              else if (e.key === 'ArrowUp') { e.preventDefault(); setActive((a) => Math.max(a - 1, 0)); }
              else if (e.key === 'Enter') { e.preventDefault(); if (q.trim() && (e.metaKey || e.ctrlKey)) { onClose(); nav(`/search?q=${encodeURIComponent(q)}`); } else choose(active); }
              else if (e.key === 'Escape') onClose();
            }} />
          <kbd className="text-[11px] font-mono border border-base rounded px-1.5 py-0.5 text-muted">Esc</kbd>
        </div>
        <div className="max-h-[60vh] overflow-y-auto p-2">
          {!q.trim() && items.length === 0 && <p className="text-sm text-muted p-4">Search everything: knowledge base, FAQs, templates, SOPs, policies, training, announcements and tickets (by number, customer, phone, email, order or transaction ID).</p>}
          {!q.trim() && meta?.recent?.length > 0 && <div className="px-2.5 pt-1 pb-1 text-[11px] font-semibold uppercase tracking-wider text-muted">Recent searches</div>}
          {items.map((it, i) => {
            const M = KIND_META[it.kind];
            const Icon = it.type === 'recent' ? Clock : it.type === 'popular' ? TrendingUp : it.type === 'all' ? Search : M?.icon || FileText;
            const header = !q.trim() && it.type === 'popular' && items[i - 1]?.type !== 'popular';
            return (
              <div key={i}>
                {header && <div className="px-2.5 pt-3 pb-1 text-[11px] font-semibold uppercase tracking-wider text-muted">Frequently used</div>}
                <button type="button" onMouseEnter={() => setActive(i)} onClick={() => choose(i)}
                  className={cx('w-full flex items-center gap-3 rounded-lg px-2.5 py-2 text-left', active === i ? 'bg-brand-50 dark:bg-brand-900/40' : '')}>
                  <Icon className={cx('size-4 shrink-0', active === i ? 'text-brand-500' : 'text-muted')} />
                  <span className="min-w-0 flex-1">
                    <span className={cx('block text-sm truncate', it.type === 'all' && 'text-brand-600 dark:text-brand-300 font-medium')}>{it.label}</span>
                    {it.sub && <span className="block text-xs text-muted truncate">{it.sub}</span>}
                  </span>
                  {M && it.type === 'result' && <Badge tone={it.kind === 'ticket' ? 'violet' : 'gray'}>{M.label}</Badge>}
                  {active === i && <CornerDownLeft className="size-3.5 text-muted" />}
                </button>
              </div>
            );
          })}
          {q.trim() && res && res.results.length === 0 && res.tickets.length === 0 && (
            <div className="px-3 py-3 text-sm text-muted">No matches. Try other words (e.g. “payment” instead of “money”). Searches with no results are reported to supervisors as knowledge gaps.</div>
          )}
        </div>
        <div className="flex items-center gap-4 px-4 py-2 border-t border-base text-[11px] text-muted surface-2">
          <span>↑↓ navigate</span><span>↵ open</span><span>Ctrl ↵ all results</span>
        </div>
      </div>
    </div>,
    document.body,
  );
}
