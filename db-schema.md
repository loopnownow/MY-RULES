---
name: db-schema
description: L1 子页：DICOM 映射与伪匿名标识（P2、P3）；家族库 / 子库表结构待并入。
up: My rule.md §5
owns: [P2, P3]
---

# 库表结构与 DICOM 映射
- 管：DICOM 来源的 PHI 映射（§P2）、伪匿名标识与一头多姓名（§P3）、像素内烧入文字、头与院内名单冲突的记法。
- 不管：PII 总闸（→ `My rule.md` §P1）；D 码与门禁码表（→ `workspace-layout.md`）；家族桶与 `_PHI` 落点（→ `workspace-layout.md`）。

# 1 DICOM 与伪匿名
**§P2** **DICOM 来源的 PHI**：以 DICOM 头为源，只进家族库——`PatientName`→`id.name`、`PatientID` / `OtherPatientIDs` / `AccessionNumber`→`id_number`、`PatientBirthDate`→`id.birth_date`、`PatientSex`→`id.sex`、`PatientAddress`→`id.address`、`PatientTelephoneNumbers`→`id.phone`。
- `InstitutionName` / `ReferringPhysicianName` / `OperatorsName` 不进子库；子库只留模态、扫描参数与 UID。
- **§P3** 伪匿名标识（`ANON*` / `XXX` / `TEST` / 纯数字 / 单字符重复）不得当真名、不得据此合并身份；一头多姓名或一姓名多头各建身份并记 qc，不合并。
- 像素内烧入的文字属无法自动剥离的 PHI，外发前须人工复核。
- DICOM 头与院内名单冲突时以头为准并记 `qc(DICOM_NAME_CONFLICT)`。判级见 `workspace-layout.md` 门禁码表 D56–D58。
