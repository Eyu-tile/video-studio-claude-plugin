<!-- doc -->
# Forgotten Password
id: acc-forgot-password
type: article
category: account-access
subcategory: passwords
audience: both
priority: low
department: support_l1
features: accounts
tags: forgot password, reset password, change password, can't remember password, new password, የይለፍ ቃል ረሳሁ, የይለፍ ቃል መቀየር, ፓስዎርድ
related: acc-password-reset-link-issues, acc-incorrect-password, acc-account-recovery-lost-access, acc-tsg-login-master, acc-locked-account
templates: tpl-password-reset-guide, tpl-never-share-otp-warning
policy_pending: yes

## Summary
The customer has forgotten their password. They can reset it themselves from the login page using the email or phone number registered on their account.

## Overview
Password resets are self-service. Support staff **cannot see, send or set** a customer's password. The agent's job is to guide the customer through the reset and help if the reset message doesn't arrive.

If the customer **no longer has access** to the registered email and phone, a normal reset will not work — use *Account recovery when customer lost access to email/phone*.

## Customer Steps
1. Go to https://byfluence.com and open the login page.
2. Choose **"Forgot password?"** (the label may differ slightly).
3. Enter the email address or phone number registered on your account.
4. Open the reset link or enter the code sent to your email/phone. Use only the newest message.
5. Create a new password. Use one you haven't used before and don't use on other websites.
6. Log in with the new password. If your browser saved the old password, update or delete it.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. You can reset your password yourself in a few steps:

1. Go to https://byfluence.com and open the login page.
2. Choose "Forgot password?".
3. Enter the email address or phone number registered on your account.
4. Open the newest reset link or enter the newest code we send you.
5. Create a new password and log in.

For your security, please never share your password or reset codes with anyone — Byfluence staff will never ask for them.

If the reset message doesn't arrive, please reply and let me know. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የይለፍ ቃልዎን በጥቂት ደረጃዎች ራስዎ መቀየር ይችላሉ፦

1. https://byfluence.com ገብተው የመግቢያ ገጹን ይክፈቱ።
2. "Forgot password?" የሚለውን ይምረጡ።
3. በመለያዎ ላይ የተመዘገበውን ኢሜይል ወይም ስልክ ቁጥር ያስገቡ።
4. የምንልክልዎትን የቅርብ ጊዜ ሊንክ ይክፈቱ ወይም የቅርብ ጊዜውን ኮድ ያስገቡ።
5. አዲስ የይለፍ ቃል ፈጥረው ይግቡ።

ለደህንነትዎ ሲባል የይለፍ ቃልዎን ወይም የመቀየሪያ ኮድዎን ለማንም አያጋሩ — የByfluence ሠራተኞች በፍጹም አይጠይቁዎትም።

የመቀየሪያ መልዕክቱ ካልደረሰዎት እባክዎ መልሰው ያሳውቁኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! On the login page choose "Forgot password?", enter your registered email/phone, open the newest link or code and set a new password. Never share your password or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! በመግቢያ ገጹ "Forgot password?" ይምረጡ፣ የተመዘገበ ኢሜይል/ስልክዎን ያስገቡ፣ የቅርብ ጊዜውን ሊንክ ወይም ኮድ ተጠቅመው አዲስ የይለፍ ቃል ያዘጋጁ። የይለፍ ቃልዎን ወይም ኮድዎን አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Reset message never arrives after standard checks → *Password reset email/link not working*; then **Technical / Engineering**.
- Customer has lost access to both registered email and phone → *Account recovery* → **Senior Support / Supervisor**.
- Customer says their password was changed without their action → *Unauthorized access* → **Trust & Safety**, Critical.

## Policy Pending Approval
- Confirm the reset method(s) in production (email link, SMS code) and the password rules.
- Confirm whether resetting a password logs the account out on all other devices.

## Internal Notes
- Never offer to "reset it for them" or set a temporary password, even if an admin tool appears to allow it, unless your role is explicitly authorized.
- Low-literacy customers: walk them through on the phone, but let them type the new password themselves; tell them not to read it aloud.

