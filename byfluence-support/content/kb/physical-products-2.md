<!-- doc -->
# Delivery Areas (Addis Ababa First)
id: phy-delivery-areas
type: article
category: physical-products
subcategory: delivery
audience: both
priority: low
department: fulfillment
features: physical-products, delivery-addis
tags: delivery areas, do you deliver to, delivery outside addis, delivery fee, shipping to my city, regional delivery, ታደርሳላችሁ, ማድረሻ ቦታዎች, ከአዲስ አበባ ውጭ
related: phy-how-to-order, phy-delivery-delay, phy-incorrect-address, phy-order-processing-status, inv-fulfillment-responsibility
templates: tpl-request-order-details
policy_pending: yes

## Summary
A buyer or seller asks where Byfluence delivers physical products, whether delivery is available outside Addis Ababa, and what delivery costs or how long it takes.

## Overview
> [!WARNING] **Planned feature.** Addis Ababa delivery is a planned expansion feature. Delivery partners, areas, fees and times are **not confirmed**. Check the **Feature Status** page before telling anyone that delivery is available, and never state specific areas, fees, times or partner names unless they are published on the Feature Status page or an approved announcement.

What is confirmed: the initial rollout of physical products **prioritises Addis Ababa**. Nothing else about coverage is confirmed. That means:
- Do **not** confirm delivery to any specific sub-city, neighbourhood, or to any city outside Addis Ababa.
- Do **not** quote delivery fees, free-delivery thresholds or delivery times.
- Do **not** name a delivery partner.
- The checkout (once live) is the authoritative source for what is available for a specific address.

How to answer common questions:
| Question | Approved approach |
|---|---|
| "Do you deliver to Bole / Kolfe / my area?" | Delivery is starting with Addis Ababa; the checkout will show whether delivery is available for the address. |
| "Do you deliver to Adama / Hawassa / Bahir Dar?" | We are starting with Addis Ababa; we cannot confirm other cities yet. Record the request as feedback. |
| "How much is delivery?" | Any delivery fee is shown at checkout before payment. |
| "How long does delivery take?" | We cannot give a delivery time in advance; the order status will be updated. |
| Seller: "Can I deliver myself?" | Delivery arrangements for sellers are not yet confirmed — escalate to Logistics & Fulfillment. |

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your question about delivery.

Byfluence is starting product delivery with Addis Ababa. Delivery areas, any delivery fees and options are shown at checkout for your address before you pay, so that is the best place to check. At the moment I'm not able to confirm delivery to other cities, but I have noted your request and shared it with our team.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ማድረስ አገልግሎት ስለጠየቁን እናመሰግናለን።

Byfluence የምርት ማድረስ አገልግሎትን በአዲስ አበባ እየጀመረ ነው። የማድረሻ ቦታዎች፣ ካለ የማድረሻ ክፍያ እና አማራጮች ከመክፈልዎ በፊት ለአድራሻዎ በክፍያ ገጹ (checkout) ላይ ይታያሉ፤ ስለዚህ እዚያ ማረጋገጥ ጥሩ ነው። በአሁኑ ጊዜ ወደ ሌሎች ከተሞች ማድረስን ማረጋገጥ አልችልም፤ ነገር ግን ጥያቄዎን መዝግቤ ለቡድናችን አጋርቻለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, product delivery is starting with Addis Ababa. Available areas and any delivery fee are shown at checkout for your address. I can't confirm other cities yet, but I've noted your request. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የምርት ማድረስ በአዲስ አበባ እየተጀመረ ነው። ለአድራሻዎ የሚገኙ ቦታዎችና ካለ ክፍያ በ checkout ላይ ይታያሉ። ሌሎች ከተሞችን ገና ማረጋገጥ አልችልም፤ ጥያቄዎን መዝግቤያለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Seller asks about delivery arrangements, pickup, fees or partner details → **Logistics & Fulfillment**.
- Buyer's address inside Addis Ababa is rejected at checkout while similar addresses work → **Technical / Engineering** with a screenshot, copy **Logistics & Fulfillment**.
- Business/partnership enquiries from delivery companies → **Management** (via the feedback/partnership process).

## Policy Pending Approval
- Confirm the delivery areas (sub-cities/zones) covered at launch and how they are shown at checkout.
- Confirm delivery fees, who pays them and whether they vary by area or size.
- Confirm delivery partners and whether sellers may self-deliver.
- Approve customer-facing wording for typical delivery times.
- Decide when and how delivery outside Addis Ababa will be offered.

## Internal Notes
- Even if you personally know of a delivery partner or a fee, do not share it until it is published on the Feature Status page.
- Log out-of-area requests with the tag "delivery-area-request" so management can see demand by city.

<!-- doc -->
# Delivery Delayed
id: phy-delivery-delay
type: article
category: physical-products
subcategory: delivery
audience: buyer
priority: medium
department: fulfillment
features: physical-products, delivery-addis
tags: delivery late, order not arrived, delayed delivery, still waiting for order, where is my package, ትዕዛዜ ዘገየ, አልደረሰኝም, መቼ ይደርሳል
related: phy-order-processing-status, phy-incorrect-address, phy-contact-seller, phy-order-cancellation-buyer, phy-not-delivered-marked-delivered, phy-tsg-order-problem-master
templates: tpl-delivery-delay, tpl-order-status-check, tpl-request-order-details
policy_pending: yes

## Summary
The buyer's order has not arrived and they feel it is taking too long, or the expected delivery date has passed.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products and Addis Ababa delivery are live. Delivery times are **not confirmed** — never promise a delivery date.

The buyer paid, the order is confirmed, but the product has not arrived. The order may still be with the seller (processing) or with delivery (shipped/out for delivery). The buyer may be frustrated, may have needed the item for a specific date (gift, event), or may suspect fraud.

## Possible Causes
- The seller has not prepared or handed over the order (stock problem, inactive seller).
- The delivery person could not find the address (no landmark, wrong sub-city) or could not reach the buyer by phone.
- The buyer's phone was off/unreachable on the delivery attempt.
- High order volume, traffic, weather, holidays or public events affecting delivery in Addis Ababa.
- The parcel was misrouted or lost.
- The status was not updated even though the parcel was delivered or returned.

