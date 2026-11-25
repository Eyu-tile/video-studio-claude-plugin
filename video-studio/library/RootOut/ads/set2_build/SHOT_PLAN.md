# RootOut Set 2 · U1 "Three kids, three fixes, two weeks" · shot plan (H1 first, then H2/H3 hook swaps)

Script: `SCRIPT.md` (VO word for word). Swipe: Amoils #046. 9:16, ~2:45 with H1 (final clock follows the recorded voice).
Project folder (git-ignored): `video-studio/projects/rootout-set2/`. Reuse candidates downloaded and checked frame by
frame: `projects/rootout-set2/raw/reuse/sheet_grp_a*.png` (50 clips, 0 credits). Still to eyeball before the edit: s4_D4/D5/D7/D9 and s19 b20_heels_tiles (picked from the catalogue notes).
Billing: Higgsfield `WilloMd` only (private workspace ab6cddcc…, Ultra). **Balance 25 Nov: 857.81 credits** (shared with
the other RootOut sessions).

## Lessons applied (vs lessons brief --brand RootOut)
- **House L1:** no "AI illustration" / "Dramatization" / footnotes on screen, so the end card loses that line. The hook title cards stay; captions stay word by word (L5).
- **House L2:** the narrator and the 3 moms are each made once as a Soul image, then edited with GPT Image 2.6 for each scene, then taken natively on Seedance 2.5 720p with the line in the prompt and one voice sample per person. No lip-sync pass.
- **L1 real bottle:** every bottle shot either reuses a real-bottle clip or is made on Seedance with the bottle image reference `2c52c56e…`.
- **L2/L3:** b-roll is ~3 s, one shot per phrase, cut on the narrator's word timings (`vs transcribe`), and each shot shows the word being said.
- **L4:** each source is used once; no freezes; nothing slower than 0.75x. **L6/L7:** music runs to the last frame; voice and music only, no SFX or room tone.
- **L8:** the mechanism uses the moving 3D cross-sections already made (Set 4 navy D-series, one style for the whole ad). **L10:** no kid faces anywhere.
- **L12:** every new job is added to `higgsfield/catalog.py` and pushed straight away.

