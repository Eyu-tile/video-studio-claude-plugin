# Apple emoji for on-screen text (EDITING_RULES: emoji are always Apple emoji).
# Fetches the Apple PNG for each emoji from the emoji-datasource-apple package (jsDelivr) into a local cache and returns it as a
# Pillow image, so headlines/captions/cards can paste it next to the text. Never falls back to another emoji style.
#
# usage as a module:   from apple_emoji import emoji_image;  im = emoji_image("😅", size=56, cache="work/apple_emoji")
# usage from the shell: python3 -I apple_emoji.py CACHE_DIR "😅🙃👀"     (downloads and lists the files)
import os, sys, urllib.request
from PIL import Image

VERSION = "15.1.2"   # emoji-datasource-apple release; 64 px is the largest size it publishes per emoji
URL = "https://cdn.jsdelivr.net/npm/emoji-datasource-apple@{v}/img/apple/64/{code}.png"
SKIP = {0xFE0F, 0x200D}   # variation selector / zero-width joiner


def codepoint_name(emoji):
    """File name the package uses: lowercase hex codepoints joined by '-' (FE0F dropped for single-codepoint emoji)."""
    cps = [ord(c) for c in emoji]
    if len(cps) > 1 and cps[-1] == 0xFE0F:
        cps = cps[:-1]
    return "-".join(f"{c:x}" for c in cps)


def fetch(emoji, cache):
    os.makedirs(cache, exist_ok=True)
    name = codepoint_name(emoji)
    path = os.path.join(cache, f"{name}.png")
    if os.path.exists(path):
        return path
    full = "-".join(f"{ord(c):x}" for c in emoji)                        # some files keep FE0F (e.g. ❤️ = 2764-fe0f)
    tries = list(dict.fromkeys([name, full, f"{name}-fe0f", name.replace("-fe0f", "")]))
    err = None
    for code in tries:
        try:
            data = urllib.request.urlopen(URL.format(v=VERSION, code=code), timeout=30).read()
            open(path, "wb").write(data)
            return path
        except Exception as e:
            err = e
    raise RuntimeError(f"Apple emoji {emoji!r} (tried {tries}) could not be fetched: {err}. Do not fall back to another emoji style.")


def emoji_image(emoji, size, cache):
    """Apple emoji as an RGBA image `size` px tall (trimmed to its visible area)."""
    im = Image.open(fetch(emoji, cache)).convert("RGBA")
    im = im.crop(im.getbbox())
    r = size / im.height
    return im.resize((max(1, round(im.width * r)), size), Image.LANCZOS)


def split_emoji(text):
    """Split a string into emoji clusters and plain characters (enough for headline copy: single emoji, skin tones, VS16, ZWJ)."""
    out, i = [], 0
    while i < len(text):
        c = text[i]
        if ord(c) >= 0x2190 and ord(c) not in SKIP:
            j = i + 1
            while j < len(text) and (ord(text[j]) in SKIP or 0x1F3FB <= ord(text[j]) <= 0x1F3FF or (text[j - 1] == "‍")):
                j += 1
            out.append(text[i:j]); i = j
        else:
            out.append(c); i += 1
    return out


if __name__ == "__main__":
    cache, text = sys.argv[1], sys.argv[2]
    for e in [x for x in split_emoji(text) if ord(x[0]) >= 0x2190]:
        print(e, fetch(e, cache))
