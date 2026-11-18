<!-- module -->
# Registration and Account Issues
id: trn-04
number: 4
duration: 60

## Learning Objectives
- Diagnose "verification code not received" and registration errors without asking for or handling the code.
- Guide customers through login problems in a safe, logical order and recognise when it becomes an escalation.
- Explain the difference between a locked, suspended and banned account and route each correctly.
- Handle requests to change email or phone, or to delete an account, with identity verification and without exposing data.
- Recognise account compromise and suspicious registrations and escalate them to Trust & Safety with the right priority.
- Explain to any customer, in Amharic and English, why Byfluence will never ask for their OTP, password or PIN.

## Lesson

### What is confirmed — and what is not
Buyer accounts and registration are in the MVP scope. However, **the exact registration fields and verification methods depend on the implemented authentication system and are not confirmed** — including whether Byfluence uses email verification, phone OTP, or both. On the Feature Status page, "Email notifications" and "SMS notifications / OTP" are listed as unconfirmed.

So in this module you learn a **method**, not a script tied to one login screen. Before you explain any step to a customer, check the relevant Knowledge Base article (Account Registration, Login & Account Access) and the Feature Status page. If the customer describes something the article does not mention, believe them, record exactly what they see (a screenshot of the error screen is useful) and escalate to Technical.

### The golden rule: never ask for the code
> [!WARNING] **Never ask for, accept, or "check" a customer's OTP, verification code, password or PIN** — not by Telegram, not by phone, not "just to test it." If a customer sends one anyway, tell them not to share it again, do not use it, and advise them to request a new code or change their password. Record in internal notes that a code was shared (do not paste the code).

Why this rule is absolute:
- Anyone with the code can take over the account. Support agents do not need it for anything.
- Scammers impersonate Byfluence staff and ask for codes. If real agents never ask, customers can recognise the scam: "Byfluence never asks for your code."
- If an agent ever handles a code, the customer can no longer be sure who accessed their account.

Teach the customer the rule every time it is relevant:
- EN: "Please never share your password, PIN or any verification code with anyone — Byfluence staff will never ask for it."
- AM: "እባክዎ የይለፍ ቃልዎን፣ ፒንዎን ወይም ማንኛውንም የማረጋገጫ ኮድ ለማንም አያጋሩ — የByfluence ሰራተኞች በፍጹም አይጠይቁዎትም።"

### Verification code not received
Work through causes from most to least likely. Ask one or two questions at a time.

| Check | Question to the customer | If yes… |
|---|---|---|
| Wrong address or number | "Which email or phone number did you enter when registering?" | Typo (e.g., gmial.com, missing digit) → register again / correct it if the flow allows |
| Spam / promotions folder | "Could you check your Spam or Promotions folder?" | Found → resolved |
| Delay | "When did you request it?" | Very recent → ask them to wait a little before requesting again |
| Many requests | "Did you press 'resend' several times?" | Only the latest code may work; use the newest message |
| Network / SIM | "Do you receive other SMS on this number right now?" | Phone/network issue on customer side |
| Code expired or rejected | "What message appears when you enter it?" | Request a new code; if it keeps failing → Technical |
| Many customers reporting | (Check Dashboard and Announcements) | Possible incident → alert supervisor, link tickets |

If none of these explain it, create a ticket (Account Registration → Email, Phone & OTP Verification), record the email/phone domain, time of request, device and browser, and escalate to **Technical**.

> [!NOTE] Do not tell customers how long a code is valid or how many times they can resend unless the article states it. These limits are not confirmed.

### Login problems
Follow this order:
1. **Which account?** Confirm the email or phone they are using. Many customers registered with a different email than the one they are typing.
2. **What exactly happens?** Ask for the exact error message or a screenshot of the screen (not of any code).
3. **Password forgotten?** Guide them to the self-service password reset, if the article confirms one exists. You never set or see passwords.
4. **Device and browser.** Try another browser, clear cache, update the app/browser, check that the date/time on the phone is correct.
5. **Account status.** If you have authorized access, check whether the account is locked, suspended or banned.
6. **Still failing?** Ticket → Login & Account Access → Login Errors → escalate to Technical with all details.