<!-- doc -->
# Password Reset Email or Link Not Working
id: acc-password-reset-link-issues
type: article
category: account-access
subcategory: passwords
audience: both
priority: medium
department: support_l1
features: accounts, notifications-email, notifications-sms
tags: reset link not working, reset email not received, reset link expired, password reset error, no reset code, የመቀየሪያ ሊንክ አይሰራም, የይለፍ ቃል መቀየሪያ ኢሜይል አልደረሰም
related: acc-forgot-password, reg-otp-not-received, tec-email-notifications-not-received, tec-sms-not-received, acc-account-recovery-lost-access
templates: tpl-password-reset-guide, tpl-request-screenshot
policy_pending: yes

## Summary
The customer requested a password reset but the email/SMS doesn't arrive, or the link/code shows an error (expired, invalid, already used), or the new password is rejected.

## Issue Description
The customer is locked out and the self-service reset isn't working. They may have requested many resets. This often blocks someone with an upcoming booking, so respond promptly.

## Possible Causes
- The email/phone entered on the reset page is not the one registered (e.g., they registered with phone but are entering email).
- The message is in Spam/Promotions, or SMS is blocked/delayed.
- Several resets requested — only the newest link/code works.
- The link expired or was already used.
- The link opened in an in-app browser (Gmail app, Telegram) that broke it.
- The link was cut or wrapped by the email app.
- The new password does not meet the password rules, or matches the old one.
- Email/SMS delivery incident.

## Information to Collect
- The email/phone they entered on the reset page
- Whether they expect the message by email or SMS
- How many times they requested a reset
- Exact error message or screenshot (no codes visible)
- Device and browser

> [!WARNING] Never ask for the old or new password, or the reset code. Never send a reset link to an address other than the registered one.

## Troubleshooting Steps
1. Confirm the account exists for the email/phone they entered. If not, check other emails/phones they might have used.
2. **Message not arriving:** check Spam/Promotions; for SMS, check signal, SIM slot, blocked messages; wait a few minutes; request **one** new reset.
3. **Link error (expired/invalid/used):** request one new reset and open only the newest link, copying it into a normal browser (Chrome, Safari) if it fails inside an app.
4. **New password rejected:** read the error; explain the password rules; ask them to choose a password they haven't used before.
5. Check Announcements for email/SMS incidents.
6. Still failing → escalate to **Technical / Engineering** with the account identifier, request times, error screenshots and device/browser.
7. If the registered email/phone is no longer accessible → *Account recovery*.

- [ ] Correct registered email/phone used
- [ ] Spam / SMS checks done
- [ ] Newest link opened in normal browser
- [ ] Password rules explained

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry the password reset isn't working.

Please try this:
1. Make sure you enter the same email address or phone number you registered with.
2. Check your Spam/Promotions folder, or your SMS inbox and blocked messages.
3. Request just one new reset, then open only the newest link. If it doesn't open properly, copy it into your browser (Chrome, Safari, etc.).
4. When choosing your new password, use one you haven't used before and follow the rules shown on the page.

If it still doesn't work, please send me a screenshot of the error and tell me which email or phone number you are using. Please don't share any password or code.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ የይለፍ ቃል መቀየሪያው ስላልሰራ ይቅርታ እንጠይቃለን።

እባክዎ እንዲህ ይሞክሩ፦
1. የተመዘገቡበትን ተመሳሳይ ኢሜይል ወይም ስልክ ቁጥር ማስገባትዎን ያረጋግጡ።
2. የSpam/Promotions ፎልደርዎን፣ ወይም የኤስኤምኤስ ሳጥንዎን እና የታገዱ መልዕክቶችን ይመልከቱ።
3. አንድ አዲስ የመቀየሪያ ጥያቄ ብቻ ያቅርቡ፣ ከዚያም የቅርብ ጊዜውን ሊንክ ብቻ ይክፈቱ። በትክክል ካልተከፈተ ገልብጠው በብራውዘርዎ (Chrome፣ Safari ወዘተ) ይክፈቱት።
4. አዲስ የይለፍ ቃል ሲመርጡ ከዚህ በፊት ያልተጠቀሙበትን ይምረጡ እና በገጹ ላይ የሚታዩትን ደንቦች ይከተሉ።

