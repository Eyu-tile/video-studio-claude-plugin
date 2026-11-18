import { useCallback, useEffect, useMemo, useState } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { Ticket, Plus, Search, LayoutList, Columns3, X, AlarmClock, Download, ChevronLeft, ChevronRight, CalendarClock } from 'lucide-react';
import { api, qs, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { STATUS, STATUS_ORDER, PRIORITY, CHANNELS, relTime, dateTime, downloadCsv, MANUAL_STATUSES } from '../lib/format.js';
import { Avatar, Badge, Button, Card, EmptyState, ErrorState, Input, Loading, PageHeader, PriorityBadge, Segmented, Select, StatusBadge, Tabs, cx, useToast } from '../components/ui.jsx';
import { CloseModal, EscalateModal, ResolveModal } from '../components/TicketActions.jsx';

const VIEWS = [
  ['all', 'All Issues'], ['mine', 'My Assigned'], ['unassigned', 'Unassigned'], ['new', 'New'], ['under_review', 'Under Review'], ['waiting_customer', 'Waiting for Customer'],
  ['waiting_seller', 'Waiting for Seller'], ['escalated', 'Escalated'], ['overdue', 'Overdue'], ['reopened', 'Reopened'], ['resolved', 'Resolved'], ['closed', 'Closed'],
];

function Due({ t }) {
  if (!t.is_open) return <span className="text-xs text-muted">{t.closed_at ? `Closed ${relTime(t.closed_at)}` : t.resolved_at ? `Resolved ${relTime(t.resolved_at)}` : '—'}</span>;
  return <span className={cx('text-xs inline-flex items-center gap-1', t.overdue ? 'text-red-600 font-medium' : 'text-muted')}>{t.overdue && <AlarmClock className="size-3" />}{t.overdue ? 'Overdue ' : 'Due '}{relTime(t.due_at)}</span>;
}

function KanbanBoard({ tickets, onMove }) {
  const [drag, setDrag] = useState(null);
  const [over, setOver] = useState(null);
  const cols = STATUS_ORDER;
  return (
    <div className="flex gap-3 overflow-x-auto pb-3 -mx-1 px-1">
      {cols.map((s) => {
        const items = tickets.filter((t) => t.status === s);
        return (
          <div key={s} onDragOver={(e) => { e.preventDefault(); setOver(s); }} onDragLeave={() => setOver(null)}
            onDrop={(e) => { e.preventDefault(); setOver(null); if (drag && drag.status !== s) onMove(drag, s); setDrag(null); }}
            className={cx('w-[264px] shrink-0 rounded-xl border border-base surface-2 flex flex-col max-h-[calc(100vh-280px)]', over === s && drag?.status !== s && 'ring-2 ring-brand-400')}>
            <div className="flex items-center justify-between px-3 py-2.5 border-b border-base">
              <StatusBadge status={s} /><span className="text-xs text-muted tabular-nums">{items.length}</span>
            </div>
            <div className="p-2 space-y-2 overflow-y-auto flex-1 min-h-[80px]">
              {items.map((t) => (
                <Link key={t.id} to={`/tickets/${t.number}`} draggable onDragStart={() => setDrag(t)} onDragEnd={() => setDrag(null)}
                  className={cx('block surface rounded-lg border border-base p-2.5 shadow-xs hover:border-brand-300 cursor-grab active:cursor-grabbing', t.overdue && 'border-l-4 border-l-red-500', drag?.id === t.id && 'opacity-50')}>
                  <div className="flex items-center justify-between gap-2 text-[11px] text-muted"><span className="font-mono">{t.number}</span><PriorityBadge priority={t.priority} /></div>
                  <div className="text-[13px] font-medium mt-1 line-clamp-2">{t.title}</div>
                  <div className="flex items-center justify-between gap-2 mt-2">
                    <span className="text-[11px] text-muted truncate">{t.customer_name}</span>
                    {t.assignee ? <Avatar name={t.assignee.name} size="sm" /> : <Badge tone="amber">Unassigned</Badge>}
                  </div>
                  <div className="mt-1.5"><Due t={t} /></div>
                </Link>
              ))}
              {!items.length && <div className="text-xs text-muted text-center py-6">Drop here</div>}
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default function Tickets() {
  const [params, setParams] = useSearchParams();
  const nav = useNavigate();
  const toast = useToast();
  const { can } = useAuth();
  const view = params.get('view') || 'all';
  const layout = params.get('layout') || 'table';
  const [f, setF] = useState({ q: params.get('q') || '', priority: '', category: '', assignee: '', channel: '', from: '', to: '', sort: 'updated' });
  const [debouncedQ, setDebouncedQ] = useState(f.q);
  const [page, setPage] = useState(1);
  const [action, setAction] = useState(null);
  useEffect(() => { const t = setTimeout(() => setDebouncedQ(f.q), 250); return () => clearTimeout(t); }, [f.q]);
  useEffect(() => { setPage(1); }, [view, debouncedQ, f.priority, f.category, f.assignee, f.channel, f.from, f.to, f.sort]);

  const query = qs({ view, q: debouncedQ, priority: f.priority, category: f.category, assignee: f.assignee, channel: f.channel, from: f.from, to: f.to, sort: f.sort, page: layout === 'kanban' ? 1 : page, pageSize: layout === 'kanban' ? 300 : 25 });
  const list = useApi(`/tickets${query}`, [query]);
  const counts = useApi('/tickets/counts');
  const cats = useApi('/categories?scope=kb');
  const users = useApi('/users');
  const reload = useCallback(() => { list.reload(true); counts.reload(true); window.dispatchEvent(new Event('byf:refresh-counts')); }, [list, counts]);

  const setView = (v) => { const p = new URLSearchParams(params); p.set('view', v); setParams(p); };
  const setLayout = (v) => { const p = new URLSearchParams(params); p.set('layout', v); setParams(p); };
  const anyFilter = f.q || f.priority || f.category || f.assignee || f.channel || f.from || f.to;

  const onMove = async (t, to) => {
    if (MANUAL_STATUSES.includes(to)) {
      try { await api(`/tickets/${t.id}/status`, { method: 'POST', body: { status: to } }); toast.success(`${t.number} → ${STATUS[to].label}`); reload(); } catch (e) { toast.error(e); }
    } else if (to === 'resolved') setAction({ type: 'resolve', t });
    else if (to === 'closed') setAction({ type: 'close', t });
    else if (to === 'escalated') setAction({ type: 'escalate', t });
    else toast.info('Open the ticket and use “Reopen” to record the reason.');
  };

  const exportCsv = () => downloadCsv(`byfluence-tickets-${view}.csv`, (list.data?.tickets || []).map((t) => ({
    ticket: t.number, title: t.title, status: STATUS[t.status]?.label, priority: t.priority, category: t.category?.name, subcategory: t.subcategory?.name,
    customer: t.customer_name, channel: t.channel, assignee: t.assignee?.name || '', reported: t.reported_at, due: t.due_at, overdue: t.overdue ? 'yes' : '', resolved: t.resolved_at || '', closed: t.closed_at || '',
  })));

  const tabs = useMemo(() => VIEWS.map(([v, l]) => ({ value: v, label: l, count: counts.data ? counts.data[v] : undefined })), [counts.data]);
  const totalPages = list.data ? Math.max(1, Math.ceil(list.data.total / list.data.pageSize)) : 1;

  return (
    <div>
      <PageHeader icon={Ticket} title="Customer Issues" subtitle="Create, investigate, escalate and resolve every customer issue. Every action is recorded on the ticket timeline."
        actions={<>
          <Segmented value={layout} onChange={setLayout} options={[{ value: 'table', label: 'Table', icon: LayoutList }, { value: 'kanban', label: 'Board', icon: Columns3 }]} />
          <Button icon={Download} onClick={exportCsv} disabled={!list.data?.tickets?.length}>Export</Button>
          <Button variant="primary" icon={Plus} onClick={() => window.dispatchEvent(new Event('byf:new-ticket'))}>Create New Issue</Button>
        </>} />
      <Tabs tabs={tabs} value={view} onChange={setView} className="mb-4" />
      <div className="flex flex-wrap gap-2 mb-4">
        <div className="relative flex-1 min-w-[240px]">
          <Search className="size-4 absolute left-3 top-2.5 text-muted" />
          <Input className="pl-9" placeholder="Ticket ID, customer name, email, phone, order or transaction ID…" value={f.q} onChange={(e) => setF({ ...f, q: e.target.value })} />
        </div>
        <Select className="w-auto" value={f.priority} onChange={(e) => setF({ ...f, priority: e.target.value })}><option value="">Any priority</option>{Object.entries(PRIORITY).map(([k, v]) => <option key={k} value={k}>{v.label}</option>)}</Select>
        <Select className="w-auto max-w-[200px]" value={f.category} onChange={(e) => setF({ ...f, category: e.target.value })}><option value="">Any category</option>{(cats.data || []).map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}</Select>
        <Select className="w-auto max-w-[180px]" value={f.assignee} onChange={(e) => setF({ ...f, assignee: e.target.value })}><option value="">Any assignee</option><option value="none">Unassigned</option>{(users.data || []).map((u) => <option key={u.id} value={u.id}>{u.name}</option>)}</Select>
        <Select className="w-auto" value={f.channel} onChange={(e) => setF({ ...f, channel: e.target.value })}><option value="">Any channel</option>{Object.entries(CHANNELS).filter(([k]) => k !== 'any').map(([k, v]) => <option key={k} value={k}>{v}</option>)}</Select>
        <Input type="date" className="w-auto" value={f.from} onChange={(e) => setF({ ...f, from: e.target.value })} title="Reported from" />
        <Input type="date" className="w-auto" value={f.to} onChange={(e) => setF({ ...f, to: e.target.value })} title="Reported to" />
        <Select className="w-auto" value={f.sort} onChange={(e) => setF({ ...f, sort: e.target.value })}><option value="updated">Recently updated</option><option value="created">Newest</option><option value="oldest">Oldest</option><option value="priority">Priority</option><option value="due">Due soonest</option></Select>
        {anyFilter && <Button variant="ghost" icon={X} onClick={() => setF({ q: '', priority: '', category: '', assignee: '', channel: '', from: '', to: '', sort: f.sort })}>Clear</Button>}
      </div>

      {list.loading && !list.data ? <Loading /> : list.error ? <ErrorState error={list.error} onRetry={list.reload} /> : list.data.tickets.length === 0 ? (
        <Card><EmptyState icon={Ticket} title={anyFilter ? 'No tickets match these filters' : 'No tickets in this view'} action={<Button variant="primary" icon={Plus} onClick={() => window.dispatchEvent(new Event('byf:new-ticket'))}>Create New Issue</Button>} /></Card>
      ) : layout === 'kanban' ? <KanbanBoard tickets={list.data.tickets} onMove={onMove} /> : (
        <Card className="overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="surface-2 text-xs text-muted">
                <tr className="text-left">
                  <th className="px-4 py-2.5 font-medium">Issue</th>
                  <th className="px-3 py-2.5 font-medium hidden md:table-cell">Category</th>
                  <th className="px-3 py-2.5 font-medium">Priority</th>
                  <th className="px-3 py-2.5 font-medium">Status</th>
                  <th className="px-3 py-2.5 font-medium hidden lg:table-cell">Assigned</th>
                  <th className="px-3 py-2.5 font-medium hidden sm:table-cell">Due / updated</th>
                </tr>
              </thead>
              <tbody>
                {list.data.tickets.map((t) => (
                  <tr key={t.id} onClick={() => nav(`/tickets/${t.number}`)} className={cx('border-t border-base cursor-pointer hover:bg-[var(--surface-2)]', t.overdue && 'bg-red-50/40 dark:bg-red-950/10')}>
                    <td className="px-4 py-2.5 max-w-[420px]">
                      <div className="flex items-center gap-2 text-xs text-muted">
                        <span className="font-mono">{t.number}</span><span>·</span><span className="truncate">{t.customer_name}</span>
                        <span className="hidden xl:inline">· {CHANNELS[t.channel]}</span>
                        {t.is_demo && <Badge tone="slate">Demo</Badge>}
                        {t.pending_followups > 0 && <CalendarClock className="size-3.5 text-amber-500" title="Pending follow-up" />}
                      </div>
                      <Link to={`/tickets/${t.number}`} onClick={(e) => e.stopPropagation()} className="font-medium hover:text-brand-600 line-clamp-1">{t.title}</Link>
                    </td>
                    <td className="px-3 py-2.5 hidden md:table-cell"><div className="text-[13px] truncate max-w-[180px]">{t.category?.name || '—'}</div><div className="text-xs text-muted truncate max-w-[180px]">{t.subcategory?.name}</div></td>
                    <td className="px-3 py-2.5"><PriorityBadge priority={t.priority} /></td>
                    <td className="px-3 py-2.5"><StatusBadge status={t.status} /></td>
                    <td className="px-3 py-2.5 hidden lg:table-cell">{t.assignee ? <span className="flex items-center gap-2"><Avatar name={t.assignee.name} size="sm" /><span className="text-[13px] truncate max-w-[120px]">{t.assignee.name}</span></span> : <Badge tone="amber">Unassigned</Badge>}</td>
                    <td className="px-3 py-2.5 hidden sm:table-cell whitespace-nowrap"><Due t={t} /><div className="text-[11px] text-muted" title={dateTime(t.updated_at)}>Updated {relTime(t.updated_at)}</div></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="flex items-center justify-between px-4 py-2.5 border-t border-base text-xs text-muted">
            <span>{list.data.total} ticket{list.data.total === 1 ? '' : 's'}</span>
            <div className="flex items-center gap-2">
              <Button size="xs" icon={ChevronLeft} disabled={page <= 1} onClick={() => setPage((p) => p - 1)}>Prev</Button>
              <span>Page {page} of {totalPages}</span>
              <Button size="xs" disabled={page >= totalPages} onClick={() => setPage((p) => p + 1)}>Next<ChevronRight className="size-3.5" /></Button>
            </div>
          </div>
        </Card>
      )}
      {!can('tickets.view_all') && <p className="text-xs text-muted mt-3">You see tickets assigned to you, created by you, and the unassigned team queue.</p>}
      <ResolveModal ticket={action?.type === 'resolve' ? action.t : null} open={action?.type === 'resolve'} onClose={() => setAction(null)} onDone={() => { setAction(null); reload(); }} />
      <CloseModal ticket={action?.type === 'close' ? action.t : null} open={action?.type === 'close'} onClose={() => setAction(null)} onDone={() => { setAction(null); reload(); }} />
      <EscalateModal ticket={action?.type === 'escalate' ? action.t : null} open={action?.type === 'escalate'} onClose={() => setAction(null)} onDone={() => { setAction(null); reload(); }} />
    </div>
  );
}
