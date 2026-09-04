---
id: c8free_c16_floor
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 61
---

# Lemma `c8free_c16_floor` (open — Q81's binding question; R61 dual attack ran the falsification probes first)

**Claim.** Every connected cubic graph on $n$ vertices,
$24 \le n \le 32$, with no $C_4$ and no $C_8$, contains a $C_{16}$.

**Why this is THE question (Section 100 / Q81 coupling).** By
`criticality_edge_witness` + the R60 disproof of `pendant_9_cap`, no
cardinality ledger can close the criticality program at the
girth-$5$/$C_8$-free level: witness supply at length $9$ is total.
Scarcity, if it exists, must come from $C_{16}$-freeness. If
`c8free_c16_floor` holds on $30 \le n \le 32$ then the witness class
for the cubic criticality target is empty above Markström's verified
range ($n \le 29$, fact F3) at the next scale, since $C_{32}$ needs
$n \ge 32$: a cubic EGC counterexample on $30 \le n \le 31$ would be
exactly a $\{C_4, C_8, C_{16}\}$-free graph there. Conversely a
falsifier of this lemma at $n = 30$ (any girth) IS a complete EGC
counterexample, and a falsifier at $n \le 28$ contradicts F3 — the
verifier-bug tripwire. For $24 \le n \le 29$ the lemma is TRUE
unconditionally, being a restatement of Markström's exhaustive search
(F3): this range is retained in the claim as the sanity anchor.

## R61 falsification probes (all negative — the floor survives)

### (a) Truncation closure — the triangle-rich route is CLOSED at $n \in \{24, 30\}$ (rigorous)

The triangle truncation $T(H)$ of a cubic $H$ (replace each vertex by
a triangle, each original edge joining its two end-triangles) is cubic
on $n = 3|H|$; the only truncation orders in $[24, 32]$ are
$|H| = 8 \mapsto 24$ and $|H| = 10 \mapsto 30$.