አሁንም ካልሰራ፣ እባክዎ የስህተቱን ስክሪንሾት ይላኩልኝ እና የትኛውን ኢሜይል ወይም ስልክ ቁጥር እየተጠቀሙ እንደሆነ ይንገሩኝ። እባክዎ ምንም ዓይነት የይለፍ ቃል ወይም ኮድ አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, use the exact email/phone you registered with, check spam/SMS, request ONE new reset and open only the newest link in your browser. Still failing? Send a screenshot (no passwords/codes). Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የተመዘገቡበትን ኢሜይል/ስልክ ይጠቀሙ፣ ስፓም/ኤስኤምኤስ ይመልከቱ፣ አንድ አዲስ መቀየሪያ ጠይቀው የቅርብ ጊዜውን ሊንክ በብራውዘር ይክፈቱ። ካልሰራ ስክሪንሾት ይላኩ (የይለፍ ቃል/ኮድ አያጋሩ)። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our technical team is still checking why the account reset isn't working for you. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የይለፍ ቃል መቀየሪያው በመለያዎ ላይ ለምን እንደማይሰራ የቴክኒክ ቡድናችን አሁንም እያጣራ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Reset messages not delivered or links failing after all checks → **Technical / Engineering**.
- Many customers affected → **Technical / Engineering** incident; notify supervisor.
- Customer cannot access the registered email/phone → **Senior Support / Supervisor** via *Account recovery*.
- Customer receives reset messages they never requested → **Trust & Safety**.
- Customer has a session soon and is blocked → mark **High**, notify **Senior Support**.

## Resolution Procedure
1. Confirm the customer logged in with the new password.
2. Recommend they update any saved password in their browser.
3. Record the cause before resolving.

## Policy Pending Approval
- Confirm how long reset links/codes stay valid (approved customer wording).
- Confirm the password rules and whether old passwords can be reused.

## Internal Notes
- "I registered with my phone but I'm typing my email" is very common — always confirm which identifier the account uses.
- Unrequested reset emails can be a sign someone is targeting the account; ask the customer whether they requested them.

<!-- doc -->
# "Incorrect Password" When the Customer Is Sure It's Right
id: acc-incorrect-password
type: article
category: account-access
subcategory: passwords
audience: both
priority: medium
department: support_l1
features: accounts
tags: incorrect password, wrong password, password not working, password correct but error, can't log in password, የይለፍ ቃል ትክክል አይደለም, ፓስዎርድ አይሰራም
related: acc-forgot-password, acc-login-error-generic, acc-unauthorized-access, acc-locked-account, acc-tsg-login-master
templates: tpl-password-reset-guide, tpl-never-share-otp-warning
policy_pending: yes

## Summary
The login page says the password is incorrect, but the customer insists they are typing the right one.

## Issue Description
The customer is frustrated and sure the system is wrong. Repeated attempts may lock the account. Occasionally the password really was changed by someone else — always do a quick security check.

## Possible Causes
- Caps Lock on, or the phone auto-capitalised the first letter.
- The keyboard is set to Amharic (or another language), so letters/numbers typed differently.
- A space was added by autocomplete.
- The browser autofilled an old saved password.
- They are logging in with a different email/phone than the one the account uses, or into a different (duplicate) account.
- They recently reset the password on another device and forgot.
- Someone else changed the password (account compromise).
- Technical fault (rare, usually affects many users).

## Information to Collect
- The email/phone they are logging in with
- Whether they recently reset or changed the password
- Whether they received any unexpected emails/SMS from Byfluence (password changed, new login, codes)
- Device and browser; whether the browser filled the password automatically

> [!WARNING] Never ask the customer to tell you the password they are typing, not even "the first letters".

## Troubleshooting Steps
1. Confirm the account exists for the email/phone they are using.
2. Ask them to:
   - Turn off Caps Lock and switch the keyboard to English.
   - Delete the autofilled password and type it manually; check for spaces.
   - Use the "show password" eye icon (if available) to see what they typed — privately, not to you.
3. Ask whether they have another Byfluence account (different email/phone).
4. If it still fails → *Forgotten password* (self-service reset). This is usually fastest.
5. **Security check:** if they received "password changed" or unknown login/code messages, or the reset email/phone on the account isn't theirs anymore → *Unauthorized access*, escalate to **Trust & Safety**.
6. If the account is locked after attempts → *Locked account*.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand how frustrating this is. A few small things often cause this error:

1. Make sure Caps Lock is off and your keyboard is set to English.
2. Delete any password your browser filled in automatically, and type it yourself without spaces.
3. Check that you are using the same email or phone number you registered with.

If it still doesn't work, the quickest solution is to reset your password using "Forgot password?" on the login page.

Also, if you received any message about a password change or a login you don't recognise, please tell me right away. Never share your password or codes with anyone, including us.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ይህ ምን ያህል እንደሚያበሳጭ ይገባኛል። ይህን ስህተት ብዙ ጊዜ የሚያመጡት ትናንሽ ነገሮች ናቸው፦

