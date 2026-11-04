#!/bin/sh
set -e
cd "$(dirname "$0")"
mflux-generate-flux2 --model flux2-klein-4b -q 8 --width 1536 --height 512 --seed 21 \
  --prompt "Wide panoramic illustration of a quiet Japanese seaside town street in midsummer, screen print style with fine pen hatching. Deep saturated cobalt blue sky. A gigantic towering cumulus cloud on the right half, cream white, drawn with dense fine ink hatching lines for shading. A wooden utility pole on the left with black power lines stretching across the sky. A small two story house with blue vertical wooden siding and a bright yellow corner shop front with a yellow door. Calm deep blue ocean horizon behind. Salmon pink road in the foreground with white crosswalk stripes. A small student with an orange backpack standing on the sidewalk. Clear open sky in the upper left. Limited palette: cobalt blue, cream, yellow, salmon pink. Clean, detailed, calm." \
  --output source.png
