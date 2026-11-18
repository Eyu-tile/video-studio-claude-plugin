<!-- doc -->
# Locked Account (Too Many Attempts)
id: acc-locked-account
type: article
category: account-access
subcategory: account-status
audience: both
priority: medium
department: support_l1
features: accounts
tags: account locked, too many attempts, temporarily blocked, locked out, try again later, unlock account, መለያዬ ተቆልፏል, ብዙ ሙከራ, ታግጃለሁ
related: acc-incorrect-password, acc-forgot-password, acc-unauthorized-access, reg-otp-invalid-expired, acc-tsg-login-master
templates: tpl-account-locked, tpl-password-reset-guide
policy_pending: yes

## Summary
The account was locked or temporarily blocked after too many failed login or code attempts. The customer wants it unlocked.

## Issue Description
After several wrong passwords or codes, the system blocks further attempts to protect the account. The customer may not have caused the lock themselves — if someone else was trying to get in, the lock is a warning sign. How long a lock lasts and whether it clears automatically are **not confirmed**.

## Possible Causes
- The customer tried several wrong passwords (keyboard, autofill, forgotten password).
- Several wrong or old verification codes entered.
- Someone else tried to log in to the account (attack or a person who knows the email/phone).
- A shared device/family member trying to log in.
- A technical fault locking accounts incorrectly.

## Information to Collect
- Registered email or phone
- Screenshot of the lock message
- Whether the customer made the failed attempts themselves
- Any unexpected messages (codes, password reset, login alerts) they received

> [!WARNING] Never ask for the password or codes. Unlocking an account is done only by the system or authorized staff.

## Troubleshooting Steps
1. Ask: "Did you make several attempts yourself just now?"
   - **Yes** → normal lock. Go to step 2.
   - **No / not sure, and they got unexpected codes or reset messages** → possible attack → *Unauthorized access*, **Trust & Safety**, Critical.
2. Check the account state in the admin dashboard (locked, and since when, if visible).
3. Explain the lock is a safety measure. Ask the customer to wait before trying again (do not quote a time unless approved), and then use *Forgotten password* instead of guessing.
4. If the lock does not clear, or the customer has an urgent need (session starting soon), escalate to **Senior Support** — unlocking is done by authorized staff only.
5. Record whether the customer confirmed the attempts were theirs.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. Your account has been temporarily locked after several unsuccessful attempts. This is a safety measure to protect your account.

Please wait a little while before trying again, and then use "Forgot password?" on the login page to set a new password instead of guessing.

If you did not make these attempts yourself, or you received codes or reset messages you didn't request, please tell me immediately so we can protect your account. Never share your password or codes with anyone, including us.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ከበርካታ ያልተሳኩ ሙከራዎች በኋላ መለያዎ ለጊዜው ተቆልፏል። ይህ መለያዎን ለመጠበቅ የሚወሰድ የደህንነት እርምጃ ነው።

እባክዎ እንደገና ከመሞከርዎ በፊት ጥቂት ይጠብቁ፤ ከዚያም ከመገመት ይልቅ በመግቢያ ገጹ ላይ "Forgot password?" ተጠቅመው አዲስ የይለፍ ቃል ያዘጋጁ።

እነዚህን ሙከራዎች ራስዎ ካላደረጉ፣ ወይም ያልጠየቁት ኮድ ወይም የመቀየሪያ መልዕክት ደርሶዎት ከሆነ፣ መለያዎን እንድንጠብቅ እባክዎ ወዲያውኑ ይንገሩኝ። የይለፍ ቃልዎን ወይም ኮድዎን ለማንም አያጋሩ፤ ለእኛም ጭምር።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your account was locked for safety after several failed attempts. Please wait a little, then use "Forgot password?". Didn't make the attempts yourself? Tell me right away. Never share codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ከበርካታ ያልተሳኩ ሙከራዎች በኋላ መለያዎ ለደህንነት ተቆልፏል። እባክዎ ጥቂት ጠብቀው "Forgot password?" ይጠቀሙ። ሙከራዎቹን ራስዎ ካላደረጉ ወዲያውኑ ይንገሩኝ። ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our team is reviewing the lock on your account. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ቡድናችን በመለያዎ ላይ ያለውን መቆለፍ እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Lock does not clear, or the customer needs urgent access → **Senior Support / Supervisor** (authorized unlock only).
- Customer did not make the attempts / received unrequested codes → **Trust & Safety**, Critical.
- Many accounts locked at once → **Technical / Engineering** + **Trust & Safety** (possible attack or bug).

## Resolution Procedure
1. Confirm the customer can log in (after waiting or resetting).
2. Confirm the security question was asked and the answer recorded.
3. Record cause and action before resolving.

## Policy Pending Approval
- Confirm the number of failed attempts that triggers a lock and how long it lasts.
- Confirm whether locks clear automatically and who may unlock manually.
- Approve the customer wording for lock duration.

## Internal Notes
- Never unlock an account just because the customer is upset. If someone else caused the lock, unlocking helps the attacker.
- Recommend a password reset after any lock, even if the customer caused it.

<!-- doc -->
# Suspended Account Enquiry
id: acc-suspended-account
type: article
category: account-access
subcategory: account-status
audience: both
priority: high
department: support_l2
features: accounts, seller-onboarding
tags: account suspended, account disabled, account restricted, why is my account suspended, seller suspended, reactivate account, መለያዬ ታግዷል, ለምን ታገድኩ, መለያ እንደገና መክፈት
related: acc-banned-account, acc-login-error-generic, reg-suspicious-registration, acc-unauthorized-access, gen-contact-support
templates: tpl-verify-identity
policy_pending: yes

## Summary
The customer's account (buyer or seller) is suspended and they want to know why and how to get it back.

## Issue Description
A suspension restricts what the account can do. For sellers, the operational status **Suspended** is separate from verification status — a seller can be **Verified but Suspended**. Customers are often upset or anxious, especially sellers with upcoming bookings or pending earnings, and buyers with paid bookings. Level 1 agents can confirm the status and route the case; they **do not** decide or reverse suspensions.

## Possible Causes
- Policy or marketplace rule violation (e.g., seller conduct, listing violations).
- Fraud or security review (suspicious payments, compromise suspected).
- Multiple complaints or disputes.
- Identity verification problems discovered after approval.
- Protective suspension after a reported compromise.
- Administrative error.

## Information to Collect
- Registered email or phone, and identity confirmation (see *Account recovery* — identity check)
- Whether the account is a buyer or seller account
- When they noticed the suspension and any message they received
- Upcoming bookings, pending payments, refunds or seller balances affected
- The customer's explanation, if they want to give one

> [!WARNING] Never ask for passwords or codes. Do not share internal notes, fraud flags or reports from other users.

