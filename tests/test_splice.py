"""Revision renders (`vs render --since`): the change window between cuts, shifted suffixes, timed items, audio-only
revisions, fallbacks, and a real splice checked against a full render (needs ffmpeg).

Run: python3 -m unittest discover -s tests -v
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VS = ROOT / "plugins" / "video-studio" / "bin" / "vs"
sys.path.insert(0, str(ROOT / "plugins" / "video-studio" / "tools"))
import splice  # noqa: E402


def man(shots, texts=(), total=None, settings=None, glob="g"):
    """A manifest by hand: shots = [(sig, length)], texts = [(start, end, sig)]."""
    gs, t = [], 0.0
    for sig, ln in shots:
        gs.append({"sig": sig, "out_start": round(t, 4), "out_end": round(t + ln, 4), "overlap": 0.0})
        t += ln
    total = total or round(t, 4)
    return {"version": 1, "settings": settings or {"W": 1}, "globals": glob, "total": total, "groups": gs,
            "items": [{"kind": "texts", "start": s, "end": e, "sig": g} for s, e, g in texts],
            "cuts": splice.cuts_of(gs, total)}


SHOTS = [(c, 2.0) for c in "abcdefghij"]   # 10 shots x 2 s


class PlanTest(unittest.TestCase):
    def test_one_shot_changed(self):
        new = [s if s[0] != "e" else ("E", 2.0) for s in SHOTS]
        p = splice.plan(man(SHOTS), man(new))
        self.assertEqual((p["a"], p["b_new"], p["b_old"]), (8.0, 10.0, 10.0))

    def test_trim_shifts_the_suffix(self):
        new = [s if s[0] != "c" else ("C", 1.2) for s in SHOTS]                  # shot 3 shortened by 0.8 s
        texts_old = [(0.5, 1.5, "hook"), (17.0, 19.0, "cta")]
        texts_new = [(0.5, 1.5, "hook"), (16.2, 18.2, "cta")]                       # the CTA moved with the picture
        p = splice.plan(man(SHOTS, texts_old), man(new, texts_new))
        self.assertEqual((p["a"], p["b_new"], p["b_old"]), (4.0, 5.2, 6.0))       # only shot 3 re-encoded

    def test_text_change_widens_to_its_cuts(self):
        p = splice.plan(man(SHOTS, [(15.0, 19.5, "cta")]), man(SHOTS, [(15.0, 19.5, "CTA v2")]))
        self.assertEqual((p["a"], p["b_new"]), (14.0, 20.0))
        self.assertTrue(any("texts" in w for w in p["why"]))

    def test_text_crossing_the_window_widens_it(self):
        new = [s if s[0] != "e" else ("E", 2.0) for s in SHOTS]                  # shot 5 (8-10 s) changed
        old_t, new_t = [(7.0, 11.5, "lower third")], [(7.0, 11.5, "lower third v2")]
        p = splice.plan(man(SHOTS, old_t), man(new, new_t))
        self.assertEqual((p["a"], p["b_new"]), (6.0, 12.0))

    def test_audio_only_copies_the_picture(self):
        self.assertTrue(splice.plan(man(SHOTS), man(SHOTS)).get("copy"))

    def test_fallbacks(self):
        self.assertIn("full", splice.plan(man(SHOTS), man(SHOTS, settings={"W": 2})))
        self.assertIn("full", splice.plan(man(SHOTS), man(SHOTS, glob="graded")))
        most = [(c.upper(), 2.0) if i < 7 else (c, 2.0) for i, (c, _) in enumerate(SHOTS)]
        self.assertIn("over 60 %", splice.plan(man(SHOTS), man(most))["full"])

    def test_transition_is_never_split(self):
        old, new = man(SHOTS), man([s if s[0] != "e" else ("E", 2.0) for s in SHOTS])
        for m in (old, new):                                                       # a dissolve into shot 5 (at 8 s)
            m["groups"][4]["overlap"] = 0.5
            m["cuts"] = splice.cuts_of(m["groups"], m["total"])
        p = splice.plan(old, new)
        self.assertEqual((p["a"], p["b_new"]), (6.0, 10.0))                        # widened to the cut before it


def sh(*cmd, ok=True, cwd=None):
    p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, cwd=cwd)
    if ok and p.returncode != 0:
        raise AssertionError(f"{' '.join(map(str, cmd))}\n{p.stdout}\n{p.stderr[-2500:]}")
    return p


class SpliceRenderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="vs-splice-"))
        os.environ["VS_HASH_CACHE"] = str(cls.tmp / "hashes.json")
        sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "testsrc2=s=320x180:r=25:d=30", "-f", "lavfi",
           "-i", "sine=f=330:d=30", "-shortest", "-c:v", "libx264", "-g", "50", "-c:a", "aac", cls.tmp / "src.mp4")
        segs = [{"src": "src.mp4", "start": i * 2.5, "end": i * 2.5 + 2.0} for i in range(10)]
        cls.edl = {"segments": segs, "texts": [{"text": "HOOK", "start": 0.5, "end": 1.8, "pos": "center"},
                                                {"text": "END CARD", "start": 17.0, "end": 19.5, "pos": "bottom"}]}
        (cls.tmp / "v1.json").write_text(json.dumps(cls.edl))
        sh(VS, "render", "v1.json", "-o", "out/v1.mp4", cwd=cls.tmp)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def frames(self, f):
        return int(sh("ffprobe", "-v", "error", "-count_packets", "-select_streams", "v:0", "-show_entries",
                      "stream=nb_read_packets", "-of", "csv=p=0", self.tmp / f).stdout.strip())

    def psnr_min(self, a, b):
        p = sh("ffmpeg", "-hide_banner", "-i", self.tmp / a, "-i", self.tmp / b, "-lavfi", "[0:v][1:v]psnr",
               "-f", "null", "-")
        m = re.findall(r"min:([\d.]+|inf)", p.stderr)[-1]
        return float("inf") if m == "inf" else float(m)

    def test_trim_revision_matches_full_render(self):
        self.assertTrue((self.tmp / "out" / "v1.mp4.render.json").exists())
        keys = splice.keyframe_times(self.tmp / "out" / "v1.mp4")
        for cut in (2.0, 4.0, 10.0, 18.0):                                        # an IDR at every hard cut
            self.assertTrue(any(abs(k - cut) < 0.02 for k in keys), cut)
        e = json.loads(json.dumps(self.edl))
        e["segments"][2]["end"] -= 0.8                                            # shot 3 shorter: 20 s -> 19.2 s
        e["texts"][1].update(start=16.2, end=18.7)                                # end card rides with the picture
        (self.tmp / "v2.json").write_text(json.dumps(e))
        out = sh(VS, "render", "v2.json", "-o", "out/v2.mp4", "--since", "out/v1.mp4", cwd=self.tmp).stdout
        self.assertIn("revision: re-encoded 00:04.000-00:05.200", out)
        sh(VS, "render", "v2.json", "-o", "out/v2_full.mp4", "--since", "none", cwd=self.tmp)
        self.assertEqual(self.frames("out/v2.mp4"), self.frames("out/v2_full.mp4"))      # 480 frames
        self.assertGreater(self.psnr_min("out/v2.mp4", "out/v2_full.mp4"), 40)            # visually identical
        self.assertTrue((self.tmp / "out" / "v2.mp4.render.json").exists())               # chainable

    def test_notes_focus_shows_only_that_moment(self):
        sh(VS, "notes", "add", "notes.json", "--edl", "v1.json", "--video", "out/v1.mp4",
           "--text", "0:09 this shot is too long", "--text", "the whole thing should be warmer", cwd=self.tmp)
        out = sh(VS, "notes", "focus", "notes.json", "1", "--edl", "v1.json", cwd=self.tmp).stdout
        self.assertIn("window 0:07.000-0:11.000", out)
        md = (self.tmp / "focus" / "note-1" / "focus.md").read_text()
        self.assertIn("| shot 5 | segments[4] |", md)                       # 8-10 s
        self.assertIn("| shot 4 | segments[3] |", md)                       # neighbours inside the window
        self.assertNotIn("segments[0]", md)                                # nothing outside the window
        self.assertNotIn("HOOK", md)
        self.assertIn("--since out/v1.mp4", md)
        self.assertTrue((self.tmp / "focus" / "note-1" / "frames.png").exists())
        p = sh(VS, "notes", "focus", "notes.json", "2", cwd=self.tmp, ok=False)  # a global note has no window
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("whole video", p.stderr)

    def test_audio_only_and_fallback(self):
        e = json.loads(json.dumps(self.edl))
        e["segments"][5]["volume_db"] = -6                                        # louder/quieter only: picture same
        (self.tmp / "v3.json").write_text(json.dumps(e))
        out = sh(VS, "render", "v3.json", "-o", "out/v3.mp4", "--since", "out/v1.mp4", cwd=self.tmp).stdout
        self.assertIn("picture unchanged", out)
        self.assertEqual(self.frames("out/v3.mp4"), 500)
        e["grade"] = "warm"                                                       # global look: everything changes
        (self.tmp / "v4.json").write_text(json.dumps(e))
        p = sh(VS, "render", "v4.json", "-o", "out/v4.mp4", "--since", "out/v1.mp4", cwd=self.tmp)
        self.assertIn("full render", p.stderr)
        self.assertNotIn("revision:", p.stdout)

    def test_auto_reuses_a_sibling_variant(self):
        """A second hook in front of the same body: `vs render` (default --since auto) finds the first hook's render in
        the folder, re-encodes only the hook and copies the body."""
        d = self.tmp / "auto"
        d.mkdir(exist_ok=True)
        h1 = json.loads(json.dumps(self.edl))
        (d / "h1.json").write_text(json.dumps(h1))
        sh(VS, "render", d / "h1.json", "-o", d / "out" / "h1.mp4", "--since", "none", cwd=self.tmp)
        h2 = json.loads(json.dumps(self.edl))
        h2["segments"][0] = {"src": "src.mp4", "start": 26.0, "end": 29.0}       # a longer, different hook shot
        h2["texts"][0]["text"] = "OTHER HOOK"
        h2["texts"][1].update(start=18.0, end=20.5)                               # the body moved 1 s later
        (d / "h2.json").write_text(json.dumps(h2))
        p = sh(VS, "render", d / "h2.json", "-o", d / "out" / "h2.mp4", cwd=self.tmp)
        self.assertIn("--since auto: reusing h1.mp4", p.stderr)
        self.assertIn("revision: re-encoded 00:00.000-00:03.000", p.stdout)
        sh(VS, "render", d / "h2.json", "-o", d / "full" / "h2.mp4", "--since", "none", cwd=self.tmp)
        self.assertEqual(self.frames("auto/out/h2.mp4"), self.frames("auto/full/h2.mp4"))
        self.assertGreater(self.psnr_min("auto/out/h2.mp4", "auto/full/h2.mp4"), 40)

        # the same name again after a fix: the previous render is parked, reused, then removed
        h2["segments"][6]["end"] -= 0.4
        h2["texts"][1].update(start=17.6, end=20.1)
        (d / "h2.json").write_text(json.dumps(h2))
        p = sh(VS, "render", d / "h2.json", "-o", d / "out" / "h2.mp4", cwd=self.tmp)
        self.assertIn("h2.mp4 (previous)", p.stderr)
        self.assertIn("revision:", p.stdout)
        self.assertTrue((d / "out" / "h2.mp4.render.json").exists())
        self.assertFalse(list((d / "out").glob(".vs-cache/previous-*")))
        self.assertEqual(self.frames("auto/out/h2.mp4"), round((21.0 - 0.4) * 25))

    def test_revision_with_a_voice_track(self):
        """Ads: muted shots under a separate voice-over track. The sound-only pass of a revision used to reference
        per-shot sound that a voice track never makes, failed, and fell back to a full render every time."""
        d = self.tmp / "vo"
        (d / "out").mkdir(parents=True, exist_ok=True)
        sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "sine=f=500:d=21", d / "vo.wav")
        e = json.loads(json.dumps(self.edl))
        for seg in e["segments"]:
            seg["mute"] = True
        e["audio_track"] = {"src": str(d / "vo.wav"), "start": 0}
        (d / "v1.json").write_text(json.dumps(e))
        sh(VS, "render", d / "v1.json", "-o", d / "out" / "ad.mp4", "--since", "none", cwd=self.tmp)
        e["segments"][6].update(start=26.0, end=28.0)                             # a different moment, same length
        (d / "v1.json").write_text(json.dumps(e))
        p = sh(VS, "render", d / "v1.json", "-o", d / "out" / "ad.mp4", cwd=self.tmp)
        self.assertIn("revision: re-encoded 00:12.000-00:14.000", p.stdout, p.stderr)
        self.assertNotIn("rendering everything", p.stderr)

    def test_limiter_in_the_finish(self):
        p = sh(VS, "render", "v1.json", "-o", "out/lim.mp4", "--loudnorm", "-14", "--lra", "7", "--limiter",
               "--dry-run", cwd=self.tmp)
        self.assertIn("LRA=7", p.stdout)
        self.assertIn("alimiter=limit=0.7079", p.stdout)


if __name__ == "__main__":
    unittest.main()
