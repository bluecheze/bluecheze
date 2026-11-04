from layout import GROUND
from palette import (
    GLASS, GLASS_LIGHT, HOUSE, HOUSE_DARK, INK, LEAF, LEAF_DARK, POLE, POLE_DARK,
    ROOF, SKY, TRIM, WOOD, WOOD_DARK, YELLOW, YELLOW_DARK,
)
from pixels import put, rect

POLE_X = 40
POLE_TOP = 40

WIRES = [
    ((32, 44), (340, 34), 7), ((48, 44), (340, 39), 8),
    ((34, 50), (340, 45), 8), ((46, 50), (340, 51), 9),
    ((32, 44), (-30, 52), 5), ((34, 50), (-30, 60), 5),
]


def paint_wire(img, start, end, sag):
    (x0, y0), (x1, y1) = start, end
    step = 1 if x1 > x0 else -1
    for x in range(x0, x1, step):
        t = (x - x0) / (x1 - x0)
        y = y0 + (y1 - y0) * t + sag * 4 * t * (1 - t)
        put(img, x, round(y), INK)


def paint_wires(img):
    for start, end, sag in WIRES:
        paint_wire(img, start, end, sag)


def paint_pole(img):
    rect(img, POLE_X, POLE_TOP, POLE_X + 1, GROUND + 1, POLE)
    rect(img, POLE_X + 1, POLE_TOP, POLE_X + 2, GROUND + 1, POLE_DARK)
    rect(img, POLE_X - 9, POLE_TOP + 4, POLE_X + 10, POLE_TOP + 5, POLE_DARK)
    rect(img, POLE_X - 7, POLE_TOP + 10, POLE_X + 8, POLE_TOP + 11, POLE_DARK)
    rect(img, POLE_X - 4, 60, POLE_X, 64, SKY)
    rect(img, POLE_X - 3, 61, POLE_X - 1, 63, TRIM)


def paint_roof(img):
    for y in range(40, 53):
        half = (y - 40) * 2 + 2
        rect(img, 86 - half, y, 86 + half, y + 1, ROOF)
        put(img, 86 - half + 1, y, TRIM)
        put(img, 86 + half - 2, y, TRIM)


def paint_walls(img):
    rect(img, 64, 53, 108, GROUND, HOUSE)
    for x in range(66, 108, 3):
        rect(img, x, 53, x + 1, GROUND, HOUSE_DARK)


def paint_window(img, x0, y0, x1, y1):
    rect(img, x0, y0, x1, y1, TRIM)
    rect(img, x0 + 1, y0 + 1, x1 - 1, y1 - 1, GLASS)
    rect(img, x0 + 1, y0 + 1, (x0 + x1) // 2, y0 + 3, GLASS_LIGHT)
    rect(img, (x0 + x1) // 2, y0, (x0 + x1) // 2 + 1, y1, TRIM)


def paint_shop(img):
    rect(img, 98, 64, 126, 67, ROOF)
    rect(img, 100, 67, 124, GROUND, YELLOW)
    for x in range(102, 124, 4):
        rect(img, x, 67, x + 1, GROUND, YELLOW_DARK)
    rect(img, 108, 72, 116, GROUND, YELLOW_DARK)
    rect(img, 109, 73, 115, GROUND, YELLOW)
    rect(img, 110, 74, 114, 78, GLASS)
    rect(img, 101, 70, 107, 78, TRIM)
    rect(img, 102, 71, 106, 77, GLASS_LIGHT)


def paint_porch(img):
    rect(img, 50, 70, 66, 72, WOOD)
    for x in (52, 63):
        rect(img, x, 72, x + 1, GROUND, WOOD_DARK)
    rect(img, 52, 79, 64, 80, WOOD)
    for x in range(53, 63, 2):
        rect(img, x, 80, x + 1, GROUND, WOOD)


def paint_plants(img):
    for x in range(54, 72):
        top = GROUND - 2 - (x * 5) % 3
        rect(img, x, top, x + 1, GROUND, LEAF if x % 2 else LEAF_DARK)
    rect(img, 129, 78, 130, GROUND, WOOD_DARK)
    for y in range(68, 80):
        for x in range(124, 135):
            if (x - 129) ** 2 + (y - 74) ** 2 <= 26:
                put(img, x, y, LEAF_DARK if (x + y) % 3 == 0 else LEAF)


def paint_house(img):
    paint_walls(img)
    paint_roof(img)
    paint_window(img, 78, 56, 95, 65)
    paint_window(img, 70, 72, 85, 81)
    paint_porch(img)
    paint_shop(img)
    paint_plants(img)
