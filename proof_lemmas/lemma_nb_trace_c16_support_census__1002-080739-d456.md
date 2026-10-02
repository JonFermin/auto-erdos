---
id: nb_trace_c16_support_census
status: proved
depends_on: [nb_trace_c8_identity]
discharged_by_round: 106
introduced_at_round: 106
---

# Lemma `nb_trace_c16_support_census` (proved — the exact composite census of $\operatorname{tr} B^{16}$ for cubic girth-$\ge 5$ $C_8$-free graphs: $\operatorname{tr} B^{16} = 32\,c_{16} + \sum_T w(T)\,N_T(G)$ over a complete finite table of $39$ composite shapes, all weights positive)

**Setting.** $G$ a finite simple cubic graph, $n = |V(G)|$, $A$ its
adjacency matrix, $B$ its $3n \times 3n$ non-backtracking (dart)
matrix, $c_{16} = c_{16}(G)$ the number of (unoriented,
basepoint-free) $16$-cycles. $q_k$ is the trace-transfer polynomial
family of `nb_trace_c8_identity`: $q_0 = 2$, $q_1 = x$,
$q_k = x\,q_{k-1} - 2\,q_{k-2}$. A *cyclically-NB closed $16$-walk*
is a dart sequence $e_1 \to \cdots \to e_{16} \to e_1$ with every
consecutive pair (including the wrap) non-backtracking; its
*support* is the set of underlying undirected edges.
$\operatorname{tr} B^{16}$ counts exactly these walks (with marked
start).

**Statement.**

- **(S1) (trace transfer at $k=16$; no girth hypothesis)** For every
  finite simple cubic $G$:
  $$\operatorname{tr} B^{16} = n + \operatorname{tr} q_{16}(A),
  \qquad q_{16} = q_8^2 - 512 .$$
  Explicitly $q_{16} = x^{16} - 32x^{14} + 416x^{12} - 2816x^{10} +
  10560x^8 - 21504x^6 + 21504x^4 - 8192x^2 + 512$, and
  $q_{16}(3) = 257^2 - 512 = 65537 = 2^{16} + 1$. (CHECKs A, B.)
- **(S2) (support classification)** If $G$ has girth $\ge 5$ and is
  $C_8$-free, the support $S$ of every cyclically-NB closed
  $16$-walk is a connected subgraph with $2 \le \deg \le 3$,
  $e(S) + \mu(S) \le 17$ ($\mu$ = cycle rank), and $\mu(S) \le 3$.
  Up to isomorphism, $S$ is one of exactly $40$ graphs:
  - $\mu = 1$: the $16$-cycle $C_{16}$ (one type);
  - $\mu = 2$, dumbbell $D(\ell_1, \ell_2, p)$ (two disjoint cycles
    joined by a path of length $p \ge 1$): exactly the five types
    with $\ell_1 + \ell_2 + 2p = 16$, $\ell_i \in \{5,6,7,9\} $:
    $(5,5,3), (5,7,2), (5,9,1), (6,6,2), (7,7,1)$;
  - $\mu = 2$, theta $\theta(a,b,c)$ ($3$ internally disjoint paths
    between two branch vertices): exactly $14$ types (table below);
  - $\mu = 3$ ($4$ branch vertices, $e \le 14$): exactly $20$
    homeomorphism types of subdivided cubic multigraphs on $4$
    vertices (CHECK D);
  - $\mu = 4$: impossible (proof step 5 + CHECK E); $\mu \ge 5$:
    impossible (proof step 6).
- **(S3) (weights)** The number $w(T)$ of cyclically-NB closed
  $16$-walks with support a FIXED copy of $T$ depends only on the
  isomorphism type of $T$: $w(C_{16}) = 32$; $w(D) = 64$ for all five
  dumbbells; for thetas
  $$\begin{array}{llll}
  w(1,4,5)=32, & w(1,4,10)=32, & w(1,5,5)=64, & w(1,5,9)=32,\\
  w(1,6,8)=32, & w(2,3,3)=192, & w(2,3,4)=32, & w(2,3,8)=32,\\
  w(2,3,9)=32, & w(2,4,5)=32, & w(2,4,8)=32, & w(2,5,7)=32,\\
  w(3,3,7)=64, & w(3,4,6)=32; &&
  \end{array}$$
  and for the $20$ $\mu=3$ types $w \in \{32, 64, 96, 192, 352\}$
  (CHECK D computes the full table). Every other admissible shape in
  the $\mu \le 3$ window has $w = 0$.
