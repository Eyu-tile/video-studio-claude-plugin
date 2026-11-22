# video-studio: agentic video editing for Claude Code

Claude becomes your editor and director. It understands footage through transcripts, shot lists
and beat maps, plans the edit, shows you a cut list for approval, renders deterministically with
FFmpeg, checks its own work, and iterates on your notes. It handles any common edit.

| you have | you get |
|---|---|
| a talking-head recording | a tight Reel/Short/YouTube cut: pauses, ums, retakes gone, captions, punch-ins, music |
| a long podcast or webinar | 5–10 vertical clips with hooks, captions and covers |
| 2–4 camera angles + a mixer recording | an auto-switched multicam edit that follows whoever is talking |
| a folder of b-roll / photos + a song | a beat-synced montage, travel film, highlight reel or slideshow |
| a screen recording | a tutorial with dead time cut, speed-ups, zooms on the action, step titles |
| a reference video you like | its pacing, captions, moves, look and sound written as rules and applied to your footage |
| a brief and no b-roll | footage, photos, music and SFX from the free internet (Internet Archive, Wikipedia/Commons, Creative Commons YouTube, Openverse) and stock libraries (Pexels, Pixabay, Unsplash, Freesound, NASA), downloaded with licences logged; archive films inspected scene by scene from a keyframe sheet before cutting, then only the seconds you need, verified, with a provenance record |
| no music | mood/genre/tempo-matched tracks from Jamendo, Openverse, Incompetech, ccMixter, Archive; fitted to the exact edit length on downbeats so the song ends on the last frame, ducked under speech, credit lines logged |
| a silent edit or HyperFrames film | every moment found (cuts, transitions, text pops, logo reveals, chart builds) and a real recording placed on the exact frame, plus an SFX stem; optional earshot scoring against pro launch films |
| files, folders, zips, brand kits, Drive/Dropbox/YouTube links | everything imported and sorted into the project (footage linked, not duplicated), with a credits ledger |
| a finished cut | every platform version, GIF, size-limited file, thumbnail, SRT, chapters, or a timeline for Premiere/Resolve/FCP |

## Install
```
/plugin marketplace add Eyu-tile/video-studio-claude-plugin        (or a local path to this marketplace folder)
/plugin install video-studio@video-studio-marketplace
```
Once per machine, ask Claude "set up video editing" (runs `vs setup`). Requirements: FFmpeg built
with libass (Homebrew and apt builds are), Node 22+, Python 3.10+. A Whisper model downloads on first
transcription (mlx-whisper on Apple Silicon, faster-whisper elsewhere).

## Use
```
vs init                 # in your project: creates video-studio/{style,projects}
vs new launch-reel      # video-studio/projects/launch-reel/{raw,work,out}
```
Drop footage into `raw/` and talk to Claude:
> Edit launch-reel into a 45 s Reel like the reference in style/refs/, bold captions, show me the cut list first.

