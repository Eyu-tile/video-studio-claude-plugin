# Set 18 generation log (Higgsfield WilloMd, private workspace ab6cddcc…), 24 Nov 2026

Owner: "finish hook 1 with the body, use existing Higgsfield clips" (approved ~680-credit H1 quote). Job ids: `jobs.json`.
Balance at start of H1: 1,161.93 → 525.03 after (other sessions spend on the same account; this build ≈ 640 by job).

| step | model | count | credits | notes |
|---|---|---|---|---|
| Voice, dad = **Mark** (preset 27c04473…), daughter = **Pixie** (0178ef57…) | text2speech_v2 / elevenlabs | 21 lines + 1 re-take | ~10 | verbatim from SCRIPT.md (numbers spelled for TTS); every line checked with ElevenLabs STT; r03 re-recorded ("wart" read as "war") |
| Dad master + 6 start frames | gpt_image_2_6 high 2k | 7 | 14 | same face in all; real bottle ref (811f8013) / 3-pack ref (e2d50d17) hold the label |
| Talking takes K1 26 s · K2a 9 · K2b 24 · K3 13 · Y1 5 · Y2 4 + hands G1 4 | seedance_2_5 720p high, omni_reference, lip-sync audio = only the on-camera pieces (`timeline.py`) | 7 | 595 | all words matched (K1 79/79, K2a 17/17, K2b 71/71, K3 38/38, Y1 9/9, Y2 7/7); K2b took ~50 min in the queue |
| Stills N1–N3, N5, N6, N9 | gpt_image_2_6 (heel ones edit a frame of S19 b21) | 6 (+3 flagged) | ~18 | N4 second bump, N7 acid ring, N8 sticky sock **blocked by the safety filter: not reworded** |
| N4, N7, N10 | code (OpenCV) on the son's heel / N5 | 3 | 0 | N8 → real CC tape photo (Conklin, CC BY 2.0) + S19 b25 socks |

