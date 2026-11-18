<!-- doc -->
# Group schedule and time-zone confusion
id: grp-scheduling-time-zones
type: article
category: group-consultations
subcategory: group-changes
audience: both
priority: medium
department: support_l1
features: consultations-group
tags: group session time, what time is the workshop, Ethiopian time group, wrong time group session, diaspora group time, የቡድን ምክክር ሰዓት, በኢትዮጵያ አቆጣጠር, ስንት ሰዓት ነው
related: con-time-zone-confusion, grp-join-group-meeting, grp-rescheduled-session, tec-calendar-time-display, grp-partial-attendance
templates: tpl-request-booking-details
policy_pending: yes

## Summary
A participant or seller is unsure of, or acted on the wrong, group session time because of Ethiopian-clock vs international-clock confusion, AM/PM, Ethiopian calendar dates, or time zones abroad.

## Issue Description
Group sessions have **one fixed time for everyone**, so a single misread time can affect many participants — or the seller. A seller who intended "ምሽት 2 ሰዓት" (8:00 PM) but entered "2:00 PM" creates a session six hours earlier than planned for every participant. Use the full conversion guide in `con-time-zone-confusion`.

Key conversions:
| International (EAT) | Ethiopian clock |
|---|---|
| 9:00 AM | ጠዋት 3 ሰዓት |
| 2:00 PM | ከሰዓት 8 ሰዓት |
| 6:00 PM | ምሽት 12 ሰዓት |
| 8:00 PM | ማታ 2 ሰዓት |

## Possible Causes
- Participant read the listed time in Ethiopian clock (or vice versa).
- Seller entered the time in Ethiopian clock by mistake.
- AM/PM error; Ethiopian calendar date confused with Gregorian.
- Participant abroad didn't convert from EAT.
- Display bug.

## Information to Collect
- Session name, seller
- The time as the person understood it (their own words) and as displayed (screenshot)
- Location (Ethiopia/abroad)

## Troubleshooting Steps
1. Read the session time from the admin record.
2. Restate it: weekday + Gregorian date + international time + EAT (+ Ethiopian clock in Amharic; + local time for diaspora).
3. If a **participant** misunderstood → correct it; if they already missed it → `grp-partial-attendance` / `grp-refund-questions`.
4. If the **seller** entered the wrong time → contact the seller to confirm the intended time. Changing the time of a session with registrations = a reschedule → `grp-rescheduled-session`; all registered participants must be informed.
5. If display differs from record → **Technical / Engineering**.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for checking. Your group session with {{seller_name}} is on {{booking_date}} at {{booking_time}} East Africa Time (EAT), using the international clock.

If you use the Ethiopian clock, please note the difference — for example, 6:00 PM international time is ምሽት 12 ሰዓት, and 8:00 PM is ማታ 2 ሰዓት. If you are outside Ethiopia, please convert from EAT (UTC+3) to your local time.

Please reply with the time in your own words so we're sure we agree. Your reference number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላረጋገጡ እናመሰግናለን። ከ{{seller_name}} ጋር ያለዎት የቡድን ምክክር {{booking_date}} በ{{booking_time}} በምሥራቅ አፍሪካ ሰዓት (EAT)፣ በፈረንጅ አቆጣጠር ነው — በኢትዮጵያ አቆጣጠር [ለምሳሌ፦ ማታ 2 ሰዓት]።

ልዩነቱን ልብ ይበሉ፦ ለምሳሌ 6:00 PM በኢትዮጵያ አቆጣጠር ምሽት 12 ሰዓት ነው፤ 8:00 PM ደግሞ ማታ 2 ሰዓት ነው። ከኢትዮጵያ ውጭ ከሆኑ፣ እባክዎ ከEAT (UTC+3) ወደ አካባቢዎ ሰዓት ይቀይሩ።

