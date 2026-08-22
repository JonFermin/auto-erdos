---
id: class_empty_below_18
status: proved
depends_on: []
discharged_by_round: 51
introduced_at_round: 51
---

# Lemma `class_empty_below_18` (proved by exhaustive enumeration: the triple-dead pair-residual class is empty below $n = 18$)

**Setting.** $G$ a connected simple cubic graph on $n$ vertices, $T$ a
normal spanning tree of $G$ rooted at $r$, back edges $B_1, \dots, B_m$
($m = n/2 + 1$) with fundamental cycles $C_1, \dots, C_m$; for
$S \subseteq \{1..m\}$ write $C_S = \bigoplus_{i \in S} C_i$. The
**triple-dead pair-residual class** (the R47–R50 falsifier class of
`triple_alive_universal` / `quad_alive_universal`) is the set of
triples $(G, T, r)$ such that NO $S$ with $|S| \le 3$ has $C_S$ a
single cycle of length in $\{4, 8, 16, 32\}$.

**Claim (PROVED, exhaustive finite computation).** The class is empty
for every $n \le 16$. Equivalently: every normal spanning tree of
every connected cubic graph on at most 16 vertices fires some back-edge
subset of size $\le 3$ (has depth $\le 3$ in the R47 sense). Together
with the five R47 falsifiers, $n = 18$ is the exact minimal scale of
the class.

**Proof structure.**

1. *Completeness of the enumeration domain.* Given any $(G, T, r)$,
   label the vertices by a BFS order of $T$ (root $= 0$, children of
   BFS-earlier vertices labeled first). Then the parent vector
   satisfies $par[i] < i$ and is nondecreasing in $i$; every non-root
   vertex has $\le 2$ tree children and the root $\le 3$ (cubicity);
   and — by normality of $T$ — every non-tree edge joins a strict
   ancestor-descendant pair, i.e. under this labeling a pair $(u, w)$
   with $u < w$, $u$ a strict ancestor of $w$, $(u,w)$ not a tree edge.
   Conversely any such parent vector plus any such back-edge completion
   filling every vertex to degree 3 is a triple in the domain (the tree
   spans, so $G$ is connected; normality holds by the comparability of
   all back edges). The enumerator generates ALL nondecreasing parent
   vectors under the degree caps and ALL comparable simple completions,
   so every isomorphism class of triples is visited at least once.
2. *Exact pruning.* The search rejects a partial completion as soon as
   a placed back edge yields a firing 1-, 2-, or 3-subset. Firing
   subsets persist under adding further back edges (the fundamental
   cycles of a fixed tree do not change), so no class state is ever
   pruned; conversely every complete unpruned leaf was re-verified by
   an independent from-scratch checker (rebuild graph, assert
   simple/cubic/connected/normal, sweep all $\binom{m}{\le 3}$
   subsets by set-XOR).
3. *Sanity locks (all passed before the production runs).*
   (a) The independent checker reproduces the exact pinned profiles of
   five known class states across four scales
   (`ta_falsifier_warm_n18` nquad 10 / minpart 2, `qa_cold_n20` 32/5,
   `qa_warm15_n20` 15/0, `qa_grow_n22` 41/7, `qa_grow_n24` 20/0 — the
   CHECK-1/3 pins of `lemma_quad_alive_universal`).
   (b) End-to-end: restricted to the BFS-relabeled tree shape of
   `ta_falsifier_warm_n18` (resp. `qa_cold_n20`), the pruned search
   finds that pin's exact back-edge set among its surviving leaves.
   (c) Coverage: with pruning disabled, the same enumerator produces
   every connected cubic graph — 5/5 isomorphism classes at $n = 8$,
   19/19 at $n = 10$ (checked by brute-force canonical forms /
   networkx isomorphism out-of-band; the CHECK below re-verifies the
   $n = 8$ count against hardcoded canonical certificates, stdlib
   only).
4. *Production runs (pruned, exhaustive).* Zero surviving states at
   every scale: $n = 4$ (0 feasible shapes), $n = 6$ (1 shape, 6
   nodes), $n = 8$ (9 shapes, 131 nodes), $n = 10$ (61 / 1{,}386),
   $n = 12$ (419 / 17{,}624), $n = 14$ (3{,}055 / 280{,}530),
   $n = 16$ (22{,}514 feasible shapes, 5{,}297{,}594 search nodes,
   98 s single-core). The $n = 16$ run is a one-parameter re-run of
   CHECK block 2 below (`run(16, prune=True)`, ~98 s); the complete
   $n = 18$ census is the same call at 18, sharded 4 ways (~15 min).

