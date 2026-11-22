# RootOut Set 17 · AU1 · "That sounds like the root." — shot plan (H1 first, then H2/H3 hook swaps)

Task ROS17. Script: `BRIEF.md` (locked, word for word). Swipe: `../../references/rosabella-skit/SWIPE.md` (watched 22 Nov:
one actress, both roles, living room, handheld, a jump cut every 2–3 s, captions mid-frame, product only in the last 25 s).
Billing: Higgsfield `WilloMd` (private workspace, Ultra, 7,426.51 credits on 22 Nov). Models: Soul (stills) · Seedance 2.5
720p `omni_reference` (video, lip-sync to the voice file) · ElevenLabs v4 (voices). 9:16, ~127 s with H1.

## How it differs from Set 1 and the swipe (unique on purpose)
- **Two people, two voices, one room**, not a single mom selfie: a pediatric exam room shot as if a phone is propped on the
  counter. Wide two-shot for the back-and-forth, quick push-ins on the "That sounds like…" answers.
- **Repeating answer device**: every "That sounds like…" lands on a hard cut to a proof insert (real footage, a real web
  screenshot, or the 3D side cut), so the rhythm reads as the swipe's but the pictures are ours.
- **Proof from the real world**: the study line uses a phone-framed screenshot of the real PubMed abstract (van Haalen 2009,
  verified 22 Nov: 1,465 children aged 4–12, family member with warts OR 1.9); the "hurts to step on" line uses the real
  Wikipedia line "They may result in pain with pressure such that walking is difficult"; "spreading at home" can add the AAD
  line "Warts can spread to another person." Plant beats use real CC footage/photos of lemon, tea tree, pokeweed, thuja.
- New cast and voices (not Emily/Maya/Nora/Sloane). Doctor never named, no credentials; end card "Dramatization. AI illustration."

## Cast (locked once, reused in every shot)
- **DOCTOR**: woman, mid-40s, white coat over a teal top, hair in a low clip, reading glasses on a cord, kind and quick; rolling
  stool. No name badge text, no stethoscope logo. Voice: ElevenLabs preset, warm/brisk (candidates: Helena, Vera, Elena).
- **MOM**: 30s, oatmeal sweater, hair up, tired but wry, phone in hand, a folded handwritten list. Voice: candidates Chloe, Hana, Quinn.
- **SON**: ~7, navy shorts, sits on the exam table; **legs and feet only**, never the face. Plantar wart on the ball of the left foot.
- **Room**: bright pediatric exam room, exam table with crinkled paper, step stool, counter with glove box and jar of tongue
  depressors, cartoon-animal wall decal (no readable text), window daylight.

## Shots (H1)
Source key: **REAL** = downloaded CC/free stock (see `BROLL.md`) · **WEB** = real page screenshot card (`WEB_SOURCES.md`) ·
**GEN** = Higgsfield Seedance (Soul start frame) · **LS** = Seedance lip-sync to the line's voice file · **3D** = Seedance 3D skin block · **CODE** = PIL/ffmpeg motion graphics (free).

