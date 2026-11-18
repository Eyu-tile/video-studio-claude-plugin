<!-- doc -->
# How Customers Can Contact Support
id: gen-contact-support
type: article
category: general
subcategory: getting-help
audience: both
priority: low
department: support_l1
features: support-telegram, support-email, support-phone, support-chat, ai-assistant
tags: contact support, customer service, help, telegram support, email support, phone number, how to reach you, ድጋፍ ማግኘት, እንዴት ላገኛችሁ, የደንበኞች አገልግሎት, ስልክ ቁጥር
related: gen-report-a-problem, gen-is-byfluence-legit, acc-security-concern-phishing, gen-languages-supported, tns-report-fraud
templates: tpl-greeting-telegram
policy_pending: yes

## Summary
Which support channels customers can use, how to give them the official contact details, and how to warn them about fake "support" accounts.

## Overview
**Intended support channels:** website support, Telegram, email, telephone and (in future) an AI assistant.

| Channel | Status (see Feature Status) |
|---|---|
| Telegram | Live |
| Email | Live |
| Telephone | Not confirmed |
| Website chat | Not confirmed |
| AI assistant | Planned |

**Rules for agents:**
- Always share contact details using the **approved official values** behind `{{support_channel}}`. Never give personal phone numbers, personal Telegram accounts or personal emails.
- Do not state support hours or response times unless approved (none are confirmed yet).
- Remind customers that Byfluence support **never asks for passwords, PINs, OTP/verification codes or full card numbers**, and never asks them to pay a "fee" to receive help.
- If a customer contacted a channel that is not official, treat it as possible impersonation (acc-security-concern-phishing).
- When a customer contacts us on a new channel about an existing case, ask for the **case number** so the history stays in one ticket.

**What to include when contacting support (tell customers):** their registered email or phone, a short description, the case number if they have one, and screenshots where useful.

## Customer Steps
1. Contact Byfluence through the official channel: `{{support_channel}}`.
2. Write your registered email or phone number and a short description of the problem.
3. If you already have a case number, include it.
4. Add a screenshot if it helps explain the problem (hide any passwords, codes or card numbers).
5. Never share your password, PIN or verification codes — real Byfluence support will never ask for them.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for reaching out! You can contact Byfluence Support through our official channel: {{support_channel}}.

To help us assist you quickly, please include:
- Your registered email or phone number
- A short description of the problem
- Your case number, if you already have one
- A screenshot, if it helps (please hide any passwords, codes or card numbers)

For your safety: Byfluence Support will never ask for your password, PIN or verification codes, and will never ask you to pay to receive help. If someone does, please report it to us.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን! Byfluence ድጋፍን በይፋዊ መገናኛችን ማግኘት ይችላሉ፦ {{support_channel}}።

በፍጥነት እንድንረዳዎ እባክዎ የሚከተሉትን ያካትቱ፦
- የተመዘገቡበትን ኢሜይል ወይም ስልክ ቁጥር
- የችግሩን አጭር መግለጫ
- የጉዳይ ቁጥር ካለዎት እሱን
- የሚረዳ ከሆነ የስክሪን ፎቶ (እባክዎ የይለፍ ቃል፣ ኮድ ወይም የካርድ ቁጥር ካለበት ይሸፍኑት)

ለደህንነትዎ፦ የByfluence ድጋፍ የይለፍ ቃልዎን፣ ፒንዎን ወይም የማረጋገጫ ኮዶችን በፍጹም አይጠይቅዎትም፤ እገዛ ለማግኘት እንዲከፍሉም አይጠይቅዎትም። እንዲህ የሚጠይቅዎት ሰው ካለ እባክዎ ለእኛ ያሳውቁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! Our official support channel is {{support_channel}}. Include your registered email/phone, a short description and any case number. We never ask for passwords, PINs or codes, and never charge for help.

## Short Response (AM)
ሰላም {{customer_name}}! ይፋዊ የድጋፍ መገናኛችን {{support_channel}} ነው። የተመዘገቡበትን ኢሜይል/ስልክ፣ አጭር መግለጫ እና የጉዳይ ቁጥር ካለ ያካትቱ። የይለፍ ቃል፣ ፒን ወይም ኮድ በፍጹም አንጠይቅም፤ ለእገዛም አናስከፍልም።

## Escalation Conditions
- A customer reports a fake Byfluence support account, page or number → **Trust & Safety**.
- A customer complains they could not reach support through a channel → **Senior Support / Supervisor**.

## Policy Pending Approval
- Confirm the official support contact details for each channel (Telegram handle, email address, phone number) to fill `{{support_channel}}`.
- Confirm support hours and whether phone and website chat are available.
- Approve wording about expected response times, if any.

## Internal Notes
- Never invent a phone number, handle or hours. If you don't know the approved value, ask your supervisor.
- Impersonation of support on Telegram is a common scam pattern. Encourage customers to verify contacts through byfluence.com.