1. Caps Lock መጥፋቱን እና ኪቦርድዎ በእንግሊዝኛ መሆኑን ያረጋግጡ።
2. ብራውዘርዎ በራሱ የሞላውን የይለፍ ቃል አጥፍተው ያለ ክፍተት ራስዎ ይጻፉት።
3. የተመዘገቡበትን ተመሳሳይ ኢሜይል ወይም ስልክ ቁጥር እየተጠቀሙ መሆኑን ያረጋግጡ።

አሁንም ካልሰራ፣ ፈጣኑ መፍትሔ በመግቢያ ገጹ ላይ ያለውን "Forgot password?" ተጠቅመው የይለፍ ቃልዎን መቀየር ነው።

እንዲሁም ስለ የይለፍ ቃል መቀየር ወይም የማያውቁት መግቢያ የሚገልጽ መልዕክት ደርሶዎት ከሆነ እባክዎ ወዲያውኑ ይንገሩኝ። የይለፍ ቃልዎን ወይም ኮድዎን ለማንም አያጋሩ፤ ለእኛም ጭምር።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, check Caps Lock, switch to the English keyboard, delete any autofilled password and type it yourself. Still failing? Use "Forgot password?". Got an unexpected "password changed" message? Tell me now. Never share codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ Caps Lockን ያረጋግጡ፣ ወደ እንግሊዝኛ ኪቦርድ ይቀይሩ፣ በራሱ የተሞላውን የይለፍ ቃል አጥፍተው ራስዎ ይጻፉ። ካልሰራ "Forgot password?" ይጠቀሙ። ያልጠበቁት የ"password changed" መልዕክት ደርሶዎታል? አሁኑኑ ይንገሩኝ። ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Signs the password was changed by someone else → **Trust & Safety**, Critical (see *Unauthorized access*).
- Correct password rejected for many users → **Technical / Engineering** incident.
- Account locked and doesn't unlock → *Locked account*.

## Resolution Procedure
1. Confirm the customer logged in (after typing fix or reset).
2. Confirm the security check was done and recorded.
3. Record the cause (keyboard, autofill, wrong identifier, reset, compromise) before resolving.

## Policy Pending Approval
- Confirm how many failed attempts trigger a lock and what the customer sees.

## Internal Notes
- The Amharic keyboard issue is common on Android phones with multiple input languages.
- Suggest a password reset early — it is quicker than trying many times and risking a lock.

<!-- doc -->
# Login Errors and Error Messages
id: acc-login-error-generic
type: article
category: account-access
subcategory: login-errors
audience: both
priority: medium
department: support_l1
features: accounts
tags: login error, can't log in, error message, login failed, something went wrong login, account disabled, login page not loading, መግባት አልቻልኩም, የመግቢያ ስህተት, ስህተት መልዕክት
related: acc-incorrect-password, acc-locked-account, acc-suspended-account, acc-cannot-login-after-registration, tec-clear-cache-cookies, acc-tsg-login-master
templates: tpl-request-screenshot, tpl-password-reset-guide
policy_pending: yes

## Summary
The customer cannot log in and sees an error message (or nothing happens). This article maps common error types to their meaning and next step.

## Issue Description
Login errors range from simple typing mistakes to account restrictions and platform incidents. The exact wording on Byfluence is not confirmed in this knowledge base, so always ask for a screenshot and match it to the closest category below.

| What the customer sees (approximate) | Likely meaning | Go to |
|---|---|---|
| Incorrect email/phone or password | Credentials don't match | *"Incorrect password" when customer is sure it's right* |
| Account not verified / not activated | Verification incomplete | *Account created but not activated* |
| Too many attempts / account locked | Temporary lock | *Locked account (too many attempts)* |
| Account suspended / disabled | Restriction on the account | *Suspended account enquiry* |
| Account banned / closed | Permanent restriction or closure | *Banned account enquiry and appeal* |
| Something went wrong / server error / page keeps loading | Technical issue | Steps below; possible incident |
| Logged in, then immediately logged out | Session/cookie issue | *Customer keeps getting logged out* |
| No account found | Wrong identifier or no account | *Cannot log in right after registering* |

## Possible Causes
- Wrong credentials (most common).
- Account state: unverified, locked, suspended, banned, closed.
- Browser issues: old cache/cookies, auto-translate, data-saver mode, outdated browser.
- Poor connection or VPN.
- Platform outage or a bug after a release.

