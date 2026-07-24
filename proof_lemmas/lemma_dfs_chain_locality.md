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

<!-- CHECK
# Petersen graph mechanism check: does every DFS tree have a FUNDAMENTAL C8,
# or does some DFS root require a sym-diff?  Answer: every root has fund C8.

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

def depth_of(parent, v):
    d = 0
    while parent[v] != -1:
        v = parent[v]
        d += 1
    return d

petersen = [(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(1,6),(2,7),(3,8),(4,9),(5,7),(7,9),(9,6),(6,8),(8,5)]
adj = [[] for _ in range(10)]
for u, v in petersen:
    adj[u].append(v)
    adj[v].append(u)

fund_c8_count = 0
for src in range(10):
    parent, back = build_dfs(adj, src)
    depths = [depth_of(parent, i) for i in range(10)]
    fund_lens = []
    for u, v in back:
        desc = u if depths[u] > depths[v] else v
        anc = v if depths[u] > depths[v] else u
        gap = depths[desc] - depths[anc]
        fund_lens.append(gap + 1)
    has_fund_pow2 = any(is_pow2(fl) for fl in fund_lens)
    assert has_fund_pow2, f"Petersen src={src}: no fund pow2, fund_lens={fund_lens}"
    if any(fl == 8 for fl in fund_lens):
        fund_c8_count += 1

assert fund_c8_count == 10, f"Expected 10 roots with fund C8, got {fund_c8_count}"
print(f"OK: Petersen — all 10 DFS roots have a fundamental C8 (back edge with depth-gap 7)")
CHECK -->

<!-- CHECK
# n=7 sampling: every 50th valid (connected, min-deg>=3) simple graph on 7 vertices.
# 7 vertices -> 21 possible edges. Minimum edges for min-deg-3: ceil(7*3/2)=11.

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

def check_graph(adj):
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
        if not ok:
            return False
    return True

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

n = 7
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
np2 = len(pairs)  # 21
checked = 0
failures = 0
step = 50  # sample every 50th
for mask in range(0, 1 << np2, step):
    edges = [pairs[k] for k in range(np2) if (mask >> k) & 1]
    adj = make_adj(n, edges)
    if not is_connected(adj):
        continue
    if min(len(nb) for nb in adj) < 3:
        continue
    if not check_graph(adj):
        failures += 1
    checked += 1

assert failures == 0, f"n=7 sample: {failures} failures out of {checked} graphs"
assert checked >= 1000, f"Too few n=7 graphs sampled: {checked}"
print(f"OK: n=7 sample ({checked} graphs, step={step}), 0 failures")
CHECK -->

<!-- CHECK
# Additional named graphs: n=12 Franklin, n=14 Heawood, n=10 second cubic.
# Also n=7 denser sample (stride=5 instead of 50).

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

# Franklin graph: n=12, 3-regular, girth=6, bipartite.
# Vertices 0-5 outer hexagon, 6-11 inner: edges outer hex + matching + inner matches.
franklin_edges = [
    (0,1),(1,2),(2,3),(3,4),(4,5),(5,0),   # outer hexagon
    (0,6),(1,7),(2,8),(3,9),(4,10),(5,11),  # spokes
    (6,9),(7,10),(8,11),(6,11),(7,8),(9,10) # inner connections (Franklin specific)
]
# Verify it's 3-regular
fadj = make_adj(12, franklin_edges)
assert all(len(fadj[v]) == 3 for v in range(12)), "Franklin not 3-regular"
check_graph(fadj, "Franklin_n12")

# Heawood graph: n=14, 3-regular, girth=6. Unique smallest (3,6)-cage.
# Bipartite: vertices 0..6 and 7..13.
# Edge rule: i in {0..6} connects to i+7, (i+2)%7+7, (i+6)%7+7.
heawood_edges = []
for i in range(7):
    heawood_edges.append((i, 7 + i))
    heawood_edges.append((i, 7 + (i + 2) % 7))
    heawood_edges.append((i, 7 + (i + 6) % 7))
hadj = make_adj(14, heawood_edges)
assert all(len(hadj[v]) == 3 for v in range(14)), "Heawood not 3-regular"
check_graph(hadj, "Heawood_n14")

# McGee graph: n=24, 3-regular, girth=7. Skip (too large for this lemma's n<=10 scope).

# Second Petersen-family graph: dodecahedron is n=20, skip.
# Instead: GP(5,2) = Petersen-like, n=10.  GP(5,1) = prism over C5.
# GP(5,1): outer 5-cycle 0-4, inner 5-cycle 5-9, spokes.
gp51_edges = [(i, (i+1)%5) for i in range(5)]           # outer C5
gp51_edges += [(5+i, 5+(i+1)%5) for i in range(5)]       # inner C5
gp51_edges += [(i, 5+i) for i in range(5)]               # spokes
gp51adj = make_adj(10, gp51_edges)
assert all(len(gp51adj[v]) == 3 for v in range(10))
check_graph(gp51adj, "GP51_n10")

# n=7 denser sample: stride=5 (covers ~10x more than stride=50)
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

def check_graph_bool(adj):
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
        if not ok:
            return False
    return True

nn = 7
pairs7 = [(i, j) for i in range(nn) for j in range(i + 1, nn)]
np2 = len(pairs7)  # 21
checked7 = 0
failures7 = 0
step = 5
for mask in range(0, 1 << np2, step):
    edges = [pairs7[k] for k in range(np2) if (mask >> k) & 1]
    adj7 = make_adj(nn, edges)
    if not is_connected(adj7):
        continue
    if min(len(nb) for nb in adj7) < 3:
        continue
    if not check_graph_bool(adj7):
        failures7 += 1
    checked7 += 1

assert failures7 == 0, f"n=7 stride-5 sample: {failures7} failures out of {checked7} graphs"
assert checked7 >= 10000, f"Too few n=7 graphs sampled: {checked7}"
print(f"OK: Franklin n=12, Heawood n=14, GP(5,1) n=10 all PASS")
print(f"OK: n=7 stride-5 sample ({checked7} graphs, 0 failures)")
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
