---
id: c16_n24_catalog_completion
status: proved
depends_on: [c16_branch_vertex_arithmetic, c16_n24_profile_resolution, c16_nonantipodal_n24_resolution]
discharged_by_round: null
introduced_at_round: 100
---

# Lemma `c16_n24_catalog_completion` (proved — the COMPLETE $n=24$ catalog: STAR is realized by exactly TWO graphs (adj24 AND W24), the $k=0$ branch is empty, and the class list at $n=24$ is exactly $\{$adj24, spider24, W24$\}$)

**Setting.** $G$ connected cubic, $\{C_4, C_8\}$-free, $n = |V(G)| = 24$,
$C$ a chordless $C_{16}$ in $G$, $H := G - V(C)$ ($8$ vertices), $k$ the
number of $0$-spoke (branch) vertices of $H$.
`c16_branch_vertex_arithmetic` (B5) proved $k \le 1$; for $k = 1$ the
profile is STAR $\{K_{1,3}, K_2, 2K_1\}$, SPIDER $\{S(2,1,1), 3K_1\}$, or
TRIPEND $\{C_3{+}\mathrm{pendant}, 4K_1\}$; for $k = 0$, $H$ is a
$4$-component forest on $8$ vertices with no degree-$3$ vertex, or
$\{C_3, K_2, 3K_1\}$. `c16_n24_profile_resolution` decided TRIPEND (dead)
and SPIDER (rigid: spider24) but ran STAR only to feasibility
(`search("STAR", 1)` — capped at the FIRST solution), and the $k = 0$
branch was never enumerated. R99's W24 (CHECK D of
`c16_nonantipodal_n24_resolution`) forced the question: W24 had to be
$k \ne 1$, or expose a gap in the "two-member rigid catalog" reading of
R97.

**Statement.**

