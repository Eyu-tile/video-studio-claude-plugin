import { useEffect, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { Save, Globe, History, Eye, Archive, Trash2 } from 'lucide-react';
import { api, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { CHANNELS, placeholdersIn } from '../lib/format.js';
import { Badge, Button, Callout, Card, DocStatusBadge, ErrorState, Field, Input, Loading, Select, Textarea, useConfirm, useToast } from '../components/ui.jsx';
import Editor from '../components/Editor.jsx';

export default function TemplateEditor() {
  const { slug } = useParams();
  const nav = useNavigate();
  const toast = useToast();
  const confirm = useConfirm();
  const { can, settings } = useAuth();
  const ex = useApi(slug ? `/templates/${slug}` : null, [slug]);
  const cats = useApi('/categories?scope=template');
  const [t, setT] = useState(null);
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    if (slug && ex.data) setT({ ...ex.data.template, change_summary: '' });
    else if (!slug) setT({ name: '', category_id: '', channel: 'telegram', style: 'standard', subject_en: '', subject_am: '', content_en: '', content_am: '', usage_notes: '', tags: [], related: [], status: 'draft' });
  }, [slug, ex.data]);
  if (slug && ex.loading && !t) return <Loading />;
  if (ex.error) return <ErrorState error={ex.error} />;
  if (!t) return <Loading />;
  if (!can('templates.edit')) return <ErrorState error={{ status: 403, message: 'You cannot edit templates.' }} />;
  const up = (p) => setT((x) => ({ ...x, ...p }));
  const known = new Set((settings?.placeholders || []).map((p) => p.key));
  const unknown = placeholdersIn(t.content_en, t.content_am, t.subject_en, t.subject_am).filter((k) => !known.has(k));
  const save = async (status) => {
    setBusy(true);
    try {
      const body = { ...t, category_id: t.category_id || null, status: status || t.status, expected_version: t.version };
      const saved = slug ? await api(`/templates/${slug}`, { method: 'PUT', body }) : await api('/templates', { method: 'POST', body });
      toast.success('Template saved');
      nav(`/templates/${saved.slug}`);
    } catch (e) { toast.error(e); } finally { setBusy(false); }
  };
  return (
    <div className="max-w-5xl mx-auto">
      <div className="flex flex-wrap items-center justify-between gap-3 mb-5">
        <div>
          <Link to="/manage?tab=templates" className="text-xs text-muted hover:text-brand-600">← Documentation Management</Link>
          <h1 className="text-xl font-semibold mt-1 flex items-center gap-2">{slug ? 'Edit template' : 'New template'} {slug && <DocStatusBadge status={t.status} />}</h1>
        </div>
        <div className="flex flex-wrap gap-2">
          {slug && <Link to={`/templates/${slug}`}><Button icon={Eye}>View</Button></Link>}
          {slug && <Link to={`/manage/history/template/${slug}`}><Button icon={History}>History</Button></Link>}
          {slug && t.status !== 'archived' && <Button icon={Archive} onClick={() => save('archived')}>Archive</Button>}
          {slug && t.status === 'archived' && can('docs.delete') && <Button icon={Trash2} variant="danger" onClick={async () => { if (await confirm({ title: 'Delete template permanently?', message: 'This cannot be undone.', danger: true, typeToConfirm: 'DELETE', confirmLabel: 'Delete' })) { await api(`/templates/${slug}`, { method: 'DELETE' }).then(() => nav('/manage?tab=templates')).catch(toast.error); } }}>Delete</Button>}
          <Button icon={Save} loading={busy} onClick={() => save(slug ? undefined : 'draft')}>Save{slug ? '' : ' draft'}</Button>
          {can('docs.publish') && <Button variant="primary" icon={Globe} loading={busy} onClick={() => save('published')}>Publish</Button>}
        </div>
      </div>
      <div className="grid lg:grid-cols-[1fr_280px] gap-5">
        <div className="space-y-4 min-w-0">
          <Card className="p-4"><Field label="Template name" required><Input value={t.name} onChange={(e) => up({ name: e.target.value })} /></Field></Card>
          {['en', 'am'].map((l) => (
            <Card key={l} className="p-4 space-y-3">
              <div className="font-semibold text-sm">{l === 'am' ? 'Amharic (primary)' : 'English'}</div>
              {(t.channel === 'email' || t[`subject_${l}`]) && <Field label="Email subject"><Input value={t[`subject_${l}`] || ''} onChange={(e) => up({ [`subject_${l}`]: e.target.value })} /></Field>}
              <Field label="Message" hint="Plain text, ready to paste. Use {{placeholders}} for details agents fill in."><Textarea rows={10} lang={l} className="font-[inherit] text-[14px]" value={t[`content_${l}`]} onChange={(e) => up({ [`content_${l}`]: e.target.value })} /></Field>
            </Card>
          ))}
          {unknown.length > 0 && <Callout tone="warning">Unknown placeholders: {unknown.map((k) => `{{${k}}}`).join(', ')}. Add them in Settings → Placeholders or use an existing one.</Callout>}
          <Card className="p-4"><Field label="Usage notes" hint="When to use it, what to fill in, what NOT to promise."><Editor value={t.usage_notes} onChange={(html) => up({ usage_notes: html })} compact minHeight={100} /></Field></Card>
          {slug && <Card className="p-4"><Field label="Change summary"><Input value={t.change_summary} onChange={(e) => up({ change_summary: e.target.value })} /></Field></Card>}
        </div>
        <aside className="space-y-4">
          <Card className="p-4 space-y-3">
            <Field label="Category"><Select value={t.category_id || ''} onChange={(e) => up({ category_id: e.target.value ? Number(e.target.value) : '' })}><option value="">—</option>{(cats.data || []).map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</Select></Field>
            <Field label="Channel"><Select value={t.channel} onChange={(e) => up({ channel: e.target.value })}>{Object.entries(CHANNELS).filter(([k]) => ['telegram', 'email', 'chat', 'sms', 'phone', 'any'].includes(k)).map(([k, v]) => <option key={k} value={k}>{v}</option>)}</Select></Field>
            <Field label="Style"><Select value={t.style} onChange={(e) => up({ style: e.target.value })}>{['short', 'standard', 'detailed', 'formal', 'friendly'].map((s) => <option key={s} value={s}>{s}</option>)}</Select></Field>
            <Field label="Tags"><Input value={t.tags.join(', ')} onChange={(e) => up({ tags: e.target.value.split(',').map((x) => x.trim()).filter(Boolean) })} /></Field>
            <Field label="Related article IDs"><Input value={t.related.join(', ')} onChange={(e) => up({ related: e.target.value.split(',').map((x) => x.trim()).filter(Boolean) })} /></Field>
          </Card>
          <Card className="p-4">
            <div className="text-[13px] font-medium mb-2">Available placeholders</div>
            <div className="flex flex-wrap gap-1">{(settings?.placeholders || []).map((p) => <Badge key={p.key} tone="gray" title={p.label}>{`{{${p.key}}}`}</Badge>)}</div>
          </Card>
        </aside>
      </div>
    </div>
  );
}
