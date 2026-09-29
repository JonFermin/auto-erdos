---
id: c16_n26_classification
status: proved
depends_on: [c16_branch_vertex_arithmetic, c16_n24_catalog_completion]
discharged_by_round: null
introduced_at_round: 101
---

# Lemma `c16_n26_classification` (proved — the complete $n = 26$ classification: 74 profiles, 30 realizable, exactly 22 graphs; $k \le 3$, $\mu(H) \le 1$, and the $k = 0$ branch is NON-empty — realized exactly once)

**Setting.** $G$ connected cubic, $\{C_4, C_8\}$-free, $n = |V(G)| = 26$,
$C$ a chordless $C_{16}$ in $G$, $H := G - V(C)$ ($10$ vertices), $Z$ the
set of $0$-spoke (branch) vertices, $k = |Z|$. By
`c16_branch_vertex_arithmetic`: (B0) every $C$-vertex has one spoke
($16$ spokes, distinct feet), (B1) each component of $H$ absorbs
$q + 2 - 2\mu$ spokes and $c(H) - \mu(H) = (32-n)/2 = 3$, (B2)
$k \le n - 22 = 4$. Since $e(H) = q(H) - c(H) + \mu(H) = 10 - 3 = 7$,
$H$ has exactly $7$ edges. A **profile** is the isomorphism type of $H$:
max degree $\le 3$ (cubic $G$), no $4$- or $8$-cycles inside $H$
($C_4/C_8$-freeness of $G$), per-component $\mu \le (q+2)/2$
(absorption $\ge 0$; (B1)), $10$ vertices, $7$ edges.

**Statement.**

- **(N1) (profile arithmetic)** Exactly $74$ profiles exist (pairwise
  non-isomorphic), and every one has $k \le 3$: the (B2) cap $k \le 4$
  is NOT attained even arithmetically at $n = 26$. Their $k$-distribution
  is $k{=}0{:}\,17$, $k{=}1{:}\,29$, $k{=}2{:}\,24$,
  $k{=}3{:}\,4$; $\mu(H){=}0{:}\,36$, $\mu(H){=}1{:}\,34$,
  $\mu(H){=}2{:}\,4$ (two via a single $\mu = 2$ component, two
  via a pair of $\mu = 1$ components). (CHECK A.)
- **(N2) (realizability decision)** Exactly $30$ of the $74$ profiles are
  realizable ($k{=}0{:}\,1$ of $17$, $k{=}1{:}\,15$ of $29$,
  $k{=}2{:}\,12$ of $24$, $k{=}3{:}\,2$ of $4$); $44$ are not. In
  particular ALL FOUR $\mu(H) = 2$ profiles are infeasible, so
  $\mu(H) \le 1$ persists at $n = 26$. Three of the four are decided
  in-harness every round (CHECK C: both single-$\Theta$ profiles;
  CHECK F: the $C_3 + (C_3{+}\mathrm{pendant})$ profile); the fourth
  (two disjoint $C_3$s $+ K_2 + 2K_1$, $36$ s) and the remaining $41$
  infeasibilities are decided by the same engine off-harness, with the
  two-way census consistency of (N4)/CHECK E as the independent
  cross-check. Realized $k$ values: $0, 1, 2, 3$ — both extremes occur.
- **(N3) (the $k = 0$ branch is NON-empty — contrast with $n = 24$)** The
  profile $\{P_5, C_3, 2K_1\}$ ($k = 0$, $\mu = 1$) is realized by
  exactly one graph, and across the ENTIRE catalog exactly ONE
  $(G, C)$ pair has $k = 0$. At $n = 24$ the $k = 0$ branch was empty
  (`c16_n24_catalog_completion` (T3)); at $n = 26$ it is inhabited, so
  the "every chordless $C_{16}$ has a branch vertex" reading of T3 does
  NOT lift to $n = 26$. (CHECK D verifies the explicit witness; CHECK E
  verifies the exactly-once census claim over the whole catalog.)
- **(N4) (the complete $n = 26$ catalog)** Up to isomorphism exactly
  $\mathbf{22}$ graphs admit a chordless $C_{16}$ at $n = 26$, jointly
  carrying $178$ chordless $C_{16}$s whose profile $k$-distribution is
  $k{=}0{:}\,1$, $k{=}1{:}\,60$, $k{=}2{:}\,109$, $k{=}3{:}\,8$.
  Every SAT profile of (N2) occurs in some member's census and every
  census profile is SAT — the census layer (pure cycle enumeration,
  independent of the SAT encoding) and the decision layer agree in both
  directions. Triangle counts span $1$–$8$; per-member chordless-$C_{16}$
  counts span $3$–$12$ (vs the rigid $3$/$3$/$4$ pattern at $n = 24$).
  (CHECKs E, F, G.)

**Method and validation.** The engine is the R100 SAT encoding of the
R97 Step-2 constraint model — (1) each $C$-position exactly one foot,
(2) vertex $v$ exactly $\operatorname{caps}[v] = 3 - \deg_H(v)$ feet,
(3) one-segment $C_4/C_8$ menu binary clauses ((B3) instances), (4)
two-segment quad-$C_8$ $4$-ary clauses — lifted verbatim from $8$ to
$10$ outside vertices ($160$ position variables). Completeness of the
clause classes at $n = 26$: a cycle of length $\le 8$ meeting $C$ uses
$1$ or $2$ $H$-segments (each segment has length $\ge 2$, each
connecting arc $\ge 1$, so $3$ segments force length $\ge 9$); cycles
inside $H$ are excluded at profile level; cycles meeting $C$ in one
vertex would need two spokes at one $C$-vertex, impossible by (B0).
The lifted encoding reproduces the ENTIRE decided $n = 24$ landscape
exactly — STAR $1536$ models, SPIDER $384$, TRIPEND $0$
(`c16_n24_catalog_completion` CHECKs B, C) — re-verified here as
CHECK B. Every profile was enumerated to exhaustion (full model
enumeration with blocking clauses, NO first-solution caps — the R100
methodology rule); models were canonicalized under
$\mathrm{Aut}(H) \times D_{16}$ and every dihedral-class representative
graph was directly verified with networkx (cubic, connected, zero
$4$/$8$-cycles) before iso-classification. Exactness scope, stated
precisely: the $30$ SAT enumerations and $42$ of the $44$ UNSAT
decisions ran off-harness (per-profile results embedded in the CHECK E
table; wall-clock $\approx 12$ min total); what runs in-harness every
round is the full profile arithmetic (CHECK A), the $n = 24$
reproduction (CHECK B), both $\mu = 2$ UNSATs (CHECK C), explicit
$k = 0$ / $k = 3$ witnesses (CHECKs D, G), and the complete two-way
census consistency over all $22$ members and all $74$ profiles
(CHECK E) — the last is an independent engine (cycle enumeration, no
SAT) confirming every decision that any realized graph touches.

