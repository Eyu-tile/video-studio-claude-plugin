# Byfluence — Business Context for Support Content Authors

(Condensed from the official Byfluence Business Overview. Treat everything here as the only
confirmed facts. Anything not stated here is NOT confirmed.)

- **Byfluence** (https://byfluence.com) is an Ethiopian multi-vendor online marketplace.
  Primary language Amharic, secondary English. Stage: MVP, more capabilities in development.
- Mission: anyone should be able to start and grow an online business, even without significant
  starting capital. Byfluence provides shared marketplace infrastructure (listings, payments,
  bookings, trust) so entrepreneurs don't need their own website/payment/booking systems.
- Byfluence is a **marketplace facilitator**, not the owner/provider of most listed products or
  services. Sellers are responsible for their offerings, subject to marketplace rules and any
  fulfillment responsibility Byfluence explicitly assumes.
- Revenue: commissions/fees on marketplace transactions. **Commission rates are not confirmed.**

## Users
- **Buyers**: discover products/services, search sellers, compare, book consultations, purchase,
  pay, track transactions, manage account, contact support. Buyer dashboard: profile, settings,
  consultation bookings (upcoming sessions + booking-management actions), purchase history, order
  info, transaction history, support options.
- **Sellers**: create seller account, complete identity verification, build public profile, create
  listings, set prices, manage availability, accept bookings/orders, monitor transactions, view
  earnings, request withdrawals.
- Seller onboarding: create account → apply to become seller → provide personal/business info →
  submit identity verification → wait for review → approved or rejected → complete profile → create
  listings → sell after permissions are granted.
- Seller status concepts: **Pending, Verified, Rejected** (verification) and **Active, Suspended,
  Banned** (operational). These are separate: a seller can be Verified but Suspended.
- Exact registration fields and verification methods depend on the implemented auth system
  (not confirmed: email verification? phone OTP? required ID documents?).

## Offerings
1. **One-on-one consultations** (MVP): buyer discovers → evaluates listing (consultant name,
   description, topic, duration, price, availability) → selects → schedules date/time → pays →
   booking confirmed after successful payment → receives Google Meet details → attends →
   consultation marked completed → seller earnings become available per settlement rules.
2. **Google Meet integration** (MVP): system associates a Meet meeting with the booking;
   participants join at scheduled time. Must handle: missing links, incorrect times, time-zone
   confusion, late buyers/sellers, no-shows, connection problems, reschedule requests.
   *A scheduled meeting does not prove the service was delivered.*
3. **Group consultations** (MVP capability): one professional, many buyers; seller sets date,
   duration, price, capacity; buyers register and pay; confirmed participants get meeting access.
   Rules for capacity, full sessions, cancellation, rescheduling, refunds, missed sessions,
   seller no-shows are **not yet approved**.
4. **Physical products** (expansion): clothing, electronics, accessories, beauty, home, lifestyle.
   Seller lists → buyer orders with delivery info → pays → seller prepares → fulfillment → order
   completed → seller settlement. Initial rollout prioritizes **Addis Ababa**. Delivery methods,
   areas, fees and times are **not confirmed**.
5. **Inventory-free selling / local dropshipping** (expansion): Byfluence partners with suppliers or
   verified sellers; eligible sellers promote/resell approved products under platform pricing rules;
   supplier or designated fulfillment partner fulfils; reseller earns agreed margin/commission.
   "Zero investment" = no upfront stock, NOT zero costs or risk. Terms, eligibility, and cost
   responsibilities are **not defined**.
6. **Digital products** (expansion): e-books, templates, guides, courses, design resources,
   documents. Seller uploads → buyer pays → buyer gets access. Must handle secure access,
   unauthorized downloads, broken links, wrong/corrupted files, description disputes, copyright
   complaints, refund eligibility, download limits. Rules **not confirmed**.

## Payments
- Providers worked with or considered: **Chapa, Telebirr, M-Pesa, bank-based methods, Stripe**
  (potential international). Availability of each is **not confirmed**.
- Flow: select → amount calculated → choose method → pay → provider processes → Byfluence receives
  confirmation → order/booking confirmed → records updated.
- Payment status concepts: Pending, Successful, Failed, Canceled, Refund Pending, Refunded, Disputed.

## Seller earnings
- Lifecycle: customer pays → confirmed → recorded → platform fees calculated → seller earnings
  calculated → **pending** until release conditions met → **available** (withdrawable) → seller
  requests withdrawal → Byfluence processes → recorded completed after confirmation.
- Balance concepts: Total Earnings, Pending Balance, Available Balance, Withdrawn Amount,
  Withdrawal Pending.
- A successful customer payment ≠ immediately withdrawable seller balance (completion, disputes,
  cancellations, refunds, settlement). Payout methods, minimums, timelines: **not confirmed**.

## Refunds & disputes
- Different categories may need different policies. Refund eligibility, deadlines, deductions and
  approval authority **must be set by official policy — not yet established**.
- Support workflow: complaint → identify transaction → collect evidence → review policy → contact
  seller/department → authorized personnel decide → explain to customer → process approved
  adjustments → document and close.

## Administration
User management, seller management (applications, verification, suspension), listing moderation,
transaction monitoring, refund review, withdrawal processing, marketplace performance.
Admin access restricted by role.

## Support
- Channels intended: website support, Telegram, email, telephone, AI-powered assistance.
- Amharic default; English on request. Professional, respectful, clear, concise, consistent.
  Never promise anything not authorized.
- AI assistant (future): answers FAQs, explains approved policies, guides users, identifies
  issues needing humans. Humans handle account-specific investigation, financial decisions,
  identity verification review, refund approval, seller disputes, fraud, admin access, sensitive data.
- Experience principles: Simplicity, Trust, Opportunity, Accountability.