**Lift-length arithmetic.** Every simple cycle of $T(H)$ is a triangle
or visits each triangle at most once (a second visit would need $4$ of
the triangle's $3$ spokes), hence projects to a simple cycle of $H$;
an $L$-cycle of $H$ lifts to cycles of length $L + s$ where each
visited triangle contributes $1$ or $2$ triangle-edges, so
$s \in [L, 2L]$ with all values realizable (choices independent per
vertex). Consequences: $T(H)$ NEVER has a $C_4$ ($4 = L + s$ needs
$L \le 4/3$); $T(H)$ has a $C_8$ iff $H$ has a $C_3$ or $C_4$
($8 - L \in [L, 2L] \iff 8/3 \le L \le 4$); $T(H)$ has a $C_{16}$ iff
$H$ has a cycle of length $6$, $7$ or $8$
($16 - L \in [L, 2L] \iff 16/3 \le L \le 8$).

So a truncation falsifier requires cubic $H$ with **no cycle of length
in $\{3, 4, 6, 7, 8\}$**.

- $|H| = 8$: exhaustively, ALL $19{,}320$ connected labeled cubic
  graphs on $8$ vertices contain a cycle of length in
  $\{3, 4, 6, 7, 8\}$ (CHECK 3, 1.4 s). No candidate.
- $|H| = 10$: $H$ needs girth $\ge 5$; exhaustive in-session
  enumeration (pruned DFS over labeled adjacency with incremental
  distance-$\ge 4$ edge filter) found exactly $30{,}240$ labeled cubic
  girth-$\ge 5$ graphs on $10$ vertices $= 10!/120$, every one with
  cycle census $(c_5, \dots, c_8) = (12, 10, 0, 15)$ — i.e. the
  Petersen graph and nothing else (its uniqueness as the $(3,5)$-cage,
  re-verified from scratch). Petersen has $C_6$ and $C_8$, so BOTH
  $C_{16}$ production routes fire. Directly: $T(\text{Petersen})$ has
  census $c_3 = 10$, $c_4 = c_5 = c_6 = c_7 = c_8 = 0$,
  $c_{16} = 165$, and the arithmetic predicts exactly
  $15 \cdot 1 + 10 \cdot \binom{6}{4} = 165$ (each $8$-cycle lifts to
  one all-direct $16$-cycle; each $6$-cycle to $\binom{6}{4}$
  four-detour $16$-cycles). CHECK 2 pins both the census and the
  identity.

Note $T(\text{Petersen})$ is a genuinely new boundary exemplar: a
$\{C_4, C_8\}$-free cubic graph at the EGC-critical order $n = 30$
that is NOT in the girth-$\ge 5$ class ($c_3 = 10$) — the lemma's
quantifier over all girths is not vacuous, and its $C_{16}$ count
$165$ is the smallest clean count any R61 probe reached.

### (b) Structured families are empty before $C_{16}$ is even tested

All $1{,}981$ graphs from three symmetric families at
$24 \le n \le 32$ — generalized Petersen $GP(m,k)$
($12 \le m \le 16$), cyclic theta-lifts $\theta(\mathbb{Z}_m; 0,a,b)$,
dihedral Cayley graphs $\mathrm{Cay}(D_m, \{r^i s, r^j s, r^k s\})$ —
contain a $C_4$ or a $C_8$: **zero** members of the
$\{C_4, C_8\}$-free class. Consistent with R54 (vertex-transitivity
excludes the class at $n = 22$); the class is intrinsically
asymmetric.

### (c) The class is rigid under local growth

Every one of the $609$ girth-$\ge 5$ H-extension children ($n = 30$)
of the R57 pin has $c_8 \ge 1$; every one of the $720$ girth-$\ge 5$
grandchildren ($n = 32$) of the best child has $c_8 \ge 2$. The known
$n = 28$ class member does not extend to a class member at $n = 30$ by
any single H-extension.

### (d) $C_{16}$ abundance at the known member

The R57 pin ($n = 28$, girth $5$, $C_8$-free) has exact long-cycle
census $c_9, \dots, c_{16} = 34, 56, 70, 120, 183, 348, 484,
\mathbf{614}$ — the same exponential-growth abundance pattern that
killed `pendant_9_cap` at length $9$. F3 promises $c_{16} \ge 1$
there; reality is $614$. A falsifier must fight this growth, not a
marginal count.

### (e) SA campaign (soft-energy hierarchical annealing, cyclic reheat)

Energy $10^4 c_3 [\text{g5}] + 2500\, c_4 + 900\, c_8 + c_{16}$ over
connected-cubic 2-opt moves, seeds from random cubic starts, from the
pin's best H-extension children, and from $T(\text{Petersen})$;
$2400$ s per worker. Best CLEAN ($c_4 = c_8 = 0$, plus $c_3 = 0$ for
g5) states reached — c16 floors observed:

| config | best clean $c_{16}$ | iters |
|---|---|---|
| $n=30$, girth $\ge 5$, warm (best child) | 755 | 215k |
| $n=30$, girth $\ge 5$, cold | 728 | 218k |
| $n=32$, girth $\ge 5$, warm | 781 | 195k |
| $n=30$, triangles allowed, cold | 210 | 366k |
| $n=30$, triangles allowed, warm from $T(\text{Petersen})$ | 165 | 431k |

Zero falsifiers across $\sim 10^6$ proposals. The triangles-allowed
chain independently converged toward truncation-like structure ($9$
triangles at its best state) — the valley whose floor (a) proves is
$> 0$ on the pure-truncation manifold, and whose observed bottom
($165$, at $T(\text{Petersen})$ itself) no chain went below. CHECK 4
pins the two strongest near-miss adjacencies and their censuses.

## Current obstacle / next move — the composition engine

The probes say the floor is real and high ($\ge 165$ observed clean
minimum at $n = 30$). The proof mechanism candidate found this round:
**on the pin, all $614$ $C_{16}$s are sym-diff compositions of two
shorter cycles**, and the sharpest shape is universal across every
known class member. Define a *share-$1$ pair* as two distinct cycles
sharing exactly one edge. Measured: every share-$1$ pair drawn from
$\{9,10\}$-cycles has single-cycle sym-diff (hence composes to a
$C_{16}$ when $9 \times 9$, $C_{17}$ when $9 \times 10$, $C_{18}$
when $10 \times 10$) on ALL FIVE known $\{C_4, C_8\}$-free graphs
tested — the R57 pin ($154 + 462 + 350$ pairs) and the four R61 SA
snapshots ($n = 30, 30, 32$ girth-$5$ and $n = 30$ triangle-rich):
$3{,}738 / 3{,}738$ pairs total, zero exceptions.

A share-$1$ pair fails to compose only if the two cycles share an
extra vertex $w$ (degree-$4$ point of the sym-diff). Writing the two
$8$-edge arcs through $w$ as $a_1 + a_2 = b_1 + b_2 = 8$, the four
sub-arc unions force closed walks of lengths $a_1 + b_1$,
$a_2 + b_2$ (summing to $16$) and $a_1 + b_2 + 1$, $a_2 + b_1 + 1$
(summing to $18$), each containing a cycle constrained by girth
$\ge 5$, $C_8$-freeness, and the `cycle_pair_sym_diff_exclusions`
table — a FINITE arithmetic case analysis (with degenerate-overlap
care), not an open-ended structure hunt.

First-order reconnaissance (in-session): with internally disjoint
arcs, requiring all four implied cycle lengths to lie in
$\{5, 6, 7\} \cup \{9, \ldots\}$ leaves $18$ surviving quadruples
$(a_1, a_2, b_1, b_2)$ (e.g. $(3,5,3,5) \to$ lengths $6, 10, 9, 9$) —
girth + $C_8$-freeness alone do NOT close the case. Every survivor
forces a $C_5$, $C_6$ or $C_7$ through $u$, $v$ or $w$, so the
second-order layer (`c5_rigidity_c8free`'s incidence cap, the
scarcity of short cycles, the exclusion table applied to the NEW
pairs) is where the proof must come from — or where a falsifying
configuration hides. Dual attack next round: CHECK-hunt a share-$1$
$+$ extra-vertex pair inside the $18$ windows on richer instances
BEFORE proving.

**R62 target `share1_c16_compose`**: cubic, girth $\ge 5$, no $C_8$
$\Rightarrow$ two distinct $9$-cycles sharing exactly one edge share
no other vertex. Corollary: a $C_{16}$-free class member has all
$9$-cycle pairs sharing $0$ or $\ge 2$ edges — in particular any two
$9$-cycles through a COMMON edge share $\ge 2$ edges, a per-edge
rigidity landing exactly where `pendant_9_cap` died unconditionally
(the pin's per-edge $9$-witness families realize share-$1$ freely; a
$C_{16}$-free member cannot). R60's $9$-abundance (which killed the
cardinality ledger) becomes the load that $C_{16}$-freeness cannot
carry. Then the counting layer: the pin
has $34 > n$ nine-cycles on $3n/2 = 42$ edges with per-edge incidence
up to $12$; how many pairwise-share-$\{0, 2^+\}$ $9$-cycles fit?

