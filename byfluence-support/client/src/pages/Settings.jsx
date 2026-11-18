import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { Settings as SettingsIcon, User, Users, Timer, Building2, ToggleRight, Link as LinkIcon, Search as SearchIcon, PlugZap, Database, ScrollText, Plus, KeyRound, Trash2, Download, Save, Phone } from 'lucide-react';
import { api, qs, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { FEATURE_STATUS, ROLE_LABEL, bytes, dateTime, relTime } from '../lib/format.js';
import { Badge, Button, Callout, Card, Checkbox, CopyButton, FeatureBadge, Field, Input, Loading, Modal, PageHeader, Select, Tabs, Textarea, useConfirm, useToast, cx } from '../components/ui.jsx';

function useSetting(key) {
  const { settings, loadSettings } = useAuth();
  const toast = useToast();
  const [value, setValue] = useState(null);
  useEffect(() => { if (settings && value === null) setValue(structuredClone(settings[key])); }, [settings, key, value]);
  const save = async () => {
    try { await api(`/settings/${key}`, { method: 'PUT', body: { value } }); toast.success('Saved'); loadSettings(); } catch (e) { toast.error(e); }
  };
  return [value, setValue, save];
}

function Profile() {
  const { user, setUser } = useAuth();
  const toast = useToast();
  const [name, setName] = useState(user.name);
  const [lang, setLang] = useState(user.preferences?.language || 'am');
  const [pw, setPw] = useState({ current: '', next: '', confirm: '' });
  const saveProfile = async () => { try { const r = await api('/me', { method: 'PATCH', body: { name, preferences: { language: lang } } }); setUser(r.user); toast.success('Profile saved'); } catch (e) { toast.error(e); } };
  const savePw = async () => {
    if (pw.next !== pw.confirm) { toast.error('New passwords do not match.'); return; }
    try { await api('/me/password', { method: 'POST', body: { current: pw.current, next: pw.next } }); toast.success('Password changed. Other sessions were signed out.'); setPw({ current: '', next: '', confirm: '' }); } catch (e) { toast.error(e); }
  };
  return (
    <div className="grid lg:grid-cols-2 gap-5">
      <Card className="p-5 space-y-3">
        <h3 className="font-semibold">Profile</h3>
        <Field label="Display name"><Input value={name} onChange={(e) => setName(e.target.value)} /></Field>
        <Field label="Email"><Input value={user.email} disabled /></Field>
        <Field label="Role"><Input value={ROLE_LABEL[user.role]} disabled /></Field>
        <Field label="Default response language" hint="Used first in templates and articles"><Select value={lang} onChange={(e) => setLang(e.target.value)}><option value="am">Amharic (አማርኛ)</option><option value="en">English</option></Select></Field>
        <Button variant="primary" icon={Save} onClick={saveProfile}>Save profile</Button>
      </Card>
      <Card className="p-5 space-y-3">
        <h3 className="font-semibold">Change password</h3>
        <Field label="Current password"><Input type="password" value={pw.current} onChange={(e) => setPw({ ...pw, current: e.target.value })} /></Field>
        <Field label="New password" hint="At least 10 characters with letters and numbers"><Input type="password" autoComplete="new-password" value={pw.next} onChange={(e) => setPw({ ...pw, next: e.target.value })} /></Field>
        <Field label="Confirm new password"><Input type="password" autoComplete="new-password" value={pw.confirm} onChange={(e) => setPw({ ...pw, confirm: e.target.value })} /></Field>
        <Button icon={KeyRound} onClick={savePw} disabled={!pw.current || !pw.next}>Change password</Button>
      </Card>
    </div>
  );
}

function Team() {
  const { user, settings } = useAuth();
  const toast = useToast();
  const confirm = useConfirm();
  const { data, loading, reload } = useApi('/users');
  const [form, setForm] = useState(null);
  const [temp, setTemp] = useState(null);
  const depts = settings?.departments || [];
  const save = async () => {
    try {
      if (form.id) await api(`/users/${form.id}`, { method: 'PATCH', body: form });
      else { const r = await api('/users', { method: 'POST', body: form }); setTemp({ email: r.user.email, password: r.temporary_password }); }
      toast.success('Saved'); setForm(null); reload(true);
    } catch (e) { toast.error(e); }
  };
  const reset = async (u) => {
    if (!(await confirm({ title: `Reset password for ${u.name}?`, message: 'They will be signed out everywhere and must set a new password at next sign-in.', confirmLabel: 'Reset password' }))) return;
    try { const r = await api(`/users/${u.id}/reset-password`, { method: 'POST' }); setTemp({ email: u.email, password: r.temporary_password }); } catch (e) { toast.error(e); }
  };
  if (loading && !data) return <Loading />;
  return (
    <div className="space-y-5">
      <div className="flex justify-end"><Button variant="primary" icon={Plus} onClick={() => setForm({ name: '', email: '', role: 'agent', department: 'support_l1', title: '' })}>Add employee</Button></div>
      <Card className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead className="surface-2 text-xs text-muted"><tr className="text-left"><th className="px-4 py-2.5 font-medium">Employee</th><th className="px-3 py-2.5 font-medium">Role</th><th className="px-3 py-2.5 font-medium">Department</th><th className="px-3 py-2.5 font-medium">Last sign-in</th><th className="px-3 py-2.5 font-medium">Status</th><th /></tr></thead>
          <tbody>{data.map((u) => (
            <tr key={u.id} className={cx('border-t border-base', !u.active && 'opacity-60')}>
              <td className="px-4 py-2"><div className="font-medium">{u.name}{u.id === user.id && ' (you)'}</div><div className="text-xs text-muted">{u.email}{u.title ? ` · ${u.title}` : ''}</div></td>
              <td className="px-3 py-2">{ROLE_LABEL[u.role]}</td>
              <td className="px-3 py-2 text-[13px]">{depts.find((d) => d.key === u.department)?.name || u.department}</td>
              <td className="px-3 py-2 text-xs text-muted">{u.last_login_at ? relTime(u.last_login_at) : 'Never'}</td>
              <td className="px-3 py-2">{u.active ? <Badge tone="green">Active</Badge> : <Badge tone="gray">Deactivated</Badge>}{u.must_change_password && <Badge tone="amber" className="ml-1">Temp password</Badge>}</td>
              <td className="px-3 py-2 text-right whitespace-nowrap">
                <Button size="xs" onClick={() => setForm({ ...u })}>Edit</Button>{' '}
                <Button size="xs" icon={KeyRound} onClick={() => reset(u)}>Reset</Button>
              </td>
            </tr>
          ))}</tbody>
        </table>
      </Card>
      <PermissionMatrix />
      <Modal open={!!form} onClose={() => setForm(null)} title={form?.id ? `Edit ${form.name}` : 'Add employee'} size="md"
        footer={<><Button onClick={() => setForm(null)}>Cancel</Button><Button variant="primary" onClick={save}>Save</Button></>}>
        {form && <div className="grid sm:grid-cols-2 gap-3">
          <Field label="Full name" required><Input value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} /></Field>
          <Field label="Work email" required><Input type="email" value={form.email} disabled={!!form.id} onChange={(e) => setForm({ ...form, email: e.target.value })} /></Field>
          <Field label="Role"><Select value={form.role} onChange={(e) => setForm({ ...form, role: e.target.value })}>{Object.entries(ROLE_LABEL).map(([k, v]) => <option key={k} value={k}>{v}</option>)}</Select></Field>
          <Field label="Department"><Select value={form.department || ''} onChange={(e) => setForm({ ...form, department: e.target.value })}>{depts.map((d) => <option key={d.key} value={d.key}>{d.name}</option>)}</Select></Field>
          <Field label="Job title" className="sm:col-span-2"><Input value={form.title || ''} onChange={(e) => setForm({ ...form, title: e.target.value })} /></Field>
          {form.id && <Checkbox label="Active" description="Deactivated employees cannot sign in; their history is kept." checked={form.active} onChange={(v) => setForm({ ...form, active: v })} />}
        </div>}
      </Modal>
      <Modal open={!!temp} onClose={() => setTemp(null)} title="Temporary password" size="sm" footer={<Button variant="primary" onClick={() => setTemp(null)}>Done</Button>}>
        {temp && <div className="space-y-3 text-sm">
          <p>Share this securely with <strong>{temp.email}</strong> (in person or via a trusted channel). It is shown only once; they must change it at first sign-in.</p>
          <div className="flex items-center gap-2 rounded-lg surface-2 border border-base px-3 py-2 font-mono">{temp.password}<span className="flex-1" /><CopyButton size="xs" text={temp.password} /></div>
        </div>}
      </Modal>
    </div>
  );
}

