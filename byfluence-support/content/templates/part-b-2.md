<!-- template -->
# Technical issue under investigation
id: tpl-technical-investigation
category: technical
channel: any
style: standard
tags: technical issue, bug, error, page not working, investigating, ቴክኒካዊ ችግር, ስህተት
related: tec-tsg-browser-basics, tec-known-outage-handling

## Message (EN)
Hello {{customer_name}},

Thank you for reporting this issue and for the details you shared — they really help.

I have passed your report to our technical team, and they are now investigating it. Your case number is {{ticket_id}}.

If you notice anything new in the meantime — for example, an error message, a screenshot, or the exact time the problem happened — please send it here. It helps to know which device and browser or app you are using.

We will update you by {{follow_up_time}}. Thank you for your patience.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ይህንን ችግር ስላሳወቁን እና ስላጋሩን ዝርዝር መረጃ እናመሰግናለን — በጣም ይረዳናል።

ሪፖርትዎን ለቴክኒክ ቡድናችን አስተላልፌያለሁ፤ ቡድኑ አሁን ጉዳዩን እያጣራ ነው። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

እስከዚያው ድረስ አዲስ ነገር ካስተዋሉ — ለምሳሌ የስህተት መልዕክት፣ ስክሪንሾት ወይም ችግሩ የተፈጠረበትን ትክክለኛ ሰዓት — እባክዎ እዚሁ ይላኩልን። የሚጠቀሙበትን መሣሪያ (ስልክ ወይም ኮምፒውተር) እና ብራውዘር ወይም መተግበሪያ ብናውቅም ይረዳናል።

እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** You have done the basic checks (see *tpl-browser-troubleshooting*), the problem is still there, and you have escalated it to Technical / Engineering.

**Fill in:** `{{ticket_id}}`, `{{follow_up_time}}`. If you already have device/browser details, remove that sentence.

**Do NOT promise:** a fix time, that "it will work again today", or compensation. If the issue blocked a payment or a session, tell the customer which separate team is checking that (payments, booking) rather than implying Technical will refund anything. If many customers report the same problem, switch to *tpl-known-outage*.

<!-- template -->
# Basic browser troubleshooting steps
id: tpl-browser-troubleshooting
category: technical
channel: any
style: detailed
tags: browser troubleshooting, clear cache, page not loading, site not working, incognito, ብራውዘር, ገጹ አይከፈትም
related: tec-tsg-browser-basics, tec-known-outage-handling

## Message (EN)
Hello {{customer_name}},

I am sorry the page is not working properly for you. Many problems like this can be solved with a few quick steps. Please try them in this order and tell me after which step it starts working (if it does):

1. **Check your internet connection.** Open another website. If you are on mobile data, try Wi-Fi (or the other way around).
2. **Refresh the page.** On a computer, press Ctrl + F5 (Windows) or Cmd + Shift + R (Mac). On a phone, pull the page down or tap the reload icon.
3. **Open a private window.** Use an Incognito/Private window in your browser and log in to Byfluence again.
4. **Clear your browser's cache and cookies.** In your browser settings, open "Privacy" or "History", then clear cached images/files and cookies. You will need to log in again afterwards.
5. **Update your browser** to the latest version, or try a different browser (for example, Chrome, Firefox, Safari or Edge).
6. **Turn off browser extensions** such as ad blockers or VPNs for a moment, then try again.
7. **Check your device's date and time.** Make sure they are set automatically — a wrong date or time can stop pages and meeting links from working.
8. **Restart your device** and try once more.

If the problem continues, please send me:
- A screenshot of the problem or the exact error message
- The device you are using (phone or computer, and its model if possible)
- The browser or app and its version, if you know it
- The time the problem happened

Please do not share your password or any verification code in screenshots — we will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ገጹ በትክክል ስላልሠራልዎ ይቅርታ እንጠይቃለን። እንዲህ ዓይነቱ ብዙ ችግር በጥቂት ቀላል እርምጃዎች ሊፈታ ይችላል። እባክዎ የሚከተሉትን በቅደም ተከተል ይሞክሩ፤ ከየትኛው እርምጃ በኋላ መሥራት እንደጀመረም ይንገሩኝ፦

