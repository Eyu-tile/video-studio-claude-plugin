<!-- doc -->
# Listing Not Visible to Buyers or Not in Search
id: lst-listing-not-visible
type: article
category: listings
subcategory: listing-review
audience: seller
priority: medium
department: seller_ops
features: seller-onboarding, consultations-1on1
tags: listing not showing, can't find my listing, not in search, buyers can't see, hidden listing, listing disappeared, ዝርዝሬ አይታይም, ፍለጋ ላይ የለም, ገዢዎች አያዩትም
related: lst-listing-under-review, lst-listing-rejected, lst-reported-listing, lst-availability-calendar, sel-account-restrictions, sel-performance-standards
templates:
policy_pending: yes

## Summary
A seller says their listing doesn't appear for buyers, doesn't show in search, or has disappeared.

## Issue Description
The seller may be searching with a different word, the listing may be under review, rejected, paused, out of availability, removed after a report, or hidden because the seller's account is restricted or suspended. Search ranking rules are **not confirmed**, so agents must not promise a position in results. The agent works through visibility causes in order.

## Possible Causes
- Listing still under review, or rejected.
- Listing paused/unpublished by the seller (or an edit sent it back to review).
- No available time slots (consultations) so it may not be bookable or shown.
- Listing removed or hidden after a report (`lst-reported-listing`).
- Seller account restricted/suspended/banned — listings hidden.
- Buyer searching with different keywords/category, or filters applied.
- Search indexing delay or technical bug.
- Seller viewing a cached page or signed in as themselves (preview vs. public view).

## Information to Collect
- Seller's registered email/phone
- Listing title (or ID / link)
- How they searched (words used, category, filters) and on which device
- Since when it's missing
- Any notice received about the listing

## Troubleshooting Steps
1. Confirm identity; open the listing in the admin dashboard (if you have access).
2. Check in order:
   - [ ] Listing status: live / under review / rejected / paused / removed
   - [ ] Seller operational status: Active / restricted / Suspended / Banned
   - [ ] Availability: any future slots? (for consultations)
   - [ ] Report or moderation action on the listing
3. If all are fine: open the public listing link in a private/incognito window; search with the exact title.
   - **Opens by link but not in search** → explain search depends on words/category; suggest clearer title and category; if exact-title search fails → **Technical / Engineering**.
   - **Link does not open publicly** → **Technical / Engineering**.
4. Advise the seller on findability: clear title with key words buyers use (in Amharic and English if relevant), right category, complete description, up-to-date availability.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand buyers can't find your listing "{{product_name}}", and I've checked it for you.

[Explain the finding, e.g. "Your listing has no available time slots at the moment, so buyers can't book it. Adding new availability will make it bookable again." / "Your listing is still under review." / "Your listing is live and opens from its link; search results depend on the words buyers use."]

Tips to help buyers find you:
- use a clear title with the words buyers would search for,
- choose the most suitable category,
- keep your availability up to date.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ገዢዎች "{{product_name}}" የተባለውን ዝርዝርዎን ማግኘት እንዳልቻሉ ተረድቻለሁ፤ አጣርቼልዎታለሁ።

[ውጤቱን ያብራሩ፤ ለምሳሌ "ዝርዝርዎ በአሁኑ ጊዜ ክፍት የቀጠሮ ሰዓት ስለሌለው ገዢዎች ቀጠሮ መያዝ አይችሉም። አዲስ የሚገኙበትን ጊዜ ሲጨምሩ እንደገና ቀጠሮ መያዝ ይቻላል።" / "ዝርዝርዎ አሁንም በግምገማ ላይ ነው።" / "ዝርዝርዎ ቀጥታ ነው፣ በሊንኩም ይከፈታል፤ የፍለጋ ውጤቶች ገዢዎች በሚጠቀሙባቸው ቃላት ላይ ይወሰናሉ።"]

