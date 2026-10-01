---
id: nb_trace_c8_identity
status: proved
depends_on: []
discharged_by_round: 105
introduced_at_round: 105
---

# Lemma `nb_trace_c8_identity` (proved — the exact spectral criterion for $C_8$-freeness of cubic girth-$\ge 5$ graphs: $\operatorname{tr} B^8 = 16\,c_8 = n + \operatorname{tr} q_8(A)$)

**Setting.** $G$ a finite simple cubic graph, $n = |V(G)|$,
$A$ its adjacency matrix, $c_8 = c_8(G)$ the number of (unoriented,
basepoint-free) $8$-cycles. $B$ is the Hashimoto non-backtracking
(dart) matrix: rows/columns indexed by the $3n$ darts (oriented
edges) $(u, v)$, with $B_{(u,v),(v,w)} = 1$ iff $w \ne u$. Define

$$q_0(x) = 2,\quad q_1(x) = x,\quad q_k(x) = x\,q_{k-1}(x) - 2\,q_{k-2}(x),$$

so that (CHECK A)

$$q_8(x) = x^8 - 16x^6 + 80x^4 - 128x^2 + 32.$$

**Statement.**

- **(S1) (trace transfer — NO girth hypothesis)** For every finite
  simple cubic $G$:
  $$\operatorname{tr} B^8 \;=\; n + \operatorname{tr} q_8(A)
  \;=\; n + \sum_{i=1}^{n} q_8(\lambda_i),$$
  where $\lambda_1, \dots, \lambda_n$ are the adjacency eigenvalues.
- **(S2) (combinatorial meaning at girth $\ge 5$)** If $G$ has girth
  $\ge 5$, then $\operatorname{tr} B^8 = 16\, c_8$.
- **(S3) (the criterion)** For cubic $G$ of girth $\ge 5$:
  $$G \text{ is } C_8\text{-free} \iff \operatorname{tr} q_8(A) = -n
  \iff \sum_i q_8(\lambda_i) = -n,$$
  and in general $c_8 = \tfrac{1}{16}\big(n + \operatorname{tr} q_8(A)\big)$.
- **(S4) (girth sharpness)** (S2) FAILS at girth $3$ and $4$: $K_4$
  (girth $3$) has $\operatorname{tr} B^8 = 168$ but $c_8 = 0$;
  $K_{3,3}$ (girth $4$) has $\operatorname{tr} B^8 = 648$, $c_8 = 0$
  (a $C_4$ traversed twice is a cyclically-non-backtracking closed
  $8$-walk). (S1) holds in both. (CHECK C.)

**Proof.**

*(S1).* We prove, SELF-CONTAINED, the determinant factorization
(classically "Ihara–Bass", the name used descriptively — no external
result is invoked): for any finite simple $d$-regular $G$ with
$m = dn/2$ edges,
$$\det(I - uB) = (1 - u^2)^{m - n}\,
  \det\!\big(I - uA + (d-1)u^2 I\big).$$

Index the $2m$ darts. Let $J$ be the dart-reversal permutation matrix
($J^2 = I$; $J$ is a product of $m$ disjoint transpositions), and let
$K, L \in \{0,1\}^{2m \times n}$ be the target / source incidence
matrices: $K_{e,v} = [\,t(e) = v\,]$, $L_{e,v} = [\,s(e) = v\,]$.
Four one-line identities:
(a) $(L^{\top} K)_{u,v} = \#\{e : s(e) = u,\ t(e) = v\} = A_{uv}$;
(b) $K = JL$ (since $t(\bar e) = s(e)$), hence $JK = L$ and
$L^{\top} J K = L^{\top} L = dI$ (each vertex is the source of $d$
darts);
(c) $(K L^{\top})_{e,f} = [\,t(e) = s(f)\,]$, so
$B = K L^{\top} - J$ (the subtraction kills exactly the backtrack
dart $f = \bar e$, whose entry in $K L^{\top}$ is $1$);
(d) $\det(I + uJ) = (1 - u^2)^m$ and, for $u^2 \ne 1$,
$(I + uJ)^{-1} = (I - uJ)/(1 - u^2)$.
Now for $u^2 \ne 1$, using $\det(I - XY) = \det(I - YX)$
(Weinstein–Aronszajn, with $X = u (I + uJ)^{-1} K$ of size
$2m \times n$ and $Y = L^{\top}$):
$$\det(I - uB) = \det\big(I + uJ - u K L^{\top}\big)
 = (1 - u^2)^m \det\!\Big(I_n - \tfrac{u}{1 - u^2}
   L^{\top}(I - uJ)K\Big),$$
