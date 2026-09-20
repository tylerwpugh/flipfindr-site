from PIL import Image, ImageDraw, ImageFont
import math, importlib.util

INK  = (16, 33, 50, 255)
BLUE = (18, 106, 176, 255)
FONT = "/System/Library/Fonts/SFNS.ttf"

spec = importlib.util.spec_from_file_location("mark", "mark.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)

def wordmark(px, weight="Heavy"):
    """'Flip' in ink + 'Findr' in blue, returned tight-cropped."""
    f = ImageFont.truetype(FONT, px)
    try: f.set_variation_by_name(weight)
    except Exception: pass
    pad = px
    img = Image.new("RGBA", (px*9, px*3), (0,0,0,0))
    d = ImageDraw.Draw(img)
    x = pad
    for part, col in (("Flip", INK), ("Findr", BLUE)):
        d.text((x, pad), part, font=f, fill=col)
        x += d.textlength(part, font=f)
    return img.crop(img.getbbox())

def place(canvas, im, cx, top):
    canvas.alpha_composite(im, (int(cx - im.width/2), int(top)))

# ---------- STACKED: mark above, wordmark below (matches his reference) ----------
mark = mk.build().resize((900, 900), Image.LANCZOS); mark = mark.crop(mark.getbbox())
wm   = wordmark(300)
gap  = 96
W    = max(mark.width, wm.width) + 160
H    = mark.height + gap + wm.height + 120
st = Image.new("RGBA", (W, H), (0,0,0,0))
place(st, mark, W/2, 40)
place(st, wm,   W/2, 40 + mark.height + gap)
st = st.crop(st.getbbox())
st.save("/Users/tylerpugh/flipfindr-lockup-stacked.png")

# ---------- HORIZONTAL: mark left, wordmark right (site header) ----------
mh   = 420
_m = mk.build(); _m = _m.crop(_m.getbbox()); markh = _m.resize((mh, int(mh*_m.height/_m.width)), Image.LANCZOS)
wmh  = wordmark(250)
gap2 = 46
W2 = markh.width + gap2 + wmh.width
H2 = max(markh.height, wmh.height)
hz = Image.new("RGBA", (W2, H2), (0,0,0,0))
hz.alpha_composite(markh, (0, int((H2-markh.height)/2)))
hz.alpha_composite(wmh,  (markh.width+gap2, int((H2-wmh.height)/2)))
hz = hz.crop(hz.getbbox())
hz.save("/Users/tylerpugh/flipfindr-lockup-horizontal.png")

for p in ["/Users/tylerpugh/flipfindr-lockup-stacked.png","/Users/tylerpugh/flipfindr-lockup-horizontal.png"]:
    im = Image.open(p); print(f"  {p.split('/')[-1]:38s} {im.size}")
