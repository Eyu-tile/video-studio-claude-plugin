import { Link, useNavigate } from 'react-router-dom';
import { AlarmClock, ArrowRight, BookOpen, CalendarClock, CheckCircle2, Clock, FileText, Flame, GraduationCap, Inbox, Megaphone, SearchX, Timer, Users, ArrowUpCircle, MessageCircleQuestion, Store, FileWarning } from 'lucide-react';
import { useApi } from '../lib/api.js';
import { iconFor } from '../lib/icons.js';
import { useAuth } from '../lib/auth.jsx';
import { DOC_TYPES, hours, minutes, relTime } from '../lib/format.js';
import { Card, CardHeader, ErrorState, Loading, PriorityBadge, Stat, StatusBadge, Badge, EmptyState, cx, Callout } from '../components/ui.jsx';

function TicketRow({ t }) {
  return (
    <Link to={`/tickets/${t.number}`} className="flex items-center gap-3 px-4 py-2.5 hover:bg-[var(--surface-2)] transition-colors border-t border-base first:border-t-0">
      <div className="min-w-0 flex-1">
        <div className="flex items-center gap-2 text-xs text-muted">
          <span className="font-mono">{t.number}</span><span>·</span><span className="truncate">{t.customer_name}</span>
          {t.is_demo && <Badge tone="slate">Demo</Badge>}
        </div>
        <div className="text-sm font-medium truncate mt-0.5">{t.title}</div>
      </div>
      <div className="hidden sm:flex flex-col items-end gap-1 shrink-0">
        <div className="flex gap-1.5"><PriorityBadge priority={t.priority} /><StatusBadge status={t.status} /></div>
        <span className={cx('text-[11px]', t.overdue ? 'text-red-600 font-medium' : 'text-muted')}>{t.overdue ? `Overdue · due ${relTime(t.due_at)}` : `Updated ${relTime(t.updated_at)}`}</span>
      </div>
    </Link>
  );
}


