# 03 — Winning ads (Hume Health)

Source: the client's master Drive, `06 — Winning Creative Collections`:
- `All Time Best Performing Ads`, monthly folders from 2024 to 2026, plus `2026/All Time Best Performing Ads (as of 04/2026)`
- `Hume x Meta Ads Evergreen Video Winners` (Hume Band 2.0, Hume Pod)

Analysed on 2026-11-12 with the same pipeline as `../02_previous_ads`: shots cut at native fps, 2 fps OCR, Whisper word timings, loudness, and SFX on cuts.
- **54 unique winning videos:** 27 Pod, 11 Band, and the rest are 2024 "Hume / HH" ads.
- **8 static winners:** in `statics/`.
- **8 Evergreen videos blocked:** Google's download quota stopped them. They're listed in INDEX.md and will be retried.

**Read this first:** the client's Drive says *"winner status does not establish current approval."* 11 of 54 winning videos and most of the statics contain wording that breaks today's Claims Bank red lines (see below). Copy the **structure, pacing and hook pattern**, never the claim.

## Files
| File | What it holds |
|---|---|
| `INDEX.md` | One row per winner: length, shots, pacing, spoken hook, HARD compliance flags, link to its beat sheet |
| `beat_sheets/*.md` | Shot-by-shot: in/out, transition, SFX, spoken words, on-screen text, highlights, headlines |
| `contact_sheets/*.jpg` | One frame per shot |
| `hooks.json` | Spoken words at 0–3 s and 0–8 s, and on-screen text at 0–3 s, per winner |
| `ads.json` / `style_stats.json` | Full per-ad data and aggregates (same schema as 02) |
| `statics/` | The 8 winning static images |

## What the winners do differently (measured: 54 winners vs 166 previous ads)

| Measure (median) | Winners | Previous ads | Takeaway |
|---|---|---|---|
| Length | **40 s** (Pod 43 s) | 70 s (Pod 71 s) | Winners are much shorter. Aim for 30–45 s for Pod, 45–65 s for Band. |
| Shots | 20 | 34 | |
| Average shot | **1.71 s** | 2.00 s | Cut faster. |
| Median shot | 1.49 s | 1.77 s | |
| Cuts per 10 s | **5.4** | 4.8 | |
| First cut | **1.4 s** | 1.8 s | Change the picture within 1.5 s. |
| Cuts in speech gaps | **73 %** | 65 % | Cut on the breath between phrases, not mid-word. |
| Talk ratio | 0.88 | 0.94 | Winners leave a little air: a beat with only music or SFX. |
| Words per minute | 219 (Pod 226, Band 200) | 218 | Pod VO is fast. Band winners are slower and calmer. |
| Loudness | **−14.5 LUFS** | −18.9 LUFS | Winners are delivered at platform loudness. Master to −14 LUFS. |
| Caption height in frame | **0.60** | 0.67 | Captions sit higher, near the middle, clear of the UI. |
| Words per caption card | 1 | 1 | One word per card, same as before. |
| On-screen headline | 100 % | 93 % | Every winner has a headline or title card. |
| SFX on cuts | 53 % | 57 % | About half of cuts get a hit; not every cut. |
| Ads with a HARD red-line flag | 20 % | 60 % | Winners are cleaner, but not clean. |

Colour highlights appear in 89 % of winners. The main colours are blue (Hume blue), then red, then green (health-score "good" states).

## Hook patterns that win (spoken first 3 s)
- **Listicle / series hook:** "Random things I wish I knew about sooner. Part 13." / "Things TikTok made me buy part 45."
- **Reasons:** "Three reasons why this body pod keeps selling out." / "Three reasons why this was rated as the most sought-after…"
- **Reframe the scale:** "When it comes to your health and fitness goals, your weight is the worst measure." / "I don't use the scale to measure my progress anymore." / "Did you know you could be gaining weight but still getting healthier?"
- **Personal pain, then relief:** "Getting older isn't bad, but no one warned me how drained I'd feel." / "Every morning that number went up and I blamed myself." / "I was a college athlete. Now I have the body of a 60-year…"
- **Reaction / unboxing:** "Look at this. Oh!" / "My body pod just arrived in the mail today." / "The body pod. It's insane."
- **Curiosity / "did you know":** "A lot of people don't know this, but you can actually track…" / "What is this Hume longevity band that everyone is wearing?"
- **Gift / seasonal:** "This is the gift everyone will want under the tree this year." / "This is the year you don't just survive, you thrive."
- **Hard result:** "40 pounds of fat loss, 16 pounds of muscle gain." / "If your goal is to hit 15 % body fat, stop guessing."

## Do NOT copy (found inside winners)
- "We had a customer who **caught their heart attack** two weeks before it…": heart-event prediction (red line).
- "**chronic illness detection** … catching potential issues early" (The Secret to Living Longer): early-detection / disease framing.
- "This is **98 % as accurate as an InBody scan**" and the statics "**DEXA Scan vs Body Pod**", "**98 % DEXA accurate**": DEXA/clinical equivalence.
- Static "We've seen **patients** … losing weight **7x faster**" with "Dr … General Practitioner": medical endorsement plus an unsupported result.
- Static "**155 lbs in 3 weeks**": implausible result claim.
- "Six in ten Americans have **chronic disease**": disease framing.
- Offer codes and prices (NEW20, DAD50, BBS15, $189/$229, 50 % OFF) are time-bound. Use only the brief's current offer.

## Static patterns (8 winners)
Pod hero (black glass, handle bar, phone showing the body-composition figure) on light blue or gradient backgrounds. Big headline in Red Hat Display, a large **50 % OFF** block, a code pill, and an "HSA/FSA eligible" pill. Seasonal variants: Father's Day (orange/yellow, "Use code DAD50") and "Level Up 2025". The ✕ BodyPod / HumeHealth logo sits top-left or bottom-left.
