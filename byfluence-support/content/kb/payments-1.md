<!-- doc -->
# Supported Payment Methods
id: pay-supported-methods
type: article
category: payments
subcategory: payment-methods
audience: both
priority: medium
department: support_l1
features: payments-chapa, payments-telebirr, payments-mpesa, payments-bank, payments-card, payments-stripe
tags: payment methods, how can I pay, which payment options, accepted payments, Chapa, Telebirr, M-Pesa, card, bank transfer, የክፍያ መንገዶች, እንዴት መክፈል እችላለሁ
related: pay-chapa, pay-telebirr, pay-mpesa, pay-card-payments, pay-bank-payments, pay-international-payments
templates: tpl-payment-failed-guidance
policy_pending: yes

## Summary
A buyer or seller asks which payment methods Byfluence accepts. No payment method is confirmed as live in this documentation — always check the Feature Status page before naming a method to a customer.

## Overview
Byfluence has worked with or considered several payment providers: **Chapa**, **Telebirr**, **M-Pesa**, **bank-based methods**, and **Stripe** (a possible option for international payments). The availability of **each** of these is **not confirmed** in this documentation. Methods may be switched on, paused or removed over time, so the only reliable source is the **Feature Status** page inside this support system.

The general payment flow is the same whatever the method:
1. The buyer selects a product or consultation.
2. Byfluence calculates the amount.
3. The buyer chooses a payment method on the checkout page.
4. The buyer pays on the provider's page or app.
5. The provider processes the payment and sends confirmation to Byfluence.
6. Byfluence confirms the booking or order and updates the records.

Payment statuses an agent may see: **Pending, Successful, Failed, Canceled, Refund Pending, Refunded, Disputed**.

> [!WARNING] Do not tell a customer that a method is "available", "coming soon" or "launching on a date" unless the Feature Status page says so. Do not guess from what you see on the checkout page of your own account — what the customer sees may differ.

### How to answer the question
1. Open **Feature Status** and look at every payment feature: `payments-chapa`, `payments-telebirr`, `payments-mpesa`, `payments-bank`, `payments-card`, `payments-stripe`.
2. List to the customer **only** the methods marked **live**.
3. If the customer asks about a method that is not live, say it is not currently available and offer the live methods. Do not speculate about launch dates.
4. If the customer is outside Ethiopia or has only a foreign card, follow *Paying from Outside Ethiopia*.
5. If **no** method is shown as live, or the page looks out of date, do not answer from memory — escalate to Senior Support / Supervisor and give the customer a holding reply.

## Customer Steps
1. Choose the consultation or item you want and continue to checkout.
2. On the payment step, the methods available to you are shown on screen.
3. Choose a method and follow the instructions on the provider's page or app.
4. Keep the receipt or SMS that shows the transaction reference until your booking or order is confirmed.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support.

At the moment you can pay on Byfluence using: {{payment_method}}. The payment options available to you are always shown on the checkout page when you pay.

A few tips for a smooth payment:
- Pay only through the Byfluence checkout page, never to a personal account or phone number.
- Keep the receipt or SMS with the transaction reference until your booking or order is confirmed.
- Byfluence will never ask for your PIN, password or any verification code — please do not share them with anyone.

Your case number is {{ticket_id}}. If you have any trouble paying, just reply here and we will help.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን።

በአሁኑ ወቅት በ Byfluence ላይ በሚከተሉት መንገዶች መክፈል ይችላሉ፦ {{payment_method}}። ለእርስዎ የሚገኙት የክፍያ አማራጮች ሁልጊዜ በክፍያ ገጹ (checkout) ላይ ይታያሉ።

ክፍያዎ ያለችግር እንዲፈጸም፦
- ክፍያውን የሚፈጽሙት በ Byfluence የክፍያ ገጽ ብቻ ይሁን፤ ወደ ግል የባንክ ሂሳብ ወይም ስልክ ቁጥር አይክፈሉ።
- ቀጠሮዎ ወይም ትዕዛዝዎ እስኪረጋገጥ ድረስ የግብይት መለያ ቁጥሩ ያለበትን ደረሰኝ ወይም ኤስኤምኤስ ያስቀምጡ።
- Byfluence ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ በፍጹም አይጠይቅዎትም — እባክዎ ለማንም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። በክፍያ ወቅት ማንኛውም ችግር ካጋጠመዎት እዚሁ ይጻፉልን፤ እንረዳዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, you can currently pay with: {{payment_method}}. Available options always show on the checkout page. Pay only through Byfluence checkout and never share your PIN or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በአሁኑ ወቅት በ {{payment_method}} መክፈል ይችላሉ። የሚገኙ አማራጮች ሁልጊዜ በክፍያ ገጹ ላይ ይታያሉ። በ Byfluence የክፍያ ገጽ ብቻ ይክፈሉ፤ ፒን ወይም ኮድ ለማንም አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Feature Status shows no live payment method, or it contradicts what customers report seeing at checkout → **Senior Support / Supervisor**.
- A customer says a method was shown at checkout but failed every time → follow *Payment Failed*; if several customers report it → **Technical / Engineering** and notify a supervisor.
- A business or partner asks to integrate a new payment method → **Senior Support / Supervisor** (log as a partnership inquiry).
- Anyone asks the customer to pay outside the checkout page → follow *Seller Asks Buyer to Pay Outside Byfluence* (**Trust & Safety**).

## Policy Pending Approval
- Confirm which payment providers are live in production and keep the Feature Status page up to date.
- Approve the official customer wording for methods that are "not yet available" (whether support may say "planned").
- Decide whether different methods are offered for different product types (consultations, physical products, digital products).

