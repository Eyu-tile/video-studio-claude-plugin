"""End-to-end tests for `vs render` on synthetic media (needs ffmpeg + numpy).

Run: python3 -m unittest discover -s tests -v
"""
import json
import re
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "video-studio"
TOOLS = PLUGIN / "tools"
sys.path.insert(0, str(TOOLS))
import numpy as np  # noqa: E402
from vs_common import probe, ramp_out, ramp_points, timeline  # noqa: E402

FPS = 25


def sh(*cmd, ok=True):
    p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if ok and p.returncode != 0:
        raise AssertionError(f"{' '.join(map(str, cmd))}\n{p.stdout}\n{p.stderr[-3000:]}")
    return p


def ff(*args):
    sh("ffmpeg", "-y", "-hide_banner", "-v", "error", *args)


class RenderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="vs-test-"))
        os.environ["VS_HASH_CACHE"] = str(cls.tmp / "hashes.json")
        cls.cwd = os.getcwd()
        os.chdir(cls.tmp)
        Path("raw").mkdir()
        Path("work").mkdir()
        # A: moving test pattern + 440 Hz. B: solid red + 880 Hz. Both 6 s.
        ff("-f", "lavfi", "-i", f"testsrc2=s=320x180:r={FPS}:d=6", "-f", "lavfi", "-i", "sine=f=440:d=6:r=48000",
           "-c:v", "libx264", "-g", "10", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", "raw/a.mp4")
        ff("-f", "lavfi", "-i", f"color=c=red:s=320x180:r={FPS}:d=6", "-f", "lavfi", "-i", "sine=f=880:d=6:r=48000",
           "-c:v", "libx264", "-g", "10", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", "raw/b.mp4")
        ff("-f", "lavfi", "-i", "sine=f=220:d=20:r=48000", "raw/music.wav")
        ff("-f", "lavfi", "-i", "anoisesrc=d=20:c=pink:a=0.2:r=48000", "raw/amb.wav")
        # Green-screen graphic: blue square on green.
        ff("-f", "lavfi", "-i", "color=c=0x00FF00:s=320x180:d=1", "-vf",
           "drawbox=x=120:y=50:w=80:h=80:color=blue:t=fill", "-frames:v", "1", "raw/gs.png")

    @classmethod
    def tearDownClass(cls):
        os.chdir(cls.cwd)
        shutil.rmtree(cls.tmp, ignore_errors=True)

    # helpers -------------------------------------------------------------------------------
    def render(self, edl, name, *extra):
        path = Path("work") / f"{name}.json"
        path.write_text(json.dumps(edl))
        out = Path("out") / f"{name}.mp4"
        if "--since" not in extra:   # these tests check full renders; revision reuse is tested on its own
            extra = (*extra, "--since", "none")
        p = sh(sys.executable, TOOLS / "render.py", path, "-o", out, *extra)
        return out, p

    def dur(self, f):
        return probe.__wrapped__(str(f))["duration"]

    def freq_at(self, f, t, win=0.2):
        p = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-t", f"{win}", "-i", str(f), "-ac", "1",
                            "-ar", "48000", "-f", "f32le", "-"], capture_output=True)
        x = np.frombuffer(p.stdout, dtype=np.float32)
        if len(x) < 256 or np.abs(x).max() < 1e-3:
            return 0.0
        spec = np.abs(np.fft.rfft(x * np.hanning(len(x))))
        return float(np.fft.rfftfreq(len(x), 1 / 48000)[spec.argmax()])

    def rms_at(self, f, t, win=0.3):
        p = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-t", f"{win}", "-i", str(f), "-ac", "1",
                            "-ar", "48000", "-f", "f32le", "-"], capture_output=True)
        x = np.frombuffer(p.stdout, dtype=np.float32)
        return float(np.sqrt(np.mean(x ** 2))) if len(x) else 0.0

    def pixel(self, f, t, x, y):
        p = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", str(f), "-frames:v", "1",
                            "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
        info = probe.__wrapped__(str(f))
        img = np.frombuffer(p.stdout, dtype=np.uint8).reshape(info["height"], info["width"], 3)
        return img[y, x].astype(int)

    def is_red(self, rgb):
        return rgb[0] > 180 and rgb[1] < 80 and rgb[2] < 80

    # tests ---------------------------------------------------------------------------------
    def test_basic_cuts_and_transition(self):
        edl = {"source": "raw/a.mp4", "segments": [
            {"start": 0, "end": 2}, {"src": "raw/b.mp4", "start": 1, "end": 3, "transition_in": {"type": "fade", "dur": 0.5}},
            {"start": 3, "end": 4}]}
        out, _ = self.render(edl, "basic", "--no-loudnorm")
        self.assertAlmostEqual(self.dur(out), 4.5, delta=0.08)
        self.assertTrue(self.is_red(self.pixel(out, 2.6, 160, 90)))

    def test_j_and_l_cuts(self):
        # A 0-2, then B with a 0.6 s J-cut lead; B has a 0.6 s L-cut tail into A again.
        edl = {"segments": [
            {"src": "raw/a.mp4", "start": 0, "end": 2},
            {"src": "raw/b.mp4", "start": 2, "end": 4, "audio_lead": 0.6, "audio_tail": 0.6},
            {"src": "raw/a.mp4", "start": 4, "end": 5.5}]}
        out, _ = self.render(edl, "jl", "--no-loudnorm")
        self.assertAlmostEqual(self.dur(out), 5.5, delta=0.08)
        # Picture is A before 2.0 but the audio is already B (880 Hz) from 1.4.
        self.assertFalse(self.is_red(self.pixel(out, 1.7, 160, 90)))
        self.assertAlmostEqual(self.freq_at(out, 1.55), 880, delta=30)
        self.assertAlmostEqual(self.freq_at(out, 0.8), 440, delta=30)
        # After the cut back to A at 4.0, B's audio continues until 4.6.
        self.assertFalse(self.is_red(self.pixel(out, 4.2, 160, 90)))
        self.assertAlmostEqual(self.freq_at(out, 4.2), 880, delta=30)
        self.assertAlmostEqual(self.freq_at(out, 5.0), 440, delta=30)

    def test_speed_ramp_reverse_freeze(self):
        ramp = [[0, 1], [1.5, 0.3], [3, 1]]
        edl = {"source": "raw/a.mp4", "segments": [
            {"start": 0, "end": 3, "speed": ramp},
            {"start": 1, "end": 3, "reverse": True},
            {"start": 4, "freeze": 1.0}]}
        expect = ramp_out(ramp_points({"speed": ramp}, 3), 3) + 2 + 1
        self.assertAlmostEqual(timeline(edl)[-1]["out_end"], expect, places=3)
        out, _ = self.render(edl, "ramp", "--no-loudnorm")
        self.assertAlmostEqual(self.dur(out), expect, delta=0.1)

    def test_keyframes_and_regions(self):
        edl = {"source": "raw/a.mp4", "segments": [
            {"start": 0, "end": 3, "kf": {"zoom": [[0, 1], [3, 1.5]], "x": [[0, 0.2], [3, 0.8]], "rotate": [[0, 0], [3, 4]]}},
            {"start": 3, "end": 5, "zoom": 1.2, "kf": {"x": [[0, 0], [2, 1]]}}],
            "blurs": [{"start": 0, "end": 5, "x": 0.1, "y": 0.1, "w": 0.3, "h": 0.3},
                      {"start": 1, "end": 4, "mode": "pixelate", "x": 0.6, "y": 0.5, "w": 0.3, "h": 0.4,
                       "kf": {"x": [[0, 0.5], [4, 0.6]]}}]}
        out, _ = self.render(edl, "kf", "--aspect", "9:16", "--no-loudnorm")
        info = probe.__wrapped__(str(out))
        self.assertEqual((info["width"], info["height"]), (1080, 1920))
        self.assertAlmostEqual(info["duration"], 5, delta=0.08)

    def test_chroma_key_overlay_with_motion(self):
        edl = {"segments": [{"src": "raw/b.mp4", "start": 0, "end": 3}],
               "overlays": [{"file": "raw/gs.png", "start": 0, "end": 3, "key": "green", "fit": True,
                             "fade_in": 0.2, "kf": {"x": [[0, 0], [1, 0]]}}]}
        out, _ = self.render(edl, "key", "--no-loudnorm")
        self.assertTrue(self.is_red(self.pixel(out, 1.5, 20, 20)))  # green keyed out: red shows through
        rgb = self.pixel(out, 1.5, 160, 90)
        self.assertGreater(rgb[2], 150)  # blue square stays

    def test_tracks_automation_and_ducking(self):
        edl = {"source": "raw/a.mp4", "segments": [{"start": 0, "end": 3, "mute": True}, {"start": 3, "end": 6}],
               "tracks": [{"name": "amb", "gain_db": -6, "gain": [[0, -40], [2.5, -6]],
                           "clips": [{"file": "raw/amb.wav", "at": 0, "loop": True}]},
                          {"name": "music", "duck": True, "gain_db": -6,
                           "clips": [{"file": "raw/music.wav", "at": 0.5, "dur": 5, "fade_out": 0.5}]}]}
        out, _ = self.render(edl, "tracks", "--no-loudnorm")
        self.assertAlmostEqual(self.dur(out), 6, delta=0.08)
        # Ambience automation: quiet at the start, loud by 2.5 s.
        self.assertLess(self.rms_at(out, 0.0, 0.3), self.rms_at(out, 2.6, 0.3))
        # Music before dialogue vs under dialogue: ducked.
        quiet = self.render({**edl, "tracks": [edl["tracks"][1]]}, "duck", "--no-loudnorm")[0]
        self.assertGreater(self.rms_at(quiet, 1.5), 0.01)

    def test_chunked_render_and_cache(self):
        segs = [{"src": "raw/a.mp4" if k % 2 == 0 else "raw/b.mp4", "start": 0.5 + 0.1 * k, "end": 2.5} for k in range(6)]
        edl = {"segments": segs, "music": {"file": "raw/music.wav", "gain_db": -20}}
        whole, _ = self.render(edl, "whole", "--chunks", "off", "--since", "none")
        chunked, p1 = self.render(edl, "chunked", "--chunks", "3", "--jobs", "2", "--since", "none")
        n = int(re.search(r"(\d+) chunks, 0 cached", p1.stderr).group(1))
        self.assertGreaterEqual(n, 2)
        self.assertAlmostEqual(self.dur(chunked), self.dur(whole), delta=0.08)
        edl["segments"][5]["end"] = 2.0  # change one shot: only its chunk re-renders
        _, p2 = self.render(edl, "chunked2", "--chunks", "3", "--jobs", "2", "--since", "none")
        m = re.search(r"(\d+) chunks, (\d+) cached, rendering (\d+)", p2.stderr)
        self.assertLessEqual(int(m.group(3)), 2, p2.stderr)    # the changed shot's chunk (and its neighbour at most)
        self.assertGreaterEqual(int(m.group(2)), 2, p2.stderr)

    def test_variants_share_body_chunks(self):
        """Two hooks of different lengths before the same body: the body splits at the same shots (chunk boundaries
        come from shot content, not time), so the second variant renders only its hook's chunk."""
        body = [{"src": "raw/a.mp4" if k % 2 == 0 else "raw/b.mp4", "start": 0.3 + 0.05 * k, "end": 1.9}
                for k in range(20)]
        h1 = {"segments": [{"src": "raw/b.mp4", "start": 0.0, "end": 1.3}] + body}
        h2 = {"segments": [{"src": "raw/a.mp4", "start": 0.2, "end": 2.9}] + body}
        _, p1 = self.render(h1, "var_h1", "--chunks", "3", "--since", "none")
        _, p2 = self.render(h2, "var_h2", "--chunks", "3", "--since", "none")
        n1 = int(re.search(r"(\d+) chunks, 0 cached", p1.stderr).group(1))
        m = re.search(r"(\d+) chunks, (\d+) cached", p2.stderr)
        self.assertGreaterEqual(n1, 3)
        self.assertGreaterEqual(int(m.group(2)), int(m.group(1)) - 2, p2.stderr)

    def test_same_content_new_file_is_unchanged(self):
        """A card rewritten with the same pixels (a script re-run) doesn't count as a change."""
        import shutil as sh_
        edl = {"segments": [{"src": "raw/a.mp4", "start": 0, "end": 2}],
               "overlays": [{"file": "work/card.png", "start": 0.2, "end": 1.5, "x": 10, "y": 10, "w": 200}]}
        sh_.copy("raw/gs.png", "work/card.png")
        self.render(edl, "card_v1", "--no-loudnorm")
        Path("work/card.png").unlink()
        sh_.copy("raw/gs.png", "work/card.png")    # new file, new mtime, same bytes
        _, p = self.render(edl, "card_v2", "--no-loudnorm", "--since", "auto")
        self.assertIn("picture unchanged", p.stderr + p.stdout)

    def test_ten_bit_and_stabilize(self):
        edl = {"source": "raw/a.mp4", "segments": [{"start": 0, "end": 2, "stabilize": True}]}
        out, _ = self.render(edl, "tenbit", "--codec", "h265", "--10bit", "--no-loudnorm")
        p = sh("ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=pix_fmt",
               "-of", "csv=p=0", out).stdout.strip()
        self.assertEqual(p, "yuv420p10le")

    def test_legacy_features(self):
        ff("-f", "lavfi", "-i", "sine=f=1000:d=0.3:r=48000", "raw/hit.wav")
        edl = {"source": "raw/a.mp4", "segments": [{"start": 0, "end": 2, "fit": "blur"}, {"start": 2, "end": 4, "zoom": 1.2}],
               "texts": [{"text": "HELLO", "start": 0.2, "end": 1.5, "pos": "top", "anim": "pop", "box": "#111111"}],
               "overlays": [{"file": "raw/gs.png", "start": 1, "end": 2, "w": 100, "x": "W-w-10", "y": 10, "opacity": 0.8}],
               "sfx": [{"file": "raw/hit.wav", "at": 2.0}], "grade": "cinematic", "audio": {"enhance": True},
               "music": {"file": "raw/music.wav", "gain_db": -20, "duck": True}}
        out, _ = self.render(edl, "legacy", "--preset", "reels")
        info = probe.__wrapped__(str(out))
        self.assertEqual((info["width"], info["height"]), (1080, 1920))
        self.assertAlmostEqual(info["duration"], 4, delta=0.08)
        edl2 = {"source": "raw/b.mp4", "segments": [{"start": 0, "end": 2}, {"start": 3, "end": 4}],
                "audio_track": {"src": "raw/music.wav", "start": 1}}
        out2, _ = self.render(edl2, "track", "--no-loudnorm")
        self.assertAlmostEqual(self.freq_at(out2, 1.0), 220, delta=20)

    def test_proxy_used_in_preview(self):
        sh(sys.executable, TOOLS / "proxy.py", "raw/a.mp4", "--height", "90")
        self.assertTrue(Path("raw/.proxy/a.mp4.mkv").exists())
        edl = {"source": "raw/a.mp4", "segments": [{"start": 1, "end": 3}]}
        out, _ = self.render(edl, "proxy", "--preview", "--no-loudnorm")
        self.assertAlmostEqual(self.dur(out), 2, delta=0.08)
        self.assertAlmostEqual(self.freq_at(out, 1.0), 440, delta=30)
        sh(sys.executable, TOOLS / "proxy.py", "raw/a.mp4", "--clean")
        self.assertFalse(Path("raw/.proxy").exists())


if __name__ == "__main__":
    unittest.main()
