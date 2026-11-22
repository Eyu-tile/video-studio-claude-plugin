"""Visual evidence for sound placement: when the picture actually changes, how strongly, and where.

Research behind the numbers (see skills/video-sound-design/references/cue-sheet.md for citations):
- Timing comes from the frames, never from a vision-language model: VLM event centres were off by 0.66 s on average
  (Huang et al., MoSound, CHI 2026). Onset transfer from visual onsets beat generative Foley on timing
  (Du et al., CondFoleyGen, CVPR 2023).
- Peak picking follows Davis & Agrawala, "Visual Rhythm and Beat" (SIGGRAPH 2018): local mean over 0.1 s, local max
  over 0.15 s, a peak must stand 10 % of the global max above its local mean; the top 1 % is clipped to the 98th
  percentile so hard cuts do not flatten everything else. Here the envelope is the frame-difference energy of a
  small grey image (numpy only, CPU), which marks appearances, cuts and fast motion to the frame.
- Pan from where the change happens (Soundify, UIST 2023; MoSound), kept subtle (|pan| <= 0.5) for mono playback.
"""
import subprocess

import numpy as np

W, H = 96, 54


def video_fps(path):
    p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=avg_frame_rate",
                        "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    try:
        a, b = p.stdout.strip().split("/")
        return float(a) / float(b) if float(b) else 25.0
    except ValueError:
        return 25.0


def envelope(path):
    """Per-frame change energy, the x-centroid (0..1) of that change, and the frame rate.
    env[i] is the change that arrives on frame i (frame 0 = 0)."""
    fps = video_fps(path)
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-an", "-vf", f"scale={W}:{H},format=gray",
                        "-f", "rawvideo", "-"], capture_output=True)
    fr = np.frombuffer(p.stdout, np.uint8)
    n = len(fr) // (W * H)
    if n < 2:
        raise RuntimeError(f"could not read frames from {path}")
    fr = fr[: n * W * H].reshape(n, H, W).astype(np.float32)
    diff = np.abs(np.diff(fr, axis=0))
    env = np.concatenate([[0.0], diff.mean(axis=(1, 2))])
    col = diff.sum(axis=1)                                     # (n-1, W): where across the frame it changed
    tot = col.sum(axis=1)
    cx = np.concatenate([[0.5], np.where(tot > 0, (col * np.arange(W)).sum(axis=1) / np.maximum(tot, 1e-9) / (W - 1), 0.5)])
    hi, top = np.percentile(env, 98), np.percentile(env, 99)
    env = np.where(env > top, hi, env)
    env = env / env.max() if env.max() > 0 else env
    return env, cx, fps


def peaks(env, fps):
    """Davis & Agrawala impact rule: local max over 0.15 s that is >= 10 % of the global max above the 0.1 s local mean.
    Returns [(frame, prominence 0..1)]."""
    n = len(env)
    rm = max(1, int(round(0.1 * fps)) // 2)
    rx = max(1, int(round(0.15 * fps)) // 2)
    gmax = env.max() or 1.0
    out = []
    for i in range(1, n):
        lo, hi = max(0, i - rx), min(n, i + rx + 1)
        if env[i] < env[lo:hi].max() or env[i] == 0:
            continue
        mean = env[max(0, i - rm): min(n, i + rm + 1)].mean()
        if env[i] - mean >= 0.1 * gmax:
            out.append((i, float(min(1.0, (env[i] - mean) / gmax))))
    return out


# How far from the planned time the picture's own change may be, per cue (seconds before, after).
# Hits: animations start on or just after the planned time; transitions: the motion peak can sit anywhere in the move.
WINDOW = {"transition-fast": (0.35, 0.35), "transition-soft": (0.4, 0.4), "transition-dip": (0.3, 0.3),
          "transition-glitch": (0.3, 0.3), "cut-section": (0.1, 0.1), "cut": (0.1, 0.1), "scene": (0.1, 0.1)}
HIT_WINDOW = (0.12, 0.25)
NO_SNAP = {"beat", "riser"}  # beats follow the music; risers follow their reveal


def onset_near(env, t, fps, before, after):
    """First frame in the window where the picture clearly starts changing compared with the half second before it
    (baseline median + 4 x MAD): the frame a title, sticker or logo appears, even when it is small next to the cuts
    elsewhere in the video. Returns (time, strength, frame) or None."""
    i0, i1 = max(1, int(round((t - before) * fps))), min(len(env) - 1, int(round((t + after) * fps)))
    b0, b1 = max(0, i0 - int(0.5 * fps)), max(1, i0)
    base = env[b0:b1]
    if i1 <= i0 or len(base) < 3:
        return None
    med = float(np.median(base))
    mad = float(np.median(np.abs(base - med)))
    thr = med + 4 * mad + 1e-4
    for i in range(i0, i1 + 1):
        if env[i] > thr and env[min(i + 1, len(env) - 1)] > med:   # a rise that holds, not a one-frame flicker
            strength = float(min(1.0, (env[i:i + 3].max() - med) / (env.max() or 1)))
            return i / fps, max(strength, 0.05), i
    return None


ONSET_CUES = {"text", "text-big", "logo", "overlay", "chart", "type", "camera", "image"}  # things that appear


def snap(t, cue, pk, fps, env=None):
    """The picture's change for this cue: for things that appear, the first frame they appear (local onset);
    for transitions and cuts, the motion peak nearest the plan (Davis & Agrawala). (time, strength, frame) or None."""
    if cue in NO_SNAP:
        return None
    before, after = WINDOW.get(cue, HIT_WINDOW)
    if cue in ONSET_CUES and env is not None:
        hit = onset_near(env, t, fps, before, after)
        if hit:
            return hit
    cand = [(f / fps, p, f) for f, p in pk if t - before <= f / fps <= t + after]
    if not cand:
        return None
    # nearest wins; a much stronger change within one more frame wins over a weak nearer one
    return min(cand, key=lambda c: abs(c[0] - t) - (0.5 / fps if c[1] > 0.5 else 0))


def pan_at(cx, frame, k=0.5):
    """Constant-width pan from where the change happened: centre 0, edges +-k."""
    if frame is None or frame >= len(cx):
        return 0.0
    return round(float(np.clip((cx[frame] - 0.5) * 2 * k, -k, k)), 2)


def centroid_hz(path, seconds=0.3):
    """Spectral centroid of the loudest part of a sound: low = heavy/big, high = bright/small."""
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "22050", "-f", "s16le", "-"],
                       capture_output=True)
    x = np.frombuffer(p.stdout, "<i2").astype(np.float32)
    if len(x) < 512:
        return None
    hop = 1024
    e = np.array([np.square(x[i:i + hop]).sum() for i in range(0, len(x) - hop, hop)] or [0])
    i = int(e.argmax()) * hop
    seg = x[i: i + int(seconds * 22050)]
    if len(seg) < 512:
        seg = x[:int(seconds * 22050)]
    spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg))))
    f = np.fft.rfftfreq(len(seg), 1 / 22050)
    return round(float((spec * f).sum() / max(spec.sum(), 1e-9)), 0)
