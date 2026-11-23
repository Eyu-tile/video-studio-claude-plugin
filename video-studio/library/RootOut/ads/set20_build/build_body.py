#!/usr/bin/env python3
"""Set 20 body edit (beats 2-16 + end card). One "line" = one VO line (Juno, verbatim) or one lip-synced talking clip
(its own audio). Each line gets visuals that fill it exactly. House rules: no frozen frames (stills always move, clips
slowed no further than 0.7x), each b-roll source once, talking clips only under their own line, no on-screen
disclaimers/credits. Output: work/body/body.mp4 (1080x1920, 30 fps, VO only; music + captions in finish.py)."""
import json, subprocess, sys
from pathlib import Path

P = Path(__file__).resolve().parent.parent; L = Path("/home/user/video-studio-claude-plugin/video-studio/library/RootOut")
CL, RU, AU, BR, GX = P / "raw/gen/clips", P / "raw/reuse", P / "raw/gen/audio", P / "assets/broll", P / "assets/graphics"
TMP = P / "work/body"; TMP.mkdir(parents=True, exist_ok=True)
HOWTO = L / "resources/site_videos/shopify-ff701bf4.mp4"
W, H, FPS = 1080, 1920, 30
ENC = ["-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS)]


def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))


def run(args):
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", *args], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr)


COVER = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1"


def overlay_chain(ovs, base="[v0]"):
    """Static PNG overlays on a moving picture (inputs 1..n)."""
    s, cur = "", base
    for i, _ in enumerate(ovs):
        s += f";{cur}[{i + 1}:v]overlay=0:0[o{i}]"; cur = f"[o{i}]"
    return s, cur


def piece(kind, src, d, out, ss=0.0, ovs=(), crop=None):
    ovin = sum((["-loop", "1", "-i", str(o)] for o in ovs), [])
    if kind == "clip":
        avail = dur(src) - ss; f = min(1.0, avail / d)
        if f < 0.7: sys.exit(f"{src}: needs {d:.2f}s, has {avail:.2f}s (would freeze/over-slow)")
        pre = f"crop={crop}," if crop else ""
        g = f"[0:v]trim=start={ss},setpts=(PTS-STARTPTS)/{f:.4f},{pre}{COVER},fps={FPS}[v0]"
        s, cur = overlay_chain(ovs); run(["-i", str(src), *ovin, "-filter_complex", g + s, "-map", cur, "-t", f"{d:.3f}", "-an", *ENC, str(out)])
    elif kind == "photo":  # real still: blurred self as moving bg + card with slow push-in (no on-screen credit)
        n = int(d * FPS) + 2
        g = (f"[0:v]split[a][b];[a]scale=1600:-2,boxblur=30,eq=brightness=-0.05,{COVER},"
             f"zoompan=z='1+0.0008*on':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s={W}x{H}:fps={FPS}[bg];"
             f"[b]scale=980:-2,pad=iw+24:ih+24:12:12:white,format=rgba,loop=loop=-1:size=1:start=0,setpts=N/{FPS}/TB[c];"
             f"[c]scale=w='trunc(iw*(0.95+0.06*t/{d:.2f})/2)*2':h=-2:eval=frame[cs];"
             f"[bg][cs]overlay=x='(W-w)/2':y='(H-h)/2-80':shortest=1[v0]")
        s, cur = overlay_chain(ovs); run(["-i", str(src), *ovin, "-filter_complex", g + s, "-map", cur, "-t", f"{d:.3f}", *ENC, str(out)])
    elif kind == "photofull":  # big real still, full bleed with push-in
        n = int(d * FPS) + 2
        g = (f"[0:v]scale=1440:2560:force_original_aspect_ratio=increase,crop=1440:2560,setsar=1,"
             f"zoompan=z='1+0.0012*on':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s={W}x{H}:fps={FPS}[v0]")
        s, cur = overlay_chain(ovs); run(["-i", str(src), *ovin, "-filter_complex", g + s, "-map", cur, "-t", f"{d:.3f}", *ENC, str(out)])
    elif kind == "card":  # PNG card (screenshot/quote/comment) over the soft moving background
        g = (f"[0:v]{COVER}[bg];[1:v]format=rgba,scale=w='trunc(min(1000,iw)*(0.96+0.04*t/{d:.2f})/2)*2':h=-2:eval=frame[c];"
             f"[bg][c]overlay=x='(W-w)/2':y='(H-h)/2-60':shortest=1[v0]")
        ov2 = sum((["-loop", "1", "-i", str(o)] for o in ovs), [])
        s = ""; cur = "[v0]"
        for i, _ in enumerate(ovs):
            s += f";{cur}[{i + 2}:v]overlay=0:0[o{i}]"; cur = f"[o{i}]"
        run(["-stream_loop", "-1", "-i", str(GX / "bg_soft.mp4"), "-loop", "1", "-i", str(src), *ov2, "-filter_complex", g + s,
             "-map", cur, "-t", f"{d:.3f}", *ENC, str(out)])
    else:
        sys.exit(kind)


