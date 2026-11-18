import { useEffect, useState, useCallback } from 'react';
import { NavLink, Outlet, useLocation, useNavigate } from 'react-router-dom';
import {
  LayoutDashboard, BookOpen, HelpCircle, MessageSquareText, Wrench, Ticket, ArrowUpCircle, ListChecks, MessagesSquare,
  GraduationCap, Scale, Megaphone, FolderCog, Settings, BarChart3, Search, Plus, Moon, Sun, Bell, LogOut, User, Menu as MenuIcon, X, KeyRound,
} from 'lucide-react';
import { useAuth } from '../lib/auth.jsx';
import { api } from '../lib/api.js';
import { relTime, ROLE_LABEL } from '../lib/format.js';
import { Avatar, IconButton, Menu, MenuItem, cx } from './ui.jsx';
import CommandSearch from './CommandSearch.jsx';
import NewTicketModal from './NewTicketModal.jsx';

const NAV = [
  { section: 'Workspace', items: [
    { to: '/', label: 'Dashboard', icon: LayoutDashboard, end: true },
    { to: '/tickets', label: 'Customer Issues', icon: Ticket, badge: 'tickets' },
    { to: '/escalations', label: 'Escalation Center', icon: ArrowUpCircle, badge: 'escalations' },
  ] },
  { section: 'Knowledge', items: [
    { to: '/kb', label: 'Knowledge Base', icon: BookOpen },
    { to: '/faqs', label: 'Customer FAQs', icon: HelpCircle },
    { to: '/templates', label: 'Response Templates', icon: MessageSquareText },
    { to: '/troubleshooting', label: 'Troubleshooting Guides', icon: Wrench },
    { to: '/sops', label: 'Support SOPs', icon: ListChecks },
    { to: '/communication', label: 'Customer Communication', icon: MessagesSquare },
    { to: '/policies', label: 'Policies & Guidelines', icon: Scale },
  ] },
  { section: 'Team', items: [
    { to: '/training', label: 'Training Center', icon: GraduationCap },
    { to: '/announcements', label: 'Announcements', icon: Megaphone, badge: 'announcements' },
  ] },
  { section: 'Administration', items: [
    { to: '/manage', label: 'Documentation Management', icon: FolderCog, perm: 'docs.edit' },
    { to: '/reports', label: 'Performance Reports', icon: BarChart3, perm: 'reports.view' },
    { to: '/settings', label: 'Settings', icon: Settings },
  ] },
];

function useTheme() {
  const [dark, setDark] = useState(() => document.documentElement.classList.contains('dark'));
  const toggle = () => {
    const next = !dark;
    document.documentElement.classList.toggle('dark', next);
    try { localStorage.setItem('byf-theme', next ? 'dark' : 'light'); } catch { /* ignore */ }
    setDark(next);
  };
  return [dark, toggle];
}

