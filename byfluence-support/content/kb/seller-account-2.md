<!-- doc -->
# Master Guide: Seller Onboarding & Verification Problems
id: sel-tsg-verification-master
type: troubleshooting
category: seller-account
subcategory: verification
audience: seller
priority: medium
department: seller_ops
features: seller-onboarding, seller-verification
tags: seller onboarding problem, verification problem, cannot become seller, seller application issue, verification troubleshooting, seller status, የሻጭ ምዝገባ ችግር, ማረጋገጫ ችግር, ሻጭ መሆን አልቻልኩም
related: sel-verification-pending-long, sel-verification-rejected, sel-resubmit-documents, sel-verified-but-cannot-sell, sel-id-documents-sent-in-chat, sel-account-restrictions
templates: tpl-seller-verification-pending, tpl-seller-verification-rejected, tpl-seller-docs-resubmit, tpl-seller-suspension-notice
policy_pending: yes

## Summary
A diagnostic playbook for any seller who says "I can't become a seller", "my verification is stuck" or "I'm verified but can't sell". It routes the agent to the right article in a few decisions.

## Overview
Seller onboarding problems almost always fall into one of five buckets: **not started**, **not finished**, **waiting**, **decided (rejected)**, or **verified but blocked**. The key skill is reading **two separate statuses**:

| Verification status | Operational status | Meaning |
|---|---|---|
| (none) | — | No seller application recorded |
| Pending | — / Active | Application in review |
| Rejected | — | Not approved; resubmission may be possible |
| Verified | Active | Can sell (if profile/listings complete and approved) |
| Verified | Suspended | Identity confirmed, but selling is blocked |
| Verified / any | Banned | Permanently removed from selling |

> [!WARNING] Agents never approve, reject, re-review or "speed up" verification. Only **Seller Operations** decides. Agents never collect ID documents in chat — the platform verification flow is the only accepted channel.

> [!POLICY] The official rule on document channels, review targets and resubmission limits is pending approval. Until approved: platform only, no promised dates, escalate disputes.

## Information to Collect
- Registered email or phone number of the seller account
- What they see on screen (status, error) — screenshot without any ID document
- Approximate date they applied / last resubmitted
- Device and browser/app if something "doesn't work"
- What they are trying to do (apply, upload, create listing, accept booking)

> [!WARNING] Never ask for passwords, OTP codes, PINs or ID numbers.

## Troubleshooting Steps
### Step 1 — Confirm identity and find the account
1. Match the contact details to an account in the admin dashboard (if you have access). If you lack access → **Senior Support / Supervisor**.
2. Multiple accounts? Identify which one holds the seller application. Note any duplicates for Seller Operations.

### Step 2 — Is there a seller application?
- **No application** → Did they start it? Guide them through `sel-seller-registration-steps`. If they insist they submitted → **Technical / Engineering**.
- **Application started but not submitted** (missing documents or final submit) → guide them to finish on the platform.
- **Application submitted** → go to Step 3.

### Step 3 — Read the verification status
- **Pending** → `sel-verification-pending-long`. Check for any "more information requested" note → `sel-resubmit-documents`.
- **Rejected** → `sel-verification-rejected`. Fixable reason → resubmit. Fraud/risk reason → neutral wording, **Trust & Safety** if disputed.
- **Verified** → go to Step 4.

### Step 4 — Read the operational status
- **Active** → go to Step 5.
- **Suspended** → `sel-suspension`. Do not discuss reasons beyond what is recorded as shareable.
- **Banned** → `sel-banned`. Never share fraud-related details.
- **Restricted (partial limits)** → `sel-account-restrictions`.

### Step 5 — Verified + Active but still cannot sell
Follow `sel-verified-but-cannot-sell`: profile incomplete, listings under review/rejected, selling permissions not granted yet, payout details missing, technical issue.

### Step 6 — Special situations
- ID sent in chat → `sel-id-documents-sent-in-chat` (stop, do not use the document).
- Applicant may be a minor, previously banned, or offering regulated advice → **Seller Operations** (see `sel-who-can-sell`).
- Same document on several accounts, edited-looking documents, applicant pressured by "an agent" to pay a fee for approval → **Trust & Safety**, priority High.
- Several sellers report the same problem at once → possible incident: alert your supervisor and check Announcements.

### Step 7 — Record
- [ ] Both statuses written in the ticket ("Verification: X / Operational: Y")
- [ ] Bucket identified (not started / not finished / waiting / rejected / blocked)
- [ ] Article followed and customer informed
- [ ] Escalation made with all collected details

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry you're having trouble setting up your seller account — I'll help you find out what's happening.

