#!/usr/bin/env python3
"""Turn review notes into a tracked checklist mapped onto the edit.

Reads notes with timestamps on the rendered video, in any of these forms (one per line):
  0:12 cut is too early            1:02.5 - 1:04 remove this            @00:00:31:12 logo too big
  [0:45] music too loud            12.4s typo in the title             0:30–0:35, 0:50 same issue
Lines without a time are general notes. Frame.io / Vimeo / Wipster CSV exports work too (any
column named like timecode/time/start and comment/note/text).

Each note is mapped to its shot (and the source file and time inside it) through the EDL the
video was rendered from, so "0:12" becomes "shot 4, a-roll.mp4 @ 31.2 s".

  vs notes add work/notes.json --edl work/edl.json notes.txt      (or - for stdin; csv works)
  vs notes add work/notes.json --edl work/edl.json --text "0:12 cut later"
  vs notes list work/notes.json [--all]
  vs notes done work/notes.json 3 --how "trimmed shot 4 end by 0.4 s"
  vs notes skip work/notes.json 5 --why "keeps the joke; asked the client"
  vs notes focus work/notes.json 3 --video out/final_v1.mp4 --edl work/edl.json   ONLY what that note touches:
        frames around its time, the shots/texts/overlays/sounds there (with their EDL index), the words spoken,
        and the commands to fix it and re-render just that part (vs render ... --since out/final_v1.mp4)

Note times are on the version that was reviewed (its EDL version is recorded): map them before
you change the EDL, and work through the notes from the END of the video backwards so earlier
times stay valid.
"""
import argparse
import csv
import io
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, fmt_ts, load_json, save_json  # noqa: E402

TS = r"(?:\d{1,2}:)?\d{1,2}:\d{2}(?::\d{2}(?![\d.]))?(?:\.\d+)?|\d+(?:\.\d+)?s\b"
RANGE = re.compile(rf"@?\[?({TS})\]?(?:\s*(?:-|–|—|to)\s*\[?({TS})\]?)?")


def to_sec(ts, fps=30.0):
    ts = ts.strip().lstrip("@[").rstrip("]")
    if ts.endswith("s"):
        return float(ts[:-1])
    parts = ts.split(":")
    if len(parts) == 4:  # HH:MM:SS:FF
        h, m, s, f = parts
        return int(h) * 3600 + int(m) * 60 + int(s) + int(f) / fps
    sec = 0.0
    for p in parts:
        sec = sec * 60 + float(p)
    return sec


def parse_line(line, fps):
    """[(t, t_end)] and the remaining text."""
    times, text = [], line.strip()
    pos = 0
    while True:
        m = RANGE.match(text, pos)
        if not m:
            break
        a = to_sec(m.group(1), fps)
        b = to_sec(m.group(2), fps) if m.group(2) else None
        times.append((a, b))
        pos = m.end()
        sep = re.match(r"\s*[,;&]\s*|\s+and\s+", text[pos:])
        if sep and RANGE.match(text, pos + sep.end()):
            pos += sep.end()
        else:
            break
    rest = text[pos:].lstrip(" :-–—)]").strip() if times else text
    return times, rest


def from_csv(text, fps):
    rows = list(csv.DictReader(io.StringIO(text)))
    if not rows:
        return []
    keys = {k.lower().strip(): k for k in rows[0]}
    tkey = next((keys[k] for k in keys if any(w in k for w in ("timecode", "time", "start", "in"))), None)
    ckey = next((keys[k] for k in keys if any(w in k for w in ("comment", "note", "text", "body"))), None)
    if not ckey:
        die(f"CSV has no comment column (columns: {', '.join(rows[0])})")
    out = []
    for r in rows:
        txt = (r.get(ckey) or "").strip()
        if not txt:
            continue
        t = r.get(tkey, "") if tkey else ""
        times = []
        if t and RANGE.fullmatch(t.strip()):
            times = [(to_sec(t, fps), None)]
        who = next((r[keys[k]] for k in keys if k in ("name", "author", "commenter", "user")), "")
        out.append((times, txt, who))
    return out


