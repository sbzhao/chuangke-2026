#!/usr/bin/env python3
"""Export text overlays and five-second credits over the reviewed 90s cut."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / 'review' / (sys.argv[2] if len(sys.argv) > 2 else '无台词版')
TITLES = ROOT / 'review/无台词版/titles'
OUTPUT = ROOT / 'output' / (sys.argv[1] if len(sys.argv) > 1 else '去看一眼_480P无台词完整版_v1.mp4')
audio_check = json.loads((REVIEW / '原音轨识别.json').read_text())
if audio_check.get('text', '').strip() or audio_check.get('n_speakers', 0):
    raise RuntimeError('Source soundtrack needs review: ASR detected speech.')

args = ['ffmpeg', '-v', 'error', '-n', '-i', str(REVIEW / '90秒原音轨剪辑.mp4')]
for name in ['title', 'jupiter', 'kuiper', 'period', 'later', 'sealed', 'credits']:
    args += ['-loop', '1', '-framerate', '24', '-i', str(TITLES / (name + '.png'))]
filters = ['[0:v]trim=duration=90,setpts=PTS-STARTPTS,fade=t=in:st=0:d=0.4,fade=t=out:st=89.2:d=0.8[v0]']
for index, (start, end) in enumerate([(0.5, 3.2), (4, 7.7), (8.3, 11.8), (24, 27.6), (38.2, 41.5), (70.2, 73.5)], 1):
    filters += [f"[v{index-1}][{index}:v]overlay=0:0:enable='between(t,{start},{end})':eof_action=repeat:shortest=1[v{index}]"]
filters += ['[7:v]trim=duration=5,setpts=PTS-STARTPTS,setsar=1,format=yuv420p[credit]',
            '[v6][credit]concat=n=2:v=1:a=0,format=yuv420p[v]',
            '[0:a]atrim=duration=90,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.4,afade=t=out:st=88.8:d=1.2,apad=whole_dur=95,atrim=duration=95[a]']
args += ['-filter_complex', ';'.join(filters), '-map', '[v]', '-map', '[a]', '-t', '95',
         '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-r', '24', '-pix_fmt', 'yuv420p',
         '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', str(OUTPUT)]
subprocess.run(args, check=True)
print(OUTPUT)
