---
id: back_edge_triangle
status: open
depends_on: [leaf_pair_witness, chain_locality_r3]
discharged_by_round: null
introduced_at_round: 13
---

# Lemma `back_edge_triangle` (back-edge triangle gives a 3-back-edge po2 cycle)

**Statement.** In a cubic DFS tree $(G, T)$, suppose:
- No back edge has depth-gap $\in \{3,7,15,\ldots\}$ (easy-path fails).
- No leaf has $\delta_1 - \delta_2 \in \{2,6,14,\ldots\}$ for its two back-edge gaps (leaf-pair fails).

Then a **3-back-edge po2 cycle** always exists. Concretely: there is a
simple cycle $C$ of length $4$ or $8$ whose edge set consists of exactly
3 back edges and exactly 1 (resp. 5) tree edges.

The cycle $C$ arises as the symmetric difference of 3 fundamental cycles
$C_{b_1} \oplus C_{b_2} \oplus C_{b_3}$, where $b_1, b_2, b_3$ are back
edges satisfying a specific ancestor interaction condition.

**Significance.** Together with Lemma `leaf_pair_witness` (R12) and the
easy-path mechanism (Section 13), this completes the coverage taxonomy:

| Type | Condition | Mechanism | Radius |
|------|-----------|-----------|--------|
| Easy | Gap $\in \{3,7,15,\ldots\}$ | 1 fundamental cycle | 1 |
| Leaf-pair | Leaf gap-diff $\in \{2,6,14,\ldots\}$ | Sym-diff of leaf's 2 back edges | 2 |
| Back-edge triangle | Neither above | Sym-diff of 3 specific back edges | 3 |

Proving this lemma would establish chain\_locality\_r3 completely for cubic
DFS trees.

## Structure of the back-edge triangle (from CL-A analysis)

Exhaustive enumeration of all Trémaux spanning trees of CL-A (n=10, cubic)
found exactly **4 Trémaux trees requiring radius 3** (after easy-path and
leaf-pair both fail). In all 4 cases:

- Depth-gaps are $\{2, 5, 9\}$ (no depth-gap in $\{3,7\}$).
- The leaf has gaps $(5, 9)$ with difference $= 4 \notin \{2,6,14\}$.
- The best po2 witness is the **same** specific C4 $= (3,7,6,4)$ with:
  - Back edges: $(7,3)$, $(7,6)$, $(4,6)$ (3 back edges).
  - Tree edge: $(3,4)$ (1 tree edge).

In all 4 trees, vertex 7 is the **double-sender** (a vertex carrying 2
back edges to ancestors $a_1, a_2$), and vertex 4 carries the third
back edge to ancestor $a_1$'s region, forming a "triangle" in the
back-edge graph: both $7$ and $4$ have back edges to the same ancestor
region, and $7$ also sends to a second ancestor.

## Sym-diff computation (verified)

For Tree 1 of CL-A (root = 6, depth = [7,1,6,4,5,2,0,9,3,8]):
- Back edges: $(7,3,\delta=5)$, $(8,1,2)$, $(4,6,5)$, $(9,2,2)$, $(7,6,9)$, $(0,5,5)$.
- $C_{(7,3)}$: tree path $3 \to 4 \to 2 \to 0 \to 9 \to 7$ + back edge $(7,3)$.
  Edges: $\{3\text{-}4, 4\text{-}2, 2\text{-}0, 0\text{-}9, 9\text{-}7, (7,3)\}$.
- $C_{(7,6)}$: tree path $6 \to 1 \to 5 \to 8 \to 3 \to 4 \to 2 \to 0 \to 9 \to 7$ + back.
  Edges: $\{6\text{-}1, 1\text{-}5, 5\text{-}8, 8\text{-}3, 3\text{-}4, 4\text{-}2, 2\text{-}0, 0\text{-}9, 9\text{-}7, (7,6)\}$.
- $C_{(4,6)}$: tree path $6 \to 1 \to 5 \to 8 \to 3 \to 4$ + back edge $(4,6)$.
  Edges: $\{6\text{-}1, 1\text{-}5, 5\text{-}8, 8\text{-}3, 3\text{-}4, (4,6)\}$.

