<!-- doc -->
# How a Customer Requests a Refund
id: ref-how-to-request-refund
type: article
category: refunds-disputes
subcategory: refund-requests
audience: buyer
priority: medium
department: support_l2
features: refunds
tags: request refund, how to get money back, refund request, money back, cancel and refund, ገንዘቤ ይመለስልኝ, ተመላሽ ገንዘብ, ገንዘብ መመለስ
related: ref-eligibility, ref-refund-status, ref-evidence-collection, ref-tsg-dispute-handling-master, pay-refund-processing
templates: tpl-refund-request-ack, tpl-request-screenshot, tpl-refund-status-update
policy_pending: yes

## Summary
How a buyer asks for a refund on Byfluence today, what the agent collects, and how the request is routed to authorized personnel. Support agents record and route refund requests — they never approve or reject them.

## Overview
Byfluence is a marketplace facilitator: the seller provides the consultation or product, and Byfluence handles the payment. A refund therefore usually involves three parties — the buyer, the seller, and Byfluence's authorized finance/review staff.

The official refund policy (eligibility, deadlines, deductions, who approves) **has not been approved yet**. What *is* confirmed is the support workflow from the business overview:

1. Customer complaint is received.
2. Support identifies the transaction (order, booking, payment reference).
3. Support collects evidence.
4. The case is reviewed against policy (currently: escalated, because policy is pending).
5. Support contacts the seller and/or the relevant department.
6. **Authorized personnel decide.**
7. Support explains the decision to the customer.
8. Approved adjustments are processed (by Payments & Finance).
9. The case is documented and closed.

Your job as an agent covers steps 1–3, 5 (contact), 7 and 9. You never perform step 6.

Payment status concepts you may see in the admin dashboard: Pending, Successful, Failed, Canceled, **Refund Pending**, **Refunded**, **Disputed**.

## Customer Steps
1. Contact Byfluence Support through an official channel ({{support_channel}}). Telegram, email and the website support option are the intended channels.
2. Share the order ID, booking ID or the transaction reference from the payment receipt/SMS.
3. Explain briefly what went wrong (e.g., the consultant did not join, the item arrived damaged, the file does not open).
4. Attach supporting evidence if available: screenshots, photos, messages with the seller — all sent through Byfluence support, never to an outside contact.
5. Keep the case number ({{ticket_id}}) and use it in every follow-up.

> [!NOTE] Whether the buyer dashboard has a self-service "Request refund" button is not confirmed. Until it is, all refund requests come through support and are logged as tickets.

## Information to Collect
- Customer full name and registered email or phone number (to confirm identity)
- Order ID / consultation (booking) ID
- Transaction reference from the payment receipt or SMS, payment method ({{payment_method}}) and amount
- Date of purchase and, for consultations, the scheduled date/time of the session
- Seller / consultant name
- Reason for the refund request, in the customer's own words
- What outcome the customer is asking for (full refund, partial refund, replacement, reschedule)
- Evidence: screenshots, photos (physical products), error messages (digital products), chat history with the seller on Byfluence
- Whether the customer has also opened a dispute/chargeback with their bank or payment provider

> [!WARNING] Never ask for passwords, OTP codes, PINs, mobile-money PINs or full card numbers. The transaction reference and receipt are enough to locate a payment.

## Troubleshooting Steps
1. Confirm identity: the request must come from the registered email/phone of the account that paid.
2. Locate the transaction in the admin dashboard (or the payment provider portal if you have authorized access). Note its status.
   - **Successful** → continue.
   - **Pending / Failed / Canceled** → this is not a refund case yet; follow the relevant payment article (the money may never have been captured).
   - **Refund Pending / Refunded** → a refund is already in progress or done; switch to *Checking Refund Status* (`ref-refund-status`).
   - **Disputed** → a dispute already exists; link this ticket to it, do not open a second one.
   - **Two successful payments for one order** → follow `pay-duplicate-charge`.
3. Identify the offering type and open the matching article: consultation (`ref-consultation-refunds`), physical product (`ref-product-refunds`), digital product (`ref-digital-refunds`).
4. Collect evidence using `ref-evidence-collection`. Ask only for what is needed for this case.
5. Create/update the ticket with category **Refunds & Disputes**, attach all references and evidence, and write a neutral one-paragraph case summary.
6. Send the acknowledgement (`tpl-refund-request-ack`) with the case number.
7. Escalate to **Senior Support / Supervisor (L2)** for a refund recommendation. If the seller's side is needed, L2 decides who contacts the seller.
8. Set a follow-up time and keep the customer updated until a decision is communicated.

- [ ] Identity confirmed
- [ ] Transaction located and status noted
- [ ] Offering type identified
- [ ] Evidence collected and attached
- [ ] Acknowledgement sent with {{ticket_id}}
- [ ] Escalated to L2 with a neutral summary

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry that your experience did not go as expected, and I will help you submit your refund request.

