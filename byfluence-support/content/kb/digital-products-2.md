<!-- doc -->
# File Won't Open
id: dig-file-wont-open
type: article
category: digital-products
subcategory: file-problems
audience: buyer
priority: low
department: support_l1
features: digital-products
tags: file won't open, can't open pdf, unsupported format, zip file, docx won't open, open on phone, ፋይሉ አይከፈትም, PDF አይከፈትም, መክፈት አልቻልኩም
related: dig-corrupted-file, dig-download-access, dig-incorrect-product, dig-tsg-access-master, dig-not-as-described
templates: tpl-request-screenshot
policy_pending: yes

## Summary
The buyer downloaded a digital product but cannot open it on their phone or computer.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm digital products are live.

Most "won't open" cases are device or app problems, not broken files: the buyer has no app for the format, the file is compressed (ZIP), the download was incomplete, or the phone opened it in the wrong app. If the file is genuinely damaged, follow *dig-corrupted-file*.

Common formats and what is needed:
| Format | What opens it |
|---|---|
| PDF | A PDF reader or most web browsers |
| DOCX / XLSX / PPTX | Microsoft Office apps, Google Docs/Sheets/Slides, or WPS Office |
| ZIP | Must be extracted first (Files app on most phones, or right-click → Extract on a computer) |
| EPUB | An e-book reader app |
| PSD / AI / Figma / Canva links | The design software stated in the listing |
| MP4 / MP3 | Phone video/music player |

## Possible Causes
- No app installed for that format.
- ZIP file not extracted.
- Download incomplete (slow or interrupted connection).
- The phone opens the file with the wrong default app.
- The file needs paid software the buyer doesn't have (should have been stated in the listing).
- The file is corrupted (→ *dig-corrupted-file*).

## Information to Collect
- Product name and file name/format
- Device (Android/iPhone/computer) and the app they tried
- Screenshot of the error message
- File size shown after download (if they can see it)

## Troubleshooting Steps
1. Check the listing for the file format and any software requirements.
2. Ask for the device, app and a screenshot of the error.
3. Guide the buyer:
   - Install or use an app that supports the format (see table).
   - For ZIP files, extract them first.
   - Re-download on a stable connection (Wi-Fi), if their access allows.
   - Try opening on another device or in a browser.
4. If the file still won't open on a suitable app → *dig-corrupted-file*.
5. If the listing did not state that special software is required → note it; this may be a *dig-not-as-described* case.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us. I'm sorry you're having trouble opening {{product_name}}.

This usually happens when the phone or computer doesn't have the right app for the file type. Please try:
1. Check the file type (for example PDF, DOCX or ZIP) and open it with a suitable app — a PDF reader for PDF, or Google Docs/Word for DOCX.
2. If it's a ZIP file, extract (unzip) it first, then open the files inside.
3. If the download was interrupted, download it again on a stable connection.

If it still doesn't open, please send me a screenshot of the error and tell me which device and app you are using.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን። {{product_name}}ን ለመክፈት በመቸገርዎ ይቅርታ እንጠይቃለን።

ይህ ብዙውን ጊዜ የሚያጋጥመው ስልኩ ወይም ኮምፒውተሩ ለፋይሉ አይነት ተስማሚ መተግበሪያ ሲያጣ ነው። እባክዎ የሚከተለውን ይሞክሩ፦
1. የፋይሉን አይነት (ለምሳሌ PDF፣ DOCX ወይም ZIP) ይመልከቱና በተስማሚ መተግበሪያ ይክፈቱት — ለ PDF የ PDF reader፣ ለ DOCX ደግሞ Google Docs ወይም Word።
2. ZIP ፋይል ከሆነ መጀመሪያ ያውጡት (unzip)፣ ከዚያ ውስጡ ያሉትን ፋይሎች ይክፈቱ።
3. ማውረዱ ተቋርጦ ከነበረ፣ በተረጋጋ ኢንተርኔት እንደገና ያውርዱት።

አሁንም ካልተከፈተ፣ እባክዎ የስህተት መልዕክቱን ስክሪንሾት ይላኩልኝ፤ የሚጠቀሙበትን መሳሪያ እና መተግበሪያም ይንገሩኝ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! Open the file with an app for its type (PDF reader for PDF, Docs/Word for DOCX), unzip ZIP files first, and re-download on a stable connection. Still stuck? Send a screenshot + your device/app. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! ፋይሉን ለአይነቱ በሚስማማ መተግበሪያ ይክፈቱ (ለ PDF የ PDF reader፣ ለ DOCX Docs/Word)፣ ZIP ከሆነ መጀመሪያ ያውጡት፣ በተረጋጋ ኢንተርኔትም እንደገና ያውርዱ። ካልሰራ ስክሪንሾት + መሳሪያ/መተግበሪያ ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are checking the file for {{product_name}} with the seller to make sure it is working correctly. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የ{{product_name}} ፋይል በትክክል እየሰራ መሆኑን ከሻጩ ጋር እያጣራን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- File fails to open on suitable apps/devices → *dig-corrupted-file* (**Seller Operations**).
- Re-download not possible because of limits → *dig-access-restricted-limit*.
- Listing failed to mention required paid software → **Senior Support** (possible not-as-described).

## Resolution Procedure
1. Confirm the buyer can open and use the file.
2. Record cause (missing app, ZIP, incomplete download, corrupted file).

## Policy Pending Approval
- Decide whether sellers must state file format and required software on every digital listing.

## Internal Notes
- Ask for the device first — iPhone and Android handle ZIP and DOCX differently.
- Do not ask the buyer to send you the file; do not open customer-sent files on your work computer without approved security procedures.

