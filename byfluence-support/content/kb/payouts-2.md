<!-- doc -->
# Withdrawal Cancelled or Rejected
id: out-withdrawal-cancelled
type: article
category: payouts
subcategory: withdrawals
audience: seller
priority: medium
department: payments
features: seller-withdrawals
tags: withdrawal rejected, withdrawal cancelled, payout declined, why was my withdrawal rejected, withdrawal denied, የወጪ ጥያቄ ውድቅ ሆነ, ገንዘብ ማውጣት ተሰረዘ
related: out-withdrawal-approval, out-incorrect-bank-details, out-payout-hold-restriction, out-failed-payout, out-how-to-withdraw
templates: tpl-withdrawal-status
policy_pending: yes

## Summary
A seller's withdrawal request was cancelled or rejected. Find the recorded reason, explain what the seller can do, and confirm the amount returned to their balance.

## Issue Description
The seller sees their withdrawal marked as cancelled or rejected, or received a notification saying so. They want to know why and when they can get their money. A rejected withdrawal normally does **not** mean the earnings are lost — the amount is expected to return to the Available Balance (to be confirmed per case) unless a hold, dispute or adjustment applies.

## Possible Causes
- Payout details invalid, incomplete or in a different name from the seller.
- Amount above the Available Balance (e.g. a refund or chargeback reduced it after the request).
- Seller account not Verified, or Suspended/Banned.
- Payout hold due to disputes, chargebacks or investigation.
- Fraud review: recent payout-detail change, unusual activity.
- Seller cancelled the request themselves.
- Amount below a minimum (minimums not confirmed).
- Duplicate request.

## Information to Collect
- Seller identity (registered email or phone number)
- Withdrawal date, amount and any reference shown in the dashboard
- Screenshot of the rejection/cancellation message
- Whether the seller changed payout details recently

> [!WARNING] Never ask for passwords, PINs or OTPs. Never take new payout details over chat — the seller updates them in the dashboard following the approved process.

## Troubleshooting Steps
1. Verify identity.
2. Find the withdrawal and the recorded rejection/cancellation reason in the admin dashboard.
3. Check that the amount returned to the Available Balance (or where it is now).
4. Act on the reason:
   - **Invalid payout details** → ask the seller to correct them in the dashboard (see *Wrong Bank/Mobile-Money Payout Details*), then resubmit.
   - **Balance changed** → explain the adjustment (refund/chargeback) neutrally; resubmit for the correct amount.
   - **Account status / hold** → follow *Payouts on Hold / Restricted*; do not reveal investigation details.
   - **Fraud review** → do not discuss; escalate to **Trust & Safety** if not already handled.
   - **Seller cancelled** → confirm and guide resubmission.
   - **No reason recorded** → escalate to **Payments & Finance**.
5. Record the reason and next step in the ticket.

- [ ] Identity verified
- [ ] Rejection reason found
- [ ] Balance location confirmed
- [ ] Next step explained or escalated

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Seller Support. I'm sorry your withdrawal of {{amount}} was not completed.

I have checked your request. [Reason in plain words, e.g. "The payout details on your account could not be used."] 

What to do next: [e.g. "Please update your payout details in your seller dashboard and submit a new withdrawal request."]

The amount from this request is shown in your balance as: [Available / on hold]. If you have any questions, just reply here.

Please never share your password, PIN or verification codes — we will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

የ Byfluence የሻጭ ድጋፍን ስላገኙን እናመሰግናለን። የ {{amount}} የገንዘብ ማውጫ ጥያቄዎ ባለመጠናቀቁ ይቅርታ እንጠይቃለን።

ጥያቄዎን አጣርቻለሁ። [ምክንያቱ በቀላል ቋንቋ፣ ለምሳሌ "በመለያዎ ላይ ያሉት የክፍያ መቀበያ ዝርዝሮች ጥቅም ላይ ሊውሉ አልቻሉም።"]

ቀጣይ እርምጃ፦ [ለምሳሌ "እባክዎ በሻጭ ዳሽቦርድዎ ላይ የክፍያ መቀበያ ዝርዝሮችዎን አስተካክለው አዲስ ጥያቄ ያቅርቡ።"]

ከዚህ ጥያቄ የነበረው መጠን በሂሳብዎ ላይ እንደሚከተለው ይታያል፦ [ለማውጣት ዝግጁ / ታግዷል]። ጥያቄ ካለዎት እዚሁ ይጻፉልን።

