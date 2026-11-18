<!-- doc -->
# Partial Refunds
id: ref-partial-refund
type: article
category: refunds-disputes
subcategory: refund-types
audience: both
priority: medium
department: support_l2
features: refunds
tags: partial refund, only part of my money, why not full refund, deduction, refund less than paid, ከፊል ተመላሽ, ሙሉ ገንዘቤ አልተመለሰም
related: ref-full-refund, ref-eligibility, ref-final-decision-communication, ref-customer-disagrees-decision, pay-refund-processing
templates: tpl-refund-partial, tpl-refund-status-update, tpl-escalation-notification
policy_pending: yes

## Summary
How to handle partial refunds: a request for part of the amount, a decision to refund only part, or a customer asking why the refunded amount is lower than what they paid.

## Overview
A partial refund returns part of the amount paid. It can come up in three ways:

1. **The customer asks for one** — e.g., the session ended early, one item in an order was damaged, part of a digital course is missing.
2. **Authorized personnel decide on one** — after reviewing evidence from both sides.
3. **The customer received less than they expected** — and asks why.

Whether Byfluence deducts any fees from refunds (platform fees, payment-provider fees, cancellation fees) is **not confirmed**. Agents therefore never calculate, propose or negotiate a partial-refund amount. Agents relay the request and, once decided, explain the authorized amount and the reason that authorized personnel recorded.

