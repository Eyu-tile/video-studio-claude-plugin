<!-- template -->
# First Telegram response
id: tpl-greeting-telegram
category: openings
channel: telegram
style: standard
tags: greeting, first reply, hello, telegram, welcome, ሰላምታ, እንኳን በደህና መጡ
related: tpl-greeting-telegram-friendly, tpl-wrong-language-switch, tpl-request-customer-info

## Message (EN)
Hello {{customer_name}}, thank you for contacting Byfluence Support. My name is {{support_agent}}.

How can I help you today? If your question is about a booking, an order or a payment, please include the booking or order number if you have it — it helps me find your details faster.

## Message (AM)
ሰላም {{customer_name}}፣ Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ስሜ {{support_agent}} ነው።

ዛሬ በምን ልርዳዎት? ጥያቄዎ ስለ ቀጠሮ፣ ስለ ትዕዛዝ ወይም ስለ ክፍያ ከሆነ፣ ካለዎት የቀጠሮውን ወይም የትዕዛዙን ቁጥር አብረው ቢልኩልኝ መረጃዎን በፍጥነት ለማግኘት ይረዳኛል።

## Usage Notes
- **When to use:** your first reply to a new Telegram conversation when the customer has only said "hello" or has not yet explained the problem clearly.
- **Language:** send the Amharic version by default. Send English only if the customer wrote in English or asked for it (see `tpl-wrong-language-switch`).
- **Fill in:** `{{customer_name}}` from the Telegram profile or the customer's message. If the profile name is a nickname, an emoji or clearly not a real name, remove the name and start with "Hello," / "ሰላም፣".
- **If the customer already explained the issue:** skip this greeting and go straight to the matching template (for example `tpl-request-transaction-ref` for payment problems). Do not make them repeat themselves.
- **Do not:** promise a response time, share personal contact numbers, or ask for passwords, PINs or verification codes.

<!-- template -->
# First Telegram response — friendly
id: tpl-greeting-telegram-friendly
category: openings
channel: telegram
style: friendly
tags: greeting, friendly, warm hello, telegram, welcome, ሰላምታ, እንኳን በደህና መጡ
related: tpl-greeting-telegram, tpl-wrong-language-switch

## Message (EN)
Hi {{customer_name}}! Welcome to Byfluence Support — I'm {{support_agent}}, and I'm happy to help.

Tell me what's going on, and we'll look into it together.

## Message (AM)
ሰላም {{customer_name}}! ወደ Byfluence ድጋፍ እንኳን በደህና መጡ። እኔ {{support_agent}} ነኝ፤ ልረዳዎ ዝግጁ ነኝ።

ምን እንደገጠመዎት ይንገሩኝ፤ አብረን እንመለከተዋለን።

## Usage Notes
- **When to use:** a relaxed, informal Telegram opening — for example when the customer writes casually, is a repeat contact, or is a seller you are already in regular contact with.
- **Prefer the standard version** (`tpl-greeting-telegram`) when the customer sounds upset, formal, or is writing about money or account security. A cheerful tone can feel dismissive to a worried customer.
- **Fill in:** `{{customer_name}}` (remove it if the profile name is not a real name) and `{{support_agent}}`.
- **Do not:** add emojis or slang beyond what the customer uses, or say things like "no problem, we'll fix it" before you know what the issue is.

<!-- template -->
# First email response
id: tpl-greeting-email
category: openings
channel: email
style: formal
tags: email greeting, first reply, acknowledgment of email, case opened, ኢሜይል, ሰላምታ, የጉዳይ ቁጥር
related: tpl-request-customer-info, tpl-acknowledge-complaint-formal

## Subject (EN)
Your Byfluence Support request — case {{ticket_id}}

## Subject (AM)
የ Byfluence ድጋፍ ጥያቄዎ — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

Thank you for contacting Byfluence Support. We have received your message and opened case {{ticket_id}} for you.

My name is {{support_agent}}, and I will be handling your request. I am reviewing the details you shared and will reply as soon as possible with an update or with any questions I need answered to move forward.

When you reply, please keep the case number {{ticket_id}} in the subject line so your messages stay together.

For your security, Byfluence will never ask for your password, PIN or verification codes by email.

