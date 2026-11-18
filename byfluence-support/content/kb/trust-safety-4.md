<!-- doc -->
# Customer Asks What Data Byfluence Holds
id: tns-data-access-request
type: article
category: trust-safety
subcategory: privacy
audience: both
priority: medium
department: trust_safety
features: accounts
tags: what data do you have, data access request, my personal data, copy of my data, data export, privacy request, ስለ እኔ ምን መረጃ አላችሁ, የግል መረጃዬ ቅጂ
related: tns-data-deletion-request, tns-privacy-complaint, tns-law-enforcement-request, tns-account-compromise, tns-identity-verification-concerns
templates: tpl-acknowledge-complaint, tpl-escalation-notification
policy_pending: yes

## Summary
A customer asks what personal information Byfluence holds about them, or asks for a copy of it. Verify the requester is the account owner, log the request, and route it to the team responsible for privacy — agents do not compile or send data exports.

## Overview
Customers may ask: "What information do you keep about me?", "Send me all my data", or "Why do you have my phone number?". These are legitimate requests. Byfluence's privacy policy, the formal process for data access requests and any legal response deadlines under applicable law are **not yet documented** — so agents log and escalate rather than answering in detail.

What agents **can** say in general terms: Byfluence uses account information to run the marketplace — accounts, bookings/orders, payments, support and safety. Customers can already see much of their own information in their dashboard (profile, bookings, purchase history, transaction history).

**Identity first.** A data request from someone who is not the verified account owner is a privacy risk — attackers use these requests to gather information. Responses go **only** to the registered contact details.

## Customer Steps
1. Log in and review the dashboard: profile, settings, consultation bookings, purchase history, order information and transaction history.
2. For anything not visible there, contact support from the registered email or phone and ask for a data access request.
3. Wait for the privacy team to contact them through the registered contact details.

## Information to Collect
- Customer name and registered email/phone — the request must come from them
- Account type (buyer, seller, both)
- What exactly they want (general explanation, a copy of specific data, or all data)
- Preferred language (Amharic/English)

> [!WARNING] Never ask for passwords, OTP codes or PINs. Never send personal data through chat to an unverified requester, and never send data to an email or phone number different from the registered one.

## Troubleshooting Steps
1. Confirm the request comes from the registered contact details. If not, ask the customer to write from their registered email/phone, or escalate to Trust & Safety for verification.
2. Point them to the dashboard sections they can already see.
3. Log the request on a ticket: type "Data access request", what they asked for, date received.
4. Escalate to **Trust & Safety** (privacy owner until a dedicated contact is designated). If the request mentions a law, a lawyer or a regulator → also **Management**.
5. Do not compile, screenshot or export the customer's data yourself.
6. Send the acknowledgement with the case number.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your request. You can see much of your information directly in your Byfluence dashboard — your profile, settings, bookings, purchase history and transaction history.

I have also recorded your request to know what personal data Byfluence holds about you, and passed it to the team responsible for privacy. For your security, they will respond only through the email or phone number registered on your account, and may ask you to confirm your identity.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጥያቄዎ እናመሰግናለን። አብዛኛውን መረጃዎን በቀጥታ በByfluence ዳሽቦርድዎ ላይ ማየት ይችላሉ — መገለጫዎን፣ ቅንብሮችዎን፣ ቀጠሮዎችዎን፣ የግዢ ታሪክዎን እና የግብይት ታሪክዎን።

