---
name: video-review
description: Present a finished video in a Frame.io-style review page - player with frame-accurate timecode, filmstrip timeline with comment pins, comments pinned to a frame or a range, replies, resolve - and bring the comments back as a revision checklist. Offer it at the end of EVERY finished task (final render, delivery, export, ad batch). Use for "present it for review", "frame.io style", "let me leave comments", "send it to the client for notes", "review link", or "the client commented on the review page".
---

# Review page

## At the end of every finished task: ask
When a task is finished (final render done, `vs task deliver`, `/video-export` done, an ad batch rendered), check
the person's standing answer first:
```bash
vs present pref          # ask (default) | always | never
```
- `never`: say nothing about it.
- `always`: make it (below) without asking.
Posting is offered at the same moment (`/social-post`, `vs social pref`): put both questions that are still at `ask`
into ONE AskUserQuestion call, so the person answers once.
- `ask`: ask with the AskUserQuestion tool, header "Review page":
  "Present <file name> in a Frame.io-style review page so you can leave comments on it?" with options
  1. **Yes, create it** - "Player with timecode, filmstrip and comments pinned to frames; I read your comments back."
  2. **No, we're good** - "Finish here."
  3. **Always** - "Create one after every finished task without asking." (then `vs present pref always`)
  4. **Never ask** - "Don't offer review pages." (then `vs present pref never`)

  No: finish with nothing more. Never ask twice for the same delivery.

## Create it
```bash
vs present $P/out/final.mp4 --project <P> [--task <CODE>] --version <v from vs task> --title "<project name>" [--client "<client>"]
```
It writes `$P/out/review/<version>/`: `index.html` (the page), `video.mp4` (a browser copy, H.264, keyframe every
second, under 14 MB so it can be published), `strip.jpg` (timeline filmstrip), `poster.jpg`, `local.html`, and
`publish.json`. Longer than about 6 minutes: present the part under review (`--section 0-300`).

**On claude.ai (the Artifact tool is available): publish it.** Read `publish.json` and call the Artifact tool with
its `file_path`, `files`, `capabilities`, `icon` and `description` (the video, filmstrip and poster go up as files
beside the page). Comments are then stored in the page's shared database: everyone the person shares it with sees
them live, and you can read them. People need **Contributor** access to comment (Viewers and Commenters can watch and
read only); say so in one line. Then:
```bash
vs present link $P/out/review/<version> <artifact url>     # remembered, and on the task's version when --task was given
```
Check once after publishing: `ArtifactData` `list` of collection `comments` (empty is fine).

**Anywhere else:** give the person `local.html` to open in a browser. Comments stay in that browser; the page's
**Export CSV** (Frame.io-style columns) or **Copy notes** sends them back.

## Bring the comments back
When the person says they commented (or "the client left notes"):
1. Published page: `ArtifactData` `list` on collection `comments` of the page's URL, save the result to
   `$P/work/review_<version>.json`. Local page: take the CSV they exported or the notes they pasted.
2. `vs present notes $P/work/review_<version>.json -o $P/work/review_<version>.txt` (open comments only; `--all`
   includes resolved). Each line is `0:12.50 text` or `0:27.00-0:30.00 text`, replies appended.
3. `vs notes add $P/work/notes.json --edl $P/work/edl.json --video $P/out/final.mp4 $P/work/review_<version>.txt`
   maps each comment to its shot and source time; for a client task also `vs task feedback <CODE> --file ... --split`.
4. Continue with the notes loop in `/video-edit` (GATE 2). After the revision, deliver it and offer a new review
   page for the new version (one page per version, so comments stay with the cut they were made on).

## The page
- Player: Space play/pause, ←/→ one frame, Shift+←/→ one second, J/L ∓1 s, M mute, F full screen, C comment.
- Timecode HH:MM:SS:FF on real time (the frame within that second), so it matches the `0:27` in notes.
- Comments: pinned to the paused frame, or a range with **+ end point**; replies; Resolve/Reopen; Open/Resolved/All
  tabs; the comment at the playhead shows over the picture; pins on the timeline jump to it.
- Shared names come from claude.ai (only ids are stored); the local page asks for a name once.