<!-- doc -->
# Corrupted or Incomplete File
id: dig-corrupted-file
type: article
category: digital-products
subcategory: file-problems
audience: buyer
priority: medium
department: seller_ops
features: digital-products
tags: corrupted file, broken file, incomplete file, missing pages, damaged zip, file error, ፋይሉ ተበላሽቷል, ያልተሟላ ፋይል, ገጾች ጎድለዋል
related: dig-file-wont-open, dig-incorrect-product, dig-not-as-described, dig-refunds, dig-tsg-access-master
templates: tpl-request-screenshot, tpl-request-order-details
policy_pending: yes

## Summary
The buyer's digital product is damaged or incomplete: it shows errors when opened, pages or lessons are missing, a ZIP archive is broken, or the file is much smaller than expected.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm digital products are live.

First rule out device/app problems (*dig-file-wont-open*). If the file is genuinely damaged or incomplete, the cause is either the seller's upload or a platform storage/download error. The seller is responsible for providing a working file.

## Possible Causes
- Seller uploaded a damaged or partial file.
- Seller uploaded the wrong version (draft, missing chapters).
- Upload/storage error on the platform.
- Download interrupted, saving a partial file.

## Information to Collect
- Product name, purchase date, account email/phone
- Screenshot of the error or of missing content (e.g., blank pages, page count)
- File size shown on the buyer's device
- Device and app used
- Whether they re-downloaded and got the same result

## Troubleshooting Steps
1. Confirm basic steps were tried (correct app, re-download on stable connection).
2. If you have authorized access, check the file details in the admin dashboard (size, upload date) and whether other buyers reported the same problem.
3. **Problem on all downloads / other buyers too** → seller file problem: **Seller Operations** asks the seller to upload a working file.
4. **Only this buyer, file in storage looks fine** → possible download problem: **Technical / Engineering**.
5. Once a fixed file is uploaded, ask the buyer to download again through Byfluence (reset access if needed).
6. If the seller cannot fix it → *dig-refunds*.
7. Never send a file manually.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know, and I'm sorry that {{product_name}} seems to be damaged or incomplete.

To check it, please send:
1. A screenshot of the error or the missing part
2. The device and app you used
3. Whether you tried downloading it again

We will check the file with the seller. Once a working version is available, you will be able to download it again from your purchase history.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን፤ {{product_name}} የተበላሸ ወይም ያልተሟላ መስሎ ስለታየዎት ይቅርታ እንጠይቃለን።

ለማጣራት እባክዎ የሚከተሉትን ይላኩ፦
1. የስህተቱን ወይም የጎደለውን ክፍል ስክሪንሾት
2. የተጠቀሙበትን መሳሪያ እና መተግበሪያ
3. እንደገና ለማውረድ ሞክረው እንደሆነ

ፋይሉን ከሻጩ ጋር እናጣራለን። የሚሰራ ቅጂ ሲገኝ ከግዢ ታሪክዎ እንደገና ማውረድ ይችላሉ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry {{product_name}} seems damaged. Please send a screenshot of the error/missing part, your device and app, and whether you re-downloaded. We'll check with the seller. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ {{product_name}} የተበላሸ ስለመሰለ ይቅርታ። እባክዎ የስህተቱን/የጎደለውን ስክሪንሾት፣ መሳሪያና መተግበሪያ፣ እንደገና አውርደው እንደሆነም ይላኩ። ከሻጩ ጋር እናጣራለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have asked the seller to check and replace the file for {{product_name}}. We will contact you again by {{follow_up_time}}, or as soon as a working version is available.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የ{{product_name}} ፋይልን አጣርቶ እንዲተካ ሻጩን ጠይቀናል። እስከ {{follow_up_time}} ድረስ፣ ወይም የሚሰራ ቅጂ እንደተገኘ ወዲያውኑ እናገኝዎታለን።

## Escalation Conditions
- Seller file faulty → **Seller Operations**.
- Platform storage/download error → **Technical / Engineering**.
- Seller does not fix the file → **Senior Support** for refund consideration (*dig-refunds*).

## Resolution Procedure
1. Confirm the buyer has downloaded and opened a working, complete file, or that a refund decision was made.
2. Record the cause (seller upload, platform, download) and whether other buyers were affected.

## Policy Pending Approval
- Define how quickly sellers must replace faulty files and what happens if they don't.
- Decide whether buyers of a faulty file are automatically notified when a fixed version is uploaded.

## Internal Notes
- If several buyers report the same product, consider asking Seller Operations to pause the listing until fixed.
- File size is a quick clue: a 20-page e-book that is a few KB is likely incomplete.

<!-- doc -->
# Received the Wrong File or Product
id: dig-incorrect-product
type: article
category: digital-products
subcategory: file-problems
audience: buyer
priority: medium
department: seller_ops
features: digital-products
tags: wrong file, wrong ebook, different product, wrong language, wrong version, got another file, የተሳሳተ ፋይል, ሌላ ፋይል ደረሰኝ, የተለየ ምርት
related: dig-corrupted-file, dig-not-as-described, dig-refunds, dig-missing-download-link, dig-tsg-access-master
templates: tpl-request-screenshot, tpl-wrong-item-ack
policy_pending: yes

## Summary
The buyer downloaded a digital product but the file is a different product, version, language or edition from what they bought.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm digital products are live.

Examples: bought an Amharic guide, received the English version; bought "Template Pack 2", received "Pack 1"; the file is unrelated to the listing. Usually a seller upload mistake. If the content is the right product but lower quality than described, use *dig-not-as-described*.