## Internal Notes
- Fill `{{payment_method}}` with the exact list of live methods from Feature Status, in the customer's language (e.g. "Chapa").
- Customers often say "Telebirr" or "CBE" when they mean the wallet or bank they used *inside* a provider's checkout. Ask what they saw on screen before concluding which method they used.
- If a customer says "the seller told me to pay by Telebirr to his number", this is an off-platform payment risk — switch to *Seller Asks Buyer to Pay Outside Byfluence*.

<!-- doc -->
# Paying with Chapa
id: pay-chapa
type: article
category: payments
subcategory: payment-methods
audience: buyer
priority: medium
department: support_l1
features: payments-chapa
tags: Chapa, Chapa payment, Chapa checkout, how to pay with Chapa, Chapa receipt, Chapa reference, በቻፓ መክፈል, ቻፓ
related: pay-supported-methods, pay-failed-transaction, pay-pending-transaction, pay-transaction-reference-help, pay-paid-booking-not-confirmed
templates: tpl-payment-failed-guidance, tpl-request-transaction-ref
policy_pending: yes

## Summary
Explains how a buyer pays through Chapa at Byfluence checkout and what to do if the Chapa step does not complete. Check Feature Status first — Chapa is not confirmed as live in this documentation.

## Overview
Chapa is an Ethiopian payment gateway that Byfluence has worked with or considered. When Chapa is live, the buyer is sent from the Byfluence checkout to a Chapa payment page, completes the payment there, and is returned to Byfluence. Chapa then sends a confirmation to Byfluence, and the booking or order is confirmed.

> [!NOTE] Check the **Feature Status** page (`payments-chapa`) before telling a customer Chapa is available. If it is not live, follow *Supported Payment Methods*.

What agents need to know:
- The buyer pays on Chapa's page, **not** on a Byfluence form. The Chapa page may offer several ways to pay (for example a wallet, bank or card); which ones appear is controlled by Chapa and Byfluence's configuration and is not confirmed here.
- After payment, the buyer should see a success page and/or receive a receipt (on screen, by email or SMS — depending on the option used). This receipt contains the **transaction reference** support needs.
- The booking or order is confirmed only after Byfluence receives Chapa's confirmation. If the buyer closes the page early, confirmation may be delayed.
- Common problems: page does not load, payment declined, buyer leaves before redirect, payment shows as pending. See *Payment Failed* and *Payment Stuck as Pending*.

## Customer Steps
1. On the Byfluence checkout page, choose **Chapa**.
2. You will be taken to the Chapa payment page. Check that the amount and the merchant name are correct.
3. Choose how you want to pay on the Chapa page and follow the instructions (for example, approve the payment on your phone).
4. Wait until you see the success page and are returned to Byfluence. Do not close the browser or press "back" during payment.
5. Save the receipt or screenshot showing the transaction reference.
6. Check your Byfluence dashboard for the confirmed booking or order.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support.

Here is how to pay with Chapa:
1. On the checkout page, choose Chapa.
2. On the Chapa page, check that the amount is correct, choose how you want to pay and follow the instructions.
3. Please wait until you see the success page and return to Byfluence — do not close the page during payment.
4. Keep the receipt with the transaction reference until your booking or order is confirmed.

If anything goes wrong, send us the transaction reference and the time of payment and we will check it for you. Please never share your PIN, password or verification codes — Byfluence will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን።

በ Chapa ለመክፈል፦
1. በክፍያ ገጹ ላይ Chapa የሚለውን ይምረጡ።
2. በ Chapa ገጹ ላይ የገንዘቡ መጠን ትክክል መሆኑን ያረጋግጡ፤ የሚፈልጉትን የክፍያ አማራጭ መርጠው መመሪያውን ይከተሉ።
3. የስኬት ገጹን አይተው ወደ Byfluence እስኪመለሱ ድረስ እባክዎ ይጠብቁ — በክፍያ ወቅት ገጹን አይዝጉ።
4. ቀጠሮዎ ወይም ትዕዛዝዎ እስኪረጋገጥ ድረስ የግብይት መለያ ቁጥሩ ያለበትን ደረሰኝ ያስቀምጡ።

ችግር ካጋጠመዎት የግብይት መለያ ቁጥሩን እና የከፈሉበትን ሰዓት ይላኩልን፤ እናጣራልዎታለን። እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድ በፍጹም አያጋሩ — Byfluence በፍጹም አይጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, choose Chapa at checkout, confirm the amount on the Chapa page, complete payment and wait to be returned to Byfluence. Keep your receipt/reference. Never share your PIN or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በክፍያ ገጹ Chapaን ይምረጡ፣ በ Chapa ገጽ ላይ መጠኑን አረጋግጠው ክፍያውን ይፈጽሙ፤ ወደ Byfluence እስኪመለሱ ይጠብቁ። ደረሰኙን/የግብይት ቁጥሩን ያስቀምጡ። ፒን ወይም ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Customer was charged but the booking/order is not confirmed → follow *Paid but Not Confirmed* (consultations) or *Paid but Product Order Not Confirmed*; escalate to **Payments & Finance** with the reference.
- The Chapa page does not load or errors for several customers at the same time → **Technical / Engineering**, notify a supervisor (possible incident).
- The Chapa page shows a different merchant name or amount than expected → stop and escalate to **Trust & Safety** (possible phishing link).