## Information to Collect
- Order/booking ID and transaction reference; amount paid ({{amount}}) and payment method
- What part of the purchase the customer says was not delivered or was defective
- Evidence for that part (photos, screenshots, session timing)
- For "I got less than expected": the amount actually received, the date, and where it arrived (as shown on the customer's bank/mobile-money statement — they can hide unrelated lines)

> [!WARNING] Never ask for passwords, OTP codes, PINs or full card numbers. Never ask for a full bank statement — only the line that shows the refund.

## Troubleshooting Steps
1. Locate the transaction and any refund record in the admin dashboard.
2. Identify which situation applies:
   - **Customer requests a partial refund** → collect evidence, escalate to **L2** with the customer's proposed amount and reason. Do not agree or counter-offer.
   - **Decision is a partial refund** → read the recorded decision and reason; use `tpl-refund-partial` to explain it.
   - **Customer received less than the approved amount** → compare the approved amount with what the customer sees; escalate the difference to **Payments & Finance** with the reference.
   - **Customer received less than they paid, and the decision was a full refund** → **Payments & Finance** immediately (possible processing error or provider fee).
3. If the seller is offering a partial refund directly to the buyer ("I'll send you half"), stop: any settlement must go through Byfluence. See `tns-off-platform-payment-request`.
4. Record the amount paid, amount requested, amount approved, and amount received on the ticket.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your message about case {{ticket_id}}.

After reviewing your request, our authorized team approved a partial refund of {{amount}} for {{product_name}}. [Insert the reason recorded by the reviewing team in one or two plain sentences.]

The refund will be sent through {{payment_method}}. We will let you know as soon as it has been processed, and you can contact us at any time with your case number.

If you have new information that was not part of the review, please send it to us and we will make sure it is considered.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጉዳይ ቁጥር {{ticket_id}} ስለላኩልን መልዕክት እናመሰግናለን።

ጥያቄዎን ከገመገመ በኋላ ስልጣን ያለው ቡድናችን ለ{{product_name}} {{amount}} ከፊል ተመላሽ ገንዘብ እንዲመለስልዎ ወስኗል። [የገምጋሚው ቡድን የመዘገበውን ምክንያት በአንድ ወይም በሁለት ግልጽ ዓረፍተ ነገሮች እዚህ ያስገቡ።]

ተመላሹ ገንዘብ በ{{payment_method}} በኩል ይላካል። ሂደቱ እንደተጠናቀቀ እናሳውቅዎታለን፤ በማንኛውም ጊዜ የጉዳይ ቁጥርዎን ይዘው ሊያገኙን ይችላሉ።

በግምገማው ያልተካተተ አዲስ መረጃ ካለዎት፣ እባክዎ ይላኩልን፤ እንዲታይ እናደርጋለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, our team reviewed case {{ticket_id}} and approved a partial refund of {{amount}}. [Reason in one sentence.] It will go to {{payment_method}}; we'll confirm once processed.

## Short Response (AM)
ሰላም {{customer_name}}፣ ቡድናችን ጉዳይ ቁጥር {{ticket_id}}ን ገምግሞ {{amount}} ከፊል ተመላሽ ፈቅዷል። [ምክንያቱ በአንድ ዓረፍተ ነገር።] ገንዘቡ በ{{payment_method}} ይላካል፤ ሲጠናቀቅ እናሳውቅዎታለን።

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your request for a partial refund is still being reviewed by our authorized team. We have not made a decision yet, and we will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የከፊል ተመላሽ ገንዘብ ጥያቄዎ አሁንም ስልጣን ባለው ቡድናችን እየተገመገመ ነው። እስካሁን ውሳኔ አልተሰጠም፤ እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Any partial refund request → **Senior Support / Supervisor (L2)**.
- Amount received differs from the approved amount → **Payments & Finance**.
- Customer rejects the partial refund decision → follow `ref-customer-disagrees-decision` (L2).
- Seller tries to settle directly with the buyer outside Byfluence → **Trust & Safety**.

## Resolution Procedure
1. Confirm the approved amount and reason are recorded by authorized personnel.
2. Confirm Payments processed exactly the approved amount.
3. Send the decision and, once processed, the confirmation.
4. Record paid / requested / approved / received amounts and close.

## Policy Pending Approval
- Decide whether partial refunds are allowed for each offering type, and on what basis (time attended, items affected, content missing).
- Decide whether platform, provider or cancellation fees are deducted from refunds, and the approved wording to explain them.
- Decide who may approve partial refunds and up to what amount.
- Decide whether a seller may propose a partial refund through Byfluence, and how it is recorded.

## Internal Notes
- Never invent a reason for a deduction. If the decision record has no reason, ask L2 before replying.
- Do not say "the fee is non-refundable" unless a published policy says so — none does yet.
- The bracketed reason in the response must be replaced before sending; never send square brackets to a customer.

<!-- doc -->
# Full Refunds
id: ref-full-refund
type: article
category: refunds-disputes
subcategory: refund-types
audience: both
priority: medium
department: support_l2
features: refunds
tags: full refund, all my money back, complete refund, refund approved, refund entire amount, ሙሉ ተመላሽ, ገንዘቤ ሙሉ በሙሉ ይመለስ
related: ref-partial-refund, ref-refund-status, ref-final-decision-communication, pay-refund-processing, out-payout-hold-restriction
templates: tpl-refund-approved, tpl-refund-status-update
policy_pending: yes

## Summary
How to communicate and follow through on a full refund that authorized personnel have approved, and how to handle requests for a "full refund" before a decision exists.

## Overview
A full refund returns the whole amount the buyer paid for the order or booking. Situations where buyers commonly ask for a full refund: seller no-show, order cancelled by seller, item never delivered, digital product never accessible, duplicate payment. Even in these cases, **support agents do not approve the refund** — the case goes to authorized personnel.

Once a full refund is approved:
- **Payments & Finance** processes it through the original payment provider (unless a different method is authorized).
- The payment status should move to **Refund Pending**, then **Refunded**.
- The seller's pending earnings for that transaction are affected. If the seller was already paid out, Payments handles recovery — agents do not contact sellers about money recovery.

Whether a full refund includes every fee the buyer paid (platform fee, provider fee) is **not confirmed**. Only say "full refund" if the decision record says full refund.

## Information to Collect
- Ticket and decision record: who approved, approved amount, date
- Transaction reference, payment method ({{payment_method}}), amount ({{amount}})
- The account/number the original payment came from (from records — do not ask the customer to provide a new one)

## Troubleshooting Steps
1. Before telling the customer anything, confirm in the ticket that authorized personnel approved a **full** refund and recorded the amount.
2. Confirm Payments & Finance has received the processing request (or send it, if that is your team's process).
3. Send the approval message (`tpl-refund-approved`). Do not give a date unless Payments provided approved wording.
4. If the order was a consultation still marked upcoming, confirm with L2 that the booking is cancelled so the buyer is not charged or expected again.
5. Set a follow-up time to check the payment status.
6. When status is **Refunded**, send a short confirmation and close.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your patience while we reviewed case {{ticket_id}}.

Our authorized team has approved a full refund of {{amount}} for {{product_name}}. The refund will be returned through {{payment_method}}, the method you used to pay.

The time it takes to appear in your account depends on the payment provider. We will confirm with you once it has been processed: {{estimated_resolution_time}}.

If you do not see it after we confirm, please reply to this message with your case number and we will check it with our payments team.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ጉዳይ ቁጥር {{ticket_id}}ን እስክንገመግም ድረስ ስለ ትዕግስትዎ እናመሰግናለን።

ስልጣን ያለው ቡድናችን ለ{{product_name}} የከፈሉት {{amount}} ሙሉ በሙሉ እንዲመለስልዎ ፈቅዷል። ገንዘቡ የከፈሉበት ዘዴ በሆነው በ{{payment_method}} በኩል ይመለሳል።

ገንዘቡ በሂሳብዎ ላይ የሚታይበት ጊዜ በክፍያ አቅራቢው ይወሰናል። ሂደቱ እንደተጠናቀቀ እናረጋግጥልዎታለን፦ {{estimated_resolution_time}}።

ካረጋገጥንልዎ በኋላ ገንዘቡ ካልደረሰዎት፣ እባክዎ የጉዳይ ቁጥርዎን ይዘው ለዚህ መልዕክት ምላሽ ይስጡ፤ ከክፍያ ቡድናችን ጋር እናጣራለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, good news on case {{ticket_id}}: a full refund of {{amount}} has been approved and will go back to your {{payment_method}}. We'll confirm when it's processed.

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መልካም ዜና፦ {{amount}} ሙሉ ተመላሽ ተፈቅዷል፤ ወደ {{payment_method}} ሂሳብዎ ይመለሳል። ሂደቱ ሲጠናቀቅ እናሳውቅዎታለን።

## Follow-Up Response (EN)
Hello {{customer_name}}, your refund of {{amount}} for case {{ticket_id}} has now been processed by our payments team (reference {{transaction_id}}). Depending on your payment provider, it may take some time to appear. If you don't see it, please reply with your case number.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ለጉዳይ ቁጥር {{ticket_id}} የ{{amount}} ተመላሽ ገንዘብዎ በክፍያ ቡድናችን ተስተናግዷል (መለያ ቁጥር {{transaction_id}})። እንደ ክፍያ አቅራቢዎ ሁኔታ በሂሳብዎ ላይ ለመታየት ጊዜ ሊወስድ ይችላል። ካልደረሰዎት እባክዎ የጉዳይ ቁጥርዎን ይዘው ምላሽ ይስጡ።

## Escalation Conditions
- No authorized decision recorded but the customer insists they were promised a full refund → **L2** (check who promised it).
- Approved refund not processed → **Payments & Finance**.
- Seller already withdrew the earnings for this transaction → **Payments & Finance** (recovery is their decision, see `out-payout-hold-restriction`).
- Customer asks for the refund to a different account → `ref-refund-to-different-account` and **Trust & Safety**.

## Resolution Procedure
1. Confirm payment status **Refunded** in the admin dashboard (or written confirmation from Payments).
2. Send the processed confirmation (follow-up response above).
3. Record decision maker, amount, processing date and provider reference; resolve the ticket.

## Policy Pending Approval
- Confirm whether a full refund includes all fees paid by the buyer.
- Confirm the approved wording for refund processing times per payment method.
- Confirm how seller earnings are adjusted or recovered after a full refund.

## Internal Notes
- "Full refund" in a customer message must match the decision record exactly. If the record says "refund of booking amount", ask L2 whether that is the full amount the customer paid.
- Do not tell the customer the seller "will be charged" or "penalised" — that is internal.
- Keep the processed reference ({{transaction_id}}) on the ticket; the customer's bank may ask for it.

<!-- doc -->
# Checking Refund Status
id: ref-refund-status
type: article
category: refunds-disputes
subcategory: refund-status
audience: buyer
priority: low
department: support_l1
features: refunds
tags: refund status, where is my refund, refund update, refund pending, has my refund been approved, ተመላሽ ገንዘቤ የት ደረሰ, ሁኔታ
related: ref-refund-delay, ref-how-to-request-refund, ref-full-refund, pay-refund-processing, ref-final-decision-communication
templates: tpl-refund-status-update, tpl-refund-request-ack
policy_pending: yes

## Summary
A customer asks for an update on a refund request. The agent identifies which stage the case is in and gives an honest, specific update without promising a date.

## Overview
A refund case moves through these stages. Use the ticket and the payment status to tell which one applies:

| Stage | How to recognise it | What to tell the customer |
|---|---|---|
| 1. Request received, information missing | Ticket open, evidence incomplete | What is still needed from them |
| 2. Under review | Escalated to L2, no decision recorded | It is being reviewed; next update time |
| 3. Waiting for seller / other department | Ticket notes show seller or department contacted | Review is ongoing, includes the other party's input (no details) |
| 4. Decision made, not yet communicated | Decision recorded on ticket | Communicate via `ref-final-decision-communication` |
| 5. Approved, processing | Payment status **Refund Pending** | Approved and being processed |
| 6. Processed | Payment status **Refunded** | Processed; provider may take time to show it |
| 7. Rejected | Decision recorded as rejected | Follow `ref-refund-rejected` |
| 8. Disputed | Payment status **Disputed** (e.g., bank chargeback) | Follow `pay-chargeback` |

## Customer Steps
1. Have the case number ({{ticket_id}}) ready, or the order/booking ID.
2. Contact support through the same official channel if possible ({{support_channel}}).
3. If the refund was confirmed as processed, check the account statement for the original payment method.

## Troubleshooting Steps
1. Find the ticket by case number, order/booking ID, or the customer's registered email/phone. Confirm identity before sharing any detail.
2. Read the last internal note and decision record.
3. Check the payment status in the admin dashboard.
4. Identify the stage (table above) and reply with the matching update.
5. If the case has had no activity since its last promised follow-up, ping the owner (L2 or department) and tell the customer you have followed up.
6. If status is **Refunded** but the customer has nothing → `ref-refund-delay`.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for checking in about case {{ticket_id}}.

Here is the current status: [choose one]
- Your request is being reviewed by our authorized team, and we are gathering the information needed for a fair decision.
- Your refund of {{amount}} has been approved and is being processed by our payments team.
- Your refund of {{amount}} was processed on our side through {{payment_method}}. Depending on the provider, it may take some time to appear in your account.

We will contact you again by {{follow_up_time}}, or sooner if there is news.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጉዳይ ቁጥር {{ticket_id}} ስለጠየቁን እናመሰግናለን።

የአሁኑ ሁኔታ የሚከተለው ነው፦ [አንዱን ይምረጡ]
- ጥያቄዎ ስልጣን ባለው ቡድናችን እየተገመገመ ነው፤ ፍትሃዊ ውሳኔ ለመስጠት የሚያስፈልገውን መረጃ እያሰባሰብን ነው።
- የ{{amount}} ተመላሽ ገንዘብዎ ተፈቅዶ በክፍያ ቡድናችን እየተስተናገደ ነው።
- የ{{amount}} ተመላሽ ገንዘብዎ በእኛ በኩል በ{{payment_method}} ተልኳል። እንደ ክፍያ አቅራቢው ሁኔታ በሂሳብዎ ላይ ለመታየት ጊዜ ሊወስድ ይችላል።

እስከ {{follow_up_time}} ድረስ፣ ወይም አዲስ መረጃ ካለ ከዚያ በፊት፣ በድጋሚ እናገኝዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, update on case {{ticket_id}}: [under review / approved and processing / processed via {{payment_method}}]. Next update by {{follow_up_time}}.

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}}፦ [በግምገማ ላይ ነው / ተፈቅዶ እየተስተናገደ ነው / በ{{payment_method}} ተልኳል]። ቀጣዩ መረጃ እስከ {{follow_up_time}} ይደርስዎታል።

