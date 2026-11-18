<!-- module -->
# Payments and Refunds
id: trn-06
number: 6
duration: 75

## Learning Objectives
- Describe the Byfluence payment flow and identify where a customer's problem sits in it.
- Explain each payment status (Pending, Successful, Failed, Canceled, Refund Pending, Refunded, Disputed) and what you tell the customer for each.
- Collect and record a transaction reference correctly, and verify payments by reference rather than by screenshot.
- Handle paid-but-not-confirmed, pending, failed-but-deducted, duplicate and wrong-amount cases using the Knowledge Base.
- Route refund requests through the confirmed support workflow while refund policy is Policy Pending Approval — without approving, refusing or promising anything.
- Recognise payment fraud signals and escalate them to Trust & Safety.

## Lesson

### The payment flow
1. Buyer selects a service (or, when live, a product).
2. The amount is calculated.
3. Buyer chooses a payment method.
4. Buyer pays.
5. The payment provider processes the payment.
6. **Byfluence receives confirmation** from the provider.
7. The order or booking is confirmed.
8. Records are updated.

Most payment tickets come from a gap between step 4 or 5 (the customer sees money leave) and step 6 or 7 (Byfluence has not confirmed). The customer experiences this as "I paid and got nothing" — a frightening moment. Your calm, structured approach is what restores trust.

### Payment methods: check before you speak
Byfluence has worked with or considered **Chapa, Telebirr, M-Pesa, bank-based methods and Stripe** (for potential international payments). **The availability of each one is not confirmed.** Before you mention any method to a customer, check the Feature Status page. If a customer says "I paid with Telebirr" and Telebirr is not listed as live, do not argue — ask for the receipt and reference and escalate to Payments & Finance; the payment may have gone through an aggregator, or it may not be a Byfluence payment at all.

### Payment statuses
| Status | Meaning | What you tell the customer | Typical action |
|---|---|---|---|
| **Pending** | Payment started, final confirmation not yet received | "Your payment is being confirmed; I'm checking it." | Verify by reference; if stuck, Payments & Finance |
| **Successful** | Provider confirmed; Byfluence recorded it | "Your payment was received." | If booking still not confirmed → paid-but-not-confirmed article |
| **Failed** | Payment did not go through | "The payment was not completed." Ask them to check with their provider whether any amount was held or reversed | If money was deducted anyway → Payments & Finance |
| **Canceled** | Payment was cancelled before completion | Explain it was not completed; they may try again | Check for duplicate attempts |
| **Refund Pending** | A refund has been approved and is being processed | "Your refund is being processed." No date unless approved wording exists | Follow up with Payments & Finance if it stalls |
| **Refunded** | Refund completed by Byfluence | "The refund has been processed on our side." Their provider may take its own time to show it | Ask for their statement only if they still don't see it |
| **Disputed** | Payment is under dispute (e.g., chargeback or formal complaint) | "This payment is under review." | Payments & Finance; Senior Support for buyer–seller side |

> [!NOTE] **Refund Pending** means a refund has already been approved and is in progress. Do not use this phrase for a refund the customer has only *requested* — that is a request under review.

### Transaction references
The transaction reference is the identifier from the payment provider, shown on the customer's receipt, SMS confirmation or in their app's transaction history. It is the single most useful piece of payment information.

- Ask for it in plain words: "the reference number on your payment SMS or receipt" — "በክፍያ ኤስኤምኤስዎ ወይም ደረሰኝዎ ላይ ያለው የግብይት መለያ ቁጥር".
- Also collect: payment date and time, amount, payment method, the service/consultation it was for, and the registered email/phone of the account.
- Enter it in the ticket's **transaction reference** field (it fills `{{transaction_id}}` in templates), not only in a note. This makes it searchable for the next agent.
- **Verify by reference, never by screenshot alone.** Screenshots can be edited. A screenshot is supporting evidence; the reference checked through authorized tools (admin dashboard or provider portal, if you have access) is the proof.

> [!WARNING] Never ask for a PIN, mobile-money PIN, password, OTP, full card number or CVV. A reference and receipt are enough for every legitimate check.

### Verification workflow
1. Confirm the customer's identity (registered email/phone).
2. Search the customer's account for transactions and bookings around the payment time — include pending and cancelled ones.
3. Search the transaction by reference through your authorized tools.
4. Match: amount, time, account, and the booking it should belong to.
5. Decide the case using the Knowledge Base article; if you **do not have access** to payment records, escalate to Senior Support / Supervisor rather than guessing.
6. Record what you found in internal notes: reference, status seen, booking ID, mismatch found.