## Policy Pending Approval
- Confirm Chapa's production status and which payment options inside Chapa are enabled for Byfluence.
- Confirm whether Chapa sends receipts by email/SMS for every option, and what the receipt reference is called.
- Approve the wording support may use about how long Chapa confirmation usually takes.

## Internal Notes
- Ask which option the customer used *inside* Chapa (wallet, bank, card) — it tells you where to look for their reference (see *Helping Customers Find Their Transaction Reference*).
- A Chapa receipt screenshot is supporting evidence only. Confirm the payment by searching the reference in the admin dashboard or Chapa portal (if you have authorized access).
- If the customer received a "Chapa" link by Telegram or SMS from someone other than the checkout page, treat it as a possible scam.

<!-- doc -->
# Paying with Telebirr (When Officially Supported)
id: pay-telebirr
type: article
category: payments
subcategory: payment-methods
audience: buyer
priority: medium
department: support_l1
features: payments-telebirr
tags: Telebirr, pay with Telebirr, Telebirr payment, Telebirr SMS, Telebirr not working, ቴሌብር, በቴሌብር መክፈል
related: pay-supported-methods, pay-chapa, pay-transaction-reference-help, pay-payment-security, pay-off-platform-payment
templates: tpl-payment-failed-guidance, tpl-request-transaction-ref
policy_pending: yes

## Summary
A buyer wants to pay with Telebirr. Telebirr is not confirmed as a Byfluence payment method — check Feature Status before saying it is available, and never let a customer pay Telebirr to a personal number.

## Overview
Telebirr is a widely used Ethiopian mobile-money service. Byfluence has worked with or considered Telebirr, but its integration status is **not confirmed** in this documentation.

> [!NOTE] Check the **Feature Status** page (`payments-telebirr`) before every answer. Also check whether Telebirr appears as an option **inside** another provider's checkout (for example on the Chapa page) — if so, the customer is paying through that provider, and the Chapa article applies.

**If Telebirr is live:** the buyer chooses Telebirr at checkout, approves the payment on their phone (in the Telebirr app or by the prompt they receive), and receives a Telebirr SMS with a transaction number. The booking or order is confirmed after Byfluence receives confirmation.

**If Telebirr is not live:** tell the customer it is not currently available on Byfluence and offer the live methods from Feature Status. Do not give dates.

> [!WARNING] Mobile-money PIN scams are common. Byfluence will **never** ask for a Telebirr PIN, and a customer should only enter their PIN in their own Telebirr app or official prompt — never in a chat, call or web form sent by another person. Never ask a buyer to "send money to this Telebirr number" — Byfluence does not take payments to personal numbers.

## Customer Steps
(Only when Feature Status shows Telebirr as live.)
1. At checkout, choose **Telebirr**.
2. Check that the amount shown is correct.
3. Approve the payment in your own Telebirr app or official prompt on your phone. Enter your PIN only there — never share it with anyone.
4. Wait for the success page and keep the Telebirr SMS with the transaction number.
5. Check your Byfluence dashboard for the confirmed booking or order.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support.

[If Telebirr is live] You can pay with Telebirr: choose Telebirr at checkout, check the amount, and approve the payment in your own Telebirr app or official prompt. Please keep the Telebirr SMS with the transaction number until your booking or order is confirmed.

[If Telebirr is not live] Telebirr is not available on Byfluence at the moment. You can currently pay using: {{payment_method}}.

Important: only pay through the Byfluence checkout page. Byfluence will never ask you to send money to a personal Telebirr number, and we will never ask for your PIN or verification codes — please do not share them with anyone.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን።

[Telebirr የሚሰራ ከሆነ] በ Telebirr መክፈል ይችላሉ፦ በክፍያ ገጹ ላይ Telebirr ን ይምረጡ፣ የገንዘቡን መጠን ያረጋግጡ፣ ከዚያም ክፍያውን በራስዎ የ Telebirr መተግበሪያ ወይም በይፋዊ መልዕክቱ ያጽድቁ። ቀጠሮዎ ወይም ትዕዛዝዎ እስኪረጋገጥ ድረስ የግብይት ቁጥሩ ያለበትን የ Telebirr ኤስኤምኤስ ያስቀምጡ።

[Telebirr የማይሰራ ከሆነ] በአሁኑ ወቅት Telebirr በ Byfluence ላይ አይገኝም። አሁን በ {{payment_method}} መክፈል ይችላሉ።

ማሳሰቢያ፦ ክፍያ የሚፈጽሙት በ Byfluence የክፍያ ገጽ ብቻ ይሁን። Byfluence ወደ ግል የ Telebirr ቁጥር ገንዘብ እንዲልኩ በፍጹም አይጠይቅዎትም፤ ፒንዎን ወይም የማረጋገጫ ኮድ በፍጹም አንጠይቅም — እባክዎ ለማንም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, [live] choose Telebirr at checkout and approve in your own Telebirr app; keep the SMS. [not live] Telebirr isn't available yet — you can pay with {{payment_method}}. Never send money to personal numbers or share your PIN. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ [የሚሰራ ከሆነ] በክፍያ ገጹ Telebirr ን መርጠው በራስዎ መተግበሪያ ያጽድቁ፤ ኤስኤምኤሱን ያስቀምጡ። [የማይሰራ ከሆነ] Telebirr ገና አይገኝም — በ {{payment_method}} መክፈል ይችላሉ። ወደ ግል ቁጥር አይላኩ፤ ፒን አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Customer already paid by Telebirr to a seller's or stranger's personal number → **Trust & Safety** (follow *Seller Asks Buyer to Pay Outside Byfluence*); priority High.
- Customer shared their Telebirr PIN with someone claiming to be Byfluence → **Trust & Safety**, priority Critical; advise them to contact Telebirr/Ethio telecom immediately through official channels to secure their wallet.
- Telebirr is live but payments fail for several customers → **Technical / Engineering** and **Payments & Finance**.
- Customer was charged but not confirmed → *Paid but Not Confirmed* flow, **Payments & Finance**.