## Escalation Conditions
- No owner activity since the last promised follow-up → owner's team lead / **L2**.
- Status **Refund Pending** for longer than Payments' internal target → **Payments & Finance**.
- Status **Refunded** but customer did not receive it → `ref-refund-delay`.
- Status **Disputed** → **Payments & Finance**.

## Resolution Procedure
1. Status updates do not close a ticket by themselves. Keep it open until the refund is processed or the decision is communicated.
2. Record each update given (date, stage, next follow-up time).

## Policy Pending Approval
- Confirm the approved wording and typical durations for review and for each payment method's refund processing.
- Confirm internal target times for L2 review and Payments processing so agents know when to chase.

## Internal Notes
- Never reveal what the seller said during the review; say only that the review "includes input from all parties".
- Remove the stage options you did not choose before sending. Never send square brackets.
- Frequent "where is my refund?" messages are normal — be patient and consistent. Give the same information on every channel.

<!-- doc -->
# Refund Approved but Not Received
id: ref-refund-delay
type: article
category: refunds-disputes
subcategory: refund-status
audience: buyer
priority: high
department: payments
features: refunds
tags: refund not received, refund approved but no money, refund delay, where is my money, refunded but not in account, ተመላሽ አልደረሰኝም, ገንዘቡ አልገባም
related: ref-refund-status, ref-full-refund, pay-refund-processing, ref-refund-to-different-account, pay-chargeback
templates: tpl-refund-status-update, tpl-request-screenshot, tpl-escalation-notification
policy_pending: yes