Kind regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ውድ {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። መልዕክትዎ ደርሶናል፤ ለጥያቄዎም የጉዳይ ቁጥር {{ticket_id}} ተከፍቷል።

ስሜ {{support_agent}} ነው፤ ጉዳይዎን የምከታተለው እኔ ነኝ። የላኩልንን ዝርዝር መረጃ እየተመለከትኩ ነው፤ በተቻለ ፍጥነት ወቅታዊ መረጃ ወይም ጉዳዩን ለማስቀጠል የሚያስፈልጉኝን ጥያቄዎች ይዤ እመለሳለሁ።

ምላሽ ሲሰጡ መልዕክቶችዎ በአንድ ቦታ እንዲቀመጡ እባክዎ የጉዳይ ቁጥሩን {{ticket_id}} በርዕሱ (subject) ላይ ያቆዩት።

ለደህንነትዎ ሲባል Byfluence የይለፍ ቃልዎን፣ ፒንዎን ወይም የማረጋገጫ ኮድዎን በኢሜይል በፍጹም አይጠይቅም።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** the first human reply to a new email, when you need time to investigate before giving a real answer.
- **If you can answer immediately,** do not send this holding message — answer the question directly and include the case number.
- **Language:** reply in the language the customer wrote in. If the email mixes both, send Amharic first, then English below a line.
- **Fill in:** `{{customer_name}}`, `{{ticket_id}}`, `{{support_agent}}`. Use the customer's name as written in the email signature or account, not the email address.
- **Do not:** promise a reply time ("within a day" etc.) — no response-time standard has been approved. If a supervisor gives approved wording, add it with `{{estimated_resolution_time}}`.

<!-- template -->
# Website live chat greeting
id: tpl-greeting-chat
category: openings
channel: chat
style: short
tags: live chat, website chat, greeting, hello, chat opening, ሰላምታ, ቻት
related: tpl-greeting-telegram, tpl-wrong-language-switch

## Message (EN)
Hi, welcome to Byfluence Support! I'm {{support_agent}}. How can I help you today?

## Message (AM)
ሰላም፣ ወደ Byfluence ድጋፍ እንኳን በደህና መጡ! እኔ {{support_agent}} ነኝ። በምን ልርዳዎት?

## Usage Notes
- **When to use:** the first line in a website live chat. Keep it short — chat customers expect a fast, simple start.
- **Name:** chat visitors may not be signed in, so this template does not use `{{customer_name}}`. Once they tell you their name, use it in your following messages.
- **Next step:** if the issue concerns their account, a booking or a payment, follow with `tpl-request-customer-info` or the specific information-request template. Do not discuss account details until you have confirmed who you are talking to (`tpl-verify-identity`).
- **Do not:** ask for passwords, PINs, verification codes or card numbers in chat — ever.

<!-- template -->
# Phone call opening (inbound)
id: tpl-phone-inbound-opening
category: openings
channel: phone
style: standard
tags: phone, call script, inbound call, answering a call, opening, ስልክ, የስልክ ጥሪ
related: tpl-verify-identity, tpl-angry-customer-deescalation, tpl-wrong-language-switch

## Message (EN)
**1. Greet**
"Hello, thank you for calling Byfluence Support. My name is {{support_agent}}. May I have your name, please?"
*(Pause. Write the name down and use it during the call.)*

**2. Invite the customer to explain**
"Thank you, {{customer_name}}. How can I help you today?"
*(Listen without interrupting. Take notes: what happened, when, which booking, order or payment.)*

**3. Confirm you understood**
"Just to make sure I have understood correctly: [summarise the problem in one sentence]. Is that right?"
*(Pause and wait for the customer to confirm or correct you.)*

**4. Find the account**
"So that I can find your account, could you please tell me the email address or phone number registered with Byfluence?"
*(Only ask the safe questions in `tpl-verify-identity`. Never ask for a password, PIN or code.)*

**5. Give the case number**
"Thank you. I have opened case number {{ticket_id}} for you. Let me repeat it slowly: {{ticket_id}}. Please keep this number in case you need to contact us again."
*(Read the number slowly, in groups. Offer to wait while they write it down.)*

**6. Security reminder**
"One more thing, for your safety: Byfluence will never ask you for your password, PIN or verification code — not on the phone, and not by message."

## Message (AM)
**1. ሰላምታ**
"ጤና ይስጥልኝ፣ ወደ Byfluence ድጋፍ ስለደወሉ እናመሰግናለን። ስሜ {{support_agent}} ነው። ስምዎን ማወቅ እችላለሁ?"
*(ቆም ይበሉ። ስሙን ይጻፉ፤ በጥሪው ውስጥ ይጠቀሙበት።)*

**2. ደንበኛው እንዲያስረዳ መጋበዝ**
"እናመሰግናለን {{customer_name}}። ዛሬ በምን ልርዳዎት?"
*(ሳያቋርጡ ያዳምጡ። ምን እንደተከሰተ፣ መቼ እንደሆነ፣ የትኛው ቀጠሮ፣ ትዕዛዝ ወይም ክፍያ እንደሆነ ይመዝግቡ።)*

**3. መረዳትዎን ማረጋገጥ**
"በትክክል መረዳቴን ለማረጋገጥ ያህል፦ [ችግሩን በአንድ ዓረፍተ ነገር ያጠቃልሉ]። ልክ ነው?"
*(ቆም ብለው ደንበኛው እስኪያረጋግጥ ወይም እስኪያርም ይጠብቁ።)*

**4. አካውንቱን ማግኘት**
"አካውንትዎን ለማግኘት እባክዎ በByfluence የተመዘገበውን ኢሜይል አድራሻ ወይም ስልክ ቁጥር ይንገሩኝ።"
*(በ`tpl-verify-identity` ያሉትን ደህንነታቸው የተጠበቀ ጥያቄዎች ብቻ ይጠይቁ። የይለፍ ቃል፣ ፒን ወይም ኮድ በፍጹም አይጠይቁ።)*

**5. የጉዳይ ቁጥሩን መስጠት**
"እናመሰግናለን። ለጉዳይዎ የጉዳይ ቁጥር {{ticket_id}} ከፍቻለሁ። ቀስ ብዬ በድጋሚ ልንገርዎ፦ {{ticket_id}}። በድጋሚ ሲያገኙን እንዲጠቀሙበት እባክዎ ይህንን ቁጥር ይያዙት።"
*(ቁጥሩን በቡድን በቡድን ቀስ ብለው ያንብቡ። እስኪጽፉት ድረስ መጠበቅ እንደሚችሉ ይንገሯቸው።)*

**6. የደህንነት ማሳሰቢያ**
"ለደህንነትዎ ሲባል አንድ ነገር ላስታውስዎ፦ Byfluence የይለፍ ቃልዎን፣ ፒንዎን ወይም የማረጋገጫ ኮድዎን በስልክም ሆነ በመልዕክት በፍጹም አይጠይቅዎትም።"

## Usage Notes
- **When to use:** every inbound support call.
- **Language:** open in Amharic by default. If the caller answers in English or asks for English, switch to the English script and stay in English for the rest of the call.
- **Pace:** speak slowly and clearly; many callers are on mobile networks with poor sound. Repeat numbers (case IDs, references) twice and ask the caller to read them back.
- **Fill in:** `{{support_agent}}` (your first name is enough), `{{customer_name}}` once given, `{{ticket_id}}` once the ticket is created. Replace the bracketed summary with your own words.
- **Recording:** do not tell callers the call is or is not recorded until management confirms the call-recording policy.
- **Do not:** promise an outcome or a callback time on the call. If you will call back, agree a `{{follow_up_time}}` only if your shift plan allows it, and record it in the ticket.

<!-- template -->
# Outbound phone call introduction
id: tpl-phone-outbound-intro
category: openings
channel: phone
style: standard
tags: phone, outbound call, call back, calling customer, call script, ስልክ, መልሶ መደወል
related: tpl-phone-inbound-opening, tpl-verify-identity, tpl-never-share-otp-warning

## Message (EN)
**1. Ask for the customer**
"Hello, may I speak with {{customer_name}}, please?"
*(If someone else answers: "I'm calling from Byfluence Support. Could you tell me a good time to reach {{customer_name}}?" Do not mention the reason for the call or any details to another person.)*

**2. Introduce yourself and the reason**
"Hello {{customer_name}}, my name is {{support_agent}}, and I'm calling from Byfluence Support about your case {{ticket_id}}. Is this a good time to talk for a few minutes?"
*(If no: "No problem. When would be a better time for me to call you back?" Record the time in the ticket.)*

**3. Security reassurance — say this before anything else**
"Before we continue: Byfluence will never ask you for your password, PIN or any verification code — on this call or any other."

**4. Confirm you have the right person**
"To make sure I'm speaking with the account holder, could you please confirm the email address or phone number registered on your account?"
*(Let the customer say it. Do not read their details out first and ask them to agree.)*

**5. Purpose of the call**
"I'm calling to [give an update on your case / ask a few questions about your booking, order or payment]."
*(Keep it brief. Check understanding: "Does that make sense?")*

**6. Close**
"Thank you for your time, {{customer_name}}. If you need us, you can reach us through {{support_channel}} — please mention case {{ticket_id}}."

**If the call goes to voicemail**
"Hello, this is {{support_agent}} from Byfluence Support, calling for {{customer_name}} about case {{ticket_id}}. Please contact us through {{support_channel}}. Thank you."

## Message (AM)
**1. ደንበኛውን መጠየቅ**
"ጤና ይስጥልኝ፣ {{customer_name}}ን ማነጋገር እችላለሁ?"
*(ሌላ ሰው ካነሳ፦ "ከByfluence ድጋፍ ነው የምደውለው። {{customer_name}}ን በየትኛው ሰዓት ባገኛቸው ይመቻል?" ብለው ይጠይቁ። የጥሪውን ምክንያት ወይም ማንኛውንም ዝርዝር ለሌላ ሰው አይናገሩ።)*

**2. ራስን ማስተዋወቅና የጥሪውን ምክንያት መግለጽ**
"ጤና ይስጥልኝ {{customer_name}}፣ ስሜ {{support_agent}} ይባላል፤ የምደውለው ከByfluence ድጋፍ ሲሆን፣ የጉዳይ ቁጥር {{ticket_id}}ን በተመለከተ ነው። ለጥቂት ደቂቃዎች ለመነጋገር አሁን አመቺ ጊዜ ነው?"
*(አመቺ ካልሆነ፦ "ችግር የለም። መቼ መልሼ ብደውል ይመችዎታል?" ሰዓቱን በቲኬቱ ላይ ይመዝግቡ።)*

**3. የደህንነት ማረጋገጫ — ከሁሉም በፊት ይህንን ይናገሩ**
"ከመቀጠላችን በፊት፦ Byfluence የይለፍ ቃልዎን፣ ፒንዎን ወይም ማንኛውንም የማረጋገጫ ኮድ በዚህም ሆነ በሌላ ጥሪ በፍጹም አይጠይቅዎትም።"

**4. ትክክለኛውን ሰው ማነጋገርዎን ማረጋገጥ**
"የአካውንቱን ባለቤት እያነጋገርኩ መሆኔን ለማረጋገጥ፣ እባክዎ በአካውንትዎ ላይ የተመዘገበውን ኢሜይል አድራሻ ወይም ስልክ ቁጥር ይንገሩኝ።"
*(ደንበኛው ራሱ እንዲናገረው ያድርጉ። እርስዎ መረጃውን አንብበው "ትክክል ነው?" ብለው አይጠይቁ።)*

**5. የጥሪው ዓላማ**
"የደወልኩት [ስለ ጉዳይዎ ወቅታዊ መረጃ ለመስጠት / ስለ ቀጠሮዎ፣ ትዕዛዝዎ ወይም ክፍያዎ ጥቂት ጥያቄዎችን ለመጠየቅ] ነው።"
*(አጭር ያድርጉት። "ግልጽ ነው?" ብለው መረዳታቸውን ያረጋግጡ።)*

**6. መዝጊያ**
"ጊዜዎን ስለሰጡኝ እናመሰግናለን {{customer_name}}። ሲያስፈልግዎ በ{{support_channel}} በኩል ሊያገኙን ይችላሉ — እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን ይጥቀሱ።"

**ጥሪው ወደ ድምፅ መልዕክት (voicemail) ከሄደ**
"ጤና ይስጥልኝ፣ እኔ {{support_agent}} ከByfluence ድጋፍ ነኝ፤ {{customer_name}}ን የጉዳይ ቁጥር {{ticket_id}}ን በተመለከተ ለማግኘት ነበር የደወልኩት። እባክዎ በ{{support_channel}} በኩል ያግኙን። እናመሰግናለን።"

## Usage Notes
- **When to use:** any call you make to a customer or seller (follow-up, information request, update).
- **Why step 3 matters:** scammers in Ethiopia often call pretending to be "support" and ask for codes or mobile-money PINs. Saying this first builds trust and protects the customer.
- **Privacy:** never leave case details, amounts, product names or account information with a third person or on voicemail — only your name, Byfluence Support, the case number and how to contact us.
- **Fill in:** `{{customer_name}}`, `{{support_agent}}`, `{{ticket_id}}`, `{{support_channel}}` (the official channel your supervisor has confirmed — never a personal number).
- **Do not:** ask the customer to make a payment, install an app or share their screen during the call. Do not promise a result; if you are giving an update, use only what is recorded in the ticket.

<!-- template -->
# Returning customer with an open case
id: tpl-greeting-returning-customer
category: openings
channel: any
style: standard
tags: returning customer, open case, follow-up contact, existing ticket, repeat contact, ተመላሽ ደንበኛ, ክፍት ጉዳይ
related: tpl-delayed-response-apology, tpl-thank-patience

## Message (EN)
Hello {{customer_name}}, welcome back to Byfluence Support. I can see you already have an open case with us, {{ticket_id}}, so I'll continue from there — you won't need to explain everything again.

Latest update: [one sentence on the current status of the case].

Is your message today about this same case, or about something new?

## Message (AM)
ሰላም {{customer_name}}፣ በድጋሚ ስላገኙን እናመሰግናለን። ቀደም ብለው ያቀረቡት የጉዳይ ቁጥር {{ticket_id}} አሁንም ክፍት መሆኑን አይቻለሁ፤ ስለዚህ ሁሉንም ነገር እንደገና ማስረዳት ሳያስፈልግዎ ከዚያው እንቀጥላለን።

የቅርብ ጊዜ ሁኔታ፦ [የጉዳዩን የአሁኑ ሁኔታ በአንድ ዓረፍተ ነገር ይጻፉ]።

የዛሬው መልዕክትዎ ስለዚሁ ጉዳይ ነው ወይስ ስለ ሌላ አዲስ ጉዳይ?

## Usage Notes
- **When to use:** a customer with an open ticket contacts us again (same or a different channel).
- **Before sending:** read the whole ticket history and the latest internal note. Replace the bracketed line with a short, factual status, e.g. "Our payments team is still checking your transaction with the provider." / "የክፍያ ቡድናችን ግብይትዎን ከክፍያ አቅራቢው ጋር አሁንም እያጣራ ነው።"
- **If the customer has been waiting longer than expected,** combine with or switch to `tpl-delayed-response-apology`.
- **New issue?** Open a separate ticket and give the new case number; do not mix two problems in one ticket.
- **Do not:** guess a status or say "it's almost done" unless the ticket shows that. Do not open a duplicate ticket for the same problem.

<!-- template -->
# After-hours reply
id: tpl-after-hours
category: openings
channel: any
style: short
tags: after hours, out of office, closed, night, weekend, holiday, auto reply, ከሥራ ሰዓት ውጭ
related: tpl-account-compromise-urgent, tpl-never-share-otp-warning

## Message (EN)
Hello, thank you for contacting Byfluence Support. Our team is currently outside working hours, but your message has been received and we will reply as soon as we are back.

If you think someone else has accessed your account, please write "account security" in your message so we can see it first.

Never share your password, PIN or verification code with anyone.

## Message (AM)
ሰላም፣ Byfluence ድጋፍን ስላገኙን እናመሰግናለን። በአሁኑ ሰዓት ከሥራ ሰዓት ውጭ ነን፤ ሆኖም መልዕክትዎ ደርሶናል፤ ሥራ እንደጀመርን በተቻለ ፍጥነት እንመልስልዎታለን።

አካውንትዎን ሌላ ሰው ከፍቶታል ብለው ከጠረጠሩ፣ ቀድመን እንድናየው እባክዎ በመልዕክትዎ ላይ "የአካውንት ደህንነት" ብለው ይጻፉ።

የይለፍ ቃልዎን፣ ፒንዎን ወይም የማረጋገጫ ኮድዎን ለማንም አያጋሩ።

## Usage Notes
- **When to use:** automatic or manual replies sent outside staffed hours, and on public holidays.
- **No name needed:** this message works without `{{customer_name}}`, so it can be used as an auto-reply.
- **Do not add opening hours or a "we'll reply by…" time** until management approves official support hours. Do not list phone numbers or handles unless they are the confirmed official ones.
- **Next shift:** the first agent on shift should search new messages for "account security" / "የአካውንት ደህንነት" and handle those first with `tpl-account-compromise-urgent`. Sessions starting soon and payment problems for imminent bookings come next.

<!-- template -->
# Offering to continue in Amharic or English
id: tpl-wrong-language-switch
category: openings
channel: any
style: short
tags: language, amharic, english, switch language, translate, ቋንቋ, አማርኛ, እንግሊዝኛ
related: tpl-greeting-telegram, tpl-greeting-chat

## Message (EN)
Hello {{customer_name}}, I'm happy to continue in English or in Amharic — whichever is easier for you. Just let me know.

(በአማርኛ መቀጠል ከፈለጉ "አማርኛ" ብለው ይጻፉልኝ።)

## Message (AM)
ሰላም {{customer_name}}፣ በአማርኛም ሆነ በእንግሊዝኛ፣ ለእርስዎ በሚቀልዎት ቋንቋ መቀጠል እንችላለን። የትኛውን እንደሚመርጡ ብቻ ይንገሩኝ።

(If you prefer English, just reply "English".)

## Usage Notes
- **When to use:** the customer writes in a mix of languages, writes Amharic in Latin letters (e.g. "selam, kifiya alhedem"), seems to struggle with the language you used, or the first reply went out in the wrong language.
- **Default:** Amharic is our primary language. Use the English version only when the customer has written mainly in English.
- **Each version contains one line in the other language on purpose,** so a customer who reads only one language still understands the offer. Keep that line.
- **After they choose,** stay in that language for the rest of the conversation and note the preference in the ticket.
- **Other languages (e.g. Afaan Oromo, Tigrinya):** do not machine-translate customer messages into replies. Reply in Amharic or English and escalate to your supervisor if the customer cannot communicate in either — support in other languages has not been confirmed.

<!-- template -->
# Asking for customer information
id: tpl-request-customer-info
category: information-requests
channel: any
style: standard
tags: customer details, account info, information request, find account, registered email, phone number, መረጃ, የአካውንት መረጃ
related: tpl-verify-identity, tpl-request-screenshot, tpl-request-transaction-ref

## Message (EN)
Hello {{customer_name}},

Thank you for reaching out. So that I can find your account and look into this properly, please send me the following:

1. Your full name as registered on Byfluence
2. The email address or phone number you use to sign in
3. A short description of what happened and when
4. Any related booking, order or transaction number, if you have one

Please do not send your password, PIN, verification codes or card details — we will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን። አካውንትዎን አግኝቼ ጉዳዩን በአግባቡ ለማጣራት እባክዎ የሚከተሉትን መረጃዎች ይላኩልኝ፦

1. በByfluence ላይ የተመዘገበው ሙሉ ስምዎ
2. ለመግባት የሚጠቀሙበት ኢሜይል አድራሻ ወይም ስልክ ቁጥር
3. ምን እንደተከሰተና መቼ እንደሆነ አጭር ማብራሪያ
4. ካለዎት ተያያዥ የቀጠሮ፣ የትዕዛዝ ወይም የግብይት ቁጥር

እባክዎ የይለፍ ቃልዎን፣ ፒንዎን፣ የማረጋገጫ ኮድዎን ወይም የካርድ መረጃዎን አይላኩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** you need to locate the customer's account before you can help, and the customer has not given enough details yet.
- **Ask only for what you need.** Delete any line you already have the answer to — customers get frustrated when asked to repeat information.
- **On Telegram/chat:** remove the sign-off lines; keep the numbered list, it is easier to answer.
- **If the request involves changing account details, refunds or security,** use `tpl-verify-identity` instead, which asks for ownership checks.
- **Do not:** ask for national ID numbers, documents or photos of IDs here. Seller verification documents go only through the official seller verification flow.

<!-- template -->
# Requesting screenshots
id: tpl-request-screenshot
category: information-requests
channel: any
style: standard
tags: screenshot, picture, photo of screen, error message, receipt image, ስክሪንሾት, ፎቶ
related: tpl-request-screenshot-short, tpl-request-transaction-ref

## Message (EN)
Hello {{customer_name}},

A screenshot will help me see exactly what you are seeing. Please send a screenshot of:
- the screen or error message where the problem appears, and/or
- the payment receipt or confirmation message, if this is about a payment.

**How to take a screenshot:**
- Most Android phones: press the Power and Volume Down buttons at the same time.
- iPhone: press the Side button and Volume Up button at the same time.
- Computer: press the Print Screen (PrtSc) key, or use the Snipping Tool.

Before sending, please cover or crop out any card numbers, PINs or verification codes. We only need to see the screen, the date and time, and any reference numbers.

Thank you — your case number is {{ticket_id}}.

## Message (AM)
ሰላም {{customer_name}}፣

እርስዎ የሚያዩትን በትክክል ለማየት ስክሪንሾት (screenshot) በጣም ይረዳኛል። እባክዎ የሚከተሉትን ስክሪንሾት ይላኩልኝ፦
- ችግሩ የሚታይበትን ገጽ ወይም የስህተት መልዕክቱን፣ እና/ወይም
- ጉዳዩ ክፍያን የሚመለከት ከሆነ የክፍያ ደረሰኙን ወይም የማረጋገጫ መልዕክቱን።

**ስክሪንሾት እንዴት እንደሚነሳ፦**
- በአብዛኞቹ የAndroid ስልኮች፦ የማብሪያ/ማጥፊያ (Power) ቁልፉንና የድምፅ መቀነሻ (Volume Down) ቁልፉን በአንድ ጊዜ ይጫኑ።
- በiPhone፦ የጎን (Side) ቁልፉንና የድምፅ መጨመሪያ (Volume Up) ቁልፉን በአንድ ጊዜ ይጫኑ።
- በኮምፒውተር፦ Print Screen (PrtSc) ቁልፍን ይጫኑ ወይም Snipping Tool ይጠቀሙ።

ከመላክዎ በፊት የካርድ ቁጥር፣ ፒን ወይም የማረጋገጫ ኮድ በምስሉ ላይ ካለ እባክዎ ይሸፍኑት ወይም ቆርጠው ያውጡት። ማየት የሚያስፈልገን ገጹን፣ ቀኑንና ሰዓቱን እንዲሁም የመለያ ቁጥሮቹን ብቻ ነው።

እናመሰግናለን — የጉዳይዎ ቁጥር {{ticket_id}} ነው።

## Usage Notes
- **When to use:** error messages, display problems, "it says something strange" reports, and payment receipts.
- **Low digital literacy:** keep the "How to take a screenshot" steps for customers who seem unsure. If they still cannot, ask them to photograph the screen with another phone, or to type out the exact message.
- **On Telegram,** ask them to send it as a photo (not a file) so you can view it quickly in the conversation.
- **Verification:** screenshots can be edited. Always confirm payments by the transaction reference in authorized tools, never by screenshot alone. Do not tell the customer you doubt their screenshot.
- **Do not:** ask for screenshots of banking or mobile-money apps that show the full balance or PIN screens. Ask only for the specific receipt or message.

<!-- template -->
# Requesting screenshots — short
id: tpl-request-screenshot-short
category: information-requests
channel: any
style: short
tags: screenshot, quick request, photo, error, ስክሪንሾት
related: tpl-request-screenshot

## Message (EN)
Hi {{customer_name}}, could you send a screenshot of the screen or message you're seeing? Please hide any card numbers, PINs or codes first. Case: {{ticket_id}}

## Message (AM)
ሰላም {{customer_name}}፣ የሚያዩትን ገጽ ወይም መልዕክት ስክሪንሾት ሊልኩልኝ ይችላሉ? እባክዎ የካርድ ቁጥር፣ ፒን ወይም ኮድ ካለበት መጀመሪያ ይሸፍኑት። የጉዳይ ቁጥር፦ {{ticket_id}}

## Usage Notes
- **When to use:** Telegram or chat, when the customer is clearly comfortable with their phone and you need one quick image.
- **If they ask how,** send the full version `tpl-request-screenshot`, which includes step-by-step instructions.
- **Do not:** rely on the screenshot alone to confirm a payment — verify the reference in authorized tools.

<!-- template -->
# Requesting the transaction reference
id: tpl-request-transaction-ref
category: information-requests
channel: any
style: standard
tags: transaction reference, transaction id, payment reference, receipt number, payment sms, የግብይት ቁጥር, ደረሰኝ, ክፍያ
related: pay-paid-booking-not-confirmed, pay-failed-transaction, pay-pending-transaction, pay-duplicate-charge, tpl-request-transaction-ref-short

## Message (EN)
Hello {{customer_name}},

To trace your payment, I need the transaction reference. This is the code or number your payment provider gives you after a payment. You can usually find it in:
- the SMS confirmation from your bank or mobile-money provider,
- the receipt or transaction history in your payment app, or
- the payment confirmation page or email, if you received one.

Please send me:
1. The transaction reference
2. The date and approximate time of the payment
3. The amount and the payment method you used

A screenshot of the receipt is also helpful. Please do not share your PIN or any verification code.

Your case number is {{ticket_id}}.

## Message (AM)
ሰላም {{customer_name}}፣

ክፍያዎን ለመከታተል የግብይት መለያ ቁጥሩ (transaction reference) ያስፈልገኛል። ይህ ክፍያ ከፈጸሙ በኋላ የክፍያ አቅራቢዎ የሚሰጥዎ ኮድ ወይም ቁጥር ነው። ብዙውን ጊዜ በሚከተሉት ላይ ያገኙታል፦
- ከባንክዎ ወይም ከሞባይል ገንዘብ አገልግሎት አቅራቢዎ የደረሰዎት የማረጋገጫ ኤስኤምኤስ፣
- በክፍያ መተግበሪያዎ (app) ላይ ያለው ደረሰኝ ወይም የግብይት ታሪክ፣ ወይም
- ከደረሰዎት፣ የክፍያ ማረጋገጫ ገጽ ወይም ኢሜይል።

እባክዎ የሚከተሉትን ይላኩልኝ፦
1. የግብይት መለያ ቁጥሩን
2. ክፍያውን የፈጸሙበትን ቀን እና ግምታዊ ሰዓት
3. የከፈሉትን የገንዘብ መጠን እና የተጠቀሙበትን የክፍያ ዘዴ

የደረሰኙ ስክሪንሾትም ቢልኩ ይረዳል። እባክዎ ፒንዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

## Usage Notes
- **When to use:** any payment problem — paid but not confirmed, failed, pending, double charge, refund follow-up.
- **Payment methods:** do not name a specific provider (Chapa, Telebirr, M-Pesa, bank, card) as available unless the Feature Status page shows it is live. The wording above is deliberately generic.
- **Customers often send the wrong number** (their phone number, the booking ID, or the amount). If the reply does not look like a reference, kindly ask again and point to the SMS or receipt.
- **Record** the reference in the ticket's transaction field so `{{transaction_id}}` fills automatically in later messages.
- **Do not:** ask for a full card number, CVV, PIN, mobile-money PIN or OTP. Do not confirm or deny a payment until you have checked the reference in authorized tools.

<!-- template -->
# Requesting the transaction reference — short
id: tpl-request-transaction-ref-short
category: information-requests
channel: any
style: short
tags: transaction reference, quick request, payment sms, receipt, የግብይት ቁጥር
related: tpl-request-transaction-ref, pay-paid-booking-not-confirmed

## Message (EN)
Hi {{customer_name}}, please send the transaction reference from your payment SMS or receipt, plus the payment date, time and amount. Never share your PIN or codes. Case: {{ticket_id}}

## Message (AM)
ሰላም {{customer_name}}፣ እባክዎ ከክፍያ ኤስኤምኤስዎ ወይም ከደረሰኝዎ ላይ ያለውን የግብይት ቁጥር ከክፍያው ቀን፣ ሰዓትና መጠን ጋር ይላኩልኝ። ፒን ወይም ኮድ በፍጹም አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Usage Notes
- **When to use:** Telegram/chat when the customer already understands what a transaction reference is.
- **If they reply "where do I find it?",** send the full version `tpl-request-transaction-ref`.
- **Do not:** confirm anything about the payment before verifying the reference in authorized tools.

<!-- template -->
# Requesting booking details
id: tpl-request-booking-details
category: information-requests
channel: any
style: standard
tags: booking details, consultation booking, appointment, session time, time zone, ቀጠሮ, ምክክር, የኢትዮጵያ ሰዓት
related: pay-paid-booking-not-confirmed, tpl-request-transaction-ref

## Message (EN)
Hello {{customer_name}},

To find your consultation booking, please send me:
1. The booking or consultation ID, if you can see it in your Byfluence dashboard under your consultation bookings
2. The consultation title and the consultant's name
3. The date and time you booked
4. Whether it is a one-on-one or a group consultation
5. The email address or phone number on your Byfluence account

**About the time and date:** please tell me whether the time is in Ethiopian local time or international time (for example, "ጠዋት 3 ሰዓት" in Ethiopian time is 9:00 AM international time), and whether the date is in the Ethiopian or the Gregorian (European) calendar. This helps us avoid any mix-up.

Your case number is {{ticket_id}}.

## Message (AM)
ሰላም {{customer_name}}፣

የምክክር ቀጠሮዎን ለማግኘት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. በByfluence ዳሽቦርድዎ ላይ በምክክር ቀጠሮዎች ስር የሚታይ ከሆነ፣ የቀጠሮው ወይም የምክክሩ መለያ ቁጥር
2. የምክክሩ ርዕስ እና የአማካሪው ስም
3. ያስያዙት ቀን እና ሰዓት
4. ምክክሩ የግል (one-on-one) ወይስ የቡድን ምክክር መሆኑን
5. በByfluence አካውንትዎ ላይ የተመዘገበው ኢሜይል አድራሻ ወይም ስልክ ቁጥር

**ስለ ሰዓቱና ቀኑ፦** እባክዎ ሰዓቱ በኢትዮጵያ የሰዓት አቆጣጠር ነው ወይስ በዓለም አቀፍ (ፈረንጅ) አቆጣጠር እንደሆነ ይንገሩኝ (ለምሳሌ በኢትዮጵያ አቆጣጠር ጠዋት 3 ሰዓት በዓለም አቀፍ አቆጣጠር 9:00 AM ነው)። እንዲሁም ቀኑ በኢትዮጵያ ወይስ በፈረንጅ የቀን አቆጣጠር እንደሆነ ቢገልጹልኝ ግራ መጋባትን ለማስወገድ ይረዳናል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

## Usage Notes
- **When to use:** missing booking, wrong time, missing Google Meet link, reschedule or cancellation questions, seller or buyer no-show reports.
- **Time confusion is common.** Ethiopian time-of-day runs six hours behind the international clock, and Ethiopian calendar dates differ from Gregorian dates. Always confirm both before concluding that a buyer or seller "missed" a session. Record times in the ticket in international format with the time zone (EAT).
- **Group consultations:** capacity, cancellation and refund rules are not approved yet. Collect the details but do not promise a seat, a reschedule or a refund.
- **Sellers:** if a seller asks about a booking, ask for the buyer's name (as shown to the seller) and the session date/time instead of the buyer's contact details.
- **Do not:** share the other party's personal phone number or email.

<!-- template -->
# Requesting order details
id: tpl-request-order-details
category: information-requests
channel: any
style: standard
tags: order details, order number, purchase, product order, item problem, ትዕዛዝ, ዕቃ, የትዕዛዝ ቁጥር
related: tpl-request-transaction-ref, tpl-request-screenshot

## Message (EN)
Hello {{customer_name}},

To look into your order, please send me:
1. The order number, if you have it
2. The product name and the seller's name
3. The date you placed the order
4. The amount paid and the payment method you used
5. A short description of the problem (for example: not received, wrong item, damaged, different from the listing)
6. Clear photos of the item and packaging, if the item arrived damaged or different from what was described

Please do not share your password, PIN or card details.

Your case number is {{ticket_id}}.

## Message (AM)
ሰላም {{customer_name}}፣

ትዕዛዝዎን ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ካለዎት የትዕዛዝ ቁጥሩን
2. የዕቃውን ስም እና የሻጩን ስም
3. ትዕዛዙን ያስገቡበትን ቀን
4. የከፈሉትን የገንዘብ መጠን እና የተጠቀሙበትን የክፍያ ዘዴ
5. ችግሩን በአጭሩ (ለምሳሌ፦ አልደረሰኝም፣ የተሳሳተ ዕቃ መጣ፣ ተበላሽቶ ደረሰ፣ ከማስታወቂያው የተለየ ነው)
6. ዕቃው ተበላሽቶ ወይም ከተገለጸው የተለየ ሆኖ ከደረሰ፣ የዕቃውንና የማሸጊያውን ግልጽ ፎቶዎች

እባክዎ የይለፍ ቃልዎን፣ ፒንዎን ወይም የካርድ መረጃዎን አያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

## Usage Notes
- **Feature check first:** physical products, delivery and digital products are expansion features. Check the Feature Status page before treating an "order" as a live product order. If the feature is not live, the customer may be describing a consultation booking or an off-platform purchase — clarify kindly.
- **Off-platform purchases:** if the customer paid a seller directly outside Byfluence, record this in internal notes and escalate to Senior Support; do not promise that Byfluence can recover the money.
- **Delivery address:** only ask for it if delivery is live and the problem is about delivery; never ask for more than is needed (area/sub-city is usually enough to start).
- **Do not:** promise a replacement, a refund or a delivery date. Delivery times, areas and fees are not confirmed.

<!-- template -->
# Verifying account ownership (safe questions only)
id: tpl-verify-identity
category: information-requests
channel: any
style: formal
tags: verify identity, account ownership, security check, confirm account holder, ማረጋገጫ, የአካውንት ባለቤት
related: tns-account-compromise, acc-account-deletion-request, acc-locked-account, tpl-account-compromise-urgent

## Message (EN)
Dear {{customer_name}},

Thank you for your request. To protect your account, we need to confirm that we are speaking with the account owner before we can discuss account details or make any changes.

Please reply with the following:
1. The full name registered on the account
2. The email address and/or phone number registered on the account
3. One recent activity on the account — for example a booking or order number, or the date and amount of a recent payment

Please note: Byfluence will never ask for your password, PIN, verification (OTP) code or full card number. If anyone asks you for these — even if they say they are from Byfluence — please do not share them, and let us know.

Your case number is {{ticket_id}}.

Kind regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ውድ {{customer_name}}፣

ስለ ጥያቄዎ እናመሰግናለን። አካውንትዎን ለመጠበቅ ሲባል፣ ስለ አካውንቱ ዝርዝር ጉዳይ ከመነጋገራችን ወይም ማንኛውንም ለውጥ ከማድረጋችን በፊት የአካውንቱ ባለቤት እርስዎ መሆንዎን ማረጋገጥ ይኖርብናል።

እባክዎ የሚከተሉትን መረጃዎች በምላሽዎ ይላኩልን፦
1. በአካውንቱ ላይ የተመዘገበው ሙሉ ስም
2. በአካውንቱ ላይ የተመዘገበው ኢሜይል አድራሻ እና/ወይም ስልክ ቁጥር
3. በአካውንቱ ላይ በቅርቡ የተከናወነ አንድ እንቅስቃሴ — ለምሳሌ የቀጠሮ ወይም የትዕዛዝ ቁጥር፣ ወይም በቅርቡ የፈጸሙት ክፍያ ቀንና መጠን

እባክዎ ልብ ይበሉ፦ Byfluence የይለፍ ቃልዎን፣ ፒንዎን፣ የማረጋገጫ (OTP) ኮድዎን ወይም ሙሉ የካርድ ቁጥርዎን በፍጹም አይጠይቅም። ማንም ሰው — ከByfluence ነኝ ቢልም እንኳ — ይህንን መረጃ ከጠየቀዎት እባክዎ አያጋሩ፤ ለእኛም ያሳውቁን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Usage Notes
- **When to use:** before discussing or changing anything account-specific: email/phone changes, account deletion, locked or compromised accounts, refund details, seller earnings and withdrawals.
- **How to check:** compare the answers with the account record in the admin dashboard. The customer must provide the details — never read them out or hint ("Is it the one ending in 45?").
- **Sending channel matters:** if the request arrives from an email or phone number that is not the one on the account, treat it with extra care and do not make changes until ownership is confirmed through the registered contact.
- **If answers do not match,** or the person is pushing for urgent changes, stop, do not reveal any account information, and escalate to Trust & Safety.
- **Do not:** ask for passwords, OTP codes, PINs, full card numbers or ID documents in this message. ID document checks (if ever required) are decided by Trust & Safety, not by Level 1 agents.
