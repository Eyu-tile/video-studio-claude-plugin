<!-- doc -->
# Payment Failed
id: pay-failed-transaction
type: article
category: payments
subcategory: failed-pending
audience: buyer
priority: medium
department: support_l1
features: payments-chapa
tags: payment failed, transaction failed, payment declined, payment error, can't pay, payment not going through, ክፍያ አልተሳካም, ክፍያ ውድቅ ሆነ, መክፈል አልቻልኩም
related: pay-pending-transaction, pay-paid-booking-not-confirmed, pay-duplicate-charge, pay-card-payments, pay-tsg-payment-master
templates: tpl-payment-failed-guidance, tpl-request-transaction-ref, tpl-payment-not-found
policy_pending: yes

## Summary
The buyer tried to pay but saw an error or "failed" message, or the payment page would not complete. The main questions are: was money actually taken, and can the buyer safely try again?

## Issue Description
The buyer reached the payment step but the payment did not complete. They may have seen a "payment failed" or "declined" message, an error page, a page that never loaded, or they were returned to Byfluence with no confirmation. Some customers also see money deducted or "on hold" in their bank or wallet even though the payment failed, which causes worry. The customer usually wants to know whether they should pay again — paying again too quickly is the most common cause of duplicate charges.

## Possible Causes
- Insufficient balance in the wallet or bank account, or a daily transaction limit reached.
- The customer cancelled on the provider page, or the approval prompt on their phone timed out.
- Wrong details entered on the provider page (expired card, wrong account).
- The bank or wallet blocked the transaction for security reasons.
- The payment method is not enabled for this customer (e.g., foreign card, card not enabled for online payments).
- Network problems on the customer's phone during payment.
- A temporary outage at the payment provider or on Byfluence.
- The booking slot or item became unavailable during checkout and the payment was not completed.

## Information to Collect
- Customer full name and registered email or phone number
- What they were paying for (consultation/listing name, seller name, booking date/time if relevant)
- Payment method chosen and the date/time of the attempt
- The exact error message or a screenshot of the error screen
- Whether any money was deducted or placed on hold (and the amount)
- Transaction reference, if they received any SMS or receipt
- Device and browser/app used (phone or computer)

> [!WARNING] Never ask for PINs, passwords, OTP codes, full card numbers or CVV. An error screenshot and (if any) the transaction reference are enough.

## Troubleshooting Steps
1. Confirm the customer's identity using their registered email or phone number.
2. Ask whether money was deducted. This decides the path:
   - **No money deducted** → go to step 3.
   - **Money deducted or on hold** → go to step 5.
3. Check the payment attempts on the customer's account in the admin dashboard (or provider portal, if you have authorized access). Confirm the attempt shows as **Failed** or **Canceled** and that no **Successful** payment exists for the same booking/order.
4. Guide a safe retry:
   - Check Feature Status — is the method live? If not, offer a live method.
   - Ask the customer to check their balance/limits and stable internet, then try once more.
   - If the error repeats, suggest a different live method rather than many retries.
5. If money was deducted:
   - Search by reference, amount and time. If the payment shows **Successful** but the booking/order is not confirmed → follow *Paid but Not Confirmed* (consultations: `pay-paid-booking-not-confirmed`; products: `pay-paid-order-not-confirmed`).
   - If it shows **Pending** → follow *Payment Stuck as Pending*.
   - If it shows **Failed** / not found → explain that no successful payment was recorded by Byfluence; a deduction on a failed payment is usually a temporary hold or is reversed by the provider. Ask the customer to confirm with their bank/wallet provider. Do **not** promise when it will be returned.
6. Tell the customer **not** to retry again until you confirm no successful payment exists, if there is any doubt.
7. Check whether other customers are reporting failures with the same method right now (recent tickets, Announcements). If yes, alert the supervisor.
8. Record findings, the error message and the payment status in the ticket.

- [ ] Identity confirmed
- [ ] Payment attempt located and status checked
- [ ] Deduction question answered
- [ ] Safe retry guidance given (or escalated)
- [ ] Possible incident checked

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry your payment did not go through.

To check what happened, please send me:
1. The payment method you used and the time you tried to pay
2. A screenshot or the text of the error message you saw
3. Whether any money was deducted from your account — and if so, the transaction reference from the SMS or receipt

Please do not try to pay again until we have checked, so you are not charged twice. And please never share your PIN, password or verification codes — Byfluence will never ask for them.

