# Set 17 generation log (Higgsfield WilloMd, private workspace) — H1 v1, 22 Nov

Owner choices (22 Nov): Set 17 with its own script word for word; H1 first; **lean budget ~700**; on-screen text = hook + end card only (no captions).

| id | job | model | what | credits | verdict |
|---|---|---|---|---|---|
| VO L01–L18, H2a/b, H3a/b | 22 ElevenLabs jobs (18:51–18:54) | elevenlabs_v4 | DOCTOR = Elena `ca83ca7f-c186-493d-bd69-0d765fa861b2`, MOM = Chloe `e9cfbbf0-4476-46be-b396-596eb774b165` | ~17 | OK; L16 read "with a little file" twice → "the" spliced in from the same take (`L16fix`, medium.en hears "the") |
| f1–f6 | Soul 2 | soul_2 | doctor/mom/legs/towels | ~0.7 | doctor framed inside a phone (×2), heart-shaped wart → rejected; **f4_towels kept** (paper-towel placeholder still) |
| g7_doctor | 192231bf-b5fe-422b-8fcc-59e22b2fde86 | gpt_image_2_6 high 2k | doctor start frame | 2 | OK |
| g8_mom | 5ce55856-66aa-42d9-a4ff-203f6b647772 | gpt_image_2_6 | mom start frame, boy knees-down | 2 | OK |
| g9_legs | b883de32-09b2-4e92-9977-cd412d9c3b44 | gpt_image_2_6 + real CC wart photo ref | child's foot on exam table | 2 | OK (realistic small wart) |
| D1 | 2b4a1b05-f5bc-4eb1-bdc6-1b9e9c7d68d9 | seedance_2_5 720p 24 s, lip-sync `D1_lipsync` | doctor, on-camera parts of L01 L03 L05 L07 L09 L11×2 L13 | 168 | OK |
| D2 | 528e5f00-6658-4ba3-8a86-593f0d69d5ae | seedance 17 s + bottle ref `5a42ab60…` | doctor with the real bottle, L15 L16 tail L17 L18 | 119 | OK, label readable |
| M1 | 25668707-efde-4b39-abfd-da6f782ce8ff | seedance 25 s | mom L02 L04 L06 L10 L12 L14 | 175 | OK |
| b1 | b27d0791-ec8c-41d4-92c4-523b7264e7fb | seedance 8 s | glove taps wart 0–4 · foot curls 4–6 · pulls away 6–8 | 56 | OK |
| b2 | 13cd338e-1a72-42fd-aac0-4be5fd12f330 | seedance 10 s + bottle ref | file ×2 · brush · clear dot | 70 | OK |
| b3 | 98c207d7-ccb0-44ea-8f7f-5c7ef437de4c | seedance t2v 5 s | dandelion snapped at the soil line, stub stays (no free real clip exists) | 35 | OK |
**Set 17 H1 spend ≈ 647 credits.** Lip-sync method: one long take per character from only the on-camera parts of each
line (`build_lipsync_audio.py` → `lipsync_map.json`), cut back apart in the edit; VO plays from the clean ElevenLabs files.

Account note: between 18:58 and 19:38 the WilloMd ledger shows ~3,300 credits of other Seedance/ElevenLabs/SFX jobs
that were not made by this build (another session on the same account). Balance after this build: 3,478.32.

## Output
`projects/rootout-set17/out/WilloMD_RootOut_Set17_H1_9x16_v1.mp4` — 1080x1920, 118.9 s, -14.0 LUFS, TP -2.5 dBFS.
Transcript of the render vs `BRIEF.md`: 333/333 words, no differences.