እባክዎ የይለፍ ቃልዎን፣ ፒንዎን ወይም የማረጋገጫ ኮድ በፍጹም አያጋሩ — አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry your {{amount}} withdrawal wasn't completed. Reason: [reason]. Next step: [action]. The amount is now [Available / on hold] in your balance. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ የ {{amount}} ጥያቄዎ ስላልተጠናቀቀ ይቅርታ። ምክንያት፦ [ምክንያት]። ቀጣይ እርምጃ፦ [እርምጃ]። መጠኑ አሁን በሂሳብዎ [ዝግጁ / ታግዷል] ነው። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our payments team is reviewing why your withdrawal of {{amount}} was not completed. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ቡድናችን የ {{amount}} የገንዘብ ማውጫ ጥያቄዎ ለምን እንዳልተጠናቀቀ እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- No rejection reason recorded, or the amount did not return to the balance → **Payments & Finance**.
- Rejection due to fraud review, or the seller pushes to change payout details urgently → **Trust & Safety**.
- Account restriction/suspension → **Seller Operations**.
- Repeated rejections for the same seller without clear reason → **Senior Support / Supervisor**.

## Resolution Procedure
1. Confirm the seller understands the reason and the next step.
2. If resubmitted, confirm the new request appears as Withdrawal Pending.
3. Record reason, amount location and outcome; close.

## Policy Pending Approval
- Define the official list of rejection reasons and the message shown to sellers for each.
- Confirm that rejected amounts always return to the Available Balance (unless held) and how this is displayed.
- Define how many times a seller may resubmit and whether rejection fees apply (none may be quoted).

## Internal Notes
- Replace all bracketed text before sending.
- Never say "you were flagged for fraud". For fraud/investigation holds say "your account needs an additional review" and escalate.

<!-- doc -->
# Withdrawal Delayed
id: out-withdrawal-delayed
type: article
category: payouts
subcategory: payout-problems
audience: seller
priority: high
department: payments
features: seller-withdrawals
tags: withdrawal delayed, payout late, withdrawal still pending, haven't received payout, where is my money, payout taking long, ገንዘቤ አልደረሰም, ክፍያ ዘገየ, የወጪ ጥያቄ ዘገየ
related: out-withdrawal-approval, out-failed-payout, out-incorrect-bank-details, out-payout-hold-restriction, out-tsg-payout-master
templates: tpl-withdrawal-delayed, tpl-withdrawal-status
policy_pending: yes

## Summary
A seller's withdrawal is still "pending" longer than they expected, or is marked completed but the money has not arrived. Locate the request, find where it is stuck and escalate — without promising a payout date.

## Issue Description
Two common situations:
1. **Still pending/processing** in Byfluence — the seller is waiting for approval or processing.
2. **Marked completed** in Byfluence but the seller's bank or mobile-money account shows nothing.

Sellers depend on this income, so delays cause frustration and sometimes threats to leave the platform. Payout timelines are **not confirmed**, so agents cannot say "it is late" against an official promise — they compare against the internal threshold set by Payments & Finance (pending).

## Possible Causes
- Request still in the review queue or batch processing.
- Additional review triggered (recent payout-detail change, large amount, new seller).
- Payout hold or account restriction.
- Payout details wrong — payout failed or bounced.
- Bank/mobile-money provider delay after Byfluence sent the payout.
- Public holidays or provider downtime.
- System error: request stuck or not submitted correctly.

## Information to Collect
- Seller identity (registered email or phone number)
- Withdrawal date, amount and status shown in the dashboard
- Payout method (bank/mobile money) — confirm only the last digits of the account/number
- If marked completed: whether they checked the right account, and any SMS from their bank/provider

> [!WARNING] Never ask for passwords, PINs or OTPs. Never ask the seller to send their full account details by chat to "re-send" a payout.

## Troubleshooting Steps
1. Verify identity.
2. Find the withdrawal in the admin dashboard; record date, amount, status and payout destination (last digits).
3. Compare with the internal processing threshold (from Payments & Finance; pending policy).
4. Decide:
   - **Pending, within threshold** → give a status update; set follow-up.
   - **Pending, beyond threshold** → escalate to **Payments & Finance** with details.
   - **On hold / restricted** → follow *Payouts on Hold / Restricted*.
   - **Failed / returned** → follow *Payout Failed*.
   - **Completed, not received** → confirm the destination (last digits) matches the seller's account; ask them to check the account and SMS. If still not received → **Payments & Finance** to obtain the payout reference/confirmation from the bank/provider.
   - **Destination does not belong to the seller** → urgent: **Trust & Safety** (possible account takeover / payout-detail fraud).
