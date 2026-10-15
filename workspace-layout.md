---
name: workspace-layout
description: A类(L:\00used)与B类(D:\0Grok)工作区的目录与文件约定。临时文件、清理与产出落点仍见 My rule.md 第 5 节。
---

# A 类与 B 类工作区

**A 类**（`L:\00used\<项目>\`）：

- 项目脚本放项目内 `0script\`。
- 项目说明放项目内 `0doc\`。须先说「放 0doc」。
- `0result\` 只放最终表。不放 QC 表、逐受试者中间表、量化参数元数据、运行日志。归属不清先问。
- 从 `derivatives\` 取结果默认复制，不移动。原件留在 `derivatives\`。`0result\` 放副本。
- 能合并的最终表要合并。键相同（如 `participant_id` + `session`）合成一张宽表。描述列只留一份。值列加前缀。合并后的原表移出 `0result\` 前，先获授权。
- 根目录只留：`rawdata\`、`derivatives\`、`atlases\`、清单或索引、`0script\`、`0doc\`、`0result\`。
- 不用 `D:\0Grok\0script\` 存项目脚本。
- 移动脚本或文档前，先搜索 `import`、`addpath`、`settings.ini`、README 的引用。有未更新的引用就不移动。移动后修正内部路径和 `0doc\` 里的调用示例，并实测。
- 日志和失效旧文件的去向是 `L:\0del\<项目名>\`。移动先获授权。临时文件走本节临时文件规则。

**B 类**（`D:\0Grok\<子项目>\`）：

- 可复用脚本放 `D:\0Grok\0script\`。
- 长期规则和参考格式放 `D:\0Grok\0doc\`。须先说「放 0doc」。
- 子项目必须保留的工程文件（设置、预审、证据包、旧稿、`.html`）放子项目 `ref\`。
- 最新 SCI 稿件放子项目根目录。
- 在改的稿件不放 `0del\`，也不放分析输出文件夹，也不放 `ref\` 或 `结果\`。
- 分析导出（`Results*.html`、PNG）留在分析输出子文件夹。
- 子项目根目录不留临时提取、草稿、一次性中间件。唯一例外是当前在改的稿件。
- `D:\0Grok\0script\stats-analysis\modules\`：新增、修改、移动、改名，都要先得到用户同意。
- 不写 `*.tsv` 索引清单。资料整理（改名、去重、归档）不产出 tsv。登记用 `.xlsx`，说明用 `.md`。

0rad 工作区布局细则：`C:\Users\loopn\.grok\skills\02_data-processing\0rad-workspace.md`。第 5 节未展开 0rad。