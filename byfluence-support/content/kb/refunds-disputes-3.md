<!-- doc -->
# Refund Request Rejected
id: ref-refund-rejected
type: article
category: refunds-disputes
subcategory: decisions
audience: buyer
priority: medium
department: support_l2
features: refunds
tags: refund rejected, refund denied, why was my refund refused, refund declined, no refund, ተመላሽ ተከልክሏል, ጥያቄዬ ተቀባይነት አላገኘም
related: ref-final-decision-communication, ref-customer-disagrees-decision, ref-evidence-collection, ref-eligibility, ref-dispute-escalation
templates: tpl-refund-rejected, tpl-acknowledge-complaint, tpl-escalation-notification
policy_pending: yes

## Summary
Authorized personnel decided not to refund the customer. This article covers how to explain a rejection clearly and respectfully, and what the customer can do next.

## Issue Description
A rejection is the most difficult refund message to deliver. The customer usually feels they lost money and may feel Byfluence sided with the seller. The agent's job is to explain the decision, its main reason, and the available next step — **without** changing the decision, apologising for the decision itself, or blaming the seller or the review team.

## Possible Causes
Typical reasons authorized personnel record (use only the one actually recorded):
- Evidence shows the service or product was delivered as described
- The customer did not attend or did not respond, and the seller did attend
- The evidence provided was insufficient or could not be verified
- The request concerned a transaction that did not go through Byfluence
- The issue was resolved another way (rescheduled session, replacement item, file fixed)
- Signs that the request was not genuine (do not state this directly — see Internal Notes)

## Information to Collect
- The decision record: decision, recorded reason, who decided, date
- Whether the customer has new evidence that was not part of the review

## Troubleshooting Steps
1. Read the decision record. If no reason is recorded, ask L2 for one before replying — never send a rejection without a reason.
2. Prepare the message in the customer's language (Amharic by default). Translate the reason into plain words; avoid internal terms.
3. Send the rejection using the response below (or `tpl-refund-rejected`). For phone/Telegram voice, explain calmly and then send it in writing too.
4. If the customer disagrees, acknowledge their feelings and follow `ref-customer-disagrees-decision`. Do not debate the evidence.
5. If they send **new** evidence, add it to the ticket and send it to L2 for a review — do not reopen the decision yourself.
6. Record that the decision was communicated, the channel, and the customer's reaction.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your patience while we reviewed your refund request for {{product_name}} (case {{ticket_id}}).

Our authorized team has carefully reviewed the information from you and from the seller. Unfortunately, they were not able to approve a refund in this case. The main reason is: [insert the recorded reason in plain words].

I understand this is not the answer you were hoping for. If you have new information or evidence that was not part of the review, you can send it to us by replying to this message with your case number, and we will make sure it is reviewed.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ለ{{product_name}} (የጉዳይ ቁጥር {{ticket_id}}) ያቀረቡትን የተመላሽ ገንዘብ ጥያቄ እስክንገመግም ድረስ ስለ ትዕግስትዎ እናመሰግናለን።

ስልጣን ያለው ቡድናችን ከእርስዎም ከሻጩም የቀረበውን መረጃ በጥንቃቄ ገምግሟል። ይሁን እንጂ በዚህ ጉዳይ ላይ ተመላሽ ገንዘብ መፍቀድ አልተቻለም። ዋናው ምክንያት፦ [የተመዘገበውን ምክንያት በቀላል ቋንቋ እዚህ ያስገቡ]።

ይህ እርስዎ የጠበቁት ምላሽ እንዳልሆነ እረዳለሁ። በግምገማው ያልተካተተ አዲስ መረጃ ወይም ማስረጃ ካለዎት፣ የጉዳይ ቁጥርዎን ይዘው ለዚህ መልዕክት ምላሽ በመስጠት ሊልኩልን ይችላሉ፤ እንዲገመገም እናደርጋለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, our team reviewed case {{ticket_id}} and couldn't approve a refund because [reason]. I know this is disappointing. If you have new evidence, reply with it and we'll make sure it's reviewed.

