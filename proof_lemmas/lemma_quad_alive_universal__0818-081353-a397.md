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

**R51 — PROVED AT THE MINIMAL SCALE (exhaustive census; see
`lemma_class_empty_below_18`).** A complete enumeration of all (cubic
graph, normal spanning tree, root) triples proves the class is EMPTY
for all $n \le 16$ and computes the ENTIRE class at $n = 18$: exactly
**6 states on exactly 3 cubic graphs** (up to isomorphism), every one
quad-alive — so the lemma holds at its minimal scale by exhaustion, not
sampling. Exhaustive facts at $n = 18$: nquad $\in \{10, 12, 14, 17,
25\}$ (so nquad $\ge m = 10$ is a theorem at 18, minimum attained);
min participation $\ge 2$ is a theorem at 18 (it still dies at
$n = 20$ per CHECK 3's `qa_warm15_n20`); every firing quadruple has
length in $\{8, 16\}$. Two corrections to the earlier evidence
narrative: (i) the five "distinct" $n = 18$ falsifier graphs used in
CHECK 2 and all R46–R48 campaigns are pairwise ISOMORPHIC — one graph
(labeled dedup never tested graph isomorphism); (ii) two of the three
carrier graphs at $n = 18$ were never reached by any SA/beam/growth
campaign. Sampled-evidence claims of "distinct graphs" at $n \ge 20$
are unaudited up to isomorphism and pending an R52 re-check.

**R52 — iso-audit of the $n \ge 20$ pinned corpus (CHECK 4).** The
three pinned $n = 20$ states sit on THREE pairwise non-isomorphic
cubic graphs — proved by triangle counts alone (5, 3, 4 for
`qa_cold_n20`, `qa_warm34_n20`, `qa_warm15_n20`; a graph invariant),
with $|\mathrm{Aut}| = 2, 1, 2$ pinned as well. So unlike $n = 18$
(where five "distinct" falsifiers collapsed to one graph), the
$n = 20$ pinned evidence is genuinely graph-diverse: at least 3 of
R49's claimed "8 distinct graphs" are real. Second finding: the
growth "ladder" is NOT graph-descent. None of the three $n = 20$
pinned graphs is a double-subdivision+join child of census graph A;
`qa_grow_n22`'s graph is not a growth child of any pinned $n = 20$
graph; `qa_grow_n24`'s graph is not a growth child of
`qa_grow_n22`'s (networkx audit over all $\binom{|E|}{2}$ growth
children, out-of-band). The R49/R50 route "grow then warm-SA" mutates
the carrier graph by double-edge-swaps before the class is
re-entered, so lineage claims are search-route provenance only — any
structural induction on $n$ via class-preserving growth moves has NO
empirical instance on record.

**R53 — the COMPLETE census at $n = 20$ (exhaustive; CHECK 5 pins all
of it).** The validated R52 harness run exhaustively at $n = 20$
(32,652,735 tree shapes, 1,289,003 feasible, 1,806,659,655 search
nodes, 4 shards, $\sim$85 min wall): 67 raw labeled survivors,
deduping to **42 states on 10 cubic graphs**. Ground truth: all three
R49 pins are contained (state-level iso). Headlines:

1. **The lemma is PROVED at the second scale by exhaustion**: all 42
   states are quad-alive; every firing quadruple has length in
   $\{8, 16\}$ (both facts now exhaustive at $n \in \{18, 20\}$).
2. **The nquad $\ge m$ floor is DEAD**: min nquad over the class is
   **9 $< m = 11$**, attained by two tree-states on ONE graph with
   $|\mathrm{Aut}| = 10$ and 5 triangles — the highest-symmetry
   carrier in the census, never reached by any SA/beam campaign
   (SA-sampled nquad range was 15–34; exhaustion reaches 9). The
   "nquad $\ge m$ at four scales" observation was a reachability
   artifact, like the participation floor before it. The two
   exhaustive scales give min-nquad $10 = m$ (at 18) and $9 = m - 2$
   (at 20): the true floor DECREASES both absolutely and relative to
   $m$; whether it reaches 0 at some scale (= a quad-dead state =
   depth-5 discovery) is now THE quantitative frontier.
3. **Participation floor**: 29/42 states have a back edge in ZERO
   firing quadruples ($n = 18$: 0/6). minpart $= 0$ is the NORM at
   20, not the exception.
4. **Carrier-graph anatomy**: state counts per graph
   23/5/5/3/1/1/1/1/1/1 (one dominant carrier, $|\mathrm{Aut}| = 2$,
   4 triangles, 23 tree-states); triangle counts span 2–6, so the
   $n = 18$ "girth 3, several triangles" pattern loosens (a
   2-triangle carrier exists); $|\mathrm{Aut}|$ multiset
   $\{10, 8, 4, 2, 2, 2, 1, 1, 1, 1\}$ — high symmetry appears
   exactly where min-nquad drops.
5. **Growth lineage (networkx, out-of-band)**: exactly ONE of the 10
   carrier graphs is a double-subdivision+join child of an $n = 18$
   census graph (of B — the first recorded graph-level descent
   instance between class carriers); the dominant carrier and the
   min-nquad carrier descend from none of A/B/C.

