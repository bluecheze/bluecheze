from layout import GROUND, HORIZON
from palette import CLOUD, SEA, SEA_LIGHT, SKY, SKY_TOP
from pixels import dithered, put

BIRDS = [(222, 14), (230, 11), (268, 30)]


def paint_sky(img):
    for y in range(HORIZON):
        fade = 1 - y / 34
        for x in range(img.width):
            put(img, x, y, SKY_TOP if dithered(x, y, fade) else SKY)


def paint_sea(img):
    for y in range(HORIZON, GROUND):
        for x in range(img.width):
            glint = (x * 7 + y * 13) % 29 == 0
            put(img, x, y, SEA_LIGHT if glint else SEA)


def paint_birds(img):
    for x, y in BIRDS:
        put(img, x - 1, y - 1, CLOUD)
        put(img, x, y, CLOUD)
        put(img, x + 1, y - 1, CLOUD)