So that our team can review your case, please send me:
1. Your order or booking ID (or the transaction reference from your payment receipt or SMS)
2. A short description of what went wrong
3. Any screenshots or photos that show the problem

Refund requests are reviewed by our authorized team, who will make the decision after checking the details with all parties. I can't confirm the outcome in advance, but I will make sure your case is complete and keep you updated.

Please do not share your password, PIN or any verification code — we will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ግዢዎ እንደጠበቁት ባለመሆኑ ይቅርታ እንጠይቃለን፤ የተመላሽ ገንዘብ ጥያቄዎን እንዲያቀርቡ እረዳዎታለሁ።

ቡድናችን ጉዳይዎን እንዲገመግም እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የትዕዛዝ ወይም የቀጠሮ መለያ ቁጥርዎን (ወይም ከክፍያ ደረሰኝዎ ወይም ከኤስኤምኤስ ላይ ያለውን የግብይት መለያ ቁጥር)
2. ምን ችግር እንደተፈጠረ አጭር ማብራሪያ
3. ችግሩን የሚያሳዩ ስክሪንሾቶች ወይም ፎቶዎች ካሉዎት

የተመላሽ ገንዘብ ጥያቄዎች የሚገመገሙት ስልጣን ባለው ቡድናችን ሲሆን፣ ውሳኔው የሚሰጠው ከሁሉም ወገኖች ጋር ዝርዝሩ ከተጣራ በኋላ ነው። ውጤቱን አስቀድሜ ማረጋገጥ ባልችልም፣ ጉዳይዎ ሙሉ መረጃ ይዞ እንዲቀርብ አደርጋለሁ፤ ሂደቱንም አሳውቅዎታለሁ።

እባክዎ የይለፍ ቃልዎን፣ ፒንዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about this. Please send your order/booking ID (or payment reference), what went wrong, and any screenshots. Our authorized team reviews every refund request and I'll keep you updated. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለተፈጠረው ችግር ይቅርታ። እባክዎ የትዕዛዝ/የቀጠሮ ቁጥርዎን (ወይም የክፍያ መለያ ቁጥሩን)፣ የተፈጠረውን ችግር እና ስክሪንሾቶች ካሉ ይላኩልኝ። እያንዳንዱን ጥያቄ ስልጣን ያለው ቡድናችን ይገመግመዋል፤ ሂደቱን አሳውቅዎታለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on your refund request, case {{ticket_id}}. Your case has been passed to our review team with all the information you provided, and it is still under review. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ተመላሽ ገንዘብ ጥያቄዎ (የጉዳይ ቁጥር {{ticket_id}}) የሚሰጥ መረጃ ነው። ጉዳይዎ ያቀረቡትን መረጃ በሙሉ ይዞ ለግምገማ ቡድናችን ተላልፏል፤ አሁንም በግምገማ ላይ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Every complete refund request → **Senior Support / Supervisor (L2)** for review and recommendation.
- Payment found but status/amount does not match what the customer says, or duplicate charge → **Payments & Finance**.
- The customer asks for the refund to go to a different account, the reference belongs to another user, or the screenshot looks edited → **Trust & Safety** (see `ref-refund-to-different-account`).
- The customer has also opened a bank/provider chargeback → **Payments & Finance** (see `pay-chargeback`).
- High-value transaction, legal threats or media/reputation threats → **Management** via L2.

## Resolution Procedure
1. Confirm the request reached L2 with complete information and that the customer received the acknowledgement.
2. When a decision is made, communicate it using `ref-final-decision-communication`.
3. If a refund was approved, confirm with Payments that it was processed and that the payment status shows **Refund Pending** or **Refunded**.
4. Record: reason category, evidence received, decision, who decided, and amount (if any) before resolving.

## Policy Pending Approval
- Decide whether buyers can request refunds directly from the dashboard or only through support.
- Confirm the official channels and the approved wording for "how long a review usually takes".
- Confirm who is authorized to approve refunds (L2, Payments & Finance, Management) and any value thresholds.
- Confirm whether a refund request must be submitted within a set period after purchase or after the session/delivery.

## Internal Notes
- Never say "you will get a refund", "approved" or "eligible" — say "your request will be reviewed".
- One ticket per transaction. If the customer writes from several channels, merge them.
- Customers with low digital literacy may not find their transaction reference: their registered phone number, the seller name and the approximate payment time are usually enough to search.
- Refund requests that arrive with urgency ("refund now or I'll call the bank") are not automatically fraud, but note them. Check `ref-abuse-of-refunds` signals before escalating.

<!-- doc -->
# Refund Eligibility (What We Know and What Is Pending)
id: ref-eligibility
type: article
category: refunds-disputes
subcategory: refund-requests
audience: both
priority: medium
department: support_l2
features: refunds
tags: am i eligible for refund, refund policy, refund rules, can i get my money back, refund deadline, ለተመላሽ ገንዘብ ብቁ ነኝ, የተመላሽ ገንዘብ ፖሊሲ, ደንብ
related: ref-how-to-request-refund, ref-consultation-refunds, ref-product-refunds, ref-digital-refunds, con-refund-eligibility
templates: tpl-refund-request-ack, tpl-escalation-notification
policy_pending: yes

