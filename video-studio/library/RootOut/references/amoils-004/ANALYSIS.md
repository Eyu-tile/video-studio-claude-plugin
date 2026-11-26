# Amoils H-Warts #004 (+ UK cut #039): shot-by-shot analysis for RootOut Set 14

Watched 26 Nov 2026 from the swipe site's own file (sha256 361ce86c…, matches `breakdown.json`): cuts detected
(ffmpeg scene > 0.28), one frame per shot and one frame per second looked at by eye, voice transcribed word by word,
levels measured. Per-shot data (start, length, words over the shot) in `projects/rootout-set14/ref/amoils-004.shots.json`
(local, git-ignored with the video and frames).

## 1. The numbers
| | Amoils #004 | UK #039 | **Set 14 H1 v1 preview** |
|---|---|---|---|
| length | **101.7 s** | 101.0 s | 126.5 s (brief clock 117.5 s) |
| shots | 38 hard cuts (+ ~10 white-flash / blur-whip transitions) | 37 | 45 |
| average shot | **2.7 s** (0.2–6.5) | 2.7 s | 2.8 s (1.5–4.4) |
| words · pace | 353 w · **3.5 w/s** | 350 w · 3.5 w/s | 307 w · **2.8 w/s** |
| pauses | ~0.4–0.6 s between sentences, no dead air | same | 0.22–0.35 s |
| narrator | off camera, calm, low voice (~126 Hz median) | same | off camera, US woman (~157 Hz) |
| music | soft bed ~9 dB under the voice (speech −15 dBFS, gaps −24) | same | same balance (speech −13.5, gaps −24.5) ✓ |
| end card | **none**: ends on a woman holding the bottle, "click below" | none | end card (script asks for one) |

## 2. Structure (#004), by time
| t (s) | block | what the viewer sees | device |
|---|---|---|---|
| 0–2.4 | **Question hook** "Why won't over-the-counter treatments work on plantar warts?" | freeze pen sprays a real wart on a toe, frost cloud | caption box **at the top** over the action; the failed fix is the first frame |
| 2.4–8.8 | "most treatments miss what's happening beneath the surface" | white flash → 2D medical illustration: a line cuts down through skin, the wart's **branching roots** spread under it | the "beneath" picture lands in the first 5 s |
| 8.8–15.2 | **Authority + curiosity** "over a decade helping people… shocked why nothing else worked" | **man in a lab coat holds the bottle to the lens with a red arrow (0:07)** → mom + son with the bottle → real wart soles → woman shocked at her phone → **red X over boxes of freeze kits and acid pads** | product in hand at 7 s; competitor shelf crossed out |
| 15.2–23.8 | **The hidden layer** "grow deep under hardened skin… acts like armor" | 2D cross-section with a yellow arrow; **3D macro of white cream sitting on a rough wart** (the armor shot); red veined wart under skin | one picture per sentence; "armor" = cream that can't get in |
| 23.8–33.4 | **Why burn / freeze / scrape fail** "…come right back, sometimes thicker" | cautery pen on a toe, 3D spheres under a peeling layer, **hands with warts + curved red arrow** (spreading), a wart going crusty | red arrows for "comes back / spreads" |
| 33.4–49.6 | **A different path** (third-party lab, plant formula, "layer by layer") | white flash → lab coats, **microscope with a "Third Party Tested" badge**, sprouts in test tubes, gloved hands with plants, a sole being softened, 3D skin cells renewing | credibility b-roll, all stock |
| 49.6–55.9 | **Named** "It's called H-Warts Formula… time-tested botanicals" | real mom on a sofa holds the bottle, smiling; dropper over leaves; hand in a plant patch | product named at **49 s** (shown at 7 s) |
| 55.9–69 | **"Here's what happens when you apply it"** soften → dry → shrink → flake → new skin | **cotton swab applies oil to a real wart between toes** (6.5 s, one shot), mom applies to a toddler's finger, a hand with a fading wart | the step-by-step is shown on **real skin**, not animation |
| 69–85 | **Gentle + routine + timeline** "without acids, freezing or pain… twice a day… a few weeks… flatten and fade" | smiling kids holding the bottle (faces shown), red X-style cut from a cautery pen, bottle in a hand, **real soles: crusty → flatter → clean soles in daylight** | before → after told with three real soles |
| 85–92.4 | **Offer** fast shipping + 90-day guarantee | parcel handed over, **scrolling screenshot of their real guarantee page (90 seal, "Third Party Tested", "1M sold")**, doctor thumbs-up | real page proof |
| 92.4–101.7 | **CTA to the same avatar** "If you've been dealing with… click below" | the worst real soles again, then a woman selfie with the bottle at her chin | ends on a person + bottle, no end card |

