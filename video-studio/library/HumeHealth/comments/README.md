# Hume Health: client comments gallery

Every review round we get (client notes, the producer's own notes, rules given mid-project) is logged here, one file
per project. **The point is to learn from them:** each note records what was wrong, what we changed, and the lesson,
so the same mistake never reaches a client twice.

## When to read it
1. **Before planning any new Hume ad:** read the *Lessons checklist* below, then skim the file of the most similar past
   project (same product, same creator or same format).
2. **Before every delivery:** run the checklist against the cut, in every hook version and every size.
3. **When a new round of comments arrives:** log it in the project's file **before changing anything** (template at
   the bottom), then fix, then fill in "What we did" and "Lesson". If the lesson applies to every future ad, add it to
   the checklist below and, if the client or producer made it a rule, to `../EDITING_RULES.md` too.

## Projects
| Project folder | Ad | Rounds logged | Latest version |
|---|---|---|---|
| [`hume-band-xmas`](hume-band-xmas.md) | Band Xmas, vs all wearables, "I wear four wearables" (Lottie) | 1 | v2 |
| [`hume-pod-visceralfat-2453`](hume-pod-visceralfat-2453.md) | Pod Visceral Fat Ad2453 iteration (Kushal Neba) | 0 | v1 |
| [`hume-pod-recomp-healthiermindset`](hume-pod-recomp-healthiermindset.md) | Pod Muscle Recomp, Healthier Mindset (Cassidy Bogan) | 10 | 9:16 H1 v12, H2/H3 v10; 4:5 v3 |
| [`hume-pod-muscle-imbalance`](hume-pod-muscle-imbalance.md) | Pod Muscle Imbalance, Active But Imbalanced (Lottie / AJ Johnson) | 6 | v9 |
| [`hume-pod-dexa-2945`](hume-pod-dexa-2945.md) | Pod Tech, At-Home Scan, Personal DEXA Scanner (Rohit) | 3 | v6 |
| [`hume-band-fitbutdying`](hume-band-fitbutdying.md) | Band Longevity, Chronic Detection, Fit But Dying (Lottie) | 3 | v4 |
| [`hume-pod-xmas-vsdexa`](hume-pod-xmas-vsdexa.md) | Pod Xmas Value vs DEXA, Scan From Home (Dawna Stafford-Wilson) | 5 | v6 |
| [`hume-band-straps-ad641`](hume-band-straps-ad641.md) | Band 2.0 Straps, "Upgrade I've Waited" AD641 (Ucef) | 1 | v2 |
| [`hume-band-peri-40plus`](hume-band-peri-40plus.md) | Band Longevity 40+ Perimenopause, AI VO (Becca Silver) | 5 | v6 |

## Review pages (how clients comment)
Template: `../tools/review_page_template.html` (fixes 4–6 built in, 2026-11-21). Copy it, then change MASTER, CUTS, the
title, eyebrow and h1. Publish with
`capabilities: {comments: {composer_only: true}, db: {}, user: {scopes: ["profile"]}}` and `contract: "latest"`.
An older live page is upgraded in place with `../tools/review_fix4.py`, then `review_fix5.py`, then `review_fix6.py`. Read
the live page first (Artifact read, no `path`), run the three scripts on its HTML, and republish to the same url. Don't
build client review pages with `vs present`: the client paths below are verified only on this template.
- **Seeking:** the page loads each cut's proxy whole into the browser before playing (the artifact file host does not serve
  byte ranges, so a plain `<video src>` snapped back to 0:00 on every seek). Keep each proxy under 16 MB (540p, ~620 kb/s).
