import { useState } from 'react';
import { Lock, ShieldCheck, Search, Ticket, BookOpen } from 'lucide-react';
import { useAuth } from '../lib/auth.jsx';
import { api } from '../lib/api.js';
import { Button, Field, Input, Callout } from '../components/ui.jsx';

export default function Login() {
  const { login } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);
  const submit = async (e) => {
    e.preventDefault();
    setError(''); setBusy(true);
    try { await login(email, password); } catch (err) { setError(err.message); } finally { setBusy(false); }
  };
  return (
    <div className="min-h-full grid lg:grid-cols-2">
      <div className="hidden lg:flex flex-col justify-between bg-brand-500 text-white p-12 relative overflow-hidden">
        <div className="absolute -right-24 -top-24 size-96 rounded-full bg-white/10" />
        <div className="absolute -left-16 bottom-10 size-72 rounded-full bg-white/5" />
        <div className="flex items-center gap-3 relative">
          <div className="size-10 rounded-xl bg-white text-brand-600 grid place-items-center font-bold text-lg">B</div>
          <div><div className="font-semibold text-lg">Byfluence</div><div className="text-white/75 text-sm">Support Operating System</div></div>
        </div>
        <div className="relative space-y-6 max-w-md">
          <h1 className="text-3xl font-semibold leading-tight">Every answer, every procedure, every customer issue — in one place.</h1>
          <ul className="space-y-3 text-white/90 text-[15px]">
            <li className="flex gap-3"><Search className="size-5 shrink-0" />Search any customer problem in seconds</li>
            <li className="flex gap-3"><BookOpen className="size-5 shrink-0" />Follow approved steps and copy bilingual responses</li>
            <li className="flex gap-3"><Ticket className="size-5 shrink-0" />Track every issue from first message to resolution</li>
          </ul>
        </div>
        <p className="relative text-white/60 text-xs">Internal use only · Byfluence employees</p>
      </div>
      <div className="flex items-center justify-center p-6">
        <form onSubmit={submit} className="w-full max-w-sm space-y-5">
          <div className="lg:hidden flex items-center gap-2.5 mb-6">
            <div className="size-9 rounded-lg bg-brand-500 grid place-items-center text-white font-bold">B</div>
            <div className="font-semibold">Byfluence Support</div>
          </div>
          <div>
            <h2 className="text-2xl font-semibold tracking-tight">Sign in</h2>
            <p className="text-sm text-muted mt-1">Use your Byfluence employee account.</p>
          </div>
          {error && <Callout tone="warning">{error}</Callout>}
          <Field label="Work email"><Input type="email" autoComplete="username" value={email} onChange={(e) => setEmail(e.target.value)} required autoFocus /></Field>
          <Field label="Password"><Input type="password" autoComplete="current-password" value={password} onChange={(e) => setPassword(e.target.value)} required /></Field>
          <Button type="submit" variant="primary" size="lg" className="w-full" loading={busy} icon={Lock}>Sign in</Button>
          <p className="text-xs text-muted flex items-start gap-2"><ShieldCheck className="size-4 shrink-0 text-emerald-600" />Customer information in this system is confidential. Access is logged.</p>
        </form>
      </div>
    </div>
  );
}

export function ForcePasswordChange() {
  const { refresh, logout, user } = useAuth();
  const [f, setF] = useState({ current: '', next: '', confirm: '' });
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);
  const submit = async (e) => {
    e.preventDefault();
    if (f.next !== f.confirm) { setError('The new passwords do not match.'); return; }
    setBusy(true); setError('');
    try { await api('/me/password', { method: 'POST', body: { current: f.current, next: f.next } }); await refresh(); } catch (err) { setError(err.message); } finally { setBusy(false); }
  };
  return (
    <div className="min-h-full grid place-items-center p-6">
      <form onSubmit={submit} className="w-full max-w-sm space-y-4 surface border border-base rounded-2xl p-6 shadow-sm">
        <h2 className="text-xl font-semibold">Set a new password</h2>
        <p className="text-sm text-muted">Welcome, {user.name}. You signed in with a temporary password — please choose your own (at least 10 characters, letters and numbers).</p>
        {error && <Callout tone="warning">{error}</Callout>}
        <Field label="Temporary password"><Input type="password" value={f.current} onChange={(e) => setF({ ...f, current: e.target.value })} required /></Field>
        <Field label="New password"><Input type="password" autoComplete="new-password" value={f.next} onChange={(e) => setF({ ...f, next: e.target.value })} required /></Field>
        <Field label="Confirm new password"><Input type="password" autoComplete="new-password" value={f.confirm} onChange={(e) => setF({ ...f, confirm: e.target.value })} required /></Field>
        <div className="flex gap-2"><Button type="submit" variant="primary" loading={busy}>Save password</Button><Button onClick={logout}>Sign out</Button></div>
      </form>
    </div>
  );
}
