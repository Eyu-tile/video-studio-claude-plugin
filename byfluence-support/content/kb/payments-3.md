<!-- doc -->
# How Support Verifies a Payment
id: pay-payment-verification
type: article
category: payments
subcategory: verification-references
audience: internal
priority: high
department: payments
features: payments-chapa
tags: verify payment, payment verification, check transaction, confirm payment, payment proof, reconcile payment, ክፍያ ማረጋገጥ, የግብይት ማረጋገጫ
related: pay-transaction-reference-help, pay-fake-payment-screenshots, pay-paid-booking-not-confirmed, pay-pending-transaction, pay-tsg-payment-master
templates: tpl-request-transaction-ref, tpl-payment-investigation, tpl-payment-verified-booking-confirmed, tpl-payment-not-found
policy_pending: yes

## Summary
The standard internal procedure for verifying any customer payment claim. A payment is verified only when its transaction reference is matched in Byfluence or provider records with the right amount, time and account — never on a screenshot alone.

## Overview
Almost every payment ticket — paid but not confirmed, pending, duplicate, wrong amount, dispute, refund — starts with the same question: **did Byfluence actually receive this payment, for this booking/order, from this customer?** This article is the single procedure every agent follows to answer it.

> [!WARNING] **Golden rule:** never tell a customer, seller or colleague that a payment is successful, and never confirm a booking/order or release anything, based on a screenshot, a forwarded SMS or the customer's word. Only a matching record found through authorized tools counts.

### What counts as verified
A payment is **verified** only when **all** of the following match:

| Check | Matches when |
|---|---|
| Transaction reference | The exact reference is found in the Byfluence admin dashboard payments section, or in the provider portal (if you have authorized access) |
| Status | The record shows **Successful** (not Pending, Failed, Canceled, Refunded) |
| Amount | Same amount as the booking/order total (or explained difference) |
| Time | Payment time is consistent with what the customer says |
| Account | The payment is linked to the customer's account, or to the booking/order they claim |
| Not reused | The reference is not already attached to another booking/order or claimed in another ticket |

If any check fails, the payment is **not verified** — investigate or escalate.

### Verification levels (what you may say)
- **Verified** → "We have confirmed your payment" — and follow the relevant article to confirm the booking/order.
- **Found but not Successful** (Pending/Failed) → "We can see a payment attempt that has not been completed" — follow *Pending* or *Failed*.
- **Not found** → "We could not find a payment with this reference yet" — ask the customer to re-check the reference (`tpl-payment-not-found`). Never say "you did not pay".
- **Mismatch or suspicious** → do not share details; escalate (see below).

## Customer Steps
1. The customer finds the transaction reference on their receipt or SMS (see *Helping Customers Find Their Transaction Reference*).
2. The customer sends the reference, payment time, amount and what it was for.
3. The customer waits for support to confirm — they should not pay again in the meantime.

## Troubleshooting Steps
1. Confirm the customer's identity (registered email or phone number). Do not share payment details with anyone else, including a seller.
2. Collect: reference, amount, date/time, payment method, booking/order, and (optional) receipt screenshot.
3. Search the reference in the admin dashboard payments section. If not found, search by customer account, amount and time window.
4. If you have authorized provider-portal access, look the reference up there too. If you do not, escalate to Payments & Finance with the details — do not ask a colleague to "just check it" outside the ticket.
5. Run the checks in the table above and record each result in internal notes.
6. Act on the outcome:
   - **Verified** → continue with the relevant article; Payments & Finance confirms the booking/order if support cannot.
   - **Pending/Failed** → follow the matching article.
   - **Not found** → re-ask for the reference once (customers often send the wrong number, e.g. a phone number or account number). If still not found, escalate to Payments & Finance with all details.
   - **Reference linked to a different account, reused, amount/time wildly different, or screenshot inconsistent** → follow *Suspected Fake or Edited Payment Screenshots*; escalate to **Trust & Safety**.
7. Write the verification result in a standard format, e.g. `VERIFIED: ref ___, ETB amount, time, status Successful, linked to booking ___` or `NOT VERIFIED: reason`.

- [ ] Identity confirmed
- [ ] Reference searched in admin dashboard
- [ ] Provider portal checked (or escalated)
- [ ] All six checks recorded
- [ ] Outcome recorded in standard format

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your patience. To confirm your payment, we check it directly against our payment records using the transaction reference — this protects you and every customer on Byfluence.

Please send me:
1. The transaction reference from your receipt or SMS
2. The date, time and amount of the payment
3. The booking or order the payment was for

A screenshot is helpful but we still need the reference to confirm the payment. Please never share your PIN, password or verification codes — we will never ask for them.

Your case number is {{ticket_id}}. I will update you as soon as the payment is checked.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ትዕግስትዎ እናመሰግናለን። ክፍያዎን የምናረጋግጠው የግብይት መለያ ቁጥሩን በመጠቀም በቀጥታ ከክፍያ መዝገባችን ጋር በማመሳከር ነው — ይህ እርስዎንና በ Byfluence ላይ ያሉ ደንበኞችን ሁሉ ይጠብቃል።

እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ከደረሰኝዎ ወይም ከኤስኤምኤሱ ላይ ያለውን የግብይት መለያ ቁጥር
2. የክፍያውን ቀን፣ ሰዓት እና መጠን
3. ክፍያው የተፈጸመበትን ቀጠሮ ወይም ትዕዛዝ

ስክሪንሾት ጠቃሚ ቢሆንም ክፍያውን ለማረጋገጥ የግብይት ቁጥሩ ያስፈልገናል። እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድ በፍጹም አያጋሩ — አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ክፍያው እንደተጣራ ወዲያውኑ መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, we confirm payments using the transaction reference against our records. Please send the reference, payment time, amount and what it was for. A screenshot alone isn't enough. Never share your PIN or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ክፍያዎችን የምናረጋግጠው በግብይት መለያ ቁጥር ነው። እባክዎ የግብይት ቁጥሩን፣ ሰዓቱን፣ መጠኑን እና የከፈሉበትን ይላኩ። ስክሪንሾት ብቻውን በቂ አይደለም። ፒን ወይም ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- You do not have access to the payment records needed → **Payments & Finance** (or **Senior Support / Supervisor** if Payments is unavailable).
- Reference not found after one re-check → **Payments & Finance**.
- Reference linked to another account, reused, or screenshot appears edited → **Trust & Safety**, priority High.
- High-value payment or repeated claims from the same customer → **Payments & Finance** and supervisor.
- Customer pressures you to "just confirm it" because the session is starting → escalate to **Payments & Finance** as Critical; do not confirm without verification.

## Resolution Procedure
1. Record the verification result in the standard format in internal notes.
2. Attach the ticket to the booking/order and transaction where the system allows.
3. Hand over to the relevant article or department with the result, so no one repeats the check.

## Policy Pending Approval
- Define which roles have provider-portal access and which may manually confirm a booking/order after verification.
- Decide whether high-value payments need a second person to verify (four-eyes rule) and the threshold.
- Confirm how long support should wait before escalating "not found" references.

## Internal Notes
- Common wrong "references": the customer's phone number, the seller's phone number, a bank account number, a booking ID, or the SMS sender number. Ask for "the code labelled transaction / Txn / Ref on the SMS or receipt".
- Never read out a reference, amount or account detail to someone who has not passed identity checks — including a seller asking "did my buyer pay?".
- Being pressured with urgency ("my session starts now!") is both a real situation and a classic fraud tactic. Escalate fast; do not skip checks.

<!-- doc -->
# Helping Customers Find Their Transaction Reference
id: pay-transaction-reference-help
type: article
category: payments
subcategory: verification-references
audience: buyer
priority: medium
department: support_l1
features: payments-chapa, payments-telebirr, payments-mpesa, payments-bank
tags: transaction reference, transaction ID, reference number, where is my reference, receipt number, Chapa receipt, Telebirr SMS, bank SMS, የግብይት ቁጥር, ደረሰኝ, የማጣቀሻ ቁጥር
related: pay-payment-verification, pay-chapa, pay-telebirr, pay-bank-payments, pay-paid-booking-not-confirmed
templates: tpl-request-transaction-ref, tpl-payment-not-found
policy_pending: yes

## Summary
Step-by-step guidance to help a customer locate the transaction reference for a payment — on a Chapa receipt, a Telebirr or M-Pesa SMS, or a bank SMS/app — so support can verify the payment.

## Overview
The transaction reference is the unique code the payment provider gives each payment. Support needs it to verify a payment. Many customers — especially those less used to digital payments — do not know which number it is and send a phone number, account number or the amount instead.

Where the reference usually appears (exact labels vary by provider and may change):

| Paid with | Where to look | What it may be called |
|---|---|---|
| Chapa | The success page after paying, the receipt (on screen or sent by email/SMS) | Reference, Transaction ID, Tx Ref |
| Telebirr | The confirmation SMS from Telebirr; the transaction history in the Telebirr app | Transaction number, Trans ID |
| M-Pesa | The confirmation SMS from M-Pesa; the M-Pesa app statement | Transaction ID, code at the start of the SMS |
| Bank (mobile/internet banking) | The bank's debit SMS; the transaction details in the banking app; a downloadable receipt | Ref, Reference No., FT/Txn number |
| Card | The receipt or confirmation email from the payment page; the card statement description | Reference, Authorization/Order number |

> [!NOTE] Telebirr, M-Pesa, bank and card payments are not confirmed as live Byfluence methods. Check Feature Status. The table is a guide only — accept whatever code the customer's provider shows, then verify it.

> [!WARNING] The customer should **never** send their PIN, password, OTP, full card number or CVV. If they send a screenshot of an SMS inbox, ask them to crop out other messages — especially any message containing a code.

