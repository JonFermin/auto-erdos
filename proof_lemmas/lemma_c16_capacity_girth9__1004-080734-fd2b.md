---
id: c16_capacity_girth9
status: proved
depends_on: [nb_trace_c8_identity, nb_trace_c16_support_census, cubic_girth5_moment_dictionary]
introduced_at_round: 110
---

# Lemma `c16_capacity_girth9` (proved — the capacity dictionary $N_T(G) \le \kappa(T)\, c_{\gamma(T)}(G)$ for all $39$ composite types, the aggregate cap on composite mass, and the first unconditional $C_{16}$ theorem: every connected cubic graph with girth $\ge 9$ on $n \le 130$ vertices contains a $16$-cycle)

**Setting.** $\mathcal{T}$ is the $39$-type composite table of
`nb_trace_c16_support_census` (S2)/(S3) (5 dumbbells, 14 thetas, 20
$\mu = 3$ types), with weights $w(T)$. For a graph $G$, $N_T(G)$ is
the number of subgraphs of $G$ isomorphic to $T$ (subgraph copies,
NOT induced), and $c_\ell(G)$ the number of (unoriented) $\ell$-cycles.
All hosts $G$ in this lemma are finite simple CUBIC graphs — the
capacity bound uses only $\Delta = 3$; girth/$C_8$ hypotheses enter
only where stated.

**Statement.**

- **(K1) (designation)** Every $T \in \mathcal{T}$ has girth
  $\gamma(T) \in \{5, 6, 7\}$ (its minimum cycle length; re-verifies
  the short-cycle claim inside census (S5)). Fix for each $T$ a
  canonical minimum-length cycle $C_T \subseteq T$ (CHECK A's
  deterministic choice).
- **(K2) (per-type capacity)** For every finite simple cubic $G$ and
  every $T \in \mathcal{T}$:
  $$N_T(G) \;\le\; \kappa(T)\; c_{\gamma(T)}(G),$$
  where $\kappa(T)$ is the exploration constant of CHECK A's table:
  $\kappa(T) = 2\gamma(T) \cdot \prod_{\text{new-vertex edges } (u,v)}
  (3 - d_u^{\mathrm{proc}})$, the product taken along CHECK A's
  canonical processing order of $E(T) \setminus E(C_T)$, with
  $d_u^{\mathrm{proc}}$ the number of edges of $T$ at the anchored
  endpoint $u$ already processed. The table (grouped: $e(T)$, min
  cycle basis lengths, $w$, $\gamma$, $\kappa$) is asserted in full
  in CHECK A; ranges: $\kappa \in [10, 1280]$.
- **(K3) (aggregate capacity)** For cubic girth-$\ge 5$ $C_8$-free
  $G$, combining census (S4) with (K2):
  $$\operatorname{tr} B^{16} - 32\,c_{16} \;=\; \sum_{T} w(T) N_T(G)
    \;\le\; K_5\, c_5 + K_6\, c_6 + K_7\, c_7,$$
  with $K_\gamma = \sum_{\gamma(T) = \gamma} w(T) \kappa(T)$:
  $$K_5 = 367360, \qquad K_6 = 104448, \qquad K_7 = 53760.$$
  By `cubic_girth5_moment_dictionary`, the right side is a linear
  functional of the spectrum:
  $K_5 \operatorname{tr} A^5/10 + K_6 (\operatorname{tr} A^6 - 87n)/12
  + K_7 (\operatorname{tr} A^7/14 - \operatorname{tr} A^5)$.
- **(K4) (the girth-$9$ $C_{16}$ theorem — unconditional)** Every
  connected cubic graph with girth $\ge 9$ and $n \le 130$ contains
  a $16$-cycle. Equivalently: no cubic Erdős–Gyárfás counterexample
  (a graph whose simple cycle lengths avoid all powers of $2$) has
  girth $\ge 9$ and $n \le 130$. Combined with the ledgered F3
  exhaustion (Markström: no cubic counterexample on $\le 29$
  vertices), any cubic counterexample on $n \le 130$ vertices must
  have girth $\in \{3, 5, 6, 7\}$. (Context only, no proof weight:
  cubic girth-$9$ graphs are known to exist from $58$ vertices, so
  the $n \le 130$ window is inhabited.)

**Proof.**

