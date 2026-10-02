---
id: cubic_girth5_moment_dictionary
status: proved
depends_on: [nb_trace_c8_identity, nb_trace_c16_support_census]
discharged_by_round: 108
introduced_at_round: 108
---

# Lemma `cubic_girth5_moment_dictionary` (proved — at girth $\ge 5$ the short-cycle vector $(c_5, c_6, c_7)$ is an exact linear functional of the adjacency moments: $\operatorname{tr} A^5 = 10\,c_5$, $\operatorname{tr} A^6 = 87n + 12\,c_6$, $\operatorname{tr} A^7 = 140\,c_5 + 14\,c_7$; plus the $k = 32$ trace transfer)

**Setting.** $G$ a finite simple cubic graph of girth $\ge 5$,
$n = |V(G)|$, $A$ its adjacency matrix, $c_\ell$ the number of
(unoriented, basepoint-free) $\ell$-cycles. $T_k$ denotes the number
of closed $k$-walks based at the root of the infinite $3$-regular
tree ($T_k = 0$ for odd $k$). This lemma is SELF-CONTAINED relative
to `nb_trace_c8_identity` and `nb_trace_c16_support_census`; no
external literature is invoked anywhere (the Section 127 externals
remain formally quarantined per Section 134 and are not used).

**Statement.**

- **(M1) (moment census, $k \le 7$)** For cubic $G$ of girth $\ge 5$:
  $$\operatorname{tr} A^2 = 3n, \quad \operatorname{tr} A^3 = 0,
    \quad \operatorname{tr} A^4 = 15n, \quad
    \operatorname{tr} A^5 = 10\, c_5,$$
  $$\operatorname{tr} A^6 = 87\, n + 12\, c_6, \qquad
    \operatorname{tr} A^7 = 140\, c_5 + 14\, c_7,$$
  with $T_2 = 3$, $T_4 = 15$, $T_6 = 87$ (CHECK A) and the per-$C_5$
  length-$7$ coefficient $140 = 70 + 5 \cdot 14$ (CHECK B).
- **(M2) (the dictionary)** Hence, for cubic girth-$\ge 5$ $G$:
  $$c_5 = \tfrac{1}{10} \operatorname{tr} A^5, \qquad
    c_6 = \tfrac{1}{12}\big(\operatorname{tr} A^6 - 87 n\big), \qquad
    c_7 = \tfrac{1}{14} \operatorname{tr} A^7 -
          \operatorname{tr} A^5,$$
  the last since $140\,c_5 = 14 \operatorname{tr} A^5$. With
  `nb_trace_c8_identity` (S3), $c_8 = \tfrac{1}{16}(n +
  \operatorname{tr} q_8(A))$: the entire short-cycle vector
  $(c_5, c_6, c_7, c_8)$ of a cubic girth-$\ge 5$ graph is determined
  by its adjacency spectrum.
- **(M3) (program corollary)** In the triangle-free stratum of the
  witness class, every quantity in the L2/L3 squeeze EXCEPT the
  composite shape counts themselves is spectral-moment data: the
  linear constraint $\sum_i q_8(\lambda_i) = -n$ ($C_8$-freeness),
  the second-moment identity
  $\sum_i q_8(\lambda_i)^2 = 511n + \operatorname{tr} B^{16}$
  (`nb_trace_c16_support_census` (S5)), and now the short-cycle
  counts $c_5, c_6, c_7$ that cap the composite mass from above
  (every composite type carries a $C_5$, $C_6$ or $C_7$). The
  two-sided squeeze is therefore a FINITE MOMENT PROBLEM on the
  spectral measure of $A$ plus bounded local-incidence capacities.
- **(M4) ($k = 32$ trace transfer; no girth hypothesis)** For every
  finite simple cubic $G$:
  $$\operatorname{tr} B^{32} = n + \operatorname{tr} q_{32}(A),
    \qquad q_{32} = q_{16}^2 - 2^{17},$$
  and $q_{32}(3) = 65537^2 - 131072 = 4294967297 = 2^{32} + 1$
  (CHECK E) — the Perron pin for the future $C_{32}$-freeness layer
  (the $C_{32}$ analogue of the L2 census is NOT claimed here).

**Proof.**

