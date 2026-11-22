---
name: library-learning
description: Learn a client's footage library from wherever they store it - Google Drive, Frame.io, Dropbox, OneDrive, any web page with videos, direct links or a local drive - into a searchable atlas (what each clip shows, best part, usable or banned), without downloading everything. Use when a client shares a resource link or folder, says "learn our footage", "here's our Drive/Frame.io", "add these resources", or before planning an edit that should use the client's own footage.
---

# Learning a client library

One library per client or product (`CaptureCards`, `AcmeShoes`): `vs learn ... <Library>`. Output goes in
`<workspace>/library/<Library>/resources/`: `ATLAS.md` and `atlas_full.json` (one record per clip),
`inventory.json`, `sources.json`, `usage.json` and `sheets/`.

## 1. Add every source the client shared
`vs learn source <Library> <link-or-path>` (repeat for each link; the provider is detected):

| Provider | Public link (no key) | With a key (`vs keys ask <provider> --project <Library>`) |
|---|---|---|
| Google Drive | folder shared "anyone with the link": listed through the public folder view | `gdrive` API key: faster, complete, durations included |
| Frame.io | share link, read with a headless browser (download links last about a day; re-read automatically) | not needed |
| Dropbox | single shared files | `dropbox` token: shared folders without downloading the zip |
| OneDrive | public share links | (business SharePoint needs the person's sign-in: ask for a public link or a download) |
| any other site | `web`: videos and images linked or played on the page, best effort | provider API: ask, then add an adapter |
| direct links, `.txt` list of links, local folder or drive | as is | - |

Ask for a key only when the public link fails or is too slow, and never in chat: `vs keys ask` opens a pop-up.
Keys are saved per client (the library name is the key's project).

## 2. Scan, then sample (fast, unattended)
- `vs learn scan <Library>`: lists every file, finds duplicates (same name and size), and flags files that
  disappeared from a source.
- `vs learn sample <Library> [--jobs 8] [--folder X] [--limit N]`: probes each clip and reads 6 frames from inside
  it over the network (no full download), then builds numbered contact sheets of 12 clips each. Roughly 3 s per
  remote clip with 8 jobs (about 25 min for 450 clips), much faster locally. Start with the folders that matter
  most for the next ad. Huge libraries are learned in rounds, not all at once.

## 3. Describe: the part that needs eyes
Repeat until nothing is waiting:
1. `vs learn next <Library>`: the next sheet and its 12 clip ids, durations and frame times.
2. Look at the sheet (one row = one clip, frames left to right over time). For each clip write `kind`
   (UGC real, AI people, AI macro, product, stock...), `people`, `product`, `beats` ("0-2: ...; 2-5: ..."),
   `framing`, `best` (most usable seconds), `status` (OK, CAUTION or BANNED, by the client's do-not-use rules in
   the library), `use` (which script lines it fits) and any `tags`.
3. Save: `vs learn tag <Library> tags.json`.
For big libraries, give sheets to parallel subagents (each gets sheet paths and the client's rules, and returns the
JSON). Never describe a clip you did not look at. Only frames seen go in `beats`.

## 4. Publish and use
- `vs learn atlas <Library>`: writes `ATLAS.md` grouped by folder. Update the library README with sources and counts.
- While editing: `vs learn find <Library> "woman blowing nose in bed" --status OK --unused` → ids, best part, beats.
- `vs learn fetch <Library> <id> -o $P/raw/lib [--section 2-6]`: a fresh download (expired links are re-read),
  only the needed part when `--section` is given.
- After delivery: `vs learn use <Library> <ids...> --project <CODE>` (the uniqueness rule: prefer `--unused`).
- When the client adds footage: `vs learn scan` again, and only the new files get sampled.