*(K1).* Finite verification over the $39$-type table rebuilt from
scratch (CHECK A re-runs the census enumeration machinery and takes
the exact minimum simple-cycle length of each type): every minimum
cycle basis starts at $5$, $6$, or $7$, and the minimum simple cycle
length equals the smallest basis length on these types. $\square$

*(K2).* Fix a cubic host $G$ and a type $T$ with designated cycle
$C_T$, $\gamma = \gamma(T)$. For each copy $H \subseteq G$,
$H \cong T$, fix one isomorphism $\varphi_H \colon T \to H$; then
$Z(H) := \varphi_H(C_T)$ is a $\gamma$-cycle of $G$ (an isomorphism
onto a subgraph maps cycles to cycles of the same length). Distinct
copies $H$ give distinct embeddings $\varphi_H$ (their images
differ), so
$$N_T(G) \;\le\; \sum_{Z \;\gamma\text{-cycle of } G}
  \#\{\psi \colon T \hookrightarrow G \text{ embedding},\;
      \psi(C_T) = Z\}.$$
Fix $Z$ and count embeddings $\psi$ with $\psi(C_T) = Z$:

1. $\psi|_{C_T}$ is a graph isomorphism from the $\gamma$-cycle
   $C_T$ onto the $\gamma$-cycle $Z$: at most $2\gamma$ choices
   (dihedral).
2. Process the remaining edges $E(T) \setminus E(C_T)$ in CHECK A's
   fixed order; the order guarantees each processed edge has at
   least one endpoint already placed (T is connected and every
   component of $T - E(C_T)$ meets $C_T$). For an edge $(u, v)$ with
   $u$ placed and $v$ new: $\psi(v)$ must lie in
   $N_G(\psi(u)) \setminus \{\psi(w) : w$ an already-processed
   $T$-neighbor of $u\}$ — the excluded images are pairwise distinct
   ($\psi$ injective) and all lie in $N_G(\psi(u))$ (processed edges
   at $u$ are already $\psi$-mapped to edges of $G$). Since
   $|N_G(\psi(u))| = 3$ (cubic), there are at most
   $3 - d_u^{\mathrm{proc}}$ choices.
3. For an edge whose endpoints are both placed, $\psi$ is already
   determined on it (and it contributes a factor $1$: the edge
   $\psi(u)\psi(v)$ is either in $G$ or the branch dies).

The product of the factors is exactly $\kappa(T)$, independent of
$Z$ and of $G$. Hence $N_T(G) \le c_\gamma(G) \cdot \kappa(T)$.
(Any processing order yields a valid bound; CHECK A's canonical
order — grow closing edges first, lexicographic tie-break after a
deterministic BFS relabeling — is fixed so the table is
reproducible.) $\square$

*(K3).* Census (S4) gives
$\operatorname{tr} B^{16} - 32 c_{16} = \sum_T w(T) N_T(G) \ge 0$
for cubic girth-$\ge 5$ $C_8$-free $G$. Apply (K2) to each term and
group by $\gamma(T)$; CHECK A computes the three aggregates. The
spectral form is the dictionary of `cubic_girth5_moment_dictionary`
(girth $\ge 5$ suffices there). $\square$

*(K4).* Let $G$ be connected cubic, girth $\ge 9$, $n \le 130$, and
suppose $c_{16}(G) = 0$. Girth $\ge 9$ gives girth $\ge 5$ and
$c_8 = 0$, so census (S5) applies: with $\lambda_1 = 3$,
$q_8(3) = 257$, and $\sum_{i \ge 2} q_8(\lambda_i) = -n - 257$,
Cauchy–Schwarz yields (the census display, valid for every connected
$C_{16}$-free instance of any $n$)
$$\operatorname{tr} B^{16} \;=\; \sum_i q_8(\lambda_i)^2 - 511 n
  \;\ge\; 66049 + \frac{(n + 257)^2}{n - 1} - 511\,n \;>\; 0
  \quad (n \le 130,\ \text{CHECK D in exact arithmetic}).$$
On the other hand girth $\ge 9$ gives $c_5 = c_6 = c_7 = 0$, so (K3)
with $c_{16} = 0$ forces $\operatorname{tr} B^{16} \le K_5 \cdot 0 +
K_6 \cdot 0 + K_7 \cdot 0 = 0$. Contradiction. Hence $c_{16} \ge 1$.
A cubic Erdős–Gyárfás counterexample avoids $C_4$, $C_8$, $C_{16}$
(powers of $2$); girth $\ge 9$ and $n \le 130$ would contradict the
above. The positivity window is sharp at this precision: CHECK D
verifies the bound goes negative at $n = 132$. $\square$

