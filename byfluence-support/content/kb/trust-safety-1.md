<!-- doc -->
# Customer Reports Fraud
id: tns-report-fraud
type: article
category: trust-safety
subcategory: fraud
audience: both
priority: critical
department: trust_safety
tags: fraud, scam, scammed, cheated, fake seller, stolen money, report scam, ማጭበርበር, ተጭበረበርኩ, አታለሉኝ
related: tns-tsg-fraud-triage, tns-suspicious-seller, tns-off-platform-payment-request, tns-unauthorized-transaction, ref-abuse-of-refunds, pay-off-platform-payment
templates: tpl-acknowledge-complaint, tpl-request-screenshot, tpl-escalation-notification
policy_pending: yes

## Summary
A buyer or seller says they have been defrauded — money taken, goods or services never delivered by a fake account, or a scam carried out using Byfluence's name. Act fast to protect the customer and preserve evidence, and route to Trust & Safety.

## Issue Description
Fraud reports are among the most serious contacts support receives. The customer may be panicked, embarrassed or angry, and may have lost money that matters a great deal to them. Speed matters: acting quickly can stop more victims, keep a seller's funds pending, or freeze a compromised account. Support agents **do not investigate or punish** — they calm, protect, preserve evidence and escalate to **Trust & Safety** with priority **Critical** when money is at risk or the fraud is ongoing.

## Possible Causes
- Fake seller listing, taking payment for consultations/products that never exist
- Seller asked the buyer to pay outside Byfluence (bank transfer, mobile money, cash) and disappeared
- Account takeover: someone used the customer's account to buy or withdraw
- Someone impersonating Byfluence staff asked for codes, PINs or payments (see `tns-impersonation-of-byfluence`)
- Fake payment confirmation shown to a seller (edited screenshot) to obtain goods/services
- Phishing links sent through messages pretending to be Byfluence or a payment provider
- Buyer–seller dispute that the customer describes as fraud (still treat seriously; may turn out to be a dispute)

## Information to Collect
- Reporter's name and registered email/phone (confirm they are the account holder)
- What happened, step by step, with dates and times
- The other party: seller/buyer name or profile link, listing link, any usernames — only what the reporter already has
- Order/booking ID and transaction reference, amount, payment method
- Whether the payment was made **through Byfluence** or **outside Byfluence** (bank transfer, mobile money, cash)
- Screenshots of messages, listings, payment receipts, links received
- Whether the reporter shared any password, OTP or PIN with anyone (do not ask for the code itself)
- Whether the reporter has already contacted their bank/provider or the police

> [!WARNING] Never ask for passwords, OTP codes, PINs, mobile-money PINs or card numbers. If the customer has shared these with someone, tell them to change their password and contact their bank or mobile-money provider immediately.

## Troubleshooting Steps
1. **Calm and protect.** Thank them for reporting. If they shared a password/OTP/PIN, tell them now: change the Byfluence password, contact their bank/provider to block or secure the account.
2. **Check for ongoing risk** (`tns-tsg-fraud-triage`):
   - Money still moving, account still compromised, more victims likely → priority **Critical**.
   - Customer's personal safety threatened → `tns-threats-safety` first.
3. **Identify the payment path:**
   - **Paid through Byfluence** → locate the transaction; ask **Payments & Finance** to keep related seller earnings pending (they decide).
   - **Paid outside Byfluence** → explain gently that Byfluence cannot see or reverse off-platform payments, but the report is still important; advise contacting their bank/provider and the police. Still escalate (the account may be scamming others).
4. **Preserve evidence.** Screenshot the listing/profile now (it may be deleted). Attach all customer screenshots in original form.
5. **Escalate to Trust & Safety** with a clear summary: who, what, when, how paid, amount, evidence, ongoing risk.
6. **Do not** contact the alleged fraudster yourself, warn them, or reveal the reporter's identity.
7. Give the customer the case number and a follow-up time. Explain what Byfluence can and cannot do.

- [ ] Customer advised to secure accounts (if credentials shared)
- [ ] Risk level set
- [ ] Payment path identified
- [ ] Evidence preserved (listing captured)
- [ ] Escalated to Trust & Safety
- [ ] Reporter identity protected

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for reporting this to Byfluence Support. I'm very sorry this happened, and I understand how upsetting it is. Your report is important and is being treated as urgent.

To help our Trust & Safety team, please send me:
1. A short description of what happened, with dates
2. The seller or account name and the listing link, if you have it
3. Screenshots of messages, payment receipts or any links you received
4. Whether you paid through Byfluence or outside Byfluence (for example by bank transfer or mobile money)

