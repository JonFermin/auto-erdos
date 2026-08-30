---
id: criticality_edge_witness
status: proved
depends_on: []
discharged_by_round: 58
introduced_at_round: 58
---

# Lemma `criticality_edge_witness` (edge-deletion saturation for a minimal cubic counterexample)

Engine of the Q80 criticality program (Section 97). This is a
*conditional* lemma of the standard minimal-counterexample form: it
assumes cubic EGC fails and derives structure of a vertex-minimal
failure. It asserts nothing about whether the class below is empty —
that IS the open conjecture, untouched here.

**Setting.** Let $\mathcal{C}$ be the class of connected cubic simple
graphs containing no cycle whose length is a power of $2$. (Cubic EGC
says $\mathcal{C} = \emptyset$.)

**Lemma.** Suppose $\mathcal{C} \ne \emptyset$, let
$G \in \mathcal{C}$ have the minimum number of vertices $n$ among
members of $\mathcal{C}$, and assume $G$ is triangle-free — hence, as
$C_4$ is a power-of-2 cycle, $\mathrm{girth}(G) \ge 5$. Then for every
non-bridge edge $e = uv$ of $G$ there exist an integer $k \ge 2$ with
$2^k \le n - 2$ and a cycle $C_e$ of $G$ such that either

- **(a) pendant witness:** $|C_e| = 2^k + 1$, exactly one endpoint of
  $e$ (say $u$) lies on $C_e$, and both edges of $u$ other than $e$
  lie on $C_e$; or
- **(b) chord witness:** $|C_e| = 2^k + 2$, both $u$ and $v$ lie on
  $C_e$, and $e \notin E(C_e)$ — i.e. $e$ is a chord of $C_e$.

**Corollary (short-witness classification under girth $\ge 5$).**
In the setting of the Lemma:

