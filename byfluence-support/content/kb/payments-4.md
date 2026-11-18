<!-- doc -->
# Payment Security and Safe-Payment Advice
id: pay-payment-security
type: article
category: payments
subcategory: payment-security
audience: both
priority: high
department: trust_safety
features: payments-chapa, payments-telebirr, payments-mpesa
tags: payment security, safe payment, PIN scam, someone asked my PIN, fake Byfluence agent, phishing link, is it safe to pay, scam call, የክፍያ ደህንነት, ማጭበርበር, ፒን ጠየቁኝ
related: pay-off-platform-payment, tns-unauthorized-transaction, tns-report-fraud, pay-fake-payment-screenshots, pay-supported-methods
templates: tpl-payment-investigation
policy_pending: yes

## Summary
How to give customers safe-payment advice and what to do when someone has asked for, or obtained, their PIN, OTP, card details or password. Mobile-money PIN scams are common — treat any disclosure as urgent.

## Overview
Customers ask "Is it safe to pay on Byfluence?" or report suspicious calls, SMS or Telegram messages claiming to be from Byfluence, a seller or a payment provider. The most common scams in mobile money are:
- **PIN/OTP request**: "I am from Byfluence/Telebirr support, tell me the code we just sent to verify your payment / your refund."
- **Wrong-transfer trick**: "I sent money to your number by mistake, please send it back" (the original "transfer" is a fake SMS).
- **Fake refund**: "To receive your refund, approve this payment / give your PIN."
- **Off-platform payment**: a seller or "agent" asks the buyer to pay to a personal number or account for a discount.
- **Phishing links**: a link that looks like Byfluence or a payment page, sent by SMS/Telegram.
- **Fake support accounts** on Telegram or social media using the Byfluence name and logo.

### Core safe-payment rules to tell customers
1. Pay **only** through the Byfluence checkout page.
2. **Never share** your PIN, password, OTP or verification code, card number or CVV — with anyone, including Byfluence Support. We will never ask.
3. Enter your PIN only inside your own Telebirr/M-Pesa/bank app or the official prompt you started yourself.
4. Byfluence does not need you to "approve a payment" to receive a refund.
5. Contact Byfluence only through the official support channels ({{support_channel}}).
6. If unsure, stop and contact support before paying.

> [!WARNING] Agents must never ask for PINs, OTPs, passwords, full card numbers or CVV — not even "the last digits of the code". If a customer sends them anyway, do not repeat them, note "sensitive data received" in the ticket without copying it, and tell the customer to change their PIN/password.

## Issue Description
When a customer reports a scam attempt or a disclosure, the situation is one of:
- **Attempt only** (nothing shared, no money lost) → advice and report.
- **Credentials shared, no money lost yet** → urgent: secure the wallet/bank/account now.
- **Money lost** → urgent: provider + Byfluence Trust & Safety + possible unauthorized transactions on Byfluence.

## Information to Collect
- Customer identity (registered email or phone number)
- What happened, when, and through which channel (call, SMS, Telegram, website)
- The phone number, Telegram username, link or account that contacted them
- Whether they shared anything — **only ask what type** (PIN, OTP, password, card), never the value
- Whether money was lost, how much, and the transaction reference
- Screenshots of the messages (with any codes hidden)

## Troubleshooting Steps
1. Stay calm and reassuring; customers are often embarrassed or panicked.
2. Determine the situation (attempt / credentials shared / money lost).
3. If **credentials were shared**, give these steps immediately:
   - Contact their wallet provider or bank through **official** channels to block or secure the account and change the PIN.
   - Change their Byfluence password (if the Byfluence account may be affected) — via the official reset flow, not with your help over chat.
4. If **money was lost on Byfluence** (unauthorized booking/order or payment) → follow `tns-unauthorized-transaction` and escalate to **Trust & Safety**, priority Critical.
5. If money was lost **outside** Byfluence (sent to a scammer) → explain that the transfer happened outside Byfluence, advise them to contact their provider immediately and, if they wish, the police; record and escalate to **Trust & Safety** so the scammer's number/account can be reported.
6. If a fake Byfluence account, number or link is involved → **Trust & Safety** with all identifiers (`tns-report-fraud`).
7. Record the identifiers in the ticket so other agents recognize repeat patterns.