## What's inside
**Skills**
| skill | does |
|---|---|
| `video-edit` | the director loop and router: brief → understand → plan (gate) → draft → QA → notes (gate) → final |
| `video-captions` | bold-pop, karaoke, clean, minimal captions, SRT, safe zones |
| `video-repurpose` | long → many shorts |
| `video-montage` | music- and footage-driven edits, beat sync, slideshows |
| `video-multicam` | audio sync, auto camera switching, tightened conversations |
| `video-screencast` | tutorials and demos |
| `video-audio` | voice clean-up, music, ducking, SFX, loudness |
| `video-color` | grades, LUTs, HDR, camera matching |
| `video-assets` | stock search + download, editor-provided files/links/brand kits, credits ledger |
| `video-music` | choose, find, fit and mix background music |
| `video-sound-design` | SFX on the exact frame from EDLs, HyperFrames or any video; libraries; earshot listening |
| `video-export` | platform presets, multi-aspect, GIF/WebM/ProRes/MP3, size limits, thumbnails, chapters |
| `video-style-guide` | learn a style from reference videos |
| `ai-presenter` | AI talking-head presenter and b-roll through the Higgsfield MCP (or another generator) as tracked jobs, pulled back into the edit |
| `video-review` | Frame.io-style review page for a finished video: frame-accurate player, filmstrip timeline, comments pinned to frames or ranges, replies, resolve; offered after every finished task; comments come back as `vs notes` (`vs present`) |
| `social-post` | Post a finished video to TikTok, Instagram Reels, YouTube/Shorts, LinkedIn or X through Composio: one checked upload per platform, platform captions, the exact plan approved before anything posts, links logged (`vs social`, `vs setup --social`) |
| `video-delivery` | Deliver approved videos straight into a client's Google Drive folder at any size, with no local copy: one folder per video, the latest version of every file only, checked at full size in Drive and logged (`vs deliver`, a one-time Apps Script) |
| `feedback-learning` | Learns from every note: per-brand lessons with machine checks, a brief before each edit, repeated feedback flagged, and `vs qa --brand` failing when a lesson is broken |
| `task-history` | Client task history by code: every delivered version (files, link, note, snapshot of the edit), client feedback with done/skipped tracking, and `vs task resume <CODE>` to pick up exactly where you left off |
| `library-learning` | Learn a client's footage from Drive, Frame.io, Dropbox, OneDrive, web pages, links or a local drive without downloading it all: scan, network frame sampling into contact sheets, described atlas, search, fetch on demand, usage log (`vs learn`) |
| `ugc-ads` | UGC and VSL ads from a brief: audience/emotion/awareness → hooks, beats, captions, music; variants; ad QA (hook, words on screen, stimulus, safe zones, CTA, loudness, compliance); client review page |
| `video-translate` | translated subtitles (SRT/ASS) and dubbed tracks timed to the edit, music kept under |
| `video-breakdown` | how a reference was made, shot by shot (camera, look, pacing, beat sync; optional rea-video forensics: live/AI/3D/screen, OCR text), remake plan + template EDL |
| `motion-graphics` | titles, lower thirds, charts, end cards with HyperFrames |
| `video-qa` | automated and visual checks |
| `video-nle-handoff` | CMX3600 / FCPXML export, Resolve and FCP MCP pointers |
| `video-setup` | install/repair tools |
| `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use` | HeyGen HyperFrames v0.9.19 (Apache-2.0) |
| `reverse-any-video`, `style-sampling` | HyperFrames: rebuild a reference video as an editable project; new episodes in proven explainer styles |

**Agents**: `edit-planner`, `footage-logger`, `broll-researcher`, `motion-designer`, `video-qa-reviewer`.

**CLI** (`vs help`): `setup doctor init new where add fetch keys credits probe ingest transcribe pack scenes
silences filmstrip beats sync cuts multicam captions music packs sfx earshot render proxy watch breakdown rea edl review notes ai translate ads gen higgsfield qa convert thumbs export yt-dlp`.

**Higgsfield accounts**: the plugin adds a `higgsfield` MCP connection (sign in once with /mcp; Higgsfield uses a
browser sign-in, there is no key to paste). `/connect-higgsfield` connects more accounts, one named connection
each (`higgsfield-<client>`), and picks the one a project generates with; `vs higgsfield list | use | remove`.
A client's team workspace that your login was invited to works too: `vs higgsfield use <account> --workspace <id>`;
before billing, Claude selects that workspace and states the account and credits.

**Watch any link**: `vs watch <link>` downloads a video from YouTube, Instagram (public embed fallback when
Instagram rate-limits), TikTok, X, Vimeo, ~1,800 yt-dlp sites, Google Drive, Dropbox or a direct file, then
writes `watch.md` with the caption, a Whisper transcript, the shot breakdown and timestamped frame sheets for
Claude to read. Private or logged-in posts: `--cookies-from-browser chrome`.

**Speed** (3-minute 1080p talk cut to a 2:35 Reel, 4 CPU cores): final render 88.6 s -> 54 s (x264 `veryfast`
by default, same quality as `medium` on real footage; crop-then-scale framing; one decoder per run of jump cuts),
review round 67.7 s -> 41 s, QA 32.6 s -> 12.5 s (one pass), silence detection 12.1 s -> 0.7 s, cut sheets 6.4 s ->
2.4 s, a repeated transcription 0.1 s (cached). Renders also land on the right source frame: 97 % exact against
82.5 % before. `--speed balanced|best` encodes masters with x264 medium/slow; `vs transcribe --fast` is a 2.5x faster
draft for reading long recordings (not for cutting).

**Fast revisions, in two commands**: `vs fix <project> "1:12 cut this pause shorter"` prints only that moment: the
shots there with their EDL index, every word with its time, every pause and filler with the exact `vs edl cut`
command, and a frame sheet. After the edit, `vs fix <project> --render` remakes the captions, re-renders only the
shots around each change (`--since`: finals carry a keyframe at every cut and a `.render.json` manifest; the rest of
the picture is copied), checks the picture around the notes plus the whole sound, and makes a before/after sheet.
On a 2:35 1080p Reel: finding the spot 3.5 s, the whole revision 19 s (a full render alone is 48 s), and the result
matches a full render frame for frame. Every shot sits on the absolute frame grid, so untouched shots never move.