**R54 — targeted hunt at $n \in \{22, 24\}$ (fixed-graph sweeps;
CHECK 6).** A canonical-DFS fixed-graph enumerator (each (root, normal
tree) pair visited exactly once — sibling subtrees of a normal tree
have no cross edges, so increasing-label child order realizes every
tree; validated by exact reproduction of the A/B/C classes at $n = 18$
and the |Aut|=10-carrier class at $n = 20$) swept: the two known
$n \ge 22$ carriers COMPLETELY, all 363 unique double-subdivision+join
children of the four most significant $n = 20$ carriers (min-nquad
G1, |Aut|=8 G9, dominant G0, B-descendant G3), all 10 cubic
circulants $C_{22}(s, 11)$, all $GP(11, k)$, and the 6-triangle-ring
family at $n = 24$ (the $k = 6$ analog of G1's pentagonal-ring
structure). Results:

1. **No quad-dead state, no below-$m$ state** at $n \in \{22, 24\}$ in
   any sweep. The min-nquad decay $(10, 9)$ seen under exhaustion at
   18/20 does NOT continue along any tested route.
2. **The complete class of the qa_grow_n22 carrier is ONE state**
   (nquad 41); a SECOND $n = 22$ carrier exists — a growth child of
   the min-nquad $|\mathrm{Aut}| = 10$ carrier (explicit un-growth
   pinned in CHECK 6), non-isomorphic to the first, with complete
   class TWO states (nquad 41, 41). Every known $n = 22$ state has
   nquad EXACTLY 41 $\gg m = 12$ — a striking uniformity across two
   carriers and three states.
3. **The complete class of the qa_grow_n24 carrier is 13 states**
   (nquad 20–31, min 20 $> m = 13$, all quad-alive, lengths {8,16};
   pinned).
4. **Full vertex-transitivity excludes the class**: all 10 cubic
   circulants and all five $GP(11, k)$ at $n = 22$ have EMPTY class
   (CHECK 6 re-sweeps the circulants in-block); the 6-triangle-ring
   family at $n = 24$ is class-empty for every chord offset. The
   "high symmetry $\Rightarrow$ low nquad" reading of R53 is wrong as
   a trend: the min-nquad carrier's $|\mathrm{Aut}| = 10$ sits in a
   narrow window — symmetric enough to thin the quad supply,
   irregular enough to admit class states at all.