const MATRIX = [
  ['Read published documentation, search, copy templates', true, true, true],
  ['Create tickets, add notes, log communication', true, true, true],
  ['Update & resolve own / unassigned tickets, escalate', true, true, true],
  ['View & update all tickets, assign to others, reopen', false, true, true],
  ['Manage escalations (decide / reassign)', false, true, true],
  ['Create & edit articles, FAQs, SOPs, templates', false, true, true],
  ['Publish non-policy content', false, true, true],
  ['Publish / approve policies', false, false, true],
  ['Publish announcements', false, true, true],
  ['View reports & team training progress', false, true, true],
  ['Manage categories, employees, settings, API keys', false, false, true],
  ['Audit log, backups, delete content', false, false, true],
];
function PermissionMatrix() {
  return (
    <Card className="overflow-x-auto">
      <div className="px-4 py-3 border-b border-base font-semibold text-sm">Roles & permissions</div>
      <table className="w-full text-sm">
        <thead className="text-xs text-muted"><tr><th className="text-left px-4 py-2 font-medium">Capability</th><th className="px-3 py-2 font-medium">Agent</th><th className="px-3 py-2 font-medium">Supervisor</th><th className="px-3 py-2 font-medium">Admin</th></tr></thead>
        <tbody>{MATRIX.map(([c, ...r]) => <tr key={c} className="border-t border-base"><td className="px-4 py-1.5">{c}</td>{r.map((v, i) => <td key={i} className="text-center">{v ? <span className="text-emerald-600">✓</span> : <span className="text-muted">—</span>}</td>)}</tr>)}</tbody>
      </table>
    </Card>
  );
}

