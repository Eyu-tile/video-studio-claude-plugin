<!-- doc -->
# Supplier Stock or Product Information Is Wrong
id: inv-supplier-stock-errors
type: article
category: inventory-free
subcategory: suppliers
audience: seller
priority: medium
department: seller_ops
features: inventory-free-selling, physical-products
tags: supplier out of stock, wrong product info, stock error, product description wrong, sold but no stock, wrong price supplier, ክምችት የለም, የምርት መረጃ ስህተት, አቅራቢ
related: inv-fulfillment-responsibility, inv-customer-complaint-reseller-order, inv-choosing-products, inv-reseller-misrepresentation, phy-seller-order-management
templates: tpl-seller-contact-request
policy_pending: yes

## Summary
A reseller (or supplier) reports that a program product shows wrong stock, wrong price, or wrong/misleading product information — sometimes after a buyer has already ordered.

## Issue Description
> [!WARNING] Inventory-free selling is a **planned** feature. Check the **Feature Status** page before handling this as a live-program issue. If the feature is not live, the report may concern a normal product listing — use the listings articles instead.

In the inventory-free model the **supplier** owns the stock and product information, while the **reseller** promotes it. When supplier data is wrong, the reseller may have sold something that cannot be delivered or that differs from the description. This harms buyers and resellers' trust. Agents must stop further harm (flag the product), protect affected buyers, and route the correction to Seller Operations — not fix the catalog themselves.

## Possible Causes
- Supplier did not update stock after selling elsewhere.
- Sync delay between supplier stock and the platform.
- Wrong product photo, size, colour, model or specification from the supplier.
- Supplier changed the product (new version) without updating information.
- Price error in the supplier feed.
- Reseller edited the information (if allowed) and introduced errors.

## Information to Collect
- Reporter's registered email/phone and role (reseller / supplier)
- Product name ({{product_name}}) and supplier name
- What is wrong (stock, price, description, photo) and how they know
- Affected orders ({{order_id}}) and their status
- Screenshots of the product page

## Troubleshooting Steps
1. Confirm identity and role; check **Feature Status**.
2. Open the product and any affected orders through authorized tools (admin dashboard, if you have access).
3. Decide:
   - **No orders affected** → report correction to **Seller Operations**; ask the reseller to pause promotion of that product meanwhile.
   - **Orders affected (cannot be fulfilled or differ from description)** → priority High; escalate to **Seller Operations** and inform **Senior Support / Supervisor** so buyers are contacted with approved options (no promises of refunds by you).
   - **Price error** → **Seller Operations** + **Payments & Finance** if orders were paid at the wrong price.
   - **Suspected deliberate misinformation by supplier** → **Trust & Safety**.
4. Record product, supplier, error type and affected orders.

- [ ] Feature Status checked
- [ ] Product flagged to Seller Operations
- [ ] Affected orders identified
- [ ] Buyers' cases escalated

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for reporting this — it helps us protect buyers. I have recorded that the information for "{{product_name}}" appears to be incorrect: [stock / price / description].

I have passed this to our Seller Operations team so the supplier information can be checked and corrected. Until then, please pause promoting this product.

[If orders affected:] For order {{order_id}}, the responsible team will review the situation and the buyer will be contacted with the available options.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ይህንን ስላሳወቁን እናመሰግናለን — ገዢዎችን እንድንጠብቅ ይረዳናል። የ"{{product_name}}" መረጃ ስህተት እንደሚመስል መዝግቤያለሁ፦ [ክምችት / ዋጋ / መግለጫ]።

የአቅራቢው መረጃ እንዲጣራ እና እንዲስተካከል ለሻጭ ኦፕሬሽንስ ቡድናችን አስተላልፌያለሁ። እስከዚያው ድረስ እባክዎ ይህንን ምርት ማስተዋወቅዎን ለጊዜው ያቁሙ።

