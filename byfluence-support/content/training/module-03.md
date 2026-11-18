<!-- module -->
# Communication Standards
id: trn-03
number: 3
duration: 60

## Learning Objectives
- Write responses that are professional, respectful, clear, concise and consistent — the Byfluence support voice.
- Default to Amharic, switch to English correctly, and write natural, respectful Amharic using the እርስዎ form.
- Adapt the same message to Telegram, email and phone, and record every contact in the ticket communication log.
- Show genuine empathy with specific, non-scripted acknowledgement phrases in both languages.
- Replace promises (dates, outcomes, amounts) with approved neutral wording.
- Protect customer privacy and security: never request passwords, OTPs or PINs, and never disclose another user's information.
- Use Response Templates correctly: right language, all placeholders filled, nothing promised that the template does not promise.

## Lesson

### The Byfluence support voice
Byfluence's standard is **professional, respectful, clear, concise and consistent**. In practice:

| Quality | Looks like | Does not look like |
|---|---|---|
| Professional | Full sentences, correct names, signed with your name | Slang, emojis in serious cases, "bro", all caps |
| Respectful | እርስዎ form, "please", "thank you", no blame | "You did it wrong", "As I already told you" |
| Clear | One topic per paragraph, numbered steps | Long blocks, internal jargon ("callback failed", "L3") |
| Concise | Only the questions you need answered | Asking for ten things "just in case" |
| Consistent | Same facts as the Knowledge Base and other agents | Your personal opinion of a policy |

### Amharic first
Amharic is the default language. English is used when the customer writes in English or asks for it. Some customers write Amharic in Latin letters ("selam, kifiya kefelku gin…"); reply in Amharic script unless they say they cannot read it, in which case use English or simple transliterated Amharic.

Rules for Amharic messages:
- Use the respectful form: **እርስዎ, እባክዎ, ይቅርታ እንጠይቃለን, እናመሰግናለን**.
- Keep placeholders, IDs, brand names and technical references in Latin script: `{{ticket_id}}`, Byfluence, Google Meet, Chapa, Telebirr, transaction references.
- Write naturally. Machine-translated Amharic sounds cold and is sometimes wrong. Prefer the Amharic versions in Knowledge Base articles and templates — they were written for customers.
- When a technical word has no common Amharic equivalent, add the English in brackets once: "የግብይት መለያ ቁጥር (transaction reference)".

> [!TIP] If you are not confident in your Amharic for a sensitive message (refund decision, suspension, fraud), copy the approved Amharic template and only fill placeholders. Ask a colleague to review before sending.

### Channels
The intended channels are the website, Telegram, email, telephone and, in future, an AI assistant. Check the Feature Status page for which channels are confirmed and the Policies section for any official contact details — **never invent a phone number, email address, Telegram handle or office hours**; use `{{support_channel}}` in templates.

| Channel | Style | Watch out for |
|---|---|---|
| Telegram | Short messages, one question at a time; use the **Short Response** versions | Long walls of text on a phone screen; sending sensitive data in chat |
| Email | Full **Recommended Response**, greeting and signature, case number in the subject or first line | Missing case number; replying to the wrong thread |
| Phone | Spoken, slower, confirm understanding; read back key references | Promising things verbally you would never write; not logging the call |
| Website support | As email or chat depending on the form | Customer may not see replies quickly — make each message complete |

> [!WARNING] The support app does **not** send messages for you. You copy the response, send it in the real channel, then record it in the ticket's **communication log** (channel, direction, summary). If it is not logged, the next agent does not know it happened.

### The structure of a good response
1. **Greeting** with the customer's name — "Hello {{customer_name}}," / "ሰላም {{customer_name}}፣"
2. **Acknowledge** the problem in one sentence, in your own words.
3. **Explain** what you have checked or what happens next.
4. **Ask** only for the information you actually need (numbered).
5. **Security reminder** when payment or login is involved.
6. **Case number** — `{{ticket_id}}` in every full response.
7. **Next step** — when you will update them, using approved wording or `{{follow_up_time}}` only when you can keep it.
8. **Sign-off** — "{{support_agent}}, Byfluence Support" / "{{support_agent}}፣ Byfluence ድጋፍ".