## Information to Collect
- Screenshot of the error (password field hidden)
- Email/phone used to log in
- Device, browser, and connection (mobile data / Wi-Fi)
- When it started; whether it worked before

> [!WARNING] Never ask for the password or any code. A screenshot and the login email/phone are enough.

## Troubleshooting Steps
1. Get the screenshot and match the message to the table above.
2. Check the account in the admin dashboard: exists? verified? locked/suspended/banned?
3. If the account state explains the error, move to the matching article.
4. If the account looks normal:
   - Try a private/incognito window or another browser.
   - Clear cache and cookies (tec-clear-cache-cookies).
   - Turn off auto-translate, data-saver and VPN.
   - Switch between mobile data and Wi-Fi.
5. Check Announcements for incidents. If several customers report login failures, notify your supervisor.
6. Still failing with a normal account → escalate to **Technical / Engineering** with screenshot, account identifier, device/browser and time.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry you're having trouble logging in.

So I can see exactly what's happening, please send me:
1. A screenshot of the error message (please hide the password box)
2. The email address or phone number you use to log in
3. The device and browser you are using

Meanwhile, you can try logging in from a private/incognito window or a different browser. Please don't share your password or any verification codes — we will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ ለመግባት ስለተቸገሩ ይቅርታ እንጠይቃለን።

ምን እየተፈጠረ እንደሆነ በትክክል ለማየት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የስህተት መልዕክቱን ስክሪንሾት (እባክዎ የይለፍ ቃል ሳጥኑን ይደብቁ)
2. ለመግባት የሚጠቀሙበትን ኢሜይል ወይም ስልክ ቁጥር
3. የሚጠቀሙትን መሳሪያ (ስልክ/ኮምፒውተር) እና ብራውዘር

እስከዚያው በprivate/incognito መስኮት ወይም በሌላ ብራውዘር ለመግባት መሞከር ይችላሉ። እባክዎ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about this! Please send a screenshot of the error (password hidden), your login email/phone, and your device/browser. Meanwhile try an incognito window. Never share passwords or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! እባክዎ የስህተቱን ስክሪንሾት (የይለፍ ቃል ተደብቆ)፣ የመግቢያ ኢሜይል/ስልክዎን እና መሳሪያ/ብራውዘርዎን ይላኩ። እስከዚያው incognito ይሞክሩ። የይለፍ ቃል ወይም ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our technical team is still looking into the login error on your account. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። በመለያዎ ላይ ያለውን የመግቢያ ስህተት የቴክኒክ ቡድናችን አሁንም እያጣራ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Normal account, error persists on standard browsers → **Technical / Engineering**.
- Several customers report login failures → **Technical / Engineering** incident; notify supervisor.
- Account restricted (suspended/banned) → follow the specific article; **Trust & Safety** or **Seller Operations**.
- Signs of compromise → **Trust & Safety**, Critical.

## Resolution Procedure
1. Confirm the customer can log in, or that they understand the account restriction and the next step.
2. Record the error message, cause and fix in the ticket.

## Policy Pending Approval
- Collect the exact login error messages (EN and AM) from the live site so this table can be made exact.
- Decide what wording agents may use to explain each account state.

## Internal Notes
- Always identify the account state in the admin dashboard before troubleshooting the browser — it saves time.
- Do not tell a customer their account is suspended or banned until you have confirmed it in the admin dashboard.

<!-- doc -->
# Cannot Log In Right After Registering
id: acc-cannot-login-after-registration
type: article
category: account-access
subcategory: login-errors
audience: both
priority: medium
department: support_l1
features: accounts
tags: just registered can't login, new account login problem, signed up but can't log in, account not found after sign up, ተመዝግቤ መግባት አልቻልኩም, አዲስ መለያ
related: reg-account-not-activated, reg-email-verification, reg-otp-not-received, acc-incorrect-password, reg-duplicate-accounts, acc-tsg-login-master
templates: tpl-otp-not-received, tpl-password-reset-guide
policy_pending: yes

## Summary
The customer has just signed up but cannot log in — they get "account not found", "not verified", or "incorrect password".

## Issue Description
New customers often assume registration finished when it didn't, or they log in with a different identifier than they registered with. Getting them in quickly matters: a bad first experience often ends with them leaving the platform.

