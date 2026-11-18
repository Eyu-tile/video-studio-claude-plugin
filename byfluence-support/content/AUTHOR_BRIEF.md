# Brief for content authors

You are writing the initial support documentation for the **Byfluence Customer Support Operating
System** — an internal web app support agents use every day. Your writing will be read by real
support agents in Ethiopia while a customer is waiting on Telegram, email or the phone.

Read these first (all in `byfluence-support/content/`):
1. `BUSINESS_CONTEXT.md` — the only confirmed facts about Byfluence.
2. `FORMAT.md` — the exact file format, metadata keys, section headings, ground rules and the
   gold-standard example article (`kb/payments-00-gold.md`). Match its depth for issue articles.
3. `taxonomy.json` — valid category/subcategory slugs, department keys, feature keys, placeholders.

## Quality bar
- **Issue articles** (something went wrong) follow the full structure: Summary, Issue Description,
  Possible Causes, Information to Collect, Troubleshooting Steps, Recommended Response EN+AM,
  Short Response EN+AM, Follow-Up Response EN+AM, Escalation Conditions, Resolution Procedure,
  Policy Pending Approval (when a rule is undecided), Internal Notes.
- **How-to / informational articles** (how something works) use: Summary, Overview,
  Customer Steps (if any), Recommended Response EN+AM, Short Response EN+AM, Escalation Conditions
  (when to hand off), Policy Pending Approval (if needed), Internal Notes. Shorter, but complete.
- Be concrete: what exactly the agent checks, in which order, what each outcome means, which
  department, which ticket priority. Think about edge cases, fraud signals, time-sensitive cases,
  sellers vs buyers, mobile users, customers with low digital literacy, Amharic-only customers.
- Customer messages: warm, professional, concise, empathetic; ask only for what's needed; always
  give the case number `{{ticket_id}}` in full responses; no promises of timelines/outcomes.
- Amharic: natural, respectful (እርስዎ form), not word-for-word machine-like. Keep placeholders,
  brand names and technical references in Latin script.
- Where business rules are unknown, add a `## Policy Pending Approval` section listing the
  decisions management must make, set `policy_pending: yes`, and tell agents in Internal Notes
  what to do meanwhile (usually: escalate to Senior Support / Supervisor, do not promise).
- Features that are planned (physical products, delivery, inventory-free selling, digital
  products, non-confirmed payment methods) must be tagged with `features:` and the article must
  tell agents to check the Feature Status page before telling customers the feature is available.

## Process
- Write ONLY the files assigned to you. Do not edit other files, code, FORMAT.md or taxonomy.json.
- Keep each file under ~1,200 lines; split into `name-1.md`, `name-2.md` if needed.
- Use the exact IDs given in your assignment so cross-links resolve. You may add a few extra
  articles you think are essential (prefix rules in FORMAT.md) — mention them in your final report.
- When done, validate:  `cd byfluence-support && node server/content/check.js <your files>`
  Fix every ERROR. Review every WARN about concrete numbers/times in customer-facing text and
  remove invented promises (warnings that are legitimately fine may stay).
- Final report (short): files written, number of docs, any extra IDs added, any policy gaps you
  think management should know about. Do not paste the content back.
