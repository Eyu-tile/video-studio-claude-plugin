<!-- doc -->
# Fake or Counterfeit Products Reported
id: tns-fake-products
type: article
category: trust-safety
subcategory: listing-violations
audience: both
priority: high
department: trust_safety
features: physical-products, digital-products
tags: fake product, counterfeit, not original, replica, knockoff, fake brand, not genuine, ሐሰተኛ ምርት, ኦሪጅናል አይደለም, ቅጂ
related: tns-misleading-descriptions, tns-intellectual-property, ref-product-refunds, tns-suspicious-seller, tns-policy-violations
templates: tpl-acknowledge-complaint, tpl-request-screenshot
policy_pending: yes

## Summary
A buyer reports that a product they received (or see listed) is fake or counterfeit — e.g., sold as an original brand but is a copy. Collect evidence, capture the listing, and route to Trust & Safety; refund handling follows the normal refund process.

## Issue Description
Counterfeit goods harm buyers, legitimate brands and Byfluence's reputation. Reports can come from buyers who received an item, from buyers browsing listings, or from brand owners (see `tns-intellectual-property`). Physical and digital products are **planned expansion areas** — check the **Feature Status** page; if they are not live, find out how the customer bought the item. Agents do not judge authenticity themselves — they collect evidence and route.

## Possible Causes
- Seller knowingly lists counterfeit items as original
- Seller sources from a supplier who supplied fakes (inventory-free/reseller chains included)
- Listing says "original" but photos show a different item
- Buyer received a genuine item but believes it is fake (packaging changed, regional version)
- Digital product that is a pirated copy of someone else's work

## Information to Collect
- Order ID ({{order_id}}) or listing link, seller name, product name
- Why the buyer believes it is fake (logo, labels, serial number, packaging, quality, missing certificate)
- Clear photos: item, labels, logos, serial/IMEI numbers where relevant, packaging
- Screenshot of the listing claims (e.g., "100% original")
- Whether the buyer wants a refund (start `ref-product-refunds` in parallel)

> [!WARNING] Never ask for passwords, OTP codes or PINs. Do not tell the buyer the item "is fake" or "is genuine" — you cannot determine that.

## Troubleshooting Steps
1. Check Feature Status for physical/digital products.
2. Capture the listing now (screenshots + link) — it may be edited or removed.
3. Collect the buyer's photos and the specific reasons.
4. Check for other reports on the same seller/listing and link them.
5. Escalate to **Trust & Safety** (listing review, seller action). Copy **Seller Operations** for listing moderation.
6. If the buyer wants their money back, open a refund request via `ref-product-refunds` and link the tickets.
7. Advise the buyer to keep the item and packaging until the case is decided.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for reporting this. We take concerns about counterfeit products seriously.

To help our team review {{product_name}} (order {{order_id}}), please send:
1. Clear photos of the item, its labels or logos, and the packaging
2. What makes you believe it is not genuine
3. A screenshot of the listing, if you have it

Please keep the item and packaging until we confirm the next step. If you would like to request a refund, let me know and I will add it to your case.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ይህንን ስላሳወቁን እናመሰግናለን። ስለ ሐሰተኛ ምርቶች የሚቀርቡ ስጋቶችን በቁም ነገር እንመለከታለን።

ቡድናችን {{product_name}}ን (ትዕዛዝ {{order_id}}) እንዲገመግም እባክዎ የሚከተሉትን ይላኩ፦
1. የዕቃውን፣ የመለያዎቹን ወይም የምልክቶቹን (logo) እና የማሸጊያውን ግልጽ ፎቶዎች
2. ኦሪጅናል አይደለም ብለው እንዲያስቡ ያደረገዎትን ምክንያት
3. ካለዎት የዝርዝሩን (listing) ስክሪንሾት