## Information to Collect
- Order ID, product name, seller name
- Date ordered and any delivery date shown to the buyer
- Current delivery address and phone number (check they are correct and reachable)
- Whether the buyer missed any calls from unknown numbers
- Whether the item was needed by a specific date

## Troubleshooting Steps
1. Find the order and check its status and history (when confirmed, when handed over).
2. Check the address and phone number on the order. If incomplete or wrong, follow *phy-incorrect-address*.
3. **Still with the seller (processing):** contact the seller for a status update and reason. If the seller cannot fulfil, follow *phy-order-cancellation-seller*.
4. **Shipped / out for delivery:** check with **Logistics & Fulfillment** (or the seller, if the seller delivers) for the last delivery attempt and any notes ("customer unreachable", "address not found").
5. **Status shows returned to seller / failed delivery:** explain why and arrange redelivery or escalate per the approved process.
6. Tell the buyer what you found and the next step — no dates you cannot guarantee.
7. If the buyer asks to cancel because of the delay, follow *phy-order-cancellation-buyer*.
8. Set a follow-up time and keep the ticket open.

- [ ] Order status and history checked
- [ ] Address and phone verified
- [ ] Seller / fulfillment contacted
- [ ] Buyer updated with next step

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us, and I'm sorry your order {{order_id}} has not arrived yet. I understand how frustrating it is to wait.

I have checked your order, and we have contacted the team handling it for an update. To help the delivery go smoothly, please confirm:
1. That your phone number on the order is correct and will be switched on
2. A clear landmark near your location (for example a well-known building, church, school or shop)

I will update you as soon as we hear back. Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን፤ ትዕዛዝዎ {{order_id}} እስካሁን ስላልደረሰ ይቅርታ እንጠይቃለን። መጠበቅ ምን ያህል እንደሚያበሳጭ እረዳለሁ።

ትዕዛዝዎን አጣርቻለሁ፤ ትዕዛዙን የሚያስተናግደውን ቡድን መረጃ እንዲሰጠን ጠይቀናል። ማድረሱ በቀላሉ እንዲከናወን፣ እባክዎ የሚከተሉትን ያረጋግጡልኝ፦
1. በትዕዛዙ ላይ ያለው ስልክ ቁጥርዎ ትክክል መሆኑን እና ክፍት እንደሚሆን
2. በአቅራቢያዎ ያለ ግልጽ መለያ ምልክት (ለምሳሌ የታወቀ ሕንፃ፣ ቤተ ክርስቲያን፣ መስጊድ፣ ትምህርት ቤት ወይም ሱቅ)

ምላሽ እንደደረሰን ወዲያውኑ መረጃ እሰጥዎታለሁ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry order {{order_id}} hasn't arrived yet. We've asked for an update. Please confirm your phone number is correct and on, and send a clear landmark near you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ትዕዛዝ {{order_id}} ገና ስላልደረሰ ይቅርታ። መረጃ ጠይቀናል። እባክዎ ስልክ ቁጥርዎ ትክክልና ክፍት መሆኑን ያረጋግጡ፤ በአቅራቢያዎ ያለ ግልጽ ምልክትም ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}} for order {{order_id}}. [What we learned: e.g., the seller has handed the order to delivery / the delivery team could not reach you.] Next step: [next step]. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} (ትዕዛዝ {{order_id}}) የሚሰጥ መረጃ ነው። [ያገኘነው መረጃ፦ ለምሳሌ ሻጩ ትዕዛዙን ለአድራሹ አስረክቧል / አድራሹ ሊያገኝዎት አልቻለም።] ቀጣዩ ደረጃ፦ [ቀጣይ እርምጃ]። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Order with delivery and no update from the delivery side → **Logistics & Fulfillment**.
- Seller has not handed over the order and does not respond → **Seller Operations**; **Senior Support** if the buyer wants to cancel.
- Parcel appears lost → **Logistics & Fulfillment**, priority High.
- Buyer needed the item for a time-critical reason and the delay caused loss, or the buyer threatens public complaint → **Senior Support / Supervisor**.
- Many orders delayed at the same time → alert the supervisor (possible operational incident) and check Announcements.

## Resolution Procedure
1. Confirm with the buyer that the order has been received, or that it has been cancelled and moved to refund.
2. Record cause of delay (seller, address, unreachable phone, delivery capacity, lost) — this data helps management set delivery policy.

## Policy Pending Approval
- Define the expected delivery timeframe and when an order officially counts as "delayed".
- Decide whether buyers can cancel and get a refund because of a delay, and from when.
- Decide whether any compensation (e.g., delivery fee refund) applies to late deliveries.
- Confirm the number of delivery attempts and what happens after failed attempts.

## Internal Notes
- Do not repeat a delivery date given by a seller or delivery person unless it is in the system — if it is missed, the buyer will blame Byfluence.
- Replace bracketed text in follow-ups before sending.
- If the delivery note says "customer unreachable" but the buyer insists they got no call, ask for the phone number again and check for a typo — very common.
- Ethiopian public holidays and big events can affect delivery in Addis Ababa; mention possible disruption only when it actually applies.

<!-- doc -->
# Wrong Delivery Address or Phone Number
id: phy-incorrect-address
type: article
category: physical-products
subcategory: delivery
audience: buyer
priority: medium
department: fulfillment
features: physical-products, delivery-addis
tags: wrong address, change address, wrong phone number, update delivery address, address not found, landmark, አድራሻ ተሳስቷል, ስልክ ቁጥር ተሳስቷል, አድራሻ መቀየር
related: phy-delivery-delay, phy-how-to-order, phy-order-processing-status, phy-not-delivered-marked-delivered, phy-delivery-areas
templates: tpl-request-order-details
policy_pending: yes

## Summary
The buyer entered a wrong or incomplete delivery address or phone number, wants to change it, or the delivery person says they could not find the address.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products and Addis Ababa delivery are live.

Addresses in Addis Ababa are usually described by **landmarks** rather than street names and house numbers. A typical good address is: sub-city, woreda, neighbourhood name, a well-known landmark ("behind ... church", "opposite ... school", "near ... roundabout"), building name and floor, and a phone number that will be answered. Missing landmarks or an unreachable phone number are the most common reasons for failed deliveries.