Symmetric difference $C_{(7,3)} \oplus C_{(7,6)} \oplus C_{(4,6)}$:
- Each tree edge present in 2 of the 3 cycles cancels (count = 2, even).
- Tree edge $3\text{-}4$ appears in ALL 3: count = 3 (odd) → **remains**.
- Back edges $(7,3), (7,6), (4,6)$: each in exactly one cycle → **remains**.
- Result: $\{(7,3), (7,6), (4,6), 3\text{-}4\}$ = exactly C4 $(3,7,6,4)$. $\square$

## Pattern abstraction

Let $v$ be the **double-sender**: a vertex with 2 back edges to ancestors
$a_1$ (shallower, depth-gap $\delta_v^{(1)} > \delta_v^{(2)}$) and $a_2$
(deeper). Let $w$ be another vertex on the DFS tree path from $a_2$ to $v$,
with a back edge to $a_1$.

Then:
$$C_{(v,a_1)} \oplus C_{(v,a_2)} \oplus C_{(w,a_1)} = \text{cycle: } w \to^T a_2 \to^T v \to^b a_1 \to^T w$$
... but this requires specific ancestor relationships and tree-edge structures.

**Corrected**: the C4 $(3,7,6,4)$ in the CL-A case has:
- Double-sender: vertex 7 sends back to $a_1 = 3$ (gap 5) and $a_2 = 6$ (gap 9).
  Note $a_2 = 6$ is the ROOT (depth 0), so it's a "global" back edge.
- Third back-edge sender: vertex 4 sends back to $a_2 = 6$ (gap 5 too).
- Tree edge $3 \to 4$: vertex 3 is parent of 4 in the DFS tree.

The C4 cycle is: $3 \xrightarrow{b} 7 \xrightarrow{b} 6 \xleftarrow{b} 4 \xrightarrow{T} 3$.
Three back edges from $\{7\to 3, 7\to 6, 4\to 6\}$, one tree edge $3\to 4$.

## General existence claim (open)

**Claim**: In any cubic DFS tree where easy-path and leaf-pair both fail,
there exist vertices $v$ (with 2 back edges) and $w$ (with 1 back edge)
such that their shared ancestor structure gives a C4 or C8 with exactly
3 back edges.

**Difficulty**: This requires showing that the back-edge graph (directed
graph on vertices, with edge from $v$ to $a$ for each back edge $(v,a)$)
contains a specific "triangle" pattern that yields a po2-length cycle when
unfolded through the tree structure.

**CHECK evidence** (exhaustive for CL-A/B/C; sampled for other cubics):
The CHECK below verifies that all (G,T) pairs with easy-path and leaf-pair
failing still have some po2 cycle with radius $\le 3$.

<!-- CHECK
# back_edge_triangle: verify radius <= 3 for all hard-path, leaf-pair-fail cubic instances.
# Tests: CL-A/B/C exhaustively; sampled cubics n=10,12 for residual cases.
# Exit 0 = all residual cases have radius <= 3 (chain_locality_r3 holds).
import itertools, random

rng = random.Random(20260730_2)

PO2_GAPS = {3, 7, 15, 31}
PO2_DIFFS = {2, 6, 14, 30}


def make_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    return adj


def connected_cubic(n, edges):
    deg = [0] * n
    for u, v in edges: deg[u] += 1; deg[v] += 1
    if min(deg) < 3 or max(deg) > 3: return False
    adj = make_adj(n, edges)
    seen = {0}; stack = [0]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); stack.append(w)
    return len(seen) == n


def sample_cubic(nn, rnd, tries=3000):
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
        if connected_cubic(nn, el): return el
    return None


def spanning_trees(n, edges, cap=20000):
    E = len(edges); trees = []
    for combo in itertools.combinations(range(E), n - 1):
        parent = list(range(n))
        def find(a):
            while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
            return a
        ok = True
        for ei in combo:
            ru, rv = find(edges[ei][0]), find(edges[ei][1])
            if ru == rv: ok = False; break
            parent[ru] = rv
        if ok:
            trees.append(sum(1 << ei for ei in combo))
            if len(trees) > cap: return None
    return trees