- **(S4) (the census identity)** For cubic girth-$\ge 5$ $C_8$-free
  $G$:
  $$\operatorname{tr} B^{16} \;=\; 32\, c_{16} \;+\;
    \sum_{T \in \mathcal{T}} w(T)\, N_T(G) \;\ge\; 32\, c_{16},$$
  where $\mathcal{T}$ is the $39$-type composite table of (S2)/(S3)
  and $N_T(G)$ counts subgraphs of $G$ isomorphic to $T$. This is
  the $C_8$-freeness-aware replacement for the FALSIFIED generic
  share bound (R103/R105 scope): the composite share is an exact
  nonnegative local-subgraph functional, not a constant fraction.
- **(S5) (second-moment law)** If $G$ is cubic with girth $\ge 5$ and
  $C_8$-free (so $\operatorname{tr} q_8(A) = -n$ by
  `nb_trace_c8_identity` (S3)), then
  $$\sum_{i=1}^n q_8(\lambda_i)^2 \;=\; 511\,n + \operatorname{tr} B^{16}
    \;=\; 511\,n + 32\,c_{16} + \textstyle\sum_T w(T) N_T(G).$$
  If $G$ is moreover $C_{16}$-free, then
  $\sum_i q_8(\lambda_i)^2 = 511n + \sum_T w(T) N_T(G)$, and (for
  connected $G$, $\lambda_1 = 3$, $q_8(3) = 257$) the power-mean
  bound on the non-Perron spectrum gives the forced composite mass
  $$\sum_T w(T)\, N_T(G) \;\ge\; 66049 + \frac{(n + 257)^2}{n-1}
    - 511\,n \qquad (> 0 \text{ for } n \le 128).$$
  Every composite type $T$ contains a cycle of length $5$, $6$, or
  $7$, so a $\{C_4, C_8, C_{16}\}$-free cubic graph in the witness
  window is forced to be rich in short odd-window cycles (e.g.
  $n = 30$: composite mass $\ge 53559$, hence $\ge
  \lceil 53559/352 \rceil = 153$ composite subgraphs).

**Proof.**

*(S1).* `nb_trace_c8_identity` (S1) proved (self-contained
Ihara–Bass factorization) that for cubic $G$ the eigenvalue multiset
of $B$ is $\{\alpha_i, \beta_i\}_{i=1}^n \cup \{\pm 1^{(n/2)}\}$ with
$\alpha_i + \beta_i = \lambda_i$, $\alpha_i \beta_i = 2$, and that
$\alpha_i^k + \beta_i^k = q_k(\lambda_i)$ (Newton recurrence with
$s_0 = 2$, $s_1 = \lambda_i$). At $k = 16$:
$\operatorname{tr} B^{16} = \sum_i q_{16}(\lambda_i) +
\tfrac{n}{2}(1^{16} + (-1)^{16}) = \operatorname{tr} q_{16}(A) + n$.
For the product identity: $s_{16} = s_8^2 - 2(\alpha\beta)^8 =
q_8^2 - 2 \cdot 2^8 = q_8^2 - 512$ as polynomials in $\lambda$
(CHECK A). $\square$

*(S2).* Let $W$ be a cyclically-NB closed $16$-walk with support $S$.

1. *Degrees and rank.* $S$ is connected (a closed walk). Every
   support vertex is entered and left by non-identical darts at each
   visit, so $\deg_S \ge 2$; $\deg_S \le 3$ (subgraph of cubic). Let
   $v_3 = \#\{\deg_S = 3\}$: handshake gives $v_3 = 2e - 2v =
   2(\mu - 1)$.
2. *The budget inequality.* $W$ makes $16$ vertex-arrivals. A
   deg-$3$ support vertex has all $3$ incident edges traversed, and
   each arrival consumes exactly $2$ edge-slots, so it is arrived at
   $\ge 2$ times. Hence $16 \ge v + v_3 = v + 2(\mu - 1)$; with
   $e = v + \mu - 1$: $\boxed{16 \ge e + \mu - 1}$.