## Summary
Byfluence has not yet approved an official refund policy. This article tells agents exactly what is confirmed, what is still undecided, and how to answer "Am I eligible for a refund?" without making promises.

## Overview
Customers and sellers will often ask "Will I get my money back?" before they submit anything. The honest answer today is: **every refund request is reviewed case by case by authorized personnel, because the official rules are still being finalized.**

### What is confirmed
| Topic | Confirmed fact |
|---|---|
| Role of Byfluence | Marketplace facilitator. Sellers are responsible for their offerings, subject to marketplace rules. |
| Who decides | Authorized personnel — **not** front-line support agents. |
| Workflow | Complaint → identify transaction → collect evidence → review policy → contact seller/department → authorized personnel decide → explain → process approved adjustments → document & close. |
| Different categories | Consultations, group consultations, physical products and digital products may need different refund rules. |
| Payment status concepts | Refund Pending, Refunded, Disputed exist as statuses. |
| Seller earnings | A buyer payment is not immediately withdrawable by the seller; disputes and refunds can affect seller earnings before release. |
| Meetings | A scheduled Google Meet does not prove the service was delivered. |

### What is NOT confirmed (do not state any of these to customers)
- Any refund deadline or time window
- Any percentage, deduction, cancellation fee or non-refundable fee
- Whether platform fees or payment-provider fees are returned
- Refund processing times for any payment method
- Whether refunds are returned to the original payment method only
- Whether store credit or rescheduling can replace a refund
- Category-specific rules (no-shows, partial attendance, damaged goods, digital downloads)

## Customer Steps
1. Contact support with the order/booking ID or transaction reference.
2. Describe what happened and send any evidence.
3. Wait for the review outcome; support will update them using the case number.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your question. At Byfluence, every refund request is reviewed individually by our authorized team. They look at what happened, the evidence from both the buyer and the seller, and the type of purchase before making a decision.

Because of this, I'm not able to confirm in advance whether a refund will be approved or how much it would be. What I can do is make sure your request is submitted with all the right information so it can be reviewed fairly.

If you would like to submit a request, please send me your order or booking ID and a short description of what happened.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጥያቄዎ እናመሰግናለን። በByfluence እያንዳንዱ የተመላሽ ገንዘብ ጥያቄ ስልጣን ባለው ቡድናችን በተናጠል ይገመገማል። ቡድኑ ውሳኔ ከመስጠቱ በፊት የተፈጠረውን ሁኔታ፣ ከገዢውም ከሻጩም የቀረበውን ማስረጃ እና የግዢውን ዓይነት ይመለከታል።

በዚህ ምክንያት ተመላሽ ገንዘብ ይፈቀድ እንደሆነ ወይም መጠኑ ምን ያህል እንደሚሆን አስቀድሜ ማረጋገጥ አልችልም። ማድረግ የምችለው ጥያቄዎ በፍትሃዊነት እንዲገመገም አስፈላጊውን መረጃ ሁሉ ይዞ መቅረቡን ማረጋገጥ ነው።

ጥያቄ ማቅረብ ከፈለጉ፣ እባክዎ የትዕዛዝ ወይም የቀጠሮ መለያ ቁጥርዎን እና የተፈጠረውን ሁኔታ በአጭሩ ይላኩልኝ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, every refund request is reviewed case by case by our authorized team, so I can't confirm the outcome in advance. Send me your order/booking ID and what happened and I'll submit it for review. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እያንዳንዱ የተመላሽ ገንዘብ ጥያቄ ስልጣን ባለው ቡድናችን በተናጠል ይገመገማል፤ ስለዚህ ውጤቱን አስቀድሜ ማረጋገጥ አልችልም። የትዕዛዝ/የቀጠሮ ቁጥርዎን እና የተፈጠረውን ይላኩልኝ፤ ለግምገማ አቀርበዋለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Customer submits an actual request → follow `ref-how-to-request-refund` and escalate to **Senior Support / Supervisor (L2)**.
- Customer insists on a written policy or quotes a rule you cannot verify → **L2**; do not confirm or deny the quoted rule.
- A seller asks what refund rules apply to their listings → **Seller Operations**.
- Customer threatens legal action over the absence of a policy → **Management** via L2.

## Policy Pending Approval
- Decide the refund eligibility rules for each offering: one-on-one consultations, group consultations, physical products, inventory-free (reseller) orders, digital products.
- Decide request deadlines (from purchase, session date, delivery date, or download).
- Decide deductions: whether platform fees, payment-provider fees or cancellation fees are kept.
- Decide approval authority and value thresholds (who approves up to which amount).
- Decide whether refunds go only to the original payment method.
- Decide whether alternatives (reschedule, replacement, store credit) can be offered instead of money.
- Approve the public customer-facing refund policy text so agents can quote it.

