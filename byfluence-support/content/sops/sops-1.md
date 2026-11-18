<!-- doc -->
# Starting a support shift
id: sop-start-shift
type: sop
category: shift
audience: internal
priority: medium
department: support_l1
tags: start of shift, shift start, login, handover read, morning checklist, የፈረቃ መጀመሪያ, queue check
related: sop-handover, sop-check-new-tickets, sop-prioritize, sop-end-shift, pol-acceptable-use-support-tools, pol-service-levels
templates: tpl-delayed-response-apology, tpl-known-outage
policy_pending: no

## Summary
The checklist every agent completes in the first part of their shift so they know what is urgent, what changed, and what they personally own before answering any customer.

## Objective
Start every shift with full situational awareness: no unread handover, no missed Critical ticket, no follow-up silently overdue, and no agent repeating outdated information to customers because they missed an announcement or a Feature Status change.

## When to Use
- At the start of every scheduled shift, including weekend and holiday shifts.
- When returning to the queue after a long break, training session or meeting during the shift (repeat steps 4–8).

## Responsible
- **Every Customer Support agent (Level 1)** completes the full checklist.
- **Senior Support / Supervisor (Level 2)** on shift completes it too and additionally confirms staffing (step 10).

## Required Information
- Your own support app login (never someone else's).
- The latest shift handover note from the previous shift.
- Access to the official support channels you are rostered on (Telegram support account, support mailbox, support phone line) — work accounts only.

## Steps
### Before you open the queue
1. Log in to the support app with your own account. If you cannot log in, tell your supervisor immediately — do not borrow a colleague's session.
2. Log in to the official channels you are assigned to today (support Telegram account, support mailbox, phone line). Never use a personal Telegram account or personal phone for customer contact.
3. Check that your workstation is safe: screen lock works, no customer documents are left in your Downloads folder from a previous shift (delete local copies after they were uploaded to the ticket).

### Catch up on what changed
4. Open **Announcements** and read every announcement published since your last shift. Pay special attention to known incidents, approved wording, and policy updates.
5. Open the **Feature Status** page. Note any feature whose status changed (for example a payment method moved from "unconfirmed" to "live", or a feature marked as having an incident). You must not tell customers a feature is available unless the Feature Status page says it is live.
6. Read the **shift handover note** from the previous shift (see *Shift handover*). Write down:
   - open Critical/High tickets and who owns them now,
   - any ongoing mass incident and its master ticket number,
   - promises made to customers ("we will call back at…") that fall into your shift.

### Check your own work
7. Filter the ticket list by **Assigned to me**. For each ticket check:
   - [ ] Status is correct (e.g., not left in *Open* when you are waiting for the customer).
   - [ ] Any **follow-up** due today or overdue — these come first.
   - [ ] Any customer reply received since your last shift (tickets in *Waiting for Customer* that have new messages must move back to *Open* or *In Progress*).
8. Open the **Follow-ups** view and sort by due date. Overdue follow-ups are handled before new tickets of the same priority.

### Check the shared queue
9. Look at the unassigned queue (status **New**) and count Critical and High tickets. If there are Critical tickets unassigned, follow *Checking and triaging new tickets* immediately — that takes priority over the rest of this checklist.
10. (Supervisor) Confirm who is on shift, which channels each agent covers, and who is the escalation point for Level 2. Post the shift plan in your team's internal channel if your team uses one.

### Start work
11. Set your availability in the team (if your team tracks it) and start working in this order: Critical → overdue follow-ups → High → New tickets by age → Medium/Low.

- [ ] Logged in with own account
- [ ] Announcements read
- [ ] Feature Status checked
- [ ] Handover note read and my inherited tickets identified
- [ ] My follow-ups for today listed
- [ ] Critical/High queue checked

## Expected Outcome
Within the first part of the shift the agent knows every urgent item, every promise falling due, and every current incident, and the queue is being worked in priority order.

## Common Mistakes
- Answering the first Telegram message that arrives before reading the handover — and contradicting what the previous agent told the customer.
- Ignoring the Feature Status page and telling a customer that Telebirr or delivery is available because "a customer said so".
- Leaving tickets in *Waiting for Customer* although the customer already replied overnight.
- Using a personal phone to call a customer back "just this once".

## Escalation
- You cannot access the support app or an official channel → **Senior Support / Supervisor** immediately; record the outage time.
- Handover mentions a Critical ticket with no owner → take it or assign it via the supervisor within your first actions.
- An announcement or Feature Status change is unclear → ask the supervisor before using it with customers.

## Related Templates
- tpl-delayed-response-apology — for customers who waited overnight or longer than usual.
- tpl-known-outage — if an incident is already announced.

## Internal Notes
- The internal response/resolution targets configured in Settings are internal goals, not customer guarantees. Overnight backlog is normal; prioritize, don't panic.
- If the previous shift left no handover note, tell your supervisor — it is a process gap that should appear in the daily report.

<!-- doc -->
# Checking and triaging new tickets
id: sop-check-new-tickets
type: sop
category: shift
audience: internal
priority: high
department: support_l1
tags: triage, new tickets, queue, assign ticket, categorize, ticket status, ትኬት መለየት, unassigned
related: sop-prioritize, sop-first-response, sop-verify-customer, sop-escalation, sop-mass-incident, pol-escalation-matrix
templates: tpl-greeting-telegram, tpl-greeting-email, tpl-request-customer-info, tpl-known-outage
policy_pending: no

## Summary
How to take a ticket from **New** to a correctly categorized, prioritized and owned ticket with the right status, so nothing sits unread in the queue.

## Objective
Every new ticket is read, understood, categorized, given a priority, linked to the right customer, owned by one agent and moved to the correct status. Triage is not about solving the issue yet — it is about making sure the right person works on the right thing first.

## When to Use
- Whenever there are tickets in status **New**.
- When you manually create a ticket from a Telegram message, email or phone call (every customer contact that needs action must become a ticket).

## Responsible
- **Level 1 agents** triage the shared queue during their shift.
- **Supervisor** re-assigns when an agent is overloaded and checks that no Critical ticket is unassigned.

## Required Information
- The customer's message(s) and attachments.
- The customer's registered email or phone number (to link the ticket to the account).
- Any reference the customer gave: transaction reference, booking/consultation ID, order ID.

## Steps
### 1. Read before you touch
1. Open the oldest **New** ticket first, unless a Critical-looking ticket is visible (subjects such as "hacked", "money taken", "session in 1 hour", "everyone can't pay" — open those first).
2. Read the full message and look at attachments. Do not decide priority from the subject line alone.

### 2. Check for duplicates and incidents
3. Search the ticket list by the customer's email/phone and by any reference they gave. If the same customer already has an open ticket for the same problem:
   - add the new message to the existing ticket's communication log, add an internal note "Duplicate of #… merged manually", and close the new one as a duplicate with a note — do not run two parallel conversations.
4. Check **Announcements** for an active incident. If the ticket matches a known incident, follow *Handling a mass incident* and use the approved wording.

### 3. Categorize
5. Set the category that matches the customer's real problem (not the words they used). Example: "I can't log in to see my booking" is a login problem, not a booking problem.
6. Link the ticket to the customer record and fill the reference fields you have (order, consultation/booking, transaction reference). These fill the placeholders in templates automatically.
7. Open the suggested knowledge base article for this category and check its **default priority** and **escalation department**.

### 4. Prioritize
8. Set priority with the matrix in *Prioritizing urgent issues*. When in doubt between two levels, choose the higher one and write why in an internal note.

### 5. Assign and set status
9. Assign the ticket to yourself (or to the agent/department the supervisor designates).
10. Set the status according to the table below.

| Status | Use it when |
|---|---|
| **New** | Nobody has looked at it yet. Never leave a ticket you have read in *New*. |
| **Open** | An agent owns it and is working on it now. |
| **Under Review** | You are checking records, policy or evidence before answering. |
| **Waiting for Customer** | You asked the customer for information and cannot continue without it. |
| **Waiting for Seller** | You contacted the seller and need their answer to continue. |
| **Escalated** | Handed to Level 2, a specialized department or management (see *Escalating issues*). |
| **In Progress** | The fix/decision is being carried out (e.g., Payments is processing an approved adjustment). |
| **Resolved** | Solution delivered and documented; customer notified. |
| **Closed** | Resolution confirmed or the closing period ended without reply. |
| **Reopened** | The customer came back with the same unresolved problem. |

### 6. First contact
11. Send the first response following *Responding to first messages*. If you need more information, use a request template and set **Waiting for Customer**, with a **follow-up** due date.
12. Write a short internal note: what the problem is, what you checked, what the next action is. Another agent must be able to continue from your note alone.

- [ ] Duplicates checked
- [ ] Incident checked in Announcements
- [ ] Category and references filled
- [ ] Priority set (with reason if Critical/High)
- [ ] Owner assigned
- [ ] Status correct
- [ ] First response sent or scheduled
- [ ] Internal note written

## Expected Outcome
No ticket stays in **New** after it has been read; every ticket has a category, a priority, an owner, a correct status and a clear next action.

## Common Mistakes
- Setting priority from the customer's tone ("URGENT!!!") rather than impact.
- Leaving a ticket *Open* while actually waiting for the customer, which hides it from follow-up tracking.
- Creating a second ticket for the same customer and the same problem.
- Choosing the category the customer named instead of the actual problem.
- Forgetting to log a phone call or Telegram message in the communication log — the app does not capture them automatically.

## Escalation
- Possible account takeover, fraud or threats → set **Critical**, follow *Handling a suspected security incident* and escalate to **Trust & Safety**.
- Many similar tickets in a short time → alert the **Supervisor** (possible mass incident).
- You cannot tell which department owns the problem → ask the **Supervisor** rather than guessing; see the *Escalation matrix* policy.

## Related Templates
- tpl-greeting-telegram, tpl-greeting-email — first contact.
- tpl-request-customer-info — when details are missing.
- tpl-known-outage — when the ticket matches an announced incident.

## Internal Notes
- Triage quality is part of the ticket quality review: wrong category and wrong priority are the most common findings.
- Customers often write in Amharic, English or a mix. Answer in the language the customer used; Amharic is the default.

<!-- doc -->
# Prioritizing urgent issues (priority matrix)
id: sop-prioritize
type: sop
category: shift
audience: internal
priority: high
department: support_l1
tags: priority, urgent, critical, priority matrix, impact, urgency, አስቸኳይ, which ticket first
related: sop-check-new-tickets, sop-security-incident, sop-mass-incident, sop-escalation, pol-service-levels, pol-escalation-matrix
templates: tpl-account-compromise-urgent, tpl-known-outage, tpl-delayed-response-apology
policy_pending: yes

## Summary
The matrix agents use to set ticket priority (Low, Medium, High, Critical) based on harm, money, time-sensitivity and number of people affected — and how to re-prioritize as a situation changes.

## Objective
Make sure the most harmful problems are handled first and consistently by every agent, regardless of how loudly a customer writes.

## When to Use
- During triage of every new ticket.
- Whenever new information arrives that changes the impact (e.g., the customer says the session is now in an hour, or a second customer reports the same problem).

## Responsible
- **Level 1 agents** set the initial priority.
- **Supervisor** may raise or lower it and must approve lowering a Critical ticket.

## Required Information
- What happened, to whom, since when.
- Whether money, account security, personal data or a scheduled session is involved.
- When the related session/booking takes place (date, time and time zone).
- How many customers are affected (check similar tickets and Announcements).

## Steps
1. Ask the four impact questions:
   - **Safety & security:** Is an account, personal data or someone's safety at risk right now?
   - **Money:** Has money moved (or failed to move) and is it unresolved?
   - **Time:** Will the harm get worse soon (a session about to start, a seller withdrawal about to be requested from a compromised account)?
   - **Scale:** Is more than one customer affected by the same thing?
2. Find the row in the matrix that matches. Use the **highest** row that applies.

| Priority | Typical situations | First action |
|---|---|---|
| **Critical** | Suspected account takeover or unauthorized withdrawal; leaked personal data or ID documents; threats to someone's safety; platform-wide outage or payment failure affecting many customers; paid session starting very soon with no confirmation or no meeting access; legal/media threat with a credible reputational risk | Handle immediately; notify Supervisor; escalate to the owning department at once |
| **High** | Money taken but booking/order not confirmed; duplicate charge; seller did not show up to a paid session; seller cannot access earnings already shown as available; buyer–seller dispute with money involved; account locked/suspended with a session or sale pending | Handle before all Medium/Low; escalate as the KB article says |
| **Medium** | Login problems with no money at risk; listing rejected; verification status questions; reschedule requests with time to spare; general complaints; seller onboarding questions | Handle in queue order |
| **Low** | How-to questions; feedback and suggestions; feature requests (e.g., "when will delivery start?"); general information | Handle when higher priorities are clear; still within internal targets |

3. Apply the modifiers:
   - **Raise one level** if the customer is vulnerable (elderly, low digital literacy, distressed), if the ticket was already **Reopened**, or if the same customer has contacted us several times about it without progress.
   - **Raise one level** if a scheduled session or deadline is close. Use the booking time in the customer's time zone.
   - **Never lower** a security or data-exposure ticket below High until Trust & Safety has confirmed it is safe.
4. Set the priority in the ticket. For Critical and High, add an internal note with the reason (e.g., "Critical: login email changed without customer's consent, seller has available balance").
5. Re-check priority every time you update the ticket. Lower it once the risk is removed (e.g., booking confirmed, account secured) and write why.
6. If several Critical tickets compete for your time, tell the **Supervisor** — they decide the order and may reassign.

## Expected Outcome
Every ticket's priority reflects real impact, Critical issues are acted on immediately, and changes in priority are explained in internal notes.

## Common Mistakes
- Treating a polite, calm message about an account takeover as Low because it "doesn't sound urgent".
- Raising everything to Critical — when everything is Critical, nothing is.
- Forgetting time zones: a customer abroad may have their session much sooner than it appears.
- Lowering priority after sending one reply although the problem is not solved.

## Escalation
- Any Critical ticket → notify **Senior Support / Supervisor** in addition to escalating to the department.
- Disagreement about priority with a colleague or department → **Supervisor** decides.
- Reputational, legal or regulatory risk → **Management (Level 4)** via the Supervisor.

## Related Templates
- tpl-account-compromise-urgent — immediate response to suspected takeover.
- tpl-known-outage — for tickets that belong to a declared incident.
- tpl-delayed-response-apology — when a high-priority ticket waited too long.

## Policy Pending Approval
- Confirm the official definition of "very soon" for sessions (the time window that makes an unconfirmed paid session Critical vs High).
- Confirm the number of similar reports that should trigger a mass-incident review.
- Confirm the internal response and resolution targets per priority (configured in Settings).
- Confirm whether a monetary threshold should automatically raise payment tickets to Critical.

## Internal Notes
- Until the windows above are approved, a common working rule is: a paid but unconfirmed session within the next 24 hours is at least High; within the next few hours it is Critical. Your supervisor may adjust this.
- Priority is about impact on the customer and on trust in Byfluence, not about who the customer is. Influencers and large sellers get the same matrix.

<!-- doc -->
# Shift handover
id: sop-handover
type: sop
category: shift
audience: internal
priority: high
department: support_l1
tags: handover, shift change, hand over tickets, next shift, ፈረቃ ማስረከብ, continuity
related: sop-start-shift, sop-end-shift, sop-follow-up, sop-mass-incident, sop-daily-report
templates: tpl-status-update, tpl-still-investigating
policy_pending: no

## Summary
How the outgoing shift hands open work to the incoming shift so that no customer promise, Critical ticket or ongoing incident is lost between shifts.

## Objective
The incoming shift can continue every open case without asking the outgoing agent anything, and customers never have to repeat their story because of a shift change.

## When to Use
- At the end of every shift where another shift follows.
- When an agent leaves mid-shift (illness, emergency) — the supervisor does the handover for them.
- Before planned leave: hand over all tickets you own.

## Responsible
- **Outgoing agent** prepares their part of the handover.
- **Outgoing Supervisor / shift lead** compiles the shift-level handover note.
- **Incoming agent/Supervisor** reads it and confirms ownership.

## Required Information
- List of tickets you own with status Open, Under Review, Waiting for Customer/Seller, Escalated, In Progress or Reopened.
- Follow-ups due in the next shift.
- Any promise you made to a customer (callback, update by a time).

## Steps
1. About the last part of your shift, filter **Assigned to me** and review every non-closed ticket.
2. For each ticket, make sure the **internal notes** are current: the problem, what was checked, what is pending, from whom, and the next action. Write it as if you will never see this ticket again.
3. Make sure every ticket waiting on someone has a **follow-up** with a due date. A ticket waiting with no follow-up will be forgotten.
4. Decide which tickets must be re-assigned:
   - **Critical/High** tickets and tickets with a follow-up or callback due during the next shift → re-assign to an incoming agent (agreed with the supervisor).
   - Tickets waiting on a department with no customer action due → can stay with you if you are back next shift; add a note.
5. Write the handover note (the format your team uses; the supervisor posts it where the team reads it). Include:
   - **Incidents:** active incidents, master ticket number, latest approved wording, last update time.
   - **Critical/High tickets:** ticket number, one-line situation, owner, next action, deadline.
   - **Promises due:** callbacks or updates promised to customers, with time and channel.
   - **Escalations waiting:** department, ticket number, when escalated, what they need.
   - **Policy questions:** cases waiting for a management decision because a policy is pending.
   - **Anything unusual:** suspected fraud patterns, angry customers likely to contact again, tooling problems.
6. Talk through Critical items verbally (or by call) with the incoming lead if possible; written notes are required but not always enough.
7. Incoming lead confirms receipt and the new owners accept their tickets in the app.

## Expected Outcome
Every open ticket has a current internal note, an owner and a follow-up where needed; the incoming shift has a single handover note listing incidents, Critical items and promises due.

## Common Mistakes
- "See chat" or "customer will reply" as the only note — useless to the next agent.
- Handing over a ticket without telling the customer's promised callback time.
- Re-assigning a ticket without telling the incoming agent.
- Keeping evidence (screenshots, receipts) on your own computer instead of attaching it to the ticket.

## Escalation
- No incoming agent arrives → the **Supervisor** decides coverage; never leave Critical tickets unowned.
- A department has not answered an escalation for longer than the internal target → note it in the handover and raise to the **Supervisor**.

## Related Templates
- tpl-status-update — send before leaving if you promised an update.
- tpl-still-investigating — when there is no news yet but the customer expects contact.

## Internal Notes
- If you promised a customer "I will update you today" and cannot, send a status update before you leave rather than letting the next agent apologize for you.
- The handover note feeds the daily report: incidents, escalations and policy gaps listed here should appear there too.

<!-- doc -->
# Ending a support shift
id: sop-end-shift
type: sop
category: shift
audience: internal
priority: medium
department: support_l1
tags: end of shift, shift end, logout, close day, የፈረቃ መጨረሻ, wrap up
related: sop-handover, sop-start-shift, sop-daily-report, pol-acceptable-use-support-tools, pol-evidence-retention
templates: tpl-status-update, tpl-still-investigating
policy_pending: no

## Summary
The checklist each agent completes before going off shift: no unanswered customer, every ticket documented, evidence stored correctly, and accounts logged out safely.

## Objective
Leave the queue in a state where nothing depends on your memory and no customer data stays on your device or in your personal accounts.

## When to Use
At the end of every shift, and before any absence longer than a short break.

## Responsible
- **Every agent**. The **Supervisor** checks that all agents completed it before the shift lead leaves.

## Required Information
- Your assigned tickets and follow-ups.
- The shift handover note format.

## Steps
1. Stop taking new tickets shortly before the end of the shift (as agreed with the supervisor) so you can finish documentation. Critical tickets are the exception — hand them over properly instead of rushing.
2. Answer or acknowledge every customer who wrote to you during the shift. If you cannot solve it, send a status update (tpl-status-update or tpl-still-investigating) and set a follow-up.
3. Check **Communication log**: every Telegram conversation, email and phone call you had today is logged on the right ticket (date, channel, summary). Nothing is recorded automatically.
4. Check statuses: nothing you have read is left in **New**; tickets waiting on customers are **Waiting for Customer**; tickets with departments are **Escalated** with a follow-up.
5. Check **Resolved** tickets from today: root cause, actions taken, final resolution and customer-notified flag are filled in.
6. Complete your part of the **Shift handover** (see that SOP).
7. Move any evidence you downloaded during the shift into the correct ticket as an attachment, then delete local copies (including Downloads, desktop and phone gallery if you used a work phone).
8. Close customer conversations in the official Telegram/email apps so they don't sit unread; log out of shared devices.
9. Log out of the support app and official channels if the workstation is shared, and lock your screen.
10. Send your shift numbers to the shift lead if your team collects them for the daily report (tickets handled, resolved, escalated, unusual items).

- [ ] Every customer contact answered or acknowledged
- [ ] Communication log complete
- [ ] Statuses and follow-ups correct
- [ ] Resolution fields complete on resolved tickets
- [ ] Handover written
- [ ] Local evidence uploaded and deleted
- [ ] Logged out / screen locked

## Expected Outcome
No customer waits without acknowledgement, the next shift can continue every case, and no customer data remains outside the support app.

## Common Mistakes
- Leaving the support Telegram account logged in on a shared computer.
- Marking tickets **Resolved** at the end of the shift just to clean the queue — never mark unresolved tickets as complete.
- Forgetting to log a phone call made in the last minutes of the shift.

## Escalation
- You cannot finish documentation of a Critical ticket before leaving → tell the **Supervisor**, who assigns it before you go.
- Something unusual happened on the shift (suspected fraud, data exposure, threat) → make sure the **Supervisor** knows before you leave, not only in writing.

## Related Templates
- tpl-status-update — final update before handover.
- tpl-still-investigating — when no news is available yet.

## Internal Notes
- End-of-shift is when quality drops. Supervisors should spot-check tickets closed in the last part of the shift during quality reviews.

<!-- doc -->
# Responding to first messages
id: sop-first-response
type: sop
category: channels
audience: internal
priority: high
department: support_l1
tags: first response, first message, greeting, acknowledge, case number, የመጀመሪያ ምላሽ, reply customer
related: sop-check-new-tickets, sop-telegram, sop-email, sop-verify-customer, com-tone-voice, com-writing-clear-messages
templates: tpl-greeting-telegram, tpl-greeting-email, tpl-request-customer-info, tpl-request-transaction-ref, tpl-delayed-response-apology, tpl-acknowledge-complaint
policy_pending: no

## Summary
How to write the first reply to a customer: greet, show you understood, give the case number, ask only what is needed, and say what happens next — without promising outcomes or timelines.

## Objective
The first reply makes the customer feel heard and safe, moves the case forward (collects exactly the information needed), and sets honest expectations.

## When to Use
- The first reply on any new ticket, on any channel.
- The first reply after a ticket is re-assigned to you (introduce yourself and confirm the situation).

## Responsible
**Level 1 agents** (or whoever owns the ticket).

## Required Information
- The customer's message and language.
- The KB article for the issue (Recommended Response and Information to Collect).
- The ticket number.

## Steps
1. **Language:** reply in the language the customer used. If they mixed Amharic and English, reply in Amharic with English technical terms in Latin script. If unclear, use Amharic and offer English.
2. **Open the KB article** for the issue. Use its Recommended Response (email) or Short Response (Telegram) as the starting point; adapt to what the customer actually said.
3. **Structure the message** in this order:
   1. Greeting with the customer's name.
   2. Thanks for contacting us (and an apology if they waited long — tpl-delayed-response-apology).
   3. One sentence that shows you understood the problem in your own words.
   4. What you need from them — numbered, maximum three or four items, only what the KB's "Information to Collect" needs.
   5. A safety line when relevant: "We will never ask for your password, PIN or verification code."
   6. The case number `{{ticket_id}}`.
   7. What happens next, without a time promise you cannot keep ("I will update you as soon as I have checked").
   8. Your name and "Byfluence Support".
4. **Check before sending:**
   - [ ] No promise of refund, approval, outcome or timeline that is not confirmed
   - [ ] No request for passwords, OTP codes, PINs, full card numbers
   - [ ] Placeholders replaced (no `{{...}}` left visible)
   - [ ] Names and amounts correct
5. **Send** on the channel the customer used, then **log it** in the communication log (channel, time, short summary). If you sent it outside the app, paste the text or summary.
6. **Set status:** *Waiting for Customer* if you asked for information (and set a follow-up), otherwise *Under Review* / *Open* while you investigate.

## Expected Outcome
Customer receives a warm, clear first reply with a case number and an exact list of what to send; the ticket status and follow-up reflect the next step.

## Common Mistakes
- Asking for information the customer already gave in their first message.
- Sending a list of eight questions; the customer answers one and the case stalls.
- "Don't worry, you will get your money back" — an unauthorized promise.
- Copying a template without adapting it, e.g., greeting "Dear seller" to a buyer.
- Forgetting the case number.

## Escalation
- The first message already shows a Critical situation (account takeover, data exposure, threat) → act first (see *Handling a suspected security incident*), reply second, using tpl-account-compromise-urgent.
- You don't know the answer and no KB article fits → acknowledge the customer, set *Under Review*, and ask the **Supervisor**; never guess.

## Related Templates
- tpl-greeting-telegram, tpl-greeting-email
- tpl-request-customer-info, tpl-request-transaction-ref
- tpl-acknowledge-complaint — when the first message is a complaint.
- tpl-delayed-response-apology — when the customer waited long.

## Internal Notes
- The first reply is where most unauthorized promises happen, out of a wish to calm the customer. Calm them with ownership and a case number instead.
- If the customer sent screenshots that show personal data of others, do not forward them; attach to the ticket only.

<!-- doc -->
# Handling Telegram conversations
id: sop-telegram
type: sop
category: channels
audience: internal
priority: medium
department: support_l1
features: support-telegram
tags: telegram, chat, voice note, telegram support, ቴሌግራም, message, screenshot telegram
related: sop-first-response, sop-verify-customer, com-telegram-etiquette, pol-communication-standards, pol-acceptable-use-support-tools
templates: tpl-greeting-telegram, tpl-request-customer-info, tpl-request-transaction-ref, tpl-status-update, tpl-issue-resolved-confirm
policy_pending: yes

## Summary
How to handle customer conversations on Byfluence's official Telegram support account: logging every exchange in the ticket, verifying identity, keeping messages short, and protecting customers from impersonators.

## Objective
Telegram is fast and informal, but every Telegram conversation must still be safe, professional, recorded in the ticket and consistent with what other channels say.

## When to Use
Any customer contact received or sent on the official Byfluence Telegram support account.

## Responsible
**Level 1 agents** rostered on Telegram; **Supervisor** for monitoring and impersonation reports.

## Required Information
- The customer's Telegram display name and username (as shown in the chat).
- The customer's registered email or phone number on Byfluence (Telegram username alone does not prove account ownership).
- The ticket number.

## Steps
### Receiving a message
1. Read the whole chat history with that customer before replying — they may have written several messages or contacted us before.
2. Search the support app for an existing ticket (by phone/email/name). If none, **create a ticket** and record the channel as Telegram.
3. Reply using tpl-greeting-telegram or the KB Short Response. Keep each message short; send one clear question at a time when the customer is struggling.

### Identity and safety
4. Ask for the registered email or phone number to link the ticket. For any account-specific detail (bookings, payments, earnings), follow *Verifying customer information and account ownership* before sharing anything.
5. Never ask for passwords, OTP codes, PINs or card numbers. If a customer sends one anyway, tell them not to share it, ask them to change it if it is a password, and delete the message from the chat if your account allows it. Record in internal notes that sensitive data was received (do not copy the value).
6. Only use the official support account. Never move the conversation to your personal Telegram, and never give your personal number.

### Voice notes, photos and files
7. Voice notes: listen fully, then summarize them in the communication log (e.g., "Voice note 1 min: says Meet link not received for booking tomorrow"). Reply in text so there is a written record; send a voice note only when the customer clearly cannot read and your team allows it.
8. Screenshots and receipts: download and **attach to the ticket**; do not keep them in your phone gallery. Verify any receipt by transaction reference, never by the image alone.

### Logging and status
9. After each exchange (or at least before you leave the chat), add an entry to the **communication log**: channel Telegram, direction (in/out), time, summary, and key details given or received.
10. Set status and follow-up as for any ticket. If the customer goes silent, follow *Following up on unresolved tickets*.
11. When resolved, send tpl-issue-resolved-confirm and complete the resolution fields.

## Expected Outcome
The customer gets short, friendly, safe answers; every Telegram exchange is visible in the ticket; no sensitive data is collected or stored in Telegram.

## Common Mistakes
- Solving the issue in Telegram but never creating or updating a ticket — the case is invisible to the team.
- Sharing booking or payment details because the Telegram name matches the customer's name.
- Sending long walls of text that do not display well on small phone screens.
- Replying with stickers or emoji-heavy messages to a complaint.

## Escalation
- Customer reports a fake "Byfluence support" account contacting them → **Trust & Safety**, priority High; warn the customer to only trust the official account listed on byfluence.com.
- Customer is abusive or threatening → see *De-escalating angry customers* and *Customers threatening legal action*; involve the **Supervisor**.

## Related Templates
- tpl-greeting-telegram, tpl-request-customer-info, tpl-request-transaction-ref
- tpl-status-update, tpl-issue-resolved-confirm

## Policy Pending Approval
- Confirm the official Telegram support account(s) customers should use and how they are published (website, app).
- Confirm whether agents may send voice notes and under which conditions.
- Confirm Telegram support hours and the approved after-hours auto-reply wording (if any).

## Internal Notes
- Telegram messages can be edited or deleted by the customer. Your communication log summary is the record — write it as you go.
- Impersonation of support accounts is a common scam pattern on Telegram. Remind customers that Byfluence support will never ask them to pay a fee to support or share codes.

<!-- doc -->
# Responding to emails
id: sop-email
type: sop
category: channels
audience: internal
priority: medium
department: support_l1
features: support-email
tags: email, mailbox, reply email, subject line, attachments, ኢሜይል, email support
related: sop-first-response, com-email-writing, pol-communication-standards, sop-verify-customer, pol-evidence-retention
templates: tpl-greeting-email, tpl-request-customer-info, tpl-status-update, tpl-issue-resolved-confirm, tpl-closing-no-response
policy_pending: yes

## Summary
How to process customer emails from the official support mailbox: one ticket per case, complete structured replies, attachments stored in the ticket, and every email logged.

## Objective
Each email gets a complete, well-structured reply that can be understood without reading the whole thread, and the support app holds the full record.

## When to Use
Any email to or from the official Byfluence support mailbox.

## Responsible
**Level 1 agents** rostered on email.

## Required Information
- Sender address (compare it with the registered account email).
- Full email thread and attachments.
- The ticket number (existing or new).

## Steps
1. **Find or create the ticket.** Search by the sender's email and by any reference in the email. Reply within the existing ticket's thread when one exists.
2. **Check the sender address.** If it differs from the registered email, treat the sender as unverified: you may give general information but not account-specific details until verified (see *Verifying customer information*).
3. **Watch for phishing signs:** attachments with unusual extensions, links asking you to log in, "urgent" requests to change payout details. Do not open suspicious attachments; forward to the Supervisor/Trust & Safety per your team's process.
4. **Download legitimate attachments** (receipts, screenshots) and attach them to the ticket; then delete local copies.
5. **Write the reply** using tpl-greeting-email or the KB Recommended Response:
   - Subject: keep the case number in the subject, e.g., "Your Byfluence support case {{ticket_id}} — payment check".
   - Greeting, thanks, one-sentence summary of the issue.
   - What you checked / what you need (numbered).
   - Next step and how you will contact them.
   - Signature: your first name, Byfluence Support.
6. **Reply to all only when appropriate.** If the customer copied other people, consider whether account details should go to them. When in doubt, reply only to the registered email.
7. **Log** the email in the communication log (direction, time, summary).
8. **Set status/follow-up** like any ticket.

## Expected Outcome
A complete, polite email in the customer's language with the case number in the subject; attachments stored in the ticket; status and follow-up set.

## Common Mistakes
- Changing the subject line and creating a new thread that the customer cannot connect to the case.
- Sending account details to a non-registered email address.
- Replying only to the last message and ignoring a question from earlier in the thread.
- Forwarding customer emails to personal addresses for "working from home".

## Escalation
- Email claims to be from a bank, payment provider, police or lawyer → do not act on it; send to the **Supervisor**, who involves **Management** or **Trust & Safety**.
- Email asks to change a seller's payout details → treat as High risk; verify and escalate to **Payments & Finance** and **Trust & Safety**.

## Related Templates
- tpl-greeting-email, tpl-request-customer-info
- tpl-status-update, tpl-issue-resolved-confirm, tpl-closing-no-response

## Policy Pending Approval
- Confirm the official support email address(es) and the approved signature format.
- Confirm whether a standard email footer (privacy notice, "we never ask for your password") must be added to every reply.

## Internal Notes
- Email customers often write once and then wait; make the first reply complete so they don't need another round.
- Long Amharic emails: keep paragraphs short; Ethiopic script in long blocks is hard to read on phones.

<!-- doc -->
# Answering phone calls
id: sop-inbound-calls
type: sop
category: channels
audience: internal
priority: medium
department: support_l1
features: support-phone
tags: phone call, inbound call, answering calls, call script, ስልክ, call log, hotline
related: sop-outbound-calls, com-phone-etiquette, sop-verify-customer, sop-first-response, com-deescalation
templates: tpl-phone-inbound-opening, tpl-verify-identity, tpl-status-update
policy_pending: yes

## Summary
How to answer an incoming customer call: opening script, verification, note-taking, confirming next steps, and logging the call in the ticket afterwards (the app does not record calls automatically).

## Objective
The caller leaves the call knowing their case number and what happens next, and the ticket contains an accurate written record of the call.

## When to Use
Every inbound call on the official Byfluence support line.

## Responsible
**Level 1 agents** rostered on the phone line.

## Required Information
- The support app open (to search and create tickets while on the call).
- The caller's name and registered phone number/email.

## Steps
1. **Answer** within a few rings using the opening script (tpl-phone-inbound-opening): greeting, "Byfluence Support", your first name, offer to help. Start in Amharic; switch to English if the caller prefers.
2. **Listen first.** Let the caller explain without interrupting. Take notes directly in a draft internal note.
3. **Identify the caller.** Ask for their full name and registered phone number or email. Search the support app for their account and existing tickets.
4. **Verify before account details.** If the caller needs account-specific information, verify ownership (tpl-verify-identity; see *Verifying customer information*). Never ask for passwords, OTP codes or PINs — not even "to check".
5. **Summarize back** the problem in one or two sentences: "So, you paid on [date] and the booking still shows pending — is that right?"
6. **Resolve or route:**
   - If you can solve it on the call (how-to, guidance), do it step by step and check the customer can follow on their phone.
   - If you need to investigate, explain that you will check and contact them, and agree on **channel** (call back, Telegram, email) and a realistic follow-up — not a promised outcome.
   - If the caller needs to send evidence (receipt screenshot), tell them exactly where to send it (official Telegram or email) and to include the case number.
7. **Give the case number** slowly, digit by digit, and ask them to write it down. Offer to send it by Telegram/email as well.
8. **Close the call:** ask "Is there anything else I can help with?", thank them, and end politely.
9. **Immediately after the call**, create/update the ticket:
   - communication log entry: channel Phone, inbound, time, duration, summary, what was agreed;
   - internal note with details collected;
   - status and follow-up (callback time agreed with the customer).
10. If the call dropped, try to call back once from the official line (see *Calling customers*) and log the attempt.

## Expected Outcome
Every call has a ticket with a written summary; the caller knows the case number and the next step; any callback is scheduled as a follow-up.

## Common Mistakes
- Not creating a ticket because "it was just a quick call" — the next agent has no record.
- Reading account details to a caller who has not been verified.
- Promising "I'll call you back in an hour" and not scheduling a follow-up.
- Talking over an angry caller.
- Spelling IDs and emails too fast for the customer to write down.

## Escalation
- Caller reports a security incident or fraud in progress → treat as **Critical**; follow *Handling a suspected security incident*.
- Caller is abusive after de-escalation attempts → you may end the call politely after a warning; inform the **Supervisor** and log it.
- Caller asks for a supervisor → offer a Level 2 callback (or transfer if available); log the request.

## Related Templates
- tpl-phone-inbound-opening — opening script.
- tpl-verify-identity — verification questions.
- tpl-status-update — follow-up message after the call.

## Policy Pending Approval
- Confirm the official support phone number(s) and hours.
- Confirm whether calls are recorded and the approved disclosure wording if they are.
- Confirm whether call transfer to Level 2 is technically available or callbacks only.

## Internal Notes
- Many callers phone because they struggle with text or apps. Be patient; offer to stay on the line while they try a step.
- If the caller is using a different phone from the registered number, treat them as unverified until checked.

<!-- doc -->
# Calling customers
id: sop-outbound-calls
type: sop
category: channels
audience: internal
priority: medium
department: support_l1
features: support-phone
tags: outbound call, call customer, callback, call seller, ደውሎ ማነጋገር, phone follow-up, missed call
related: sop-inbound-calls, com-phone-etiquette, sop-follow-up, sop-verify-customer, pol-communication-standards
templates: tpl-phone-outbound-intro, tpl-status-update, tpl-satisfaction-followup
policy_pending: yes

## Summary
When and how agents phone customers or sellers: from the official line only, with a clear purpose, without asking for sensitive data, and with every attempt logged in the ticket.

## Objective
Use phone calls when they genuinely speed up a resolution (urgent sessions, confusing cases, low digital literacy, promised callbacks) while protecting customers from impersonation and protecting the agent's personal number.

## When to Use
- A callback was promised or requested.
- The issue is urgent and written messages are not getting answered (e.g., a session soon and the seller has not confirmed).
- The customer struggles with written communication.
- A seller must be contacted about a dispute or no-show (when the escalation process allows support to contact sellers).

## Responsible
**Level 1 agents**; **Senior Support** for sensitive calls (disputes with money involved, complaints threatening legal action).

## Required Information
- The ticket and its latest internal notes.
- The phone number registered on the account (call only that number unless the customer gave another one in writing on the ticket).
- The purpose of the call and what you need to say/ask.

## Steps
1. **Prepare:** read the ticket, write down the purpose and the two or three points you must cover. Have the case number ready.
2. **Call from the official support line only.** Never use your personal phone, and never give your personal number.
3. **Introduce yourself** with tpl-phone-outbound-intro: your name, Byfluence Support, the reason for the call, the case number. Ask if it is a good time to talk.
4. **Verify** the person if you will discuss account details (*Verifying customer information*). Remind them: "We will never ask for your PIN, password or code."
5. **Deliver the update or questions.** Keep to the purpose. Summarize what was agreed at the end.
6. **If there is no answer:** do not leave account details on voicemail. Leave at most: your first name, Byfluence Support, the case number, and that you will also write to them. Then send a short message on Telegram/email (tpl-status-update).
7. **Log every attempt** in the communication log (answered/no answer/wrong number, time, summary).
8. **Retry policy:** if unanswered, try again at a different time of day before concluding no contact. Follow *Following up on unresolved tickets* for the overall number of attempts.
9. **Update the ticket** status and follow-ups after the call.

## Expected Outcome
The call achieved its purpose (or attempts are documented), the customer received a written summary, and the ticket shows what happened.

## Common Mistakes
- Calling late in the evening or very early — respect reasonable hours.
- Leaving detailed account or payment information on voicemail or with a family member.
- Calling a seller to "tell them off" on behalf of a buyer; you are a neutral facilitator.
- Not logging unanswered attempts, which makes closure for no-response unjustifiable later.

## Escalation
- During the call the customer reveals fraud, threats or a security issue → **Trust & Safety** (Critical if ongoing).
- The seller refuses to cooperate in a dispute → **Senior Support / Supervisor**, then **Seller Operations**.

## Related Templates
- tpl-phone-outbound-intro — call opening.
- tpl-status-update — written summary after the call or after a missed call.
- tpl-satisfaction-followup — post-resolution check by phone.

## Policy Pending Approval
- Confirm acceptable calling hours for customers and sellers.
- Confirm whether support agents may call sellers directly in disputes, or only Seller Operations.
- Confirm the number of call attempts required before a ticket can be closed for no response.

## Internal Notes
- Customers are increasingly warned about scam calls. If the customer is suspicious, encourage them to contact Byfluence through the official channels listed on byfluence.com and quote the case number — that is a good outcome, not a failure.
