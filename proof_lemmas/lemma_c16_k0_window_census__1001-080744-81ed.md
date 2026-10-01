---
id: c16_k0_window_census
status: proved
depends_on: [c16_charge_transport, c16_branch_vertex_arithmetic, c16_n24_catalog_completion, c16_n26_classification]
discharged_by_round: 104
introduced_at_round: 104
---

# Lemma `c16_k0_window_census` (proved — the complete inhabitation map of the cubic $k = 0$ branch: empty at $n \in \{22, 24\}$, one profile at $26$, exactly the six two-path profiles at $28$, 16 of 27 profiles at $30$, inhabited at $32$)

**Setting.** $G$ connected cubic, $\{C_4, C_8\}$-free, $C$ a chordless
$C_{16}$ in $G$, $H := G - V(C)$, $k$ = number of $0$-spoke vertices of
$H$ (for cubic $G$: the vertices with $\deg_H = 3$, i.e. the branch
vertices, per (B0)/(Z) of `c16_branch_vertex_arithmetic`).

**The window and the profile shape (arithmetic).** Suppose $k = 0$.
Then $\Delta(H) \le 2$, so $H$ is a disjoint union of paths (including
$K_1$) and cycles, and since $G$ is $\{C_4, C_8\}$-free, no component
is a $C_4$ or $C_8$. With $|V(H)| = n - 16$ and (B0) spoke count $16$:
$e(H) = \tfrac{3(n-16) - 16}{2}$, hence

$$\#\{\text{path components}\} = |V(H)| - e(H) = \frac{32 - n}{2},
\qquad \#\{\text{cycle components}\} = \mu(H).$$

$e(H) \ge 0$ forces $n \ge 22$; path-count $\ge 0$ forces $n \le 32$
(the charge-transport window `c16_charge_transport` (ii), recovered
here by pure counting). So the whole cubic $k = 0$ branch lives at
$n \in \{22, 24, 26, 28, 30, 32\}$, with the number of path
components of $H$ pinned to $5, 4, 3, 2, 1, 0$ respectively.

**Statement.**