If you have shared your password, PIN or any verification code with anyone, please change your Byfluence password now and contact your bank or mobile-money provider immediately. We will never ask you for these.

Your case number is {{ticket_id}}. We will keep your identity confidential and update you as soon as possible.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ይህንን ለByfluence ድጋፍ ስላሳወቁን እናመሰግናለን። ይህ በመድረሱ በጣም እናዝናለን፤ ምን ያህል እንደሚያስጨንቅ እረዳለሁ። ሪፖርትዎ አስፈላጊ ሲሆን በአስቸኳይ እየተስተናገደ ነው።

የእምነትና ደህንነት (Trust & Safety) ቡድናችንን ለመርዳት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የተፈጠረውን ሁኔታ ከቀናት ጋር በአጭሩ
2. ካለዎት የሻጩን ወይም የመለያውን ስም እና የዝርዝሩን (listing) ሊንክ
3. የመልዕክቶች፣ የክፍያ ደረሰኞች ወይም የደረሱዎት ሊንኮች ስክሪንሾቶች
4. ክፍያውን በByfluence በኩል ወይም ከByfluence ውጭ (ለምሳሌ በባንክ ዝውውር ወይም በሞባይል ገንዘብ) እንደፈጸሙ

የይለፍ ቃልዎን፣ ፒንዎን ወይም ማንኛውንም የማረጋገጫ ኮድ ለማንም አጋርተው ከሆነ፣ እባክዎ አሁኑኑ የByfluence የይለፍ ቃልዎን ይቀይሩ፤ ባንክዎን ወይም የሞባይል ገንዘብ አቅራቢዎን ወዲያውኑ ያነጋግሩ። እኛ እነዚህን በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ማንነትዎን በሚስጥር እንጠብቃለን፤ በተቻለ ፍጥነት መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I'm very sorry. We're treating this as urgent. Please send what happened, the seller/account name or link, screenshots, and whether you paid through Byfluence or outside it. Never share your password/PIN/codes; if you already did, change your password and call your bank now. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በጣም እናዝናለን። ጉዳዩን በአስቸኳይ እያየነው ነው። እባክዎ የተፈጠረውን፣ የሻጩን/የመለያውን ስም ወይም ሊንክ፣ ስክሪንሾቶች እና በByfluence ወይም ከውጭ እንደከፈሉ ይላኩ። የይለፍ ቃል/ፒን/ኮድ አጋርተው ከሆነ አሁኑኑ ይቀይሩ፤ ባንክዎንም ያነጋግሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our Trust & Safety team is reviewing your report. For security reasons we may not be able to share every action we take regarding other accounts, but your report is being acted on. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የእምነትና ደህንነት ቡድናችን ሪፖርትዎን እየገመገመ ነው። ለደህንነት ሲባል በሌሎች መለያዎች ላይ የምንወስዳቸውን እርምጃዎች ሁሉ ልናካፍልዎ ላንችል እንችላለን፤ ሆኖም ሪፖርትዎ ላይ እርምጃ እየተወሰደ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every fraud report → **Trust & Safety**; priority **Critical** if money is still at risk, the account is compromised, or the fraud is ongoing.
- Payment through Byfluence involved → also **Payments & Finance** (holds/reversals are their decision).
- Customer's account compromised → follow `tns-account-compromise` in parallel.
- Many victims, a fake Byfluence website/page, or media attention → **Management** via Trust & Safety.
- Physical safety threatened → `tns-threats-safety` immediately.

## Resolution Procedure
1. Trust & Safety acknowledges and takes ownership.
2. The customer receives the outcome that can be shared (e.g., "we have taken action on the account", refund decision via the normal refund process).
3. Record fraud type, payment path, amount, accounts involved and actions taken.

## Policy Pending Approval
- Decide whether Byfluence will compensate victims of on-platform fraud and under what conditions.
- Decide what Byfluence tells reporters about actions taken against reported accounts.
- Approve the process for referring customers to police and what documents Byfluence can provide (via Management).
- Approve the official list of safety contacts agents may share.

## Internal Notes
- Never say "this is not our responsibility" even for off-platform payments. Say what we can and cannot do.
- Victims often feel ashamed. Avoid "why did you pay outside?" — focus on next steps.
- Do not disclose the reporter's identity to the reported account, including indirectly ("a buyer from yesterday's session reported you").
- Fraud reports about the same seller from different customers should be linked immediately.

<!-- doc -->
# Report of a Suspicious Seller
id: tns-suspicious-seller
type: article
category: trust-safety
subcategory: fraud
audience: buyer
priority: high
department: trust_safety
features: seller-verification
tags: suspicious seller, fake seller, is this seller real, scam seller, unverified seller, seller looks fake, አጠራጣሪ ሻጭ, ሐሰተኛ ሻጭ
related: tns-report-fraud, tns-off-platform-payment-request, tns-fake-products, tns-misleading-descriptions, tns-identity-verification-concerns
templates: tpl-acknowledge-complaint, tpl-request-screenshot
policy_pending: yes