def tremaux_root(n, edges, tree_mask):
    adj_t = [[] for _ in range(n)]
    nontree_e = []
    for i, (u, v) in enumerate(edges):
        if tree_mask >> i & 1:
            adj_t[u].append(v); adj_t[v].append(u)
        else:
            nontree_e.append((u, v))
    for r in range(n):
        depth = [-1] * n; par = [-1] * n
        depth[r] = 0; stack = [r]
        while stack:
            u = stack.pop()
            for w in adj_t[u]:
                if depth[w] < 0 and w != par[u]:
                    depth[w] = depth[u] + 1; par[w] = u; stack.append(w)
        ok = True
        for u, v in nontree_e:
            a, b = (u, v) if depth[u] <= depth[v] else (v, u)
            if b < 0: ok = False; break
            x = b
            while depth[x] > depth[a]: x = par[x]
            if x != a: ok = False; break
        if ok: return r, depth, par
    return None, None, None


def get_info(n, edges, tree_mask, depth, par):
    nontree = []; children = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if tree_mask >> i & 1:
            if depth[u] > depth[v]: children[v].append(u)
            else: children[u].append(v)
        else:
            if depth[u] > depth[v]: nontree.append((u, v, depth[u] - depth[v]))
            else: nontree.append((v, u, depth[v] - depth[u]))
    return nontree, children


def po2_min_radius(n, edges, adj, nontree, cap=250000):
    eidx = {(min(u, v), max(u, v)): i for i, (u, v) in enumerate(edges)}
    nt = sum(1 << eidx[(min(u, v), max(u, v))] for u, v, _ in nontree)
    min_rad = None; steps = 0
    for L in [4, 8, 16]:
        if L > n: continue
        for s in range(n):
            stack = [(s, (s,), 1 << s)]
            while stack:
                u, path, vis = stack.pop(); steps += 1
                if steps > cap: return min_rad
                if len(path) == L:
                    if s in adj[u]:
                        m = 0; cyc = path + (s,)
                        for a, b in zip(cyc, cyc[1:]): m |= 1 << eidx[(min(a, b), max(a, b))]
                        r = bin(m & nt).count('1')
                        if min_rad is None or r < min_rad: min_rad = r
                        if min_rad == 0: return 0
                    continue
                for w in adj[u]:
                    if w > s and not (vis >> w & 1):
                        stack.append((w, path + (w,), vis | (1 << w)))
    return min_rad


def check_graph(name, n, edges, all_trees=True, sample_roots=0):
    edges = [tuple(sorted(e)) for e in edges]
    adj = make_adj(n, edges)
    if all_trees:
        trees = spanning_trees(n, edges)
        assert trees is not None, name + ": too many spanning trees"
    else:
        trees = None

    rnd = random.Random(rng.randrange(1 << 30))
    processed = set()

    def process_tree(tm):
        if tm in processed: return
        processed.add(tm)
        r0, depth, par = tremaux_root(n, edges, tm)
        if r0 is None: return
        nontree, children = get_info(n, edges, tm, depth, par)

        easy = any(g in PO2_GAPS for _, _, g in nontree)
        if easy: return

        leaves = [v for v in range(n) if not children[v]]
        lp_ok = False
        for L in leaves:
            lb = [(u, v, g) for u, v, g in nontree if u == L]
            if len(lb) < 2: continue
            for i in range(len(lb)):
                for j in range(i + 1, len(lb)):
                    d1, d2 = max(lb[i][2], lb[j][2]), min(lb[i][2], lb[j][2])
                    if d1 - d2 in PO2_DIFFS: lp_ok = True; break
                if lp_ok: break
        if lp_ok: return

        # Residual: must have radius <= 3
        mr = po2_min_radius(n, edges, adj, nontree)
        assert mr is not None and mr <= 3, (
            "back_edge_triangle: chain_locality_r3 FALSIFIED on residual: "
            "graph=" + name + " n=" + str(n) +
            " edges=" + repr(edges) + " root=" + str(r0) +
            " nontree=" + repr(nontree) + " min_rad=" + repr(mr))

    if trees is not None:
        for tm in trees:
            process_tree(tm)
    else:
        for _ in range(sample_roots):
            root = rnd.randrange(n)
            tm = 0
            adj2 = make_adj(n, edges)
            eidx2 = {(min(u, v), max(u, v)): i for i, (u, v) in enumerate(edges)}
            seen = [False] * n; seen[root] = True
            def nbrs(u): ns = adj2[u][:]; rnd.shuffle(ns); return ns
            stack = [(root, iter(nbrs(root)))]
            while stack:
                u, it = stack[-1]; adv = False
                for w in it:
                    if not seen[w]:
                        seen[w] = True
                        tm |= 1 << eidx2[(min(u, w), max(u, w))]
                        stack.append((w, iter(nbrs(w)))); adv = True; break
                if not adv: stack.pop()
            process_tree(tm)


