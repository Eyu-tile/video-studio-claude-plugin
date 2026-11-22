---
name: video-translate
description: Translate a finished or in-progress edit into other languages - translated subtitles (SRT for upload, burned-in ASS) and dubbed voice tracks timed to the picture, keeping music and effects underneath. Use for "add Spanish subtitles", "make a French version", "dub this into German", "localise for Japan", multi-language ad variants, or translating captions.
---

# Translate and dub an edit

Translate from the **edited** timeline, so every version keeps the same picture. You (Claude) write the
translations; the tools handle timing, length budgets, files and mixing.

## 1. Export the lines
```bash
vs translate export $P/work/<f>.transcript.json $P/work/edl.json -o $P/work/tr/es.json --lang es
```
One line per sentence (≤ 6 s), with `start`/`end` on the output timeline, the `source` text and a
`max_chars` budget from reading speed (17 chars/s; 8 for Japanese/Chinese). Generate the transcript first if
needed (`vs transcribe`), and re-export after any EDL change.

## 2. Translate (you)
Fill every `text` in the JSON. Spoken, natural phrasing in the target market's register, not word-for-word;
keep names, numbers, product names and on-screen brand terms; stay inside `max_chars` (subtitles) and close
to the line's duration (dubbing). Spanish, French, German and Portuguese run 25–35% longer than English:
condense. Ask the person for a glossary or a native reviewer for anything public-facing, and say which
lines you were unsure about.
```bash
vs translate check $P/work/tr/es.json      # untranslated lines FAIL, over-long lines WARN: shorten them
```

## 3. Subtitles
```bash
vs translate subs $P/work/tr/es.json -o $P/work/captions_es --aspect 9:16
vs render $P/work/edl.json -o $P/out/final_es.mp4 --preset reels --captions $P/work/captions_es.ass
```
Upload `captions_es.srt` as a separate track where the platform supports it (YouTube, LinkedIn, Vimeo);
burn in for Reels/TikTok. Replace on-screen `texts` in the EDL with translated copies for that version
(save as `edl_es.json`), and check them in `texts.png` from `vs review`.

## 4. Dubbing (when asked)
Never clone or imitate a real person's voice without their explicit consent (hard rule 2 of `/video-edit`).
1. Voice clips, one per line, named `<id>.wav` in `work/tr/es_tts/`: a TTS of the person's choice via
   `/media-use` (HeyGen voices or local Kokoro: `npx hyperframes tts line.txt --voice <v> --output 3.wav`),
   ElevenLabs with their key, or a voice actor's recordings.
2. Keep the music and effects: `vs ai stems $P/raw/<a-roll> -o $P/work/stems` (Demucs gives a clean bed;
   without it, use the edit's own `music`/`sfx` and leave the original voice out).
3. Lay it out:
   ```bash
   vs translate dub $P/work/tr/es.json --clips $P/work/tr/es_tts -o $P/work/tr/es_dub.wav --bed $P/work/stems/music.wav
   ```
   Clips longer than their slot are sped up (≤ 1.25×), then allowed into the following pause; the report lists
   lines that still don't fit: shorten those translations and regenerate the clips.
4. Version EDL: copy `edl.json` to `edl_es.json`, set `"audio_track": {"src": "work/tr/es_dub.wav"}` (picture
   timing unchanged), translated texts, then `vs review` and render. Lip-sync is not adjusted; say so.

## Deliver
Per language: the video, the `.srt`, and a note of lines that need a native check. Name files
`<project>_<lang>.mp4`.

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