### Locked, suspended and banned
These words sound similar to customers but mean different things and go to different teams.

| Status | Usually means | Your action | Department |
|---|---|---|---|
| **Locked** | Temporary security lock, often after repeated failed logins | Guide through the unlock/reset flow if one exists; otherwise escalate | Technical (or Trust & Safety if suspicious) |
| **Suspended** | Restricted by Byfluence pending review or for a rule violation | Do not speculate about reasons; do not promise reactivation | Trust & Safety or Seller Operations (sellers) |
| **Banned** | Permanently removed | Explain neutrally; appeals process is Policy Pending Approval | Senior Support / Supervisor |

> [!WARNING] Never reveal fraud-detection details ("we noticed three cards from different countries"). Say: "Your account is under review by the responsible team."

### Changing email, phone, or deleting an account
These requests are high-risk because they are exactly what an attacker would ask for.
- **Verify identity first**: the request must come from the registered email/phone, and the person should be able to describe their own account activity (e.g., recent bookings). Never use a code for this.
- If the customer has **lost access** to the registered email or phone, do not change anything yourself — escalate to Trust & Safety.
- **Deletion requests**: record the request and escalate to Senior Support / Supervisor. The process, what data is kept and any waiting period are Policy Pending Approval. Sellers with pending earnings or open disputes need special handling — note this in the ticket.

### Account compromise
Signs: "I didn't make this booking", "my email was changed", "someone withdrew my earnings", unknown logins.
1. Treat as **Critical** if money is moving or a seller's payout details may have changed; otherwise **High**.
2. Advise the customer to change their password (and email password) immediately using the official reset flow.
3. Create a ticket (Login & Account Access → Recovery & Unauthorized Access) and escalate to **Trust & Safety** right away; involve Payments & Finance if transactions are affected.
4. Do not reverse transactions or promise reimbursement.

### Duplicate and suspicious registrations
Customers sometimes create two accounts by accident (two emails). Explain that bookings stay on the account that made them, and escalate any request to merge accounts — merging is not a confirmed capability. Many accounts from one person, fake names or registrations linked to fraud reports go to **Trust & Safety**.

### Account issues that are really something else
A "login problem" two hours before a consultation is also a consultation problem. A "suspended account" for a seller is also an earnings problem. Record all references (consultation ID, transaction reference) in the ticket and set the priority by the **most urgent impact**.

## Realistic Examples

### Example 1: Code not received (Amharic)
**Customer (Telegram):**
> ሰላም፣ ለመመዝገብ ሞክሬ ኮድ ይላካል አለ ግን ምንም አልደረሰኝም። ሶስት ጊዜ ልኬዋለሁ።

*(Hello, I tried to register; it said a code would be sent but nothing arrived. I sent it three times.)*

**Agent action:** Searches "ኮድ አልደረሰኝም", opens the verification article. Asks which email/phone they used and whether they checked Spam. Reminds them only the newest code may work. Does not ask for the code.

**Model reply (AM):**
> ሰላም፣ ስላገኙን እናመሰግናለን። እባክዎ ሲመዘገቡ ያስገቡትን ኢሜል ወይም ስልክ ቁጥር ያረጋግጡልኝ፤ ኢሜል ከሆነ የ"Spam" ማህደሩንም ይመልከቱ። ብዙ ጊዜ ከላኩ የመጨረሻውን ኮድ ብቻ ይጠቀሙ። ኮዱን ለኔም ሆነ ለማንም አያጋሩ — አንጠይቅዎትም። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

### Example 2: Customer sends their OTP
**Customer (Telegram, English):**
> Here is the code I got: 4 8 2 9 1 7. Please log me in.

**Agent action:** Does not use or repeat the code. Replies immediately, advises a new code and a password change, and adds an internal note: "Customer shared a code in chat; advised not to share; code not used."

**Model reply (EN):**
> Thank you, but please don't share codes with anyone, including us — we will never ask for them and can't use them to log you in. Please request a new code and, to be safe, change your password using "Forgot password". Then tell me what happens when you try to log in. Case: {{ticket_id}}

### Example 3: Email change request from an unregistered address
**Customer (email from a new address):**
> I lost my old Gmail. Change my Byfluence email to this one. I'm a seller and have earnings there.

