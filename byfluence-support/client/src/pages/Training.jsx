import { useState } from 'react';
import { Link } from 'react-router-dom';
import { GraduationCap, CheckCircle2, Clock, PlayCircle, Users } from 'lucide-react';
import { useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { Badge, Card, ErrorState, Loading, PageHeader, Tabs, cx } from '../components/ui.jsx';

function TeamProgress() {
  const { data, loading } = useApi('/training/team');
  if (loading || !data) return <Loading />;
  return (
    <Card className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead className="surface-2 text-xs text-muted"><tr><th className="text-left px-4 py-2.5 font-medium">Employee</th>{data.modules.map((m) => <th key={m.id} className="px-2 py-2.5 font-medium text-center" title={m.title}>M{m.number}</th>)}<th className="px-3 py-2.5 font-medium">Done</th></tr></thead>
        <tbody>
          {data.users.map((u) => {
            const done = data.modules.filter((m) => u.progress[m.id]?.status === 'completed').length;
            return (
              <tr key={u.id} className="border-t border-base">
                <td className="px-4 py-2"><div className="font-medium">{u.name}</div><div className="text-xs text-muted capitalize">{u.role}</div></td>
                {data.modules.map((m) => {
                  const p = u.progress[m.id];
                  return <td key={m.id} className="px-2 py-2 text-center">{p?.status === 'completed' ? <span title={`Score ${p.best_score}%`} className="inline-grid place-items-center size-7 rounded-full bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-300 text-[11px] font-semibold">{p.best_score}</span> : p ? <span className="inline-block size-2.5 rounded-full bg-amber-400" title="In progress" /> : <span className="text-muted">·</span>}</td>;
                })}
                <td className="px-3 py-2 text-center tabular-nums font-medium">{done}/{data.modules.length}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </Card>
  );
}

export default function Training() {
  const { can } = useAuth();
  const [tab, setTab] = useState('modules');
  const { data, loading, error, reload } = useApi('/training');
  if (loading && !data) return <Loading />;
  if (error) return <ErrorState error={error} onRetry={reload} />;
  const done = data.modules.filter((m) => m.progress === 'completed').length;
  const pct = data.modules.length ? Math.round((done / data.modules.length) * 100) : 0;
  return (
    <div className="max-w-5xl">
      <PageHeader icon={GraduationCap} title="Training Center" subtitle={`Onboarding for new support employees. Each module has objectives, a lesson, realistic examples, practical exercises in this app and a knowledge check (pass mark ${data.pass_score}%).`} />
      <Card className="p-4 mb-5 flex flex-wrap items-center gap-4">
        <div className="relative size-14">
          <svg viewBox="0 0 36 36" className="size-14 -rotate-90"><circle cx="18" cy="18" r="15.5" fill="none" strokeWidth="3.5" className="stroke-[var(--surface-2)]" /><circle cx="18" cy="18" r="15.5" fill="none" strokeWidth="3.5" strokeLinecap="round" className="stroke-brand-500" strokeDasharray={`${pct * 0.974} 100`} /></svg>
          <span className="absolute inset-0 grid place-items-center text-xs font-semibold">{pct}%</span>
        </div>
        <div className="flex-1"><div className="font-semibold">Your progress</div><div className="text-sm text-muted">{done} of {data.modules.length} modules completed</div></div>
        {done < data.modules.length && <Link to={`/training/${(data.modules.find((m) => m.progress !== 'completed') || data.modules[0]).slug}`} className="inline-flex items-center gap-1.5 h-9 px-3.5 rounded-lg bg-brand-500 text-white text-sm font-medium"><PlayCircle className="size-4" />Continue</Link>}
      </Card>
      {can('training.view_team') && <Tabs className="mb-4" value={tab} onChange={setTab} tabs={[{ value: 'modules', label: 'Modules', icon: GraduationCap }, { value: 'team', label: 'Team progress', icon: Users }]} />}
      {tab === 'team' ? <TeamProgress /> : (
        <div className="space-y-3">
          {data.modules.map((m) => (
            <Link key={m.id} to={`/training/${m.slug}`} className="block">
              <Card className="p-4 hover:border-brand-300 transition flex gap-4 items-start">
                <div className={cx('size-11 rounded-xl grid place-items-center shrink-0 font-semibold', m.progress === 'completed' ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-300' : 'bg-brand-50 text-brand-600 dark:bg-brand-900/40 dark:text-brand-300')}>
                  {m.progress === 'completed' ? <CheckCircle2 className="size-5" /> : m.number}
                </div>
                <div className="min-w-0 flex-1">
                  <div className="flex flex-wrap items-center gap-2"><span className="font-semibold">Module {m.number}: {m.title}</span>{m.status !== 'published' && <Badge tone="gray">{m.status}</Badge>}</div>
                  <ul className="text-[13px] text-muted mt-1 list-disc pl-4 space-y-0.5">{m.objectives.slice(0, 3).map((o) => <li key={o} className="line-clamp-1">{o}</li>)}</ul>
                </div>
                <div className="text-right text-xs text-muted shrink-0 space-y-1">
                  {m.duration && <div className="flex items-center gap-1 justify-end"><Clock className="size-3" />{m.duration} min</div>}
                  <div>{m.questions} questions</div>
                  {m.progress === 'completed' ? <Badge tone="green">Completed · {m.best_score}%</Badge> : m.progress === 'in_progress' ? <Badge tone="amber">In progress{m.best_score != null ? ` · best ${m.best_score}%` : ''}</Badge> : <Badge tone="gray">Not started</Badge>}
                </div>
              </Card>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