## Summary
A buyer (or another seller) reports that a seller looks suspicious — before or after buying. The agent records the concern, protects the reporter, gives safe-buying advice, and routes to Trust & Safety.

## Issue Description
Buyers may notice warning signs: prices far below market, copied photos, a profile with no details, pressure to pay outside Byfluence, requests for personal information, or a seller claiming credentials that look fake. Early reports are valuable because they can stop fraud before money is lost. Sellers have verification statuses (**Pending, Verified, Rejected**) and operational statuses (**Active, Suspended, Banned**); these are separate, and a Verified seller can still behave suspiciously.

## Possible Causes
- Fake or stolen identity used in seller verification (see `tns-identity-verification-concerns`)
- Copied listings, photos or credentials from another seller or website
- Seller pushing buyers to pay or communicate off-platform
- Unrealistic prices or promises (guaranteed income, miracle results)
- Compromised genuine seller account used by a fraudster
- A legitimate new seller with an incomplete profile (not every report is fraud)

## Information to Collect
- Seller name / profile link and the listing link(s)
- What made the reporter suspicious (specific signs)
- Screenshots of messages, listings or anything the seller sent
- Whether the reporter has paid anything, and how (through Byfluence or outside)
- Whether the reporter shared personal information with the seller

> [!WARNING] Never ask for passwords, OTP codes or PINs. Do not share any information about the seller's verification documents, identity or other complaints with the reporter.

## Troubleshooting Steps
1. Thank the reporter; reassure them that the report is confidential.
2. If they already paid or were asked to pay off-platform → follow `tns-report-fraud` / `tns-off-platform-payment-request`.
3. Capture the seller profile and listing(s) as they are now (screenshots to the ticket).
4. Check, through authorized tools, the seller's verification and operational status — **for your escalation note only**. Do not disclose it to the reporter.
5. Check for other reports about the same seller and link them.
6. Escalate to **Trust & Safety** (and **Seller Operations** if it is a listing quality issue rather than fraud).
7. Give safe-buying advice: pay only through Byfluence, keep all communication on Byfluence, never share codes or PINs.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know about your concerns with this seller. Reports like yours help keep Byfluence safe for everyone, and your report will be kept confidential.

To help our Trust & Safety team review it, please send:
1. The seller's name or profile link and the listing link
2. What made you concerned
3. Any screenshots of messages or listings

For your safety, please make all payments only through Byfluence, keep your communication on Byfluence, and never share your password, PIN or verification codes with anyone.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለዚህ ሻጭ ያለዎትን ስጋት ስላሳወቁን እናመሰግናለን። እንደ እርስዎ ያሉ ሪፖርቶች Byfluenceን ለሁሉም ደህንነቱ የተጠበቀ ለማድረግ ይረዳሉ፤ ሪፖርትዎ በሚስጥር ይያዛል።

የእምነትና ደህንነት ቡድናችን እንዲገመግመው እባክዎ የሚከተሉትን ይላኩ፦
1. የሻጩን ስም ወይም የመገለጫ ሊንክ እና የዝርዝሩን (listing) ሊንክ
2. ስጋት ያሳደረብዎትን ነገር
3. የመልዕክቶች ወይም የዝርዝሮች ስክሪንሾቶች ካሉ

ለደህንነትዎ ሲባል እባክዎ ማንኛውንም ክፍያ በByfluence በኩል ብቻ ይፈጽሙ፣ ግንኙነትዎን በByfluence ላይ ያድርጉ፣ የይለፍ ቃልዎን፣ ፒንዎን ወይም የማረጋገጫ ኮዶችን ለማንም በፍጹም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thank you — your report is confidential. Please send the seller/listing link, what concerned you, and any screenshots. Only pay through Byfluence and never share codes or PINs. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እናመሰግናለን — ሪፖርትዎ በሚስጥር ይያዛል። እባክዎ የሻጩን/የዝርዝሩን ሊንክ፣ ያሳሰበዎትን እና ስክሪንሾቶች ይላኩ። በByfluence ብቻ ይክፈሉ፤ ኮድ ወይም ፒን በፍጹም አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, thank you again for your report (case {{ticket_id}}). Our Trust & Safety team has reviewed it and taken appropriate steps. For privacy reasons we cannot share details about other accounts. If you notice anything else, please contact us again.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ሪፖርትዎ (የጉዳይ ቁጥር {{ticket_id}}) በድጋሚ እናመሰግናለን። የእምነትና ደህንነት ቡድናችን ገምግሞ ተገቢውን እርምጃ ወስዷል። በግላዊነት ምክንያት ስለ ሌሎች መለያዎች ዝርዝር ማካፈል አንችልም። ሌላ ነገር ካስተዋሉ እባክዎ በድጋሚ ያግኙን።