ገዢዎች እንዲያገኙዎት የሚረዱ ምክሮች፦
- ገዢዎች የሚፈልጉባቸውን ቃላት የያዘ ግልጽ ርዕስ ይጠቀሙ፣
- በጣም ተስማሚውን ምድብ ይምረጡ፣
- የሚገኙበትን ጊዜ ወቅታዊ ያድርጉ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I checked "{{product_name}}": [finding]. Tip: clear title with words buyers search, right category, up-to-date availability. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ "{{product_name}}"ን አጣርቻለሁ፦ [ውጤት]። ምክር፦ ገዢዎች የሚፈልጉባቸውን ቃላት የያዘ ግልጽ ርዕስ፣ ትክክለኛ ምድብ፣ ወቅታዊ የሚገኙበት ጊዜ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our team is still checking why "{{product_name}}" isn't showing as expected. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። "{{product_name}}" እንደሚጠበቀው ለምን እንደማይታይ ቡድናችን አሁንም እያጣራ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Live listing doesn't open publicly or not found by exact title → **Technical / Engineering**, priority Medium.
- Listing removed after a report, seller disputes → `lst-reported-listing` / **Seller Operations**.
- Account restricted/suspended → follow seller-status articles.
- Seller demands top placement or asks how ranking works → ranking rules not confirmed; **Senior Support / Supervisor** if they insist.

## Resolution Procedure
1. Listing confirmed visible publicly (incognito) or cause explained.
2. Record cause and advice given.

## Policy Pending Approval
- Document how search ranking works (factors, reviews, performance) and what can be shared with sellers.
- Decide whether listings without availability are hidden or shown as unavailable.
- Decide whether paid promotion/featured placement will exist.

## Internal Notes
- Always test in an incognito window — the seller's own view may differ from the public view.
- Never promise "your listing will appear at the top".

<!-- doc -->
# Seller's Listing Was Reported or Removed
id: lst-reported-listing
type: article
category: listings
subcategory: listing-review
audience: seller
priority: medium
department: seller_ops
features: seller-onboarding
tags: listing reported, listing removed, taken down, complaint about my listing, listing deleted by byfluence, copyright claim, ዝርዝሬ ተወገደ, ሪፖርት ተደርጓል, ቅሬታ
related: lst-listing-rejected, lst-prohibited-items, tns-fake-products, tns-misleading-descriptions, sel-account-restrictions, sel-reactivation-request
templates: tpl-listing-rejected
policy_pending: yes

## Summary
A seller's live listing was reported by a buyer or another party and has been hidden or removed, and the seller wants to know why and how to restore it.

## Issue Description
Listings can be reported for misleading descriptions, fake/counterfeit items, copyright infringement (copied images or course content), prohibited content, or off-platform contact. After review, Seller Operations or Trust & Safety may remove or hide the listing. The seller may also see it as an unfair attack by a competitor. Agents must **never reveal who reported** the listing, share only recorded shareable reasons, and route disputes.

## Possible Causes
- Misleading description or unverifiable claims.
- Counterfeit or fake product (when product selling is live).
- Copyright or trademark complaint (images, materials, brand names).
- Prohibited or restricted item/service.
- Contact details / off-platform payment requests.
- Multiple buyer complaints about delivery not matching the listing.
- Malicious or mistaken report (competitor).

## Information to Collect
- Seller's registered email/phone
- Listing title (or ID)
- Notice received (screenshot)
- Seller's explanation and evidence (e.g., proof they own images, licences, permissions) — uploaded via the platform or attached to the ticket, **not** ID documents in chat
- Whether upcoming bookings/orders exist for this listing

## Troubleshooting Steps
1. Confirm identity; check listing status and moderation notes through authorized tools (admin dashboard, if you have access).
2. Identify the category of action (misleading, IP, prohibited, counterfeit, contact info, complaints).
3. Share only the shareable reason. **Never** share reporter identity or report text.
4. Fixable (e.g., remove contact info, correct description) → guide edit and resubmission.
5. Seller disputes (e.g., "I own these images") → collect evidence, escalate to **Seller Operations** (IP or counterfeit → **Trust & Safety**).
6. Check for upcoming bookings on the removed listing → **Senior Support / Supervisor** to make sure buyers are handled.
7. Repeated reports on the same seller → note for Seller Operations (possible account review).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand your listing "{{product_name}}" has been removed from public view, and I know this affects your business.

