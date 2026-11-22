# Hook text card (transparent PNG) in the brand look: white rounded box, navy Newsreader, upper third.
import sys
from PIL import Image, ImageDraw, ImageFont
txt, out = sys.argv[1], sys.argv[2]
f = ImageFont.truetype("assets/fonts/Newsreader-SemiBold.ttf", 66); W, H = 720, 1280
im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); tw = d.textlength(txt, font=f)
x0, y0 = (W - tw) / 2 - 34, 250; d.rounded_rectangle((x0, y0, x0 + tw + 68, y0 + 104), 26, fill=(255, 255, 255, 240))
d.text(((W - tw) / 2, y0 + 12), txt, font=f, fill=(11, 42, 91)); im.save(out)
