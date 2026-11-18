import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { ArrowLeft, ArrowRight, CheckCircle2, Clock, Target, XCircle, Pencil, Plus, Trash2, Award } from 'lucide-react';
import { api, useApi } from '../lib/api.js';
import { useAuth } from '../lib/auth.jsx';
import { Badge, Button, Callout, Card, ErrorState, Field, Input, Loading, Textarea, useToast, cx } from '../components/ui.jsx';
import RichText from '../components/RichText.jsx';
import Editor from '../components/Editor.jsx';

function ModuleEditor({ slug, onDone }) {
  const toast = useToast();
  const { data } = useApi(`/training/${slug}?edit=1`, [slug]);
  const [m, setM] = useState(null);
  const [busy, setBusy] = useState(false);
  useEffect(() => { if (data) setM({ ...data.module, objectivesText: data.module.objectives.join('\n'), change_summary: '' }); }, [data]);
  if (!m) return <Loading />;
  const save = async () => {
    setBusy(true);
    try {
      await api(`/training/${slug}`, { method: 'PUT', body: { title: m.title, duration: m.duration, status: m.status, objectives: m.objectivesText.split('\n').map((x) => x.trim()).filter(Boolean), sections: m.sections, quiz: m.quiz, change_summary: m.change_summary } });
      toast.success('Module saved'); onDone();
    } catch (e) { toast.error(e); } finally { setBusy(false); }
  };
  const setQ = (i, patch) => setM({ ...m, quiz: m.quiz.map((q, j) => (j === i ? { ...q, ...patch } : q)) });
  return (
    <div className="space-y-5">
      <div className="grid sm:grid-cols-[1fr_120px_160px] gap-3">
        <Field label="Title"><Input value={m.title} onChange={(e) => setM({ ...m, title: e.target.value })} /></Field>
        <Field label="Minutes"><Input type="number" value={m.duration || ''} onChange={(e) => setM({ ...m, duration: Number(e.target.value) })} /></Field>
        <Field label="Status"><select className="h-9 w-full rounded-lg border border-base surface px-2 text-sm" value={m.status} onChange={(e) => setM({ ...m, status: e.target.value })}><option value="published">Published</option><option value="draft">Draft</option><option value="archived">Archived</option></select></Field>
      </div>
      <Field label="Learning objectives (one per line)"><Textarea rows={5} value={m.objectivesText} onChange={(e) => setM({ ...m, objectivesText: e.target.value })} /></Field>
      {m.sections.map((s, i) => (
        <Field key={s.key + i} label={<span className="flex items-center gap-2"><Input className="h-7 w-64" value={s.label} onChange={(e) => setM({ ...m, sections: m.sections.map((x, j) => (j === i ? { ...x, label: e.target.value } : x)) })} /></span>}>
          <Editor value={s.html} onChange={(html) => setM((mm) => ({ ...mm, sections: mm.sections.map((x, j) => (j === i ? { ...x, html } : x)) }))} />
        </Field>
      ))}
      <Card className="p-4 space-y-4">
        <div className="flex items-center justify-between"><h3 className="font-semibold">Knowledge check ({m.quiz.length})</h3><Button size="sm" icon={Plus} onClick={() => setM({ ...m, quiz: [...m.quiz, { question: '', options: ['', ''], answer: 0, explanation: '' }] })}>Add question</Button></div>
        {m.quiz.map((q, i) => (
          <div key={i} className="rounded-lg border border-base p-3 space-y-2">
            <div className="flex gap-2"><Input value={q.question} placeholder={`Question ${i + 1}`} onChange={(e) => setQ(i, { question: e.target.value })} /><Button size="sm" variant="ghost" icon={Trash2} onClick={() => setM({ ...m, quiz: m.quiz.filter((_, j) => j !== i) })} /></div>
            {q.options.map((o, k) => (
              <div key={k} className="flex items-center gap-2 pl-2">
                <input type="radio" className="accent-brand-500" checked={q.answer === k} onChange={() => setQ(i, { answer: k })} title="Correct answer" />
                <Input className="h-8" value={o} onChange={(e) => setQ(i, { options: q.options.map((x, j) => (j === k ? e.target.value : x)) })} />
                {q.options.length > 2 && <button type="button" onClick={() => setQ(i, { options: q.options.filter((_, j) => j !== k), answer: q.answer >= k && q.answer > 0 ? q.answer - 1 : q.answer })}><Trash2 className="size-3.5 text-muted" /></button>}
              </div>
            ))}
            <div className="flex gap-2 pl-2"><Button size="xs" onClick={() => setQ(i, { options: [...q.options, ''] })}>+ Option</Button></div>
            <Input className="h-8" placeholder="Explanation shown after answering" value={q.explanation} onChange={(e) => setQ(i, { explanation: e.target.value })} />
          </div>
        ))}
      </Card>
      <div className="flex flex-wrap items-end gap-3">
        <Field label="Change summary" className="flex-1"><Input value={m.change_summary} onChange={(e) => setM({ ...m, change_summary: e.target.value })} placeholder="What changed?" /></Field>
        <Button onClick={onDone}>Cancel</Button><Button variant="primary" loading={busy} onClick={save}>Save module</Button>
      </div>
    </div>
  );
}