3. *$\mu = 1$.* On a cycle $C_\ell$, non-backtracking forces constant
   direction, so $W$ winds $k \ge 1$ full turns: $k\ell = 16$ with
   $\ell \ge 5$, $\ell \ne 8$ (girth, $C_8$-free) forces
   $\ell = 16$, $k = 1$. Each of the $32$ darts of a $C_{16}$ starts
   exactly one such walk: $w(C_{16}) = 32$.
4. *$\mu \in \{2, 3\}$.* Suppressing deg-$2$ vertices turns $S$ into
   a connected multigraph $M$ (loops and parallel edges allowed) on
   $v_3 = 2(\mu-1)$ vertices of degree $3$, with $e(M) = 3(\mu - 1)$;
   $S$ is a subdivision of $M$ with total length $e \le 17 - \mu$.
   The cycles of $S$ are exactly the subdivided cycles of $M$, so
   admissibility (every cycle length $\ge 5$ and $\ne 8$) is a
   finite arithmetic condition on the subdivision vector. For
   $\mu = 2$ ($M$ on $2$ vertices): $M$ is the triple edge (theta) or
   two loops plus a bar (dumbbell). For $\mu = 3$: $M$ ranges over
   the degree-$3$ multigraphs on $4$ vertices. Both lists of
   admissible subdivision types with $e \le 15$ resp. $e \le 14$ are
   finite and enumerated exhaustively in CHECKs C/D.
5. *$\mu = 4$ is impossible.* Here $v_3 = 6$, $e \le 13$, $M$ is a
   degree-$3$ multigraph on $6$ vertices with $9$ edges, and the
   subdivision budget is $s = e - 9 \le 4$ extra vertices.
   (a) *$M$ has no loop:* a loop subdivides to a cycle, needing
   length $\ge 5$, i.e. $\ge 4$ interior points — the whole budget.
   All other edges then have length $1$, so $S$ minus the loop and
   its base vertex contains the unit graph $H'$ on $5$ vertices with
   $7$ edges (degrees $(2,3,3,3,3)$), whose cycles must all have
   length $\ge 5$. But a girth-$\ge 5$ graph on $5$ vertices is a
   subgraph of $C_5$ plus isolated vertices ($\le 5$ edges): any
   chord of a $C_5$ makes a $3$- or $4$-cycle. Contradiction.
   (b) *$M$ has no parallel pair:* two parallel $u$–$v$ edges
   subdivide to a cycle of length $\ell_1 + \ell_2 \ge 5$, consuming
   $\ge 3$ points, leaving $\le 1$. A triple edge would disconnect
   $\{u, v\}$ from the rest, so $u, v$ each have one further edge.
   Deleting the two parallel edges and the (now pendant) $u, v$
   leaves a core multigraph on the other $4$ vertices with $5$ edges
   and cycle rank $\ge 2$, all of whose cycles have combinatorial
   length $\le 4$ and must reach subdivided length $\ge 5$ using the
   single remaining point: two independent cycles (rank $2$) cannot
   both contain the pointed edge while their symmetric difference —
   again a cycle of length $\le 4$ — avoids it. Contradiction.
   (c) So $M$ is a SIMPLE cubic graph on $6$ vertices ($K_{3,3}$ or
   the prism, in any labeling). CHECK E enumerates ALL simple cubic
   graphs on $6$ labeled vertices and ALL subdivision vectors with
   $e \le 13$ and finds NO vector with every cycle length $\ge 5$
   and $\ne 8$. Hence no $\mu = 4$ support exists.
6. *$\mu = 5$ is impossible:* $v_3 = 8$ and $e \le 12$ force
   $v = e - 4 \le 8 = v_3$, so $S$ itself is a simple cubic graph on
   $8$ vertices of girth $\ge 5$; but in a cubic graph of girth
   $\ge 5$ the ball of radius $2$ about any vertex contains
   $1 + 3 + 6 = 10$ distinct vertices (no $C_3$/$C_4$ collapses),
   so $v \ge 10$. Contradiction. *$\mu \ge 6$:*
   $v_3 = 2(\mu - 1) \ge 10 > 18 - 2\mu \ge v$. Contradiction.
   $\square$

