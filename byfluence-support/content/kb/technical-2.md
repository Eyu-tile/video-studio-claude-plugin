<!-- doc -->
# Broken Page or Missing Content
id: tec-broken-page
type: article
category: technical
subcategory: functionality
audience: both
priority: medium
department: technical
tags: page broken, page looks wrong, images not showing, missing content, listing disappeared, blank section, page layout messed up, ገጹ ተበላሽቷል, ፎቶዎች አይታዩም, ይዘቱ ጠፍቷል
related: tec-buttons-not-working, tec-tsg-browser-basics, tec-clear-cache-cookies, tec-mobile-browser-problems, tec-language-display-amharic
templates: tpl-technical-investigation, tpl-browser-troubleshooting, tpl-request-screenshot
policy_pending: no

## Summary
A Byfluence page opens but looks wrong: the layout is broken, images or text are missing, sections are blank, or a listing/profile the customer expects is not there.

## Issue Description
The site loads, but a specific page does not display correctly. Common reports: "the photos are not showing", "the page is all text with no design", "the seller's page is empty", "my listing disappeared", "half the page is white". It is important to separate a **display problem** (the content exists but does not show on this device) from a **content problem** (the content was removed, hidden, unpublished or never saved), because they go to different teams.

## Possible Causes
**Display problems (device/browser/network):**
- Slow or interrupted connection — styles and images did not finish loading.
- Opera Mini Extreme mode or another data-saving mode stripping images and styles.
- Browser auto-**translate** (e.g., Google Translate) rewriting the page.
- Old cached version of the page; outdated browser.
- Ad blockers or "image blocking" settings.
- Missing Ethiopic font (Amharic shows as boxes) — see tec-language-display-amharic.

**Content problems (account/listing status):**
- The listing was **unpublished, under review, rejected or removed** by moderation.
- The seller's account is **Suspended or Banned**, or the seller is not yet Verified.
- The seller deleted or edited the listing; a consultation slot is fully booked or expired.
- The link is old or wrong (copied incorrectly, shared before an edit).

**Platform problems:**
- A bug after an update, or images not being served (storage/CDN problem).

## Information to Collect
- The exact page link (ask them to copy-paste it) and what they expected to see
- Screenshot of the broken page (tpl-request-screenshot)
- Device, browser (and mode, e.g., Opera Mini Extreme / in-app browser) and network
- When they last saw the content correctly
- For sellers: the listing name and whether they recently edited it or received any review/moderation message

## Troubleshooting Steps
1. Open the same link yourself.
   - **Looks fine for you** → display problem on the customer's side → step 2.
   - **Broken for you too** → check whether it's content or platform → step 4.
2. Customer-side display fixes, one at a time:
   1. Reload the page and wait until it fully loads.
   2. Turn off browser translation (Chrome: ⋮ → untick *Translate*; or tap "Show original").
   3. Opera Mini: switch off Extreme data saving, or use Chrome.
   4. Open in a private tab; then clear cache for byfluence.com (tec-clear-cache-cookies).
   5. Update the browser; try another browser or device.
3. If Amharic appears as boxes or question marks → tec-language-display-amharic.
4. **Content check (authorized tools):**
   - Look up the listing/seller in the admin dashboard: status (published, under review, rejected, removed), seller verification (Pending/Verified/Rejected) and operational status (Active/Suspended/Banned).
   - If the listing is under review/rejected/removed → explain to the **seller** in general terms and route to Seller Operations for listing decisions. To a **buyer**, only say the listing is not currently available — do not share the seller's account status.
5. **Platform check:** if content exists and is active but does not show for you or for many users (e.g., all images missing) → report to Technical (tec-reporting-a-bug) with the link, screenshot and time; check Announcements first.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry the page is not showing correctly.

Please try these steps:
1. Reload the page and let it load completely
2. If your browser is translating the page, choose "Show original" or turn translation off
3. If you use Opera Mini, turn off the "Extreme" data-saving mode, or open the page in Chrome

If it still looks wrong, please send me:
- The link of the page (copy and paste it)
- A screenshot of what you see
- Your phone model and browser name

Your case number is {{ticket_id}}. I will check it for you.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ገጹ በትክክል ስላልታየዎት ይቅርታ እንጠይቃለን።

እባክዎ እነዚህን ይሞክሩ፦
1. ገጹን እንደገና ከፍተው ሙሉ በሙሉ እስኪጫን ይጠብቁ
2. ብሮውዘርዎ ገጹን እየተረጎመ ከሆነ "Show original" የሚለውን ይምረጡ ወይም ትርጉሙን ያጥፉ
3. Opera Mini የሚጠቀሙ ከሆነ "Extreme" የሚለውን የዳታ ቁጠባ ሁነታ ያጥፉ፣ ወይም ገጹን በChrome ይክፈቱ

አሁንም በትክክል ካልታየ እባክዎ የሚከተሉትን ይላኩልኝ፦
- የገጹን ሊንክ (ኮፒ አድርገው ይለጥፉት)
- የሚያዩትን የስክሪን ፎቶ (screenshot)
- የስልክዎን ዓይነት እና የብሮውዘሩን ስም

የጉዳይዎ ቁጥር {{ticket_id}} ነው። አጣራልዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about that! Please reload the page, turn off auto-translate, and if you use Opera Mini switch off "Extreme" mode or try Chrome. Still broken? Send me the page link + a screenshot. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! እባክዎ ገጹን እንደገና ይክፈቱ፣ የትርጉም (translate) አገልግሎቱን ያጥፉ፤ Opera Mini ከሆነ "Extreme" ሁነታን ያጥፉ ወይም Chrome ይሞክሩ። አሁንም ከተበላሸ የገጹን ሊንክ እና የስክሪን ፎቶ ይላኩልኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: we have shared the page link and your screenshot with our technical team and they are checking why it is not displaying correctly. We will update you by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ የገጹን ሊንክ እና የላኩልንን የስክሪን ፎቶ ለቴክኒክ ቡድናችን አጋርተናል፤ ገጹ ለምን በትክክል እንደማይታይ እያጣሩ ነው። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- The page is broken for you too, or for many users (e.g., images missing site-wide) → **Technical / Engineering**, High if it affects listings, booking or payment pages.
- A seller's listing is missing because of review, rejection or removal → **Seller Operations**.
- A seller says their listing disappeared without any action from them and the admin shows no moderation action → **Technical / Engineering** and **Seller Operations**.
- The page shows someone else's personal data → **Trust & Safety**, priority Critical.