## Customer Steps
1. Think about how you paid (which app or page you used).
2. Open the confirmation SMS or receipt you received right after paying.
3. Look for a code labelled "Transaction", "Trans ID", "Ref" or "Reference". It is usually a mix of letters and numbers.
4. If you can't find the SMS, open the app you paid with (Telebirr, M-Pesa or your bank app) and look in the transaction history for the payment at that date and time.
5. Send the code to support. You can also send a cropped screenshot of the receipt — please hide any other messages and never include a PIN or verification code.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you! To find your payment, I need the transaction reference — a code made of letters and numbers that your payment provider sends after you pay.

Where to find it:
- **Chapa**: on the success page or the receipt you received after paying
- **Telebirr or M-Pesa**: in the confirmation SMS, or in the transaction history in the app
- **Bank app**: in the bank's SMS, or in the transaction details in your banking app

Look for a code labelled "Transaction", "Trans ID" or "Ref". Please send just that code (or a cropped screenshot of the receipt). Please do not send your PIN, password or any verification code — we will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

እናመሰግናለን! ክፍያዎን ለማግኘት የግብይት መለያ ቁጥሩ ያስፈልገኛል — ይህ ከከፈሉ በኋላ የክፍያ አቅራቢዎ የሚልከው የፊደላትና የቁጥሮች ኮድ ነው።

የት ማግኘት እንደሚችሉ፦
- **Chapa**፦ ከከፈሉ በኋላ በሚታየው የስኬት ገጽ ወይም በደረሰዎት ደረሰኝ ላይ
- **Telebirr ወይም M-Pesa**፦ በማረጋገጫ ኤስኤምኤሱ ውስጥ፣ ወይም በመተግበሪያው የግብይት ታሪክ ውስጥ
- **የባንክ መተግበሪያ**፦ በባንኩ ኤስኤምኤስ ውስጥ፣ ወይም በባንክ መተግበሪያዎ የግብይት ዝርዝር ውስጥ

"Transaction"፣ "Trans ID" ወይም "Ref" የሚል ምልክት ያለበትን ኮድ ይፈልጉ። እባክዎ ያንን ኮድ ብቻ (ወይም የተቆረጠ የደረሰኝ ስክሪንሾት) ይላኩ። ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አይላኩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please send the transaction code from your payment SMS/receipt (labelled "Transaction", "Trans ID" or "Ref"). Telebirr/M-Pesa: in the SMS or app history. Bank: in the bank SMS/app. Never send your PIN or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ ከክፍያ ኤስኤምኤስ/ደረሰኝ ላይ "Transaction"፣ "Trans ID" ወይም "Ref" የሚለውን ኮድ ይላኩ። Telebirr/M-Pesa፦ በኤስኤምኤሱ ወይም በመተግበሪያ ታሪክ። ባንክ፦ በባንክ ኤስኤምኤስ/መተግበሪያ። ፒን ወይም ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- The customer cannot find any reference and no payment is visible by account/amount/time → **Payments & Finance** with all other details.
- The customer sends a screenshot that includes a PIN, OTP or card number → do not repeat it; note "sensitive data received" and inform **Trust & Safety**.
- Customer has no SMS because they paid from someone else's phone/account → **Payments & Finance** (third-party payment; policy pending).

## Policy Pending Approval
- Confirm the exact reference labels for each live provider so this table can be made precise.
- Decide how support handles payments made from a third party's wallet or account.

## Internal Notes
- For customers with low digital literacy, a phone call or a voice note walking them through their SMS inbox often works better than text instructions.
- Read the code back character by character to avoid confusion between O/0 and I/1.
- If the customer only has the amount and time, you can still search by account and time window — the reference just makes it faster.

<!-- doc -->
# Suspected Fake or Edited Payment Screenshots
id: pay-fake-payment-screenshots
type: article
category: payments
subcategory: verification-references
audience: internal
priority: high
department: trust_safety
features: payments-chapa
tags: fake screenshot, edited receipt, fake payment proof, photoshopped receipt, fraud payment, fake SMS, ሀሰተኛ ደረሰኝ, የተቀየረ ስክሪንሾት, ማጭበርበር
related: pay-payment-verification, pay-transaction-reference-help, tns-report-fraud, pay-paid-booking-not-confirmed, pay-off-platform-payment
templates: tpl-request-transaction-ref, tpl-payment-not-found
policy_pending: yes

## Summary
A customer (buyer or seller) sends a payment screenshot that may be edited, reused or fake. Do not accuse anyone; do not confirm anything; verify by reference and hand suspicious cases to Trust & Safety.

## Issue Description
Fake or edited screenshots are used to get bookings/orders confirmed without paying, to claim refunds for payments never made, or to trick sellers into delivering ("I already paid, here is the proof"). Sometimes the customer is innocent: a scammer sent *them* a fake receipt, or they are confused between two payments. Support's job is to verify through records, protect the marketplace and stay neutral and polite.

