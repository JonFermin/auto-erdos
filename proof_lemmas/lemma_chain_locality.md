---
id: chain_locality
status: disproved
depends_on: []
discharged_by_round: 1
introduced_at_round: 1
---

# Lemma `chain_locality` (Q9 first lemma — pairwise chain-locality of power-of-2 cycles)

**Statement.** Let $G$ be a connected graph with minimum degree $\ge 3$ on
$n \le 12$ vertices, let $T$ be any DFS (Trémaux) tree of $G$ with any root
$r$. Then some simple cycle of $G$ whose length is a power of two contains
at most **2** non-tree edges; equivalently, some power-of-2 cycle is a
fundamental cycle of $T$ or the symmetric difference of two fundamental
cycles of $T$.

Scope note: for $n \le 12$ the only realizable power-of-2 lengths are 4
and 8 ($16 > 12$).

## Reformulation (proved) — the symdiff caveat dissolves

**Claim.** For a spanning tree $T$ of connected $G$ and a simple cycle $C$:
$C$ is a fundamental cycle or a symmetric difference of two fundamental
cycles that is a simple cycle **iff** $|C \setminus T| \le 2$.

**Proof.** Over $\mathrm{GF}(2)$, the fundamental cycles
$\{F(e) : e \in E \setminus T\}$ form a basis of the cycle space, and
$F(e)$ is the unique basis element containing the non-tree edge $e$.
Hence every simple cycle $C$ has the unique representation
$C = \bigtriangleup_{e \in C \setminus T} F(e)$: the right side is an
element of the cycle space whose set of non-tree edges is exactly
$C \setminus T$ (each $e \in C\setminus T$ appears in exactly one summand),
and cycle-space elements are determined by their coordinates in the basis.
If $|C \setminus T| = 1$, $C = F(e)$ is a fundamental cycle. If
$|C \setminus T| = 2$, $C = F(e_1) \bigtriangleup F(e_2)$ — and this
symmetric difference IS the simple cycle $C$ by construction, so no
separate edge-disjointness/nesting condition is needed. Conversely, a
fundamental cycle contains exactly 1 non-tree edge; and if
$F(e_1)\bigtriangleup F(e_2)$ is a simple cycle it contains exactly the
non-tree edges $e_1, e_2$. $\blacksquare$

This resolves the judge's caveat on Q9: quantifying over *simple
power-of-2 cycles $C$ with $|C\setminus T| \le 2$* is exactly the intended
"fundamental or symdiff-of-two" notion, with simplicity built in.

**Trémaux characterization used by the probe.** A spanning tree $T$ of a
connected graph $G$, rooted at $r$, is realizable as a DFS tree iff every
non-tree edge of $G$ joins an ancestor–descendant pair in $(T, r)$
(Trémaux trees; standard). The probe below therefore enumerates
*(spanning tree, root)* pairs and filters by the ancestor condition —
this covers **all** DFS trees, not a sample of adjacency orderings.

Sandbox-checkable core (arithmetic content of the forbidden-gap sets; graph
re-derivations are deferred to the CHECK block per the falsify-critic WARN
path): `all((d + 1) & d == 0 and d + 1 in (4, 8, 16, 32) for d in (3, 7, 15, 31))`

## Dual attack — falsification probe

The CHECK below is deterministic (seeded) and runs in ~4s:

- **Exhaustive over graphs AND DFS trees**: every labeled connected
  min-degree-3 graph on $n \in \{4,5\}$; named suite (K4, K5, K6,
  K33, K34, 3-/4-/5-prisms, Wagner V8, Möbius ladder ML10, Petersen,
  Petersen+chord, all six Z5 theta-lifts — the bipartite cubic
  10-vertex lift family from the Q8 round) — each with ALL spanning
  trees enumerated and ALL Trémaux (tree, root) pairs tested.
- **Sampled**: seeded random min-degree-3 graphs at $n = 7..12$
  (cubic-biased at 11–12), each against many random-order DFS trees.
- Self-tests: the cycle enumerator is checked against known counts
  (K4 has 3 C4s; the cube Q3 has 6 C4s and 6 C8s).
