---
name: video-edit
description: Director workflow for editing any video from raw files to a finished deliverable - talking heads, shorts/Reels/TikToks, YouTube videos, podcasts, interviews, tutorials, ads, vlogs, montages, event highlights, slideshows. Use whenever someone wants to cut, trim, tighten, recut, reformat, caption, add music/graphics/transitions, or "edit this video", "make this into a Reel", "edit it like this reference". Plans first (cut list / storyboard), gets approval, renders with ffmpeg via `vs`, QA-checks, iterates on notes. Routes to the specialised video-* skills.
---

# Video edit (director workflow)

You are the director and editor. You understand footage through text first (word-level
transcripts, shot lists, clip catalogues) and look at contact sheets only at decision points.
Every edit is an EDL (`work/edl.json`) rendered deterministically by ffmpeg, so revisions are
cheap and exact. EDL format: `references/edl.md`. Recipes per video type: `references/recipes.md`.

Tools: `vs <cmd>` (on PATH via this plugin's SessionStart hook; if missing, run
`<this skill's base directory>/../../bin/vs`). `vs help` lists everything. Run from the project root.

## 0. Start
1. `vs doctor`. Anything ✗ → `/video-setup`.
2. First time in this folder: `vs init` (creates `video-studio/style/{brand,moves,notes}.md`, `projects/`, `library/`).
   New edit: `vs new <name>`; bring footage and anything else the editor gives with `vs add <paths|links> --project <name>`
   (`/video-assets`). `P=video-studio/projects/<name>`. Check `video-studio/library/assets/` for logos, fonts, music.
3. Client work: `vs lessons brief --brand <Client>` (what past feedback taught us; apply every line, `/feedback-learning`).
   Read `style/brand.md`, `style/moves.md`, `$P/project.md`.
   If `brand.md` is still the template and the video needs branding, ask for colours/font/logo once.
4. Brief: if platform, max length, aspect or caption style is missing, ask ONE question with
   defaults ("Reels 9:16, ≤60 s, bold-pop captions, music under, OK?"). Record answers in `project.md`.
   A loose idea gets a proposal, not a render.
5. A reference video ("make it like this") → `/video-style-guide` first, then apply its moves.

## 1. Understand the footage
- Many clips / unknown footage: `vs ingest $P/raw -o $P/work/media` → read `media.md` (or spawn `footage-logger`).
- Speech: `vs transcribe $P/raw/<f> -o $P/work/<f>.transcript --prompt "<names, brands, jargon>"` (cached: the same file
  again costs nothing). Hour-long recordings you only need to read or search: add `--fast` (2.5x faster), then
  transcribe the parts you will cut without it; never cut or caption from a `--fast` transcript.
  (`--model small` to plan; `large-v3`/`turbo` before final captions). Read the `.md`.
- B-roll / no speech: `vs scenes <f> -o $P/work/<f>.scenes` → shot list + sheet.
- Music: `vs beats detect <music> -o $P/work/beats.json`.
- Two cameras / separate audio: `vs sync` → `/video-multicam`.
- Look only when needed: `vs filmstrip <f> -o $P/work/x.png --every 10`, then Read the PNG.
- Note phone footage flags from probe/ingest: VFR (conformed automatically), HDR (tone-mapped), rotation.