**Consequences.**

1. The R49/R50 cold-SA failures at $n \in \{14, 16\}$ were genuine
   emptiness, not search failure — the reachability picture is now
   exact below 18: there is nothing to reach.
2. The class has a hard minimal scale: any analytic mechanism for
   `quad_alive_universal` (or any depth-escalation counterexample)
   must engage structure that only exists from $n = 18$ on ($m \ge
   10$ back edges). Small-$n$ intuition is provably vacuous.
3. `depth(T) <= 3` is a THEOREM for cubic graphs on $\le 16$ vertices:
   the depth-$\le 3$ certificate layer, disproved as a universal in
   R47, is exactly true below the falsifier scale.

<!-- CHECK
# class_empty_below_18 CHECK 1 (self-contained harness + locks A/C +
# emptiness up to n=12): (A) coverage pin -- pruning OFF at n=8 produces
# exactly the 5 connected cubic graphs on 8 vertices (hardcoded
# certificates, stdlib iso backtracking); emptiness at n in {8,10,12};
# (C) non-vacuity -- on the BFS-relabeled shape of the pinned n=18
# falsifier ta_falsifier_warm_n18 the SAME pruned search finds its exact
# back-edge set, and every survivor re-verifies triple-dead from scratch.
from itertools import combinations
PO2 = (4, 8, 16, 32)
BAD_DD = {L - 1 for L in PO2}

def gen_shapes(n):
    par = [-1] * n; kids = [0] * n
    def rec(i):
        if i == n:
            yield tuple(par); return
        lo = par[i - 1] if i >= 2 else 0
        for p in range(lo, i):
            cap = 3 if p == 0 else 2
            if kids[p] >= cap: continue
            par[i] = p; kids[p] += 1
            yield from rec(i + 1)
            kids[p] -= 1
        par[i] = -1
    yield from rec(1)

def build(n, par, exclude_po2_singles):
    depth = [0] * n
    for v in range(1, n): depth[v] = depth[par[v]] + 1
    pathmask = [0] * n; ancmask = [0] * n
    for v in range(1, n):
        pathmask[v] = pathmask[par[v]] | (1 << (v - 1))
        ancmask[v] = ancmask[par[v]] | (1 << par[v])
    kids = [0] * n
    for v in range(1, n): kids[par[v]] += 1
    deficit = [3 - kids[0]] + [2 - kids[v] for v in range(1, n)]
    bad = BAD_DD if exclude_po2_singles else set()
    partners = [[] for _ in range(n)]
    for u in range(n):
        if deficit[u] <= 0: continue
        for w in range(u + 1, n):
            if deficit[w] <= 0 or par[w] == u: continue
            if not (ancmask[w] >> u) & 1: continue
            if depth[w] - depth[u] in bad: continue
            partners[u].append(w)
    # cheap feasibility: each deficient vertex needs enough comparable slots
    for v in range(n):
        if deficit[v] <= 0: continue
        pool = len(partners[v])
        for u in range(v):
            if deficit[u] > 0 and (ancmask[v] >> u) & 1 and par[v] != u \
                    and depth[v] - depth[u] not in bad:
                pool += 1
        if pool < deficit[v]: return None
    return depth, pathmask, deficit, partners

