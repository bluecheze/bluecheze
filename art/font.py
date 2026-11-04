from palette import CREAM, INK
from pixels import rect

GLYPHS = {
    "b": ["#....", "#....", "####.", "#...#", "#...#", "#...#", "####."],
    "c": [".....", ".....", ".###.", "#...#", "#....", "#...#", ".###."],
    "e": [".....", ".....", ".###.", "#...#", "#####", "#....", ".###."],
    "h": ["#....", "#....", "####.", "#...#", "#...#", "#...#", "#...#"],
    "l": [".##..", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "n": [".....", ".....", "####.", "#...#", "#...#", "#...#", "#...#"],
    "o": [".....", ".....", ".###.", "#...#", "#...#", "#...#", ".###."],
    "p": [".....", ".....", "####.", "#...#", "####.", "#....", "#...."],
    "r": [".....", ".....", "#.##.", "##..#", "#....", "#....", "#...."],
    "s": [".....", ".....", ".####", "#....", ".###.", "....#", "####."],
    "t": [".#...", ".#...", "####.", ".#...", ".#...", ".#..#", "..##."],
    "u": [".....", ".....", "#...#", "#...#", "#...#", "#..##", ".##.#"],
    "z": [".....", ".....", "#####", "...#.", "..#..", ".#...", "#####"],
    " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
}


def paint_glyph(img, glyph, x, y, scale, color):
    for row, line in enumerate(glyph):
        for col, cell in enumerate(line):
            if cell == "#":
                px, py = x + col * scale, y + row * scale
                rect(img, px, py, px + scale, py + scale, color)


OUTLINE = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1, 2) if (dx, dy) != (0, 0)]


def paint_text(img, text, x, y, scale=1, color=CREAM, shadow=INK):
    for i, char in enumerate(text):
        left = x + i * 6 * scale
        for dx, dy in OUTLINE:
            paint_glyph(img, GLYPHS[char], left + dx, y + dy, scale, shadow)
        paint_glyph(img, GLYPHS[char], left, y, scale, color)


def paint_title(img, x, y, color=CREAM, shadow=INK):
    paint_text(img, "bluecheze", x, y, 3, color, shadow)
    paint_text(img, "open source tools", x, y + 28, 2, color, shadow)
