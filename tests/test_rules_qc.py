"""Negative tests for qc_rules.py gates (R1-R3, R5-R7, R9-R10, R13-R17; R11 lives in _Docs structure_check S30). Run: python -B -m pytest -q tests"""
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

CONTENT = list(qc.CONTENT)
ROUTED_EXTRA = ["README.md", "QC.md"]
OLD = "00db"


def _router_table() -> str:
    files = CONTENT + ROUTED_EXTRA
    return "\n".join(f"| 例 | `{n}` | 挂 |" for n in files)


def _routes_header() -> str:
    files = CONTENT + ROUTED_EXTRA
    return "routes: [" + ", ".join(files) + "]\n"


def write_my_rule(tmp: Path, extra_body: str = "") -> None:
    router = _router_table()
    (tmp / "My rule.md").write_text(
        "---\nname: my-rule\ndescription: top\n"
        + _routes_header()
        + "---\n# 0\n"
        + extra_body
        + "# 4 别名与术语\n"
        "术语：`A` 助手，`Adm` 城城标记，席位 `00`。\n"
        "# 5 路由\n"
        "| 触发 | 读 | 挂 |\n|---|---|---|\n"
        + router
        + "\n",
        encoding="utf-8",
    )


def write_db_gates(tmp: Path, body: str | None = None) -> None:
    if body is None:
        body = (
            "本表覆盖 D1–D2。D2 不存在。\n"
            "| 码 | 说明 |\n|---|---|\n"
            "| D1 | 示例码 |\n"
        )
    (tmp / "db-gates.md").write_text(
        "---\nname: db-gates\ndescription: d\ngenerated: false\n---\n# 0\n" + body,
        encoding="utf-8",
    )


def build(tmp: Path) -> None:
    write_my_rule(tmp)
    for n in CONTENT[1:]:
        (tmp / n).write_text(
            f"---\nname: {n[:-3]}\ndescription: d\n---\n# 0\n正文。\n",
            encoding="utf-8",
        )
    write_db_gates(tmp)
    (tmp / "README.md").write_text("# readme\n\n说明。\n", encoding="utf-8")
    (tmp / "QC.md").write_text("---\nname: rules-qc\ndescription: d\n---\n# 0\n判据。\n", encoding="utf-8")
    (tmp / "aliases.yaml").write_text(
        f'- old: "{OLD}"\n  tokens: ["{OLD}"]\n  new: "_DataBase"\n',
        encoding="utf-8",
    )


def run(tmp: Path):
    qc.ROOT = tmp
    hits = []
    for fn in (
        qc.check_r1, qc.check_r2, qc.check_r3, qc.check_r5, qc.check_r6,
        qc.check_r7, qc.check_r9, qc.check_r10, qc.check_r13, qc.check_r14,
        qc.check_r15, qc.check_r16, qc.check_r17,
    ):
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


def test_r2_expanded_retired_word():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\n---\n此条已退休，改走别文件。\n", encoding="utf-8"
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


def test_r5_similar_sentence_at_080():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        a = "本条款要求代理人在完成交付后立即把摘要写回会话并通知调度跟进。"
        b = "本条款要求代理人在完成交付后立即把摘要写回会话并告知调度跟进。"
        (tmp / "skills.md").write_text(f"---\nname: skills\ndescription: d\n---\n{a}\n", encoding="utf-8")
        (tmp / "workspace-layout.md").write_text(f"---\nname: w\ndescription: d\n---\n{b}\n", encoding="utf-8")
        assert gates(run(tmp), "R5")


def test_r5_short_section_pointer_exempt():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        line = "执行细则 → `skills.md` §0。"
        body = f"---\nname: x\ndescription: d\n---\n# 0\n{line}\n另有一句足够长的非指针正文以免空壳。再补一行。\n"
        (tmp / "skills.md").write_text(body.replace("name: x", "name: skills"), encoding="utf-8")
        (tmp / "execution.md").write_text(body.replace("name: x", "name: execution"), encoding="utf-8")
        assert not gates(run(tmp), "R5")


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


def test_r10_pointer_shell():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\n---\n# 0\n已移至 {DEL}。\n", encoding="utf-8")
        assert gates(run(tmp), "R10")