**Agent reasoning:** The request does not come from the registered email, and the account holds earnings — a classic takeover pattern even if the person is genuine. The agent changes nothing, opens a ticket (Account Changes), sets priority High, escalates to **Trust & Safety** and replies that the identity check is handled by a specialised team.

### Example 4: Suspended buyer demands the reason
**Customer (phone, Amharic):** "መለያዬ ለምን ታገደ? አሁኑኑ ንገሩኝ!" *(Why was my account suspended? Tell me now!)*

**Agent action:** Stays calm, does not guess or reveal internal reasons, explains the account is under review by the responsible team, creates the ticket and escalates. Logs the call.

## Practical Exercises
1. **Article mapping.** Open the Account Registration and Login & Account Access categories. List the articles for: code not received, password reset, locked account, suspended account, email change, unauthorized access. Note each one's default priority and department.
2. **Never-ask drill.** Find the template for reminding a customer not to share codes. Fill it in Amharic and English. Then write your own one-sentence version for a phone call.
3. **Ticket build.** Create a practice ticket for Example 3 (email change from unregistered address): customer info, category/subcategory, priority, internal note explaining the risk, escalation to Trust & Safety with a clear escalation note.
4. **Diagnosis role-play.** With a partner playing the customer, run the "code not received" table from top to bottom in Amharic. Your partner secretly picks the cause. Can you find it in five questions or fewer?
5. **Feature Status check.** Open Feature Status and record the current status of Email notifications and SMS notifications / OTP. Write how the answer changes what you tell a customer about where their code should arrive.

## Knowledge Check
Q: A customer offers to send you the OTP they received so you can "fix it faster." What do you do?
- [x] Refuse, explain Byfluence never asks for codes, and advise them to request a new one if needed
- [ ] Accept it, since the customer offered
- [ ] Accept it only on a phone call
- [ ] Ask a supervisor to accept it instead
> No agent ever handles OTPs, passwords or PINs, under any circumstances.

Q: A customer says the verification code never arrived. Which is the best first question?
- [x] "Which email or phone number did you register with?"
- [ ] "What is your password?"
- [ ] "Have you tried another country's SIM?"
> Wrong or mistyped contact details are among the most common causes.

Q: Which department should handle a suspected account takeover where a seller's earnings may be at risk?
- [ ] Technical only
- [ ] Customer Support Level 1 closes it after a password reset
- [x] Trust & Safety, with Payments & Finance involved if transactions are affected, priority Critical
> Account compromise is a Trust & Safety case; money at risk makes it Critical.

Q: A customer asks you to change their email, writing from an address that is not registered. What do you do?
- [ ] Change it because they know the account name
- [x] Make no change, create a ticket and escalate to Trust & Safety for identity verification
- [ ] Ask them to send the OTP to prove ownership
> Requests from unregistered contacts are a takeover risk. Never verify with a code.

Q: What is the difference between a locked and a suspended account?
- [x] Locked is usually a temporary security lock; suspended is a restriction by Byfluence pending review or for a rule violation
- [ ] There is none
- [ ] Suspended is temporary; locked is permanent
> Locked usually follows failed logins; suspension is a decision by Byfluence. Banned is permanent.

Q: A suspended customer demands the exact reason. What do you say?
- [ ] Share the fraud signals from the admin dashboard
- [ ] Tell them it was probably a mistake and will be lifted
- [x] Explain neutrally that the account is under review by the responsible team, without revealing internal details, and escalate
> Never disclose detection details and never promise reactivation.

Q: A customer asks how long a verification code stays valid. No article states it. What do you do?
- [ ] Say a typical time used by other platforms
- [x] Do not state a time; ask them to use the newest code and request a new one if it fails
- [ ] Say codes never expire
> Code validity and resend limits are not confirmed.

Q: A customer wants to merge two accounts they created by mistake. What is correct?
- [x] Explain that bookings stay on the account that made them and escalate the merge request, since merging is not a confirmed capability
- [ ] Merge them in the admin dashboard
- [ ] Delete one account immediately
> Do not claim to perform actions that are not confirmed capabilities.