ቀጣዩን እርምጃ እስክናረጋግጥ ድረስ እባክዎ ዕቃውን እና ማሸጊያውን ያስቀምጡ። ተመላሽ ገንዘብ መጠየቅ ከፈለጉ ይንገሩኝ፤ ወደ ጉዳይዎ እጨምረዋለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for reporting this. Please send clear photos of the item, labels and packaging, why you think it's not genuine, and a listing screenshot if you have one. Keep the item for now. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን። እባክዎ የዕቃውን፣ የመለያዎቹን እና የማሸጊያውን ግልጽ ፎቶዎች፣ ኦሪጅናል አይደለም ያሉበትን ምክንያት እና ካለ የዝርዝሩን ስክሪንሾት ይላኩ። ዕቃውን ለጊዜው ያስቀምጡት። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, update on case {{ticket_id}}: our Trust & Safety team is reviewing the listing and the evidence you sent. If you requested a refund, it is being reviewed in the same case. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}}፦ የእምነትና ደህንነት ቡድናችን ዝርዝሩን እና የላኩልንን ማስረጃ እየገመገመ ነው። ተመላሽ ገንዘብ ጠይቀው ከሆነ በዚሁ ጉዳይ ውስጥ እየታየ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every counterfeit report → **Trust & Safety** (+ **Seller Operations** for the listing).
- Refund requested → **L2** via `ref-product-refunds`.
- Brand owner or lawyer complaint → `tns-intellectual-property`; legal notices → **Management**.
- Counterfeit items that may be dangerous (electronics, cosmetics, medicine) → **Trust & Safety**, priority Critical.
- Reseller/supplier chain involved → **Seller Operations**.

## Resolution Procedure
1. Trust & Safety records its finding and any listing/seller action.
2. Refund decision communicated separately through the refund process.
3. Record product type, seller, and outcome; link related reports.

## Policy Pending Approval
- Approve the prohibited/restricted items list including counterfeit goods.
- Decide the evidence required to remove a listing for counterfeiting and the seller's right to respond.
- Decide refund rules for confirmed counterfeit items (including return logistics).
- Decide supplier accountability for counterfeits in inventory-free selling.

## Internal Notes
- Possibly dangerous counterfeits (chargers, cosmetics, medication) are safety issues — escalate as Critical and advise the buyer to stop using the item.
- Don't publicly label a seller as a counterfeiter; findings belong to Trust & Safety.
- Screenshots of the listing should show the date captured.

<!-- doc -->
# Misleading Listing Descriptions
id: tns-misleading-descriptions
type: article
category: trust-safety
subcategory: listing-violations
audience: both
priority: medium
department: seller_ops
tags: misleading listing, not as described, false description, fake credentials, wrong photos, exaggerated claims, listing lies, የተሳሳተ መግለጫ, እንደተገለጸው አይደለም
related: tns-fake-products, ref-buyer-seller-disagreement, ref-consultation-refunds, ref-product-refunds, tns-policy-violations
templates: tpl-acknowledge-complaint, tpl-request-screenshot
policy_pending: yes

## Summary
A buyer reports that a listing is misleading — wrong photos, false credentials, exaggerated claims, hidden conditions, or a service/product that differs from its description. Capture the listing, collect the specifics, and route to Seller Operations (Trust & Safety if deception looks intentional).

## Issue Description
Listings must accurately describe the offering: consultant name and expertise, topic, duration, price and availability for consultations; item details for products; content and format for digital products. Misleading descriptions cause disputes and refund requests and damage trust. Some cases are honest mistakes (outdated photos, unclear wording); others are deliberate deception (fake qualifications, "guaranteed income"). The agent records, does not judge, and routes.

## Possible Causes
- Outdated or copied photos
- Exaggerated or unverifiable claims ("certified", "guaranteed results", "earn ETB … per day")
- Fake qualifications or credentials for consultants
- Missing important conditions (language of session, duration, item condition, digital format)
- Wrong category, wrong price, or hidden extra charges requested later
- Listing edited after purchase

## Information to Collect
- Listing link and seller name; order/booking ID if purchased
- The exact claim the buyer considers misleading (quote it)
- What was actually received or experienced
- Screenshots of the listing (ideally from the time of purchase) and of what was received

> [!WARNING] Never ask for passwords, OTP codes or PINs.