## Escalation Conditions
- Suspected fraud or fake identity → **Trust & Safety**.
- Listing quality/misleading content without fraud signs → **Seller Operations**.
- Reporter has already lost money → `tns-report-fraud`, priority Critical if ongoing.
- Multiple reports about the same seller → **Trust & Safety**, priority High, link all tickets.

## Resolution Procedure
1. Trust & Safety records its assessment and any action.
2. Send the reporter the closing follow-up (no details about the seller).
3. Record the report type and linked tickets.

## Policy Pending Approval
- Decide the criteria for suspending a seller pending investigation.
- Decide what Byfluence tells reporters about the outcome.
- Decide whether verified sellers display a public badge buyers can check.

## Internal Notes
- Never tell the reporter "this seller is verified, so it's safe" — verification is not a guarantee of behaviour.
- Never tell the seller who reported them.
- A new seller with a thin profile is not automatically suspicious. Report facts, not impressions.

<!-- doc -->
# Seller Asked for Payment Outside Byfluence
id: tns-off-platform-payment-request
type: article
category: trust-safety
subcategory: fraud
audience: both
priority: high
department: trust_safety
tags: pay outside, off-platform payment, seller asked bank transfer, pay directly, telebirr directly, avoid fees, ውጭ ክፈል, በቀጥታ ክፈል, ከByfluence ውጭ ክፍያ
related: pay-off-platform-payment, tns-report-fraud, tns-suspicious-seller, tns-policy-violations, ref-consultation-refunds
templates: tpl-acknowledge-complaint, tpl-request-screenshot
policy_pending: yes

## Summary
A buyer reports that a seller asked them to pay directly (bank transfer, mobile money, cash) instead of through Byfluence — or a buyer has already paid off-platform and now has a problem.

## Issue Description
Paying outside Byfluence removes every protection the marketplace provides: there is no transaction record, no confirmed booking, no dispute process and no way for Byfluence to see or reverse the payment. It is also the most common setup for scams. Sellers may ask for off-platform payment to avoid fees, for "convenience", or to defraud. Whatever the reason, buyers should be advised to pay only through Byfluence. Whether off-platform payment requests are a formal marketplace violation and what action follows is **not yet a published rule** — Trust & Safety decides.

## Possible Causes
- Seller wants to avoid platform commissions/fees
- Seller is a fraudster who will disappear after payment
- Seller says "the Byfluence payment isn't working" (check for real payment incidents first)
- Buyer asked the seller to pay directly (it happens; note it neutrally)
- Someone impersonating the seller contacted the buyer outside Byfluence

## Information to Collect
- Seller name / profile, listing link, order/booking ID if any
- Screenshot of the message requesting off-platform payment (and where: Byfluence messages, Telegram, phone, SMS)
- Has the buyer already paid? If yes: amount, method, date, recipient name/number **as shown on their receipt** (for Trust & Safety only)
- Whether the buyer received anything

> [!WARNING] Never ask for passwords, OTP codes or PINs. Do not tell the buyer to "go ahead and pay" outside Byfluence under any circumstances.

## Troubleshooting Steps
1. Check Announcements and payment status for a real payment outage. If payments are failing, tell the buyer to wait for the fix rather than pay outside.
2. **Not yet paid** → advise the buyer not to pay outside Byfluence; record the report; escalate to **Trust & Safety**.
3. **Already paid outside** → explain kindly that Byfluence cannot see or reverse that payment; advise them to contact their bank/provider and, if they believe it was a scam, the police. Escalate to **Trust & Safety** (follow `tns-report-fraud` if they lost money).
4. **Paid through Byfluence and then asked to pay "extra" outside** → escalate to Trust & Safety; the original booking/order remains protected by normal support processes.
5. Capture the seller profile/listing and attach the screenshots.
6. Do not contact the seller yourself. Do not reveal the reporter's identity.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for telling us about this. For your protection, please make payments only through Byfluence. When you pay outside Byfluence, we have no record of the payment and cannot help if something goes wrong.

Please send me a screenshot of the message asking you to pay outside, and the seller's name or listing link. Our Trust & Safety team will review it, and your report will be kept confidential.

