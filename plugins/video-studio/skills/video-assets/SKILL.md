---
name: video-assets
description: Get every resource an edit needs - b-roll, photos, music and sound effects from the free internet (Internet Archive, Wikipedia, Wikimedia Commons, Creative Commons YouTube, Openverse, Pexels, Pixabay, Unsplash, Freesound, NASA), anything the editor provides (local files and folders, zips, brand kits, fonts, LUTs, Google Drive / Dropbox links, YouTube or other page URLs), and generated media as a last resort - with licences tracked in a credits file. Use for "add b-roll", "find footage of...", "get some music", "use these files", "here's the Drive link", "import my brand kit".
---

# Assets: stock, editor-provided, generated

All imports land in the project with a ledger: `<project>/assets/credits.json` + `CREDITS.md`
(source, author, licence, whether a credit line is required). Shared brand material goes to the
workspace library (`--library` → `video-studio/library/assets/...`) and is reusable from any project.

Layout created by `vs new`: `raw/` (main footage) · `refs/` (reference videos) · `assets/{broll,images,
logos,music,sfx,fonts,luts,graphics}`.

## 1. What the editor gives you (always first choice)
```bash
vs add ~/Desktop/shoot/ --project P                 # folders: footage → raw/ (linked, not copied), audio → music/sfx, images, fonts, LUTs by type
vs add clip.mp4 --as broll --project P               # override the type
vs add brand-kit.zip --library                       # logos, fonts, LUTs, stings for every project
vs add "https://drive.google.com/drive/folders/<id>" --project P      # Drive file or folder (gdown; must be shared "anyone with the link")
vs add "https://www.dropbox.com/s/<id>/x.mp4?dl=0" --project P
vs add "https://wetransfer.com/..." --project P       # direct-download links only; otherwise ask them to download and give the folder
vs add "https://www.youtube.com/watch?v=..." --as ref --project P     # pages via yt-dlp (YouTube, Vimeo, Instagram*, TikTok*, X)
```
`*` logged-in sites: `--cookies-from-browser chrome|safari|firefox`. Add `--license "..."` / `--credit "..."` when the
editor tells you the rights. Anything from a third-party page is recorded as "confirm rights": use it as a
**reference**, or in the edit only if the person confirms they have the rights. After importing footage: `vs ingest`.
Fonts in `assets/fonts` or the library are picked up by renders automatically (use the family name in `--font`/`texts`).

## 2. Stock from the internet
| source | best for | key |
|---|---|---|
| `archive` (Internet Archive) | historical/archival footage, newsreels, 1900s–1970s films, home movies (Prelinger), public-domain audio | none |
| `wikipedia` | the actual person/place/product/event a sentence mentions (article images, licence per file) | none |
| `wikimedia` | Commons photos and video by keyword | none |
| `youtube` | specific real-world footage; **Creative Commons uploads only** by default (needs yt-dlp) | none |
| `openverse` | 800M+ CC images and audio: music and sound effects | none |
| `jamendo` | 500k+ CC music tracks, mood/genre tags, instrumental filter | free client id |
| `incompetech` | Kevin MacLeod production music, CC BY 4.0, feel/genre/BPM | none |
| `ccmixter` | CC remixes and instrumental beds | none |
| GitHub packs | `vs packs install --defaults` (uisfx + Kenney, CC0) or `vs packs add <repo>` for any free sound repo | none |
| `pexels`, `pixabay` | modern, polished stock video/photos | free key |
| `unsplash` | high-end photos | free key |
| `freesound` | sound effects | free key |
| `nasa` | space, earth, science (public domain) | none |

Keys (one-time, per machine): the person creates them, then `vs keys ask pexels` (pop-up; pixabay, unsplash, freesound);
`vs keys list` shows what's set. With no keys, archive, wikipedia, wikimedia, youtube, openverse and nasa all work.

```bash
vs fetch search "barista pouring latte art close up" --type video --orientation portrait --max-dur 20 --project P
# -> work/assets/<query>_video.md (table) + _video.png (numbered contact sheet) → Read the PNG, pick
vs fetch get video-studio/projects/P/work/assets/<query>_video.json 3 7 --quality hd
vs fetch search "warm acoustic uplifting" --type music --project P      # openverse (Jamendo, ccMixter…), freesound
vs fetch search "whoosh transition" --type sfx --max-dur 3 --project P
vs fetch search "team meeting office" --type photo --provider unsplash,pexels --project P
vs fetch search "1950s city traffic" --type video --provider archive --project P          # archival film
vs fetch inspect <archive results.json> 2                                                  # LOOK first: scenes + keyframe sheet
vs fetch get <archive results.json> 2 --section 1:35-1:50                                  # only those 15 s, verified, provenance
vs fetch search "Golden Gate Bridge" --type photo --provider wikipedia --project P        # the real thing being talked about
vs fetch search "drone flight over forest" --type video --provider youtube --project P   # CC-licensed uploads only
vs fetch get <youtube results.json> 1 --section 30-42
```