## Short Response (AM)
ሰላም {{customer_name}}፣ ቡድናችን ጉዳይ ቁጥር {{ticket_id}}ን ገምግሞ በ[ምክንያት] ምክንያት ተመላሽ መፍቀድ አልቻለም። ይህ እንደሚያሳዝን እረዳለሁ። አዲስ ማስረጃ ካለዎት ይላኩልን፤ እንዲገመገም እናደርጋለን።

## Follow-Up Response (EN)
Hello {{customer_name}}, thank you for the additional information for case {{ticket_id}}. I have added it to your case and sent it to our review team. We will let you know the result by {{follow_up_time}}. Until then, the earlier decision remains in place.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ለጉዳይ ቁጥር {{ticket_id}} ተጨማሪ መረጃ ስለላኩልን እናመሰግናለን። ወደ ጉዳይዎ አክዬ ለግምገማ ቡድናችን ልኬዋለሁ። ውጤቱን እስከ {{follow_up_time}} እናሳውቅዎታለን። እስከዚያው ድረስ ቀደም ሲል የተሰጠው ውሳኔ ይቀጥላል።

## Escalation Conditions
- No recorded reason for the rejection → **L2** before replying.
- Customer provides new evidence → **L2** for review.
- Customer requests an appeal or a supervisor → `ref-customer-disagrees-decision` (**L2**).
- Customer threatens legal action, media exposure, or a bank chargeback → **L2**, who may involve **Management** or **Payments & Finance**.
- Customer becomes abusive or threatening → `tns-harassment` / `tns-threats-safety`.

## Resolution Procedure
1. Confirm the rejection message was sent in writing in the customer's language.
2. Record the channel, date and the customer's response.
3. If no new evidence or appeal follows, resolve the ticket with outcome "Refund rejected — communicated".

## Policy Pending Approval
- Decide whether customers have a formal appeal right and any deadline for it.
- Approve standard rejection reasons and their customer-facing wording.
- Decide whether rejected customers may be offered goodwill alternatives (and who authorizes them).

## Internal Notes
- Never say "the seller proved you wrong" or "you are lying". If the reason is suspected abuse, the customer-facing reason is "we were not able to verify the claim with the information available".
- Do not apologise for the decision ("sorry we rejected you") — apologise for the experience. Do not say "I agree with you but...".
- Do not share the seller's evidence (e.g., their screenshots) with the buyer unless L2 approves; it may contain personal data.

<!-- doc -->
# Buyer and Seller Disagree
id: ref-buyer-seller-disagreement
type: article
category: refunds-disputes
subcategory: disputes
audience: both
priority: high
department: support_l2
features: refunds
tags: dispute, buyer seller conflict, seller says delivered buyer says no, disagreement, he said she said, complaint against seller, ክርክር, አለመግባባት, ሻጩ አይስማማም
related: ref-dispute-investigation, ref-evidence-collection, ref-seller-disputes-refund, ref-dispute-escalation, ref-tsg-dispute-handling-master
templates: tpl-acknowledge-complaint, tpl-request-screenshot, tpl-escalation-notification
policy_pending: yes

## Summary
The buyer and the seller give conflicting accounts of what happened (e.g., "the consultant never joined" vs. "I was there, the buyer didn't come"). Support must stay neutral, collect evidence from both sides, and route the case for an authorized decision.

## Issue Description
Disputes are where Byfluence's "Trust" principle is tested. Both parties are customers: the buyer paid and expects value; the seller depends on earnings and reputation. Support must never take a side, never share one party's personal data with the other, and never promise an outcome. When a dispute is open, the payment may show status **Disputed** and the seller's earnings for that transaction may stay **pending** until it is resolved.

## Possible Causes
- Genuine misunderstanding: time zone, wrong Meet link, different expectations of the session
- Description mismatch: listing unclear or misleading
- Delivery confusion: item delivered to the wrong person, or delivery marked complete wrongly
- Quality disagreement: product/service delivered, but the buyer is unhappy with the quality
- One party is not telling the truth (buyer refund abuse or seller fraud)
- Off-platform contact led to a separate arrangement that went wrong