If you have already paid outside Byfluence, please tell me the amount and the date, and contact your bank or mobile-money provider as soon as possible. Never share your PIN or verification codes with anyone.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ይህንን ስላሳወቁን እናመሰግናለን። ለጥበቃዎ ሲባል እባክዎ ክፍያዎችን በByfluence በኩል ብቻ ይፈጽሙ። ከByfluence ውጭ ሲከፍሉ የክፍያው መዝገብ በእኛ ዘንድ ስለማይኖር ችግር ቢፈጠር ልንረዳዎ አንችልም።

እባክዎ ከByfluence ውጭ እንዲከፍሉ የተጠየቁበትን መልዕክት ስክሪንሾት እና የሻጩን ስም ወይም የዝርዝሩን ሊንክ ይላኩልኝ። የእምነትና ደህንነት ቡድናችን ይገመግመዋል፤ ሪፖርትዎም በሚስጥር ይያዛል።

አስቀድመው ከByfluence ውጭ ከፍለው ከሆነ፣ እባክዎ መጠኑን እና ቀኑን ይንገሩኝ፤ ባንክዎን ወይም የሞባይል ገንዘብ አቅራቢዎን በተቻለ ፍጥነት ያነጋግሩ። ፒንዎን ወይም የማረጋገጫ ኮዶችን ለማንም በፍጹም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for telling us. Please pay only through Byfluence — we can't protect payments made outside. Send a screenshot of the request and the seller/listing link; your report is confidential. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን። እባክዎ በByfluence በኩል ብቻ ይክፈሉ — ከውጭ የተፈጸመ ክፍያን መጠበቅ አንችልም። የጥያቄውን ስክሪንሾት እና የሻጩን/የዝርዝሩን ሊንክ ይላኩ፤ ሪፖርትዎ በሚስጥር ይያዛል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, update on case {{ticket_id}}: our Trust & Safety team has reviewed your report and taken appropriate steps. For privacy reasons we can't share details about other accounts. Thank you for helping keep Byfluence safe.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}}፦ የእምነትና ደህንነት ቡድናችን ሪፖርትዎን ገምግሞ ተገቢውን እርምጃ ወስዷል። በግላዊነት ምክንያት ስለ ሌሎች መለያዎች ዝርዝር ማካፈል አንችልም። Byfluenceን ደህንነቱ የተጠበቀ ለማድረግ ስለረዱን እናመሰግናለን።

## Escalation Conditions
- Every off-platform payment request report → **Trust & Safety**.
- Buyer already lost money → **Trust & Safety**, priority High/Critical (`tns-report-fraud`).
- Seller claims Byfluence payments don't work and there is a real outage → **Technical / Engineering** and **Payments & Finance**.
- Pattern across multiple buyers → **Trust & Safety**, Critical.

## Resolution Procedure
1. Trust & Safety records action taken on the seller account.
2. Reporter receives the closing follow-up.
3. Record whether money was lost, the amount and method.

## Policy Pending Approval
- Confirm whether requesting off-platform payment is a marketplace violation and the actions that follow (warning, suspension, ban).
- Decide whether Byfluence helps victims of off-platform payments in any way (e.g., documentation for police).
- Approve the public "pay only through Byfluence" safety message.

## Internal Notes
- Never blame the buyer for paying outside. Focus on what to do now.
- Sellers who send their personal Telegram or phone number in listings or messages to move buyers off-platform should be reported even if no payment is requested.
- If the buyer says the "seller" contacted them only by phone/Telegram and never on Byfluence, it may be an impersonator — say so in the escalation.

<!-- doc -->
# Unauthorized Transaction on Customer's Account
id: tns-unauthorized-transaction
type: article
category: trust-safety
subcategory: fraud
audience: buyer
priority: critical
department: payments
features: payments-chapa
tags: unauthorized transaction, i didn't make this payment, unknown charge, someone used my account, stolen card, fraud charge, ያልፈጸምኩት ክፍያ, ያልታወቀ ክፍያ, አካውንቴ ተጠቅመዋል
related: tns-account-compromise, acc-unauthorized-access, pay-duplicate-charge, pay-chargeback, tns-report-fraud, ref-refund-to-different-account
templates: tpl-account-compromise-urgent, tpl-escalation-notification, tpl-request-screenshot
policy_pending: yes

## Summary
A customer reports a payment, booking, order or withdrawal on their Byfluence account that they did not make, or a charge from Byfluence on their bank/mobile-money account that they do not recognise. Treat as Critical: secure the account, stop further loss, and escalate to Payments & Finance and Trust & Safety together.

## Issue Description
An unauthorized transaction may mean someone has access to the customer's Byfluence account, their payment method, or both. It may also be a misunderstanding (a family member used the account, a duplicate charge, a provider hold). Agents must act quickly without assuming either way. For sellers, an unauthorized **withdrawal** request or changed payout details is especially urgent — see `tns-account-compromise`.