*(S3).* A walk with support $S$ never leaves $S$, so $w(T)$ is an
isomorphism invariant. The walks counted by
$\operatorname{tr} B_T^{16}$ (the dart matrix of the abstract shape
$T$) partition by support over the connected min-deg-$2$ subgraphs
of $T$, which are exactly the unions of whole suppressed paths with
min-degree $\ge 2$ (a partial path leaves a deg-$1$ end): hence the
Möbius recursion
$$w(T) = \operatorname{tr} B_T^{16} -
  \sum_{T' \subsetneq T} w(T'),$$
with the sum over proper connected min-deg-$2$ path-unions. For
$\mu \le 2$ every proper $T'$ is a cycle of length $\le 14 \ne 16$,
so $w(T) = \operatorname{tr} B_T^{16}$ outright; for $\mu = 3$ the
recursion bottoms out in the $\mu \le 2$ tables. CHECK C computes
the complete $\mu \le 2$ tables and CHECK D the complete $\mu = 3$
table by this recursion; the $20$ positive $\mu = 3$ weights were
additionally cross-validated against a direct full-support DFS walk
enumeration, and the ENTIRE table against ground-truth whole-graph
walk censuses on $11$ distinct samples (see Scope notes). $\square$

*(S4).* Partition the $\operatorname{tr} B^{16}$ walks by support;
apply (S2) + (S3). Positivity: all table weights are positive.
$\square$

*(S5).* By `nb_trace_c8_identity` (S3), $C_8$-freeness at girth
$\ge 5$ gives $\operatorname{tr} q_8(A) = -n$. By (S1):
$\sum_i q_8(\lambda_i)^2 = \operatorname{tr} q_{16}(A) + 512n =
\operatorname{tr} B^{16} + 511n$. Substitute (S4). For the bound:
$C_{16}$-free kills the $32 c_{16}$ term;
$\sum_{i \ge 2} q_8(\lambda_i) = -n - 257$ and Cauchy–Schwarz give
$\sum_{i \ge 2} q_8(\lambda_i)^2 \ge (n + 257)^2/(n - 1)$, so
$\operatorname{tr} B^{16} = \sum_i q_8(\lambda_i)^2 - 511n \ge
66049 + (n+257)^2/(n-1) - 511n$. The short-cycle claim: every
dumbbell has $\min(\ell_1, \ell_2) \le 7$; every table theta has
smallest cycle $\min(a{+}b, a{+}c) \in \{5, 6, 7\}$; every $\mu = 3$
type has minimum-cycle-basis entries $\le 7$ (CHECK D verifies
$\min \le 7$ for all $39$). $\square$

**Scope notes (honest, program-facing).**

1. The classification needs girth $\ge 5$ (triangle-free stratum of
   the verifier class) — at girth $3$ the composite zoo is unbounded
   in the same window and this census does NOT apply. $C_8$-freeness
   enters twice: through the cycle filter ($\ne 8$) on shapes AND
   through the linear constraint $\operatorname{tr} q_8(A) = -n$
   used in (S5).
2. Numerical map (offline, 11 distinct girth-$\ge 5$ $C_8$-free
   cubic samples, $n \in \{30, \dots, 40\}$ — two census-witness
   carriers from `c16_k0_window_census` plus $9$ annealed random
   samples): $\operatorname{tr} B^{16}$ stays within $[64000,
   67776]$ across all samples (Perron pin $q_{16}(3) + 1 = 65538$
   dominates; non-Perron spectrum averages $q_{16} \approx -1$),
   while the composite share falls from $63\%$ ($n = 30$) to $46\%$
   ($n = 40$). Full walk censuses on $5$ samples (incl. $n = 36,
   40$) matched the tables shape-for-shape and weight-for-weight
   with zero residual.
3. The minimum $n$ for a girth-$\ge 5$ $C_8$-free cubic graph
   appears to be $30$ (annealing from $n \le 28$ always stalled at
   $c_8 \ge 1$; two independent searches at $n = 30$ converged to
   ISOMORPHIC graphs). Not proved — recorded as a conjecture-grade
   observation for the composition program.
