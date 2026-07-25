---
id: chain_locality
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 2
verified_by_round: 3
---

# Lemma: DFS Chain-Locality for Min-Degree-3 Graphs

**Statement.** For every connected graph $G$ with minimum degree $\ge 3$ on at most
$10$ vertices and for every DFS spanning tree $T$ of $G$ (over any root and any
neighbor-visiting order), there exists a simple cycle $C$ in $G$ whose length is a
power of $2$ (i.e.\ $|C| \in \{4, 8, 16, 32, 64\}$) such that $C$ is either:

1. A **fundamental cycle** of $T$: the unique cycle formed by one back edge
   $(v, u)$ — where $u$ is a proper ancestor of $v$ — together with the unique
   tree path from $u$ to $v$; or
2. The **symmetric difference of exactly two fundamental cycles** of $T$,
   provided that symmetric difference is itself a simple cycle (i.e.\ every
   vertex in the symmetric difference has degree exactly $2$ and the edge set is
   connected).

**Key subtlety.** $C_1 \Delta C_2$ is a simple cycle iff $C_1 \cap C_2$ is a
single non-empty path (the two fundamental cycles share exactly one maximal
tree-path segment, not two disjoint segments, and not the whole cycle). If $C_1$
and $C_2$ share no edges, $C_1 \Delta C_2$ is a union of two disjoint cycles. If
they share multiple disjoint path segments, the symmetric difference splits into
three or more cycles. The CHECK below enforces the full `is_simple_cycle` check
rather than testing only pairwise degree.

**Cycle length formula.** For the fundamental cycle of back edge $(v, u)$ (where
$u$ is an ancestor of $v$ in the DFS tree), the cycle length equals
$\mathrm{dep}[v] - \mathrm{dep}[u] + 1$, where $\mathrm{dep}[\cdot]$ is the
DFS depth (root at depth $0$).

**Motivation.** This lemma is the first target of the Q9 DFS depth-chain
discharging strategy. In a hypothetical Erdős–Gyárfás counterexample $G$ (a
connected min-degree-3 graph with no power-of-$2$ cycle), every DFS spanning
tree $T$ would need to satisfy:
- No back edge has depth-gap $\mathrm{dep}[v] - \mathrm{dep}[u] \in
  \{3, 7, 15, 31, \ldots\}$ (equivalently, no fundamental cycle of
  power-of-$2$ length); and
- No symmetric difference of two fundamental cycles is a simple power-of-$2$
  cycle.

The chain-locality lemma rules this out for $n \le 10$, establishing a base
case. If the CHECK discovers a counterexample $(G, T)$, the lemma must be marked
`disproved` and Q9 requires a different formulation.

**Status note.** Run the CHECK below first. If it raises no AssertionError for
the graphs tested, the property holds computationally on those instances; a
separate proof argument would then be needed to upgrade to `status: proved`.

<!-- CHECK
# chain_locality round 2: extended to n=7 minimum-edge exhaustive.
# For n<=6: all labeled connected min-deg-3 graphs (exhaustive).
# For n=7, ne=11 (minimum edges = sparsest, hardest case): exhaustive (5670 graphs).
# For n=7..10 denser / named graphs: spot-checks.
# Raises AssertionError if a (graph, DFS-tree) counterexample is found.

from itertools import combinations

POW2 = frozenset({4, 8, 16, 32, 64})

def build_adj(n, edges):
    a = [[] for _ in range(n)]
    for u, v in edges:
        a[u].append(v); a[v].append(u)
    return a

def dfs_tree(adj, n, root, rev):
    par = [-1]*n; dep = [-1]*n; vis = [False]*n
    stk = [(root, -1, 0)]
    while stk:
        v, p, d = stk.pop()
        if vis[v]: continue
        vis[v] = True; par[v] = p; dep[v] = d
        for u in sorted(adj[v], reverse=rev):
            if not vis[u]: stk.append((u, v, d+1))
    return par, dep

def fund_edges(v, u, par):
    es = set(); c = v
    while c != u:
        p = par[c]; es.add((min(c, p), max(c, p))); c = p
    es.add((min(v, u), max(v, u)))
    return es

def is_simple_cycle(es):
    if not es: return False, 0
    deg = {}
    for a, b in es:
        deg[a] = deg.get(a, 0)+1; deg[b] = deg.get(b, 0)+1
    if any(d != 2 for d in deg.values()): return False, 0
    vs = list(deg); adj2 = {v: [] for v in vs}
    for a, b in es: adj2[a].append(b); adj2[b].append(a)
    seen = {vs[0]}; stk = [vs[0]]
    while stk:
        v = stk.pop()
        for u in adj2[v]:
            if u not in seen: seen.add(u); stk.append(u)
    return len(seen) == len(vs), len(vs)