## Troubleshooting Steps
1. Verify the customer's identity before discussing the account.
2. Confirm the status in the admin dashboard (buyer account status; seller verification + operational status).
3. Check what the internal record says about who suspended it and why — **do not** disclose internal reasons unless an approved customer-facing reason is recorded.
4. Identify urgent impacts: upcoming sessions (as buyer or seller), pending payments/refunds, seller withdrawals.
5. Route the case:
   - **Seller account** → **Seller Operations**.
   - **Buyer account / security or fraud review** → **Trust & Safety**.
   - **Protective suspension after compromise** → **Trust & Safety** (follow *Unauthorized access*).
6. Record the customer's statement and any evidence they provide in the ticket for the reviewing team.
7. Tell the customer the case is being reviewed; do not promise reinstatement.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand how concerning this is, and I'm here to help.

I can confirm that your account is currently restricted. I have recorded your message under case number {{ticket_id}} and passed it to the responsible team for review. If you'd like to share any explanation or information that may help the review, please reply to this message.

I'm not able to promise an outcome, but we will contact you with an update as soon as the review progresses. Please do not share your password or verification codes with anyone.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ይህ ምን ያህል እንደሚያሳስብ ይገባኛል፤ ለመርዳት ዝግጁ ነኝ።

መለያዎ በአሁኑ ወቅት ገደብ እንደተጣለበት ማረጋገጥ እችላለሁ። መልዕክትዎን በጉዳይ ቁጥር {{ticket_id}} መዝግቤ ለግምገማ ለሚመለከተው ቡድን አስተላልፌዋለሁ። ለግምገማው የሚረዳ ማብራሪያ ወይም መረጃ ማጋራት ከፈለጉ እባክዎ ለዚህ መልዕክት ምላሽ ይስጡ።

የውጤቱን ዓይነት ቃል መግባት አልችልም፤ ነገር ግን ግምገማው እንደተሻሻለ መረጃ እንሰጥዎታለን። እባክዎ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድዎን ለማንም አያጋሩ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I can confirm your account is currently restricted. I've passed your case to the responsible team for review — you can reply with any information that may help. Never share codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ መለያዎ በአሁኑ ወቅት ገደብ እንደተጣለበት አረጋግጣለሁ። ጉዳይዎን ለግምገማ ለሚመለከተው ቡድን አስተላልፌያለሁ — የሚረዳ መረጃ ካለ መላክ ይችላሉ። ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. The review of your account is still in progress. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የመለያዎ ግምገማ አሁንም በሂደት ላይ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Seller suspension → **Seller Operations**.
- Buyer suspension, fraud/security review → **Trust & Safety**.
- Suspension affects upcoming paid bookings or seller earnings/withdrawals → also notify **Payments & Finance**; priority High.
- Customer threatens legal action or public complaints → **Management**.
- Suspension appears to be an administrative error → **Senior Support / Supervisor**.

## Resolution Procedure
1. The reviewing team decides; the agent communicates only the approved outcome.
2. Confirm affected bookings/payments were handled per the decision.
3. Record the outcome and communication in the ticket before resolving.

## Policy Pending Approval
- Define suspension reasons, durations, and what customers may be told.
- Define the appeal/review process, who decides, and response targets.
- Decide what happens to upcoming bookings, buyer payments and seller earnings during a suspension.

## Internal Notes
- "Restricted" is safer wording than "suspended for fraud" — never imply guilt.
- Do not tell a suspended user to create a new account.
- Keep all communication in one ticket; the reviewing team needs the full history.

<!-- doc -->
# Banned Account Enquiry and Appeal
id: acc-banned-account
type: article
category: account-access
subcategory: account-status
audience: both
priority: high
department: trust_safety
features: accounts, seller-onboarding
tags: account banned, permanently banned, appeal ban, account closed by byfluence, unban, seller banned, መለያዬ ሙሉ በሙሉ ታግዷል, ይግባኝ, እገዳ ይነሳልኝ
related: acc-suspended-account, reg-suspicious-registration, reg-duplicate-accounts, acc-login-error-generic, gen-contact-support
templates: tpl-verify-identity
policy_pending: yes

## Summary
The customer's account has been banned (permanently restricted) and they want to know why, or want to appeal.

## Issue Description
A ban is the most serious operational status (Active → Suspended → Banned). Whether bans are always permanent, and whether appeals are accepted, is **not confirmed**. Agents record the appeal accurately, route it, and avoid any promise. Banned sellers may also ask about earnings; banned buyers about paid bookings.

## Possible Causes
- Serious or repeated violation of marketplace rules.
- Confirmed fraud, abuse or harassment.
- Ban evasion (new account created after a suspension/ban).
- Identity fraud during seller verification.
- Administrative error (rare).

## Information to Collect
- Identity confirmation (registered email/phone + account details — see *Account recovery*)
- The customer's appeal statement in their own words
- Any evidence they want reviewed (documents, screenshots)
- Outstanding items: upcoming bookings, payments, refunds, seller earnings/withdrawals

> [!WARNING] Never ask for passwords or codes. Do not share the internal reason, reporter identity, or evidence held by Trust & Safety.

## Troubleshooting Steps
1. Verify identity.
2. Confirm the status in the admin dashboard (Banned) and check the internal record for an approved customer-facing reason.
3. If the customer wants to appeal, record their full statement and attachments in the ticket.
4. List outstanding financial items (bookings, payments, seller balances) for the reviewing team.
5. Escalate to **Trust & Safety** (buyers and sellers); include **Seller Operations** for sellers and **Payments & Finance** if money is outstanding.
6. Tell the customer the appeal has been recorded and will be reviewed; no outcome or timeline promises.
7. If the customer is contacting from a new account → note possible ban evasion; do not act on the new account yourself.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I can confirm that your account is currently closed to use on Byfluence.

If you would like the decision to be reviewed, please reply with your explanation and any information or documents you would like the team to consider. I will add everything to your case, number {{ticket_id}}, and pass it to the responsible team.

I'm not able to promise a particular outcome, but we will inform you once the review has been completed. Please do not share your password or verification codes with anyone.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። መለያዎ በአሁኑ ወቅት በByfluence ላይ ጥቅም ላይ እንዳይውል መዘጋቱን ማረጋገጥ እችላለሁ።

ውሳኔው እንደገና እንዲታይ ከፈለጉ፣ እባክዎ ማብራሪያዎን እና ቡድኑ እንዲያየው የሚፈልጉትን ማንኛውንም መረጃ ወይም ሰነድ ይላኩልን። ሁሉንም በጉዳይ ቁጥር {{ticket_id}} ላይ ጨምሬ ለሚመለከተው ቡድን አስተላልፋለሁ።