Byfluence ስለ እርስዎ የያዘውን የግል መረጃ ለማወቅ ያቀረቡትን ጥያቄም መዝግቤ ለግላዊነት ኃላፊነት ላለው ቡድን አስተላልፌዋለሁ። ለደህንነትዎ ሲባል ቡድኑ ምላሽ የሚሰጠው በመለያዎ ላይ በተመዘገበው ኢሜይል ወይም ስልክ ቁጥር ብቻ ሲሆን፣ ማንነትዎን እንዲያረጋግጡም ሊጠይቅዎ ይችላል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, you can see much of your data in your dashboard (profile, bookings, purchases, transactions). I've logged your data request with our privacy team; they'll reply only via your registered email/phone. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ አብዛኛውን መረጃዎን በዳሽቦርድዎ (መገለጫ፣ ቀጠሮዎች፣ ግዢዎች፣ ግብይቶች) ማየት ይችላሉ። የመረጃ ጥያቄዎን ለግላዊነት ቡድናችን መዝግቤያለሁ፤ ምላሹ በተመዘገበው ኢሜይል/ስልክዎ ብቻ ይላካል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Every data access request → **Trust & Safety** (privacy owner).
- Request references a law, lawyer, court or regulator → **Management**.
- Request from someone other than the account holder (relative, employer, lawyer) → **Trust & Safety**; do not share anything.
- Request from police or a government body → `tns-law-enforcement-request` (**Management** only).

## Policy Pending Approval
- Approve the data access request process, response format and who fulfils it.
- Confirm legal obligations and response deadlines under applicable Ethiopian data protection law.
- Approve the identity verification standard for data requests.
- Publish the privacy policy describing what data is collected and why.

## Internal Notes
- Don't list from memory "we have your X, Y, Z" — you may be wrong or incomplete.
- A sudden data request right after an email/phone change on the account is a takeover signal — check `tns-account-compromise`.

<!-- doc -->
# Customer Asks to Delete Their Data
id: tns-data-deletion-request
type: article
category: trust-safety
subcategory: privacy
audience: both
priority: medium
department: trust_safety
features: accounts
tags: delete my data, delete my account, remove my information, right to be forgotten, erase data, close account, መረጃዬን ሰርዙ, መለያዬን ሰርዙ, አካውንቴን አጥፉ
related: tns-data-access-request, tns-privacy-complaint, tns-account-compromise, ref-refund-status, out-payout-hold-restriction
templates: tpl-acknowledge-complaint, tpl-escalation-notification
policy_pending: yes

## Summary
A customer asks Byfluence to delete their personal data or their account. Verify identity, check for open transactions, disputes or balances, explain that some records may need to be kept, and route the request — agents do not delete data.

## Overview
Customers may want to leave Byfluence, or may be upset after a bad experience or a privacy incident. A deletion request must be handled carefully:
- **Identity**: only the verified account owner can request deletion. An attacker who took over an account might try to delete it to hide fraud.
- **Open items**: upcoming bookings, open orders, pending refunds, disputes, or (for sellers) pending/available balances and withdrawals must be resolved or decided first — otherwise deletion could cause the customer to lose money or break someone else's case.
- **Records that may need to be kept**: transaction and financial records may have to be kept for legal, tax, accounting, fraud-prevention or dispute reasons. Which records, and for how long, is **not yet defined**.

The deletion process, timelines and what can be deleted are **pending approval**.

## Customer Steps
1. Contact support from the registered email or phone and state that they want their account/data deleted.
2. Finish or cancel any upcoming bookings or open orders (sellers: settle withdrawals) — support will help identify these.
3. Confirm the request when the privacy team contacts them through the registered contact details.

## Information to Collect
- Customer name and registered email/phone — request must come from them
- Account type (buyer, seller, both)
- Whether they want the **whole account** deleted or **specific information** removed (e.g., a phone number, a photo)
- The reason (optional — never pressure them; it helps if the reason is a complaint we can resolve)

> [!WARNING] Never ask for passwords, OTP codes or PINs. Never delete, deactivate or edit account data yourself based on a chat request.

## Troubleshooting Steps
1. Verify the request comes from the registered contact details; if not, escalate to **Trust & Safety** for verification.
2. Check for open items through authorized tools:
   - Upcoming bookings / open orders
   - Refunds pending, disputes or chargebacks open
   - Seller: pending or available balance, withdrawal pending, active listings