1. **የኢንተርኔት ግንኙነትዎን ያረጋግጡ።** ሌላ ድረ-ገጽ ይክፈቱ። የሞባይል ዳታ እየተጠቀሙ ከሆነ Wi-Fi ይሞክሩ (ወይም በተቃራኒው)።
2. **ገጹን እንደገና ይጫኑ (Refresh)።** በኮምፒውተር ላይ Ctrl + F5 (Windows) ወይም Cmd + Shift + R (Mac) ይጫኑ። በስልክ ላይ ገጹን ወደ ታች ይጎትቱ ወይም የመጫኛ (reload) ምልክቱን ይንኩ።
3. **የግል መስኮት ይክፈቱ።** በብራውዘርዎ ውስጥ Incognito/Private መስኮት ከፍተው ወደ Byfluence እንደገና ይግቡ።
4. **የብራውዘርዎን ካሽ (cache) እና ኩኪዎች (cookies) ያጽዱ።** በብራውዘርዎ ቅንብሮች (Settings) ውስጥ "Privacy" ወይም "History" የሚለውን ከፍተው የተቀመጡ ምስሎችን/ፋይሎችን እና ኩኪዎችን ያጽዱ። ከዚያ በኋላ እንደገና መግባት ያስፈልግዎታል።
5. **ብራውዘርዎን ወደ አዲሱ ስሪት ያዘምኑ** ወይም ሌላ ብራውዘር ይሞክሩ (ለምሳሌ Chrome፣ Firefox፣ Safari ወይም Edge)።
6. **የብራውዘር ተጨማሪዎችን (extensions)** ለምሳሌ ማስታወቂያ አጋጆችን ወይም VPNን ለጊዜው አጥፍተው እንደገና ይሞክሩ።
7. **የመሣሪያዎን ቀን እና ሰዓት ያረጋግጡ።** በራስ-ሰር (automatic) መቀመጡን ያረጋግጡ — የተሳሳተ ቀን ወይም ሰዓት ገጾች እና የስብሰባ ሊንኮች እንዳይሠሩ ሊያደርግ ይችላል።
8. **መሣሪያዎን አጥፍተው እንደገና ያብሩ** እና አንድ ጊዜ ደግመው ይሞክሩ።

ችግሩ ከቀጠለ እባክዎ የሚከተሉትን ይላኩልኝ፦
- የችግሩን ስክሪንሾት ወይም ትክክለኛውን የስህተት መልዕክት
- የሚጠቀሙበትን መሣሪያ (ስልክ ወይም ኮምፒውተር፣ ከተቻለም ሞዴሉን)
- የሚጠቀሙበትን ብራውዘር ወይም መተግበሪያ እና ስሪቱን፣ የሚያውቁት ከሆነ
- ችግሩ የተፈጠረበትን ሰዓት

እባክዎ በስክሪንሾቶቹ ላይ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A customer reports pages not loading, buttons not responding, a blank screen, a login page looping, or a payment/booking page freezing — and there is **no known outage** on the Announcements page.

**Adapt it:** For low digital-literacy customers or Telegram, send only steps 1–3 first and continue step by step; on the phone, guide them through each step and wait. Remove step 2's keyboard shortcuts for phone-only users.

**Fill in:** `{{ticket_id}}`.

**Do NOT:** ask the customer to install unknown apps, share their screen with a stranger, or send passwords/OTP. Do not tell them to repeat a payment after clearing the cache — if a payment page failed, check the transaction first. If the steps do not help, escalate with the details collected and send *tpl-technical-investigation*.

<!-- template -->
# Known service issue notice
id: tpl-known-outage
category: technical
channel: any
style: standard
tags: known issue, outage, service down, site down, system problem, የአገልግሎት መቋረጥ, ሲስተም ችግር
related: tec-known-outage-handling, tec-tsg-browser-basics

## Message (EN)
Hello {{customer_name}},

Thank you for contacting us, and I am sorry for the inconvenience.

We are aware of a technical issue that is currently affecting some Byfluence users, and our technical team is working to fix it. The problem you are seeing is most likely related to this issue — there is nothing wrong with your account or your device.

While the issue is ongoing, please:
- Avoid repeating a payment if a payment page does not complete. If you were charged, keep your receipt or SMS — any payment will be checked once the service is back to normal.
- Try again later rather than many times in a row.

We will share an update as soon as the service is working normally again. Your case number is {{ticket_id}}.

Thank you for your patience and understanding.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን፤ ለተፈጠረው መጉላላት ይቅርታ እንጠይቃለን።

