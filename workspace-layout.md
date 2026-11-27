---
name: workspace-layout
description: L1 总图：根到 zone 对照、syn.bat、数据流向、退役禁建表。
up: My rule.md §5
---

# 本机布局总图

工作区只有一层（`D:\MyProjects\<stage>\<project>`）；不再有 A/B 双工作区或挂载缓存树。路径别名见 `My rule.md` §4。各区内部规则按 zone 文件，不在本文件展开。

## 1 根 → zone

| 根 | 角色 | 细则 |
|---|---|---|
| `D:\MyProjects\_DataBase`（`{RAW}`） | 课题原始件（家族桶：`_PHI` / `__zip` / `_thesis`）+ `_` 非课题分支 + `_lab` 历史档只读；除 `_index.csv` / `_diseases.csv` 外只读除非点名 | `zone-database.md`；表结构 `db-schema.md`；D 码 `db-gates.md` |
| `D:\MyProjects\.Del`（`{DEL}`） | AI 可操作临时 / 移出区（`_by-project` / `_by-function`）；**syn 不同步**（`/XD .Del`） | `zone-del.md` |
| `D:\MyProjects\_Docs`（`{doc_root}`） | 语料与可复用层：`_library` / `templates` / `mem` / `GitHub` / `test` / `harvest` | `zone-docs.md`；库分类 `library-taxonomy.md` |
| `D:\MyProjects\_Docs\mem` | bot 记忆导出（仅隐私 + 可变 SSOT）；查阅授权 → `My rule.md` §2 | `execution.md`（mem 口径） |
| `D:\MyProjects` | 分阶段子工程工作区（`drafting` / `pre-submit` / `reviewing` / `accepted`） | `zone-projects.md` |
| `D:\MyProjects\archived` | 已完结项目冷库（非阶段、不进阶段别名） | `zone-projects.md` |

## 2 同步
- `syn.bat`：`D:\MyProjects` → **`E:\Aitor`**（镜像到 Aitor **根**；**不是** `E:\Aitor\MyProjects`）。
- `/XD .Del`：不同步 `.Del`；`_DataBase` 随主树同步。
- 同步入口只有 `D:\MyProjects\syn.bat`（E 侧镜像 `E:\Aitor`）；无其它同步脚本或快捷方式。

## 3 数据角色与单向流（抽象，不改本机盘符）

四个角色单向流转、不回写。本机落点仍按上文 `{RAW}` 与阶段工程根；不把外机盘符写进本仓。

| 角色 | 放什么 | 不放什么 |
|---|---|---|
| 原始影像 | 原始 DICOM；由 DICOM 转出的 NIfTI **视同原始件**（不算处理后图像） | 定位像 / 二次重建、处理后图像、流水线中间件、文本、代码；同一病例 DICOM 与 nii 不得双留 |
| 处理后 | 处理后图像（ROI 外扩、掩膜、配准后、生境掩膜）与流水线 `01–03` / checkpoints / 模型 | 原始影像、整理后的文本（表 / 文档 / 结果 `04–06` / 代码） |
| 归档 | 整理后的文本、数据表、`ref\`、结果 `04–06`、代码仓 | 原始影像、处理后图像、`01–03` 大件 |
| 备份 | 归档侧的单向镜像（排除隔离区） | 把备份当工作盘或数据源，或在备份盘上直接改稿 |

- 转换完成后：nii 留在原始影像侧，原 DICOM 同批移 `{DEL}` 并留台账，不双留。
- 派生图只许新增，禁止覆盖源 seg（输出路径等于输入路径即中止）；写原始盘先 `--dry-run`，经主人点头再执行。

## 4 退役禁建表
下列名称勿重建；机器来源是 `aliases.yaml` 中 `status: retired` 的条目。

| 名称 | 去向 |
|---|---|
| 已退役，不重建：`D:\00ds` / 夹名 `00ds` | 改用 `{RAW}`（`D:\MyProjects\_DataBase`）；活引用算 QC 发现，不得当 legacy 保留 |
| 已退役，不重建：`D:\0script` / 课题根 `0script\` | 改用 `{code_stats}\tools\<fine-id>\` |
| 已退役，不重建：活兄弟根 `R&P` | 申请包 → `_DataBase\_grants\<year>\`；评阅 → `_DataBase\_reviews\{peer,grants,thesis}\<year>\`（细则 `zone-database.md`） |
| 已退役，不重建：`_Docs\_code` | 脚本在 `{code_stats}`；壳与索引移 `{DEL}` |
| 已退役，不重建：`_DataBase\_lab\ethics` | 不设该子树；批件留存 → `library-taxonomy.md` §3 |
| 勿建已退役路径 `_code\04-analysis\stats-analysis` | 改用 `{code_stats}` |
| 已退役，不重建：课题根 `results\` / `analysis\` / `materials\` / `exec\` / `code\` / `gates\` / `writing-refs\` / `raw-pre\` | 改用 `ref\` 地图（`project-ref-layout.md`） |
| 已退役，不重建：`harvest-sources-park` 已吸收批次夹 | 原件去向见 `aliases.yaml`；勿按旧批次名再建 |
| 已退役，不重建：`<family>\_share\ethics` / `_DataBase` 伦理桶 | 伦理材料不进 `{RAW}`；批件与提取物 → `{lib_root}\ethics\`（`library-taxonomy.md` §3） |
