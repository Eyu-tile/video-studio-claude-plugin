<!-- template -->
# Seller did not join: acknowledgment
id: tpl-seller-no-show-ack
category: consultations
channel: any
style: standard
tags: seller no-show, consultant did not join, seller absent, empty meeting, አማካሪው አልገባም, ሻጩ አልመጣም
related: con-seller-no-show, con-missing-meet-link, con-time-zone-confusion

## Message (EN)
Hello {{customer_name}},

I am very sorry that {{seller_name}} did not join your consultation scheduled for {{booking_date}} at {{booking_time}} (booking {{consultation_id}}). I understand how frustrating it is to prepare for a session and then wait with nobody joining.

We have recorded your report under case number {{ticket_id}}. We are now checking the booking and contacting the consultant to understand what happened.

To help us review this, please reply with:
1. The time you joined the Google Meet and how long you waited
2. Whether you received any message from the consultant before or during the session
3. A screenshot of the empty meeting screen, if you have one

Once we have the facts, we will review the options available for your booking and update you by {{follow_up_time}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

{{booking_date}} በ{{booking_time}} ለተያዘው ምክክርዎ (የቀጠሮ ቁጥር {{consultation_id}}) አማካሪው {{seller_name}} ባለመገኘታቸው ከልብ ይቅርታ እንጠይቃለን። ለክፍለ ጊዜው ተዘጋጅተው ማንም ሳይገባ መጠበቅ ምን ያህል እንደሚያበሳጭ እንረዳለን።

ሪፖርትዎን በጉዳይ ቁጥር {{ticket_id}} መዝግበናል። አሁን ቀጠሮውን እያጣራን ሲሆን ምን እንደተፈጠረ ለማወቅ አማካሪውን እያነጋገርን ነው።

ጉዳዩን ለማጣራት እንዲረዳን እባክዎ የሚከተሉትን ይላኩልን፦
1. ወደ Google Meet የገቡበትን ሰዓት እና ምን ያህል ጊዜ እንደጠበቁ
2. ከክፍለ ጊዜው በፊት ወይም በክፍለ ጊዜው ወቅት ከአማካሪው የደረሰዎት መልዕክት ካለ
3. ካለዎት፣ ባዶውን የስብሰባ ገጽ የሚያሳይ ስክሪንሾት

እውነታውን ካጣራን በኋላ ለቀጠሮዎ ያሉትን አማራጮች እንመለከታለን፤ እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A buyer reports that the consultant never joined the Google Meet at the booked time (one-on-one or group). Use it as the first written reply after you have opened the ticket.

**Before sending:** Check the booking time in the admin dashboard and rule out time-zone or Ethiopian-clock confusion first (see *tpl-time-zone-clarification*). If the session is happening **right now**, try to reach the seller immediately following *con-seller-no-show* before sending this.

**Fill in:** `{{seller_name}}`, `{{booking_date}}`, `{{booking_time}}`, `{{consultation_id}}`, `{{ticket_id}}`, and a realistic `{{follow_up_time}}` you can actually meet. Remove question 3 if the customer already sent a screenshot.

**Do NOT promise:** a refund, a free rebooking, compensation, or that the seller will be penalized. Seller no-show rules are not yet approved — the outcome is decided by authorized staff. Do not blame the seller in writing before you have their side; a missing link or a wrong time can look like a no-show.

<!-- template -->
# Seller did not join: acknowledgment (short)
id: tpl-seller-no-show-ack-short
category: consultations
channel: any
style: short
tags: seller no-show, consultant absent, telegram, short reply, አማካሪው አልገባም
related: con-seller-no-show, con-time-zone-confusion

## Message (EN)
Hi {{customer_name}}, I'm sorry {{seller_name}} didn't join your session. We're checking booking {{consultation_id}} and contacting the consultant now. Please send the time you joined and any messages you received. Case: {{ticket_id}}

## Message (AM)
ሰላም {{customer_name}}፣ {{seller_name}} ወደ ምክክሩ ባለመግባታቸው ይቅርታ እንጠይቃለን። ቀጠሮ {{consultation_id}}ን እያጣራን አማካሪውን እያነጋገርን ነው። እባክዎ የገቡበትን ሰዓት እና የደረሰዎት መልዕክት ካለ ይላኩልን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Usage Notes
**When to use:** Telegram or live chat, when the customer is upset and needs a fast first reply. Follow up with the full *tpl-seller-no-show-ack* or a status update once you have more information.

**Fill in:** `{{seller_name}}`, `{{consultation_id}}`, `{{ticket_id}}`.

**Do NOT promise:** a refund, rebooking or any outcome. Check the booking time for time-zone confusion before replying.

<!-- template -->
# Missing meeting link: investigating
id: tpl-missing-meet-link
category: consultations
channel: any
style: standard
tags: no meet link, missing google meet link, meeting link not received, cannot find link, ሊንክ አልደረሰኝም, የስብሰባ ሊንክ
related: con-missing-meet-link, con-seller-no-show, con-time-zone-confusion

## Message (EN)
Hello {{customer_name}},

Thank you for letting us know that you have not received the Google Meet link for your consultation with {{seller_name}} on {{booking_date}} at {{booking_time}} (booking {{consultation_id}}). I am sorry for the inconvenience.

We are checking your booking now. In the meantime, please:
1. Open your Byfluence dashboard and look under your consultation bookings (upcoming sessions) — the meeting details may already be there
2. Check your email inbox, including the Spam/Junk and Promotions folders
3. Confirm the email address or phone number you used when you booked

I will send you the meeting details as soon as I have them. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

{{booking_date}} በ{{booking_time}} ከ{{seller_name}} ጋር ላለዎት ምክክር (የቀጠሮ ቁጥር {{consultation_id}}) የGoogle Meet ሊንክ እንዳልደረሰዎት ስላሳወቁን እናመሰግናለን። ለተፈጠረው ችግር ይቅርታ እንጠይቃለን።

ቀጠሮዎን አሁን እያጣራን ነው። እስከዚያው ድረስ እባክዎ፦
1. ወደ Byfluence ዳሽቦርድዎ ገብተው በምክክር ቀጠሮዎች (የሚመጡ ክፍለ ጊዜዎች) ስር ይመልከቱ — የስብሰባው መረጃ እዚያ ሊኖር ይችላል
2. የኢሜይል ሳጥንዎን፣ Spam/Junk እና Promotions የሚባሉትን ማህደሮች ጨምሮ ይፈትሹ
3. ቀጠሮውን ሲያስይዙ የተጠቀሙበትን ኢሜይል ወይም ስልክ ቁጥር ያረጋግጡልን

የስብሰባውን መረጃ እንዳገኘሁ ወዲያውኑ እልክልዎታለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** The buyer says they have no Google Meet link (or cannot find it) for a confirmed booking.

**Before sending:** Confirm the booking is actually **confirmed and paid** — if payment is pending, use the payment templates instead. If the session starts very soon, mark the ticket High/Critical and escalate to Technical (link generation) and contact the seller at the same time.

**Fill in:** `{{seller_name}}`, `{{booking_date}}`, `{{booking_time}}`, `{{consultation_id}}`, `{{ticket_id}}`.

**Do NOT promise:** that the session will go ahead at the original time, or that a link "will arrive in X minutes". Whether links are generated automatically or added by the seller is not yet confirmed — do not tell the customer how the link is created. When you have the link, send *tpl-meet-link-resent*.

<!-- template -->
# Missing meeting link: investigating (short)
id: tpl-missing-meet-link-short
category: consultations
channel: any
style: short
tags: no meet link, missing link, telegram, short reply, ሊንክ አልደረሰኝም
related: con-missing-meet-link

## Message (EN)
Hi {{customer_name}}, sorry about the missing Meet link! I'm checking booking {{consultation_id}} now. Please also check your dashboard and your email Spam folder. I'll send the details as soon as I have them. Case: {{ticket_id}}

## Message (AM)
ሰላም {{customer_name}}፣ የMeet ሊንኩ ስላልደረሰዎት ይቅርታ! ቀጠሮ {{consultation_id}}ን አሁን እያጣራሁ ነው። እባክዎ ዳሽቦርድዎን እና የኢሜይልዎን Spam ማህደርም ይመልከቱ። መረጃውን እንዳገኘሁ ወዲያውኑ እልክልዎታለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Usage Notes
**When to use:** Telegram/chat first reply when a buyer has no meeting link, especially close to the session time.

**Fill in:** `{{consultation_id}}`, `{{ticket_id}}`.

**Do NOT promise:** a specific time the link will arrive or that the session will start on time. Escalate immediately if the session is about to start.

<!-- template -->
# Meeting details shared / resent
id: tpl-meet-link-resent
category: consultations
channel: any
style: standard
tags: meet link resent, meeting details, google meet link, session link, የስብሰባ መረጃ, ሊንክ ተልኳል
related: con-missing-meet-link, con-time-zone-confusion

## Message (EN)
Hello {{customer_name}},

Here are the meeting details for your consultation:

- Consultant: {{seller_name}}
- Booking: {{consultation_id}}
- Date: {{booking_date}}
- Time: {{booking_time}} East Africa Time (EAT, Addis Ababa time)
- Google Meet link: [paste the meeting link from the booking record]

We recommend opening the link a little before the start time and checking that your internet connection, microphone and camera are working.

If the link does not open, or nobody is in the meeting at the start time, please reply here and mention case {{ticket_id}} so we can help you quickly.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

የምክክርዎ የስብሰባ መረጃ እነሆ፦

- አማካሪ፦ {{seller_name}}
- የቀጠሮ ቁጥር፦ {{consultation_id}}
- ቀን፦ {{booking_date}}
- ሰዓት፦ {{booking_time}} በምሥራቅ አፍሪካ ሰዓት (EAT፣ የአዲስ አበባ ሰዓት)
- የGoogle Meet ሊንክ፦ [ከቀጠሮው መዝገብ ላይ ሊንኩን እዚህ ያስገቡ]

ክፍለ ጊዜው ከመጀመሩ ትንሽ ቀደም ብለው ሊንኩን እንዲከፍቱ እና የኢንተርኔት ግንኙነትዎ፣ ማይክሮፎንዎ እና ካሜራዎ በትክክል መሥራታቸውን እንዲያረጋግጡ እንመክራለን።

ሊንኩ ካልተከፈተ ወይም በመጀመሪያው ሰዓት ማንም ስብሰባው ውስጥ ከሌለ፣ በፍጥነት እንድንረዳዎ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን ጠቅሰው እዚሁ ይመልሱልን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** You have the correct Google Meet link (from the booking record or confirmed by the seller) and need to send or resend it to the buyer.

**Fill in:** All booking placeholders, and **replace the bracketed line** with the real meeting link. Never send the template with the bracket text still in it.

**Check before sending:** The link belongs to *this* booking (do not copy a link from another booking), and the time you write is the one in the booking record. If the customer seems unsure about the time, add the clarification from *tpl-time-zone-clarification*.

**Do NOT promise:** that the consultant will definitely be present, or that a missed session will be rebooked.

<!-- template -->
# Consultation cancellation request received
id: tpl-consultation-cancellation-ack
category: consultations
channel: any
style: standard
tags: cancel consultation, cancel booking, cancellation request, ቀጠሮ መሰረዝ, ምክክር ይሰረዝልኝ
related: con-cancellation-by-buyer, con-reschedule-request

## Message (EN)
Hello {{customer_name}},

We have received your request to cancel your consultation with {{seller_name}} on {{booking_date}} at {{booking_time}} (booking {{consultation_id}}). Your case number is {{ticket_id}}.

We are now reviewing your request, including any questions about your payment, according to the rules that apply to this booking. Until you receive a confirmation from us, please treat your booking as still active.

If you would prefer to move the session to another time instead of cancelling, just let us know — we can check with the consultant whether that is possible.

We will update you on the outcome by {{follow_up_time}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

{{booking_date}} በ{{booking_time}} ከ{{seller_name}} ጋር ያለዎትን ምክክር (የቀጠሮ ቁጥር {{consultation_id}}) ለመሰረዝ ያቀረቡትን ጥያቄ ተቀብለናል። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ጥያቄዎን፣ ከክፍያዎ ጋር የተያያዙ ጥያቄዎችንም ጨምሮ፣ ለዚህ ቀጠሮ በሚመለከተው ደንብ መሠረት እየገመገምን ነው። ከእኛ ማረጋገጫ እስኪደርስዎ ድረስ እባክዎ ቀጠሮዎ አሁንም እንደጸና ይቁጠሩት።

ከመሰረዝ ይልቅ ክፍለ ጊዜውን ወደ ሌላ ጊዜ ማዛወር ከመረጡ እባክዎ ያሳውቁን — ይህ የሚቻል መሆኑን ከአማካሪው ጋር እናጣራለን።

የውሳኔውን ውጤት እስከ {{follow_up_time}} ድረስ እናሳውቅዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A buyer asks support to cancel a booked consultation (one-on-one).

**Fill in:** booking placeholders, `{{ticket_id}}`, `{{follow_up_time}}`.

**Do NOT promise:** that the booking is already cancelled, a refund, a full or partial refund amount, or any deadline ("you cancelled in time"). Cancellation and refund rules are not yet approved — authorized staff decide. If the session is very close, mark the ticket High and inform the seller side so nobody waits in an empty meeting. For group sessions, escalate to Senior Support because group cancellation rules are pending.

<!-- template -->
# Reschedule request received
id: tpl-reschedule-request
category: consultations
channel: any
style: standard
tags: reschedule, change time, move session, new date, ቀጠሮ ማዛወር, ሰዓት መቀየር
related: con-reschedule-request, con-cancellation-by-buyer, con-time-zone-confusion

## Message (EN)
Hello {{customer_name}},

Thank you for letting us know that you would like to reschedule your consultation with {{seller_name}}, currently booked for {{booking_date}} at {{booking_time}} (booking {{consultation_id}}).

To help us arrange this, please send two or three alternative dates and times that work for you (please mention that they are in Addis Ababa time, or tell us your time zone).

Rescheduling depends on the consultant's availability and the rules that apply to this booking, so we cannot confirm a new time yet. Until we confirm a change, your original booking stays as scheduled.

Your case number is {{ticket_id}}, and we will update you by {{follow_up_time}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

{{booking_date}} በ{{booking_time}} ከ{{seller_name}} ጋር የተያዘውን ምክክርዎን (የቀጠሮ ቁጥር {{consultation_id}}) ወደ ሌላ ጊዜ ማዛወር እንደሚፈልጉ ስላሳወቁን እናመሰግናለን።

ይህንን ለማመቻቸት እንዲረዳን፣ እባክዎ የሚመችዎትን ሁለት ወይም ሦስት አማራጭ ቀኖችና ሰዓቶች ይላኩልን (ሰዓቶቹ በአዲስ አበባ ሰዓት መሆናቸውን ይግለጹ፣ ወይም ያሉበትን የሰዓት ክልል ያሳውቁን)።

ቀጠሮ ማዛወር በአማካሪው ክፍት ጊዜ እና ለዚህ ቀጠሮ በሚመለከተው ደንብ ላይ የተመሠረተ ስለሆነ፣ አዲሱን ሰዓት አሁን ማረጋገጥ አንችልም። ለውጡን እስክናረጋግጥልዎ ድረስ የመጀመሪያው ቀጠሮዎ እንደተያዘ ይቆያል።

የጉዳይዎ ቁጥር {{ticket_id}} ሲሆን እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A buyer asks to move a booked session to another date/time, and they cannot do it themselves from their dashboard.

**Fill in:** current booking details and `{{follow_up_time}}`.

**Do NOT promise:** that the new time is accepted, that rescheduling is free, or that the original payment automatically moves to the new slot. Only confirm a new time after the seller has agreed and the booking record shows the change. If the request comes from the **seller** side, escalate to Senior Support instead of using this template.

<!-- template -->
# Responding to a buyer who missed their session
id: tpl-buyer-no-show-explain
category: consultations
channel: any
style: standard
tags: buyer missed session, buyer no-show, missed consultation, late buyer, ክፍለ ጊዜው አመለጠኝ, ቀጠሮ አመለጠኝ
related: con-buyer-no-show, con-time-zone-confusion, con-reschedule-request

## Message (EN)
Hello {{customer_name}},

Thank you for contacting us about your consultation with {{seller_name}} on {{booking_date}} at {{booking_time}} (booking {{consultation_id}}). I am sorry that you were not able to attend.

To review your case fairly, we will check the booking details and ask the consultant for their account of the session. It would help us if you could tell us briefly what happened — for example, a connection problem, confusion about the time, or the link not opening — and share a screenshot if you have one.

Options after a missed session depend on the consultant and on the rules that apply to your booking, so I cannot confirm a new session or a refund at this stage. We will look into it carefully and update you by {{follow_up_time}}.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

{{booking_date}} በ{{booking_time}} ከ{{seller_name}} ጋር ስለነበረዎት ምክክር (የቀጠሮ ቁጥር {{consultation_id}}) ስላነጋገሩን እናመሰግናለን። በክፍለ ጊዜው ላይ መገኘት ባለመቻልዎ እናዝናለን።

ጉዳይዎን በፍትሃዊነት ለመገምገም የቀጠሮውን ዝርዝር እናጣራለን፤ ስለ ክፍለ ጊዜውም አማካሪውን እንጠይቃለን። ምን እንደተፈጠረ በአጭሩ ቢነግሩን ይረዳናል — ለምሳሌ የኢንተርኔት ግንኙነት ችግር፣ ስለ ሰዓቱ የተፈጠረ ግራ መጋባት፣ ወይም ሊንኩ አለመከፈቱ — ካለዎትም ስክሪንሾት ይላኩልን።

ያመለጠ ክፍለ ጊዜን በተመለከተ ያሉት አማራጮች በአማካሪው እና ለቀጠሮዎ በሚመለከተው ደንብ ላይ የተመሠረቱ ስለሆኑ፣ በዚህ ደረጃ አዲስ ክፍለ ጊዜም ሆነ ተመላሽ ክፍያ ማረጋገጥ አልችልም። ጉዳዩን በጥንቃቄ ተመልክተን እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** The buyer did not join (or joined very late) and is now asking for a new session or their money back.

**Tone:** Never blame or lecture the customer. Many "no-shows" are caused by Ethiopian-clock vs international-clock confusion, a missing link or a weak connection — check those first.

**Fill in:** booking placeholders, `{{follow_up_time}}`, `{{ticket_id}}`.

**Do NOT promise:** a free reschedule, a refund, or that the seller "must" offer anything. Missed-session rules are not approved yet; escalate to Senior Support / Supervisor for a decision. Remember a scheduled meeting does not prove the service was delivered — collect both sides before any decision.

<!-- template -->
# Group session cancelled notice
id: tpl-group-session-cancelled
category: consultations
channel: email
style: formal
tags: group session cancelled, group consultation cancelled, session cancelled by seller, የቡድን ምክክር ተሰርዟል
related: grp-cancelled-by-seller, con-cancellation-by-buyer

## Subject (EN)
Your group session on {{booking_date}} has been cancelled — case {{ticket_id}}

## Subject (AM)
{{booking_date}} ሊካሄድ የነበረው የቡድን ምክክርዎ ተሰርዟል — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

We regret to inform you that the group consultation hosted by {{seller_name}}, scheduled for {{booking_date}} at {{booking_time}} (booking {{consultation_id}}), has been cancelled. We sincerely apologize for the inconvenience this may cause you.

Please note that you do not need to join the meeting link for this session.

Regarding your payment of {{amount}}, our team is reviewing the next steps for all registered participants in line with the applicable Byfluence policy. We will contact you with the available options by {{follow_up_time}}. Please do not make a new payment for this session in the meantime.

If you have any questions, please reply to this email or contact us through {{support_channel}}, quoting case number {{ticket_id}}.

Thank you for your understanding.

Sincerely,
{{support_agent}}
Byfluence Customer Support

## Message (AM)
ውድ {{customer_name}}፣

በ{{seller_name}} የሚመራው እና {{booking_date}} በ{{booking_time}} ሊካሄድ ቀጠሮ የተያዘለት የቡድን ምክክር (የቀጠሮ ቁጥር {{consultation_id}}) መሰረዙን ስናሳውቅዎ በአክብሮት ነው። ይህ ለሚፈጥርብዎ መጉላላት ከልብ ይቅርታ እንጠይቃለን።

ለዚህ ክፍለ ጊዜ በተላከው የስብሰባ ሊንክ መግባት አያስፈልግዎትም።

የከፈሉትን {{amount}} በተመለከተ፣ ቡድናችን ለሁሉም የተመዘገቡ ተሳታፊዎች የሚወሰዱትን ቀጣይ እርምጃዎች በሚመለከተው የByfluence ፖሊሲ መሠረት እየገመገመ ነው። ያሉትን አማራጮች ይዘን እስከ {{follow_up_time}} ድረስ እናገኝዎታለን። እስከዚያው ድረስ እባክዎ ለዚህ ክፍለ ጊዜ አዲስ ክፍያ አይፈጽሙ።

ማንኛውም ጥያቄ ካለዎት፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን ጠቅሰው ለዚህ ኢሜይል ምላሽ ይስጡ ወይም በ{{support_channel}} በኩል ያግኙን።

ስለ ግንዛቤዎ እናመሰግናለን።

ከአክብሮት ሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A group consultation has been **confirmed as cancelled** (by the seller or by Byfluence) and every registered participant must be informed. Send one email per participant; never put all participants in To/CC.

**Fill in:** `{{seller_name}}`, date/time, `{{consultation_id}}`, the amount this participant paid (`{{amount}}`), `{{follow_up_time}}`, `{{support_channel}}`.

**Do NOT:** state the reason for the cancellation unless Seller Operations approved the wording; promise a refund, a replacement session or a credit; or give a refund date. Group cancellation, rescheduling and refund rules are **not yet approved** — Senior Support / Supervisor must confirm the options before the follow-up message.

<!-- template -->
# Clarifying session time (EAT / Ethiopian vs international clock)
id: tpl-time-zone-clarification
category: consultations
channel: any
style: standard
tags: time zone, ethiopian time, EAT, wrong time, ሰዓት አቆጣጠር, የኢትዮጵያ ሰዓት, ፈረንጅ ሰዓት
related: con-time-zone-confusion, con-missing-meet-link, con-seller-no-show

## Message (EN)
Hello {{customer_name}},

Thank you for checking with us — I am happy to clarify the time of your consultation with {{seller_name}} (booking {{consultation_id}}).

Your session is on {{booking_date}} at {{booking_time}} East Africa Time (EAT), which is the time in Addis Ababa.

Please note that this time uses the international clock. In traditional Ethiopian time-telling, hours are counted six hours differently. For example, 9:00 AM on the international clock is 3 o'clock in the morning in Ethiopian time ("ሦስት ሰዓት").

If you are joining from outside Ethiopia, please convert the time from EAT (UTC+3) to your local time.

If anything is still unclear, just reply here and mention case {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስለጠየቁን እናመሰግናለን — ከ{{seller_name}} ጋር ያለዎትን ምክክር (የቀጠሮ ቁጥር {{consultation_id}}) ሰዓት በደስታ ላብራራልዎ።

ክፍለ ጊዜዎ {{booking_date}} በ{{booking_time}} በምሥራቅ አፍሪካ ሰዓት (EAT)፣ ማለትም በአዲስ አበባ ሰዓት ነው።

እባክዎ ልብ ይበሉ፦ ይህ ሰዓት የተገለጸው በዓለም አቀፍ (በፈረንጅ) የሰዓት አቆጣጠር ነው። በኢትዮጵያ የሰዓት አቆጣጠር ሰዓቱ በስድስት ሰዓት ልዩነት ይቆጠራል። ለምሳሌ በዓለም አቀፍ አቆጣጠር 9:00 AM ማለት በኢትዮጵያ አቆጣጠር ጠዋት ሦስት ሰዓት ነው።

ከኢትዮጵያ ውጭ ሆነው የሚገቡ ከሆነ፣ እባክዎ ሰዓቱን ከEAT (UTC+3) ወደ ያሉበት አካባቢ ሰዓት ይቀይሩት።

አሁንም ግልጽ ያልሆነ ነገር ካለ፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን ጠቅሰው እዚሁ ይመልሱልን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** The customer (buyer or seller) is unsure when the session starts, joined at the wrong time, or mixes Ethiopian and international clocks. Also useful before a session if the customer asks "is it ሦስት ሰዓት or 3 o'clock?".

**How to convert:** Ethiopian clock = international EAT time minus six hours (day hours start at 6:00 AM = 12 ሰዓት / ማለዳ). Examples: 7:00 AM = 1 ሰዓት ጠዋት; 12:00 PM = 6 ሰዓት; 3:00 PM = 9 ሰዓት ከሰዓት በኋላ; 8:00 PM = 2 ሰዓት ማታ.

**Fill in:** `{{booking_date}}` and `{{booking_time}}` exactly as in the booking record (international clock). You may replace the example sentence with the customer's actual time converted to Ethiopian clock — double-check your conversion before sending.

**Watch out:** The Ethiopian **calendar** date is also different from the Gregorian date. If the customer writes dates in the Ethiopian calendar, confirm the Gregorian date shown in the booking record before agreeing on anything.

**Do NOT promise:** a rebooking if the customer missed the session because of the time confusion — use *tpl-buyer-no-show-explain* for that.

<!-- template -->
# Checking order status
id: tpl-order-status-check
category: orders
channel: any
style: standard
features: physical-products, delivery-addis
tags: order status, where is my order, track order, order update, ትዕዛዜ የት ደረሰ, የትዕዛዝ ሁኔታ
related: phy-delivery-delay, phy-order-status

## Message (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I am checking the status of your order {{order_id}} for {{product_name}} from {{seller_name}} now.

You can also see your order information at any time in your Byfluence dashboard under your purchase history.

If you placed the order with a different email address or phone number than the one you are contacting us from, please let me know so I can find it quickly.

Your case number is {{ticket_id}}. I will update you by {{follow_up_time}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ከ{{seller_name}} ያዘዙትን {{product_name}} (የትዕዛዝ ቁጥር {{order_id}}) ሁኔታ አሁን እያጣራሁ ነው።

የትዕዛዝዎን መረጃ በማንኛውም ጊዜ በByfluence ዳሽቦርድዎ ላይ በግዢ ታሪክዎ ስር ማየት ይችላሉ።

ትዕዛዙን ያስገቡት አሁን ካገኙን ኢሜይል ወይም ስልክ ቁጥር በተለየ ከሆነ፣ በፍጥነት እንዳገኘው እባክዎ ያሳውቁኝ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። እስከ {{follow_up_time}} ድረስ መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**Feature check first:** Physical products and delivery are **planned** features. Check the *Feature Status* page before using this template. If physical orders are not live, use *tpl-feature-not-available* instead.

**When to use:** A buyer asks where their product order is, or what stage it is at.

**Fill in:** `{{order_id}}`, `{{product_name}}`, `{{seller_name}}`, `{{ticket_id}}`, `{{follow_up_time}}`. If you already know the status, add one factual sentence (e.g. "The seller has marked your order as being prepared").

**Do NOT promise:** a delivery date or time window, free delivery, or that the order "will arrive today". Delivery times and areas are not confirmed.

<!-- template -->
# Delivery delay update
id: tpl-delivery-delay
category: orders
channel: any
style: standard
features: physical-products, delivery-addis
tags: delivery delay, late delivery, order not arrived, delayed order, ትዕዛዝ ዘገየ, አልደረሰልኝም
related: phy-delivery-delay, phy-order-status

## Message (EN)
Hello {{customer_name}},

I am sorry that your order {{order_id}} ({{product_name}}) has not reached you yet. I understand that waiting for an order without clear information is frustrating.

We are checking the order with {{seller_name}} and the team handling the delivery to find out where it is and what caused the delay.

To make sure nothing is holding it up on our side, please confirm:
1. Your full delivery address, including a nearby landmark
2. A phone number where the delivery person can reach you

We do not have a confirmed new delivery time yet, but we will update you by {{follow_up_time}}. Your case number is {{ticket_id}}.

Thank you for your patience.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ትዕዛዝዎ {{order_id}} ({{product_name}}) እስካሁን ስላልደረሰዎት ይቅርታ እንጠይቃለን። ግልጽ መረጃ ሳያገኙ ትዕዛዝን መጠበቅ እንደሚያስቸግር እንረዳለን።

ትዕዛዙ የት እንዳለ እና የመዘግየቱ ምክንያት ምን እንደሆነ ለማወቅ ከ{{seller_name}} እና ማድረሱን ከሚያስተባብረው ቡድን ጋር እያጣራን ነው።

በእኛ በኩል የሚያዘገየው ነገር እንዳይኖር፣ እባክዎ የሚከተሉትን ያረጋግጡልን፦
1. ሙሉ የማድረሻ አድራሻዎን፣ በአቅራቢያ ያለ የሚታወቅ ቦታን ጨምሮ
2. አድራሹ ሊያገኝዎት የሚችልበትን ስልክ ቁጥር

አዲስ የማድረሻ ጊዜ እስካሁን አልተረጋገጠም፤ ሆኖም እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ስለ ትዕግስትዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**Feature check first:** Delivery is a **planned** feature (initial rollout prioritizes Addis Ababa). Confirm on the *Feature Status* page that delivery is live before using this template.

**When to use:** The buyer's order is late compared with what they were told, or they have had no update.

**Fill in:** order placeholders, `{{follow_up_time}}`, `{{ticket_id}}`. Remove the address/phone request if you have already verified both in the order record.

**Do NOT promise:** a delivery date, a delivery-fee refund, compensation or cancellation without charge. Delivery times, fees and partner responsibilities are not confirmed. Escalate to Logistics & Fulfillment if the order cannot be located.

<!-- template -->
# Damaged item report received
id: tpl-damaged-item-ack
category: orders
channel: any
style: standard
features: physical-products, delivery-addis
tags: damaged item, broken product, damaged delivery, item arrived broken, የተበላሸ እቃ, ተሰብሮ ደረሰ
related: phy-damaged-product, phy-wrong-item

## Message (EN)
Hello {{customer_name}},

I am very sorry that your {{product_name}} (order {{order_id}}) arrived damaged. Thank you for reporting it to us.

To review your case, please send us:
1. Clear photos of the damaged item from several angles
2. Photos of the outer packaging and any label on it
3. A short description of the damage and when you noticed it

Please keep the item and all packaging as they are for now, and do not throw anything away or send the item back until we tell you the next steps.

We will review the evidence with {{seller_name}} and update you by {{follow_up_time}}. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ያዘዙት {{product_name}} (የትዕዛዝ ቁጥር {{order_id}}) ተበላሽቶ ስለደረሰዎት በጣም ይቅርታ እንጠይቃለን። ስላሳወቁን እናመሰግናለን።

ጉዳይዎን ለመገምገም እባክዎ የሚከተሉትን ይላኩልን፦
1. የተበላሸውን እቃ ከተለያዩ አቅጣጫዎች የተነሱ ግልጽ ፎቶዎች
2. የውጪውን ማሸጊያ እና በላዩ ያለውን መለያ (label) ፎቶዎች
3. ጉዳቱ ምን እንደሆነ እና መቼ እንዳስተዋሉት አጭር መግለጫ

እባክዎ እቃውን እና ማሸጊያውን በሙሉ ባሉበት ሁኔታ ያቆዩ፤ ቀጣዩን እርምጃ እስክንነግርዎ ድረስ ምንም ነገር አይጣሉ፣ እቃውንም አይመልሱ።

ማስረጃውን ከ{{seller_name}} ጋር ገምግመን እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**Feature check first:** Physical products are a **planned** feature — check *Feature Status* before using.

**When to use:** The buyer reports the product arrived broken, damaged or not working.

**Fill in:** `{{product_name}}`, `{{order_id}}`, `{{seller_name}}`, `{{follow_up_time}}`, `{{ticket_id}}`.

**Do NOT promise:** a replacement, a refund, a return pick-up or who will pay for return shipping. Return and refund rules for physical products are not approved. Never ask for photos that show the customer's ID or payment details. Watch for fraud signals (old or internet photos, damage that does not match the product) and escalate to Trust & Safety if in doubt.

<!-- template -->
# Wrong item received
id: tpl-wrong-item-ack
category: orders
channel: any
style: standard
features: physical-products, delivery-addis
tags: wrong item, wrong product, different item, not what I ordered, የተሳሳተ እቃ, ያላዘዝኩት እቃ
related: phy-wrong-item, phy-damaged-product

## Message (EN)
Hello {{customer_name}},

I am sorry that you received a different item from the {{product_name}} you ordered (order {{order_id}}). Thank you for letting us know.

To help us sort this out, please send:
1. Photos of the item you received, including any label or tag
2. A photo of the packaging or delivery slip, if there was one

Please keep the item unused and in its original packaging, and do not send it back until we confirm the next steps with you.

We are checking the order with {{seller_name}} and will update you by {{follow_up_time}}. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ካዘዙት {{product_name}} (የትዕዛዝ ቁጥር {{order_id}}) የተለየ እቃ ስለደረሰዎት ይቅርታ እንጠይቃለን። ስላሳወቁን እናመሰግናለን።

ጉዳዩን ለማስተካከል እንዲረዳን እባክዎ የሚከተሉትን ይላኩልን፦
1. የደረሰዎትን እቃ ፎቶዎች፣ መለያ (label) ወይም ታግ ካለውም ጨምሮ
2. ማሸጊያው ወይም የማድረሻ ወረቀት ካለ ፎቶው

እባክዎ እቃውን ሳይጠቀሙበት በዋናው ማሸጊያው ውስጥ ያቆዩት፤ ቀጣዩን እርምጃ እስክናረጋግጥልዎ ድረስም አይመልሱት።

ትዕዛዙን ከ{{seller_name}} ጋር እያጣራን ሲሆን እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**Feature check first:** Physical products are a **planned** feature — check *Feature Status* before using.

**When to use:** The buyer received a different product, size, colour or quantity from what the order shows.

**Fill in:** `{{product_name}}` as it appears on the order (what they *should* have received), `{{order_id}}`, `{{seller_name}}`, `{{follow_up_time}}`, `{{ticket_id}}`.

**Do NOT promise:** an exchange, a refund, a free return, or that the correct item will be sent. Return/exchange rules are not approved; Senior Support or Logistics & Fulfillment decide next steps.

<!-- template -->
# Order cancellation request received
id: tpl-order-cancellation-ack
category: orders
channel: any
style: standard
features: physical-products
tags: cancel order, order cancellation, stop order, ትዕዛዝ መሰረዝ, ትዕዛዜን ሰርዙልኝ
related: phy-order-cancellation, phy-delivery-delay

## Message (EN)
Hello {{customer_name}},

We have received your request to cancel your order {{order_id}} for {{product_name}}. Your case number is {{ticket_id}}.

Whether an order can still be cancelled depends on its current stage — for example, whether {{seller_name}} has already prepared or sent it — and on the rules that apply to the order. We are checking this now and will confirm the outcome, including any payment-related next steps, by {{follow_up_time}}.

Until you receive our confirmation, please treat the order as still active. If the item is delivered before we reply, please let us know and do not open or use it.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

የ{{product_name}} ትዕዛዝዎን (የትዕዛዝ ቁጥር {{order_id}}) ለመሰረዝ ያቀረቡትን ጥያቄ ተቀብለናል። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ትዕዛዝ አሁንም ሊሰረዝ ይችል እንደሆነ የሚወሰነው ትዕዛዙ ባለበት ደረጃ ላይ ነው — ለምሳሌ {{seller_name}} ትዕዛዙን አዘጋጅተው ወይም ልከው እንደሆነ — እንዲሁም ለትዕዛዙ በሚመለከተው ደንብ ላይ ነው። ይህንን አሁን እያጣራን ሲሆን ውጤቱን፣ ከክፍያ ጋር የተያያዙ ቀጣይ እርምጃዎችን ጨምሮ፣ እስከ {{follow_up_time}} ድረስ እናረጋግጥልዎታለን።

ማረጋገጫችን እስኪደርስዎ ድረስ እባክዎ ትዕዛዙ አሁንም እንደጸና ይቁጠሩት። ምላሽ ከመስጠታችን በፊት እቃው ከደረሰዎት እባክዎ ያሳውቁን፤ እቃውንም አይክፈቱ ወይም አይጠቀሙበት።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**Feature check first:** Physical product orders are **planned** — check *Feature Status* before using.

**When to use:** A buyer asks to cancel a product order.

**Fill in:** `{{order_id}}`, `{{product_name}}`, `{{seller_name}}`, `{{ticket_id}}`, `{{follow_up_time}}`.

**Do NOT promise:** that the order is cancelled, a refund, a refund amount or date, or that no fees apply. Cancellation and refund rules are not approved; Payments & Finance and authorized staff decide. Inform the seller quickly so they do not dispatch the order while it is under review.

<!-- template -->
# Feature not available yet (planned)
id: tpl-feature-not-available
category: orders
channel: any
style: standard
features: physical-products, delivery-addis, digital-products, inventory-free-selling
tags: feature not available, coming soon, delivery not available, digital products, dropshipping, not yet available, አገልግሎቱ ገና አልተጀመረም
related: phy-delivery-delay, dig-access-issue, inv-program-overview

## Message (EN)
Hello {{customer_name}},

Thank you for your interest and for your question.

The service you asked about is not available on Byfluence yet. It is part of our plans as the marketplace grows, but we do not have a confirmed launch date to share at the moment.

We appreciate your patience, and we will share news through our official channels when it becomes available. In the meantime, if there is anything else I can help you with on Byfluence today, please let me know.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስላሳዩት ፍላጎት እና ስለጠየቁን እናመሰግናለን።

የጠየቁት አገልግሎት በByfluence ላይ ገና አልተጀመረም። የገበያ ቦታችን እያደገ ሲሄድ ለማቅረብ ካቀድናቸው አገልግሎቶች አንዱ ነው፤ ሆኖም በአሁኑ ጊዜ ልናሳውቅዎ የምንችለው የተረጋገጠ የመጀመሪያ ቀን የለም።

ስለ ትዕግስትዎ እናመሰግናለን፤ አገልግሎቱ ሲጀመር በይፋዊ መገናኛዎቻችን እናሳውቃለን። እስከዚያው ድረስ በByfluence ላይ ሌላ የምረዳዎት ነገር ካለ እባክዎ ይንገሩኝ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A customer asks about something that the *Feature Status* page shows as **planned** or **unconfirmed** — e.g. product delivery, physical product orders, digital products, inventory-free selling / reselling, or a payment method that is not live.

**Always check first:** Open the *Feature Status* page. If the feature is now live, do NOT use this template — answer with the relevant how-to article.

**Optional:** You may name the feature in the first sentence (e.g. "The home delivery service you asked about…" / "የጠየቁት የቤት ለቤት ማድረሻ አገልግሎት…").

**Do NOT promise:** a launch date, "very soon", early access, a waiting list, or special prices. Do not describe how the future feature will work (fees, zones, commissions) — none of this is confirmed. Never say "zero cost" about inventory-free selling.