## Troubleshooting Steps
1. Capture the listing as it is now; ask the buyer if they have a screenshot from the time of purchase.
2. Record the specific claim vs. reality, quoting the listing.
3. Decide the route:
   - **Honest mistake / quality issue** → **Seller Operations** (listing correction).
   - **Deliberate deception, fake credentials, dangerous claims** → **Trust & Safety**.
   - **Buyer wants money back** → open the matching refund article (`ref-consultation-refunds`, `ref-product-refunds`, `ref-digital-refunds`) and link it.
4. Do not tell the buyer what action will be taken against the seller.
5. Close the report loop with a neutral follow-up.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know. Accurate listings are important for everyone on Byfluence, and we appreciate your report.

To review this listing, please send:
1. The listing link or the seller's name
2. The part of the description you believe is misleading
3. What you actually received or experienced, with screenshots or photos if possible

If you would also like to request a refund, please tell me and I will add it to your case. Your report will be kept confidential.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን። ትክክለኛ ዝርዝሮች ለሁሉም የByfluence ተጠቃሚዎች አስፈላጊ ናቸው፤ ሪፖርትዎን እናደንቃለን።

ይህን ዝርዝር ለመገምገም እባክዎ የሚከተሉትን ይላኩ፦
1. የዝርዝሩን (listing) ሊንክ ወይም የሻጩን ስም
2. አሳሳች ነው ብለው የሚያምኑበትን የመግለጫውን ክፍል
3. በእርግጥ የደረሰዎትን ወይም ያጋጠመዎትን፣ ከተቻለ ከስክሪንሾቶች ወይም ከፎቶዎች ጋር

ተመላሽ ገንዘብም መጠየቅ ከፈለጉ እባክዎ ይንገሩኝ፤ ወደ ጉዳይዎ እጨምረዋለሁ። ሪፖርትዎ በሚስጥር ይያዛል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for reporting this. Please send the listing link, the part you find misleading, and what you actually received (with screenshots). Tell me if you also want a refund. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን። እባክዎ የዝርዝሩን ሊንክ፣ አሳሳች ያሉትን ክፍል እና በእርግጥ የደረሰዎትን (ከስክሪንሾት ጋር) ይላኩ። ተመላሽ ገንዘብም ከፈለጉ ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, thank you again for your report (case {{ticket_id}}). The listing has been reviewed by our team and appropriate steps have been taken. For privacy reasons we cannot share details about actions on other accounts.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ሪፖርትዎ (የጉዳይ ቁጥር {{ticket_id}}) በድጋሚ እናመሰግናለን። ዝርዝሩ በቡድናችን ተገምግሞ ተገቢው እርምጃ ተወስዷል። በግላዊነት ምክንያት በሌሎች መለያዎች ላይ ስለተወሰዱ እርምጃዎች ዝርዝር ማካፈል አንችልም።

## Escalation Conditions
- Listing inaccuracies → **Seller Operations**.
- Fake credentials, deliberate deception, health/financial "guarantees" → **Trust & Safety**.
- Refund request → **L2** via the relevant refund article.
- Same listing reported multiple times → **Seller Operations**, priority High.

## Resolution Procedure
1. Seller Operations / Trust & Safety record the review result.
2. Reporter receives the neutral closing message.
3. Record the claim type (photos, credentials, claims, conditions, price).

## Policy Pending Approval
- Approve listing accuracy standards and prohibited claims (e.g., guaranteed income or health results).
- Decide whether consultant credentials are verified and how.
- Decide whether Byfluence keeps listing version history to resolve "edited after purchase" disputes.

## Internal Notes
- Quote the listing exactly in the ticket; paraphrasing loses the evidence.
- "Zero investment" claims for inventory-free selling must not suggest zero cost or zero risk — report such listings to Seller Operations.
- Unclear ≠ misleading. Describe the gap; let reviewers decide intent.

<!-- doc -->
# Trademark, Copyright and IP Complaints
id: tns-intellectual-property
type: article
category: trust-safety
subcategory: listing-violations
audience: both
priority: medium
department: trust_safety
features: digital-products
tags: copyright, trademark, intellectual property, stolen content, pirated ebook, my design copied, brand complaint, ip complaint, የቅጂ መብት, የንግድ ምልክት, አእምሯዊ ንብረት
related: tns-fake-products, tns-misleading-descriptions, ref-digital-refunds, tns-policy-violations, tns-law-enforcement-request
templates: tpl-acknowledge-complaint, tpl-escalation-notification
policy_pending: yes

