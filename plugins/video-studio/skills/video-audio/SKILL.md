---
name: video-audio
description: Audio for video edits - clean up noisy or echoey dialogue, level voices, add and duck music, sound effects on cuts and graphics, room tone, platform loudness targets (LUFS), audio-only exports. Use for "the audio is bad", "add music", "add sound effects", "make it louder", "remove background noise", or any mix question.
---

# Audio

Everything is in the EDL and applied at render time, so it is non-destructive.

## Dialogue
- Clean-up: `"audio": {"enhance": true}` = high-pass 80 Hz, FFT denoise, de-ess, 3:1 compression.
  Preview on a raw clip first: `vs convert raw/take.mp4 -o work/clean.wav --enhance-voice`, compare by
  transcribing both or by the person's ear. Heavy noise/echo beyond that: suggest re-recording or a dedicated
  tool (Adobe Podcast Enhance, iZotope RX, or `/media-use` cleanup options) and import the cleaned WAV
  as the segment `src`'s audio via `audio_track`.
- Music or noise under the voice in the source: `vs ai stems raw/a.mp4 -o work/stems` → `vocals.wav`
  (Demucs when installed with `vs setup --stems`, else a centre-channel + dialogue-band fallback that only works
  for a centred voice over stereo music). Use the stem as `audio_track` (with `follow` for cut edits) or per shot.
- J/L cuts for natural dialogue edits: `audio_lead` (hear the next speaker before the cut) / `audio_tail`
  (let a line finish over the next picture) on the segment, 0.3–1.0 s.
- Extra beds (ambience, room tone, a second music cue): `tracks[]` with `gain` automation and `duck`.
- Uneven levels between shots: `volume_db` per segment (±3–6 dB), then `--loudnorm`.
- Mic recorded separately: `vs sync`, then `audio_track` with that file.
- Cuts sound clicky: renderer already fades 25 ms at every cut; for a gap in room tone, keep 100–200 ms more
  pause or lay a quiet room-tone loop as `music` at −40 dB without ducking.

## Music
`"music": {"file", "gain_db", "duck", "start", "fade_out"}`
| use | gain_db | duck |
|---|---|---|
| under talking head / tutorial | −20 to −24 | true |
| ad with voice-over | −16 to −18 | true |
| montage / no dialogue | −6 to −10 | false |
- Choosing, finding (Jamendo, Openverse, Incompetech, ccMixter, Archive), fitting to length on downbeats and
  crediting: `/video-music`. Never pull a reference video's song.
- Match mood and tempo to the cut; for cuts on the beat see `/video-montage`.
- End on a phrase: set `fade_out` 1.5–3 s or trim the edit to land on a downbeat.

## Sound effects
Full workflow (find every moment, place real recordings, stems, earshot scoring): `/video-sound-design`.
Manual: `"sfx": [{"file", "at", "gain_db", "in", "dur", "fade_in", "fade_out", "pan"}]` at output times (only
`file` and `at` are required). `at` is when the file starts, so measure the sound first (`vs sfx analyse x.wav`):
a whoosh's crest, an impact's hit and a click's onset go on the frame (`at = frame − anchor`), and files differ by
up to 30 dB, so use the `norm` column as the base gain. Prefer `vs sfx plan --style <style>`, which does this;
numbers in `/video-sound-design` → `references/cue-sheet.md`. Free SFX ship with the `media-use` skill
(`audio/assets/sfx/`).

## Loudness & delivery
- Targets (integrated / true peak): social & YouTube −14 LUFS / −1 dBTP, podcasts −16, broadcast −23.
  Presets set it; `--loudnorm <LUFS>` overrides. `vs qa` measures it.
- Audio-only: `vs convert out/final.mp4 -o out/final.mp3` (or `.wav` for masters).

## Paid voice and audio API keys (per project)
ElevenLabs, HeyGen API, OpenAI and Gemini keys can belong to a different account for each project.
Before the first paid call in a project, run `vs keys check <provider> --project <P>`:
- **available**: run the call through `vs keys exec --project <P> -- <command>` so that project's key is
  in the environment (`$ELEVENLABS_API_KEY`, `$HEYGEN_API_KEY`, `$OPENAI_API_KEY`, `$GEMINI_API_KEY`).
  Never `echo` or print a key.
- **missing**: run `vs keys ask <provider> --project <P>`. It opens a pop-up with a hidden field; tell the person
  one line first ("a window is asking for the ElevenLabs key for this project") and wait for it to finish.
  If it exits 3 (no desktop, e.g. SSH), ask them to type `! vs keys set <provider> --project <P>` in the prompt,
  which asks for the key hidden in their terminal. In a Claude Code cloud session, use the secure credential
  form for the API host instead.
- Never ask for a key in chat, and never put one in a file inside the workspace.