This is **time-sensitive**: a change is easiest before the order is handed over for delivery. After handover, it may require coordination with the delivery team, and may not be possible.

## Possible Causes
- Typo in the phone number (missing digit, wrong prefix).
- Address too vague (only "Bole" or "near the main road").
- The buyer used an old address or a saved address from another order.
- The buyer is ordering for someone else and gave their own address or phone.
- Auto-fill on the phone filled wrong details.

## Information to Collect
- Order ID and registered email/phone (to verify the account holder)
- The corrected details: recipient name, phone number, sub-city, woreda, neighbourhood, landmark, building/floor
- An alternative phone number if available
- Whether the order is already marked shipped/out for delivery

> [!WARNING] Only change delivery details at the request of the **verified account holder**. Never ask for passwords, OTP codes or PINs to verify identity.

## Troubleshooting Steps
1. Verify the requester is the account holder (registered email/phone, order details they know).
2. Check the order status:
   - **Not yet handed over** → update the address if you have the tool, or ask the seller/fulfillment team to update it. Confirm the change is saved.
   - **Shipped / out for delivery** → contact **Logistics & Fulfillment** (or the seller, if self-delivering) immediately with the corrected details. Do not promise the change will be possible.
   - **Delivered to the wrong place** → treat as a delivery problem; follow *phy-not-delivered-marked-delivered*.
   - **Returned / failed delivery** → ask the fulfillment team about redelivery.
3. Read the corrected details back to the customer to confirm (especially the phone number, digit by digit).
4. Record old and new details in the internal notes.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for letting us know about the delivery details for order {{order_id}}.

To update them, please send me the correct information:
1. Name of the person receiving the order
2. A phone number that will be switched on (and an alternative number if possible)
3. Sub-city, woreda and neighbourhood
4. A clear landmark near you (for example a well-known building, church, mosque, school or shop) and the building name/floor if relevant

I will pass this to the team handling your order straight away. If the order is already on its way, we will do our best to update it, but I can't guarantee the change is possible at that stage.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ትዕዛዝ {{order_id}} የማድረሻ መረጃ ስላሳወቁን እናመሰግናለን።

መረጃውን ለማስተካከል እባክዎ ትክክለኛውን መረጃ ይላኩልኝ፦
1. ትዕዛዙን የሚቀበለው ሰው ስም
2. ክፍት የሚሆን ስልክ ቁጥር (ከተቻለ ተጨማሪ አማራጭ ቁጥር)
3. ክፍለ ከተማ፣ ወረዳ እና ሰፈር
4. በአቅራቢያዎ ያለ ግልጽ መለያ ምልክት (ለምሳሌ የታወቀ ሕንፃ፣ ቤተ ክርስቲያን፣ መስጊድ፣ ትምህርት ቤት ወይም ሱቅ) እና አስፈላጊ ከሆነ የሕንፃው ስም/ፎቅ

ትዕዛዝዎን ለሚያስተናግደው ቡድን ወዲያውኑ አስተላልፋለሁ። ትዕዛዙ አስቀድሞ በጉዞ ላይ ከሆነ ለማስተካከል የተቻለንን እናደርጋለን፤ ነገር ግን በዚያ ደረጃ ለውጡ እንደሚቻል ማረጋገጥ አልችልም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, please send the correct recipient name, a reachable phone number, sub-city, woreda, neighbourhood and a clear landmark for order {{order_id}}. I'll pass it on right away (changes may not be possible if it's already on the way). Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለትዕዛዝ {{order_id}} እባክዎ ትክክለኛውን የተቀባይ ስም፣ የሚደረስበት ስልክ፣ ክፍለ ከተማ፣ ወረዳ፣ ሰፈር እና ግልጽ መለያ ምልክት ይላኩ። ወዲያውኑ አስተላልፋለሁ (በጉዞ ላይ ከሆነ ለውጡ ላይቻል ይችላል)። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your corrected delivery details for order {{order_id}} have been shared with the team handling the delivery. [Confirmed updated / waiting for confirmation.] Please keep your phone switched on. We will update you by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለትዕዛዝ {{order_id}} የላኩት የተስተካከለ የማድረሻ መረጃ ማድረሱን ለሚያስተናግደው ቡድን ተላልፏል። [ተስተካክሏል / ማረጋገጫ እየጠበቅን ነው።] እባክዎ ስልክዎን ክፍት ያድርጉ። እስከ {{follow_up_time}} ድረስ መረጃ እንሰጥዎታለን።

## Escalation Conditions
- Order already out for delivery → **Logistics & Fulfillment** immediately.
- Request to change the address comes from someone who is not the verified account holder, or right after a suspicious login → **Trust & Safety** (possible account takeover redirecting goods).
- Buyer wants to change to an area outside the supported delivery area → **Logistics & Fulfillment**.
- Change cannot be made and the buyer wants to cancel → *phy-order-cancellation-buyer*.

## Resolution Procedure
1. Confirm the corrected details are saved on the order (or the fulfillment team confirmed them).
2. Confirm the order is later delivered, or record the alternative outcome.
3. Record old/new details and who made the change.

## Policy Pending Approval
- Confirm whether buyers can edit delivery details themselves, and until which order stage.
- Decide whether address changes after handover are allowed and whether extra fees apply.
- Confirm whether a structured address form with a landmark field will be used at checkout.

## Internal Notes
- Read phone numbers back digit by digit — typos are the top cause of "customer unreachable".
- **Fraud signal:** a new address in a different area, a different recipient name, plus a recent password or phone change on the account → possible account takeover; escalate before changing anything.
- Never share the buyer's address or phone with anyone other than the seller/delivery team handling the order.