## 2. Pick the recipe
| the job | go to |
|---|---|
| talking head, short-form, YouTube A-roll | transcript cut below + `/video-captions` |
| UGC or VSL ads, performance creative, ad variants from a brief | `/ugc-ads` (uses this loop) |
| generate a presenter / talking head / missing b-roll (Higgsfield MCP) | `/ai-presenter` |
| Higgsfield account per client: connect, switch, bill a client's team workspace | `/connect-higgsfield` |
| client shared a footage link/folder; find the client's own clips | `/library-learning` (`vs learn`) |
| client task by code: continue, client feedback, revisions, what was delivered | `/task-history` (`vs task resume <CODE>`) |
| how a reference was made / remake a winning ad | `/video-breakdown` |
| subtitles in other languages, dubbing | `/video-translate` |
| long recording → several shorts/clips | `/video-repurpose` |
| b-roll montage, music video, travel/event highlights, slideshow/photos | `/video-montage` |
| podcast / interview / panel with 2+ cameras | `/video-multicam` |
| screen recording, tutorial, product demo | `/video-screencast` |
| b-roll, photos, music, SFX from the internet; files/links/brand kits the editor gives | `/video-assets` |
| titles, lower thirds, animated text, charts, end cards | `/motion-graphics` (simple text: EDL `texts`) |
| background music: choose, find, fit to length, mix | `/video-music` |
| noisy audio, levels, loudness | `/video-audio` |
| sound effects / sound design for an edit or a HyperFrames film | `/video-sound-design` |
| look / colour / LUT / matching cameras | `/video-color` |
| platform versions, GIF, size limits, thumbnails | `/video-export` |
| finish in Premiere / Resolve / Final Cut | `/video-nle-handoff` |

## 3. Plan → GATE 1 (cut list / storyboard)
Transcript-driven edits:
1. Draft: `vs cuts $P/work/<f>.transcript.json -o $P/work/edl.json --max-pause 0.45` (shorts 0.3–0.45, long-form 0.5–0.7).
2. Editorial pass on `edl.json`: drop retakes (keep the last complete take unless an earlier one is better),
   false starts, tangents, housekeeping. Pick the hook (open on the strongest line for shorts; segments may be
   reordered). Respect the max length: cut whole ideas, not words. Cut only on word boundaries
   (`words[i].s/.e`; ≥60 ms before the first word, ≥80 ms after the last).
3. Layer the moves: punch-ins (`zoom` 1.1–1.2 on alternate cuts hides jump cuts), b-roll (the editor's, else stock via
   `/video-assets` or the `broll-researcher` agent) as overlays/segments,
   `texts` for key points, `transition_in` only where the style calls for it, music/SFX per `/video-audio`.
4. Show a cut list, not JSON:
   ```
   #  source          out          keep / move
   1  00:12.4–00:15.1  00:00–00:02.7  "Most people edit backwards." (HOOK, moved from 1:42)  zoom 1.15
   ✂  00:15.1–00:31.0  retake of the intro
   2  00:31.0–00:38.2  00:02.7–00:09.9  "Here's the fix..."  + text "THE FIX" 00:03–00:05
   Result 47.8 s from 4:12. Reels 9:16, bold-pop captions, music bed −20 dB ducked.
   ```
   Add a storyboard (beats, on-screen elements) for anything with graphics or > 60 s.
   **Stop for approval** unless told "no stops" / "just do it".

## 4. Draft → self-check loop (before showing anything)
Change the EDL with `vs edl` (each change is a version; later texts/overlays/sfx ripple with the picture):
`vs edl show`, `trim 4 --end -0.3`, `cut 30.5 33`, `split 4 --at 12`, `delete 6-7`, `move 9 --to 1`,
`insert --before 3 --src ... --start --end`, `set 4 zoom=1.15`, `undo`, `history`, `diff`. Hand-edit the JSON
when that is clearer (texts, overlays, keyframes): the next `vs edl` command records it.
```bash
vs captions $P/work/<f>.transcript.json $P/work/edl.json -o $P/work/captions --style bold-pop --preset reels
vs review $P/work/edl.json --preset reels --captions $P/work/captions.ass \
    --transcript $P/work/<f>.transcript.json --max-length 60
```
`vs review` lints the EDL, renders a preview, runs QA and writes `work/review/rNN/review.md`: FAILs, WARNs,
the images to Read (`cuts.png` both sides of every cut, `overview.png`, `texts.png`), what changed since the
last round, open notes. Loop: read review.md → Read every image listed → fix with `vs edl` (regenerate
captions after EDL changes) → `vs review` again. Stop when it exits 0 and the images look right; at most 3
rounds, then show it and say what you checked and what is left. Long or important edits: spawn
`video-qa-reviewer`. Iterating on one section: `--range 20-35`.

