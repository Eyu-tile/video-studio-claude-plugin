import { useMemo, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { Scale, ToggleRight, ClipboardList, ShieldCheck, Settings as SettingsIcon } from 'lucide-react';
import { useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { DOC_TYPES, FEATURE_STATUS } from '../lib/format.js';
import { Card, Callout, FeatureBadge, Loading, PageHeader, Tabs, Input } from '../components/ui.jsx';
import DocList from './DocList.jsx';

function FeatureStatus() {
  const { settings, can } = useAuth();
  const features = settings?.features || [];
  const groups = [
    ['Live', features.filter((f) => f.status === 'live' || f.status === 'beta')],
    ['Unconfirmed — verify before answering', features.filter((f) => f.status === 'unconfirmed')],
    ['Planned — not available to customers', features.filter((f) => f.status === 'planned' || f.status === 'unavailable')],
  ];
  return (
    <div className="space-y-4">
      <Callout tone="note" title="Use this page before telling a customer that something is available.">
        Planned features must never be described as live. If a status says “unverified”, an administrator has not yet confirmed it against production.
        {can('settings.manage') && <> <Link to="/settings?tab=features" className="font-medium">Edit feature status →</Link></>}
      </Callout>
      {groups.map(([title, list]) => list.length > 0 && (
        <Card key={title}>
          <div className="px-4 py-3 border-b border-base font-semibold text-sm">{title}</div>
          <div className="divide-y divide-[var(--border)]">
            {list.map((f) => (
              <div key={f.key} className="flex flex-wrap items-center gap-3 px-4 py-2.5">
                <div className="flex-1 min-w-[200px]">
                  <div className="text-sm font-medium">{f.name}</div>
                  {f.notes && <div className="text-xs text-muted mt-0.5">{f.notes}</div>}
                </div>
                <FeatureBadge status={f.status} verified={f.verified} />
              </div>
            ))}
          </div>
        </Card>
      ))}
      <p className="text-xs text-muted">Status values: {Object.values(FEATURE_STATUS).map((s) => s.label).join(' · ')}</p>
    </div>
  );
}

function PendingTracker() {
  const { data, loading } = useApi('/docs?pending=1&limit=2000&sort=title');
  const [q, setQ] = useState('');
  const groups = useMemo(() => {
    const g = new Map();
    for (const d of (data || []).filter((x) => !q || x.title.toLowerCase().includes(q.toLowerCase()))) {
      const k = d.parent_category_name || d.category_name || 'Other';
      if (!g.has(k)) g.set(k, []);
      g.get(k).push(d);
    }
    return [...g.entries()].sort((a, b) => b[1].length - a[1].length);
  }, [data, q]);
  if (loading) return <Loading />;
  return (
    <div className="space-y-4">
      <Callout tone="policy" title={`${data.length} documents contain decisions that management has not yet approved`}>
        Each linked document lists the exact open decisions in its “Policy Pending Approval” section. Use this as management’s to-do list. Once a policy is approved, update the policy document and remove the pending section from the affected articles.
      </Callout>
      <Input placeholder="Filter…" value={q} onChange={(e) => setQ(e.target.value)} className="max-w-sm" />
      <div className="grid md:grid-cols-2 gap-4">
        {groups.map(([k, list]) => (
          <Card key={k}>
            <div className="px-4 py-2.5 border-b border-base flex justify-between text-sm font-semibold"><span>{k}</span><span className="text-muted tabular-nums">{list.length}</span></div>
            <ul className="py-1 max-h-72 overflow-y-auto">
              {list.map((d) => <li key={d.slug}><Link to={`/kb/${d.slug}#policy_pending`} className="flex justify-between gap-3 px-4 py-1.5 text-sm hover:bg-[var(--surface-2)]"><span className="truncate">{d.title}</span><span className="text-[11px] text-muted shrink-0">{DOC_TYPES[d.type]?.label}</span></Link></li>)}
            </ul>
          </Card>
        ))}
      </div>
    </div>
  );
}

function SafetyRules() {
  return (
    <Card className="p-5">
      <div className="flex items-center gap-2 font-semibold mb-3"><ShieldCheck className="size-5 text-emerald-600" />Operational safety rules — always apply</div>
      <ol className="grid md:grid-cols-2 gap-x-8 gap-y-2 text-sm list-decimal pl-5">
        {['Never ask customers for passwords or OTP codes.', 'Never expose private customer information to unauthorized employees.', 'Never approve refunds without the required authorization.', 'Never mark a payment successful without verification by transaction reference.',
          'Never promise refund timelines that have not been officially confirmed.', 'Never invent Byfluence policies.', 'Never mark unresolved tickets as completed.', 'Important ticket actions are recorded in the audit log.',
          'Access is restricted by employee permissions.', 'Uploaded customer documents are protected — never forward them.', 'Destructive actions require confirmation.', 'Data is backed up and recoverable.'].map((r) => <li key={r}>{r}</li>)}
      </ol>
      <Link to="/kb/pol-operational-safety-rules" className="inline-block mt-3 text-sm text-brand-600 font-medium">Read the full policy →</Link>
    </Card>
  );
}

export default function Policies() {
  const [params, setParams] = useSearchParams();
  const tab = params.get('tab') || 'policies';
  const { can } = useAuth();
  return (
    <div className="max-w-6xl">
      <PageHeader icon={Scale} title="Policies & Guidelines" subtitle="Approved rules for support staff, the live status of features and payment methods, and the list of decisions still waiting for management approval." />
      <Tabs className="mb-5" value={tab} onChange={(v) => setParams({ tab: v })} tabs={[
        { value: 'policies', label: 'Policies', icon: Scale },
        { value: 'features', label: 'Feature Status', icon: ToggleRight },
        { value: 'pending', label: 'Policy Pending Tracker', icon: ClipboardList },
      ]} />
      {tab === 'policies' && <div className="space-y-5"><SafetyRules /><DocList type="policy" embedded /></div>}
      {tab === 'features' && <FeatureStatus />}
      {tab === 'pending' && <PendingTracker />}
      {can('settings.manage') && tab === 'features' && <Link to="/settings?tab=features" className="mt-4 inline-flex items-center gap-1.5 text-sm text-brand-600"><SettingsIcon className="size-4" />Manage in Settings</Link>}
    </div>
  );
}