export default function TrainingModule() {
  const { slug } = useParams();
  const { can } = useAuth();
  const toast = useToast();
  const { data, loading, error, reload } = useApi(`/training/${slug}`, [slug]);
  const [answers, setAnswers] = useState([]);
  const [result, setResult] = useState(null);
  const [busy, setBusy] = useState(false);
  const [editing, setEditing] = useState(false);
  useEffect(() => { setAnswers([]); setResult(null); setEditing(false); api(`/training/${slug}/start`, { method: 'POST' }).catch(() => {}); }, [slug]);
  if (loading && !data) return <Loading />;
  if (error) return <ErrorState error={error} onRetry={reload} />;
  const { module: m, progress, prev, next, pass_score: pass } = data;
  if (editing) return <div className="max-w-4xl"><h1 className="text-xl font-semibold mb-4">Edit module {m.number}</h1><ModuleEditor slug={slug} onDone={() => { setEditing(false); reload(); }} /></div>;
  const submit = async () => {
    setBusy(true);
    try { const r = await api(`/training/${slug}/submit`, { method: 'POST', body: { answers } }); setResult(r); if (r.passed) toast.success(`Passed with ${r.score}%`); reload(true); } catch (e) { toast.error(e); } finally { setBusy(false); }
  };

  return (
    <div className="max-w-4xl mx-auto">
      <Link to="/training" className="text-xs text-muted hover:text-brand-600 inline-flex items-center gap-1 mb-2"><ArrowLeft className="size-3" />Training Center</Link>
      <div className="flex flex-wrap items-start justify-between gap-3 mb-5">
        <div>
          <div className="flex items-center gap-2 mb-1"><Badge tone="blue">Module {m.number}</Badge>{m.duration && <span className="text-xs text-muted flex items-center gap-1"><Clock className="size-3" />{m.duration} min</span>}
            {progress?.status === 'completed' && <Badge tone="green"><Award className="size-3" />Completed · {progress.best_score}%</Badge>}</div>
          <h1 className="text-2xl font-semibold tracking-tight">{m.title}</h1>
        </div>
        {can('training.edit') && <Button icon={Pencil} onClick={() => setEditing(true)}>Edit module</Button>}
      </div>
      <Card className="p-5 mb-6">
        <h2 className="font-semibold flex items-center gap-2 mb-2"><Target className="size-4 text-brand-500" />Learning objectives</h2>
        <ul className="space-y-1.5 text-sm">{m.objectives.map((o) => <li key={o} className="flex gap-2"><CheckCircle2 className="size-4 text-emerald-500 shrink-0 mt-0.5" />{o}</li>)}</ul>
      </Card>
      <div className="space-y-8">
        {m.sections.map((s) => (
          <section key={s.key}>
            <h2 className="text-lg font-semibold mb-3 pb-2 border-b border-base">{s.label}</h2>
            <RichText html={s.html} interactive />
          </section>
        ))}
      </div>
      <Card className="p-5 mt-8" id="quiz">
        <h2 className="text-lg font-semibold">Knowledge check</h2>
        <p className="text-sm text-muted mb-4">{m.quiz.length} questions · pass mark {pass}%{progress?.attempts ? ` · ${progress.attempts} previous attempt(s)` : ''}</p>
        <ol className="space-y-5">
          {m.quiz.map((q, i) => {
            const r = result?.results[i];
            return (
              <li key={i}>
                <div className="font-medium text-sm mb-2">{i + 1}. {q.question}</div>
                <div className="space-y-1.5">
                  {q.options.map((o, k) => {
                    const chosen = answers[i] === k;
                    const showCorrect = r && r.answer === k;
                    const showWrong = r && chosen && !r.correct;
                    return (
                      <label key={k} className={cx('flex items-start gap-2.5 rounded-lg border px-3 py-2 text-sm cursor-pointer', showCorrect ? 'border-emerald-400 bg-emerald-50 dark:bg-emerald-950/30' : showWrong ? 'border-red-400 bg-red-50 dark:bg-red-950/30' : chosen ? 'border-brand-400 bg-brand-50/60 dark:bg-brand-900/20' : 'border-base hover:border-brand-200')}>
                        <input type="radio" name={`q${i}`} className="mt-0.5 accent-brand-500" checked={chosen} disabled={!!result} onChange={() => { const a = [...answers]; a[i] = k; setAnswers(a); }} />
                        <span className="flex-1">{o}</span>
                        {showCorrect && <CheckCircle2 className="size-4 text-emerald-600" />}{showWrong && <XCircle className="size-4 text-red-600" />}
                      </label>
                    );
                  })}
                </div>
                {r?.explanation && <p className="text-xs text-muted mt-1.5 pl-1">{r.explanation}</p>}
              </li>
            );
          })}
        </ol>
        {result && <Callout tone={result.passed ? 'tip' : 'warning'} className="mt-5" title={result.passed ? `Passed — ${result.score}%` : `Score ${result.score}% — pass mark is ${result.pass_score}%`}>{result.passed ? 'Module marked as completed.' : 'Review the explanations above and try again.'}</Callout>}
        <div className="flex gap-2 mt-5">
          {!result ? <Button variant="primary" loading={busy} disabled={answers.filter((a) => a != null).length !== m.quiz.length} onClick={submit}>Submit answers</Button>
            : <Button onClick={() => { setResult(null); setAnswers([]); document.getElementById('quiz')?.scrollIntoView({ behavior: 'smooth' }); }}>Try again</Button>}
        </div>
      </Card>
      <div className="flex justify-between mt-6 text-sm">
        {prev ? <Link to={`/training/${prev.slug}`} className="flex items-center gap-1 text-brand-600"><ArrowLeft className="size-4" />{prev.title}</Link> : <span />}
        {next && <Link to={`/training/${next.slug}`} className="flex items-center gap-1 text-brand-600">{next.title}<ArrowRight className="size-4" /></Link>}
      </div>
    </div>
  );
}
