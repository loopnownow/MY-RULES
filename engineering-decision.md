---
name: engineering-decision
description: 工程决策、瘦身与重大变更门。需求优先、证据排错、有序简化、风险比例、保护不变量、闭环验证。
license: MIT
---

# Engineering decision (工程决策)

Short rules for build, debug, slim-down, and irreversible change. Not a persona pack. Do **not** force a full multi-step ritual on every routine task.

## R1–R6

### R1 Requirement-first（需求优先）

Before optimize or rewrite: verify the **outcome**, the **requirement source**, and **hard constraints**.

Remove or merge only after checking dependencies, safety, data impact, and invariants.

### R2 Evidence-based debugging（证据排错）

Expected vs observed → reproduce / isolate → first divergence → smallest change → verify adjacent behavior.

Do not “fix by rewriting” without a divergence point.

### R3 Ordered simplification — existing systems（有序简化）

For live / inherited systems, prefer this order:

1. Question requirements  
2. Remove unjustified parts  
3. Merge / flatten  
4. Optimize the **measured** bottleneck  
5. Accelerate  
6. Automate what is already proven  

Do not skip to accelerate/automate first.

### R4 Risk-proportional checks（风险比例）

- Reversible routine work → light checks.  
- Irreversible or high downstream risk → escalate: list assumptions, impact, and get user confirm when needed.

### R5 Protected invariants（保护不变量）

Must **not** silently change:

- user-approved architecture  
- research definitions  
- primary outcomes  
- data provenance  
- ethics / regulatory constraints  
- public interfaces  

If a change would touch these: **flag and ask**.

### R6 Close the loop（闭环验证）

A QC finding is **not** closed by proposing a fix.

Verify the target, its dependencies, and regression risk. Report:

- checked  
- unverified  
- residual risk  

## 00 Major-change gate（重大变更门）

**Trigger** (destructive / structural):

- deleting or merging skill directories  
- renaming coarse or fine IDs  
- changing A/B layout (mount paths, registry shape, top-only vs body packs)

**Before any destructive step**, require:

1. Assumption list  
2. Dependency / impact notes (what breaks, what mounts, what pointers)  
3. Explicit **user approval**

This gate is **not** a full five-step ceremony for every routine edit. Routine file edits inside an approved pack stay under R1–R6 only.

## Sources

Adapted once from publicly discussed engineering-simplification and first-principles debugging practice (no branded persona pack installed).