## Summary
The customer was told their refund was approved (or processed), but the money has not arrived in their bank or mobile-money account.

## Issue Description
After approval, refunds pass through Byfluence's payments team and then the payment provider (e.g., Chapa or another method, if live) before reaching the customer. A delay can happen at any step. The customer is often frustrated because they were already told "approved". Treat as **High** priority: the customer has an approved decision and is waiting for their own money.

## Possible Causes
- Refund approved but not yet processed by Payments (status still **Refund Pending**)
- Refund processed, but the provider has not completed it yet
- Refund returned to the original method, but the customer is checking a different account/wallet
- Refund failed at the provider (closed account, wallet limit, wrong details) and was returned
- The customer is looking for the full amount, but a partial refund was approved
- The customer was told "approved" by mistake before a decision was recorded
- A chargeback was also filed with the bank, which can change how the money is returned

## Information to Collect
- Case number, transaction reference of the original payment, amount
- Which account/wallet the customer is checking, and whether it is the same one they paid from
- A screenshot of the relevant statement line(s) since the refund date, with other transactions hidden if they wish
- Whether the customer filed a dispute with their bank or provider

> [!WARNING] Never ask for passwords, OTP codes, PINs or full card numbers, and never ask for full bank statements. Never change the refund destination on the customer's request — see `ref-refund-to-different-account`.