## Possible Causes
- Deliberate fraud: an edited amount, date, name or reference.
- Reuse of a genuine receipt from an earlier or different payment.
- A screenshot of a payment to someone else (another merchant or a personal number).
- A fake "payment successful" SMS sent from a regular phone number rather than the provider.
- An innocent customer who received a fake receipt from a third party.
- A genuine but pending/failed payment that looks successful on a partial screenshot.

## Information to Collect
- Customer identity (registered email or phone number)
- The original screenshot/file as sent (do not edit it); note the channel and time received
- The transaction reference, amount, date/time and method the customer claims
- The booking/order the payment is for
- Who sent them the receipt, if it came from someone else (e.g. a seller or "agent")

> [!WARNING] Never ask for PINs, passwords, OTP codes or card numbers — even to "prove" a payment.

## Troubleshooting Steps
1. Do **not** confirm the booking/order or tell anyone the payment is valid.
2. Verify by reference following *How Support Verifies a Payment*.
3. Look for warning signs (record which ones you see):
   - Reference not found, or found with a different amount, time, status or account.
   - Reference already used for another booking/order or ticket.
   - Mismatched fonts, misaligned numbers, odd spacing, wrong currency format, wrong date format.
   - Payment time in the screenshot is before the booking/order was created.
   - The "SMS" comes from a regular phone number rather than the provider's sender name.
   - Recipient/merchant name is a person, not Byfluence or the provider.
   - The customer refuses to give a reference, gives several different ones, or pressures for instant confirmation.
4. Decide:
   - **Reference verified and everything matches** → it is genuine; continue the normal process.
   - **Not found / mismatch, no clear warning signs** → treat as "not verified"; ask once for the correct reference (`tpl-payment-not-found`).
   - **Warning signs present** → escalate to **Trust & Safety** with the original file, your findings and the account details. Use a neutral holding reply.
5. If a **seller** reports a buyer's fake receipt for an off-platform deal → also follow *Seller Asks Buyer to Pay Outside Byfluence* (off-platform payment is itself a policy issue).
6. Keep all evidence in the ticket; do not delete messages.

- [ ] No confirmation given
- [ ] Reference checked
- [ ] Warning signs recorded
- [ ] Original file preserved
- [ ] Trust & Safety notified (if suspicious)

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for sending this. To confirm any payment, we must match its transaction reference against our payment records — a screenshot alone cannot be used as confirmation. This is a standard check we do for every customer.

So far we have not been able to match this payment. Please send the transaction reference exactly as shown in the original SMS or receipt from your payment provider, together with the date and time of payment.

Please do not share your PIN, password or any verification code.

Your case number is {{ticket_id}}. We will update you once the check is complete.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ይህን ስለላኩልን እናመሰግናለን። ማንኛውንም ክፍያ ለማረጋገጥ የግብይት መለያ ቁጥሩን ከክፍያ መዝገባችን ጋር ማመሳከር አለብን — ስክሪንሾት ብቻውን እንደ ማረጋገጫ ሊያገለግል አይችልም። ይህ ለሁሉም ደንበኞች የምናደርገው መደበኛ ማጣሪያ ነው።

እስካሁን ይህን ክፍያ ከመዝገባችን ጋር ማመሳከር አልቻልንም። እባክዎ ከክፍያ አቅራቢዎ በደረሰዎት ዋናው ኤስኤምኤስ ወይም ደረሰኝ ላይ እንደሚታየው የግብይት መለያ ቁጥሩን፣ ከክፍያው ቀን እና ሰዓት ጋር ይላኩልን።

እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ማጣራቱ እንደተጠናቀቀ መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks. We confirm payments only by matching the transaction reference with our records, not by screenshot. Please send the reference exactly as in the original SMS/receipt, with the payment time. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እናመሰግናለን። ክፍያዎችን የምናረጋግጠው የግብይት ቁጥሩን ከመዝገባችን ጋር በማመሳከር እንጂ በስክሪንሾት አይደለም። እባክዎ በዋናው ኤስኤምኤስ/ደረሰኝ ላይ ያለውን የግብይት ቁጥር ከክፍያ ሰዓቱ ጋር ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our team is still reviewing the payment details you provided. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ቡድናችን ያቀረቡትን የክፍያ ዝርዝር አሁንም እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Any clear warning sign of editing or reuse → **Trust & Safety**, priority High.
- Same person submits suspicious proof more than once, or several accounts use the same reference → **Trust & Safety**, priority Critical.
- A seller says a buyer sent fake proof for an off-platform deal → **Trust & Safety**.
- Customer becomes abusive or threatens after being told the payment is not verified → **Senior Support / Supervisor**.

## Resolution Procedure
1. Trust & Safety records its decision (genuine / not verified / fraud) in the ticket.
2. If genuine, continue the normal payment process and apologize for the delay.
3. If not verified, inform the customer neutrally that no matching payment was found.
4. Any account action (restriction, ban) is decided and communicated by Trust & Safety, not by the agent.

## Policy Pending Approval
- Decide what account actions follow confirmed fake payment proof (warning, suspension, ban) and who decides.
- Decide whether and how confirmed fraud is reported outside Byfluence (e.g. to authorities or providers).
- Approve the wording used to tell a customer their proof was not accepted.

