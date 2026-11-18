<!-- module -->
# Ticket Management
id: trn-08
number: 8
duration: 75

## Learning Objectives
- Decide when a contact needs a ticket and create one completely: customer info, channel, category, priority and references.
- Choose a ticket priority using impact and urgency, and adjust it when the situation changes.
- Move a ticket through all ten statuses correctly and explain what each status tells the next agent.
- Use the timeline, internal notes, communication log and follow-ups so that any colleague can continue the case without asking you.
- Escalate through the Escalation Center to the correct level and department with an escalation note that needs no follow-up questions.
- Resolve and close tickets only when root cause, actions, resolution and customer notification are recorded, and reopen correctly when a problem returns.

## Lesson

### Why tickets matter
A ticket is Byfluence's memory of a customer's problem. It protects the customer (nothing is forgotten), protects you (your actions are recorded), and teaches the business (root causes show which policies and features need work). The Accountability principle lives in the ticket.

Create a ticket whenever a contact needs **investigation, a follow-up, an escalation, or any account-specific check**. A simple general question answered completely from an FAQ may not need one — follow your supervisor's rule for logging quick questions. When in doubt, create the ticket.

### Creating a ticket
Use **Tickets → Create issue**.

| Field | What to enter | Common mistake |
|---|---|---|
| Customer info | Name, registered email/phone, buyer/seller, preferred language | Using the Telegram display name instead of the account name |
| Channel | Where the contact came from (Telegram, email, phone, website) | Leaving it blank — the next agent doesn't know where to reply |
| Category / subcategory | The Knowledge Base category that matches the issue | Choosing "General" for everything |
| Priority | See priority guide below | Leaving every ticket at Medium |
| Subject / description | One-line summary + the customer's problem in their own words | "Customer has issue" |
| References | Order ID, consultation/booking ID, transaction reference | Putting references only in the description, so they aren't searchable |

> [!TIP] The reference fields feed the template placeholders: transaction reference → `{{transaction_id}}`, consultation reference → `{{consultation_id}}`, order reference → `{{order_id}}`, ticket number → `{{ticket_id}}`. Filling them once saves time on every reply.

Before creating, **search** for an existing ticket by customer email/phone or reference. A customer who writes three times should have one ticket with three contacts in the communication log, not three tickets.

### Priority guide
| Priority | Use when | Examples |
|---|---|---|
| **Critical** | Money or account at active risk, a session is happening now and can't proceed, a safety threat, or a widespread incident | Account takeover with payout changes; session starting and no link; threat of harm; many customers can't pay |
| **High** | Significant impact soon or financial harm already happened | Paid but not confirmed with session soon; duplicate charge; seller suspended with bookings today |
| **Medium** | Real problem without immediate deadline | Verification pending; withdrawal question; session next week with wrong time |
| **Low** | Information requests, minor inconvenience | How to edit profile; general feature question |

Priority is not fixed. Raise it when a deadline approaches or the customer's situation worsens; record why in an internal note.

> [!NOTE] Official response-time targets (SLAs) for each priority are not part of this training. Follow the targets your supervisor publishes in SOPs or Announcements.

### The ten statuses
| Status | Meaning | Typical next step |
|---|---|---|
| **New** | Created, not yet picked up | Agent takes ownership → Open |
| **Open** | An agent is working on it | Investigate, reply, decide |
| **Under Review** | Being checked internally (by you or a senior) before a response or decision | → In Progress, Escalated or Waiting… |
| **Waiting for Customer** | You need information or confirmation from the customer | Customer replies → Open/In Progress; set a follow-up |
| **Waiting for Seller** | You need the seller's response | Seller replies → Open/In Progress; set a follow-up |
| **Escalated** | Handed to a higher level or specialised department | Department responds → In Progress |
| **In Progress** | Active work toward resolution (e.g., department fixing it) | → Resolved |
| **Resolved** | Solution delivered and recorded; customer notified | Customer confirms or no further issue → Closed |
| **Closed** | Final; no further action | Problem returns → Reopened |
| **Reopened** | A resolved/closed case has the same problem again | Back to active handling |

On the **Kanban view** each status is a column — drag cards as work moves and use it in team huddles to see where tickets are stuck (e.g., many cards in Waiting for Seller). The **table view** is better for sorting by priority, filtering by category or searching by reference.

### Timeline, internal notes and communication log
These are three different tools:

- **Timeline** — the automatic history of the ticket: status changes, priority changes, assignments, escalations. You don't write it; you read it to understand what happened.
- **Internal notes** — agent-only. Record findings and reasoning: "Verified ref via admin dashboard: Successful 10:42. Booking still pending. Escalating to Payments." Never paste passwords, codes or full card data — and never write anything you wouldn't want a colleague or auditor to read.
- **Communication log** — every contact with the customer or seller: channel, direction (inbound/outbound), date and a short summary or the message sent.

> [!WARNING] **Nothing is sent automatically.** The support app does not message customers. You send the reply in Telegram, email or by phone, then log it. An unlogged reply means the next agent may contact the customer again with the same question — or think nobody replied.

### Follow-ups
Whenever a ticket is waiting — on the customer, the seller or a department — add a **follow-up** with the date/time and what to check. When it comes due, it appears on your Dashboard. Follow-ups are how you keep the promise "we will update you": even "no news yet, still being reviewed" is an update. If you tell a customer `{{follow_up_time}}`, the follow-up in the app must match it.

### Escalation
Open the **Escalation Center** or use the escalate action on the ticket.

| Level | Who | Escalate when |
|---|---|---|
| 1 | Customer Support | (You) routine questions, guidance, basic troubleshooting |
| 2 | Senior Support / Supervisor | Complex complaints, buyer–seller disputes, repeated unresolved issues, refund recommendations, Policy Pending Approval decisions, you lack access |
| 3 | Specialized Department | **Payments & Finance** (verification, duplicates, refunds processing, payouts) · **Technical** (bugs, outages, booking errors, Meet links, notifications) · **Seller Operations** (verification review, listing review, seller restrictions) · **Trust & Safety** (fraud, compromise, harassment, privacy incidents) · **Logistics** (delivery — planned) |
| 4 | Management | Critical decisions, policy exceptions, legal or regulatory matters, high-value or reputational issues |

A good escalation note answers, without anyone needing to ask you:
1. **What** the customer needs (one sentence)
2. **Facts** verified, with references
3. **What you already did** and its result
4. **Why** you are escalating (policy pending, no access, needs a decision, suspected fraud)
5. **Urgency** — deadline such as a session time
6. **Customer language** and channel

Escalating does not end your ownership of the customer relationship unless your SOP says so: you still keep the customer updated and the communication log current.

### Resolving
To mark a ticket **Resolved**, the app requires:
- **Root cause** — e.g., "provider callback delay", "customer used a different email", "seller set availability in the wrong time zone". Avoid "unknown" unless it truly is, and say why.
- **Actions** — what was done, by whom.
- **Resolution** — the outcome for the customer.
- **Customer notified** — confirm you told the customer, with a log entry for that message.

A ticket is resolved when the customer's problem is solved or a final decision has been communicated — **not** when you have merely escalated it.

### Closing and reopening
Close a resolved ticket when the customer has confirmed, or when your team's closing rule applies (for example, no reply after a resolution message). The exact waiting period before closing is set by your supervisor's SOP — do not invent one, and never close a ticket to improve your numbers. If the **same** problem returns, **reopen** the ticket (status Reopened) so the history stays together. A **new, unrelated** problem gets a new ticket, referenced in the notes.

### Quality checklist before you leave a ticket
- [ ] Customer info and preferred language correct
- [ ] Category, subcategory and priority correct
- [ ] All references in the reference fields
- [ ] Every contact in the communication log
- [ ] Internal note says what you found and what happens next
- [ ] Status matches reality; follow-up set if waiting
- [ ] Escalation note complete (if escalated)

## Realistic Examples

### Example 1: Creating a complete ticket (Amharic customer)
**Customer (Telegram):**
> ሁለት ጊዜ ተቆርጦብኛል! ለአንድ ምክክር ሁለት ጊዜ ከፈልኩ።

*(I was charged twice! I paid twice for one consultation.)*

**Ticket:** Channel Telegram · Category Payments → Paid but Not Confirmed / Wrong Amounts · Priority High · Consultation reference filled · Transaction reference: first ref in the field, second in internal notes · Status Open → after asking for references: Waiting for Customer + follow-up · after verification: Escalated to Payments & Finance with a full note.

### Example 2: A weak vs. strong escalation note
**Weak:** "Customer payment problem pls check urgent."

**Strong:** "Buyer requests booking confirmation. Transaction ref (in field) verified Successful in admin dashboard at payment time; booking (consultation ref field) still pending. Session is tomorrow morning Addis Ababa time. Already: confirmed identity, checked no duplicate. Need: Payments to confirm booking manually. Customer prefers Amharic, Telegram."