በአሁኑ ጊዜ አንዳንድ የByfluence ተጠቃሚዎችን የሚያጋጥም የቴክኒክ ችግር መኖሩን እናውቃለን፤ የቴክኒክ ቡድናችንም ችግሩን ለማስተካከል እየሠራ ነው። እያጋጠመዎት ያለው ችግር ከዚሁ ጋር የተያያዘ ሊሆን ይችላል — ችግሩ ከመለያዎ ወይም ከመሣሪያዎ አይደለም።

ችግሩ እስኪስተካከል ድረስ እባክዎ፦
- የክፍያ ገጹ ካልተጠናቀቀ ክፍያውን ደግመው አይፈጽሙ። ገንዘብ ተቆርጦብዎ ከሆነ ደረሰኝዎን ወይም የኤስኤምኤስ መልዕክቱን ያስቀምጡ — አገልግሎቱ ወደ መደበኛ ሁኔታ ሲመለስ ማንኛውም ክፍያ ይጣራል።
- በተከታታይ ብዙ ጊዜ ከመሞከር ይልቅ ትንሽ ቆይተው እንደገና ይሞክሩ።

አገልግሎቱ ወደ መደበኛ ሁኔታ እንደተመለሰ መረጃ እናጋራለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ስለ ትዕግስትዎ እና ግንዛቤዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** Only when a **confirmed** incident is posted on Announcements / by the supervisor, and the customer's problem matches it. Link the ticket to the incident so everyone gets the resolution message (*tpl-bug-fixed*).

**Fill in:** `{{ticket_id}}`. You may add one sentence describing the affected area if the incident notice gives approved wording (e.g. "affecting payments" / "ክፍያዎችን የሚያጋጥም").

**Do NOT:** guess the cause ("the server crashed", "the payment company failed"), promise a fix time, or promise refunds/compensation for missed sessions. If the customer has a session or payment that is time-critical, create a separate high-priority ticket for that — do not leave it waiting only on the outage.

<!-- template -->
# Known service issue notice (SMS)
id: tpl-known-outage-short
category: technical
channel: sms
style: short
tags: outage sms, known issue, service down, sms notice, የአገልግሎት መቋረጥ
related: tec-known-outage-handling

## Message (EN)
Byfluence: We're aware of a technical issue affecting some users and are fixing it. Please don't repeat payments. Updates via {{support_channel}}. Case {{ticket_id}}

## Message (AM)
Byfluence፦ አንዳንድ ተጠቃሚዎችን የሚያጋጥም የቴክኒክ ችግር እያስተካከልን ነው። እባክዎ ክፍያ አይድገሙ። መረጃ በ{{support_channel}}። ጉዳይ {{ticket_id}}

## Usage Notes
**When to use:** SMS notice to customers affected by a **confirmed** incident (e.g. those with open tickets or upcoming sessions).

**Length:** The EN text is close to one SMS once placeholders are filled — keep `{{support_channel}}` short (e.g. the Telegram name, not a long sentence). Amharic SMS uses a different character set and is usually split into more than one SMS part; that is acceptable, but do not add text.

**Do NOT:** promise a fix time or refunds. Send only through the approved SMS tool.

<!-- template -->
# Technical issue fixed
id: tpl-bug-fixed
category: technical
channel: any
style: standard
tags: issue fixed, bug fixed, working again, problem solved, ችግሩ ተስተካክሏል, አሁን ይሠራል
related: tec-known-outage-handling, tec-tsg-browser-basics

## Message (EN)
Hello {{customer_name}},

Good news: our technical team has fixed the issue you reported in case {{ticket_id}}.

Please try again now. If the page still shows the old behaviour, refresh it or log out and log back in.

Could you please reply to let us know whether everything is working for you now? If you still see a problem, send us a screenshot and we will look into it again right away.

Thank you for your patience while we worked on this.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

መልካም ዜና፦ በጉዳይ ቁጥር {{ticket_id}} ያሳወቁንን ችግር የቴክኒክ ቡድናችን አስተካክሎታል።

እባክዎ አሁን እንደገና ይሞክሩ። ገጹ አሁንም ቀድሞ በነበረው ሁኔታ ከታየ፣ ገጹን እንደገና ይጫኑ (refresh) ወይም ከመለያዎ ወጥተው እንደገና ይግቡ።

አሁን ሁሉም ነገር በትክክል እየሠራልዎ መሆኑን እባክዎ ያሳውቁን። አሁንም ችግር ካለ፣ ስክሪንሾት ይላኩልን፤ ወዲያውኑ በድጋሚ እናጣራለን።

ጉዳዩን እስክናስተካክል ድረስ ስለታገሱን እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** Technical / Engineering has confirmed the fix (for an individual bug or a known outage).

