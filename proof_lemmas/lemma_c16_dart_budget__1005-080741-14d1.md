---
id: c16_dart_budget
status: open
depends_on: [c16_capacity_girth9, nb_trace_c8_identity, nb_trace_c16_support_census, cubic_girth5_moment_dictionary]
introduced_at_round: 111
---

# Lemma `c16_dart_budget` (host-aware anchored-walk capacity: $K_5, K_6, K_7 \to K_5', K_6', K_7' = 89464, 28848, 29536$ — a $4.11\times / 3.62\times / 1.82\times$ cut of the capacity functional, and the first nontrivial short-cycle population floors)

**Setting.** As in `c16_capacity_girth9`: $G$ is a finite simple cubic
graph with girth $\ge 5$ and no $8$-cycle; $B$ its non-backtracking
(dart) operator; $c_\ell(G)$ the number of unoriented $\ell$-cycles.
For a closed NB $16$-walk $w$ (a dart sequence $d_1,\dots,d_{16}$ with
$d_{i+1}$ following $d_i$ and $d_1$ following $d_{16}$, the cyclic NB
condition included — exactly what $\operatorname{tr} B^{16}$ counts,
rooted), $\operatorname{supp}(w)$ is the set of (unoriented) edges
traversed. By census (S2)/(S3) + `c16_capacity_girth9` (K1), every
closed NB $16$-walk in such a $G$ has support either a $16$-cycle or
one of the $39$ composite types; every composite type has girth
$\gamma \in \{5,6,7\}$ and cycle rank $\mu + 1 \le 3$ ($5$ dumbbells
and $14$ thetas of rank $2$, $20$ types of rank $3$).

**Statement.**

- **(B1) (anchored walk bound)** Let $Z$ be an $\ell$-cycle of $G$,
  $\ell \in \{5,6,7\}$. Then
  $$W_\ell(Z) \;:=\; \#\{\,w \text{ rooted closed NB } 16\text{-walk}:
    \operatorname{supp}(w) \supseteq E(Z),\;
    \operatorname{girth}(\operatorname{supp}(w)) = \ell\,\}
    \;\le\; K_\ell',$$
  with
  $$K_5' = 89464, \qquad K_6' = 28848, \qquad K_7' = 29536.$$
  The constants are host-independent: they are computed by an
  exhaustive, finitely-branching enumeration of canonical anchored
  walk patterns (CHECK A) and are valid for EVERY cubic girth-$\ge 5$
  $C_8$-free host.
- **(B2) (aggregate capacity, replacing (K3) of `c16_capacity_girth9`)**
  $$\operatorname{tr} B^{16} - 32\,c_{16} \;\le\;
    K_5'\,c_5 + K_6'\,c_6 + K_7'\,c_7
    \;=\; 89464\,c_5 + 28848\,c_6 + 29536\,c_7,$$
  a $4.11\times / 3.62\times / 1.82\times$ reduction of the capacity
  functional's coefficients. (The right side remains a spectral
  functional via `cubic_girth5_moment_dictionary`.)
- **(B3) (squeeze re-test — verdict unchanged, honest)** On the
  $n = 30$ window-census carrier ($c_5, c_6, c_7, c_{16} =
  5, 12, 8, 750$; composite mass $41952$): the new cap evaluates to
  $1029784$ — a $24.5\times$ overshoot (was $83.9\times$). The
  one-anchor cost $\min_\ell K_\ell' = 28848$ is still below the S5
  mass requirement only for $n > 74$, so the two-sided squeeze still
  closes exactly the girth-$\ge 9$ stratum ((K4) of
  `c16_capacity_girth9` is unaffected; it used only
  $c_5 = c_6 = c_7 = 0$).
- **(B4) (population floors — unconditional, new)** Let $G$ be a
  connected cubic Erdős–Gyárfás counterexample ($c_4 = c_8 = c_{16}
  = 0$) with girth $\ge 5$ on $n$ vertices, $30 \le n \le 130$. Then
  $$89464\,c_5 + 28848\,c_6 + 29536\,c_7 \;\ge\; R(n)
    \;:=\; 66049 + \frac{(n+257)^2}{n-1} - 511\,n \;>\; 0 .$$
  In particular (CHECK C, exact arithmetic): if $G$ has girth $6$
  then $c_6 + c_7 \ge 2$ for all even $n \le 74$; if $G$ has girth
  $7$ then $c_7 \ge 2$ for all even $n \le 74$. With the old
  constants every such floor was the trivial $\ge 1$; these are the
  first spectral population floors above the definitional minimum.

**Proof.**