## Possible Causes
- Seller uploaded the wrong file to the listing.
- Seller sells several versions and attached the wrong one.
- Platform error linked the wrong file to the purchase.
- The buyer bought a different listing than they intended (check the order).

## Information to Collect
- Product name and purchase date
- Screenshot of the listing as bought
- Screenshot of the file received (title page, file name)
- What the buyer expected

## Troubleshooting Steps
1. Check the purchase: which listing did the buyer actually buy?
2. Compare the listing with the file received.
3. **Buyer bought a different listing by mistake** → explain kindly; refund question → *dig-refunds*.
4. **Wrong file attached by the seller** → **Seller Operations** to have the seller upload the correct file; check if other buyers were affected.
5. **File belongs to another seller's product** → **Technical / Engineering** (platform mapping error) — urgent, as it may expose another seller's content.
6. After correction, ask the buyer to download again through Byfluence.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know, and I'm sorry you received the wrong file for {{product_name}}.

Please send a screenshot of the file you received (for example its title page or file name) and tell me what you expected to receive. We will check with the seller so that the correct file is made available in your purchase history.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላሳወቁን እናመሰግናለን፤ ለ{{product_name}} የተሳሳተ ፋይል ስለደረሰዎት ይቅርታ እንጠይቃለን።

እባክዎ የደረሰዎትን ፋይል (ለምሳሌ የመጀመሪያ ገጹን ወይም የፋይሉን ስም) ስክሪንሾት ይላኩ፤ እንዲደርስዎ የጠበቁትንም ይንገሩኝ። ትክክለኛው ፋይል በግዢ ታሪክዎ ውስጥ እንዲቀርብ ከሻጩ ጋር እናጣራለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry you got the wrong file. Please send a screenshot of what you received and tell me what you expected. We'll get the seller to make the correct file available. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የተሳሳተ ፋይል ስለደረሰዎት ይቅርታ። እባክዎ የደረሰዎትን ስክሪንሾት ይላኩ፤ የጠበቁትንም ይንገሩኝ። ሻጩ ትክክለኛውን ፋይል እንዲያቀርብ እናደርጋለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have asked the seller to upload the correct file for {{product_name}}. We will let you know when it is available, and by {{follow_up_time}} at the latest with an update.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለ{{product_name}} ትክክለኛውን ፋይል እንዲጭን ሻጩን ጠይቀናል። ሲገኝ እናሳውቅዎታለን፤ በማንኛውም ሁኔታ እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

## Escalation Conditions
- Seller uploaded the wrong file → **Seller Operations**.
- File from another seller's product delivered → **Technical / Engineering** (High) and inform **Trust & Safety** if content was exposed.
- Seller cannot provide the correct file → **Senior Support** (*dig-refunds*).

## Resolution Procedure
1. Confirm the buyer has the correct file.
2. Record cause and whether other buyers were affected.

## Policy Pending Approval
- Decide whether buyers may keep the wrong file when it is another paid product (and how sellers are compensated if a platform error caused it).
- Define seller deadlines for correcting wrong uploads.

## Internal Notes
- Do not ask the buyer to delete the wrong file as a condition of help — focus on providing the right one; Trust & Safety decides on platform-error exposure.

<!-- doc -->
# Digital Product Not as Described
id: dig-not-as-described
type: article
category: digital-products
subcategory: digital-disputes
audience: buyer
priority: medium
department: support_l2
features: digital-products
tags: not as described, misleading digital product, poor quality ebook, fewer pages, course incomplete, template not editable, እንደተገለጸው አይደለም, ጥራቱ ዝቅተኛ, አሳሳች
related: dig-refunds, dig-corrupted-file, dig-incorrect-product, dig-copyright-complaint, ref-evidence-collection, ref-digital-refunds
templates: tpl-request-screenshot, tpl-refund-request-ack
policy_pending: yes

## Summary
The buyer says the digital product they received does not match its description (content, length, quality, format, language or features).

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm digital products are live.

Digital product disputes are hard because the buyer keeps the file after downloading. Examples:
- Listing says "200 pages", file has 40.
- Listing says "editable Canva template", buyer receives a flat image/PDF.
- Course promises 10 modules, only 3 are available.
- E-book is machine-translated or copied from free sources.
- Content is in a different language than listed.

Separate **objective mismatches** (format, length, language, missing content) from **subjective dissatisfaction** ("not useful", "too basic"). Objective mismatches are stronger complaints; subjective ones depend on refund policy.

## Possible Causes
- Exaggerated or inaccurate listing description.
- Seller uploaded an incomplete version.
- Listing was edited after the purchase.
- Buyer misunderstood the description.
- Content copied from others (→ *dig-copyright-complaint*).

## Information to Collect
- Product name, purchase date
- Screenshot of the listing claims (as close to purchase time as possible)
- Screenshots showing the mismatch (page count, format, missing modules)
- What the buyer wants (fix, replacement, refund) — recorded, not promised

## Troubleshooting Steps
1. Snapshot the current listing; check if it was edited after purchase (if history is available).
2. Compare listing claims with the buyer's evidence. Classify objective vs subjective.
3. Contact the seller with the evidence; ask for a response or a corrected file.
4. If the seller fixes it (e.g., uploads missing modules), let the buyer download through Byfluence.
5. If not resolved, route to **Senior Support** for a decision; refunds via *dig-refunds*.
6. If the content appears copied or pirated → **Trust & Safety**.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your feedback about {{product_name}}. I'm sorry it did not match what you expected from the description.

