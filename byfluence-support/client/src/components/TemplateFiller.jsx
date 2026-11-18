import { useEffect, useMemo, useState } from 'react';
import { AlertTriangle, Send, Ticket } from 'lucide-react';
import { api } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { CHANNELS, fillPlaceholders, placeholdersIn } from '../lib/format.js';
import { Button, CopyButton, Field, Input, Segmented, Select, useToast, cx, Badge } from './ui.jsx';

/** Renders text with {{placeholders}} highlighted (filled ones shown normally). */
function Preview({ text }) {
  const parts = (text || '').split(/({{\s*[a-z_]+\s*}})/g);
  return (
    <div className="whitespace-pre-wrap text-[14px] leading-relaxed font-[inherit]">
      {parts.map((p, i) => (/^{{/.test(p)
        ? <span key={i} className="rounded px-1 bg-amber-100 text-amber-900 dark:bg-amber-900/40 dark:text-amber-200 font-medium">{p}</span>
        : <span key={i}>{p}</span>))}
    </div>
  );
}

const ticketValues = (t, user) => t ? ({
  customer_name: t.customer_name, ticket_id: t.number, order_id: t.order_ref || '', consultation_id: t.consultation_ref || '',
  transaction_id: t.transaction_ref || '', support_agent: user.name,
}) : { support_agent: user.name };

/**
 * Fill placeholders and copy a template.
 * @param {object} props.template  {slug,name,channel,content_en,content_am,subject_en,subject_am}
 * @param {object} [props.ticket]  ticket to pre-fill from and log communication to
 */
export default function TemplateFiller({ template, ticket: fixedTicket, onLogged, compact }) {
  const { user, settings } = useAuth();
  const toast = useToast();
  const hasAm = !!template.content_am?.trim();
  const hasEn = !!template.content_en?.trim();
  const preferred = fixedTicket?.language || user.preferences?.language || 'am';
  const [lang, setLang] = useState(preferred === 'en' ? (hasEn ? 'en' : 'am') : (hasAm ? 'am' : 'en'));
  const [ticketList, setTicketList] = useState([]);
  const [ticketId, setTicketId] = useState(fixedTicket ? String(fixedTicket.id) : '');
  const [values, setValues] = useState({});
  const [copied, setCopied] = useState(false);
  const [logging, setLogging] = useState(false);

  const ticket = fixedTicket || ticketList.find((t) => String(t.id) === ticketId) || null;
  useEffect(() => { if (!fixedTicket) api('/tickets?view=mine&pageSize=50&status=new,open,under_review,waiting_customer,waiting_seller,escalated,in_progress,reopened').then((r) => setTicketList(r.tickets)).catch(() => {}); }, [fixedTicket]);
  useEffect(() => { setValues((v) => ({ ...ticketValues(ticket, user), ...Object.fromEntries(Object.entries(v).filter(([, x]) => x)) })); }, [ticket?.id]); // eslint-disable-line
  useEffect(() => { setCopied(false); }, [template.slug]);

  const body = lang === 'am' ? template.content_am : template.content_en;
  const subject = lang === 'am' ? template.subject_am : template.subject_en;
  const keys = useMemo(() => placeholdersIn(template.content_en, template.content_am, template.subject_en, template.subject_am), [template]);
  const labels = Object.fromEntries((settings?.placeholders || []).map((p) => [p.key, p.label]));
  const filled = fillPlaceholders(body, values);
  const filledSubject = subject ? fillPlaceholders(subject, values) : null;
  const missing = placeholdersIn(filled, filledSubject);
  const bracketed = /\[[^\]]{3,}\]/.test(filled);

  const logToTicket = async () => {
    if (!ticket) return;
    setLogging(true);
    try {
      await api(`/tickets/${ticket.id}/communications`, { method: 'POST', body: {
        direction: 'outbound', party: 'customer', channel: template.channel === 'any' ? ticket.channel : template.channel === 'chat' ? 'chat' : template.channel,
        summary: `Sent template “${template.name}” (${lang === 'am' ? 'Amharic' : 'English'}).`, template: template.slug,
      } });
      toast.success(`Logged on ${ticket.number}`);
      onLogged?.();
    } catch (e) { toast.error(e); } finally { setLogging(false); }
  };

  return (
    <div className={cx('grid gap-4', !compact && 'lg:grid-cols-[300px_1fr]')}>
      <div className="space-y-3">
        <div className="flex items-center justify-between gap-2">
          <Segmented value={lang} onChange={setLang} options={[{ value: 'am', label: 'አማርኛ' }, { value: 'en', label: 'English' }].filter((o) => (o.value === 'am' ? hasAm : hasEn))} />
          <Badge tone="gray">{CHANNELS[template.channel] || template.channel}</Badge>
        </div>
        {!fixedTicket && (
          <Field label="Fill from ticket" hint="Pre-fills customer name, ticket ID and references">
            <Select value={ticketId} onChange={(e) => setTicketId(e.target.value)}>
              <option value="">— none —</option>
              {ticketList.map((t) => <option key={t.id} value={t.id}>{t.number} · {t.customer_name}</option>)}
            </Select>
          </Field>
        )}
        {keys.length === 0 && <p className="text-xs text-muted">This template has no placeholders.</p>}
        {keys.map((k) => (
          <Field key={k} label={labels[k] || k.replace(/_/g, ' ')} hint={k === 'estimated_resolution_time' ? 'Only use wording approved in a published policy.' : undefined}>
            <Input value={values[k] || ''} onChange={(e) => setValues((v) => ({ ...v, [k]: e.target.value }))} placeholder={`{{${k}}}`} />
          </Field>
        ))}
      </div>
      <div className="min-w-0 space-y-3">
        {filledSubject && (
          <div className="rounded-lg border border-base surface-2 px-3 py-2 flex items-center gap-3">
            <span className="text-xs font-semibold text-muted shrink-0">Subject</span>
            <span className="text-sm flex-1 min-w-0 truncate">{filledSubject}</span>
            <CopyButton size="xs" text={filledSubject} label="Copy" />
          </div>
        )}
        <div className={cx('rounded-xl border border-base p-4 min-h-[180px]', lang === 'am' ? 'text-[15px]' : '')} lang={lang}>
          <Preview text={filled} />
        </div>
        {(missing.length > 0 || bracketed) && (
          <div className="flex items-start gap-2 text-xs text-amber-700 dark:text-amber-300">
            <AlertTriangle className="size-4 shrink-0" />
            <span>{missing.length > 0 && <>Fill in: {missing.map((m) => labels[m] || m).join(', ')}. </>}{bracketed && 'Replace the [bracketed] text before sending.'}</span>
          </div>
        )}
        <div className="flex flex-wrap items-center gap-2">
          <CopyButton variant="primary" size="md" text={filled} label="Copy message" copiedLabel="Copied — paste into the customer chat"
            onCopied={() => { setCopied(true); api(`/templates/${template.slug}/used`, { method: 'POST' }).catch(() => {}); }} />
          {ticket && (
            <Button icon={Send} loading={logging} variant={copied ? 'subtle' : 'secondary'} onClick={logToTicket} title="Records that you sent this message. Nothing is sent automatically.">
              I sent it — log on {ticket.number}
            </Button>
          )}
          {!ticket && !fixedTicket && <span className="text-xs text-muted inline-flex items-center gap-1"><Ticket className="size-3.5" />Pick a ticket to log the message on its timeline</span>}
        </div>
        <p className="text-[11px] text-muted">Messages are never sent automatically — copy, paste into {CHANNELS[template.channel] || 'the channel'}, then log it.</p>
      </div>
    </div>
  );
}
