<!-- doc -->
# Missing Google Meet link
id: con-missing-meet-link
type: article
category: consultations
subcategory: meeting-access
audience: buyer
priority: high
department: technical
features: consultations-1on1, google-meet
tags: no meeting link, didn't receive meet link, google meet link missing, paid but no link, where is my link, how do I join, meeting link not sent, የስብሰባ ሊንክ አልደረሰኝም, ሊንክ የለም, Google Meet ሊንክ, ከፍዬ ሊንክ አልደረሰኝም
related: con-tsg-meeting-access-master, con-booking-confirmation, pay-paid-booking-not-confirmed, con-incorrect-meet-link, con-seller-meet-link-setup, con-tsg-no-show-decision-guide
templates: tpl-missing-meet-link, tpl-meet-link-resent, tpl-seller-contact-request, tpl-request-booking-details, tpl-waiting-for-seller
policy_pending: yes

## Summary
The buyer booked and paid for a consultation but did not receive the Google Meet link — e.g., "I booked a consultation and paid, but I didn't receive my meeting link." Time-sensitive: the closer the session, the higher the priority.

## Issue Description
A buyer has a booking (usually paid) but cannot find the link to join the Google Meet session. They may have looked in their email, SMS and dashboard. They are worried they will miss a session they paid for, and may suspect a scam. If the session starts soon, every minute matters — work the case **immediately** and keep the customer informed.

> [!WARNING] It is **not yet confirmed** whether Byfluence generates Google Meet links automatically or whether the seller adds them. Check the Feature Status page (`google-meet`) and the booking record, then follow **Path A** (link exists), **Path B** (automatic link missing) or **Path C** (seller-provided link missing) below.

### Urgency triage (set ticket priority first)
| Time until session | Priority | What to do |
|---|---|---|
| Session already started or starts within the hour | **Critical** | Work it now; contact the seller in parallel; notify a supervisor if not solved quickly. |
| Starts later today / within 24 hours | **High** | Resolve in this contact if possible. |
| More than a day away | **Medium** | Resolve normally; the link may simply not be issued yet. |
| Session time has passed | **High** | This is now a missed-session case — see Step 7. |

## Possible Causes
- The booking is **not confirmed** (payment pending/failed), so no meeting details were issued.
- The link exists in the booking, but the buyer is looking in the wrong place (email/SMS instead of the dashboard, or the wrong account).
- The confirmation message went to Spam/Promotions, or the registered email/phone has a typo.
- **(If links are automatic)** Google Meet link generation failed for this booking.
- **(If the seller adds links)** The seller has not yet added or shared the link.
- The link is only made visible close to the session time (if the system works this way — unconfirmed).
- The buyer is confused about the date/time and is looking at a different booking.

## Information to Collect
- Full name and registered email/phone
- Consultant name and consultation title
- Session date and time — confirm whether they mean EAT/international clock or Ethiopian clock
- Booking ID if they have it; otherwise transaction reference and payment time
- Where they have already looked (dashboard, email, SMS, Spam folder)
- Screenshot of the booking page in their dashboard (optional)

> [!WARNING] Never ask for passwords, OTP codes or PINs. Send the meeting link only to the verified booking owner, through the channel they are contacting from or their registered contact.

## Troubleshooting Steps
1. **Triage urgency.** Ask the session time first and set priority using the table above. If the session is within the hour, say so in the ticket and keep the conversation open.
2. **Verify identity** with the registered email or phone.
3. **Find the booking** in the admin dashboard (search by buyer, consultant, date; include pending and cancelled).
   - **Not confirmed / payment pending** → the link is not issued until confirmation. Follow `pay-paid-booking-not-confirmed` and mark High/Critical if the session is soon.
   - **Cancelled** → find out by whom; follow the matching cancellation article.
   - **Confirmed** → continue.
4. **Check the booking record for a meeting link.**
   ### Path A — link exists in the booking
   - Guide the buyer to dashboard → consultation bookings → open the booking.
   - If they still cannot find it, send the link yourself using `tpl-meet-link-resent`, together with the date and time in EAT (and Ethiopian clock in Amharic).
   - Check the link format is a genuine Google Meet link (`https://meet.google.com/xxx-xxxx-xxx`). Never send a link on another domain.
   ### Path B — link missing and links are generated automatically
   - This is a system failure → escalate to **Technical / Engineering** with booking ID, session time and seller name. Priority = triage level.
   - In parallel, if the session is soon, contact the seller (`tpl-seller-contact-request`) to ask them to create a Google Meet for the booked time and share it through support or the booking (see `con-seller-meet-link-setup`). Do not wait for engineering if the session starts soon.
   ### Path C — link missing and the seller is responsible for adding it
   - Contact the seller immediately (`tpl-seller-contact-request`), asking them to add the link to the booking (or send it to support to pass on).
   - Tell the buyer you are contacting the consultant (`tpl-missing-meet-link`).
   - If the seller does not respond and the session is close → **Senior Support / Supervisor**; keep the buyer updated (`tpl-waiting-for-seller`).
5. **Once you have a link**, send it to the buyer, confirm the time in EAT and the Ethiopian clock, and remind them to sign in to their Google account before joining.
6. **Stay with the customer** when the session is imminent: ask them to tell you once they are in. If they are stuck on "Ask to join", see `con-cannot-join-meet`.
7. **Session time already passed without a link** → do not decide the outcome. Collect evidence (when they contacted support, screenshots, messages with the seller), check whether the seller joined/created any meeting, and follow `con-tsg-no-show-decision-guide`. Escalate to **Senior Support / Supervisor**. Never promise a refund or a new session.
8. **Record** in the ticket: booking ID, path (A/B/C), who created the link, times of each action.

- [ ] Priority set by time until session
- [ ] Identity verified
- [ ] Booking status checked
- [ ] Link located or created
- [ ] Link sent and buyer confirmed receipt
- [ ] Seller informed (if they had to act)

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry you haven't received your meeting link. I understand how worrying this is when you have already paid.

I am checking your booking now. Your session details:
- Consultation: {{product_name}} with {{seller_name}}
- Date and time: {{booking_date}} at {{booking_time}} (EAT, international clock)
- Booking reference: {{consultation_id}}

[If you already have the link] Here is your Google Meet link: [paste link]. Please sign in to your Google account before you join, and join a little early to check your camera and microphone.

[If the link is not ready yet] I am working with the consultant and our team to get your link to you before the session. I will message you here as soon as I have it.

Please keep this chat open. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ የስብሰባ ሊንክዎ ስላልደረሰዎት ይቅርታ እንጠይቃለን። ከፍለው ሊንኩን ሳያገኙ ሲቀሩ ምን ያህል እንደሚያሳስብ ይገባኛል።