5. **Growth-descent is rare but real**: of 363 unique children of the
   four carriers, exactly ONE is in the class (G1's child above);
   G9/G0/G3 have NO class-carrying children. Combined with R52-R53:
   two descent instances are now on record (B $\to$ G3 at $18 \to
   20$, G1 $\to$ new carrier at $20 \to 22$), both to HIGH-nquad
   children — growth never transports the low-nquad structure.


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

<!-- CHECK
# quad_alive_universal CHECK 4 (R52 iso-audit anchor): the three pinned
# n=20 carrier graphs are pairwise NON-isomorphic — proved by triangle
# count alone (an isomorphism invariant): 5, 3, 4.  |Aut| pinned via
# exhaustive invariant-pruned backtracking (2, 1, 2), plus the n=22/24
# growth-pin invariants (tri 5 |Aut| 1; tri 7 |Aut| 2).  This corrects
# the n=18 lesson (five "distinct" falsifiers = ONE graph) in the other
# direction: the n>=20 pinned corpus is genuinely graph-diverse.
GRAPHS = {
 'qa_cold_n20': (20, [(0,3),(0,8),(0,11),(1,6),(1,8),(1,19),(2,8),(2,13),
  (2,18),(3,7),(3,10),(4,6),(4,11),(4,12),(5,13),(5,16),(5,19),(6,19),
  (7,15),(7,17),(9,10),(9,14),(9,18),(10,18),(11,12),(12,15),(13,16),
  (14,16),(14,17),(15,17)], 5, 2),
 'qa_warm34_n20': (20, [(0,2),(0,4),(0,7),(1,3),(1,5),(1,18),(2,4),(2,6),
  (3,15),(3,18),(4,8),(5,10),(5,19),(6,13),(6,15),(7,9),(7,12),(8,14),
  (8,16),(9,10),(9,15),(10,17),(11,12),(11,17),(11,19),(12,14),(13,16),
  (13,19),(14,16),(17,18)], 3, 1),
 'qa_warm15_n20': (20, [(0,2),(0,4),(0,7),(1,3),(1,5),(1,12),(2,4),(2,5),
  (3,17),(3,18),(4,8),(5,13),(6,10),(6,15),(6,17),(7,9),(7,12),(8,14),
  (8,16),(9,10),(9,14),(10,17),(11,13),(11,18),(11,19),(12,15),(13,16),
  (14,16),(15,19),(18,19)], 4, 2),
 'qa_grow_n22': (22, [(0,8),(0,11),(0,21),(1,6),(1,8),(1,19),(2,7),(2,13),
  (2,18),(3,4),(3,8),(3,16),(4,11),(4,12),(5,13),(5,16),(5,19),(6,19),
  (6,20),(7,15),(7,17),(9,10),(9,18),(9,21),(10,14),(10,18),(11,12),
  (12,15),(13,16),(14,17),(14,20),(15,17),(20,21)], 5, 1),
 'qa_grow_n24': (24, [(0,19),(0,21),(0,22),(1,5),(1,6),(1,8),(2,7),(2,9),
  (2,18),(3,8),(3,10),(3,16),(4,11),(4,12),(4,13),(5,6),(5,16),(6,20),
  (7,15),(7,17),(8,10),(9,14),(9,18),(10,18),(11,12),(11,21),(12,15),
  (13,16),(13,19),(14,17),(14,23),(15,17),(19,21),(20,22),(20,23),
  (22,23)], 7, 2),
}

def adj_of(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    assert all(len(a) == 3 for a in adj)
    return adj

def tri_per_vertex(n, adj):
    t = [0] * n
    for u in range(n):
        ns = sorted(adj[u])
        for i in range(3):
            for j in range(i + 1, 3):
                if ns[j] in adj[ns[i]]: t[u] += 1
    return t

def count_autos(n, adj, invar):
    # exhaustive backtracking over invariant-compatible maps; complete.
    order = sorted(range(n), key=lambda v: (invar[v], -len(adj[v])))
    mp = [-1] * n; inv = [-1] * n; cnt = [0]
    def rec(i):
        if i == n: cnt[0] += 1; return
        u = order[i]
        for c in range(n):
            if inv[c] >= 0 or invar[c] != invar[u]: continue
            ok = True
            for w in adj[u]:
                if mp[w] >= 0 and mp[w] not in adj[c]: ok = False; break
            if not ok: continue
            for w in adj[c]:
                if inv[w] >= 0 and inv[w] not in adj[u]: ok = False; break
            if not ok: continue
            mp[u] = c; inv[c] = u
            rec(i + 1)
            mp[u] = -1; inv[c] = -1
    rec(0)
    return cnt[0]

tris = {}
for name, (n, edges, expect_tri, expect_aut) in GRAPHS.items():
    adj = adj_of(n, edges)
    tv = tri_per_vertex(n, adj)
    ntri = sum(tv) // 3
    assert ntri == expect_tri, f"{name}: triangles {ntri} != {expect_tri}"
    invar = [(tv[v], tuple(sorted(tv[w] for w in adj[v]))) for v in range(n)]
    aut = count_autos(n, adj, invar)
    assert aut == expect_aut, f"{name}: |Aut| {aut} != {expect_aut}"
    tris[name] = ntri
    print(f"{name}: n={n} triangles={ntri} |Aut|={aut}")
n20 = ['qa_cold_n20', 'qa_warm34_n20', 'qa_warm15_n20']
assert len({tris[k] for k in n20}) == 3
print("R52 iso-audit anchor OK: triangle counts 5/3/4 pairwise distinct -> "
      "the three pinned n=20 carrier graphs are pairwise non-isomorphic")
CHECK -->

<!-- CHECK
# quad_alive_universal CHECK 5 (R53 exhaustive-census anchor, n=20): the
# COMPLETE triple-dead pair-residual class at n=20, all 42 states pinned
# compactly (BFS-canonical parent vector ; back edges), each re-verified
# from scratch: simple/cubic/connected, normal tree, triple-dead over all
# |S|<=3, quad-alive with EXACT (nquad, minpart, #8-cycles, #16-cycles).
# Census-level pins: 42 states; min nquad = 9 < m = 11 attained exactly
# twice, both minpart 0, both on ONE carrier graph with |Aut| = 10 (the
# nquad >= m floor is DEAD at the second exhaustive scale); 29/42 states
# have minpart = 0; all firing lengths in {8,16}; graph dedup (invariant
# partition + complete backtracking isomorphism) gives EXACTLY 10 carrier
# graphs with state counts 23/5/5/3/1x6.
from itertools import combinations
PO2_LENS = {4, 8, 16, 32}

CENSUS20 = [
 ('0,1,2,3,4,5,6,7,8,9,10,10,11,12,13,14,15,16,17;0-11,0-18,1-3,2-15,4-19,5-7,6-12,8-16,9-19,13-17,14-18', 26, 6, 7, 19),
 ('0,1,2,3,4,5,6,7,8,9,10,10,11,13,14,15,16,17,18;0-12,0-19,1-3,2-11,4-14,5-7,6-16,8-18,9-12,13-15,17-19', 21, 2, 5, 16),
 ('0,1,2,3,4,5,6,7,8,9,10,10,11,13,14,15,16,17,18;0-12,0-19,1-3,2-11,4-18,5-7,6-16,8-14,9-12,13-19,15-17', 20, 3, 7, 13),
 ('0,1,2,3,4,5,6,7,8,9,10,10,11,13,14,15,16,17,18;0-12,0-19,1-7,2-16,3-5,4-14,6-11,8-18,9-12,13-15,17-19', 19, 2, 7, 12),
 ('0,1,2,3,4,5,6,7,8,9,10,11,11,12,14,15,16,17,18;0-2,0-13,1-14,3-5,4-15,6-8,7-16,9-18,10-13,12-19,17-19', 24, 3, 5, 19),
 ('0,1,2,3,4,5,6,7,8,9,10,11,11,12,14,15,16,17,18;0-2,0-13,1-14,3-5,4-15,6-17,7-9,8-19,10-13,12-19,16-18', 32, 5, 5, 27),
 ('0,1,2,3,4,5,6,7,8,9,10,11,11,12,14,15,16,17,18;0-2,0-13,1-14,3-16,4-6,5-18,7-9,8-19,10-13,12-15,17-19', 37, 4, 10, 27),
 ('0,1,2,3,4,5,6,7,8,9,10,11,11,12,14,15,16,17,18;0-2,0-13,1-14,3-16,4-6,5-18,7-9,8-19,10-13,12-19,15-17', 24, 5, 5, 19),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,16,17,18;0-2,0-15,1-5,3-7,4-19,6-17,8-14,9-11,10-15,12-19,16-18', 37, 7, 9, 28),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,16,17,18;0-2,0-15,1-11,3-9,4-19,5-7,6-17,8-14,10-15,12-19,16-18', 34, 8, 10, 24),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,16,17,18;0-4,0-15,1-16,2-6,3-18,5-7,8-15,9-11,10-19,12-17,14-19', 45, 10, 7, 38),
 ('0,1,2,3,4,5,6,6,7,9,10,10,11,12,13,14,15,17,17;0-4,0-16,1-8,2-18,3-13,5-8,7-14,9-19,11-18,12-16,15-19', 34, 7, 7, 27),
 ('0,1,2,3,4,5,6,7,8,8,10,11,12,12,13,15,16,17,17;0-2,0-14,1-10,3-9,4-18,5-15,6-19,7-9,11-14,13-18,16-19', 30, 6, 6, 24),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-2,0-19,1-11,3-9,4-6,5-15,7-17,8-14,10-12,13-19,16-18', 19, 0, 4, 15),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-2,0-19,1-11,3-9,4-18,5-7,6-16,8-14,10-12,13-19,15-17', 17, 0, 8, 9),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-2,0-19,1-11,3-9,4-18,5-15,6-8,7-17,10-12,13-19,14-16', 17, 0, 5, 12),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-2,0-19,1-11,3-13,4-6,5-15,7-17,8-10,9-19,12-14,16-18', 9, 0, 4, 5),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-2,0-19,1-11,3-13,4-10,5-19,6-8,7-17,9-15,12-14,16-18', 16, 0, 6, 10),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-2,0-19,1-11,3-17,4-6,5-15,7-13,8-10,9-19,12-18,14-16', 15, 0, 6, 9),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-6,0-19,1-3,2-12,4-14,5-11,7-9,8-18,10-16,13-15,17-19', 19, 0, 4, 15),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-6,0-19,1-15,2-4,3-13,5-11,7-9,8-18,10-16,12-14,17-19', 17, 0, 8, 9),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-6,0-19,1-15,2-4,3-13,5-11,7-17,8-10,9-19,12-14,16-18', 20, 0, 6, 14),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-6,0-19,1-15,2-12,3-5,4-14,7-9,8-18,10-16,11-13,17-19', 17, 0, 5, 12),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-10,0-19,1-3,2-12,4-14,5-7,6-16,8-18,9-11,13-15,17-19', 9, 0, 4, 5),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-10,0-19,1-3,2-12,4-18,5-7,6-16,8-14,9-11,13-19,15-17', 20, 0, 6, 14),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-10,0-19,1-7,2-16,3-5,4-14,6-12,8-18,9-11,13-15,17-19', 15, 0, 6, 9),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-10,0-19,1-19,2-8,3-5,4-14,6-16,7-13,9-11,12-18,15-17', 25, 0, 6, 19),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-10,0-19,1-19,2-8,3-17,4-6,5-15,7-13,9-11,12-18,14-16', 27, 0, 10, 17),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-10,0-19,1-19,2-8,3-17,4-14,5-7,6-16,9-11,12-18,13-15', 23, 0, 6, 17),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-10,0-19,1-19,2-12,3-5,4-14,6-16,7-9,8-18,11-13,15-17', 19, 0, 4, 15),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-10,0-19,1-19,2-12,3-9,4-18,5-7,6-16,8-14,11-13,15-17', 18, 0, 6, 12),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-10,0-19,1-19,2-16,3-5,4-14,6-12,7-9,8-18,11-17,13-15', 21, 0, 6, 15),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-14,0-19,1-3,2-12,4-10,5-7,6-16,8-18,9-15,11-13,17-19', 16, 0, 6, 10),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-14,0-19,1-3,2-12,4-10,5-19,6-8,7-17,9-15,11-13,16-18', 22, 0, 8, 14),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-14,0-19,1-3,2-12,4-10,5-19,6-16,7-9,8-18,11-13,15-17', 22, 0, 5, 17),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-14,0-19,1-11,2-4,3-13,5-19,6-8,7-17,9-15,10-12,16-18', 22, 0, 5, 17),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-18,0-19,1-7,2-4,3-13,5-15,6-12,8-10,9-19,11-17,14-16', 25, 0, 6, 19),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-18,0-19,1-7,2-16,3-5,4-14,6-12,8-10,9-19,11-17,13-15', 27, 0, 10, 17),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-18,0-19,1-7,2-16,3-13,4-6,5-15,8-10,9-19,11-17,12-14', 23, 0, 6, 17),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-18,0-19,1-11,2-4,3-13,5-15,6-8,7-17,9-19,10-12,14-16', 19, 0, 4, 15),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-18,0-19,1-11,2-8,3-17,4-6,5-15,7-13,9-19,10-12,14-16', 21, 0, 6, 15),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;0-18,0-19,1-15,2-4,3-13,5-11,6-8,7-17,9-19,10-16,12-14', 18, 0, 6, 12),
]

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

