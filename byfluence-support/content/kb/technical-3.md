<!-- doc -->
# Email Notifications Not Received
id: tec-email-notifications-not-received
type: article
category: technical
subcategory: notifications
audience: both
priority: medium
department: technical
features: notifications-email
tags: no email, didn't receive email, confirmation email missing, verification email not received, email in spam, booking email not received, ኢሜይል አልደረሰኝም, የማረጋገጫ ኢሜይል, ኢሜይል አልመጣም
related: tec-sms-not-received, tec-dashboard-loading-error, tec-reporting-a-bug, reg-how-to-create-account, con-how-consultations-work
templates: tpl-technical-investigation, tpl-request-screenshot
policy_pending: yes

## Summary
The customer expected an email from Byfluence (account verification, booking confirmation, meeting details, password reset, seller updates) but it did not arrive.

## Issue Description
Customers rely on emails to confirm actions, especially booking confirmations and meeting details. Missing emails cause worry ("did my booking go through?") and can block account setup. Which events send an email is **not yet confirmed** (see Feature Status for *Email notifications*), so first confirm that the event actually sends an email before investigating.

## Possible Causes
- The event does not send an email (feature not enabled for that event).
- Email is in **Spam/Junk**, or Gmail's **Promotions/Updates** tab.
- **Typo in the registered email** (e.g., "gmial.com", missing letter), or the customer registered with another email or with phone only.
- The customer is checking a different inbox from the one registered.
- Inbox full, or the email provider is delaying/blocking messages.
- The customer requested several emails quickly; only the latest link/code is valid.
- Email delivery problem on our side (email provider issue, bug).

## Information to Collect
- The email address they are checking (spelled out)
- What email they expected and what action triggered it (booking, registration, password reset…)
- When they did the action (date/time)
- Whether they checked Spam/Junk and Promotions/Updates
- Email provider (Gmail, Yahoo, Outlook, company email)

> [!WARNING] Never ask the customer to forward a password-reset link or a verification code to support, and never ask for their email password.

## Troubleshooting Steps
1. Confirm via Feature Status / approved process that this event sends an email. If it doesn't, explain where to find the information instead (e.g., dashboard → bookings).
2. Compare the email they gave you with the **registered email** in authorized tools. If there's a typo, follow the approved account-change process (identity verification first).
3. Ask them to check **Spam/Junk** and **Promotions/Updates**, and search the inbox for "Byfluence".
4. If found in spam, ask them to mark it "Not spam" so future emails arrive in the inbox.
5. If they requested several times, ask them to use only the **latest** email.
6. If the information exists in the dashboard (e.g., confirmed booking, meeting details), point them there so they are not blocked.
7. If you have access to email delivery logs, check delivery status. Otherwise, and if several customers report missing emails, escalate to Technical.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry you haven't received our email.

Please check the following:
1. Your Spam or Junk folder, and the "Promotions" or "Updates" tab if you use Gmail
2. Search your inbox for "Byfluence"
3. Make sure you are checking the same email address you registered with

If you find our email in spam, please mark it as "Not spam" so future emails reach your inbox.

You can also find your booking details in your Byfluence dashboard. If you still can't find the email, reply here with the email address you registered with and what the email was about. Your case number is {{ticket_id}}.

Please never share your password or any verification code with anyone.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ኢሜይላችን ስላልደረሰዎት ይቅርታ እንጠይቃለን።

እባክዎ የሚከተሉትን ይመልከቱ፦
1. የSpam ወይም Junk ፎልደርዎን፣ Gmail የሚጠቀሙ ከሆነ ደግሞ "Promotions" ወይም "Updates" የሚለውን ክፍል
2. በኢሜይል ሳጥንዎ ውስጥ "Byfluence" ብለው ይፈልጉ
3. የተመዘገቡበትን ተመሳሳይ ኢሜይል አድራሻ እየተመለከቱ መሆኑን ያረጋግጡ

ኢሜይላችንን በSpam ውስጥ ካገኙት፣ ወደፊት የሚላኩት ኢሜይሎች በቀጥታ እንዲደርስዎት "Not spam" የሚለውን ይጫኑ።

የቀጠሮዎን ዝርዝር በByfluence ዳሽቦርድዎ ውስጥም ማግኘት ይችላሉ። አሁንም ኢሜይሉን ካላገኙት የተመዘገቡበትን ኢሜይል አድራሻ እና ኢሜይሉ ስለ ምን እንደነበር እዚሁ ይጻፉልኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

እባክዎ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ ለማንም አያጋሩ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please check Spam/Junk and Gmail's Promotions/Updates tab, and search for "Byfluence". Make sure it's the email you registered with. Booking details are also in your dashboard. Still nothing? Reply with your registered email. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ Spam/Junk እና በGmail ውስጥ Promotions/Updates የሚለውን ይመልከቱ፤ "Byfluence" ብለውም ይፈልጉ። የተመዘገቡበት ኢሜይል መሆኑን ያረጋግጡ። የቀጠሮ ዝርዝሩ በዳሽቦርድዎም አለ። ካላገኙት የተመዘገቡበትን ኢሜይል ይላኩልኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is checking why our emails are not reaching you. Meanwhile, your booking and account information is available in your Byfluence dashboard. We will update you by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ ኢሜይሎቻችን ለምን እንደማይደርስዎት የቴክኒክ ቡድናችን እያጣራ ነው። እስከዚያው የቀጠሮዎ እና የአካውንትዎ መረጃ በByfluence ዳሽቦርድዎ ውስጥ ይገኛል። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

## Escalation Conditions
- Several customers report missing emails, or delivery logs show failures → **Technical / Engineering**, High.
- A single customer with correct email and nothing in spam after checks → **Technical / Engineering**, Medium.
- The customer received an email claiming to be Byfluence asking for passwords, codes or payment → **Trust & Safety** (acc-security-concern-phishing).
- A registered email must be corrected → follow the account-change process; **Senior Support / Supervisor** if identity can't be verified.

## Resolution Procedure
1. Confirm the customer has received the email (or has the needed information from the dashboard).
2. Record the cause (spam, typo, wrong inbox, not an email event, delivery failure).

