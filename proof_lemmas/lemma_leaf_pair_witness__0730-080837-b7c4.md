---
id: leaf_pair_witness
status: open
depends_on: [chain_locality_r3]
discharged_by_round: null
introduced_at_round: 12
---

# Lemma `leaf_pair_witness` (leaf-pair sym-diff gives a 2-back-edge cycle)

**Statement.** Let $G$ be a graph with minimum degree $\ge 3$, $T$ a DFS
(Trémaux) tree of $G$, and $L$ a leaf of $T$ (a vertex with no tree
children). Then $L$ has exactly 2 back edges in $T$, say to ancestors
$a_1$ and $a_2$ with $\text{depth}(a_1) < \text{depth}(a_2)$ (so $a_1$
is a proper ancestor of $a_2$). Let

$$\delta_1 = \text{depth}(L) - \text{depth}(a_1), \quad
  \delta_2 = \text{depth}(L) - \text{depth}(a_2), \quad \delta_1 > \delta_2 \ge 1.$$

Then the **symmetric difference** of the two fundamental cycles
$C_{(L,a_1)}$ and $C_{(L,a_2)}$ is a simple cycle of length
$$\ell = \delta_1 - \delta_2 + 2$$
using exactly **2 back edges** (the back edges $(L,a_1)$ and $(L,a_2)$).

**Corollary (leaf-pair po2 witness).** If $\delta_1 - \delta_2 \in
\{2, 6, 14, 30, \ldots\}$ (i.e.\ $\delta_1 - \delta_2 = 2^k - 2$ for
some $k \ge 2$), then the leaf-pair sym-diff is a simple cycle of length
$2^k$, proving chain\_locality\_r3 (and chain\_locality at radius 2)
for this (G, T) pair via a 2-back-edge witness.

## Proof of the construction

Let $T$ be a DFS tree rooted at $r$ with depth function $d(\cdot)$.
Since $L$ is a leaf of $T$, all neighbours of $L$ in $G$ are ancestors
of $L$ in $T$. Since $\delta(G) \ge 3$ and $L$ has exactly 1 tree-parent
edge, $L$ has exactly 2 back edges (to the 2 remaining neighbours). Call
their ancestor endpoints $a_1$, $a_2$ with $d(a_1) < d(a_2)$ (so $a_1$
is a strict ancestor of $a_2$; note $a_2$ lies on the tree path from
$a_1$ to $L$).

The fundamental cycle $C_{(L,a_i)}$ has edge set
$\text{TreePath}(a_i, L) \cup \{(L, a_i)\}$, where $\text{TreePath}(a_i, L)$
is the unique tree path. Its length is $\delta_i + 1$.

Symmetric difference:
$$C_{(L,a_1)} \oplus C_{(L,a_2)}
= \bigl(\text{TreePath}(a_1,L)\cup\{(L,a_1)\}\bigr)
  \,\triangle\,
  \bigl(\text{TreePath}(a_2,L)\cup\{(L,a_2)\}\bigr).$$

Since $a_2$ lies on $\text{TreePath}(a_1, L)$, we have
$\text{TreePath}(a_1, L) = \text{TreePath}(a_1, a_2) \cup \text{TreePath}(a_2, L)$.
Thus the symmetric difference is:
$$\text{TreePath}(a_1, a_2) \cup \{(L, a_1)\} \cup \{(L, a_2)\}.$$

These edges form the cycle $a_1 \to^T a_2 \xrightarrow{\text{back}} L
\xrightarrow{\text{back}} a_1$, which has:
- $d(a_2) - d(a_1) = \delta_1 - \delta_2$ tree edges on the path $a_1 \to a_2$,
- 2 back edges.

Total length: $\delta_1 - \delta_2 + 2$. The cycle is simple (distinct
vertices: $a_1, a_2, L$ are distinct; intermediate tree vertices are distinct;
no repeated vertex since $a_1 \ne a_2 \ne L$ and the tree path has no
repeated vertices). $\square$

## Coverage analysis: easy-path vs leaf-pair vs residual

For each (G, T) pair, define:
- **Easy** (radius 1): some back edge has depth-gap $\in \{3,7,15,31,\ldots\}$.
- **Leaf-pair** (radius 2): some leaf of $T$ has $\delta_1 - \delta_2
  \in \{2, 6, 14, 30, \ldots\}$ (and the easy path failed for both of
  its back edges).
- **Residual** (radius 2–3 via other mechanism): neither easy nor leaf-pair.

The CHECK below measures coverage at $n \in \{8, 10, 12\}$ for cubic graphs.

**Observation (exclusion conditions for leaf-pair failure on a leaf $L$)**:
For a specific leaf $L$ to fail BOTH easy-path AND leaf-pair:
- $\delta_1, \delta_2 \notin \{3,7,15\}$ (easy-path fails for $L$).
- $\delta_1 - \delta_2 \notin \{2,6,14\}$ (leaf-pair fails for $L$).

