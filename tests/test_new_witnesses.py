"""Tests for the 2026-07 portfolio additions: erdos_gyarfas and
frankl_union_closed witness verifiers.

Both conjectures are OPEN, so no genuine is_valid=True witness can appear
here (constructing one would be a research result). The tests therefore
pin down: schema rejection, hypothesis-class rejection, correct detection
of power-of-2 cycles / union-closure violations / high-frequency elements
on known graphs and families, and the conservative budget path.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from library.erdos_gyarfas_witness import (
    verify_witness as eg_verify,
    _has_cycle_of_length,
    _powers_of_two_up_to,
)
from library.union_closed_witness import verify_witness as uc_verify

REPO_ROOT = Path(__file__).resolve().parent.parent

EG_SPEC = json.loads((REPO_ROOT / "proofs" / "erdos_gyarfas.json").read_text(encoding="utf-8"))
UC_SPEC = json.loads((REPO_ROOT / "proofs" / "frankl_union_closed.json").read_text(encoding="utf-8"))


def _adj(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    a: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        a[u].append(v)
        a[v].append(u)
    return a


PETERSEN_EDGES = [
    # outer 5-cycle
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
    # spokes
    (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),
    # inner pentagram
    (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
]

K4_EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


class TestPowersOfTwo(unittest.TestCase):
    def test_lengths(self):
        self.assertEqual(_powers_of_two_up_to(3), [])
        self.assertEqual(_powers_of_two_up_to(4), [4])
        self.assertEqual(_powers_of_two_up_to(10), [4, 8])
        self.assertEqual(_powers_of_two_up_to(64), [4, 8, 16, 32, 64])


class TestCycleDetection(unittest.TestCase):
    def test_c5_has_only_5_cycle(self):
        # 5-cycle graph: cycle of length 5, none of length 4.
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
        adj = _adj(5, edges)
        self.assertFalse(_has_cycle_of_length(adj, 5, 4, [10**6]))
        self.assertTrue(_has_cycle_of_length(adj, 5, 5, [10**6]))

    def test_k4_has_3_and_4_cycles(self):
        adj = _adj(4, K4_EDGES)
        self.assertTrue(_has_cycle_of_length(adj, 4, 3, [10**6]))
        self.assertTrue(_has_cycle_of_length(adj, 4, 4, [10**6]))

    def test_petersen_cycle_spectrum(self):
        # Petersen: girth 5; has cycles of lengths 5, 6, 8, 9 but NOT 3, 4, 7, 10.
        adj = _adj(10, PETERSEN_EDGES)
        budget = [10**7]
        present = {L for L in range(3, 11) if _has_cycle_of_length(adj, 10, L, budget)}
        self.assertEqual(present, {5, 6, 8, 9})


class TestGyarfasVerifier(unittest.TestCase):
    def test_k4_rejected_has_4_cycle(self):
        r = eg_verify({"num_vertices": 4, "edges": K4_EDGES}, EG_SPEC)
        self.assertFalse(r.is_valid)
        self.assertIn("cycle of length 4", r.reason)

    def test_petersen_rejected_has_8_cycle(self):
        r = eg_verify({"num_vertices": 10, "edges": PETERSEN_EDGES}, EG_SPEC)
        self.assertFalse(r.is_valid)
        self.assertIn("cycle of length 8", r.reason)

    def test_min_degree_rejected(self):
        # 5-cycle: every vertex has degree 2.
        r = eg_verify({"num_vertices": 5, "edges": [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]}, EG_SPEC)
        self.assertFalse(r.is_valid)
        self.assertIn("degree", r.reason)

    def test_simple_graph_enforced(self):
        r = eg_verify({"num_vertices": 4, "edges": K4_EDGES + [(0, 1)]}, EG_SPEC)
        self.assertFalse(r.is_valid)
        self.assertIn("duplicate edge", r.reason)
        r = eg_verify({"num_vertices": 4, "edges": [(0, 0)] + K4_EDGES}, EG_SPEC)
        self.assertFalse(r.is_valid)
        self.assertIn("loop", r.reason)

    def test_budget_exhaustion_is_conservative_rejection(self):
        # Force a tiny budget through the spec knob: even K4 can't be
        # certified, and the verifier must REJECT rather than accept.
        spec = dict(EG_SPEC)
        spec["witness_node_budget"] = 2
        r = eg_verify({"num_vertices": 4, "edges": K4_EDGES}, spec)
        self.assertFalse(r.is_valid)
        self.assertIn("budget", r.reason)

    def test_schema_rejections(self):
        self.assertFalse(eg_verify({}, EG_SPEC).is_valid)
        self.assertFalse(eg_verify({"num_vertices": 3, "edges": []}, EG_SPEC).is_valid)
        self.assertFalse(eg_verify({"num_vertices": 65, "edges": []}, EG_SPEC).is_valid)
        self.assertFalse(
            eg_verify({"num_vertices": 4, "edges": [[0, 9]]}, EG_SPEC).is_valid
        )


class TestUnionClosedVerifier(unittest.TestCase):
    def test_power_set_rejected_frequency_at_half(self):
        # Power set of {1,2}: element 1 in 2 of 4 members — exactly half,
        # so the conjecture holds and the witness is rejected.
        fam = [[], [1], [2], [1, 2]]
        r = uc_verify({"sets": fam}, UC_SPEC)
        self.assertFalse(r.is_valid)
        self.assertIn(">= half", r.reason)

    def test_not_union_closed_rejected(self):
        fam = [[1], [2]]  # union {1,2} missing
        r = uc_verify({"sets": fam}, UC_SPEC)
        self.assertFalse(r.is_valid)
        self.assertIn("NOT union-closed", r.reason)

    def test_duplicates_rejected(self):
        r = uc_verify({"sets": [[1], [1]]}, UC_SPEC)
        self.assertFalse(r.is_valid)
        self.assertIn("distinct", r.reason)

    def test_empty_only_family_rejected(self):
        r = uc_verify({"sets": [[]]}, UC_SPEC)
        self.assertFalse(r.is_valid)
        self.assertIn("nonempty", r.reason)

    def test_full_power_set_boundary(self):
        # All subsets of {1,2,3}: 8 members, every element in 4/8 = exactly
        # half — the strict-inequality boundary must reject. (A genuine
        # accept-path fixture cannot exist: it would disprove Frankl.)
        fam = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        r = uc_verify({"sets": fam}, UC_SPEC)
        self.assertFalse(r.is_valid)

    def test_schema_rejections(self):
        self.assertFalse(uc_verify({}, UC_SPEC).is_valid)
        self.assertFalse(uc_verify({"sets": []}, UC_SPEC).is_valid)
        self.assertFalse(uc_verify({"sets": "nope"}, UC_SPEC).is_valid)
        self.assertFalse(uc_verify({"sets": [["a"]]}, UC_SPEC).is_valid)


if __name__ == "__main__":
    unittest.main()
