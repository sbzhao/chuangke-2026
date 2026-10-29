#!/usr/bin/env python3
"""Keep the target rock; omit an inconsistent far companion in generated N03."""
from pathlib import Path
import subprocess
import json

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / 'review/无台词版'
target = REVIEW / 'N03_edit.mp4'
backup = REVIEW / 'N03_edit_before_target_crop.mp4'
if target.exists() and not backup.exists():
    target.rename(backup)
filters = (
    '[0:v]split=2[v0][v1];'
    '[v0]trim=start=0:end=6,setpts=PTS-STARTPTS,scale=832:480,pad=854:480:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24[a];'
    '[v1]trim=start=6:end=9,setpts=(PTS-STARTPTS)*4/3,crop=620:348:0:90,scale=854:480,setsar=1,fps=24[b];'
    '[a][b]concat=n=2:v=1:a=0,tpad=stop_mode=clone:stop_duration=0.1,trim=duration=10[v]'
)
if not target.exists():
    subprocess.run(['ffmpeg', '-v', 'error', '-n', '-i', str(ROOT/'output/N03_识别_480P_v1.mp4'),
                    '-i', str(backup), '-filter_complex', filters, '-map', '[v]', '-map', '1:a',
                    '-t', '10', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                    '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-ac', '2', str(target)], check=True)
rough = REVIEW / '90秒原音轨剪辑.mp4'
old = REVIEW / '90秒原音轨剪辑_调整前.mp4'
if rough.exists() and not old.exists():
    rough.rename(old)
if not rough.exists():
    subprocess.run(['ffmpeg', '-v', 'error', '-n', '-f', 'concat', '-safe', '0', '-i', str(REVIEW/'concat.txt'),
                    '-c', 'copy', '-movflags', '+faststart', str(rough)], check=True)
timeline = json.loads((REVIEW/'剪辑时间线.json').read_text())
for row in timeline:
    if row['id'] == 'N03':
        row['refinement'] = '0–6s crew; 6–9s rock crop excluding inconsistent companion, stretched to 4s; original 10s nonverbal audio retained'
(REVIEW/'剪辑时间线.json').write_text(json.dumps(timeline, ensure_ascii=False, indent=2)+'\n')