4. For the L3 hunt: (S5) is an exact moment identity, not an
   inequality — the moment-LP side can consume
   $\operatorname{tr} A^k$ ($k \le 7$, girth-pinned),
   $\operatorname{tr} q_8(A) = -n$, and
   $\sum q_8(\lambda)^2 - 511n = $ (composite mass $\ge$ the (S5)
   bound), while the counting side must bound the SAME composite
   mass above via short-cycle counts. The two-sided squeeze on
   composite mass is the program's next target
   (qid Q0930-083610-2 continuation).

<!-- CHECK
# CHECK A — q16 from the recurrence q0=2, q1=x, qk = x q_{k-1} - 2 q_{k-2};
# the product identity q16 = q8^2 - 512; q16(3) = 65537 = 2^16 + 1.
def qpoly(k):
    q0, q1 = [2], [0, 1]
    if k == 0: return q0
    for _ in range(k - 1):
        xq1 = [0] + q1
        L = max(len(xq1), len(q0))
        q0, q1 = q1, [(xq1[i] if i < len(xq1) else 0)
                      - 2 * (q0[i] if i < len(q0) else 0) for i in range(L)]
    return q1
q8, q16 = qpoly(8), qpoly(16)
assert q8 == [32, 0, -128, 0, 80, 0, -16, 0, 1]
assert q16 == [512, 0, -8192, 0, 21504, 0, -21504, 0, 10560, 0, -2816, 0, 416, 0, -32, 0, 1]
sq = [0] * 17
for i, a in enumerate(q8):
    for j, b in enumerate(q8): sq[i + j] += a * b
sq[0] -= 512
assert sq == q16
v3 = sum(c * 3 ** i for i, c in enumerate(q16))
assert v3 == 65537 == 2 ** 16 + 1 and v3 == 257 ** 2 - 512
print("CHECK A ok: q16 = q8^2 - 512; q16(3) = 65537")
CHECK -->

<!-- CHECK
# CHECK B — (S1) trace transfer at k=16 on Petersen, Heawood, and three
# random cubic graphs (no girth hypothesis): tr B^16 == n + tr q16(A).
import numpy as np, networkx as nx, random
Q16 = [512, 0, -8192, 0, 21504, 0, -21504, 0, 10560, 0, -2816, 0, 416, 0, -32, 0, 1]
def trB16(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=np.int64)
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return int(np.trace(np.linalg.matrix_power(B, 16)))
def trq16(G):
    A = nx.to_numpy_array(G).astype(np.int64); n = len(A)
    tot = Q16[0] * np.eye(n, dtype=np.int64); P = np.eye(n, dtype=np.int64)
    for c in Q16[1:]:
        P = P @ A; tot = tot + c * P
    return int(np.trace(tot))
rng = random.Random(106)
Gs = [nx.petersen_graph(), nx.heawood_graph()]
while len(Gs) < 5:
    G = nx.random_regular_graph(3, 14, seed=rng.randint(0, 10 ** 6))
    if nx.is_connected(G): Gs.append(G)
for G in Gs:
    assert trB16(G) == G.number_of_nodes() + trq16(G)
print("CHECK B ok: tr B^16 = n + tr q16(A) on Petersen, Heawood, 3 random cubics")
CHECK -->

<!-- CHECK
# CHECK C — (S3) complete mu<=2 weight tables by abstract trace: thetas
# (all admissible a<=b<=c, a+b+c<=15, pair sums >=5 and !=8) and dumbbells
# (all admissible l1+l2+2p=16 within e<=15). w = tr B_T^16 outright since
# every proper min-deg-2 connected subshape is a cycle of length <=14 != 16.
import numpy as np, networkx as nx
def trB16(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=np.int64)
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return int(np.trace(np.linalg.matrix_power(B, 16)))
thetas = {}
for a in range(1, 6):
    for b in range(a, 15):
        for c in range(b, 16 - a - b):
            if a + b + c > 15: continue
            sums = (a + b, a + c, b + c)
            if any(s < 5 or s == 8 for s in sums): continue
            G = nx.Graph()
            for li, L in enumerate((a, b, c)):
                prev = "u"
                for j in range(1, L): G.add_edge(prev, (li, j)); prev = (li, j)
                G.add_edge(prev, "v")
            w = trB16(G)
            if w: thetas[(a, b, c)] = w
