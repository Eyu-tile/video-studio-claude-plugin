// Standard section structure per document type (mirrors content/FORMAT.md)
export const SECTION_LABELS = {
  overview: 'Overview', description: 'Issue Description', causes: 'Possible Causes', collect: 'Information to Collect',
  steps: 'Troubleshooting Steps', customer_steps: 'Customer Steps',
  response_en: 'Recommended Response (EN)', response_am: 'Recommended Response (AM)', short_en: 'Short Response (EN)', short_am: 'Short Response (AM)',
  followup_en: 'Follow-Up Response (EN)', followup_am: 'Follow-Up Response (AM)', escalation: 'Escalation Conditions', resolution: 'Resolution Procedure',
  policy_pending: 'Policy Pending Approval', internal: 'Internal Notes', answer_en: 'Answer (EN)', answer_am: 'Answer (AM)',
  objective: 'Objective', when_to_use: 'When to Use', responsible: 'Responsible', required_info: 'Required Information', sop_steps: 'Steps',
  expected_outcome: 'Expected Outcome', common_mistakes: 'Common Mistakes', sop_escalation: 'Escalation', related_templates: 'Related Templates',
  purpose: 'Purpose', scope: 'Scope', confirmed_rules: 'Confirmed Rules', staff_rules: 'Rules for Support Staff', guidelines: 'Guidelines', examples: 'Examples', do_dont: "Do and Don't",
};

export const TYPE_SECTIONS = {
  article: ['description', 'causes', 'collect', 'steps', 'response_en', 'response_am', 'short_en', 'short_am', 'followup_en', 'followup_am', 'escalation', 'resolution', 'internal'],
  troubleshooting: ['overview', 'steps', 'escalation', 'internal'],
  faq: ['answer_en', 'answer_am', 'internal'],
  sop: ['objective', 'when_to_use', 'responsible', 'required_info', 'sop_steps', 'expected_outcome', 'common_mistakes', 'sop_escalation', 'related_templates', 'internal'],
  policy: ['purpose', 'scope', 'confirmed_rules', 'staff_rules', 'policy_pending', 'internal'],
  guide: ['overview', 'guidelines', 'examples', 'do_dont', 'internal'],
};
export const OPTIONAL_SECTIONS = {
  article: ['overview', 'customer_steps', 'policy_pending'],
  troubleshooting: ['description', 'causes', 'collect', 'response_en', 'response_am', 'short_en', 'short_am', 'resolution', 'policy_pending'],
  faq: [],
  sop: ['policy_pending'],
  policy: [],
  guide: ['policy_pending'],
};
export const SCOPE_OF = { article: 'kb', troubleshooting: 'kb', faq: 'kb', sop: 'sop', policy: 'policy', guide: 'communication' };

export const SECTION_HINTS = {
  description: 'Explain the problem clearly from the customer\'s point of view.',
  collect: 'Exactly what to ask for. Never passwords, OTP codes, PINs or card numbers.',
  steps: 'Numbered steps the agent follows. Use checklists for verification steps.',
  response_en: 'Ready-to-copy message. Use placeholders like {{customer_name}}, {{ticket_id}}. No invented timelines.',
  response_am: 'Amharic version of the recommended response (respectful እርስዎ form).',
  short_en: 'Short version for Telegram.', short_am: 'Short Amharic version for Telegram.',
  followup_en: 'What to send when the issue is still unresolved.', followup_am: 'Amharic follow-up message.',
  escalation: 'When to escalate and to which department.',
  resolution: 'How to confirm the issue is resolved and what to record before closing.',
  policy_pending: 'Decisions management has not yet approved. Never present these as rules.',
  internal: 'Agent-only guidance. Never shown to customers or the AI assistant.',
};
