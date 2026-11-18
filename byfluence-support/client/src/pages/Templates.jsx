import { useEffect, useMemo, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { MessageSquareText, Search, Pencil, History, Plus, Info, FileText } from 'lucide-react';
import { useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { CHANNELS, relTime } from '../lib/format.js';
import { Badge, Button, Card, DocStatusBadge, EmptyState, ErrorState, Input, Loading, PageHeader, Select, cx } from '../components/ui.jsx';
import TemplateFiller from '../components/TemplateFiller.jsx';
import RichText from '../components/RichText.jsx';

const STYLE_TONE = { short: 'sky', standard: 'gray', detailed: 'indigo', formal: 'violet', friendly: 'green' };

export default function Templates() {
  const { slug } = useParams();
  const nav = useNavigate();
  const { can } = useAuth();
  const list = useApi('/templates');
  const cats = useApi('/categories?scope=template');
  const detail = useApi(slug ? `/templates/${slug}` : null, [slug]);
  const [f, setF] = useState({ q: '', category: '', channel: '', style: '', language: '' });

  const filtered = useMemo(() => (list.data || []).filter((t) =>
    (!f.category || String(t.category_id) === f.category) && (!f.channel || t.channel === f.channel || t.channel === 'any') && (!f.style || t.style === f.style)
    && (!f.language || (f.language === 'am' ? t.content_am : t.content_en)?.trim())
    && (!f.q || `${t.name} ${t.tags.join(' ')} ${t.content_en}`.toLowerCase().includes(f.q.toLowerCase()))), [list.data, f]);

  useEffect(() => {
    if (!slug && filtered.length && window.innerWidth >= 1024) nav(`/templates/${filtered[0].slug}`, { replace: true });
  }, [slug, filtered, nav]);

  if (list.loading && !list.data) return <Loading />;
  if (list.error) return <ErrorState error={list.error} onRetry={list.reload} />;
  const groups = (cats.data || []).map((c) => ({ ...c, items: filtered.filter((t) => t.category_id === c.id) })).filter((g) => g.items.length);
  const t = detail.data?.template;

  return (
    <div>
      <PageHeader icon={MessageSquareText} title="Response Templates" subtitle={`${list.data.length} approved messages in Amharic and English for Telegram, email, live chat, SMS and phone. Fill the placeholders, copy, send — then log it on the ticket.`}
        actions={can('templates.edit') && <Link to="/manage/templates/new"><Button icon={Plus}>New template</Button></Link>} />
      <div className="grid lg:grid-cols-[340px_1fr] gap-5">
        <div className={cx('space-y-3', slug && 'hidden lg:block')}>
          <div className="relative"><Search className="size-4 absolute left-3 top-2.5 text-muted" /><Input className="pl-9" placeholder="Search templates…" value={f.q} onChange={(e) => setF({ ...f, q: e.target.value })} /></div>
          <div className="grid grid-cols-2 gap-2">
            <Select value={f.category} onChange={(e) => setF({ ...f, category: e.target.value })}><option value="">All categories</option>{(cats.data || []).map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</Select>
            <Select value={f.channel} onChange={(e) => setF({ ...f, channel: e.target.value })}><option value="">All channels</option>{['telegram', 'email', 'chat', 'sms', 'phone'].map((c) => <option key={c} value={c}>{CHANNELS[c]}</option>)}</Select>
            <Select value={f.style} onChange={(e) => setF({ ...f, style: e.target.value })}><option value="">All styles</option>{Object.keys(STYLE_TONE).map((s) => <option key={s} value={s} className="capitalize">{s}</option>)}</Select>
            <Select value={f.language} onChange={(e) => setF({ ...f, language: e.target.value })}><option value="">Any language</option><option value="am">Has Amharic</option><option value="en">Has English</option></Select>
          </div>
          <Card className="max-h-[calc(100vh-290px)] overflow-y-auto">
            {groups.length === 0 && <EmptyState title="No templates match" />}
            {groups.map((g) => (
              <div key={g.id}>
                <div className="sticky top-0 surface-2 px-3 py-1.5 text-[11px] font-semibold uppercase tracking-wider text-muted border-b border-base">{g.name}</div>
                {g.items.map((x) => (
                  <Link key={x.slug} to={`/templates/${x.slug}`} className={cx('block px-3 py-2 border-b border-base last:border-b-0', x.slug === slug ? 'bg-brand-50 dark:bg-brand-900/30' : 'hover:bg-[var(--surface-2)]')}>
                    <div className={cx('text-[13.5px] font-medium', x.slug === slug && 'text-brand-700 dark:text-brand-200')}>{x.name}</div>
                    <div className="flex gap-1 mt-1">
                      <Badge tone="gray">{CHANNELS[x.channel]}</Badge>
                      <Badge tone={STYLE_TONE[x.style]} className="capitalize">{x.style}</Badge>
                      {x.status !== 'published' && <DocStatusBadge status={x.status} />}
                    </div>
                  </Link>
                ))}
              </div>
            ))}
          </Card>
        </div>
        <div className="min-w-0">
          {!slug ? <Card><EmptyState icon={MessageSquareText} title="Choose a template">Pick a template from the list to fill in and copy.</EmptyState></Card>
            : detail.loading && !t ? <Loading /> : detail.error ? <ErrorState error={detail.error} /> : t && (
              <Card className="p-5">
                <div className="flex flex-wrap items-start justify-between gap-3 mb-4">
                  <div>
                    <button type="button" className="lg:hidden text-xs text-brand-600 mb-2" onClick={() => nav('/templates')}>← All templates</button>
                    <h2 className="text-lg font-semibold">{t.name}</h2>
                    <div className="flex flex-wrap gap-1.5 mt-1.5">
                      <Badge tone="blue">{t.category_name}</Badge>
                      <Badge tone="gray">{CHANNELS[t.channel]}</Badge>
                      <Badge tone={STYLE_TONE[t.style]} className="capitalize">{t.style}</Badge>
                      {t.status !== 'published' && <DocStatusBadge status={t.status} />}
                      <span className="text-xs text-muted self-center">· used {t.usage_count}× · v{t.version} · updated {relTime(t.updated_at)}</span>
                    </div>
                  </div>
                  {can('templates.edit') && (
                    <div className="flex gap-2">
                      <Link to={`/manage/templates/${t.slug}`}><Button size="sm" icon={Pencil}>Edit</Button></Link>
                      <Link to={`/manage/history/template/${t.slug}`}><Button size="sm" icon={History}>History</Button></Link>
                    </div>
                  )}
                </div>
                <TemplateFiller key={t.slug} template={t} />
                {(t.usage_notes || detail.data.related.length > 0) && (
                  <div className="grid md:grid-cols-2 gap-4 mt-6 pt-5 border-t border-base">
                    {t.usage_notes && <div><div className="text-xs font-semibold uppercase tracking-wider text-muted mb-2 flex items-center gap-1.5"><Info className="size-3.5" />Usage notes</div><RichText html={t.usage_notes} className="text-sm" /></div>}
                    {detail.data.related.length > 0 && (
                      <div><div className="text-xs font-semibold uppercase tracking-wider text-muted mb-2 flex items-center gap-1.5"><FileText className="size-3.5" />Related articles</div>
                        <ul className="space-y-1">{detail.data.related.map((r) => <li key={r.slug}><Link to={`/kb/${r.slug}`} className="text-sm text-brand-600 hover:underline">{r.title}</Link></li>)}</ul></div>
                    )}
                  </div>
                )}
              </Card>
            )}
        </div>
      </div>
    </div>
  );
}
