# Decisions Byfluence Management Needs to Make

The support documentation was written **without inventing any Byfluence policy**. Wherever an article needed a rule that hasn't been decided, it has a *Policy Pending Approval* section. Agents are told to collect evidence, make no promises and escalate. **328 of the 447 documents** have these markers. The live list is in the app under *Policies & Guidelines → Policy Pending Tracker*.

This document groups the open decisions by priority. Once a decision is made:

1. Update the matching policy document in the app (administrator).
2. Remove or replace the *Policy Pending Approval* sections in the affected articles. The tracker lists them.
3. Publish an announcement so agents know.

---

## Priority 1: blocks daily support

### A. What is actually live
- Which features are live in production. Consultations, group sessions, Google Meet, withdrawals, physical products, delivery, digital products and inventory-free selling are all unconfirmed. **Update Settings → Feature Status.**
- Which payment methods are live: Chapa, Telebirr, M-Pesa, bank, card, Stripe.
- Whether Google Meet links are **created automatically or by the seller**, which Google account owns the meeting, the access settings ("Ask to join"), and whether agents may send links to customers.
- Which events send email and SMS notifications, the sender names, and whether phone OTP exists.
- Which time zone the platform shows (always EAT, or the device's time), and whether Ethiopian-clock times are shown.

### B. Official contact points
- The official Telegram handle, support email, phone number and support hours (used as `{{support_channel}}`). Publishing these also helps customers spot impersonators.
- An on-call path for Critical safety, fraud and security cases outside office hours.
- Named contacts for legal, police, regulator and media requests.

### C. Refunds, cancellations and no-shows
- Refund eligibility and deadlines for each offering: one-on-one, group, physical, digital and inventory-free.
- Full vs. partial refunds, any deductions (payment-provider fees), and whether refunds ever go anywhere other than the original payment method.
- **Who may approve refunds, and up to what amount.**
- Approved wording for review and processing times.
- No-show and lateness rules: grace periods for late buyers and late sellers, and what evidence counts as proof of a no-show.
- Cancellation and rescheduling deadlines for buyers and sellers; whether there is a self-service button.
- Group sessions: cancelling for low attendance, waitlists, transferring a place, what happens when the host doesn't show.
- How a consultation is marked "completed", and how long the window to dispute it is.

### D. Seller earnings and payouts
- Commission and fee rates (sellers ask constantly), whether buyers pay any fee, and VAT and withholding tax treatment.
- When earnings move from *pending* to *available*; holds during disputes.
- Payout methods, the minimum withdrawal, the processing schedule, and the internal threshold for "delayed".
- How refunds and chargebacks reduce seller earnings, including after a payout.
- **Changing payout details:** re-verification, a cooling-off period, and whether the account must be in the seller's own name. Last-minute changes are a fraud signal.

## Priority 2: accounts, sellers and trust

### E. Customer identity verification
- The checks needed before account changes: changing email or phone, recovery, deletion, merging accounts. The temporary rule is *contact from the registered channel plus two account-specific details*.
- Recovery when the customer has lost access to both their email and their phone.
- Whether ID documents can be requested, how they are stored, and who approves.
- Lock rules (number of attempts, how long, who can unlock) and the session timeout.
- Whether an email or phone held by an old account can be released (Ethiopian phone numbers get recycled).

### F. Seller verification and conduct
- The accepted ID and business documents, the verification method and the internal review target.
- Seller eligibility: minimum age, licence or TIN, sellers outside Ethiopia, business accounts, licences for medical, legal or financial advice.
- Resubmission limits, the appeal process, and which rejection reasons can be shared.
- The enforcement ladder (warning → restriction → suspension → ban), which reasons can be shared, and what happens to bookings and earnings during a suspension.
- A seller code of conduct; rules on off-platform contact and payment; performance thresholds.
- The **prohibited and restricted items and services list**. Proposals are in *pol-prohibited-items*.
- Listing review targets, which edits send a listing back to review, image rules, and how search ranking works.

### G. Privacy, data and security
- A published privacy policy and the Ethiopian data protection obligations that apply (needs legal confirmation).
- The process for data access and deletion requests, and how long data is kept (tickets, attachments, ID documents).
- A data-breach notification process; a policy for law-enforcement requests.
- Which external tools (AI, translation) may be used with customer data.
- A procedure for when customers send card numbers, PINs or ID documents through chat by mistake.

## Priority 3: expansion features (before launch)

### H. Physical products and delivery
- Delivery partners, areas, fees and timeframes (Addis Ababa first).
- Who is liable for loss or damage in transit; what counts as proof of delivery; whether seller packing photos are required.
- Returns and exchanges: who pays return delivery, non-returnable items, reporting deadlines; whether cash on delivery is offered.

### I. Digital products
- The access model: download limits, expiry, who can reset access; whether files may ever be delivered by hand.
- Refunds before and after download; whether access is revoked after a refund.
- A copyright complaint and counter-notice process.

### J. Inventory-free selling (reselling)
- Eligibility, the pricing and margin model, how sales are credited to a reseller, and which costs resellers carry.
- Supplier obligations, and who answers to the buyer and pays when fulfilment fails.
- Rules for resellers' marketing claims.

## Support operations

- Approve the internal response and resolution targets (Settings → Service targets). The current values are placeholders.
- The minimum waiting period before closing a ticket for "no response"; when resolved tickets are closed automatically.
- Whether quick FAQ answers should be logged as tickets.
- Whether phone calls are recorded, and the disclosure script.
- Who approves goodwill gestures or compensation.
- When to declare a mass incident, and how customers are informed publicly.
- Whether to support languages other than Amharic and English.
- **Native Amharic review** of all customer-facing Amharic text before it goes live. It was written carefully, but a native-speaking support lead should proofread it.

## Interim operating rules used in the content (confirm or change)

These sit in internal notes only, as triage guidance. They are never shown to customers.

- A paid session that is unconfirmed or has no link is **High** priority if it starts within 24 hours, and **Critical** if it starts within the hour.
- After hours, customers are asked to write "account security" / "የአካውንት ደህንነት" so urgent takeover cases are handled first.
- A payment is "verified" only when its transaction reference matches the records. Screenshots alone are never proof.
