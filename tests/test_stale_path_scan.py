"""Negative / regression tests for Rules MD stale-path scan (P2-03)."""
from __future__ import annotations

import unittest

from check_paths import STALE_RULES, stale_line_allowed


class StalePathAllowIfTests(unittest.TestCase):
    def test_unrelated_not_does_not_allow_0grok_0del(self) -> None:
        pat, _, kind = STALE_RULES[0]
        line = (
            "This is not a drill; live temp SSOT remains D:\\0Grok\\0del until migrated."
        )
        self.assertFalse(stale_line_allowed(line, pat, kind))

    def test_explicit_non_before_path_still_allowed(self) -> None:
        pat, _, kind = STALE_RULES[0]
        line = "路径 SSOT 为 `D:\\0del`（非 `D:\\0Grok\\0del`）。"
        self.assertTrue(stale_line_allowed(line, pat, kind))

    def test_historic_marker_allows_line(self) -> None:
        pat, _, kind = STALE_RULES[0]
        line = "HISTORIC: former path D:\\0Grok\\0del was used in 2024."
        self.assertTrue(stale_line_allowed(line, pat, kind))

    def test_ssot_asserting_stale_path_not_allowed(self) -> None:
        pat, _, kind = STALE_RULES[0]
        line = "路径 SSOT 为 `D:\\0Grok\\0del`。"
        self.assertFalse(stale_line_allowed(line, pat, kind))

    def test_mixed_not_and_positive_stale_path_fails_allow(self) -> None:
        """Unrelated 'not' on the line must not suppress a live stale-path claim."""
        pat, _, kind = STALE_RULES[0]
        line = (
            "Policy note: this is not optional — use D:\\0Grok\\0del for new scratch."
        )
        self.assertTrue(pat.search(line))
        self.assertFalse(stale_line_allowed(line, pat, kind))


class OldRootScanTests(unittest.TestCase):
    """Root-rename scan: live old-root claims fail, rename/historic notes pass."""

    @staticmethod
    def _rule(kind: str):
        for pat, label, rule_kind in STALE_RULES:
            if rule_kind == kind:
                return pat, label, rule_kind
        raise AssertionError(f"missing rule kind: {kind}")

    def test_old_grok_root_live_claim_fails(self) -> None:
        pat, _, kind = self._rule("old_root_0grok")
        line = "输出落 D:\\0Grok\\tmp\\out.txt"
        self.assertTrue(pat.search(line))
        self.assertFalse(stale_line_allowed(line, pat, kind))

    def test_old_grok_root_rename_note_allowed(self) -> None:
        pat, _, kind = self._rule("old_root_0grok")
        line = "工程根 `D:\\MyProjects`（原 `D:\\0Grok`）。"
        self.assertTrue(pat.search(line))
        self.assertTrue(stale_line_allowed(line, pat, kind))

    def test_old_del_root_live_claim_fails(self) -> None:
        pat, _, kind = self._rule("old_root_0del")
        line = "清空后写 D:\\0del\\_by-function\\x.txt"
        self.assertTrue(pat.search(line))
        self.assertFalse(stale_line_allowed(line, pat, kind))

    def test_old_del_root_historic_allowed(self) -> None:
        pat, _, kind = self._rule("old_root_0del")
        line = "移出区 `D:\\MyProjects\\.Del`（旧名 **0del** / `D:\\0del`）。"
        self.assertTrue(pat.search(line))
        self.assertTrue(stale_line_allowed(line, pat, kind))

    def test_old_00db_component_live_claim_fails(self) -> None:
        pat, _, kind = self._rule("old_root_00db")
        line = "落 D:\\MyProjects\\00db\\SSD_1\\"
        self.assertTrue(pat.search(line))
        self.assertFalse(stale_line_allowed(line, pat, kind))

    def test_old_00ds_component_retired_note_allowed(self) -> None:
        pat, _, kind = self._rule("old_root_00ds")
        line = "`D:\\00ds` / 夹名 `00ds` 已退役"
        self.assertTrue(pat.search(line))
        self.assertTrue(stale_line_allowed(line, pat, kind))

    def test_old_0doc_abs_live_claim_fails(self) -> None:
        pat, _, kind = self._rule("old_root_0doc")
        line = "文档落 D:\\MyProjects\\0doc\\x.md"
        self.assertTrue(pat.search(line))
        self.assertFalse(stale_line_allowed(line, pat, kind))

    def test_bare_legacy_alias_word_not_flagged(self) -> None:
        pat, _, kind = self._rule("old_root_00db")
        self.assertFalse(pat.search("旧名 00db = `_DataBase`"))


if __name__ == "__main__":
    unittest.main()
