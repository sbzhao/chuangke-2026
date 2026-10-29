#!/usr/bin/env python3
"""Create a separate revision cut; preserve the previous complete film and edits."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / 'review/无台词版'
NEW = ROOT / 'review/片头升级版'
NEW.mkdir(parents=True, exist_ok=True)
SOURCE = ROOT / 'output/R01_史诗引力辅助片头_480P_v1.mp4'
RANGES = [(0.5, 3.5), (5, 7.5), (9, 11.5)]

def run(args):
    subprocess.run(['ffmpeg', '-v', 'error', '-n'] + args, check=True)

target = NEW / 'R01_8秒片头.mp4'
filters = ['[0:v]split=3[v0][v1][v2]', '[0:a]asplit=3[a0][a1][a2]']
for i, (start, end) in enumerate(RANGES):
    length = end - start
    filters += [f'[v{i}]trim=start={start}:end={end},setpts=PTS-STARTPTS,scale=832:480:force_original_aspect_ratio=decrease,pad=854:480:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24[p{i}]',
                f'[a{i}]atrim=start={start}:end={end},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.06,afade=t=out:st={length-0.08}:d=0.08[s{i}]']
filters += ['[p0][s0][p1][s1][p2][s2]concat=n=3:v=1:a=1[v][a]']
if not target.exists():
    run(['-i', str(SOURCE), '-filter_complex', ';'.join(filters), '-map', '[v]', '-map', '[a]', '-t', '8',
         '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
         '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-ac', '2', str(target)])
concat = NEW / 'concat.txt'
sources = [target] + [OLD / f'N{i:02d}_edit.mp4' for i in range(2, 10)]
concat.write_text(''.join("file '" + str(path) + "'\n" for path in sources))
rough = NEW / '90秒原音轨剪辑.mp4'
if not rough.exists():
    run(['-f', 'concat', '-safe', '0', '-i', str(concat), '-c', 'copy', '-movflags', '+faststart', str(rough)])
sound = NEW / '原音轨检查.wav'
if not sound.exists():
    run(['-i', str(rough), '-vn', '-ac', '1', '-ar', '16000', '-c:a', 'pcm_s16le', str(sound)])
timeline = json.loads((OLD / '剪辑时间线.json').read_text())
timeline[0].update(source=SOURCE.name, source_ranges=RANGES, duration=8,
                   note='Epic extreme-wide / near ship / outbound acceleration montage')
(NEW / '剪辑时间线.json').write_text(json.dumps(timeline, ensure_ascii=False, indent=2)+'\n')
print(rough)