### Internet Archive footage: look before you cut
Archive films are long, and the title rarely says what is on screen at a given minute. Never cut from a title alone:
1. **Search with a plain brief** of what is visible: `vs fetch search "children eating bananas black and white"
   --provider archive`. Shot words (footage, b-roll, cinematic, 4k) are dropped; "1950s" becomes a year filter;
   "black and white" prefers B&W prints. All words must match first (title, subject, description, shotlist); only
   if that finds too few does it accept any word. Ranking: title > subject > shotlist, trusted collections
   (Prelinger, NASA tier 1; stock_footage, feature_films tier 2), popularity, h.264 available. The `why` column says
   what matched. `--collection prelinger,nasa` narrows it.
2. **Inspect** the pick: `vs fetch inspect <results.json> <n>` (or `archive:<identifier>`) reads the film over HTTPS
   (no download), detects scenes in the first 15 min (`--window 15:00-30:00` for later), and writes
   `inspect_<id>.md` (scenes, the archive's shotlist, licence) and `.png` (one keyframe per scene, numbered with
   times). **Read the PNG** and choose the shot by what you see. Items that hold many separate clips (stock footage
   reels) list the clips with thumbnails instead (`--page 2` for more); inspect one with `--file <name>`.
3. **Cut** only those seconds: `vs fetch get <results.json> <n> --section 4:47-4:55 [--file <name>] [--no-audio]`.
   The cut is re-encoded (a stream copy snaps to keyframes: 8 s can come back as 11 s), must be within 0.1 s of the
   asked length with zero decode errors, and gets a `.provenance.json` beside it: item, file and its MD5, exact
   segment, data server, time, licence, attribution text. The credits ledger records the segment too.

Licences come from an exact URL table (PD, CC0, PD Mark, CC BY/BY-SA/BY-ND/BY-NC… 1.0–4.0); anything else is
`unrecognized` / `unknown` with commercial use `unknown`, never guessed. NC and ND are excluded unless `--allow-nc`.
Items with only a rights statement: tell the person and check the item page before publishing.

YouTube rules: default search uses YouTube's Creative Commons filter and keeps only CC BY uploads (credit line
required, logged automatically). `--allow-any-license` lists everything, marked "rights not cleared": those
can be downloaded only `--as ref` (to study), or with `--i-have-rights` when the person owns or licensed the
video. Never use a non-cleared YouTube clip in a deliverable on your own judgment.
How to search well:
- Derive queries from the transcript/beat: concrete nouns + action + setting + shot type ("hands typing laptop
  close up", "aerial city sunset"), not abstract ideas ("productivity"). Try 2–3 phrasings; English works best.
- Match the edit: `--orientation portrait` for 9:16, `landscape` for 16:9 (or plan a crop with `focus`);
  `--max-dur` keeps results short; `--quality 4k` only for 4K deliveries.
- Pick for: subject clearly visible in the first second, motion that suits the cut, lighting/colour close to the
  A-roll (grade it to match with `/video-color`), no visible brands/logos/faces that imply endorsement, no
  watermarks, no text burned in. Avoid the over-used "stock look" when the brand is premium.
- Variety: don't take three shots from the same clip/author in a row.

## 3. Use it in the EDL
- Cutaway (picture changes, voice continues): an `overlays` entry, full frame, at output times, with `in` = where
  to start inside the clip: `{"file": ".../assets/broll/x.mp4", "start": 12.0, "end": 14.5, "in": 3.2}`.
- Inserted shot (story beat without the speaker): a segment `{"src": ..., "start", "end", "mute": true}`.
- Photos: image segments (Ken Burns automatic) or overlays with `w` for picture-in-picture.
- Music: EDL `music`; SFX: EDL `sfx`. See `/video-audio`.
- Many beats needing b-roll → spawn `broll-researcher` with the cut list (it searches, picks from sheets,
  downloads, and returns overlay entries).

## 4. Generated media (only when stock and the editor's media can't do it)
`/media-use` covers voice-over, music, images, cut-outs and generated video (HeyGen or free local tools).
Generate only when asked or when nothing real fits, never to fake a real person, place or product, and say
which shots are generated.

## 5. Licences (non-negotiable)
- Search excludes NonCommercial / NoDerivatives licences by default (`--allow-nc` only for personal, non-commercial projects).
- CC BY / BY-SA items need a credit line: `CREDITS.md` lists them; put them in the video description.
- Pexels / Pixabay / Unsplash / NASA: free commercial use, no credit required (Unsplash appreciates credit). No resale
  of unaltered files, no implying endorsement by people or brands shown, NASA logos excluded.
- Music from video platforms, TV, films, or a reference video is never used in the edit.
- Before delivery: `vs credits --project P` and mention required credits to the person.
