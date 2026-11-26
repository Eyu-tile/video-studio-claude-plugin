# Tools for EDITING_RULES.md Rule 1 (metric screens)

- `app_rows.py OUT.json VIDEO...`: OCRs app screen recordings at 2 fps and records where each metric row sits (y as a fraction of height).
- `app_windows.py ROWS.json...`: lists still windows (2 s or more) where a metric row holds steady, the best moments to use.
- `metric_card.py SRC T LABEL_REGEX OUT.mp4 [ROW_Y=0.38] [--grid]`: makes a 2.8 s 1080x1920 metric shot from one frame. The row sits at ROW_Y, a red box around label + value fades in, then a slow push-in. Use `--grid` for side-by-side tiles (e.g. Metabolic Age).

Example: `python3 -I metric_card.py screen-20250628-152518.mp4 18.5 'bodywater' m_water.mp4`
Needs: ffmpeg, Pillow, rapidocr_onnxruntime.
- `apple_emoji.py CACHE "😅🙃👀"`: emoji rule (EDITING_RULES: always Apple emoji). Fetches the Apple PNG for each emoji from `emoji-datasource-apple` into a local cache; `emoji_image(e, size, cache)` returns it ready to paste beside text. Fails loudly instead of falling back to another emoji style. Don't commit the PNGs.
- `scroll_card.py SRC A B OUT.mp4 DUR [--hold 0.9] [--ty 0.40] [--below 2.4] [--reverse] [--tile] LABEL_RX...`: Rule 1 metric shot from a scrolling app recording: plays A→B (or B→A with --reverse) until the metric arrives, then holds with the red box animating on.
- `broll_unique.py EDL.json [AROLL_SUBSTR]`: STRICT b-roll uniqueness check (EDITING_RULES). Flags b-roll/metric shots that share a source file (Drive id from the `.json` sidecar) or show the same footage under another name (frame fingerprints compared between every pair of shots). Run it on every hook and size before delivery; fix every flag.

## Renderer notes (from the GLP C331 round 2, 2026-11-21)
- `render.py` (v2.16 + Hume fixes) loops image overlays at the timeline fps and runs them 2 frames past `end`. Back-to-back caption PNGs now swap on the same frame. Before this fix there was a blank frame at every caption change: image2's 25 fps default, and a trim ending one frame early.
- Each segment gets `round(len * 30)` frames, so the real cut times are the running sum of those, not `round(t0 * 30)`. An overlay that must end on a cut should use that sum.
- A caption that starts exactly on a frame time can miss its first frame. Start captions 0.01 s early and end each one 0.001 s before the next one starts.
