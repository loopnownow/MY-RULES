## 改了什么

<!-- 一句话说行为变化；不写流水账，不复述 diff。 -->

## 门（三条全绿才提 PR）

- [ ] `python -B check_paths.py --check`
- [ ] `python -B qc_rules.py`
- [ ] `python -B -m pytest -q tests`

## 留痕（R8）

- [ ] PR 标题带编号（如 `t20261114h:`），同号条目已写进 `HISTORY.md`（§I 或对应节）
- [ ] 决策号 / 日期 / 旧名没有留在正文，全部进 `HISTORY.md` / `aliases.yaml`
- [ ] 改名或删名：`aliases.yaml` 已补 `old` / `tokens` / `new` / `kind`
- [ ] 新增或删除 L1 文件：`My rule.md` 路由表、`README.md` 地图、`check_paths.py` 必检清单三处同步

## 边界

- [ ] 只改本仓正文，没有复制 `{SKILLS}` / `{code_root}` 的内容
- [ ] 没有把旧记录塞回正文，也没有新增第二个 SSOT
- [ ] 技能侧若依赖本仓节号，已按「节号 + 标题名」引用