def test_r10_empty_body():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "library-taxonomy.md").write_text(
            "---\nname: library-taxonomy\ndescription: d\n---\n# 0\n", encoding="utf-8")
        assert gates(run(tmp), "R10")


def test_r10_real_body_passes():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\n---\n# 0\n判据一\n判据二\n判据三\n判据四\n判据五\n判据六\n",
            encoding="utf-8")
        assert not gates(run(tmp), "R10")


def test_r13_oversize_l1_fails():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\n---\n# 0\n" + ("字" * 13000) + "\n",
            encoding="utf-8",
        )
        assert gates(run(tmp), "R13")


def test_r13_generated_exempt():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\ngenerated: true\n---\n# 0\n" + ("字" * 13000) + "\n",
            encoding="utf-8",
        )
        assert not gates(run(tmp), "R13")


def test_r13_grandfathered_l0_does_not_fail():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        write_my_rule(tmp, extra_body=("填充。" * 2500) + "\n")
        assert len((tmp / "My rule.md").read_text(encoding="utf-8")) > qc.L0_TARGET
        assert not gates(run(tmp), "R13")


def test_r14_broken_title_pointer():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\n---\n# 0\n见 `workspace-layout.md`「不存在的标题」。再写一行充实正文。\n",
            encoding="utf-8",
        )
        assert gates(run(tmp), "R14")


def test_r14_title_pointer_and_up_with_space_pass():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\nup: My rule.md §5\n---\n# 0 范围\n"
            "见 `workspace-layout.md`「0」。再写一行充实正文以免空壳。\n",
            encoding="utf-8",
        )
        assert not gates(run(tmp), "R14")


def test_r15_missing_glossary():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        router = _router_table()
        (tmp / "My rule.md").write_text(
            "---\nname: my-rule\ndescription: top\n"
            + _routes_header()
            + "---\n# 0\n# 4 别名\n只有路径别名，没有词表。\n# 5 路由\n"
            "| 触发 | 读 | 挂 |\n|---|---|---|\n" + router + "\n",
            encoding="utf-8",
        )
        assert gates(run(tmp), "R15")


def test_r15_glossary_present_passes():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        assert not gates(run(tmp), "R15")


def test_r16_ref_slash_fails():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\n---\n# 0\n临时件进 ref/tmp/。再写一行充实正文。\n",
            encoding="utf-8",
        )
        assert gates(run(tmp), "R16")


def test_r16_ref_backslash_and_fence_pass():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\n---\n# 0\n"
            "临时件进 `ref\\tmp\\`。\n"
            "```\nref/tmp/inside-fence\n```\n"
            "链接 http://example.com/ref/foo 与 file:///C:/ref/x 均可。\n",
            encoding="utf-8",
        )
        assert not gates(run(tmp), "R16")


def test_r16_drive_outside_allowed_fails():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "skills.md").write_text(
            "---\nname: skills\ndescription: d\n---\n# 0\n落点 D:\\MyProjects\\foo。再写一行充实正文。\n",
            encoding="utf-8",
        )
        assert gates(run(tmp), "R16")


def test_r16_drive_in_overlay_passes():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        (tmp / "local-overlay.md").write_text(
            "---\nname: local-overlay\ndescription: d\n---\n# 0\n"
            "本机 `{AITOR}` = `E:\\Aitor`。再写一行充实正文以免空壳。\n",
            encoding="utf-8",
        )
        assert not gates(run(tmp), "R16")


def test_r17_duplicate_d_code():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        write_db_gates(
            tmp,
            "本表覆盖 D1–D2。D2 不存在。\n| 码 | 说明 |\n|---|---|\n| D1 | 一 |\n| D1 | 重复 |\n",
        )
        assert gates(run(tmp), "R17")


def test_r17_complete_table_passes():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        assert not gates(run(tmp), "R17")


def test_r17_missing_undeclared_code():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); build(tmp)
        write_db_gates(
            tmp,
            "本表覆盖 D1–D3。D3 不存在。\n| 码 | 说明 |\n|---|---|\n| D1 | 一 |\n",
        )
        assert gates(run(tmp), "R17")