- [ ] Situation classified
- [ ] Securing steps given (if anything shared)
- [ ] Unauthorized Byfluence activity checked
- [ ] Scam identifiers recorded and reported

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us about this — you did the right thing.

Please remember:
- Byfluence will never ask for your PIN, password, OTP/verification code, card number or CVV — by phone, SMS, Telegram or email.
- Only pay through the Byfluence checkout page, never to a personal phone number or account.
- You never need to approve a payment or share a code to receive a refund.
- Only contact Byfluence through our official channels: {{support_channel}}.

If you shared any PIN, code or password, please contact your mobile-money provider or bank immediately through their official channels to secure your account, and change your PIN and password.

Could you send us the phone number, username or link that contacted you, and a screenshot of the message (please hide any codes)? This helps us protect other customers.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለዚህ ጉዳይ ስላሳወቁን እናመሰግናለን — ትክክለኛውን ነገር አድርገዋል።

እባክዎ ያስታውሱ፦
- Byfluence ፒንዎን፣ የይለፍ ቃልዎን፣ የማረጋገጫ ኮድ (OTP)፣ የካርድ ቁጥርዎን ወይም CVV በስልክ፣ በኤስኤምኤስ፣ በቴሌግራም ወይም በኢሜይል በፍጹም አይጠይቅም።
- ክፍያ የሚፈጽሙት በ Byfluence የክፍያ ገጽ ብቻ ይሁን፤ ወደ ግል ስልክ ቁጥር ወይም ሂሳብ አይክፈሉ።
- ተመላሽ ገንዘብ ለመቀበል ክፍያ ማጽደቅ ወይም ኮድ ማጋራት በፍጹም አያስፈልግዎትም።
- Byfluence ን የሚያገኙት በይፋዊ መንገዶቻችን ብቻ ይሁን፦ {{support_channel}}።

ማንኛውንም ፒን፣ ኮድ ወይም የይለፍ ቃል አጋርተው ከሆነ፣ እባክዎ ሂሳብዎን ለመጠበቅ የሞባይል ገንዘብ አቅራቢዎን ወይም ባንክዎን በይፋዊ መንገዶቻቸው ወዲያውኑ ያነጋግሩ፤ ፒንዎን እና የይለፍ ቃልዎን ይቀይሩ።

ያገኘዎትን ስልክ ቁጥር፣ የተጠቃሚ ስም ወይም ሊንክ እና የመልዕክቱን ስክሪንሾት (ኮዶቹን ደብቀው) ሊልኩልን ይችላሉ? ይህ ሌሎች ደንበኞችን ለመጠበቅ ይረዳናል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thank you for telling us. Byfluence never asks for your PIN, password or codes, and never asks you to pay a personal number. If you shared anything, contact your provider/bank now and change your PIN. Please send us the number/link that contacted you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን። Byfluence ፒን፣ የይለፍ ቃል ወይም ኮድ አይጠይቅም፤ ወደ ግል ቁጥር እንዲከፍሉም አይጠይቅም። ያጋሩት ነገር ካለ አሁኑኑ አቅራቢዎን/ባንክዎን አነጋግረው ፒንዎን ይቀይሩ። ያገኘዎትን ቁጥር/ሊንክ ይላኩልን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Customer shared a PIN/OTP/password or card details → **Trust & Safety**, priority Critical.
- Unauthorized payment or booking/order on Byfluence → **Trust & Safety** (`tns-unauthorized-transaction`), priority Critical.
- Fake Byfluence support account, phone number, website or link → **Trust & Safety**, priority High.
- Multiple customers report the same scam → **Trust & Safety** and supervisor; consider an Announcement for agents.
- A Byfluence seller is involved in the scam → **Trust & Safety** and **Seller Operations**.

## Resolution Procedure
1. Confirm the customer has secured their wallet/bank/account (or was advised to).
2. Confirm any Byfluence-side unauthorized activity has been handed to Trust & Safety.
3. Record scam identifiers in the ticket and report them.
4. Close with a short safety reminder.

## Policy Pending Approval
- Confirm the official support channels to place in `{{support_channel}}` and publish them so customers can recognize fake accounts.
- Decide whether Byfluence reports scam numbers/accounts to providers or authorities, and who does it.
- Decide whether Byfluence will compensate customers in any scam scenario (none may be promised).

