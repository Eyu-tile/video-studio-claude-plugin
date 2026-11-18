# Byfluence Support Content — Authoring Format

All seed content for the support system is written as Markdown files in this folder.
`npm run seed` parses them into the database. After seeding, everything is editable inside the
app (Documentation Management), so these files are only the **initial** content.

Read `taxonomy.json` first: it defines the only valid category/subcategory slugs, department keys,
feature keys and placeholders.

---

## 1. Ground rules (apply to every file)

1. **Never invent Byfluence policies.** No refund percentages, fees, commission rates, payout
   timelines, delivery times, deadlines, legal requirements, phone numbers, emails, Telegram handles,
   or office hours. Where a rule is needed but not confirmed, write it in a
   `## Policy Pending Approval` section as an open decision ("Decide whether…", "Confirm the…").
   In customer responses use neutral wording ("as soon as possible", "we will update you",
   `{{estimated_resolution_time}}`, `{{support_channel}}`) instead of concrete promises.
2. **Never ask customers for passwords, OTP/verification codes, full card numbers, CVV, PINs or
   mobile-money PINs.** Every "Information to Collect" list must respect this, and articles about
   login/payment should explicitly remind agents of it.
3. **Do not claim the agent performed actions they cannot perform.** Agents check information
   "through authorized tools (admin dashboard / payment provider portal, if you have access)".
   If they lack access, they escalate.
4. **Do not treat planned features as live.** Physical products, delivery, inventory-free selling,
   digital products, Telebirr/M-Pesa/card/Stripe payments are not confirmed as live. Tag them with
   `features:` so the app can show the live-status banner, and tell agents to check the
   *Feature Status* page before confirming availability to a customer.
5. **Amharic is the primary customer language.** Every customer-facing response has an English and
   an Amharic version. Write natural, polite Amharic (use the respectful form "እርስዎ", "እባክዎ",
   "ይቅርታ እንጠይቃለን"). Keep placeholders, IDs, brand names (Byfluence, Google Meet, Chapa,
   Telebirr) and transaction references unchanged inside Amharic text.