## Summary
Someone reports that a listing uses their trademark, copyrighted content (e-book, course, design, photos) or other intellectual property without permission — or a seller asks why their listing was flagged for IP. Collect the claim in a structured way and route; agents never remove listings or judge ownership.

## Issue Description
IP complaints come from brand owners, creators, other sellers, or buyers who notice pirated content (common with digital products). They can also come as formal legal letters. Byfluence is a marketplace facilitator; the seller is responsible for their listings. A formal IP notice-and-takedown process **has not been approved yet**, so every IP complaint is escalated to **Trust & Safety**, and any legal notice goes to **Management**.

## Possible Causes
- Seller re-selling someone else's e-book, course, template or design
- Listing photos copied from another seller or brand website
- Brand name/logo used on counterfeit goods
- Seller name or store name confusingly similar to a known brand
- Mistaken claim (the seller has a licence or is an authorised reseller)

## Information to Collect
**From the complainant**
- Name, organisation (if any) and contact email
- The work or trademark they own, and proof or a link showing ownership (e.g., original publication, registration reference)
- The Byfluence listing link(s) they say infringe
- A short explanation of what is copied
- Whether they are the owner or authorised to act for the owner
**From the seller (if they contact us)**
- Their explanation and any licence, authorisation or proof of original creation

> [!WARNING] Never ask for passwords, OTP codes or PINs. Do not share the complainant's personal contact details with the seller, or the seller's with the complainant, without Trust & Safety approval.

## Troubleshooting Steps
1. Thank the complainant; confirm you will route it to the responsible team.
2. Collect the structured information above. If it is a formal legal letter (from a lawyer or court), do not respond on the substance — acknowledge receipt only and escalate to **Management** immediately.
3. Capture the listing(s) as they are now.
4. Escalate to **Trust & Safety** with the complaint and evidence; copy **Seller Operations**.
5. If a buyer reports pirated content they purchased and wants a refund, link `ref-digital-refunds`.
6. If the seller contacts support about an IP flag, record their response and evidence, and add it to the same case.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence about your intellectual property concern. We take these reports seriously.

So our responsible team can review it, please send:
1. A description of the work or trademark you own
2. A link or document showing your ownership
3. The Byfluence listing link(s) concerned
4. A short explanation of what has been copied or used, and whether you are the owner or acting for the owner

Our team will review the information and may contact you for more details. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ አእምሯዊ ንብረትዎ (intellectual property) ስጋት Byfluenceን ስላገኙ እናመሰግናለን። እንደዚህ ያሉ ሪፖርቶችን በቁም ነገር እንመለከታለን።

የሚመለከተው ቡድናችን እንዲገመግመው እባክዎ የሚከተሉትን ይላኩ፦
1. የእርስዎ የሆነውን ሥራ ወይም የንግድ ምልክት መግለጫ
2. ባለቤትነትዎን የሚያሳይ ሊንክ ወይም ሰነድ
3. የሚመለከታቸውን የByfluence ዝርዝሮች (listing) ሊንክ
4. ምን እንደተቀዳ ወይም ጥቅም ላይ እንደዋለ አጭር ማብራሪያ፣ እንዲሁም ባለቤቱ ራስዎ መሆንዎን ወይም ባለቤቱን ወክለው መሆንዎን

ቡድናችን መረጃውን ይገመግማል፤ ተጨማሪ ዝርዝር ካስፈለገም ሊያገኝዎ ይችላል። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for reporting this. Please send: what you own, proof of ownership (link/document), the Byfluence listing link(s), and what was copied. Our team will review. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን። እባክዎ ይላኩ፦ የእርስዎ የሆነውን ሥራ፣ የባለቤትነት ማረጋገጫ (ሊንክ/ሰነድ)፣ የByfluence ዝርዝር ሊንክ(ኮች) እና የተቀዳውን። ቡድናችን ይገመግመዋል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, update on case {{ticket_id}}: our team is reviewing your intellectual property report together with the listing information. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}}፦ ቡድናችን የአእምሯዊ ንብረት ሪፖርትዎን ከዝርዝሩ መረጃ ጋር እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every IP complaint → **Trust & Safety** (+ **Seller Operations**).
- Formal legal letter, lawyer, court order or threatened lawsuit → **Management** immediately; acknowledge receipt only.
- Counterfeit physical goods → also `tns-fake-products`.
- Buyer refund for pirated content → **L2** via `ref-digital-refunds`.

