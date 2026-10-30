# H3-Max 视频固定设定图

生成日期：2026-10-30
用途：为 MiniMax H3-Max 视频请求提供人物、飞船、场景、道具和关键动作参考。

## 资产总览

当前目录中有 **63 张可用设定图**：原计划 62 张，加上单独重做的赵以清新版定妆照 1 张。`drafts/` 下另保留 9 张工作草稿，不要作为正式参考图输入 H3-Max。

| 类别 | 数量 | 目录 |
|---|---:|---|
| 回声号飞船外观、侧视、发动机/散热板、木星加速 | 4 | `ship/` |
| 舰桥主屏、机械臂控制台、样本舱、采样区及四处岗位控制台 | 8 | `bridge/` |
| 冰川折线科考服正、背、侧 | 3 | `suit/` |
| 样本小石头、伴星三状态、木星云带 | 5 | `objects/` |
| 五人正面/侧面/背面，以及五人专注表情 | 20 | `characters/` |
| 五瓣抓手三状态、机械臂六状态 | 9 | `mechanics/` |
| 机械臂连接、样本舱开闭、采样前后空间状态、四组动作首尾帧 | 13 | `continuity/`、`keyframes/` |
| 赵以清按新照片单独重做的定妆照 | 1（计入上表人物集的额外版本） | `characters/` |

## 统一设定

- 飞船：回声号，浅灰白大型科考船，圆钝船首、单个大型环形结构、后部发动机与散热板、侧面采样区。各外景保持船首朝向、环的位置及采样区位置一致。
- 舰桥：沿用 `bridge_topview_v4.png` 和 `bridge_cutaway_v2.png` 的布局与灯光。屏幕画面保持空白或只有低亮青色边光；精确界面和字卡在后期添加。
- 人物：以成员本人照片为身份参考，服装采用“冰川折线”。张铭轩、张楚珺不戴眼镜；汤兴昊、赵以清、王一初戴浅色眼镜。赵以清新版定妆照的身份参考为 `members/赵以清3.jpg`。
- 样本：唯一一块灰褐色凹坑小石头，表面有一处平滑反光面；不得与远处大型伴星混为一物。
- 机械臂：始终固定连接船体，动作按接近、接触、抓牢、回收、送入、固定、释放、回折表现。抓手保持五瓣。
- 伴星：外轮廓与弧形山脊保持一致；反光是飞船暖光映射，开启缓慢克制，不画成自发光或恐怖眼睛。
- 场景：木星只出现在引力辅助参考中。柯伊伯带采样镜头不出现木星，不显示精确距离。空间保持稀疏，避免密集碎石隧道。

## 关键动作帧

四组起始/结束画面配对存放，供 H3-Max 提示词锁定动作起止状态：

1. `keyframes/start/approach_start_v1.png` → `keyframes/end/approach_end_v1.png`
2. `keyframes/start/grasp_start_v1.png` → `keyframes/end/grasp_end_v1.png`
3. `keyframes/start/transfer_start_v1.png` → `keyframes/end/transfer_end_v1.png`
4. `keyframes/start/companion_start_v1.png` → `keyframes/end/companion_end_v1.png`

## 草稿说明

`bridge/drafts/` 中的四张早期舰桥图有伪界面纹理；请使用 `bridge/details/` 和 `bridge/stations/` 中的正式版本。`continuity/drafts/` 留有重复参考和一张旧的采样后空间图，仅作过程记录；正式的采样前后状态在 `continuity/sampling_space_before_v1.png` 与 `continuity/sampling_space_after_v1.png`。

## 与旧方案的冲突处理

旧故事背景文档仍出现旧服装/眼镜描述和精确距离。制作提示词应以本资产目录、已确认的冰川折线设定和“不出现精确距离”的要求为准；不要复制旧数值。此清单不会替代原故事方案，只为防止后续视频生成误用过期设定。
