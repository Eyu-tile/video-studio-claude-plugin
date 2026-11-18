import { useEffect, useMemo, useState } from 'react';
import { ShieldAlert, Lightbulb } from 'lucide-react';
import { api } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { CHANNELS, PRIORITY, toLocalInput } from '../lib/format.js';
import { Button, Field, Input, Modal, Select, Textarea, useToast, Callout, Badge } from './ui.jsx';

const EMPTY = {
  customer_name: '', customer_ref: '', customer_email: '', customer_phone: '', account_type: 'buyer', language: 'am', channel: 'telegram',
  title: '', category_id: '', subcategory_id: '', description: '', order_ref: '', consultation_ref: '', transaction_ref: '',
  priority: 'medium', assignee_id: '', internal_note: '', reported_at: '',
};

/** Detect sensitive data that must never be stored (OTP codes, PINs, card numbers, passwords). */
export function sensitiveWarning(text) {
  const t = text || '';
  if (/\b(?:\d[ -]?){13,19}\b/.test(t) && /card|visa|master|ካርድ/i.test(t)) return 'This looks like a card number. Never record full card numbers.';
  if (/\b(otp|code|pin|password|passcode|ኮድ|ፒን|የይለፍ)\b[^\n]{0,20}\b\d{4,8}\b/i.test(t)) return 'This looks like a verification code, PIN or password. Never record or request them — remove it.';
  return null;
}