## Policy Pending Approval
- Confirm whether Telebirr is integrated directly, offered through another gateway, or not available.
- Approve the official wording for "not available yet" (whether support may say it is planned).
- Confirm how Telebirr references appear in the admin dashboard so agents can match them.

## Internal Notes
- Delete the bracketed option that does not apply before sending.
- Many customers say "I paid with Telebirr" when they chose Telebirr inside a gateway page. Ask them to describe the screens they saw.
- A Telebirr SMS forwarded as a screenshot is not proof of payment — verify the transaction number through authorized tools.

<!-- doc -->
# Paying with M-Pesa (When Officially Supported)
id: pay-mpesa
type: article
category: payments
subcategory: payment-methods
audience: buyer
priority: medium
department: support_l1
features: payments-mpesa
tags: M-Pesa, Mpesa, Safaricom M-Pesa, pay with M-Pesa, M-Pesa SMS, ኤምፔሳ, በኤምፔሳ መክፈል
related: pay-supported-methods, pay-telebirr, pay-transaction-reference-help, pay-payment-security, pay-off-platform-payment
templates: tpl-payment-failed-guidance, tpl-request-transaction-ref
policy_pending: yes

## Summary
A buyer wants to pay with M-Pesa. M-Pesa is not confirmed as a Byfluence payment method — check Feature Status first and never direct payment to a personal M-Pesa number.

## Overview
M-Pesa (Safaricom M-Pesa in Ethiopia) is a mobile-money service Byfluence has worked with or considered. Its integration status is **not confirmed** in this documentation.

> [!NOTE] Check the **Feature Status** page (`payments-mpesa`) before answering. M-Pesa may also appear as an option **inside** another provider's checkout page — in that case the customer is paying through that provider.

**If M-Pesa is live:** the buyer chooses M-Pesa at checkout, approves the payment on their own phone (M-Pesa app or official prompt), and receives an M-Pesa confirmation SMS with a transaction ID. Byfluence confirms the booking or order after receiving confirmation.

**If M-Pesa is not live:** say it is not currently available on Byfluence and offer the live methods. No dates.

> [!WARNING] Never ask for an M-Pesa PIN. Warn customers that anyone asking for their PIN or asking them to "reverse" or "re-send" money to a personal number is likely a scammer, even if they use the Byfluence name.

## Customer Steps
(Only when Feature Status shows M-Pesa as live.)
1. At checkout, choose **M-Pesa**.
2. Check the amount.
3. Approve the payment in your own M-Pesa app or official phone prompt. Enter your PIN only there.
4. Wait for the success page and keep the M-Pesa SMS with the transaction ID.
5. Check your Byfluence dashboard for the confirmed booking or order.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support.

[If M-Pesa is live] You can pay with M-Pesa: choose M-Pesa at checkout, check the amount, and approve the payment in your own M-Pesa app or official prompt. Please keep the M-Pesa SMS with the transaction ID until your booking or order is confirmed.

[If M-Pesa is not live] M-Pesa is not available on Byfluence at the moment. You can currently pay using: {{payment_method}}.

Please pay only through the Byfluence checkout page. We will never ask you to send money to a personal number, and we will never ask for your PIN or any verification code — please do not share them with anyone.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን።

[M-Pesa የሚሰራ ከሆነ] በ M-Pesa መክፈል ይችላሉ፦ በክፍያ ገጹ ላይ M-Pesa ን ይምረጡ፣ መጠኑን ያረጋግጡ፣ ከዚያም ክፍያውን በራስዎ የ M-Pesa መተግበሪያ ወይም በይፋዊ መልዕክቱ ያጽድቁ። ቀጠሮዎ ወይም ትዕዛዝዎ እስኪረጋገጥ ድረስ የግብይት መለያ ቁጥሩ ያለበትን የ M-Pesa ኤስኤምኤስ ያስቀምጡ።

[M-Pesa የማይሰራ ከሆነ] በአሁኑ ወቅት M-Pesa በ Byfluence ላይ አይገኝም። አሁን በ {{payment_method}} መክፈል ይችላሉ።

እባክዎ ክፍያ የሚፈጽሙት በ Byfluence የክፍያ ገጽ ብቻ ይሁን። ወደ ግል ቁጥር ገንዘብ እንዲልኩ በፍጹም አንጠይቅዎትም፤ ፒንዎን ወይም ማንኛውንም የማረጋገጫ ኮድ በፍጹም አንጠይቅም — እባክዎ ለማንም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, [live] choose M-Pesa at checkout and approve in your own M-Pesa app; keep the SMS. [not live] M-Pesa isn't available yet — you can pay with {{payment_method}}. Never send to personal numbers or share your PIN. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ [የሚሰራ ከሆነ] በክፍያ ገጹ M-Pesa ን መርጠው በራስዎ መተግበሪያ ያጽድቁ፤ ኤስኤምኤሱን ያስቀምጡ። [የማይሰራ ከሆነ] M-Pesa ገና አይገኝም — በ {{payment_method}} መክፈል ይችላሉ። ወደ ግል ቁጥር አይላኩ፤ ፒን አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Customer paid M-Pesa to a personal number at someone's request → **Trust & Safety**, priority High.
- Customer shared their M-Pesa PIN → **Trust & Safety**, priority Critical; advise them to contact Safaricom through official channels immediately.
- M-Pesa is live but failing for several customers → **Technical / Engineering** and **Payments & Finance**.
- Charged but not confirmed → **Payments & Finance** via the *Paid but Not Confirmed* flow.