To review this, please send:
1. Screenshots of the parts of the listing that don't match
2. Screenshots from the file showing the difference (for example missing sections, format or page count)

We will share this with the seller and review your case. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ {{product_name}} አስተያየትዎን ስላጋሩን እናመሰግናለን። ከመግለጫው እንደጠበቁት ባለመሆኑ ይቅርታ እንጠይቃለን።

ጉዳዩን ለመገምገም እባክዎ የሚከተሉትን ይላኩ፦
1. የማይመሳሰሉትን የዝርዝሩን (listing) ክፍሎች የሚያሳዩ ስክሪንሾቶች
2. ልዩነቱን የሚያሳዩ ከፋይሉ የተወሰዱ ስክሪንሾቶች (ለምሳሌ የጎደሉ ክፍሎች፣ የፋይል አይነት ወይም የገጽ ብዛት)

ይህንን ለሻጩ አጋርተን ጉዳይዎን እንገመግማለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry {{product_name}} didn't match the description. Please send screenshots of the listing claims and of the file showing the difference. We'll review with the seller. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ {{product_name}} ከመግለጫው ጋር ባለመመሳሰሉ ይቅርታ። እባክዎ የዝርዝሩን እና ልዩነቱን የሚያሳዩ የፋይሉን ስክሪንሾቶች ይላኩ። ከሻጩ ጋር እንገመግማለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have shared your evidence with the seller and your case is under review. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ያቀረቡትን ማስረጃ ለሻጩ አጋርተናል፤ ጉዳይዎ በግምገማ ላይ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Seller disputes the claim or does not respond → **Senior Support / Supervisor**.
- Listing appears deliberately misleading, or many buyers complain → **Seller Operations** (listing review); **Trust & Safety** if fraudulent.
- Content appears copied/pirated → **Trust & Safety**.
- Refund requested → *dig-refunds*.

## Resolution Procedure
1. Resolve when the seller provides the missing content, or an authorized refund/decline decision is communicated.
2. Record listing snapshot, evidence, classification (objective/subjective), seller response and decision.

## Policy Pending Approval
- Define what counts as "not as described" for digital products, and the remedies.
- Decide whether listing edit history is kept and visible to support.
- Decide whether sellers must provide previews (sample pages) for digital products.

## Internal Notes
- Always snapshot the listing on first contact — it may change.
- Avoid judging content quality yourself; focus on whether the listing claims are met.

<!-- doc -->
# Digital Product Refund Requests
id: dig-refunds
type: article
category: digital-products
subcategory: digital-disputes
audience: buyer
priority: medium
department: payments
features: digital-products, refunds
tags: refund digital product, money back ebook, refund course, refund template, digital refund policy, ገንዘቤ ይመለስ, ዲጂታል ተመላሽ ገንዘብ, ተመላሽ
related: ref-digital-refunds, dig-not-as-described, dig-corrupted-file, dig-duplicate-payment, dig-missing-download-link, ref-evidence-collection
templates: tpl-refund-request-ack, tpl-request-order-details
policy_pending: yes

## Summary
A buyer asks for a refund for a digital product, or asks about the status of a digital refund.

## Issue Description
> [!WARNING] **Planned features.** Digital products are planned and refund processing is **unconfirmed**. Check the **Feature Status** page before discussing refunds as an available process.

Refund eligibility for digital products is **not confirmed**. Digital products are special because the buyer can keep a copy after downloading, so many marketplaces limit refunds after download. Byfluence has **not** set such a rule yet — do not tell buyers "digital products are non-refundable" or "you can get a refund" until policy exists.

Typical reasons, from strongest to weakest:
1. Paid but never received access (*dig-missing-download-link*).
2. Duplicate payment (*dig-duplicate-payment*).
3. File corrupted/wrong and the seller cannot fix it.
4. Not as described (objective mismatch).
5. Change of mind / not useful.

## Possible Causes
See the reasons above. Also check for copyright removal of the listing (access lost).

## Information to Collect
- Account email/phone, product name, purchase date
- Transaction reference, payment method and amount
- Refund reason and evidence (screenshots)
- Whether the buyer downloaded/accessed the file (check the access record)

> [!WARNING] Never ask for passwords, OTP codes, PINs or full card numbers.

## Troubleshooting Steps
1. Verify the account and purchase; check the payment status (Refund Pending/Refunded already?).
2. Identify the reason; if it is an access or file problem, try to fix it first through the matching article.
3. Check the access record (downloaded or not) and add it to the case.
4. Collect evidence and the seller's response where relevant.
5. Submit to the authorized reviewer (Senior Support → Payments) and send *tpl-refund-request-ack*.
6. Communicate the decision once made. If approved, Payments processes it, and access may be removed per policy.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us about a refund for {{product_name}}. I'm sorry it hasn't worked out as expected.

I have submitted your refund request for review, together with the details you provided. Refund decisions are made by our authorized team after checking the purchase, the payment and the seller's information. I will update you on the outcome.

If you have screenshots that show the problem, please send them here.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ {{product_name}} ተመላሽ ገንዘብ ስላገኙን እናመሰግናለን። እንደጠበቁት ባለመሆኑ ይቅርታ እንጠይቃለን።

የተመላሽ ገንዘብ ጥያቄዎን ከሰጡን መረጃ ጋር ለግምገማ አስገብቻለሁ። የተመላሽ ገንዘብ ውሳኔዎች የሚሰጡት ግዢውን፣ ክፍያውን እና የሻጩን መረጃ ካጣራ በኋላ ስልጣን ባለው ቡድናችን ነው። ስለ ውጤቱ መረጃ እሰጥዎታለሁ።