n = 20
adjs = []; stats = []
for enc, xnq, xmp, xs8, xs16 in CENSUS20:
    ps, bs = enc.split(';')
    par = [-1] + [int(x) for x in ps.split(',')]
    bes = [tuple(int(x) for x in e.split('-')) for e in bs.split(',')]
    for i in range(2, n):
        assert par[i] >= par[i - 1] and par[i] < i
    edges = [tuple(sorted((par[v], v))) for v in range(1, n)] \
          + [tuple(sorted(e)) for e in bes]
    assert len(set(edges)) == 30
    deg = {}
    for u, v in edges:
        assert u != v
        deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    assert len(deg) == n and all(d == 3 for d in deg.values())
    depth = [0] * n
    for v in range(1, n): depth[v] = depth[par[v]] + 1
    anc = [set() for _ in range(n)]
    for v in range(1, n): anc[v] = anc[par[v]] | {par[v]}
    fc = []
    for u, w in bes:
        a, b = (u, w) if depth[u] <= depth[w] else (w, u)
        assert a in anc[b]              # normality
        es = set(); x = b
        while x != a:
            p = par[x]; es.add((min(x, p), max(x, p))); x = p
        es.add((min(u, w), max(u, w))); fc.append(es)
    m = len(fc)
    assert m == 11
    for size in (1, 2, 3):
        for sub in combinations(range(m), size):
            acc = set()
            for i in sub: acc ^= fc[i]
            assert scl(acc) not in PO2_LENS, "NOT triple-dead"
    quads = []
    for sub in combinations(range(m), 4):
        acc = set()
        for i in sub: acc ^= fc[i]
        L = scl(acc)
        if L in PO2_LENS: quads.append((sub, L))
    part = [0] * m; s8 = s16 = 0
    for sub, L in quads:
        if L == 8: s8 += 1
        else:
            assert L == 16; s16 += 1
        for i in sub: part[i] += 1
    assert (len(quads), min(part), s8, s16) == (xnq, xmp, xs8, xs16), \
        f"profile mismatch: {(len(quads), min(part), s8, s16)}"
    adj = [set() for _ in range(n)]
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    adjs.append(adj); stats.append((xnq, xmp))