## Internal Notes
- Never blame the customer. Scammers are skilled; shame stops people reporting.
- You cannot block a Telebirr/M-Pesa/bank account — only the provider can. Say so clearly and send them there.
- Elderly and low-digital-literacy customers are frequent targets; consider calling them back to make sure the securing steps were done.

<!-- doc -->
# Seller Asks Buyer to Pay Outside Byfluence
id: pay-off-platform-payment
type: article
category: payments
subcategory: payment-security
audience: buyer
priority: high
department: trust_safety
features: payments-chapa
tags: pay outside platform, seller asked direct payment, pay seller Telebirr, off-platform payment, discount for direct payment, pay to personal account, ከመድረኩ ውጭ ክፍያ, ሻጩ በቀጥታ ክፈል አለኝ
related: pay-payment-security, tns-report-fraud, pay-fake-payment-screenshots, pay-supported-methods, pay-payment-dispute
templates: tpl-payment-investigation
policy_pending: yes

## Summary
A buyer reports (or asks about) a seller who wants payment outside Byfluence — to a personal phone number, bank account or another app. Protect the buyer, gather evidence, and send the case to Trust & Safety.

## Issue Description
Some sellers ask buyers to pay them directly ("pay me by Telebirr and I'll give you a discount", "the site is down, transfer to my account"). Sometimes a scammer pretends to be a seller. The buyer may ask before paying, or contact support after paying and losing money. Off-platform payments remove Byfluence's ability to verify the payment, confirm the booking/order, handle disputes or refunds, and protect either party. They also avoid marketplace fees, which is a policy concern.

## Possible Causes
- Seller wants to avoid platform fees/commission.
- Seller is a scammer, or the account is compromised.
- An impostor contacted the buyer pretending to be a Byfluence seller.
- A genuine payment problem on Byfluence and the seller "helpfully" offered an alternative.
- Buyer and seller already know each other and agreed to pay directly.

## Information to Collect
- Buyer identity (registered email or phone number)
- Seller name / profile link, listing and booking/order (if any)
- How the request was made (Byfluence messages, phone, Telegram, SMS) and when
- Screenshots of the request (do not ask the buyer to keep chatting with the seller to gather evidence)
- The phone number, account number or username the seller asked them to pay
- Whether the buyer already paid; if so, amount, method, date and reference

> [!WARNING] Never ask the buyer for their PIN, password or verification codes.

## Troubleshooting Steps
1. Thank the buyer and advise them **not** to pay outside Byfluence (or not to pay any more).
2. Determine:
   - **Not paid yet** → advise them to use only the Byfluence checkout; collect evidence; report to Trust & Safety.
   - **Paid off-platform** → explain gently that Byfluence cannot verify or protect payments made outside the platform, but that we will still review the seller's behaviour. Advise them to contact their provider/bank immediately. Escalate to **Trust & Safety**, priority High.
   - **Paid on Byfluence and the seller asks for more money outside** → escalate to **Trust & Safety**; check the Byfluence booking/order is intact.
3. Check whether the "seller" is actually a Byfluence seller (profile, listing). If not, it is an impostor — include that in the escalation.
4. Do **not** contact or warn the seller yourself; Trust & Safety decides the action.
5. If the Byfluence checkout really was failing, check for an incident and help the buyer complete payment properly.
6. Record identifiers and evidence.

- [ ] Buyer advised not to pay outside
- [ ] Payment status (on/off platform) established
- [ ] Evidence and identifiers collected
- [ ] Escalated to Trust & Safety

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know — this is very helpful.

For your protection, please only pay through the Byfluence checkout page. Payments made directly to a seller's phone number, bank account or another app are outside Byfluence, so we cannot verify them, confirm your booking or order, or help with a refund or dispute.

Could you please send us:
1. The seller's name or profile, and the listing
2. Screenshots of the message asking you to pay outside Byfluence
3. The phone number or account you were asked to pay
4. Whether you have already paid, and if so the amount, date and transaction reference

Our Trust & Safety team will review this. Please do not share your PIN, password or any verification code with anyone.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን — ይህ በጣም ይረዳናል።