Your case number is {{ticket_id}}. I will update you as soon as I have checked.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ ክፍያዎ ባለመሳካቱ ይቅርታ እንጠይቃለን።

ምን እንደተፈጠረ ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የተጠቀሙበትን የክፍያ መንገድ እና ለመክፈል የሞከሩበትን ሰዓት
2. ያዩትን የስህተት መልዕክት ስክሪንሾት ወይም ጽሑፍ
3. ከሂሳብዎ ገንዘብ ተቀንሶ እንደሆነ — ከተቀነሰ ከኤስኤምኤሱ ወይም ከደረሰኙ ላይ ያለውን የግብይት መለያ ቁጥር

ሁለት ጊዜ እንዳይከፍሉ እባክዎ እስክናጣራ ድረስ በድጋሚ ለመክፈል አይሞክሩ። እንዲሁም ፒንዎን፣ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድ በፍጹም አያጋሩ — Byfluence አይጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። እንዳጣራሁ ወዲያውኑ መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry your payment failed. Please send the method, the time, the error message, and whether money was deducted (with the reference if so). Please don't retry until we check. Never share your PIN or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ክፍያዎ ስላልተሳካ ይቅርታ። እባክዎ የክፍያ መንገዱን፣ ሰዓቱን፣ የስህተት መልዕክቱን እና ገንዘብ ተቀንሶ እንደሆነ (ከሆነ የግብይት ቁጥሩን) ይላኩ። እስክናጣራ ድረስ በድጋሚ አይክፈሉ። ፒን ወይም ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We checked your payment attempt and Byfluence did not record a successful payment, so no booking or order was charged on our side. If an amount still appears as deducted on your account, please check with your bank or payment provider, as failed payments are usually held temporarily or reversed by them. You are welcome to try again using {{payment_method}}, and we are here if you need help.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ሙከራዎን አጣርተናል፤ Byfluence የተሳካ ክፍያ አልመዘገበም፣ ስለዚህ በእኛ በኩል ለቀጠሮ ወይም ለትዕዛዝ የተቆረጠ ገንዘብ የለም። አሁንም ከሂሳብዎ የተቀነሰ መጠን ካለ እባክዎ ባንክዎን ወይም የክፍያ አቅራቢዎን ያነጋግሩ፤ ያልተሳኩ ክፍያዎች ብዙውን ጊዜ ለጊዜው ይያዛሉ ወይም በእነሱ በኩል ይመለሳሉ። በ {{payment_method}} በድጋሚ መሞከር ይችላሉ፤ እርዳታ ከፈለጉ እዚህ ነን።

## Escalation Conditions
- Money deducted and the payment shows **Successful** or **Pending** in Byfluence → **Payments & Finance** (follow the relevant article).
- The same method fails for several customers in a short time → **Technical / Engineering**, priority High, and notify the supervisor (possible incident).
- Error appears on the Byfluence checkout page itself (not the provider page) → **Technical / Engineering** with screenshot, device and browser.
- You cannot see payment attempts with your access level → **Senior Support / Supervisor**.
- Customer reports attempts they did not make → **Trust & Safety** (`tns-unauthorized-transaction`).

## Resolution Procedure
1. Confirm one of: the customer paid successfully on a retry and the booking/order is confirmed; or no successful payment exists and the customer understands any hold is handled by their provider; or the case was handed to the right department.
2. Confirm there is no duplicate successful payment for the same booking/order.
3. Send the resolution message and invite the customer to reply if the deduction is not reversed by their provider.
4. Record payment status, error message, root cause (e.g. "insufficient balance", "provider outage") and actions in the ticket.

## Policy Pending Approval
- Approve the wording support may use about how failed-payment holds are released (support must not give timelines without approval).
- Confirm whether support may see all failed attempts in the admin dashboard or only successful payments.
- Decide whether a booking slot is held for the customer during a failed/pending payment, and for how long.

## Internal Notes
- "Failed but money deducted" is usually a provider hold. Do not say "you will get it back in X days" — say the provider handles it, and invite them back if it is not reversed.
- Repeated retries are the main cause of duplicate charges; slow the customer down.
- Low-digital-literacy customers may not know which method they used — ask them what app or screen they saw and whether they got an SMS.