## Cast (locked once)
- **Narrator:** woman, mid-40s, calm, plain knit top, bright family kitchen table (daylight). Home base for rows 2, "why", close.
- **Kid 1:** boy ~8, **blue socks**. **Kid 2:** girl ~7, **yellow socks**. **Kid 3:** girl ~6, **green socks** (VO: her wart is on a finger, visuals show her foot; we follow the script's visuals and show her sole).
- **MOM 1:** 30s, sofa, boy's foot on her lap. **MOM 2:** 40s, kitchen, holds the bottle. **MOM 3:** 50s, hallway, green socks in hand.
- Kids: socks/feet/hands/pajama legs only.

## Source codes
**R:** reused WilloMd clip (0 cr) · **N:** new Seedance clip (7 cr/s, 4 s min) · **S:** new still (Soul/GPT 2.6) + code push-in (~1–3 cr) · **T:** new talking take (Seedance native, 7 cr/s) · **C:** code graphic (0)

## Shots (H1)
| # | VO cue | picture | src |
|---|---|---|---|
| **Hook + bridge** ||||
| 01 | "We gave three kids with warts" | three kids' bare feet side by side on a rug, blue / yellow / green socks beside them; slow pan; hook title | **N** 5 s |
| 02 | "a different fix for two weeks." | same clip, pan reaches the green socks | N (same take) |
| 03 | "A freeze kit. Acid pads. And RootOut." | real lineup: duct tape, pads, freeze can, RootOut; hand sweeps across | R: s4_P1_lineup (b5365ce0) |
| **Row 2 · failed-fix line** ||||
| 04 | "Freezing, pads, acid, clippers. You've tried at least one. It grew back." | narrator at kitchen table, boxes/freeze can/clippers in front, pushes them aside | **T** 6 s |
| 05 | "Here's what we saw." | calendar page flips to day 1 | **C** (calendar graphic) |
| **Night one** ||||
| 06 | "Night one. Kid one, a wart on his foot, got the freeze kit." | blue socks, boy's foot on a parent's knee, freeze spray puff on the sole | **N** 4 s |
| 07 | "He cried." | small hand grips the chair edge | N (same take, tail) |
| 08 | "Kid two got an acid pad." | yellow socks, parent presses a round pad on the sole | **S** (GPT edit) |
| 09 | "Kid three, a wart on her finger, got RootOut at bedtime." | green socks on the bed, warm lamp, bottle on the duvet | **N** 4 s |
| 10 | "She didn't fight it." | same, toes relax, a picture book in her hands | N (same take) |
| **Week one** ||||
| 11 | "Week one. Kid one had a blister. The wart was still under it." | blue sock pulled down, pale blister over the spot, wart edge showing | **S** |
| 12 | "Kid two's pad slid off by lunch, every day." | yellow sock peeled off, the pad stuck inside the sock | **S** |
| 13 | "Kid three's dot stayed on all night." | morning light, clear dot still on, fingers peel it | **S** (green sock in frame) |
| **Two weeks** ||||
| 14 | "Two weeks. Kid one's wart grew back." | blue sock, same rough wart back | **S** |
| 15 | "Kid two's skin went white. The wart stayed." | macro, ring of soggy white skin around the wart | **S** |
| 16 | "Kid three's spot was gone." | green-sock foot, smooth sole | **S** (green sock in frame; s4_B18 smooth sole = backup) |
| 17 | (tail) | girl runs barefoot down a hallway from behind | R: s1_hallway (e73e0ad5) |
| **Why** ||||
| 18 | "So why did only one work?" | narrator to camera, bottle alone on the table | **T** 4 s |
| **Mechanism (one 3D style: Set 4 navy blocks)** ||||
| 19 | "Freezing, acid and shaving only snap off the top," | cross-section: frost, acid, blade take only the top | R: s4_D2_toponly (41c510bb) |
| 20 | "like picking a dandelion." | hand snaps a dandelion, stub stays | R: s1_dand_snap (3e99af22) |
| 21 | "The root stays under the hard skin," | soil cutaway, root alive underground | R: s17_soil_cutaway (ee317059) 0–2 s |
| 22 | "so it grows back." | dandelion back in the same spot | R: s1_dand_back (644d4a63) |
| 23 | "Kid three used RootOut. It's an oil with four plants." | bottle with lemon, cedar, pokeweed, tea tree flat lay | R: s4_P4_flatlay (c9a3a938) |
| 24 | "The lemon softens that hard skin on top, so the rest can get in." | 3D: lemon drop softens top, door opens | R: s4_D4_lemon3d (f1cf23e1) |
| 25 | "The tea tree is a thin oil. It sinks in," | 3D: drop sinks | R: s4_D5_sink (c8b506d4) |
| 26 | "up to 8x deeper than a regular cream," | paper-towel test (cream stays, oil soaks 3 sheets) + code "8x" gauge | R: s1_towels (ce962fe0) + C |
| 27 | "and carries the pokeweed and white cedar down with it." | 3D: green drop carried down the root | R: s4_D6_carry (e1c706fd) |
| 28 | "Then those two break the wart down from the root, so it can't grow back." | 3D: root crumbles | R: s4_D7_crumble (3ca33dac) |
| 29 | "One alone can't do that. Together, they get all the way down." | 3D: drops travel together to the bottom | R: s4_D8_together (d8d2be71) |
| 30 | "And the clear dot keeps them in all night." | 3D: clean skin + code clock 9 pm → 5 am | R: s4_D9_clean (80da1c88) + C |
| **Safety** ||||
| 31 | "Deep doesn't mean harsh. It's a kids' formula, ages 4 and up." | real bottle on a bedside table with a picture book and glass of water | R: s4_P5_nightbook (2ca62c5c) |
| 32 | "No acid, no freezing, no blister." | used freeze can / acid bottle dropped in a bin | R: s4_B17_bin (cc05bcb3) |
| 33 | "Just a little cool tingle." | brush paints oil on a sole (real bottle) | R: s17_b2_routine (13cd338e) 2–5 s |
| 34 | "Recommended by pediatricians." | real bottle hero, slow push | R: s4_P3_hero (7a84c998) |
| 35 | MOM 2 "I tried it on my own hand first. Cool for a second. No sting at all." | MOM 2, kitchen, holds the bottle | **T** 6 s |
| **Routine** ||||
| 36 | "Here's what you do at bedtime." | green-sock girl's bed at night, feet up, book | **N** 4 s (green socks; the reused pink-lights clip has white socks) |
| 37 | "Two light strokes with the file." | file on a kid's foot, bedtime | R: s20_file_kid (757ba2f9) |
| 38 | "Then you brush the oil on." | hand brushes oil, real bottle | **N** 4 s (bedroom, bottle ref) — s17_b2 is used in 33 |
| 39 | "The file only touches the hard top." | macro, thumb on the rough top | R: s4_B13_thumbrub (5ac712ad) |
| 40 | "Never the skin. So it doesn't hurt." | relaxed sole, clear dot pressed on | R: s19_dot_v2 (686ace6f) |
| 41 | MOM 1 "I was scared to file his foot. Two light strokes. He didn't even look up from his show." | MOM 1 on sofa, boy's foot on her lap | **T** 7 s |
| **Root Rule** ||||
| 42 | "When it looks gone, keep going 14 more nights. That's the Root Rule." | calendar crossed off, "+14" written in green | R: s4_B20_plus14 (e211dc9d) |
| 43 | MOM 3 "I kept going two more weeks after it looked gone. It hasn't come back." | MOM 3 in a hallway, green socks in hand | **T** 6 s |
| **Stakes** ||||
| 44 | "Warts spread. One can turn into fifteen." | two kids' heels on bathroom tiles | R: s19 b20_heels_tiles (45874fd0) |
| 45 | "Every fix that only gets the top means another round." | checkout belt: freeze-kit box slides toward the scanner, a hand takes it back | **N** 4 s |
| **Close** ||||
| 46 | "You can get yours from the link below. Third bottle's on us." | narrator slides the third bottle into the row | **T** 9 s (bottle ref) |
| 47 | "And if it's not gone, you get every penny back. You've got 90 days." | same take | T |
| 48 | end card | "Not the top. The root." · Buy 2, get 1 free · bottle + snapped-vs-whole dandelion icon (no AI line) | **C** |

**H2 swap:** hook over a shelf of wart boxes being swept into a basket (R: s19_shelf_sweep b18b5a5c); bridge over the three-feet clip (01). **H3 swap:** hook over a wart back on a sole (R: s19_wart_back 28fafd4b); bridge over 01. In H2/H3 the "A freeze kit…" line isn't said, so 03 drops out and 01 covers the bridge.

## Voice
On camera: each take's own voice (narrator, 3 moms). Off camera (hook, bridge, test rows, mechanism, routine, stakes):
narrator voice cloned from her first take with Seed Audio (Set 18 method, every chunk checked word for word with STT).

## Cost (estimate, credits)
| item | count | est |
|---|---|---|
| Soul identities: narrator + 3 moms | 4 | ~4 |
| GPT 2.6 scene edits (narrator ×3 scenes, moms ×3, test stills ×7) | 13 | ~25 |
| Talking takes: narrator 6+4+9 s, moms 6+7+6 s | 38 s | ~266 |
| New silent clips: three feet (5 s), blue-sock freeze (4), green-sock bed night one (4), green-sock routine bed (4), brush in bedroom (4), checkout belt (4) | 25 s | ~175 |
| Off-camera VO (Seed Audio clone, ~280 words) | ~20 chunks | ~25 |
| **Total H1** | | **~495** |
| H2 + H3 | reused visuals + VO only | ~5 |

Re-rolls are not included; at 857.81 credits there is room for roughly one full re-roll of the talking takes. Reused clips
also appear in Sets 1, 4, 13, 17, 19 and 20 (same Meta audience may see repeats of the 3D blocks, dandelion and bottles);
the narrator, the sock-coloured test and the three moms keep Set 2 its own.
