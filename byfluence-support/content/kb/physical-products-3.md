<!-- doc -->
# Product Quality Complaint
id: phy-product-complaint-quality
type: article
category: physical-products
subcategory: order-problems
audience: buyer
priority: medium
department: support_l2
features: physical-products
tags: poor quality, not as described, stopped working, low quality, defective, doesn't fit, cheap material, ጥራቱ ዝቅተኛ ነው, እንደተገለጸው አይደለም, ተበላሸ
related: phy-damaged-product, phy-counterfeit-misleading, phy-product-description-questions, phy-returns, phy-refund-request-product, phy-seller-dispute
templates: tpl-request-screenshot, tpl-request-order-details
policy_pending: yes

## Summary
The buyer is unhappy with the quality of a product they received: it is not as described, stopped working, is defective, or is lower quality than expected.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products are live.

Separate the complaint into one of four types — each is handled differently:
| Type | Example | Route |
|---|---|---|
| **Not as described** | Listing says leather, item is plastic; listing says 128GB, item is 64GB | Seller error or misleading listing → Senior Support; if deliberate → *phy-counterfeit-misleading* |
| **Defective** | Stops working after first use; stitching comes apart immediately | Seller responsibility / warranty question → Senior Support |
| **Damaged on arrival** | Cracked, broken | *phy-damaged-product* |
| **Expectation / preference** | "I don't like the colour", "looks smaller than I thought" though it matches the listing | Not a defect → *phy-returns* (change-of-mind rules pending) |

Warranty terms are offered by sellers/manufacturers, if at all. Byfluence warranty rules are **not confirmed** — do not promise repair or replacement under warranty.

## Possible Causes
- Listing description or photos were inaccurate or exaggerated.
- Manufacturing defect.
- Product misuse or incompatible use (e.g., wrong charger).
- Buyer expectation differs from what was listed.

## Information to Collect
- Order ID, product, seller name, date received
- Photos/video showing the quality problem or defect
- Screenshot of the listing claim the item does not meet
- When the problem started and how the item was used
- What the buyer would like (exchange, repair, refund) — record it, do not promise it

## Troubleshooting Steps
1. Verify the order and delivery date.
2. Classify the complaint using the table above.
3. Compare the evidence with the listing description and photos.
4. Contact the seller with the evidence and ask for their response and any warranty they offer.
5. If the seller offers a solution acceptable to the buyer (e.g., exchange), record it clearly on the ticket and follow up until completed.
6. If not, route to Senior Support for a decision under approved policy (*phy-refund-request-product*, *phy-returns*).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for telling us about the problem with {{product_name}} from order {{order_id}}. I'm sorry it has not met your expectations.

To review this, please send:
1. Photos or a short video showing the problem
2. A screenshot of the part of the listing that the product does not match, if relevant
3. When you first noticed the problem

We will share this with the seller and review the case. Please keep the item and its packaging for now.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ከትዕዛዝ {{order_id}} ስለደረሰዎት {{product_name}} ችግር ስላሳወቁን እናመሰግናለን። ምርቱ እንደጠበቁት ባለመሆኑ ይቅርታ እንጠይቃለን።

ጉዳዩን ለመገምገም እባክዎ የሚከተሉትን ይላኩ፦
1. ችግሩን የሚያሳዩ ፎቶዎች ወይም አጭር ቪዲዮ
2. አስፈላጊ ከሆነ፣ ምርቱ የማይመሳሰልበትን የዝርዝሩን ክፍል የሚያሳይ ስክሪንሾት
3. ችግሩን መጀመሪያ ያስተዋሉበትን ጊዜ

ይህንን ለሻጩ አጋርተን ጉዳዩን እንገመግማለን። ለጊዜው እባክዎ ዕቃውንና ማሸጊያውን ያስቀምጡ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry {{product_name}} isn't as expected. Please send photos/video of the problem, a screenshot of the listing detail it doesn't match, and when it started. Keep the item and packaging. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ {{product_name}} እንደጠበቁት ባለመሆኑ ይቅርታ። እባክዎ የችግሩን ፎቶ/ቪዲዮ፣ የማይመሳሰልበትን የዝርዝሩን ስክሪንሾት እና መቼ እንደጀመረ ይላኩ። ዕቃውንና ማሸጊያውን ያስቀምጡ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We have shared your information about order {{order_id}} with the seller and the case is under review. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ስለ ትዕዛዝ {{order_id}} የላኩትን መረጃ ለሻጩ አጋርተናል፤ ጉዳዩ በግምገማ ላይ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Seller rejects the complaint and the buyer disagrees → **Senior Support / Supervisor** (*phy-seller-dispute*).
- Listing appears deliberately misleading → **Trust & Safety**.
- Product poses a safety risk (overheating electronics, skin reaction to cosmetics) → **Trust & Safety**, High; advise the buyer to stop using it.
- Repeated quality complaints against the same seller or listing → **Seller Operations**.