<!-- doc -->
# Order Marked Delivered but Not Received
id: phy-not-delivered-marked-delivered
type: article
category: physical-products
subcategory: delivery
audience: buyer
priority: high
department: fulfillment
features: physical-products, delivery-addis
tags: marked delivered not received, never got my order, delivery person lied, package stolen, delivered to wrong person, proof of delivery, ደርሷል ይላል ግን አልደረሰኝም, ዕቃው አልደረሰኝም, ተሰርቋል
related: phy-delivery-delay, phy-incorrect-address, phy-missing-items, phy-seller-dispute, ref-evidence-collection, phy-tsg-order-problem-master
templates: tpl-request-order-details, tpl-order-status-check
policy_pending: yes

## Summary
The order shows as delivered, but the buyer says they never received it.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products and Addis Ababa delivery are live.

The system or the seller/delivery person marked the order as delivered, but the buyer says the parcel never reached them. This is **High priority**: the buyer has paid, money may be released to the seller, and it can involve theft or fraud by any party. Act quickly and neutrally — do not accuse the buyer, the seller or the delivery person.

## Possible Causes
- The parcel was handed to someone else at the address (family member, guard, neighbour, building reception, shop next door).
- Delivered to the wrong address or wrong building because of an unclear landmark.
- The status was marked "delivered" by mistake or in advance of the actual delivery.
- The delivery person did not deliver and marked it delivered (delivery-person fraud).
- The seller marked it delivered without sending it (seller fraud or error).
- The buyer received it but claims otherwise (buyer fraud — rare, but check history).

## Information to Collect
- Order ID, product, seller name
- Date and time the order was marked delivered (from the system)
- The delivery address and phone number on the order
- Whether the buyer received any call or message from the delivery person, and from which number
- Whether anyone else at the address (family, guard, reception, neighbours) could have received it
- Whether the buyer was asked for any code, signature or photo at delivery
- Any proof of delivery held by the delivery team or seller (photo, signature, recipient name, confirmation code, GPS — whatever the live process provides)

> [!WARNING] Never ask the buyer for passwords, OTP codes or PINs. If a delivery person asked the buyer for a verification code by phone, treat it as a possible scam.

## Troubleshooting Steps
1. Verify the buyer's identity and the order.
2. Note the exact time and who marked the order delivered (seller, delivery partner, system).
3. Ask the buyer to check with everyone who could have received it at the address (household, guard, neighbours, office reception) and to check for missed calls.
4. Request proof of delivery from **Logistics & Fulfillment** (or the seller, if self-delivering): recipient name, photo, signature or confirmation code, time and location of handover.
5. Compare: does the proof match the buyer's address and details?
6. Check for **fraud signals** (see Internal Notes). If present, escalate to **Trust & Safety** in parallel.
7. Ask Payments / Seller Operations to **hold the seller settlement** for this order while it is investigated, if that is possible in the system.
8. Give the buyer an honest update and a follow-up time. Do not promise a refund or replacement.

- [ ] Buyer checked with household/guard/neighbours
- [ ] Proof of delivery requested
- [ ] Fraud signals reviewed
- [ ] Settlement hold requested (if available)

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us, and I'm very sorry for the worry this is causing. I understand order {{order_id}} shows as delivered but you have not received it. We are treating this as a priority.

To help us investigate, please:
1. Check with anyone who might have received the parcel at your address (family members, guard, neighbours or reception)
2. Tell me whether you received any call or message from a delivery person, and from which number
3. Confirm the delivery address and phone number you used

We are also requesting the delivery record for your order. I will update you as soon as we have it.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን፤ ለፈጠረብዎት ስጋት ከልብ ይቅርታ እንጠይቃለን። ትዕዛዝ {{order_id}} እንደደረሰ ቢያሳይም እርስዎ እንዳልተቀበሉት ተረድቻለሁ። ይህንን ጉዳይ በቅድሚያ እየተከታተልነው ነው።

ለማጣራት እንዲረዳን፣ እባክዎ፦
1. በአድራሻዎ ጥቅሉን ሊቀበሉ የሚችሉ ሰዎችን (የቤተሰብ አባላት፣ ጥበቃ፣ ጎረቤቶች ወይም እንግዳ ተቀባይ) ይጠይቁ
2. ከአድራሹ ምንም ጥሪ ወይም መልዕክት ደርሶዎት እንደሆነ፣ ከደረሰዎትም ከየትኛው ቁጥር እንደሆነ ይንገሩኝ
3. የተጠቀሙትን የማድረሻ አድራሻ እና ስልክ ቁጥር ያረጋግጡልኝ

የትዕዛዝዎን የማድረሻ መዝገብም እየጠየቅን ነው። እንዳገኘነው ወዲያውኑ መረጃ እሰጥዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, so sorry — we're treating this as a priority. Please check with family/guard/neighbours, tell me if a delivery person called you (and from which number), and confirm your address and phone. We're requesting the delivery record. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ በጣም ይቅርታ — በቅድሚያ እየተከታተልነው ነው። እባክዎ ቤተሰብ/ጥበቃ/ጎረቤቶችን ይጠይቁ፣ አድራሹ ደውሎልዎት እንደሆነ (ከየትኛው ቁጥር) ይንገሩኝ፣ አድራሻና ስልክዎንም ያረጋግጡ። የማድረሻ መዝገቡን እየጠየቅን ነው። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}} for order {{order_id}}. We have requested the delivery record and our team is reviewing it together with the information you provided. Your case is being actively investigated, and we will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} (ትዕዛዝ {{order_id}}) የሚሰጥ መረጃ ነው። የማድረሻ መዝገቡን ጠይቀናል፤ ቡድናችን ከሰጡን መረጃ ጋር አብሮ እየመረመረው ነው። ጉዳይዎ በንቃት እየተጣራ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Always → **Logistics & Fulfillment** for proof of delivery (High priority).
- Fraud signals present (delivery person asked for a code/extra money, same delivery person in several complaints, proof of delivery looks fake) → **Trust & Safety** in parallel.
- Seller self-delivered and cannot show proof → **Senior Support / Supervisor** (buyer–seller dispute; see *phy-seller-dispute*).
- High-value item, or the buyer reports theft to police → **Senior Support / Supervisor**; **Management** for high-value or reputational cases.
- Seller settlement needs to be held → **Payments & Finance**.

## Resolution Procedure
1. Resolve when the parcel is found and received, or when an authorized decision (redelivery, refund, no action) is made and communicated.
2. Record: proof of delivery reviewed, statements from all parties, fraud signals checked, final decision and who approved it.

