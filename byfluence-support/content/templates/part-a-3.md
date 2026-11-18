<!-- template -->
# Refund request acknowledgment
id: tpl-refund-request-ack
category: refunds
channel: any
style: standard
tags: refund request, money back, want refund, return payment, refund received, ገንዘብ ተመላሽ, ገንዘቤ ይመለስልኝ
related: ref-how-to-request-refund, ref-refund-status, tpl-refund-request-ack-formal, tpl-refund-status-update

## Message (EN)
Hello {{customer_name}},

Thank you for your message. I have recorded your refund request for {{product_name}} under case {{ticket_id}}.

Refund requests are reviewed case by case by our authorized team, so I'm not able to confirm the outcome at this stage. To help the review, please send me (if you haven't already):
1. The reason for your refund request, in a few sentences
2. The transaction reference and the payment method you used
3. Any screenshots, messages or other information that supports your request

We may also contact the seller to hear their side. I will update you by {{follow_up_time}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስለ መልዕክትዎ እናመሰግናለን። ለ{{product_name}} ያቀረቡትን የገንዘብ ተመላሽ ጥያቄ በጉዳይ ቁጥር {{ticket_id}} መዝግቤዋለሁ።

የገንዘብ ተመላሽ ጥያቄዎች በእያንዳንዱ ጉዳይ በተናጠል በሥልጣን ባለው ቡድናችን ይገመገማሉ፤ ስለዚህ በዚህ ደረጃ ውጤቱን ማረጋገጥ አልችልም። ግምገማውን ለማገዝ፣ እስካሁን ካልላኩ እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ገንዘቡ እንዲመለስልዎ የጠየቁበትን ምክንያት በጥቂት ዓረፍተ ነገሮች
2. የግብይት መለያ ቁጥሩን እና የተጠቀሙበትን የክፍያ ዘዴ
3. ጥያቄዎን የሚደግፍ ማንኛውም ስክሪንሾት፣ መልዕክት ወይም ሌላ መረጃ

የሻጩንም ማብራሪያ ለመስማት ሻጩን ልናነጋግር እንችላለን። እስከ {{follow_up_time}} ድረስ አሳውቅዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** the customer asks for their money back (consultation not delivered, seller no-show, unhappy with the service, double payment, cancelled booking).
- **Refund policy is not yet approved.** Eligibility, deadlines, deductions and who approves are still pending. Record the request, collect evidence and escalate to Senior Support / Supervisor (and Payments & Finance for payment errors).
- **Fill in:** `{{product_name}}` (consultation or product title); add the booking/order ID in the first sentence if useful ("…for {{product_name}} (booking {{consultation_id}})…").
- **Duplicate charges:** use `tpl-duplicate-charge-ack` instead — that is a payment error, not a refund request.
- **Do not:** say "you are eligible", "you will get a full refund", quote a percentage, or give a processing time. Do not tell the customer to dispute the payment with their bank.

<!-- template -->
# Refund request acknowledgment — formal
id: tpl-refund-request-ack-formal
category: refunds
channel: email
style: formal
tags: refund request, formal refund email, money back, refund acknowledgment, ገንዘብ ተመላሽ, ደብዳቤ
related: ref-how-to-request-refund, ref-refund-status, tpl-refund-request-ack

## Subject (EN)
Your refund request has been received — case {{ticket_id}}

## Subject (AM)
የገንዘብ ተመላሽ ጥያቄዎ ደርሶናል — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

Thank you for contacting Byfluence Support. We confirm that we have received your refund request regarding {{product_name}}, and it has been registered under case number {{ticket_id}}.

Your request will be reviewed by our authorized team. As part of this review, we will check the relevant transaction and booking or order records and, where appropriate, contact the seller for their account. We are not able to confirm the outcome until the review is complete.

To help us review your request, please reply with the following if you have not already provided them:
- The reason for your request
- The transaction reference ({{transaction_id}}, if already known) and the payment method used
- Any supporting screenshots, messages or documents

We will contact you with an update by {{follow_up_time}}. Please keep the case number in the subject line of any reply.

Kind regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ውድ {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። {{product_name}}ን በተመለከተ ያቀረቡት የገንዘብ ተመላሽ ጥያቄ እንደደረሰን እና በጉዳይ ቁጥር {{ticket_id}} መመዝገቡን እናረጋግጣለን።

ጥያቄዎ በሥልጣን ባለው ቡድናችን ይገመገማል። በግምገማው ሂደት ተያያዥ የሆኑ የግብይት፣ የቀጠሮ ወይም የትዕዛዝ መዝገቦችን እንመረምራለን፤ አስፈላጊ ሲሆንም የሻጩን ማብራሪያ እንጠይቃለን። ግምገማው እስኪጠናቀቅ ድረስ ውጤቱን ማረጋገጥ አንችልም።

ጥያቄዎን ለመገምገም እንዲረዳን፣ እስካሁን ካልላኩልን እባክዎ የሚከተሉትን በምላሽዎ ይላኩልን፦
- ጥያቄዎን ያቀረቡበትን ምክንያት
- የግብይት መለያ ቁጥሩን (የሚታወቅ ከሆነ {{transaction_id}}) እና የተጠቀሙበትን የክፍያ ዘዴ
- ጥያቄዎን የሚደግፉ ስክሪንሾቶች፣ መልዕክቶች ወይም ሰነዶች

እስከ {{follow_up_time}} ድረስ ወቅታዊ መረጃ ይዘን እናገኝዎታለን። ምላሽ ሲሰጡ እባክዎ የጉዳይ ቁጥሩን በርዕሱ ላይ ያቆዩት።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** refund requests that arrive by email, high-value requests, requests from businesses, or any refund request a supervisor asks you to handle formally.
- **Fill in:** if you do not yet have the transaction reference, delete "({{transaction_id}}, if already known)" so the customer does not see an empty value.
- **Follow the same rules as** `tpl-refund-request-ack`: refund policy is pending approval; escalate to Senior Support / Supervisor; never promise eligibility, amount or timing.

<!-- template -->
# Refund approved
id: tpl-refund-approved
category: refunds
channel: email
style: formal
tags: refund approved, refund accepted, money will be returned, refund decision, ገንዘብ ተመላሽ ተፈቅዷል
related: ref-refund-status, ref-how-to-request-refund, tpl-refund-status-update

## Subject (EN)
Your refund request has been approved — case {{ticket_id}}

## Subject (AM)
የገንዘብ ተመላሽ ጥያቄዎ ተቀባይነት አግኝቷል — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

Thank you for your patience while your request was reviewed.

We are pleased to confirm that your refund request has been approved. The details are below:
- Case number: {{ticket_id}}
- Service or product: {{product_name}}
- Refund amount: {{amount}}
- Refund to: {{payment_method}}
- Original transaction reference: {{transaction_id}}

The refund will now be processed by our payments team and then by your payment provider. Because it passes through both, the amount may not appear in your account immediately. We will let you know once the refund has been processed on our side.

If you have any questions, please reply to this email and quote case {{ticket_id}}.

Kind regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ውድ {{customer_name}}፣

ጥያቄዎ እስኪገመገም ድረስ ስለ ትዕግስትዎ እናመሰግናለን።

የገንዘብ ተመላሽ ጥያቄዎ ተቀባይነት ማግኘቱን ስናሳውቅዎ ደስ ይለናል። ዝርዝሩ ከዚህ በታች ቀርቧል፦
- የጉዳይ ቁጥር፦ {{ticket_id}}
- አገልግሎት ወይም ምርት፦ {{product_name}}
- ተመላሽ የሚደረገው የገንዘብ መጠን፦ {{amount}}
- ተመላሽ የሚደረግበት፦ {{payment_method}}
- የመጀመሪያው የግብይት መለያ ቁጥር፦ {{transaction_id}}

ተመላሹ በመጀመሪያ በክፍያ ቡድናችን፣ ከዚያም በክፍያ አቅራቢዎ በኩል ይፈጸማል። በሁለቱም በኩል ስለሚያልፍ ገንዘቡ ወዲያውኑ በሂሳብዎ ላይ ላይታይ ይችላል። በእኛ በኩል ተመላሹ እንደተፈጸመ እናሳውቅዎታለን።

ማንኛውም ጥያቄ ካለዎት፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን በመጥቀስ ለዚህ ኢሜይል ምላሽ ይስጡ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **Send ONLY after an authorized person has approved the refund in writing** (recorded in the ticket with their name and the approved amount). Level 1 agents cannot approve refunds.
- **Fill in:** `{{amount}}` exactly as approved (in ETB), `{{payment_method}}` as recorded by Payments (where the money is going), `{{transaction_id}}` of the original payment.
- **Timing:** do not add a processing time. Only if Payments & Finance gives approved timing wording may you add one sentence using `{{estimated_resolution_time}}`, e.g. "Based on current processing, you can expect the refund within {{estimated_resolution_time}}."
- **Partial amount?** Use `tpl-refund-partial` instead, so the customer understands why the amount differs.
- **Do not:** describe fees or deductions that are not in the approval, or promise the money will "arrive by" any date.

<!-- template -->
# Refund request not approved
id: tpl-refund-rejected
category: refunds
channel: email
style: formal
tags: refund rejected, refund declined, refund denied, not eligible, refund decision, ገንዘብ ተመላሽ አልተፈቀደም
related: ref-how-to-request-refund, ref-refund-status, tpl-refund-request-ack

## Subject (EN)
Update on your refund request — case {{ticket_id}}

## Subject (AM)
ስለ ገንዘብ ተመላሽ ጥያቄዎ ወቅታዊ መረጃ — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

Thank you for your patience while your refund request for {{product_name}} was reviewed, and for the information you shared with us.

After a careful review by our authorized team, we are sorry to let you know that your refund request has not been approved.

The reason for this decision is: [write one clear, factual sentence, for example: "Our records show that the consultation took place on the scheduled date and both participants joined the session."]

We understand this is not the outcome you were hoping for, and we are sorry for your disappointment. If you have additional information or evidence that was not part of the original review, please reply to this email quoting case {{ticket_id}}, and we will make sure it is passed to the team for consideration.

Thank you for your understanding.

Kind regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ውድ {{customer_name}}፣

ለ{{product_name}} ያቀረቡት የገንዘብ ተመላሽ ጥያቄ እስኪገመገም ድረስ ስለታገሱን እና ስላጋሩን መረጃ እናመሰግናለን።

በሥልጣን ባለው ቡድናችን በጥንቃቄ ከተገመገመ በኋላ፣ የገንዘብ ተመላሽ ጥያቄዎ ተቀባይነት አለማግኘቱን ስናሳውቅዎ እናዝናለን።

የውሳኔው ምክንያት፦ [አንድ ግልጽና ተጨባጭ ዓረፍተ ነገር ይጻፉ፤ ለምሳሌ፦ "በመዝገባችን መሠረት ምክክሩ በተያዘለት ቀን የተካሄደ ሲሆን ሁለቱም ተሳታፊዎች ስብሰባውን ተቀላቅለዋል።"]

ይህ እርስዎ የጠበቁት ውጤት እንዳልሆነ እንረዳለን፤ ስላሳዘነዎትም ይቅርታ እንጠይቃለን። በመጀመሪያው ግምገማ ውስጥ ያልተካተተ ተጨማሪ መረጃ ወይም ማስረጃ ካለዎት፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን በመጥቀስ ለዚህ ኢሜይል ምላሽ ይስጡ፤ መረጃው ለሚመለከተው ቡድን እንዲደርስ እናደርጋለን።

ስለ መረዳትዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **Send ONLY after an authorized person has made and recorded the decision** in the ticket. Level 1 agents cannot reject refunds on their own.
- **Write the reason yourself** in place of the bracketed line, in both languages. Use the reason recorded by the decision-maker, stated as facts from our records — no blame, no opinion, no internal jargon, and never the other party's private information.
- **Appeal path:** a formal appeal process has not been approved yet. The closing paragraph only invites new information; it does not promise a second review or a different outcome. If the customer replies with new evidence, attach it to the ticket and escalate to Senior Support / Supervisor.
- **Do not:** cite a policy rule, deadline or percentage that is not officially approved, or suggest the customer contact their bank to reverse the payment.

<!-- template -->
# Refund status update
id: tpl-refund-status-update
category: refunds
channel: any
style: standard
tags: refund status, where is my refund, refund update, refund progress, refund pending, ተመላሹ የት ደረሰ, የገንዘብ ተመላሽ ሁኔታ
related: ref-refund-status, ref-how-to-request-refund, tpl-refund-request-ack, tpl-refund-approved

## Message (EN)
Hello {{customer_name}},

Thank you for checking in. Here is an update on your refund request (case {{ticket_id}}).

Current status: [choose one — Under review / Approved and being processed / Processed by Byfluence]

[Add one sentence on what is happening now, for example: "Our payments team is still reviewing the transaction with the payment provider."]

We will contact you again by {{follow_up_time}}, or sooner if there is news. Thank you for your patience.

{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስለጠየቁን እናመሰግናለን። ስለ ገንዘብ ተመላሽ ጥያቄዎ (የጉዳይ ቁጥር {{ticket_id}}) ወቅታዊ መረጃ ይህ ነው፦

የአሁኑ ሁኔታ፦ [ከሚከተሉት አንዱን ይምረጡ — በግምገማ ላይ / ተፈቅዶ በሂደት ላይ / በByfluence በኩል ተፈጽሟል]

[አሁን እየተደረገ ያለውን በአንድ ዓረፍተ ነገር ይጻፉ፤ ለምሳሌ፦ "የክፍያ ቡድናችን ግብይቱን ከክፍያ አቅራቢው ጋር አሁንም እያጣራ ነው።"]

እስከ {{follow_up_time}} ድረስ፣ ወይም ከዚያ ቀደም አዲስ መረጃ ካለ፣ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** the customer asks where their refund is, or a scheduled follow-up is due.
- **Check the ticket and the payment record first,** and use only the status that is actually recorded. Replace both bracketed lines; delete the options you did not choose.
- **"Processed by Byfluence" but customer has not received it:** explain that the provider also needs to complete its part, ask them to check with their provider, and ask for a screenshot of their recent transactions if they still don't see it after that. Escalate to Payments & Finance with the refund reference.
- **Do not:** say "it will arrive tomorrow" or give any timing unless Payments gives approved wording (`{{estimated_resolution_time}}`). Do not say "approved" if it is still under review.

<!-- template -->
# Partial refund decision
id: tpl-refund-partial
category: refunds
channel: email
style: formal
tags: partial refund, part refund, refund decision, reduced refund, refund amount, ከፊል ገንዘብ ተመላሽ
related: ref-refund-status, ref-how-to-request-refund, tpl-refund-approved, tpl-refund-rejected

## Subject (EN)
Decision on your refund request — case {{ticket_id}}

## Subject (AM)
በገንዘብ ተመላሽ ጥያቄዎ ላይ የተሰጠ ውሳኔ — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

Thank you for your patience while your refund request for {{product_name}} was reviewed.

After a careful review, our authorized team has decided to approve a partial refund of {{amount}}.

The reason for this decision is: [write one or two clear, factual sentences explaining why part of the payment is being refunded, for example: "Our records show that the session started as scheduled but ended early because of a connection problem on the consultant's side."]

Refund details:
- Case number: {{ticket_id}}
- Refund amount: {{amount}}
- Refund to: {{payment_method}}
- Original transaction reference: {{transaction_id}}

The refund will be processed by our payments team and then by your payment provider, so the amount may not appear in your account immediately. We will let you know once it has been processed on our side.

If you have additional information that was not part of the review, please reply to this email quoting case {{ticket_id}}, and we will make sure it is passed to the team.

Kind regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ውድ {{customer_name}}፣

ለ{{product_name}} ያቀረቡት የገንዘብ ተመላሽ ጥያቄ እስኪገመገም ድረስ ስለ ትዕግስትዎ እናመሰግናለን።

በጥንቃቄ ከተገመገመ በኋላ፣ በሥልጣን ያለው ቡድናችን የ{{amount}} ከፊል ገንዘብ ተመላሽ እንዲደረግልዎ ወስኗል።

የውሳኔው ምክንያት፦ [የክፍያው የተወሰነ ክፍል ብቻ ለምን እንደሚመለስ በአንድ ወይም በሁለት ግልጽና ተጨባጭ ዓረፍተ ነገሮች ይጻፉ፤ ለምሳሌ፦ "በመዝገባችን መሠረት ምክክሩ በተያዘለት ሰዓት ቢጀመርም በአማካሪው በኩል በተፈጠረ የግንኙነት ችግር ምክንያት ቀድሞ ተቋርጧል።"]

የተመላሹ ዝርዝር፦
- የጉዳይ ቁጥር፦ {{ticket_id}}
- ተመላሽ የሚደረገው የገንዘብ መጠን፦ {{amount}}
- ተመላሽ የሚደረግበት፦ {{payment_method}}
- የመጀመሪያው የግብይት መለያ ቁጥር፦ {{transaction_id}}

ተመላሹ በመጀመሪያ በክፍያ ቡድናችን፣ ከዚያም በክፍያ አቅራቢዎ በኩል ስለሚፈጸም ገንዘቡ ወዲያውኑ በሂሳብዎ ላይ ላይታይ ይችላል። በእኛ በኩል እንደተፈጸመ እናሳውቅዎታለን።

በግምገማው ውስጥ ያልተካተተ ተጨማሪ መረጃ ካለዎት፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን በመጥቀስ ለዚህ ኢሜይል ምላሽ ይስጡ፤ መረጃው ለሚመለከተው ቡድን እንዲደርስ እናደርጋለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **Send ONLY after an authorized person has approved the partial amount** and recorded the amount and reason in the ticket.
- **Fill in:** `{{amount}}` = the refund amount (not the original payment). If you need to mention the original amount, write it out in the reason sentence.
- **Reason:** state the facts behind the decision. Do not mention commission, platform fees or deduction percentages — these are not confirmed policy and must not be quoted unless management approves the wording.
- **Appeal path:** not yet approved; the closing paragraph only invites new information. Escalate any reply with new evidence to Senior Support / Supervisor.
- **Do not:** add a processing time unless Payments gives approved wording for `{{estimated_resolution_time}}`.

<!-- template -->
# Password reset instructions
id: tpl-password-reset-guide
category: accounts
channel: any
style: standard
tags: password reset, forgot password, cannot log in, change password, sign in problem, የይለፍ ቃል ረሳሁ, መግባት አልቻልኩም
related: acc-forgot-password, acc-locked-account, reg-otp-not-received, tpl-otp-not-received

## Message (EN)
Hello {{customer_name}},

You can reset your password yourself in a few simple steps:
1. Go to the Byfluence sign-in page at byfluence.com.
2. Select "Forgot password?".
3. Enter the email address or phone number registered on your account.
4. Follow the instructions in the message we send you, and choose a new password.

**Helpful tips:**
- Choose a strong password that you don't use for any other website or app.
- If the reset message doesn't arrive, check your spam/junk folder and make sure you entered the same email or phone number you registered with.
- If you requested the reset more than once, use the most recent message.

Byfluence will never ask you to send us your password or a reset code. If these steps don't work, reply here with a screenshot of what you see, and I'll help you further.

Your case number is {{ticket_id}}.

## Message (AM)
ሰላም {{customer_name}}፣

የይለፍ ቃልዎን በጥቂት ቀላል ደረጃዎች ራስዎ መቀየር ይችላሉ፦
1. ወደ Byfluence የመግቢያ ገጽ (byfluence.com) ይሂዱ።
2. "Forgot password?" (የይለፍ ቃል ረሱ?) የሚለውን ይምረጡ።
3. በአካውንትዎ ላይ የተመዘገበውን ኢሜይል አድራሻ ወይም ስልክ ቁጥር ያስገቡ።
4. የምንልክልዎትን መልዕክት መመሪያ ይከተሉ፤ አዲስ የይለፍ ቃልም ይምረጡ።

**ጠቃሚ ምክሮች፦**
- ለሌላ ድረ-ገጽ ወይም መተግበሪያ የማይጠቀሙበትን ጠንካራ የይለፍ ቃል ይምረጡ።
- የመቀየሪያ መልዕክቱ ካልደረሰዎት፣ የኢሜይልዎን spam/junk ማህደር ይመልከቱ፤ የተመዘገቡበትን ተመሳሳይ ኢሜይል ወይም ስልክ ቁጥር ማስገባትዎንም ያረጋግጡ።
- ከአንድ ጊዜ በላይ ጠይቀው ከሆነ፣ የመጨረሻውን (አዲሱን) መልዕክት ይጠቀሙ።

Byfluence የይለፍ ቃልዎን ወይም የመቀየሪያ ኮድዎን እንዲልኩልን በፍጹም አይጠይቅዎትም። እነዚህ ደረጃዎች ካልሠሩ፣ የሚያዩትን ገጽ ስክሪንሾት እዚሁ ይላኩልኝ፤ ተጨማሪ እገዛ አደርግልዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

## Usage Notes
- **Check the current flow first:** the exact sign-in method (email, phone OTP, or both) and button wording depend on the live authentication system. Read `acc-forgot-password` and adjust step names if the screen differs.
- **Agents cannot see or set passwords.** Never offer to "reset it for you" or send a password by message.
- **If the customer no longer has access** to the registered email or phone, do not change contact details on request — verify ownership with `tpl-verify-identity` and escalate per `acc-forgot-password`.
- **Suspicious signs** (the customer says they didn't request a reset, or details were changed): switch to `tpl-account-compromise-urgent`.
- **Do not:** ask for the old password, the reset code or the OTP.

<!-- template -->
# Verification code not received
id: tpl-otp-not-received
category: accounts
channel: any
style: standard
tags: otp not received, verification code, sms code, code not arriving, email code, ኮድ አልደረሰኝም, የማረጋገጫ ኮድ
related: reg-otp-not-received, acc-forgot-password, tpl-never-share-otp-warning

## Message (EN)
Hello {{customer_name}},

I'm sorry you haven't received your verification code. Please try these steps:
1. Check that the phone number or email address you entered is correct and is the one registered on your account.
2. If the code is sent by email, check your spam/junk folder.
3. If it is sent by SMS, check that your phone has network signal and that your SMS inbox is not full.
4. Wait a little before asking for a new code — requesting many codes quickly can cause delays. Always use the most recent code you receive.
5. Make sure your internet connection is stable, then close and reopen the page or app and try again.

If it still doesn't arrive, reply with the phone number or email you are using and the approximate time you tried. You do not need to send any code.

Important: never share a verification code with anyone — not even Byfluence Support. We will never ask for it.

Your case number is {{ticket_id}}.

## Message (AM)
ሰላም {{customer_name}}፣

የማረጋገጫ ኮድዎ ስላልደረሰዎት ይቅርታ እንጠይቃለን። እባክዎ የሚከተሉትን ደረጃዎች ይሞክሩ፦
1. ያስገቡት ስልክ ቁጥር ወይም ኢሜይል አድራሻ ትክክል መሆኑን እና በአካውንትዎ ላይ የተመዘገበው መሆኑን ያረጋግጡ።
2. ኮዱ የሚላከው በኢሜይል ከሆነ የspam/junk ማህደርዎን ይመልከቱ።
3. ኮዱ የሚላከው በኤስኤምኤስ ከሆነ፣ ስልክዎ ኔትወርክ እንዳለው እና የመልዕክት ሳጥንዎ እንዳልሞላ ያረጋግጡ።
4. አዲስ ኮድ ከመጠየቅዎ በፊት ትንሽ ይጠብቁ — ብዙ ኮዶችን በተከታታይ መጠየቅ መዘግየት ሊያስከትል ይችላል። ሁልጊዜም የደረሰዎትን የመጨረሻውን ኮድ ይጠቀሙ።
5. የኢንተርኔት ግንኙነትዎ የተረጋጋ መሆኑን ያረጋግጡ፤ ከዚያም ገጹን ወይም መተግበሪያውን ዘግተው እንደገና በመክፈት ይሞክሩ።

አሁንም ካልደረሰዎት፣ የሚጠቀሙበትን ስልክ ቁጥር ወይም ኢሜይል እና የሞከሩበትን ግምታዊ ሰዓት ይላኩልኝ። ምንም ኮድ መላክ አያስፈልግዎትም።

አስፈላጊ፦ የማረጋገጫ ኮድ ለማንም፣ ለByfluence ድጋፍም ቢሆን፣ በፍጹም አያጋሩ። እኛ በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

## Usage Notes
- **Check Feature Status:** whether Byfluence uses SMS OTP, email codes, or both is not yet confirmed. Remove step 2 or step 3 if that channel is not used.
- **Number format:** many failures are caused by a wrong country code or a missing/extra leading zero. Compare the number the customer gives with the account record (without reading the record out to them).
- **Several customers at once** reporting missing codes may mean a provider or system incident — alert your supervisor and Technical, and check Announcements.
- **If the customer sends you a code anyway,** do not use it; tell them kindly to never share codes, and note it in the ticket.
- **Do not:** ask for the code, promise when it will arrive, or change the registered phone/email without ownership verification.

<!-- template -->
# Account locked
id: tpl-account-locked
category: accounts
channel: any
style: standard
tags: account locked, blocked account, cannot sign in, account restricted, too many attempts, አካውንቴ ተቆልፏል, መግባት አልቻልኩም
related: acc-locked-account, acc-forgot-password, tpl-verify-identity, tpl-account-compromise-urgent

## Message (EN)
Hello {{customer_name}},

I'm sorry you can't get into your account. An account can be locked or restricted for different reasons — for example after several unsuccessful sign-in attempts, or as a security precaution.

I will check this for you. Please send me:
1. The email address or phone number registered on the account
2. The exact message you see when you try to sign in (a screenshot is best)
3. When this started

For now, please avoid repeated sign-in attempts. Our team will review the account and let you know the next steps. I'm not able to say when access will be restored until the review is complete.

Please never share your password or verification codes with anyone, including us.

Your case number is {{ticket_id}}.

## Message (AM)
ሰላም {{customer_name}}፣

ወደ አካውንትዎ መግባት ባለመቻልዎ ይቅርታ እንጠይቃለን። አንድ አካውንት በተለያዩ ምክንያቶች ሊቆለፍ ወይም ሊገደብ ይችላል — ለምሳሌ ብዙ ያልተሳኩ የመግቢያ ሙከራዎች ከተደረጉ በኋላ፣ ወይም ለደህንነት ጥንቃቄ ሲባል።

ይህንን አጣራልዎታለሁ። እባክዎ የሚከተሉትን ይላኩልኝ፦
1. በአካውንቱ ላይ የተመዘገበው ኢሜይል አድራሻ ወይም ስልክ ቁጥር
2. ለመግባት ሲሞክሩ የሚታየዎት ትክክለኛ መልዕክት (ስክሪንሾት ቢሆን ይመረጣል)
3. ችግሩ መቼ እንደጀመረ

ለጊዜው እባክዎ በተደጋጋሚ ለመግባት ከመሞከር ይቆጠቡ። ቡድናችን አካውንቱን ገምግሞ ቀጣዩን እርምጃ ያሳውቅዎታል። ግምገማው እስኪጠናቀቅ ድረስ አካውንትዎ መቼ እንደሚከፈት መናገር አልችልም።

እባክዎ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድዎን ለማንም፣ ለእኛም ቢሆን፣ በፍጹም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

## Usage Notes
- **When to use:** the customer sees a "locked", "blocked", "suspended" or "restricted" message, or says they can no longer sign in although the password is correct.
- **Find out why before promising anything.** Check the account status in authorized tools. Locked by failed attempts → follow `acc-locked-account`. Locked by Trust & Safety, or a seller account Suspended/Banned → do not discuss the reason; escalate to Trust & Safety or Seller Operations as recorded.
- **Sellers:** a seller can be Verified but Suspended. Do not confuse verification status with operational status in your reply.
- **Verify ownership** (`tpl-verify-identity`) before sharing any account information.
- **Do not:** unlock accounts you are not authorized to unlock, explain internal security rules (number of attempts, lock duration), or give a time for restoring access.

<!-- template -->
# Urgent: account may be compromised
id: tpl-account-compromise-urgent
category: accounts
channel: any
style: standard
tags: hacked account, account compromised, someone accessed my account, unknown login, fraud, scam, አካውንቴ ተጠልፏል, ማጭበርበር
related: tns-account-compromise, tpl-verify-identity, tpl-never-share-otp-warning, tpl-password-reset-guide

## Message (EN)
Hello {{customer_name}},

Thank you for telling us straight away — we are treating this as urgent. I have flagged your account to our security team under case {{ticket_id}}.

**Please do these things now:**
1. If you can still sign in, change your Byfluence password immediately, and choose one you have never used anywhere else.
2. If you think the email account linked to Byfluence may also be affected, change that password too.
3. Do not share any verification code, PIN or password with anyone — including anyone who says they are from Byfluence.
4. Do not send money to anyone who contacted you about this account.

**Then please reply with:**
- The email address or phone number registered on the account
- When you first noticed something wrong
- What you noticed (for example: a sign-in you don't recognise, changed details, bookings or payments you didn't make)
- The transaction references of any payments you did not make

We will contact you with the next steps as soon as possible.

{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ወዲያውኑ ስላሳወቁን እናመሰግናለን — ጉዳዩን እንደ አስቸኳይ እየተመለከትነው ነው። አካውንትዎን በጉዳይ ቁጥር {{ticket_id}} ለደህንነት ቡድናችን አሳውቄያለሁ።

**እባክዎ እነዚህን አሁኑኑ ያድርጉ፦**
1. አሁንም መግባት ከቻሉ፣ የByfluence የይለፍ ቃልዎን ወዲያውኑ ይቀይሩ፤ ከዚህ በፊት የትም ያልተጠቀሙበትን አዲስ የይለፍ ቃል ይምረጡ።
2. ከByfluence ጋር የተገናኘው የኢሜይል አካውንትዎም ሊጎዳ ይችላል ብለው ካሰቡ፣ የእሱንም የይለፍ ቃል ይቀይሩ።
3. ማንኛውንም የማረጋገጫ ኮድ፣ ፒን ወይም የይለፍ ቃል ለማንም አያጋሩ — ከByfluence ነኝ ለሚልም ሰው ቢሆን።
4. ስለዚህ አካውንት ላገኘዎት ለማንኛውም ሰው ገንዘብ አይላኩ።

**ከዚያም እባክዎ የሚከተሉትን ይላኩልን፦**
- በአካውንቱ ላይ የተመዘገበውን ኢሜይል አድራሻ ወይም ስልክ ቁጥር
- ችግሩን መጀመሪያ መቼ እንዳስተዋሉ
- ምን እንዳስተዋሉ (ለምሳሌ፦ የማያውቁት መግቢያ፣ የተቀየረ መረጃ፣ እርስዎ ያላደረጓቸው ቀጠሮዎች ወይም ክፍያዎች)
- እርስዎ ያልፈጸሟቸው ክፍያዎች ካሉ የግብይት መለያ ቁጥሮቻቸውን

ቀጣዩን እርምጃ ይዘን በተቻለ ፍጥነት እናገኝዎታለን።

{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **Priority:** create the ticket as **Critical** and escalate to Trust & Safety immediately — before you finish the conversation.
- **Sellers:** if the account is a seller account, tell Trust & Safety and Payments & Finance right away so that withdrawal requests and payout details can be reviewed. Do not promise to block withdrawals yourself.
- **If the customer cannot sign in** because the email/phone was changed by someone else, do not change contact details on their word alone — Trust & Safety decides after ownership checks.
- **Do not:** ask for the password, OTP or PIN "to check", promise to recover money or reverse transactions, or reveal what you can see in the account (devices, locations, other users) until ownership is verified.

<!-- template -->
# Account deletion request received
id: tpl-account-deletion-ack
category: accounts
channel: email
style: formal
tags: delete account, close account, remove my account, account deletion, data removal, አካውንቴን ሰርዙልኝ, አካውንት መዝጋት
related: acc-account-deletion-request, tpl-verify-identity

## Subject (EN)
Your account deletion request — case {{ticket_id}}

## Subject (AM)
አካውንትዎን ለመሰረዝ ያቀረቡት ጥያቄ — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

We have received your request to delete your Byfluence account, and it has been registered under case number {{ticket_id}}.

Before the request can be completed, we need to:
1. Confirm that the request comes from the account owner. We may contact you with a few verification questions.
2. Check for any open bookings, orders, payments or refunds — and, for seller accounts, any earnings or withdrawals — linked to the account, as these may need to be completed or resolved first.

If you have upcoming sessions or open orders, please let us know how you would like them handled. You may also wish to save any receipts or records you need before the account is deleted.

We will contact you with the next steps. If you change your mind, simply reply to this email.

Kind regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ውድ {{customer_name}}፣

የByfluence አካውንትዎ እንዲሰረዝ ያቀረቡት ጥያቄ ደርሶናል፤ በጉዳይ ቁጥር {{ticket_id}} ተመዝግቧል።

ጥያቄውን ከማጠናቀቃችን በፊት የሚከተሉትን ማድረግ ይኖርብናል፦
1. ጥያቄው ከአካውንቱ ባለቤት የመጣ መሆኑን ማረጋገጥ። ለዚህም ጥቂት የማረጋገጫ ጥያቄዎችን ይዘን ልናገኝዎ እንችላለን።
2. ከአካውንቱ ጋር የተያያዙ ክፍት ቀጠሮዎች፣ ትዕዛዞች፣ ክፍያዎች ወይም የገንዘብ ተመላሾች — የሻጭ አካውንት ከሆነም ገቢዎች ወይም የገንዘብ ማውጫ ጥያቄዎች — መኖራቸውን ማጣራት፤ እነዚህ አስቀድመው መጠናቀቅ ወይም መፍትሔ ማግኘት ሊኖርባቸው ይችላል።

የሚቀሩ ቀጠሮዎች ወይም ክፍት ትዕዛዞች ካሉዎት፣ እንዴት እንዲስተናገዱ እንደሚፈልጉ እባክዎ ያሳውቁን። አካውንቱ ከመሰረዙ በፊት የሚያስፈልጉዎትን ደረሰኞች ወይም መዝገቦች ማስቀመጥም ይችላሉ።

ቀጣዩን እርምጃ ይዘን እናገኝዎታለን። ሃሳብዎን ከቀየሩ ለዚህ ኢሜይል ምላሽ መስጠት ብቻ በቂ ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** a buyer or seller asks for their account to be deleted or closed (any channel — send this by email so there is a written record).
- **Data and retention rules are pending approval:** what is deleted, what must be kept (for example transaction records), and how long it takes are not yet decided. Do not explain these to the customer; escalate to Senior Support / Supervisor per `acc-account-deletion-request`.
- **Sellers with pending or available balances,** open bookings or disputes: flag to Seller Operations and Payments & Finance before anything else happens.
- **Verify ownership** with `tpl-verify-identity`, especially if the request comes from an email or phone number not on the account.
- **Do not:** confirm that the account "has been deleted", promise a completion date, or delete anything yourself unless your role is authorized to do so.

<!-- template -->
# Safety warning: never share codes/PIN
id: tpl-never-share-otp-warning
category: accounts
channel: sms
style: short
tags: security warning, never share otp, pin safety, scam warning, fraud prevention, sms, ኮድ አያጋሩ, ማጭበርበር
related: tns-account-compromise, tpl-never-share-otp-warning-telegram, tpl-account-compromise-urgent

## Message (EN)
Byfluence: Never share your password, PIN or verification code with anyone, including Byfluence staff. We will never ask for it.

## Message (AM)
Byfluence፦ የይለፍ ቃልዎን፣ ፒንዎን ወይም የማረጋገጫ ኮድዎን ለማንም፣ ለByfluence ሠራተኞችም ቢሆን፣ አያጋሩ። እኛ በፍጹም አንጠይቅዎትም።

## Usage Notes
- **When to use:** as a stand-alone SMS reminder after a call, after a reported scam attempt, or as part of a security campaign approved by your supervisor.
- **Length:** the English text fits a single SMS. Amharic characters use more SMS space, so the Amharic version may be split into more than one message by the network — keep the wording as is.
- **SMS sending:** only send from the official Byfluence SMS channel if one exists (check Feature Status); never from a personal phone.
- **Do not:** add links, phone numbers or handles to this SMS — scam messages often contain links, and customers should learn that ours do not.

<!-- template -->
# Safety warning: never share codes/PIN — Telegram
id: tpl-never-share-otp-warning-telegram
category: accounts
channel: telegram
style: standard
tags: security warning, scam warning, fake support, impersonation, telegram scam, otp, pin, ማጭበርበር, ኮድ አያጋሩ
related: tns-account-compromise, tpl-never-share-otp-warning, tpl-account-compromise-urgent

## Message (EN)
Hello {{customer_name}}, a quick but important safety reminder from Byfluence Support:

- We will **never** ask for your password, PIN, mobile-money PIN or verification (OTP) code — not on Telegram, by phone, SMS or email.
- We will never ask you to send money to a personal account to "unlock", "verify" or "speed up" anything.
- Scammers sometimes create Telegram accounts that look like Byfluence Support. Only trust messages that come through {{support_channel}}.

If someone has asked you for a code or for money, please don't reply to them — tell us here, and if you already shared anything, let us know straight away so we can help protect your account.

## Message (AM)
ሰላም {{customer_name}}፣ ከByfluence ድጋፍ አጭር ግን አስፈላጊ የደህንነት ማሳሰቢያ፦

- የይለፍ ቃልዎን፣ ፒንዎን፣ የሞባይል ገንዘብ ፒንዎን ወይም የማረጋገጫ (OTP) ኮድዎን በቴሌግራም፣ በስልክ፣ በኤስኤምኤስም ሆነ በኢሜይል **በፍጹም** አንጠይቅዎትም።
- አንድን ነገር "ለመክፈት"፣ "ለማረጋገጥ" ወይም "ለማፋጠን" በሚል ወደ ግል አካውንት ገንዘብ እንዲልኩ በፍጹም አንጠይቅዎትም።
- አጭበርባሪዎች አንዳንድ ጊዜ Byfluence ድጋፍን የሚመስሉ የቴሌግራም አካውንቶችን ይከፍታሉ። እባክዎ በ{{support_channel}} በኩል የሚመጡ መልዕክቶችን ብቻ ይመኑ።

አንድ ሰው ኮድ ወይም ገንዘብ ከጠየቀዎት፣ እባክዎ ለእሱ ምላሽ አይስጡ — እዚሁ ያሳውቁን። ቀድመው ያጋሩት ነገር ካለም አካውንትዎን ለመጠበቅ እንድንረዳዎ ወዲያውኑ ይንገሩን።

## Usage Notes
- **When to use:** after a customer mentions a suspicious message or call, when closing an account-security case, or when a customer offers to send you a code.
- **Fill in:** `{{support_channel}}` with the official, confirmed Byfluence support handle/contact only.
- **If the customer already shared a code, PIN or password,** switch to `tpl-account-compromise-urgent` and escalate to Trust & Safety as Critical.
- **Report impersonation:** record any fake account names or numbers the customer shares in the ticket and forward them to Trust & Safety.
- **Do not:** click links or contact the scammer yourself, or ask the customer to forward screenshots that show their own codes or PINs.
