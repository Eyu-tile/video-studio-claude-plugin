#!/usr/bin/env python3
"""Make a labelled contact sheet (one PNG) so the agent can LOOK at a video
cheaply instead of dumping hundreds of frames.

Modes (pick one):
  --every 5              a frame every 5 s
  --at 1.2,8.5,30        frames at given times
  --cuts work/edl.json   both sides of every cut, on the rendered output timeline
                         (run against the render to check jump cuts, flashes, bad frames)

Usage:
  python3 video-studio/scripts/filmstrip.py out/draft.mp4 -o work/strip.png --every 4
  python3 video-studio/scripts/filmstrip.py out/draft.mp4 -o work/cuts.png --cuts work/edl.json
"""
import argparse
import math
import os
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import cut_points, die, fmt_ts, load_json, need, probe, run, timeline  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("-o", "--out", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--every", type=float)
    g.add_argument("--at")
    g.add_argument("--cuts")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--width", type=int, default=480, help="thumbnail width in px")
    ap.add_argument("--max", type=int, default=48, help="cap on thumbnails")
    args = ap.parse_args()

    need("ffmpeg")
    info = probe(args.input)
    dur = info["duration"]
    if args.every:
        times = [round(t * args.every, 3) for t in range(int(dur // args.every) + 1)]
    elif args.at:
        times = [float(x) for x in args.at.split(",")]
    else:
        times = []
        for it in cut_points(timeline(load_json(args.cuts)))[1:]:
            mid = it["out_start"] + it["overlap"] / 2
            times += [max(it["out_start"] - 0.08, 0), mid, it["out_start"] + it["overlap"] + 0.04] if it["overlap"] \
                else [max(it["out_start"] - 0.08, 0), it["out_start"] + 0.04]
    times = [t for t in times if 0 <= t < dur][: args.max]
    if not times:
        die("no timestamps inside the video")

    td = Path(tempfile.mkdtemp())
    try:
        label = "drawtext=text='%s':x=8:y=8:fontsize=h/12:fontcolor=white:box=1:boxcolor=black@0.6"
        def grab(i, t):  # each frame is its own seek: run them side by side on every core
            run(["ffmpeg", "-y", "-v", "error", "-threads", "2", "-ss", f"{t:.3f}", "-i", args.input, "-frames:v", "1",
                 "-vf", f"scale={args.width}:-2," + label % fmt_ts(t).replace(":", r"\:"),
                 str(td / f"f{i:03d}.png")])
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=max(2, min(8, os.cpu_count() or 2))) as ex:
            list(ex.map(lambda it: grab(*it), enumerate(times)))
        cols = min(args.cols, len(times))
        rows = math.ceil(len(times) / cols)
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        run(["ffmpeg", "-y", "-v", "error", "-framerate", "1", "-i", str(td / "f%03d.png"),
             "-vf", f"tile={cols}x{rows}:padding=4:margin=4:color=0x222222", "-frames:v", "1", args.out])
    finally:
        shutil.rmtree(td, ignore_errors=True)
    print(f"{len(times)} frames ({cols}x{rows}) -> {args.out}")


if __name__ == "__main__":
    main()
