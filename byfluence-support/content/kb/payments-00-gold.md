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