## Policy Pending Approval
- Confirm M-Pesa's integration status (direct, via gateway, or not available).
- Approve the "not available yet" wording.
- Confirm how M-Pesa transaction IDs appear in the admin dashboard.

## Internal Notes
- Delete the bracketed option that does not apply before sending.
- Customers sometimes confuse M-Pesa with Telebirr or bank wallets; confirm by asking which app sent the SMS.
- Verify by transaction ID in authorized tools — never accept the SMS screenshot alone.

<!-- doc -->
# Card Payments (When Supported)
id: pay-card-payments
type: article
category: payments
subcategory: payment-methods
audience: buyer
priority: medium
department: support_l1
features: payments-card, payments-stripe
tags: card payment, Visa, Mastercard, debit card, credit card, card declined, pay by card, 3D Secure, በካርድ መክፈል, ካርድ
related: pay-supported-methods, pay-international-payments, pay-failed-transaction, pay-currency-and-fees-questions, pay-payment-security
templates: tpl-payment-failed-guidance
policy_pending: yes

## Summary
A buyer asks whether they can pay by debit or credit card. Card payments are not confirmed as live — check Feature Status, and never collect card details in chat, email or by phone.

## Overview
Card payments may be offered directly, through a gateway such as Chapa, or (for international buyers) through Stripe, which is a **potential** option only. None of these is confirmed in this documentation.

> [!NOTE] Check **Feature Status** for `payments-card` and `payments-stripe` before answering. If cards are not live, offer the live methods.

**If cards are live:**
- The buyer enters card details only on the secure provider page that opens from Byfluence checkout — **never** in chat, email, Telegram, or on the phone.
- The bank may ask the buyer to approve the payment (for example by a code sent to their phone or in their banking app). This code is for the bank's page only and must never be shared with anyone, including support.
- Common declines: insufficient funds, card not enabled for online or international payments, wrong expiry date, bank security block, card currency restrictions.
- A card payment may show as a "hold" on the statement before it settles or is released; a declined payment can still show a temporary hold.

> [!WARNING] Never ask for or accept a full card number, CVV/security code, expiry date or OTP. If a customer sends a full card number in chat, do not repeat it, ask them to delete the message if the channel allows, advise them to contact their bank if they are worried, and note in the ticket that sensitive data was received (do not copy it).

## Customer Steps
(Only when Feature Status shows card payments as live.)
1. At checkout, choose the card option.
2. Enter your card details only on the secure payment page that opens.
3. If your bank asks you to approve the payment, approve it in your bank's app or page. Never share that code with anyone.
4. Wait for the success page and keep the receipt.
5. If the card is declined, check with your bank that online (and, if relevant, international) payments are enabled, then try again or use another method.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support.

[If cards are live] You can pay by card at checkout. Please enter your card details only on the secure payment page that opens from Byfluence. If your card is declined, your bank may need to enable online payments on your card — your bank can confirm this for you.

[If cards are not live] Card payments are not available on Byfluence at the moment. You can currently pay using: {{payment_method}}.

For your safety, please never send your card number, security code (CVV) or any verification code by chat, email or phone — Byfluence will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን።

[ካርድ የሚሰራ ከሆነ] በክፍያ ገጹ ላይ በካርድ መክፈል ይችላሉ። የካርድዎን መረጃ የሚያስገቡት ከ Byfluence በሚከፈተው ደህንነቱ የተጠበቀ የክፍያ ገጽ ላይ ብቻ ይሁን። ካርድዎ ውድቅ ከተደረገ፣ ባንክዎ በካርድዎ የኦንላይን ክፍያን መፍቀድ ሊያስፈልገው ይችላል — ባንክዎ ሊያረጋግጥልዎት ይችላል።

[ካርድ የማይሰራ ከሆነ] በአሁኑ ወቅት የካርድ ክፍያ በ Byfluence ላይ አይገኝም። አሁን በ {{payment_method}} መክፈል ይችላሉ።

ለደህንነትዎ ሲባል የካርድ ቁጥርዎን፣ የደህንነት ኮዱን (CVV) ወይም ማንኛውንም የማረጋገጫ ኮድ በቻት፣ በኢሜይል ወይም በስልክ አይላኩ — Byfluence በፍጹም አይጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, [live] you can pay by card on the secure checkout page; if declined, ask your bank to enable online payments. [not live] Cards aren't available yet — use {{payment_method}}. Never send card numbers, CVV or codes in chat. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ [የሚሰራ ከሆነ] በደህንነቱ በተጠበቀው የክፍያ ገጽ በካርድ መክፈል ይችላሉ፤ ውድቅ ከሆነ ባንክዎን ያነጋግሩ። [የማይሰራ ከሆነ] ካርድ ገና አይገኝም — በ {{payment_method}} ይክፈሉ። የካርድ ቁጥር፣ CVV ወይም ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Customer reports a card charge they did not make → **Trust & Safety** (see *Unauthorized Transaction*, `tns-unauthorized-transaction`).
- Customer says their bank is reversing the charge / filing a chargeback → follow *Chargeback or Bank Reversal Request* (**Payments & Finance**).
- Card was charged but the order/booking is not confirmed → **Payments & Finance**.
- Customer sent full card details in a support channel → **Trust & Safety** (data-handling incident), priority High.

