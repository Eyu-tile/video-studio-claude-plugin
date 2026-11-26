# Set 1B generation log (Higgsfield WilloMd, private workspace)

All jobs are also in `../../higgsfield/catalog.jsonl` (search `s1b_`).

## 25 Nov: voices + start frames (~12 credits)
- **Boy narrator = Cody** (owner pick). ElevenLabs v4 rejects this preset (all 12 jobs failed), so his lines run on
  **Seed Speech** (`seed_audio`), the engine behind the preview the owner heard. 16 lines k01–k16, ~0.3 cr each.
  Filter flagged "Last time, I cried the whole way home." → re-worded to "...the whole **ride** home." (k02).
- Mom = Emily (ElevenLabs v4) m01–m08. Testimonials: girl = Annie (v4), Mom 2 = Maya (v4, also her voice sample for
  the Seedance take), boy 2 = Miles (Seed Speech).
- Lines tightened locally (pauses > 0.32 s cut to 0.22 s), track = 125.6 s (H1).
- Start frames: Soul 2 → GPT Image 2.6 fixes (crop above the chin, strip fake lettering). Real bottle via GPT 2.6 with
  media 2c52c56e as reference: g03 mom, g07 girl (label correct). Rejected: two hook frames (face visible) and two
  frames blocked by the safety filter (kid's bare foot) → hook N01 still to make; thumbs-up made as hand only.
- **Stopped: account at 0.55 credits** (other sessions spent the balance in parallel). 10 Seedance clips not made.

## Free preview (26 Nov)
- 29 reused clips (0 credits): see SHOT_PLAN.md; dropped S4 clinicfoot (shows a pad, not a freeze) and S1 b05 for H1
  (disc-like wart; kept only as H3 bridge placeholder). Music: Set 5-era bed 8d087a0e (ElevenLabs music, 135 s).
- `build.py H1 H2 H3 --version N`: word-cued shots from the whisper transcript, stills with slow push for clips not yet
  made (tagged TEMP in the preview only), captions (ASS, bold word-by-word), calendar split + end card in code,
  music ducked under the voice and lifted on the end card, voice + music only.

## To generate when credits are back (~340 credits)
N01 hook (boy on bed, 5 s) · N02 car (4) · N03 mom + bottle (5) · N04 dandelion (5) · N05 thumbs-up (5) · N06 bin (4) ·
N07 girl + bottle (5) · N08 Mom 2 talking take (7, voice ref t02) · N09 school yard (5) · N10 H2 run (4).
Prompts for N02/N03/N04/N06/N09 are written (submit attempt 25 Nov in this session's log).