### Empathy that sounds real
Empathy is naming the customer's situation accurately, not repeating "sorry for the inconvenience" in every line.

| Situation | English | Amharic |
|---|---|---|
| Money worry | "I understand it's worrying to see money leave your account without a confirmation." | "ገንዘብዎ ተቆርጦ ማረጋገጫ አለማግኘትዎ እንደሚያሳስብ ይገባኛል።" |
| Missed session | "I'm sorry you waited and the session didn't happen." | "ጠብቀው ምክክሩ ባለመካሄዱ በጣም ይቅርታ እንጠይቃለን።" |
| Seller income | "I know your earnings matter to your business, so I've prioritised this." | "ገቢዎ ለስራዎ ምን ያህል አስፈላጊ እንደሆነ እረዳለሁ፤ ለዚህም ቅድሚያ ሰጥቼዋለሁ።" |
| Repeat contact | "Thank you for your patience — I can see you've contacted us before about this." | "ስለ ትዕግስትዎ እናመሰግናለን፤ ቀደም ብለው ስለዚህ ጉዳይ እንዳገኙን አይቻለሁ።" |

### Never promise
Many Byfluence rules are **Policy Pending Approval**. Even when a rule exists, outcomes are decided by authorized teams, not by you.

| Don't say | Say instead |
|---|---|
| "You'll get your refund in 3 days." | "Your request has been passed to the team responsible. I'll update you as soon as there is a decision." |
| "Don't worry, you'll definitely get your money back." | "I've recorded everything needed for the review under case {{ticket_id}}." |
| "The seller will be banned." | "Thank you for reporting this. Our team will review it." |
| "Your withdrawal will arrive tomorrow." | "Your withdrawal request is being processed. I'll let you know if anything is needed from you." |
| "I'll fix it right now." (when you can't) | "I've escalated this to our technical team." |

Use `{{estimated_resolution_time}}` only with **approved wording** supplied by your supervisor or the article. If none exists, leave it out.

### Privacy and security
- **Never ask** for passwords, OTP or verification codes, PINs, mobile-money PINs, full card numbers or CVV. Say so in payment and login messages: "Please do not share your password, PIN or any code — we will never ask for them."
- Verify identity using the **registered email or phone** and details only the account owner would know about their own activity (e.g., the booking they made) — never with a secret code.
- **Never disclose** another user's personal information: a seller's personal phone number, a buyer's email, another customer's transaction. Communication between buyer and seller goes through the proper process.
- Do not confirm whether an account exists to someone who is not verified as its owner.
- Do not ask customers to send ID documents through Telegram or email unless an approved process tells you to.

### Using Response Templates well
1. Search Response Templates by situation ("transaction reference", "no-show", "escalated").
2. Choose the language (Amharic default) and channel version.
3. Fill **every** placeholder — a message that says "Hello {{customer_name}}" is a public mistake.
4. Read it once before copying: does it match this customer's facts? Does it promise anything?
5. Send in the channel, then log it in the ticket.

## Realistic Examples

### Example 1: Rewriting a risky reply
**Customer (Telegram, Amharic):**
> ለምክክር ከፍያለሁ ግን ምንም መልዕክት አልደረሰኝም። ገንዘቤ ጠፍቷል?

*(I paid for a consultation but received no message. Has my money disappeared?)*

**A trainee's draft:** "Don't worry, your money is safe, it will be confirmed in 1 hour."

**Problems:** Promises an outcome ("safe") and a time ("1 hour") that nobody confirmed.

**Better reply (AM):**
> ሰላም፣ ገንዘብዎ ተቆርጦ ማረጋገጫ አለማግኘትዎ እንደሚያሳስብ ይገባኛል። ለማጣራት እባክዎ ከክፍያ ደረሰኝዎ ወይም ኤስኤምኤስዎ ላይ ያለውን የግብይት ቁጥር ይላኩልኝ። የይለፍ ቃል፣ ፒን ወይም ኮድ በፍጹም አያጋሩ። የጉዳይዎ ቁጥር {{ticket_id}} ነው።

### Example 2: Switching language
**Customer (email):**
> Selam. Please answer me in English, my Amharic reading is not good. My booking link is missing.

**Agent action:** Replies fully in English, notes "Preferred language: English" in the ticket so the next agent does not switch back to Amharic.

### Example 3: Privacy request from a buyer
**Customer (Telegram, English):**
> The consultant isn't answering on the platform. Just give me her phone number and I'll call her.

**Model reply (EN):**
> I understand you want to reach her quickly. For privacy reasons we can't share a seller's personal contact details, but I've opened case {{ticket_id}} and our team is contacting the consultant through Byfluence now. I'll update you here as soon as I hear back.

### Example 4: Phone call to written record
A seller calls about a withdrawal. After the call the agent adds a communication-log entry: *"Phone, inbound. Seller asked about Withdrawal Pending since last week. Explained processing; no date promised. Agreed to update by Telegram after Payments responds."* and sets a follow-up.

## Practical Exercises
1. **Template drill.** Open Response Templates and find a payment information-request template. Fill every placeholder for a fictional customer, select Amharic, copy it into a practice ticket's communication log as if sent by Telegram. Then do the same in English for email.
2. **Promise hunt.** Your trainer gives you five draft replies. Highlight every promise (date, amount, outcome) and rewrite each line using the "Say instead" table.
3. **Empathy in Amharic.** Write an acknowledgement sentence in Amharic for: a seller whose listing was rejected; a buyer whose session started late; a customer contacting you for the third time. Compare with the Customer Communication guides.
4. **Channel adaptation.** Take one Knowledge Base article's Recommended Response and turn it into (a) the Telegram short version and (b) a phone script of what you would say. Check against the article's Short Response.
5. **Privacy scenarios.** Search the Policies section for privacy rules. For each of three trainer-provided requests (e.g., "tell me if my wife has an account"), write the reply and the ticket note.

## Knowledge Check
Q: A customer writes to you in English. Which language should you reply in?
- [x] English, and note the preference in the ticket
- [ ] Amharic, because it is the default
- [ ] Both languages in every message
> Amharic is the default, but you switch to English when the customer writes in or requests English.

Q: Which item must appear in every full customer response?
- [ ] The seller's contact number
- [x] The case number {{ticket_id}}
- [ ] An exact resolution date
- [ ] The department's internal name
> The case number lets the customer and any agent find the case. Dates are not promised unless approved.

Q: You sent a reply on Telegram. What must you do in the support app?
- [ ] Nothing — the app sends and logs messages automatically
- [x] Record the contact in the ticket's communication log
- [ ] Close the ticket
> The app never sends messages automatically. Agents record contacts manually.

Q: Which sentence is acceptable to send?
- [ ] "Your refund will arrive in 3 days."
- [x] "I've passed your request to the responsible team and will update you as soon as there is a decision."
- [ ] "The seller will definitely be suspended."
- [ ] "I promise this will be fixed today."
> Never promise outcomes or timelines that are not approved.

Q: How should you verify that you are talking to the account owner?
- [ ] Ask them to read out the OTP code they just received
- [ ] Ask for their password so you can check
- [x] Match their registered email or phone and details of their own activity, without asking for any secret code
> Never ask for passwords, OTPs or PINs. Verify using non-secret registered details.

Q: In Amharic responses, how should placeholders and brand names be written?
- [ ] Translated into Amharic script
- [x] Kept in Latin script exactly as they are (e.g., {{ticket_id}}, Byfluence, Google Meet)
- [ ] Removed
> Placeholders, IDs and brand names stay unchanged in Latin script.

Q: A buyer asks for a seller's personal phone number. What do you do?
- [x] Decline politely for privacy reasons and contact the seller through the proper process
- [ ] Share it, because the buyer paid
- [ ] Tell the buyer to search for it online
> Never disclose another user's personal information.

Q: Which Amharic form is required in customer messages?
- [ ] The informal አንተ/አንቺ form
- [ ] Whichever matches the customer's tone
- [x] The respectful እርስዎ form
> Byfluence uses the respectful form with all customers.