<!-- CHECK
# CHECK 1 — counter self-validation + R57 pin spectrum spot values.
# Pruned-DFS cycle counter (root = min vertex, distance pruning), the
# instrument every R61 probe relies on. K4 and Petersen censuses are
# textbook; the pin values c9=34 (R60) and c16=614 (R61) are pinned.
from collections import deque

def bfs_dist(adj, n, s):
    d = [n+1]*n; d[s] = 0; q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] > d[v] + 1:
                d[w] = d[v] + 1; q.append(w)
    return d

def count_cycles(adj, n, lengths):
    Lmax = max(lengths); want = set(lengths)
    counts = {L: 0 for L in want}
    for s in range(n):
        dist = bfs_dist(adj, n, s)
        stack = [(u, (1 << s) | (1 << u), 1) for u in adj[s] if u > s]
        while stack:
            v, mask, depth = stack.pop()
            for w in adj[v]:
                if w == s:
                    clen = depth + 1
                    if clen >= 3 and clen in want:
                        counts[clen] += 1
                    continue
                if w < s or (mask >> w) & 1:
                    continue
                nd = depth + 1
                if nd + dist[w] > Lmax:
                    continue
                if nd < Lmax:
                    stack.append((w, mask | (1 << w), nd))
    return {L: c // 2 for L, c in counts.items()}

adjK4 = [[1,2,3],[0,2,3],[0,1,3],[0,1,2]]
assert count_cycles(adjK4, 4, {3,4}) == {3: 4, 4: 3}
EP = [(i,(i+1)%5) for i in range(5)] + [(i,i+5) for i in range(5)] \
     + [(5+i,5+(i+2)%5) for i in range(5)]
adjP = [[] for _ in range(10)]
for a,b in EP: adjP[a].append(b); adjP[b].append(a)
cc = count_cycles(adjP, 10, {3,4,5,6,7,8,9,10})
assert cc == {3:0,4:0,5:12,6:10,7:0,8:15,9:20,10:0}, cc
E28 = [(0, 11), (0, 19), (0, 27), (1, 17), (1, 19), (1, 21), (2, 9), (2, 13),
       (2, 14), (3, 22), (3, 24), (3, 25), (4, 5), (4, 7), (4, 26), (5, 14),
       (5, 18), (6, 7), (6, 8), (6, 20), (7, 13), (8, 14), (8, 25), (9, 17),
       (9, 24), (10, 16), (10, 21), (10, 27), (11, 15), (11, 16), (12, 19),
       (12, 23), (12, 26), (13, 18), (15, 22), (15, 26), (16, 25), (17, 23),
       (18, 23), (20, 21), (20, 24), (22, 27)]
adj = [[] for _ in range(28)]
for u,v in E28: adj[u].append(v); adj[v].append(u)
cc = count_cycles(adj, 28, {3,4,8,9,16})
assert (cc[3], cc[4], cc[8]) == (0, 0, 0), cc
assert cc[9] == 34 and cc[16] == 614, cc
CHECK -->

<!-- CHECK
# CHECK 2 — T(Petersen): the n=30 boundary exemplar. Census must be
# c3=10, c4..c8=0, c16=165, and 165 must equal the lift-arithmetic
# prediction 15*1 + 10*C(6,4) from Petersen's 15 C8s and 10 C6s.
from collections import deque
from math import comb

def bfs_dist(adj, n, s):
    d = [n+1]*n; d[s] = 0; q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] > d[v] + 1:
                d[w] = d[v] + 1; q.append(w)
    return d

