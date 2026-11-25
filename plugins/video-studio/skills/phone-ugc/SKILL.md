---
name: phone-ugc
description: Make UGC ads that look shot on a phone with no camera and no shoot - one realistic AI character built once (selfie, then a nine-angle character sheet), a new still for every script line, one voice read cut at the pauses, talking shots, hands-and-product b-roll, and a cut on the lines - with Claude planning and prompting and Hyperscale generating every image (GPT Image 2.5), clip (Seedance 2.5), talking shot (OmniHuman 1.5) and voice (ElevenLabs / Gemini TTS). Use for "make a realistic AI character", "build the story around her", "UGC that looks shot on iPhone", "character sheet", "same woman in every shot", night-routine / testimonial / straight-ad formats, or when generated people look like AI slop.
---

# Shot-on-phone UGC from one character (Hyperscale)

The HeyGen "Shot-on-iPhone UGC" method, rebuilt on our tools. **Claude** writes the script, every prompt and
the edit; **Hyperscale** (`mcp__Hyperscale__*`) makes every picture, clip and voice; `vs gen` tracks the jobs,
cuts the voice and builds the EDL. Read `/hyperscale-briefs` first when the ad comes from a brief.

> The core idea: a new still for every line, and one voice read for the whole script. The still carries the pose
> and the place. The talking model makes it talk. Short shots and hard cuts do the rest.

| HeyGen article | Here (Hyperscale) | Price (quote every time) |
|---|---|---|
| ChatGPT image (character, sheet, stills) | `gpt-image-2-5` (16 refs, follows long prompts) | ~$0.05 / image |
| Product picture as a reference | Products tab photos (`list_products`) as refs | free |
| Avatar 6 (a still talks) | `omnihuman-1-5` (image + audio + prompt); fallback `kling-avatar-pro` | quote per second |
| Video 1 (hands/props b-roll, 5 s) | `seedance-2-5` 720p, `start_frame_url` = the still | ~$1.58 quoted, often ~$1 charged |
| One voice | `eleven-tts-v2` or `gemini-tts` on Hyperscale (or the ElevenLabs API) | quote |
| Cut it | `vs gen edl` → `vs render`, captions, music | free |

## 1. Look of a phone (every still must carry it)
| What | Do this | Not this |
|---|---|---|
| Framing | chest-up to face-filling, a little off-center, a couple of degrees of tilt | centered, level, far |
| The arm | one arm angling out of a bottom corner toward the lens | both hands free in a selfie |
| Skin | named flaws: lines, pores, redness, a spot, sun spots | smooth, glowing, retouched |
| Focus | everything sharp, front to back | blurred background |
| Color | flat, honest phone color | a grade, glow, contrast |
| Room | lived in: unmade bed, cluttered counter, blown-out window | a styled set |
| Shot length | 1-4 s | one long take |
Polished is the tell. Too close, slightly crooked, one window of light: ask for that on purpose.

## 2. The character (spend the time here)
Five parts: **camera, person, moment, place, look**. Age as a number, flaws by name, "not a model".
Make 3-4 (`count: 4`), show them as a labelled sheet, the person picks the face "you could know".
- **Person = the brief's avatar.** Map every avatar line to something visible (age, the lines she complains
  about, her room, her routine). For an aspirational product, she is real *and* likeable: someone who takes care
  of herself; tired-and-grim reads as "older than her age", the opposite of the desire.
- **Moment:** mid-sentence to a friend, eyes on the lens. Music-only ads: caught mid-laugh / mid-reaction.
`vs gen plan` writes this prompt from the script's `character` (see the gen_hs.py docstring).

## 3. The sheet, the master frames, one still per line
- **Sheet:** the pick as the only reference → a 3x3 grid, same person / clothes / light / room, only angle and
  expression change. Name every detail that must hold (hair, eyes, marks, earrings, top).
