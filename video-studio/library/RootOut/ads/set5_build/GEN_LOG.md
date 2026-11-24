# Set 5 H1 generation log (Higgsfield WilloMd, private workspace ab6cddcc…), 24 Nov 2026

Owner: "build the first hook with the body; reuse clips already generated on Higgsfield, generate only what's missing,
nothing that looks like AI slop; script exactly as the brief." Job ids: `jobs.json`. Reference read first:
`../../references/sofyre-004/ANALYSIS.md`.

| step | model | count | credits (approx) | notes |
|---|---|---|---|---|
| Voice: narrator **Helena** (preset 3c2b83c0…), moms **Willow / Livia / Hallie** | text2speech_v2 · elevenlabs | 25 lines + 2 re-takes + 1 test | ~3 | verbatim from `SET5_BRIEF.md` ("8x" read as "eight times", "90-day" as "ninety-day"); every line checked by STT; v03 re-recorded ("a little file" → "the little file", confirmed with whisper medium) |
| Start frames: mom master + nights 1/3/10/14, 3 testimonial moms, car flip-flops, nightstand tap, crayon calendar, kid brushes, wart night 1 → 3 → 7 → 14 (edits of one foot) | gpt_image_2_6 high 2k | 18 (1 rejected: girl's room) | ~35 | real bottle photo 811f8013 as reference wherever the bottle shows; wart base = frame of S19 b60 |
| Talking clips t01 11 s · t06 10 · t13 4 · t19 7 · t27 13 · m1 8 · m2 8 · m3 5 | seedance_2_5 720p high, omni_reference + line audio | 8 | 462 | t13 first submission refused (audio < 2 s), padded and resubmitted |
| Inserts: kid brushes 5 s · flip-flops 4 · nightstand tap 5 · crayon X 4 | seedance_2_5 | 4 | 126 | all bottle labels readable |
| Blocked by the safety filter (**not reworded**): wart night 3 / night 7 clips (child's bare foot), new 3D tea-tree clip | seedance_2_5 | 3 | refund status unknown | wart nights use the stills with code push-in + handheld drift; tea-tree beat rebuilt from reused/real footage |
| Voice-change test on t13 | voice_change_merge | 1 | small | kept the clip's lower pitch, not used |

Balance 7,426.51 → 6,518.33 (−908) across this build; the jobs above add up to ~650 by my count (other sessions spend on
the same account; blocked jobs' refunds not confirmed).

Reused free (the account's own clips): 16 from Sets 1, 13, 17, 19, 20 (`jobs.json` → `reused_free`).
Real footage (Mixkit / Coverr free licences, Flickr CC BY / PD; credits in `../../stock/assets/set5/SET5_BROLL.md`): pool
feet, lemon tree, watering seedling, dandelion meadow, touch lamp, plantar-wart photo, tea tree, pokeweed, white cedar,
dandelion roots. Real brand footage: RootOut how-to loop (brush, cover). Real web cards: RootOut PDP (night 1, bundle
tiers, guarantee), AAD (black dots, repeat freezing). Music: "Dreamer", Kevin MacLeod (incompetech.com), CC BY 4.0 —
credit line in the post copy.

## Edit (H1 v2) — `build5.py`, `make_gfx5.py`, `qa5.py`
- 128.6 s, 63 shots (~2.0 s average; swipe 1.7 s), captions on every shot (script text on the voice's word times).
- Talking clips: Seedance re-voices the reference, so its audio is not used. Our ElevenLabs line is placed phrase by
  phrase on the clip's own word times (lips match, narrator voice identical to the voice-over), and long pauses are
  jump-cut (video + voice cut together).
- Swipe devices (SoFyre #004): crayon NIGHT stamps on the blurred next shot, split screens (real plant / its job in the
  3D side cut), grey + red X for freezing / acid / blister, real PDP bundle card with a tap, 9 pm → 7 am clock.
- House rules: no 'AI illustration' / footnote text on screen (L1; the brief's end-card line dropped), no frozen frames,
  lip-synced clips only under their own line, real bottle in every product shot.
- QA v2: transcript 351/351 script words; no frozen spans ≥ 0.5 s; −14.3 LUFS, peak −1.6 dBFS. Repeats are one clip
  carried across back-to-back shots (r03 door/drop, r04/r05 root, pool) and the brand how-to loop (brush, cover).

## Open (client)
- Night 14 "It's gone" on a foot vs the PDP's "Weeks 4–8: feet and corns take longer" (kept verbatim, flagged).
- "Recommended by pediatricians", kids' formula vs pokeweed/white cedar, 8x proof (towel test is an AI placeholder).
- AAD screenshots in a paid ad: client legal to confirm.