## Information to Collect
**From the buyer**
- Their account of events with dates and times, and the outcome they want
- Evidence: screenshots, photos, Meet screen, Byfluence messages
**From the seller**
- Their account of events with dates and times
- Evidence: proof of delivery/attendance, messages, files delivered, listing at time of purchase
**From the records**
- Order/booking record, status history, payment status, listing (current and, if available, previous version), message history on Byfluence

> [!WARNING] Never ask either party for passwords, OTP codes, PINs or card numbers. Never forward one party's phone number, email, address or ID documents to the other.

## Troubleshooting Steps
1. Acknowledge the complaint to the party who raised it (`tpl-acknowledge-complaint`) and create one dispute ticket linking both parties.
2. Lock in the facts that cannot change later: screenshot the listing, note the booking/order status history and payment status at this moment.
3. Ask the complaining party for their account and evidence (see `ref-evidence-collection`).
4. Ask the other party for their account and evidence, using neutral wording ("we received a report about booking {{consultation_id}} and would like your account of what happened"). Do not repeat accusations or share the other party's evidence.
5. Compare: where do the accounts agree? Where do they conflict? What does the record support?
6. If the dispute can be solved practically without a refund decision (reschedule, resend file, replace item) **and both agree in writing**, record the agreement and ask L2 to confirm.
7. Otherwise, escalate to **L2** with a neutral case summary (see `ref-dispute-investigation` for the format).
8. Keep both parties updated with the same level of information and the same tone.

- [ ] Single dispute ticket created
- [ ] Listing and records captured
- [ ] Buyer statement + evidence
- [ ] Seller statement + evidence
- [ ] Neutral summary written
- [ ] Escalated to L2

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand there is a disagreement about {{product_name}}, and I want to make sure it is handled fairly.

We review every dispute by listening to both sides and looking at the records and evidence. To make sure your side is fully considered, please send me:
1. Your account of what happened, with dates and times
2. Any screenshots, photos or messages that support it
3. The outcome you are asking for

We will also request information from the other party. Your personal contact details will not be shared with them. Our authorized team will then make a decision, and I will keep you updated.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ስለ {{product_name}} አለመግባባት እንደተፈጠረ ተረድቻለሁ፤ ጉዳዩ በፍትሃዊነት እንዲታይ አደርጋለሁ።

እያንዳንዱን ክርክር የምንገመግመው የሁለቱንም ወገኖች ሀሳብ በመስማት እና መዝገቦችንና ማስረጃዎችን በመመልከት ነው። የእርስዎ ሀሳብ ሙሉ በሙሉ እንዲታይ እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የተፈጠረውን ሁኔታ ከቀን እና ከሰዓት ጋር
2. የሚደግፉ ስክሪንሾቶች፣ ፎቶዎች ወይም መልዕክቶች
3. የሚጠይቁትን መፍትሄ

ከሌላኛው ወገንም መረጃ እንጠይቃለን። የእርስዎ የግል የመገኛ መረጃ ለእነሱ አይሰጥም። ከዚያም ስልጣን ያለው ቡድናችን ውሳኔ ይሰጣል፤ ሂደቱንም አሳውቅዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, we review every dispute by hearing both sides. Please send your account with dates/times, any evidence, and the outcome you want. Your contact details won't be shared with the other party. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እያንዳንዱን ክርክር የምናየው የሁለቱንም ወገኖች ሀሳብ ሰምተን ነው። እባክዎ የተፈጠረውን ከቀን/ሰዓት ጋር፣ ማስረጃዎችን እና የሚፈልጉትን መፍትሄ ይላኩ። የመገኛ መረጃዎ ለሌላኛው ወገን አይሰጥም። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have received the information and are completing the review with input from both parties. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። መረጃውን ተቀብለናል፤ ከሁለቱም ወገኖች በተገኘ መረጃ ግምገማውን እያጠናቀቅን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Every buyer–seller dispute that is not settled by written agreement → **Senior Support / Supervisor (L2)**.
- Either party is abusive, threatening or harassing the other → **Trust & Safety**.
- Signs of fraud (edited screenshots, fake delivery proof, identity mismatch) → **Trust & Safety**.
- Dispute affects the seller's payout or the seller already withdrew → **Payments & Finance**.
- High value, legal threats, or the same seller/buyer in multiple disputes → **L2**, who may involve **Management** or **Seller Operations**.

