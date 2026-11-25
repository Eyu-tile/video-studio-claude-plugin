"""`vs gen`: plan, dependency order, done/fail/retry, fetch (local HTTP server) and EDL assembly."""
import functools
import http.server
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "plugins" / "video-studio" / "tools"

SCRIPT = {"variant": "v1", "aspect": "9:16",
          "presenter": {"name": "Maya", "look": "woman, early 30s, dark curly hair, green sweater",
                        "voice": "warm, conversational", "setting": "bright kitchen", "consent": "fictional"},
          "lines": [{"beat": "hook", "say": "My knees used to scream every single time I took the stairs.",
                     "show": "talking", "perform": "wince on 'scream'"},
                    {"beat": "demo", "say": "Now I just slip this sleeve on before my walk and go.",
                     "show": "broll", "broll": "hands sliding a knee sleeve on", "source": "generate"},
                    {"beat": "proof", "say": "Three weeks later I take the stairs two at a time again.",
                     "show": "talking"},
                    {"beat": "cta", "say": "Tap the link and get thirty percent off today.", "show": "broll",
                     "broll": "product on a table", "source": "library"}]}


def sh(*cmd, ok=True):
    p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if ok and p.returncode:
        raise AssertionError(f"{cmd}\n{p.stdout}\n{p.stderr[-3000:]}")
    return p


def gen(*args, ok=True):
    return sh(sys.executable, TOOLS / "gen.py", *args, ok=ok)


class GenTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="vs-gen-"))
        cls.cwd = os.getcwd()
        os.chdir(cls.tmp)
        for d in ("srv", "proj/work/gen", "proj/work/ads"):
            Path(d).mkdir(parents=True)
        # "Generated" results: a talking clip with speech-length audio, b-roll, a start frame, a speech file.
        sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "testsrc2=s=360x640:r=25:d=7", "-f", "lavfi", "-i",
           "sine=f=300:d=7", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", "srv/talk.mp4")
        sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "color=c=orange:s=360x640:r=25:d=4", "-c:v", "libx264",
           "-pix_fmt", "yuv420p", "srv/broll.mp4")
        sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "sine=f=300:d=7", "srv/speech.wav")
        sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "color=c=gray:s=360x640", "-frames:v", "1", "srv/frame.png")
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(cls.tmp / "srv"))
        handler.log_message = lambda *a: None
        cls.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.httpd.server_address[1]}"
        Path("proj/work/gen/v1.script.json").write_text(json.dumps(SCRIPT))

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        os.chdir(cls.cwd)
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_full_cycle(self):
        J = "proj/work/gen/v1.jobs.json"
        out = gen("plan", "proj/work/gen/v1.script.json").stdout
        self.assertIn("generations", out)
        jobs = json.loads(Path(J).read_text())["jobs"]
        ids = [j["id"] for j in jobs]
        self.assertEqual(ids[:2], ["character", "voice"])
        self.assertIn("talk1", ids)
        self.assertIn("broll2", ids)            # line 2 is generated b-roll
        self.assertNotIn("broll4", ids)         # line 4 comes from the library
        talk1 = next(j for j in jobs if j["id"] == "talk1")
        self.assertEqual(talk1["needs"], ["speech1", "frame1"])
        self.assertIn("wince on 'scream'", talk1["prompt"])
        # Only character, voice and the b-roll are ready at first.
        ready = gen("next", J).stdout
        self.assertIn('"id": "character"', ready)
        self.assertNotIn('"id": "talk1"', ready)
        gen("done", J, "character", "--ref", "Maya-soul")
        gen("done", J, "voice", "--ref", "voice-delia")
        n = len([j for j in jobs if j["kind"] == "talking"])
        for k in range(1, n + 1):
            gen("done", J, f"speech{k}", "--url", f"{self.base}/speech.wav", "--credits", "1")
            gen("done", J, f"frame{k}", "--url", f"{self.base}/frame.png")
            nxt = gen("next", J).stdout
            self.assertIn(f'"id": "talk{k}"', nxt)
            self.assertIn("speech.wav", nxt)     # dependency results are handed over
            gen("fail", J, f"talk{k}", "--why", "lips out of sync")
            gen("retry", J, f"talk{k}")
            gen("done", J, f"talk{k}", "--url", f"{self.base}/talk.mp4", "--model", "seedance-2.5", "--credits", "3.8")
        gen("done", J, "broll2", "--url", f"{self.base}/broll.mp4")
        self.assertIn("credits used", gen("list", J).stdout)
        gen("fetch", J, "--project", "proj")
        self.assertTrue(list(Path("proj/raw/gen").glob("v1_talk1.mp4")))
        ledger = json.loads(Path("proj/assets/credits.json").read_text())
        self.assertTrue(all(e["ai_generated"] for e in ledger))
        r = gen("edl", J, "-o", "proj/work/ads/v1.edl.json", "--no-transcribe")
        self.assertIn("add footage: line 4", r.stdout)
        edl = json.loads(Path("proj/work/ads/v1.edl.json").read_text())
        self.assertEqual(len(edl["segments"]), n)
        ov = edl["overlays"][0]
        self.assertTrue(ov["file"].endswith("v1_broll2.mp4"))
        self.assertGreater(ov["start"], 0.5)     # placed on line 2, after line 1
        sh(sys.executable, TOOLS / "render.py", "proj/work/ads/v1.edl.json", "-o", "proj/out.mp4", "--preview",
           "--no-loudnorm")

    def test_hyperscale_character_method(self):
        """provider hyperscale: character -> sheet -> master -> one still per line -> one read cut at the
        pauses -> talking / b-roll / motion -> one shot per line with the read under it."""
        hs = {"variant": "hs1", "aspect": "9:16", "provider": "hyperscale",
              "character": {"name": "June", "age": 65, "look": "short silver hair", "flaws": "crow's feet, sun spots",
                            "wardrobe": "lilac cardigan", "consent": "fictional"},
              "product": {"name": "Roll On", "photos": [f"{self.base}/frame.png"], "look": "amber glass, gold cap"},
              "voice": {"model": "eleven-tts-v2", "voice": "v123"},
              "rooms": {"bathroom": "small bathroom at night, one warm bulb"},
              "lines": [{"say": "I'm sixty five and I used to do nine steps.", "room": "bathroom",
                         "still": "close to the mirror", "perform": "small shrug"},
                        {"say": "Now I do one.", "show": "broll", "room": "bathroom", "product": True,
                         "still": "her hand by the roller", "action": "fingers pick up the roller"},
                        {"show": "motion", "room": "bedroom", "still": "in bed by the lamp", "camera": "propped",
                         "action": "she switches off the lamp", "seconds": 1.5, "caption": "Works while you sleep"}]}
        Path("proj/work/gen/hs1.script.json").write_text(json.dumps(hs))
        J = "proj/work/gen/hs1.jobs.json"
        out = gen("plan", "proj/work/gen/hs1.script.json").stdout
        self.assertIn("Hyperscale", out)
        jobs = {j["id"]: j for j in json.loads(Path(J).read_text())["jobs"]}
        self.assertEqual(list(jobs)[:3], ["character", "sheet", "product"])
        self.assertIn("master_bathroom", jobs)            # two lines share the bathroom
        self.assertNotIn("master_bedroom", jobs)
        self.assertEqual(jobs["still1"]["needs"][0], "master_bathroom")
        self.assertIn("product", jobs["still2"]["needs"])
        self.assertIn("No face", jobs["still2"]["prompt"])
        self.assertIn("amber glass, gold cap", jobs["still2"]["prompt"])
        self.assertEqual(jobs["talk1"]["model"], "omnihuman-1-5")
        self.assertEqual(jobs["broll2"]["model"], "seedance-2-5")
        self.assertEqual(jobs["motion3"]["needs"], ["still3"])
        self.assertIn("65-year-old", jobs["character"]["prompt"])
        self.assertIn("not a model", jobs["character"]["prompt"])
        self.assertIn("propped", jobs["still3"]["prompt"])
        self.assertNotIn("arm's length", jobs["still3"]["prompt"])
        # One read with two pauses' worth of lines: tone, silence, tone.
        sh("ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "sine=f=300:d=1.4", "-f", "lavfi", "-i",
           "anullsrc=r=44100:cl=mono:d=0.6", "-f", "lavfi", "-i", "sine=f=500:d=0.8", "-filter_complex",
           "[0][1][2]concat=n=3:v=0:a=1", "srv/read.wav")
        for jid in ("character", "sheet", "master_bathroom", "still1", "still2", "still3"):
            gen("done", J, jid, "--url", f"{self.base}/frame.png")
        gen("done", J, "read", "--url", f"{self.base}/read.wav")
        gen("fetch", J, "--project", "proj")
        r = gen("slice", J, "--project", "proj").stdout
        self.assertIn("2 slices", r)
        doc = json.loads(Path(J).read_text())
        sl = next(j for j in doc["jobs"] if j["id"] == "slices")["result"]["slices"]
        self.assertAlmostEqual(sl[0]["seconds"], 1.4, delta=0.2)
        self.assertAlmostEqual(sl[1]["seconds"], 0.8, delta=0.2)
        self.assertIn('"id": "talk1"', gen("next", J).stdout)
        gen("done", J, "talk1", "--url", f"{self.base}/talk.mp4")
        gen("done", J, "broll2", "--url", f"{self.base}/broll.mp4")
        gen("done", J, "motion3", "--url", f"{self.base}/broll.mp4")
        gen("fetch", J, "--project", "proj")
        gen("edl", J, "-o", "proj/work/ads/hs1.edl.json")
        edl = json.loads(Path("proj/work/ads/hs1.edl.json").read_text())
        self.assertEqual(len(edl["segments"]), 3)
        self.assertTrue(all(s["mute"] for s in edl["segments"]))
        self.assertAlmostEqual(edl["segments"][2]["end"] - edl["segments"][2]["start"], 1.5, delta=0.01)
        self.assertEqual(len(edl["tracks"][0]["clips"]), 2)
        sh(sys.executable, TOOLS / "render.py", "proj/work/ads/hs1.edl.json", "-o", "proj/hs1.mp4", "--preview",
           "--no-loudnorm")

    def test_consent_required(self):
        s = dict(SCRIPT, presenter={**SCRIPT["presenter"], "consent": ""})
        Path("proj/work/gen/nc.script.json").write_text(json.dumps(s))
        r = gen("plan", "proj/work/gen/nc.script.json", ok=False)
        self.assertEqual(r.returncode, 1)
        self.assertIn("consent", r.stderr)


if __name__ == "__main__":
    unittest.main()