## Resolution Procedure
1. Resolve when the agreed/approved outcome is completed and the buyer is informed.
2. Record complaint type, evidence, seller response and outcome.

## Policy Pending Approval
- Decide whether Byfluence requires sellers to offer any minimum guarantee for defects.
- Define the time window for quality complaints after delivery.
- Decide whether "change of mind" returns are allowed at all (see *phy-returns*).

## Internal Notes
- Be careful with expectation complaints: if the product matches the listing, explain kindly that it is not a defect and check the returns rules.
- Ask open questions about how the item was used before suggesting misuse — never accuse the buyer.

<!-- doc -->
# Buyer Wants to Cancel an Order
id: phy-order-cancellation-buyer
type: article
category: physical-products
subcategory: cancellations-returns
audience: buyer
priority: medium
department: support_l2
features: physical-products, delivery-addis
tags: cancel order, cancel my order, changed my mind, ordered by mistake, stop order, cancel before delivery, ትዕዛዝ መሰረዝ, መሰረዝ እፈልጋለሁ, በስህተት አዘዝኩ
related: phy-order-cancellation-seller, phy-refund-request-product, phy-delivery-delay, phy-returns, ref-product-refunds
templates: tpl-order-cancellation-ack, tpl-request-order-details
policy_pending: yes

## Summary
A buyer asks to cancel a physical product order they have placed (and usually paid for).

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products are live.

Cancellation rules for physical products are **not yet approved**. The practical difference is the order stage:
- **Before the seller prepares/hands over the order** — cancellation is usually simplest.
- **After handover to delivery** — may not be possible to stop; it may become a return.
- **After delivery** — this is a return, not a cancellation (*phy-returns*).

Common reasons: ordered by mistake, duplicate order, found it cheaper, delivery taking too long, address problem, changed mind.

## Possible Causes
- Buyer error (wrong item/variant/quantity, duplicate order).
- Delivery delay or poor seller communication.
- Payment issues (charged twice — see *pay-duplicate-charge*).
- Change of mind.

## Information to Collect
- Order ID, product, seller name
- Reason for cancellation
- Payment status and method (for the refund process)
- Whether the buyer has already been contacted by a delivery person

## Troubleshooting Steps
1. Verify the account holder and the order.
2. Check the order status:
   - **Pending payment** → the buyer can usually just not complete payment; confirm no money was taken.
   - **Confirmed / processing (not handed over)** → use the cancellation option if available to you, or ask the seller to cancel immediately. Notify Seller Operations if the seller does not respond.
   - **Shipped / out for delivery** → contact **Logistics & Fulfillment** to see whether it can be stopped; do not promise.
   - **Delivered** → move to *phy-returns*.
3. If the reason is a delay or seller problem, note it — this may affect how management treats the refund.
4. If cancelled and paid, open the refund process (*phy-refund-request-product*) and send *tpl-order-cancellation-ack*.
5. Never promise a full refund, a refund amount or a refund date.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us about cancelling order {{order_id}}.

I have checked the order and submitted your cancellation request. Whether it can be cancelled depends on how far the order has progressed — for example, if it has already been handed over for delivery, it may not be possible to stop it.

If the cancellation is confirmed and you have already paid, your refund request will be reviewed under our refund process. I will update you on both the cancellation and any refund.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ትዕዛዝ {{order_id}}ን ስለመሰረዝ ስላገኙን እናመሰግናለን።

ትዕዛዙን አጣርቼ የመሰረዝ ጥያቄዎን አስገብቻለሁ። መሰረዝ መቻሉ ትዕዛዙ በደረሰበት ደረጃ ላይ ይወሰናል — ለምሳሌ ለማድረስ አስቀድሞ ተሰጥቶ ከሆነ ማቆም ላይቻል ይችላል።

መሰረዙ ከተረጋገጠ እና አስቀድመው ከፍለው ከሆነ፣ የተመላሽ ገንዘብ ጥያቄዎ በተመላሽ ገንዘብ ሂደታችን መሰረት ይገመገማል። ስለ መሰረዙም ሆነ ስለ ተመላሽ ገንዘቡ መረጃ እሰጥዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I've submitted a cancellation request for order {{order_id}}. If it's already out for delivery it may not be possible to stop. If cancelled and paid, your refund will be reviewed. I'll update you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለትዕዛዝ {{order_id}} የመሰረዝ ጥያቄ አስገብቻለሁ። አስቀድሞ ለማድረስ ከወጣ ማቆም ላይቻል ይችላል። ከተሰረዘና ከከፈሉ ተመላሽ ገንዘብዎ ይገመገማል። መረጃ እሰጥዎታለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. The cancellation of order {{order_id}} is [confirmed / still being checked with the seller / not possible because the order was already delivered]. [Refund status if relevant.] We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የትዕዛዝ {{order_id}} መሰረዝ [ተረጋግጧል / ከሻጩ ጋር እየተጣራ ነው / ትዕዛዙ አስቀድሞ ስለደረሰ አልተቻለም]። [አስፈላጊ ከሆነ የተመላሽ ገንዘብ ሁኔታ።] እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Seller refuses or does not respond to a cancellation before handover → **Senior Support / Supervisor**.
- Order already with delivery → **Logistics & Fulfillment**.
- Paid order cancelled → **Payments & Finance** for refund processing after approval.
- Buyer cancels because of suspected fraud by the seller → **Trust & Safety**.