[ትዕዛዞች ከተነኩ፦] ለትዕዛዝ {{order_id}} ኃላፊው ቡድን ሁኔታውን ገምግሞ ገዢው ስላሉት አማራጮች ይነገረዋል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for reporting! I've passed the incorrect info on "{{product_name}}" to Seller Operations to check with the supplier. Please pause promoting it for now. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን! የ"{{product_name}}" የተሳሳተ መረጃ ከአቅራቢው ጋር እንዲጣራ ለሻጭ ኦፕሬሽንስ አስተላልፌያለሁ። እባክዎ ለጊዜው ማስተዋወቁን ያቁሙ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Seller Operations is still checking the information for "{{product_name}}" with the supplier. We will contact you again by {{follow_up_time}}.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የሻጭ ኦፕሬሽንስ ቡድን የ"{{product_name}}"ን መረጃ ከአቅራቢው ጋር አሁንም እያጣራ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን።

## Escalation Conditions
- Any catalog error → **Seller Operations**.
- Paid orders that can't be fulfilled → **Seller Operations** + **Senior Support / Supervisor**, priority High.
- Wrong-price paid orders → + **Payments & Finance**.
- Delivery already in progress with wrong item → **Logistics & Fulfillment**.
- Deliberate misinformation → **Trust & Safety**.

## Resolution Procedure
1. Product information corrected or product removed; affected buyers handled.
2. Reporter informed.
3. Record error type, supplier, orders affected and outcome.

## Policy Pending Approval
- Define supplier obligations for stock and information accuracy and consequences for errors.
- Define what buyers are offered when an inventory-free order cannot be fulfilled.
- Define whether resellers lose their margin when a supplier error cancels an order.

## Internal Notes
- Ask "has anyone already paid?" first — that decides priority.
- Repeated errors from one supplier → tag `supplier-quality` for Seller Operations.

<!-- doc -->
# Who Fulfils Orders and Who the Buyer Contacts
id: inv-fulfillment-responsibility
type: article
category: inventory-free
subcategory: suppliers
audience: both
priority: low
department: seller_ops
features: inventory-free-selling, physical-products, delivery-addis
tags: who delivers, who fulfils, contact supplier, contact reseller, reseller order delivery, responsibility, ማን ያደርሳል, ማንን ላግኝ, ኃላፊነት
related: inv-how-it-works, inv-customer-complaint-reseller-order, inv-supplier-stock-errors, phy-seller-order-management, inv-reseller-misrepresentation
templates:
policy_pending: yes

## Summary
A buyer, reseller or supplier asks who is responsible for delivering an inventory-free order and who the buyer should contact if something goes wrong.

## Overview
> [!WARNING] Inventory-free selling is a **planned** feature, and delivery (including Addis Ababa delivery) is also planned. Check the **Feature Status** page before describing any of this as available.

From the business overview:
- The **supplier or a designated fulfillment partner** fulfils the order.
- The **reseller** promotes and sells; they do not hold stock.
- **Byfluence** is the marketplace facilitator; it takes fulfillment responsibility only where it explicitly assumes it.

### Who the buyer contacts
Until a formal rule is approved, the safest guidance is: **the buyer contacts Byfluence Support** about any problem with an inventory-free order. Support then coordinates with Seller Operations, the supplier, the fulfillment partner and the reseller. This avoids buyers being bounced between parties and keeps buyer data protected.

| Problem | Owner (as described) | Support routes to |
|---|---|---|
| Not delivered / late | Supplier / fulfillment partner | Logistics & Fulfillment, Seller Operations |
| Wrong/damaged item | Supplier | Seller Operations |
| Item differs from reseller's promotion | Reseller (claims) / supplier (info) | Seller Operations, Trust & Safety |
| Payment/refund | Byfluence processes | Payments & Finance |

> [!POLICY] Who is formally responsible to the buyer, and who pays for failures, is not defined. Do not tell buyers "it's the supplier's problem" or "contact the reseller".

## Customer Steps
1. Buyers: contact Byfluence Support with your order ID for any problem.
2. Resellers: direct buyers to Byfluence Support rather than handling refunds or replacements yourself.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your question. For orders through the inventory-free program, the product is supplied and delivered by the supplier or a delivery partner, and the reseller is the one who promoted it to you.

If anything goes wrong with your order, please contact Byfluence Support with your order number. We will coordinate with everyone involved, so you don't need to chase different parties.

