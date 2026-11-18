import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { BookOpen, Search, TrendingUp, History, Wrench, ArrowRight } from 'lucide-react';
import { useApi } from '../lib/api.js';
import { iconFor } from '../lib/icons.js';
import { Card, ErrorState, Loading, PageHeader, Badge } from '../components/ui.jsx';

export { iconFor };

export default function KnowledgeBase() {
  const cats = useApi('/categories?scope=kb');
  const meta = useApi('/search/meta');
  const tsg = useApi('/docs?type=troubleshooting&sort=views&limit=6');
  const [q, setQ] = useState('');
  const nav = useNavigate();
  if (cats.loading && !cats.data) return <Loading />;
  if (cats.error) return <ErrorState error={cats.error} onRetry={cats.reload} />;
  const total = cats.data.reduce((a, c) => a + c.count, 0);
  return (
    <div className="space-y-6">
      <PageHeader icon={BookOpen} title="Knowledge Base" subtitle={`${total} support articles, troubleshooting guides and FAQs across ${cats.data.length} categories. Every article tells you what to collect, what to check, what to say and when to escalate.`} />
      <form onSubmit={(e) => { e.preventDefault(); if (q.trim()) nav(`/search?q=${encodeURIComponent(q)}`); }}
        className="flex items-center gap-3 surface border border-base rounded-xl px-4 h-12 shadow-sm focus-within:ring-2 focus-within:ring-brand-500/25 focus-within:border-brand-400">
        <Search className="size-5 text-muted" />
        <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Describe the customer's problem in their words — e.g. “money deducted but booking not confirmed”" className="flex-1 bg-transparent outline-none text-[15px]" />
        <button type="submit" className="text-sm font-medium text-brand-600">Search</button>
      </form>

      <div className="grid sm:grid-cols-2 xl:grid-cols-3 gap-3">
        {cats.data.map((c) => {
          const I = iconFor(c.icon);
          return (
            <Link key={c.id} to={`/kb/c/${c.slug}`} className="group surface border border-base rounded-xl p-4 hover:border-brand-300 hover:shadow-sm transition">
              <div className="flex items-start gap-3">
                <div className="size-10 rounded-lg bg-brand-50 text-brand-600 dark:bg-brand-900/40 dark:text-brand-300 grid place-items-center shrink-0"><I className="size-5" /></div>
                <div className="min-w-0 flex-1">
                  <div className="flex items-baseline justify-between gap-2">
                    <h3 className="font-semibold text-[15px] group-hover:text-brand-600 truncate">{c.name}</h3>
                    <span className="text-xs text-muted tabular-nums shrink-0">{c.count}</span>
                  </div>
                  {c.name_am && <div className="text-xs text-muted">{c.name_am}</div>}
                  <p className="text-[13px] text-muted mt-1.5 line-clamp-2">{c.description}</p>
                  <div className="flex flex-wrap gap-1 mt-2.5">
                    {c.subcategories.slice(0, 4).map((s) => <Badge key={s.id} tone="gray">{s.name}</Badge>)}
                    {c.subcategories.length > 4 && <Badge tone="gray">+{c.subcategories.length - 4}</Badge>}
                  </div>
                </div>
              </div>
            </Link>
          );
        })}
      </div>

      <div className="grid lg:grid-cols-3 gap-5">
        <Card className="p-4">
          <h3 className="font-semibold text-sm flex items-center gap-2 mb-3"><TrendingUp className="size-4 text-brand-500" />Most used articles</h3>
          <ul className="space-y-1.5">{(meta.data?.popular || []).map((d) => <li key={d.slug}><Link className="text-sm hover:text-brand-600 line-clamp-1" to={d.type === 'faq' ? `/faqs?open=${d.slug}` : `/kb/${d.slug}`}>{d.title}</Link></li>)}</ul>
        </Card>
        <Card className="p-4">
          <h3 className="font-semibold text-sm flex items-center gap-2 mb-3"><History className="size-4 text-brand-500" />Recently viewed by you</h3>
          {(meta.data?.recently_viewed || []).length === 0 ? <p className="text-sm text-muted">Articles you open appear here.</p>
            : <ul className="space-y-1.5">{meta.data.recently_viewed.map((d) => <li key={d.slug}><Link className="text-sm hover:text-brand-600 line-clamp-1" to={`/kb/${d.slug}`}>{d.title}</Link></li>)}</ul>}
        </Card>
        <Card className="p-4">
          <h3 className="font-semibold text-sm flex items-center gap-2 mb-3"><Wrench className="size-4 text-brand-500" />Master troubleshooting guides</h3>
          <ul className="space-y-1.5">{(tsg.data || []).map((d) => <li key={d.slug}><Link className="text-sm hover:text-brand-600 line-clamp-1" to={`/kb/${d.slug}`}>{d.title}</Link></li>)}</ul>
          <Link to="/troubleshooting" className="mt-3 text-xs font-medium text-brand-600 inline-flex items-center gap-1">All guides <ArrowRight className="size-3" /></Link>
        </Card>
      </div>
    </div>
  );
}
