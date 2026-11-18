import { useEffect, useMemo, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { ChevronDown, HelpCircle, Search, ExternalLink, Lock } from 'lucide-react';
import { api, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { Badge, Card, CopyButton, EmptyState, ErrorState, Input, Loading, PageHeader, Segmented, cx } from '../components/ui.jsx';
import RichText, { htmlToPlain } from '../components/RichText.jsx';

function FaqItem({ slug, title, open, onToggle, lang }) {
  const [doc, setDoc] = useState(null);
  useEffect(() => { if (open && !doc) api(`/docs/${slug}`).then((d) => setDoc(d.doc)).catch(() => {}); }, [open, slug, doc]);
  const by = Object.fromEntries((doc?.sections || []).map((s) => [s.key, s]));
  const ans = (lang === 'am' ? by.answer_am : by.answer_en) || by.answer_en || by.answer_am;
  return (
    <div id={slug} className="border-t border-base first:border-t-0 scroll-mt-24">
      <button type="button" onClick={onToggle} className="w-full flex items-center gap-3 px-4 py-3 text-left hover:bg-[var(--surface-2)]" aria-expanded={open}>
        <HelpCircle className="size-4 text-brand-500 shrink-0" />
        <span className="flex-1 text-[14px] font-medium">{title}</span>
        <ChevronDown className={cx('size-4 text-muted transition-transform', open && 'rotate-180')} />
      </button>
      {open && (
        <div className="px-4 pb-4 pl-11 animate-in">
          {!doc ? <div className="text-sm text-muted">Loading…</div> : (
            <>
              <div lang={lang}><RichText html={ans?.html} className={lang === 'am' ? 'text-[15px]' : ''} /></div>
              {by.internal && <div className="mt-3 rounded-lg surface-2 border border-dashed border-base p-3"><div className="text-xs font-semibold text-muted flex items-center gap-1 mb-1"><Lock className="size-3" />Internal note</div><RichText html={by.internal.html} /></div>}
              <div className="flex flex-wrap gap-2 mt-3">
                <CopyButton variant="primary" label={`Copy ${lang === 'am' ? 'Amharic' : 'English'} answer`} getText={() => htmlToPlain(ans?.html)} />
                {doc.related?.length > 0 && <Link to={`/kb/${doc.related[0]}`} className="inline-flex items-center gap-1 text-xs text-brand-600 font-medium px-2"><ExternalLink className="size-3" />Detailed article</Link>}
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default function Faqs() {
  const { user } = useAuth();
  const [params] = useSearchParams();
  const faqs = useApi('/docs?type=faq&limit=2000');
  const cats = useApi('/categories?scope=kb');
  const [q, setQ] = useState('');
  const [lang, setLang] = useState(user.preferences?.language || 'am');
  const [openSet, setOpenSet] = useState(() => new Set(params.get('open') ? [params.get('open')] : []));
  const [cat, setCat] = useState('all');

  useEffect(() => {
    const o = params.get('open');
    if (o) { setOpenSet(new Set([o])); setTimeout(() => document.getElementById(o)?.scrollIntoView({ behavior: 'smooth', block: 'center' }), 300); }
  }, [params, faqs.data]);

  const grouped = useMemo(() => {
    if (!faqs.data || !cats.data) return [];
    const parentOf = new Map();
    for (const c of cats.data) { parentOf.set(c.id, c); for (const s of c.subcategories) parentOf.set(s.id, c); }
    const list = faqs.data.filter((f) => !q || `${f.title} ${f.summary} ${f.tags.join(' ')}`.toLowerCase().includes(q.toLowerCase()));
    return cats.data.map((c) => ({ ...c, faqs: list.filter((f) => parentOf.get(f.category_id)?.id === c.id) })).filter((g) => g.faqs.length && (cat === 'all' || String(g.id) === cat));
  }, [faqs.data, cats.data, q, cat]);

  if ((faqs.loading && !faqs.data) || (cats.loading && !cats.data)) return <Loading />;
  if (faqs.error) return <ErrorState error={faqs.error} onRetry={faqs.reload} />;
  const toggle = (slug) => setOpenSet((s) => { const n = new Set(s); if (n.has(slug)) n.delete(slug); else n.add(slug); return n; });

  return (
    <div className="max-w-5xl">
      <PageHeader icon={HelpCircle} title="Customer FAQs" subtitle={`${faqs.data.length} short, approved answers to the questions customers ask most — in Amharic and English, ready to copy.`}
        actions={<Segmented value={lang} onChange={setLang} options={[{ value: 'am', label: 'አማርኛ' }, { value: 'en', label: 'English' }]} />} />
      <div className="flex flex-wrap gap-2 mb-4">
        <div className="relative flex-1 min-w-[220px]"><Search className="size-4 absolute left-3 top-2.5 text-muted" /><Input className="pl-9" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Filter questions…" /></div>
      </div>
      <div className="flex flex-wrap gap-1.5 mb-5">
        <button type="button" onClick={() => setCat('all')}><Badge tone={cat === 'all' ? 'blue' : 'gray'} className="cursor-pointer px-2 py-1">All topics</Badge></button>
        {(cats.data || []).filter((c) => faqs.data.some((f) => f.category_id === c.id || c.subcategories.some((s) => s.id === f.category_id))).map((c) => (
          <button type="button" key={c.id} onClick={() => setCat(String(c.id))}><Badge tone={cat === String(c.id) ? 'blue' : 'gray'} className="cursor-pointer px-2 py-1">{c.name}</Badge></button>
        ))}
      </div>
      {grouped.length === 0 ? <Card><EmptyState title="No FAQs match your filter" /></Card> : grouped.map((g) => (
        <section key={g.id} className="mb-5">
          <h2 className="text-xs font-semibold uppercase tracking-wider text-muted mb-2">{g.name} {g.name_am && <span className="normal-case font-normal">· {g.name_am}</span>}</h2>
          <Card>{g.faqs.map((f) => <FaqItem key={f.slug} slug={f.slug} title={f.title} lang={lang} open={openSet.has(f.slug)} onToggle={() => toggle(f.slug)} />)}</Card>
        </section>
      ))}
    </div>
  );
}
