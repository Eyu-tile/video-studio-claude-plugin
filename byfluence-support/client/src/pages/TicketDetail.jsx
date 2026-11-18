import { useEffect, useMemo, useRef, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import {
  ArrowLeft, ArrowUpCircle, CheckCircle2, XCircle, RotateCcw, MessageSquare, StickyNote, CalendarClock, Paperclip, UserPlus, Flag, PlusCircle, Pencil,
  Phone, Mail, Send, MessageCircle, FileText, Clock, AlarmClock, Download, Trash2, Star, Lightbulb, MessageSquareText, Link2, Inbox, Gavel, RefreshCcw, ShieldAlert, User, Tag,
} from 'lucide-react';
import { api, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { STATUS, PRIORITY, CHANNELS, MANUAL_STATUSES, dateTime, relTime, hours, bytes, toLocalInput } from '../lib/format.js';
import {
  Avatar, Badge, Button, Callout, Card, ErrorState, Field, Input, Loading, Menu, MenuItem, Modal, PriorityBadge, Select, StatusBadge, Tabs, Textarea, useConfirm, useToast, cx, Segmented,
} from '../components/ui.jsx';
import { CloseModal, EscalateModal, ReopenModal, ResolveModal } from '../components/TicketActions.jsx';
import TemplateFiller from '../components/TemplateFiller.jsx';
import { sensitiveWarning } from '../components/NewTicketModal.jsx';

const CH_ICON = { telegram: Send, email: Mail, phone: Phone, chat: MessageCircle, sms: MessageSquare, website: Inbox, other: MessageSquare };

function eventView(e, depts) {
  const d = e.data;
  const dept = (k) => depts.find((x) => x.key === k)?.name || k;
  switch (e.type) {
    case 'reported': return { icon: Inbox, tone: 'gray', text: <>Customer reported the issue via <strong>{CHANNELS[d.channel] || d.channel}</strong></> };
    case 'created': return { icon: PlusCircle, tone: 'blue', text: <>Ticket <strong>{d.number}</strong> created{d.via ? ` via ${d.via}` : ''}</>, body: d.conversation_summary };
    case 'assigned': return { icon: UserPlus, tone: 'gray', text: d.to ? <>Assigned to <strong>{d.to_name}</strong>{d.from_name ? <> (from {d.from_name})</> : ''}</> : <>Unassigned{d.from_name ? ` (was ${d.from_name})` : ''}</> };
    case 'status_changed': return { icon: RefreshCcw, tone: 'gray', text: <>Status changed from <StatusBadge status={d.from} /> to <StatusBadge status={d.to} /></>, body: d.reason };
    case 'priority_changed': return { icon: Flag, tone: 'gray', text: <>Priority changed from <PriorityBadge priority={d.from} /> to <PriorityBadge priority={d.to} /></>, body: d.reason };
    case 'updated': return { icon: Pencil, tone: 'gray', text: <>Updated {d.fields?.map((f) => f.replace(/_/g, ' ')).join(', ')}</> };
    case 'note': return { icon: StickyNote, tone: 'amber', text: <>Internal note</>, body: d.text, internal: true };
    case 'communication': {
      const I = CH_ICON[d.channel] || MessageSquare;
      const who = d.party === 'seller' ? 'seller' : d.party === 'department' ? 'department' : 'customer';
      const label = d.direction === 'inbound' ? `Message from ${who}` : d.direction === 'attempt' ? `Contact attempt to ${who} (no answer)` : `Message to ${who}`;
      return { icon: I, tone: d.direction === 'inbound' ? 'violet' : 'green', text: <>{label} · <span className="text-muted">{CHANNELS[d.channel]}</span>{d.template && <Badge tone="gray" className="ml-1.5">{d.template}</Badge>}</>, body: d.summary };
    }
    case 'escalated': return { icon: ArrowUpCircle, tone: 'red', text: <>Escalated to <strong>Level {d.level} · {dept(d.department)}</strong>{d.assignee_name ? <> — {d.assignee_name}</> : ''}</>, body: d.reason };
    case 'escalation_updated': return { icon: ArrowUpCircle, tone: 'orange', text: <>Escalation updated{d.status ? ` (${d.status.replace('_', ' ')})` : ''}{d.assignee_name ? ` — reassigned to ${d.assignee_name}` : ''}</>, body: d.progress };
    case 'escalation_decided': return { icon: Gavel, tone: 'green', text: <>Escalation decision recorded · Level {d.level} · {dept(d.department)}</>, body: d.decision };
    case 'escalation_cancelled': return { icon: XCircle, tone: 'gray', text: <>Escalation cancelled</>, body: d.decision };
    case 'followup_set': return { icon: CalendarClock, tone: 'amber', text: <>Follow-up set for <strong>{dateTime(d.due_at)}</strong>{d.assignee_name ? ` · ${d.assignee_name}` : ''}</>, body: d.reason };
    case 'followup_done': return { icon: CheckCircle2, tone: 'green', text: <>Follow-up completed</>, body: [d.reason, d.note].filter(Boolean).join(' — ') };
    case 'followup_cancelled': return { icon: XCircle, tone: 'gray', text: <>Follow-up cancelled</>, body: d.reason };
    case 'followup_rescheduled': return { icon: CalendarClock, tone: 'gray', text: <>Follow-up moved to {dateTime(d.to)}</> };
    case 'attachment': return { icon: Paperclip, tone: 'gray', text: <>Attached <strong>{d.filename}</strong> ({bytes(d.size)})</>, body: d.description };
    case 'attachment_removed': return { icon: Trash2, tone: 'gray', text: <>Removed attachment {d.filename}</> };
    case 'doc_linked': return { icon: Link2, tone: 'blue', text: <>Linked article <Link className="text-brand-600 hover:underline" to={`/kb/${d.slug}`}>{d.title}</Link></> };
    case 'resolved': return { icon: CheckCircle2, tone: 'green', text: <>Resolved {d.customer_notified ? '· customer notified' : '· customer NOT yet notified'}</>, body: `Root cause: ${d.root_cause}\nActions: ${d.actions_taken}\nResolution: ${d.resolution}${d.evidence ? `\nEvidence: ${d.evidence}` : ''}` };
    case 'closed': return { icon: CheckCircle2, tone: 'gray', text: <>Ticket closed · {String(d.close_type).replace('_', ' ')}{d.was_resolved ? '' : ' (without resolution)'}</>, body: d.note };
    case 'reopened': return { icon: RotateCcw, tone: 'pink', text: <>Ticket reopened</>, body: d.reason };
    case 'csat': return { icon: Star, tone: 'amber', text: <>Customer satisfaction recorded: <strong>{'★'.repeat(d.score)}{'☆'.repeat(5 - d.score)}</strong></>, body: d.comment };
    default: return { icon: Clock, tone: 'gray', text: e.type };
  }
}
const DOT = { gray: 'bg-slate-100 text-slate-500 dark:bg-slate-800', blue: 'bg-brand-100 text-brand-600 dark:bg-brand-900/50 dark:text-brand-300', amber: 'bg-amber-100 text-amber-600 dark:bg-amber-900/40', violet: 'bg-violet-100 text-violet-600 dark:bg-violet-900/40', green: 'bg-emerald-100 text-emerald-600 dark:bg-emerald-900/40', red: 'bg-red-100 text-red-600 dark:bg-red-900/40', orange: 'bg-orange-100 text-orange-600 dark:bg-orange-900/40', pink: 'bg-pink-100 text-pink-600 dark:bg-pink-900/40' };

function Timeline({ events, depts }) {
  const [filter, setFilter] = useState('all');
  const list = events.filter((e) => filter === 'all' || (filter === 'comms' && e.type === 'communication') || (filter === 'notes' && e.type === 'note') || (filter === 'system' && !['communication', 'note'].includes(e.type)));
  let lastDay = '';
  return (
    <Card>
      <div className="flex flex-wrap items-center justify-between gap-2 px-4 pt-4 pb-2">
        <h3 className="font-semibold text-[15px]">Issue timeline</h3>
        <Segmented size="xs" value={filter} onChange={setFilter} options={[{ value: 'all', label: `All (${events.length})` }, { value: 'comms', label: 'Communications' }, { value: 'notes', label: 'Notes' }, { value: 'system', label: 'System' }]} />
      </div>
      <ol className="px-4 pb-4">
        {list.map((e, i) => {
          const v = eventView(e, depts);
          const day = new Date(e.occurred_at).toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Africa/Addis_Ababa' });
          const showDay = day !== lastDay;
          lastDay = day;
          return (
            <li key={e.id}>
              {showDay && <div className="text-[11px] font-semibold uppercase tracking-wider text-muted mt-3 mb-2">{day}</div>}
              <div className="flex gap-3 relative">
                {i < list.length - 1 && <span className="absolute left-[13px] top-7 bottom-0 w-px bg-[var(--border)]" />}
                <span className={cx('size-7 rounded-full grid place-items-center shrink-0 relative z-[1]', DOT[v.tone])}><v.icon className="size-3.5" /></span>
                <div className="min-w-0 flex-1 pb-4">
                  <div className="text-[13.5px] flex flex-wrap items-center gap-x-1.5 gap-y-1">{v.text}</div>
                  <div className="text-[11px] text-muted mt-0.5">{new Date(e.occurred_at).toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit', hour12: true, timeZone: 'Africa/Addis_Ababa' })} EAT · {e.user?.name || 'Customer / system'}{e.created_at !== e.occurred_at && Math.abs(new Date(e.created_at) - new Date(e.occurred_at)) > 120000 ? ` · logged ${relTime(e.created_at)}` : ''}</div>
                  {v.body && <div className={cx('mt-1.5 text-[13.5px] whitespace-pre-wrap rounded-lg px-3 py-2', v.internal ? 'bg-amber-50 border border-amber-200 dark:bg-amber-950/20 dark:border-amber-900' : 'surface-2')}>{v.body}</div>}
                </div>
              </div>
            </li>
          );
        })}
        {!list.length && <li className="text-sm text-muted py-4">Nothing in this filter.</li>}
      </ol>
    </Card>
  );
}

function Composer({ t, onDone, users, canUpdate }) {
  const toast = useToast();
  const [tab, setTab] = useState('note');
  const [note, setNote] = useState('');
  const [comm, setComm] = useState({ direction: 'outbound', channel: t.channel, party: 'customer', summary: '', occurred_at: toLocalInput() });
  const [fu, setFu] = useState({ due_at: toLocalInput(new Date(Date.now() + 24 * 3600e3).toISOString()), reason: '', assignee_id: '' });
  const [files, setFiles] = useState([]);
  const [desc, setDesc] = useState('');
  const [busy, setBusy] = useState(false);
  const fileRef = useRef(null);
  const warn = sensitiveWarning(tab === 'note' ? note : comm.summary);
  const run = async (fn, msg) => { setBusy(true); try { await fn(); toast.success(msg); onDone(); return true; } catch (e) { toast.error(e); return false; } finally { setBusy(false); } };
  return (
    <Card className="overflow-hidden">
      <Tabs className="px-2" value={tab} onChange={setTab} tabs={[
        { value: 'note', label: 'Internal note', icon: StickyNote },
        ...(canUpdate ? [{ value: 'comm', label: 'Log communication', icon: MessageSquare }, { value: 'followup', label: 'Follow-up', icon: CalendarClock }, { value: 'files', label: 'Attach files', icon: Paperclip }] : []),
      ]} />
      <div className="p-4 space-y-3">
        {tab === 'note' && <>
          <Textarea rows={3} value={note} onChange={(e) => setNote(e.target.value)} placeholder="e.g. “Contacted the payment team. Waiting for transaction confirmation.” — visible to employees only." />
          <div className="flex justify-end"><Button variant="primary" loading={busy} disabled={!note.trim()} onClick={() => run(() => api(`/tickets/${t.id}/notes`, { method: 'POST', body: { text: note } }), 'Note added').then((ok) => ok && setNote(''))}>Add note</Button></div>
        </>}
        {tab === 'comm' && <>
          <div className="grid sm:grid-cols-4 gap-2">
            <Select value={comm.direction} onChange={(e) => setComm({ ...comm, direction: e.target.value })}><option value="outbound">We sent / said</option><option value="inbound">They replied</option><option value="attempt">Attempt — no answer</option></Select>
            <Select value={comm.party} onChange={(e) => setComm({ ...comm, party: e.target.value })}><option value="customer">Customer</option><option value="seller">Seller</option><option value="department">Internal department</option></Select>
            <Select value={comm.channel} onChange={(e) => setComm({ ...comm, channel: e.target.value })}>{Object.entries(CHANNELS).filter(([k]) => k !== 'any').map(([k, v]) => <option key={k} value={k}>{v}</option>)}</Select>
            <Input type="datetime-local" value={comm.occurred_at} max={toLocalInput()} onChange={(e) => setComm({ ...comm, occurred_at: e.target.value })} />
          </div>
          <Textarea rows={3} value={comm.summary} onChange={(e) => setComm({ ...comm, summary: e.target.value })} placeholder="Summary of what was said or sent (no passwords, codes or card numbers)." />
          <div className="flex items-center justify-between gap-2">
            <p className="text-[11px] text-muted">Records a contact you made — nothing is sent from here.</p>
            <Button variant="primary" loading={busy} disabled={!comm.summary.trim()} onClick={() => run(() => api(`/tickets/${t.id}/communications`, { method: 'POST', body: { ...comm, occurred_at: new Date(comm.occurred_at).toISOString() } }), 'Communication logged').then((ok) => ok && setComm({ ...comm, summary: '', occurred_at: toLocalInput() }))}>Save to timeline</Button>
          </div>
        </>}
        {tab === 'followup' && <>
          <div className="grid sm:grid-cols-3 gap-2">
            <Field label="Date & time"><Input type="datetime-local" value={fu.due_at} onChange={(e) => setFu({ ...fu, due_at: e.target.value })} /></Field>
            <Field label="Assigned to" className="sm:col-span-2"><Select value={fu.assignee_id} onChange={(e) => setFu({ ...fu, assignee_id: e.target.value })}><option value="">Ticket owner</option>{users.map((u) => <option key={u.id} value={u.id}>{u.name}</option>)}</Select></Field>
          </div>
          <Input value={fu.reason} onChange={(e) => setFu({ ...fu, reason: e.target.value })} placeholder="Reason — e.g. “Call seller again; if no answer escalate to supervisor”" />
          <div className="flex justify-end"><Button variant="primary" loading={busy} disabled={!fu.reason.trim() || !fu.due_at} onClick={() => run(() => api(`/tickets/${t.id}/followups`, { method: 'POST', body: { ...fu, due_at: new Date(fu.due_at).toISOString(), assignee_id: fu.assignee_id ? Number(fu.assignee_id) : undefined } }), 'Follow-up scheduled').then((ok) => ok && setFu({ ...fu, reason: '' }))}>Schedule follow-up</Button></div>
        </>}
        {tab === 'files' && <>
          <div onClick={() => fileRef.current?.click()} onDragOver={(e) => e.preventDefault()} onDrop={(e) => { e.preventDefault(); setFiles([...e.dataTransfer.files].slice(0, 5)); }}
            className="rounded-lg border-2 border-dashed border-base p-5 text-center text-sm text-muted cursor-pointer hover:border-brand-300">
            <Paperclip className="size-5 mx-auto mb-1.5" />
            {files.length ? files.map((f) => f.name).join(', ') : 'Drop screenshots or files here, or click to choose (PNG, JPG, WEBP, GIF, PDF, TXT · max 10 MB · up to 5)'}
          </div>
          <input ref={fileRef} type="file" multiple className="hidden" accept="image/png,image/jpeg,image/webp,image/gif,application/pdf,text/plain" onChange={(e) => setFiles([...e.target.files].slice(0, 5))} />
          <Input value={desc} onChange={(e) => setDesc(e.target.value)} placeholder="Short description (optional) — e.g. “Customer's Chapa receipt”" />
          <div className="flex justify-end"><Button variant="primary" loading={busy} disabled={!files.length} onClick={() => run(() => {
            const fd = new FormData(); files.forEach((f) => fd.append('files', f)); fd.append('description', desc);
            return api(`/tickets/${t.id}/attachments`, { method: 'POST', form: fd });
          }, 'Files attached').then((ok) => ok && (setFiles([]), setDesc('')))}>Upload</Button></div>
        </>}
        {warn && <Callout tone="warning">{warn}</Callout>}
      </div>
    </Card>
  );
}

function EditTicketModal({ t, open, onClose, onDone, cats }) {
  const toast = useToast();
  const [f, setF] = useState({});
  useEffect(() => { if (open) setF({ title: t.title, description: t.description, customer_name: t.customer_name, customer_ref: t.customer_ref || '', customer_email: t.customer_email || '', customer_phone: t.customer_phone || '', account_type: t.account_type, language: t.language, channel: t.channel, order_ref: t.order_ref || '', consultation_ref: t.consultation_ref || '', transaction_ref: t.transaction_ref || '', category_id: t.category_id || '', subcategory_id: t.subcategory_id || '' }); }, [open, t]);
  const subs = cats.find((c) => String(c.id) === String(f.category_id))?.subcategories || [];
  const set = (k) => (e) => setF({ ...f, [k]: e.target.value, ...(k === 'category_id' ? { subcategory_id: '' } : {}) });
  const save = async () => { try { await api(`/tickets/${t.id}`, { method: 'PATCH', body: { ...f, category_id: f.category_id ? Number(f.category_id) : null, subcategory_id: f.subcategory_id ? Number(f.subcategory_id) : null } }); toast.success('Ticket updated'); onDone(); } catch (e) { toast.error(e); } };
  return (
    <Modal open={open} onClose={onClose} title={`Edit ${t.number}`} size="lg" footer={<><Button onClick={onClose}>Cancel</Button><Button variant="primary" onClick={save}>Save changes</Button></>}>
      <div className="grid sm:grid-cols-2 gap-3">
        <Field label="Issue title" className="sm:col-span-2"><Input value={f.title || ''} onChange={set('title')} /></Field>
        <Field label="Description" className="sm:col-span-2"><Textarea rows={4} value={f.description || ''} onChange={set('description')} /></Field>
        <Field label="Category"><Select value={f.category_id} onChange={set('category_id')}><option value="">—</option>{cats.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</Select></Field>
        <Field label="Subcategory"><Select value={f.subcategory_id} onChange={set('subcategory_id')}><option value="">—</option>{subs.map((s) => <option key={s.id} value={s.id}>{s.name}</option>)}</Select></Field>
        <Field label="Customer name"><Input value={f.customer_name || ''} onChange={set('customer_name')} /></Field>
        <Field label="Customer ID"><Input value={f.customer_ref || ''} onChange={set('customer_ref')} /></Field>
        <Field label="Email"><Input value={f.customer_email || ''} onChange={set('customer_email')} /></Field>
        <Field label="Phone"><Input value={f.customer_phone || ''} onChange={set('customer_phone')} /></Field>
        <Field label="Account type"><Select value={f.account_type} onChange={set('account_type')}><option value="buyer">Buyer</option><option value="seller">Seller</option><option value="both">Both</option><option value="guest">Not registered</option></Select></Field>
        <Field label="Language"><Select value={f.language} onChange={set('language')}><option value="am">Amharic</option><option value="en">English</option></Select></Field>
        <Field label="Channel"><Select value={f.channel} onChange={set('channel')}>{Object.entries(CHANNELS).filter(([k]) => k !== 'any').map(([k, v]) => <option key={k} value={k}>{v}</option>)}</Select></Field>
        <Field label="Order ID"><Input value={f.order_ref || ''} onChange={set('order_ref')} /></Field>
        <Field label="Consultation ID"><Input value={f.consultation_ref || ''} onChange={set('consultation_ref')} /></Field>
        <Field label="Transaction reference"><Input value={f.transaction_ref || ''} onChange={set('transaction_ref')} /></Field>
      </div>
    </Modal>
  );
}

function TemplatePicker({ t, open, onClose, onLogged }) {
  const { data } = useApi(open ? '/templates' : null, [open]);
  const [q, setQ] = useState('');
  const [sel, setSel] = useState(null);
  useEffect(() => { if (!open) { setSel(null); setQ(''); } }, [open]);
  const list = (data || []).filter((x) => !q || `${x.name} ${x.tags.join(' ')}`.toLowerCase().includes(q.toLowerCase()));
  return (
    <Modal open={open} onClose={onClose} title={sel ? sel.name : 'Choose a response template'} subtitle={`Pre-filled with ${t.number} · ${t.customer_name}`} size="xl">
      {!sel ? (
        <div className="space-y-3">
          <Input placeholder="Search templates…" value={q} onChange={(e) => setQ(e.target.value)} />
          <div className="grid sm:grid-cols-2 gap-2 max-h-[55vh] overflow-y-auto">
            {list.map((x) => (
              <button key={x.slug} type="button" onClick={() => setSel(x)} className="text-left rounded-lg border border-base p-3 hover:border-brand-300">
                <div className="text-sm font-medium">{x.name}</div>
                <div className="text-xs text-muted mt-0.5">{x.category_name} · {CHANNELS[x.channel]} · {x.style}</div>
              </button>
            ))}
          </div>
        </div>
      ) : (
        <div className="space-y-3">
          <button type="button" className="text-xs text-brand-600" onClick={() => setSel(null)}>← Back to templates</button>
          <TemplateFiller template={sel} ticket={t} onLogged={() => { onLogged(); onClose(); }} />
        </div>
      )}
    </Modal>
  );
}

export default function TicketDetail() {
  const { id } = useParams();
  const { user, settings, can } = useAuth();
  const toast = useToast();
  const confirm = useConfirm();
  const { data, loading, error, reload } = useApi(`/tickets/${id}`, [id]);
  const users = useApi('/users');
  const cats = useApi('/categories?scope=kb');
  const [modal, setModal] = useState(null);
  const [suggest, setSuggest] = useState([]);
  const t = data?.ticket;
  const depts = settings?.departments || [];

  useEffect(() => {
    if (!t) return;
    api(`/search?q=${encodeURIComponent(`${t.title} ${t.subcategory?.name || ''}`)}&kinds=article,troubleshooting,template&limit=6&log=0`).then((r) => setSuggest(r.results)).catch(() => {});
  }, [t?.id]); // eslint-disable-line
  const refresh = () => { reload(true); window.dispatchEvent(new Event('byf:refresh-counts')); };
  const linked = useMemo(() => new Set((data?.docs || []).map((d) => d.slug)), [data]);

  if (loading && !data) return <Loading />;
  if (error) return <ErrorState error={error} onRetry={reload} />;
  const perm = data.permissions;
  const closed = ['resolved', 'closed'].includes(t.status);
  const openEsc = data.escalations.filter((e) => ['open', 'in_progress'].includes(e.status));
  const patch = async (body, msg) => { try { await api(`/tickets/${t.id}`, { method: 'PATCH', body }); toast.success(msg); refresh(); } catch (e) { toast.error(e); } };
  const setStatus = async (s) => { try { await api(`/tickets/${t.id}/status`, { method: 'POST', body: { status: s } }); toast.success(`Status: ${STATUS[s].label}`); refresh(); } catch (e) { toast.error(e); } };
  const linkDoc = async (slug) => { try { await api(`/tickets/${t.id}/links`, { method: 'POST', body: { slug } }); refresh(); } catch (e) { toast.error(e); } };
  const followup = async (f, status) => { try { await api(`/followups/${f.id}`, { method: 'PATCH', body: { status } }); toast.success(status === 'done' ? 'Follow-up completed' : 'Follow-up cancelled'); refresh(); } catch (e) { toast.error(e); } };
  const sla = settings?.sla?.[t.priority];
  const claim = t.assignee_id == null && !closed;

  return (
    <div className="max-w-[1400px] mx-auto">
      <Link to="/tickets" className="text-xs text-muted hover:text-brand-600 inline-flex items-center gap-1 mb-2"><ArrowLeft className="size-3" />Customer Issues</Link>
      <div className="flex flex-wrap items-start justify-between gap-3 mb-5">
        <div className="min-w-0">
          <div className="flex flex-wrap items-center gap-2 mb-1.5">
            <span className="font-mono text-sm text-muted">{t.number}</span>
            <StatusBadge status={t.status} /><PriorityBadge priority={t.priority} />
            {t.overdue && <Badge tone="red"><AlarmClock className="size-3" />Overdue</Badge>}
            {t.escalation_level > 1 && <Badge tone="orange">Escalation level {t.escalation_level}</Badge>}
            {t.reopen_count > 0 && <Badge tone="pink">Reopened ×{t.reopen_count}</Badge>}
            {t.is_demo && <Badge tone="slate">Demo data</Badge>}
          </div>
          <h1 className="text-xl font-semibold tracking-tight">{t.title}</h1>
          <p className="text-xs text-muted mt-1">Reported {dateTime(t.reported_at)} via {CHANNELS[t.channel]} · Created by {t.creator?.name || 'integration'}</p>
        </div>
        <div className="flex flex-wrap gap-2">
          {claim && <Button variant="primary" icon={UserPlus} onClick={() => patch({ assignee_id: user.id }, 'Ticket assigned to you')}>Assign to me</Button>}
          {perm.update && !closed && <Button icon={MessageSquareText} onClick={() => setModal('template')}>Use template</Button>}
          {perm.update && !closed && (
            <Menu trigger={({ toggle }) => <Button icon={RefreshCcw} onClick={toggle}>Status</Button>}>
              {MANUAL_STATUSES.map((s) => <MenuItem key={s} disabled={s === t.status} onClick={() => setStatus(s)}><StatusBadge status={s} /></MenuItem>)}
            </Menu>
          )}
          {perm.update && !closed && <Button icon={ArrowUpCircle} onClick={() => setModal('escalate')}>Escalate</Button>}
          {perm.update && !closed && <Button variant="primary" icon={CheckCircle2} onClick={() => setModal('resolve')} disabled={openEsc.length > 0} title={openEsc.length ? 'Record the escalation decision first' : ''}>Resolve</Button>}
          {perm.update && t.status !== 'closed' && <Button icon={XCircle} onClick={() => setModal('close')}>Close</Button>}
          {closed && perm.reopen && <Button icon={RotateCcw} onClick={() => setModal('reopen')}>Reopen</Button>}
          {t.is_demo && can('tickets.delete_demo') && <Button variant="ghost" icon={Trash2} onClick={async () => { if (await confirm({ title: 'Delete demo ticket?', message: 'This permanently deletes this demo ticket. Real tickets can never be deleted.', danger: true, confirmLabel: 'Delete' })) { await api(`/tickets/${t.id}`, { method: 'DELETE' }); window.history.back(); } }} />}
        </div>
      </div>

      {!perm.update && <Callout tone="note" className="mb-4">You can view this ticket and add internal notes. Only the assigned employee or a supervisor can change it.{claim ? ' Click “Assign to me” to take it.' : ''}</Callout>}
      {openEsc.length > 0 && <Callout tone="warning" className="mb-4" title={`Open escalation — Level ${openEsc[0].level} · ${depts.find((d) => d.key === openEsc[0].department)?.name}`}>Waiting for a decision{openEsc[0].assignee ? ` from ${openEsc[0].assignee.name}` : ''}. Do not promise the customer an outcome until it is recorded.</Callout>}

      <div className="grid lg:grid-cols-[1fr_340px] gap-5">
        <div className="space-y-5 min-w-0">
          <Card className="p-5">
            <div className="flex items-start justify-between gap-3">
              <h3 className="font-semibold text-[15px]">Issue summary</h3>
              {perm.update && t.status !== 'closed' && <Button size="xs" variant="ghost" icon={Pencil} onClick={() => setModal('edit')}>Edit</Button>}
            </div>
            <p className="text-[14px] whitespace-pre-wrap mt-2 leading-relaxed">{t.description}</p>
            <div className="grid sm:grid-cols-3 gap-3 mt-4 text-sm">
              {[['Category', t.category?.name], ['Subcategory', t.subcategory?.name], ['Order ID', t.order_ref], ['Consultation ID', t.consultation_ref], ['Transaction ref.', t.transaction_ref]].map(([k, v]) => (
                <div key={k}><div className="text-xs text-muted">{k}</div><div className="font-medium break-all">{v || '—'}</div></div>
              ))}
            </div>
            {data.docs.length > 0 && <div className="flex flex-wrap gap-1.5 mt-4">{data.docs.map((d) => <Link key={d.slug} to={`/kb/${d.slug}`}><Badge tone="blue" className="cursor-pointer"><FileText className="size-3" />{d.title}</Badge></Link>)}</div>}
          </Card>

          {(t.resolution || t.close_reason) && (
            <Card className="p-5 border-emerald-200 dark:border-emerald-900">
              <h3 className="font-semibold text-[15px] flex items-center gap-2"><CheckCircle2 className="size-4 text-emerald-600" />{closed ? 'Resolution' : 'Previous resolution (before reopening)'}</h3>
              {t.resolution ? (
                <dl className="grid sm:grid-cols-2 gap-x-6 gap-y-3 mt-3 text-sm">
                  <div><dt className="text-xs text-muted">Root cause</dt><dd>{t.root_cause}</dd></div>
                  {t.resolved_at && <div><dt className="text-xs text-muted">Resolved</dt><dd>{dateTime(t.resolved_at)}</dd></div>}
                  <div className="sm:col-span-2"><dt className="text-xs text-muted">Actions taken</dt><dd className="whitespace-pre-wrap">{t.actions_taken}</dd></div>
                  <div className="sm:col-span-2"><dt className="text-xs text-muted">Final resolution</dt><dd className="whitespace-pre-wrap">{t.resolution}</dd></div>
                  <div><dt className="text-xs text-muted">Customer notified</dt><dd>{t.customer_notified ? 'Yes' : <span className="text-amber-600 font-medium">Not yet</span>}</dd></div>
                  {t.close_reason && <div><dt className="text-xs text-muted">Closed as</dt><dd className="capitalize">{t.close_reason.replace('_', ' ')}</dd></div>}
                </dl>
              ) : <p className="text-sm mt-2">Closed without resolution: <strong className="capitalize">{t.close_reason?.replace('_', ' ')}</strong> — see timeline for the explanation.</p>}
              {t.status === 'resolved' && <div className="mt-4 flex flex-wrap gap-2 items-center">
                <span className="text-xs text-muted">Customer satisfaction:</span>
                {[1, 2, 3, 4, 5].map((n) => <button key={n} type="button" disabled={!perm.update} onClick={async () => { try { await api(`/tickets/${t.id}/csat`, { method: 'POST', body: { score: n } }); refresh(); } catch (e) { toast.error(e); } }} className={cx('text-lg leading-none', (t.csat || 0) >= n ? 'text-amber-400' : 'text-slate-300 dark:text-slate-600')} aria-label={`${n} stars`}>★</button>)}
              </div>}
            </Card>
          )}

          {t.status !== 'closed' && <Composer t={t} canUpdate={perm.update} users={users.data || []} onDone={refresh} />}
          <Timeline events={data.events} depts={depts} />
        </div>

        <aside className="space-y-4">
          <Card className="p-4">
            <div className="flex items-center justify-between mb-3"><h3 className="font-semibold text-sm flex items-center gap-1.5"><User className="size-4 text-brand-500" />Customer</h3><Badge tone="gray" className="capitalize">{t.account_type}</Badge></div>
            <div className="font-medium">{t.customer_name}</div>
            <div className="text-sm space-y-1 mt-2 text-muted">
              {t.customer_ref && <div>ID: <span className="text-[var(--text)]">{t.customer_ref}</span></div>}
              {t.customer_email && <div className="break-all">{t.customer_email}</div>}
              {t.customer_phone && <div>{t.customer_phone}</div>}
              <div>Prefers {t.language === 'am' ? 'Amharic' : 'English'} · {CHANNELS[t.channel]}</div>
            </div>
            {data.customer_history.length > 0 && (
              <div className="mt-3 pt-3 border-t border-base">
                <div className="text-xs font-medium text-muted mb-1.5">Other tickets from this customer</div>
                {data.customer_history.map((h) => <Link key={h.id} to={`/tickets/${h.number}`} className="flex items-center justify-between gap-2 text-xs py-1 hover:text-brand-600"><span className="truncate">{h.number} · {h.title}</span><StatusBadge status={h.status} /></Link>)}
              </div>
            )}
          </Card>

          <Card className="p-4 space-y-3 text-sm">
            <h3 className="font-semibold text-sm">Details</h3>
            <Field label="Assigned employee">
              <Select value={t.assignee_id || ''} disabled={!perm.assign || closed} onChange={(e) => patch({ assignee_id: e.target.value ? Number(e.target.value) : null }, 'Assignment updated')}>
                <option value="">Unassigned</option>{(users.data || []).map((u) => <option key={u.id} value={u.id}>{u.name}</option>)}
              </Select>
            </Field>
            <Field label="Priority">
              <Select value={t.priority} disabled={!perm.update || closed} onChange={(e) => patch({ priority: e.target.value }, 'Priority updated')}>{Object.entries(PRIORITY).map(([k, v]) => <option key={k} value={k}>{v.label}</option>)}</Select>
            </Field>
            <dl className="grid grid-cols-2 gap-y-2 gap-x-3 pt-1">
              <dt className="text-muted">Internal target</dt><dd className={cx(t.overdue && 'text-red-600 font-medium')}>{t.is_open ? relTime(t.due_at) : '—'}</dd>
              <dt className="text-muted">Target (priority)</dt><dd>{sla ? hours(sla.resolution_hours) : '—'}</dd>
              <dt className="text-muted">First response</dt><dd>{t.first_response_at ? relTime(t.first_response_at).replace('ago', 'ago') : <span className="text-amber-600">Not yet</span>}</dd>
              <dt className="text-muted">Last update</dt><dd>{relTime(t.updated_at)}</dd>
              {t.csat && <><dt className="text-muted">CSAT</dt><dd>{'★'.repeat(t.csat)}</dd></>}
            </dl>
          </Card>

          <Card className="p-4">
            <div className="flex items-center justify-between mb-2"><h3 className="font-semibold text-sm flex items-center gap-1.5"><ArrowUpCircle className="size-4 text-orange-500" />Escalations</h3><Link to="/escalations" className="text-xs text-brand-600">Center</Link></div>
            {data.escalations.length === 0 ? <p className="text-sm text-muted">Not escalated.</p> : data.escalations.map((e) => (
              <div key={e.id} className="rounded-lg border border-base p-2.5 mb-2 text-sm">
                <div className="flex items-center justify-between gap-2"><span className="font-medium">L{e.level} · {depts.find((d) => d.key === e.department)?.name}</span><Badge tone={e.status === 'decided' ? 'green' : e.status === 'cancelled' ? 'gray' : 'orange'} className="capitalize">{e.status.replace('_', ' ')}</Badge></div>
                <p className="text-xs text-muted mt-1 line-clamp-3">{e.reason}</p>
                {e.progress && <p className="text-xs mt-1"><strong>Progress:</strong> {e.progress}</p>}
                {e.decision && <p className="text-xs mt-1"><strong>Decision:</strong> {e.decision}</p>}
                <p className="text-[11px] text-muted mt-1">{e.assignee?.name || 'Department queue'}{e.expected_followup_at && ['open', 'in_progress'].includes(e.status) ? ` · follow up ${relTime(e.expected_followup_at)}` : ''}</p>
              </div>
            ))}
          </Card>

          <Card className="p-4">
            <h3 className="font-semibold text-sm flex items-center gap-1.5 mb-2"><CalendarClock className="size-4 text-amber-500" />Follow-ups</h3>
            {data.followups.length === 0 ? <p className="text-sm text-muted">None scheduled.</p> : data.followups.map((f) => (
              <div key={f.id} className={cx('rounded-lg border p-2.5 mb-2 text-sm', f.overdue ? 'border-red-300 bg-red-50/50 dark:bg-red-950/20 dark:border-red-900' : 'border-base')}>
                <div className="flex items-center justify-between gap-2">
                  <span className={cx('text-xs font-medium', f.overdue ? 'text-red-600' : f.status !== 'pending' ? 'text-muted' : 'text-amber-600')}>{f.status === 'pending' ? `${f.overdue ? 'Overdue' : 'Due'} ${relTime(f.due_at)}` : f.status}</span>
                  <span className="text-[11px] text-muted">{f.assignee?.name}</span>
                </div>
                <p className={cx('mt-1', f.status !== 'pending' && 'line-through text-muted')}>{f.reason}</p>
                {f.status === 'pending' && perm.update && <div className="flex gap-1.5 mt-2"><Button size="xs" icon={CheckCircle2} onClick={() => followup(f, 'done')}>Done</Button><Button size="xs" variant="ghost" onClick={() => followup(f, 'cancelled')}>Cancel</Button></div>}
              </div>
            ))}
          </Card>

          <Card className="p-4">
            <h3 className="font-semibold text-sm flex items-center gap-1.5 mb-2"><Paperclip className="size-4 text-muted" />Evidence & files</h3>
            {data.attachments.length === 0 ? <p className="text-sm text-muted">No files attached.</p> : (
              <ul className="space-y-1.5">{data.attachments.map((a) => (
                <li key={a.id} className="flex items-center gap-2 text-sm">
                  <a href={`/api/files/${a.id}`} target="_blank" rel="noreferrer" className="flex-1 min-w-0 truncate text-brand-600 hover:underline">{a.filename}</a>
                  <span className="text-[11px] text-muted">{bytes(a.size)}</span>
                  <a href={`/api/files/${a.id}`} download aria-label="Download"><Download className="size-3.5 text-muted" /></a>
                  {can('tickets.update_all') && <button type="button" aria-label="Delete file" onClick={async () => { if (await confirm({ title: 'Delete this file?', message: `“${a.filename}” will be removed permanently. This is recorded in the audit log.`, danger: true, confirmLabel: 'Delete' })) { await api(`/files/${a.id}`, { method: 'DELETE' }); refresh(); } }}><Trash2 className="size-3.5 text-muted hover:text-red-600" /></button>}
                </li>
              ))}</ul>
            )}
            <p className="text-[11px] text-muted mt-2 flex items-center gap-1"><ShieldAlert className="size-3" />Files are private to authorized employees.</p>
          </Card>

          <Card className="p-4">
            <h3 className="font-semibold text-sm flex items-center gap-1.5 mb-2"><Lightbulb className="size-4 text-brand-500" />Suggested knowledge</h3>
            {suggest.length === 0 ? <p className="text-sm text-muted">No suggestions.</p> : (
              <ul className="space-y-1.5">{suggest.map((s) => (
                <li key={`${s.kind}-${s.slug}`} className="flex items-start gap-2 text-sm">
                  {s.kind === 'template' ? <MessageSquareText className="size-3.5 mt-0.5 text-muted shrink-0" /> : <FileText className="size-3.5 mt-0.5 text-muted shrink-0" />}
                  <Link to={s.kind === 'template' ? `/templates/${s.slug}` : `/kb/${s.slug}`} className="flex-1 hover:text-brand-600 line-clamp-2">{s.title}</Link>
                  {s.kind !== 'template' && !linked.has(s.slug) && <button type="button" title="Link to ticket" onClick={() => linkDoc(s.slug)} className="text-muted hover:text-brand-600"><Link2 className="size-3.5" /></button>}
                </li>
              ))}</ul>
            )}
          </Card>
          <p className="text-[11px] text-muted px-1 flex items-center gap-1"><Tag className="size-3" />Ticket ID {t.number} · internal #{t.id}</p>
        </aside>
      </div>

      <ResolveModal ticket={t} open={modal === 'resolve'} onClose={() => setModal(null)} onDone={() => { setModal(null); refresh(); }} />
      <CloseModal ticket={t} open={modal === 'close'} onClose={() => setModal(null)} onDone={() => { setModal(null); refresh(); }} />
      <ReopenModal ticket={t} open={modal === 'reopen'} onClose={() => setModal(null)} onDone={() => { setModal(null); refresh(); }} />
      <EscalateModal ticket={t} open={modal === 'escalate'} suggestedDept={null} onClose={() => setModal(null)} onDone={() => { setModal(null); refresh(); }} />
      <EditTicketModal t={t} cats={cats.data || []} open={modal === 'edit'} onClose={() => setModal(null)} onDone={() => { setModal(null); refresh(); }} />
      <TemplatePicker t={t} open={modal === 'template'} onClose={() => setModal(null)} onLogged={refresh} />
    </div>
  );
}