## Resolution Procedure
1. A decision (or written mutual agreement confirmed by L2) is recorded.
2. Both parties receive the outcome in neutral language (`ref-final-decision-communication`).
3. Approved adjustments (refund, release of seller earnings) are processed by Payments and confirmed.
4. Record root cause and whether the listing or a party needs follow-up by Seller Operations / Trust & Safety.

## Policy Pending Approval
- Decide the standard of proof for disputes (what evidence outweighs what).
- Decide response deadlines for each party and what happens if one party does not respond.
- Decide whether seller earnings are automatically held while a dispute is open.
- Decide who has final authority on disputes and whether parties can appeal.

## Internal Notes
- Neutral language only: "the buyer reports", "the seller states". Never "the buyer is right" or "the seller lied".
- Give each party a fair chance to respond, and record when you asked and when they answered.
- If one party contacts support many times and the other once, that does not make the first party more credible.
- Sellers may ask "who complained?" for a public or group booking. Don't confirm details beyond the specific booking reference they already know.

<!-- doc -->
# Seller Disputes a Buyer's Refund Request
id: ref-seller-disputes-refund
type: article
category: refunds-disputes
subcategory: disputes
audience: seller
priority: high
department: support_l2
features: refunds, seller-withdrawals
tags: seller disputes refund, seller refuses refund, unfair refund, buyer lying, seller objects, earnings held due to dispute, ሻጭ ተመላሹን ይቃወማል, ገዢው ዋሽቷል
related: ref-buyer-seller-disagreement, ref-evidence-collection, ref-dispute-investigation, out-payout-hold-restriction, ref-abuse-of-refunds
templates: tpl-acknowledge-complaint, tpl-request-screenshot, tpl-escalation-notification
policy_pending: yes

## Summary
A seller objects to a buyer's refund request (or to a refund that was already approved), says they delivered as promised, and/or asks why their earnings are on hold.

## Issue Description
Sellers are customers too, and their income depends on fair treatment. A seller may learn about a refund request when Byfluence asks for their account of events, when earnings show as pending longer than usual, or when a refund has already been approved. They may be upset, feel accused, or worry about their reputation. Support must take the seller's objection seriously, collect their evidence, and route it — without revealing the buyer's personal data or promising either outcome.

## Possible Causes
- The seller genuinely delivered and believes the buyer is mistaken or abusing refunds
- The seller and buyer understood the listing differently
- The seller was not informed of the complaint before the decision
- The seller's earnings are pending because of the open dispute or settlement rules
- A refund was approved and the seller was not given the reason

## Information to Collect
- Seller name and registered contact; order/booking ID ({{order_id}} / {{consultation_id}})
- The seller's account of events, with dates and times
- Seller evidence: proof of attendance (e.g., their Meet screen at the scheduled time), delivery confirmation, file delivery record, messages with the buyer on Byfluence
- The listing as it was at the time of purchase (if the seller kept it)
- What the seller is asking for (refund not to be approved, decision reviewed, earnings released)

> [!WARNING] Never ask for passwords, OTP codes or PINs. Never share the buyer's phone, email, address or the buyer's evidence files with the seller without L2 approval.

## Troubleshooting Steps
1. Confirm the seller's identity through registered details.
2. Find the related ticket/dispute. If one exists, add the seller's statement to it; do not open a separate case.
3. Check the stage:
   - **Request under review** → collect the seller's evidence and add it before the decision.
   - **Already decided** → this is an appeal from the seller side; follow `ref-customer-disagrees-decision`.
   - **Earnings pending, no dispute** → this may be normal settlement; see `out-payout-hold-restriction`.
4. Explain neutrally that disputes are reviewed by authorized personnel using information from both sides, and that sellers' earnings for a disputed transaction may stay pending until the case is resolved (confirmed concept: earnings are pending until release conditions are met).
5. Escalate the seller's statement and evidence to **L2**.
6. If the seller suspects refund abuse by the buyer, note it and let L2 decide whether to involve Trust & Safety (`ref-abuse-of-refunds`). Do not confirm or comment on the buyer's history.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support and for sharing your side of what happened with order/booking {{order_id}}.

