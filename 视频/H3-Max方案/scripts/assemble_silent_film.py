#!/usr/bin/env python3
"""Deterministic 90-second picture cut + five-second credits, retaining originals."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'review/无台词版'
TITLES = OUT / 'titles'
EDITS = [
    ('N01', 'P01_大船外景_480P_v1.mp4', 0, 8),
    ('N02', 'N02_抵达_480P_v1.mp4', 0, 10),
    ('N03', 'N03_识别_480P_v1.mp4', 0, 10),
    ('N04', 'N04_接近_480P_v1.mp4', 0.5, 10),
    ('N05', 'N05_等待_480P_v1.mp4', 2, 9),
    ('N06', 'N06_抓取_480P_v2.mp4', 1, 10),
    ('N07', 'N07_封装_480P_v1.mp4', 1.5, 13),
    ('N08', 'N08_异常_480P_v1.mp4', 1, 10),
    ('N09', 'N09_回望_480P_v1.mp4', 2, 10),
]

def run(args):
    subprocess.run(['ffmpeg', '-v', 'error', '-n'] + args, check=True)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    timeline = []
    time = 0
    for identifier, source, start, length in EDITS:
        target = OUT / (identifier + '_edit.mp4')
        timeline.append({'id': identifier, 'source': source, 'source_start': start,
                         'duration': length, 'film_start': time, 'film_end': time + length})
        time += length
        if not target.exists():
            run(['-ss', str(start), '-i', str(ROOT / 'output' / source), '-t', str(length),
                 '-vf', 'scale=832:480:force_original_aspect_ratio=decrease,pad=854:480:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24',
                 '-af', f'aresample=48000,afade=t=in:st=0:d=0.08,afade=t=out:st={length-0.12}:d=0.12',
                 '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                 '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-ac', '2', str(target)])
    assert time == 90
    (OUT / '剪辑时间线.json').write_text(json.dumps(timeline, ensure_ascii=False, indent=2)+'\n')
    concat = OUT / 'concat.txt'
    concat.write_text(''.join("file '" + row['id'] + "_edit.mp4'\n" for row in timeline))
    rough = OUT / '90秒原音轨剪辑.mp4'
    if not rough.exists():
        run(['-f', 'concat', '-safe', '0', '-i', str(concat), '-c', 'copy', '-movflags', '+faststart', str(rough)])
    sound = OUT / '原音轨检查.wav'
    if not sound.exists():
        run(['-i', str(rough), '-vn', '-ac', '1', '-ar', '16000', '-c:a', 'pcm_s16le', str(sound)])
    print('90-second cut and source audio prepared', flush=True)

if __name__ == '__main__':
    main()
