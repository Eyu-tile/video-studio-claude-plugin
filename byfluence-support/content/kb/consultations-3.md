<!-- doc -->
# Buyer joined late
id: con-buyer-late
type: article
category: consultations
subcategory: attendance
audience: both
priority: medium
department: support_l1
features: consultations-1on1, google-meet
tags: buyer late, I am late, running late, joined late, buyer arrived late, extend session, ዘግይቻለሁ, ዘግይቼ ገባሁ, ገዢው ዘገየ
related: con-seller-late, con-buyer-no-show, con-tsg-no-show-decision-guide, con-duration-dispute, con-time-zone-confusion
templates: tpl-waiting-for-seller, tpl-buyer-no-show-explain, tpl-request-booking-details
policy_pending: yes

## Summary
The buyer is running late for, or joined late to, their consultation — either the buyer asks for help ("I'm late, will the consultant wait?") or the seller reports the buyer arrived late and wants the session to end on time.

## Issue Description
Two common contacts:
1. **Before/at session time** — the buyer tells support they are late or will be late (transport, power, work, connection). They want to know whether the consultant will wait and whether they will get their full time.
2. **After the session** — the buyer complains the session was short, or the seller reports the buyer joined late and asks how to handle it.

Late arrival can also be caused by problems that are *not* the buyer's fault: missing link, waiting in "Ask to join", or time confusion. Check these before treating it as buyer lateness.

## Possible Causes
- Buyer's personal delay (transport, work, power outage, connection).
- Buyer misread the time (Ethiopian clock, AM/PM, date).
- Buyer had no link or the wrong link and lost time finding it.
- Buyer was waiting to be admitted and it looked like lateness to the seller.
- Buyer's dashboard/notification showed a wrong time (display bug).

## Information to Collect
- Booking ID / consultant name and session time (EAT)
- What time the buyer joined or expects to join
- Reason for lateness (ask kindly; it affects the outcome)
- Whether the buyer had the link and the correct time
- After the session: how long the session actually lasted, from both sides

## Troubleshooting Steps
1. **If the buyer is late right now:**
   - Tell them to join as soon as possible with the link (send it if needed).
   - Let the seller know the buyer is on their way, if you can reach them quickly (`tpl-seller-contact-request`).
   - Do not promise that the consultant will wait or extend the session.
2. **Check whether it was really the buyer's fault:** compare their join time with any support contact about missing link/access, confirm they understood the time correctly.
   - If the delay was caused by a platform problem (no link, broken link, display error) → treat as a platform issue: `con-missing-meet-link` / `con-incorrect-meet-link`; note it for the outcome decision.
3. **After the session:** if the buyer wants extra time or compensation → collect both sides' times and follow `con-duration-dispute`. If the seller asks to mark it completed → `con-completion-confirmation`.
4. If the buyer never joined → `con-buyer-no-show`.
5. Record the buyer's join time, reason and any messages in the ticket.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know. Please join your session with {{seller_name}} as soon as you can, using your Google Meet link: [link]. Your session was booked for {{booking_date}} at {{booking_time}} (EAT).

I will let the consultant know you are on your way. Please note that consultants may have other commitments after your booked time, so I can't guarantee the session can be extended.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን። እባክዎ በGoogle Meet ሊንክዎ ተጠቅመው ከ{{seller_name}} ጋር ያለዎትን ምክክር በተቻለዎት ፍጥነት ይቀላቀሉ፦ [ሊንክ]። ምክክርዎ የተያዘው ለ{{booking_date}} በ{{booking_time}} (EAT) ነበር።

በመንገድ ላይ እንዳሉ ለአማካሪው አሳውቃለሁ። እባክዎ አማካሪዎች ከእርስዎ ሰዓት በኋላ ሌላ ቀጠሮ ሊኖራቸው ስለሚችል፣ ምክክሩ እንደሚራዘም ማረጋገጥ እንደማልችል ልብ ይበሉ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please join now with your Meet link: [link] ({{booking_date}}, {{booking_time}} EAT). I'll tell {{seller_name}} you're on your way — I can't guarantee extra time. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ እባክዎ አሁኑኑ በMeet ሊንክዎ ይግቡ፦ [ሊንክ] ({{booking_date}}፣ {{booking_time}} EAT)። በመንገድ ላይ እንዳሉ ለ{{seller_name}} እነግራለሁ — ተጨማሪ ጊዜ ማረጋገጥ ግን አልችልም። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have recorded your join time and the session details for booking {{consultation_id}}, and we are reviewing your request with the consultant. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለቀጠሮ {{consultation_id}} የገቡበትን ሰዓት እና የምክክሩን ዝርዝር መዝግበናል፤ ጥያቄዎንም ከአማካሪው ጋር እያየን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Buyer requests a refund, extra session or compensation for lost time → **Senior Support / Supervisor**.
- Lateness was caused by a platform problem (link, display) → **Technical / Engineering** for the cause + **Senior Support / Supervisor** for the outcome.
- Seller and buyer disagree about join times → **Senior Support / Supervisor** with evidence.