Every refund request is reviewed by our authorized team using information from both the buyer and the seller. Your input is important to a fair decision. Please send me:
1. Your account of what happened, with dates and times
2. Any evidence you have, such as proof that you attended the session or delivered the item or file, and your messages with the buyer on Byfluence

While a case is under review, the earnings for this transaction may stay pending. This is part of our normal review process and is not a penalty.

Your case number is {{ticket_id}}. I will keep you updated.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እና በትዕዛዝ/ቀጠሮ {{order_id}} ላይ የተፈጠረውን ከእርስዎ ወገን ስላካፈሉን እናመሰግናለን።

እያንዳንዱ የተመላሽ ገንዘብ ጥያቄ ስልጣን ባለው ቡድናችን ከገዢውም ከሻጩም በተገኘ መረጃ ይገመገማል። የእርስዎ ሀሳብ ለፍትሃዊ ውሳኔ በጣም አስፈላጊ ነው። እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የተፈጠረውን ሁኔታ ከቀን እና ከሰዓት ጋር
2. ያሉዎትን ማስረጃዎች፣ ለምሳሌ ምክክሩ ላይ እንደተገኙ ወይም ዕቃውን/ፋይሉን እንዳደረሱ የሚያሳይ ማስረጃ እና በByfluence ላይ ከገዢው ጋር የተለዋወጧቸውን መልዕክቶች

አንድ ጉዳይ በግምገማ ላይ እያለ የዚህ ግብይት ገቢ በተያዘ (pending) ሁኔታ ሊቆይ ይችላል። ይህ የመደበኛ የግምገማ ሂደታችን አካል ነው እንጂ ቅጣት አይደለም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ሂደቱን አሳውቅዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for sharing your side. Every case is reviewed using input from both buyer and seller. Please send your account with dates/times and any proof of delivery or attendance. Earnings may stay pending during review — this isn't a penalty. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ሀሳብዎን ስላካፈሉን እናመሰግናለን። እያንዳንዱ ጉዳይ ከገዢውም ከሻጩም በተገኘ መረጃ ይገመገማል። እባክዎ የተፈጠረውን ከቀን/ሰዓት ጋር እና የማድረስ ወይም የመገኘት ማስረጃ ይላኩ። በግምገማ ወቅት ገቢው ተይዞ ሊቆይ ይችላል — ቅጣት አይደለም። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your statement and evidence have been added to the review. The decision has not been made yet; we will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ያቀረቡት ሀሳብ እና ማስረጃ ወደ ግምገማው ተጨምሯል። እስካሁን ውሳኔ አልተሰጠም፤ እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Seller statement and evidence → **L2** (attach to the existing dispute).
- Seller objects to a decision already made → **L2** as an appeal.
- Seller's withdrawal is held or reversed because of the refund → **Payments & Finance**.
- Seller claims a pattern of refund abuse by the same buyer → **L2**, who may involve **Trust & Safety**.
- Seller threatens the buyer or contacts them off-platform about the dispute → **Trust & Safety**.

## Resolution Procedure
1. Seller evidence attached to the dispute before the decision (or appeal recorded).
2. Decision communicated to the seller in neutral terms, including effect on the transaction's earnings.
3. Record outcome and any follow-up (listing correction, seller education, Trust & Safety review).

## Policy Pending Approval
- Decide how long seller earnings stay pending while a dispute is open.
- Decide whether sellers are notified of every refund request and how long they have to respond.
- Decide whether sellers can appeal decisions and who reviews seller appeals.
- Decide how refunds affect seller performance records or status.

## Internal Notes
- Do not tell the seller what the buyer claimed in detail or share the buyer's files; summarise neutrally ("the buyer reports the session did not take place").
- Never contact a buyer on a seller's behalf to "convince" them to withdraw a complaint.
- A seller who becomes threatening toward a buyer must be escalated to Trust & Safety immediately, regardless of the merits of the dispute.

