from PIL import Image


def palette_with_accents(adaptive, count, accents):
    colors = adaptive.getpalette()[: 3 * count]
    for accent in accents:
        colors += list(accent)
    padding = colors[:3] * (256 - len(colors) // 3)
    holder = Image.new("P", (1, 1))
    holder.putpalette(colors + padding)
    return holder


def pixelate(img, grid_width, colors, accents=()):
    grid_height = round(grid_width * img.height / img.width)
    small = img.convert("RGB").resize((grid_width, grid_height), Image.Resampling.BOX)
    count = colors - len(accents)
    adaptive = small.quantize(colors=count, method=Image.Quantize.MEDIANCUT, kmeans=3)
    palette = palette_with_accents(adaptive, count, accents)
    return small.quantize(palette=palette, dither=Image.Dither.NONE).convert("RGB")


def upscale(img, width):
    scale = width // img.width
    return img.resize((img.width * scale, img.height * scale), Image.Resampling.NEAREST)
