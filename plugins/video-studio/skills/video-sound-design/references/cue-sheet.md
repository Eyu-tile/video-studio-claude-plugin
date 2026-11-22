# Cue sheet reference

The numbers `vs sfx plan` uses, and the ones to use when editing a plan by hand. Every value here is
what the planner does by default, so a hand-made cue and a planned cue sound the same. Sources are in
section 7; values marked *practice* are working conventions with no standard behind them.

## 0. Who decides what

| decision | decided by | why |
|---|---|---|
| **when** (the frame) | the picture: `--snap out/draft.mp4` | vision-language models put events 0.66 s off on average (MoSound, CHI 2026); frame analysis is exact |
| **whether** a moment deserves a sound, and what kind | Claude, reading `<plan>.png` (`--sheet`) | models judge meaning well, timing badly |
| **which file** | measured fit: length of build vs the move, weight vs the event, no repeats of the last 3 | Soundify (UIST 2023): the sound should cover the event |
| **how loud** | normalised hit + cue level + on-screen size/strength (±6 dB) − 10 dB on speech | Torcoli et al. 2019; Video-Foley: intensity from video is rough, so it is clamped |
| **check** | `vs sfx check`: each sound rendered alone, its anchor measured | EBU R37 limits |

## 1. Which point of the sound goes on the frame

A sound file is not "one moment". Measure it first (`vs sfx analyse <file|dir>`), then put the right
point on the frame, not the start of the file.

| sound | anchor | why | `vs sfx analyse` column |
|---|---|---|---|
| whoosh, swish, whip | **crest** (loudest 50 ms) | the object passes the camera on the cut | `crest` |
| riser, swell, reverse cymbal | **crest** | it tops out on the reveal, then gets cut | `crest` |
| impact, boom, braam, hit | **hit** (first 50 ms within 3 dB of the loudest) | skips silent lead-ins and pre-swells; a sustained boom starts on the frame | `hit` |
| click, pop, chime, typing, glitch, shutter, paper | **onset** (first 10 ms within 20 dB of the loudest) | starts on the action | `onset` |

`at = frame − anchor`. When that is before 0 s, the head is trimmed (`in`), never slid late.

Measured on the bundled library, these are the errors a fixed lead (whoosh 0.12 s early, others on the frame) causes:

| file | anchor | anchor time | error with a fixed lead |
|---|---|---|---|
| whoosh-cinematic.mp3 | crest | 2.90 s | 2.8 s late |
| riser.mp3 (10.03 s file) | crest | 3.02 s | "climax − 10.03 s" puts the crest 7 s early; the last 5.5 s are silence |
| chime.mp3 | onset | 0.41 s | 0.41 s late (10 frames at 25 fps) |
| impact-bass-2.mp3 | hit | 0.04 s | aligning its loudest frame (1.83 s) instead would put the boom 1.8 s early |

## 2. How long it plays