## Troubleshooting Steps
1. Confirm identity and open the ticket and decision record.
2. Check payment status in the admin dashboard:
   - **Refund Pending** → refund not yet completed on Byfluence's side; escalate to **Payments & Finance** with the approval reference.
   - **Refunded** → get the refund reference/date from the record or Payments; share it with the customer so they can check with their provider.
   - **No refund record** but customer says approved → check the ticket history; if no decision exists, apologise for the confusion and escalate to **L2**.
   - **Disputed** → follow `pay-chargeback`.
3. Confirm the customer is checking the same account/wallet they paid from.
4. Compare the approved amount with the amount expected by the customer (partial vs. full).
5. If the provider shows the refund as failed, escalate to **Payments & Finance**; do not collect new account details yourself.
6. Give the customer the refund reference and a follow-up time.

- [ ] Decision record confirmed
- [ ] Payment status checked
- [ ] Same account/wallet confirmed
- [ ] Amount confirmed
- [ ] Escalated to Payments with references

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know, and I'm sorry you are still waiting for your refund for case {{ticket_id}}.

I have checked your case and have passed it to our payments team to confirm where the refund of {{amount}} is. To help them, please confirm:
1. That you are checking the same {{payment_method}} account you used to pay
2. A screenshot of your account history since the refund date (you may hide other transactions)