ችግሩን የሚያሳዩ ስክሪንሾቶች ካሉዎት እባክዎ እዚህ ይላኩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I've submitted your refund request for {{product_name}} for review by our authorized team and will update you on the outcome. Please send any screenshots of the problem. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለ{{product_name}} ያቀረቡትን የተመላሽ ገንዘብ ጥያቄ ስልጣን ላለው ቡድናችን ለግምገማ አስገብቻለሁ፤ ውጤቱን አሳውቅዎታለሁ። ችግሩን የሚያሳዩ ስክሪንሾቶች ካሉ ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your refund request for {{product_name}} is still under review. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለ{{product_name}} ያቀረቡት የተመላሽ ገንዘብ ጥያቄ አሁንም በግምገማ ላይ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- All refund decisions → **Senior Support / Supervisor** (recommendation) and **Payments & Finance** (processing).
- Chargeback/dispute opened with the payment provider → **Payments & Finance**.
- Repeated refund requests after downloading many products → **Trust & Safety** (possible abuse).
- Policy exceptions or high-value bundles/courses → **Management**.

## Resolution Procedure
1. Resolve when the refund is processed (confirmed by Payments) or declined with an explanation.
2. Record reason, access record (downloaded or not), evidence, decision, approver and amount.

## Policy Pending Approval
- Define digital refund eligibility (e.g., before vs after download, faulty file, not as described).
- Define the time window for digital refund requests.
- Decide whether access is revoked after a refund.
- Define who approves digital refunds and how seller earnings are adjusted.

## Internal Notes
- The access record (downloaded or not) is the most important fact for future policy — always include it.
- Never say "digital products are non-refundable" — that rule has not been approved.

<!-- doc -->
# Copyright or Stolen Content Complaint
id: dig-copyright-complaint
type: article
category: digital-products
subcategory: digital-disputes
audience: both
priority: high
department: trust_safety
features: digital-products
tags: copyright, stolen content, my work is being sold, pirated ebook, plagiarism, intellectual property, የቅጂ መብት, ስራዬ ተሰርቋል, ያለፈቃድ ተሸጧል
related: tns-intellectual-property, dig-unauthorized-sharing, dig-not-as-described, dig-seller-responsibilities, dig-refunds
templates: tpl-request-screenshot
policy_pending: yes

## Summary
Someone reports that a digital product on Byfluence contains their copyrighted work or content copied without permission, or a buyer suspects they bought pirated content.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm digital products are live.

Reporters may be authors, designers, course creators, publishers, other Byfluence sellers or buyers. Copyright complaints can have **legal consequences**, so support does **not** decide whether infringement happened. Support collects a complete report and sends it to **Trust & Safety**, who may involve **Management** for legal matters. A formal copyright complaint procedure is **not yet approved**.

## Possible Causes
- A seller re-sells someone else's e-book, course or templates.
- A seller copies parts of a work (text, images, design elements).
- A seller uses licensed assets beyond their licence (e.g., stock images, fonts).
- Mistaken complaint (content is public domain, licensed, or original).
- Malicious complaint by a competitor.

## Information to Collect
- Reporter's name and contact details, and whether they are the owner or authorized representative
- Link or name of the Byfluence listing(s)
- Description of the original work and evidence of ownership (links to the original publication, creation files, publication date)
- What exactly is copied (whole product, specific pages, images)
- Any previous contact with the seller

## Troubleshooting Steps
1. Thank the reporter and create a ticket; do not discuss the merits.
2. Collect the information above in one message.
3. Snapshot the listing (title, description, preview images, seller).
4. Escalate to **Trust & Safety** with everything. Do not remove, hide or change the listing yourself.
5. If a buyer reports that what they bought appears pirated, collect their purchase details and also escalate to Trust & Safety; refunds follow *dig-refunds* after review.
6. Do not share the reporter's details with the seller unless Trust & Safety approves.
7. If the complaint mentions lawyers, police or court → **Management** via Trust & Safety, Critical.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for reporting this. We take concerns about copyright and stolen content seriously.

To review your report, please send:
1. The link or name of the Byfluence listing you are concerned about
2. Information about your original work (for example a link to where it was first published) and why you believe you own it or are authorized to act for the owner
3. What exactly has been copied

Your report will be reviewed by our specialist team. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ይህንን ስላሳወቁን እናመሰግናለን። የቅጂ መብትን እና የተሰረቀ ይዘትን በተመለከተ የሚቀርቡ ስጋቶችን በቁም ነገር እንመለከታቸዋለን።

ሪፖርትዎን ለመገምገም እባክዎ የሚከተሉትን ይላኩ፦
1. ያሳሰበዎትን የ Byfluence ዝርዝር (listing) ሊንክ ወይም ስም
2. ስለ መጀመሪያው ስራዎ መረጃ (ለምሳሌ መጀመሪያ የታተመበት ሊንክ) እና ባለቤት ወይም የባለቤቱ ወኪል እንደሆኑ የሚያምኑበት ምክንያት
3. በትክክል የተቀዳው ምን እንደሆነ

ሪፖርትዎ በልዩ ቡድናችን ይገመገማል። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for reporting this — we take it seriously. Please send the listing link/name, details of your original work and proof of ownership, and what was copied. Our specialist team will review it. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን — በቁም ነገር እንመለከተዋለን። እባክዎ የዝርዝሩን ሊንክ/ስም፣ የመጀመሪያ ስራዎን መረጃ እና የባለቤትነት ማስረጃ፣ የተቀዳውንም ይላኩ። ልዩ ቡድናችን ይገመግመዋል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your report is being reviewed by our Trust & Safety team. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ሪፖርትዎ በእምነትና ደህንነት (Trust & Safety) ቡድናችን እየተገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every copyright complaint → **Trust & Safety** (High).
- Legal threats, lawyers, police, court orders, publishers/brands → **Management** via Trust & Safety (Critical).
- Seller whose listing was reported contacts support → **Trust & Safety** (do not reveal reporter details).