3. Explain any open items to the customer and what needs to happen first (or that the team will advise).
4. If the reason is a complaint (privacy, harassment, a dispute), offer to handle that too — open the relevant article.
5. Log the request ("Data deletion request"), list the open items, and escalate to **Trust & Safety** (privacy owner). Sellers with balances → also **Payments & Finance**.
6. Send the acknowledgement. Do not promise when or what will be deleted.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your request. I have recorded that you would like your Byfluence account and personal data deleted, and passed it to the team responsible for privacy.

Before the request can be completed, any open bookings, orders, refunds or (for sellers) balances on your account need to be settled, so that you don't lose money or access you are entitled to. [List any open items found.] Some transaction records may also need to be kept for legal and financial reasons; the team will explain what applies to you.

For your security, they will contact you only through your registered email or phone number to confirm the request.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጥያቄዎ እናመሰግናለን። የByfluence መለያዎ እና የግል መረጃዎ እንዲሰረዝ እንደሚፈልጉ መዝግቤ ለግላዊነት ኃላፊነት ላለው ቡድን አስተላልፌዋለሁ።

ጥያቄው ከመፈጸሙ በፊት፣ ገንዘብ ወይም የሚገባዎትን አገልግሎት እንዳያጡ በመለያዎ ላይ ያሉ ክፍት ቀጠሮዎች፣ ትዕዛዞች፣ ተመላሽ ገንዘቦች ወይም (ለሻጮች) ቀሪ ሂሳቦች መጠናቀቅ አለባቸው። [የተገኙ ክፍት ጉዳዮችን እዚህ ይዘርዝሩ።] አንዳንድ የግብይት መዝገቦች በሕግ እና በፋይናንስ ምክንያቶች ተጠብቀው መቆየት ሊኖርባቸው ይችላል፤ ቡድኑ ለእርስዎ የሚመለከተውን ያብራራልዎታል።

ለደህንነትዎ ሲባል ጥያቄውን ለማረጋገጥ የሚያገኙዎት በተመዘገበው ኢሜይል ወይም ስልክ ቁጥርዎ ብቻ ነው።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I've logged your deletion request with our privacy team. Open bookings, orders, refunds or balances must be settled first, and some transaction records may need to be kept. They'll confirm via your registered email/phone. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የመሰረዝ ጥያቄዎን ለግላዊነት ቡድናችን መዝግቤያለሁ። ክፍት ቀጠሮዎች፣ ትዕዛዞች፣ ተመላሾች ወይም ቀሪ ሂሳቦች መጀመሪያ መጠናቀቅ አለባቸው፤ አንዳንድ የግብይት መዝገቦችም ሊጠበቁ ይችላሉ። በተመዘገበው ኢሜይል/ስልክዎ ያረጋግጡልዎታል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, update on case {{ticket_id}}: your deletion request is with our privacy team. [If applicable: the following items still need to be settled first: ...] We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}}፦ የመሰረዝ ጥያቄዎ በግላዊነት ቡድናችን ዘንድ ነው። [የሚመለከት ከሆነ፦ የሚከተሉት ጉዳዮች መጀመሪያ መጠናቀቅ አለባቸው፦ ...] እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every deletion request → **Trust & Safety** (privacy owner).
- Seller with pending/available balance or withdrawal pending → **Payments & Finance**.
- Open disputes, refunds or chargebacks → **L2** / **Payments & Finance** decide sequencing.
- Request not from registered contact, or signs of takeover → **Trust & Safety** (`tns-account-compromise`).
- Legal reference, lawyer or regulator → **Management**.

## Resolution Procedure
1. Privacy owner records the decision: what is deleted/anonymised, what is retained and why.
2. Customer informed through registered contact details.
3. Ticket records the request date, open items handled and completion date.

## Policy Pending Approval
- Approve the account/data deletion process and who performs it.
- Define what data must be retained (transactions, invoices, dispute evidence, fraud records), for how long, and on what legal basis.
- Confirm legal obligations and response deadlines under applicable Ethiopian law.
- Decide how seller balances and active listings are handled when a seller requests deletion.

## Internal Notes
- Never say "your data will be completely erased" — retention rules are not defined.
- Deletion requests from accounts under investigation (fraud, disputes) must be flagged to Trust & Safety before anything happens.
- Replace or remove the bracketed lines before sending.