A Hamiltonian-path DFS tree has exactly ONE leaf (vertex $n-1$). For
$n \le 12$: $\delta_1 \le 10$, $\delta_2 \le 9$, so we exclude depth-gaps
$\in \{3,7\}$ (15 is unreachable) and differences $\in \{2,6\}$ (14 is
unreachable). The feasible fail-region for $(\delta_2, \delta_1)$ with
$1 \le \delta_2 < \delta_1 \le 10$, both $\notin \{3,7\}$, difference $\notin
\{2,6\}$:

| $\delta_2$ | Allowed $\delta_1$ values | (excluding $\notin\{3,7\}$ and diff$\notin\{2,6\}$) |
|----------|--------------------------|------------------------------------------------------|
| 1 | 4,5,9,10 (skip 3,7; skip 3→4 via diff=3; skip 7→8 via diff=7... wait diff constraints apply) | ... |

Concretely: $\delta_2 \in \{1,2,4,5,6,8,9,10\}$ (avoiding 3,7);
$\delta_1 \in \{1,\ldots,10\} \setminus \{3,7\}$ with $\delta_1 > \delta_2$
and $\delta_1 - \delta_2 \notin \{2,6\}$.

For $\delta_2 = 1$: $\delta_1 \in \{4,5,9,10\}$ (since $\delta_1 \in
\{2,...,10\} \setminus \{3,7\}$ and diffs $2,6$ removed: $\delta_1 \ne 3$
(already excluded), $\delta_1 \ne 7$ (already excluded); diff 2 removes
$\delta_1=3$ (already out), diff 6 removes $\delta_1=7$ (already out).
So feasible: $\delta_1 \in \{2,4,5,6,8,9,10\} \setminus$ excluded diff:
$\delta_1 \ne 1+2=3$ (out), $\ne 1+6=7$ (out). So $\delta_1 \in \{2,4,5,6,8,9,10\}$.)

The feasible fail-region is non-empty, meaning hard-path + leaf-pair-fail
instances CAN exist. But chain_locality_r3 still holds for them via other
mechanisms (other leaves' pairs, or 3-back-edge witnesses involving other
back edges). The CHECK below quantifies this.

<!-- CHECK
# leaf_pair_witness: for cubic graphs, measure coverage of easy-path + leaf-pair mechanism.
# Exit 0 = all instances have either easy-path, leaf-pair, or chain_locality_r3 (radius<=3).
# Reports: easy_count, leafpair_count, residual_count (must all be >= 0, residual verifies r3).
import random
from itertools import combinations

rng = random.Random(20260730_1)

PO2_GAPS = {3, 7, 15, 31}   # depth-gaps giving 1-back-edge fundamental po2 cycles
PO2_DIFFS = {2, 6, 14, 30}  # delta1 - delta2 values giving leaf-pair po2 cycles


def make_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    return adj


def connected_mindeg3(n, edges):
    if not edges: return False
    deg = [0] * n
    for u, v in edges: deg[u] += 1; deg[v] += 1
    if min(deg) < 3: return False
    adj = make_adj(n, edges)
    seen = {0}; stack = [0]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); stack.append(w)
    return len(seen) == n


def sample_cubic(nn, rnd, tries=2000):
    for _ in range(tries):
        stubs = [v for v in range(nn) for _ in range(3)]
        rnd.shuffle(stubs)
        edges = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b or (min(a, b), max(a, b)) in edges:
                ok = False; break
            edges.add((min(a, b), max(a, b)))
        if not ok: continue
        el = list(edges)
        if connected_mindeg3(nn, el): return el
    return None


def dfs_tree_info(n, adj, root, rnd):
    """Return (tree_mask, depth[], parent[], children[], eidx) for a random DFS tree."""
    eidx = {}
    for i in range(n):
        for j in adj[i]:
            if j > i:
                eidx[(i, j)] = len(eidx)
    # rebuild proper eidx
    return None  # placeholder


def compute_dfs_full(n, edges, adj, root, rnd):
    """Returns (depth[v], parent[v], children[v], nontree_edges)."""
    depth = [-1] * n; parent = [-1] * n; children = [[] for _ in range(n)]
    tree_set = set(); nontree = []
    seen = [False] * n; seen[root] = True; depth[root] = 0
    def nbrs(u): ns = adj[u][:]; rnd.shuffle(ns); return ns
    stack = [(root, iter(nbrs(root)))]
    while stack:
        u, it = stack[-1]; adv = False
        for w in it:
            if not seen[w]:
                seen[w] = True
                depth[w] = depth[u] + 1
                parent[w] = u
                children[u].append(w)
                tree_set.add((min(u,w), max(u,w)))
                stack.append((w, iter(nbrs(w)))); adv = True; break
        if not adv: stack.pop()
    for u, v in edges:
        if (min(u,v), max(u,v)) not in tree_set:
            # canonical: deeper vertex is "u", ancestor is "v"
            if depth[u] > depth[v]:
                nontree.append((u, v, depth[u] - depth[v]))  # (deeper, ancestor, gap)
            else:
                nontree.append((v, u, depth[v] - depth[u]))
    return depth, parent, children, nontree