## Resolution Procedure
1. Resolve after Trust & Safety confirms the outcome and it has been communicated to the reporter (and to affected buyers, if any).
2. Record the reporter, listing snapshot, evidence, Trust & Safety reference and outcome.

## Policy Pending Approval
- Define Byfluence's copyright complaint and counter-notice process, including required information.
- Decide what happens to buyers' access and refunds when a listing is removed for infringement.
- Decide seller penalties for repeated infringement.

## Internal Notes
- Never say "the seller stole your work" or "this is not infringement". Say "your report will be reviewed".
- Keep reporter identity confidential by default.
- Public-domain classics and free resources re-sold with no added value may still breach marketplace rules — let Trust & Safety decide.

<!-- doc -->
# Purchased Content Shared or Resold Without Permission
id: dig-unauthorized-sharing
type: article
category: digital-products
subcategory: digital-disputes
audience: seller
priority: medium
department: trust_safety
features: digital-products
tags: content shared, ebook shared on telegram, resold my product, leaked file, piracy, unauthorized download, ፋይሌ ተጋርቷል, ያለፈቃድ ተሽጧል, ቴሌግራም ላይ ተለቋል
related: dig-copyright-complaint, dig-access-restricted-limit, dig-seller-responsibilities, tns-intellectual-property, dig-seller-upload-guide
templates: tpl-request-screenshot
policy_pending: yes

## Summary
A seller reports that a digital product they sell on Byfluence has been shared, leaked or resold without permission (e.g., posted in Telegram groups or resold by another seller).

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm digital products are live.

Unauthorized sharing is common for e-books, templates and courses, especially in Telegram channels. Byfluence can act on content **inside Byfluence** (e.g., another seller re-listing it, a buyer account abusing downloads). For content shared **outside Byfluence** (Telegram, websites), Byfluence's role is limited — support must not promise takedowns on other platforms.

## Possible Causes
- A buyer shared the downloaded file with others.
- Another Byfluence seller is re-selling the product.
- The file was leaked before it was listed on Byfluence (from another platform).
- A platform weakness allowed downloads without purchase (security issue).

## Information to Collect
- Seller's listing name/link
- Where the content was found (Byfluence listing link, Telegram channel/group name, website) and screenshots
- When they noticed it
- Any identifying marks in the shared file (watermark, buyer name, unique code) if their product uses them

## Troubleshooting Steps
1. Thank the seller and record the report.
2. **Re-sold on Byfluence by another seller** → treat as *dig-copyright-complaint*; escalate to **Trust & Safety**.
3. **Shared outside Byfluence** → record the evidence; escalate to **Trust & Safety** to check whether a Byfluence account is the source (download patterns). Explain honestly that Byfluence cannot remove content from other platforms; the seller may use those platforms' reporting tools.
4. **Suspected download without purchase (security issue)** → **Technical / Engineering** and **Trust & Safety**, High.
5. Do not reveal buyer identities to the seller.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for reporting this, and I'm sorry to hear your product may have been shared without permission.

Please send me:
1. Where you found the content (a Byfluence listing link, or the name of the Telegram group or website) with screenshots
2. When you noticed it
3. Any marks in the shared file that could identify where it came from, if your product has them

Our Trust & Safety team will review what can be done on Byfluence. For content on other platforms such as Telegram, those platforms' own reporting tools are usually the way to request removal.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ይህንን ስላሳወቁን እናመሰግናለን፤ ምርትዎ ያለፈቃድ ተጋርቶ ሊሆን እንደሚችል በመስማታችን እናዝናለን።

እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ይዘቱን ያገኙበትን ቦታ (የ Byfluence ዝርዝር ሊንክ፣ ወይም የቴሌግራም ቡድኑን ወይም የድረ-ገጹን ስም) ከስክሪንሾቶች ጋር
2. መቼ እንዳስተዋሉት
3. ምርትዎ ካለው፣ የተጋራው ፋይል ከየት እንደመጣ ሊያሳዩ የሚችሉ ምልክቶች

የእምነትና ደህንነት (Trust & Safety) ቡድናችን በ Byfluence ላይ ምን ማድረግ እንደሚቻል ይገመግማል። እንደ ቴሌግራም ባሉ ሌሎች መድረኮች ላይ ያለ ይዘትን ለማስወገድ ብዙውን ጊዜ የእነዚያ መድረኮች የሪፖርት ማድረጊያ መንገዶች ይጠቅማሉ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry to hear this. Please send where you found it (link or Telegram group/website name) with screenshots and when you noticed. Trust & Safety will review what can be done on Byfluence. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይህን በመስማታችን እናዝናለን። እባክዎ ያገኙበትን ቦታ (ሊንክ ወይም የቴሌግራም ቡድን/የድረ-ገጽ ስም) ከስክሪንሾት ጋር እና መቼ እንዳስተዋሉት ይላኩ። Trust & Safety በ Byfluence ላይ ምን እንደሚቻል ይገመግማል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our Trust & Safety team is reviewing your report. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የእምነትና ደህንነት ቡድናችን ሪፖርትዎን እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- All reports → **Trust & Safety**.
- Evidence that files can be downloaded without purchase → **Technical / Engineering** + **Trust & Safety** (High).
- Seller requests legal action → **Management** via Trust & Safety.

