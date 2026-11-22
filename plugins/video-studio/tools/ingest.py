#!/usr/bin/env python3
"""Catalogue a folder of footage: one entry per clip with duration, size,
orientation, fps (and VFR), HDR, audio, how much of it is speech-level sound,
and a contact sheet per clip. The first thing to run on a pile of clips.

Usage:
  vs ingest video-studio/projects/x/raw -o video-studio/projects/x/work/media
  -> work/media.json, work/media.md (table to read), work/media/<clip>.png
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import IMAGE_EXT, fmt_ts, is_image, probe, save_json  # noqa: E402

MEDIA_EXT = {".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi", ".mts", ".m2ts", ".mxf",
             ".mp3", ".wav", ".m4a", ".aac", ".flac", ".aiff", ".aif"} | IMAGE_EXT


def sound_ratio(path, dur):
    """Fraction of the clip above -35 dBFS (rough 'someone is talking / something audible')."""
    if dur <= 0:
        return 0.0
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-vn", "-af",
                        "silencedetect=noise=-35dB:d=0.4", "-f", "null", "-"], capture_output=True, text=True)
    sil = sum(float(x) for x in re.findall(r"silence_duration: ([\d.]+)", p.stderr))
    return max(0.0, min(1.0, 1 - sil / dur))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder")
    ap.add_argument("-o", "--out", required=True, help="output path without extension")
    ap.add_argument("--no-sheets", action="store_true", help="skip per-clip contact sheets")
    args = ap.parse_args()

    files = sorted(p for p in Path(args.folder).rglob("*") if p.suffix.lower() in MEDIA_EXT and p.is_file())
    if not files:
        print(f"no media found in {args.folder}", file=sys.stderr)
        sys.exit(1)
    out = Path(args.out)
    sheets = out.parent / out.name
    clips, total = [], 0.0
    for f in files:
        p = probe(str(f))
        kind = "image" if is_image(f) else ("video" if p["has_video"] else "audio")
        entry = {"file": str(f), "kind": kind, **p}
        if kind != "image":
            entry["sound_ratio"] = round(sound_ratio(f, p["duration"]), 2) if p["has_audio"] else 0.0
            total += p["duration"]
        if kind == "video" and not args.no_sheets and p["duration"] > 0:
            sheet = sheets / (f.stem + ".png")
            every = max(p["duration"] / 12, 0.5)
            subprocess.run([sys.executable, str(Path(__file__).parent / "filmstrip.py"), str(f), "-o", str(sheet),
                            "--every", f"{every:.2f}", "--max", "12", "--width", "320"],
                           capture_output=True, text=True)
            entry["sheet"] = str(sheet)
        clips.append(entry)
        print(f"  {f.name}: {kind} {fmt_ts(p['duration'])} {p['width']}x{p['height']}", file=sys.stderr)

    save_json(out.with_suffix(".json"), {"folder": args.folder, "total_duration": total, "clips": clips})
    rows = ["| # | file | kind | dur | size | orient | fps | audio | speech-ish | flags |",
            "|---|------|------|-----|------|--------|-----|-------|-----------|-------|"]
    for i, c in enumerate(clips):
        orient = "-" if not c["width"] else ("vertical" if c["height"] > c["width"] else
                                             ("square" if c["height"] == c["width"] else "landscape"))
        flags = ",".join(x for x, on in (("HDR", c.get("hdr")), ("VFR", c.get("vfr")),
                                          (f"rot{c.get('rotation')}", c.get("rotation"))) if on)
        rows.append(f"| {i} | {Path(c['file']).name} | {c['kind']} | {fmt_ts(c['duration'])} | {c['width']}x{c['height']} | "
                    f"{orient} | {format(c['fps'], 'g') if c['width'] and c['fps'] else '-'} | "
                    f"{'yes' if c['has_audio'] else 'no'} | "
                    f"{int(100 * c.get('sound_ratio', 0))}% | {flags} |")
    md = [f"# Media in {args.folder}", f"{len(clips)} files, {fmt_ts(total)} of video/audio.", "",
          *rows, "", "Contact sheets: " + str(sheets) + "/<clip>.png (Read the ones you need)."]
    out.with_suffix(".md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(clips)} files, {fmt_ts(total)} -> {out.with_suffix('.md')}")


if __name__ == "__main__":
    main()
