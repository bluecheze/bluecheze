BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def put(img, x, y, color):
    if 0 <= x < img.width and 0 <= y < img.height:
        img.putpixel((x, y), color)


def rect(img, x0, y0, x1, y1, color):
    for y in range(y0, y1):
        for x in range(x0, x1):
            put(img, x, y, color)


def dithered(x, y, amount):
    return BAYER[y % 4][x % 4] < amount * 16
