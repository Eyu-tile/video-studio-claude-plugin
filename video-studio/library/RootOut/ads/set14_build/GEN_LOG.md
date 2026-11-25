# Set 14 generation log (Higgsfield WilloMd, private workspace ab6cddcc…), 25 Nov 2026

Owner approved ~170 credits for H1. Balance at start 857.81 → 364.30 by the time generation began → 5.53 after
(other sessions spend on the same account). Job ids: `../../higgsfield/catalog.jsonl` (set "Set 14").

| step | model | count | credits (approx.) | notes |
|---|---|---|---|---|
| Characters | soul_2 | 2 | ~2 | mom (gray sweatshirt, kid's bedroom) · dad (navy henley, porch) |
| Scene frames | gpt_image_2_6 high 2k | 5 | ~10 | hook frame (kid heel, white ring, store liquid brush), mom + dad scene edits, 2 flake frames |
| Narrator | text2speech_v2 / elevenlabs, **Sloane** (b57b22a0) | 11 lines + 1 voice test | ~10 | verbatim SET14_BRIEF (numbers spelled for TTS), each line checked with speech-to-text |
| Hook clip | seedance_2_5 720p high, start frame | 1 × 5 s | 35 | words: none (VO over it) |
| Testimonials | seedance_2_5 720p high, start frame, own native voice (house L2, no lip-sync pass) | 2 (5 s, 6 s) | 77 | words exact |
| 3D flaking shot | seedance_2_5 | 1 | 0 | blocked by the safety filter (fleshy macro start frame); retry with a cleaner frame refused: account out of credits |

Not generated (no credits left): the flaking 3D shot → replaced by two free clips already on the account (k25 a72f + b0d3:
the hard top dries, cracks and flakes off over oil), same 0-credit rule as the rest of the reuse.

## Edit (H1 v1 preview, `build14.py --preview`)
- 45 shots, 126.5 s (the narrator runs ~2.8 w/s; brief clock assumed 2.6). 41 reused clips (0 credits) + 3 new + offer card + end card.
- Every b-roll shot 1.5–4.1 s, cut on the narrator's words (transcript anchors), each source once, no slow motion below 0.76x.
- Captions: script text word by word, active word highlighted, kept under the bottle on product shots, under the offer card and the end-card pill.
- Overlays (code): hook box, "8x" depth gauge, 9 PM → 5 AM clock, PDP offer card (pdp-09), end card (dandelion top vs root + real bottle).
- Sound: narrator + the two takes' own voices + "Inspired", Kevin MacLeod (incompetech.com), CC BY 4.0, ducked under speech,
  full level on the end card, 0.6 s fade on the last frame. No SFX, no room tone (L7). Credit line goes in the post copy.
- QA (`vs qa --brand RootOut`): -14.2 LUFS, TP -2.6, no silences/black/frozen frames, L1 pass; length > 90 s reels cap (by script).
  Transcript vs script: 307/307 words (differences are speech-to-text spellings only).