<!-- doc -->
# Payment Stuck as Pending
id: pay-pending-transaction
type: article
category: payments
subcategory: failed-pending
audience: buyer
priority: high
department: payments
features: payments-chapa
tags: payment pending, pending payment, payment processing, waiting for confirmation, payment not confirmed yet, stuck pending, ክፍያ በመጠባበቅ ላይ, ክፍያ አልተረጋገጠም
related: pay-failed-transaction, pay-paid-booking-not-confirmed, pay-paid-order-not-confirmed, pay-payment-verification, pay-tsg-payment-master
templates: tpl-payment-pending-explain, tpl-request-transaction-ref, tpl-payment-investigation
policy_pending: yes

## Summary
The customer's payment shows as Pending on Byfluence (or they were told "processing") and their booking or order is not yet confirmed. Support must find out whether the provider actually completed the payment.

## Issue Description
A payment is **Pending** when Byfluence has started a payment but has not yet received a final result (Successful or Failed) from the provider. The customer may see "processing", "awaiting confirmation" or a pending booking/order in their dashboard. They may or may not see a deduction in their account. Customers worry about losing their slot or item, and some try to pay again — which can cause duplicate charges. Treat as **High** when the consultation is soon or when money has been deducted.

## Possible Causes
- The provider has not yet completed processing (common with bank-based payments).
- The customer did not finish the approval step on their phone (prompt ignored or timed out).
- The provider's confirmation (callback) to Byfluence was delayed or failed.
- The customer closed the browser before being returned to Byfluence.
- A temporary outage at the provider or on Byfluence.
- The payment was actually completed under a different booking/order or account.

## Information to Collect
- Customer full name and registered email or phone number
- What they paid for (booking/order, seller name, date/time of session if relevant)
- Payment method and the date/time of payment
- Transaction reference from the SMS or receipt (if they have one)
- Whether money was deducted, and the amount
- Booking ID or order ID if visible in their dashboard

> [!WARNING] Never ask for PINs, passwords, OTP codes or card numbers.

## Troubleshooting Steps
1. Confirm identity using the registered email or phone number.
2. Find the pending payment in the admin dashboard (search by customer, amount, time, or reference).
3. Check how long the payment has been pending compared with the payment time. Very recent payments may simply still be processing.
4. Check the provider result (admin dashboard detail or provider portal if you have authorized access):
   - **Provider shows Successful** → the confirmation did not reach Byfluence. Escalate to **Payments & Finance** to update the payment and confirm the booking/order. Tell the customer their payment is found and being confirmed.
   - **Provider shows Failed/Canceled** → explain no successful payment was completed; follow *Payment Failed* for safe retry guidance.
   - **Provider still processing / no result** → explain it is still being processed and that you will follow up. Set a follow-up.
   - **Payment not found at the provider** → ask for the reference again (see *Helping Customers Find Their Transaction Reference*), then use `tpl-payment-not-found` if still not found.
5. If a consultation starts soon and the payment is still pending, mark the ticket **High/Critical**, escalate to Payments & Finance, and ask them to protect the slot if possible.
6. Tell the customer **not** to pay again while the payment is pending.
7. If several pending payments appear for the same provider at the same time, alert the supervisor (possible callback incident).
8. Record findings and set a follow-up time in the ticket.

- [ ] Identity confirmed
- [ ] Pending payment located
- [ ] Provider result checked (or escalated)
- [ ] Customer told not to pay again
- [ ] Follow-up time set

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand your payment is showing as pending and your booking or order is not confirmed yet — I know this is worrying.

A payment stays pending until the payment provider sends us the final result. I am checking it now. To help me, please send:
1. The transaction reference from your SMS or receipt
2. The date and time you paid
3. Whether the amount was deducted from your account

Please do not pay again while this is pending, so you are not charged twice. And please never share your PIN, password or any verification code with anyone.

Your case number is {{ticket_id}}. I will update you as soon as I have the result.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ክፍያዎ በመጠባበቅ ላይ (pending) እንደሚታይ እና ቀጠሮዎ ወይም ትዕዛዝዎ ገና እንዳልተረጋገጠ ተረድቻለሁ — ይህ እንደሚያሳስብ አውቃለሁ።

ክፍያ የክፍያ አቅራቢው የመጨረሻውን ውጤት እስኪልክልን ድረስ በመጠባበቅ ላይ ይቆያል። አሁን እያጣራሁት ነው። እንዲረዳኝ እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ከኤስኤምኤሱ ወይም ከደረሰኙ ላይ ያለውን የግብይት መለያ ቁጥር
2. የከፈሉበትን ቀን እና ሰዓት
3. ገንዘቡ ከሂሳብዎ ተቀንሶ እንደሆነ