ለጥበቃዎ ሲባል እባክዎ ክፍያ የሚፈጽሙት በ Byfluence የክፍያ ገጽ ብቻ ይሁን። በቀጥታ ወደ ሻጭ ስልክ ቁጥር፣ የባንክ ሂሳብ ወይም ሌላ መተግበሪያ የሚደረጉ ክፍያዎች ከ Byfluence ውጭ ስለሆኑ ልናረጋግጣቸው፣ ቀጠሮዎን ወይም ትዕዛዝዎን ልናረጋግጥ፣ ወይም በተመላሽ ገንዘብ ወይም በክርክር ልንረዳዎ አንችልም።

እባክዎ የሚከተሉትን ይላኩልን፦
1. የሻጩን ስም ወይም ፕሮፋይል እና ዝርዝሩን (listing)
2. ከ Byfluence ውጭ እንዲከፍሉ የጠየቀዎትን መልዕክት ስክሪንሾት
3. እንዲከፍሉ የተነገረዎትን ስልክ ቁጥር ወይም ሂሳብ
4. አስቀድመው ከፍለው እንደሆነ፣ ከሆነም መጠኑን፣ ቀኑን እና የግብይት ቁጥሩን

የእምነት እና ደህንነት ቡድናችን ይህን ይገመግማል። እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ ለማንም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for telling us! Please pay only through Byfluence checkout — we can't protect payments made directly to a seller. Please send the seller's name, screenshots, the number/account they gave, and whether you already paid. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን! እባክዎ በ Byfluence የክፍያ ገጽ ብቻ ይክፈሉ — በቀጥታ ለሻጭ የሚደረግ ክፍያን መጠበቅ አንችልም። የሻጩን ስም፣ ስክሪንሾቶች፣ የሰጠዎትን ቁጥር/ሂሳብ እና ከፍለው እንደሆነ ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our Trust & Safety team is reviewing your report. For privacy reasons we may not be able to share the actions taken on another account, but your report is being handled. We will contact you again by {{follow_up_time}} if we need anything else.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የእምነት እና ደህንነት ቡድናችን ሪፖርትዎን እየገመገመ ነው። በግላዊነት ምክንያት በሌላ መለያ ላይ የተወሰደውን እርምጃ ላናጋራ እንችላለን፤ ሆኖም ሪፖርትዎ እየተስተናገደ ነው። ተጨማሪ ነገር ካስፈለገን እስከ {{follow_up_time}} ድረስ እናገኝዎታለን።

## Escalation Conditions
- Every confirmed off-platform payment request by a Byfluence seller → **Trust & Safety**, priority High.
- Buyer already lost money → **Trust & Safety**, priority High (Critical if large amount or several victims).
- Impostor using a seller's name or the Byfluence brand → **Trust & Safety**.
- Repeat behaviour by the same seller → **Trust & Safety** and **Seller Operations**.

## Resolution Procedure
1. Confirm the buyer has the safety advice and, if they paid on Byfluence, that their booking/order is intact.
2. Trust & Safety records the outcome; support informs the buyer only of what may be shared.
3. Record identifiers and evidence; resolve after Trust & Safety acknowledges the report.

## Policy Pending Approval
- Confirm the official marketplace rule on off-platform payments and the sanctions for sellers.
- Decide whether Byfluence offers any help or compensation to buyers who paid off-platform (none may be promised).
- Decide whether buyers who agree to off-platform payment face any consequence.

## Internal Notes
- Do not lecture a buyer who already paid; they are a victim and a valuable witness.
- Off-platform requests often appear right after a "payment failed" — check for an incident before assuming bad intent.
- Never share another user's account status or sanctions with the reporter.

<!-- doc -->
# Master Guide: All Payment Problems
id: pay-tsg-payment-master
type: troubleshooting
category: payments
subcategory: failed-pending
audience: both
priority: high
department: payments
features: payments-chapa, payments-telebirr, payments-mpesa, payments-bank, payments-card
tags: payment problem, payment issue, payment help, money deducted, payment master guide, payment decision tree, የክፍያ ችግር, ገንዘብ ተቆርጧል, ክፍያ
related: pay-payment-verification, pay-failed-transaction, pay-pending-transaction, pay-paid-booking-not-confirmed, pay-duplicate-charge, pay-payment-dispute
templates: tpl-request-transaction-ref, tpl-payment-investigation, tpl-payment-failed-guidance, tpl-payment-pending-explain, tpl-payment-not-found
policy_pending: yes

