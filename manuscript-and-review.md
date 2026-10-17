---
name: manuscript-and-review
description: 稿件与审稿常驻政策。正文禁 agent 免责声明；Track Changes 归属；缺事实只进批注；审稿包交付。
license: MIT
---

# 稿件与审稿（常驻政策）

对所有执行方生效。长流程、版式表、审稿矩阵留在技能（§4 指针）。不编造总则见 `My rule.md` §4。

## 1 正文与批注（只写一次）

稿件正文和回复信正文禁止写入 **agent 新增**的免责声明、占位或内部说明，包括但不限于：`Do not invent…`、`We did not invent…`、`cannot_invent`、`Undecidable pending source`、`will supply from source`、编造的 pathway n/κ/missingness/新 AUC-cutoff/power；图/表占位（如 `[Figure N near here]`）；内部工作说明（pending source / not in the current files 等）；伦理/作者/资助核对与数字不一致的内部备注。

**否定表述**：禁止代理自行新增 “was not tested/measured/examined/included …” 类缺口清单或免责句。用户稿中已有、可核验的 Methods/局限否定事实可以保留。未决与待补仍只进批注。

以上 agent 侧说明一律只进 Word 批注，作者字段 **A**。需要补正文时，批注给建议英文：建议句单独成句，以 `Suggested …` 开头（或同等措辞）；问题说明可用中文。缺口改为「建议做什么」写进批注，不进正文。

若本轮同时写回复信：对应条必须标明未决与待补来源，禁止在回复正文假装已解决；建议措辞放批注，不把免责声明写进回复信正文。

## 2 Track Changes 归属

- 稿件 Track Changes 由 **Aitee（05）** 落笔。
- **Lee（06）** 只标问题、写批注；默认不自行改稿。
- 批注与 Track Changes 的作者字段写 **A**。禁止 `Grok`。禁止黄色填充。

## 3 细则

### 3.1 缺事实

伦理 Date/NO、n、AUC、DOI、未写完的方法事实：写 Word 批注，或先问用户。禁止正文黄色占位。禁止编造。

### 3.2 修订落笔

- 只在原稿上开修订（Track Changes）；不另做替代 docx；润色以修订交付。
- 能定的用修订改；不能定的用批注（作者 A）：中文写问题，并附英文建议措辞和/或建议文献。

### 3.3 批注来源标签

文首格式 `[源:skill-id]`。不默认 `[A:personal]`。用了外部包时来自该包的项标包级标签；可以双标；无从判定才用 `[A:personal]`。

### 3.4 元数据与用户手改

- 稿件已有通讯作者/资助/伦理时，不用模板覆盖。
- 与上次不同的段落视为用户手改；不擅自改回；动该段前先问。HTML/PDF/脚本不套此条。

### 3.5 排版、用词与成段

- **版式优先级**：用户当轮点名 → 目标期刊指南 → 默认模板（Times New Roman 12 pt，1.5 倍行距，两端对齐，段前段后 0；含 PDF）。默认范本：`{WORK_B}\0doc\03-review-replies\_templates\02-layout-template.docx`。长表见技能。
- 比较措辞用 Compared，不用 Relative（禁用语境=比较叙述用词；`relCBF` 等指标/缩写名保留）。不用 attenuated / framework（软件库名除外）。按写作风格技能改；清 AI 腔。正文成段；换主题才分段。摘要标签、Methods/Results 小标题、Highlights、图表注保留格式。

### 3.6 审稿意见与回复

审稿意见：短、锚定数据、被动、直指问题与要求。回复逐条对应并注明位置；改后核对页码/数字/样本量/引用。打分时分项+依据。无法修复→批注。

### 3.7 审稿包与引文

审稿意见/回复用 `.docx`。要求写成 `Please …`（不用 `Please fix:`）。收录审稿人全文；已改用过去时。禁止 `We agree that…`；已声称改过禁止 `we will…`。Undecidable 见 §1。`ACCEPT-*.html` 仅当轮点名。交付放用户已放的项目夹（如 `{WORK_B}\submitting\<project>\`）。05/06 必须经 03 做 citation-verify（`{SKILLS}\03_research\personal\citation-verify.md`）；禁止自称已核对。

## 4 指针

- 版式：`{SKILLS}\05_manuscript\personal\Aitor-format.md`
- 审稿陈述与习惯：`{SKILLS}\06_review\personal\review.md`
- 禁词与去 AI 腔：`{SKILLS}\05_manuscript\personal\vocab\L1\ban-phrases.md`
- 引文与语言过程：`{SKILLS}\05_manuscript\personal\process\citation-and-language.md`
- 座位与 Track Changes 契约：`{SKILLS}\00_orchestrator\references\ownership-contract.md`
