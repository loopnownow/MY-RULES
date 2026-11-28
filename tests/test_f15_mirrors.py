"""F15 mirror-header gate: fail on stale or missing required headers."""
from __future__ import annotations

from pathlib import Path

from check_paths import check_f15_mirrors, sha256_8


def _write(p: Path, text: str) -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")
    return p


def test_f15_ok_when_header_matches(tmp_path: Path) -> None:
    rules = tmp_path / "rules"
    skills = tmp_path / "skills"
    src = _write(rules / "project-ref-layout.md", "# chinese source\n")
    digest = sha256_8(src)
    _write(
        skills / "00_orchestrator/references/project-ref-layout.md",
        f"<!-- rules-mirror-of: project-ref-layout.md src-sha256-8: {digest} -->\n# index\n",
    )
    assert check_f15_mirrors(skills, rules_root=rules) == []


def test_f15_fails_on_hash_mismatch(tmp_path: Path) -> None:
    rules = tmp_path / "rules"
    skills = tmp_path / "skills"
    _write(rules / "project-ref-layout.md", "# chinese source\n")
    _write(
        skills / "00_orchestrator/references/project-ref-layout.md",
        "<!-- rules-mirror-of: project-ref-layout.md src-sha256-8: deadbeef -->\n# index\n",
    )
    bad = check_f15_mirrors(skills, rules_root=rules)
    assert any("header deadbeef" in row for row in bad)


def test_f15_fails_when_required_header_missing(tmp_path: Path) -> None:
    rules = tmp_path / "rules"
    skills = tmp_path / "skills"
    _write(rules / "project-ref-layout.md", "# chinese source\n")
    _write(skills / "00_orchestrator/references/project-ref-layout.md", "# index only\n")
    bad = check_f15_mirrors(skills, rules_root=rules)
    assert any("has no header" in row for row in bad)


def test_f15_fails_when_source_missing(tmp_path: Path) -> None:
    rules = tmp_path / "rules"
    skills = tmp_path / "skills"
    rules.mkdir()
    _write(
        skills / "00_orchestrator/references/project-ref-layout.md",
        "<!-- rules-mirror-of: project-ref-layout.md src-sha256-8: abcd1234 -->\n# index\n",
    )
    bad = check_f15_mirrors(skills, rules_root=rules)
    assert any("missing source" in row for row in bad)