and $L^{\top}(I - uJ)K = L^{\top}K - u L^{\top} J K = A - u d I$ by
(a), (b), so the right factor equals
$(1 - u^2)^{-n} \det\big((1 - u^2)I - uA + u^2 d I\big)
 = (1 - u^2)^{-n} \det\big(I - uA + (d-1)u^2 I\big)$.
Both sides are polynomials in $u$, so the identity extends to all
$u$. Factoring the degree-$2m$ polynomial identity over $\mathbb{C}$:
$\det(I - uA + (d-1)u^2 I) = \prod_i (1 - \alpha_i u)(1 - \beta_i u)$
with $\alpha_i + \beta_i = \lambda_i$,
$\alpha_i \beta_i = d - 1$, and $\det(I - uB) =
\prod_{\mu \in \operatorname{spec} B}(1 - \mu u)$. Hence the
eigenvalue multiset of $B$ is exactly
$\{\alpha_i, \beta_i\}_{i=1}^n \cup \{+1^{(m-n)}, -1^{(m-n)}\}$
(verified numerically as a multiset on $K_4$, $K_{3,3}$, Petersen —
CHECK D). For cubic $d = 3$: $m - n = n/2$, $\alpha_i\beta_i = 2$.
The power sums $s_k = \alpha_i^k + \beta_i^k$ satisfy Newton's
recurrence $s_k = \lambda_i s_{k-1} - 2 s_{k-2}$ with $s_0 = 2$,
$s_1 = \lambda_i$ — i.e. $s_k = q_k(\lambda_i)$. Therefore
$$\operatorname{tr} B^8 = \sum_i q_8(\lambda_i)
  + \frac{n}{2}\big(1^8 + (-1)^8\big)
  = \operatorname{tr} q_8(A) + n. \qquad \square$$

*(S2).* $\operatorname{tr} B^8$ counts CYCLICALLY non-backtracking
closed dart sequences $e_1 \to e_2 \to \dots \to e_8 \to e_1$ (the
wrap-around step is also non-backtracking). Let $W$ be such a walk,
$g \ge 5$ the girth; note $8 < 2g$.

*Claim: $W$ is vertex-injective.* Suppose not; choose a repeated
vertex pair at minimal cyclic distance $j - i$ along $W$. The
minimal segment is then an internally vertex-injective closed walk,
i.e. a simple cycle $C_1$ of length $\ell := j - i \ge g$. The
complementary segment $W'$ is a closed walk of length
$s = 8 - \ell \le 8 - g < g$, non-backtracking at every INTERNAL
junction (those are junctions of $W$); only its basepoint may
backtrack. If $W'$ backtracks at its basepoint, strip the mutually
reverse first and last darts: the result is again a closed walk,
internally non-backtracking, of length $s - 2$. Iterate. Full
collapse is impossible: the innermost stripped pair would be two
consecutive mutually-reverse darts at an internal junction of $W$
(for $s' = 2$ the backtrack sits at the segment's midpoint, an
internal junction of $W$), contradicting that $W$ is cyclically
non-backtracking; $s' = 1$ is a loop edge, absent in a simple graph.
So the iteration reaches a CYCLICALLY non-backtracking closed walk
of some length $s' \le s < g$. By induction on length, a cyclically
non-backtracking closed walk is either vertex-injective — a simple
cycle, here of length $< g$, contradicting the girth — or repeats a
vertex, and the same decomposition yields a simple cycle of length
$\le s' < g$, again a contradiction. So no repeated vertex exists.