<!-- doc -->
# Police or Government Request for Information
id: tns-law-enforcement-request
type: article
category: trust-safety
subcategory: privacy
audience: internal
priority: high
department: management
tags: police request, law enforcement, government request, court order, subpoena, investigator asking, authorities want data, ፖሊስ, የፍርድ ቤት ትዕዛዝ, የመንግሥት ጥያቄ
related: tns-privacy-complaint, tns-data-access-request, tns-threats-safety, tns-report-fraud, tns-security-incident-report
templates: tpl-acknowledge-complaint, tpl-escalation-notification
policy_pending: yes

## Summary
Someone identifying as police, a court, a regulator or another government body asks support for information about a user, transaction or account. Support never shares any data — not even whether an account exists. Record the request and hand it to Management immediately.

## Overview
Law enforcement requests can arrive by phone, email, Telegram, letter, or in person. Some are genuine; some are impersonators trying to obtain personal data. Front-line agents cannot verify authority or judge legal validity — that requires Management and legal counsel. Therefore the rule is absolute:

> [!WARNING] **Support agents never share any user information with police, government or anyone claiming legal authority** — no names, contact details, transaction details, booking details, documents, or even confirmation that a person has an account. All such requests go to **Management** only.

This also applies when a **customer** asks support to "give the police" another user's details — the customer should report to the police, who then make an official request to Byfluence.

**Emergency exception**: if the requester says someone's life is in immediate danger, do not try to handle it yourself — escalate to Management in real time (phone/instant channel), and follow any emergency instructions Management gives.

## Information to Collect
- Requester's name, rank/title, organisation/unit, station or office
- Official contact details (office phone, official email) — as given by them
- Reference number of their case or document, if any
- What information they are asking for (as stated), and about whom (as stated)
- Whether they have a written request, court order or official letter
- Whether they claim urgency/emergency, and why
- Date, time and channel of contact

## Troubleshooting Steps
1. Be polite and professional. Do not confirm or deny anything about any user or transaction.
2. Explain that requests for information are handled by Byfluence management and must be made formally in writing.
3. Record the information above exactly as given.
4. Escalate immediately to **Management** with the record and any documents received. If urgency/emergency is claimed, also alert your supervisor in real time.
5. Do not forward documents to anyone except Management. Do not discuss the request with colleagues outside the escalation.
6. **Do not inform the user** that they are the subject of a request — Management decides any notification.
7. If a customer later asks "did the police contact you about me?", do not confirm or deny; escalate to Management.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence. Requests for information are handled by our management team and must be submitted formally in writing. Support staff are not able to share or confirm any information about users, accounts or transactions.

I have recorded your contact details and your request reference, and passed them to our management team, who will contact you through your official contact details.

Reference: {{ticket_id}}

Kind regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluenceን ስላገኙ እናመሰግናለን። የመረጃ ጥያቄዎች የሚስተናገዱት በአመራር ቡድናችን ሲሆን፣ በጽሑፍ በይፋ መቅረብ አለባቸው። የድጋፍ ሰራተኞች ስለ ተጠቃሚዎች፣ መለያዎች ወይም ግብይቶች ምንም ዓይነት መረጃ ማጋራትም ሆነ ማረጋገጥ አይችሉም።

የመገኛ መረጃዎን እና የጥያቄዎን መለያ ቁጥር መዝግቤ ለአመራር ቡድናችን አስተላልፌዋለሁ፤ በይፋዊ የመገኛ መረጃዎ በኩል ያገኙዎታል።

መለያ ቁጥር፦ {{ticket_id}}

ከአክብሮት ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Thank you for contacting Byfluence. Information requests are handled by our management team and must be made formally in writing; support staff cannot share or confirm any user information. I've passed your details to management. Reference: {{ticket_id}}

