<!-- doc -->
# Website Not Loading
id: tec-site-not-loading
type: article
category: technical
subcategory: site-access
audience: both
priority: high
department: technical
tags: website not opening, site down, can't open byfluence, page not loading, this site can't be reached, connection timed out, your connection is not private, ድረ-ገጹ አይከፈትም, ገጹ አይሰራም, ሳይቱ አይከፈትም
related: tec-slow-website, tec-poor-connectivity, tec-known-outage-handling, tec-tsg-browser-basics, tec-clear-cache-cookies, acc-security-concern-phishing
templates: tpl-technical-investigation, tpl-browser-troubleshooting, tpl-known-outage, tpl-request-screenshot
policy_pending: no

## Summary
The customer cannot open byfluence.com at all — they see a blank screen, an endless loading bar, or a browser message such as "This site can't be reached" or "Your connection is not private".

## Issue Description
The customer types or taps the Byfluence address and nothing useful appears. This is different from a *slow* site (the page eventually opens) and from a *broken page* (the site opens but one page is wrong). The problem can sit on the customer's side (data balance, network, phone settings, wrong address) or on our side (outage, deployment, DNS or certificate problem). Because both buyers and sellers depend on the site for bookings, payments and Google Meet details, a customer who cannot open the site shortly before a consultation is time-sensitive.

## Possible Causes
- **Byfluence is down or partly down** (outage, maintenance, failed deployment) — check Announcements first.
- The customer's **mobile data or airtime package has run out**, or Wi-Fi is connected but has no internet.
- **Local network or regional internet disruption** (mobile operator outage, regional shutdown, power cut affecting the Wi-Fi router).
- **Wrong address**: typo (e.g., "byfluense.com"), an old bookmark, or a **look-alike/fake site** sent through Telegram or social media.
- **Phone date and time set incorrectly** — very common; it causes "Your connection is not private" / `NET::ERR_CERT_DATE_INVALID` errors because the security certificate looks expired.
- Corrupted browser cache or cookies.
- **Opera Mini "Extreme" data-saving mode**, a VPN, a proxy or an ad-blocking DNS app blocking the site.
- Very old browser or Android version that no longer supports modern security (TLS).
- Company, school or public Wi-Fi blocking the site.

## Information to Collect
- Registered email or phone number (to check for related open tickets)
- Device type and model (e.g., Android phone, iPhone, laptop)
- Browser and version if known (Chrome, Opera Mini, Safari, Samsung Internet, browser inside Telegram/Facebook)
- Network type: mobile data (which operator) or Wi-Fi
- The exact address they are typing or the link they tapped (ask them to copy-paste it)
- The exact error message on screen (word for word) and the time it happened
- Screenshot of the screen (ask with tpl-request-screenshot)
- Whether other websites (e.g., Google) open on the same phone/network
- Whether they have an upcoming consultation or an unfinished payment

> [!WARNING] Never ask for the customer's password, OTP code or PIN while troubleshooting access. If the customer reached a site that asked for their password or payment details and the address was not byfluence.com, follow *Phishing / security concern* immediately.

## Troubleshooting Steps
1. **Check Announcements** in the support app for a known incident or maintenance. If one exists, stop troubleshooting and follow *Handling contacts during a known outage* (tec-known-outage-handling).
2. **Open https://byfluence.com yourself** (on your work device and, if possible, on a phone using mobile data).
   - It does not load for you either → possible outage. Tell your supervisor immediately and report it to Technical (see tec-reporting-a-bug). Check whether other agents are receiving the same complaint.
   - It loads for you → the problem is most likely on the customer's side; continue.
3. **Check the address.** Ask the customer to copy-paste the link they are using. Confirm it is exactly `byfluence.com`. If it is a different domain, treat it as a possible phishing site — do not let them enter details there, and follow acc-security-concern-phishing.
4. **Check their internet.** Ask whether Google or YouTube opens. If nothing opens, the issue is their connection or data balance → follow *Slow or unstable internet connection* (tec-poor-connectivity).
5. **Read the error message** and act on it:
   - "Your connection is not private" / "certificate" / "date invalid" → ask them to check their phone's date and time and turn on *automatic date & time*. Then reload.
   - "This site can't be reached" / "DNS_PROBE" / "ERR_NAME_NOT_RESOLVED" → switch between Wi-Fi and mobile data; turn airplane mode on and off; turn off any VPN or "data saver" app.
   - "Connection timed out" → weak signal or congested network; try again from a different location or network.
   - "403 / Access denied" → they may be on a blocked network (office/school Wi-Fi) or using a VPN; try mobile data.
   - "500 / 502 / 503 / 504" → server-side error; collect the time and escalate (see tec-unexpected-error-message).
6. **Run the basic browser checks** (tec-tsg-browser-basics): reload, open in a private/incognito tab, try a different browser (Chrome is the safest choice on Android), update the browser, clear cache and cookies for the site (tec-clear-cache-cookies).
7. If they use **Opera Mini**, ask them to switch data-saving mode off or to "High" (not "Extreme"), or to use Chrome.
8. If they are opening the link **inside Telegram, Facebook or TikTok**, ask them to tap the menu (⋮ or …) and choose *Open in browser* / *Open in Chrome*.
9. If still not working, and it works for you, collect device/browser/network details and a screenshot and escalate to Technical with tpl-technical-investigation.
10. If the customer has a **consultation soon** or an **unfinished payment**, help them with the urgent part through support (e.g., confirm the booking status and meeting details from your tools) while the access problem is investigated.

- [ ] Announcements checked
- [ ] Site tested by the agent
- [ ] Address confirmed as byfluence.com
- [ ] Customer's internet confirmed working
- [ ] Error message recorded word for word
- [ ] Basic browser checks done

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm sorry you are having trouble opening the website — let's fix this together.