## Resolution Procedure
1. Trust & Safety records the decision (listing kept, edited, removed) and informs the parties as appropriate.
2. Record complainant type (brand, creator, seller, buyer), content type and outcome.

## Policy Pending Approval
- Approve a formal IP notice-and-takedown process (required information, review steps, seller response/counter-notice).
- Decide repeat-infringer rules for sellers.
- Confirm with legal counsel the obligations under applicable law and who signs responses to legal notices.

## Internal Notes
- Do not state that something "is" or "is not" copyright infringement. That is a legal/Trust & Safety decision.
- Do not remove or hide listings yourself, even if the claim looks obvious.
- Keep any legal letter exactly as received; forward it unchanged to Management.

<!-- doc -->
# Harassment Between Users
id: tns-harassment
type: article
category: trust-safety
subcategory: abuse
audience: both
priority: high
department: trust_safety
tags: harassment, abusive messages, insults, bullying, unwanted contact, stalking, sexual harassment, keeps messaging me, ትንኮሳ, ስድብ, ማስፈራራት, ያልተፈለገ መልዕክት
related: tns-threats-safety, tns-report-abusive-behavior, ref-buyer-seller-disagreement, tns-privacy-complaint, tns-policy-violations
templates: tpl-acknowledge-complaint, tpl-request-screenshot, tpl-escalation-notification
policy_pending: yes

## Summary
A buyer or seller reports being harassed by another user — insulting, sexual, discriminatory or repeated unwanted messages, during a consultation, or contact outside Byfluence after a transaction. Support the person, preserve evidence, protect their identity, and escalate to Trust & Safety.

## Issue Description
Harassment can happen in Byfluence messages, during Google Meet sessions, or off-platform after a user obtained someone's contact details. It can be sexual, discriminatory, insulting, or persistent unwanted contact. The person reporting may be distressed or afraid. Agents should respond with empathy, not judgment, and never minimise the experience. **If there is any threat of violence or immediate danger, switch to `tns-threats-safety` immediately.**

## Possible Causes
- A dispute that escalated into insults or pressure
- Sexual harassment during or after a consultation
- Discriminatory remarks (ethnicity, religion, gender, disability)
- Repeated unwanted contact after a booking or purchase, including off-platform (phone, Telegram)
- A user sharing or threatening to share someone's personal information or images

## Information to Collect
- Reporter's name and account (confirm identity)
- The other user's name/profile and the related booking/order, if any
- What happened, when, and where (Byfluence messages, Google Meet session, phone, Telegram, other)
- Screenshots or recordings the reporter already has (do not ask them to record anyone)
- Whether they feel in immediate danger
- What they want (stop contact, block, report, refund for a session that became abusive)

> [!WARNING] Never ask for passwords, OTP codes or PINs. Never ask the reporter to keep engaging with the harasser to "collect more evidence". Never share the reporter's details with the reported user.

## Troubleshooting Steps
1. **Safety check:** "Do you feel you are in immediate danger?" If yes → `tns-threats-safety` now.
2. Acknowledge with empathy; thank them for reporting. Do not question their account or ask "what did you do to provoke this?"
3. Collect evidence they already have; attach original files to a ticket with restricted visibility if available.
4. Advise practical protection: stop replying to the person, use blocking tools on Byfluence (if available) and on Telegram/phone, do not share more personal details.
5. Escalate to **Trust & Safety**, priority **High** (Critical if sexual exploitation, threats, or sharing of intimate images).
6. If the harassment is linked to an upcoming booking, ask L2/Trust & Safety whether the booking should be cancelled or reassigned — the reporter should not be forced to attend.
7. If a refund is requested for an abusive session, open the refund process and link it.
8. Never contact the reported user to "mediate" — Trust & Safety handles contact and action.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for telling us, and I'm sorry you have experienced this. No one should be treated this way on Byfluence, and your report is being taken seriously.