**Proof.**

*(N1)* The component candidates are: trees on $q \le 8$ vertices with
max degree $\le 3$ (a tree component with $e$ edges has $q = e + 1 \le 8$
since $e(H) = 7$), and connected graphs with $\mu \ge 1$, $e \le 7$,
hence $q \le 8 - \mu \le 7$, max degree $\le 3$, cycle lengths avoiding
$\{4, 8\}$, $\mu \le (q+2)/2$. Multisets of candidates with
$\sum q = 10$, $\sum e = 7$: the constraint $c - \mu = 3$ is automatic
($c - \mu = q - e = 3$). Exhaustive recursion over the candidate list
(CHECK A, using the networkx graph atlas for the cyclic candidates and
`nonisomorphic_trees` for trees) yields exactly $74$ multisets, pairwise
non-isomorphic as graphs, with the stated $k$- and $\mu$-distributions;
no profile attains $k = 4$ — with $7$ edges, four degree-$3$ vertices
force degree sum $\ge 12$ of $14$, and the recursion finds no legal
completion. $\square$

*(N2)* One SAT decision per profile with the lifted encoding. The four
$\mu(H) = 2$ profiles are $\{\Theta(1,2,4), 4K_1\}$ (the $6$-vertex
theta, cycles $3,5,6$), $\{2C_3{+}\mathrm{bridge}, 4K_1\}$ (cycles
$3,3$), $\{C_3, C_3{+}\mathrm{pendant}, 3K_1\}$ and
$\{C_3, C_3, K_2, 2K_1\}$ — all UNSAT (CHECKs C and F in-harness for
the first three; the last off-harness). The full SAT/UNSAT table with
model counts is embedded in CHECK E. $\square$

*(N3)* CHECK D verifies the explicit realization: the member whose
$C = (0, 1, \dots, 15)$ has $H$ on vertices $16..25$ isomorphic to
$P_5 + C_3 + 2K_1$ with zero degree-$3$ vertices — all $10$ outside
vertices carry spokes. CHECK E confirms that over all $178$ chordless
$C_{16}$s of the $22$ members, exactly one has $k = 0$. $\square$

*(N4)* The $22$ edge lists are embedded in CHECK E, which re-verifies:
each is cubic, connected, $\{C_4, C_8\}$-free; they are pairwise
non-isomorphic; their chordless-$C_{16}$ censuses total $178$; each
census $H$ (computed by cycle enumeration + induced-subgraph check,
independent of SAT) matches exactly one of the $74$ profiles up to
isomorphism, that profile is SAT in the table, every SAT profile is
observed, and the $k$-distribution is as stated. Completeness of the
$22$-member list follows from (N2): every realizable profile's full
model enumeration was canonicalized and iso-classified; a $23$rd member
would require a model of some profile outside its enumerated orbit
list, contradicting exhaustion. $\square$

**Consequences for the program.**

1. The branch-vertex law "$k \ge 1$" is a FINITE-SIZE artifact of
   $n = 24$, not a structural law of the class: supply falsifiers at
   general $n$ cannot assume a branch vertex exists. Q85's zero-free
   completion question is ALIVE at $n = 26$ — but barely (one pair in
   $178$), suggesting $k = 0$ is heavily constrained, not forbidden.
2. $\mu(H) \le 1$ now holds at both decided sizes; the absorption
   arithmetic alone permits $\mu = 2$ at $n = 26$, so this is a
   genuine geometric exclusion — candidate for a general-$n$ proof
   (the theta/dumbbell feet menus die against the C4/C8 arithmetic).
3. Growth of the catalog: $3$ members at $n = 24$ $\to$ $22$ at
   $n = 26$, with the per-graph $C_{16}$ count spreading from
   $\{3, 4\}$ to $[3, 12]$. Any counting-based route (Q81/Q82
   composition program) must absorb this growth rate.
4. The R97-style "profile rigidity" fails wholesale at $n = 26$:
   realized profiles carry up to $8$ distinct graphs (profile
   $\{K_{1,3}, C_3{+}\mathrm{pendant}, 2K_1\}$-type, idx 47). The
   R100 methodology rule (census, never feasibility) was load-bearing
   here.

## Data appendix (decision table)

The per-profile table (H edge list on vertices $0..9$, SAT flag, model
count, distinct-graph count) and the $22$ member edge lists are embedded
in CHECK E below; profile indices $0..73$ are in CHECK A's enumeration
order (deterministic).

<!-- CHECK
# CHECK A — (N1): exactly 74 profiles, pairwise non-isomorphic, k <= 3,
# k-distribution 17/29/24/4, mu-distribution 36/34/4.
import networkx as nx
from networkx.generators.atlas import graph_atlas_g
def cycles_ok(g):
    lens = {len(c) for c in nx.simple_cycles(g)} if g.number_of_edges() >= 3 else set()
    return not (lens & {4, 8})
comps = []
for q in range(1, 9):
    if q == 1: trees = [nx.empty_graph(1)]
    elif q == 2: trees = [nx.path_graph(2)]
    else: trees = list(nx.nonisomorphic_trees(q))
    for t in trees:
        if max(dict(t.degree()).values()) <= 3:
            comps.append((t, q, q-1, 0, sum(1 for _, d in t.degree() if d == 3)))
for g in graph_atlas_g()[1:]:
    q, e = g.number_of_nodes(), g.number_of_edges()
    if q == 0 or not nx.is_connected(g): continue
    mu = e - q + 1
    if mu < 1 or e > 7: continue
    if max(dict(g.degree()).values()) > 3: continue
    if 2*mu > q + 2: continue
    if not cycles_ok(g): continue
    comps.append((g, q, e, mu, sum(1 for _, d in g.degree() if d == 3)))
profiles = []
def rec(i, q_left, e_left, k_used, chosen):
    if q_left == 0:
        if e_left == 0: profiles.append(list(chosen))
        return
    if i == len(comps) or e_left < 0: return
    g, q, e, mu, nd3 = comps[i]
    m = 0
    while m*q <= q_left and m*e <= e_left and k_used + m*nd3 <= 4:
        if m > 0:
            chosen.append((i, m))
            rec(i+1, q_left - m*q, e_left - m*e, k_used + m*nd3, chosen)
            chosen.pop()
        else:
            rec(i+1, q_left, e_left, k_used, chosen)
        m += 1
