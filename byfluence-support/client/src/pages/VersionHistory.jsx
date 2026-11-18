import { useMemo, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { History, RotateCcw } from 'lucide-react';
import { api, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { dateTime, relTime } from '../lib/format.js';
import { Badge, Button, Card, ErrorState, Loading, PageHeader, Segmented, useConfirm, useToast, cx } from '../components/ui.jsx';
import RichText, { htmlToPlain } from '../components/RichText.jsx';

/** Simple line diff (LCS) for comparing two versions as plain text. */
function diffLines(a, b) {
  const A = a.split('\n');
  const B = b.split('\n');
  const n = A.length;
  const m = B.length;
  if (n * m > 400000) return [...A.map((l) => ['-', l]), ...B.map((l) => ['+', l])];
  const dp = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--) dp[i][j] = A[i] === B[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  const out = [];
  let i = 0;
  let j = 0;
  while (i < n && j < m) {
    if (A[i] === B[j]) { out.push([' ', A[i]]); i++; j++; } else if (dp[i + 1][j] >= dp[i][j + 1]) out.push(['-', A[i++]]); else out.push(['+', B[j++]]);
  }
  while (i < n) out.push(['-', A[i++]]);
  while (j < m) out.push(['+', B[j++]]);
  return out;
}

const docText = (s) => (s ? [`# ${s.title}`, s.summary, ...(s.sections || []).flatMap((x) => [`## ${x.label}`, htmlToPlain(x.html)])].join('\n') : '');
const tplText = (s) => (s ? [`# ${s.name}`, `[${s.channel} · ${s.style}]`, s.subject_en && `Subject (EN): ${s.subject_en}`, '## English', s.content_en, s.subject_am && `Subject (AM): ${s.subject_am}`, '## Amharic', s.content_am].filter(Boolean).join('\n') : '');

export default function VersionHistory() {
  const { kind, slug } = useParams();
  const { can } = useAuth();
  const toast = useToast();
  const confirm = useConfirm();
  const base = kind === 'template' ? 'templates' : 'docs';
  const { data, loading, error, reload } = useApi(`/${base}/${slug}/versions`, [slug]);
  const [sel, setSel] = useState(0);
  const [mode, setMode] = useState('diff');
  const toText = kind === 'template' ? tplText : docText;
  const diff = useMemo(() => {
    if (!data || !data[sel]) return [];
    const prev = data[sel + 1];
    return diffLines(toText(prev?.snapshot), toText(data[sel].snapshot)).filter(([op], i, arr) => op !== ' ' || arr[i - 1]?.[0] !== ' ' || arr[i + 1]?.[0] !== ' ');
  }, [data, sel, toText]);
  if (loading && !data) return <Loading />;
  if (error) return <ErrorState error={error} onRetry={reload} />;
  const v = data[sel];
  const restore = async () => {
    if (!(await confirm({ title: `Restore version ${v.version}?`, message: 'A new version will be created with this content. Nothing is lost — the current version stays in history.', confirmLabel: 'Restore' }))) return;
    try { await api(`/${base}/${slug}/restore/${v.id}`, { method: 'POST' }); toast.success('Version restored'); reload(); setSel(0); } catch (e) { toast.error(e); }
  };
  return (
    <div className="max-w-6xl mx-auto">
      <PageHeader icon={History} title="Version history" subtitle={<>{kind === 'template' ? 'Template' : 'Document'} <span className="font-mono">{slug}</span> · {data.length} versions</>}
        breadcrumb={<Link to={kind === 'template' ? `/templates/${slug}` : `/kb/${slug}`} className="hover:text-brand-600">← Back</Link>} />
      <div className="grid lg:grid-cols-[300px_1fr] gap-5">
        <Card className="max-h-[75vh] overflow-y-auto">
          {data.map((x, i) => (
            <button key={x.id} type="button" onClick={() => setSel(i)} className={cx('w-full text-left px-4 py-3 border-b border-base last:border-b-0', i === sel ? 'bg-brand-50 dark:bg-brand-900/30' : 'hover:bg-[var(--surface-2)]')}>
              <div className="flex items-center justify-between"><span className="font-semibold text-sm">v{x.version}</span>{i === 0 && <Badge tone="green">Current</Badge>}</div>
              <div className="text-[13px] mt-0.5 line-clamp-2">{x.change_summary || '—'}</div>
              <div className="text-[11px] text-muted mt-1">{x.user_name} · {relTime(x.created_at)}</div>
            </button>
          ))}
        </Card>
        <div className="min-w-0 space-y-3">
          <div className="flex flex-wrap items-center justify-between gap-2">
            <div className="text-sm"><strong>Version {v.version}</strong> · {dateTime(v.created_at)} · {v.user_name}</div>
            <div className="flex gap-2">
              <Segmented value={mode} onChange={setMode} options={[{ value: 'diff', label: 'Changes' }, { value: 'full', label: 'Full content' }]} />
              {sel > 0 && (kind === 'template' ? can('templates.edit') : can('docs.edit')) && <Button icon={RotateCcw} variant="primary" onClick={restore}>Restore this version</Button>}
            </div>
          </div>
          {mode === 'diff' ? (
            <Card className="p-0 overflow-hidden">
              <div className="px-4 py-2 text-xs text-muted border-b border-base surface-2">{data[sel + 1] ? `Compared with v${data[sel + 1].version}` : 'First version'} · <span className="text-emerald-600">+ added</span> · <span className="text-red-600">− removed</span></div>
              <pre className="text-[12.5px] leading-relaxed overflow-x-auto max-h-[70vh] p-0 m-0 font-mono">
                {diff.length === 0 ? <div className="p-4 text-muted">No text changes (metadata or status only).</div> : diff.map(([op, line], i) => (
                  <div key={i} className={cx('px-4 whitespace-pre-wrap', op === '+' && 'bg-emerald-50 text-emerald-900 dark:bg-emerald-950/40 dark:text-emerald-200', op === '-' && 'bg-red-50 text-red-900 line-through decoration-red-300 dark:bg-red-950/40 dark:text-red-200')}>
                    <span className="select-none opacity-50 mr-2">{op === ' ' ? ' ' : op === '+' ? '+' : '−'}</span>{line || ' '}
                  </div>
                ))}
              </pre>
            </Card>
          ) : (
            <Card className="p-5 space-y-5">
              {kind === 'template' ? <pre className="whitespace-pre-wrap text-sm font-[inherit]">{tplText(v.snapshot)}</pre> : (<>
                <h2 className="text-lg font-semibold">{v.snapshot.title}</h2>
                <p className="text-muted">{v.snapshot.summary}</p>
                {(v.snapshot.sections || []).map((s) => <section key={s.key}><h3 className="font-semibold mb-1.5">{s.label}</h3><RichText html={s.html} /></section>)}
              </>)}
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}