def remember(book, round_no, path, brand):
    """Log this round in the brand's feedback history and flag notes that repeat a lesson (vs lessons)."""
    import lessons
    project = None
    parts = Path(path).resolve().parts
    if "projects" in parts and parts.index("projects") + 1 < len(parts) - 1:
        project = parts[parts.index("projects") + 1]
    brand = brand or os.environ.get("VS_BRAND") or (lessons.brand_for_project(project) if project else None)
    if not brand:
        return []
    return lessons.record_notes(brand, [n for n in book["notes"] if n["round"] == round_no], project, str(path))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("notes")
    a.add_argument("source", nargs="?", help="text or csv file with notes, - for stdin")
    a.add_argument("--text", action="append", help="a note as text (repeatable)")
    a.add_argument("--edl", help="the EDL the reviewed video was rendered from")
    a.add_argument("--video", help="the reviewed video (recorded with the notes)")
    a.add_argument("--by", default="", help="who gave the notes")
    a.add_argument("--fps", type=float, default=30.0, help="for HH:MM:SS:FF timecodes")
    a.add_argument("--brand", help="client library: notes go into its feedback log and are checked against its "
                                   "lessons (default: $VS_BRAND, or the client of this project's task)")
    fo = sub.add_parser("focus", help="everything about one note's moment, nothing else")
    fo.add_argument("notes")
    fo.add_argument("id", type=int)
    fo.add_argument("--video", help="the reviewed render (default: the one recorded with the note)")
    fo.add_argument("--edl", help="the EDL that render came from")
    fo.add_argument("--words", help="vs transcribe JSON of that render (output time): the words in the window")
    fo.add_argument("--before", help="an older render: its frames go on the row above, for a before/after check")
    fo.add_argument("--pad", type=float, default=2.0, help="seconds around the note (default 2)")
    fo.add_argument("-o", "--out", help="folder (default: work/focus/note-<id>/ next to notes.json)")
    ls = sub.add_parser("list")
    ls.add_argument("notes")
    ls.add_argument("--all", action="store_true")
    for name in ("done", "skip", "reopen"):
        d = sub.add_parser(name)
        d.add_argument("notes")
        d.add_argument("ids", nargs="+", type=int)
        d.add_argument("--how", "--why", dest="how", default="")
    args = ap.parse_args()

    path = Path(args.notes)
    book = load_json(path) if path.exists() else {"notes": []}
    if args.cmd == "add":
        raw = []
        if args.source:
            text = sys.stdin.read() if args.source == "-" else Path(args.source).read_text(encoding="utf-8-sig")
            if args.source.lower().endswith(".csv") or (text.count(",") > text.count("\n") and "comment" in text[:200].lower()):
                raw += from_csv(text, args.fps)
            else:
                for line in text.splitlines():
                    if line.strip() and not line.strip().startswith("#"):
                        t, rest = parse_line(line.lstrip("-*• ").strip(), args.fps)
                        raw.append((t, rest, args.by))
        for line in args.text or []:
            t, rest = parse_line(line, args.fps)
            raw.append((t, rest, args.by))
        if not raw:
            die("no notes given (a file, - for stdin, or --text)")
        edl = load_json(args.edl) if args.edl else None
        if edl:
            from edl import locate
        nid = max((n["id"] for n in book["notes"]), default=0)
        round_no = max((n.get("round", 1) for n in book["notes"]), default=0) + 1
        for times, txt, who in raw:
            nid += 1
            n = {"id": nid, "round": round_no, "text": txt, "by": who or args.by, "status": "open",
                 "added": time.strftime("%Y-%m-%d %H:%M"), "video": args.video, "edl_version": None}
            if times:
                n["at"] = [[round(a, 3), round(b, 3) if b is not None else None] for a, b in times]
                if edl:
                    hits = []
                    for a0, b0 in times:
                        for t in ([a0] if b0 is None else [a0, b0]):
                            r = locate(edl, t)
                            if r:
                                hits.append({"t": t, "shot": r["shot"], "src": r["src"], "src_t": r["src_t"]})
                    n["where"] = hits
            book["notes"].append(n)
        if args.edl:
            try:
                from edl import hist_state
                st, _ = hist_state(args.edl)
                if st["versions"]:
                    v = st["versions"][st["head"]]["v"]
                    for n in book["notes"]:
                        if n["round"] == round_no:
                            n["edl_version"] = v
            except Exception:  # noqa: BLE001 - history is optional
                pass
        repeats = remember(book, round_no, path, args.brand)
        save_json(path, book)
        print(f"added {len(raw)} note(s) as round {round_no} -> {path}")
        show(book, False)
        for n, les, scope in repeats:
            print(f"REPEAT: note #{n['id']} is feedback we already learned ({scope} {les['id']}: {les['rule']}). "
                  f"Fix it, then ask why the lesson didn't hold (add a --check, or make it --must).")
        return
    if args.cmd == "list":
        show(book, args.all)
        return
    if args.cmd == "focus":
        focus(book, path, args)
        return
    status = {"done": "done", "skip": "skipped", "reopen": "open"}[args.cmd]
    for i in args.ids:
        n = next((x for x in book["notes"] if x["id"] == i), None)
        if not n:
            die(f"no note {i}")
        n["status"] = status
        if args.how:
            n["resolution"] = args.how
        n["updated"] = time.strftime("%Y-%m-%d %H:%M")
    save_json(path, book)
    show(book, False)