I have checked your account. [Explain the status in simple words and the next step, e.g. "Your application is under review by our Seller Operations team" / "Your verification needs a clearer document photo" / "Your account is verified, and your first listing is waiting for review".]

Please remember: documents are only accepted through the verification page in your Byfluence account — never by chat — and we will never ask for your password or verification codes.

Your case number is {{ticket_id}}. I'll keep you updated.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የሻጭ መለያዎን ለማዘጋጀት ችግር ስላጋጠመዎት ይቅርታ እንጠይቃለን — ምን እየሆነ እንዳለ እንድናውቅ እረዳዎታለሁ።

መለያዎን አይቻለሁ። [ሁኔታውን እና ቀጣዩን እርምጃ በቀላል ቋንቋ ያብራሩ፤ ለምሳሌ "ማመልከቻዎ በሻጭ ኦፕሬሽንስ ቡድናችን እየተገመገመ ነው" / "ማረጋገጫዎ የበለጠ ግልጽ የሰነድ ፎቶ ይፈልጋል" / "መለያዎ ተረጋግጧል፤ የመጀመሪያ ዝርዝርዎ ግምገማ እየጠበቀ ነው"።]

እባክዎ ያስታውሱ፦ ሰነዶች የሚቀበሉት በByfluence መለያዎ ውስጥ ባለው የማረጋገጫ ገጽ ብቻ ነው — በቻት አይደለም — እንዲሁም የይለፍ ቃልዎን ወይም የማረጋገጫ ኮዶችን በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Escalation Conditions
- Verification decisions, re-reviews, aged applications, resubmission permission → **Seller Operations**.
- Platform errors (upload, submit, status not updating) → **Technical / Engineering**.
- Fraud signals, impersonation, ID exposure, banned identity → **Trust & Safety**, priority High.
- Agent lacks access, seller is distressed/aggressive or the case has been reopened repeatedly → **Senior Support / Supervisor**.
- Legal threats or media → **Senior Support / Supervisor** → **Management**.

## Policy Pending Approval
- Approve official accepted documents, review targets and customer-facing wait wording.
- Approve resubmission limits and the appeal process.
- Approve the "platform-only" rule for identity documents and the procedure for documents received elsewhere.
- Define what reasons can be shared for rejection, restriction, suspension and ban.

## Internal Notes
- The single most common mistake is answering from the verification status alone. "Verified" does not mean "can sell".
- Any message claiming a "fee to speed up verification" is a scam signal — Byfluence has no confirmed such fee. Report to Trust & Safety.

<!-- doc -->
# Verified but Cannot Create Listings or Sell
id: sel-verified-but-cannot-sell
type: article
category: seller-account
subcategory: seller-status
audience: seller
priority: medium
department: seller_ops
features: seller-onboarding, seller-verification
tags: verified but cannot sell, cannot create listing, no sell button, listing button missing, approved but not selling, seller permissions, ተረጋግጧል ግን መሸጥ አልቻልኩም, ዝርዝር መፍጠር አልቻልኩም
related: sel-tsg-verification-master, sel-account-restrictions, sel-suspension, lst-create-listing, lst-listing-under-review, sel-dashboard-overview
templates: tpl-seller-suspension-notice
policy_pending: yes

## Summary
The seller's identity is verified, but they cannot create listings, cannot publish them, or cannot receive bookings.

## Issue Description
The seller sees **Verified** and expects to start selling immediately. Instead the create-listing option is missing or disabled, listings stay unpublished, or buyers cannot book. Because verification and operational status are separate, a verified seller can still be suspended or restricted. Other causes are incomplete setup (profile, payout details), listings stuck in review, selling permissions not yet granted, or a technical problem.

## Possible Causes
- Operational status is **Suspended**, **Banned** or **restricted** (separate from verification).
- Selling permissions have not yet been granted after verification.
- Seller profile is incomplete (required fields, photo, description).
- Payout/withdrawal details not set up (if required before selling — not confirmed).
- Listing created but **under review** or **rejected**.
- Listing published but no availability set, so buyers cannot book.
- Seller is signed in to a different (buyer) account.
- Technical issue (page error, button not loading, app cache).
- Trying to create a listing type that is not live yet (physical, digital, inventory-free).

## Information to Collect
- Registered email or phone of the seller account
- What exactly fails: no button / button disabled / error message / listing not visible / no bookings
- Screenshot of the screen or error
- Listing title (if one exists)
- Device and browser/app