assert len(CENSUS20) == 42
nqs = sorted(q for q, _ in stats)
assert nqs[0] == 9 and nqs.count(9) == 2 and all(q > 0 for q in nqs)
assert all(mp == 0 for q, mp in stats if q == 9)
assert sum(1 for _, mp in stats if mp == 0) == 29

def tri_pv(adj):
    t = [0] * n
    for u in range(n):
        ns = sorted(adj[u])
        for a in range(3):
            for b in range(a + 1, 3):
                if ns[b] in adj[ns[a]]: t[u] += 1
    return t

def iso_maps(adj1, adj2, count_all=False):
    t1, t2 = tri_pv(adj1), tri_pv(adj2)
    i1 = [(t1[v], tuple(sorted(t1[w] for w in adj1[v]))) for v in range(n)]
    i2 = [(t2[v], tuple(sorted(t2[w] for w in adj2[v]))) for v in range(n)]
    if sorted(i1) != sorted(i2): return 0
    order = sorted(range(n), key=lambda v: i1[v])
    mp = [-1] * n; iv = [-1] * n; cnt = [0]
    def rec(k):
        if k == n:
            cnt[0] += 1
            return not count_all
        u = order[k]
        for c in range(n):
            if iv[c] >= 0 or i2[c] != i1[u]: continue
            ok = True
            for w in adj1[u]:
                if mp[w] >= 0 and mp[w] not in adj2[c]: ok = False; break
            if ok:
                for w in adj2[c]:
                    if iv[w] >= 0 and iv[w] not in adj1[u]: ok = False; break
            if not ok: continue
            mp[u] = c; iv[c] = u
            if rec(k + 1): return True
            mp[u] = -1; iv[c] = -1
        return False
    rec(0)
    return cnt[0]

reps = []   # (adj, count, first index)
for i, adj in enumerate(adjs):
    for r in reps:
        if iso_maps(r[0], adj):
            r[1] += 1; break
    else:
        reps.append([adj, 1, i])