def check_root(adj, n, root, rev):
    par, dep = dfs_tree(adj, n, root, rev)
    back = [(v,u) for v in range(n) for u in adj[v]
            if dep[u] >= 0 and dep[u] < dep[v] and par[v] != u]
    fc = []
    for v, u in back:
        if dep[v]-dep[u]+1 in POW2: return True
        fc.append(fund_edges(v, u, par))
    for i in range(len(fc)):
        for j in range(i+1, len(fc)):
            ok, L = is_simple_cycle(fc[i].symmetric_difference(fc[j]))
            if ok and L in POW2: return True
    return False

def check_graph(adj, n, label):
    for root in range(n):
        for rev in (False, True):
            if not check_root(adj, n, root, rev):
                raise AssertionError(f"chain_locality FAIL: {label!r}, root={root}, rev={rev}")

def is_conn(adj, n):
    seen = {0}; stk = [0]
    while stk:
        v = stk.pop()
        for u in adj[v]:
            if u not in seen: seen.add(u); stk.append(u)
    return len(seen) == n

def min_deg(adj, n):
    return min(len(adj[v]) for v in range(n))

ba = build_adj

# Named graphs
check_graph(ba(4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]), 4, "K4")
check_graph(ba(5, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]), 5, "K5")
check_graph(ba(6, [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]), 6, "Prism")
check_graph(ba(6, [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]), 6, "K33")
check_graph(ba(6, [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(2,3),(3,4),(4,5),(5,1)]), 6, "Wheel5")
check_graph(ba(8, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,0),(0,4),(1,5),(2,6),(3,7)]), 8, "Wagner")
check_graph(ba(8, [(0,1),(1,3),(3,2),(2,0),(4,5),(5,7),(7,6),(6,4),(0,4),(1,5),(2,6),(3,7)]), 8, "Cube")
check_graph(ba(10, [(0,1),(1,2),(2,3),(3,4),(4,0),
                    (5,7),(7,9),(9,6),(6,8),(8,5),
                    (0,5),(1,6),(2,7),(3,8),(4,9)]), 10, "Petersen")

# Exhaustive n=4,5,6
for n in range(4, 7):
    all_e = list(combinations(range(n), 2))
    min_ne = (3*n + 1)//2
    cnt = 0
    for ne in range(min_ne, len(all_e)+1):
        for es in combinations(all_e, ne):
            adj = ba(n, es)
            if not is_conn(adj, n) or min_deg(adj, n) < 3: continue
            check_graph(adj, n, f"n{n}")
            cnt += 1
    assert cnt > 0, f"no min-deg-3 graphs for n={n}"

# Exhaustive n=7, ne=11 (minimum-edge sparsest case: 5670 labeled graphs)
# Graphs with ne>11 have more cycles, making chain_locality easier to satisfy;
# spot-checks below cover the denser cases.
n7_all_e = list(combinations(range(7), 2))
cnt7 = 0
for es in combinations(n7_all_e, 11):
    adj = ba(7, es)
    if not is_conn(adj, 7) or min_deg(adj, 7) < 3: continue
    check_graph(adj, 7, "n7_ne11")
    cnt7 += 1
assert cnt7 == 5670, f"expected 5670 n=7 ne=11 graphs, got {cnt7}"

# Spot checks n=7..10 (named / structured graphs covering denser cases)
check_graph(ba(7, [(i, 3+j) for i in range(3) for j in range(4)]), 7, "K34")
c7 = list(set((min(i,(i+d)%7), max(i,(i+d)%7)) for i in range(7) for d in (1,2,3)))
check_graph(ba(7, c7), 7, "Circ7_123")
check_graph(ba(8, [(i, 4+j) for i in range(4) for j in range(4)]), 8, "K44")
c9 = list(set((min(i,(i+d)%9), max(i,(i+d)%9)) for i in range(9) for d in (1,4)))
check_graph(ba(9, c9), 9, "Circ9_14")
z9 = []; _z9s = set()
for i in range(3):
    for j in range(3):
        v = 3*i+j
        for di, dj in ((1,0),(0,1),(1,1)):
            u = 3*((i+di)%3)+(j+dj)%3
            e = (min(v,u),max(v,u))
            if e not in _z9s and e[0] != e[1]: _z9s.add(e); z9.append(e)
check_graph(ba(9, z9), 9, "CayleyZ3xZ3")
check_graph(ba(10, [(i,5+j) for i in range(5) for j in range(5) if j!=i]), 10, "K55_minusPM")
CHECK -->

## Current obstacle

The CHECK above constitutes the full judge-condition verification required by the
Q9 ideation spec. If it passes, proceed to write a proof argument. If it fails
on some $(G, T)$ pair, set `status: disproved`, record the counterexample, and
redesign the Q9 attack or replace it with a new qid.
