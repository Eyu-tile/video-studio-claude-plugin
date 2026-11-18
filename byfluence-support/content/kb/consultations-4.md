<!-- doc -->
# Buyer wants to reschedule
id: con-reschedule-request-buyer
type: article
category: consultations
subcategory: changes
audience: buyer
priority: medium
department: support_l1
features: consultations-1on1
tags: reschedule, change time, move my session, change date, can't make it, postpone consultation, ቀጠሮ መቀየር, ሰዓት መቀየር, ቀጠሮውን ማዛወር
related: con-reschedule-request-seller, con-cancellation-by-buyer, con-select-time-slot, con-time-zone-confusion, con-missing-meet-link
templates: tpl-reschedule-request, tpl-request-booking-details, tpl-seller-contact-request
policy_pending: yes

## Summary
The buyer cannot attend at the booked time and asks to move the consultation to another date or time.

## Issue Description
The buyer has a confirmed (paid) booking but something has come up. They may ask before the session, at the last minute, or even after missing it. Whether buyers can reschedule by themselves in the dashboard, how late they can do it, and how many times are **not confirmed**. Until rules are approved, a reschedule needs the seller's agreement and must be recorded.

## Possible Causes
- Personal conflict (work, travel, illness, family event, holiday).
- The buyer realised they booked the wrong time (time-zone or Ethiopian clock mistake).
- Expected power or internet problem at the booked time.
- The buyer missed the session and wants another chance (treat via the no-show guide).

## Information to Collect
- Booking ID or consultant name + current session date/time
- Reason (optional, but helps the seller agree)
- Two or three preferred new dates/times — **ask the buyer to state them in EAT international time; confirm with Ethiopian clock and weekday**
- When the request was made (record the timestamp — any future deadline rule will depend on it)

## Troubleshooting Steps
1. Verify identity and find the booking; confirm it is confirmed and not in the past.
   - Session already passed → this is not a reschedule; follow `con-tsg-no-show-decision-guide` (scenario 3 or 4).
2. Check whether the dashboard offers a reschedule action for this booking. If yes, guide the buyer; confirm the new time appears.
3. If not self-service: ask for preferred new times (in EAT + Ethiopian clock) and the seller's open availability.
4. Contact the seller with `tpl-reschedule-request`, including the buyer's options.
   - **Seller agrees** → the change is made by the authorized party (seller or admin — process pending). Confirm the new date/time with both sides in both clocks and make sure the meeting link is correct for the new time.
   - **Seller cannot offer any suitable time** → tell the buyer; if they then want to cancel → `con-cancellation-by-buyer`.
   - **Seller does not respond** → follow up; if the original session is close → **Senior Support / Supervisor**.
5. If the request is very close to the session start → priority High; tell the buyer the original booking stands unless the change is confirmed.
6. Record: request time, options, seller response, final time.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know in advance. I've noted your request to reschedule your consultation with {{seller_name}}, currently booked for {{booking_date}} at {{booking_time}} (EAT).

Please send me two or three dates and times that suit you. To avoid confusion, please write the times in East Africa Time on the international clock (for example, 2:00 PM, which is ከሰዓት 8 ሰዓት in Ethiopian time).

I will check with the consultant and confirm. Until the change is confirmed, your original booking remains in place. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

አስቀድመው ስላሳወቁን እናመሰግናለን። በአሁኑ ጊዜ ለ{{booking_date}} በ{{booking_time}} (EAT) ከ{{seller_name}} ጋር የተያዘውን ምክክርዎን ለመቀየር ያቀረቡትን ጥያቄ መዝግቤያለሁ።

እባክዎ የሚመችዎትን ሁለት ወይም ሶስት ቀን እና ሰዓት ይላኩልኝ። መምታታትን ለማስቀረት፣ ሰዓቶቹን በምሥራቅ አፍሪካ ሰዓት እና በፈረንጅ አቆጣጠር ይጻፉ፤ ከፈለጉ የኢትዮጵያውንም አቆጣጠር ይጨምሩ (ለምሳሌ 2:00 PM፣ ማለትም ከሰዓት 8 ሰዓት)።