assert len(reps) == 10, f"{len(reps)} carrier graphs != 10"
assert sorted(r[1] for r in reps) == [1, 1, 1, 1, 1, 1, 3, 5, 5, 23]
lowidx = [i for i, (q, _) in enumerate(stats) if q == 9]
assert iso_maps(adjs[lowidx[0]], adjs[lowidx[1]]), "nquad-9 states on different graphs?"
aut = iso_maps(adjs[lowidx[0]], adjs[lowidx[0]], count_all=True)
assert aut == 10, f"min-nquad carrier |Aut| = {aut} != 10"
assert sum(tri_pv(adjs[lowidx[0]])) // 3 == 5
print("R53 census anchor OK: complete n=20 class = 42 states / 10 graphs, "
      "all quad-alive, lengths {8,16}; min nquad 9 < m = 11 (twice, minpart "
      "0, one |Aut|=10 carrier); 29/42 states have a quad-idle back edge")
CHECK -->

<!-- CHECK
# quad_alive_universal CHECK 6 (R54 targeted-hunt anchors, n in {22, 24}):
# (a) complete fixed-graph class sweeps IN-BLOCK via the validated
#     canonical-DFS enumerator: the qa_grow_n22 carrier has EXACTLY 1
#     class state (nquad 41); the new R54 carrier (a double-subdivision+
#     join child of the CHECK-5 min-nquad |Aut|=10 carrier) has EXACTLY 2
#     (nquad 41, 41) — every known n=22 state has nquad 41 >> m = 12;
# (b) the two n=22 carriers are NOT isomorphic (backtracking decision);
#     the new carrier IS a growth child of the min-nquad carrier
#     (verified by explicit un-growth);
# (c) ALL cubic circulants C22(s,11), s=1..10, have EMPTY class — full
#     vertex-transitivity excludes the class at n=22 entirely;
# (d) the 13 pinned states of the qa_grow_n24 carrier re-verify exactly
#     (min nquad 20 > m = 13, all quad-alive, lengths {8,16}).
from itertools import combinations
PO2MASK = (1 << 4) | (1 << 8) | (1 << 16) | (1 << 32)
PO2_LENS = {4, 8, 16, 32}

QA22 = [(0,8),(0,11),(0,21),(1,6),(1,8),(1,19),(2,7),(2,13),(2,18),(3,4),
 (3,8),(3,16),(4,11),(4,12),(5,13),(5,16),(5,19),(6,19),(6,20),(7,15),
 (7,17),(9,10),(9,18),(9,21),(10,14),(10,18),(11,12),(12,15),(13,16),
 (14,17),(14,20),(15,17),(20,21)]
CH22 = [(0,1),(0,2),(0,20),(1,2),(1,11),(2,3),(3,4),(3,13),(4,5),(4,6),
 (5,6),(5,15),(6,7),(7,8),(7,21),(8,9),(8,10),(9,10),(9,19),(10,11),
 (11,12),(12,13),(12,14),(13,14),(14,15),(15,16),(16,17),(16,18),(17,18),
 (17,21),(18,19),(19,20),(20,21)]
G1_20 = [(0,1),(0,2),(0,19),(1,2),(1,11),(2,3),(3,4),(3,13),(4,5),(4,6),
 (5,6),(5,15),(6,7),(7,8),(7,17),(8,9),(8,10),(9,10),(9,19),(10,11),
 (11,12),(12,13),(12,14),(13,14),(14,15),(15,16),(16,17),(16,18),(17,18),
 (18,19)]
N24_STATES = [
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,16,17,18,19,20,21,21;9-11,4-0,22-17,22-20,1-23,13-15,3-5,0-23,15-10,12-2,19-7,16-18,6-8', 26),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,16,17,18,19,20,20,22;9-11,4-0,1-23,13-15,3-5,21-16,21-17,0-23,19-22,15-10,12-2,18-7,6-8', 27),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,17,18,19,20,21,22;10-12,5-0,22-18,2-0,14-16,4-6,21-23,1-23,16-11,13-3,20-8,17-19,7-9', 21),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,17,18,19,20,21,22;10-12,5-0,23-18,23-21,2-0,14-16,4-6,1-22,16-11,13-3,20-8,17-19,7-9', 22),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,17,18,19,20,21,21;10-12,5-0,2-0,14-16,4-6,22-17,22-18,20-23,1-23,16-11,13-3,19-8,7-9', 20),
 ('0,1,2,3,4,4,5,7,8,9,10,11,12,13,14,15,15,17,18,19,20,21,22;10-12,23-18,23-21,1-6,14-16,3-5,6-0,0-22,16-11,13-2,20-8,17-19,7-9', 28),
 ('0,1,2,3,4,4,5,7,8,9,10,11,12,13,14,15,15,17,18,19,20,21,21;10-12,1-6,14-16,3-5,22-17,22-18,6-0,20-23,0-23,16-11,13-2,19-8,7-9', 25),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,17,18,19,20,21,22;10-12,5-1,23-18,23-21,2-0,14-16,4-6,0-22,16-11,13-3,20-8,17-19,7-9', 20),
 ('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,17,18,19,20,21,21;10-12,5-1,2-0,14-16,4-6,22-17,22-18,20-23,0-23,16-11,13-3,19-8,7-9', 21),
 ('0,1,2,3,4,5,6,7,8,9,10,11,11,12,14,15,16,17,17,18,19,21,22;3-1,9-7,15-20,22-0,8-13,16-19,10-12,20-14,23-21,23-2,0-13,18-5,6-4', 31),
 ('0,1,2,3,4,5,5,7,8,9,10,11,11,12,14,15,16,17,18,19,20,21,22;17-19,6-1,6-4,8-13,21-23,10-12,13-7,23-18,22-0,20-9,3-15,0-2,14-16', 20),
 ('0,1,2,3,4,5,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22;17-19,12-8,6-1,6-4,9-7,21-23,11-13,22-18,23-0,20-10,3-15,0-2,14-16', 21),
 ('0,1,2,3,4,5,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22;17-19,12-8,6-1,6-4,9-7,21-23,11-13,23-18,22-0,20-10,3-15,0-2,14-16', 20),
]


