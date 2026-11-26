# Hume Health: editing rules (client-confirmed, must follow)

Every review round and its lessons are logged per project in `comments/` (start with `comments/README.md`, the lessons checklist). These rules come from the client's review rounds on the 2026-11 ads (Band Xmas, Pod Visceral Fat Ad2453, Pod Muscle Recomp / Healthier Mindset). **Apply them to every new Hume ad, without being asked.** If a brief conflicts with a rule, follow the brief and say so in the delivery note.

---

## RULE 1 (MUST): every spoken metric gets matching app footage
Whenever the VO, the creator or a caption names a metric, show that metric's screen from the client's app recordings. Each one gets a coloured mark around its row (colour chosen per ad, see 3a). Don't let a talking head, product shot or generic b-roll play over a metric word.

Metrics this covers (Pod and Band): body fat %, metabolic age, BMR / basal metabolic rate / metabolic rate, visceral fat, body water / hydration %, skeletal muscle mass / muscle mass, lean mass, bone mass, protein, BMI, weight trend, goals, segmental (arms/legs/trunk), health score, biological age, metabolic capacity / momentum, sleep, recovery, strain, HRV, resting heart rate.

How to do it:
1. **Source:** use the **latest** real Hume app screen recordings only (the client's newest set first; older recordings show an outdated app). Never use old phone/app b-roll when a newer recording exists, from the client's Drive `01 — Brand & Product Library / App Recordings` (verified list below). Never mock up or type a fake app screen.
2. **Row on screen:** the metric's row must be fully readable: label and value. Don't use phone-in-hand shots where the text is too small to read.
3. **Mark (motion, not a still):** app recordings are scrolling videos, so use them that way. Play the real recording scrolling until the metric row arrives, then hold on it while a rounded box in the ad's mark colour (3a) fades in around the row (label + value), with a slow push-in on the hold. Never show a frozen screenshot for the whole shot. For grid tiles (e.g. Age | Metabolic Age | Height), box only the named tile. Tool: `tools/scroll_card.py`.
4. **Framing:** full-width 9:16 crop with the row at about 35–40 % of the height, so it stays above the captions (about 55–62 %).
5. **Timing:** the screen starts about 0.35 s before the metric word and stays until the next metric or the end of the sentence. Rapid lists can go below 2 s per screen, because each screen must still follow the words. Otherwise a metric screen runs 2–3 s.
6. **Variety:** each metric uses a different recording or a different screen. Don't show the same screen twice in one ad.
3a. **Mark colour, one per ad (client, 2026-11-20).** Don't make every ad's marks red. Pick ONE colour per ad from this palette, all easy on the eye over the dark app screens, and use it for every metric mark in that ad (all hooks, all sizes):
   - Red `#FF4B4B` · Green `#3DDC84` · Yellow `#FFD23F` · White `#FFFFFF`
   Rotate so consecutive ads differ: check the last delivered ad's colour in `comments/` and pick another. Avoid a colour that matches the row it marks (e.g. yellow around an amber "Elevated" value, green around a green "Optimal" badge): take the next one. Stroke 9 px, radius 26 px, same fade-in and push-in as before. Write the choice at the top of the project's `comments/<project>.md` ("Style: mark = Green, captions = B").
7. **Product match:** Pod metrics use Pod (Body) screens; Band metrics use Band screens.
7b. **Hidden metrics (Straps AD641 r2):** when the client asks to blur or hide a metric (e.g. Blood Pressure numbers), blur it on every app screen in the ad where it appears, not only at the flagged timecode. Blur the reading, the date line and the chart's axis numbers frame by frame (`tools/st_bpblur.py`, OCR-anchored), keep the label, and check every frame where the card is on screen.
8. **Captions:** pop the metric word in Hume blue (#1882FF), and use short 1–2-word cards while the metric list runs.

### Verified metric footage (clean, full-screen, readable)
| Metric | Drive file (App Recordings) | Drive id | Time | Notes |
|---|---|---|---|---|
| Body fat % | `2025/screen-20250628-152345.mp4` | 19Pt38wXN1QWw3jbbzqtc1iD4U9hGaGm4 | 16.0–20.0 s (still) | "Body Composition Hub" screen: Metabolic Age 31, Skeletal Muscle 110.4, Body Fat 22.5 % |
| Metabolic age (tile) | `Old/screen-20250628-152518.mp4` | 1q7gKQBT7h71_BwCVbaQ7EbT3DVXH80BK | 34.0–36.0 s (still) | Age / Metabolic Age 31 / Height tiles; box only the middle tile |
| Metabolic age (animation) | `Hume Band Animations/metabolic age 1.mov` | 1dw13fvTevS8WPKq-Id1X5Kq0prG4rwk8 | 0–4 s | Counter animation; the client removed it once. Prefer a real screen |
| BMR (2001 cal) | `Old/screen-20250628-152518.mp4` | 1q7gKQBT7h71_BwCVbaQ7EbT3DVXH80BK | 22.0–22.5 s | Basal Metabolic Rate row high on screen |
| BMR / metabolic rate (1277 cal) | `2025/Body Stats.mp4` | 10AWR-Gs9n9Gh-sldm3hxyP3E54Uiy4cP | 13.8 s | Different account from the 2001 one: use when two BMR shots are needed |
| BMR (2001 cal) | `2025/screen-20250628-152345.mp4` | 19Pt38wXN1QWw3jbbzqtc1iD4U9hGaGm4 | 133.5–139.0 s (still) | Same values as 152518; don't pair with it |
| Visceral fat | copy of `screen-20250628-152518.mp4` in UGC/Matt S Broll | 1saT_Gq06xsrXtYPhxUlYDMD9O2xTSMPd | 14.5–15.0 s | Visceral Fat Index 10 Standard, row at ~31 % |
| Body water % | `Old/screen-20250628-152518.mp4` | 1q7gKQBT7h71_BwCVbaQ7EbT3DVXH80BK | 18.0–19.0 s | Body Water Percentage 57.1 % |
| Body water % (56.9 %) | `2025/Body Stats.mp4` | 10AWR-Gs9n9Gh-sldm3hxyP3E54Uiy4cP | 11.7 s | Second account |
| Skeletal muscle mass | `2025/Body Stats.mp4` | 10AWR-Gs9n9Gh-sldm3hxyP3E54Uiy4cP | 9.8 s | 52.4 lbs Standard |
| Skeletal muscle mass | `Old/screen-20250628-152518.mp4` | 1q7gKQBT7h71_BwCVbaQ7EbT3DVXH80BK | 11.5–17.0 s (scrolls) | 110.4 lbs High |
| Goals | `Old/screen-20250628-152518.mp4` | 1q7gKQBT7h71_BwCVbaQ7EbT3DVXH80BK | 55.0–62.5 s (still) | Goals screen |
| Weigh-in tips / progress | `2025/screen-20250628-152345.mp4` | 19Pt38wXN1QWw3jbbzqtc1iD4U9hGaGm4 | 8.5–15.0 s | Tutorial cards, **not** the "optimal weigh-in time" feature (no footage of that feature exists yet) |
| Segmental / muscle map | `Old/screen-20250628-152518.mp4` | 1q7gKQBT7h71_BwCVbaQ7EbT3DVXH80BK | 40.0–43.5 s (still) | Body map with arms/legs/trunk |

Avoid: `Womenshowingmetrics*`, `Womenscrollingshowingmetrics`, `Copy of 08..MOV` and `Muscle_Fat metrics .mov` (hand-held phone, text too small or a creator's face). Find more with the app-screen index method: OCR every second of the App Recordings, then pick still windows where the metric row holds steady for 2 s or more.

---

## Other client rules (from review rounds)
**Shots and b-roll**
- **Product fully in frame (STRICT).** Whenever a product shot is on screen (Hume Pod, Hume Band, or a product we compare against, such as an InBody), the whole product is visible, edge to edge: nothing cropped by the frame, the reframe for another aspect ratio (4:5, 1:1, 16:9), a push-in, a graphic or a caption. Check every product shot in every size you deliver, at its first and last frame.
  - If the product is clipped in the source itself, cut a different in-point or use another clip. Never ship a partly visible product.
  - When reframing a 9:16 shot to 4:5 or 1:1, set the crop to keep the whole product; frame the person's face out of shot before cutting the product.
  - A push-in must stop before the product touches the frame edge (shorten it, slow the clip, or drop the push-in).
  - CTA cards, headlines and captions never sit on top of the product; move the shot's framing or the graphic.
  - A product that is only partly visible at a frame edge in a talking shot counts as cut off: frame it fully or keep it fully out of frame.
- **Pod scan pose (STRICT): barefoot, arms straight.** Every person on the Pod is barefoot (no socks, no shoes) and holds the handles with straight arms (down or out in front), never bent at the elbows. Check the feet and elbows of every Pod shot, first to last frame; end a shot before the person bends their arms. (DEXA v6 → v7 client notes; Pod Xmas "bent arms".)
  - **Choose clips by the hold pose (STRICT).** When picking a Pod clip, pick a person whose arms stay straight while they stretch the handle cord out and hold it: arms straight down or straight out in front, elbows locked. Skip any clip where the person holds the handle at chest or waist height with bent elbows, however good the rest of it is. Look at the hold, not only the first frame. (DEXA v8 → v9: Hook 2 woman held the handle with bent elbows; replaced by a creator holding it with arms straight out.)
  - The only bend allowed is the brief lift of the handle off the Pod; keep it under ~0.3 s on screen (speed-ramp it in the same continuous shot, don't jump-cut).
- **Product use starts at the action (STRICT).** When someone uses our product on screen, the shot starts at the moment they use it (stepping onto the Pod, gripping the handle, putting the Band on, a reading appearing), not on something else first (walking in, fiddling with a phone, setting up, looking around). Trim the in-point to the start of the use and keep the action going for the whole shot. If the clip has no clean start of use that fits the slot, use another clip.
- **Every b-roll is unique (STRICT).** No piece of b-roll footage appears twice in one ad: not the same clip, not the same source file at another in-point, and not the same footage saved under another name (b-roll copied between projects and Drive folders often is). This covers product shots, lifestyle shots and app/metric shots (each metric shot is a different recording or a different screen, Rule 1). The creator's own A-roll is not b-roll.
  - Judge by the footage, not the file name. Before delivery, run `tools/broll_unique.py EDL.json` on every hook version and size: it flags shots from the same source file (Drive id in the clip's `.json` sidecar) and shots that look the same (frame fingerprints compared pairwise). Every flag must be fixed by swapping in different footage, then run it again until it is clean.
  - When choosing a replacement, check it against every shot already in the cut, not only the one it replaces.
- **Every hook version has its own hook shots (STRICT).** The b-roll inside a hook (before the body starts) never appears in another hook version of the same ad: H1, H2, H3… each open on different footage of the person, judged by footage, not file name. A hook may take a clip the body uses, as long as that hook's body then uses a different clip there. Delivery check: list the hook shots of every version side by side and confirm no overlap, then run `tools/broll_unique.py` on each version. (Fit But Dying v3 → v4.)
- No shot longer than 3.0 s, and no shot shorter than 0.7 s. Short slivers read as glitches.
- Non-metric b-roll runs **3.0 s** each and must match the words being spoken (a weightlifting line gets a gym shot, a scale line gets a person stepping on a scale, and so on).
- The body opens on b-roll that matches its first line.
- Hooks: keep the creator on camera; no b-roll in the hook.
- B-roll must show the right product generation (Pod 1.0 vs Pod 2.0; never Band 1.0). For a woman creator, b-roll people are women. Show no other creator's face where avoidable.
- Check b-roll sources for cuts inside the clip (agency edits) and start after them.

**Creator footage and sync**
- Her picture must be lip-synced wherever she's on screen. Never cover her lines with her own footage from a different moment.
- If her raw has burned-in overlays (phone screens, text), don't show them. Cover those seconds with matching b-roll; don't try to paint them out.
- Cover every change of setup (selfie ↔ bathroom, and so on) with a b-roll shot.
- Keep the **whole script**; don't drop lines unless the client agrees. Flag claim problems instead (see `04_do_not_use/DO_NOT_USE.md`).
- Remove dead air and repeated words or phrases (e.g. a doubled "the body pod"). Check pauses from the audio level, not only the transcript, and re-transcribe the final cut to confirm.

**Text and graphics**
- Captions: proper capitalization and punctuation (commas, full stops, question marks). Fix words the transcript gets wrong (e.g. "fat" heard as "that", "7:41", "90%", "Body Pod").
- **Product names (STRICT): `Hume Pod` and `Hume Band`.** Two words, each capitalised. Whenever a product is named in on-screen text (captions, hook headlines, CTA, cards, end slates), write it exactly like that, even when the brief or script writes it differently ("HumePod", "Hume pod", "hume band", "HealthPod", "Health Pod"). "Hume Health Pod" (brand + product) may stay as the script writes it. The pop colour, if any, applies to the whole name. Leave the audio and the client's file names alone; this is about what appears on screen. Before delivery, search every caption/headline file for `HumePod`, `HumeBand`, `HealthPod` and lower-case variants and fix all hits.
- **Caption format, one per ad (client, 2026-11-20).** Two looks; pick one per ad and keep it for every hook and size, and rotate between ads like the mark colour (3a):
  - **A: outline.** White text with a 4 px black outline (TikTok Display Bold), no background.
  - **B: white card.** Black text (#111) on a white rounded box: corner radius about 18 px at 1080 wide, 22 px side and 12 px top/bottom padding, one box per line, no outline or shadow.
  Both keep every other caption rule (position, safe area, punctuation, pop words). In B the metric pop word stays Hume blue (#1882FF) and red key-line boxes become white text on a red box, as in A. Log the choice with the mark colour.
- **Captions never leave the frame.** A caption or pop card wider than the 9:16 safe area (90 px side margins) is broken into two balanced lines, or scaled down, never cut off.
- **Hook headline stays up for the whole hook (STRICT).** When the brief asks for headline (hook) text, it stays on screen from the first frame until the body starts (the first frame of the first body line), in every hook version and every size. It never leaves early and never runs into the body. Set its end from the hook's measured end time in the edit, not a fixed length. This replaces the earlier "2.45 s" note.
  - Accent word in **red**. Never cover the creator's face for any frame of the hook (she may move or walk toward the camera: check the first, middle and last hook frames; move it below the face for full-length shots).
  - Delivery check: pull the frame just before and just after the hook/body cut and confirm the headline is on, then off.
- CTA card: compact, above her head, never covering her face.
- **Emoji (STRICT): always Apple emoji.** Any emoji in on-screen text (hook headlines, captions, CTA, cards) must be the Apple emoji design, never Noto, Twemoji or a system font's emoji. Draw them as images with `tools/apple_emoji.py`, which fetches the Apple PNG for each codepoint from the `emoji-datasource-apple` package (jsDelivr) into a local cache. Don't commit the PNGs to the repo; fetch them per project. If an emoji can't be fetched, stop and say so rather than falling back to another style.
- **No sound effects** unless the brief asks; music bed only, ducked under the voice.
- **Music plays to the last frame (STRICT).** The music bed stays at its normal (ducked) level until the video ends, then fades in 1 s or less. Never fit a song so that its natural outro lands on the ending: outros fade over 10-15 s and the music seems to stop early. Cut a continuous stretch of the track instead. Delivery check: the music is still audible in the last 0.5 s after the final word. (Pod Xmas v4 → v5.)

**Delivery**
- Master to −14 LUFS, true peak ≤ −1 dBTP (loudnorm + limiter).
- Before sending: run a frame-level cut scan (no shot under 0.7 s), a word-by-word check that each shot matches its words, and a re-transcription of the hook and ending.
- Before sending: `tools/broll_unique.py` is clean for every hook version and size (STRICT b-roll uniqueness).
- Before sending: a product check in **every size**. Pull the first and last frame of every product shot and confirm the whole product is in frame and nothing covers it. Confirm each product-use shot opens on the use itself (see the two STRICT rules under Shots and b-roll).
