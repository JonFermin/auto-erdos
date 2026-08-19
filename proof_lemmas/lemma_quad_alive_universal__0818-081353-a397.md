---
id: quad_alive_universal
status: open
depends_on: [triple_alive_universal]
discharged_by_round: null
introduced_at_round: 48
---

# Lemma `quad_alive_universal` (conjecture + probe: every triple-dead pair-residual tree fires via some quadruple)

**Setting.** $T$ a normal spanning tree of a connected cubic graph,
back edges $B_1, \dots, B_m$ with fundamental cycles $C_1, \dots,
C_m$. For a subset $S$ of back-edge indices write $C_S = \bigoplus_{i
\in S} C_i$. $T$ is **triple-dead** (R47 terminology) if no $C_S$ with
$|S| \le 3$ is a single cycle of power-of-2 length; the R47 falsifier
corpus shows triple-dead pair-residual trees exist ($n = 18$, five
distinct pinned/recorded examples — see
`lemma_triple_alive_universal` CHECK 3).

**Claim (open, universally quantified — sampling can only falsify).**
Every triple-dead pair-residual normal spanning tree of a connected
cubic graph has some 4-subset $S$ with $C_S$ a single cycle of
power-of-2 length.

**Why this is the successor universal.** Every simple cycle of $G$ is
$C_S$ for exactly one back-edge subset $S$ (cycle-space unique
representation over the normal tree), so the depth hierarchy
$\mathrm{depth}(T) = \min\{|S| : C_S$ a single PO2 cycle$\}$
interpolates between the dead depth-$\le 3$ certificate layer
(R23–R47) and the EGC statement itself ("$\mathrm{depth}(T) <
\infty$ for every $T$ of a min-degree-3 graph" restricted to cubic).
R47 established $\mathrm{depth} = 4$ is realized; this lemma asserts
depth $\le 4$ universally. If IT dies, the escalation question (is
depth unbounded?) takes over and the bounded-depth program is likely
hopeless.

**Designated falsifier executed SAME ROUND (standing policy).** Two
campaigns, both at $n = 18$ (the only scale where triple-dead states
are currently reachable):

1. R47 basin-constrained SA: 1.8M proposals across 3 warm starts from
   distinct falsifier trees. The class is *brittle* — only ~0.03% of
   double-edge-swap/re-root moves preserve triple-deadness — ~480
   class states visited, no quad-dead state, nquad (\#firing
   quadruples) never below 10.
2. R48 class-preserving beam search (targeted neighbors: swaps
   $\times$ fresh DFS, mass re-rootings, cubic growth moves $n \to
   n+2$ by double subdivision + join): $\ge$ 100k evaluations per
   seed, dozens of distinct class states, best_ever nquad = 10, zero
   falsifiers. Growth moves produced NO triple-dead states at $n =
   20$ so far — the class is unreached beyond $n = 18$; this is the
   open flank, not evidence.

**Census (R48).** 20,000 random DFS trees per falsifier GRAPH (all
five, including the two R46 graphs whose pinned trees have firing
triples): triple-dead-residual rates 0.035%–0.075% per graph; all 52
triple-dead trees found are quad-alive, **every one with nquad $\ge$
10 and minimum exactly 10 $= m$**. The sharper floor "nquad $\ge m$ on
triple-dead trees" is recorded as a census observation ONLY ($n = 18$
data; per standing policy it gets no lemma without its own falsifier
campaign at other $n$) — but it is provocative: participation counts
show every back edge lies in $\ge 2$ firing quadruples on all three
R47 pins, suggesting a structural supply mechanism rather than
coincidence.

**R49 falsifier campaign at $n = 20$ (the class reached beyond 18).**
The reachability flank closed at $n = 20$: 49 distinct triple-dead
pair-residual trees on 8 distinct cubic graphs, found by TWO
independent routes — (i) warm SA from the best growth child
(double-subdivision + join of edges 14, 18) of the R47 `ta_warm`
falsifier, after a census of all 351 growth children per pin ranked by
(residuality, viol3); (ii) cold SA from random cubic graphs at
$n = 20$ directly (2 hits, $\sim$714k iterations). Every state
verified by exhaustive cycle-space sweep (all $2^{11} - 1$ subsets).
Outcome: **zero quad-dead states — the lemma survives at a second
scale.** Depth spectrum uniform $\{8 \mapsto 4, 16 \mapsto 4\}$ on all
49, same as every $n = 18$ falsifier. nquad range 15–34, so **nquad
$\ge m = 11$ holds at $n = 20$** (census observation now at two
scales) — but two sharper $n = 18$ features die: the minimum is NOT
attained at $m$ (15 > 11), and the participation floor is gone —
most $n = 20$ states have a back edge in ZERO firing quadruples
(CHECK 3 pins one). Any analytic mechanism for quadruple supply must
therefore be global (counting the $\binom{m}{4}$ layer), not
per-back-edge. $n = 16$ remains unreached (cold SA, 1.7M iterations,
best energy 2 — one residual violation); whether the class is empty
below 18 is open.