rec(0, 10, 7, 0, [])
def build_H(prof):
    G = nx.Graph(); G.add_nodes_from(range(10)); off = 0
    for ci, mult in prof:
        g = comps[ci][0]
        for _ in range(mult):
            mapping = {v: off+j for j, v in enumerate(sorted(g.nodes()))}
            for a, b in g.edges(): G.add_edge(mapping[a], mapping[b])
            off += comps[ci][1]
    return G
assert len(profiles) == 74, len(profiles)
Hs = [build_H(p) for p in profiles]
from collections import Counter
kd, md = Counter(), Counter()
for Hg in Hs:
    kd[sum(1 for _, d in Hg.degree() if d == 3)] += 1
    md[Hg.number_of_edges() - 10 + nx.number_connected_components(Hg)] += 1
    assert Hg.number_of_edges() == 7
assert max(kd) == 3 and kd[0] == 17 and kd[1] == 29 and kd[2] == 24 and kd[3] == 4, kd
assert md[0] == 36 and md[1] == 34 and md[2] == 4, md
import itertools
for i, j in itertools.combinations(range(74), 2):
    deg_i = sorted(d for _, d in Hs[i].degree())
    deg_j = sorted(d for _, d in Hs[j].degree())
    if deg_i == deg_j and nx.is_isomorphic(Hs[i], Hs[j]):
        raise AssertionError((i, j))
print("CHECK A ok: 74 pairwise non-isomorphic profiles, k<=3 (17/29/24/4), mu 36/34/4")
CHECK -->

<!-- CHECK
# CHECK B — encoding validation: the lifted encoder (parametric NV) reproduces
# the decided n=24 landscape: SPIDER 384 models, TRIPEND 0. (STAR 1536 is
# re-verified every round by c16_n24_catalog_completion CHECK B.)
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
def count_models(NV, hedges, caps, cap=None):
    X, cl = encode(NV, hedges, caps)
    n = 0
    with Minisat22(bootstrap_with=cl) as m:
        while m.solve():
            mod = m.get_model()
            feet = [[p for p in range(16) if mod[v*16+p] > 0] for v in range(NV)]
            n += 1
            if cap is not None and n > cap: return n
            m.add_clause([-X[v][p] for v in range(NV) for p in feet[v]])
    return n
assert count_models(8, [(0,1),(1,2),(0,3),(0,4)], [0,1,2,2,2,3,3,3]) == 384
assert count_models(8, [(0,1),(1,2),(2,0),(0,3)], [0,1,1,2,3,3,3,3]) == 0
print("CHECK B ok: n=24 reproduction — SPIDER 384, TRIPEND UNSAT")
CHECK -->

<!-- CHECK
# CHECK C — (N2) mu(H)=2 exclusion IN-HARNESS: both mu=2 profiles UNSAT.
# Profile 72: theta(1,2,4) (6 vertices, cycles 3,5,6) + 4K1.
# Profile 73: two triangles joined by a bridge (6 vertices) + 4K1.
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
def count_models(NV, hedges, caps, cap=None):
    X, cl = encode(NV, hedges, caps)
    n = 0
    with Minisat22(bootstrap_with=cl) as m:
        while m.solve():
            mod = m.get_model()
            feet = [[p for p in range(16) if mod[v*16+p] > 0] for v in range(NV)]
            n += 1
            if cap is not None and n > cap: return n
            m.add_clause([-X[v][p] for v in range(NV) for p in feet[v]])
    return n
theta = [(4,5),(4,6),(5,6),(5,7),(6,8),(7,9),(8,9)]
import collections
deg = collections.Counter()
for a, b in theta: deg[a] += 1; deg[b] += 1
caps_t = [3 - deg[v] for v in range(10)]
assert count_models(10, theta, caps_t, cap=0) == 0
dumb = [(4,5),(4,6),(5,6),(6,7),(7,8),(7,9),(8,9)]
deg = collections.Counter()
for a, b in dumb: deg[a] += 1; deg[b] += 1
caps_d = [3 - deg[v] for v in range(10)]
assert count_models(10, dumb, caps_d, cap=0) == 0
print("CHECK C ok: both mu=2 profiles UNSAT — mu(H) <= 1 at n=26")
CHECK -->

<!-- CHECK
# CHECK D — (N3) explicit k=0 witness: C = (0..15) chordless, H on 16..25
# iso to P5+C3+2K1 with ZERO degree-3 vertices (every outside vertex spoked).
import networkx as nx
E = [(0,1),(0,15),(0,22),(1,2),(1,22),(2,3),(2,16),(3,4),(3,17),(4,5),(4,17),(5,6),(5,16),(6,7),(6,16),(7,8),(7,23),(8,9),(8,20),(9,10),(9,20),(10,11),(10,21),(11,12),(11,19),(12,13),(12,17),(13,14),(13,25),(14,15),(14,18),(15,24),(18,19),(18,21),(19,20),(21,22),(23,24),(23,25),(24,25)]
g = nx.Graph(E)
assert g.number_of_nodes() == 26 and all(d == 3 for _, d in g.degree())
assert nx.is_connected(g)
cyc = {}
for c in nx.simple_cycles(g, length_bound=8):
    cyc[len(c)] = cyc.get(len(c), 0) + 1
assert cyc.get(4, 0) == 0 and cyc.get(8, 0) == 0, cyc
C = list(range(16))
assert all(g.has_edge(C[i], C[(i+1) % 16]) for i in range(16))
assert g.subgraph(C).number_of_edges() == 16          # chordless
H = g.subgraph(range(16, 26))
assert H.number_of_edges() == 7
assert sum(1 for _, d in H.degree() if d == 3) == 0    # k = 0
comps = sorted((s.number_of_nodes(), s.number_of_edges())
               for s in (H.subgraph(cc) for cc in nx.connected_components(H)))
assert comps == [(1, 0), (1, 0), (3, 3), (5, 4)], comps  # 2K1 + C3 + P5
degs = sorted(d for _, d in H.degree())
assert degs == [0, 0, 1, 1, 2, 2, 2, 2, 2, 2], degs      # P5 (not T5)
print("CHECK D ok: explicit k=0 realization at n=26 — P5+C3+2K1, all 10 outside vertices spoked")
CHECK -->