Please try these simple steps:
1. Make sure the address is exactly byfluence.com
2. Check that other websites (for example Google) open on your phone
3. Check that your phone's date and time are correct (turn on "automatic date & time")
4. Switch between Wi-Fi and mobile data, then reload the page
5. Try a different browser, such as Chrome

If it still does not open, please send me:
- A screenshot of what you see on the screen
- The name of your phone and the browser you use
- Whether you are using Wi-Fi or mobile data

Your case number is {{ticket_id}}. I will stay with you until we find the cause.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ድረ-ገጹን ለመክፈት ስለተቸገሩ ይቅርታ እንጠይቃለን — በጋራ እናስተካክለው።

እባክዎ እነዚህን ቀላል ደረጃዎች ይሞክሩ፦
1. የሚጽፉት አድራሻ በትክክል byfluence.com መሆኑን ያረጋግጡ
2. ሌሎች ድረ-ገጾች (ለምሳሌ Google) በስልክዎ ላይ እንደሚከፈቱ ይመልከቱ
3. የስልክዎ ቀን እና ሰዓት ትክክል መሆናቸውን ያረጋግጡ ("automatic date & time" የሚለውን ያብሩ)
4. ከWi-Fi ወደ ሞባይል ዳታ (ወይም በተቃራኒው) ቀይረው ገጹን እንደገና ይክፈቱ
5. ሌላ ብሮውዘር ለምሳሌ Chrome ይሞክሩ

አሁንም ካልተከፈተ እባክዎ የሚከተሉትን ይላኩልኝ፦
- በስክሪኑ ላይ የሚያዩትን የስክሪን ፎቶ (screenshot)
- የስልክዎን ዓይነት እና የሚጠቀሙበትን ብሮውዘር
- Wi-Fi ወይስ ሞባይል ዳታ እየተጠቀሙ እንደሆነ

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ችግሩን እስክናገኝ ድረስ አብሬዎት እሆናለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about this! Please check: the address is byfluence.com, other sites open, your phone's date/time is correct, then switch Wi-Fi/mobile data and reload. Still not working? Send a screenshot + your phone and browser name. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለችግሩ ይቅርታ! እባክዎ አድራሻው byfluence.com መሆኑን፣ ሌሎች ድረ-ገጾች እንደሚከፈቱ እና የስልክዎ ቀንና ሰዓት ትክክል መሆኑን ያረጋግጡ፤ ከዚያ Wi-Fi/ሞባይል ዳታ ቀይረው ገጹን እንደገና ይክፈቱ። ካልሰራ የስክሪን ፎቶ እና የስልክዎን/ብሮውዘርዎን ስም ይላኩልኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our technical team is still checking why byfluence.com is not opening for you. We have your device and network details, so you don't need to send them again. We will contact you again by {{follow_up_time}}. If you have an upcoming consultation, reply here and we will help you with your booking details in the meantime.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። byfluence.com ለምን እንደማይከፈትልዎ የቴክኒክ ቡድናችን አሁንም እያጣራ ነው። የስልክዎ እና የኔትወርክዎ መረጃ ደርሶናል፤ እንደገና መላክ አያስፈልግዎትም። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። በቅርቡ ምክክር ካለዎት እዚሁ ይጻፉልን፤ እስከዚያው የቀጠሮዎን መረጃ እንዲያገኙ እንረዳዎታለን።

## Escalation Conditions
- The site does not load for you either, or several customers report it at the same time → **Technical / Engineering**, priority **Critical**, and notify your supervisor immediately.
- The site loads for you but not for the customer after all basic checks, and other websites work for them → **Technical / Engineering**, priority Medium (High if they have a consultation or payment in progress).
- The customer reached a look-alike site or was asked for their password/payment details on another domain → **Trust & Safety**, priority High.
- A consultation starts soon and the customer cannot access booking details → **Senior Support / Supervisor** to help with the session while Technical investigates.

## Resolution Procedure
1. Ask the customer to open byfluence.com and log in while you are still in the conversation.
2. Confirm they can see what they came for (dashboard, booking, listing, payment page).
3. Record the root cause in the ticket (e.g., "phone date wrong", "data finished", "Opera Mini Extreme mode", "platform outage — incident #…").
4. If it was an outage, link the ticket to the incident and send the resolution message (tpl-bug-fixed) when Technical confirms the fix.

## Internal Notes
- The most common real causes in Ethiopia: data package finished, weak mobile signal, wrong phone date/time, and Opera Mini Extreme mode. Check these before escalating.
- Customers often say "the site is down" when only their connection is down. Always test the site yourself first.
- A sudden wave of "site not loading" tickets is an incident signal. Do not escalate each ticket separately — tell the supervisor, who will open one incident.
- Links shared in Telegram groups may point to fake domains. Always ask for the exact link.
- Never ask the customer to install third-party "VPN" or "booster" apps to reach Byfluence.

<!-- doc -->
# Website Is Slow
id: tec-slow-website
type: article
category: technical
subcategory: site-access
audience: both
priority: medium
department: technical
tags: slow website, site is slow, pages take long, loading forever, lagging, spinning, ድረ-ገጹ ቀርፋፋ ነው, ገጹ ይዘገያል, በዝግታ ይከፈታል
related: tec-site-not-loading, tec-poor-connectivity, tec-mobile-browser-problems, tec-clear-cache-cookies, tec-known-outage-handling
templates: tpl-technical-investigation, tpl-browser-troubleshooting, tpl-known-outage
policy_pending: no

## Summary
Byfluence opens but pages, images or actions (search, booking, payment) take a long time to load or freeze part-way.

## Issue Description
The customer can reach the site but it feels very slow: pages load partly, images appear late, buttons react after a long delay, or the page keeps spinning. Slowness during **payment** or **booking** is the most important case, because customers may tap "Pay" again and risk paying twice, or lose a time slot.