ከአማካሪው ጋር አጣርቼ አረጋግጥልዎታለሁ። ለውጡ እስኪረጋገጥ ድረስ የመጀመሪያው ቀጠሮዎ እንዳለ ይቆያል። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, noted! Please send 2–3 new dates/times (EAT, international clock). I'll check with {{seller_name}} and confirm. Your current booking stays in place until the change is confirmed. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ተመዝግቧል! እባክዎ 2–3 አዲስ ቀን/ሰዓት (በEAT፣ በፈረንጅ አቆጣጠር) ይላኩ። ከ{{seller_name}} ጋር አጣርቼ አረጋግጣለሁ። ለውጡ እስኪረጋገጥ የአሁኑ ቀጠሮዎ ይቆያል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are still waiting for {{seller_name}} to confirm a new time for booking {{consultation_id}}. Your original booking remains in place for now. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለቀጠሮ {{consultation_id}} አዲስ ሰዓት እንዲያረጋግጡ ከ{{seller_name}} መልስ እየጠበቅን ነው። ለጊዜው የመጀመሪያው ቀጠሮዎ እንዳለ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Seller refuses and the buyer asks for a refund → **Senior Support / Supervisor** (`con-cancellation-by-buyer`).
- Seller does not respond and the session is close → **Senior Support / Supervisor**.
- Reschedule action in the dashboard fails → **Technical / Engineering**.
- Buyer has rescheduled repeatedly and the seller complains → **Senior Support / Supervisor**.

## Resolution Procedure
1. New time confirmed in the system and acknowledged by both parties, in EAT + Ethiopian clock.
2. Meeting link checked for the new time.
3. Ticket records request time, reason, agreed time, who made the change.

## Policy Pending Approval
- Decide whether buyers can reschedule by themselves, up to what point before the session, and how many times.
- Decide whether the seller must accept a reschedule request made with enough notice.
- Decide what happens if no new time is agreed (cancel, refund, credit).
- Confirm who is authorized to change a booking time in the system.

## Internal Notes
- Never confirm a new time until the seller has agreed and the booking is actually changed.
- Write the request timestamp in the ticket — it will matter once notice-period rules exist.
- Watch for time-confusion reschedules: a buyer who "wants to change" may actually have misread the original time.

<!-- doc -->
# Seller needs to reschedule
id: con-reschedule-request-seller
type: article
category: consultations
subcategory: changes
audience: both
priority: high
department: support_l1
features: consultations-1on1
tags: seller reschedule, consultant wants to change time, seller can't attend, move booking seller, seller emergency, አማካሪው ሰዓት መቀየር ይፈልጋል, ሻጩ መገኘት አይችልም
related: con-reschedule-request-buyer, con-cancellation-by-seller, con-seller-no-show, con-seller-availability-setup, con-time-zone-confusion
templates: tpl-reschedule-request, tpl-seller-contact-request, tpl-request-booking-details
policy_pending: yes

## Summary
A seller cannot attend a confirmed booking and asks to move it, or a buyer reports that the seller asked them to change the time.

## Issue Description
The seller has an emergency or conflict. The buyer has already paid and planned their time, so **the buyer must agree** to any new time. A seller who cannot attend should tell Byfluence as early as possible instead of simply not appearing. Sometimes the buyer contacts support first because the seller messaged them about a change.

## Possible Causes
- Emergency, illness, travel, double booking.
- The seller set availability wrongly (e.g., in Ethiopian clock) and the booked time is not what they intended.
- Expected power/internet outage.
- Seller's availability changed after the booking was made.

## Information to Collect
- Seller identity; booking ID; current session date/time
- Reason (kept internal unless the seller agrees to share a general reason)
- Two or three alternative times from the seller (EAT, international clock)
- Time of the request (record it)
- If the buyer reports it: the message they received (screenshot) — check it really came from the seller through the platform

## Troubleshooting Steps
1. Verify the seller and the booking; confirm the session has not passed. If it has → `con-seller-no-show`.
2. Ask the seller for alternative times (in EAT; confirm Ethiopian clock).
3. Contact the buyer with `tpl-reschedule-request`: explain the seller has asked to reschedule, offer the alternatives, and make clear the buyer can decline.
   - **Buyer accepts** → change made by the authorized party; confirm the new time with both in both clocks; check the meeting link.
   - **Buyer declines / none suit** → treat as a seller cancellation: `con-cancellation-by-seller` and escalate to **Senior Support / Supervisor** for the outcome (policy pending).
   - **Buyer does not respond and the session is close** → the original booking stands; tell the seller they are expected to attend unless the change is confirmed or a supervisor decides otherwise.
