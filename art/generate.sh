#!/bin/sh
set -e
cd "$(dirname "$0")"
mflux-generate-flux2 --model flux2-klein-4b -q 8 --width 1536 --height 512 --seed 11 \
  --prompt "Wide panoramic illustration of a quiet sunlit forest in late summer, screen print style with fine pen hatching. Tall old trees with thick textured trunks and lush green canopy. On the right side, a young person in a white shirt sits on the mossy ground leaning back against a big tree trunk, relaxed, eyes closed, a small orange backpack beside them. Soft golden sun rays shining through gaps in the leaves, dappled light spots on the grass and ferns. The left side opens into a bright hazy glade with soft light and few details. Limited palette: deep forest green, sage, warm gold, cream, touches of cobalt blue in the shadows. Clean, detailed, calm, peaceful." \
  --output source.png
