from pathlib import Path

from PIL import Image

from clouds import paint_clouds
from font import paint_title
from layout import HEIGHT, SCALE, WIDTH
from sky import paint_birds, paint_sea, paint_sky
from street import paint_figure, paint_street
from town import paint_house, paint_pole, paint_wires

OUT = Path(__file__).resolve().parent.parent / "assets" / "banner.png"

LAYERS = [
    paint_sky, paint_sea, paint_clouds, paint_birds, paint_wires,
    paint_pole, paint_house, paint_street, paint_figure, paint_title,
]


def render():
    img = Image.new("RGB", (WIDTH, HEIGHT))
    for layer in LAYERS:
        layer(img)
    return img.resize((WIDTH * SCALE, HEIGHT * SCALE), Image.NEAREST)


if __name__ == "__main__":
    OUT.parent.mkdir(exist_ok=True)
    render().save(OUT)
    print(OUT)
