"""Wikimedia originals fall back to standard thumbnails on thumb.wikimedia.org (Wikimedia answers originals with 429)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plugins" / "video-studio" / "tools"))
from assets import wiki_thumb  # noqa: E402


class WikiThumbTest(unittest.TestCase):
    def test_original_with_tracking_query(self):
        u = ("https://upload.wikimedia.org/wikipedia/commons/e/e4/PEbers_c41-bc.jpg"
             "?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=original")
        self.assertEqual(wiki_thumb(u, 1920), "https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e4/"
                                              "PEbers_c41-bc.jpg/1920px-PEbers_c41-bc.jpg")

    def test_tiff_becomes_jpg_and_non_images_skip(self):
        self.assertTrue(wiki_thumb("https://upload.wikimedia.org/wikipedia/commons/a/ab/X.tif", 960)
                        .endswith("/960px-X.tif.jpg"))
        self.assertIsNone(wiki_thumb("https://upload.wikimedia.org/wikipedia/commons/a/ab/Film.webm", 960))
        self.assertIsNone(wiki_thumb("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/X.jpg/330px-X.jpg", 960))
        self.assertIsNone(wiki_thumb("https://example.com/a/ab/X.jpg", 960))


if __name__ == "__main__":
    unittest.main()
