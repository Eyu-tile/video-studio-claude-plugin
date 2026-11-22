#!/usr/bin/env python3
"""Background music that fits the edit.

  vs music analyze <track>                      BPM, downbeats, loudness, energy sections (intro / body / outro)
  vs music fit <track> --length 47.5 -o work/music_fit.wav [--start auto|12.0] [--edl work/edl.json]
      Makes the track exactly the edit length, cutting on downbeats so it sounds composed:
      - longer than the edit: keeps the opening and the real ending, removes whole bars from the middle
        (one 60 ms crossfade on a downbeat) so the song ends on its own ending, on the last frame
      - shorter than the edit: loops whole bars of the body with crossfades, then plays the ending
      With --edl, the length is the EDL's output length and the EDL gets a `music` entry.

Use with any track: from `vs fetch search --type music`, a GitHub pack, or the person's own file.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vs_common import die, fmt_ts, load_json, need, need_numpy, probe, run, save_json, total_duration  # noqa: E402

XF = 0.06  # crossfade at a downbeat


def energy(path, rate=10):
    np = need_numpy()
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "8000", "-f", "f32le", "-"],
                         capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    per = 8000 // rate
    n = x.size // per
    return np.sqrt((x[: n * per].reshape(n, per) ** 2).mean(axis=1)), rate


def loudness(path):
    p = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af", "ebur128", "-f", "null", "-"])
    m = re.search(r"I:\s+(-?[\d.]+) LUFS", p.stderr[p.stderr.rfind("Summary:"):])
    return float(m.group(1)) if m else None


def analyze(path):
    from beats import detect
    b = detect(path)
    e, rate = energy(path)
    np = need_numpy()
    dur = probe(path)["duration"]
    smooth = np.convolve(e, np.ones(rate * 2) / (rate * 2), mode="same")
    thr = 0.6 * np.percentile(smooth, 80)
    loud = np.where(smooth > thr)[0]
    body_start = loud[0] / rate if loud.size else 0.0
    body_end = loud[-1] / rate if loud.size else dur
    return {"duration": dur, "bpm": b["bpm"], "beats": b["beats"], "downbeats": b["downbeats"],
            "lufs": loudness(path), "intro_end": round(body_start, 2), "outro_start": round(body_end, 2)}


def nearest(xs, t):
    return min(xs, key=lambda x: abs(x - t)) if xs else t


def fit(path, length, start, out):
    need("ffmpeg")
    an = analyze(path)
    db = an["downbeats"] or an["beats"]
    dur = an["duration"]
    s0 = (db[0] if db and db[0] < 4 else 0.0) if start == "auto" else float(start)
    pieces = []  # (from, to) source ranges joined with crossfades on downbeats
    if dur - s0 >= length:
        # Cut out whole bars from the middle so the real ending lands on the last frame.
        tail_start = dur - (length - 0)  # where the tail would need to start if we only kept the ending
        if tail_start <= s0 + 0.01:
            pieces = [(s0, s0 + length)]
        else:
            # keep [s0, a] + [b, dur] with a, b on downbeats, (a - s0) + (dur - b) ≈ length
            best = None
            for a_ in [d for d in db if s0 + 4 <= d <= dur - 4]:
                b_ = nearest([d for d in db if d > a_], dur - (length - (a_ - s0)))
                if b_ <= a_:
                    continue
                err = abs((a_ - s0) + (dur - b_) - length)
                # prefer a long opening section and the cut inside the body, not in the intro/outro
                penalty = err + (0.5 if a_ < an["intro_end"] or b_ > an["outro_start"] else 0)
                if best is None or penalty < best[0]:
                    best = (penalty, a_, b_)
            pieces = [(s0, best[1]), (best[2], dur)] if best else [(dur - length, dur)]
    else:
        # Loop whole bars of the body, then the ending.
        body = [d for d in db if an["intro_end"] - 0.5 <= d <= an["outro_start"]]
        l0, l1 = (body[0], body[-1]) if len(body) >= 2 else (s0, dur)
        pieces = [(s0, l1)]
        total = l1 - s0
        tail = dur - l1
        while total + tail < length - 0.05 and l1 - l0 > 1:
            pieces.append((l0, l1))
            total += l1 - l0 - XF
        pieces.append((l1, dur))
    ins, filt = [], []
    for i, (a_, b_) in enumerate(pieces):
        ins += ["-ss", f"{a_:.3f}", "-t", f"{b_ - a_:.3f}", "-i", path]
        filt.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS[p{i}]")
    cur = "p0"
    for i in range(1, len(pieces)):
        filt.append(f"[{cur}][p{i}]acrossfade=d={XF}:c1=tri:c2=tri[x{i}]")
        cur = f"x{i}"
    # exact length: pad if short; a 1.5 s fade only when the natural ending would overrun the edit
    natural = sum(b_ - a_ for a_, b_ in pieces) - XF * (len(pieces) - 1)
    fo = 1.5 if natural > length + 0.25 else 0.15
    filt.append(f"[{cur}]apad,atrim=0:{length:.3f},afade=t=out:st={max(length - fo, 0):.3f}:d={fo}[out]")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    run(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", ";".join(filt), "-map", "[out]",
         "-c:a", "pcm_s16le", out])
    return an, pieces


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    z = sub.add_parser("analyze")
    z.add_argument("track")
    z.add_argument("-o", "--out")
    f = sub.add_parser("fit")
    f.add_argument("track")
    f.add_argument("--length", type=float, help="seconds (default: the --edl output length)")
    f.add_argument("--edl", help="EDL to fit; also adds/updates its `music` entry")
    f.add_argument("--start", default="auto", help="'auto' (first downbeat) or seconds into the track")
    f.add_argument("--gain-db", type=float, help="music level in the EDL entry (default -20 with dialogue, -8 without)")
    f.add_argument("--no-duck", action="store_true")
    f.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    if a.cmd == "analyze":
        an = analyze(a.track)
        print(f"{Path(a.track).name}: {fmt_ts(an['duration'])}, {an['bpm']} BPM, {an['lufs']} LUFS, "
              f"intro to {an['intro_end']}s, outro from {an['outro_start']}s, {len(an['downbeats'])} downbeats")
        if a.out:
            save_json(a.out, an)
        return
    edl = load_json(a.edl) if a.edl else None
    length = a.length or (total_duration(edl) if edl else None)
    if not length:
        die("give --length or --edl")
    an, pieces = fit(a.track, length, a.start, a.out)
    plan = " + ".join(f"{fmt_ts(x)}–{fmt_ts(y)}" for x, y in pieces)
    print(f"fitted {Path(a.track).name} ({an['bpm']} BPM) to {fmt_ts(length)}: {plan} -> {a.out}")
    if edl is not None:
        has_voice = not edl.get("audio_track") and any(not s.get("mute") for s in edl["segments"])
        gain = a.gain_db if a.gain_db is not None else (-20 if has_voice else -8)
        edl["music"] = {"file": a.out, "gain_db": gain, "duck": has_voice and not a.no_duck, "start": 0, "fade_out": 0.01}
        save_json(a.edl, edl)
        print(f"EDL music entry set: gain {gain} dB, duck {edl['music']['duck']} -> {a.edl}")


if __name__ == "__main__":
    main()