## Internal Notes
- If a customer quotes "Byfluence's refund policy" from a screenshot or a third party, do not confirm it — no official policy is published yet. Escalate to L2 if they insist.
- Do not use phrases like "you qualify", "you are not eligible", "non-refundable" or "within X days". They create commitments Byfluence has not made.
- Sellers sometimes write their own refund terms in listings ("no refunds"). Seller terms do not override marketplace rules; flag such listings to **Seller Operations** but do not tell the buyer the seller's term is invalid — that is a management decision.
- Once the policy is approved, this article must be rewritten. Check Announcements for policy updates.

<!-- doc -->
# Consultation Refund Requests
id: ref-consultation-refunds
type: article
category: refunds-disputes
subcategory: refund-types
audience: both
priority: high
department: support_l2
features: refunds, consultations-1on1, consultations-group, google-meet
tags: consultation refund, session refund, consultant did not join, no-show refund, bad session, group session refund, የምክክር ተመላሽ ገንዘብ, አማካሪው አልመጣም
related: con-seller-no-show, con-refund-eligibility, ref-how-to-request-refund, ref-evidence-collection, ref-buyer-seller-disagreement
templates: tpl-refund-request-ack, tpl-request-screenshot, tpl-refund-status-update
policy_pending: yes

## Summary
A buyer asks for a refund for a one-on-one or group consultation — for example because the consultant did not join, the session was cut short, the meeting link did not work, or the session was not what was described.

## Issue Description
Consultations are the core MVP offering. The buyer pays, the booking is confirmed, Google Meet details are shared and the session is held at the scheduled time. Refund requests arise when something in that chain fails. Because a consultation is a live service, evidence is harder than for physical goods: **a scheduled Google Meet meeting does not prove the service was delivered**, and a "completed" status may be set before or regardless of actual attendance. Both buyer and seller may honestly remember the session differently.

Treat as **High** priority when the buyer has another session coming up with the same seller, or when many buyers report the same seller.

## Possible Causes
- **Seller no-show** — the consultant never joined (see `con-seller-no-show`).
- **Buyer no-show or late arrival** — the buyer missed the session and now asks for a refund.
- **Technical failure** — missing/wrong Google Meet link, wrong time or time-zone confusion, connection problems on either side.
- **Session shorter than the listed duration** or ended early.
- **Quality / description dispute** — buyer says the content did not match the listing (topic, expertise, language).
- **Buyer cancelled before the session** and wants the money back.
- **Seller cancelled or rescheduled** and the new time does not work for the buyer.
- **Group consultation issues** — session full, seller cancelled the group session, buyer could only attend part of it.
- **Duplicate booking/payment** for the same session (follow `pay-duplicate-charge`).

## Information to Collect
- Booking/consultation ID ({{consultation_id}}), seller name, scheduled date and time **with time zone**
- Whether it was one-on-one or a group consultation
- Transaction reference and amount paid
- What happened, in the buyer's words: did they join? at what time? did the seller join? how long did they wait?
- Screenshots: the Google Meet waiting screen with the device clock visible, any error message, messages exchanged with the seller on Byfluence
- Whether the buyer contacted the seller before/after the session and the reply
- What the buyer wants: refund, partial refund, or reschedule

> [!WARNING] Never ask for passwords, OTP codes, PINs or card numbers. Never ask the buyer to share their Google account login.

## Troubleshooting Steps
1. Confirm identity and locate the booking and the payment (status should be **Successful**).
2. Check the booking record in the admin dashboard: scheduled time (and time zone), status (upcoming, completed, cancelled), any cancellation or reschedule history, and who made it.
3. Check whether the Meet link existed and was the same link the buyer used (if your tools show it).
4. Decide the case type:
   - **Seller did not attend** → follow `con-seller-no-show` and collect the buyer's waiting evidence.
   - **Buyer did not attend** → collect the buyer's reason; note it neutrally. Do not tell the buyer they will lose their money — the rule is not approved.
   - **Technical failure** → check Announcements for incidents; if the link was missing or wrong, involve **Technical** to confirm.
   - **Session quality / description** → collect specifics (what was promised in the listing vs. what happened). Open `ref-buyer-seller-disagreement` if the seller disagrees.
   - **Session cancelled/rescheduled by seller** → note who changed it and when; the buyer may prefer a refund over the new time.
   - **Group session** → note capacity, whether the group session ran at all, and how much the buyer attended.
5. Ask the seller for their account of events through the approved seller contact process (or ask L2 to do it). Ask neutrally; do not reveal more buyer data than needed.
6. If the session has not happened yet and the issue is fixable (e.g., missing link), fix the issue first — a refund is not always what the buyer wants.
7. Escalate the complete case to **L2** with both accounts and evidence.