## v2 (23 Nov) — client fixes 1–10, lip-sync, no labels on b-roll
| id | job | what | credits | verdict |
|---|---|---|---|---|
| D2 redo | 1130dc95-5d14-42c5-8b5d-2fce0223dccf | bottle take; start = frame of old D2 with bottle up (`8209086f…`), audio ref only | 119 | OK — old D2 had ignored the audio (gibberish speech) |
| g20 / g21 | 50f771dd-d524-4f82-bde5-9dfbcba2f710 / 0459c33d-7aa1-4250-a627-e8821f3e0615 | 3D skin block before / healed (gpt_image_2_6) | 4 | OK, base for the explainers |
| x3 cutaway | ee317059-f193-4812-a2f9-3066d78009cf | soil cutaway: stub on top, root alive, dandelion regrows (#3) | 28 | OK |
| x6 root 3D | 692c7031-49df-42a0-8c29-7b75826f9008 | green drops reach root, root breaks, skin heals (#6) | 35 | OK |
| x9 product | 04796e0c-f595-4ad0-9afd-5d5b844a0dd0 | hand sets the real bottle on the exam counter, push-in (#9) | 35 | OK |
| x10 CTA hero | 5e57f5fc-7598-4519-9320-ab8c47a3f6e2 | 3 real bottles, hand adds the third, light sweep (#10) | 56 | OK |
| blocked | d402b065 (freeze/acid/shave), 4f2d3fe0 (lemon), 93c866ff (tea tree), 40eb7f8e (night) | Higgsfield content filter on the skin+wart start image | refunded? check ledger | not retried (no prompt rewording around the filter) → code explainers on the 3D render instead |
Fixes made in code (free): #1 hook moved to lower third with pop-in · #2 `e_top` (freeze/acid/shave hit only the top, root stays) then the
snap lands on "like picking a dandelion" · #4 `e_lemon` · #5 real footage (cream blob + amber oil drop, Mixkit) · #7 mom stays on camera +
animated arrow list with real-plant circles (`plants`) · #8 `e_night` · routine step chips · product callout · CTA overlay; separate end card removed.
**Lip-sync:** Seedance re-voices the reference audio with its own timing (drift up to ~1 s). `lipwarp.py` word-aligns each take's own speech to
our lip-sync track and retimes the picture chunk by chunk; checked by warping the clip speech the same way: mean word error 0.04–0.10 s.
**Frame grid:** every cut snapped to 1/30 s in absolute time (was drifting ~0.3 s by the end).
No "AI illustration" / FDA / † text on any b-roll (client rule, 23 Nov). The CTA keeps a small "Dramatization." only.
Output: `out/WilloMD_RootOut_Set17_H1_9x16_v2.mp4` — 118.5 s, -13.9 LUFS, TP -2.4 dBFS, transcript 333/333 words = BRIEF.

## H2 / H3 + captions (23 Nov)
| id | job | what | credits |
|---|---|---|---|
| MH | 24c9f7fe-4632-447b-b4b4-c6c6545132da | mom hook take: Lh2a + Lh3a (8 s), start g8 | 56 |
| DH | 0dc1cd74-65ee-48b3-b891-fa0c8279f89b | doctor hook take: Lh2b + Lh3b (5 s), start g7 | 35 |
H2 drops "That sounds like the root." from row 2 (`L03b`, cut at 1.6 s) as the brief says; H3 runs row 2 whole.
Captions throughout (client, 23 Nov): `make_captions17.py`, script text from BRIEF timed to VO word stamps, spoken word orange,
off the CTA, dropped low under web cards. Hook text auto-fits the frame.
Outputs: H1 v3 118.5 s · H2 v2 115.2 s · H3 v2 115.6 s — all -14 LUFS, TP -2.4 dBFS.

## Fix pass (23 Nov): client notes 0:32, 1:02, 1:40 + 7 transitions — no new credits
- Bug: `T(..., at=)` mapped mid-line pieces to the wrong take time ("So, don't wait" showed lips of another sentence; the
  "Two minutes" piece asked for take time -4.2 s → a held frame). Now take_in + (at − src_in).
- Warp speed limits: 0.65–1.6× while speaking, up to 2.2× across pauses (a chunk is a pause if <30% overlaps clip speech),
  trailing silence at 1.0× (the 0:32 glitch was a 2.6× tail). `check_lips.py` QA on every on-camera piece: all ≤0.15 s mean.
- L12 "He screams…" opens on the foot-curl cutaway (Seedance drags out "He…" too long to match without a visible speed-up).
- 7 transitions (incoming shot): x2 zoomin · x3 fade · x5 slideleft · x6 circleopen · x8 fade · x9 smoothleft · x10 fadewhite;
  0.35 s, the outgoing shot holds so the incoming one still starts on its line.
- Step chips moved to the top (were under the captions).
Outputs: H1 v4 · H2 v3 · H3 v3.

## Review page (23 Nov)
One page, three tabs (H1 v4 · H2 v3 · H3 v3): https://claude.ai/artifact/X4eY8egYcx9gqRSMrxj7cm
Built from the plugin review page (`vs present` copies, 13.6 MB each) by `make_review_page.py`; comments per ad in db collections
`comments_h1` / `comments_h2` / `comments_h3` (read back with ArtifactData list, then `vs present notes`). `#h2` in the link opens that ad.

## Delivered (24 Nov) — WilloMD Drive
Folder `WilloMD/WilloMD_RootOut_Set17`: https://drive.google.com/drive/folders/1b6iixDgArvapSbf5MWW-7UWB7aRzDsUX
H1_9x16_v4 54,681,023 B · H2_9x16_v3 53,638,474 B · H3_9x16_v3 53,844,988 B — `vs deliver verify`: all at full size.
Older versions moved to `out/old/` before planning so only the finals were picked.