- Any (graph, tree, root) hit is a verified falsification of the lemma
  (soundness does not depend on coverage; coverage only strengthens a pass).

<!-- CHECK
# chain_locality falsification probe. Exit 0 = lemma survives these instances.
import itertools, random
from math import comb
rng = random.Random(20260724)

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

def cycle_masks(n, edges, L, cap=300000):
    eidx = {}
    for i, (u, v) in enumerate(edges):
        eidx[(u, v)] = i; eidx[(v, u)] = i
    adj = make_adj(n, edges)
    out = set(); steps = 0; complete = True
    for s in range(n):
        stack = [(s, (s,), 1 << s)]
        while stack:
            u, path, vis = stack.pop()
            steps += 1
            if steps > cap:
                complete = False; stack.clear(); break
            if len(path) == L:
                if s in adj[u]:
                    m = 0
                    cyc = path + (s,)
                    for a, b in zip(cyc, cyc[1:]):
                        m |= 1 << eidx[(a, b)]
                    out.add(m)
                continue
            for w in adj[u]:
                if w > s and not (vis >> w & 1):
                    stack.append((w, path + (w,), vis | 1 << w))
        if not complete: break
    return out, complete

def po2_masks(n, edges):
    masks = set(); complete = True
    for L in (4, 8):
        if L <= n:
            ms, comp = cycle_masks(n, edges, L)
            masks |= ms; complete = complete and comp
    return list(masks), complete

def spanning_tree_masks(n, edges, cap_comb=60000, cap_trees=9000):
    E = len(edges)
    if comb(E, n - 1) > cap_comb: return None
    trees = []
    for combo in itertools.combinations(range(E), n - 1):
        parent = list(range(n))
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            return a
        ok = True
        for ei in combo:
            ru, rv = find(edges[ei][0]), find(edges[ei][1])
            if ru == rv: ok = False; break
            parent[ru] = rv
        if ok:
            trees.append(sum(1 << ei for ei in combo))
            if len(trees) > cap_trees: return None
    return trees

def tremaux_root(n, edges, tree_mask):
    adj_t = [[] for _ in range(n)]
    nontree = []
    for i, (u, v) in enumerate(edges):
        if tree_mask >> i & 1:
            adj_t[u].append(v); adj_t[v].append(u)
        else:
            nontree.append((u, v))
    for r in range(n):
        depth = [-1] * n; par = [-1] * n
        depth[r] = 0; stack = [r]
        while stack:
            u = stack.pop()
            for w in adj_t[u]:
                if depth[w] < 0 and w != r:
                    depth[w] = depth[u] + 1; par[w] = u; stack.append(w)
        ok = True
        for u, v in nontree:
            a, b = (u, v) if depth[u] <= depth[v] else (v, u)
            x = b
            while depth[x] > depth[a]: x = par[x]
            if x != a: ok = False; break
        if ok: return r
    return None

def random_dfs_tree(n, edges, adj, eidx2, root, rnd):
    tm = 0
    seen = [False] * n; seen[root] = True
    def nbrs(u):
        ns = adj[u][:]; rnd.shuffle(ns); return ns
    stack = [(root, iter(nbrs(root)))]
    while stack:
        u, it = stack[-1]
        adv = False
        for w in it:
            if not seen[w]:
                seen[w] = True
                tm |= 1 << eidx2[(u, w)]
                stack.append((w, iter(nbrs(w))))
                adv = True
                break
        if not adv: stack.pop()
    return tm