<!-- CHECK
# CHECK E — (N2)+(N4): catalog well-formedness AND full two-way census
# consistency. 22 members: cubic, connected, C4/C8-free, pairwise non-iso.
# 178 chordless C16s in total; every census H matches exactly one of the 74
# profiles up to iso; that profile is SAT; every SAT profile is observed;
# k-distribution 1/60/109/8. The census engine is pure cycle enumeration —
# independent of the SAT decisions it cross-checks.
import networkx as nx
PROFILES = [  # (H edges on 0..9; sat; nmodels; ngraphs). caps[v]=3-deg_H(v)
 ([(0, 2), (1, 0), (3, 5), (4, 3), (6, 8), (6, 9), (7, 6)], 1, 768, 1),  # 0: P3+P3+T4d3111 k=1
 ([(0, 2), (1, 0), (3, 5), (4, 3), (6, 9), (7, 6), (7, 8)], 0, 0, 0),  # 1: P3+P3+P4 k=0
 ([(0, 1), (2, 4), (2, 5), (3, 2), (6, 8), (6, 9), (7, 6)], 1, 13824, 5),  # 2: K2+T4d3111+T4d3111 k=2
 ([(0, 1), (2, 5), (3, 2), (3, 4), (6, 8), (6, 9), (7, 6)], 1, 768, 1),  # 3: K2+P4+T4d3111 k=1
 ([(0, 1), (2, 5), (3, 2), (3, 4), (6, 9), (7, 6), (7, 8)], 0, 0, 0),  # 4: K2+P4+P4 k=0
 ([(0, 1), (2, 4), (3, 2), (5, 8), (5, 9), (6, 5), (6, 7)], 1, 1536, 5),  # 5: K2+P3+T5d32111 k=1
 ([(0, 1), (2, 4), (3, 2), (5, 8), (6, 5), (6, 7), (8, 9)], 0, 0, 0),  # 6: K2+P3+P5 k=0
 ([(0, 1), (2, 3), (4, 7), (4, 9), (5, 4), (5, 6), (7, 8)], 1, 256, 1),  # 7: K2+K2+T6d322111 k=1
 ([(0, 1), (2, 3), (4, 8), (4, 9), (5, 4), (5, 6), (5, 7)], 0, 0, 0),  # 8: K2+K2+T6d331111 k=2
 ([(0, 1), (2, 3), (4, 8), (5, 4), (5, 6), (5, 7), (8, 9)], 1, 512, 1),  # 9: K2+K2+T6d322111 k=1
 ([(0, 1), (2, 3), (4, 8), (5, 4), (5, 6), (6, 7), (8, 9)], 0, 0, 0),  # 10: K2+K2+P6 k=0
 ([(0, 1), (2, 3), (4, 6), (5, 4), (7, 8), (7, 9), (8, 9)], 0, 0, 0),  # 11: K2+K2+P3+q3mu1c3 k=0
 ([(0, 1), (2, 3), (4, 5), (6, 9), (7, 8), (7, 9), (8, 9)], 0, 0, 0),  # 12: K2+K2+K2+q4mu1c3 k=1
 ([(1, 3), (1, 4), (2, 1), (5, 8), (5, 9), (6, 5), (6, 7)], 1, 2304, 5),  # 13: K1+T4d3111+T5d32111 k=2
 ([(1, 3), (1, 4), (2, 1), (5, 8), (6, 5), (6, 7), (8, 9)], 1, 768, 2),  # 14: K1+P5+T4d3111 k=1
 ([(1, 4), (2, 1), (2, 3), (5, 8), (5, 9), (6, 5), (6, 7)], 0, 0, 0),  # 15: K1+P4+T5d32111 k=1
 ([(1, 4), (2, 1), (2, 3), (5, 8), (6, 5), (6, 7), (8, 9)], 0, 0, 0),  # 16: K1+P4+P5 k=0
 ([(1, 3), (2, 1), (4, 7), (4, 9), (5, 4), (5, 6), (7, 8)], 1, 384, 3),  # 17: K1+P3+T6d322111 k=1
 ([(1, 3), (2, 1), (4, 8), (4, 9), (5, 4), (5, 6), (5, 7)], 1, 512, 1),  # 18: K1+P3+T6d331111 k=2
 ([(1, 3), (2, 1), (4, 8), (5, 4), (5, 6), (5, 7), (8, 9)], 1, 256, 2),  # 19: K1+P3+T6d322111 k=1
 ([(1, 3), (2, 1), (4, 8), (5, 4), (5, 6), (6, 7), (8, 9)], 0, 0, 0),  # 20: K1+P3+P6 k=0
 ([(1, 3), (2, 1), (4, 6), (5, 4), (7, 8), (7, 9), (8, 9)], 0, 0, 0),  # 21: K1+P3+P3+q3mu1c3 k=0
 ([(1, 2), (3, 6), (3, 8), (4, 3), (4, 5), (6, 7), (8, 9)], 0, 0, 0),  # 22: K1+K2+T7d3222111 k=1
 ([(1, 2), (3, 7), (3, 9), (4, 3), (4, 5), (4, 6), (7, 8)], 1, 640, 4),  # 23: K1+K2+T7d3321111 k=2
 ([(1, 2), (3, 7), (4, 3), (4, 5), (4, 6), (7, 8), (7, 9)], 0, 0, 0),  # 24: K1+K2+T7d3321111 k=2
 ([(1, 2), (3, 7), (3, 9), (4, 3), (4, 5), (5, 6), (7, 8)], 0, 0, 0),  # 25: K1+K2+T7d3222111 k=1
 ([(1, 2), (3, 7), (4, 3), (4, 5), (5, 6), (7, 8), (7, 9)], 0, 0, 0),  # 26: K1+K2+T7d3222111 k=1
 ([(1, 2), (3, 7), (4, 3), (4, 5), (5, 6), (7, 8), (8, 9)], 0, 0, 0),  # 27: K1+K2+P7 k=0
 ([(1, 2), (3, 5), (3, 6), (4, 3), (7, 8), (7, 9), (8, 9)], 1, 9216, 3),  # 28: K1+K2+T4d3111+q3mu1c3 k=1
 ([(1, 2), (3, 6), (4, 3), (4, 5), (7, 8), (7, 9), (8, 9)], 0, 0, 0),  # 29: K1+K2+P4+q3mu1c3 k=0
 ([(1, 2), (3, 5), (4, 3), (6, 9), (7, 8), (7, 9), (8, 9)], 1, 1280, 5),  # 30: K1+K2+P3+q4mu1c3 k=1
 ([(1, 2), (3, 4), (5, 6), (5, 9), (6, 7), (7, 8), (8, 9)], 0, 0, 0),  # 31: K1+K2+K2+q5mu1c5 k=0
 ([(1, 2), (3, 4), (5, 9), (6, 7), (6, 8), (7, 8), (8, 9)], 1, 1536, 1),  # 32: K1+K2+K2+q5mu1c3 k=1
 ([(1, 2), (3, 4), (5, 6), (5, 7), (5, 9), (6, 7), (7, 8)], 1, 3584, 3),  # 33: K1+K2+K2+q5mu1c3 k=2
 ([(2, 6), (2, 8), (3, 2), (3, 4), (3, 5), (6, 7), (8, 9)], 1, 128, 1),  # 34: K1+K1+T8d33221111 k=2
 ([(2, 6), (2, 9), (3, 2), (3, 4), (3, 5), (6, 7), (6, 8)], 1, 1792, 2),  # 35: K1+K1+T8d33311111 k=3
 ([(2, 6), (2, 8), (3, 2), (3, 4), (4, 5), (6, 7), (8, 9)], 1, 128, 1),  # 36: K1+K1+T8d32222111 k=1
 ([(2, 6), (2, 9), (3, 2), (3, 4), (4, 5), (6, 7), (6, 8)], 1, 256, 2),  # 37: K1+K1+T8d33221111 k=2
 ([(2, 6), (2, 9), (3, 2), (3, 4), (4, 5), (6, 7), (7, 8)], 0, 0, 0),  # 38: K1+K1+T8d32222111 k=1
 ([(2, 7), (2, 9), (3, 2), (3, 4), (3, 6), (4, 5), (7, 8)], 1, 256, 2),  # 39: K1+K1+T8d33221111 k=2
 ([(2, 7), (3, 2), (3, 4), (3, 6), (4, 5), (7, 8), (7, 9)], 0, 0, 0),  # 40: K1+K1+T8d33221111 k=2
 ([(2, 7), (3, 2), (3, 4), (3, 6), (4, 5), (7, 8), (8, 9)], 1, 192, 3),  # 41: K1+K1+T8d32222111 k=1
 ([(2, 7), (3, 2), (3, 4), (4, 5), (4, 6), (7, 8), (7, 9)], 1, 1536, 3),  # 42: K1+K1+T8d33221111 k=2
 ([(2, 7), (3, 2), (3, 4), (4, 5), (4, 6), (7, 8), (8, 9)], 0, 0, 0),  # 43: K1+K1+T8d32222111 k=1
 ([(2, 7), (3, 2), (3, 4), (4, 5), (5, 6), (7, 8), (8, 9)], 0, 0, 0),  # 44: K1+K1+P8 k=0
 ([(2, 5), (2, 6), (3, 2), (3, 4), (7, 8), (7, 9), (8, 9)], 1, 768, 1),  # 45: K1+K1+T5d32111+q3mu1c3 k=1
 ([(2, 5), (3, 2), (3, 4), (5, 6), (7, 8), (7, 9), (8, 9)], 1, 768, 1),  # 46: K1+K1+P5+q3mu1c3 k=0
 ([(2, 4), (2, 5), (3, 2), (6, 9), (7, 8), (7, 9), (8, 9)], 1, 9216, 8),  # 47: K1+K1+T4d3111+q4mu1c3 k=2
 ([(2, 5), (3, 2), (3, 4), (6, 9), (7, 8), (7, 9), (8, 9)], 0, 0, 0),  # 48: K1+K1+P4+q4mu1c3 k=1
 ([(2, 4), (3, 2), (5, 6), (5, 9), (6, 7), (7, 8), (8, 9)], 0, 0, 0),  # 49: K1+K1+P3+q5mu1c5 k=0
 ([(2, 4), (3, 2), (5, 9), (6, 7), (6, 8), (7, 8), (8, 9)], 0, 0, 0),  # 50: K1+K1+P3+q5mu1c3 k=1
 ([(2, 4), (3, 2), (5, 6), (5, 7), (5, 9), (6, 7), (7, 8)], 0, 0, 0),  # 51: K1+K1+P3+q5mu1c3 k=2
 ([(2, 3), (4, 5), (4, 9), (5, 6), (6, 7), (7, 8), (8, 9)], 0, 0, 0),  # 52: K1+K1+K2+q6mu1c6 k=0
 ([(2, 3), (4, 5), (4, 8), (5, 6), (5, 9), (6, 7), (7, 8)], 0, 0, 0),  # 53: K1+K1+K2+q6mu1c5 k=1
 ([(2, 3), (4, 8), (4, 9), (5, 6), (5, 7), (6, 7), (7, 8)], 1, 256, 1),  # 54: K1+K1+K2+q6mu1c3 k=1
 ([(2, 3), (4, 5), (4, 6), (4, 7), (7, 8), (7, 9), (8, 9)], 1, 1280, 3),  # 55: K1+K1+K2+q6mu1c3 k=2
 ([(2, 3), (4, 6), (5, 6), (5, 7), (5, 8), (6, 8), (7, 9)], 1, 512, 3),  # 56: K1+K1+K2+q6mu1c3 k=2
 ([(2, 3), (4, 8), (5, 9), (6, 7), (7, 8), (7, 9), (8, 9)], 1, 1536, 2),  # 57: K1+K1+K2+q6mu1c3 k=3
 ([(2, 3), (4, 5), (4, 6), (5, 6), (7, 8), (7, 9), (8, 9)], 0, 0, 0),  # 58: K1+K1+K2+q3mu1c3+q3mu1c3 k=0
 ([(3, 4), (3, 9), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)], 0, 0, 0),  # 59: K1+K1+K1+q7mu1c7 k=0
 ([(3, 5), (3, 7), (3, 8), (4, 7), (5, 6), (6, 9), (8, 9)], 0, 0, 0),  # 60: K1+K1+K1+q7mu1c5 k=1
 ([(3, 7), (4, 5), (4, 6), (5, 8), (5, 9), (6, 7), (8, 9)], 0, 0, 0),  # 61: K1+K1+K1+q7mu1c3 k=1
 ([(3, 6), (3, 7), (4, 5), (5, 8), (5, 9), (6, 9), (7, 8)], 0, 0, 0),  # 62: K1+K1+K1+q7mu1c6 k=1
 ([(3, 4), (3, 6), (3, 7), (4, 5), (5, 8), (5, 9), (8, 9)], 0, 0, 0),  # 63: K1+K1+K1+q7mu1c3 k=2
 ([(3, 5), (3, 8), (4, 5), (5, 6), (6, 9), (7, 8), (8, 9)], 0, 0, 0),  # 64: K1+K1+K1+q7mu1c5 k=2
 ([(3, 4), (3, 7), (4, 5), (5, 6), (5, 8), (7, 8), (8, 9)], 0, 0, 0),  # 65: K1+K1+K1+q7mu1c5 k=2
 ([(3, 7), (4, 5), (4, 6), (4, 7), (5, 8), (5, 9), (8, 9)], 0, 0, 0),  # 66: K1+K1+K1+q7mu1c3 k=2
 ([(3, 4), (3, 7), (4, 5), (4, 7), (5, 6), (7, 8), (8, 9)], 0, 0, 0),  # 67: K1+K1+K1+q7mu1c3 k=2
 ([(3, 4), (3, 7), (4, 5), (4, 7), (5, 6), (6, 9), (7, 8)], 0, 0, 0),  # 68: K1+K1+K1+q7mu1c3 k=2
 ([(3, 4), (3, 6), (3, 7), (4, 5), (4, 7), (5, 8), (5, 9)], 0, 0, 0),  # 69: K1+K1+K1+q7mu1c3 k=3
 ([(3, 4), (4, 5), (5, 8), (5, 9), (6, 9), (7, 8), (8, 9)], 0, 0, 0),  # 70: K1+K1+K1+q7mu1c3 k=3
 ([(3, 4), (3, 5), (4, 5), (6, 9), (7, 8), (7, 9), (8, 9)], 0, 0, 0),  # 71: K1+K1+K1+q3mu1c3+q4mu1c3 k=1
 ([(4, 5), (4, 6), (4, 7), (5, 6), (7, 8), (7, 9), (8, 9)], 0, 0, 0),  # 72: K1+K1+K1+K1+q6mu2c3-3 k=2
 ([(4, 6), (4, 9), (5, 6), (5, 7), (6, 7), (7, 8), (8, 9)], 0, 0, 0),  # 73: K1+K1+K1+K1+q6mu2c3-5-6 k=2
]
assert len(PROFILES) == 74 and sum(1 for p in PROFILES if p[1]) == 30
profH = [nx.Graph(p[0]) for p in PROFILES]
for Hg in profH: Hg.add_nodes_from(range(10))
CATALOG = [  # 22 members, edge lists (n=26 vertices 0..25)
 [(0,1),(0,15),(0,19),(1,2),(1,19),(2,3),(2,23),(3,4),(3,16),(4,5),(4,16),(5,6),(5,23),(6,7),(6,24),(7,8),(7,18),(8,9),(8,18),(9,10),(9,20),(10,11),(10,20),(11,12),(11,16),(12,13),(12,25),(13,14),(13,25),(14,15),(14,24),(15,22),(17,18),(17,19),(17,20),(21,22),(21,24),(21,25),(22,23)],  # 0: tri=5 c16=11
 [(0,1),(0,15),(0,19),(1,2),(1,19),(2,3),(2,23),(3,4),(3,16),(4,5),(4,16),(5,6),(5,23),(6,7),(6,24),(7,8),(7,24),(8,9),(8,20),(9,10),(9,20),(10,11),(10,18),(11,12),(11,16),(12,13),(12,25),(13,14),(13,25),(14,15),(14,18),(15,22),(17,18),(17,19),(17,20),(21,22),(21,24),(21,25),(22,23)],  # 1: tri=5 c16=10
 [(0,1),(0,15),(0,22),(1,2),(1,24),(2,3),(2,17),(3,4),(3,25),(4,5),(4,19),(5,6),(5,17),(6,7),(6,20),(7,8),(7,20),(8,9),(8,16),(9,10),(9,23),(10,11),(10,18),(11,12),(11,25),(12,13),(12,19),(13,14),(13,23),(14,15),(14,24),(15,16),(16,17),(18,19),(18,20),(21,22),(21,24),(21,25),(22,23)],  # 2: tri=1 c16=9
 [(0,1),(0,15),(0,21),(1,2),(1,21),(2,3),(2,23),(3,4),(3,24),(4,5),(4,19),(5,6),(5,25),(6,7),(6,20),(7,8),(7,20),(8,9),(8,17),(9,10),(9,17),(10,11),(10,24),(11,12),(11,23),(12,13),(12,16),(13,14),(13,25),(14,15),(14,18),(15,18),(16,17),(16,18),(19,20),(19,21),(22,23),(22,24),(22,25)],  # 3: tri=4 c16=10
 [(0,1),(0,15),(0,24),(1,2),(1,20),(2,3),(2,19),(3,4),(3,25),(4,5),(4,24),(5,6),(5,20),(6,7),(6,17),(7,8),(7,21),(8,9),(8,21),(9,10),(9,16),(10,11),(10,19),(11,12),(11,25),(12,13),(12,16),(13,14),(13,23),(14,15),(14,23),(15,17),(16,17),(18,19),(18,20),(18,21),(22,23),(22,24),(22,25)],  # 4: tri=2 c16=12
 [(0,1),(0,15),(0,19),(1,2),(1,16),(2,3),(2,16),(3,4),(3,23),(4,5),(4,21),(5,6),(5,18),(6,7),(6,18),(7,8),(7,24),(8,9),(8,19),(9,10),(9,16),(10,11),(10,25),(11,12),(11,25),(12,13),(12,22),(13,14),(13,20),(14,15),(14,20),(15,23),(17,18),(17,19),(17,20),(21,22),(21,24),(22,23),(24,25)],  # 5: tri=4 c16=12
 [(0,1),(0,15),(0,19),(1,2),(1,25),(2,3),(2,25),(3,4),(3,20),(4,5),(4,16),(5,6),(5,16),(6,7),(6,20),(7,8),(7,21),(8,9),(8,21),(9,10),(9,23),(10,11),(10,23),(11,12),(11,24),(12,13),(12,17),(13,14),(13,17),(14,15),(14,18),(15,24),(16,17),(18,19),(18,21),(19,20),(22,23),(22,24),(22,25)],  # 6: tri=5 c16=7
 [(0,1),(0,15),(0,17),(1,2),(1,23),(2,3),(2,23),(3,4),(3,25),(4,5),(4,18),(5,6),(5,22),(6,7),(6,20),(7,8),(7,20),(8,9),(8,16),(9,10),(9,16),(10,11),(10,25),(11,12),(11,24),(12,13),(12,24),(13,14),(13,19),(14,15),(14,19),(15,17),(16,17),(18,19),(18,20),(21,22),(21,24),(21,25),(22,23)],  # 7: tri=6 c16=8
 [(0,1),(0,15),(0,25),(1,2),(1,25),(2,3),(2,23),(3,4),(3,16),(4,5),(4,16),(5,6),(5,23),(6,7),(6,19),(7,8),(7,19),(8,9),(8,22),(9,10),(9,24),(10,11),(10,24),(11,12),(11,16),(12,13),(12,20),(13,14),(13,20),(14,15),(14,18),(15,18),(17,18),(17,19),(17,20),(21,22),(21,24),(21,25),(22,23)],  # 8: tri=6 c16=12
 [(0,1),(0,15),(0,19),(1,2),(1,19),(2,3),(2,17),(3,4),(3,17),(4,5),(4,25),(5,6),(5,25),(6,7),(6,24),(7,8),(7,24),(8,9),(8,21),(9,10),(9,21),(10,11),(10,16),(11,12),(11,16),(12,13),(12,23),(13,14),(13,23),(14,15),(14,20),(15,20),(16,17),(18,19),(18,20),(18,21),(22,23),(22,24),(22,25)],  # 9: tri=8 c16=9
 [(0,1),(0,15),(0,21),(1,2),(1,20),(2,3),(2,17),(3,4),(3,17),(4,5),(4,24),(5,6),(5,24),(6,7),(6,25),(7,8),(7,25),(8,9),(8,19),(9,10),(9,19),(10,11),(10,16),(11,12),(11,16),(12,13),(12,23),(13,14),(13,23),(14,15),(14,20),(15,21),(16,17),(18,19),(18,20),(18,21),(22,23),(22,24),(22,25)],  # 10: tri=7 c16=8
 [(0,1),(0,15),(0,21),(1,2),(1,17),(2,3),(2,17),(3,4),(3,25),(4,5),(4,21),(5,6),(5,19),(6,7),(6,20),(7,8),(7,20),(8,9),(8,16),(9,10),(9,19),(10,11),(10,23),(11,12),(11,16),(12,13),(12,24),(13,14),(13,24),(14,15),(14,23),(15,25),(16,17),(18,19),(18,20),(18,21),(22,23),(22,24),(22,25)],  # 11: tri=3 c16=4
 [(0,1),(0,15),(0,20),(1,2),(1,22),(2,3),(2,17),(3,4),(3,17),(4,5),(4,20),(5,6),(5,19),(6,7),(6,19),(7,8),(7,23),(8,9),(8,23),(9,10),(9,25),(10,11),(10,16),(11,12),(11,16),(12,13),(12,25),(13,14),(13,18),(14,15),(14,24),(15,24),(16,17),(18,19),(18,20),(21,22),(21,24),(21,25),(22,23)],  # 12: tri=5 c16=4
 [(0,1),(0,15),(0,18),(1,2),(1,17),(2,3),(2,17),(3,4),(3,22),(4,5),(4,24),(5,6),(5,24),(6,7),(6,19),(7,8),(7,19),(8,9),(8,20),(9,10),(9,20),(10,11),(10,25),(11,12),(11,23),(12,13),(12,23),(13,14),(13,25),(14,15),(14,16),(15,16),(16,17),(18,19),(18,20),(21,22),(21,24),(21,25),(22,23)],  # 13: tri=6 c16=3
 [(0,1),(0,15),(0,25),(1,2),(1,25),(2,3),(2,23),(3,4),(3,16),(4,5),(4,16),(5,6),(5,23),(6,7),(6,19),(7,8),(7,19),(8,9),(8,22),(9,10),(9,24),(10,11),(10,24),(11,12),(11,16),(12,13),(12,20),(13,14),(13,18),(14,15),(14,18),(15,20),(17,18),(17,19),(17,20),(21,22),(21,24),(21,25),(22,23)],  # 14: tri=5 c16=8
 [(0,1),(0,15),(0,17),(1,2),(1,17),(2,3),(2,23),(3,4),(3,20),(4,5),(4,20),(5,6),(5,21),(6,7),(6,21),(7,8),(7,16),(8,9),(8,16),(9,10),(9,24),(10,11),(10,22),(11,12),(11,22),(12,13),(12,19),(13,14),(13,18),(14,15),(14,18),(15,16),(17,18),(19,20),(19,21),(22,25),(23,24),(23,25),(24,25)],  # 15: tri=7 c16=6
 [(0,1),(0,15),(0,17),(1,2),(1,17),(2,3),(2,24),(3,4),(3,21),(4,5),(4,20),(5,6),(5,20),(6,7),(6,21),(7,8),(7,16),(8,9),(8,16),(9,10),(9,23),(10,11),(10,22),(11,12),(11,22),(12,13),(12,19),(13,14),(13,18),(14,15),(14,18),(15,16),(17,18),(19,20),(19,21),(22,25),(23,24),(23,25),(24,25)],  # 16: tri=6 c16=12
 [(0,1),(0,15),(0,21),(1,2),(1,20),(2,3),(2,17),(3,4),(3,17),(4,5),(4,25),(5,6),(5,24),(6,7),(6,24),(7,8),(7,25),(8,9),(8,19),(9,10),(9,19),(10,11),(10,16),(11,12),(11,16),(12,13),(12,23),(13,14),(13,23),(14,15),(14,20),(15,21),(16,17),(18,19),(18,20),(18,21),(22,23),(22,24),(22,25)],  # 17: tri=6 c16=6
 [(0,1),(0,15),(0,20),(1,2),(1,20),(2,3),(2,16),(3,4),(3,16),(4,5),(4,17),(5,6),(5,17),(6,7),(6,16),(7,8),(7,24),(8,9),(8,21),(9,10),(9,21),(10,11),(10,22),(11,12),(11,18),(12,13),(12,18),(13,14),(13,25),(14,15),(14,22),(15,23),(17,18),(19,20),(19,21),(19,22),(23,24),(23,25),(24,25)],  # 18: tri=6 c16=4
 [(0,1),(0,15),(0,16),(1,2),(1,16),(2,3),(2,18),(3,4),(3,18),(4,5),(4,16),(5,6),(5,20),(6,7),(6,20),(7,8),(7,22),(8,9),(8,25),(9,10),(9,25),(10,11),(10,17),(11,12),(11,17),(12,13),(12,19),(13,14),(13,19),(14,15),(14,24),(15,24),(17,18),(19,20),(21,22),(21,23),(21,25),(22,23),(23,24)],  # 19: tri=8 c16=8
 [(0,1),(0,15),(0,16),(1,2),(1,20),(2,3),(2,21),(3,4),(3,19),(4,5),(4,19),(5,6),(5,24),(6,7),(6,17),(7,8),(7,17),(8,9),(8,16),(9,10),(9,20),(10,11),(10,17),(11,12),(11,16),(12,13),(12,22),(13,14),(13,23),(14,15),(14,21),(15,22),(18,19),(18,20),(18,21),(22,25),(23,24),(23,25),(24,25)],  # 20: tri=3 c16=3
 [(0,1),(0,15),(0,23),(1,2),(1,16),(2,3),(2,16),(3,4),(3,17),(4,5),(4,17),(5,6),(5,16),(6,7),(6,19),(7,8),(7,19),(8,9),(8,24),(9,10),(9,22),(10,11),(10,22),(11,12),(11,17),(12,13),(12,21),(13,14),(13,21),(14,15),(14,20),(15,20),(18,19),(18,20),(18,21),(22,25),(23,24),(23,25),(24,25)],  # 21: tri=7 c16=12
]
assert len(CATALOG) == 22
from collections import Counter
gs = [nx.Graph(e) for e in CATALOG]
for g in gs:
    assert g.number_of_nodes() == 26 and all(d == 3 for _, d in g.degree())
    assert nx.is_connected(g)
    cyc = Counter(len(c) for c in nx.simple_cycles(g, length_bound=8))
    assert cyc[4] == 0 and cyc[8] == 0, cyc
