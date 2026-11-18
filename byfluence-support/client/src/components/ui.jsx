import { createContext, forwardRef, useCallback, useContext, useEffect, useId, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import clsx from 'clsx';
import { AlertTriangle, Check, CheckCircle2, Copy, Info, Loader2, X, XCircle } from 'lucide-react';
import { STATUS, PRIORITY, DOC_STATUS, FEATURE_STATUS, initials } from '../lib/format.js';

export const cx = clsx;

// ---------- Buttons ----------
const BTN = {
  primary: 'bg-brand-500 text-white hover:bg-brand-600 active:bg-brand-700 shadow-sm',
  secondary: 'surface border border-base text-[var(--text)] hover:bg-[var(--surface-2)] shadow-xs',
  ghost: 'text-[var(--text)] hover:bg-[var(--surface-2)]',
  danger: 'bg-red-600 text-white hover:bg-red-700 shadow-sm',
  subtle: 'bg-brand-50 text-brand-700 hover:bg-brand-100 dark:bg-brand-900/40 dark:text-brand-200 dark:hover:bg-brand-900/60',
};
const SIZE = { xs: 'h-7 px-2 text-xs gap-1', sm: 'h-8 px-2.5 text-[13px] gap-1.5', md: 'h-9 px-3.5 text-sm gap-2', lg: 'h-10 px-4 text-sm gap-2' };

export const Button = forwardRef(function Button({ variant = 'secondary', size = 'md', icon: Icon, loading, className, children, ...p }, ref) {
  return (
    <button ref={ref} type="button" disabled={loading || p.disabled} {...p}
      className={cx('inline-flex items-center justify-center rounded-lg font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none whitespace-nowrap', BTN[variant], SIZE[size], className)}>
      {loading ? <Loader2 className="size-4 animate-spin" /> : Icon ? <Icon className={size === 'xs' ? 'size-3.5' : 'size-4'} /> : null}
      {children}
    </button>
  );
});

export function IconButton({ icon: Icon, label, className, size = 'md', ...p }) {
  return (
    <button type="button" aria-label={label} title={label} {...p}
      className={cx('inline-flex items-center justify-center rounded-lg text-muted hover:text-[var(--text)] hover:bg-[var(--surface-2)] transition-colors disabled:opacity-40', size === 'sm' ? 'size-7' : 'size-9', className)}>
      <Icon className={size === 'sm' ? 'size-4' : 'size-[18px]'} />
    </button>
  );
}

// ---------- Badges ----------
const TONES = {
  gray: 'bg-slate-100 text-slate-700 ring-slate-200 dark:bg-slate-800 dark:text-slate-300 dark:ring-slate-700',
  slate: 'bg-slate-200/70 text-slate-600 ring-slate-300 dark:bg-slate-800 dark:text-slate-400 dark:ring-slate-700',
  blue: 'bg-brand-50 text-brand-700 ring-brand-200 dark:bg-brand-900/40 dark:text-brand-200 dark:ring-brand-800',
  sky: 'bg-sky-50 text-sky-700 ring-sky-200 dark:bg-sky-900/30 dark:text-sky-300 dark:ring-sky-800',
  indigo: 'bg-indigo-50 text-indigo-700 ring-indigo-200 dark:bg-indigo-900/30 dark:text-indigo-300 dark:ring-indigo-800',
  violet: 'bg-violet-50 text-violet-700 ring-violet-200 dark:bg-violet-900/30 dark:text-violet-300 dark:ring-violet-800',
  green: 'bg-emerald-50 text-emerald-700 ring-emerald-200 dark:bg-emerald-900/30 dark:text-emerald-300 dark:ring-emerald-800',
  amber: 'bg-amber-50 text-amber-800 ring-amber-200 dark:bg-amber-900/30 dark:text-amber-300 dark:ring-amber-800',
  orange: 'bg-orange-50 text-orange-700 ring-orange-200 dark:bg-orange-900/30 dark:text-orange-300 dark:ring-orange-800',
  red: 'bg-red-50 text-red-700 ring-red-200 dark:bg-red-900/30 dark:text-red-300 dark:ring-red-800',
  pink: 'bg-pink-50 text-pink-700 ring-pink-200 dark:bg-pink-900/30 dark:text-pink-300 dark:ring-pink-800',
};
export function Badge({ tone = 'gray', className, children, dot, ...p }) {
  return (
    <span {...p} className={cx('inline-flex items-center gap-1 rounded-md px-1.5 py-0.5 text-[11.5px] font-medium ring-1 ring-inset whitespace-nowrap', TONES[tone], className)}>
      {dot && <span className="size-1.5 rounded-full bg-current opacity-80" />}
      {children}
    </span>
  );
}
export const StatusBadge = ({ status }) => <Badge tone={STATUS[status]?.tone} dot>{STATUS[status]?.label || status}</Badge>;
export const PriorityBadge = ({ priority }) => <Badge tone={PRIORITY[priority]?.tone}>{PRIORITY[priority]?.label || priority}</Badge>;
export const DocStatusBadge = ({ status }) => <Badge tone={DOC_STATUS[status]?.tone}>{DOC_STATUS[status]?.label || status}</Badge>;
export const FeatureBadge = ({ status, verified }) => (
  <Badge tone={FEATURE_STATUS[status]?.tone}>{FEATURE_STATUS[status]?.label || status}{status === 'live' && verified === false ? ' (unverified)' : ''}</Badge>
);

// ---------- Layout bits ----------
export function Card({ className, children, ...p }) {
  return <div {...p} className={cx('surface rounded-xl border border-base shadow-[0_1px_2px_rgba(16,24,40,0.04)]', className)}>{children}</div>;
}
export function CardHeader({ title, subtitle, icon: Icon, actions, className }) {
  return (
    <div className={cx('flex items-start justify-between gap-3 px-4 pt-4 pb-3', className)}>
      <div className="flex items-start gap-2.5 min-w-0">
        {Icon && <Icon className="size-[18px] text-brand-500 mt-0.5 shrink-0" />}
        <div className="min-w-0">
          <h3 className="font-semibold text-[15px] leading-tight">{title}</h3>
          {subtitle && <p className="text-xs text-muted mt-0.5">{subtitle}</p>}
        </div>
      </div>
      {actions && <div className="flex items-center gap-1.5 shrink-0">{actions}</div>}
    </div>
  );
}

export function PageHeader({ title, subtitle, actions, icon: Icon, breadcrumb }) {
  return (
    <div className="mb-5">
      {breadcrumb && <div className="text-xs text-muted mb-1.5 flex items-center gap-1 flex-wrap">{breadcrumb}</div>}
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="flex items-start gap-3 min-w-0">
          {Icon && <div className="size-10 rounded-xl bg-brand-50 text-brand-600 dark:bg-brand-900/40 dark:text-brand-300 grid place-items-center shrink-0"><Icon className="size-5" /></div>}
          <div className="min-w-0">
            <h1 className="text-[22px] font-semibold tracking-tight leading-tight">{title}</h1>
            {subtitle && <p className="text-sm text-muted mt-1 max-w-3xl">{subtitle}</p>}
          </div>
        </div>
        {actions && <div className="flex flex-wrap items-center gap-2">{actions}</div>}
      </div>
    </div>
  );
}

export function Spinner({ className }) { return <Loader2 className={cx('size-5 animate-spin text-brand-500', className)} />; }

export function Loading({ label = 'Loading…', className }) {
  return <div className={cx('flex items-center justify-center gap-2 py-16 text-sm text-muted', className)}><Spinner />{label}</div>;
}

export function Skeleton({ className }) { return <div className={cx('animate-pulse rounded-md bg-[var(--surface-2)]', className)} />; }

export function ErrorState({ error, onRetry }) {
  return (
    <div className="flex flex-col items-center justify-center text-center py-14 px-4">
      <XCircle className="size-9 text-red-500 mb-2" />
      <p className="font-medium">{error?.status === 403 ? 'You don’t have access to this' : error?.status === 404 ? 'Not found' : 'Something went wrong'}</p>
      <p className="text-sm text-muted mt-1 max-w-md">{error?.message}</p>
      {onRetry && error?.status !== 403 && error?.status !== 404 && <Button className="mt-4" size="sm" onClick={() => onRetry()}>Try again</Button>}
    </div>
  );
}

export function EmptyState({ icon: Icon = Info, title, children, action }) {
  return (
    <div className="flex flex-col items-center justify-center text-center py-12 px-4">
      <div className="size-11 rounded-full bg-[var(--surface-2)] grid place-items-center mb-3"><Icon className="size-5 text-muted" /></div>
      <p className="font-medium">{title}</p>
      {children && <div className="text-sm text-muted mt-1 max-w-md">{children}</div>}
      {action && <div className="mt-4">{action}</div>}
    </div>
  );
}

export function Avatar({ name, size = 'md', className }) {
  const s = size === 'sm' ? 'size-6 text-[10px]' : size === 'lg' ? 'size-10 text-sm' : 'size-8 text-xs';
  const hue = [...(name || '')].reduce((a, c) => a + c.charCodeAt(0), 0) % 360;
  return (
    <span className={cx('inline-grid place-items-center rounded-full font-semibold text-white shrink-0', s, className)} style={{ background: `hsl(${hue} 55% 48%)` }} title={name}>
      {initials(name) || '?'}
    </span>
  );
}

// ---------- Form controls ----------
const widthOf = (c) => (/(^|\s)(w-|min-w-|flex-1)/.test(c || '') ? '' : 'w-full');
const inputCls = 'rounded-lg border border-base surface px-3 text-sm placeholder:text-[var(--muted)]/70 focus:border-brand-400 focus:ring-2 focus:ring-brand-500/20 outline-none transition disabled:opacity-60';
export const Input = forwardRef(function Input({ className, ...p }, ref) {
  return <input ref={ref} {...p} className={cx(inputCls, widthOf(className), 'h-9', className)} />;
});
export const Textarea = forwardRef(function Textarea({ className, rows = 3, ...p }, ref) {
  return <textarea ref={ref} rows={rows} {...p} className={cx(inputCls, widthOf(className), 'py-2 leading-relaxed', className)} />;
});
export const Select = forwardRef(function Select({ className, children, ...p }, ref) {
  return <select ref={ref} {...p} className={cx(inputCls, widthOf(className), 'h-9 pr-8 appearance-none bg-[url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 20 20%27 fill=%27%2394a3b8%27%3E%3Cpath d=%27M5.5 7.5 10 12l4.5-4.5%27 stroke=%27%2394a3b8%27 stroke-width=%271.5%27 fill=%27none%27/%3E%3C/svg%3E")] bg-[length:18px] bg-[right_8px_center] bg-no-repeat', className)}>{children}</select>;
});

export function Field({ label, hint, error, required, children, className }) {
  const id = useId();
  const child = children && typeof children === 'object' && !Array.isArray(children) ? { ...children, props: { id, ...children.props } } : children;
  return (
    <div className={className}>
      {label && <label htmlFor={id} className="block text-[13px] font-medium mb-1.5">{label}{required && <span className="text-red-500 ml-0.5">*</span>}</label>}
      {child}
      {error ? <p className="text-xs text-red-600 mt-1">{error}</p> : hint ? <p className="text-xs text-muted mt-1">{hint}</p> : null}
    </div>
  );
}

export function Checkbox({ label, checked, onChange, description, disabled }) {
  return (
    <label className={cx('flex items-start gap-2.5 text-sm cursor-pointer select-none', disabled && 'opacity-60 pointer-events-none')}>
      <input type="checkbox" className="mt-0.5 size-4 accent-brand-500 rounded" checked={!!checked} onChange={(e) => onChange(e.target.checked)} disabled={disabled} />
      <span><span className="font-medium">{label}</span>{description && <span className="block text-xs text-muted mt-0.5">{description}</span>}</span>
    </label>
  );
}

export function Segmented({ value, onChange, options, size = 'sm', className }) {
  return (
    <div className={cx('inline-flex rounded-lg surface-2 p-0.5 border border-base', className)} role="tablist">
      {options.map((o) => {
        const v = typeof o === 'string' ? o : o.value;
        const l = typeof o === 'string' ? o : o.label;
        const Icon = o.icon;
        return (
          <button key={v} type="button" role="tab" aria-selected={value === v} onClick={() => onChange(v)}
            className={cx('inline-flex items-center gap-1.5 rounded-md font-medium transition-colors', size === 'xs' ? 'px-2 h-6 text-xs' : 'px-2.5 h-7 text-[13px]',
              value === v ? 'surface shadow-sm text-[var(--text)]' : 'text-muted hover:text-[var(--text)]')}>
            {Icon && <Icon className="size-3.5" />}{l}
          </button>
        );
      })}
    </div>
  );
}

export function Tabs({ tabs, value, onChange, className }) {
  return (
    <div className={cx('flex gap-1 border-b border-base overflow-x-auto', className)} role="tablist">
      {tabs.map((t) => (
        <button key={t.value} type="button" role="tab" aria-selected={value === t.value} onClick={() => onChange(t.value)}
          className={cx('relative inline-flex items-center gap-1.5 px-3 h-9 text-[13px] font-medium whitespace-nowrap transition-colors',
            value === t.value ? 'text-brand-600 dark:text-brand-300' : 'text-muted hover:text-[var(--text)]')}>
          {t.icon && <t.icon className="size-4" />}
          {t.label}
          {t.count != null && <span className={cx('rounded-full px-1.5 text-[11px] tabular-nums', value === t.value ? 'bg-brand-100 text-brand-700 dark:bg-brand-900/50 dark:text-brand-200' : 'surface-2')}>{t.count}</span>}
          {value === t.value && <span className="absolute inset-x-2 -bottom-px h-0.5 rounded-full bg-brand-500" />}
        </button>
      ))}
    </div>
  );
}

// ---------- Modal ----------
export function Modal({ open, onClose, title, subtitle, children, footer, size = 'md', dismissable = true }) {
  const ref = useRef(null);
  useEffect(() => {
    if (!open) return;
    const prev = document.activeElement;
    const onKey = (e) => { if (e.key === 'Escape' && dismissable) onClose?.(); };
    document.addEventListener('keydown', onKey);
    document.body.style.overflow = 'hidden';
    setTimeout(() => ref.current?.querySelector('input,textarea,select,button[data-autofocus]')?.focus(), 30);
    return () => { document.removeEventListener('keydown', onKey); document.body.style.overflow = ''; prev?.focus?.(); };
  }, [open, onClose, dismissable]);
  if (!open) return null;
  const w = { sm: 'max-w-md', md: 'max-w-xl', lg: 'max-w-3xl', xl: 'max-w-5xl' }[size];
  return createPortal(
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4">
      <div className="absolute inset-0 bg-slate-900/45 backdrop-blur-[1px]" onClick={() => dismissable && onClose?.()} />
      <div ref={ref} role="dialog" aria-modal="true" aria-label={title}
        className={cx('relative surface w-full rounded-t-2xl sm:rounded-2xl border border-base shadow-2xl animate-in flex flex-col max-h-[92vh]', w)}>
        <div className="flex items-start justify-between gap-3 px-5 pt-4 pb-3 border-b border-base">
          <div>
            <h2 className="font-semibold text-base">{title}</h2>
            {subtitle && <p className="text-xs text-muted mt-0.5">{subtitle}</p>}
          </div>
          {dismissable && <IconButton icon={X} label="Close" size="sm" onClick={onClose} />}
        </div>
        <div className="px-5 py-4 overflow-y-auto">{children}</div>
        {footer && <div className="flex flex-wrap justify-end gap-2 px-5 py-3 border-t border-base surface-2 rounded-b-2xl">{footer}</div>}
      </div>
    </div>,
    document.body,
  );
}

// ---------- Confirm dialog (promise based) ----------
const ConfirmCtx = createContext(null);
export function ConfirmProvider({ children }) {
  const [state, setState] = useState(null);
  const [typed, setTyped] = useState('');
  const confirm = useCallback((opts) => new Promise((resolve) => { setTyped(''); setState({ ...opts, resolve }); }), []);
  const close = (v) => { state?.resolve(v); setState(null); };
  return (
    <ConfirmCtx.Provider value={confirm}>
      {children}
      <Modal open={!!state} onClose={() => close(false)} title={state?.title || 'Are you sure?'} size="sm"
        footer={<>
          <Button onClick={() => close(false)}>Cancel</Button>
          <Button variant={state?.danger ? 'danger' : 'primary'} data-autofocus disabled={state?.typeToConfirm && typed !== state.typeToConfirm} onClick={() => close(true)}>{state?.confirmLabel || 'Confirm'}</Button>
        </>}>
        <div className="flex gap-3">
          {state?.danger && <AlertTriangle className="size-5 text-red-500 shrink-0 mt-0.5" />}
          <div className="text-sm text-muted space-y-3">
            <div>{state?.message}</div>
            {state?.typeToConfirm && (
              <Field label={<>Type <code className="font-mono text-[var(--text)]">{state.typeToConfirm}</code> to confirm</>}>
                <Input value={typed} onChange={(e) => setTyped(e.target.value)} />
              </Field>
            )}
          </div>
        </div>
      </Modal>
    </ConfirmCtx.Provider>
  );
}
export const useConfirm = () => useContext(ConfirmCtx);

// ---------- Toasts ----------
const ToastCtx = createContext(null);
export function ToastProvider({ children }) {
  const [items, setItems] = useState([]);
  const push = useCallback((msg, type = 'success') => {
    const id = Math.random().toString(36).slice(2);
    setItems((x) => [...x.slice(-3), { id, msg, type }]);
    setTimeout(() => setItems((x) => x.filter((i) => i.id !== id)), type === 'error' ? 6000 : 3200);
  }, []);
  const api = useRef(null);
  api.current = { success: (m) => push(m, 'success'), error: (m) => push(m?.message || m, 'error'), info: (m) => push(m, 'info') };
  return (
    <ToastCtx.Provider value={api.current}>
      {children}
      {createPortal(
        <div className="fixed z-[60] bottom-4 right-4 left-4 sm:left-auto flex flex-col gap-2 items-end pointer-events-none" aria-live="polite">
          {items.map((t) => (
            <div key={t.id} className="pointer-events-auto animate-in flex items-start gap-2.5 rounded-xl border border-base surface shadow-lg px-3.5 py-2.5 text-sm max-w-sm">
              {t.type === 'error' ? <XCircle className="size-4 text-red-500 mt-0.5 shrink-0" /> : t.type === 'info' ? <Info className="size-4 text-brand-500 mt-0.5 shrink-0" /> : <CheckCircle2 className="size-4 text-emerald-500 mt-0.5 shrink-0" />}
              <span>{t.msg}</span>
            </div>
          ))}
        </div>,
        document.body,
      )}
    </ToastCtx.Provider>
  );
}
export const useToast = () => useContext(ToastCtx);

// ---------- Copy ----------
export async function copyText(text) {
  try { await navigator.clipboard.writeText(text); return true; } catch {
    const ta = document.createElement('textarea');
    ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    const ok = document.execCommand('copy');
    ta.remove();
    return ok;
  }
}
export function CopyButton({ text, getText, label = 'Copy', copiedLabel = 'Copied', size = 'sm', variant = 'secondary', onCopied, className }) {
  const [done, setDone] = useState(false);
  const toast = useToast();
  return (
    <Button size={size} variant={done ? 'subtle' : variant} icon={done ? Check : Copy} className={className}
      onClick={async () => {
        const t = getText ? getText() : text;
        if (await copyText(t)) { setDone(true); onCopied?.(); setTimeout(() => setDone(false), 1800); } else toast.error('Copy failed — select the text and copy manually.');
      }}>
      {done ? copiedLabel : label}
    </Button>
  );
}

// ---------- Menu ----------
export function Menu({ trigger, children, align = 'right', className }) {
  const [open, setOpen] = useState(false);
  const ref = useRef(null);
  useEffect(() => {
    if (!open) return;
    const h = (e) => { if (!ref.current?.contains(e.target)) setOpen(false); };
    const k = (e) => e.key === 'Escape' && setOpen(false);
    document.addEventListener('mousedown', h);
    document.addEventListener('keydown', k);
    return () => { document.removeEventListener('mousedown', h); document.removeEventListener('keydown', k); };
  }, [open]);
  return (
    <div ref={ref} className={cx('relative', className)}>
      {trigger({ open, toggle: () => setOpen((o) => !o) })}
      {open && (
        <div className={cx('absolute z-40 mt-1.5 min-w-[200px] rounded-xl border border-base surface shadow-xl p-1 animate-in', align === 'right' ? 'right-0' : 'left-0')} onClick={() => setOpen(false)}>
          {children}
        </div>
      )}
    </div>
  );
}
export function MenuItem({ icon: Icon, children, danger, ...p }) {
  return (
    <button type="button" {...p} className={cx('w-full flex items-center gap-2.5 rounded-lg px-2.5 py-1.5 text-sm text-left hover:bg-[var(--surface-2)] disabled:opacity-50', danger && 'text-red-600')}>
      {Icon && <Icon className="size-4 text-muted" />}{children}
    </button>
  );
}

export function Stat({ label, value, hint, tone, icon: Icon, onClick, active }) {
  const toneCls = { red: 'text-red-600 dark:text-red-400', amber: 'text-amber-600 dark:text-amber-400', green: 'text-emerald-600 dark:text-emerald-400', brand: 'text-brand-600 dark:text-brand-300' }[tone] || '';
  const Comp = onClick ? 'button' : 'div';
  return (
    <Comp onClick={onClick} className={cx('surface rounded-xl border border-base px-3.5 py-3 text-left transition', onClick && 'hover:border-brand-300 hover:shadow-sm', active && 'ring-2 ring-brand-500/40')}>
      <div className="flex items-start justify-between gap-2">
        <span className="text-xs font-medium text-muted leading-tight line-clamp-2">{label}</span>
        {Icon && <Icon className="size-4 text-muted shrink-0" />}
      </div>
      <div className={cx('mt-1 text-[22px] font-semibold tabular-nums tracking-tight', toneCls)}>{value ?? '—'}</div>
      {hint && <div className="text-[11px] text-muted mt-0.5 truncate">{hint}</div>}
    </Comp>
  );
}

export function Callout({ tone = 'note', title, children, className }) {
  return (
    <div className={cx('callout prose-byf', `callout-${tone}`, className)}>
      {title && <p className="font-semibold">{title}</p>}
      <div className="text-sm">{children}</div>
    </div>
  );
}