## 3. Visual grammar
1. **Real-looking skin carries the ad.** About 40 % of the running time is real (or real-looking) close-ups of warts, soles and fingers,
   mostly gross and specific. The animation is mainly **2D medical illustration**, only 3–4 shots are 3D (cream-on-armor, spheres).
2. **Failed fix in the first frame** (freeze pen on a wart), question caption on top of it.
3. **Product in a person's hand early** (0:07, red arrow) and again at every turn (named 0:50, routine 1:15, close 1:25 / 1:37).
4. **Red graphics do the arguing:** a red X over the store wart boxes, red arrows for "comes back / spreads", a yellow arrow
   pointing at the root in the cross-section.
5. **White flash / blur-whip** at each chapter change (0:02, 0:20, 0:33, 0:49, 0:54, 1:02, 1:13, 1:26, 1:32, 1:36).
6. **Captions:** short phrase in a white rounded box, black text, 2 lines, placed top or middle to stay off the action.
7. **"Here's what happens when you apply it"** is a short story of stages (soften, dry, shrink, flake, new skin) on real skin.
8. **No end card**: the last frame is a person holding the bottle.

## 4. Set 14 v1 against the swipe
| | swipe | our v1 | verdict |
|---|---|---|---|
| question hook over the failed fix in frame 1 | freeze pen on a toe | store liquid on a kid's heel, hook title on top | ✓ matches |
| "beneath" picture in the first seconds | 2D roots at 0:03 | clinic freeze 0:05, 3D wart + root at 0:08 | ✓ close |
| product shown early | in hand at 0:07 | first at 0:25 ("RootOut takes a different path") | ✗ later |
| hidden layer / armor | cream on a rough wart | thick dead-skin layers + cream (k24), tape on top (D1) | ✓ same idea |
| failed fixes | red X over store boxes, red arrows | D2 frost + blade on the top only, the dandelion | ~ no red X / arrows |
| mechanism | ~16 s of lab + plants b-roll | 35 s of plant-by-plant 3D (script's UMS v3) | longer by design |
| "what happens when you apply it" | real swab on a real wart, real soles going smooth | file / brush / dot on real-looking kid feet; flaking = stand-in 3D (k25 a72f + b0d3) | ~ the flake beat is weaker |
| real skin share | ~40 % of the time | ~25 % (3D/illustration ~40 %) | ~ |
| pace | 3.5 w/s, 102 s | 2.8 w/s, 126 s | ✗ slow |
| transitions | white flash at each chapter | hard cuts only | ~ |
| captions | phrase boxes | word-by-word bold, active word highlighted (house L5) | keep ours |
| kids | faces shown | never (L10) | keep ours |
| end | person + bottle, no card | end card | script asks for the card |

## 5. What to change for v2 (no new credits)
1. **Pace:** narrator to ~1.15x (pitch kept) and pauses to ~0.25 s → ≈ 110 s, 3.2 w/s.
2. **Red X on the failed fixes:** over the freeze can / acid pads / tape when the narrator says "No acid, no freezing"
   (P1 lineup) and over the shelf on "Tried the store stuff already?" (code, no brands shown).
3. **Red / yellow arrows:** a yellow arrow onto the root on "The root stays under the hard skin"; a red arrow on the tape
   shot ("Store stuff stops there").
4. **White flash** at the four chapter turns: "here's why", "RootOut takes a different path", "Here's what you do at
   bedtime", "Tried the store stuff already?".
5. **More real skin:** swap a 3D shot or two for real-looking close-ups already on the account (S19 b21 heel spot,
   S4 B10 three warts, S19 b60 wart back), e.g. on "On a foot," and "so it grows back".
6. **Product earlier:** the brief's line order puts RootOut at 0:25; a bottle on "here's why" would break L3 (the shot must
   show what is said), so leave it unless the client wants a product flash in the bridge.
7. **Flaking beat:** the swipe shows it on real skin. Ours is a 3D stand-in because the account ran out of credits;
   a real-looking flaking sole (~35 credits) would match the swipe better.

## Do not copy
Their brand, bottle, lab/scientist stock, "Third Party Tested" badge, "over a decade" claim, their guarantee page,
competitor box art, kid faces, and the cotton-swab routine (ours is file · brush · dot).