**R50 falsifier campaign at $n = 24$ (fourth scale).** Second-
generation growth from the $n = 22$ state reached $n = 24$: 2 states
on 2 distinct graphs ($m = 13$), both quad-alive (nquad 20 and 33,
$\ge m$), both with depth spectrum $\{8 \mapsto 4, 16 \mapsto 4\}$,
exhaustively verified ($2^{13} - 1$ subsets); min participation 0
recurs at $n = 24$ (CHECK 3 pins it). Sampling caveats, recorded
deliberately: the $n = 22$ evidence is a SINGLE state (714k further
warm-SA iterations on its graph produced no second one), so the
$n = 22$ value nquad $= 41$ supports the FLOOR (nquad $\ge m$) but
no trend — the $n = 24$ minimum of 20 shows the apparent widening
10, 15, 41 was a one-sample artifact. Cold SA fails at $n = 22$
(best energy 2, 1.2M iterations) as at $n = 16$: cold reachability
is scale-spotty (works at 18, 20 only so far); the growth route is
the reliable ladder. Cumulative: nquad $\ge m$ at four scales
($10 \ge 10$, $15 \ge 11$, $41 \ge 12$, $20 \ge 13$), zero quad-dead
states ever observed.

<!-- CHECK
# quad_alive_universal CHECK 1 (deterministic anchor): the three R47
# pinned triple-dead trees each have >= 10 firing quadruples, with
# every back edge participating in >= 2 of them, and lengths in {8,16}.
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

PINS = [
    ('ta_falsifier_warm_n18', 18,
     [(0, 7), (0, 9), (0, 16), (1, 2), (1, 15), (1, 17), (2, 8), (2, 13),
      (3, 12), (3, 13), (3, 14), (4, 5), (4, 11), (4, 15), (5, 7), (5, 10),
      (6, 9), (6, 10), (6, 11), (7, 16), (8, 11), (8, 12), (9, 10),
      (12, 17), (13, 14), (14, 16), (15, 17)],
     17, [7, 17, 13, 12, 15, 4, 9, 16, 11, 10, 5, 6, 8, 3, 13, 1, 14, -1], 10),
    ('ta_falsifier_cold_n18', 18,
     [(0, 3), (0, 9), (0, 13), (1, 7), (1, 8), (1, 11), (2, 9), (2, 10),
      (2, 16), (3, 4), (3, 6), (4, 6), (4, 8), (5, 11), (5, 12), (5, 15),
      (6, 12), (7, 10), (7, 17), (8, 15), (9, 13), (10, 17), (11, 16),
      (12, 15), (13, 14), (14, 16), (14, 17)],
     10, [9, 7, 9, 0, 6, 15, 3, 17, 4, 13, -1, 1, 5, 14, 16, 8, 11, 10], 12),
    ('ta_falsifier_b2_n18', 18,
     [(0, 5), (0, 13), (0, 15), (1, 6), (1, 7), (1, 15), (2, 7), (2, 10),
      (2, 12), (3, 7), (3, 14), (3, 16), (4, 8), (4, 9), (4, 11), (5, 11),
      (5, 15), (6, 10), (6, 13), (8, 12), (8, 16), (9, 11), (9, 17),
      (10, 13), (12, 17), (14, 16), (14, 17)],
     14, [15, 7, 10, 16, 9, 11, 1, 3, 4, 17, 13, 4, 2, 6, -1, 5, 14, 12], 10),
]

