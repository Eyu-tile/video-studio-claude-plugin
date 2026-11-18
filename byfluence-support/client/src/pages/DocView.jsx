import { useMemo, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import {
  ChevronRight, Pencil, History, Printer, Link2, ThumbsUp, ThumbsDown, Flag, Plus, ArrowUpCircle, Lock, Scale, MessageSquareText, Clock,
  Users, Building2, AlertTriangle, CheckCircle2, ListChecks, Wand2,
} from 'lucide-react';
import { api, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { DOC_TYPES, dateTime, relTime, hours, CHANNELS } from '../lib/format.js';
import {
  Badge, Button, Card, CopyButton, DocStatusBadge, ErrorState, FeatureBadge, Loading, Modal, PriorityBadge, Segmented, Tabs, Textarea, useToast, cx, copyText,
} from '../components/ui.jsx';
import RichText, { htmlToPlain } from '../components/RichText.jsx';
import TemplateFiller from '../components/TemplateFiller.jsx';
import NewTicketModal from '../components/NewTicketModal.jsx';

const RESPONSE_KEYS = {
  recommended: ['response_en', 'response_am', 'Recommended response'],
  short: ['short_en', 'short_am', 'Short (Telegram)'],
  followup: ['followup_en', 'followup_am', 'Follow-up'],
  answer: ['answer_en', 'answer_am', 'Answer'],
};
const SPECIAL = new Set(['response_en', 'response_am', 'short_en', 'short_am', 'followup_en', 'followup_am', 'answer_en', 'answer_am', 'internal', 'policy_pending', 'escalation']);
const SECTION_ICON = { steps: ListChecks, sop_steps: ListChecks, collect: ListChecks, customer_steps: ListChecks };

export function ResponsesCard({ sections, docTitle, defaultLang }) {
  const by = Object.fromEntries(sections.map((s) => [s.key, s]));
  const kinds = Object.entries(RESPONSE_KEYS).filter(([, [en, am]]) => by[en] || by[am]);
  const [kind, setKind] = useState(kinds[0]?.[0]);
  const [lang, setLang] = useState(defaultLang || 'am');
  const [fill, setFill] = useState(false);
  if (!kinds.length) return null;
  const [enKey, amKey] = RESPONSE_KEYS[kind];
  const sec = (lang === 'am' ? by[amKey] : by[enKey]) || by[enKey] || by[amKey];
  const plainEn = by[enKey] ? htmlToPlain(by[enKey].html) : '';
  const plainAm = by[amKey] ? htmlToPlain(by[amKey].html) : '';
  return (
    <Card id="responses" className="overflow-hidden border-brand-200 dark:border-brand-800 scroll-mt-20">
      <div className="flex flex-wrap items-center justify-between gap-2 px-4 pt-3 bg-brand-50/60 dark:bg-brand-900/20">
        <div className="flex items-center gap-2 font-semibold text-[15px]"><MessageSquareText className="size-[18px] text-brand-500" />Customer responses</div>
        <Segmented size="xs" value={lang} onChange={setLang} options={[{ value: 'am', label: 'አማርኛ' }, { value: 'en', label: 'English' }]} />
      </div>
      <div className="bg-brand-50/60 dark:bg-brand-900/20 px-2"><Tabs className="border-b-0" value={kind} onChange={setKind} tabs={kinds.map(([k, [, , l]]) => ({ value: k, label: l }))} /></div>
      <div className="p-4 border-t border-base" lang={lang}>
        <RichText html={sec?.html} className={lang === 'am' ? 'text-[15px]' : ''} />
        <div className="flex flex-wrap gap-2 mt-4">
          <CopyButton variant="primary" label={`Copy ${lang === 'am' ? 'Amharic' : 'English'}`} getText={() => (lang === 'am' ? plainAm : plainEn)} />
          <Button icon={Wand2} size="sm" onClick={() => setFill(true)}>Fill placeholders</Button>
        </div>
      </div>
      <Modal open={fill} onClose={() => setFill(false)} title={`Fill & copy — ${docTitle}`} size="xl">
        <TemplateFiller template={{ slug: `doc-${kind}`, name: `${docTitle} (${RESPONSE_KEYS[kind][2]})`, channel: kind === 'short' ? 'telegram' : 'any', content_en: plainEn, content_am: plainAm }} />
      </Modal>
    </Card>
  );
}

function FeedbackBox({ slug }) {
  const toast = useToast();
  const [sent, setSent] = useState(null);
  const [open, setOpen] = useState(null);
  const [comment, setComment] = useState('');
  const send = async (kind) => {
    try {
      await api(`/docs/${slug}/feedback`, { method: 'POST', body: { kind, comment } });
      setSent(kind); setOpen(null); setComment('');
      toast.success(kind === 'helpful' || kind === 'not_helpful' ? 'Thanks for the feedback' : 'Sent to the documentation team');
    } catch (e) { toast.error(e); }
  };
  return (
    <Card className="p-4 no-print">
      <div className="text-sm font-medium mb-2">Was this article helpful?</div>
      {sent === 'helpful' || sent === 'not_helpful' ? <p className="text-sm text-muted">Thank you!</p> : (
        <div className="flex gap-2">
          <Button size="sm" icon={ThumbsUp} onClick={() => send('helpful')}>Yes</Button>
          <Button size="sm" icon={ThumbsDown} onClick={() => send('not_helpful')}>No</Button>
        </div>
      )}
      <div className="flex flex-wrap gap-x-3 gap-y-1 mt-3 text-xs">
        <button type="button" className="text-muted hover:text-brand-600 flex items-center gap-1" onClick={() => setOpen('outdated')}><Flag className="size-3" />Report outdated</button>
        <button type="button" className="text-muted hover:text-brand-600 flex items-center gap-1" onClick={() => setOpen('suggestion')}><Pencil className="size-3" />Suggest an edit</button>
      </div>
      <Modal open={!!open} onClose={() => setOpen(null)} title={open === 'outdated' ? 'Report outdated information' : 'Suggest an edit'} size="sm"
        footer={<><Button onClick={() => setOpen(null)}>Cancel</Button><Button variant="primary" disabled={!comment.trim()} onClick={() => send(open)}>Send</Button></>}>
        <Textarea rows={4} value={comment} onChange={(e) => setComment(e.target.value)} placeholder="What is wrong or missing? Be specific — e.g. “Telebirr is now live; step 3 is outdated.”" />
        <p className="text-xs text-muted mt-2">Goes to supervisors in Documentation Management → Feedback.</p>
      </Modal>
    </Card>
  );
}

export default function DocView() {
  const { slug } = useParams();
  const { can, settings, user } = useAuth();
  const toast = useToast();
  const navigate = useNavigate();
  const { data, loading, error, reload } = useApi(`/docs/${slug}`, [slug]);
  const [ticketOpen, setTicketOpen] = useState(false);
  const preset = useMemo(() => data && ({
    category_id: data.path[0] ? String(data.path[0].id) : '', subcategory_id: data.path[1] ? String(data.path[1].id) : '',
    priority: data.doc.priority, linked_docs: [data.doc.slug], title: data.doc.type === 'article' ? data.doc.title : '',
  }), [data]);

  if (loading && !data) return <Loading />;
  if (error) return <ErrorState error={error} onRetry={reload} />;
  const { doc, path, related, backlinks, templates, features, versions, department } = data;
  const sections = doc.sections;
  const by = Object.fromEntries(sections.map((s) => [s.key, s]));
  const body = sections.filter((s) => !SPECIAL.has(s.key));
  const firstResponseIdx = sections.findIndex((s) => /^(response|short|followup|answer)_/.test(s.key));
  const before = firstResponseIdx === -1 ? body : body.filter((s) => sections.indexOf(s) < firstResponseIdx);
  const after = firstResponseIdx === -1 ? [] : body.filter((s) => sections.indexOf(s) > firstResponseIdx);
  const notLive = features.filter((f) => f.status !== 'live' || !f.verified);
  const sla = settings?.sla?.[doc.priority];
  const typeMeta = DOC_TYPES[doc.type];
  const isIssue = ['article', 'troubleshooting'].includes(doc.type);
  const toc = [
    ...before.map((s) => ({ id: s.key, label: s.label })),
    ...(firstResponseIdx !== -1 ? [{ id: 'responses', label: 'Customer responses' }] : []),
    ...(by.escalation ? [{ id: 'escalation', label: 'Escalation conditions' }] : []),
    ...after.map((s) => ({ id: s.key, label: s.label })),
    ...(by.policy_pending ? [{ id: 'policy_pending', label: 'Policy pending approval' }] : []),
    ...(by.internal ? [{ id: 'internal', label: 'Internal notes' }] : []),
  ];

  const Section = ({ s }) => {
    const Icon = SECTION_ICON[s.key];
    return (
      <section id={s.key} className="scroll-mt-20">
        <h2 className="flex items-center gap-2 text-[15px] font-semibold mb-2">{Icon && <Icon className="size-4 text-brand-500" />}{s.label}</h2>
        <RichText html={s.html} interactive />
      </section>
    );
  };

  return (
    <div className="max-w-[1200px] mx-auto">
      <div className="text-xs text-muted mb-2 flex items-center gap-1 flex-wrap">
        <Link to={typeMeta.path} className="hover:text-brand-600">{typeMeta.plural}</Link>
        {path.map((p, i) => (
          <span key={p.id} className="flex items-center gap-1"><ChevronRight className="size-3" />
            {p.scope === 'kb' ? <Link to={`/kb/c/${path[0].slug}`} className="hover:text-brand-600">{p.name}</Link> : <span>{p.name}</span>}{i === 0 && path.length === 1 ? '' : ''}
          </span>
        ))}
      </div>
      <div className="flex flex-wrap items-start justify-between gap-4 mb-4">
        <div className="min-w-0 max-w-3xl">
          <div className="flex flex-wrap items-center gap-1.5 mb-2">
            <Badge tone={doc.type === 'troubleshooting' ? 'violet' : doc.type === 'policy' ? 'amber' : 'blue'}>{typeMeta.label}</Badge>
            {doc.status !== 'published' && <DocStatusBadge status={doc.status} />}
            {isIssue && <PriorityBadge priority={doc.priority} />}
            {doc.audience !== 'both' && <Badge tone={doc.audience === 'internal' ? 'slate' : 'sky'}>{doc.audience === 'internal' ? <><Lock className="size-3" />Internal only</> : `For ${doc.audience}s`}</Badge>}
            {doc.policy_pending && <a href="#policy_pending"><Badge tone="amber"><Scale className="size-3" />Policy pending approval</Badge></a>}
          </div>
          <h1 className="text-2xl font-semibold tracking-tight leading-snug">{doc.title}</h1>
          {doc.summary && <p className="text-[15px] text-muted mt-2 leading-relaxed">{doc.summary}</p>}
          <p className="text-xs text-muted mt-2">Version {doc.version} · Last updated {dateTime(doc.updated_at)} ({relTime(doc.updated_at)}){doc.updated_by_name ? ` by ${doc.updated_by_name}` : ''}</p>
        </div>
        <div className="flex flex-wrap gap-2 no-print">
          {isIssue && <Button variant="primary" icon={Plus} onClick={() => setTicketOpen(true)}>Create ticket for this issue</Button>}
          <Button icon={Link2} onClick={async () => { await copyText(window.location.href); toast.success('Link copied'); }}>Copy link</Button>
          <Button icon={Printer} onClick={() => window.print()} className="hidden sm:inline-flex">Print</Button>
          {can('docs.edit') && <Link to={`/manage/docs/${doc.slug}`}><Button icon={Pencil}>Edit</Button></Link>}
          {can('docs.read_unpublished') && versions > 1 && <Link to={`/manage/history/doc/${doc.slug}`}><Button icon={History}>History ({versions})</Button></Link>}
        </div>
      </div>

      {notLive.length > 0 && (
        <div className="callout callout-warning mb-4 prose-byf">
          <p className="font-semibold">Check feature status before confirming anything to the customer</p>
          <div className="flex flex-wrap gap-2 mt-1.5 text-sm">
            {notLive.map((f) => <span key={f.key} className="inline-flex items-center gap-1.5">{f.name}: <FeatureBadge status={f.status} verified={f.verified} /></span>)}
          </div>
          <p className="text-xs mt-1.5"><Link to="/policies?tab=features">Open the Feature Status page</Link> — administrators keep it up to date.</p>
        </div>
      )}

      <div className="grid lg:grid-cols-[1fr_290px] gap-6">
        <article className="min-w-0 space-y-6">
          {before.map((s) => <Section key={s.key} s={s} />)}
          {firstResponseIdx !== -1 && <ResponsesCard sections={sections} docTitle={doc.title} defaultLang={user.preferences?.language} />}
          {by.escalation && (
            <section id="escalation" className="scroll-mt-20 rounded-xl border border-orange-200 dark:border-orange-900 bg-orange-50/50 dark:bg-orange-950/20 p-4">
              <h2 className="flex items-center gap-2 text-[15px] font-semibold mb-2"><ArrowUpCircle className="size-4 text-orange-500" />Escalation conditions</h2>
              <RichText html={by.escalation.html} />
            </section>
          )}
          {after.map((s) => <Section key={s.key} s={s} />)}
          {by.policy_pending && (
            <section id="policy_pending" className="scroll-mt-20 callout callout-policy prose-byf">
              <p className="font-semibold">Policy pending approval — do not present these as Byfluence rules</p>
              <RichText html={by.policy_pending.html} />
              <p className="text-xs">Until management approves these, follow <Link to="/kb/pol-policy-pending-procedure">the policy-pending procedure</Link>: collect evidence, make no promises, escalate to Senior Support.</p>
            </section>
          )}
          {by.internal && (
            <section id="internal" className="scroll-mt-20 rounded-xl border border-dashed border-slate-300 dark:border-slate-600 surface-2 p-4">
              <h2 className="flex items-center gap-2 text-[15px] font-semibold mb-2"><Lock className="size-4 text-muted" />Internal notes <span className="text-xs font-normal text-muted">— employees only, never share with customers</span></h2>
              <RichText html={by.internal.html} />
            </section>
          )}
          {doc.tags.length > 0 && <div className="flex flex-wrap gap-1.5 pt-2">{doc.tags.map((t) => <Badge key={t} tone="gray">{t}</Badge>)}</div>}
        </article>

        <aside className="space-y-4 lg:sticky lg:top-20 self-start no-print">
          {toc.length > 2 && (
            <Card className="p-4 hidden lg:block">
              <div className="text-xs font-semibold uppercase tracking-wider text-muted mb-2">On this page</div>
              <ul className="space-y-1">{toc.map((t) => <li key={t.id}><a href={`#${t.id}`} className="text-[13px] text-muted hover:text-brand-600 block truncate">{t.label}</a></li>)}</ul>
            </Card>
          )}
          {isIssue && (
            <Card className="p-4 space-y-2.5 text-sm">
              <div className="text-xs font-semibold uppercase tracking-wider text-muted">Handling</div>
              <div className="flex items-center justify-between"><span className="text-muted flex items-center gap-1.5"><AlertTriangle className="size-3.5" />Suggested priority</span><PriorityBadge priority={doc.priority} /></div>
              {department && <div className="flex items-start justify-between gap-2"><span className="text-muted flex items-center gap-1.5 shrink-0"><Building2 className="size-3.5" />Escalate to</span><span className="text-right font-medium">{department.name}</span></div>}
              {sla && <div className="flex items-start justify-between gap-2"><span className="text-muted flex items-center gap-1.5 shrink-0"><Clock className="size-3.5" />Internal target</span><span className="text-right">{hours(sla.resolution_hours)} resolution<br /><span className="text-xs text-muted">{sla.first_response_minutes} min first reply</span></span></div>}
              <p className="text-[11px] text-muted">Targets are internal and configurable{settings?.sla?.approved ? '' : ' (not yet approved by management)'} — never quote them to customers.</p>
              <div className="flex items-center justify-between"><span className="text-muted flex items-center gap-1.5"><Users className="size-3.5" />Audience</span><span className="capitalize">{doc.audience}</span></div>
            </Card>
          )}
          {templates.length > 0 && (
            <Card className="p-4">
              <div className="text-xs font-semibold uppercase tracking-wider text-muted mb-2">Response templates</div>
              <ul className="space-y-1.5">{templates.map((t) => (
                <li key={t.slug}><Link to={`/templates/${t.slug}`} className="text-sm hover:text-brand-600 flex items-center gap-2"><MessageSquareText className="size-3.5 text-muted shrink-0" /><span className="truncate flex-1">{t.name}</span><span className="text-[10px] text-muted">{CHANNELS[t.channel]}</span></Link></li>
              ))}</ul>
            </Card>
          )}
          {(related.length > 0 || backlinks.length > 0) && (
            <Card className="p-4">
              <div className="text-xs font-semibold uppercase tracking-wider text-muted mb-2">Related articles</div>
              <ul className="space-y-1.5">
                {[...related, ...backlinks.filter((b) => !related.some((r) => r.slug === b.slug))].slice(0, 10).map((r) => (
                  <li key={r.slug}><Link to={r.type === 'faq' ? `/faqs?open=${r.slug}` : `/kb/${r.slug}`} className="text-sm hover:text-brand-600 line-clamp-2">{r.title}</Link></li>
                ))}
              </ul>
            </Card>
          )}
          {features.length > 0 && notLive.length === 0 && (
            <Card className="p-4 text-sm"><div className="flex items-center gap-2 text-emerald-600"><CheckCircle2 className="size-4" />All related features are live & verified</div></Card>
          )}
          <FeedbackBox slug={doc.slug} />
          <p className="text-[11px] text-muted px-1">{doc.views} views · 👍 {doc.helpful_yes} · 👎 {doc.helpful_no}{doc.ai_visible ? ' · Available to AI assistant' : ' · Hidden from AI assistant'}</p>
        </aside>
      </div>
      <NewTicketModal open={ticketOpen} onClose={() => setTicketOpen(false)} preset={preset}
        onCreated={(t) => { setTicketOpen(false); window.dispatchEvent(new Event('byf:refresh-counts')); navigate(`/tickets/${t.number}`); }} />
    </div>
  );
}