If you feel you are in immediate danger, please contact local police or emergency services right away.

To help our Trust & Safety team act, please send me:
1. The name or profile of the person involved, and the related booking or order if there is one
2. Screenshots of the messages or a description of what happened, with dates
3. Where it happened (Byfluence messages, a Google Meet session, phone, Telegram or elsewhere)

We recommend that you stop replying to this person and block them where you can. Your identity will not be shared with them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለነገሩን እናመሰግናለን፤ ይህ ስላጋጠመዎት በጣም እናዝናለን። በByfluence ላይ ማንም ሰው እንዲህ ዓይነት አያያዝ ሊደርስበት አይገባም፤ ሪፖርትዎንም በቁም ነገር እየተመለከትነው ነው።

አሁን አስቸኳይ አደጋ ላይ እንዳሉ ከተሰማዎት፣ እባክዎ ወዲያውኑ በአካባቢዎ ያለውን ፖሊስ ወይም የአስቸኳይ ጊዜ አገልግሎት ያነጋግሩ።

የእምነትና ደህንነት ቡድናችን እርምጃ እንዲወስድ እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የሚመለከተውን ሰው ስም ወይም መገለጫ፣ እንዲሁም ተያያዥ ቀጠሮ ወይም ትዕዛዝ ካለ
2. የመልዕክቶቹን ስክሪንሾቶች ወይም የተፈጠረውን ሁኔታ ከቀናት ጋር
3. የተፈጠረበትን ቦታ (የByfluence መልዕክቶች፣ የGoogle Meet ምክክር፣ ስልክ፣ ቴሌግራም ወይም ሌላ)

ለዚህ ሰው ምላሽ መስጠት እንዲያቆሙ እና በሚቻልበት ቦታ ሁሉ እንዲያግዱት (block) እንመክራለን። ማንነትዎ ለእሱ/ለእሷ አይገለጽም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I'm sorry this happened — we take it seriously. If you're in immediate danger, contact local police now. Please send the person's name/profile, screenshots and where it happened. Stop replying and block them; your identity won't be shared. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለደረሰብዎ እናዝናለን — በቁም ነገር እናየዋለን። አስቸኳይ አደጋ ላይ ከሆኑ አሁኑኑ ፖሊስ ያነጋግሩ። እባክዎ የሰውዬውን ስም/መገለጫ፣ ስክሪንሾቶች እና የተፈጠረበትን ቦታ ይላኩ። ምላሽ መስጠት ያቁሙ፤ ያግዱት። ማንነትዎ አይገለጽም። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our Trust & Safety team has reviewed your report and is taking appropriate action. For privacy reasons we can't share details of actions on another account. If the behaviour continues or you feel unsafe, please contact us again right away.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የእምነትና ደህንነት ቡድናችን ሪፖርትዎን ገምግሞ ተገቢውን እርምጃ እየወሰደ ነው። በግላዊነት ምክንያት በሌላ መለያ ላይ ስለሚወሰዱ እርምጃዎች ዝርዝር ማካፈል አንችልም። ድርጊቱ ከቀጠለ ወይም ደህንነት ካልተሰማዎት እባክዎ ወዲያውኑ በድጋሚ ያግኙን።

## Escalation Conditions
- Every harassment report → **Trust & Safety**, priority High.
- Threats of violence, stalking, sexual exploitation, minors involved, or sharing of intimate images → **Trust & Safety** Critical **and** **Management** (`tns-threats-safety`).
- Harasser is a seller with upcoming bookings with the reporter → **Trust & Safety** + **L2** (booking handling).
- Personal data of the reporter was leaked → also `tns-privacy-complaint`.

## Resolution Procedure
1. Trust & Safety records action taken.
2. Reporter receives the closing follow-up and knows how to report again.
3. Linked bookings/refunds handled through normal processes.
4. Record harassment type and channel.