ቀጠሮዎን አሁኑኑ እያጣራሁ ነው። የምክክርዎ ዝርዝር፦
- ምክክር፦ {{product_name}} ከ{{seller_name}} ጋር
- ቀን እና ሰዓት፦ {{booking_date}} በ{{booking_time}} (EAT፣ በዓለም አቀፍ/የፈረንጅ አቆጣጠር)
- የቀጠሮ ቁጥር፦ {{consultation_id}}

[ሊንኩ ካለ] የGoogle Meet ሊንክዎ ይህ ነው፦ [ሊንኩን እዚህ ያስገቡ]። እባክዎ ከመግባትዎ በፊት በGoogle መለያዎ ይግቡ (sign in)፤ ካሜራዎን እና ማይክሮፎንዎን ለማረጋገጥም ትንሽ ቀደም ብለው ይቀላቀሉ።

[ሊንኩ ገና ካልተዘጋጀ] ከምክክሩ በፊት ሊንኩ እንዲደርስዎ ከአማካሪው እና ከቡድናችን ጋር እየሰራሁ ነው። ሊንኩን እንዳገኘሁ ወዲያውኑ እዚሁ እልክልዎታለሁ።

እባክዎ ይህን ውይይት ክፍት ያድርጉት። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about this! I'm checking your booking with {{seller_name}} ({{booking_date}}, {{booking_time}} EAT) right now and will send your Google Meet link here as soon as I have it. Please keep this chat open. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! ከ{{seller_name}} ጋር ያለዎትን ቀጠሮ ({{booking_date}}፣ {{booking_time}} EAT) አሁኑኑ እያጣራሁ ነው፤ የGoogle Meet ሊንክዎን እንዳገኘሁ እዚሁ እልክልዎታለሁ። እባክዎ ውይይቱን ክፍት ያድርጉት። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are still working with the consultant and our technical team to provide the meeting link for your session on {{booking_date}} at {{booking_time}} (EAT). Your booking {{consultation_id}} is confirmed and recorded. We will contact you again by {{follow_up_time}}, or sooner as soon as we have the link.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለ{{booking_date}} በ{{booking_time}} (EAT) ላለዎት ምክክር የስብሰባ ሊንኩን ለማቅረብ ከአማካሪው እና ከቴክኒክ ቡድናችን ጋር አሁንም እየሰራን ነው። ቀጠሮዎ {{consultation_id}} ተረጋግጦ ተመዝግቧል። እስከ {{follow_up_time}} ድረስ፣ ወይም ሊንኩን እንዳገኘን ቀደም ብለን እናገኝዎታለን።

## Escalation Conditions
- Links are automatic and the link is missing for a confirmed booking → **Technical / Engineering**, priority by triage (Critical if within the hour).
- Seller must provide the link and cannot be reached, with the session soon → **Senior Support / Supervisor**; keep the buyer updated.
- Several buyers report missing links at the same time → possible incident: **Technical / Engineering** + supervisor; check Announcements.
- Booking not confirmed despite payment → **Payments & Finance** (`pay-paid-booking-not-confirmed`).
- Session time passed without a working link → **Senior Support / Supervisor** (outcome decision; policy pending).
- The "link" the buyer received is not a Google Meet link, or asks for payment/login details → **Trust & Safety**.

## Resolution Procedure
1. The buyer confirms they have the correct Google Meet link and the correct time (EAT + Ethiopian clock).
2. Ideally confirm after the session that both parties joined.
3. Record: path (A/B/C), root cause (not confirmed / buyer couldn't find / generation failure / seller didn't add), who provided the link, timestamps.
4. If the session was missed or shortened, do not close — hand over to the no-show/incomplete-session process.

## Policy Pending Approval
- Confirm whether Google Meet links are generated automatically by Byfluence or added by the seller, and when they become visible to the buyer.
- Confirm whether support agents may relay a meeting link directly to the buyer, and through which channels.
- Decide what happens when a session is missed because no link was provided (rebook, refund, partial refund) and who decides.
- Decide seller obligations and consequences when a seller fails to provide a link (if links are seller-provided).
- Confirm whether buyers receive reminders with the link before the session.

## Internal Notes
- Ask **"When is your session?"** before anything else. A session in a few minutes changes how you work the case.
- Never send a link to anyone other than the verified booking owner. A meeting link shared with the wrong person is a privacy incident.
- Phishing risk: fake "Byfluence" messages with fake meeting links. Only `meet.google.com` links are genuine; never ask the buyer to log in through a link you send.
- Do not tell the buyer the seller "forgot" — say you are contacting the consultant.
- Record exact times (in EAT) when the buyer contacted support and when the link was delivered. If the session is later disputed, this timeline is key evidence.

<!-- doc -->
# Wrong or broken Google Meet link
id: con-incorrect-meet-link
type: article
category: consultations
subcategory: meeting-access
audience: both
priority: high
department: technical
features: consultations-1on1, google-meet
tags: wrong meet link, broken link, link not working, invalid meeting code, meeting not found, link expired, different meeting, ሊንኩ አይሰራም, የተሳሳተ ሊንክ, የስብሰባ ኮድ ልክ አይደለም
related: con-missing-meet-link, con-cannot-join-meet, con-tsg-meeting-access-master, con-seller-meet-link-setup, con-time-zone-confusion
templates: tpl-meet-link-resent, tpl-seller-contact-request, tpl-missing-meet-link
policy_pending: yes

## Summary
The buyer (or seller) has a meeting link but it does not work: it shows an error, leads to the wrong meeting, or the other party is waiting in a different meeting.

## Issue Description
Typical reports: "The link says the meeting code is invalid", "It says 'Check your meeting code'", "I'm in the meeting but the consultant isn't here — they say they're waiting too", "The link opens a meeting for another day", or "The link isn't a Google Meet link". If both parties are waiting in different meetings, each may later claim the other didn't show up — so record carefully.

## Possible Causes
- The link was copied incompletely (missing characters), or contains extra text/spaces from copying.
- The seller created a new meeting and shared a different link than the one in the booking (two different meetings).
- The buyer is using an old link from a previous or rescheduled booking.
- The link points to a meeting set up for a different date/time (calendar or time-zone error).
- The meeting was deleted/ended by the organizer, or access settings block the participant.
- System error in link generation (if automatic).
- **Suspicious:** the link is not on `meet.google.com`, or asks for payment or a login on another site.

## Information to Collect
- Booking ID or consultant name + session date/time
- The exact link they are using (copy-paste, not retyped)
- The exact error message or a screenshot of what they see
- Device (phone/computer), browser or app
- Whether the other party is waiting elsewhere (ask the seller which link they are in)