## Policy Pending Approval
- Define the official proof of delivery (photo, signature, confirmation code, recipient name) required from delivery partners and self-delivering sellers.
- Decide who is liable when delivery cannot be proven: seller, Byfluence or the delivery partner.
- Define the deadline for a buyer to report non-receipt after an order is marked delivered.
- Decide whether seller settlement is automatically held when a non-receipt claim is opened.

## Internal Notes
**Delivery-person fraud signals**
- Marked delivered with no call to the buyer, or at a time the buyer was clearly reachable at the address.
- Delivery person asked the buyer for an SMS code, PIN or "confirmation code" by phone without being at the door.
- Delivery person demanded extra cash or asked the buyer to pay outside Byfluence.
- The same delivery person appears in several non-receipt or missing-item complaints.

**Buyer-side signals** (check carefully, never accuse)
- Several non-receipt claims from the same buyer or address in a short period.
- Proof of delivery with a matching photo/signature from the buyer.

Stay neutral in every message; never say "the delivery person stole it" or "you must have received it".

<!-- doc -->
# Items Missing From the Order
id: phy-missing-items
type: article
category: physical-products
subcategory: order-problems
audience: buyer
priority: medium
department: support_l2
features: physical-products, delivery-addis
tags: missing item, incomplete order, part of order missing, only received one, empty box, short quantity, ዕቃ ጎድሏል, ያልተሟላ ትዕዛዝ, ባዶ ሳጥን
related: phy-damaged-product, phy-wrong-product, phy-not-delivered-marked-delivered, phy-seller-dispute, ref-evidence-collection, phy-tsg-order-problem-master
templates: tpl-request-screenshot, tpl-request-order-details
policy_pending: yes

## Summary
The buyer received the order, but one or more items, parts or accessories are missing, or the package arrived empty.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products and delivery are live.

Examples: ordered three items, received two; a phone arrived without the charger listed in the description; a set is incomplete; the box was empty. The key question is **where the item went missing**: never packed by the seller, removed in transit, or delivered separately. Evidence from both sides decides this.

## Possible Causes
- The seller forgot or chose not to pack an item (stock shortage).
- The order was split and the rest is coming separately.
- The package was opened or tampered with during delivery.
- The listing was unclear about what is included (e.g., accessories shown in photos but not included).
- The buyer misread the quantity or bundle.

## Information to Collect
- Order ID, product(s), quantity ordered vs received
- **Photos or a short video** of: the outer package as received (all sides), the shipping label with order details, the opened package and all contents laid out
- Whether the package was sealed, re-taped, torn or damaged on arrival
- Whether the buyer noticed anything at delivery (and whether they told the delivery person)
- Screenshot of the listing if the dispute is about what was included

> [!TIP] Ask the buyer to **keep all packaging** until the case is closed. Unboxing photos/videos are the strongest evidence.

## Troubleshooting Steps
1. Verify the order and compare items/quantity ordered with what the buyer says they received.
2. Check if the order was split or partially shipped.
3. Request the buyer's photos/video (see above).
4. Request the seller's **packing evidence** (photos of items packed, sealed parcel and label) and their packing record.
5. Check the listing description: was the missing part actually included in the offer?
6. Assess:
   - **Seller evidence shows item not packed / seller admits** → seller to send the missing item or follow the refund process.
   - **Package arrived tampered** → **Logistics & Fulfillment**; possible transit theft.
   - **Listing unclear** → treat as not-as-described; see *phy-product-complaint-quality*.
   - **Conflicting evidence** → *phy-seller-dispute* (Senior Support).
7. Do not promise a refund or replacement; explain the case is under review.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us, and I'm sorry that your order {{order_id}} arrived incomplete.

To look into this, please send:
1. Photos of the package as you received it (all sides) and the delivery label
2. A photo of everything that was inside the package
3. Which item(s) or parts are missing

Please keep the packaging and all items until we finish checking. We will also contact the seller about how the order was packed.

Your case number is {{ticket_id}}. I will update you as soon as we have reviewed the information.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን፤ ትዕዛዝዎ {{order_id}} ሳይሟላ በመድረሱ ይቅርታ እንጠይቃለን።

ጉዳዩን ለማጣራት እባክዎ የሚከተሉትን ይላኩ፦
1. ጥቅሉ ሲደርስዎ የነበረበትን ሁኔታ የሚያሳዩ ፎቶዎች (ከሁሉም አቅጣጫ) እና የማድረሻ መለያውን (label)
2. በጥቅሉ ውስጥ የነበረውን ነገር ሁሉ የሚያሳይ ፎቶ
3. የጎደሉትን ዕቃዎች ወይም ክፍሎች

ማጣራታችንን እስክንጨርስ ድረስ እባክዎ ማሸጊያውን እና ሁሉንም ዕቃዎች ያስቀምጡ። ትዕዛዙ እንዴት እንደታሸገም ሻጩን እንጠይቃለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። መረጃውን እንደገመገምን ወዲያውኑ መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry your order arrived incomplete. Please send photos of the package (all sides + label), everything inside, and tell me what's missing. Keep all packaging for now. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ትዕዛዝዎ ሳይሟላ በመድረሱ ይቅርታ። እባክዎ የጥቅሉን (ከሁሉም አቅጣጫ + መለያው)፣ በውስጡ የነበረውን ሁሉ ፎቶ ይላኩ፤ ምን እንደጎደለም ይንገሩኝ። ማሸጊያውን ለጊዜው ያስቀምጡ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have received your photos and asked the seller for their packing information for order {{order_id}}. The case is under review, and we will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ፎቶዎችዎን ተቀብለናል፤ ስለ ትዕዛዝ {{order_id}} አስተሻሸግ ሻጩን መረጃ ጠይቀናል። ጉዳዩ በግምገማ ላይ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Package arrived opened/re-taped or empty → **Logistics & Fulfillment** and **Trust & Safety** if theft is suspected.
- Seller and buyer evidence conflict → **Senior Support / Supervisor**.
- Buyer requests refund for the missing part → *phy-refund-request-product* (**Payments & Finance** after approval).
- Repeated missing-item complaints against the same seller → **Seller Operations**.

