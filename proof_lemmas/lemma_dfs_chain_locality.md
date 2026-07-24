---
id: dfs_chain_locality
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 1
---

# Lemma: pairwise chain-locality for DFS fundamental cycles

**Statement.** For every connected simple graph $G$ with minimum degree $\ge 3$
and at most $10$ vertices, and for every DFS tree $T$ of $G$ (enumerated by
starting vertex), there exists a simple cycle $C$ in $G$ whose length is a
power of $2$ ($4, 8, 16, \ldots$) such that $C$ is one of:

1. a **fundamental cycle** of $T$: a tree path between the endpoints of a
   back edge, closed by that back edge; or
2. the **symmetric difference of two fundamental cycles** of $T$, when that
   symmetric difference forms a simple cycle (every vertex has degree exactly
   $2$ in the edge-set and the edge-set is connected).

**Motivation.** In a hypothetical Erdős–Gyárfás counterexample (min degree
$\ge 3$, no power-of-2 cycle of any length), fix a DFS tree $T$. Every back
edge $(v, u)$ with $u$ an ancestor of $v$ spans a depth-gap
$\delta = \operatorname{depth}(v) - \operatorname{depth}(u)$; the
corresponding fundamental cycle has length $\delta + 1$. Forbidding power-of-2
lengths means $\delta \notin \{3, 7, 15, 31, \ldots\}$. Min degree $3$ forces
every DFS leaf to carry $\ge 2$ back edges. If pairwise chain-locality holds,
the DFS tree structure itself produces a power-of-2 cycle — contradicting the
counterexample hypothesis. Failure would instead mean the conjecture's power-of-2
cycles are always "non-DFS-structured" on small graphs, redirecting the proof
search away from depth-chain discharging.

**Killable first lemma.** The conjecture is open; a failure of this lemma on any
graph $\le 10$ vertices would falsify the approach and be documented as a
dead end. A uniform pass (all named and exhaustive cases) is evidence but not
proof, since the lemma as stated covers only $n \le 10$.

<!-- CHECK
# Pairwise chain-locality falsification probe.
# Tests: all connected min-degree-3 simple graphs on n=4,5,6 (exhaustive)
# and named graphs Cube/Q3, Wagner (n=8), Petersen (n=10).
# Failure = lemma falsified on that graph+DFS-tree pair.

def is_pow2(n):
    return n > 1 and (n & (n - 1)) == 0

def build_dfs(adj_list, src):
    n = len(adj_list)
    parent = [-1] * n
    visited = [False] * n
    back = []
    seen_back = set()

    def rec(v, p):
        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = True
                parent[w] = v
                rec(w, v)
            elif w != p:
                key = (min(v, w), max(v, w))
                if key not in seen_back:
                    seen_back.add(key)
                    back.append(key)

    visited[src] = True
    rec(src, -1)
    return parent, back

def fund_edges(parent, u, v):
    anc_u = set()
    cur = u
    while cur != -1:
        anc_u.add(cur)
        cur = parent[cur]
    desc, anc = (u, v) if v in anc_u else (v, u)
    edges = set()
    cur = desc
    while cur != anc:
        p = parent[cur]
        edges.add((min(cur, p), max(cur, p)))
        cur = p
    edges.add((min(u, v), max(u, v)))
    return edges

def sd_cycle_len(e1, e2):
    sd = e1.symmetric_difference(e2)
    if not sd:
        return 0
    deg = {}
    for a, b in sd:
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
    if any(d != 2 for d in deg.values()):
        return 0
    verts = list(deg)
    nb2 = {v2: [] for v2 in verts}
    for a, b in sd:
        nb2[a].append(b)
        nb2[b].append(a)
    vis = {verts[0]}
    q = [verts[0]]
    while q:
        cur = q.pop()
        for w in nb2[cur]:
            if w not in vis:
                vis.add(w)
                q.append(w)
    return len(sd) if len(vis) == len(verts) else 0

def check_graph(adj, label):
    n = len(adj)
    for src in range(n):
        parent, back = build_dfs(adj, src)
        fcs = [fund_edges(parent, u, v) for u, v in back]
        ok = any(is_pow2(len(fc)) for fc in fcs)
        if not ok:
            k = len(fcs)
            for i in range(k):
                for j in range(i + 1, k):
                    sd = sd_cycle_len(fcs[i], fcs[j])
                    if sd and is_pow2(sd):
                        ok = True
                        break
                if ok:
                    break
        assert ok, f"chain-locality FAILS: {label}, src={src}, back={back}"

def make_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def is_connected(adj):
    n = len(adj)
    vis = [False] * n
    vis[0] = True
    q = [0]
    cnt = 1
    while q:
        v = q.pop()
        for w in adj[v]:
            if not vis[w]:
                vis[w] = True
                cnt += 1
                q.append(w)
    return cnt == n

# Exhaustive n=4..6: all connected min-degree-3 simple graphs
checked = 0
for n in (4, 5, 6):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    np2 = len(pairs)
    for mask in range(1 << np2):
        edges = [pairs[k] for k in range(np2) if (mask >> k) & 1]
        adj = make_adj(n, edges)
        if not is_connected(adj):
            continue
        if min(len(nb) for nb in adj) < 3:
            continue
        check_graph(adj, f"n{n}m{mask}")
        checked += 1

# Named graphs n=8
check_graph(make_adj(8, [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]), "Cube_Q3")
check_graph(make_adj(8, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,0),(0,4),(1,5),(2,6),(3,7)]), "Wagner")

# Petersen graph n=10 (3-regular, girth 5 — most interesting case)
check_graph(make_adj(10, [(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(1,6),(2,7),(3,8),(4,9),(5,7),(7,9),(9,6),(6,8),(8,5)]), "Petersen")

checked += 3
assert checked >= 10
print(f"OK: pairwise chain-locality holds on {checked} graphs (exhaustive n<=6, named n=8,10)")
CHECK -->

**Proof direction (if CHECK passes).** Let $G$ be a connected min-degree-$3$
graph and $T$ a DFS tree. Every non-tree edge $e_i = (v_i, u_i)$ with $u_i$
an ancestor of $v_i$ produces fundamental cycle $F_i$ of length
$\delta_i + 1$ ($\delta_i = \operatorname{depth}(v_i) - \operatorname{depth}(u_i)$).
If some $\delta_i + 1$ is a power of $2$, done. Otherwise, consider two back
edges sharing a "depth-chain segment": if $u_j$ lies on the tree path
$v_i \dashrightarrow u_i$, then $F_i \triangle F_j$ contains exactly the
tree edges between $u_j$ and $v_i$ that are in $F_i$ but not $F_j$, plus
the tree edges between $u_i$ and $v_j$ (reversed), plus both back edges —
and if the two fundamental cycles share exactly one contiguous tree path
(nesting condition), the result is a simple cycle of length
$(\delta_i + 1) + (\delta_j + 1) - 2\ell$ where $\ell$ is the length of
the shared path. Whether a combination of gap-lengths forbidden from
$\{3, 7, 15, \ldots\}$ can produce a power-of-2 sum minus even overlap is
the arithmetic question that the depth-chain discharging argument would
need to close. The CHECK decides the small-$n$ base case; the general
argument (if the lemma holds) requires a structural analysis of DFS
depth-gap arithmetic.