## Possible Causes
- Weak or congested mobile network, or nearly-finished data package (operators may slow speed).
- Many apps downloading in the background (app updates, Telegram media auto-download, video).
- Old phone with little free storage or memory; too many open browser tabs.
- Data-saver modes (Opera Mini Extreme, Chrome Lite mode) that change how pages load.
- A large page (many listing images) on a slow connection.
- Platform-side slowness: high traffic, a slow server, a slow payment provider or a partial incident.

## Information to Collect
- Which pages or actions are slow (whole site, search, dashboard, booking, payment page)
- Device and browser
- Network type (Wi-Fi / mobile data and operator) and their location (city/area)
- Approximate time it started, and whether it is constant or on and off
- Whether other websites are also slow for them
- Whether they were in the middle of a payment or booking

## Troubleshooting Steps
1. Check **Announcements** for a known slowdown. If listed, use tpl-known-outage and link the ticket to the incident.
2. Test the same page yourself. If it is slow for you too, note the page and time and inform your supervisor; several reports = possible incident.
3. If they were **paying**: tell them not to tap Pay again. Check the transaction/booking status through authorized tools before any retry (see tec-payment-gateway-error).
4. If only they are affected, go through the connection checks in tec-poor-connectivity: signal strength, data balance, background downloads, switch network.
5. Ask them to close other tabs and apps, then reload the page.
6. Run basic browser checks (tec-tsg-browser-basics): update browser, try another browser, clear cache for the site.
7. For older phones: suggest restarting the phone and freeing some storage.
8. If it remains slow for them only and their other sites are fast, collect details and escalate to Technical with tpl-technical-investigation.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know, and I'm sorry the website is slow for you.

Please try the following:
1. Close other apps and browser tabs, then reload the page
2. Check your internet signal and data balance, or switch between Wi-Fi and mobile data
3. Pause downloads or video running in the background
4. Try again in Chrome or another updated browser

Important: if you were making a payment, please do not tap "Pay" again. Tell me first and I will check whether your payment went through.

If it is still slow, please tell me which page is slow, your phone model, browser and whether you use Wi-Fi or mobile data. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን፤ ድረ-ገጹ ስለዘገየብዎ ይቅርታ እንጠይቃለን።

እባክዎ የሚከተሉትን ይሞክሩ፦
1. ሌሎች መተግበሪያዎችን (apps) እና የብሮውዘር ታቦችን ዘግተው ገጹን እንደገና ይክፈቱ
2. የኢንተርኔት ኔትወርክዎን እና የዳታ ቀሪ ሂሳብዎን ያረጋግጡ፤ ወይም ከWi-Fi ወደ ሞባይል ዳታ ይቀይሩ
3. ከጀርባ እየወረዱ ያሉ ፋይሎችን ወይም ቪዲዮዎችን ያቁሙ
4. በChrome ወይም በሌላ የዘመነ ብሮውዘር እንደገና ይሞክሩ

ማሳሰቢያ፦ ክፍያ እየፈጸሙ ከነበረ እባክዎ "Pay" የሚለውን ቁልፍ እንደገና አይጫኑ። መጀመሪያ ይንገሩኝ፤ ክፍያዎ መፈጸሙን አጣራለሁ።

አሁንም ቀርፋፋ ከሆነ የትኛው ገጽ እንደሚዘገይ፣ የስልክዎን ዓይነት፣ ብሮውዘሩን እና Wi-Fi ወይስ ሞባይል ዳታ እንደሚጠቀሙ ይንገሩኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry it's slow! Please close other apps/tabs, check your signal or switch Wi-Fi/data, and reload. If you were paying, don't tap Pay again — tell me and I'll check. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለመዘግየቱ ይቅርታ! እባክዎ ሌሎች apps/ታቦችን ይዝጉ፣ ኔትወርክዎን ያረጋግጡ ወይም Wi-Fi/ዳታ ይቀይሩ፣ ከዚያ ገጹን እንደገና ይክፈቱ። ክፍያ እየፈጸሙ ከነበረ "Pay" እንደገና አይጫኑ — ይንገሩኝ፣ አጣራለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is looking into the slowness you reported. Is the website still slow for you now? If yes, please tell me which page and the time you last tried. We will update you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ ያሳወቁትን የድረ-ገጹን መዘግየት የቴክኒክ ቡድናችን እያጣራ ነው። አሁንም ድረ-ገጹ ቀርፋፋ ነው? ከሆነ የትኛው ገጽ እንደሆነ እና ለመጨረሻ ጊዜ የሞከሩበትን ሰዓት ይንገሩኝ። እስከ {{follow_up_time}} ድረስ በድጋሚ መረጃ እንሰጥዎታለን።

## Escalation Conditions
- The site is slow for you as well, or several customers report slowness → **Technical / Engineering**, priority High; notify supervisor.
- Slowness on the payment page caused a possible double payment or a payment with no booking → **Payments & Finance**, priority High.
- One customer is consistently slow on Byfluence only, after all checks → **Technical / Engineering**, priority Low/Medium.

## Resolution Procedure
1. Confirm with the customer that pages now load at a normal speed, or that their pending action (booking/payment) is complete.
2. Record the cause (customer network, device, browser mode, platform incident).
3. If a payment was involved, confirm the final payment and booking status before closing.

## Internal Notes
- "Slow" complaints peak in the evening when mobile networks are busy. Check the time pattern before escalating.
- The biggest risk is double payment. Always ask "were you paying?" early.
- A slow site for many users is often the first sign of an outage — report early rather than late.

<!-- doc -->
# Handling Contacts During a Known Outage
id: tec-known-outage-handling
type: article
category: technical
subcategory: site-access
audience: internal
priority: critical
department: technical
tags: outage, incident, site down for everyone, mass incident, many tickets same problem, system down, maintenance, announcement, ሲስተሙ ተቋርጧል, የአገልግሎት መቋረጥ
related: tec-site-not-loading, tec-reporting-a-bug, tec-tsg-technical-master, tec-booking-system-error, tec-payment-gateway-error
templates: tpl-known-outage, tpl-bug-fixed, tpl-greeting-telegram
policy_pending: yes