## Resolution Procedure
1. Buyer joined (or the case is handed to the duration/no-show process).
2. Join time, reason and session length recorded.
3. Any outcome decided only by authorized staff.

## Policy Pending Approval
- Decide the grace period a seller must wait for a late buyer before the buyer is treated as a no-show.
- Decide whether a late buyer's session ends at the original end time, and whether sellers may extend.
- Decide whether buyer lateness affects refund eligibility.

## Internal Notes
- Never tell a late buyer "the consultant must wait" or "you'll still get the full time" — neither is an approved rule.
- If lateness was caused by our link or display problem, write that clearly in the ticket — it changes who is responsible.
- Kindness matters: late buyers are usually embarrassed and stressed.

<!-- doc -->
# Seller joined late
id: con-seller-late
type: article
category: consultations
subcategory: attendance
audience: buyer
priority: high
department: support_l2
features: consultations-1on1, google-meet
tags: seller late, consultant late, consultant not here yet, waiting for seller, seller hasn't joined, session started late, አማካሪው አልመጣም, አማካሪው ዘገየ, እየጠበቅሁ ነው
related: con-seller-no-show, con-cannot-join-meet, con-duration-dispute, con-tsg-no-show-decision-guide, con-time-zone-confusion
templates: tpl-waiting-for-seller, tpl-seller-contact-request, tpl-seller-no-show-ack
policy_pending: yes

## Summary
The buyer is in the meeting (or waiting to be admitted) and the consultant has not joined at the scheduled time, or the consultant joined late and the session was shortened.

## Issue Description
This is usually reported **live**: "It's time and the consultant isn't here." The buyer is anxious and may leave too early. Your job is to keep the buyer in the meeting, reach the seller quickly, and record the timeline. If the seller never comes, the case becomes a **seller no-show** (`con-seller-no-show`). If the seller joins late, the buyer may want the lost time back (`con-duration-dispute`).

## Possible Causes
- Seller is simply late (another session overran, transport, power, connection).
- Seller misread the time (Ethiopian clock / AM-PM / date) or has the booking at a different time.
- Seller is in a **different meeting** link and waiting too.
- Seller is in the meeting but has not seen/admitted the buyer's "Ask to join".
- Seller did not know about the booking (notification/dashboard problem — `con-seller-cannot-see-booking`).
- Seller forgot or is unavailable.

