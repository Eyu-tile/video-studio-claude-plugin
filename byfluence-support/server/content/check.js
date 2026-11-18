#!/usr/bin/env node
// Validates seed content files. Usage:
//   node server/content/check.js                 (checks every file under content/)
//   node server/content/check.js content/kb/payments.md content/faqs/payments.md
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { splitBlocks, parseBlock, parseQuiz, list } from './parse.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../content');
const tax = JSON.parse(fs.readFileSync(path.join(root, 'taxonomy.json'), 'utf8'));

const TYPES = ['article', 'troubleshooting', 'faq', 'sop', 'policy', 'guide'];
const SCOPE_OF = { article: 'kb', troubleshooting: 'kb', faq: 'kb', sop: 'sop', policy: 'policy', guide: 'communication' };
const PRIORITIES = ['low', 'medium', 'high', 'critical'];
const AUDIENCES = ['buyer', 'seller', 'both', 'internal'];
const CHANNELS = ['telegram', 'email', 'chat', 'sms', 'phone', 'any'];
const STYLES = ['short', 'standard', 'detailed', 'formal', 'friendly'];
const DEPTS = tax.departments.map((d) => d.key);
const FEATURES = tax.features.map((f) => f.key);
const PLACEHOLDERS = tax.placeholders.map((p) => p.key);

export function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) return walk(p);
    return e.name.endsWith('.md') && !['FORMAT.md', 'BUSINESS_CONTEXT.md', 'AUTHOR_BRIEF.md'].includes(e.name) && !p.includes(`${path.sep}_`) ? [p] : [];
  });
}

const PAIRS = [['response_en', 'response_am'], ['short_en', 'short_am'], ['followup_en', 'followup_am'], ['answer_en', 'answer_am'], ['message_en', 'message_am'], ['subject_en', 'subject_am']];
const CUSTOMER_FACING = ['response_en', 'short_en', 'followup_en', 'answer_en', 'message_en', 'subject_en'];
// Concrete promises that must not be invented
const PROMISE_RE = /\b\d+\s*(?:-\s*\d+\s*)?(?:business\s+|working\s+)?(?:days?|hours?|hrs?|minutes?|weeks?)\b|\b\d+(?:\.\d+)?\s*%|\b\d[\d,]*\s*(?:ETB|birr)\b/i;