## Troubleshooting Steps
1. Confirm identity and the correct account.
2. Check both statuses through authorized tools (admin dashboard, if you have access): **verification** and **operational**.
3. Decide the case:
   - **Suspended / Banned** → follow `sel-suspension` / `sel-banned`.
   - **Restricted** → follow `sel-account-restrictions`.
   - **Verified + Active, permissions not granted** → escalate to **Seller Operations** to confirm whether selling permissions are pending.
   - **Profile incomplete** → guide them to complete required profile fields (`sel-profile-management`).
   - **Listing under review / rejected** → `lst-listing-under-review` / `lst-listing-rejected`.
   - **Listing live but buyers cannot book** → check availability (`lst-availability-calendar`, `con-seller-availability-setup`) and visibility (`lst-listing-not-visible`).
   - **Wrong account** → help them sign in to the seller account.
   - **Planned product type** → check **Feature Status**; if not live, explain it is not available yet without giving dates.
   - **Everything looks correct** → basic technical steps (refresh, sign out/in, another browser, update app), then **Technical / Engineering**.
4. Note both statuses and the cause in the ticket.

- [ ] Verification and operational status checked
- [ ] Profile and listing state checked
- [ ] Cause identified or escalated

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and congratulations on being verified! I understand you are not yet able to [create a listing / start selling].

I have checked your account. [Explain the cause, e.g. "Your seller profile is missing some required information" / "Your first listing is still being reviewed" / "Your selling permissions are still being set up by our Seller Operations team".]

Next step: [clear instruction, e.g. "Please open your seller profile and complete the missing fields, then try creating your listing again."]

Your case number is {{ticket_id}}. I'll stay with you until this is sorted.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ ማንነትዎ በመረጋገጡም እንኳን ደስ አለዎት! እስካሁን [ዝርዝር መፍጠር / መሸጥ መጀመር] እንዳልቻሉ ተረድቻለሁ።

መለያዎን አይቻለሁ። [ምክንያቱን ያብራሩ፤ ለምሳሌ "የሻጭ መገለጫዎ አንዳንድ አስፈላጊ መረጃዎች ይጎድሉታል" / "የመጀመሪያ ዝርዝርዎ አሁንም እየተገመገመ ነው" / "የመሸጥ ፈቃድዎ በሻጭ ኦፕሬሽንስ ቡድናችን እየተዘጋጀ ነው"።]

ቀጣይ እርምጃ፦ [ግልጽ መመሪያ፤ ለምሳሌ "እባክዎ የሻጭ መገለጫዎን ከፍተው የጎደሉትን መስኮች ይሙሉ፣ ከዚያ ዝርዝርዎን እንደገና ለመፍጠር ይሞክሩ።"]

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ይህ እስኪስተካከል ድረስ አብሬዎት እሆናለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, congrats on being verified! I checked your account: [cause]. Next step: [action]. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ማንነትዎ በመረጋገጡ እንኳን ደስ አለዎት! መለያዎን አይቻለሁ፦ [ምክንያት]። ቀጣይ እርምጃ፦ [እርምጃ]። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our team is still working on enabling selling on your account. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። በመለያዎ ላይ መሸጥ እንዲችሉ ቡድናችን አሁንም እየሰራ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Verified + Active + profile complete, but selling still blocked → **Seller Operations**, priority Medium.
- Error messages or missing buttons after basic troubleshooting → **Technical / Engineering**.
- Seller has buyers waiting/booked and cannot deliver → raise priority to High and notify **Senior Support / Supervisor**.
- Account shows suspension the seller did not know about → follow `sel-suspension`.

## Resolution Procedure
1. Seller can create a listing (or the listing is live) and the seller confirms.
2. Record statuses, cause and action in the ticket before resolving.

## Policy Pending Approval
- Confirm whether selling permissions are granted automatically at verification or separately.
- Confirm whether payout details or a complete profile are mandatory before listing.
- Confirm which listing types each seller can create at MVP stage.

## Internal Notes
- Always write "Verification: Verified / Operational: X" in the ticket — this is the first thing the next agent needs.
- Don't send the "congratulations" line if the account is suspended or banned — use those articles' wording instead.

<!-- doc -->
# Seller Account Restrictions Explained
id: sel-account-restrictions
type: article
category: seller-account
subcategory: seller-status
audience: seller
priority: medium
department: seller_ops
features: seller-onboarding
tags: account restricted, seller limited, cannot publish, limits on account, seller restriction, payout hold, listing limit, መለያ ተገድቧል, ገደብ, ሻጭ ተገድቧል
related: sel-suspension, sel-banned, sel-reactivation-request, sel-verified-but-cannot-sell, sel-performance-standards, out-how-earnings-work
templates: tpl-seller-suspension-notice
policy_pending: yes