6. **Be practical and specific.** Write as a Customer Support Director training real agents.
   Steps must be actionable ("Ask for the transaction reference shown in the payment SMS or
   receipt", "Check the booking status in the admin dashboard"). Avoid filler.
7. Use only these placeholders inside responses (double curly braces):
   `{{customer_name}} {{ticket_id}} {{order_id}} {{consultation_id}} {{transaction_id}}
   {{support_agent}} {{estimated_resolution_time}} {{seller_name}} {{booking_date}}
   {{booking_time}} {{product_name}} {{amount}} {{payment_method}} {{follow_up_time}}
   {{support_channel}}`
8. IDs are lowercase-kebab, globally unique, prefixed by area (e.g. `reg-`, `acc-`, `buy-`, `sel-`,
   `lst-`, `con-`, `grp-`, `phy-`, `inv-`, `dig-`, `pay-`, `out-`, `ref-`, `tec-`, `tns-`, `gen-`,
   `faq-`, `tpl-`, `sop-`, `pol-`, `com-`, `trn-`). `related:` and `templates:` may reference IDs
   written by other authors; use the ID plans given in your brief so links resolve. Unknown IDs are
   ignored at seed time (not an error).

---

## 2. Document files (`kb/`, `faqs/`, `sops/`, `policies/`, `communication/`)

A file contains one or more documents. Each document starts with the marker line `<!-- doc -->`,
then an H1 title, then `key: value` metadata lines, then `## Section` blocks.

```
<!-- doc -->
# Title of the document
id: pay-paid-booking-not-confirmed
type: article
category: payments
subcategory: payment-mismatch
audience: buyer
priority: high
department: payments
features: consultations-1on1, payments-chapa
tags: paid but no booking, money deducted, booking missing, ክፍያ ተቆርጧል
related: pay-pending-transaction, con-booking-confirmation
templates: tpl-payment-investigation, tpl-request-transaction-ref
policy_pending: yes

## Summary
...
```

### Metadata keys

| key | values | notes |
|---|---|---|
| id | kebab id | required, unique |
| type | `article` `troubleshooting` `faq` `sop` `policy` `guide` | required |
| category | slug from taxonomy (scope depends on type) | kb scope for article/troubleshooting/faq; `sop` scope for sop; `policy` for policy; `communication` for guide |
| subcategory | subcategory slug of that category | kb types only |
| audience | `buyer` `seller` `both` `internal` | who the issue affects |
| priority | `low` `medium` `high` `critical` | default ticket priority suggested for this issue |
| department | department key | default escalation department |
| features | comma list of feature keys | optional; drives live-status banner |
| tags | comma list | synonyms customers/agents might type, incl. Amharic words. 5–12 tags. |
| related | comma list of doc ids | 2–6 |
| templates | comma list of template ids | optional |
| policy_pending | `yes` / `no` | `yes` if the doc contains a Policy Pending Approval section |

### Section headings

Use these exact headings (omit ones that don't apply; order as listed).

**article** and **troubleshooting**
- `## Summary` — required, 1–2 sentences, plain text.
- `## Overview` — for how-to / informational articles (instead of, or before, Issue Description).
- `## Issue Description`
- `## Possible Causes`
- `## Information to Collect` — bullet list; never passwords/OTP/PIN/card numbers.
- `## Troubleshooting Steps` — numbered steps; may contain `### sub-headings` and `- [ ]` checklists.
- `## Customer Steps` — steps the customer can do themselves (for how-to articles).
- `## Recommended Response (EN)` / `## Recommended Response (AM)` — full, ready-to-copy message.
- `## Short Response (EN)` / `## Short Response (AM)` — Telegram-length version.
- `## Follow-Up Response (EN)` / `## Follow-Up Response (AM)` — when unresolved after first contact.
- `## Escalation Conditions` — bullet list of when to escalate and to whom.
- `## Resolution Procedure` — how to confirm it's resolved and what to record before closing.
- `## Policy Pending Approval` — open decisions management must make (as bullets).
- `## Internal Notes` — agent-only guidance, pitfalls, fraud signals. (Never shown to the future AI assistant.)

Troubleshooting guides are broader diagnostic playbooks (e.g. "Master guide: payment problems").
They usually use Overview + Troubleshooting Steps with `### Step / decision` subsections, + Escalation.

**faq** — short customer-facing answers.
- `## Answer (EN)`
- `## Answer (AM)`
- `## Internal Notes` (optional)

**sop**
- `## Summary`, `## Objective`, `## When to Use`, `## Responsible`, `## Required Information`,
  `## Steps`, `## Expected Outcome`, `## Common Mistakes`, `## Escalation`, `## Related Templates`
  (bullet list of template ids/titles), `## Internal Notes`.

**policy**
- `## Summary`, `## Purpose`, `## Scope`, `## Confirmed Rules` (only facts given in the business
  overview or universal safety rules), `## Rules for Support Staff`, `## Policy Pending Approval`,
  `## Internal Notes`.

**guide** (Customer Communication)
- `## Summary`, `## Overview`, `## Guidelines`, `## Examples`, `## Do and Don't`, `## Internal Notes`.
  Extra custom `##` headings are allowed in guides and SOPs.

### Markdown features available
- Lists, numbered lists, **bold**, *italic*, tables, links, `### sub-headings`.
- Checklists: `- [ ] Check the booking status`.
- Callouts (blockquote with a tag on the first line):
  - `> [!NOTE] text` — information
  - `> [!TIP] text` — helpful advice
  - `> [!WARNING] text` — risk / don't do this
  - `> [!POLICY] text` — "Policy pending approval" marker inline

---

## 3. Response templates (`templates/`)

```
<!-- template -->
# Seller did not join — acknowledgment
id: tpl-seller-no-show-ack
category: consultations
channel: telegram
style: standard
tags: no-show, seller absent, meeting
related: con-seller-no-show

## Subject (EN)
(email templates only)

## Subject (AM)

## Message (EN)
Hello {{customer_name}}, ...

## Message (AM)
ሰላም {{customer_name}}፣ ...

## Usage Notes
When to use it, what to fill in, what not to promise.
```

- `channel`: `telegram` `email` `chat` `sms` `phone` `any`
- `style`: `short` `standard` `detailed` `formal` `friendly`
- Phone templates are call scripts (what to say), written as spoken language.
- SMS templates must be short (≈160 chars EN where possible).

---

## 4. Training modules (`training/`)

```
<!-- module -->
# Introduction to Byfluence
id: trn-01
number: 1
duration: 45

## Learning Objectives
- ...

## Lesson
Long-form teaching content with ### sub-headings, tables, callouts.

## Realistic Examples
### Example 1: ...

## Practical Exercises
1. ...

## Knowledge Check
Q: What is Byfluence's role in a consultation booking?
- [ ] It provides the consultation itself
- [x] It facilitates the transaction between buyer and seller
- [ ] It only hosts Google Meet
> Byfluence is a marketplace facilitator; the seller delivers the service.

Q: Next question...
```

Each knowledge-check question: `Q:` line, 3–4 options with exactly one `[x]`, then `>` explanation.

---

## 5. Gold-standard example (match this depth and tone)

```
<!-- doc -->
# Customer Paid but Consultation Booking Was Not Confirmed
id: pay-paid-booking-not-confirmed
type: article
category: payments
subcategory: payment-mismatch
audience: buyer
priority: high
department: payments
features: consultations-1on1, payments-chapa
tags: paid but no booking, money deducted no confirmation, booking missing after payment, payment successful booking not showing, ክፍያ ተቆርጧል, ቀጠሮ አልተረጋገጠም
related: pay-pending-transaction, pay-duplicate-charge, con-booking-confirmation, con-missing-meet-link
templates: tpl-request-transaction-ref, tpl-payment-investigation, tpl-payment-verified-booking-confirmed
policy_pending: yes

## Summary
The customer says money left their account for a consultation, but no confirmed booking appears in their dashboard and they did not receive a confirmation.

## Issue Description
The buyer completed (or believes they completed) payment for a one-on-one or group consultation. Their bank or mobile-money account shows a deduction, but Byfluence shows no confirmed booking, the booking is stuck as pending, or they never received a confirmation message. The customer is usually worried that they lost money and that their time slot will be given to someone else. Treat this as high priority when the session is within the next 24 hours.

## Possible Causes
- The payment provider confirmed the payment late, so the booking is still pending confirmation.
- The confirmation callback from the payment provider to Byfluence failed or timed out.
- The customer closed the browser before being redirected back to Byfluence.
- The payment actually failed or was reversed, but the customer saw a temporary hold/deduction.
- The customer paid twice and one payment was attached to the booking while the other was not.
- The booking was made from a different account (e.g., a second email address).
- The time slot was taken by another buyer while the customer was paying.

## Information to Collect
- Customer full name and registered email or phone number
- Consultation name and seller/consultant name
- Booking date and time they selected
- Payment method used (e.g., Chapa) and date/time of payment
- Transaction reference from the payment receipt or SMS
- Amount paid
- Screenshot of the payment receipt or confirmation message (optional but helpful)

> [!WARNING] Never ask for passwords, OTP codes, PINs or full card numbers. A transaction reference and a receipt screenshot are enough.

## Troubleshooting Steps
1. Confirm the customer's identity using their registered email or phone number.
2. Search the customer's account for bookings created around the payment time (check pending and cancelled bookings too).
3. Search the transaction by reference in the payments section of the admin dashboard (or the provider portal if you have authorized access).
4. Decide the case:
   - **Payment successful + booking pending** → escalate to Payments to confirm the booking manually; tell the customer their payment is recorded.
   - **Payment successful + no booking at all** → escalate to Payments with the reference; check whether the slot is still available.
   - **Payment not found / failed** → explain that no successful payment was recorded; ask them to check with their provider whether the amount was reversed.
   - **Two payments for one booking** → follow *Customer Charged Twice*.
5. If the session is soon (within 24 hours), mark the ticket **High** or **Critical** and notify the seller-side team so the slot is protected.
6. Record the transaction reference, booking ID and findings in the ticket internal notes.

- [ ] Identity confirmed
- [ ] Transaction located (or confirmed missing)
- [ ] Booking status checked
- [ ] Ticket created with references

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Support, and I'm sorry for the worry this has caused. I understand you paid for your consultation but have not received a booking confirmation.

To check this quickly, please send me:
1. The transaction reference from your payment receipt or SMS
2. The date and time of the payment
3. The consultation and consultant name you booked

Please do not share your password, PIN or any verification code — we will never ask for them.

Your case number is {{ticket_id}}. I will update you as soon as we have checked the payment.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

Byfluence ድጋፍን ስላገኙን እናመሰግናለን፤ ለተፈጠረው ስጋት ይቅርታ እንጠይቃለን። ለምክክሩ ክፍያ እንደፈጸሙ ነገር ግን የቀጠሮ ማረጋገጫ እንዳልደረሰዎት ተረድቻለሁ።

በፍጥነት ለማጣራት እባክዎ የሚከተሉትን ይላኩልኝ፦
1. ከክፍያ ደረሰኝዎ ወይም ከኤስኤምኤስ መልዕክቱ ላይ ያለውን የግብይት መለያ ቁጥር (transaction reference)
2. ክፍያውን የፈጸሙበትን ቀን እና ሰዓት
3. ያስያዙትን የምክክር ርዕስ እና የአማካሪውን ስም

እባክዎ የይለፍ ቃልዎን፣ ፒንዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አያጋሩ — በፍጹም አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው። ክፍያውን እንዳጣራን ወዲያውኑ መረጃ እሰጥዎታለሁ።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry about this! Please send the transaction reference from your receipt/SMS, the payment time, and the consultation you booked. I'll check it right away. (Never share your PIN or codes.) Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለተፈጠረው ችግር ይቅርታ! እባክዎ ከደረሰኙ/ኤስኤምኤሱ ላይ ያለውን የግብይት ቁጥር፣ የክፍያውን ሰዓት እና ያስያዙትን ምክክር ይላኩልኝ። ወዲያውኑ አጣራለሁ። (ፒን ወይም ኮድ በፍጹም አያጋሩ።) የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our payments team is still verifying transaction {{transaction_id}} with the payment provider. Your case is being actively handled and we will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ቡድናችን የግብይት ቁጥር {{transaction_id}}ን ከክፍያ አቅራቢው ጋር እያጣራ ነው። ጉዳይዎ በንቃት እየተከታተለ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Payment is confirmed in the provider records but the booking cannot be confirmed by support → **Payments & Finance**.
- The session starts within 24 hours and the booking is still unconfirmed → **Payments & Finance**, priority High/Critical, and notify a supervisor.
- The customer was charged more than once → **Payments & Finance**.
- You cannot see payment records with your access level → **Senior Support / Supervisor**.
- Signs of fraud (reference belongs to another account, edited screenshot) → **Trust & Safety**.

## Resolution Procedure
1. Confirm the booking now shows as confirmed in the customer's dashboard (or that a refund/reversal is confirmed by Payments).
2. Confirm the customer has the meeting details for the session.
3. Send the resolution message and ask the customer to confirm.
4. Record root cause (e.g., "provider callback delay"), actions taken and final resolution in the ticket before resolving.

## Policy Pending Approval
- Confirm the official process when payment succeeded but the slot was taken by another buyer (rebook vs. refund).
- Confirm who is authorized to manually confirm a booking after payment verification.
- Confirm the approved wording for how long payment verification usually takes.

## Internal Notes
- Most cases are a delayed provider callback; check the timestamp gap between payment and booking.
- Screenshots can be edited — always verify by transaction reference, never by screenshot alone.
- If several customers report this at the same time, it may be a system-wide incident: alert the supervisor and check Announcements.
```