function Sla() {
  const [v, setV, save] = useSetting('sla');
  if (!v) return <Loading />;
  return (
    <Card className="p-5 space-y-4 max-w-3xl">
      <Callout tone="policy" title="Internal targets only">These targets drive “overdue” flags, due dates and reports. They are never shown to customers. {v.approved ? 'Management has approved these values.' : 'The default values are placeholders until management approves them.'}</Callout>
      <table className="w-full text-sm">
        <thead className="text-xs text-muted"><tr><th className="text-left py-2 font-medium">Priority</th><th className="text-left py-2 font-medium">First response (minutes)</th><th className="text-left py-2 font-medium">Resolution (hours)</th></tr></thead>
        <tbody>{['critical', 'high', 'medium', 'low'].map((p) => (
          <tr key={p} className="border-t border-base"><td className="py-2 capitalize font-medium">{p}</td>
            <td className="py-2 pr-3"><Input type="number" min="1" value={v[p].first_response_minutes} onChange={(e) => setV({ ...v, [p]: { ...v[p], first_response_minutes: Number(e.target.value) } })} /></td>
            <td className="py-2"><Input type="number" min="1" value={v[p].resolution_hours} onChange={(e) => setV({ ...v, [p]: { ...v[p], resolution_hours: Number(e.target.value) } })} /></td></tr>
        ))}</tbody>
      </table>
      <Checkbox label="These targets are approved by management" checked={!!v.approved} onChange={(x) => setV({ ...v, approved: x })} />
      <p className="text-xs text-muted">Changes apply to new tickets and to priority changes; existing due dates are not recalculated.</p>
      <Button variant="primary" icon={Save} onClick={save}>Save targets</Button>
    </Card>
  );
}