**Fill in:** `{{ticket_id}}`.

**Do NOT:** close the ticket before the customer confirms or before your no-response follow-up process is complete. Do not promise compensation for the time lost. If the bug affected a payment or a booking, separately confirm that the payment/booking record is correct before closing.

<!-- template -->
# Your case has been escalated
id: tpl-escalation-notification
category: escalations
channel: any
style: standard
tags: escalated, escalation, specialist team, case transferred, ጉዳዩ ተላልፏል, ለሚመለከተው ቡድን
related: tec-known-outage-handling, con-seller-no-show, out-withdrawal-delayed

## Message (EN)
Hello {{customer_name}},

Thank you for your patience. To make sure your case gets the right attention, I have escalated it to our specialist team, who can review it in more detail.

Your case number is {{ticket_id}}. You do not need to repeat the information you have already shared — everything has been passed on with your case.

We will update you by {{follow_up_time}}. If anything changes on your side in the meantime, just reply here.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስለ ትዕግስትዎ እናመሰግናለን። ጉዳይዎ ተገቢውን ትኩረት እንዲያገኝ፣ በዝርዝር ሊመረምሩት ለሚችሉት ለሚመለከተው ልዩ ቡድናችን አስተላልፌዋለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ቀደም ብለው ያጋሩንን መረጃ እንደገና መላክ አያስፈልግዎትም — ሁሉም መረጃ ከጉዳይዎ ጋር ተላልፏል።

እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። እስከዚያው በእርስዎ በኩል የሚለወጥ ነገር ካለ፣ እዚሁ ይመልሱልን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** Right after you escalate a ticket to Level 2 or a Level 3 department (Payments & Finance, Technical, Seller Operations, Trust & Safety, Logistics & Fulfillment).

**Optional:** You may name the team if that helps the customer ("our Payments team" / "የክፍያ ቡድናችን"). Do **not** name Trust & Safety or mention a fraud check to the customer.

**Fill in:** `{{ticket_id}}`, a `{{follow_up_time}}` you will really meet (you must send an update then, even if there is no result yet — use *tpl-still-investigating*).

**Do NOT promise:** the outcome ("they will refund you"), or a resolution time unless the department gave you `{{estimated_resolution_time}}`.

<!-- template -->
# Your case has been escalated (formal email)
id: tpl-escalation-notification-formal
category: escalations
channel: email
style: formal
tags: escalated, escalation email, formal escalation, complaint escalated, ጉዳዩ ተላልፏል
related: tec-known-outage-handling, out-withdrawal-delayed

## Subject (EN)
Your case {{ticket_id}} has been escalated for further review

## Subject (AM)
ጉዳይዎ {{ticket_id}} ለተጨማሪ ግምገማ ተላልፏል

## Message (EN)
Dear {{customer_name}},

Thank you for your patience regarding case number {{ticket_id}}.

We would like to inform you that your case has been escalated to our specialist team for further review. All the information you have provided has been passed on, so you do not need to submit it again.

We will contact you with an update by {{follow_up_time}}. If you have any additional information that may help, please reply to this email quoting your case number.

We appreciate your understanding and remain committed to handling your case carefully.

Sincerely,
{{support_agent}}
Byfluence Customer Support

## Message (AM)
ውድ {{customer_name}}፣

የጉዳይ ቁጥር {{ticket_id}}ን በተመለከተ ስላሳዩን ትዕግስት እናመሰግናለን።

ጉዳይዎ ለተጨማሪ ግምገማ ለሚመለከተው ልዩ ቡድናችን መተላለፉን በአክብሮት እናሳውቃለን። ያቀረቡልን መረጃ በሙሉ ተላልፏል፤ ስለዚህ እንደገና ማቅረብ አያስፈልግዎትም።

እስከ {{follow_up_time}} ድረስ መረጃ ይዘን እናገኝዎታለን። ሊረዳ የሚችል ተጨማሪ መረጃ ካለዎት፣ እባክዎ የጉዳይ ቁጥርዎን ጠቅሰው ለዚህ ኢሜይል ምላሽ ይስጡ።

ስለ ግንዛቤዎ እናመሰግናለን፤ ጉዳይዎን በጥንቃቄ ለመያዝ ቁርጠኞች ነን።

ከአክብሮት ሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** Email escalations, formal complaints, high-value or sensitive cases, or customers who wrote formally (e.g. businesses).