<!-- doc -->
# How Users Can Report Problems
id: gen-report-a-problem
type: article
category: general
subcategory: getting-help
audience: both
priority: medium
department: support_l1
tags: report a problem, complaint, something wrong, report issue, report seller, report bug, ችግር ሪፖርት ማድረግ, ቅሬታ, ችግር አጋጥሞኛል
related: gen-contact-support, tec-reporting-a-bug, tns-report-fraud, acc-security-concern-phishing, tec-tsg-technical-master
templates: tpl-request-screenshot, tpl-technical-investigation, tpl-greeting-telegram
policy_pending: no

## Summary
How buyers and sellers report any problem (technical, payment, seller/buyer behaviour, fraud, security) and how agents route each type.

## Overview
Customers report problems through the official support channel (`{{support_channel}}`). The agent's job is to capture the right details the first time and route the case correctly.

**What customers should send:**
- Registered email or phone number
- What happened, when (date and time) and where (which page, booking or transaction)
- Booking reference, transaction reference or seller name if relevant
- Screenshots or a short screen recording (with passwords/codes/card numbers hidden)

**Routing guide for agents:**

| Problem type | First article / team |
|---|---|
| Website/app not working | tec-tsg-technical-master → Technical |
| Payment taken, booking missing, double charge | Payments articles → Payments & Finance |
| Seller didn't show up / poor service | Consultation articles → Senior Support |
| Fraud, scam, off-platform payment request | tns-report-fraud → Trust & Safety |
| Suspicious link, account hacked | acc-security-concern-phishing → Trust & Safety |
| Abuse, harassment | Trust & Safety |
| Listing breaks rules | Seller Operations / Trust & Safety |
| Suggestion or idea | gen-suggest-feature |

**Urgency:** treat as high priority anything involving money taken, a session starting soon, account compromise, harassment or threats.

## Customer Steps
1. Contact Byfluence Support through `{{support_channel}}`.
2. Say what happened, when, and on which page/booking/transaction.
3. Add the booking or transaction reference if you have it.
4. Add a screenshot or short screen recording (hide passwords, codes and card numbers).
5. Keep your case number for follow-up.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know — I'm sorry you've run into a problem. To look into it properly, please send me:

1. What happened, and the date and time
2. Where it happened (the page, booking or transaction)
3. Any booking or transaction reference, or the seller's name
4. A screenshot or short screen recording, if possible (please hide any passwords, codes or card numbers)

Your case number is {{ticket_id}}. Please keep it for any follow-up. We will review your report and update you.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን — ችግር ስላጋጠመዎት ይቅርታ እንጠይቃለን። በአግባቡ ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦

1. ምን እንደተፈጠረ፣ ቀኑን እና ሰዓቱን
2. የት እንደተፈጠረ (ገጹን፣ ቀጠሮውን ወይም ግብይቱን)
3. የቀጠሮ ወይም የግብይት መለያ ቁጥር፣ ወይም የሻጩን ስም
4. ከተቻለ የስክሪን ፎቶ ወይም አጭር የስክሪን ቪዲዮ (እባክዎ የይለፍ ቃል፣ ኮድ ወይም የካርድ ቁጥር ካለ ይሸፍኑት)

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ለቀጣይ ክትትል እባክዎ ይያዙት። ሪፖርትዎን ገምግመን መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about this! Please send what happened (date/time), where (page/booking/transaction), any reference number, and a screenshot (hide passwords/codes). Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! እባክዎ ምን እንደተፈጠረ (ቀን/ሰዓት)፣ የት (ገጽ/ቀጠሮ/ግብይት)፣ የመለያ ቁጥር ካለ እና የስክሪን ፎቶ (የይለፍ ቃል/ኮድ ሸፍነው) ይላኩልኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: your report is being reviewed by the responsible team. We will contact you again by {{follow_up_time}}. If anything new happens, reply here with the details.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ ሪፖርትዎ በሚመለከተው ቡድን እየተገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። አዲስ ነገር ከተፈጠረ ዝርዝሩን እዚሁ ይጻፉልን።

## Escalation Conditions
- Follow the routing table above. When unsure which team owns it → **Senior Support / Supervisor**.
- Threats, harassment, fraud or account compromise → **Trust & Safety**, High.
- Repeated reports about the same seller → **Seller Operations** / **Trust & Safety**.

## Resolution Procedure
1. Confirm the reported problem is resolved or a decision has been explained to the customer.
2. Record the category, routing, actions and outcome in the ticket.

## Internal Notes
- One ticket per problem; link related tickets rather than merging different problems.
- Thank the customer for reporting — reports help protect other users.
- Never share the outcome of action against another user (e.g., "the seller was banned"); say the report was reviewed and appropriate action taken where needed.