for name, nn, edges, root, par, expect_nquad in PINS:
    edges = [tuple(sorted(e)) for e in edges]
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
        assert is_anc(a, b)
        es = set(); x = b
        while x != a:
            p = par[x]; es.add((min(x, p), max(x, p))); x = p
        es.add(e); fc.append(es)
    m = len(fc)
    assert m == 10
    quads = []
    for sub in combinations(range(m), 4):
        acc = set()
        for i in sub: acc ^= fc[i]
        L = single_cycle_len(acc)
        if L in PO2_LENS: quads.append((sub, L))
    assert len(quads) == expect_nquad, \
        f"{name}: nquad {len(quads)} != {expect_nquad}"
    assert all(L in {8, 16} for _, L in quads), f"{name}: unexpected length"
    part = [0] * m
    for sub, L in quads:
        for i in sub: part[i] += 1
    assert min(part) >= 2, f"{name}: back edge with < 2 firing quads: {part}"
    print(f"{name}: quad-alive, nquad={len(quads)}, min participation "
          f"{min(part)}, lengths {sorted(set(L for _, L in quads))}")
print("anchor OK: all three pinned triple-dead trees are quad-alive")
CHECK -->

<!-- CHECK
# quad_alive_universal CHECK 2 (falsification probe, fixed seed): every
# triple-dead pair-residual DFS tree sampled on the five falsifier
# graphs is quad-alive.  ~4000 DFS samples per graph keeps this under
# ~60s while remaining non-vacuous (expected ~10 class hits total).
import random
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

GRAPHS = [
    ('ta_warm', 18,
     [(0, 7), (0, 9), (0, 16), (1, 2), (1, 15), (1, 17), (2, 8), (2, 13),
      (3, 12), (3, 13), (3, 14), (4, 5), (4, 11), (4, 15), (5, 7), (5, 10),
      (6, 9), (6, 10), (6, 11), (7, 16), (8, 11), (8, 12), (9, 10),
      (12, 17), (13, 14), (14, 16), (15, 17)]),
    ('ta_cold', 18,
     [(0, 3), (0, 9), (0, 13), (1, 7), (1, 8), (1, 11), (2, 9), (2, 10),
      (2, 16), (3, 4), (3, 6), (4, 6), (4, 8), (5, 11), (5, 12), (5, 15),
      (6, 12), (7, 10), (7, 17), (8, 15), (9, 13), (10, 17), (11, 16),
      (12, 15), (13, 14), (14, 16), (14, 17)]),
    ('ta_b2', 18,
     [(0, 5), (0, 13), (0, 15), (1, 6), (1, 7), (1, 15), (2, 7), (2, 10),
      (2, 12), (3, 7), (3, 14), (3, 16), (4, 8), (4, 9), (4, 11), (5, 11),
      (5, 15), (6, 10), (6, 13), (8, 12), (8, 16), (9, 11), (9, 17),
      (10, 13), (12, 17), (14, 16), (14, 17)]),
    ('po2_falsifier_n18', 18,
     [(0, 4), (0, 7), (0, 9), (1, 2), (1, 15), (1, 17), (2, 8), (2, 13),
      (3, 12), (3, 13), (3, 14), (4, 11), (4, 15), (5, 6), (5, 7), (5, 16),
      (6, 9), (6, 10), (7, 16), (8, 11), (8, 12), (9, 10), (10, 11),
      (12, 17), (13, 14), (14, 16), (15, 17)]),
    ('sb_falsifier_n18', 18,
     [(0, 8), (0, 16), (0, 17), (1, 2), (1, 5), (1, 7), (2, 15), (2, 17),
      (3, 5), (3, 10), (3, 12), (4, 6), (4, 12), (4, 14), (5, 7), (6, 14),
      (6, 16), (7, 8), (8, 15), (9, 11), (9, 12), (9, 13), (10, 13),
      (10, 15), (11, 13), (11, 14), (16, 17)]),
]