Please do not share your password, PIN or any verification code.

We will update you by {{follow_up_time}} with what we find.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን፤ ለጉዳይ ቁጥር {{ticket_id}} ተመላሽ ገንዘብዎን አሁንም እየጠበቁ በመሆኑ ይቅርታ እንጠይቃለን።

ጉዳይዎን አይቼ የ{{amount}} ተመላሽ ገንዘብ የት እንደደረሰ እንዲያረጋግጥ ለክፍያ ቡድናችን አስተላልፌዋለሁ። እንዲረዳቸው እባክዎ የሚከተሉትን ያረጋግጡልኝ፦
1. የሚመለከቱት ለመክፈል የተጠቀሙበትን ተመሳሳይ የ{{payment_method}} ሂሳብ መሆኑን
2. ተመላሹ ከተላከበት ቀን ጀምሮ ያለውን የሂሳብዎን ታሪክ የሚያሳይ ስክሪንሾት (ሌሎች ግብይቶችን መደበቅ ይችላሉ)

እባክዎ የይለፍ ቃልዎን፣ ፒንዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ።

ያገኘነውን እስከ {{follow_up_time}} ድረስ እናሳውቅዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry for the wait on case {{ticket_id}}. I've asked our payments team to trace your {{amount}} refund. Please confirm you're checking the same {{payment_method}} account you paid from. Update by {{follow_up_time}}.

## Short Response (AM)
ሰላም {{customer_name}}፣ ለጉዳይ ቁጥር {{ticket_id}} ስለ መዘግየቱ ይቅርታ። የ{{amount}} ተመላሽዎን እንዲያጣራ ለክፍያ ቡድናችን አሳውቄያለሁ። እባክዎ የከፈሉበትን ተመሳሳይ የ{{payment_method}} ሂሳብ እየተመለከቱ መሆኑን ያረጋግጡ። መረጃ እስከ {{follow_up_time}}።

## Follow-Up Response (EN)
Hello {{customer_name}}, update on case {{ticket_id}}: our payments team confirmed that the refund of {{amount}} was sent with reference {{transaction_id}}. If it is still not visible, you can share this reference with your payment provider, and please let us know their answer so we can follow up.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}}፦ የክፍያ ቡድናችን የ{{amount}} ተመላሽ ገንዘብ በመለያ ቁጥር {{transaction_id}} መላኩን አረጋግጧል። አሁንም ካልታየ ይህን መለያ ቁጥር ለክፍያ አቅራቢዎ ማሳየት ይችላሉ፤ የሰጡዎትን ምላሽ ቢያሳውቁን እንከታተላለን።

