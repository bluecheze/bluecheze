import math

from layout import HORIZON
from palette import CLOUD, CLOUD_DEEP, CLOUD_LIGHT, CLOUD_SHADE
from pixels import put

LIGHT = (0.55, -0.83)

TOWER = [
    (176, 12, 10), (192, 8, 9), (168, 17, 8),
    (162, 30, 12), (183, 25, 14), (205, 31, 11),
    (150, 50, 12), (172, 44, 15), (196, 46, 14), (219, 50, 11),
    (122, 60, 7), (138, 55, 9),
    (130, 66, 9), (148, 64, 11), (168, 62, 12), (190, 63, 12),
    (212, 64, 11), (232, 66, 10), (252, 67, 8), (270, 69, 6),
]

WISPS = [
    (8, 69, 4), (16, 68, 5), (24, 70, 3),
    (282, 40, 4), (290, 42, 3), (296, 41, 3),
]


def inside_blob(x, y, cx, cy, r):
    angle = math.atan2(y - cy, x - cx)
    bumpy = r * (1 + 0.1 * math.sin(6 * angle + cx))
    return (x - cx) ** 2 + (y - cy) ** 2 <= bumpy * bumpy


def build_mask(blobs):
    mask = {}
    for index, (cx, cy, r) in enumerate(blobs):
        for y in range(cy - r - 2, min(cy + r + 2, HORIZON - 1) + 1):
            for x in range(cx - r - 2, cx + r + 3):
                if inside_blob(x, y, cx, cy, r):
                    mask[(x, y)] = index
    return mask


def toward_light(x, y, steps):
    return round(x + LIGHT[0] * steps), round(y + LIGHT[1] * steps)


def facing(x, y, blob):
    cx, cy, r = blob
    return ((x - cx) * LIGHT[0] + (y - cy) * LIGHT[1]) / r


def shade(x, y, mask, blobs):
    if toward_light(x, y, 3) not in mask:
        return CLOUD_LIGHT
    if toward_light(x, y, -3) not in mask:
        return CLOUD_DEEP if (x - y) % 3 == 0 else CLOUD_SHADE
    side = facing(x, y, blobs[mask[(x, y)]])
    if side > 0.55:
        return CLOUD_LIGHT
    if side < -0.7:
        return CLOUD_DEEP if (x - y) % 3 == 0 else CLOUD_SHADE
    if side < -0.3:
        return CLOUD_SHADE if (x + y) % 3 == 0 else CLOUD
    return CLOUD


def paint_group(img, blobs):
    mask = build_mask(blobs)
    for x, y in mask:
        put(img, x, y, shade(x, y, mask, blobs))


def paint_clouds(img):
    paint_group(img, TOWER)
    paint_group(img, WISPS)
