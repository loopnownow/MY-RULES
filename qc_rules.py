"""Rules gates R1-R3, R5-R7, R9-R10, R13-R17 (R4 lives in check_paths.py; R8 is a PR checklist; R11 lives in _Docs test structure_check.py S30).

Usage:
  python -B qc_rules.py            # report only, exit 1 if any gate fails
  python -B qc_rules.py --json     # machine-readable

Gates (see QC.md §2):
  R1 routing closure   every live md is routed from My rule.md §5 and exists
  R2 no change history t-ids / decision dates / "此前|曾用|更名|formerly|原 §x|已瘦身|已退休|已卸|已并入|已拆出"
  R3 old names only    old-name tokens live in aliases.yaml
  R5 no copies         >=30-char sentences, similarity >=0.80; short §ID pointers exempt
  R6 frontmatter       name + description on every content file
  R7 line length       no live line over 400 characters
  R9 section refs      every §N resolves to a numbered heading in the target file
  R10 no pointer shells a stub, or an empty rule, is not a rule — delete it
  R13 size report      L0/L1/overview targets; currently-over files report only (D-8)
  R14 anchors          letter §IDs unique, owns: match, title pointers, up:, routes:
  R15 glossary         L0 §4 terminology table must exist (does not ban 主人; D-3)
  R16 path writing     no ref/ outside code/URL; drive letters only in §4 / overlay / aliases
  R17 D-code table     db-gates.md codes unique and complete vs header exclusions

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
    "library-taxonomy.md",
    "network-security.md",
    "skills.md",
    "project-fact-lookup.md",
    "local-overlay.md",
    "execution.md",
    "manuscript-docx.md",
    "db-schema.md",
    "zone-del.md",
    "zone-database.md",
    "db-gates.md",
    "zone-docs.md",
    "zone-projects.md",
]
ROUTED = CONTENT + ["README.md", "QC.md"]
ARCHIVE = {"aliases.yaml", "QC.md"}

T_ID_RE = re.compile(r"(?<![A-Za-z0-9])t\d{3,4}[a-z]?(?![A-Za-z0-9])")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
HISTORY_WORDS = re.compile(r"此前|曾用|更名|formerly|原\s*My rule|原\s*§|旧\s*§|已瘦身|已退休|已卸|已并入|已拆出", re.I)
# Data thresholds are rules, not change history.
THRESHOLD_CUES = ("≥", ">=", "早于", ">")
LINE_MAX = 400
SENTENCE_MIN = 30
R5_THRESHOLD = 0.80
R5_POINTER_MAX = 60

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


SECTION_ID_RE = re.compile(r"§\s*(?:[A-Z]\d+|\d+(?:\.\d+)*)")


def is_r5_pointer_exempt(s: str) -> bool:
    """Narrow exemption (D-5): <=60 chars, contains → and a §ID."""
    return len(s) <= R5_POINTER_MAX and "→" in s and bool(SECTION_ID_RE.search(s))


def sentences(text: str):
    for raw in re.split(r"(?<=[。；;])|\n", text):
        s = raw.strip()
        if len(s) < SENTENCE_MIN:
            continue
        if s.startswith(("|", "#", "```", "- **", "  -", "1.", "2.", "3.", "4.", "5.")):
            continue
        if is_r5_pointer_exempt(s):
            continue
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
                elif abs(len(norm) - len(other_norm)) <= 12 and SequenceMatcher(None, norm, other_norm).ratio() >= R5_THRESHOLD:
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



# ---------- R13–R17 ----------

L0_FILE = "My rule.md"
OVERVIEW_FILE = "workspace-layout.md"
L0_TARGET = 6000
L1_TARGET = 12000
OVERVIEW_TARGET = 3000
# D-8: files already over target at C8. Measured and printed; do not fail. Pending owner confirmation.
R13_GRANDFATHER = frozenset({"My rule.md", "zone-database.md"})
SUPPORT_FILES = frozenset({"README.md", "QC.md"})

LETTER_ID_RE = re.compile(r"§\s*([A-Z]\d+)")
BOLD_DEF_RE = re.compile(r"\*\*§\s*([A-Z]\d+)\*\*")
OWN_ID_RE = re.compile(r"([A-Z]\d+)")
TITLE_PTR_RE = re.compile(
    r"(?:`([^`]+?\.md)`|本文件|同文件)\s*[「『]([^」』]+)[」』]"
)
DRIVE_RE = re.compile(r"(?<![A-Za-z0-9./])([A-Za-z]):(?:\\|/)")
REF_SLASH_RE = re.compile(r"(?<![A-Za-z0-9_])ref/")
D_CODE_ROW_RE = re.compile(r"^\|\s*(D\d+)\s*\|", re.M)
D_RANGE_RE = re.compile(r"D(\d+)\s*[–—-]\s*D?(\d+)")


def file_size_kind(name: str) -> tuple[str, int | None]:
    if name == L0_FILE:
        return "L0", L0_TARGET
    if name == OVERVIEW_FILE:
        return "总图", OVERVIEW_TARGET
    if name in SUPPORT_FILES or name == "aliases.yaml":
        return "支撑", None
    return "L1", L1_TARGET


def r13_rows() -> list[dict]:
    rows = []
    for name in ROUTED:
        text = load(name)
        fm = frontmatter(text)
        n = len(text)
        kind, target = file_size_kind(name)
        generated = fm.get("generated") == "true"
        over = target is not None and n > target and not generated
        rows.append({
            "file": name, "kind": kind, "chars": n, "target": target,
            "generated": generated, "over": over,
            "grandfathered": name in R13_GRANDFATHER,
        })
    return rows


def format_r13_table(rows: list[dict]) -> str:
    lines = ["R13 size (python len, full file):"]
    for r in rows:
        tgt = "—" if r["target"] is None else str(r["target"])
        if r["generated"]:
            flag = "exempt-generated"
        elif r["target"] is None:
            flag = "n/a"
        elif not r["over"]:
            flag = "OK"
        elif r["grandfathered"]:
            flag = "OVER (grandfathered, report only; D-8)"
        else:
            flag = "OVER"
        lines.append(f"  {r['file']:28} {r['kind']:4} {r['chars']:6} / {tgt:>6}  {flag}")
    return "\n".join(lines)


def check_r13() -> list[dict]:
    """Targets stay 6000/12000/3000. Grandfathered over-target files do not fail."""
    hits = []
    for r in r13_rows():
        if r["over"] and not r["grandfathered"] and not r["generated"]:
            hits.append(fail(
                "R13",
                f"{r['file']}: {r['chars']} chars > {r['kind']} target {r['target']}",
            ))
    return hits


def letter_defs() -> dict[str, list[tuple[str, int, str]]]:
    """id -> list of (file, line, kind) for owns: and **§ID** definitions."""
    found: dict[str, list[tuple[str, int, str]]] = {}
    for name in ROUTED:
        text = load(name)
        fm = frontmatter(text)
        for oid in OWN_ID_RE.findall(fm.get("owns", "")):
            found.setdefault(oid, []).append((name, 0, "owns"))
        for i, line in enumerate(text.splitlines(), 1):
            for m in BOLD_DEF_RE.finditer(line):
                found.setdefault(m.group(1), []).append((name, i, "bold-def"))
    return found


def heading_texts(name: str) -> list[str]:
    if not (ROOT / name).exists():
        return []
    heads = []
    for line in load(name).splitlines():
        m = re.match(r"^#{1,6}\s+(.+)$", line)
        if m:
            heads.append(re.sub(r"[`*]", "", m.group(1)).strip())
    return heads


def title_matches(title: str, heads: list[str]) -> bool:
    tn = re.sub(r"[`*]", "", title).strip()
    for h in heads:
        if tn == h or tn in h or h in tn:
            return True
    return False


def section_numbers_any(name: str) -> set[str]:
    return section_numbers(name)


def check_r14() -> list[dict]:
    hits = []
    defs = letter_defs()

    # unique bold-def file; owns: must match bold-def set in that file
    bold_files: dict[str, set[str]] = {}
    owns_files: dict[str, set[str]] = {}
    for oid, locs in defs.items():
        bold = {f for f, _, k in locs if k == "bold-def"}
        own = {f for f, _, k in locs if k == "owns"}
        bold_files[oid] = bold
        owns_files[oid] = own
        if len(bold) > 1:
            hits.append(fail("R14", f"§{oid}: defined in multiple files {sorted(bold)}"))
        if len(bold) == 1 and own and bold != own:
            hits.append(fail("R14", f"§{oid}: owns: {sorted(own)} != definition file {sorted(bold)}"))
        if len(bold) == 1 and not own:
            hits.append(fail("R14", f"§{oid}: defined in {sorted(bold)[0]} but missing from owns:"))
        if own and not bold:
            hits.append(fail("R14", f"§{oid}: listed in owns: {sorted(own)} but no **§{oid}** definition"))

    defined = {oid for oid, locs in defs.items() if any(k == "bold-def" for _, _, k in locs)}
    for name in ROUTED:
        for i, line in enumerate(load(name).splitlines(), 1):
            # skip the definition itself
            for m in re.finditer(r"§\s*([A-Z]\d+)(?:\s*[–—-]\s*([A-Z]\d+))?", line):
                ids = [m.group(1)]
                if m.group(2):
                    ids.append(m.group(2))
                for oid in ids:
                    if oid not in defined:
                        hits.append(fail("R14", f"{name}:{i}: §{oid} has no unique definition"))

    # title pointers
    for name in ROUTED:
        for i, line in enumerate(load(name).splitlines(), 1):
            for m in TITLE_PTR_RE.finditer(line):
                target = m.group(1) or name
                title = m.group(2)
                if not (ROOT / target).exists():
                    hits.append(fail("R14", f"{name}:{i}: title pointer target missing: {target}"))
                    continue
                if not title_matches(title, heading_texts(target)):
                    hits.append(fail("R14", f"{name}:{i}: title {title!r} not a heading in {target}"))

    # up:
    for name in ROUTED:
        up = frontmatter(load(name)).get("up")
        if not up:
            continue
        m = re.match(r"`?(.+?\.md)`?(?:\s+§\s*(\S+))?\s*$", up)
        if not m:
            hits.append(fail("R14", f"{name}: unparsable up: {up!r}"))
            continue
        target, secn = m.group(1).strip(), m.group(2)
        if not (ROOT / target).exists():
            hits.append(fail("R14", f"{name}: up: target missing: {target}"))
            continue
        if secn and re.match(r"^\d", secn):
            nums = section_numbers_any(target)
            if secn not in nums and not any(n.startswith(secn + ".") for n in nums):
                hits.append(fail("R14", f"{name}: up: §{secn} not found in {target}"))

    # routes: vs §5 读 column
    router = load("My rule.md")
    fm = frontmatter(router)
    routes = [x.strip(" []") for x in fm.get("routes", "").split(",") if x.strip()]
    body = router
    m5 = re.search(r"^# 5 .+$", body, re.M)
    m6 = re.search(r"^# 6 .+$", body, re.M)
    if not m5:
        hits.append(fail("R14", "My rule.md: missing # 5 routing table"))
    else:
        sec5 = body[m5.start(): m6.start() if m6 else len(body)]
        read_md = []
        for line in sec5.splitlines():
            if not line.startswith("|") or re.match(r"^\|\s*-+", line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2 or cells[0] in {"触发", "触发条件"} or cells[1] in {"读", "读什么"}:
                continue
            for fn in re.findall(r"`([A-Za-z0-9_. -]+\.md)`", cells[1]):
                if (ROOT / fn).exists():
                    read_md.append(fn)
        if set(routes) != set(read_md):
            hits.append(fail(
                "R14",
                "routes: != §5 读 column: "
                f"only-routes={sorted(set(routes)-set(read_md))} "
                f"only-§5={sorted(set(read_md)-set(routes))}",
            ))
    return hits


def check_r15() -> list[dict]:
    """L0 §4 terminology table must exist. Does not ban 主人 (D-3; differs from plan)."""
    hits = []
    text = load("My rule.md")
    m4 = re.search(r"^# 4 .+$", text, re.M)
    m5 = re.search(r"^# 5 .+$", text, re.M)
    if not m4:
        hits.append(fail("R15", "My rule.md: missing # 4 别名与术语"))
        return hits
    sec4 = text[m4.start(): m5.start() if m5 else len(text)]
    if "术语" not in sec4:
        hits.append(fail("R15", "My rule.md §4: 术语表 missing (need the word 术语)"))
    # existing terms mentioned in the current glossary
    for token in ("`A`", "`Adm`", "`00`"):
        if token not in sec4:
            hits.append(fail("R15", f"My rule.md §4: glossary missing {token}"))
    return hits


def _mask_exempt_path_spans(text: str) -> str:
    def sp(m: re.Match) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))
    out = re.sub(r"```.*?```", sp, text, flags=re.S)
    out = re.sub(r"https?://\S+", sp, out)
    out = re.sub(r"file:///\S+", sp, out)
    return out


def _in_l0_section4(name: str, lineno: int, text: str) -> bool:
    if name != "My rule.md":
        return False
    s4 = s5 = None
    for i, line in enumerate(text.splitlines(), 1):
        if re.match(r"^# 4 ", line):
            s4 = i
        elif re.match(r"^# 5 ", line) and s4 is not None:
            s5 = i
            break
    return s4 is not None and s4 <= lineno < (s5 or 10**9)


def check_r16() -> list[dict]:
    hits = []
    allowed_drive_files = {"local-overlay.md", "aliases.yaml"}
    for name in list(dict.fromkeys(CONTENT + ["README.md", "QC.md"])):
        raw = load(name)
        masked = _mask_exempt_path_spans(raw)
        raw_lines = raw.splitlines()
        mask_lines = masked.splitlines()
        for i, (oline, mline) in enumerate(zip(raw_lines, mask_lines), 1):
            if REF_SLASH_RE.search(mline):
                hits.append(fail("R16", f"{name}:{i}: ref/ outside code/URL (use ref\\)"))
            for m in DRIVE_RE.finditer(mline):
                if name in allowed_drive_files or _in_l0_section4(name, i, raw):
                    continue
                hits.append(fail("R16", f"{name}:{i}: drive letter {m.group(0)!r} outside §4 / local-overlay.md / aliases.yaml"))
    return hits


def _parse_declared_d_exclusions(text: str) -> set[int]:
    """Integers in D1–D92 that the file says are absent or out of the table."""
    excluded = set()
    # allow `D10`–`D18` 不存在 and D76–D86 判级以 gates.py 为准
    rng = r"D(\d+)`?\s*[–—-]\s*`?D?(\d+)`?"
    for m in re.finditer(rng + r"\s*不存在", text):
        a, b = int(m.group(1)), int(m.group(2))
        excluded.update(range(min(a, b), max(a, b) + 1))
    for m in re.finditer(r"(?<![\d–—-])D(\d+)\s*不存在", text):
        excluded.add(int(m.group(1)))
    for m in re.finditer(rng + r"\s*判级以\s*`?gates\.py`?\s*为准", text):
        a, b = int(m.group(1)), int(m.group(2))
        excluded.update(range(min(a, b), max(a, b) + 1))
    return excluded


def check_r17() -> list[dict]:
    """Intra-table D-code uniqueness and completeness vs header (D-6). No bind to gates.py."""
    hits = []
    text = load("db-gates.md")
    rows = D_CODE_ROW_RE.findall(text)
    seen = {}
    nums = []
    for i, code in enumerate(rows, 1):
        n = int(code[1:])
        nums.append(n)
        if code in seen:
            hits.append(fail("R17", f"db-gates.md: duplicate {code}"))
        seen[code] = i
    header = re.search(r"D(\d+)\s*[–—-]\s*D?(\d+)", text)
    if not header:
        hits.append(fail("R17", "db-gates.md: header missing D-range declaration"))
        return hits
    lo, hi = int(header.group(1)), int(header.group(2))
    excluded = _parse_declared_d_exclusions(text)
    for n in nums:
        if n < lo or n > hi:
            hits.append(fail("R17", f"db-gates.md: {f'D{n}'} outside declared D{lo}–D{hi}"))
        if n in excluded:
            hits.append(fail("R17", f"db-gates.md: {f'D{n}'} is declared excluded but appears in the table"))
    missing = [n for n in range(lo, hi + 1) if n not in nums and n not in excluded]
    if missing:
        sample = ", ".join(f"D{n}" for n in missing[:12])
        more = f" (+{len(missing)-12})" if len(missing) > 12 else ""
        hits.append(fail("R17", f"db-gates.md: missing codes vs header (not excluded): {sample}{more}"))
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
    "R13": check_r13,
    "R14": check_r14,
    "R15": check_r15,
    "R16": check_r16,
    "R17": check_r17,
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
        try:
            print(format_r13_table(r13_rows()))
        except OSError as exc:
            print(f"R13 size table unavailable: {exc}")
        if not hits:
            print(f"rules QC OK ({', '.join(GATES)})")
        for h in hits:
            print(f"[{h['gate']}] {h['msg']}")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