**Scope notes (honest, program-facing).**

1. **The squeeze verdict (qid Q0930-083610-2 step 2, numeric test
   BEFORE infeasibility proof — executed, verdict NEGATIVE for the
   girth-5 stratum).** On the $n = 30$ window-census carrier
   (girth $5$, $C_8$-free, $c_5, c_6, c_7 = 5, 12, 8$): actual
   composite mass $= \operatorname{tr} B^{16} - 32 c_{16} = 65952 -
   32 \cdot 750 = 41952$, while the (K3) cap evaluates to
   $3520256$ — an $83.9\times$ overshoot (CHECK C). Since already
   $K_5 \cdot 1 = 367360$ exceeds the (S5) mass requirement
   ($53559$ at $n = 30$, decreasing in $n$), the squeeze as
   aggregated here cannot close ANY stratum with
   $c_5 + c_6 + c_7 \ge 1$. The two-sided squeeze closes exactly
   the $c_5 = c_6 = c_7 = 0$ (girth $\ge 9$) stratum — that is (K4),
   and it is the honest extent of the generic-host capacity
   constants.
2. **Why the constants are loose, and the sharpening path.** $\kappa$
   counts extensions in an ARBITRARY cubic host: every new-vertex
   step contributes its full $3 - d^{\mathrm{proc}}$ even though in
   a girth-$\ge 5$ $C_8$-free host most branches die (closing a
   subdivided cycle at length $3$, $4$, or $8$ is forbidden, and the
   far endpoint must land on a prescribed vertex). Host-aware
   extension counting (the ear-automaton residue tables of
   `mod8_ladder_L3` Section 146 are the same kind of object) or
   per-$Z$ multiplicity accounting (a single $C_5$ cannot
   simultaneously carry its $\kappa$-worth of every type — the
   extensions exhaust the $5$ off-cycle darts) are the two visible
   routes; both are bounded local combinatorics but need their own
   round.
3. (K2) needs only $\Delta \le 3$ in the host and is stated for
   cubic hosts; it is NOT a min-degree-$3$ statement. (K4) is
   cubic-only — consistent with the program's standing scope (the
   verifier class is min-degree-$\ge 3$; the spectral program works
   the cubic stratum first).
4. $\kappa(T)$ is an upper bound on per-cycle multiplicity, not
   exact; tightness was NOT measured per type (CHECK B validates
   the inequality, zero violations across $124$ host–type pairs,
   including hosts with $c_{\gamma} = 0$ forcing $N_T = 0$).

<!-- CHECK
# CHECK A — (K1)+(K2)+(K3) table: rebuild the 39 composite types from the
# census machinery, compute gamma (exact min cycle length) and kappa (the
# canonical exploration product), assert the full table and the aggregates
# K5=367360, K6=104448, K7=53760, and gamma in {5,6,7} with gamma = min of
# the minimum-cycle-basis lengths for every type.
import numpy as np, networkx as nx, itertools
def trB16(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=np.int64)
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return int(np.trace(np.linalg.matrix_power(B, 16)))
def build_theta(a, b, c):
    G = nx.Graph()
    for li, L in enumerate((a, b, c)):
        prev = "u"
        for j in range(1, L): G.add_edge(prev, (li, j)); prev = (li, j)
        G.add_edge(prev, "v")
    return G
def build_dumbbell(l1, l2, p):
    G = nx.Graph()
    for j in range(l1): G.add_edge(("a", j), ("a", (j + 1) % l1))
    for j in range(l2): G.add_edge(("b", j), ("b", (j + 1) % l2))
    prev = ("a", 0)
    for j in range(1, p): G.add_edge(prev, ("p", j)); prev = ("p", j)
    G.add_edge(prev, ("b", 0))
    return G
THETAS = {(1,4,5):32, (1,4,10):32, (1,5,5):64, (1,5,9):32, (1,6,8):32,
          (2,3,3):192, (2,3,4):32, (2,3,8):32, (2,3,9):32, (2,4,5):32,
          (2,4,8):32, (2,5,7):32, (3,3,7):64, (3,4,6):32}