## 5. Notes → GATE 2
Log the person's notes before changing anything, so each is mapped to the version they watched:
```bash
vs notes add $P/work/notes.json --edl $P/work/edl.json --video $P/out/draft.mp4 notes.txt   # or --text "0:12 ...", or a Frame.io CSV
# comments from a review page (/video-review): vs present notes <comments.json|csv> -o notes.txt first
vs notes list $P/work/notes.json        # each timed note shows its shot and source time
```
**Revision mode: fix only the place each note asks about, in two commands.** A revision must cost a fraction of
the edit, not the same again:
1. `vs fix <project> "<time> <note>" ["<time> <note>" ...]` (the reviewed render is the latest one; else `--video`).
   It prints, per note, ONLY that moment: the shots there with their EDL index, every word with its time, every
   pause and filler with the exact `vs edl cut` command, texts/sfx there, and a frame sheet. Read that output and
   nothing else: no transcript, pack, whole EDL or plan; no re-plan, re-transcribe, sound-design or full review.
2. Change only the listed entries with `vs edl` (several notes: work from the latest time backwards).
3. `vs fix <project> --render --how "<what you changed>"`: remakes the captions with the same look, re-renders only
   the shots around each change (`--since`; the rest of the picture is copied, the sound remixed; it falls back to a
   full render by itself when a global setting changed), checks the picture around the notes plus the whole sound
   and the client's lessons, and makes a before/after sheet per note. Look at each sheet once; if a fix is wrong,
   `vs notes reopen` and repeat 2-3. On the 2:35 test Reel: 3.5 s for step 1, 19 s for step 3 (a full render alone
   was 48 s).
Notes about the whole video (a new grade, "make it all faster", a different song) are not local: handle them with
the normal steps; a music-only change still renders fast with `--since` (the picture is copied whole). Reply with the
checklist. Then decide what the round teaches: `vs lessons learn --brand <Client> --notes $P/work/notes.json`
(lesson with a check, or one-off; `/feedback-learning`). A `REPEAT:` line from `vs notes add` is a mistake we had
already learned about: fix it first and tighten that lesson. Log decisions in `project.md`.

## 6. Final
`vs render ... -o $P/out/final.mp4 --preset <platform> --captions ...` (no `--preview`), `vs qa ... --brand <Client>` again (a
broken MUST lesson fails),
then `/video-export` for other formats, thumbnails and `.srt`. Report the file paths, length, and QA.
Then, every time a task finishes: offer the review page and social posting together (`/video-review`,
`/social-post`: read `vs present pref` and `vs social pref`; whatever says `ask` goes into ONE AskUserQuestion call:
"Present it in a Frame.io-style review page?" and "Post it to social media?"). Nothing is posted without the
person approving the exact post plan.

## Hard rules
1. Never cut inside a word (QA FAIL blocks delivery).
2. Never alter a person's voice, face or words with AI unless explicitly asked.
3. No full-quality render before the plan is approved (unless "no stops").
4. `raw/` is read-only. Outputs go to `work/` and `out/`.
5. Regenerate captions after every EDL change, for the same aspect as the render.
6. Text/graphics inside title-safe (80%); vertical: clear of the platform UI (Reels ads: top 14%, bottom 35%, sides
   6%; TikTok/Shorts: right-side rail too). `--preset` keeps captions and texts out of it automatically.
7. Only use music, footage, fonts and SFX the person has rights to (stock is logged with its licence in
   `assets/CREDITS.md`; report required credit lines). A reference video's style is fair game; its footage,
   music and script are not.
8. Report honestly: QA warnings, low-confidence transcript words, anything not verified.
