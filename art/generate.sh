#!/bin/sh
set -e
cd "$(dirname "$0")"
STYLE_REF="${1:?usage: generate.sh <style-reference-image>}"

mflux-generate-flux2 --model flux2-klein-4b -q 4 --low-ram --width 1536 --height 512 --seed 11 \
  --prompt "Wide panoramic illustration of a quiet sunlit forest in late summer, screen print style with fine pen hatching. Tall old trees with thick textured trunks and lush green canopy. On the right side, a young person in a white shirt sits on the mossy ground leaning back against a big tree trunk, relaxed, eyes closed, a small orange backpack beside them. Soft golden sun rays shining through gaps in the leaves, dappled light spots on the grass and ferns. The left side opens into a bright hazy glade with soft light and few details. Limited palette: deep forest green, sage, warm gold, cream, touches of cobalt blue in the shadows. Clean, detailed, calm, peaceful." \
  --output draft.png

mflux-generate-flux2-edit --model flux2-klein-4b -q 4 --low-ram --width 1536 --height 512 --seed 5 \
  --image-paths draft.png "$STYLE_REF" \
  --prompt "Redraw the first image in the exact art style of the second image. Keep the same composition, the same forest, the same young man in a white shirt sitting against the big tree trunk with his orange backpack, the same sun rays. Style: crisp precise black ink linework, dense fine pen hatching on tree trunks and foliage shadows, flat bold saturated screen print colors, high contrast, sharp edges, no haze, no blur, no soft gradients. Rich deep greens, cream highlights, golden sunlight, cobalt blue in the shadows." \
  --output source.png

rm draft.png
