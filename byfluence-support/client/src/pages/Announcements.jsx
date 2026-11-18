import { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import { Megaphone, Plus, Pin, Pencil, Archive, CheckCheck, Eye } from 'lucide-react';
import { api, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { dateTime, relTime, toLocalInput } from '../lib/format.js';
import { Badge, Button, Card, Checkbox, EmptyState, ErrorState, Field, Input, Loading, Modal, PageHeader, Select, Segmented, useConfirm, useToast, cx } from '../components/ui.jsx';
import RichText from '../components/RichText.jsx';
import Editor from '../components/Editor.jsx';

const KINDS = { update: 'Update', policy: 'Policy change', feature: 'New feature', incident: 'Technical issue', maintenance: 'Service interruption', instruction: 'Support instruction' };
const PRI = { normal: { label: 'Normal', tone: 'gray' }, important: { label: 'Important', tone: 'amber' }, critical: { label: 'Critical', tone: 'red' } };

function AnnouncementForm({ open, onClose, onDone, item }) {
  const toast = useToast();
  const [f, setF] = useState({});
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    if (open) setF(item ? { ...item, expires_at: item.expires_at ? toLocalInput(item.expires_at) : '', mark_unread_for_all: false } : { title: '', body: '', priority: 'normal', kind: 'update', status: 'published', pinned: false, expires_at: '' });
  }, [open, item]);
  const save = async () => {
    setBusy(true);
    try {
      const body = { title: f.title, body: f.body, priority: f.priority, kind: f.kind, status: f.status, pinned: !!f.pinned, expires_at: f.expires_at ? new Date(f.expires_at).toISOString() : null, mark_unread_for_all: f.mark_unread_for_all };
      if (item) await api(`/announcements/${item.id}`, { method: 'PUT', body }); else await api('/announcements', { method: 'POST', body });
      toast.success(item ? 'Announcement updated' : 'Announcement published'); onDone();
    } catch (e) { toast.error(e); } finally { setBusy(false); }
  };
  return (
    <Modal open={open} onClose={onClose} title={item ? 'Edit announcement' : 'New announcement'} size="lg"
      footer={<><Button onClick={onClose}>Cancel</Button><Button variant="primary" loading={busy} disabled={!f.title?.trim()} onClick={save}>{f.status === 'draft' ? 'Save draft' : 'Publish'}</Button></>}>
      <div className="space-y-3">
        <Field label="Title" required><Input value={f.title || ''} onChange={(e) => setF({ ...f, title: e.target.value })} placeholder="e.g. Telebirr payments are now live" /></Field>
        <div className="grid sm:grid-cols-4 gap-3">
          <Field label="Type"><Select value={f.kind} onChange={(e) => setF({ ...f, kind: e.target.value })}>{Object.entries(KINDS).map(([k, v]) => <option key={k} value={k}>{v}</option>)}</Select></Field>
          <Field label="Priority"><Select value={f.priority} onChange={(e) => setF({ ...f, priority: e.target.value })}>{Object.entries(PRI).map(([k, v]) => <option key={k} value={k}>{v.label}</option>)}</Select></Field>
          <Field label="Status"><Select value={f.status} onChange={(e) => setF({ ...f, status: e.target.value })}><option value="published">Published</option><option value="draft">Draft</option><option value="archived">Archived</option></Select></Field>
          <Field label="Expires (optional)"><Input type="datetime-local" value={f.expires_at || ''} onChange={(e) => setF({ ...f, expires_at: e.target.value })} /></Field>
        </div>
        <Field label="Message"><Editor value={f.body} onChange={(html) => setF((x) => ({ ...x, body: html }))} compact minHeight={160} /></Field>
        <div className="flex flex-wrap gap-5">
          <Checkbox label="Pin to top" checked={!!f.pinned} onChange={(v) => setF({ ...f, pinned: v })} />
          {item && <Checkbox label="Mark as unread for everyone" description="Use when the update changes significantly" checked={!!f.mark_unread_for_all} onChange={(v) => setF({ ...f, mark_unread_for_all: v })} />}
        </div>
      </div>
    </Modal>
  );
}