## Troubleshooting Steps
1. Set priority by time until session (Critical if the session is now).
2. Compare the link the customer is using with the link in the booking record.
   - **Different** → send the correct link (`tpl-meet-link-resent`).
   - **Same** → continue.
3. Check the link format: `https://meet.google.com/` followed by a code like `abc-defg-hij`. If it is on any other domain or asks for payment/credentials → tell the customer not to use it, and escalate to **Trust & Safety**.
4. If the session is now: contact the seller and ask **which link they are in**. Make sure both use one link — preferably the one in the booking. If the seller must create a new one, update both parties and record it.
5. If the meeting says the code is invalid or the meeting ended:
   - If links are automatic → **Technical / Engineering** with booking ID and screenshot; meanwhile ask the seller to create a meeting and share it via support.
   - If seller-provided → ask the seller to create a new link (`con-seller-meet-link-setup`).
6. If the link opens but says "You can't join this video call" or waits on "Asking to join" → `con-cannot-join-meet`.
7. If the link was for a different date (old/rescheduled booking) → confirm the current booking time in EAT and Ethiopian clock.
8. Record the original link, the corrected link and timestamps in internal notes.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us, and I'm sorry the meeting link isn't working. I've checked your booking {{consultation_id}} with {{seller_name}} for {{booking_date}} at {{booking_time}} (EAT).

Please use this Google Meet link for your session: [paste correct link]

A few tips:
- Open the link directly from this message rather than retyping it.
- Sign in to your Google account first.
- If you see an error, send me a screenshot and I'll help straight away.

I have also confirmed with the consultant that this is the link for your session. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን፤ የስብሰባ ሊንኩ ስላልሰራ ይቅርታ እንጠይቃለን። ከ{{seller_name}} ጋር ለ{{booking_date}} በ{{booking_time}} (EAT) ያለዎትን ቀጠሮ {{consultation_id}} አጣርቻለሁ።

እባክዎ ለምክክርዎ ይህን የGoogle Meet ሊንክ ይጠቀሙ፦ [ትክክለኛውን ሊንክ ያስገቡ]

ጥቂት ምክሮች፦
- ሊንኩን እንደገና ከመጻፍ ይልቅ ከዚህ መልዕክት በቀጥታ ይክፈቱት።
- መጀመሪያ በGoogle መለያዎ ይግቡ።
- ስህተት ካዩ ስክሪንሾት ይላኩልኝ፤ ወዲያውኑ እረዳዎታለሁ።

ይህ ሊንክ ለምክክርዎ መሆኑን ከአማካሪው ጋርም አረጋግጫለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about that! Please use this Google Meet link for your session with {{seller_name}}: [link]. Open it directly from this message and sign in to Google first. Send a screenshot if you see an error. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! ከ{{seller_name}} ጋር ላለዎት ምክክር ይህን የGoogle Meet ሊንክ ይጠቀሙ፦ [ሊንክ]። ከዚህ መልዕክት በቀጥታ ይክፈቱት፤ መጀመሪያ በGoogle መለያዎ ይግቡ። ስህተት ካዩ ስክሪንሾት ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our technical team is checking the meeting link problem for booking {{consultation_id}}. We are coordinating with {{seller_name}} so that you both use the same working link. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የቴክኒክ ቡድናችን የቀጠሮ {{consultation_id}}ን የሊንክ ችግር እያጣራ ነው። ሁለታችሁም አንድ አይነት የሚሰራ ሊንክ እንድትጠቀሙ ከ{{seller_name}} ጋር እያስተባበርን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Automatically generated links are invalid/broken → **Technical / Engineering** (High; Critical if the session is now or several bookings are affected).
- Buyer and seller waited in different meetings and the session was missed → **Senior Support / Supervisor** (dispute; see `con-tsg-no-show-decision-guide`).
- Link is not a Google Meet link, requests payment or credentials → **Trust & Safety**.
- A buyer received a link belonging to someone else's session → **Technical / Engineering** + **Trust & Safety** (privacy).

## Resolution Procedure
1. Both parties confirm they are using the same working link (ideally confirm they met).
2. Record the incorrect link, the corrected link, the cause and timestamps.
3. If session time was lost, open/attach the incomplete-session or duration-dispute process.

## Policy Pending Approval
- Confirm who generates Meet links and whether sellers may replace the link on a booking.
- Decide how missed or shortened sessions caused by a faulty link are handled, and who bears responsibility.

## Internal Notes
- "We were both waiting" is common and is nobody's fault if two links were in use. Screenshots from both sides, showing the meeting code and the clock, settle it.
- Never ask a customer to type a link from a screenshot — always send it as text.
- Ask sellers not to send links through unofficial channels if an official way exists; it creates link confusion.

<!-- doc -->
# Cannot join the Google Meet
id: con-cannot-join-meet
type: article
category: consultations
subcategory: meeting-access
audience: both
priority: high
department: support_l1
features: consultations-1on1, google-meet
tags: can't join meet, ask to join, waiting to be let in, you can't join this video call, google account required, camera permission, microphone blocked, Meet app, መግባት አልቻልኩም, ስብሰባው ውስጥ መግባት አልቻልኩም, Ask to join
related: con-tsg-meeting-access-master, con-incorrect-meet-link, con-meeting-connection-problems, con-seller-meet-link-setup, con-seller-late
templates: tpl-meet-link-resent, tpl-waiting-for-seller, tpl-seller-contact-request
policy_pending: yes

## Summary
The customer has the right Google Meet link but cannot get into the meeting: stuck on "Ask to join", told "You can't join this video call", asked to sign in, or blocked by camera/microphone permissions.

## Issue Description
This usually happens minutes before or after the session start, so it is **urgent**. The customer may be on a phone with limited data, not signed in to Google, or using an app/browser that does not support Meet well. Many buyers have never used Google Meet before.

## Possible Causes
| What they see | Likely cause | Fix |
|---|---|---|
| "Asking to join…" / waiting to be let in | The organizer (usually the seller) must admit them, and has not joined yet or has not seen the request | Contact the seller to join/admit; buyer stays on the screen |
| "You can't join this video call" | Organizer's settings block guests or people outside their organization; the request was denied or timed out; not signed in | Sign in to Google; seller changes access or admits; seller shares a new link |
| "Sign in to join" / asked for Google account | Some meetings require a Google account | Sign in or create a free Google account |
| No camera / microphone | Browser or phone permission blocked | Allow camera/mic in browser or phone settings |
| Link opens Play Store / App Store | Phone wants the Google Meet app | Install the app, or open the link in Chrome |
| Page does not load | Connection, old browser, blocked network | See `con-meeting-connection-problems` |

## Information to Collect
- Booking ID or consultant name + session time
- Exact message on screen (screenshot if possible)
- Device (Android/iPhone/computer) and app/browser used
- Whether they are signed in to a Google account
- Whether the seller has joined (ask the seller if you can reach them)