def check_graph(name, n, edges, sampled_rounds=80):
    edges = [tuple(sorted(e)) for e in edges]
    assert connected_mindeg3(n, edges), name + ": test graph not connected min-deg-3"
    eidx2 = {}
    for i, (u, v) in enumerate(edges):
        eidx2[(u, v)] = i; eidx2[(v, u)] = i
    adj = make_adj(n, edges)
    po2, complete = po2_masks(n, edges)
    assert po2, name + ": NO C4/C8 at all in a min-deg-3 graph on <=12 vertices " \
        "- EG-relevant, inspect: edges=" + repr(edges)
    full = (1 << len(edges)) - 1
    trees = spanning_tree_masks(n, edges)
    if trees is not None:
        for tm in trees:
            nt = full & ~tm
            if any(bin(c & nt).count('1') <= 2 for c in po2):
                continue
            r = tremaux_root(n, edges, tm)
            if r is not None:
                assert complete, name + ": candidate failure but cycle enum capped"
                raise AssertionError(
                    "chain_locality FALSIFIED: graph=" + name + " n=" + str(n) +
                    " edges=" + repr(edges) + " tree_mask=" + str(tm) + " root=" + str(r))
        return
    rnd = random.Random(rng.randrange(1 << 30))
    for _ in range(sampled_rounds):
        root = rnd.randrange(n)
        tm = random_dfs_tree(n, edges, adj, eidx2, root, rnd)
        nt = full & ~tm
        if not any(bin(c & nt).count('1') <= 2 for c in po2):
            assert complete, name + ": candidate failure but cycle enum capped"
            raise AssertionError(
                "chain_locality FALSIFIED (sampled DFS): graph=" + name + " n=" + str(n) +
                " edges=" + repr(edges) + " tree_mask=" + str(tm) + " root=" + str(root))

def complete_graph(k):
    return k, [(i, j) for i in range(k) for j in range(i + 1, k)]

def complete_bip(a, b):
    return a + b, [(i, a + j) for i in range(a) for j in range(b)]

def prism(m):
    ed = [(i, (i + 1) % m) for i in range(m)]
    ed += [(m + i, m + (i + 1) % m) for i in range(m)]
    ed += [(i, m + i) for i in range(m)]
    return 2 * m, ed

def mobius(m):
    N = 2 * m
    ed = [(i, (i + 1) % N) for i in range(N)]
    ed += [(i, i + m) for i in range(m)]
    return N, ed

def petersen():
    ed = [(i, (i + 1) % 5) for i in range(5)]
    ed += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    ed += [(i, i + 5) for i in range(5)]
    return 10, ed

def theta_lift_z5(a2, a3):
    ed = [(i, 5 + i) for i in range(5)]
    ed += [(i, 5 + (i + a2) % 5) for i in range(5)]
    ed += [(i, 5 + (i + a3) % 5) for i in range(5)]
    return 10, ed

def sample_cubic(nn, rnd, extra=0):
    allpairs = [(i, j) for i in range(nn) for j in range(i + 1, nn)]
    for _ in range(4000):
        stubs = [v for v in range(nn) for _ in range(3)]
        if len(stubs) % 2 == 1:
            stubs.append(0)  # odd n: vertex 0 gets an extra stub (degree 4)
        rnd.shuffle(stubs)
        edges = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b or (min(a, b), max(a, b)) in edges: ok = False; break
            edges.add((min(a, b), max(a, b)))
        if not ok: continue
        edges = list(edges)
        if extra:
            rest = [e for e in allpairs if e not in set(edges)]
            edges += rnd.sample(rest, extra)
        if connected_mindeg3(nn, edges): return edges
    return None

# self-tests of the cycle enumerator against known counts
n, ed = complete_graph(4)
ms, _ = cycle_masks(n, [tuple(sorted(e)) for e in ed], 4)
assert len(ms) == 3, "self-test K4 C4 count"
n, ed = prism(4)
edt = [tuple(sorted(e)) for e in ed]
m4, _ = cycle_masks(n, edt, 4); m8, _ = cycle_masks(n, edt, 8)
assert len(m4) == 6 and len(m8) == 6, "self-test Q3 C4/C8 counts"

# exhaustive: ALL labeled connected min-deg-3 graphs on 4 and 5 vertices
for nn in (4, 5):
    allpairs = [(i, j) for i in range(nn) for j in range(i + 1, nn)]
    for r in range(len(allpairs) + 1):
        if r * 2 < 3 * nn: continue
        for sub in itertools.combinations(allpairs, r):
            if connected_mindeg3(nn, list(sub)):
                check_graph("exh_n" + str(nn), nn, list(sub))

