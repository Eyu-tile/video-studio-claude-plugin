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

## v3 (24 Nov) — client: "the woman feels robotic, not syncing, some parts glitch; make the flow smoother"
Causes found: the mom's voice was 25 separately generated snippets, then time-stretched word by word onto Seedance clips
(Seedance re-voices the reference, so its lips followed a different, slower read) → choppy intonation and drifting lips;
the edit ran at 30 fps from 24 fps sources (repeated frames); slowed shots repeated frames; jump cuts and zoom/whip/spin
transitions; still push-ins with a sine drift jittered.
- Voice: re-recorded as one continuous ElevenLabs take per night (Helena; 6 takes + 2 night-1 retakes, n1 retake kept
  because the first read "a little file"), pauses capped at 0.5 s, nothing stretched. Verbatim check 351/351.
- Lip-sync: the 8 talking clips re-synced with **Sync Lipsync 3** (`sync_so`, cut_off) to the exact slice of the take they
  play under (testimonials to their own lines). ~4 cr/s, ~260 credits.
- Edit (`build6.py`): each night = one take, shots start on the word they show; 24 fps end to end; straight cuts (only the
  NIGHT stamps ease in); stills rendered 2x then one linear push-in; slowed shots frame-blended; calendar/end card
  re-rendered at 24 fps with fading X's. Talking shots are never jump-cut.
- Mix: music only under the voice (no SFX or room tone, per the client note on Set 18).
- QA v3: 131.98 s, 53 shots; transcript 351/351 ("hardtop" spacing only); stutter frames 45 → 0; frozen spans 0;
  −14.5 LUFS, peak −1.6 dBFS.

## v4 (24 Nov) — client workflow: Soul → GPT Image 2.6 → Seedance 2.5 720p, no Sync
- Mom: Soul 2.0 base (momD, locked) → GPT Image 2.6 scene edits (hook with bottle, night 3 with book, car, close in cream
  sweater) → Seedance 2.5 omni_reference 720p, start frame locked, native audio. First clip (night 1) = voice lock;
  the others used a 9.4 s sample of it as audio reference. All verbatim (medium.en).
- Voice: cloning the lock voice was refused (account custom-voice limit 3/3). Per the client's choice, the account's
  existing "S7 RootOut mom" voice is used everywhere: voice_change on her 5 on-camera clips (envelope match 0.97–0.99,
  0 ms shift, so lips stay synced) + ElevenLabs takes in that voice for her off-camera lines (raw/v4/vo).
- Testimonials: Seedance native voices (m1 re-rolled: the first take dropped "She's four").
- Builder: build7.py (sections = VO blocks + talking clips back to back; talking shots cut from the clip whose audio plays).
- QA: 351/351 script words, no frozen spans, 2 single repeated frames at cuts, −14.2 LUFS. Job ids: work/v4_jobs.json.

## v5 (24 Nov) — one voice: hers
- Client: "take out the main woman's audio, clone it, make the VO match — no voice change between VO and the woman".
- Cloning in Higgsfield still refused (voice limit 3/3, nothing deleted on the WilloMD account); the ElevenLabs key in this
  session has no voices_write permission. Used Seed Audio 1.0 (seed_audio) with her own Seedance voice-lock clip
  (media f06ac05f…, 9.4 s from c_n1) as audio_references: no voice slot needed.
- Speaker similarity to her real voice (resemblyzer, ref = 36 s of her Seedance clips): new VO 0.82–0.93, her own car
  clip 0.89, old S7 VO 0.65. Picks in work/clone/pick (pauses capped at 0.5 s); all verbatim.
- On-camera shots back to her untouched Seedance audio (no voice_change). Music bed 0.20 → 0.11 (client: too loud).

## v6 (25 Nov) — client: "too slow, cut the space"; shot notes
- Her lines (VO + on-camera) play 10% faster (atempo / setpts together, lips stay synced); VO pauses capped at 0.25 s;
  block gap 0.08 s; section tails 0.1–0.35 s. 147.5 s → 120.0 s, no speech gap over 0.48 s.
- 1:01–1:04 dandelion: new Seedance clip from r06's first frame (raw/v5/dand_a.mp4, job 67b04547…): flower snapped off,
  stub stays in the soil; replaces r06 + the blurry seed-head close-up.
- 1:08 "it grows back" card removed. 1:25 flip-flops now cover "I only noticed on the drive home" (her 1.3 s flash cut).
- 1:19 kid brush: start frame I2 re-edited in GPT Image 2.6 (natural foot, job 9b128f4e…) → Seedance (raw/v5/kid_a.mp4,
  job 59792279…).
- Whisper tail hallucinations dropped from word timings (clean_words). QA: 351/351 words, no freezes, 1 repeated frame at
  a cut, −15.2 LUFS.

## v7 (25 Nov) — client: music that builds, energetic, direct-response feel
- New bed: ElevenLabs Music v2.5 via Higgsfield, instrumental, 117.5 BPM (job ba6f195f…, assets/music/dr_build.mp3).
  Builds soft → full by ~50 s, short breakdown ~70 s, full energy through the offer, no fade (cut with a 0.6 s tail).
  First take (a449a025…) rejected: it faded out from 112 s, under the offer. Music is ours, so no credit line needed.
- Level 0.12 with voice ducking: music ~8 dB under her voice. −14.8 LUFS, TP −1.8. Words 351/351 (Whisper "until" for
  "till" only). build7.py --remix redoes only music/captions/mix from the last cut.

## Hooks H2 / H3 / H4 v1 (25 Nov) — on the v6 body (client chose v6 over v7's music)
- Frames (GPT Image 2.6, refs: Soul momD 1e4c170c…, H1 bedroom a2d300ba…, bottle 811f8013…): H2 bed edge + blank card at the
  drawer (141bb690…), H3 foot with wart on a pillow + her hand setting the bottle down (ef0c0424…, from W1), H4 winter
  sweater, fairy lights, snow (887791dd…).
- Seedance 2.5 720p with her voice-lock clip as voice reference: H2 33bb83b0… (verbatim, sim 0.89), H4 1b2a5f8d…
  (verbatim, sim 0.94); H3 foot insert c855773d… (no audio) + Seed Audio VO (raw/hooks/H3_vo.wav, sim 0.90, verbatim).
- Titles: H2 "Before you book the freeze", H3 "Don't book the freeze yet" (brief); H4 "14 nights of winter break" (ours —
  the brief gives H4 no title). build7.py --hook H2|H3|H4 builds the hook and reuses the v6 body sections.
- QA: H2 346/346, H4 348/348, H3 all words present (long-form Whisper skipped two lines; re-checked by section).
  No freezes. −14.5 to −15.1 LUFS; added alimiter −2 dB after loudnorm (H2 had peaked at +0.5 dBFS → −1.7).

## Delivered (25 Nov, client: "lets push it to drive")
- WilloMD Drive → WilloMD/WilloMD_RootOut_Set5 (folder 1AewKUC21IwAOx7T3hiezy1zl90mbv3UF): H1 v6 (client-chosen over v7),
  H2 v1, H3 v1, H4 v1 — all verified in Drive at exact size (request rootout-set5_20261125082718_90f4).