## Resolution Procedure
1. Confirm the order shows as cancelled (or the outcome if cancellation was not possible).
2. Confirm a refund case was opened where payment was taken.
3. Record cancellation reason, stage at cancellation and outcome.

## Policy Pending Approval
- Define until which order stage buyers may cancel, and whether they can cancel themselves.
- Decide whether any fees (delivery, payment processing) are deducted when a buyer cancels.
- Decide refund approval authority for cancelled orders.

## Internal Notes
- Replace bracketed text before sending follow-ups.
- Speed matters: a cancellation request sitting in the queue may become an unstoppable delivery.
- If the buyer cancels because of a duplicate order, check for a duplicate payment too.

<!-- doc -->
# Seller Cancelled the Order
id: phy-order-cancellation-seller
type: article
category: physical-products
subcategory: cancellations-returns
audience: both
priority: medium
department: support_l2
features: physical-products
tags: seller cancelled order, order cancelled by seller, why was my order cancelled, seller out of stock cancel, seller cancel, ሻጩ ትዕዛዜን ሰረዘ, ትዕዛዜ ተሰርዟል, ለምን ተሰረዘ
related: phy-product-availability, phy-order-cancellation-buyer, phy-refund-request-product, phy-seller-order-management, ref-product-refunds
templates: tpl-order-cancellation-ack, tpl-refund-request-ack
policy_pending: yes

## Summary
A buyer's order was cancelled by the seller, or a seller asks how and when they may cancel an order.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products are live.

**Buyer side:** the buyer sees their order cancelled and wants to know why and what happens to their money. **Seller side:** the seller cannot fulfil (out of stock, price error, cannot deliver to the area) and wants to cancel.

Seller-initiated cancellation rules (allowed reasons, penalties, refund handling) are **not yet approved**.

## Possible Causes
- Item out of stock or listing quantity incorrect.
- Pricing mistake on the listing.
- Seller cannot deliver to the buyer's area or cannot reach the buyer.
- Seller suspected the order was fraudulent.
- Seller account was suspended and orders were cancelled.
- Seller wants to sell the item to the buyer at a higher price or outside Byfluence (fraud signal).

## Information to Collect
- Order ID, product, seller name
- Date of cancellation and reason shown (if any)
- Payment status and method
- For buyers: any messages from the seller about the cancellation
- For sellers: reason for cancelling

## Troubleshooting Steps
1. Find the order, the cancellation time, who cancelled and the reason recorded.
2. Check the payment status. If paid, confirm whether a refund was triggered automatically or a refund case is needed (*phy-refund-request-product*).
3. **Buyer:** explain the reason (if the seller recorded one) in neutral terms, and the refund next step.
4. **Seller asking to cancel:** ask for the reason; tell them to cancel through the official option **as early as possible** and inform the buyer; remind them to update the listing stock.
5. Check the seller's cancellation history. Frequent cancellations → note for Seller Operations.
6. If the seller asked the buyer to pay more or pay outside Byfluence → Trust & Safety.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us, and I'm sorry that your order {{order_id}} for {{product_name}} was cancelled by the seller.

I have checked the order: [reason recorded by the seller, if any]. Since you had already paid, your case has been passed to our team for a refund review. I will keep you updated on its progress.

Please do not make any payment to the seller outside Byfluence, even if you are asked to.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስላገኙን እናመሰግናለን፤ ለ{{product_name}} ያስገቡት ትዕዛዝ {{order_id}} በሻጩ በመሰረዙ ይቅርታ እንጠይቃለን።

ትዕዛዙን አጣርቻለሁ፦ [ሻጩ የመዘገበው ምክንያት፣ ካለ]። አስቀድመው ከፍለው ስለነበር ጉዳይዎ ለተመላሽ ገንዘብ ግምገማ ለቡድናችን ተላልፏል። ስለ ሂደቱ መረጃ እሰጥዎታለሁ።

