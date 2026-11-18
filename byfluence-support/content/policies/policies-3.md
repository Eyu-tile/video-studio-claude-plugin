<!-- doc -->
# Escalation matrix
id: pol-escalation-matrix
type: policy
category: support-standards
audience: internal
priority: high
department: support_l2
tags: escalation matrix, who to escalate to, department, level 2, level 3, level 4, የማሳደጊያ ሰንጠረዥ, routing
related: sop-escalation, sop-prioritize, sop-security-incident, sop-payment-investigation, sop-mass-incident, pol-service-levels
templates: tpl-escalation-notification, tpl-status-update
policy_pending: yes

## Summary
Which issue goes to which escalation level and department, and when. The four-level structure and department responsibilities are confirmed; named contacts and handoff channels are pending.

## Purpose
Send every issue to the team that can actually solve it, the first time, with the right urgency.

## Scope
All tickets on all channels.

## Confirmed Rules
The support structure has four levels:

| Level | Team | Handles |
|---|---|---|
| 1 | **Customer Support** | Routine questions, guidance, basic troubleshooting, information collection, first response, documentation |
| 2 | **Senior Support / Supervisor** | Complex complaints, buyer–seller disputes, repeated unresolved issues, refund recommendations, policy-pending decisions, supervisor requests |
| 3 | **Specialized Department** | **Payments & Finance** — payment verification, duplicate charges, refund processing, payouts, reconciliation · **Technical / Engineering** — bugs, outages, booking errors, Google Meet link generation, notification failures · **Seller Operations** — seller verification review, listing review, seller restrictions, supplier/reseller programs · **Trust & Safety** — fraud, account compromise, harassment, counterfeit listings, privacy and security incidents · **Logistics & Fulfillment** — delivery partners, Addis Ababa delivery operations, lost or damaged shipments (when live) |
| 4 | **Management** | Critical decisions, policy exceptions, legal or regulatory matters, high-value or reputational issues |

Humans (not the AI assistant) handle account-specific investigation, financial decisions, identity verification review, refund approval, seller disputes, fraud, admin access and sensitive data.

## Rules for Support Staff
Use this matrix together with the KB article's Escalation Conditions.

| Issue | Escalate to | When | Suggested priority |
|---|---|---|---|
| Paid but booking/order not confirmed | Payments & Finance | After verifying customer and collecting reference | High (Critical if session very soon) |
| Duplicate charge / wrong amount | Payments & Finance | After locating both transactions or the reference | High |
| Failed payment but money deducted | Payments & Finance | After checking records | High |
| Refund request (any) | Senior Support → Payments & Finance / Management | After facts, evidence and seller's side collected | High |
| Withdrawal missing / balance wrong | Payments & Finance | After full seller verification | High |
| Payout details change request | Payments & Finance (+ Trust & Safety if suspicious) | After full verification | High |
| Bug, error message, page not working | Technical | After basic troubleshooting and collecting device/browser/screenshot | Medium–High |
| Missing/incorrect Google Meet link | Technical (+ inform seller side per policy) | Immediately if session is soon | High/Critical |
| Many customers same problem | Supervisor → Technical / Payments | As soon as pattern is noticed | Critical |
| Seller verification delayed or rejected | Seller Operations | After collecting application details | Medium |
| Listing rejected / reported listing | Seller Operations (Trust & Safety if harmful/counterfeit) | After documenting | Medium–High |
| Seller suspended/banned asks why | Seller Operations | After verification | Medium |
| Buyer–seller dispute | Senior Support (→ Seller Ops, Payments, Management) | After both sides collected | High |
| Account takeover / unauthorized access | Trust & Safety (+ Payments if money at risk) | Immediately | Critical |
| Fraud signals, fake receipts, scams | Trust & Safety | Immediately after documenting | High/Critical |
| Harassment, threats, safety risk | Trust & Safety (+ Management if severe) | Immediately | Critical |
| Data exposure / privacy incident | Trust & Safety + Management | Immediately | Critical |
| Delivery lost/damaged (when live) | Logistics & Fulfillment | After order and delivery details collected | High |
| Legal threat, lawyer/police contact, regulator | Management via Supervisor | Immediately; do not respond on substance | High/Critical |
| Media, influencer or viral social post | Management via Supervisor | Immediately | High/Critical |
| Policy pending, decision needed | Senior Support → Management | When the customer needs a decision | Per issue |
| Customer asks for a supervisor | Senior Support | On request (after trying to help) | Per issue |

