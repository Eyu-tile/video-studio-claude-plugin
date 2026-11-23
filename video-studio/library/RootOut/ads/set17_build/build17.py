#!/usr/bin/env python3
"""Set 17 H1 edit: VO lines in script order, each line's pictures as segments (take cut-outs, real b-roll, web cards,
graphics). Every segment is normalised to 720x1280/30 fps, concatenated, then VO + room tone + music are mixed.
Usage: python3 work/build17.py [h1]"""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parent.parent; W = P / "work"; SEG = W / f"seg_{(sys.argv[1:] or ["h1"])[0]}"; SEG.mkdir(exist_ok=True)
SRC = json.load(open(W / "sources.json"))           # name -> {"path":..., "in": optional offset}
LS = json.load(open(W / "lipsync_map.json")); VOW = json.load(open(W / "vo_words.json"))
GAP = 0.18                                            # breath between turns
def sh(c): subprocess.run(c, shell=True, check=True)
def dur(p): return float(subprocess.check_output(f"ffprobe -v error -show_entries format=duration -of csv=p=0 '{p}'", shell=True))
def take(t, line, k=0):
    m = [x for x in LS[t] if x["line"] == line][k]; return m["take_in"], m["take_out"]
VOF = {n: (P / f"raw/vo/{n}.wav" if n in ("L16fix", "L03b") else P / f"raw/vo/{n}.mp3") for n in
       [f"L{i:02d}" for i in range(1, 19) if i != 16] + ["L16fix", "L03b", "Lh2a", "Lh2b", "Lh3a", "Lh3b"]}
HOOK = (sys.argv[1:] or ["h1"])[0]

# Each line: (vo, [ (seconds_into_line, source, src_in, card) ... ]) — a segment runs until the next one starts (or line end).
# source "D1"/"D2"/"M1" = lip-sync take, src_in = take time that lines up with seconds_into_line.
def T(t, line, k=0, at=0.0): a, _ = take(t, line, k); return a - at   # take offset so line time `at` maps to the take
LINES = [
 ("L01", [(0, "D1", T("D1", "L01"), None)]),
 ("L02", [(0, "M1", T("M1", "L02"), None), (1.55, "p_sole", 0, None)]),
 ("L03", [(0, "D1", T("D1", "L03"), None), (1.35, "x2_freeze", None, None), (5.45, "dand_snap", None, None), (7.2, "x3_cutaway", None, None)]),
 ("L04", [(0, "M1", T("M1", "L04"), None), (2.3, "b1", 0.0, None)]),
 ("L05", [(0, "D1", T("D1", "L05"), None), (2.0, "lemon", None, None), (2.75, "x4_lemon", None, None)]),
 ("L06", [(0, "M1", T("M1", "L06"), None)]),
 ("L07", [(0, "D1", T("D1", "L07"), None), (3.4, "cream", None, None), (4.0, "x5_tea", None, None), (8.3, "towels", None, None)]),
 ("L08", [(0, "b1", 4.0, "w_wiki_pain")]),
 ("L09", [(0, "D1", T("D1", "L09"), None), (1.9, "x6_root", None, None)]),
 ("L10", [(0, "M1", T("M1", "L10"), None), (0.95, "p_heel", 0.2, None)]),
 ("L11", [(0, "D1", T("D1", "L11"), None), (2.0, "blurD1", 0, "w_pubmed_result"), (5.4, "blurD1", 3.4, "w_pubmed_zoom"), (9.0, "kids_feet", None, None),
          (10.2, "D1", T("D1", "L11", 1, at=10.3), None)]),
 ("L12", [(0, "M1", T("M1", "L12"), None)]),
 ("L13", [(0, "D1", T("D1", "L13"), None), (4.1, "b1", 6.0, None), (6.5, "kids_feet2", None, None)]),
 ("L14", [(0, "M1", T("M1", "L14"), None)]),
 ("L15", [(0, "D2", T("D2", "L15"), None)]),
 ("L16fix", [(0, "b2", 0.0, None), (3.1, "b2", 3.0, None), (6.0, "b2", 7.0, None), (7.8, "x8_night", None, None),
             (9.15, "D2", T("D2", "L16fix", at=9.15), None)]),
 ("L17", [(0, "D2", T("D2", "L17"), None), (2.45, "x9_product", None, None)]),
 ("L18", [(0, "D2", T("D2", "L18"), None), (2.6, "x10_cta", None, None)]),
]
TAIL = 2.8   # the CTA shot holds after the last line (no separate end card)

from lipwarp import warp
def exact(out, d):
    """Force exactly round(d*30) frames (pad by cloning the last frame, or cut)."""
    n = int(round(d * 30)); tmp = f"{out}.x.mp4"
    sh(f"ffmpeg -v error -y -i {out} -vf tpad=stop_mode=clone:stop_duration=1,fps=30 -frames:v {n} -c:v libx264 -crf 16 -preset veryfast {tmp} && mv {tmp} {out}")