## Resolution Procedure
1. Ask the customer to reload the page and confirm it now displays correctly (or that they understand why the content is unavailable).
2. Record whether it was a display, content or platform cause.
3. For platform bugs, keep the ticket linked to the bug until the fix is confirmed, then send tpl-bug-fixed.

## Internal Notes
- Never tell a buyer that a seller is suspended or banned — just say the listing is not available right now.
- Browser auto-translation is a hidden cause of broken pages and broken buttons for customers whose phones are set to English but read Amharic content (or the reverse).
- "My listing disappeared" from a seller is often a moderation outcome — check the listing history before calling it a bug.

<!-- doc -->
# Buttons or Links Not Working
id: tec-buttons-not-working
type: article
category: technical
subcategory: functionality
audience: both
priority: medium
department: technical
tags: button not working, can't click, link does nothing, nothing happens when I tap, submit button disabled, stuck on page, ቁልፉ አይሰራም, ሲጫኑት ምንም አይሆንም, ሊንኩ አይከፈትም
related: tec-broken-page, tec-mobile-browser-problems, tec-tsg-browser-basics, tec-booking-system-error, tec-payment-gateway-error
templates: tpl-technical-investigation, tpl-browser-troubleshooting, tpl-request-screenshot
policy_pending: no

## Summary
The customer taps or clicks a button or link on Byfluence (e.g., Book, Pay, Save, Submit, Log in) and nothing happens, or the button stays grey/disabled.

## Issue Description
A button or link does not respond, keeps loading, or is greyed out. This blocks key flows (registration, booking, payment, listing creation, withdrawal requests). Often the button works as designed but is **disabled** because a required field is empty or invalid, and the error message is hidden higher up the page or below the visible area on a small screen.

## Possible Causes
- A required field is missing or invalid (e.g., date not selected, phone number in the wrong format, terms checkbox not ticked); the error is shown off-screen.
- The page did not finish loading (slow connection), so the scripts behind buttons are not ready.
- **Opera Mini Extreme mode** or JavaScript turned off.
- Opening the site inside Telegram/Facebook/TikTok (in-app browser) — new windows and payment pop-ups are blocked.
- **Pop-up blocker** stopping a new window (common for payment or Google Meet links).
- Browser auto-translation or an extension (ad blocker) interfering.
- A cookie/consent banner or keyboard covering the button on a small screen; page zoomed in.
- Double-tapping, which can cancel the first action.
- A platform bug.

## Information to Collect
- Which button/link (its label) and on which page (link)
- What happens when tapped (nothing, spins, greys out, error)
- Screenshot or short screen recording (tpl-request-screenshot)
- Device, browser and mode (in-app, Opera Mini), network
- Whether all fields on the page are filled in

## Troubleshooting Steps
1. If it's the **Pay** button or a payment step, first check whether a payment already went through (authorized tools) before letting the customer retry — follow tec-payment-gateway-error.
2. Ask the customer to **scroll up and down** the whole page for a red message or highlighted field, and to fill in every required field (date, time, checkbox).
3. Ask them to close the keyboard and any banner at the bottom (cookie notice), and zoom back to normal.
4. Wait for the page to fully load, then tap **once** and wait.
5. If opened from Telegram/Facebook/TikTok → *Open in browser* (Chrome/Safari).
6. Opera Mini → switch off Extreme mode or use Chrome.
7. Turn off auto-translate and ad blockers; allow pop-ups for byfluence.com if a new window is expected (Chrome: ⋮ → Settings → Site settings → Pop-ups and redirects).
8. Private tab → other browser → clear cache for byfluence.com (tec-tsg-browser-basics).
9. Try the same button yourself. If it fails for you too, or still fails for the customer after the checks → escalate to Technical with the page link, button label, device/browser and recording.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry the button is not working for you.

Please try these steps:
1. Scroll through the whole page and check that every required field is filled in (look for any red message)
2. Wait until the page has fully loaded, then tap the button once
3. If you opened Byfluence from Telegram, Facebook or TikTok, tap the menu (⋮ or …) and choose "Open in browser"
4. If you use Opera Mini, turn off "Extreme" mode or use Chrome

If it still does not work, please send me a screenshot or short screen recording and tell me which button and page it is. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ቁልፉ ስላልሰራልዎት ይቅርታ እንጠይቃለን።

እባክዎ እነዚህን ይሞክሩ፦
1. ገጹን ከላይ እስከ ታች ይመልከቱ፤ መሞላት ያለባቸው ቦታዎች በሙሉ መሞላታቸውን ያረጋግጡ (ቀይ መልዕክት ካለ ይመልከቱ)
2. ገጹ ሙሉ በሙሉ እስኪጫን ይጠብቁ፤ ከዚያ ቁልፉን አንድ ጊዜ ብቻ ይጫኑ
3. Byfluenceን ከTelegram፣ Facebook ወይም TikTok ውስጥ ከከፈቱት፣ ምናሌውን (⋮ ወይም …) ተጭነው "Open in browser" የሚለውን ይምረጡ
4. Opera Mini የሚጠቀሙ ከሆነ "Extreme" ሁነታን ያጥፉ ወይም Chrome ይጠቀሙ

አሁንም ካልሰራ እባክዎ የስክሪን ፎቶ ወይም አጭር የስክሪን ቪዲዮ ይላኩልኝ፤ የትኛው ቁልፍ እና የትኛው ገጽ እንደሆነም ይንገሩኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about that! Please check every required field is filled (look for red messages), let the page load fully and tap once. Opened from Telegram/Facebook? Choose "Open in browser". Still stuck? Send a screenshot. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! እባክዎ መሞላት ያለባቸው ቦታዎች በሙሉ መሞላታቸውን ያረጋግጡ (ቀይ መልዕክት ይመልከቱ)፣ ገጹ ሙሉ በሙሉ እስኪጫን ጠብቀው አንድ ጊዜ ይጫኑ። ከTelegram/Facebook ከከፈቱት "Open in browser" ይምረጡ። ካልሰራ የስክሪን ፎቶ ይላኩልኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is checking the button problem you reported using your screenshot and device details. We will update you by {{follow_up_time}}. If you need to complete something urgently (a booking or payment), reply here and we will help you.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ ያሳወቁትን የቁልፍ ችግር የቴክኒክ ቡድናችን በላኩልን የስክሪን ፎቶ እና የስልክ መረጃ እያጣራ ነው። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። በአስቸኳይ ማጠናቀቅ ያለብዎት ነገር (ቀጠሮ ወይም ክፍያ) ካለ እዚሁ ይጻፉልን፤ እንረዳዎታለን።