## Internal Notes
- **Never accuse** the customer of fraud in writing or by phone. Say "we could not match this payment" — Trust & Safety decides intent.
- Do not tell the customer which warning signs you noticed; it teaches fraudsters what to fix.
- Never forward or post the screenshot outside the ticket system.

<!-- doc -->
# Payment Dispute Raised by a Customer
id: pay-payment-dispute
type: article
category: payments
subcategory: disputes-chargebacks
audience: buyer
priority: high
department: payments
features: payments-chapa, refunds
tags: payment dispute, dispute charge, contest payment, I want my money back, unfair charge, service not received, ክርክር, የክፍያ ቅሬታ, ገንዘቤ ይመለስልኝ
related: pay-chargeback, pay-refund-processing, ref-how-to-request-refund, pay-incorrect-amount, pay-duplicate-charge, tns-unauthorized-transaction
templates: tpl-payment-investigation, tpl-refund-status-update
policy_pending: yes

## Summary
A buyer formally disputes a payment made on Byfluence — for example a service not delivered, a wrong charge, or a payment they say they did not authorize. Support collects facts and evidence, routes the case correctly and never decides the outcome alone.

## Issue Description
A payment dispute is different from a simple question. The buyer says the money should not have been taken or should be returned, and wants Byfluence to act. Typical reasons: the seller did not deliver (no-show, item not received, broken digital file); the service was very different from the listing; the amount was wrong; they were charged twice; or they did not make the payment at all. While a dispute is open the payment may show as **Disputed**, and the related seller earnings may be held.

Byfluence is a marketplace facilitator: the seller provides the service or product. Refund eligibility and decision authority are **not yet set by official policy**, so support's role is to gather evidence, involve the seller and the right department, and keep the customer informed.

## Possible Causes
- Seller no-show or service not delivered.
- Item not received, damaged or wrong (physical products — expansion feature).
- Service/product significantly different from the listing.
- Wrong amount or duplicate charge.
- Unauthorized payment (account compromise, stolen card/wallet).
- Misunderstanding of what was purchased, or buyer's remorse.

## Information to Collect
- Customer identity (registered email or phone number)
- Transaction reference, amount, date and payment method
- Booking/order ID, seller name, product/consultation name
- What went wrong, in the customer's words, with dates and times
- What outcome the customer is asking for (refund, partial refund, rebooking, replacement)
- Evidence: screenshots of messages with the seller, photos (physical items), proof of attendance attempts (e.g. a screenshot of an empty Google Meet room), listing screenshots
- Whether they have also contacted their bank or provider to reverse the payment

> [!WARNING] Never ask for PINs, passwords, OTP codes or card numbers. If the customer says they did not make the payment, switch to `tns-unauthorized-transaction` and treat the account as possibly compromised.

## Troubleshooting Steps
1. Confirm identity and verify the payment (see *How Support Verifies a Payment*).
2. Classify the dispute:
   - **Duplicate / wrong amount** → *Customer Charged Twice* or *Charged a Different Amount*.
   - **Unauthorized** → *Unauthorized Transaction* (**Trust & Safety**), priority Critical.
   - **Service/product not delivered or not as described** → continue below.
3. Check the booking/order record: status, meeting details, completion marking, any cancellation, previous tickets.
4. Collect the customer's evidence and record it in the ticket.
5. Contact the seller (through the approved channel) for their side and evidence. Do not share the buyer's personal contact details.
6. Ask Payments & Finance to place the payment/related seller earnings in a **Disputed** state or hold, if the system and policy allow.
7. Escalate with a clear summary: facts, both sides' evidence, what the customer asks for.
8. Keep the customer updated; do not predict the outcome.
9. If the customer has already filed a chargeback with their bank, follow *Chargeback or Bank Reversal Request* as well.

- [ ] Payment verified
- [ ] Dispute type classified
- [ ] Customer evidence collected
- [ ] Seller response requested
- [ ] Escalated with summary
- [ ] Customer informed of next steps

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry about your experience, and I understand you want this payment reviewed.

I have opened a dispute case for you. To review it fairly, please send:
1. The transaction reference and the booking or order this payment was for
2. A short description of what went wrong, with dates and times
3. Any evidence you have (for example, messages with the seller, screenshots or photos)
4. What you are asking for (for example, a refund or rebooking)

We will also ask the seller for their side, and our team will review the case according to Byfluence policy. I can't promise a specific outcome yet, but I will keep you updated at each step.

Please do not share your PIN, password or any verification code.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ስላጋጠመዎት ሁኔታ ይቅርታ እንጠይቃለን፤ ይህ ክፍያ እንዲገመገም እንደሚፈልጉ ተረድቻለሁ።

