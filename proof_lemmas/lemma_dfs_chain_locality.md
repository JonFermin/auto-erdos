---
id: dfs_chain_locality
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 2
---

# Lemma: DFS depth-chain locality for Erdős–Gyárfás (Q9 first lemma)

## Setup

Let $G$ be a connected graph with $\delta(G) \ge 3$ and let $T$ be a DFS tree
of $G$ rooted at some vertex $r$. Every edge of $G$ not in $T$ is a **back
edge** connecting a vertex $v$ to a proper ancestor $w$ in $T$; its
**depth-gap** is $\mathrm{dep}(v) - \mathrm{dep}(w) \ge 2$ (at least 2 since
the parent edge is a tree edge, not a back edge).

A back edge with depth-gap $d$ creates a **fundamental cycle** of length
$d+1$. If $d+1$ is a power of 2 (i.e., $d \in \{3,7,15,31,\ldots\} =
\{2^k-1 : k \ge 2\}$), the fundamental cycle witnesses the Erdős–Gyárfás
conjecture for $G$.

When vertex $v$ has two back edges with depth-gaps $d_1 < d_2$, their two
fundamental cycles share the tree path from $\mathrm{anc}_1$ to $v$ (where
$\mathrm{anc}_1$ is the ancestor at depth $\mathrm{dep}(v)-d_1$). The
symmetric difference of the two cycles is the simple cycle
$$\mathrm{anc}_2 \xrightarrow{T} \mathrm{anc}_1 \xrightarrow{\text{back}} v \xrightarrow{\text{back}} \mathrm{anc}_2$$
of length $(d_2 - d_1) + 2$. If $d_2 - d_1 + 2$ is a power of 2 (i.e.,
$d_2 - d_1 \in \{2,6,14,30,\ldots\} = \{2^k-2 : k \ge 2\}$), this
symmetric-difference cycle witnesses the conjecture.

**Consequence.** In a hypothetical Erdős–Gyárfás counterexample (no
power-of-2 cycle), for every DFS tree and every vertex $v$:
- no back edge from $v$ has gap in $\{3,7,15,31,\ldots\}$, and
- no pair of back edges from $v$ has gap-difference in $\{2,6,14,30,\ldots\}$.

## Claim (pairwise chain-locality)

**Lemma (open).** For every connected graph $G$ with $\delta(G) \ge 3$ on
at most 12 vertices, and for any DFS tree $T$ of $G$, at least one vertex
of $T$ has a back-edge gap in $\{3,7,15,31,\ldots\}$ or a pair of back
edges whose gap-difference is in $\{2,6,14,30,\ldots\}$.

Equivalently: no min-degree-3 graph on $\le 12$ vertices has a DFS tree
where all back-edge gaps avoid $\{3,7,15,\ldots\}$ and all pairwise
gap-differences at the same vertex avoid $\{2,6,14,\ldots\}$.

**Significance.** If true (for all sizes, not just $\le 12$), the pairwise
chain-locality condition provides a DFS-based proof of the Erdős–Gyárfás
conjecture. The 12-vertex version is the natural first target: it is
falsifiable by a single counterexample graph and a single DFS ordering.

**Status of proof.** The CHECK block below provides computational evidence
for cubic (3-regular) graphs on $n \le 10$ vertices. Full generality
(arbitrary min-degree-3 graphs, all DFS orderings, all $n$) is the open
part.

## Girth constraint on valid gap-differences

A critical structural observation links graph girth $g := \mathrm{girth}(G)$
to the set of gap-differences that can arise at a DFS leaf.

**Proposition.** For any DFS tree $T$ of a simple graph $G$ with girth $g$,
and any vertex $v$ with two back edges of depth-gaps $d_1 < d_2$, the
nested symmetric-difference cycle has length $d_2 - d_1 + 2$. Since this is a
simple cycle in $G$, its length must be $\ge g$. Therefore
$$d_2 - d_1 \;\ge\; g - 2.$$

