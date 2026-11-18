import { useEffect, useState } from 'react';
import { api } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { toLocalInput } from '../lib/format.js';
import { Button, Callout, Checkbox, Field, Input, Modal, Select, Textarea, useToast } from './ui.jsx';

export function ResolveModal({ ticket, open, onClose, onDone }) {
  const toast = useToast();
  const [f, setF] = useState({ root_cause: '', actions_taken: '', resolution: '', customer_notified: null, evidence: '', cancel_followups: true });
  const [busy, setBusy] = useState(false);
  useEffect(() => { if (open) setF({ root_cause: ticket?.root_cause || '', actions_taken: ticket?.actions_taken || '', resolution: ticket?.resolution || '', customer_notified: null, evidence: '', cancel_followups: true }); }, [open, ticket]);
  const ok = f.root_cause.trim() && f.actions_taken.trim() && f.resolution.trim() && f.customer_notified !== null;
  const submit = async () => {
    setBusy(true);
    try { await api(`/tickets/${ticket.id}/resolve`, { method: 'POST', body: f }); toast.success(`${ticket.number} resolved`); onDone?.(); } catch (e) { toast.error(e); } finally { setBusy(false); }
  };
  return (
    <Modal open={open} onClose={onClose} title={`Resolve ${ticket?.number || ''}`} subtitle="A ticket can only be resolved when the resolution is documented." size="lg"
      footer={<><Button onClick={onClose}>Cancel</Button><Button variant="primary" disabled={!ok} loading={busy} onClick={submit}>Mark as resolved</Button></>}>
      <div className="space-y-4">
        <Field label="Root cause" required hint="Why did this happen? e.g. “Payment provider callback delayed”"><Textarea rows={2} value={f.root_cause} onChange={(e) => setF({ ...f, root_cause: e.target.value })} /></Field>
        <Field label="Actions taken" required><Textarea rows={3} value={f.actions_taken} onChange={(e) => setF({ ...f, actions_taken: e.target.value })} /></Field>
        <Field label="Final resolution" required hint="What the outcome is for the customer"><Textarea rows={2} value={f.resolution} onChange={(e) => setF({ ...f, resolution: e.target.value })} /></Field>
        <Field label="Supporting evidence (optional)" hint="e.g. verified transaction reference, decision reference, screenshot attached"><Input value={f.evidence} onChange={(e) => setF({ ...f, evidence: e.target.value })} /></Field>
        <div>
          <div className="text-[13px] font-medium mb-1.5">Has the customer been notified of the resolution? <span className="text-red-500">*</span></div>
          <div className="flex gap-2">
            <Button size="sm" variant={f.customer_notified === true ? 'primary' : 'secondary'} onClick={() => setF({ ...f, customer_notified: true })}>Yes, notified</Button>
            <Button size="sm" variant={f.customer_notified === false ? 'primary' : 'secondary'} onClick={() => setF({ ...f, customer_notified: false })}>Not yet</Button>
          </div>
          {f.customer_notified === false && <p className="text-xs text-amber-600 mt-1.5">Remember to notify the customer and log it in the communication history.</p>}
        </div>
        <Checkbox label="Cancel pending follow-ups" checked={f.cancel_followups} onChange={(v) => setF({ ...f, cancel_followups: v })} />
      </div>
    </Modal>
  );
}

const CLOSE_TYPES = [
  ['resolved', 'Resolved and confirmed'], ['duplicate', 'Duplicate of another ticket'], ['no_response', 'Customer did not respond'],
  ['withdrawn', 'Customer withdrew the request'], ['spam', 'Spam / not a real request'], ['out_of_scope', 'Out of scope for Byfluence support'], ['other', 'Other (explain)'],
];
export function CloseModal({ ticket, open, onClose, onDone }) {
  const toast = useToast();
  const resolved = ticket?.status === 'resolved';
  const [type, setType] = useState(resolved ? 'resolved' : '');
  const [note, setNote] = useState('');
  const [busy, setBusy] = useState(false);
  useEffect(() => { if (open) { setType(resolved ? 'resolved' : ''); setNote(''); } }, [open, resolved]);
  const ok = type && (resolved || (type !== 'resolved' && note.trim().length >= 15));
  const submit = async () => {
    setBusy(true);
    try { await api(`/tickets/${ticket.id}/close`, { method: 'POST', body: { close_type: type, note } }); toast.success(`${ticket.number} closed`); onDone?.(); } catch (e) { toast.error(e); } finally { setBusy(false); }
  };
  return (
    <Modal open={open} onClose={onClose} title={`Close ${ticket?.number || ''}`} size="md"
      footer={<><Button onClick={onClose}>Cancel</Button><Button variant="primary" disabled={!ok} loading={busy} onClick={submit}>Close ticket</Button></>}>
      <div className="space-y-4">
        {!resolved && <Callout tone="warning" title="This ticket has not been resolved">Unresolved tickets can only be closed with a documented reason (e.g. duplicate, no response). If the issue was fixed, use <strong>Resolve</strong> first.</Callout>}
        <Field label="Closing reason" required>
          <Select value={type} onChange={(e) => setType(e.target.value)}>
            <option value="">Select…</option>
            {CLOSE_TYPES.filter(([k]) => resolved || k !== 'resolved').map(([k, l]) => <option key={k} value={k}>{l}</option>)}
          </Select>
        </Field>
        <Field label={resolved ? 'Closing note (optional)' : 'Explanation (required)'} hint={resolved ? '' : 'At least 15 characters. This is kept in the ticket history.'}>
          <Textarea rows={3} value={note} onChange={(e) => setNote(e.target.value)} />
        </Field>
      </div>
    </Modal>
  );
}