የክርክር ጉዳይ ከፍቼልዎታለሁ። በፍትሃዊነት ለመገምገም እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የግብይት መለያ ቁጥሩን እና ክፍያው የተፈጸመበትን ቀጠሮ ወይም ትዕዛዝ
2. የተፈጠረውን ችግር በአጭሩ ከቀንና ሰዓት ጋር
3. ያለዎትን ማስረጃ (ለምሳሌ ከሻጩ ጋር የተለዋወጧቸው መልዕክቶች፣ ስክሪንሾቶች ወይም ፎቶዎች)
4. የሚጠይቁትን (ለምሳሌ ተመላሽ ገንዘብ ወይም ቀጠሮ እንደገና ማስያዝ)

የሻጩንም ሀሳብ እንጠይቃለን፤ ቡድናችን ጉዳዩን በ Byfluence ፖሊሲ መሠረት ይገመግመዋል። ውጤቱን አሁን ቃል መግባት ባልችልም በእያንዳንዱ ደረጃ መረጃ እሰጥዎታለሁ።

እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about this. I've opened a dispute case. Please send the reference, booking/order, what went wrong (with dates), any evidence, and what you're asking for. We'll hear the seller too and keep you updated. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ። የክርክር ጉዳይ ከፍቻለሁ። እባክዎ የግብይት ቁጥሩን፣ ቀጠሮውን/ትዕዛዙን፣ የተፈጠረውን (ከቀን ጋር)፣ ማስረጃ እና የሚጠይቁትን ይላኩ። የሻጩንም ሀሳብ እንሰማለን፤ መረጃ እንሰጥዎታለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on your dispute, case {{ticket_id}}. We have received your evidence and the case is under review by our team. We will contact you again by {{follow_up_time}} with an update. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ክርክርዎ (ጉዳይ ቁጥር {{ticket_id}}) የሚሰጥ መረጃ ነው። ማስረጃዎን ተቀብለናል፤ ጉዳዩ በቡድናችን እየተገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ መረጃ እንሰጥዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- All service/product disputes after evidence is collected → **Senior Support / Supervisor** (buyer–seller dispute), with **Payments & Finance** for any money movement.
- Unauthorized payment → **Trust & Safety**, priority Critical.
- High-value disputes, legal threats, media/social-media threats → **Management**.
- Repeated disputes against the same seller → also notify **Seller Operations**.
- Customer has filed a bank chargeback → **Payments & Finance**.

## Resolution Procedure
1. Record the authorized decision, who made it and the reason.
2. Explain the decision to the customer politely, in their language.
3. If money is to be returned, follow *How Refunds Are Processed* and share status updates only.
4. Inform the seller of the outcome through the approved channel.
5. Record evidence, decision and outcome before closing.

## Policy Pending Approval
- Define refund eligibility for each product type and dispute reason.
- Define who has authority to decide disputes and approve refunds, and any value thresholds.
- Decide whether seller earnings are automatically held when a dispute opens.
- Set the deadline (if any) for buyers to raise a dispute after a transaction.

## Internal Notes
- Stay neutral: the seller may be right. Never say "you will get a refund" before an authorized decision.
- A scheduled Google Meet does not prove the session happened; ask both sides for evidence.
- Customers who also file a chargeback can end up refunded twice — always ask and record it.

<!-- doc -->
# Chargeback or Bank Reversal Request
id: pay-chargeback
type: article
category: payments
subcategory: disputes-chargebacks
audience: both
priority: high
department: payments
features: payments-card, payments-bank
tags: chargeback, bank reversal, reverse payment, bank dispute, card dispute, bank took money back, payment reversed, ክፍያ መመለስ, ባንክ መለሰ
related: pay-payment-dispute, pay-refund-processing, tns-unauthorized-transaction, out-payout-hold-restriction, pay-duplicate-charge
templates: tpl-payment-investigation
policy_pending: yes

## Summary
A buyer asks their bank, card issuer or wallet provider to reverse a Byfluence payment, or a reversal has already happened. Support documents the case, avoids double refunds, and sends it to Payments & Finance.

## Issue Description
A chargeback or reversal is when the customer's bank or provider takes back money from a payment, usually after the customer complains to them. It can happen for card payments and sometimes for bank or wallet payments, depending on the provider. Contacts typically come from:
- **A buyer** who says "I will ask my bank to reverse it" or "my bank reversed it".
- **A seller** whose earnings went down or whose payout is on hold because a buyer's payment was reversed.
- **Payments & Finance**, who received a reversal notice from a provider.

A reversal while a refund is also being processed by Byfluence can lead to the buyer being refunded twice.

## Possible Causes
- The buyer did not receive the service/product and chose to go to the bank instead of (or as well as) Byfluence.
- Unauthorized payment (stolen card or wallet, compromised account).
- Duplicate or wrong-amount charge.
- "Friendly fraud": the buyer received the service but claims otherwise.
- A failed payment that the bank automatically reversed (not a real dispute).

## Information to Collect
- Who is contacting (buyer or seller) and their identity
- Transaction reference, amount, date, payment method
- Booking/order ID and seller name
- For buyers: reason for the reversal and whether they also asked Byfluence for a refund
- For buyers: any reference number the bank gave for the dispute (not card numbers)
- For sellers: which earnings or payout are affected

