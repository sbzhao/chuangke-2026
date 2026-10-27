# 《去看一眼》32 页绘本 · 绘图工作区

更新日期：2026-10-27  
用途：给 codex imagegen 逐页生成插画，再排版成 32 页绘本  
故事文字稿：`../故事绘本_去看一眼_文字稿_2026-10-27.md`  
视频方案：`../视频生成方案_去看一眼_2026-10-26.md`

---

## 1. 目录里有什么

| 文件 | 内容 |
|---|---|
| `README.md` | 成书规格、视觉风格、角色/场景设定、全局提示词、工作流 |
| `32页绘本版式.md` | 32 页逐页结构：页码、类型、正文文字、画面描述、文字区 |
| `32页提示词.md` | 32 条可直接复制的绘图提示词，按页码排列 |

---

## 2. 成书规格

| 项目 | 建议 |
|---|---|
| 开本 | 16 开竖版，210 × 285 mm（或 8.5 × 11 in） |
| 页数 | 32 页（含封面、环衬、扉页、献词、正文、作者的话、知识页、封底） |
| 图片比例 | **3:4 竖版**（建议 1536 × 2048 或 1024 × 1365） |
| 出血 | 3 mm |
| 文字安全区 | 距裁切线 10 mm |
| 正文字体 | 思源宋体 / 霞鹜文楷；16–18 pt |
| 标题字体 | 思源黑体 / 站酷快乐体；28–36 pt |
| 纸张 | 157 g 哑粉纸；封面 250 g 铜版纸 + 哑膜 |
| 装订 | 精装 / 锁线胶装；先做一本数码样书 |

> 32 页是“页”不是“张”。印刷时一张大纸印 2 页（正反），实际是 16 张纸对折。

---

## 3. 视觉风格

**一句话：** 手绘水粉 + 彩铅，深靛蓝的太空，暖琥珀的飞船灯光，温柔、神秘、不吓人。

- **媒介感**：水粉、彩铅、纸张纹理、轻微颗粒；不要 3D 渲染、不要塑料感。
- **颜色**：深靛蓝 `#0B1420`、午夜蓝 `#1B2A41`、冰蓝 `#5B7C99`、暖琥珀 `#E8A24A`、黄铜 `#B08D57`、纸白 `#F2E8D5`。
- **光线**：单一冷光勾轮廓，暖光只出现在飞船窗口、控制台、瞳孔里的倒影。
- **形状**：圆润、友好；石头可以有棱角，但不要尖锐。
- **角色**：10–12 岁的中国孩子，深蓝远征外套，左胸一枚五瓣岩石徽章。
- **情绪**：好奇 → 紧张 → 安静 → 敬畏；结尾不是恐怖，是“被看见”的安静。
- **文字**：图片里**不要生成任何文字**；标题、页码、正文全部后期排版。

---

## 4. 角色设定（每次出现都照这个写）

| 姓名 | 角色 | 外形 | 道具/习惯 |
|---|---|---|---|
| **张铭轩** | 指令长 | 12 岁男孩，短黑发，个子最高，表情稳 | 深蓝外套 + 徽章；平板；下命令前敲三下控制台 |
| **张楚珺** | 驾驶员 | 11 岁女孩，黑色马尾，圆脸，星星发卡 | 深蓝外套；饼干罐；每天数一遍 43 块饼干 |
| **汤兴昊** | 机械臂手 | 11 岁男孩，短发，护目镜推在额头上，微胖 | 深蓝外套；一只大拇指破洞的幸运手套 |
| **赵以清** | 科学官 | 12 岁女孩，黑长发扎起，圆框眼镜 | 深蓝外套；《奇怪，但是真的》笔记本 + 铅笔 |
| **王一初** | 通讯员 | 10 岁男孩，卷发，头顶一撮翘起来的“天线” | 深蓝外套；头戴耳机，耳机边有一点暖光 |

**共同点：** 深蓝灰外套、黑色内搭、左胸五瓣岩石徽章；不要穿绿色、不要大 logo、不要反光面料。

**英文提示词写法（直接复制到每条人物提示词里）：**