## Resolution Procedure
1. Resolve when the missing item is delivered, or an authorized refund/other decision is made and communicated.
2. Record evidence from both sides, assessment of where the item went missing, and the decision.

## Policy Pending Approval
- Define the deadline for reporting missing items after delivery.
- Decide who is responsible when packaging was tampered with in transit.
- Decide whether partial refunds are allowed for missing items, and who approves them.

## Internal Notes
- A sealed, untouched package + seller packing photo showing all items is strong evidence for the seller; a re-taped box points to transit.
- Empty-box claims are high risk — check buyer history and escalate to Trust & Safety if there is a pattern.
- Ask for photos, never for the buyer to send the remaining items back unless approved.

<!-- doc -->
# Product Arrived Damaged
id: phy-damaged-product
type: article
category: physical-products
subcategory: order-problems
audience: buyer
priority: medium
department: support_l2
features: physical-products, delivery-addis
tags: damaged item, broken product, cracked screen, crushed box, arrived broken, defective on arrival, ተሰብሮ ደረሰ, የተጎዳ ዕቃ, ተበላሽቷል
related: phy-missing-items, phy-wrong-product, phy-product-complaint-quality, phy-returns, phy-refund-request-product, ref-evidence-collection
templates: tpl-damaged-item-ack, tpl-request-screenshot
policy_pending: yes

## Summary
The buyer received a product that is physically damaged (broken, cracked, crushed, leaking, torn) or does not work on arrival.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products and delivery are live.

Damage can happen before packing (seller sent a damaged item), during delivery (poor handling, insufficient packaging), or after delivery. The agent's job is to collect clear evidence quickly while it is fresh, protect the buyer from further loss, and route the case — **not** to decide who pays.

## Possible Causes
- Item was already damaged or defective when the seller packed it.
- Insufficient packaging for a fragile item.
- Rough handling during delivery (drops, heavy items on top, rain).
- Manufacturing defect (dead on arrival electronics).
- Damage after delivery (buyer handling) — consider carefully before suggesting.

## Information to Collect
- Order ID, product, seller name, delivery date
- **Photos/video of the damage**, close-up and full item
- Photos of the **outer packaging** (all sides) and the **shipping label**, showing any dents, tears or wetness
- Photos of the inner packaging/padding
- For electronics: a short video showing the item does not power on/work
- Whether the damage was visible at delivery and whether the buyer refused or accepted the package

> [!TIP] Ask the buyer not to use, repair or throw away the item or packaging until the case is closed.

## Troubleshooting Steps
1. Verify the order and delivery date.
2. Send *tpl-damaged-item-ack* and request the evidence above.
3. Review the photos:
   - **Outer packaging damaged** → likely transit damage; inform **Logistics & Fulfillment**.
   - **Packaging intact, item damaged** → likely pre-packing damage or defect; contact the seller for packing evidence.
   - **Item works poorly but not physically damaged** → may be a quality/defect issue; see *phy-product-complaint-quality*.
4. Contact the seller with the evidence and ask for their packing photos.
5. Record findings and route to Senior Support for a decision (replacement, return, refund, or rejection) under the approved policy.
6. Do not tell the buyer to send the item back before a return is approved (see *phy-returns*).

## Recommended Response (EN)
Hello {{customer_name}},

I'm very sorry that {{product_name}} from order {{order_id}} arrived damaged. Thank you for letting us know.

To review this as quickly as possible, please send:
1. Clear photos or a short video of the damage
2. Photos of the outer package from all sides and the delivery label
3. If it is an electronic item, a short video showing the problem

Please keep the item and all packaging as they are, and do not repair or discard them until we finish reviewing. We will also contact the seller.

Your case number is {{ticket_id}}. I will update you once we have reviewed the information.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ከትዕዛዝ {{order_id}} የደረሰዎት {{product_name}} ተጎድቶ በመድረሱ በጣም ይቅርታ እንጠይቃለን። ስላሳወቁን እናመሰግናለን።

በተቻለ ፍጥነት ለመገምገም እባክዎ የሚከተሉትን ይላኩ፦
1. ጉዳቱን በግልጽ የሚያሳዩ ፎቶዎች ወይም አጭር ቪዲዮ
2. የውጭውን ጥቅል ከሁሉም አቅጣጫ እና የማድረሻ መለያውን (label) የሚያሳዩ ፎቶዎች
3. የኤሌክትሮኒክስ ዕቃ ከሆነ ችግሩን የሚያሳይ አጭር ቪዲዮ

ግምገማችንን እስክንጨርስ ድረስ እባክዎ ዕቃውንና ማሸጊያውን እንዳለ ያስቀምጡ፤ አያስጠግኑት ወይም አይጣሉት። ሻጩንም እናገኛለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። መረጃውን እንደገመገምን መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, so sorry {{product_name}} arrived damaged. Please send photos/video of the damage, the outer package (all sides) and the label. Keep the item and packaging as they are. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ {{product_name}} ተጎድቶ በመድረሱ በጣም ይቅርታ። እባክዎ የጉዳቱን፣ የውጭ ጥቅሉን (ከሁሉም አቅጣጫ) እና የመለያውን ፎቶ/ቪዲዮ ይላኩ። ዕቃውንና ማሸጊያውን እንዳለ ያስቀምጡ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have shared your photos with the seller and the team handling deliveries, and the case is under review for order {{order_id}}. Please continue to keep the item and packaging. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ፎቶዎችዎን ለሻጩ እና ማድረሱን ለሚያስተናግደው ቡድን አጋርተናል፤ የትዕዛዝ {{order_id}} ጉዳይ በግምገማ ላይ ነው። እባክዎ ዕቃውንና ማሸጊያውን ማስቀመጥዎን ይቀጥሉ። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Evidence suggests transit damage → **Logistics & Fulfillment**.
- Seller disputes the damage, or decision on replacement/refund needed → **Senior Support / Supervisor**.
- Damaged item is dangerous (leaking battery, broken glass, spoiled cosmetics) → tell the buyer to stop using it safely and escalate to **Senior Support** with priority High.
- High-value electronics → **Senior Support**; **Management** if the value or reputational risk is high.