- **(K1) (profile universes)** The $k = 0$ profile universes (iso-types
  of $H$: paths + cycles as above, cycle lengths $\notin \{4, 8\}$)
  have sizes exactly $1, 6, 17, 29, 27$ at $n = 22, 24, 26, 28, 30$.
  (CHECK A; the $n = 26$ count $17$ matches
  `c16_n26_classification` (N1)'s $k{=}0$ stratum.)
- **(K2) (window edge)** $n = 22$: the unique profile
  ($K_2 + 4K_1$) is UNSAT — decided in-harness every round (CHECK B).
  $k = 0$ is impossible at $n = 22$.
- **(K3) ($n = 24$)** All $6$ profiles UNSAT. This re-proves
  `c16_n24_catalog_completion` (T3) ("the $k = 0$ branch is empty at
  $n = 24$") by an independent per-profile SAT route — T3 came from
  the catalog census. One representative UNSAT runs in-harness
  (CHECK C); the engine itself revalidated against the full decided
  $n = 24$ landscape (SPIDER $384$ / TRIPEND $0$) before any new run.
- **(K4) ($n = 26$, reproduction)** Exactly $1$ of $17$ SAT, namely
  $\{P_5, C_3, 2K_1\}$ — reproduces `c16_n26_classification` (N3)
  per-profile.
- **(K5) ($n = 28$ — THE INTERIOR IS INHABITED, and $\mu(H) = 0$ is
  FORCED)** Exactly $6$ of $29$ profiles are SAT: the six two-path
  profiles $P_a + P_b$, $a + b = 12$ — ALL of them — and NO
  cycle-containing profile. Equivalently: a $k = 0$ carrier at
  $n = 28$ has $H$ = two disjoint paths, $c(H) = 2$ (the positivity
  floor of `c16_charge_transport` attained exactly), $\mu(H) = 0$.
  All six witnesses are networkx-verified in-harness (CHECK D).
- **(K6) ($n = 30$ — cycles return)** Exactly $16$ of $27$ profiles
  are SAT: the cycle-free $P_{14}$; every single-cycle profile
  $P_{14-L} + C_L$ EXCEPT $P_1 + C_{13}$ (so $L \in \{3, 5, 6, 7,
  9, 10, 11, 12\}$); and seven multi-cycle profiles
  ($\{3,3\}, \{3,3,3\}, \{3,3,6\}, \{3,5\}, \{3,6\},
  \{3,7\}, \{3,10\}$ with the complementary path). $\mu(H)$
  takes EVERY value $0, 1, 2, 3$. Two clean exclusion laws over the
  $11$ UNSATs: (a) no two cycles of length $\ge 5$ coexist (all
  five such profiles — $\{5,5\}, \{5,6\}, \{5,7\}, \{6,6\},
  \{6,7\}$ — are UNSAT), and (b) every realizable multi-cycle
  profile contains a $C_3$ — but $C_3$ does not suffice
  ($\{3,9\}, \{3,3,5\}, \{3,3,7\}, \{3,5,5\}, \{3,3,3,3\}$
  all die). All $16$ witnesses are networkx-verified in-harness
  (CHECK E).
- **(K7) (the inhabitation map)** Combining (K2)–(K6) with the $n=32$
  witness of `c16_charge_transport` CHECK B: the cubic $k = 0$ branch
  is inhabited EXACTLY at $n \in \{26, 28, 30, 32\}$ — empty at the
  arithmetic edge $22$ and at $24$, then inhabited at every size up
  to the ceiling $32$, with realizable-profile counts
  $0, 0, 1, 6, 16$ at $n = 22, 24, 26, 28, 30$ — monotone filling
  toward the ceiling. Open-core item 1's finite residue is decided:
  the window interior IS inhabited, the $n = 26$ scarcity ($1$ pair
  in $178$) is the lower-edge effect `c16_charge_transport` (R103)
  predicted, and no general-$n$ "$k = 0$ scarcity law" exists.

**Method and scope (stated precisely).** The engine is the R100/R101
SAT encoding lifted verbatim (parametric in $|V(H)|$): position vars
$X[v][p]$, (1) each $C$-position exactly one foot, (2) vertex $v$
exactly $3 - \deg_H(v)$ feet, (3) one-segment $C_4/C_8$ menu binary
clauses, (4) two-segment quad-$C_8$ $4$-ary clauses. The completeness
argument for the clause classes (`c16_n26_classification`, Method) is
$n$-independent: a $C_4/C_8$ meeting $C$ uses $1$ or $2$ $H$-segments
(each $\ge 2$ edges, each arc $\ge 1$, so $3$ segments force length
$\ge 9$); cycles inside $H$ are excluded at profile level; no cycle
meets $C$ in exactly one vertex by (B0). Validation stack, run fresh
this round IN ORDER before any new decision: (V1) the decided $n=24$
landscape (SPIDER $384$, TRIPEND $0$); (V2) the full $n = 26$
$k{=}0$ slice — $17$ profiles, exactly $1$ SAT, the SAT one
isomorphic to $\{P_5, C_3, 2K_1\}$ (R101 (N3)); (V3) the $n = 24$
$k{=}0$ slice — all $6$ UNSAT (R100 T3). What runs in-harness every
round: the full profile arithmetic (CHECK A), the $n = 22$ UNSAT
(CHECK B), a representative $n = 24$ UNSAT (CHECK C), and every
SAT witness at $n = 28$ and $n = 30$ verified with independent code —
cubic, connected, $\{C_4, C_8\}$-free, $C$ chordless, $k = 0$, $H$
isomorphic to the named profile (CHECKs D, E — no SAT involved). The
$23$ cycle-containing UNSATs at $n = 28$ and the MM UNSATs at
$n = 30$ ran off-harness ($38$–$880$s each; full decision table in
the Data appendix), exactly the R101 precedent for enumeration-scale
decisions, with the two validation reproductions (V2)/(V3) as the
independent cross-check of the engine.

**Proof.** (K1): exhaustive recursion over cycle multisets (lengths in
$\{3,5,6,7,9,\dots\} \setminus \{8\}$, sum $\le |V(H)| -$ path count)
and unordered path partitions of the remainder; counts as stated
(CHECK A). (K2)–(K6): one SAT decision per profile with the validated
engine; SAT instances carry explicit verified witnesses (CHECKs D, E),
UNSAT instances are minisat refutations of the validated encoding.
(K7): combine with `c16_charge_transport` (ii) (no $k = 0$ above
$32$) and its CHECK B ($n = 32$ realization). $\square$

**Consequences for the program.**

1. **Open-core item 1 (the "$k = 0$ mechanism") CLOSES.** The honest
   content of "why does $\{P_5, C_3, 2K_1\}$ squeak through at
   $n = 26$" is now: the $k = 0$ branch fills the window monotonically
   from the ceiling down — $0, 0, 1, 6, 16, \ge 1$ realizable
   profiles at $n = 22 \dots 32$ — and $n = 26$ is simply the first
   inhabited size above the empty edge. There is no special $n = 26$
   mechanism to extract and no scarcity law to prove.
2. **The branch-vertex hypothesis is now EXACTLY delimited**: supply /
   floor arguments may assume $k \ge 1$ only at $n \le 24$ (and
   vacuously at $n \ge 34$); at $26 \le n \le 32$ they must handle
   $k = 0$ carriers, whose $H$-shapes this lemma catalogs at the
   profile level.
3. **$\mu$-behaviour across the window is NOT monotone**: the $k = 0$
   realizations have $\mu(H) = 1$ forced at $n = 26$, $\mu(H) = 0$
   forced at $n = 28$ (K5), every value $0 \le \mu \le 3$ realized at $n = 30$ (K6), and
   $\mu = 2$ realized at $n = 32$. Any uniform structural law must
   live at the level of the path/cycle split
   ($\#$paths $= (32-n)/2$), not at the level of $\mu$.

## Data appendix — the full decision table

Profile indices are in CHECK A's deterministic enumeration order.
Format: `idx name SAT|UNSAT decide_s`.

### $n = 28$ ($29$ profiles, $6$ SAT)

```
 0 P1+P11        SAT     0.4
 1 P2+P10        SAT     0.5
 2 P3+P9         SAT     0.2
 3 P4+P8         SAT     0.4
 4 P5+P7         SAT     0.8
 5 P6+P6         SAT     0.2
 6 P1+P8+C3      UNSAT 149.0
 7 P2+P7+C3      UNSAT  93.0
 8 P3+P6+C3      UNSAT 112.2
 9 P4+P5+C3      UNSAT 145.0
10 P1+P5+C3+C3   UNSAT 101.7
11 P2+P4+C3+C3   UNSAT 389.7
12 P3+P3+C3+C3   UNSAT 319.3
13 P1+P2+C3+C3+C3 UNSAT 84.2
14 P1+P3+C3+C5   UNSAT  93.2
15 P2+P2+C3+C5   UNSAT 172.9
16 P1+P2+C3+C6   UNSAT  73.9
17 P1+P1+C3+C7   UNSAT  38.0
18 P1+P6+C5      UNSAT  68.7
19 P2+P5+C5      UNSAT 116.5
20 P3+P4+C5      UNSAT  83.5
21 P1+P1+C5+C5   UNSAT  49.3
22 P1+P5+C6      UNSAT  65.9
23 P2+P4+C6      UNSAT 314.4
24 P3+P3+C6      UNSAT  48.2
25 P1+P4+C7      UNSAT  53.0
26 P2+P3+C7      UNSAT  89.8
27 P1+P2+C9      UNSAT 220.5
28 P1+P1+C10     UNSAT 117.4
```

### $n = 30$ ($27$ profiles, $16$ SAT)

```
 0 P14            SAT     0.9
 1 P11+C3         SAT     1.5
 2 P8+C3+C3       SAT     1.0
 3 P5+C3+C3+C3    SAT     0.5
 4 P2+C3+C3+C3+C3 UNSAT 1385.9
 5 P3+C3+C3+C5    UNSAT  879.7
 6 P2+C3+C3+C6    SAT     0.4
 7 P1+C3+C3+C7    UNSAT   78.1
 8 P6+C3+C5       SAT     0.7
 9 P1+C3+C5+C5    UNSAT  255.5
10 P5+C3+C6       SAT     0.4
11 P4+C3+C7       SAT     0.3
12 P2+C3+C9       UNSAT  981.6
13 P1+C3+C10      SAT     0.5
14 P9+C5          SAT     0.3
15 P4+C5+C5       UNSAT 1600.7
16 P3+C5+C6       UNSAT 1142.6
17 P2+C5+C7       UNSAT  789.7
18 P8+C6          SAT     0.4
19 P2+C6+C6       UNSAT 2264.4
20 P1+C6+C7       UNSAT   67.9
21 P7+C7          SAT     0.3
22 P5+C9          SAT     0.4
23 P4+C10         SAT     0.3
24 P3+C11         SAT     0.4
25 P2+C12         SAT     0.4
26 P1+C13         UNSAT  501.4
```

<!-- CHECK
# CHECK A — (K1) profile universes: sizes 1/6/17/29/26 at n=22/24/26/28/30;
# path-count law #paths = (32-n)/2; no C4/C8 component; e(H) formula.
def path_partitions(m, parts):
    if parts == 0:
        return [()] if m == 0 else []
    out = []
    def rec(rem, kk, lo, cur):
        if kk == 1:
            if rem >= lo: out.append(tuple(cur + [rem]))
            return
        L = lo
        while L * kk <= rem:
            rec(rem - L, kk - 1, L, cur + [L]); L += 1
    rec(m, parts, 1, [])
    return out
def k0_profiles(NV):
    assert (3 * NV - 16) % 2 == 0
    e = (3 * NV - 16) // 2
    npaths = NV - e
    assert npaths == (32 - (NV + 16)) // 2   # the path-count law
    allowed = [L for L in range(3, NV + 1) if L not in (4, 8)]
    profs = []
    def rec(minL, rem, cyc):
        if rem >= npaths:
            for pp in path_partitions(rem, npaths):
                profs.append((pp, tuple(cyc)))
        for L in allowed:
            if L < minL or rem - L < npaths: continue
            rec(L, rem - L, cyc + [L])
    rec(0, NV, [])
    return profs
sizes = {}
for NV in (6, 8, 10, 12, 14):
    ps = k0_profiles(NV)
    sizes[NV + 16] = len(ps)
    for paths, cycles in ps:
        assert sum(paths) + sum(cycles) == NV
        assert all(L not in (4, 8) and L >= 3 for L in cycles)
        assert len(paths) == (32 - (NV + 16)) // 2
        # e(H) check: paths contribute a-1, cycles L
        eH = sum(a - 1 for a in paths) + sum(cycles)
        assert eH == (3 * NV - 16) // 2
assert sizes == {22: 1, 24: 6, 26: 17, 28: 29, 30: 27}, sizes
print("CHECK A ok: k=0 profile universes 1/6/17/29/27 at n=22/24/26/28/30")
CHECK -->

<!-- CHECK
# CHECK B — (K2) the n=22 window edge: the unique k=0 profile (K2+4K1)
# is UNSAT. Engine embedded verbatim (R100/R101 encoding).
from itertools import combinations
from pysat.solvers import Minisat22
from pysat.card import CardEnc, EncType
def h_paths(NV, caps, hedges):
    adj = [[] for _ in range(NV)]
    for a,b in hedges: adj[a].append(b); adj[b].append(a)
    paths = [(v,v,0,frozenset([v])) for v in range(NV) if caps[v] >= 2]
    for u in range(NV):
        if caps[u] == 0: continue
        stack = [(u, frozenset([u]))]
        while stack:
            x, used = stack.pop()
            for w in adj[x]:
                if w in used: continue
                nu = used | frozenset([w])
                if caps[w] >= 1 and u < w: paths.append((u,w,len(nu)-1,nu))
                stack.append((w, nu))
    return paths
def arc_set(p,q,dr):
    out = [p]; x = p
    while x != q: x = (x+dr) % 16; out.append(x)
    return out
def quad_c8(al,be,L1,ga,de,L2):
    for (b,c,d,a) in ((be,ga,de,al),(be,de,ga,al)):
        for d1 in (1,-1):
            A1 = arc_set(b,c,d1)
            if a in A1 or d in A1: continue
            for d2 in (1,-1):
                A2 = arc_set(d,a,d2)
                if b in A2 or c in A2 or set(A1) & set(A2): continue
                if L1+L2+len(A1)+len(A2)-2 == 8: return True
    return False
TABLES = {}
def table(L1,L2):
    if (L1,L2) not in TABLES:
        TABLES[(L1,L2)] = {(b,g,d) for b in range(16) for g in range(16)
                           for d in range(16) if len({0,b,g,d}) == 4
                           and quad_c8(0,b,L1,g,d,L2)}
    return TABLES[(L1,L2)]
def encode(NV, hedges, caps):
    X = [[v*16+p+1 for p in range(16)] for v in range(NV)]
    cl = []
    for p in range(16):
        col = [X[v][p] for v in range(NV) if caps[v] > 0]
        cl.append(col)
        cl += [[-a,-b] for a,b in combinations(col,2)]
        for v in range(NV):
            if caps[v] == 0: cl.append([-X[v][p]])
    top = NV*16
    for v in range(NV):
        if caps[v] == 0: continue
        enc = CardEnc.equals(lits=X[v], bound=caps[v], top_id=top,
                             encoding=EncType.seqcounter)
        cl += enc.clauses; top = max(top, enc.nv)
    paths = h_paths(NV, caps, hedges)
    for u,w,ell,_ in paths:
        diffs = {dd for dd in range(1,16)
                 if dd+ell+2 in (4,8) or 16-dd+ell+2 in (4,8)}
        for p in range(16):
            for q in range(16):
                if p != q and (p-q) % 16 in diffs:
                    if u == w and p > q: continue
                    cl.append([-X[u][p], -X[w][q]])
    pairs2 = [(paths[i], paths[j]) for i in range(len(paths))
              for j in range(i+1, len(paths))
              if paths[i][2]+paths[j][2] <= 2 and not (paths[i][3] & paths[j][3])]
    for A, B in pairs2:
        u1,w1,e1,_ = A; u2,w2,e2,_ = B
        L1, L2 = e1+2, e2+2
        for (b,g,d) in table(L1,L2):
            for al in range(16):
                be, ga, de = (al+b)%16, (al+g)%16, (al+d)%16
                if u1 == w1 and al > be: continue
                if u2 == w2 and ga > de: continue
                cl.append([-X[u1][al], -X[w1][be], -X[u2][ga], -X[w2][de]])
    return X, cl
# n=22: H = K2 + 4K1 on 6 vertices, 1 edge; caps: K2 ends 2, K1s 3.
X, cl = encode(6, [(0,1)], [2,2,3,3,3,3])
with Minisat22(bootstrap_with=cl) as m:
    assert not m.solve(), "n=22 k=0 unexpectedly SAT"
# (K3) representative n=24 UNSAT in-harness: P1+P1+P3+P3
# (vertices 0,1 = K1s; 2-3-4 and 5-6-7 = P3s).
X, cl = encode(8, [(2,3),(3,4),(5,6),(6,7)], [3,3,2,1,2,2,1,2])
with Minisat22(bootstrap_with=cl) as m:
    assert not m.solve(), "n=24 P1+P1+P3+P3 unexpectedly SAT"
print("CHECK B ok: n=22 edge UNSAT (K2+4K1); n=24 representative UNSAT (P1+P1+P3+P3)")
CHECK -->

<!-- CHECK
# CHECK D — (K5) all six n=28 witnesses, verified with independent code
# (no SAT): cubic, connected, C4/C8-free, C chordless, k=0, H iso to
# the named two-path profile. Feet layout: H vertex v (0-indexed, paths
# laid out in order, each path consecutively) gets feet (C positions)
# from the list.
import networkx as nx
WITNESSES = [
    ((1, 11), [[6,9,10],[11,12],[15],[3],[13],[5],[2],[4],[7],[1],[14],[0,8]]),
    ((2, 10), [[14,15],[2,11],[8,12],[5],[9],[7],[3],[10],[1],[4],[0],[6,13]]),
    ((3, 9),  [[7,8],[5],[1,2],[9,10],[0],[3],[11],[4],[13],[6],[12],[14,15]]),
    ((4, 8),  [[6,7],[10],[0],[8,13],[14,15],[5],[1],[4],[11],[2],[9],[3,12]]),
    ((5, 7),  [[5,9],[15],[11],[13],[0,4],[10,14],[2],[12],[8],[1],[3],[6,7]]),
    ((6, 6),  [[11,12],[15],[13],[5],[7],[3,4],[9,10],[6],[0],[8],[14],[1,2]]),
]
for paths, feet in WITNESSES:
    NV = sum(paths)
    assert NV == 12 and len(feet) == NV
    Hx = nx.Graph(); Hx.add_nodes_from(range(NV)); off = 0
    for a in paths:
        for j in range(a - 1): Hx.add_edge(off + j, off + j + 1)
        off += a
    G = nx.Graph()
    for i in range(16): G.add_edge(i, (i + 1) % 16)
    for a, b in Hx.edges(): G.add_edge(16 + a, 16 + b)
    for v in range(NV):
        for p in feet[v]: G.add_edge(p, 16 + v)
    assert G.number_of_nodes() == 28
    assert all(d == 3 for _, d in G.degree()), "cubic"
    assert nx.is_connected(G), "connected"
    lens = {len(c) for c in nx.simple_cycles(G, length_bound=8)}
    assert not (lens & {4, 8}), "C4/C8-free"
    from itertools import combinations as comb
    for p, q in comb(range(16), 2):
        if (p - q) % 16 not in (1, 15):
            assert not G.has_edge(p, q), "chordless C"
    Hs = G.subgraph(range(16, 16 + NV))
    assert max(d for _, d in Hs.degree()) <= 2, "k=0"
    assert nx.is_isomorphic(nx.Graph(Hs), Hx), "H profile"
print("CHECK D ok: all 6 n=28 two-path witnesses verified (cubic, connected, C4/C8-free, chordless C, k=0)")
CHECK -->

<!-- CHECK
# CHECK E — (K6) all sixteen n=30 witnesses, verified with independent
# code (no SAT). Layout: paths first (consecutive vertices), then
# cycles, in the listed order; feet[v] = C positions of H vertex v.
import networkx as nx
WITNESSES = [
    ((14,), (), [[7, 8], [5], [1], [3], [0], [10], [2], [9], [11], [4], [13], [6], [12], [14, 15]]),
    ((11,), (3,), [[7, 8], [4], [6], [12], [14], [5], [1], [15], [9], [2], [10, 11], [13], [3], [0]]),
    ((8,), (3, 3), [[3, 4], [0], [2], [5], [7], [10], [12], [8, 9], [11], [1], [14], [6], [13], [15]]),
    ((5,), (3, 3, 3), [[8, 9], [5], [7], [3], [0, 1], [2], [12], [10], [11], [4], [14], [6], [13], [15]]),
    ((2,), (3, 3, 6), [[2, 3], [5, 9], [12], [14], [4], [13], [0], [10], [6], [15], [1], [7], [11], [8]]),
    ((6,), (3, 5), [[13, 14], [1], [11], [8], [2], [5, 6], [7], [0], [9], [4], [10], [3], [15], [12]]),
    ((5,), (3, 6), [[1, 2], [5], [3], [13], [10, 11], [6], [15], [12], [4], [7], [9], [0], [14], [8]]),
    ((4,), (3, 7), [[6, 9], [13], [7], [0, 15], [1], [3], [10], [2], [12], [4], [14], [11], [8], [5]]),
    ((1,), (3, 10), [[5, 6, 13], [2], [8], [11], [7], [9], [0], [14], [10], [12], [15], [3], [1], [4]]),
    ((9,), (5,), [[4, 5], [2], [11], [3], [13], [10], [7], [9], [0, 1], [6], [14], [8], [12], [15]]),
    ((8,), (6,), [[10, 11], [4], [13], [6], [0], [14], [8], [1, 5], [3], [7], [9], [12], [2], [15]]),
    ((7,), (7,), [[8, 9], [12], [6], [3], [0], [4], [2, 10], [7], [5], [14], [11], [1], [13], [15]]),
    ((5,), (9,), [[4, 8], [1], [10], [0], [12, 13], [14], [2], [6], [15], [7], [5], [9], [3], [11]]),
    ((4,), (10,), [[7, 10], [14], [4], [6, 11], [2], [12], [9], [3], [1], [5], [8], [0], [13], [15]]),
    ((3,), (11,), [[9, 13], [7], [10, 11], [14], [12], [5], [3], [6], [0], [8], [2], [15], [1], [4]]),
    ((2,), (12,), [[7, 14], [1, 4], [8], [6], [9], [3], [0], [10], [13], [15], [12], [2], [5], [11]]),
]
assert len(WITNESSES) == 16
for paths, cycles, feet in WITNESSES:
    NV = sum(paths) + sum(cycles)
    assert NV == 14 and len(feet) == NV
    Hx = nx.Graph(); Hx.add_nodes_from(range(NV)); off = 0
    for a in paths:
        for j in range(a - 1): Hx.add_edge(off + j, off + j + 1)
        off += a
    for L in cycles:
        for j in range(L): Hx.add_edge(off + j, off + (j + 1) % L)
        off += L
    lens_H = {len(c) for c in nx.simple_cycles(Hx)} if Hx.number_of_edges() >= 3 else set()
    assert not (lens_H & {4, 8})
    G = nx.Graph()
    for i in range(16): G.add_edge(i, (i + 1) % 16)
    for a, b in Hx.edges(): G.add_edge(16 + a, 16 + b)
    for v in range(NV):
        for p in feet[v]: G.add_edge(p, 16 + v)
    assert G.number_of_nodes() == 30
    assert all(d == 3 for _, d in G.degree()), "cubic"
    assert nx.is_connected(G), "connected"
    lens = {len(c) for c in nx.simple_cycles(G, length_bound=8)}
    assert not (lens & {4, 8}), "C4/C8-free"
    from itertools import combinations as comb
    for p, q in comb(range(16), 2):
        if (p - q) % 16 not in (1, 15):
            assert not G.has_edge(p, q), "chordless C"
    Hs = G.subgraph(range(16, 16 + NV))
    assert max(d for _, d in Hs.degree()) <= 2, "k=0"
    assert nx.is_isomorphic(nx.Graph(Hs), Hx), "H profile"
mus = sorted({len(c) for p, c, f in WITNESSES})
assert mus == [0, 1, 2, 3], mus
print("CHECK E ok: all 16 n=30 witnesses verified; mu(H) takes every value 0..3")
CHECK -->