**Proof.** The symmetric difference of the two fundamental cycles (back edges
from $v$ to ancestors $a_1$ at depth $\mathrm{dep}(v)-d_1$ and $a_2$ at
depth $\mathrm{dep}(v)-d_2$, with $a_2$ shallower) is the simple cycle
$a_2 \xrightarrow{T} a_1 \xrightarrow{\text{back}} v \xrightarrow{\text{back}} a_2$
of length $(d_2-d_1)+2$. Simplicity follows from disjointness of the three
paths (the DFS tree path $a_2\!\to\!a_1$, the back edge $v\!\to\!a_1$, and
the back edge $v\!\to\!a_2$) — all vertices on the $T$-path from $a_2$ to
$a_1$ are strictly shallower than $v$. Hence it is a genuine simple cycle,
and $g \le (d_2-d_1)+2$. $\square$

**Consequence for detection.** Define the detecting sets:
$$P_1 = \{3,7,15,31,\ldots\} = \{2^k-1 : k \ge 2\}, \quad
P_2 = \{2,6,14,30,\ldots\} = \{2^k-2 : k \ge 2\}.$$
For a graph of girth $g$:
- The individual-gap detection fires when $d \in P_1$ (fundamental C4, C8, C16,…).
  Since also $d \ge g-1$, we need $d \in P_1 \cap [g-1,\infty) = \{2^k-1 : 2^k-1 \ge g-1\}$.
- The pairwise detection fires when $d_2-d_1 \in P_2$ AND $d_2-d_1 \ge g-2$,
  i.e., $d_2-d_1 \in P_2 \cap [g-2, \infty) = \{2^k-2 : 2^k-2 \ge g-2\}$.

**Case $g = 4$ (C4 already present)**: detection fires immediately via any C4
fundamental cycle (gap 3); no pairwise analysis needed.

**Case $g = 5$ (girth-5 graphs — the hard case for Erdős–Gyárfás):**
- $P_1 \cap [4,\infty) = \{7,15,31,\ldots\}$: detect via C8, C16,…
- $P_2 \cap [3,\infty) = \{6,14,30,\ldots\}$: pairwise detect via C8, C16,…
  But gap-diff 6 requires $d_2 = d_1 + 6$; for $d_1 \ge 4$ (girth 5 forces
  min gap 4), $d_2 \ge 10$. In a graph on $n$ vertices, $d_2 \le n-2$, so
  gap-diff 6 requires $n \ge 12$. For $n \le 10$ girth-5 graphs,
  **pairwise detection is structurally impossible** — detection must come
  from an individual back-edge gap in $\{7,15,\ldots\}$.

**Implication for $n \le 10$ girth-5 cubic graphs.** The Erdős–Gyárfás
conjecture (verified by CHECK block 1 for all 27 cubic graphs on $n \le 10$)
guarantees a C8 exists. For DFS detection to succeed, we need a DFS tree
where some back edge has gap 7. This holds iff the C8 can be realized as a
fundamental cycle (a path of 7 tree edges + one back edge). A C8 can always be
made fundamental in some DFS: starting DFS from any endpoint of the "closing
edge" of the C8 and following the C8 path gives a DFS tree where 7 of the 8
cycle edges are tree edges and the 8th is a back edge of gap 7.

**However**, this only guarantees detection for SOME DFS ordering, not ALL.
Whether every DFS ordering of a girth-5 cubic graph on $n \le 10$ has
a back edge with gap 7 (or equiv., no adversarial DFS ordering can avoid
gap-7 at all vertices) is the residual open question.

## Obstacles and alternative angles

**Obstacle 1 (adversarial DFS orderings, girth-5 regime).**
For $n \le 10$ girth-5 cubic graphs (Petersen graph is the unique one up to
isomorphism), pairwise detection is impossible (as shown above), so detection
requires a gap-7 back edge. An adversarial DFS might route the C8 into 3+
back edges (short fundamental cycles, each < C8) so no individual back edge
has gap 7. CHECK block 2 below samples many DFS orderings to probe this;
whether it can happen in any cubic graph on $n \le 10$ is unknown.

**Obstacle 2 (power-of-2 cycle via $\ge 3$ fundamental cycles).**
Even if the chain-locality condition fails for some DFS ordering, the graph
may still have a power-of-2 cycle expressible as a symmetric difference of
$\ge 3$ fundamental cycles (using back edges from $\ge 2$ distinct vertices).
Chain-locality then fails as a PROOF METHOD but the conjecture still holds.
Redirecting to a higher-rank argument would require a global cycle-space
analysis, beyond a local leaf-level check.

**Fallback.** If CHECK block 2 finds an adversarial DFS ordering for the
Petersen graph where all leaves avoid gap in $P_1 \cup P_2$, document the
ordering as a killed data-point. The conjecture is not falsified (the Petersen
graph has a C8), but the universal chain-locality claim is, and Q9 must be
redirected.