## Policy Pending Approval
- Approve the marketplace code of conduct and the actions for violations (warning, suspension, ban).
- Decide whether Byfluence offers in-platform blocking and message reporting tools.
- Decide the process for cancelling/refunding bookings where the buyer or seller was harassed.
- Approve the official emergency/support contacts agents can share.

## Internal Notes
- Believe and support; do not investigate in front of the reporter. Neutral fact-finding belongs to Trust & Safety.
- Don't tell the reported user who complained, even if they guess.
- If an agent is harassed by a customer, tell your supervisor; you can end the conversation politely after one warning.

<!-- doc -->
# Threats of Violence or Safety Emergencies
id: tns-threats-safety
type: article
category: trust-safety
subcategory: abuse
audience: both
priority: critical
department: management
tags: threat, violence, threatened to kill, safety emergency, in danger, self harm, suicide, physical threat, ዛቻ, አደጋ, ደህንነት, ራስን መጉዳት
related: tns-harassment, tns-tsg-fraud-triage, tns-report-abusive-behavior, tns-law-enforcement-request, tns-privacy-complaint
templates: tpl-escalation-notification, tpl-acknowledge-complaint
policy_pending: yes

## Summary
A customer reports a threat of violence, says they are in danger, or expresses intent to harm themselves or others. This overrides every normal process: prioritise the person's safety, direct them to emergency help, and escalate immediately to Management and Trust & Safety.

## Issue Description
Safety emergencies are rare but critical. Examples: a seller threatens to come to a buyer's home over a dispute; a buyer threatens a consultant; a delivery leads to a physical confrontation; a customer writes that they want to end their life after losing money. **Normal workflows (evidence requests, refund steps, waiting times) stop.** The agent's only goals are: encourage immediate contact with emergency services if there is imminent danger, stay calm and supportive, and get the case to Management and Trust & Safety immediately.

Approved emergency contact numbers are **not yet listed in this knowledge base**; refer to "local police or emergency services" until Management publishes the official list.

## Possible Causes
- Dispute escalation (refund, no-show, delivery) leading to threats
- Harassment that escalates to threats or stalking
- Doxxing: someone has the reporter's address or phone and threatens to use it
- In-person meeting arranged off-platform that became unsafe
- Customer in emotional crisis expressing self-harm intent
- Threats made against Byfluence staff or offices

## Information to Collect
Only what is needed to get help — do not delay for evidence:
- Is the person in immediate danger right now?
- Their general location if they need emergency help (city/area) — only if they offer it
- Who made the threat (name/profile) and how (message, call, in person)
- Screenshots of threats, if already available (later, not first)

> [!WARNING] Do not ask for passwords, OTP codes or PINs. Do not argue, investigate or ask "are you sure?" Do not promise action you cannot take (e.g., "we will send someone"). Never share the reporter's location or details with the person making the threat.

## Troubleshooting Steps
### If danger is immediate
1. Tell the person clearly to contact **local police or emergency services now**, or to go to a safe place and contact someone they trust.
2. Keep the conversation open if they want to keep talking; be calm and supportive.
3. **At the same time**, notify your supervisor and escalate to **Management** and **Trust & Safety** as **Critical** (use the fastest internal channel, not only the ticket queue).

### If the threat is serious but not immediate
1. Acknowledge, take it seriously, and advise them not to meet or engage with the person.
2. Collect the threat details and screenshots.
3. Escalate to **Trust & Safety** (Critical) and **Management**.
4. Advise them that they can report the threat to the police; Byfluence may be asked for information through official channels (see `tns-law-enforcement-request`).

### If someone expresses self-harm intent
1. Respond with care and without judgment: "I'm really sorry you're feeling this way. Your safety matters."
2. Encourage them to contact emergency services, a medical professional, or someone they trust right now.
3. Do not end the conversation abruptly. Notify your supervisor immediately and escalate to **Management**.
4. Do not discuss refunds or policies until the person is safe; the money issue can be handled later.

### Afterwards
- Record exactly what was said and done, with times.
- Any related booking with the threatening person is suspended from your side by escalation (Trust & Safety/L2 decides).
- Agents may be affected by these conversations — talk to your supervisor.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for telling us. Your safety is the most important thing right now.