<!-- doc -->
# How Sellers Can Grow Their Business on Byfluence
id: gen-grow-seller-business
type: article
category: general
subcategory: growth
audience: seller
priority: low
department: seller_ops
features: consultations-1on1, consultations-group, reviews-ratings
tags: grow business, more bookings, more customers, increase sales, seller tips, improve listing, get more clients, ንግዴን ማሳደግ, ብዙ ደንበኛ, ሽያጭ መጨመር
related: gen-seller-marketing-tips, gen-who-can-sell, sel-how-to-become-seller, gen-how-transactions-protected, gen-suggest-feature
templates: tpl-greeting-telegram
policy_pending: yes

## Summary
Practical, approved advice agents can give sellers who want more bookings, without promising income or results.

## Overview
Sellers often ask "How do I get more customers?". Agents can share good practice — focused on what the seller controls — but must never promise bookings, rankings, featured placement or earnings.

**1. A complete, trustworthy profile**
- Clear, real profile photo and the seller's real name or business name.
- A short bio: experience, qualifications, who they help, languages they speak.
- Completed identity verification (verified sellers build trust).

**2. Clear listings**
- Specific title (e.g., "CV review and interview coaching — 1 hour" rather than "Consulting").
- Description that explains: who it is for, what the buyer gets, what to prepare, the session length.
- Write in Amharic, English or both — whichever your buyers use.
- Fair, clear price for what is delivered. (Sellers set their own prices.)

**3. Availability that matches demand**
- Keep the calendar up to date; open times buyers can attend (e.g., evenings and weekends for working people).
- Remove times you can't keep — cancellations and no-shows damage trust quickly.

