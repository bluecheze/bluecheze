import random

from pixels import put, rect

GRASS_LIGHT = (122, 168, 72)
GRASS = (62, 118, 52)
GRASS_DARK = (34, 76, 40)
SOIL = (92, 62, 38)
SOIL_DARK = (58, 38, 24)


def paint_ground(img, top, seed):
    rng = random.Random(seed)
    width = img.width
    rect(img, 0, top, width, top + 2, GRASS)
    rect(img, 0, top + 2, width, top + 4, GRASS_DARK)
    rect(img, 0, top + 4, width, top + 6, SOIL)
    rect(img, 0, top + 6, width, top + 7, SOIL_DARK)
    for x in range(width):
        if rng.random() < 0.45:
            put(img, x, top - 1, GRASS)
        if rng.random() < 0.12:
            put(img, x, top - 2, GRASS_LIGHT)
        if rng.random() < 0.08:
            put(img, x, top + 5, SOIL_DARK)