**Fill in:** `{{ticket_id}}`, `{{follow_up_time}}`.

**Do NOT promise:** an outcome, compensation, or a resolution time unless the department gave you `{{estimated_resolution_time}}`. Do not mention internal department names that suggest wrongdoing (e.g. Trust & Safety).

<!-- template -->
# General status update
id: tpl-status-update
category: escalations
channel: any
style: standard
tags: status update, case update, progress update, any news, የጉዳይ ሁኔታ, ምን ደረሰ

## Message (EN)
Hello {{customer_name}},

Here is an update on your case {{ticket_id}}.

What has happened so far: [one or two factual sentences — what was checked and what was found]

Next step: [what happens next and who is handling it]

We will contact you again by {{follow_up_time}}. If you have any questions in the meantime, just reply here.

Thank you for your patience.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስለ ጉዳይዎ {{ticket_id}} የሚከተለውን መረጃ እናጋራዎታለን።

እስካሁን የተከናወነው፦ [ምን እንደተጣራ እና ምን እንደተገኘ በአንድ ወይም በሁለት ዓረፍተ ነገሮች]

ቀጣዩ እርምጃ፦ [ቀጥሎ የሚሆነውን እና ጉዳዩን የሚከታተለውን አካል]

እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። እስከዚያው ጥያቄ ካለዎት፣ እዚሁ ይመልሱልን።

ስለ ትዕግስትዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** Any open case where you have real progress to share (something checked, a department replied, the seller answered).

**Fill in:** Replace **both** bracketed lines with short, factual text in both languages. Never send the bracket text. Keep it to facts — no guesses about the result.

**Do NOT promise:** the outcome or a resolution date. If there is no progress to report, use *tpl-still-investigating* instead.

<!-- template -->
# Waiting for the seller's response
id: tpl-waiting-for-seller
category: escalations
channel: any
style: standard
tags: waiting for seller, seller not responding, contacted seller, pending seller, ሻጩን እየጠበቅን ነው, የአማካሪው ምላሽ
related: con-seller-no-show, phy-delivery-delay, phy-damaged-product

## Message (EN)
Hello {{customer_name}},

This is an update on your case {{ticket_id}}.

We have contacted {{seller_name}} about your case and are now waiting for their response. We need to hear their side so that we can review the situation fairly.

We will update you by {{follow_up_time}}, whether or not we have heard back from the seller by then.

Thank you for your patience.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ይህ ስለ ጉዳይዎ {{ticket_id}} የሚሰጥ መረጃ ነው።

ስለ ጉዳይዎ {{seller_name}}ን አነጋግረናል፤ አሁን ምላሻቸውን እየጠበቅን ነው። ሁኔታውን በፍትሃዊነት ለመገምገም የእነሱንም ሃሳብ መስማት ያስፈልገናል።

እስከዚያ ድረስ ከሻጩ ምላሽ ብናገኝም ባናገኝም፣ እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

ስለ ትዕግስትዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** The case depends on the seller's answer (no-show, quality complaint, damaged/wrong item, delivery) and you have already contacted the seller (*tpl-seller-contact-request*).

**Fill in:** `{{ticket_id}}`, `{{seller_name}}`, `{{follow_up_time}}`.

**Do NOT:** share what the seller has said so far before it has been reviewed; give the buyer the seller's personal contact details; or promise a decision "even if the seller doesn't answer". If the seller stays silent past your follow-up time, escalate to Senior Support / Seller Operations.

<!-- template -->
# Still investigating (follow-up)
id: tpl-still-investigating
category: escalations
channel: any
style: short
tags: still investigating, follow-up, no update yet, still working, አሁንም እያጣራን ነው

## Message (EN)
Hello {{customer_name}}, a quick update on case {{ticket_id}}: we are still working on it and do not have a final answer yet. Your case is being actively handled, and we will update you again by {{follow_up_time}}. Thank you for your patience.

## Message (AM)
ሰላም {{customer_name}}፣ ስለ ጉዳይ ቁጥር {{ticket_id}} አጭር መረጃ፦ አሁንም እየሠራንበት ነው፤ የመጨረሻ ምላሽ ገና አላገኘንም። ጉዳይዎ በንቃት እየተከታተለ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ መረጃ እንሰጥዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Usage Notes
**When to use:** You promised an update by a certain time and there is no new result yet. Sending this on time builds trust — never let a promised follow-up pass silently.

**Fill in:** `{{ticket_id}}`, a new `{{follow_up_time}}`.