- **Who can post where** (claude.ai's rules, checked 2026-11-21):
  - **Owner, organization members, and outside clients invited by email as Editor** write the page's own shared comment
    list, which is live, with a Refresh button.
  - **Commenters** post with "Comment on this frame", which uses claude.ai's comment box. Those threads show in claude.ai's
    comment panel (the speech-bubble icon), not in the page's list.
  - **Everyone else** (signed out, or on the plain "anyone with the link" link) can only read. Their notes stay on their
    device, marked "NOT sent yet", with Email my notes / Copy my notes and a warning before they leave.
- **Before 2026-11-21 no comment ever reached us.** The page started in device-only mode and never left it (fix4). One
  failed claude.ai request also sent everyone to device-only notes (fix5).
- **Access check line:** device-only notes carry "Access check: … user=… db=… write=… error=…", which is also in Copy my notes.
  `user=false` means claude.ai doesn't link the client's account to the invite: they must sign in with the invited email
  and open the invitation link (fix6).
- **Getting comments to us:** the hourly "Hume review comments check" reads every live review page (the page's own list
  and the claude.ai threads) and sends new notes to that ad's session. Add each new review page to its list.

## Lessons checklist (from every round so far)
Each line is a mistake that a client or the producer caught at least once. The project it came from is in brackets.

**Story and footage**
- [ ] Every shot matches the words under it, word for word. Re-check every cutaway against its line before delivery. (Band Xmas, Muscle Imbalance)
- [ ] Every b-roll is unique: no clip twice, no same source at another in-point, no same footage under another name. Run `tools/broll_unique.py` on every hook and size. (Band Xmas, Pod Xmas: a name-only check missed two repeats)
- [ ] **Hooks never share shots across hook versions** (STRICT): H1, H2, H3 each open on different footage. (Fit But Dying v3: one clip was in all three hooks)
- [ ] No sub-1.2 s insert to patch a line; let the previous shot run on. A money figure gets money on screen. (Fit But Dying v3)
- [ ] Shots run 2-3 s, never longer than 3.0 s, and never shorter than 0.7 s; slivers read as glitches. (Band Xmas, Cassidy)
- [ ] Use the creator's own footage first; b-roll only where her footage can't show what she says, and then faceless b-roll. (Muscle Imbalance)
- [ ] One-person story when the brief is a personal story: build it around one character, not scattered people. (Fit But Dying)
- [ ] Right product generation in every shot: Pod 1.0 vs 2.0 as the brief says; **never Band 1.0** in a Band 2.0 ad. (Fit But Dying, Pod Xmas, Muscle Imbalance H3)
- [ ] People match the creator: a woman creator gets women in b-roll and a female app account (no male body map, no 220 lb male weight screen). (Cassidy, Pod Xmas)
- [ ] App footage is the **newest** recording set only; old app UI gets rejected. (DEXA, Pod Xmas)
- [ ] Metrics scroll in the real recording, then the red box draws on; no frozen screenshots. Every spoken metric gets its screen (Rule 1). (Cassidy, DEXA)
- [ ] The metric screen stays up until she finishes the sentence that names it. (Cassidy)
- [ ] Every app shot moves: pick a stretch of the recording where it scrolls (speed it up if needed), never a resting screen. Two shots of the same app tab count as a repeat. (Band Straps v1 → v2)
- [ ] Talking-head bodies: cut away to the creator's own b-roll right after the hook; don't leave long stretches of talking head. (Band Straps, Muscle Imbalance)
- [ ] Product fully in frame in every size, at the first and last frame of the shot; no push-in that carries it out of frame. (Cassidy 4:5, Pod Xmas)
- [ ] **Resizing (4:5, 1:1):** the Pod in the creator's A-roll is either fully in or framed fully out; Pod b-roll that is already cut by the edge in the 9:16 source is swapped, not reframed; captions are placed per shot so they never sit on the Pod or a red box; headline/CTA PNGs are re-laid for the size; on-screen names re-checked ("Hume Pod"). (Muscle Imbalance 4:5)
- [ ] **On the Pod: barefoot (no socks) and arms straight on the handles**, every frame of the shot. (DEXA v6, Pod Xmas)
- [ ] **Pod clip choice: arms stay straight while stretching and holding the handle** (straight down or straight out, never bent at chest/waist); the handle lift shows ≤ ~0.3 s. (DEXA v9)
- [ ] Product use starts at the action (stepping on, gripping the handle), and hooks show the whole use, not a cut-off moment. (DEXA, Pod Xmas)
- [ ] Never use footage from folders marked "NO USAGE" / "Do Not Use". (DEXA H2 `os33`)
- [ ] Check stock/library clips for agency cuts inside the clip; start after them. (Cassidy 4:5)
- [ ] **Real footage only**: `BAND2_InHouse/Icon` clips are AI stock and finished ads can be illustrated; neither is "real footage". Exclude both from searches. (Perimenopause v1)
- [ ] A story with a doctor, scan or hospital: ask the producer for real clinic clips up front; the library has none. (Perimenopause v1)
- [ ] App cards: no two from the same app tab (e.g. HRV and Stress on one Band vitals screen is a repeat). (Perimenopause v1)
- [ ] **No frame without a caption** in the body: each caption holds until the next one starts; never cover the product with a caption (move it up for that shot). (Perimenopause v3)

**Creator audio and sync**
- [ ] Keep the whole script; don't drop lines without asking. (Cassidy)
- [ ] Cut pauses from the **audio level**, not only the transcript; transcripts stretch words over silences. (Cassidy: lost audio at 1:00)
- [ ] Remove repeated words completely; set cut points on measured silence so no fragment ("the bo-") survives. Re-transcribe the final cut. (Cassidy: "body pod" twice)
- [ ] Her lips are always in sync: never cover her line with her footage from another moment. (Cassidy 0:58)
- [ ] Burned-in overlays in her raw (phone UI, text) are covered with b-roll, not painted out. (Cassidy)
- [ ] VO pauses tightened so the audio sounds natural, and the hook joins the body with no gap. (Fit But Dying)

**Text and graphics**
- [ ] Captions follow grammar: capitals, commas, full stops, question marks; fix mis-heard words. (Cassidy)
- [ ] Product names on screen are exactly `Hume Pod` and `Hume Band` (two words). (DEXA, Muscle Imbalance v8)
- [ ] Hook headline stays on from the first frame until the body starts, in every hook and size; accent word red; never over a face. (Cassidy, Muscle Imbalance, Pod Xmas)
- [ ] Headline, captions and CTA never cover a face or the product, and stay inside the safe zone (headline ≥ 15 % from the top, 120 px from the sides). (Cassidy, Muscle Imbalance, DEXA 1:13)
- [ ] Long captions break into two lines inside the frame; never cut off. (DEXA "45-day money-back guarantee")
- [ ] The CTA card comes in on the CTA line and stays to the last frame. (Muscle Imbalance)
- [ ] Emoji are Apple emoji. (Muscle Imbalance)
- [ ] Overlays (phone UI insets, product images) small enough not to cover the creator. (Cassidy)
- [ ] On scrolling app screens, captions can land on a number (Pod Xmas v4 at 0:29). Watch for it; offer a soft caption backing if it hurts readability.

**Sound**
- [ ] No sound effects unless the brief or client asks (Muscle Imbalance v9 Hook 2 is a client-requested exception). (Cassidy, Muscle Imbalance)
- [ ] Music fits the ad's tone; ask before changing a track the producer chose. (Fit But Dying)
- [ ] **Music plays at bed level to the last frame.** Never land a song's natural outro on the ending: outros fade over 10-15 s and the music "disappears". End with a fade of 1 s or less. (Pod Xmas v4 → v5)
- [ ] No Higgsfield or AI generation unless the producer asks for it. (Fit But Dying)

**Delivery**
- [ ] Glitch scan (no shot under 0.7 s, no flash frames), −14 LUFS, true peak ≤ −1 dBTP.
- [ ] Re-transcribe hook and ending; word match against the script.
- [ ] Frames before and after every hook/body cut (headline on, then off).
- [ ] Once the producer approves: deliver every file straight to Drive (Hume_4Kiru/<ad name>) with `../tools/drive_delivery/` and log the folder link.
- [ ] Review page is shareable as Commenter when the producer wants others to comment, and comments land in the shared store (`comments: {composer_only: true}`), not only in one browser.

## Template for a new round
```md
## Round N: YYYY-MM-DD, on vX → vY
Source: client (zip of annotated frames `name.zip`) | producer in chat | review page comments
| # | Where | Note (as given, lightly cleaned) | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | H1 0:04 | ... | ... | ... (→ checklist / EDITING_RULES if general) |
```