def sweep(n, edges):
    """Canonical-DFS class enumerator (validated R54): returns list of
    (root, par) for every triple-dead pair-residual normal tree."""
    edges = sorted(tuple(sorted(e)) for e in edges)
    adj = [[] for _ in range(n)]
    eidx = {}
    for i, (u, v) in enumerate(edges):
        adj[u].append(v); adj[v].append(u)
        eidx[(u, v)] = i; eidx[(v, u)] = i
    for a in adj:
        a.sort(); assert len(a) == 3
    par = [-1] * n; visited = [False] * n
    pathmask = [0] * n; lastchild = [-1] * n
    fcs = []; cands = []; marks = []
    deg2 = bytearray(n); nb1 = [0] * n; nb2 = [0] * n; tv = [0] * 70
    out = []

    def is_single(t, L):
        mm = t; ntv = 0
        while mm:
            b = mm & -mm; i = b.bit_length() - 1; mm ^= b
            u, v = edges[i]
            if deg2[u]: nb2[u] = v
            else: nb1[u] = v; tv[ntv] = u; ntv += 1
            deg2[u] += 1
            if deg2[v]: nb2[v] = u
            else: nb1[v] = u; tv[ntv] = v; ntv += 1
            deg2[v] += 1
        start = tv[0]; prev = start; cur = nb1[start]; steps = 1
        while cur != start:
            a = nb1[cur]
            if a == prev: a = nb2[cur]
            prev = cur; cur = a; steps += 1
        for x in range(ntv): deg2[tv[x]] = 0
        return steps == L

    def close_backedges(w):
        added = 0; pw = par[w]
        for u in adj[w]:
            if not visited[u] or u == pw: continue
            f = (pathmask[w] ^ pathmask[u]) | (1 << eidx[(u, w)])
            ok = True
            c = f.bit_count()
            if c == 4 or ((PO2MASK >> c) & 1 and is_single(f, c)): ok = False
            if ok:
                for x in cands:
                    t = f ^ x; c = t.bit_count()
                    if c == 4 or ((PO2MASK >> c) & 1 and is_single(t, c)):
                        ok = False; break
            if not ok:
                for _ in range(added):
                    fcs.pop(); del cands[marks.pop():]
                return added, False
            marks.append(len(cands)); k = len(fcs)
            cands.append(f)
            for i in range(k): cands.append(f ^ fcs[i])
            fcs.append(f); added += 1
        return added, True

    def rec(stack, root):
        i = len(stack) - 1
        while i >= 0:
            cur = stack[i]
            if not (visited[adj[cur][0]] and visited[adj[cur][1]]
                    and visited[adj[cur][2]]): break
            i -= 1
        if i < 0:
            out.append((root, tuple(par))); return
        cur = stack[i]; live = stack[:i + 1]; lc = lastchild[cur]
        for w in adj[cur]:
            if visited[w] or w <= lc: continue
            visited[w] = True; par[w] = cur
            pathmask[w] = pathmask[cur] | (1 << eidx[(cur, w)])
            lastchild[cur] = w
            k, ok = close_backedges(w)
            if ok:
                rec(live + [w], root)
                for _ in range(k):
                    fcs.pop(); del cands[marks.pop():]
            visited[w] = False; par[w] = -1; lastchild[cur] = lc
        return

    for root in range(n):
        visited[root] = True; par[root] = -1; pathmask[root] = 0
        rec([root], root)
        visited[root] = False
    return out


def profile(n, root, par, edges):
    edges = [tuple(sorted(e)) for e in edges]
    depth = [-1] * n; depth[root] = 0
    pend = [v for v in range(n) if v != root]
    while pend:
        nxt = []
        for v in pend:
            if depth[par[v]] >= 0: depth[v] = depth[par[v]] + 1
            else: nxt.append(v)
        assert len(nxt) < len(pend); pend = nxt
    tre = {(min(v, par[v]), max(v, par[v])) for v in range(n) if v != root}
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
    assert m == n // 2 + 1
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
    for size in (1, 2, 3):
        for sub in combinations(range(m), size):
            acc = set()
            for i in sub: acc ^= fc[i]
            assert scl(acc) not in PO2_LENS, "not triple-dead"
    nq = 0
    for sub in combinations(range(m), 4):
        acc = set()
        for i in sub: acc ^= fc[i]
        L = scl(acc)
        if L in PO2_LENS:
            assert L in (8, 16); nq += 1
    return nq