## Escalation Conditions
- Status **Refund Pending** after approval → **Payments & Finance**.
- Refund failed or returned by the provider → **Payments & Finance** (they decide how to re-send).
- No decision on record although the customer was told "approved" → **L2** (and note who gave the wrong information).
- Customer asks to receive it on another account → **Trust & Safety** (`ref-refund-to-different-account`).
- Repeated delays across many customers → supervisor; may be a provider incident (check Announcements).

## Resolution Procedure
1. Customer confirms receipt, **or** Payments provides a provider reference showing completion and the customer has it.
2. Record the refund reference, date, and the cause of delay.
3. Resolve the ticket; if the customer later reports non-receipt with a provider statement, reopen and escalate to Payments.

## Policy Pending Approval
- Confirm approved wording for refund arrival times per payment method.
- Decide the process when a refund fails at the provider (re-send to the same method, verified alternative, or other).
- Decide who may authorize any change of refund destination and what verification is required.

## Internal Notes
- "Refunded" in the dashboard does not always mean the customer can see it yet. Give them the reference — it is the most useful thing they can take to their provider.
- Never ask the customer to "send us your new account number" — refund destination changes are a high fraud risk.
- If an agent wrongly promised a refund, do not argue with the customer; apologise for the confusion and escalate to L2 for a decision.

<!-- doc -->
# Customer Wants the Refund Sent to a Different Account
id: ref-refund-to-different-account
type: article
category: refunds-disputes
subcategory: refund-status
audience: buyer
priority: high
department: trust_safety
features: refunds
tags: refund to another account, change refund account, send refund to my friend, different phone number refund, refund to new wallet, ገንዘቡን ወደ ሌላ ሂሳብ, ሌላ አካውንት
related: ref-refund-delay, ref-full-refund, tns-report-fraud, tns-account-compromise, acc-unauthorized-access
templates: tpl-refund-status-update, tpl-escalation-notification
policy_pending: yes

## Summary
A customer asks for their refund to be sent to a bank account, mobile-money number or person other than the one that made the original payment. This is a known fraud signal and must never be actioned by front-line support.