## Policy Pending Approval
- Confirm which events send email notifications (registration, booking confirmation, meeting link, reminders, payments, withdrawals, seller verification).
- Confirm the official sender address(es) so agents can tell customers how to recognise genuine Byfluence emails.
- Confirm whether agents may manually resend emails and through which tool.

## Internal Notes
- Ask customers to spell their email letter by letter — typos are very common.
- Never change an email address on request without identity verification; email change is a common account-takeover tactic.
- The dashboard is the source of truth for bookings; an email is only a notification.

<!-- doc -->
# SMS Messages Not Received
id: tec-sms-not-received
type: article
category: technical
subcategory: notifications
audience: both
priority: medium
department: technical
features: notifications-sms
tags: no sms, didn't get code, verification code not received, otp not received, sms not coming, text message missing, ኤስኤምኤስ አልደረሰኝም, ኮድ አልመጣም, የማረጋገጫ ኮድ
related: tec-email-notifications-not-received, reg-how-to-create-account, tec-poor-connectivity, acc-security-concern-phishing, tec-unexpected-error-message
templates: tpl-technical-investigation
policy_pending: yes

## Summary
The customer is not receiving SMS messages from Byfluence, such as a verification code or a booking notification.

## Issue Description
SMS may be used for verification codes or notifications (which events send SMS, and whether phone OTP is used, is **not yet confirmed** — check Feature Status for *SMS notifications*). Missing SMS can block registration or login. Agents must help without ever asking for the code itself.

## Possible Causes
- The event does not send SMS (feature not enabled for that event).
- **Wrong phone number** registered (typo, missing digit, wrong country code, an old number).
- No network signal, phone in airplane mode, or the SIM with that number is not in the phone (dual-SIM phones).
- **Inbox full** on older phones, or SMS blocked by a spam filter or a "block promotional messages" setting.
- The customer requested many codes in a short time — sending is temporarily limited, or only the newest code works.
- Operator delays or SMS provider problems; platform-side bug.

## Information to Collect
- The phone number they expect SMS on (ask them to type it fully)
- Which mobile operator
- What SMS they expected (verification code, booking notice) and when they requested it
- Whether they receive SMS from others right now
- Whether the phone has two SIMs and which one has that number

> [!WARNING] Never ask the customer to read out or send you the verification code/OTP, even when they finally receive it. The code is for them to type on byfluence.com only. Anyone asking for it is a scammer.

## Troubleshooting Steps
1. Confirm via Feature Status / approved process that this event sends SMS.
2. Compare the number with the **registered phone number** in authorized tools (format, digits, country code). If wrong → approved account-change process with identity verification.
3. Ask the customer to check: signal, airplane mode off, the correct SIM is active, and they can receive SMS from someone else.
4. Ask them to check the SMS inbox is not full (delete old messages) and any blocked/spam SMS folder.
5. Ask them to **stop requesting new codes**, wait a while, then request **once** and use only the newest code.
6. Restart the phone (refreshes the network connection).
7. If email is also available for that action, suggest using it.
8. If several customers (often on the same operator) report the same, or the number is correct and all checks pass → escalate to Technical with the number (internal ticket only), operator and request times.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry you haven't received our SMS.

Please check:
1. Your phone has network signal and airplane mode is off
2. The SIM card with your registered number is active (if your phone has two SIMs)
3. Your SMS inbox is not full — delete some old messages
4. Restart your phone, then request the message only once and wait a little

If you requested several codes, please use only the newest one.

Important: never share a verification code with anyone — not even with Byfluence Support. Type it only on byfluence.com.

If you still don't receive it, please confirm the phone number you registered with and your mobile operator. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የእኛ ኤስኤምኤስ ስላልደረሰዎት ይቅርታ እንጠይቃለን።

እባክዎ የሚከተሉትን ያረጋግጡ፦
1. ስልክዎ ኔትወርክ እንዳለው እና airplane mode እንደጠፋ
2. የተመዘገቡበት ቁጥር ያለበት ሲም ካርድ እየሰራ መሆኑን (ስልክዎ ሁለት ሲም ካለው)
3. የኤስኤምኤስ ሳጥንዎ እንዳልሞላ — አንዳንድ የቆዩ መልዕክቶችን ይሰርዙ
4. ስልክዎን አጥፍተው ያብሩ፤ ከዚያ መልዕክቱን አንድ ጊዜ ብቻ ጠይቀው ትንሽ ይጠብቁ

ብዙ ኮዶችን ጠይቀው ከነበረ፣ እባክዎ የመጨረሻውን (አዲሱን) ኮድ ብቻ ይጠቀሙ።

ማሳሰቢያ፦ የማረጋገጫ ኮድን ለማንም አያጋሩ — ለByfluence ድጋፍ ሰጪዎችም ጭምር። ኮዱን በbyfluence.com ላይ ብቻ ያስገቡ።

አሁንም ካልደረሰዎት እባክዎ የተመዘገቡበትን ስልክ ቁጥር እና የሞባይል ኦፕሬተርዎን ይንገሩኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please check your signal, that the right SIM is active and your SMS inbox isn't full. Restart your phone and request the code once; use only the newest. Never share the code with anyone, including us. Still nothing? Tell me your registered number. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ ኔትወርክዎን፣ ትክክለኛው ሲም መስራቱን እና የኤስኤምኤስ ሳጥንዎ አለመሙላቱን ያረጋግጡ። ስልክዎን አጥፍተው አብርተው ኮዱን አንድ ጊዜ ይጠይቁ፤ አዲሱን ብቻ ይጠቀሙ። ኮዱን ለማንም አያጋሩ፣ ለእኛም ጭምር። ካልደረሰዎት የተመዘገቡበትን ቁጥር ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is checking why our SMS messages are not reaching your number. Please avoid requesting more codes for now. We will update you by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ የእኛ ኤስኤምኤስ ለምን ወደ ቁጥርዎ እንደማይደርስ የቴክኒክ ቡድናችን እያጣራ ነው። እስከዚያው እባክዎ ተጨማሪ ኮድ አይጠይቁ። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