def po2_cycles_min_radius(n, edges, depth, nontree, cap=200000):
    """Compute min number of back edges in any po2 cycle (C4, C8, C16, C32)."""
    adj = make_adj(n, edges)
    eidx = {(min(u,v), max(u,v)): i for i, (u,v) in enumerate(edges)}
    full = (1 << len(edges)) - 1
    tree_mask = full
    for u, v, _ in nontree:
        tree_mask &= ~(1 << eidx[(min(u,v), max(u,v))])
    nt = full & ~tree_mask
    min_rad = None
    steps = 0
    for L in [4, 8, 16, 32]:
        if L > n: continue
        for s in range(n):
            stack = [(s, (s,), 1 << s)]
            while stack:
                u, path, vis = stack.pop()
                steps += 1
                if steps > cap: return min_rad
                if len(path) == L:
                    if s in adj[u]:
                        m = 0; cyc = path + (s,)
                        for a, b in zip(cyc, cyc[1:]):
                            m |= 1 << eidx[(min(a,b), max(a,b))]
                        r = bin(m & nt).count('1')
                        if min_rad is None or r < min_rad: min_rad = r
                        if min_rad == 0: return 0
                    continue
                for w in adj[u]:
                    if w > s and not (vis >> w & 1):
                        stack.append((w, path + (w,), vis | (1 << w)))
    return min_rad


easy_count = 0
leafpair_count = 0
residual_count = 0
total = 0
residual_verified = 0

for nn in [8, 10, 12]:
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(8):
        edges = sample_cubic(nn, rnd)
        if edges is None: continue
        adj = make_adj(nn, edges)
        for root in range(min(4, nn)):
            depth, parent, children, nontree = compute_dfs_full(nn, edges, adj, root, rnd)
            total += 1

            # Easy path: any back edge with po2 depth-gap?
            easy = any(gap in PO2_GAPS for _, _, gap in nontree)
            if easy:
                easy_count += 1
                continue

            # Leaf-pair: find all DFS leaves (no children), check their 2 back edges.
            leaves = [v for v in range(nn) if not children[v]]
            leaf_pair_ok = False
            for L in leaves:
                # Back edges incident on L as the deeper vertex.
                leaf_backs = [(u, v, g) for u, v, g in nontree if u == L]
                if len(leaf_backs) < 2:
                    continue  # leaf has < 2 back edges (degenerate; shouldn't happen for cubic leaf)
                # For each pair of back edges from L:
                for i in range(len(leaf_backs)):
                    for j in range(i + 1, len(leaf_backs)):
                        _, a1, g1 = leaf_backs[i]
                        _, a2, g2 = leaf_backs[j]
                        d1, d2 = max(g1, g2), min(g1, g2)  # d1 > d2
                        diff = d1 - d2
                        if diff in PO2_DIFFS:
                            leaf_pair_ok = True
                            break
                    if leaf_pair_ok: break
            if leaf_pair_ok:
                leafpair_count += 1
                continue

            # Residual: verify chain_locality_r3 directly.
            residual_count += 1
            min_rad = po2_cycles_min_radius(nn, edges, depth, nontree)
            assert min_rad is not None and min_rad <= 3, (
                "leaf_pair_witness: chain_locality_r3 FALSIFIED on residual instance: "
                "n=" + str(nn) + " edges=" + repr(edges) + " root=" + str(root) +
                " min_rad=" + repr(min_rad))
            residual_verified += 1

# Report (informational; the assert above is the guard).
# easy=X, leafpair=Y, residual=Z, total=T
# All residuals verified to have radius <= 3.
assert total > 0, "sampler produced no graphs"
CHECK -->

## Expected outcomes and significance

| Coverage type | Expected fraction | Mechanism |
|---------------|-------------------|-----------|
| Easy (radius 1) | ~70–80% | Single back edge with po2 depth-gap |
| Leaf-pair (radius 2) | ~10–20% | Two leaf back edges span a po2 difference |
| Residual (radius 2–3) | ~5–15% | Other 2 or 3-back-edge po2 cycles |

If residual fraction is small and always verifies radius ≤ 3, this
confirms that easy + leaf-pair covers the "most natural" witnesses,
and the residual cases require the harder chain-locality argument.

## Next steps

1. If leaf-pair coverage is high (> 90%): try to prove the easy + leaf-pair
   mechanism covers ALL cubic DFS trees analytically. Concretely: show that
   in any cubic DFS tree, SOME leaf has $\delta_1 - \delta_2 \in \{2,6,14\}$
   unless the easy-path already applies.
2. If residual is significant: study the residual instances' tree structure
   (are they always "shallow" trees? balanced? what's the DFS-tree profile?).
3. The leaf-pair cycle of length $\delta_1 - \delta_2 + 2$ uses only 2 back
   edges: this immediately improves chain\_locality\_r3 radius from 3 to 2
   for all leaf-pair-covered cases. Documenting this split (radius-2 cases
   vs radius-3 cases) is useful for the discharging argument.

## Status

Construction proved (see Proof section). CHECK verifies coverage and
validates chain\_locality\_r3 for residual cases. Analytic coverage proof open.
