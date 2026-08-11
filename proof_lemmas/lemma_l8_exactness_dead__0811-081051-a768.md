---
id: l8_exactness_dead
status: proved
depends_on: [triple_alive_universal, sup1_dead_tree]
discharged_by_round: 35
introduced_at_round: 35
---

# Lemma `l8_exactness_dead` (PROVED — counterexample): residual-tree firings are NOT always $L = 8$

**Statement.** There exists a cubic graph $G_1$ on 12 vertices and a
normal (Trémaux) spanning tree $T_1$ of $G_1$ such that:

1. $T_1$ is **pair-residual**: no fundamental cycle and no 2-subset
   symmetric difference is a single cycle of power-of-2 length;
2. some triple of back edges of $T_1$ fires at length **4**: its 3-way
   symmetric difference is a single cycle of length exactly 4;
3. six further triples fire at length 8 (so $T_1$ is triple-alive, and
   both lengths coexist on one tree).

**Consequence.** The R34 observation "every firing triple on a
pair-residual tree has $L = 8$ exactly" (176/176 trees, 571k-tree
census) is **FALSE** — it was a census-window artifact. The
`triple_alive_universal` target cannot be sharpened to "some triple
with $|D| + \operatorname{gap}_3 + 1 - 2k'' = 8$"; the honest universal
keeps the full power-of-2 disjunction $L \in \{4, 8, 16, 32\}$. This
reconciles with the older R18 census (738 firing triples on
crossing-failed residuals: $C_8$ 698x, $C_4$ 39x, $C_{16}$ 1x), which
had already seen non-8 firings under the earlier residual pipeline.

**Scale (R35 census, five seeds + smoke, 1,605,440 trees, 465
pair-residual, all triple-alive).** Firing-length histogram over all
3,268 firing triples: $L = 8$: 3,017 (92.3%); $L = 16$: 199 (6.1%);
$L = 4$: 52 (1.6%). Non-8 firings are real but rare, which is why four
R34 seeds missed them.

**What survives (R36 target, NOT claimed here).** Per-tree, the value
8 was always available: in the 295 residual trees with per-tree
tracking, the set of firing lengths was $\{8\}$ 225x, $\{4,8\}$ 31x,
$\{8,16\}$ 36x, $\{4,8,16\}$ 3x — **8 present in 295/295**. "Every
pair-residual tree has some $L = 8$ firing triple" (per-tree SUP-8) is
unfalsified and becomes its own probe lemma; this lemma only kills the
per-firing exactness.

**Remark (mechanism depth).** The fired 4-cycle
$(1,2),(2,10),(4,10),(1,4)$ is an ordinary 4-cycle of $G_1$, yet $T_1$
is pair-residual: the $C_4$ is invisible to every fundamental cycle and
every 2-subset symmetric difference, and is only recovered at triple
depth. Even *detecting* an existing power-of-2 cycle can genuinely
require the triple mechanism.

**The pinned object.** $G_1$ has edge list (12 vertices, 18 edges,
3-regular, connected):

```
(4,10) (1,2) (5,11) (0,10) (5,8) (3,7) (6,8) (2,10) (1,4) (0,6) (6,7)
(4,5) (8,9) (2,9) (1,7) (3,9) (0,11) (3,11)
```

$T_1$ is rooted at 10 with parent array (index = vertex):

```
par = [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0]
```

$T_1$ has 7 back edges; no fundamental cycle and no single-cycle pair
symmetric difference has power-of-2 length; exactly 7 firing triples
exist, one at $L = 4$ (the cycle above) and six at $L = 8$. Found by
randomized sweep (seed 99001) at $n = 12$; verified deterministically
below (no sampling — the CHECK re-derives the tree from the parent
array and exhausts all pairs and triples).

<!-- CHECK
# l8_exactness_dead CHECK (deterministic, exhaustive on the pin):
# the pinned 12-vertex tree is pair-residual, has exactly 7 firing
# triples with length histogram {4: 1, 8: 6}, and the L=4 triple
# fires the 4-cycle (1,2)-(2,10)-(4,10)-(1,4).
edges = [(4, 10), (1, 2), (5, 11), (0, 10), (5, 8), (3, 7), (6, 8), (2, 10),
         (1, 4), (0, 6), (6, 7), (4, 5), (8, 9), (2, 9), (1, 7), (3, 9),
         (0, 11), (3, 11)]