## Issue Description
Redirecting a refund is one of the most common ways fraudsters steal money from marketplaces: an attacker takes over an account (or poses as the customer on Telegram/phone), asks for a refund, and asks for it to go "to my other number". There are also genuine reasons (the original wallet was closed, the phone was lost, someone else paid on the buyer's behalf), but support agents cannot verify these. **Agents must never agree to, or collect details for, a different refund destination.**

## Possible Causes
- Genuine: the original mobile-money account or bank account was closed
- Genuine: the customer lost the phone/SIM used for payment
- Genuine: a family member or employer paid on the buyer's behalf
- Fraud: account takeover — the attacker controls the Byfluence account but not the original wallet
- Fraud: social engineering — someone contacts support pretending to be the buyer
- Fraud: a seller trying to route a "refund" to themselves or an associate
- Fraud: payment made with a stolen account, and the refund would "clean" the money

## Information to Collect
- Case number and original transaction reference
- The contact channel used for the request and whether it matches the registered email/phone
- The reason given for the change (in the customer's words)
- Any recent account changes: new email, new phone, password resets, new login devices (from admin tools, if visible)

> [!WARNING] Do **not** ask for or write down the new account number, wallet number or recipient name. Do not ask for passwords, OTP codes or PINs. Collecting the new destination yourself creates a record that can be misused.

## Troubleshooting Steps
1. Do not change anything and do not promise anything. Politely explain that refunds go back to the original payment method for security reasons, and that any exception needs a security review.
2. Confirm whether the request came from the registered contact details. If not, treat it as unverified.
3. Check the account for recent security changes (email/phone changed, many password resets, new devices) through authorized tools.
4. Check whether the refund was already approved, and to which method.
5. Escalate to **Trust & Safety** with: the request, the channel, the reason given, recent account changes, and the refund status. Mark the ticket **High**.
6. If there are signs of account takeover (customer says "I didn't request this" or contact details were changed recently), follow `tns-account-compromise` and ask Payments to hold the refund.
7. Wait for Trust & Safety's decision; they (with Payments) handle any verified alternative.

- [ ] Nothing changed, nothing promised
- [ ] Contact channel compared with registered details
- [ ] Recent account changes checked
- [ ] Escalated to Trust & Safety with High priority
- [ ] Payments informed to hold if takeover suspected

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your message about case {{ticket_id}}.

To protect your money, Byfluence returns refunds to the original payment method used for the purchase. We are not able to change the destination of a refund through a support chat.

I have passed your request to our security team, who will review it and contact you through your registered contact details if any further step is possible. Please do not send account numbers or personal details in this chat, and never share your password, PIN or verification codes.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጉዳይ ቁጥር {{ticket_id}} ስለላኩልን መልዕክት እናመሰግናለን።

ገንዘብዎን ለመጠበቅ ሲባል Byfluence ተመላሽ ገንዘብን የሚመልሰው ለግዢው በተጠቀሙበት የመጀመሪያው የክፍያ ዘዴ ነው። የተመላሹን መድረሻ በድጋፍ ውይይት በኩል መቀየር አንችልም።

ጥያቄዎን ለደህንነት ቡድናችን አስተላልፌዋለሁ፤ ቡድኑ ገምግሞ ሌላ አማራጭ ካለ በተመዘገበው የመገኛ መረጃዎ በኩል ያገኝዎታል። እባክዎ በዚህ ውይይት ውስጥ የሂሳብ ቁጥሮችን ወይም የግል መረጃዎችን አይላኩ፤ የይለፍ ቃልዎን፣ ፒንዎን ወይም የማረጋገጫ ኮዶችን በፍጹም አያጋሩ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, for your security refunds go back to the original payment method and can't be redirected via chat. I've sent your request to our security team, who will contact you through your registered details. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለደህንነትዎ ሲባል ተመላሽ ገንዘብ ወደ መጀመሪያው የክፍያ ዘዴ ይመለሳል፤ በውይይት መቀየር አይቻልም። ጥያቄዎን ለደህንነት ቡድናችን ልኬዋለሁ፤ በተመዘገበው መረጃዎ ያገኙዎታል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your request is still with our security team. For your protection, they will only contact you through your registered email or phone number. We will update you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ጥያቄዎ አሁንም በደህንነት ቡድናችን ዘንድ ነው። ለጥበቃዎ ሲባል የሚያገኙዎት በተመዘገበው ኢሜይል ወይም ስልክ ቁጥርዎ ብቻ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ መረጃ እንሰጥዎታለን።

## Escalation Conditions
- Every request to change a refund destination → **Trust & Safety**, priority High.
- Signs of account takeover or the registered owner denies the request → **Trust & Safety**, priority Critical; ask **Payments & Finance** to hold the refund.
- A seller asks for a buyer's refund to be sent to them → **Trust & Safety** (possible collusion/fraud).
- The original payment method genuinely no longer exists (verified by Trust & Safety) → **Payments & Finance** decides the alternative.

## Resolution Procedure
1. Trust & Safety records its decision (rejected, or verified alternative approved with Payments).
2. Communicate only what Trust & Safety approves, via the registered contact details.
3. Record the reason for the request, verification result and outcome. Flag the account if fraud was suspected.

## Policy Pending Approval
- Decide whether refunds can ever be sent to a different destination, and under what verification.
- Decide which team (Trust & Safety, Payments, Management) authorizes such exceptions.
- Decide the identity verification standard for these requests.

## Internal Notes
- Pressure tactics ("I'm travelling, just send it to my brother", "urgent, hospital") are classic social engineering. Stay polite and firm.
- The same "new" account number appearing in requests from different customers is a strong fraud ring signal — tell Trust & Safety.
- Never confirm to an unverified requester whether a refund was approved or how much it is.