[If not live:] Please note this program is part of Byfluence's plans and is not yet available.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጥያቄዎ እናመሰግናለን። ያለ ክምችት በሚሸጥ ፕሮግራም በኩል በሚደረጉ ትዕዛዞች ምርቱን የሚያቀርበው እና የሚያደርሰው አቅራቢው ወይም የማድረስ አጋር ሲሆን ዳግም ሻጩ ደግሞ ምርቱን ያስተዋወቀልዎት ነው።

በትዕዛዝዎ ላይ ማንኛውም ችግር ከተፈጠረ እባክዎ በትዕዛዝ ቁጥርዎ Byfluence ድጋፍን ያግኙ። ከሚመለከታቸው ሁሉ ጋር እኛ እናስተባብራለን፤ እርስዎ የተለያዩ ወገኖችን መከታተል አያስፈልግዎትም።

[ገና ካልተጀመረ፦] እባክዎ ይህ ፕሮግራም የByfluence ዕቅድ አካል መሆኑን እና ገና እንዳልተጀመረ ልብ ይበሉ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! In inventory-free orders the supplier or a delivery partner delivers, and the reseller promoted the product. For any problem, contact Byfluence Support with your order number — we'll coordinate. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! ያለ ክምችት በሚሸጡ ትዕዛዞች አቅራቢው ወይም የማድረስ አጋር ያደርሳል፤ ዳግም ሻጩ ምርቱን አስተዋወቀ። ለማንኛውም ችግር በትዕዛዝ ቁጥርዎ Byfluence ድጋፍን ያግኙ — እኛ እናስተባብራለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Delivery problems → **Logistics & Fulfillment**.
- Product/supplier problems → **Seller Operations**.
- Reseller claims vs. reality → **Trust & Safety** (see `inv-reseller-misrepresentation`).
- Refund requests → **Senior Support / Supervisor** → **Payments & Finance**.

## Policy Pending Approval
- Define the legal and operational responsibility of supplier, reseller and Byfluence toward the buyer.
- Define who bears the cost of failed deliveries, returns and refunds.
- Decide whether buyers can see the supplier's identity.
- Confirm delivery areas, fees and partners.

## Internal Notes
- Don't give the buyer the supplier's or reseller's personal phone — coordinate through official channels.

<!-- doc -->
# How Reseller Earnings Are Calculated and Paid
id: inv-reseller-earnings-how
type: article
category: inventory-free
subcategory: reseller-earnings
audience: seller
priority: low
department: payments
features: inventory-free-selling, seller-withdrawals
tags: reseller earnings, reseller commission, margin paid, when do resellers get paid, reseller payout, reseller balance, የዳግም ሻጭ ገቢ, ኮሚሽን መቼ, ክፍያ
related: inv-pricing-rules, inv-reseller-earnings-missing, out-how-earnings-work, out-pending-vs-available, out-how-to-withdraw
templates:
policy_pending: yes

## Summary
A reseller asks how their margin/commission is calculated, when it becomes available and how to withdraw it.

## Overview
> [!WARNING] Inventory-free selling is a **planned** feature. Check the **Feature Status** page first. Never quote margins, release times or payout methods — none are confirmed.

Confirmed: resellers earn an **agreed margin or commission**. The general seller earnings lifecycle on Byfluence is also confirmed and is likely to apply (not confirmed for resellers specifically):

1. Buyer pays → payment confirmed → recorded.
2. Platform fees calculated → earnings calculated.
3. Earnings are **Pending** until release conditions are met (e.g., order completed, no dispute/cancellation/refund).
4. Earnings become **Available** (withdrawable).
5. Seller requests withdrawal → Byfluence processes → recorded as completed after confirmation.

Balance terms: Total Earnings, Pending Balance, Available Balance, Withdrawn Amount, Withdrawal Pending. A buyer's successful payment ≠ immediately withdrawable reseller earnings. See `out-how-earnings-work`, `out-pending-vs-available`, `out-how-to-withdraw`.

## Customer Steps
1. Check your earnings in your seller dashboard (when the program is live).
2. Wait until earnings move from Pending to Available.
3. Request a withdrawal of your Available Balance.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for your question. Resellers in the inventory-free program earn an agreed margin or commission on completed sales.