## Escalation Conditions
- Several customers (especially on one operator) not receiving SMS → **Technical / Engineering**, High.
- Correct number, all checks done, still nothing → **Technical / Engineering**, Medium (High if it blocks login to a paid booking).
- The customer received codes they did not request, or someone asked them for their code → **Trust & Safety** (possible account takeover attempt).
- Phone number must be changed → approved account-change process; **Senior Support / Supervisor** if identity can't be verified.

## Resolution Procedure
1. Confirm the customer received the SMS and completed their action (without sharing the code).
2. Record the cause (wrong number, SIM/signal, inbox full, rate limit, operator/provider issue, bug).

## Policy Pending Approval
- Confirm whether SMS/phone OTP is used for registration or login, and which events send SMS.
- Confirm the official SMS sender name so customers can recognise genuine messages.
- Confirm whether there is an approved alternative verification route when SMS fails.

## Internal Notes
- Ethiopian mobile numbers are often written in different formats (with +251, with a leading 0, or without either). Note exactly what the customer entered when reporting to Technical.
- Unrequested codes arriving are a warning sign that someone is trying to access the account.
- Repeated requests usually make things worse because of sending limits.

<!-- doc -->
# Problems on Mobile Browsers
id: tec-mobile-browser-problems
type: article
category: technical
subcategory: browser-device
audience: both
priority: medium
department: technical
tags: phone problem, mobile not working, android browser, opera mini, telegram browser, works on computer not phone, page too small, ስልክ ላይ አይሰራም, በስልክ, ኦፔራ ሚኒ
related: tec-tsg-browser-basics, tec-clear-cache-cookies, tec-buttons-not-working, tec-payment-gateway-error, tec-poor-connectivity, tec-upload-failures
templates: tpl-browser-troubleshooting, tpl-technical-investigation, tpl-request-screenshot
policy_pending: no

## Summary
Byfluence does not work properly on the customer's phone (pages, buttons, login, payments or uploads fail), even though it may work on a computer or another phone.

## Issue Description
Most Byfluence customers use the site on Android phones, often older models with limited storage, on mobile data, and frequently through links shared on Telegram, Facebook or TikTok. Problems that appear "only on my phone" usually come from the browser being used, data-saving modes, or the in-app browser — not from Byfluence itself.