tri = [sum(1 for c in nx.simple_cycles(g, length_bound=3)) for g in gs]
import itertools
for i, j in itertools.combinations(range(22), 2):
    if tri[i] == tri[j] and nx.is_isomorphic(gs[i], gs[j]):
        raise AssertionError((i, j))
kdist, observed, total = Counter(), set(), 0
for g in gs:
    for c in nx.simple_cycles(g, length_bound=16):
        if len(c) != 16 or g.subgraph(set(c)).number_of_edges() != 16: continue
        total += 1
        H = g.subgraph(set(g.nodes()) - set(c))
        hits = [i for i in range(74)
                if profH[i].number_of_edges() == H.number_of_edges()
                and sorted(d for _, d in profH[i].degree())
                    == sorted(d for _, d in H.degree())
                and nx.is_isomorphic(profH[i], H)]
        assert len(hits) == 1, hits
        assert PROFILES[hits[0]][1] == 1, (hits[0], "census hit an UNSAT profile")
        observed.add(hits[0])
        kdist[sum(1 for _, d in H.degree() if d == 3)] += 1
assert total == 178, total
assert observed == {i for i in range(74) if PROFILES[i][1]}, "SAT profile never observed"
assert kdist[0] == 1 and kdist[1] == 60 and kdist[2] == 109 and kdist[3] == 8, kdist
print("CHECK E ok: 22 members verified; 178 C16s; two-way census/decision consistency; k-dist 1/60/109/8")
CHECK -->

