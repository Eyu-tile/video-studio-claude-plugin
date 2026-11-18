<!-- doc -->
# Email Address Rejected as Invalid
id: reg-invalid-email
type: article
category: registration
subcategory: registration-errors
audience: both
priority: low
department: support_l1
features: accounts
tags: invalid email, email not accepted, email format error, wrong email, enter valid email, ኢሜይል አይቀበልም, ትክክለኛ ኢሜይል, የኢሜይል ስህተት
related: reg-registration-error-generic, reg-email-verification, reg-unsupported-method, reg-how-to-create-account, reg-tsg-registration-master
templates: tpl-request-screenshot
policy_pending: yes

## Summary
The sign-up form says the email address is invalid, so the customer cannot continue registration.

## Issue Description
The customer types their email and sees a message such as "Enter a valid email address". Many Ethiopian customers use their email rarely, or only on their phone, and may not remember the exact spelling. Some customers do not have an email address at all.

## Possible Causes
- Typo: missing `@`, missing dot, `gmail.con`, `gmial.com`, `yahoo.co` instead of `yahoo.com`.
- A space before, inside or after the address (phone keyboards often add a space after autocomplete).
- The phone's autocorrect changed or capitalised part of the address.
- A comma used instead of a dot.
- Ethiopic letters or other non-Latin characters typed with an Amharic keyboard.
- The customer typed their phone number or name in the email field.
- The email domain is blocked by the system (e.g., temporary/disposable email services) — not confirmed.
- The customer does not actually have an email address.

## Information to Collect
- The email address exactly as they are typing it (ask them to type it in the chat)
- A screenshot of the error message
- Whether they can open this email inbox right now

## Troubleshooting Steps
1. Ask the customer to type the address in the chat so you can see the spelling. Check for `@`, the domain spelling and the ending (`.com`, `.et`, etc.).
2. Ask them to delete the field and retype it slowly using the English keyboard, without spaces, and to make sure autocorrect has not changed it.
3. Confirm they can open that inbox — if not, the verification email will never reach them.
4. If the address is correct and still rejected, ask for a screenshot and try a different email provider address (if they have one).
5. If the customer has no email address: explain that the form may require one (if confirmed), and see *Unsupported registration methods* for alternatives. Do not create an email for them.
6. If correct addresses from a common domain are being rejected for several customers → escalate to **Technical / Engineering**.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. Let's fix the email error together.

Please delete the email address in the form and type it again slowly, using the English keyboard and without any spaces. Check that it has an "@" and ends correctly (for example "@gmail.com"). On phones, autocorrect sometimes changes the address — please check it carefully before submitting.

If it's still rejected, please type your email address here in the chat and send a screenshot of the error, and I'll check it for you.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የኢሜይሉን ስህተት አብረን እናስተካክል።

እባክዎ በቅጹ ላይ ያለውን የኢሜይል አድራሻ አጥፍተው በእንግሊዝኛ ኪቦርድ፣ ያለ ምንም ክፍተት በቀስታ እንደገና ይጻፉት። "@" ምልክት እንዳለው እና በትክክል እንደሚያልቅ (ለምሳሌ "@gmail.com") ያረጋግጡ። በስልክ ላይ autocorrect አንዳንዴ አድራሻውን ይቀይራል — ከመላክዎ በፊት እባክዎ በጥንቃቄ ይመልከቱ።

አሁንም ተቀባይነት ካላገኘ፣ እባክዎ የኢሜይል አድራሻዎን እዚሁ ይጻፉልኝ እና የስህተቱን ስክሪንሾት ይላኩ፤ አጣራልዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please retype your email slowly on the English keyboard, with no spaces, and check the "@" and ending (e.g. @gmail.com). Still rejected? Type it here + send a screenshot. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ ኢሜይልዎን በእንግሊዝኛ ኪቦርድ፣ ያለ ክፍተት በቀስታ እንደገና ይጻፉ፤ "@" እና መጨረሻውን (ለምሳሌ @gmail.com) ያረጋግጡ። ካልሰራ እዚህ ይጻፉት እና ስክሪንሾት ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- A correctly formatted address from a common provider is rejected → **Technical / Engineering**.
- The customer has no email and no supported alternative exists → **Senior Support / Supervisor** (log as a policy gap).

## Resolution Procedure
1. Confirm the email was accepted and the customer can open the verification message (if any).
2. Record the cause (typo, space, keyboard, blocked domain, no email) before resolving.

## Policy Pending Approval
- Confirm whether an email address is mandatory for registration.
- Confirm whether any email domains (disposable or otherwise) are blocked.

## Internal Notes
- Read the address back letter by letter on phone calls (e.g., "g-m-a-i-l dot com").
- Do not suggest the customer use a relative's email unless they understand that all resets and messages will go there.

<!-- doc -->
# "Email or Phone Already Registered" Error
id: reg-email-already-used
type: article
category: registration
subcategory: registration-errors
audience: both
priority: medium
department: support_l1
features: accounts
tags: email already registered, phone already in use, account already exists, already taken, can't register, email exists, ኢሜይሉ ተመዝግቧል, ስልኩ ተመዝግቧል, አካውንት አለ
related: acc-forgot-password, reg-duplicate-accounts, reg-phone-verification, acc-unauthorized-access, reg-tsg-registration-master
templates: tpl-password-reset-guide, tpl-verify-identity
policy_pending: yes

## Summary
The customer tries to register but the form says their email address or phone number is already registered.