| # | t (s) | line (speaker) | picture | source | billed s |
|---|---|---|---|---|---|
| 1 | 0–4 | DOCTOR "Sorry to keep you waiting. It's wart season. So, what's going on?" | doctor rolls in on the stool, shuts the door with her foot, small smile; hook text "It came back." | LS | 5 |
| 2 | 4–8 | MOM "We froze his wart twice, and it came back." | mom holds up her phone: a photo of the sole (real CC plantar-wart photo composited on the screen) | LS + REAL comp | 4 |
| 3a | 8–10 | DOCTOR "That sounds like the root." | push-in on the doctor | LS | 4 |
| 3b | 10–18.5 | …"Freezing, acid and shaving only snap off the top, like picking a dandelion. The root stays under the hard skin, so it grows back." | REAL dandelion: snap at the soil line → stub → regrown; GEN fills any missing step (whole root pulled) ; back to doctor miming a snap (from 3a) | REAL (+GEN 4) | 4 |
| 4 | 18.5–21.5 | MOM "But the skin on top is so hard. Nothing gets in." | the boy's sole on the exam paper, gloved finger taps the hard ring | LS (mom) + GEN insert | 4 + 4 |
| 5 | 21.5–29 | DOCTOR "That sounds like a hard-top problem. Lemon softens that skin, so the rest can get in." | doctor 2 s → REAL cut lemon → 3D lemon drop softens the hard top, a little door opens | LS + REAL + 3D | 4 + 5 |
| 6 | 29–32 | MOM "The cream from the store just sits on top." | mom pulls a half-used unbranded tube from her bag | LS | 4 |
| 7 | 32–44.5 | DOCTOR "That sounds like a thick cream. You need a thin oil. Tea tree sinks in, up to 8x deeper than a regular cream, and carries the rest down with it." | doctor 2 s → REAL cream blob on skin → REAL tea tree → 3D thin drop slides down with two on its back, gauge fills to "8x" (†) → 2 s paper-towel test (AI placeholder, labelled) | LS + REAL + 3D + GEN | 4 + 6 + 4 |
| 8 | 44.5–47 | MOM "And it hurts him to step on." | the boy's foot lifts off the step stool, toes curl | LS (mom off-screen over GEN) | 4 |
| 9 | 47–55.5 | DOCTOR "That sounds like it's growing inward. Pokeweed and white cedar break it down from the root, so it can't grow back." | doctor 2 s → WEB Wikipedia "pain with pressure" card 1.5 s → REAL pokeweed + thuja → 3D drops reach the root, it cracks apart | LS + WEB + REAL + 3D | 4 + 5 |
| 10 | 55.5–58 | MOM "Now his sister has one." | mom swipes to a second photo: a smaller heel with one spot (real CC heel-wart photo on the phone screen) | LS + REAL comp | 4 |
| 11 | 58–71 | DOCTOR "That sounds like it's spreading at home. A study of almost 1,500 schoolkids found someone at home with a wart makes the other kids about twice as likely to get one. So don't wait." | doctor nods, serious → WEB PubMed abstract card (scroll to "family member with warts … OR 1.9", highlighted) → REAL two pairs of kids' bare feet (no faces) → doctor "So don't wait." | LS + WEB + REAL | 6 |
| 12 | 71–73.5 | MOM "He screams if anyone touches it." | mom, deadpan-tired | LS | 4 |
| 13 | 73.5–83.5 | DOCTOR "That sounds like he's been hurt before. So, nothing that stings. No acid, no freezing. A kids' formula, ages 4 and up. Just a little cool tingle." | boy's foot jerks back as her hand comes near; she pulls back, smiles; CODE ✕ acid ✕ freeze chips | LS (wide) | 8 |
| 14 | 83.5–90 | MOM "So I need lemon, tea tree, pokeweed, white cedar… four different bottles? That's going to get expensive." | mom counts on her fingers, deadpan; REAL plant cutaways flash on each name (0.4 s each) | LS + REAL | 6 |
| 15 | 90–94.5 | DOCTOR "You could. But RootOut has all four plants in one little oil." | doctor takes the **real RootOut bottle** (bottle ref, label readable) from the counter and hands it over | LS + bottle ref | 5 |
| 16 | 94.5–106 | DOCTOR "At bedtime, two light rubs with the little file, just on the hard top. Brush the oil on. A clear dot on top, so it soaks all night. Two minutes." | doctor shows it on the boy's foot: file ×2 · cap brush paints the oil · clear dot pressed on (3 inserts) + 3D dot seals, clock 9 pm → 5 am | GEN ×3 + 3D | 12 + 4 |
| 17 | 106–113.5 | DOCTOR "Most spots are gone in about two weeks. Then keep going fourteen more nights, so the root is gone too." | doctor writes "2 weeks + 14 nights" on a sticky note, presses it onto the bottle (note text added in CODE so it's legible) | LS + bottle ref | 6 |
| 18 | 113.5–124 | DOCTOR "I'd grab a couple, one for each kid. Buy two, and the third one's free. And you've got 90 days to ask for your money back." | doctor to mom; mom holds up two fingers, then three; doctor laughs and rolls back toward the door; CODE offer card (3 bottles, 90-day seal) | LS + CODE | 8 |
| 19 | 124–127 | — | end card: bottle + snapped-vs-whole dandelion icon · "Not the top. The root." · Buy 2, get 1 free · 90-day money-back · Dramatization. AI illustration. · † footnote | CODE | 0 |
| H2 | 0–7.5 | MOM "I'd get it down till the black dots were gone…" DOCTOR "That sounds like the root." | close on mom, foot beside her | LS ×2 | 8 |
| H3 | 0–4 | MOM "His wart is back. Again." DOCTOR "Then let's talk about the root." | mom points, doctor leans in | LS ×2 | 6 |

Captions: the brief says "On screen = hook + end card only", but the client's Set 1 notes asked for **captions throughout**;
default is captions throughout (Set 1 style), kept off the screenshots, the bottle and disclaimers. Footnote † "Based on our
manufacturer's absorption testing against a regular cream." rides under shot 7.

## Cost (WilloMd, quoted 22 Nov; Seedance 2.5 720p = 7 credits/s)
| item | seconds | credits |
|---|---|---|
| Lip-sync talking clips (doctor + mom), shots 1–18 | 88 | 616 |
| Generated b-roll (sole tap, foot lift, routine ×3, dandelion fill, paper towels) | 32 | 224 |
| 3D skin side cut (lemon door, tea-tree carry + 8x, root breaks, dot + clock) | 20 | 140 |
| Soul start frames (~25) + bottle cutout | | ~12 |
| ElevenLabs voices, H1 body (299 words, two voices) | | ~8 |
| **H1 first pass** | | **~1,000** |
| Re-roll budget (about 1 in 4 shots) | | +250 |
| **H1 ceiling** | | **~1,250 of 7,426** |
| H2 + H3 hook swaps (later) | 14 | ~100 |
Free: real b-roll, web screenshot cards, offer/end cards, captions, music (CC), finish.