# Exhaustive test of the 3 radius-2 falsifier cubic graphs (n=10, all spanning trees).
CL_A = [(3,8),(2,4),(3,4),(5,8),(1,5),(3,7),(1,8),(0,9),(4,6),(7,9),(2,9),(6,7),(0,2),(0,5),(1,6)]
CL_B = [(0,7),(3,4),(2,7),(5,8),(6,8),(0,9),(6,7),(0,2),(4,5),(3,9),(4,8),(1,6),(2,5),(1,3),(1,9)]
CL_C = [(0,1),(3,4),(2,7),(1,5),(0,3),(4,6),(5,7),(4,5),(8,9),(0,2),(3,6),(6,9),(1,9),(7,8),(2,8)]
for name, ed in [("CL_A", CL_A), ("CL_B", CL_B), ("CL_C", CL_C)]:
    check_graph(name, 10, ed, all_trees=True)

# Petersen graph (exhaustive, anchor).
pet = [(i, (i + 1) % 5) for i in range(5)]
pet += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
pet += [(i, i + 5) for i in range(5)]
check_graph("petersen", 10, pet, all_trees=True)

# Sampled cubic graphs at n=10,12 (100 DFS trees each).
for nn in [10, 12]:
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(6):
        edges = sample_cubic(nn, rnd)
        if edges is None: continue
        check_graph("cubic_n" + str(nn), nn, edges, all_trees=False, sample_roots=100)
CHECK -->

## Key structural question (open)

**Why does every residual cubic DFS tree have a 3-back-edge po2 cycle?**

From the CL-A analysis: in the 4 radius-3 trees, the po2 cycle arises
because two back edges share the same deeper endpoint (the double-sender
$v$), and a third back edge from a different vertex $w$ closes the cycle
through their common ancestor.

**Conjecture (double-sender lemma)**: In any cubic DFS tree, either:
(a) easy-path holds (some back edge has po2 gap), OR
(b) leaf-pair holds (some leaf's gap-difference is po2-minus-2), OR  
(c) some vertex $v$ carries 2 back edges to ancestors $a_1, a_2$, and
    some vertex $w$ (on the tree path from $a_2$ to $v$) carries a back
    edge to $a_1$, forming a C4 or C8 with back edges
    $\{(v,a_1),(v,a_2),(w,a_1)\}$ and tree path $a_1 \to^T w \to^T \cdots
    \to^T a_2$.

If (c) is true, the sym-diff $C_{(v,a_1)} \oplus C_{(v,a_2)} \oplus
C_{(w,a_1)}$ is a cycle of length $(\delta_v^{(1)} - \delta_v^{(2)}) + 2$
... wait, this doesn't directly give a po2 length. The actual length
depends on the tree-path structure.

**True mechanism**: The key is that the SYM-DIFF of 3 fundamental cycles
leaves a cycle of specific length. This length is po2 when the depth-gap
differences satisfy certain arithmetic conditions. The exact conditions
require a careful case analysis.

## Status

Construction verified: the C4 = sym-diff of 3 fundamental cycles is
proved for the specific CL-A radius-3 trees. General existence of a
3-back-edge po2 cycle in the residual (easy-fail, leaf-pair-fail) cases
is CHECK-verified but not analytically proved.