**Agentic loop**: `vs edl` makes small edits (trim, split, cut a time range, delete, move, insert, set) with
version history, undo/redo and ripple (texts, overlays, sfx follow the picture); `vs review` runs one
self-check round (lint, preview render, QA, cut/overview/text sheets, what changed, open notes) and exits 0
only when nothing fails; `vs notes` turns timestamped feedback or Frame.io CSVs into a checklist mapped to
shots and source times.

**Renderer features**: frame-accurate cuts from any number of sources, still images, speed 0.25–4×
with pitch-kept audio, smooth speed ramps, reverse and freeze frames, J/L cuts, keyframed zoom / pan /
rotation (reframing that follows a subject), cover/contain/blurred-fill reframing to any aspect,
25+ transitions, 14 colour grades and `.cube` LUTs per shot, automatic HDR tone-mapping (or HDR10/HLG
kept) and VFR conforming, two-pass vid.stab stabilisation, text overlays with animations, alpha overlays,
green-screen keying, keyframed picture-in-picture, blur/pixelate regions, burned captions, voice enhancement,
SFX, multiple audio tracks with volume automation and ducking, continuous audio tracks for multicam,
EBU R128 loudness, h264/h265/ProRes and 10-bit, proxies, chunked parallel rendering with a per-chunk cache
(only changed shots re-render), partial-range previews.

## Optional extras
- **Free sound packs from GitHub** (`vs setup --packs` or `vs packs install --defaults`): uisfx (936 CC0 sounds in
  12 styles) and Kenney Interface Sounds (100 CC0 recordings); add any other free sound repo with `vs packs add`.
- **earshot** (`vs setup --earshot`, MIT, CPU-only, ~1.3 GB): lets Claude hear: describe, rank and find sounds,
  critique a mix against 7 professional launch films, and render 250+ code-made sound effects.

- **AI helpers** (`vs setup --ai`, `--stems`; `vs ai status`): face-tracking reframe (OpenCV), PySceneDetect cuts,
  librosa beats, rembg cutouts, Demucs stems; Real-ESRGAN / RIFE binaries on PATH for upscaling and smooth
  slow motion. Each has a built-in fallback (skin/motion tracking, ffmpeg scene score, built-in beat tracker,
  flat-colour key, centre/side split, lanczos, minterpolate), so nothing here is required. `vs ai match`
  (reference frame → `.cube` LUT) is native.
- **rea-video** (`vs setup --rea`, Apache-2.0, ~1 GB): deep shot forensics for `/video-breakdown`: live action vs AI
  video vs 3D vs screen recording per shot, on-screen text timeline by OCR, stickers, vocal/music separation.

## Learn a client's footage library (`vs learn`)
Clients keep footage in different places. Add each share once; public links work as they are, and a saved key
(`vs keys ask gdrive|dropbox --project <Library>`) switches to the provider's API:

    vs learn source AcmeShoes "https://drive.google.com/drive/folders/..."   # Drive, Frame.io, Dropbox, OneDrive,
    vs learn source AcmeShoes "https://next.frame.io/share/..."              # any page with videos, direct links,
    vs learn source AcmeShoes /Volumes/Footage/Acme                          # a .txt list of links, a local drive
    vs learn scan AcmeShoes          # list every file (duplicates and removed files flagged)
    vs learn sample AcmeShoes        # 6 frames per clip read over the network -> contact sheets of 12 clips
    vs learn next AcmeShoes          # Claude looks at a sheet and saves what it sees: vs learn tag
    vs learn atlas AcmeShoes         # ATLAS.md: every clip, what's in it, best part, OK/CAUTION/BANNED
    vs learn find AcmeShoes "woman sneezing in bed" --status OK --unused
    vs learn fetch AcmeShoes <id> -o raw/lib --section 2-6     # fresh download of just what the edit needs

Measured on a real Frame.io share: 454 files listed in about 80 s, then 36 clips (including 4K .mov) sampled in
about 110 s with 8 parallel jobs. Frame.io and other web pages are read with headless Chromium (Node.js and
Playwright). Output lives in `library/<Library>/resources/`.

## Learning from feedback (`vs lessons`)