## Information to Collect
- Booking ID / consultant name, session time (EAT)
- Exact time the buyer joined/started waiting
- The link the buyer is using (to compare with the booking and with the seller's)
- What the buyer sees: empty meeting, or "Asking to join"
- Screenshot of the Meet screen with the time visible (phone status bar or computer clock)
- After the session: the time the seller actually joined and when the session ended

## Troubleshooting Steps
1. Confirm the buyer has the right time (restate in EAT and Ethiopian clock) and the correct link from the booking.
2. Ask the buyer to **stay in the meeting** and take a screenshot showing the meeting screen and the time.
3. Contact the seller immediately through the platform/registered contact (`tpl-seller-contact-request`). Ask: Are you joining? Which link are you in?
4. Update the buyer (`tpl-waiting-for-seller`) and keep updating them regularly.
5. If the seller is in a different meeting → make both use one link (`con-incorrect-meet-link`).
6. If the seller is in the meeting but the buyer is stuck in "Asking to join" → ask the seller to admit them (`con-cannot-join-meet`).
7. If the seller joins late → let the session run. Afterwards, ask the buyer whether the session was complete. If time was lost → `con-duration-dispute`.
8. If the seller does not join or respond by the end of the booked time → switch to `con-seller-no-show`; escalate to **Senior Support / Supervisor**.
9. Record the full timeline (EAT) in internal notes.

## Recommended Response (EN)
Hello {{customer_name}},

I'm sorry you're waiting. I am contacting {{seller_name}} right now about your session booked for {{booking_date}} at {{booking_time}} (EAT).

Please:
1. Stay in the meeting with your current link, so the consultant can find you.
2. Take a screenshot of the meeting screen showing the time — this helps us if we need to review what happened.

I will update you here as soon as I hear from the consultant. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

በመጠበቅዎ ይቅርታ እንጠይቃለን። ለ{{booking_date}} በ{{booking_time}} (EAT) ስለተያዘው ምክክርዎ {{seller_name}}ን አሁኑኑ እያገኘሁ ነው።

እባክዎ፦
1. አማካሪው እንዲያገኝዎ በአሁኑ ሊንክዎ ስብሰባው ውስጥ ይቆዩ።
2. ሰዓቱ የሚታይበትን የስብሰባ ገጽ ስክሪንሾት ያንሱ — የሆነውን ማጣራት ካስፈለገ ይጠቅመናል።

ከአማካሪው መልስ እንዳገኘሁ ወዲያውኑ እዚሁ አሳውቅዎታለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry for the wait! I'm contacting {{seller_name}} now. Please stay in the meeting and take a screenshot showing the time. I'll update you here shortly. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ መጠበቅዎ ይቅርታ! {{seller_name}}ን አሁኑኑ እያገኘሁ ነው። እባክዎ ስብሰባው ውስጥ ይቆዩ እና ሰዓቱ የሚታይበትን ስክሪንሾት ያንሱ። በቅርቡ እዚሁ መረጃ እሰጥዎታለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have recorded that {{seller_name}} joined late for your session {{consultation_id}}, and we are reviewing how much session time was affected. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። {{seller_name}} ለምክክርዎ {{consultation_id}} ዘግይተው መግባታቸውን መዝግበናል፤ የምክክሩ ጊዜ ምን ያህል እንደተነካ እያጣራን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Seller unreachable at session time → **Senior Support / Supervisor**, priority High (Critical while the buyer is waiting).
- Seller joined late and the buyer asks for a refund/extra session → **Senior Support / Supervisor**.
- Repeated lateness by the same seller → **Seller Operations** (pattern).
- The seller did not know about the booking because of a platform problem → **Technical / Engineering** + note for the outcome decision.

## Resolution Procedure
1. Seller joined and the session took place, or the case moved to the no-show process.
2. Timeline recorded: buyer joined, seller contacted, seller responded, seller joined, session ended.
3. Any lost-time claim is handled as a duration dispute, not closed here.

## Policy Pending Approval
- Decide how long a buyer is expected to wait before a late seller is treated as a no-show.
- Decide whether a late seller must give the full booked duration, a make-up session, or a partial refund.
- Decide consequences for sellers who are repeatedly late.

## Internal Notes
- Do not tell the buyer to leave the meeting — leaving early weakens their evidence.
- Do not say "the seller is a no-show" while the session time is still running.
- Write down exact times as they happen. Memory after the fact is unreliable for both parties.

<!-- doc -->
# Seller didn't join the consultation
id: con-seller-no-show
type: article
category: consultations
subcategory: attendance
audience: buyer
priority: high
department: support_l2
features: consultations-1on1, google-meet, refunds
tags: seller no show, consultant didn't join, consultant never came, paid but no session, seller absent, I waited but nobody came, አማካሪው አልመጣም, ከፍዬ ምክክሩ አልተካሄደም, ሻጩ አልገባም, ጠብቄ ማንም አልመጣም
related: con-tsg-no-show-decision-guide, con-seller-late, con-time-zone-confusion, ref-consultation-refunds, ref-evidence-collection, con-incorrect-meet-link
templates: tpl-seller-no-show-ack, tpl-seller-contact-request, tpl-waiting-for-seller, tpl-request-booking-details
policy_pending: yes

## Summary
The buyer paid for a consultation, but the consultant did not join the meeting — e.g., "I paid for a consultation, but the seller didn't join the meeting." Collect evidence from both sides before any outcome; all outcomes are policy pending.

## Issue Description
The buyer was ready at the scheduled time, but the seller never appeared. The buyer feels cheated and wants their money back or a new session. This is one of the most important trust moments on Byfluence: the buyer must feel heard and protected, and the seller must be treated fairly until the facts are known.

> [!WARNING] A scheduled meeting does not prove the session was delivered — but a buyer's statement alone does not prove a no-show either. Many "no-shows" turn out to be time-zone confusion, two different meeting links, or a buyer stuck on "Ask to join". **Collect evidence from both sides. Never promise a refund or a new session.**

## Possible Causes
- The seller genuinely missed the session (forgot, emergency, power/connection failure).
- The seller did not know about the booking (notification/dashboard failure).
- **Time confusion**: one side came at the Ethiopian-clock time, the other at the international time, or on a different date.
- **Two different links**: each side waited in a different meeting.
- The seller was in the meeting but did not admit the buyer from "Ask to join".
- The buyer joined at the wrong time or with an old link.
- The booking had been cancelled or rescheduled and the buyer did not see it.

## Information to Collect
**From the buyer**
- Booking ID or consultant name + session date/time (as they understood it)
- Exact time they joined and how long they waited (EAT)
- The link they used (copy-paste)
- Screenshot(s) of the Meet screen showing the meeting code and the time (empty meeting or "Asking to join")
- Any messages sent to the seller or support during the wait

**From the seller** (`tpl-seller-contact-request`)
- Whether they joined, at what time, and with which link
- Any evidence: screenshots, calendar event, Meet history; if their Google account offers meeting attendance reports, a copy of it
- Reason, if they missed it

**From the system** (authorized tools)
- Booking status, payment status, time stored on the booking, the Meet link on record
- Any cancellation/reschedule actions and who made them
- Any support contacts during the session window (ticket timestamps)
- The seller's history of no-shows/cancellations

## Troubleshooting Steps
1. **Is the session time still running?** If yes, this is a late seller → `con-seller-late` (contact the seller now, keep the buyer in the meeting).
2. **Verify identity and the booking** (status confirmed, paid, not cancelled/rescheduled). If cancelled/rescheduled → matching changes article.
3. **Check time understanding**: restate the booking time in both clocks and the weekday. If the buyer came about six hours early/late or on another day → `con-time-zone-confusion`.
4. **Check the link**: does the buyer's link match the one on the booking?
5. **Acknowledge the buyer** with `tpl-seller-no-show-ack` and collect the buyer's evidence.
6. **Contact the seller** and request their account and evidence. Give them a clear deadline using approved wording (`{{follow_up_time}}`).
7. **Assess the scenario** using `con-tsg-no-show-decision-guide` (seller absent / both waited in different links / not admitted / time confusion / seller unaware).
8. **Escalate to Senior Support / Supervisor** with an evidence pack: timeline, both statements, screenshots, booking record, seller history. Mark the booking as disputed in the ticket and inform **Payments & Finance** that the booking is under dispute (whether earnings are held is policy pending).
9. **Update the buyer** regularly. Explain the case is under review; do not predict the outcome.
10. **Record** everything in the ticket. Do not close until an authorized decision is communicated.

- [ ] Session time over (not a live late case)
- [ ] Booking/payment status verified
- [ ] Time zone and link checked
- [ ] Buyer evidence collected
- [ ] Seller contacted and response recorded
- [ ] Escalated with evidence pack
- [ ] Payments informed of dispute

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I'm very sorry that your consultation with {{seller_name}} on {{booking_date}} at {{booking_time}} (EAT) did not happen as expected. I understand how disappointing this is after you paid and made time for it.

Your case is now open and recorded. To review it fairly, please send me:
1. The time you joined the meeting and how long you waited
2. The meeting link you used (please copy and paste it)
3. Any screenshots of the meeting screen showing the time
4. Any messages you exchanged with the consultant

We are also contacting the consultant to hear their side. Our team will review the information from both sides and let you know the outcome.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በ{{booking_date}} በ{{booking_time}} (EAT) ከ{{seller_name}} ጋር የነበረዎት ምክክር እንደተጠበቀው ስላልተካሄደ ከልብ ይቅርታ እንጠይቃለን። ከፍለው ጊዜዎን ሰጥተው ሲጠብቁ እንዲህ መሆኑ ምን ያህል እንደሚያሳዝን ይገባኛል።

ጉዳይዎ ተከፍቶ ተመዝግቧል። በፍትሃዊነት ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ወደ ስብሰባው የገቡበትን ሰዓት እና ምን ያህል እንደጠበቁ
2. የተጠቀሙበትን የስብሰባ ሊንክ (እባክዎ ኮፒ አድርገው ይለጥፉት)
3. ሰዓቱ የሚታይበት የስብሰባ ገጽ ስክሪንሾት ካለዎት
4. ከአማካሪው ጋር የተለዋወጧቸው መልዕክቶች ካሉ

የአማካሪውንም ሃሳብ ለመስማት እያገኘናቸው ነው። ቡድናችን ከሁለቱም ወገን የተገኘውን መረጃ አጣርቶ ውጤቱን ያሳውቅዎታል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I'm very sorry your session didn't happen. Your case is recorded. Please send the time you joined, the link you used, and any screenshots showing the time. We're also contacting the consultant and will review both sides. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ምክክርዎ ስላልተካሄደ ከልብ ይቅርታ እንጠይቃለን። ጉዳይዎ ተመዝግቧል። እባክዎ የገቡበትን ሰዓት፣ የተጠቀሙበትን ሊንክ እና ሰዓቱ የሚታይበት ስክሪንሾት ይላኩ። አማካሪውንም እያገኘን ነው፤ የሁለቱንም ወገን መረጃ እናጣራለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}} about your consultation {{consultation_id}} with {{seller_name}}. We have received your information and contacted the consultant. Our team is reviewing the case and we will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ከ{{seller_name}} ጋር ስለነበረዎት ምክክር {{consultation_id}} (ጉዳይ ቁጥር {{ticket_id}}) የሚሰጥ መረጃ ነው። የላኩልንን መረጃ ተቀብለናል፤ አማካሪውንም አግኝተናል። ቡድናችን ጉዳዩን እያጣራ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Every confirmed seller no-show claim (session time passed) → **Senior Support / Supervisor**, priority High, with the evidence pack.
- Seller does not respond to support → **Senior Support / Supervisor**; repeated non-response → **Seller Operations**.
- Seller has prior no-shows or multiple buyers report the same seller → **Seller Operations** (and **Trust & Safety** if it looks like taking payments without delivering).
- Seller did not know about the booking due to a platform failure → **Technical / Engineering** (cause) + Senior Support (outcome).
- Refund or payment adjustment approved → **Payments & Finance** processes it (only after authorized decision).

## Resolution Procedure
1. An authorized decision has been made (by Senior Support / Supervisor or higher, per policy).
2. The outcome is communicated to the buyer and the seller, using approved wording.
3. Any approved rebooking or payment adjustment is confirmed as completed.
4. The ticket records: scenario type, evidence summary, both statements, decision, decision-maker, actions.

## Policy Pending Approval
- Decide the outcomes for a confirmed seller no-show (full refund, rebooking, credit) and who approves them.
- Decide the evidence standard needed to confirm a seller no-show when the seller disputes it.
- Decide whether seller earnings for a disputed booking are automatically held, and how.
- Decide the deadline for a seller to respond to a no-show claim, and what happens if they do not.
- Decide seller consequences for no-shows (warning, suspension thresholds).
- Decide the deadline for buyers to report a no-show after the session.

## Internal Notes
- Lead with empathy, then evidence. Do not sound like you doubt the buyer — explain that you collect both sides for every case.
- Ask for evidence **early**: screenshots and memories fade, and Meet history may not be retained.
- Never share the seller's personal contact details with the buyer, or the buyer's with the seller.
- If the seller admits the no-show and offers a new time, you may tell the buyer about the offer, but the buyer is free to choose; if the buyer refuses and wants a refund, escalate — don't push the rebooking.
- Fraud signal: a new seller with several paid bookings and repeated no-shows → Trust & Safety immediately.

<!-- doc -->
# Buyer didn't attend (seller reports)
id: con-buyer-no-show
type: article
category: consultations
subcategory: attendance
audience: seller
priority: medium
department: support_l2
features: consultations-1on1, google-meet, seller-withdrawals
tags: buyer no show, buyer didn't come, client didn't join, buyer absent, will I get paid, mark completed no show, ገዢው አልመጣም, ደንበኛው አልገባም, ይከፈለኛል ወይ
related: con-tsg-no-show-decision-guide, con-buyer-late, con-completion-confirmation, out-pending-vs-available, con-time-zone-confusion, ref-evidence-collection
templates: tpl-buyer-no-show-explain, tpl-request-booking-details, tpl-seller-contact-request
policy_pending: yes

## Summary
A seller reports that the buyer did not attend the booked consultation and asks whether the session counts and whether they will be paid. Also covers the buyer side when they later say they could not attend.

## Issue Description
The seller joined at the scheduled time and waited, but the buyer never appeared. The seller is concerned about their time and earnings. Often, the buyer contacts support separately — sometimes with a valid reason (missing link, access problem, time confusion) — so the facts must come from both sides before anyone is labelled a no-show.

## Possible Causes
- The buyer forgot or chose not to attend.
- The buyer had no link or the wrong link (platform or seller-side issue).
- The buyer was stuck on "Asking to join" and the seller did not see the request.
- Time confusion (Ethiopian clock / AM-PM / date / time zone abroad).
- The buyer had a connection or power problem.
- The buyer believed they had cancelled or rescheduled.

## Information to Collect
**From the seller**
- Booking ID, session date/time
- Time they joined and how long they waited (EAT)
- The link they used
- Screenshots of the meeting showing the time and no participant / no join requests
- Any messages to the buyer through the platform

**From the buyer** (contact them neutrally — `tpl-buyer-no-show-explain`)
- Whether they tried to join, when, and with which link
- Any problems they had (link, access, time)
- Screenshots if available

**From the system**
- Booking and payment status; link on record; any cancellation/reschedule requests; support contacts by the buyer around the session time

## Troubleshooting Steps
1. Verify the seller and the booking; confirm it was not cancelled or rescheduled.
2. Collect the seller's evidence.
3. Check for buyer support contacts around the session time (missing link, access problem). If the buyer contacted support → the "no-show" may be a platform/access problem; follow that article.
4. Contact the buyer neutrally: "We noticed you may not have been able to join — did anything go wrong?" Do not accuse.
5. Assess the scenario with `con-tsg-no-show-decision-guide`.
6. If both sides agree to a new time → `con-reschedule-request-buyer` (record that both agreed).
7. If the seller asks to be paid / mark complete, or the buyer asks for a refund → escalate to **Senior Support / Supervisor** with the evidence. Do not tell the seller they will (or won't) be paid.
8. Tell the seller how earnings normally work: earnings stay pending until release conditions are met (`out-pending-vs-available`) — without giving timelines.
9. Record everything.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know, and for waiting for your buyer. I'm sorry the session on {{booking_date}} at {{booking_time}} (EAT) did not take place.

To review this, please send me:
1. The time you joined and how long you waited
2. The meeting link you used
3. Screenshots of the meeting screen showing the time
4. Any messages you sent to the buyer

We will also check with the buyer whether they had any problem joining. Your earnings for this booking will be handled according to Byfluence's settlement process once the review is complete — we will let you know the outcome.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እና ገዢዎን ስለጠበቁ እናመሰግናለን። በ{{booking_date}} በ{{booking_time}} (EAT) የነበረው ምክክር ባለመካሄዱ ይቅርታ እንጠይቃለን።

ጉዳዩን ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ወደ ስብሰባው የገቡበትን ሰዓት እና ምን ያህል እንደጠበቁ
2. የተጠቀሙበትን የስብሰባ ሊንክ
3. ሰዓቱ የሚታይበት የስብሰባ ገጽ ስክሪንሾት
4. ለገዢው የላኳቸው መልዕክቶች ካሉ

ገዢውም ለመግባት ችግር አጋጥሞት እንደሆነ እናጣራለን። የዚህ ቀጠሮ ገቢዎ ማጣራቱ ሲጠናቀቅ በByfluence የክፍያ አሰራር መሰረት ይስተናገዳል — ውጤቱን እናሳውቅዎታለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for waiting and for telling us. Please send your join time, the link you used and screenshots showing the time. We'll check with the buyer too and update you on the outcome. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለጠበቁ እና ስላሳወቁን እናመሰግናለን። እባክዎ የገቡበትን ሰዓት፣ የተጠቀሙበትን ሊንክ እና ሰዓቱ የሚታይበት ስክሪንሾት ይላኩ። ገዢውንም እናጣራለን፤ ውጤቱን እናሳውቅዎታለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}} for booking {{consultation_id}}. We have your information and have contacted the buyer. The case is under review, and we will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ቀጠሮ {{consultation_id}} (ጉዳይ ቁጥር {{ticket_id}}) የሚሰጥ መረጃ ነው። የላኩልንን መረጃ ተቀብለናል፤ ገዢውንም አግኝተናል። ጉዳዩ እየተጣራ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Seller asks for payment/completion, or buyer asks for a refund → **Senior Support / Supervisor**.
- Evidence suggests a platform failure prevented the buyer from joining → **Technical / Engineering** + Senior Support.
- Seller pressures the buyer for payment outside Byfluence or threatens them → **Trust & Safety**.

## Resolution Procedure
1. Authorized decision made and communicated to both sides, or a new time agreed by both.
2. Booking status updated by authorized staff (completed / rescheduled / other).
3. Ticket records evidence from both sides and the decision.

## Policy Pending Approval
- Decide whether a seller is paid for a buyer no-show, fully or partly, and the evidence required.
- Decide how long a seller must wait before a buyer is a no-show.
- Decide whether buyers can request a reschedule after missing a session.

## Internal Notes
- Always check for buyer support contacts around the session time before treating it as a buyer no-show.
- Don't share the buyer's personal contact with the seller.
- Sellers may be anxious about earnings; explain the process calmly without timelines.

<!-- doc -->
# Decision guide: no-shows, lateness and incomplete sessions
id: con-tsg-no-show-decision-guide
type: troubleshooting
category: consultations
subcategory: attendance
audience: internal
priority: high
department: support_l2
features: consultations-1on1, consultations-group, google-meet, refunds
tags: no show decision, attendance dispute, who is responsible, evidence checklist, missed session, late session, incomplete session, ያልተካሄደ ምክክር, ማስረጃ, ክርክር
related: con-seller-no-show, con-buyer-no-show, con-seller-late, con-buyer-late, con-incomplete-consultation, ref-evidence-collection
templates: tpl-seller-no-show-ack, tpl-buyer-no-show-explain, tpl-seller-contact-request, tpl-waiting-for-seller
policy_pending: yes

## Summary
A structured guide for classifying attendance problems (no-shows, lateness, interrupted or shortened sessions), the evidence to collect for each, and who decides. All outcome rules are pending management approval.

## Overview
Attendance disputes are where buyers lose trust and sellers lose earnings. Support's job is to **classify the scenario, collect evidence from both sides, and route the case** — not to decide refunds or penalties. The decision is made by authorized staff (Senior Support / Supervisor, with Payments & Finance and Management as needed) under policy that is not yet approved.

> [!POLICY] Every outcome in this guide (refund, partial refund, rebooking, seller payment, penalty) is **policy pending approval**. Until rules are approved, escalate every disputed case to Senior Support / Supervisor and never promise an outcome.

### Evidence standards (use for every scenario)
| Evidence | Strength | Notes |
|---|---|---|
| Platform records (booking status, link on record, cancellations, timestamps) | Strong | Check via authorized tools. Join tracking may not exist — confirm with Technical. |
| Support ticket timestamps (customer contacted support during the session) | Strong | Shows the person was present and trying at that time. |
| Screenshots of the Meet screen with meeting code **and** device clock visible | Medium | Can be edited; check consistency with other evidence. |
| Meeting attendance report from the organizer's Google account (if their plan offers it) | Strong | Not available for every Google account — never promise it exists. |
| Messages between the parties (on the platform) | Medium | Look at times and tone. |
| Written statements from both sides | Weak alone | Collect promptly; compare details (link, time, what they saw). |
| History/pattern (seller's past no-shows, buyer's past claims) | Context | Patterns go to Seller Operations / Trust & Safety. |

## Information to Collect
- Booking ID, consultant, buyer, session date/time as stored (and how each side understood it)
- Both parties' join times, links used, screenshots and messages
- Support contacts during the session window
- Booking change history (cancel/reschedule) and who made each change
- Payment status and any prior disputes on this booking

## Troubleshooting Steps
### Step 1 — Is it live?
If the session time is still running, it is a **live attendance problem**: use `con-seller-late` / `con-buyer-late` / `con-cannot-join-meet`. Do not classify it as a no-show yet.

### Step 2 — Rule out the "nobody's fault" causes first
1. **Time confusion** — did either side act on a different time (Ethiopian clock, AM/PM, date, abroad)? → `con-time-zone-confusion`.
2. **Two links** — were they in different meetings? → `con-incorrect-meet-link`.
3. **Not admitted** — was the buyer stuck on "Asking to join" while the seller was inside? → `con-cannot-join-meet`.
4. **Platform failure** — no link, broken link, booking not visible to seller, wrong display time? → Technical.

### Step 3 — Classify using the decision table
| # | Scenario | Evidence to collect | First actions | Who decides the outcome |
|---|---|---|---|---|
| 1 | Seller never joined; buyer was present | Buyer join time + screenshots; support contacts; seller's account | Acknowledge buyer (`tpl-seller-no-show-ack`); contact seller (`tpl-seller-contact-request`); inform Payments of dispute | Senior Support / Supervisor (policy pending) |
| 2 | Seller joined late; session shortened | Both join times; actual session end; buyer's statement of what was lost | Ask buyer if session was completed; record lost time | Senior Support / Supervisor |
| 3 | Buyer never joined; seller was present | Seller join time + screenshots; check buyer support contacts; buyer's account | Contact buyer neutrally (`tpl-buyer-no-show-explain`) | Senior Support / Supervisor |
| 4 | Buyer joined late | Both join times; reason; whether a platform issue caused it | Check link/time issues first | Senior Support / Supervisor (if disputed) |
| 5 | Both say they were there | Links used by each; meeting codes on screenshots; admit requests | Compare links; check "Ask to join" | Senior Support / Supervisor; Technical if the platform link was faulty |
| 6 | Both missed it (time confusion) | How each understood the time; how it was displayed | Offer to help arrange a new time if both agree | Senior Support / Supervisor if either wants a refund |
| 7 | Session started but interrupted (connection/power) | Who lost connection, when, for how long; rejoin attempts | `con-meeting-connection-problems` → `con-incomplete-consultation` | Senior Support / Supervisor |
| 8 | Seller ended the session early | Session start/end times; seller's reason; buyer's statement | `con-duration-dispute` | Senior Support / Supervisor |
| 9 | Missing/broken link prevented the session | Support contact times; link on record; who was responsible for the link | `con-missing-meet-link`; Technical if automatic | Senior Support / Supervisor (+ Technical findings) |
| 10 | Seller cancelled at the last minute | Cancellation time and reason | `con-cancellation-by-seller` | Senior Support / Supervisor |
| 11 | Group session: one participant could not join, others did | Participant's join attempts; seller's view; other participants' attendance | `grp-participant-access-denied` / `grp-partial-attendance` | Senior Support / Supervisor |

### Step 4 — Build the evidence pack and escalate
Include: scenario number, timeline in EAT, both statements, screenshots, platform records, support contacts, history. Mark the booking as disputed in the ticket and notify **Payments & Finance** that a dispute exists.

### Step 5 — Communicate while waiting
Use the follow-up responses in the scenario articles. Tell both sides the case is under review; never predict the outcome.

## Escalation Conditions
- Any disputed attendance case after the session time → **Senior Support / Supervisor**.
- Platform failure involved → **Technical / Engineering** for root cause.
- Approved refunds or payment adjustments → **Payments & Finance** (only after decision).
- Pattern of seller no-shows or suspected taking payment without delivering → **Seller Operations** / **Trust & Safety**.
- High-value, reputational or repeated disputes → **Management**.

## Resolution Procedure
1. Scenario classified and evidence pack complete.
2. Decision made by authorized staff and recorded with decision-maker name.
3. Both parties informed; approved actions completed and confirmed.
4. Root cause tagged (time confusion / two links / not admitted / platform failure / seller absent / buyer absent / connection).

## Policy Pending Approval
- Approve outcome rules for each scenario in the decision table (refund, partial refund, rebooking, credit, seller payment).
- Approve grace periods for late buyers and late sellers.
- Approve the evidence standard for disputed cases and the deadline for each side to respond.
- Approve how seller earnings are handled while an attendance dispute is open.
- Approve seller performance consequences for no-shows and repeated lateness.
- Approve the reporting deadline for buyers and sellers after a missed session.

## Internal Notes
- In practice most disputes are scenarios 5 and 6 — confusion, not bad faith. Check those first, and use calm, neutral language with both sides.
- Ask for evidence immediately; it disappears quickly.
- Never tell one party what the other party said word for word; summarise neutrally.
- Track root-cause tags carefully — management needs them to write the missing policies.