ቢጠየቁም እንኳ እባክዎ ከ Byfluence ውጭ ለሻጩ ምንም ክፍያ አይፈጽሙ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry the seller cancelled order {{order_id}}. Since you paid, it has been passed for refund review and I'll update you. Please don't pay the seller outside Byfluence. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ሻጩ ትዕዛዝ {{order_id}}ን በመሰረዙ ይቅርታ። ስለከፈሉ ለተመላሽ ገንዘብ ግምገማ ተላልፏል፤ መረጃ እሰጥዎታለሁ። እባክዎ ከ Byfluence ውጭ ለሻጩ አይክፈሉ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. The refund review for cancelled order {{order_id}} is in progress with our payments team. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለተሰረዘው ትዕዛዝ {{order_id}} የተመላሽ ገንዘብ ግምገማ በክፍያ ቡድናችን እየተካሄደ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Paid order cancelled → **Payments & Finance** for refund processing (after approval where required).
- Seller asked the buyer to pay extra or outside Byfluence → **Trust & Safety**.
- Seller has a pattern of cancellations → **Seller Operations**.
- Cancellation caused by a seller suspension → **Seller Operations** to handle remaining orders.

## Resolution Procedure
1. Confirm the refund case is open (or completed) for paid orders.
2. Record who cancelled, reason, payment status and refund case reference.

## Policy Pending Approval
- Define acceptable reasons for seller cancellations and any penalties.
- Decide whether refunds for seller-cancelled orders are automatic and full.
- Decide whether pricing-error cancellations are allowed after payment.

## Internal Notes
- Replace the bracketed reason before sending; if no reason is recorded, say "the seller was unable to fulfil the order".
- **Fraud pattern:** seller cancels, then messages the buyer offering the same item "directly" for cash — always escalate.

<!-- doc -->
# Returning a Product
id: phy-returns
type: article
category: physical-products
subcategory: cancellations-returns
audience: buyer
priority: medium
department: support_l2
features: physical-products, delivery-addis
tags: return product, return item, send back, exchange, return policy, change size, ዕቃ መመለስ, መቀየር, የመመለሻ ፖሊሲ
related: phy-refund-request-product, phy-damaged-product, phy-wrong-product, phy-product-complaint-quality, phy-order-cancellation-buyer, ref-product-refunds
templates: tpl-request-order-details, tpl-request-screenshot
policy_pending: yes

## Summary
A buyer wants to return or exchange a physical product after delivery.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products and delivery are live.

**Byfluence's return policy is not yet established.** Return eligibility, time limits, condition requirements, who pays return delivery and how items are collected must all be decided by management. Support collects the request and evidence, and routes it for a decision — **never tell a buyer to send an item back until a return is approved and a method is given**.

Return reasons usually fall into:
- Seller fault: damaged, wrong item, missing parts, defective, not as described (see the specific articles).
- Buyer preference: wrong size chosen, changed mind, didn't like it.

## Possible Causes
- Product problem (seller or transit fault).
- Size/fit issues, especially clothing and shoes.
- Change of mind.

## Information to Collect
- Order ID, product, seller name, delivery date
- Reason for return
- Condition of the item: unused, tags attached, original packaging
- Photos of the item and packaging
- What the buyer wants: exchange (which size/colour) or refund

## Troubleshooting Steps
1. Verify the order and delivery date.
2. Identify the reason. For seller-fault reasons, follow the specific article (*phy-damaged-product*, *phy-wrong-product*, *phy-missing-items*, *phy-product-complaint-quality*).
3. For preference returns, record the request and check whether the seller's listing states any return terms.
4. Collect photos of the item's condition.
5. Contact the seller and ask whether they accept the return/exchange.
6. Route to **Senior Support** for a decision under approved policy; coordinate collection with **Logistics & Fulfillment** only after approval.
7. Once approved, give the buyer exact instructions from the approved process.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us about returning {{product_name}} from order {{order_id}}.

I have recorded your return request. To review it, please send:
1. The reason for the return
2. Photos of the item and its packaging, showing its current condition (tags attached if possible)
3. Whether you would prefer an exchange or a refund

Please do not send the item anywhere yet — once your request is reviewed, we will tell you whether it is approved and exactly how the return would work.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ከትዕዛዝ {{order_id}} የደረሰዎትን {{product_name}} ስለመመለስ ስላገኙን እናመሰግናለን።

የመመለሻ ጥያቄዎን መዝግቤያለሁ። ለመገምገም እባክዎ የሚከተሉትን ይላኩ፦
1. ዕቃውን ለመመለስ የፈለጉበትን ምክንያት
2. የዕቃውንና የማሸጊያውን አሁን ያለበትን ሁኔታ የሚያሳዩ ፎቶዎች (ከተቻለ መለያዎቹ እንዳሉ)
3. መቀየር ወይም ተመላሽ ገንዘብ — የትኛውን እንደሚመርጡ

