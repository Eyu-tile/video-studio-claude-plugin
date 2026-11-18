import { useMemo, useState } from 'react';
import { BarChart3, Download, Info } from 'lucide-react';
import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, Tooltip, CartesianGrid, BarChart, Bar, PieChart, Pie, Cell, Legend } from 'recharts';
import { qs, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { PRIORITY, STATUS, CHANNELS, hours, minutes, downloadCsv } from '../lib/format.js';
import { Button, Card, CardHeader, Checkbox, ErrorState, Input, Loading, PageHeader, Segmented, Stat } from '../components/ui.jsx';

const PALETTE = ['#0095e8', '#6366f1', '#14b8a6', '#f59e0b', '#ef4444', '#8b5cf6', '#ec4899', '#22c55e', '#64748b', '#0ea5e9'];
const PRI_COLOR = { critical: '#dc2626', high: '#f97316', medium: '#0095e8', low: '#94a3b8' };
const iso = (d) => d.toISOString().slice(0, 10);

function rangeFor(p) {
  const now = new Date();
  const today = iso(now);
  if (p === 'today') return { from: today, to: today };
  if (p === 'week') { const d = new Date(now); d.setDate(d.getDate() - ((d.getDay() + 6) % 7)); return { from: iso(d), to: today }; }
  if (p === 'month') return { from: iso(new Date(now.getFullYear(), now.getMonth(), 1)), to: today };
  if (p === '30d') { const d = new Date(now); d.setDate(d.getDate() - 29); return { from: iso(d), to: today }; }
  return null;
}

const tooltipStyle = { contentStyle: { background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: 8, fontSize: 12 }, labelStyle: { color: 'var(--text)' } };

export default function Reports() {
  const { can } = useAuth();
  const [preset, setPreset] = useState('30d');
  const [custom, setCustom] = useState(rangeFor('30d'));
  const [demo, setDemo] = useState(true);
  const range = preset === 'custom' ? custom : rangeFor(preset);
  const query = qs({ ...range, include_demo: demo ? '1' : '0' });
  const { data, loading, error, reload } = useApi(can('reports.view') ? `/reports${query}` : null, [query]);
  const series = useMemo(() => (data?.series || []).map((d) => ({ ...d, label: new Date(d.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }) })), [data]);
  if (!can('reports.view')) return <ErrorState error={{ status: 403, message: 'Reports are available to supervisors and administrators.' }} />;
  if (loading && !data) return <Loading />;
  if (error) return <ErrorState error={error} onRetry={reload} />;
  const s = data.summary;
  const exportAll = () => downloadCsv(`byfluence-support-report-${range.from}-to-${range.to}.csv`, data.agents.map((a) => ({
    employee: a.name, role: a.role, open_now: a.open_now, overdue_now: a.overdue_now, resolved_in_period: a.resolved, avg_resolution_hours: a.avg_resolution_hours ?? '', escalations_raised: a.escalations, reopened: a.reopened, csat: a.csat ?? '',
  })));

  return (
    <div>
      <PageHeader icon={BarChart3} title="Support Performance" subtitle="Every metric is calculated from real ticket activity in the selected period."
        actions={<>
          <Segmented value={preset} onChange={setPreset} options={[{ value: 'today', label: 'Today' }, { value: 'week', label: 'This week' }, { value: 'month', label: 'This month' }, { value: '30d', label: '30 days' }, { value: 'custom', label: 'Custom' }]} />
          <Button icon={Download} onClick={exportAll}>Export CSV</Button>
        </>} />
      <div className="flex flex-wrap items-center gap-3 mb-5">
        {preset === 'custom' && <><Input type="date" className="w-auto" value={custom.from} onChange={(e) => setCustom({ ...custom, from: e.target.value })} /><span className="text-muted text-sm">to</span><Input type="date" className="w-auto" value={custom.to} onChange={(e) => setCustom({ ...custom, to: e.target.value })} /></>}
        <Checkbox label="Include demo tickets" checked={demo} onChange={setDemo} />
        <span className="text-xs text-muted">{range.from} → {range.to}</span>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 mb-5">
        <Stat label="Tickets created" value={s.created} />
        <Stat label="Tickets resolved" value={s.resolved} tone="green" />
        <Stat label="Tickets reopened" value={s.reopened} tone={s.reopened ? 'amber' : undefined} />
        <Stat label="Avg. first response" value={minutes(s.avg_first_response_minutes)} hint={`${s.first_response_sample} tickets`} />
        <Stat label="Avg. resolution time" value={hours(s.avg_resolution_hours)} hint={`${s.resolution_sample} tickets`} />
        <Stat label="Overdue now" value={s.overdue_now} tone={s.overdue_now ? 'red' : 'green'} />
        <Stat label="Escalation rate" value={s.escalation_rate == null ? '—' : `${s.escalation_rate}%`} hint={`${s.escalated_tickets} tickets escalated`} />
        <Stat label="Resolved after target" value={s.resolved_after_target} hint="Past internal target" />
        <Stat label="Closed" value={s.closed} />
        <Stat label="Customer satisfaction" value={s.csat_avg == null ? '—' : `${s.csat_avg} / 5`} hint={s.csat_count ? `${s.csat_count} ratings collected` : 'Not collected yet'} />
      </div>

      <div className="grid lg:grid-cols-3 gap-5 mb-5">
        <Card className="lg:col-span-2">
          <CardHeader title="Tickets created vs resolved" />
          <div className="h-64 px-2 pb-3">
            <ResponsiveContainer>
              <AreaChart data={series} margin={{ left: -18, right: 10, top: 5 }}>
                <defs><linearGradient id="gc" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stopColor="#0095e8" stopOpacity={0.3} /><stop offset="100%" stopColor="#0095e8" stopOpacity={0} /></linearGradient></defs>
                <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} />
                <XAxis dataKey="label" tick={{ fontSize: 11, fill: 'var(--muted)' }} interval="preserveStartEnd" />
                <YAxis allowDecimals={false} tick={{ fontSize: 11, fill: 'var(--muted)' }} />
                <Tooltip {...tooltipStyle} />
                <Legend wrapperStyle={{ fontSize: 12 }} />
                <Area type="monotone" dataKey="created" name="Created" stroke="#0095e8" fill="url(#gc)" strokeWidth={2} />
                <Area type="monotone" dataKey="resolved" name="Resolved" stroke="#14b8a6" fill="transparent" strokeWidth={2} />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </Card>
        <Card>
          <CardHeader title="By priority" />
          <div className="h-64">
            <ResponsiveContainer>
              <PieChart>
                <Pie data={data.byPriority.map((p) => ({ ...p, label: PRIORITY[p.name]?.label }))} dataKey="n" nameKey="label" innerRadius={55} outerRadius={85} paddingAngle={2}>
                  {data.byPriority.map((p) => <Cell key={p.name} fill={PRI_COLOR[p.name]} />)}
                </Pie>
                <Tooltip {...tooltipStyle} /><Legend wrapperStyle={{ fontSize: 12 }} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </Card>
      </div>

      <div className="grid lg:grid-cols-2 gap-5 mb-5">
        <Card>
          <CardHeader title="Issues by category" />
          <div className="h-72 px-2 pb-3">
            <ResponsiveContainer>
              <BarChart data={data.byCategory} layout="vertical" margin={{ left: 40, right: 16 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" horizontal={false} />
                <XAxis type="number" allowDecimals={false} tick={{ fontSize: 11, fill: 'var(--muted)' }} />
                <YAxis type="category" dataKey="name" width={150} tick={{ fontSize: 11, fill: 'var(--muted)' }} />
                <Tooltip {...tooltipStyle} />
                <Bar dataKey="n" name="Tickets" fill="#0095e8" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </Card>
        <Card>
          <CardHeader title="Most common customer issues" subtitle="By subcategory" />
          <div className="px-4 pb-4 space-y-2">
            {data.topIssues.map((t, i) => {
              const max = data.topIssues[0]?.n || 1;
              return (
                <div key={i}>
                  <div className="flex justify-between text-sm"><span className="truncate">{t.name} <span className="text-xs text-muted">· {t.category}</span></span><span className="tabular-nums font-medium">{t.n}</span></div>
                  <div className="h-1.5 rounded-full surface-2 mt-1"><div className="h-full rounded-full" style={{ width: `${(t.n / max) * 100}%`, background: PALETTE[i % PALETTE.length] }} /></div>
                </div>
              );
            })}
            {!data.topIssues.length && <p className="text-sm text-muted">No tickets in this period.</p>}
          </div>
        </Card>
      </div>

      <div className="grid lg:grid-cols-3 gap-5 mb-5">
        <Card><CardHeader title="Channels" /><div className="px-4 pb-4 space-y-1.5 text-sm">{data.byChannel.map((c) => <div key={c.name} className="flex justify-between"><span>{CHANNELS[c.name] || c.name}</span><span className="tabular-nums">{c.n}</span></div>)}</div></Card>
        <Card><CardHeader title="Current status (all time)" /><div className="px-4 pb-4 space-y-1.5 text-sm">{data.byStatus.map((c) => <div key={c.name} className="flex justify-between"><span>{STATUS[c.name]?.label}</span><span className="tabular-nums">{c.n}</span></div>)}</div></Card>
        <Card><CardHeader title="Escalations by department" /><div className="px-4 pb-4 space-y-1.5 text-sm">{data.byEscalationDept.length ? data.byEscalationDept.map((c) => <div key={c.name} className="flex justify-between"><span>{c.name}</span><span className="tabular-nums">{c.n}</span></div>) : <p className="text-muted">None in this period.</p>}</div></Card>
      </div>

      <Card className="overflow-hidden">
        <CardHeader title="Employee workload & performance" subtitle="Open/overdue are current; other columns are for the selected period." />
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead className="surface-2 text-xs text-muted"><tr className="text-left">{['Employee', 'Open now', 'Overdue now', 'Resolved', 'Avg. resolution', 'Escalations raised', 'Reopened', 'CSAT'].map((h, i) => <th key={h} className={`px-4 py-2.5 font-medium ${i ? 'text-right' : ''}`}>{h}</th>)}</tr></thead>
            <tbody>{data.agents.map((a) => (
              <tr key={a.id} className="border-t border-base">
                <td className="px-4 py-2"><div className="font-medium">{a.name}</div><div className="text-xs text-muted capitalize">{a.role}</div></td>
                <td className="px-4 py-2 text-right tabular-nums">{a.open_now}</td>
                <td className={`px-4 py-2 text-right tabular-nums ${a.overdue_now ? 'text-red-600 font-medium' : ''}`}>{a.overdue_now}</td>
                <td className="px-4 py-2 text-right tabular-nums">{a.resolved}</td>
                <td className="px-4 py-2 text-right">{hours(a.avg_resolution_hours)}</td>
                <td className="px-4 py-2 text-right tabular-nums">{a.escalations}</td>
                <td className="px-4 py-2 text-right tabular-nums">{a.reopened}</td>
                <td className="px-4 py-2 text-right">{a.csat ?? '—'}</td>
              </tr>
            ))}</tbody>
          </table>
        </div>
      </Card>
      <p className="text-xs text-muted mt-4 flex items-start gap-1.5"><Info className="size-3.5 mt-0.5" />First response = first outbound customer contact logged on the ticket. Resolution time = reported → resolved. Targets come from Settings → Service targets.</p>
    </div>
  );
}