## Resolution Procedure
1. Resolve when an authorized outcome (replacement, return, refund, or decline with reason) is completed and communicated.
2. Record evidence, likely damage stage (seller/transit/unknown), decision and approver.

## Policy Pending Approval
- Define the deadline for reporting damage after delivery.
- Decide who is liable for transit damage (seller, Byfluence or delivery partner), and for poor packaging.
- Decide whether buyers may refuse visibly damaged packages at the door.
- Decide minimum packaging standards for fragile categories.

## Internal Notes
- Photos taken days later in a different location are weaker evidence; ask when the photos were taken.
- Watch for re-used damage photos (same image from other tickets or the internet) → **Trust & Safety**.
- Never say "the delivery company will pay" or "the seller will replace it" before a decision.

<!-- doc -->
# Wrong Product Received
id: phy-wrong-product
type: article
category: physical-products
subcategory: order-problems
audience: buyer
priority: medium
department: support_l2
features: physical-products, delivery-addis
tags: wrong item, wrong size, wrong colour, different product, not what I ordered, someone else's order, የተሳሳተ ዕቃ, ያላዘዝኩት, የተለየ መጠን
related: phy-missing-items, phy-damaged-product, phy-returns, phy-counterfeit-misleading, phy-seller-dispute, ref-evidence-collection
templates: tpl-wrong-item-ack, tpl-request-screenshot
policy_pending: yes

## Summary
The buyer received a different product, size, colour or model from what they ordered, or a parcel meant for someone else.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products and delivery are live.

Wrong-item cases range from small variant errors (size 40 instead of 41) to completely different products or someone else's parcel. If the item is a cheaper or lower-quality version of what was advertised, it may also be a misleading-listing case (*phy-counterfeit-misleading*).

## Possible Causes
- Seller picked the wrong variant or product while packing.
- Parcels were swapped between orders (wrong label).
- The listing photos show a different model from what the seller actually sells.
- The buyer selected the wrong variant at checkout (check the order details first).

## Information to Collect
- Order ID, what was ordered (product, size, colour, model) and what was received
- Photos of the item received, including any brand/model/size tags
- Photo of the shipping label (to check if the parcel was for another order)
- Screenshot of the order details or listing as ordered
- Whether the item was used or tags removed

## Troubleshooting Steps
1. Open the order and confirm exactly what the buyer selected (variant, quantity). If the buyer chose the wrong variant, explain kindly and see *phy-returns*.
2. Send *tpl-wrong-item-ack* and collect photos.
3. Check the label: if it shows another buyer's name/order → contact **Logistics & Fulfillment** immediately (two buyers are likely affected).
4. Contact the seller with the evidence and ask for their packing record.
5. Route to Senior Support for the decision (exchange, return, refund) under approved policy.
6. Ask the buyer to keep the item unused with tags and packaging; do not ask them to return it until a return is approved.

## Recommended Response (EN)
Hello {{customer_name}},

I'm sorry you received the wrong item in order {{order_id}}. Thank you for letting us know.

To sort this out, please send:
1. Photos of the item you received, including any size, model or brand tags
2. A photo of the delivery label on the package
3. What you expected to receive (or a screenshot of your order)

Please keep the item unused, with its tags and packaging, until we confirm the next steps. We are contacting the seller now.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

በትዕዛዝ {{order_id}} የተሳሳተ ዕቃ ስለደረሰዎት ይቅርታ እንጠይቃለን። ስላሳወቁን እናመሰግናለን።

ይህንን ለማስተካከል እባክዎ የሚከተሉትን ይላኩ፦
1. የደረሰዎትን ዕቃ ፎቶዎች፣ የመጠን፣ የሞዴል ወይም የብራንድ መለያዎችን ጨምሮ
2. በጥቅሉ ላይ ያለውን የማድረሻ መለያ (label) ፎቶ
3. እንዲደርስዎ የጠበቁትን (ወይም የትዕዛዝዎን ስክሪንሾት)

ቀጣዩን እርምጃ እስክናረጋግጥ ድረስ እባክዎ ዕቃውን ሳይጠቀሙበት ከመለያዎቹና ከማሸጊያው ጋር ያስቀምጡት። ሻጩን አሁን እያገኘነው ነው።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry you got the wrong item. Please send photos of what you received (with tags), the delivery label, and what you ordered. Keep it unused with tags for now. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የተሳሳተ ዕቃ ስለደረሰዎት ይቅርታ። እባክዎ የደረሰዎትን (ከመለያዎቹ ጋር)፣ የማድረሻ መለያውን እና ያዘዙትን የሚያሳዩ ፎቶዎች ይላኩ። ለጊዜው ሳይጠቀሙበት ከመለያዎቹ ጋር ያስቀምጡት። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have contacted the seller about the item you received for order {{order_id}} and are waiting for their response. We will contact you again by {{follow_up_time}} with the next steps.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለትዕዛዝ {{order_id}} ስለደረሰዎት ዕቃ ሻጩን አግኝተናል፤ ምላሻቸውን እየጠበቅን ነው። ቀጣዩን እርምጃ ይዘን እስከ {{follow_up_time}} ድረስ እናገኝዎታለን።

## Escalation Conditions
- Label shows another buyer's order (swapped parcels) → **Logistics & Fulfillment**, High priority.
- Seller refuses to correct the error or evidence conflicts → **Senior Support / Supervisor**.
- Item received appears counterfeit or substantially different from the listing → *phy-counterfeit-misleading* (**Trust & Safety**).
- Same seller repeatedly sends wrong items → **Seller Operations**.

## Resolution Procedure
1. Resolve when the correct item is received, or an approved return/refund is completed.
2. Record what was ordered vs received, cause (seller error, swap, buyer selection) and outcome.

## Policy Pending Approval
- Decide whether an exchange, return or refund is the default remedy for wrong items, and who pays return delivery.
- Define the reporting deadline for wrong items.
- Decide how swapped parcels between two buyers are handled.

## Internal Notes
- Always check the order variant first — a polite "the order shows size 40 was selected" avoids blaming the seller wrongly.
- Do not let the buyer and seller arrange private exchanges with cash payments outside Byfluence.

