<!-- template -->
# Seller verification pending
id: tpl-seller-verification-pending
category: sellers
channel: any
style: standard
tags: verification pending, seller application, under review, not verified yet, ማረጋገጫ በሂደት ላይ, የሻጭ ማመልከቻ
related: sel-verification-pending, sel-verification-rejected

## Message (EN)
Hello {{customer_name}},

Thank you for applying to sell on Byfluence. I have checked your account, and your seller verification is currently **pending review** by our Seller Operations team.

There is nothing more you need to do right now unless our team contacts you for additional information. Please keep an eye on your email and your Byfluence account for any message from us.

We cannot confirm an exact review time, but you will be notified once a decision has been made. If you would like to check again, please contact us through {{support_channel}} and mention case {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{customer_name}}፣

በByfluence ላይ ለመሸጥ ስላመለከቱ እናመሰግናለን። መለያዎን አጣርቻለሁ፤ የሻጭ ማንነት ማረጋገጫዎ በአሁኑ ጊዜ በሻጭ ኦፕሬሽንስ ቡድናችን **በግምገማ ላይ** ይገኛል።

ቡድናችን ተጨማሪ መረጃ ለመጠየቅ ካላገኘዎት በስተቀር አሁን ማድረግ የሚጠበቅብዎ ሌላ ነገር የለም። እባክዎ ከእኛ የሚላክ መልዕክት እንዳያመልጥዎ ኢሜይልዎን እና የByfluence መለያዎን ይከታተሉ።

ግምገማው የሚጠናቀቅበትን ትክክለኛ ጊዜ ማረጋገጥ አንችልም፤ ሆኖም ውሳኔ እንደተሰጠ ይነገርዎታል። እንደገና ማጣራት ከፈለጉ፣ እባክዎ በ{{support_channel}} በኩል ያግኙን እና የጉዳይ ቁጥር {{ticket_id}}ን ይጥቀሱ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A seller applicant asks why they cannot sell yet and the admin dashboard shows verification status **Pending**.

**Fill in:** `{{customer_name}}` (the seller's name), `{{support_channel}}`, `{{ticket_id}}`.

**Do NOT promise:** approval, a review time ("within X days"), or that you can speed it up. Do not ask for ID documents in this message — documents are requested only by Seller Operations through the approved channel (see *tpl-seller-docs-resubmit*). If the application has been pending unusually long by your team's standard, escalate to Seller Operations rather than guessing.

<!-- template -->
# Seller verification not approved
id: tpl-seller-verification-rejected
category: sellers
channel: email
style: formal
tags: verification rejected, seller application rejected, not approved, seller denied, ማረጋገጫ አልጸደቀም, ማመልከቻ ውድቅ
related: sel-verification-rejected, sel-docs-resubmit

## Subject (EN)
Update on your Byfluence seller verification — case {{ticket_id}}

## Subject (AM)
የByfluence የሻጭ ማረጋገጫዎን በተመለከተ — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

Thank you for your interest in selling on Byfluence and for the time you took to complete your application.

After careful review, we are unable to approve your seller verification at this time.

Reason provided by our review team:
[insert the reason exactly as approved by Seller Operations]

We understand this may be disappointing. If you believe a mistake has been made, or if you would like to know whether and how you may apply again, please reply to this email quoting case number {{ticket_id}}, and our team will guide you.

Thank you for your understanding.

Sincerely,
{{support_agent}}
Byfluence Customer Support

## Message (AM)
ውድ {{customer_name}}፣

በByfluence ላይ ለመሸጥ ስላሳዩት ፍላጎት እና ማመልከቻዎን ለማሟላት ስለሰጡት ጊዜ እናመሰግናለን።

ማመልከቻዎን በጥንቃቄ ከገመገምን በኋላ፣ የሻጭ ማንነት ማረጋገጫዎን በአሁኑ ጊዜ ማጽደቅ እንዳልቻልን በአክብሮት እናሳውቃለን።

የግምገማ ቡድናችን የሰጠው ምክንያት፦
[በሻጭ ኦፕሬሽንስ የጸደቀውን ምክንያት በትክክል እዚህ ያስገቡ]

ይህ ውሳኔ ቅር ሊያሰኝዎ እንደሚችል እንረዳለን። ስህተት ተፈጽሟል ብለው ካመኑ፣ ወይም እንደገና ማመልከት የሚችሉ መሆኑን እና እንዴት እንደሆነ ማወቅ ከፈለጉ፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን ጠቅሰው ለዚህ ኢሜይል ምላሽ ይስጡ፤ ቡድናችን ይመራዎታል።

ስለ ግንዛቤዎ እናመሰግናለን።

ከአክብሮት ሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** Seller Operations has recorded a **Rejected** verification decision and asked Support to inform the applicant, or the applicant asks why they were rejected.

**Fill in:** Replace the bracketed line with the reason **exactly as approved by Seller Operations** (keep it factual and short). If Seller Operations has not given a shareable reason, remove the "Reason" lines entirely — never invent one.

**Do NOT:** promise that a new application will be approved, state a waiting period before re-applying, or reveal internal fraud checks or risk scores. Re-application rules are not confirmed. If the applicant disputes the decision or becomes aggressive, escalate to Seller Operations / Senior Support.

<!-- template -->
# Request to resubmit verification documents
id: tpl-seller-docs-resubmit
category: sellers
channel: email
style: formal
tags: resubmit documents, verification documents, unclear ID, document rejected, ሰነድ እንደገና ማስገባት, መታወቂያ
related: sel-docs-resubmit, sel-verification-pending, sel-verification-rejected

## Subject (EN)
Action needed: please resubmit your verification documents — case {{ticket_id}}

## Subject (AM)
እርምጃ ያስፈልጋል፦ እባክዎ የማረጋገጫ ሰነዶችዎን እንደገና ያስገቡ — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{customer_name}},

