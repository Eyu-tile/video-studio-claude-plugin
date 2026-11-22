# Set 4 build kit (ROS4, "Every wart fix, ranked", in progress 22 Nov)

TikTok green-screen ranking ad: the mom (Seedance, lip-synced to ElevenLabs "Quinn") is keyed over a code-drawn,
word-timed foot cut-away (pins per rank, ranking board, 8x ruler, clock, smooth ending). Project media lives in
`video-studio/projects/rootout-set4/` (git-ignored).

| file | what |
|---|---|
| `BRIEF.md` | the client's Set 4 brief, word for word (locked) |
| `SCRIPT_LOCK.json` | every spoken line split by clip, exact text + what is sent to TTS |
| `check_script.py` / `check_clips.py` | whisper the VO / each lip-synced clip and compare word for word (catches Seedance dropping words) |
| `SHOT_PLAN.md` | routing real / web screenshot / code / AI per beat, credit quote |
| `cutaway.py` | the animated cut-away renderer (scenes as JSON events) |
| `composite.py` | numpy chroma key + spill suppression, mom over the cut-away |
| `render_gfx.py` | calendar, offer, end card, CC stills as push-in clips |
| `make_web_cards.py`, `WEB_SOURCES.md` | real source pages (AAFP, NHS, Cleveland Clinic) framed as phone screenshots |
| `BROLL_PICKS.md`, `broll_map.json` | real CC/public-domain footage and photos, licences |
| `build4.py` | timeline: word-timed scenes + composites + inserts -> `vs render` EDLs for H1/H2/H3 |
| `make_captions.py` | render transcript -> spelling fixed back to the script -> bold-pop captions placed per shot |