## Policy Pending Approval
- Confirm whether card payments are live, and through which provider.
- Confirm whether foreign cards are accepted and in which currency cards are charged.
- Decide the procedure for support channels that receive card details by mistake (redaction, deletion, reporting).

## Internal Notes
- "Card declined" is decided by the customer's bank; support cannot override it. Do not tell the customer to retry many times — repeated attempts can trigger bank blocks and multiple holds.
- A temporary hold after a decline is common; ask the customer to check with their bank before treating it as a duplicate charge.

<!-- doc -->
# Bank-Based Payments
id: pay-bank-payments
type: article
category: payments
subcategory: payment-methods
audience: buyer
priority: medium
department: support_l1
features: payments-bank
tags: bank transfer, pay from bank, CBE, mobile banking, bank payment, bank SMS, direct deposit, በባንክ መክፈል, የባንክ ዝውውር
related: pay-supported-methods, pay-transaction-reference-help, pay-pending-transaction, pay-off-platform-payment, pay-payment-verification
templates: tpl-request-transaction-ref, tpl-payment-pending-explain
policy_pending: yes

## Summary
A buyer wants to pay from their bank account (mobile banking, internet banking or a bank option inside a payment gateway). Bank-based payments are not confirmed — check Feature Status, and never accept manual transfers to unofficial accounts.

## Overview
"Bank-based payment" can mean different things to a customer:
- Choosing a **bank option inside the Byfluence checkout** (directly or through a gateway such as Chapa).
- Paying from their **mobile/internet banking app** after being redirected from checkout.
- A **manual transfer** to an account number — this is **not** a confirmed Byfluence payment method.

> [!NOTE] Check **Feature Status** (`payments-bank`) to see whether bank payments are live and which banks are included. Do not name banks that are not listed.

> [!WARNING] Never give a customer a bank account number to transfer money to, and never accept a manual transfer as payment for a booking or order unless an approved official process exists (none is confirmed). If someone — including a person claiming to be a seller or Byfluence staff — gave the customer an account number, treat it as an off-platform payment risk.

**If bank payments are live:** the buyer pays through the checkout flow, receives a bank SMS or app confirmation with a reference, and the booking/order is confirmed after Byfluence receives confirmation. Bank confirmations can take longer than wallet payments, so the payment may show as **Pending** for a while.

## Customer Steps
(Only when Feature Status shows bank payments as live.)
1. At checkout, choose the bank option and your bank (if listed).
2. Follow the instructions to approve the payment in your bank's app or page.
3. Keep the bank SMS or app receipt that shows the transaction reference.
4. Check your Byfluence dashboard. If it still shows pending, contact support with the reference.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support.

[If bank payments are live] You can pay from your bank by choosing the bank option at checkout and approving the payment in your bank's app or page. Please keep the bank SMS or receipt with the transaction reference until your booking or order is confirmed.

[If bank payments are not live] Paying directly from a bank is not available on Byfluence at the moment. You can currently pay using: {{payment_method}}.

Please note: Byfluence does not ask customers to transfer money manually to a personal or business account number. Always pay through the checkout page. We will also never ask for your PIN, password or verification codes.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን።

[የባንክ ክፍያ የሚሰራ ከሆነ] በክፍያ ገጹ ላይ የባንክ አማራጩን መርጠው ክፍያውን በባንክዎ መተግበሪያ ወይም ገጽ በማጽደቅ ከባንክ ሂሳብዎ መክፈል ይችላሉ። ቀጠሮዎ ወይም ትዕዛዝዎ እስኪረጋገጥ ድረስ የግብይት መለያ ቁጥሩ ያለበትን የባንክ ኤስኤምኤስ ወይም ደረሰኝ ያስቀምጡ።

[የባንክ ክፍያ የማይሰራ ከሆነ] በአሁኑ ወቅት በቀጥታ ከባንክ መክፈል በ Byfluence ላይ አይገኝም። አሁን በ {{payment_method}} መክፈል ይችላሉ።

ማሳሰቢያ፦ Byfluence ደንበኞች ገንዘብ ወደ ግል ወይም የንግድ ሂሳብ ቁጥር በእጅ እንዲያስተላልፉ አይጠይቅም። ሁልጊዜ በክፍያ ገጹ በኩል ይክፈሉ። ፒንዎን፣ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድ በፍጹም አንጠይቅም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, [live] choose the bank option at checkout and approve in your bank app; keep the SMS. [not live] Bank payment isn't available yet — use {{payment_method}}. We never ask for manual transfers to account numbers. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ [የሚሰራ ከሆነ] በክፍያ ገጹ የባንክ አማራጩን መርጠው በባንክ መተግበሪያዎ ያጽድቁ፤ ኤስኤምኤሱን ያስቀምጡ። [የማይሰራ ከሆነ] የባንክ ክፍያ ገና አይገኝም — በ {{payment_method}} ይክፈሉ። ወደ ሂሳብ ቁጥር በእጅ እንዲያስተላልፉ አንጠይቅም። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Customer already made a manual transfer to an account number given by a seller or "agent" → **Trust & Safety**, priority High.
- Bank payment shows as pending in Byfluence long after the customer's bank shows success → **Payments & Finance** with the reference.
- Customer claims to have paid by manual transfer to an official-looking Byfluence account → **Payments & Finance** and **Trust & Safety** (confirm whether any such account exists before saying anything).

## Policy Pending Approval
- Confirm whether bank payments are live, through which provider, and which banks are supported.
- Decide whether Byfluence will ever accept manual bank transfers (e.g., for large orders) and, if so, the verification process.
- Approve wording on typical bank confirmation delays.