## Short Response (AM)
Byfluenceን ስላገኙ እናመሰግናለን። የመረጃ ጥያቄዎች በአመራር ቡድናችን የሚስተናገዱ ሲሆን በጽሑፍ በይፋ መቅረብ አለባቸው፤ የድጋፍ ሰራተኞች ምንም ዓይነት የተጠቃሚ መረጃ ማጋራት ወይም ማረጋገጥ አይችሉም። ዝርዝርዎን ለአመራር አስተላልፌያለሁ። መለያ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Every police, court, regulator or government information request → **Management** only, immediately.
- Claimed emergency (life in danger) → **Management** in real time + supervisor.
- Customer asks support to pass another user's details to police → explain they should report to police; log and inform **Management**.
- Suspected impersonation of authorities → **Management** + **Trust & Safety**.

## Resolution Procedure
1. Management confirms receipt and ownership.
2. Agent's record of the contact is complete and stored on a restricted ticket.
3. Support takes no further action unless Management instructs.

## Policy Pending Approval
- Approve the law enforcement request policy: who reviews, legal counsel involvement, required documents, verification of requester.
- Designate the official contact for authorities and how it is published.
- Decide the emergency disclosure procedure and who can authorise it.
- Decide when and how users are notified about requests concerning them.

## Internal Notes
- Pressure is common ("I'm a police officer, I need this now or you'll be in trouble"). Stay calm; the answer is the same every time.
- Never send screenshots of user profiles or transactions, even "to help identify the right person".
- If a person visits in person, take their details and call your supervisor/Management; do not show any screen.

<!-- doc -->
# Marketplace Policy Violations
id: tns-policy-violations
type: article
category: trust-safety
subcategory: policy-violations
audience: both
priority: medium
department: trust_safety
tags: policy violation, against the rules, prohibited item, banned listing, rule breaking, why was my account suspended, report rule violation, የደንብ ጥሰት, የተከለከለ ዕቃ, ደንብ መጣስ
related: tns-report-abusive-behavior, tns-misleading-descriptions, tns-fake-products, tns-off-platform-payment-request, tns-harassment
templates: tpl-acknowledge-complaint, tpl-escalation-notification
policy_pending: yes

## Summary
How to handle reports of marketplace rule violations (prohibited items, fake reviews, fee avoidance, abusive conduct) and questions from users who were restricted, suspended or banned for a violation.

## Overview
Byfluence has marketplace rules that sellers' offerings are subject to, and an admin function for listing moderation and seller suspension. Seller operational statuses are **Active, Suspended, Banned** (separate from verification statuses Pending, Verified, Rejected). However, the **detailed marketplace rules, prohibited items list and enforcement ladder are not yet published** in this knowledge base.

Two kinds of contacts:
1. **Someone reports a violation** → collect facts and route (this article plus the specific article for the type).
2. **A user was restricted for a violation** and asks why or wants to appeal → explain what you can see, never debate the decision, and route the appeal.

Common violation types (route to the specific article where one exists):
| Type | Article / department |
|---|---|
| Fraud, scams | `tns-report-fraud` — Trust & Safety |
| Off-platform payment requests | `tns-off-platform-payment-request` — Trust & Safety |
| Counterfeit items | `tns-fake-products` — Trust & Safety |
| Misleading listings | `tns-misleading-descriptions` — Seller Operations |
| IP infringement | `tns-intellectual-property` — Trust & Safety |
| Harassment, threats | `tns-harassment`, `tns-threats-safety` |
| Prohibited/illegal items or services | Trust & Safety (Management if illegal or dangerous) |
| Fake accounts, multiple accounts to abuse promotions/refunds | Trust & Safety |
| Fake reviews (if reviews exist) | Trust & Safety |

## Information to Collect
**Report of a violation**
- Listing/profile link, what rule they think is broken, screenshots, dates
**User asking about their own restriction**
- Their name and registered contact (confirm identity)
- What they see (message, status, listing removed)
- Their explanation and any evidence they want considered

> [!WARNING] Never ask for passwords, OTP codes or PINs. Do not reveal who reported a user or what internal evidence was used.