እባክዎ ዕቃውን እስካሁን ወደየትም አይላኩ — ጥያቄዎ ከተገመገመ በኋላ መጽደቁን እና መመለሱ በትክክል እንዴት እንደሚከናወን እናሳውቅዎታለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I've recorded your return request for order {{order_id}}. Please send the reason, photos of the item and packaging, and whether you want an exchange or refund. Don't send the item anywhere yet. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለትዕዛዝ {{order_id}} የመመለሻ ጥያቄዎን መዝግቤያለሁ። እባክዎ ምክንያቱን፣ የዕቃውንና የማሸጊያውን ፎቶ እንዲሁም መቀየር ወይም ተመላሽ ገንዘብ እንደሚፈልጉ ይላኩ። ዕቃውን እስካሁን አይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your return request for order {{order_id}} is being reviewed with the seller. Please keep the item in its current condition. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለትዕዛዝ {{order_id}} ያቀረቡት የመመለሻ ጥያቄ ከሻጩ ጋር እየተገመገመ ነው። እባክዎ ዕቃውን አሁን ባለበት ሁኔታ ያስቀምጡ። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every return decision → **Senior Support / Supervisor** (until a policy allows L1 approval).
- Approved return needing collection → **Logistics & Fulfillment**.
- Approved refund after return → **Payments & Finance**.
- Seller and buyer disagree about the item's condition → *phy-seller-dispute*.

## Resolution Procedure
1. Resolve when the return/exchange is completed (item received by the seller and replacement/refund done), or the request is declined with an explanation.
2. Record reason, condition evidence, seller response, decision, approver and logistics reference.

## Policy Pending Approval
- Define Byfluence's return policy: eligible reasons, time window, condition requirements, non-returnable categories (e.g., underwear, cosmetics once opened).
- Decide who pays return delivery for seller-fault vs preference returns.
- Define how returned items are collected and how receipt is confirmed.
- Decide whether sellers can set stricter or more generous return terms on their listings.

## Internal Notes
- The most common mistake is telling a buyer to "just send it back to the seller" — items get lost and nobody can prove they were returned.
- Hygiene-sensitive items may never be returnable; do not promise until policy exists.

<!-- doc -->
# Refund Request for a Physical Product
id: phy-refund-request-product
type: article
category: physical-products
subcategory: cancellations-returns
audience: buyer
priority: medium
department: payments
features: physical-products, refunds
tags: refund product, money back, refund for order, when will I get my money, refund status order, ገንዘቤ ይመለስልኝ, ተመላሽ ገንዘብ, ትዕዛዝ ተመላሽ
related: ref-product-refunds, phy-returns, phy-order-cancellation-buyer, phy-order-cancellation-seller, ref-evidence-collection, pay-duplicate-charge
templates: tpl-refund-request-ack, tpl-request-order-details
policy_pending: yes

## Summary
A buyer asks for a refund for a physical product order (cancelled, not delivered, damaged, wrong, missing or not as described), or asks about the status of a refund.

## Issue Description
> [!WARNING] **Planned features.** Physical products are planned and refund processing is **unconfirmed**. Check the **Feature Status** page before discussing refunds as an available process.

Refund eligibility, deadlines, deductions and approval authority **must be set by official policy and are not yet established.** Support's role is the confirmed workflow: complaint → identify transaction → collect evidence → review policy → contact seller/department → authorized personnel decide → explain to customer → process approved adjustments → document and close.

See *ref-product-refunds* for the cross-category refund rules once they are approved.

## Possible Causes
Typical refund reasons:
- Order cancelled (by buyer or seller) after payment.
- Order not delivered / marked delivered but not received.
- Damaged, wrong, missing or counterfeit item.
- Not as described or defective.
- Duplicate payment (see *pay-duplicate-charge*).

## Information to Collect
- Order ID, product, seller name
- Transaction reference, payment method, amount and date
- Reason for refund and the related evidence (photos, screenshots)
- Whether the item has been received, and its condition
- Whether a return was requested or approved

> [!WARNING] Never ask for passwords, OTP codes, PINs or full card numbers. To process a refund to mobile money or a bank, use only the details Payments asks for under the approved procedure.

## Troubleshooting Steps
1. Verify the account holder, order and payment (by transaction reference in the admin dashboard).
2. Check the payment status: Successful, Refund Pending, Refunded, Disputed.
   - **Refund Pending / Refunded already** → tell the buyer the current status; do not open a second request.
3. Identify the reason and make sure the evidence is collected per the specific article.
4. Contact the seller for their response where relevant.
5. Submit the case to the authorized reviewer (Senior Support / Payments) with all evidence. Send *tpl-refund-request-ack*.
6. After a decision, explain it to the buyer and, if approved, ask Payments to process it.
7. Never promise approval, amount, method or timing.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting us about a refund for order {{order_id}}. I'm sorry for the trouble with this order.

I have submitted your refund request, together with the information you provided, for review by our team. Refund decisions are made by our authorized team after checking the order, the payment and the details from the seller. I will keep you updated on the outcome.

If you have any photos or screenshots related to the problem that you haven't sent yet, please share them here.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ለትዕዛዝ {{order_id}} ተመላሽ ገንዘብ ለመጠየቅ ስላገኙን እናመሰግናለን። በዚህ ትዕዛዝ ላይ ለገጠመዎት ችግር ይቅርታ እንጠይቃለን።

