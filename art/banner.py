import sys
from pathlib import Path

from PIL import Image

from font import paint_title
from palette import ORANGE, ORANGE_DARK
from pixelate import pixelate, upscale

ART = Path(__file__).resolve().parent
SOURCE = ART / "source.png"
OUT = ART.parent / "assets" / "banner.png"

GRID_WIDTH = 512
COLORS = 48
OUT_WIDTH = 1536
TITLE_AT = (118, 12)


def render(grid_width=GRID_WIDTH, colors=COLORS):
    img = pixelate(Image.open(SOURCE), grid_width, colors, (ORANGE, ORANGE_DARK))
    paint_title(img, *TITLE_AT)
    return upscale(img, OUT_WIDTH)


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else OUT
    out.parent.mkdir(exist_ok=True)
    render().save(out)
    print(out)