# (a) complete sweeps
hits22 = sweep(22, QA22)
nq22 = sorted(profile(22, r, p, QA22) for r, p in hits22)
# labeled dedup not needed for the count claim if raw == states; assert raw
assert nq22 == [41], f"qa_grow_n22 carrier class: {nq22}"
hits_ch = sweep(22, CH22)
nq_ch = sorted(profile(22, r, p, CH22) for r, p in hits_ch)
assert nq_ch == [41, 41], f"new n=22 carrier class: {nq_ch}"
print(f"n=22 complete sweeps OK: known carriers have classes {nq22} and {nq_ch} "
      f"(every known n=22 state: nquad 41, m=12)")

# (b) carriers distinct + growth-descent verified by explicit un-growth
def adj_of(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    return adj

def tri_pv(n, adj):
    t = [0] * n
    for u in range(n):
        ns = sorted(adj[u])
        for a in range(len(ns)):
            for b in range(a + 1, len(ns)):
                if ns[b] in adj[ns[a]]: t[u] += 1
    return t

def iso(n, adj1, adj2):
    t1, t2 = tri_pv(n, adj1), tri_pv(n, adj2)
    i1 = [(t1[v], tuple(sorted(t1[w] for w in adj1[v]))) for v in range(n)]
    i2 = [(t2[v], tuple(sorted(t2[w] for w in adj2[v]))) for v in range(n)]
    if sorted(i1) != sorted(i2): return False
    order = sorted(range(n), key=lambda v: i1[v])
    mp = [-1] * n; iv = [-1] * n
    def rec(k):
        if k == n: return True
        u = order[k]
        for c in range(n):
            if iv[c] >= 0 or i2[c] != i1[u]: continue
            ok = True
            for w in adj1[u]:
                if mp[w] >= 0 and mp[w] not in adj2[c]: ok = False; break
            if ok:
                for w in adj2[c]:
                    if iv[w] >= 0 and iv[w] not in adj1[u]: ok = False; break
            if not ok: continue
            mp[u] = c; iv[c] = u
            if rec(k + 1): return True
            mp[u] = -1; iv[c] = -1
        return False
    return rec(0)

assert not iso(22, adj_of(22, QA22), adj_of(22, CH22)), "n=22 carriers iso?!"
# un-growth: contract 20 and 21 out of CH22 -> must equal G1_20 exactly
ch = set(map(tuple, (tuple(sorted(e)) for e in CH22)))
n20, n21 = 20, 21
nb20 = sorted(u for u, v in ch if v == n20) + sorted(v for u, v in ch if u == n20)
nb21 = sorted(u for u, v in ch if v == n21) + sorted(v for u, v in ch if u == n21)
nb20 = [x for x in nb20 if x != n21]; nb21 = [x for x in nb21 if x != n20]
assert len(nb20) == 2 and len(nb21) == 2
base = {e for e in ch if n20 not in e and n21 not in e}
base.add(tuple(sorted(nb20))); base.add(tuple(sorted(nb21)))
assert base == {tuple(sorted(e)) for e in G1_20}, "un-growth != G1"
print("n=22 carriers pairwise non-iso; new carrier = double-subdivision+join "
      "child of the CHECK-5 min-nquad |Aut|=10 carrier (explicit un-growth)")

# (c) circulant emptiness
for s in range(1, 11):
    e = set()
    for i in range(22):
        e.add(tuple(sorted((i, (i + s) % 22))))
        e.add(tuple(sorted((i, (i + 11) % 22))))
    assert not sweep(22, sorted(e)), f"C22({s},11) has a class state?!"
print("all 10 cubic circulants C22(s,11): class EMPTY (vertex-transitivity "
      "excludes the class at n=22)")

# (d) the 13 pinned states of the qa_grow_n24 carrier
QA24 = [(0,19),(0,21),(0,22),(1,5),(1,6),(1,8),(2,7),(2,9),(2,18),(3,8),
 (3,10),(3,16),(4,11),(4,12),(4,13),(5,6),(5,16),(6,20),(7,15),(7,17),
 (8,10),(9,14),(9,18),(10,18),(11,12),(11,21),(12,15),(13,16),(13,19),
 (14,17),(14,23),(15,17),(19,21),(20,22),(20,23),(22,23)]
seen_nq = []
for enc, xnq in N24_STATES:
    ps, bs = enc.split(';')
    par = [-1] + [int(x) for x in ps.split(',')]
    bes = [tuple(int(x) for x in e.split('-')) for e in bs.split(',')]
    n = 24
    edges = [tuple(sorted((par[v], v))) for v in range(1, n)] \
          + [tuple(sorted(e)) for e in bes]
    assert len(set(edges)) == 36
    nq = profile(n, 0, par, edges)
    assert nq == xnq, f"n=24 state nquad {nq} != {xnq}"
    seen_nq.append(nq)
assert sorted(seen_nq) == [20, 20, 20, 20, 21, 21, 21, 22, 25, 26, 27, 28, 31]
print("qa_grow_n24 carrier: 13 pinned states re-verified (min nquad 20 > "
      "m = 13, all quad-alive, lengths {8,16})")
print("R54 anchors OK")

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
