#!/usr/bin/env python3
"""Detect silences with ffmpeg and optionally draft an EDL that removes them.

Use this when no transcript exists (music beds, b-roll, a quick rough cut)
or to cross-check the transcript-based cut list.

Usage:
  python3 video-studio/scripts/silences.py RAW.mp4 -o work/silences.json
  python3 video-studio/scripts/silences.py RAW.mp4 -o work/silences.json --edl work/edl.json --min 0.6 --db -35
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import fmt_ts, need, probe, run, save_json  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--db", type=float, default=-35.0, help="noise floor in dBFS (default -35)")
    ap.add_argument("--min", type=float, default=0.5, help="minimum silence length (s)")
    ap.add_argument("--pad", type=float, default=0.1, help="keep this much of each silence edge (s)")
    ap.add_argument("--edl", help="also write an EDL keeping the non-silent parts")
    args = ap.parse_args()

    need("ffmpeg")
    info = probe(args.input)
    if not info["has_audio"]:
        print("no audio stream; nothing to detect", file=sys.stderr)
    p = run(["ffmpeg", "-hide_banner", "-nostats", "-i", args.input, "-vn", "-sn", "-dn", "-af",
             f"silencedetect=noise={args.db}dB:d={args.min}", "-f", "null", "-"])
    starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", p.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", p.stderr)]
    dur = info["duration"]
    if len(ends) < len(starts):
        ends.append(dur)
    sil = [{"start": round(max(s, 0), 3), "end": round(e, 3)} for s, e in zip(starts, ends)]
    save_json(args.out, {"source": args.input, "duration": dur, "db": args.db, "min": args.min,
                         "silences": sil})
    total = sum(s["end"] - s["start"] for s in sil)
    print(f"{len(sil)} silences, {fmt_ts(total)} total -> {args.out}")

    if args.edl:
        keep, t = [], 0.0
        for s in sil:
            a, b = s["start"] + args.pad, s["end"] - args.pad
            if b <= a:
                continue
            if a - t > 0.05:
                keep.append({"start": round(t, 3), "end": round(a, 3)})
            t = b
        if dur - t > 0.05:
            keep.append({"start": round(t, 3), "end": round(dur, 3)})
        kept = sum(k["end"] - k["start"] for k in keep)
        save_json(args.edl, {"version": 1, "source": args.input, "segments": keep,
                             "meta": {"from": "silencedetect", "db": args.db, "min": args.min,
                                      "source_duration": round(dur, 3),
                                      "kept_duration": round(kept, 3)}})
        print(f"EDL: {len(keep)} segments, {fmt_ts(kept)} kept -> {args.edl}")


if __name__ == "__main__":
    main()
