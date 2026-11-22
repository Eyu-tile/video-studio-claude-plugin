# hume-band-straps-ad641: client comments
**Ad:** VIDEO_Band2.0_Straps_UpgradeI'veWaited_Batch47_Milka_Ucef_Eyasu_AD641_092426_Week38_9x16.
Ucef talking head (one take, 4 hooks), Midnight Blue + Evergreen straps. v1 sent 2026-11-18
(review page https://claude.ai/artifact/KNfGLsE7PLxasJYXvc3eiE).

No review rounds logged yet. Things already applied from other projects' lessons: no punch-in while he holds a strap,
captions low and moved off the straps on close-ups, each colour shown when named, every b-roll unique, "Hume Band" on
screen, "on limited sale" checked against the audio (whisper heard "unlimited"), music at bed level to the end.

## Round 1: 2026-11-18, on v1 → v2
Source: producer, review-page comments (on Hook 1) + chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | H1 0:13:10 ("It tracks everything", app) | Footage feels too static; add more scrolling movement to make it dynamic | Band tab recording that scrolls steps → sleep → BP → heart rate → HRV → stress → temp → SpO2, at 2x (`ba3` 0-3 s) | App screens must move: pick a stretch of the recording where it scrolls (speed it up if needed); never a resting screen |
| 2 | H1 0:44:24 ("all of my data stays", app) | Same | Home tab scrolling down to Health Score 743, at 1.2x (`ba5` 75-78.4 s); a Band-tab scroll was rejected because it looked like the 0:13 shot | Same; two app shots of the same tab count as a visual repeat |
| 3 | body | Add b-rolls from his shots after the hooks | Producer allowed other moments of his long clips for this ad (visual check still enforced). Added: workout ("on my wrist for the gym"), Midnight strap stretched ("more ways to style it"), dinner ("I'd go to dinner"), Evergreen on the wrist ("They fit so well"), Band popping out of the strap ("Swapping is quick"), Midnight on the wrist ("bored of how your band looks"). Body cutaways 16 → 20, no visual repeats in any hook | Talking-head bodies need more cutaways; ask before bending the uniqueness rule |

## Round 2: 2026-11-19, on v2 → v3 (9:16), then 4:5 and 16:9
Source: producer in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | captions | Remove the shadow / strokes on the captions | Caption styles (Cap and Pop) set to outline 0 and shadow 0 in all hooks and sizes: plain white Red Hat Display Black, with the coloured pop words kept. | No stroke means a card can disappear on a light area, so on light shots (white shirt, beige wall) move the card to a dark area instead of adding the stroke back. |
| 2 | H4 0:00:03:01 | Zoom in to the Band | H4 A-roll split at 2.70 / 3.28 s: push-in from 1.0x to 1.8x while he shows the Band on his wrist, centred on the Band (zoompan anchor x 0.32, y 0.72), then a cut back to the wide when he moves. In the 4:5 the push-in is centred on the Band in the 4:5 crop (kf.y), with no framing jump. | A push-in on the product is aimed at the product, not the face; the anchor is computed so the product lands near the centre at full zoom. |
| 3 | 0:00:14:12 | Blur the numbers on the blood-pressure metric screen | `ba3` replaced by `broll_metric/ba3_bpblur.mp4`: every frame is OCR'd for the Blood Pressure card, and the reading, the date line and the chart's axis numbers are blurred (label and BETA kept). The same reading also showed in `ba5` ("and all of my data stays", ~0:42), so that card is blurred too (`ba5_bpblur.mp4`). Checked frame by frame. | When a client hides a metric, hide it on every screen that shows it in the ad, not only at the flagged timecode. |

4:5 and 16:9 (round 2): 4:5 built with `sa45.py` (per-shot focus from measured product extents; captions re-placed per shot). The strap texture close-ups (`evergreen`, `midnight`) span 77 % of the height, more than a 4:5 crop keeps, so they use the blur fit to keep the strap whole. `ev_workout` is framed low (focus 0.8) because the curl takes the Band down to 93 % of the height. The 16:9 is built from the 4:5 with the house method.