የተወሰነ ውጤት ቃል መግባት አልችልም፤ ነገር ግን ግምገማው ሲጠናቀቅ እናሳውቅዎታለን። እባክዎ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድዎን ለማንም አያጋሩ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your account is currently closed to use on Byfluence. To request a review, reply with your explanation and any documents — I'll add them to your case for the team. Never share codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ መለያዎ በአሁኑ ወቅት በByfluence ላይ እንዳይሰራ ተዘግቷል። ግምገማ ለመጠየቅ ማብራሪያዎን እና ሰነዶችዎን ይላኩ — ለቡድኑ በጉዳይዎ ላይ እጨምራለሁ። ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your review request is still with the responsible team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የግምገማ ጥያቄዎ አሁንም በሚመለከተው ቡድን ዘንድ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- All ban enquiries and appeals → **Trust & Safety**.
- Seller bans → also **Seller Operations**; outstanding earnings/withdrawals → **Payments & Finance**.
- Legal threats, media/reputation risk → **Management**.

## Resolution Procedure
1. Trust & Safety (or Management) decides the appeal.
2. The agent sends only the approved outcome wording.
3. Record the appeal, decision, and how outstanding money/bookings were handled.

## Policy Pending Approval
- Decide whether bans are permanent and whether appeals are accepted, by whom, and with what response target.
- Decide what customers are told about the reason for a ban.
- Decide how outstanding seller earnings, buyer payments and upcoming bookings are handled after a ban.

## Internal Notes
- Stay calm and respectful even if the customer is angry; offer a supervisor if needed.
- Never suggest creating a new account, and never reveal who reported them.

<!-- doc -->
# Email Change Request
id: acc-change-email
type: article
category: account-access
subcategory: account-changes
audience: both
priority: high
department: support_l2
features: accounts
tags: change email, update email, new email address, wrong email on account, email no longer used, ኢሜይል መቀየር, አዲስ ኢሜይል, ኢሜይሌን ቀይሩልኝ
related: acc-change-phone, acc-account-recovery-lost-access, acc-unauthorized-access, buy-update-profile, reg-email-verification
templates: tpl-verify-identity, tpl-never-share-otp-warning
policy_pending: yes

## Summary
The customer wants to change the email address on their account. Because the email controls password resets, this is a high-risk change that requires identity verification and is performed only by authorized staff (or by the customer through a self-service setting, if one exists).

## Issue Description
Customers change email when they stop using an old address, made a typo, or want to use a work/personal address. Attackers also request email changes to take over accounts — the most common account-takeover route through support. Treat every request carefully.

## Possible Causes
- Old email no longer used or accessible.
- Typo in the email at registration.
- Preference for a different address.
- Account takeover attempt (attacker wants control of resets).

