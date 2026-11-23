# #457 "The oldest anti-aging secret": production plan

Sources read: the brief (Hyperscale, round 1, unchanged 2026-11-23), Gabriel's 10-min walkthrough
(`refs/drive_1v4F/`, transcript + every storyboard frame he opened, saved in `refs/storyboard/`), the two
reference ads (`refs/main_ref/` Frøya "ancient Viking remedy", `refs/ref2/` cacao bar) and the Swedish-babies
VSL (`refs/drive_1jfs/`, voice reference only). Haven & Spool lessons: `vs lessons brief --brand HavenSpool`.

## What Gabriel asked for (his own words, walkthrough)
- **The script structure = the cacao ad (ref2)**: "this is the main one honestly". Hook question → "I'll give you
  a hint" → "This is a castor bean" (cacao pod) → ancient medicine → "But then anti-aging became an industry"
  (sugar) → "We truly believe the future of…" → "One ingredient. That's it." Copy its caption style (below).
- **The look = branded editorial collage**, "something more brandable, people trust it more", in the brand colours.
  The storyboard frames are **inspiration, not to copy exactly**: "I'm not saying to use this exact one".
- **Real, not AI**: "I don't want it to feel AI, I want it to feel real… like someone actually filmed it, spent time
  on it." From the benefits onward, **real shots of real people**, especially the social proof ("we have a lot of
  real shots").
- **Mechanism as clean animation**, like Frøya's skin-repair animation (main_ref ~0:28-0:35): "it's animated,
  that's something I like."
- **Voice like the Swedish-babies VSL**: natural, "not something screaming at you", a woman who'd actually say it.
  Frøya's VO flow is also good. No AI presenter talking to camera.
- **Hook visual that pops**: "the woman applying… something that pops on screen, rather than just showing a woman
  applying the product". The $90 jar beat and the counter sweep.
- **6 exports**: 3 hooks × (Black Friday ending + evergreen ending).
- Music: the brief says Editor's Choice.

## Specs
- 9:16, 1080×1920, ~2:02-2:10 (367 VO words at 170-180 wpm; never speed the voice up). Meta safe zone: top 14%,
  bottom 35%, sides 6%. Hook title only for the first 5 s, top of the safe zone.
- **Captions (copy ref2)**: mid-screen, 2-4 words, two staggered lines: small white bold sans, then the keyword big.
  Keywords glow: **red** = the industry (ninety-dollar jar, ten-step, six weeks, pouring), **deep green / gold** = our
  side (castor bean, 3,000 years, generations, one ingredient, ten seconds…). Italic serif for the odd emphasis word.
  Captions start at "I'll give you a hint."
- Two looks: **editorial collage** (aged paper, torn white edges, soft shadow, bold italic serif; warm colour for our
  side, black & white for the industry; gentle slide-in/parallax) on H1, H3, papyrus, "for generations", "became an
  industry", "No needles…", end card. **Clean real footage**, warm grade, everywhere else.
- Pace: refs cut every ~1.5 s (ref2 31 cuts/min, main_ref 30); this ad is longer and calmer, aim ~20-25 cuts/min
  with faster cuts in the hook and social proof.
- Source lines: "Source: American Academy of Dermatology" (rows 6 and 8), "Ebers Papyrus, c. 1550 BC" (row 4).