## Summary
A seller notices limits on their account (cannot publish new listings, cannot accept bookings, payouts on hold) and wants to know what a restriction is and why it happened.

## Issue Description
Besides full suspension or a ban, Seller Operations may place partial limits on a seller account — for example during an investigation, after complaints, or when information is missing. The exact restriction types are **not confirmed**. The seller usually notices a missing function before reading any notice, and may fear they have lost their business or earnings. Agents explain what is visible, share only reasons recorded as shareable, and route to Seller Operations.

### Status reminder
| Concept | Values |
|---|---|
| Verification | Pending, Verified, Rejected |
| Operational | Active, Suspended, Banned |
A restriction is a limit placed while the account is otherwise Active. Suspension and ban are stronger operational statuses (see `sel-suspension`, `sel-banned`).

## Possible Causes
- Missing or outdated information (profile, business details, payout identity).
- Open investigation after buyer complaints or reports.
- Listing policy violations (prohibited or misleading listings).
- Performance concerns (missed sessions, no-shows, unresolved complaints).
- Payment risk: disputes, chargebacks or unusual activity.
- Pending identity re-check after changing key details.

## Information to Collect
- Registered email/phone of the seller account
- Which function is limited and since when
- Any notice/email/notification received (screenshot)
- Any open orders/bookings affected (IDs)

> [!WARNING] Never ask for passwords, OTP codes or PINs.

## Troubleshooting Steps
1. Confirm identity and check operational status and any restriction notes through authorized tools (admin dashboard, if you have access).
2. Check what is restricted (listings, bookings, payouts) and whether a reason is recorded as **shareable**.
3. Decide:
   - **Missing information** → tell the seller exactly what to complete, on the platform.
   - **Under investigation / complaints / policy** → say the account is under review; share only recorded shareable reason; escalate to **Seller Operations**.
   - **Payout hold** → explain that earnings remain recorded but withdrawals are paused during review; see `out-pending-vs-available`; escalate payout questions to **Payments & Finance**.
   - **Fraud/risk related** → neutral wording only; **Trust & Safety**.
   - **No restriction found** → treat as technical; see `sel-verified-but-cannot-sell`.
4. Check whether buyers are affected (upcoming bookings). If so, flag High and notify **Senior Support / Supervisor** so buyers are protected.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand some functions on your seller account are currently limited, and I know this is worrying.

I have checked your account. [Explain what is limited and the shareable reason, e.g. "New listings are paused while our team reviews some information on your account."]

[If action needed:] To help us review this, please [action on the platform].

Our Seller Operations team is handling the review and will make the decision. I have added your message to your case so they have your side of the story.

Your case number is {{ticket_id}}. We will update you as soon as we can.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በሻጭ መለያዎ ላይ አንዳንድ ተግባራት ለጊዜው እንደተገደቡ ተረድቻለሁ፤ ይህ እንደሚያሳስብዎ እገነዘባለሁ።

መለያዎን አይቻለሁ። [የተገደበውን እና ሊገለጽ የሚችለውን ምክንያት ያብራሩ፤ ለምሳሌ "ቡድናችን በመለያዎ ላይ ያሉ አንዳንድ መረጃዎችን እስኪገመግም ድረስ አዲስ ዝርዝሮች ለጊዜው ቆመዋል።"]

[እርምጃ የሚያስፈልግ ከሆነ፦] ግምገማውን እንድናግዝ እባክዎ [በመድረኩ ላይ የሚወሰድ እርምጃ]።

ግምገማውን የሚያከናውነው እና ውሳኔውን የሚሰጠው የሻጭ ኦፕሬሽንስ ቡድናችን ነው። የእርስዎንም ሃሳብ እንዲያዩት መልዕክትዎን በጉዳይዎ ላይ አክያለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። በተቻለ ፍጥነት መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I see some functions on your seller account are limited: [what/reason]. Seller Operations is reviewing it and I've added your message to the case. We'll update you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በሻጭ መለያዎ ላይ አንዳንድ ተግባራት እንደተገደቡ አይቻለሁ፦ [ምን/ምክንያት]። የሻጭ ኦፕሬሽንስ ቡድን እየገመገመው ነው፤ መልዕክትዎንም በጉዳዩ ላይ አክያለሁ። መረጃ እንሰጥዎታለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. The review of your seller account is still in progress with our Seller Operations team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የሻጭ መለያዎ ግምገማ በሻጭ ኦፕሬሽንስ ቡድናችን አሁንም በሂደት ላይ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Any restriction question beyond the shareable reason → **Seller Operations**, priority Medium.
- Payout holds and earnings questions → **Payments & Finance**.
- Fraud/risk restriction disputed → **Trust & Safety**.
- Buyers with upcoming sessions affected → priority High + **Senior Support / Supervisor**.

