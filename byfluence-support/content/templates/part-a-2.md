<!-- template -->
# Acknowledging a complaint
id: tpl-acknowledge-complaint
category: acknowledgments
channel: any
style: standard
tags: complaint, unhappy customer, dissatisfied, report a problem, acknowledgment, ቅሬታ, አቤቱታ
related: tpl-acknowledge-complaint-formal, tpl-angry-customer-deescalation, tpl-request-screenshot

## Message (EN)
Hello {{customer_name}},

Thank you for telling us about this, and I'm sorry for the experience you've had. I understand this has been frustrating, and I want to make sure it is looked into properly.

I have recorded your complaint under case {{ticket_id}}. Here is what happens next:
1. I will review the details you shared and check the related records.
2. If needed, I will contact the relevant team or the seller to get their side.
3. I will update you by {{follow_up_time}}, or sooner if I have news.

If you have any screenshots, receipts or other details that could help, please send them here.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስለዚህ ጉዳይ ስላሳወቁን እናመሰግናለን፤ ላጋጠመዎት ሁኔታም ይቅርታ እንጠይቃለን። ይህ ምን ያህል እንዳስቸገረዎት ይገባኛል፤ ጉዳዩ በአግባቡ መጣራቱን አረጋግጣለሁ።

ቅሬታዎን በጉዳይ ቁጥር {{ticket_id}} መዝግቤዋለሁ። ቀጣዮቹ ደረጃዎች እነዚህ ናቸው፦
1. የላኩልኝን ዝርዝር መረጃ እና ተያያዥ መዝገቦችን እመረምራለሁ።
2. አስፈላጊ ከሆነ የሚመለከተውን ክፍል ወይም ሻጩን አነጋግሬ የእነሱን ማብራሪያ እጠይቃለሁ።
3. እስከ {{follow_up_time}} ድረስ፣ ወይም ከዚያ ቀደም አዲስ መረጃ ካገኘሁ፣ አሳውቅዎታለሁ።

ሊረዳ የሚችል ስክሪንሾት፣ ደረሰኝ ወይም ሌላ መረጃ ካለዎት እባክዎ እዚሁ ይላኩልኝ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** any complaint about a seller, a consultation, an order, a payment experience or our service, once you understand the basic issue.
- **Fill in:** `{{follow_up_time}}` with a realistic time you or the next shift will actually check the case (e.g. "tomorrow afternoon" / "ነገ ከሰዓት በኋላ") — and record it in the ticket. If you cannot commit to a time, replace step 3 with "I will update you as soon as I have news." / "አዲስ መረጃ እንዳገኘሁ አሳውቅዎታለሁ።"
- **Apologise for the experience, not for fault.** "I'm sorry for the experience you've had" is fine; do not say "the seller was wrong" or "this was our mistake" before the facts are checked.
- **Do not:** promise a refund, compensation, seller suspension or any specific outcome. Byfluence is a marketplace facilitator; decisions are made by authorized staff.

<!-- template -->
# Acknowledging a complaint — formal
id: tpl-acknowledge-complaint-formal
category: acknowledgments
channel: email
style: formal
tags: formal complaint, written complaint, complaint email, escalated complaint, ቅሬታ, አቤቱታ, ደብዳቤ
related: tpl-acknowledge-complaint, tpl-apology-service-failure

## Subject (EN)
We have received your complaint — case {{ticket_id}}

## Subject (AM)
ቅሬታዎ ደርሶናል — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

Thank you for taking the time to write to us. We confirm that we have received your complaint, and it has been registered under case number {{ticket_id}}.

We are sorry that your experience with Byfluence did not meet your expectations. We take every complaint seriously, and your case will be reviewed carefully. As part of this review, we may check the relevant transaction and booking records and, where appropriate, ask the seller for their account of what happened.

We will contact you with an update by {{follow_up_time}}. If you have any further documents, screenshots or information you would like us to consider, please reply to this email and keep the case number in the subject line.

Thank you for your patience while we look into this matter.

Kind regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ውድ {{customer_name}}፣

ጊዜዎን ወስደው ስለጻፉልን እናመሰግናለን። ቅሬታዎ እንደደረሰን እና በጉዳይ ቁጥር {{ticket_id}} መመዝገቡን እናረጋግጣለን።