## Shot plan (storyboard frame → where the footage comes from)
| row | VO (start) | storyboard | source |
|---|---|---|---|
| H1 | "What's the oldest anti-aging secret…" | `r01_H1_oldest_secret` | collage: real woman ~60 rolling oil near the eye (**Library: Rolling on, 55+, close-up**) + Met tomb painting cut-out |
| H2 | same VO | `r02_H2_sweep_counter` | **generate** (no Library match likely): woman ~60 sweeps creams into a bin, our bottle stays. White sans title |
| H3 | same VO | `r03_H3_seeds_before_90_creams` | collage: whole castor seeds falling into a palm next to a gold jar (**generate**, seeds whole) |
| all | "…ninety-dollar jar" | `r01b_90_dollar_jar` | **generate once**, used by all 3 hooks + row 15: gold-lidded $90 jar on a marble counter, a hand pushes it away |
| 4 | "This is a castor bean… 3,000 years" | `r04a_papyrus`, `r04b_pressing_oil` | seeds macro (reuse H3), **Ebers Papyrus** (Wikimedia Commons, CC BY-SA 3.0, credit), pressing-oil reenactment (**generate**, tight, hands only) |
| 5 | "for generations, women have rubbed it…" | `r05a_for_generations_collage`, `r05b_lamplight_neck` | **Met tomb painting + alabaster jars** (public domain), lamplight hand on neck (**generate**, no face), vintage vanity photo (archive/stock), woman 55+ rolling at night (**Library**) |
| 6 | "Castor oil is almost 90% ricinoleic acid…" | `r06_mechanism_diagram` (rough) | oil drop on skin (**Library/generate**) + **skin-layer animation** (motion graphics, Frøya-style): oil film, skin plumps, line softens |
| 7 | "anti-aging became an industry…" | `r07_ten_step_collage` | B&W collage: dropper bottles with tags (graphics + stock/generate cut-outs) |
| 8 | "six weeks… ten steps every night" | `r08_six_weeks_mirror` | calendar crossed off + tired woman 55+ at the mirror, light off (**generate**), jars in a drawer |
| 9 | "This is Haven & Spool… rose quartz roller" | `r09_product_reveal` | counter sweep, then **real product** (Products tab photos / Library "Hand holding roll-on"), reveal ~0:40 |
| 10 | "Instead of pouring oil… roll one thin layer…" | `r10a_old_way_pouring`, `r10b_roll_on_lines` | pouring into palm (**Library: Pouring**), rolling under eyes / brows / neck (**Library: Anti-aging, Rolling on, 55+**), nightstand lamp off |
| 11 | "ten seconds… stick with it" | – | nightstand loop + gold calendar (**generate**, reuse the row 8 calendar setup) |
| 12 | "Night one, your skin wakes up soft…" | `r12_night_one_soft` | woman 55+ morning light touching cheek, foundation gliding, eye corner (**Library / generate**) |
| 13 | "your whole face looks younger…" | `r13_text_message_younger` | woman at mirror + phone text "ok what did you change?? you look amazing" (footage + graphic) |
| 14 | "over 43,000 women… 4,000 five-star reviews" | `r14_social_proof` | **3-4 real UGC clips, 1 s each, Library only** (Gabriel: must be real), five gold stars |
| 15 | "costs less than a single jar…" | `r15_lasts_for_months` | our bottle next to the row-1 $90 jar (**generate** with product photos as references, true size) |
| 16 | "No needles. No ten-step routine. No $90 jars." | `r16_no_needles_strips` | B&W collage strips with red X (graphics; capped syringe only, no needle) |
| 17 | "the future of anti-aging isn't more… That's it." | `r17_simpler_one_ingredient` | bottle on cream linen, seeds, oil pool, rose quartz (**Library product shot / generate** with product refs) |
| 18 | CTA (BF / evergreen) | `r18_end_card` | collage end card: bottle cut-out, "Buy 1, Get 1 FREE / 30 nights or your money back / Link below" |

## Order of work
1. **VO first** (sets every timing): AI female, American, 50-60, warm and knowing, 170-180 wpm, real pauses;
   HAY-vin & SPOOL, riss-in-oh-LAY-ik. Two endings. Quote before generating.
2. **Library pass** per row (`vs hyperscale shots`), pick clips; list what's still missing.
3. **Archive**: Ebers Papyrus, Met tomb painting, alabaster jars, vintage vanity photo (`vs fetch`, licences logged).
4. **Generate the gaps** (quote first): $90 jar, H2 sweep, H3 seeds, pressing oil, lamplight neck, calendar/mirror,
   nightstand loop, bottle-vs-jar. Draft cheap (Veo Fast / Seedance Mini), final on Seedance 2.5 or Veo with the
   product photos as references. Check each against the lessons: true product size, reads as real phone footage.
5. **Graphics**: collage system (paper, torn edges, serif titles), mechanism animation, end card, captions.
6. **Edit** body once, swap the first 5 s per hook, 2 endings → 6 exports. QA (`vs ads qa`, frame-by-frame look),
   `vs hyperscale prep`, upload.

## Open questions for Gabriel
- (YouTube reference dropped by the editor: not needed.)
- Music: decided. Original Suno instrumental (`assets/music/457_bed_suno_v1.mp3`, 1:59, no drums, warm/dark), fit to the edit length on a downbeat at about -20 dB under the voice.

## Footage pulled from the Library (assets/broll/, credit "Hyperscale Library")
- Rolling on, women 55+: 2b31275e, 97eb2054, 6d1c337b (forehead), 7c60cde2 · 45-54: 015565e5, 8c625345 · applying 55+: e513d72d
- Pouring into hands: 74c91fd4 (45-54, hands only), f3d839d8 · bottle on counter: 59fd99a8
- Animation: castor bean pressed for oil d31c46b7 (row 4 option), oil on skin model d6147e71 (row 6 option)