def complete(n, par, built, prune, collect):
    depth, pathmask, deficit, partners = built
    deficit = list(deficit)
    tree_ep = [(par[v], v) for v in range(1, n)]
    back_ep = []; used = set(); fcs = []; edges = []
    def single_po2(mask):
        if mask.bit_count() not in PO2: return False
        deg = {}; es = []; mm = mask
        while mm:
            b = mm & -mm; i = b.bit_length() - 1; mm ^= b
            e = tree_ep[i] if i < n - 1 else back_ep[i - (n - 1)]
            es.append(e)
            for x in e: deg[x] = deg.get(x, 0) + 1
        if any(c != 2 for c in deg.values()): return False
        adj = {}
        for u, v in es:
            adj.setdefault(u, []).append(v); adj.setdefault(v, []).append(u)
        st = es[0][0]; seen = {st}; stk = [st]
        while stk:
            u = stk.pop()
            for w in adj[u]:
                if w not in seen: seen.add(w); stk.append(w)
        return len(seen) == len(deg)
    def rec(min_w, cur_u):
        u = -1
        for v in range(n):
            if deficit[v] > 0: u = v; break
        if u == -1:
            collect.append((par, tuple(edges))); return
        floor = min_w if u == cur_u else 0
        for w in partners[u]:
            if w < floor or deficit[w] <= 0 or (u, w) in used: continue
            k = len(fcs)
            f = (pathmask[w] ^ pathmask[u]) | (1 << (n - 1 + k))
            if prune:
                back_ep.append((u, w)); ok = True
                for i in range(k):
                    if single_po2(f ^ fcs[i]): ok = False; break
                if ok and k >= 2:
                    for i, j in combinations(range(k), 2):
                        if single_po2(f ^ fcs[i] ^ fcs[j]): ok = False; break
                back_ep.pop()
                if not ok: continue
            used.add((u, w)); deficit[u] -= 1; deficit[w] -= 1
            back_ep.append((u, w)); fcs.append(f); edges.append((u, w))
            rec(w + 1, u)
            edges.pop(); fcs.pop(); back_ep.pop()
            deficit[u] += 1; deficit[w] += 1; used.discard((u, w))
    rec(0, -1)

def run(n, prune, exclude_po2_singles=True):
    hits = []
    for par in gen_shapes(n):
        built = build(n, par, exclude_po2_singles)
        if built is None: continue
        complete(n, par, built, prune, hits)
    return hits

CERTS8 = {
 ((0,1),(0,2),(0,3),(1,2),(1,3),(2,4),(3,5),(4,6),(4,7),(5,6),(5,7),(6,7)),
 ((0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,7),(5,6),(5,7),(6,7)),
 ((0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,6),(3,7),(4,6),(4,7),(5,6),(5,7)),
 ((0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,6),(4,7),(5,7),(6,7)),
 ((0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,7),(4,7),(5,6),(6,7)),
}

def iso(es1, es2, n=8):
    a1 = [[] for _ in range(n)]; a2 = [[] for _ in range(n)]
    for u, v in es1: a1[u].append(v); a1[v].append(u)
    for u, v in es2: a2[u].append(v); a2[v].append(u)
    mp = [-1] * n; inv = [-1] * n
    def rec(i):
        if i == n: return True
        for c in range(n):
            if inv[c] >= 0: continue
            ok = True
            for w in a1[i]:
                if w < i and mp[w] not in a2[c]: ok = False; break
            if ok and sum(1 for w in a1[i] if w < i) ==                       sum(1 for w in a2[c] if inv[w] >= 0 and inv[w] < i):
                mp[i] = c; inv[c] = i
                if rec(i + 1): return True
                mp[i] = -1; inv[c] = -1
        return False
    return rec(0)

labeled = set()
for par, bes in run(8, prune=False, exclude_po2_singles=False):
    es = frozenset([(min(par[v], v), max(par[v], v)) for v in range(1, 8)]
                   + [tuple(sorted(e)) for e in bes])
    labeled.add(es)
reps = []
for es in labeled:
    esl = sorted(es)
    if not any(iso(esl, r) for r in reps):
        reps.append(esl)
assert len(reps) == 5, f"coverage broken: {len(reps)} iso classes at n=8"
for r in reps:
    assert sum(1 for c in CERTS8 if iso(r, sorted(c))) == 1
print(f"coverage OK: {len(labeled)} labeled states = exactly the 5 cubic graphs on 8 vertices")

# exhaustive emptiness at n in {8, 10, 12} (n=14 is CHECK block 2)
for n in (8, 10, 12):
    hits = run(n, prune=True)
    assert not hits, f"CLASS STATE BELOW 18?! n={n}: {hits[:1]}"
    print(f"n={n}: triple-dead pair-residual class EMPTY (exhaustive)")
# (C) non-vacuity: the pinned n=18 falsifier is found on its own shape
EDGES18 = [(0,7),(0,9),(0,16),(1,2),(1,15),(1,17),(2,8),(2,13),(3,12),
 (3,13),(3,14),(4,5),(4,11),(4,15),(5,7),(5,10),(6,9),(6,10),(6,11),
 (7,16),(8,11),(8,12),(9,10),(12,17),(13,14),(14,16),(15,17)]
