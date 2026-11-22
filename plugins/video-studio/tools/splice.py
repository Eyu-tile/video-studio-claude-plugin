"""Revision renders that touch only what changed.

A final render writes a manifest (<out>.render.json): every shot's signature and output time, every timed video
item (texts, overlays, blurs, caption events) and the render settings. Finals are encoded with an IDR keyframe at
every hard cut, so the video can be cut there without re-encoding.

On a revision (`vs render new_edl.json -o out/final_v2.mp4 --since out/final_v1.mp4`), `plan()` compares the two
manifests and returns the smallest window between hard cuts that contains every change, in both timelines:
  - shots: the unchanged run at the start (prefix) and at the end (suffix, shifted when the edit got longer/shorter)
  - timed items: anything that differs, appeared or disappeared widens the window to cover it
  - audio-only changes (music, sfx, tracks, volume, ducking) never widen the video window: audio is remixed in full
The renderer then encodes only that window and copies the rest of the old file's video stream around it.
Anything global (size, fps, codec, grade, LUT, caption styles, renderer version) means a full render.
"""
import hashlib
import json
import re
from pathlib import Path

# EDL keys that only change sound (the audio is always re-rendered in full on a revision)
AUDIO_EDL_KEYS = {"sfx", "music", "tracks", "audio", "audio_track"}
TIMED_VIDEO_KEYS = ("texts", "overlays", "blurs")
AUDIO_SEG_KEYS = {"volume_db", "mute", "audio_lead", "audio_tail", "audio", "gain"}
MAX_WINDOW_SHARE = 0.6      # a window over 60 % of the edit: a full render is about as fast and simpler


def _sig(obj):
    return hashlib.sha1(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()[:16]


def file_sig(path):
    try:
        st = Path(path).stat()
        return [str(Path(path).resolve()), st.st_size, int(st.st_mtime)]
    except OSError:
        return [str(path), None, None]


def ass_events(path):
    """Caption events from an ASS file: (start, end, signature of everything else), plus a hash of the header."""
    if not path or not Path(path).exists():
        return [], None
    head, events = [], []
    for line in Path(path).read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("Dialogue:"):
            parts = line.split(",", 9)
            if len(parts) < 10:
                continue

            def t(s):
                h, m, rest = s.strip().split(":")
                return int(h) * 3600 + int(m) * 60 + float(rest)
            events.append({"start": round(t(parts[1]), 3), "end": round(t(parts[2]), 3),
                           "sig": _sig([parts[0], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9]])})
        elif not line.startswith(("Comment:",)):
            head.append(line)
    return events, _sig(head)


def manifest(edl, groups, total, settings, captions=None):
    """What a render contains, for comparing against the next version."""
    gs = []
    for g in groups:
        seg = {k: v for k, v in g["seg"].items() if k not in AUDIO_SEG_KEYS}
        gs.append({"sig": _sig([g["src"], file_sig(g["src"]), round(g["start"], 4), round(g["end"], 4), seg,
                                round(g["overlap"], 4), round(g["len"], 4)]),
                   "out_start": round(g["out_start"], 4), "out_end": round(g["out_end"], 4),
                   "overlap": round(g["overlap"], 4)})
    items = []
    for key in TIMED_VIDEO_KEYS:
        for it in edl.get(key, []) or []:
            start = float(it.get("start", 0))
            end = float(it.get("end", start))
            body = {k: v for k, v in it.items() if k not in ("start", "end")}
            if key == "overlays" and it.get("file"):
                body["_file"] = file_sig(it["file"])
            items.append({"kind": key, "start": round(start, 4), "end": round(end, 4), "sig": _sig([key, body])})
    cap_events, cap_head = ass_events(captions)
    for e in cap_events:
        items.append({"kind": "caption", "start": e["start"], "end": e["end"], "sig": e["sig"]})
    globals_ = {k: v for k, v in edl.items() if k not in AUDIO_EDL_KEYS | set(TIMED_VIDEO_KEYS) | {"segments"}}
    return {"version": 1, "settings": dict(settings, captions_style=cap_head), "globals": _sig(globals_),
            "total": round(total, 4), "groups": gs, "items": items,
            "cuts": cuts_of(gs, total)}


def cuts_of(gs, total):
    """Times where the picture can be split without touching a transition: 0, every hard cut, the end."""
    cuts = [0.0] + [g["out_start"] for g in gs[1:] if g["overlap"] <= 1e-6] + [round(total, 4)]
    return sorted(set(cuts))