በአንድ ሰዓት ላይ መስማማታችንን ለማረጋገጥ፣ ሰዓቱን በራስዎ አገላለጽ መልሰው ይጻፉልኝ። የጉዳይ ቁጥርዎ {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! The group session is {{booking_date}} at {{booking_time}} EAT (international clock). Example: 8:00 PM = ማታ 2 ሰዓት. Please reply with the time in your own words to confirm. Ref: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! የቡድን ምክክሩ {{booking_date}} በ{{booking_time}} EAT (በፈረንጅ አቆጣጠር) ነው — በኢትዮጵያ አቆጣጠር [ለምሳሌ ማታ 2 ሰዓት]። ለማረጋገጥ ሰዓቱን በራስዎ አገላለጽ ይጻፉልኝ። ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Seller set the wrong time and registrations exist → **Senior Support / Supervisor** (reschedule affecting many buyers).
- Display bug → **Technical / Engineering**.
- Participants missed the session due to confusion and request refunds → **Senior Support / Supervisor**.

## Resolution Procedure
1. Person confirms the correct time in their own words.
2. If the session time changed, all participants notified (see `grp-rescheduled-session`).

## Policy Pending Approval
- Confirm display time zone for group sessions and whether Ethiopian-clock equivalents are shown.
- Decide responsibility when a seller's time-entry mistake causes a reschedule.

## Internal Notes
- When a seller creates a group session, it's worth reading the time back to them in both clocks — one check prevents dozens of tickets.

<!-- doc -->
# Group session cancelled by the seller
id: grp-cancelled-by-seller
type: article
category: group-consultations
subcategory: group-changes
audience: buyer
priority: high
department: support_l2
features: consultations-group, refunds
tags: group session cancelled, workshop cancelled, seller cancelled group, event cancelled, what happens to my payment, የቡድን ምክክሩ ተሰረዘ, ወርክሾፑ ተሰረዘ, ገንዘቤስ
related: grp-low-attendance-seller, grp-refund-questions, grp-rescheduled-session, con-cancellation-by-seller, ref-consultation-refunds
templates: tpl-group-session-cancelled, tpl-request-booking-details
policy_pending: yes

## Summary
The seller cancelled a group session that participants had paid for. Many buyers are affected at once; outcomes (refund, transfer to another date) are policy pending.

## Issue Description
A cancellation affects every registered participant, so expect several contacts at the same time. Participants are not at fault and expect clear information about their money. Consistency is essential: all participants should get the same message from support. The seller may have cancelled for low registrations (`grp-low-attendance-seller`), an emergency, or because their account was restricted.

## Possible Causes
- Seller emergency or conflict.
- Low registrations.
- Seller account restricted/suspended (do not disclose).
- Technical problem (e.g., cannot host the meeting).
- Accidental cancellation or system error.

## Information to Collect
- Session ID/name, seller, original date/time
- Cancellation time and reason (from record/seller — internal)
- List of affected confirmed participants (from the admin dashboard)
- Each participant's preference (new date if offered / payment review)
- Transaction references

## Troubleshooting Steps
1. Confirm the cancellation in the session record; note who cancelled and when.
   - System error → **Technical / Engineering** immediately (session may need restoring).
2. Inform your supervisor: one coordinator should handle communication to all participants, using `tpl-group-session-cancelled`.
3. Ask the seller whether they will offer a new date (`grp-rescheduled-session`).
4. Contact each confirmed participant with the same message; record each preference.
5. Escalate the group case (one parent ticket, participants linked) to **Senior Support / Supervisor** for the outcome; **Payments & Finance** for processing approved refunds.
6. Note seller cancellation history for **Seller Operations**.

## Recommended Response (EN)
Hello {{customer_name}},

We're sorry to let you know that the group session "{{product_name}}" with {{seller_name}}, scheduled for {{booking_date}} at {{booking_time}} (EAT), has been cancelled by the consultant. We apologise for the inconvenience.

Your registration and payment are recorded. Our team is reviewing the next steps for all participants of this session, and we will contact you with the outcome. If the consultant offers a new date, we will let you know so you can choose whether to join.

Please keep your payment receipt or transaction reference. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ለ{{booking_date}} በ{{booking_time}} (EAT) ከ{{seller_name}} ጋር ተይዞ የነበረው "{{product_name}}" የቡድን ምክክር በአማካሪው መሰረዙን ስናሳውቅዎ እናዝናለን። ለተፈጠረው ችግር ይቅርታ እንጠይቃለን።

ምዝገባዎ እና ክፍያዎ ተመዝግበዋል። ቡድናችን ለዚህ ምክክር ተሳታፊዎች ሁሉ ቀጣዩን ደረጃ እያጤነ ሲሆን፣ ውጤቱን እናሳውቅዎታለን። አማካሪው አዲስ ቀን ካቀረበ፣ መሳተፍ ይፈልጉ እንደሆነ እንዲመርጡ እናሳውቅዎታለን።

እባክዎ የክፍያ ደረሰኝዎን ወይም የግብይት ቁጥሩን ያስቀምጡ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry — {{seller_name}} cancelled the group session on {{booking_date}} ({{booking_time}} EAT). Your registration and payment are recorded; we're reviewing next steps for all participants and will update you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ — {{seller_name}} በ{{booking_date}} ({{booking_time}} EAT) የነበረውን የቡድን ምክክር ሰርዘዋል። ምዝገባዎ እና ክፍያዎ ተመዝግበዋል፤ ለሁሉም ተሳታፊዎች ቀጣዩን ደረጃ እያየን ነው፤ መረጃ እንሰጥዎታለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are still reviewing the next steps for participants of the cancelled group session "{{product_name}}". We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለተሰረዘው "{{product_name}}" የቡድን ምክክር ተሳታፊዎች ቀጣዩን ደረጃ አሁንም እያጤንን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every seller-cancelled group session with paid participants → **Senior Support / Supervisor** (one coordinated case).
- Approved refunds → **Payments & Finance**.
- System-caused cancellation → **Technical / Engineering**.
- Repeated cancellations / cancellation after collecting many payments → **Seller Operations** / **Trust & Safety**.

## Resolution Procedure
1. All affected participants contacted and their preferences recorded.
2. Authorized outcome applied consistently to all participants.
3. Parent ticket records the decision, the participant list and completion of each action.

## Policy Pending Approval
- Decide participants' entitlement when a seller cancels a group session (refund, transfer, credit) and whether it is automatic.
- Decide the minimum notice for seller cancellations and consequences.
- Decide who communicates mass cancellations (support vs automated notification).

## Internal Notes
- Use one parent ticket and link each participant's ticket — consistency is everything.
- Never tell one participant something different from the others.

<!-- doc -->
# Participant wants to cancel registration
id: grp-cancel-registration-buyer
type: article
category: group-consultations
subcategory: group-changes
audience: buyer
priority: medium
department: support_l2
features: consultations-group, refunds
tags: cancel group registration, can't attend workshop, withdraw from group session, cancel my place, transfer my place, ምዝገባዬን መሰረዝ, መገኘት አልችልም, ቦታዬን ማስተላለፍ
related: grp-refund-questions, grp-capacity-full, con-cancellation-by-buyer, ref-consultation-refunds, grp-rescheduled-session
templates: tpl-consultation-cancellation-ack, tpl-request-booking-details
policy_pending: yes

## Summary
A registered participant can no longer attend a group session and wants to cancel, get a refund, or transfer their place to someone else. Rules are not yet approved.

## Issue Description
Unlike one-on-one bookings, the group session happens whether or not this participant attends, and the seller has planned for a certain number of participants. Participants often ask to **give their place to a friend or colleague**. Cancellation deadlines, refunds and transfers are **policy pending** — record the request and escalate.

## Possible Causes
- Schedule conflict, emergency, change of plans.
- Registered by mistake or twice.
- Session rescheduled to a time that doesn't suit them (`grp-rescheduled-session`).
- Lost interest or concerns about the seller.

## Information to Collect
- Session, seller, date/time; registration reference
- Reason
- What they want: cancel + refund, transfer to another person, or move to a future session of the same seller
- Transaction reference
- Request timestamp (record it)

## Troubleshooting Steps
1. Verify identity and confirm the registration.
2. Special cases:
   - **Registered twice / paid twice** → **Payments & Finance**.
   - **Session was rescheduled by the seller** → treat under `grp-rescheduled-session` (different situation from a voluntary cancellation).
   - **Session already happened** → `grp-partial-attendance` / `grp-refund-questions`.
3. **Transfer request** → do not change the registrant yourself; record the request and escalate (transfers are not an approved process). Never share the meeting link with the new person.
4. Acknowledge (`tpl-consultation-cancellation-ack`), record the request time, and escalate to **Senior Support / Supervisor**.
5. If the session is full and has interest from others, mention it in the escalation (a freed place may matter).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know. I've recorded your request regarding your registration for the group session "{{product_name}}" with {{seller_name}} on {{booking_date}} at {{booking_time}} (EAT). The time of your request is noted on your case.

Your request will be reviewed by our team according to Byfluence's policies, and we will let you know the outcome. Please don't share your meeting link with anyone else in the meantime — it is linked to your registration.

Please keep your payment receipt or transaction reference. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን። በ{{booking_date}} በ{{booking_time}} (EAT) ከ{{seller_name}} ጋር ለሚካሄደው "{{product_name}}" የቡድን ምክክር ምዝገባዎን በተመለከተ ያቀረቡትን ጥያቄ መዝግቤያለሁ። ጥያቄዎ የቀረበበት ሰዓትም በጉዳይዎ ላይ ተመዝግቧል።

ጥያቄዎ በByfluence ፖሊሲዎች መሰረት በቡድናችን ይታያል፤ ውጤቱንም እናሳውቅዎታለን። እስከዚያው ድረስ የስብሰባ ሊንክዎ ከምዝገባዎ ጋር የተያያዘ ስለሆነ እባክዎ ለሌላ ሰው አያጋሩት።

እባክዎ የክፍያ ደረሰኝዎን ወይም የግብይት ቁጥሩን ያስቀምጡ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, your request about your group session registration is recorded (time noted) and will be reviewed per Byfluence policy. Please don't share your meeting link meanwhile. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የቡድን ምክክር ምዝገባዎን በተመለከተ ያቀረቡት ጥያቄ ተመዝግቧል (ሰዓቱም ተይዟል)፤ በByfluence ፖሊሲ መሰረት ይታያል። እስከዚያው የስብሰባ ሊንክዎን አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your request regarding your registration for "{{product_name}}" is still under review. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለ"{{product_name}}" ምዝገባዎ ያቀረቡት ጥያቄ አሁንም እየታየ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Cancellation with refund request, or transfer request → **Senior Support / Supervisor**.
- Duplicate registration/payment → **Payments & Finance**.

## Resolution Procedure
1. Authorized decision recorded and communicated.
2. Registration updated by authorized staff (cancelled/transferred) and seller informed.
3. Ticket records request time, request type, decision.

## Policy Pending Approval
- Decide group cancellation deadlines and refund rules for participants.
- Decide whether places can be transferred to another person, and how identity is handled.
- Decide whether participants can move to a future session of the same seller.

## Internal Notes
- Transfers by link-sharing bypass verification and capacity control — always discourage it.
- Record the request time precisely; future deadline rules will depend on it.

<!-- doc -->
# Group session rescheduled
id: grp-rescheduled-session
type: article
category: group-consultations
subcategory: group-changes
audience: both
priority: medium
department: support_l2
features: consultations-group
tags: group session moved, workshop rescheduled, new date group session, can't attend new time, seller changed time, የቡድን ምክክሩ ቀን ተቀየረ, አዲሱ ሰዓት አይመቸኝም
related: grp-cancelled-by-seller, grp-cancel-registration-buyer, grp-scheduling-time-zones, grp-refund-questions, con-reschedule-request-seller
templates: tpl-reschedule-request, tpl-group-session-cancelled, tpl-request-booking-details
policy_pending: yes

## Summary
The seller moved a group session to a new date/time (or wants to), and participants ask what this means — especially those who cannot attend the new time.

## Issue Description
A group reschedule changes the plan for every participant. Some will accept the new time; others can't attend and will want a refund or another option. Participants must be informed clearly and consistently, with the new time in EAT and Ethiopian clock. Rules for group reschedules are **policy pending**.

## Possible Causes
- Seller emergency or conflict.
- Seller's original time entry was wrong (time confusion).
- Low registrations (seller hopes for more participants later).
- Technical problems on the original date.

## Information to Collect
- Session, seller, original and new date/time
- When and how participants were notified (if at all)
- Each participant's response: accepts / cannot attend
- Seller's reason (internal)

## Troubleshooting Steps
1. Confirm the change in the session record (original vs new time, who changed it, when).
2. **Seller asking to reschedule** → collect the proposed new time; inform the supervisor; confirm how participants will be notified (coordinated message, one parent ticket).
3. **Participant asking** → give the new time in EAT + Ethiopian clock + weekday; ask whether they can attend.
   - Can attend → confirm their registration stays valid and the link is correct for the new time.
   - Cannot attend → record and escalate to **Senior Support / Supervisor** (refund/transfer pending).
4. Check that the meeting link is valid for the new time; inform participants if it changed.
5. Track all participant responses in the parent ticket.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us about the group session "{{product_name}}" with {{seller_name}}. The session has been moved to a new date and time:

- New date and time: {{booking_date}} at {{booking_time}} (EAT, international clock)

We're sorry for the change. Please let us know whether you can attend at the new time. If you can't, tell us and we will review your options according to Byfluence's policies.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ከ{{seller_name}} ጋር ስለሚካሄደው "{{product_name}}" የቡድን ምክክር ስላገኙን እናመሰግናለን። ምክክሩ ወደ አዲስ ቀን እና ሰዓት ተዛውሯል፦

- አዲሱ ቀን እና ሰዓት፦ {{booking_date}} በ{{booking_time}} (EAT፣ በፈረንጅ አቆጣጠር) — በኢትዮጵያ አቆጣጠር [ለምሳሌ፦ ማታ 2 ሰዓት]

ለለውጡ ይቅርታ እንጠይቃለን። እባክዎ በአዲሱ ሰዓት መገኘት ይችሉ እንደሆነ ያሳውቁን። ካልቻሉ ይንገሩን፤ ያሉዎትን አማራጮች በByfluence ፖሊሲዎች መሰረት እናያለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, the group session "{{product_name}}" moved to {{booking_date}} at {{booking_time}} EAT. Sorry for the change! Can you attend? If not, tell us and we'll review your options. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ "{{product_name}}" የቡድን ምክክር ወደ {{booking_date}} በ{{booking_time}} EAT ተዛውሯል። ለለውጡ ይቅርታ! መገኘት ይችላሉ? ካልቻሉ ይንገሩን፤ አማራጮችዎን እናያለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have recorded that you cannot attend the new time for "{{product_name}}", and your case is under review. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለ"{{product_name}}" በአዲሱ ሰዓት መገኘት እንደማይችሉ መዝግበናል፤ ጉዳይዎ እየታየ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Participants who can't attend the new time → **Senior Support / Supervisor**.
- Seller reschedules repeatedly or at very short notice → **Seller Operations**.
- Participants were not notified of the change → **Technical / Engineering** (notifications) + supervisor.

## Resolution Procedure
1. All participants informed of the new time in both clocks.
2. Each participant's response recorded; non-attendees' cases decided by authorized staff.
3. Meeting link valid for the new time.

## Policy Pending Approval
- Decide how much notice sellers must give to reschedule a group session, and how many times.
- Decide options for participants who cannot attend the new time.
- Decide whether participants must actively accept a reschedule or are assumed to accept.

## Internal Notes
- Silence is not acceptance — record explicit responses where possible.
- A "reschedule" right after low registrations may really be a cancellation; check `grp-low-attendance-seller`.

<!-- doc -->
# Seller didn't join the group session
id: grp-seller-no-show
type: article
category: group-consultations
subcategory: group-attendance
audience: buyer
priority: high
department: support_l2
features: consultations-group, google-meet, refunds
tags: group seller no show, host didn't come, workshop host absent, group session didn't start, nobody came group, አማካሪው አልመጣም ቡድን, ወርክሾፑ አልተጀመረም
related: con-seller-no-show, con-tsg-no-show-decision-guide, grp-cancelled-by-seller, grp-refund-questions, grp-missing-link
templates: tpl-seller-no-show-ack, tpl-waiting-for-seller, tpl-seller-contact-request
policy_pending: yes

## Summary
Participants were waiting in the group meeting, but the seller (host) never joined. Many buyers are affected at once — handle as a coordinated case.

## Issue Description
Several participants contact support at the same time saying the session hasn't started or they are stuck on "Asking to join". While the session time is running, contact the seller urgently and keep participants informed. Once the time has passed, this is a group no-show: collect evidence once for the whole session and escalate one coordinated case. Outcomes are **policy pending**.

## Possible Causes
- Seller late or absent (emergency, forgot).
- Seller in a different meeting link.
- Seller misread the time (Ethiopian clock / AM-PM).
- Seller didn't know the session had registrations (notification issue).
- Platform link problem.

## Information to Collect
- Session, seller, time
- From participants: join time, link used, screenshot with the time visible
- From the seller: whether/when they joined, link used, reason
- Number of confirmed participants and how many contacted support

## Troubleshooting Steps
1. **Live:** contact the seller immediately; tell participants you're on it (`tpl-waiting-for-seller`); ask them to stay and take a screenshot showing the time. Inform your supervisor — one coordinator.
2. Compare the link participants are using with the session record; check the seller's link if reachable.
3. Check the time understanding (seller and participants).
4. **After the session time:** acknowledge every participant (`tpl-seller-no-show-ack`); collect the seller's account; build one evidence pack for the session.
5. Escalate one parent case to **Senior Support / Supervisor**; inform **Payments & Finance** that the session is disputed.
6. Note for **Seller Operations** (and **Trust & Safety** if the seller collected many payments and disappeared).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us, and I'm sorry the group session "{{product_name}}" with {{seller_name}} on {{booking_date}} at {{booking_time}} (EAT) did not start as planned.

We are contacting the consultant now. If the session time is still running, please stay in the meeting and take a screenshot showing the time — it helps us review what happened.

Your registration is recorded, and our team will review this case for all participants and let you know the outcome. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን፤ በ{{booking_date}} በ{{booking_time}} (EAT) ከ{{seller_name}} ጋር ሊካሄድ የነበረው "{{product_name}}" የቡድን ምክክር እንደታቀደው ስላልተጀመረ ይቅርታ እንጠይቃለን።

አማካሪውን አሁኑኑ እያገኘን ነው። የምክክሩ ሰዓት ገና ካላለፈ፣ እባክዎ ስብሰባው ውስጥ ይቆዩ እና ሰዓቱ የሚታይበትን ስክሪንሾት ያንሱ — የሆነውን ለማጣራት ይረዳናል።

ምዝገባዎ ተመዝግቧል፤ ቡድናችን ይህን ጉዳይ ለሁሉም ተሳታፊዎች አጣርቶ ውጤቱን ያሳውቅዎታል። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry the group session hasn't started. We're contacting {{seller_name}} now. If it's still session time, please stay in the meeting and screenshot the screen with the time. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የቡድን ምክክሩ ስላልተጀመረ ይቅርታ። {{seller_name}}ን አሁኑኑ እያገኘን ነው። የምክክሩ ሰዓት ገና ከሆነ ስብሰባው ውስጥ ይቆዩ እና ሰዓቱ የሚታይበትን ስክሪንሾት ያንሱ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}} about the group session "{{product_name}}". We have contacted the consultant and are reviewing the case for all participants. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ "{{product_name}}" የቡድን ምክክር (ጉዳይ ቁጥር {{ticket_id}}) የሚሰጥ መረጃ ነው። አማካሪውን አግኝተናል፤ ጉዳዩንም ለሁሉም ተሳታፊዎች እያጣራን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Group seller no-show → **Senior Support / Supervisor**, High, one coordinated case.
- Seller unreachable / disappeared after collecting payments → **Trust & Safety** + **Seller Operations**.
- Platform link failure → **Technical / Engineering**.

## Resolution Procedure
1. Authorized outcome applied consistently to all participants.
2. Parent ticket records evidence, seller's account, decision, participant list.

## Policy Pending Approval
- Decide outcomes for group seller no-shows (refund all, reschedule, credit) and whether they apply automatically.
- Decide seller consequences for group no-shows.

## Internal Notes
- One coordinator, one message, one evidence pack. Avoid ten agents contacting the seller separately.
- Follow `con-seller-no-show` for the detailed evidence method.

<!-- doc -->
# Participant attended only part of the session
id: grp-partial-attendance
type: article
category: group-consultations
subcategory: group-attendance
audience: buyer
priority: medium
department: support_l2
features: consultations-group, refunds
tags: missed part of group session, joined late group, left early, partial attendance, missed workshop, ከፊሉን ብቻ ተሳተፍኩ, ዘግይቼ ገባሁ, ቀድሜ ወጣሁ
related: grp-participant-access-denied, grp-meeting-interrupted, grp-refund-questions, con-buyer-late, grp-scheduling-time-zones
templates: tpl-request-booking-details, tpl-seller-contact-request
policy_pending: yes

## Summary
A participant attended only part of a group session — joined late, dropped out, or was let in late — and asks for compensation or access to what they missed.

## Issue Description
The session ran for everyone else, so the question is **why** this participant missed part of it: their own lateness or connection, the host not admitting them, a missing link, or time confusion. The answer affects who is responsible. Outcomes are **policy pending**.

## Possible Causes
- Participant joined late (personal reasons, time confusion).
- Participant's connection or power failed.
- Host didn't admit them promptly (`grp-participant-access-denied`).
- Missing/incorrect link (`grp-missing-link`).
- Participant removed from the meeting.

## Information to Collect
- Session, seller, time
- When they joined and left (EAT), and why
- Any support contacts during the session (strong evidence for access problems)
- What they are asking for (recording, materials, partial refund, future session)

## Troubleshooting Steps
1. Check for support contacts by this participant during the session (access/link problems).
2. Determine the cause category: participant-side / host-side / platform-side / time confusion.
3. If they ask for materials or a recording → ask the seller whether these exist and can be shared (consent of other participants is required for recordings — `con-recording-requests`).
4. If they ask for compensation → escalate to **Senior Support / Supervisor** with the cause category.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us, and I'm sorry you missed part of the group session "{{product_name}}" with {{seller_name}}.

To review this, please tell me:
1. Roughly when you joined and when you left (EAT)
2. What caused you to miss part of the session (for example, a problem getting in, a connection issue or a timing issue)
3. What you would like us to look into

We will check with the consultant and review your case according to Byfluence's policies. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን፤ ከ{{seller_name}} ጋር የነበረውን "{{product_name}}" የቡድን ምክክር በከፊል ስላመለጠዎት ይቅርታ እንጠይቃለን።

ጉዳዩን ለማየት እባክዎ የሚከተሉትን ይንገሩኝ፦
1. በግምት መቼ እንደገቡ እና መቼ እንደወጡ (በEAT)
2. ከፊሉ እንዲያመልጥዎ ያደረገው ምን እንደሆነ (ለምሳሌ፦ የመግባት ችግር፣ የግንኙነት ችግር ወይም የሰዓት መምታታት)
3. ምን እንድናጣራልዎ እንደሚፈልጉ

ከአማካሪው ጋር አጣርተን ጉዳይዎን በByfluence ፖሊሲዎች መሰረት እናያለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry you missed part of the session. Please tell me roughly when you joined/left (EAT), what caused it, and what you'd like us to look into. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ከምክክሩ ከፊሉ ስላመለጠዎት ይቅርታ። እባክዎ በግምት መቼ እንደገቡ/እንደወጡ (EAT)፣ ምክንያቱን እና ምን እንድናጣራ እንደሚፈልጉ ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are reviewing your partial attendance at "{{product_name}}" with the consultant. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። በ"{{product_name}}" ላይ በከፊል መሳተፍዎን ከአማካሪው ጋር እያጣራን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Compensation requested → **Senior Support / Supervisor**.
- Host/platform caused the missed time → **Senior Support / Supervisor** (+ **Technical / Engineering** if platform).

## Resolution Procedure
1. Cause established; authorized decision communicated.
2. Ticket records cause category and times.

## Policy Pending Approval
- Decide whether partial attendance is ever compensated, and depending on which cause.
- Decide whether sellers should provide materials or recordings to participants who missed part of a session.

## Internal Notes
- Support contacts during the session are the best evidence that a participant was trying to get in.

<!-- doc -->
# Group session interrupted or ended early
id: grp-meeting-interrupted
type: article
category: group-consultations
subcategory: group-attendance
audience: both
priority: medium
department: support_l2
features: consultations-group, google-meet, refunds
tags: group session interrupted, workshop ended early, host disconnected, group meeting dropped, session cut short group, የቡድን ምክክሩ ተቋረጠ, ቀድሞ አለቀ, አማካሪው ተቋረጠ
related: grp-partial-attendance, con-incomplete-consultation, con-meeting-connection-problems, grp-refund-questions, grp-seller-no-show
templates: tpl-group-session-cancelled, tpl-reschedule-request, tpl-request-booking-details
policy_pending: yes

## Summary
A group session was interrupted (host lost connection or power) or ended before its scheduled end time, affecting all participants.

## Issue Description
When the **host** drops, the whole group loses the session. Participants may wait, leave, or contact support at once. The practical fix is usually a continuation session for everyone; the formal outcome is **policy pending**. Treat as a coordinated case when several participants report it.

## Possible Causes
- Host's internet or power failure.
- Google Meet ended for everyone (e.g., host ended the call by mistake).
- Seller ended early deliberately (ran out of content, other commitment).
- Disruptive participant forced the host to end.
- Platform/Meet integration issue.

## Information to Collect
- Session, seller, scheduled vs actual start/end times
- What happened (from the seller and a few participants)
- Whether the host rejoined, and whether a continuation was announced
- Number of participants affected

## Troubleshooting Steps
1. **Live:** contact the seller — can they rejoin with the same link? Tell participants to stay in the meeting for a few moments.
2. **After:** get the seller's account; ask whether they will offer a continuation for all participants.
   - Continuation offered → coordinate one message to all participants with the date/time in EAT + Ethiopian clock (`tpl-reschedule-request`).
   - Not offered / participants want refunds → one parent case to **Senior Support / Supervisor**.
3. Disruptive participant → **Trust & Safety** (`con-inappropriate-conduct-in-session`).
4. Inform **Payments & Finance** that the session is disputed.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know, and I'm sorry the group session "{{product_name}}" with {{seller_name}} was interrupted.

We are in contact with the consultant about what happened and about completing the session. We will update all participants together as soon as we have more information. If you have screenshots or noticed the time the session stopped, please share them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን፤ ከ{{seller_name}} ጋር የነበረው "{{product_name}}" የቡድን ምክክር ስለተቋረጠ ይቅርታ እንጠይቃለን።

ስለተፈጠረው ነገር እና ምክክሩን ስለማጠናቀቅ ከአማካሪው ጋር እየተነጋገርን ነው። ተጨማሪ መረጃ እንዳገኘን ለሁሉም ተሳታፊዎች በአንድ ላይ እናሳውቃለን። ስክሪንሾት ካለዎት ወይም ምክክሩ የቆመበትን ሰዓት ካስተዋሉ፣ እባክዎ ያጋሩን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry the group session was interrupted. We're in touch with {{seller_name}} about completing it and will update all participants together. Share any screenshots or the time it stopped. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የቡድን ምክክሩ ስለተቋረጠ ይቅርታ። ስለማጠናቀቁ ከ{{seller_name}} ጋር እየተነጋገርን ነው፤ ለሁሉም ተሳታፊዎች በአንድ ላይ እናሳውቃለን። ስክሪንሾት ወይም የቆመበትን ሰዓት ያጋሩን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are still arranging next steps with the consultant for the interrupted session "{{product_name}}". We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለተቋረጠው "{{product_name}}" ምክክር ቀጣዩን ደረጃ ከአማካሪው ጋር አሁንም እያመቻቸን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- No continuation agreed, or refunds requested → **Senior Support / Supervisor** (coordinated case).
- Disruptive participant → **Trust & Safety**.
- Platform/Meet failure → **Technical / Engineering**.
- Seller ended early deliberately and repeatedly → **Seller Operations**.

## Resolution Procedure
1. Continuation held (confirm with participants) or authorized outcome applied to all.
2. Parent ticket records cause, times, participants, decision.

## Policy Pending Approval
- Decide whether sellers must offer a continuation after a host-side interruption.
- Decide outcomes for participants who cannot attend the continuation.
- Decide how a deliberate early end by the seller is treated.

## Internal Notes
- Communicate once to all participants; avoid different promises in different chats.

<!-- doc -->
# Group session refund questions
id: grp-refund-questions
type: article
category: group-consultations
subcategory: group-attendance
audience: buyer
priority: medium
department: support_l2
features: consultations-group, refunds
tags: group refund, workshop refund, money back group session, refund group consultation, missed group session refund, የቡድን ምክክር ተመላሽ, ገንዘቤ ይመለስልኝ
related: con-refund-eligibility, ref-consultation-refunds, ref-how-to-request-refund, grp-cancelled-by-seller, grp-cancel-registration-buyer, grp-partial-attendance
templates: tpl-consultation-cancellation-ack, tpl-group-session-cancelled, tpl-request-booking-details
policy_pending: yes

## Summary
A participant asks whether they can get a refund for a group session. Group refund rules are not approved — route to the right situation, record and escalate; never promise or refuse.

## Issue Description
Group refund requests arise from cancellation by the seller, reschedules, the participant's own cancellation, missed or partial attendance, interruptions, or dissatisfaction. Because one decision may affect many participants, consistency matters. All outcomes are **policy pending**.

| Situation | Article |
|---|---|
| Seller cancelled | `grp-cancelled-by-seller` |
| Seller didn't join | `grp-seller-no-show` |
| Rescheduled, can't attend | `grp-rescheduled-session` |
| Participant wants to cancel | `grp-cancel-registration-buyer` |
| Missed part / couldn't get in | `grp-partial-attendance` / `grp-participant-access-denied` |
| Interrupted / ended early | `grp-meeting-interrupted` |
| Unhappy with quality | `con-quality-complaint` |
| Paid but no place | `grp-capacity-full` |

## Possible Causes
- See the situations above.

## Information to Collect
- Session, seller, date/time; registration reference
- Situation and reason
- Transaction reference
- Relevant evidence for the situation
- Request time

> [!WARNING] Never ask for PINs, passwords, verification codes or card numbers. The transaction reference is enough.

## Troubleshooting Steps
1. Identify the situation and follow its article.
2. Check whether other participants of the same session have open requests — link them to one parent ticket.
3. Record the request and escalate to **Senior Support / Supervisor**; approved refunds processed by **Payments & Finance**.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your question about the group session "{{product_name}}". Refund requests for group sessions are reviewed by our team according to Byfluence's policies. I can't confirm the outcome myself, but I'll make sure your request is recorded and reviewed.

Please send me:
1. The reason for your request
2. The transaction reference from your payment receipt or SMS

Please never share your PIN, password or any verification code. Your case number is {{ticket_id}}, and we will update you as soon as there is a decision.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ "{{product_name}}" የቡድን ምክክር ስላቀረቡት ጥያቄ እናመሰግናለን። የቡድን ምክክር ተመላሽ ገንዘብ ጥያቄዎች በByfluence ፖሊሲዎች መሰረት በቡድናችን ይታያሉ። ውጤቱን እኔ ራሴ ማረጋገጥ ባልችልም፣ ጥያቄዎ መመዝገቡን እና መታየቱን አረጋግጣለሁ።

እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የጥያቄዎን ምክንያት
2. ከክፍያ ደረሰኝዎ ወይም ከኤስኤምኤስ ላይ ያለውን የግብይት ቁጥር

እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ በፍጹም አያጋሩ። የጉዳይዎ ቁጥር {{ticket_id}} ነው፤ ውሳኔ እንደተሰጠ መረጃ እንሰጥዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, group session refund requests are reviewed under Byfluence policy — I can't confirm the outcome, but I'll record yours. Please send your reason and transaction reference (never your PIN or codes). Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የቡድን ምክክር ተመላሽ ጥያቄዎች በByfluence ፖሊሲ መሰረት ይታያሉ — ውጤቱን ማረጋገጥ ባልችልም ጥያቄዎን እመዘግባለሁ። እባክዎ ምክንያትዎን እና የግብይት ቁጥሩን ይላኩ (ፒን ወይም ኮድ በፍጹም አያጋሩ)። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your refund request for "{{product_name}}" is still under review. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለ"{{product_name}}" ያቀረቡት የተመላሽ ገንዘብ ጥያቄ አሁንም እየታየ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every group refund request → **Senior Support / Supervisor**; approved refunds → **Payments & Finance**.
- Many participants of one session requesting refunds → coordinated parent case, notify supervisor.

## Resolution Procedure
1. Authorized decision recorded and communicated; consistent across participants in the same situation.
2. Payments confirms processing if approved.

## Policy Pending Approval
- Approve group refund rules for every situation in the table, including deadlines and partial refunds.
- Decide whether seller-caused cancellations/no-shows trigger automatic refunds for all participants.
- Approve who authorizes group refunds.

## Internal Notes
- Consistency across participants is critical — check the parent ticket before replying.

<!-- doc -->
# Seller asks about low registration or cancelling for low attendance
id: grp-low-attendance-seller
type: article
category: group-consultations
subcategory: group-attendance
audience: seller
priority: medium
department: support_l2
features: consultations-group
tags: low registration, few participants, cancel group session low attendance, not enough people, minimum participants, ተሳታፊ አነሰ, ጥቂት ሰዎች ተመዘገቡ, መሰረዝ እፈልጋለሁ
related: grp-cancelled-by-seller, grp-rescheduled-session, grp-seller-create-group-session, grp-capacity-full, grp-refund-questions
templates: tpl-group-session-cancelled, tpl-reschedule-request
policy_pending: yes

## Summary
A seller has few registrations for a group session and asks whether they can cancel, postpone or merge the session — or how to get more participants.

## Issue Description
A seller expected more participants and feels the session isn't worth running. But the participants who **did** register have paid and planned for it. There is **no approved minimum-attendance rule** and no approved process for cancelling for low attendance. Support's role: explain the impact, discourage silent no-shows, record the request and escalate.

## Possible Causes
- Low visibility of the listing; short time between publishing and the session date.
- Price, topic or time (e.g., during working hours, Ethiopian-clock confusion) not suited to the audience.
- Seller set capacity high and expected to fill it.

## Information to Collect
- Session, date/time, capacity, current confirmed registrations
- What the seller wants: run anyway / postpone / cancel
- Proposed new date (if postponing)

## Troubleshooting Steps
1. Confirm registration numbers in the admin dashboard.
2. Explain to the seller that registered participants have paid; the preferred option is to run the session as planned.
3. If the seller insists on postponing/cancelling → record their reason and the proposed new date; tell them not to simply skip the session; escalate to **Senior Support / Supervisor** before any change.
4. If approved, follow `grp-rescheduled-session` or `grp-cancelled-by-seller` to inform all participants.
5. Offer general tips for future sessions: clear title and description in Amharic and English, time stated in both clocks, enough lead time, sharing the listing link on their own channels.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us about your group session "{{product_name}}" on {{booking_date}} at {{booking_time}} (EAT).

The participants who registered have already paid and planned their time, so where possible we encourage you to run the session as scheduled — smaller groups often allow more personal attention.

If you need to postpone or cancel, please don't simply skip the session. Tell us your reason and any new date you can offer, and our team will review it before anything changes. We'll then help inform the participants.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

በ{{booking_date}} በ{{booking_time}} (EAT) ስለሚካሄደው "{{product_name}}" የቡድን ምክክርዎ ስላገኙን እናመሰግናለን።

የተመዘገቡ ተሳታፊዎች አስቀድመው ከፍለው ጊዜያቸውን ያቀዱ በመሆናቸው፣ በተቻለ መጠን ምክክሩን በታቀደው ጊዜ እንዲያካሂዱ እናበረታታለን — አነስተኛ ቡድኖች ብዙ ጊዜ ለእያንዳንዱ ተሳታፊ የተሻለ ትኩረት ለመስጠት ያስችላሉ።

ማዛወር ወይም መሰረዝ ካስፈለገዎት፣ እባክዎ ዝም ብለው ምክክሩን አይተዉት። ምክንያትዎን እና ሊያቀርቡ የሚችሉትን አዲስ ቀን ይንገሩን፤ ማንኛውም ለውጥ ከመደረጉ በፊት ቡድናችን ያየዋል። ከዚያም ተሳታፊዎችን ለማሳወቅ እንረዳዎታለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, registered participants have already paid, so we encourage running the session as planned. If you must postpone or cancel, tell us your reason and a new date — please don't just skip it. We'll review first. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የተመዘገቡት ተሳታፊዎች አስቀድመው ስለከፈሉ ምክክሩን በታቀደው ጊዜ እንዲያካሂዱ እናበረታታለን። ማዛወር ወይም መሰረዝ ካለብዎት ምክንያትዎን እና አዲስ ቀን ይንገሩን — እባክዎ ዝም ብለው አይተዉት። መጀመሪያ እናየዋለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Seller wants to cancel or postpone a session with paid participants → **Senior Support / Supervisor**.
- Seller repeatedly cancels for low attendance → **Seller Operations**.

## Policy Pending Approval
- Decide whether sellers may set a minimum number of participants, and what happens if it is not reached (automatic cancellation and refunds?).
- Decide notice requirements for cancelling for low attendance.
- Decide whether participants must be offered a refund or a transfer when a session is cancelled for low attendance.

## Internal Notes
- Never approve a cancellation yourself. Encourage running the session — it protects buyers' trust in group sessions.
- Marketing advice must stay general; don't promise listing promotion by Byfluence.