## Summary
How agents handle the flood of contacts when Byfluence (or one part of it, such as payments or booking) has a confirmed, system-wide problem that is already posted in Announcements.

## Overview
A **known outage** is an incident that Technical or a supervisor has confirmed and posted in the support app's **Announcements**. During an outage many customers contact us about the same thing. The goal is to: answer quickly and consistently, avoid duplicate escalations, protect customers with time-sensitive bookings or payments, and close the loop when the fix is released.

**Agent workflow:**

### 1. Before replying — confirm the incident
1. Open **Announcements** and read the incident post: what is affected (whole site, login, payments, booking, notifications, Google Meet links), since when, and the approved customer wording.
2. Confirm the customer's problem matches the incident. If it does not match (different symptom, different feature), handle it as a normal ticket.
3. If you are seeing many similar reports and **no announcement exists**, tell your supervisor immediately — do not wait. The supervisor decides whether to declare an incident.

### 2. Reply using the approved message
1. Use **tpl-known-outage** (EN + AM). Do not write your own explanation of the cause.
2. Do not promise a fix time unless Announcements gives an approved one; use `{{estimated_resolution_time}}` only with the approved wording.
3. Do not ask the customer to clear cache, reinstall or change settings for a confirmed server-side problem — it wastes their time and data.

### 3. Log the ticket correctly
1. Create or update a ticket for each customer who contacted us (we must be able to notify them later).
2. **Link the ticket to the incident** (incident ID / parent ticket from Announcements) and add the incident tag.
3. Do **not** escalate each ticket separately to Technical. Only add new information to the incident (a new symptom, a new error message, a new affected area).

### 4. Prioritise time-sensitive customers
Raise these to **High/Critical** and inform the supervisor:
- A consultation (one-on-one or group) that starts during or shortly after the outage — the buyer or seller may not reach booking details or Meet links.
- A payment that may have been deducted while the site failed (risk of paid-but-not-confirmed or double payment) → also follow pay-paid-booking-not-confirmed logic with Payments.
- A seller withdrawal in progress.
For consultations, record buyer, seller, booking ID and time so Senior Support can decide on rescheduling after the outage.

### 5. When the fix is released
1. Wait until Technical/supervisor marks the incident resolved in Announcements.
2. Send **tpl-bug-fixed** to every linked customer, asking them to try again.
3. For customers with affected bookings or payments, check their records individually before closing.
4. Close tickets only after the customer confirms or after the standard no-reply period set by your team.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry for the inconvenience. We are aware of a technical problem currently affecting part of the Byfluence website, and our technical team is working on it.

You don't need to do anything on your phone or computer — the issue is on our side. Your case number is {{ticket_id}}, and we will message you here as soon as it is fixed.

If you have a consultation booked soon or you were making a payment when the problem happened, please tell me the details so we can give your case priority.

Thank you for your patience.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ ለተፈጠረው መጉላላት ይቅርታ እንጠይቃለን። በአሁኑ ሰዓት የByfluence ድረ-ገጽን በከፊል የሚያውክ የቴክኒክ ችግር እንዳለ እናውቃለን፤ የቴክኒክ ቡድናችንም እየሰራበት ነው።

በስልክዎ ወይም በኮምፒውተርዎ ላይ ምንም ማድረግ አያስፈልግዎትም — ችግሩ በእኛ በኩል ነው። የጉዳይዎ ቁጥር {{ticket_id}} ነው፤ ችግሩ እንደተስተካከለ እዚሁ መልዕክት እንልክልዎታለን።

በቅርቡ የተያዘ ምክክር ካለዎት ወይም ችግሩ ሲፈጠር ክፍያ እየፈጸሙ ከነበረ፣ ጉዳይዎን በቅድሚያ እንድናይ እባክዎ ዝርዝሩን ይንገሩኝ።

ስለ ትዕግስትዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry for the trouble! We know about a technical issue on our side and our team is fixing it — no need to change anything on your phone. We'll message you when it's fixed. Booked session or payment in progress? Tell me. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለችግሩ ይቅርታ! በእኛ በኩል የቴክኒክ ችግር እንዳለ እናውቃለን፤ ቡድናችን እያስተካከለው ነው — በስልክዎ ላይ ምንም መቀየር አያስፈልግዎትም። ሲስተካከል መልዕክት እንልክልዎታለን። የተያዘ ምክክር ወይም በሂደት ላይ ያለ ክፍያ ካለ ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, an update on case {{ticket_id}}: our technical team is still working on the problem affecting the website. We have not forgotten your request and will message you as soon as it is fixed. Our next update will be by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} መረጃ፦ የቴክኒክ ቡድናችን ድረ-ገጹን እያወከ ያለውን ችግር አሁንም እየፈታ ነው። ጥያቄዎን አልረሳነውም፤ እንደተስተካከለ ወዲያውኑ እናሳውቅዎታለን። ቀጣዩ መረጃ እስከ {{follow_up_time}} ይደርስዎታል። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Many similar contacts and **no** announcement → **Senior Support / Supervisor** immediately (they open the incident with Technical).
- A customer reports a **new symptom** not described in the announcement → add it to the incident for **Technical / Engineering**.
- Money deducted during the outage, or a possible double payment → **Payments & Finance**, priority High.
- A consultation could not happen because of the outage → **Senior Support / Supervisor** for the rescheduling/refund decision.
- Media, public social-media complaints going viral, or a security-related outage (data exposure) → **Management** and **Trust & Safety**.

## Resolution Procedure
1. Confirm in Announcements that the incident is resolved.
2. Send tpl-bug-fixed to each linked customer.
3. Check payments/bookings individually for customers flagged as time-sensitive.
4. Record "Resolved — linked to incident [ID]" plus any individual follow-up in each ticket.

