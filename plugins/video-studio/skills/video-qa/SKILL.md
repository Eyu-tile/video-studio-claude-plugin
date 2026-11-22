---
name: video-qa
description: Quality-check a rendered video before anyone sees it - sync, cuts inside words, duration vs EDL, loudness (LUFS / true peak), black or frozen frames, leftover silences, caption collisions, safe zones, jump cuts. Use after every render, when asked to review/check/QA a video, or before delivering a final.
---

# Video QA

Run both the automated checks and a visual pass. Never show a draft that FAILs.

## Automated
```bash
vs qa out/draft.mp4 --edl work/edl.json --transcript work/transcript.json --preset reels --max-length 60 -o work/qa.json
# client work: add --brand <Client> [--captions work/captions.ass] to check the lessons learned from feedback
```
| check | FAIL / WARN means | fix |
|-------|-------------------|-----|
| length | over the platform/brief max | cut whole ideas (never speed up speech to fit) |
| duration | render ≠ EDL length | re-render; check sources exist and segment times are inside the source duration |
| word-boundaries | a cut slices a word | move the segment edge to `words[i].s - 0.06` or `words[i].e + 0.08` |
| loudness | > ±1.5 LU from target | render with `--loudnorm -14` (social) or `-16` (YouTube/podcast) |
| true-peak | > -1 dBTP | `--loudnorm` (TP -1.5) |
| silences | dead air left in | tighten `--max-pause` or trim that segment |
| black-frames | flash/black gap | usually a segment past the end of its source, or an overlay with no alpha |
| frozen-frames | stuck picture | fine for slides; otherwise a bad source or overlay holding |

## Visual (cheap)
```bash
vs filmstrip out/draft.mp4 -o work/cuts.png --cuts work/edl.json   # both sides of every cut
vs filmstrip out/draft.mp4 -o work/strip.png --every 4             # overall look
```
Read the PNGs and check:
- Jump cuts: same framing on both sides with a visible head jump → propose a punch-in (crop 112%) or b-roll.
- Captions: on faces, over slide text, outside safe zone, two lines where one fits.
- Graphics: on time, inside title-safe, brand colours, not covering the face.
- Reframe (9:16): subject's face in frame on every shot; otherwise set EDL `reframe` (0 = left, 1 = right).

## Listen (when it matters)
Can't hear, so check audio by data: `qa` loudness + silences, and the transcript of the render
(`vs transcribe out/draft.mp4 -o work/draft_check --model small`) should read as the approved cut list. Clipped or missing words show up as transcript differences.

## Score the sound (optional)
If earshot is installed (`vs setup --earshot`): `vs earshot timeline <video> --json` (are the hits on the cuts?),
and for launch/promo films `vs earshot critique <video> --json` (scorecard vs pro launch films). Add its top
timestamped fixes to the report.

## Report
Tell the person: PASS/WARN summary, what you fixed, anything you couldn't verify.
