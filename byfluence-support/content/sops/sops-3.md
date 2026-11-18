<!-- doc -->
# Preparing the daily support report
id: sop-daily-report
type: sop
category: reporting
audience: internal
priority: medium
department: support_l2
tags: daily report, support report, metrics, KPIs, backlog, ዕለታዊ ሪፖርት, shift report, management report
related: sop-handover, sop-mass-incident, sop-quality-review, sop-kb-update-request, pol-service-levels, pol-policy-pending-procedure
templates: tpl-status-update
policy_pending: yes

## Summary
How the supervisor or shift lead compiles one short daily report for management: volumes, backlog, urgent items, escalations, incidents, reopened tickets, policy gaps and recommended actions.

## Objective
Give management a reliable daily picture of customer problems and support performance so they can fix root causes, approve pending policies and staff the team correctly. The report must be factual, short and actionable.

## When to Use
Once per day, at the end of the support day (or after the last shift), and additionally after any major incident.

## Responsible
- **Supervisor / shift lead (Level 2)** prepares and sends it.
- **Agents** provide shift notes (unusual cases, policy questions) via the handover.

## Required Information
- Ticket list and filters in the support app (by status, priority, category, escalation level, created/resolved date).
- Handover notes from all shifts of the day.
- Incident summaries, if any.
- Quality review findings (if reviews were done that day).

## Steps
1. **Pull the numbers** from the support app for the reporting day:
   - Tickets created (by channel: Telegram, email, phone, web).
   - Tickets resolved and closed.
   - Open backlog by status (New, Open, Under Review, Waiting for Customer, Waiting for Seller, Escalated, In Progress, Reopened).
   - Open Critical and High tickets (list them individually).
   - Tickets past the internal response/resolution targets configured in Settings.
   - Escalations by level and department; escalations still waiting for a department.
   - Reopened tickets.
2. **Identify the top issues:** the top categories by volume and anything new or growing compared with the previous days.
3. **Summarize incidents:** for each mass incident: start/end, affected feature, number of tickets, current status, open customer follow-ups.
4. **List policy gaps encountered:** each case where agents had to escalate because a policy is pending (e.g., "3 refund requests for seller no-shows — no approved rule"). Include ticket numbers. This is the most useful input for management.
5. **List knowledge gaps:** missing/wrong KB articles and KB update requests submitted.
6. **Note risks:** fraud patterns, security reports, legal/media threats, very unhappy high-profile customers, sellers with repeated complaints.
7. **Team notes:** staffing gaps, tool problems (app or channel outages), training needs.
8. **Recommendations:** up to five concrete actions, each with an owner suggestion ("Payments to approve wording for verification times").
9. **Check the report:** no customer personal data beyond ticket numbers; no speculation presented as fact.
10. **Send** it to the management recipients through the agreed internal channel and keep a copy where your team stores reports.

### Suggested layout
| Section | Content |
|---|---|
| Headline | One to three sentences: how was the day, anything critical? |
| Volumes | Created, resolved, closed, backlog by status |
| Urgent | Open Critical/High with owner and next step |
| Escalations | By department; overdue ones |
| Incidents | Summary per incident |
| Top issues | Top categories and trends |
| Policy gaps | Pending decisions blocking tickets, with ticket numbers |
| KB gaps | Requests submitted |
| Risks | Fraud, security, legal/media, reputational |
| Team | Staffing, tools, training |
| Recommendations | Actions with suggested owners |

## Expected Outcome
A concise daily report sent on time, with accurate figures from the app and clear decisions requested from management.

## Common Mistakes
- Numbers only, no explanation of what they mean.
- Including customer names, phone numbers or screenshots — use ticket numbers.
- Leaving out policy gaps because "management already knows".
- Copying yesterday's report without checking.

## Escalation
- Any Critical item still open at report time → inform **Management** directly, not only in the report.
- A trend suggesting fraud or a security issue → **Trust & Safety** as well.

## Related Templates
- tpl-status-update — the report itself is internal; use status updates to inform customers about items listed as open.