## Policy Pending Approval
- Decide who is authorized to declare an incident and post it in Announcements (supervisor only, or Technical too).
- Decide whether and how customers are informed publicly (website banner, Telegram channel, social media) and who approves the wording.
- Decide the policy for consultations missed because of a platform outage (automatic reschedule, refund, or case-by-case) and for seller earnings in that case.
- Confirm whether a standard "no-reply" period applies before closing outage tickets.

## Internal Notes
- Consistency matters more than speed of writing: everyone uses the same approved message.
- Never guess the cause to customers ("the server crashed", "we were hacked"). Say "a technical problem on our side".
- Never say "it will be fixed in X minutes" unless Announcements says so.
- Keep a list of time-sensitive customers in the incident thread so Senior Support can act after recovery.

<!-- doc -->
# Slow or Unstable Internet Connection / Mobile Data Issues
id: tec-poor-connectivity
type: article
category: technical
subcategory: site-access
audience: both
priority: medium
department: support_l1
tags: no internet, weak signal, mobile data not working, data finished, network problem, connection drops, ኔትወርክ የለም, ዳታ አልቋል, ኢንተርኔት ይቆራረጣል, ኔትወርክ ደካማ ነው
related: tec-site-not-loading, tec-slow-website, tec-mobile-browser-problems, con-how-consultations-work, tec-payment-gateway-error
templates: tpl-browser-troubleshooting, tpl-technical-investigation
policy_pending: no

## Summary
The customer's own internet is weak, unstable or out of data, so Byfluence (and often other sites) loads badly, payments time out, or Google Meet sessions drop.

## Issue Description
Many Byfluence customers use Android phones on mobile data with limited data packages, and signal quality varies by area and time of day. A poor connection causes slow pages, half-loaded pages, failed uploads, payment timeouts and dropped consultation calls. The agent's job is to help the customer confirm it is a connection problem, give simple steps to improve it, and protect anything time-sensitive (payment, consultation).

## Possible Causes
- Data or airtime package finished or nearly finished.
- Weak signal (indoors, basement, rural area, moving vehicle).
- Network congestion at busy hours or local operator problems.
- Mobile data switched off, or the phone is set to 2G/3G only.
- Wi-Fi connected but the router has no internet (power cut, unpaid subscription).
- Background apps using the data (updates, Telegram/TikTok auto-download, backups).
- A regional internet disruption.

## Information to Collect
- Network type: Wi-Fi or mobile data, and which operator
- Their general location (city/area) — to spot regional problems
- Whether other websites/apps (Google, YouTube, Telegram) work normally
- What they were doing when it failed (browsing, paying, uploading, in a consultation)
- Device type

## Troubleshooting Steps
1. Ask whether other sites/apps work. If **nothing** works → it is their connection. If **only Byfluence** fails → follow tec-site-not-loading instead.
2. Guide the customer through simple checks (one at a time, in this order):
   1. Check the data balance with their mobile operator.
   2. Turn **airplane mode on, then off** (this reconnects to the network).
   3. Move closer to a window/outdoors or to a place with better signal.
   4. Switch between Wi-Fi and mobile data.
   5. In phone settings, make sure the network mode allows 4G/LTE (if their phone and SIM support it).
   6. Stop background downloads and set Telegram/other apps not to auto-download media.
   7. Restart the phone.
3. **If they were paying:** tell them not to retry the payment until you check. Verify the transaction/booking status through authorized tools (see tec-payment-gateway-error).
4. **If they are in or about to start a consultation:** suggest turning off video in Google Meet and using audio only, closing other apps, and staying in one place. If the session cannot continue, record times and follow the consultation attendance process (con-how-consultations-work).
5. **If several customers in the same area report it**, inform your supervisor — it may be a regional disruption; note it in Announcements if approved.
6. There is nothing Technical can fix on a customer's own network. Escalate only if the customer's other services work well and Byfluence alone fails.

## Customer Steps
1. Check that you still have data or airtime.
2. Turn airplane mode ON, wait a moment, then turn it OFF.
3. Move to a place with a stronger signal.
4. Try Wi-Fi instead of mobile data (or the opposite).
5. Close apps you are not using and stop downloads.
6. Restart your phone and open byfluence.com again.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. It sounds like your internet connection may be weak right now, which can make the website slow or stop it from loading.

Please try these steps:
1. Check that you still have data or airtime
2. Turn airplane mode on, wait a moment, then turn it off
3. Move to a place with better signal, or switch between Wi-Fi and mobile data
4. Close apps you are not using and stop any downloads
5. Restart your phone, then open byfluence.com again

If you were making a payment or have a consultation soon, please tell me — I will check your booking and payment status for you, so please do not pay again before we confirm.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በአሁኑ ሰዓት የኢንተርኔት ግንኙነትዎ ደካማ ሊሆን ይችላል፤ ይህ ደግሞ ድረ-ገጹ እንዲዘገይ ወይም እንዳይከፈት ያደርጋል።

እባክዎ እነዚህን ደረጃዎች ይሞክሩ፦
1. ዳታ ወይም የአየር ሰዓት (airtime) እንዳለዎት ያረጋግጡ
2. የአውሮፕላን ሁነታን (airplane mode) ያብሩ፣ ጥቂት ቆይተው ያጥፉት
3. ኔትወርክ ወደሚሻልበት ቦታ ይሂዱ፣ ወይም በWi-Fi እና በሞባይል ዳታ መካከል ይቀያይሩ
4. የማይጠቀሙባቸውን መተግበሪያዎች (apps) ይዝጉ፤ የሚወርዱ ነገሮችን ያቁሙ
5. ስልክዎን አጥፍተው ያብሩ፤ ከዚያ byfluence.com ን እንደገና ይክፈቱ