export function ReopenModal({ ticket, open, onClose, onDone }) {
  const toast = useToast();
  const [reason, setReason] = useState('');
  const [busy, setBusy] = useState(false);
  useEffect(() => { if (open) setReason(''); }, [open]);
  const submit = async () => {
    setBusy(true);
    try { await api(`/tickets/${ticket.id}/reopen`, { method: 'POST', body: { reason } }); toast.success(`${ticket.number} reopened`); onDone?.(); } catch (e) { toast.error(e); } finally { setBusy(false); }
  };
  return (
    <Modal open={open} onClose={onClose} title={`Reopen ${ticket?.number || ''}`} subtitle="The original history and resolution are preserved." size="md"
      footer={<><Button onClick={onClose}>Cancel</Button><Button variant="primary" disabled={reason.trim().length < 10} loading={busy} onClick={submit}>Reopen ticket</Button></>}>
      <Field label="Why is the issue not resolved?" required hint="e.g. “Customer reports the refund still has not arrived.”"><Textarea rows={3} value={reason} onChange={(e) => setReason(e.target.value)} /></Field>
    </Modal>
  );
}

const LEVELS = [
  [2, 'Level 2 — Senior Support / Supervisor', 'Complex complaints, disputes, repeated unresolved issues.'],
  [3, 'Level 3 — Specialized department', 'Payments, technical, seller operations, trust & safety, fulfillment.'],
  [4, 'Level 4 — Management', 'Critical issues requiring a management decision.'],
];
export function EscalateModal({ ticket, open, onClose, onDone, suggestedDept }) {
  const { settings } = useAuth();
  const toast = useToast();
  const [users, setUsers] = useState([]);
  const [f, setF] = useState({ level: 3, department: '', reason: '', assignee_id: '', expected_followup_at: '' });
  const [busy, setBusy] = useState(false);
  const depts = settings?.departments || [];
  useEffect(() => {
    if (!open) return;
    api('/users').then(setUsers).catch(() => {});
    const d = depts.find((x) => x.key === suggestedDept && x.level > 1);
    setF({ level: d?.level || 3, department: d?.key || '', reason: '', assignee_id: '', expected_followup_at: toLocalInput(new Date(Date.now() + 4 * 3600e3).toISOString()) });
  }, [open]); // eslint-disable-line
  const deptOptions = depts.filter((d) => d.level === Number(f.level) || (Number(f.level) === 3 && d.level === 3));
  const submit = async () => {
    setBusy(true);
    try {
      await api(`/tickets/${ticket.id}/escalations`, { method: 'POST', body: { ...f, level: Number(f.level), assignee_id: f.assignee_id ? Number(f.assignee_id) : null, expected_followup_at: f.expected_followup_at ? new Date(f.expected_followup_at).toISOString() : null } });
      toast.success(`${ticket.number} escalated`); onDone?.();
    } catch (e) { toast.error(e); } finally { setBusy(false); }
  };
  return (
    <Modal open={open} onClose={onClose} title={`Escalate ${ticket?.number || ''}`} subtitle="The ticket moves to “Escalated” until the escalation decision is recorded." size="lg"
      footer={<><Button onClick={onClose}>Cancel</Button><Button variant="primary" disabled={!f.department || f.reason.trim().length < 10} loading={busy} onClick={submit}>Escalate</Button></>}>
      <div className="space-y-4">
        <div className="grid gap-2">
          {LEVELS.map(([lv, label, desc]) => (
            <label key={lv} className={`flex gap-3 rounded-lg border p-3 cursor-pointer ${Number(f.level) === lv ? 'border-brand-400 bg-brand-50/60 dark:bg-brand-900/20' : 'border-base'}`}>
              <input type="radio" name="level" className="mt-1 accent-brand-500" checked={Number(f.level) === lv} onChange={() => setF({ ...f, level: lv, department: depts.find((d) => d.level === lv)?.key || '' })} />
              <span><span className="font-medium text-sm">{label}</span><span className="block text-xs text-muted">{desc}</span></span>
            </label>
          ))}
        </div>
        <div className="grid sm:grid-cols-2 gap-3">
          <Field label="Department" required>
            <Select value={f.department} onChange={(e) => setF({ ...f, department: e.target.value })}><option value="">Select…</option>{deptOptions.map((d) => <option key={d.key} value={d.key}>{d.name}</option>)}</Select>
          </Field>
          <Field label="Assigned person (optional)">
            <Select value={f.assignee_id} onChange={(e) => setF({ ...f, assignee_id: e.target.value })}><option value="">Department queue</option>{users.map((u) => <option key={u.id} value={u.id}>{u.name} — {u.title || u.role}</option>)}</Select>
          </Field>
        </div>
        <Field label="Escalation reason" required hint="What you checked, what you found, and what decision or action you need."><Textarea rows={4} value={f.reason} onChange={(e) => setF({ ...f, reason: e.target.value })} /></Field>
        <Field label="Expected follow-up" hint="A follow-up reminder is created for you."><Input type="datetime-local" value={f.expected_followup_at} onChange={(e) => setF({ ...f, expected_followup_at: e.target.value })} /></Field>
      </div>
    </Modal>
  );
}