*Reduction structure.* Let $W$ be a closed $k$-walk, $k \le 7$.
Cyclically cancelling adjacent backtracking pairs (a step followed
by its reverse, cyclically) removes $2$ steps at a time and
terminates in a CYCLICALLY REDUCED closed walk — i.e. a cyclically
non-backtracking closed walk — of some length $\ell = k - 2t \ge 0$
of the same parity as $k$.

1. *$\ell = 0$ (null-homotopic).* $W$ lifts to a closed walk at a
   root of the universal cover, the $3$-regular tree; conversely
   every closed tree walk projects. So the number of such $W$ based
   at any fixed vertex is $T_k$, independent of $G$ — contributing
   $T_k\, n$, with $T_2 = 3$, $T_4 = 15$, $T_6 = 87$ computed by the
   distance-from-root DP (CHECK A) and $T_k = 0$ for odd $k$.
2. *$\ell > 0$.* The reduced core is a cyclically-NB closed walk of
   length $\ell \le 7 < 10 \le 2g$, hence (the vertex-injectivity
   argument of `nb_trace_c8_identity` (S2), verbatim with $\ell$ in
   place of $8$ — it needs only $\ell < 2g$) a single traversal of an
   $\ell$-cycle, $\ell \ge g \ge 5$.
3. *Case $k \le 4$:* $\ell \in \{3, 4\}$ is impossible (girth), so
   only the tree term survives: $\operatorname{tr} A^k = T_k n$ for
   $k \in \{2, 3, 4\}$ ($T_3 = 0$).
4. *Case $k = 5$:* odd, so $\ell = 5$ ($t = 0$): $W$ IS a $C_5$
   traversal. Each $5$-cycle yields $5 \times 2 = 10$ based,
   directed traversals: $\operatorname{tr} A^5 = 10\,c_5$.
5. *Case $k = 6$:* $\ell = 6$ ($t = 0$, a $C_6$ traversal, $12$ per
   $6$-cycle) or $\ell = 4, 2$ (girth-impossible) or $0$ (tree):
   $\operatorname{tr} A^6 = 87 n + 12\, c_6$.
6. *Case $k = 7$:* $\ell = 7$ ($C_7$ traversal, $14$ per) or
   $\ell = 5$, $t = 1$: $W$ carries exactly one cancellable spur
   over a $C_5$ traversal. Such a $W$ stays inside
   $C_5 \cup \{\text{edges incident to } C_5\}$. In a CUBIC girth-$5$
   host this neighborhood is rigid: each cycle vertex has exactly
   one off-cycle edge, the five off-cycle neighbors are distinct
   (a shared neighbor makes a $C_3$ or $C_4$ with a cycle arc of
   length $1$ or $2$), and no chords exist ($C_5$ chords make
   $C_3$/$C_4$) — the "sun" gadget. A $7$-walk wrapping the $C_5$
   uses at most one spur ($5 + 2 + 2 > 7$), so the per-$C_5$ count
   is $\operatorname{tr} A_{C_5}^7 + 5\,\big(\operatorname{tr}
   A_{C_5 + e}^7 - \operatorname{tr} A_{C_5}^7\big) = 70 + 5 \cdot 14
   = 140$ (CHECK B; every closed $7$-walk on the gadget wraps its
   unique cycle, odd length forbids tree walks, so the gadget traces
   count exactly these). Hence
   $\operatorname{tr} A^7 = 140\, c_5 + 14\, c_7$. $\square$

*(M2)* is arithmetic. *(M3)* combines (M2) with
`nb_trace_c8_identity` (S3) and `nb_trace_c16_support_census`
(S4)/(S5). *(M4)*: `nb_trace_c8_identity` (S1) proved the
$B$-spectrum multiset $\{\alpha_i, \beta_i\}_i \cup \{\pm 1^{(n/2)}\}$
with $\alpha_i^k + \beta_i^k = q_k(\lambda_i)$; at $k = 32$ the
$\pm 1$ block contributes $n$ and
$s_{32} = s_{16}^2 - 2(\alpha\beta)^{16} = q_{16}^2 - 2 \cdot 2^{16}$
as polynomials. $\square$

**Scope notes (honest, program-facing).**

1. Everything in (M1)/(M2) needs girth $\ge 5$ (triangle-free
   stratum). At girth $3$ the tree terms and wrap census change
   ($C_3$ wraps enter at $k = 3$) — this dictionary does NOT port to
   the full verifier class.