export function checkFiles(files) {
  const errors = [];
  const warnings = [];
  const ids = new Map();
  let count = { doc: 0, template: 0, module: 0 };
  for (const file of files) {
    const rel = path.relative(path.resolve(root, '..'), file);
    const text = fs.readFileSync(file, 'utf8');
    const blocks = splitBlocks(text);
    if (!blocks.length) errors.push(`${rel}: no <!-- doc|template|module --> markers found`);
    for (const b of blocks) {
      const d = parseBlock(b);
      const where = `${rel}:${d.line} [${d.meta.id || d.title || '?'}]`;
      const err = (m) => errors.push(`${where} ${m}`);
      const warn = (m) => warnings.push(`${where} ${m}`);
      count[d.kind]++;
      if (!d.title) err('missing "# Title" line right after the marker');
      if (!d.meta.id) err('missing id');
      else if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(d.meta.id)) err(`id "${d.meta.id}" must be lowercase-kebab`);
      else if (ids.has(d.meta.id)) err(`duplicate id (also in ${ids.get(d.meta.id)})`);
      else ids.set(d.meta.id, rel);
      const keys = d.sections.map((s) => s.key);
      const sec = Object.fromEntries(d.sections.map((s) => [s.key, s.body]));
      for (const s of d.sections) if (!s.body) warn(`section "${s.label}" is empty`);
      for (const [a, b2] of PAIRS) {
        if (keys.includes(a) && !keys.includes(b2)) err(`has ${a} but missing ${b2}`);
        if (keys.includes(b2) && !keys.includes(a)) err(`has ${b2} but missing ${a}`);
      }
      for (const k of CUSTOMER_FACING) {
        const body = sec[k];
        if (!body) continue;
        const m = body.match(PROMISE_RE);
        if (m) warn(`customer-facing ${k} contains a concrete number/time "${m[0]}" — make sure it is not an invented policy (use {{estimated_resolution_time}})`);
        for (const ph of body.match(/{{\s*([a-z_]+)\s*}}/g) || []) {
          const key = ph.replace(/[{}\s]/g, '');
          if (!PLACEHOLDERS.includes(key)) err(`unknown placeholder ${ph}`);
        }
        if (/\b(password|otp|pin)\b/i.test(body) && !/(never|not|don't|do not|አያጋሩ|አንጠይቅ)/i.test(body)) warn(`${k} mentions password/OTP/PIN — make sure it is a warning not a request`);
      }
      if (d.kind === 'doc') {
        const t = d.meta.type;
        if (!TYPES.includes(t)) { err(`type "${t}" invalid`); continue; }
        const scope = tax.scopes[SCOPE_OF[t]];
        const cat = scope.find((c) => c.slug === d.meta.category);
        if (!cat) err(`category "${d.meta.category}" not in scope ${SCOPE_OF[t]}`);
        if (SCOPE_OF[t] === 'kb' && cat) {
          if (!d.meta.subcategory) err('missing subcategory');
          else if (!cat.subcategories.some((s) => s.slug === d.meta.subcategory)) err(`subcategory "${d.meta.subcategory}" not in ${cat.slug}`);
        }
        if (d.meta.priority && !PRIORITIES.includes(d.meta.priority)) err(`priority "${d.meta.priority}" invalid`);
        if (d.meta.audience && !AUDIENCES.includes(d.meta.audience)) err(`audience "${d.meta.audience}" invalid`);
        if (d.meta.department && !DEPTS.includes(d.meta.department)) err(`department "${d.meta.department}" invalid`);
        for (const f of list(d.meta.features)) if (!FEATURES.includes(f)) err(`feature "${f}" invalid`);
        if (t === 'faq') {
          if (!sec.answer_en) err('faq needs ## Answer (EN) and ## Answer (AM)');
        } else if (!sec.summary) err('missing ## Summary');
        if (t === 'article') {
          if (!sec.response_en) warn('article has no Recommended Response (EN/AM)');
          if (!sec.escalation) warn('article has no Escalation Conditions');
        }
        const pp = (d.meta.policy_pending || 'no') === 'yes';
        if (pp && !sec.policy_pending) err('policy_pending: yes but no ## Policy Pending Approval section');
        if (!pp && sec.policy_pending) err('has Policy Pending Approval section but policy_pending is not yes');
        if (!d.meta.tags && t !== 'sop' && t !== 'policy' && t !== 'guide') warn('no tags');
      } else if (d.kind === 'template') {
        const cat = tax.scopes.template.find((c) => c.slug === d.meta.category);
        if (!cat) err(`template category "${d.meta.category}" invalid`);
        if (!CHANNELS.includes(d.meta.channel)) err(`channel "${d.meta.channel}" invalid`);
        if (!STYLES.includes(d.meta.style)) err(`style "${d.meta.style}" invalid`);
        if (!sec.message_en || !sec.message_am) err('template needs ## Message (EN) and ## Message (AM)');
        if (d.meta.channel === 'email' && !sec.subject_en) warn('email template without ## Subject (EN)/(AM)');
      } else if (d.kind === 'module') {
        if (!d.meta.number) err('module missing number');
        for (const k of ['objectives', 'lesson', 'quiz']) if (!sec[k]) err(`module missing section ${k}`);
        const qs = parseQuiz(sec.quiz);
        if (qs.length < 3) err(`knowledge check has ${qs.length} questions (need ≥3)`);
        qs.forEach((q, n) => { if (q.answer < 0 || q.options.length < 2) err(`quiz question ${n + 1} needs options and exactly one [x]`); });
      }
    }
  }
  return { errors, warnings, count, ids };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const args = process.argv.slice(2);
  const files = args.length ? args.map((a) => path.resolve(a)) : walk(root);
  const { errors, warnings, count } = checkFiles(files);
  for (const w of warnings) console.log('WARN ', w);
  for (const e of errors) console.log('ERROR', e);
  console.log(`\n${files.length} files · ${count.doc} docs · ${count.template} templates · ${count.module} modules · ${errors.length} errors · ${warnings.length} warnings`);
  process.exit(errors.length ? 1 : 0);
}
