# Haven & Spool ad playbook

Built 2026-11-23 from 139 Hyperscale briefs: every launched (116) and approved (21) brief, plus older winners they
cite. Haven & Spool only: nothing here comes from another brand. Per-brief data: `ads/briefs_index.json`.
Lists: `ads/CATALOGUE.md`, `ads/HOOK_BANK.md` (120 hooks). Evidence: `WINNING_ADS.md`, `DO_NOT_USE.md`.
Refresh: `vs hyperscale learn library/HavenSpool/ads/briefs --brand "Haven & Spool"` after saving new briefs.

## 1. Product and offer
- **Products** (Hyperscale Products tab; always use these photos as references): 50 ml Castor Oil Roll On (amber
  glass, rose quartz roller ball), Castor Oil Belly Pack (cotton wrap), Castor Oil Bottle (100 ml refill).
- **One ingredient**: organic, cold-pressed castor oil. The roller is the difference: no oily fingers, ten seconds,
  right on the spot.
- **Offer in current briefs**: Buy 1 Get 1 Free + 30 nights (30-night money-back guarantee). Earlier: 50% off + a
  free bottle (#181, #375; matches the site pop-up). Black Friday briefs export a BF ending and an evergreen ending.

## 2. Who buys
Women, mostly **45-65+** (briefs say "women 55+", "45+", "50-65"). They know the usual fixes (cutting, freezing kits,
nail clippers, string, the dermatologist, Botox, ten-step routines, $90 creams) and are tired of them or afraid of
pain, blood and scars.

## 3. Angles (by launched + approved briefs)
| angle | launched | approved | backed by |
|---|---|---|---|
| **Skin tags** | 21 | 15 | #316 (top spender), #156, #78, #160, #79, #189, #331, #332 |
| **Bloating** (belly pack / belly button) | 22 | 3 | #294, #303, #305, Skeleton #10 |
| Multiple / multi-use | 19 | 0 | #107, #108 |
| Anti-aging, face, eyes, dark circles | 19 | 1 | #106, #304 (#160 swapped to wrinkles), #457 |
| Lymph nodes / drainage | 7 | 1 | |
| Thyroid, cysts, armpits, liver, period cramps, acne scars, smooth neck | 1-4 each | | test angles |
Skin tags is the money angle right now; bloating is the second proven one.

## 4. Formats that work and how they're built
| format | how it's built | model ad |
|---|---|---|
| **Ranking** | A presenter rates the usual methods out loud (freezing kits, clippers...), score big on screen, ours last and highest. Fixed white title the whole video. No b-roll cut-aways; the mechanism plays in a pop-up square. | #316, #303 |
| **Us vs Them** | The skin tag (or problem) talks back to the failed methods ("You really think those nail clippers scare me?"), then castor oil wins. AI animation. | #156, #189 |
| **Timeline** | Day 1 → Day 4 (→ Day 14) of one tag drying and falling off, labels on screen, result in the first second. | #78, #332 |
| **Reverse psychology** | "Do not buy Haven & Spool until you hear..." / "we lied": numbered countdown, benefits as confessions, the "lie" is the price. | #160, #79, #305 |
| **Storytelling / VO + B-roll** | Narrated story ("six months pregnant"), b-roll under VO. 1:45-2:10 for documentary VSLs. | #294, #181, #457 |
| **UGC** | One woman filming her own routine, her own voice, real before/after on screen from frame one. | #107, #332, #450 |
| **Doctor** | Authority figure explains the mechanism. | #243, #319 |
| **Duplicate** | Shot-for-shot remake of a proven outside ad, our product swapped in only where the reference shows theirs. 57 launched. | references in `ads/CATALOGUE.md` |

## 5. Hooks
- Test system: one locked body, **3 hooks** (up to 5); only the first ~3-5 s change. Same VO across visual hooks keeps
  the test clean.
- Patterns that won: result in the first second (Day montage, tag falling off); the enemy talking ("Oh, you're gonna
  try the freezing kit?"); the anti-hook ("Do not buy Haven & Spool..."); a confession ("we lied"); a ranking opener
  ("Freezing kits." + "Rating skin tag removal methods 1-10"); the offer frame ("50% OFF + A FREE BOTTLE").
- Put the angle keyword in the hook line itself (#423).
- All 120 hooks by angle: `ads/HOOK_BANK.md`.

## 6. The mechanism (say it the same way)
- Skin tags: castor oil **soaks into the root; ricinoleic acid cuts off the blood supply; the tag dries out and falls
  off**. Visual: the #156 / #189 3D animation (tag turns dark, shrinks, falls).
- Wrinkles / anti-aging: oil **soaks in vs creams that sit on top**; castor oil is ~90% ricinoleic acid, holds
  moisture, moisture plumps fine lines (Source: American Academy of Dermatology).

## 7. Editing defaults (what briefs ask for)
- **Music and captions: copy the reference** (133 and 138 of 139 briefs). Learn them from the reference with
  `/video-style-guide` before cutting.
- **B-roll**: mostly AI (34), then UGC + AI (13); UGC-only on UGC briefs. AI must pass as real phone footage.
- **Voice**: match the reference's gender, age and accent; AI VO must sound natural (ElevenLabs voice changer is
  the team's fix). Don't speed up VO to fit a length.
- **Size**: 9:16 every time; Meta safe zone top 14% / bottom 35% / sides 6%.
- Rounds: many briefs go 2-5 rounds; most notes are the items in `DO_NOT_USE.md`. Checking those before upload is the
  quickest way to cut rounds.

## 8. Before you start a new brief
1. Find the winner it builds on (the brief usually names it: "#316's angle", "#107's format") and watch it.
2. Read the same angle in `ads/HOOK_BANK.md` and the same format's corrections in `ads/REVIEW_NOTES.md`.
3. Run `vs lessons brief --brand HavenSpool` and keep those checks in the plan.
4. Product shots from the Products tab / Library; generate only what nothing fits (price first).