Thank you for submitting your seller application to Byfluence. To continue reviewing it, we need you to resubmit the following:

[list exactly what Seller Operations requested, one item per line]

When resubmitting, please make sure that:
- Each document is clear, well lit and fully readable, with all four corners visible
- The document is valid (not expired)
- The name on the document matches the name on your Byfluence account

Please upload the documents through the verification section of your Byfluence seller account, or as instructed by our team. For your security, please do not send identity documents through public chats or social media comments.

Your application will remain pending until we receive and review the updated documents. If you have any questions, please reply to this email quoting case number {{ticket_id}}.

Sincerely,
{{support_agent}}
Byfluence Customer Support

## Message (AM)
ውድ {{customer_name}}፣

የሻጭ ማመልከቻዎን ለByfluence ስላስገቡ እናመሰግናለን። ግምገማውን ለመቀጠል የሚከተሉትን እንደገና እንዲያስገቡልን እንጠይቃለን፦

[ሻጭ ኦፕሬሽንስ የጠየቀውን በትክክል፣ እያንዳንዱን በአንድ መስመር እዚህ ይዘርዝሩ]

ሰነዶቹን እንደገና ሲያስገቡ እባክዎ የሚከተሉትን ያረጋግጡ፦
- እያንዳንዱ ሰነድ ግልጽ፣ በቂ ብርሃን ያለውና ሙሉ በሙሉ የሚነበብ መሆኑን፣ አራቱም ጠርዞች እንደሚታዩ
- ሰነዱ የአገልግሎት ጊዜው ያላለፈበት መሆኑን
- በሰነዱ ላይ ያለው ስም በByfluence መለያዎ ላይ ካለው ስም ጋር አንድ መሆኑን

እባክዎ ሰነዶቹን በByfluence የሻጭ መለያዎ የማረጋገጫ ክፍል በኩል፣ ወይም ቡድናችን በሚሰጥዎ መመሪያ መሠረት ይጫኑ። ለደህንነትዎ ሲባል የማንነት ሰነዶችን በግልጽ ቻቶች ወይም በማህበራዊ ሚዲያ አስተያየቶች ላይ አይላኩ።