function Departments() {
  const [v, setV, save] = useSetting('departments');
  if (!v) return <Loading />;
  return (
    <Card className="p-5 space-y-3">
      <p className="text-sm text-muted">Escalation departments and their level (1 = front line, 2 = supervisor, 3 = specialized, 4 = management).</p>
      {v.map((d, i) => (
        <div key={i} className="grid sm:grid-cols-[140px_1fr_90px_2fr_auto] gap-2 items-start">
          <Input value={d.key} disabled={!!d._locked} placeholder="key" onChange={(e) => setV(v.map((x, j) => (j === i ? { ...x, key: e.target.value.replace(/[^a-z0-9_]/g, '') } : x)))} />
          <Input value={d.name} placeholder="Name" onChange={(e) => setV(v.map((x, j) => (j === i ? { ...x, name: e.target.value } : x)))} />
          <Select value={d.level} onChange={(e) => setV(v.map((x, j) => (j === i ? { ...x, level: Number(e.target.value) } : x)))}>{[1, 2, 3, 4].map((l) => <option key={l} value={l}>L{l}</option>)}</Select>
          <Input value={d.description || ''} placeholder="What they handle" onChange={(e) => setV(v.map((x, j) => (j === i ? { ...x, description: e.target.value } : x)))} />
          <Button size="sm" variant="ghost" icon={Trash2} onClick={() => setV(v.filter((_, j) => j !== i))} aria-label="Remove" />
        </div>
      ))}
      <div className="flex gap-2"><Button icon={Plus} onClick={() => setV([...v, { key: '', name: '', level: 3, description: '' }])}>Add department</Button><Button variant="primary" icon={Save} onClick={save}>Save</Button></div>
    </Card>
  );
}

function Features() {
  const [v, setV, save] = useSetting('features');
  if (!v) return <Loading />;
  return (
    <Card className="p-5 space-y-3">
      <Callout tone="note">Agents check this before telling customers a feature or payment method is available. Mark “verified” only after confirming in production.</Callout>
      <div className="space-y-2">
        {v.map((f, i) => (
          <div key={f.key} className="grid md:grid-cols-[1.3fr_170px_110px_2fr] gap-2 items-center border-t border-base pt-2">
            <div><div className="text-sm font-medium">{f.name}</div><div className="text-[11px] text-muted font-mono">{f.key}</div></div>
            <Select value={f.status} onChange={(e) => setV(v.map((x, j) => (j === i ? { ...x, status: e.target.value } : x)))}>{Object.entries(FEATURE_STATUS).map(([k, s]) => <option key={k} value={k}>{s.label}</option>)}</Select>
            <Checkbox label="Verified" checked={!!f.verified} onChange={(x) => setV(v.map((y, j) => (j === i ? { ...y, verified: x } : y)))} />
            <Input value={f.notes || ''} placeholder="Notes for agents" onChange={(e) => setV(v.map((x, j) => (j === i ? { ...x, notes: e.target.value } : x)))} />
          </div>
        ))}
      </div>
      <div className="flex flex-wrap gap-2 items-center">
        <Button icon={Plus} onClick={() => { const name = prompt('Feature name'); if (name) setV([...v, { key: name.toLowerCase().replace(/[^a-z0-9]+/g, '-'), name, status: 'unconfirmed', verified: false, notes: '' }]); }}>Add feature</Button>
        <Button variant="primary" icon={Save} onClick={save}>Save feature status</Button>
        <span className="text-xs text-muted">Preview: <FeatureBadge status="live" verified={false} /></span>
      </div>
    </Card>
  );
}

function QuickLinks() {
  const [v, setV, save] = useSetting('quick_links');
  const [info, setInfo, saveInfo] = useSetting('support_info');
  if (!v || !info) return <Loading />;
  return (
    <div className="grid lg:grid-cols-2 gap-5">
      <Card className="p-5 space-y-3">
        <h3 className="font-semibold">Dashboard quick access</h3>
        {v.map((q, i) => (
          <div key={i} className="grid grid-cols-[1fr_1fr_110px_auto] gap-2">
            <Input value={q.label} placeholder="Label" onChange={(e) => setV(v.map((x, j) => (j === i ? { ...x, label: e.target.value } : x)))} />
            <Input value={q.to} placeholder="/kb/c/payments" onChange={(e) => setV(v.map((x, j) => (j === i ? { ...x, to: e.target.value } : x)))} />
            <Input value={q.icon} placeholder="icon" onChange={(e) => setV(v.map((x, j) => (j === i ? { ...x, icon: e.target.value } : x)))} />
            <Button size="sm" variant="ghost" icon={Trash2} onClick={() => setV(v.filter((_, j) => j !== i))} />
          </div>
        ))}
        <div className="flex gap-2"><Button icon={Plus} onClick={() => setV([...v, { label: '', to: '/kb', icon: 'file-text' }])}>Add link</Button><Button variant="primary" icon={Save} onClick={save}>Save</Button></div>
      </Card>
      <Card className="p-5 space-y-3">
        <h3 className="font-semibold flex items-center gap-2"><Phone className="size-4" />Official support channels</h3>
        <p className="text-xs text-muted">Shown to agents as the approved value for {'{{support_channel}}'}. Leave empty until officially confirmed.</p>
        {['telegram', 'email', 'phone', 'website', 'hours', 'timezone'].map((k) => (
          <Field key={k} label={k[0].toUpperCase() + k.slice(1)}><Input value={info[k] || ''} onChange={(e) => setInfo({ ...info, [k]: e.target.value })} /></Field>
        ))}
        <Button variant="primary" icon={Save} onClick={saveInfo}>Save</Button>
      </Card>
    </div>
  );
}