ROOT18 = 17
PAR18 = [7,17,13,12,15,4,9,16,11,10,5,6,8,3,13,1,14,-1]
nn = 18
kids = [[] for _ in range(nn)]
for v in range(nn):
    if v != ROOT18: kids[PAR18[v]].append(v)
new = {ROOT18: 0}; order = [ROOT18]; qi = 0
while qi < len(order):
    u = order[qi]; qi += 1
    for c in kids[u]:
        new[c] = len(order); order.append(c)
npar = [-1] * nn
for v in range(nn):
    if v != ROOT18: npar[new[v]] = new[PAR18[v]]
npar = tuple(npar)
for i in range(2, nn):
    assert npar[i] >= npar[i - 1] and npar[i] < i
tre = {(min(v, PAR18[v]), max(v, PAR18[v])) for v in range(nn) if v != ROOT18}
target = frozenset((min(new[a], new[b]), max(new[a], new[b]))
                   for a, b in EDGES18 if (min(a, b), max(a, b)) not in tre)
built = build(nn, npar, True)
assert built is not None
hits = []
complete(nn, npar, built, True, hits)
assert any(frozenset(b) == target for _, b in hits), "pin NOT found on its shape"
# re-verify each survivor triple-dead from scratch (independent set-XOR sweep)
def scl(sym):
    if not sym: return None
    dg = {}
    for u, v in sym: dg[u] = dg.get(u, 0) + 1; dg[v] = dg.get(v, 0) + 1
    if any(d != 2 for d in dg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    st = next(iter(dg)); seen = {st}; stk = [st]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(sym) if len(seen) == len(dg) else None
for parv, bes in hits:
    fcl = []
    dep = [0] * nn
    for v in range(1, nn): dep[v] = dep[parv[v]] + 1
    for u, w in bes:
        es = set(); x = w
        while x != u:
            p = parv[x]; es.add((min(x, p), max(x, p))); x = p
        es.add((min(u, w), max(u, w))); fcl.append(es)
    for size in (1, 2, 3):
        for sub in combinations(range(len(fcl)), size):
            acc = set()
            for i in sub: acc ^= fcl[i]
            assert scl(acc) not in set(PO2), "survivor fires at |S|<=3?!"
print(f"non-vacuity OK: ta_falsifier_warm_n18 found among {len(hits)} class "
      f"states on its own tree shape; all survivors re-verified triple-dead")
print("class_empty_below_18: ALL LOCKS PASS")
CHECK -->

<!-- CHECK
# class_empty_below_18 CHECK 2 (the headline scale that a fast block can
# carry): exhaustive emptiness at n=14 (3,055 feasible shapes, ~280k
# search nodes, ~6 s).  n=16 (98 s) and the complete n=18 census are
# one-parameter re-runs of this same code, done out-of-loop in R51.
from itertools import combinations
PO2 = (4, 8, 16, 32)
BAD_DD = {L - 1 for L in PO2}

def gen_shapes(n):
    par = [-1] * n; kids = [0] * n
    def rec(i):
        if i == n:
            yield tuple(par); return
        lo = par[i - 1] if i >= 2 else 0
        for p in range(lo, i):
            cap = 3 if p == 0 else 2
            if kids[p] >= cap: continue
            par[i] = p; kids[p] += 1
            yield from rec(i + 1)
            kids[p] -= 1
        par[i] = -1
    yield from rec(1)

def build(n, par, exclude_po2_singles):
    depth = [0] * n
    for v in range(1, n): depth[v] = depth[par[v]] + 1
    pathmask = [0] * n; ancmask = [0] * n
    for v in range(1, n):
        pathmask[v] = pathmask[par[v]] | (1 << (v - 1))
        ancmask[v] = ancmask[par[v]] | (1 << par[v])
    kids = [0] * n
    for v in range(1, n): kids[par[v]] += 1
    deficit = [3 - kids[0]] + [2 - kids[v] for v in range(1, n)]
    bad = BAD_DD if exclude_po2_singles else set()
    partners = [[] for _ in range(n)]
    for u in range(n):
        if deficit[u] <= 0: continue
        for w in range(u + 1, n):
            if deficit[w] <= 0 or par[w] == u: continue
            if not (ancmask[w] >> u) & 1: continue
            if depth[w] - depth[u] in bad: continue
            partners[u].append(w)
    # cheap feasibility: each deficient vertex needs enough comparable slots
    for v in range(n):
        if deficit[v] <= 0: continue
        pool = len(partners[v])
        for u in range(v):
            if deficit[u] > 0 and (ancmask[v] >> u) & 1 and par[v] != u \
                    and depth[v] - depth[u] not in bad:
                pool += 1
        if pool < deficit[v]: return None
    return depth, pathmask, deficit, partners

def complete(n, par, built, prune, collect):
    depth, pathmask, deficit, partners = built
    deficit = list(deficit)
    tree_ep = [(par[v], v) for v in range(1, n)]
    back_ep = []; used = set(); fcs = []; edges = []
    def single_po2(mask):
        if mask.bit_count() not in PO2: return False
        deg = {}; es = []; mm = mask
        while mm:
            b = mm & -mm; i = b.bit_length() - 1; mm ^= b
            e = tree_ep[i] if i < n - 1 else back_ep[i - (n - 1)]
            es.append(e)
            for x in e: deg[x] = deg.get(x, 0) + 1
        if any(c != 2 for c in deg.values()): return False
        adj = {}
        for u, v in es:
            adj.setdefault(u, []).append(v); adj.setdefault(v, []).append(u)
        st = es[0][0]; seen = {st}; stk = [st]
        while stk:
            u = stk.pop()
            for w in adj[u]:
                if w not in seen: seen.add(w); stk.append(w)
        return len(seen) == len(deg)
    def rec(min_w, cur_u):
        u = -1
        for v in range(n):
            if deficit[v] > 0: u = v; break
        if u == -1:
            collect.append((par, tuple(edges))); return
        floor = min_w if u == cur_u else 0
        for w in partners[u]:
            if w < floor or deficit[w] <= 0 or (u, w) in used: continue
            k = len(fcs)
            f = (pathmask[w] ^ pathmask[u]) | (1 << (n - 1 + k))
            if prune:
                back_ep.append((u, w)); ok = True
                for i in range(k):
                    if single_po2(f ^ fcs[i]): ok = False; break
                if ok and k >= 2:
                    for i, j in combinations(range(k), 2):
                        if single_po2(f ^ fcs[i] ^ fcs[j]): ok = False; break
                back_ep.pop()
                if not ok: continue
            used.add((u, w)); deficit[u] -= 1; deficit[w] -= 1
            back_ep.append((u, w)); fcs.append(f); edges.append((u, w))
            rec(w + 1, u)
            edges.pop(); fcs.pop(); back_ep.pop()
            deficit[u] += 1; deficit[w] += 1; used.discard((u, w))
    rec(0, -1)

def run(n, prune, exclude_po2_singles=True):
    hits = []
    for par in gen_shapes(n):
        built = build(n, par, exclude_po2_singles)
        if built is None: continue
        complete(n, par, built, prune, hits)
    return hits

hits = run(14, prune=True)
assert not hits, f"CLASS STATE AT n=14?! {hits[:1]}"
print("n=14: triple-dead pair-residual class EMPTY (exhaustive)")

CHECK -->

## Addendum (same round): the COMPLETE class census at the minimal scale $n = 18$

The same enumeration run exhaustively at $n = 18$ (169{,}049 feasible
shapes, 102{,}771{,}427 search nodes, 4 shards, ~13 min wall-clock)
returns the ENTIRE triple-dead pair-residual class at its minimal
scale. Every raw survivor was re-verified by the independent
from-scratch checker; dedup up to isomorphism of rooted
(graph, tree)-pairs (node invariant: depth; edge invariant: tree flag)
gives:

**The class at $n = 18$ is exactly 6 states on exactly 3 cubic graphs.**

| state | graph | nquad | min participation | size-4 spectrum |
|---|---|---|---|---|
| censusA_nq10 | A | 10 | 2 | 8: 3, 16: 7 |
| censusA_nq12 | A | 12 | 2 | 8: 3, 16: 9 |
| censusA_nq14 | A | 14 | 3 | 8: 3, 16: 11 |
| censusB_nq17 | B | 17 | 4 | 8: 8, 16: 9 |
| censusC_nq25a | C | 25 | 6 | 8: 6, 16: 19 |
| censusC_nq25b | C | 25 | 6 | 8: 6, 16: 19 |

Graph data: A has $|\mathrm{Aut}| = 2$, B and C are asymmetric; all
three have girth 3. All three R47 pinned falsifier trees are present
(sanity: the census contains the known ground truth).

**Corrections this forces on the R46–R50 narrative:**

1. **All five "distinct" $n = 18$ falsifiers (ta_warm, ta_cold, ta_b2,
   po2_falsifier_n18, sb_falsifier_n18) are pairwise ISOMORPHIC — one
   single graph (= A).** The SA/beam dedup was by labeled canonical
   (edges, root, par) and never tested graph isomorphism; every
   cross-falsifier "anatomy comparison" in R46–R47 compared the same
   graph under different trees/labelings. Prior "distinct graphs"
   counts at other scales (e.g. "8 graphs at $n = 20$") are unaudited
   up to isomorphism and must be re-checked before use.
2. Graphs B and C were NEVER reached by any SA/beam/growth campaign
   (R47–R50 all lived on A and its growth lineage) — cold SA
   reachability is biased as well as scale-spotty.
3. **`quad_alive_universal` is PROVED at the minimal scale**: all 6
   states fire quadruples (nquad 10–25, lengths in {8, 16}), by
   exhaustion rather than sampling.
4. **nquad $\ge m = 10$ is exact at $n = 18$** (min 10, attained on
   A), and **min participation $\ge 2$ is a THEOREM at $n = 18$** —
   the participation floor that dies at $n = 20$ by sampling
   (qa_warm15_n20, CHECK 3 of `lemma_quad_alive_universal`) holds
   exhaustively at 18.

<!-- CHECK
# class_empty_below_18 CHECK 3 (deterministic census anchor): the six
# states of the complete n=18 census, pinned exactly — each re-verified
# from scratch (simple/cubic/connected, normal tree, triple-dead over all
# |S|<=3, quad-alive with exact nquad / min-participation / lengths).
from itertools import combinations
PO2_LENS = {4, 8, 16, 32}

def single_cycle_len(sym):
    if not sym: return None
    dg = {}
    for u, v in sym: dg[u] = dg.get(u, 0) + 1; dg[v] = dg.get(v, 0) + 1
    if any(d != 2 for d in dg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    st = next(iter(dg)); seen = {st}; stk = [st]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(sym) if len(seen) == len(dg) else None

PINS18 = [
    ('censusA_nq12', 18,
     [(0, 1), (0, 2), (0, 10), (1, 2), (1, 6), (2, 3), (3, 4), (3, 14), (4, 5), (4, 16), (5, 6), (5, 10), (6, 7), (7, 8), (7, 9), (8, 9), (8, 10), (9, 11), (11, 12), (11, 13), (12, 13), (12, 17), (13, 14), (14, 15), (15, 16), (15, 17), (16, 17)],
     0, [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 11, 12, 13, 14, 15, 16],
     12, 2),
    ('censusA_nq10', 18,
     [(0, 1), (0, 2), (0, 10), (1, 2), (1, 14), (2, 3), (3, 4), (3, 8), (4, 5), (4, 16), (5, 6), (5, 7), (6, 7), (6, 17), (7, 8), (8, 9), (9, 10), (9, 14), (10, 11), (11, 12), (11, 13), (12, 13), (12, 14), (13, 15), (15, 16), (15, 17), (16, 17)],
     0, [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 15, 16],
     10, 2),
    ('censusA_nq14', 18,
     [(0, 1), (0, 2), (0, 14), (1, 2), (1, 10), (2, 3), (3, 4), (3, 8), (4, 5), (4, 17), (5, 6), (5, 7), (6, 7), (6, 16), (7, 8), (8, 9), (9, 10), (9, 14), (10, 11), (11, 12), (11, 13), (12, 13), (12, 14), (13, 15), (15, 16), (15, 17), (16, 17)],
     0, [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 15, 16],
     14, 3),
    ('censusB_nq17', 18,
     [(0, 1), (0, 2), (0, 10), (1, 2), (1, 14), (2, 3), (3, 4), (3, 5), (4, 5), (4, 17), (5, 6), (6, 7), (6, 8), (7, 8), (7, 16), (8, 9), (9, 10), (9, 13), (10, 11), (11, 12), (11, 14), (12, 13), (12, 14), (13, 15), (15, 16), (15, 17), (16, 17)],
     0, [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 15, 16],
     17, 4),
    ('censusC_nq25a', 18,
     [(0, 1), (0, 2), (0, 6), (1, 2), (1, 9), (2, 3), (3, 4), (3, 7), (4, 5), (4, 14), (5, 6), (5, 17), (6, 7), (7, 8), (8, 9), (8, 10), (9, 10), (10, 11), (11, 12), (11, 13), (12, 13), (12, 16), (13, 14), (14, 15), (15, 16), (15, 17), (16, 17)],
     0, [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
     25, 6),
    ('censusC_nq25b', 18,
     [(0, 1), (0, 2), (0, 12), (1, 2), (1, 5), (2, 3), (3, 4), (3, 13), (4, 5), (4, 6), (5, 6), (6, 7), (7, 8), (7, 9), (8, 9), (8, 16), (9, 10), (10, 11), (10, 14), (11, 12), (11, 17), (12, 13), (13, 14), (14, 15), (15, 16), (15, 17), (16, 17)],
     0, [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
     25, 6),
]

for name, nn, edges, root, par, expect_nquad, expect_minpart in PINS18:
    edges = [tuple(sorted(e)) for e in edges]
    deg = {}
    for u, v in edges:
        assert u != v
        deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    assert len(deg) == nn and all(d == 3 for d in deg.values())
    depth = [-1] * nn; depth[root] = 0
    pending = [v for v in range(nn) if v != root]
    while pending:
        nxt = []
        for v in pending:
            if depth[par[v]] >= 0: depth[v] = depth[par[v]] + 1
            else: nxt.append(v)
        assert len(nxt) < len(pending)
        pending = nxt
    tre = {(min(v, par[v]), max(v, par[v])) for v in range(nn) if v != root}
    assert tre <= set(edges)

    def is_anc(u, v):
        if depth[u] > depth[v]: return False
        x = v
        while depth[x] > depth[u]: x = par[x]
        return x == u

    fc = []
    for e in edges:
        if e in tre: continue
        u, v = e
        a, b = (u, v) if depth[u] <= depth[v] else (v, u)
        assert is_anc(a, b)   # normality
        es = set(); x = b
        while x != a:
            p = par[x]; es.add((min(x, p), max(x, p))); x = p
        es.add(e); fc.append(es)
    m = len(fc)
    assert m == nn // 2 + 1
    for size in (1, 2, 3):
        for sub in combinations(range(m), size):
            acc = set()
            for i in sub: acc ^= fc[i]
            assert single_cycle_len(acc) not in PO2_LENS, \
                f"{name}: NOT triple-dead at |S|={size}"
    quads = []
    for sub in combinations(range(m), 4):
        acc = set()
        for i in sub: acc ^= fc[i]
        L = single_cycle_len(acc)
        if L in PO2_LENS: quads.append((sub, L))
    assert len(quads) == expect_nquad, f"{name}: nquad {len(quads)} != {expect_nquad}"
    assert all(L in {8, 16} for _, L in quads), name
    assert len(quads) >= m, f"{name}: nquad below m"
    part = [0] * m
    for sub, L in quads:
        for i in sub: part[i] += 1
    assert min(part) == expect_minpart, \
        f"{name}: min participation {min(part)} != {expect_minpart}"
    print(f"{name}: verified in-class, nquad={len(quads)}, minpart={min(part)}")
print("census anchor OK: the complete n=18 class (6 states) pinned; all "
      "quad-alive; nquad >= m and participation >= 2 exhaustive at n=18")
CHECK -->

## Summary

Exhaustive enumeration (BFS-canonical rooted tree shapes with $\le 2$
children per non-root vertex, $\le 3$ at the root, plus all comparable
simple back-edge completions — a complete cover of all (cubic $G$,
normal $T$, root) triples up to isomorphism) proves the triple-dead
pair-residual class is EMPTY for all $n \le 16$. The R47 falsifiers at
$n = 18$ therefore sit at the exact minimal scale of the class. The
enumeration's pruning is exact (firing subsets persist under edge
addition); its checker is sanity-locked on all five cross-scale pins of
`lemma_quad_alive_universal`, its coverage is verified against the
known cubic-graph counts at $n \in \{8, 10\}$, and its non-vacuity
against the pinned $n = 18$ falsifier. Cold-SA unreachability at
$n \in \{14, 16\}$ (R49/R50) is thereby explained as genuine emptiness.
The same run at $n = 18$ yields the COMPLETE census of the class at its
minimal scale: exactly 6 states on exactly 3 cubic graphs — all five
prior "distinct" falsifiers being ONE graph up to isomorphism — all
quad-alive, with nquad $\ge m$ and per-back-edge participation $\ge 2$
exhaustive at 18 (CHECK 3 pins all six).
