"""Generates placeholder logos (Image/Logo.png, Image/inverseLogo.png).
Replace them with your own branding any time - same filenames."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "Image"
OUT.mkdir(exist_ok=True)


def font(size):
    for name in ("DejaVuSerif.ttf", "DejaVuSerif-Bold.ttf", "Georgia.ttf", "times.ttf", "Times New Roman.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default(size)


def draw_logo(color, path):
    w, h = 800, 220
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, top, lw = 110, 40, 8
    # scales of justice
    d.line([(cx, top), (cx, 175)], fill=color, width=lw)                 # pillar
    d.line([(cx - 70, top + 20), (cx + 70, top + 20)], fill=color, width=lw)  # beam
    d.ellipse([cx - 12, top - 12, cx + 12, top + 12], fill=color)
    d.rounded_rectangle([cx - 45, 168, cx + 45, 184], radius=6, fill=color)   # base
    for sx in (cx - 70, cx + 70):
        d.line([(sx, top + 20), (sx - 35, top + 90)], fill=color, width=4)
        d.line([(sx, top + 20), (sx + 35, top + 90)], fill=color, width=4)
        d.pieslice([sx - 40, top + 55, sx + 40, top + 125], 0, 180, fill=color)
    d.text((215, 45), "LegalEase", font=font(105), fill=color)
    img.save(path)


draw_logo((25, 25, 25, 255), OUT / "Logo.png")
draw_logo((245, 245, 245, 255), OUT / "inverseLogo.png")
print("Logos created in", OUT)
