// Parser for the Markdown seed content in /content (see content/FORMAT.md).
// Pure functions, no dependencies — shared by the seeder and the content checker.

export const SECTION_KEYS = {
  'Summary': 'summary',
  'Overview': 'overview',
  'Issue Description': 'description',
  'Possible Causes': 'causes',
  'Information to Collect': 'collect',
  'Troubleshooting Steps': 'steps',
  'Customer Steps': 'customer_steps',
  'Recommended Response (EN)': 'response_en',
  'Recommended Response (AM)': 'response_am',
  'Short Response (EN)': 'short_en',
  'Short Response (AM)': 'short_am',
  'Follow-Up Response (EN)': 'followup_en',
  'Follow-Up Response (AM)': 'followup_am',
  'Escalation Conditions': 'escalation',
  'Resolution Procedure': 'resolution',
  'Policy Pending Approval': 'policy_pending',
  'Internal Notes': 'internal',
  'Answer (EN)': 'answer_en',
  'Answer (AM)': 'answer_am',
  'Objective': 'objective',
  'When to Use': 'when_to_use',
  'Responsible': 'responsible',
  'Required Information': 'required_info',
  'Steps': 'sop_steps',
  'Expected Outcome': 'expected_outcome',
  'Common Mistakes': 'common_mistakes',
  'Escalation': 'sop_escalation',
  'Related Templates': 'related_templates',
  'Purpose': 'purpose',
  'Scope': 'scope',
  'Confirmed Rules': 'confirmed_rules',
  'Rules for Support Staff': 'staff_rules',
  'Guidelines': 'guidelines',
  'Examples': 'examples',
  "Do and Don't": 'do_dont',
  // templates
  'Subject (EN)': 'subject_en',
  'Subject (AM)': 'subject_am',
  'Message (EN)': 'message_en',
  'Message (AM)': 'message_am',
  'Usage Notes': 'usage_notes',
  // training
  'Learning Objectives': 'objectives',
  'Lesson': 'lesson',
  'Realistic Examples': 'examples',
  'Practical Exercises': 'exercises',
  'Knowledge Check': 'quiz',
};

export function slugify(s) {
  return String(s).toLowerCase().normalize('NFKD').replace(/[^\w\s-]/g, '').trim().replace(/[\s_]+/g, '_').slice(0, 60) || 'section';
}


/** Split a file into raw blocks: [{kind, text, line}] */
export function splitBlocks(text) {
  const out = [];
  const lines = text.replace(/\r\n/g, '\n').split('\n');
  let cur = null;
  lines.forEach((ln, i) => {
    const m = ln.match(/^<!--\s*(doc|template|module)\s*-->\s*$/);
    if (m) {
      if (cur) out.push(cur);
      cur = { kind: m[1], lines: [], line: i + 1 };
    } else if (cur) cur.lines.push(ln);
  });
  if (cur) out.push(cur);
  return out.map((b) => ({ kind: b.kind, text: b.lines.join('\n'), line: b.line }));
}

/** Parse one block into {title, meta, sections:[{label,key,body}]} */
export function parseBlock(block) {
  const lines = block.text.split('\n');
  let i = 0;
  while (i < lines.length && !lines[i].trim()) i++;
  const titleLine = lines[i] || '';
  const title = titleLine.startsWith('# ') ? titleLine.slice(2).trim() : null;
  i++;
  const meta = {};
  for (; i < lines.length; i++) {
    const ln = lines[i];
    if (ln.startsWith('## ')) break;
    const m = ln.match(/^([a-z_]+):\s*(.*)$/);
    if (m) meta[m[1]] = m[2].trim();
  }
  const sections = [];
  let cur = null;
  let inFence = false;
  for (; i < lines.length; i++) {
    const ln = lines[i];
    if (/^```/.test(ln)) inFence = !inFence;
    if (!inFence && ln.startsWith('## ')) {
      if (cur) sections.push(cur);
      const label = ln.slice(3).trim();
      cur = { label, key: SECTION_KEYS[label] || slugify(label), lines: [] };
    } else if (cur) cur.lines.push(ln);
  }
  if (cur) sections.push(cur);
  return {
    kind: block.kind,
    line: block.line,
    title,
    meta,
    sections: sections.map((s) => ({ label: s.label, key: s.key, body: s.lines.join('\n').trim() })),
  };
}

export const list = (v) => (v ? String(v).split(',').map((s) => s.trim()).filter(Boolean) : []);

/** Parse the Knowledge Check section into questions. */
export function parseQuiz(md) {
  const qs = [];
  let cur = null;
  for (const raw of (md || '').split('\n')) {
    const ln = raw.trim();
    if (/^Q:/i.test(ln)) {
      if (cur) qs.push(cur);
      cur = { question: ln.replace(/^Q:\s*/i, ''), options: [], answer: -1, explanation: '' };
    } else if (cur && /^- \[( |x|X)\]/.test(ln)) {
      if (/^- \[(x|X)\]/.test(ln)) cur.answer = cur.options.length;
      cur.options.push(ln.replace(/^- \[( |x|X)\]\s*/, ''));
    } else if (cur && ln.startsWith('>')) {
      cur.explanation += (cur.explanation ? ' ' : '') + ln.replace(/^>\s*/, '');
    }
  }
  if (cur) qs.push(cur);
  return qs;
}
