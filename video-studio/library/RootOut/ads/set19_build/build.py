#!/usr/bin/env python3
"""RootOut Set 19 edit builder. Each row of the locked script is a list of pieces:
  talk(clip, a, b)                 video + its own lip-synced audio from a Seedance talking clip
  vo(file, a, b, shots)            ElevenLabs line (the script, verbatim) with b-roll shots cut on words
Shots: (source, src_in, cut_at) where cut_at is the VO time (s, relative to the vo file) where the NEXT shot starts.
Sources: AI clips (720x1280), Mixkit (16:9 -> centre crop), CC photos (Ken Burns), code graphics (1080x1920).
Writes work/build/<hook>/ pieces, out/<name>.mp4 (pre-finish, no captions) and work/build/<hook>/words.json (caption timing)."""
import json, subprocess, sys, os
from pathlib import Path

P = Path(__file__).resolve().parent.parent
W, H, FPS, AR = 1080, 1920, 30, 48000
CL, ST, VO, GF = P / "raw/gen/clips", P / "raw/stock", P / "raw/vo", P / "work/gfx"
PH = P / "assets/images"
WORDS = json.load(open(P / "work/vo_words.json"))


def run(cmd): subprocess.run(cmd, check=True)
def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout)


def w(name, word, occ=0, edge="end"):
    """time of a word in a VO file (start or end), by occurrence."""
    hits = [x for x in WORDS[name] if x[2].lower().strip(".,!?'\"").replace("’", "'") == word.lower()]
    x = hits[occ]; return x[1] if edge == "end" else x[0]


def vf_for(src):
    s = str(src)
    if s.endswith((".jpg", ".png")):
        return None
    probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height", "-of", "csv=p=0", s],
                           capture_output=True, text=True).stdout.split(",")
    wv, hv = int(probe[0]), int(probe[1])
    if wv > hv:  # landscape stock -> centre crop to 9:16
        return f"crop=ih*9/16:ih,scale={W}:{H}:flags=lanczos,setsar=1,fps={FPS}"
    return f"scale={W}:{H}:flags=lanczos,setsar=1,fps={FPS}"


def shot_clip(src, src_in, d, out, overlay=None, label=None, speed=1.0, blur=None):
    """render d seconds of video-only from src starting at src_in."""
    src = Path(src)
    if not src.exists():  # placeholder while a clip is still rendering
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", f"{d:.3f}", "-i", f"color=c=0x553333:s={W}x{H}:r={FPS}",
             "-vf", f"drawtext=fontfile=/usr/share/fonts/opentype/inter/Inter-Bold.otf:text='MISSING {src.stem}':fontsize=40:fontcolor=white:x=40:y=900",
             "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", str(out)]); return
    if str(src).endswith((".jpg", ".png")):  # Ken Burns on a photo
        n = int(d * FPS) + 2
        vf = (f"scale=2400:-2,crop='min(iw,ih*9/16)':'min(ih,iw*16/9)',zoompan=z='1.0+0.12*on/{n}':x='iw/2-(iw/zoom/2)':"
              f"y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},setsar=1")
        cmd = ["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(src), "-t", f"{d:.3f}", "-vf", vf]
    else:
        L = dur(src); src_in = max(0.0, min(src_in, max(0.0, L - 0.05)))
        vf = vf_for(src)
        if speed != 1.0: vf += f",setpts=PTS/{speed}"
        avail = (L - src_in) * speed
        if avail < d:  # hold the last frame
            vf += f",tpad=stop_mode=clone:stop_duration={d - avail + 0.1:.3f}"
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{src_in:.3f}", "-i", str(src), "-t", f"{d:.3f}", "-vf", vf]
    cmd += ["-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS), str(out)]
    run(cmd)
    if blur:
        y0, y1 = int(H * blur[0]), int(H * blur[1]); tmp = str(out) + ".b.mp4"; os.rename(out, tmp)
        run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-filter_complex",
             f"[0:v]split[a][b];[b]crop={W}:{y1 - y0}:0:{y0},boxblur=28:3[bl];[a][bl]overlay=0:{y0}",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", str(out)]); os.remove(tmp)
    if overlay or label:
        tmp = str(out) + ".o.mp4"; os.rename(out, tmp)
        inputs = ["-i", tmp]; fc = "[0:v]"
        chain = []
        if overlay:
            odir, ooff = overlay
            inputs += ["-framerate", str(FPS), "-i", str(GF / odir / "%04d.png")]
            chain.append(f"[1:v]format=rgba,setpts=PTS+{ooff}/TB[o];[0:v][o]overlay=0:0:eof_action=pass[v1]"); fc = "[v1]"
        if label:
            fontf = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
            chain.append(f"{fc}drawtext=fontfile={fontf}:text='{label}':x=w-tw-40:y=h-th-60:fontsize=30:fontcolor=white@0.9:"
                         f"box=1:boxcolor=black@0.35:boxborderw=12[v2]"); fc = "[v2]"
        run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(chain), "-map", fc, "-t", f"{d:.3f}",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS), str(out)])
        os.remove(tmp)


def audio_cut(src, a, b, out):
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-i", str(src), "-t", f"{b - a:.3f}", "-vn", "-ac", "2", "-ar", str(AR),
         "-af", "afade=t=in:d=0.02,areverse,afade=t=in:d=0.03,areverse", "-c:a", "pcm_s16le", str(out)])


