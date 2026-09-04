---
id: frac_starvation_l1pass
status: disproved
depends_on: []
discharged_by_round: 58
introduced_at_round: 57
---

# Lemma `frac_starvation_l1pass` — mixed LP packing certificates block the cotree layer on the $c_8 \ge 2$ stratum

**Claim.** Let $G$ be a connected cubic C4-free graph on $n < 32$
vertices, $m = n/2 + 1$, $C(G)$ its cycles of length 8 or 16, $D(G)$ its
cycles of length $\le 7$, and
$$\Lambda(G) = \max\Big\{ 5 \sum_{c \in C(G)} y_c + \sum_{D \in D(G)} z_D \;:\; y, z \ge 0,\;\; \forall e:\; \sum_{c \ni e} y_c + \sum_{D \ni e} z_D \le 1 \Big\}.$$
If $G$ is 5-coverable (some $m$-subset $X$ has $|c \cap X| \ge 5$ for all
$c \in C(G)$) and $c_8(G) \ge 2$, then $\Lambda(G) > m$.

**Why $\Lambda > m$ blocks the cotree layer (weak duality, 3 lines).**
A cotree is an $m$-edge set hitting EVERY cycle of $G$ (complement
acyclic), in particular every $D \in D(G)$. If $X$ is a cotree AND a
5-cover, then for any feasible $(y, z)$:
$5\sum y_c + \sum z_D \le \sum_c y_c |c \cap X| + \sum_D z_D |D \cap X|
= \sum_{e \in X} \big(\textstyle\sum_{c \ni e} y_c + \sum_{D \ni e} z_D\big) \le |X| = m$.
So $\Lambda(G) > m$ implies no 5-cover is a cotree, hence (R55) no
quad-dead normal-tree state exists on $G$. This is the L2
"triangle starvation" of R56 expressed as explicit rational dual data.

**Strictly weaker than EGC / than `quad_alive_universal`:** finite
family, conditional on $c_8 \ge 2$; the $c_8 \le 1$ stratum is exempt.

