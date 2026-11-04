from layout import GROUND, HEIGHT, ROAD_TOP
from palette import (
    BAG, HAIR, ROAD, SHIRT, SHORTS, SKIN, STRIPE, WALK, WALK_DARK, YELLOW,
)
from pixels import rect

FIGURE = [
    (1, 0, 3, 2, HAIR),
    (2, 2, 3, 3, SKIN),
    (0, 3, 5, 7, SHIRT),
    (2, 3, 5, 7, BAG),
    (-1, 3, 0, 7, SKIN),
    (5, 4, 6, 7, SKIN),
    (0, 7, 4, 9, SHORTS),
    (0, 9, 1, 11, SKIN),
    (3, 9, 4, 11, SKIN),
    (0, 11, 1, 12, SHORTS),
    (3, 11, 4, 12, SHORTS),
]


def paint_street(img):
    rect(img, 0, GROUND, img.width, ROAD_TOP, WALK)
    rect(img, 0, ROAD_TOP - 1, img.width, ROAD_TOP, WALK_DARK)
    rect(img, 152, GROUND + 2, 206, GROUND + 3, YELLOW)
    rect(img, 0, ROAD_TOP, img.width, HEIGHT, ROAD)
    for row, y in enumerate(range(ROAD_TOP + 1, HEIGHT, 3)):
        rect(img, 150 - row * 4, y, 210 + row * 4, y + 2, STRIPE)


def paint_figure(img, x=214, y=GROUND - 11):
    for x0, y0, x1, y1, color in FIGURE:
        rect(img, x + x0, y + y0, x + x1, y + y1, color)