> [!WARNING] Never ask for the customer's Google password or verification codes. If they cannot sign in to Google, they must recover it with Google directly.

## Troubleshooting Steps
1. Confirm the session time and that they are using the correct link (compare with the booking record). Wrong link → `con-incorrect-meet-link`.
2. Identify what they see (table above).
3. **Stuck on "Asking to join"** → ask them to stay on that screen. Contact the seller (`tpl-seller-contact-request`) to join and admit the buyer. Tell the buyer you are contacting the consultant (`tpl-waiting-for-seller`). If the seller does not respond → `con-seller-late`.
4. **"You can't join this video call"** → ask the buyer to:
   - sign in to a Google account (in the browser or the Meet app), then open the link again;
   - try again once (a request that was denied or timed out cannot be resent many times).
   If still blocked, ask the seller to check their meeting access settings or create a new link that allows the buyer (see `con-seller-meet-link-setup`).
5. **No Google account** → explain they can create a free Google account, or try joining from a computer browser (Chrome) if the meeting allows guests. If time is short, the seller can admit them after sign-in.
6. **Camera/microphone blocked** → computer: click the camera icon in the address bar → Allow; phone: Settings → Apps → Meet/Chrome → Permissions → allow Camera and Microphone. Then rejoin.
7. **Phone**: the Google Meet app is most reliable; otherwise use Chrome (Android) or Safari/Chrome (iPhone). Gmail app users can also join from the Meet tab.
8. If both are in the meeting but cannot hear/see each other → `con-meeting-connection-problems`.
9. Record what was blocking and the times (EAT) of each step. If the session lost time, note it for a possible duration dispute.

## Recommended Response (EN)
Hello {{customer_name}},

I'm sorry you're having trouble getting into your session. Let's fix this quickly:

1. Please make sure you are signed in to a Google account, then open the meeting link again.
2. If you see "Asking to join", please stay on that screen — the consultant needs to let you in. I am contacting {{seller_name}} now.
3. If your camera or microphone is blocked, allow access in your browser or phone settings, then rejoin.
4. On a phone, the Google Meet app usually works best.

If you see a different message, please send me a screenshot. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ወደ ምክክሩ ለመግባት በመቸገርዎ ይቅርታ እንጠይቃለን። በፍጥነት እናስተካክለው፦

1. እባክዎ በGoogle መለያዎ መግባትዎን (sign in) ያረጋግጡ፤ ከዚያም የስብሰባ ሊንኩን እንደገና ይክፈቱ።
2. "Asking to join" የሚል ካዩ፣ እባክዎ በዚያው ገጽ ላይ ይቆዩ — አማካሪው ሊያስገባዎ ይገባል። አሁኑኑ {{seller_name}}ን እያገኘሁ ነው።
3. ካሜራዎ ወይም ማይክሮፎንዎ ከታገደ፣ በብሮውዘርዎ ወይም በስልክዎ ማስተካከያ (Settings) ውስጥ ይፍቀዱ፤ ከዚያ እንደገና ይግቡ።
4. በስልክ ከሆነ፣ የGoogle Meet መተግበሪያ (app) ብዙውን ጊዜ የተሻለ ይሰራል።

ሌላ መልዕክት ካዩ፣ እባክዎ ስክሪንሾት ይላኩልኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! Sign in to Google, then reopen the link. If it says "Asking to join", stay on that screen — I'm contacting {{seller_name}} to let you in. Send a screenshot if you see another message. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! በGoogle መለያዎ ይግቡ፣ ከዚያ ሊንኩን እንደገና ይክፈቱ። "Asking to join" ካለ በዚያው ገጽ ይቆዩ — {{seller_name}} እንዲያስገባዎ እያገኘሁ ነው። ሌላ መልዕክት ካዩ ስክሪንሾት ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have contacted {{seller_name}} about letting you into the meeting for booking {{consultation_id}}. We have recorded the time you tried to join. We will update you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለቀጠሮ {{consultation_id}} ወደ ስብሰባው እንዲያስገባዎ {{seller_name}}ን አግኝተናል። ለመግባት የሞከሩበትን ሰዓት መዝግበናል። እስከ {{follow_up_time}} ድረስ በድጋሚ መረጃ እንሰጥዎታለን።

## Escalation Conditions
- Seller cannot be reached while the buyer waits to be admitted → follow `con-seller-late`; **Senior Support / Supervisor** if the session time passes.
- Automatically created meetings block buyers by default (settings issue in the integration) → **Technical / Engineering**, High.
- Buyer could not join at all and the session was lost → **Senior Support / Supervisor** (`con-tsg-no-show-decision-guide`).
- Customer reports their Google account is hacked → advise Google account recovery; if their Byfluence account is also affected → **Trust & Safety**.

## Resolution Procedure
1. Customer confirms they are in the meeting with the other party.
2. Record the blocker (not admitted / not signed in / permissions / app) and the time lost.
3. If time was lost, note it so a later duration complaint can be assessed.

## Policy Pending Approval
- Confirm the required Google Meet access settings for consultation meetings (e.g., whether buyers must be admitted manually) and who owns the meeting (Byfluence account or seller account).
- Decide how lost time caused by access problems is treated.

## Internal Notes
- "Ask to join" with no response almost always means the organizer is not in the meeting yet. Treat it as a possible late seller and start the clock.
- Keep a simple screenshot guide for camera/mic permissions on Android and iPhone in your saved replies.
- Do not ask the buyer to repeatedly click "Ask to join" — repeated requests can be blocked by Google for a while.

<!-- doc -->
# Audio, video or connection problems during the session
id: con-meeting-connection-problems
type: article
category: consultations
subcategory: meeting-access
audience: both
priority: medium
department: support_l1
features: consultations-1on1, google-meet
tags: no sound, can't hear, video freezing, bad connection, call dropped, internet problem, power cut, poor network, ድምፅ አይሰማም, ኢንተርኔት ተቋረጠ, ቪዲዮ ቆሟል, ኔትወርክ የለም
related: con-cannot-join-meet, con-incomplete-consultation, con-duration-dispute, con-tsg-meeting-access-master, con-reschedule-request-buyer
templates: tpl-request-booking-details, tpl-reschedule-request
policy_pending: yes

## Summary
The buyer and seller are in the Google Meet, or were, but audio, video or the connection is failing — including dropped calls caused by mobile data, Wi-Fi or power outages.

## Issue Description
In Ethiopia, unstable mobile data, low bandwidth, power cuts and occasional regional network disruptions are common causes of poor session quality. Customers may contact support during the session ("I can't hear the consultant") or after it ("the call kept dropping, I want my money back"). During the session, help them recover quickly; after the session, collect facts for the incomplete-session process.

