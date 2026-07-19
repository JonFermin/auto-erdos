"""erdos_gyarfas_witness — verifier for Erdős–Gyárfás counterexample witnesses.

The Erdős–Gyárfás conjecture (1995): every finite graph with minimum degree
at least 3 contains a simple cycle whose length is a power of 2. A witness
here is a finite simple graph with min degree >= 3 and NO cycle of length
2^k for any k — a single such graph disproves the conjecture. This module
is the only sanctioned path to ``witness_valid = 1`` on the
``erdos_gyarfas`` proof spec, so it must be conservative: it accepts ONLY
when its exhaustive cycle search *completes* within budget and finds no
power-of-2 cycle. Budget exhaustion is a rejection, never an acceptance.

Witness payload:

    {
      "num_vertices": int,                # 4 <= n <= MAX_VERTICES
      "edges": [[u, v], ...]              # 0-indexed, simple (no loops/dups)
    }

Verifier contract — ``verify_witness(payload, spec) -> VerifyResult``:
    - is_valid=True iff
        (a) the graph is simple, within size caps;
        (b) every vertex has degree >= 3;
        (c) for every power-of-2 length L with 4 <= L <= n, the exhaustive
            search proves NO simple cycle of length exactly L exists, and
            every per-length search completed within the operation budget.
    - score = float(num_vertices) (smaller counterexamples are not ranked
      differently — a single witness suffices; the keep rule fires on
      is_valid alone).

Search: for each target length L, enumerate simple paths by DFS from each
start vertex v, restricted to vertices with index > v except v itself
(so v is the minimum-index vertex of any found cycle — each cycle is
found exactly once and the search space shrinks). A cycle of length L is
found when a path v, x_1, ..., x_{L-1} of distinct vertices has an edge
x_{L-1} -> v. The DFS counts node expansions against a global budget;
exceeding it aborts with is_valid=False (cannot certify absence).

Known context (2026): the conjecture is open; verified for 3-connected
cubic planar graphs (Heckman–Krakovski 2013), P_10-free graphs (Hu–Shen
2024); any cubic counterexample has >= 30 vertices (Markström) and a 2026
preprint shows a minimal counterexample is predominantly cubic. Sparse,
near-cubic graphs are therefore the plausible witness shape — which is
exactly the regime where this exhaustive search is cheap (cubic graphs
have few long simple paths).

Stdlib only. Matches library.primitive_set_witness.VerifyResult's shape.
"""
from __future__ import annotations

import time
from dataclasses import dataclass

MAX_VERTICES = 64
MAX_EDGES = 160
# Global node-expansion budget across all per-length searches. Cubic
# graphs up to 64 vertices complete far below this; dense adversarial
# inputs hit the cap and are rejected (conservatively) instead.
DEFAULT_NODE_BUDGET = 20_000_000


@dataclass
class VerifyResult:
    is_valid: bool
    score: float
    reason: str
    verifier_seconds: float


class _BudgetExceeded(Exception):
    pass


def _powers_of_two_up_to(n: int) -> list[int]:
    """Cycle lengths to exclude: powers of 2 in [3, n]. 2 is not a cycle
    length in a simple graph, so the relevant lengths start at 4."""
    out = []
    L = 4
    while L <= n:
        out.append(L)
        L *= 2
    return out


def _has_cycle_of_length(
    adj: list[list[int]], n: int, L: int, budget: list[int]
) -> bool:
    """Exhaustive check for a simple cycle of length exactly L.

    DFS from each start vertex v over paths whose interior vertices all
    have index > v (v is the cycle's minimum-index vertex). budget is a
    one-element list used as a mutable countdown of node expansions;
    raises _BudgetExceeded when it runs out.
    """
    visited = [False] * n
    adj_set = [set(neigh) for neigh in adj]
    for v in range(n):
        def dfs(u: int, depth: int) -> bool:
            budget[0] -= 1
            if budget[0] <= 0:
                raise _BudgetExceeded
            if depth == L:
                # depth counts vertices on the path v, ..., u; an edge
                # u -> v closes a simple cycle of length exactly L.
                return v in adj_set[u]
            for w in adj[u]:
                if w > v and not visited[w]:
                    visited[w] = True
                    found = dfs(w, depth + 1)
                    visited[w] = False
                    if found:
                        return True
            return False

        visited[v] = True
        found = dfs(v, 1)
        visited[v] = False
        if found:
            return True
    return False