export default function Announcements() {
  const { can } = useAuth();
  const toast = useToast();
  const confirm = useConfirm();
  const loc = useLocation();
  const manage = can('announcements.manage');
  const [scope, setScope] = useState('active');
  const { data, loading, error, reload, setData } = useApi(`/announcements?scope=${scope}`, [scope]);
  const [form, setForm] = useState(null);

  useEffect(() => {
    if (loc.hash && data) setTimeout(() => document.getElementById(loc.hash.slice(1))?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
  }, [loc.hash, data]);

  const markRead = async (a) => {
    if (a.is_read) return;
    await api(`/announcements/${a.id}/read`, { method: 'POST' }).catch(() => {});
    setData((d) => d.map((x) => (x.id === a.id ? { ...x, is_read: true, read_count: x.read_count + 1 } : x)));
    window.dispatchEvent(new Event('byf:refresh-counts'));
  };

  if (loading && !data) return <Loading />;
  if (error) return <ErrorState error={error} onRetry={reload} />;
  const unread = data.filter((a) => !a.is_read).length;
  return (
    <div className="max-w-4xl">
      <PageHeader icon={Megaphone} title="Internal Announcements" subtitle="New payment methods, policy changes, feature launches, known technical issues and new support instructions."
        actions={<>
          {manage && <Segmented value={scope} onChange={setScope} options={[{ value: 'active', label: 'Active' }, { value: 'all', label: 'All incl. drafts & expired' }]} />}
          {unread > 0 && <Button icon={CheckCheck} onClick={async () => { await api('/announcements/read-all', { method: 'POST' }); reload(true); window.dispatchEvent(new Event('byf:refresh-counts')); }}>Mark all read</Button>}
          {manage && <Button variant="primary" icon={Plus} onClick={() => setForm({ item: null })}>New announcement</Button>}
        </>} />
      {data.length === 0 ? <Card><EmptyState icon={Megaphone} title="No announcements" /></Card> : (
        <div className="space-y-3">
          {data.map((a) => (
            <Card key={a.id} id={`a${a.id}`} className={cx('p-5 scroll-mt-20', !a.is_read && 'border-l-4 border-l-brand-500', a.priority === 'critical' && 'border-red-300 dark:border-red-900')} onMouseEnter={() => markRead(a)} onClick={() => markRead(a)}>
              <div className="flex flex-wrap items-start justify-between gap-3">
                <div className="min-w-0">
                  <div className="flex flex-wrap items-center gap-1.5 mb-1.5">
                    {a.pinned && <Badge tone="blue"><Pin className="size-3" />Pinned</Badge>}
                    <Badge tone={PRI[a.priority].tone}>{PRI[a.priority].label}</Badge>
                    <Badge tone="gray">{KINDS[a.kind] || a.kind}</Badge>
                    {a.status !== 'published' && <Badge tone="slate" className="capitalize">{a.status}</Badge>}
                    {a.expired && <Badge tone="slate">Expired</Badge>}
                    {a.is_demo && <Badge tone="slate">Demo</Badge>}
                    {!a.is_read && <Badge tone="blue">New</Badge>}
                  </div>
                  <h2 className="text-[17px] font-semibold">{a.title}</h2>
                  <p className="text-xs text-muted mt-1">{a.author_name} · {dateTime(a.published_at || a.created_at)}{a.expires_at ? ` · expires ${relTime(a.expires_at)}` : ''}</p>
                </div>
                {manage && (
                  <div className="flex gap-1.5">
                    <span className="text-xs text-muted flex items-center gap-1 mr-1" title="Employees who read it"><Eye className="size-3.5" />{a.read_count}/{a.team_size}</span>
                    <Button size="xs" icon={Pencil} onClick={(e) => { e.stopPropagation(); setForm({ item: a }); }}>Edit</Button>
                    {a.status !== 'archived' && <Button size="xs" icon={Archive} onClick={async (e) => { e.stopPropagation(); if (await confirm({ title: 'Archive announcement?', message: 'It will disappear for employees. You can restore it from “All”.', confirmLabel: 'Archive' })) { await api(`/announcements/${a.id}`, { method: 'PUT', body: { status: 'archived' } }).then(() => { toast.success('Archived'); reload(true); }).catch(toast.error); } }}>Archive</Button>}
                  </div>
                )}
              </div>
              <RichText html={a.body} className="mt-3" />
            </Card>
          ))}
        </div>
      )}
      <AnnouncementForm open={!!form} item={form?.item} onClose={() => setForm(null)} onDone={() => { setForm(null); reload(true); }} />
    </div>
  );
}