**Do NOT:** invent progress or guess the result. If the case has been waiting a long time or the customer is very upset, ask a supervisor to review and consider escalating.

<!-- template -->
# SMS ticket update
id: tpl-sms-ticket-update
category: escalations
channel: sms
style: short
tags: sms update, ticket update, case update sms, አጭር መልዕክት, የጉዳይ መረጃ

## Message (EN)
Byfluence: Update on case {{ticket_id}} - we're still working on your request and will contact you again by {{follow_up_time}}. Help: {{support_channel}}

## Message (AM)
Byfluence፦ ጉዳይ {{ticket_id}} አሁንም በሂደት ላይ ነው። እስከ {{follow_up_time}} በድጋሚ እናገኝዎታለን። ለእርዳታ፦ {{support_channel}}

## Usage Notes
**When to use:** The customer cannot be reached on Telegram or email, or asked for SMS updates.

**Length:** Keep `{{follow_up_time}}` and `{{support_channel}}` short so the EN text stays within one SMS. Amharic SMS is usually split into more parts — do not add extra text.

**Do NOT:** include amounts, account details, personal information or links in SMS. Do not promise an outcome.

<!-- template -->
# Issue resolved: confirmation
id: tpl-issue-resolved-confirm
category: closing
channel: any
style: standard
tags: issue resolved, case resolved, problem solved, resolution confirmation, ጉዳዩ ተፈቷል, ችግሩ ተፈቷል

## Message (EN)
Hello {{customer_name}},

I am pleased to let you know that your case {{ticket_id}} has been resolved.

Summary: [one or two sentences describing what was done]

Could you please confirm that everything is now in order on your side? If anything is still not right, just reply to this message and we will continue helping you under the same case number.

Thank you for your patience and for choosing Byfluence.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ጉዳይዎ {{ticket_id}} መፈታቱን ሳሳውቅዎ ደስ ይለኛል።

ማጠቃለያ፦ [የተከናወነውን በአንድ ወይም በሁለት ዓረፍተ ነገሮች ይግለጹ]

እባክዎ በእርስዎ በኩል ሁሉም ነገር በትክክል መስተካከሉን ያረጋግጡልን። አሁንም ያልተስተካከለ ነገር ካለ፣ ለዚህ መልዕክት ብቻ ምላሽ ይስጡ፤ በዚሁ የጉዳይ ቁጥር እርዳታችንን እንቀጥላለን።

ስለ ትዕግስትዎ እና Byfluenceን ስለመረጡ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** The fix or decision has been completed and verified in the system (e.g. booking confirmed, link sent and used, payment record corrected, approved refund processed).

**Fill in:** `{{ticket_id}}` and replace the bracketed summary with what was actually done, in both languages.

**Do NOT:** describe a refund as completed unless Payments & Finance has confirmed it; mention amounts that have not been approved; or promise that the problem "will never happen again". Record the root cause and resolution in the ticket before resolving.

<!-- template -->
# Issue resolved: confirmation (friendly)
id: tpl-issue-resolved-confirm-friendly
category: closing
channel: any
style: friendly
tags: issue resolved, all sorted, problem fixed, friendly closing, ተስተካክሏል, ችግሩ ተፈቷል

## Message (EN)
Hi {{customer_name}}! Good news — your case {{ticket_id}} is all sorted: [what was done, in a few words]. Can you check that everything looks right on your side? If anything's still off, just reply here and I'll be happy to help. Thanks so much for your patience!

{{support_agent}}, Byfluence Support

## Message (AM)
ሰላም {{customer_name}}! መልካም ዜና — ጉዳይዎ {{ticket_id}} ተስተካክሏል፦ [የተከናወነውን በጥቂት ቃላት]። እባክዎ በእርስዎ በኩል ሁሉም ነገር ትክክል መሆኑን ያረጋግጡልኝ። አሁንም ያልተስተካከለ ነገር ካለ፣ እዚሁ ይጻፉልኝ፤ በደስታ እረዳዎታለሁ። ስለ ትዕግስትዎ በጣም እናመሰግናለን!

{{support_agent}}፣ Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** Telegram or chat, with customers who have been writing in a relaxed, friendly way, and for simple cases (link sent, booking found, small bug fixed).

**Fill in:** `{{ticket_id}}`, and replace the bracketed text in both languages. Do not use this light tone if the customer was upset or the case was serious.

**Do NOT use** for complaints, financial disputes or formal email — use *tpl-issue-resolved-confirm* instead. Do not describe any refund as completed unless Payments & Finance confirmed it.

