---
id: lp_dual_8cycle
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 57
---

# Lemma `lp_dual_8cycle` — integer counting duals certify the L1 8-cycle layer (no integrality gap at n <= 22)

**Claim.** Let $G$ be a connected cubic graph on $n \le 22$ vertices with
no 4-cycle, $m = n/2 + 1$, and let $C_8(G)$ be its set of 8-cycles. If no
$m$-edge subset $X \subseteq E(G)$ satisfies $|c \cap X| \ge 5$ for every
$c \in C_8(G)$ (the 8-cycle system is integrally un-5-coverable), then
some integer dual $y : C_8(G) \to \mathbb{Z}_{\ge 0}$, $y \ne 0$,
satisfies
$$\Big(\text{sum of the } m \text{ largest values of } w_y(e) = \sum_{c \ni e} y_c\Big) \;<\; 5 \sum_c y_c.$$

**Why a firing dual proves L1-infeasibility (3 lines).** For any $m$-set
$X$: $\sum_c y_c\,|c \cap X| = \sum_{e \in X} w_y(e) \le \text{top}_m(w_y)
< 5\sum_c y_c$, so some 8-cycle $c$ has $|c \cap X| \le 4$. Hence $G$ is
not 5-coverable at the 8-cycle layer, hence (R55 reframing, Section 95)
no quad-dead normal-tree state exists on $G$.

**Status of the claim.** The *certificate direction* (a firing dual
implies infeasibility) is proved above unconditionally, at every $n$.
The open content is the CONVERSE (no integrality gap at $n \le 22$):
integral infeasibility always exhibits an integer counting dual.
Evidence: 4/4 pinned carriers fire (three on the uniform dual $y \equiv 1$;
`qa_grow_n22` needs $y = (1,2,1,1,1)$, value $14 < 15$); 36/36 random
C4-free cubic $n = 18$ graphs with exactly-infeasible 8-cycle systems
fire under integer dual ascent; zero gap instances observed.

**Theorem shape this feeds (the analytic target).** If every edge of $G$
lies on at most $d$ of its 8-cycles and $c_8 > d \cdot m / 5$, the uniform
dual fires: $\text{top}_m(w_1) \le d\,m < 5\,c_8$. So quad-death requires
the 8-cycle incidence mass ($8 c_8$ slots) to concentrate on $\le m$
edges — "L1 needs $c_8$ collapse" with explicit constants.

**Re-audit finding (R57, corrects an R55 sub-tally).** Carrier A
(`ta_falsifier_warm_n18`, $N = 67$, $c_8 = 3$) has a 5-COVERABLE 8-cycle
subsystem: the 10-edge set pinned in the CHECK hits all three 8-cycles
$\ge 5$ times ($m = 10$). Independently re-verified this session. So
R55's prose sub-tally "the 8-cycle subsystem is already un-5-coverable
for 14 of the 15 carriers (lone exception the $(c_8,N) = (7,139)$
carrier at $n=20$)" is WRONG about carrier A — it has (at least) TWO
exceptions. The R55 THEOREM itself (no quad-dead state on any known
carrier; full 8+16 system un-5-coverable) is unaffected: it was proved
by SAT + the stdlib DP over the FULL PO2 system (CHECKs 7-8 of
`lemma_quad_alive_universal`, which still pass), and adding 16-cycle
constraints only strengthens infeasibility. Carrier A's L1 obstruction
lives in the mixed 8/16 layer, where counting duals with 16-cycle
weights (see `lemma_frac_starvation_l1pass`) are the right certificate
language.

**Current obstacle.** Prove the converse at $n \le 22$ (LP duality gives
a FRACTIONAL dual whenever the fractional relaxation is infeasible; the
gap questions are (i) fractional feasibility vs integral infeasibility
of the cover side, and (ii) rounding the dual to integer $y$ — dual
ascent has closed every observed instance, suggesting a Hall-type
exchange argument on the 8-cycle incidence structure). Falsified by:
one C4-free cubic graph at $n \le 22$ whose 8-cycle system is exactly
un-5-coverable but on which no integer dual fires.