**The $c_8 \ge 2$ hypothesis is provably necessary.** The $n = 24$
carrier QA24 ($c_8 = 1$) has $\Lambda = 167/14 < 13 = m$ (exact LP,
verified this session's ideation probes by two independent proposers:
the fractional relaxation of "cotree 5-cover" is FEASIBLE on QA24 by
Frank-Wolfe over the cographic base polytope, while the integral
problem is UNSAT by R55's CEGAR). The L2 block at $c_8 \le 1$ is a pure
integrality gap — no LP certificate can express it. That stratum is the
benched triangle-pocket integral-discharging program (ideation P2, see
notes channel).

**Evidence (all exact rational, pinned in the CHECKs).**
1. QA22 carrier: fractional PO2-only packing value $5\nu^* = 25/2 > 12 = m$
   (11-cycle certificate) — the fractional refinement of the DEAD integer
   packing bound ($\nu \le 2$, never fired) DOES fire.
2. The pinned R56 $n = 26$ L1-pass (CHECK-10 graph of
   `lemma_quad_alive_universal`, $c_8 = 4$): mixed value $57/4 > 14 = m$,
   with triangle weights $1/4$–$5/8$ on 7 of its 8 triangles — starvation
   as dual data.
3. Three fresh C4-free $c_8 \ge 2$ double-subdivision children of QA24
   that pass L1 (exact DP): all certified $\Lambda \ge 103/7, 59/4, 103/7
   > 14$ (search out-of-block, ~41 s float LP + exact rational rounding
   + exact re-verification; certificates pinned in CHECK 2).

**Analytic target.** A closed-form dual construction (one 8-cycle near
weight $1/2$, triangles near $1/2$, a spread of 16-cycles) proving
$\Lambda > m$ for EVERY C4-free 5-coverable cubic $G$ with $c_8 \ge 2$ —
this would convert the computational R56 closure into a two-line-
verifiable theorem on that stratum.

**Current obstacle / falsifier.** Exact LP on any single C4-free
5-coverable (L1-pass) cubic graph with $c_8 \ge 2$ certifying
$\Lambda \le m$ falsifies the lemma. Next round: exact LP over ALL 61
R56 L1-passes ($c_8$ ranges 2–6) to map the survivor family; any
$\Lambda \le m$ instance kills the claim (and becomes the P2 bench's
first target). The out-of-block search harness is reconstructable from
`draft_check.py`'s description in this file plus the CHECK-2 pinned
example.

<!-- CHECK
# frac_starvation_l1pass CHECK (draft): (a) pinned rational dual certificate
# that the QA22 carrier is L1-infeasible at the LP level: 11 PO2 cycles with
# weights y, per-edge load <= 1, 5*sum(y) = 25/2 > m = 12 (the DEAD integer
# packing bound gives only 5*nu = 10 <= 12 -- the fractional refinement
# fires where the integer one never did).  (b) pinned MIXED certificate on
# the R56 n=26 L1-pass (CHECK-10 graph): 9 PO2 cycles + 10 short cycles,
# value 57/4 > m = 14 => no 5-cover is a cotree, LP-certified (replacing
# the out-of-block SAT/CEGAR certificate for THIS graph).  (c) killable
# probe of the lemma "L1-pass & c8 >= 2 => Lambda(G) > m": the first 3
# C4-free 5-coverable c8>=2 double-subdivision+join children of the n=24
# carrier get a float LP + exact rational rounding; a child whose certified
# value is <= m FALSIFIES the lemma.  Boundary fact (not asserted here,
# session-verified): the n=24 carrier itself (c8=1) has Lambda = 167/14 < 13
# -- the c8 >= 2 hypothesis is necessary.
from fractions import Fraction
from itertools import combinations

def cyc_enum(n, edges, lens, Lmax):
    adj = [[] for _ in range(n)]
    for u, v in edges: adj[u].append(v); adj[v].append(u)
    out = []; path = [0]*(Lmax+1); onpath = [False]*n
    def rec(s, u, ln):
        for w in adj[u]:
            if w == s and ln >= 3:
                if ln in lens and path[1] < path[ln-1]:
                    out.append(frozenset(
                        [tuple(sorted((path[i], path[i+1]))) for i in range(ln-1)]
                        + [tuple(sorted((path[ln-1], s)))]))
            elif w > s and not onpath[w] and ln < Lmax:
                onpath[w] = True; path[ln] = w
                rec(s, w, ln+1)
                onpath[w] = False
    for s in range(n):
        onpath[s] = True; path[0] = s
        rec(s, s, 1); onpath[s] = False
    return out

def verify_cert(n, edges, cert, m, po2set):
    # cert: list of (num, den, [edge,...]); PO2 members weighted 5, short 1
    load = {e: Fraction(0) for e in edges}
    val = Fraction(0)
    for num, den, ce in cert:
        w = Fraction(num, den); ce = frozenset(tuple(sorted(e)) for e in ce)
        assert all(e in load for e in ce)
        deg = {}
        for u, v in ce: deg[u] = deg.get(u, 0)+1; deg[v] = deg.get(v, 0)+1
        assert all(d == 2 for d in deg.values())          # disjoint-cycle union suffices for validity of the dual row only if a SINGLE cycle; check connectivity:
        aj = {}
        for u, v in ce: aj.setdefault(u, []).append(v); aj.setdefault(v, []).append(u)
        st = next(iter(deg)); seen = {st}; stk = [st]
        while stk:
            u = stk.pop()
            for w2 in aj[u]:
                if w2 not in seen: seen.add(w2); stk.append(w2)
        assert len(seen) == len(deg), "not a single cycle"
        if len(ce) in (8, 16) and ce in po2set: coef = 5
        else:
            assert len(ce) <= 7, "short constraint too long"
            coef = 1
        val += coef * w
        for e in ce: load[e] += w
    assert max(load.values()) <= 1, "dual infeasible"
    return val

QA22 = [(0,8),(0,11),(0,21),(1,6),(1,8),(1,19),(2,7),(2,13),(2,18),(3,4),
 (3,8),(3,16),(4,11),(4,12),(5,13),(5,16),(5,19),(6,19),(6,20),(7,15),
 (7,17),(9,10),(9,18),(9,21),(10,14),(10,18),(11,12),(12,15),(13,16),
 (14,17),(14,20),(15,17),(20,21)]
CERT22 = [
 (1,6,[(0,8),(0,11),(1,6),(1,8),(2,13),(2,18),(3,4),(3,16),(4,11),(5,13),(5,16),(6,20),(9,10),(9,21),(10,18),(20,21)]),
 (1,6,[(0,8),(0,21),(2,7),(2,18),(3,4),(3,8),(4,11),(7,17),(9,10),(9,18),(10,14),(11,12),(12,15),(14,20),(15,17),(20,21)]),
 (1,6,[(0,11),(0,21),(1,6),(1,8),(2,13),(2,18),(3,4),(3,8),(4,11),(5,16),(5,19),(6,19),(9,10),(9,21),(10,18),(13,16)]),
 (1,6,[(0,11),(0,21),(1,6),(1,19),(3,4),(3,16),(4,11),(5,13),(5,19),(6,20),(9,18),(9,21),(10,14),(10,18),(13,16),(14,20)]),
 (1,6,[(0,11),(0,21),(2,7),(2,13),(4,11),(4,12),(5,13),(5,19),(6,19),(6,20),(7,15),(9,10),(9,21),(10,14),(12,15),(14,20)]),
 (1,3,[(0,11),(0,21),(11,12),(12,15),(14,17),(14,20),(15,17),(20,21)]),
 (1,2,[(1,6),(1,8),(3,8),(3,16),(5,13),(5,19),(6,19),(13,16)]),
 (1,6,[(1,8),(1,19),(3,4),(3,8),(4,11),(6,19),(6,20),(9,18),(9,21),(10,14),(10,18),(11,12),(12,15),(14,17),(15,17),(20,21)]),
 (1,6,[(2,7),(2,13),(3,4),(3,16),(4,12),(7,15),(12,15),(13,16)]),
 (1,3,[(2,7),(2,18),(7,15),(9,10),(9,18),(10,14),(14,17),(15,17)]),
 (1,6,[(2,7),(2,18),(7,17),(9,18),(9,21),(14,17),(14,20),(20,21)]),
]
E22 = sorted(tuple(sorted(e)) for e in QA22)
po2_22 = set(cyc_enum(22, E22, {8, 16}, 16))
v = verify_cert(22, E22, CERT22, 12, po2_22)
assert v == Fraction(25, 2) and v > 12, v
print(f"(a) QA22 carrier: fractional packing certificate value {v} > m=12 "
      f"-> L1-infeasible at the LP level (integer nu<=2 never fired)")

G26 = [(0,19),(0,21),(0,22),(1,5),(1,6),(1,8),(2,7),(2,9),(2,18),(3,8),
 (3,10),(3,16),(4,11),(4,12),(4,13),(5,6),(5,16),(6,20),(7,15),(7,17),
 (8,10),(9,14),(9,18),(10,18),(11,12),(11,21),(12,15),(13,16),(13,19),
 (14,24),(14,25),(15,17),(17,24),(19,21),(20,22),(20,23),(22,23),
 (23,25),(24,25)]
CERT26 = [
 (1,2,[(0,19),(0,22),(5,6),(5,16),(6,20),(13,16),(13,19),(20,22)]),
 (1,4,[(0,21),(0,22),(3,10),(3,16),(4,12),(4,13),(9,14),(9,18),(10,18),(11,12),(11,21),(13,16),(14,24),(22,23),(23,25),(24,25)]),
 (1,4,[(0,21),(0,22),(1,6),(1,8),(2,7),(2,18),(6,20),(7,17),(8,10),(10,18),(11,12),(11,21),(12,15),(15,17),(20,23),(22,23)]),
 (1,8,[(1,5),(1,6),(2,7),(2,9),(3,10),(3,16),(5,16),(6,20),(7,17),(9,18),(10,18),(14,24),(14,25),(17,24),(20,23),(23,25)]),
 (1,8,[(1,5),(1,8),(2,9),(2,18),(4,12),(4,13),(5,16),(7,15),(7,17),(8,10),(9,14),(10,18),(12,15),(13,16),(14,24),(17,24)]),
 (1,8,[(1,6),(1,8),(3,8),(3,16),(4,12),(4,13),(6,20),(7,15),(7,17),(12,15),(13,16),(14,24),(14,25),(17,24),(20,23),(23,25)]),
 (1,8,[(2,7),(2,18),(7,15),(9,14),(9,18),(14,24),(15,17),(17,24)]),
 (3,8,[(2,7),(2,9),(7,15),(9,14),(14,25),(15,17),(17,24),(24,25)]),
 (1,8,[(2,7),(2,18),(7,17),(9,14),(9,18),(14,25),(17,24),(24,25)]),
 (1,2,[(0,19),(0,21),(19,21)]),
 (1,2,[(1,5),(1,6),(5,6)]),
 (1,4,[(1,5),(1,8),(3,8),(3,16),(5,16)]),
 (3,8,[(2,9),(2,18),(9,18)]),
 (5,8,[(3,8),(3,10),(8,10)]),
 (1,2,[(4,11),(4,12),(11,12)]),
 (1,2,[(4,11),(4,13),(11,21),(13,19),(19,21)]),
 (1,4,[(7,15),(7,17),(15,17)]),
 (1,4,[(14,24),(14,25),(24,25)]),
 (1,2,[(20,22),(20,23),(22,23)]),
]
E26 = sorted(tuple(sorted(e)) for e in G26)
po2_26 = cyc_enum(26, E26, {8, 16}, 16)
assert (sum(1 for c in po2_26 if len(c) == 8), len(po2_26)) == (4, 285)
X26 = {(0,22),(2,7),(2,9),(2,18),(4,13),(5,16),(6,20),(9,14),(11,21),
       (13,16),(13,19),(14,24),(17,24),(24,25)}
assert all(len(c & X26) >= 5 for c in po2_26)      # L1-pass re-verified
v = verify_cert(26, E26, CERT26, 14, set(po2_26))
assert v == Fraction(57, 4) and v > 14, v
print(f"(b) n=26 L1-pass (c8=4): mixed LP certificate value {v} > m=14 "
      f"-> NO 5-cover is a cotree, fractionally certified (triangle "
      f"starvation as explicit dual weights)")
CHECK -->

<!-- CHECK
# frac_starvation_l1pass CHECK (draft): (a) pinned rational dual certificate
# that the QA22 carrier is L1-infeasible at the LP level: 11 PO2 cycles with
# weights y, per-edge load <= 1, 5*sum(y) = 25/2 > m = 12 (the DEAD integer
# packing bound gives only 5*nu = 10 <= 12 -- the fractional refinement
# fires where the integer one never did).  (b) pinned MIXED certificate on
# the R56 n=26 L1-pass (CHECK-10 graph): 9 PO2 cycles + 10 short cycles,
# value 57/4 > m = 14 => no 5-cover is a cotree, LP-certified (replacing
# the out-of-block SAT/CEGAR certificate for THIS graph).  (c) killable
# probe of the lemma "L1-pass & c8 >= 2 => Lambda(G) > m": the first 3
# C4-free 5-coverable c8>=2 double-subdivision+join children of the n=24
# carrier get a float LP + exact rational rounding; a child whose certified
# value is <= m FALSIFIES the lemma.  Boundary fact (not asserted here,
# session-verified): the n=24 carrier itself (c8=1) has Lambda = 167/14 < 13
# -- the c8 >= 2 hypothesis is necessary.
from fractions import Fraction
from itertools import combinations

def cyc_enum(n, edges, lens, Lmax):
    adj = [[] for _ in range(n)]
    for u, v in edges: adj[u].append(v); adj[v].append(u)
    out = []; path = [0]*(Lmax+1); onpath = [False]*n
    def rec(s, u, ln):
        for w in adj[u]:
            if w == s and ln >= 3:
                if ln in lens and path[1] < path[ln-1]:
                    out.append(frozenset(
                        [tuple(sorted((path[i], path[i+1]))) for i in range(ln-1)]
                        + [tuple(sorted((path[ln-1], s)))]))
            elif w > s and not onpath[w] and ln < Lmax:
                onpath[w] = True; path[ln] = w
                rec(s, w, ln+1)
                onpath[w] = False
    for s in range(n):
        onpath[s] = True; path[0] = s
        rec(s, s, 1); onpath[s] = False
    return out

def verify_cert(n, edges, cert, m, po2set):
    # cert: list of (num, den, [edge,...]); PO2 members weighted 5, short 1
    load = {e: Fraction(0) for e in edges}
    val = Fraction(0)
    for num, den, ce in cert:
        w = Fraction(num, den); ce = frozenset(tuple(sorted(e)) for e in ce)
        assert all(e in load for e in ce)
        deg = {}
        for u, v in ce: deg[u] = deg.get(u, 0)+1; deg[v] = deg.get(v, 0)+1
        assert all(d == 2 for d in deg.values())          # disjoint-cycle union suffices for validity of the dual row only if a SINGLE cycle; check connectivity:
        aj = {}
        for u, v in ce: aj.setdefault(u, []).append(v); aj.setdefault(v, []).append(u)
        st = next(iter(deg)); seen = {st}; stk = [st]
        while stk:
            u = stk.pop()
            for w2 in aj[u]:
                if w2 not in seen: seen.add(w2); stk.append(w2)
        assert len(seen) == len(deg), "not a single cycle"
        if len(ce) in (8, 16) and ce in po2set: coef = 5
        else:
            assert len(ce) <= 7, "short constraint too long"
            coef = 1
        val += coef * w
        for e in ce: load[e] += w
    assert max(load.values()) <= 1, "dual infeasible"
    return val

# Pinned children + rational certificates, generated 2026-08-23 from draft_check.py part (c) search
CHILDREN = [
  # subdiv(0, 22)+(2, 7): c8=6, Lambda >= 103/7
  ((0, 22), (2, 7), 6, 103, 7, [(1, 14, [(0, 19), (0, 21), (4, 11), (4, 12), (5, 6), (5, 16), (6, 20), (11, 21), (12, 15), (13, 16), (13, 19), (14, 17), (14, 23), (15, 17), (20, 22), (22, 23)]), (1, 7, [(0, 19), (0, 24), (1, 5), (1, 8), (3, 8), (3, 16), (4, 11), (4, 13), (5, 6), (6, 20), (11, 21), (13, 16), (19, 21), (20, 23), (22, 23), (22, 24)]), (3, 14, [(0, 19), (0, 24), (1, 6), (1, 8), (3, 10), (3, 16), (4, 11), (4, 13), (6, 20), (8, 10), (11, 21), (13, 16), (19, 21), (20, 23), (22, 23), (22, 24)]), (1, 14, [(0, 19), (0, 24), (1, 6), (1, 8), (3, 8), (3, 16), (4, 12), (4, 13), (6, 20), (11, 12), (11, 21), (13, 16), (19, 21), (20, 23), (22, 23), (22, 24)]), (3, 7, [(0, 21), (0, 24), (7, 15), (7, 25), (11, 12), (11, 21), (12, 15), (24, 25)]), (1, 7, [(1, 5), (1, 8), (3, 10), (3, 16), (4, 12), (4, 13), (5, 6), (6, 20), (8, 10), (12, 15), (13, 16), (14, 17), (14, 23), (15, 17), (20, 22), (22, 23)]), (1, 14, [(1, 5), (1, 8), (3, 8), (3, 16), (4, 11), (4, 13), (5, 6), (6, 20), (11, 12), (12, 15), (13, 16), (14, 17), (14, 23), (15, 17), (20, 22), (22, 23)]), (1, 14, [(1, 5), (1, 6), (4, 11), (4, 12), (5, 16), (6, 20), (11, 21), (12, 15), (13, 16), (13, 19), (14, 17), (14, 23), (15, 17), (19, 21), (20, 22), (22, 23)]), (1, 14, [(1, 6), (1, 8), (2, 9), (2, 25), (4, 12), (4, 13), (5, 6), (5, 16), (7, 17), (7, 25), (8, 10), (9, 18), (10, 18), (12, 15), (13, 16), (15, 17)]), (1, 14, [(1, 6), (1, 8), (2, 9), (2, 18), (3, 8), (3, 10), (4, 12), (4, 13), (5, 6), (5, 16), (9, 14), (10, 18), (12, 15), (13, 16), (14, 17), (15, 17)]), (1, 14, [(1, 6), (1, 8), (3, 10), (3, 16), (4, 12), (4, 13), (6, 20), (7, 15), (7, 17), (8, 10), (12, 15), (13, 16), (14, 17), (14, 23), (20, 22), (22, 23)]), (3, 7, [(2, 9), (2, 25), (9, 14), (14, 23), (20, 22), (20, 23), (22, 24), (24, 25)]), (3, 7, [(2, 18), (2, 25), (7, 15), (7, 25), (9, 14), (9, 18), (14, 17), (15, 17)]), (1, 14, [(2, 18), (2, 25), (9, 14), (9, 18), (14, 23), (22, 23), (22, 24), (24, 25)]), (1, 14, [(7, 17), (7, 25), (14, 17), (14, 23), (20, 22), (20, 23), (22, 24), (24, 25)]), (1, 2, [(0, 19), (0, 21), (19, 21)]), (3, 7, [(1, 5), (1, 6), (5, 6)]), (1, 7, [(1, 5), (1, 8), (3, 8), (3, 16), (5, 16)]), (3, 7, [(2, 9), (2, 18), (9, 18)]), (1, 2, [(3, 8), (3, 10), (8, 10)]), (3, 7, [(4, 11), (4, 12), (11, 12)]), (1, 14, [(7, 15), (7, 17), (15, 17)]), (1, 14, [(20, 22), (20, 23), (22, 23)])]),
  # subdiv(1, 8)+(12, 15): c8=5, Lambda >= 59/4
  ((1, 8), (12, 15), 5, 59, 4, [(1, 12, [(0, 19), (0, 21), (3, 10), (3, 16), (4, 11), (4, 12), (9, 14), (9, 18), (10, 18), (11, 21), (12, 25), (13, 16), (13, 19), (14, 17), (15, 17), (15, 25)]), (1, 4, [(0, 19), (0, 22), (5, 6), (5, 16), (6, 20), (13, 16), (13, 19), (20, 22)]), (1, 12, [(0, 19), (0, 22), (2, 7), (2, 9), (4, 11), (4, 12), (7, 17), (9, 14), (11, 21), (12, 25), (14, 23), (15, 17), (15, 25), (19, 21), (20, 22), (20, 23)]), (1, 12, [(0, 19), (0, 22), (1, 6), (1, 24), (3, 8), (3, 16), (4, 12), (4, 13), (6, 20), (8, 24), (11, 12), (11, 21), (13, 16), (19, 21), (20, 23), (22, 23)]), (1, 12, [(0, 19), (0, 22), (3, 10), (3, 16), (4, 12), (4, 13), (9, 14), (9, 18), (10, 18), (11, 12), (11, 21), (13, 16), (14, 23), (19, 21), (20, 22), (20, 23)]), (1, 12, [(0, 21), (0, 22), (2, 7), (2, 9), (3, 10), (3, 16), (4, 11), (4, 13), (7, 17), (9, 18), (10, 18), (11, 21), (13, 16), (14, 17), (14, 23), (22, 23)]), (1, 12, [(0, 21), (0, 22), (1, 5), (1, 24), (3, 10), (3, 16), (5, 16), (9, 14), (9, 18), (10, 18), (11, 12), (11, 21), (12, 25), (14, 23), (22, 23), (24, 25)]), (1, 4, [(0, 21), (0, 22), (2, 7), (2, 9), (4, 11), (4, 13), (7, 17), (9, 14), (11, 12), (12, 25), (13, 19), (14, 23), (15, 17), (15, 25), (19, 21), (22, 23)]), (1, 12, [(0, 21), (0, 22), (2, 7), (2, 9), (4, 12), (4, 13), (7, 17), (9, 14), (12, 25), (13, 19), (14, 23), (15, 17), (15, 25), (19, 21), (20, 22), (20, 23)]), (1, 4, [(1, 5), (1, 24), (4, 12), (4, 13), (5, 16), (12, 25), (13, 16), (24, 25)]), (5, 12, [(1, 6), (1, 24), (3, 10), (3, 16), (5, 6), (5, 16), (8, 10), (8, 24)]), (1, 6, [(1, 6), (1, 24), (3, 10), (3, 16), (4, 11), (4, 13), (6, 20), (9, 14), (9, 18), (10, 18), (11, 12), (12, 25), (13, 16), (14, 23), (20, 23), (24, 25)]), (1, 2, [(2, 7), (2, 18), (7, 15), (8, 10), (8, 24), (10, 18), (15, 25), (24, 25)]), (5, 12, [(0, 19), (0, 21), (19, 21)]), (1, 3, [(1, 5), (1, 6), (5, 6)]), (1, 2, [(2, 9), (2, 18), (9, 18)]), (1, 12, [(3, 8), (3, 10), (8, 10)]), (1, 3, [(4, 11), (4, 12), (11, 12)]), (1, 2, [(7, 15), (7, 17), (15, 17)]), (1, 2, [(20, 22), (20, 23), (22, 23)])]),
  # subdiv(2, 7)+(6, 20): c8=6, Lambda >= 103/7
  ((2, 7), (6, 20), 6, 103, 7, [(1, 14, [(0, 19), (0, 21), (2, 9), (2, 24), (3, 10), (3, 16), (7, 17), (7, 24), (9, 18), (10, 18), (11, 12), (11, 21), (12, 15), (13, 16), (13, 19), (15, 17)]), (1, 14, [(0, 19), (0, 21), (3, 10), (3, 16), (4, 11), (4, 12), (7, 15), (7, 17), (9, 14), (9, 18), (10, 18), (11, 21), (12, 15), (13, 16), (13, 19), (14, 17)]), (1, 14, [(0, 19), (0, 22), (1, 6), (1, 8), (3, 8), (3, 10), (5, 6), (5, 16), (9, 14), (9, 18), (10, 18), (13, 16), (13, 19), (14, 23), (20, 22), (20, 23)]), (1, 7, [(0, 19), (0, 22), (1, 5), (1, 8), (3, 8), (3, 16), (4, 11), (4, 13), (5, 6), (6, 25), (11, 21), (13, 16), (19, 21), (20, 23), (20, 25), (22, 23)]), (3, 14, [(0, 19), (0, 22), (3, 10), (3, 16), (4, 12), (4, 13), (9, 14), (9, 18), (10, 18), (11, 12), (11, 21), (13, 16), (14, 23), (19, 21), (20, 22), (20, 23)]), (1, 14, [(0, 21), (0, 22), (2, 9), (2, 18), (3, 8), (3, 16), (4, 11), (4, 13), (8, 10), (9, 14), (10, 18), (11, 21), (13, 16), (14, 23), (20, 22), (20, 23)]), (1, 14, [(0, 21), (0, 22), (1, 5), (1, 8), (3, 10), (3, 16), (4, 11), (4, 13), (5, 6), (6, 25), (8, 10), (11, 21), (13, 16), (20, 23), (20, 25), (22, 23)]), (3, 14, [(0, 21), (0, 22), (1, 5), (1, 8), (3, 8), (3, 16), (4, 12), (4, 13), (5, 6), (6, 25), (11, 12), (11, 21), (13, 16), (20, 23), (20, 25), (22, 23)]), (1, 14, [(0, 21), (0, 22), (1, 5), (1, 8), (3, 8), (3, 10), (5, 16), (9, 14), (9, 18), (10, 18), (13, 16), (13, 19), (14, 23), (19, 21), (20, 22), (20, 23)]), (3, 7, [(1, 6), (1, 8), (2, 18), (2, 24), (6, 25), (8, 10), (10, 18), (24, 25)]), (1, 14, [(2, 9), (2, 24), (9, 14), (14, 23), (20, 22), (20, 25), (22, 23), (24, 25)]), (3, 7, [(2, 18), (2, 24), (7, 15), (7, 24), (9, 14), (9, 18), (14, 17), (15, 17)]), (1, 14, [(7, 15), (7, 24), (14, 17), (14, 23), (15, 17), (20, 23), (20, 25), (24, 25)]), (3, 7, [(7, 17), (7, 24), (14, 17), (14, 23), (20, 22), (20, 25), (22, 23), (24, 25)]), (3, 7, [(0, 19), (0, 21), (19, 21)]), (1, 2, [(1, 5), (1, 6), (5, 6)]), (1, 14, [(2, 9), (2, 18), (9, 18)]), (3, 7, [(3, 8), (3, 10), (8, 10)]), (1, 2, [(4, 11), (4, 12), (11, 12)]), (1, 7, [(4, 11), (4, 13), (11, 21), (13, 19), (19, 21)]), (3, 7, [(7, 15), (7, 17), (15, 17)]), (1, 14, [(20, 22), (20, 23), (22, 23)])]),
]

# Verify each pinned child: reconstruct from QA24 by double subdivision,
# no C4, PO2 census matches, certificate is exact rational and > m = 14.
QA24 = [(0,19),(0,21),(0,22),(1,5),(1,6),(1,8),(2,7),(2,9),(2,18),(3,8),
 (3,10),(3,16),(4,11),(4,12),(4,13),(5,6),(5,16),(6,20),(7,15),(7,17),
 (8,10),(9,14),(9,18),(10,18),(11,12),(11,21),(12,15),(13,16),(13,19),
 (14,17),(14,23),(15,17),(19,21),(20,22),(20,23),(22,23)]
E24 = sorted(tuple(sorted(e)) for e in QA24)
for e1, e2, c8_exp, vnum, vden, cert in CHILDREN:
    ch = [e for e in E24 if e not in (e1, e2)]
    ch += [(e1[0], 24), (e1[1], 24), (e2[0], 25), (e2[1], 25), (24, 25)]
    ch = sorted(tuple(sorted(e)) for e in ch)
    assert not cyc_enum(26, ch, {4}, 4), (e1, e2)          # C4-free
    po2 = cyc_enum(26, ch, {8, 16}, 16)
    c8 = sum(1 for c in po2 if len(c) == 8)
    assert c8 == c8_exp and c8 >= 2, (e1, e2, c8)
    cert = [(a, b, [tuple(e) for e in ce]) for a, b, ce in cert]
    val = verify_cert(26, ch, cert, 14, set(po2))
    assert val == Fraction(vnum, vden) and val > 14, (e1, e2, val)
    print(f"child subdiv{e1}+{e2}: c8={c8}, certified Lambda >= {val} > 14")
print("all 3 pinned subdivision children LP-certified above budget m=14")

CHECK -->


## DISPROVED (R58, session s_0823-080606-3598) — the designated falsifier sweep killed the claim same-day

The R58 sweep regenerated the complete organic L1-pass population (all
630 double-subdivision children of QA24; census exactly matches R56's
row: 550 C4-excluded, 30 L1-infeasible, 50 L1-passes). Of the 46
L1-passes with $c_8 \ge 2$: 27 satisfy $\Lambda > 14$ (exact rational
certificates), but **19 have exact LP optimum $\Lambda < 14 = m$** —
computed by exact rational simplex (Bland's rule, Fraction arithmetic)
and INDEPENDENTLY certified by explicit feasible DUAL covers (below).
The $c_8$ boundary is not clean: falsifiers have $c_8 \in \{2,3,4\}$
(9/8/2), certified have $c_8 \in \{3,4,5,6,8\}$ (2/11/7/5/2) — overlap
at $c_8 \in \{3,4\}$, so NO $c_8$ threshold rescues the claim.

**Pinned counterexample 1** — subdiv$(12,15)+(13,16)$ of QA24
($n = 26$, $c_8 = 2$, C4-free, 203 PO2 cycles, 22 short cycles):

- Hypothesis holds (L1-pass): the 14-edge set
  $X = \{(0,22),(1,8),(2,7),(3,16),(6,20),(10,18),(11,21),(12,24),
  (13,19),(13,25),(14,23),(15,24),(16,25),(24,25)\}$
  has $|c \cap X| \ge 5$ for all 203 PO2 cycles.
- Conclusion fails: the edge weighting $u$ pinned in the CHECK below is
  feasible for the covering dual ($\sum_{e \in c} u_e \ge 5$ per PO2
  cycle, $\ge 1$ per cycle $\le 7$) with
  $\sum_e u_e = 27/2 < 14$, so by weak duality EVERY packing $(y,z)$
  has value $\le 27/2$: $\Lambda = 27/2 < m$.

**Pinned counterexample 2** — subdiv$(0,22)+(10,18)$ ($c_8 = 4$,
225 PO2 cycles): 5-cover exists (pinned in CHECK), dual cover sums to
$736/53 < 14$. Kills any retreat to $c_8 \ge 4$.

**What survives.** The certificate DIRECTION is untouched: $\Lambda > m$
still proves the L2 block wherever it holds, and 27/46 of the organic
family (plus QA22 at the L1 layer and the pinned R56 $n = 26$ L1-pass)
carry exact certificates. What died is the claim that the fractional
mechanism covers the whole $c_8 \ge 2$ stratum: **the integral
obstruction (pure integrality gap, as at QA24) extends to 19/46 of the
organic L1-pass family.** All 19 falsifiers are quad-death-free anyway
— they are among R56's 61 L1-passes, each with a complete CEGAR UNSAT
certificate at L2 — so no quad-dead candidate emerges; what fails is
only the LP EXPLANATION of the block. The refined question (what
invariant separates the 27 LP-certifiable children from the 19
integral ones) is follow-up work under a NEW lemma id, and the benched
triangle-pocket integral-discharging program (ideation P2) is promoted:
the integral mechanism is the DOMINANT one on this family, not a
$c_8 \le 1$ corner case.

<!-- CHECK
# frac_starvation_l1pass DISPROOF certificate (R58): pinned falsifier 1
# subdiv(12,15)+(13,16) of QA24. Verifies from scratch, exact arithmetic:
# (i) child is C4-free with c8 = 2 (hypothesis stratum), (ii) the pinned
# 14-edge X is a 5-cover of ALL PO2 cycles (hypothesis: L1-pass),
# (iii) the pinned dual u is feasible (>= 5 per PO2 cycle, >= 1 per
# cycle <= 7) with sum = 27/2 < 14, so Lambda <= 27/2 < m by weak
# duality and the lemma's conclusion FAILS. This CHECK passing = the
# disproof is machine-verified (lemma status: disproved is correct).
from fractions import Fraction

def cyc_enum(n, edges, lens, Lmax):
    adj = [[] for _ in range(n)]
    for u, v in edges: adj[u].append(v); adj[v].append(u)
    out = []; path = [0]*(Lmax+1); onpath = [False]*n
    def rec(s, u, ln):
        for w in adj[u]:
            if w == s and ln >= 3:
                if ln in lens and path[1] < path[ln-1]:
                    out.append(frozenset(
                        [tuple(sorted((path[i], path[i+1]))) for i in range(ln-1)]
                        + [tuple(sorted((path[ln-1], s)))]))
            elif w > s and not onpath[w] and ln < Lmax:
                onpath[w] = True; path[ln] = w
                rec(s, w, ln+1)
                onpath[w] = False
    for s in range(n):
        onpath[s] = True; path[0] = s
        rec(s, s, 1); onpath[s] = False
    return out

QA24 = [(0,19),(0,21),(0,22),(1,5),(1,6),(1,8),(2,7),(2,9),(2,18),(3,8),
 (3,10),(3,16),(4,11),(4,12),(4,13),(5,6),(5,16),(6,20),(7,15),(7,17),
 (8,10),(9,14),(9,18),(10,18),(11,12),(11,21),(12,15),(13,16),(13,19),
 (14,17),(14,23),(15,17),(19,21),(20,22),(20,23),(22,23)]
E24 = sorted(tuple(sorted(e)) for e in QA24)
e1, e2 = (12,15), (13,16)
ch = [e for e in E24 if e not in (e1, e2)]
ch += [(e1[0],24),(e1[1],24),(e2[0],25),(e2[1],25),(24,25)]
ch = sorted(tuple(sorted(e)) for e in ch)
assert not cyc_enum(26, ch, {4}, 4)
po2 = cyc_enum(26, ch, {8,16}, 16)
assert sum(1 for c in po2 if len(c) == 8) == 2 and len(po2) == 203
short = cyc_enum(26, ch, {3,4,5,6,7}, 7)
assert len(short) == 22

X = {(0,22),(1,8),(2,7),(3,16),(6,20),(10,18),(11,21),(12,24),(13,19),
     (13,25),(14,23),(15,24),(16,25),(24,25)}
assert len(X) == 14 and X <= set(ch)
assert all(len(c & X) >= 5 for c in po2)   # hypothesis: 5-coverable, c8 >= 2

U = {
  (0,19): Fraction(1,2),
  (0,21): Fraction(1,2),
  (0,22): Fraction(1,4),
  (1,5): Fraction(1,4),
  (1,6): Fraction(1,2),
  (1,8): Fraction(1,4),
  (2,7): Fraction(1,4),
  (2,9): Fraction(1,2),
  (2,18): Fraction(1,4),
  (3,8): Fraction(1,2),
  (3,10): Fraction(1,4),
  (4,11): Fraction(1,2),
  (4,12): Fraction(1,2),
  (5,6): Fraction(1,4),
  (6,20): Fraction(1,4),
  (7,15): Fraction(1,2),
  (7,17): Fraction(1,4),
  (8,10): Fraction(1,4),
  (9,18): Fraction(1,4),
  (10,18): Fraction(1,2),
  (11,21): Fraction(1,2),
  (12,24): Fraction(1,1),
  (13,25): Fraction(3,2),
  (14,23): Fraction(3,4),
  (15,17): Fraction(1,4),
  (15,24): Fraction(1,4),
  (20,22): Fraction(1,4),
  (20,23): Fraction(1,4),
  (22,23): Fraction(1,2),
  (24,25): Fraction(1,1),
}
tot = sum(U.values())
assert tot == Fraction(27,2) and tot < 14
assert set(U) <= set(ch)
for c in po2:
    assert sum(U.get(e, Fraction(0)) for e in c) >= 5
for D in short:
    assert sum(U.get(e, Fraction(0)) for e in D) >= 1
print("DISPROOF verified: L1-pass child with c8=2 has Lambda <= 27/2 < 14")
CHECK -->

<!-- CHECK
# frac_starvation_l1pass DISPROOF certificate (R58): pinned falsifier 2
# subdiv(0,22)+(10,18), c8 = 4 — kills any c8-threshold retreat below 5.
from fractions import Fraction

def cyc_enum(n, edges, lens, Lmax):
    adj = [[] for _ in range(n)]
    for u, v in edges: adj[u].append(v); adj[v].append(u)
    out = []; path = [0]*(Lmax+1); onpath = [False]*n
    def rec(s, u, ln):
        for w in adj[u]:
            if w == s and ln >= 3:
                if ln in lens and path[1] < path[ln-1]:
                    out.append(frozenset(
                        [tuple(sorted((path[i], path[i+1]))) for i in range(ln-1)]
                        + [tuple(sorted((path[ln-1], s)))]))
            elif w > s and not onpath[w] and ln < Lmax:
                onpath[w] = True; path[ln] = w
                rec(s, w, ln+1)
                onpath[w] = False
    for s in range(n):
        onpath[s] = True; path[0] = s
        rec(s, s, 1); onpath[s] = False
    return out

QA24 = [(0,19),(0,21),(0,22),(1,5),(1,6),(1,8),(2,7),(2,9),(2,18),(3,8),
 (3,10),(3,16),(4,11),(4,12),(4,13),(5,6),(5,16),(6,20),(7,15),(7,17),
 (8,10),(9,14),(9,18),(10,18),(11,12),(11,21),(12,15),(13,16),(13,19),
 (14,17),(14,23),(15,17),(19,21),(20,22),(20,23),(22,23)]
E24 = sorted(tuple(sorted(e)) for e in QA24)
e1, e2 = (0,22), (10,18)
ch = [e for e in E24 if e not in (e1, e2)]
ch += [(e1[0],24),(e1[1],24),(e2[0],25),(e2[1],25),(24,25)]
ch = sorted(tuple(sorted(e)) for e in ch)
assert not cyc_enum(26, ch, {4}, 4)
po2 = cyc_enum(26, ch, {8,16}, 16)
assert sum(1 for c in po2 if len(c) == 8) == 4 and len(po2) == 225
short = cyc_enum(26, ch, {3,4,5,6,7}, 7)

X = {(1,8),(2,7),(3,16),(4,13),(6,20),(9,14),(10,25),(12,15),(13,16),
     (13,19),(14,23),(18,25),(22,24),(24,25)}
assert len(X) == 14 and X <= set(ch)
assert all(len(c & X) >= 5 for c in po2)

U = {
  (0,19): Fraction(41,106),
  (0,21): Fraction(27,106),
  (1,5): Fraction(18,53),
  (1,6): Fraction(19,53),
  (1,8): Fraction(4,53),
  (2,9): Fraction(20,53),
  (2,18): Fraction(22,53),
  (3,8): Fraction(19,53),
  (3,10): Fraction(16,53),
  (3,16): Fraction(12,53),
  (4,11): Fraction(20,53),
  (4,12): Fraction(16,53),
  (5,6): Fraction(16,53),
  (7,15): Fraction(20,53),
  (7,17): Fraction(16,53),
  (8,10): Fraction(18,53),
  (9,14): Fraction(17,53),
  (9,18): Fraction(11,53),
  (10,25): Fraction(119,106),
  (11,12): Fraction(17,53),
  (13,16): Fraction(127,106),
  (13,19): Fraction(14,53),
  (14,23): Fraction(99,106),
  (15,17): Fraction(17,53),
  (18,25): Fraction(7,53),
  (19,21): Fraction(19,53),
  (20,22): Fraction(26,53),
  (20,23): Fraction(16,53),
  (22,23): Fraction(11,53),
  (22,24): Fraction(59,53),
  (24,25): Fraction(3,2),
}
tot = sum(U.values())
assert tot == Fraction(736,53) and tot < 14
assert set(U) <= set(ch)
for c in po2:
    assert sum(U.get(e, Fraction(0)) for e in c) >= 5
for D in short:
    assert sum(U.get(e, Fraction(0)) for e in D) >= 1
print("DISPROOF verified: L1-pass child with c8=4 has Lambda <= 736/53 < 14")
CHECK -->
