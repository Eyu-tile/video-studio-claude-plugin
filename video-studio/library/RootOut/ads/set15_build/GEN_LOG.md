# Set 15 generation log (Higgsfield WilloMd, private workspace ab6cddcc…), 26 Nov 2026

Owner approved H1 (~465 cr quote + ~70 buffer). Spent ≈ 625 cr (by job time in `transactions`; other sessions spend on
the same account). Job ids: `jobs.json`. Every generation is in `../../higgsfield/catalog.py` (Set 15).

| step | model | count | credits | notes |
|---|---|---|---|---|
| Mom identity | Soul 2 | 2 | ~1 | bfb7aff9 kept (late 30s, real, tired); 592d761f rejected (too young) |
| Scene start frames E1–E9 | GPT Image 2.6 high 2k | 9 | ~20 | same face everywhere; real bottle ref 2c52c56e holds the label (E2, E3, E5, E6) |
| Mom takes M1–M7 | Seedance 2.5 720p omni_reference, native voice | 7 | 455 | M1 = voice lock (163 Hz); M2–M7 use M1's audio as `audio_references` (167–183 Hz). Took longer than the quote: M2 9 s and M3 15 s carry the whole Dandelion / four-plants lines in her own voice instead of cloned VO |
| Boy shots B1–B4 | Seedance 2.5 720p, native voice | 4 (+1 blocked, refunded) | 140 | B1 = his voice lock (234 Hz); B2–B4 use B1's audio. B3 v1 (bare foot on a pillow) **blocked by the safety filter** → socks + dino pajama legs |
| Re-voice 2 lines | Seed Audio 1.0 cloned from M1 / B1 | 4 | ~4 | M3 said "white sledder" (2 STT models agree) → fix_m3_a "white cedar" (pauses tightened = fix_m3_c); B2 said "I miss swim" → fix_b2_a "I missed swim". Both play under b-roll (no lips) |

Reused free (account's own clips, frame-checked): S1 b04 clinic, S17 x3 soil cutaway, S13 m1 skin door, S1 b10 towels,
S17 x6 root 3D, S13 m2 root dissolves, 25 Nov file macro (b62b060b), S17 b2 routine (real bottle), 23 Nov brush+dot
(807a3b6b), S17 x10 three bottles. Brand site video `shopify-3062835a` (freezing vs oil) cropped below/above its labels
(one carries a † mark, house L1).
Music: "Pamgaea", Kevin MacLeod (incompetech.com), CC BY 4.0 — credit line goes in the post copy.

## Edit (H1 v1, draft)
- `build15.py`: 24 shots, 74.2 s. Every spoken line is the speaker's own take audio (lips and voice made together), cut on
  the words (ElevenLabs STT); b-roll 1.5–4 s, each source once; talking shots get a slow push-in.
- M7 laughs between its sentences and the bottles fly off after ~4 s → first sentence on camera, laugh dropped,
  "And if it's not gone…" over S17 x10. B3's top edge (his chin) cropped off (L10). B4 take shows the smooth sole.
- Bug fixed before delivery: 24 fps takes through zoompan played 1.25× fast (lip drift + tail freezes) → fps=30 first.
- QA: transcript 201/202 script words (only "RootOut" heard as "root out"); `vs qa --brand RootOut`: -14.1 LUFS,
  -1.5 dBTP, no silences, no black or frozen frames, lesson L1 pass. Captions bold word by word, active word highlighted,
  moved to the top on the routine bottle shot and the close (L5). Voice + music only (L7); music to the last frame,
  lifted on the end card (L6). End card: "Not the top. The root." · Buy 2, get 1 free (no "AI illustration", house L1).
- Out: `projects/rootout-set15/out/WilloMD_RootOut_Set15_H1_9x16_v1.mp4`.

## v2 (26 Nov) — owner: "do all of those changes" (from the Amoils #022 swipe analysis)
- **Bottle in the boy's hand early:** new B5 (kid's hand + navy sleeve pushes the real bottle to the lens) on "Then I found
  out why." at ~10 s (the swipe shows it at 7.8 s). The couch-frame version was blocked by the safety filter (bare kid
  foot) → hand-only close-up.
- **Before/after on the result line:** rounded photo insets (top right) cut from the boy's own couch frames: wart sole on
  "About two weeks…", clear sole on "…and it was gone" (swipe 0:11). No labels (house L1). AI images (owner's call).
- **Hand-held end card:** new E1 (woman's hand holds the real bottle in the blurred kitchen) + overlay: "Not the top. The
  root." · "Buy 2, get 1 free" · red "Shop now!" sticker + arrow down to the link (swipe's last 4 s). 3.6 s.
- **Hook caption** = his words: "They froze my wart / five times." (the bottom caption is skipped while it shows).
- Cost: 2 GPT Image frames (+1 blocked) + 2 × 4 s Seedance ≈ 60 cr. Proxy ad analysis 2 credits.
- QA: transcript matches the script; `vs qa --brand RootOut` all PASS (-14.1 LUFS, -1.4 dBTP, no freezes, L1).
- Out: `projects/rootout-set15/out/WilloMD_RootOut_Set15_H1_9x16_v2.mp4` (75.1 s).