def norm(name, src, a, d, out, card=None, blur=False):
    if src in ("D1", "D2", "M1", "MH", "DH") and not card and not blur:
        warp(src, a, a + d, out); exact(out, d); return
    s = SRC[src]; p = P / s["path"] if not s["path"].startswith("/") else Path(s["path"])
    a = s.get("in", 0.0) if a is None else a
    vf = "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1,fps=30"
    if s.get("crop"): vf = s["crop"] + "," + vf
    if blur: vf += ",boxblur=18:2,eq=brightness=-0.06"
    vid = p.suffix in (".mp4", ".webm", ".mov", ".ogv")
    inp = f"-ss {a:.3f} -t {d:.3f} -i '{p}'" if vid else f"-loop 1 -framerate 30 -t {d:.3f} -i '{p}'"
    if not vid and s.get("kb"):
        n = int(d * 30) + 1
        vf = ("scale=1440:2560:force_original_aspect_ratio=increase,crop=1440:2560,"
              f"zoompan=z='1+0.10*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=720x1280:fps=30,setsar=1")
    if card:
        c = P / f"assets/graphics/{card}_card.png"
        ov = ("[1]scale=660:-1[c];[v][c]overlay=(W-w)/2:'if(lt(h,1150),(H-h)/2,(H-h)/2-(h-1150)/2*sin(min(t/%.2f,1)*PI/2)*2+ (h-1150)/2)':shortest=1" % max(d - 1.0, 1.0))
        fc = f"[0]{vf}[v];{ov},format=yuv420p"
        sh(f"ffmpeg -v error -y {inp} -loop 1 -i '{c}' -filter_complex \"{fc}\" -t {d:.3f} -an -c:v libx264 -crf 17 -preset veryfast {out}")
    else:
        sh(f"ffmpeg -v error -y {inp} -vf \"{vf},format=yuv420p\" -t {d:.3f} -an -c:v libx264 -crf 17 -preset veryfast {out}")
    exact(out, d)
    return
    got = dur(out)
    if got < d - 0.05:  # source too short: freeze the last frame to fill
        sh(f"ffmpeg -v error -y -i {out} -vf tpad=stop_mode=clone:stop_duration={d-got+0.1:.3f} -t {d:.3f} -c:v libx264 -crf 17 -preset veryfast {out}.tmp.mp4 && mv {out}.tmp.mp4 {out}")

def hook_lines():
    if HOOK == "h2":   # mom's line + doctor's "That sounds like the root.", then row 2 from "Freezing, acid and shaving…"
        return [("Lh2a", [(0, "MH", T("MH", "Lh2a"), None)]), ("Lh2b", [(0, "DH", T("DH", "Lh2b"), None)]),
                ("L03b", [(0, "x2_freeze", 0.0, None), (3.85, "dand_snap", None, None), (5.6, "x3_cutaway", None, None)])] + LINES[3:]
    if HOOK == "h3":
        return [("Lh3a", [(0, "MH", T("MH", "Lh3a"), None)]), ("Lh3b", [(0, "DH", T("DH", "Lh3b"), None)])] + LINES[2:]
    return LINES
def main():
    t = 0.0; segs = []; vo = []; LINES_ = hook_lines()
    for li, (line, plan) in enumerate(LINES_):
        ld = dur(VOF[line]) - 0.12; vo.append((line, t))
        for k, (at, src, a, card) in enumerate(plan):
            end = plan[k + 1][0] if k + 1 < len(plan) else ld + GAP + (TAIL if li == len(LINES_) - 1 else 0)
            qs, qe = round((t + at) * 30) / 30, round((t + end) * 30) / 30   # snap cuts to the frame grid: no drift
            d = qe - qs; blur = src.startswith("blur")
            if a is not None and src in ("D1", "D2", "M1", "MH", "DH") : a += qs - (t + at)
            srcn = src[4:] if blur else src
            out = SEG / f"{li:02d}_{k}_{src}.mp4"; norm(line, srcn, a, d, out, card, blur); segs.append(out)
        t += ld + GAP
    total = t + TAIL
    (SEG / "list.txt").write_text("".join(f"file '{s.name}'\n" for s in segs))
    sh(f"cd {SEG} && ffmpeg -v error -y -f concat -safe 0 -i list.txt -c copy {W}/{HOOK}_video.mp4")
    json.dump(vo, open(W / f"{HOOK}_vo_times.json", "w"))
    # audio: VO lines at their times, room tone, music bed ducked
    ins = " ".join(f"-i '{VOF[n]}'" for n, _ in vo); fl = []
    for k, (n, st) in enumerate(vo): fl.append(f"[{k}]aresample=48000,aformat=channel_layouts=mono,adelay={int(st*1000)}|{int(st*1000)},volume=1.0[v{k}]")
    nv = len(vo); mus = P / "raw/music/Wallpaper.mp3"
    fl.append(f"anoisesrc=d={total:.2f}:c=pink:a=0.02,lowpass=f=900,highpass=f=80,volume=0.35[rt]")
    fl.append(f"[{nv}]atrim=0:{total:.2f},afade=t=in:d=1.5,afade=t=out:st={total-2.5:.2f}:d=2.5,volume=0.11[mu]")
    fl.append("".join(f"[v{k}]" for k in range(nv)) + f"amix=inputs={nv}:normalize=0[vo]")
    fl.append("[vo][rt][mu]amix=inputs=3:normalize=0,aformat=channel_layouts=stereo[a]")
    sh(f"ffmpeg -v error -y {ins} -i '{mus}' -filter_complex \"{';'.join(fl)}\" -map [a] -t {total:.2f} -c:a pcm_s16le {W}/{HOOK}_audio.wav")
    print("total", round(total, 2))
if __name__ == "__main__": main()
