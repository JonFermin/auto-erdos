---
id: c5_rigidity_c8free
status: proved
depends_on: []
discharged_by_round: 57
introduced_at_round: 57
---

# Lemma `c5_rigidity_c8free` (5-cycle rigidity under $C_8$-freeness)

First rung of the criticality/witness-supply program (Q80, Section 97):
in the environment every minimal EGC counterexample lives in ($C_4$-free
and $C_8$-free by definition of counterexample), short witness cycles
are rigidly constrained. This lemma is unconditional graph theory — it
mentions no counterexample, no tree, no covering.

**Lemma.** Let $G$ be a cubic (3-regular simple) graph with girth
$\ge 5$ and no cycle of length $8$. Then:

1. **(i)** any two distinct $5$-cycles of $G$ share exactly $0$ or
   exactly $2$ edges;
2. **(ii)** every edge of $G$ lies on at most $2$ five-cycles, and if an
   edge $e$ lies on two $5$-cycles $C, C'$, then $C$ and $C'$ share $e$
   and exactly one further edge, adjacent to $e$.

*Remark (sharpness).* The Petersen graph (girth 5, every edge on four
$5$-cycles, two $5$-cycles often sharing exactly one edge) shows both
conclusions fail once $C_8$'s are allowed — and indeed Petersen contains
$8$-cycles, as it must. The CHECK below verifies this anchor and
stress-tests the contrapositive on random cubic graphs.

## Proof

Throughout, cycles are edge sets when convenient; the symmetric
difference of two cycles is an even subgraph (every vertex has even
degree), and every nonempty even subgraph decomposes into edge-disjoint
simple cycles, each of length $\ge$ girth $\ge 5$.

**(i).** Let $C_1 \ne C_2$ be $5$-cycles sharing $p$ edges,
$D = C_1 \triangle C_2$, $|D| = 10 - 2p$.

- $p = 5$ forces $C_1 = C_2$ (a $5$-cycle is determined by its edge
  set): excluded.
- $p = 4$: $|D| = 2$, a nonempty even subgraph with $2 < 5$ edges —
  impossible.
- $p = 3$: $|D| = 4 < 5$ — impossible.
- $p = 1$: $|D| = 8$; a decomposition into cycles of length $\ge 5$
  summing to $8$ must be a single $8$-cycle — contradicting
  $C_8$-freeness.

So $p \in \{0, 2\}$. (Only $p = 1$ used $C_8$-freeness; $p \in \{3,4\}$
die under girth $\ge 5$ alone.)

**(ii).** Let $e = xy$, and let $u_1, u_2$ be the other neighbors of
$x$, $v_1, v_2$ the other neighbors of $y$ (distinct by simplicity;
girth $\ge 5$ makes all six vertices distinct — $u_i = v_j$ would give
the triangle $x u_i y$).

Any $5$-cycle through $e$ is $e$ plus a $4$-edge path
$x, u_i, w, v_j, y$: it leaves $x$ by some $u_i$, arrives at $y$ by
some $v_j$, and its middle vertex $w$ is a common neighbor of $u_i$ and
$v_j$. Call $(i, j)$ the **combo** of the cycle.

*Step 1: each combo carries at most one $5$-cycle.* Two distinct common
neighbors $w \ne w'$ of $u_i, v_j$ give the $4$-cycle
$u_i w v_j w' u_i$ — excluded by girth.

*Step 2: two $5$-cycles through $e$ with combos differing in both
coordinates ("diagonal" combos) share only $e$.* Let
$C = x u_1 w v_1 y$ and $C' = x u_2 w' v_2 y$ (after relabeling). Their
possible shared edges besides $e$: the $x$-edges $x u_1 \ne x u_2$ and
$y$-edges $v_1 y \ne v_2 y$ differ by assumption, so a further shared
edge must be a middle edge of both. Enumerate the coincidences (edges
as unordered pairs):

- $u_1 w = u_2 w'$: forces $u_1 = w', w = u_2$, so $u_1 u_2 = u_1 w \in
  E$, giving the triangle $x u_1 u_2$ — excluded.