*Reduction of (B2) to (B1).* By the census decomposition, the
composite mass $M := \operatorname{tr} B^{16} - 32 c_{16}$ counts the
rooted closed NB $16$-walks whose support is a composite type. Each
such support $S$ has girth $\gamma(S) \in \{5,6,7\}$; designate
$\operatorname{can}(S)$, the lexicographically least minimum-length
cycle of $S$ (any fixed choice works). Mapping each composite walk $w$
to $Z = \operatorname{can}(\operatorname{supp}(w))$ — an $\ell$-cycle
of $G$ with $\ell = \operatorname{girth}(\operatorname{supp}(w))$ —
gives
$$M = \sum_{\ell \in \{5,6,7\}} \sum_{Z\; \ell\text{-cycle of } G}
  \#\{w : \operatorname{can}(\operatorname{supp}(w)) = Z\}
  \;\le\; \sum_{\ell} \sum_{Z} W_\ell(Z)
  \;\le\; K_5' c_5 + K_6' c_6 + K_7' c_7. \qquad \square$$

*Proof of (B1).* Fix $G$ and the $\ell$-cycle $Z$, with vertices
labeled $z_0, \dots, z_{\ell-1}$ in cycle order.

1. *(Rotation offsets.)* Every walk counted by $W_\ell(Z)$ traverses
   the anchor edge $\{z_0, z_1\}$ at least once (coverage). Rotate
   the dart sequence to start at the FIRST traversal of
   $\{z_0, z_1\}$ at-or-after the root; recording the rotation amount
   $k$ gives an injection
   $$w \;\longmapsto\; (\text{rotated walk } P,\; k), \qquad
     0 \le k \le 16 - L(P),$$
   where $L(P)$ is the $1$-based position of the LAST
   $\{z_0,z_1\}$-traversal in $P$ (the last $k$ steps of $P$ must be
   traversal-free for the un-rotation to have its first traversal at
   step $1$). Hence
   $W_\ell(Z) \le \sum_{P} (17 - L(P)) \cdot \#\{\text{walks
   realizing } P\}$, the sum over rotated walks grouped by canonical
   pattern $P$ (next item), split by the direction ($z_0 \to z_1$ or
   $z_1 \to z_0$) of step $1$.
2. *(Canonical patterns.)* The pattern of a rotated walk records, per
   step, the abstract label of the next vertex: $Z$-vertices carry
   their fixed labels; external vertices are labeled in order of
   first appearance. The pattern determines the sequence of
   known-edge re-traversals, fresh-vertex steps, and identification
   steps (a new edge between two already-labeled vertices).
3. *(Realization bound — slot allocation.)* By induction on remaining
   steps: from the current host vertex $x$ (image of pattern vertex
   $cur$, entered from $\psi(prev)$), the walk's next host vertex is
   one of the $\le 3$ neighbors of $x$, excluding $\psi(prev)$
   (non-backtracking; simple graph). Neighbors along already-known
   edges contribute their full pattern-subtree bounds. The remaining
   host neighbors number at most $s = 3 - \deg_{\mathrm{known}}(x)$,
   are pairwise distinct vertices, and each is either unlabeled
   (continuations bounded by the fresh-vertex subtree value, usable
   for every slot) or equal to one specific labeled vertex $v$
   (continuations bounded by the identification subtree for $v$,
   usable at most once). Hence the unknown-slot contribution is at
   most the sum of the $s$ largest values of the multiset
   $\{v_{\mathrm{new}} \times s\} \cup \{v_{\mathrm{ident}}(v)\}_v$.
   CHECK A's recursion computes exactly this.
4. *(Pruning soundness.)* The known graph (all of $Z$, plus every
   edge the pattern has used) is a subgraph of $G$ at all times.
   (i) An identification edge closing — together with known edges — a
   cycle of length $3$, $4$, or $8$ would place that cycle in $G$:
   excluded, since $G$ has girth $\ge 5$ and no $C_8$. All new host
   cycles pass through the new edge, so checking simple paths of
   length $2, 3, 7$ between its endpoints is complete.
   (ii) The traversed subgraph is contained in the final support, so
   a $5$-cycle (resp. $5$- or $6$-cycle) among traversed edges
   contradicts $\operatorname{girth}(\operatorname{supp}) = 6$
   (resp. $7$): such patterns are excluded from $W_6$ (resp. $W_7$).
   (iii) The support's cycle rank is at most $3$ (census, header);
   the traversed subgraph is connected with monotonically
   non-decreasing rank along the walk, and every still-uncovered
   $Z$-edge whose endpoints already lie in the traversed subgraph
   adds $+1$ rank when eventually traversed (coverage forces it):
   patterns whose guaranteed final rank exceeds $3$ are excluded.
   (iv) Budget prunes (remaining steps vs. uncovered $Z$-edges,
   closure and cyclic-NB at the root) are immediate.
