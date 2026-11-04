import sys
from pathlib import Path

from PIL import Image

from font import paint_title
from palette import CREAM, MOSS_INK, ORANGE, ORANGE_DARK, SKIN
from pixelate import pixelate, upscale

ART = Path(__file__).resolve().parent
SOURCE = ART / "source.png"
OUT = ART.parent / "assets" / "banner.png"

GRID_WIDTH = 768
COLORS = 56
OUT_WIDTH = 1536
TITLE_AT = (92, 42)
TITLE_SCALE = 4
GRASS = (0, 238, 768, 250)


def render(grid_width=GRID_WIDTH, colors=COLORS):
    img = pixelate(Image.open(SOURCE), grid_width, colors, (ORANGE, ORANGE_DARK, SKIN))
    grass = upscale(img.crop(GRASS), OUT_WIDTH)
    paint_title(img, *TITLE_AT, TITLE_SCALE, CREAM, MOSS_INK)
    return upscale(img, OUT_WIDTH), grass


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else OUT
    out.parent.mkdir(exist_ok=True)
    banner, grass = render()
    banner.save(out)
    grass.save(out.with_name("divider.png"))
    print(out)