## Resolution Procedure
1. Resolve after Trust & Safety communicates the outcome (e.g., listing removed, buyer account restricted, no action possible).
2. Record evidence, source location, and actions taken.

## Policy Pending Approval
- Define buyer usage rights for digital products (personal use, no redistribution) and how they are shown at purchase.
- Decide on consequences for buyers who share purchased content.
- Decide whether Byfluence will offer protections such as watermarking or per-buyer download links.
- Decide whether Byfluence assists sellers with takedown requests on other platforms.

## Internal Notes
- Never promise to remove content from Telegram or other platforms.
- Never tell the seller which buyer may have leaked the file.

<!-- doc -->
# Seller: Uploading and Pricing Digital Products
id: dig-seller-upload-guide
type: article
category: digital-products
subcategory: digital-sellers
audience: seller
priority: low
department: seller_ops
features: digital-products
tags: upload ebook, sell digital product, how to sell templates, digital listing, file upload, price digital product, ዲጂታል ምርት መጫን, ኢ-መጽሐፍ መሸጥ, ፋይል መጫን
related: dig-seller-responsibilities, lst-create-listing, dig-corrupted-file, dig-copyright-complaint, dig-unauthorized-sharing
templates: tpl-request-screenshot
policy_pending: yes

## Summary
A seller asks how to upload a digital product, describe it, and set its price on Byfluence.

## Overview
> [!WARNING] **Planned feature.** Digital product selling is planned. Check the **Feature Status** page before explaining uploading as a live feature. File size limits, allowed formats and fees are **not confirmed** — never quote them.

Digital products include e-books, templates, guides, courses, design resources and documents. The seller must be an approved seller (see seller onboarding articles) and is responsible for the product's accuracy and for owning or having rights to sell it. General listing steps are in *lst-create-listing*.

A good digital listing includes:
- clear title and full description of what the buyer gets;
- **file format(s)** (PDF, DOCX, PPTX, ZIP, EPUB, MP4 …) and any **software needed** (e.g., Canva, Photoshop);
- size of the content (pages, number of templates, lesson count/length);
- language (Amharic, English, both);
- preview images or sample pages that honestly represent the content;
- usage terms (personal use, commercial use allowed or not).

## Customer Steps
For the seller:
1. Log in to your seller account and start a new listing (see *lst-create-listing*), choosing the digital product type if offered.
2. Write the title, description, format, language, content size and software requirements.
3. Upload the final, complete file(s). Open the file yourself first to check it works and is the correct version.
4. Add honest preview images or sample pages.
5. Set the price. Platform fees/commission apply to sales; rates are shown in your seller terms once published.
6. Submit for listing review if required, and wait for approval.
7. After publishing, test what a buyer sees if possible, and update the file promptly if you find a problem.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your interest in selling digital products on Byfluence. Here are the main steps:

1. Start a new listing from your seller account and choose the digital product option if available.
2. Describe exactly what the buyer gets: format (for example PDF or ZIP), language, number of pages/templates/lessons and any software needed.
3. Upload the final file and open it yourself first to make sure it works.
4. Add honest preview images, set your price and submit the listing.

Please only sell content that you created or have the right to sell. If an upload fails, send me a screenshot of the error and the file type.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

በ Byfluence ላይ ዲጂታል ምርቶችን ለመሸጥ ስለፈለጉ እናመሰግናለን። ዋና ዋና ደረጃዎቹ እነዚህ ናቸው፦

1. ከሻጭ መለያዎ አዲስ ዝርዝር (listing) ይጀምሩ፤ ካለ የዲጂታል ምርት አማራጭን ይምረጡ።
2. ገዢው በትክክል የሚያገኘውን ይግለጹ፦ የፋይል አይነት (ለምሳሌ PDF ወይም ZIP)፣ ቋንቋ፣ የገጽ/የቴምፕሌት/የትምህርት ብዛት እና የሚያስፈልግ ሶፍትዌር ካለ።
3. የመጨረሻውን ፋይል ይጫኑ፤ በትክክል እንደሚሰራ ለማረጋገጥ መጀመሪያ እርስዎ ይክፈቱት።
4. ትክክለኛ ቅድመ-እይታ ምስሎችን ያክሉ፣ ዋጋዎን ያስቀምጡ እና ዝርዝሩን ያስገቡ።

እባክዎ እርስዎ የፈጠሩትን ወይም ለመሸጥ መብት ያለዎትን ይዘት ብቻ ይሽጡ። መጫኑ ካልተሳካ፣ የስህተቱን ስክሪንሾት እና የፋይሉን አይነት ይላኩልኝ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! New listing → digital product → describe format, language, content size and software needed → upload and test the final file → add honest previews → set price → submit. Only sell content you have rights to. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! አዲስ ዝርዝር → ዲጂታል ምርት → የፋይል አይነት፣ ቋንቋ፣ የይዘት መጠን እና የሚያስፈልግ ሶፍትዌር ይግለጹ → የመጨረሻውን ፋይል ጭነው ይሞክሩ → ትክክለኛ ቅድመ-እይታ ያክሉ → ዋጋ ያስቀምጡ → ያስገቡ። መብት ያለዎትን ይዘት ብቻ ይሽጡ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Upload fails repeatedly → **Technical / Engineering** (collect file type, approximate size, browser/device, screenshot).
- Listing rejected and seller disagrees → **Seller Operations**.
- Seller asks about commission/fees → payouts/fees articles; do not quote rates.
- Seller wants to sell content they did not create (e.g., "resell rights" packs, public-domain books) → **Seller Operations** / **Trust & Safety** for guidance.