## Internal Notes
- Bank SMS screenshots are easy to edit. Only a match in the admin dashboard or provider portal counts as verified.
- If the customer's bank shows success but Byfluence shows nothing, collect the reference, the bank name, the exact amount and time — then follow *Payment Stuck as Pending*.

<!-- doc -->
# Paying from Outside Ethiopia / Foreign Cards
id: pay-international-payments
type: article
category: payments
subcategory: payment-methods
audience: buyer
priority: medium
department: support_l1
features: payments-stripe, payments-card
tags: international payment, foreign card, pay from abroad, diaspora, USD, Stripe, PayPal, Visa abroad, ከውጭ ሀገር መክፈል, ዳያስፖራ, የውጭ ካርድ
related: pay-supported-methods, pay-card-payments, pay-currency-and-fees-questions, pay-failed-transaction, pay-off-platform-payment
templates: tpl-payment-failed-guidance
policy_pending: yes

## Summary
A buyer outside Ethiopia (often diaspora) wants to pay with a foreign card or international method. International payments are not confirmed; Stripe is only a potential option — check Feature Status and do not suggest workarounds.

## Overview
Byfluence prices are shown for the Ethiopian market. Stripe is mentioned as a **potential** international payment option; its status — and whether foreign cards work through any other provider — is **not confirmed**.

> [!NOTE] Check **Feature Status** for `payments-stripe` and `payments-card` before answering. If neither is live, tell the customer international payment is not currently available.

What agents should know:
- A foreign card may be declined if the provider only accepts local cards, or if the card's bank blocks international/online payments.
- If a foreign card is accepted, the buyer's bank may convert currency and add its own fees; the amount on their statement can differ from the ETB price (see *Currency, Extra Fees and Price Shown vs Charged*).
- Buyers abroad often book consultations — remind them that session times are shown in a specific time zone (see consultation booking articles).

> [!WARNING] Do **not** suggest workarounds such as "ask a relative in Ethiopia to pay for you by transfer to the seller", "send the money by remittance to the seller" or "pay the seller by PayPal". Paying outside Byfluence removes all buyer protection and is a common fraud pattern. A relative may pay through the normal Byfluence checkout on their own account only if that is permitted — not confirmed.

## Customer Steps
1. At checkout, look at the payment options shown to you.
2. If an international or card option is shown, use it and enter card details only on the secure payment page.
3. If your card is declined, ask your bank whether it allows online payments to Ethiopian merchants.
4. If no option works for you, contact support — do not pay any person directly.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your interest in Byfluence.

[If international payment is live] You can pay from outside Ethiopia using: {{payment_method}}. Your bank may convert the amount into your currency and may add its own charges; please check with your bank if the amount on your statement looks different.

[If not live] At the moment, Byfluence does not offer a payment option for cards or accounts outside Ethiopia. The available options are: {{payment_method}}. We have noted your request and will be happy to help once more options are available.

For your protection, please only pay through the Byfluence checkout page and never send money directly to a seller or another person.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ለ Byfluence ላሳዩት ፍላጎት እናመሰግናለን።

[ዓለም አቀፍ ክፍያ የሚሰራ ከሆነ] ከኢትዮጵያ ውጭ ሆነው በ {{payment_method}} መክፈል ይችላሉ። ባንክዎ መጠኑን ወደ ሀገርዎ ገንዘብ ሊቀይርና የራሱን ክፍያ ሊጨምር ይችላል፤ በሂሳብ መግለጫዎ ላይ ያለው መጠን የተለየ ከመሰለዎት እባክዎ ባንክዎን ያነጋግሩ።

[የማይሰራ ከሆነ] በአሁኑ ወቅት Byfluence ከኢትዮጵያ ውጭ ለሚገኙ ካርዶች ወይም ሂሳቦች የክፍያ አማራጭ አያቀርብም። የሚገኙት አማራጮች፦ {{payment_method}} ናቸው። ጥያቄዎን መዝግበናል፤ ተጨማሪ አማራጮች ሲኖሩ ልንረዳዎ ደስተኞች ነን።

ለጥበቃዎ ሲባል እባክዎ በ Byfluence የክፍያ ገጽ ብቻ ይክፈሉ፤ ገንዘብ በቀጥታ ለሻጭ ወይም ለሌላ ሰው አይላኩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, [live] from abroad you can pay with {{payment_method}}; your bank may convert currency and add charges. [not live] Payments from outside Ethiopia aren't available yet. Please never pay a seller directly. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ [የሚሰራ ከሆነ] ከውጭ ሀገር በ {{payment_method}} መክፈል ይችላሉ፤ ባንክዎ ምንዛሬ ሊቀይርና ክፍያ ሊጨምር ይችላል። [የማይሰራ ከሆነ] ከኢትዮጵያ ውጭ ክፍያ ገና አይገኝም። እባክዎ ለሻጭ በቀጥታ አይክፈሉ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- A seller offered to accept payment abroad (PayPal, remittance, crypto, etc.) → **Trust & Safety** via *Seller Asks Buyer to Pay Outside Byfluence*.
- An international buyer was charged but the booking is not confirmed → **Payments & Finance**.
- Business/partnership requests for international payment support → **Senior Support / Supervisor**.
- Repeated requests from diaspora customers → log the demand and inform the supervisor (product feedback).

## Policy Pending Approval
- Confirm whether any provider accepts foreign cards today, and whether Stripe will be adopted.
- Decide whether a third party (e.g. a relative in Ethiopia) may pay on a buyer's behalf, and how support should treat such payments.
- Confirm in which currency international buyers are charged and whether prices are shown in other currencies.

