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

## Obstacles and alternative angles

**Obstacle 1 (non-detecting pairs exist).** The condition is not void: pairs
$(d_1, d_2)$ that avoid both detection sets do exist. For instance
$d_1 = 2, d_2 = 5$: $2 \notin \{3,7,15,\ldots\}$, $5 \notin \{3,7,\ldots\}$,
$5-2=3 \notin \{2,6,14,\ldots\}$. A cubic graph leaf with this DFS profile
would escape chain-locality detection. Whether min-degree-3 and small $n$
together prevent this profile from arising (or force some other vertex to
detect instead) is the open combinatorial question.

**Obstacle 2 (DFS ordering sensitivity).** For the universal claim ("any DFS
tree"), the DFS ordering is adversarially chosen. A proof would need to show
that no matter how the DFS is rooted and no matter how ties are broken, some
vertex detects. The CHECK samples two orderings per root; it does not cover
all $n! $ orderings.

**Obstacle 3 (power-of-2 cycle via $\ge 3$ fundamental cycles).** Even if
the pairwise condition fails, the graph may still have a power-of-2 cycle
expressible only as a symmetric difference of $\ge 3$ fundamental cycles (using
back edges from $\ge 2$ distinct vertices). In that case chain-locality is
insufficient and a more global cycle-space argument is needed.

**Fallback.** If the CHECK below reveals a cubic graph on $\le 10$ vertices
where SOME DFS ordering avoids detection, document the graph and ordering as
a killed data-point and redirect Q9 toward Obstacle 3 (higher-rank
combination of fundamental cycles).

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

## Next steps (if CHECK passes)

1. **Strengthen to "all DFS orderings"**: the CHECK only verifies SOME DFS
   ordering detects. A proof of the universal claim requires showing every
   ordering detects, or finding a canonical ordering (e.g., degree-decreasing,
   or depth-maximizing) that always works. Try to find an adversarial DFS
   ordering that avoids detection on some n=10 cubic graph.

2. **Extend to min-degree-3 non-cubic**: the cubic case is the tight one
   (higher-degree vertices give more back edges and more pairs). If CHECK
   passes for cubic graphs, the non-cubic extension likely holds but needs
   its own CHECK (or a degree-monotonicity argument).

3. **General n**: if the pattern for $n \le 12$ is confirmed, move toward
   a combinatorial proof. The key structural fact is that in a cubic graph
   DFS tree, every leaf has exactly 2 back edges — the chain-locality
   condition needs to handle the constraint that both gaps can be
   "non-detecting" simultaneously.

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
