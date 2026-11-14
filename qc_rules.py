"""Rules gates R1-R3, R5-R7, R9-R10 (R4 lives in check_paths.py; R8 is a PR checklist).

Usage:
  python -B qc_rules.py            # report only, exit 1 if any gate fails
  python -B qc_rules.py --json     # machine-readable

Gates (see QC.md §2):
  R1 routing closure   every live md is routed from My rule.md §5 and exists
  R2 no change history t-ids / decision dates / "此前|曾用|更名|formerly|原 §x"
  R3 old names only    old-name tokens live in aliases.yaml
  R5 no copies         >=40-char sentences must not repeat across live files
  R6 frontmatter       name + description on every content file
  R7 line length       no live line over 400 characters
  R9 section refs      every §N resolves to a numbered heading in the target file
  R10 no pointer shells a stub, or an empty rule, is not a rule — delete it

The alias registry and this file itself are exempt.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent

CONTENT = [
    "My rule.md",
    "workspace-layout.md",
    "project-ref-layout.md",
    "del-and-harvest.md",
    "library-taxonomy.md",
    "network-security.md",
    "skills.md",
]
ROUTED = CONTENT + ["README.md", "QC.md"]
ARCHIVE = {"aliases.yaml", "QC.md"}

T_ID_RE = re.compile(r"(?<![A-Za-z0-9])t\d{3,4}[a-z]?(?![A-Za-z0-9])")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
HISTORY_WORDS = re.compile(r"此前|曾用|更名|formerly|原\s*My rule|原\s*§|旧\s*§", re.I)
# Data thresholds are rules, not change history.
THRESHOLD_CUES = ("≥", ">=", "早于", ">")
LINE_MAX = 400
SENTENCE_MIN = 40

# Old names that may legitimately appear as "do not recreate" bans.
BAN_CUES = ("勿再新建", "已退役", "退役", "禁止", "勿用", "不要",
            "不建", "不重建", "不 bulk", "已退休", "原 `")


def load(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def lines(name: str):
    for i, line in enumerate(load(name).splitlines(), 1):
        yield i, line


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    out = {}
    for raw in text[4:end].splitlines():
        if ":" in raw:
            k, v = raw.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def fail(gate: str, msg: str) -> dict:
    return {"gate": gate, "msg": msg}


def check_r1() -> list[dict]:
    hits = []
    router = load("My rule.md")
    routed = set(re.findall(r"`([A-Za-z0-9_.-]+\.md)`", router))
    fm = frontmatter(router)
    if fm.get("routes"):
        routed |= {x.strip(" []") for x in fm["routes"].split(",") if x.strip()}
    routed.add("My rule.md")
    local = {p.name for p in ROOT.glob("*.md") if p.name not in ARCHIVE}
    for name in sorted(local):
        if name not in routed:
            hits.append(fail("R1", f"{name}: live file not reachable from My rule.md routing"))
    for name in sorted(routed & local):
        if not (ROOT / name).exists():
            hits.append(fail("R1", f"{name}: routed but missing on disk"))
    return hits


def check_r2() -> list[dict]:
    hits = []
    for name in CONTENT + ["README.md"]:
        for i, line in lines(name):
            for m in T_ID_RE.finditer(line):
                hits.append(fail("R2", f"{name}:{i}: change id {m.group(0)!r}"))
            for m in DATE_RE.finditer(line):
                before = line[max(0, m.start() - 8): m.start()]
                if any(cue in before for cue in THRESHOLD_CUES):
                    continue
                hits.append(fail("R2", f"{name}:{i}: decision date {m.group(0)!r}"))
            if HISTORY_WORDS.search(line):
                hits.append(fail("R2", f"{name}:{i}: history wording {HISTORY_WORDS.search(line).group(0)!r}"))
    return hits


def check_r3() -> list[dict]:
    """Only author-curated `tokens:` are enforced; bare path/kind entries are not."""
    hits = []
    blocks = re.split(r"^\s*-\s+old:", load("aliases.yaml"), flags=re.M)[1:]
    tokens = []
    for b in blocks:
        m = re.search(r"tokens:\s*\[([^\]]*)\]", b)
        if m:
            tokens += [t.strip().strip("'\"") for t in m.group(1).split(",") if t.strip()]
    pats = [(t, re.compile(r"(?<![A-Za-z0-9_])" + re.escape(t) + r"(?![A-Za-z0-9_])")) for t in tokens]
    for name in CONTENT + ["README.md"]:
        for i, line in lines(name):
            if any(cue in line for cue in BAN_CUES):
                continue
            for tok, pat in pats:
                if pat.search(line):
                    hits.append(fail("R3", f"{name}:{i}: old name {tok!r} outside archive"))
    return hits


def sentences(text: str):
    for raw in re.split(r"(?<=[。；;])|\n", text):
        s = raw.strip()
        if len(s) < SENTENCE_MIN:
            continue
        if s.startswith(("|", "#", "```", "- **", "  -", "1.", "2.", "3.", "4.", "5.")):
            continue
        if "→" in s and any(k in s for k in ("见", "同文件", "细则", "权威", "指针", "落点")):
            continue  # delegation pointers repeat by design (I1)
        norm = re.sub(r"[\s`*_\[\]()（）<>|#>-]", "", s).lower()
        if len(norm) >= SENTENCE_MIN:
            yield s, norm


def check_r5() -> list[dict]:
    hits = []
    seen: list[tuple[str, str, str]] = []
    for name in CONTENT + ["README.md"]:
        for orig, norm in sentences(load(name)):
            for other_name, other_orig, other_norm in seen:
                if other_name == name:
                    continue
                if norm == other_norm:
                    hits.append(fail("R5", f"{name} == {other_name}: {orig[:60]}..."))
                elif abs(len(norm) - len(other_norm)) <= 12 and SequenceMatcher(None, norm, other_norm).ratio() >= 0.92:
                    hits.append(fail("R5", f"{name} ~ {other_name} (near-copy): {orig[:60]}..."))
            seen.append((name, orig, norm))
    return hits


def check_r6() -> list[dict]:
    hits = []
    for name in CONTENT:
        fm = frontmatter(load(name))
        for key in ("name", "description"):
            if not fm.get(key):
                hits.append(fail("R6", f"{name}: missing frontmatter {key!r}"))
    return hits


def check_r7() -> list[dict]:
    hits = []
    for name in ROUTED:
        in_fence = False
        for i, line in lines(name):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or line.lstrip().startswith("|"):
                continue
            if len(line) > LINE_MAX:
                hits.append(fail("R7", f"{name}:{i}: {len(line)} chars"))
    return hits


HEADING_NUM_RE = re.compile(r"^(#{1,6})\s+(\d+(?:\.\d+)*)(?:[.、\s]|$)")
REF_RE = re.compile(
    r"(?:(?<![A-Za-z0-9_.-])`?((?:My rule|[A-Za-z0-9][A-Za-z0-9_.-]*)\.md)`?\s*)?§\s*(\d+(?:\.\d+)*)"
)


def section_numbers(name: str) -> set[str]:
    nums = set()
    for _, line in lines(name):
        m = HEADING_NUM_RE.match(line)
        if m:
            nums.add(m.group(2))
    return nums


RANGE_RE = re.compile(r"\s*[–—~-]\s*§?\s*(\d+(?:\.\d+)*)")


def check_r9() -> list[dict]:
    """A §N reference must resolve to a numbered heading in the file it targets.

    A bare §N inherits the file named earlier on the same line, else the current
    file; §A–B ranges validate both ends.
    """
    hits = []
    cache: dict[str, set[str]] = {}

    def ok(target: str, ref: str) -> bool:
        if target not in cache:
            cache[target] = section_numbers(target)
        nums = cache[target]
        return ref in nums or any(n.startswith(ref + ".") for n in nums)

    for name in ROUTED:
        for i, line in lines(name):
            last = name
            for m in REF_RE.finditer(line):
                if m.group(1):
                    last = m.group(1)
                target = last
                if target in ARCHIVE or not (ROOT / target).exists():
                    continue
                ref = m.group(2)
                if not ok(target, ref):
                    hits.append(fail("R9", f"{name}:{i}: §{ref} not found in {target}"))
                tail = RANGE_RE.match(line, m.end())
                if tail and not ok(target, tail.group(1)):
                    hits.append(fail("R9", f"{name}:{i}: §{tail.group(1)} not found in {target}"))
    return hits


POINTER_CUE = re.compile(
    r"指针壳|pointer stub|pointer shell|moved to|已移至|已迁移|Body moved|thin pointer", re.I
)


def check_r10() -> list[dict]:
    """R10: a pointer-only shell is transient, not a rule.

    A live md whose body (frontmatter and headings stripped) is at most 5
    non-empty lines and only names a move/pointer is a stub: delete it, or keep
    it only behind a live consumer. An empty file is reported too — an empty
    rule is worse than a stub.
    """
    hits = []
    for name in ROUTED:
        text = load(name)
        body = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
        body_lines = [ln for ln in body.splitlines()
                      if ln.strip() and not ln.lstrip().startswith("#")]
        if not body_lines:
            hits.append(fail("R10", f"{name}: empty rule body"))
        elif len(body_lines) <= 5 and POINTER_CUE.search(body):
            hits.append(fail("R10", f"{name}: pointer-only shell ({len(body_lines)} lines) — delete it"))
    return hits


GATES = {
    "R1": check_r1,
    "R2": check_r2,
    "R3": check_r3,
    "R5": check_r5,
    "R6": check_r6,
    "R7": check_r7,
    "R9": check_r9,
    "R10": check_r10,
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--only", nargs="*", choices=sorted(GATES))
    args = ap.parse_args()

    hits: list[dict] = []
    for gate, fn in GATES.items():
        if args.only and gate not in args.only:
            continue
        hits.extend(fn())

    if args.json:
        print(json.dumps(hits, ensure_ascii=False, indent=2))
    else:
        if not hits:
            print(f"rules QC OK ({', '.join(GATES)})")
        for h in hits:
            print(f"[{h['gate']}] {h['msg']}")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