1. $k = 2$ witnesses are always pendant: a chord of a $6$-cycle at
   cycle-distance $2$ creates a triangle and at distance $3$ a
   $C_4$ — both absent from $G$. So every non-bridge edge whose
   witness has $k = 2$ lies pendant on a $5$-cycle, and each
   $5$-cycle pendant-witnesses exactly the $5$ off-cycle edges at its
   $5$ vertices (in a cubic graph each cycle vertex has exactly one
   off-cycle edge, and its two cycle edges are automatically "the
   other two edges").
2. $k = 3$ chord witnesses are constrained: a chord of a $10$-cycle at
   distance $d$ creates cycles of lengths $d + 1$ and $11 - d$;
   $d = 2$ gives a $C_3$, $d = 3$ gives a $C_4$ and a $C_8$ — all
   excluded — so only $d \in \{4, 5\}$ (splitting into $C_5 + C_7$ or
   $C_6 + C_6$) can occur.

## Proof

Fix a non-bridge edge $e = uv$. Write $a_u, b_u$ for the neighbors of
$u$ other than $v$, and $a_v, b_v$ for the neighbors of $v$ other than
$u$ (each pair distinct by simplicity).

*Step 0: the six vertices $u, v, a_u, b_u, a_v, b_v$ are distinct.*
$a_u \ne v$ and $a_v \ne u$ by construction; a common neighbor of $u$
and $v$ would form a triangle with $e$ — excluded. So
$\{a_u, b_u\} \cap \{a_v, b_v\} = \emptyset$.

*Step 1: the suppressed graph $G_e$ is a smaller member candidate.*
Delete $e$, then suppress the two degree-$2$ vertices $u$ and $v$:
$V(G_e) = V(G) \setminus \{u, v\}$, and
$E(G_e) = (E(G) - e - \{\text{edges at } u, v\}) \cup \{a_u b_u,\ a_v b_v\}$.

- **Simple:** $a_u b_u \in E(G)$ would give the triangle
  $u a_u b_u$ — excluded (likewise for $a_v b_v$); and
  $\{a_u, b_u\} = \{a_v, b_v\}$ is impossible by Step 0, so no
  parallel edges arise; no loops since $a_u \ne b_u$, $a_v \ne b_v$.
- **Cubic:** every vertex of $G_e$ keeps degree $3$: $a_u$ trades the
  edge $a_u u$ for $a_u b_u$, etc.
- **Connected:** $e$ is not a bridge, so $G - e$ is connected;
  suppression of a degree-$2$ vertex preserves connectivity.
- **Smaller:** $|V(G_e)| = n - 2 < n$.

*Step 2: minimality forces a PO2 cycle downstairs.* If $G_e$ had no
power-of-2 cycle, then $G_e \in \mathcal{C}$ with fewer vertices than
$G$ — contradicting the choice of $G$. So $G_e$ contains a cycle $c'$
with $|c'| = 2^k$ for some $k \ge 2$ ($G_e$ is simple, so
$|c'| \ge 3 > 2$), and $2^k \le |V(G_e)| = n - 2$.

*Step 3: lift $c'$ to $G$.* Every edge of $G_e$ except $a_u b_u$ and
$a_v b_v$ is an edge of $G$. Replace $a_u b_u$ (if $c'$ uses it) by
the path $a_u\, u\, b_u$, and $a_v b_v$ (if used) by $a_v\, v\, b_v$;
since $u, v \notin V(c')$ and $u \ne v$, the result $C_e$ is a simple
cycle of $G$ whose length is $2^k$ plus the number of new edges $c'$
used. That number cannot be $0$: a cycle of $G$ of length $2^k$
contradicts $G \in \mathcal{C}$. If it is $1$ — say $a_u b_u$ — then
$|C_e| = 2^k + 1$, $u \in C_e$ with both its non-$e$ edges
$u a_u, u b_u$ on $C_e$, and $v \notin C_e$: case **(a)**. If it is
$2$, then $|C_e| = 2^k + 2$ and $u, v \in C_e$; the two edges of
$C_e$ at $u$ are $u a_u, u b_u \ne e$, so $e \notin E(C_e)$ and $e$ is
a chord: case **(b)**. $\blacksquare$

*Proof of the Corollary.* A chord of a cycle $C$ of $G$ joining two
vertices at distance $d$ along $C$ ($2 \le d \le \lfloor |C|/2
\rfloor$) closes two cycles of $G$, of lengths $d + 1$ and
$|C| - d + 1$. For $|C| = 6$: $d = 2 \Rightarrow C_3$ (no triangles),
$d = 3 \Rightarrow C_4$ (a PO2 cycle) — so case (b) with $k = 2$ is
impossible, and (a) is the only $k = 2$ witness shape. The per-cycle
accounting in 1. is immediate from cubicity. For $|C| = 10$: $d = 2
\Rightarrow C_3$, $d = 3 \Rightarrow C_4$ and $C_8$ — excluded; $d \in
\{4, 5\}$ yields $\{C_5, C_7\}$ or $\{C_6, C_6\}$, not powers of $2$.
$\blacksquare$

**Interface to the counting program (R59+).** Under the Lemma, every
non-bridge edge of $G$ demands a witness with
$2^k + 2 \le n$, i.e. length in $\{5, 6, 9, 10, 17, 18, 33, 34,
\dots\} \cap [1, n]$; for $n \le 32$ only $\{5, 6, 9, 10, 17, 18\}$
exist, and $6$-witnesses do not exist at all (Corollary 1). Supply is
capped by rigidity: Lemma `c5_rigidity_c8free` bounds
$\#C_5 \le \lfloor 3n/5 \rfloor$, so at most $3n$ edges receive
$k = 2$ witnesses; the analogous caps for $9/10/17/18$ are the next
rungs. Demand is $3n/2 - \#\mathrm{bridges}$.

<!-- CHECK
# criticality_edge_witness CHECK 1 (deterministic, stdlib): validate the
# delete-suppress-lift bookkeeping of Steps 1-3 on cubic girth>=5 graphs
# (Petersen, Heawood-like, seeded random). These test graphs are NOT
# counterexamples, so lifts with 0 new edges are legal here; the CHECK
# asserts every structural claim the proof makes: G_e simple cubic
# connected on n-2 vertices, new edges distinct and absent from G, every
# PO2 cycle of G_e lifts to a simple cycle of G of length 2^k + (#new
# edges used), pendant lifts avoid the other endpoint, chord lifts avoid
# e itself.
import random

def adj_of(n, edges):
    a = [set() for _ in range(n)]
    for u, v in edges:
        a[u].add(v); a[v].add(u)
    return a

def girth_ge5(adj, n):
    for s in range(n):
        for w in adj[s]:
            for x in adj[w]:
                if x != s:
                    if s in adj[x]:
                        return False
                    for y in adj[x]:
                        if y != w and y != s and s in adj[y]:
                            return False
    return True

def connected_verts(adj, verts):
    verts = set(verts)
    s = next(iter(verts))
    seen, stk = {s}, [s]
    while stk:
        u = stk.pop()
        for w in adj[u]:
            if w in verts and w not in seen:
                seen.add(w); stk.append(w)
    return seen == verts

def cycles_of_length(adj, verts, L):
    out = []
    for s in sorted(verts):
        stack = [(s, (s,))]
        while stack:
            u, path = stack.pop()
            if len(path) == L:
                if s in adj[u] and path[1] < path[-1]:
                    out.append(path)
                continue
            for w in adj[u]:
                if w in verts and w > s and w not in path:
                    stack.append((w, path + (w,)))
    return out

def bridges(adj, n):
    disc, low, out, t = {}, {}, set(), [0]
    def dfs(u, pe):
        disc[u] = low[u] = t[0]; t[0] += 1
        for w in adj[u]:
            eid = frozenset((u, w))
            if eid == pe:
                continue
            if w in disc:
                low[u] = min(low[u], disc[w])
            else:
                dfs(w, eid)
                low[u] = min(low[u], low[w])
                if low[w] > disc[u]:
                    out.add(eid)
    dfs(0, None)
    return out

def rand_cubic_g5(n, rng, tries=4000):
    for _ in range(tries):
        stubs = [v for v in range(n) for _ in range(3)]
        rng.shuffle(stubs)
        E, ok = set(), True
        for i in range(0, 3 * n, 2):
            u, v = stubs[i], stubs[i + 1]
            if u == v or (min(u, v), max(u, v)) in E:
                ok = False
                break
            E.add((min(u, v), max(u, v)))
        if not ok:
            continue
        adj = adj_of(n, E)
        if connected_verts(adj, range(n)) and girth_ge5(adj, n):
            return sorted(E)
    return None

def probe_graph(n, E, name):
    adj = adj_of(n, E)
    assert girth_ge5(adj, n), name
    br = bridges(adj, n)
    rng = random.Random(sum(u * 31 + v for u, v in E) & 0xffff)
    cand = [e for e in E if frozenset(e) not in br]
    rng.shuffle(cand)
    checked = 0
    for (u, v) in cand[:4]:
        au, bu = sorted(adj[u] - {v})
        av, bv = sorted(adj[v] - {u})
        n1, n2 = frozenset((au, bu)), frozenset((av, bv))
        assert n1 != n2, "new edges coincide => C4 in G"
        assert bu not in adj[au] and bv not in adj[av], "new edge already in G => triangle"
        verts = set(range(n)) - {u, v}
        adj2 = [set(x) for x in adj]
        adj2[u].clear(); adj2[v].clear()
        for x in verts:
            adj2[x].discard(u); adj2[x].discard(v)
        adj2[au].add(bu); adj2[bu].add(au)
        adj2[av].add(bv); adj2[bv].add(av)
        assert all(len(adj2[x]) == 3 for x in verts), "G_e not cubic"
        assert connected_verts(adj2, verts), "G_e disconnected despite non-bridge e"
        for L in (4, 8, 16):
            if L > n - 2:
                continue
            for c in cycles_of_length(adj2, verts, L):
                lifted, used = [], 0
                for i in range(L):
                    a, b = c[i], c[(i + 1) % L]
                    lifted.append(a)
                    if frozenset((a, b)) == n1:
                        lifted.append(u); used += 1
                    elif frozenset((a, b)) == n2:
                        lifted.append(v); used += 1
                m = len(lifted)
                assert m == L + used, "length bookkeeping broken"
                assert len(set(lifted)) == m, "lift not simple"
                for i in range(m):
                    a, b = lifted[i], lifted[(i + 1) % m]
                    assert b in adj[a], "lift edge missing in G"
                if used == 1:
                    w = u if u in lifted else v
                    assert (v if w == u else u) not in lifted, "pendant lift hits both endpoints"
                elif used == 2:
                    iu, iv = lifted.index(u), lifted.index(v)
                    assert abs(iu - iv) not in (1, m - 1), "e lies ON the chord-witness cycle"
                checked += 1
    return checked

pet = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] \
    + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
total = probe_graph(10, sorted(tuple(sorted(e)) for e in pet), "petersen")
hea = [(i, (i + 1) % 14) for i in range(14)] \
    + [tuple(sorted((i, (i + 5) % 14))) for i in range(0, 14, 2)]
total += probe_graph(14, sorted(set(tuple(sorted(e)) for e in hea)), "heawood_like")
rng = random.Random(20260830)
for n in (14, 16):
    for s in range(3):
        E = rand_cubic_g5(n, rng)
        if E:
            total += probe_graph(n, E, f"rand{n}_{s}")
assert total >= 20, "probe vacuous"
CHECK -->