```text
a calm 12-year-old Chinese boy with short black hair, dark blue expedition jacket, small brass five-petal badge, holding a tablet (commander)
an 11-year-old Chinese girl with a black ponytail, small star hairpin, dark blue jacket, holding a cookie tin (pilot)
an 11-year-old Chinese boy with short hair, goggles pushed up on his forehead, one worn glove with a hole in the thumb, dark blue jacket (arm operator)
a 12-year-old Chinese girl with round glasses, long black hair tied back, dark blue jacket, holding a notebook and pencil (science officer)
a 10-year-old Chinese boy with curly hair, a small antenna-like tuft, headphones with a warm light, dark blue jacket (comms officer)
```

---

## 5. 场景与道具设定（每次出现都照这个写）

| 对象 | 外形 | 提示词关键词 |
|---|---|---|
| **回声号** | 小型科考飞船，像银色陀螺；圆柱形居住环；尾部一盏暖黄小灯；灰白旧船体；细天线 | `a small silver research spaceship like a spinning top, cylindrical habitat ring, one warm yellow tail light, weathered white-gray hull, thin antenna` |
| **蓝珠** | 蓝色冰矮行星，像冻住的玻璃弹珠；白色冰斑；薄薄蓝色雾 | `a blue ice dwarf planet like a frozen glass marble, white ice patches, thin blue haze` |
| **K-16** | 不规则深灰褐小石头，像被咬了一口的土豆；表面有坑；一小片光滑反光面 | `a small irregular dark gray-brown asteroid like a bitten potato, cratered, one smooth reflective facet` |
| **伴星** | 陨石形深色石头；两个黑坑 + 一道弯弯山脊，像闭着的眼；睁开后是深色玻璃质表面 | `a distant meteorite-shaped dark asteroid with two dark crater pits and a long curved ridge like a closed eye` |
| **花瓣抓手** | 五瓣黄铜 + 深色金属机械花；关节有细划痕 | `a five-petaled brass and dark metal mechanical gripper like a flower` |
| **万花筒舱** | 三角形玻璃样本舱；黄铜框；三面镜子；无限反射 | `a triangular glass sample chamber with a brass frame and mirrors, infinite reflections` |
| **观察舱** | 圆柱形舱体；巨大圆形舷窗；金属肋条；冷蓝光；中央全息台 | `a cylindrical spaceship observation deck with a huge circular window, metal ribs, cold blue light, a central holographic display` |

---

## 6. 全局风格前缀

把这段放在**每一条**提示词的最前面（`32页提示词.md` 里已经帮你拼好）：

```text
Children's picture book illustration, hand-painted gouache and colored pencil on textured paper, soft edges, deep indigo and midnight blue palette with warm amber and brass accents, gentle cinematic lighting, rounded friendly shapes, storybook composition, child-friendly, not scary, 3:4 portrait, no text, no watermark, no logo.
```

## 7. 全局负向提示词

如果工具支持 negative prompt，把这段放进去：

```text
text, letters, watermark, logo, photorealistic, 3D render, CGI, anime, manga, horror, creepy, sharp teeth, blood, weapon, extra limbs, deformed hands, extra fingers, blurry, low resolution, oversaturated, neon, plastic
```

如果工具不支持负向提示词，就把 `no text, no watermark, no logo, not scary, child-friendly` 写进正向提示词，并在出图后人工筛掉带文字/恐怖感的版本。

---

## 8. 一致性技巧（32 张图不“换人”的关键）

1. **先做 5 张“锚点图”**：
   - `p04_crew.png`：五个人的合照（角色参考）
   - `p07_ship.png`：回声号全身（飞船参考）
   - `p09_planet_rock.png`：蓝珠 + K-16（天体参考）
   - `p22_closed_eye.png`：伴星闭眼（石头参考）
   - `p23_eye_open.png`：伴星睁眼（眼睛参考）