def count_cycles(adj, n, lengths):
    Lmax = max(lengths); want = set(lengths)
    counts = {L: 0 for L in want}
    for s in range(n):
        dist = bfs_dist(adj, n, s)
        stack = [(u, (1 << s) | (1 << u), 1) for u in adj[s] if u > s]
        while stack:
            v, mask, depth = stack.pop()
            for w in adj[v]:
                if w == s:
                    clen = depth + 1
                    if clen >= 3 and clen in want:
                        counts[clen] += 1
                    continue
                if w < s or (mask >> w) & 1:
                    continue
                nd = depth + 1
                if nd + dist[w] > Lmax:
                    continue
                if nd < Lmax:
                    stack.append((w, mask | (1 << w), nd))
    return {L: c // 2 for L, c in counts.items()}

EP = [(i,(i+1)%5) for i in range(5)] + [(i,i+5) for i in range(5)] \
     + [(5+i,5+(i+2)%5) for i in range(5)]
adjH = [[] for _ in range(10)]
for a,b in EP: adjH[a].append(b); adjH[b].append(a)

n = 30
adj = [[] for _ in range(n)]
pos = {}
for v in range(10):
    for i, w in enumerate(sorted(adjH[v])):
        pos[(v, w)] = 3*v + i
def add(a, b): adj[a].append(b); adj[b].append(a)
for v in range(10):
    t = [3*v, 3*v+1, 3*v+2]
    add(t[0], t[1]); add(t[1], t[2]); add(t[0], t[2])
    for w in sorted(adjH[v]):
        if v < w: add(pos[(v, w)], pos[(w, v)])
assert all(len(set(a)) == 3 for a in adj)
cc = count_cycles(adj, n, {3,4,5,6,7,8,16})
assert cc[3] == 10 and cc[4] == 0 and cc[5] == 0 and cc[6] == 0 \
       and cc[7] == 0 and cc[8] == 0, cc
assert cc[16] == 165, cc
assert 165 == 15 * 1 + 10 * comb(6, 4)
CHECK -->

<!-- CHECK
# CHECK 3 — truncation closure at n=24: ALL connected cubic graphs on
# 8 vertices (19,320 labeled) contain a cycle of length in {3,4,6,7,8},
# so no truncation T(H), |H|=8, is a falsifier. Exhaustive, ~1.4s.
import itertools
from collections import deque

def bfs_dist(adj, n, s):
    d = [n+1]*n; d[s] = 0; q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] > d[v] + 1:
                d[w] = d[v] + 1; q.append(w)
    return d

def has_bad_cycle(adj, n, want):
    Lmax = max(want)
    for s in range(n):
        dist = bfs_dist(adj, n, s)
        stack = [(u, (1 << s) | (1 << u), 1) for u in adj[s] if u > s]
        while stack:
            v, mask, depth = stack.pop()
            for w in adj[v]:
                if w == s:
                    if depth + 1 >= 3 and depth + 1 in want:
                        return True
                    continue
                if w < s or (mask >> w) & 1:
                    continue
                nd = depth + 1
                if nd + dist[w] > Lmax:
                    continue
                if nd < Lmax:
                    stack.append((w, mask | (1 << w), nd))
    return False