def silence(d, out):
    run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", f"{d:.3f}", "-i", f"anullsrc=r={AR}:cl=stereo", "-c:a", "pcm_s16le", str(out)]); return out


def has_audio(src):
    return bool(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", str(src)],
                               capture_output=True, text=True).stdout.strip())


_AMB = [0]
def amb_clip(src, sin, d, gain):
    _AMB[0] += 1; out = P / f"work/build/_amb{os.getpid()}" / f"a{_AMB[0]:04d}.wav"; out.parent.mkdir(parents=True, exist_ok=True)
    if gain <= 0 or not Path(src).exists() or str(src).endswith((".jpg", ".png")) or not has_audio(src): return silence(d, out)
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{sin:.3f}", "-i", str(src), "-t", f"{d:.3f}", "-vn", "-ac", "2", "-ar", str(AR),
         "-af", f"apad,atrim=0:{d:.3f},volume={gain},afade=t=in:d=0.05,areverse,afade=t=in:d=0.08,areverse", "-c:a", "pcm_s16le", str(out)])
    return out


class Build:
    def __init__(self, name):
        self.name = name; self.dir = P / "work/build" / name; self.dir.mkdir(parents=True, exist_ok=True)
        self.parts = []; self.amb = []; self.n = 0; self.t = 0.0; self.words = []; self.nocap = []; self.captop = []  # caption-free zones

    def _p(self, ext): self.n += 1; return self.dir / f"p{self.n:03d}{ext}"

    def talk(self, clip, a, b, gap=0.0, label=None):
        """on-camera piece: video + own audio. Words from whisper of the clip are aligned later."""
        clip = CL / clip; d = b - a + gap
        v = self._p(".mp4"); shot_clip(clip, a, d, v, label=label)
        au = self._p(".wav"); audio_cut(clip, a, b, au)
        if gap: self._pad(au, gap)
        self.amb.append(silence(d, self._p(".wav")))
        self.parts.append((v, au, d)); self.words.append(("talk", str(clip), a, b, self.t)); self.t += d

    def vo(self, name, a, b, shots, gap=0.25, nocap=None):
        """VO piece: audio = VO file [a,b] + gap; shots: list of (src, src_in, cut_at_vo_time | None, opts)."""
        d = b - a + gap
        cuts = [a] + [s[2] for s in shots[:-1]] + [b + gap]
        vids, ambs = [], []
        for k, s in enumerate(shots):
            src, sin = s[0], s[1]; opts = s[3] if len(s) > 3 else {}
            sd = cuts[k + 1] - cuts[k]
            if sd <= 0.05: continue
            v = self._p(".mp4"); shot_clip(src, sin, sd, v, overlay=opts.get("overlay"), label=opts.get("label"), speed=opts.get("speed", 1.0), blur=opts.get("blur"))
            ambs.append(amb_clip(src, sin, sd, opts.get("amb", 0.0 if "/clips/t" in str(src) else 1.0)))
            vids.append(v)
            if opts.get("nocap"): self.nocap.append((self.t + cuts[k] - a, self.t + cuts[k + 1] - a))
            if opts.get("captop"): self.captop.append((self.t + cuts[k] - a, self.t + cuts[k + 1] - a))
        v = self._p(".mp4"); self._concat_v(vids, v)
        au = self._p(".wav"); audio_cut(VO / f"{name}.mp3", a, b, au)
        if gap: self._pad(au, gap)
        am = self._p(".wav"); lst = am.with_suffix(".txt"); lst.write_text("".join(f"file '{x}'\n" for x in ambs))
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:a", "pcm_s16le", str(am)])
        self.amb.append(am)
        self.parts.append((v, au, d)); self.words.append(("vo", name, a, b, self.t)); self.t += d

    def card(self, src, d):
        v = self._p(".mp4"); shot_clip(src, 0, d, v)
        au = self._p(".wav"); run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", f"{d:.3f}", "-i", f"anullsrc=r={AR}:cl=stereo", str(au)])
        self.amb.append(silence(d, self._p(".wav")))
        self.parts.append((v, au, d)); self.nocap.append((self.t, self.t + d)); self.t += d

    def _pad(self, au, gap):
        tmp = str(au) + ".t.wav"; os.rename(au, tmp)
        run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", f"apad=pad_dur={gap:.3f}", "-c:a", "pcm_s16le", str(au)]); os.remove(tmp)

    def _concat_v(self, vids, out):
        lst = out.with_suffix(".txt"); lst.write_text("".join(f"file '{x}'\n" for x in vids))
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(out)])

    def finish(self):
        vids = [p[0] for p in self.parts]; auds = [p[1] for p in self.parts]
        vcat = self.dir / "video.mp4"; self._concat_v(vids, vcat)
        lst = self.dir / "audio.txt"; lst.write_text("".join(f"file '{x}'\n" for x in auds))
        acat = self.dir / "voice.wav"
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:a", "pcm_s16le", str(acat)])
        lst = self.dir / "amb.txt"; lst.write_text("".join(f"file '{x}'\n" for x in self.amb))
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:a", "pcm_s16le", str(self.dir / "amb.wav")])
        json.dump({"pieces": self.words, "nocap": self.nocap, "captop": self.captop, "length": self.t}, open(self.dir / "timeline.json", "w"), indent=1)
        print(self.name, f"{self.t:.2f}s", "->", vcat)
        return vcat, acat