edges = [tuple(sorted(e)) for e in edges]
root = 10
nn = 12
par = [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0]
PO2_LENS = {4, 8, 16, 32}

deg = {}
for u, v in edges:
    deg[u] = deg.get(u, 0) + 1
    deg[v] = deg.get(v, 0) + 1
assert len(deg) == nn and all(deg[v] == 3 for v in deg), "not cubic"

depth = [-1] * nn
depth[root] = 0
pending = [v for v in range(nn) if v != root]
while pending:
    nxt = []
    for v in pending:
        if depth[par[v]] >= 0: depth[v] = depth[par[v]] + 1
        else: nxt.append(v)
    assert len(nxt) < len(pending)
    pending = nxt

def is_ancestor(u, v):
    if depth[u] > depth[v]: return False
    x = v
    while depth[x] > depth[u]: x = par[x]
    return x == u

tre = set()
for v in range(nn):
    if v != root:
        tre.add((min(v, par[v]), max(v, par[v])))
assert tre <= set(edges), "parent array uses a non-edge"
be = []
for e in edges:
    if e in tre: continue
    u, v = e
    a, b = (u, v) if depth[u] <= depth[v] else (v, u)
    assert is_ancestor(a, b), "non-ancestral back edge: tree not normal"
    be.append((b, a))
assert len(be) == 7, f"expected 7 back edges, got {len(be)}"

def fund_cycle_edges(sender, ancestor):
    path = set(); u = sender
    while u != ancestor:
        p = par[u]; path.add((min(u, p), max(u, p))); u = p
    path.add((min(sender, ancestor), max(sender, ancestor)))
    return path

def single_cycle_len(sym):
    if not sym: return None
    dg = {}
    for u, v in sym:
        dg[u] = dg.get(u, 0) + 1
        dg[v] = dg.get(v, 0) + 1
    if any(dg[x] != 2 for x in dg): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v)
        adjS.setdefault(v, []).append(u)
    start = sorted(dg)[0]; sn = {start}; st = [start]
    while st:
        u = st.pop()
        for w in adjS[u]:
            if w not in sn: sn.add(w); st.append(w)
    return len(sym) if len(sn) == len(dg) else None

fc = [fund_cycle_edges(s, a) for s, a in be]
m = len(fc)
for i in range(m):
    assert len(fc[i]) not in PO2_LENS, f"fund cycle {i} is po2"
for i in range(m):
    for j in range(i + 1, m):
        L = single_cycle_len(fc[i] ^ fc[j])
        assert L not in PO2_LENS, f"pair ({i},{j}) fires: not pair-residual"

hist = {}
l4_cycles = []
for x in range(m):
    for y in range(x + 1, m):
        for z in range(y + 1, m):
            sym = fc[x] ^ fc[y] ^ fc[z]
            L = single_cycle_len(sym)
            if L in PO2_LENS:
                hist[L] = hist.get(L, 0) + 1
                if L == 4: l4_cycles.append(sorted(sym))
assert hist == {4: 1, 8: 6}, f"expected {{4: 1, 8: 6}}, got {hist}"
assert l4_cycles == [[(1, 2), (1, 4), (2, 10), (4, 10)]], \
    f"unexpected L=4 cycle: {l4_cycles}"
print("pin OK: pair-residual 12-vertex tree fires {4: 1, 8: 6} -- "
      "L=8 exactness refuted, triple-aliveness confirmed")
CHECK -->

## Summary

Pinned counterexample killing the "all residual-tree firings are
$L = 8$" sharpening of `triple_alive_universal`: a 12-vertex cubic
graph with a pair-residual normal tree firing one triple at $L = 4$
(alongside six at $L = 8$). At scale (1.6M trees, 465 residuals) non-8
firings are 7.7% of all firings ($C_{16}$ 199, $C_4$ 52 of 3,268), so
the universal must keep the full power-of-2 disjunction. The per-tree
refinement "some $L = 8$ firing always exists" survived 295/295 and is
split off as its own probe (R36).