ሁለት ጊዜ እንዳይከፍሉ እባክዎ ክፍያው በመጠባበቅ ላይ እያለ በድጋሚ አይክፈሉ። እንዲሁም ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ ለማንም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ውጤቱን እንዳገኘሁ ወዲያውኑ አሳውቅዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your payment is pending until the provider sends us the result — I'm checking it. Please send the reference, payment time and whether money was deducted. Please don't pay again meanwhile. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ክፍያዎ አቅራቢው ውጤቱን እስኪልክልን ድረስ በመጠባበቅ ላይ ነው — እያጣራሁ ነው። እባክዎ የግብይት ቁጥሩን፣ የክፍያ ሰዓቱን እና ገንዘብ ተቀንሶ እንደሆነ ይላኩ። እስከዚያው በድጋሚ አይክፈሉ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our payments team is still confirming transaction {{transaction_id}} with the payment provider. Your case is being actively handled and we will contact you again by {{follow_up_time}}. Please do not pay again in the meantime. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ቡድናችን የግብይት ቁጥር {{transaction_id}}ን ከክፍያ አቅራቢው ጋር እያረጋገጠ ነው። ጉዳይዎ በንቃት እየተከታተለ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። እባክዎ እስከዚያው በድጋሚ አይክፈሉ። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Provider shows Successful but Byfluence still shows Pending → **Payments & Finance** to reconcile and confirm.
- Pending with money deducted and no provider result available to you → **Payments & Finance**.
- Consultation starts soon (same day) and payment is still pending → **Payments & Finance**, priority Critical, notify the supervisor.
- Many payments pending for the same provider at once → **Technical / Engineering** and supervisor (incident).
- No access to provider results → **Senior Support / Supervisor**.

## Resolution Procedure
1. Confirm the payment's final status (Successful or Failed) in the admin dashboard.
2. If Successful: confirm the booking/order now shows as confirmed and the customer has what they need (e.g., meeting details).
3. If Failed: confirm no money was taken by Byfluence and guide a safe retry.
4. Send the resolution message, then record the root cause (e.g., "callback delay", "customer did not approve prompt") and final status in the ticket.

## Policy Pending Approval
- Define how long a payment may remain pending before support escalates (internal threshold), per provider.
- Confirm the approved wording for how long payment confirmation usually takes.
- Decide whether pending payments automatically expire and what the customer is told when they do.
- Confirm whether a booking slot is held while payment is pending.

## Internal Notes
- Most "pending" cases are either an unapproved phone prompt or a delayed callback. Ask the customer whether they approved the payment on their phone.
- Never mark a pending payment as successful because of a screenshot. Only the provider record counts.
- Pending + session soon is the most time-sensitive payment case; move it to the top of your queue.

<!-- doc -->
# Paid but Product Order Not Confirmed
id: pay-paid-order-not-confirmed
type: article
category: payments
subcategory: payment-mismatch
audience: buyer
priority: high
department: payments
features: physical-products, digital-products, payments-chapa
tags: paid but no order, order not confirmed, money deducted order missing, paid product not showing, no download after payment, ክፍያ ተቆርጧል ትዕዛዝ የለም, ትዕዛዝ አልተረጋገጠም
related: pay-paid-booking-not-confirmed, pay-pending-transaction, pay-duplicate-charge, pay-payment-verification, pay-tsg-payment-master
templates: tpl-request-transaction-ref, tpl-payment-investigation, tpl-payment-not-found
policy_pending: yes

## Summary
The customer paid for a physical or digital product, money left their account, but no confirmed order appears, or they did not receive access to the digital product.

## Issue Description
This is the product version of *Paid but Booking Not Confirmed*. The buyer paid for a physical item (for delivery) or a digital product (download/access), but their dashboard shows no order, the order is stuck as pending payment, or — for digital products — no access or download link was provided. The customer worries they lost money and, for physical products, that the item may sell out.

> [!NOTE] Physical and digital products are **expansion features**. Check the **Feature Status** page (`physical-products`, `digital-products`) first. If the feature is not live, the customer may have paid on a fake site or to an off-platform seller — check carefully and consider Trust & Safety.

## Possible Causes
- Delayed provider confirmation; the order is still pending.
- The provider's confirmation (callback) to Byfluence failed.
- The customer closed the browser before returning to Byfluence.
- The payment failed or was reversed but the customer saw a temporary hold.
- Duplicate payment: one attached to the order, the other not.
- The order was placed from a different account.
- The item went out of stock while the customer was paying.
- For digital products: the order is confirmed but the access/delivery step failed (a technical issue, not a payment issue).
- The customer paid a seller outside Byfluence or on a look-alike website.