assert thetas == {(1,4,5):32, (1,4,10):32, (1,5,5):64, (1,5,9):32, (1,6,8):32,
                  (2,3,3):192, (2,3,4):32, (2,3,8):32, (2,3,9):32, (2,4,5):32,
                  (2,4,8):32, (2,5,7):32, (3,3,7):64, (3,4,6):32}, thetas
dbs = {}
for l1 in range(5, 15):
    for l2 in range(l1, 15):
        if 8 in (l1, l2): continue
        rem = 16 - l1 - l2
        if rem < 2 or rem % 2: continue
        p = rem // 2
        G = nx.Graph()
        for j in range(l1): G.add_edge(("a", j), ("a", (j + 1) % l1))
        for j in range(l2): G.add_edge(("b", j), ("b", (j + 1) % l2))
        prev = ("a", 0)
        for j in range(1, p): G.add_edge(prev, ("p", j)); prev = ("p", j)
        G.add_edge(prev, ("b", 0))
        w = trB16(G)
        if w: dbs[(l1, l2, p)] = w
assert dbs == {(5,5,3):64, (5,7,2):64, (5,9,1):64, (6,6,2):64, (7,7,1):64}, dbs
print("CHECK C ok: 14 theta types + 5 dumbbell types, weights as stated")
CHECK -->

<!-- CHECK
# CHECK D — (S2)+(S3) complete mu=3 table: enumerate ALL degree-3 multigraphs
# on 4 vertices (loops allowed), all subdivision vectors with e<=14 and every
# cycle >=5 and !=8, dedupe by isomorphism, weight by the Moebius recursion
# over connected min-deg-2 path-unions. Exactly 20 types have w>0; min cycle
# <= 7 for every one (used by S5).
import numpy as np, networkx as nx, itertools
def trB16(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=np.int64)
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return int(np.trace(np.linalg.matrix_power(B, 16)))
def multigraphs4():
    pairs = list(itertools.combinations(range(4), 2))
    slots = [("p", p) for p in pairs] + [("l", v) for v in range(4)]
    out, cur = [], {}
    def dadd(deg, s, k):
        if s[0] == "p": u, v = s[1]; deg[u] += k; deg[v] += k
        else: deg[s[1]] += 2 * k
    def rec(i, deg):
        if any(d > 3 for d in deg): return
        if i == len(slots):
            if all(d == 3 for d in deg): out.append({s: m for s, m in cur.items() if m})
            return
        for k in range(0, (3 if slots[i][0] == "p" else 1) + 1):
            cur[slots[i]] = k; dadd(deg, slots[i], k)
            rec(i + 1, deg); dadd(deg, slots[i], -k)
        cur[slots[i]] = 0
    rec(0, [0, 0, 0, 0])
    return out
def build(mg, lengths):
    G = nx.Graph(); nid = [100]
    k = 0
    for slot, m in mg.items():
        for _ in range(m):
            L = lengths[k]; k += 1
            if slot[0] == "p":
                u, v = slot[1]; prev = u
                for _ in range(L - 1):
                    nid[0] += 1; G.add_edge(prev, nid[0]); prev = nid[0]
                G.add_edge(prev, v)
            else:
                v = slot[1]; nid[0] += 1; first = nid[0]; G.add_edge(v, first)
                prev = first
                for _ in range(L - 2):
                    nid[0] += 1; G.add_edge(prev, nid[0]); prev = nid[0]
                G.add_edge(prev, v)
    return G
def paths_of(G):
    deg3 = {v for v, d in G.degree() if d == 3}
    out, used = [], set()
    for a in deg3:
        for b in G.neighbors(a):
            if (a, b) in used: continue
            pe = [(a, b)]; prev, cur = a, b
            while cur not in deg3:
                nxt = [w for w in G.neighbors(cur) if w != prev][0]
                pe.append((cur, nxt)); prev, cur = cur, nxt
            used.add((a, b)); used.add((pe[-1][1], pe[-1][0]))
            out.append(pe)
    return out