Like other Byfluence seller earnings, reseller earnings would first show as Pending — for example, until the order is completed and there is no cancellation, refund or dispute — and then become Available, when you can request a withdrawal.

The exact margins, release conditions and payout details for the program have not been announced yet. We will share them through {{support_channel}} when available.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ስለ ጥያቄዎ እናመሰግናለን። ያለ ክምችት በመሸጥ ፕሮግራም ውስጥ ያሉ ዳግም ሻጮች በተጠናቀቁ ሽያጮች ላይ የተስማሙበትን የትርፍ ህዳግ ወይም ኮሚሽን ያገኛሉ።

እንደ ሌሎች የByfluence ሻጮች ገቢ ሁሉ የዳግም ሻጭ ገቢም መጀመሪያ "Pending" (በመጠባበቅ ላይ) ሆኖ ይታያል — ለምሳሌ ትዕዛዙ እስኪጠናቀቅ እና ስረዛ፣ ተመላሽ ገንዘብ ወይም ክርክር እስከሌለ ድረስ — ከዚያም ገንዘብ ለማውጣት መጠየቅ የሚችሉበት "Available" ይሆናል።

ለፕሮግራሙ ትክክለኛ የትርፍ መጠኖች፣ የመልቀቂያ ሁኔታዎች እና የክፍያ ዝርዝሮች ገና አልተገለጹም። ሲገኙ በ{{support_channel}} በኩል እናጋራለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}! Resellers earn an agreed margin/commission on completed sales. Earnings show as Pending first, then Available for withdrawal. Exact margins and payout details aren't announced yet. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}! ዳግም ሻጮች በተጠናቀቁ ሽያጮች የተስማሙበትን ትርፍ/ኮሚሽን ያገኛሉ። ገቢ መጀመሪያ "Pending" ከዚያም ለማውጣት "Available" ይሆናል። ትክክለኛ የትርፍ መጠንና የክፍያ ዝርዝሮች ገና አልተገለጹም። የጉዳይ ቁጥር፦ {{ticket_id}}

## Escalation Conditions
- Questions on exact margins, release timing or payout methods → **Senior Support / Supervisor** / **Payments & Finance**.
- Earnings missing or wrong → `inv-reseller-earnings-missing`.

## Policy Pending Approval
- Define reseller margin/commission and how it is calculated (before/after fees, delivery costs).
- Define release conditions for reseller earnings (delivery confirmation, return window).
- Confirm whether reseller payouts use the same withdrawal process as other sellers.

## Internal Notes
- Keep the explanation conceptual; use the payouts articles for detail.

<!-- doc -->
# Reseller Earnings Missing or Wrong
id: inv-reseller-earnings-missing
type: article
category: inventory-free
subcategory: reseller-earnings
audience: seller
priority: medium
department: payments
features: inventory-free-selling, seller-withdrawals
tags: reseller earnings missing, commission not received, wrong margin, earnings not showing, reseller balance wrong, unpaid commission, ገቢ አልደረሰም, ኮሚሽን አልተከፈለም, የተሳሳተ ገቢ
related: inv-reseller-earnings-how, inv-pricing-rules, out-pending-vs-available, out-how-earnings-work, out-how-to-withdraw, inv-customer-complaint-reseller-order
templates: tpl-seller-contact-request
policy_pending: yes

## Summary
A reseller says their margin/commission for a sale is missing, lower than expected, or still pending.

## Issue Description
> [!WARNING] Inventory-free selling is a **planned** feature. Check the **Feature Status** page first. If the program is not live, the person may be confused with normal seller earnings (use the payouts articles) or may be a victim of a fake "reseller" scheme run outside Byfluence.

Most "missing earnings" cases are timing (still **Pending**), the order not being completed, cancellations/returns, or misunderstanding how margins are calculated. Real errors exist (wrong margin, sale not attributed to the reseller). Agents check facts and escalate calculation issues to Payments & Finance — never promise an amount or adjust balances.