የተስተካከሉትን ሰነዶች ተቀብለን እስክንገመግም ድረስ ማመልከቻዎ በመጠባበቅ ላይ ይቆያል። ማንኛውም ጥያቄ ካለዎት፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን ጠቅሰው ለዚህ ኢሜይል ምላሽ ይስጡ።

ከአክብሮት ሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** Seller Operations has asked for clearer, missing or updated verification documents.

**Fill in:** Replace the bracketed line with the exact items Seller Operations listed. Required document types are **not yet confirmed** platform-wide — never guess or add documents yourself.

**Check:** Confirm with Seller Operations which upload method is approved. If the seller account has no upload option, adjust the sentence to the approved channel only.

**Do NOT:** ask for passwords, OTP codes, bank PINs or card numbers; promise approval after resubmission; or give a review time. Never accept documents through a channel your team has not approved for sensitive data.

<!-- template -->
# Listing not approved
id: tpl-listing-rejected
category: sellers
channel: email
style: formal
tags: listing rejected, listing not approved, listing review, moderation, ዝርዝር አልጸደቀም, listing ውድቅ
related: lst-listing-rejected, sel-verification-rejected

## Subject (EN)
Your listing "{{product_name}}" was not approved — case {{ticket_id}}

## Subject (AM)
ያቀረቡት "{{product_name}}" ዝርዝር አልጸደቀም — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{seller_name}},

Thank you for submitting your listing "{{product_name}}" on Byfluence.

After review, we are unable to approve this listing in its current form.

Reason provided by our review team:
[insert the reason exactly as approved by Seller Operations]

If you would like to update the listing and have it reviewed again, or if you believe the decision was made in error, please reply to this email quoting case number {{ticket_id}}, and our team will guide you on the next steps.

Thank you for helping us keep Byfluence a trusted marketplace for buyers and sellers.

Sincerely,
{{support_agent}}
Byfluence Customer Support

## Message (AM)
ውድ {{seller_name}}፣

"{{product_name}}" የተባለውን ዝርዝር (listing) በByfluence ላይ ስላቀረቡ እናመሰግናለን።

ከግምገማ በኋላ፣ ይህንን ዝርዝር አሁን ባለበት ሁኔታ ማጽደቅ እንዳልቻልን በአክብሮት እናሳውቃለን።

የግምገማ ቡድናችን የሰጠው ምክንያት፦
[በሻጭ ኦፕሬሽንስ የጸደቀውን ምክንያት በትክክል እዚህ ያስገቡ]

ዝርዝሩን አስተካክለው እንደገና እንዲገመገም ከፈለጉ፣ ወይም ውሳኔው በስህተት ተሰጥቷል ብለው ካመኑ፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን ጠቅሰው ለዚህ ኢሜይል ምላሽ ይስጡ፤ ቡድናችን ቀጣዮቹን እርምጃዎች ያሳውቅዎታል።

Byfluenceን ለገዢዎችም ለሻጮችም ታማኝ የገበያ ቦታ እንዲሆን ስለሚያግዙን እናመሰግናለን።

ከአክብሮት ሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A seller's listing (consultation, group session or product) was rejected in listing moderation, or the seller asks why a listing is not visible and the dashboard shows it was rejected.

**Fill in:** `{{seller_name}}`, `{{product_name}}` (the listing title), `{{ticket_id}}`, and replace the bracketed line with the moderation reason exactly as recorded. If no shareable reason exists, ask Seller Operations — do not invent one.

**Do NOT:** promise approval after editing, quote listing rules that are not in an approved policy, or mention other sellers' listings. If the rejection relates to suspected counterfeit or prohibited content, coordinate with Trust & Safety before replying.

<!-- template -->
# Withdrawal status update
id: tpl-withdrawal-status
category: sellers
channel: any
style: standard
tags: withdrawal status, payout status, where is my money, seller earnings, ገንዘብ ማውጣት, ክፍያዬ የት ደረሰ
related: out-withdrawal-delayed, out-withdrawal-status

## Message (EN)
Hello {{seller_name}},

Thank you for your message. Here is the current status of your withdrawal request:

- Amount: {{amount}}
- Withdrawal reference: {{transaction_id}}
- Payout method: {{payment_method}}
- Current status: [e.g. Withdrawal Pending / Processing / Completed — as shown in the records]