**4. Excellent delivery**
- Join Google Meet on time, prepared; test your connection beforehand.
- Deliver what the listing promised; follow up politely after the session (on the platform's channels).
- Ask satisfied buyers to recommend you (and to leave a review if reviews are available — check Feature Status).

**5. Use group consultations**
- A group session lets one expert serve many buyers at once, at a lower price per person — good for workshops and classes.

**6. Promote your Byfluence listing**
- Share your listing link on your social channels so buyers book and pay on Byfluence (see gen-seller-marketing-tips).

**7. Stay within the rules**
- Keep payments and bookings on Byfluence; follow marketplace rules and listing standards.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your question — we love helping sellers grow! Here are practical tips that make a real difference:

1. Complete your profile: a clear photo, your experience and who you help
2. Write clear listings: a specific title, what the buyer gets, and the session length
3. Keep your availability up to date, including times your buyers can attend (such as evenings or weekends)
4. Be on time and well prepared for every session — reliability builds your reputation
5. Try group consultations to reach more people at once
6. Share your Byfluence listing link on Telegram, Facebook and TikTok so buyers can book and pay safely on Byfluence

Results depend on many things, but sellers who follow these steps usually build trust faster. Would you like tips on promoting your listing on social media?

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለጥያቄዎ እናመሰግናለን — ሻጮች እንዲያድጉ መርዳት ያስደስተናል! ትልቅ ለውጥ የሚያመጡ ተግባራዊ ምክሮች እነሆ፦

1. ፕሮፋይልዎን ያጠናቅቁ፦ ግልጽ ፎቶ፣ ልምድዎን እና የሚረዷቸውን ሰዎች ይግለጹ
2. ግልጽ የአገልግሎት መግለጫ ይጻፉ፦ የተወሰነ ርዕስ፣ ገዢው የሚያገኘውን ነገር እና የምክክሩን ርዝመት
3. ክፍት ሰዓቶችዎን ሁልጊዜ ያዘምኑ፤ ደንበኞችዎ የሚመቻቸውን ሰዓት (ለምሳሌ ምሽት ወይም ቅዳሜና እሁድ) ያካትቱ
4. ለእያንዳንዱ ምክክር በሰዓቱ እና ተዘጋጅተው ይገኙ — ታማኝነት ስምዎን ይገነባል
5. ብዙ ሰዎችን በአንድ ጊዜ ለማግኘት የቡድን ምክክር ይሞክሩ
6. ገዢዎች በByfluence ላይ ደህንነቱ በተጠበቀ መንገድ እንዲያስይዙ እና እንዲከፍሉ የByfluence አገልግሎትዎን ሊንክ በTelegram፣ Facebook እና TikTok ያጋሩ

ውጤቱ በብዙ ነገሮች ይወሰናል፤ ነገር ግን እነዚህን ደረጃዎች የሚከተሉ ሻጮች በአብዛኛው እምነትን በፍጥነት ይገነባሉ። አገልግሎትዎን በማህበራዊ ሚዲያ ስለማስተዋወቅ ምክር ይፈልጋሉ?

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! Top tips: complete your profile, write clear listings (specific title, what buyers get, session length), keep availability updated, always be on time, try group sessions, and share your listing link on Telegram/Facebook/TikTok. Want marketing tips too?

## Short Response (AM)
ሰላም {{customer_name}}! ዋና ምክሮች፦ ፕሮፋይልዎን ያጠናቅቁ፣ ግልጽ የአገልግሎት መግለጫ ይጻፉ (ርዕስ፣ ገዢው የሚያገኘው፣ የምክክሩ ርዝመት)፣ ክፍት ሰዓቶችን ያዘምኑ፣ ሁልጊዜ በሰዓቱ ይገኙ፣ የቡድን ምክክር ይሞክሩ፣ ሊንክዎንም በTelegram/Facebook/TikTok ያጋሩ። የማስተዋወቂያ ምክርም ይፈልጋሉ?

## Escalation Conditions
- A seller asks for featured placement, promotion programmes or special visibility → **Seller Operations**.
- A seller's listing is hidden, rejected or not appearing in search → **Seller Operations** (and Technical if it looks like a bug).
- A seller asks for business coaching beyond support's scope → note the request as feedback (gen-suggest-feature).

## Policy Pending Approval
- Confirm whether Byfluence offers seller promotion features (featured listings, badges, ranking factors) and what may be said about how search ranking works.
- Confirm whether buyer reviews/ratings are live and how sellers can request them.
- Confirm whether Byfluence offers seller training or onboarding sessions.

## Internal Notes
- Never promise that following tips will bring bookings or a certain income.
- Never explain search ranking unless the rules are approved.
- Encourage reliability above all — seller no-shows are a top cause of complaints.

<!-- doc -->
# Practical Marketing Tips for New Sellers (Telegram, TikTok, Facebook, Referrals)
id: gen-seller-marketing-tips
type: article
category: general
subcategory: growth
audience: seller
priority: low
department: seller_ops
tags: marketing tips, promote listing, telegram marketing, tiktok, facebook, referrals, social media, share link, ማስተዋወቅ, ቴሌግራም, ቲክቶክ, ፌስቡክ, ማስታወቂያ
related: gen-grow-seller-business, gen-who-can-sell, gen-how-transactions-protected, tns-report-fraud, gen-is-byfluence-legit
templates: tpl-greeting-telegram
policy_pending: yes

## Summary
Simple, low-cost ways new sellers can bring buyers to their Byfluence listings using Telegram, TikTok, Facebook and word of mouth — while keeping bookings and payments on Byfluence.

## Overview
Most new sellers have no marketing budget. These tips need only a phone and time. Agents can share them freely; they are general good practice, not Byfluence promises.

### Golden rule
Always send people to your **Byfluence listing link** to book and pay. This keeps buyers protected and keeps your bookings, payments and earnings recorded. Never ask buyers to pay you directly.

### Telegram
- Create a **channel** for your expertise (e.g., tips on CVs, nutrition, business, language learning) and post useful short tips regularly.
- Pin a message with your Byfluence listing link and how to book.
- Share in relevant **groups** only where the group rules allow promotion; give value first (answer questions), don't spam.
- Write in Amharic (and English if your audience uses it); keep posts short and clear.

### TikTok
- Post short videos (one tip per video) showing your expertise and personality.
- Speak simply, add Amharic captions, and end with: "Book a session with me on Byfluence — link in my profile."
- Put your Byfluence listing link in your profile bio.
- Post consistently; reply to comments with helpful answers.

### Facebook
- Use a **Page** for your service; post tips, short videos and announcements of new session times or group workshops.
- Share in community groups where allowed (professional, student, business groups).
- Use the Page's "About" section and pinned post for your Byfluence link.

### Referrals and word of mouth
- Ask satisfied buyers to recommend you to friends and colleagues and share your link.
- Tell your existing clients, colleagues, alumni and community groups that they can now book you on Byfluence.
- Offer group sessions or workshops that participants can invite friends to.

### Content ideas
- "3 mistakes people make when…"
- Short answers to common questions you get
- Before/after examples (with permission and without personal data)
- Announce your available times or an upcoming group session

### Avoid
- Fake followers, fake reviews or fake testimonials.
- Exaggerated claims ("guaranteed job", "guaranteed income", medical cures).
- Using Byfluence's name or logo as if you were Byfluence itself, or claiming to be an official partner.
- Spamming groups or private messages.
- Sharing buyers' personal details or screenshots without permission.

## Recommended Response (EN)
Hello {{customer_name}},

Great that you want to promote your services! Here are simple tips that cost little more than your time:

1. Telegram: create a channel with short, useful tips in your field, and keep your Byfluence listing link as a pinned message
2. TikTok: post short videos (one tip per video) with Amharic captions, and put your Byfluence link in your profile
3. Facebook: use a Page to share tips and new session times, and post in groups where promotion is allowed
4. Word of mouth: ask happy clients to recommend you and share your link

Always send people to your Byfluence listing to book and pay — this protects your buyers and keeps your bookings and earnings recorded. Please avoid fake reviews, spam and big promises like "guaranteed results".

Good luck — we're happy to help if you have questions.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

አገልግሎትዎን ማስተዋወቅ መፈለግዎ ጥሩ ነው! ከጊዜዎ በስተቀር ብዙ ወጪ የማይጠይቁ ቀላል ምክሮች እነሆ፦

1. Telegram፦ በሙያዎ ላይ አጫጭር እና ጠቃሚ ምክሮችን የሚያጋሩበት ቻናል ይክፈቱ፤ የByfluence አገልግሎትዎን ሊንክ ፒን (pin) ያድርጉ
2. TikTok፦ አጫጭር ቪዲዮዎችን (በአንድ ቪዲዮ አንድ ምክር) በአማርኛ ጽሑፍ (caption) ይለጥፉ፤ የByfluence ሊንክዎን በፕሮፋይልዎ ላይ ያስቀምጡ
3. Facebook፦ ምክሮችን እና አዳዲስ የምክክር ሰዓቶችን ለማጋራት ፔጅ (Page) ይጠቀሙ፤ ማስተዋወቅ በሚፈቀድባቸው ግሩፖች ውስጥ ይለጥፉ
4. ከአፍ ወደ አፍ፦ የረኩ ደንበኞችዎ እንዲጠቁሙዎት እና ሊንክዎን እንዲያጋሩ ይጠይቁ

ሰዎች ቀጠሮ እንዲያስይዙ እና እንዲከፍሉ ሁልጊዜ ወደ Byfluence አገልግሎትዎ ሊንክ ይምሯቸው — ይህ ገዢዎችዎን ይጠብቃል፤ ቀጠሮዎችዎ እና ገቢዎም ይመዘገባሉ። እባክዎ የውሸት አስተያየቶችን (reviews)፣ አላስፈላጊ መልዕክቶችን (spam) እና "ውጤት የተረጋገጠ" የመሳሰሉ ትልልቅ ቃል ኪዳኖችን ያስወግዱ።

መልካም ዕድል — ጥያቄ ካለዎት ለመርዳት ዝግጁ ነን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! Try: a Telegram channel with useful tips + pinned Byfluence link; short TikTok tips with Amharic captions + link in bio; a Facebook Page and relevant groups; and referrals from happy clients. Always send buyers to your Byfluence link to book and pay.

## Short Response (AM)
ሰላም {{customer_name}}! ይሞክሩ፦ ጠቃሚ ምክሮች ያሉት የTelegram ቻናል + ፒን የተደረገ የByfluence ሊንክ፤ በአማርኛ caption አጫጭር የTikTok ምክሮች + ሊንክ በፕሮፋይል፤ የFacebook ፔጅ እና ተዛማጅ ግሩፖች፤ ከረኩ ደንበኞች የሚመጡ ጥቆማዎች። ገዢዎችን ሁልጊዜ ለማስያዝ እና ለመክፈል ወደ Byfluence ሊንክዎ ይምሩ።

## Escalation Conditions
- A seller wants to use Byfluence's logo/brand in their promotion or asks for co-marketing → **Seller Operations** (brand approval).
- A seller is found promoting off-platform payment, fake reviews or misleading claims → **Seller Operations** / **Trust & Safety**.
- A seller asks about paid advertising on Byfluence → **Seller Operations**.

## Policy Pending Approval
- Confirm the rules for sellers using the Byfluence name and logo in their own marketing.
- Confirm whether Byfluence runs any referral or affiliate programme for sellers or buyers.

## Internal Notes
- These are general tips, not guarantees. Never suggest a seller will earn a specific amount.
- If a seller's promotion makes medical, legal or financial guarantees, flag it to Seller Operations.
- Do not recommend buying followers, paid "growth" services or third-party tools.

<!-- doc -->
# Suggesting New Features
id: gen-suggest-feature
type: article
category: general
subcategory: feedback
audience: both
priority: low
department: support_l2
tags: feature request, suggestion, idea, feedback, improve byfluence, wish list, I want, ሀሳብ, አስተያየት, ጥቆማ, ማሻሻያ
related: gen-report-a-problem, gen-grow-seller-business, tec-reporting-a-bug, gen-contact-support
templates: tpl-greeting-telegram
policy_pending: yes

## Summary
How to receive and record customer ideas and feature requests so they reach the product team, without promising they will be built.

## Overview
Customer suggestions are valuable — especially for an MVP marketplace. Typical requests: a mobile app, more payment methods, delivery to more cities, Afaan Oromo/Tigrinya support, reviews, reminders by SMS, seller analytics.

**Agent workflow:**
1. Thank the customer and make sure you understand the idea: *what* they want, *why* (the problem it solves), and *who* it helps (buyers, sellers).
2. Check whether it's actually a **bug** (something that should already work) → tec-reporting-a-bug instead.
3. Check Feature Status: if the feature is already **planned** (e.g., physical products, digital products), you may say it is being worked on — but never give a date.
4. Record it in the ticket with the tag **feature-request** and a one-line summary, using the customer's words where helpful.
5. Forward according to your team's process (supervisor collects and shares with the product team).
6. Close the ticket after thanking them — no follow-up is promised unless approved.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you so much for your suggestion! Ideas from our users help us decide how to improve Byfluence.

I have recorded your idea and shared it with our team. While I can't promise if or when it will be added, every suggestion is reviewed. Your reference number is {{ticket_id}}.

If you have more details — such as how this would help you — feel free to reply here.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለሰጡን ሀሳብ በጣም እናመሰግናለን! ከተጠቃሚዎቻችን የሚመጡ ሀሳቦች Byfluenceን እንዴት ማሻሻል እንዳለብን ለመወሰን ይረዱናል።

ሀሳብዎን መዝግቤ ለቡድናችን አጋርቻለሁ። ሀሳቡ ስለመጨመሩ ወይም መቼ እንደሚጨመር ቃል መግባት ባልችልም፣ እያንዳንዱ ጥቆማ ይገመገማል። የመለያ ቁጥርዎ {{ticket_id}} ነው።

ተጨማሪ ዝርዝር ካለዎት — ለምሳሌ ይህ እንዴት እንደሚረዳዎት — እዚሁ ሊጽፉልን ይችላሉ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Thank you {{customer_name}}! I've recorded your idea and shared it with our team. I can't promise if or when it will be added, but every suggestion is reviewed. Ref: {{ticket_id}}

## Short Response (AM)
እናመሰግናለን {{customer_name}}! ሀሳብዎን መዝግቤ ለቡድናችን አጋርቻለሁ። ሀሳቡ ስለመጨመሩ ወይም መቼ እንደሚጨመር ቃል መግባት ባልችልም እያንዳንዱ ጥቆማ ይገመገማል። መለያ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- The "suggestion" is really a bug or broken feature → **Technical / Engineering** via tec-reporting-a-bug.
- Many customers asking for the same thing in a short period → tell **Senior Support / Supervisor** (possible product priority).
- A business proposing to build or provide a feature → gen-partnership-inquiries.

## Policy Pending Approval
- Confirm how feature requests are collected and passed to the product team, and whether customers are ever notified when a requested feature launches.

## Internal Notes
- Never say "we will add it soon" or "it's coming next month".
- Group similar requests under one clear summary so management can count demand.
- A suggestion about a planned feature is still worth recording — it shows demand.

<!-- doc -->
# Partnership and Supplier Inquiries
id: gen-partnership-inquiries
type: article
category: general
subcategory: feedback
audience: internal
priority: medium
department: management
features: inventory-free-selling, physical-products, delivery-addis
tags: partnership, supplier, wholesale, business proposal, collaboration, delivery partner, investor, sponsor, አጋርነት, አቅራቢ, የንግድ ሀሳብ, ትብብር
related: inv-how-it-works, gen-who-can-sell, gen-media-inquiries, gen-suggest-feature, gen-how-byfluence-earns
templates: tpl-greeting-telegram
policy_pending: yes

## Summary
How to handle businesses and individuals proposing partnerships — suppliers, delivery companies, payment companies, institutions, sponsors or investors — without making commitments.

## Overview
Byfluence plans to partner with **suppliers** and verified sellers for inventory-free selling, and will need **delivery/fulfilment partners** for physical products. Support may receive proposals from:
- Suppliers/wholesalers wanting their products resold on Byfluence
- Delivery or logistics companies
- Payment providers, banks, fintechs
- Training institutions, NGOs, universities, associations
- Sponsors, advertisers and investors

**Agent workflow:**
1. Thank them and collect: organisation name, contact person and role, official email/phone, type of partnership, a short description of the proposal, and their location.
2. Do **not** discuss commercial terms, commissions, pricing, exclusivity, volumes, timelines or internal plans.
3. Do **not** sign, accept or forward NDAs, contracts or forms; do not open unknown attachments or links (possible phishing) — forward per security process.
4. Create a ticket tagged **partnership** with the details and route it: suppliers/resellers → **Seller Operations**; delivery, payments, investors, sponsors, institutions → **Management** (via supervisor).
5. Reply with the acknowledgement message. No promise of a reply is made unless approved.

If the person actually wants to **sell as an individual seller**, guide them to gen-who-can-sell / sel-how-to-become-seller instead.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your interest in partnering with Byfluence.

So that the right team can review your proposal, please share:
1. Your organisation's name and your role
2. Official contact email and phone number
3. The type of partnership you are proposing (for example: supplier, delivery, payments, training)
4. A short description of your proposal

I will pass your details to the responsible team. Please note that I am not able to discuss commercial terms, and sharing your proposal does not create any agreement. Your reference number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ከByfluence ጋር በአጋርነት ለመስራት ስላሳዩት ፍላጎት እናመሰግናለን።

የሚመለከተው ቡድን ሀሳብዎን እንዲገመግም እባክዎ የሚከተሉትን ያጋሩን፦
1. የድርጅትዎን ስም እና የእርስዎን ኃላፊነት
2. ይፋዊ የኢሜይል አድራሻ እና ስልክ ቁጥር
3. ያቀረቡትን የአጋርነት ዓይነት (ለምሳሌ፦ አቅራቢ፣ ማድረስ/delivery፣ ክፍያ፣ ስልጠና)
4. የሀሳብዎን አጭር መግለጫ

መረጃዎን ለሚመለከተው ቡድን አስተላልፋለሁ። እባክዎ ልብ ይበሉ፦ ስለ ንግድ ውሎች መወያየት አልችልም፤ ሀሳብዎን ማጋራትም ምንም ዓይነት ስምምነት አይፈጥርም። የመለያ ቁጥርዎ {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Thank you {{customer_name}}! Please send your organisation name, your role, official contact details, the partnership type and a short description. I'll pass it to the right team (this doesn't create any agreement). Ref: {{ticket_id}}

## Short Response (AM)
እናመሰግናለን {{customer_name}}! እባክዎ የድርጅትዎን ስም፣ ኃላፊነትዎን፣ ይፋዊ አድራሻዎን፣ የአጋርነቱን ዓይነት እና አጭር መግለጫ ይላኩ። ለሚመለከተው ቡድን አስተላልፋለሁ (ይህ ምንም ስምምነት አይፈጥርም)። መለያ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Supplier/reseller proposals → **Seller Operations**.
- Delivery, payment, investor, sponsor, institutional or government proposals → **Management**.
- Suspicious proposals (requests for money, unusual attachments/links, pressure) → **Trust & Safety**.

## Policy Pending Approval
- Confirm the official partnership contact/owner for each type of proposal and whether support should share a dedicated partnerships email.
- Confirm supplier eligibility for inventory-free selling, once the programme is defined.

## Internal Notes
- Never confirm that Byfluence "is looking for" a specific partner type or discuss internal plans.
- Investors and journalists sometimes present as "partners" — if the questions are about company finances or strategy, route to Management.

<!-- doc -->
# Media and Press Inquiries
id: gen-media-inquiries
type: article
category: general
subcategory: feedback
audience: internal
priority: medium
department: management
tags: media, press, journalist, interview, news, blogger, podcast, statement, comment, ሚዲያ, ጋዜጠኛ, ቃለ መጠይቅ, ዜና
related: gen-partnership-inquiries, gen-what-is-byfluence, tec-known-outage-handling, gen-is-byfluence-legit
templates: tpl-greeting-telegram
policy_pending: yes

## Summary
Support agents do not speak to the media on Byfluence's behalf; they collect the request and route it to Management.

## Overview
Journalists, bloggers, podcasters, YouTubers and influencers may contact support for interviews, comments, statistics or reactions (for example, during an outage or after a public complaint).

**Rules:**
- Agents **never** give statements, opinions, numbers (users, sellers, revenue), or comments "off the record" — even friendly or informal ones.
- Agents do not confirm or deny incidents, disputes or details about any user.
- Collect: name, outlet/channel, contact details, topic and questions, and their deadline.
- Create a ticket tagged **media** and route to **Management** via supervisor immediately — media deadlines can be short.
- If a journalist is also a customer with a personal issue, handle the personal issue normally but do not comment on anything else.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your interest in Byfluence.

Media and press requests are handled by our management team. Please share your name, your media outlet or channel, your contact details, the topic or questions, and your deadline, and I will forward them right away.

Your reference number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ለByfluence ስላሳዩት ፍላጎት እናመሰግናለን።

የሚዲያ እና የፕሬስ ጥያቄዎች የሚስተናገዱት በማኔጅመንት ቡድናችን ነው። እባክዎ ስምዎን፣ የሚዲያ ተቋምዎን ወይም ቻናልዎን፣ አድራሻዎን፣ ርዕሱን ወይም ጥያቄዎቹን እና የጊዜ ገደብዎን ያጋሩኝ፤ ወዲያውኑ አስተላልፋለሁ።

የመለያ ቁጥርዎ {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for reaching out! Media requests are handled by our management team. Please send your name, outlet, contact details, topic/questions and deadline, and I'll forward them right away. Ref: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላገኙን እናመሰግናለን! የሚዲያ ጥያቄዎች የሚስተናገዱት በማኔጅመንት ቡድናችን ነው። እባክዎ ስምዎን፣ ተቋምዎን፣ አድራሻዎን፣ ርዕሱን/ጥያቄዎቹን እና የጊዜ ገደቡን ይላኩ፤ ወዲያውኑ አስተላልፋለሁ። መለያ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Every media or press request → **Management**, via supervisor, same shift.
- Media asking about a security incident, fraud case or specific user → **Management** and **Trust & Safety**.

## Policy Pending Approval
- Confirm the official media spokesperson/contact and whether a press email should be shared with journalists.

## Internal Notes
- "Just one quick comment" is still a statement. Politely decline and route.
- Influencers offering promotion deals are partnership/marketing inquiries — route via gen-partnership-inquiries.
- Never share screenshots of internal tools or conversations with anyone outside Byfluence.

<!-- doc -->
# Job and Internship Inquiries
id: gen-job-inquiries
type: article
category: general
subcategory: feedback
audience: internal
priority: low
department: management
tags: job, vacancy, internship, career, hiring, work at byfluence, cv, apply for job, ስራ, ክፍት የስራ ቦታ, ልምምድ, ኢንተርንሺፕ, ሲቪ
related: gen-contact-support, gen-is-byfluence-legit, tns-report-fraud, gen-who-can-sell, gen-partnership-inquiries
templates: tpl-greeting-telegram
policy_pending: yes

## Summary
How to respond to people asking about jobs or internships at Byfluence, and how to protect them from fake job offers.

## Overview
People may ask support about vacancies, internships, volunteering or "working with Byfluence". Some confuse **working for Byfluence** (employment) with **earning on Byfluence** (becoming a seller).

**Agent workflow:**
1. Clarify what they want: a job/internship **at Byfluence**, or to **earn as a seller**? If seller → gen-who-can-sell.
2. Do not confirm or deny open positions, salaries, or hiring timelines unless an approved announcement exists.
3. Do not accept CVs or documents through support channels unless an approved process exists — CVs contain personal data.
4. Share the official careers information if approved; otherwise record the request (tag **job-inquiry**) and forward per team process.
5. **Scam warning:** if they mention a job offer "from Byfluence" that asks for payment, documents, or contact through an unofficial account, treat it as a possible scam → Trust & Safety.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your interest in working with Byfluence!

I'm not able to share information about vacancies through support, but I have recorded your interest and passed it to the right team. Any official opportunities will be shared through Byfluence's official channels.

Please be careful: if anyone offers you a job "from Byfluence" and asks you to pay money or send personal documents through an unofficial account, please do not pay and tell us right away.

If you are interested in earning by offering your services on Byfluence as a seller, I'd be happy to explain how. Your reference number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ከByfluence ጋር ለመስራት ስላሳዩት ፍላጎት እናመሰግናለን!

ስለ ክፍት የስራ ቦታዎች መረጃ በድጋፍ መስመር በኩል ማጋራት አልችልም፤ ነገር ግን ፍላጎትዎን መዝግቤ ለሚመለከተው ቡድን አስተላልፌዋለሁ። ይፋዊ የስራ ዕድሎች ካሉ በByfluence ይፋዊ መገናኛዎች ይገለጻሉ።

እባክዎ ይጠንቀቁ፦ ማንም ሰው "ከByfluence" ነው በሚል የስራ ዕድል አቅርቦልዎ ገንዘብ እንዲከፍሉ ወይም የግል ሰነዶችዎን ይፋዊ ባልሆነ አካውንት እንዲልኩ ከጠየቀዎት፣ እባክዎ አይክፈሉ፤ ወዲያውኑም ያሳውቁን።

አገልግሎትዎን በByfluence ላይ እንደ ሻጭ በማቅረብ ገቢ ማግኘት ከፈለጉ፣ እንዴት እንደሆነ ላስረዳዎ ደስተኛ ነኝ። የመለያ ቁጥርዎ {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for your interest! I've passed it to the right team; official opportunities are shared through Byfluence's official channels. Never pay anyone for a "Byfluence job". Want to earn as a seller instead? I can explain. Ref: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለፍላጎትዎ እናመሰግናለን! ለሚመለከተው ቡድን አስተላልፌዋለሁ፤ ይፋዊ የስራ ዕድሎች በByfluence ይፋዊ መገናኛዎች ይገለጻሉ። ለ"Byfluence ስራ" ለማንም አይክፈሉ። እንደ ሻጭ ገቢ ማግኘት ይፈልጋሉ? ላስረዳዎ እችላለሁ። መለያ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Reports of fake Byfluence job offers or recruitment scams → **Trust & Safety**, High.
- Requests from universities or institutions for internship programmes → **Management** (gen-partnership-inquiries).

## Policy Pending Approval
- Confirm the official careers channel (page, email) support may share, and whether support should accept CVs.
- Confirm whether Byfluence offers internships or volunteer programmes.

## Internal Notes
- Fake job offers using a company's name are a common scam; take reports seriously and collect the scammer's account/number for Trust & Safety.
- Do not discuss team size, salaries or internal structure.