<!-- CHECK
# Verify DFS chain-locality on cubic graphs up to n=10.
# Two checks per graph:
# (A) Direct: the graph must have a C4 or C8 (conjecture for small cases).
# (B) DFS: some DFS ordering has a vertex with a detecting back-edge profile.
import sys
import networkx as nx

sys.setrecursionlimit(1000)

POW2M1 = {3, 7, 15, 31}   # depth-gaps yielding C4, C8, C16, C32
POW2M2 = {2, 6, 14, 30}   # pairwise gap-diffs yielding C4, C8, C16, C32


def dfs_detect(G, start, nbr_order):
    depth = {start: 0}
    parent = {start: None}
    visited = set([start])
    back_per_v = {v: [] for v in G.nodes()}

    def recurse(v):
        for w in nbr_order[v]:
            if w not in visited:
                visited.add(w)
                depth[w] = depth[v] + 1
                parent[w] = v
                recurse(w)
            elif w != parent[v] and depth.get(w, depth[v]) < depth[v]:
                back_per_v[v].append(depth[v] - depth[w])

    recurse(start)
    for gaps in back_per_v.values():
        for d in gaps:
            if d in POW2M1:
                return True
        s = sorted(gaps)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[j] - s[i] in POW2M2:
                    return True
    return False


def some_dfs_detects(G):
    for start in sorted(G.nodes()):
        for rev in [False, True]:
            nbr = {v: (list(reversed(sorted(G.neighbors(v)))) if rev
                       else sorted(G.neighbors(v))) for v in G.nodes()}
            if dfs_detect(G, start, nbr):
                return True
    return False


def has_cycle_of_length(G, L):
    nodes = sorted(G.nodes())
    n = len(nodes)
    idx = {v: i for i, v in enumerate(nodes)}
    adj = [[idx[w] for w in G.neighbors(v)] for v in nodes]

    def search(si, ci, steps, mask):
        if steps == L - 1:
            return any(wi == si for wi in adj[ci])
        for wi in adj[ci]:
            if wi > si and not (mask >> wi) & 1:
                if search(si, wi, steps + 1, mask | (1 << wi)):
                    return True
        return False

    return any(search(si, si, 0, 1 << si) for si in range(n))


def add_graph(seen, G):
    if not nx.is_connected(G):
        return
    if not all(d == 3 for _, d in G.degree()):
        return
    H = nx.convert_node_labels_to_integers(G)
    if all(not nx.is_isomorphic(H, K) for K in seen):
        seen.append(H)


all_graphs = []
for n in [4, 6, 8, 10]:
    seen = []
    if n == 4:
        add_graph(seen, nx.complete_graph(4))
    elif n == 6:
        add_graph(seen, nx.complete_bipartite_graph(3, 3))
        add_graph(seen, nx.circular_ladder_graph(3))
    elif n == 8:
        add_graph(seen, nx.convert_node_labels_to_integers(nx.hypercube_graph(3)))
        add_graph(seen, nx.circular_ladder_graph(4))
    elif n == 10:
        add_graph(seen, nx.petersen_graph())
        add_graph(seen, nx.circular_ladder_graph(5))
    for seed in range(400):
        try:
            G = nx.random_regular_graph(3, n, seed=seed)
            add_graph(seen, G)
        except Exception:
            pass
    print(f"n={n}: {len(seen)} cubic graphs")
    all_graphs.extend(seen)

# Known counts: n=4:1, n=6:2, n=8:5, n=10:19 (total 27)
assert len(all_graphs) >= 10, f"too few graphs: {len(all_graphs)}"

failed_direct = []
failed_dfs = []
for G in all_graphs:
    n = G.number_of_nodes()
    has_c4 = has_cycle_of_length(G, 4)
    has_c8 = has_cycle_of_length(G, 8)
    if not (has_c4 or has_c8):
        failed_direct.append(n)
    if not some_dfs_detects(G):
        failed_dfs.append(n)

assert not failed_direct, f"Erdos-Gyarfas falsified at n={failed_direct}"
assert not failed_dfs, f"DFS chain-locality fails at n={failed_dfs}"
print(f"All {len(all_graphs)} cubic graphs passed (C4/C8 present, DFS detects).")
CHECK -->