<!-- template -->
# Customer satisfaction follow-up
id: tpl-satisfaction-followup
category: closing
channel: any
style: friendly
tags: satisfaction survey, rating, feedback, csat, how did we do, አስተያየት, ደረጃ ይስጡ

## Message (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support about case {{ticket_id}}. We hope we were able to help!

We would really value your feedback. How would you rate the support you received, from 1 (very poor) to 5 (excellent)?

Simply reply with a number. If you would like to add a short comment about what we did well or what we could do better, we would be glad to read it.

Thank you for helping us improve!

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስለ ጉዳይ ቁጥር {{ticket_id}} Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በሚገባ እንደረዳንዎ ተስፋ እናደርጋለን!

የእርስዎ አስተያየት ለእኛ በጣም ጠቃሚ ነው። ያገኙትን ድጋፍ ከ1 (በጣም ደካማ) እስከ 5 (እጅግ በጣም ጥሩ) ባለው ደረጃ እንዴት ይገመግሙታል?

ቁጥሩን ብቻ በመላክ ምላሽ መስጠት ይችላሉ። በጥሩ የሠራነውን ወይም ልናሻሽለው የሚገባንን በተመለከተ አጭር አስተያየት ማከል ከፈለጉ፣ በደስታ እናነበዋለን።

አገልግሎታችንን እንድናሻሽል ስለረዱን እናመሰግናለን!

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** After a case is resolved and the customer has confirmed (or the case was closed normally). Send once per case.

**Fill in:** `{{ticket_id}}`.

**Record:** Enter the rating and any comment in the ticket. A rating of 1–2 or a negative comment should be flagged to the supervisor for review.

**Do NOT:** send this to customers whose case was closed for no response, who are still unhappy, or whose complaint was rejected; do not ask for a rating in exchange for anything; do not argue with negative feedback.

<!-- template -->
# Closing the conversation
id: tpl-closing-conversation
category: closing
channel: any
style: short
tags: closing, goodbye, end chat, anything else, ውይይቱን መዝጋት, ሌላ የምረዳዎት

## Message (EN)
Thank you for contacting Byfluence Support, {{customer_name}}. Is there anything else I can help you with today? If not, I will close this conversation now. You can always reach us again through {{support_channel}}. Have a great day!

## Message (AM)
{{customer_name}}፣ Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ዛሬ ሌላ የምረዳዎት ነገር አለ? ከሌለ ይህንን ውይይት አሁን እዘጋለሁ። በማንኛውም ጊዜ በ{{support_channel}} በኩል እንደገና ሊያገኙን ይችላሉ። መልካም ቀን ይሁንልዎ!

## Usage Notes
**When to use:** End of a Telegram/chat conversation where the question is answered and nothing is pending.

**Fill in:** `{{support_channel}}`.

**Do NOT** close a conversation while any action is still pending (payment check, seller reply, escalation) — use *tpl-status-update* or *tpl-still-investigating* instead.

<!-- template -->
# Closing after no customer response
id: tpl-closing-no-response
category: closing
channel: any
style: standard
tags: no response, closing inactive case, customer not responding, case closed, ምላሽ ስላልመጣ, ጉዳዩ ተዘግቷል

## Message (EN)
Hello {{customer_name}},

We have not heard back from you regarding case {{ticket_id}}, so we are closing it for now.

If you still need help, simply reply to this message or contact us through {{support_channel}} and mention your case number — we will be happy to continue from where we left off.

Thank you for contacting Byfluence Support.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

የጉዳይ ቁጥር {{ticket_id}}ን በተመለከተ ከእርስዎ ምላሽ ስላላገኘን ጉዳዩን ለጊዜው እየዘጋነው ነው።

አሁንም እርዳታ የሚያስፈልግዎ ከሆነ፣ ለዚህ መልዕክት ምላሽ ይስጡ ወይም በ{{support_channel}} በኩል የጉዳይ ቁጥርዎን ጠቅሰው ያግኙን — ካቆምንበት በደስታ እንቀጥላለን።

Byfluence ድጋፍን ስላገኙን እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** You asked the customer for information or confirmation, sent the follow-up reminder(s) your team's SOP requires, and still had no reply.

**Waiting period:** No official waiting period is defined yet. Do **not** write "after X days" or claim a policy period in the message; follow your supervisor's current instruction on how long to wait.

**Fill in:** `{{ticket_id}}`, `{{support_channel}}`.