- [ ] Booking and payment located
- [ ] Time zone confirmed
- [ ] Buyer account and evidence collected
- [ ] Seller account requested
- [ ] Escalated to L2 with neutral summary

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry your consultation with {{seller_name}} on {{booking_date}} at {{booking_time}} did not go as planned.

To review your refund request, please send me:
1. A short description of what happened (for example: you joined but the consultant did not, the link did not work, or the session ended early)
2. The time you joined and how long you waited, if relevant
3. Any screenshots you have, such as the Google Meet screen or messages with the consultant

We will also ask the consultant for their side, as we do for every case. Our authorized team will then review the request and make a decision. I can't confirm the result in advance, but I will keep you informed.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በ{{booking_date}} በ{{booking_time}} ከ{{seller_name}} ጋር የነበረዎት ምክክር እንደታቀደው ባለመካሄዱ ይቅርታ እንጠይቃለን።

የተመላሽ ገንዘብ ጥያቄዎን ለመገምገም እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የተፈጠረውን ሁኔታ በአጭሩ (ለምሳሌ፦ እርስዎ ገብተው አማካሪው አልገባም፣ ሊንኩ አልሰራም፣ ወይም ምክክሩ ቀድሞ ተቋርጧል)
2. አስፈላጊ ከሆነ የገቡበትን ሰዓት እና ምን ያህል እንደጠበቁ
3. ያሉዎትን ስክሪንሾቶች፣ ለምሳሌ የGoogle Meet ገጹን ወይም ከአማካሪው ጋር የተለዋወጧቸውን መልዕክቶች

እንደ ሁሉም ጉዳዮች የአማካሪውንም ሀሳብ እንጠይቃለን። ከዚያም ስልጣን ያለው ቡድናችን ጥያቄውን ገምግሞ ውሳኔ ይሰጣል። ውጤቱን አስቀድሜ ማረጋገጥ ባልችልም ሂደቱን ሁሉ አሳውቅዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry your session didn't go as planned. Please tell me what happened, when you joined, and send any screenshots (Meet screen, messages). We'll hear from the consultant too and our team will review. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ምክክርዎ እንደታቀደው ባለመሄዱ ይቅርታ። እባክዎ የተፈጠረውን፣ የገቡበትን ሰዓት እና ያሉዎትን ስክሪንሾቶች (የMeet ገጽ፣ መልዕክቶች) ይላኩልኝ። የአማካሪውንም ሀሳብ ሰምተን ቡድናችን ይገመግማል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}} about your consultation on {{booking_date}}. We have your information and are waiting for the review to be completed, which includes hearing from the consultant. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ በ{{booking_date}} ስለነበረዎት ምክክር (የጉዳይ ቁጥር {{ticket_id}}) የሚሰጥ መረጃ ነው። መረጃዎን ተቀብለናል፤ የአማካሪውን ሀሳብ ጨምሮ ግምገማው እስኪጠናቀቅ እየጠበቅን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Every complete consultation refund request → **Senior Support / Supervisor (L2)**.
- Missing/incorrect Meet link, wrong time displayed, or platform error → **Technical / Engineering** (in parallel with L2).
- Same seller has several no-show or refund complaints → **Seller Operations** (pattern review) and L2.
- Seller has been paid out already and a refund is being considered → **Payments & Finance** (see `out-payout-hold-restriction`).
- Seller or buyer is abusive or threatening during the dispute → **Trust & Safety** (see `tns-harassment`).
- Group session cancelled by the seller affecting many buyers → **L2** immediately; supervisor may treat as one incident.

## Resolution Procedure
1. Confirm a decision was made by authorized personnel and recorded on the ticket.
2. Communicate the decision (`ref-final-decision-communication`). If a reschedule was agreed instead, confirm the new date/time and Meet details in writing.
3. If a refund was approved, confirm with Payments that the payment status changed to **Refund Pending** or **Refunded**.
4. Record the case type (seller no-show, buyer no-show, technical, quality, cancellation, group) for reporting.

## Policy Pending Approval
- Decide refund rules for seller no-shows, buyer no-shows, late arrivals (by either party) and sessions that ended early.
- Decide whether buyer cancellations before the session are refundable and up to when.
- Decide what evidence is accepted to prove attendance or non-attendance.
- Decide group-consultation rules: cancellation by seller, partial attendance, full sessions, missed sessions.
- Decide whether a reschedule can be offered instead of a refund, and whether the buyer can refuse it.
- Decide how consultation "completed" status is set and whether it can be reversed after a complaint.

## Internal Notes
- Always confirm time zones. Many "no-show" complaints are actually a time mismatch — compare the booking time and time zone with the buyer's device time on the screenshot.
- The Meet link existing and the booking being marked "completed" are **not** proof the session happened. Do not tell the buyer "our records show it was completed" as an argument.
- Do not share the seller's personal phone number or email with the buyer (or vice versa). Communication stays on Byfluence.
- If the session is still upcoming and the buyer only fears a no-show, do not open a refund request — reassure and monitor.
- Sellers may push buyers to "settle privately" outside Byfluence. That is a fraud signal; see `tns-off-platform-payment-request`.