For your information: earnings first appear in your **Pending Balance** and move to your **Available Balance** once the release conditions for the booking or order are met. Only the Available Balance can be withdrawn.

If you have any further questions, please reply here and mention case {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{seller_name}}፣

ስለ መልዕክትዎ እናመሰግናለን። የገንዘብ ማውጫ ጥያቄዎ የአሁኑ ሁኔታ እንደሚከተለው ነው፦

- መጠን፦ {{amount}}
- የገንዘብ ማውጫ መለያ ቁጥር፦ {{transaction_id}}
- የክፍያ መቀበያ ዘዴ፦ {{payment_method}}
- አሁን ያለበት ሁኔታ፦ [ለምሳሌ በመጠባበቅ ላይ / በሂደት ላይ / ተጠናቋል — በመዝገቡ ላይ እንደሚታየው]

ለመረጃዎ ያህል፦ ገቢዎ በመጀመሪያ በ**በመጠባበቅ ላይ ያለ ቀሪ ሂሳብ (Pending Balance)** ውስጥ ይታያል፤ ለቀጠሮው ወይም ለትዕዛዙ የተቀመጡት የመልቀቂያ ሁኔታዎች ሲሟሉ ወደ **ሊወጣ የሚችል ቀሪ ሂሳብ (Available Balance)** ይዛወራል። ማውጣት የሚቻለው Available Balance ውስጥ ያለውን ብቻ ነው።

ተጨማሪ ጥያቄ ካለዎት፣ እባክዎ የጉዳይ ቁጥር {{ticket_id}}ን ጠቅሰው እዚሁ ይመልሱልን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A seller asks about the status of a withdrawal they requested, and you can see the status in the admin dashboard (or Payments & Finance has told you).

**Fill in:** `{{amount}}`, `{{transaction_id}}` (the withdrawal reference), `{{payment_method}}` (payout method), `{{ticket_id}}`, and replace the bracketed status with the **exact** status from the records. Remove the Pending/Available explanation if the seller did not ask about balances.

**Do NOT promise:** a payout date, a processing time, or that "it will reach your account today". Payout methods, minimums and timelines are **not confirmed**. Never ask for the seller's mobile-money PIN or bank password. If the withdrawal looks stuck, use *tpl-withdrawal-delayed* and escalate to Payments & Finance.

<!-- template -->
# Withdrawal delayed
id: tpl-withdrawal-delayed
category: sellers
channel: any
style: standard
tags: withdrawal delayed, payout late, money not received, withdrawal stuck, ገንዘቤ አልደረሰም, ክፍያ ዘገየ
related: out-withdrawal-delayed, out-withdrawal-status

## Message (EN)
Hello {{seller_name}},

I am sorry that your withdrawal of {{amount}} (reference {{transaction_id}}) to {{payment_method}} has not reached you yet. I understand how important it is to receive your earnings.

I have escalated your case to our Payments & Finance team so they can check the status of the payout. Your case number is {{ticket_id}}.

To help them, please confirm that the payout account details saved in your Byfluence seller account are correct (for example, the account name and number or mobile-money number). Please do not send us any PIN, password or verification code — we will never ask for them.

We will update you by {{follow_up_time}}. Thank you for your patience.

Best regards,
{{support_agent}}
Byfluence Support

## Message (AM)
ሰላም {{seller_name}}፣

ወደ {{payment_method}} ያቀረቡት የ{{amount}} የገንዘብ ማውጫ ጥያቄ (መለያ ቁጥር {{transaction_id}}) እስካሁን ስላልደረሰዎት ይቅርታ እንጠይቃለን። ገቢዎን በወቅቱ ማግኘት ምን ያህል አስፈላጊ እንደሆነ እንረዳለን።