If you are in immediate danger, please contact the local police or emergency services right away, or go to a safe place and contact someone you trust.

I have escalated your report to our senior management and safety team as an urgent matter. Please do not meet or reply to the person who threatened you. When you are safe, please send me any messages or screenshots of the threat.

Your case number is {{ticket_id}}. We are here to help.

{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለነገሩን እናመሰግናለን። አሁን ከሁሉም በላይ አስፈላጊው የእርስዎ ደህንነት ነው።

አሁን አስቸኳይ አደጋ ላይ ከሆኑ፣ እባክዎ ወዲያውኑ በአካባቢዎ ያለውን ፖሊስ ወይም የአስቸኳይ ጊዜ አገልግሎት ያነጋግሩ፤ ወይም ደህንነቱ ወደተጠበቀ ቦታ ሄደው የሚያምኑትን ሰው ያግኙ።

ሪፖርትዎን እንደ አስቸኳይ ጉዳይ ለከፍተኛ አመራራችን እና ለደህንነት ቡድናችን አስተላልፌዋለሁ። እባክዎ ካስፈራራዎት ሰው ጋር አይገናኙ፤ ምላሽም አይስጡ። ደህንነትዎ ከተጠበቀ በኋላ የዛቻውን መልዕክቶች ወይም ስክሪንሾቶች ይላኩልኝ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ልንረዳዎ እዚህ አለን።

{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
{{customer_name}}, your safety comes first. If you're in immediate danger, contact local police or emergency services now. I've escalated this urgently. Don't meet or reply to this person. Case: {{ticket_id}}

## Short Response (AM)
{{customer_name}}፣ ደህንነትዎ ይቀድማል። አስቸኳይ አደጋ ላይ ከሆኑ አሁኑኑ ፖሊስ ወይም የአስቸኳይ ጊዜ አገልግሎት ያነጋግሩ። ጉዳዩን በአስቸኳይ አስተላልፌዋለሁ። ከሰውዬው ጋር አይገናኙ፤ ምላሽም አይስጡ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, we are following up on case {{ticket_id}}. We hope you are safe. Our safety team is handling your report as a priority. If anything changes or you feel unsafe again, please contact us immediately — and contact the police or emergency services if you are in danger.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ጉዳይ ቁጥር {{ticket_id}}ን እየተከታተልን ነው። ደህና እንደሆኑ ተስፋ እናደርጋለን። የደህንነት ቡድናችን ሪፖርትዎን በቅድሚያ እያስተናገደ ነው። ማንኛውም ነገር ከተለወጠ ወይም በድጋሚ ደህንነት ካልተሰማዎት እባክዎ ወዲያውኑ ያግኙን — አደጋ ላይ ከሆኑም ፖሊስ ወይም የአስቸኳይ ጊዜ አገልግሎት ያነጋግሩ።

## Escalation Conditions
- Every threat of violence or safety emergency → **Management** and **Trust & Safety**, **Critical**, immediately, plus your supervisor in real time.
- Self-harm intent → supervisor immediately + **Management**.
- Threat involves a minor → **Management** + **Trust & Safety**, Critical.
- Threats against Byfluence staff/office → **Management** immediately.
- Police contact Byfluence about the case → `tns-law-enforcement-request` (Management only).

## Resolution Procedure
1. Management/Trust & Safety confirm ownership of the case.
2. Agent records a complete, timed account of the conversation.
3. Related accounts, bookings and refunds handled by the owning team.
4. Supervisor checks in with the agent after the conversation.

## Policy Pending Approval
- Publish the official emergency contacts and crisis-support resources agents may share.
- Define the internal fast-escalation channel for safety emergencies (who is on call, how to reach them out of hours).
- Decide when Byfluence proactively contacts police, and who authorises it.
- Decide account actions for users who make threats.

## Internal Notes
- Speed over completeness. Escalate first, document second.
- Do not try to verify whether the threat is "real". Treat it as real.
- Never give the threatening user any information about the reporter.
- Look after yourself: these conversations are hard. Tell your supervisor.