function Synonyms() {
  const { settings, loadSettings } = useAuth();
  const toast = useToast();
  const [text, setText] = useState(null);
  useEffect(() => { if (settings && text === null) setText((settings.search_synonyms || []).map((g) => g.join(', ')).join('\n')); }, [settings, text]);
  if (text === null) return <Loading />;
  const save = async () => {
    const value = text.split('\n').map((l) => l.split(',').map((x) => x.trim()).filter(Boolean)).filter((g) => g.length > 1);
    try { await api('/settings/search_synonyms', { method: 'PUT', body: { value } }); toast.success(`Saved ${value.length} synonym groups`); loadSettings(); } catch (e) { toast.error(e); }
  };
  return (
    <Card className="p-5 space-y-3">
      <p className="text-sm text-muted">One group per line, phrases separated by commas. When an employee types any phrase in a group, results matching the other phrases are included too (e.g. “didn't join, no-show, absent”). Add customer wording you find in Documentation Management → Knowledge gaps.</p>
      <Textarea rows={16} className="font-mono text-[12.5px]" value={text} onChange={(e) => setText(e.target.value)} />
      <Button variant="primary" icon={Save} onClick={save}>Save synonyms</Button>
    </Card>
  );
}

function Integrations() {
  const toast = useToast();
  const confirm = useConfirm();
  const { data, reload } = useApi('/admin/api-keys');
  const [name, setName] = useState('');
  const [scopes, setScopes] = useState(['kb:read']);
  const [created, setCreated] = useState(null);
  const create = async () => { try { const r = await api('/admin/api-keys', { method: 'POST', body: { name, scopes } }); setCreated(r.key); setName(''); reload(true); } catch (e) { toast.error(e); } };
  const base = `${window.location.origin}/api/v1`;
  return (
    <div className="space-y-5">
      <Callout tone="note" title="Knowledge API for the future AI assistant (Telegram bot)">
        The API returns only <strong>published, AI-visible</strong> documentation. Internal notes, drafts, tickets and customer data are never exposed. Documents with pending policies are flagged so the assistant hands off to a human.
      </Callout>
      <Card className="p-5 space-y-3">
        <h3 className="font-semibold">API keys</h3>
        <div className="flex flex-wrap gap-2 items-end">
          <Field label="Name" className="flex-1 min-w-[200px]"><Input value={name} onChange={(e) => setName(e.target.value)} placeholder="Telegram AI assistant" /></Field>
          <Checkbox label="kb:read" checked={scopes.includes('kb:read')} onChange={(x) => setScopes(x ? [...scopes, 'kb:read'] : scopes.filter((s) => s !== 'kb:read'))} />
          <Checkbox label="tickets:create" checked={scopes.includes('tickets:create')} onChange={(x) => setScopes(x ? [...scopes, 'tickets:create'] : scopes.filter((s) => s !== 'tickets:create'))} />
          <Button variant="primary" icon={KeyRound} disabled={!name.trim()} onClick={create}>Create key</Button>
        </div>
        <table className="w-full text-sm mt-2"><tbody>{(data || []).map((k) => (
          <tr key={k.id} className={cx('border-t border-base', k.revoked_at && 'opacity-50')}>
            <td className="py-2 font-medium">{k.name}</td><td className="py-2 font-mono text-xs">{k.prefix}…</td><td className="py-2">{k.scopes.map((s) => <Badge key={s} tone="gray" className="mr-1">{s}</Badge>)}</td>
            <td className="py-2 text-xs text-muted">{k.last_used_at ? `used ${relTime(k.last_used_at)}` : 'never used'}</td>
            <td className="py-2 text-right">{k.revoked_at ? <Badge tone="gray">Revoked</Badge> : <Button size="xs" icon={Trash2} onClick={async () => { if (await confirm({ title: 'Revoke key?', message: 'Integrations using it stop working immediately.', danger: true, confirmLabel: 'Revoke' })) { await api(`/admin/api-keys/${k.id}`, { method: 'DELETE' }); reload(true); } }}>Revoke</Button>}</td>
          </tr>
        ))}</tbody></table>
      </Card>
      <Card className="p-5 text-sm space-y-2">
        <h3 className="font-semibold">Endpoints</h3>
        <pre className="surface-2 rounded-lg p-3 text-xs overflow-x-auto">{`GET  ${base}/kb/search?q=seller+did+not+join&limit=5&full=1
GET  ${base}/kb/docs/{id}
GET  ${base}/kb/faqs
GET  ${base}/kb/templates
GET  ${base}/kb/escalation          (departments, feature status, hand-off rules)
POST ${base}/tickets                (scope tickets:create — hand-off to a human)

Header: Authorization: Bearer <api key>`}</pre>
      </Card>
      <Modal open={!!created} onClose={() => setCreated(null)} title="API key created" size="sm" footer={<Button variant="primary" onClick={() => setCreated(null)}>I have stored it</Button>}>
        <p className="text-sm mb-3">Copy this key now — it will not be shown again. Store it in the integration's secret settings, never in code or chat.</p>
        <div className="flex items-center gap-2 rounded-lg surface-2 border border-base px-3 py-2 font-mono text-xs break-all">{created}<CopyButton size="xs" text={created} /></div>
      </Modal>
    </div>
  );
}

function Data() {
  const toast = useToast();
  const confirm = useConfirm();
  const { data, reload } = useApi('/admin/stats');
  const delDemo = async () => {
    if (!(await confirm({ title: 'Delete all demo data?', message: 'Removes demo tickets (and their timelines, escalations, follow-ups) and demo announcements. Demo employee accounts stay — deactivate them in Team. Documentation is not affected.', danger: true, typeToConfirm: 'DELETE DEMO DATA', confirmLabel: 'Delete demo data' }))) return;
    try { const r = await api('/admin/demo-data', { method: 'DELETE', body: { confirm: 'DELETE DEMO DATA' } }); toast.success(`Removed ${r.tickets} tickets and ${r.announcements} announcements`); reload(); } catch (e) { toast.error(e); }
  };
  return (
    <div className="grid lg:grid-cols-2 gap-5">
      <Card className="p-5 space-y-3">
        <h3 className="font-semibold flex items-center gap-2"><Database className="size-4" />Backups</h3>
        <p className="text-sm text-muted">Download a consistent snapshot of the entire database (all tickets, documentation, users and history). Store backups securely — they contain customer data. Uploaded files are in the server's <code>data/uploads</code> folder; back that up too.</p>
        <div className="flex flex-wrap gap-2"><a href="/api/admin/backup"><Button variant="primary" icon={Download}>Download database backup</Button></a><a href="/api/admin/export"><Button icon={Download}>Export documentation (JSON)</Button></a></div>
        {data && <p className="text-xs text-muted">Database size {bytes(data.db_bytes)} · {Object.entries(data.counts).map(([k, n]) => `${n} ${k.replace('_', ' ')}`).join(' · ')}</p>}
      </Card>
      <Card className="p-5 space-y-3">
        <h3 className="font-semibold">Demo data</h3>
        <p className="text-sm text-muted">The system was seeded with clearly marked demonstration tickets and announcements so it is useful from day one. Remove them before going live.</p>
        {data && <p className="text-sm">{data.demo.tickets} demo tickets · {data.demo.announcements} demo announcements</p>}
        <Button variant="danger" icon={Trash2} onClick={delDemo} disabled={!data || (data.demo.tickets + data.demo.announcements === 0)}>Delete demo data</Button>
      </Card>
    </div>
  );
}

function Audit() {
  const [f, setF] = useState({ action: '', user: '', from: '', to: '', page: 1 });
  const users = useApi('/users');
  const { data, loading } = useApi(`/audit${qs(f)}`, [JSON.stringify(f)]);
  return (
    <div className="space-y-3">
      <div className="flex flex-wrap gap-2">
        <Select className="w-auto" value={f.action} onChange={(e) => setF({ ...f, action: e.target.value, page: 1 })}>
          <option value="">All actions</option>{['auth', 'ticket', 'escalation', 'doc', 'template', 'attachment', 'user', 'settings', 'announcement', 'backup', 'apikey', 'demo'].map((a) => <option key={a} value={a}>{a}.*</option>)}
        </Select>
        <Select className="w-auto" value={f.user} onChange={(e) => setF({ ...f, user: e.target.value, page: 1 })}><option value="">All employees</option>{(users.data || []).map((u) => <option key={u.id} value={u.id}>{u.name}</option>)}</Select>
        <Input type="date" className="w-auto" value={f.from} onChange={(e) => setF({ ...f, from: e.target.value, page: 1 })} />
        <Input type="date" className="w-auto" value={f.to} onChange={(e) => setF({ ...f, to: e.target.value, page: 1 })} />
      </div>
      {loading && !data ? <Loading /> : (
        <Card className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead className="surface-2 text-xs text-muted"><tr className="text-left"><th className="px-4 py-2 font-medium">When</th><th className="px-3 py-2 font-medium">Employee</th><th className="px-3 py-2 font-medium">Action</th><th className="px-3 py-2 font-medium">Target</th><th className="px-3 py-2 font-medium">Details</th></tr></thead>
            <tbody>{data.rows.map((r) => (
              <tr key={r.id} className="border-t border-base align-top">
                <td className="px-4 py-1.5 text-xs whitespace-nowrap">{dateTime(r.created_at)}</td>
                <td className="px-3 py-1.5 text-[13px]">{r.user_name || '—'}</td>
                <td className="px-3 py-1.5 font-mono text-xs">{r.action}</td>
                <td className="px-3 py-1.5 text-xs">{r.entity_type} {r.entity_id}</td>
                <td className="px-3 py-1.5 text-xs text-muted max-w-[380px] truncate" title={JSON.stringify(r.details)}>{JSON.stringify(r.details)}</td>
              </tr>
            ))}</tbody>
          </table>
          <div className="flex justify-between items-center px-4 py-2 border-t border-base text-xs text-muted">
            <span>{data.total} entries</span>
            <span className="flex gap-2"><Button size="xs" disabled={f.page <= 1} onClick={() => setF({ ...f, page: f.page - 1 })}>Prev</Button><Button size="xs" disabled={f.page * 100 >= data.total} onClick={() => setF({ ...f, page: f.page + 1 })}>Next</Button></span>
          </div>
        </Card>
      )}
    </div>
  );
}

export default function SettingsPage() {
  const { can } = useAuth();
  const [params, setParams] = useSearchParams();
  const admin = can('settings.manage');
  const tabs = [
    { value: 'profile', label: 'My profile', icon: User },
    ...(admin ? [
      { value: 'team', label: 'Team & roles', icon: Users },
      { value: 'sla', label: 'Service targets', icon: Timer },
      { value: 'departments', label: 'Departments', icon: Building2 },
      { value: 'features', label: 'Feature status', icon: ToggleRight },
      { value: 'links', label: 'Quick links & channels', icon: LinkIcon },
      { value: 'search', label: 'Search synonyms', icon: SearchIcon },
      { value: 'integrations', label: 'Integrations / AI', icon: PlugZap },
      { value: 'data', label: 'Data & backup', icon: Database },
      { value: 'audit', label: 'Audit log', icon: ScrollText },
    ] : []),
  ];
  const tab = tabs.some((t) => t.value === params.get('tab')) ? params.get('tab') : 'profile';
  return (
    <div>
      <PageHeader icon={SettingsIcon} title="Settings" subtitle={admin ? 'Your profile, the team, service targets, feature status, integrations, backups and the audit log.' : 'Your profile and preferences.'} />
      <Tabs className="mb-5" value={tab} onChange={(v) => setParams({ tab: v })} tabs={tabs} />
      {tab === 'profile' && <Profile />}
      {tab === 'team' && <Team />}
      {tab === 'sla' && <Sla />}
      {tab === 'departments' && <Departments />}
      {tab === 'features' && <Features />}
      {tab === 'links' && <QuickLinks />}
      {tab === 'search' && <Synonyms />}
      {tab === 'integrations' && <Integrations />}
      {tab === 'data' && <Data />}
      {tab === 'audit' && <Audit />}
    </div>
  );
}
