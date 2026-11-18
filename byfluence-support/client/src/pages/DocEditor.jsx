import { useEffect, useMemo, useState } from 'react';
import { Link, useNavigate, useParams, useSearchParams } from 'react-router-dom';
import { ArrowDown, ArrowUp, Plus, Trash2, Save, Send, Globe, Eye, History, X, Archive } from 'lucide-react';
import { api, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { DOC_TYPES, PRIORITY } from '../lib/format.js';
import { SCOPE_OF, SECTION_HINTS, SECTION_LABELS, TYPE_SECTIONS, OPTIONAL_SECTIONS } from '../lib/sections.js';
import { Badge, Button, Callout, Card, Checkbox, DocStatusBadge, ErrorState, Field, Input, Loading, Menu, MenuItem, Select, Textarea, useConfirm, useToast } from '../components/ui.jsx';
import Editor from '../components/Editor.jsx';

function SlugPicker({ value, onChange, kind = 'docs', placeholder }) {
  const [q, setQ] = useState('');
  const [res, setRes] = useState([]);
  useEffect(() => {
    if (q.trim().length < 2) { setRes([]); return; }
    const t = setTimeout(() => {
      const kinds = kind === 'templates' ? 'template' : 'article,troubleshooting,faq,sop,policy,guide';
      api(`/search?q=${encodeURIComponent(q)}&kinds=${kinds}&limit=8&log=0&unpublished=1`).then((r) => setRes(r.results)).catch(() => {});
    }, 200);
    return () => clearTimeout(t);
  }, [q, kind]);
  return (
    <div>
      <div className="flex flex-wrap gap-1.5 mb-1.5">{value.map((s) => <Badge key={s} tone="blue">{s}<button type="button" onClick={() => onChange(value.filter((x) => x !== s))} aria-label={`Remove ${s}`}><X className="size-3" /></button></Badge>)}</div>
      <div className="relative">
        <Input value={q} onChange={(e) => setQ(e.target.value)} placeholder={placeholder} />
        {res.length > 0 && (
          <div className="absolute z-20 mt-1 w-full surface border border-base rounded-lg shadow-lg max-h-56 overflow-y-auto">
            {res.filter((r) => !value.includes(r.slug)).map((r) => <button type="button" key={r.slug} onClick={() => { onChange([...value, r.slug]); setQ(''); setRes([]); }} className="w-full text-left px-3 py-1.5 text-sm hover:bg-[var(--surface-2)]"><span className="block truncate">{r.title}</span><span className="text-[11px] text-muted font-mono">{r.slug}</span></button>)}
          </div>
        )}
      </div>
    </div>
  );
}

export default function DocEditor() {
  const { slug } = useParams();
  const [params] = useSearchParams();
  const nav = useNavigate();
  const toast = useToast();
  const confirm = useConfirm();
  const { can, settings } = useAuth();
  const existing = useApi(slug ? `/docs/${slug}?view=0` : null, [slug]);
  const [d, setD] = useState(null);
  const [dirty, setDirty] = useState(false);
  const [busy, setBusy] = useState(false);
  const type = d?.type || params.get('type') || 'article';
  const cats = useApi(`/categories?scope=${SCOPE_OF[type]}`, [type]);

  useEffect(() => {
    if (slug && existing.data) {
      const x = existing.data.doc;
      setD({ ...x, change_summary: '' });
    } else if (!slug) {
      const t = params.get('type') || 'article';
      setD({ type: t, title: '', summary: '', category_id: params.get('category') ? Number(params.get('category')) : '', audience: 'both', priority: 'medium', department: '', features: [], tags: [], related: [], templates: [], policy_pending: false, ai_visible: true, status: 'draft',
        sections: TYPE_SECTIONS[t].map((k) => ({ key: k, label: SECTION_LABELS[k], html: '' })) });
    }
  }, [slug, existing.data, params]);

  useEffect(() => {
    const h = (e) => { if (dirty) { e.preventDefault(); e.returnValue = ''; } };
    window.addEventListener('beforeunload', h);
    return () => window.removeEventListener('beforeunload', h);
  }, [dirty]);

  const flatCats = useMemo(() => (cats.data || []).flatMap((c) => [{ id: c.id, name: c.name }, ...c.subcategories.map((s) => ({ id: s.id, name: `${c.name} → ${s.name}` }))]), [cats.data]);
  if (slug && existing.loading && !d) return <Loading />;
  if (existing.error) return <ErrorState error={existing.error} />;
  if (!d) return <Loading />;
  if (!can('docs.edit')) return <ErrorState error={{ status: 403, message: 'You cannot edit documentation.' }} />;

  const up = (patch) => { setD((x) => ({ ...x, ...patch })); setDirty(true); };
  const setSec = (i, patch) => { setD((x) => ({ ...x, sections: x.sections.map((s, j) => (j === i ? { ...s, ...patch } : s)) })); setDirty(true); };
  const move = (i, dir) => { const s = [...d.sections]; const [it] = s.splice(i, 1); s.splice(i + dir, 0, it); up({ sections: s }); };
  const addSection = (key) => up({ sections: [...d.sections, { key: key || `custom_${Date.now().toString(36)}`, label: key ? SECTION_LABELS[key] : 'New section', html: '' }], ...(key === 'policy_pending' ? { policy_pending: true } : {}) });
  const missingStd = [...TYPE_SECTIONS[type], ...OPTIONAL_SECTIONS[type]].filter((k) => !d.sections.some((s) => s.key === k));
  const canPublish = type === 'policy' ? can('policies.publish') : can('docs.publish');
  const hasPolicySection = d.sections.some((s) => s.key === 'policy_pending' && s.html);

  const save = async (status) => {
    if (!d.title.trim()) { toast.error('Title is required.'); return; }
    if (slug && !d.change_summary.trim()) { toast.error('Add a short change summary (bottom of the page).'); return; }
    if (d.policy_pending !== hasPolicySection && hasPolicySection) { up({ policy_pending: true }); }
    setBusy(true);
    try {
      const body = { title: d.title, summary: d.summary, category_id: d.category_id || null, audience: d.audience, priority: d.priority, department: d.department || null, features: d.features, tags: d.tags, related: d.related, templates: d.templates, policy_pending: d.policy_pending || hasPolicySection, ai_visible: d.ai_visible, sections: d.sections.filter((s) => s.label.trim()), change_summary: d.change_summary, expected_version: d.version };
      let saved;
      if (slug) {
        saved = await api(`/docs/${slug}`, { method: 'PUT', body });
        if (status && status !== saved.status) await api(`/docs/${slug}/status`, { method: 'POST', body: { status } });
      } else saved = await api('/docs', { method: 'POST', body: { ...body, type, status: status || 'draft' } });
      setDirty(false);
      toast.success(status === 'published' ? 'Published' : status === 'review' ? 'Sent for review' : 'Saved');
      nav(`/kb/${saved.slug}`);
    } catch (e) { toast.error(e); } finally { setBusy(false); }
  };

  return (
    <div className="max-w-6xl mx-auto">
      <div className="flex flex-wrap items-center justify-between gap-3 mb-5">
        <div>
          <Link to="/manage" className="text-xs text-muted hover:text-brand-600">← Documentation Management</Link>
          <h1 className="text-xl font-semibold mt-1 flex items-center gap-2">{slug ? 'Edit' : 'New'} {DOC_TYPES[type].label.toLowerCase()} {slug && <DocStatusBadge status={d.status} />}{slug && <span className="text-sm font-normal text-muted">v{d.version}</span>}</h1>
        </div>
        <div className="flex flex-wrap gap-2">
          {slug && <Link to={`/kb/${slug}`}><Button icon={Eye}>View</Button></Link>}
          {slug && <Link to={`/manage/history/doc/${slug}`}><Button icon={History}>History</Button></Link>}
          {slug && d.status !== 'archived' && canPublish && <Button icon={Archive} onClick={async () => { if (await confirm({ title: 'Archive this document?', message: 'It will no longer be visible to agents or the AI assistant. You can restore it later.', confirmLabel: 'Archive' })) { try { await api(`/docs/${slug}/status`, { method: 'POST', body: { status: 'archived' } }); toast.success('Archived'); nav('/manage'); } catch (e) { toast.error(e); } } }}>Archive</Button>}
          <Button icon={Save} loading={busy} onClick={() => save(slug ? undefined : 'draft')}>{slug ? 'Save' : 'Save draft'}</Button>
          {d.status !== 'review' && d.status !== 'published' && <Button icon={Send} loading={busy} onClick={() => save('review')}>Submit for review</Button>}
          {canPublish && <Button variant="primary" icon={Globe} loading={busy} onClick={() => save('published')}>{d.status === 'published' ? 'Save & keep published' : 'Publish'}</Button>}
        </div>
      </div>
      {d.status === 'published' && !canPublish && <Callout tone="note" className="mb-4">This document is published. Your changes will be sent for review before they become official instructions.</Callout>}

      <div className="grid lg:grid-cols-[1fr_300px] gap-5">
        <div className="space-y-4 min-w-0">
          <Card className="p-4 space-y-3">
            <Field label="Title" required><Input value={d.title} onChange={(e) => up({ title: e.target.value })} placeholder="e.g. Customer Paid but Consultation Booking Was Not Confirmed" /></Field>
            <Field label="Summary" hint="1–2 sentences shown in search results and at the top of the article."><Textarea rows={2} value={d.summary} onChange={(e) => up({ summary: e.target.value })} /></Field>
          </Card>
          {d.sections.map((s, i) => (
            <Card key={`${s.key}-${i}`} className="p-4">
              <div className="flex items-center gap-2 mb-2">
                <Input className="h-8 font-semibold flex-1" value={s.label} onChange={(e) => setSec(i, { label: e.target.value })} />
                <Button size="xs" variant="ghost" icon={ArrowUp} disabled={i === 0} onClick={() => move(i, -1)} aria-label="Move up" />
                <Button size="xs" variant="ghost" icon={ArrowDown} disabled={i === d.sections.length - 1} onClick={() => move(i, 1)} aria-label="Move down" />
                <Button size="xs" variant="ghost" icon={Trash2} onClick={async () => { if (!s.html || await confirm({ title: 'Remove this section?', message: `“${s.label}” and its content will be removed (previous versions remain in history).`, danger: true, confirmLabel: 'Remove' })) up({ sections: d.sections.filter((_, j) => j !== i) }); }} aria-label="Remove section" />
              </div>
              {SECTION_HINTS[s.key] && <p className="text-xs text-muted mb-2">{SECTION_HINTS[s.key]}</p>}
              <Editor value={s.html} onChange={(html) => setSec(i, { html })} placeholder={`Write the ${s.label.toLowerCase()}…`} minHeight={s.key.startsWith('short') ? 80 : 120} />
            </Card>
          ))}
          <Menu align="left" trigger={({ toggle }) => <Button icon={Plus} onClick={toggle}>Add section</Button>}>
            {missingStd.map((k) => <MenuItem key={k} onClick={() => addSection(k)}>{SECTION_LABELS[k]}</MenuItem>)}
            <MenuItem onClick={() => addSection(null)}>Custom section…</MenuItem>
          </Menu>
          {slug && <Card className="p-4"><Field label="Change summary" required hint="Recorded in version history — e.g. “Telebirr is now live; updated step 3.”"><Input value={d.change_summary} onChange={(e) => up({ change_summary: e.target.value })} /></Field></Card>}
        </div>

        <aside className="space-y-4 lg:sticky lg:top-20 self-start">
          <Card className="p-4 space-y-3">
            <Field label="Category">
              <Select value={d.category_id || ''} onChange={(e) => up({ category_id: e.target.value ? Number(e.target.value) : '' })}><option value="">— none —</option>{flatCats.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</Select>
            </Field>
            {['article', 'troubleshooting', 'faq'].includes(type) && (
              <div className="grid grid-cols-2 gap-2">
                <Field label="Audience"><Select value={d.audience} onChange={(e) => up({ audience: e.target.value })}><option value="both">Buyers & sellers</option><option value="buyer">Buyers</option><option value="seller">Sellers</option><option value="internal">Internal only</option></Select></Field>
                <Field label="Default priority"><Select value={d.priority} onChange={(e) => up({ priority: e.target.value })}>{Object.entries(PRIORITY).map(([k, v]) => <option key={k} value={k}>{v.label}</option>)}</Select></Field>
              </div>
            )}
            {['article', 'troubleshooting'].includes(type) && (
              <Field label="Escalation department"><Select value={d.department || ''} onChange={(e) => up({ department: e.target.value })}><option value="">—</option>{(settings?.departments || []).map((x) => <option key={x.key} value={x.key}>{x.name}</option>)}</Select></Field>
            )}
            <Field label="Search tags" hint="Comma-separated words customers use, incl. Amharic"><Input value={d.tags.join(', ')} onChange={(e) => up({ tags: e.target.value.split(',').map((x) => x.trim()).filter(Boolean) })} /></Field>
          </Card>
          <Card className="p-4 space-y-3">
            <Field label="Related articles"><SlugPicker value={d.related} onChange={(v) => up({ related: v })} placeholder="Search articles…" /></Field>
            <Field label="Response templates"><SlugPicker kind="templates" value={d.templates} onChange={(v) => up({ templates: v })} placeholder="Search templates…" /></Field>
          </Card>
          <Card className="p-4 space-y-2">
            <div className="text-[13px] font-medium">Features this depends on</div>
            <p className="text-xs text-muted">Shows a live-status warning when any is not live.</p>
            <div className="max-h-48 overflow-y-auto space-y-1.5 pt-1">
              {(settings?.features || []).map((f) => <Checkbox key={f.key} label={f.name} checked={d.features.includes(f.key)} onChange={(v) => up({ features: v ? [...d.features, f.key] : d.features.filter((x) => x !== f.key) })} />)}
            </div>
          </Card>
          <Card className="p-4 space-y-3">
            <Checkbox label="Contains policy pending approval" description="Shows the amber warning; AI assistant must hand off to a human." checked={d.policy_pending || hasPolicySection} onChange={(v) => up({ policy_pending: v })} disabled={hasPolicySection} />
            <Checkbox label="Available to AI assistant" description="Published content only; internal notes are always excluded." checked={d.ai_visible} onChange={(v) => up({ ai_visible: v })} />
          </Card>
        </aside>
      </div>
    </div>
  );
}
