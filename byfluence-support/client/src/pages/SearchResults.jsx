import { useEffect, useMemo, useState } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { Search, Sparkles } from 'lucide-react';
import { useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { Badge, Card, Checkbox, EmptyState, Loading, PriorityBadge, StatusBadge, cx } from '../components/ui.jsx';
import { KIND_META } from '../components/CommandSearch.jsx';

export default function SearchResults() {
  const [params, setParams] = useSearchParams();
  const nav = useNavigate();
  const { can } = useAuth();
  const q = params.get('q') || '';
  const [input, setInput] = useState(q);
  const [kind, setKind] = useState('all');
  const [unpublished, setUnpublished] = useState(false);
  useEffect(() => setInput(q), [q]);
  const { data, loading } = useApi(q ? `/search?q=${encodeURIComponent(q)}&limit=80${unpublished ? '&unpublished=1' : ''}` : null, [q, unpublished]);
  const counts = useMemo(() => {
    const c = { all: (data?.results.length || 0) + (data?.tickets.length || 0) };
    for (const r of data?.results || []) c[r.kind] = (c[r.kind] || 0) + 1;
    if (data?.tickets.length) c.ticket = data.tickets.length;
    return c;
  }, [data]);
  const results = (data?.results || []).filter((r) => kind === 'all' || r.kind === kind);
  return (
    <div className="max-w-4xl">
      <form onSubmit={(e) => { e.preventDefault(); setParams({ q: input }); }} className="flex items-center gap-3 surface border border-base rounded-xl px-4 h-12 shadow-sm mb-4 focus-within:ring-2 focus-within:ring-brand-500/25">
        <Search className="size-5 text-muted" />
        <input value={input} onChange={(e) => setInput(e.target.value)} className="flex-1 bg-transparent outline-none text-[15px]" placeholder="Search everything…" autoFocus />
      </form>
      {data?.expanded?.length > 0 && <p className="text-xs text-muted mb-3 flex items-center gap-1.5"><Sparkles className="size-3.5 text-brand-500" />Also matched related terms: {data.expanded.slice(0, 10).join(', ')}</p>}
      <div className="flex flex-wrap items-center gap-1.5 mb-4">
        {Object.entries(counts).map(([k, n]) => (
          <button key={k} type="button" onClick={() => setKind(k)} className={cx('rounded-full px-3 h-7 text-[13px] font-medium border', kind === k ? 'bg-brand-500 text-white border-brand-500' : 'surface border-base hover:border-brand-300')}>
            {k === 'all' ? 'All' : KIND_META[k]?.label} <span className="opacity-70">{n}</span>
          </button>
        ))}
        <span className="flex-1" />
        {can('docs.read_unpublished') && <Checkbox label="Include drafts" checked={unpublished} onChange={setUnpublished} />}
      </div>
      {!q ? <Card><EmptyState icon={Search} title="Search the whole support system" /></Card> : loading && !data ? <Loading /> : (
        <div className="space-y-3">
          {(kind === 'all' || kind === 'ticket') && data.tickets.length > 0 && (
            <Card>
              <div className="px-4 pt-3 pb-1 text-xs font-semibold uppercase tracking-wider text-muted">Tickets</div>
              {data.tickets.map((t) => (
                <Link key={t.id} to={`/tickets/${t.number}`} className="flex items-center gap-3 px-4 py-2.5 border-t border-base first:border-t-0 hover:bg-[var(--surface-2)]">
                  <span className="font-mono text-xs text-muted">{t.number}</span><span className="flex-1 text-sm truncate">{t.title} <span className="text-muted">· {t.customer_name}</span></span><PriorityBadge priority={t.priority} /><StatusBadge status={t.status} />
                </Link>
              ))}
            </Card>
          )}
          {results.length === 0 && !(data.tickets.length && (kind === 'all' || kind === 'ticket')) && <Card><EmptyState icon={Search} title={`No results for “${q}”`}>Try fewer or different words. This search has been recorded as a knowledge gap for supervisors.</EmptyState></Card>}
          {results.length > 0 && (
            <Card>
              {results.map((r) => {
                const M = KIND_META[r.kind];
                return (
                  <button type="button" key={`${r.kind}-${r.id}`} onClick={() => nav(M.path(r))} className="w-full text-left flex gap-3 px-4 py-3 border-t border-base first:border-t-0 hover:bg-[var(--surface-2)]">
                    <M.icon className="size-4 mt-1 text-brand-500 shrink-0" />
                    <span className="min-w-0 flex-1">
                      <span className="flex flex-wrap items-center gap-1.5"><span className="font-medium">{r.title}</span><Badge tone="gray">{M.label}</Badge>{r.status !== 'published' && r.kind !== 'announcement' && <Badge tone="amber">{r.status}</Badge>}</span>
                      {r.category && <span className="block text-xs text-muted mt-0.5">{r.category}</span>}
                      {r.summary && <span className="block text-[13px] text-muted mt-1 line-clamp-2">{r.summary}</span>}
                    </span>
                  </button>
                );
              })}
            </Card>
          )}
        </div>
      )}
    </div>
  );
}