4. If the seller's request is a pattern (several reschedules) → note for **Seller Operations**.
5. If the "seller" message asks the buyer to pay extra or pay outside Byfluence → **Trust & Safety**.
6. Record all times and responses.

## Recommended Response (EN)
Hello {{customer_name}},

We're contacting you about your consultation {{consultation_id}}, booked for {{booking_date}} at {{booking_time}} (EAT). Unfortunately, {{seller_name}} is unable to attend at that time and has asked to reschedule. We're sorry for the inconvenience.

The consultant has offered these times (East Africa Time, international clock):
- [option 1]
- [option 2]
- [option 3]

Please reply with the option that suits you. If none of these work for you, just let us know and we will review the next steps with you. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ለ{{booking_date}} በ{{booking_time}} (EAT) ስለተያዘው ምክክርዎ {{consultation_id}} ልናሳውቅዎ ነው። እንደ አለመታደል ሆኖ {{seller_name}} በዚያ ሰዓት መገኘት ስለማይችሉ ቀጠሮውን ለመቀየር ጠይቀዋል። ለተፈጠረው ችግር ይቅርታ እንጠይቃለን።

አማካሪው ያቀረቧቸው ሰዓቶች (በምሥራቅ አፍሪካ ሰዓት፣ በፈረንጅ አቆጣጠር)፦
- [አማራጭ 1 — በኢትዮጵያ አቆጣጠርም ይጻፉ]
- [አማራጭ 2]
- [አማራጭ 3]

እባክዎ የሚመችዎትን አማራጭ ይንገሩን። አንዳቸውም የማይመቹዎት ከሆነ፣ ያሳውቁን፤ ቀጣዩን ደረጃ ከእርስዎ ጋር እናያለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry — {{seller_name}} can't attend on {{booking_date}} at {{booking_time}} EAT and has offered new times: [options]. Please reply with one that suits you, or tell us if none do. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ — {{seller_name}} በ{{booking_date}} በ{{booking_time}} EAT መገኘት ስለማይችሉ አዲስ ሰዓቶችን አቅርበዋል፦ [አማራጮች]። የሚመችዎትን ይንገሩን፣ ወይም አንዳቸውም ካልተመቹ ያሳውቁን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are still arranging a new time for consultation {{consultation_id}} with {{seller_name}}. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ከ{{seller_name}} ጋር ላለዎት ምክክር {{consultation_id}} አዲስ ሰዓት እያመቻቸን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Buyer declines the new times or asks for a refund → **Senior Support / Supervisor**.
- Last-minute seller reschedule (session imminent) → **Senior Support / Supervisor**, High.
- Seller reschedules repeatedly → **Seller Operations**.
- Reschedule message asks for extra/off-platform payment → **Trust & Safety**.

## Resolution Procedure
1. Buyer accepted a new time and the booking is updated; both confirmed in EAT + Ethiopian clock; link checked.
2. Or: case handed to the cancellation process with buyer's decision recorded.
3. Ticket records request time, reason (internal), options, buyer decision.

## Policy Pending Approval
- Decide the minimum notice a seller must give to reschedule, and consequences for late requests.
- Decide the buyer's options when they decline a seller reschedule (refund, credit, choose another consultant).
- Decide how many seller-initiated reschedules are acceptable before Seller Operations reviews the seller.

## Internal Notes
- Phrase it as the seller's request — never pressure the buyer to accept.
- Don't share personal reasons (health, family) without the seller's consent.
- If the seller simply asks support to "cancel it", treat as `con-cancellation-by-seller`.

<!-- doc -->
# Buyer wants to cancel
id: con-cancellation-by-buyer
type: article
category: consultations
subcategory: changes
audience: buyer
priority: medium
department: support_l2
features: consultations-1on1, refunds
tags: cancel booking, cancel consultation, I want to cancel, cancel and refund, don't need session anymore, ቀጠሮ መሰረዝ, ምክክሩን መሰረዝ እፈልጋለሁ, ገንዘቤ ይመለስልኝ
related: con-reschedule-request-buyer, con-refund-eligibility, ref-consultation-refunds, ref-how-to-request-refund, con-cancellation-by-seller
templates: tpl-consultation-cancellation-ack, tpl-reschedule-request, tpl-request-booking-details
policy_pending: yes

## Summary
The buyer wants to cancel a paid consultation booking, usually with a refund request. Refund eligibility and cancellation deadlines are not yet approved — record the request and escalate; never promise a refund.