DUMBBELLS = {(5,5,3):64, (5,7,2):64, (5,9,1):64, (6,6,2):64, (7,7,1):64}
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
def build_mg(mg, lengths):
    G = nx.Graph(); nid = [100]; k = 0
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
    paths = paths_of(G); m = len(paths); shapes = []
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
def all_types():
    types = []
    for (a, b, c), w in sorted(THETAS.items()): types.append((build_theta(a, b, c), w))
    for (l1, l2, p), w in sorted(DUMBBELLS.items()): types.append((build_dumbbell(l1, l2, p), w))
    mu3 = []
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
                G = build_mg(mg, L)
                if G.number_of_edges() != sum(L) or not nx.is_connected(G): continue
                if sorted(d for _, d in G.degree()).count(3) != 4: continue
                inv = (G.number_of_edges(),
                       tuple(sorted(len(cb) for cb in nx.minimum_cycle_basis(G))))
                dup = any(hinv == inv and nx.is_isomorphic(G, H) for H, hinv in mu3)
                if not dup: mu3.append((G, inv))
    for G, inv in mu3:
        w = weight(G)
        if w > 0: types.append((G, w))
    return types
def canon(G):
    nodes = sorted(G.nodes(), key=str)
    order, seen = [], set()
    for s in nodes:
        if s in seen: continue
        for v in nx.bfs_tree(G, s):
            if v not in seen: order.append(v); seen.add(v)
    return nx.relabel_nodes(G, {v: i for i, v in enumerate(order)})
def kappa_canon(G):
    G = canon(G)
    best = None
    for c in nx.simple_cycles(G):
        if best is None or (len(c), tuple(sorted(c))) < (len(best), tuple(sorted(best))):
            best = c
    C = best; g = len(C)
    cyc = {frozenset((C[i], C[(i + 1) % g])) for i in range(g)}
    rem = sorted(tuple(sorted(e)) for e in G.edges() if frozenset(e) not in cyc)
    embedded = set(C)
    degp = {v: 0 for v in G}
    for e in cyc:
        for v in e: degp[v] += 1
    prod = 2 * g
    while rem:
        both = [e for e in rem if e[0] in embedded and e[1] in embedded]
        pick = min(both) if both else min(e for e in rem
                                          if e[0] in embedded or e[1] in embedded)
        u, v = pick
        if v in embedded and u not in embedded: u, v = v, u
        if v not in embedded:
            prod *= 3 - degp[u]; embedded.add(v)
        degp[u] += 1; degp[v] += 1
        rem.remove(pick)
    return g, prod
types = all_types()
assert len(types) == 39
rows = []
for G, w in types:
    g, k = kappa_canon(G)
    basis = tuple(sorted(len(cb) for cb in nx.minimum_cycle_basis(G)))
    assert g == min(basis) and g in (5, 6, 7)
    rows.append((G.number_of_edges(), basis, w, g, k))
expected = [(8,(5,5),192,5,10),(9,(5,6),32,5,20),(10,(5,6),32,5,40),
 (11,(5,5,6),352,5,40),(11,(6,6),64,6,48),(11,(6,7),32,6,48),
 (12,(5,5,6),64,5,40),(13,(5,5),64,5,320),(13,(5,5,6),32,5,80),
 (13,(5,5,6),96,5,40),(13,(5,5,7),192,5,40),(13,(5,6,6),96,5,80),
 (13,(5,6,6),96,5,160),(13,(5,6,7),192,5,160),(13,(5,10),32,5,320),
 (13,(6,6,7),96,6,48),(13,(6,10),64,6,192),(13,(7,9),32,7,112),
 (14,(5,5,6),32,5,80),(14,(5,5,6),32,5,80),(14,(5,5,7),64,5,160),
 (14,(5,5,9),96,5,80),(14,(5,6,6),64,5,80),(14,(5,6,7),64,5,160),
 (14,(5,6,7),64,5,160),(14,(5,6,7),96,5,160),(14,(5,7),64,5,640),
 (14,(5,11),32,5,640),(14,(6,6),64,6,384),(14,(6,6,6),64,6,96),
 (14,(6,6,7),64,6,96),(14,(6,7,7),96,6,96),(14,(6,10),32,6,384),
 (14,(7,9),32,7,224),(15,(5,9),64,5,1280),(15,(5,11),32,5,1280),
 (15,(6,10),32,6,768),(15,(7,7),64,7,448),(15,(7,9),32,7,448)]