2. 后面每页生成时，把对应的锚点图作为 **image reference / 参考图** 传给 codex imagegen；如果工具支持 seed，固定同一个 seed 的“风格种子”。
3. 每条人物提示词都重复同一套外形描述（发型、眼镜、手套、耳机、徽章），不要只写“the commander”。
4. 一页只画一个瞬间；不要把“张开 + 合拢 + 抓住”塞进同一张图。
5. 先生成 2–4 个版本，选最接近锚点图的一张；不要一张不满意就无限重抽。
6. 所有图统一后期加纸张纹理、轻微颗粒、暗角；这样即使模型有细微色差，成书也会统一。
7. **图片里不要出现文字**；所有文字后期排版。模型最容易把中文画成乱码。

---

## 9. 文件命名

```text
绘本/
├── 参考图/
│   ├── p04_crew.png
│   ├── p07_ship.png
│   ├── p09_planet_rock.png
│   ├── p22_closed_eye.png
│   └── p23_eye_open.png
├── 生成原图/
│   ├── p01_cover_v1.png
│   ├── p01_cover_v2.png
│   └── ...
├── 选图/
│   ├── p01_cover.png
│   ├── p02_endpaper.png
│   └── ... p32_backcover.png
└── 排版/
    └── book_32p.indd / .afpub / .pdf
```

建议：`生成原图` 保留每页 2–4 个版本；`选图` 只放最终一张，文件名固定，方便排版软件自动链接。

---

## 10. 推荐工作流

1. **读版式**：打开 `32页绘本版式.md`，确认每页文字和画面。
2. **做锚点图**：先生成 p04、p07、p09、p22、p23，选 5 张最满意的。
3. **逐页生成**：按 `32页提示词.md` 从 p01 到 p32；每页 2–4 版；用锚点图做参考。
4. **选图**：把最终图放进 `选图/`，文件名按 `p01_cover.png` … `p32_backcover.png`。
5. **排版**：按 32 页版式放入文字；标题、页码、正文后期加。
6. **调色**：统一纸张纹理、颗粒、暗角；整体压暗 5%，暖光提一点。
7. **打样**：先打印一本黑白样书检查文字位置，再打彩色样书。
8. **检查**：角色是否 5 个人都对、石头是否同一块、眼睛是否同一只、每页是否留了文字区。

---

## 11. 32 页结构速览

| 页 | 内容 | 文字量 |
|---|---|---|
| p01 | 封面 | 标题 + 副标题 + 一句话 |
| p02 | 环衬 | 无字 |
| p03 | 扉页 | 标题 + 副标题 + 献词 |
| p04 | 五名船员 | 名字/角色 |
| p05 | 黑暗里的眨眼 | 中 |
| p06 | 地球上的人 | 中 |
| p07 | 回声号 | 中 |
| p08 | 船上的五个人 | 多（可做跨页） |
| p09 | 蓝珠与 K-16 | 中 |
| p10 | 不是信号 | 中 |
| p11 | 第二颗 | 中 |
| p12 | 只取一块 | 中 |
| p13 | 金属花 | 少 |
| p14 | 三次落空 | 少 |
| p15 | 像在等我们 | 少 |
| p16 | 咔哒 | 少 |
| p17 | 空空的圆 | 少 |
| p18 | 多闪了一下 | 中 |
| p19 | 一千个它 | 中 |
| p20 | 返航 | 中 |
| p21 | 再看它一眼 | 少 |
| p22 | 闭着的眼睛 | 中 |
| p23 | 睁开 | 少（大图） |
| p24 | 它只看过一样东西 | 少（大图） |
| p25 | 回家的路 | 中 |
| p26 | 后悔吗 | 中 |
| p27 | 如果你也去 | 中 |
| p28 | 我们走了 | 少（大图） |
| p29 | 无字/留白 | 无字 |
| p30 | 作者的话 | 多 |
| p31 | 知识小口袋 | 多 |
| p32 | 封底 | 一句话 |

---

## 12. 排版小建议

- 图占 70–80%，文字占 20–30%；文字尽量放在天空、暗部、海面这类“负空间”里。
- 文字不要压在人物脸上；不要压在眼睛上。
- 关键页（p23、p24、p28、p29）少字或留白，让画面自己说话。
- 每页文字 2–4 段，每段 1–2 句；朗读时一页停 2 秒。
- 页码放在外侧下角，不要压图；封面、环衬、封底不放页码。
- 标题、页码、正文用同一套字体；正文不要用花体，孩子要能读。