የክፍያውን ሁኔታ እንዲያጣሩ ጉዳይዎን ለክፍያ እና ፋይናንስ ቡድናችን አስተላልፌዋለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ቡድኑን ለማገዝ፣ እባክዎ በByfluence የሻጭ መለያዎ ላይ የተቀመጠው የክፍያ መቀበያ መረጃ (ለምሳሌ የሂሳብ ስም እና ቁጥር ወይም የሞባይል ገንዘብ ቁጥር) ትክክል መሆኑን ያረጋግጡልን። እባክዎ ማንኛውንም ፒን፣ የይለፍ ቃል ወይም የማረጋገጫ ኮድ አይላኩልን — በፍጹም አንጠይቅዎትም።

እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A seller says a withdrawal is taking longer than expected or shows "completed" but the money has not arrived.

**Before sending:** Check the withdrawal record. If the amount was never in the **Available Balance** (still pending, disputed or refunded), explain that instead with *tpl-withdrawal-status*.

**Fill in:** `{{amount}}`, `{{transaction_id}}`, `{{payment_method}}`, `{{ticket_id}}`, `{{follow_up_time}}`.

**Do NOT promise:** a payout date or that the money "will arrive tomorrow". Do not confirm the payout failed or succeeded until Payments & Finance confirms. If the seller reports that payout details were changed without their knowledge, treat it as possible account compromise → Trust & Safety, High priority.

<!-- template -->
# Seller account suspension enquiry response
id: tpl-seller-suspension-notice
category: sellers
channel: email
style: formal
tags: seller suspended, account suspended, account restricted, cannot sell, መለያዬ ታግዷል, የሻጭ መለያ እገዳ
related: sel-account-suspended, sel-verification-rejected

## Subject (EN)
Regarding the status of your Byfluence seller account — case {{ticket_id}}

## Subject (AM)
የByfluence የሻጭ መለያዎን ሁኔታ በተመለከተ — የጉዳይ ቁጥር {{ticket_id}}

## Message (EN)
Dear {{seller_name}},

Thank you for contacting us about the status of your seller account.

We can confirm that your seller account is currently suspended. While it is suspended, you may not be able to receive new bookings or orders, or to make changes to your listings.

To protect the fairness and security of the marketplace, we are not able to share all details of an ongoing review. If you have information that you believe is relevant — for example, an explanation or supporting documents — please reply to this email, and our Seller Operations team will take it into account.

Your case number is {{ticket_id}}. We will contact you with an update by {{follow_up_time}}.

Thank you for your understanding.

Sincerely,
{{support_agent}}
Byfluence Customer Support

## Message (AM)
ውድ {{seller_name}}፣

የሻጭ መለያዎን ሁኔታ በተመለከተ ስላነጋገሩን እናመሰግናለን።

የሻጭ መለያዎ በአሁኑ ጊዜ መታገዱን እናረጋግጣለን። መለያዎ ታግዶ በሚቆይበት ጊዜ አዳዲስ ቀጠሮዎችን ወይም ትዕዛዞችን መቀበል፣ ወይም ዝርዝሮችዎን ማስተካከል ላይችሉ ይችላሉ።

የገበያ ቦታውን ፍትሃዊነትና ደህንነት ለመጠበቅ ሲባል፣ በሂደት ላይ ያለን ግምገማ ዝርዝር በሙሉ ልናጋራ አንችልም። ጉዳዩን ይመለከታል ብለው የሚያምኑት መረጃ ካለዎት — ለምሳሌ ማብራሪያ ወይም ደጋፊ ሰነዶች — እባክዎ ለዚህ ኢሜይል ምላሽ ይስጡ፤ የሻጭ ኦፕሬሽንስ ቡድናችን ከግምት ውስጥ ያስገባዋል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። እስከ {{follow_up_time}} ድረስ መረጃ ይዘን እናገኝዎታለን።

ስለ ግንዛቤዎ እናመሰግናለን።

ከአክብሮት ሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** A seller asks why they cannot sell or why their account is restricted, and the admin dashboard shows operational status **Suspended**. (Verification status is separate — a seller can be Verified but Suspended.)

**Before sending:** Ask Seller Operations / Trust & Safety what may be shared. If they approved a specific reason, you may add one factual sentence after the first paragraph.

**Fill in:** `{{seller_name}}`, `{{ticket_id}}`, `{{follow_up_time}}`.