## Possible Causes
- **In-app browsers**: opening a link inside Telegram, Facebook, Instagram or TikTok. These limit logins, pop-ups, payment redirects, file uploads and cookies.
- **Opera Mini** in *Extreme* data-saving mode (pages are processed on Opera's servers; many interactive features stop working).
- Chrome *Lite mode* / data saver, battery saver.
- Outdated browser or old Android version; outdated "Android System WebView".
- Low storage/memory on the phone.
- "Desktop site" turned on, or the page zoomed/text size very large so buttons are hidden.
- Browser auto-translate.
- Weak mobile connection.

## Information to Collect
- Phone brand/model and Android/iOS version (Settings → About phone)
- Browser used, and how they opened Byfluence (typed address, Telegram link, Facebook link)
- What fails (page, button, login, payment, upload) — screenshot/recording
- Whether it works on another phone or a computer
- Network type

## Troubleshooting Steps
1. Ask **how they opened the site**. If from Telegram/Facebook/TikTok → tap ⋮ / … → *Open in browser* / *Open in Chrome*. Suggest typing **byfluence.com** directly in Chrome next time, or adding it to the home screen (Chrome ⋮ → *Add to Home screen*).
2. **Opera Mini** users: Opera Mini menu → *Data savings* → turn off or choose *High* instead of *Extreme*; or use Chrome.
3. Update the browser (Play Store → search Chrome → Update). On Android, also update *Android System WebView* if it shows an update.
4. Turn off *Desktop site* (Chrome ⋮ → untick Desktop site); reset zoom/text size.
5. Turn off auto-translate, data saver/Lite mode and battery saver while using Byfluence.
6. Free some space and close other apps; restart the phone.
7. Clear site data for byfluence.com (tec-clear-cache-cookies).
8. If the phone is very old and the browser cannot be updated, suggest using another device for important actions (payment, uploads) if available.
9. If it still fails on an updated Chrome/Safari opened directly → escalate with device model, OS version, browser version and recording.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry the website isn't working well on your phone. These steps usually fix it:

1. Don't open Byfluence from inside Telegram, Facebook or TikTok. Tap the menu (⋮ or …) and choose "Open in browser", or type byfluence.com directly in Chrome
2. If you use Opera Mini, turn off "Extreme" data saving, or use Chrome
3. Update your browser from the Play Store or App Store
4. Close other apps and restart your phone

If it still doesn't work, please tell me your phone model, the browser you use, and send a screenshot of the problem. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ድረ-ገጹ በስልክዎ ላይ በደንብ ስላልሰራ ይቅርታ እንጠይቃለን። እነዚህ ደረጃዎች ብዙ ጊዜ ችግሩን ይፈታሉ፦

1. Byfluenceን በTelegram፣ Facebook ወይም TikTok ውስጥ ሆነው አይክፈቱ። ምናሌውን (⋮ ወይም …) ተጭነው "Open in browser" ይምረጡ፣ ወይም byfluence.com ን በቀጥታ በChrome ላይ ይጻፉ
2. Opera Mini የሚጠቀሙ ከሆነ "Extreme" የዳታ ቁጠባ ሁነታን ያጥፉ፣ ወይም Chrome ይጠቀሙ
3. ብሮውዘርዎን ከPlay Store ወይም ከApp Store ያዘምኑ (Update)
4. ሌሎች መተግበሪያዎችን ዘግተው ስልክዎን አጥፍተው ያብሩ

አሁንም ካልሰራ እባክዎ የስልክዎን ዓይነት፣ የሚጠቀሙበትን ብሮውዘር ይንገሩኝ፤ የችግሩንም የስክሪን ፎቶ ይላኩልኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please open byfluence.com directly in Chrome (not inside Telegram/Facebook), turn off Opera Mini "Extreme" mode, update your browser and restart your phone. Still not working? Send your phone model + a screenshot. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ byfluence.com ን በቀጥታ በChrome ይክፈቱ (በTelegram/Facebook ውስጥ ሳይሆን)፣ የOpera Mini "Extreme" ሁነታን ያጥፉ፣ ብሮውዘርዎን ያዘምኑ፣ ስልክዎንም አጥፍተው ያብሩ። ካልሰራ የስልክዎን ዓይነት እና የስክሪን ፎቶ ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is checking the problem on your phone model and browser. We will update you by {{follow_up_time}}. If you need to finish something urgent, using another phone or a computer may help in the meantime.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ የቴክኒክ ቡድናችን በስልክዎ ዓይነት እና በብሮውዘርዎ ላይ ያለውን ችግር እያጣራ ነው። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። በአስቸኳይ ማጠናቀቅ ያለብዎት ነገር ካለ፣ እስከዚያው ሌላ ስልክ ወይም ኮምፒውተር መጠቀም ሊረዳ ይችላል።

## Escalation Conditions
- Fails on an updated Chrome/Safari opened directly, on a common phone model → **Technical / Engineering**, Medium (High if it blocks payment/booking).
- Many customers on the same device/browser report the same issue → **Technical / Engineering**, High.
- Payment issues on mobile with possible deduction → **Payments & Finance**.

## Resolution Procedure
1. Confirm the customer completed their action on their phone.
2. Record device, OS, browser and what fixed it (this helps product decisions about supported devices).

## Internal Notes
- In-app browsers and Opera Mini Extreme cause most mobile-only problems. Ask about them first.
- Explain steps in very simple words; offer to go step by step. A screenshot from the customer helps you see which browser they are in.
- Do not recommend unofficial "APK" versions of browsers or any app claiming to be a Byfluence app.

<!-- doc -->
# "Session Expired" or Logged Out Unexpectedly
id: tec-session-expired
type: article
category: technical
subcategory: browser-device
audience: both
priority: medium
department: technical
tags: session expired, logged out, keeps logging me out, please log in again, signed out automatically, can't stay logged in, ከአካውንቴ ያስወጣኛል, session expired ይላል, ደጋግሞ ያስወጣኛል
related: tec-clear-cache-cookies, tec-mobile-browser-problems, tec-payment-gateway-error, acc-security-concern-phishing, tec-tsg-browser-basics
templates: tpl-browser-troubleshooting, tpl-technical-investigation
policy_pending: yes

## Summary
The customer sees "Session expired" or is logged out of Byfluence unexpectedly, sometimes repeatedly or in the middle of booking or payment.

## Issue Description
A session is how the website remembers that the customer is logged in. Sessions end after inactivity, after logout, or when cookies are lost. Customers notice it most when they are sent back to the login page during booking, payment or form filling and lose what they typed. Repeated unexpected logouts can also be a **security signal** (password changed by someone else, account accessed elsewhere), so agents must keep that possibility in mind.

## Possible Causes
- Inactivity: the page was left open for a long time.
- Cookies blocked or cleared: private/incognito mode, cleaning apps ("cleaner", "booster"), browser set to delete cookies on exit.
- **In-app browsers** (Telegram/Facebook) not keeping cookies; switching between in-app and normal browser.
- **Wrong phone date/time**.
- Logging in on several devices/browsers (depending on platform rules).
- Password reset or security action on the account.
- Payment redirect returned to a different browser than the one where they logged in.
- A platform bug in session handling.

## Information to Collect
- When it happens (after a while idle, during a specific step, every few clicks)
- Device, browser, and whether they opened Byfluence from Telegram/Facebook
- Whether they use private mode or a cleaner/booster app
- Whether they changed their password recently or received unexpected login/code messages
- If during payment: whether money was deducted (follow tec-payment-gateway-error)

> [!WARNING] Never ask for the customer's password or a login code to "check the session". If the customer reports logins or codes they did not request, treat it as a possible account compromise.

## Troubleshooting Steps
1. If it happened during **payment**, check the payment/booking status first.
2. Ask about **unexpected security signs** (codes they didn't request, password changes they didn't make, unknown activity). If yes → acc-security-concern-phishing / Trust & Safety.
3. Ask them to open byfluence.com **directly in Chrome/Safari**, not inside Telegram/Facebook, and to use the same browser for the whole booking and payment.
4. Check phone **date and time** are set automatically.
5. Turn off private mode for Byfluence; pause any "cleaner/booster" apps; make sure cookies are allowed (Chrome ⋮ → Settings → Site settings → Third-party cookies / Cookies → allow for byfluence.com if blocked).
6. Clear site data for byfluence.com once (tec-clear-cache-cookies), then log in again.
7. Advise: for long forms (e.g., listings), complete them without long pauses; save progress where the page allows.
8. If logouts happen within a short time while active, on an updated browser opened directly → escalate to Technical with device/browser and times.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry you keep getting logged out. Please try:

1. Open byfluence.com directly in Chrome or Safari (not inside Telegram or Facebook), and use the same browser for the whole booking and payment
2. Check that your phone's date and time are set automatically
3. Don't use private/incognito mode for Byfluence, and pause any phone "cleaner" or "booster" app
4. Log out, log in again, and continue without leaving the page idle for long

If you were paying when this happened, please tell me before paying again so I can check your payment.

For your safety: if you received login codes you didn't ask for, or your password was changed without you, please tell me right away. Never share your password or codes with anyone.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በተደጋጋሚ ከአካውንትዎ ስለሚያስወጣዎት ይቅርታ እንጠይቃለን። እባክዎ ይሞክሩ፦

1. byfluence.com ን በቀጥታ በChrome ወይም በSafari ይክፈቱ (በTelegram ወይም በFacebook ውስጥ ሳይሆን)፤ ቀጠሮ ማስያዙንና ክፍያውን በሙሉ በአንድ ብሮውዘር ያጠናቅቁ
2. የስልክዎ ቀን እና ሰዓት በራሱ (automatic) እንዲስተካከል መደረጉን ያረጋግጡ
3. ለByfluence private/incognito ሁነታ አይጠቀሙ፤ በስልክዎ ላይ ያሉ "cleaner" ወይም "booster" መተግበሪያዎችን ለጊዜው ያቁሙ
4. ወጥተው (log out) እንደገና ይግቡ፤ ገጹን ለረጅም ጊዜ ሳይነኩ ሳይተዉ ይቀጥሉ

ይህ የሆነው ክፍያ እየፈጸሙ ከሆነ፣ ክፍያዎን እንዳጣራ እንደገና ከመክፈልዎ በፊት እባክዎ ይንገሩኝ።

ለደህንነትዎ፦ ያልጠየቁት የመግቢያ ኮድ ከደረሰዎት ወይም ያለእርስዎ ፈቃድ የይለፍ ቃልዎ ከተቀየረ ወዲያውኑ ይንገሩኝ። የይለፍ ቃልዎን ወይም ኮዶችን ለማንም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please open byfluence.com directly in Chrome (not inside Telegram), keep your phone's date/time automatic, avoid private mode and cleaner apps, then log in again. Got codes you didn't request? Tell me now. Never share codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ byfluence.com ን በቀጥታ በChrome ይክፈቱ (በTelegram ውስጥ ሳይሆን)፣ የስልክዎን ቀንና ሰዓት automatic ያድርጉ፣ private mode እና cleaner apps አይጠቀሙ፤ ከዚያ እንደገና ይግቡ። ያልጠየቁት ኮድ ደርሶዎታል? አሁኑኑ ይንገሩኝ። ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is checking why you are being logged out. Is it still happening after the steps we shared? Please tell me roughly when it happens and on which page. We will update you by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ ለምን ከአካውንትዎ እንደሚያስወጣዎት የቴክኒክ ቡድናችን እያጣራ ነው። ያጋራናቸውን ደረጃዎች ከሞከሩ በኋላም አሁንም እየሆነ ነው? በግምት መቼ እና በየትኛው ገጽ ላይ እንደሚሆን ይንገሩኝ። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

## Escalation Conditions
- Unrequested codes, password changes or unknown activity → **Trust & Safety**, High.
- Logouts while active on an updated browser opened directly, or many users affected → **Technical / Engineering** (High if many).
- Logged out during payment with unclear payment status → **Payments & Finance**.

## Resolution Procedure
1. Confirm the customer can stay logged in and complete their action.
2. Record the cause (in-app browser, cookies blocked, cleaner app, date/time, security, bug).

## Policy Pending Approval
- Confirm how long a session lasts before automatic logout, and whether users can stay logged in on several devices.
- Confirm whether users are notified of new logins, so agents can explain it.

## Internal Notes
- A customer who says "someone else logged me out" or "I see bookings I didn't make" is a security case, not a technical one.
- "Cleaner" and "booster" apps common on Android phones delete cookies regularly — a frequent cause of repeated logouts.

<!-- doc -->
# How to Clear Cache and Cookies (Chrome, Safari, Opera Mini, Phones)
id: tec-clear-cache-cookies
type: article
category: technical
subcategory: browser-device
audience: both
priority: low
department: support_l1
tags: clear cache, clear cookies, delete browsing data, clear browser data, refresh browser, opera mini clear, ካሽ ማጽዳት, ኩኪ ማጥፋት, የብሮውዘር መረጃ ማጥፋት
related: tec-tsg-browser-basics, tec-mobile-browser-problems, tec-session-expired, tec-broken-page, tec-site-not-loading
templates: tpl-browser-troubleshooting
policy_pending: no

## Summary
Step-by-step instructions agents can send customers to clear Byfluence's stored data (cache and cookies) on Chrome, Safari, Opera Mini, Samsung Internet and computers.

## Overview
The browser saves parts of websites (**cache**) and login information (**cookies**) to load faster and keep users logged in. When these become old or damaged, pages look broken, buttons fail, or logins loop. Clearing them is safe but has one effect customers must know: **they will be logged out** and will need their login details.

**Agent rules:**
- Prefer clearing data **for byfluence.com only** — this does not log the customer out of Telegram Web, email or other sites.
- Ask the customer which browser they use (or ask for a screenshot) and send only the steps for that browser.
- Make sure the customer knows how to log in again (email/phone and password, or how to reset it) before they clear cookies.
- Send one step per line, in simple words. Offer to stay in the chat while they do it.
- Menu names differ slightly by phone and browser version; if the customer can't find an option, ask for a screenshot.

## Customer Steps

### Chrome on Android — only Byfluence (recommended)
1. Open Chrome and go to byfluence.com
2. Tap the icon to the left of the address (lock or settings icon)
3. Tap **Cookies and site data** (or **Site settings**)
4. Tap **Delete** / **Clear & reset**, then confirm
5. Reload byfluence.com and log in again

### Chrome on Android — all data (if the above is not available)
1. Open Chrome and tap **⋮** (three dots, top right)
2. Tap **History**, then **Delete browsing data** (or **Clear browsing data**)
3. Choose time range **All time**
4. Tick **Cookies and site data** and **Cached images and files**
5. Tap **Delete data**
6. Open byfluence.com and log in again

### Safari on iPhone
1. Open the **Settings** app (not Safari)
2. Tap **Safari** (on newer iPhones: **Apps → Safari**)
3. Tap **Advanced → Website Data**, search "byfluence" and swipe left to delete it
4. Or, to clear everything: tap **Clear History and Website Data** and confirm
5. Open Safari, go to byfluence.com and log in again

### Opera Mini
1. Open Opera Mini and tap the **Opera icon** or your **profile/menu** (bottom or top right)
2. Tap **Settings** (gear icon)
3. Tap **Clear browsing data** (sometimes under *Privacy*)
4. Tick **Cookies and site data** and **Cached images and files**, then **Clear**
5. While in Settings, open **Data savings** and turn off **Extreme** mode (choose High or Off)
6. Open byfluence.com again and log in

### Samsung Internet
1. Tap **≡** (menu, bottom right) → **Settings**
2. Tap **Personal browsing data** (or **Privacy**) → **Delete browsing data**
3. Tick **Cookies and site data** and **Cached images and files** → **Delete**
4. Open byfluence.com and log in again

### Computer (Chrome, Edge, Firefox)
1. Press **Ctrl + Shift + Delete** (on Mac: **Cmd + Shift + Delete**)
2. Choose time range **All time**
3. Tick **Cookies** and **Cached images and files**
4. Click **Delete / Clear data**
5. Open byfluence.com and log in again

### Amharic steps for the most common case (Chrome on Android)
1. Chrome ን ከፍተው byfluence.com ይግቡ
2. ከአድራሻው በስተግራ ያለውን ምልክት (የቁልፍ ወይም የሴቲንግ ምልክት) ይጫኑ
3. **Cookies and site data** (ወይም **Site settings**) የሚለውን ይጫኑ
4. **Delete** ወይም **Clear & reset** የሚለውን ተጭነው ያረጋግጡ
5. byfluence.com ን እንደገና ከፍተው ወደ አካውንትዎ ይግቡ

### Amharic steps — Opera Mini
1. Opera Mini ን ከፍተው የOpera ምልክቱን ወይም ምናሌውን ይጫኑ
2. **Settings** (የማርሽ ምልክት) ይጫኑ
3. **Clear browsing data** የሚለውን ይጫኑ
4. **Cookies and site data** እና **Cached images and files** የሚሉትን ምልክት አድርገው **Clear** ይጫኑ
5. በSettings ውስጥ **Data savings** ገብተው **Extreme** የሚለውን ያጥፉ
6. byfluence.com ን እንደገና ከፍተው ይግቡ

### Amharic steps — iPhone (Safari)
1. የስልክዎን **Settings** ይክፈቱ
2. **Safari** (በአዳዲስ iPhone ላይ **Apps → Safari**) የሚለውን ይጫኑ
3. **Clear History and Website Data** ተጭነው ያረጋግጡ
4. Safari ን ከፍተው byfluence.com ይግቡ

## Recommended Response (EN)
Hello {{customer_name}},

Clearing your browser's saved data for Byfluence should fix this. Note: you will be logged out, so please make sure you know your login details first.

If you use Chrome on Android:
1. Open Chrome and go to byfluence.com
2. Tap the icon to the left of the address
3. Tap "Cookies and site data" (or "Site settings")
4. Tap "Delete" (or "Clear & reset") and confirm
5. Reload byfluence.com and log in again

If you use a different browser (Opera Mini, Safari, Samsung Internet), tell me which one and I'll send the right steps. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ብሮውዘርዎ ለByfluence ያስቀመጠውን መረጃ ማጽዳት ችግሩን ሊፈታው ይችላል። ማሳሰቢያ፦ ከአካውንትዎ ይወጣሉ፤ ስለዚህ እባክዎ በመጀመሪያ የመግቢያ መረጃዎን እንደሚያውቁ ያረጋግጡ።

Chrome በAndroid ስልክ የሚጠቀሙ ከሆነ፦
1. Chrome ን ከፍተው byfluence.com ይግቡ
2. ከአድራሻው በስተግራ ያለውን ምልክት ይጫኑ
3. "Cookies and site data" (ወይም "Site settings") የሚለውን ይጫኑ
4. "Delete" (ወይም "Clear & reset") ተጭነው ያረጋግጡ
5. byfluence.com ን እንደገና ከፍተው ይግቡ

ሌላ ብሮውዘር (Opera Mini፣ Safari፣ Samsung Internet) የሚጠቀሙ ከሆነ የትኛውን እንደሆነ ይንገሩኝ፤ ትክክለኛውን መመሪያ እልክልዎታለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, in Chrome: open byfluence.com → tap the icon left of the address → "Cookies and site data" → Delete → reload and log in again (you'll be logged out). Using another browser? Tell me which. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በChrome፦ byfluence.com ይክፈቱ → ከአድራሻው በስተግራ ያለውን ምልክት ይጫኑ → "Cookies and site data" → Delete → ገጹን እንደገና ከፍተው ይግቡ (ከአካውንትዎ ይወጣሉ)። ሌላ ብሮውዘር ከሆነ የትኛው እንደሆነ ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Clearing data did not help and the issue continues on an updated browser → continue with the relevant technical article and escalate to **Technical / Engineering** if needed.
- After clearing, the customer cannot log in and cannot reset their password → follow account-access articles; **Senior Support / Supervisor** if identity can't be verified.

## Internal Notes
- Always warn about being logged out — customers who forget their password then get stuck.
- Never ask the customer to send their password so you can "log them back in".
- If the customer is not comfortable with settings, a private/incognito tab is a quick test before clearing anything.

<!-- doc -->
# Amharic Text Not Displaying Correctly / Typing Amharic
id: tec-language-display-amharic
type: article
category: technical
subcategory: browser-device
audience: both
priority: low
department: technical
tags: amharic not showing, boxes instead of letters, question marks, can't type amharic, amharic keyboard, geez font, fidel, አማርኛ አይታይም, አማርኛ መጻፍ አልቻልኩም, የአማርኛ ኪቦርድ, ፊደል
related: gen-languages-supported, tec-broken-page, tec-mobile-browser-problems, tec-calendar-time-display, tec-reporting-a-bug
templates: tpl-browser-troubleshooting, tpl-request-screenshot
policy_pending: yes

## Summary
Amharic (Ge'ez/Ethiopic) text shows as empty boxes, question marks or strange symbols, or the customer cannot type Amharic in Byfluence forms.

## Issue Description
Byfluence's primary language is Amharic. When the device or browser lacks Ethiopic font support, Amharic text appears as boxes (□□□), question marks or random characters. Sellers also need to type Amharic in listing titles, descriptions and profiles, and some do not have an Amharic keyboard installed. This article covers both display and typing.

## Possible Causes
**Display:**
- Old Android phone without an Ethiopic font, or a browser that does not use the system font.
- **Opera Mini Extreme mode** (pages rendered on Opera's servers) showing boxes.
- Browser auto-translate changing Amharic text.
- Text copied from another app in an old non-Unicode Amharic font (e.g., older Amharic word-processing fonts) — it shows as Latin letters or symbols.
- A platform bug (wrong encoding) — if it appears for everyone.

**Typing:**
- No Amharic keyboard installed or enabled on the phone/computer.
- Text pasted from an old non-Unicode document.

## Information to Collect
- Screenshot of how the text looks
- Which page (listing, profile, form) and whether it's Byfluence's own text or text the user typed
- Device and OS version, browser (and Opera Mini mode)
- For typing problems: phone/computer type and whether they have an Amharic keyboard

## Troubleshooting Steps
1. Open the same page yourself. If Amharic shows correctly for you → device/browser issue. If broken for you too → platform/content issue → step 6.
2. Turn off Opera Mini Extreme mode or use **Chrome**; turn off auto-translate.
3. Update the browser and, if possible, the phone software.
4. If the text was typed by a seller and looks wrong for everyone, it was likely pasted from a non-Unicode font. Ask the seller to retype it using a Unicode Amharic keyboard (steps below).
5. Help with typing Amharic:
   - **Android (Gboard):** Settings → System → Languages & input → On-screen keyboard → Gboard → Languages → Add keyboard → **Amharic (አማርኛ)**. Then press the globe 🌐 key to switch. If Gboard isn't installed, it is free in the Play Store.
   - **iPhone:** Settings → General → Keyboard → Keyboards → Add New Keyboard → look for **Amharic**. If not listed on their iOS version, a trusted keyboard app from the App Store may be used.
   - **Windows:** Settings → Time & language → Language & region → Add a language → **Amharic** → then switch with the language button on the taskbar (or Windows key + Space).
   - **Mac:** System Settings → Keyboard → Input Sources → Edit → + → **Amharic**.
6. If Byfluence's own Amharic text is broken for everyone (or for a common device/browser), escalate to Technical with screenshots, page link and device/browser.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry the Amharic text isn't showing properly.

Please try:
1. Open byfluence.com in Chrome (if you use Opera Mini, turn off "Extreme" mode)
2. If your browser offers to translate the page, choose "Show original"
3. Update your browser from the Play Store or App Store

To type in Amharic on an Android phone: open Settings → Languages & input → Gboard → Languages → Add keyboard → Amharic. Then tap the globe key on your keyboard to switch.

If it still looks wrong, please send me a screenshot and your phone model. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የአማርኛ ጽሑፍ በትክክል ስላልታየዎት ይቅርታ እንጠይቃለን።

እባክዎ ይሞክሩ፦
1. byfluence.com ን በChrome ይክፈቱ (Opera Mini የሚጠቀሙ ከሆነ "Extreme" ሁነታን ያጥፉ)
2. ብሮውዘርዎ ገጹን ልተርጉም ካለ "Show original" የሚለውን ይምረጡ
3. ብሮውዘርዎን ከPlay Store ወይም ከApp Store ያዘምኑ

በAndroid ስልክ አማርኛ ለመጻፍ፦ Settings → Languages & input → Gboard → Languages → Add keyboard → Amharic (አማርኛ) ይምረጡ። ከዚያ በኪቦርዱ ላይ ያለውን የዓለም ምልክት (🌐) ተጭነው ቋንቋውን ይቀይሩ።

አሁንም በትክክል ካልታየ እባክዎ የስክሪን ፎቶ እና የስልክዎን ዓይነት ይላኩልኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please open byfluence.com in Chrome (turn off Opera Mini "Extreme"), choose "Show original" if it's translating, and update your browser. To type Amharic: Settings → Languages & input → Gboard → Add keyboard → Amharic. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ byfluence.com ን በChrome ይክፈቱ (የOpera Mini "Extreme" ሁነታን ያጥፉ)፣ እየተረጎመ ከሆነ "Show original" ይምረጡ፣ ብሮውዘርዎንም ያዘምኑ። አማርኛ ለመጻፍ፦ Settings → Languages & input → Gboard → Add keyboard → Amharic። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is checking the Amharic display problem using your screenshot. We will update you by {{follow_up_time}}. Thank you for helping us improve Byfluence.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ የአማርኛ ጽሑፍ አለመታየት ችግሩን የቴክኒክ ቡድናችን በላኩልን የስክሪን ፎቶ መሰረት እያጣራ ነው። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። Byfluenceን ለማሻሻል ስለረዱን እናመሰግናለን።

## Escalation Conditions
- Byfluence's own Amharic text is broken for you or for many users → **Technical / Engineering**, Medium (High if it affects booking/payment pages).
- Amharic text broken on a common device/browser after updates → **Technical / Engineering**, Medium.
- Wrong or offensive Amharic wording in Byfluence's own pages → **Senior Support / Supervisor** (content owner).

## Resolution Procedure
1. Confirm Amharic now shows correctly, or the customer can type Amharic.
2. Record device/browser and the fix.

## Policy Pending Approval
- Confirm whether Byfluence offers a language switch (Amharic/English) on the website and where it is.
- Confirm whether other Ethiopian languages (e.g., Afaan Oromo, Tigrinya) are planned for the interface.

## Internal Notes
- Very old Android phones are the main cause of boxes; Chrome updates usually fix it.
- If a seller's listing text looks like random Latin letters, it was typed in an old non-Unicode Amharic font — retyping with Gboard Amharic fixes it.
- Be patient: some customers are learning to type Amharic on phones for the first time. Offer to send the steps as a voice note if your channel allows.

<!-- doc -->
# Dates or Times Displayed Wrong (Time Zone, Ethiopian vs Gregorian Calendar)
id: tec-calendar-time-display
type: article
category: technical
subcategory: browser-device
audience: both
priority: medium
department: technical
features: consultations-1on1, consultations-group, google-meet
tags: wrong time, wrong date, time zone, ethiopian time, gregorian calendar, ethiopian calendar, session time different, meet time wrong, ሰዓቱ ልክ አይደለም, የኢትዮጵያ ሰዓት, የኢትዮጵያ ዘመን አቆጣጠር, ቀኑ ተሳስቷል
related: con-time-zone-confusion, con-how-consultations-work, tec-booking-system-error, tec-session-expired, tec-language-display-amharic
templates: tpl-technical-investigation, tpl-request-screenshot
policy_pending: yes

## Summary
The customer believes a date or time on Byfluence (or in Google Meet / Google Calendar) is wrong — often because of time zones, the Ethiopian local clock, or the Ethiopian vs Gregorian calendar.

## Issue Description
Booking times matter: a misunderstanding leads to missed sessions, no-shows and refund disputes. Three different "systems" can confuse customers:
1. **Time zone** — Ethiopia uses East Africa Time (EAT, UTC+3). A customer abroad, or a phone/computer set to another time zone, will see times converted differently in Google Calendar/Meet.
2. **Ethiopian local clock** — in everyday Ethiopian usage, hours are counted from sunrise: ጠዋት 1 ሰዓት = 7:00 AM; ቀን 6 ሰዓት = 12:00 noon; ከሰዓት 9 ሰዓት = 3:00 PM; ምሽት 1 ሰዓት = 7:00 PM. Byfluence and Google Meet show international clock times, which many customers read as Ethiopian local time.
3. **Calendar** — the Ethiopian calendar has 13 months and a different year number from the Gregorian calendar used by most websites and Google. A date like "12/1" can be read in either system.

## Possible Causes
- Customer reads the international time as Ethiopian local time (most common).
- Phone/computer set to the wrong time zone, or manual (wrong) date/time.
- Customer outside Ethiopia; Google Calendar converts to their local zone.
- Ethiopian vs Gregorian date confusion.
- AM/PM confusion (12-hour vs 24-hour display).
- Seller set availability with a wrong time zone or misunderstanding.
- A platform bug storing or displaying times incorrectly.

## Information to Collect
- Booking reference (or consultation, seller, date) and the time the customer **expected**
- The time **shown** on Byfluence, in the confirmation, and in Google Meet/Calendar — screenshots
- Where the customer is located (Ethiopia or abroad) and their device time zone setting
- Whether the issue affects a buyer, a seller or both

## Troubleshooting Steps
1. Find the booking in authorized tools and note the stored date and time (and its time zone, as shown in admin).
2. Compare with what the customer sees:
   - Same time, customer reading it as Ethiopian local time → explain both ways. Example: "Your session is at 3:00 PM (ከሰዓት 9 ሰዓት)."
   - Different time on their device → check their phone's time zone (Settings → Date & time → automatic time zone / "Addis Ababa" / EAT).
   - Customer abroad → explain the session time in EAT and their local time equivalent if you can calculate it reliably; otherwise state EAT clearly.
   - Date confusion → say the date with the month name in words (Gregorian), and confirm the weekday ("Tuesday, 18 November").
3. For sellers: check their availability settings are in the correct time zone and that they understand the displayed times.
4. If the time stored or shown by Byfluence is wrong for everyone (e.g., all sessions shifted) → escalate as a **High** bug and identify affected upcoming bookings; follow con-time-zone-confusion for customer handling.
5. If a session was missed because of confusion, follow con-time-zone-confusion / consultation attendance articles; do not promise refunds or rebooking.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand the session time looks confusing — let me confirm it clearly.

Your consultation with {{seller_name}} is on {{booking_date}} at {{booking_time}}.

Please note: Byfluence shows times in the international clock format. For example, 3:00 PM on Byfluence is ከሰዓት 9 ሰዓት in Ethiopian local time.

If the time looks different on your phone, please check that your phone's date, time and time zone are set automatically (Settings → Date & time). If you are outside Ethiopia, tell me where you are and I will help you compare the times.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የምክክሩ ሰዓት ግራ እንዳጋባዎት ተረድቻለሁ — በግልጽ ላረጋግጥልዎ።

ከ{{seller_name}} ጋር ያለዎት ምክክር {{booking_date}} በ{{booking_time}} ነው።

ልብ ይበሉ፦ Byfluence ሰዓትን የሚያሳየው በዓለም አቀፍ (የፈረንጅ) የሰዓት አቆጣጠር ነው። ለምሳሌ፣ Byfluence ላይ 3:00 PM ማለት በኢትዮጵያ አቆጣጠር ከሰዓት 9 ሰዓት ማለት ነው።

በስልክዎ ላይ ሰዓቱ የተለየ ሆኖ ከታየዎት፣ እባክዎ የስልክዎ ቀን፣ ሰዓት እና የሰዓት ሰቅ (time zone) በራሱ (automatic) እንዲስተካከል መደረጉን ያረጋግጡ (Settings → Date & time)። ከኢትዮጵያ ውጭ ከሆኑ ያሉበትን ቦታ ይንገሩኝ፤ ሰዓቱን እንዲያነጻጽሩ እረዳዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your session with {{seller_name}} is on {{booking_date}} at {{booking_time}}. Byfluence uses the international clock — e.g., 3:00 PM = ከሰዓት 9 ሰዓት in Ethiopian time. Please keep your phone's time zone automatic. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ከ{{seller_name}} ጋር ያለዎት ምክክር {{booking_date}} በ{{booking_time}} ነው። Byfluence የሚጠቀመው የዓለም አቀፍ ሰዓት አቆጣጠር ነው — ለምሳሌ 3:00 PM = ከሰዓት 9 ሰዓት። እባክዎ የስልክዎን የሰዓት ሰቅ automatic ያድርጉ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is checking the time shown for your booking. Until we confirm, please use this time for your session: {{booking_date}} at {{booking_time}}. We will update you by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ ለቀጠሮዎ የሚታየውን ሰዓት የቴክኒክ ቡድናችን እያጣራ ነው። እስክናረጋግጥ ድረስ እባክዎ ይህንን ሰዓት ይጠቀሙ፦ {{booking_date}} በ{{booking_time}}። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

## Escalation Conditions
- The stored or displayed time is wrong on Byfluence's side (for you too, or for many bookings) → **Technical / Engineering**, High; list affected upcoming bookings.
- A session was missed because of time confusion and a refund/reschedule is requested → **Senior Support / Supervisor** (con-time-zone-confusion).
- Seller availability set in a wrong time zone affecting several buyers → **Seller Operations** and **Technical**.

## Resolution Procedure
1. Confirm the buyer (and seller, if needed) understand the correct session date and time, written in both international and Ethiopian local time.
2. Record whether the cause was customer interpretation, device settings or a platform bug.

## Policy Pending Approval
- Confirm which time zone Byfluence uses to store and display booking times, and whether the time zone is shown next to times on the website.
- Decide whether Byfluence will show Ethiopian local time and/or Ethiopian calendar dates alongside international times.
- Confirm how times are shown to buyers or sellers located outside Ethiopia.

## Internal Notes
- Always write session times in two ways for Amharic-speaking customers: "3:00 PM (ከሰዓት 9 ሰዓት)". This single habit prevents many no-shows.
- When you say a date, use the month name and weekday, not "12/1".
- `{{booking_time}}` should include the time zone (e.g., "3:00 PM EAT").