<!-- doc -->
# Suspected Refund Abuse
id: ref-abuse-of-refunds
type: article
category: refunds-disputes
subcategory: disputes
audience: internal
priority: high
department: trust_safety
features: refunds
tags: refund abuse, refund fraud, serial refunder, fake refund claim, repeated refunds, friendly fraud, wardrobing, የተመላሽ ገንዘብ ማጭበርበር, ተደጋጋሚ ተመላሽ
related: ref-dispute-investigation, ref-evidence-collection, tns-report-fraud, ref-refund-to-different-account, pay-chargeback
templates: tpl-request-screenshot, tpl-escalation-notification
policy_pending: yes

## Summary
Internal guidance for recognising and routing possible refund abuse — by buyers (false claims, repeated refunds) or by sellers (collusion, fake orders) — without accusing anyone.

## Issue Description
Most refund requests are genuine. A small number are not: buyers claiming a service did not happen when it did, claiming items were not received, using a product and then requesting a refund, or opening a refund and a bank chargeback for the same payment. Sellers can also abuse the system, for example by creating fake buyer accounts to move money. Support agents are the first to see these patterns, but they **do not investigate, accuse or punish**. They note the signals, keep the tone neutral with the customer, and route to Trust & Safety.

## Possible Causes
Signals to note (none of them is proof on its own):
- **Buyer side**
  - Several refund requests in a short period, especially across different sellers
  - Same complaint wording on different orders
  - Evidence that looks edited, cropped to hide dates, or reused from another case
  - Refund request plus a chargeback with the bank for the same payment
  - Digital product fully downloaded, then "never worked" without error evidence
  - Pressure to send the refund to a different account (see `ref-refund-to-different-account`)
  - Claims that contradict the records (e.g., says never joined, but joined from their own account per available logs)
- **Seller side / collusion**
  - Buyer and seller accounts sharing the same phone, email pattern, device or payment account
  - A seller who repeatedly "agrees" to refunds right after payouts
  - Many new buyer accounts purchasing from one new seller and then requesting refunds

## Information to Collect
- All related tickets and transaction references for the account(s)
- The specific signals observed and where you saw them (ticket number, screenshot, record)
- The customer's evidence as received (do not edit, rename or compress)

> [!WARNING] Never ask for passwords, OTP codes or PINs. Do not ask the customer intrusive questions to "test" them, and do not search their personal social media.

## Troubleshooting Steps
1. Handle the customer exactly as you would any refund case: polite, neutral, same evidence requests (`ref-evidence-collection`).
2. In **internal notes only**, list the signals you observed, factually ("3 refund requests in this ticket queue in the last month: #A, #B, #C").
3. Do not tell the customer they are suspected, and do not delay their acknowledgement.
4. Escalate to **Trust & Safety** with the list of signals and linked tickets; keep **L2** informed because the refund decision stays with authorized personnel.
5. If a chargeback was also opened, inform **Payments & Finance** (`pay-chargeback`).
6. If you see possible collusion (buyer–seller links), escalate to **Trust & Safety** and **Seller Operations**.
7. Continue to give the customer normal status updates until a decision is communicated.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your message about case {{ticket_id}}.

To complete the review of your request, our team needs a little more information. Please send:
1. The original, uncropped screenshots or photos showing the problem, including the date and time where visible
2. Any messages exchanged with the seller on Byfluence about this order

Your request will be reviewed by our authorized team once we have this information. We will keep you updated.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጉዳይ ቁጥር {{ticket_id}} ስለላኩልን መልዕክት እናመሰግናለን።

የጥያቄዎን ግምገማ ለማጠናቀቅ ቡድናችን ተጨማሪ መረጃ ያስፈልገዋል። እባክዎ የሚከተሉትን ይላኩ፦
1. ችግሩን የሚያሳዩ፣ ያልተቆረጡ የመጀመሪያዎቹ ስክሪንሾቶች ወይም ፎቶዎች (ቀን እና ሰዓት የሚታይ ከሆነ ጨምሮ)
2. ስለዚህ ትዕዛዝ በByfluence ላይ ከሻጩ ጋር የተለዋወጧቸው መልዕክቶች