> [!WARNING] Never ask for full card numbers, CVV, PINs, OTPs or online banking passwords.

## Troubleshooting Steps
1. Verify identity and the original payment.
2. Check whether a Byfluence refund or dispute already exists for this payment (status **Refund Pending**, **Refunded** or **Disputed**).
3. Buyer **thinking** about a chargeback:
   - Offer to review the problem through Byfluence first (*Payment Dispute*), but do **not** discourage or forbid the customer from contacting their bank — that is their right.
   - Explain that if they do, they should tell us, so the case is not handled twice.
4. Buyer has **already** filed or the reversal happened:
   - Record the bank's dispute reference and date.
   - Escalate to **Payments & Finance** to stop any parallel refund and handle the provider's process.
   - If unauthorized → also **Trust & Safety** (`tns-unauthorized-transaction`).
5. Seller asking about a reversal:
   - Confirm the seller's identity; explain that a payment reversal by the buyer's bank can affect earnings for that transaction.
   - Do not share the buyer's personal or bank details.
   - Escalate to **Payments & Finance**; see *Seller Disputes a Payout or Deduction* and *Payouts on Hold*.
6. Record everything in the ticket.

- [ ] Identity verified
- [ ] Existing refund/dispute checked
- [ ] Bank dispute reference recorded
- [ ] Escalated to Payments & Finance

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know. I understand you have contacted (or plan to contact) your bank or payment provider about this payment.

To make sure your case is handled correctly and not twice, please send me:
1. The transaction reference and the booking or order it was for
2. The reason for the reversal request
3. The date you contacted your bank and any case number they gave you

If you prefer, we can also review the problem directly through Byfluence. Our payments team will look at your case and I will keep you updated.

Please do not share your card number, PIN, password or any verification code with us.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን። ስለዚህ ክፍያ ባንክዎን ወይም የክፍያ አቅራቢዎን እንዳነጋገሩ (ወይም ለማነጋገር እንዳሰቡ) ተረድቻለሁ።

ጉዳይዎ በትክክል እና ሁለት ጊዜ ሳይስተናገድ እንዲታይ እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የግብይት መለያ ቁጥሩን እና ክፍያው የተፈጸመበትን ቀጠሮ ወይም ትዕዛዝ
2. ክፍያው እንዲመለስ የጠየቁበትን ምክንያት
3. ባንክዎን ያነጋገሩበትን ቀን እና የሰጡዎትን የጉዳይ ቁጥር ካለ

ከፈለጉ ችግሩን በቀጥታ በ Byfluence በኩልም መገምገም እንችላለን። የክፍያ ቡድናችን ጉዳይዎን ያያል፤ እኔም መረጃ እሰጥዎታለሁ።

እባክዎ የካርድ ቁጥርዎን፣ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for telling us. Please send the reference, the booking/order, the reason, and the date/case number from your bank, so we don't handle it twice. We can also review it directly. Never share card numbers or PINs. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን። ጉዳዩ ሁለት ጊዜ እንዳይስተናገድ የግብይት ቁጥሩን፣ ቀጠሮውን/ትዕዛዙን፣ ምክንያቱን እና የባንኩን ቀን/የጉዳይ ቁጥር ይላኩ። በቀጥታም ልንገመግመው እንችላለን። የካርድ ቁጥር ወይም ፒን አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our payments team is reviewing the reversal request for transaction {{transaction_id}} together with the payment provider. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ቡድናችን ለግብይት ቁጥር {{transaction_id}} የቀረበውን የመመለስ ጥያቄ ከክፍያ አቅራቢው ጋር እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Every confirmed chargeback or reversal → **Payments & Finance**.
- Reversal claimed as unauthorized → **Trust & Safety**, priority Critical.
- Seller affected by a reversal → **Payments & Finance**; inform **Seller Operations** if the seller disputes it.
- Pattern of chargebacks from one buyer or against one seller → **Trust & Safety**.
- High-value or legal threats → **Management**.

## Resolution Procedure
1. Payments & Finance records the provider's outcome and any adjustment to seller earnings.
2. Confirm no duplicate Byfluence refund was issued.
3. Inform the buyer (and, where affected, the seller) of the outcome.
4. Record bank dispute reference, outcome and adjustments before closing.

## Policy Pending Approval
- Define how chargebacks affect seller earnings and payouts (hold, deduction, recovery).
- Define how Byfluence responds to provider chargeback requests and who prepares the evidence.
- Decide account consequences for buyers with abusive chargebacks.

## Internal Notes
- Never threaten a customer with account closure for contacting their bank.
- Never tell a seller who the buyer is beyond what the order already shows.
- Chargebacks often arrive weeks after the transaction — check whether seller earnings were already paid out and flag that to Payments.