## Possible Causes
- Weak or unstable mobile data / Wi-Fi; data bundle ran out.
- Power outage affecting the router or a laptop without battery.
- Regional network disruption (affects one side or both).
- Microphone muted, wrong speaker/microphone selected, or headphones not connected.
- Browser/phone permissions block mic or camera.
- Many apps or browser tabs using bandwidth; phone in power-saving mode.
- Old browser or device; Meet app not updated.

## Information to Collect
- Booking ID / consultant name + session time
- Who has the problem (buyer, seller, both) and what exactly (no sound, frozen video, dropped)
- Device and connection type (mobile data, Wi-Fi)
- When it started and how much of the session was affected (approximate times in EAT)
- After the session: whether they rejoined, and screenshots or messages exchanged with the other party

## Troubleshooting Steps
### During the session (fast fixes, in this order)
1. **Check mute**: the microphone icon in Meet should not be red; ask the other party to unmute too.
2. **Check audio device**: in Meet, More options (⋮) → Settings → Audio — select the right microphone/speaker; unplug/replug headphones.
3. **Turn off video** (camera icon) on both sides — audio-only uses much less data and often fixes freezing.
4. **Leave and rejoin** the meeting with the same link.
5. **Switch network**: from Wi-Fi to mobile data or the other way; move closer to the router or a window.
6. **Close other apps/tabs** and downloads; turn off power-saving mode.
7. **Switch device** if one is available (e.g., from laptop to phone with the Meet app).
8. If the problem is only on one side, tell that side; it is not the other party's fault.

### After the session
1. Ask how much of the session was lost and whether the seller offered to continue or reschedule.
2. If both agree on a continuation/new time → help them arrange it through the booking (`con-reschedule-request-buyer` / `-seller`).
3. If they disagree or the buyer wants compensation → `con-incomplete-consultation`; collect evidence; escalate to **Senior Support / Supervisor**. Do not promise a refund or a new session.

## Recommended Response (EN)
Hello {{customer_name}},

I'm sorry you're having connection problems in your session. Please try these quick steps:

1. Check that your microphone is not muted, and ask the consultant to check theirs.
2. Turn off your camera — audio-only uses much less internet and often fixes freezing.
3. Leave the meeting and rejoin with the same link.
4. If possible, switch between Wi-Fi and mobile data, and close other apps.

If the session was seriously affected, please tell me roughly when the problems started and how much time was lost. Your case number is {{ticket_id}}, and we will review what happened.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

በምክክርዎ ወቅት የግንኙነት ችግር ስላጋጠመዎት ይቅርታ እንጠይቃለን። እባክዎ እነዚህን ፈጣን ደረጃዎች ይሞክሩ፦

1. ማይክሮፎንዎ ድምፅ ያልተዘጋ (mute ያልሆነ) መሆኑን ያረጋግጡ፤ አማካሪውም የራሱን/የራሷን እንዲያረጋግጥ ይጠይቁ።
2. ካሜራዎን ያጥፉ — ድምፅ ብቻ መጠቀም በጣም ያነሰ ኢንተርኔት ይወስዳል፤ መቆራረጡንም ብዙ ጊዜ ያስተካክላል።
3. ከስብሰባው ወጥተው በዚያው ሊንክ እንደገና ይግቡ።
4. ከተቻለ በWi-Fi እና በሞባይል ዳታ መካከል ይቀያይሩ፤ ሌሎች መተግበሪያዎችንም ይዝጉ።

ምክክሩ በከፍተኛ ሁኔታ ከተስተጓጎለ፣ እባክዎ ችግሩ በግምት መቼ እንደጀመረ እና ምን ያህል ጊዜ እንደባከነ ይንገሩኝ። የጉዳይዎ ቁጥር {{ticket_id}} ነው፤ የሆነውንም እናጣራለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about this! Try: unmute → turn camera off (audio-only) → leave and rejoin the same link → switch Wi-Fi/mobile data. If time was lost, tell me roughly how much. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ! ይሞክሩ፦ mute ያንሱ → ካሜራ ያጥፉ (ድምፅ ብቻ) → ወጥተው በዚያው ሊንክ ይግቡ → Wi-Fi/ሞባይል ዳታ ይቀይሩ። ጊዜ ከባከነ በግምት ምን ያህል እንደሆነ ይንገሩኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have recorded the connection problems during your session {{consultation_id}} with {{seller_name}} and are reviewing what happened with both sides. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ከ{{seller_name}} ጋር በነበረዎት ምክክር {{consultation_id}} ወቅት የተፈጠረውን የግንኙነት ችግር መዝግበናል፤ ከሁለቱም ወገን ጋር ሆነን የሆነውን እያጣራን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Significant session time lost and the parties do not agree on a continuation → **Senior Support / Supervisor** (`con-incomplete-consultation`).
- Many sessions affected at the same time, or the problem looks like a Meet integration issue → **Technical / Engineering**.
- One party accuses the other of deliberately leaving or faking connection problems → **Senior Support / Supervisor**.

## Resolution Procedure
1. During the session: customer confirms the call is working.
2. After the session: record lost time, cause (buyer side / seller side / both / unknown), and whether a continuation was agreed.
3. Link the ticket to any duration or incomplete-session case.

## Policy Pending Approval
- Decide how sessions affected by connection problems are handled (continuation, reschedule, partial refund) and whether it matters which side had the problem.
- Decide whether sellers are expected to offer extra time or a continuation when the problem was on their side.

## Internal Notes
- Connectivity problems are often nobody's "fault". Avoid blaming language with either party.
- Ask for approximate times (EAT) while the memory is fresh — this is your main evidence later.
- If a regional internet disruption is reported in the news or by several customers, inform the supervisor so cases are handled consistently.

<!-- doc -->
# Time-zone or wrong-time confusion
id: con-time-zone-confusion
type: article
category: consultations
subcategory: meeting-access
audience: both
priority: high
department: support_l1
features: consultations-1on1, google-meet
tags: wrong time, time zone, Ethiopian time, ሰዓት አቆጣጠር, EAT, missed session wrong time, Ethiopian calendar, Gregorian date, diaspora time, የኢትዮጵያ ሰዓት, በፈረንጅ ሰዓት, የተሳሳተ ሰዓት
related: con-select-time-slot, tec-calendar-time-display, con-tsg-no-show-decision-guide, con-buyer-no-show, con-seller-no-show, grp-scheduling-time-zones
templates: tpl-request-booking-details, tpl-reschedule-request
policy_pending: yes

## Summary
The buyer or seller came at the wrong time — or fears they will — because of Ethiopian-clock vs international-clock confusion, time zones, or Ethiopian vs Gregorian calendar dates. This is one of the most common real causes of "no-shows".

