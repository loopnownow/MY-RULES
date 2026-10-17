---
name: workspace-layout
description: A类(L:\00used)与B类(D:\0Grok)工作区目录约定。临时文件与产出落点见 My rule.md 第 5 节。
---

# A 类与 B 类工作区

路径别名见 `My rule.md` §1。写入 `0doc\` 须用户说「放 0doc」（权威在 `My rule.md` §5）。产出落点权威在 `My rule.md` §5。

**A 类**（`{WORK_A}\<项目>\` = `L:\00used\<项目>\`）：

- 项目脚本→项目内 `0script\`；项目说明→项目内 `0doc\`。
- `0result\` **只**放最终表（不放 QC HTML、逐受试者中间表、量化元数据、运行日志）；归属不清先问。报告/阶段 QC HTML → 项目 `ref\`（或 Downloads）；细则见 `My rule.md` §5。
- 从 `derivatives\` 取结果默认复制不移动；原件留 `derivatives\`；`0result\` 放副本。
- 能合并的最终表要合并（同键宽表；描述列一份；值列加前缀）；原表移出 `0result\` 前先授权。
- 根目录只留：`rawdata\`、`derivatives\`、`atlases\`、清单/索引、`0script\`、`0doc\`、`0result\`、`ref\`。不用 `{WORK_B}\0script\` 存项目脚本。
- 移动脚本/文档前搜 `import`/`addpath`/`settings.ini`/README；有未更新引用就不移；移后修正路径与 `0doc\` 示例并实测。
- 日志/失效旧文件→`{DEL_A}`（先授权）。临时文件→`My rule.md` §5。

**B 类**（`{WORK_B}\<子项目>\` = `D:\0Grok\<子项目>\`）：

- 可复用脚本→`{WORK_B}\0script\`；长期规则/参考→`{WORK_B}\0doc\`。
- 须保留工程文件→子项目 `ref\`；最新 SCI 稿→子项目根。在改稿不放 `{DEL}`/分析输出/`ref\`/`结果\`。分析导出留分析输出子夹。
- 子项目根不留临时/草稿/一次性中间件（例外：当前在改稿）。`stats-analysis\modules\` 增改移改名须先同意。
- 不写 `*.tsv` 索引；整理用 `.xlsx` 登记、`.md` 说明。

**0rad**：布局细则见 `{SKILLS}\02_data-processing\personal\workspace.md`（原 0rad 独立文件已归档）。
