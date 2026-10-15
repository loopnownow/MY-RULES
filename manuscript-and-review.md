---
name: manuscript-and-review
description: 稿件与审稿常驻政策。正文禁 agent 免责声明；Track Changes 归属；缺事实只进批注；审稿包交付偏好；稿件细则。长流程留在技能。
license: MIT
---

# 稿件与审稿（常驻政策）

对所有执行方生效。原 `My rule.md` 第 6 节中的「稿件」「审稿与回复」已并入本文件。长流程、版式表、审稿矩阵留在技能，本文件只给指针。

## 1 正文与批注

稿件正文和回复信正文不得写入 agent 免责声明或占位，包括：

- `Do not invent…`
- `We did not invent…`
- `cannot_invent`
- `Undecidable pending source`
- `will supply from source`
- 编造的 pathway n、κ、missingness 表、新的 AUC-cutoff、power 数字

这些说明只进 Word 批注，作者 **A**。需要补正文时，批注里给出建议英文。

- 批注里给英文建议句时，建议句单独成句，以 `Suggested …` 开头（或同等 Suggested 措辞）；问题说明可用中文。`Suggested …` 与 `cannot_invent` / Undecidable 说明只进批注，不进正文。
- Undecidable / `cannot_invent`：Word 批注必有（含 `Suggested …` 建议句时写在批注里）。
- 若本轮同时写回复信：回复对应条须标明未决与待补来源，不得在回复正文假装已解决；建议措辞本身放在批注，不把免责声明写进回复信正文。

- 图/表占位与编辑备注只进 Word 批注，禁止正文写 [Figure N near here] 之类。
- 内部工作说明（pending source / not in the current files / In the present file 等）只进批注，禁止进正文或回复信正文。
- 禁止否定列举进正文（was not tested/measured/examined/included 等）；缺口改为「建议做什么」写进批注。
- 伦理、作者、资助核对、数字不一致：只进批注，不进正文（与第 3.1 节一并遵守）。

## 2 Track Changes 归属

- 稿件 Track Changes 由 **Aitee（05）** 落笔。
- **Lee（06）** 只标问题、写批注。默认不自行改稿。
- 批注与 Track Changes 的作者字段写 **A**。禁止 `Grok`。禁止黄色填充（yellow fills）。

## 3 稿件与审稿细则

### 3.1 缺事实

伦理 Date/NO、n、AUC、DOI、未写完的方法事实：写 Word 批注，或先问用户。禁止正文黄色占位。禁止编造。

### 3.2 修订落笔

- 只在原稿上开修订（Track Changes）。不另做替代 docx。润色以修订交付。
- 能定的用修订改。不能定的用 Word 批注（作者 A）。批注用中文写问题，并附英文建议措辞和/或建议文献。

### 3.3 批注来源标签

- 批注来源标签写在文首。格式：`[源:skill-id]`。不默认 `[A:personal]`。本轮用了外部包时，来自该包的项标包级标签。可以双标。无从判定来源时才用 `[A:personal]`。

### 3.4 元数据与用户手改

- 稿件已有通讯作者、资助、伦理时，不用模板内容覆盖。
- 稿件中与上次不同的段落视为用户手改。不擅自改回。动该段前先问。HTML、PDF、脚本不套此条。

### 3.5 排版、用词与成段

- 排版：Times New Roman 12 pt，1.5 倍行距，两端对齐，段前段后 0。范本：`D:\0Grok\0doc\03-review-replies\_templates\02-layout-template.docx`。长表见技能指针。
- 用 Compared，不用 Relative。指标名（如 relCBF）保留。
- 不用 attenuated。不用 framework。软件库名除外。
- 按用户的写作风格技能改。每次都清除 AI 腔词和 AI 句式。
- 正文成段写。不写成一句一行。换主题才分段。
- 以下保留各自格式：摘要四段标签、Methods 和 Results 小标题、Highlights、图表注。

### 3.6 审稿意见与回复

- 审稿意见：简短，锚定数据，被动语态，直指问题并写明要求。
- 回复信逐条对应。每处改动注明稿件中的位置。改稿后核对回复信与稿件：页码、数字、样本量、引用必须一致。
- 用户要求打分时，分项给分，每项附依据。
- 无法修复的问题，以批注提出。
- 正文禁未完成句与否定列举、图/表占位、内部工作说明：见第 1 节（不在此重复）。

### 3.7 审稿包交付与引文核对

- 审稿意见和回复信用 `.docx`。
- 对审稿人的要求写成 `Please …`。不用 `Please fix:`。
- 回复收录审稿人评论全文。已完成的修改用过去时（past tense）。禁止 `We agree that…`。已声称改过的地方禁止 `we will…`。
- Undecidable / `cannot_invent`：建议句写在批注（`Suggested …`）。回复对应条标明未决与待补来源，不得假装已解决，不把免责声明写进回复正文。见第 1 节。
- `ACCEPT-*.html` 只在用户当轮明确要求时才做。未要求则先问。
- 用户已把文件放到项目文件夹时，交付物放该处，例如 `D:\0Grok\submitting\<project>\`。
- 05 与 06 必须调用或要求 03 做 citation-verify。不得自行宣称文献已核对。流程见 `C:\Users\loopn\.grok\skills\03_research\personal\citation-verify.md`。

## 4 指针

- 版式（Times New Roman、行距、Normal style、拆名）：`C:\Users\loopn\.grok\skills\05_manuscript\personal\Aitor-format.md`。
- 审稿陈述与数据一致性表：`C:\Users\loopn\.grok\skills\06_review\personal\review-comment-habits.md`。
- 禁词表与去 AI 腔：`C:\Users\loopn\.grok\skills\05_manuscript\personal\forbidden-phrases.md`。
- 座位与 Track Changes 操作契约：`C:\Users\loopn\.grok\skills\00_orchestrator\references\ownership-contract.md`。