## Issue Description
Ethiopia uses **East Africa Time (EAT, UTC+3)**, with no daylight saving. But many Ethiopians tell time with the **Ethiopian clock (የኢትዮጵያ ሰዓት አቆጣጠር)**, where the day's hours are counted from about sunrise: **6:00 AM international = 12 o'clock (ንጋት/ጠዋት 12 ሰዓት)** and **7:00 AM = ጠዋት 1 ሰዓት**. So "3 o'clock" in Ethiopian time (ጠዋት 3 ሰዓት) is **9:00 AM** international. A session listed as "9:00" can be read as ሰዓት 9 (= 3:00 PM), producing a six-hour mistake.

In addition:
- **Ethiopian calendar dates** differ from Gregorian dates (13 months; the year number is 7–8 years behind; months start on different days). A buyer who says "ኅዳር 12" means an Ethiopian date, not "November 12".
- **Diaspora users** (abroad) or phones set to another time zone may see times converted to their local time, or may forget to convert.
- How Byfluence displays times (always EAT, or the device's time zone) is **not yet confirmed** (`tec-calendar-time-display`).

### Ethiopian clock ↔ international clock (EAT)
Rule: **Ethiopian hour = international hour − 6** (and the period of day tells you which half).

| International (EAT) | Ethiopian clock | Period word |
|---|---|---|
| 6:00 AM | 12:00 | ንጋት / ጠዋት 12 ሰዓት |
| 7:00 AM | 1:00 | ጠዋት 1 ሰዓት |
| 9:00 AM | 3:00 | ጠዋት 3 ሰዓት |
| 12:00 PM (noon) | 6:00 | ቀን 6 ሰዓት |
| 2:00 PM | 8:00 | ከሰዓት 8 ሰዓት |
| 3:00 PM | 9:00 | ከሰዓት 9 ሰዓት |
| 6:00 PM | 12:00 | ምሽት 12 ሰዓት |
| 7:00 PM | 1:00 | ምሽት 1 ሰዓት |
| 8:00 PM | 2:00 | ማታ 2 ሰዓት |
| 12:00 AM (midnight) | 6:00 | ሌሊት 6 ሰዓት |

### Ethiopian calendar months (approximate Gregorian start)
Meskerem/መስከረም (~Sep 11), Tikimt/ጥቅምት (~Oct 11), Hidar/ኅዳር (~Nov 10), Tahsas/ታኅሣሥ (~Dec 10), Tir/ጥር (~Jan 9), Yekatit/የካቲት (~Feb 8), Megabit/መጋቢት (~Mar 10), Miyazia/ሚያዝያ (~Apr 9), Ginbot/ግንቦት (~May 9), Sene/ሰኔ (~Jun 8), Hamle/ሐምሌ (~Jul 8), Nehase/ነሐሴ (~Aug 7), Pagume/ጳጉሜ (~Sep 6, 5–6 days). Exact start dates shift by one day in some years — **always confirm with a reliable converter and the weekday**.

## Possible Causes
- Buyer or seller read the international time as Ethiopian clock time (or the reverse).
- AM/PM misread (e.g., 8:00 PM read as 8 in the morning).
- Ethiopian calendar date confused with the Gregorian date.
- Device set to the wrong time zone, or a user abroad did not convert.
- The seller set availability in Ethiopian clock by mistake, so the slot is 6 hours off from what they intended.
- A display bug shows the wrong time zone in the dashboard or notifications.

## Information to Collect
- Booking ID / consultant name
- The time and date **as the customer understood it**, in their own words (e.g., "ጠዋት 3 ሰዓት on Tuesday")
- Screenshot of the booking time as shown in their dashboard or notification
- Their location (Ethiopia or abroad) and their phone's time zone setting
- What time they actually tried to join (EAT)

## Troubleshooting Steps
1. Read the booking time from the admin record (and note which time zone the record uses).
2. Restate it to the customer in **all forms**: weekday + Gregorian date + international time + "EAT" + Ethiopian clock in Amharic. Example: "Tuesday, {{booking_date}}, 9:00 AM EAT — ማክሰኞ ጠዋት 3 ሰዓት".
3. If the customer is abroad, also state their local time (convert from UTC+3) and say which you are using.
4. Compare with what the customer understood:
   - **Session still ahead** → confirm the correct time; ask them to reply with the time in their own words to be sure.
   - **Session missed because of confusion** → do not blame. Collect what happened on both sides (who joined when) and follow `con-tsg-no-show-decision-guide`. A reschedule may be possible if both agree (`con-reschedule-request-buyer` / `-seller`). Outcome decisions are policy pending.
   - **Dashboard/notification shows a different time from the admin record** → **Technical / Engineering** (`tec-calendar-time-display`), High.
   - **Seller's availability was set in Ethiopian clock by mistake** → help the seller fix future availability (`con-seller-availability-setup`); for existing bookings, contact both sides to confirm the intended time.
5. Record the time confusion type in the ticket (Ethiopian clock / AM-PM / calendar / time zone / display bug).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for checking with us — times can easily be confusing, so let me confirm your session clearly:

- Consultation: {{product_name}} with {{seller_name}}
- Date: {{booking_date}} (please check the weekday)
- Time: {{booking_time}} East Africa Time (EAT), international clock

If you usually use the Ethiopian clock, please note the difference: for example, 9:00 AM international time is 3 o'clock in the morning in Ethiopian time (ጠዋት 3 ሰዓት), and 2:00 PM is ከሰዓት 8 ሰዓት.

If you are outside Ethiopia, please convert from EAT (UTC+3) to your local time.

Could you reply with the time in your own words so we are sure we agree? Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላረጋገጡ እናመሰግናለን — የሰዓት አቆጣጠር በቀላሉ ሊያምታታ ስለሚችል ቀጠሮዎን በግልጽ ላረጋግጥልዎት፦

- ምክክር፦ {{product_name}} ከ{{seller_name}} ጋር
- ቀን፦ {{booking_date}} (እባክዎ የሳምንቱን ቀን ያረጋግጡ)
- ሰዓት፦ {{booking_time}} በምሥራቅ አፍሪካ ሰዓት (EAT)፣ በዓለም አቀፍ (የፈረንጅ) አቆጣጠር
- በኢትዮጵያ አቆጣጠር፦ [ለምሳሌ፦ ጠዋት 3 ሰዓት]

ልዩነቱን ልብ ይበሉ፦ ለምሳሌ በፈረንጅ አቆጣጠር 9:00 AM በኢትዮጵያ አቆጣጠር ጠዋት 3 ሰዓት ነው፤ 2:00 PM ደግሞ ከሰዓት 8 ሰዓት ነው።

ከኢትዮጵያ ውጭ ከሆኑ፣ እባክዎ ሰዓቱን ከEAT (UTC+3) ወደ አካባቢዎ ሰዓት ይቀይሩ።

ሁለታችንም በአንድ ሰዓት ላይ መስማማታችንን ለማረጋገጥ፣ ሰዓቱን በራስዎ አገላለጽ መልሰው ቢጽፉልኝ? የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! Your session is {{booking_date}} at {{booking_time}} EAT (international clock). Note: 9:00 AM international = ጠዋት 3 ሰዓት in Ethiopian time. Please reply with the time in your own words so we're sure. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! ምክክርዎ {{booking_date}} በ{{booking_time}} EAT (በፈረንጅ አቆጣጠር) ነው — በኢትዮጵያ አቆጣጠር [ለምሳሌ ጠዋት 3 ሰዓት]። ለማረጋገጥ እባክዎ ሰዓቱን በራስዎ አገላለጽ መልሰው ይጻፉልኝ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are reviewing the time mix-up for your session {{consultation_id}} with {{seller_name}} and have asked both sides what happened. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ከ{{seller_name}} ጋር ስለነበረዎት ምክክር {{consultation_id}} የሰዓት መምታታት እያጣራን ሲሆን፣ ሁለቱንም ወገኖች የሆነውን ጠይቀናል። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Displayed time differs from the booking record, or a time zone is applied wrongly → **Technical / Engineering**, High.
- A session was missed due to time confusion and either party wants a refund, compensation or penalty → **Senior Support / Supervisor**.
- Several customers misread the same display format → report to supervisor as a product issue (labelling).

## Resolution Procedure
1. The customer confirms the correct time in their own words.
2. If missed: reschedule agreed by both, or case handed to Senior Support with evidence.
3. Record the confusion type and how it was resolved.

## Policy Pending Approval
- Confirm which time zone Byfluence uses to display booking times (EAT always vs device time zone) and in notifications.
- Decide whether the platform should show Ethiopian-clock equivalents for Amharic users.
- Decide who bears responsibility when a session is missed because of time confusion (and whether a free reschedule is allowed).

## Internal Notes
- **Always** write times as: weekday + Gregorian date + international time + "EAT", and add Ethiopian clock in Amharic messages. Never write a bare "3:00".
- Asking the customer to repeat the time "in their own words" catches most mistakes.
- The weekday is the easiest cross-check for Ethiopian vs Gregorian dates.
- Late-evening and night sessions are especially confusing (ማታ, ሌሊት). Be extra careful.
- Use a reliable Ethiopian–Gregorian converter; do not convert dates from memory.

<!-- doc -->
# Seller: providing and checking the Google Meet link
id: con-seller-meet-link-setup
type: article
category: consultations
subcategory: meeting-access
audience: seller
priority: medium
department: support_l1
features: consultations-1on1, google-meet
tags: seller meet link, create google meet, how to add meeting link, admit buyer, meeting settings, host meeting, የስብሰባ ሊንክ መፍጠር, Google Meet መፍጠር, ሊንክ ማጋራት
related: con-missing-meet-link, con-cannot-join-meet, con-incorrect-meet-link, con-seller-availability-setup, con-tsg-meeting-access-master
templates: tpl-seller-contact-request, tpl-meet-link-resent
policy_pending: yes

## Summary
Guides a seller on how the Google Meet link for a booking works, how to create one if the seller is responsible for it, and how to make sure the buyer can get in.

## Overview
It is **not yet confirmed** whether Byfluence creates Google Meet links automatically for each booking or whether sellers add them. Check the Feature Status page (`google-meet`) before advising.

- **If links are automatic:** the seller should open the booking in their dashboard, find the link, and join from it at the session time. They should not create a different meeting unless support asks — two different links cause "we were both waiting" disputes.
- **If the seller adds the link** (or support asks the seller to create one because the automatic link failed): the seller creates a Google Meet and adds it to the booking or sends it to support.

### Seller checklist before every session
1. Open the booking and confirm the date and time in EAT (and in Ethiopian clock if you think that way).
2. Make sure the booking has **one** Google Meet link, and that it is the one you will use.
3. Sign in to the Google account that owns or is invited to the meeting.
4. Join **a little early**, so you can admit the buyer as soon as they ask to join.
5. Keep your phone/notifications on so support can reach you if the buyer cannot get in.

## Customer Steps
1. Go to meet.google.com (or the Google Meet app) and sign in.
2. Choose **New meeting → Create a meeting for later** and copy the link (format `https://meet.google.com/abc-defg-hij`). Alternatively, create a Google Calendar event at the booked time with Google Meet video conferencing.
3. Add the link to the booking (if the booking has a meeting-link field) or send it to Byfluence Support to pass on — as instructed by support.
4. At the session time, join early and **admit** the buyer when "Someone wants to join" appears.
5. If the buyer says "You can't join this video call", check your meeting's host controls/access settings so that invited guests or people with the link can ask to join, then admit them.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. Here is how to make sure your buyer can join your session on {{booking_date}} at {{booking_time}} (EAT):

1. Open the booking in your dashboard and check the Google Meet link.
2. [If you need to create the link] Go to meet.google.com, choose "New meeting" → "Create a meeting for later", copy the link, and [add it to the booking / send it to us here].
3. Sign in to your Google account and join a little early.
4. When the buyer asks to join, admit them promptly.

Please use only one link for the session, so you and the buyer end up in the same meeting. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ገዢዎ በ{{booking_date}} በ{{booking_time}} (EAT) ወደ ምክክሩ መግባት እንዲችል እንደሚከተለው ያድርጉ፦

1. ቀጠሮውን በዳሽቦርድዎ ውስጥ ይክፈቱ እና የGoogle Meet ሊንኩን ያረጋግጡ።
2. [ሊንኩን መፍጠር ካስፈለገ] ወደ meet.google.com ይሂዱ፣ "New meeting" → "Create a meeting for later" ይምረጡ፣ ሊንኩን ይቅዱ እና [በቀጠሮው ላይ ያስገቡት / እዚሁ ይላኩልን]።
3. በGoogle መለያዎ ይግቡ እና ትንሽ ቀደም ብለው ስብሰባውን ይቀላቀሉ።
4. ገዢው ለመግባት ሲጠይቅ፣ ፈጥነው ያስገቡት (Admit)።

እርስዎ እና ገዢው አንድ ስብሰባ ውስጥ እንድትገናኙ፣ እባክዎ ለምክክሩ አንድ ሊንክ ብቻ ይጠቀሙ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! Check the Meet link in your booking (or create one: meet.google.com → New meeting → Create a meeting for later, and send it to us). Join a little early and admit the buyer. Use one link only. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! በቀጠሮዎ ውስጥ ያለውን የMeet ሊንክ ያረጋግጡ (ወይም ይፍጠሩ፦ meet.google.com → New meeting → Create a meeting for later፣ ከዚያ ይላኩልን)። ትንሽ ቀደም ብለው ገብተው ገዢውን ያስገቡ። አንድ ሊንክ ብቻ ይጠቀሙ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Automatic link missing or broken for the seller's booking → **Technical / Engineering**.
- Seller cannot add a link to the booking although that is the expected process → **Technical / Engineering**.
- Seller refuses to use the platform's link and insists on another app (Zoom, Telegram call, WhatsApp) → **Senior Support / Supervisor** (marketplace rules pending).

## Policy Pending Approval
- Confirm whether links are automatic or seller-provided, and which Google account owns the meeting.
- Decide whether sellers may use a different meeting tool if the buyer agrees.
- Confirm the required meeting access settings (who can join without being admitted).

## Internal Notes
- Ask sellers to join early: most "can't get in" cases are buyers waiting for an absent host.
- If a seller sends you a link to pass on, check it is a `meet.google.com` link before forwarding it.
- Remind sellers not to collect buyers' personal contacts or move communication off-platform for payments.

<!-- doc -->
# Master guide: meeting link & access problems
id: con-tsg-meeting-access-master
type: troubleshooting
category: consultations
subcategory: meeting-access
audience: both
priority: high
department: support_l1
features: consultations-1on1, consultations-group, google-meet
tags: meeting problems, can't join session, meet link issues, session access, urgent session, troubleshooting meeting, የስብሰባ ችግር, መግባት አልቻልኩም, ሊንክ ችግር
related: con-missing-meet-link, con-incorrect-meet-link, con-cannot-join-meet, con-meeting-connection-problems, con-time-zone-confusion, con-tsg-no-show-decision-guide
templates: tpl-missing-meet-link, tpl-meet-link-resent, tpl-waiting-for-seller, tpl-seller-contact-request
policy_pending: yes

## Summary
One diagnostic playbook for every "I can't get into my session" contact — missing link, wrong link, blocked access, connection problems and wrong-time confusion — ordered so the agent can act fast when a session is about to start.

## Overview
Meeting access problems are the highest-pressure consultation contacts: the customer is usually minutes away from a session they paid for. Work in this order: **time → booking → link → access → connection**. Each step routes to a detailed article. Keep the conversation open and update the customer often; silence feels like abandonment.

Key facts:
- Whether Meet links are automatic or seller-provided is **unconfirmed** — check Feature Status (`google-meet`).
- A scheduled meeting does not prove the session happened. Record times (EAT) for everything.
- Always state times as weekday + date + international time + EAT (+ Ethiopian clock in Amharic).

## Information to Collect
- Session date and time (as the customer understands it)
- Booking ID or consultant name; registered email/phone for identity
- What they see on screen (screenshot), device and app/browser
- Whether the other party is reachable / already in a meeting

## Troubleshooting Steps
### Step 1 — When is the session?
- Already started / within the hour → **Critical**. Tell the customer you are on it; contact the seller in parallel.
- Later today → **High**. Within days → **Medium**.
- Already passed → this is a missed/incomplete session: go to `con-tsg-no-show-decision-guide`.

### Step 2 — Is the time understood correctly?
Restate the booking time in both clocks. If the customer is early/late by about six hours, or on the wrong day → `con-time-zone-confusion`.

### Step 3 — Is the booking confirmed?
- Not confirmed / payment pending → `pay-paid-booking-not-confirmed` (no confirmed booking = no link).
- Cancelled or rescheduled → check by whom; matching changes article.
- Not in dashboard but confirmed → `con-booking-not-in-dashboard`.

### Step 4 — Does the customer have a link?
- No link → `con-missing-meet-link` (Path A/B/C).
- Has a link but it errors, or leads to a different meeting → `con-incorrect-meet-link`.

### Step 5 — Can they get into the meeting?
- "Asking to join" with no response → seller not present: contact seller → `con-cannot-join-meet` / `con-seller-late`.
- "You can't join this video call", sign-in required, permissions → `con-cannot-join-meet`.

### Step 6 — Are they in, but can't hear/see?
→ `con-meeting-connection-problems`.

### Step 7 — Close the loop
- Confirm with the customer that they are in the session.
- After the session, if time was lost → `con-incomplete-consultation` or `con-duration-dispute`.
- Record the step where the problem was and the times.

### Quick decision table
| Symptom | Go to |
|---|---|
| "I paid but have no link" | `con-missing-meet-link` |
| "Invalid meeting code" / different meeting | `con-incorrect-meet-link` |
| "Asking to join" forever | `con-cannot-join-meet` + `con-seller-late` |
| "You can't join this video call" | `con-cannot-join-meet` |
| "No sound / frozen / dropped" | `con-meeting-connection-problems` |
| "Nobody is here" (but six hours off) | `con-time-zone-confusion` |
| "The consultant never came" | `con-seller-no-show` |
| Group session participant | `grp-join-group-meeting`, `grp-missing-link`, `grp-participant-access-denied` |

## Short Response (EN)
Hi {{customer_name}}, I'm on it right now. Please confirm your session time and stay in this chat — I'm checking your booking and will get you into your meeting as quickly as possible. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ አሁኑኑ እየሰራሁበት ነው። እባክዎ የምክክርዎን ሰዓት ያረጋግጡልኝ እና በዚህ ውይይት ላይ ይቆዩ — ቀጠሮዎን እያጣራሁ ነው፤ በተቻለ ፍጥነት ወደ ስብሰባዎ እንዲገቡ አደርጋለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Session imminent and the blocker is on the platform side (no link, broken automatic link) → **Technical / Engineering**, Critical; inform supervisor.
- Seller unreachable at session time → **Senior Support / Supervisor**.
- Many customers affected simultaneously → incident: **Technical / Engineering** + supervisor; check Announcements.
- Suspicious links or off-platform payment requests → **Trust & Safety**.
- Session lost entirely → **Senior Support / Supervisor** via `con-tsg-no-show-decision-guide`.

## Resolution Procedure
1. Customer confirms they joined and the session is running.
2. Ticket records: step where the problem was, root cause, all timestamps (EAT), who fixed what.
3. Any lost time is linked to a duration/incomplete-session case — never closed silently.

## Policy Pending Approval
- Confirm Meet link ownership and generation (automatic vs seller-provided).
- Confirm the official response-time target for imminent-session contacts.
- Decide outcomes for sessions lost because of access problems on the platform side, the seller side or the buyer side.

## Internal Notes
- Imminent-session contacts jump the queue. Tell your shift lead if you are handling one and need help with other tickets.
- Send a message at least every few minutes while the customer waits — even "Still contacting the consultant".
- Keep your own timeline in internal notes: customer contact time, seller contacted time, link sent time, joined time.