## Information to Collect
- Customer full name and registered email or phone number
- Product name, seller name and (if visible) order ID
- Payment method, date and time of payment, amount
- Transaction reference from the receipt or SMS
- For physical products: delivery details given at checkout (to check the order record matches)
- For digital products: what they see when they try to access the product
- Where they paid (the Byfluence checkout page, or a link/number sent by someone)

> [!WARNING] Never ask for PINs, passwords, OTP codes or full card numbers.

## Troubleshooting Steps
1. Confirm feature status and the customer's identity.
2. Search the customer's orders around the payment time (include pending, cancelled and failed orders).
3. Search the transaction by reference in the admin dashboard (or provider portal, if authorized).
4. Decide the case:
   - **Payment successful + order pending** → escalate to **Payments & Finance** to confirm the order; tell the customer their payment is recorded.
   - **Payment successful + no order** → escalate to **Payments & Finance** with the reference; check stock with the seller-side team.
   - **Payment successful + order confirmed but no digital access** → this is an access problem: escalate to **Technical / Engineering** (see digital product access articles).
   - **Payment pending** → follow *Payment Stuck as Pending*.
   - **Payment not found / failed** → explain that no successful payment was recorded; check where they paid. If they paid outside the checkout, go to *Seller Asks Buyer to Pay Outside Byfluence*.
   - **Two payments for one order** → follow *Customer Charged Twice*.
5. If the item may be out of stock, ask the seller-side team to hold the item if possible while Payments confirms the order. Do not promise the item.
6. Record reference, order ID and findings in the ticket.

- [ ] Feature status checked
- [ ] Identity confirmed
- [ ] Transaction located (or confirmed missing)
- [ ] Order and access status checked
- [ ] Ticket updated with references

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry for the worry. I understand you paid for {{product_name}} but your order has not been confirmed.

To check this quickly, please send:
1. The transaction reference from your payment receipt or SMS
2. The date, time and amount of the payment
3. The product and seller name (and the order number if you see one)

Please do not share your PIN, password or any verification code — we will never ask for them.

Your case number is {{ticket_id}}. I will update you as soon as we have checked the payment.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ ለተፈጠረው ስጋት ይቅርታ እንጠይቃለን። ለ {{product_name}} ክፍያ እንደፈጸሙ ነገር ግን ትዕዛዝዎ እንዳልተረጋገጠ ተረድቻለሁ።

በፍጥነት ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ከክፍያ ደረሰኝዎ ወይም ከኤስኤምኤሱ ላይ ያለውን የግብይት መለያ ቁጥር
2. የክፍያውን ቀን፣ ሰዓት እና መጠን
3. የምርቱን እና የሻጩን ስም (የትዕዛዝ ቁጥር ካለ እሱንም)

እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ክፍያውን እንዳጣራን ወዲያውኑ መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about this! Please send the transaction reference, payment time and amount, and the product/seller name. I'll check right away. (Never share your PIN or codes.) Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለተፈጠረው ችግር ይቅርታ! እባክዎ የግብይት ቁጥሩን፣ የክፍያ ሰዓቱን እና መጠኑን እንዲሁም የምርቱን/የሻጩን ስም ይላኩ። ወዲያውኑ አጣራለሁ። (ፒን ወይም ኮድ አያጋሩ።) የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our payments team is still verifying transaction {{transaction_id}} for your order of {{product_name}}. Your case is being actively handled and we will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ቡድናችን ለ {{product_name}} ትዕዛዝዎ የግብይት ቁጥር {{transaction_id}}ን እያጣራ ነው። ጉዳይዎ በንቃት እየተከታተለ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Payment confirmed by the provider but the order is not confirmed → **Payments & Finance**.
- Item is out of stock after a successful payment → **Payments & Finance** and **Seller Operations** (rebook/refund decision is pending policy).
- Order confirmed but digital access not delivered → **Technical / Engineering**.
- Customer paid through a link, number or account outside checkout, or the feature is not live → **Trust & Safety**, priority High.
- No access to payment records → **Senior Support / Supervisor**.

## Resolution Procedure
1. Confirm the order now shows as confirmed (or that Payments has approved a refund/reversal).
2. For physical products, confirm delivery details on the order are correct; for digital products, confirm the customer can access the file.
3. Send the resolution message and ask the customer to confirm.
4. Record root cause, actions and outcome before resolving.

