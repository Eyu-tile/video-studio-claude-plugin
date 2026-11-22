# hume-band-fitbutdying: client comments
**Ad:** VIDEO_BAND_Longevity_ChronicDetection_FitButDying_LOTTIE_EYASU (brief 091126, 2026 Week 46). Supplied VO (hooks +
body), b-roll story, Band 2.0. Review page https://claude.ai/artifact/JTsfx4SVSc7Je3Fkj7MFkj. Latest: v6 (H1-H3, 9:16).

Producer's direction at the start: build the story around **one middle-aged woman**, not scattered people; our b-roll;
natural spacing in the audio.

## Round 1: 2026-11-17, on v1 → v2 (client, `kiruu_comm4.zip`)
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | whole ad | Use Band 2.0 everywhere | Every shot with the old Band replaced by Band 2.0 footage (van woman, doctor, hands on chest, family, closing wrist) | **Never Band 1.0** in a Band 2.0 ad; check every wrist |
| 2 | "was climbing" | Hold the heart card through the line | Held to the end of the line | Metric screen holds through its sentence |
| 3 | 30:27, 33:18, 41:16 | Change these shots | Band 2.0 shots matching the words | |
| 4 | "my whole family" | Family wearing Band 2.0 | Studio couple, then a second Band 2.0 couple | |
| 5 | bill | Show a bill with no face | Hands-only papers (no real bill footage exists; repeat agreed with the producer) | |
| 6 | ending | Unboxing / ending | Closes on a wrist raise with Band 2.0, slow push-in | |
| 7 | VO | Remove pauses | Every pause ≤ 0.12 s; hook joins the body with no gap | Tighten VO, keep it natural |
| 8 | music | Client asked for different music | Producer: keep the previous music for now; **no Higgsfield** | Ask before using AI tools; the producer decides the music |

## Round 2: 2026-11-17, on v2 → v3
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | music | Change the music to fit the ad's tone; keep everything else the same | "Revival" (Kevin MacLeod) fitted so the groove lands on "Hume Band showed" and the final chord on "Get your" | Music matches the tone of the story, with its hits on story beats |

Open at hand-off: "Two weeks from…" and the cardiac-event line clash with the no-heart-event-prediction rule; strategist
approval needed.

## Round 3: 2026-11-18, on v3 → v4
Source: producer in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | hooks | The hook b-roll of the 3 hooks must be unique: every hook needs different shots of the woman (take it seriously) | v3 shared `L_Problem_H` in all three hooks and `L_General_L` / `L___2` in H1 and H3; H2's hook cardiac screen was the same footage as the body's. New: H1 unchanged; H2 = yoga warrior + laptop calls; H3 = running + tree pose + kitchen routine + worried at her desk. Body shots swapped per hook where a hook took them | **Hooks are unique across hook versions too**, not only within one ad: no shot appears in two hooks. Run the uniqueness check across all hook versions together |
| 2 | 1:00-1:01 | Remove the short clip | The 1.06 s bill shot ("One cardiac event") is gone; the kitchen shot before it runs on through the line. It was also a second use of the checkups clip | Short sub-1.2 s inserts read as glitches; don't patch a line with a sliver |
| 3 | 1:02 "$100,000" | Money-counting b-roll where she says the money number, replacing the previous shot | Woman counting $100 bills (hands only) on "could cost $100,000." | A money figure in the VO gets money on screen |

## Round 4: 2026-11-18, on v4 → v5
Source: producer in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | ~1:01 "One cardiac event" | Still not changed: remove that clip and use something that explains the line; just that part | In v4 I had only stretched the kitchen shot over the line, so the visual still didn't explain it. Now: a heart-monitor graphic whose trace turns into a fast irregular rhythm with the rate climbing to ~200 and the screen flashing red, on "One cardiac event could cost"; the money clip starts on "$100,000."; "We're not living longer, we're living safer." stays on one shot (no sub-1 s kitchen insert) | **"Remove the clip" means put a new visual that explains the line, not stretch a neighbour over it.** No library or free stock clip fit (YouTube downloads are blocked here), so a simple code-drawn graphic did |

## Round 5: 2026-11-19, on v5 → v6
Source: producer in chat, with two SFX files (`heart_beat_.MP3`, `r_sfr.MP3` riser).
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | H1 0:05:24 | Add a beating-heart SFX | Client's `heart_beat_.MP3` with its first beat on 5.80 s, under "I try to prioritize…" at −7 dB, 4.8 s with a fade | Place an SFX's first hit on the given frame, not the file start (this file has 0.1 s of lead-in) |
| 2 | 0:24:09 | Spelling: "flag" → "flagged" | Caption now "and the AI / flagged that is / urgent." in all hooks | Captions follow the script's grammar, not a clipped transcript word |
| 3 | 0:53:16 | Center the rectangle | Health Score card rebuilt with `fbd_scroll_card.py --tile --center`: the box sits symmetric on the frame centre around "Health Score 743" | A box on a centred UI element is centred too (new `--center` option) |
| 4 | 0:58:13-1:00:24 | Footage is weird (she just looks at the camera); use a happy couple walking | "Both walking by lake" (Pod UGC, Drive) 9.6 s in, zoom 1.3 on the couple chatting with coffee, on "We're not living longer, we're living safer." | A talking-to-camera clip without her voice reads as odd in a VO ad |
| 5 | 1:11:10 | Keep "humehealth.com" on screen to the end | The closing "humehealth.com." caption holds to the last frame | The CTA text stays until the end |
| 6 | 1:12:15 | End the video when she stops talking | Cut 0.06 s after her measured last sound: H1 70.1 s, H2 71.2 s, H3 72.6 s (was +0.7 s); music fades in 0.8 s | End on the voice, measured, as on the Pod Xmas ads |
| 7 | H2 0:02:27 | Add a heartbeat-lines overlay when the heart beats, with SFX | Code-drawn ECG trace (`fbd_ecg_overlay.py`, alpha .mov) scrolls over the laptop shot 2.70-5.16 s with spikes and a red edge pulse on 2.90 / 3.90 / 4.90, the same beats as the heartbeat SFX | Graphic beats and SFX hits share one beat list |
| 8 | H3 0:03:18 | Add the riser SFX | Client's `r_sfr.MP3` from 3.60 s (+8 dB, the file is quiet), rising into "the damage" at 4.86 | |

The client's body timecodes in this round were read on Hook 3 (its hook runs 2.5 s longer than H1's); map timecodes to the hook being watched before changing anything.

## Round 6: 2026-11-19, on v6 → v7 (Hook 3 only)
Source: producer in chat.
| # | Where | Note | What we did | Lesson / rule |
|---|---|---|---|---|
| 1 | H3 riser | A bit loud; lower it, and place it between the last second of the hook and the body as a bridge SFX | Riser moved from 3.60 s to 5.65 s: it builds under "…to my heart." and peaks on the 6.60 s hook/body cut, tail 0.15 s into "I go to the gym". Gain +8 → −3 dB; measured in the mix its peak is ~5 dB below v6 (loudnorm lifts the pause it now sits in, so 5 dB on the clip alone measured the same) | A riser bridges hook → body with its peak on the cut. Check SFX level in the final mastered mix, not the clip gain |
