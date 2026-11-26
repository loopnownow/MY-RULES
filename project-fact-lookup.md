---
name: project-fact-lookup
description: 开工、改稿、内审必查的课题事实：通讯作者、伦理号、扫描序列、实验室参考范围。
---

# 课题事实查找卡

**范围**：通讯作者邮箱、伦理号、扫描序列参数、实验室检查参考范围。
**何时**：开工、改稿（含 Track Changes 增量合并）、内审，均须先打开对应 SSOT，再写或审稿面数字。
一般检索可交 Bai；改稿与内审必须自己打开下表，不得等别人代查。派单须带本课题指针，不得只写「规则已挂」。

## 查哪

| 事实 | SSOT | 空或缺时 |
|---|---|---|
| 通讯作者邮箱 | Vault 条目「通讯作者 corresponding」 | 只取用；禁止写入 mem、本仓、技能、课题文件或聊天 |
| 伦理号 | `{doc_root}\_library\ethics\approvals-index.xlsx`（批件 PDF：`_library\ethics\approvals\<L1>\<L2>\`；家族原件：`{RAW}\<family>\_ethics\`，留存口径 `workspace-layout.md`「伦理材料留存」） | 以索引为准；与稿面不一致先报，禁止臆造或未授权改号 |
| 扫描序列参数 | `{doc_root}\_library\scanner-registry\scanner-parameter-registry.xlsx` | 缺项（如翻转角、TI）标缺；查原始 DICOM 或机房协议；禁止跨课题移植 |
| 实验室检查范围 | `{doc_root}\_library\lab-ref-ranges\lab-reference-ranges.xlsx`（别名 `alias-map.tsv`） | 禁止用表 1 均数或 IQR 倒推正常值；国内与欧美区间分行；禁止编造上下限 |

库总索引（路径与形态，不替代本卡）→ `{doc_root}\_library\INDEX.md`。批件分类契约 → `library-taxonomy.md`。

## 课题侧指针

开工时把本课题对应的批件行、扫描参数登记表行、涉及的检验项，写入 `ref/README.md` 或 `ref/manuscript-revision.md`（禁止新建 `OWNER.md`，口径 `project-ref-layout.md`）。通讯作者邮箱不写入课题树。
改稿与内审按已有指针复核稿面；无指针则先补查再动笔。

## 什么算对 / 何时停

- **算对：** 稿面引用的伦理号、序列参数、实验室范围与上表 SSOT 一致，或已标明「库中未记录」并指出待查来源（DICOM、机房协议、医院 SOP）。
- **停：** SSOT 无值时停止填写该数字，向城城报缺；不从旧稿、他题、摘要或表 1 统计量补数。