Reused free (account's own clips, `REUSE.md`): 20 clips from Sets 1, 13, 17, 19, 20. Real stock: Mixkit 32176 doctor, 19551 sprinkler.
Real web screenshots: PubMed 19438464 (van Haalen 2009), PubMed 24019275 (Bruggink 2013), AAD warts-treatment (×2).
Music: "Investigations", Kevin MacLeod (incompetech.com), CC BY 4.0 — credit line in the post copy.

## Edit (H1 v1)
- 71 shots, 172.2 s (the voice runs at the swipe's pace, ~3.1 w/s; the brief's clock assumed 2.5), captions on, selfie.
- Talking shots retimed to the VO word by word (`build18.py`, Set 17 lipwarp method on ElevenLabs STT anchors).
- QA (`qa18.py`): transcript 489/489 script words (only formatting differences), no frozen frames ≥ 0.5 s, every b-roll
  source used once, -14.1 LUFS.
- Not used (no licence/download here): the 4 YouTube picks; free fallbacks in their place.

## v2 (24 Nov) — client: "his audio seems off, not natural, not syncing; more b-roll, faster; energetic music"
- **Voice rebuilt:** on camera = each Seedance take's OWN audio (lips and voice generated together → no drift, no retiming);
  off camera = **Seed Audio 1.0 cloned from the dad's takes** (`audio_references` = 63 s of K1+K2b+K3 speech, media 4a70d5a1…),
  19 chunks (~21 cr), every chunk checked word for word. Pitch 118 Hz vs takes 124 Hz (old ElevenLabs preset: 113 Hz).
  Higgsfield `create_voice` refused (account voice limit; the two saved voices belong to other sets — not deleted); the
  connected ElevenLabs key is speech-to-text only.
- **More b-roll, faster:** 82 shots (was 71), median 1.9 s, dad on screen 32 % (was 50 %); cutaways over his long lines;
  new sources: Mixkit 17475 doctor, 31411 sleeping kid; S19 b60, b32, b39; S17 x9; brand site videos (how-to brush,
  freezing-vs-oil cross-section, cropped below labels); PDP "vs freezing" and "Buy 2 / 90 days" cards. Gaps 0.02–0.15 s;
  whole ad at 1.1× (take audio and lips sped together, pitch kept): **152.9 s** (was 172.2).
- **Music:** "Pamgaea", Kevin MacLeod (incompetech.com), CC BY 4.0 (was "Investigations"), ducked under the voice.
- QA: transcript 489/489 (formatting only), no frozen frames, each b-roll once, -14.1 LUFS.
- Out: `out/WilloMD_RootOut_Set18_H1_9x16_v2.mp4` (122 MB). Builder: `build18v2.py`.
- v2 audio pass (24 Nov, client): **all sound effects removed** (whooshes, pops, lamp click, end-card whoosh) and the room-tone bed; voice + music only. Transcript 489/489, -14.1 LUFS, no freezes.

## v3 (24 Nov) — client: "skin/lighting robotic → Soul character, GPT 2.6 for props; natural casual acting; no sync forcing"
- **Character:** Soul 2 base (s3, job 3314f013) → GPT Image 2.6 scene edits (props, bottle, three bottles, backyard, coffee).
- **Takes:** Seedance 2.5 720p, each scene image locked as start frame, the line written in the prompt, natural casual
  direction, his own native voice (no audio-reference lip sync). 11 takes (K1a–K1d, K2a, Y1, K2b1–3, Y2, K3); K1b and K2a
  re-shot (cut-off word / skipped sentence) with the hook's voice as a timbre-only reference. All words match the script.
- **Voice lock:** first take (K1a) = the voice; all 16 off-camera lines re-cloned from it with Seed Audio (raw/vo4, gaps
  tightened by `compact_vo.py`). Bedtime line re-recorded once ("a little file" → "the little file").
- **Edit (`build18v3.py`):** 0–7 s dad only; every dad segment ≥ 4 s with a slow push-in; b-roll runs split into equal
  ~3 s shots (2.7–3.8 s; soil cutaway 4.2 s, one move); one study card (van Haalen) + real b-roll (sneakers, doctor,
  wart close); no infant clips (b35/b37/b55/31411 out; S17 b2 routine, S1 b11 nightstand, S19 b52 socks in).
- QA: transcript 489/489 (formatting only), no freezes ≥ 0.5 s, each b-roll once, -14.1 LUFS, 153 s, 39 shots.
- Cost: sync-method takes started before the client's note (~660 cr, kept only for comparison) + native takes ~760 cr
  + VO ~20 cr. Out: `out/WilloMD_RootOut_Set18_H1_9x16_v3.mp4`.

## H2 / H3 (24 Nov) — client: "this good, let's do the rest 2 hooks"
- Takes (Seedance 2.5 720p, s3 start frame, hook voice as timbre reference, line in the prompt): H2 9 s (air quotes,
  slow blink), H3 10 s (one finger, then two), K1c_h3 7 s ("She's wanted everything… This, she got." on camera, so the dad
  segment stays ≥ 4 s once H3 drops the study). ~180 cr. Words exact; pitch 105–113 Hz (hook 109).
- Per SCRIPT.md: H2 row 3 = "My son had one wart on his heel. One." (t03_h2, heel close-up); H3 row 6 starts at
  "And the 'it'll go away' part…" (t06_h3; doctor + wart close b-roll). Hook boxes: hook_h2.png, hook_h3.png.
- Builder: `HOOK=H2|H3 python3 build18v3.py` (shared content-keyed shot cache); QA: `HOOK=Hn python3 qa_hook.py`.
- QA: H2 473/473 words, -14.1 LUFS, 151 s · H3 464/464 words, -14.1 LUFS, 144.5 s, no freezes.

## H4 (24 Nov) — client: "I forgot hook 4, do that first"
- Take H4 9 s (s3 start frame, hook voice as timbre reference): words exact, 104.6 Hz. ~63 cr. Body as H1.
- Hook boxes: H4 "We stopped leaving it." (the full line clipped at 1080); H3 box rebuilt smaller (was 1252 px wide,
  clipped at the edges in the first H3 delivery) and H3 re-rendered.
- QA: H4 485/485 words, no freezes, -14.1 LUFS, 153.5 s · H3 re-check 464/464, no freezes, -14.1 LUFS.

## Delivered (24 Nov, approved by the client: "push all 4 hooks to the drive")
- WilloMD Drive › WilloMD_RootOut_Set18 (https://drive.google.com/drive/folders/1ALqQGyAR7lVGRlRKok0Km2Udfq625sZ6):
  H1/H2/H3/H4 `_9x16_v3.mp4`, all verified at full size (110.6 / 109.6 / 104.1 / 111.4 MB). Request id
  rootout-set18_20261124195156_3232.