## Policy Pending Approval
- Confirm named contacts, queues or handoff channels for each Level 3 department and for Management.
- Confirm after-hours escalation contacts for Critical issues (security, mass incidents).
- Confirm whether Logistics & Fulfillment is staffed before physical products go live.
- Confirm monetary thresholds (if any) that require Management involvement.

## Internal Notes
- When two departments are involved, escalate to the one that must act first and mention the other in the note; the Supervisor coordinates.
- Escalating does not end your responsibility: you remain the customer's contact and keep following up.

<!-- doc -->
# Internal response & resolution targets
id: pol-service-levels
type: policy
category: support-standards
audience: internal
priority: medium
department: management
tags: SLA, response time, resolution time, targets, service levels, የምላሽ ጊዜ, overdue tickets, breach
related: sop-prioritize, sop-follow-up, sop-daily-report, pol-escalation-matrix, pol-communication-standards
templates: tpl-delayed-response-apology, tpl-status-update, tpl-still-investigating
policy_pending: yes

## Summary
Byfluence support uses configurable **internal** response and resolution targets per priority (set in Settings). They are management tools, not promises to customers. The actual target values are pending approval.

## Purpose
Help the team prioritize, spot tickets at risk, and measure performance — without creating customer guarantees Byfluence has not approved.

## Scope
All tickets, all channels, all levels including escalations to departments.

## Confirmed Rules
- The support app has configurable internal response and resolution targets; they are not customer guarantees.
- Byfluence must never promise anything not authorized (business support principles).

## Rules for Support Staff
- **Never quote internal targets to customers** ("we answer within X hours", "resolved within X days"). Use neutral wording: "as soon as possible", "we will update you", or `{{estimated_resolution_time}}` only with approved wording.
- Use targets to order your work: tickets close to or past their target come first within the same priority.
- A target being close is never a reason to resolve a ticket that isn't solved, or to skip verification.
- If a ticket missed its target, apologize to the customer for the wait (tpl-delayed-response-apology) — without excuses or blaming other teams.
- Escalations past their target: chase, then raise to the Supervisor (*Escalating issues*).

## Policy Pending Approval
- Approve the first-response and resolution target values per priority (Low, Medium, High, Critical) and enter them in Settings.
- Decide whether targets count business hours or calendar hours, and define support hours per channel.
- Decide after-hours and holiday coverage, especially for Critical tickets.
- Decide whether any customer-facing service commitment will be published, and its exact wording.
- Decide targets for Level 3 departments responding to escalations.
- Decide how target breaches are reported and reviewed.

## Internal Notes
- Supervisors: review overdue tickets daily and include the count in the daily report.
- Meeting targets with poor quality is not success. Quality reviews and reopen rates are read together with target performance.

<!-- doc -->
# Communication standards
id: pol-communication-standards
type: policy
category: support-standards
audience: internal
priority: medium
department: support_l2
tags: communication standards, language, tone, case number, signature, official channels, የግንኙነት መመሪያ, Amharic default
related: com-tone-voice, com-writing-clear-messages, com-amharic-guidelines, com-what-never-to-say, pol-service-levels, sop-first-response
templates: tpl-greeting-telegram, tpl-greeting-email, tpl-phone-inbound-opening, tpl-status-update
policy_pending: yes

## Summary
The standards every customer message must meet: language, tone, structure, case numbers, official channels, honesty about what we know, and complete recording in the ticket.

## Purpose
Customers should experience one consistent, trustworthy Byfluence voice on every channel and from every agent.

## Scope
All written and spoken communication with buyers and sellers on all channels, including templates and KB responses.

## Confirmed Rules
- Channels intended: website support, Telegram, email, telephone, AI-powered assistance (future).
- **Amharic is the default language; English on request.**
- Communication must be professional, respectful, clear, concise and consistent.
- **Never promise anything not authorized.**
- Experience principles: Simplicity, Trust, Opportunity, Accountability.
- The support app's communication log is manual: agents record Telegram, email and phone contacts themselves; nothing is sent automatically from the app.

## Rules for Support Staff
### Language
- Reply in the customer's language. Default to Amharic; switch to English when the customer writes in English or asks. Use the respectful form (እርስዎ) in Amharic.
- Keep brand names, placeholders and technical references (Byfluence, Google Meet, Chapa, transaction IDs) in Latin script.

### Every full message includes
- Greeting with the customer's name.
- Acknowledgement of the issue.
- What we need or what we did, clearly.
- The case number `{{ticket_id}}`.
- The next step (without unapproved timelines).
- Agent's first name and "Byfluence Support".