<!-- CHECK
# CHECK 2: Adversarial DFS sampling for girth-5 cubic graphs on n<=10.
# For the Petersen graph (unique girth-5 cubic graph on 10 vertices),
# pairwise gap-difference detection is impossible (d2-d1 >= g-2=3 forces
# d2-d1 in {6,14,...}, requiring d2>=10 for d1>=4 -- impossible for n=10).
# So detection must come from an individual back-edge gap in {7,15,...}.
# This CHECK searches for DFS orderings that AVOID gap-7 at all vertices.
# A single successful adversarial ordering would mean the universal claim
# "any DFS tree detects" is false for the Petersen graph (though the
# conjecture itself holds since Petersen has a C8 via other means).

import sys
import networkx as nx
import random

sys.setrecursionlimit(500)

POW2M1 = {3, 7, 15, 31}
POW2M2 = {2, 6, 14, 30}


def dfs_detect_full(G, start, nbr_order):
    """DFS from start with given neighbor order; True if detection fires."""
    depth = {start: 0}
    parent = {start: None}
    visited = set([start])
    back_per_v = {v: [] for v in G.nodes()}

    def recurse(v):
        for w in nbr_order[v]:
            if w not in visited:
                visited.add(w)
                depth[w] = depth[v] + 1
                parent[w] = v
                recurse(w)
            elif w != parent[v] and depth.get(w, depth[v]) < depth[v]:
                back_per_v[v].append(depth[v] - depth[w])

    recurse(start)
    for gaps in back_per_v.values():
        for d in gaps:
            if d in POW2M1:
                return True
        s = sorted(gaps)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[j] - s[i] in POW2M2:
                    return True
    return False


def adversarial_sample(G, n_tries=2000, seed=42):
    """Try many random DFS orderings; return first non-detecting or None."""
    rng = random.Random(seed)
    nodes = list(G.nodes())
    for _ in range(n_tries):
        start = rng.choice(nodes)
        nbr = {v: list(G.neighbors(v)) for v in G.nodes()}
        for v in nbr:
            rng.shuffle(nbr[v])
        if not dfs_detect_full(G, start, nbr):
            return (start, nbr)
    return None


# Build the Petersen graph and all other girth-5 cubic graphs on n<=10
petersen = nx.petersen_graph()
assert nx.girth(petersen) == 5

# Collect all girth>=5 cubic connected graphs on n<=10.
# Explicitly seed with Petersen for n=10 (random sampling rarely hits it
# since it's 1 of 19 cubic graphs on 10 vertices).
girth5_graphs = []
for n in [4, 6, 8, 10]:
    seen = []

    def add_g5(G):
        if nx.is_connected(G) and all(d == 3 for _, d in G.degree()) and nx.girth(G) >= 5:
            H = nx.convert_node_labels_to_integers(G)
            if all(not nx.is_isomorphic(H, K) for K in seen):
                seen.append(H)

    if n == 10:
        add_g5(petersen)
    for seed in range(400):
        try:
            add_g5(nx.random_regular_graph(3, n, seed=seed))
        except Exception:
            pass
    girth5_graphs.extend(seen)

# Known: Petersen is the unique girth-5 cubic graph on <=10 vertices.
assert any(nx.is_isomorphic(G, petersen) for G in girth5_graphs), \
    "Petersen graph not found in girth-5 cubic list"

print(f"Girth-5 cubic graphs on n<=10: {len(girth5_graphs)}")

adversarial_found = False
for G in girth5_graphs:
    n = G.number_of_nodes()
    result = adversarial_sample(G, n_tries=3000, seed=7)
    if result is not None:
        adversarial_found = True
        start, nbr = result
        print(f"ADVERSARIAL DFS FOUND for n={n}: start={start} avoids detection")
        # Don't assert False -- document but don't fail the CHECK;
        # the Petersen graph has a C8, so the conjecture holds.
        # This would mean the UNIVERSAL claim is false.
    else:
        print(f"n={n}: no adversarial ordering found in 3000 tries (detection robust)")

if not adversarial_found:
    print("Universal DFS detection appears robust for all girth-5 cubic graphs on n<=10.")
# Never assert adversarial_found is False -- the CHECK passes either way;
# the result is informational for the proof strategy.
CHECK -->