## Resolution Procedure
1. Restriction lifted, or seller has the final decision from Seller Operations.
2. Affected buyers handled (if any).
3. Record restriction type, reason category (not fraud details), actions and outcome.

## Policy Pending Approval
- Define the restriction types (listing pause, booking pause, payout hold) and who may apply them.
- Define which reasons may be shared with the seller, and the notification wording.
- Define what happens to existing bookings/orders and pending earnings during a restriction.

## Internal Notes
- Never say "you did nothing wrong" or "this will be lifted soon" — you don't know.
- If the seller asks to cancel all their upcoming sessions because of the restriction, involve Senior Support so buyers are informed properly.

<!-- doc -->
# Seller Account Suspended
id: sel-suspension
type: article
category: seller-account
subcategory: seller-status
audience: seller
priority: high
department: seller_ops
features: seller-onboarding, seller-withdrawals
tags: seller suspended, store suspended, account suspended, cannot sell suspended, suspension reason, suspended verified seller, መለያ ታግዷል, ሻጭ ታግዷል, መደብሬ ተዘጋ
related: sel-reactivation-request, sel-account-restrictions, sel-banned, sel-performance-standards, out-pending-vs-available, sel-tsg-verification-master
templates: tpl-seller-suspension-notice, tpl-seller-contact-request
policy_pending: yes

## Summary
A seller's operational status is **Suspended**: they cannot sell, their listings may be hidden, and they want to know why and how to get reinstated.

## Issue Description
Suspension is a temporary operational block decided by Seller Operations (or Trust & Safety). It is independent of verification — a seller can be **Verified but Suspended**. The seller is often anxious about upcoming bookings, buyer messages and earnings, and may be angry. Agents must: confirm the status, share only the reason recorded as shareable, explain the appeal path, protect affected buyers, and never lift or promise to lift a suspension.

## Possible Causes
- Repeated buyer complaints, no-shows or missed sessions.
- Listing policy violations (prohibited, misleading, counterfeit).
- Investigation of possible fraud or payment risk.
- Abusive behavior toward buyers or staff.
- Identity or business information found to be incorrect.
- Off-platform payment requests to buyers (if prohibited — policy pending).

## Information to Collect
- Registered email/phone of the seller account
- Suspension notice they received (screenshot)
- Any upcoming bookings or open orders (IDs, dates)
- Seller's explanation, if they want to give one
- Whether they want to appeal

> [!WARNING] Never ask for passwords, OTP codes or PINs. Do not discuss other users' complaints by name.

## Troubleshooting Steps
1. Confirm identity and check operational status, suspension date, reason category and shareable note through authorized tools (admin dashboard, if you have access).
2. Check for **upcoming bookings** and **open orders**. If buyers are affected, raise priority to High and notify **Senior Support / Supervisor** — buyers must be informed through the approved process.
3. Decide what to share:
   - **Shareable reason recorded** → share it in neutral words.
   - **Fraud/safety investigation** → do not explain; say the account is under review.
   - **No reason recorded** → escalate to **Seller Operations** for shareable wording.
4. Explain what the suspension means for the seller (cannot sell; listings may be hidden; earnings remain recorded but may be on hold — see `out-pending-vs-available`). Do not promise payout timing.
5. If the seller wants to appeal → follow `sel-reactivation-request`.
6. Record everything in the ticket.

- [ ] Status and reason category confirmed
- [ ] Affected buyers identified and flagged
- [ ] Shareable explanation given
- [ ] Appeal path explained or appeal submitted

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand your seller account has been suspended, and I know this is stressful, especially if you have clients waiting.

I have checked your account. Your seller account is currently suspended. [Shareable reason, if any: "This follows a review of …" / or: "Your account is currently under review by our team."] While your account is suspended, you cannot accept new bookings or orders.

If you believe this is a mistake or would like the decision reviewed, you can submit a reactivation request. Please reply with your explanation and any information that supports it, and I will add it to your case for our Seller Operations team. They will make the decision.

Your earnings records remain in your account. Questions about payouts during a suspension will be reviewed by our team.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የሻጭ መለያዎ እንደታገደ ተረድቻለሁ፤ በተለይ ደንበኞች እየጠበቁዎት ከሆነ ይህ ምን ያህል እንደሚያስጨንቅ እገነዘባለሁ።

