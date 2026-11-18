import { useState } from 'react';
import { Link } from 'react-router-dom';
import { ArrowUpCircle, Gavel, Pencil, AlarmClock, Layers } from 'lucide-react';
import { api, qs, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { relTime, dateTime, toLocalInput } from '../lib/format.js';
import { Badge, Button, Card, Checkbox, EmptyState, ErrorState, Field, Input, Loading, Modal, PageHeader, PriorityBadge, Select, StatusBadge, Textarea, useToast, cx } from '../components/ui.jsx';

const LEVELS = [
  { level: 1, title: 'Level 1 · Customer Support', desc: 'Routine questions and basic troubleshooting. Agents resolve using the knowledge base.' },
  { level: 2, title: 'Level 2 · Senior Support / Supervisor', desc: 'Complex complaints, disputes, repeated unresolved issues, anything policy-pending.' },
  { level: 3, title: 'Level 3 · Specialized Department', desc: 'Payments & Finance, Technical, Seller Operations, Trust & Safety, Logistics.' },
  { level: 4, title: 'Level 4 · Management', desc: 'Critical issues requiring management decisions, legal, media, policy exceptions.' },
];

function UpdateModal({ e, open, onClose, onDone, mode }) {
  const toast = useToast();
  const { can } = useAuth();
  const users = useApi(open ? '/users' : null, [open]);
  const [f, setF] = useState({});
  const [busy, setBusy] = useState(false);
  if (open && f._id !== e?.id) setF({ _id: e?.id, progress: '', status: e?.status, assignee_id: e?.assignee_id || '', expected_followup_at: e?.expected_followup_at ? toLocalInput(e.expected_followup_at) : '', decision: '', cancel: false });
  const submit = async () => {
    setBusy(true);
    try {
      if (mode === 'decide') await api(`/escalations/${e.id}/decide`, { method: 'POST', body: { decision: f.decision, cancel: f.cancel } });
      else {
        const body = {};
        if (f.progress.trim()) body.progress = f.progress;
        if (f.status !== e.status) body.status = f.status;
        if (can('escalations.manage') && String(f.assignee_id || '') !== String(e.assignee_id || '')) body.assignee_id = f.assignee_id ? Number(f.assignee_id) : null;
        if (f.expected_followup_at && toLocalInput(e.expected_followup_at) !== f.expected_followup_at) body.expected_followup_at = new Date(f.expected_followup_at).toISOString();
        await api(`/escalations/${e.id}`, { method: 'PATCH', body });
      }
      toast.success(mode === 'decide' ? 'Decision recorded' : 'Escalation updated');
      onDone();
    } catch (err) { toast.error(err); } finally { setBusy(false); }
  };
  if (!e) return null;
  return (
    <Modal open={open} onClose={onClose} title={mode === 'decide' ? `Record decision — ${e.number}` : `Update escalation — ${e.number}`} size="md"
      footer={<><Button onClick={onClose}>Cancel</Button><Button variant="primary" loading={busy} disabled={mode === 'decide' && f.decision?.trim().length < 10} onClick={submit}>{mode === 'decide' ? (f.cancel ? 'Cancel escalation' : 'Record decision') : 'Save'}</Button></>}>
      <div className="space-y-3">
        <div className="rounded-lg surface-2 p-3 text-sm"><div className="text-xs text-muted mb-1">Reason</div>{e.reason}</div>
        {mode === 'decide' ? (<>
          <Field label="Final decision" required hint="What was decided and what the support agent should tell the customer. The ticket moves to In Progress."><Textarea rows={4} value={f.decision} onChange={(x) => setF({ ...f, decision: x.target.value })} /></Field>
          <Checkbox label="Cancel instead (escalation no longer needed)" checked={f.cancel} onChange={(v) => setF({ ...f, cancel: v })} />
        </>) : (<>
          <Field label="Progress update"><Textarea rows={3} value={f.progress} onChange={(x) => setF({ ...f, progress: x.target.value })} placeholder="e.g. Requested settlement report from Chapa." /></Field>
          <div className="grid grid-cols-2 gap-3">
            <Field label="State"><Select value={f.status} onChange={(x) => setF({ ...f, status: x.target.value })}><option value="open">Open</option><option value="in_progress">In progress</option></Select></Field>
            <Field label="Expected follow-up"><Input type="datetime-local" value={f.expected_followup_at} onChange={(x) => setF({ ...f, expected_followup_at: x.target.value })} /></Field>
          </div>
          {can('escalations.manage') && <Field label="Assigned person"><Select value={f.assignee_id} onChange={(x) => setF({ ...f, assignee_id: x.target.value })}><option value="">Department queue</option>{(users.data || []).map((u) => <option key={u.id} value={u.id}>{u.name}</option>)}</Select></Field>}
        </>)}
      </div>
    </Modal>
  );
}

export default function Escalations() {
  const { settings, user, can } = useAuth();
  const depts = settings?.departments || [];
  const [f, setF] = useState({ status: 'active', level: '', department: '', mine: '' });
  const { data, loading, error, reload } = useApi(`/escalations${qs(f)}`, [JSON.stringify(f)]);
  const [modal, setModal] = useState(null);
  const deptName = (k) => depts.find((d) => d.key === k)?.name || k;
  const byLevel = [2, 3, 4].map((lv) => ({ lv, n: (data || []).filter((e) => e.level === lv && ['open', 'in_progress'].includes(e.status)).length }));

  return (
    <div>
      <PageHeader icon={ArrowUpCircle} title="Escalation Center" subtitle="Issues that need a supervisor, a specialized department or management. Every escalation records the reason, owner, expected follow-up, progress and final decision." />
      <div className="grid md:grid-cols-4 gap-3 mb-5">
        {LEVELS.map((l) => (
          <Card key={l.level} className={cx('p-3.5', l.level > 1 && 'cursor-pointer hover:border-brand-300', String(l.level) === f.level && 'ring-2 ring-brand-500/40')} onClick={() => l.level > 1 && setF({ ...f, level: String(l.level) === f.level ? '' : String(l.level) })}>
            <div className="flex items-center justify-between"><span className="text-sm font-semibold">{l.title}</span>{l.level > 1 && <span className="text-lg font-semibold tabular-nums">{byLevel.find((x) => x.lv === l.level)?.n ?? 0}</span>}</div>
            <p className="text-xs text-muted mt-1">{l.desc}</p>
          </Card>
        ))}
      </div>
      <div className="flex flex-wrap gap-2 mb-4">
        <Select className="w-auto" value={f.status} onChange={(e) => setF({ ...f, status: e.target.value })}><option value="active">Active (open & in progress)</option><option value="open">Open</option><option value="in_progress">In progress</option><option value="decided">Decided</option><option value="cancelled">Cancelled</option><option value="all">All</option></Select>
        <Select className="w-auto" value={f.department} onChange={(e) => setF({ ...f, department: e.target.value })}><option value="">All departments</option>{depts.filter((d) => d.level > 1).map((d) => <option key={d.key} value={d.key}>{d.name}</option>)}</Select>
        <Select className="w-auto" value={f.mine} onChange={(e) => setF({ ...f, mine: e.target.value })}><option value="">Everyone</option><option value="1">Assigned to / raised by me</option></Select>
      </div>
      {loading && !data ? <Loading /> : error ? <ErrorState error={error} onRetry={reload} /> : data.length === 0 ? <Card><EmptyState icon={Layers} title="No escalations in this view" /></Card> : (
        <div className="space-y-3">
          {data.map((e) => {
            const mineToHandle = e.assignee_id === user.id || can('escalations.manage');
            const active = ['open', 'in_progress'].includes(e.status);
            return (
              <Card key={e.id} className={cx('p-4', e.followup_overdue && 'border-red-300 dark:border-red-900')}>
                <div className="flex flex-wrap items-start justify-between gap-3">
                  <div className="min-w-0 flex-1">
                    <div className="flex flex-wrap items-center gap-2 text-xs">
                      <Badge tone={e.level === 4 ? 'red' : e.level === 3 ? 'orange' : 'amber'}>Level {e.level}</Badge>
                      <span className="font-medium">{deptName(e.department)}</span>
                      <Badge tone={e.status === 'decided' ? 'green' : e.status === 'cancelled' ? 'gray' : e.status === 'in_progress' ? 'blue' : 'orange'} className="capitalize">{e.status.replace('_', ' ')}</Badge>
                      {e.followup_overdue && <Badge tone="red"><AlarmClock className="size-3" />Follow-up overdue</Badge>}
                    </div>
                    <Link to={`/tickets/${e.number}`} className="block mt-1.5 font-medium hover:text-brand-600"><span className="font-mono text-xs text-muted mr-2">{e.number}</span>{e.title}</Link>
                    <div className="flex flex-wrap items-center gap-2 mt-1"><PriorityBadge priority={e.priority} /><StatusBadge status={e.ticket_status} /><span className="text-xs text-muted">{e.customer_name}</span></div>
                    <p className="text-sm mt-2.5"><span className="text-muted">Reason: </span>{e.reason}</p>
                    {e.progress && <p className="text-sm mt-1"><span className="text-muted">Progress: </span>{e.progress}</p>}
                    {e.decision && <p className="text-sm mt-1"><span className="text-muted">Decision: </span>{e.decision} <span className="text-xs text-muted">— {e.decider?.name}, {relTime(e.decided_at)}</span></p>}
                  </div>
                  <div className="text-right text-xs text-muted space-y-1 shrink-0">
                    <div>Raised by <strong className="text-[var(--text)]">{e.creator?.name}</strong> · {relTime(e.created_at)}</div>
                    <div>Owner: <strong className="text-[var(--text)]">{e.assignee?.name || 'Department queue'}</strong></div>
                    {e.expected_followup_at && <div title={dateTime(e.expected_followup_at)}>Follow up {relTime(e.expected_followup_at)}</div>}
                    {active && mineToHandle && (
                      <div className="flex gap-2 justify-end pt-1.5">
                        <Button size="xs" icon={Pencil} onClick={() => setModal({ e, mode: 'update' })}>Update</Button>
                        <Button size="xs" variant="primary" icon={Gavel} onClick={() => setModal({ e, mode: 'decide' })}>Decide</Button>
                      </div>
                    )}
                  </div>
                </div>
              </Card>
            );
          })}
        </div>
      )}
      <UpdateModal e={modal?.e} mode={modal?.mode} open={!!modal} onClose={() => setModal(null)} onDone={() => { setModal(null); reload(true); }} />
    </div>
  );
}