def plan(old, new):
    """None: render everything. {"copy": True}: the video is unchanged (audio only). Otherwise the window:
    {"a": start (same in both), "b_new": end in the new edit, "b_old": end in the old one, "why": [...]}."""
    if old.get("version") != new.get("version") or old["settings"] != new["settings"]:
        changed = sorted(k for k in set(old["settings"]) | set(new["settings"])
                         if old["settings"].get(k) != new["settings"].get(k))
        return {"full": f"render settings changed: {', '.join(changed) or 'version'}"}
    if old["globals"] != new["globals"]:
        return {"full": "a global setting of the edit changed (grade, LUT, reframe, output...)"}
    go, gn = old["groups"], new["groups"]
    k = 0
    while k < min(len(go), len(gn)) and go[k]["sig"] == gn[k]["sig"] and abs(go[k]["out_start"] - gn[k]["out_start"]) < 1e-3:
        k += 1
    m = 0
    while m < min(len(go), len(gn)) - k and go[-1 - m]["sig"] == gn[-1 - m]["sig"]:
        m += 1
    cuts_new, cuts_old = new["cuts"], old["cuts"]
    same_groups = k == len(go) == len(gn)
    if same_groups:
        a, b_new = None, None
    else:
        a = gn[k]["out_start"] if k < len(gn) else new["total"]
        b_new = gn[len(gn) - m]["out_start"] if m else new["total"]
        b_old = go[len(go) - m]["out_start"] if m else old["total"]
    shift = (b_new - b_old) if not same_groups else 0.0
    why = []
    if not same_groups:
        why.append(f"shots {k + 1}-{len(gn) - m} changed")

    def snap(a, b_new):
        a = max([c for c in cuts_new if c <= a + 1e-6] or [0.0])
        b_new = min([c for c in cuts_new if c >= b_new - 1e-6] or [new["total"]])
        return a, b_new

    if a is not None:
        a, b_new = snap(a, b_new)
    for _ in range(20):
        # with the window known, the suffix shift is b_new - b_old; a cut in the new edit maps back by that shift
        b_old_ = (b_new - shift) if a is not None else None
        ws = []

        def region_ok(it, ref, sh):
            """Is item `it` (times in its own edit) outside the window and matched in the other edit?"""
            return any(r["sig"] == it["sig"] and abs(r["start"] - (it["start"] + sh)) < 1e-3
                       and abs(r["end"] - (it["end"] + sh)) < 1e-3 for r in ref)

        # Any item that touches a copied stretch (before `a` or after the window) must be in the other version
        # unchanged, at the same place in the picture; one that crosses a window edge is checked on both sides.
        for it in new["items"]:
            pre = a is None or it["start"] < a - 1e-6
            post = a is not None and it["end"] > b_new + 1e-6
            ok = (not pre or region_ok(it, old["items"], 0.0)) and (not post or region_ok(it, old["items"], -shift))
            if not ok:
                ws.append((it["start"], it["end"], it["kind"]))
        for it in old["items"]:
            pre = a is None or it["start"] < a - 1e-6
            post = a is not None and it["end"] > b_old_ + 1e-6
            ok = (not pre or region_ok(it, new["items"], 0.0)) and (not post or region_ok(it, new["items"], shift))
            if not ok:
                if a is None or it["end"] <= a + 1e-6:
                    ws.append((it["start"], it["end"], it["kind"] + " removed"))
                elif it["start"] >= b_old_ - 1e-6:
                    ws.append((it["start"] + shift, it["end"] + shift, it["kind"] + " removed"))
                else:
                    ws.append((min(it["start"], a), max(it["end"] + shift, b_new), it["kind"] + " removed"))
        grow = [(s, e, kind) for s, e, kind in ws if a is None or s < a - 1e-6 or e > b_new + 1e-6]
        if not grow:
            break
        lo = min(s for s, _, _ in grow)
        hi = max(e for _, e, _ in grow)
        why += sorted({f"{kind} at {s:.2f}-{e:.2f} s" for s, e, kind in grow})
        if a is None:
            a, b_new = snap(lo, hi)
        else:
            a, b_new = snap(min(a, lo), max(b_new, hi))
    else:
        return {"full": "could not settle the changed window"}
    if a is None:
        return {"copy": True, "why": ["only sound changed"]}
    b_old = b_new - shift
    if not any(abs(b_old - c) < 1e-3 for c in cuts_old) or not any(abs(a - c) < 1e-3 for c in cuts_old):
        return {"full": "the changed window does not start and end on cuts of the previous version"}
    if b_new - a > MAX_WINDOW_SHARE * new["total"]:
        return {"full": f"{b_new - a:.1f} s of {new['total']:.1f} s changed (over {int(MAX_WINDOW_SHARE * 100)} %)"}
    return {"a": round(a, 4), "b_new": round(b_new, 4), "b_old": round(b_old, 4), "why": why}


def keyframe_times(path):
    """Keyframe times of a video (to confirm the old file can be cut where the plan says)."""
    import subprocess
    p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-skip_frame", "nokey", "-show_entries",
                        "frame=pts_time", "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    return [float(x) for x in re.findall(r"[\d.]+", p.stdout)]