def verify_witness(payload: dict, spec: dict) -> VerifyResult:
    t0 = time.time()

    if not isinstance(payload, dict):
        return VerifyResult(False, 0.0, f"payload must be dict, got {type(payload).__name__}", time.time() - t0)
    if "num_vertices" not in payload or "edges" not in payload:
        return VerifyResult(False, 0.0, "payload missing 'num_vertices' or 'edges'", time.time() - t0)

    try:
        n = int(payload["num_vertices"])
    except (TypeError, ValueError) as e:
        return VerifyResult(False, 0.0, f"'num_vertices' not an int: {e}", time.time() - t0)
    if not (4 <= n <= MAX_VERTICES):
        return VerifyResult(False, 0.0, f"num_vertices={n} outside [4, {MAX_VERTICES}]", time.time() - t0)

    raw_edges = payload["edges"]
    if not isinstance(raw_edges, list):
        return VerifyResult(False, 0.0, f"'edges' must be list, got {type(raw_edges).__name__}", time.time() - t0)
    if len(raw_edges) > MAX_EDGES:
        return VerifyResult(False, 0.0, f"{len(raw_edges)} edges exceeds cap {MAX_EDGES}", time.time() - t0)

    edge_set: set[tuple[int, int]] = set()
    for e in raw_edges:
        if not (isinstance(e, (list, tuple)) and len(e) == 2):
            return VerifyResult(False, 0.0, f"edge {e!r} is not a pair", time.time() - t0)
        try:
            u, v = int(e[0]), int(e[1])
        except (TypeError, ValueError):
            return VerifyResult(False, 0.0, f"edge {e!r} has non-integer endpoint", time.time() - t0)
        if u == v:
            return VerifyResult(False, 0.0, f"loop at vertex {u} — graph must be simple", time.time() - t0)
        if not (0 <= u < n and 0 <= v < n):
            return VerifyResult(False, 0.0, f"edge ({u},{v}) endpoint out of range [0,{n})", time.time() - t0)
        key = (min(u, v), max(u, v))
        if key in edge_set:
            return VerifyResult(False, 0.0, f"duplicate edge ({u},{v}) — graph must be simple", time.time() - t0)
        edge_set.add(key)

    adj: list[list[int]] = [[] for _ in range(n)]
    for (u, v) in edge_set:
        adj[u].append(v)
        adj[v].append(u)

    # Min-degree check.
    for v in range(n):
        if len(adj[v]) < 3:
            return VerifyResult(
                False, 0.0,
                f"vertex {v} has degree {len(adj[v])} < 3 — not in the conjecture's hypothesis class",
                time.time() - t0,
            )

    # Exhaustive power-of-2 cycle exclusion.
    lengths = _powers_of_two_up_to(n)
    budget = [int(spec.get("witness_node_budget", DEFAULT_NODE_BUDGET))]
    checked: list[int] = []
    for L in lengths:
        try:
            if _has_cycle_of_length(adj, n, L, budget):
                return VerifyResult(
                    False, 0.0,
                    f"graph CONTAINS a cycle of length {L} = 2^{L.bit_length()-1} — "
                    f"conjecture holds on this graph, not a counterexample "
                    f"(checked lengths so far: {checked + [L]})",
                    time.time() - t0,
                )
        except _BudgetExceeded:
            return VerifyResult(
                False, 0.0,
                f"node-expansion budget exhausted while searching for {L}-cycles — "
                f"cannot certify absence; witness REJECTED conservatively "
                f"(shrink the graph or raise witness_node_budget in the spec)",
                time.time() - t0,
            )
        checked.append(L)

    return VerifyResult(
        True, float(n),
        f"VERIFIED counterexample candidate: simple graph, n={n}, m={len(edge_set)}, "
        f"min degree >= 3, exhaustive search completed and found NO cycle of length "
        f"in {checked} (all powers of 2 in [4, {n}]); this graph disproves "
        f"Erdős–Gyárfás if independently confirmed",
        time.time() - t0,
    )