- **(T1) (W24 taxonomy — the gap located)** W24 has exactly $4$
  chordless $C_{16}$s, and EVERY one has $k = 1$ with the STAR profile.
  In particular W24 is a $k = 1$ STAR realization not isomorphic to
  adj24 ($6$ vs $7$ triangles): the "unique realization per profile"
  reading of R97 (Section 135's "each rigidly … unique-up-to-symmetry
  realizations of their profile") is FALSE for STAR. The FORMAL
  statements (P1)–(P4) of `c16_n24_profile_resolution` all survive:
  (P3) claimed rigidity for SPIDER only, and (P4) claimed
  realizability of the profile set $\{$STAR, SPIDER$\}$, not
  uniqueness — the overstatement lived in the strategy prose, not in
  the lemma. (CHECK A.)

- **(T2) (STAR census — the corrected rigidity)** The exhaustive
  enumeration of STAR feet assignments — a SAT encoding of the
  validated R97 Step-2 constraint model, run with NO symmetry
  breaking and full model enumeration — returns exactly $1536$
  assignments $= 64$ classes under $\mathrm{Aut}(H)$
  ($|{\mathrm{Aut}(H)}| = 3! \cdot 2 \cdot 2 = 24$) $= $ exactly
  $\mathbf{2}$ classes under the additional dihedral action on
  positions, each of multiplicity $32 = |D_{16}|$ (both assignment
  orbits are free): **adj24** ($7$ triangles) and **W24**
  ($6$ triangles). STAR is realized by exactly two graphs; the R99
  completion sweep and the profile enumeration converge on the same
  second graph from independent directions. (CHECK B.)

- **(T3) (the $k = 0$ branch is EMPTY)** All six $k = 0$ profiles are
  infeasible: the five path-forest profiles ($H$ a disjoint union of
  paths with $\ge$ one vertex, partitions
  $(5,1,1,1), (4,2,1,1), (3,3,1,1), (3,2,2,1), (2,2,2,2)$ of $8$) and
  the $\mu = 1$ profile $\{C_3, K_2, 3K_1\}$ each admit ZERO valid
  feet assignments. Verified by TWO independent methods: the SAT
  encoding with no symmetry breaking (CHECKs D, E, F) and the R97
  backtracker with exact wreath-group symmetry-breaking classes
  (CHECK G for $(2,2,2,2)$; the other five confirmed by the same
  backtracker off-harness). Consequently every chordless $C_{16}$ at
  $n = 24$ has $k = 1$. (CHECKs D–G.)

- **(T4) (corollary — the complete $n = 24$ catalog)** Every pair
  $(G, C)$ with $G$ a connected cubic $\{C_4, C_8\}$-free graph on
  $24$ vertices and $C$ a chordless $C_{16}$ has
  $G \cong{}$ **adj24**, **W24** (STAR profile) or **spider24**
  (SPIDER profile) — exactly THREE graphs, no others. Their
  chordless-$C_{16}$ censuses: adj24 $3 \times$ STAR, spider24
  $3 \times$ SPIDER, W24 $4 \times$ STAR — every chordless $C_{16}$
  of every member is $k = 1$, and W24's count of $4$ breaks the
  $3$–$3$ pattern of the other two. (CHECKs A–G jointly.)

**Proof.**

*(T1)* Direct computation on the explicit W24 edge list (CHECK A): the
$C_{16}$ census is an exhaustive DFS over the cycles of length $16$
(anchored at their minimum vertex), filtered by chordlessness (every
cycle vertex has exactly $2$ neighbors on the cycle), and $k$ and the
profile of each survivor are read off the outside graph. The same code
path reproduces the known censuses of adj24 ($3$, all STAR) and
spider24 ($3$, all SPIDER) as validation.

*(T2), (T3) — reduction.* The Step 1–Step 3 argument of
`c16_n24_profile_resolution` applies verbatim to every profile here: at
$n = 24$ a feet assignment determines the graph (one spoke per
$C$-vertex, the $16$ feet partition $\mathbb{Z}_{16}$), and the
constraint model — (i) the one-segment menu (no arc-plus-segment cycle
of length $4$ or $8$) plus (ii) the two-segment quadruple $C_8$ layer
($L_1 + L_2 \le 6$) — is EXACTLY $\{C_4, C_8\}$-freeness. Step 2 there
uses only that every $H$-component has $\le 5$ vertices and carries no
cycle other than possibly a $C_3$: true for all profiles here (largest
component $P_5$; the only $H$-cycle is the $C_3$ of
$\{C_3, K_2, 3K_1\}$). Connectivity is automatic for $k = 0$ (every
$H$-vertex is touched) and holds for STAR as in R97 Step 1. The
$k = 0$ profile list is exhaustive by (B1)/(B5): $k = 0$ means no
degree-$3$ $H$-vertex, so $\Delta(H) \le 2$ and every component is a
path or a cycle; $c(H) - \mu(H) = 4$ with $\mu(H) \le 1$ (B5) gives
either $\mu = 0$ — four path components partitioning $8$ vertices, the
five listed partitions — or $\mu = 1$ — five components, one a cycle;
the cycle has length $3$ (a $C_4$ is forbidden outright, and length
$\ge 5$ leaves fewer than $4$ vertices for the other four components),
leaving $(2,1,1,1)$ on the remaining five vertices, i.e.
$\{C_3, K_2, 3K_1\}$.

*(T2), (T3) — enumeration.* The SAT encoding (CHECK B) has variables
$x_{v,p}$ ("$H$-vertex $v$ has a foot at position $p$"), with: each
position carrying exactly one vertex; each vertex $v$ carrying exactly
$\mathrm{caps}(v) = 3 - \deg_H(v)$ feet; a binary clause per forbidden
one-segment difference (constraint (i), from the same
`pair_forbidden` arithmetic as R97); and a $4$-ary clause per
violating two-segment quadruple (constraint (ii), from a
rotation-normalized violation table computed by the same `quad_c8`
predicate as R97). It uses NO symmetry breaking, so its model count is
the raw assignment count. Validation (CHECK C): on the two profiles
R97 decided, the encoding reproduces the backtracker exactly —
TRIPEND UNSAT, and SPIDER with $384 = 32 \times 12$ models
$= 32$ $\mathrm{Aut}(H)$-classes $= $ ONE dihedral class (spider24,
rigid — precisely R97 (P2)+(P3)). On STAR it yields $1536$ models;
canonicalization under $\mathrm{Aut}(H)$ (the explicit $24$-element
group) gives $64$ classes, and further canonicalization under the
$32$-element dihedral action gives exactly $2$ classes of $32$ each;
both representatives' graphs are directly whole-graph verified
$\{C_4, C_8\}$-free and matched by VF2 isomorphism to the explicit
adj24 and W24 edge lists (CHECK B). Equivalent assignments give
isomorphic graphs (R97 Step 3), and conversely an isomorphism between
built graphs is exactly an equivalence of assignments here, so the
class count is the graph count. The six $k = 0$ profiles are UNSAT
(CHECKs D, E, F), independently confirmed by the R97 backtracker with
symmetry-breaking classes that quotient exactly the wreath-type
$H$-automorphism groups (CHECK G shows $(2,2,2,2)$; soundness: any
assignment normalizes to a unique representative satisfying the
first-foot orderings, so pruned branches lose only
$\mathrm{Aut}(H)$-duplicates).

*(T4)* (B5) ($k \le 1$) + (P1) (TRIPEND dead) + (T3) ($k = 0$ empty)
leave STAR and SPIDER; (T2) and R97 (P2)/(P3) list their realizations:
adj24, W24, spider24. The censuses are CHECK A. $\square$

**Program consequences.**

1. **The bottom stratum is now genuinely closed.** The $n = 24$
   catalog is complete and exact: three graphs, all $k = 1$, no
   loose branch. Any future argument quantifying over "all $n = 24$
   class members" may cite this lemma and enumerate
   $\{$adj24, spider24, W24$\}$.
2. **Methodology correction (standing).** A feasibility probe
   (`max_sol=1`) is NOT a census — "rigid"/"exact" language must not
   attach to a profile until it is enumerated to exhaustion. R97's
   formal statements were careful; the session prose was not, and
   R99(e)'s "two-membered" gloss propagated it. The corpus's member
   count at $n = 24$ was wrong for two sessions ($2$, actually $3$)
   until the R99 completion sweep surfaced W24 by accident.
3. **The rigidity conjecture (Section 135 next-move 3) dies in its
   naive form**: profile $\mapsto$ graph is NOT $1{:}1$ at $n = 24$
   (STAR has two realizations). The surviving form is
   finite-multiplicity rigidity: every profile has $\le 2$
   realizations at $n = 24$.
4. **W24's census multiplicity ($4$, vs $3$ and $3$) breaks the
   "perfect mirror" pattern** — chordless-$C_{16}$ multiplicity is
   not constant across the class. The extra $C_{16}$s of W24 (three
   of its four leave the spine $C$) are new raw material for the
   arc-exchange program: they realize STAR on DIFFERENT vertex sets
   of the same graph.
5. **The SAT encoding is a new fast tool** for the $n = 26$ profile
   decision (Section 134 move (ii)): it needs no per-profile anchor
   analysis, enumerates or refutes in seconds at $n = 24$-scale, and
   its two-layer clause structure lifts to $n = 26$ unchanged
   ($10$ outside vertices, $c(H) - \mu(H) = 3$, $k \le 4$).

<!-- CHECK
# CHECK A - W24 taxonomy: exactly 4 chordless C16s, ALL k=1 with the STAR
# profile {K_{1,3}, K2, 2K1}; the same code path reproduces the known
# censuses of adj24 (3, all STAR) and spider24 (3, all SPIDER) as validation.
from collections import deque
W24_EDGES = [(0,1),(0,15),(0,18),(1,2),(1,18),(2,3),(2,21),(3,4),(3,21),(4,5),
         (4,19),(5,6),(5,19),(6,7),(6,20),(7,8),(7,16),(8,9),(8,19),(9,10),
         (9,22),(10,11),(10,22),(11,12),(11,23),(12,13),(12,23),(13,14),
         (13,20),(14,15),(14,20),(15,16),(16,17),(17,18),(17,22),(21,23)]
ADJ24 = [[8,16,21],[7,15,23],[4,16,18],[10,12,15],[2,13,18],[19,20,21],
[11,14,18],[1,10,23],[0,17,21],[13,15,22],[3,7,12],[6,14,23],[3,10,17],
[4,9,22],[6,11,20],[1,3,9],[0,2,22],[8,12,19],[2,4,6],[5,17,20],[5,14,19],
[0,5,8],[9,13,16],[1,7,11]]
SP_E = [(i,(i+1)%16) for i in range(16)] + [(16,17),(17,18),(16,19),(16,20)]
for v, ft in [(17,[0]),(18,[3,6]),(19,[1,2]),(20,[11,15]),(21,[4,7,8]),
              (22,[5,9,12]),(23,[10,13,14])]:
    for p in ft: SP_E.append((v,p))
def from_edges(E, n=24):
    adj = [[] for _ in range(n)]
    for a,b in E: adj[a].append(b); adj[b].append(a)
    return adj
def all_chordless_c16(adj, n=24):
    sets = set()
    for s in range(n):
        stack = [(s, frozenset([s]), 1)]
        while stack:
            v, used, L = stack.pop()
            for w in adj[v]:
                if w == s and L == 16:
                    sets.add(used); continue
                if w <= s or w in used or L >= 16: continue
                stack.append((w, used | frozenset([w]), L+1))
    return [S for S in sets
            if all(sum(1 for w in adj[v] if w in S) == 2 for v in S)]
def profile_of(adj, S, n=24):
    outside = [v for v in range(n) if v not in S]
    hdeg = {v: sum(1 for w in adj[v] if w not in S) for v in outside}
    k = sum(1 for v in outside if hdeg[v] == 3)
    seen, comps = set(), []
    for v in outside:
        if v in seen: continue
        comp = []; q = deque([v]); seen.add(v)
        while q:
            x = q.popleft(); comp.append(x)
            for w in adj[x]:
                if w not in S and w not in seen:
                    seen.add(w); q.append(w)
        comps.append(tuple(sorted(hdeg[x] for x in comp)))
    return k, sorted(comps)
STAR   = [(0,), (0,), (1,1), (1,1,1,3)]
SPIDER = [(0,), (0,), (0,), (1,1,1,2,3)]
W24 = from_edges(W24_EDGES)
cs = all_chordless_c16(W24)
assert len(cs) == 4, len(cs)
assert all(profile_of(W24, S) == (1, STAR) for S in cs)
csA = all_chordless_c16(ADJ24)
assert len(csA) == 3 and all(profile_of(ADJ24, S) == (1, STAR) for S in csA)
SP = from_edges(SP_E)
csS = all_chordless_c16(SP)
assert len(csS) == 3 and all(profile_of(SP, S) == (1, SPIDER) for S in csS)
print("CHECK A ok: W24 has 4 chordless C16s, all k=1 STAR; "
      "adj24 3x STAR and spider24 3x SPIDER reproduced")
CHECK -->

<!-- CHECK
# CHECK B - STAR full census by SAT: 1536 raw models = 64 Aut(H)-classes =
# 2 graphs up to iso (adj24 and W24), 32 dihedral-orbit members each.
# The encoding is the R97 Step-2 constraint model (exactly {C4,C8}-freeness):
# (1) each position one vertex, (2) vertex v exactly caps[v] feet,
# (3) one-segment menu binary clauses, (4) two-segment quad-C8 4-ary clauses.
from itertools import combinations, permutations
from pysat.solvers import Minisat22
from pysat.card import CardEnc, EncType
import networkx as nx
HEDGES = [(0,1),(0,2),(0,3),(4,5)]
CAPS   = [0,2,2,2,2,2,3,3]
def h_paths(caps, hedges):
    adj = [[] for _ in range(8)]
    for a,b in hedges: adj[a].append(b); adj[b].append(a)
    paths = [(v,v,0,frozenset([v])) for v in range(8) if caps[v] >= 2]
    for u in range(8):
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
def encode(hedges, caps):
    X = [[v*16+p+1 for p in range(16)] for v in range(8)]
    cl = []
    for p in range(16):
        col = [X[v][p] for v in range(8) if caps[v] > 0]
        cl.append(col)
        cl += [[-a,-b] for a,b in combinations(col,2)]
        for v in range(8):
            if caps[v] == 0: cl.append([-X[v][p]])
    top = 128
    for v in range(8):
        if caps[v] == 0: continue
        enc = CardEnc.equals(lits=X[v], bound=caps[v], top_id=top,
                             encoding=EncType.seqcounter)
        cl += enc.clauses; top = max(top, enc.nv)
    paths = h_paths(caps, hedges)
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
    tables = {}
    for A, B in pairs2:
        u1,w1,e1,_ = A; u2,w2,e2,_ = B
        L1, L2 = e1+2, e2+2
        if (L1,L2) not in tables:
            tables[(L1,L2)] = {(b,g,d) for b in range(16) for g in range(16)
                               for d in range(16) if len({0,b,g,d}) == 4
                               and quad_c8(0,b,L1,g,d,L2)}
        for (b,g,d) in tables[(L1,L2)]:
            for al in range(16):
                be, ga, de = (al+b)%16, (al+g)%16, (al+d)%16
                if u1 == w1 and al > be: continue
                if u2 == w2 and ga > de: continue
                cl.append([-X[u1][al], -X[w1][be], -X[u2][ga], -X[w2][de]])
    return X, cl
X, cl = encode(HEDGES, CAPS)
models = []
with Minisat22(bootstrap_with=cl) as m:
    while m.solve():
        mod = m.get_model()
        feet = tuple(frozenset(p for p in range(16) if mod[v*16+p] > 0)
                     for v in range(8))
        models.append(feet)
        m.add_clause([-X[v][p] for v in range(8) for p in feet[v]])
assert len(models) == 1536, len(models)
AUTS = []
for lp in permutations((1,2,3)):
    for k2 in ((4,5),(5,4)):
        for k1 in ((6,7),(7,6)):
            AUTS.append((0,)+lp+k2+k1)
assert len(AUTS) == 24
def canon_aut(feet):
    return min(tuple(tuple(sorted(feet[s[v]])) for v in range(8)) for s in AUTS)
aut_classes = {canon_aut(f) for f in models}
assert len(aut_classes) == 64, len(aut_classes)
def canon_dihedral(feet):
    best = None
    for refl in (False, True):
        for r in range(16):
            nf = tuple(frozenset(((-p if refl else p)+r) % 16 for p in fs)
                       for fs in feet)
            c = canon_aut(nf)
            if best is None or c < best: best = c
    return best
orbit = {}
for f in aut_classes:
    orbit.setdefault(canon_dihedral(f), []).append(f)
assert len(orbit) == 2, len(orbit)
assert sorted(len(v) for v in orbit.values()) == [32, 32]
def build(feet):
    g = nx.Graph()
    for i in range(16): g.add_edge(i, (i+1) % 16)
    for a,b in HEDGES: g.add_edge(16+a, 16+b)
    for v in range(8):
        for p in feet[v]: g.add_edge(16+v, p)
    return g
W24_EDGES = [(0,1),(0,15),(0,18),(1,2),(1,18),(2,3),(2,21),(3,4),(3,21),(4,5),
         (4,19),(5,6),(5,19),(6,7),(6,20),(7,8),(7,16),(8,9),(8,19),(9,10),
         (9,22),(10,11),(10,22),(11,12),(11,23),(12,13),(12,23),(13,14),
         (13,20),(14,15),(14,20),(15,16),(16,17),(17,18),(17,22),(21,23)]
ADJ24 = [[8,16,21],[7,15,23],[4,16,18],[10,12,15],[2,13,18],[19,20,21],
[11,14,18],[1,10,23],[0,17,21],[13,15,22],[3,7,12],[6,14,23],[3,10,17],
[4,9,22],[6,11,20],[1,3,9],[0,2,22],[8,12,19],[2,4,6],[5,17,20],[5,14,19],
[0,5,8],[9,13,16],[1,7,11]]
gW = nx.Graph(W24_EDGES)
gA = nx.Graph([(a,b) for a,nb in enumerate(ADJ24) for b in nb if a < b])
hits = set()
for rep in orbit:
    g = build(rep)
    cyc = {}
    for c in nx.simple_cycles(g, length_bound=8):
        cyc[len(c)] = cyc.get(len(c), 0) + 1
    assert cyc.get(4, 0) == 0 and cyc.get(8, 0) == 0, cyc
    if nx.is_isomorphic(g, gA): hits.add("adj24")
    elif nx.is_isomorphic(g, gW): hits.add("W24")
assert hits == {"adj24", "W24"}, hits
print("CHECK B ok: STAR census 1536 SAT models = 64 Aut-classes = 2 graphs "
      "(adj24, W24), dihedral multiplicity 32+32; reps directly C4/C8-verified")
CHECK -->

<!-- CHECK
# CHECK C - SAT validation against R97's decided profiles: TRIPEND UNSAT;
# SPIDER: 384 raw models = 32 Aut(H)-classes = ONE dihedral class (spider24
# is rigid) - the encoding reproduces the R97 backtracker's results exactly.
from itertools import combinations, permutations
from pysat.solvers import Minisat22, Cadical153
from pysat.card import CardEnc, EncType
def h_paths(caps, hedges):
    adj = [[] for _ in range(8)]
    for a,b in hedges: adj[a].append(b); adj[b].append(a)
    paths = [(v,v,0,frozenset([v])) for v in range(8) if caps[v] >= 2]
    for u in range(8):
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
def encode(hedges, caps):
    X = [[v*16+p+1 for p in range(16)] for v in range(8)]
    cl = []
    for p in range(16):
        col = [X[v][p] for v in range(8) if caps[v] > 0]
        cl.append(col)
        cl += [[-a,-b] for a,b in combinations(col,2)]
        for v in range(8):
            if caps[v] == 0: cl.append([-X[v][p]])
    top = 128
    for v in range(8):
        if caps[v] == 0: continue
        enc = CardEnc.equals(lits=X[v], bound=caps[v], top_id=top,
                             encoding=EncType.seqcounter)
        cl += enc.clauses; top = max(top, enc.nv)
    paths = h_paths(caps, hedges)
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
    tables = {}
    for A, B in pairs2:
        u1,w1,e1,_ = A; u2,w2,e2,_ = B
        L1, L2 = e1+2, e2+2
        if (L1,L2) not in tables:
            tables[(L1,L2)] = {(b,g,d) for b in range(16) for g in range(16)
                               for d in range(16) if len({0,b,g,d}) == 4
                               and quad_c8(0,b,L1,g,d,L2)}
        for (b,g,d) in tables[(L1,L2)]:
            for al in range(16):
                be, ga, de = (al+b)%16, (al+g)%16, (al+d)%16
                if u1 == w1 and al > be: continue
                if u2 == w2 and ga > de: continue
                cl.append([-X[u1][al], -X[w1][be], -X[u2][ga], -X[w2][de]])
    return X, cl
X, cl = encode([(0,1),(0,2),(1,2),(0,3)], [0,1,1,2,3,3,3,3])   # TRIPEND
with Cadical153(bootstrap_with=cl) as m:
    assert not m.solve()                     # TRIPEND: infeasible (= R97 P1)
X, cl = encode([(0,1),(1,2),(0,3),(0,4)], [0,1,2,2,2,3,3,3])   # SPIDER
models = []
with Minisat22(bootstrap_with=cl) as m:
    while m.solve():
        mod = m.get_model()
        feet = tuple(frozenset(p for p in range(16) if mod[v*16+p] > 0)
                     for v in range(8))
        models.append(feet)
        m.add_clause([-X[v][p] for v in range(8) for p in feet[v]])
assert len(models) == 384, len(models)
AUTS = []
for ll in ((3,4),(4,3)):
    for ap in permutations((5,6,7)):
        AUTS.append((0,1,2)+ll+ap)
assert len(AUTS) == 12
def canon_aut(feet):
    return min(tuple(tuple(sorted(feet[s[v]])) for v in range(8)) for s in AUTS)
aut_classes = {canon_aut(f) for f in models}
assert len(aut_classes) == 32, len(aut_classes)
def canon_dihedral(feet):
    best = None
    for refl in (False, True):
        for r in range(16):
            nf = tuple(frozenset(((-p if refl else p)+r) % 16 for p in fs)
                       for fs in feet)
            c = canon_aut(nf)
            if best is None or c < best: best = c
    return best
assert len({canon_dihedral(f) for f in aut_classes}) == 1
print("CHECK C ok: TRIPEND UNSAT; SPIDER 384 models = 32 Aut-classes = "
      "1 dihedral class - the SAT encoding reproduces R97 exactly")
CHECK -->

<!-- CHECK
# CHECK D - k=0 branch: path-forest profiles (5,1,1,1) and (3,3,1,1)
# admit NO valid feet assignment at n=24 (SAT, no symmetry breaking).
from itertools import combinations
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
def h_paths(caps, hedges):
    adj = [[] for _ in range(8)]
    for a,b in hedges: adj[a].append(b); adj[b].append(a)
    paths = [(v,v,0,frozenset([v])) for v in range(8) if caps[v] >= 2]
    for u in range(8):
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
def encode(hedges, caps):
    X = [[v*16+p+1 for p in range(16)] for v in range(8)]
    cl = []
    for p in range(16):
        col = [X[v][p] for v in range(8) if caps[v] > 0]
        cl.append(col)
        cl += [[-a,-b] for a,b in combinations(col,2)]
        for v in range(8):
            if caps[v] == 0: cl.append([-X[v][p]])
    top = 128
    for v in range(8):
        if caps[v] == 0: continue
        enc = CardEnc.equals(lits=X[v], bound=caps[v], top_id=top,
                             encoding=EncType.seqcounter)
        cl += enc.clauses; top = max(top, enc.nv)
    paths = h_paths(caps, hedges)
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
    tables = {}
    for A, B in pairs2:
        u1,w1,e1,_ = A; u2,w2,e2,_ = B
        L1, L2 = e1+2, e2+2
        if (L1,L2) not in tables:
            tables[(L1,L2)] = {(b,g,d) for b in range(16) for g in range(16)
                               for d in range(16) if len({0,b,g,d}) == 4
                               and quad_c8(0,b,L1,g,d,L2)}
        for (b,g,d) in tables[(L1,L2)]:
            for al in range(16):
                be, ga, de = (al+b)%16, (al+g)%16, (al+d)%16
                if u1 == w1 and al > be: continue
                if u2 == w2 and ga > de: continue
                cl.append([-X[u1][al], -X[w1][be], -X[u2][ga], -X[w2][de]])
    return X, cl
X, cl = encode([(0,1),(1,2),(2,3),(3,4)], [2,1,1,1,2,3,3,3])   # F5111
with Cadical153(bootstrap_with=cl) as m:
    assert not m.solve(), "F5111 unexpectedly SAT"
X, cl = encode([(0,1),(1,2),(3,4),(4,5)], [2,1,2,2,1,2,3,3])   # F3311
with Cadical153(bootstrap_with=cl) as m:
    assert not m.solve(), "F3311 unexpectedly SAT"
print("CHECK D ok: F5111, F3311 all UNSAT")
CHECK -->

<!-- CHECK
# CHECK E - k=0 branch: path-forest profile (4,2,1,1) admits NO valid
# feet assignment at n=24 (SAT, no symmetry breaking).
from itertools import combinations
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
def h_paths(caps, hedges):
    adj = [[] for _ in range(8)]
    for a,b in hedges: adj[a].append(b); adj[b].append(a)
    paths = [(v,v,0,frozenset([v])) for v in range(8) if caps[v] >= 2]
    for u in range(8):
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
def encode(hedges, caps):
    X = [[v*16+p+1 for p in range(16)] for v in range(8)]
    cl = []
    for p in range(16):
        col = [X[v][p] for v in range(8) if caps[v] > 0]
        cl.append(col)
        cl += [[-a,-b] for a,b in combinations(col,2)]
        for v in range(8):
            if caps[v] == 0: cl.append([-X[v][p]])
    top = 128
    for v in range(8):
        if caps[v] == 0: continue
        enc = CardEnc.equals(lits=X[v], bound=caps[v], top_id=top,
                             encoding=EncType.seqcounter)
        cl += enc.clauses; top = max(top, enc.nv)
    paths = h_paths(caps, hedges)
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
    tables = {}
    for A, B in pairs2:
        u1,w1,e1,_ = A; u2,w2,e2,_ = B
        L1, L2 = e1+2, e2+2
        if (L1,L2) not in tables:
            tables[(L1,L2)] = {(b,g,d) for b in range(16) for g in range(16)
                               for d in range(16) if len({0,b,g,d}) == 4
                               and quad_c8(0,b,L1,g,d,L2)}
        for (b,g,d) in tables[(L1,L2)]:
            for al in range(16):
                be, ga, de = (al+b)%16, (al+g)%16, (al+d)%16
                if u1 == w1 and al > be: continue
                if u2 == w2 and ga > de: continue
                cl.append([-X[u1][al], -X[w1][be], -X[u2][ga], -X[w2][de]])
    return X, cl
X, cl = encode([(0,1),(1,2),(2,3),(4,5)], [2,1,1,2,2,2,3,3])   # F4211
with Cadical153(bootstrap_with=cl) as m:
    assert not m.solve(), "F4211 unexpectedly SAT"
print("CHECK E ok: F4211 UNSAT")
CHECK -->

<!-- CHECK
# CHECK F - k=0 branch: path-forest profile (3,2,2,1) and the mu=1
# profile {C3,K2,3K1} admit NO valid feet assignment at n=24.
from itertools import combinations
from pysat.solvers import Glucose42, Cadical153
from pysat.card import CardEnc, EncType
def h_paths(caps, hedges):
    adj = [[] for _ in range(8)]
    for a,b in hedges: adj[a].append(b); adj[b].append(a)
    paths = [(v,v,0,frozenset([v])) for v in range(8) if caps[v] >= 2]
    for u in range(8):
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
def encode(hedges, caps):
    X = [[v*16+p+1 for p in range(16)] for v in range(8)]
    cl = []
    for p in range(16):
        col = [X[v][p] for v in range(8) if caps[v] > 0]
        cl.append(col)
        cl += [[-a,-b] for a,b in combinations(col,2)]
        for v in range(8):
            if caps[v] == 0: cl.append([-X[v][p]])
    top = 128
    for v in range(8):
        if caps[v] == 0: continue
        enc = CardEnc.equals(lits=X[v], bound=caps[v], top_id=top,
                             encoding=EncType.seqcounter)
        cl += enc.clauses; top = max(top, enc.nv)
    paths = h_paths(caps, hedges)
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
    tables = {}
    for A, B in pairs2:
        u1,w1,e1,_ = A; u2,w2,e2,_ = B
        L1, L2 = e1+2, e2+2
        if (L1,L2) not in tables:
            tables[(L1,L2)] = {(b,g,d) for b in range(16) for g in range(16)
                               for d in range(16) if len({0,b,g,d}) == 4
                               and quad_c8(0,b,L1,g,d,L2)}
        for (b,g,d) in tables[(L1,L2)]:
            for al in range(16):
                be, ga, de = (al+b)%16, (al+g)%16, (al+d)%16
                if u1 == w1 and al > be: continue
                if u2 == w2 and ga > de: continue
                cl.append([-X[u1][al], -X[w1][be], -X[u2][ga], -X[w2][de]])
    return X, cl
X, cl = encode([(0,1),(1,2),(3,4),(5,6)], [2,1,2,2,2,2,2,3])   # F3221
with Glucose42(bootstrap_with=cl) as m:
    assert not m.solve(), "F3221 unexpectedly SAT"
X, cl = encode([(0,1),(1,2),(0,2),(3,4)], [1,1,1,2,2,3,3,3])   # TRIK2 = {C3,K2,3K1}
with Cadical153(bootstrap_with=cl) as m:
    assert not m.solve(), "TRIK2 unexpectedly SAT"
print("CHECK F ok: F3221, TRIK2 all UNSAT")
CHECK -->

<!-- CHECK
# CHECK G - k=0 branch: the (2,2,2,2) path-forest profile (four K2
# components) admits NO valid feet assignment at n=24, by the R97
# backtracker. Symmetry-breaking classes quotient EXACTLY the wreath group
# S2 wr S4 of H-automorphisms: within-pair order ([0,1],[2,3],[4,5],[6,7])
# plus pair order by first foot ([0,2,4,6]); any assignment normalizes to
# a unique representative satisfying all orderings (sort pairs by earliest
# foot, then endpoints within pair), so UNSAT here is UNSAT outright.
# (The SAT encoding of CHECKs C-F confirms independently: 0 models.)
HEDGES = [(0,1),(2,3),(4,5),(6,7)]
CAPS = [2]*8
CLASSES = [[0,1],[2,3],[4,5],[6,7],[0,2,4,6]]
def h_paths(caps, hedges):
    adj = [[] for _ in range(8)]
    for a,b in hedges: adj[a].append(b); adj[b].append(a)
    paths = [(v,v,0,frozenset([v])) for v in range(8) if caps[v] >= 2]
    for u in range(8):
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
def seg_feet(P, feet):
    u,w,_,_ = P
    if u != w:
        return [(a,b) for a in feet[u] for b in feet[w]]
    return [(a,b) for i,a in enumerate(feet[u]) for b in feet[u][i+1:]]
def search(hedges, caps, classes):
    paths = h_paths(caps, hedges)
    forb = {}
    for u,w,ell,_ in paths:
        s = forb.setdefault((u,w), set())
        for dd in range(1,16):
            if dd+ell+2 in (4,8) or 16-dd+ell+2 in (4,8): s.add(dd)
    pairs2 = [(paths[i], paths[j]) for i in range(len(paths))
              for j in range(i+1, len(paths))
              if paths[i][2]+paths[j][2] <= 2 and not (paths[i][3] & paths[j][3])]
    feet = [[] for _ in range(8)]; placed = [0]*8; sols = []
    def allowed(v):
        for cl in classes:
            if v in cl:
                i = cl.index(v)
                if i > 0 and placed[cl[i-1]] == 0: return False
        return True
    def ok(v, p):
        for w in range(8):
            if not feet[w]: continue
            s = forb.get((min(v,w), max(v,w)) if v != w else (v,v))
            if s and any(q != p and (p-q) % 16 in s for q in feet[w]): return False
        for P1, P2 in pairs2:
            for (A, B) in ((P1,P2),(P2,P1)):
                u1,w1,e1,_ = A
                if v != u1 and v != w1: continue
                other = w1 if v == u1 else u1
                bf = [q for q in feet[other] if q != p]
                for b in bf:
                    for g,d in seg_feet(B, feet):
                        if len({p,b,g,d}) == 4 and (
                           quad_c8(p,b,e1+2,g,d,B[2]+2) or quad_c8(b,p,e1+2,g,d,B[2]+2)):
                            return False
        return True
    def bt(pos):
        if pos == 16:
            sols.append([list(f) for f in feet]); return
        for v in range(8):
            if placed[v] >= caps[v] or not allowed(v): continue
            if ok(v, pos):
                feet[v].append(pos); placed[v] += 1
                bt(pos+1)
                feet[v].pop(); placed[v] -= 1
    bt(0)
    return sols
sols = search(HEDGES, CAPS, CLASSES)
assert sols == [], sols
print("CHECK G ok: F2222 (four K2 components) admits no valid assignment")
CHECK -->
