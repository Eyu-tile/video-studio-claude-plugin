---
name: video-sound-design
description: Sound design for edits and motion graphics - find every moment that wants a sound (cuts, transitions, text pops, overlays, logo reveals, chart builds, HyperFrames clip entrances, scene changes in any render) and place real recordings on the exact frame; build an SFX library from Openverse/Freesound/your files or earshot's code-made bank; listen to and score a mix with earshot. Use for "add sound effects", "sound design this", "make it sound like a launch film", "the edit feels flat/silent", or after rendering a HyperFrames/motion piece.
---

# Sound design

Background music is its own skill: `/video-music`. Three layers here, all free:
1. **Real recordings** placed on the frame by `vs sfx` (the plugin's own "real SFX" engine).
2. **Libraries** to draw from: your files, Openverse (no key, CC-licensed sounds), Freesound (free key),
   the CC sounds bundled with `media-use`, and earshot's 250+ code-made effects.
3. **Ears**: earshot (optional, MIT) describes, finds and scores sound, including a launch-film scorecard.

## 1. Build the library (once per machine/workspace, reused by every project)
```bash
vs packs install --defaults                             # free GitHub sound libraries, CC0: uisfx (936 sounds, 12 styles) + Kenney Interface (100)
vs packs list                                           # what's registered / installed
vs packs add https://github.com/<user>/<repo> --name x --path audio --license CC0-1.0   # any free sound repo
vs sfx library                                          # what's available, by category
vs fetch search "whoosh transition" --type sfx --max-dur 3 --library    # Openverse first (no key), then Freesound
vs fetch search "door slam" --type sfx --cc0 --library   # client ads: CC0/public domain only, free anywhere, no credit
vs fetch get <results.json> 1 3 4 --library
vs add ~/Sounds/brand-kit/ --as sfx --library           # your own recordings
vs sfx bank --from earshot                              # render earshot's bank (needs vs setup --earshot)
```
Categories come from filenames (UI cue names like success, swipe, toggle, unlock, level-up are understood):
whoosh, riser, impact, pop, click, chime, glitch, swell, camera, type, paper. uisfx styles (cinematic, glass,
studio, minimal, soft, scifi, arcade, organic, zen, dreamy, rubber, mechanical) are picked with `--prefer`.
Rename files so the category word is in the name (`whoosh_air_fast.wav`). Licences go to `CREDITS.md`.

## 2. Plan (moments → sounds)
```bash
vs sfx plan --edl $P/work/edl.json --style ugc-ad -o $P/work/sfx_plan.json            # transitions, text pops, overlays, photos, source changes
vs sfx plan --hyperframes $P/work/gfx/launch --style launch -o $P/work/sfx_plan.json  # every timed clip in a HyperFrames film (follows sub-compositions)
vs sfx plan --video $P/out/draft.mp4 -o $P/work/sfx_plan.json                         # any finished video: scene changes
  [--style talking-head|tutorial|ugc-ad|montage|launch] [--words $P/work/draft_words.json] [--risers]
  [--prefer cinematic,studio] [--beats $P/work/beats.json --on-beats 1] [--every-cut] [--min-gap 0.35] [--gain-offset -3]
  [--max-head 0.8] [--max-tail 2.0] [--snap $P/out/draft.mp4] [--sheet] [--sync-bias 10] [--max-layers 2]
  [--library <brand pack> --library-only]
vs sfx analyse $P/assets/sfx      # onset / hit / crest times, loudest-50 ms level, normalising gain of every sound
```
**Accurate workflow (use it for anything that ships):**
1. Render a draft without SFX: `vs render $P/work/edl.json -o $P/out/draft.mp4`.
2. `vs sfx plan --edl $P/work/edl.json --snap $P/out/draft.mp4 --sheet --style <style> [--words ...] -o $P/work/sfx_plan.json`.
   Every cue moves to the frame the picture actually changes (a title's first visible frame, a cut's first frame,
   a move's motion peak) and lands +10 ms after it, never before.
3. **Read `sfx_plan.png`** (one frame per cue). You judge meaning: delete cues whose frame shows nothing worth a
   sound, change the kind where it is wrong. Never move timing by eye; timing comes from the frames.
4. `vs sfx check --plan $P/work/sfx_plan.json`: must say 0 outside −40/+60 ms. Then apply or merge.

**Always pass `--style`** (it sets density, level and risers) and, when anyone speaks, `--words` with a
transcript of the draft itself (`vs transcribe $P/out/draft.mp4 -o $P/work/draft_words`), so cues on a word
are lowered and minor ones dropped. The exact numbers (anchors, levels, tail/head caps, styles, search words)
are in [references/cue-sheet.md](references/cue-sheet.md); use them when editing the plan by hand.

What the planner does for every cue, so you don't have to:
- **Measures the file** and puts the right point on the frame: whoosh/riser/swell **crest** (loudest moment),
  impact **hit** (where the loud part arrives, after any silence or pre-swell), click/pop/chime/typing **onset**.
  A fixed "start 0.1 s early" is wrong by up to 2.8 s on real files.
- **Normalises loudness**: each file's loudest 50 ms goes to −12 dBFS before the cue's level is applied, so a
  quiet chime and a slammed impact both sit where the cue asks (raw files differ by 30 dB).
- **Caps build-ups and tails**: at most 0.8 s before the anchor and 2 s after, and a tail fades out by the next
  cue's frame, so a long boom never masks the whoosh after it.
- **Risers** (`--risers`, on for montage/launch): crest exactly on a logo or big-title reveal, sized to the free
  gap before it (1–4 s), cut right after the crest, at most one per 6 s.
- **Pans** whooshes with the motion of left/right transitions (±0.4).

Read `sfx_plan.md` (columns: frame, when the file starts, cue, sound, anchor, level, final gain, why). Edit the
JSON (swap `file`, move `frame_t`/`at`, change `level_db`/`gain_db`, delete cues) until it reads like a sound
designer's cue sheet, then show it to the person for approval along with the draft. If you swap a file, re-run
`plan` (or `vs sfx analyse` the new file and set `at = frame − anchor`, `gain_db = norm + level`).

Taste rules:
- Fewer, better: talking heads ≈ one cue per 5–10 s (`--style talking-head`); launch films and motion pieces can
  hit every beat (`--style launch`).
- Never cover speech: a cue on a word sits ≥ 6 dB lower, or goes in the pause.
- Vary: the planner rotates files per category; still listen for a repeated sound in a row.
- Music + SFX: duck nothing for SFX; lower the music 2–3 dB around big hits if they mask each other.

## 3. Apply
```bash
vs sfx apply $P/out/draft.mp4 --plan $P/work/sfx_plan.json -o $P/out/draft_sfx.mp4 --stem $P/out/sfx_stem.wav
vs sfx merge $P/work/edl.json --plan $P/work/sfx_plan.json -o $P/work/edl.sfx.json   # or bake into the EDL and vs render
```
`apply` keeps the picture and original audio untouched and adds the SFX bus (trims, fades and pans from the
plan are applied the same way by `apply` and by `vs render` after `merge`); `--stem` writes the SFX alone
as a WAV to drop into Premiere / After Effects / Resolve. For HyperFrames films, apply to the HyperFrames render.

## 4. Listen with earshot (optional, CPU-only, ~1.3 GB)
Install once: `vs setup --earshot` (MIT, https://github.com/Leonxlnx/earshot). Each call loads models (~20–40 s);
for many calls, the person can add its MCP server (setup prints the `claude mcp add earshot ...` line).
```bash
vs earshot critique $P/out/draft_sfx.mp4 --json        # launch-film scorecard vs 7 pro films, timestamped fixes
vs earshot timeline $P/out/draft_sfx.mp4 --json        # what is heard when: events, loudness, beat grid, sync to cuts
vs earshot describe $P/assets/sfx/x.wav                # what a sound is (tags, AudioSet labels)
vs earshot rank "a deep cinematic impact" $P/assets/sfx/*.wav   # pick the best candidate by description
vs earshot find long_recording.wav "a single camera shutter" --top 4    # cut usable hits out of a long take
vs earshot sfx list | sfx render <id> -o x.wav         # code-made effects (no models, offline)
vs earshot kit init --preset launch -o $P/work/kit.json && vs earshot kit render $P/work/kit.json --out $P/assets/sfx/kit
```
Use `critique` as a second opinion, not a verdict: it describes the style of its 7 reference films. Report its
top fixes to the person and apply the ones that fit the brief.

## Related: Clipwing "Real SFX"
A separate free skill from Clipwing (clipwing.pro/skills/real-sfx) does the same job. Its built-in sounds are the
same uisfx library this plugin installs with `vs packs install --defaults` (78 UI sounds × 12 styles = 936, CC0),
so nothing extra is needed: `vs sfx` places them on the frame, Openverse adds real recordings, earshot makes or
judges the rest. If the person has Clipwing's skill installed too, either tool is fine.