የተመላሽ ገንዘብ ጥያቄዎን ከሰጡን መረጃ ጋር ለቡድናችን ግምገማ አስገብቻለሁ። የተመላሽ ገንዘብ ውሳኔዎች የሚሰጡት ትዕዛዙን፣ ክፍያውን እና ከሻጩ የተገኘውን መረጃ ካጣራ በኋላ በሚመለከተው ስልጣን ያለው ቡድን ነው። ስለ ውጤቱ መረጃ እሰጥዎታለሁ።

ከችግሩ ጋር የተያያዙ ያልላኩልን ፎቶዎች ወይም ስክሪንሾቶች ካሉ እባክዎ እዚህ ያጋሩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I've submitted your refund request for order {{order_id}} for review by our authorized team. I'll update you on the outcome. Send any extra photos/screenshots here. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለትዕዛዝ {{order_id}} ያቀረቡትን የተመላሽ ገንዘብ ጥያቄ ስልጣን ላለው ቡድናችን ለግምገማ አስገብቻለሁ። ውጤቱን አሳውቅዎታለሁ። ተጨማሪ ፎቶ/ስክሪንሾት ካለ እዚህ ይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your refund request for order {{order_id}} is still under review. We have not forgotten you, and we will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለትዕዛዝ {{order_id}} ያቀረቡት የተመላሽ ገንዘብ ጥያቄ አሁንም በግምገማ ላይ ነው። አልረሳንዎትም፤ እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- All refund decisions → **Senior Support / Supervisor** for recommendation; **Payments & Finance** for processing.
- Payment provider dispute/chargeback opened by the buyer → **Payments & Finance**.
- High-value refunds or policy exceptions → **Management**.
- Evidence of refund abuse (repeated claims, edited photos) → **Trust & Safety**.

## Resolution Procedure
1. Resolve when the refund is processed and confirmed by Payments, or declined with an explanation sent to the buyer.
2. Record reason, evidence, decision, approver, amount (if approved) and payment reference.

## Policy Pending Approval
- Define refund eligibility per reason for physical products, and deadlines to request.
- Decide whether delivery fees and payment processing fees are refundable.
- Define who approves refunds and up to what amount.
- Define refund methods (original payment method or other) and approved wording for processing times.
- Decide how seller earnings are adjusted when a refund is approved.

## Internal Notes
- Check for an existing refund case before opening a new one — duplicates confuse Payments.
- Never say "you will get your money back" before approval; say "your request is under review".

<!-- doc -->
# Buyer–Seller Disagreement Over an Order
id: phy-seller-dispute
type: article
category: physical-products
subcategory: cancellations-returns
audience: both
priority: high
department: support_l2
features: physical-products, delivery-addis
tags: dispute with seller, seller refuses, buyer seller conflict, seller says I received it, disagreement, complaint about seller, ከሻጩ ጋር አለመግባባት, ሻጩ አልቀበልም አለ, ክርክር
related: ref-buyer-seller-disagreement, ref-evidence-collection, phy-not-delivered-marked-delivered, phy-missing-items, phy-damaged-product, phy-refund-request-product
templates: tpl-request-screenshot, tpl-request-order-details
policy_pending: yes

## Summary
A buyer and a seller disagree about a physical product order (delivery, condition, what was promised, return or refund), and support must handle the dispute fairly.

## Issue Description
> [!WARNING] **Planned feature.** Check the **Feature Status** page to confirm physical products and delivery are live.

Byfluence is a **marketplace facilitator**: the seller is responsible for their product, subject to marketplace rules and any fulfillment responsibility Byfluence explicitly assumes. In a dispute, support must stay **neutral**, gather evidence from both sides, and pass the case to authorized personnel for a decision. Liability between seller, Byfluence and any delivery partner is **policy pending**.

Typical disputes:
- Buyer says not delivered; seller says delivered.
- Buyer says damaged/missing/wrong; seller says it left in perfect condition.
- Seller refuses a return or refund the buyer believes is fair.
- Disagreement about what the seller promised in messages.

## Possible Causes
- Genuine misunderstanding about the listing or agreement.
- Problem caused in transit by a third party.
- Missing evidence on one or both sides.
- Bad faith by the buyer or the seller.

## Information to Collect
**From the buyer**
- Order ID, description of the problem, what outcome they want
- Unboxing photos/video, packaging, label, item photos
- Screenshots of the listing and messages with the seller

**From the seller**
- Their account of events
- Packing photos/video, handover record, proof of delivery
- Screenshots of messages with the buyer

**From the system / other teams**
- Order and payment history, status changes and who made them
- Delivery record from **Logistics & Fulfillment** (if involved)
- Previous complaints involving either party