Hence $W$ is a vertex-injective closed walk of length $8$, i.e. a
traversal of an $8$-cycle. Conversely each $8$-cycle yields exactly
$2 \times 8 = 16$ such walks (orientation $\times$ starting dart),
all distinct, and distinct cycles yield distinct walks. So
$\operatorname{tr} B^8 = 16\,c_8$. $\square$

*(S3).* Combine (S1) and (S2); $C_8$-free $\iff c_8 = 0 \iff
\operatorname{tr} B^8 = 0 \iff \operatorname{tr} q_8(A) = -n$.
$\square$

*(S4).* Direct computation (CHECK C): the dart matrix of $K_4$
($24$ darts) has $\operatorname{tr} B^8 = 168 = 4 + \operatorname{tr}
q_8(A_{K_4})$ with $c_8 = 0$; $K_{3,3}$ ($18$ darts, girth $4$):
$\operatorname{tr} B^8 = 648 = 6 + \operatorname{tr} q_8(A)$,
$c_8 = 0$. $\square$

**Scope notes (honest, program-facing).**

1. The program's verifier class is cubic $\{C_4, C_8\}$-free, which
   ALLOWS triangles (girth $3$). (S1) holds there unconditionally,
   but (S2)/(S3) do NOT: at girth $3$, composite cyclically-NB
   $8$-walks (triangle + pentagon chains etc.) contribute — this is
   exactly Judge RIGOR's $n = 30$ falsifier observation (composite:
   simple $\approx 40{:}1$ for $16$-walks). The criterion (S3) is
   the exact tool for the TRIANGLE-FREE stratum, and the clean
   algebraic target for the L2 hunt: any $C_8$-freeness-aware lower
   bound on $\operatorname{tr} B^{16} - 32 c_{16}$ may use
   $\operatorname{tr} q_8(A) = -n$ as an exact linear constraint on
   the spectral measure in that stratum.
2. $q_8(\pm 3) = 6561 - 11664 + 6480 - 1152 + 32 = 257$; the
   constraint $\sum_i q_8(\lambda_i) = -n$ with $\lambda_1 = 3$
   (connected cubic) says the remaining spectrum must average
   $q_8 \approx -(257 + n)/(n-1) \to -1$: $C_8$-freeness pins the
   spectral measure against the $q_8$-negative window
   ($q_8(x) < 0$ exactly on the four intervals where
   $x^8 - 16x^6 + 80x^4 - 128x^2 + 32 < 0$). This is the L2 program's
   LP side.

<!-- CHECK
# CHECK A — q_8 from the recurrence q0=2, q1=x, qk = x q_{k-1} - 2 q_{k-2}
# (pure integer polynomial arithmetic), plus the q8(3) value used in scope
# note 2.
q0, q1 = [2], [0, 1]
for _ in range(7):
    xq1 = [0] + q1
    L = max(len(xq1), len(q0))
    q2 = [(xq1[i] if i < len(xq1) else 0) - 2 * (q0[i] if i < len(q0) else 0)
          for i in range(L)]
    q0, q1 = q1, q2
assert q1 == [32, 0, -128, 0, 80, 0, -16, 0, 1], q1
val3 = sum(c * 3**i for i, c in enumerate(q1))
assert val3 == 257, val3
print("CHECK A ok: q8 = x^8-16x^6+80x^4-128x^2+32; q8(3) = 257")
CHECK -->

<!-- CHECK
# CHECK B — (S1)+(S2)+(S3) on girth-5 and girth-6 cubic graphs:
# Petersen (n=10, c8=15) and Heawood (n=14, c8=21): the three
# quantities tr B^8, n + tr q8(A), 16*c8 agree; both graphs carry
# C8s and indeed tr q8(A) > -n.
import numpy as np, networkx as nx
Q8 = [32, 0, -128, 0, 80, 0, -16, 0, 1]
def tr_B8(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=np.int64)
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return int(np.trace(np.linalg.matrix_power(B, 8)))
def tr_q8A(G):
    A = nx.to_numpy_array(G).astype(np.int64)
    n = len(A); tot = Q8[0] * np.eye(n, dtype=np.int64); P = np.eye(n, dtype=np.int64)
    for c in Q8[1:]:
        P = P @ A; tot = tot + c * P
    return int(np.trace(tot))