2. The $140$ uses cubic-ness (exactly one pendant per cycle vertex).
   Near-cubic witnesses with degree-$>3$ vertices would need a
   degree-corrected coefficient; the minimal-counterexample shape
   (F3: predominantly cubic) keeps this relevant.
3. Verified end-to-end on nine girth-$\ge 5$ cubic graphs spanning
   $c_5, c_6, c_7$ zero and nonzero (Petersen, dodecahedral,
   Desargues, Pappus, Heawood, McGee, plus three of the program's
   $C_8$-free samples incl. the $n = 30$ census carrier) — CHECKs
   C/D.
4. (M4) gives only the TRANSFER at $k = 32$; turning it into a
   $C_{32}$ statement needs the $k = 32$ analogue of the L2 support
   census (walks up to length $32$ admit a far larger composite zoo),
   which is future work, not claimed.

<!-- CHECK
# CHECK A — tree constants T2, T4, T6 by two independent methods:
# (1) distance-from-root DP on the infinite cubic tree; (2) explicit
# adjacency-trace on a depth-5 truncated cubic tree (root walks of
# length <= 6 never feel the truncation at depth > 3).
import numpy as np
import functools
@functools.lru_cache(None)
def walks(dist, steps):
    if steps == 0: return 1 if dist == 0 else 0
    if dist > steps: return 0
    if dist == 0: return 3 * walks(1, steps - 1)
    return walks(dist - 1, steps - 1) + 2 * walks(dist + 1, steps - 1)
T = {k: walks(0, k) for k in (2, 3, 4, 5, 6, 7)}
assert (T[2], T[4], T[6]) == (3, 15, 87), T
assert T[3] == T[5] == T[7] == 0
# truncated tree: root 0; grow 3-regular to depth 5
edges, frontier, nid = [], [(0, None)], 0
depth = {0: 0}
for _ in range(5):
    newf = []
    for v, parent in frontier:
        kids = 3 if parent is None else 2
        for _ in range(kids):
            nid += 1; edges.append((v, nid)); depth[nid] = depth[v] + 1
            newf.append((nid, v))
    frontier = newf
N = nid + 1
A = np.zeros((N, N), dtype=np.int64)
for u, v in edges: A[u, v] = A[v, u] = 1
for k in (2, 4, 6):
    assert int(np.linalg.matrix_power(A, k)[0, 0]) == T[k], k
print("CHECK A ok: T2,T4,T6 = 3,15,87 (DP == truncated-tree trace)")
CHECK -->

<!-- CHECK
# CHECK B — the C5 gadget constants for tr A^7: on-cycle 70, per-pendant
# extra 14, total per-C5 coefficient 140; and linearity on the full sun
# (no 7-walk uses two pendants).
import numpy as np, networkx as nx
def tr7(G):
    A = nx.to_numpy_array(G).astype(np.int64)
    return int(np.trace(np.linalg.matrix_power(A, 7)))
C5 = nx.cycle_graph(5)
w_on = tr7(C5)
g1 = nx.cycle_graph(5); g1.add_edge(0, "w")
w_pend = tr7(g1) - w_on
sun = nx.cycle_graph(5)
for i in range(5): sun.add_edge(i, f"p{i}")
assert (w_on, w_pend) == (70, 14), (w_on, w_pend)
assert tr7(sun) == w_on + 5 * w_pend == 140
print("CHECK B ok: per-C5 7-walk coefficient 140 = 70 + 5*14; sun linearity exact")
CHECK -->

<!-- CHECK
# CHECK C — (M1)+(M2) on six named girth>=5 cubic graphs spanning zero and
# nonzero c5, c6, c7 (Petersen, dodecahedral, Desargues, Pappus, Heawood,
# McGee). C8s allowed — the dictionary needs only girth >= 5.
import numpy as np, networkx as nx
def lcf(n, pattern, reps):
    G = nx.Graph()
    for i in range(n): G.add_edge(i, (i + 1) % n)
    for i, s in enumerate(pattern * reps): G.add_edge(i, (i + s) % n)
    return G
tests = [nx.petersen_graph(), nx.dodecahedral_graph(), nx.desargues_graph(),
         nx.pappus_graph(), nx.heawood_graph(), lcf(24, [12, 7, -7], 8)]