መለያዎን አይቻለሁ። የሻጭ መለያዎ በአሁኑ ጊዜ ታግዷል። [ሊገለጽ የሚችል ምክንያት ካለ፦ "ይህ የሆነው … ግምገማን ተከትሎ ነው" / ወይም፦ "መለያዎ በአሁኑ ጊዜ በቡድናችን እየተገመገመ ነው።"] መለያዎ ታግዶ እያለ አዲስ ቀጠሮዎችን ወይም ትዕዛዞችን መቀበል አይችሉም።

ይህ ስህተት ነው ብለው ካመኑ ወይም ውሳኔው እንደገና እንዲታይ ከፈለጉ፣ የመልሶ ማንቃት ጥያቄ ማቅረብ ይችላሉ። እባክዎ ማብራሪያዎን እና የሚደግፍ መረጃ ካለ ይላኩልኝ፤ ለሻጭ ኦፕሬሽንስ ቡድናችን በጉዳይዎ ላይ አክለዋለሁ። ውሳኔውን የሚሰጡት እነሱ ናቸው።

የገቢ መዝገቦችዎ በመለያዎ ውስጥ ይቆያሉ። እገዳው በሚቆይበት ጊዜ ስለሚኖሩ ክፍያዎች (payout) የሚነሱ ጥያቄዎች በቡድናችን ይታያሉ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I'm sorry — your seller account is currently suspended [shareable reason / under review]. If you'd like it reviewed, reply with your explanation and I'll add it to your case for Seller Operations, who decide. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ — የሻጭ መለያዎ በአሁኑ ጊዜ ታግዷል [ሊገለጽ የሚችል ምክንያት / በግምገማ ላይ]። እንዲታይ ከፈለጉ ማብራሪያዎን ይላኩልኝ፤ ውሳኔ ለሚሰጠው የሻጭ ኦፕሬሽንስ ቡድን በጉዳይዎ ላይ አክለዋለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your request is still being reviewed by our Seller Operations team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ጥያቄዎ አሁንም በሻጭ ኦፕሬሽንስ ቡድናችን እየታየ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Every appeal or reactivation request → **Seller Operations** (via `sel-reactivation-request`).
- Upcoming bookings/orders affected → **Senior Support / Supervisor**, priority High.
- Fraud or safety-related suspension disputed → **Trust & Safety**.
- Payout or earnings questions → **Payments & Finance**.
- Threats, legal claims, media → **Senior Support / Supervisor** → **Management**.

## Resolution Procedure
1. Seller has been informed of status and appeal path; appeal (if any) submitted with details.
2. Affected buyers flagged and handled by the responsible team.
3. Record reason category, buyer impact, appeal and outcome.

## Policy Pending Approval
- Define suspension reasons, standard duration (if any), and notification wording.
- Define how upcoming bookings/orders are handled when a seller is suspended (cancel, refund, reassign).
- Define treatment of pending and available earnings during suspension.
- Define the appeal process, deadlines and decision-maker.

## Internal Notes
- Never reveal who complained or the content of a report.
- Suspended sellers sometimes contact buyers directly to take payment off-platform — if a buyer reports this, escalate to Trust & Safety.
- Use `tpl-seller-suspension-notice` only with Seller Operations-approved reason wording.

<!-- doc -->
# Seller Account Banned
id: sel-banned
type: article
category: seller-account
subcategory: seller-status
audience: seller
priority: high
department: trust_safety
features: seller-onboarding, seller-withdrawals
tags: seller banned, permanently banned, store closed permanently, account terminated, ban reason, cannot sell anymore, በቋሚነት ታግዷል, መለያ ተዘግቷል, ሻጭ ተባረረ
related: sel-suspension, sel-reactivation-request, sel-account-restrictions, out-pending-vs-available, tns-fake-products, sel-who-can-sell
templates: tpl-seller-suspension-notice
policy_pending: yes

## Summary
A seller's operational status is **Banned** — permanent removal from selling — and they contact support to ask why, to complain, or to get their earnings.

## Issue Description
A ban is the most serious seller status and is usually linked to fraud, serious safety issues, counterfeit or prohibited goods, or repeated severe violations. These conversations can be emotional or hostile. Banned sellers may try to obtain details of the investigation, identify who reported them, or pressure the agent. **Agents never share detailed reasons for fraud-related bans**, never reverse a ban, and never promise payouts. They record the request and route it.

## Possible Causes
- Confirmed fraud (fake identity, payment fraud, scam services).
- Counterfeit, illegal or prohibited listings.
- Serious harassment, threats or abuse.
- Repeated severe violations after suspension.
- Ban evasion (opening new accounts after a previous ban).

## Information to Collect
- Registered email/phone of the banned account
- What the seller is asking for: reason, appeal, earnings, data, account closure
- Any notice received (screenshot)
- Seller's statement if they want to appeal