5. *(Finiteness and the constants.)* The recursion branches finitely
   (at most $2$ known continuations, one fresh class, at most
   $|V_{\mathrm{labeled}}|$ identifications per step) and terminates
   at depth $16$; CHECK A runs it for $\ell = 5, 6, 7$ and both
   directions of step $1$ (which agree, as forced by the reflection
   automorphism of the initial state) and outputs
   $(89464, 28848, 29536)$. $\square$

*Proof of (B3).* Arithmetic on the carrier invariants, re-verified in
CHECK B/C: $89464 \cdot 5 + 28848 \cdot 12 + 29536 \cdot 8 = 1029784$
against mass $41952$. $\square$

*Proof of (B4).* For such $G$: $c_4 = c_8 = c_{16} = 0$, so census
(S5) (Cauchy–Schwarz on $q_8$, $\lambda_1 = 3$, connected) gives
$\operatorname{tr} B^{16} \ge R(n)$, and (B2) with $c_{16} = 0$ gives
$\operatorname{tr} B^{16} \le K_5' c_5 + K_6' c_6 + K_7' c_7$. If
girth $= 6$ then $c_5 = 0$ and $K_6' c_6 + K_7' c_7 \le 29536
(c_6 + c_7)$, so $c_6 + c_7 \ge R(n)/29536 > 1$ for even
$n \in [30, 74]$ (CHECK C: $R(74) = 29736\tfrac{57}{73} > 29536$,
$R(76) = 28692\tfrac{3}{25} < 29536$); $c_6 + c_7 \ge 2$. Girth $7$:
likewise with $c_6 = 0$, $c_7 \ge R(n)/29536 > 1$. $\square$

**Scope notes (honest, program-facing).**

1. **What improved and what did not.** The squeeze verdict for the
   girth-$5$ stratum is STILL negative: $K_5' = 89464$ exceeds the S5
   requirement $R(n) \le R(30) = 53559.3$ for the whole F3-truncated
   window, so one $5$-cycle still "pays" for the required mass. The
   deliverables are the $4.11\times/3.62\times/1.82\times$ constant
   cuts (feeding any later per-$n$ or $k=32$ refinement) and the
   first nontrivial floors (B4).
2. **Tightness.** On the carrier the worst anchored actuals are
   $4032 / 2240 / 896$ ($\ell = 5/6/7$, girth-restricted attribution,
   CHECK B) against $89464 / 28848 / 29536$ — a further $\sim 22\times
   / 13\times / 33\times$ of slack remains in the slot-allocation
   factor-$2$s
   (fresh steps never die in the abstract enumeration; in a real
   host most die on closure). The visible next cut: replace the
   fresh-step factor $2$ by the ear-automaton residue tables of
   `mod8_ladder_L3` (Section 146) — host-aware transition counts —
   or stack the $k = 32$ moment (needs the $k=32$ support census,
   offline-sized).
3. The $(17 - L)$ offset weighting is what the blanket $16\times$
   rotation factor sharpens to; it alone is worth $\sim 10\%$. The
   support-girth restriction (girth $= \ell$ in the attribution) is
   worth $21\%$ on $K_6'$ and $5\%$ on $K_7'$; the census rank-$\le 3$
   prune is binding only jointly with the budget prunes.
4. (B1) is stated for girth-$\ge 5$ $C_8$-free cubic hosts (the
   pruning uses both); unlike (K2) of `c16_capacity_girth9` it is NOT
   a statement about arbitrary cubic hosts. (B4) inherits the
   standing cubic-stratum scope; girth $3$ is outside the spectral
   program, per the program's stratification.

<!-- CHECK
# CHECK A — (B1): the anchored-pattern enumeration. Recomputes K5', K6',
# K7' from scratch (exhaustive canonical-pattern DFS with slot-allocation
# realization bounds, girth/C8 host pruning, support-girth and rank<=3
# pruning, offset weights) and asserts (89464, 28848, 29536), with the
# two step-1 directions agreeing per anchor length.
import sys
sys.setrecursionlimit(100000)
STEPS = 16
FORBID = {5: (), 6: (4,), 7: (4, 5)}  # TRAV path lengths closing C5 / C5,C6