rng = random.Random(20260818)
tdead_total = 0
for name, nn, edges in GRAPHS:
    edges = [tuple(sorted(e)) for e in edges]
    adj = [[] for _ in range(nn)]
    for u, v in edges: adj[u].append(v); adj[v].append(u)
    for _ in range(4000):
        r = rng.randrange(nn)
        sh = [list(adj[v]) for v in range(nn)]
        for v in range(nn): rng.shuffle(sh[v])
        depth = [-1] * nn; par = [-1] * nn
        depth[r] = 0; vis = [False] * nn; vis[r] = True
        stack = [(r, iter(sh[r]))]
        while stack:
            u, it = stack[-1]; adv = False
            for w in it:
                if not vis[w]:
                    vis[w] = True; depth[w] = depth[u] + 1; par[w] = u
                    stack.append((w, iter(sh[w]))); adv = True; break
            if not adv: stack.pop()
        tre = {(min(v, par[v]), max(v, par[v])) for v in range(nn) if v != r}
        fc = []
        for e in edges:
            if e in tre: continue
            u, v = e
            a, b = (u, v) if depth[u] <= depth[v] else (v, u)
            es = set(); x = b
            while x != a:
                p = par[x]; es.add((min(x, p), max(x, p))); x = p
            es.add(e); fc.append(es)
        m = len(fc)
        if any(len(c) in PO2_LENS for c in fc): continue
        dead3 = True
        for i in range(m):
            if not dead3: break
            for j in range(i + 1, m):
                if single_cycle_len(fc[i] ^ fc[j]) in PO2_LENS:
                    dead3 = False; break
        if not dead3: continue
        for x, y, z in combinations(range(m), 3):
            if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) in PO2_LENS:
                dead3 = False; break
        if not dead3: continue
        tdead_total += 1
        alive4 = False
        for sub in combinations(range(m), 4):
            acc = set()
            for i in sub: acc ^= fc[i]
            if single_cycle_len(acc) in PO2_LENS:
                alive4 = True; break
        assert alive4, \
            (f"FALSIFIED quad_alive_universal: triple-dead tree with no "
             f"firing quadruple (graph={name}, root={r}, par={par}, "
             f"edges={edges})")

assert tdead_total >= 5, f"only {tdead_total} triple-dead trees — probe vacuous"
print(f"probe OK: {tdead_total} triple-dead residual trees sampled across "
      f"5 graphs, all quad-alive")
CHECK -->

<!-- CHECK
# quad_alive_universal CHECK 3 (R49 deterministic anchor, n=20): three
# pinned triple-dead pair-residual trees at n=20 (m=11), from TWO
# independent routes (cold SA on random cubic + warm SA from a growth
# child of the R47 ta_warm falsifier).  Each is verified triple-dead
# from scratch (all subsets |S|<=3) and quad-alive with the exact
# pinned nquad / participation profile.  qa_warm15_n20 has a back edge
# in ZERO firing quadruples (min participation 0) — the n=18
# "every back edge in >= 2 firing quads" observation does NOT extend
# to n=20; the nquad >= m floor itself survives (15, 32, 34 >= 11).
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

PINS20 = [
    ('qa_cold_n20', 20,
     [(0, 3), (0, 8), (0, 11), (1, 6), (1, 8), (1, 19), (2, 8), (2, 13),
      (2, 18), (3, 7), (3, 10), (4, 6), (4, 11), (4, 12), (5, 13), (5, 16),
      (5, 19), (6, 19), (7, 15), (7, 17), (9, 10), (9, 14), (9, 18),
      (10, 18), (11, 12), (12, 15), (13, 16), (14, 16), (14, 17), (15, 17)],
     4, [8, 19, 18, 0, -1, 13, 1, 15, 1, 10, 3, 4, 11, 16, 17, 12, 14, 7, 9, 5],
     32, 5),
    ('qa_warm34_n20', 20,
     [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 18), (2, 4), (2, 6),
      (3, 15), (3, 18), (4, 8), (5, 10), (5, 19), (6, 13), (6, 15), (7, 9),
      (7, 12), (8, 14), (8, 16), (9, 10), (9, 15), (10, 17), (11, 12),
      (11, 17), (11, 19), (12, 14), (13, 16), (13, 19), (14, 16), (17, 18)],
     18, [4, 18, 6, 1, 2, 10, 15, 0, 14, 7, 9, 19, 11, 16, 12, 3, 8, 11, -1, 5],
     34, 8),
    ('qa_warm15_n20', 20,
     [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 12), (2, 4), (2, 5),
      (3, 17), (3, 18), (4, 8), (5, 13), (6, 10), (6, 15), (6, 17), (7, 9),
      (7, 12), (8, 14), (8, 16), (9, 10), (9, 14), (10, 17), (11, 13),
      (11, 18), (11, 19), (12, 15), (13, 16), (14, 16), (15, 19), (18, 19)],
     15, [7, 5, 4, 1, 0, 2, 17, 12, 16, 14, 9, 19, 15, 11, 8, -1, 13, 10, 3, 18],
     15, 0),
    ('qa_grow_n22', 22,
     [(0, 8), (0, 11), (0, 21), (1, 6), (1, 8), (1, 19), (2, 7), (2, 13),
      (2, 18), (3, 4), (3, 8), (3, 16), (4, 11), (4, 12), (5, 13), (5, 16),
      (5, 19), (6, 19), (6, 20), (7, 15), (7, 17), (9, 10), (9, 18),
      (9, 21), (10, 14), (10, 18), (11, 12), (12, 15), (13, 16), (14, 17),
      (14, 20), (15, 17), (20, 21)],
     15, [8, 6, 7, 16, 11, 13, 20, 17, 3, 21, 9, 0, 4, 2, 10, -1, 5, 15,
          10, 1, 14, 0],
     41, 7),
    ('qa_grow_n24', 24,
     [(0, 19), (0, 21), (0, 22), (1, 5), (1, 6), (1, 8), (2, 7), (2, 9),
      (2, 18), (3, 8), (3, 10), (3, 16), (4, 11), (4, 12), (4, 13), (5, 6),
      (5, 16), (6, 20), (7, 15), (7, 17), (8, 10), (9, 14), (9, 18),
      (10, 18), (11, 12), (11, 21), (12, 15), (13, 16), (13, 19), (14, 17),
      (14, 23), (15, 17), (19, 21), (20, 22), (20, 23), (22, 23)],
     15, [22, 5, 18, 8, 13, 16, 1, 15, 10, 14, 18, 12, 4, 19, 17, -1, 3, 7,
          9, 21, 6, 0, 23, 20],
     20, 0),
]