def is_connected(adj, n):
    seen = [False]*n; seen[0] = True; q = deque([0]); c = 1
    while q:
        v = q.popleft()
        for w in adj[v]:
            if not seen[w]:
                seen[w] = True; c += 1; q.append(w)
    return c == n

BAD = {3, 4, 6, 7, 8}
total = 0
def rec(adj, v):
    global total
    if v == 8:
        if is_connected(adj, 8):
            total += 1
            assert has_bad_cycle(adj, 8, BAD), f"trunc-safe H found: {adj}"
        return
    need = 3 - len(adj[v])
    if need == 0:
        rec(adj, v + 1); return
    cands = [w for w in range(v + 1, 8) if len(adj[w]) < 3 and w not in adj[v]]
    for combo in itertools.combinations(cands, need):
        for w in combo: adj[v].append(w); adj[w].append(v)
        rec(adj, v + 1)
        for w in combo: adj[v].pop(); adj[w].remove(v)
rec([[] for _ in range(8)], 0)
assert total == 19320, total
CHECK -->

<!-- CHECK
# CHECK 4 — SA near-miss audit pins. The two strongest clean states the
# R61 campaign reached (n=30 girth-5 cold, c16=728; n=30 triangles
# -allowed, c16=210). Both must verify as connected cubic, C4/C8-free,
# with the pinned C16 counts — i.e. NOT falsifiers, by a wide margin.
from collections import deque

def bfs_dist(adj, n, s):
    d = [n+1]*n; d[s] = 0; q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] > d[v] + 1:
                d[w] = d[v] + 1; q.append(w)
    return d

def count_cycles(adj, n, lengths):
    Lmax = max(lengths); want = set(lengths)
    counts = {L: 0 for L in want}
    for s in range(n):
        dist = bfs_dist(adj, n, s)
        stack = [(u, (1 << s) | (1 << u), 1) for u in adj[s] if u > s]
        while stack:
            v, mask, depth = stack.pop()
            for w in adj[v]:
                if w == s:
                    clen = depth + 1
                    if clen >= 3 and clen in want:
                        counts[clen] += 1
                    continue
                if w < s or (mask >> w) & 1:
                    continue
                nd = depth + 1
                if nd + dist[w] > Lmax:
                    continue
                if nd < Lmax:
                    stack.append((w, mask | (1 << w), nd))
    return {L: c // 2 for L, c in counts.items()}

def connected(adj, n):
    seen = {0}; q = deque([0])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w not in seen: seen.add(w); q.append(w)
    return len(seen) == n

G5 = [[8, 28, 9], [11, 14, 2], [9, 15, 1], [20, 29, 17], [14, 21, 16],
      [8, 27, 6], [9, 22, 5], [10, 12, 19], [5, 25, 0], [6, 2, 0],
      [7, 16, 26], [1, 24, 13], [21, 7, 13], [11, 12, 18], [4, 22, 1],
      [24, 2, 25], [10, 29, 4], [3, 24, 19], [23, 13, 19], [7, 17, 18],
      [3, 25, 26], [12, 4, 27], [14, 6, 28], [26, 18, 27], [11, 15, 17],
      [8, 20, 15], [23, 10, 20], [5, 21, 23], [22, 29, 0], [3, 16, 28]]
TRI = [[11, 16, 21], [29, 18, 13], [9, 8, 10], [21, 12, 9], [12, 7, 20],
       [26, 8, 22], [27, 11, 22], [4, 20, 26], [5, 2, 22], [2, 3, 10],
       [29, 2, 9], [0, 27, 6], [4, 3, 21], [17, 29, 1], [15, 24, 28],
       [14, 16, 25], [15, 25, 0], [13, 23, 19], [24, 25, 1], [23, 17, 27],
       [7, 4, 23], [3, 12, 0], [6, 5, 8], [19, 17, 20], [18, 14, 28],
       [18, 16, 15], [5, 28, 7], [11, 6, 19], [26, 14, 24], [1, 13, 10]]
for adj, want3, want16 in ((G5, 0, 728), (TRI, 9, 210)):
    n = 30
    assert all(len(set(a)) == 3 for a in adj) and connected(adj, n)
    assert all(u != v and u in adj[v] for v in range(n) for u in adj[v])
    cc = count_cycles(adj, n, {3, 4, 8, 16})
    assert cc[3] == want3 and cc[4] == 0 and cc[8] == 0, cc
    assert cc[16] == want16, cc
CHECK -->