## Possible Causes
- Account takeover (password reused, phishing, shared OTP) — someone else logged in and paid
- Stolen or misused payment method (card or mobile-money account used by someone else)
- Family member or colleague used the customer's account or phone
- Duplicate charge or provider hold that looks like an unknown payment (see `pay-duplicate-charge`)
- The charge is from another merchant, not Byfluence
- Seller account: payout details changed and withdrawal requested by an attacker

## Information to Collect
- Customer name and registered email/phone (confirm identity carefully)
- Which transaction(s) they do not recognise: date, amount, reference as shown on their statement/SMS
- Whether they can still log in; any recent password reset emails, unknown login alerts, or OTP messages they did not request
- Whether they shared any code, password or PIN with anyone
- Whether anyone else has access to their phone or account
- Whether they have contacted their bank/provider

> [!WARNING] Never ask for passwords, OTP codes, PINs, mobile-money PINs, full card numbers or CVV. If they mention a code they received, tell them not to share it with anyone — including you.

## Troubleshooting Steps
1. **Secure first.** Ask the customer to change their Byfluence password immediately (if they can log in) and to contact their bank/mobile-money provider to block or secure the payment method.
2. **Confirm the transaction is on Byfluence.** Search by reference/amount/time in the admin dashboard.
   - Not found → it may be another merchant; advise contacting the provider; still note the case.
   - Found on the customer's account → continue.
3. **Look for takeover signs** (through authorized tools): recent changes to email/phone/password, new devices, unusual bookings/orders, changed payout details (sellers).
4. **Escalate immediately** to **Payments & Finance** (transaction review, holds) **and** **Trust & Safety** (account security), priority **Critical**. Use `tpl-account-compromise-urgent` for the customer.
5. If a booking/order is upcoming and was made by the attacker, ask L2/Payments whether it should be held or cancelled — do not cancel on your own unless your role allows it.
6. If takeover is likely, follow `tns-account-compromise` in parallel.
7. If the customer has filed a chargeback, inform Payments (`pay-chargeback`).
8. Do not promise a refund. Explain that the security and payments teams will review.

- [ ] Customer told to change password and contact provider
- [ ] Transaction located (or confirmed not Byfluence)
- [ ] Takeover signs checked
- [ ] Escalated to Payments & Trust & Safety (Critical)
- [ ] No refund promised

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us right away — that was the right thing to do. I'm sorry you are dealing with this.

Please do these two things now:
1. Change your Byfluence password (if you can still log in).
2. Contact your bank or mobile-money provider to secure your payment method.

Then please send me the date, amount and reference of the transaction you don't recognise, as shown in your SMS or statement. Please do not share your password, PIN or any verification code with anyone, including us.

I have marked your case as urgent and passed it to our payments and security teams. Your case number is {{ticket_id}}. We will update you as soon as possible.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ወዲያውኑ ስላገኙን እናመሰግናለን — ትክክለኛውን ነገር አድርገዋል። ይህ ስላጋጠመዎት ይቅርታ እንጠይቃለን።

እባክዎ እነዚህን ሁለት ነገሮች አሁኑኑ ያድርጉ፦
1. የByfluence የይለፍ ቃልዎን ይቀይሩ (አሁንም መግባት ከቻሉ)።
2. የክፍያ ዘዴዎን ለማስጠበቅ ባንክዎን ወይም የሞባይል ገንዘብ አቅራቢዎን ያነጋግሩ።

ከዚያም እባክዎ የማያውቁትን ግብይት ቀን፣ መጠን እና መለያ ቁጥር (በኤስኤምኤስዎ ወይም በሂሳብ መግለጫዎ ላይ እንደሚታየው) ይላኩልኝ። የይለፍ ቃልዎን፣ ፒንዎን ወይም ማንኛውንም የማረጋገጫ ኮድ ለማንም — ለእኛም ቢሆን — አያጋሩ።

ጉዳይዎን አስቸኳይ ብዬ ምልክት አድርጌ ለክፍያ እና ለደህንነት ቡድኖቻችን አስተላልፌዋለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው። በተቻለ ፍጥነት መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for telling us quickly. Please change your Byfluence password now and contact your bank/mobile-money provider. Then send the date, amount and reference of the unknown transaction. Never share your PIN or codes. Marked urgent. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በፍጥነት ስላሳወቁን እናመሰግናለን። እባክዎ የByfluence የይለፍ ቃልዎን አሁኑኑ ይቀይሩ፤ ባንክዎን/የሞባይል ገንዘብ አቅራቢዎን ያነጋግሩ። ከዚያም የማያውቁትን ግብይት ቀን፣ መጠን እና መለያ ቁጥር ይላኩ። ፒን ወይም ኮድ በፍጹም አያጋሩ። አስቸኳይ ተብሎ ተመዝግቧል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our payments and security teams are reviewing transaction {{transaction_id}} and your account activity. We will contact you again by {{follow_up_time}}. If you notice any other unknown activity, tell us immediately.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ እና የደህንነት ቡድኖቻችን ግብይት {{transaction_id}}ን እና የመለያዎን እንቅስቃሴ እየገመገሙ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ሌላ የማያውቁት እንቅስቃሴ ካዩ ወዲያውኑ ያሳውቁን።