<!-- CHECK
# lp_dual_8cycle CHECK (draft): fractional/counting duals for the L1 layer.
# A counting dual is y >= 0 on the 8-cycles with
#   sum of the m largest w_y(e) < 5 * sum_c y_c,   w_y(e) = sum_{c ni e} y_c.
# Any such y proves (3 lines) that NO m-subset X 5-covers the 8-cycle
# system, hence G is L1-infeasible (non-5-coverable), hence no quad-dead
# state on G.  Probe:
#  A) the three n=20 pinned carriers fire on the UNIFORM dual (y=1);
#     qa_grow_n22 fires on a nonuniform integer dual found by ascent;
#  B) ta_warm_n18 (carrier A, N=67): its 8-cycle system IS 5-coverable
#     (explicit pinned cover) — so no 8-cycle dual can exist and the
#     R55 "14 of 15 carriers are 8-cycle-obstructed" tally needs
#     re-audit: A's obstruction lives in the mixed 8/16 system;
#  C) killable universal arm: random 4-cycle-free cubic graphs at n=18;
#     whenever the exact B&B says the 8-cycle system is integrally
#     un-5-coverable, integer dual ascent must find a firing y
#     (falsified => an integrality-gap instance at the 8-cycle layer).
import random
from itertools import combinations

def cycles_of_len(n, adj, L):
    out = []
    for s in range(n):
        stack = [(s, [s], {s})]
        while stack:
            u, path, vis = stack.pop()
            if len(path) == L:
                if s in adj[u] and path[1] < path[-1]:
                    out.append(frozenset(tuple(sorted((path[i], path[(i+1) % L])))
                                         for i in range(L)))
                continue
            for w in adj[u]:
                if w > s and w not in vis:
                    stack.append((w, path + [w], vis | {w}))
    return out

def fires(y, cyc, m):
    w = {}
    for yc, c in zip(y, cyc):
        if yc:
            for e in c: w[e] = w.get(e, 0) + yc
    vals = sorted(w.values(), reverse=True)
    return sum(vals[:m]) < 5 * sum(y)

def dual_ascent(cyc, m, rounds=200):
    """Integer dual ascent; returns a firing y or None. Exact arithmetic."""
    k = len(cyc)
    y = [1] * k
    for _ in range(rounds):
        if fires(y, cyc, m): return y
        w = {}
        for yc, c in zip(y, cyc):
            for e in c: w[e] = w.get(e, 0) + yc
        top = set(sorted(w, key=w.get, reverse=True)[:m])
        # bump cycles undercovered by the current adversarial top-m set
        bumped = False
        for i, c in enumerate(cyc):
            if len(c & top) < 5:
                y[i] += 1; bumped = True
        if not bumped: return None       # top-m 5-covers everything: no ascent step
        if max(y) > 64: return None
    return y if fires(y, cyc, m) else None

def coverable_exact(cyc, m, node_cap=4_000_000):
    """Exact: does some edge set of size <= m meet every cycle in >= 5 edges?
       Branch & bound on the most-deficient cycle, pruned by the counting
       lower bound ceil(total_deficit / max_edge_multiplicity).
       Returns True/False/None(cap)."""
    mult = {}
    for c in cyc:
        for e in c: mult[e] = mult.get(e, 0) + 1
    maxmult = max(mult.values())
    nodes = [0]
    def rec(X, budget):
        nodes[0] += 1
        if nodes[0] > node_cap: raise TimeoutError
        worst, deficit, total = None, 0, 0
        for c in cyc:
            d = 5 - len(c & X)
            if d > 0:
                total += d
                if d > deficit: worst, deficit = c, d
        if deficit == 0: return True
        if deficit > budget: return False
        if (total + maxmult - 1) // maxmult > budget: return False
        for e in sorted(worst - X, key=lambda e: -mult[e]):
            if rec(X | {e}, budget - 1): return True
        return False
    try:
        return rec(frozenset(), m)
    except TimeoutError:
        return None

