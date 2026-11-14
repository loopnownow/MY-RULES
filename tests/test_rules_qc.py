"""Negative tests for qc_rules.py gates (R1-R3, R5-R7, R9). Run: python -B -m pytest -q tests"""
from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("qc_rules", HERE / "qc_rules.py")
qc = importlib.util.module_from_spec(spec)
sys.modules["qc_rules"] = qc
spec.loader.exec_module(qc)

CONTENT = ["My rule.md", "workspace-layout.md", "project-ref-layout.md",
           "del-and-harvest.md", "library-taxonomy.md", "network-security.md", "skills.md"]
ROUTED_EXTRA = ["README.md", "QC.md"]
OLD = "00db"


def build(tmp: Path) -> None:
    router = "\n".join(f"| 触发 | `{n}` | 挂 |" for n in CONTENT + ROUTED_EXTRA)
    (tmp / "My rule.md").write_text(
        "---\nname: my-rule\ndescription: top\n---\n# 0\n" + router + "\n", encoding="utf-8")
    for n in CONTENT[1:]:
        (tmp / n).write_text(f"---\nname: {n[:-3]}\ndescription: d\n---\n# 0\n", encoding="utf-8")
    (tmp / "README.md").write_text("# readme\n", encoding="utf-8")
    (tmp / "QC.md").write_text("---\nname: rules-qc\ndescription: d\n---\n", encoding="utf-8")
    (tmp / "HISTORY.md").write_text("t1800u 与 2026-10-31 的历史\n", encoding="utf-8")
    (tmp / f"aliases.yaml").write_text(f'- old: "{OLD}"\n  tokens: ["{OLD}"]\n  new: "_DataBase"\n', encoding="utf-8")


def run(tmp: Path):
    qc.ROOT = tmp
    hits = []
    for fn in (qc.check_r1, qc.check_r2, qc.check_r3, qc.check_r5, qc.check_r6, qc.check_r7, qc.check_r9):
        hits.extend(fn())
    return hits


def gates(hits, gate):
    return [h for h in hits if h["gate"] == gate]


def test_clean_passes():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        assert run(tmp) == []


def test_r2_change_id():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text("---\nname: skills\ndescription: d\n---\n旧 t1800u 规则\n", encoding="utf-8")
        assert gates(run(tmp), "R2")


def test_r2_decision_date_but_allows_threshold():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        p = tmp / "skills.md"
        p.write_text("---\nname: skills\ndescription: d\n---\n2026-10-31 起不再留 xlsx\n", encoding="utf-8")
        assert gates(run(tmp), "R2")
        p.write_text("---\nname: skills\ndescription: d\n---\n批件日期 ≥ 2023-11-10\n", encoding="utf-8")
        assert not gates(run(tmp), "R2")


def test_r2_history_word():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text("---\nname: skills\ndescription: d\n---\n此前放在 0doc\n", encoding="utf-8")
        assert gates(run(tmp), "R2")


def test_r2_old_section_ref():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\n---\n（原 My rule §5.2 迁入）\n", encoding="utf-8"
        )
        assert gates(run(tmp), "R2")


def test_r3_old_name_outside_archive():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(f"---\nname: skills\ndescription: d\n---\n写入 {OLD} 根\n", encoding="utf-8")
        assert gates(run(tmp), "R3")
        (tmp / "skills.md").write_text(f"---\nname: skills\ndescription: d\n---\n{OLD} 已退役，勿再新建\n", encoding="utf-8")
        assert not gates(run(tmp), "R3")


def test_r1_unrouted_file():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "extra.md").write_text("# extra\n", encoding="utf-8")
        assert gates(run(tmp), "R1")


def test_r5_duplicate_sentence():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        line = "这是同一条规则句子，用来验证跨文件重复检测能力是否正常工作，包括中文与标点归一化处理。"
        (tmp / "skills.md").write_text(f"---\nname: skills\ndescription: d\n---\n{line}\n", encoding="utf-8")
        (tmp / "workspace-layout.md").write_text(f"---\nname: w\ndescription: d\n---\n{line}\n", encoding="utf-8")
        assert gates(run(tmp), "R5")


def test_r6_missing_frontmatter():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "library-taxonomy.md").write_text("# no frontmatter\n", encoding="utf-8")
        assert gates(run(tmp), "R6")


def test_r7_long_line_and_table_exemption():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text("---\nname: skills\ndescription: d\n---\n" + "字" * 401 + "\n", encoding="utf-8")
        assert gates(run(tmp), "R7")
        (tmp / "skills.md").write_text("---\nname: skills\ndescription: d\n---\n| " + "字" * 500 + "\n", encoding="utf-8")
        assert not gates(run(tmp), "R7")


def test_r9_section_ref_must_resolve():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        p = tmp / "skills.md"
        p.write_text(
            "---\nname: skills\ndescription: d\n---\n# 9 写盘\n见 `My rule.md` §0\n", encoding="utf-8")
        assert not gates(run(tmp), "R9")
        p.write_text(
            "---\nname: skills\ndescription: d\n---\n# 9 写盘\n见 `My rule.md` §7\n", encoding="utf-8")
        assert gates(run(tmp), "R9")