በByfluence ያገኙት አገልግሎት የጠበቁትን ባለማሟላቱ ይቅርታ እንጠይቃለን። እያንዳንዱን ቅሬታ በቁም ነገር እንመለከታለን፤ ጉዳይዎም በጥንቃቄ ይገመገማል። በግምገማው ሂደት ተያያዥ የሆኑ የግብይትና የቀጠሮ መዝገቦችን ልንመረምር፣ አስፈላጊ ሲሆንም ስለተፈጠረው ሁኔታ የሻጩን ማብራሪያ ልንጠይቅ እንችላለን።

እስከ {{follow_up_time}} ድረስ ወቅታዊ መረጃ ይዘን እናገኝዎታለን። ልንመለከተው የሚገባ ተጨማሪ ሰነድ፣ ስክሪንሾት ወይም መረጃ ካለዎት፣ እባክዎ የጉዳይ ቁጥሩን በርዕሱ ላይ በማቆየት ለዚህ ኢሜይል ምላሽ ይስጡ።

ጉዳዩን እስክናጣራ ድረስ ስለ ትዕግስትዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** formal written complaints, complaints from businesses or sellers, complaints that mention legal action, the media or regulators, and any complaint a supervisor asks you to answer formally.
- **Legal or media threats:** send this acknowledgment only, add an internal note, and escalate immediately to Senior Support / Supervisor (and Management if the supervisor decides). Do not argue the facts in writing.
- **Fill in:** `{{follow_up_time}}` with a date agreed with your supervisor. If none is agreed, replace that sentence with "We will contact you with an update as soon as our review allows." / "ግምገማችን እንደፈቀደ ወዲያውኑ ወቅታዊ መረጃ ይዘን እናገኝዎታለን።"
- **Do not:** admit liability, offer compensation or describe internal processes beyond what is written here.

<!-- template -->
# Apology for a delayed response
id: tpl-delayed-response-apology
category: acknowledgments
channel: any
style: standard
tags: delay, late reply, slow response, sorry for waiting, waited long, ዘግይቶ መመለስ, ይቅርታ, መዘግየት
related: tpl-greeting-returning-customer, tpl-thank-patience

## Message (EN)
Hello {{customer_name}},

I'm sorry for the delay in getting back to you, and thank you for waiting. I know it's frustrating to wait for an answer, especially when it concerns your money or your booking.

I'm now looking at your case {{ticket_id}} personally. [Give the update, answer, or the one question you need answered.]