## Information to Collect
- Current registered email (customer states it; you don't reveal it)
- New email address they want to use
- Reason for the change
- Identity check items (see below)
- Whether they can still log in and access the old email

> [!WARNING] Never ask for passwords, OTP codes or PINs. Never read out the current email for them to confirm — ask them to tell you.

## Troubleshooting Steps
1. **Self-service first:** if the customer can log in and the live account settings allow changing email, guide them to do it there (verification will go to the new email). Confirm the option exists before suggesting it.
2. If self-service is not available or they can't log in, do the **interim identity check**:
   - The request comes from the registered email or phone, **or** the customer correctly states the registered email and phone; **and**
   - They give at least one account detail only the holder would know: full name on the account, a recent booking (consultation, seller, date) or a recent transaction (reference, amount, date).
3. Check the new email is not already used by another account (do not reveal that account's details).
4. Look for **risk signals**: urgency/pressure, recent phone change, recent password reset, request from an unregistered channel, seller with pending withdrawal or recently changed payout details, details that don't match.
5. Create the ticket with all evidence and escalate to **Senior Support** — the change is made by authorized staff only. If risk signals exist → **Trust & Safety** instead.
6. Tell the customer the request is under review; do not confirm a completion time.
7. After the change, the customer should verify the new email and, ideally, reset their password.

- [ ] Self-service option checked
- [ ] Identity check completed and recorded
- [ ] New email not in use by another account
- [ ] Risk signals reviewed
- [ ] Escalated to authorized staff

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I can help you request an email change. To protect your account, we first need to confirm that you are the account owner.

Please reply with:
1. The email address and phone number currently registered on your account
2. The new email address you would like to use
3. Details of a recent booking or payment on your account (for example, the consultation name and date, or the transaction reference)

Please do not send your password or any verification code — we will never ask for them.

Once we receive this, your request will be reviewed by our authorized team. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የኢሜይል ለውጥ ጥያቄዎን እንዲያቀርቡ እረዳዎታለሁ። መለያዎን ለመጠበቅ፣ በመጀመሪያ እርስዎ የመለያው ባለቤት መሆንዎን ማረጋገጥ ያስፈልገናል።

እባክዎ የሚከተሉትን ይላኩልን፦
1. በአሁኑ ወቅት በመለያዎ ላይ የተመዘገበውን ኢሜይል እና ስልክ ቁጥር
2. ሊጠቀሙበት የሚፈልጉትን አዲስ የኢሜይል አድራሻ
3. በመለያዎ ላይ ያለ የቅርብ ጊዜ ቀጠሮ ወይም ክፍያ ዝርዝር (ለምሳሌ የምክክሩ ርዕስ እና ቀን፣ ወይም የግብይት መለያ ቁጥር)

እባክዎ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አይላኩ — በፍጹም አንጠይቅዎትም።

ይህን እንደደረሰን ጥያቄዎ ስልጣን ባለው ቡድናችን ይገመገማል። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, to request an email change please send: your current registered email + phone, the new email, and a recent booking or payment detail. Never send passwords or codes. Our authorized team will review it. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የኢሜይል ለውጥ ለመጠየቅ እባክዎ፦ አሁን የተመዘገበ ኢሜይል + ስልክ፣ አዲሱን ኢሜይል እና የቅርብ ቀጠሮ ወይም ክፍያ ዝርዝር ይላኩ። የይለፍ ቃል ወይም ኮድ አይላኩ። ስልጣን ያለው ቡድናችን ይገመግመዋል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your email change request is still being reviewed by our authorized team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የኢሜይል ለውጥ ጥያቄዎ አሁንም ስልጣን ባለው ቡድናችን እየተገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Every verified request that can't be done by self-service → **Senior Support / Supervisor** (authorized staff make the change).
- Any risk signal or failed identity check → **Trust & Safety**.
- Seller account with pending withdrawal or recent payout-detail change → **Trust & Safety** + **Payments & Finance**, priority High.

## Resolution Procedure
1. Authorized staff confirm the change and record who approved it.
2. Confirm the customer can log in and has verified the new email.
3. Recommend a password reset; record the identity evidence and outcome in the ticket.

## Policy Pending Approval
- Approve the official identity verification procedure for account changes (factors required, documents, who approves).
- Confirm whether customers can change email themselves in settings.
- Decide whether the old email is notified of the change and whether there is a waiting/hold period for sellers' payouts after a change.

## Internal Notes
- Never change an email on the basis of a single chat message from an unregistered channel.
- If the customer cannot pass the check, do not hint which detail was wrong — escalate to Trust & Safety.
- Record exactly which identity items were provided (not the values of any secret), so the approver can audit the decision.

<!-- doc -->
# Phone Number Change Request
id: acc-change-phone
type: article
category: account-access
subcategory: account-changes
audience: both
priority: high
department: support_l2
features: accounts, notifications-sms
tags: change phone number, new phone number, lost SIM, update phone, number changed, ስልክ ቁጥር መቀየር, አዲስ ስልክ ቁጥር, ሲም ጠፍቶብኛል
related: acc-change-email, acc-account-recovery-lost-access, acc-unauthorized-access, reg-phone-verification, buy-update-profile
templates: tpl-verify-identity, tpl-never-share-otp-warning
policy_pending: yes

## Summary
The customer wants to change the phone number on their account — because they have a new number, lost their SIM, or entered the wrong one. Identity verification is required and the change is made by authorized staff (or by the customer in settings, if available).

## Issue Description
If the phone number is used for codes or password resets, whoever controls it can control the account. Lost/stolen phones and SIM-swap fraud make this a high-risk request. A customer who has lost their phone may also be worried about who can access their account.

## Possible Causes
- New SIM / new number.
- Lost or stolen phone; SIM no longer active.
- Typo in the number at registration.
- Account takeover attempt (SIM-swap or social engineering).

## Information to Collect
- Current registered phone and email (customer states them)
- New phone number
- Reason (new number, lost/stolen phone, typo)
- Identity check items (registered email/phone + recent booking/transaction details)
- If lost/stolen: whether the phone was unlocked/logged in to Byfluence

> [!WARNING] Never ask for passwords, OTP codes or PINs. Never confirm the current number for them — ask them to state it.

## Troubleshooting Steps
1. **Lost/stolen phone?** Treat as a security case first: advise the customer to contact their mobile operator to block the SIM, and to change their Byfluence password from another device if they can log in. If they think someone is using the account → *Unauthorized access* (**Trust & Safety**, Critical).
2. **Self-service:** if the customer can log in and the settings allow changing phone, guide them there (confirm the option exists first).
3. Otherwise, do the **interim identity check** (same as *Email change request*): contact from registered email/phone or correct statement of both, plus at least one recent booking/transaction detail or the full name on the account.
4. Check the new number is not registered to another account (don't reveal details).
5. Review risk signals (recent email change, seller withdrawal pending, urgency, mismatches).
6. Escalate to **Senior Support** for the change by authorized staff; risk signals → **Trust & Safety**.
7. After the change, the customer should verify the new number and reset their password.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I can help you request a phone number change. To protect your account, we first need to confirm you are the account owner.

Please reply with:
1. The email address and phone number currently registered on your account
2. The new phone number you want to use
3. Details of a recent booking or payment on your account (for example, the consultation name and date, or the transaction reference)

If your phone was lost or stolen, please also contact your mobile operator to block the SIM. Please do not share your password or any verification code — we will never ask for them.

Your case number is {{ticket_id}}. Your request will be reviewed by our authorized team.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የስልክ ቁጥር ለውጥ ጥያቄዎን እንዲያቀርቡ እረዳዎታለሁ። መለያዎን ለመጠበቅ፣ በመጀመሪያ እርስዎ የመለያው ባለቤት መሆንዎን ማረጋገጥ ያስፈልገናል።

እባክዎ የሚከተሉትን ይላኩልን፦
1. በአሁኑ ወቅት በመለያዎ ላይ የተመዘገበውን ኢሜይል እና ስልክ ቁጥር
2. ሊጠቀሙበት የሚፈልጉትን አዲስ ስልክ ቁጥር
3. በመለያዎ ላይ ያለ የቅርብ ጊዜ ቀጠሮ ወይም ክፍያ ዝርዝር (ለምሳሌ የምክክሩ ርዕስ እና ቀን፣ ወይም የግብይት መለያ ቁጥር)

ስልክዎ ጠፍቶ ወይም ተሰርቆ ከሆነ፣ እባክዎ ሲም ካርዱን ለማዘጋት የሞባይል ኦፕሬተርዎን ያነጋግሩ። እባክዎ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ጥያቄዎ ስልጣን ባለው ቡድናችን ይገመገማል።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, to request a phone change please send: current registered email + phone, the new number, and a recent booking/payment detail. Lost phone? Ask your operator to block the SIM. Never send passwords or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የስልክ ለውጥ ለመጠየቅ እባክዎ፦ አሁን የተመዘገበ ኢሜይል + ስልክ፣ አዲሱን ቁጥር እና የቅርብ ቀጠሮ/ክፍያ ዝርዝር ይላኩ። ስልክ ጠፍቶ ከሆነ ሲሙን እንዲያዘጉ ኦፕሬተርዎን ይጠይቁ። የይለፍ ቃል ወይም ኮድ አይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your phone number change request is still being reviewed by our authorized team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የስልክ ቁጥር ለውጥ ጥያቄዎ አሁንም ስልጣን ባለው ቡድናችን እየተገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Verified request not possible via self-service → **Senior Support / Supervisor**.
- Lost/stolen phone with signs of account use, or failed identity check → **Trust & Safety**, Critical/High.
- Seller with pending withdrawals or payout-detail changes → **Trust & Safety** + **Payments & Finance**.

## Resolution Procedure
1. Authorized staff make and record the change.
2. Confirm the customer verified the new number and can log in.
3. Recommend a password reset; record identity evidence and outcome.

## Policy Pending Approval
- Approve the official identity verification procedure for phone changes.
- Confirm whether customers can change their phone number themselves in settings.
- Decide whether a hold applies to seller withdrawals after a phone/email change.

## Internal Notes
- SIM-swap fraud is real in the region: a request to change the phone **and** the email at the same time is a strong risk signal.
- Ethiopian numbers can be recycled; a "new owner" of the old number may receive codes — another reason to process changes promptly once verified.

<!-- doc -->
# Account Deletion / Closure Request
id: acc-account-deletion-request
type: article
category: account-access
subcategory: account-changes
audience: both
priority: medium
department: support_l2
features: accounts
tags: delete account, close account, remove my account, deactivate, delete my data, cancel account, መለያዬን ሰርዙልኝ, መለያ መዝጋት, መረጃዬን አጥፉ
related: tns-data-deletion-request, reg-duplicate-accounts, buy-privacy-concerns, acc-change-email, gen-contact-support
templates: tpl-account-deletion-ack, tpl-verify-identity
policy_pending: yes

## Summary
The customer wants their Byfluence account deleted or closed. The request must be verified, checked for open bookings/payments/balances, and processed by authorized staff under the (pending) deletion and data-retention policy.

## Issue Description
Customers ask for deletion because they no longer use the platform, have a duplicate account, are unhappy, or have privacy concerns. Deletion may be irreversible and may affect upcoming bookings, refunds and seller earnings. Some data may need to be kept for financial or legal reasons — the retention rules are **not confirmed**.

## Possible Causes
- No longer using Byfluence.
- Duplicate account cleanup.
- Dissatisfaction after a bad experience (consider resolving the underlying issue first).
- Privacy concerns.
- Account compromise (the customer wants to "delete it before someone uses it").

## Information to Collect
- Identity check (registered email/phone + recent booking/transaction details)
- Reason for deletion (optional for the customer, but helpful)
- Whether they want the **account closed** or also a **personal data deletion** request
- Upcoming bookings, pending payments/refunds, open disputes
- For sellers: active listings, upcoming sessions, pending/available balance, withdrawals in progress

> [!WARNING] Never ask for passwords or codes. Do not delete or deactivate the account yourself.

## Troubleshooting Steps
1. Verify identity (interim check as in *Email change request*).
2. If the reason is a fixable problem (complaint, compromise), offer help first — without pressure. Compromise → *Unauthorized access*.
3. Check the account in the admin dashboard for open items: upcoming bookings, pending/refund payments, disputes, seller balances and withdrawals.
4. Explain to the customer that open items must be settled first (and what they are), without promising refund outcomes.
5. If they also want their personal data deleted, follow tns-data-deletion-request.
6. Send the deletion acknowledgement (tpl-account-deletion-ack) and escalate to **Senior Support** for processing by authorized staff. Seller accounts → also **Seller Operations**; balances → **Payments & Finance**.
7. Record the request date, identity evidence, open items and the customer's choices.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry to hear you'd like to close your account. If there is a problem we can help with, please let me know.

To process your request safely, please confirm:
1. The email address and phone number registered on your account
2. Details of a recent booking or payment on your account, if any
3. Whether you would also like us to delete your personal data

Before an account can be closed, any upcoming bookings, pending payments or open issues need to be settled. I will check this and let you know if anything needs your attention. Please never share your password or verification codes.

Your request is recorded under case number {{ticket_id}} and will be handled by our authorized team.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። መለያዎን መዝጋት እንደሚፈልጉ በመስማታችን እናዝናለን። ልንረዳዎ የምንችለው ችግር ካለ እባክዎ ያሳውቁኝ።

ጥያቄዎን ደህንነቱ በተጠበቀ መንገድ ለማስተናገድ እባክዎ የሚከተሉትን ያረጋግጡልኝ፦
1. በመለያዎ ላይ የተመዘገበውን ኢሜይል እና ስልክ ቁጥር
2. በመለያዎ ላይ ያለ የቅርብ ጊዜ ቀጠሮ ወይም ክፍያ ዝርዝር (ካለ)
3. የግል መረጃዎም እንዲሰረዝ ይፈልጉ እንደሆነ

መለያ ከመዘጋቱ በፊት ማንኛውም መጪ ቀጠሮ፣ በሂደት ላይ ያለ ክፍያ ወይም ያልተፈታ ጉዳይ መጠናቀቅ አለበት። ይህንን አጣርቼ ትኩረትዎን የሚሻ ነገር ካለ አሳውቅዎታለሁ። እባክዎ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድዎን በፍጹም አያጋሩ።

ጥያቄዎ በጉዳይ ቁጥር {{ticket_id}} ተመዝግቧል፤ ስልጣን ባለው ቡድናችን ይስተናገዳል።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry to see you go. Please confirm your registered email + phone, a recent booking/payment detail, and whether you also want your data deleted. Open bookings or payments must be settled first. Never share codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ መሄድዎ ያሳዝነናል። እባክዎ የተመዘገበ ኢሜይል + ስልክዎን፣ የቅርብ ቀጠሮ/ክፍያ ዝርዝር እና መረጃዎ እንዲሰረዝ ይፈልጉ እንደሆነ ያረጋግጡ። ያልተጠናቀቁ ቀጠሮዎች ወይም ክፍያዎች መጀመሪያ መፈታት አለባቸው። ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your account closure request is still being processed by our authorized team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የመለያ መዝጊያ ጥያቄዎ አሁንም ስልጣን ባለው ቡድናችን እየተስተናገደ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- All verified deletion requests → **Senior Support / Supervisor** (authorized processing).
- Personal data deletion → **Trust & Safety** via tns-data-deletion-request.
- Seller accounts with listings/sessions → **Seller Operations**; any balance or pending payment/refund → **Payments & Finance**.
- Deletion requested because of compromise → **Trust & Safety**, Critical.

## Resolution Procedure
1. Authorized staff confirm the account is closed (or tell the customer what must be settled first).
2. Send the confirmation using approved wording.
3. Record request date, identity evidence, open items, and final outcome.

## Policy Pending Approval
- Define the account deletion/closure process, who approves it, and whether it is reversible.
- Define data-retention rules (what is kept, for how long, and why — e.g., financial records).
- Decide how upcoming bookings, refunds and seller balances are handled before closure.
- Decide whether a "deactivate" option exists separate from deletion, and the target processing time.

## Internal Notes
- Don't argue or try hard to retain the customer; one sincere offer to help is enough.
- Never tell the customer "all your data will be erased" — retention rules are pending.
- Duplicate-account cleanups: confirm which account is being closed in writing before escalating.

<!-- doc -->
# Account Recovery When Customer Lost Access to Email/Phone
id: acc-account-recovery-lost-access
type: article
category: account-access
subcategory: account-security
audience: both
priority: high
department: support_l2
features: accounts
tags: lost access to email, lost phone number, account recovery, can't reset password, old email, recover account, መለያዬን መመለስ, ኢሜይሌን ማግኘት አልችልም, ስልኬ ጠፍቷል
related: acc-forgot-password, acc-change-email, acc-change-phone, acc-unauthorized-access, tns-account-compromise, acc-tsg-login-master
templates: tpl-verify-identity, tpl-never-share-otp-warning
policy_pending: yes

## Summary
The customer can't log in and can't use password reset because they no longer have access to the registered email and/or phone. Recovery requires a careful identity check and is decided by authorized staff.

## Issue Description
This is the highest-risk access request: if an attacker convinces support to recover an account, they get full control (bookings, personal data and, for sellers, earnings). At the same time, real customers lose phones and old emails all the time. The agent's role is to collect strong evidence and escalate — **never** to recover the account directly.

## Possible Causes
- Old email account closed, hacked or forgotten.
- Phone lost/stolen, SIM expired or number recycled.
- Account was registered by a relative/assistant with their email/phone.
- Account was taken over and the attacker changed the email/phone.

## Information to Collect
**Interim identity check (until the official procedure is approved):**
- **A. Contact channel / registered contact:** the customer states the registered email **and** phone (you never reveal them), and explains which one they still have access to, if any.
- **B. Account knowledge (at least two):**
  - Full name on the account
  - A recent booking: consultation name, seller/consultant, date and time
  - A recent transaction: transaction reference, amount, date, payment method
  - Approximate registration date or first booking date
  - For sellers: listing titles, application submission date
- The new email/phone they want to use, and why they lost access.

> [!WARNING] Never ask for passwords, OTP codes, PINs or card numbers. Never read account details aloud for the customer to confirm ("Is your email abc@…?"). If answers don't match, do not reveal which answer was wrong.

## Troubleshooting Steps
1. Check whether a normal reset is possible with **either** registered email or phone. If they still have one of them → *Forgotten password*.
2. If not, run the interim identity check (A + at least two items from B). Record which items were given and whether they matched (do not store secrets).
3. Check the account history for risk signals: recent email/phone/password changes not made by the customer, new logins, seller payout details changed, withdrawals requested.
4. Decide:
   - **Strong match, no risk signals** → escalate to **Senior Support** for recovery by authorized staff.
   - **Signs of takeover** (details recently changed, unfamiliar activity) → *Unauthorized access*, **Trust & Safety**, Critical.
   - **Weak or mismatched answers** → do not proceed; escalate to **Trust & Safety** without telling the customer which detail failed.
5. Tell the customer the request is under review; no timeline or outcome promises.
6. Once recovered: customer sets a new password, verifies new contact details, reviews bookings and (sellers) payout details.

- [ ] Normal reset ruled out
- [ ] Identity check completed and recorded
- [ ] Risk signals reviewed
- [ ] Escalated to authorized staff / Trust & Safety

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry you've lost access to your email/phone — we'll do our best to help you get back into your account safely.

To confirm you are the account owner, please send:
1. The email address and phone number registered on your account
2. Your full name as it appears on the account
3. Details of a recent booking or payment (for example, the consultation name, consultant and date, or the transaction reference and amount)
4. The new email or phone number you'd like to use

Please do not send your password or any verification code — we will never ask for them.

Your request will be reviewed carefully by our authorized team to protect your account. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ኢሜይልዎን/ስልክዎን ማግኘት ባለመቻልዎ እናዝናለን — ወደ መለያዎ ደህንነቱ በተጠበቀ መንገድ እንዲመለሱ የተቻለንን ሁሉ እናደርጋለን።

የመለያው ባለቤት መሆንዎን ለማረጋገጥ እባክዎ የሚከተሉትን ይላኩ፦
1. በመለያዎ ላይ የተመዘገበውን ኢሜይል እና ስልክ ቁጥር
2. በመለያው ላይ የሰፈረውን ሙሉ ስምዎን
3. የቅርብ ጊዜ ቀጠሮ ወይም ክፍያ ዝርዝር (ለምሳሌ የምክክሩ ርዕስ፣ አማካሪው እና ቀኑ፣ ወይም የግብይት መለያ ቁጥሩ እና መጠኑ)
4. ሊጠቀሙበት የሚፈልጉትን አዲስ ኢሜይል ወይም ስልክ ቁጥር

እባክዎ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አይላኩ — በፍጹም አንጠይቅዎትም።

መለያዎን ለመጠበቅ ጥያቄዎ ስልጣን ባለው ቡድናችን በጥንቃቄ ይገመገማል። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, to recover your account please send: registered email + phone, full name on the account, a recent booking/payment detail, and your new email/phone. Never send passwords or codes. Our authorized team will review it. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ መለያዎን ለመመለስ እባክዎ፦ የተመዘገበ ኢሜይል + ስልክ፣ በመለያው ላይ ያለ ሙሉ ስም፣ የቅርብ ቀጠሮ/ክፍያ ዝርዝር እና አዲሱን ኢሜይል/ስልክ ይላኩ። የይለፍ ቃል ወይም ኮድ አይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your account recovery request is still being reviewed by our authorized team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የመለያ መመለሻ ጥያቄዎ አሁንም ስልጣን ባለው ቡድናችን እየተገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Identity check passed, no risk signals → **Senior Support / Supervisor** (authorized recovery).
- Takeover signs or mismatched answers → **Trust & Safety**, Critical/High.
- Seller with earnings or pending withdrawals → also **Payments & Finance** (protect funds).
- Customer has an imminent paid session → priority High; Senior Support may coordinate with the seller.

## Resolution Procedure
1. Authorized staff recover the account and record the approval.
2. Confirm the customer set a new password and verified new contact details.
3. Ask the customer to review recent activity; record evidence, decision and actions in the ticket.

## Policy Pending Approval
- Approve the official identity verification procedure for recovery: required factors, whether ID documents may be requested and how they are handled securely, who approves.
- Decide waiting/hold periods for sensitive actions (withdrawals, payout changes) after recovery.
- Define the process when the customer fails verification but appears genuine.

## Internal Notes
- Social engineers are friendly, urgent and well-prepared. Follow the checklist every time, even for regular customers you "recognise".
- Don't accept screenshots of the account as identity proof — they can be edited.
- Never discuss recovery evidence in group chats; keep it in the ticket only.

<!-- doc -->
# Unauthorized Access: Someone Else Logged Into My Account
id: acc-unauthorized-access
type: article
category: account-access
subcategory: account-security
audience: both
priority: critical
department: trust_safety
features: accounts
tags: hacked account, someone logged into my account, unauthorized access, account compromised, strange bookings, password changed not me, መለያዬ ተጠልፏል, ሌላ ሰው ገብቷል, ሀክ
related: tns-account-compromise, acc-security-concern-phishing, acc-account-recovery-lost-access, acc-change-email, acc-locked-account, acc-tsg-login-master
templates: tpl-account-compromise-urgent, tpl-never-share-otp-warning, tpl-verify-identity
policy_pending: yes

## Summary
The customer believes someone else accessed their account — unknown logins, changed details, bookings or payments they didn't make, or codes they didn't request. This is a Critical case for Trust & Safety.

## Issue Description
Signs reported by customers: password suddenly not working, "password changed" or login alerts they didn't trigger, email/phone changed, unfamiliar bookings or messages, payments they didn't make, seller listings or payout details changed, withdrawals they didn't request. Money and personal data may be at risk, so act immediately and escalate.

## Possible Causes
- The customer shared a code or password with someone pretending to be Byfluence or a seller (phishing).
- Reused password leaked from another website.
- Lost/stolen phone or SIM swap.
- Shared device or someone close who knows the password.
- Malware or a fake login page.

## Information to Collect
- Registered email/phone and identity check items (see *Account recovery*)
- What they noticed and when (timeline)
- Whether they can still log in
- Whether they shared any code/password, clicked a link, or lost their phone
- Unfamiliar bookings, payments, messages, listings, payout changes or withdrawals
- Screenshots of suspicious messages or alerts

> [!WARNING] Never ask for the password or codes — not even "to check". Never ask the customer to log in while you watch via screen share.

## Troubleshooting Steps
1. Mark the ticket **Critical** and escalate to **Trust & Safety** immediately (do not wait to finish all steps). Use tpl-account-compromise-urgent.
2. Guide the customer through immediate protective steps:
   - **If they can still log in:** change the password now (a new one not used elsewhere); log out of other sessions if the option exists; check email/phone on the account.
   - **Secure their email account and phone** too — whoever controls them can reset Byfluence.
   - Do not click links in suspicious messages; never share codes.
3. If they cannot log in → collect identity check items for recovery (*Account recovery*); Trust & Safety decides.
4. Check the admin dashboard for recent changes and activity: contact detail changes, bookings, transactions, seller payout details, withdrawal requests. Record findings.
5. **Sellers:** ask Trust & Safety and **Payments & Finance** to review/hold pending withdrawals and payout changes (authorized staff only).
6. **Payments the customer didn't make** → collect transaction references and involve **Payments & Finance**.
7. Keep the customer updated; no promises about refunds or reversals.

- [ ] Ticket Critical + Trust & Safety notified
- [ ] Protective steps given to customer
- [ ] Recent activity reviewed and recorded
- [ ] Payments/withdrawals flagged to Payments & Finance (if any)

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for telling us right away — we are treating this as urgent. Your case number is {{ticket_id}} and it has been passed to our security team.

Please do these steps now:
1. If you can still log in, change your Byfluence password immediately to a new one you don't use anywhere else.
2. Secure your email account and phone as well, since they can be used to reset your password.
3. Don't click links in suspicious messages, and never share your password or verification codes with anyone — Byfluence will never ask for them.

Please reply with what you noticed and when (for example, unknown bookings, payments or changed details), and any screenshots of suspicious messages. We will contact you with an update as soon as possible.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ወዲያውኑ ስላሳወቁን እናመሰግናለን — ጉዳዩን እንደ አስቸኳይ እየያዝነው ነው። የጉዳይዎ ቁጥር {{ticket_id}} ሲሆን ለደህንነት ቡድናችን ተላልፏል።

እባክዎ እነዚህን ደረጃዎች አሁኑኑ ይውሰዱ፦
1. አሁንም መግባት ከቻሉ፣ የByfluence የይለፍ ቃልዎን ወዲያውኑ በሌላ ቦታ በማይጠቀሙበት አዲስ የይለፍ ቃል ይቀይሩ።
2. የይለፍ ቃልዎን ለመቀየር ሊያገለግሉ ስለሚችሉ የኢሜይል መለያዎን እና ስልክዎንም ደህንነታቸውን ያረጋግጡ።
3. በአጠራጣሪ መልዕክቶች ውስጥ ያሉ ሊንኮችን አይጫኑ፤ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድዎን ለማንም አያጋሩ — Byfluence በፍጹም አይጠይቅዎትም።

እባክዎ ምን እንዳስተዋሉ እና መቼ እንደሆነ (ለምሳሌ የማያውቋቸው ቀጠሮዎች፣ ክፍያዎች ወይም የተቀየሩ መረጃዎች) እና የአጠራጣሪ መልዕክቶችን ስክሪንሾት ይላኩልን። በተቻለ ፍጥነት መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, we're treating this as urgent. If you can log in, change your password now; secure your email and phone too. Never share codes. Send what you noticed + screenshots. Security team notified. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ጉዳዩን እንደ አስቸኳይ እየያዝነው ነው። መግባት ከቻሉ የይለፍ ቃልዎን አሁኑኑ ይቀይሩ፤ ኢሜይልዎን እና ስልክዎንም ይጠብቁ። ኮድ አያጋሩ። ያስተዋሉትን እና ስክሪንሾት ይላኩ። የደህንነት ቡድኑ ተነግሮታል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our security team is actively reviewing your account. We will contact you again by {{follow_up_time}}. Meanwhile, please keep your password and codes private and tell us immediately if you notice anything new.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የደህንነት ቡድናችን መለያዎን በንቃት እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። እስከዚያው የይለፍ ቃልዎን እና ኮዶችዎን ለማንም አያጋሩ፤ አዲስ ነገር ካስተዋሉ ወዲያውኑ ያሳውቁን።

## Escalation Conditions
- Every suspected unauthorized access → **Trust & Safety**, **Critical**.
- Unauthorized payments → also **Payments & Finance**.
- Seller payout changes or withdrawals → **Payments & Finance** + **Trust & Safety** immediately.
- Many accounts reporting compromise → **Trust & Safety** + **Technical / Engineering** + supervisor (possible breach); **Management** if confirmed.

## Resolution Procedure
1. Trust & Safety confirms the account is secured (customer in control, contact details correct, new password set).
2. Unauthorized bookings/payments/withdrawals handled by the responsible teams.
3. Customer informed of outcome using approved wording.
4. Record the timeline, root cause (phishing, reuse, SIM swap…), actions, and decisions.

## Policy Pending Approval
- Approve the official compromise response procedure (who can lock/secure accounts, hold withdrawals, reverse changes).
- Decide refund/reversal rules for unauthorized transactions.
- Decide whether and how affected customers are notified in a wider incident.

## Internal Notes
- Speed matters more than completeness — escalate first, gather details second.
- Customers often feel embarrassed if they shared a code. Be reassuring, not judgmental; the details help us stop the attacker.
- Never confirm or deny to a third party that an account was compromised.

<!-- doc -->
# Phishing Messages or Fake Byfluence Contacts
id: acc-security-concern-phishing
type: article
category: account-access
subcategory: account-security
audience: both
priority: high
department: trust_safety
features: accounts
tags: phishing, scam message, fake byfluence, fake support, someone asked for my code, suspicious link, telegram scam, ማጭበርበሪያ መልዕክት, ሐሰተኛ Byfluence, ኮዴን ጠየቁኝ
related: acc-unauthorized-access, tns-account-compromise, reg-suspicious-registration, gen-contact-support, acc-forgot-password
templates: tpl-never-share-otp-warning, tpl-account-compromise-urgent, tpl-request-screenshot
policy_pending: yes

## Summary
The customer received a suspicious message, call, link or Telegram contact claiming to be Byfluence (or a Byfluence seller) asking for codes, passwords, payments or personal details.

## Issue Description
Scammers impersonate support agents, sellers or "Byfluence verification" to steal codes and passwords, or to get customers to pay outside the platform. Customers may ask "is this message really from you?" or report they already shared a code. If they shared anything, it becomes an *Unauthorized access* case.

Typical patterns:
- "Your account will be closed — send us the code we just sent you."
- A fake Telegram account using the Byfluence name/logo offering "support".
- A link to a page that looks like Byfluence login but is a different web address.
- A seller asking the buyer to pay directly by mobile money/bank instead of through Byfluence.
- Offers of "seller approval" or "verification" for a fee.

## Possible Causes
- Targeted phishing using the customer's public details.
- The customer's phone number/email leaked from another service.
- Fake social-media pages or Telegram channels using the brand.
- A dishonest seller trying to move the transaction off-platform.

## Information to Collect
- Screenshot of the message/profile (including sender number, username or email address)
- The link shown (ask them to copy the text, **not** open it)
- Date/time and channel (SMS, Telegram, call, email, social media)
- Whether they replied, clicked, paid, or shared any code/password/personal data

> [!WARNING] Never ask for the code or password the scammer requested. Do not open suspicious links yourself on a work device.

## Troubleshooting Steps
1. Reassure the customer: Byfluence never asks for passwords, verification codes or PINs.
2. Ask whether they shared anything or clicked a link:
   - **Shared a code/password or logged in via the link** → treat as compromise: *Unauthorized access*, **Trust & Safety**, Critical.
   - **Paid someone off-platform** → collect payment details; **Trust & Safety**; explain we can't promise recovery of off-platform payments.
   - **Didn't share anything** → advise to ignore/block/report the sender.
3. Collect screenshots and sender details and record them in the ticket.
4. Escalate to **Trust & Safety** (priority High) so the fake account/page can be reported and other customers warned.
5. Remind the customer to use only official Byfluence channels: {{support_channel}} and the website https://byfluence.com.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for reporting this — you did the right thing by checking with us.

Byfluence will never ask for your password, verification codes or PINs, and will never ask you to pay outside the Byfluence website. Please don't reply to that message, don't open the link, and block the sender.

If you have already shared a code or password, or clicked the link and logged in, please tell me right away so we can help protect your account.

Could you please send a screenshot of the message, including the sender's number, username or email? We'll pass it to our security team. For support, please only use our official channel: {{support_channel}}.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጉዳዩ ስላሳወቁን እናመሰግናለን — ከእኛ ጋር በማረጋገጥዎ ትክክለኛውን ነገር አድርገዋል።

Byfluence የይለፍ ቃልዎን፣ የማረጋገጫ ኮድዎን ወይም ፒንዎን በፍጹም አይጠይቅም፤ ከByfluence ድረ-ገጽ ውጭ እንዲከፍሉም አይጠይቅዎትም። እባክዎ ለዚያ መልዕክት ምላሽ አይስጡ፣ ሊንኩን አይክፈቱ፣ ላኪውንም ያግዱት (block)።

ኮድ ወይም የይለፍ ቃል አስቀድመው አጋርተው ከሆነ፣ ወይም ሊንኩን ከፍተው ከገቡ፣ መለያዎን እንድንጠብቅ እባክዎ ወዲያውኑ ይንገሩኝ።

እባክዎ የመልዕክቱን ስክሪንሾት ከላኪው ስልክ ቁጥር፣ የተጠቃሚ ስም ወይም ኢሜይል ጋር ይላኩልኝ? ለደህንነት ቡድናችን እናስተላልፈዋለን። ለድጋፍ እባክዎ ኦፊሴላዊ መስመራችንን ብቻ ይጠቀሙ፦ {{support_channel}}።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for checking! Byfluence never asks for passwords, codes or PINs, or for payment outside our website. Don't reply or open the link; block the sender and send us a screenshot. Already shared a code? Tell me now. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላረጋገጡ እናመሰግናለን! Byfluence የይለፍ ቃል፣ ኮድ ወይም ፒን፣ ወይም ከድረ-ገጻችን ውጭ ክፍያ በፍጹም አይጠይቅም። ምላሽ አይስጡ፣ ሊንኩን አይክፈቱ፤ ላኪውን አግደው ስክሪንሾት ይላኩልን። ኮድ አጋርተው ከሆነ አሁኑኑ ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our security team is reviewing the message you reported. Thank you for helping keep Byfluence safe — we will contact you again by {{follow_up_time}} if we need anything further. Remember: never share your codes or password.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ያሳወቁትን መልዕክት የደህንነት ቡድናችን እየገመገመ ነው። Byfluenceን ደህንነቱ የተጠበቀ ለማድረግ ስለረዱን እናመሰግናለን — ተጨማሪ ነገር ካስፈለገን እስከ {{follow_up_time}} ድረስ እናገኝዎታለን። ያስታውሱ፦ ኮድዎን ወይም የይለፍ ቃልዎን ለማንም አያጋሩ።

## Escalation Conditions
- All phishing / impersonation reports → **Trust & Safety**, High.
- Customer shared a code/password or logged in via the link → **Trust & Safety**, Critical (*Unauthorized access*).
- Off-platform payment to a scammer or seller → **Trust & Safety**; **Payments & Finance** if a Byfluence transaction is involved.
- A Byfluence seller is involved in the scam → also **Seller Operations**.
- Many customers receiving the same message → supervisor + **Trust & Safety** (campaign); consider an Announcement.

## Resolution Procedure
1. Confirm the customer has not shared credentials (or the compromise case is open).
2. Confirm evidence was passed to Trust & Safety.
3. Record sender details and the pattern in the ticket for trend tracking.

## Policy Pending Approval
- Publish the official list of Byfluence support channels (Telegram handle, email address, phone number) so agents and customers can verify them.
- Confirm the official sender name/domain for Byfluence emails and SMS.
- Decide the process for reporting fake pages/accounts and warning customers.

## Internal Notes
- Agents must never contact customers from personal Telegram or phone accounts — it trains customers to trust fake contacts.
- Until official channels are confirmed, use the {{support_channel}} placeholder; do not type handles or numbers from memory.
- Off-platform payments are a major marketplace risk; always record them even if the customer doesn't want to pursue it.
