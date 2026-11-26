# Set 6 · Higgsfield (WilloMd) generation log

Account: WilloMd private workspace ab6cddcc…, Ultra. Balance 857.81 at plan time (25 Nov); first pass H1 approved (~420 cr).
All jobs also logged in `../../higgsfield/catalog.jsonl` (L12).

## Pass 1 (25 Nov)
| job | model | what | verdict | cr |
|---|---|---|---|---|
| 77f0a066 / 16deaad4 / dbc1310c / aee21248 | soul_2 | mom identity, 4 options | **dbc1310c = identity**, 77f0a066 backup | 0.5 |
| e5b43ab6 / c1ae75fa | gpt_image_2_6 | edit of dbc1310c: real bottle in hand, fridge text removed | **e5b43ab6 = start frame** (label readable), c1ae75fa backup | 1.5 |
| 0c2f00ce | gpt_image_2_6 | N1 sneakers by the door | use | 0.75 |
| ecb59073 | gpt_image_2_6 | N2 shoe shaken over the sink | use | 0.75 |
| 56952fc2 | gpt_image_2_6 | N3 tweezers + flashlight, dino pajamas | use | 0.75 |
| d6e750aa | gpt_image_2_6 | N4 two spots on the heel | use | 0.75 |
| d7ee7fcf | gpt_image_2_6 | N5 soccer bench from behind | use | 0.75 |
| 6ddd5d40 | gpt_image_2_6 | N6 shoe pile, his sneakers on | use | 0.75 |
| 4c859dd3 | gpt_image_2_6 | N7 blank clinic card on the fridge | use | 0.75 |
| 281451bc | seedance_2_5 720p 11 s | K1 hook take (start e5b43ab6 + bottle ref): 28/28 words, natural, bottle label readable; her voice = Set 6 voice | **use** | 77 |
| G1 walk to school, G2 sideline moms | seedance_2_5 | **not submitted: account out of credits (5.53 left)** | — | 0 |

Spent by this set so far: ~84 cr. The shared balance fell from 857.81 to 5.53 while this pass ran (other RootOut sessions).

## Free (code)
`render_gfx6.py` → hook boxes H1/H2/H3, citation card (van Haalen 2009; PubMed blocks this server with 403, so a code card
per the script's "show as a citation card"), 8x gauge frames, offer card + 90-day seal, end card "Start before it spreads."

## Pass 2 (26 Nov) — owner: "more natural, the way she talks in the hook; do the whole ad with the body"
Decision (owner, 26 Nov): every line on camera in her own Seedance voice; b-roll cuts away over her take audio. No cloned VO.
Voice reference for all takes: K1 take 1 audio (media 260e1746…, timbre only, "never its words"). Test take T07 first: words
exact, f0 174 vs 182 Hz, natural sigh → then the batch. All takes checked with `qa_takes.py` (ElevenLabs STT vs script, f0).

| take | job | s | result |
|---|---|---|---|
| T07_next (test) | 968ed216 | 5 | OK |
| T02 … T13b (15 takes) | see `jobs.json` | 153 | all word-exact; T09b adds "Three simple steps," before the line (trimmed in the edit) |
| K1 re-shoot 1 | c0ecee8b | 11 | still "lumping" → reject |
| K1 re-shoot 2 (pronunciation note) | bddeb77d | 11 | "limping" clear → **use** |
| T10b take 1 | 633b5920 | 14 | "poke wood", "white clier" → reject |
| T10b re-shoot 1 | fc4d3b9e | 14 | pokeweed OK, "white eyeliner" → reject |
| T10b re-shoot 2 (phonetic) | ff5e21b4 | 14 | pokeweed OK, "white seed Dieter" → **use with patch** |
| G1 walk to school | cb0f5b4a | 4 | use |
| G2 sideline moms + real bottle | 56e01931 | 5 | use |
| Seed Audio patch ×3 (ref fcc246df = 31 s of her takes) | 5eac3787 / e3ab1ac7 / 8c5a0d4c | — | 5eac3787 used: "and carries the pokeweed and white cedar down to the root." spliced into T10b (gain 0.84, f0 184 vs 180 Hz), plays only under b-roll (692c7031 3D root + b747a959 root pull), never over her lips |

Spent this pass ≈ 1,630 cr (takes 1,176 + test 35 + G1/G2 63 + re-shoots 350 + audio ~3). Balance 3,961 → 673 (shared account; other sessions ran too).
Music: "Wholesome", Kevin MacLeod (incompetech.com), CC BY 4.0 — credit line goes in the post copy, not on screen.