Every note is a chance not to make that mistake again. After each revision round, the notes that apply to future
videos become lessons in the client's library (`library/<Brand>/LESSONS.md`), most with a machine check:
```bash
vs lessons brief --brand TrueClean                      # before planning: the ranked rules for this client
vs lessons add --brand TrueClean --rule "Music bed at -22 dB or lower" --check music_gain_max=-22 --must
vs lessons learn --brand TrueClean --notes work/notes.json   # handled notes to classify + feedback that keeps returning
vs qa out/final.mp4 --edl work/edl.json --brand TrueClean    # a broken MUST lesson fails QA before the client sees it
```
`vs notes add` and `vs task feedback` flag a note that repeats a lesson (`REPEAT:`), so a lesson that didn't hold
gets tightened. House rules for every client: `--global`. Skill: `/feedback-learning`.

## Task history: pick up a client task by its code
Every client task gets a code (e.g. `TC0488`). Its history is kept in `video-studio/history/` (committed with the
workspace), so a new session, or another machine, can continue it:

    vs task new TC0488 --project capturecards-tc0488 --client TrueClean --title "Scale & awareness 1"
    vs task deliver TC0488 --file out/final/ad.mp4 --link <drive link> --note "v2: real people, TC0217 structure"
    vs task feedback TC0488 "make the hook faster; 0:12 swap the shot"   # client comments, kept word for word
    vs task resume TC0488     # brief, versions, open feedback, files to read, next step
    vs task done TC0488 1 --how "hook now 2 cuts"   ·   vs task list --open   ·   vs task restore TC0488

Each delivery snapshots the edit's inputs (script, shot list, EDLs, builder, project.md) into
`history/<CODE>/vN/`. At session start the plugin lists open tasks, so "continue TC0488" or "the client replied"
starts from the recorded state.

## API keys: per project, entered in a pop-up
Paid voice and audio services (ElevenLabs, HeyGen API, OpenAI, Gemini) often bill a different account for each
project, so keys can be saved per project. When a project needs one, Claude runs `vs keys ask elevenlabs --project
<name>`, which opens a native pop-up with a hidden field (macOS dialog, Windows credential prompt, zenity/kdialog on
Linux). The key never passes through the chat. Calls then run with `vs keys exec --project <name> -- <command>`.

    vs keys ask elevenlabs --project acme      # pop-up; saved for project "acme" only
    vs keys ask elevenlabs                     # machine-wide (all projects without their own key)
    vs keys check elevenlabs --project acme    # where the key comes from (never prints it)
    vs keys list --project acme                # all providers, last 4 characters only
    vs keys set elevenlabs --project acme      # terminal alternative (hidden prompt), e.g. over SSH

Lookup order: the project's key, then the environment variable (`ELEVENLABS_API_KEY`, ...), then the machine-wide
key. Keys live in `~/.config/video-studio/` (`keys.env` and `projects/<name>.env`, mode 600), outside the
workspace, so they are never committed. Inside `<workspace>/projects/<name>/` the project is detected automatically.

## Stock media keys (optional, free)
Pexels, Pixabay, Unsplash and Freesound need a free API key each: `vs keys ask pexels` (stored in
`~/.config/video-studio/keys.env`, mode 600; environment variables `PEXELS_API_KEY` etc. also work). Internet
Archive, Wikipedia, Wikimedia Commons, Creative Commons YouTube, Openverse and NASA work without keys. NonCommercial/NoDerivs licences are excluded by default; `--cc0` keeps only CC0/public-domain results (free to use anywhere, no credit), the safe choice for client ads.

## Privacy
The bundled HyperFrames CLI sends usage telemetry (and a usage beacon when its skill starts). Turn it off with
`npx hyperframes telemetry disable`. The plugin's own `vs` tools send nothing.

## Workspace
Style files, projects and a shared `library/` (logos, fonts, LUTs, music) live in your repo (`video-studio/`), so brand rules, notes from past feedback
and editing "moves" travel with the project. Footage and renders are git-ignored by the generated `.gitignore`.

## Limits
- No generative video/voice by default; `media-use` can add it on request (HeyGen or local tools).
- Very heavy colour work, audio restoration beyond denoise/de-ess, and complex compositing are better
  finished in an NLE (`video-nle-handoff`).
- Instagram/TikTok downloads usually need browser cookies; you can always drop files in manually.

Third-party notices: `THIRD_PARTY_NOTICES.md`. Research behind the tool choices: `SKILLS_GALLERY.md`.