<!-- doc -->
# Physical Product Refund Requests
id: ref-product-refunds
type: article
category: refunds-disputes
subcategory: refund-types
audience: both
priority: medium
department: support_l2
features: refunds, physical-products, delivery-addis
tags: product refund, return item, damaged item refund, wrong item, item not received refund, return product, ዕቃ መመለስ, የተበላሸ ዕቃ, ተመላሽ ገንዘብ ለዕቃ
related: phy-damaged-product, ref-how-to-request-refund, ref-evidence-collection, ref-partial-refund, tns-fake-products
templates: tpl-refund-request-ack, tpl-request-screenshot, tpl-refund-status-update
policy_pending: yes

## Summary
A buyer asks for a refund on a physical product — because it was not delivered, arrived damaged, was the wrong item, was not as described, or they changed their mind. Physical products are a planned expansion area: check the Feature Status page first.

## Issue Description
Physical products (clothing, electronics, accessories, beauty, home, lifestyle) are an expansion area, with the initial rollout prioritizing **Addis Ababa**. Delivery methods, areas, fees and times are **not confirmed**, and neither are return or refund rules.

> [!WARNING] Check the **Feature Status** page before handling this case as a normal order. If physical products are not live, the "order" may have been arranged off-platform or through a fake listing — treat it as a possible fraud case and see `tns-report-fraud`.

Refund requests for products usually involve: who had the item when it was damaged (seller, delivery partner, buyer), whether the buyer still has the item, and whether a return is possible.

## Possible Causes
- Item never delivered, or delivery marked complete but not received
- Item damaged in transit or arrived broken
- Wrong item, wrong size/colour or missing parts
- Item does not match the listing (misleading description — see `tns-misleading-descriptions`)
- Suspected counterfeit (see `tns-fake-products`)
- Buyer changed their mind or ordered by mistake
- Order cancelled by the seller after payment
- Inventory-free (reseller) order where the supplier, not the listed seller, fulfils the item

## Information to Collect
- Order ID ({{order_id}}), product name, seller name, transaction reference and amount
- Delivery address area (only what is needed — e.g., sub-city) and the date the item was received or expected
- Clear photos: the item, the damage, the packaging/label, and anything missing
- An unboxing photo or video if the buyer has one
- Whether the buyer still has the item, and whether it was used
- Whether the buyer refused delivery or signed/confirmed receipt
- Messages with the seller on Byfluence
- What the buyer wants: refund, partial refund, replacement or return

> [!WARNING] Never ask for passwords, OTP codes, PINs or card numbers. Ask only for the part of the address needed to identify the delivery.

## Troubleshooting Steps
1. Check the **Feature Status** page for physical products and Addis Ababa delivery.
2. Confirm identity; locate the order and the payment in the admin dashboard.
3. Check the order status history: paid, preparing, shipped/out for delivery, delivered, completed, cancelled.
4. Decide the case type:
   - **Not received** → check delivery records; involve **Logistics & Fulfillment** to trace it before discussing refunds.
   - **Damaged** → follow `phy-damaged-product`; collect photos before anything is thrown away.
   - **Wrong / not as described** → compare the photos with the listing; take a screenshot of the listing now (sellers can edit listings later).
   - **Counterfeit suspected** → follow `tns-fake-products` in parallel.
   - **Change of mind** → record the request; the rule is not approved, so escalate without promising.
   - **Seller cancelled** → confirm the cancellation in the record; escalate to L2/Payments.
5. Ask the buyer to keep the item, packaging and labels until the case is decided. Do not tell them to send the item back unless an authorized return process is confirmed.
6. Request the seller's account (or the supplier's, for inventory-free orders) through L2/Seller Operations.
7. Escalate the complete case to **L2**.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry about the problem with your order {{order_id}} ({{product_name}}).

To review your refund request, please send me:
1. Clear photos of the item, showing the problem
2. Photos of the packaging and any label
3. A short description of what happened and what you would like us to do

Please keep the item and its packaging for now, and do not send it anywhere until we confirm the next step with you.

We will also contact the seller for their side. Our authorized team will review the request and decide. I can't confirm the result in advance, but I will keep you updated.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በትዕዛዝ ቁጥር {{order_id}} ({{product_name}}) ላይ ስለተፈጠረው ችግር ይቅርታ እንጠይቃለን።

የተመላሽ ገንዘብ ጥያቄዎን ለመገምገም እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ችግሩን በግልጽ የሚያሳዩ የዕቃው ፎቶዎች
2. የማሸጊያውን እና ካለ የመለያ ወረቀቱን (label) ፎቶዎች
3. የተፈጠረውን ሁኔታ እና እንድናደርግልዎ የሚፈልጉትን በአጭሩ