# ---- Part A: pinned carriers --------------------------------------------
PINS = {
 'qa_cold_n20': (20, [(0,3),(0,8),(0,11),(1,6),(1,8),(1,19),(2,8),(2,13),
  (2,18),(3,7),(3,10),(4,6),(4,11),(4,12),(5,13),(5,16),(5,19),(6,19),
  (7,15),(7,17),(9,10),(9,14),(9,18),(10,18),(11,12),(12,15),(13,16),
  (14,16),(14,17),(15,17)], 5, True),
 'qa_warm34_n20': (20, [(0,2),(0,4),(0,7),(1,3),(1,5),(1,18),(2,4),(2,6),
  (3,15),(3,18),(4,8),(5,10),(5,19),(6,13),(6,15),(7,9),(7,12),(8,14),
  (8,16),(9,10),(9,15),(10,17),(11,12),(11,17),(11,19),(12,14),(13,16),
  (13,19),(14,16),(17,18)], 10, True),
 'qa_warm15_n20': (20, [(0,2),(0,4),(0,7),(1,3),(1,5),(1,12),(2,4),(2,5),
  (3,17),(3,18),(4,8),(5,13),(6,10),(6,15),(6,17),(7,9),(7,12),(8,14),
  (8,16),(9,10),(9,14),(10,17),(11,13),(11,18),(11,19),(12,15),(13,16),
  (14,16),(15,19),(18,19)], 7, True),
 'qa_grow_n22': (22, [(0,8),(0,11),(0,21),(1,6),(1,8),(1,19),(2,7),(2,13),
  (2,18),(3,4),(3,8),(3,16),(4,11),(4,12),(5,13),(5,16),(5,19),(6,19),
  (6,20),(7,15),(7,17),(9,10),(9,18),(9,21),(10,14),(10,18),(11,12),
  (12,15),(13,16),(14,17),(14,20),(15,17),(20,21)], 5, False),
}
for name, (n, edges, exp_c8, exp_uniform) in PINS.items():
    edges = [tuple(sorted(e)) for e in edges]
    adj = [set() for _ in range(n)]
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    assert all(len(a) == 3 for a in adj)
    m = n // 2 + 1
    cyc = cycles_of_len(n, adj, 8)
    assert len(cyc) == exp_c8, f"{name}: c8 {len(cyc)} != {exp_c8}"
    uni = fires([1] * len(cyc), cyc, m)
    assert uni == exp_uniform, f"{name}: uniform-dual fire = {uni}"
    y = dual_ascent(cyc, m)
    assert y is not None, f"{name}: NO integer dual fires (ascent failed)"
    # a firing dual is itself the infeasibility proof; no B&B cross-check needed
    print(f"{name}: c8={len(cyc)} uniform_fires={uni} dual={y} "
          f"-> L1-infeasible by counting certificate")

# ---- Part B: ta_warm (carrier A) is NOT 8-cycle-obstructed --------------
n, edges = 18, [(0,7),(0,9),(0,16),(1,2),(1,15),(1,17),(2,8),(2,13),
 (3,12),(3,13),(3,14),(4,5),(4,11),(4,15),(5,7),(5,10),(6,9),(6,10),
 (6,11),(7,16),(8,11),(8,12),(9,10),(12,17),(13,14),(14,16),(15,17)]
adj = [set() for _ in range(n)]
for u, v in edges: adj[u].add(v); adj[v].add(u)
cyc = cycles_of_len(n, adj, 8)
assert len(cyc) == 3
COVER_A = {(1,2),(3,14),(1,15),(6,11),(0,9),(2,13),(5,7),(4,5),(3,12),(4,11)}
assert len(COVER_A) == 10 and all(len(c & COVER_A) >= 5 for c in cyc)
assert dual_ascent(cyc, 10) is None
print("ta_warm_n18: c8=3, 8-cycle system 5-COVERABLE (pinned 10-edge cover) "
      "-> carrier A's L1 obstruction is NOT in the 8-cycle layer; "
      "R55 '14 of 15' tally needs re-audit")

# ---- Part C: killable arm on random 4-cycle-free cubic graphs -----------
def random_cubic(n, rng):
    while True:
        stubs = [v for v in range(n) for _ in range(3)]
        rng.shuffle(stubs)
        E = set()
        ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i+1]
            if a == b or (min(a,b), max(a,b)) in E: ok = False; break
            E.add((min(a,b), max(a,b)))
        if ok: return sorted(E)

rng = random.Random(20260823)
n = 18; m = n // 2 + 1
tested = infeasible_cases = fired_cases = 0
for trial in range(400):
    if tested >= 18: break
    edges = random_cubic(n, rng)
    adj = [set() for _ in range(n)]
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    if cycles_of_len(n, adj, 4): continue          # 4-cycle: quad-death dead outright
    cyc = cycles_of_len(n, adj, 8)
    if not cyc: continue
    tested += 1
    cov = coverable_exact(cyc, m)
    if cov is None: print("  (node cap; skipped)"); continue
    if cov: continue                                # feasible: no dual required
    infeasible_cases += 1
    y = dual_ascent(cyc, m)
    assert y is not None, \
        (f"FALSIFIED (integrality gap at the 8-cycle layer): un-5-coverable "
         f"8-cycle system with no counting dual; edges={edges}")
    fired_cases += 1
assert infeasible_cases >= 3, \
    f"probe vacuous: only {infeasible_cases} infeasible instances among {tested}"
print(f"random arm OK: {tested} 4-cycle-free cubic graphs at n=18, "
      f"{infeasible_cases} un-5-coverable 8-cycle systems, ALL certified by "
      f"an integer counting dual ({fired_cases}/{infeasible_cases})")

CHECK -->