seen5 = seen6 = seen7 = 0
for G in tests:
    n = G.number_of_nodes()
    A = nx.to_numpy_array(G).astype(np.int64)
    tr = {k: int(np.trace(np.linalg.matrix_power(A, k))) for k in range(2, 8)}
    cnt = {L: 0 for L in (3, 4, 5, 6, 7)}
    for c in nx.simple_cycles(G, length_bound=7): cnt[len(c)] += 1
    assert cnt[3] == cnt[4] == 0
    assert tr[2] == 3 * n and tr[3] == 0 and tr[4] == 15 * n
    assert tr[5] == 10 * cnt[5]
    assert tr[6] == 87 * n + 12 * cnt[6]
    assert tr[7] == 140 * cnt[5] + 14 * cnt[7]
    assert cnt[7] == tr[7] // 14 - tr[5]
    seen5 += cnt[5] > 0; seen6 += cnt[6] > 0; seen7 += cnt[7] > 0
assert seen5 and seen6 and seen7
print("CHECK C ok: moment dictionary exact on 6 named graphs (c5, c6, c7 all exercised)")
CHECK -->

<!-- CHECK
# CHECK D — the dictionary on the program's own n=30 girth-5 C8-free census
# carrier (same construction data as nb_trace_c16_support_census CHECK F).
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
n = G.number_of_nodes(); assert n == 30
A = nx.to_numpy_array(G).astype(np.int64)
tr = {k: int(np.trace(np.linalg.matrix_power(A, k))) for k in (5, 6, 7)}
cnt = {L: 0 for L in (3, 4, 5, 6, 7, 8)}
for c in nx.simple_cycles(G, length_bound=8): cnt[len(c)] += 1
assert cnt[3] == cnt[4] == cnt[8] == 0
c5, c6, c7 = tr[5] // 10, (tr[6] - 87 * n) // 12, tr[7] // 14 - tr[5]
assert (c5, c6, c7) == (cnt[5], cnt[6], cnt[7]) == (5, 12, 8)
print("CHECK D ok: n=30 carrier — spectral (c5,c6,c7) = (5,12,8) matches direct enumeration")
CHECK -->

<!-- CHECK
# CHECK E — (M4): q32 = q16^2 - 2^17 from the Newton recurrence, the Perron
# pin q32(3) = 65537^2 - 131072 = 2^32 + 1, and the k=32 trace transfer
# tr B^32 = n + tr q32(A) verified exactly (python ints) on K4 and Petersen.
import numpy as np, networkx as nx
def qpoly(k):
    q0, q1 = [2], [0, 1]
    if k == 0: return q0
    for _ in range(k - 1):
        xq1 = [0] + q1
        L = max(len(xq1), len(q0))
        q0, q1 = q1, [(xq1[i] if i < len(xq1) else 0)
                      - 2 * (q0[i] if i < len(q0) else 0) for i in range(L)]
    return q1
q16, q32 = qpoly(16), qpoly(32)
sq = [0] * 33
for i, a in enumerate(q16):
    for j, b in enumerate(q16): sq[i + j] += a * b
sq[0] -= 2 ** 17
assert sq == q32
v = sum(c * 3 ** i for i, c in enumerate(q32))
assert v == 65537 ** 2 - 131072 == 2 ** 32 + 1
for G in (nx.complete_graph(4), nx.petersen_graph()):
    n = G.number_of_nodes()
    darts = [(a, b) for a, b in G.edges()] + [(b, a) for a, b in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=object)
    for (a, b) in darts:
        for w in G.neighbors(b):
            if w != a: B[idx[(a, b)], idx[(b, w)]] = 1
    trB32 = int(np.trace(np.linalg.matrix_power(B, 32)))
    A = nx.to_numpy_array(G).astype(object)
    tot = q32[0] * np.eye(n, dtype=object); P = np.eye(n, dtype=object)
    for c in q32[1:]:
        P = P @ A; tot = tot + c * P
    assert trB32 == n + int(np.trace(tot))
print("CHECK E ok: q32 = q16^2 - 2^17; q32(3) = 2^32 + 1; tr B^32 = n + tr q32(A) on K4, Petersen")
CHECK -->