## Escalation Conditions
- The button fails for you too, or for several users → **Technical / Engineering**, High if it blocks booking, payment, registration or withdrawals.
- The button failed during payment and money may have been deducted → **Payments & Finance**.
- After basic checks it still fails for one customer → **Technical / Engineering**, Medium.

## Resolution Procedure
1. Ask the customer to complete the action while you are in the conversation, and confirm the result (booking created, profile saved, etc.).
2. Record the cause (missing field, in-app browser, Opera Mini, pop-up blocker, bug).
3. If a bug, link the ticket and follow up with tpl-bug-fixed after the fix.

## Internal Notes
- "Nothing happens" is very often a hidden validation message. Ask the customer to scroll before anything else.
- Phone numbers are a common validation problem — customers mix formats (with/without +251 or a leading 0). Note what they entered (not codes or passwords) for Technical.
- Never ask the customer to send their password so you can "try the button for them".

<!-- doc -->
# Unexpected Error Message
id: tec-unexpected-error-message
type: article
category: technical
subcategory: functionality
audience: both
priority: medium
department: technical
tags: error message, something went wrong, error 500, 404 not found, 503 service unavailable, oops, access denied, too many requests, የስህተት መልዕክት, ስህተት ተፈጥሯል, error ይላል
related: tec-tsg-technical-master, tec-reporting-a-bug, tec-site-not-loading, tec-session-expired, tec-known-outage-handling
templates: tpl-technical-investigation, tpl-request-screenshot, tpl-known-outage
policy_pending: no

## Summary
The customer sees an error message on Byfluence (e.g., "Something went wrong", "404", "500", "Access denied") and cannot continue.

## Issue Description
Error messages are the most useful clue the customer can give us. The agent's job is to get the **exact text** (or screenshot), understand roughly what kind of error it is, apply the right first steps, and escalate with the details if it is a platform error. The same message may appear during registration, login, booking, payment, uploads or withdrawals, so always note the action the customer was doing.

## Possible Causes
Use this table to interpret common messages (wording on Byfluence may differ — always rely on the exact text):

| Message / code | Usually means | First action |
|---|---|---|
| 404 / "Page not found" | Wrong or old link; page/listing removed | Check the link; search the listing; check listing status |
| 401 / "Unauthorized" / "Please log in" | Not logged in or session ended | Log in again (tec-session-expired) |
| 403 / "Access denied" / "Forbidden" | No permission (e.g., seller-only page, restricted account) or blocked network/VPN | Check account role/status; try without VPN / other network |
| 429 / "Too many requests" / "Try again later" | Too many attempts in a short time (often login or code requests) | Ask them to stop retrying and wait a while |
| 500 / "Internal server error" / "Something went wrong" | Server-side error | Collect time + action; check Announcements; escalate |
| 502 / 503 / 504 / "Service unavailable" / "Gateway timeout" | Server overloaded, maintenance or outage | Check Announcements; test yourself; escalate if widespread |
| "Network error" / "Failed to fetch" / "No internet" | Customer connection dropped | tec-poor-connectivity |
| "Your connection is not private" / certificate | Wrong phone date/time, or fake site | Fix date/time; verify the address is byfluence.com |
| Form messages ("Invalid phone number", "Field required") | Validation of what they typed | Guide them to correct the field |
| Payment provider messages ("Transaction failed", "Insufficient balance") | Shown by the payment provider | tec-payment-gateway-error / Payments articles |

## Information to Collect
- The exact error text and any code/number (screenshot preferred — tpl-request-screenshot)
- The page link and what they were doing (logging in, booking, paying, uploading…)
- Date and time it happened
- Device, browser and network
- Whether it happens every time or only once
- If during payment: payment method and transaction reference (if they received one)

> [!WARNING] If the screenshot shows a password, an OTP/verification code, a PIN or full card number, tell the customer not to share it again and delete or redact it from the ticket attachment per your team's process.

