# Set 18 reference: PestLab #009, analysed shot by shot (23 Nov)

Source: the swipe link in the brief (`pestlab-co-benchmark-20261104 / …890882434018739`), video re-downloaded from the
swipe site (sha256 421d5571… matches the library). 191.7 s, 360x640, voice + room tone.
Method: ffmpeg scene cuts (threshold 0.30) → **66 shots**; ElevenLabs speech-to-text with word times → words per shot;
one mid-shot frame per shot, all looked at (`references/pestlab-009/frames/sheet0-2.png`, `shots.json`, not committed).

## The numbers
| | PestLab #009 | our Set 18 script |
|---|---|---|
| length | 191.7 s | 194.5 s (clock in brief) |
| spoken words | 588 | 478 (H1) |
| pace | **3.07 w/s**, no pause over 0.6 s | brief clocks it at 2.5 w/s |
| shots | 66 (avg 2.9 s) | target ~70–80 |
| presenter on screen | 96.6 s = **50 %**, 21 returns, avg 4.6 s | |
| b-roll | 95.1 s, 45 shots, **median 2.0 s** | inserts "1–2 s each" (brief) |
| product first on screen | 75.9 s (in hand), named at 88.0 s | bottle soft in background at 9.5 s, named at ~106 s |

## Structure, time-matched to our rows
| swipe beat | swipe time | swipe length | our row(s) | our time | our length |
|---|---|---|---|---|---|
| Hook: the one you see → hidden colony | 0–9.5 | 9.5 s | 1 Hook | 0–9.5 | 9.5 s |
| Promise "how to actually get rid of them… every single one" | 9.5–17.2 | 7.7 s | 2 Promise | 9.5–14.5 | 5 s |
| "Isn't alone" + colony + 60 babies + droppings | 17.2–33 | 16 s | 3 One you see · 4 It grows · 5 Second one, daughter · 6 Real numbers | 14.5–66.5 | **52 s** |
| "Let me save you some time and money" | ~33.5 | 2 s | 7 The turn | 66.5–72 | 5.5 s |
| 5 fixes, one comic failure each (traps, poison, steel wool, cheap plug-ins, exterminator → "subscription") | 34–75.9 | **42 s** | 8 Freezing · 9 Acid · 10 Duct tape | 72–91 | 19 s |
| "Only thing that works… every wall cavity" + "That's what PestLab does" | 75.9–89.6 | 13.7 s | 11 Dandelion · 12 What reaches it | 91–115 | 24 s |
| 3 technologies, each with its job + "all three at once" + lasts 4–5 years | 89.6–153.9 | **64 s** | 13 Each plant, one job | 115–137.5 | 22.5 s |
| Placement list (kitchen, fridge, pantry, basement, garage) | 153.9–159.4 | 5.5 s | 15 Routine (file · brush · dot) | 148–159 | 11 s |
| Results triple "48 h later, no more…" | 159.4–167.7 | 8.3 s | 16 Result · 17 Life after | 162–176.5 | 14.5 s |
| Safety "no poison, no chemicals… safe around kids and pets" | 163.5–173.9 | 10 s | 14 Safe for kids | 137.5–148 | 10.5 s |
| Social proof collage "140,000 homeowners" | 173.9–178 | 4 s | (none: testimonial line row 15b) | | |
| Offer + guarantee "Not 30 days. 90 days… every penny back" | 178–190 | 12 s | 18 Close | 176.5–188 | 11.5 s |
| "Tap below before they sell out" | 190–191.7 | 1.7 s | 19 Button (Cheerio callback) | 188–191.5 | 3.5 s |
Read: ours is a **story first** (52 s of family spread before any fix), the swipe is a **lecture first** (16 s of
problem, then 42 s of fixes and 64 s of mechanism). The script is locked, so the edit has to keep the story half
moving with the swipe's cutting speed: an insert every ~2 s, a return to the dad every 4–5 s.

