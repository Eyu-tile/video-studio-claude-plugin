<!-- doc -->
# Verifying customer information and account ownership
id: sop-verify-customer
type: sop
category: investigation
audience: internal
priority: high
department: support_l1
features: accounts
tags: verify identity, account ownership, verification, identity check, ማንነት ማረጋገጥ, who is calling, account holder
related: pol-customer-verification, sop-security-incident, sop-telegram, sop-inbound-calls, pol-data-privacy
templates: tpl-verify-identity, tpl-request-customer-info, tpl-account-compromise-urgent
policy_pending: yes

## Summary
The interim procedure agents use to confirm that the person contacting support is the account holder before sharing or changing anything account-specific — without ever asking for passwords, OTP codes or PINs.

## Objective
Protect customers' accounts, money and data from social engineering, while still helping genuine customers quickly. The rule is simple: **no verification, no account-specific information or changes.**

## When to Use
Before you:
- share any account-specific detail (bookings, orders, payments, earnings, registered contact details, verification status);
- change anything or request a change on the customer's behalf (email/phone change, cancellation, reschedule, payout-related requests);
- discuss a dispute or refund about a specific transaction.

General information (how bookings work, how to reset a password using the website) needs no verification.

## Responsible
- **Level 1 agents** perform the standard check.
- **Senior Support / Supervisor** decides doubtful cases.
- **Trust & Safety** handles suspected impersonation or takeover.

## Required Information
Collect only what you need. Possible verification factors (use those available in your tools):
- Registered email address or phone number on the account.
- Contact coming **from** the registered email address or phone number.
- Details only the account holder is likely to know: a recent booking/consultation (seller name, date), recent order, amount of a recent payment, transaction reference from their receipt.
- For sellers: the name on the seller profile and a recent listing or booking.

> [!WARNING] Never ask for passwords, OTP/verification codes, PINs, mobile-money PINs, full card numbers or CVV. Never ask the customer to "read the code we just sent". Real Byfluence staff never need these.

## Steps
1. **Decide whether verification is needed** (see When to Use). If not, help with general information.
2. **Check the contact channel:**
   - Email from the registered address, or call/Telegram from the registered phone number → one factor matched.
   - Different email/phone → no factor yet; continue carefully.
3. **Ask for identifying details** using tpl-verify-identity: full name and registered email/phone, plus **two** account-specific details from the list above. Ask open questions ("Which consultation did you book most recently?") rather than leading ones ("Was it with Abebe on Monday?").
4. **Compare** the answers with what you see in the admin tools you are authorized to use. Do not reveal what is on file while checking ("That doesn't match the email we have" is fine; "We have abebe@… on file" is not).
5. **Decide:**
   - **Verified** (channel matches + details match) → continue; add internal note "Verified: [factors used]" (never copy the full details again).
   - **Partially matched** → share nothing account-specific; give general guidance; ask for the missing factor or ask them to contact us from the registered email/phone.
   - **Failed or suspicious** (wrong answers, pressure, urgency to change contact/payout details, story keeps changing) → do not proceed; set priority High; escalate to **Senior Support** or **Trust & Safety** per *Handling a suspected security incident*.
6. **Requests to change email, phone or payout details** always need the full check and must be escalated as the KB article for that request says; Level 1 does not approve these alone.
7. **Third parties** (family member, assistant, "my friend's account"): do not share account details. Ask the account holder to contact us directly. Exception cases (e.g., a customer who cannot communicate) go to the Supervisor.
8. **Record** in an internal note which factors were checked and the result. Never record passwords or codes; if a customer sent one, note "customer sent a code — not used, advised to change password".

## Expected Outcome
Account-specific information is only shared with or changed for verified account holders; every verification decision is documented in the ticket.

## Common Mistakes
- Treating a matching Telegram display name as proof of identity.
- Reading the registered email or phone number out to the caller "to check it".
- Accepting a screenshot of the account page as proof (screenshots can be faked or stolen).
- Skipping verification because the customer is angry or in a hurry — urgency is a classic social-engineering tactic.
- Verifying once and then accepting changes requested from a different channel later without re-checking.

## Escalation
- Failed verification combined with a request to change contact/payout details → **Trust & Safety**, priority High or Critical.
- Customer cannot pass verification because they lost access to their email/phone → **Senior Support / Supervisor** (account recovery process).
- Legal/police requests for customer data → do not answer; **Management**.

## Related Templates
- tpl-verify-identity — verification questions.
- tpl-request-customer-info — collecting the details.
- tpl-account-compromise-urgent — if verification reveals a possible takeover.

## Policy Pending Approval
- Approve the official verification factors and how many are required for (a) sharing information, (b) changing contact details, (c) payout-related requests.
- Decide the account recovery process for customers who lost access to both registered email and phone.
- Decide whether identity documents may be requested from buyers for recovery, and who reviews them.
- Decide rules for authorized representatives (businesses with several staff, family members).

## Internal Notes
- Until the verification standard is approved, apply the interim rule above (registered channel + two account-specific details) and escalate any doubt to the Supervisor.
- See the policy *Customer identity verification standard* for the full rule set.

<!-- doc -->
# Investigating payment issues
id: sop-payment-investigation
type: sop
category: investigation
audience: internal
priority: high
department: payments
features: payments-chapa, payments-telebirr, payments-mpesa, payments-bank, payments-card
tags: payment problem, payment failed, money deducted, duplicate charge, transaction reference, ክፍያ, payment pending, reconciliation
related: pay-paid-booking-not-confirmed, sop-verify-customer, sop-refund-requests, sop-escalation, pol-operational-safety-rules, pol-escalation-matrix
templates: tpl-request-transaction-ref, tpl-payment-investigation, tpl-status-update, tpl-still-investigating
policy_pending: yes