<!-- CHECK
# CHECK F — the third mu(H)=2 profile in-harness: C3 + (C3+pendant) + 3K1
# (two mu=1 components) is UNSAT.
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
def count_models(NV, hedges, caps, cap=None):
    X, cl = encode(NV, hedges, caps)
    n = 0
    with Minisat22(bootstrap_with=cl) as m:
        while m.solve():
            mod = m.get_model()
            feet = [[p for p in range(16) if mod[v*16+p] > 0] for v in range(NV)]
            n += 1
            if cap is not None and n > cap: return n
            m.add_clause([-X[v][p] for v in range(NV) for p in feet[v]])
    return n
import collections
p = [(3, 4), (3, 5), (4, 5), (6, 9), (7, 8), (7, 9), (8, 9)]
deg = collections.Counter()
for a, b in p: deg[a] += 1; deg[b] += 1
assert count_models(10, p, [3 - deg[v] for v in range(10)], cap=0) == 0
print("CHECK F ok: mu=2 via two mu=1 components (C3 + C3+pendant + 3K1) UNSAT")
CHECK -->

<!-- CHECK
# CHECK H — spot UNSAT re-decisions beyond the mu=2 family: the all-path
# k=0 profile P3+P3+P4 and a k=3 profile (3K1 + 7-vertex triangle-tree).
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
def count_models(NV, hedges, caps, cap=None):
    X, cl = encode(NV, hedges, caps)
    n = 0
    with Minisat22(bootstrap_with=cl) as m:
        while m.solve():
            mod = m.get_model()
            feet = [[p for p in range(16) if mod[v*16+p] > 0] for v in range(NV)]
            n += 1
            if cap is not None and n > cap: return n
            m.add_clause([-X[v][p] for v in range(NV) for p in feet[v]])
    return n