## Escalation Conditions
- Every unauthorized transaction report → **Payments & Finance** and **Trust & Safety**, priority **Critical**.
- Seller payout details changed or withdrawal requested by someone else → **Payments & Finance** (hold) and **Trust & Safety**, Critical.
- Customer cannot log in / contact details changed → `tns-account-compromise`.
- Many customers reporting unknown charges → **Technical / Engineering** + **Management** (possible security incident, `tns-security-incident-report`).

## Resolution Procedure
1. Trust & Safety confirms the account is secured.
2. Payments & Finance records the outcome for each transaction (reversed/refunded, held, or confirmed as legitimate).
3. Communicate the outcome via the registered contact details.
4. Record cause (takeover, payment method misuse, family use, duplicate, not Byfluence) and actions taken.

## Policy Pending Approval
- Decide Byfluence's liability and refund approach for transactions made through a compromised account.
- Decide whether bookings/orders made by an attacker are cancelled automatically.
- Decide the identity re-verification required before restoring a compromised account.

## Internal Notes
- Speed matters most for sellers' withdrawals: a hold request to Payments can prevent the money from leaving.
- Many "unknown charges" turn out to be family members using the same phone. Ask gently, without accusing.
- Do not discuss the case with anyone who is not verified as the account owner, even if they say they are a relative.

<!-- doc -->
# Someone Impersonating Byfluence Staff
id: tns-impersonation-of-byfluence
type: article
category: trust-safety
subcategory: fraud
audience: both
priority: high
department: trust_safety
tags: fake byfluence, impersonation, fake support, someone called from byfluence, phishing, fake telegram account, scam message, የByfluence ሰራተኛ ነኝ ያለ, ሐሰተኛ, አስመሳይ
related: tns-report-fraud, tns-account-compromise, tns-unauthorized-transaction, tns-security-incident-report, tns-tsg-fraud-triage
templates: tpl-acknowledge-complaint, tpl-request-screenshot, tpl-account-compromise-urgent
policy_pending: yes

## Summary
A customer reports a call, message, Telegram account, website or social-media page claiming to be Byfluence — often asking for codes, PINs, payments or "verification fees". Protect the customer, collect details, and escalate to Trust & Safety.

## Issue Description
Scammers pose as marketplace staff to steal accounts and money: "This is Byfluence support, send me the code we just sent you", "Your seller account will be suspended unless you pay a verification fee", "Click this link to receive your payout". Customers with low digital literacy are especially at risk. The key message: **Byfluence staff will never ask for passwords, OTP codes, PINs, or payments outside Byfluence.**

The official support channels, Telegram handle and phone numbers are **not yet confirmed in this knowledge base** — do not quote any contact details except via `{{support_channel}}` as approved.

## Possible Causes
- Fake Telegram account or group using Byfluence's name/logo
- Phone call or SMS claiming to be Byfluence support
- Phishing website that copies Byfluence's login page
- Fake social-media page offering "jobs", "investment" or "zero-investment selling" in Byfluence's name
- A real seller or buyer claiming to be Byfluence staff to pressure someone

## Information to Collect
- How the impersonator made contact (Telegram, phone, SMS, email, website, social media)
- The username, phone number, email address, page name or link used by the impersonator
- Screenshots of the messages or page
- What they asked for, and whether the customer gave anything (code, password, PIN, payment, ID document)
- Date and time of contact

> [!WARNING] Never ask for the code, password or PIN the customer may have shared. Ask only **whether** they shared one.

## Troubleshooting Steps
1. Confirm to the customer clearly: Byfluence staff never ask for passwords, OTP codes, PINs or off-platform payments.
2. Find out whether they gave anything:
   - **Shared a code/password** → ask them to change their Byfluence password immediately; follow `tns-account-compromise`.
   - **Shared a PIN or paid money** → advise contacting their bank/mobile-money provider immediately; follow `tns-report-fraud`.
   - **Shared an ID document** → note it for Trust & Safety (`tns-identity-verification-concerns`).
   - **Gave nothing** → thank them; advise them to block and report the account on the platform where it contacted them.