> [!WARNING] Never ask for passwords, OTP codes or PINs. Do not share investigation details, reporter identities or evidence.

## Troubleshooting Steps
1. Confirm identity and check operational status and ban category through authorized tools (admin dashboard, if you have access).
2. Determine the ban category:
   - **Fraud / safety / legal** → use only neutral wording ("violation of marketplace rules"). Do not describe evidence. Route any appeal to **Trust & Safety**.
   - **Policy violations with shareable reason** → share the recorded shareable reason only.
3. Earnings/balance questions → do not promise anything; record and escalate to **Payments & Finance** (and Trust & Safety for fraud bans, since funds may be held).
4. Appeal request → record the seller's statement and escalate per `sel-reactivation-request` (to **Trust & Safety** for fraud bans; **Seller Operations** otherwise).
5. If the seller threatens staff or buyers → stay calm, end politely, escalate to **Trust & Safety** and your supervisor.
6. If you notice a **new account** created by a banned seller → do not confront; report to **Trust & Safety**.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand you are asking about the status of your seller account.

Your seller account has been permanently removed from selling following a review under our marketplace rules. I'm not able to share further details of the review.

If you would like to request a review of this decision, please reply with your explanation. I will record it in your case and pass it to the responsible team, who will make the final decision.

I have also noted your question about [earnings / your account]; the responsible team will review it.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ስለ ሻጭ መለያዎ ሁኔታ እየጠየቁ መሆኑን ተረድቻለሁ።

በገበያ ቦታችን ደንቦች መሠረት በተደረገ ግምገማ ምክንያት የሻጭ መለያዎ ከመሸጥ በቋሚነት ታግዷል። ስለ ግምገማው ተጨማሪ ዝርዝር ማጋራት አልችልም።

ይህ ውሳኔ እንደገና እንዲታይ መጠየቅ ከፈለጉ እባክዎ ማብራሪያዎን ይላኩልኝ። በጉዳይዎ ላይ መዝግቤ የመጨረሻውን ውሳኔ ለሚሰጠው ኃላፊ ቡድን አስተላልፋለሁ።

ስለ [ገቢዎ / መለያዎ] ያቀረቡትንም ጥያቄ መዝግቤያለሁ፤ የሚመለከተው ቡድን ይመለከተዋል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your seller account has been permanently removed from selling following a review under our marketplace rules; I can't share more details. If you want the decision reviewed, reply with your explanation and I'll pass it on. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በገበያ ቦታችን ደንቦች መሠረት በተደረገ ግምገማ የሻጭ መለያዎ በቋሚነት ታግዷል፤ ተጨማሪ ዝርዝር ማጋራት አልችልም። ውሳኔው እንዲታይ ከፈለጉ ማብራሪያዎን ይላኩ፤ አስተላልፋለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your request has been passed to the responsible team and is under review. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ጥያቄዎ ለሚመለከተው ቡድን ተላልፎ በግምገማ ላይ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Any appeal of a fraud/safety ban → **Trust & Safety**.
- Appeal of a non-fraud ban → **Seller Operations**.
- Earnings/payout questions → **Payments & Finance** (Trust & Safety informed for fraud bans).
- Threats, legal action, police, media → **Senior Support / Supervisor** → **Management**.
- Suspected ban evasion (new account) → **Trust & Safety**.

## Resolution Procedure
1. Seller informed of status; appeal or earnings question escalated with full statement.
2. Record ban category (not details), request type and escalation. Close only after the responsible team's final answer is communicated.

## Policy Pending Approval
- Define ban grounds and whether bans can be appealed.
- Define the treatment of pending/available earnings after a ban (release, hold, offset against refunds).
- Define data-access and account-deletion rights for banned sellers.
- Approve the standard neutral wording for ban notices.

## Internal Notes
- Fraud-related bans: **never** confirm or deny specific allegations, evidence, reporters or linked accounts — even if the seller "already knows".
- Keep messages short and factual. Long explanations invite argument.
- Banned sellers sometimes pose as buyers or new applicants — check for links to the banned identity and report, don't confront.

<!-- doc -->
# Seller Reactivation / Appeal Request
id: sel-reactivation-request
type: article
category: seller-account
subcategory: seller-status
audience: seller
priority: medium
department: seller_ops
features: seller-onboarding
tags: reactivate seller account, appeal suspension, appeal decision, unsuspend, reinstatement, review my account, መለያ እንዲከፈት, ይግባኝ, መልሶ ማንቃት
related: sel-suspension, sel-banned, sel-account-restrictions, sel-verification-rejected, sel-performance-standards
templates: tpl-seller-contact-request, tpl-seller-suspension-notice
policy_pending: yes

