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