## Issue Description
The buyer no longer wants or cannot attend the session. They usually ask "Can I get my money back?". The cancellation rules — deadlines, deductions, who approves — **have not been set**. Support's role is to record the request accurately (especially **when** it was made), offer a reschedule as an option without pressure, and pass the case to authorized staff.

## Possible Causes
- Change of plans, emergency, no longer needs the help.
- Booked by mistake (wrong consultant, wrong time, duplicate booking).
- Lost trust in the seller (e.g., after reading something, or seller behaviour in messages).
- Previous problems (reschedule refused, no link).

## Information to Collect
- Booking ID or consultant + date/time
- Reason for cancelling
- Whether the buyer would accept a reschedule instead
- Payment method and transaction reference (for any refund later)
- Exact date/time of the cancellation request (recorded automatically on the ticket — note it)

> [!WARNING] Never ask for PINs, passwords, codes or full card numbers. For refunds, the transaction reference is enough.

## Troubleshooting Steps
1. Verify identity and find the booking. Note the time remaining until the session.
2. Check for special cases:
   - **Duplicate booking / paid twice** → Payments & Finance (`pay-duplicate-charge` flow).
   - **Session already passed** → this is a dispute/no-show, not a cancellation → `con-tsg-no-show-decision-guide`.
   - **Booking was never confirmed** → payment articles.
   - **Cancelling because of seller behaviour** → note details; if harassment or fraud → Trust & Safety.