## Summary
A decision tree for any payment complaint: start from the customer's symptom, run the common first checks, then jump to the right article, template and department.

## Overview
Use this guide when a customer describes a payment problem and you are not yet sure which article applies. Work top to bottom. Every path depends on the same foundation: **identify the customer, get the transaction reference, verify in records** (see *How Support Verifies a Payment*).

> [!WARNING] Universal rules for every payment ticket:
> - Never mark or describe a payment as successful without verifying the transaction reference in records. Screenshots alone are not proof.
> - Never promise a refund, a refund date, or any timeline.
> - Never ask for PINs, OTPs, passwords, full card numbers or CVV.
> - Check Feature Status before naming any payment method as available.

## Troubleshooting Steps

### Step 1 — First checks (every case)
- [ ] Confirm identity with the registered email or phone number.
- [ ] Ask what they were paying for (booking/order, seller, date/time).
- [ ] Ask for payment method, date/time, amount and the transaction reference (`tpl-request-transaction-ref`).
- [ ] Ask: "Was money deducted from your account?"
- [ ] Check Feature Status for the method used.
- [ ] Check Announcements / recent tickets for an ongoing payment incident.
- [ ] If a consultation is soon, raise priority now.

### Step 2 — Identify the symptom
| Customer says | Go to |
|---|---|
| "Which methods can I use?" / "Can I pay with Telebirr / card / from abroad?" | *Supported Payment Methods* and the method article |
| "Payment failed / declined / error" | Step 3A |
| "It says pending / processing" | Step 3B |
| "I paid but my booking is not confirmed" | Step 3C |
| "I paid but my order isn't there / no download" | Step 3C |
| "I was charged twice" | Step 3D |
| "I was charged the wrong amount / extra fees" | Step 3E |
| "I want my money back / the seller didn't deliver" | Step 3F |
| "My bank reversed it / I'll do a chargeback" | Step 3F |
| "Where is my refund?" | Step 3G |
| "Someone asked for my PIN / I got a strange call or link" | Step 3H |
| "The seller wants me to pay him directly" | Step 3H |
| "I can't find my reference" | *Helping Customers Find Their Transaction Reference* |
| Seller asks "did my buyer pay?" / about earnings | *Master Guide: Seller Earnings & Payout Problems* |

### Step 3A — Payment failed
1. Was money deducted?
   - **No** → confirm no successful payment exists; guide one safe retry or another live method (*Payment Failed*, `tpl-payment-failed-guidance`).
   - **Yes** → search the reference: Successful → 3C; Pending → 3B; Failed/not found → explain provider hold, no Byfluence charge (`tpl-payment-not-found` if not found).
2. Many failures with the same method → **Technical / Engineering** + supervisor.

### Step 3B — Pending
1. Locate the pending record; check the provider result if you have access.
2. Provider Successful → **Payments & Finance** to confirm. Provider Failed → 3A. Still processing → explain (`tpl-payment-pending-explain`) and set a follow-up.
3. Tell the customer not to pay again.
4. Session soon → Critical.

### Step 3C — Paid but not confirmed
1. Verify the reference.
2. Consultation → *Paid but Booking Not Confirmed* (`pay-paid-booking-not-confirmed`). Product → *Paid but Product Order Not Confirmed*.
3. Verified → **Payments & Finance** confirms; then `tpl-payment-verified-booking-confirmed`.
4. Not found → re-ask reference once, then **Payments & Finance**.
5. Signs of editing/reuse → *Suspected Fake or Edited Payment Screenshots* (**Trust & Safety**).

### Step 3D — Charged twice
1. Get both references; check each status.
2. Two Successful for one booking/order → **Payments & Finance** (`tpl-duplicate-charge-ack`).
3. One Successful + one hold → explain the hold is handled by the provider.
4. Two bookings/orders → ask whether both were intended.

### Step 3E — Wrong amount / fees
1. Compare listing price, checkout total, Byfluence record, statement amount.
2. Statement higher only → bank/provider charges or currency (*Currency, Extra Fees*).
3. Byfluence record wrong → **Payments & Finance** (*Charged a Different Amount*).

