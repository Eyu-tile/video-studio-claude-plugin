# Status: resource atlas (in progress)

Partial build, 2026-11-12 20:10 UTC. The atlas is in `atlas/`:
- `ATLAS.json`: one record per analysed clip (path, creator/concept parsed from the folder, duration, resolution, fps, device, loudness, Drive link).
- `per_second/*.jsonl.gz`: one row per second (spoken words, faces, motion, luma, scene change, CLIP visual tags).
- `transcripts/*.md`: word-timed transcripts, per folder.
- `compliance_flags.json`: red-line wording found in creator speech.

Sources:
1. The two resource Drive folders shared first (Band 2.0 in-house creators, UGC Pod): 6,933 files.
2. The client's master Drive "Hume Health" (13y_YusLvfyR2fVbq7AIBW8NZrs5HGT_X): 106,938 files, of which ~49,000 are videos (~613 h, ~4.5 TB), ~38,400 unique after de-duplication.

Coverage at this build: 2,350 clips fully analysed. The rest are queued in priority order: Brand/App, Pod 2.0 launch, Studio, In-house, Hume Care, Agencies, UGC, Trybe, Paid Ads, Influencer. Files blocked by Google's daily download quota are skipped and retried after 24 h.

Excluded by rule: `99 — Archive / Band 1.0 — Do Not Use` (1,731 files) is never analysed or used. The `98 — Needs Classification` and `Customer Proof — Unreviewed` lists are on hold. See `../04_do_not_use/DRIVE_BLOCKLISTS.md`.

Client folder rule: `02 — Raw & Reusable Footage / In-house Creators / 0. [use this folder only] All Raw footages from Sept 29, 2026`. All 3,714 in-house files currently sit inside it. If in-house footage ever appears outside it, don't use it without asking.

To-do before final: group master-Drive per-second files by creator/shoot folder (they are currently grouped by top folder); write ATLAS.md (a human-readable index by product → creator → shot type).