5. Record findings and the follow-up time.

- [ ] Identity verified
- [ ] Withdrawal located with status
- [ ] Destination (last digits) confirmed
- [ ] Escalated or follow-up set

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Seller Support, and I'm sorry you are still waiting for your withdrawal. I understand how important this payment is to you.

I have checked your withdrawal of {{amount}}: it is currently [status]. I have [shared it with our payments team for review / added a note to follow it up], and I will update you by {{follow_up_time}}.

To help us, please confirm the last few digits of the account or number you expect to receive the payment on, and whether you received any SMS from your bank or provider. Please do not send your PIN, password or any verification code.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

የ Byfluence የሻጭ ድጋፍን ስላገኙን እናመሰግናለን፤ አሁንም የገንዘብ ማውጫ ጥያቄዎን እየጠበቁ በመሆኑ ይቅርታ እንጠይቃለን። ይህ ክፍያ ለእርስዎ ምን ያህል አስፈላጊ እንደሆነ እረዳለሁ።

የ {{amount}} የገንዘብ ማውጫ ጥያቄዎን አጣርቻለሁ፦ አሁን [ሁኔታ] ላይ ነው። [ለክፍያ ቡድናችን ለግምገማ አስተላልፌዋለሁ / ለክትትል ማስታወሻ አስቀምጫለሁ]፤ እስከ {{follow_up_time}} ድረስ መረጃ እሰጥዎታለሁ።

እንዲረዳን እባክዎ ክፍያውን ይቀበሉበታል ብለው የሚጠብቁትን ሂሳብ ወይም ቁጥር የመጨረሻ ጥቂት አሃዞች እና ከባንክዎ ወይም ከአቅራቢዎ ኤስኤምኤስ ደርሶዎት እንደሆነ ያረጋግጡልን። እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ አይላኩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry for the wait. Your {{amount}} withdrawal is currently [status]; I've passed it to our payments team and will update you by {{follow_up_time}}. Please confirm the last digits of your payout account. Never share your PIN. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ስለ መዘግየቱ ይቅርታ። የ {{amount}} ጥያቄዎ አሁን [ሁኔታ] ላይ ነው፤ ለክፍያ ቡድናችን አስተላልፌዋለሁ፣ እስከ {{follow_up_time}} መረጃ እሰጥዎታለሁ። የመቀበያ ሂሳብዎን የመጨረሻ አሃዞች ያረጋግጡልን። ፒን አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our payments team is still working on your withdrawal of {{amount}}. Your case is being actively handled and we will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ቡድናችን የ {{amount}} የገንዘብ ማውጫ ጥያቄዎን አሁንም እያስተናገደ ነው። ጉዳይዎ በንቃት እየተከታተለ ሲሆን እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Pending beyond the internal threshold → **Payments & Finance**, priority High.
- Marked completed but not received after the seller checked → **Payments & Finance** for provider confirmation.
- Payout destination does not belong to the seller, or details changed without the seller's knowledge → **Trust & Safety**, priority Critical.
- Many sellers report delays at once → **Payments & Finance** + supervisor (possible processing incident).
- Seller threatens legal action or public complaint → **Senior Support / Supervisor**; **Management** if high-value.

## Resolution Procedure
1. Confirm with the seller that the money arrived (or that Payments has confirmed the payout with a provider reference).
2. Confirm the withdrawal shows as completed in the dashboard.
3. Record cause (queue, review, provider delay, failed details) and close.

## Policy Pending Approval
- Define the payout processing schedule and the internal "delayed" threshold.
- Approve wording on expected payout times for sellers.
- Decide whether sellers are compensated or prioritised after delays caused by Byfluence (none may be promised).

## Internal Notes
- Never say "it will arrive today/tomorrow". Use `{{follow_up_time}}` for when *we* will update them.
- A seller pushing to change payout details while a withdrawal is pending is a fraud signal — see *Wrong Bank/Mobile-Money Payout Details*.