named = [
    ("K4",) + complete_graph(4), ("K5",) + complete_graph(5), ("K6",) + complete_graph(6),
    ("K33",) + complete_bip(3, 3), ("K34",) + complete_bip(3, 4),
    ("prism3",) + prism(3), ("cubeQ3",) + prism(4), ("prism5_GP51",) + prism(5),
    ("wagnerV8",) + mobius(4), ("mobius10",) + mobius(5),
    ("petersen_GP52",) + petersen(),
]
for a2 in range(1, 5):
    for a3 in range(a2 + 1, 5):
        named.append(("thetaZ5_" + str(a2) + str(a3),) + theta_lift_z5(a2, a3))
n, ed = petersen()
named.append(("petersen_plus02", n, ed + [(0, 2)]))
for name, n, ed in named:
    check_graph(name, n, ed)

# seeded random min-deg-3 graphs, n = 7..10
for nn in (7, 8, 9, 10):
    got = 0; attempts = 0
    allpairs = [(i, j) for i in range(nn) for j in range(i + 1, nn)]
    while got < 10 and attempts < 4000:
        attempts += 1
        m = rng.randrange((3 * nn + 1) // 2, 2 * nn + 1)
        ed = rng.sample(allpairs, m)
        if not connected_mindeg3(nn, ed): continue
        check_graph("rand_n" + str(nn), nn, ed)
        got += 1
    assert got >= 5, "random generator starved at n=" + str(nn)

# seeded cubic-biased probes at the lemma boundary n = 11, 12
for nn in (11, 12):
    got = 0
    for i in range(8):
        extra = i % 3
        if nn % 2 == 1 and extra == 0:
            extra = 1  # odd n has no cubic graph; add an edge
        ed = sample_cubic(nn, rng, extra=extra)
        if ed is None: continue
        check_graph("cubicish_n" + str(nn), nn, ed, sampled_rounds=60)
        got += 1
    assert got >= 4, "cubic sampler starved at n=" + str(nn)
CHECK -->

## DISPROOF (2026-07-25, session s_0724-213346-43a1, round 1)

The offline extended sweep (same core algorithms as the CHECK plus
networkx iso-dedup; seed 20260724) **falsified the lemma**: 23 verified
(graph, DFS tree, root) instances in scope with NO power-of-2 cycle
carrying ≤ 2 non-tree edges — 22 instances across **three connected
cubic 10-vertex graphs** (found while exhaustively tree-checking all 19
cubic 10-vertex isomorphism classes) and 1 instance at n = 12.

The three falsifying cubic graphs (all 3-regular, n = 10):

- **CL-A** (girth 3, one C4, ten C8s), 4 bad (tree, root) pairs:
  edges `[(3,8),(2,4),(3,4),(5,8),(1,5),(3,7),(1,8),(0,9),(4,6),(7,9),(2,9),(6,7),(0,2),(0,5),(1,6)]`
- **CL-B** (girth 3, NO C4, twelve C8s), 6 bad pairs:
  edges `[(0,7),(3,4),(2,7),(5,8),(6,8),(0,9),(6,7),(0,2),(4,5),(3,9),(4,8),(1,6),(2,5),(1,3),(1,9)]`
- **CL-C** (girth 3, NO C4, nine C8s), 12 bad pairs:
  edges `[(0,1),(3,4),(2,7),(1,5),(0,3),(4,6),(5,7),(4,5),(8,9),(0,2),(3,6),(6,9),(1,9),(7,8),(2,8)]`

Canonical instance (CL-A): DFS tree rooted at **6** with tree edges
`[(3,8),(2,4),(3,4),(5,8),(1,5),(0,9),(7,9),(0,2),(1,6)]` — every C4
and C8 of CL-A carries ≥ 3 of the 6 back edges.

The n = 12 instance (degrees 3^10 4^2, two C4s, eighteen C8s): edges
`[(0,2),(7,10),(1,7),(0,3),(2,11),(5,6),(8,11),(1,8),(4,9),(3,6),(3,7),(10,11),(4,7),(0,4),(5,9),(1,10),(2,8),(2,5),(6,9)]`,
DFS tree rooted at **10** with tree edges
`[(0,2),(7,10),(1,7),(2,11),(5,6),(1,8),(4,9),(3,6),(0,4),(5,9),(2,8)]`.

**Independent verification**: every instance re-confirmed with disjoint
machinery — networkx `simple_cycles(length_bound=8)` for the po2 cycle
set, and an explicit DFS simulation (tree-edge-preferring traversal from
the recorded root) that reproduces the tree edge set exactly, proving
each tree is a genuine DFS tree, not merely spanning.

**The structural signal**: in ALL 23 instances the minimum over
power-of-2 cycles of the back-edge count is EXACTLY 3 — never 4 or
more. Radius-3 chain-locality (some po2 cycle with ≤ 3 non-tree edges)
survives every instance probed in scope; it is spun off as the revised
first lemma (`chain_locality_r3`). Falsifier profile: girth-3,
C4-free-or-poor, C8-rich cubic graphs — the C8s are long enough for a
deep DFS to spread every one of them across ≥ 3 back edges.

## Probe coverage record (final)

In-CHECK probe (retained below as audit trail; it PASSES because its
named suite happened to miss the three falsifying cubic classes —
coverage, not soundness, was the gap; it no longer runs now that the
lemma is `disproved`):
exhaustive labeled n=4,5; named suite with ALL Trémaux (tree, root)
pairs; seeded random n=7..12.

Offline extended sweep (seed 20260724, ~3 min): exhaustive iso-free
n=6 (19 classes / 1,858 labeled) and n=7 (150 classes / 236,926
labeled) with all Trémaux pairs per class — 0 failures; ALL 19,320
labeled connected cubic graphs on 8 vertices, exhaustive trees — 0
failures; all 19 connected cubic 10-vertex iso classes, exhaustive
trees — **22 failures in 3 classes**; seeded random min-deg-3 sweeps
n=8..11 (600/600/600/400 graphs) — 0 failures; n=12 (400 graphs) —
**1 failure**; out-of-scope reconnaissance n=13..16 — 7 more radius-2
failures (radius-3 status there not yet measured).

Secondary observation (DFS-ness relevance): on Petersen, two Z5 theta
lifts, and the Möbius ladder ML10, EVERY spanning tree — Trémaux or
not — carries a radius-2 po2 cycle (`popcount-bad-but-non-tremaux = 0`),
so the ancestral structure did no work on those graphs; on the CL
falsifiers it demonstrably does.

Honest coverage gap: exhaustive iso-free enumeration of NON-cubic
min-degree-3 graphs at n=8..12 is infeasible in this stdlib harness
(no geng); that regime was covered by seeded random sampling only.

## Why this lemma mattered for Q9 (discharging direction)

For a DFS tree, a fundamental cycle of back edge $e$ with depth-gap $d$
has length $d+1$, so a power-of-2 fundamental cycle exists iff some gap
lies in $\{3, 7, 15, 31, \dots\}$. Two-back-edge cycles tie pairs of
gaps arithmetically (e.g. two back edges from the same vertex with gaps
$d_1 < d_2$ span a cycle of length $d_2 - d_1 + 2$). A hypothetical EG
counterexample must therefore satisfy ALL radius-2 constraints
simultaneously: no gap in $\{3,7,15,\dots\}$ AND no realizable
2-back-edge power-of-2 cycle, for EVERY DFS tree. `chain_locality`
says these radius-2 constraints are already unsatisfiable on $\le 12$
vertices. The discharging program (Q9) seeks a charge argument turning
this local unsatisfiability into an all-$n$ statement; the failure mode
to watch is that radius-2 may be satisfiable at larger $n$ (see the
out-of-scope reconnaissance in the sweep).

## Post-mortem / revival condition

The lemma is dead as stated (radius 2, $n \le 12$). Revive ONLY as the
radius-3 statement — see `chain_locality_r3` — or as a quantitative
variant (e.g. "at most $f(n)$ of a graph's Trémaux (tree, root) pairs
are radius-2-bad"), for which the falsifiers give data points (CL-C:
12 bad pairs out of its full Trémaux family). Any discharging argument
built on "power-of-2 cycles are visible within two fundamental cycles"
is unsound from n = 10 upward; pairwise (radius-2) constraint
accounting alone cannot close Q9.