እባክዎ ቀጣዩን እርምጃ እስክናሳውቅዎ ድረስ ዕቃውን ከነማሸጊያው ያስቀምጡት፤ ወደ የትም አይላኩት።

የሻጩንም ሀሳብ እንጠይቃለን። ስልጣን ያለው ቡድናችን ጥያቄውን ገምግሞ ውሳኔ ይሰጣል። ውጤቱን አስቀድሜ ማረጋገጥ ባልችልም ሂደቱን አሳውቅዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about order {{order_id}}. Please send clear photos of the item, the problem and the packaging, and tell me what you'd like us to do. Keep the item for now. Our team will review. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ ትዕዛዝ {{order_id}} ይቅርታ። እባክዎ የዕቃውን፣ የችግሩን እና የማሸጊያውን ግልጽ ፎቶዎች ይላኩ፤ ምን እንድናደርግልዎ እንደሚፈልጉም ይንገሩኝ። ዕቃውን ለጊዜው ያስቀምጡት። ቡድናችን ይገመግማል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}} for order {{order_id}}. We are still reviewing your request together with the seller's information. Please keep the item and packaging until we confirm the next step. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ትዕዛዝ {{order_id}} (የጉዳይ ቁጥር {{ticket_id}}) የሚሰጥ መረጃ ነው። ጥያቄዎን ከሻጩ መረጃ ጋር አሁንም እየገመገምን ነው። ቀጣዩን እርምጃ እስክናረጋግጥ ድረስ እባክዎ ዕቃውን እና ማሸጊያውን ያስቀምጡ። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every complete product refund request → **Senior Support / Supervisor (L2)**.
- Item not delivered, lost or damaged in transit → **Logistics & Fulfillment**.
- Suspected counterfeit, fake listing, or physical products not live but buyer paid → **Trust & Safety**.
- Inventory-free/reseller order → **Seller Operations** (supplier side) plus L2.
- Refund approved and needs processing → **Payments & Finance**.

## Resolution Procedure
1. Confirm the authorized decision and communicate it (`ref-final-decision-communication`).
2. If a return was approved, confirm the return instructions were given by the responsible team — agents do not invent return addresses or couriers.
3. Confirm the refund/replacement was completed (payment status **Refund Pending/Refunded**, or replacement delivered).
4. Record the case type and whether the seller was at fault for reporting.

## Policy Pending Approval
- Decide return and refund rules for physical products (time limits, item condition, change-of-mind returns).
- Decide who pays return delivery costs and who arranges pickup.
- Decide liability for damage in transit (seller, delivery partner, Byfluence).
- Decide whether partial refunds can be offered for minor damage or missing parts.
- Decide refund rules for inventory-free (reseller) orders: supplier vs. reseller responsibility.

## Internal Notes
- Photos must be taken **before** the buyer discards packaging. Ask early.
- Screenshot the listing as it is now and save it to the ticket — sellers can edit descriptions after a complaint.
- A buyer reporting the same "damage" on multiple orders is a refund-abuse signal (`ref-abuse-of-refunds`). Don't accuse; note and escalate.
- Never give a buyer the seller's home address or phone number to "return it yourself".

<!-- doc -->
# Digital Product Refund Requests
id: ref-digital-refunds
type: article
category: refunds-disputes
subcategory: refund-types
audience: both
priority: medium
department: support_l2
features: refunds, digital-products
tags: digital product refund, ebook refund, course refund, file not working refund, template refund, download refund, ዲጂታል ምርት ተመላሽ, ፋይሉ አይከፈትም
related: dig-refunds, ref-how-to-request-refund, ref-evidence-collection, tns-intellectual-property, ref-abuse-of-refunds
templates: tpl-refund-request-ack, tpl-request-screenshot, tpl-refund-status-update
policy_pending: yes

## Summary
A buyer asks for a refund on a digital product (e-book, template, guide, course, design resource, document) — usually because the file is broken, wrong, inaccessible, or not as described. Digital products are a planned expansion area: check the Feature Status page first.

## Issue Description
Digital products are delivered instantly and cannot be "returned" — once downloaded, the buyer keeps a copy. This makes digital refunds especially sensitive to abuse, but buyers also have genuine problems: broken links, corrupted or wrong files, missing content, or content that is very different from the description. Rules for access, download limits and refund eligibility are **not confirmed**.

> [!WARNING] Check the **Feature Status** page before treating this as a normal digital purchase. If digital products are not live, investigate how the buyer paid.

## Possible Causes
- Download link broken or expired, or access never granted after payment
- Corrupted file, wrong file, wrong format, or file will not open on the buyer's device
- Content incomplete (missing chapters, lessons or pages)
- Content does not match the listing description, language or level
- Content appears copied from another creator (copyright issue — see `tns-intellectual-property`)
- Duplicate purchase of the same product
- Buyer changed their mind after downloading

