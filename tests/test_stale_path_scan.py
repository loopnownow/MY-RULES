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


if __name__ == "__main__":
    unittest.main()