I have checked it. The listing was reviewed after a concern was raised, and the reason recorded is: [shareable reason]. For privacy reasons, we can't share details about who raised the concern.

[If fixable:] You can edit the listing to [change] and resubmit it for review.
[If disputing:] If you believe this is a mistake, please reply with your explanation and any supporting information (for example, proof that you own the images), and I'll pass it to the responsible team.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። "{{product_name}}" የተባለው ዝርዝርዎ ከሕዝብ እይታ እንደተወገደ ተረድቻለሁ፤ ይህ ንግድዎን እንደሚነካ እገነዘባለሁ።

አጣርቼዋለሁ። ዝርዝሩ የተገመገመው ስጋት ከተነሳ በኋላ ሲሆን የተመዘገበው ምክንያት፦ [ሊገለጽ የሚችል ምክንያት]። ለግላዊነት ሲባል ስጋቱን ማን እንዳነሳ ዝርዝር ማጋራት አንችልም።

[የሚስተካከል ከሆነ፦] ዝርዝሩን [ለውጥ] በማድረግ አስተካክለው ለግምገማ እንደገና ማስገባት ይችላሉ።
[ከተቃወሙ፦] ይህ ስህተት ነው ብለው ካመኑ እባክዎ ማብራሪያዎን እና የሚደግፍ መረጃ (ለምሳሌ ምስሎቹ የእርስዎ መሆናቸውን የሚያሳይ) ይላኩልኝ፤ ለሚመለከተው ቡድን አስተላልፋለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, "{{product_name}}" was removed after a review: [shareable reason]. We can't share who raised it. You can [fix and resubmit] or reply with your explanation/evidence and I'll pass it on. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ "{{product_name}}" ከግምገማ በኋላ ተወግዷል፦ [ሊገለጽ የሚችል ምክንያት]። ማን እንዳነሳው ማጋራት አንችልም። [አስተካክለው እንደገና ማስገባት] ወይም ማብራሪያዎን/ማስረጃዎን መላክ ይችላሉ፤ አስተላልፋለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. The responsible team is still reviewing your listing "{{product_name}}". We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ኃላፊው ቡድን "{{product_name}}" ዝርዝርዎን አሁንም እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Dispute about misleading/prohibited removal → **Seller Operations**.
- Copyright, trademark, counterfeit, fraud → **Trust & Safety**.
- Upcoming bookings/orders affected → **Senior Support / Supervisor**, priority High.
- Seller accuses a competitor of malicious reporting → record and pass to **Trust & Safety**; don't comment.

## Resolution Procedure
1. Listing restored, edited and re-approved, or removal confirmed as final.
2. Affected buyers handled.
3. Record category, evidence received, decision and outcome.

## Policy Pending Approval
- Define the listing report/takedown process and who decides.
- Define the counter-notice process for copyright complaints.
- Define how many removals lead to account review.

## Internal Notes
- Even if the seller guesses who reported them, do not confirm or deny.
- Buyers who report listings are handled via `tns-fake-products` / `tns-misleading-descriptions`.

<!-- doc -->
# Setting Prices and Price Changes
id: lst-pricing-questions
type: article
category: listings
subcategory: pricing-availability
audience: seller
priority: low
department: support_l1
features: seller-onboarding, consultations-1on1, consultations-group
tags: set price, change price, pricing, discount, how much to charge, price in birr, commission deducted, ዋጋ ማስቀመጥ, ዋጋ መቀየር, ቅናሽ, ኮሚሽን
related: lst-create-listing, lst-edit-listing, out-how-earnings-work, out-pending-vs-available, inv-pricing-rules
templates:
policy_pending: yes

