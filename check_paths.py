"""Lightweight Rules->Skills path check (E3).

Usage:
  python -B check_paths.py --check
  python -B check_paths.py --check --allow-missing-skills   # portable skip only

When MY-SKILLS is present (sibling clone, or SKILLS_ROOT / MY_SKILLS env), verify
that seat folders and concrete file cites in skills.md / My rule.md / README.md
exist, and scan Rules MD for stale path claims that conflict with project-ref /
DEL SSOT. Exits 0 on success, 1 on missing paths or stale claims.

Fail-loud (no false-green): missing required Rules MD, missing skills root
(unless --allow-missing-skills), or skipped checks that would otherwise exit 0
without verifying. No GitHub Actions; local only.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_RULES_MD = ("skills.md", "My rule.md", "README.md")
# Also scan these for stale path claims (N14).
SCAN_MD = REQUIRED_RULES_MD + (
    "workspace-layout.md",
    "project-ref-layout.md",
    "network-security.md",
    "library-taxonomy.md",
)

RULES_SKILL_PATH_RE = re.compile(
    r"(?:\{SKILLS\}|\{skills_git\}|\{skills_runtime\}|MY-SKILLS)"
    r"[\\/]+"
    r"([A-Za-z0-9_.\\/-]+\.(?:md|yaml|yml|txt|mmd))",
)
SEAT_RE = re.compile(r"`((?:00|02|03|05|06|07)_[a-z0-9-]+)`")

# Live claims that conflict with check_paths / project-ref-layout / My rule SSOT.
# Lines matching stale_line_allowed are historical / negation and are ignored.
HISTORIC_LINE_MARKERS = re.compile(
    r"HISTORIC:|SUPERSEDED:|former\s+path:|retired\s+path:",
    re.I,
)
# Explicit negation or historic cue immediately before the stale path token (not whole-line "not").
PATH_NEGATION_BEFORE = re.compile(
    r"(?:HISTORIC|SUPERSEDED|former\s+path|retired\s+path|"
    r"非|不是|勿用|勿|禁止|≠|!\s*=|"
    r"formerly|retired(?:\s+live)?|historical|legacy|archived|"
    r"relocated|moved\s+to|was\s)\s*[`「\"'（(]*\s*$",
    re.I,
)
RETIRED_STATS_PATH_CONTEXT = re.compile(
    r"retired|former|formerly|historical|legacy|archived|pruned|relocated|"
    r"absorbed|勿建|do not recreate|归档|历史|moved to|was\s",
    re.I,
)

STALE_RULES = (
    (
        re.compile(r"D:\\0Grok\\0del", re.I),
        r"D:\0Grok\0del",
        "0grok_0del",
    ),
    (
        re.compile(
            r"_code\\04-analysis\\stats-analysis|_code/04-analysis/stats-analysis",
            re.I,
        ),
        r"_code\04-analysis\stats-analysis (retired; use {code_stats})",
        "retired_stats",
    ),
)


def stale_line_allowed(line: str, pat: re.Pattern[str], rule_kind: str) -> bool:
    """True when a stale-path hit on this line is clearly historic / negated."""
    if HISTORIC_LINE_MARKERS.search(line):
        return True
    m = pat.search(line)
    if not m:
        return True
    tail = line[: m.start()]
    window = tail[-80:] if len(tail) > 80 else tail
    if PATH_NEGATION_BEFORE.search(window):
        return True
    if rule_kind == "retired_stats" and RETIRED_STATS_PATH_CONTEXT.search(line):
        # Retired stats path: allow only when the qualifier precedes the path token.
        ctx = RETIRED_STATS_PATH_CONTEXT.search(line)
        if ctx and ctx.end() <= m.start():
            return True
    return False


def resolve_skills() -> Path | None:
    for key in ("SKILLS_ROOT", "MY_SKILLS"):
        raw = (os.environ.get(key) or "").strip()
        if raw:
            p = Path(raw)
            if p.is_dir():
                return p.resolve()
    sib = ROOT.parent / "MY-SKILLS"
    if sib.is_dir():
        return sib.resolve()
    return None


def check_skill_cites(skills: Path) -> list[str]:
    missing: list[str] = []
    for name in REQUIRED_RULES_MD:
        path = ROOT / name
        if not path.is_file():
            missing.append(f"required Rules file missing: {name}")
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


def check_stale_md_paths() -> list[str]:
    """N14: Rules MD must not claim stale live paths that conflict with SSOT."""
    bad: list[str] = []
    for name in SCAN_MD:
        path = ROOT / name
        if not path.is_file():
            if name in REQUIRED_RULES_MD:
                continue
            bad.append(f"scan target missing: {name}")
            continue
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for pat, label, rule_kind in STALE_RULES:
                if not pat.search(line):
                    continue
                if stale_line_allowed(line, pat, rule_kind):
                    continue
                bad.append(
                    f"{name}:{i}: stale live path {label}: {line.strip()[:100]}"
                )
    return bad


def check(skills: Path) -> list[str]:
    return check_skill_cites(skills) + check_stale_md_paths()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="verify Rules cites against MY-SKILLS + stale MD path scan",
    )
    ap.add_argument(
        "--allow-missing-skills",
        action="store_true",
        help="exit 0 when MY-SKILLS is absent (portable only; default is fail-loud)",
    )
    args = ap.parse_args(argv)
    if not args.check:
        ap.print_help()
        return 2
    skills = resolve_skills()
    if skills is None:
        if args.allow_missing_skills:
            print(
                "MY-SKILLS absent; --allow-missing-skills set; "
                "skip Rules->Skills path check."
            )
            return 0
        print(
            "MY-SKILLS sibling/env absent; refuse (no false-green). "
            "Set SKILLS_ROOT/MY_SKILLS or pass --allow-missing-skills."
        )
        return 1
    missing = check(skills)
    if missing:
        print("Rules->Skills / path-scan failures:")
        for row in missing:
            print(" ", row)
        return 1
    print(f"Rules->Skills path check OK (skills={skills})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