## Policy Pending Approval
- Decide what happens when payment succeeds but the item is out of stock (substitute, wait, refund) and who approves.
- Confirm who may manually confirm an order after payment verification.
- Confirm the approved wording for verification timing.

## Internal Notes
- Because product sales are an expansion area, a "paid but no order" report while the feature is not live is a strong signal of a fake site or off-platform payment. Ask for the website address or link they used.
- Verify by transaction reference only; screenshots are supporting evidence.

<!-- doc -->
# Customer Charged Twice
id: pay-duplicate-charge
type: article
category: payments
subcategory: payment-mismatch
audience: buyer
priority: high
department: payments
features: payments-chapa
tags: charged twice, double payment, duplicate charge, paid two times, money taken twice, two deductions, ሁለት ጊዜ ተቆርጧል, ድርብ ክፍያ, ሁለቴ ከፍያለሁ
related: pay-paid-booking-not-confirmed, pay-failed-transaction, pay-refund-processing, ref-refund-status, pay-incorrect-amount
templates: tpl-duplicate-charge-ack, tpl-request-transaction-ref, tpl-refund-status-update
policy_pending: yes

## Summary
The customer says they were charged more than once for the same booking or order. Support must confirm whether there are really two successful payments before anything is promised.

## Issue Description
The customer sees two (or more) deductions for one purchase in their bank or wallet. Common situations: they retried after a failed or slow payment; they double-tapped the pay button; or they paid again because the booking stayed pending. Sometimes only one deduction is a real payment and the other is a temporary hold. Sometimes the customer actually made two separate bookings or orders. The customer usually wants the extra money back quickly and may be angry.

## Possible Causes
- Customer retried after a failed/pending payment and both eventually succeeded.
- Double-click/double-tap on the pay button or browser refresh during payment.
- One real payment plus one temporary hold from a failed attempt.
- Two separate bookings/orders were created (e.g., one by mistake, or for two sessions).
- A system or provider error created two charges for one checkout.
- Customer is looking at one payment plus a provider or bank fee line.

## Information to Collect
- Customer full name and registered email or phone number
- What they paid for and the booking/order ID if visible
- Transaction references for **both** deductions (from SMS/receipts)
- Date, time and amount of each deduction
- Payment method used
- Screenshot of the bank/wallet statement showing both deductions (supporting evidence)

> [!WARNING] Never ask for PINs, passwords, OTP codes or full card numbers.

## Troubleshooting Steps
1. Confirm identity.
2. Search both transaction references in the admin dashboard (or provider portal if authorized).
3. For each reference record: status (Successful / Pending / Failed), amount, time and the booking/order it is attached to.
4. Decide the case:
   - **Two Successful payments, one booking/order** → genuine duplicate. Escalate to **Payments & Finance** for refund of the extra payment. Use `tpl-duplicate-charge-ack`.
   - **One Successful, one Failed/not found** → the second is likely a temporary hold. Explain that Byfluence recorded only one payment and the other should be handled by their provider. Do not promise timelines.
   - **Two Successful payments, two bookings/orders** → ask the customer whether they wanted both. If not, follow the cancellation/refund process for the unwanted one (policy pending).
   - **One payment found, second reference not found** → ask the customer to re-check the reference; follow *Helping Customers Find Their Transaction Reference*.
5. Check that the booking/order itself is confirmed and correct.
6. Record both references, statuses and your conclusion in the ticket.

- [ ] Identity confirmed
- [ ] Both references checked
- [ ] Genuine duplicate confirmed or ruled out
- [ ] Booking/order status checked
- [ ] Escalated to Payments & Finance (if genuine)

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry about this — I understand how stressful it is to see money taken twice.

To check both payments, please send me:
1. The transaction reference for each deduction (from the SMS or receipt)
2. The date, time and amount of each deduction
3. The booking or order you were paying for

Please do not share your PIN, password or any verification code — we will never ask for them.

Your case number is {{ticket_id}}. Once we confirm the details, our payments team will review it and I will keep you updated.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ ለዚህ ችግር ይቅርታ እንጠይቃለን — ገንዘብ ሁለት ጊዜ ሲቆረጥ ምን ያህል እንደሚያሳስብ እረዳለሁ።