3. Collect the impersonator's identifiers and screenshots.
4. Escalate to **Trust & Safety**. If it is a fake website or a large-scale campaign, Trust & Safety informs **Management** and **Technical**.
5. Tell the customer to use only official Byfluence channels ({{support_channel}}).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for warning us. Please be assured: Byfluence staff will never ask you for your password, verification codes, PIN, or for any payment outside Byfluence.

To help us stop this, please send:
1. A screenshot of the message, call log or page
2. The username, phone number or link they used
3. Whether you shared any code, password, PIN, money or documents with them

If you shared a password or code, please change your Byfluence password now. If you shared a PIN or sent money, contact your bank or mobile-money provider immediately.

Please contact us only through our official channel: {{support_channel}}. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላስጠነቀቁን እናመሰግናለን። እባክዎ እርግጠኛ ይሁኑ፦ የByfluence ሰራተኞች የይለፍ ቃልዎን፣ የማረጋገጫ ኮዶችን፣ ፒንዎን ወይም ከByfluence ውጭ የሚፈጸም ማንኛውንም ክፍያ በፍጹም አይጠይቁም።

ይህንን ለማስቆም እንዲረዳን እባክዎ የሚከተሉትን ይላኩ፦
1. የመልዕክቱን፣ የጥሪ መዝገቡን ወይም የገጹን ስክሪንሾት
2. የተጠቀሙበትን የተጠቃሚ ስም፣ ስልክ ቁጥር ወይም ሊንክ
3. ማንኛውንም ኮድ፣ የይለፍ ቃል፣ ፒን፣ ገንዘብ ወይም ሰነድ እንደሰጧቸው ወይም እንዳልሰጧቸው

የይለፍ ቃል ወይም ኮድ ሰጥተው ከሆነ፣ እባክዎ የByfluence የይለፍ ቃልዎን አሁኑኑ ይቀይሩ። ፒን ሰጥተው ወይም ገንዘብ ልከው ከሆነ፣ ባንክዎን ወይም የሞባይል ገንዘብ አቅራቢዎን ወዲያውኑ ያነጋግሩ።

እባክዎ እኛን የሚያገኙት በይፋዊ መስመራችን ብቻ ይሁን፦ {{support_channel}}። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thank you for warning us. Byfluence staff never ask for passwords, codes, PINs or payments outside Byfluence. Please send screenshots and the username/number they used, and tell me if you shared anything. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላስጠነቀቁን እናመሰግናለን። የByfluence ሰራተኞች የይለፍ ቃል፣ ኮድ፣ ፒን ወይም ከውጭ ክፍያ በፍጹም አይጠይቁም። እባክዎ ስክሪንሾቶችን እና የተጠቀሙበትን ስም/ቁጥር ይላኩ፤ ምንም ነገር ሰጥተው እንደሆነም ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, thank you again for your report (case {{ticket_id}}). Our Trust & Safety team is acting on it. Please remember that our only official channel is {{support_channel}}, and keep your codes and PINs private.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ሪፖርትዎ (የጉዳይ ቁጥር {{ticket_id}}) በድጋሚ እናመሰግናለን። የእምነትና ደህንነት ቡድናችን እርምጃ እየወሰደ ነው። እባክዎ ይፋዊ መስመራችን {{support_channel}} ብቻ መሆኑን ያስታውሱ፤ ኮዶችዎን እና ፒንዎን በሚስጥር ይያዙ።

## Escalation Conditions
- Every impersonation report → **Trust & Safety**.
- Customer shared credentials → `tns-account-compromise` (Critical).
- Customer lost money → `tns-report-fraud` (Critical if ongoing).
- Fake website/login page, or many reports in a short time → **Trust & Safety** + **Technical / Engineering** + **Management** (possible public warning).
- Impersonator is a registered Byfluence user → **Trust & Safety** (account action).

## Resolution Procedure
1. Customer's account secured (if needed) and advised on bank/provider steps.
2. Impersonator details logged with Trust & Safety.
3. Record channel used, what was requested, and whether loss occurred.

## Policy Pending Approval
- Publish the official list of Byfluence support channels, handles and numbers so agents and customers can verify them.
- Decide the process for reporting fake pages/accounts to Telegram, social networks and hosting providers.
- Decide when Byfluence issues a public warning about an impersonation campaign.

## Internal Notes
- Agents must never ask customers for codes "to verify" them — doing so trains customers to trust impersonators.
- Never contact customers from personal Telegram or phone accounts; it makes impersonation harder to spot.
- If several customers report the same fake account in one shift, alert the supervisor immediately.
