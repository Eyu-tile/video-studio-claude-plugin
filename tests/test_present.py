"""Tests for `vs present`: the review page folder, the size cap, comments back as notes, the preference, and the
link recorded on a task (needs ffmpeg). The page's own behaviour is checked in a browser by
tests/review_page_check.js when Node + Playwright are available.

Run: python3 -m unittest discover -s tests -v
"""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VS = ROOT / "plugins" / "video-studio" / "bin" / "vs"


def sh(*cmd, env=None, ok=True, cwd=None):
    p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, env=env, cwd=cwd)
    if ok and p.returncode != 0:
        raise AssertionError(f"{' '.join(map(str, cmd))}\n{p.stdout}\n{p.stderr[-2000:]}")
    return p


class PresentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="vs-present-"))
        cls.ws = cls.tmp / "video-studio"
        cls.env = {**os.environ, "VS_WORKSPACE": str(cls.ws)}
        sh(VS, "new", "demo", env=cls.env, cwd=cls.tmp)
        cls.final = cls.ws / "projects" / "demo" / "out" / "final.mp4"
        cls.final.parent.mkdir(parents=True, exist_ok=True)
        sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "testsrc2=s=1920x1080:r=30:d=12", "-f", "lavfi",
           "-i", "sine=f=330:d=12", "-shortest", "-c:v", "libx264", "-b:v", "20M", "-c:a", "aac", cls.final)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def vs(self, *args, ok=True):
        return sh(VS, *args, env=self.env, ok=ok, cwd=self.tmp)

    def test_page_folder(self):
        self.vs("present", self.final, "--project", "demo", "--version", "v2", "--title", "Launch Reel", "--max-mb", "3")
        d = self.ws / "projects" / "demo" / "out" / "review" / "v2"
        for f in ("index.html", "local.html", "video.mp4", "strip.jpg", "poster.jpg", "publish.json"):
            self.assertTrue((d / f).exists(), f)
        self.assertLessEqual((d / "video.mp4").stat().st_size, 3 * 1048576)        # size cap honoured (20 Mbps source)
        info = json.loads(sh("ffprobe", "-v", "error", "-show_entries", "stream=codec_name,width,height",
                             "-of", "json", d / "video.mp4").stdout)["streams"]
        self.assertEqual({s["codec_name"] for s in info}, {"h264", "aac"})
        self.assertLessEqual(max(s.get("width", 0) for s in info), 1280)
        pub = json.loads((d / "publish.json").read_text())
        self.assertEqual(set(pub["files"]), {"video.mp4", "strip.jpg", "poster.jpg"})
        self.assertEqual(set(pub["capabilities"]), {"db", "user", "downloads"})
        cfg = pub["config"]
        self.assertEqual((cfg["version"], cfg["title"], cfg["fps"]), ("v2", "Launch Reel", 30.0))
        self.assertEqual(cfg["strip"]["count"], 24)                                  # 2 per second, at least 8
        page = (d / "index.html").read_text()
        self.assertTrue(page.startswith("<title>Launch Reel v2</title>"))
        self.assertNotIn("__CONFIG__", page)
        self.assertNotIn("<!doctype", page.lower())                                  # the Artifact tool adds the skeleton
        self.assertTrue((d / "local.html").read_text().lower().startswith("<!doctype html>"))

    def test_notes_from_db_rows_and_csv(self):
        rows = [{"id": "a", "data": {"t": 12.5, "text": "Swap this\nshot", "created": 1, "resolved": False}},
                {"id": "b", "data": {"t": 27.0, "te": 30.0, "text": "Music too loud", "created": 2, "resolved": False}},
                {"id": "c", "data": {"parent": "a", "text": "Agreed", "created": 3}},
                {"id": "d", "data": {"t": 5.0, "text": "Done already", "created": 4, "resolved": True}},
                {"id": "e", "data": {"text": "General: warmer grade", "created": 5, "resolved": False}}]
        j = self.tmp / "rows.json"
        j.write_text(json.dumps(rows))
        out = self.vs("present", "notes", j).stdout.splitlines()
        self.assertEqual(out, ["0:12.50 Swap this shot [replies: Agreed]", "0:27.00-0:30.00 Music too loud",
                               "General: warmer grade"])
        self.assertEqual(len(self.vs("present", "notes", j, "--all").stdout.splitlines()), 4)
        c = self.tmp / "export.csv"
        c.write_text('#,Time,End,Timecode,Frame,Commenter,Comment,Status,Replies\n'
                     '1,"0:12.50","","00:00:12:15",375,"Josh","Swap this shot",Open,""\n'
                     '2,"0:05.00","","00:00:05:00",150,"Josh","Fixed",Completed,""\n')
        self.vs("notes", "add", self.tmp / "csvnotes.json", c)                   # vs notes reads the CSV directly too
        got = json.loads((self.tmp / "csvnotes.json").read_text())["notes"]
        self.assertEqual(got[0]["at"], [[12.5, None]])
        self.assertEqual(self.vs("present", "notes", c).stdout.strip(), "0:12.50 Swap this shot")
        # the lines are what vs notes reads
        notes_txt = self.tmp / "n.txt"
        self.vs("present", "notes", j, "-o", notes_txt)
        self.vs("notes", "add", self.tmp / "notes.json", notes_txt)
        items = json.loads((self.tmp / "notes.json").read_text())["notes"]
        self.assertEqual([n.get("at") for n in items], [[[12.5, None]], [[27.0, 30.0]], None])

    def test_page_in_browser(self):
        """Runs tests/review_page_check.js in headless Chromium when Node + Playwright are installed."""
        if not shutil.which("node") or subprocess.run(["node", "-e", "require('playwright')"],
                                                      capture_output=True).returncode != 0:
            self.skipTest("node + playwright not installed")
        self.vs("present", self.final, "--project", "demo", "--version", "v9", "--max-mb", "3")
        d = self.ws / "projects" / "demo" / "out" / "review" / "v9"
        p = sh("node", Path(__file__).with_name("review_page_check.js"), d, ok=False)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr[-1500:])
        # who can post: owner and editor reach the shared list; view-only and unlinked viewers keep notes, marked NOT sent
        p = sh("node", Path(__file__).with_name("review_access_check.js"), d, ok=False)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr[-1500:])

    def test_pref_and_link(self):
        self.assertEqual(self.vs("present", "pref").stdout.strip(), "ask")
        self.vs("present", "pref", "never")
        self.assertEqual(self.vs("present", "pref").stdout.strip(), "never")
        self.vs("task", "new", "TC0001", "--project", "demo", "--client", "Acme")
        out = self.vs("task", "deliver", "TC0001", "--file", self.final).stdout
        self.assertNotIn("vs present", out)                                         # "never": no offer
        self.vs("present", "pref", "ask")
        out = self.vs("task", "deliver", "TC0001", "--file", self.final, "--version", "v2").stdout
        self.assertIn("vs present", out)
        self.vs("present", self.final, "--project", "demo", "--task", "TC0001", "--version", "v2", "--max-mb", "3")
        d = self.ws / "projects" / "demo" / "out" / "review" / "v2"
        self.vs("present", "link", d, "https://claude.ai/artifact/abc")
        self.assertEqual(json.loads((d / "publish.json").read_text())["url"], "https://claude.ai/artifact/abc")
        t = json.loads((self.ws / "history" / "TC0001.json").read_text())
        self.assertEqual(t["versions"][-1]["review"], "https://claude.ai/artifact/abc")


if __name__ == "__main__":
    unittest.main()