## Summary
A seller asks how to set or change prices, how fees affect what they receive, or whether they can offer discounts.

## Overview
Sellers set their own prices for their listings. Byfluence earns through commissions/fees on transactions, but **commission rates are not confirmed** — never quote a percentage or amount. The seller's earnings are calculated after platform fees (see `out-how-earnings-work`).

### Key points for sellers
- Prices are set per listing (for consultations: per session; for group sessions: per participant).
- Price changes apply to **new** bookings; buyers who already paid keep their price.
- The amount shown in earnings may be lower than the listing price because platform fees are deducted.
- Pricing advice: research similar listings, price for the value and duration, be clear about what's included.
- Discounts, coupons or promotional pricing are **not confirmed** features.
- Off-platform discounts ("pay me directly and I'll give you a lower price") must not be encouraged — it removes buyer protection (formal rule pending).

> [!WARNING] Never quote commission rates, fees or a "you'll receive X%" figure. These are pending approval.

## Customer Steps
1. Open your seller dashboard and select the listing.
2. Edit the price field and save.
3. Check the listing status (it may be reviewed again).
4. Remember: existing bookings keep their original price.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. You set the price for each of your listings, and you can change it from your seller dashboard by editing the listing.

A few things to know:
- A new price applies to new bookings; buyers who have already paid keep their original price.
- Byfluence earns a fee on transactions, so the earnings shown in your dashboard are calculated after platform fees. I'm not able to quote exact fee details here — I've noted your question for the responsible team.
- Please keep all payments on Byfluence. This protects you and your buyers.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ለእያንዳንዱ ዝርዝርዎ ዋጋውን የሚወስኑት እርስዎ ነዎት፤ ዝርዝሩን በማስተካከል ከሻጭ ዳሽቦርድዎ ዋጋውን መቀየር ይችላሉ።

ማወቅ ያለብዎት ነገሮች፦
- አዲሱ ዋጋ ለአዲስ ቀጠሮዎች ይሠራል፤ ቀደም ብለው የከፈሉ ገዢዎች በነበረው ዋጋ ይቀጥላሉ።
- Byfluence በግብይቶች ላይ ክፍያ (fee) ስለሚያገኝ በዳሽቦርድዎ ላይ የሚታየው ገቢ የመድረኩ ክፍያ ከተቀነሰ በኋላ የሚሰላ ነው። ትክክለኛውን የክፍያ ዝርዝር እዚህ መናገር አልችልም — ጥያቄዎን ለሚመለከተው ቡድን መዝግቤያለሁ።
- እባክዎ ሁሉንም ክፍያዎች በByfluence በኩል ያድርጉ። ይህ እርስዎንም ገዢዎችዎንም ይጠብቃል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! You set and change prices by editing your listing in the dashboard. New prices apply to new bookings only. Earnings are shown after platform fees; I can't quote fee details but have noted your question. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! ዋጋን ዝርዝርዎን በዳሽቦርድ በማስተካከል ያስቀምጣሉ/ይቀይራሉ። አዲስ ዋጋ ለአዲስ ቀጠሮዎች ብቻ ይሠራል። ገቢ የሚታየው የመድረክ ክፍያ ከተቀነሰ በኋላ ነው፤ የክፍያ ዝርዝር መናገር ባልችልም ጥያቄዎን መዝግቤያለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Seller asks for exact commission/fee rates → **Senior Support / Supervisor** (do not quote).
- Price shown to buyers differs from what the seller set → **Technical / Engineering**.
- Seller's earnings don't match price minus fees → **Payments & Finance** (see `out-how-earnings-work`).
- Seller changed price on already-booked sessions and charged buyers more → **Senior Support / Supervisor**.

## Policy Pending Approval
- Approve and publish commission/fee rates and how they are shown to sellers.
- Decide whether minimum/maximum prices apply per listing type.
- Decide whether discounts, coupons or promotions will exist.
- Approve the rule on off-platform payments and discounts.

