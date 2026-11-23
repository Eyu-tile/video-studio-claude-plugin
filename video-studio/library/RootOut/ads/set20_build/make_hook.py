#!/usr/bin/env python3
"""Build a Set 20 hook: mom talking clip, then a real black-dot photo card over the same clip (blurred, still playing),
hook text in the upper third. Usage: make_hook.py <talk.mp4> <vo.mp3> <cut_at_s> <photo.jpg> "<hook text, | = line break>" <out.mp4>
Rules: no frozen frames (background keeps playing), no on-screen credits/disclaimers, 1080x1920."""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

talk, vo, cut, photo, text, out = sys.argv[1:7]; cut = float(cut)
NEWS = str(Path.home() / ".fonts/Newsreader-SemiBold.ttf"); NAVY = (11, 42, 91)
tmp = Path(tempfile.mkdtemp())


def wrap(d, t, f, w):
    out, cur = [], ""
    for word in t.split():
        s = (cur + " " + word).strip()
        if d.textlength(s, font=f) <= w: cur = s
        else: out.append(cur); cur = word
    return out + [cur]


# hook text: white rounded box, navy Newsreader, upper third (house style, Set 17)
W, H = 1080, 1920; f = ImageFont.truetype(NEWS, 78)
im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
lines = [l for part in text.split('|') for l in wrap(d, part.strip(), f, W - 220)]; lh = 92; bw = max(d.textlength(l, font=f) for l in lines) + 90
y0 = 1330; x0 = (W - bw) / 2  # lower third: keeps her face clear, above platform UI
d.rounded_rectangle((x0, y0, x0 + bw, y0 + lh * len(lines) + 50), 34, fill=(255, 255, 255, 242))
for i, l in enumerate(lines):
    d.text(((W - d.textlength(l, font=f)) / 2, y0 + 22 + i * lh), l, font=f, fill=NAVY)
im.save(tmp / "hook.png")

# photo card: real photo, white border, rounded, soft shadow
p = Image.open(photo).convert("RGB"); cw = 900; p = p.resize((cw, int(p.height * cw / p.width)), Image.LANCZOS)
B = 18; card = Image.new("RGBA", (cw + 2 * B, p.height + 2 * B), (0, 0, 0, 0))
ImageDraw.Draw(card).rounded_rectangle((0, 0, card.width - 1, card.height - 1), 28, fill=(255, 255, 255, 255))
m = Image.new("L", p.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, p.width - 1, p.height - 1), 18, fill=255)
card.paste(p, (B, B), m)
sh = Image.new("RGBA", (card.width + 120, card.height + 120), (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle((60, 75, card.width + 60, card.height + 75), 28, fill=(0, 0, 0, 140))
sh = sh.filter(ImageFilter.GaussianBlur(22)); sh.paste(card, (60, 60), card); sh.save(tmp / "card.png")

dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", talk]))
vod = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", vo]))
end = min(dur, vod + 0.6); pd = end - cut
# simpler, explicit: show sharp clip before cut, blurred+card after
fc = (
    f"[0:v]scale=1080:1920:flags=lanczos,setsar=1,trim=0:{end},setpts=PTS-STARTPTS,split[a][b];"
    f"[b]gblur=sigma=28,eq=brightness=-0.06,trim={cut}:{end},setpts=PTS-STARTPTS[bl];"
    f"[2:v]format=rgba,scale=w='iw*(0.94+0.06*t/{pd:.2f})':h=-2:eval=frame[cd];"
    f"[bl][cd]overlay=x='(W-w)/2':y='(H-h)/2-120':shortest=1[pc];"
    f"[a]trim=0:{cut},setpts=PTS-STARTPTS[t0];"
    f"[t0][pc]concat=n=2:v=1:a=0[cat];"
    f"[cat][1:v]overlay=0:0[v]"
)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", talk, "-loop", "1", "-i", str(tmp / "hook.png"),
                "-loop", "1", "-framerate", "30", "-i", str(tmp / "card.png"), "-i", vo,
                "-filter_complex", fc, "-map", "[v]", "-map", "3:a", "-t", f"{end:.2f}", "-r", "30",
                "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                "-map_metadata", "-1", out], check=True)
print(out, f"{end:.2f}s, card from {cut}s")