ይህ መረጃ እንደደረሰን ጥያቄዎ ስልጣን ባለው ቡድናችን ይገመገማል። ሂደቱን እናሳውቅዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, to complete the review of case {{ticket_id}}, please send the original uncropped screenshots/photos (with date and time if visible) and any Byfluence messages with the seller. Thank you!

## Short Response (AM)
ሰላም {{customer_name}}፣ የጉዳይ ቁጥር {{ticket_id}} ግምገማን ለማጠናቀቅ እባክዎ ያልተቆረጡ የመጀመሪያ ስክሪንሾቶችን/ፎቶዎችን (ቀን እና ሰዓት ከታየ) እና ከሻጩ ጋር በByfluence የተለዋወጧቸውን መልዕክቶች ይላኩ። እናመሰግናለን!

## Escalation Conditions
- Any suspected refund abuse → **Trust & Safety** (with signals listed), and keep **L2** informed.
- Refund plus chargeback on the same payment → **Payments & Finance**.
- Possible buyer–seller collusion → **Trust & Safety** and **Seller Operations**.
- Organised pattern (many accounts, same payment account) → **Trust & Safety**, priority Critical; supervisor notified.

## Resolution Procedure
1. Trust & Safety records its assessment; L2/authorized personnel record the refund decision.
2. The customer receives the decision through normal channels (`ref-final-decision-communication`), never an accusation.
3. Any account action (restriction, suspension) is decided and communicated by Trust & Safety / Seller Operations, not front-line support.

## Policy Pending Approval
- Define what counts as refund abuse and the thresholds that trigger a review.
- Decide the actions available (warnings, refund limits, account restriction) and who authorizes them.
- Decide how suspected abuse is communicated to the customer, if at all.

## Internal Notes
- "Suspected" is not "confirmed". Many repeated requests come from customers who genuinely had bad luck or bought from a bad seller.
- Never write accusations in customer-visible fields. Keep observations factual and in internal notes.
- Do not refuse to acknowledge or log a refund request because you suspect abuse — the log is evidence too.

<!-- doc -->
# How to Investigate a Dispute
id: ref-dispute-investigation
type: article
category: refunds-disputes
subcategory: decisions
audience: internal
priority: high
department: support_l2
features: refunds
tags: dispute investigation, investigate complaint, case review, dispute summary, neutral investigation, ምርመራ, የክርክር ማጣራት
related: ref-evidence-collection, ref-buyer-seller-disagreement, ref-dispute-escalation, ref-final-decision-communication, ref-tsg-dispute-handling-master
templates: tpl-acknowledge-complaint, tpl-request-screenshot, tpl-escalation-notification
policy_pending: yes

## Summary
Step-by-step internal method for investigating a refund dispute so that authorized personnel receive a complete, neutral, verifiable case file.

## Overview
The investigation is **fact-finding, not judging**. Front-line agents (L1) and Senior Support (L2) prepare the case; authorized personnel decide. A good case file lets a reviewer decide without having to contact anyone again.

### Principles
- **Neutral**: both parties are customers; describe, don't judge.
- **Verifiable**: prefer system records over screenshots; prefer original files over forwarded ones.
- **Complete**: both sides heard, or a record that one side did not respond.
- **Private**: each party sees only their own data.
- **Documented**: every request, response and date is in the ticket.

## Information to Collect
- Transaction: reference, amount, method, status and status history
- Order/booking: ID, offering type, listing at time of purchase, status history (created, confirmed, rescheduled, cancelled, completed)
- Buyer statement + evidence (`ref-evidence-collection`)
- Seller statement + evidence
- Byfluence message history between the parties
- Related tickets for either party (same listing, same seller, same buyer)
- Any technical incident on that date (check Announcements / Technical)

## Troubleshooting Steps
### Step 1 — Open and freeze
1. Create or confirm a single dispute ticket; link both parties' accounts and the transaction.
2. Capture the listing and records as they are now (screenshots saved to the ticket with the time captured).
3. Ask Payments whether seller earnings for this transaction should be held (L2 decision; do not promise either party).

