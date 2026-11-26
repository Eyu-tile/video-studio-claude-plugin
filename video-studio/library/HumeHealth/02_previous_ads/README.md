# 02 · Previous Hume ads: what the team actually ships

Source: Frame.io share **f.io/bVz6r02a** ("Created by Cubert General", 200 top folders, 2,246 videos, ~439 GB), crawled 2026-11-12 through the share's own GraphQL API. The Frame.io 1080p transcodes were analysed.

- **166 Hume ad families** analysed (83 Pod / 82 Band / 1 unclear). Each family = one creative, with hook variants (Hook 1–n) and reframes (9:16, 4:5, 1:1, sometimes 16:9 and a `raw` textless copy).
- **24 families (227 files) of a different brand** (GLP-1 injection, `INJ-TZ` / `HC`) were in the same share. They are **excluded** and listed in `EXCLUDED_OTHER_BRAND.md`.
- Master per family = the 9:16 Hook 1 (or the first render). Masters got a full analysis. Hook variants got the first 8–12 s (OCR + transcript); reframes got cuts/size only. Hook-variant coverage is still filling in (see "Status" below).

## Files
| File | What |
|---|---|
| `INDEX.md` | one row per ad: product, duration, shots, average shot, cuts/10 s, wpm, LUFS, spoken hook, HARD compliance flags, link to beat sheet |
| `beat_sheets/*.md` (166) | shot-by-shot table: in–out, duration, cut (+SFX hit), words spoken in the shot, on-screen text (caption / headline / colour), hook-variant table, other versions, full transcript |
| `contact_sheets/*.jpg` (166) | one frame per shot of the master, timestamped |
| `ads.json` | all per-ad data: cuts, shots, pacing, captions (position/size/colours/highlighted words), headlines, audio (BPM, loudness, SFX-on-cut), hook, CTA, compliance flags, hook variants, other versions |
| `HOOKS.md` / `hooks.json` | hook bank: every hook render's first 3 s (spoken + on-screen) and first cut |
| `style_stats.json` | aggregate medians / quartiles: all ads, Pod, Band |
| `COMPLIANCE.md` | red-line wording found in shipped ads, with context |

## The measured house style (medians across 166 masters; p25–p75 in brackets)

| Metric | All | Pod | Band |
|---|---|---|---|
| Duration | **70 s** (49–90) | 71 s | 68 s |
| Shots per ad | 34 (24–46) | | |
| Average shot length | **2.0 s** (1.8–2.4) | 2.06 s | 1.98 s |
| Median shot length | 1.8 s (1.5–2.0) | | |
| Cuts per 10 s | **4.8** (4.0–5.5) | 4.8 | 4.9 |
| First cut | **1.8 s** (1.2–2.8) | 1.7 s | 1.9 s |
| VO speed | **~219 wpm** (198–240) | 217 | 220 |
| Talk ratio (speech/duration) | 0.94: VO is wall-to-wall, almost no pauses | | |
| Cuts landing on a word start (±0.12 s) | **80 %** (71–87) | 78 % | 82 % |
| Cuts falling between words | 65 % (55–74) | | |
| Cuts with an audible transient (whoosh/hit/pop) | **57 %** (45–70) | 59 % | 57 % |
| Integrated loudness | **−18.9 LUFS** (−20.1 to −16.1) | −19.0 | −18.8 |
| True peak | −1.8 dBTP (−3.4 to **0.0**): a quarter of ads hit 0 dBTP | | |
| Loudness range | 3.2 LU (very compressed) | | |
| Music tempo (beat tracker) | ~123 BPM (112–129) | | |
| Ads with a top headline/banner | **93 %** | 96 % | 92 % |
| Ads with coloured caption highlights | **95 %** | | |

Caption measurements (OCR):
- Captions sit at **~67 % of frame height** (64–72 %), the lower-middle, above the platform UI.
- Line height is **~3 % of frame height** (~58 px on 1920).
- Cards are **1–3 words** (median reads as 1 word per OCR line; cards change faster than the 0.5–1 s sampling, so card duration is below what was measured).
- Highlight colours counted on caption cards: red 795 · blue 634 · green 489 · yellow 166. Red = problem/pain words, green = proof/positive, blue = brand/feature.
- Captions crossing a cut: median 2 per ad. This is the rule most often broken (SOP: caption starts and ends on the same clip).

## Patterns seen in the ads (from beat sheets + contact sheets)
1. **Structure:** hook headline (frame 1) → personal problem → "until I scanned myself using this" product reveal → app-screen proof matching each spoken metric → mechanism ("step on, grab the handles, 60 seconds, 45 metrics") → result / transformation → CTA (sale / "link below" / HumeHealth.com pill).
2. **Two dominant formats.** (a) Creator A-roll (selfie talking head) interleaved with cutaways every 1.5–2 s, with a persistent **top banner headline in a coloured box** (often with an emoji) for the first ~7–10 s. (b) Wall-to-wall VO over b-roll and app screen recordings, with word-by-word captions.
3. **Captions:** short cards on **white pills with black text**, or white bold text with outline for influencer cuts; the key word flips to a **red or green pill**.
4. **Proof shots:** a hand holding the phone with the Hume app (body map, BMR, visceral fat index, muscle by segment), the black glass Pod on a bathroom floor, feet on the plates + hands on the handle bar, the 3D blue body render, the Band on the wrist / in the hand, the retail box.
5. **Pacing:** the first cut lands at ~1.8 s; a cut every ~2 s for the whole ad; 4 out of 5 cuts land on a word start; more than half carry a whoosh/hit.
6. **Audio:** VO-dominant mix at about −19 LUFS integrated with a music bed ~120 BPM; heavily compressed (LRA ≈ 3). Because the VO is continuous, the bed level under the voice could not be isolated from the mix.
7. **CTA language:** sale/discount (22 ads mention "% off", 14 "sale"), "tap / click / link below", "get yours", HumeHealth.com.

## Compliance warning
**100 of 166 shipped ads contain at least one red-line pattern** (regex, so some false positives; see `COMPLIANCE.md`):
- DEXA equivalence (32 ads, e.g. "98 % DEXA accuracy… basically identical")
- disease named (56)
- early-detection framing (16)
- heart attack / stroke (11)
- medical/clinical ("medical-grade", "hospital machines", 9)
- diagnosis/treatment (5)

The current Claims Bank forbids most of these. Copy the **editing** style, not the claims.

## Status
- Masters: complete (cuts, transcripts, OCR, audio, beat sheets).
- Hook variants: ~600 of 628 cut-analysed; transcripts/OCR of their first seconds are still running. `HOOKS.md` / `hooks.json` fill in as they finish (re-run of the builder).
- Reframes / textless copies: pending (low value, same edit re-cropped).
- Not done: isolating the music bed / SFX stems (would need source separation).