## Summary
A seller asks for their suspended, restricted or banned account to be reactivated, or appeals a verification or account decision.

## Issue Description
The seller wants a decision reversed. Support's role is to make sure the appeal reaches the right team **complete and well documented**, to set honest expectations, and to keep the seller informed. Support does not decide appeals and must not hint at the likely outcome. A good appeal record saves many repeat contacts.

## Possible Causes
- Seller believes the suspension/ban/rejection was a mistake.
- Seller has fixed the issue (updated info, removed listings, resolved complaints).
- Seller wants to understand the conditions for reinstatement.

## Information to Collect
- Registered email/phone of the seller account
- Which decision they are appealing (rejection, restriction, suspension, ban) and the date
- Seller's explanation in their own words
- What they have changed or corrected since the decision
- Supporting information (e.g., order/booking IDs, screenshots of conversations) — **not** ID documents in chat
- Preferred language (Amharic/English) and contact channel

> [!WARNING] Never ask for passwords, OTP codes or PINs. If new identity documents are needed, they must be uploaded on the platform.

## Troubleshooting Steps
1. Confirm identity and current statuses.
2. Check whether an appeal is already open — avoid duplicates; add new information to the existing case.
3. Write the appeal summary in the ticket using this structure:
   - Decision appealed + date
   - Seller's explanation (quote key sentences)
   - Corrections made
   - Supporting references
4. Route:
   - Verification rejection, restriction, non-fraud suspension/ban → **Seller Operations**.
   - Fraud/safety-related suspension or ban → **Trust & Safety**.
5. Send the acknowledgment response. Do not promise reinstatement or a decision date.
6. When the decision arrives, communicate it using the wording approved by the deciding team.

- [ ] No duplicate appeal
- [ ] Appeal summary complete
- [ ] Routed to the correct team
- [ ] Seller acknowledged

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your message. I have recorded your request to review the decision on your seller account, including your explanation and the information you shared.

Your request has been sent to the responsible team, who will review it and make the decision. I'm not able to predict the outcome, but I will make sure you are informed as soon as there is an answer.

If you have any additional information that supports your request, please reply to this case rather than opening a new one.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ መልዕክትዎ እናመሰግናለን። በሻጭ መለያዎ ላይ የተሰጠው ውሳኔ እንደገና እንዲታይ ያቀረቡትን ጥያቄ፣ ማብራሪያዎን እና ያጋሩትን መረጃ ጨምሮ መዝግቤያለሁ።

ጥያቄዎ ለሚመለከተው ቡድን ተልኳል፤ እነሱ ገምግመው ውሳኔ ይሰጣሉ። ውጤቱን አስቀድሜ መናገር ባልችልም መልስ እንደተገኘ ወዲያውኑ እንዲያውቁ አደርጋለሁ።

ጥያቄዎን የሚደግፍ ተጨማሪ መረጃ ካለዎት እባክዎ አዲስ ጉዳይ ከመክፈት ይልቅ በዚሁ ጉዳይ ላይ ይመልሱ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I've recorded your appeal with your explanation and sent it to the responsible team, who will decide. I can't predict the outcome, but I'll update you. Please add any new info to this case. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የይግባኝ ጥያቄዎን ከማብራሪያዎ ጋር መዝግቤ ውሳኔ ለሚሰጠው ቡድን ልኬያለሁ። ውጤቱን አስቀድሜ መናገር ባልችልም መረጃ እሰጥዎታለሁ። ተጨማሪ መረጃ ካለ በዚሁ ጉዳይ ላይ ያክሉ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your appeal is still under review by the responsible team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ይግባኝዎ አሁንም በሚመለከተው ቡድን እየታየ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- All appeals → **Seller Operations** (non-fraud) or **Trust & Safety** (fraud/safety).
- Appeal open beyond the internal target with no response → **Senior Support / Supervisor**.
- Seller claims discrimination, legal rights, or threatens action → **Senior Support / Supervisor** → **Management**.

## Resolution Procedure
1. Final decision received from the deciding team.
2. Decision communicated with approved wording; if reinstated, guide seller back to dashboard and listings.
3. Record decision, decision-maker team and date before closing.

## Policy Pending Approval
- Define the appeal process: who decides, internal response target, how many appeals are allowed.
- Define conditions for reinstatement (e.g., corrective actions, probation period).
- Define whether banned sellers may appeal at all.

## Internal Notes
- One appeal per decision — merge duplicates.
- Do not forward the seller's raw message only; write a clear summary so the deciding team can act quickly.