<!-- doc -->
# Counterfeit or Misleading Product
id: phy-counterfeit-misleading
type: article
category: physical-products
subcategory: order-problems
audience: buyer
priority: high
department: trust_safety
features: physical-products
tags: fake product, counterfeit, not original, replica, misleading listing, fake brand, ፎርጅድ, ኦሪጅናል አይደለም, ሀሰተኛ ምርት, አሳሳች
related: tns-fake-products, tns-intellectual-property, phy-wrong-product, phy-product-complaint-quality, phy-seller-dispute, ref-evidence-collection
templates: tpl-request-screenshot, tpl-request-order-details
policy_pending: yes

## Summary
The buyer believes the product they received is counterfeit, or that the listing misrepresented the product (brand, originality, condition, specifications).

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products are live.

Counterfeit and misleading listings damage buyer trust and can create legal risk. Typical reports: a "original" phone or perfume that appears fake, a "new" item that is clearly used, specifications far below what was advertised, photos copied from a brand's website. **Support does not decide whether an item is legally counterfeit.** We record a "reported concern", protect evidence, and escalate to **Trust & Safety**.

## Possible Causes
- The seller knowingly sells counterfeit or replica items as original.
- The seller is unaware their supplier sells fakes.
- The listing uses stock photos from the brand, so the item looks different.
- The item is genuine but from a different region/version, and the buyer is unfamiliar with it.
- Condition (new vs refurbished/used) was not disclosed.

## Information to Collect
- Order ID, product and seller name
- Screenshot or link of the listing as it was when ordered (claims like "original", "new", specifications)
- Photos of the item received: logos, labels, serial number/IMEI area, packaging, any certificates
- Why the buyer believes it is fake/misleading (e.g., comparison with an original, failed serial check)
- Any messages where the seller made claims about originality

## Troubleshooting Steps
1. Verify the order.
2. Collect the evidence above. Save copies in the ticket (listings can be edited later).
3. Check whether the listing still exists and what it claims now.
4. Check for other complaints against the same seller or listing.
5. Escalate to **Trust & Safety** with all evidence. Trust & Safety decides on listing removal and seller action.
6. Treat the buyer's refund/return request through *phy-refund-request-product* after Trust & Safety input.
7. Tell the buyer we are reviewing the report — never say "the item is fake" or "the seller is a fraud".

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for reporting this. I understand you are concerned that {{product_name}} from order {{order_id}} is not genuine or not as described, and we take reports like this seriously.

To review it, please send:
1. Clear photos of the item, its labels, logos, packaging and any serial number area
2. A screenshot of the listing or any messages where the seller described the product
3. A short explanation of what is different from what was advertised

Please keep the item and its packaging as they are. Your report will be reviewed by our specialist team.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ይህንን ስላሳወቁን እናመሰግናለን። ከትዕዛዝ {{order_id}} የደረሰዎት {{product_name}} ትክክለኛ (ኦሪጅናል) ወይም እንደተገለጸው እንዳልሆነ ስጋት እንዳለዎት ተረድቻለሁ፤ እንደዚህ ያሉ ሪፖርቶችን በቁም ነገር እንመለከታቸዋለን።

ለመገምገም እባክዎ የሚከተሉትን ይላኩ፦
1. የዕቃውን፣ የመለያዎቹን፣ የአርማዎቹን፣ የማሸጊያውን እና የሲሪያል ቁጥሩ ያለበትን ቦታ በግልጽ የሚያሳዩ ፎቶዎች
2. የዝርዝሩን (listing) ወይም ሻጩ ምርቱን የገለጸበትን መልዕክት ስክሪንሾት
3. ከማስታወቂያው የተለየውን ነገር የሚገልጽ አጭር ማብራሪያ

እባክዎ ዕቃውንና ማሸጊያውን እንዳለ ያስቀምጡ። ሪፖርትዎ በልዩ ቡድናችን ይገመገማል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for reporting this — we take it seriously. Please send photos of the item, labels, packaging and serial area, plus a screenshot of the listing or seller's claims. Keep everything as it is. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን — በቁም ነገር እንመለከተዋለን። እባክዎ የዕቃውን፣ የመለያዎቹን፣ የማሸጊያውን እና የሲሪያል ቦታውን ፎቶ እንዲሁም የዝርዝሩን ወይም የሻጩን መግለጫ ስክሪንሾት ይላኩ። ሁሉንም እንዳለ ያስቀምጡ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your report about order {{order_id}} is being reviewed by our Trust & Safety team. We will contact you again by {{follow_up_time}}. Thank you for helping keep Byfluence safe.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ስለ ትዕዛዝ {{order_id}} ያቀረቡት ሪፖርት በእምነትና ደህንነት (Trust & Safety) ቡድናችን እየተገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። Byfluenceን ደህንነቱ የተጠበቀ ለማድረግ ስለረዱን እናመሰግናለን።

## Escalation Conditions
- All counterfeit/misleading reports → **Trust & Safety** (High).
- Brand owner or their representative reports counterfeits → **Trust & Safety**; **Management** for legal matters (see *tns-intellectual-property*).
- Health/safety risk (fake cosmetics, chargers, medicines) → **Trust & Safety**, Critical; advise the buyer to stop using it.
- Buyer wants a refund → *phy-refund-request-product* after Trust & Safety review.

## Resolution Procedure
1. Resolve after Trust & Safety has reviewed and the buyer outcome (refund/return/decline) is decided and communicated.
2. Record evidence, listing snapshot, Trust & Safety reference and decision.

## Policy Pending Approval
- Define Byfluence's counterfeit policy: prohibited items, seller penalties, and buyer remedies.
- Decide whether buyers must return suspected counterfeit items, and who pays return delivery.
- Confirm the process for brand-owner complaints and legal requests.

## Internal Notes
- Never use the words "fake" or "fraud" about a seller in customer messages; use "reported concern".
- Screenshot the listing immediately — sellers sometimes edit "original" out after a complaint.
- Serial number/IMEI photos may contain unique identifiers; store them only in the ticket, never in public channels.