- $u_1 w = w' v_2$ with $u_1 = w', w = v_2$: then $C'$ passes
  $u_2 u_1$ ($= u_2 w'$), again edge $u_1 u_2 \in E$ and triangle
  $x u_1 u_2$ — excluded. With $u_1 = v_2$: impossible
  ($u_1 = v_2$ is a common neighbor of $x$ and $y$, triangle).
- $w v_1 = u_2 w'$ with $w = u_2$: then $C$ passes $u_1 u_2$, triangle
  $x u_1 u_2$ — excluded. With $v_1 = u_2$: impossible (common neighbor
  of $x, y$).
- $w v_1 = w' v_2$: $v_1 \ne v_2$ forces $w = v_2, v_1 = w'$, so both
  $y v_1, y v_2$ and $v_1 v_2$ ($= w' v_2 = v_1 w$... explicitly:
  $w v_1 = v_2 v_1$) are edges — the triangle $y v_1 v_2$ — excluded.

So the diagonal pair shares exactly $e$, i.e. $p = 1$ — contradicting
**(i)**. Hence no two $5$-cycles through $e$ have diagonal combos.

*Step 3: conclusion.* The combos of the $5$-cycles through $e$ form a
diagonal-free subset of the $2 \times 2$ grid $\{1,2\}^2$. Any
$3$-subset of the grid contains a diagonal pair (removing one cell
kills at most one of the two diagonals), so at most $2$ five-cycles
pass through $e$ — and when there are two, their combos share a
coordinate, i.e. the cycles share the corresponding edge $x u_i$ or
$v_j y$ (adjacent to $e$) in addition to $e$; by (i) they share exactly
those two. $\blacksquare$

**Corollary (witness-supply cap, used by Section 97).** In any cubic
graph of girth $\ge 5$ with no $8$-cycle: each $5$-cycle uses $5$
edges and each edge lies on at most $2$ five-cycles by (ii), so
double-counting incidences, $5 \cdot \#C_5 \le 2|E| = 3n$, i.e.
$\#C_5 \le \lfloor 3n/5 \rfloor$, and the total number of (edge,
$5$-cycle) incidences is at most $3n$ — versus the $|E| = 3n/2$ edges
a Section 97 saturation argument must supply with witnesses.

*(Empirical note, R57 probes: the coexistence "girth $5$ but no
$C_8$" is rare — seeded random sampling at $n \le 16$ and short SA
found nothing — but NOT empty: a longer SA run (energy
$10^6 c_3 + 10^4 c_4 + c_8$, double-edge-swap moves) produced a cubic
graph at $n = 28$ with girth $5$, no $C_8$, and exactly five
$5$-cycles, pinned in CHECK 2 below. On it both conclusions are
realized tightly: two disjoint sharing pairs, each sharing exactly
$2$ adjacent edges, and an edge attaining the incidence cap $2$. The
graph has $c_6 = 12$, $c_7 = 12$, and contains a $C_{16}$ —
consistent with F3.)*

<!-- CHECK
# c5_rigidity_c8free CHECK 1 (deterministic, stdlib).
# (a) Petersen anchor: girth 5, an edge on >=3 five-cycles, two 5-cycles
#     sharing exactly one edge -> the graph MUST contain a C8 (it does).
# (b) contrapositive stress on seeded random cubic graphs: any violation
#     of (i)/(ii) is explained by a C3, C4, or C8; and p in {3,4} never
#     occurs under girth >= 5 alone (no C8-freeness needed).
import random

def adj_of(n, edges):
    a = [set() for _ in range(n)]
    for u, v in edges:
        a[u].add(v); a[v].add(u)
    return a

def cycles_of_length(adj, n, L):
    out = []
    for s in range(n):
        stack = [(s, (s,))]
        while stack:
            u, path = stack.pop()
            if len(path) == L:
                if s in adj[u] and path[1] < path[-1]:
                    out.append(path)
                continue
            for w in adj[u]:
                if w > s and w not in path:
                    stack.append((w, path + (w,)))
    return out

def edge_set(cyc):
    return frozenset(frozenset((cyc[i], cyc[(i + 1) % len(cyc)]))
                     for i in range(len(cyc)))

def rand_cubic(n, rng):
    for _ in range(500):
        stubs = [v for v in range(n) for _ in range(3)]
        rng.shuffle(stubs)
        E, ok = set(), True
        for i in range(0, 3 * n, 2):
            u, v = stubs[i], stubs[i + 1]
            if u == v or (min(u, v), max(u, v)) in E:
                ok = False
                break
            E.add((min(u, v), max(u, v)))
        if not ok:
            continue
        adj = adj_of(n, E)
        seen, stk = {0}, [0]
        while stk:
            u = stk.pop()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w); stk.append(w)
        if len(seen) == n:
            return sorted(E)
    return None

# (a) Petersen anchor
pet = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] \
    + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