# --- the body, in script order. audio: ("clip", talking clip, cut_end) | ("vo", mp3). visuals: (kind, src, dur|None, opts)
ck = lambda n: GX / f"checklist_{n}.png"
B4, B8 = BR / "b04_check_macro", BR / "b08_dandelion"
LINES = [
    ("b02a", ("clip", CL / "t01.mp4", 5.0), [("clip", CL / "t01.mp4", 2.95, {}), ("clip", CL / "g02_walk.mp4", None, {})]),
    ("b02b", ("vo", AU / "vo02.mp3"), [("photo", B4 / "wm_plantar-wart-at-heel.jpg", 2.4, {}), ("photo", B4 / "wm_calluses.jpg", 2.0, {}),
                                       ("card", GX / "w2_pebbles_aad_card.png", None, {})]),
    ("b03", ("vo", AU / "vo03.mp3"), [("clip", CL / "g03_counter.mp4", 3.4, {}), ("photo", BR / "b03_pumice_tweezers/wm_pumice-stone.jpg", 2.6, {}),
                                      ("photo", BR / "b03_pumice_tweezers/wm_tweezers-variety.jpg", 2.4, {}), ("photo", B4 / "wm_a-callus.jpg", None, {})]),
    ("b04a", ("clip", CL / "t04.mp4", 5.0), [("clip", CL / "t04.mp4", None, {})]),
    ("b04b", ("vo", AU / "vo05.mp3"), [("photo", B4 / "wm_evolucion-de-un-callo.jpg", 3.4, {"ovs": [ck(0)]}),
                                       ("card", GX / "w1_dots_nhs_card.png", 3.4, {"ovs": [ck(1)]}),
                                       ("photofull", B4 / "wm_largeplanterwart.jpg", None, {"ovs": [ck(1)]})]),
    ("b04c", ("vo", AU / "vo06.mp3"), [("clip", CL / "g04_squeeze.mp4", 3.9, {"ovs": [ck(2)]}), ("photo", BR / "b07_sister_toe/wm_verruca-vulgaris-on-the-first-toe.jpg", None, {"ovs": [ck(2)]})]),
    ("b04d", ("vo", AU / "vo07.mp3"), [("photo", B4 / "wm_plantar-warts-1.jpg", 4.2, {"ovs": [ck(3)]}), ("photo", B4 / "wm_painful-plantar-warts.jpg", None, {"ovs": [ck(3)]})]),
    ("b05a", ("vo", AU / "vo08.mp3"), [("photo", B4 / "wm_painful-deep-plantar-wart.jpg", 1.7, {"ovs": [ck(3)]}), ("photo", B4 / "wm_deep-plantar-wart.jpg", 1.6, {"ovs": [ck(3)]}),
                                       ("photofull", B4 / "wm_large-plantar-warts.jpg", None, {"ovs": [ck(3)]})]),
    ("b05b", ("clip", CL / "t09.mp4", 4.0), [("clip", CL / "t09.mp4", 2.55, {}), ("clip", GX / "sidecut_root.mp4", None, {})]),
    ("b06a", ("clip", CL / "t10.mp4", 4.0), [("clip", CL / "t10.mp4", None, {})]),
    ("b06b", ("vo", AU / "vo11.mp3"), [("card", GX / "c_comment_card.png", None, {})]),
    ("b07", ("vo", AU / "vo12.mp3"), [("clip", CL / "g07_drawer.mp4", 4.6, {}), ("card", GX / "w3_nopick_aad_card.png", 3.4, {}),
                                      ("clip", CL / "g07_sister.mp4", 2.6, {}), ("photo", BR / "b07_sister_toe/wm_toe-plantar-wart-0147.jpg", 2.0, {}),
                                      ("card", GX / "c_study_card.png", None, {})]),
    ("b08a", ("clip", CL / "t13.mp4", 4.0), [("clip", CL / "t13.mp4", None, {})]),
    ("b08b", ("vo", AU / "vo14.mp3"), [("photo", BR / "b08_freeze/wm_wart-cryotherapy.jpg", 1.8, {}), ("clip", RU / "s1_dand_snap.mp4", 2.4, {}),
                                       ("photo", B8 / "wm_taraxacum-officinale-15-p-bot-tara-offi-62.jpg", 2.4, {}), ("clip", RU / "s1_dand_back.mp4", None, {})]),
    ("b09a", ("clip", CL / "t15.mp4", 5.0), [("clip", CL / "t15.mp4", 1.9, {}), ("clip", GX / "sidecut_arrows.mp4", None, {})]),
    ("b09b", ("vo", AU / "vo16.mp3"), [("clip", RU / "s1_dand_root.mp4", None, {})]),
    ("b10a", ("clip", CL / "t17.mp4", 5.0), [("clip", CL / "t17.mp4", None, {})]),
    ("b10b", ("vo", AU / "vo18.mp3"), [("clip", RU / "s19_skin_lemon.mp4", 5.2, {}), ("clip", RU / "s19_skin_teatree.mp4", 6.2, {"ovs": [GX / "gauge_8x.png"]}),
                                       ("clip", GX / "sidecut_break.mp4", None, {})]),
    ("b11", ("vo", AU / "vo19.mp3"), [("clip", RU / "s19_socks_bed.mp4", 5.0, {}), ("photofull", L / "brand/images/pdp/A01-bottle-front-white.jpg", 3.0, {}),
                                      ("card", GX / "q_flinch_card.png", None, {})]),
    ("b12", ("vo", AU / "vo20.mp3"), [("clip", RU / "s19_file_kid.mp4", 4.4, {}),
                                      ("clip", HOWTO, 2.6, {"ss": 2.35, "crop": "560:1000:190:80"}),
                                      ("clip", HOWTO, 2.4, {"ss": 4.75, "crop": "560:1000:260:80"}),
                                      ("clip", CL / "g12_feetup.mp4", None, {})]),
    ("b13", ("vo", AU / "vo21.mp3"), [("clip", GX / "calendar.mp4", 3.9, {}), ("card", GX / "q_dots_card.png", None, {})]),
    ("b14", ("vo", AU / "vo22.mp3"), [("clip", CL / "g14_run.mp4", None, {})]),
    ("b15", ("clip", CL / "t23.mp4", 8.0), [("clip", CL / "t23.mp4", None, {})]),
    ("b16a", ("clip", CL / "t24.mp4", 6.0), [("clip", CL / "t24.mp4", None, {})]),
    ("b16b", ("vo", AU / "vo25.mp3"), [("clip", RU / "s19_three_bottles.mp4", None, {"ovs": [GX / "offer.png"]})]),
    ("b16c", ("vo", AU / "vo26.mp3"), [("clip", GX / "endcard.mp4", None, {})]),
]
LEAD, TAIL = 0.08, 0.22