## Issue Description
The customer believes they are new, or has forgotten they registered before. Less often, the email/phone was used by someone else (a relative, a previous owner of a recycled phone number, or someone misusing their details). The customer cannot create a new account with that email/phone.

## Possible Causes
- The customer registered before (perhaps an incomplete or unverified registration) and forgot.
- They registered moments ago, the page was slow, and they submitted again.
- A family member registered using the customer's email/phone.
- The phone number was recycled by the operator and the previous owner had a Byfluence account.
- Someone registered with the customer's email/phone without permission.
- A previously closed/deleted account still holds the email/phone (data retention rules not confirmed).

## Information to Collect
- The email/phone they are trying to register with
- Whether they remember registering before or using Byfluence (bookings, payments)
- Whether anyone else may have used their email/phone
- For phone numbers: how long they have had the SIM

> [!WARNING] Do not confirm or reveal any detail of the existing account (name, bookings, other contact details) until the customer has proven they own it. Never ask for passwords or codes.

## Troubleshooting Steps
1. Ask the customer to try **logging in** with that email/phone. If they don't remember the password, guide them through *Forgotten password*.
2. If the password reset message arrives and they can log in → resolved; it was their own account.
3. If the reset message reaches them but they don't recognise the account's contents → it may be an old registration of theirs or a relative's. Verify identity (see *Account recovery*) before discussing the account.
4. If the reset message does **not** reach them (e.g., phone number recycled, or email belongs to them but account isn't theirs):
   - Search the admin dashboard; check account status, verification state and recent activity — do not share details.
   - Recycled phone number → escalate to **Senior Support** to decide on releasing the number (policy pending).
   - Account with the customer's email that they say they never created → **Trust & Safety**.
5. If the customer has two half-finished registrations → follow *Customer has duplicate accounts*.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. This message usually means an account has already been created with this email address or phone number — often from an earlier registration that was not finished.

Please try to log in with it. If you don't remember the password, choose "Forgot password" on the login page and follow the instructions sent to your email or phone.

If the reset message doesn't reach you, or you're sure you never registered before, please reply and let me know. For your security I can't share details of the existing account here, but I will check it with the responsible team. Please never share your password or verification codes with anyone.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ይህ መልዕክት ብዙውን ጊዜ የሚመጣው በዚህ ኢሜይል ወይም ስልክ ቁጥር ቀደም ብሎ መለያ ሲከፈት ነው — ብዙ ጊዜ ያልተጠናቀቀ የቀድሞ ምዝገባ ሊሆን ይችላል።

እባክዎ በዚሁ ኢሜይል/ስልክ ለመግባት ይሞክሩ። የይለፍ ቃሉን ካላስታወሱ፣ በመግቢያ ገጹ ላይ "Forgot password" የሚለውን ይምረጡ እና ወደ ኢሜይልዎ ወይም ስልክዎ የሚላከውን መመሪያ ይከተሉ።

የመቀየሪያ መልዕክቱ ካልደረሰዎት ወይም ከዚህ በፊት እንዳልተመዘገቡ እርግጠኛ ከሆኑ፣ እባክዎ መልሰው ያሳውቁኝ። ለደህንነትዎ ሲባል ስለ ነባሩ መለያ ዝርዝር መረጃ እዚህ ማጋራት አልችልም፤ ነገር ግን ከሚመለከተው ቡድን ጋር አጣራለሁ። እባክዎ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድዎን ለማንም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, this usually means an account already exists with that email/phone. Please try logging in or use "Forgot password". If the reset doesn't reach you, tell me and I'll check. Never share codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይህ ብዙውን ጊዜ በዚያ ኢሜይል/ስልክ መለያ እንዳለ ያሳያል። እባክዎ ለመግባት ይሞክሩ ወይም "Forgot password" ይጠቀሙ። መልዕክቱ ካልደረሰዎት ይንገሩኝ፣ አጣራለሁ። ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are still reviewing the existing registration linked to your email or phone number. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ከኢሜይልዎ ወይም ስልክ ቁጥርዎ ጋር የተያያዘውን ነባር ምዝገባ አሁንም እየገመገምን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Recycled phone number held by another account → **Senior Support / Supervisor**.
- Customer says they never registered and the account shows activity (bookings, payments, seller application) → **Trust & Safety**, priority High.
- The existing account is suspended or banned and the customer is trying to register again → **Trust & Safety** (possible ban evasion); do not disclose the status reason.

## Resolution Procedure
1. Confirm the customer can log in to their own account, or that the conflict has been passed to the right team.
2. Record which case it was (forgotten account, recycled number, relative, misuse) before resolving.

## Policy Pending Approval
- Define the process and identity check for releasing an email/phone held by an old or unverified account.
- Confirm whether a closed/deleted account frees its email/phone for new registrations.
- Decide whether unverified registrations are automatically removed after a period.

## Internal Notes
- Treat "someone else has my email registered" as a potential privacy/security incident, not a nuisance.
- Never reveal an account's name or details to "help the customer remember" — ask them to recall it instead.

<!-- doc -->
# Registration Form Error or Form Won't Submit
id: reg-registration-error-generic
type: article
category: registration
subcategory: registration-errors
audience: both
priority: medium
department: technical
features: accounts
tags: registration error, sign up not working, form won't submit, button not working, something went wrong, page loading, password requirements, ምዝገባ አይሰራም, ቅጹ አይላክም, ስህተት ተፈጥሯል
related: reg-invalid-email, reg-email-already-used, tec-clear-cache-cookies, reg-tsg-registration-master, reg-unsupported-method
templates: tpl-request-screenshot
policy_pending: yes

## Summary
The customer fills in the sign-up form but gets an error, the submit button does nothing, or the page keeps loading.

## Issue Description
The customer cannot finish registration. They may see a specific field error (password rules, missing field), a general message ("Something went wrong"), or nothing at all. This often happens on older phones, slow connections, or when the browser auto-translates the page.

## Possible Causes
- A required field is empty or invalid and the error is shown off-screen (scroll up/down).
- The password doesn't meet the rules (length, letters/numbers/symbols).
- Terms checkbox or captcha not completed.
- Slow or unstable internet; the request timed out.
- Browser auto-translation (e.g., Chrome translating the page to Amharic/English) breaking the form.
- Ad blockers, data-saver modes (Opera Mini, Chrome Lite) or old browsers blocking scripts.
- Outdated cached files after a site update.
- A server error or incident on the Byfluence side.

## Information to Collect
- Screenshot of the form and any error message (password field hidden)
- Device and browser (e.g., "Android, Chrome", "iPhone, Safari", "Opera Mini")
- Internet connection type (mobile data or Wi-Fi)
- Date and time of the attempt
- Whether the page was translated by the browser

> [!WARNING] Ask the customer to hide or blank the password field before taking a screenshot. Never ask for the password itself.

## Troubleshooting Steps
1. Ask for a screenshot and read the exact message.
2. **Field error** → explain the specific fix (e.g., password needs more characters; tick the terms box).
3. **No message / button does nothing:**
   - Scroll the whole form to look for a red error message.
   - Turn off browser translation for the page.
   - Disable data-saver/"lite" mode or try a standard browser (Chrome, Safari, Firefox).
   - Try the other connection (mobile data ↔ Wi-Fi).
   - Clear cache and cookies (tec-clear-cache-cookies), or use a private/incognito window.
4. **"Something went wrong" / server error** → check Announcements for an incident. Ask the customer to try again a little later.
5. Before re-trying, check the admin dashboard — the account may have been created despite the error. If so, guide them to log in and avoid creating a duplicate.
6. Still failing on a standard browser → escalate to **Technical / Engineering** with screenshot, device, browser, time and the email/phone used.

- [ ] Screenshot reviewed
- [ ] Field errors fixed
- [ ] Different browser / connection tried
- [ ] Checked whether the account was created anyway

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry the registration form isn't working for you.

Please try these steps:
1. Scroll through the whole form and look for any message in red — a field may need correcting.
2. If your browser has translated the page, switch translation off and try again.
3. Try a different browser (such as Chrome or Safari) or a private/incognito window, and switch between mobile data and Wi-Fi.

If it still doesn't work, please send me a screenshot of the page (with the password box hidden), and tell me your phone/computer and browser. Please don't send your password.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ የመመዝገቢያ ቅጹ ስላልሰራልዎ ይቅርታ እንጠይቃለን።

እባክዎ እነዚህን ደረጃዎች ይሞክሩ፦
1. ቅጹን ከላይ እስከ ታች ይመልከቱ፤ በቀይ የተጻፈ መልዕክት ካለ አንድ መስክ መስተካከል ሊያስፈልገው ይችላል።
2. ብራውዘርዎ ገጹን ተርጉሞት ከሆነ፣ ትርጉሙን አጥፍተው እንደገና ይሞክሩ።
3. ሌላ ብራውዘር (ለምሳሌ Chrome ወይም Safari) ወይም private/incognito መስኮት ይሞክሩ፤ በሞባይል ዳታ እና በWi-Fi መካከልም ይቀያይሩ።

አሁንም ካልሰራ፣ እባክዎ የገጹን ስክሪንሾት (የይለፍ ቃሉ ሳጥን ተደብቆ) ይላኩልኝ፤ የሚጠቀሙትን ስልክ/ኮምፒውተር እና ብራውዘር ይንገሩኝ። እባክዎ የይለፍ ቃልዎን አይላኩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry! Check the form for red error messages, turn off page translation, and try another browser or incognito window. Still stuck? Send a screenshot (password hidden) + your device/browser. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! በቅጹ ላይ ቀይ የስህተት መልዕክት ካለ ይመልከቱ፣ የገጽ ትርጉምን ያጥፉ፣ ሌላ ብራውዘር ወይም incognito ይሞክሩ። ካልሰራ ስክሪንሾት (የይለፍ ቃል ተደብቆ) እና መሳሪያዎን/ብራውዘርዎን ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our technical team is still investigating the registration error you reported. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ያሳወቁንን የምዝገባ ስህተት የቴክኒክ ቡድናችን አሁንም እያጣራ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Error persists on a standard, up-to-date browser → **Technical / Engineering**.
- "Something went wrong"/server errors reported by several customers → **Technical / Engineering** incident; notify supervisor.
- The form blocks a customer for reasons that look like an automated fraud flag → **Trust & Safety** (do not tell the customer they are flagged).

## Resolution Procedure
1. Confirm the customer registered successfully (account visible in admin dashboard) and can log in.
2. Check no duplicate accounts were created during repeated attempts.
3. Record the cause and the device/browser in the ticket for trend tracking.

## Policy Pending Approval
- Confirm the password rules so agents can explain them exactly.
- Confirm the supported browsers and minimum versions.

## Internal Notes
- Auto-translate is a frequent, invisible cause for Amharic-speaking users with English browsers and vice versa.
- Opera Mini's server-side compression often breaks forms; recommend Chrome or the phone's default browser.
- Always check whether the account was created before telling the customer to try again.

<!-- doc -->
# Unsupported Registration Methods (Social Login, No Email, Foreign Numbers)
id: reg-unsupported-method
type: article
category: registration
subcategory: registration-errors
audience: both
priority: low
department: support_l1
features: accounts
tags: sign in with google, facebook login, telegram login, no email, foreign number, diaspora, register without phone, social login, በGoogle መግባት, ኢሜይል የለኝም, የውጭ ስልክ ቁጥር
related: reg-requirements, reg-invalid-email, reg-phone-verification, reg-how-to-create-account, gen-contact-support
policy_pending: yes

## Summary
The customer wants to register in a way the site may not support — "Sign in with Google/Facebook/Telegram", without an email address, without a phone, or with a non-Ethiopian phone number.

## Overview
Which sign-up methods are available is **not confirmed** in this knowledge base. Before answering, check the **Feature Status** page and the live sign-up page.

| Request | What to do |
|---|---|
| Sign in with Google / Facebook / Apple / Telegram | Only confirm if visible on the live sign-up page. Otherwise guide the customer through the standard form. |
| No email address | Check whether the live form allows phone-only sign-up. If an email is required, the customer may create a free email with a provider of their choice — do not create it for them. |
| No phone number | Check whether the form allows email-only sign-up. |
| Foreign phone number (diaspora, visitors) | Not confirmed. Do not promise. Log it and escalate if the customer needs a decision. |
| Registering through Telegram or by phone call with an agent | Not supported by support staff — agents never create accounts for customers. |

## Customer Steps
1. Open https://byfluence.com and check which sign-up options are shown on the page.
2. Use one of the options shown. If you don't have the required email or phone number, contact support and tell us what you have available.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your question. At the moment, please use the sign-up options shown on the Byfluence registration page at https://byfluence.com. If an option you'd like (such as signing in with another service, or using a phone number from outside Ethiopia) is not shown there, it is not available yet.

I have noted your request under case number {{ticket_id}} so our team can consider it. If you can't register with the options available, please tell me what contact details you do have, and I'll check what we can do.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለጥያቄዎ እናመሰግናለን። ለጊዜው እባክዎ https://byfluence.com የመመዝገቢያ ገጽ ላይ የሚታዩትን አማራጮች ይጠቀሙ። የሚፈልጉት አማራጭ (ለምሳሌ በሌላ አገልግሎት መግባት ወይም ከኢትዮጵያ ውጭ ያለ ስልክ ቁጥር መጠቀም) እዚያ ካልታየ፣ አሁን አይገኝም ማለት ነው።

ቡድናችን እንዲያጤነው ጥያቄዎን በጉዳይ ቁጥር {{ticket_id}} መዝግቤዋለሁ። ባሉት አማራጮች መመዝገብ ካልቻሉ፣ ያለዎትን የመገናኛ መረጃ ይንገሩኝ፤ ምን ማድረግ እንደምንችል አጣራለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please use the sign-up options shown on byfluence.com — if an option isn't shown, it isn't available yet. I've logged your request. Tell me what contact details you have if you're stuck. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ byfluence.com ላይ የሚታዩትን የምዝገባ አማራጮች ይጠቀሙ — የማይታይ አማራጭ ገና አይገኝም። ጥያቄዎን መዝግቤያለሁ። ከተቸገሩ ያለዎትን የመገናኛ መረጃ ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- A customer cannot register with any available method (e.g., diaspora buyer with only a foreign number) and needs a decision → **Senior Support / Supervisor**.
- A social-login button is shown but fails → **Technical / Engineering**.

## Policy Pending Approval
- Confirm which sign-up methods are live (email, phone, social login).
- Decide whether foreign phone numbers and diaspora users are supported.
- Decide whether there is an assisted-registration option for customers without email or a smartphone.

## Internal Notes
- Log every unsupported-method request with a clear tag (e.g., "request-google-login", "request-foreign-number") — this is product feedback.
- Never create an email account, Byfluence account, or password on the customer's behalf.

<!-- doc -->
# Account Created but Not Activated
id: reg-account-not-activated
type: article
category: registration
subcategory: activation
audience: both
priority: medium
department: support_l1
features: accounts
tags: account not active, account not activated, inactive account, pending activation, can't use account, verify account, መለያዬ አልነቃም, አካውንቱ አልሰራም, ማግበር
related: reg-email-verification, reg-otp-not-received, reg-account-approval, acc-cannot-login-after-registration, reg-tsg-registration-master
templates: tpl-otp-not-received, tpl-request-screenshot
policy_pending: yes

## Summary
The customer completed sign-up but the account is not active: they see "account not activated/verified", cannot log in, or cannot use key features.

## Issue Description
The customer believes registration is complete, but the system treats the account as inactive. This can be an unfinished verification step, a technical failure, or an internal review/flag. Buyers may be blocked from booking; sellers often confuse account activation with seller application approval.

## Possible Causes
- Email or phone verification was not completed (link not opened, code not entered).
- The verification link expired or the customer used an old code.
- The customer verified a different (duplicate) account.
- A technical error left the account in an inactive state.
- The account was held by automated checks (suspicious registration signals).
- The customer is actually a seller waiting for **seller application** approval — the account itself is active (see *Waiting for account approval*).

## Information to Collect
- Registered email or phone number
- Exact message shown, or a screenshot
- Whether they received and used a verification link/code
- Whether they are trying to buy or to sell

> [!WARNING] Never ask for passwords or verification codes.

## Troubleshooting Steps
1. Find the account in the admin dashboard and read its status and verification state.
2. Decide the case:
   - **Not verified** → guide the customer to complete verification (*Email verification link not received or expired* / *OTP not received*).
   - **Verified but shown inactive / error** → technical issue → escalate to **Technical / Engineering** with the account identifier and screenshot.
   - **Held/flagged by review** → do not disclose the reason; escalate to **Trust & Safety**; tell the customer the account is being reviewed.
   - **Account active, seller application pending** → explain the difference and use *Waiting for account approval*.
   - **No account found** → registration didn't complete; check for typos or a second account, then guide them to register.
3. Check for duplicate accounts with the customer's other email/phone.
4. Record findings in the ticket.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry your account isn't active yet.

In most cases this means a verification step wasn't completed. Please check your email (including Spam/Promotions) or SMS for a message from Byfluence, and open the newest link or enter the newest code on the site.

If you've already done this, please reply with the email or phone number you registered with and a screenshot of the message you see, and I will check your account status. Please don't share your password or any codes.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። መለያዎ ገና ስላልነቃ ይቅርታ እንጠይቃለን።

ብዙውን ጊዜ ይህ የሚሆነው አንድ የማረጋገጫ ደረጃ ሳይጠናቀቅ ሲቀር ነው። እባክዎ ኢሜይልዎን (Spam/Promotionsን ጨምሮ) ወይም ኤስኤምኤስዎን ከByfluence የመጣ መልዕክት ካለ ይመልከቱ፤ የቅርብ ጊዜውን ሊንክ ይክፈቱ ወይም የቅርብ ጊዜውን ኮድ በድረ-ገጹ ላይ ያስገቡ።

ይህንን አስቀድመው ካደረጉ፣ እባክዎ የተመዘገቡበትን ኢሜይል ወይም ስልክ ቁጥር እና የሚያዩትን መልዕክት ስክሪንሾት ይላኩልኝ፤ የመለያዎን ሁኔታ አጣራለሁ። እባክዎ የይለፍ ቃልዎን ወይም ማንኛውንም ኮድ አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, this usually means verification isn't finished. Check email/SMS for the newest Byfluence link or code. Already done? Send your registered email/phone + a screenshot and I'll check. Never share codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይህ ብዙውን ጊዜ ማረጋገጫው እንዳልተጠናቀቀ ያሳያል። በኢሜይል/ኤስኤምኤስ የቅርብ ጊዜውን የByfluence ሊንክ ወይም ኮድ ይጠቀሙ። ካደረጉት የተመዘገቡበትን ኢሜይል/ስልክ እና ስክሪንሾት ይላኩ። ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your account is still being checked by the responsible team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። መለያዎ አሁንም በሚመለከተው ቡድን እየተጣራ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Account verified but still inactive → **Technical / Engineering**.
- Account held by a review or fraud flag → **Trust & Safety** (do not disclose the flag).
- The customer has an upcoming paid booking and cannot access the account → **Senior Support / Supervisor**, priority High.

## Resolution Procedure
1. Confirm the account status is active in the admin dashboard and the customer can log in.
2. Record the cause before resolving.

## Policy Pending Approval
- Confirm the account states used for buyers (e.g., unverified, active, held) and their meaning.
- Decide what customers may be told when an account is held for review.

## Internal Notes
- Never activate or verify an account manually unless your role explicitly allows it.
- "Activated" for a seller usually means "my seller application is approved" — clarify which one the customer means.

<!-- doc -->
# Waiting for Account Approval
id: reg-account-approval
type: article
category: registration
subcategory: activation
audience: both
priority: medium
department: seller_ops
features: accounts, seller-onboarding, seller-verification
tags: waiting for approval, application pending, seller approval, account under review, when will I be approved, verification pending, ማመልከቻዬ መቼ ይጸድቃል, በግምገማ ላይ, ፈቃድ እየጠበቅሁ ነው
related: reg-account-not-activated, reg-seller-vs-buyer-account, sel-how-to-become-seller, reg-tsg-registration-master, gen-contact-support
templates: tpl-request-screenshot
policy_pending: yes

## Summary
The customer is waiting for their account or seller application to be approved and wants to know the status or when it will happen.

## Issue Description
Seller applications are reviewed before approval (confirmed onboarding flow: apply → info → identity verification → review → approved or rejected). Customers often ask repeatedly about timing, especially if they have clients waiting. Buyers sometimes believe their account is "waiting for approval" when it is actually unverified or held — there is **no confirmed approval step for buyer accounts**.

## Possible Causes
- **Seller application in review** (status Pending) — normal.
- Application incomplete: missing information or identity documents, unclear photos.
- Application needs additional checks by Seller Operations.
- Review backlog.
- Buyer account not verified (see *Account created but not activated*).
- Account held by a security/fraud review.

## Information to Collect
- Registered email or phone number
- Whether this is a buyer account or a seller application
- When they submitted the application (approximate date)
- Any message or email they received about missing information
- Screenshot of the status shown in their account

## Troubleshooting Steps
1. Find the account in the admin dashboard.
2. **Buyer account** → there is no confirmed approval step; check verification status and follow *Account created but not activated*.
3. **Seller application** → read the seller verification status:
   - **Pending** → check whether anything is missing (incomplete form, documents). If complete, tell the customer it is in review; do not give a date.
   - **Pending with missing information** → tell the customer exactly what is missing, if your access shows it; otherwise escalate to **Seller Operations**.
   - **Verified** → approval is done; guide them to complete their seller profile and create listings. Check operational status (Active/Suspended).
   - **Rejected** → do not argue or re-explain the reason beyond what Seller Operations has approved; follow the seller verification articles.
4. If the application has been pending for longer than the supervisor's internal guideline, escalate to **Seller Operations** with the submission date.
5. Record the status and next step in the ticket.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your patience while your application is reviewed. I have checked your account, and your application is currently in review with our team.

I'm not able to give an exact date, but I have noted your request under case number {{ticket_id}}. If we need any more information from you, we will contact you. You can also check the status in your account at any time.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ማመልከቻዎ እስኪገመገም በትዕግስት ስለጠበቁ እናመሰግናለን። መለያዎን አጣርቻለሁ፤ ማመልከቻዎ በአሁኑ ወቅት በቡድናችን እየተገመገመ ነው።

ትክክለኛ ቀን መስጠት አልችልም፤ ነገር ግን ጥያቄዎን በጉዳይ ቁጥር {{ticket_id}} መዝግቤዋለሁ። ተጨማሪ መረጃ ካስፈለገን እናገኝዎታለን። እንዲሁም ሁኔታውን በማንኛውም ጊዜ በመለያዎ ውስጥ ማየት ይችላሉ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your application is in review. I can't give an exact date, but we'll contact you if anything else is needed. You can check the status in your account. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ማመልከቻዎ በግምገማ ላይ ነው። ትክክለኛ ቀን መስጠት አልችልም፤ ተጨማሪ ነገር ካስፈለገ እናገኝዎታለን። ሁኔታውን በመለያዎ ማየት ይችላሉ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your application is still being reviewed by our Seller Operations team. We will contact you again by {{follow_up_time}} or as soon as there is a decision. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ማመልከቻዎ አሁንም በሻጭ ኦፕሬሽንስ ቡድናችን እየተገመገመ ነው። እስከ {{follow_up_time}} ድረስ ወይም ውሳኔ እንደተሰጠ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Seller application pending beyond the internal guideline set by your supervisor → **Seller Operations**.
- Application missing information and you cannot see what is missing → **Seller Operations**.
- Customer disputes a rejection → **Seller Operations** (via the seller verification process).
- Account held for security review → **Trust & Safety**.

## Resolution Procedure
1. Confirm the customer knows the current status and what (if anything) they need to do.
2. Record the status, submission date and escalation (if any).
3. Resolve once the customer has the information; Seller Operations communicates the final decision.

## Policy Pending Approval
- Confirm the target review time for seller applications and the approved customer wording.
- Confirm whether buyer accounts ever require approval.
- Define how and by whom applicants are told about missing documents and rejection reasons.

## Internal Notes
- Never say "you'll be approved soon" or "it's just a formality" — approval is not guaranteed.
- Repeated "when will I be approved?" contacts: link them to the same ticket instead of opening new ones.
- An applicant pushing to be approved urgently "because clients are waiting" is not a reason to skip verification.

<!-- doc -->
# Customer Has Duplicate Accounts
id: reg-duplicate-accounts
type: article
category: registration
subcategory: registration-security
audience: both
priority: medium
department: support_l2
features: accounts
tags: two accounts, duplicate account, merge accounts, second account, wrong account, bookings in other account, ሁለት መለያ, የተደጋገመ መለያ, መለያ ማዋሃድ
related: reg-email-already-used, acc-account-deletion-request, buy-purchase-history-missing, reg-seller-vs-buyer-account, reg-suspicious-registration
templates: tpl-verify-identity
policy_pending: yes

## Summary
The customer has more than one Byfluence account (e.g., one with email, one with phone) and their bookings, payments or seller application are split between them.

## Issue Description
Customers create a second account when they forget the first one, cannot verify, or think they need a separate seller account. They then cannot find bookings or purchase history, or their seller application is on a different account from their buyer history. They usually ask to "merge" the accounts.

## Possible Causes
- Registered once with email and once with phone number.
- Forgot the first account and registered again.
- Verification failed on the first attempt, so they registered again.
- Created a separate account to sell (see *Buyer or seller account*).
- Less commonly: intentional multiple accounts (to abuse offers, leave reviews, or evade a suspension/ban).

## Information to Collect
- The email(s) and phone number(s) for each account
- Which account they want to keep, and why
- Any bookings, payments or seller application linked to each account
- Identity confirmation for **every** account involved

> [!WARNING] Verify ownership of each account separately. Never ask for passwords or codes.

## Troubleshooting Steps
1. Verify the customer owns each account (contact from the registered email/phone, or details of a recent booking/transaction on that account). Follow the identity check in *Account recovery*.
2. In the admin dashboard, list for each account: status, verification, bookings (upcoming and past), transactions, seller status, balances.
3. Recommend which account to keep — usually the one with upcoming bookings, payment history or seller status.
4. **Merging** accounts is not a confirmed capability. Do not promise it. Escalate to **Senior Support** if the customer needs history moved.
5. For the unused account: if the customer wants it closed, follow *Account deletion / closure request* — only after checking there are no active bookings, pending payments, refunds or seller balances.
6. If the duplicate pattern suggests abuse (one account suspended/banned, many accounts, review manipulation) → **Trust & Safety**; do not discuss suspicions with the customer.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know you have more than one Byfluence account. To protect your information, I first need to confirm that both accounts belong to you. Please reply from (or tell us) the email address or phone number registered on each account, and share details of a recent booking or payment on each one, if any.

Once confirmed, I will check which account holds your bookings and payments and advise you which one to keep. Please never share your password or verification codes — we will not ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ከአንድ በላይ የByfluence መለያ እንዳለዎት ስላሳወቁን እናመሰግናለን። መረጃዎን ለመጠበቅ፣ በመጀመሪያ ሁለቱም መለያዎች የእርስዎ መሆናቸውን ማረጋገጥ ያስፈልገኛል። እባክዎ በእያንዳንዱ መለያ ላይ ከተመዘገበው ኢሜይል ወይም ስልክ ቁጥር ይጻፉልን (ወይም ይንገሩን)፤ እንዲሁም በእያንዳንዱ መለያ ላይ የቅርብ ጊዜ ቀጠሮ ወይም ክፍያ ካለ ዝርዝሩን ያጋሩን።

ከተረጋገጠ በኋላ ቀጠሮዎችዎ እና ክፍያዎችዎ በየትኛው መለያ ላይ እንዳሉ አጣርቼ የትኛውን መለያ መያዝ እንዳለብዎ እመክርዎታለሁ። እባክዎ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድዎን በፍጹም አያጋሩ — አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, to help with your two accounts I first need to confirm both are yours: send the registered email/phone of each and a recent booking/payment detail. Never share passwords or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በሁለቱ መለያዎችዎ ለመርዳት መጀመሪያ ሁለቱም የእርስዎ መሆናቸውን ማረጋገጥ አለብኝ፦ የእያንዳንዱን የተመዘገበ ኢሜይል/ስልክ እና የቅርብ ቀጠሮ/ክፍያ ዝርዝር ይላኩ። የይለፍ ቃል ወይም ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our team is still reviewing your accounts to confirm the best way forward. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ቡድናችን የተሻለውን መፍትሔ ለማረጋገጥ መለያዎችዎን አሁንም እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Customer needs bookings/history moved between accounts → **Senior Support / Supervisor**.
- Seller application or seller balance on the "wrong" account → **Seller Operations** (and **Payments & Finance** for balances).
- One of the accounts is suspended/banned, or many accounts are linked to the same person/device → **Trust & Safety**.

## Resolution Procedure
1. Confirm the customer knows which account to use and can log in to it.
2. Confirm any closure of the unused account went through the deletion process.
3. Record both account identifiers, what was found, and the decision in the ticket.

## Policy Pending Approval
- Decide whether one person may hold multiple accounts.
- Decide whether accounts can be merged, and who can do it.
- Define what happens to bookings/transactions on an account that is closed.

## Internal Notes
- Duplicate accounts are usually innocent. Stay neutral and helpful; escalate quietly if there are abuse signals.
- Do not delete or deactivate either account yourself.

<!-- doc -->
# Suspicious or Bulk Registration Attempts
id: reg-suspicious-registration
type: article
category: registration
subcategory: registration-security
audience: internal
priority: high
department: trust_safety
features: accounts, seller-onboarding
tags: fake accounts, bulk registration, spam accounts, suspicious signup, ban evasion, fraud registration, bot accounts, አጠራጣሪ ምዝገባ, ሐሰተኛ መለያ
related: reg-duplicate-accounts, reg-email-already-used, acc-banned-account, acc-security-concern-phishing, tns-account-compromise
templates: tpl-verify-identity
policy_pending: yes

## Summary
Internal guidance for spotting and reporting registrations that may be fake, automated, or used for fraud, ban evasion or manipulation.

## Overview
Agents see registration patterns through tickets and the admin dashboard. Early reporting protects buyers, honest sellers and payments. Agents **do not** investigate or take enforcement action themselves — they record signals and escalate to **Trust & Safety**.

## Issue Description
Typical situations:
- A wave of new accounts with similar names, sequential emails (`user101@`, `user102@`) or disposable email domains.
- A person whose account was suspended or banned contacts support from a new account.
- Several seller applications using the same identity documents, phone number or payout details.
- Many new accounts booking and cancelling, or leaving reviews for the same seller.
- A customer reports receiving verification codes for an account they never created.
- Someone asks support to "create accounts" for a group of people.

## Possible Causes
- Automated (bot) sign-ups.
- Ban or suspension evasion.
- Seller trying to inflate reviews or bookings.
- Identity theft — registering with someone else's details.
- Payment fraud testing (many small bookings with different cards/accounts).
- Innocent causes: a training class, a company onboarding staff, a family sharing a device.

## Information to Collect
- Account identifiers involved (emails/phones as shown in the admin dashboard)
- What pattern you noticed and when
- Related tickets, bookings, transactions or seller IDs
- Any statements the person made (copy them into internal notes)

> [!WARNING] Do not accuse the customer, reveal what triggered your concern, or tell them their account is "flagged". Never ask for passwords or codes.

## Troubleshooting Steps
1. Stay neutral with the customer. Handle only their stated request within normal rules.
2. Record the signals in the ticket's internal notes with account identifiers and timestamps.
3. Escalate to **Trust & Safety**, priority **High** (Critical if money is moving or a seller payout is involved).
4. Do not approve, verify, unlock, or change anything on accounts in the pattern until Trust & Safety responds.
5. If the person asks why their registration/account is limited, use the neutral response below.
6. If you see the pattern across many tickets, tell your supervisor immediately — it may be an attack.

- [ ] Signals recorded in internal notes
- [ ] Escalated to Trust & Safety
- [ ] No account changes made
- [ ] Supervisor informed if widespread

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. Your account is currently being reviewed by our team as part of our standard checks to keep the marketplace safe.

I have recorded your message under case number {{ticket_id}}. We will contact you if we need any further information. Thank you for your patience.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የገበያ ቦታውን ደህንነት ለመጠበቅ በምናደርገው መደበኛ ማጣራት መሰረት መለያዎ በአሁኑ ወቅት በቡድናችን እየተገመገመ ነው።

መልዕክትዎን በጉዳይ ቁጥር {{ticket_id}} መዝግቤዋለሁ። ተጨማሪ መረጃ ካስፈለገን እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your account is being reviewed as part of our standard safety checks. We've recorded your message and will contact you if we need anything. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ መለያዎ በመደበኛ የደህንነት ማጣራት እየተገመገመ ነው። መልዕክትዎን መዝግበናል፤ ተጨማሪ ነገር ካስፈለገ እናገኝዎታለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Any suspected fake, bulk or evasion registration → **Trust & Safety**, priority High.
- Money involved (payments, refunds, seller withdrawals) → **Trust & Safety** and notify **Payments & Finance**, priority Critical.
- Widespread pattern / possible attack → **Trust & Safety** + supervisor + **Technical / Engineering**.

## Resolution Procedure
1. The ticket is resolved by Trust & Safety's decision, not by the agent.
2. Agent confirms escalation is recorded and that the customer received a neutral response.

## Policy Pending Approval
- Define the official fraud signals list and thresholds for registrations.
- Decide what customers may be told when their account is under review, and who tells them.
- Decide the rule on multiple accounts per person and on new accounts by banned users.

## Internal Notes
- Shared devices are normal in Ethiopia (families, internet cafés, offices). One signal alone is not proof — record and escalate, don't conclude.
- Never search social media or contact third parties about a suspected registrant.
- Keep the response neutral even if the person becomes aggressive; hand over to a supervisor if needed.

<!-- doc -->
# Master Guide: Registration & Verification Problems
id: reg-tsg-registration-master
type: troubleshooting
category: registration
subcategory: registration-errors
audience: both
priority: medium
department: support_l1
features: accounts, notifications-email, notifications-sms
tags: registration problem, can't sign up, verification problem, master guide, sign up troubleshooting, registration flowchart, የምዝገባ ችግር, መመዝገብ አልቻልኩም
related: reg-registration-error-generic, reg-otp-not-received, reg-email-verification, reg-email-already-used, reg-account-not-activated, acc-tsg-login-master
templates: tpl-otp-not-received, tpl-request-screenshot, tpl-never-share-otp-warning
policy_pending: yes

## Summary
A diagnostic playbook for any "I can't register / can't verify my account" contact. Use it to find the right specific article quickly.

## Overview
Registration problems fall into five groups: the form itself, the email/phone details, verification messages, account state after sign-up, and security concerns. Work top to bottom; most cases are solved by step 2 or 3.

Before you start:
- Greet in Amharic (English if the customer prefers).
- Remind the customer never to share passwords or codes.
- Ask what they are trying to do (buy, book, sell) — sellers may actually be asking about application approval.

## Troubleshooting Steps
### Step 1 — Does an account already exist?
Search the admin dashboard by the email and phone the customer gives (try common typos).
- **No account** → go to Step 2.
- **Account exists, verified** → this is a login problem → *Master guide: login & account access problems*.
- **Account exists, not verified** → go to Step 3.
- **Account exists but customer says it isn't theirs** → *"Email or phone already registered" error*; consider **Trust & Safety**.
- **Two or more accounts** → *Customer has duplicate accounts*.

### Step 2 — What happens when they submit the form?
- "Invalid email" → *Email address rejected as invalid*.
- Phone rejected → *Phone number verification problems*.
- "Already registered" → *"Email or phone already registered" error*.
- Other field error, nothing happens, or "something went wrong" → *Registration form error or form won't submit*.
- They want Google/Facebook login, have no email, or a foreign number → *Unsupported registration methods*.

### Step 3 — Verification
- Email link missing/expired → *Email verification link not received or expired*.
- Code (OTP) not arriving → *OTP / verification code not received*.
- Code rejected → *Verification code rejected as invalid or expired*.

### Step 4 — Account state after sign-up
- Account says not activated → *Account created but not activated*.
- Seller waiting for approval → *Waiting for account approval*.
- Can't log in right after registering → *Cannot log in right after registering*.

### Step 5 — Security check (always)
- Codes the customer didn't request, an account they didn't create, or someone else "helping" them register → *Unauthorized access* / *Suspicious or bulk registration attempts* → **Trust & Safety**.
- Customer was asked by "Byfluence" to share a code → *Phishing messages or fake Byfluence contacts*.

### Step 6 — Incident check
If three or more similar reports arrive close together, check Announcements and tell your supervisor — it may be a platform-wide issue (email/SMS provider, sign-up page).

- [ ] Account existence checked
- [ ] Correct specific article followed
- [ ] Security check done
- [ ] Incident check done
- [ ] Ticket notes complete (cause + action)

## Escalation Conditions
- Technical failure confirmed (form, emails, SMS) → **Technical / Engineering**.
- Eligibility or policy questions → **Senior Support / Supervisor**.
- Seller application status → **Seller Operations**.
- Fraud, misuse of identity, ban evasion → **Trust & Safety**.

## Policy Pending Approval
- Confirm the live registration fields and verification methods so this guide can be made exact.
- Define the identity check required before any change to an unverified account.

## Internal Notes
- Always check the admin dashboard before telling a customer to "register again" — duplicates create more work later.
- Keep the customer informed at each step; long silences make customers retry and create duplicate tickets.
- Tag tickets consistently (e.g., "reg-otp", "reg-form-error") so trends are visible.