def compute_K(ell):
    FULL = (1 << ell) - 1
    ZE = [tuple(sorted((i, (i + 1) % ell))) for i in range(ell)]
    fb = FORBID[ell]
    def zbit(u, v):
        if u < ell and v < ell:
            if abs(u - v) == 1: return 1 << min(u, v)
            if {u, v} == {0, ell - 1}: return 1 << (ell - 1)
        return 0
    per_dir = []
    for first in ((0, 1), (1, 0)):
        adj = {i: {(i - 1) % ell, (i + 1) % ell} for i in range(ell)}
        root = first[0]
        sadj = {}
        def sadd(u, v):
            if v in sadj.get(u, ()): return False
            sadj.setdefault(u, set()).add(v); sadj.setdefault(v, set()).add(u)
            return True
        def sdel(u, v):
            sadj[u].discard(v); sadj[v].discard(u)
            if not sadj[u]: del sadj[u]
            if not sadj[v]: del sadj[v]
        def bad_host_path(src, dst):
            found = [False]
            def dfs(v, visited, depth):
                if found[0] or depth >= 7: return
                for w in adj[v]:
                    if w == dst:
                        if depth + 1 in (2, 3, 7): found[0] = True; return
                    elif w not in visited:
                        visited.add(w); dfs(w, visited, depth + 1); visited.discard(w)
                        if found[0]: return
            dfs(src, {src}, 0)
            return found[0]
        def bad_supp_path(src, dst):
            if not fb: return False
            found = [False]; mx = max(fb)
            def dfs(v, visited, depth):
                if found[0] or depth >= mx: return
                for w in sadj.get(v, ()):
                    if w == dst:
                        if depth + 1 in fb: found[0] = True; return
                    elif w not in visited:
                        visited.add(w); dfs(w, visited, depth + 1); visited.discard(w)
                        if found[0]: return
            dfs(src, {src}, 0)
            return found[0]
        def rank_bad(covered):
            e = sum(len(s) for s in sadj.values()) // 2
            r = e - len(sadj) + 1
            for b in range(ell):
                if not (covered >> b) & 1:
                    i, j = ZE[b]
                    if i in sadj and j in sadj: r += 1
            return r > 3
        def rec(cur, prev, covered, step, nverts, last):
            if step == STEPS:
                return (17 - last) if (cur == root and prev != first[1]
                                       and covered == FULL) else 0
            rem = STEPS - step
            unc = ell - bin(covered).count("1")
            if rem < unc + (1 if (cur >= ell and unc > 0) else 0): return 0
            total = 0
            def attempt(w, cov2, nv2, lst):
                newe = sadd(cur, w)
                val = 0
                if not (newe and rank_bad(cov2)):
                    val = rec(w, cur, cov2, step + 1, nv2, lst)
                if newe: sdel(cur, w)
                return val
            for w in list(adj[cur]):
                if w == prev: continue
                if (w not in sadj.get(cur, ())) and bad_supp_path(cur, w): continue
                lst = step + 1 if {cur, w} == {0, 1} else last
                total += attempt(w, covered | zbit(cur, w), nverts, lst)
            slots = 3 - len(adj[cur])
            if slots > 0:
                nv = nverts
                adj[nv] = {cur}; adj[cur].add(nv)
                v_new = attempt(nv, covered, nverts + 1, last)
                adj[cur].remove(nv); del adj[nv]
                opts = []
                for w in list(adj.keys()):
                    if w == cur or w in adj[cur] or len(adj[w]) >= 3: continue
                    if bad_host_path(cur, w) or bad_supp_path(cur, w): continue
                    adj[cur].add(w); adj[w].add(cur)
                    v_w = attempt(w, covered | zbit(cur, w), nverts, last)
                    adj[cur].remove(w); adj[w].remove(cur)
                    if v_w: opts.append(v_w)
                total += sum(sorted(opts + [v_new] * slots, reverse=True)[:slots])
            return total
        sadd(*first)
        per_dir.append(rec(first[1], first[0], zbit(*first), 1, ell, 1))
        sdel(*first)
    assert per_dir[0] == per_dir[1], (ell, per_dir)  # reflection symmetry
    return per_dir[0] + per_dir[1]

K = {ell: compute_K(ell) for ell in (5, 6, 7)}
assert K == {5: 89464, 6: 28848, 7: 29536}, K
old = {5: 367360, 6: 104448, 7: 53760}
print("CHECK A ok: K' =", K,
      "improvements:", {l: round(old[l] / K[l], 2) for l in (5, 6, 7)})
CHECK -->