## Internal Notes
- "Why did I get less than my price?" is almost always fees + Pending vs. Available — explain, then escalate if numbers still don't add up.
- Very low or very high prices can be a fraud signal (e.g., bait listings); flag to Seller Operations if suspicious.

<!-- doc -->
# Managing Availability and Stock
id: lst-availability-calendar
type: article
category: listings
subcategory: pricing-availability
audience: seller
priority: medium
department: support_l1
features: consultations-1on1, consultations-group, physical-products
tags: availability, calendar, time slots, block dates, stock, out of stock, double booking, holiday, የሚገኙበት ጊዜ, ቀን መዝጋት, ክምችት, ሰዓት ማስቀመጥ
related: con-seller-availability-setup, grp-seller-create-group-session, lst-create-consultation-listing, lst-listing-not-visible, lst-edit-listing, phy-seller-order-management
templates:
policy_pending: yes

## Summary
A seller asks how to set, update or block availability for consultations, or how to manage stock for products, or reports a double booking.

## Overview
For consultations, availability determines which date/time slots buyers can book. Outdated availability is a top cause of seller no-shows and buyer complaints. For physical products (planned), stock determines whether items can be ordered.

> [!NOTE] Physical products are a planned feature. Check the **Feature Status** page before explaining stock management to a seller; if not live, say it isn't available yet. For order management when live, see `phy-seller-order-management`.

### Good availability practice
- Only open slots the seller can definitely attend.
- Block holidays, travel and busy days in advance.
- Check the time zone shown on the platform (time-zone confusion causes missed sessions).
- Leave buffer time between sessions.
- Removing a slot does **not** cancel a booking already made in it — existing bookings must still be delivered or handled through the official reschedule/cancel process.

For setup details see `con-seller-availability-setup`; for group sessions see `grp-seller-create-group-session`.

### Double bookings
If two buyers appear booked in the same 1:1 slot, treat it as a technical issue and protect both buyers — escalate quickly, especially if the session is soon.

## Customer Steps
1. Open your seller dashboard and go to availability/calendar.
2. Add the dates and times you can attend; remove times you can't.
3. Block holidays or busy days.
4. Check that times show in the correct time zone.
5. Review upcoming bookings — removing a slot doesn't cancel a booking.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. You can manage your availability from your seller dashboard: open your availability or calendar, add the times you can attend, and remove or block times you can't.

Helpful tips:
- only open times you are sure you can attend,
- block holidays and busy days in advance,
- check that the times are shown in the correct time zone,
- removing a time slot does not cancel a session that is already booked — please still attend it, or contact us if you can't.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። የሚገኙበትን ጊዜ ከሻጭ ዳሽቦርድዎ ማስተዳደር ይችላሉ፦ የሚገኙበት ጊዜ (availability) ወይም የቀን መቁጠሪያ ክፍሉን ይክፈቱ፣ መገኘት የሚችሉባቸውን ሰዓቶች ይጨምሩ፣ የማይችሉባቸውን ያስወግዱ ወይም ይዝጉ።

ጠቃሚ ምክሮች፦
- መገኘት እንደሚችሉ እርግጠኛ የሆኑባቸውን ሰዓቶች ብቻ ይክፈቱ፣
- በዓላትን እና የተጨናነቁ ቀናትን አስቀድመው ይዝጉ፣
- ሰዓቶቹ በትክክለኛው የሰዓት አቆጣጠር (time zone) መታየታቸውን ያረጋግጡ፣
- አንድን ሰዓት ማስወገድ ቀድሞ የተያዘን ምክክር አይሰርዝም — እባክዎ በሰዓቱ ይገኙ፣ መገኘት ካልቻሉ ደግሞ ያሳውቁን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! Dashboard → availability/calendar → add times you can attend, remove/block others. Check the time zone. Removing a slot doesn't cancel an existing booking — attend it or contact us. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! ዳሽቦርድ → የሚገኙበት ጊዜ/የቀን መቁጠሪያ → የሚገኙባቸውን ሰዓቶች ይጨምሩ፣ ሌሎቹን ያስወግዱ/ይዝጉ። የሰዓት አቆጣጠሩን ያረጋግጡ። ሰዓት ማስወገድ የተያዘ ቀጠሮን አይሰርዝም — ይገኙ ወይም ያሳውቁን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Double booking or bookings in removed/blocked slots → **Technical / Engineering**, priority High if the session is soon; inform **Senior Support / Supervisor** to protect buyers.
- Seller cannot attend an already booked session → follow consultation reschedule/cancellation articles; **Senior Support / Supervisor** if the session is imminent.
- Times displayed in the wrong time zone → **Technical / Engineering**.
- Stock questions while physical products are not live → check **Feature Status**; do not promise.