export default function NewTicketModal({ open, onClose, onCreated, preset }) {
  const { user, can } = useAuth();
  const toast = useToast();
  const [f, setF] = useState(EMPTY);
  const [cats, setCats] = useState([]);
  const [users, setUsers] = useState([]);
  const [errors, setErrors] = useState({});
  const [saving, setSaving] = useState(false);
  const [suggest, setSuggest] = useState([]);

  useEffect(() => {
    if (!open) return;
    setF({ ...EMPTY, reported_at: toLocalInput(), assignee_id: String(user.id), ...(preset || {}) });
    setErrors({});
    api('/categories?scope=kb').then(setCats).catch(() => {});
    api('/users').then(setUsers).catch(() => {});
  }, [open, preset, user.id]);

  // Suggest matching articles while typing the title
  useEffect(() => {
    if (!open || f.title.trim().length < 6) { setSuggest([]); return; }
    const t = setTimeout(() => {
      api(`/search?q=${encodeURIComponent(f.title)}&kinds=article,troubleshooting&limit=4&log=0`).then((r) => setSuggest(r.results)).catch(() => {});
    }, 350);
    return () => clearTimeout(t);
  }, [f.title, open]);

  const subs = useMemo(() => cats.find((c) => String(c.id) === String(f.category_id))?.subcategories || [], [cats, f.category_id]);
  const set = (k) => (e) => setF((x) => ({ ...x, [k]: e?.target ? e.target.value : e, ...(k === 'category_id' ? { subcategory_id: '' } : {}) }));
  const warn = sensitiveWarning(`${f.description}\n${f.internal_note}\n${f.title}`);

  const applySuggestion = async (s) => {
    try {
      const d = await api(`/docs/${s.slug}?view=0`);
      const top = d.path[0];
      const sub = d.path[1];
      setF((x) => ({ ...x, category_id: top ? String(top.id) : x.category_id, subcategory_id: sub ? String(sub.id) : '', priority: d.doc.priority || x.priority, linked_docs: [s.slug] }));
      toast.info(`Category and priority set from “${s.title}”.`);
    } catch (e) { toast.error(e); }
  };

  const submit = async () => {
    const er = {};
    if (!f.customer_name.trim()) er.customer_name = 'Required';
    if (f.title.trim().length < 5) er.title = 'At least 5 characters';
    if (!f.description.trim()) er.description = 'Describe the issue';
    if (!f.category_id) er.category_id = 'Choose a category';
    if (f.customer_email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.customer_email)) er.customer_email = 'Invalid email';
    if (f.customer_phone && !/^[+\d][\d\s-]{6,19}$/.test(f.customer_phone)) er.customer_phone = 'Invalid phone number';
    if (!f.customer_email && !f.customer_phone && !f.customer_ref) er.customer_phone = 'Add at least one way to identify the customer (phone, email or customer ID)';
    setErrors(er);
    if (Object.keys(er).length) return;
    setSaving(true);
    try {
      const t = await api('/tickets', { method: 'POST', body: { ...f, assignee_id: f.assignee_id ? Number(f.assignee_id) : null, reported_at: f.reported_at ? new Date(f.reported_at).toISOString() : undefined } });
      toast.success(`Ticket ${t.number} created`);
      onCreated?.(t);
    } catch (e) { toast.error(e); } finally { setSaving(false); }
  };

  return (
    <Modal open={open} onClose={onClose} title="Create new customer issue" subtitle="Ticket ID is generated automatically. Fields marked * are required." size="lg"
      footer={<><Button onClick={onClose}>Cancel</Button><Button variant="primary" loading={saving} onClick={submit}>Create issue</Button></>}>
      <div className="space-y-6">
        <section>
          <h3 className="text-xs font-semibold uppercase tracking-wider text-muted mb-3">Customer information</h3>
          <div className="grid sm:grid-cols-2 gap-3">
            <Field label="Customer full name" required error={errors.customer_name}><Input value={f.customer_name} onChange={set('customer_name')} placeholder="e.g. Bethlehem Assefa" /></Field>
            <Field label="Customer ID" hint="Byfluence user ID, if known"><Input value={f.customer_ref} onChange={set('customer_ref')} /></Field>
            <Field label="Email address" error={errors.customer_email}><Input type="email" value={f.customer_email} onChange={set('customer_email')} /></Field>
            <Field label="Phone number" error={errors.customer_phone}><Input value={f.customer_phone} onChange={set('customer_phone')} placeholder="09…" /></Field>
            <Field label="Account type">
              <Select value={f.account_type} onChange={set('account_type')}><option value="buyer">Buyer</option><option value="seller">Seller</option><option value="both">Buyer & seller</option><option value="guest">Not registered</option></Select>
            </Field>
            <div className="grid grid-cols-2 gap-3">
              <Field label="Preferred language"><Select value={f.language} onChange={set('language')}><option value="am">Amharic</option><option value="en">English</option></Select></Field>
              <Field label="Contact channel"><Select value={f.channel} onChange={set('channel')}>{Object.entries(CHANNELS).filter(([k]) => k !== 'any').map(([k, v]) => <option key={k} value={k}>{v}</option>)}</Select></Field>
            </div>
          </div>
        </section>
        <section>
          <h3 className="text-xs font-semibold uppercase tracking-wider text-muted mb-3">Issue information</h3>
          <div className="grid sm:grid-cols-2 gap-3">
            <Field label="Issue title" required error={errors.title} className="sm:col-span-2"><Input value={f.title} onChange={set('title')} placeholder="e.g. Paid for consultation but seller did not join" /></Field>
            {suggest.length > 0 && (
              <div className="sm:col-span-2 rounded-lg border border-brand-200 dark:border-brand-800 bg-brand-50/60 dark:bg-brand-900/20 p-2.5">
                <div className="flex items-center gap-1.5 text-xs font-medium text-brand-700 dark:text-brand-200 mb-1.5"><Lightbulb className="size-3.5" />Matching articles — click to use its category & priority</div>
                <div className="flex flex-wrap gap-1.5">
                  {suggest.map((s) => <button key={s.slug} type="button" onClick={() => applySuggestion(s)} className="text-xs rounded-md surface border border-base px-2 py-1 hover:border-brand-400 text-left">{s.title}</button>)}
                </div>
              </div>
            )}
            <Field label="Issue category" required error={errors.category_id}>
              <Select value={f.category_id} onChange={set('category_id')}><option value="">Select…</option>{cats.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</Select>
            </Field>
            <Field label="Subcategory">
              <Select value={f.subcategory_id} onChange={set('subcategory_id')} disabled={!subs.length}><option value="">Select…</option>{subs.map((s) => <option key={s.id} value={s.id}>{s.name}</option>)}</Select>
            </Field>
            <Field label="Detailed description" required error={errors.description} className="sm:col-span-2">
              <Textarea rows={4} value={f.description} onChange={set('description')} placeholder="What happened, when, what the customer already tried, what they are asking for." />
            </Field>
            <Field label="Related order ID"><Input value={f.order_ref} onChange={set('order_ref')} /></Field>
            <Field label="Related consultation ID"><Input value={f.consultation_ref} onChange={set('consultation_ref')} /></Field>
            <Field label="Related transaction reference"><Input value={f.transaction_ref} onChange={set('transaction_ref')} /></Field>
            <Field label="Date reported"><Input type="datetime-local" value={f.reported_at} max={toLocalInput()} onChange={set('reported_at')} /></Field>
            <Field label="Priority">
              <Select value={f.priority} onChange={set('priority')}>{Object.entries(PRIORITY).map(([k, v]) => <option key={k} value={k}>{v.label}</option>)}</Select>
            </Field>
            <Field label="Assigned support employee" hint={can('tickets.assign') ? undefined : 'Supervisors can assign to others'}>
              <Select value={f.assignee_id} onChange={set('assignee_id')} disabled={!can('tickets.assign')}>
                <option value="">Unassigned (team queue)</option>
                {users.map((u) => <option key={u.id} value={u.id}>{u.name}{u.id === user.id ? ' (me)' : ''}</option>)}
              </Select>
            </Field>
            <Field label="Internal note" hint="Visible to employees only. Screenshots & files can be attached after creating." className="sm:col-span-2">
              <Textarea rows={2} value={f.internal_note} onChange={set('internal_note')} />
            </Field>
          </div>
          {f.linked_docs?.length > 0 && <p className="text-xs text-muted mt-2">Linked article: <Badge tone="blue">{f.linked_docs[0]}</Badge></p>}
        </section>
        {warn && <Callout tone="warning" title="Sensitive data detected"><span className="flex items-center gap-1.5"><ShieldAlert className="size-4" />{warn}</span></Callout>}
        <p className="text-xs text-muted">Never record passwords, OTP/verification codes, PINs or full card numbers.</p>
      </div>
    </Modal>
  );
}