ክፍያ እየፈጸሙ ከነበረ ወይም በቅርቡ ምክክር ካለዎት እባክዎ ይንገሩኝ — የቀጠሮዎን እና የክፍያዎን ሁኔታ አጣራልዎታለሁ፤ ስለዚህ እስክናረጋግጥ ድረስ እንደገና አይክፈሉ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your connection may be weak. Please check your data balance, turn airplane mode on/off, move to better signal or switch Wi-Fi/data, then reload. If you were paying, don't pay again — I'll check first. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የኢንተርኔት ግንኙነትዎ ደካማ ሊሆን ይችላል። እባክዎ የዳታ ቀሪ ሂሳብዎን ያረጋግጡ፣ airplane mode አብርተው ያጥፉ፣ ኔትወርክ ወደሚሻልበት ቦታ ይሂዱ ወይም Wi-Fi/ዳታ ይቀይሩ፣ ከዚያ ገጹን እንደገና ይክፈቱ። ክፍያ እየፈጸሙ ከነበረ እንደገና አይክፈሉ — መጀመሪያ አጣራለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, checking in on case {{ticket_id}}. Were you able to open Byfluence after trying the connection steps? If it is still not working while other apps work fine, please send me a screenshot and your phone and browser name, and we will look into it further.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} እየጠየቅኩዎት ነው። የኔትወርክ ደረጃዎቹን ከሞከሩ በኋላ Byfluenceን መክፈት ችለዋል? ሌሎች መተግበሪያዎች በደንብ እየሰሩ Byfluence ብቻ የማይሰራ ከሆነ፣ እባክዎ የስክሪን ፎቶ እና የስልክዎን እና የብሮውዘርዎን ስም ይላኩልኝ፤ የበለጠ እናጣራለን።

## Escalation Conditions
- Other services work but Byfluence alone fails → handle as tec-site-not-loading; **Technical / Engineering** if unresolved.
- A payment may have gone through during the connection drop → **Payments & Finance** if the status is unclear in your tools.
- A consultation was interrupted by connection loss and a reschedule/refund is requested → **Senior Support / Supervisor**.
- Many customers from one region report connection problems → inform **Senior Support / Supervisor** (possible regional disruption).

## Resolution Procedure
1. Confirm the customer can load Byfluence and complete what they needed.
2. If a payment or booking was involved, confirm its final status.
3. Record "customer connectivity" as the root cause, with network type and area.

## Internal Notes
- Be patient and give one step at a time. Many customers are not comfortable with phone settings; a short voice note or simple words help.
- Do not tell customers to buy more data or switch operators — just suggest checking their balance.
- Never ask the customer to send you their airtime/mobile-money PIN or a code received by SMS.
- Internet disruptions in some regions can last a long time; do not promise when service will return.

<!-- doc -->
# How to Report a Bug to the Technical Team
id: tec-reporting-a-bug
type: article
category: technical
subcategory: functionality
audience: internal
priority: medium
department: technical
tags: report bug, escalate to engineering, bug report, technical escalation, steps to reproduce, engineering ticket, ስህተት ሪፖርት, ለቴክኒክ ቡድን ማሳወቅ
related: tec-tsg-technical-master, tec-known-outage-handling, tec-unexpected-error-message, tec-tsg-browser-basics, gen-report-a-problem
templates: tpl-technical-investigation, tpl-request-screenshot, tpl-bug-fixed
policy_pending: yes

## Summary
The standard way support agents write a bug report for Technical / Engineering so it can be reproduced and fixed without going back to the customer for more details.

## Overview
A good bug report saves days. Engineers cannot fix what they cannot reproduce, and every round of "please ask the customer again" costs the customer time and trust. Before you escalate:

1. **Check Announcements** — if it is a known incident, link the ticket to it instead of reporting again.
2. **Search existing tickets** for the same symptom. If a bug report exists, add your ticket and any new details to it (more affected users = higher priority).
3. **Do the basic checks** (tec-tsg-browser-basics) so the report is not just a cache or connection issue.
4. **Try to reproduce it yourself** with a test or your own account (never log in as the customer and never ask for their password).

### What every bug report must include

| Field | What to write | Example |
|---|---|---|
| Title | Area + what fails, short | "Booking: 'Confirm' button does nothing on Android Chrome" |
| Ticket IDs | All linked customer tickets | #1042, #1047 |
| User type | Buyer / seller / both; account email or ID (internal) | Buyer, user ID … |
| Page / URL | The exact page address | byfluence.com/... |
| Steps to reproduce | Numbered, exactly what the user did | 1. Open listing 2. Choose date 3. Tap Confirm |
| Expected result | What should happen | Moves to payment page |
| Actual result | What happened instead | Nothing happens; button greys out |
| Error message | Copy word for word, including any code | "Something went wrong (500)" |
| Time | Date + time it happened, with time zone (EAT) | 18 Nov, 14:20 EAT |
| Device / OS | Phone model and Android/iOS version, or computer OS | Tecno Spark, Android 12 |
| Browser | Name + version, and mode (Opera Mini Extreme, in-app Telegram browser) | Chrome 1xx |
| Network | Wi-Fi / mobile data + operator | Mobile data |
| Frequency | Always / sometimes / once; how many users | Always; 3 users today |
| Reproduced by agent? | Yes/No and on what device | Yes, on desktop Chrome |
| Workaround | Anything that helps users meanwhile | Works on desktop |
| Evidence | Screenshots, screen recording, references | Attached |
| Business impact | Money, bookings, sellers blocked? | Buyers cannot pay for sessions |

### Suggested severity (until an official definition is approved)
- **Critical** — site/login/payment/booking down for many users; money taken without a record; security or data exposure.
- **High** — a core flow fails for some users (booking, payment, withdrawal, Meet link), or one user with an urgent session/payment and no workaround.
- **Medium** — a feature fails but a workaround exists, or display problems on a common device.
- **Low** — cosmetic issues, typos, rare devices, with no effect on money or bookings.