## Possible Causes
- Earnings still **Pending** (order not delivered/completed, release conditions not met).
- Order cancelled, returned, refunded or disputed.
- Sale not attributed to the reseller (buyer used a different link/route — attribution rules not confirmed).
- Margin calculated differently than the reseller expected (fees, delivery costs — rules not defined).
- System error in commission calculation.
- Fake program outside Byfluence (no record of the reseller at all).

## Information to Collect
- Reseller's registered email/phone
- Order ID(s) ({{order_id}}) and product names
- Expected amount and how they calculated it
- What the dashboard shows (screenshot)
- Date of sale

> [!WARNING] Never ask for passwords, OTP codes, PINs or bank account numbers.

## Troubleshooting Steps
1. Confirm identity; check **Feature Status**.
2. If the program is not live and the person says they are a reseller → ask how they joined; if through a third party → possible scam → **Trust & Safety**.
3. Check through authorized tools (admin dashboard, if you have access) for each order: status, delivery/completion, cancellations/refunds/disputes, attribution to the reseller, earnings record.
4. Decide:
   - **Order not completed / Pending** → explain Pending vs. Available.
   - **Cancelled/refunded/returned** → explain that earnings depend on completed sales (do not quote rules not approved).
   - **Not attributed** → **Seller Operations** + **Payments & Finance**.
   - **Amount differs** → **Payments & Finance** with order IDs and reseller's calculation.
   - **Available but withdrawal problem** → payouts articles (`out-how-to-withdraw`).
5. Record findings per order.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support. I understand the earnings for your sale(s) don't look right, and I'll help check this.

I have looked at order {{order_id}}: [finding, e.g. "the order is not yet completed, so the earnings are still pending" / "the order was cancelled, so no earnings were recorded" / "I've sent the calculation to our Payments team to review"].

Your case number is {{ticket_id}}. We will update you as soon as we have more information.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን። ለሽያጭዎ(ዎችዎ) የተመዘገበው ገቢ ትክክል እንዳልመሰለዎት ተረድቻለሁ፤ ለማጣራት እረዳዎታለሁ።