3. Ask (once, without pressure) whether a new time would help → `con-reschedule-request-buyer`.
4. If they still want to cancel, check whether the dashboard offers a cancel action; guide them only if approved for use.
5. Acknowledge with `tpl-consultation-cancellation-ack`. Inform the seller that the buyer has requested cancellation (so they don't wait at the session time).
6. Escalate the refund request to **Senior Support / Supervisor** with: booking, payment reference, request time, reason, time remaining before the session. Refund processing (if approved) goes to **Payments & Finance**.
7. Do not mark the booking cancelled yourself unless authorized.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know. I have recorded your request to cancel your consultation {{consultation_id}} with {{seller_name}}, booked for {{booking_date}} at {{booking_time}} (EAT). Your request was received today and the time is noted on your case.

If you would prefer a different time instead of cancelling, I'm happy to check with the consultant — just tell me.

Your cancellation and refund request will be reviewed by our team according to Byfluence's policies, and we will let you know the outcome. Please keep your payment receipt or transaction reference.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን። ለ{{booking_date}} በ{{booking_time}} (EAT) ከ{{seller_name}} ጋር የተያዘውን ምክክርዎን {{consultation_id}} ለመሰረዝ ያቀረቡትን ጥያቄ መዝግቤያለሁ። ጥያቄዎ ዛሬ ደርሶናል፤ የቀረበበት ሰዓትም በጉዳይዎ ላይ ተመዝግቧል።

ከመሰረዝ ይልቅ ሌላ ሰዓት ቢመርጡ፣ ከአማካሪው ጋር ለማጣራት ፈቃደኛ ነኝ — ብቻ ይንገሩኝ።

የመሰረዝ እና የተመላሽ ገንዘብ ጥያቄዎ በByfluence ፖሊሲዎች መሰረት በቡድናችን ይታያል፤ ውጤቱንም እናሳውቅዎታለን። እባክዎ የክፍያ ደረሰኝዎን ወይም የግብይት ቁጥሩን ያስቀምጡ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your cancellation request for {{consultation_id}} is recorded (time noted). If a new time would help instead, tell me. Your refund request will be reviewed per Byfluence policy and we'll update you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የ{{consultation_id}} የመሰረዝ ጥያቄዎ ተመዝግቧል (ሰዓቱም ተይዟል)። በምትኩ ሌላ ሰዓት ቢመርጡ ይንገሩኝ። የተመላሽ ገንዘብ ጥያቄዎ በByfluence ፖሊሲ መሰረት ይታያል፤ መረጃ እንሰጥዎታለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your cancellation request for consultation {{consultation_id}} is still under review by our team. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የምክክር {{consultation_id}} የመሰረዝ ጥያቄዎ አሁንም በቡድናችን እየታየ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Every cancellation with a refund request → **Senior Support / Supervisor** (decision) → **Payments & Finance** (processing, if approved).
- Duplicate payment → **Payments & Finance**.
- Cancellation because of seller misconduct → **Trust & Safety**.
- High-value or repeated cancellation/refund requests by the same buyer → **Senior Support / Supervisor** (possible abuse).

## Resolution Procedure
1. Authorized decision recorded (cancelled with/without refund, or rescheduled instead).
2. Seller informed; booking status updated by authorized staff.
3. If refunded: Payments confirms processing; buyer informed using approved wording (see `ref-consultation-refunds`).
4. Ticket records request time, reason, decision and decision-maker.

## Policy Pending Approval
- Decide cancellation deadlines (how long before the session a buyer can cancel) and refund amounts at each stage.
- Decide whether any fees are non-refundable (e.g., payment provider fees).
- Decide whether buyers can cancel themselves in the dashboard.
- Decide who approves consultation refunds and the approved wording for refund timing.

## Internal Notes
- The request timestamp is the single most important fact for future cancellation rules — make sure it is in the ticket.
- Offer a reschedule only once; respect the buyer's decision.
- Never say "you will get a full refund" or "you can't get a refund". Say "your request will be reviewed".

<!-- doc -->
# Seller cancelled the consultation
id: con-cancellation-by-seller
type: article
category: consultations
subcategory: changes
audience: both
priority: high
department: support_l2
features: consultations-1on1, refunds
tags: seller cancelled, consultant cancelled, my booking was cancelled, seller cancel booking, cancellation by consultant, አማካሪው ሰረዘ, ቀጠሮዬ ተሰረዘ, ሻጩ ቀጠሮውን ሰረዘ
related: con-reschedule-request-seller, con-cancellation-by-buyer, con-seller-no-show, ref-consultation-refunds, con-refund-eligibility
templates: tpl-consultation-cancellation-ack, tpl-reschedule-request, tpl-seller-contact-request
policy_pending: yes

## Summary
The seller cancelled a paid booking (or asks support to cancel it), and the buyer wants to know what happens to their session and money.

## Issue Description
The buyer did nothing wrong — they paid and the seller cancelled. Buyers expect a refund or a new time and may be angry, especially with short notice. Sellers sometimes ask support to cancel because they cannot attend. The outcome (refund, rebooking, credit) is **policy pending**; support records, communicates and escalates.

## Possible Causes
- Seller emergency, illness, travel, double booking.
- Seller set availability incorrectly and cannot do the booked time.
- Seller no longer offers the service or account is being closed.
- Seller account suspended or restricted (bookings cancelled as a result — do not disclose enforcement details).
- Accidental cancellation by the seller.
- System error cancelled the booking.

## Information to Collect
- Booking ID; session date/time; when and how the cancellation happened (from booking history)
- Seller's reason (internal) and whether they can offer alternative times
- Buyer's preference: a new time with the same seller, another consultant, or a refund
- Payment method and transaction reference

## Troubleshooting Steps
1. Find the booking and its history: who cancelled, when, from where (seller action, admin, system).
   - **System cancellation with no seller action** → **Technical / Engineering**.
   - **Seller restricted/suspended** → coordinate with **Seller Operations**; buyer message stays neutral.
2. If a seller is asking you to cancel: ask whether they can offer alternative times instead (`con-reschedule-request-seller`). If not, record the reason and timing; tell them the buyer will be informed and the case reviewed.
3. Contact the buyer with an apology, explain the consultant cancelled, and ask their preference (new time with the seller if offered / other options).
4. Escalate to **Senior Support / Supervisor** with the buyer's preference, the booking, payment reference and the notice given.
5. Note seller cancellation history; frequent cancellations → **Seller Operations**.

## Recommended Response (EN)
Hello {{customer_name}},

I'm sorry to let you know that your consultation {{consultation_id}} with {{seller_name}}, booked for {{booking_date}} at {{booking_time}} (EAT), has been cancelled by the consultant. We apologise for the inconvenience — we know you had planned your time for it.

Please tell us what you would prefer:
1. A new time with the same consultant (if they can offer one), or
2. Our team reviewing your payment for this booking.

Your case has been recorded and our team will review it according to Byfluence's policies. Please keep your payment receipt or transaction reference. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ለ{{booking_date}} በ{{booking_time}} (EAT) ከ{{seller_name}} ጋር የተያዘው ምክክርዎ {{consultation_id}} በአማካሪው መሰረዙን ስናሳውቅዎ እናዝናለን። ጊዜዎን አቅደው እንደነበር ስለምናውቅ ለተፈጠረው ችግር ይቅርታ እንጠይቃለን።

እባክዎ የሚመርጡትን ይንገሩን፦
1. ከተመሳሳዩ አማካሪ ጋር አዲስ ሰዓት (አማካሪው ማቅረብ ከቻለ)፣ ወይም
2. ለዚህ ቀጠሮ የፈጸሙት ክፍያ በቡድናችን እንዲታይ

ጉዳይዎ ተመዝግቧል፤ ቡድናችንም በByfluence ፖሊሲዎች መሰረት ያየዋል። እባክዎ የክፍያ ደረሰኝዎን ወይም የግብይት ቁጥሩን ያስቀምጡ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry — {{seller_name}} cancelled your session on {{booking_date}} ({{booking_time}} EAT). Would you like a new time (if offered) or for us to review your payment? Your case is recorded. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ — {{seller_name}} በ{{booking_date}} ({{booking_time}} EAT) የነበረውን ምክክርዎን ሰርዘዋል። አዲስ ሰዓት (ከቀረበ) ይፈልጋሉ ወይስ ክፍያዎ እንዲታይ? ጉዳይዎ ተመዝግቧል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your case about the cancelled consultation {{consultation_id}} is under review by our team. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ስለተሰረዘው ምክክር {{consultation_id}} ያለዎት ጉዳይ በቡድናችን እየታየ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every seller cancellation of a paid booking where the buyer wants a refund → **Senior Support / Supervisor** → **Payments & Finance** if approved.
- Cancellation caused by a system error → **Technical / Engineering**.
- Cancellation linked to seller suspension → **Seller Operations**.
- Seller with repeated cancellations, or cancellations after taking many bookings → **Seller Operations** / **Trust & Safety**.

## Resolution Procedure
1. Buyer's preference recorded; authorized decision made (rebook / refund / other).
2. Rebooking confirmed in both clocks, or refund processing confirmed by Payments.
3. Ticket records who cancelled, when, notice given, decision.

## Policy Pending Approval
- Decide the buyer's entitlement when a seller cancels (full refund, rebooking, credit) and who approves.
- Decide seller consequences for cancellations, especially at short notice.
- Decide whether seller-cancelled bookings are refunded automatically.

## Internal Notes
- The buyer is not at fault here — apologise sincerely, but don't promise the outcome.
- Never disclose a seller's suspension or enforcement reason; say "the consultant is unable to hold the session".
- Seller cancellations right after receiving many payments are a fraud signal.

<!-- doc -->
# Session shorter than booked (duration dispute)
id: con-duration-dispute
type: article
category: consultations
subcategory: session-quality
audience: both
priority: medium
department: support_l2
features: consultations-1on1, google-meet, refunds
tags: session too short, ended early, didn't get full time, short consultation, consultant left early, duration complaint, ምክክሩ አጭር ነበር, ቀድሞ ጨረሰ, ሙሉ ጊዜ አላገኘሁም
related: con-incomplete-consultation, con-seller-late, con-buyer-late, con-tsg-no-show-decision-guide, con-refund-eligibility, ref-evidence-collection
templates: tpl-request-booking-details, tpl-seller-contact-request
policy_pending: yes

## Summary
The buyer says the session was shorter than the duration on the listing — because the seller joined late, ended early, or time was lost — and asks for compensation.

## Issue Description
The listing shows a duration (e.g., the seller's stated session length). The buyer says they received less. Sometimes the seller ended early because the buyer's questions were answered; sometimes the seller was late; sometimes the buyer joined late; sometimes the connection failed. The outcome depends on **why** time was lost and is **policy pending**.

## Possible Causes
- Seller joined late (`con-seller-late`).
- Seller ended the session before the booked end time.
- Buyer joined late (`con-buyer-late`) — the session ended at the booked end time.
- Connection or power problem on either side (`con-meeting-connection-problems`).
- Time spent on access problems (link, "Ask to join").
- Both agreed to end early because the topic was covered.

## Information to Collect
- Booking ID, listed duration, booked start/end (EAT)
- Actual start and end times according to the buyer and the seller
- Reason the session was short (from both sides)
- Any evidence: screenshots, messages, support contacts during the session
- Whether the seller offered extra time or a follow-up

## Troubleshooting Steps
1. Verify the booking and the listed duration on the listing.
2. Collect the buyer's account and evidence.
3. Contact the seller for their account (`tpl-seller-contact-request`).
4. Identify the cause category (seller late / seller ended early / buyer late / connection / access / mutual).
5. If both agree to a short follow-up to complete the time → arrange it through the booking process and record it.
6. Otherwise escalate to **Senior Support / Supervisor** with the facts. Use `con-tsg-no-show-decision-guide` scenarios 2, 4, 7, 8.
7. Do not promise extra time, a partial refund or a new session.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for telling us, and I'm sorry your session felt shorter than expected. I'd like to understand exactly what happened.

Please send me:
1. The time the session actually started and ended (approximately is fine)
2. What caused the session to be shorter (for example, the consultant joined late or ended early, or there were connection problems)
3. Any screenshots or messages that show this

We will also ask the consultant for their account, review both sides and let you know the outcome. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን፤ ምክክርዎ ከጠበቁት ያነሰ ጊዜ ስለወሰደ ይቅርታ እንጠይቃለን። በትክክል ምን እንደተፈጠረ ማወቅ እፈልጋለሁ።

እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ምክክሩ በትክክል የጀመረበት እና ያለቀበት ሰዓት (በግምትም ቢሆን)
2. ምክክሩን ያሳጠረው ምን እንደሆነ (ለምሳሌ፦ አማካሪው ዘግይቶ ገባ ወይም ቀድሞ ጨረሰ፣ ወይም የግንኙነት ችግር ነበር)
3. ይህን የሚያሳዩ ስክሪንሾቶች ወይም መልዕክቶች ካሉ

የአማካሪውንም ሃሳብ እንጠይቃለን፤ የሁለቱንም ወገን አጣርተን ውጤቱን እናሳውቅዎታለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry the session felt short. Please send the actual start/end times, what caused it, and any screenshots/messages. We'll hear the consultant's side too and update you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ምክክሩ ስላጠረ ይቅርታ። እባክዎ የጀመረበትን/ያለቀበትን ሰዓት፣ ምክንያቱን እና ስክሪንሾት/መልዕክቶች ይላኩ። የአማካሪውንም ሃሳብ ሰምተን መረጃ እንሰጥዎታለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have your information about consultation {{consultation_id}} and have asked {{seller_name}} for their account. The case is under review and we will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ስለ ምክክር {{consultation_id}} የላኩልንን መረጃ ተቀብለናል፤ {{seller_name}}ንም ሃሳባቸውን ጠይቀናል። ጉዳዩ እየታየ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Any compensation request → **Senior Support / Supervisor**.
- Seller ending sessions early repeatedly → **Seller Operations**.
- Time lost due to platform link/access failure → **Technical / Engineering** (root cause) + Senior Support (outcome).

## Resolution Procedure
1. Cause established with input from both sides.
2. Authorized decision (follow-up session, adjustment, no action) recorded and communicated.
3. Ticket tags the cause category.

## Policy Pending Approval
- Decide what counts as a "delivered" session when it is shorter than the listed duration.
- Decide compensation for seller-caused lost time (make-up time, partial refund) and for platform-caused lost time.
- Decide whether buyer-caused lost time (late arrival) is compensated.

## Internal Notes
- "Shorter" is sometimes subjective; the buyer may be unhappy with content rather than time. If so, see `con-quality-complaint`.
- Mutual early finish is legitimate if the buyer agreed at the time — ask the buyer neutrally whether they agreed.

<!-- doc -->
# Consultation interrupted or incomplete
id: con-incomplete-consultation
type: article
category: consultations
subcategory: session-quality
audience: both
priority: medium
department: support_l2
features: consultations-1on1, google-meet, refunds
tags: session interrupted, call dropped, couldn't finish, incomplete session, power cut during session, internet lost during consultation, ምክክሩ ተቋረጠ, አልጨረስንም, መብራት ጠፋ, ኢንተርኔት ተቋረጠ
related: con-meeting-connection-problems, con-duration-dispute, con-tsg-no-show-decision-guide, con-reschedule-request-buyer, con-refund-eligibility, con-completion-confirmation
templates: tpl-reschedule-request, tpl-request-booking-details, tpl-seller-contact-request
policy_pending: yes

## Summary
The consultation started but could not be finished — because of a connection loss, power outage, emergency or another interruption — and the buyer or seller asks what happens next.

## Issue Description
Unlike a no-show, both parties met, but part of the session was lost and could not be recovered. The buyer usually wants a continuation; the seller wants the session counted. Interruptions are common in Ethiopia (power cuts, mobile data loss, regional network disruptions) and often nobody is at fault. The fairest first step is usually to help both sides agree on a short continuation; the formal outcome is **policy pending**.

## Possible Causes
- Connection loss on the buyer's or seller's side.
- Power outage (router, laptop, phone charging).
- Regional internet disruption.
- Emergency for one party.
- Google Meet or device crash.
- Session ended at the booked time after time was lost earlier (late start).

## Information to Collect
- Booking ID, booked duration and times (EAT)
- When the session started, when it was interrupted, and how much was completed (both sides)
- Who lost connection, and whether they tried to rejoin
- Whether a continuation was discussed and what each party proposed
- Evidence: screenshots, messages, support contacts during the session

## Troubleshooting Steps
1. Verify the booking and collect both accounts.
2. Ask both sides whether they are willing to complete the remaining time at a new time.
   - **Both agree** → help arrange the continuation (`tpl-reschedule-request`), confirm the time in EAT + Ethiopian clock, confirm the link. Record it as a continuation of the same booking.
   - **Seller declines / buyer wants money instead** → escalate to **Senior Support / Supervisor** with the facts.
3. If the interruption was caused by the platform (Meet integration failure) → **Technical / Engineering**.
4. Make sure the booking is not marked completed (or earnings released) while a dispute is open — inform **Payments & Finance** that a dispute exists.
5. Record the interruption cause, time completed and agreement.

## Recommended Response (EN)
Hello {{customer_name}},

I'm sorry your consultation with {{seller_name}} was interrupted. Interruptions from connection or power problems can happen, and we want to help you complete your session.

Could you tell me:
1. Roughly how much of the session was completed before the interruption
2. Whether you were able to rejoin
3. A few times when you could continue the remaining part (East Africa Time)

I will contact the consultant about completing the session and let you know. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ከ{{seller_name}} ጋር የነበረዎት ምክክር ስለተቋረጠ ይቅርታ እንጠይቃለን። በኢንተርኔት ወይም በመብራት ምክንያት መቋረጥ ሊያጋጥም ይችላል፤ ምክክርዎን እንዲያጠናቅቁ ልንረዳዎ እንፈልጋለን።

እባክዎ የሚከተሉትን ይንገሩኝ፦
1. ከመቋረጡ በፊት በግምት ምን ያህሉ ምክክር እንደተካሄደ
2. እንደገና መግባት ችለው እንደሆነ
3. ቀሪውን ክፍል ለመቀጠል የሚመችዎት ጥቂት ሰዓቶች (በምሥራቅ አፍሪካ ሰዓት)

ምክክሩን ስለማጠናቀቅ አማካሪውን አግኝቼ አሳውቅዎታለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry your session was interrupted. How much was completed, and when could you continue (EAT)? I'll contact {{seller_name}} about completing it. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ምክክርዎ ስለተቋረጠ ይቅርታ። ምን ያህሉ ተካሂዷል፣ መቼስ መቀጠል ይችላሉ (በEAT)? ስለማጠናቀቅ {{seller_name}}ን አገኛለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have contacted {{seller_name}} about completing consultation {{consultation_id}} and are waiting for their reply. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ምክክር {{consultation_id}}ን ስለማጠናቀቅ {{seller_name}}ን አግኝተናል፤ መልሳቸውን እየጠበቅን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- No agreement on a continuation, or refund requested → **Senior Support / Supervisor**.
- Platform/Meet failure caused the interruption → **Technical / Engineering**.
- Many sessions interrupted at the same time (regional outage) → inform supervisor for consistent handling.

## Resolution Procedure
1. Continuation completed (confirm with the buyer afterwards), or authorized decision made.
2. Booking completion handled by authorized staff only after resolution.
3. Ticket records cause, time completed, agreement or decision.

## Policy Pending Approval
- Decide whether sellers must offer a continuation for interruptions caused on their side, and how the remaining time is calculated.
- Decide outcomes when no continuation is agreed (partial refund, completion as-is).
- Decide how platform-caused interruptions are compensated.

## Internal Notes
- Lead with a practical fix (continuation) — most buyers prefer finishing the session to a long dispute.
- Avoid blame; say "the connection was lost", not "you lost connection".
- Record whether the booking was auto-marked completed; if so, tell Payments a dispute is open.