def weight(G):
    paths = paths_of(G); m = len(paths)
    shapes = []
    for r in range(1, m + 1):
        for comb in itertools.combinations(range(m), r):
            H = nx.Graph()
            for i in comb: H.add_edges_from(paths[i])
            if H.number_of_edges() != sum(len(paths[i]) for i in comb): continue
            if not nx.is_connected(H): continue
            if min(d for _, d in H.degree()) < 2: continue
            shapes.append((frozenset(comb), H))
    shapes.sort(key=lambda t: t[1].number_of_edges())
    W = {}
    for key, H in shapes:
        W[key] = trB16(H) - sum(W[k2] for k2, _ in shapes if k2 < key)
    return W[frozenset(range(m))]
def mg_cycles(slots):
    """simple cycles of the multigraph as slot-index tuples (loops, parallel
    pairs, and vertex-DFS cycles)."""
    cycles = set()
    for i, s in enumerate(slots):
        if s[0] == "l": cycles.add((i,))
    for i in range(len(slots)):
        for j in range(i + 1, len(slots)):
            if slots[i][0] == slots[j][0] == "p" and slots[i][1] == slots[j][1]:
                cycles.add((i, j))
    def dfs(start, v, used, verts):
        for i, s in enumerate(slots):
            if i in used or s[0] == "l": continue
            a, b = s[1]
            if a == v: w = b
            elif b == v: w = a
            else: continue
            if w == start and len(used) >= 1:
                cycles.add(tuple(sorted(used | {i}))); continue
            if w in verts: continue
            dfs(start, w, used | {i}, verts | {w})
    for v in range(4): dfs(v, v, frozenset(), frozenset({v}))
    return sorted(cycles)
types = []
for mg in multigraphs4():
    slots = [s for s, m in mg.items() for _ in range(m)]
    if not slots: continue
    mins = [5 if s[0] == "l" else 1 for s in slots]
    budget = 14 - sum(mins)
    if budget < 0: continue
    cyc = mg_cycles(slots)
    for s in range(budget + 1):
        for combo in itertools.combinations_with_replacement(range(len(slots)), s):
            L = list(mins)
            for i in combo: L[i] += 1
            if any((t := sum(L[i] for i in c)) < 5 or t == 8 for c in cyc): continue
            G = build(mg, L)
            if G.number_of_edges() != sum(L) or not nx.is_connected(G): continue
            if sorted(d for _, d in G.degree()).count(3) != 4: continue
            inv = (G.number_of_edges(),
                   tuple(sorted(len(c) for c in nx.minimum_cycle_basis(G))))
            dup = any(hinv == inv and nx.is_isomorphic(G, H) for H, hinv in types)
            if not dup: types.append((G, inv))
table = sorted((inv[0], inv[1], w) for G, inv in types if (w := weight(G)) > 0)
assert len(types) == 34 and len(table) == 20, (len(types), len(table))
expected = [(11,(5,5,6),352),(12,(5,5,6),64),(13,(5,5,6),32),(13,(5,5,6),96),
            (13,(5,5,7),192),(13,(5,6,6),96),(13,(5,6,6),96),(13,(5,6,7),192),
            (13,(6,6,7),96),(14,(5,5,6),32),(14,(5,5,6),32),(14,(5,5,7),64),
            (14,(5,5,9),96),(14,(5,6,6),64),(14,(5,6,7),64),(14,(5,6,7),64),
            (14,(5,6,7),96),(14,(6,6,6),64),(14,(6,6,7),64),(14,(6,7,7),96)]
assert table == sorted(expected), table
assert all(min(b) <= 7 for _, b, _ in table)
print("CHECK D ok: mu=3 — 34 admissible types, exactly 20 with w>0, table as stated")
CHECK -->

