"""Match an S7 VO take to her on-camera (voice-changed Seedance) audio: formant-preserving pitch shift + EQ curve."""
import sys, subprocess, numpy as np, librosa, soundfile as sf
from scipy.signal import firwin2, fftconvolve
src, out, st = sys.argv[1], sys.argv[2], float(sys.argv[3])
tmp = out + ".ps.wav"
subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-af", f"aresample=24000,rubberband=pitch={2 ** (st / 12):.5f}:formant=preserved:pitchq=quality", "-ac", "1", tmp], check=True)
y, sr = sf.read(tmp)
r = np.load("work/match/eq.npy"); f = np.linspace(0, sr / 2, len(r))
g = 20 * np.log10(np.clip(r, 1e-3, None)); g -= np.median(g[(f > 300) & (f < 3000)])
g = np.convolve(g, np.ones(25) / 25, mode="same"); g = np.clip(g * 0.7, -9, 9); g[f < 80] = -12   # gentle: 70% of the measured difference
fir = firwin2(1025, f / (sr / 2), 10 ** (g / 20)); z = fftconvolve(y, fir, mode="same")
z *= np.sqrt(np.mean(y ** 2) / np.mean(z ** 2)); sf.write(out, np.clip(z, -0.99, 0.99), sr)
