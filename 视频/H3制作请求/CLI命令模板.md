# CLI 命令模板（尚不可直接批量执行）

从项目根目录执行。refs参考图已由imagegen生成并完成初步视觉检查，正式视频前请核对人物身份；audio/*.wav仍待制作。完成童声试听、测长和时间轴调整后，再单条执行。每条命令是一笔生成请求；不得自动全批运行或失败重投。引用图片仅作为条件，时间线以提示词为准。

### 01 遥远的眨光

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/01.txt)" \
  --duration 10 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/world_star.png' \
  --reference-audio '视频/H3制作请求/audio/01_01_旁白.wav' \
  --download 视频/H3制作请求/output/01.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 02 途中：木星引力辅助

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/02.txt)" \
  --duration 6 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/ship.png' \
  --reference-image '视频/H3制作请求/refs/jupiter.png' \
  --reference-audio '视频/H3制作请求/audio/02_01_旁白.wav' \
  --download 视频/H3制作请求/output/02.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 03 抵达柯伊伯带

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/03.txt)" \
  --duration 5 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/ship.png' \
  --reference-image '视频/H3制作请求/refs/world_wide.png' \
  --reference-audio '视频/H3制作请求/audio/03_01_旁白.wav' \
  --download 视频/H3制作请求/output/03.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 04 驾驶员与科学官判断

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/04.txt)" \
  --duration 9 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/cabin.png' \
  --reference-image '视频/H3制作请求/refs/张楚珺.png' \
  --reference-image '视频/H3制作请求/refs/赵以清.png' \
  --reference-audio '视频/H3制作请求/audio/04_mix.wav' \
  --download 视频/H3制作请求/output/04.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 05 指令长下令

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/05.txt)" \
  --duration 9 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/cabin.png' \
  --reference-image '视频/H3制作请求/refs/张铭轩.png' \
  --reference-audio '视频/H3制作请求/audio/05_01_张铭轩.wav' \
  --download 视频/H3制作请求/output/05.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 06 相伴的两颗石头

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/06.txt)" \
  --duration 9 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/world_wide.png' \
  --reference-image '视频/H3制作请求/refs/rock.png' \
  --reference-image '视频/H3制作请求/refs/companion_closed.png' \
  --reference-audio '视频/H3制作请求/audio/06_01_旁白.wav' \
  --download 视频/H3制作请求/output/06.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 07 第一次接近落空

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/07.txt)" \
  --duration 6 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/arm.png' \
  --reference-image '视频/H3制作请求/refs/rock.png' \
  --reference-image '视频/H3制作请求/refs/汤兴昊_station-v2.png' \
  --reference-audio '视频/H3制作请求/audio/07_01_汤兴昊.wav' \
  --download 视频/H3制作请求/output/07.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 08 等待下一个窗口

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/08.txt)" \
  --duration 7 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/cabin.png' \
  --reference-image '视频/H3制作请求/refs/汤兴昊.png' \
  --reference-image '视频/H3制作请求/refs/张楚珺.png' \
  --reference-audio '视频/H3制作请求/audio/08_01_张楚珺.wav' \
  --download 视频/H3制作请求/output/08.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 09 窗口将至

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/09.txt)" \
  --duration 6 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/cabin.png' \
  --reference-image '视频/H3制作请求/refs/赵以清.png' \
  --reference-audio '视频/H3制作请求/audio/09_01_赵以清.wav' \
  --download 视频/H3制作请求/output/09.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 10 五瓣抓手锁定

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/10.txt)" \
  --duration 6 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/arm.png' \
  --reference-image '视频/H3制作请求/refs/rock.png' \
  --reference-audio '视频/H3制作请求/audio/10_01_汤兴昊.wav' \
  --download 视频/H3制作请求/output/10.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 11 缓慢带离

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/11.txt)" \
  --duration 7 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/arm.png' \
  --reference-image '视频/H3制作请求/refs/rock.png' \
  --reference-image '视频/H3制作请求/refs/world_wide.png' \
  --reference-audio '视频/H3制作请求/audio/11_01_旁白.wav' \
  --download 视频/H3制作请求/output/11.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 12 多出的一次闪光

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/12.txt)" \
  --duration 7 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/cabin.png' \
  --reference-image '视频/H3制作请求/refs/赵以清.png' \
  --reference-image '视频/H3制作请求/refs/companion_closed.png' \
  --reference-audio '视频/H3制作请求/audio/12_01_赵以清.wav' \
  --download 视频/H3制作请求/output/12.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 13 样本进入三角舱

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/13.txt)" \
  --duration 8 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/arm.png' \
  --reference-image '视频/H3制作请求/refs/rock.png' \
  --reference-image '视频/H3制作请求/refs/chamber-v2.png' \
  --reference-audio '视频/H3制作请求/audio/13_01_旁白.wav' \
  --download 视频/H3制作请求/output/13.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 14 一千个倒影

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/14.txt)" \
  --duration 9 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/chamber-v2.png' \
  --reference-image '视频/H3制作请求/refs/rock.png' \
  --reference-image '视频/H3制作请求/refs/cabin.png' \
  --reference-image '视频/H3制作请求/refs/王一初.png' \
  --reference-audio '视频/H3制作请求/audio/14_mix.wav' \
  --download 视频/H3制作请求/output/14.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 15 返航姿态调整

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/15.txt)" \
  --duration 5 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/ship.png' \
  --reference-image '视频/H3制作请求/refs/world_wide.png' \
  --download 视频/H3制作请求/output/15.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 16 再看一眼

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/16.txt)" \
  --duration 5 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/cabin.png' \
  --reference-image '视频/H3制作请求/refs/张铭轩.png' \
  --reference-audio '视频/H3制作请求/audio/16_01_张铭轩.wav' \
  --download 视频/H3制作请求/output/16.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 17 回望与睁开

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/17.txt)" \
  --duration 7 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/cabin.png' \
  --reference-image '视频/H3制作请求/refs/companion_closed.png' \
  --reference-image '视频/H3制作请求/refs/companion_open-v2.png' \
  --reference-audio '视频/H3制作请求/audio/17_01_旁白.wav' \
  --download 视频/H3制作请求/output/17.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```

### 18 它看着我们

```bash
mmx video generate \
  --model MiniMax-H3 \
  --prompt "$(cat 视频/H3制作请求/prompts/18.txt)" \
  --duration 5 --ratio 16:9 \
  --reference-image '视频/H3制作请求/refs/companion_open-v2.png' \
  --reference-image '视频/H3制作请求/refs/ship.png' \
  --reference-audio '视频/H3制作请求/audio/18_01_旁白.wav' \
  --download 视频/H3制作请求/output/18.mp4 \
  --poll-interval 10 --timeout 1800 --non-interactive
```