### Step 2 — Hear both sides
1. Ask the complaining party for their statement and evidence.
2. Ask the other party with the same neutral wording. Record the date and time of each request.
3. If a party does not respond after the follow-up time you set, send one reminder and record it.

### Step 3 — Verify
1. Match each claim to a record: "Buyer says booking was for 3 PM" → booking record shows the time and time zone.
2. Check the evidence quality: original vs. cropped, dates visible, consistent with records, signs of editing.
3. Check for technical causes (Meet link generation, notification failures, delivery records).
4. Note anything you cannot verify as "unverified" — not as "false".

### Step 4 — Write the case summary
Use this format in the internal note:
```
DISPUTE SUMMARY — {{ticket_id}}
Transaction: <ref> · <amount> · <method> · status <status>
Offering: <consultation / product / digital> · listing <id>
Buyer claims: <one or two sentences>
Seller states: <one or two sentences>
Records show: <facts from system records>
Agreed facts: <...>
Disputed facts: <...>
Evidence received: buyer <list> · seller <list>
Unverified items: <...>
Related tickets / patterns: <...>
Requested outcome: <buyer wants ... / seller wants ...>
Open risks: <fraud signals, payout already withdrawn, time-sensitive session>
```

### Step 5 — Route
1. Send to **L2** (or the authorized reviewer named by L2).
2. Add Trust & Safety, Payments, Technical or Seller Operations if their facts are needed.
3. Update both parties that the case is under review.

## Recommended Response (EN)
Hello {{customer_name}},

We have received a report about {{product_name}} (reference {{order_id}}), and as part of our standard review we would like to hear your account of what happened.

Please reply with:
1. Your description of events, with dates and times
2. Any evidence you have, such as screenshots, photos or Byfluence messages

Your information will be used only to review this case. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ {{product_name}} (መለያ ቁጥር {{order_id}}) ሪፖርት ደርሶናል፤ በመደበኛ የግምገማ ሂደታችን መሠረት የተፈጠረውን ከእርስዎ ወገን መስማት እንፈልጋለን።

እባክዎ የሚከተሉትን ይላኩልን፦
1. የተፈጠረውን ሁኔታ ከቀን እና ከሰዓት ጋር
2. ያሉዎትን ማስረጃዎች፣ ለምሳሌ ስክሪንሾቶች፣ ፎቶዎች ወይም የByfluence መልዕክቶች

የሚሰጡን መረጃ የሚውለው ይህን ጉዳይ ለመገምገም ብቻ ነው። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, we received a report about {{order_id}} and would like your account of what happened, with dates/times and any evidence. It will be used only for this review. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ {{order_id}} ሪፖርት ደርሶናል፤ የተፈጠረውን ከቀን/ሰዓት እና ከማስረጃ ጋር ከእርስዎ መስማት እንፈልጋለን። መረጃው የሚውለው ለዚህ ግምገማ ብቻ ነው። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Complete case file → **L2 / authorized reviewer**.
- Fraud signals or edited evidence → **Trust & Safety**.
- Payment status questions, holds, provider records → **Payments & Finance**.
- Platform error suspected (Meet link, booking time, notifications, downloads) → **Technical / Engineering**.
- Listing accuracy or seller conduct pattern → **Seller Operations**.
- High value, legal, regulatory or reputational risk → **Management** via L2.

## Resolution Procedure
1. The case summary is complete and reviewed by L2.
2. The decision is recorded with reason and decision maker.
3. Both parties informed (`ref-final-decision-communication`); approved adjustments processed.
4. Lessons recorded (e.g., unclear listing, time-zone bug) and shared with the supervisor.

## Policy Pending Approval
- Approve the standard of proof and how conflicting evidence is weighed.
- Approve response deadlines for parties and the default outcome when one party does not respond.
- Approve who may view the full case file (both parties' evidence).
- Approve retention rules for dispute evidence.

## Internal Notes
- Write the summary so that someone who has never seen the case could decide in a few minutes.
- Do not include your personal opinion in the summary. If you have a professional observation (e.g., "screenshot clock shows a different time zone"), label it "Agent observation".
- Do not contact parties by personal phone or personal Telegram. Use official channels only.