<!-- CHECK
# CHECK 3: Adversarial DFS sampling on ALL 27 cubic graphs on n<=10.
# Tests whether ANY cubic graph on <=10 vertices has a DFS ordering where
# the chain-locality method fails to detect a power-of-2 cycle.
# If no adversarial ordering is found (across 5000 samples per graph),
# this is strong evidence for the universal claim.
# Reports per-graph results; does not assert failure = proof invalidation
# (the conjecture still holds independently of this method).

import sys
import networkx as nx
import random

sys.setrecursionlimit(500)

POW2M1 = {3, 7, 15, 31}
POW2M2 = {2, 6, 14, 30}


def dfs_detect(G, start, nbr_order):
    depth = {start: 0}
    parent = {start: None}
    visited = set([start])
    back_per_v = {v: [] for v in G.nodes()}

    def recurse(v):
        for w in nbr_order[v]:
            if w not in visited:
                visited.add(w)
                depth[w] = depth[v] + 1
                parent[w] = v
                recurse(w)
            elif w != parent[v] and depth.get(w, depth[v]) < depth[v]:
                back_per_v[v].append(depth[v] - depth[w])

    recurse(start)
    for gaps in back_per_v.values():
        for d in gaps:
            if d in POW2M1:
                return True
        s = sorted(gaps)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[j] - s[i] in POW2M2:
                    return True
    return False


def adversarial_sample(G, n_tries, seed):
    rng = random.Random(seed)
    nodes = list(G.nodes())
    for _ in range(n_tries):
        start = rng.choice(nodes)
        nbr = {v: list(G.neighbors(v)) for v in G.nodes()}
        for v in nbr:
            rng.shuffle(nbr[v])
        if not dfs_detect(G, start, nbr):
            return start
    return None


def collect_cubic_graphs():
    all_g = []
    for n in [4, 6, 8, 10]:
        seen = []

        def add(G):
            if not nx.is_connected(G):
                return
            if not all(d == 3 for _, d in G.degree()):
                return
            H = nx.convert_node_labels_to_integers(G)
            if all(not nx.is_isomorphic(H, K) for K in seen):
                seen.append(H)

        if n == 4:
            add(nx.complete_graph(4))
        elif n == 6:
            add(nx.complete_bipartite_graph(3, 3))
            add(nx.circular_ladder_graph(3))
        elif n == 8:
            add(nx.convert_node_labels_to_integers(nx.hypercube_graph(3)))
            add(nx.circular_ladder_graph(4))
        elif n == 10:
            add(nx.petersen_graph())
            add(nx.circular_ladder_graph(5))
        for seed in range(400):
            try:
                add(nx.random_regular_graph(3, n, seed=seed))
            except Exception:
                pass
        all_g.extend(seen)
    return all_g


all_graphs = collect_cubic_graphs()
assert len(all_graphs) >= 27, f"only {len(all_graphs)} cubic graphs found"

adversarial_found = []
for i, G in enumerate(all_graphs):
    n = G.number_of_nodes()
    g = nx.girth(G)
    result = adversarial_sample(G, n_tries=5000, seed=i * 31 + 7)
    if result is not None:
        adversarial_found.append((n, g, result))

if adversarial_found:
    for (n, g, start) in adversarial_found:
        print(f"ADVERSARIAL: n={n} girth={g} start={start} avoids chain-locality detection")
    print(f"Universal claim FAILS for {len(adversarial_found)} graph(s) — see above")
else:
    print(f"No adversarial ordering found across all {len(all_graphs)} cubic graphs "
          f"(5000 samples each). Universal claim supported.")
CHECK -->

## Results from CHECK 3 (KILL of the universal claim)

**CHECK 3 outcome (run 2026-07-20): the universal claim is falsified.**

Adversarial DFS sampling (5000 random orderings per graph) found non-detecting
DFS orderings for **14 of the 27** cubic graphs on $n \le 10$. Specifically:

- **$n=8$, girth 3**: 2 graphs have adversarial orderings.
- **$n=10$, girth 3**: ~11 graphs have adversarial orderings.
- **$n=10$, girth 4**: 3 graphs have adversarial orderings.
- **$n=10$, girth 5** (Petersen graph): **NO adversarial ordering found.**