assert sorted(rows) == sorted(expected), sorted(rows)
K = {5: 0, 6: 0, 7: 0}
for _, _, w, g, k in rows: K[g] += w * k
assert K == {5: 367360, 6: 104448, 7: 53760}, K
print("CHECK A ok: 39 types, gamma in {5,6,7} = min basis; kappa table; K5,K6,K7 = 367360,104448,53760")
CHECK -->

<!-- CHECK
# CHECK B — (K2) empirical validation: N_T <= kappa(T) c_gamma(T) on real
# cubic hosts (Petersen girth 5, Heawood girth 6, dodecahedron girth 5, one
# seeded random connected cubic girth-5 n=16), N_T counted exactly by VF2
# monomorphisms / |Aut|. Includes hosts with c_gamma = 0 (forcing N_T = 0).
# Zero violations across all host-type pairs.
import networkx as nx, numpy as np, itertools, random
from networkx.algorithms import isomorphism as iso
def build_theta(a, b, c):
    G = nx.Graph()
    for li, L in enumerate((a, b, c)):
        prev = "u"
        for j in range(1, L): G.add_edge(prev, (li, j)); prev = (li, j)
        G.add_edge(prev, "v")
    return G
def build_dumbbell(l1, l2, p):
    G = nx.Graph()
    for j in range(l1): G.add_edge(("a", j), ("a", (j + 1) % l1))
    for j in range(l2): G.add_edge(("b", j), ("b", (j + 1) % l2))
    prev = ("a", 0)
    for j in range(1, p): G.add_edge(prev, ("p", j)); prev = ("p", j)
    G.add_edge(prev, ("b", 0))
    return G
def trB16(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=np.int64)
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return int(np.trace(np.linalg.matrix_power(B, 16)))
THETAS = {(1,4,5):32, (1,4,10):32, (1,5,5):64, (1,5,9):32, (1,6,8):32,
          (2,3,3):192, (2,3,4):32, (2,3,8):32, (2,3,9):32, (2,4,5):32,
          (2,4,8):32, (2,5,7):32, (3,3,7):64, (3,4,6):32}
DUMBBELLS = {(5,5,3):64, (5,7,2):64, (5,9,1):64, (6,6,2):64, (7,7,1):64}
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
def build_mg(mg, lengths):
    G = nx.Graph(); nid = [100]; k = 0
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
    paths = paths_of(G); m = len(paths); shapes = []
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
def all_types():
    types = []
    for (a, b, c), w in sorted(THETAS.items()): types.append((build_theta(a, b, c), w))
    for (l1, l2, p), w in sorted(DUMBBELLS.items()): types.append((build_dumbbell(l1, l2, p), w))
    mu3 = []
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
                G = build_mg(mg, L)
                if G.number_of_edges() != sum(L) or not nx.is_connected(G): continue
                if sorted(d for _, d in G.degree()).count(3) != 4: continue
                inv = (G.number_of_edges(),
                       tuple(sorted(len(cb) for cb in nx.minimum_cycle_basis(G))))
                dup = any(hinv == inv and nx.is_isomorphic(G, H) for H, hinv in mu3)
                if not dup: mu3.append((G, inv))
    for G, inv in mu3:
        w = weight(G)
        if w > 0: types.append((G, w))
    return types
def canon(G):
    nodes = sorted(G.nodes(), key=str)
    order, seen = [], set()
    for s in nodes:
        if s in seen: continue
        for v in nx.bfs_tree(G, s):
            if v not in seen: order.append(v); seen.add(v)
    return nx.relabel_nodes(G, {v: i for i, v in enumerate(order)})
def kappa_canon(G):
    G = canon(G)
    best = None
    for c in nx.simple_cycles(G):
        if best is None or (len(c), tuple(sorted(c))) < (len(best), tuple(sorted(best))):
            best = c
    C = best; g = len(C)
    cyc = {frozenset((C[i], C[(i + 1) % g])) for i in range(g)}
    rem = sorted(tuple(sorted(e)) for e in G.edges() if frozenset(e) not in cyc)
    embedded = set(C)
    degp = {v: 0 for v in G}
    for e in cyc:
        for v in e: degp[v] += 1
    prod = 2 * g
    while rem:
        both = [e for e in rem if e[0] in embedded and e[1] in embedded]
        pick = min(both) if both else min(e for e in rem
                                          if e[0] in embedded or e[1] in embedded)
        u, v = pick
        if v in embedded and u not in embedded: u, v = v, u
        if v not in embedded:
            prod *= 3 - degp[u]; embedded.add(v)
        degp[u] += 1; degp[v] += 1
        rem.remove(pick)
    return g, prod
