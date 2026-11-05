#!/bin/sh
cd "$(dirname "$0")" || exit 1
ffmpeg -y -i fenjing002.png -i fenjing003.png -i fenjing004.png -filter_complex "$(cat cockpit_gentle_6s.filter)" -map '[out]' -an -t 6 -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -movflags +faststart output_cockpit_gentle_6s_native.mp4