- **Every later still** gets the selfie + the sheet as refs ("strictly identity references... ignore the
  references' framing... output ONE single photo, not a grid").
- **One room, one master frame.** A room used by 2+ lines gets a master still first; every other angle in it:
  "Keep EVERYTHING. Change only the camera position" (or "only the clothes"). Lock the light by name if a still
  comes back flatter or cooler.
- **The product is its own reference.** Attach the brand's product photos to every still it's in. Keep it at
  arm's length; label close-ups come from real Library footage (generated close-ups garble labels).
- **Change the distance** line to line: wide, face-filling, hands. Same distance three times reads as a jumpy take.
- **The pose lives in the still.** Lying down, leaning in, holding the jar: put it in the picture.
- **Say how the phone is held** per line: `"camera": "selfie"` (arm out of a bottom corner, default), `"propped"`
  (on a counter / nightstand, still, slightly crooked) or `"close"` (extreme close-up). A propped shot written as
  a selfie comes back with an arm in it.
- **Describe the product's real look** once in the script (`product.look`: "amber glass, dark green label, gold
  cap, pink rose quartz roller") so every still that holds it says the same thing as the photos.

## 4. Voice: one read, cut by line
One TTS read of the whole script (one line per paragraph so the pauses fall between lines), then
`vs gen slice <jobs> --project <P>`: cut at the pauses (not the clock), one slice per spoken line; upload each
slice (`start_reference_upload`) for its talking shot. A line in another language goes in the same script.

## 5. Make them move
- **Talking (`omnihuman-1-5`):** image = the line's still, audio = its slice, prompt = where + tone in three
  words + "stays in place, head upright and level, only small natural nods; handheld, the frame drifts slightly".
  One take per line, face big (chest-up or closer). A prop in the hand gets used: put it on the table if not.
- **B-roll / motion (`seedance-2-5`, 5 s, 720p, start frame only):** ONE clear action ("fingers lift the
  roller", "she switches off the lamp"), handheld, small shake, no face for hands shots, "label stays exactly as
  it is". Keep the best 1-2 s. Two actions in 5 s rush both.

## 6. Cut it
`vs gen edl <jobs> -o work/ads/<v>.edl.json`: each line whole in its own shot, the read laid under, a beat (not a
breath) between lines. 15-30 s. Captions in full phrases, one line, inside the safe zone (Meta: top 14%, bottom
35%). Music low under a voice. **End on a moment**, not a slogan. Home stays flat colour; new rooms (outdoors,
a café) carry the warm light.

## 7. Run it
```bash
vs gen plan work/gen/v3.script.json --provider hyperscale   # jobs, models, prompts, $ estimate
vs gen next work/gen/v3.jobs.json                           # ready jobs with their inputs filled in
# Claude: quote -> person says yes -> generate -> check_generation -> download (tempfile urls expire)
vs gen done work/gen/v3.jobs.json still4 --url <result url>
vs gen fetch work/gen/v3.jobs.json --project .               # raw/gen/ + credits ledger (ai_generated)
vs gen slice work/gen/v3.jobs.json --project .               # talking ads only
vs gen edl   work/gen/v3.jobs.json -o work/ads/v3.edl.json
```
Show the character candidates, then the sheet, then the stills as contact sheets before any video: stills
are cents, clips are dollars.

## Formats
- **The straight ad:** one person, one product, one room, told across a night and a morning.
- **Music + text (brief says no VO):** same character and stills, `show: motion` lines, captions carry the story.
- **"I didn't film this" / one person, many places:** same seat and pose, the room changes around her.

## Rules
- Price first, a yes before every `generate` (team credits, daily limit). Images before video.
- `consent`: "fictional" for made-up people; a real person only with written consent, never a real person's look.
- No invented proof: no fake reviews, star ratings, customer counts or "real" before/afters. A fictional
  character's story is a dramatization; real reviews and numbers come from the brand.
- Save liked results to the Library (`save_to_library`) so the team can reuse the character.