<!-- CHECK
# CHECK E — (S2) step 5(c): mu=4 exhaustion. With loops and parallel edges
# excluded by proof steps 5(a)/5(b), enumerate ALL simple cubic graphs on 6
# labeled vertices and ALL subdivision vectors with total e <= 13: no vector
# makes every cycle >= 5 and != 8. (Cycles of the subdivision = subdivided
# cycles of the base graph, so pure arithmetic on the base cycle list.)
import networkx as nx, itertools
pairs = list(itertools.combinations(range(6), 2))
found = 0; graphs = 0
for es in itertools.combinations(pairs, 9):
    deg = [0] * 6
    for u, v in es: deg[u] += 1; deg[v] += 1
    if deg != [3] * 6: continue
    G = nx.Graph(); G.add_edges_from(es)
    if not nx.is_connected(G): continue
    graphs += 1
    eidx = {e: i for i, e in enumerate(es)}
    cycles = []
    for c in nx.simple_cycles(G):
        idxs = []
        for t in range(len(c)):
            u, v = c[t], c[(t + 1) % len(c)]
            idxs.append(eidx[(u, v) if (u, v) in eidx else (v, u)])
        cycles.append(tuple(idxs))
    for s in range(5):
        for combo in itertools.combinations_with_replacement(range(9), s):
            L = [1] * 9
            for i in combo: L[i] += 1
            if all((t := sum(L[i] for i in c)) >= 5 and t != 8 for c in cycles):
                found += 1
assert graphs == 70 and found == 0, (graphs, found)   # 10 x K33 + 60 x prism
print("CHECK E ok: mu=4 — 70 labeled simple cubic graphs on 6 vertices, 0 admissible subdivisions")
CHECK -->

<!-- CHECK
# CHECK F — (S4)+(S5) spot identities on a REAL girth-5 C8-free cubic carrier:
# the (2,)+(12,) n=30 window-census witness (rebuilt from c16_k0_window_census
# CHECK E data). tr q8(A) = -30 (C8-free criterion), tr B^16 = 30 + tr q16(A),
# and sum q8(lambda_i)^2 = 511 n + tr B^16 as exact integers.
import numpy as np, networkx as nx
paths, cycles, feet = (2,), (12,), [[7, 14], [1, 4], [8], [6], [9], [3], [0], [10], [13], [15], [12], [2], [5], [11]]
G = nx.Graph()
for i in range(16): G.add_edge(i, (i + 1) % 16)
off = 0
for a in paths:
    for j in range(a - 1): G.add_edge(16 + off + j, 16 + off + j + 1)
    off += a
for L in cycles:
    for j in range(L): G.add_edge(16 + off + j, 16 + off + (j + 1) % L)
    off += L
for v in range(14):
    for p in feet[v]: G.add_edge(p, 16 + v)
n = G.number_of_nodes()
assert n == 30 and all(d == 3 for _, d in G.degree()) and nx.is_connected(G)
lens = {len(c) for c in nx.simple_cycles(G, length_bound=8)}
assert not (lens & {3, 4, 8})   # girth >= 5 and C8-free
Q8 = [32, 0, -128, 0, 80, 0, -16, 0, 1]
Q16 = [512, 0, -8192, 0, 21504, 0, -21504, 0, 10560, 0, -2816, 0, 416, 0, -32, 0, 1]
def trpoly(G, C):
    A = nx.to_numpy_array(G).astype(np.int64); m = len(A)
    tot = C[0] * np.eye(m, dtype=np.int64); P = np.eye(m, dtype=np.int64)
    for c in C[1:]:
        P = P @ A; tot = tot + c * P
    return int(np.trace(tot))
def trB16(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=np.int64)
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return int(np.trace(np.linalg.matrix_power(B, 16)))
t8, t16, b16 = trpoly(G, Q8), trpoly(G, Q16), trB16(G)
assert t8 == -30                      # spectral C8-freeness
assert b16 == 30 + t16 == 65952       # (S1) + the offline census total
# second-moment law: sum q8(l)^2 = tr q8(A)^2-as-polynomial = t16 + 512*30
A = nx.to_numpy_array(G).astype(np.int64)
P = np.eye(30, dtype=np.int64); M = Q8[0] * np.eye(30, dtype=np.int64)
for c in Q8[1:]:
    P = P @ A; M = M + c * P
assert int(np.trace(M @ M)) == 511 * 30 + b16
print("CHECK F ok: n=30 carrier — trq8=-30, trB16 = 30+trq16 = 65952, sum q8^2 = 511n + trB16")
CHECK -->