## Internal Notes
- Diaspora buyers are a valuable segment; tag these tickets (e.g. "international-payment-request") so demand can be measured.
- Never quote exchange rates or estimate the amount in foreign currency — the customer's bank decides this.

<!-- doc -->
# Currency, Extra Fees and Price Shown vs Charged
id: pay-currency-and-fees-questions
type: article
category: payments
subcategory: payment-methods
audience: buyer
priority: medium
department: support_l1
features: payments-chapa, payments-card
tags: extra fee, price different, charged more, service fee, transaction fee, currency, ETB, birr, VAT, ተጨማሪ ክፍያ, ዋጋ ልዩነት, ብር
related: pay-incorrect-amount, pay-international-payments, pay-card-payments, out-transaction-fees, pay-supported-methods
templates: tpl-payment-investigation, tpl-request-transaction-ref
policy_pending: yes

## Summary
A buyer asks why the amount at checkout or on their statement differs from the listed price, whether Byfluence adds fees, or which currency they pay in. Byfluence fee and tax rules are not confirmed — explain the possible reasons without inventing any fee.

## Overview
Buyers usually ask before paying ("Why is the total higher than the price?") or after paying ("My bank took more than the price"). There are several possible sources of a difference:
- **Byfluence-side:** a service/processing fee or tax may be added at checkout — **not confirmed**; only describe it if it is visible on the checkout page or in the order record.
- **Provider-side:** the payment provider or wallet may charge the customer a fee for the transfer.
- **Bank-side:** the customer's bank may charge a transfer fee, or convert currency for foreign cards.
- **Listing-side:** the seller changed the price, or the customer chose a different option (duration, quantity, variant).
- **Error:** a genuine wrong charge — follow *Charged a Different Amount Than Expected*.

Prices on Byfluence are expected to be in Ethiopian Birr (ETB); confirm on the listing and checkout page before telling the customer.

> [!WARNING] Never state a fee percentage, a tax rate or "Byfluence charges no fees" — none of these is confirmed. Describe only what the checkout page or the order record shows.

## Customer Steps
1. Before paying, review the total on the checkout page; it shows what you will be asked to pay on Byfluence.
2. After paying, compare the Byfluence receipt with your bank/wallet SMS.
3. If they differ, note both amounts and the transaction reference and contact support.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your question — I understand you want to be sure about what you are paying.

The total shown on the Byfluence checkout page is the amount requested for your booking or order. A different amount on your bank or wallet statement can happen if your bank or payment provider adds its own charge, or converts currency for a card from outside Ethiopia.

So I can check your specific payment, please send:
1. The transaction reference from your receipt or SMS
2. The amount shown at checkout and the amount taken from your account
3. The booking or order you paid for

Please do not share your PIN, password or verification codes — we will never ask for them.

Your case number is {{ticket_id}}. I will get back to you once I have reviewed it.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለጥያቄዎ እናመሰግናለን — የሚከፍሉትን መጠን በትክክል ማወቅ እንደሚፈልጉ ተረድቻለሁ።

በ Byfluence የክፍያ ገጽ ላይ የሚታየው ጠቅላላ መጠን ለቀጠሮዎ ወይም ለትዕዛዝዎ የሚጠየቀው ገንዘብ ነው። በባንክዎ ወይም በዋሌትዎ መግለጫ ላይ የተለየ መጠን ሊታይ የሚችለው ባንክዎ ወይም የክፍያ አቅራቢው የራሱን ክፍያ ሲጨምር፣ ወይም ከኢትዮጵያ ውጭ ለሆነ ካርድ ምንዛሬ ሲቀየር ነው።

የእርስዎን ክፍያ በተለይ ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ከደረሰኝዎ ወይም ከኤስኤምኤሱ ላይ ያለውን የግብይት መለያ ቁጥር
2. በክፍያ ገጹ ላይ የታየውን መጠን እና ከሂሳብዎ የተቀነሰውን መጠን
3. የከፈሉበትን ቀጠሮ ወይም ትዕዛዝ

እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድ አያጋሩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ካጣራሁ በኋላ መልስ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, the checkout total is what Byfluence requests; your bank/provider may add its own charge or convert currency. Send the reference, both amounts and what you paid for and I'll check. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በክፍያ ገጹ ያለው ጠቅላላ መጠን Byfluence የሚጠይቀው ነው፤ ባንክዎ/አቅራቢው የራሱን ክፍያ ሊጨምር ወይም ምንዛሬ ሊቀይር ይችላል። የግብይት ቁጥሩን፣ ሁለቱን መጠኖች እና የከፈሉበትን ይላኩ፤ አጣራለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- The amount recorded by Byfluence is higher than the checkout total or listing price → *Charged a Different Amount Than Expected*, **Payments & Finance**.
- Customer asks for an official breakdown of Byfluence fees or taxes, or a tax invoice → **Payments & Finance** (do not answer from memory).
- Seller is suspected of changing prices after the buyer committed → **Seller Operations**.

## Policy Pending Approval
- Confirm whether Byfluence charges buyers any service, processing or convenience fee, and how it is shown at checkout.
- Confirm whether prices include VAT or other taxes and how this is displayed.
- Confirm display currency and whether any other currencies will be shown.

## Internal Notes
- Fill nothing in about fees from memory. If the checkout page shows a fee line, you may read it back to the customer exactly as shown.
- Fee questions often hide a real problem (duplicate charge, wrong variant). Always ask for the reference and check the record.
