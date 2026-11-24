# SoFyre #004 (+ sister #002): shot-by-shot analysis for RootOut Set 5

Watched 24 Nov 2026: every cut detected (ffmpeg scdet), one frame per shot looked at by eye (80 shots for #004, 88 for #002),
voice transcribed word by word (faster-whisper small.en), audio levels measured. Per-shot data: `shots.json` here and
`../sofyre-002/shots.json` (start, end, length, words spoken over the shot; kept local, git-ignored). Videos and frames stay local (git-ignored).

## 1. The numbers
| | #004 (main swipe) | #002 (sister cut) | **Set 5 brief (H1)** |
|---|---|---|---|
| length | 133.7 s | 111.4 s | 141.5 s |
| shots | 80 | 88 | — |
| average shot | **1.67 s** (0.5–4.1) | **1.27 s** (0.4–3.8) | brief writes ~25 visual beats → must be cut to ~80 shots |
| words / speech rate | 506 w · **3.8 w/s** | 324 w · 2.9 w/s | 345 w · 2.5 w/s (her low bedtime voice) |
| pauses | none over 0.4 s | none over 0.7 s | keep it wall-to-wall: no dead air between lines |
| on-camera presenter | **none** (faceless VO) | none | mom on camera (diary) |
| music | a bed ~9 dB under the voice (gap level −24 dBFS vs speech −15) | same | soft bed ~9 dB under her voice |
| master loudness | −12.4 LUFS integrated (loud) | — | deliver −14 LUFS, TP −2 (Set 1 finish) |

## 2. Structure (#004), by time
| t (s) | block | what the viewer sees | device |
|---|---|---|---|
| 0–8 | **Hook + promise** | pouch lands on a granite counter with a vapour puff (0 s, product in frame 1) → man at the stove ignores it → vapour in the wall → x-ray mouse in vapour | 2-colour top title (red / brand green) for 8 s only; "One SoFyre pouch" caption with the brand word in brand green |
| 8–17.6 | **It spreads** ("every crack, every gap, every cavity") | vapour rolls across real kitchens, floors, into open walls with pink insulation; 0.6–0.7 s shots on the list words | one shot per list item, list words get the shortest shots |
| 17.6–49.8 | **Hour 1 → hour 12, oil by oil** | ingredient shot **stacked over** the mechanism (split screen: castor-oil pour / wall vapour; cedar cones / x-ray mouse); then the "no trap · no spray · no exterminator" triple | split screen = ingredient on top, what it does below · **failed fixes shown desaturated grey with a red X** |
| 49.8 | **stamp "BY HOUR 24"** | 1.3 s: the *next* shot, heavily blurred, pulling into focus, bold white stamp in the middle | chapter card made from the next shot, not a separate graphic |
| 51–70.5 | hour 24, peppermint → **first visible change** | mint leaves over an x-ray mouse with a green scent wisp; mice on real floors; **red X over droppings on the counter** ("no droppings on the counter in the morning") | payoff = an everyday thing the buyer would notice |
| 70.5 / 83.4 | stamps "BY HOUR 48", "BY HOUR 72" | same blurred-pull stamp | each stamp opens a 12–13 s chapter |
| 71–97.7 | the exit | mice leave through a back door into a garden; "just one pouch" held to the lens; "a pouch in every room" | product returns in hand at the end of the mechanism |
| **97.7–111.8** | **DAY 3 / 7 / 10 / 14 run** | **one shared blurred backdrop** (hand placing the pouch) under each DAY stamp, 0.6–0.7 s each, alternating with a 1.5–2 s life-back shot: clean kitchen island · blinds at 3 am · man opening a drawer "out of habit" · kid's hand with a cereal box (face blurred) · teen at a shelf from behind | fastest rhythm in the ad: stamp, payoff, stamp, payoff |
| 109.6–111.8 | "Not from poison. From the mice actually leaving." | grey + red X on poison bait; door open to the garden | the red X again |
| 111.8–123.9 | **What it is** | 4-up split of hands placing pouches in cabinets/drawers · ingredient roll call **0.5–0.8 s per word** (castor bottle, pine cone, mint, cinnamon in a palm) · finger taps the ingredient panel on the pack · pouch with vapour "for 90" | ingredient roll call at word speed |
| 123.9–133.7 | **Offer + close** | pack on a windowsill "59% off" → **real PDP screenshot**, blurred-in, "Buy 2 Get 1 FREE" in a **yellow highlight**, **a hand cursor clicks the tier** → pack on a table with a **green box "30-day money-back guarantee"** → pack held in hand, "constantly", "if the link below", "this batch" | PDP proof + cursor click; caption colour changes for the offer words |

## 3. Visual grammar to borrow (in our look, never their frames)
1. **Product in the first frame** and again at every turn (mechanism end, recap, close). Ours: the real RootOut bottle.
2. **Chapter stamps from a blurred frame.** "BY HOUR 24" / "DAY 3" sit on the next shot blurred and pulling into focus,
   ~0.7–1.3 s. → Our **NIGHT 1 / 3 / 7 / 10 / 14**: the next bedroom shot blurred, crayon-orange handwritten stamp
   (instead of their white Proxima). The DAY run reuses one backdrop; our nights reuse the calendar by the bed.
3. **Split screen for "ingredient + what it does".** → Top: the real plant (lemon, tea tree, pokeweed, white cedar from the
   Set 5 stock); bottom: our skin side cut doing that plant's job. Matches lines in beat 3 and beat 5.
4. **Desaturated + red X for every fix the product replaces.** → "No freezing, no acid, no blister" (beat 8): grey shots of
   a freeze can, an acid bottle, a blister plaster, each with a red X. Also H2/H3's "don't book the freeze".
5. **Payoff = an ordinary moment the parent notices**, never the pest itself. Theirs: clean counter, quiet 3 am, cereal box.
   Ours already is: barefoot at the pool, the drive home, "he wants to do the brush himself", the +14 on the calendar.
6. **List words get the shortest shots** (0.5–0.7 s): our "Two light rubs… Brush the oil on. A clear dot on top." and
   "No freezing, no acid, no blister" should cut on each phrase.
7. **Offer proof = a real PDP screenshot** with a yellow highlight and a cursor click on the bundle tier, then the guarantee
   in a coloured box. → Our captured `ads/set5_build/web/pdp_1_Buy_2_Get_1_FREE.png` (RootOut's own tier list), tap on
   "90 Nights, Buy 2 Get 1 FREE"; guarantee from `pdp_2_…`.
8. **Captions on every shot**, 1–3 words, black text in a white rounded box, brand word in brand colour, words change
   with the voice. Ours: RootOut navy/blue (`#0B2A5B` / `#1763B8`), offer words in CTA orange `#E04E18`.
9. **Title on top for the hook only** (0–8 s), two colours. Ours: "14 nights at bedtime" with "14 nights" in blue.
10. **Real footage + light VFX over AI:** most of #004 is real home footage with added vapour; the AI x-ray animals are
    1–2 s inserts. → Real stock where it exists (dandelion root, pool, lamp, calendar, plants, wart photo), AI for the
    bedroom and the foot, our 3D skin side cut for the "inside view".

## 4. What #002 adds
- Typewriter stamps ("Within the first f…" typed on), a **4-up grid** for "the 4 oils", glowing **blue grid / shield**
  for coverage, a cost anchor ("No $2,000 rewiring bill"), a count claim ("over 60,000"), and a toddler near the pouch for
  "safe around family". Pace 1.27 s. Useful for H4 (winter break) as an alternative stamp style; skip the count claim
  (we have no number) and the shield.

## 5. Where the brief and the swipe disagree (brief wins; how we bridge it)
| | swipe | Set 5 brief | decision |
|---|---|---|---|
| presenter | faceless VO | mom on camera, phone on the nightstand | Mom on camera only on each night's opener and a few lines (~30% of runtime); everything else is inserts under her voice, so the cut rate can match the swipe |
| pace | 1.3–1.7 s shots | ~25 described beats | Split each beat into 2–5 shots → target **~75 shots, ~1.9 s average** (slower than the swipe because she talks slower) |
| captions | every shot | "No captions or name tags (On screen = hook + end card only)" | **Ask the client.** Their Set 1 feedback asked for captions throughout, which contradicts this line; captions are what the swipe does |
| speech rate | 3.8 w/s, no pauses | 2.5 w/s, low voice | Keep her low voice (the brief's "she talks low because he's falling asleep") but tight: no gaps over 0.4 s |
| hour stamps | hour 1 / 12 / 24 / 48 / 72 + day 3 / 7 / 10 / 14 | nights 1 / 3 / 7 / 10 / 14 | NIGHT stamps as above. Inside night 1, the side-cut clock (9 pm → 7 am, in the brief) carries the "hour by hour" idea; no extra stamps added |
| claims | heavy (nervous system, heart rate) | the four-plant jobs, 8x†, kids' formula, pediatricians | Nothing borrowed from their claims; ours carry the Round 1 claim checks |

## 6. Do not copy
Their brand, pack, vapour effect, x-ray animals, wall-cavity footage, white Proxima stamps, numbers (59%, 60,000, 30-day),
music. Kid faces (their cereal shot shows a child, face only blurred): ours never show a face.
