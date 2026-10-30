"""Lightweight Rules->Skills path check (E3).

Usage:
  python -B check_paths.py --check

When sibling MY-SKILLS (or lab-paths skills_git) is present, verify that seat
folders and concrete file cites in skills.md / My rule.md / README.md exist.
Exits 0 on success, 1 on missing paths. No GitHub Actions; local only.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

RULES_SKILL_PATH_RE = re.compile(
    r"(?:\{SKILLS\}|\{skills_git\}|\{skills_runtime\}|MY-SKILLS)"
    r"[\\/]+"
    r"([A-Za-z0-9_.\\/-]+\.(?:md|yaml|yml|txt|mmd))",
)
SEAT_RE = re.compile(r"`((?:00|02|03|05|06|07)_[a-z0-9-]+)`")


def resolve_skills() -> Path | None:
    # Prefer sibling clone next to MY-RULES (lab layout).
    sib = ROOT.parent / "MY-SKILLS"
    if sib.is_dir():
        return sib
    # Optional: read lab-paths from sibling if somehow remapped.
    lab = sib / "00_orchestrator" / "references" / "lab-paths.yaml"
    if lab.is_file():
        try:
            import yaml

            data = yaml.safe_load(lab.read_text(encoding="utf-8")) or {}
            alias = (data.get("aliases") or {}).get("skills_git")
            if alias and Path(str(alias)).is_dir():
                return Path(str(alias))
        except Exception:
            pass
    return None


def check(skills: Path) -> list[str]:
    missing: list[str] = []
    for name in ("skills.md", "My rule.md", "README.md"):
        path = ROOT / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for m in RULES_SKILL_PATH_RE.finditer(text):
            rel = m.group(1).replace("\\", "/")
            if not (skills / rel).exists():
                missing.append(f"{name}: {rel}")
        if name in ("skills.md", "My rule.md"):
            for m in SEAT_RE.finditer(text):
                seat = m.group(1)
                if not (skills / seat).is_dir():
                    missing.append(f"{name}: seat {seat}")
    return missing


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="verify Rules cites against sibling MY-SKILLS",
    )
    args = ap.parse_args(argv)
    if not args.check:
        ap.print_help()
        return 2
    skills = resolve_skills()
    if skills is None:
        print("MY-SKILLS sibling absent; skip Rules->Skills path check (ok).")
        return 0
    missing = check(skills)
    if missing:
        print("Rules->Skills broken cites:")
        for row in missing:
            print(" ", row)
        return 1
    print(f"Rules->Skills path check OK (skills={skills})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())