## Policy Pending Approval
- Confirm how the platform displays time zones to buyers and sellers.
- Decide minimum notice for sellers to change availability or cancel booked sessions.
- Define stock rules for physical products (oversell handling) when the feature launches.

## Internal Notes
- When a seller says "I removed that time, why did someone book?", check the booking timestamp vs. the edit time — the booking may have come first.
- Sellers abroad (diaspora consultants) are especially prone to time-zone errors.

<!-- doc -->
# Prohibited and Restricted Items and Services
id: lst-prohibited-items
type: article
category: listings
subcategory: prohibited
audience: both
priority: medium
department: seller_ops
features: seller-onboarding, physical-products, digital-products
tags: prohibited items, restricted items, not allowed to sell, banned products, illegal goods, counterfeit, weapons, adult content, medical advice, የተከለከሉ ዕቃዎች, መሸጥ የማይፈቀድ, ሕገወጥ
related: lst-listing-rejected, lst-reported-listing, tns-fake-products, tns-misleading-descriptions, sel-who-can-sell, sel-responsibilities
templates: tpl-listing-rejected
policy_pending: yes

## Summary
A seller asks whether something can be listed, or a buyer reports a listing that should not be allowed. The official prohibited/restricted list has not yet been approved.

## Overview
Byfluence must keep illegal, dangerous and deceptive offerings off the marketplace. The **official prohibited and restricted list is pending approval**. Until it is approved, agents use the **proposed** categories below to recognise obvious problems and **escalate** — they do not make final rulings and do not quote the list as official policy.

> [!POLICY] The categories below are a **proposal for management approval**, not an approved policy. Do not present them to customers as "Byfluence's official rules". Say the listing "may not be allowed under marketplace rules" and escalate.

### Proposed PROHIBITED categories (for approval)
| Proposed category | Examples |
|---|---|
| Illegal goods and services | Drugs and drug paraphernalia, stolen goods, forged documents, hacking services, services that break Ethiopian law |
| Weapons and dangerous items | Firearms, ammunition, explosives, weapon parts, dangerous chemicals |
| Counterfeit and IP-infringing items | Fake branded goods, pirated software, copied courses/e-books, unlicensed brand use |
| Adult and sexual content | Pornography, sexual services, sexually explicit material |
| Fraudulent / deceptive offers | Get-rich-quick schemes, pyramid/Ponzi schemes, "guaranteed" investment returns, fake certificates, exam cheating services |
| Identity and financial documents | Selling IDs, accounts, SIM cards registered to others, bank accounts, personal data |
| Hate and violence | Content promoting hate, violence, or discrimination |
| Hazardous health products | Unapproved medicines, prescription drugs, unregistered supplements with health claims |

### Proposed RESTRICTED categories (allowed only with extra review/approval)
| Proposed category | Why restricted |
|---|---|
| Regulated medical advice / health consultations | Risk of harm; may need proof of professional licence |
| Legal advice | May need licensed professional |
| Financial / investment advice | Risk of fraud and loss; may need licence |
| Mental health / psychological counselling | Duty of care; may need qualification |
| Alcohol, tobacco and age-restricted goods (when products live) | Age and legal limits |
| Used electronics and phones (when products live) | Stolen goods and IMEI risk |
| Educational certificates or "official" training | Accreditation claims |

