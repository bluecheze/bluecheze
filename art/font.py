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


def paint_text(img, text, x, y, scale=1, color=CREAM):
    for i, char in enumerate(text):
        left = x + i * 6 * scale
        paint_glyph(img, GLYPHS[char], left + scale, y + scale, scale, INK)
        paint_glyph(img, GLYPHS[char], left, y, scale, color)


def paint_title(img, x, y):
    paint_text(img, "bluecheze", x, y, scale=3)
    paint_text(img, "open source tools", x, y + 28, scale=2)