## Troubleshooting Steps
### Report of a violation
1. Capture the listing/profile now.
2. Route to the specific article from the table; otherwise escalate to **Trust & Safety**.
3. Illegal or dangerous items/services (weapons, drugs, medicines, exploitation) → **Trust & Safety** Critical + **Management**.

### User asking about their restriction
1. Confirm identity.
2. Check, through authorized tools, the account status and any recorded reason. Distinguish verification status (Pending/Verified/Rejected) from operational status (Active/Suspended/Banned).
3. Share only the reason recorded as shareable. If no shareable reason is recorded, say the team will explain and escalate.
4. If they want to appeal, collect their explanation and evidence, and escalate to **Trust & Safety** / **Seller Operations** (whichever applied the action).
5. For sellers: explain that questions about pending earnings during a restriction go to Payments (see `out-payout-hold-restriction`).
6. Never promise reinstatement.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support.

[For a report] Thank you for reporting this. Please send the listing or profile link, what you believe is against the rules, and any screenshots. Your report will be kept confidential.

[For a restricted user] I understand you have questions about the restriction on your account. I have recorded your request, and the team responsible will review it. If you would like them to consider any information or evidence, please send it to me and I will add it to your case. I'm not able to promise a particular outcome, but I will keep you updated.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን።

[ለሪፖርት] ይህንን ሪፖርት ስላደረጉ እናመሰግናለን። እባክዎ የዝርዝሩን ወይም የመገለጫውን ሊንክ፣ ደንብ ይጥሳል ብለው የሚያምኑበትን ነገር እና ያሉዎትን ስክሪንሾቶች ይላኩ። ሪፖርትዎ በሚስጥር ይያዛል።

