# Set 2 · generation log (WilloMd, private workspace ab6cddcc…)

## Step 1 (25 Nov, approved ~50 cr) — cast + narrator voice lock
| job | model | what | verdict |
|---|---|---|---|
| 775f8138 | soul_2 | narrator identity (mid-40s, sage sweater, kitchen table) | use via edit (raw has a kid face behind her) |
| 5e41eba1 | soul_2 | MOM 1 identity (early 30s, sofa, cream hoodie) | fix in edit: garbled hoodie text + kid face at the bottom |
| a3b27f60 | soul_2 | MOM 2 identity (mid-40s, rust tee, kitchen) | use |
| fb0a325f | soul_2 | MOM 3 identity (mid-50s, silver bob, hallway) | use |
| e32fc596 | gpt_image_2_6 | narrator row-2 scene: remedies on the table, kid + phone removed | use |
| ad56e80b | seedance_2_5 720p, 6 s | **T1** narrator take, row 2 line, native voice = **voice lock** | use: 12/12 words, face stable, arm sweep on "It grew back" |

Balance before: 857.81.
Balance after (25 Nov, ~19:15 UTC): **0.55 credits**. This step spent ~44.5 (4 × Soul 0.12, GPT 2.6 edit 2, Seedance 6 s 42); the other RootOut sessions spent the rest of the 857.81 in parallel. Step 2 (~445 cr) is blocked until the account is topped up.

## Step 2 (26 Nov, approved ~445 cr; balance before 3,888.79)
- Images (GPT 2.6, `step2_images.json`): narrator why/close with real bottles, MOM 1 fixed (plain hoodie, kid face removed), MOM 2 with bottle, MOM 3 with green socks, start frames for the new clips, test stills. All checked by eye.
- **Safety-blocked, not retried:** three kids' bare feet together (4d73cd6d), and close-ups of a kid's blister (166d42a4), wart back (0e60aa89) and white acid ring (c1a64d4c). The hook was re-made with socks on (71d885b1, a different picture). The three close-ups are covered by reused clips instead of re-prompting around the filter.
- Voice reference: narrator T1 audio uploaded as media c6ab93a2 (for her later takes).
- Videos (`step2_videos.json`): 6 silent b-roll (29 s) + 5 talking takes (36 s), Seedance 2.5 720p.
- Narration: 23 cloned lines + 1 re-roll (v12b, kept as backup; both read "Kid two's pad"), Seed Audio 1.0, voice ref = T1 (`vo_jobs.json`). Every line transcribed word for word.
- Videos: V06 failed once (generic error, refunded path) and was retried (81932a47). Takes: T46/T41/T43 words exact; T18 trimmed at 2.5 s (adds "Only one."); T35 MOM 2 repeats "my own hand" → jump cut 2.2–3.6 s (cheaper than a 49-cr re-roll).
- Music: "Life of Riley", Kevin MacLeod (incompetech.com), CC BY 4.0 — **credit line in the post copy**. Sidechain-ducked under the voice, short fade on the last frame only.

## v1 previews (26 Nov) — `build_v1.py`, shot lists `SHOTS_H{1,2,3}_v1.md`
- H1 151.2 s · H2 151.1 s · H3 148.8 s, 720p preview. Captions word by word (active word orange), hook title box first 3 s, end card with the real bottle + box (A12 PDP image), no disclaimer text.
- QA (`vs qa --brand RootOut`, all three): -14.0/-14.1/-14.2 LUFS, true peak ≤ -1.6 dBTP, no silences > 1 s, no black or frozen frames. Each b-roll source once per ad, no b-roll shot > 4.6 s, slowest clip 0.81x.
- Transcript vs script (H1): 404/406 words; every difference is number/apostrophe formatting by the transcriber.
- Weak beats to flag to the client: "Kid two's skin went white" uses the reused pad-press clip (the white-ring close-up was safety-blocked); the "8x" and "dandelion icon" end-card elements are not in v1.