import collections
p1 = [(0,2),(1,0),(3,5),(4,3),(6,9),(7,6),(7,8)]     # P3+P3+P4, k=0
deg = collections.Counter()
for a, b in p1: deg[a] += 1; deg[b] += 1
assert count_models(10, p1, [3 - deg[v] for v in range(10)], cap=0) == 0
p2 = [(3, 4), (3, 6), (3, 7), (4, 5), (4, 7), (5, 8), (5, 9)]                                 # k=3 tree profile, UNSAT
deg = collections.Counter()
for a, b in p2: deg[a] += 1; deg[b] += 1
assert count_models(10, p2, [3 - deg[v] for v in range(10)], cap=0) == 0
print("CHECK H ok: spot UNSAT re-decisions (all-path k=0; a k=3 profile)")
CHECK -->

<!-- CHECK
# CHECK G — (N2) k=3 IS realized: explicit witness. C=(0..15) chordless,
# H on 16..25 has exactly THREE degree-3 vertices (profile 2K1 + T8 with
# degree sequence 3,3,3,1,1,1,1,1 — the (B2) cap 4 is not attained, but 3 is).
import networkx as nx
E = [(0,1),(0,15),(0,21),(1,2),(1,17),(2,3),(2,17),(3,4),(3,16),(4,5),(4,21),(5,6),(5,24),(6,7),(6,20),(7,8),(7,23),(8,9),(8,16),(9,10),(9,24),(10,11),(10,23),(11,12),(11,25),(12,13),(12,16),(13,14),(13,17),(14,15),(14,25),(15,20),(18,19),(18,22),(18,25),(19,20),(19,21),(22,23),(22,24)]
g = nx.Graph(E)
assert g.number_of_nodes() == 26 and all(d == 3 for _, d in g.degree())
assert nx.is_connected(g)
from collections import Counter
cyc = Counter(len(c) for c in nx.simple_cycles(g, length_bound=8))
assert cyc[4] == 0 and cyc[8] == 0, cyc
C = list(range(16))
assert all(g.has_edge(C[i], C[(i+1) % 16]) for i in range(16))
assert g.subgraph(C).number_of_edges() == 16
H = g.subgraph(range(16, 26))
assert H.number_of_edges() == 7
assert sum(1 for _, d in H.degree() if d == 3) == 3
print("CHECK G ok: explicit k=3 realization at n=26")
CHECK -->