## Policy Pending Approval
- Confirm the report recipients, delivery channel and time of day.
- Confirm which KPIs management wants tracked and the internal targets they are compared against.

## Internal Notes
- Keep it to one screen if possible; link the master tickets for detail.
- Trends matter more than single days. Mention when something has been growing for several days.

<!-- doc -->
# Ticket quality review (supervisors)
id: sop-quality-review
type: sop
category: reporting
audience: internal
priority: medium
department: support_l2
tags: quality review, QA, ticket review, scorecard, coaching, የጥራት ግምገማ, audit tickets, agent feedback
related: sop-close-ticket, sop-reopen-ticket, sop-daily-report, pol-communication-standards, pol-operational-safety-rules, com-what-never-to-say
templates: tpl-issue-resolved-confirm, tpl-greeting-telegram, tpl-greeting-email
policy_pending: yes

## Summary
How supervisors review a sample of tickets per agent against a standard scorecard, give coaching feedback, and feed findings into training and the knowledge base.

## Objective
Keep answers accurate, safe and consistent; catch unauthorized promises and safety-rule breaches early; and help every agent improve through specific, fair feedback.

## When to Use
- Regularly (frequency set by management) for every agent.
- Additionally for: every reopened ticket, every customer complaint about support, every ticket involving a safety-rule question, and new agents during their first weeks.

## Responsible
**Senior Support / Supervisor (Level 2)**. Reviews of supervisors are done by Management or another supervisor.

## Required Information
- Access to tickets, internal notes, communication log and resolution fields.
- The scorecard below.

## Steps
1. **Select the sample:** a random selection of each agent's resolved/closed tickets from the period, plus all mandatory-review tickets (reopened, complaints, safety-related). Mix channels and priorities.
2. **Read the full ticket:** customer messages, agent replies, internal notes, communication log, status history, resolution fields.
3. **Score each criterion** (Meets / Partly / Does not meet) and write a short comment with the example:

| Area | What "meets" looks like |
|---|---|
| **Safety (critical)** | No password/OTP/PIN/card data requested; no unauthorized promise of refund, timeline or outcome; no payment marked successful without verification; no invented policy |
| **Verification** | Identity verified before account-specific details were shared or changed |
| **Accuracy** | Information correct and consistent with KB, Announcements and Feature Status |
| **Triage** | Correct category, priority and status throughout |
| **Escalation** | Escalated to the right level/department with a complete package, at the right time |
| **Documentation** | Internal notes let another agent continue; communication log complete (Telegram/email/phone logged) |
| **Communication** | Language matches the customer; respectful Amharic (እርስዎ form) or clear English; empathetic, concise; case number given |
| **Follow-up** | Follow-ups set and met; customer never left without update |
| **Resolution** | Root cause, actions, final resolution specific; customer-notified flag accurate; not closed prematurely |

4. **Any "Does not meet" on Safety** is a critical finding: discuss with the agent the same day, check whether the customer needs a correction message (e.g., withdrawing an unauthorized promise), and record it.
5. **Write feedback:** start with what was done well, then one to three specific improvements with the example and the better version. Avoid general comments ("be more professional").
6. **Hold a short coaching conversation** with the agent; agree on one focus area for the next period.
7. **Feed the system:**
   - Repeated mistakes across agents → training topic.
   - Wrong or missing KB content → *Requesting a knowledge base update*.
   - Unclear policy → policy gap in the daily report.
8. **Record** the review results where your team keeps them, and summarize trends (not individual blame) in the daily/weekly report.

## Expected Outcome
Each agent receives regular, specific feedback; safety breaches are caught and corrected quickly; systemic issues reach training, KB and management.

## Common Mistakes
- Reviewing only tickets that went wrong — sample randomly too.
- Scoring on tone alone and missing a safety breach in the internal notes.
- Feedback with no example.
- Using reviews to punish rather than coach; agents then hide mistakes.

## Escalation
- Serious misconduct (data misuse, deliberate false resolution, sharing customer data externally) → **Management**, following HR processes.
- Correction to a customer needed after an unauthorized promise → Supervisor contacts the customer or assigns it, with approved wording.