I will stay with your case and update you by {{follow_up_time}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ምላሽ ለመስጠት በመዘግየታችን ይቅርታ እንጠይቃለን፤ ስለጠበቁንም እናመሰግናለን። በተለይ ጉዳዩ ገንዘብዎን ወይም ቀጠሮዎን የሚመለከት ሲሆን መልስ መጠበቅ ምን ያህል እንደሚያስጨንቅ ይገባኛል።

አሁን የጉዳይ ቁጥር {{ticket_id}}ን እኔ ራሴ እየተከታተልኩት ነው። [ወቅታዊ መረጃውን፣ መልሱን ወይም የሚያስፈልግዎን አንድ ጥያቄ እዚህ ይጻፉ።]

ጉዳይዎን መከታተሌን እቀጥላለሁ፤ እስከ {{follow_up_time}} ድረስም አሳውቅዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** the customer waited longer than they should have for a reply, or a promised follow-up was missed.
- **Always add real content** in the bracketed line. An apology with no update makes the customer feel ignored twice.
- **Keep the apology simple.** Do not blame colleagues, "the system" or the volume of messages, and do not invent a reason for the delay.
- **Fill in:** `{{follow_up_time}}` only with a time you will actually keep; record it in the ticket. Delete that line if you are resolving the case in this message.
- **Do not:** promise faster service in the future or offer any goodwill gesture unless a supervisor has approved it.

<!-- template -->
# Apology for a service failure
id: tpl-apology-service-failure
category: acknowledgments
channel: email
style: formal
tags: service failure, outage, system problem, platform error, incident apology, technical issue, ብልሽት, የአገልግሎት መቋረጥ, ይቅርታ
related: tpl-acknowledge-complaint-formal, tpl-payment-pending-explain

## Subject (EN)
Our apologies for the problem you experienced — case {{ticket_id}}

## Subject (AM)
ላጋጠመዎት ችግር ይቅርታ እንጠይቃለን — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

We sincerely apologise for the problem you experienced while using Byfluence.

[Describe in one or two plain sentences what went wrong and how it affected the customer, for example: "A technical problem on our platform delayed the confirmation of some consultation bookings, including yours."]

We understand that this caused you inconvenience, and we are sorry. Our team has been informed and is working on the issue. Here is where your case stands:
- [What has been done for this customer so far, e.g. "Your payment has been recorded and your booking is now confirmed."]
- [What is still pending, if anything, and who is handling it.]

We will keep you informed by {{follow_up_time}}. If anything is still not working for you, please reply to this email quoting case {{ticket_id}}.

Thank you for your patience and for your trust in Byfluence.

Kind regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ውድ {{customer_name}}፣

Byfluenceን በሚጠቀሙበት ወቅት ላጋጠመዎት ችግር ከልብ ይቅርታ እንጠይቃለን።

[የተፈጠረውን ችግርና ደንበኛውን እንዴት እንደጎዳ በአንድ ወይም በሁለት ቀላል ዓረፍተ ነገሮች ይግለጹ፤ ለምሳሌ፦ "በፕላትፎርማችን ላይ በተፈጠረ የቴክኒክ ችግር ምክንያት የእርስዎን ጨምሮ የአንዳንድ የምክክር ቀጠሮዎች ማረጋገጫ ዘግይቷል።"]

ይህ ችግር እንዳጉላላዎት እንረዳለን፤ ይቅርታም እንጠይቃለን። ቡድናችን ስለ ችግሩ መረጃ ደርሶታል፤ መፍትሔ ለመስጠትም እየሠራ ነው። የጉዳይዎ ሁኔታ እንደሚከተለው ነው፦
- [እስካሁን ለዚህ ደንበኛ የተደረገው፤ ለምሳሌ፦ "ክፍያዎ ተመዝግቧል፤ ቀጠሮዎም አሁን ተረጋግጧል።"]
- [አሁንም በሂደት ላይ ያለ ነገር ካለ እና ማን እየተከታተለው እንደሆነ።]

እስከ {{follow_up_time}} ድረስ ወቅታዊ መረጃ እናደርስዎታለን። አሁንም የማይሠራ ነገር ካለ፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን በመጥቀስ ለዚህ ኢሜይል ምላሽ ይስጡ።

ስለ ትዕግስትዎ እና በByfluence ላይ ስላሳደሩት እምነት እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** a confirmed problem on Byfluence's side (outage, booking or payment system error, notification failure, missing Google Meet links caused by the platform) affected this customer.
- **Confirm first:** only send after a supervisor or Technical team has confirmed the incident. Check Announcements for approved incident wording and use it in the first bracketed line.
- **Fill in all bracketed lines** with plain, factual statements. Do not use technical jargon ("callback", "API"). Remove a bullet if it does not apply.
- **Do not:** promise compensation, refunds, credits, a fix time or that "it will never happen again". Do not blame a payment provider or partner by name unless management has approved that statement.

<!-- template -->
# Thanking the customer for patience
id: tpl-thank-patience
category: acknowledgments
channel: any
style: short
tags: thank you, patience, waiting, holding message, still checking, ትዕግስት, እናመሰግናለን
related: tpl-delayed-response-apology, tpl-greeting-returning-customer

## Message (EN)
Thank you for your patience, {{customer_name}}. I'm still working on your case {{ticket_id}} and will update you by {{follow_up_time}}.

## Message (AM)
ስለ ትዕግስትዎ እናመሰግናለን {{customer_name}}። የጉዳይ ቁጥር {{ticket_id}}ን አሁንም እየተከታተልኩ ነው፤ እስከ {{follow_up_time}} ድረስ አሳውቅዎታለሁ።

## Usage Notes
- **When to use:** a quick holding message during a live chat or Telegram conversation while you check something, or when the customer asks "any news?" and there is nothing new yet.
- **Live conversation:** if you will answer within the same conversation, replace the last part with "I'll be right back with you." / "በቅርቡ እመለሳለሁ።" — and then actually come back.
- **Do not:** send this repeatedly without progress. If the customer has received it more than once, send a real status update or escalate.

<!-- template -->
# Responding to an angry customer
id: tpl-angry-customer-deescalation
category: acknowledgments
channel: any
style: standard
tags: angry customer, upset, frustrated, rude, shouting, de-escalation, complaint, የተናደደ ደንበኛ, ቁጣ
related: tpl-acknowledge-complaint, tpl-acknowledge-complaint-formal, tpl-delayed-response-apology

## Message (EN)
Hello {{customer_name}},

I can see how frustrated you are, and I'm sorry for what you've been through. I'm here to help you, and I'll stay with your case until you have a clear answer.

So that I don't miss anything, here is what I understand: [summarise the problem in one calm sentence, using the customer's own key words].