**Do NOT use** when Byfluence still owes the customer something (a payment check, refund decision, seller response or technical fix) — those cases stay open until we finish our part. Do not send a satisfaction survey after this message.

<!-- template -->
# Reopening your case
id: tpl-reopen-ack
category: closing
channel: any
style: standard
tags: reopen case, case reopened, problem came back, still not fixed, ጉዳዩ እንደገና ተከፍቷል, ችግሩ ተመልሷል

## Message (EN)
Hello {{customer_name}},

Thank you for getting back to us, and I am sorry that the issue is not fully resolved.

I have reopened your case {{ticket_id}}, so all the earlier information stays together and you do not need to explain everything again.

To continue, could you please tell me briefly what is happening now, and share a screenshot if it helps?

We will update you by {{follow_up_time}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

በድጋሚ ስላገኙን እናመሰግናለን፤ ጉዳዩ ሙሉ በሙሉ ባለመፈታቱ ይቅርታ እንጠይቃለን።

ጉዳይዎን {{ticket_id}} እንደገና ከፍቼዋለሁ፤ ስለዚህ ቀደም ሲል የሰጡን መረጃ በሙሉ አንድ ላይ ይቆያል፤ ሁሉንም ነገር እንደገና ማስረዳት አያስፈልግዎትም።

ለመቀጠል፣ እባክዎ አሁን እየሆነ ያለውን በአጭሩ ይንገሩኝ፤ የሚረዳ ከሆነም ስክሪንሾት ይላኩልኝ።

እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A customer replies about a closed or resolved case because the same problem continues or came back.

**Fill in:** `{{ticket_id}}` (the original case number), `{{follow_up_time}}`.

**Check:** If it is actually a **new, different** problem, open a new ticket instead and tell the customer the new number. If the case has been reopened more than once, flag it to Senior Support as a repeated unresolved issue.

**Do NOT promise:** a different outcome from an earlier decision (e.g. a refund that was declined) — reopening means we will look again, not that the decision will change.

<!-- template -->
# Phone call closing script
id: tpl-phone-call-closing
category: closing
channel: phone
style: standard
tags: phone closing, end call, call script, telephone, የስልክ ጥሪ መዝጊያ

## Message (EN)
"Before we finish, let me quickly summarize what we discussed: [summarize the issue and what was agreed in one or two sentences]."

"Your case number is {{ticket_id}}. Would you like me to repeat it, or send it to you by message?"

(If something is pending:) "The next step is [next step]. We will contact you again by {{follow_up_time}}."

"Is there anything else I can help you with today?"

(Wait for the answer. If there is something else, handle it before closing.)

"Thank you for calling Byfluence Support, {{customer_name}}. My name is {{support_agent}}. Have a good day, goodbye."

(Let the customer hang up first if possible.)

## Message (AM)
"ከመጨረሳችን በፊት የተነጋገርነውን በአጭሩ ላጠቃልልዎ፦ [ችግሩን እና የተስማማንበትን በአንድ ወይም በሁለት ዓረፍተ ነገሮች ያጠቃልሉ]።"

"የጉዳይዎ ቁጥር {{ticket_id}} ነው። ቁጥሩን ደግሜ ልንገርዎ ወይስ በመልዕክት ልላክልዎ?"

(በሂደት ላይ ያለ ነገር ካለ፦) "ቀጣዩ እርምጃ [ቀጣዩ እርምጃ] ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።"

"ዛሬ ሌላ የምረዳዎት ነገር አለ?"

(መልሱን ይጠብቁ። ሌላ ጉዳይ ካለ ከመዝጋትዎ በፊት ያስተናግዱት።)

"{{customer_name}}፣ Byfluence ድጋፍን ስለደወሉ እናመሰግናለን። ስሜ {{support_agent}} ይባላል። መልካም ቀን ይሁንልዎ፣ ደህና ይሁኑ።"

(ከተቻለ ደንበኛው መጀመሪያ ስልኩን እንዲዘጋ ይጠብቁ።)

## Usage Notes
**When to use:** At the end of every support phone call, inbound or outbound. Speak Amharic by default unless the customer chose English.

**How to use:** Text in round brackets is an instruction for you — do not read it aloud. Replace the square-bracket parts with the real summary and next step, spoken naturally. Speak slowly when giving the case number; repeat it digit by digit if asked.

**Do NOT:** promise anything during the summary that was not actually agreed or authorized (refunds, dates, outcomes). After the call, write the summary and any commitments in the ticket immediately.