<!-- CHECK
# CHECK B — (B1) empirical validation on the n=30 window-census carrier
# (girth 5, C8-free): exact enumeration of ALL rooted closed cyclic-NB
# 16-walks (total must equal tr B^16 = 65952), support attribution, and
# W_ell(Z) <= K_ell' for every one of the 5+12+8 anchor cycles, with the
# support-girth restriction of the attribution. Also: the attribution
# chain covers the composite mass (sum over anchors >= M = 41952).
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
assert G.number_of_nodes() == 30 and all(d == 3 for _, d in G.degree())
edges = sorted(tuple(sorted(e)) for e in G.edges())
eidx = {e: i for i, e in enumerate(edges)}
darts = [(u, v) for u, v in edges] + [(v, u) for u, v in edges]
didx = {d: i for i, d in enumerate(darts)}
nd = len(darts)
succ = [[didx[(v, w)] for w in G.neighbors(v) if w != u] for (u, v) in darts]
R1 = np.zeros((nd, nd), dtype=bool)
for i in range(nd):
    for j in succ[i]: R1[i, j] = True
R = [np.eye(nd, dtype=bool), R1]
for k in range(2, 16):
    R.append((R[-1].astype(np.int8) @ R1.astype(np.int8)) > 0)
support_counts, total = {}, 0
ebit = [1 << eidx[tuple(sorted(d))] for d in darts]
for s in range(nd):
    tgt = np.array([s in succ[t] for t in range(nd)], dtype=bool)
    stack = [(s, 1, ebit[s])]
    while stack:
        d, step, mask = stack.pop()
        rem = 16 - step
        for e in succ[d]:
            if rem == 1:
                if tgt[e]:
                    m2 = mask | ebit[e]
                    total += 1
                    support_counts[m2] = support_counts.get(m2, 0) + 1
            elif R[rem - 1][e][tgt].any():
                stack.append((e, step + 1, mask | ebit[e]))
assert total == 65952, total
def mask_girth(mask):
    H = nx.Graph(e for i, e in enumerate(edges) if (mask >> i) & 1)
    best = 99
    for c in nx.simple_cycles(H, length_bound=7):
        best = min(best, len(c))
    return best
girth_of = {m: mask_girth(m) for m in support_counts}
K = {5: 89464, 6: 28848, 7: 29536}
anchors, worst, sumW = [], {5: 0, 6: 0, 7: 0}, 0
for c in nx.simple_cycles(G, length_bound=7):
    l = len(c)
    if l in (5, 6, 7):
        em = 0
        for i in range(l):
            em |= 1 << eidx[tuple(sorted((c[i], c[(i + 1) % l])))]
        anchors.append((l, em))
assert {l: sum(1 for x, _ in anchors if x == l) for l in (5, 6, 7)} == {5: 5, 6: 12, 7: 8}
for l, em in anchors:
    W = sum(cnt for m, cnt in support_counts.items()
            if (m & em) == em and girth_of[m] == l)
    assert W <= K[l], (l, W, K[l])
    worst[l] = max(worst[l], W); sumW += W
M = 65952 - 32 * 750
assert sumW >= M, (sumW, M)
print(f"CHECK B ok: 65952 walks, worst anchored actuals {worst} <= K' {K}; "
      f"attribution sum {sumW} >= composite mass {M}")
CHECK -->

<!-- CHECK
# CHECK C — (B2)+(B3)+(B4) in exact arithmetic: the carrier squeeze
# re-test (cap 1029784, mass 41952, 24.5x overshoot, verdict unchanged)
# and the population floors: R(n) > 29536 for even n in [30, 74] and
# R(76) < 29536 (floors c6+c7 >= 2 at girth 6, c7 >= 2 at girth 7,
# for even n in [30, 74]); R(n) > 0 up to n = 130; K5' > R(30) (the
# girth-5 squeeze stays open, honestly).
from fractions import Fraction
K5, K6, K7 = 89464, 28848, 29536
def R(n): return 66049 + Fraction((n + 257) ** 2, n - 1) - 511 * n
cap = K5 * 5 + K6 * 12 + K7 * 8
mass = 65952 - 32 * 750
assert cap == 1029784 and mass == 41952
assert Fraction(cap, mass) > 24 and Fraction(cap, mass) < 25
assert all(R(n) > 29536 for n in range(30, 75, 2))
assert R(74) > 29536 and R(76) < 29536
assert all(R(n) > 0 for n in range(30, 131, 2)) and R(132) < 0
assert K5 > R(30)                      # girth-5 squeeze still open
assert max(K5, K6, K7) < 367360        # strict improvement vs old K5
print("CHECK C ok: cap 1029784 vs mass 41952 (24.5x); floors c6+c7>=2 "
      "(girth 6) and c7>=2 (girth 7) for even n in [30,74]; R>0 to n=130")
CHECK -->