## Summary
The standard investigation for any payment complaint — failed payment, money deducted without confirmation, pending payment, duplicate charge, wrong amount — from collecting the transaction reference to escalating to Payments & Finance with a complete case.

## Objective
Establish the facts about a payment (what the customer paid, what Byfluence recorded, what the provider shows) without ever marking a payment as successful or promising a refund before it is verified by authorized personnel.

## When to Use
- Customer says money was deducted but the booking/order is not confirmed.
- Payment shows as Pending, Failed or Canceled but the customer believes it succeeded.
- Customer was charged twice or the wrong amount.
- Seller says a buyer paid but the earnings do not appear.

## Responsible
- **Level 1** collects information and checks records they have access to.
- **Payments & Finance** verifies with the payment provider and decides corrections.
- **Senior Support** if Level 1 lacks access or the case is disputed.

## Required Information
- Customer name and registered email/phone (verified — see *Verifying customer information*).
- What was being paid for (consultation/booking ID, order ID, listing name, seller name).
- Payment method used (only methods shown as live on the Feature Status page should exist; note it anyway if the customer names another).
- Date and time of payment (and the customer's time zone).
- Amount paid.
- Transaction reference from the provider's SMS or receipt.
- Screenshot of the receipt or SMS (supporting evidence only).

> [!WARNING] Never ask for PINs, passwords, OTP codes, full card numbers or CVV. A transaction reference and a receipt are enough.

## Steps
1. **Verify the customer** before discussing any transaction details.
2. **Collect the information above** with tpl-request-transaction-ref. Set *Waiting for Customer* with a follow-up if needed.
3. **Check Byfluence records** through authorized tools (admin dashboard, if you have access):
   - Find the booking/order and its status.
   - Find the payment record by transaction reference, amount and time; note its status (Pending, Successful, Failed, Canceled, Refund Pending, Refunded, Disputed).
   - Check for other payments by the same customer around that time (duplicates).
4. **Classify the case:**

| What you find | Meaning | Next action |
|---|---|---|
| Payment **Successful**, booking/order confirmed | Records are fine; customer may be looking in the wrong place | Guide the customer to their dashboard; resolve |
| Payment **Successful**, booking/order not confirmed | Confirmation step failed | Escalate to Payments & Finance (High; Critical if session very soon) |
| Payment **Pending** | Provider has not confirmed yet | Explain it is being verified; escalate if it stays pending beyond the internal threshold |
| Payment **Failed/Canceled**, customer says money left account | Possible temporary hold or reversal in progress at the provider | Escalate to Payments & Finance with reference; do not tell the customer the money "will come back" unless Payments confirms |
| **Two successful payments** for one booking | Possible duplicate charge | Escalate to Payments & Finance |
| **No record** of the reference | Wrong reference, other account, other merchant, or fraud | Re-check reference with customer; check other accounts they may use; escalate if still missing |
| Reference belongs to another account or receipt looks edited | Fraud signal | Escalate to Trust & Safety; do not accuse the customer |

5. **Never** change a payment status, confirm a booking manually, or tell the customer the payment is successful unless the records show it as Successful or Payments & Finance confirmed it.
6. **Escalate** to Payments & Finance with a complete package: customer, booking/order ID, transaction reference, amount, method, time, what Byfluence shows, what the customer shows, your classification, and the urgency (session date/time).
7. **Update the customer** with tpl-payment-investigation: we are verifying with our payments team; case number; no promised timeline (use `{{estimated_resolution_time}}` only if Payments gave approved wording).
8. **Follow up** on the escalation per *Following up on unresolved tickets*; set status **Escalated**.
9. When Payments & Finance decides, communicate the outcome exactly as they confirmed it and complete the resolution fields.

## Expected Outcome
A documented, verified picture of the payment, escalated with all evidence; the customer is informed honestly without unverified promises.

## Common Mistakes
- Accepting a receipt screenshot as proof of payment.
- Telling the customer "the money will be returned automatically" without confirmation.
- Confusing a seller's Pending Balance with a payment problem — a successful customer payment does not mean the seller's balance is immediately withdrawable.
- Escalating with "customer says they paid" and no reference, amount or time.

## Escalation
- Payment verification, duplicate charges, refunds and reversals → **Payments & Finance**.
- No access to payment records → **Senior Support / Supervisor**.
- Fraud signals → **Trust & Safety**.
- Many customers with the same payment failure → **Supervisor** + **Technical** (possible mass incident).

## Related Templates
- tpl-request-transaction-ref — ask for the reference.
- tpl-payment-investigation — "we are verifying".
- tpl-status-update, tpl-still-investigating — follow-ups.

## Policy Pending Approval
- Confirm which payment methods are live (also shown on the Feature Status page).
- Confirm the approved wording for how long payment verification and reversals usually take.
- Confirm who may manually confirm a booking/order after payment verification.
- Confirm the threshold after which a Pending payment must be escalated.

## Internal Notes
- Most "paid but not confirmed" cases are delayed provider confirmations. Most "failed but deducted" cases are holds reversed by the provider — but only Payments may tell the customer so.
- Always record the transaction reference in the ticket's reference field so placeholders fill correctly.

<!-- doc -->
# Handling a suspected security incident or account takeover
id: sop-security-incident
type: sop
category: investigation
audience: internal
priority: critical
department: trust_safety
features: accounts, seller-withdrawals
tags: hacked, account takeover, compromised account, unauthorized access, phishing, security incident, አካውንቴ ተጠልፏል, data leak, scam
related: sop-verify-customer, sop-prioritize, sop-escalation, pol-operational-safety-rules, pol-data-privacy, pol-evidence-retention
templates: tpl-account-compromise-urgent, tpl-verify-identity, tpl-escalation-notification, tpl-status-update
policy_pending: yes

## Summary
What to do immediately when a customer reports their account was taken over, someone used it without permission, they were phished, or when you notice personal data or documents may have been exposed.

## Objective
Contain the harm quickly (protect money, earnings and data), get Trust & Safety involved immediately, preserve evidence, and never let an attacker use support to finish the takeover.

## When to Use
- "My account was hacked / someone changed my email or phone / I can't log in and see bookings I didn't make."
- Unauthorized bookings, purchases or withdrawal requests.
- Customer shared a code or password with someone pretending to be Byfluence.
- Fake Byfluence support accounts, phishing links or messages.
- Suspected exposure of customer data or uploaded documents (including by staff mistake).

## Responsible
- **Level 1**: immediate steps 1–6 and documentation.
- **Trust & Safety**: investigation, account protection actions, decisions.
- **Payments & Finance**: holds or reviews on withdrawals/payments.
- **Supervisor**: informed of every case; involves **Management** for data exposure.

## Required Information
- Reporter's name and registered email/phone (and the contact they are using now).
- What happened and when (first noticed, last legitimate login if known).
- What changed: email, phone, password, payout details, listings, bookings, withdrawals.
- Any suspicious messages, links or caller numbers (screenshots).
- Whether they shared a password or code, with whom, through which channel.

> [!WARNING] Never ask the customer for their password or code "to check". Never read out the registered email/phone to the reporter — the reporter may be the attacker.

## Steps
### Immediate (first minutes)
1. Set the ticket to **Critical** and status **Escalated** once step 5 is done. Notify the **Supervisor**.
2. Send tpl-account-compromise-urgent: acknowledge, case number, advise them to use the official password reset on the Byfluence login page (if available to them), not to share codes with anyone, and to check their email/phone provider security too.
3. Do **not** share any account details with the reporter until verified. If the account's contact details were changed by the attacker, verification may fail — that is expected; note it and let Trust & Safety decide.
4. Ask the reporter the Required Information questions. Collect screenshots of phishing messages/links (ask them not to click links again).
5. **Escalate to Trust & Safety** immediately with: account, what changed, timeline, evidence, whether earnings/withdrawals or payments are at risk. If the account is a seller with available balance or a pending withdrawal, also notify **Payments & Finance** that a review/hold may be needed — only they decide.

### Protect and document
6. Do not take destructive actions yourself (deleting the account, removing listings, cancelling bookings) — confirm every destructive action with Trust & Safety first.
7. Attach all evidence to the ticket. Record in internal notes: timeline, what the customer reported, what you observed in records, who you notified and when.
8. If other customers may be affected (same phishing message, fake support account), tell the **Supervisor** — it may become a mass incident and need an Announcement.

### Follow-up
9. Keep the customer updated (tpl-status-update) and follow Trust & Safety's instructions about what may be said.
10. After Trust & Safety confirms the account is secured, help the customer review their bookings, orders and payments. Any money disputes go through *Investigating payment issues* / *Handling refund requests*.
11. Resolve only when Trust & Safety confirms closure; record root cause (e.g., phishing via fake Telegram account), actions taken and final resolution.

### If the exposure was caused by staff
12. If customer data or documents were sent to the wrong person or shared incorrectly by a Byfluence team member (including you), report it to the **Supervisor** at once. Do not try to hide or quietly fix it — fast reporting limits the harm. Management decides on customer notification.

## Expected Outcome
Trust & Safety is involved immediately, money and data at risk are flagged to the right teams, evidence is preserved, and no information leaks to an attacker through support.

## Common Mistakes
- Changing the account email to the "new" one the reporter gives — this can complete the takeover.
- Treating it as a normal login problem and sending password-reset instructions only.
- Delaying escalation until the customer sends all screenshots.
- Discussing the case in public channels or group chats.

## Escalation
- Every case → **Trust & Safety** (Level 3), Critical, and the **Supervisor**.
- Earnings, payments or withdrawals at risk → also **Payments & Finance**.
- Data exposure affecting several customers, staff involvement, or legal/regulatory implications → **Management (Level 4)** via the Supervisor.
- Platform vulnerability suspected (bug that exposed data) → **Technical** via Trust & Safety.

## Related Templates
- tpl-account-compromise-urgent — first response.
- tpl-verify-identity — verification.
- tpl-escalation-notification — telling the customer a specialist team is handling it.
- tpl-status-update — updates.

## Policy Pending Approval
- Define who may lock, freeze or restore a compromised account and the steps for restoration.
- Define whether and when seller withdrawals are paused during a takeover investigation.
- Define the data-breach notification process (who decides, which customers are told, what wording, any legal obligations).
- Define the official recovery process when the attacker changed both email and phone.

## Internal Notes
- Fraud pattern: attacker contacts support "urgently" to change the email or payout account, often claiming to be travelling or to have lost their phone. Slow down; escalate.
- Fake support accounts often ask victims to "verify" by sending a code. Educate customers kindly — they are victims, not at fault.

<!-- doc -->
# Handling refund requests
id: sop-refund-requests
type: sop
category: resolution
audience: internal
priority: high
department: payments
features: refunds
tags: refund, money back, cancel and refund, refund request, ገንዘብ ተመላሽ, chargeback, refund status
related: pol-refunds-cancellations, sop-payment-investigation, sop-buyer-seller-disputes, sop-escalation, pol-policy-pending-procedure, pol-consultation-attendance
templates: tpl-refund-request-ack, tpl-request-transaction-ref, tpl-escalation-notification, tpl-status-update, tpl-acknowledge-complaint
policy_pending: yes

## Summary
How to receive, document and route a refund request while the official refund policy is not yet approved: collect facts and evidence, never approve or promise a refund, and escalate to authorized personnel for a decision.

## Objective
Every refund request is captured completely and consistently so that authorized personnel can decide quickly and fairly, and the customer receives honest communication with no unauthorized promise of amount, eligibility or timeline.

## When to Use
- A buyer asks for their money back for any reason (seller no-show, cancellation, dissatisfaction, technical problem, duplicate charge, product/digital issue).
- A seller asks support to refund a buyer.
- A customer asks about the status of a refund already requested.

## Responsible
- **Level 1**: intake, evidence, documentation, communication.
- **Senior Support / Supervisor**: reviews the case and makes a recommendation.
- **Payments & Finance**: processes refunds that authorized personnel approved.
- **Management**: exceptions and anything outside policy.

## Required Information
- Verified customer identity.
- Booking/consultation ID or order ID, seller name, listing name.
- Transaction reference, amount, payment method, payment date.
- Reason for the request in the customer's own words, and what outcome they want (refund, reschedule, replacement).
- Evidence: screenshots of messages with the seller, Google Meet join attempts, time of joining, photos (for products), etc.
- For consultations: was the session held, partly held, missed by whom, cancelled by whom and when.

## Steps
1. **Verify the customer** and **acknowledge** the request with tpl-refund-request-ack: we have received your request, it will be reviewed, case number. **Do not** say "you will get a refund", "full refund", or give any timeline.
2. **Check the payment** following *Investigating payment issues* — a refund can only be considered for a payment that is verified as Successful. If the problem is actually a failed payment or duplicate charge, handle it as a payment issue (Payments & Finance).
3. **Collect the facts and evidence** listed above. Use the relevant KB article (e.g., seller no-show, booking cancellation) for issue-specific questions.
4. **Get the other side** when a seller is involved: set *Waiting for Seller*, ask the seller for their account of what happened (neutral wording), and record it. See *Managing buyer–seller disputes*.
5. **Check the refund policy** (*Refunds & cancellations policy*). Today most decisions there are **pending approval**, so:
   - record "Policy pending: [which decision]" in internal notes;
   - do not apply your own judgement as a rule.
6. **Prepare the case summary** as an internal note:
   - Request: what the customer wants and why.
   - Facts verified: payment status, booking status, session/order timeline.
   - Seller's response.
   - Evidence attached.
   - Applicable policy or "pending".
   - Your recommendation (optional, clearly labeled as a recommendation).
7. **Escalate** to **Senior Support / Supervisor** (Level 2) for review. They escalate to **Payments & Finance** or **Management** as needed. Set status **Escalated**; send tpl-escalation-notification.
8. **While waiting:** update the customer per follow-up schedule with tpl-status-update. Never hint at the likely decision.
9. **When a decision is made:**
   - Approved → Payments & Finance processes it; status **In Progress**. Tell the customer only what Payments confirmed (amount, method). Do not state a timeline unless Payments gave approved wording.
   - Declined → explain the reason respectfully using *Saying no / delivering bad news*; offer what alternatives were approved (e.g., reschedule).
10. **Resolve** after the refund is confirmed processed (or the decline is communicated), with root cause, actions taken, final resolution and customer-notified flag completed.

## Expected Outcome
A complete, evidence-backed refund case decided by authorized personnel; customer informed accurately at each stage; no refund promised or processed by support alone.

## Common Mistakes
- "Don't worry, we will refund you" in the first message.
- Promising "full refund within 3 days" or any number not confirmed by Payments.
- Processing or approving a refund because the seller agreed in chat — the decision still follows the approval process.
- Not asking the seller for their side.
- Losing evidence because it stayed in Telegram and was not attached to the ticket.

## Escalation
- Every refund decision → **Senior Support / Supervisor** → **Payments & Finance** (processing) / **Management** (exceptions, high value, reputational risk).
- Customer mentions a chargeback or dispute with their bank/provider → **Payments & Finance** immediately.
- Pattern of repeated refund requests from the same buyer, or a seller with many refund complaints → **Trust & Safety** / **Seller Operations**.

## Related Templates
- tpl-refund-request-ack — acknowledgment.
- tpl-request-transaction-ref — payment details.
- tpl-escalation-notification — under review by the team.
- tpl-status-update — progress updates.
- tpl-acknowledge-complaint — when the refund request is part of a complaint.

## Policy Pending Approval
- Refund eligibility, deadlines, deductions and approval authority for every offering category (see *Refunds & cancellations policy*).
- Who may approve refunds and up to which amount.
- Approved wording for refund processing times per payment method.
- How seller earnings are adjusted when a refund is approved after earnings became available or were withdrawn.

## Internal Notes
- The refund feature is listed as "unconfirmed" on the Feature Status page; check it before describing how a refund will reach the customer.
- A customer who feels heard and sees a clear process accepts a "no" much better than one who was given false hope. Honesty first.

<!-- doc -->
# Managing buyer–seller disputes
id: sop-buyer-seller-disputes
type: sop
category: resolution
audience: internal
priority: high
department: support_l2
features: consultations-1on1, consultations-group
tags: dispute, buyer seller conflict, complaint about seller, complaint about buyer, no-show dispute, ክርክር, service not delivered, mediation
related: sop-refund-requests, pol-consultation-attendance, pol-seller-conduct, sop-escalation, com-deescalation, sop-outbound-calls
templates: tpl-acknowledge-complaint, tpl-escalation-notification, tpl-status-update, tpl-request-customer-info
policy_pending: yes

## Summary
How support acts as a neutral facilitator when a buyer and seller disagree — about a no-show, lateness, service quality, cancellation, or what was promised — collecting both sides and evidence before authorized personnel decide.

## Objective
Resolve disputes fairly and consistently, protect both parties' dignity and data, and keep decisions with the people authorized to make them. Byfluence is a marketplace facilitator: sellers are responsible for their offerings, and support does not take sides before the facts are clear.

## When to Use
- Buyer says the seller did not show up, was late, ended early, or delivered something different from the listing.
- Seller says the buyer did not show up, was abusive, or is demanding something not included.
- Either side requests a refund, reschedule or compensation that the other side contests.

## Responsible
- **Level 1**: intake, evidence from the reporting party, neutral contact with the other party (if allowed), documentation.
- **Senior Support / Supervisor (Level 2)**: owns the dispute, reviews evidence, recommends an outcome.
- **Seller Operations**: seller conduct issues and enforcement.
- **Payments & Finance**: any money movement.
- **Trust & Safety**: harassment, fraud, threats.

## Required Information
- Verified identity of the reporting party.
- Booking/consultation ID or order ID, listing, date/time (with time zone), amount paid.
- Each side's account in their own words.
- Evidence: platform messages, screenshots, Google Meet join times or attempts, emails, photos.
- What outcome each side wants.

## Steps
1. **Acknowledge** the reporting party (tpl-acknowledge-complaint) without agreeing or disagreeing with their claims. Set priority High if money is involved or the dispute blocks a future session.
2. **Collect the reporting party's account and evidence.** Ask for facts: times, what they did to join/contact, screenshots.
3. **Check platform records** you can access: booking status and time, payment status, cancellation/reschedule history, messages on the platform.
4. **Contact the other party** in neutral language (if your access and current policy allow; otherwise route via Seller Operations): "We received a report about booking {{consultation_id}}. Please share what happened from your side." Set status **Waiting for Seller** (or Waiting for Customer) with a follow-up.
5. **Never** share one party's personal contact details or private evidence with the other party beyond what is needed. Summarize instead of forwarding.
6. **Compare the two accounts** in an internal note: facts both agree on, facts in dispute, evidence for each.
7. **Escalate to Level 2** with the case summary. Level 2 checks the relevant policy (*Consultation attendance, lateness & no-show policy*, *Refunds & cancellations policy*); where rules are pending, Level 2 escalates to Management for a decision and records the precedent.
8. **Communicate the decision** to both parties separately, in neutral, respectful wording. Explain what was decided and what happens next (refund processing, reschedule, no action).
9. **Follow through:** money movement by Payments & Finance; seller conduct follow-up by Seller Operations (warnings etc. are their decision).
10. **Resolve** with root cause, actions taken, final resolution and customer-notified flag for each party.

## Expected Outcome
Both sides heard, evidence documented, decision taken by authorized personnel, both parties informed respectfully, and follow-up actions assigned.

## Common Mistakes
- Telling the buyer "the seller is wrong, you'll get your money back" after hearing one side.
- Forwarding the buyer's angry message directly to the seller.
- Treating a Google Meet link existing as proof the session happened — a scheduled meeting does not prove delivery.
- Giving the seller's phone number to the buyer "so they can sort it out".

## Escalation
- All disputes with money involved → **Senior Support / Supervisor**.
- Seller misconduct patterns → **Seller Operations**.
- Harassment, threats, discrimination, fraud → **Trust & Safety** (High/Critical).
- Decision needed where policy is pending, or high-value/reputational dispute → **Management**.

## Related Templates
- tpl-acknowledge-complaint — first response.
- tpl-request-customer-info — evidence request.
- tpl-escalation-notification — under review.
- tpl-status-update — updates.

## Policy Pending Approval
- Approve rules for lateness, no-shows (buyer and seller), partial sessions and technical failures.
- Decide what evidence is accepted to prove attendance or non-attendance.
- Decide whether support agents may contact sellers directly or only via Seller Operations.
- Decide the decision authority and appeal process for dispute outcomes.

## Internal Notes
- Ask both sides for the same kind of evidence; inconsistency in what you ask looks like bias.
- Record each dispute outcome where policy was pending — management needs these precedents to write the policy.

<!-- doc -->
# Escalating issues
id: sop-escalation
type: sop
category: resolution
audience: internal
priority: high
department: support_l2
tags: escalate, escalation, level 2, specialized department, management, handoff, ማሳደግ, supervisor
related: pol-escalation-matrix, sop-prioritize, sop-follow-up, sop-payment-investigation, sop-security-incident, pol-service-levels
templates: tpl-escalation-notification, tpl-status-update, tpl-still-investigating
policy_pending: yes

## Summary
How to escalate a ticket to the right level (Senior Support, a specialized department, or Management) with a complete case package, keep the customer informed, and stay accountable for the ticket while others work on it.

## Objective
Escalations reach the right team the first time, with everything needed to act, and the customer never falls into silence between teams.

## When to Use
- The KB article's Escalation Conditions apply.
- You lack the access, authority or expertise to resolve it (financial decisions, identity review, refunds, fraud, admin actions, sensitive data).
- A policy needed for a decision is pending approval.
- The customer requests a supervisor.
- The ticket has been reopened or is not progressing.

## Responsible
- **Escalating agent** prepares the package and remains the customer contact unless ownership is formally transferred.
- **Receiving level/department** acknowledges and acts.
- **Supervisor** monitors escalations that exceed internal targets.

## Required Information
- Ticket with category, priority and references filled in.
- Clear problem statement and what was already checked.
- Evidence attached.
- What decision or action you need from the receiving team.

## Steps
1. **Pick the level** using the *Escalation matrix* policy:
   - **Level 2 — Senior Support / Supervisor:** complex complaints, disputes, repeated unresolved issues, refund recommendations, policy-pending decisions, customer asks for a supervisor, you lack access.
   - **Level 3 — Specialized department:** Payments & Finance; Technical / Engineering; Seller Operations; Trust & Safety; Logistics & Fulfillment.
   - **Level 4 — Management:** critical decisions, policy exceptions, legal or regulatory matters, high-value or reputational issues. Normally via Level 2.
2. **Do the Level 1 work first.** Verify the customer, collect the KB's required information and check what you can. Escalating an empty ticket only delays the customer. (Exception: Critical security cases — escalate immediately, collect while waiting.)
3. **Write the escalation note** (internal note) in this format:
   - **Request:** what you need (e.g., "Verify transaction and confirm booking", "Decide refund").
   - **Customer & references:** account, booking/order ID, transaction reference.
   - **Facts verified:** what you checked and found.
   - **Customer's claim:** in one or two sentences.
   - **Evidence:** list of attachments.
   - **Urgency:** priority and why (e.g., session date/time).
   - **Customer told:** what you said to the customer, including any follow-up time.
4. **Set the escalation in the app:** escalation level, department, status **Escalated**, priority. Assign to the department queue or person as your team configures it.
5. **Inform the customer** with tpl-escalation-notification: a specialist team is reviewing; case number; we will update you. No promise of outcome or timeline.
6. **Create a follow-up** for yourself to check the escalation and update the customer.
7. **Chase** if there is no response from the receiving team within the internal target configured in Settings; after a second chase, raise to the **Supervisor**.
8. **When the team responds,** move status to **In Progress** (action underway) or back to **Open**, inform the customer of the confirmed result, and resolve following *Resolving and closing support tickets*.

## Expected Outcome
Escalated tickets have a complete package, the right department and level, a correct status, a customer who knows the case is being handled, and a follow-up date.

## Common Mistakes
- Escalating "customer has payment problem, please check" with no reference.
- Escalating to Management directly for routine issues.
- Telling the customer "it's with another team now, contact them" — Byfluence is one company to the customer; you stay their contact.
- Escalating and forgetting: no follow-up set.
- Escalating to two departments in parallel without telling either.

## Escalation
- Receiving team disagrees it is theirs → **Supervisor** decides ownership.
- Escalation stalled beyond internal targets → **Supervisor**; if still stalled, **Management** via the Supervisor.

## Related Templates
- tpl-escalation-notification — customer notification.
- tpl-status-update — progress.
- tpl-still-investigating — no news yet.

## Policy Pending Approval
- Confirm named contacts and handoff channels for each Level 3 department and Management.
- Confirm internal response targets for escalations per priority (configured in Settings).
- Confirm after-hours escalation paths for Critical issues.

## Internal Notes
- The best escalation note can be acted on without opening a single chat transcript.
- Escalation is not failure; holding a ticket you cannot resolve is.

<!-- doc -->
# Following up on unresolved tickets
id: sop-follow-up
type: sop
category: resolution
audience: internal
priority: medium
department: support_l1
tags: follow up, follow-up, reminder, waiting for customer, no response, chase, ክትትል, pending ticket
related: sop-escalation, sop-close-ticket, sop-handover, sop-outbound-calls, pol-service-levels
templates: tpl-status-update, tpl-still-investigating, tpl-closing-no-response, tpl-satisfaction-followup, tpl-delayed-response-apology
policy_pending: yes

## Summary
How to use the app's follow-ups so every open ticket gets regular, honest updates — whether we are waiting for the customer, a seller, or an internal department.

## Objective
No customer has to chase Byfluence for news; no ticket waits silently; and tickets where the customer stops responding are closed fairly and documented.

## When to Use
- Any ticket in Waiting for Customer, Waiting for Seller, Escalated, Under Review or In Progress.
- When you promised the customer an update.

## Responsible
**Ticket owner**; **Supervisor** reviews overdue follow-ups daily.

## Required Information
- Ticket history, latest internal note and last customer contact time.
- Follow-up due dates in the Follow-ups view.

## Steps
1. **Always set a follow-up** when a ticket is waiting on someone. Choose a due date that matches the priority and the internal targets in Settings, and any time you promised the customer.
2. **Work your follow-ups** at the start of the shift and again mid-shift (Follow-ups view, sorted by due date). Overdue first.
3. **Waiting for an internal team** (Escalated):
   - Check for an update from the team.
   - If none, chase the team (internal note + their agreed channel).
   - Update the customer anyway with tpl-still-investigating — "no news" is still news. Never invent progress.
4. **Waiting for Customer:**
   - First reminder: friendly, repeat exactly what you need (tpl-status-update or the KB follow-up response).
   - Second reminder on a different channel if possible (e.g., call or Telegram if you wrote by email), logged in the communication log.
   - Final notice: tell them the ticket will be closed if we don't hear back, and that they can reopen by replying with the case number.
   - Close with tpl-closing-no-response following *Resolving and closing support tickets* — only if the issue does not put the customer at risk (never close a security or money-at-risk ticket for no response without Supervisor approval).
5. **Waiting for Seller:** remind the seller; if the seller does not respond, escalate to **Seller Operations** via Level 2. Keep the buyer updated.
6. **After every follow-up action:** log it, set the next follow-up date, update status if it changed.
7. **After resolution:** where your team does satisfaction checks, send tpl-satisfaction-followup.

## Expected Outcome
Every waiting ticket has a future follow-up date; customers receive regular updates; no-response closures are justified by documented attempts.

## Common Mistakes
- Marking the follow-up done without actually contacting anyone.
- Sending "any update?" to a department with no context.
- Closing a ticket for no response after a single message.
- Telling the customer "the team is almost done" when you have no information.

## Escalation
- Department has not responded after two chases → **Supervisor**.
- Customer complains about lack of updates → apologize (tpl-delayed-response-apology), raise priority one level, inform the **Supervisor**.

## Related Templates
- tpl-status-update, tpl-still-investigating — updates.
- tpl-closing-no-response — closure after no response.
- tpl-satisfaction-followup — after resolution.
- tpl-delayed-response-apology — if updates were late.

## Policy Pending Approval
- Confirm the number of reminders and waiting period before closing a ticket for no customer response.
- Confirm follow-up frequency per priority (internal targets in Settings).

## Internal Notes
- Customers judge us more by how often we update them than by how fast we solve. A short honest update builds trust.

<!-- doc -->
# Resolving and closing support tickets
id: sop-close-ticket
type: sop
category: resolution
audience: internal
priority: medium
department: support_l1
tags: resolve ticket, close ticket, resolution, root cause, customer notified, ትኬት መዝጋት, done, closing
related: sop-follow-up, sop-reopen-ticket, sop-quality-review, pol-operational-safety-rules, sop-kb-update-request
templates: tpl-issue-resolved-confirm, tpl-closing-no-response, tpl-satisfaction-followup
policy_pending: yes

## Summary
How to move a ticket to **Resolved** and then **Closed** correctly: only when the problem is truly solved (or a final decision was communicated), with root cause, actions taken, final resolution and the customer-notified flag completed.

## Objective
Resolved tickets reflect reality, are fully documented for audits, reporting and future agents, and the customer knows the outcome. Marking an unresolved ticket as complete is a breach of the operational safety rules.

## When to Use
- The issue is fixed and confirmed (e.g., booking confirmed, refund processed, account secured).
- A final decision was made and communicated (e.g., refund declined with explanation).
- The customer stopped responding after the follow-up procedure.
- The ticket is a duplicate or was opened by mistake.

## Responsible
**Ticket owner**. Supervisor approval is needed to close Critical tickets and any ticket closed for no response while money or security was involved.

## Required Information
- Confirmation of the outcome (system record, department confirmation, or customer confirmation).
- The full ticket history.

## Steps
1. **Check that it is really resolved:**
   - [ ] The customer's actual problem is solved, not just answered.
   - [ ] Any department action is completed (not just approved).
   - [ ] The customer has what they need (e.g., meeting details, access, explanation).
2. **Send the resolution message** (tpl-issue-resolved-confirm): what was done, what the customer should see now, case number, invitation to reply if anything is still wrong. Log it in the communication log.
3. **Complete the resolution fields** (the app requires them):
   - **Root cause** — the real cause, specific: "Provider confirmation delayed; booking stayed pending", not "payment issue".
   - **Actions taken** — what you and other teams did, in order.
   - **Final resolution** — the outcome for the customer: "Booking confirmed manually by Payments; customer received Meet details."
   - **Customer notified** — tick only if you actually sent/told the outcome.
4. **Set status Resolved.**
5. **Closing:**
   - When the customer confirms, or after the closing period your team uses passes without a new problem reported, set **Closed**.
   - No response cases: follow *Following up on unresolved tickets*; send tpl-closing-no-response; root cause "Unknown — customer did not respond" is acceptable only with the attempts documented.
6. **Knowledge:** if the case revealed a missing or wrong KB article, or a policy gap, follow *Requesting a knowledge base update*.
7. **Satisfaction follow-up** (where used): tpl-satisfaction-followup.

## Expected Outcome
Only genuinely resolved (or properly concluded) tickets are Resolved/Closed; resolution fields are specific and accurate; customers know the outcome.

## Common Mistakes
- Resolving because a department "said they'll fix it".
- Root cause "N/A" or "resolved" — useless for reporting.
- Ticking "customer notified" before the message is sent.
- Closing to meet a target. Targets measure our process; they are never a reason to misreport.

## Escalation
- Unsure whether the problem is really solved → leave it open and ask the **Supervisor**.
- Customer disputes the resolution → keep open (or reopen) and escalate to **Level 2**.

## Related Templates
- tpl-issue-resolved-confirm — resolution message.
- tpl-closing-no-response — closure after no reply.
- tpl-satisfaction-followup — feedback request.

## Policy Pending Approval
- Confirm the waiting period between Resolved and automatic/manual Closed.
- Confirm the approved list of root-cause categories for reporting.

## Internal Notes
- Quality reviews check resolution fields first. Write them for someone reading the ticket six months from now.

<!-- doc -->
# Reopening a ticket
id: sop-reopen-ticket
type: sop
category: resolution
audience: internal
priority: high
department: support_l1
tags: reopen, reopened ticket, issue came back, not solved, still broken, ጉዳዩ አልተፈታም, repeat contact
related: sop-close-ticket, sop-escalation, sop-prioritize, sop-quality-review, sop-follow-up
templates: tpl-reopen-ack, tpl-delayed-response-apology, tpl-status-update
policy_pending: no

## Summary
What to do when a customer says a resolved or closed problem is not actually fixed or has returned: reopen the original ticket, apologize, re-investigate, and raise priority.

## Objective
Keep the full history in one place, recover the customer's trust, and learn why the first resolution failed.

## When to Use
- Customer replies to a Resolved/Closed ticket saying the problem persists or returned.
- A department reverses or fails to complete an action we reported as done.
- A new ticket turns out to be the same problem as a recently resolved one.

Do **not** reopen for a genuinely new, unrelated problem — create a new ticket and reference the old one.

## Responsible
**Original ticket owner** if on shift; otherwise the agent who receives the contact. **Supervisor** reviews all reopened tickets.

## Required Information
- Original ticket number and resolution fields.
- What exactly is still wrong (new evidence, screenshots, times).

## Steps
1. **Find the original ticket** (search by customer and references). If the customer opened a new ticket, link them: add internal notes on both, close the new one as a duplicate, continue in the original.
2. **Set status Reopened** and raise priority by one level (see *Prioritizing urgent issues*). Add an internal note: "Reopened: [reason]".
3. **Acknowledge** with tpl-reopen-ack: apologize sincerely, confirm you have their history (they should not have to repeat everything), case number.
4. **Re-investigate from the facts,** not from the previous conclusion. Read the original root cause and check whether it was right.
5. **Escalate** if the original fix came from a department; include "reopened" in the escalation note so they know it is a repeat. Second reopen of the same ticket → **Level 2** owns it.
6. **Resolve** using *Resolving and closing support tickets* — update the resolution fields to reflect the real root cause and add what failed the first time.
7. **Flag for learning:** reopened tickets are reviewed in quality reviews; if a KB article led to the wrong fix, request an update.

## Expected Outcome
History stays in one ticket, the customer feels taken seriously, the real root cause is found, and the reason for the reopen is documented.

## Common Mistakes
- Making the customer explain the whole problem again.
- Creating a new ticket and losing the history.
- Repeating the same fix without checking why it failed.
- Defensive language ("but we solved this already").

## Escalation
- Reopened twice or more → **Senior Support / Supervisor** owns it.
- Reopen caused by a department action not completed → that department and the **Supervisor**.

## Related Templates
- tpl-reopen-ack — acknowledgment.
- tpl-delayed-response-apology — if the customer waited.
- tpl-status-update — progress.

## Internal Notes
- The reopen rate is a key quality indicator in the daily report. It usually points to resolving too early or a wrong root cause.

<!-- doc -->
# Handling a mass incident (many customers, same problem)
id: sop-mass-incident
type: sop
category: resolution
audience: internal
priority: critical
department: technical
features: support-telegram, support-email, support-phone
tags: outage, mass incident, many customers, system down, incident, everyone affected, ሲስተም ተበላሽቷል, payment outage, meet links broken
related: sop-prioritize, sop-escalation, sop-check-new-tickets, sop-daily-report, pol-communication-standards, sop-handover
templates: tpl-known-outage, tpl-status-update, tpl-issue-resolved-confirm, tpl-delayed-response-apology
policy_pending: yes

## Summary
How the team detects, declares and handles an incident where many customers report the same problem (e.g., payments failing, Google Meet details missing, login down): one master ticket, Technical engaged, consistent approved messaging via Announcements, and every affected customer updated when it ends.

## Objective
Fix fast, communicate consistently, and avoid each agent investigating the same problem separately or telling customers different stories.

## When to Use
- Several customers report the same symptom in a short period.
- Monitoring, a department or management announces a known problem.
- A Feature Status change or provider outage affects many customers.

## Responsible
- **Any agent**: spots the pattern and alerts the Supervisor.
- **Supervisor (incident lead for support)**: declares the incident, creates the master ticket, coordinates with Technical/Payments, gets messaging approved, publishes Announcements, assigns agents.
- **Technical / Payments & Finance**: investigate and fix.
- **Management**: approves external/public communication and decisions on compensation.

## Required Information
- Ticket numbers of the reports, symptoms, first report time, affected features, payment methods, devices/browsers, any error messages/screenshots.

## Steps
### Detect
1. If you see similar tickets (same symptom) in a short period, check **Announcements**. If not announced, alert the **Supervisor** immediately with ticket numbers and the common symptom.

### Declare
2. The Supervisor confirms the pattern (quick check of the tickets) and **declares the incident**:
   - creates a **master ticket**: Critical, escalated to **Technical** (or **Payments & Finance** for payment-provider issues), with all known details;
   - publishes an internal **Announcement**: what is affected, master ticket number, what agents must say, what agents must not say, next update time.
3. If a feature is unavailable, the Supervisor asks an administrator to reflect it on the **Feature Status** page (according to who has permission).

### Handle affected tickets
4. For every related ticket:
   - add an internal note "Part of incident — master #…";
   - set priority according to individual impact (a customer whose session is very soon may still need individual help);
   - reply with tpl-known-outage (approved wording only); status **Escalated** or **Waiting** with a follow-up linked to the next update time.
5. Do not troubleshoot each ticket individually unless the Supervisor asks; collect only the extra details Technical requested (e.g., time of failure, payment method, device).
6. Keep a list of all affected ticket numbers in the master ticket (internal note) so everyone is updated at the end.

### Update
7. The Supervisor posts updates in Announcements at the promised times, even if there is no progress. Agents send tpl-status-update to affected customers with only approved information.
8. Payment incidents: never tell customers that payments "went through" or will be reversed until Payments & Finance confirms per customer.

### Close the incident
9. When Technical confirms the fix, the Supervisor announces it. Agents ask affected customers to retry/check and confirm (tpl-issue-resolved-confirm), handle individual consequences (missed sessions, double payments) as separate investigations within their tickets, and resolve each ticket with root cause "Incident #…: [cause]".
10. The Supervisor writes an incident summary for the daily report: start/end, impact (number of tickets), cause (as known), customer follow-ups still open, lessons, KB updates needed.

## Expected Outcome
One master ticket, one approved message, every affected customer informed at start, during and after, and an incident summary in the daily report.

## Common Mistakes
- Each agent escalating separately to Technical, flooding them.
- Agents guessing causes ("the bank is down") or timelines ("fixed in an hour").
- Forgetting customers who reported early once the fix is in place.
- Posting about the incident on public social media without Management approval.

## Escalation
- Incident affecting payments → **Payments & Finance** + **Technical**.
- Incident involving data exposure → **Trust & Safety** + **Management**.
- Long or high-impact incident, public attention, media → **Management**.

## Related Templates
- tpl-known-outage — standard incident reply.
- tpl-status-update — updates.
- tpl-issue-resolved-confirm — after the fix.
- tpl-delayed-response-apology — for customers who waited during the incident.

## Policy Pending Approval
- Define the trigger (number of similar reports/time window) for declaring an incident.
- Define who may publish public status messages (website, Telegram channel) and approval steps.
- Decide compensation/goodwill rules for customers affected by platform incidents (e.g., missed sessions).
- Define incident severity levels and after-hours on-call contacts for Technical.

## Internal Notes
- When in doubt, alert the Supervisor early; a false alarm costs minutes, a missed incident costs trust.
- Use the same words as the Announcement. Consistency is what makes customers believe us during an outage.