### Example 3: Resolution record
**Root cause:** Seller set availability in a different time zone; buyer booked a slot shown at the wrong local time.
**Actions:** Explained time zones to buyer; Seller Operations helped seller correct availability; Senior Support approved re-booking.
**Resolution:** Buyer re-booked; new session confirmed and Meet details received.
**Customer notified:** Yes — Telegram message logged.

### Example 4: Reopen or new ticket?
A buyer whose missing-link ticket was resolved writes the next week: "The link is missing again for my new booking." Same problem, different booking → your team rule decides; the safe choice is **reopen** if it is the same root cause still unfixed (and tell Technical it recurred), or a **new ticket referencing the old one** if it is a fresh occurrence. Either way, mention the earlier ticket number in the notes.

## Practical Exercises
1. **Full lifecycle.** Create a practice ticket for Example 1. Move it through New → Open → Waiting for Customer → Open → Escalated → In Progress → Resolved → Closed, adding the right note, log entry or follow-up at each step. Then view it in both table and Kanban views.
2. **Escalation note.** Write an escalation note to Trust & Safety for a seller who reports an unrequested payout. Swap with a colleague: can they act on it without asking you a single question?
3. **Resolution fields.** For three trainer-provided closed cases, write the root cause, actions, resolution and customer-notified fields. Avoid vague root causes.
4. **Kanban review.** Open the Kanban view for the training queue. Identify tickets in Waiting for Customer or Waiting for Seller without a follow-up, and add one to each.
5. **Priority sorting.** Your trainer gives you eight new tickets. Assign priority to each and justify it in one line. Then re-prioritise two of them after the trainer adds a new fact (e.g., "the session is in one hour").

## Knowledge Check
Q: You replied to a customer on Telegram. What must you do in the ticket?
- [x] Add the contact to the communication log
- [ ] Nothing; the app sends replies automatically
- [ ] Add it to the timeline manually
- [ ] Close the ticket
> The app sends nothing; agents log every contact manually.

Q: Which fields are required to mark a ticket Resolved?
- [ ] Priority and channel only
- [ ] A refund amount
- [x] Root cause, actions, resolution and confirmation that the customer was notified
- [ ] Only the resolution text
> Resolution requires all four so the case is fully documented.

Q: You asked the customer for a transaction reference. Which status and action fit?
- [x] Waiting for Customer, with a follow-up set
- [ ] Resolved, no follow-up
- [ ] Escalated
- [ ] Closed
> Waiting statuses should always have a follow-up so the case isn't forgotten.

Q: A customer's problem returns after the ticket was closed — same issue, same booking. What do you do?
- [ ] Create a completely new ticket and ignore the old one
- [ ] Tell the customer to wait and see
- [x] Reopen the ticket so the history stays together
> Reopened keeps the full history for the same problem.

Q: Which escalation level handles policy exceptions and legal or reputational matters?
- [x] Level 4 — Management
- [ ] Level 1 — Support
- [ ] Level 2 — Senior Support / Supervisor
- [ ] Level 3 — Specialized Department
> Management handles critical decisions, policy exceptions, legal/regulatory and high-value or reputational issues.

Q: Where should the transaction reference go?
- [x] In the transaction reference field, so it is searchable and fills {{transaction_id}}
- [ ] Only in the description text
- [ ] In the communication log
> Reference fields make tickets searchable and feed template placeholders.

Q: What is the difference between internal notes and the communication log?
- [ ] They are the same thing
- [ ] Internal notes are visible to customers
- [x] Internal notes record agent findings and reasoning; the communication log records contacts with the customer or seller
> Internal notes are agent-only analysis; the communication log is the record of contacts.

Q: Which ticket deserves Critical priority?
- [ ] A seller asking how to edit their profile picture
- [x] A seller reporting their payout details were changed without their consent and a withdrawal is pending
- [ ] A verification pending question
> Active financial and account risk is Critical.

Q: You escalated a ticket to Payments & Finance. Is it resolved?
- [x] No; it is resolved only when the problem is solved or a final decision is communicated and recorded
- [ ] Yes, escalation completes your work
> Escalation is a handoff, not a resolution.

Q: A customer writes for the third time about the same payment. What is correct?
- [ ] Create a third ticket
- [ ] Ignore the message since the ticket is already escalated
- [x] Find the existing ticket, add the contact to its communication log and update the customer
> One problem, one ticket. Search by email, phone or reference before creating.