<!-- doc -->
# How Refunds Are Processed Back to the Payment Method
id: pay-refund-processing
type: article
category: payments
subcategory: disputes-chargebacks
audience: buyer
priority: medium
department: payments
features: refunds, payments-chapa
tags: refund processing, how refunds work, refund to Telebirr, refund to bank, where is my refund, refund method, ተመላሽ ገንዘብ, ገንዘቤ መቼ ይመለሳል, ሪፈንድ
related: ref-how-to-request-refund, ref-refund-status, ref-refund-delay, pay-duplicate-charge, pay-payment-dispute
templates: tpl-refund-status-update
policy_pending: yes

## Summary
Explains, after a refund has been approved, how the money is expected to be returned and what support can and cannot say. Refund processing is an unconfirmed feature and no refund timeline is approved.

## Overview
A refund is the return of money for an approved reason (duplicate charge, cancelled booking, approved dispute, etc.). This article covers **processing** after approval. Eligibility and how to request a refund are covered in `ref-how-to-request-refund`; status and delays in `ref-refund-status` and `ref-refund-delay`.

> [!NOTE] Check **Feature Status** (`refunds`). Refund processing is **unconfirmed** and the refund policy is not yet approved.

Expected flow (to be confirmed by Payments & Finance):
1. An authorized person approves the refund and the amount (full or partial).
2. The payment record moves to **Refund Pending**.
3. Payments & Finance processes the refund, usually back to the **original payment method** through the provider.
4. The provider processes it; the customer's bank/wallet receives it.
5. The payment record moves to **Refunded**.

What support must know:
- Support **cannot** issue refunds and must never promise timing. The provider and the customer's bank control the last steps.
- Refunding to a **different** account or phone number than the one used to pay is a classic fraud request — never agree to it; escalate.
- If the original method can no longer receive money (closed account, expired card), Payments & Finance decides the alternative.
- If the customer has also filed a chargeback, the refund must be stopped to avoid double payment.

## Customer Steps
1. Wait for confirmation from Byfluence Support that your refund is approved.
2. Check the account or wallet you originally paid from.
3. If you do not see it after you are told it was processed, contact support with your case number and transaction reference — your bank or provider may also be able to trace it with the refund reference.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your patience. Your refund for transaction {{transaction_id}} has been approved and is being processed by our payments team.

Refunds are normally returned to the same payment method you used ({{payment_method}}). After we send it, your payment provider or bank completes the final step, so the time it takes to appear can vary. We will update you on the status.

For your security, we can only refund to the original payment method, and we will never ask for your PIN, password or verification codes.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ትዕግስትዎ እናመሰግናለን። ለግብይት ቁጥር {{transaction_id}} የጠየቁት ተመላሽ ገንዘብ ጸድቋል፤ የክፍያ ቡድናችን እያስኬደው ነው።

ተመላሽ ገንዘብ በአብዛኛው የሚመለሰው በከፈሉበት ተመሳሳይ የክፍያ መንገድ ({{payment_method}}) ነው። እኛ ከላክን በኋላ የመጨረሻውን ደረጃ የክፍያ አቅራቢዎ ወይም ባንክዎ ስለሚያጠናቅቀው ገንዘቡ ለመድረስ የሚወስደው ጊዜ ሊለያይ ይችላል። ስለ ሁኔታው መረጃ እንሰጥዎታለን።

ለደህንነትዎ ሲባል ተመላሽ ገንዘብ የምንልከው ወደ መጀመሪያው የክፍያ መንገድ ብቻ ነው፤ ፒንዎን፣ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድ በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your refund for {{transaction_id}} is approved and being processed to your original method ({{payment_method}}). Your provider/bank completes the last step, so timing can vary — we'll update you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለ {{transaction_id}} ተመላሽ ገንዘብዎ ጸድቆ ወደ መጀመሪያው የክፍያ መንገድዎ ({{payment_method}}) እየተላከ ነው። የመጨረሻውን ደረጃ አቅራቢዎ/ባንክዎ ስለሚያጠናቅቅ ጊዜው ሊለያይ ይችላል — መረጃ እንሰጥዎታለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Customer asks to receive the refund to a different account/number → **Payments & Finance** and **Trust & Safety**; do not agree.
- Original payment method can no longer receive funds → **Payments & Finance**.
- Refund marked **Refunded** but the customer says nothing arrived → **Payments & Finance** to obtain the refund reference from the provider (`ref-refund-delay`).
- Chargeback also filed → **Payments & Finance** to stop duplicate refund.

## Policy Pending Approval
- Confirm that refunds always go to the original payment method and the exceptions process.
- Approve wording on how long refunds take for each provider (none may be quoted until approved).
- Decide whether provider fees are deducted from refunds.
- Define who can approve refunds and at which amounts.

## Internal Notes
- Use this article only after a refund is approved. If not yet approved, use `ref-how-to-request-refund` and say the request is under review.
- "Refund to my friend's Telebirr" or "to my new number" requests are high-risk; always escalate.
- Update the ticket each time the status changes (Refund Pending → Refunded) so other agents give the same answer.