| rule | default | flag |
|---|---|---|
| build-up before the anchor, at most | 0.8 s (a longer one starts part-way in, faded in over ≤ 0.15 s) | `--max-head` |
| ring after the anchor, at most | 2.0 s, faded out over ≤ 0.25 s | `--max-tail` |
| a tail never covers the next hit | fades out by the next cue's frame + 0.05 s | always on |
| risers stop at the reveal | crest + 0.12 s, then cut (the hit takes over) | always on |
| risers fit the room | build = min(gap since the previous cue − 0.3 s, file's crest, 4 s); needs ≥ 1 s; one per 6 s | `--risers` |

## 3. How loud

Recordings from Openverse, Freesound and packs differ by up to 30 dB (bundled library: −1.6 to −31.6 dBFS
loudest-50 ms). Every file is normalised first: its loudest 50 ms RMS goes to **−12 dBFS** (at most +18 dB
of lift, sample peak never above −1 dBFS). A cue's `level_db` is relative to that, so 0 dB ≈ a dialogue
peak. `gain_db` in the plan is the final volume, already including the normalisation (`norm_db`).

| moment | cue | sound | level |
|---|---|---|---|
| fast transition (whip, slide, wipe, zoom) | transition-fast | whoosh → swell | −8 |
| glitch/pixelize transition | transition-glitch | glitch → whoosh | −12 |
| dip to black | transition-dip | impact → swell | −10 |
| soft dissolve | transition-soft | swell → whoosh | −14 |
| cut to another source | cut-section | whoosh → impact | −12 |
| every hard cut (montage) | cut | click → pop | −18 |
| big/centred title | text-big | impact → pop | −10 |
| small text / lower third | text | pop → click | −12 |
| overlay / sticker enters | overlay | whoosh → pop | −12 |
| logo / end card | logo | chime → impact | −10 |
| chart / number | chart | click → pop | −14 |
| photo reveal | image | swell → whoosh | −16 |
| typing on screen | type | typing → click | −16 |
| photo / flash | camera | shutter → click | −12 |
| downbeat (with `--beats --on-beats N`) | beat | impact | −9 |
| scene change in a finished video | scene | whoosh → click | −14 |
| build into logo / big title (`--risers`) | riser | riser → swell | −14 |

A cue that lands on a word (`--words` = `vs transcribe` JSON **of the edit itself**, so the times are
output times) is lowered by `--speech-duck` dB: 10 by default, 12 for talking-head and tutorial. Torcoli et al.
(JAES 2019): keep speech ≥ 10 LU above music and ≥ 15 LU above ambience. On-screen size and visual strength add
up to ±6 dB (Soundify, MoSound), clamped because intensity predicted from video is rough (Video-Foley).

## 4. How many: styles

`--style` sets density and level; any explicit flag overrides it.

| style | min gap | tick every cut | level offset | risers | dropped when over a word |
|---|---|---|---|---|---|
| talking-head | 5.0 s | no | −2 dB | no | cut, scene, chart, type |
| tutorial | 1.5 s | no | −2 dB | no | cut, scene |
| ugc-ad | 0.8 s | yes | 0 | no | cut |
| montage | 0.5 s | yes | 0 | yes | none |
| launch | 0.25 s | yes | +2 dB | yes | none |
| (none) | 0.35 s | no | 0 | no | none |

When two moments fall within the min gap, the more important one is kept:
logo > text-big > transition-fast > transition-glitch > transition-dip > beat > cut-section > overlay >
chart > transition-soft > image > camera > type > text > scene > cut.

Stereo: whooshes on a left-moving transition (whip, whip-left, *left) are panned −0.4, right-moving +0.4.

## 5. Finding the right sound

Search words that return usable effects on Openverse/Freesound (`vs fetch search "<words>" --type sfx --max-dur 4`):

| category | search words | avoid |
|---|---|---|
| whoosh | `whoosh fast`, `swish air`, `swoosh transition`, `whip pan` | "transition" alone (returns music stings) |
| riser | `riser cinematic`, `uplifter`, `tension rise`, `reverse cymbal` | anything over 8 s |
| impact | `impact cinematic`, `boom sub`, `braam`, `punch hit` | "explosion" (debris tails) |
| pop | `pop mouth`, `bubble pop`, `ui pop` | "pop music" |
| click | `ui click`, `button click`, `mouse click`, `switch toggle` | |
| chime | `chime notification`, `success ding`, `bell short`, `sparkle` | "bell" alone (church bells) |
| glitch | `glitch digital`, `static burst`, `data glitch` | |
| type | `typing keyboard`, `typewriter key` | |
| camera | `camera shutter`, `shutter click` | |
| swell | `swell whoosh`, `reverse swell`, `suck back` | |
| paper | `page flip`, `paper rustle` | |

Save it with the category word first in the filename (`whoosh_air_fast.wav`) so the planner files it.
Prefer files under 4 s, with < 0.3 s of silence before the sound, 44.1/48 kHz, CC0 or CC BY.
Then run `vs sfx analyse` on the folder: a sound whose `hit dB` is below −40 or whose `onset` is past 1 s
is either mostly silence or the wrong cut; trim it or drop it.

## 5b. Snapping to the picture (`--snap`)

| cue | what the frame is | rule |
|---|---|---|
| title, sticker, logo, chart, photo, overlay | the first frame it is visible | first frame > median + 4×MAD of the 0.5 s before; window −0.12/+0.25 s |
| fast/soft/glitch/dip transition | the motion peak of the move | Davis & Agrawala: local max over 0.15 s, ≥ 10 % of the global max above the 0.1 s local mean; window ±0.3–0.4 s |
| cut | the first frame of the new shot | same rule, window ±0.1 s |
| beat, riser | not snapped | beats follow the music; risers follow their reveal |

`--video` alone (no EDL) finds cuts adaptively, like PySceneDetect's AdaptiveDetector: a frame's scene score is
≥ 3× the mean of its 2 neighbours each side and above the clip's own noise floor (1.5× its 95th percentile, at least
0.10), or above 0.3 outright, with shots ≥ 15 frames. On a grainy 1935 film this found 13 of 13 real cuts in a minute;
a fixed 0.3 found 7.