def focus(book, path, a):
    """One note's window: frames, the EDL entries that touch it, the words, and the next commands."""
    n = next((x for x in book["notes"] if x["id"] == a.id), None)
    if not n:
        die(f"no note {a.id}")
    if not n.get("at"):
        die(f"note {a.id} has no time ({n['text']!r}): it is about the whole video, so there is no single window")
    video = a.video or n.get("video")
    t0 = min(x for x, _ in n["at"])
    t1 = max((y if y is not None else x) for x, y in n["at"])
    lo, hi = max(0.0, t0 - a.pad), t1 + a.pad
    out = Path(a.out) if a.out else path.parent / "focus" / f"note-{a.id}"
    out.mkdir(parents=True, exist_ok=True)
    rows = [f"# Note {a.id}: {n['text']}", "",
            f"At {', '.join(fmt_ts(x)[1:] + (f'-{fmt_ts(y)[1:]}' if y is not None else '') for x, y in n['at'])} "
            f"(window {fmt_ts(lo)[1:]}-{fmt_ts(hi)[1:]}) on {Path(video).name if video else 'the reviewed render'}"
            + (f", by {n['by']}" if n.get("by") else "") + ".", "",
            "Fix only what this note asks. Do not re-plan, re-transcribe or re-review the whole video.", ""]
    if a.edl:
        from edl import shots
        edl = load_json(a.edl)
        sh = shots(edl)
        rows += ["## The edit here (EDL entries that touch the window)", "",
                 "| what | EDL index | output time | details |", "|---|---|---|---|"]
        for i, s in enumerate(sh):
            if s["out_end"] > lo and s["out_start"] < hi:
                seg = edl["segments"][i]
                extra = ", ".join(f"{k}={v}" for k, v in seg.items() if k not in ("src", "start", "end", "words", "text"))
                rows.append(f"| shot {i + 1} | segments[{i}] | {fmt_ts(s['out_start'])[1:]}-{fmt_ts(s['out_end'])[1:]} | "
                            f"{Path(seg.get('src') or edl.get('source') or '?').name} {float(seg.get('start', 0)):.2f}-{float(seg.get('end', 0)):.2f} s"
                            + (f"; {extra}" if extra else "") + " |")
        for key in ("texts", "overlays", "blurs", "sfx"):
            for j, it in enumerate(edl.get(key, []) or []):
                s0 = float(it.get("start", it.get("at", 0)))
                s1 = float(it.get("end", s0 + 0.5))
                if s1 > lo and s0 < hi:
                    label = it.get("text") or Path(str(it.get("file", ""))).name or key
                    rows.append(f"| {key[:-1] if key.endswith('s') else key} | {key}[{j}] | "
                                f"{fmt_ts(s0)[1:]}-{fmt_ts(s1)[1:]} | {str(label)[:60]} |")
        if edl.get("music"):
            rows.append(f"| music | music | whole edit | {Path(edl['music']['file']).name} at {edl['music'].get('gain_db', -18)} dB |")
        rows.append("")
    ws = window_words(a, lo, hi)
    if ws is not None:
        edl_arg0 = a.edl or "work/edl.json"
        rows += ["## Words here (output time)", "",
                 " ".join(f"[{w['s']:.2f}] " + ("{" + w["w"] + "}" if w.get("filler") else w["w"]) for w in ws)
                 or "(no speech)", ""]
        gaps = [(p_["e"], n_["s"]) for p_, n_ in zip(ws, ws[1:]) if n_["s"] - p_["e"] >= 0.25]
        fills = [w for w in ws if w.get("filler")]
        if gaps or fills:
            rows += ["## Exact cuts available here", ""]
            for g0, g1 in gaps:   # keep a short breath either side so the cut sounds natural
                rows.append(f"- pause {g0:.2f}-{g1:.2f} ({g1 - g0:.2f} s): shorten to 0.15 s -> "
                            f"`vs edl cut {edl_arg0} {g0 + 0.08:.2f} {g1 - 0.07:.2f}`")
            for w in fills:
                rows.append(f"- filler {w['w']!r} {w['s']:.2f}-{w['e']:.2f} -> `vs edl cut {edl_arg0} "
                            f"{w['s'] - 0.02:.2f} {w['e'] + 0.02:.2f}`")
            rows.append("- a word or phrase: cut from its start to the next word's start (times above)")
            rows.append("")
    sheet_png = None
    if video and Path(video).exists():
        import archive  # noqa: E402  (shared keyframe + contact-sheet helpers)
        step = max(0.25, round((hi - lo) / (7 if a.before else 15), 2))   # 8 per row before/after, 16 alone
        times = [round(lo + i * step, 3) for i in range(int((hi - lo) / step) + 1)]
        imgs, labels = [], []
        if a.before and Path(a.before).exists():
            imgs += archive.keyframes(a.before, times, out / "before", "vs")
            labels += [f"before {fmt_ts(t)[3:]}" for t in times]
        imgs += archive.keyframes(video, times, out / "frames", "vs")
        labels += [f"{'after ' if a.before else ''}{fmt_ts(t)[3:]}" for t in times]
        sheet_png = archive.sheet(imgs, labels, out / "frames.png", cols=len(times) if a.before else 4)
        rows += ["## Frames", "", f"`{out / 'frames.png'}`: one frame every {step:.2f} s"
                 + (" (top row: before, bottom row: after)" if a.before else "") + ".", ""]
    edl_arg = a.edl or "work/edl.json"
    vid = video or "out/final.mp4"
    nxt = Path(vid).with_name(Path(vid).stem + "_next" + Path(vid).suffix)
    rows += ["## Next", "",
             "1. Change only the entries above with `vs edl` (trim/split/cut/set ...).",
             f"2. `vs render {edl_arg} -o {nxt} --since {vid} [same --preset/--captions as before]`: re-encodes only "
             "the shots between the cuts around the change and copies the rest.",
             f"3. `vs notes focus {path} {a.id} --video {nxt} --before {vid} --edl {edl_arg}`: check that window only.",
             f"4. `vs notes done {path} {a.id} --how \"...\"`."]
    (out / "focus.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"note {a.id}: window {fmt_ts(lo)[1:]}-{fmt_ts(hi)[1:]} -> {out / 'focus.md'}" + (f", {sheet_png}" if sheet_png else ""))


def window_words(a, lo, hi):
    """Words in [lo, hi] on the output timeline: from --words (a transcript of the render), else the edit's own
    transcript (its EDL's meta.from) mapped through the EDL, fillers included and marked."""
    if a.words and Path(a.words).exists():
        return [w for w in load_json(a.words).get("words", []) if w["e"] > lo and w["s"] < hi]
    if not a.edl:
        return None
    edl = load_json(a.edl)
    src = (edl.get("meta") or {}).get("from")
    if not src:
        return None
    cands = [Path(src), Path(a.edl).parent / Path(src).name]
    tp = next((c for c in cands if c.exists()), None)
    if not tp:
        return None
    t = load_json(tp)
    from captions import remap
    return [w for w in remap(t["words"], edl, t.get("source") or edl.get("source"), keep_fillers=True)
            if w["e"] > lo and w["s"] < hi]


def show(book, everything):
    notes = book["notes"] if everything else [n for n in book["notes"] if n["status"] == "open"]
    for n in notes:
        when = ", ".join(fmt_ts(a)[1:] + (f"-{fmt_ts(b)[1:]}" if b is not None else "") for a, b in n.get("at", [])) or "general"
        where = "; ".join(f"shot {w['shot']} {Path(w['src']).name}@{w['src_t']:.2f}s" for w in n.get("where", []))
        mark = {"open": "[ ]", "done": "[x]", "skipped": "[-]"}[n["status"]]
        print(f"{mark} {n['id']:>3}  {when:<16} {n['text']}" + (f"   ({where})" if where else "")
              + (f"  -> {n['resolution']}" if n.get("resolution") and everything else ""))
    left = sum(n["status"] == "open" for n in book["notes"])
    print(f"{left} open, {sum(n['status'] == 'done' for n in book['notes'])} done, "
          f"{sum(n['status'] == 'skipped' for n in book['notes'])} skipped")


if __name__ == "__main__":
    main()