## Possible Causes
- Registration did not complete (an error on the last step, connection dropped).
- Verification (email link / SMS code) not completed.
- Email or phone mistyped at registration — the account exists under the typo.
- Logging in with phone when they registered with email (or the reverse).
- Browser saved a different password, or the customer mistyped the password when creating it.
- The account is held for review.

## Information to Collect
- Email and phone they registered with (and any variations)
- What message they see when logging in (screenshot)
- Whether they received any verification email/SMS
- Approximate time of registration

> [!WARNING] Never ask for the password or verification codes.

## Troubleshooting Steps
1. Search the admin dashboard by email, phone and likely typos.
2. Decide the case:
   - **No account** → registration didn't complete. Ask them to register again carefully (*Registration form error* if it fails again).
   - **Account under a typo** → do not edit it yourself; escalate to **Senior Support** (or have the customer re-register with the correct details if that's the approved approach).
   - **Account not verified** → complete verification (*Email verification* / *OTP not received*).
   - **Account verified, "incorrect password"** → the password may have been mistyped at creation → *Forgotten password*.
   - **Account held for review** → **Trust & Safety**; neutral response.
3. Check for duplicates created during retries.

## Recommended Response (EN)
Hello {{customer_name}},

Welcome to Byfluence, and I'm sorry you can't log in yet. Let's sort it out:

1. Please check your email (including Spam) or SMS for a verification message from Byfluence, and complete it if you haven't.
2. Make sure you log in with the same email or phone number you used to register.
3. If it says the password is incorrect, use "Forgot password?" on the login page to set a new one.

If none of this works, reply with the email/phone you registered with and a screenshot of the message you see, and I'll check your account. Please never share your password or codes.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ወደ Byfluence እንኳን በደህና መጡ፤ ገና መግባት ባለመቻልዎ ይቅርታ እንጠይቃለን። አብረን እናስተካክለው፦

1. እባክዎ ኢሜይልዎን (Spamን ጨምሮ) ወይም ኤስኤምኤስዎን ከByfluence የመጣ የማረጋገጫ መልዕክት ካለ ይመልከቱ፤ ካላጠናቀቁት ያጠናቅቁት።
2. ለመመዝገብ በተጠቀሙበት ተመሳሳይ ኢሜይል ወይም ስልክ ቁጥር መግባትዎን ያረጋግጡ።
3. የይለፍ ቃሉ ትክክል አይደለም ካለ፣ በመግቢያ ገጹ ላይ "Forgot password?" ተጠቅመው አዲስ ያዘጋጁ።

ከእነዚህ አንዱም ካልሰራ፣ የተመዘገቡበትን ኢሜይል/ስልክ እና የሚያዩትን መልዕክት ስክሪንሾት ይላኩልኝ፤ መለያዎን አጣራለሁ። እባክዎ የይለፍ ቃልዎን ወይም ኮድዎን በፍጹም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please complete the verification email/SMS, log in with the same email/phone you registered with, or use "Forgot password?". Still stuck? Send your registered email/phone + screenshot. Never share codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ የማረጋገጫ ኢሜይል/ኤስኤምኤሱን ያጠናቅቁ፣ በተመዘገቡበት ኢሜይል/ስልክ ይግቡ፣ ወይም "Forgot password?" ይጠቀሙ። ካልሰራ የተመዘገቡበትን ኢሜይል/ስልክ እና ስክሪንሾት ይላኩ። ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Account exists under a typo → **Senior Support / Supervisor**.
- Verified account, reset works, still can't log in → **Technical / Engineering**.
- Account held for review → **Trust & Safety**.

## Resolution Procedure
1. Confirm the customer is logged in and can see their dashboard.
2. Check and note any duplicate accounts created.
3. Record the cause before resolving.

## Policy Pending Approval
- Decide whether support may correct a mistyped email/phone on a new, unverified account, and the identity check required.

## Internal Notes
- This is a first impression moment — be extra patient and stay with the customer until they're in.
- Ask "did you see a success message after registering?" — it quickly tells you whether registration completed.

<!-- doc -->
# Customer Keeps Getting Logged Out
id: acc-logged-out-repeatedly
type: article
category: account-access
subcategory: login-errors
audience: both
priority: medium
department: technical
features: accounts
tags: keeps logging out, session expired, logged out automatically, have to log in again, signed out, session timeout, በተደጋጋሚ ከመለያዬ ያስወጣኛል, ሎግ አውት
related: tec-clear-cache-cookies, acc-unauthorized-access, acc-login-error-generic, acc-tsg-login-master, acc-incorrect-password
templates: tpl-request-screenshot
policy_pending: yes

## Summary
The customer can log in but is repeatedly logged out — after a short time, when changing pages, or every time they reopen the browser.

## Issue Description
Being logged out repeatedly interrupts bookings and payments and can make customers suspect a security problem. Most cases are browser settings; occasionally it means the password was changed elsewhere or the account was acted on by staff.

## Possible Causes
- Browser blocks or deletes cookies (privacy settings, "clear on exit", incognito/private mode).
- Data-saver or "lite" browsers, or in-app browsers (Telegram, Facebook) not keeping the session.
- Corrupted cache/cookies after a site update.
- Several tabs or devices logging in and out.
- Device date/time set incorrectly.
- VPN or unstable connection changing network often.
- The password was changed (by the customer on another device, or by someone else), ending sessions.
- Normal session expiry after inactivity (duration not confirmed).
- A bug after a release (several customers affected).

## Information to Collect
- When it happens (after a few minutes, on page change, on reopening the browser, during payment)
- Device, browser and whether they use private/incognito or an in-app browser
- Whether they use a VPN
- Whether they changed their password recently, or received unexpected security messages

## Troubleshooting Steps
1. Ask the security questions first: unexpected "password changed"/login/code messages? If yes → *Unauthorized access*.
2. Ask them to use a normal (not private) window in a standard browser — not inside Telegram or Facebook.
3. Clear cookies and cache for byfluence.com (tec-clear-cache-cookies), then log in again.
4. Make sure cookies are allowed for the site and "clear cookies on exit" is off.
5. Check the device date and time are set automatically.
6. Turn off VPN / data-saver mode.
7. If the problem continues on a standard browser with cookies allowed → escalate to **Technical / Engineering** with device, browser, timestamps and what they were doing.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry you keep being logged out.

Please try these steps:
1. Open Byfluence in a normal browser window (Chrome, Safari, etc.), not in a private/incognito window and not inside another app like Telegram.
2. Clear your browser's cookies and cache for byfluence.com, then log in again.
3. Make sure your phone's date and time are set automatically, and turn off any VPN or data-saver mode.

Also, if you have received any message about a password change or a login you don't recognise, please tell me right away. Never share your password or codes with anyone.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ በተደጋጋሚ ከመለያዎ እየወጡ ስለሆነ ይቅርታ እንጠይቃለን።

እባክዎ እነዚህን ደረጃዎች ይሞክሩ፦
1. Byfluenceን በመደበኛ የብራውዘር መስኮት (Chrome፣ Safari ወዘተ) ይክፈቱ፤ በprivate/incognito መስኮት ወይም እንደ Telegram ባሉ ሌሎች መተግበሪያዎች ውስጥ አይክፈቱት።
2. ለbyfluence.com የብራውዘርዎን cookies እና cache አጽድተው እንደገና ይግቡ።
3. የስልክዎ ቀን እና ሰዓት በራሱ (automatic) መሆኑን ያረጋግጡ፤ VPN ወይም data-saver ካለ ያጥፉት።

እንዲሁም ስለ የይለፍ ቃል መቀየር ወይም የማያውቁት መግቢያ የሚገልጽ መልዕክት ደርሶዎት ከሆነ እባክዎ ወዲያውኑ ይንገሩኝ። የይለፍ ቃልዎን ወይም ኮድዎን ለማንም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please use a normal browser window (not incognito or inside Telegram), clear cookies for byfluence.com, set your phone's time to automatic, and turn off VPN. Any unexpected security messages? Tell me now. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ መደበኛ የብራውዘር መስኮት ይጠቀሙ (incognito ወይም Telegram ውስጥ አይደለም)፣ የbyfluence.com cookiesን ያጽዱ፣ የስልክ ሰዓትን automatic ያድርጉ፣ VPN ያጥፉ። ያልጠበቁት የደህንነት መልዕክት ደርሶዎታል? አሁኑኑ ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our technical team is still investigating why you are being logged out. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለምን ከመለያዎ እንደሚወጡ የቴክኒክ ቡድናችን አሁንም እያጣራ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Persists on a standard browser with cookies allowed → **Technical / Engineering**.
- Many customers affected after a release → **Technical / Engineering** incident.
- Unexpected security messages or password changes → **Trust & Safety**, Critical.
- Logged out during payment and unsure if payment went through → check the transaction; involve **Payments & Finance** if needed.

## Resolution Procedure
1. Confirm the customer stays logged in through a normal session (e.g., can complete a booking flow).
2. Record the cause (cookies, in-app browser, VPN, compromise, bug) before resolving.

## Policy Pending Approval
- Confirm the session duration / inactivity timeout so agents can explain expected behaviour.
- Confirm whether changing the password logs out all devices.

## Internal Notes
- Telegram's in-app browser is a very common cause for customers who click links sent in Telegram chats.
- If the customer was logged out in the middle of paying, always check for a pending/successful transaction before they pay again.

<!-- doc -->
# Master Guide: Login & Account Access Problems
id: acc-tsg-login-master
type: troubleshooting
category: account-access
subcategory: login-errors
audience: both
priority: medium
department: support_l1
features: accounts
tags: login problem, can't access account, account access master guide, login troubleshooting, locked out, መግባት አልቻልኩም, መለያዬን ማግኘት አልቻልኩም
related: acc-login-error-generic, acc-forgot-password, acc-locked-account, acc-account-recovery-lost-access, acc-unauthorized-access, reg-tsg-registration-master
templates: tpl-password-reset-guide, tpl-account-locked, tpl-account-compromise-urgent, tpl-request-screenshot
policy_pending: yes

## Summary
A diagnostic playbook for any "I can't get into my account" contact, starting with the security check and ending with the specific article to follow.

## Overview
Access problems fall into four groups: **security** (someone else may be in the account), **account state** (unverified, locked, suspended, banned), **credentials** (password, wrong identifier, lost email/phone), and **technical** (browser, sessions, outages). Always rule out security first — a compromised account is time-critical, especially for sellers with earnings.

Golden rules:
- Never ask for passwords, OTP codes or PINs.
- Never change account details (email, phone, password) yourself unless your role is authorized.
- Verify identity before discussing account details.

## Troubleshooting Steps
### Step 1 — Security check (always first)
Ask: "Have you received any messages about a password change, a new login, or codes you didn't request? Has anyone else had access to your phone or email? Have you shared a code with anyone?"
- **Yes to any** → *Unauthorized access* — **Trust & Safety**, priority **Critical**.
- **Customer received a suspicious message claiming to be Byfluence** → *Phishing messages or fake Byfluence contacts*.
- **No** → Step 2.

### Step 2 — Find the account and its state
Search the admin dashboard by email/phone (and typos).
- **No account** → *Cannot log in right after registering* / registration master guide.
- **Not verified** → *Account created but not activated*.
- **Locked** → *Locked account (too many attempts)*.
- **Suspended** → *Suspended account enquiry*.
- **Banned / closed** → *Banned account enquiry and appeal*.
- **Active** → Step 3.

### Step 3 — Credentials
- Forgot password → *Forgotten password*.
- Sure the password is right → *"Incorrect password" when customer is sure it's right*.
- Reset email/SMS not working → *Password reset email/link not working*.
- No longer has the registered email or phone → *Account recovery when customer lost access to email/phone*.

### Step 4 — Technical
- Error message or page won't load → *Login errors and error messages*.
- Logged in but keeps getting logged out → *Customer keeps getting logged out*.
- Several customers at once → incident: check Announcements, notify supervisor, escalate to **Technical / Engineering**.

### Step 5 — Urgency check
If the customer has a consultation starting soon, or is a seller with a pending withdrawal, raise the priority (**High**) and tell Senior Support.

- [ ] Security check asked and recorded
- [ ] Account state confirmed in admin dashboard
- [ ] Specific article followed
- [ ] Urgency assessed
- [ ] Ticket notes complete

## Escalation Conditions
- Compromise suspected → **Trust & Safety**, Critical.
- Account restrictions (suspended/banned) → **Trust & Safety** (buyers) or **Seller Operations** (sellers).
- Recovery without access to email/phone → **Senior Support / Supervisor**.
- Technical failures → **Technical / Engineering**.

## Policy Pending Approval
- Approve the official identity verification procedure for account access cases.
- Confirm lock thresholds/durations, session timeouts and the wording for each account state.

## Internal Notes
- Customers often describe a suspension as "my account is broken". Always check the account state before troubleshooting the browser.
- Keep one ticket per customer issue — link repeat contacts to the existing ticket.