export default function Layout() {
  const { user, logout, can } = useAuth();
  const [dark, toggleTheme] = useTheme();
  const [searchOpen, setSearchOpen] = useState(false);
  const [newOpen, setNewOpen] = useState(false);
  const [preset, setPreset] = useState(null);
  const [drawer, setDrawer] = useState(false);
  const [counts, setCounts] = useState({});
  const [notifs, setNotifs] = useState({ followups: [], announcements: [] });
  const loc = useLocation();
  const nav = useNavigate();

  const loadCounts = useCallback(async () => {
    try {
      const [t, a, f, e] = await Promise.all([
        api('/tickets/counts'), api('/announcements'), api('/followups?status=pending'), api('/escalations?status=active&mine=1'),
      ]);
      const unread = a.filter((x) => !x.is_read);
      setCounts({ tickets: t.mine || 0, announcements: unread.length, escalations: e.length, overdue: t.overdue });
      const soon = Date.now() + 2 * 3600e3;
      setNotifs({ followups: f.filter((x) => new Date(x.due_at).getTime() < soon), announcements: unread.slice(0, 5) });
    } catch { /* ignore */ }
  }, []);

  useEffect(() => { loadCounts(); const t = setInterval(loadCounts, 60000); return () => clearInterval(t); }, [loadCounts]);
  useEffect(() => { setDrawer(false); }, [loc.pathname]);
  useEffect(() => {
    const onKey = (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); setSearchOpen(true); }
      else if (e.key === '/' && !['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName) && !document.activeElement?.isContentEditable) { e.preventDefault(); setSearchOpen(true); }
    };
    const onNew = (e) => { setPreset(e?.detail || null); setNewOpen(true); };
    const onRefresh = () => loadCounts();
    window.addEventListener('keydown', onKey);
    window.addEventListener('byf:new-ticket', onNew);
    window.addEventListener('byf:refresh-counts', onRefresh);
    return () => { window.removeEventListener('keydown', onKey); window.removeEventListener('byf:new-ticket', onNew); window.removeEventListener('byf:refresh-counts', onRefresh); };
  }, [loadCounts]);

  const notifCount = notifs.followups.length + notifs.announcements.length;

  const sidebar = (
    <nav className="flex flex-col h-full">
      <div className="flex items-center gap-2.5 px-4 h-14 shrink-0">
        <div className="size-8 rounded-lg bg-brand-500 grid place-items-center text-white font-bold text-[15px] shadow-sm">B</div>
        <div className="leading-tight">
          <div className="font-semibold text-[15px] tracking-tight">Byfluence</div>
          <div className="text-[11px] text-muted">Support Operating System</div>
        </div>
      </div>
      <div className="flex-1 overflow-y-auto px-2.5 pb-4">
        {NAV.map((g) => {
          const items = g.items.filter((i) => !i.perm || can(i.perm));
          if (!items.length) return null;
          return (
            <div key={g.section} className="mt-4">
              <div className="px-2.5 mb-1 text-[10.5px] font-semibold uppercase tracking-wider text-muted/80">{g.section}</div>
              {items.map((i) => (
                <NavLink key={i.to} to={i.to} end={i.end}
                  className={({ isActive }) => cx('group flex items-center gap-2.5 rounded-lg px-2.5 h-8 text-[13.5px] font-medium transition-colors',
                    isActive ? 'bg-brand-50 text-brand-700 dark:bg-brand-900/40 dark:text-brand-200' : 'text-[var(--text)]/80 hover:bg-[var(--surface-2)] hover:text-[var(--text)]')}>
                  {({ isActive }) => (<>
                    <i.icon className={cx('size-4 shrink-0', isActive ? 'text-brand-500' : 'text-muted group-hover:text-[var(--text)]')} />
                    <span className="truncate flex-1">{i.label}</span>
                    {i.badge && counts[i.badge] > 0 && (
                      <span className={cx('rounded-full px-1.5 min-w-5 text-center text-[11px] font-semibold tabular-nums', i.badge === 'announcements' ? 'bg-brand-500 text-white' : 'surface-2 text-muted')}>{counts[i.badge]}</span>
                    )}
                  </>)}
                </NavLink>
              ))}
            </div>
          );
        })}
      </div>
      <div className="border-t border-base p-3 flex items-center gap-2.5">
        <Avatar name={user.name} />
        <div className="min-w-0 flex-1">
          <div className="text-sm font-medium truncate">{user.name}</div>
          <div className="text-[11px] text-muted truncate">{ROLE_LABEL[user.role]}</div>
        </div>
      </div>
    </nav>
  );

  return (
    <div className="min-h-full flex">
      <aside className="hidden lg:block w-[248px] shrink-0 surface border-r border-base sticky top-0 h-screen self-start">{sidebar}</aside>
      {drawer && (
        <div className="lg:hidden fixed inset-0 z-40">
          <div className="absolute inset-0 bg-slate-900/40" onClick={() => setDrawer(false)} />
          <aside className="absolute inset-y-0 left-0 w-[264px] surface border-r border-base animate-in">
            <IconButton icon={X} label="Close menu" className="absolute right-2 top-2.5" onClick={() => setDrawer(false)} />
            {sidebar}
          </aside>
        </div>
      )}
      <div className="flex-1 min-w-0 flex flex-col">
        <header className="sticky top-0 z-30 h-14 shrink-0 surface/90 backdrop-blur border-b border-base flex items-center gap-2 px-3 sm:px-5" style={{ background: 'color-mix(in srgb, var(--surface) 92%, transparent)' }}>
          <IconButton icon={MenuIcon} label="Open menu" className="lg:hidden" onClick={() => setDrawer(true)} />
          <button type="button" onClick={() => setSearchOpen(true)}
            className="flex-1 min-w-0 max-w-xl flex items-center gap-2.5 h-9 px-3 rounded-lg border border-base surface-2 text-sm text-muted hover:border-brand-300 transition text-left">
            <Search className="size-4 shrink-0" />
            <span className="truncate flex-1"><span className="sm:hidden">Search…</span><span className="hidden sm:inline">Search issues, articles, templates, tickets…</span></span>
            <kbd className="hidden sm:inline text-[11px] font-mono border border-base rounded px-1.5 py-0.5 surface">Ctrl K</kbd>
          </button>
          <div className="hidden md:block flex-1" />
          <button type="button" onClick={() => { setPreset(null); setNewOpen(true); }}
            className="shrink-0 inline-flex items-center gap-1.5 h-9 px-3 rounded-lg bg-brand-500 hover:bg-brand-600 text-white text-sm font-medium shadow-sm">
            <Plus className="size-4" /><span className="hidden sm:inline">New Issue</span>
          </button>
          <IconButton icon={dark ? Sun : Moon} label={dark ? 'Light mode' : 'Dark mode'} onClick={toggleTheme} className="shrink-0 hidden sm:inline-flex" />
          <Menu trigger={({ toggle }) => (
            <button type="button" onClick={toggle} aria-label="Notifications" className="relative size-9 grid place-items-center rounded-lg text-muted hover:bg-[var(--surface-2)] hover:text-[var(--text)]">
              <Bell className="size-[18px]" />
              {notifCount > 0 && <span className="absolute top-1.5 right-1.5 min-w-4 h-4 px-1 rounded-full bg-red-500 text-white text-[10px] font-semibold grid place-items-center">{notifCount}</span>}
            </button>
          )}>
            <div className="w-80 max-w-[85vw]">
              <div className="px-2.5 py-1.5 text-xs font-semibold text-muted">Follow-ups due soon</div>
              {notifs.followups.length === 0 && <div className="px-2.5 pb-2 text-sm text-muted">Nothing due in the next 2 hours.</div>}
              {notifs.followups.map((f) => (
                <MenuItem key={f.id} onClick={() => nav(`/tickets/${f.number}`)}>
                  <span className="min-w-0">
                    <span className={cx('block text-xs font-medium', f.overdue ? 'text-red-600' : 'text-amber-600')}>{f.overdue ? 'Overdue' : 'Due'} {relTime(f.due_at)} · {f.number}</span>
                    <span className="block truncate">{f.reason}</span>
                  </span>
                </MenuItem>
              ))}
              <div className="px-2.5 py-1.5 text-xs font-semibold text-muted border-t border-base mt-1">Unread announcements</div>
              {notifs.announcements.length === 0 && <div className="px-2.5 pb-2 text-sm text-muted">All caught up.</div>}
              {notifs.announcements.map((a) => (
                <MenuItem key={a.id} onClick={() => nav(`/announcements#a${a.id}`)}>
                  <span className="truncate">{a.priority === 'critical' ? '🔴 ' : a.priority === 'important' ? '🟠 ' : ''}{a.title}</span>
                </MenuItem>
              ))}
            </div>
          </Menu>
          <Menu trigger={({ toggle }) => (
            <button type="button" onClick={toggle} className="rounded-full" aria-label="Account menu"><Avatar name={user.name} /></button>
          )}>
            <div className="px-2.5 py-2 border-b border-base mb-1">
              <div className="text-sm font-medium">{user.name}</div>
              <div className="text-xs text-muted">{user.email}</div>
            </div>
            <MenuItem icon={User} onClick={() => nav('/settings')}>Profile & preferences</MenuItem>
            <MenuItem icon={KeyRound} onClick={() => nav('/settings?tab=profile')}>Change password</MenuItem>
            <MenuItem icon={LogOut} onClick={logout}>Sign out</MenuItem>
          </Menu>
        </header>
        <main className="flex-1 min-w-0 px-4 sm:px-6 lg:px-8 py-6 max-w-[1480px] w-full mx-auto">
          <Outlet context={{ refreshCounts: loadCounts }} />
        </main>
      </div>
      <CommandSearch open={searchOpen} onClose={() => setSearchOpen(false)} />
      <NewTicketModal open={newOpen} preset={preset} onClose={() => setNewOpen(false)} onCreated={(t) => { setNewOpen(false); loadCounts(); nav(`/tickets/${t.number}`); }} />
    </div>
  );
}