<!-- doc -->
# Wrong Bank or Mobile-Money Payout Details
id: out-incorrect-bank-details
type: article
category: payouts
subcategory: payout-problems
audience: seller
priority: high
department: payments
features: seller-withdrawals
tags: wrong bank details, change payout account, wrong account number, update payout details, wrong Telebirr number, payout to wrong account, የተሳሳተ የባንክ ሂሳብ, የክፍያ መቀበያ ቀይር, የተሳሳተ ቁጥር
related: out-failed-payout, out-withdrawal-delayed, sel-change-business-details, tns-unauthorized-transaction, out-payout-hold-restriction
templates: tpl-withdrawal-status
policy_pending: yes

## Summary
A seller entered wrong payout details, wants to change them, or a payout went to the wrong account. Payout-detail changes are a top fraud signal — especially last-minute changes before or during a withdrawal — so verify identity carefully and never change details over chat.

## Issue Description
Situations include:
- The seller notices a typo in their bank account or mobile-money number before withdrawing.
- The seller wants to switch to a new bank or number.
- A withdrawal failed or bounced because of wrong details.
- A withdrawal went to an account the seller does not recognise.
- Someone (possibly an attacker with access to the seller's email/phone) asks to change the details "urgently" right before a large withdrawal.

> [!WARNING] **Fraud signal:** a request to change payout details shortly before or while a withdrawal is pending, especially combined with urgency, a new device/location, a recent password or email/phone change, or a name that does not match the seller's verified identity. Treat as possible account takeover and involve **Trust & Safety** before anything is processed.

## Possible Causes
- Typing mistake by the seller.
- Seller changed bank/number legitimately.
- Account in someone else's name (family member, business partner).
- Seller account compromised and details changed by an attacker.
- System error saving details.

## Information to Collect
- Seller identity: registered email or phone number, plus any additional identity checks required by policy (pending)
- What is wrong: the last few digits of the current (wrong) details and of the intended details — not the full numbers in chat
- Whether a withdrawal is pending, failed or completed, with date and amount
- When the details were last changed, and whether the seller made that change
- Account-holder name on the new account (must match the verified seller, as required by policy — pending)

> [!WARNING] Never ask for passwords, PINs, OTPs, or online-banking credentials. Do not accept full account numbers in chat to "update for them"; the seller updates details through the dashboard or approved process.

## Troubleshooting Steps
1. Verify the seller's identity thoroughly. If anything feels off (different phone, urgency, recent account changes), stop and escalate to **Trust & Safety**.
2. Check the audit history in the admin dashboard (if available): when were payout details last changed, from which session/device, and any recent email/phone/password changes.
3. Check withdrawals: pending, failed, completed — and their destinations (last digits).
4. Decide:
   - **No withdrawal pending, simple correction, no fraud signals** → guide the seller to update details in the dashboard (or the approved process, e.g. *Change Business Details*, `sel-change-business-details`). Remind them the name must match their verified identity (if required).
   - **Withdrawal pending with wrong details** → escalate to **Payments & Finance** to stop/hold the payout before it is sent.
   - **Payout already sent to a wrong account the seller entered** → escalate to **Payments & Finance**; recovery depends on the bank/provider. Do not promise recovery.
   - **Seller did not make the change / unknown account** → **Trust & Safety**, priority Critical; ask Payments to hold all withdrawals; advise the seller to secure their account (password reset via official flow).
5. Record everything, including the fraud-signal checks you made.

- [ ] Identity verified (extra care)
- [ ] Change history checked
- [ ] Withdrawals checked
- [ ] Fraud signals assessed
- [ ] Correct department involved

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Seller Support. I understand there is a problem with your payout details.

For your security, payout details can only be updated by you through your seller dashboard (or the official verification process), and the account should be in the name verified on your seller account. We never change payout details over chat.

To help me check your account, please confirm:
1. Your registered email or phone number
2. The last few digits of the account or number currently saved, and of the correct one
3. Whether you have a withdrawal pending right now

Please do not send your full account number, PIN, password or any verification code here.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

የ Byfluence የሻጭ ድጋፍን ስላገኙን እናመሰግናለን። በክፍያ መቀበያ ዝርዝሮችዎ ላይ ችግር እንዳለ ተረድቻለሁ።

ለደህንነትዎ ሲባል የክፍያ መቀበያ ዝርዝሮች ሊቀየሩ የሚችሉት በእርስዎ በኩል በሻጭ ዳሽቦርድዎ (ወይም በይፋዊ የማረጋገጫ ሂደት) ብቻ ነው፤ ሂሳቡም በሻጭ መለያዎ ላይ በተረጋገጠው ስም መሆን አለበት። የክፍያ ዝርዝሮችን በቻት በፍጹም አንቀይርም።

መለያዎን ለማጣራት እባክዎ የሚከተሉትን ያረጋግጡልኝ፦
1. የተመዘገበ ኢሜይልዎን ወይም ስልክ ቁጥርዎን
2. አሁን የተቀመጠውን እና ትክክለኛውን ሂሳብ ወይም ቁጥር የመጨረሻ ጥቂት አሃዞች
3. አሁን በሂደት ላይ ያለ የገንዘብ ማውጫ ጥያቄ እንዳለዎት

እባክዎ ሙሉ የሂሳብ ቁጥርዎን፣ ፒንዎን፣ የይለፍ ቃልዎን ወይም ማንኛውንም የማረጋገጫ ኮድ እዚህ አይላኩ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, for security, payout details can only be changed by you in your seller dashboard (in your verified name). Please confirm your registered email/phone, the last digits of the saved and correct accounts, and if a withdrawal is pending. Never send your PIN or full account number. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለደህንነት ሲባል የክፍያ ዝርዝሮችን መቀየር የሚችሉት እርስዎ በሻጭ ዳሽቦርድ ብቻ ነው (በተረጋገጠ ስምዎ)። የተመዘገበ ኢሜይል/ስልክዎን፣ የተቀመጠውንና ትክክለኛውን ሂሳብ የመጨረሻ አሃዞች እና በሂደት ያለ ጥያቄ እንዳለ ያረጋግጡ። ፒን ወይም ሙሉ የሂሳብ ቁጥር አይላኩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our team is reviewing your payout details and any related withdrawal for your security. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። ለደህንነትዎ ሲባል ቡድናችን የክፍያ መቀበያ ዝርዝሮችዎን እና ተያያዥ የገንዘብ ማውጫ ጥያቄዎን እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Wrong details with a withdrawal pending → **Payments & Finance** immediately (hold before sending), priority High.
- Payout sent to a wrong account → **Payments & Finance**, priority High.
- Seller did not make the change, unknown destination, or any fraud signal → **Trust & Safety**, priority Critical, and ask Payments to hold withdrawals.
- Account-holder name does not match verified identity → **Seller Operations**.
- Seller cannot update details in the dashboard (bug) → **Technical / Engineering**.

## Resolution Procedure
1. Confirm the correct details are saved by the seller (last digits only) and, where required, verified.
2. Confirm any held/failed withdrawal has been resubmitted or released by Payments.
3. If fraud was involved, confirm Trust & Safety has secured the account.
4. Record checks, changes and outcome.

## Policy Pending Approval
- Define how sellers change payout details (dashboard only? re-verification? cooling-off period before payouts to new details?).
- Confirm whether the payout account must be in the seller's own name, and exceptions for businesses.
- Define who may hold or release withdrawals after a suspicious change.
- Define what happens when a payout goes to a wrong account due to seller error.

## Internal Notes
- The combination "new details + urgent withdrawal + new phone/email" is the classic takeover pattern. Slow down even if the seller is upset.
- Only ever discuss the last few digits of account numbers.
- Never accept identity proof such as ID photos over Telegram unless a secure, approved process exists.

<!-- doc -->
# Payout Failed
id: out-failed-payout
type: article
category: payouts
subcategory: payout-problems
audience: seller
priority: high
department: payments
features: seller-withdrawals
tags: payout failed, withdrawal failed, payout returned, payout bounced, transfer failed, money returned to balance, ክፍያ አልተሳካም, ገንዘብ ማውጣት አልተሳካም
related: out-incorrect-bank-details, out-withdrawal-delayed, out-withdrawal-cancelled, out-how-to-withdraw, out-tsg-payout-master
templates: tpl-withdrawal-status, tpl-withdrawal-delayed
policy_pending: yes

## Summary
A seller's approved withdrawal could not be paid out — for example the bank or mobile-money provider rejected or returned it. Find the failure reason, make sure the amount is safe, and guide the seller to fix the cause.

## Issue Description
Unlike a *rejected* withdrawal (stopped by Byfluence review), a *failed* payout was sent for processing but did not reach the seller. The dashboard may show the withdrawal as failed, returned, or still processing, and the seller sees nothing in their account. They want to know where the money is.

## Possible Causes
- Account or mobile-money number wrong, closed, dormant or blocked.
- Account-holder name does not match.
- Mobile-money wallet limit reached or wallet not fully registered.
- Bank or provider technical failure.
- Payout method not supported for that bank/provider (not confirmed which are supported).
- Internal processing error.

## Information to Collect
- Seller identity
- Withdrawal date, amount and status
- Payout method and the last digits of the destination
- Any message from the bank/provider about the failure
- Whether the account/wallet is active and in the seller's name

> [!WARNING] Never ask for PINs, passwords, OTPs or full account numbers in chat.

## Troubleshooting Steps
1. Verify identity.
2. Find the withdrawal and the failure reason/code recorded by Payments & Finance (if visible).
3. Confirm where the amount is now (returned to Available Balance, held for re-processing, or unknown).
4. Decide:
   - **Wrong/closed account** → seller updates details (*Wrong Bank/Mobile-Money Payout Details*), then a new withdrawal or re-processing as Payments decides.
   - **Name mismatch** → **Seller Operations** to check verified identity vs account name.
   - **Wallet limit/registration issue** → seller contacts their provider to resolve, then retry.
   - **Provider/technical failure** → **Payments & Finance** to retry; no timeline promised.
   - **Amount not returned and not held** → **Payments & Finance**, priority High.
5. Record the reason and next steps.

- [ ] Identity verified
- [ ] Failure reason found
- [ ] Amount location confirmed
- [ ] Seller action / escalation done

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Seller Support, and I'm sorry your payout of {{amount}} did not reach you.

I have checked your withdrawal: the payment could not be completed because [reason in plain words]. The amount is currently [returned to your Available Balance / held while our payments team reviews it].

Next step: [e.g. "please check that your account is active and in your name, update your payout details in your dashboard if needed, and let us know"].

Please never share your PIN, password or verification codes — we will never ask for them.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

የ Byfluence የሻጭ ድጋፍን ስላገኙን እናመሰግናለን፤ የ {{amount}} ክፍያዎ ስላልደረሰዎት ይቅርታ እንጠይቃለን።

የገንዘብ ማውጫ ጥያቄዎን አጣርቻለሁ፦ ክፍያው ሊጠናቀቅ ያልቻለው [ምክንያቱ በቀላል ቋንቋ] ስለሆነ ነው። መጠኑ አሁን [ወደ ለማውጣት ዝግጁ ሂሳብዎ ተመልሷል / የክፍያ ቡድናችን እስኪገመግመው ተይዟል]።

ቀጣይ እርምጃ፦ [ለምሳሌ "እባክዎ ሂሳብዎ ንቁ እና በስምዎ መሆኑን ያረጋግጡ፤ አስፈላጊ ከሆነ በዳሽቦርድዎ ላይ የክፍያ ዝርዝሮችዎን አስተካክለው ያሳውቁን"]።

እባክዎ ፒንዎን፣ የይለፍ ቃልዎን ወይም የማረጋገጫ ኮድ በፍጹም አያጋሩ — አንጠይቅዎትም።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry — your {{amount}} payout failed because [reason]. The amount is [back in Available / held for review]. Next: [action]. Never share your PIN or codes. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ይቅርታ — የ {{amount}} ክፍያዎ [ምክንያት] ስለሆነ አልተሳካም። መጠኑ [ወደ ዝግጁ ሂሳብ ተመልሷል / ለግምገማ ተይዟል]። ቀጣይ፦ [እርምጃ]። ፒን ወይም ኮድ አያጋሩ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. Our payments team is still working on your failed payout of {{amount}}. We will contact you again by {{follow_up_time}}. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የክፍያ ቡድናችን ያልተሳካውን የ {{amount}} ክፍያዎን አሁንም እያስተናገደ ነው። እስከ {{follow_up_time}} ድረስ በድጋሚ እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Failure reason unknown, or amount not returned/held → **Payments & Finance**, priority High.
- Name mismatch with verified identity → **Seller Operations**.
- Repeated failures to the same provider for many sellers → **Payments & Finance** + **Technical / Engineering**.
- Destination unknown to the seller → **Trust & Safety**, priority Critical.

## Resolution Procedure
1. Confirm the payout succeeded on retry (seller confirms receipt) or the amount is back in the Available Balance.
2. Confirm corrected details (last digits) if they were the cause.
3. Record reason and outcome; close.

## Policy Pending Approval
- Define whether failed payouts return automatically to the Available Balance or are re-processed.
- Confirm whether any fee applies to failed/returned payouts (none may be quoted).
- Confirm supported payout banks and mobile-money providers.

## Internal Notes
- Replace bracketed text before sending.
- If the seller changed details right after a failure and wants an immediate retry, apply the fraud checks in *Wrong Bank/Mobile-Money Payout Details*.

<!-- doc -->
# Payouts on Hold / Restricted
id: out-payout-hold-restriction
type: article
category: payouts
subcategory: payout-restrictions
audience: seller
priority: high
department: seller_ops
features: seller-withdrawals
tags: payout on hold, withdrawals blocked, payout restricted, account under review, can't withdraw, earnings frozen, ክፍያ ታግዷል, ገንዘብ ማውጣት ተከልክሏል, መለያ በግምገማ ላይ
related: out-pending-vs-available, out-withdrawal-cancelled, out-seller-payment-dispute, pay-chargeback, out-tsg-payout-master
templates: tpl-withdrawal-status
policy_pending: yes

## Summary
A seller cannot withdraw because their payouts or account are on hold or restricted. Explain what may be shared, guide the seller to resolve any request for information, and route the review to the right team.

## Issue Description
Holds can apply to the whole seller account (e.g. Suspended status) or to payouts only, and to all earnings or only specific sales. Sellers see blocked withdrawals, frozen balances, or a notice that their account is under review. They are frustrated and often want to know exactly why and when it will end. Some holds relate to investigations that cannot be discussed in detail.

Remember: verification status (**Pending, Verified, Rejected**) and operational status (**Active, Suspended, Banned**) are separate. A seller can be Verified but Suspended.

## Possible Causes
- Identity verification not complete (status Pending) or Rejected.
- Account Suspended or Banned for policy reasons.
- Open disputes, refund requests or chargebacks on the seller's sales.
- High dispute/refund rate or complaints.
- Fraud or risk review (e.g. off-platform payment reports, payout-detail changes, unusual volumes).
- Missing or mismatched payout or business information.
- Legal or regulatory request (rare; Management).

## Information to Collect
- Seller identity (registered email or phone number)
- What exactly the seller sees (screenshot of notice/blocked button)
- When it started and any messages they received from Byfluence
- Whether they have been asked to provide information or documents

> [!WARNING] Never ask for passwords, PINs or OTPs. Do not request ID documents over insecure channels unless an approved secure process exists.

## Troubleshooting Steps
1. Verify identity.
2. Check the seller's verification status, operational status and any payout hold flag and note in the admin dashboard.
3. Identify the hold type and owner:
   - **Verification pending/rejected** → explain the seller must complete verification; see seller verification articles; **Seller Operations**.
   - **Disputes/refunds/chargebacks on specific sales** → explain that the related earnings are held while reviewed; others may still be available.
   - **Suspension/ban** → share only the reason category approved for sharing; **Seller Operations** handles appeals.
   - **Fraud/risk review** → do not disclose details; say the account needs an additional review; **Trust & Safety**.
   - **Missing information** → tell the seller exactly what to provide and through which approved process.
   - **No visible reason** → **Seller Operations**.
4. Do not lift holds or promise release dates.
5. Record what you shared and the owning department.

- [ ] Identity verified
- [ ] Statuses and hold flag checked
- [ ] Hold type and owner identified
- [ ] Seller told what they can do
- [ ] Escalated to owner

## Recommended Response (EN)
Hello {{customer_name}},

Thank you for contacting Byfluence Seller Support. I understand you cannot withdraw your earnings right now, and I'm sorry for the inconvenience.

I have checked your account. Your payouts are currently on hold because [approved reason category, e.g. "your identity verification is not yet complete" / "some sales are under review" / "your account needs an additional review"].

What you can do: [e.g. "complete your verification in your seller dashboard" / "no action is needed from you right now — our team is reviewing it"].

Your earnings remain recorded in your account while this review takes place. I can't give a specific release date, but your case has been passed to the responsible team and I will update you.

Your case number is {{ticket_id}}.

Best regards,
{{support_agent}}
Byfluence Support

## Recommended Response (AM)
ሰላም {{customer_name}}፣

የ Byfluence የሻጭ ድጋፍን ስላገኙን እናመሰግናለን። አሁን ገቢዎን ማውጣት እንደማይችሉ ተረድቻለሁ፤ ለተፈጠረው ችግር ይቅርታ እንጠይቃለን።

መለያዎን አጣርቻለሁ። ክፍያዎችዎ በአሁኑ ጊዜ የታገዱት [የተፈቀደው የምክንያት ዓይነት፣ ለምሳሌ "የማንነት ማረጋገጫዎ ገና ስላልተጠናቀቀ" / "አንዳንድ ሽያጮች በግምገማ ላይ ስለሆኑ" / "መለያዎ ተጨማሪ ግምገማ ስለሚያስፈልገው"] ነው።

ማድረግ የሚችሉት፦ [ለምሳሌ "በሻጭ ዳሽቦርድዎ ላይ ማረጋገጫዎን ያጠናቅቁ" / "አሁን ከእርስዎ የሚጠበቅ ነገር የለም — ቡድናችን እየገመገመው ነው"]።

ይህ ግምገማ እስኪጠናቀቅ ገቢዎ በመለያዎ ውስጥ ተመዝግቦ ይቆያል። የሚለቀቅበትን የተወሰነ ቀን መስጠት ባልችልም ጉዳይዎ ለሚመለከተው ቡድን ተላልፏል፤ መረጃ እሰጥዎታለሁ።

የጉዳይዎ ቁጥር {{ticket_id}} ነው።

ከሰላምታ ጋር፣
{{support_agent}}
Byfluence ድጋፍ

## Short Response (EN)
Hi {{customer_name}}, sorry for the trouble. Your payouts are on hold because [reason category]. What you can do: [action]. Your earnings stay recorded during the review; I'll update you. Case: {{ticket_id}}

## Short Response (AM)
ሰላም {{customer_name}}፣ ለችግሩ ይቅርታ። ክፍያዎችዎ የታገዱት [የምክንያት ዓይነት] ስለሆነ ነው። ማድረግ የሚችሉት፦ [እርምጃ]። በግምገማው ወቅት ገቢዎ ተመዝግቦ ይቆያል፤ መረጃ እሰጥዎታለሁ። የጉዳይ ቁጥር፦ {{ticket_id}}

## Follow-Up Response (EN)
Hello {{customer_name}}, this is an update on case {{ticket_id}}. The responsible team is still reviewing your account. We will contact you again by {{follow_up_time}}, or sooner if we need anything from you. Thank you for your patience.

## Follow-Up Response (AM)
ሰላም {{customer_name}}፣ ይህ ስለ ጉዳይ ቁጥር {{ticket_id}} የሚሰጥ መረጃ ነው። የሚመለከተው ቡድን መለያዎን አሁንም እየገመገመ ነው። እስከ {{follow_up_time}} ድረስ፣ ወይም ከእርስዎ የሚያስፈልግ ነገር ካለ ቀደም ብለን እናገኝዎታለን። ስለ ትዕግስትዎ እናመሰግናለን።

## Escalation Conditions
- Verification, suspension, ban or unexplained holds → **Seller Operations**.
- Fraud/risk holds → **Trust & Safety**.
- Holds caused by disputes/chargebacks → **Payments & Finance** (and Senior Support for dispute decisions).
- Seller appeals a ban or long hold, or threatens legal action → **Senior Support / Supervisor**; **Management** for legal/regulatory matters.

## Resolution Procedure
1. The owning team records the decision (released, continued, account action).
2. Inform the seller of the outcome in approved wording.
3. If released, confirm the seller can request a withdrawal.
4. Record the hold type, decision and date; close.

## Policy Pending Approval
- Define hold types, the reasons that may be shared with sellers, and the approved wording for each.
- Define maximum review durations and the seller appeal process.
- Define what happens to held earnings if a seller is banned (refunds to buyers, release, forfeiture) — must not be stated until approved.

## Internal Notes
- Never reveal fraud-detection details or who reported the seller.
- "Your earnings remain recorded" is true; do **not** say "your money is safe and will be paid" — outcomes depend on the review.
- Replace bracketed text before sending.
