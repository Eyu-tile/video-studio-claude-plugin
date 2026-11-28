# hume-pod-dexa-2945: client comments
**Ad:** VIDEO_POD_Tech_AtHomeScan_PersonalDexaScanner_ROHIT_EYASU (brief 101126, 2026 Week 46). Supplied VO (hooks + body
mp3s, nothing generated), a study screenshot from the brief, b-roll and app screens. Delivered 9:16 H1-H3.
Review page https://claude.ai/artifact/1h4A4tFG3y7y93Qs9TCRoo. Final: v6.

Producer's direction at the start: analyse the brief and every link in it; use the supplied VO and screenshot; no footage
redundancy; every clip matches what is said; search the resources.

## Round 1: 2026-11-16, on v3 → v4
Source: producer in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | app shots | Old mobile-app footage used; use the latest recordings from the new Drive folder | Every app shot from the new folder | **Newest app recordings only** (Rule 1) |
| 2 | 0:14 | Keep the clip but start on the man using the device | In-point moved to the use | Became STRICT: product use starts at the action |
| 3 | all metrics | Metrics were static, but they are scrolling videos: scroll until the metric, then the red mark | Scroll-in then red box for every metric (`tools/scroll_card.py`) | No frozen screenshots for metrics |
| 4 | 0:34-0:40 | Keep the screenshot, add a background of a man scrolling a phone | Screenshot over phone-scrolling footage | Static images sit over moving footage |
| 5 | 0:50 | Another man using the Hume Pod | Swapped | |
| 6 | 1:13 | "45-day money-back guarantee" out of frame | Broken onto two lines inside the frame (same for "45 different body metrics") | Captions never leave the frame |
| 7 | text | Product names are "Hume Pod" and "Hume Band" (corrects the camel-case request) | Fixed everywhere | Product names (STRICT) |

Note: the new folder had only seven app recordings, so three were reused at different moments. Later the unique-b-roll
rule made that a violation: ask for more recordings instead.

## Round 2: 2026-11-16, on v4 → v5
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | 0:39 | Remove the man in the red shirt | Replaced | |
| 2 | 1:14 → end | Change the woman | Replaced | |

## Round 3: 2026-11-17, on v5 → v6
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | hooks | Hooks shouldn't feel cut; show what the person does using the device | One uncut 4.4-4.9 s shot of the whole use (step on, bend for the handle, hold the pose), then straight to the metric screen | Show the whole product use in the hook; the 3 s cap gives way to a complete action |
| 2 | own QA | H2 clip `os33` came from a folder named "ECKO - NO USAGE" | Replaced; folder added to `DO_NOT_USE.md` | **Check the source folder name for usage restrictions** |

## Round 4: 2026-11-18, on v6 → v7
Source: client comments on Frame.io (screenshots in `another_.zip`) + producer in chat, with a replacement audio clip.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | 00:00:03:12 | We can't use footage where the person is using socks on the Pod | That was Hook 2 (Kendra). New Hook 2: a barefoot woman steps on, bends for the handles and stands with straight arms (Insense creator raw, one continuous shot, ends before her elbows bend). The best alternative found had white socks too and was rejected | **Barefoot on the Pod, always**: check feet in every Pod shot (STRICT, Pod guideline) |
| 2 | 00:00:03:18 | Choose footage of a person who is not bending their arms | That was Hook 1. New Hook 1: Ucef (in-house) steps on barefoot, bends for the handles, stands with arms straight down; the shot ends before he lifts the handles to chest height | Arms straight on the handles in the scan pose (already a Pod Xmas note: now a checklist item) |
| 3 | 00:00:38:22 | Move the image a little higher, still in the safe zone | Study card moved up ~150 px (centre 37 % -> 29 % of the height); its top sits at y 380, below the 288 px top safe line | |
| 4 | 00:00:47:22 | The audio should say "Hume Pod", not "Health Pod" | The producer's clip in the zip turned out to have no speech (a 2 s bin video). Fixed in the VO itself: "Health" replaced by the same voice's "Hume" from "the Hume Health Pod" line, total length unchanged; re-transcription of the final mix reads "I've been using Hume pod" in all hooks. Caption already read "Hume Pod" | Listen for product names in supplied VO, not only captions: "Health Pod" in the audio is a client fail |

## Round 5: 2026-11-19, on v7 → v8 (Hooks 1 and 2 only)
Source: producer in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | H1 + H2 hook shot | Hooks are good, but the man's and the woman's footage must start from where they use the device; now it cuts out just as they start to use it | v7 showed step on → bend → stand, and cut as the handles came up. v8: H1 Ucef plays 2.7-7.56 s, H2 woman 2.9-7.34 s, both at real speed (were slowed to 0.86x): each starts gripping the handles, lifts them and ends holding the scan pose. Body unchanged | "Show the use" = the scan itself (handles up, holding), not the approach. Note: this shows the handles lifted, which round 4 #2 (straight arms) had avoided; the producer's newer direction wins, flagged |

## Round 6: 2026-11-19, on v8 → v9
Source: producer in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | 0:15:20-0:16:24 | Cut that voice-over and remove the "university study" footage | "and a University study." cut from the VO (15.545 → 16.79 s in H1, just after the "s" of "clinics" to the silence before "This"), a 0.20 s pause kept, 8 ms fades; captions now "medical clinics."; the binder shot `of02` is gone and the clinic shot runs through the line; every later shot, caption and the code overlay move up 1.05 s (all three hooks) | Cut a VO phrase at measured sound boundaries (high-frequency energy for the final "s"), then shift words, captions and overlays by the same amount |
| 2 | 0:35:24 | Start on the app with no image on top, then pop the image up; change the footage to a person showing weight loss or happy at the mirror | New study card (`dx_study4.py`): 1.54 s of the phone app with nothing on top ("Greater digital self-monitoring"), then on "was linked" a cut to a woman smiling at her mirror selfie (Shelby, UGC_Pod "HAPPY IN MIRROR") while the study screenshot pops up (scale 0.82 → 1.06 → 1.0) and the key line highlights 0.55 s later; card position unchanged (29 %), her face stays clear below it | A study card can open on the context shot and pop in on the claim; match its background to the claim (weight loss → happy at the mirror) |
| 3 | H2 hook | Use footage of a woman who is not bending her arms | New Hook 2: Lily (Influencer 2024, barefoot) on the Pod: bends for the handle, then holds it with arms straight out. The handle lift (elbows bent ~0.8 s) plays at 2.75x so the bend is ~0.3 s, one continuous shot, 4.44 s as before | Pick a creator whose hold pose is straight arms; speed-ramp the unavoidable lift rather than jump-cut it |