## The visual grammar (what to take)
1. **One home base.** Presenter locked off, waist-up behind a granite kitchen counter, window behind, hands on the
   counter; identical framing all 21 times. Every b-roll burst returns to it. → Our dad's night kitchen is the home base;
   keep one framing and one light for every return. (Brief says phone at arm's length: keep the selfie, but lock the
   distance and angle so it reads as one place.)
2. **Hook frame shows the problem in shot** (a live mouse on the counter in front of him) + two red label boxes top-centre
   ("HOW TO FORCE MICE OUT IN 48 HOURS", "LICENSED PEST CONTROL EXPERT"). → Our on-screen hook text in the same
   top-centre box style; the Cheerio bowl in frame from shot 1 (no credential label: brief forbids it).
3. **Each fix = name cut + failure insert + back for the punchline.** "Poison." is a 0.7 s shot of a bait box; "Steel
   wool." 0.8 s; "Exterminator." 0.7 s of a fogging suit; then the failure; then him. → Freezing / Acid / Duct tape each
   open on a 0.7–1 s hard cut of the object on the counter, then the failure insert, then the dad's deadpan line.
4. **Real screenshot as proof, marked up.** Shots 18–19: a real Amazon search for "ultrasonic pest repeller", red X drawn
   over the listings. → Our real AAD and PubMed screenshots, phone-framed, sentence highlighted; same quick in-out (2–3 s).
   (Not drugstore listings: they'd show competitor brands.)
5. **Lists cut on every item, ~1 s each:** "your walls / your insulation / your attic / your crawl space"; "kitchen /
   behind the fridge / pantry / basement / garage". → Our lists: "No acid, no freezing, no blister"; "two light rubs /
   brush / clear dot"; "His were gone. Hers too."
6. **Mechanism = glowing animation, held longer** (rings round the device, x-ray mouse, blue waves through walls,
   3–7 s each). → Our navy/ice skin side cut, one beat per plant, the only shots allowed to run 4–6 s.
7. **Comic inserts land the jokes.** A woman dangling a dead mouse on "pretend you won"; a $1,200 exterminator in
   hazmat. → Ours: the Cheerio ruler (row 4), milkshake in the back seat (row 8), sticky sock (row 10), the dad eating
   the Cheerio (row 19).
8. **Product in a real hand, close to the lens**, several times (75.9, 88, 137, 178 s), always white on clean light.
   → RootOut bottle held to the lens, label readable, at rows 2 (background), 12, 14, 18.
9. **Results triple over life b-roll:** "no more scratching at 3 AM" over a person in bed; "safe around your kids and
   pets" over a toddler and a dog on a couch. → Row 17 sprinkler, row 16 bath mat.
10. **Captions on every line:** white rounded box, bold black sentence case, 1–2 lines, centre-lower third, changing
    every 3–6 words. The brief says "No captions" for Set 18, but Set 1's client note asked for captions throughout.
    **Decision needed.**
11. **Sound:** dry close voice, room tone; no strong music bed audible under the voice. Energy comes from the cutting.

## What not to copy
Profanity ("this little f***er" ×9: it's the swipe's rhythm device; ours is the deadpan "One." / "The wart was winning."),
the "licensed expert" badge, the "140,000 homeowners" collage, the cash fan, "before they sell out", unbranded CGI
claims. No competitor listings on screen.

## Consequences for our shot map
- ~75 shots: dad home-base returns every 4–5 s (about half the screen time), inserts ~2 s, side-cut animation 4–6 s.
- Rows 3–6 (52 s of story) get the densest inserts: heel, doctor wave-off + AAD card, Cheerio weeks 1/3/6, second
  bump, daughter's finger, PubMed card ×2, split circle, hallway.
- Rows 8–10: name cut → failure → punchline, swipe rhythm exactly.
- Hook text box style and position taken from the swipe; end card ours.
- Open: captions on or off? Keep the selfie, or lock the phone on the counter like the swipe (steadier, more "expert")?