[ለተገደበ ተጠቃሚ] በመለያዎ ላይ ስለተደረገው ገደብ ጥያቄ እንዳለዎት ተረድቻለሁ። ጥያቄዎን መዝግቤያለሁ፤ ኃላፊነት ያለው ቡድን ይገመግመዋል። ቡድኑ እንዲያየው የሚፈልጉት መረጃ ወይም ማስረጃ ካለ ይላኩልኝ፤ ወደ ጉዳይዎ እጨምረዋለሁ። የተለየ ውጤት ቃል መግባት ባልችልም ሂደቱን አሳውቅዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, [report] please send the listing/profile link, the rule you think is broken, and screenshots — it's confidential. [restricted] I've logged your request for review; send any evidence you want considered. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ [ሪፖርት] እባክዎ የዝርዝሩን/የመገለጫውን ሊንክ፣ ይጣሳል ያሉትን ደንብ እና ስክሪንሾቶች ይላኩ — በሚስጥር ይያዛል። [ገደብ] ጥያቄዎን ለግምገማ መዝግቤያለሁ፤ እንዲታይ የሚፈልጉትን ማስረጃ ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, update on case {{ticket_id}}: the responsible team is reviewing it. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}}፦ ኃላፊነት ያለው ቡድን እየገመገመው ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Violation reports → **Trust & Safety** (or the specific article's department).
- Illegal, dangerous or exploitative items/services → **Trust & Safety** Critical + **Management**.
- Restriction appeals → the team that applied the action (**Trust & Safety** or **Seller Operations**).
- Seller earnings affected by a restriction → **Payments & Finance**.

## Resolution Procedure
1. Owning team records the review result and any action or reinstatement.
2. User informed in approved wording; reporter receives a neutral closing message.
3. Record violation type and outcome.

## Policy Pending Approval
- Publish the marketplace rules / code of conduct and the prohibited & restricted items list.
- Approve the enforcement ladder (warning, listing removal, suspension, ban) and who decides each step.
- Approve the appeal process for restricted users.
- Decide how earnings are handled for suspended or banned sellers.

## Internal Notes
- Remove the bracketed option you don't need before sending.
- A Verified seller can still be Suspended — don't tell a user "you're verified so you can't be suspended".
- Never quote a rule that isn't published. If you can't find the rule, escalate rather than guess.

<!-- doc -->
# Fraud & Safety Triage Guide
id: tns-tsg-fraud-triage
type: troubleshooting
category: trust-safety
subcategory: fraud
audience: internal
priority: critical
department: trust_safety
tags: triage, severity levels, fraud triage, safety triage, who to call, urgent escalation, critical case, ቅድሚያ, አስቸኳይ, የደህንነት ደረጃ
related: tns-report-fraud, tns-threats-safety, tns-account-compromise, tns-unauthorized-transaction, ref-dispute-escalation, ref-tsg-dispute-handling-master
templates: tpl-account-compromise-urgent, tpl-escalation-notification, tpl-acknowledge-complaint
policy_pending: yes

## Summary
A one-page decision guide for any fraud, safety, security or abuse contact: how to set the severity, the immediate actions for each level, and which team to call.

## Overview
Trust & Safety cases override normal queues. In the first minutes of a contact, the agent must answer three questions:
1. **Is anyone in danger?**
2. **Is money or access being lost right now?**
3. **Is this one person, or many?**

### Severity levels
| Level | Examples | Response |
|---|---|---|
| **Critical** | Threat of violence; self-harm intent; minor at risk; account takeover with money at risk (seller balance, payout details changed); unauthorized transactions in progress; many customers affected; live data exposure; dangerous/illegal items | Act now. Real-time escalation (supervisor + department on-call). Customer gets safety steps first. |
| **High** | Fraud report with loss already happened; suspected account compromise without money moving; harassment; off-platform payment request with payment made; identity theft; refund to a different account; counterfeit report | Escalate to Trust & Safety in the same shift with full information. |
| **Medium** | Suspicious seller without loss; misleading listing; IP complaint; policy violation report; privacy complaint without exposure; data access/deletion request | Log and route through the normal queue to the owning team. |
| **Low** | General safety questions ("is it safe to pay?"), how to report, education | Answer with approved guidance; log. |

When unsure between two levels, choose the **higher** one.

## Troubleshooting Steps
### Step 1 — Danger check
- Threat of violence, self-harm, minor at risk, physical danger → **Critical** → `tns-threats-safety`.
  - Tell the person to contact local police/emergency services if in immediate danger.
  - Alert supervisor and **Management** in real time.

### Step 2 — Money / access at risk now?
- Customer can't log in, contact details changed, unknown logins → `tns-account-compromise`.
- Unknown payment/withdrawal → `tns-unauthorized-transaction`.
- Seller balance or payout details involved → ask **Payments & Finance** to hold now.
- Customer shared codes/PIN → tell them to change password and call their bank/provider now.
- Refund destination change request → `ref-refund-to-different-account`.
→ **Critical** if money is moving or about to move; otherwise **High**.

### Step 3 — Scale
- Several customers reporting the same seller, link, fake account, or system behavior in a short time → **Critical** incident → supervisor + Trust & Safety + Technical + Management (`tns-security-incident-report`, `tns-impersonation-of-byfluence`).

### Step 4 — Classify and route
| What | Article | Department |
|---|---|---|
| Fraud / scam | `tns-report-fraud` | Trust & Safety (+ Payments if on-platform payment) |
| Suspicious seller | `tns-suspicious-seller` | Trust & Safety |
| Off-platform payment | `tns-off-platform-payment-request` | Trust & Safety |
| Impersonation of Byfluence | `tns-impersonation-of-byfluence` | Trust & Safety |
| Counterfeit / misleading / IP | `tns-fake-products`, `tns-misleading-descriptions`, `tns-intellectual-property` | Trust & Safety / Seller Operations |
| Harassment / abuse | `tns-harassment`, `tns-report-abusive-behavior` | Trust & Safety |
| Identity documents | `tns-identity-verification-concerns` | Trust & Safety + Seller Operations |
| Security vulnerability | `tns-security-incident-report` | Trust & Safety + Technical + Management |
| Privacy / data requests | `tns-privacy-complaint`, `tns-data-access-request`, `tns-data-deletion-request` | Trust & Safety |
| Police / government | `tns-law-enforcement-request` | Management only |
| Refund abuse | `ref-abuse-of-refunds` | Trust & Safety + L2 |

### Step 5 — Immediate actions checklist
- [ ] Safety advice given (emergency services / change password / call bank)
- [ ] Severity set (higher when in doubt)
- [ ] Evidence preserved (listing/profile captured, original files attached)
- [ ] Money movement hold requested (if relevant)
- [ ] Escalated to the right team(s), real-time for Critical
- [ ] Reporter's identity protected
- [ ] Customer has case number and next update time

### Who to call
| Need | Team |
|---|---|
| Danger to a person, legal/police, reputational crisis | **Management (Level 4)** + supervisor |
| Fraud, compromise, abuse, privacy, counterfeit | **Trust & Safety** |
| Holds, reversals, refunds, payouts | **Payments & Finance** |
| System bugs, data exposure, login issues | **Technical / Engineering** |
| Seller verification, listings, seller status | **Seller Operations** |
| Delivery-related incidents | **Logistics & Fulfillment** |
| Unsure / no access | **Senior Support / Supervisor (L2)** |

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us. Your safety and the security of your account are our priority.

If you are in immediate danger, please contact the local police or emergency services right away. If you have shared your password, PIN or any code with anyone, change your Byfluence password now and contact your bank or mobile-money provider — and never share these again; Byfluence will never ask for them.

I have escalated your case to our specialised team as urgent. Your case number is {{ticket_id}}, and we will update you as soon as possible.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን። የእርስዎ ደህንነት እና የመለያዎ ጥበቃ ቅድሚያ የምንሰጠው ጉዳይ ነው።

አሁን አስቸኳይ አደጋ ላይ ከሆኑ፣ እባክዎ ወዲያውኑ በአካባቢዎ ያለውን ፖሊስ ወይም የአስቸኳይ ጊዜ አገልግሎት ያነጋግሩ። የይለፍ ቃልዎን፣ ፒንዎን ወይም ማንኛውንም ኮድ ለማንም አጋርተው ከሆነ፣ የByfluence የይለፍ ቃልዎን አሁኑኑ ይቀይሩ፤ ባንክዎን ወይም የሞባይል ገንዘብ አቅራቢዎን ያነጋግሩ — ከዚህ በኋላም በፍጹም አያጋሩ፤ Byfluence በፍጹም አይጠይቅዎትም።

ጉዳይዎን እንደ አስቸኳይ ለልዩ ቡድናችን አስተላልፌዋለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው፤ በተቻለ ፍጥነት መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your safety comes first. In immediate danger? Contact local police now. Shared a password/PIN/code? Change your password and call your bank — and never share them again. Escalated as urgent. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ደህንነትዎ ይቀድማል። አስቸኳይ አደጋ ላይ ነዎት? አሁኑኑ ፖሊስ ያነጋግሩ። የይለፍ ቃል/ፒን/ኮድ አጋርተዋል? የይለፍ ቃልዎን ይቀይሩ፤ ባንክዎንም ያነጋግሩ — ዳግመኛ በፍጹም አያጋሩ። በአስቸኳይ ተላልፏል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- **Critical** → real-time escalation to supervisor and the owning department; **Management** for danger to people, legal/police, many customers affected, or data exposure.
- **High** → **Trust & Safety** (plus Payments/Technical/Seller Operations as relevant) within the same shift.
- **Medium/Low** → normal queue to the owning team.
- No access to the tools needed to assess → **Senior Support / Supervisor (L2)** immediately.

## Policy Pending Approval
- Approve official severity definitions and internal response targets for each level.
- Define the on-call/real-time escalation path for Critical cases (including outside working hours).
- Publish the official emergency contacts agents may share with customers.
- Approve which teams can place holds on payouts/refunds and how agents request them.

## Internal Notes
- The most common mistake is treating a Critical case as a normal ticket and waiting in the queue. If money or safety is at risk, use the real-time channel.
- Never ask for codes, even to "verify". Never change contact or payout details through chat.
- Protect reporters: no reported user is ever told who reported them.
- After a hard case, talk to your supervisor — it's part of the job, not a weakness.