### Honesty and promises
- Say only what is confirmed in the KB, Announcements, Feature Status page or by the responsible department.
- Do not promise outcomes (refunds, approvals, reinstatement), timelines, compensation or features.
- When a policy is pending, say the request will be reviewed (see *What to do when a policy is not yet approved*).
- Never blame the customer, the seller, a payment provider or another team.

### Channels and records
- Use official Byfluence channels only; never personal accounts or numbers.
- Record every contact in the communication log (channel, direction, time, summary).
- Keep the conversation in one ticket per case.

### Safety lines
- Remind customers that Byfluence never asks for passwords, PINs or verification codes whenever payment or login is discussed.

## Policy Pending Approval
- Confirm the official support channels, contact details and hours to publish to customers (`{{support_channel}}`).
- Approve signature formats per channel and any mandatory footer text.
- Approve the approved wording library for timelines (`{{estimated_resolution_time}}`) per issue type.
- Decide whether other languages (e.g., Afaan Oromo, Tigrinya) will be supported and how.

## Internal Notes
- The best consistency tool is the knowledge base: start from KB responses and templates, then personalize.
- Read *Byfluence tone of voice* and *Phrases to never use* alongside this policy.

<!-- doc -->
# What to do when a policy is not yet approved
id: pol-policy-pending-procedure
type: policy
category: support-standards
audience: internal
priority: high
department: support_l2
tags: policy pending, no policy, unknown rule, not decided, interim procedure, ፖሊሲ ያልጸደቀ, what do I say, holding response
related: pol-operational-safety-rules, pol-refunds-cancellations, sop-escalation, sop-daily-report, sop-kb-update-request, com-saying-no
templates: tpl-escalation-notification, tpl-status-update, tpl-still-investigating
policy_pending: no

## Summary
Byfluence is at MVP stage and many rules (refunds, attendance, payouts, verification documents, prohibited items) are not yet approved. This is the procedure every agent follows when a customer needs an answer that depends on an unapproved policy.

## Purpose
Prevent agents from inventing rules under pressure, give customers an honest and consistent answer, and turn each gap into input for management to decide.

## Scope
Any ticket where the KB article has a **Policy Pending Approval** section relevant to the customer's question, or where no rule exists at all.

## Confirmed Rules
- Never invent policies; never promise anything not authorized; never auto-approve refunds; never promise unconfirmed timelines (*Operational safety rules*).
- Decisions on refunds, disputes, exceptions and policy are made by authorized personnel (Level 2 and above, Management for exceptions).

## Rules for Support Staff
1. **Recognize it.** If the KB says "Policy Pending Approval" for the point you need, or there is no article, you do not have a rule. Do not fill the gap with what you think is fair, what another company does, or what a colleague said once.
2. **Do the fact-finding anyway.** Verify the customer, collect all information and evidence the decision will need. A complete case gets decided faster.
3. **Tell the customer the truth, positively:**
   - EN: "Thank you for the details. Your request needs to be reviewed by our team, and I have submitted it with all the information you provided. I will update you as soon as there is a decision. Your case number is {{ticket_id}}."
   - AM: "ለዝርዝር መረጃው እናመሰግናለን። ጥያቄዎ በቡድናችን መገምገም ያስፈልገዋል፤ የሰጡንን መረጃ በሙሉ አያይዤ አስገብቼዋለሁ። ውሳኔ እንደተሰጠ ወዲያውኑ አሳውቅዎታለሁ። የጉዳይ ቁጥርዎ {{ticket_id}} ነው።"
   - Do **not** say "there is no policy" or "nobody has decided" in a way that undermines trust; say it "needs to be reviewed".
4. **Record it.** Internal note: "Policy pending: [exact decision needed, e.g., buyer no-show refund rule for 1:1 consultations]". Link the KB article ID.
5. **Escalate** to Senior Support / Supervisor (status Escalated, follow-up set). Level 2 decides within their authority or escalates to Management.
6. **Report it.** The Supervisor includes the case in the daily report's **policy gaps** list with ticket numbers.
7. **Apply decisions consistently.** When Management decides a case, Level 2 records the decision and reasoning. If Management says the decision is a rule going forward, it is announced and the KB is updated (*Requesting a knowledge base update*). Until then, a one-off decision is not a rule — don't apply it to other customers by yourself.

## Internal Notes
- Customers accept "this needs review" far better than a confident answer that is later reversed.
- If customers keep asking the same unapproved question, that is a strong signal for management — make sure it reaches the daily report.