ትዕዛዝ {{order_id}}ን አይቻለሁ፦ [ውጤት፤ ለምሳሌ "ትዕዛዙ ገና ስላልተጠናቀቀ ገቢው አሁንም በመጠባበቅ ላይ ነው" / "ትዕዛዙ ስለተሰረዘ ምንም ገቢ አልተመዘገበም" / "ስሌቱን እንዲገመግሙ ለክፍያ ቡድናችን ልኬያለሁ"]።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ተጨማሪ መረጃ እንዳገኘን ወዲያውኑ እናሳውቅዎታለን።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, I checked order {{order_id}}: [finding]. [If escalated: I've sent it to our Payments team.] I'll update you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ትዕዛዝ {{order_id}}ን አጣርቻለሁ፦ [ውጤት]። [ከተላለፈ፦ ለክፍያ ቡድናችን ልኬያለሁ።] መረጃ እሰጥዎታለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our Payments team is still reviewing the earnings for order {{order_id}}. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ቡድናችን ለትዕዛዝ {{order_id}} የተመዘገበውን ገቢ አሁንም እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Calculation differences or missing earnings records → **Payments & Finance**, priority Medium.
- Attribution problems → **Seller Operations** + **Payments & Finance**.
- Person "joined" through a third party while the program isn't live → **Trust & Safety**, priority High.
- Many resellers report wrong earnings at once → **Technical / Engineering** + **Payments & Finance**, notify supervisor.

## Resolution Procedure
1. Earnings corrected/confirmed by Payments, or cause explained.
2. Record order IDs, cause and outcome.

## Policy Pending Approval
- Define reseller margin calculation, attribution rules and release conditions.
- Define how cancellations, returns and refunds affect reseller earnings.

## Internal Notes
- Never adjust or promise amounts. Even if the reseller's maths looks right, Payments decides.

<!-- doc -->
# Buyer Complaint About a Resold Product
id: inv-customer-complaint-reseller-order
type: article
category: inventory-free
subcategory: reseller-issues
audience: buyer
priority: high
department: support_l2
features: inventory-free-selling, physical-products, delivery-addis
tags: complaint reseller product, wrong item reseller, damaged resold product, not as described, reseller order problem, dropshipping complaint, የተሸጠልኝ ምርት ችግር, የተሳሳተ ዕቃ, የተበላሸ ዕቃ
related: inv-fulfillment-responsibility, inv-supplier-stock-errors, inv-reseller-misrepresentation, phy-seller-order-management, tns-fake-products, inv-reseller-earnings-missing
templates: tpl-request-customer-info, tpl-seller-contact-request
policy_pending: yes

## Summary
A buyer complains about a product bought through a reseller in the inventory-free program: not delivered, wrong, damaged, not as described, or different from what the reseller promised.

## Issue Description
> [!WARNING] Inventory-free selling and delivery are **planned** features. Check the **Feature Status** page first. If the program is not live, the buyer may have bought through a **third party claiming to be a Byfluence reseller** outside the platform — treat as possible fraud and check whether the order exists on Byfluence at all.

Three parties are involved (supplier, reseller, fulfillment partner), which can confuse the buyer. Byfluence Support is the single point of contact. The agent must collect evidence, identify which party's failure it is, protect the buyer from being bounced around, and route to the decision-makers. Refund eligibility and responsibility are **not yet defined** — no refund promises.

## Possible Causes
- Supplier sent the wrong item or a damaged item.
- Supplier information was wrong (see `inv-supplier-stock-errors`).
- Reseller exaggerated or made false claims (see `inv-reseller-misrepresentation`).
- Delivery delayed or lost by fulfillment partner.
- Buyer ordered the wrong variant.
- Counterfeit product.
- Purchase happened outside Byfluence (scam).

## Information to Collect
- Buyer's name and registered email/phone
- Order ID ({{order_id}}), product ({{product_name}}), amount and payment method
- What the problem is and when it was noticed
- Photos of the item, packaging and label (if received)
- Screenshots of what the reseller promised (posts, messages)
- Where they bought it: on Byfluence checkout, or paid someone directly?

> [!WARNING] Never ask for passwords, OTP codes, PINs or full card numbers.

## Troubleshooting Steps
1. Confirm identity; check **Feature Status**.
2. Find the order through authorized tools (admin dashboard, if you have access). **No order on Byfluence** → ask how they paid; if paid outside Byfluence → **Trust & Safety**, explain Byfluence can only investigate platform orders, and collect details of the person.
3. Classify:
   - **Not delivered / late** → **Logistics & Fulfillment**.
   - **Wrong / damaged / defective** → **Seller Operations** (supplier), with photos.
   - **Different from reseller's claims** → `inv-reseller-misrepresentation` → **Trust & Safety** + **Seller Operations**.
   - **Counterfeit** → **Trust & Safety** (see `tns-fake-products`).
4. Ask the buyer to keep the item and packaging; do not tell them to return it until a process is approved.
5. Escalate the refund/replacement decision to **Senior Support / Supervisor** (and **Payments & Finance** for any refund). Do not promise an outcome.
6. Record all evidence and the classification.

- [ ] Feature Status checked
- [ ] Order found on Byfluence (or off-platform scam identified)
- [ ] Evidence collected
- [ ] Classified and routed

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry your order has not met your expectations. I'm here to help.

To look into order {{order_id}}, please send me:
1. a short description of the problem,
2. photos of the item, packaging and label (if you received it),
3. any screenshots of what the seller told you about the product.

Please keep the item and its packaging for now. You don't need to contact the supplier or reseller yourself — we will coordinate with everyone involved. Any decision about a replacement or refund will be made by the responsible team after review.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ ትዕዛዝዎ እንደጠበቁት ባለመሆኑ ይቅርታ እንጠይቃለን። ልረዳዎት ዝግጁ ነኝ።

ትዕዛዝ {{order_id}}ን ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ስለ ችግሩ አጭር መግለጫ፣
2. የዕቃውን፣ የማሸጊያውን እና የመለያውን (label) ፎቶዎች (ደርሶዎት ከሆነ)፣
3. ሻጩ ስለ ምርቱ የነገረዎት ነገር ካለ ስክሪንሾቶች።

እባክዎ ዕቃውን እና ማሸጊያውን ለጊዜው ያስቀምጡ። አቅራቢውን ወይም ዳግም ሻጩን ራስዎ ማግኘት አያስፈልግዎትም — ከሚመለከታቸው ሁሉ ጋር እኛ እናስተባብራለን። ስለ መተኪያ ወይም ተመላሽ ገንዘብ የሚሰጠው ማንኛውም ውሳኔ ከግምገማ በኋላ በኃላፊው ቡድን ይሰጣል።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about your order! Please send a short description, photos of the item/packaging/label and any screenshots of the seller's claims. Keep the item for now — we'll coordinate with everyone involved. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ ትዕዛዝዎ ይቅርታ! እባክዎ አጭር መግለጫ፣ የዕቃ/ማሸጊያ/መለያ ፎቶዎች እና የሻጩ ቃል ስክሪንሾቶችን ይላኩ። ዕቃውን ለጊዜው ያስቀምጡ — ከሁሉም ጋር እኛ እናስተባብራለን። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. We are reviewing order {{order_id}} with the supplier and the responsible teams. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ትዕዛዝ {{order_id}}ን ከአቅራቢው እና ከሚመለከታቸው ቡድኖች ጋር እየገመገምን ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Delivery problems → **Logistics & Fulfillment**.
- Wrong/damaged/defective item → **Seller Operations**.
- False claims by reseller, counterfeit, or off-platform payment → **Trust & Safety**, priority High.
- Refund/replacement decision → **Senior Support / Supervisor** → **Payments & Finance**.
- High-value order or public complaint → **Management** via supervisor.

## Resolution Procedure
1. Responsible team decided the outcome (replacement, refund, no action) and it has been processed.
2. Buyer informed with approved wording and confirms.
3. Record classification, evidence, parties involved, decision and outcome.

## Policy Pending Approval
- Define refund/return/replacement rules for inventory-free orders.
- Define which party bears the cost in each failure type.
- Define deadlines for buyers to report problems.
- Define what Byfluence can do for buyers who paid a "reseller" outside the platform.

## Internal Notes
- Ask early "Did you pay on Byfluence or directly to someone?" — this changes everything.
- Don't blame the supplier or reseller in messages to the buyer; say "the responsible teams".

<!-- doc -->
# Reseller Made False Claims About a Product
id: inv-reseller-misrepresentation
type: article
category: inventory-free
subcategory: reseller-issues
audience: both
priority: high
department: trust_safety
features: inventory-free-selling
tags: reseller false claims, misleading reseller, fake advertising, reseller lied, exaggerated product, reseller scam, ሐሰተኛ ማስታወቂያ, አሳሳች ዳግም ሻጭ, ውሸት
related: inv-customer-complaint-reseller-order, tns-misleading-descriptions, tns-fake-products, inv-choosing-products, inv-zero-investment-meaning, sel-account-restrictions
templates: tpl-request-customer-info
policy_pending: yes

## Summary
A buyer (or supplier) reports that a reseller made false or exaggerated claims about a product — features, origin, brand, health benefits, guarantees, price or delivery — in their promotion.

## Issue Description
> [!WARNING] Inventory-free selling is a **planned** feature. Check the **Feature Status** page first. If it is not live, someone may be falsely calling themselves a "Byfluence reseller" — that is impersonation and goes to Trust & Safety.

Resellers promote products they don't hold and may be tempted to over-promise (e.g., "original brand", "cures diabetes", "free delivery anywhere", "guaranteed"). Because promotions often happen on social media or Telegram, evidence is usually screenshots. False claims harm buyers and Byfluence's trust. Agents collect evidence, protect the buyer's order case, and route to Trust & Safety; they do not confront the reseller or decide penalties.

## Possible Causes
- Reseller exaggerated to make sales.
- Reseller copied claims from elsewhere without checking.
- Supplier information was wrong and the reseller repeated it.
- Person falsely claiming to be a Byfluence reseller.
- Reseller added unapproved charges or promises (delivery, warranty).

## Information to Collect
- Reporter's name, role (buyer/supplier/other) and registered contact
- Reseller's name/store name and where the claim was made (Byfluence page, Telegram, social media) — link if available
- Screenshots of the claims, with dates
- Related order ID ({{order_id}}) if a purchase was made
- What was actually received or found to be untrue

## Troubleshooting Steps
1. Confirm identity; check **Feature Status**.
2. Verify the reseller exists on Byfluence (admin dashboard, if you have access). Not found → impersonation → **Trust & Safety**, priority High.
3. Compare the claim with the official product information:
   - **Claim not in official info** → reseller misrepresentation → **Trust & Safety** + **Seller Operations**.
   - **Claim is in official info but false** → supplier issue → `inv-supplier-stock-errors`.
4. Health, safety or legal claims (medical cures, safety certifications) → priority High.
5. If the buyer has an order problem → also follow `inv-customer-complaint-reseller-order`.
6. Do not contact the reseller yourself or reveal the reporter's identity.

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for reporting this. Accurate information is very important on Byfluence, and we take reports like this seriously.

I have recorded your report. To help our team review it, please send:
1. the name of the seller/reseller and where you saw the claim,
2. screenshots of the claim (with the date, if possible),
3. your order number, if you bought the product.

Our Trust & Safety team will review the report. For privacy reasons we may not be able to share the actions taken, but your report will be handled. If you have a problem with an order, we will also handle that in this case.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

ይህንን ስላሳወቁን እናመሰግናለን። በByfluence ላይ ትክክለኛ መረጃ በጣም አስፈላጊ ነው፤ እንደዚህ ያሉ ሪፖርቶችን በቁም ነገር እንመለከታለን።

ሪፖርትዎን መዝግቤያለሁ። ቡድናችን እንዲገመግመው እባክዎ የሚከተሉትን ይላኩ፦
1. የሻጩን/የዳግም ሻጩን ስም እና ማስታወቂያውን የት እንዳዩት፣
2. የማስታወቂያው ስክሪንሾቶች (ከተቻለ ከቀኑ ጋር)፣
3. ምርቱን ገዝተው ከሆነ የትዕዛዝ ቁጥርዎ።

የእምነትና ደህንነት (Trust & Safety) ቡድናችን ሪፖርቱን ይገመግማል። ለግላዊነት ሲባል የተወሰዱትን እርምጃዎች ልናጋራ ላንችል እንችላለን፤ ሆኖም ሪፖርትዎ ይስተናገዳል። በትዕዛዝ ላይ ችግር ካለ እሱንም በዚሁ ጉዳይ እናስተናግዳለን።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, thanks for reporting this. Please send the reseller's name, where you saw the claim, screenshots (with date) and your order number if you bought it. Trust & Safety will review. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስላሳወቁን እናመሰግናለን። እባክዎ የዳግም ሻጩን ስም፣ ማስታወቂያውን የት እንዳዩ፣ ስክሪንሾቶች (ከቀን ጋር) እና ከገዙ የትዕዛዝ ቁጥርዎን ይላኩ። Trust & Safety ይገመግማል። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Your report is under review by our Trust & Safety team. We will contact you again by {{follow_up_time}} [about your order]. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ሪፖርትዎ በእምነትና ደህንነት ቡድናችን እየተገመገመ ነው። እስከ {{follow_up_time}} ድረስ [ስለ ትዕዛዝዎ] በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- All misrepresentation reports → **Trust & Safety**, priority High.
- Health/medical/safety claims or counterfeit brand claims → **Trust & Safety**, priority High; supervisor informed.
- Supplier-originated false information → **Seller Operations**.
- Buyer order losses → **Senior Support / Supervisor** (and Payments for refunds).
- Impersonation of Byfluence → **Trust & Safety**, priority High.

## Resolution Procedure
1. Trust & Safety reviewed; any order issue resolved separately.
2. Reporter informed with approved wording.
3. Record reseller, claim, evidence, routing and outcome.

## Policy Pending Approval
- Define reseller marketing rules (what claims are allowed, off-platform promotion, use of Byfluence brand).
- Define penalties for reseller misrepresentation.
- Decide whether resellers are liable for buyer losses caused by their claims.

## Internal Notes
- Screenshots can be fabricated — record them as evidence, not proof.
- Never say "the reseller will be banned" — outcomes are decided by Trust & Safety.