**Do NOT:** reveal who reported the seller, buyer details, internal fraud signals or evidence; promise reinstatement or a review end date; or describe an appeal process — appeal rules are not confirmed. If the seller has confirmed upcoming bookings, flag this internally so affected buyers can be handled; do not tell the seller what will happen to those bookings. For **Banned** accounts, escalate to Senior Support — do not use this template.

<!-- template -->
# Support contacting a seller about a buyer issue
id: tpl-seller-contact-request
category: sellers
channel: any
style: formal
tags: contact seller, seller response needed, buyer complaint, seller statement, ሻጩን ማነጋገር, የገዢ ቅሬታ
related: con-seller-no-show, phy-damaged-product, phy-delivery-delay

## Message (EN)
Dear {{seller_name}},

This is {{support_agent}} from Byfluence Support. We are contacting you regarding booking {{consultation_id}} scheduled for {{booking_date}} at {{booking_time}}.

The buyer has reported the following issue: [short, neutral description of the reported issue].

To help us resolve this fairly for both sides, please reply by {{follow_up_time}} with:
1. Your account of what happened
2. Any supporting evidence you have (for example, screenshots, messages or meeting details)
3. Any solution you would like to propose

Please reply through this channel so that all information is recorded under case number {{ticket_id}}.

Thank you for your cooperation.

Sincerely,
{{support_agent}}
Byfluence Customer Support

## Message (AM)
ውድ {{seller_name}}፣

እኔ {{support_agent}} ከByfluence የደንበኞች ድጋፍ ነኝ። {{booking_date}} በ{{booking_time}} የተያዘውን ቀጠሮ ቁጥር {{consultation_id}}ን በተመለከተ ነው የምናገኝዎት።

ገዢው የሚከተለውን ችግር አሳውቀዋል፦ [የቀረበውን ችግር በአጭሩና ያለ አድልዎ እዚህ ይግለጹ]።

ጉዳዩን ለሁለቱም ወገኖች በፍትሃዊነት ለመፍታት እንዲረዳን፣ እባክዎ እስከ {{follow_up_time}} ድረስ የሚከተሉትን ይላኩልን፦
1. የተፈጠረውን ነገር በእርስዎ በኩል ያለውን ማብራሪያ
2. ያለዎትን ማንኛውንም ደጋፊ ማስረጃ (ለምሳሌ ስክሪንሾቶች፣ መልዕክቶች ወይም የስብሰባ መረጃ)
3. ሊያቀርቡት የሚፈልጉት መፍትሄ ካለ

ሁሉም መረጃ በጉዳይ ቁጥር {{ticket_id}} ስር እንዲመዘገብ፣ እባክዎ በዚሁ መስመር ምላሽ ይስጡ።

ስለ ትብብርዎ እናመሰግናለን።

ከአክብሮት ሰላምታ ጋር፣
{{support_agent}}
Byfluence የደንበኞች ድጋፍ

## Usage Notes
**When to use:** You need the seller's side of a buyer complaint (no-show, missing link, quality complaint, damaged/wrong item, delivery problem). For calls, use *tpl-seller-contact-request-phone*.

**Fill in:** For **product orders**, replace "booking {{consultation_id}} scheduled for {{booking_date}} at {{booking_time}}" with "order {{order_id}} for {{product_name}}" (AM: "የትዕዛዝ ቁጥር {{order_id}} ({{product_name}})"). Replace the bracketed line with a short, neutral summary — facts only, no accusation.

**Privacy:** Share only what the seller needs to respond. Do not share the buyer's phone number, email, address or payment details unless an approved process requires it.

**Do NOT:** threaten penalties, suspension or deductions from earnings; promise the seller any outcome; or tell the seller what the buyer has been promised. If the seller does not respond by `{{follow_up_time}}`, follow your escalation SOP (Senior Support / Seller Operations).

<!-- template -->
# Support contacting a seller about a buyer issue (phone script)
id: tpl-seller-contact-request-phone
category: sellers
channel: phone
style: formal
tags: call seller, phone script, seller response needed, buyer complaint, ሻጩን መደወል
related: con-seller-no-show, phy-damaged-product