Hits land **+10 ms after** the frame (`--sync-bias`, 0–40). Sound before picture is noticed at about 45 ms, sound
after it only at about 125 ms (ITU-R BT.1359); for impacts, 75 ms early vs 188 ms late (Dixon & Spitz 1980).

## 5c. Selection, variation, layers

- **Fit**: a whoosh whose build (onset → crest) is 0.5–2× the transition's length wins; big events prefer a low
  spectral centroid (heavy), UI events a high one (bright) and short files (< 1.2 s). The reason is in `why`.
- **No repeats**: the last 3 files used are skipped while others exist (shuffle bag, as in Wwise/FMOD/Unity random
  containers).
- **Variation** when a file must repeat: pitch ±0.5 semitone and 0 to −2 dB, seeded so the plan is reproducible
  (FMOD units; the ranges are *practice*).
- **Layers**: at most 2 sounds ring at once (`--max-layers`); Murch: listeners follow about 2.5 similar layers,
  at 3 they blur. The least important extra is dropped.
- **Pan**: hits and anything the message depends on stay centred (phones play mono); whooshes on moves and overlays
  follow where the picture changes, at most ±0.5 (*practice*).
- **Client packs**: `--library <brand pack> --library-only` uses only that brand's sounds.

## 6. Checks before showing a draft

1. `sfx_plan.md`: no category marked missing; no two identical files in a row.
2. `vs sfx check --plan work/sfx_plan.json`: every sound rendered alone through the same chain as apply/render and
   its anchor measured; fails (exit 1) if any lands > 40 ms early or > 60 ms late (EBU R37). Expect "100 % within
   one frame".
3. Read `<plan>.png` (`--sheet`): one frame per cue. Delete cues whose frame shows nothing worth a sound.
4. Talking content: cues over words are ≥ 10 dB down; `vs qa` loudness still on target (−14 LUFS, ≤ −1 dBTP;
   short-term ≤ integrated + 5 LU, EBU R128 s1).
5. Music + SFX: if a big hit is masked, lower the music 2–3 dB around it; never duck the music for small cues.

## 7. Sources

- ITU-R BT.1359-1 (1998): A/V sync detectability +45 / −125 ms, acceptability +90 / −185 ms (+ = sound early).
- EBU R37-2007: end to end, sound ≤ 40 ms early, ≤ 60 ms late. https://tech.ebu.ch/docs/r/r037.pdf
- Dixon & Spitz 1980, *Perception* 9:719 (via Eg & Behne 2015, *Frontiers*): impact asynchrony noticed at 75 ms
  early vs 188 ms late.
- EBU R128 s1 (2020): short-term ≤ target + 5 LU, true peak ≤ −1 dBTP. https://tech.ebu.ch/docs/r/r128s1.pdf
- Torcoli, Freke-Morin, Paulus, Simon, Shirley, JAES 67(12) 2019: speech ≥ 10 LU over music, ≥ 15 LU over ambience.
- Murch, "Dense Clarity – Clear Density": about 2.5 layers.
- Davis & Agrawala, "Visual Rhythm and Beat", SIGGRAPH 2018: impact envelope and peak rule.
- Lin et al., "Soundify: Matching Sound Effects to Video", UIST 2023: interval timing, pan/gain from on-screen
  position and size, sound covers the event. https://arxiv.org/abs/2112.09726
- Huang et al., "MoSound", CHI 2026 (Adobe): VLM event centres 0.66 ± 0.25 s off; size/velocity → volume/pan.
- Du et al., "CondFoleyGen", CVPR 2023: onset transfer from visual onsets beat generation on timing (AP 71.9 % vs
  60.0 % at ±100 ms).
- Lee et al., "Video-Foley" 2024: intensity from video, half of frames within ±6 dB.
- PySceneDetect AdaptiveDetector: adaptive_threshold 3.0, window 2, min_scene_len 15.
- OpusClip Auto SFX docs: a curated library times more precisely than generated sounds; skipping moments is part of
  the job. https://help.opus.pro/docs/article/auto-sfx