### Evidence handling
- Ask customers for screenshots or a short screen recording with tpl-request-screenshot. Ask them to **crop or cover** any personal data, and never to show passwords, OTP codes, PINs or card numbers.
- If a screenshot shows sensitive data, do not forward it in group chats; attach it only to the ticket.
- Never share internal links, admin screenshots or other customers' data with the customer.

### After reporting
1. Tell the customer it has been passed to the technical team (tpl-technical-investigation), with no fix-time promise.
2. Keep the ticket open and linked to the bug.
3. When Technical confirms the fix, send tpl-bug-fixed and ask the customer to confirm.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for the details and the screenshots — they are very helpful. I have passed your report to our technical team with everything you sent, so you don't need to explain it again.

Your case number is {{ticket_id}}. We will message you as soon as we have an update. If the problem changes or you see a new error message, just reply here with a screenshot.

Thank you for helping us improve Byfluence.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለላኩልን ዝርዝር መረጃ እና የስክሪን ፎቶዎች እናመሰግናለን — በጣም ጠቃሚ ናቸው። ሪፖርትዎን ከላኩልን መረጃ ሁሉ ጋር ለቴክኒክ ቡድናችን አስተላልፌዋለሁ፤ ስለዚህ እንደገና ማስረዳት አያስፈልግዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። አዲስ መረጃ እንዳገኘን መልዕክት እንልክልዎታለን። ችግሩ ከተቀየረ ወይም አዲስ የስህተት መልዕክት ካዩ፣ እዚሁ የስክሪን ፎቶ ይላኩልን።

Byfluenceን ለማሻሻል ስለረዱን እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Thanks {{customer_name}}! I've sent your report and screenshots to our technical team — no need to repeat anything. We'll update you here. Case: {{ticket_id}}