ሁለቱንም ክፍያዎች ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ለእያንዳንዱ ቅነሳ የግብይት መለያ ቁጥር (ከኤስኤምኤሱ ወይም ከደረሰኙ)
2. የእያንዳንዱን ቅነሳ ቀን፣ ሰዓት እና መጠን
3. የከፈሉበትን ቀጠሮ ወይም ትዕዛዝ

እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ዝርዝሩን ካረጋገጥን በኋላ የክፍያ ቡድናችን ይገመግመዋል፤ በየጊዜው መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about the double charge! Please send the reference, time and amount of each deduction, and what you were paying for. Our payments team will review it. (Never share your PIN or codes.) Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ ድርብ ቅነሳው ይቅርታ! እባክዎ የእያንዳንዱን ቅነሳ የግብይት ቁጥር፣ ሰዓት እና መጠን እንዲሁም የከፈሉበትን ይላኩ። የክፍያ ቡድናችን ይገመግመዋል። (ፒን ወይም ኮድ አያጋሩ።) የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have confirmed the details of both payments and our payments team is reviewing the extra charge. We will update you on the outcome and any refund status by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የሁለቱንም ክፍያዎች ዝርዝር አረጋግጠናል፤ የክፍያ ቡድናችን ተጨማሪውን ክፍያ እየገመገመ ነው። ስለ ውጤቱ እና ስለማንኛውም ተመላሽ ገንዘብ ሁኔታ እስከ {{follow_up_time}} ድረስ እናሳውቅዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Two successful payments for one booking/order → **Payments & Finance** (refund of the duplicate), priority High.
- Several customers report duplicates at the same time → **Technical / Engineering** and supervisor (possible system bug).
- Customer threatens a chargeback or has already filed one → follow *Chargeback or Bank Reversal Request*.
- References belong to another customer or look edited → **Trust & Safety**.
- No access to payment records → **Senior Support / Supervisor**.

## Resolution Procedure
1. Confirm with Payments & Finance whether the duplicate refund was approved and processed (status **Refund Pending** / **Refunded**).
2. Confirm the original booking/order is still valid and confirmed.
3. Send the customer the status update (`tpl-refund-status-update`) without promising when the money will arrive.
4. Record both references, the decision and refund status; resolve only after Payments confirms processing.

## Policy Pending Approval
- Confirm that genuine duplicate charges are always refunded in full and who approves them.
- Confirm whether provider/bank fees on a duplicate are refunded.
- Approve wording on how long duplicate refunds take to reach the customer.

## Internal Notes
- Never promise "you will get it back" until two **Successful** payments are confirmed in the system.
- Customers usually retry because the payment screen did not show a clear result. Be apologetic and never blame the customer for paying twice.
- Check whether the customer also opened a ticket on another channel to avoid two refunds for one duplicate.

<!-- doc -->
# Charged a Different Amount Than Expected
id: pay-incorrect-amount
type: article
category: payments
subcategory: payment-mismatch
audience: buyer
priority: high
department: payments
features: payments-chapa
tags: wrong amount, charged more, overcharged, charged less, price different, amount mismatch, extra money taken, የተሳሳተ መጠን, ከዋጋው በላይ ተቆረጠ, ትርፍ ገንዘብ
related: pay-currency-and-fees-questions, pay-duplicate-charge, pay-refund-processing, pay-payment-dispute, pay-tsg-payment-master
templates: tpl-payment-investigation, tpl-request-transaction-ref, tpl-refund-status-update
policy_pending: yes

## Summary
The customer was charged more (or less) than the price they expected. Support must compare the listing price, the checkout total, the Byfluence record and the customer's statement to find where the difference came from.

## Issue Description
The customer says the deduction does not match the listed price or the checkout total. They may have been overcharged (more common complaint) or undercharged (sometimes the booking then fails). The difference may come from Byfluence (a fee or a pricing error), the seller (price change, wrong option), the provider or bank (their own charges or currency conversion), or a combination of a payment and a hold.

## Possible Causes
- Provider or bank charged its own transfer fee.
- Currency conversion on a foreign card.
- A Byfluence fee or tax line at checkout (not confirmed — check the checkout/order record).
- The seller changed the price between viewing and paying, or listed the wrong price.
- The customer chose a different option (longer duration, more quantity, different product variant).
- A duplicate charge or hold made the total look higher.
- A system pricing error.

## Information to Collect
- Customer full name and registered email or phone number
- Booking/order ID, product or consultation name and seller name
- The price the customer expected and where they saw it (listing, checkout, message from seller)
- The amount deducted and transaction reference
- Screenshot of the checkout page or listing showing the price (supporting evidence)
- Payment method used and whether the card/account is from outside Ethiopia

