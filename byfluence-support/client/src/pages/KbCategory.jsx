import { useMemo, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { ChevronRight, Scale, Search } from 'lucide-react';
import { useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { DOC_TYPES } from '../lib/format.js';
import { Badge, Card, DocStatusBadge, EmptyState, ErrorState, Input, Loading, PageHeader, PriorityBadge, Segmented, cx } from '../components/ui.jsx';
import { iconFor } from './KnowledgeBase.jsx';

export function DocCard({ d, showCategory }) {
  return (
    <Link to={d.type === 'faq' ? `/faqs?open=${d.slug}` : `/kb/${d.slug}`}
      className="flex items-start gap-3 px-4 py-3 border-t border-base first:border-t-0 hover:bg-[var(--surface-2)] transition-colors">
      <div className="min-w-0 flex-1">
        <div className="flex flex-wrap items-center gap-1.5">
          <span className="font-medium text-[14px]">{d.title}</span>
          {d.type !== 'article' && <Badge tone={d.type === 'troubleshooting' ? 'violet' : 'gray'}>{DOC_TYPES[d.type]?.label}</Badge>}
          {d.status !== 'published' && <DocStatusBadge status={d.status} />}
          {d.policy_pending && <Badge tone="amber"><Scale className="size-3" />Policy pending</Badge>}
        </div>
        {d.summary && <p className="text-[13px] text-muted mt-0.5 line-clamp-2">{d.summary}</p>}
        {showCategory && d.category_name && <p className="text-[11px] text-muted mt-1">{d.parent_category_name ? `${d.parent_category_name} → ` : ''}{d.category_name}</p>}
      </div>
      <div className="hidden sm:flex items-center gap-2 shrink-0">
        {d.audience && d.audience !== 'both' && <Badge tone={d.audience === 'internal' ? 'slate' : 'sky'}>{d.audience}</Badge>}
        {d.type !== 'faq' && <PriorityBadge priority={d.priority} />}
        <ChevronRight className="size-4 text-muted" />
      </div>
    </Link>
  );
}

export default function KbCategory() {
  const { cat } = useParams();
  const { can } = useAuth();
  const cats = useApi('/categories?scope=kb');
  const category = cats.data?.find((c) => c.slug === cat);
  const docs = useApi(category ? `/docs?category=${category.id}&type=article,troubleshooting,faq` : null, [category?.id]);
  const [sub, setSub] = useState('all');
  const [type, setType] = useState('all');
  const [audience, setAudience] = useState('all');
  const [q, setQ] = useState('');

  const filtered = useMemo(() => (docs.data || []).filter((d) =>
    (sub === 'all' || d.category_id === Number(sub)) && (type === 'all' || d.type === type) && (audience === 'all' || d.audience === audience || d.audience === 'both')
    && (!q || `${d.title} ${d.summary} ${d.tags.join(' ')}`.toLowerCase().includes(q.toLowerCase()))), [docs.data, sub, type, audience, q]);

  if (cats.loading && !cats.data) return <Loading />;
  if (cats.error) return <ErrorState error={cats.error} />;
  if (!category) return <ErrorState error={{ status: 404, message: 'Category not found.' }} />;
  const I = iconFor(category.icon);
  const groups = category.subcategories.map((s) => ({ ...s, docs: filtered.filter((d) => d.category_id === s.id) })).filter((g) => g.docs.length);
  const direct = filtered.filter((d) => d.category_id === category.id);

  return (
    <div>
      <PageHeader icon={I} title={category.name} subtitle={category.description}
        breadcrumb={<><Link to="/kb" className="hover:text-brand-600">Knowledge Base</Link><ChevronRight className="size-3" />{category.name}{category.name_am && <span className="ml-1">· {category.name_am}</span>}</>}
        actions={can('docs.edit') && <Link to={`/manage/docs/new?type=article&category=${category.id}`} className="text-sm font-medium text-brand-600">+ New article</Link>} />
      <div className="grid lg:grid-cols-[230px_1fr] gap-5">
        <nav className="space-y-0.5 lg:sticky lg:top-20 self-start">
          {[{ id: 'all', name: 'All topics', count: category.count }, ...category.subcategories].map((s) => (
            <button key={s.id} type="button" onClick={() => setSub(String(s.id))}
              className={cx('w-full flex items-center justify-between rounded-lg px-3 py-1.5 text-sm text-left', String(s.id) === sub ? 'bg-brand-50 text-brand-700 font-medium dark:bg-brand-900/40 dark:text-brand-200' : 'hover:bg-[var(--surface-2)]')}>
              <span className="truncate">{s.name}</span><span className="text-xs text-muted tabular-nums">{s.count}</span>
            </button>
          ))}
        </nav>
        <div className="space-y-4 min-w-0">
          <div className="flex flex-wrap items-center gap-2">
            <div className="relative flex-1 min-w-[200px]"><Search className="size-4 absolute left-3 top-2.5 text-muted" /><Input className="pl-9" placeholder="Filter this category…" value={q} onChange={(e) => setQ(e.target.value)} /></div>
            <Segmented value={type} onChange={setType} options={[{ value: 'all', label: 'All' }, { value: 'article', label: 'Articles' }, { value: 'troubleshooting', label: 'Guides' }, { value: 'faq', label: 'FAQs' }]} />
            <Segmented value={audience} onChange={setAudience} options={[{ value: 'all', label: 'Everyone' }, { value: 'buyer', label: 'Buyers' }, { value: 'seller', label: 'Sellers' }]} />
          </div>
          {docs.loading && !docs.data ? <Loading /> : filtered.length === 0 ? <Card><EmptyState title="No articles match">Try a different filter or search the whole knowledge base.</EmptyState></Card> : (
            <>
              {direct.length > 0 && <Card>{direct.map((d) => <DocCard key={d.slug} d={d} />)}</Card>}
              {groups.map((g) => (
                <section key={g.id}>
                  <h2 className="text-xs font-semibold uppercase tracking-wider text-muted mb-2 mt-1">{g.name} <span className="font-normal">({g.docs.length})</span></h2>
                  <Card>{g.docs.map((d) => <DocCard key={d.slug} d={d} />)}</Card>
                </section>
              ))}
            </>
          )}
        </div>
      </div>
    </div>
  );
}