## Troubleshooting Steps
1. Get the **exact** message. "It says error" is not enough; ask for a screenshot.
2. Check **Announcements**. Server errors (500/502/503/504) during a known incident → tec-known-outage-handling.
3. Use the table above to apply the first action.
4. Try the same action yourself (where it does not involve the customer's account or money).
5. If the error happened **during payment**, check the transaction and booking status through authorized tools before any retry.
6. If the error is a validation or login message, guide the customer through it and confirm success.
7. If it is a server/platform error, or repeats after basic checks (tec-tsg-browser-basics), escalate with tec-reporting-a-bug, including the exact text and time (EAT).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry you received an error.

To find the cause, please send me:
1. A screenshot of the error message (or the exact words it shows)
2. What you were doing when it appeared (for example: logging in, booking, paying)
3. The time it happened
4. Your phone or computer model and the browser you use

If the error appeared while you were paying, please do not pay again until I check your payment status. Never share your password, PIN or verification codes with anyone, including us.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ የስህተት መልዕክት ስለገጠመዎት ይቅርታ እንጠይቃለን።

ምክንያቱን ለማወቅ እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የስህተት መልዕክቱን የስክሪን ፎቶ (ወይም መልዕክቱ ላይ የተጻፉትን ቃላት በትክክል)
2. መልዕክቱ ሲመጣ ምን እያደረጉ እንደነበር (ለምሳሌ፦ እየገቡ፣ ቀጠሮ እያስያዙ፣ እየከፈሉ)
3. የተፈጠረበትን ሰዓት
4. የስልክዎን ወይም የኮምፒውተርዎን ዓይነት እና የሚጠቀሙበትን ብሮውዘር

መልዕክቱ የመጣው ክፍያ እየፈጸሙ ከሆነ፣ የክፍያዎን ሁኔታ እስካጣራ ድረስ እባክዎ እንደገና አይክፈሉ። የይለፍ ቃልዎን፣ ፒንዎን ወይም የማረጋገጫ ኮዶችን ለማንም አያጋሩ — ለእኛም ጭምር።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about the error! Please send a screenshot of the message, what you were doing and the time. If it happened while paying, don't pay again until I check. (Never share passwords or codes.) Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ ስህተቱ ይቅርታ! እባክዎ የመልዕክቱን የስክሪን ፎቶ፣ ምን እያደረጉ እንደነበር እና ሰዓቱን ይላኩልኝ። ክፍያ እየፈጸሙ ከነበረ እስካጣራ ድረስ እንደገና አይክፈሉ። (የይለፍ ቃል ወይም ኮድ አያጋሩ።) የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is investigating the error you received, using the screenshot and time you sent. We will contact you again by {{follow_up_time}}. If the error message changes, please send a new screenshot here.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ የገጠመዎትን ስህተት የቴክኒክ ቡድናችን በላኩልን የስክሪን ፎቶ እና ሰዓት መሰረት እያጣራ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። የስህተት መልዕክቱ ከተቀየረ እባክዎ አዲስ የስክሪን ፎቶ እዚሁ ይላኩ።

## Escalation Conditions
- Server errors (500/502/503/504) for several users or for you too → **Technical / Engineering**, priority High/Critical; notify supervisor.
- Any error during payment with possible money deducted → **Payments & Finance** (and Technical if it's a platform error).
- "Access denied" for a seller who should have access, or an account status the customer disputes → **Seller Operations** (sellers) or **Senior Support / Supervisor** (buyers).
- Error messages that show another user's data or internal system details → **Trust & Safety** and **Technical**, Critical.

## Resolution Procedure
1. Confirm the customer can complete the action without the error.
2. Record the exact error text, cause and fix in the ticket (this builds our list of known errors).
3. For platform bugs, keep the ticket linked and send tpl-bug-fixed when resolved.

## Internal Notes
- Always write the exact error text in the ticket — engineers search logs by message and time.
- "429 / too many requests" usually comes from customers repeatedly requesting login codes. Tell them to stop and wait; repeated attempts make it worse.
- Do not explain technical codes to the customer in detail; keep it simple ("a problem on our side", "the page link is no longer valid").

<!-- doc -->
# Dashboard Won't Load
id: tec-dashboard-loading-error
type: article
category: technical
subcategory: functionality
audience: both
priority: high
department: technical
tags: dashboard not loading, dashboard blank, my account page empty, bookings not showing, earnings not loading, spinning dashboard, seller dashboard error, ዳሽቦርዱ አይከፈትም, ቀጠሮዎቼ አይታዩም, አካውንቴ ባዶ ነው
related: tec-session-expired, tec-unexpected-error-message, tec-tsg-browser-basics, tec-booking-system-error, tec-known-outage-handling
templates: tpl-technical-investigation, tpl-browser-troubleshooting, tpl-request-screenshot
policy_pending: no

## Summary
After logging in, the buyer or seller dashboard stays blank, keeps spinning, shows an error, or does not show bookings, transactions or earnings.

## Issue Description
The dashboard is where buyers see upcoming consultations, purchase and transaction history, and where sellers see listings, bookings, transactions, earnings and withdrawals. If it does not load, customers fear their bookings or money are gone. Separate three cases: (1) the dashboard does not load at all, (2) it loads but a section is empty or wrong, (3) the customer is in a **different account** than they think.

## Possible Causes
- Session expired or partly expired (the page shell loads but data does not) — tec-session-expired.
- Slow/unstable connection, so data sections time out.
- Old cache/cookies; in-app browser; Opera Mini Extreme mode.
- The customer is logged in to a **second account** (another email/phone) with no bookings.
- Seller account restrictions (Pending verification, Suspended) limiting what the seller dashboard shows.
- A platform bug or incident affecting dashboard data.
- For earnings: the amount is **pending** under settlement rules, which the seller reads as "missing" — this is not a technical error.

## Information to Collect
- Registered email or phone of the account they are logged in with (ask them to check their profile)
- Buyer or seller dashboard; which section fails (bookings, history, listings, earnings, withdrawals)
- What they see (blank, spinner, error text) — screenshot
- Device, browser and network; time it happened
- For bookings: booking/consultation reference or seller name and date, if they have it

## Troubleshooting Steps
1. Check **Announcements** for dashboard or login incidents.
2. Ask them to **log out and log in again**, then reload.
3. Confirm they are in the right account: ask which email/phone is shown on their profile and compare it with the account that has the bookings/transactions (via authorized tools).
4. Check in the admin dashboard that the data exists (bookings, transactions, listings, balances). If the data exists → it's a display/technical problem → continue. If it does not exist → it's not technical; route to the correct article (e.g., booking or payment issues).
5. Run basic checks: private tab, other browser, clear site data (tec-tsg-browser-basics), stable network.
6. For **sellers** seeing limited features, check verification status (Pending/Verified/Rejected) and operational status (Active/Suspended/Banned). Restrictions → Seller Operations, not Technical.
7. For **earnings that look wrong**, check whether amounts are pending vs available; route to payouts articles / Payments if the numbers don't match records.
8. If it still fails and data exists, escalate to Technical with screenshots, account ID (internal), device/browser and time.
9. **Urgent:** if the customer needs booking details (time, Meet link) for a session soon, give them the details from your tools while Technical investigates.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry your dashboard is not loading — please don't worry, your bookings and records are not deleted when the page fails to load.

Please try:
1. Log out, log in again, and reload the page
2. Check that you are logged in with the same email or phone number you used for your bookings
3. Try a different browser (for example Chrome) or a private tab

If it still does not load, please send me a screenshot and your phone and browser name. If you have a consultation coming up, tell me and I will share your booking details with you while we fix this.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ዳሽቦርድዎ ስላልተከፈተ ይቅርታ እንጠይቃለን — አይጨነቁ፤ ገጹ ባይከፈትም ቀጠሮዎችዎ እና መረጃዎችዎ አይጠፉም።

እባክዎ ይሞክሩ፦
1. ከአካውንትዎ ወጥተው (log out) እንደገና ይግቡ፣ ገጹንም እንደገና ይክፈቱ
2. ቀጠሮዎችዎን ባስያዙበት ተመሳሳይ ኢሜይል ወይም ስልክ ቁጥር መግባትዎን ያረጋግጡ
3. ሌላ ብሮውዘር (ለምሳሌ Chrome) ወይም private tab ይሞክሩ

አሁንም ካልተከፈተ እባክዎ የስክሪን ፎቶ እና የስልክዎን እና የብሮውዘርዎን ስም ይላኩልኝ። በቅርቡ ምክክር ካለዎት ይንገሩኝ፤ ችግሩን እስክናስተካክል ድረስ የቀጠሮዎን ዝርዝር እልክልዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry! Your records are safe. Please log out and in again, check it's the same email/phone you booked with, and try Chrome or a private tab. Still blank? Send a screenshot. Session soon? Tell me and I'll share the details. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! መረጃዎችዎ ደህና ናቸው። እባክዎ ወጥተው እንደገና ይግቡ፣ ቀጠሮ ባስያዙበት ተመሳሳይ ኢሜይል/ስልክ መሆኑን ያረጋግጡ፣ Chrome ወይም private tab ይሞክሩ። አሁንም ባዶ ከሆነ የስክሪን ፎቶ ይላኩ። በቅርቡ ምክክር ካለ ይንገሩኝ፤ ዝርዝሩን እልካለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is working on the dashboard problem. Your bookings and records remain saved in our system. We will update you by {{follow_up_time}}. If you need any booking or transaction details before then, just ask here.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ የቴክኒክ ቡድናችን የዳሽቦርዱን ችግር እየፈታ ነው። ቀጠሮዎችዎ እና መረጃዎችዎ በሲስተማችን ውስጥ ተቀምጠዋል። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። እስከዚያው የቀጠሮ ወይም የግብይት ዝርዝር ካስፈለገዎት እዚሁ ይጠይቁን።

## Escalation Conditions
- Data exists in admin but the dashboard won't show it after basic checks → **Technical / Engineering**, High (Critical if many users).
- Bookings or transactions are missing from admin records too → follow booking/payment articles; **Payments & Finance** if money is involved.
- Seller dashboard limited due to verification/suspension → **Seller Operations**.
- Earnings figures don't match transaction records → **Payments & Finance**.
- The dashboard shows another person's data → **Trust & Safety** + **Technical**, Critical.

## Resolution Procedure
1. Confirm the customer can see their dashboard and the section they needed.
2. If urgent booking details were shared manually, note it in the ticket.
3. Record the cause (session, wrong account, browser, restriction, bug).

## Internal Notes
- "Wrong account" is a frequent cause: customers register once with email and later with phone. Check before escalating.
- Never confirm account details to someone you have not verified as the account owner.
- Pending earnings are not a bug — explain using the approved payouts content rather than escalating to Technical.

<!-- doc -->
# Error While Booking a Consultation
id: tec-booking-system-error
type: article
category: technical
subcategory: functionality
audience: buyer
priority: high
department: technical
features: consultations-1on1, consultations-group, google-meet
tags: booking error, can't book consultation, time slot not available, booking failed, calendar not loading, cannot select date, booking button not working, ቀጠሮ መያዝ አልቻልኩም, ቀጠሮ ስህተት, ሰዓት መምረጥ አልቻልኩም
related: con-how-consultations-work, con-time-zone-confusion, tec-payment-gateway-error, tec-calendar-time-display, tec-buttons-not-working, tec-dashboard-loading-error
templates: tpl-technical-investigation, tpl-request-screenshot, tpl-browser-troubleshooting
policy_pending: yes

## Summary
The buyer gets an error, a frozen page or no available times when trying to book a one-on-one or group consultation, before reaching payment.

## Issue Description
Booking is: choose a consultation → pick date/time → (confirm details) → pay → booking confirmed after successful payment. This article covers failures **before or at the moment of moving to payment**: the calendar doesn't load, no slots appear, the chosen time is rejected, the "Book/Continue" step fails, or an error appears. If the buyer already paid and has no confirmation, use the Payments article *Customer Paid but Consultation Booking Was Not Confirmed* (pay-paid-booking-not-confirmed) instead.

## Possible Causes
- The seller has **no availability set** for the chosen dates, or the slot was just taken by another buyer.
- A **group session is full** (capacity reached) or registration closed.
- Time display confusion (time zone, Ethiopian local time vs international time) makes the buyer think a slot is missing — see tec-calendar-time-display / con-time-zone-confusion.
- The buyer is not logged in, or the session expired during the booking.
- The listing became unavailable (paused, under review, seller restricted).
- Browser problems (in-app browser, Opera Mini, old cache) or a weak connection.
- A platform bug in the booking calendar or slot reservation.

## Information to Collect
- Consultation/listing name or link and the seller/consultant name
- The date and time they want (and how they read the time — local Ethiopian time or international)
- What happens: no slots, error text, frozen button — screenshot
- Whether it's one-on-one or group
- Whether they reached the payment page or paid anything
- Device, browser, network, time of attempt

## Troubleshooting Steps
1. **Ask whether money was taken.** If yes → do not troubleshoot here; follow pay-paid-booking-not-confirmed.
2. Check **Announcements** for booking incidents.
3. Open the listing yourself and check availability for the requested date:
   - No slots for anyone → the seller has not opened availability; suggest other dates or other consultants. Optionally inform the seller through the approved process.
   - Group session full → tell the buyer it is full; suggest other sessions.
   - Listing not available → tell the buyer it's not available right now (don't disclose seller status).
4. Confirm the time interpretation. Many buyers count hours in Ethiopian local time. Clarify the slot time in both ways when possible (see tec-calendar-time-display).
5. Ask them to log in again and retry; then run browser basics (open in Chrome/Safari, not inside Telegram; turn off Opera Mini Extreme; private tab).
6. Try the booking flow yourself up to (not including) payment, if allowed. If it fails for you too → escalate as a bug (High).
7. If the buyer has a deadline (e.g., needs the session today) and the system fails, escalate to Senior Support to find an approved alternative; do not arrange bookings or payments outside the platform.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry you had trouble booking your consultation.

To help you quickly, please tell me:
1. The consultation name (or link) and the consultant's name
2. The date and time you want to book
3. What happens when you try (or send a screenshot)
4. Whether any money was taken from your account

Meanwhile, please try logging in again and opening Byfluence directly in Chrome or Safari (not inside Telegram or Facebook).

Please do not pay the consultant outside Byfluence — bookings and payments made outside the platform are not protected.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ምክክሩን ለማስያዝ ስለተቸገሩ ይቅርታ እንጠይቃለን።

በፍጥነት ልረዳዎ እባክዎ የሚከተሉትን ይንገሩኝ፦
1. የምክክሩን ርዕስ (ወይም ሊንክ) እና የአማካሪውን ስም
2. ማስያዝ የሚፈልጉትን ቀን እና ሰዓት
3. ለማስያዝ ሲሞክሩ ምን እንደሚሆን (ወይም የስክሪን ፎቶ ይላኩ)
4. ከሂሳብዎ ገንዘብ ተቆርጦ እንደሆነ

እስከዚያው እባክዎ እንደገና ገብተው Byfluenceን በቀጥታ በChrome ወይም በSafari ይክፈቱ (በTelegram ወይም በFacebook ውስጥ ሳይሆን)።

እባክዎ ለአማካሪው ከByfluence ውጭ ክፍያ አይፈጽሙ — ከፕላትፎርሙ ውጭ የሚደረጉ ቀጠሮዎች እና ክፍያዎች ጥበቃ የላቸውም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about the booking trouble! Please send the consultation name, the date/time you want, a screenshot of the error, and tell me if any money was taken. Try opening Byfluence directly in Chrome. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ቀጠሮ ለማስያዝ ስለተቸገሩ ይቅርታ! እባክዎ የምክክሩን ስም፣ የሚፈልጉትን ቀንና ሰዓት፣ የስህተቱን የስክሪን ፎቶ ይላኩ፤ ገንዘብ ተቆርጦ እንደሆነም ይንገሩኝ። Byfluenceን በቀጥታ በChrome ይክፈቱ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is checking the booking error for the consultation with {{seller_name}}. We will update you by {{follow_up_time}}. If you would like, I can also help you look at other available times or consultants in the meantime.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ ከ{{seller_name}} ጋር ለሚደረገው ምክክር የገጠመዎትን የቀጠሮ ስህተት የቴክኒክ ቡድናችን እያጣራ ነው። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። ከፈለጉ እስከዚያው ሌሎች ክፍት ሰዓቶችን ወይም አማካሪዎችን እንዲያዩ ልረዳዎ እችላለሁ።

## Escalation Conditions
- Booking fails for you too or for several buyers → **Technical / Engineering**, High (Critical if no bookings can be made).
- Money taken but no booking → **Payments & Finance** (pay-paid-booking-not-confirmed).
- Slots shown at clearly wrong times (time-zone bug) → **Technical / Engineering**, High.
- Buyer and seller both affected and a session deadline is near → **Senior Support / Supervisor**.
- A seller asks the buyer to pay outside the platform → **Trust & Safety**.

## Resolution Procedure
1. Confirm the booking was created (and paid/confirmed if they continued).
2. Confirm the buyer understands the session time correctly.
3. Record the cause (no availability, full group, time confusion, browser, bug).

## Policy Pending Approval
- Confirm whether support agents may create or hold a booking on a buyer's behalf when the booking system fails.
- Confirm the rules for full group sessions (waitlists, extra seats) and whether buyers can be told when new sessions open.
- Confirm whether and how support should notify a seller that their availability is empty or wrong.

## Internal Notes
- Off-platform payment requests are a fraud signal and break buyer protection — always discourage them.
- Many "no slots" complaints are time-zone or local-time misunderstandings. Confirm the time in words: "2:00 in the afternoon (ከሰዓት 8 ሰዓት)".
- Do not tell the buyer that a seller is suspended; just say the consultation is not available right now.

<!-- doc -->
# Payment Page Error or Payment Gateway Won't Open
id: tec-payment-gateway-error
type: article
category: technical
subcategory: functionality
audience: buyer
priority: high
department: technical
features: payments-chapa, payments-telebirr, payments-mpesa, payments-bank, payments-card
tags: payment page not opening, payment error, chapa not opening, gateway error, stuck on payment, redirect failed, payment page blank, pay button not working, የክፍያ ገጹ አይከፈትም, ክፍያ ስህተት, መክፈል አልቻልኩም
related: pay-supported-methods, pay-payment-security, pay-paid-booking-not-confirmed, tec-buttons-not-working, tec-mobile-browser-problems, tec-session-expired
templates: tpl-technical-investigation, tpl-request-screenshot, tpl-browser-troubleshooting
policy_pending: yes

## Summary
The customer cannot reach or complete the payment page: the payment provider's page does not open, is blank, shows an error, or the customer is not returned to Byfluence after paying.

## Issue Description
When a buyer taps Pay, Byfluence normally sends them to the payment provider's page, then back to Byfluence after payment. Failures at this step are high priority because (1) the customer may have already been charged, (2) they may retry and pay twice, and (3) a booking slot may be lost. The very first question is always: **was any money deducted?**

## Possible Causes
- The site is opened inside Telegram/Facebook/TikTok (in-app browser), which blocks the redirect or new window.
- A pop-up blocker stops the payment window.
- Opera Mini Extreme mode, or an old browser that cannot load the provider page.
- Weak/interrupted connection during redirect.
- The session expired before payment (tec-session-expired).
- The selected payment method is not available yet (only some methods may be live — check Feature Status / pay-supported-methods).
- The payment provider is down or slow (third-party incident).
- Customer-side payment issues (insufficient balance, limits, wrong details) shown by the provider.
- A platform bug in creating the payment request.

## Information to Collect
- Was money deducted? If yes: amount, date/time, payment method, transaction reference from SMS/receipt
- What they were paying for (consultation name, seller, date/time)
- The exact error text or a screenshot of the payment screen
- Payment method chosen
- Device, browser (and whether in-app), network

> [!WARNING] Never ask for card numbers, CVV, PINs, mobile-money PINs, passwords or OTP codes. A transaction reference and a screenshot of the receipt are enough. Never send the customer a payment link from a personal account or ask them to pay to a phone number.

## Troubleshooting Steps
1. **Ask if money was deducted.**
   - **Yes** → tell the customer not to pay again. Check the transaction and booking in authorized tools. Then follow pay-paid-booking-not-confirmed (Payments). Stop technical troubleshooting until money is clarified.
   - **No / not sure** → continue, but still check whether a pending/successful payment exists before telling them to retry.
2. Check **Announcements** for payment or provider incidents.
3. Check the chosen method is available (Feature Status / pay-supported-methods). If not available, explain which methods are currently supported.
4. Ask them to open byfluence.com **directly in Chrome or Safari** (not in Telegram/Facebook), log in again and go back to the booking.
5. Allow pop-ups for byfluence.com; turn off Opera Mini Extreme mode; ensure a stable connection.
6. If the provider shows its own message (e.g., insufficient balance, limit exceeded, wrong details), explain that this comes from the payment provider and suggest checking with their provider or using another available method.
7. Only after confirming no successful or pending payment exists, allow **one** retry while you are in the conversation.
8. If the page still fails, or fails for you/others too → escalate to Technical (High) with screenshot, method, time; inform Payments if the provider seems down.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry you had trouble with the payment page.

First, please tell me: was any money taken from your account? If yes, please send the transaction reference from your SMS or receipt, the amount and the time — and please do not pay again until I check.

If no money was taken, please try:
1. Open byfluence.com directly in Chrome or Safari (not inside Telegram or Facebook)
2. Log in again and go back to your booking
3. Make sure your internet connection is stable, then tap Pay once and wait

Please never share your PIN, password, card details or verification codes — Byfluence will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በክፍያ ገጹ ላይ ስለተቸገሩ ይቅርታ እንጠይቃለን።

በመጀመሪያ እባክዎ ይንገሩኝ፦ ከሂሳብዎ ገንዘብ ተቆርጧል? ከተቆረጠ፣ ከኤስኤምኤስ ወይም ከደረሰኙ ላይ ያለውን የግብይት መለያ ቁጥር (transaction reference)፣ መጠኑን እና ሰዓቱን ይላኩልኝ — እስካጣራ ድረስም እባክዎ እንደገና አይክፈሉ።

ገንዘብ ካልተቆረጠ እባክዎ ይሞክሩ፦
1. byfluence.com ን በቀጥታ በChrome ወይም በSafari ይክፈቱ (በTelegram ወይም በFacebook ውስጥ ሳይሆን)
2. እንደገና ገብተው ወደ ቀጠሮዎ ይመለሱ
3. የኢንተርኔት ግንኙነትዎ የተረጋጋ መሆኑን ያረጋግጡ፤ ከዚያ "Pay" የሚለውን አንድ ጊዜ ብቻ ተጭነው ይጠብቁ

እባክዎ ፒንዎን፣ የይለፍ ቃልዎን፣ የካርድ መረጃዎን ወይም የማረጋገጫ ኮዶችን በፍጹም አያጋሩ — Byfluence በፍጹም አይጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry! Was money taken? If yes, send the transaction reference, amount and time — and don't pay again until I check. If not, open byfluence.com directly in Chrome, log in again and tap Pay once. (Never share PINs or codes.) Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! ገንዘብ ተቆርጧል? ከተቆረጠ የግብይት ቁጥሩን፣ መጠኑን እና ሰዓቱን ይላኩ — እስካጣራ ድረስ እንደገና አይክፈሉ። ካልተቆረጠ byfluence.com ን በቀጥታ በChrome ከፍተው እንደገና ይግቡ፣ "Pay" አንድ ጊዜ ይጫኑ። (ፒን ወይም ኮድ አያጋሩ።) የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our team is still checking the payment page problem and your payment status. Please do not make another payment for this booking until we confirm. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ ቡድናችን የክፍያ ገጹን ችግር እና የክፍያዎን ሁኔታ አሁንም እያጣራ ነው። እስክናረጋግጥ ድረስ እባክዎ ለዚህ ቀጠሮ ሌላ ክፍያ አይፈጽሙ። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Money deducted and no booking, or possible double payment → **Payments & Finance**, High.
- Payment page fails for you too or for several buyers → **Technical / Engineering**, Critical; notify supervisor.
- Provider appears down → **Payments & Finance** (provider contact) and **Technical**.
- Customer was sent a payment link or account number by someone claiming to be Byfluence or the seller → **Trust & Safety**, High (see pay-payment-security).

## Resolution Procedure
1. Confirm the payment is either successful with a confirmed booking, or confirmed not taken (no duplicate).
2. Confirm the customer received booking confirmation/meeting details if paid.
3. Record method, reference, cause (in-app browser, provider outage, bug, customer-side) and outcome.

## Policy Pending Approval
- Confirm which payment methods are live in production (Chapa, Telebirr, M-Pesa, bank, card) and keep the Feature Status page updated.
- Confirm whether a booking slot is held while the buyer is on the payment page, and for how long.
- Confirm the approved customer wording about how long a pending payment takes to update.

## Internal Notes
- The most common technical cause is the in-app browser (Telegram/Facebook). Ask early.
- Never let a customer retry "a few times" — each retry can create a charge.
- Screenshots of receipts can be edited; verify payments by reference in authorized tools only.

<!-- doc -->
# File or Image Upload Fails
id: tec-upload-failures
type: article
category: technical
subcategory: uploads
audience: both
priority: medium
department: technical
tags: upload failed, can't upload photo, image not uploading, document upload error, file too large, profile picture not saving, ID upload failed, ፎቶ መጫን አልቻልኩም, ፋይል አይጫንም, መታወቂያ መጫን አልቻልኩም
related: tec-poor-connectivity, tec-mobile-browser-problems, tec-tsg-browser-basics, sel-how-to-become-seller, tec-unexpected-error-message
templates: tpl-technical-investigation, tpl-request-screenshot, tpl-browser-troubleshooting
policy_pending: yes

## Summary
The customer cannot upload a file — a profile photo, listing image or verification document — because the upload fails, freezes or shows an error.

## Issue Description
Uploads are used for profile pictures, listing images and seller identity verification documents. Failures block sellers from completing onboarding or publishing listings. Uploads are sensitive to connection quality, file size/format and browser permissions, and they fail more often on older Android phones and in-app browsers.

## Possible Causes
- **File too large** (high-resolution camera photos, scanned PDFs) or an unsupported format (e.g., iPhone **HEIC** photos, WEBP, very large PDFs).
- Weak or unstable connection — upload times out.
- Opening Byfluence inside Telegram/Facebook (in-app browser cannot open the file picker or camera).
- Opera Mini Extreme mode not supporting uploads.
- Browser lacks permission to access photos/files or the camera.
- Low phone storage; the file is in cloud storage (Google Drive/iCloud) and not downloaded to the phone.
- File name with unusual characters, or a corrupted file.
- A platform/storage bug.

## Information to Collect
- What they are uploading (profile photo, listing image, verification document) and on which page
- File type and approximate size (e.g., "photo from camera", "PDF scan")
- Exact error message or screenshot
- Device, browser (in-app or not), network
- Whether any upload has ever worked for them

> [!WARNING] Do not ask customers to send identity documents through Telegram, email or chat as a workaround unless an approved secure process exists. Ask only for a screenshot of the **error**, not of the document.

## Troubleshooting Steps
1. Check **Announcements** for upload/storage incidents.
2. Ask them to open byfluence.com directly in **Chrome or Safari** (not inside Telegram/Facebook) and turn off Opera Mini Extreme mode.
3. Ask for a stable connection (Wi-Fi if possible) and to keep the page open until the upload finishes.
4. **Reduce the file:**
   - Photo: take a screenshot of the photo, or use the phone's *Edit → Crop/Resize*, then upload the smaller image.
   - iPhone: change Camera → Formats → **Most Compatible** (saves JPG instead of HEIC) or upload a screenshot of the photo.
   - Document: take a clear photo (JPG) instead of a large scanned PDF, if the page accepts images.
5. Make sure the file is saved on the phone (not only in Google Drive/iCloud) and rename it simply (e.g., "id-front.jpg").
6. Allow the browser access to photos/files/camera (phone Settings → Apps → Chrome → Permissions).
7. Try another browser or a computer.
8. Try uploading a similar test file yourself (never the customer's document). If it fails → escalate as a bug with page, file type/size, error, device/browser.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry your upload did not work. Here are a few simple fixes:

1. Open byfluence.com directly in Chrome or Safari (not inside Telegram or Facebook)
2. Use a stable connection, and keep the page open until the upload finishes
3. Make the file smaller — for a photo, crop it or take a screenshot of it and upload that
4. On iPhone, if the photo will not upload, try a screenshot of the photo instead
5. Allow your browser to access your photos and files when your phone asks

If it still fails, please send me a screenshot of the error message (not of your document) and tell me your phone model and browser. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ፋይሉን መጫን ስላልቻሉ ይቅርታ እንጠይቃለን። እነዚህን ቀላል መፍትሄዎች ይሞክሩ፦

1. byfluence.com ን በቀጥታ በChrome ወይም በSafari ይክፈቱ (በTelegram ወይም በFacebook ውስጥ ሳይሆን)
2. የተረጋጋ ኢንተርኔት ይጠቀሙ፤ ፋይሉ ተጭኖ እስኪያልቅ ድረስ ገጹን አይዝጉ
3. ፋይሉን ያሳንሱት — ፎቶ ከሆነ ይቁረጡት (crop) ወይም የፎቶውን የስክሪን ፎቶ አንስተው ያንን ይጫኑ
4. iPhone ላይ ፎቶው ካልተጫነ የፎቶውን የስክሪን ፎቶ (screenshot) ይሞክሩ
5. ስልክዎ ሲጠይቅ ብሮውዘሩ ፎቶዎችዎን እና ፋይሎችዎን እንዲጠቀም ይፍቀዱ

አሁንም ካልሰራ እባክዎ የስህተት መልዕክቱን የስክሪን ፎቶ ይላኩልኝ (የሰነድዎን ፎቶ ሳይሆን)፤ የስልክዎን ዓይነት እና ብሮውዘሩንም ይንገሩኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry! Please open byfluence.com directly in Chrome/Safari, use a stable connection, and make the file smaller (crop it or upload a screenshot of the photo). Still failing? Send a screenshot of the error (not your document). Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! እባክዎ byfluence.com ን በቀጥታ በChrome/Safari ይክፈቱ፣ የተረጋጋ ኢንተርኔት ይጠቀሙ፣ ፋይሉንም ያሳንሱ (crop ያድርጉ ወይም የፎቶውን screenshot ይጫኑ)። ካልሰራ የስህተቱን የስክሪን ፎቶ ይላኩ (የሰነድዎን አይደለም)። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is checking the upload problem. Please do not send your documents through chat in the meantime. We will update you by {{follow_up_time}} and let you know when you can try again.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ የቴክኒክ ቡድናችን የፋይል መጫን ችግሩን እያጣራ ነው። እስከዚያው እባክዎ ሰነዶችዎን በቻት አይላኩ። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን፤ እንደገና መሞከር ሲችሉም እናሳውቅዎታለን።

## Escalation Conditions
- Uploads fail for you too or for many users → **Technical / Engineering**, High.
- A seller cannot submit verification documents after all checks → **Technical / Engineering** and inform **Seller Operations** (onboarding blocked).
- A customer sent identity documents through chat → follow your data-handling process and inform **Trust & Safety** if required.
- An uploaded image appears on another user's profile/listing → **Trust & Safety** + **Technical**, Critical.

## Resolution Procedure
1. Ask the customer to upload again and confirm the file now appears (profile, listing or verification status).
2. Record the cause (file size/format, in-app browser, connection, permissions, bug).
3. For verification documents, confirm the submission status shows as received/pending review.

## Policy Pending Approval
- Confirm the accepted file types and maximum file sizes for profile photos, listing images and verification documents, so agents can tell customers exactly.
- Decide whether an alternative secure channel exists for sellers who cannot upload verification documents, and who may receive them.
- Confirm how long received documents are stored and who can view them (privacy).

## Internal Notes
- iPhone HEIC photos and large scans are the top causes. A screenshot of the photo is a simple, reliable workaround.
- Never save customers' ID documents to personal devices or forward them in group chats.
- Listing images that are rejected for content reasons are a moderation matter, not an upload failure.