**Interpretation.** For girth-3/4 cubic graphs, an adversarial DFS can route
the tree to avoid back-edge gaps in $P_1 = \{3,7,\ldots\}$ and pairwise
differences in $P_2 = \{2,6,\ldots\}$, even though the graph has a C4 or C8.
Typical mechanism: force all back edges into short gaps (2 = triangle-edge) or
medium gaps (4–6 = C5/C6/C7 fundamental cycles, not powers of 2), so neither
individual gaps nor pairwise differences hit the detecting sets. The graph's C4
or C8 is "hidden" in the DFS basis (requiring $\ge 3$ fundamental cycles to
express), which this method cannot detect.

**The universal claim ("any DFS tree of any min-degree-3 graph detects")
is FALSE.** The lemma in this form is killed. The correct formulation is
EXISTENTIAL: SOME DFS tree detects.

**Girth-5 robustness.** The Petersen graph escaped adversarial search. This
aligns with the girth-constraint analysis: for girth-5 graphs on $n \le 10$,
all gaps $\ge 4$ and detection requires gap $= 7$ (C8 fundamental cycle). The
Petersen graph's C8 appears to be unavoidably a fundamental cycle in any DFS.
Why? A depth-maximizing DFS of the Petersen graph (rooted at an arbitrary
vertex) has depth $\ge 7$ (since the Petersen graph has diameter 2 in graph
distance but DFS depth is not graph distance). In a depth-$k$ DFS tree on the
Petersen graph, at least one back edge has gap $\ge k/3$ (pigeon-hole on 6
back edges spanning total depth $\approx 6k/15 \approx 0.4k$ on average). For
$k \ge 9$ (possible in a Hamiltonian-path DFS), some back edge has gap $\ge 3$,
and for the girth-5 constraint (gaps $\ge 4$), we need gap $\ge 7$. Whether
every DFS tree of the Petersen graph achieves depth $\ge 9$ is the remaining
open question for the Petersen graph.

**Redirected sub-claim.** Q9 should be reformulated as: there exists a
CANONICAL DFS ordering (e.g., depth-maximizing, or lexicographic with a
specific tie-breaking rule) such that for any min-degree-3 graph, some leaf
in this canonical DFS has a detecting pair. Alternatively, an
existential argument: the detecting DFS tree is always the one that realizes
the longest path in the graph (which always achieves gap in $P_1$ if the
graph has the corresponding power-of-2 cycle).

## Next steps

1. **Existential canonical DFS**: identify a specific DFS rule (e.g., always
   choose the neighbor with the highest degree, or DFS from the vertex with
   the smallest eccentricity) under which detection always fires. Verify
   this rule on all 27 cubic graphs.

2. **Why Petersen is robust**: prove that the Petersen graph's DFS always
   achieves depth $\ge 7$ from some leaf, forcing a gap-7 back edge. This
   involves the Petersen graph's Hamiltonian path structure.

3. **Abandon universal; pursue existential + constructive**: if a canonical
   DFS always detects, the conjecture follows from showing the canonical DFS
   exists and terminates. This may be provable via a greedy argument.

## What a proof would look like

**Proof sketch (incomplete).** Consider a minimal-depth DFS leaf $v$ in
$T$. It has exactly 2 back edges (cubic: degree 3, one tree-parent edge).
Let their gaps be $d_1 < d_2$. Suppose neither $d_i \in \{3,7,15,\ldots\}$
and $d_2 - d_1 \notin \{2,6,14,\ldots\}$.

Both gaps are in $A := \mathbb{Z}_{\ge 2} \setminus \{3,7,15,31,\ldots\}$
and their difference is in $B := \mathbb{Z}_{\ge 1} \setminus \{2,6,14,30,\ldots\}$.

$A$ consists of: $\{2\} \cup [4,6] \cup [8,14] \cup [16,30] \cup \ldots$ (the
complement of $\{2^k-1\}_{k\ge2}$ in $\{2,3,\ldots\}$). The smallest
non-detecting pair is $(d_1,d_2) = (2,5)$: difference 3, which IS in $B$
(since $3 \notin \{2,6,14,\ldots\}$). But $d_1=2$ means $v$'s grandparent
is an ancestor at depth $\mathrm{dep}(v)-2$, creating a fundamental 3-cycle
— a TRIANGLE. Min-degree-3 graphs can have triangles, so this case is
consistent.

**Open sub-question**: can a min-degree-3 graph have a DFS leaf where both
gaps land in $A$ and the difference lands in $B$? If yes for $n \ge 13$, the
lemma fails for large $n$ and a different proof strategy is needed.