## Message (EN)
"Hello, good morning / good afternoon. May I please speak with {{seller_name}}?"

(Wait for confirmation that you are speaking to the right person.)

"Thank you. My name is {{support_agent}}, and I am calling from Byfluence Support. Is now a good time to talk for a moment?"

(If not: "No problem. When would be a better time for me to call you back?" — note the time and end the call politely.)

"I am calling about booking {{consultation_id}} on {{booking_date}} at {{booking_time}}. The buyer has contacted us about an issue with this booking, and we would like to hear your side so that we can handle it fairly."

(Briefly and neutrally describe the reported issue. Do not accuse.)

"Could you please tell me what happened from your side?"

(Listen without interrupting. Take notes. Ask only clarifying questions.)

"Thank you for explaining. Do you have anything that could support this — for example, screenshots, messages or meeting details? If so, please send them through {{support_channel}} and mention case number {{ticket_id}}."

"Is there any solution you would like to propose for the buyer?"

"Thank you for your time, {{seller_name}}. We will review all the information and get back to you if we need anything else. Have a good day."

## Message (AM)
"ሃሎ፣ ጤና ይስጥልኝ። {{seller_name}}ን ማነጋገር እችላለሁ?"

(ትክክለኛውን ሰው እያነጋገሩ መሆንዎን ያረጋግጡ።)

"አመሰግናለሁ። ስሜ {{support_agent}} ይባላል፤ የምደውለው ከByfluence የደንበኞች ድጋፍ ነው። ለጥቂት ደቂቃ ለመነጋገር አሁን ይመችዎታል?"

(የማይመቻቸው ከሆነ፦ "ችግር የለም። መቼ ብደውልልዎ ይሻልዎታል?" — ሰዓቱን መዝግበው ጥሪውን በትህትና ይዝጉ።)

"የምደውለው {{booking_date}} በ{{booking_time}} የተያዘውን ቀጠሮ ቁጥር {{consultation_id}}ን በተመለከተ ነው። ገዢው ስለዚህ ቀጠሮ ችግር እንዳለ አሳውቀውናል፤ ጉዳዩን በፍትሃዊነት ለማየት የእርስዎንም ሃሳብ መስማት እንፈልጋለን።"

(የቀረበውን ችግር በአጭሩና ያለ አድልዎ ይግለጹ። አይክሰሱ።)

"በእርስዎ በኩል የተፈጠረውን ነገር ሊነግሩኝ ይችላሉ?"

(ሳያቋርጡ ያዳምጡ። ማስታወሻ ይያዙ። ለማብራራት የሚረዱ ጥያቄዎችን ብቻ ይጠይቁ።)

"ስላብራሩልኝ እናመሰግናለን። ይህንን የሚደግፍ ነገር አለዎት? ለምሳሌ ስክሪንሾቶች፣ መልዕክቶች ወይም የስብሰባ መረጃ። ካለዎት እባክዎ በ{{support_channel}} በኩል የጉዳይ ቁጥር {{ticket_id}}ን ጠቅሰው ይላኩልን።"

"ለገዢው ሊያቀርቡት የሚፈልጉት መፍትሄ አለ?"

"{{seller_name}}፣ ጊዜዎን ስለሰጡን እናመሰግናለን። ሁሉንም መረጃ ገምግመን ተጨማሪ ነገር ካስፈለገን እናገኝዎታለን። መልካም ቀን ይሁንልዎ።"

## Usage Notes
**When to use:** The case is urgent (e.g. a session is about to start or a buyer is waiting) or the seller has not answered written messages. Speak Amharic by default; switch to English only if the seller prefers.

**Fill in:** For product orders, say "order {{order_id}} for {{product_name}}" instead of the booking details. Text in brackets are instructions for you — do not read them aloud.

**During the call:** Stay neutral and polite even if the seller is defensive. Do not share the buyer's contact details. Do not ask for the seller's password, PIN or codes.

**Do NOT promise or threaten:** no penalties, suspensions or earnings deductions; no promises about what the buyer will receive. After the call, write a short summary of what the seller said in the ticket internal notes.
