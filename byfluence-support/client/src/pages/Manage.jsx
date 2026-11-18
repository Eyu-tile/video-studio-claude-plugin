import { useMemo, useState } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { FolderCog, Plus, Search, Pencil, History, Eye, Trash2, CheckCircle2, XCircle, FolderTree, MessageSquareWarning, SearchX, FileText, MessageSquareText, Download, ClipboardCheck } from 'lucide-react';
import { api, qs, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { DOC_TYPES, DOC_STATUS, relTime, CHANNELS } from '../lib/format.js';
import { Badge, Button, Card, DocStatusBadge, EmptyState, ErrorState, Field, Input, Loading, Menu, MenuItem, Modal, PageHeader, Select, Tabs, useConfirm, useToast, Segmented } from '../components/ui.jsx';

function ContentTable({ status: fixedStatus }) {
  const { can } = useAuth();
  const toast = useToast();
  const confirm = useConfirm();
  const nav = useNavigate();
  const [f, setF] = useState({ type: '', status: fixedStatus || '', q: '', pending: '' });
  const { data, loading, error, reload } = useApi(`/docs${qs({ type: f.type, status: f.status || 'all', q: f.q, pending: f.pending, sort: 'updated', limit: 2000 })}`, [JSON.stringify(f)]);
  const setStatus = async (d, s) => {
    try { await api(`/docs/${d.slug}/status`, { method: 'POST', body: { status: s } }); toast.success(`${d.title} → ${DOC_STATUS[s].label}`); reload(true); } catch (e) { toast.error(e); }
  };
  const del = async (d) => {
    if (!(await confirm({ title: 'Delete permanently?', message: `“${d.title}” will be deleted. A final snapshot is kept in version history, but the document disappears everywhere.`, danger: true, typeToConfirm: 'DELETE', confirmLabel: 'Delete permanently' }))) return;
    try { await api(`/docs/${d.slug}`, { method: 'DELETE' }); toast.success('Deleted'); reload(true); } catch (e) { toast.error(e); }
  };
  return (
    <div className="space-y-3">
      <div className="flex flex-wrap gap-2">
        <div className="relative flex-1 min-w-[220px]"><Search className="size-4 absolute left-3 top-2.5 text-muted" /><Input className="pl-9" placeholder="Search title or ID…" value={f.q} onChange={(e) => setF({ ...f, q: e.target.value })} /></div>
        <Select className="w-auto" value={f.type} onChange={(e) => setF({ ...f, type: e.target.value })}><option value="">All types</option>{Object.entries(DOC_TYPES).map(([k, v]) => <option key={k} value={k}>{v.label}</option>)}</Select>
        {!fixedStatus && <Select className="w-auto" value={f.status} onChange={(e) => setF({ ...f, status: e.target.value })}><option value="">All statuses</option>{Object.entries(DOC_STATUS).map(([k, v]) => <option key={k} value={k}>{v.label}</option>)}</Select>}
        <Select className="w-auto" value={f.pending} onChange={(e) => setF({ ...f, pending: e.target.value })}><option value="">Any</option><option value="1">Policy pending only</option></Select>
      </div>
      {loading && !data ? <Loading /> : error ? <ErrorState error={error} /> : data.length === 0 ? <Card><EmptyState icon={FileText} title={fixedStatus === 'review' ? 'Nothing waiting for review' : 'No documents'} /></Card> : (
        <Card className="overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="surface-2 text-xs text-muted"><tr className="text-left"><th className="px-4 py-2.5 font-medium">Document</th><th className="px-3 py-2.5 font-medium">Type</th><th className="px-3 py-2.5 font-medium hidden md:table-cell">Category</th><th className="px-3 py-2.5 font-medium">Status</th><th className="px-3 py-2.5 font-medium hidden lg:table-cell">Updated</th><th className="px-3 py-2.5 font-medium hidden lg:table-cell text-right">Views</th><th className="px-3 py-2.5" /></tr></thead>
              <tbody>
                {data.map((d) => (
                  <tr key={d.slug} className="border-t border-base hover:bg-[var(--surface-2)]">
                    <td className="px-4 py-2 max-w-[380px]"><Link to={`/kb/${d.slug}`} className="font-medium hover:text-brand-600 line-clamp-1">{d.title}</Link><div className="text-[11px] text-muted font-mono">{d.slug}{d.policy_pending && <Badge tone="amber" className="ml-2 font-sans">Policy pending</Badge>}</div></td>
                    <td className="px-3 py-2 whitespace-nowrap text-[13px]">{DOC_TYPES[d.type]?.label}</td>
                    <td className="px-3 py-2 hidden md:table-cell text-[13px] text-muted max-w-[200px] truncate">{d.parent_category_name ? `${d.parent_category_name} → ` : ''}{d.category_name}</td>
                    <td className="px-3 py-2"><DocStatusBadge status={d.status} /></td>
                    <td className="px-3 py-2 hidden lg:table-cell text-xs text-muted whitespace-nowrap">v{d.version} · {relTime(d.updated_at)}<br />{d.updated_by_name}</td>
                    <td className="px-3 py-2 hidden lg:table-cell text-right tabular-nums text-muted">{d.views}</td>
                    <td className="px-3 py-2 text-right whitespace-nowrap">
                      <Menu trigger={({ toggle }) => <Button size="xs" onClick={toggle}>Actions</Button>}>
                        <MenuItem icon={Eye} onClick={() => nav(`/kb/${d.slug}`)}>View</MenuItem>
                        <MenuItem icon={Pencil} onClick={() => nav(`/manage/docs/${d.slug}`)}>Edit</MenuItem>
                        <MenuItem icon={History} onClick={() => nav(`/manage/history/doc/${d.slug}`)}>Version history</MenuItem>
                        {d.status !== 'published' && (d.type === 'policy' ? can('policies.publish') : can('docs.publish')) && <MenuItem icon={CheckCircle2} onClick={() => setStatus(d, 'published')}>Approve & publish</MenuItem>}
                        {d.status === 'review' && <MenuItem icon={XCircle} onClick={() => setStatus(d, 'draft')}>Send back to draft</MenuItem>}
                        {d.status === 'draft' && <MenuItem icon={ClipboardCheck} onClick={() => setStatus(d, 'review')}>Submit for review</MenuItem>}
                        {d.status !== 'archived' && (d.type === 'policy' ? can('policies.publish') : can('docs.publish')) && <MenuItem onClick={() => setStatus(d, 'archived')}>Archive</MenuItem>}
                        {d.status === 'archived' && can('docs.delete') && <MenuItem icon={Trash2} danger onClick={() => del(d)}>Delete permanently</MenuItem>}
                      </Menu>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="px-4 py-2 text-xs text-muted border-t border-base">{data.length} documents</div>
        </Card>
      )}
    </div>
  );
}

function TemplatesTable() {
  const [q, setQ] = useState('');
  const { data, loading } = useApi('/templates?status=all');
  const list = (data || []).filter((t) => !q || `${t.name} ${t.slug}`.toLowerCase().includes(q.toLowerCase()));
  if (loading && !data) return <Loading />;
  return (
    <div className="space-y-3">
      <Input placeholder="Search templates…" value={q} onChange={(e) => setQ(e.target.value)} className="max-w-sm" />
      <Card className="overflow-x-auto">
        <table className="w-full text-sm">
          <thead className="surface-2 text-xs text-muted"><tr className="text-left"><th className="px-4 py-2.5 font-medium">Template</th><th className="px-3 py-2.5 font-medium">Category</th><th className="px-3 py-2.5 font-medium">Channel</th><th className="px-3 py-2.5 font-medium">Languages</th><th className="px-3 py-2.5 font-medium">Status</th><th className="px-3 py-2.5 font-medium text-right">Used</th><th /></tr></thead>
          <tbody>{list.map((t) => (
            <tr key={t.slug} className="border-t border-base hover:bg-[var(--surface-2)]">
              <td className="px-4 py-2"><Link to={`/templates/${t.slug}`} className="font-medium hover:text-brand-600">{t.name}</Link><div className="text-[11px] text-muted font-mono">{t.slug}</div></td>
              <td className="px-3 py-2 text-[13px]">{t.category_name}</td>
              <td className="px-3 py-2 text-[13px]">{CHANNELS[t.channel]} · <span className="capitalize">{t.style}</span></td>
              <td className="px-3 py-2">{t.content_am && <Badge tone="gray">AM</Badge>} {t.content_en && <Badge tone="gray">EN</Badge>}</td>
              <td className="px-3 py-2"><DocStatusBadge status={t.status} /></td>
              <td className="px-3 py-2 text-right tabular-nums text-muted">{t.usage_count}</td>
              <td className="px-3 py-2 text-right whitespace-nowrap"><Link to={`/manage/templates/${t.slug}`}><Button size="xs" icon={Pencil}>Edit</Button></Link></td>
            </tr>
          ))}</tbody>
        </table>
      </Card>
    </div>
  );
}

function FeedbackQueue() {
  const toast = useToast();
  const [status, setStatus] = useState('open');
  const { data, loading, reload } = useApi(`/feedback?status=${status}`, [status]);
  const act = async (f, s) => { try { await api(`/feedback/${f.id}`, { method: 'PATCH', body: { status: s } }); reload(true); } catch (e) { toast.error(e); } };
  return (
    <div className="space-y-3">
      <Segmented value={status} onChange={setStatus} options={[{ value: 'open', label: 'Open' }, { value: 'done', label: 'Done' }, { value: 'dismissed', label: 'Dismissed' }, { value: 'all', label: 'All' }]} />
      {loading && !data ? <Loading /> : !data?.length ? <Card><EmptyState icon={MessageSquareWarning} title="No feedback here">Agents report outdated content and suggest edits from any article.</EmptyState></Card> : data.map((f) => (
        <Card key={f.id} className="p-4">
          <div className="flex flex-wrap items-start justify-between gap-3">
            <div className="min-w-0">
              <div className="flex items-center gap-2 text-xs"><Badge tone={f.kind === 'outdated' ? 'red' : f.kind === 'suggestion' ? 'blue' : 'gray'}>{f.kind.replace('_', ' ')}</Badge><span className="text-muted">{f.user_name} · {relTime(f.created_at)}</span></div>
              <Link to={`/kb/${f.slug}`} className="block font-medium mt-1 hover:text-brand-600">{f.title}</Link>
              {f.comment && <p className="text-sm mt-1.5 whitespace-pre-wrap">{f.comment}</p>}
            </div>
            {f.status === 'open' && <div className="flex gap-2"><Link to={`/manage/docs/${f.slug}`}><Button size="sm" icon={Pencil}>Edit article</Button></Link><Button size="sm" icon={CheckCircle2} onClick={() => act(f, 'done')}>Done</Button><Button size="sm" variant="ghost" onClick={() => act(f, 'dismissed')}>Dismiss</Button></div>}
          </div>
        </Card>
      ))}
    </div>
  );
}

function CategoryManager() {
  const { can } = useAuth();
  const toast = useToast();
  const confirm = useConfirm();
  const [scope, setScope] = useState('kb');
  const { data, loading, reload } = useApi(`/categories?scope=${scope}`, [scope]);
  const [form, setForm] = useState(null);
  const save = async () => {
    try {
      if (form.id) await api(`/categories/${form.id}`, { method: 'PATCH', body: form });
      else await api('/categories', { method: 'POST', body: { ...form, scope } });
      toast.success('Category saved'); setForm(null); reload(true);
    } catch (e) { toast.error(e); }
  };
  const del = async (c) => {
    if (!(await confirm({ title: `Delete “${c.name}”?`, message: 'Only empty categories can be deleted. Subcategories are deleted with it.', danger: true, confirmLabel: 'Delete' }))) return;
    try { await api(`/categories/${c.id}`, { method: 'DELETE' }); toast.success('Deleted'); reload(true); } catch (e) { toast.error(e); }
  };
  const editable = can('categories.manage');
  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <Segmented value={scope} onChange={setScope} options={[{ value: 'kb', label: 'Knowledge base' }, { value: 'template', label: 'Templates' }, { value: 'sop', label: 'SOPs' }, { value: 'policy', label: 'Policies' }, { value: 'communication', label: 'Communication' }]} />
        {editable && <Button icon={Plus} onClick={() => setForm({ name: '', name_am: '', description: '', icon: '', parent_id: null })}>New category</Button>}
      </div>
      {!editable && <p className="text-xs text-muted">Only administrators can change categories.</p>}
      {loading && !data ? <Loading /> : (
        <div className="grid md:grid-cols-2 gap-3">
          {data.map((c) => (
            <Card key={c.id} className="p-4">
              <div className="flex items-start justify-between gap-2">
                <div><div className="font-semibold">{c.name} <span className="text-xs font-normal text-muted">({c.count})</span></div>{c.name_am && <div className="text-xs text-muted">{c.name_am}</div>}{c.description && <p className="text-xs text-muted mt-1">{c.description}</p>}</div>
                {editable && <div className="flex gap-1 shrink-0"><Button size="xs" icon={Pencil} onClick={() => setForm({ ...c })} /><Button size="xs" icon={Plus} title="Add subcategory" onClick={() => setForm({ name: '', parent_id: c.id, _parent: c.name })} /><Button size="xs" icon={Trash2} onClick={() => del(c)} /></div>}
              </div>
              {c.subcategories?.length > 0 && <ul className="mt-2.5 space-y-1">{c.subcategories.map((s) => (
                <li key={s.id} className="flex items-center justify-between text-sm pl-3 border-l-2 border-base"><span>{s.name} <span className="text-xs text-muted">({s.count})</span></span>{editable && <span className="flex gap-1"><button type="button" onClick={() => setForm({ ...s })} aria-label="Edit"><Pencil className="size-3.5 text-muted" /></button><button type="button" onClick={() => del(s)} aria-label="Delete"><Trash2 className="size-3.5 text-muted" /></button></span>}</li>
              ))}</ul>}
            </Card>
          ))}
        </div>
      )}
      <Modal open={!!form} onClose={() => setForm(null)} title={form?.id ? 'Edit category' : form?._parent ? `New subcategory in ${form._parent}` : 'New category'} size="sm"
        footer={<><Button onClick={() => setForm(null)}>Cancel</Button><Button variant="primary" disabled={!form?.name?.trim()} onClick={save}>Save</Button></>}>
        {form && <div className="space-y-3">
          <Field label="Name" required><Input value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} /></Field>
          {!form.parent_id && <><Field label="Amharic name"><Input value={form.name_am || ''} onChange={(e) => setForm({ ...form, name_am: e.target.value })} /></Field>
            <Field label="Description"><Input value={form.description || ''} onChange={(e) => setForm({ ...form, description: e.target.value })} /></Field>
            <Field label="Icon" hint="A Lucide icon name, e.g. credit-card, video, store"><Input value={form.icon || ''} onChange={(e) => setForm({ ...form, icon: e.target.value })} /></Field></>}
        </div>}
      </Modal>
    </div>
  );
}

function SearchGaps() {
  const { data, loading } = useApi('/search/gaps');
  if (loading && !data) return <Loading />;
  return (
    <Card>
      <div className="px-4 py-3 border-b border-base text-sm text-muted">Searches employees made that returned nothing. Each one is a candidate for a new article, a new tag on an existing article, or a new synonym (Settings → Search).</div>
      {!data?.length ? <EmptyState icon={SearchX} title="No knowledge gaps recorded" /> : (
        <table className="w-full text-sm"><tbody>{data.map((g) => (
          <tr key={g.q} className="border-t border-base first:border-t-0"><td className="px-4 py-2 font-medium">{g.q}</td><td className="px-3 py-2 text-muted">{g.n}× · last {relTime(g.last)}</td>
            <td className="px-3 py-2 text-right"><Link to={`/manage/docs/new?type=article`}><Button size="xs" icon={Plus}>Write article</Button></Link></td></tr>
        ))}</tbody></table>
      )}
    </Card>
  );
}

export default function Manage() {
  const { can } = useAuth();
  const [params, setParams] = useSearchParams();
  const tab = params.get('tab') || 'content';
  const review = useApi('/docs?status=review&limit=500');
  const fb = useApi(can('feedback.manage') ? '/feedback?status=open' : null);
  const tabs = useMemo(() => [
    { value: 'content', label: 'All content', icon: FileText },
    { value: 'templates', label: 'Templates', icon: MessageSquareText },
    { value: 'review', label: 'Review queue', icon: ClipboardCheck, count: review.data?.length },
    { value: 'feedback', label: 'Feedback', icon: MessageSquareWarning, count: fb.data?.length },
    { value: 'categories', label: 'Categories', icon: FolderTree },
    { value: 'gaps', label: 'Knowledge gaps', icon: SearchX },
  ], [review.data, fb.data]);
  if (!can('docs.edit')) return <ErrorState error={{ status: 403, message: 'Documentation management is available to supervisors and administrators.' }} />;
  return (
    <div>
      <PageHeader icon={FolderCog} title="Documentation Management" subtitle="Create, edit, review, publish and archive every piece of support content. All changes are versioned and can be restored."
        actions={<>
          {can('backup.download') && <a href="/api/admin/export"><Button icon={Download}>Export content</Button></a>}
          <Menu trigger={({ toggle }) => <Button variant="primary" icon={Plus} onClick={toggle}>Create</Button>}>
            {Object.entries(DOC_TYPES).filter(([k]) => k !== 'policy' || can('docs.edit')).map(([k, v]) => <Link key={k} to={`/manage/docs/new?type=${k}`}><MenuItem>{v.label}</MenuItem></Link>)}
            <Link to="/manage/templates/new"><MenuItem>Response template</MenuItem></Link>
          </Menu>
        </>} />
      <Tabs className="mb-5" value={tab} onChange={(v) => setParams({ tab: v })} tabs={tabs} />
      {tab === 'content' && <ContentTable />}
      {tab === 'templates' && <TemplatesTable />}
      {tab === 'review' && <ContentTable status="review" />}
      {tab === 'feedback' && <FeedbackQueue />}
      {tab === 'categories' && <CategoryManager />}
      {tab === 'gaps' && <SearchGaps />}
    </div>
  );
}
