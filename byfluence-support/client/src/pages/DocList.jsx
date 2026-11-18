import { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { Wrench, ListChecks, MessagesSquare, Search, Plus } from 'lucide-react';
import { useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { Card, EmptyState, ErrorState, Input, Loading, PageHeader, cx } from '../components/ui.jsx';
import { DocCard } from './KbCategory.jsx';

const META = {
  troubleshooting: { icon: Wrench, title: 'Troubleshooting Guides', scope: 'kb', subtitle: 'Master diagnostic playbooks: start from the symptom, follow the decision steps, know exactly when to escalate.' },
  sop: { icon: ListChecks, title: 'Support SOPs', scope: 'sop', subtitle: 'Standard operating procedures for every part of the support day — from starting a shift to the daily report.' },
  guide: { icon: MessagesSquare, title: 'Customer Communication', scope: 'communication', subtitle: 'How Byfluence sounds: tone, Amharic & English writing, channel etiquette and difficult conversations.' },
  policy: { icon: ListChecks, title: 'Policies', scope: 'policy', subtitle: '' },
};

export default function DocList({ type, embedded }) {
  const m = META[type];
  const { can } = useAuth();
  const docs = useApi(`/docs?type=${type}&limit=1000`, [type]);
  const cats = useApi(`/categories?scope=${m.scope}`, [type]);
  const [q, setQ] = useState('');
  const [cat, setCat] = useState('all');

  const groups = useMemo(() => {
    if (!docs.data || !cats.data) return [];
    const parentOf = new Map();
    for (const c of cats.data) { parentOf.set(c.id, c.id); for (const s of c.subcategories) parentOf.set(s.id, c.id); }
    const list = docs.data.filter((d) => !q || `${d.title} ${d.summary}`.toLowerCase().includes(q.toLowerCase()));
    const out = cats.data.map((c) => ({ ...c, docs: list.filter((d) => parentOf.get(d.category_id) === c.id) })).filter((g) => g.docs.length);
    const orphan = list.filter((d) => !parentOf.has(d.category_id));
    if (orphan.length) out.push({ id: 0, name: 'Other', docs: orphan });
    return out.filter((g) => cat === 'all' || String(g.id) === cat);
  }, [docs.data, cats.data, q, cat]);

  if ((docs.loading && !docs.data) || (cats.loading && !cats.data)) return <Loading />;
  if (docs.error) return <ErrorState error={docs.error} onRetry={docs.reload} />;

  return (
    <div className={embedded ? '' : 'max-w-5xl'}>
      {!embedded && <PageHeader icon={m.icon} title={m.title} subtitle={m.subtitle}
        actions={can('docs.edit') && <Link to={`/manage/docs/new?type=${type}`}><button type="button" className="inline-flex items-center gap-1.5 h-9 px-3 rounded-lg border border-base surface text-sm font-medium hover:bg-[var(--surface-2)]"><Plus className="size-4" />New</button></Link>} />}
      <div className="flex flex-wrap gap-2 mb-4">
        <div className="relative flex-1 min-w-[220px]"><Search className="size-4 absolute left-3 top-2.5 text-muted" /><Input className="pl-9" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Filter…" /></div>
      </div>
      <div className="flex flex-wrap gap-1.5 mb-5">
        {[{ id: 'all', name: `All (${docs.data.length})` }, ...cats.data.filter((c) => docs.data.some((d) => d.category_id === c.id || c.subcategories.some((s) => s.id === d.category_id)))].map((c) => (
          <button type="button" key={c.id} onClick={() => setCat(String(c.id))}
            className={cx('rounded-full px-3 h-7 text-[13px] font-medium border', String(c.id) === cat ? 'bg-brand-500 text-white border-brand-500' : 'surface border-base hover:border-brand-300')}>{c.name}</button>
        ))}
      </div>
      {groups.length === 0 ? <Card><EmptyState title="Nothing here yet" /></Card> : groups.map((g) => (
        <section key={g.id} className="mb-5">
          <h2 className="text-xs font-semibold uppercase tracking-wider text-muted mb-2">{g.name}</h2>
          <Card>{g.docs.map((d) => <DocCard key={d.slug} d={d} showCategory={type === 'troubleshooting'} />)}</Card>
        </section>
      ))}
    </div>
  );
}