Here is what I'm doing right now: [the one concrete step you are taking, e.g. "I have sent your payment details to our payments team to check against the provider's records."]

Your case number is {{ticket_id}}, and I will update you by {{follow_up_time}}. If you would prefer, I can also ask a senior member of our team to review your case.

{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ምን ያህል እንደተበሳጩ ይገባኛል፤ ላጋጠመዎትም ነገር ይቅርታ እጠይቃለሁ። ልረዳዎት እዚህ ነኝ፤ ግልጽ ምላሽ እስኪያገኙ ድረስም ጉዳይዎን እከታተላለሁ።

ምንም ነገር እንዳያመልጠኝ፣ የተረዳሁት ይህ ነው፦ [ችግሩን የደንበኛውን ዋና ዋና ቃላት በመጠቀም በአንድ የተረጋጋ ዓረፍተ ነገር ይጻፉ]።

አሁን እያደረግሁ ያለሁት፦ [የሚወስዱትን አንድ ተጨባጭ እርምጃ ይጻፉ፤ ለምሳሌ፦ "የክፍያዎን ዝርዝር ከክፍያ አቅራቢው መዝገብ ጋር እንዲያመሳክር ለክፍያ ቡድናችን ልኬዋለሁ።"]

የጉዳይዎ ቁጥር {{ticket_id}} ነው፤ እስከ {{follow_up_time}} ድረስ አሳውቅዎታለሁ። ከፈለጉ ጉዳይዎን ከቡድናችን ከፍተኛ ባለሙያ አንዱ እንዲመለከተው ማድረግ እችላለሁ።

{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** the customer is upset, uses capital letters, threatens to leave bad reviews, or has contacted us several times about the same issue.
- **Before sending:** read the full history so you do not ask for anything they have already given. Replace both bracketed lines — the summary shows you listened; the action shows something is happening.
- **Tone:** never write "calm down", "as I already said", "you should have…" or "that's our policy". Do not match the customer's tone; stay warm and steady.
- **Abuse and threats:** if the customer uses insults, threats of violence or discriminatory language, do not reply in kind. Send one polite boundary message ("I want to help you, and I'll be able to do that best if we keep the conversation respectful."), record it, and inform your supervisor. Threats of harm go to Trust & Safety.
- **Supervisor offer:** only offer it if you will actually escalate. When you do, assign the ticket to Senior Support / Supervisor and note the reason.
- **Do not:** offer refunds, discounts or compensation to calm the customer down. Do not promise what another team will decide.

<!-- template -->
# Payment investigation started
id: tpl-payment-investigation
category: payments
channel: any
style: standard
tags: payment investigation, checking payment, payment problem, verify transaction, money deducted, ክፍያ ማጣራት, ክፍያ ተቆርጧል
related: pay-paid-booking-not-confirmed, pay-pending-transaction, pay-duplicate-charge, tpl-payment-investigation-short, tpl-request-transaction-ref

## Message (EN)
Hello {{customer_name}},

Thank you for sending the details. I have started an investigation into your payment of {{amount}} made with {{payment_method}} (transaction reference {{transaction_id}}).

Our payments team will check this transaction against the payment provider's records. While we check:
- Please do not make the same payment again, as this could lead to a double charge.
- Please keep your receipt or payment SMS in case we need it.

Your case number is {{ticket_id}}. I will update you by {{follow_up_time}}, or sooner if we have news.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ዝርዝር መረጃውን ስለላኩልን እናመሰግናለን። በ{{payment_method}} የፈጸሙትን የ{{amount}} ክፍያ (የግብይት መለያ ቁጥር {{transaction_id}}) ማጣራት ጀምረናል።

የክፍያ ቡድናችን ይህንን ግብይት ከክፍያ አቅራቢው መዝገብ ጋር ያመሳክራል። ማጣራቱ እስኪጠናቀቅ ድረስ፦
- እባክዎ ተመሳሳዩን ክፍያ በድጋሚ አይፈጽሙ፤ ይህ ሁለት ጊዜ እንዲቆረጥብዎ ሊያደርግ ይችላል።
- አስፈላጊ ሊሆን ስለሚችል እባክዎ ደረሰኝዎን ወይም የክፍያ ኤስኤምኤሱን ያስቀምጡ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። እስከ {{follow_up_time}} ድረስ፣ ወይም ከዚያ ቀደም አዲስ መረጃ ካለ፣ አሳውቅዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** after you have received the transaction reference and escalated the payment to Payments & Finance (or started checking it yourself with authorized access).
- **Fill in:** `{{amount}}` exactly as on the customer's receipt (in ETB), `{{payment_method}}` as the customer named it, `{{transaction_id}}` from the receipt, `{{follow_up_time}}` as agreed with Payments.
- **Session soon?** If the paid consultation starts soon, mark the ticket High/Critical and tell the customer you are treating it as urgent — but do not promise the booking will be confirmed in time.
- **Do not:** say "your payment was successful" or "you will get your money back" before Payments confirms. Do not name a provider as the cause of the problem.

<!-- template -->
# Payment investigation started — short
id: tpl-payment-investigation-short
category: payments
channel: any
style: short
tags: payment investigation, checking payment, quick update, ክፍያ ማጣራት
related: tpl-payment-investigation, pay-paid-booking-not-confirmed

## Message (EN)
Thanks, {{customer_name}}. We're now checking payment {{transaction_id}} with our payments team. Please don't pay again meanwhile. I'll update you by {{follow_up_time}}. Case: {{ticket_id}}

## Message (AM)
እናመሰግናለን {{customer_name}}። የግብይት ቁጥር {{transaction_id}}ን ከክፍያ ቡድናችን ጋር እያጣራን ነው። እስከዚያው እባክዎ በድጋሚ አይክፈሉ። እስከ {{follow_up_time}} ድረስ አሳውቅዎታለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Usage Notes
- **When to use:** Telegram/chat confirmation that the payment check has started.
- **Fill in:** `{{transaction_id}}`, `{{follow_up_time}}`, `{{ticket_id}}`.
- **Do not:** suggest the payment is fine or that money will be returned before Payments confirms.

<!-- template -->
# Payment failed: what to do
id: tpl-payment-failed-guidance
category: payments
channel: any
style: standard
tags: payment failed, transaction failed, payment declined, could not pay, payment error, ክፍያ አልተሳካም, ክፍያ አልሄደም
related: pay-failed-transaction, pay-pending-transaction, tpl-request-transaction-ref, tpl-request-screenshot

## Message (EN)
Hello {{customer_name}},

I'm sorry your payment didn't go through. When a payment fails, the booking or order is not confirmed — a booking is confirmed only after a successful payment. Here's what to do:

**1. Check whether money left your account.** Look at your bank or mobile-money SMS or your transaction history.
- **If money WAS taken:** please don't pay again yet. Send me the transaction reference, the amount and the time of payment, and I will check it for you.
- **If NO money was taken:** you can try the payment again.

**2. Before trying again, please check that:**
- you have enough balance, including any charges from your provider,
- your internet connection is stable,
- the payment details you enter are correct,
- you keep the page or app open until you are returned to Byfluence.

**3. If it fails again,** send me a screenshot of the error message (please cover any card numbers, PINs or codes), and I will look into it.

Please never share your PIN or verification codes with anyone, including Byfluence staff.

Your case number is {{ticket_id}}.

## Message (AM)
ሰላም {{customer_name}}፣

ክፍያዎ ባለመሳካቱ ይቅርታ እንጠይቃለን። ክፍያ ካልተሳካ ቀጠሮው ወይም ትዕዛዙ አይረጋገጥም — ቀጠሮ የሚረጋገጠው ክፍያው በተሳካ ሁኔታ ሲፈጸም ብቻ ነው። ማድረግ ያለብዎት የሚከተለውን ነው፦

**1. ከሂሳብዎ ገንዘብ መቆረጡን ያረጋግጡ።** ከባንክዎ ወይም ከሞባይል ገንዘብ አቅራቢዎ የደረሰዎትን ኤስኤምኤስ ወይም የግብይት ታሪክዎን ይመልከቱ።
- **ገንዘብ ተቆርጦ ከሆነ፦** እባክዎ ገና በድጋሚ አይክፈሉ። የግብይት መለያ ቁጥሩን፣ የገንዘቡን መጠን እና የከፈሉበትን ሰዓት ይላኩልኝ፤ አጣራልዎታለሁ።
- **ምንም ገንዘብ ካልተቆረጠ፦** ክፍያውን በድጋሚ መሞከር ይችላሉ።

**2. በድጋሚ ከመሞከርዎ በፊት እባክዎ የሚከተሉትን ያረጋግጡ፦**
- የአቅራቢዎን ክፍያዎች ጨምሮ በቂ ቀሪ ሂሳብ እንዳለዎት፣
- የኢንተርኔት ግንኙነትዎ የተረጋጋ መሆኑን፣
- የሚያስገቡት የክፍያ መረጃ ትክክል መሆኑን፣
- ወደ Byfluence እስኪመለሱ ድረስ ገጹን ወይም መተግበሪያውን አለመዝጋትዎን።

**3. በድጋሚ ካልተሳካ፣** የስህተት መልዕክቱን ስክሪንሾት ይላኩልኝ (የካርድ ቁጥር፣ ፒን ወይም ኮድ ካለበት እባክዎ ይሸፍኑት)፤ እኔም አጣራዋለሁ።

እባክዎ ፒንዎን ወይም የማረጋገጫ ኮድዎን ለማንም፣ የByfluence ሠራተኞችንም ጨምሮ፣ በፍጹም አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

## Usage Notes
- **When to use:** the customer reports a failed or declined payment, or the system shows the payment as Failed.
- **Check first:** look up the attempt in the admin dashboard (if you have access) — if it shows Successful or Pending, use `tpl-payment-verified-booking-confirmed` or `tpl-payment-pending-explain` instead.
- **Method availability:** do not suggest switching to a specific payment method unless the Feature Status page shows it is live.
- **Slot availability:** if the customer is retrying for a consultation, they may need to re-select the time slot. Do not promise the same slot will still be available.
- **Do not:** say a deducted amount "will be reversed automatically" or give a reversal time — that depends on the provider and is not confirmed.

<!-- template -->
# Payment pending explanation
id: tpl-payment-pending-explain
category: payments
channel: any
style: standard
tags: payment pending, processing, awaiting confirmation, stuck payment, not confirmed yet, ክፍያ በመጠባበቅ ላይ, አልተረጋገጠም
related: pay-pending-transaction, pay-paid-booking-not-confirmed, tpl-payment-investigation

## Message (EN)
Hello {{customer_name}},

Thank you for your patience. Your payment (transaction reference {{transaction_id}}) currently shows as **pending**. This means the payment has been started, but Byfluence has not yet received the final confirmation from {{payment_method}}.

What this means for you:
- Your booking or order will be confirmed once the payment is confirmed as successful.
- If the payment does not succeed, the booking or order will not be confirmed. If money was deducted in that case, we will help you follow it up.
- Please do not pay again while the payment is pending, as this could lead to a double charge.

I am following this payment and will update you by {{follow_up_time}}. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስለ ትዕግስትዎ እናመሰግናለን። ክፍያዎ (የግብይት መለያ ቁጥር {{transaction_id}}) በአሁኑ ጊዜ **በመጠባበቅ ላይ (pending)** እንዳለ ያሳያል። ይህ ማለት ክፍያው ተጀምሯል፤ ነገር ግን Byfluence ከ{{payment_method}} የመጨረሻውን ማረጋገጫ ገና አላገኘም ማለት ነው።

ይህ ለእርስዎ ምን ማለት ነው፦
- ክፍያው በተሳካ ሁኔታ መፈጸሙ እንደተረጋገጠ ቀጠሮዎ ወይም ትዕዛዝዎ ይረጋገጣል።
- ክፍያው ካልተሳካ ቀጠሮው ወይም ትዕዛዙ አይረጋገጥም። በዚህ ሁኔታ ገንዘብ ተቆርጦ ከሆነ ጉዳዩን እንዲከታተሉ እንረዳዎታለን።
- ክፍያው በመጠባበቅ ላይ እያለ እባክዎ በድጋሚ አይክፈሉ፤ ይህ ሁለት ጊዜ እንዲቆረጥብዎ ሊያደርግ ይችላል።

ይህንን ክፍያ እየተከታተልኩ ነው፤ እስከ {{follow_up_time}} ድረስም አሳውቅዎታለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** the payment record shows status Pending in authorized tools, or the customer sees "pending/processing" after paying.
- **Verify first:** look up `{{transaction_id}}` before sending. If it is actually Successful or Failed, use the matching template instead.
- **Session soon?** If the booking is for a session starting soon and the payment is still pending, escalate to Payments & Finance as High/Critical; do not tell the customer the slot is guaranteed.
- **Do not:** say "pending payments always go through" or give a time by which pending payments clear — no approved wording exists. Use `{{estimated_resolution_time}}` only if Payments gives approved wording.

<!-- template -->
# Payment verified and booking confirmed
id: tpl-payment-verified-booking-confirmed
category: payments
channel: any
style: standard
tags: payment verified, booking confirmed, payment successful, resolved payment, confirmation, ክፍያ ተረጋግጧል, ቀጠሮ ተረጋግጧል
related: pay-paid-booking-not-confirmed, pay-pending-transaction, tpl-payment-investigation

## Message (EN)
Hello {{customer_name}},

Good news: we have verified your payment of {{amount}} (transaction reference {{transaction_id}}), and your booking is now confirmed.

**Your booking:**
- Consultation: {{product_name}}
- Consultant: {{seller_name}}
- Date: {{booking_date}}
- Time: {{booking_time}}
- Booking ID: {{consultation_id}}

You can see this booking in your Byfluence dashboard under your consultation bookings. Please check that you have the Google Meet details for the session, and that the date and time match what you expected in your local time.

If anything looks wrong, or the meeting details are missing as the session approaches, just reply here or contact us through {{support_channel}} and mention case {{ticket_id}}.

Thank you for your patience, and we hope you have a great session.

{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

መልካም ዜና፦ የ{{amount}} ክፍያዎን (የግብይት መለያ ቁጥር {{transaction_id}}) አረጋግጠናል፤ ቀጠሮዎም አሁን ተረጋግጧል።

**የቀጠሮዎ ዝርዝር፦**
- ምክክር፦ {{product_name}}
- አማካሪ፦ {{seller_name}}
- ቀን፦ {{booking_date}}
- ሰዓት፦ {{booking_time}}
- የቀጠሮ መለያ ቁጥር፦ {{consultation_id}}

ይህንን ቀጠሮ በByfluence ዳሽቦርድዎ ላይ በምክክር ቀጠሮዎች ስር ማየት ይችላሉ። እባክዎ የምክክሩ የGoogle Meet መረጃ እንደደረሰዎት፣ እንዲሁም ቀኑና ሰዓቱ በአካባቢዎ ሰዓት አቆጣጠር እርስዎ ከጠበቁት ጋር እንደሚመሳሰል ያረጋግጡ።

የተሳሳተ ነገር ካዩ፣ ወይም የምክክሩ ሰዓት ሲቃረብ የስብሰባው መረጃ ካልደረሰዎት፣ እዚሁ ምላሽ ይስጡ ወይም በ{{support_channel}} በኩል ያግኙን፤ የጉዳይ ቁጥር {{ticket_id}}ን መጥቀስዎን አይርሱ።

ስለ ትዕግስትዎ እናመሰግናለን፤ መልካም ምክክር እንዲሆንልዎ እንመኛለን።

{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** only after you have confirmed in authorized tools that the payment is Successful AND the booking status is Confirmed.
- **Fill in every placeholder** from the booking record, not from the customer's message. Write `{{booking_time}}` with the time zone (e.g. "9:00 AM EAT / ጠዋት 3 ሰዓት") to avoid Ethiopian-time confusion.
- **Group consultations:** replace "Consultant" with the session host and remove the Booking ID line if there is no individual ID.
- **Do not:** send this if the booking is still pending, or say the Google Meet link "has been sent" unless you have checked it exists. Missing links go to Technical.

<!-- template -->
# Duplicate charge acknowledgment
id: tpl-duplicate-charge-ack
category: payments
channel: any
style: standard
tags: charged twice, duplicate charge, double payment, paid two times, deducted twice, ሁለት ጊዜ ተቆርጧል, ድርብ ክፍያ
related: pay-duplicate-charge, tpl-request-transaction-ref, tpl-payment-investigation

## Message (EN)
Hello {{customer_name}},

I'm sorry to hear you may have been charged more than once — I understand how worrying that is.

I have recorded this under case {{ticket_id}} and will pass it to our payments team to check. To help them, please send:
1. The transaction references of each payment
2. The date, time and amount of each payment
3. The payment method you used
4. Screenshots of the receipts or payment SMS messages, if you have them

Once our payments team has checked the records with the payment provider, I will let you know what they find and what the next steps are. In the meantime, please do not make any further payment for this booking or order.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ከአንድ ጊዜ በላይ ተቆርጦብዎት ሊሆን እንደሚችል በመስማቴ አዝናለሁ — ይህ ምን ያህል እንደሚያሳስብ ይገባኛል።

ጉዳዩን በጉዳይ ቁጥር {{ticket_id}} መዝግቤዋለሁ፤ እንዲያጣራውም ለክፍያ ቡድናችን አስተላልፋለሁ። ቡድኑን ለማገዝ እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የእያንዳንዱን ክፍያ የግብይት መለያ ቁጥር
2. የእያንዳንዱን ክፍያ ቀን፣ ሰዓት እና መጠን
3. የተጠቀሙበትን የክፍያ ዘዴ
4. ካለዎት የደረሰኞቹን ወይም የክፍያ ኤስኤምኤሶቹን ስክሪንሾት

የክፍያ ቡድናችን መዝገቦቹን ከክፍያ አቅራቢው ጋር አመሳክሮ እንደጨረሰ፣ ያገኘውን ውጤት እና ቀጣዩን እርምጃ አሳውቅዎታለሁ። እስከዚያው ድረስ እባክዎ ለዚህ ቀጠሮ ወይም ትዕዛዝ ተጨማሪ ክፍያ አይፈጽሙ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** the customer says they were charged twice (or more) for one booking or order.
- **Check first:** a "second charge" is sometimes a temporary hold, a failed attempt or a separate booking. Look up all references before escalating, and record each one in the ticket.
- **Escalate** every confirmed or suspected duplicate to Payments & Finance with all references.
- **Do not:** promise that the extra amount will be refunded, or when. Refund rules and timelines are not yet approved. Say only that Payments will check and you will share the next steps.

<!-- template -->
# Payment not found in our records
id: tpl-payment-not-found
category: payments
channel: any
style: standard
tags: payment not found, no record of payment, cannot find payment, missing payment, wrong reference, ክፍያው አልተገኘም
related: pay-paid-booking-not-confirmed, pay-failed-transaction, tpl-request-transaction-ref, tpl-request-screenshot

## Message (EN)
Hello {{customer_name}},

Thank you for your patience while we checked. At the moment, we cannot find a successful payment matching the details you sent (transaction reference {{transaction_id}}).

This can happen when:
- a character in the reference was mistyped,
- the payment was made while signed in to a different Byfluence account,
- the payment did not complete on the provider's side.

To help us look again, please:
1. Double-check the transaction reference and send a screenshot of the receipt or payment SMS.
2. Confirm the email address or phone number of the Byfluence account you were signed in to when you paid.
3. Check with {{payment_method}} or your bank whether the money actually left your account, or whether it was returned.

Your case stays open — as soon as you send this, we will check again. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

እስክናጣራ ድረስ ስለታገሱን እናመሰግናለን። በአሁኑ ጊዜ እርስዎ ከላኩልን መረጃ (የግብይት መለያ ቁጥር {{transaction_id}}) ጋር የሚዛመድ የተሳካ ክፍያ በመዝገባችን ላይ ማግኘት አልቻልንም።

ይህ ሊሆን የሚችለው፦
- በግብይት ቁጥሩ ላይ አንድ ፊደል ወይም ቁጥር በስህተት ተጽፎ ከሆነ፣
- ክፍያው የተፈጸመው በሌላ የByfluence አካውንት ገብተው ሳለ ከሆነ፣
- ክፍያው በአቅራቢው በኩል ሙሉ በሙሉ ሳይጠናቀቅ ቀርቶ ከሆነ ነው።

በድጋሚ ለማጣራት እንድንችል እባክዎ፦
1. የግብይት መለያ ቁጥሩን በድጋሚ ያረጋግጡ፤ የደረሰኙን ወይም የክፍያ ኤስኤምኤሱን ስክሪንሾትም ይላኩልን።
2. ሲከፍሉ የገቡበትን የByfluence አካውንት ኢሜይል አድራሻ ወይም ስልክ ቁጥር ያረጋግጡልን።
3. ገንዘቡ በእርግጥ ከሂሳብዎ መውጣቱን ወይም ተመልሶልዎት እንደሆነ {{payment_method}}ን ወይም ባንክዎን ይጠይቁ።

ጉዳይዎ ክፍት ሆኖ ይቆያል — ይህንን እንደላኩልን በድጋሚ እናጣራለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** you (or Payments) searched authorized records and found no successful payment for the reference given.
- **Search well before sending:** try the reference with and without spaces/prefixes, search by the customer's account and payment time, and check Failed and Pending records.
- **Tone:** never imply the customer is lying. Most cases are typing mistakes, a second account, or a payment that did not complete.
- **Fraud signals** (reference belongs to another customer, edited receipt, repeated "not found" claims across accounts): do not accuse — record the details and escalate to Trust & Safety.
- **Do not:** close the ticket while the customer is gathering information, or tell them the money "will come back" — that depends on their provider.