## Short Response (AM)
እናመሰግናለን {{customer_name}}! ሪፖርትዎን እና የስክሪን ፎቶዎቹን ለቴክኒክ ቡድናችን ልኬያለሁ — ምንም መድገም አያስፈልግዎትም። እዚሁ መረጃ እንሰጥዎታለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Anything involving money (payment taken but not recorded, wrong amounts, withdrawals) → **Technical / Engineering** and **Payments & Finance** together.
- Anything suggesting a security problem (seeing another user's data, unexpected logins, data exposure) → **Trust & Safety** and **Technical**, priority Critical; notify supervisor.
- Many users affected → supervisor, so it becomes an incident (tec-known-outage-handling).
- No response from Technical on a High/Critical report within your team's agreed time → **Senior Support / Supervisor**.

## Policy Pending Approval
- Approve the official bug severity levels and the expected response time per level for Technical.
- Confirm the tool/channel used to file bug reports (support app escalation, issue tracker, dedicated Telegram group) and who has access.
- Confirm whether agents may use test accounts to reproduce buyer/seller flows, including payment flows.

## Internal Notes
- "It doesn't work" is not a bug report. Steps to reproduce + exact error + device/browser are the minimum.
- One clear report with five linked tickets beats five separate reports.
- Always write the time with the time zone (EAT) — engineers search logs by time.
- Do not guess at technical causes in the report; describe what you saw.

<!-- doc -->
# Master Guide: Technical Troubleshooting (Symptom → Steps)
id: tec-tsg-technical-master
type: troubleshooting
category: technical
subcategory: functionality
audience: internal
priority: medium
department: technical
tags: technical troubleshooting, master guide, website problem, technical issue, error, not working, diagnose, ቴክኒካዊ ችግር, አይሰራም
related: tec-tsg-browser-basics, tec-reporting-a-bug, tec-known-outage-handling, tec-site-not-loading, tec-unexpected-error-message, tec-payment-gateway-error
templates: tpl-technical-investigation, tpl-browser-troubleshooting, tpl-request-screenshot, tpl-known-outage
policy_pending: no

## Summary
A single decision guide for any "it's not working" contact: identify the symptom, rule out known outages and customer-side causes, then route to the right article or escalation.

## Overview
Use this guide when the customer describes a technical problem and you are not sure which article applies. Work top to bottom. Most technical contacts are solved at steps 1–3 without escalation.

## Troubleshooting Steps

### Step 1 — Is there a known incident?
1. Check **Announcements**.
2. Matches the customer's symptom → follow **tec-known-outage-handling** (use tpl-known-outage). Stop here.
3. You are seeing several similar reports with no announcement → tell your supervisor now.

### Step 2 — Is anything urgent or financial?
Ask early: *"Were you making a payment, or do you have a consultation soon?"*
- Payment in progress / money deducted → do **not** let the customer pay again; check status via authorized tools; follow **tec-payment-gateway-error** (and Payments articles).
- Consultation starting soon → find the booking and meeting details in your tools and help with the session first; investigate the technical issue afterwards.
- Possible account compromise or phishing → **acc-security-concern-phishing** / Trust & Safety.

### Step 3 — Collect the basics (once, in one message)
- Device and OS (Android/iPhone/computer), browser (and whether it's inside Telegram/Facebook)
- Network (Wi-Fi / mobile data)
- Exact error text, time, page
- Screenshot or screen recording (tpl-request-screenshot)

### Step 4 — Match the symptom

| Symptom | Go to |
|---|---|
| Site doesn't open at all | tec-site-not-loading |
| Site opens but very slowly | tec-slow-website |
| Other sites also fail / weak data | tec-poor-connectivity |
| Page looks broken, images/text missing | tec-broken-page |
| Buttons or links do nothing | tec-buttons-not-working |
| An error message appears | tec-unexpected-error-message |
| Dashboard won't load / blank / spinning | tec-dashboard-loading-error |
| Error while booking a consultation | tec-booking-system-error |
| Payment page error / gateway won't open | tec-payment-gateway-error |
| Photo/document upload fails | tec-upload-failures |
| No emails from Byfluence | tec-email-notifications-not-received |
| No SMS / code by SMS | tec-sms-not-received |
| Problems only on phone | tec-mobile-browser-problems |
| "Session expired" / logged out | tec-session-expired |
| Amharic shows as boxes / can't type Amharic | tec-language-display-amharic |
| Dates or times look wrong | tec-calendar-time-display |

### Step 5 — Basic checks
Run **tec-tsg-browser-basics** with the customer (reload → private tab → other browser → update → clear site data → other network). Use tpl-browser-troubleshooting for the customer message. Give steps **one or two at a time** for customers who are not comfortable with phone settings.

### Step 6 — Reproduce
- Try the same action yourself on a similar device/browser where possible.
- Reproduced → strong bug report; escalate.
- Not reproduced and the basics fixed it → resolve and record the cause.
- Not reproduced and the basics did not fix it → escalate with full device/browser/network details.

### Step 7 — Escalate correctly
Follow **tec-reporting-a-bug**. Send the customer tpl-technical-investigation. Never promise a fix date.

### Step 8 — Close the loop
When Technical confirms a fix, send tpl-bug-fixed, ask the customer to try again, and confirm before resolving. Record the root cause category: *customer network*, *device/browser*, *user error/guidance*, *platform bug*, *platform outage*, *third-party (payment provider, email/SMS provider, Google Meet)*.

## Escalation Conditions
- Platform-side bug confirmed or likely → **Technical / Engineering** (via tec-reporting-a-bug).
- Money involved → **Payments & Finance** as well.
- Security or data exposure → **Trust & Safety**, priority Critical.
- Customer is repeatedly contacting about an unresolved technical issue, or is very upset → **Senior Support / Supervisor**.

## Internal Notes
- The two most expensive mistakes: (1) letting a customer pay twice while "the page is stuck", (2) escalating 20 separate tickets during one outage.
- Keep your own language simple: "tap", "the three dots at the top", "the lock icon next to the address".
- Record the root cause on every ticket — it shows management where the product needs work.

<!-- doc -->
# Basic Browser & Device Checks Before Escalating
id: tec-tsg-browser-basics
type: troubleshooting
category: technical
subcategory: browser-device
audience: internal
priority: low
department: support_l1
tags: basic troubleshooting, browser checks, refresh, incognito, update browser, try another browser, restart phone, መሰረታዊ ማጣሪያ, ብሮውዘር
related: tec-tsg-technical-master, tec-clear-cache-cookies, tec-mobile-browser-problems, tec-reporting-a-bug, tec-poor-connectivity
templates: tpl-browser-troubleshooting, tpl-request-screenshot
policy_pending: no

## Summary
The short standard checklist agents run with the customer before escalating any technical problem to Technical / Engineering.

## Overview
These checks solve a large share of "it's not working" cases and, when they don't, they give Technical the information they need. Go in order, stop when the problem is solved, and record which step fixed it. Ask for one or two actions per message so the customer is not overwhelmed, especially on Telegram and with customers who are new to smartphones.

## Troubleshooting Steps

### 1. Reload the page
- Phone: pull the page down, or tap the circular arrow ⟳ in the browser.
- Computer: press F5 (or Ctrl+R; Cmd+R on Mac).

### 2. Check the address and the app they are in
- The address must be **byfluence.com**.
- If the customer opened the link inside **Telegram, Facebook, Instagram or TikTok**, ask them to tap ⋮ / … and choose *Open in browser* (or *Open in Chrome*). In-app browsers often break login, payment redirects and uploads.

### 3. Check the internet
Does Google open? If not → tec-poor-connectivity.

### 4. Check date and time
Phone **Settings → Date & time → turn on automatic date & time** (or "Set automatically" on iPhone). A wrong date breaks secure pages and logins.

### 5. Try a private (incognito) tab
- Chrome: ⋮ → *New Incognito tab*. Safari: tabs button → *Private*.
- Works in private but not normally → old cache/cookies or an extension → step 7.

### 6. Try another browser
On Android, Google **Chrome** is the safest option; on iPhone, **Safari**. If they use **Opera Mini**, ask them to switch off *Extreme* data saving or try Chrome.

### 7. Clear cache and cookies for Byfluence
Follow **tec-clear-cache-cookies** (site-only clearing first, so they are not logged out everywhere). Make sure they know their login details before clearing.

### 8. Update the browser and phone
Open Play Store / App Store → search the browser → *Update*. Very old Android versions may not open modern secure websites at all; note the Android version in the ticket.

### 9. Turn off extras
VPN apps, ad blockers, "data booster" apps, the browser's automatic **translate** feature (Google Translate can break buttons), and battery/data saver modes.

### 10. Restart the device
Restart the phone or computer and try once more.

### 11. Try another device or network
If possible, the same action on another phone, a computer, or another network. Works elsewhere → device/browser-specific; record it for Technical.

### Record before escalating
- [ ] Device + OS version
- [ ] Browser + version / mode (in-app, Opera Mini mode)
- [ ] Network type
- [ ] Exact error text + time (EAT)
- [ ] Which steps were tried and the result of each
- [ ] Screenshot / screen recording

## Escalation Conditions
- All applicable steps tried and the problem remains → **Technical / Engineering** via tec-reporting-a-bug.
- A step reveals a security concern (unknown site, unexpected login prompt, account changed) → **Trust & Safety**.
- The customer cannot follow the steps and has an urgent booking or payment → **Senior Support / Supervisor** to assist directly (e.g., by phone if available).

## Internal Notes
- Don't make the customer repeat steps they already did — read the ticket history first.
- Clearing all browsing data logs customers out of every site (Telegram Web, email, banking). Always prefer clearing for byfluence.com only.
- Never ask the customer to share their screen in a way that would reveal passwords or codes, and never ask for those details.
