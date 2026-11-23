# Set 13 generation log (Higgsfield WilloMd, private workspace, 22 Nov)
Owner approved a ceiling of ~1,060 credits. Job ids: `jobs.json`.

| step | model | count | credits | notes |
|---|---|---|---|---|
| Voice (Mom A = Naomi, MOM 2 = Chloe) | elevenlabs_v4 | 11 lines | ~10 | all 11 checked word for word with whisper |
| Master cast | soul_2 | 6 | ~1 | Soul kept adding the girl's face and the raised finger read as a rude gesture; 1 flagged. Kept f01a's mom only |
| Scene start frames | gpt_image_2_6 high 2k (f01a as ref, real bottle as ref) | 17 | 34 | bottle label held exactly; F10 rerolled (game logo on the boy's shirt) |
| Talking / action clips | seedance_2_5 720p high, omni_reference, lip-sync to the voice file | 14 | 714 | c04 first try flagged by the safety filter (refunded), re-worded |
| Kid lines | seedance_2_5 native voice (mouth never in frame) | 3 (c02, c10, h3a) | incl. above | all three said the exact words first time |
| 3D skin side cut | seedance_2_5 from a gpt_image style frame | 2 (m1, m2) | 70 | lemon door + tea tree carries; root dissolves + clear dot |
| **Set 13 total** | | | **~860** | |

Account note: between 19:00 and 19:08 the account also spent ~1,450 credits on ElevenLabs, Soul and Seedance jobs that this
build did not submit (another session or user on the same workspace). Balance after: 5,081.08.

## Edit
- Speaker audio is always the clip's own lip-synced track (brief: no voice-over over b-roll). Real b-roll and screenshots
  sit as cards in the upper half while the speaker stays on camera.
- Adult lines run at 1.07x (pace; brief clock assumed 2.6 w/s, the voice runs ~2.3), kids at 1.0x. Trailing silence trimmed.
- Captions: whisper word timings per clip → 3-word bold caps, current word yellow (Inter ExtraBold).
- Music: "Wholesome" by Kevin MacLeod (incompetech.com), CC BY 4.0, -19 dB under speech. Credit line required.
- Finish: 1 px fringe, luma grain, vignette, light sharpen; loudnorm -14 LUFS, TP -2.2.

## Open items for the client (Set 13 v1)
- **Kids' formula vs the plants** (ROUND1_SCRIPTS check #2, confirmed on the live FAQ): the Kids 4+ oil has no thuja (white
  cedar) and no pokeweed, yet the locked script says "kids' formula, ages 4 and up" right after "pokeweed and white cedar break
  the wart down". Kept word for word; the site FAQ screenshot was left out because it contradicts the line on screen.
- "Recommended by pediatricians", "about two weeks", "never came back", "no scar": still [proof needed]. All testimonials are AI.
- On-screen labels: finger photos "AI illustration"; end card "AI illustration."; † and * footnotes ride on the 8x and plant lines.
- Real third-party pages (AAD, Cleveland Clinic) shown as quoted screenshots, no logos implying endorsement: legal to confirm.
- Kid voices are Seedance's own voices (no adult voice actor); mouths never in frame.

## v2 (23 Nov, owner notes)
- 0:37 odd hand movement at the start of the four-plants shot: the 3D side cut now starts on the shot's first frame.
- Removed the bottom "*Benefit claims… not FDA evaluated" footnote (owner request). The † 8x footnote stays.
  Compliance note: CLAIMS.md asks for that disclaimer wherever the plants "break the wart down" — the client should confirm dropping it.
- Hook redone: new warm start frame (gpt_image, 2 cr) + Seedance 8 s (56 cr; dropped "start to finish", kept as c01_v2a_dropped)
  + reroll 9 s (63 cr, full line). Bigger two-tone title, before/after proof pop (zoomed on the wart, "AI illustration"), lighter grade.
- Set 13 total now ~980 credits.

## v3 (23 Nov, owner notes)
- Before/after card in the hook: "AI illustration" label removed (owner request; the gallery photos at 0:16 and the end card keep it).
- Four-plants beat (0:37–0:50): the 3D skin animation is now full screen (the mom is hidden), slowed to fill the beat
  instead of looping; plant photo chips sit in the sky band, "8x deeper†" at the bottom, real root photo centred at the end.
- No new generation (0 credits).