## Policy Pending Approval
- Confirm allowed file formats, maximum file size, and whether courses are hosted on Byfluence or linked externally.
- Confirm commission/fees for digital products.
- Decide rules for "private label rights"/"resell rights" products and public-domain content.
- Decide whether previews and usage terms are mandatory fields.

## Internal Notes
- Do not accept files from sellers by Telegram/email to "upload for them".
- Encourage clear format and software information — it prevents most "won't open" and "not as described" tickets.

<!-- doc -->
# Seller Responsibilities for Digital Products
id: dig-seller-responsibilities
type: article
category: digital-products
subcategory: digital-sellers
audience: seller
priority: low
department: seller_ops
features: digital-products
tags: seller responsibilities digital, digital seller rules, fix broken file, buyer complaint digital, copyright rules seller, የሻጭ ኃላፊነት, ዲጂታል ሻጭ ደንቦች
related: dig-seller-upload-guide, dig-corrupted-file, dig-not-as-described, dig-copyright-complaint, dig-unauthorized-sharing, lst-create-listing
templates: tpl-request-order-details
policy_pending: yes

## Summary
A seller asks what they are responsible for when selling digital products on Byfluence, or support needs to explain a seller's obligations after a buyer complaint.

## Overview
> [!WARNING] **Planned feature.** Check the **Feature Status** page before treating digital product selling as live.

Byfluence is a marketplace facilitator; sellers are responsible for their offerings, subject to marketplace rules. For digital products, sellers are responsible for:

| Area | Responsibility |
|---|---|
| **Rights** | Only sell content they created or are licensed to sell (including images, fonts, music inside the product). |
| **Accuracy** | The description, previews, format, language and content size match what buyers receive. |
| **Working files** | Upload complete, working files; fix or replace faulty files promptly when told. |
| **Buyer support** | Respond to support enquiries about their products through official channels. |
| **Delivery through Byfluence** | Deliver only through Byfluence's access system — not by private Telegram/email, which bypasses buyer protection and records. |
| **No off-platform payments** | Never ask buyers to pay outside Byfluence. |
| **Honest marketing** | No fake reviews, misleading claims or exaggerated income promises (common in "make money" guides). |

What Byfluence does (confirmed at a high level): provides the marketplace, payments infrastructure, access delivery and support; reviews listings and seller accounts; may restrict sellers who break rules (seller statuses Active / Suspended / Banned).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your question. As a seller of digital products on Byfluence, you are responsible for:
1. Only selling content you created or have the right to sell
2. Making sure your description, previews and file format match what buyers receive
3. Uploading complete, working files and fixing any faulty file quickly
4. Delivering only through Byfluence and never asking buyers to pay outside the platform
5. Responding to our team when we contact you about a buyer's issue

Following these keeps your listings in good standing and protects you in case of disputes.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለጠየቁን እናመሰግናለን። በ Byfluence ላይ ዲጂታል ምርቶችን የሚሸጡ እንደመሆንዎ የሚከተሉት ኃላፊነቶች አሉብዎት፦
1. እርስዎ የፈጠሩትን ወይም ለመሸጥ መብት ያለዎትን ይዘት ብቻ መሸጥ
2. መግለጫዎ፣ ቅድመ-እይታዎችዎ እና የፋይሉ አይነት ገዢዎች ከሚያገኙት ጋር መመሳሰሉን ማረጋገጥ
3. የተሟሉ እና የሚሰሩ ፋይሎችን መጫን፣ የተበላሸ ፋይል ካለም በፍጥነት ማስተካከል
4. በ Byfluence በኩል ብቻ ማድረስ፣ ገዢዎች ከመድረኩ ውጭ እንዲከፍሉ በፍጹም አለመጠየቅ
5. ስለ ገዢ ጉዳይ ቡድናችን ሲያገኝዎት ምላሽ መስጠት

እነዚህን መከተል ዝርዝሮችዎ በጥሩ ሁኔታ እንዲቆዩ ያደርጋል፤ አለመግባባት ሲፈጠርም ይጠብቅዎታል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! As a digital seller you must: sell only content you have rights to, describe it accurately, upload working files and fix faults quickly, deliver only through Byfluence, never take off-platform payments, and respond to our team. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! እንደ ዲጂታል ሻጭ፦ መብት ያለዎትን ይዘት ብቻ ይሽጡ፣ በትክክል ይግለጹ፣ የሚሰሩ ፋይሎችን ይጫኑ እና ችግሮችን በፍጥነት ያስተካክሉ፣ በ Byfluence ብቻ ያድርሱ፣ ከመድረኩ ውጭ ክፍያ አይቀበሉ፣ ለቡድናችንም ምላሽ ይስጡ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Seller repeatedly ignores requests to fix files or respond → **Seller Operations**.
- Seller delivers files privately or takes off-platform payments → **Trust & Safety**.
- Seller makes misleading income/health claims in a digital product → **Seller Operations** / **Trust & Safety**.
- Seller asks about penalties or account restrictions → **Seller Operations**.

## Policy Pending Approval
- Publish the official digital seller rules, including deadlines to fix faulty files and response times to support.
- Define penalties for violations (warnings, listing removal, suspension).
- Define buyer usage rights and seller licensing requirements.
- Decide how refunds affect seller earnings for digital products.

## Internal Notes
- When explaining responsibilities after a complaint, stay factual and avoid implying guilt before review.
- Sellers who move buyers to Telegram for "faster delivery" undermine buyer protection — report the pattern.