def c8(G):
    return sum(1 for c in nx.simple_cycles(G, length_bound=8) if len(c) == 8)
for G, n_exp, c8_exp in ((nx.petersen_graph(), 10, 15), (nx.heawood_graph(), 14, 21)):
    n = G.number_of_nodes(); assert n == n_exp
    g = min(len(cy) for cy in nx.simple_cycles(G)); assert g >= 5
    t, s, c = tr_B8(G), tr_q8A(G), c8(G)
    assert c == c8_exp, (n, c)
    assert t == n + s == 16 * c, (t, n + s, 16 * c)
    assert s > -n   # C8s present <=> tr q8(A) > -n
print("CHECK B ok: Petersen & Heawood — tr B^8 = n + tr q8(A) = 16 c8 (240, 336)")
CHECK -->

<!-- CHECK
# CHECK C — (S4) girth sharpness: K4 (girth 3) and K33 (girth 4) satisfy
# (S1) but violate (S2) with c8 = 0; plus (S1) on five random cubic
# graphs with NO girth filter (trace transfer needs no girth).
import numpy as np, networkx as nx, random
Q8 = [32, 0, -128, 0, 80, 0, -16, 0, 1]
def tr_B8(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=np.int64)
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return int(np.trace(np.linalg.matrix_power(B, 8)))
def tr_q8A(G):
    A = nx.to_numpy_array(G).astype(np.int64)
    n = len(A); tot = Q8[0] * np.eye(n, dtype=np.int64); P = np.eye(n, dtype=np.int64)
    for c in Q8[1:]:
        P = P @ A; tot = tot + c * P
    return int(np.trace(tot))
def c8(G):
    return sum(1 for c in nx.simple_cycles(G, length_bound=8) if len(c) == 8)
K4 = nx.complete_graph(4); K33 = nx.complete_bipartite_graph(3, 3)
assert tr_B8(K4) == 168 and c8(K4) == 0 and 168 == 4 + tr_q8A(K4)
assert tr_B8(K33) == 648 and c8(K33) == 0 and 648 == 6 + tr_q8A(K33)
rng = random.Random(1001)
done = 0
while done < 5:
    G = nx.random_regular_graph(3, 14, seed=rng.randint(0, 10**6))
    if not nx.is_connected(G): continue
    assert tr_B8(G) == G.number_of_nodes() + tr_q8A(G)
    done += 1
print("CHECK C ok: S4 sharpness (K4: 168 vs 0; K33: 648 vs 0); S1 on 5 random cubic graphs")
CHECK -->
<!-- CHECK
# CHECK D — the B-spectrum multiset identity behind (S1): eig(B) equals
# {roots of x^2 - lambda x + (d-1)} over eig(A), plus +-1 each with
# multiplicity m-n. Verified on K4 (d=3), K33 (d=3), Petersen (d=3).
import numpy as np, networkx as nx
def dart_B(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)))
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return B
for G in (nx.complete_graph(4), nx.complete_bipartite_graph(3, 3), nx.petersen_graph()):
    n, m, d = G.number_of_nodes(), G.number_of_edges(), 3
    evB = sorted(np.linalg.eigvals(dart_B(G)), key=lambda z: (round(z.real, 6), round(z.imag, 6)))
    evA = np.linalg.eigvalsh(nx.to_numpy_array(G))
    pred = []
    for lam in evA:
        disc = complex(lam * lam - 4 * (d - 1)) ** 0.5
        pred += [(lam + disc) / 2, (lam - disc) / 2]
    pred += [1.0] * (m - n) + [-1.0] * (m - n)
    pred = sorted(map(complex, pred), key=lambda z: (round(z.real, 6), round(z.imag, 6)))
    assert len(evB) == len(pred) == 2 * m
    assert max(abs(a - b) for a, b in zip(evB, pred)) < 1e-6
print("CHECK D ok: spec(B) = {roots of x^2-lx+2} + {+-1 x (m-n)} on K4, K33, Petersen")
CHECK -->
