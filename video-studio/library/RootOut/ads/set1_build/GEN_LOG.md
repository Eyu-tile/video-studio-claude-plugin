# Set 1 generation log (Higgsfield WilloMd, private workspace)
| id | job | model | what | credits | verdict |
|---|---|---|---|---|---|
| vo_h1_hook | db730a52-7801-4220-b82f-76a619617974 | elevenlabs_v4 (Emily) | "I'm never holding my son down for a freeze again." 3.0 s | ~0.3 | OK |
| f01 | f39e944d-e2e0-4ed9-b26a-5c2872d783ea | soul_2 | mom on bed edge, night, boy turned away | ~0.12 | OK (a sliver of the boy's cheek: keep cropped) |
| f02 | 5d7880d3-db1e-4382-8abc-0f4504229417 | soul_2 | clinic freeze still | ~0.12 | RE-ROLL: fake lettering on can, wrong toes |
| f15 | ef29798e-3849-41ef-80e9-53f70bb7abea | soul_2 + bottle ref | brush routine still | ~0.12 | FAIL: Soul redrew the bottle with a garbled label, no scene |
| c01 | 15118a36-5f70-4b8e-9281-b94ec71c51dd | seedance_2_5 720p 4 s | H1 hook, lip-sync to vo_h1_hook | 28 | OK: lips follow, same face, boy stays turned away |
Running total: ~29 credits.

## Full build (21 Nov) — owner approved, ceiling ~1,135 credits
- Voice: 18 ElevenLabs v4 lines (Emily narrator; Maya, Nora, Sloane for the three testimonial moms, no-result lines).
- Frames: ~30 Soul 2 stills; re-rolled 9 (kid faces in f13/f15, fake lettering, wrong file, missing wart); 2 blocked by the safety filter (child + bare skin) and reworded.
- Video: 24 Seedance 2.5 clips, 720p, high bitrate (4 talking-mom hooks/reframe, 3 testimonial moms, 17 b-roll). All accepted for v1.
- Bottle cutout: Higgsfield remove_background on the site packshot (owner: cutouts inside Higgsfield).
- Graphics (free, code): frost cross-section, four-plants side cut, clock, calendar split, offer shelf, end card.
- Music: "Promises to Keep" by Kevin MacLeod (incompetech.com), CC BY 4.0, fitted per hook, -22 dB ducked. Credit line required.
- **Spent: 805.15 credits** (balance 8,496.67 → 7,691.52).
- Known v1 issues: brush clip's wart looks a little red/raw; clinic can lettering blurred; trash-bin shot dropped (gibberish text);
  nightstand bottle is AI (soft focus, label not readable); "Recommended by pediatricians" and the kids-formula/four-plants
  conflict are still unresolved claims (see library ads/ROUND1_SCRIPTS.md).

## v2 pass (21 Nov): captions, no AI-customer text, realism
- Removed the "AI-generated people. Not real customers." overlay (client request). End card keeps "AI illustration."
- b05 re-rolled: Seedance job 69410575-c340-48ab-b66b-17c4c41ffcbc -> raw/gen/clips/b05_wart_back_v2.mp4 (28 cr). Old b05 read as a smooth grey disc.
- Higgsfield Mirelo SFX (spray, lamp click, footsteps, water pour, paper crinkle): 3.75 cr. Soul rerolls ~0.24 cr.
- Sound bed: room tone/ambience under every silent AI shot + foley on the actions (build_edl.py sound_design()).
- Captions: whisper transcript of each render, spelling fixes, bold-pop (work/make_captions.py), moved off disclaimers and product graphics.
- Finish (work/finish.sh): luma grain, 1 px lens fringe, vignette, light sharpening; loudnorm TP -2.2 + limiter.
- Balance after: 7,659.28 (total Set 1 spend 837.39 of the ~1,135 ceiling).

## v3 pass (21 Nov): urgency CTA + 3D motion animations (client asked for motion like the reference, Amoils #004)
- CTA VO vo19_cta (ElevenLabs v4, Emily, job b6c5318b-0628-4927-a9c7-9cb63ef0dea9): "Tap the link below and check if Buy two, get one
  free is still on. And you're covered by our ninety-day money-back guarantee." Replaces vo11 ("if it's not gone, you get your money back").
- c19_cta: Seedance 8 s, start f01 + real bottle reference + vo19 lip-sync (job 66f71352-9c0e-4287-bd00-31719ee13cfa). Label reads RootOut.
- 3D skin-block style frame: Soul job f74904d2-7446-436d-9088-644bbab32ea4 (the only keeper; Soul turned other block frames into cake; a mom
  frame with f01 ref was nsfw-flagged). Seedance clips with it as style/start ref: m1_frost 54e0a6ac (4 s), m2_soak 9d811e6b (7 s),
  m3_root d6a635db (5 s), m4_night f7f0ab6a (4 s). They replace the flat PIL g11/g12a/g12b/g19.
- Code motion (free): g26_stakes push-in/float/shine; g27b_offer_cta (drop-in bounce, pulsing pill, "while the offer lasts", 90-day seal stamp,
  glass shine); g28b_end_cta (rising line, floating bottle, swaying dandelions, pulsing "Shop now" with tap ripple, "AI illustration.").
- Spend this pass 197.77; balance 7,461.51; Set 1 total ~1,035 of the ~1,135 ceiling.

## v4 fix (22 Nov): c04 reframe redone with the real bottle
- Client note: at 0:18-0:20 ("Here's what the freeze missed") the mom held a generic pill bottle. Seedance redo, start f01 + bottle ref
  2c52c56e + vo04 lip-sync (job fd51d751-47b1-4e7c-b754-783cb25fff91, 35 cr). Old clip kept as c04_reframe_old.mp4.