### Common payment cases
| Customer says | Likely case | Article / action |
|---|---|---|
| "Money was deducted but no booking" | Paid but not confirmed | *Customer Paid but Consultation Booking Was Not Confirmed* → Payments & Finance if payment is successful but booking isn't |
| "It's been loading / says pending" | Pending payment | Verify by reference; avoid a second attempt until checked |
| "It said failed but my balance went down" | Failed with hold or deduction | Ask them to check with their provider; escalate with reference |
| "I was charged twice" | Duplicate charge | Collect both references; Payments & Finance |
| "I was charged more than the price" | Wrong amount | Compare listing price and amount; Payments & Finance |
| "My bank says I didn't authorize this" | Possible fraud / dispute | Trust & Safety and Payments & Finance |

> [!TIP] If several customers report the same payment problem at the same time, it may be a provider or system incident. Alert your supervisor, check Announcements, and reference one master ticket in the others.

### Refunds: the routing rule
Refund eligibility, deadlines, deductions and approval authority **must be set by official policy and are not yet established**. On the Feature Status page, "Refund processing" is unconfirmed. Different categories (consultations, group sessions, future products) may get different policies.

The confirmed **support workflow** for refunds and disputes is:
1. Receive the complaint
2. Identify the transaction
3. Collect evidence
4. Review the applicable policy (or its Policy Pending Approval marker)
5. Contact the seller or the responsible department
6. **Authorized personnel decide**
7. Explain the decision to the customer
8. Process approved adjustments (by the responsible team)
9. Document and close

Your part is steps 1–5, 7 and 9. **You never approve or refuse a refund yourself.**

| You can say | You cannot say |
|---|---|
| "I've recorded your refund request with all the details." | "You'll get a full refund." |
| "The team responsible will review it according to Byfluence's policy." | "Refunds aren't allowed." |
| "I'll update you as soon as there's a decision." | "It takes 7 days." |
| "Your case number is {{ticket_id}}." | "I've refunded you." (unless Payments confirmed it) |

### Handling "Policy Pending Approval" in payments
1. Read the policy section and the marker so you know exactly which decision is pending.
2. Do not fill the gap with your own judgement or another company's rules.
3. Create the ticket with references, evidence and the customer's request in their own words.
4. Escalate to **Senior Support / Supervisor** (or the department named in the article) with a clear note: what is requested, what policy is pending, what evidence exists.
5. Tell the customer honestly that the request is under review and give the case number.
6. Set a follow-up so the customer hears from you even if there is no decision yet.

### Disputes and chargebacks
If a customer says they will contact their bank to reverse the payment, or the payment shows as Disputed, involve **Payments & Finance**. Do not discourage a customer from using their legal rights, and do not threaten them. Simply explain that Byfluence is reviewing the case and record it.

### Fraud signals
- A transaction reference that belongs to another account or another amount.
- A receipt screenshot with inconsistent fonts, times or amounts.
- A request to refund to a **different** account or phone number than the one that paid.
- A seller asking a buyer to pay **outside** Byfluence.
- Pressure: "Refund me now or I'll post everywhere" combined with inconsistent details.

Escalate these to **Trust & Safety** and never reveal what made you suspicious.

## Realistic Examples

### Example 1: Paid but not confirmed (Amharic)
**Customer (Telegram):**
> ሰላም፣ ለነገ ምክክር ከፍያለሁ፤ ገንዘቡ ከአካውንቴ ተቆርጧል ግን ቀጠሮው "pending" ይላል።