export default function Dashboard() {
  const { user, can } = useAuth();
  const nav = useNavigate();
  const { data, loading, error, reload } = useApi('/dashboard');
  if (loading && !data) return <Loading />;
  if (error) return <ErrorState error={error} onRetry={reload} />;
  const s = data.stats;
  const hour = new Date().getHours();
  const greet = hour < 12 ? 'Good morning' : hour < 18 ? 'Good afternoon' : 'Good evening';
  const go = (q) => () => nav(`/tickets${q}`);

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="text-[22px] font-semibold tracking-tight">{greet}, {user.name.split(' ')[0]}</h1>
          <p className="text-sm text-muted mt-1">
            You have <strong className="text-[var(--text)]">{s.mine_open}</strong> open {s.mine_open === 1 ? 'issue' : 'issues'} assigned to you
            {data.followups.filter((f) => f.overdue).length > 0 && <>, and <strong className="text-red-600">{data.followups.filter((f) => f.overdue).length} overdue follow-up(s)</strong></>}.
          </p>
        </div>
        <div className="flex gap-2 text-xs text-muted items-center">
          {s.demo_tickets > 0 && <Badge tone="slate">{s.demo_tickets} demo tickets in data</Badge>}
          <span>Live from ticket data · {new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
        </div>
      </div>

      {data.announcements.filter((a) => a.priority === 'critical' && !a.is_read).map((a) => (
        <Callout key={a.id} tone="warning" title={a.title}>
          <Link to={`/announcements#a${a.id}`} className="underline">Read the announcement</Link>
        </Callout>
      ))}

      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-3">
        <Stat label="Total customer issues" value={s.total} icon={Inbox} onClick={go('?view=all')} hint={`${s.created_today} reported today`} />
        <Stat label="Open tickets" value={s.open} icon={Clock} tone="brand" onClick={go('?view=open')} hint={`${s.unassigned} unassigned`} />
        <Stat label="Under review" value={s.under_review} icon={FileText} onClick={go('?view=under_review')} />
        <Stat label="Pending customer response" value={s.waiting_customer} icon={MessageCircleQuestion} onClick={go('?view=waiting_customer')} />
        <Stat label="Pending seller response" value={s.waiting_seller} icon={Store} onClick={go('?view=waiting_seller')} />
        <Stat label="Escalated issues" value={s.escalated} icon={ArrowUpCircle} tone={s.escalated ? 'amber' : undefined} onClick={go('?view=escalated')} />
        <Stat label="High-priority open" value={s.high_priority} icon={Flame} tone={s.high_priority ? 'red' : undefined} onClick={go('?view=high')} hint={s.critical ? `${s.critical} critical` : undefined} />
        <Stat label="Overdue tickets" value={s.overdue} icon={AlarmClock} tone={s.overdue ? 'red' : 'green'} onClick={go('?view=overdue')} hint="Past internal target" />
        <Stat label="Resolved" value={s.resolved} icon={CheckCircle2} tone="green" onClick={go('?view=resolved')} hint="Awaiting closure" />
        <Stat label="Closed tickets" value={s.closed} icon={CheckCircle2} onClick={go('?view=closed')} />
        <Stat label="Avg. resolution time" value={hours(s.avg_resolution_hours)} icon={Timer} hint={`Last 30 days · ${s.avg_resolution_sample} tickets`} />
        <Stat label="Avg. first response" value={minutes(s.avg_first_response_minutes)} icon={Timer} hint="Last 30 days" />
      </div>

      <div className="grid lg:grid-cols-3 gap-5">
        <div className="lg:col-span-2 space-y-5">
          <Card>
            <CardHeader title="Urgent issues" subtitle="Critical/high priority or past the internal target" icon={Flame}
              actions={<Link to="/tickets?view=high" className="text-xs font-medium text-brand-600 hover:underline flex items-center gap-1">View all <ArrowRight className="size-3" /></Link>} />
            {data.urgent.length ? <div>{data.urgent.map((t) => <TicketRow key={t.id} t={t} />)}</div>
              : <EmptyState icon={CheckCircle2} title="Nothing urgent">No critical, high-priority or overdue tickets right now.</EmptyState>}
          </Card>
          <Card>
            <CardHeader title="Recent customer issues" icon={Inbox} actions={<Link to="/tickets" className="text-xs font-medium text-brand-600 hover:underline flex items-center gap-1">All tickets <ArrowRight className="size-3" /></Link>} />
            {data.recent.length ? data.recent.map((t) => <TicketRow key={t.id} t={t} />)
              : <EmptyState title="No tickets yet" action={<button className="text-sm text-brand-600 font-medium" onClick={() => window.dispatchEvent(new Event('byf:new-ticket'))}>Create the first issue</button>} />}
          </Card>
          <Card>
            <CardHeader title="Quick access" subtitle="Most common customer topics" icon={BookOpen} />
            <div className="grid grid-cols-2 md:grid-cols-4 gap-2 px-4 pb-4">
              {data.quick_links.map((q) => {
                const I = iconFor(q.icon);
                return (
                  <Link key={q.to + q.label} to={q.to} className="flex items-center gap-2.5 rounded-lg border border-base px-3 py-2.5 text-sm font-medium hover:border-brand-300 hover:bg-brand-50/50 dark:hover:bg-brand-900/20 transition">
                    <I className="size-4 text-brand-500 shrink-0" /><span className="truncate">{q.label}</span>
                  </Link>
                );
              })}
            </div>
          </Card>
        </div>

        <div className="space-y-5">
          <Card>
            <CardHeader title="My follow-ups" icon={CalendarClock} subtitle={data.team_followups_overdue ? `${data.team_followups_overdue} overdue across the team` : 'Upcoming and overdue'} />
            {data.followups.length === 0 ? <p className="px-4 pb-4 text-sm text-muted">No pending follow-ups.</p> : (
              <ul className="pb-2">
                {data.followups.map((f) => (
                  <li key={f.id}>
                    <Link to={`/tickets/${f.number}`} className="flex gap-3 px-4 py-2 hover:bg-[var(--surface-2)]">
                      <AlarmClock className={cx('size-4 mt-0.5 shrink-0', f.overdue ? 'text-red-500' : 'text-amber-500')} />
                      <div className="min-w-0">
                        <div className={cx('text-xs font-medium', f.overdue ? 'text-red-600' : 'text-muted')}>{f.overdue ? 'Overdue' : 'Due'} {relTime(f.due_at)} · {f.number}</div>
                        <div className="text-sm truncate">{f.reason}</div>
                      </div>
                    </Link>
                  </li>
                ))}
              </ul>
            )}
          </Card>

          <Card>
            <CardHeader title="Support announcements" icon={Megaphone} actions={<Link to="/announcements" className="text-xs font-medium text-brand-600 hover:underline">All</Link>} />
            {data.announcements.length === 0 ? <p className="px-4 pb-4 text-sm text-muted">No active announcements.</p> : (
              <ul className="pb-2">
                {data.announcements.map((a) => (
                  <li key={a.id}>
                    <Link to={`/announcements#a${a.id}`} className="flex gap-2.5 px-4 py-2 hover:bg-[var(--surface-2)]">
                      <span className={cx('mt-1.5 size-2 rounded-full shrink-0', a.priority === 'critical' ? 'bg-red-500' : a.priority === 'important' ? 'bg-amber-500' : 'bg-brand-400', a.is_read && 'opacity-30')} />
                      <div className="min-w-0">
                        <div className={cx('text-sm truncate', !a.is_read && 'font-semibold')}>{a.title}</div>
                        <div className="text-xs text-muted">{a.author} · {relTime(a.published_at)}</div>
                      </div>
                    </Link>
                  </li>
                ))}
              </ul>
            )}
          </Card>

          <Card>
            <CardHeader title="Recently updated documentation" icon={FileText} />
            <ul className="pb-2">
              {data.docs.map((d) => (
                <li key={d.slug}>
                  <Link to={d.type === 'faq' ? `/faqs?open=${d.slug}` : `/kb/${d.slug}`} className="flex items-center gap-2 px-4 py-1.5 hover:bg-[var(--surface-2)]">
                    <span className="text-sm truncate flex-1">{d.title}</span>
                    <span className="text-[11px] text-muted shrink-0">{DOC_TYPES[d.type]?.label} · v{d.version}</span>
                  </Link>
                </li>
              ))}
            </ul>
          </Card>

          <Card className="p-4">
            <div className="flex items-center gap-3">
              <GraduationCap className="size-5 text-brand-500" />
              <div className="flex-1">
                <div className="text-sm font-medium">Training progress</div>
                <div className="h-1.5 rounded-full surface-2 mt-2 overflow-hidden"><div className="h-full bg-brand-500 rounded-full" style={{ width: `${data.training.total ? (data.training.done / data.training.total) * 100 : 0}%` }} /></div>
              </div>
              <Link to="/training" className="text-sm font-semibold tabular-nums">{data.training.done}/{data.training.total}</Link>
            </div>
          </Card>

          {can('reports.view') && (
            <Card>
              <CardHeader title="Supervisor checks" icon={Users} />
              <div className="px-4 pb-4 space-y-2 text-sm">
                <Link to="/escalations" className="flex justify-between hover:text-brand-600"><span>Active escalations</span><strong>{data.escalations_open}</strong></Link>
                <Link to="/manage?tab=review" className="flex justify-between hover:text-brand-600"><span>Articles waiting for review</span><strong>{data.review_queue}</strong></Link>
                <Link to="/manage?tab=feedback" className="flex justify-between hover:text-brand-600"><span className="flex items-center gap-1.5"><FileWarning className="size-3.5" />Outdated / suggestion reports</span><strong>{data.feedback_open}</strong></Link>
                {data.search_gaps.length > 0 && (
                  <div className="pt-2 border-t border-base">
                    <div className="flex items-center gap-1.5 text-xs font-medium text-muted mb-1.5"><SearchX className="size-3.5" />Searches with no results (knowledge gaps)</div>
                    <div className="flex flex-wrap gap-1.5">{data.search_gaps.map((g) => <Badge key={g.q} tone="amber">{g.q} ×{g.n}</Badge>)}</div>
                  </div>
                )}
              </div>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}