> [!WARNING] Never ask for PINs, passwords, OTP codes or full card numbers.

## Troubleshooting Steps
1. Confirm identity and locate the payment by reference.
2. Compare four numbers and note them in the ticket:
   - Listing price (current and, if visible, at time of purchase)
   - Checkout total recorded on the booking/order
   - Amount received by Byfluence in the payment record
   - Amount deducted on the customer's statement
3. Decide where the difference comes from:
   - **Byfluence record = checkout total, statement higher** → provider/bank charges or currency conversion. Explain neutrally; Byfluence cannot see or change bank fees.
   - **Byfluence record higher than checkout total or listing** → possible pricing/system error. Escalate to **Payments & Finance**.
   - **Checkout total higher than listing** → check the option chosen and any fee line; if a seller price change is suspected, involve **Seller Operations**.
   - **Two deductions** → follow *Customer Charged Twice*.
   - **Undercharged / partial payment** → escalate to **Payments & Finance**; do not ask the customer to pay the difference until Payments decides.
4. Check that the booking/order itself is correct (right option, duration, quantity).
5. Record the four numbers and your conclusion.

- [ ] Payment located
- [ ] Four amounts compared and recorded
- [ ] Source of difference identified
- [ ] Escalated if Byfluence-side

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand the amount taken is different from what you expected, and I'm sorry for the confusion.

To find out where the difference comes from, please send me:
1. The transaction reference from your receipt or SMS
2. The amount you expected to pay and where you saw it (listing or checkout page)
3. The exact amount deducted from your account
4. A screenshot of the price you saw, if you have one

Please do not share your PIN, password or verification codes — we will never ask for them.

Your case number is {{ticket_id}}. I will review it and get back to you.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የተቆረጠው መጠን ከጠበቁት የተለየ እንደሆነ ተረድቻለሁ፤ ለተፈጠረው ግራ መጋባት ይቅርታ እንጠይቃለን።

ልዩነቱ ከየት እንደመጣ ለማወቅ እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ከደረሰኝዎ ወይም ከኤስኤምኤሱ ላይ ያለውን የግብይት መለያ ቁጥር
2. ለመክፈል የጠበቁትን መጠን እና የት እንዳዩት (በዝርዝሩ ወይስ በክፍያ ገጹ ላይ)
3. ከሂሳብዎ የተቀነሰውን ትክክለኛ መጠን
4. ያዩት ዋጋ ስክሪንሾት ካለዎት

እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድ አያጋሩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ገምግሜ መልስ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry for the confusion. Please send the reference, the amount you expected (and where you saw it), the amount deducted, and a screenshot if you have one. I'll check it. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለግራ መጋባቱ ይቅርታ። እባክዎ የግብይት ቁጥሩን፣ የጠበቁትን መጠን (የት እንዳዩት)፣ የተቀነሰውን መጠን እና ስክሪንሾት ካለ ይላኩ። አጣራለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our payments team is reviewing the amount charged for transaction {{transaction_id}}. Your case is being actively handled and we will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ቡድናችን ለግብይት ቁጥር {{transaction_id}} የተቆረጠውን መጠን እየገመገመ ነው። ጉዳይዎ በንቃት እየተከታተለ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Byfluence recorded more than the checkout total or listing price → **Payments & Finance**, priority High.
- Undercharge or partial payment → **Payments & Finance**.
- Seller changed the price after agreement or listed misleading prices → **Seller Operations**.
- Several customers report the same wrong amount on one listing → **Technical / Engineering** and **Seller Operations**.
- Customer disputes the charge formally → *Payment Dispute Raised by a Customer*.

## Resolution Procedure
1. Explain the source of the difference to the customer with the numbers you verified.
2. If Byfluence-side, confirm the correction (partial refund or adjustment) with Payments & Finance and share the status.
3. Record the four amounts, the cause and the outcome before resolving.

## Policy Pending Approval
- Decide how overcharges caused by pricing errors are corrected (partial refund vs. full refund and rebook) and who approves.
- Decide what happens when a customer is undercharged.
- Confirm whether any Byfluence buyer fee exists and how it is shown.

## Internal Notes
- Never confirm a bank's fee amount or exchange rate — tell the customer their bank is the right source.
- Keep the four-number comparison in internal notes; it saves the payments team time.