## Troubleshooting Steps
1. Acknowledge the buyer and the seller separately. Do not share one party's personal data with the other.
2. Collect evidence from both sides using *tpl-request-screenshot*; give each a fair chance to respond.
3. Request the delivery record where delivery is disputed.
4. Ask Payments to hold the seller's settlement for the order while the dispute is open, if possible.
5. Summarise the case in the ticket: timeline, evidence from each side, gaps, any fraud signals.
6. Escalate to **Senior Support / Supervisor** for a decision under approved policy (*ref-buyer-seller-disagreement*).
7. Communicate the decision to both parties neutrally, then route approved actions (refund → Payments, return → Logistics).

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for explaining the situation with order {{order_id}}. I understand this disagreement is frustrating, and I want to make sure your case is reviewed fairly.

We are collecting information from both sides, including the order history and any delivery records. Please send any photos, videos or screenshots that support your account, if you have not already.

Once the review is complete, our team will let you know the outcome. Please keep all communication on Byfluence and do not agree to any payment outside the platform.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ትዕዛዝ {{order_id}} ሁኔታውን ስላብራሩልን እናመሰግናለን። ይህ አለመግባባት እንደሚያበሳጭ እረዳለሁ፤ ጉዳይዎ በፍትሃዊነት እንዲገመገም እፈልጋለሁ።

የትዕዛዙን ታሪክና ካሉ የማድረሻ መዝገቦችን ጨምሮ ከሁለቱም ወገኖች መረጃ እየሰበሰብን ነው። እስካሁን ካልላኩ፣ እባክዎ የእርስዎን ገለጻ የሚደግፉ ፎቶዎችን፣ ቪዲዮዎችን ወይም ስክሪንሾቶችን ይላኩ።

ግምገማው ሲጠናቀቅ ቡድናችን ውጤቱን ያሳውቅዎታል። እባክዎ ሁሉንም ግንኙነት በ Byfluence ላይ ያድርጉ፤ ከመድረኩ ውጭ ለሚደረግ ማንኛውም ክፍያም አይስማሙ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I understand — we'll review order {{order_id}} fairly with information from both sides. Please send any photos, videos or screenshots that support your account. Keep everything on Byfluence. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ተረድቻለሁ — የትዕዛዝ {{order_id}}ን ጉዳይ ከሁለቱም ወገን በተገኘ መረጃ በፍትሃዊነት እንገመግማለን። እባክዎ ገለጻዎን የሚደግፉ ፎቶዎችን፣ ቪዲዮዎችን ወይም ስክሪንሾቶችን ይላኩ። ሁሉንም በ Byfluence ላይ ያድርጉ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are still reviewing the information from both sides for order {{order_id}}. Your case is with our senior team, and we will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለትዕዛዝ {{order_id}} ከሁለቱም ወገን የተገኘውን መረጃ አሁንም እየገመገምን ነው። ጉዳይዎ በከፍተኛ ቡድናችን እጅ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Every buyer–seller dispute requiring a decision → **Senior Support / Supervisor**.
- Delivery evidence needed → **Logistics & Fulfillment**.
- Fraud, threats, harassment or doxxing between parties → **Trust & Safety**.
- High-value, legal threat or media/reputational risk → **Management**.
- Settlement hold / refund processing → **Payments & Finance**.

## Resolution Procedure
1. Resolve after the authorized decision is communicated to both parties and approved actions are completed.
2. Record the full timeline, evidence summary, decision, approver and actions.

## Policy Pending Approval
- Define who decides buyer–seller disputes, what evidence standard applies, and whether decisions can be appealed.
- Define liability between seller, Byfluence and delivery partners for each dispute type.
- Define response deadlines for each party and what happens if a party does not respond.
- Decide whether seller settlement is automatically held while a dispute is open.

## Internal Notes
- Stay neutral: "we are reviewing the information from both sides". Never take sides in writing.
- Never forward one party's phone number, address or personal photos to the other.
- Evidence quality matters more than who complains louder; note gaps honestly in the ticket.

<!-- doc -->
# Master Guide: Order and Delivery Problems
id: phy-tsg-order-problem-master
type: troubleshooting
category: physical-products
subcategory: order-problems
audience: internal
priority: medium
department: support_l2
features: physical-products, delivery-addis
tags: order problem, delivery problem, master guide, order troubleshooting, decision tree, which article, የትዕዛዝ ችግር, የማድረስ ችግር
related: phy-delivery-delay, phy-not-delivered-marked-delivered, phy-damaged-product, phy-missing-items, phy-wrong-product, phy-seller-dispute
templates: tpl-request-order-details, tpl-order-status-check, tpl-request-screenshot
policy_pending: yes

## Summary
A diagnostic playbook to quickly identify any physical order or delivery problem, route it to the right article and department, and collect the right evidence the first time.

## Overview
> [!WARNING] **Planned features.** Physical products and Addis Ababa delivery are planned. Check the **Feature Status** page first. If they are not live and a customer describes an "order", confirm whether they bought through Byfluence at all — they may have bought from a seller's social media page.