for name, nn, edges, root, par, expect_nquad, expect_minpart in PINS20:
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
        assert is_anc(a, b)   # normality of the tree
        es = set(); x = b
        while x != a:
            p = par[x]; es.add((min(x, p), max(x, p))); x = p
        es.add(e); fc.append(es)
    m = len(fc)
    assert m == nn // 2 + 1
    # triple-deadness from scratch: no PO2 single cycle at |S| <= 3
    for size in (1, 2, 3):
        for sub in combinations(range(m), size):
            acc = set()
            for i in sub: acc ^= fc[i]
            assert single_cycle_len(acc) not in PO2_LENS, \
                f"{name}: NOT triple-dead at |S|={size}, sub={sub}"
    quads = []
    for sub in combinations(range(m), 4):
        acc = set()
        for i in sub: acc ^= fc[i]
        L = single_cycle_len(acc)
        if L in PO2_LENS: quads.append((sub, L))
    assert len(quads) == expect_nquad, \
        f"{name}: nquad {len(quads)} != {expect_nquad}"
    assert all(L in {8, 16} for _, L in quads), f"{name}: unexpected length"
    assert len(quads) >= m, f"{name}: nquad below m"
    part = [0] * m
    for sub, L in quads:
        for i in sub: part[i] += 1
    assert min(part) == expect_minpart, \
        f"{name}: min participation {min(part)} != {expect_minpart}"
    print(f"{name}: triple-dead verified, quad-alive, nquad={len(quads)}, "
          f"min participation {min(part)}")
print("R49 anchor OK: class reached at n=20 by two routes; all quad-alive; "
      "nquad >= m holds; participation floor dies at n=20")
CHECK -->

## Summary

The depth-4 successor universal opened by R47's disproof of
`triple_alive_universal`: every triple-dead pair-residual normal
spanning tree of a connected cubic graph fires some 4-subset of back
edges (single PO2-cycle sym-diff). Evidence at introduction: ~530
distinct triple-dead states across two designated falsifier campaigns
(basin-constrained SA + class-preserving beam search) and a 100k-tree
DFS census over all five falsifier graphs — all quad-alive, all with
nquad $\ge 10 = m$ (minimum attained exactly, every back edge in
$\ge 2$ firing quadruples on the pins). R49 extended the evidence to
$n = 20$: 49 triple-dead states on 8 graphs from two independent
routes (warm growth + cold SA), all quad-alive with nquad $\ge 15 >
m = 11$, uniform depth spectrum $\{8 \mapsto 4, 16 \mapsto 4\}$ —
while the per-back-edge participation floor and the "minimum exactly
$m$" coincidence both died ($n = 20$ states with a quad-idle back
edge exist; CHECK 3). If the lemma dies at some scale, the
depth-escalation question (Q77) takes over; if it holds with the
observed $> m$ margin, a GLOBAL counting mechanism on the
$\binom{m}{4}$ layer (not per-back-edge supply) is the analytic
target.
