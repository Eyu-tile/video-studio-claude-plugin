# Set 7 generation + build log (25 Nov 2026)

Account: WilloMd private workspace. Balance 857.81 at the start; ~93 cr spent on Set 7 (owner OK'd up to 200).
At the end the account showed 0.55 cr: other sessions spent the rest at the same time.

## Reused (0 cr)
- 23 Nov Set 7 run: mom takes for H1/H2/H3 + every body line, DAD / MOM 1 / MOM 2 testimonials, name-sticker bottles
  (Leo · Mia · Mom), brush + dot (both takes, used once each), soccer handshake (cropped waist-down, L10), aisle still.
  All named in `higgsfield/catalog.jsonl` as `s7_*`.
- Rule 2 uses the 480p take abf890fe (the 1080p 79f0b3d8 says "tea wood"/"pokewood"; it is small in the inset).
- "The one I use" says "clear drop" in both takes: the word is swapped for her own "dot" from the rule 2 take
  (use 11.72–12.04 s ← r2b 20.28–20.60 s, cut points found by test-transcribing 9 variants); the brush/dot b-roll is full
  frame there, so her lips are not on screen. Whisper large-v3 on the final: "Put a clear dot on top."
- 33 b-roll clips from Sets 1, 4, 5, 13, 17, 19, 20 (ids in `build7.py` / SHOT_PLAN.md), each once per ad.

## New (Seedance 2.5 720p, GPT Image 2.6)
| job | what | cr |
|---|---|---|
| 93577073 → 370f474f | bath-time hook frame → 5 s clip (boy in towel, knees down, thumb by the black-dot wart) | 0.75 + 35 |
| 77c3c4aa → 31306546 | fingernail about to pick a black dot, frame → 4 s clip (little motion, fine at 2.6 s) | 0.75 + 28 |
| 4be26c88 | smooth yellow callus still (split with the wart still, push-in in code) | 0.75 |
| 2af822f3 | aisle: hand takes a freeze can, puts it back (from the 23 Nov still 03473b8f) | 28 |

## Edit (`build7.py H1|H2|H3 [--preview]`)
- Layout: scene 1080x1200 on top, mom inset 1080x720 below (900 px of her selfie, blurred sides), white divider; full frame
  for "timing", "I felt awful", "My friend waited", the bonus opener, the routine, testimonials, offer close.
- Captions word by word (Inter ExtraBold, active word yellow), above the inset / mid-frame on full shots, off the end card.
- Music: "Wholesome", Kevin MacLeod (incompetech.com), CC BY 4.0 — credit goes in the post description (L1). Plays to the last
  frame, lifted on the end card, 0.4 s fade. Voice loudnorm -16 LUFS, no SFX/room tone (L7).
- End card: real PDP 3-pack photo (A08), "Not the top. The root." / "Buy 2, get 1 free · 90-day money-back" (no AI label, L1).
- Checks: lessons check PASS (L1), no b-roll repeats, shots 1.1–4.3 s, freezedetect clean, no kid faces.
- Previews: H1 133.1 s, H2 138.3 s, H3 135.4 s (`projects/rootout-set7/out/*_v1_preview.mp4`).
