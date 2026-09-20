from PIL import Image, ImageDraw
import math

INK  = (16, 33, 50, 255)      # #102132  - his site's --ink
BLUE = (18, 106, 176, 255)    # #126ab0  - his site's --blue

def build(SS=6, N=1024):
    W = N * SS
    k = W / 1024.0                      # everything below is authored on a 1024 grid
    img = Image.new("RGBA", (W, W), (0,0,0,0))
    d = ImageDraw.Draw(img)
    def P(*pts): return [(x*k, y*k) for x, y in pts]
    sw = int(74 * k)                    # main stroke weight

    # ---- roof: apex, down both sides ----
    d.line(P((196,470),(512,196),(828,470)), fill=INK, width=sw, joint="curve")
    # round the three ends/joint
    for (x,y) in [(196,470),(512,196),(828,470)]:
        r = sw/2
        d.ellipse([x*k-r, y*k-r, x*k+r, y*k+r], fill=INK)

    # ---- left wall + a short return along the bottom ----
    d.line(P((286,430),(286,812),(430,812)), fill=INK, width=sw, joint="curve")
    for (x,y) in [(286,430),(286,812),(430,812)]:
        r = sw/2
        d.ellipse([x*k-r, y*k-r, x*k+r, y*k+r], fill=INK)

    # ---- blue accent on the right of the roof (the chimney-ish flag) ----
    d.polygon(P((742,300),(806,300),(806,432),(742,368)), fill=BLUE)

    # ---- magnifying glass: lens ring ----
    cx, cy, R = 598, 596, 176
    ring = int(66 * k)
    d.ellipse([(cx-R)*k, (cy-R)*k, (cx+R)*k, (cy+R)*k], outline=INK, width=ring)
    # knock the lens interior clear so the roof line doesn't show through
    inner = R - ring/k/2 - 2
    d.ellipse([(cx-inner)*k, (cy-inner)*k, (cx+inner)*k, (cy+inner)*k], fill=(0,0,0,0))

    # ---- handle, 45 degrees to lower-right, rounded ----
    a = math.radians(45)
    hx0, hy0 = cx + math.cos(a)*(R+ring/k/2-14), cy + math.sin(a)*(R+ring/k/2-14)
    hx1, hy1 = cx + math.cos(a)*(R+150),         cy + math.sin(a)*(R+150)
    hw = int(86 * k)
    d.line(P((hx0,hy0),(hx1,hy1)), fill=INK, width=hw)
    for (x,y) in [(hx0,hy0),(hx1,hy1)]:
        r = hw/2
        d.ellipse([x*k-r, y*k-r, x*k+r, y*k+r], fill=INK)

    # ---- four blue panes inside the lens ----
    pane, gap = 62, 20
    ox, oy = cx - pane - gap/2, cy - pane - gap/2
    for r_ in range(2):
        for c_ in range(2):
            x0 = ox + c_*(pane+gap); y0 = oy + r_*(pane+gap)
            d.rounded_rectangle([x0*k, y0*k, (x0+pane)*k, (y0+pane)*k],
                                radius=int(8*k), fill=BLUE)
    return img

img = build()
for size, name in [(120,"120"), (512,"512"), (1024,"1024")]:
    img.resize((size,size), Image.LANCZOS).save(f"/Users/tylerpugh/flipfindr-mark-{name}.png")
print("built")