## Related Templates
- tpl-issue-resolved-confirm, tpl-greeting-telegram, tpl-greeting-email — reference examples of good communication for coaching.

## Policy Pending Approval
- Confirm review frequency and sample size per agent.
- Confirm whether a numeric score is used and how it affects performance evaluation.
- Confirm who reviews supervisors' tickets.

## Internal Notes
- Calibrate: supervisors should occasionally score the same tickets independently and compare, so standards stay consistent across reviewers.

<!-- doc -->
# Requesting a knowledge base update
id: sop-kb-update-request
type: sop
category: reporting
audience: internal
priority: low
department: support_l2
tags: knowledge base, KB update, article wrong, missing article, documentation request, suggest edit, ዕውቀት ማዕከል, outdated answer
related: sop-close-ticket, sop-quality-review, sop-daily-report, pol-policy-pending-procedure, pol-communication-standards
templates: tpl-status-update
policy_pending: yes

## Summary
How any agent reports that a knowledge base article, template or SOP is missing, wrong, unclear or outdated, so that the documentation stays the team's single source of truth.

## Objective
Fix documentation gaps quickly and with evidence, so the next agent (and later the AI assistant) gives the right answer.

## When to Use
- No article exists for a recurring question or issue.
- An article gave a wrong or outdated answer (e.g., Feature Status changed, a policy was approved).
- A template's wording caused confusion or a complaint.
- Amharic text is unnatural, unclear or incorrect.
- A policy was approved or changed and the articles still show "pending".

## Responsible
- **Any agent** submits the request.
- **Supervisor / content owner** with Documentation Management permission reviews, edits and publishes.
- **The owning department or Management** approves any change involving policy, money or legal wording.

## Required Information
- Article/template/SOP ID and title (or "missing" with a proposed title).
- What is wrong or missing, precisely.
- Evidence: ticket numbers where it caused a problem, Announcement, approved policy.
- Proposed new text (optional but very helpful), in English and Amharic where relevant.

## Steps
1. **Check first:** search the KB to make sure the article really is missing, and check Announcements for recent changes.
2. **Never fix it yourself in a customer reply by inventing a rule.** If the article lacks a rule, follow *What to do when a policy is not yet approved*.
3. **Submit the request** through your team's documentation feedback process (the feedback option on the article if your version has one, otherwise an internal note on a related ticket plus a message to the Supervisor). Include:
   - **Type:** missing / incorrect / outdated / unclear / translation.
   - **Doc ID and title.**
   - **Problem:** what it says now vs. what is correct, and how you know.
   - **Evidence:** ticket numbers.
   - **Proposal:** suggested text, EN and AM.
   - **Urgency:** "wrong and causing harm now" (e.g., says a payment method is live when it is not) vs. "improvement".
4. **Urgent errors** (could cause a wrong promise, a safety breach or money loss): tell the Supervisor directly the same shift; the Supervisor may publish an Announcement as a temporary correction until the article is fixed.
5. **The reviewer** checks the facts with the owning department, edits the article in Documentation Management, updates the policy_pending status if a policy was approved, and records what changed.
6. **Close the loop:** the reviewer tells the requester the result; significant changes are announced to the team.

## Expected Outcome
Documentation problems are reported with evidence, urgent errors are corrected the same day via Announcements, and articles are updated by authorized editors.

## Common Mistakes
- Complaining in chat ("this article is wrong") without the ID or evidence.
- Writing your own unofficial "cheat sheet" for customers instead of fixing the KB.
- Proposing policy wording as if it were approved.

## Escalation
- The change requires a policy decision → **Management** via the daily report's policy gaps list.
- The article describes a feature incorrectly → **Technical** or the feature owner confirms the correct behaviour.

## Related Templates
- tpl-status-update — if customers received wrong information and need a correction, inform them with an update approved by the Supervisor.

## Policy Pending Approval
- Confirm who owns each knowledge base category and who may publish changes.
- Confirm the review cycle for articles (how often every article is re-checked).

## Internal Notes
- The knowledge base will also train the future AI assistant. A wrong article will be repeated at scale — report errors even when they seem small.