*(Hello, I paid for tomorrow's consultation; the money was deducted but the booking says "pending".)*

**Agent action:** Opens *Customer Paid but Consultation Booking Was Not Confirmed*. Priority High (session tomorrow). Uses the request-transaction-reference template in Amharic. Once the reference arrives, verifies it; payment successful + booking pending → escalate to Payments & Finance; ticket status Escalated.

**Model reply (AM):**
> ሰላም {{customer_name}}፣ ስለተፈጠረው ስጋት ይቅርታ እንጠይቃለን። ለማጣራት እባክዎ በክፍያ ኤስኤምኤስዎ ወይም ደረሰኝዎ ላይ ያለውን የግብይት ቁጥር፣ የከፈሉበትን ሰዓት እና መጠኑን ይላኩልኝ። የይለፍ ቃል፣ ፒን ወይም ኮድ በፍጹም አያጋሩ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

### Example 2: Duplicate charge (English)
**Customer (email):**
> The page froze so I paid again. Now I see two payments for the same consultation.

**Agent action:** Asks for both references and times; verifies both; records both in the ticket (one in the transaction field, the second in internal notes); escalates to Payments & Finance. Tells the customer the duplicate is being reviewed — not "you will be refunded in X days".

### Example 3: Refund request while policy is pending
**Customer (Telegram, Amharic):**
> ምክክሩን ማድረግ አልችልም፤ ገንዘቤን መልሱልኝ።

*(I can't attend the consultation; give me my money back.)*

**Agent reasoning:** No approved cancellation/refund rule. The agent collects the consultation ID and reason, checks whether a cancel action exists in the dashboard, records the request, escalates to Senior Support, and replies:

> ጥያቄዎን ተቀብለናል። የተመላሽ ገንዘብ ጥያቄዎ ከሙሉ መረጃው ጋር ተመዝግቦ ለሚመለከተው ቡድን ተላልፏል። ውሳኔው እንደደረሰን እናሳውቅዎታለን። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

### Example 4: Suspicious refund destination
**Customer (Telegram, English):**
> Please send my refund to this other Telebirr number, my old one is closed.

**Agent action:** Does not agree or refuse on the spot; records the request, flags it in internal notes, escalates to **Trust & Safety** and Payments & Finance. Replies that refund details are verified by a specialised team.

## Practical Exercises
1. **Status card.** Using this lesson and the Payments category, write a one-line EN and AM explanation for each of the seven payment statuses. Keep it in your notes for live use.
2. **Gold article walk-through.** Open *Customer Paid but Consultation Booking Was Not Confirmed*. Run its troubleshooting steps on a practice ticket: fill customer info, category Payments → Paid but Not Confirmed / Wrong Amounts, priority, transaction reference field, and the checklist in internal notes.
3. **Feature Status for payments.** Open Feature Status and record the status of Chapa, Telebirr, M-Pesa, bank, card and Stripe. Write how you would answer "Can I pay with M-Pesa?" today.
4. **Refund escalation note.** Write an escalation note for Example 3 that a Senior Support agent could act on without asking you anything: request, references, evidence, policy pending, customer's preferred language.
5. **Fraud spotting.** Your trainer will show three receipt screenshots and references. Decide which ones you would escalate to Trust & Safety and write the internal note (without accusing the customer).

## Knowledge Check
Q: What is the best proof that a payment was made?
- [ ] A screenshot of the receipt
- [ ] The customer's word
- [x] The transaction reference verified through authorized tools
- [ ] The seller's confirmation
> Screenshots can be edited; verify by reference. Screenshots are supporting evidence only.

Q: What does "Refund Pending" mean?
- [x] A refund has been approved and is being processed
- [ ] The customer has asked for a refund
- [ ] The refund was refused
- [ ] The payment is still being confirmed
> Refund Pending is an approved refund in progress — not a request under review.

Q: A customer asks for a refund. Refund policy is Policy Pending Approval. What do you do?
- [ ] Approve it because the amount is small
- [ ] Refuse it because there is no policy
- [x] Collect evidence, record the request, escalate to Senior Support / Supervisor and keep the customer updated
- [ ] Ask the seller to refund the buyer directly in cash
> Authorized personnel decide refunds. Agents never approve or refuse.

Q: A customer paid twice for one booking. Which department handles it?
- [x] Payments & Finance
- [ ] Technical
- [ ] Seller Operations
- [ ] Logistics & Fulfillment
> Duplicate charges go to Payments & Finance with both references.

Q: Which information must you never request when investigating a payment?
- [ ] Transaction reference
- [ ] Payment date and amount
- [x] Mobile-money PIN or OTP
- [ ] Payment method used
> PINs, OTPs, passwords, full card numbers and CVV are never requested.

Q: A customer insists they paid with a method that Feature Status does not show as live. What do you do?
- [ ] Tell them they are wrong
- [x] Ask for the receipt and reference and escalate to Payments & Finance for verification
- [ ] Close the ticket as invalid
> Don't argue; verify by reference and escalate.

Q: Where should the transaction reference be recorded in the ticket?
- [x] In the ticket's transaction reference field (plus notes if there are several)
- [ ] Only in the customer message history
- [ ] Nowhere — it is sensitive
> The reference field makes it searchable and fills {{transaction_id}} in templates.

Q: A customer asks for their refund to be sent to a different phone number than the one that paid. What is the right action?
- [ ] Agree, since it's their money
- [ ] Refuse and close the ticket
- [x] Record it, flag it as a possible fraud signal and escalate to Trust & Safety and Payments & Finance
> Refunds to different destinations are a classic fraud pattern and need specialised verification.

Q: Which step of the refund workflow is never done by a Level 1 agent?
- [ ] Identifying the transaction
- [ ] Collecting evidence
- [x] Deciding whether the refund is approved
- [ ] Documenting and closing
> Authorized personnel decide; support collects, routes, explains and documents.
