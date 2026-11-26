# hume-pod-xmas-vsdexa: client comments
**Ad:** VIDEO_POD_Xmas_Value_VsDEXAScan_ScanFromHome_LOTTIE_DAWNASTAFFORDWILSON_EYASU (brief 201026, 2026 Week 43).
Dawna talking head (1080p, holds the Pod half out of frame from ~18 s of the body), Pod 1.0, 3 hooks, music "Inspired".
Review page https://claude.ai/artifact/FVnywkbVdboWfQCN67oXWH. Final: v5 (H1-H3, 9:16).

## Round 1: 2026-11-17, on v1 → v2
Source: producer rule in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | hooks | The hook headline stays until the body starts (strict rule) | H1 0-7.6 s, H2 0-6.4 s, H3 0-7.1 s; on in the last hook frame, off in the first body frame | **STRICT** in `EDITING_RULES.md`; end time from the measured hook end, never a fixed length |

## Round 2: 2026-11-17, on v2 → v3
Source: producer rule in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | whole ad | Every b-roll unique, no single b-roll used twice | New `tools/broll_unique.py` found `fp03` = `feet_on_pod_04` and `fp05` = `feet_on_pod_06` (same footage, other names); swapped to `fp14` / `fp38` | **Judge by footage, not file names**; test every replacement against the whole cut |

## Round 3: 2026-11-18, on v3 → v4 (client, `comm3.zip`, 13 notes on annotated frames)
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | H1 0:04 "a scan like this" | Show a bathroom scale | Pod 1.0 product image in the empty floor space, ~1 s (read "bathroom scale" as the Pod) | When a note is ambiguous, say how you read it |
| 2 | 0:30 | Old app | New-app scroll of the creator's own (female) metric list | Newest app only |
| 3 | 0:39 | Male body map | Female body map (`ui3c`) | Woman creator → female account |
| 4 | 0:58 | Bent arms on the handles | Woman holding the handles with straight arms (`gw28`) | Correct product use, per the UGC guideline |
| 5-7 | 1:01-1:03 | Glitch; remove footage; woman counting money | Producer-supplied clip of a woman counting $100 bills | No free stock fit: ask the producer for a clip |
| 8 | 1:06 | Step on and hold the handles | Woman stepping on and bending for the handles, from the step (`sam_scan`) | Product use starts at the action |
| 9 | 1:31 | Change the footage | Woman running under "and burn fat" | |
| 10 | 1:35 | Old app | New-app weight trend chart | |
| 11 | 1:44 | A woman | Woman's morning scan in her bathroom (`h2w`) | |
| 12-13 | 2:06 end | End when she stops talking | Video ends on her last word; music refitted so the song's ending lands on the last frame | (Caused round 4: see below) |
| — | knock-on | `ui3c` was already used later | That line now shows her weight screen; first candidate was a 220 lb male account, rejected | Every swap can create a repeat: re-run the uniqueness check |

## Round 4: 2026-11-18, on v4 → v5
Source: producer in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | end, all hooks | Keep the background music until the end | The v4 beds ended on the song's natural outro, which fades for ~13 s, so the music had almost gone in the last 5 s. Rebuilt the beds as one continuous stretch at full bed level with a 0.8 s fade on the final frame | **Music plays at bed level to the last frame; never land a song's outro on the ending.** Check the music level over the last 10 s before delivery |

## Watch
- On the scrolling app screens a caption can land on a number (v4/v5 ~0:29 "$50" over BMI). Offer a soft caption backing if the client minds.
- Claims: "98% as accurate as those $20,000 machines" (DEXA equivalence), "45 metrics", "no subscription", "before they sell out": strategist approval.

## Round 5: 2026-11-19, on v5 → v6
Source: producer in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | H1 "a scan like this" | Remove the Hume Pod image; show an InBody scanner in the top-left corner when she says "like this" | Pod image removed. The client's own InBody 270 photo (`08 — Partners & B2B/Hume Health Partner Assets for Content/InBody Scan for Comparison.png`) on a white card, top-left, from "like this" for 1.4 s; it stops above the hook headline and clear of her face | Look in the client's partner-assets folder for competitor product images before stock (the only free InBody photo found was CC BY-NC, not usable in an ad) |
| 2 | body 01:04:13 | Change the clip of a woman holding a product package and reaching to the camera | "You buy this one time," now a clean Pod product shot (`pod_hero_26`, unused anywhere else) | |
| 3 | body 01:08:25 | Replace with a clip where she doesn't bend her arms | `gw14` (bent over, elbows bent) → `gw04` from 2.1 s: standing on the Pod, arms held straight out with the handles | Same straight-arms rule as round 3 #4; check every on-Pod shot for bent elbows |
| 4 | end | Cut the video as soon as the woman stops speaking | The end now comes 0.06 s after her voice stops, measured from the audio level (v5 ran ~0.25 s past it: transcript end + 0.15 s pad + A-roll tail). Music still at bed level, 0.6 s fade into the last frame | End point = measured voice end, not transcript end + pad |

## Round 6: 2026-11-19, on H3 v6 → v7, then 4:5 and 16:9 of all three
Source: producer in chat. H1 and H2 9:16 are approved as they are.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | H3 0:00:02:14 | Show b-roll of the InBody scanner they use in gyms somewhere in this hook (use the InBody video supplied before) | The client's InBody clip (`121aecfb-In_functional_medicine….mp4`, a woman in a clinic gym) from 9.8 s: she grips the handles and stands barefoot with arms straight out, on "…used to charge me $50 to get." (2.36-4.71 s), headline kept on top. H3 9:16 v7, -13.8 LUFS, no repeats | The InBody product photo (H1) and a real scan in use (H3) are different shots; use the clip when the line is about the gym scan |
| 2 | all hooks | Then 4:5 and 16:9 of all three (H1, H2 straight from 9:16 v6; H3 after the fix) | 4:5 via `scripts/xd45.py` (scratch): hook A-roll framed from her head down, headline under her chin (top 470 px), H1 InBody photo scaled 82 % into the top-left above the headline, CTA at the top (90 px); every Pod shot framed so the whole Pod is in, no push-ins; `fp14` (Pod corner cut in the source) → `fp20`; `pod_hero_26` uses 2.4-4.0 s of the clip (earlier it runs off the sides, also in 9:16); captions placed per shot clear of the Pod and the red boxes (the 9:16 \pos overrides recomputed). 16:9 = the 4:5 centred over a blurred copy (house method) | Same 4:5 checklist as Muscle Imbalance |