def build_line(i, name, audio, vis):
    kind, src = audio[0], audio[1]
    if kind == "clip":
        slot = min(dur(src), audio[2])
    else:
        slot = LEAD + dur(src) + TAIL
    if name == "b16c": slot += 2.6  # end card holds after "The link is right below."
    fixed = sum(v[2] for v in vis if v[2]); free = [v for v in vis if v[2] is None]
    rest = slot - fixed
    if rest < 0.5 and free: sys.exit(f"{name}: fixed visuals {fixed:.2f}s leave {rest:.2f}s in a {slot:.2f}s slot")
    parts = []
    for j, (k, s, d, o) in enumerate(vis):
        d = d or rest / len(free); out = TMP / f"{i:02d}_{name}_{j}.mp4"
        piece(k, s, d, out, ss=o.get("ss", 0.0), ovs=o.get("ovs", ()), crop=o.get("crop")); parts.append(out)
    ins = sum((["-i", str(p)] for p in parts), [])
    vcat = "".join(f"[{j}:v]" for j in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[v]"
    na = len(parts)
    if kind == "clip":
        a = f"[{na}:a]atrim=0:{slot:.3f},asetpts=PTS-STARTPTS,afade=t=out:st={slot - 0.06:.3f}:d=0.06[a]"
    else:
        a = f"[{na}:a]adelay={int(LEAD * 1000)}|{int(LEAD * 1000)},apad,atrim=0:{slot:.3f}[a]"
    out = TMP / f"line_{i:02d}_{name}.mp4"
    run([*ins, "-i", str(src), "-filter_complex", f"{vcat};{a}", "-map", "[v]", "-map", "[a]", "-t", f"{slot:.3f}",
         *ENC, "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(out)])
    return out, slot


if __name__ == "__main__":
    only = set(sys.argv[1:])
    outs, t, log = [], 0.0, []
    for i, (name, audio, vis) in enumerate(LINES):
        out = TMP / f"line_{i:02d}_{name}.mp4"
        if only and name not in only and out.exists():
            d = dur(out)
        else:
            out, d = build_line(i, name, audio, vis)
        log.append({"line": name, "start": round(t, 2), "dur": round(d, 2)}); outs.append(out); t += d
        print(f"{name:5s} {t - d:7.2f} +{d:5.2f}")
    (TMP / "list.txt").write_text("".join(f"file '{o}'\n" for o in outs))
    run(["-f", "concat", "-safe", "0", "-i", str(TMP / "list.txt"), "-c", "copy", str(TMP / "body.mp4")])
    json.dump(log, open(TMP / "timeline.json", "w"), indent=1)
    print("body", round(t, 2), "s ->", TMP / "body.mp4")