pet = [tuple(sorted(e)) for e in pet]
padj = adj_of(10, pet)
assert not cycles_of_length(padj, 10, 3) and not cycles_of_length(padj, 10, 4)
pfives = [edge_set(c) for c in cycles_of_length(padj, 10, 5)]
assert len(pfives) == 12
assert max(sum(frozenset(e) in f for f in pfives) for e in pet) >= 3
assert any(len(pfives[i] & pfives[j]) == 1
           for i in range(len(pfives)) for j in range(i + 1, len(pfives)))
assert cycles_of_length(padj, 10, 8), "Petersen without C8: lemma machinery broken"

# (b) contrapositive stress
rng = random.Random(20260830)
tested = 0
for n in (10, 12, 14, 16):
    for s in range(8):
        E = rand_cubic(n, rng)
        if E is None:
            continue
        adj = adj_of(n, E)
        g3 = bool(cycles_of_length(adj, n, 3))
        g4 = bool(cycles_of_length(adj, n, 4))
        c8 = bool(cycles_of_length(adj, n, 8))
        fives = [edge_set(c) for c in cycles_of_length(adj, n, 5)]
        tested += 1
        viol = False
        for i in range(len(fives)):
            for j in range(i + 1, len(fives)):
                p = len(fives[i] & fives[j])
                if not g3 and not g4:
                    assert p not in (3, 4), f"p={p} under girth>=5 alone (n={n})"
                if p == 1:
                    viol = True
        if fives:
            for e in set().union(*fives):
                if sum(e in f for f in fives) >= 3:
                    viol = True
        if viol:
            assert g3 or g4 or c8, f"rigidity violated with no C3/C4/C8 (n={n} s={s})"
assert tested >= 20, "probe vacuous: too few cubic samples"
CHECK -->

<!-- CHECK
# c5_rigidity_c8free CHECK 2 (deterministic, stdlib): the pinned
# NON-VACUOUS instance — cubic, connected, girth 5, NO C8, five
# 5-cycles — must satisfy (i) and (ii) exactly as proved: every
# sharing pair shares exactly 2 edges, and no edge exceeds incidence 2.
E28 = [(0, 11), (0, 19), (0, 27), (1, 17), (1, 19), (1, 21), (2, 9), (2, 13),
       (2, 14), (3, 22), (3, 24), (3, 25), (4, 5), (4, 7), (4, 26), (5, 14),
       (5, 18), (6, 7), (6, 8), (6, 20), (7, 13), (8, 14), (8, 25), (9, 17),
       (9, 24), (10, 16), (10, 21), (10, 27), (11, 15), (11, 16), (12, 19),
       (12, 23), (12, 26), (13, 18), (15, 22), (15, 26), (16, 25), (17, 23),
       (18, 23), (20, 21), (20, 24), (22, 27)]
n = 28
adj = [set() for _ in range(n)]
for u, v in E28:
    adj[u].add(v); adj[v].add(u)
assert all(len(a) == 3 for a in adj), "pin not cubic"
seen, stk = {0}, [0]
while stk:
    u = stk.pop()
    for w in adj[u]:
        if w not in seen:
            seen.add(w); stk.append(w)
assert len(seen) == n, "pin not connected"

def cycles_of_length(L):
    out = []
    for s in range(n):
        stack = [(s, (s,))]
        while stack:
            u, path = stack.pop()
            if len(path) == L:
                if s in adj[u] and path[1] < path[-1]:
                    out.append(path)
                continue
            for w in adj[u]:
                if w > s and w not in path:
                    stack.append((w, path + (w,)))
    return out

assert not cycles_of_length(3) and not cycles_of_length(4), "pin girth < 5"
assert not cycles_of_length(8), "pin has a C8"
fives = cycles_of_length(5)
assert len(fives) == 5, f"pin c5 changed: {len(fives)}"
es = [frozenset(frozenset((c[i], c[(i + 1) % 5])) for i in range(5)) for c in fives]
share2 = 0
for i in range(len(es)):
    for j in range(i + 1, len(es)):
        p = len(es[i] & es[j])
        assert p in (0, 2), f"(i) FALSIFIED on pin: p={p}"
        if p == 2:
            share2 += 1
            a, b = sorted(es[i] & es[j], key=sorted)
            assert a & b, "sharing pair's two edges are not adjacent"
assert share2 == 2, f"pin sharing-pair count changed: {share2}"
inc = {}
for f in es:
    for e in f:
        inc[e] = inc.get(e, 0) + 1
assert max(inc.values()) == 2, "(ii) FALSIFIED on pin or cap not attained"
CHECK -->