def n_copies(G, T):
    m = sum(1 for _ in iso.GraphMatcher(G, T).subgraph_monomorphisms_iter())
    aut = sum(1 for _ in iso.GraphMatcher(T, T).subgraph_monomorphisms_iter())
    assert m % aut == 0
    return m // aut
types = all_types()
ktab = [(T, w, *kappa_canon(T)) for T, w in types]
hosts = [nx.petersen_graph(), nx.heawood_graph(), nx.dodecahedral_graph()]
rng = random.Random(1004)
while len(hosts) < 4:
    H = nx.random_regular_graph(3, 16, seed=rng.randint(0, 10 ** 6))
    if nx.is_connected(H) and not list(nx.simple_cycles(H, length_bound=4)):
        hosts.append(H)
checked = 0
for H in hosts:
    cc = {5: 0, 6: 0, 7: 0}
    for c in nx.simple_cycles(H, length_bound=7):
        if len(c) in cc: cc[len(c)] += 1
    for T, w, g, k in ktab:
        if T.number_of_nodes() > H.number_of_nodes(): continue
        assert n_copies(H, T) <= k * cc[g], (H.number_of_nodes(), g, k)
        checked += 1
assert checked >= 100
print(f"CHECK B ok: N_T <= kappa c_gamma on 4 cubic hosts, {checked} pairs, 0 violations")
CHECK -->

<!-- CHECK
# CHECK C — (K3) + Scope note 1 on the n=30 window-census carrier (girth 5,
# C8-free): dictionary cross-check of c5,c6,c7 against traces, exact mass
# M = tr B^16 - 32 c16 = 41952, capacity cap = 3520256 (83.9x overshoot),
# and the mass stays BELOW the C16-free S5 requirement only because the
# carrier has c16 = 750 > 0 (no contradiction).
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
cnt = {k: 0 for k in range(3, 17)}
for c in nx.simple_cycles(G, length_bound=16):
    cnt[len(c)] += 1
assert cnt[3] == cnt[4] == cnt[8] == 0
c5, c6, c7, c16 = cnt[5], cnt[6], cnt[7], cnt[16]
assert (c5, c6, c7, c16) == (5, 12, 8, 750)
A = nx.to_numpy_array(G).astype(np.int64)
tA = {k: int(np.trace(np.linalg.matrix_power(A, k))) for k in (5, 6, 7)}
assert c5 == tA[5] // 10 and c6 == (tA[6] - 87 * n) // 12 and c7 == tA[7] // 14 - tA[5]
def trB16(G):
    darts = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    idx = {d: i for i, d in enumerate(darts)}
    B = np.zeros((len(darts), len(darts)), dtype=np.int64)
    for (u, v) in darts:
        for w in G.neighbors(v):
            if w != u: B[idx[(u, v)], idx[(v, w)]] = 1
    return int(np.trace(np.linalg.matrix_power(B, 16)))
b16 = trB16(G)
M = b16 - 32 * c16
cap = 367360 * c5 + 104448 * c6 + 53760 * c7
assert b16 == 65952 and M == 41952 and cap == 3520256 and M <= cap
print(f"CHECK C ok: carrier mass {M} <= capacity cap {cap} ({cap/M:.1f}x overshoot — squeeze verdict)")
CHECK -->

<!-- CHECK
# CHECK D — (K4) positivity window in EXACT arithmetic: the S5 lower bound
# 66049 + (n+257)^2/(n-1) - 511 n is > 0 for all even n with 4 <= n <= 130,
# and < 0 at n = 132 (the window is sharp at this precision). Girth >= 9
# cubic graphs exist from n = 58 (the (3,9)-cages), so (K4) is non-vacuous.
from fractions import Fraction
def lb(n): return 66049 + Fraction((n + 257) ** 2, n - 1) - 511 * n
assert all(lb(n) > 0 for n in range(4, 131, 2))
assert lb(130) > 0 and lb(132) < 0
print("CHECK D ok: S5 lower bound positive for even n <= 130, negative at n = 132")
CHECK -->