### How to handle
- **Seller asks before listing** → explain it may be restricted/prohibited; escalate to **Seller Operations** for a decision before they publish.
- **Listing already live and clearly prohibited** (weapons, drugs, adult, counterfeit) → report to **Trust & Safety**, priority High. Do not wait.
- **Buyer reports a listing** → thank them, collect the link/title, report to **Trust & Safety** (see `tns-fake-products`, `tns-misleading-descriptions`).
- **Possible immediate danger** (weapons, threats, exploitation of minors) → **Trust & Safety**, priority Critical, inform supervisor immediately.

## Customer Steps
1. Before listing, make sure your service or product is legal and honestly described.
2. If you are unsure whether it is allowed, contact support **before** publishing.
3. For professional advice (medical, legal, financial, psychological), be ready to show your qualifications if asked.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for checking with us before listing — that's very helpful.

Some items and services may not be allowed, or may need extra review, under Byfluence marketplace rules — for example, anything illegal, dangerous, counterfeit or misleading, and some types of professional advice.

I have sent your question about "{{product_name}}" to our Seller Operations team so they can confirm whether it can be listed. Please don't publish it until you receive their answer.

Your case number is {{ticket_id}}. We will update you as soon as we have a decision.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ዝርዝሩን ከመለጠፍዎ በፊት ስላጣሩን እናመሰግናለን — ይህ በጣም ጠቃሚ ነው።

አንዳንድ ዕቃዎች እና አገልግሎቶች በByfluence የገበያ ቦታ ደንቦች መሠረት ላይፈቀዱ ወይም ተጨማሪ ግምገማ ሊያስፈልጋቸው ይችላል — ለምሳሌ ሕገወጥ፣ አደገኛ፣ ሐሰተኛ (counterfeit) ወይም አሳሳች የሆነ ማንኛውም ነገር፣ እንዲሁም አንዳንድ የሙያ ምክር አይነቶች።

"{{product_name}}" መለጠፍ ይቻል እንደሆነ እንዲያረጋግጡ ጥያቄዎን ለሻጭ ኦፕሬሽንስ ቡድናችን ልኬያለሁ። እባክዎ መልሳቸው እስኪደርስዎ ድረስ አይለጥፉት።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ውሳኔ እንዳገኘን ወዲያውኑ እናሳውቅዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for checking first! Some items/services may not be allowed or need extra review. I've asked Seller Operations to confirm "{{product_name}}" — please don't publish until they reply. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ አስቀድመው ስላጣሩ እናመሰግናለን! አንዳንድ ዕቃዎች/አገልግሎቶች ላይፈቀዱ ወይም ተጨማሪ ግምገማ ሊያስፈልጋቸው ይችላል። "{{product_name}}"ን እንዲያረጋግጡ የሻጭ ኦፕሬሽንስ ቡድንን ጠይቄያለሁ — መልስ እስኪመጣ አይለጥፉ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Pre-listing question about a possibly restricted item/service → **Seller Operations**, priority Low/Medium.
- Live listing in a clearly prohibited category → **Trust & Safety**, priority High.
- Weapons, threats, exploitation of minors, serious illegal activity → **Trust & Safety**, priority Critical + supervisor immediately; **Management** for legal/regulatory matters.
- Counterfeit or IP complaint → **Trust & Safety**.

## Policy Pending Approval
- Approve the official prohibited items/services list (proposal above).
- Approve the restricted list and the extra evidence required for each (e.g., professional licence for medical/legal/financial advice).
- Decide penalties for listing prohibited items (removal, warning, suspension, ban).
- Decide the process for law-enforcement referrals.
- Decide age-restricted product handling when physical products launch.

## Internal Notes
- When in doubt, escalate — never say "yes, that's fine" for anything in the restricted table.
- Medical consultations are the most frequent grey area: general wellness talk vs. diagnosis/prescription. Always escalate.
- Do not describe to a seller exactly how to reword a prohibited listing so it passes review.