## Information to Collect
- Order ID ({{order_id}}), product name, seller name, transaction reference and amount
- What exactly fails: the link, the download, opening the file, or the content itself
- Device and app used to open the file (phone/computer, PDF reader, etc.)
- Screenshots of the error message or of the problem in the content
- Whether the buyer downloaded/opened the file successfully at any point
- For description disputes: which part of the listing does not match

> [!WARNING] Never ask for passwords, OTP codes, PINs or card numbers. Do not ask the buyer to send you the paid file itself unless L2 asks for it for review.

## Troubleshooting Steps
1. Check the **Feature Status** page for digital products.
2. Confirm identity; locate the order and the payment.
3. Check access records if your tools show them (access granted, download attempts).
4. Try to **fix before refunding**:
   - Broken link / no access → escalate to **Technical** to restore access; tell the buyer what you are doing.
   - Won't open → check the format against the buyer's device; suggest a suitable free reader app only if the format is standard.
   - Wrong or corrupted file → ask the seller (via L2/Seller Operations) for a corrected file.
5. If fixing is not possible or the buyer disputes the content, collect evidence and escalate to **L2** for a decision.
6. If copyright infringement is suspected, also follow `tns-intellectual-property`.
7. Note whether the buyer has had full access to the content — L2 will need this.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry you are having trouble with {{product_name}} (order {{order_id}}).

To help, please send me:
1. A short description of the problem (for example: the link does not work, the file does not open, or the content is not what was described)
2. A screenshot of any error message or of the problem
3. The device you are using to open the file

In many cases we can fix access or get a corrected file from the seller. If that is not possible, our authorized team will review your refund request. I can't confirm the outcome in advance, but I will keep you updated.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በ{{product_name}} (ትዕዛዝ {{order_id}}) ላይ ችግር ስላጋጠመዎት ይቅርታ እንጠይቃለን።

ለመርዳት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የችግሩን አጭር ማብራሪያ (ለምሳሌ፦ ሊንኩ አይሰራም፣ ፋይሉ አይከፈትም፣ ወይም ይዘቱ እንደተገለጸው አይደለም)
2. የሚታየውን የስህተት መልዕክት ወይም ችግሩን የሚያሳይ ስክሪንሾት
3. ፋይሉን ለመክፈት የሚጠቀሙበትን መሣሪያ (ስልክ ወይም ኮምፒውተር)

በብዙ አጋጣሚዎች ተደራሽነቱን ማስተካከል ወይም ከሻጩ የተስተካከለ ፋይል ማግኘት እንችላለን። ይህ የማይቻል ከሆነ ስልጣን ያለው ቡድናችን የተመላሽ ገንዘብ ጥያቄዎን ይገመግማል። ውጤቱን አስቀድሜ ማረጋገጥ ባልችልም ሂደቱን አሳውቅዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about {{product_name}}. Please tell me what's wrong (link, file or content), send a screenshot, and tell me your device. We'll try to fix it first; otherwise our team reviews a refund. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ {{product_name}} ይቅርታ። እባክዎ ችግሩን (ሊንክ፣ ፋይል ወይም ይዘት) ይንገሩኝ፣ ስክሪንሾት ይላኩ፣ መሣሪያዎንም ይጥቀሱ። መጀመሪያ ለማስተካከል እንሞክራለን፤ ካልተቻለ ቡድናችን ጥያቄውን ይገመግማል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}} for {{product_name}}. We are still working on your request with the relevant team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ {{product_name}} (የጉዳይ ቁጥር {{ticket_id}}) የሚሰጥ መረጃ ነው። ጥያቄዎን ከሚመለከተው ቡድን ጋር አሁንም እየሰራንበት ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Access not granted after successful payment, broken links, platform download errors → **Technical / Engineering**.
- Wrong/corrupted file that the seller must replace → **Seller Operations**.
- Refund decision needed → **Senior Support / Supervisor (L2)**.
- Copyright complaint or pirated content → **Trust & Safety**.
- Same buyer requesting refunds on many digital products after downloading → **Trust & Safety** (refund abuse review).

## Resolution Procedure
1. If fixed: confirm the buyer can now open the full content; ask them to confirm.
2. If a decision was made: communicate it (`ref-final-decision-communication`).
3. If refunded: confirm whether access should be removed (per the decision) and that payment status shows **Refund Pending/Refunded**.
4. Record the root cause (link, file, content, copyright, change of mind).

## Policy Pending Approval
- Decide refund eligibility for digital products after download/access.
- Decide download limits and how long access lasts.
- Decide whether access is revoked when a refund is approved.
- Decide what counts as "not as described" for digital content.

## Internal Notes
- Always try to fix access before discussing money; most digital complaints are access problems.
- Do not download or forward paid files to anyone outside the review process.
- A buyer who downloaded the full content and then claims it "never worked" without any error evidence should be reviewed carefully — but stay polite and neutral.