Use this guide when the customer's problem is unclear, mixed (e.g., late **and** damaged), or when you need to choose priority and department.

Golden rules for every order case:
1. Identify the order (order ID or account) **before** anything else.
2. Never promise delivery dates, refunds, replacements or who is liable.
3. Evidence first: photos/video of package, label, contents; screenshots of listing and messages.
4. Keep all payments and communication on Byfluence.
5. Never ask for passwords, OTP codes, PINs or card numbers.

## Troubleshooting Steps
### Step 1 — Identify the order and its status
- Find the order by order ID, or by the registered email/phone and approximate date.
- No order found? → Check payment: paid but no order → *pay-paid-order-not-confirmed*; no payment → the order was not placed; bought outside Byfluence → explain we can't trace it; if a scam is suspected → **Trust & Safety**.

### Step 2 — Where is the order in its life?
| Status | Customer says | Go to |
|---|---|---|
| Pending payment | "I paid but it's pending" | *pay-paid-order-not-confirmed* |
| Confirmed / processing | "Where is my order?" | *phy-order-processing-status* |
| Confirmed / processing | "I want to cancel" | *phy-order-cancellation-buyer* |
| Processing for a long time | "Seller isn't responding" | *phy-contact-seller*, *phy-product-availability* |
| Shipped / out for delivery | "It's late" | *phy-delivery-delay* |
| Shipped / out for delivery | "Wrong address/phone" | *phy-incorrect-address* (urgent) |
| Delivered | "I never got it" | *phy-not-delivered-marked-delivered* (High) |
| Delivered | "Something is missing" | *phy-missing-items* |
| Delivered | "It's broken" | *phy-damaged-product* |
| Delivered | "It's not what I ordered" | *phy-wrong-product* |
| Delivered | "It's fake / misleading" | *phy-counterfeit-misleading* (Trust & Safety) |
| Delivered | "Poor quality / stopped working" | *phy-product-complaint-quality* |
| Delivered | "I want to return it" | *phy-returns* |
| Cancelled | "Why was it cancelled?" | *phy-order-cancellation-seller* |
| Any | "I want my money back" | *phy-refund-request-product* |
| Any | Buyer and seller disagree | *phy-seller-dispute* |

### Step 3 — Set priority
- **Critical:** safety risk (dangerous product), suspected organised fraud, account takeover redirecting deliveries.
- **High:** marked delivered but not received; counterfeit report; high-value item; parcel swapped between buyers; buyer–seller dispute with money at stake.
- **Medium:** delays, damaged/wrong/missing items, cancellations, refunds.
- **Low:** availability, product questions, how-to.

### Step 4 — Collect evidence (one message, not five)
- [ ] Order ID and account verification
- [ ] Photos/video: outer package (all sides), label, contents, the problem
- [ ] Screenshot of listing as ordered and relevant messages
- [ ] Delivery details used (address, landmark, phone)
- [ ] What outcome the customer wants (recorded, not promised)

### Step 5 — Check for fraud signals
- Delivery person asked for a code, PIN, extra cash or off-platform payment.
- Seller cancels and offers the item "directly".
- Address/phone change requested after a recent login or password change.
- Repeated claims by the same buyer, or repeated complaints about the same seller or delivery person.
- Edited or re-used photos.
→ Any of these: add **Trust & Safety** to the case.

### Step 6 — Route to the department
| Situation | Department |
|---|---|
| Delivery record, lost parcel, address change in transit, transit damage | **Logistics & Fulfillment** |
| Payment, refunds processing, settlement hold | **Payments & Finance** |
| Decision needed (refund/return/dispute) | **Senior Support / Supervisor** |
| Seller not responding, repeated seller problems | **Seller Operations** |
| Fraud, counterfeit, harassment | **Trust & Safety** |
| System errors (checkout, statuses not updating) | **Technical / Engineering** |
| High-value, legal, reputational | **Management** |

### Step 7 — Close properly
Record root cause (seller error, transit, address, buyer error, fraud, system), evidence, decision and approver. These records will inform the delivery and returns policies still to be written.

## Escalation Conditions
- Mixed cases (e.g., delayed and then damaged) → handle under the most serious issue and link the others in the ticket.
- Several customers reporting the same delivery or seller problem at once → **Senior Support / Supervisor** (possible incident).
- Any case where you are unsure who is responsible → **Senior Support / Supervisor**; never guess liability.

## Policy Pending Approval
- Confirm official order status names, delivery partners, areas, fees and timeframes.
- Define liability between seller, Byfluence and delivery partners.
- Approve return, refund and cancellation policies for physical products.
- Define proof-of-delivery and seller packing-evidence requirements.

## Internal Notes
- Physical products are new: expect customers who do not know the order flow. Explain one step at a time.
- Tag every order ticket with the root cause; management needs this data to design delivery policy.
- When in doubt, collect evidence and escalate rather than improvise a remedy.