### Step 3F — Disputes and reversals
1. Unauthorized → `tns-unauthorized-transaction`, **Trust & Safety**, Critical.
2. Not delivered / not as described / wants money back → *Payment Dispute*; refund requests also via `ref-how-to-request-refund`.
3. Bank reversal or chargeback → *Chargeback or Bank Reversal Request*, **Payments & Finance**.

### Step 3G — Refund status
1. Not yet approved → say it is under review (`ref-refund-status`).
2. Approved → *How Refunds Are Processed* (`tpl-refund-status-update`); no timelines.
3. Marked Refunded but not received → `ref-refund-delay`, **Payments & Finance**.

### Step 3H — Security and off-platform
1. PIN/OTP/password shared or scam contact → *Payment Security* (**Trust & Safety**; Critical if anything was shared).
2. Seller/“agent” wants direct payment → *Seller Asks Buyer to Pay Outside Byfluence* (**Trust & Safety**).

### Step 4 — Before you close
- [ ] Verification result recorded in standard format (`VERIFIED` / `NOT VERIFIED: reason`).
- [ ] Booking/order final status checked.
- [ ] No duplicate refund or chargeback in parallel.
- [ ] Customer received a message with `{{ticket_id}}`.
- [ ] Root cause tagged (provider delay, callback failure, customer error, duplicate, fraud, incident).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry you are having trouble with your payment. I'm here to help.

So I can check it quickly, please send me:
1. What you were paying for (the consultation or product, and the seller)
2. The payment method, date and time
3. The transaction reference from your receipt or SMS
4. Whether money was deducted from your account

Please do not pay again until we have checked, and never share your PIN, password or any verification code — Byfluence will never ask for them.

Your case number is {{ticket_id}}. I will update you as soon as I have checked.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ በክፍያዎ ላይ ችግር ስለገጠመዎት ይቅርታ እንጠይቃለን። ልረዳዎ ዝግጁ ነኝ።

በፍጥነት ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የከፈሉበትን (ምክክሩን ወይም ምርቱን እና ሻጩን)
2. የክፍያ መንገዱን፣ ቀኑን እና ሰዓቱን
3. ከደረሰኝዎ ወይም ከኤስኤምኤሱ ላይ ያለውን የግብይት መለያ ቁጥር
4. ከሂሳብዎ ገንዘብ ተቀንሶ እንደሆነ

እስክናጣራ ድረስ እባክዎ በድጋሚ አይክፈሉ፤ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ በፍጹም አያጋሩ — Byfluence አይጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። እንዳጣራሁ ወዲያውኑ መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about the payment trouble! Please send what you paid for, the method, time, transaction reference, and whether money was deducted. Please don't pay again until we check. Never share your PIN or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ ክፍያ ችግሩ ይቅርታ! እባክዎ የከፈሉበትን፣ የክፍያ መንገዱን፣ ሰዓቱን፣ የግብይት ቁጥሩን እና ገንዘብ ተቀንሶ እንደሆነ ይላኩ። እስክናጣራ በድጋሚ አይክፈሉ። ፒን ወይም ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Verified payment that support cannot apply to a booking/order; duplicates; wrong amounts; refunds; reversals → **Payments & Finance**.
- Fraud signals, edited screenshots, PIN/OTP disclosure, off-platform payment, unauthorized payment → **Trust & Safety**.
- Checkout errors or many simultaneous failures/pending payments → **Technical / Engineering** + supervisor.
- Buyer–seller dispute decisions → **Senior Support / Supervisor**.
- No access to payment records → **Senior Support / Supervisor**.
- Legal threats, high-value or reputational cases → **Management**.

## Policy Pending Approval
- Confirm which payment methods are live and keep Feature Status current.
- Approve customer wording for verification times, pending expiry, and refund timing.
- Define internal escalation thresholds (how long pending before escalation; value thresholds for second verification).
- Define refund eligibility and approval authority.

## Internal Notes
- Most payment tickets resolve to one of four root causes: customer did not finish approval, provider callback delay, duplicate attempt, or wrong reference supplied. Check those first.
- A sudden spike in any one symptom is an incident until proven otherwise — tell the supervisor early.
- Keep your tone calm and specific; customers worried about money calm down when they see a clear next step and a case number.
