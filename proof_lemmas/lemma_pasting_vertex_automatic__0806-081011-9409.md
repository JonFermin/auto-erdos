---
id: pasting_vertex_automatic
status: proved
depends_on: [fund_pair_overlap, pasting_meeting_structure]
discharged_by_round: null
introduced_at_round: 25
---

# Lemma `pasting_vertex_automatic` (in subcubic graphs the stray-vertex condition is free; the meeting criterion collapses to one interval condition)

**Setting.** As in `pasting_meeting_structure`: $T$ a DFS tree of a
connected simple graph $G$, $B_1 = (s_1, a_1)$, $B_2 = (s_2, a_2)$ an
overlapping back-edge pair ($k_{12} \ge 1$, so $D = C_1 \triangle C_2$
is a single cycle by `fund_pair_overlap`(2)), $B_3 \notin \{B_1, B_2\}$
a third back edge with tree path $P_3$ and fundamental cycle
$C_3 = P_3 + B_3$, and $E(D) \cap E(T) = A \sqcup L_1 \sqcup L_2$ the
three-segment decomposition of `pasting_meeting_structure`(1).

**Claim.**

1. **(Two-cycle vertex-meeting, $\Delta(G) \le 3$.)** Let $G$ be any
   graph of maximum degree $\le 3$ and let $Z, Z'$ be cycles
   (edge sets in which every vertex has degree exactly 2) with
   $v \in V(Z) \cap V(Z')$. Then $Z$ and $Z'$ share an edge incident
   to $v$. In particular two cycles of a subcubic graph can never cross
   at a vertex without sharing an edge there.
2. **(Vertex-automatic pasting.)** If $\Delta(G) \le 3$ and exactly one
   of the three intersections $P_3 \cap A$, $P_3 \cap L_1$,
   $P_3 \cap L_2$ is edge-nonempty, then every shared vertex of $D$ and
   $C_3$ lies on that subpath — the stray-vertex condition of
   `pasting_meeting_structure`(3) holds automatically.
3. **(Collapsed meeting criterion.)** Hence for $\Delta(G) \le 3$:
   $D \cap C_3$ is a single path of length $k' \ge 1$ (the
   `triple_sym_diff_structure`(5) pasting hypothesis) **iff** exactly
   one of the three intersections is edge-nonempty; $k'$ is that
   interval's length. The R24 "vertex-automatic" conjecture is proved.

**Proofs.**

*(1)* $Z$ is a cycle through $v$, so exactly 2 of $v$'s incident edges
lie in $Z$; likewise exactly 2 lie in $Z'$. If the two pairs were
disjoint, $v$ would have $\ge 4$ distinct incident edges, contradicting
$\deg_G(v) \le 3$. So the pairs intersect: some edge at $v$ lies in both
$Z$ and $Z'$. □

*(2)* Let $X \in \{A, L_1, L_2\}$ be the unique segment with
$P_3 \cap X \ne \varnothing$. By `pasting_meeting_structure`(0)–(1),
$$E(D) \cap E(C_3) \;=\; P_3 \cap (A \sqcup L_1 \sqcup L_2) \;=\; P_3 \cap X$$
(the back edges contribute nothing: $B_3 \notin \{B_1, B_2\}$ and back
edges are not tree edges), and by (2) of that lemma $P_3 \cap X$ is a
single contiguous vertical subpath. Now let $v$ be ANY shared vertex of
$D$ and $C_3$. Both $D$ and $C_3$ are cycles through $v$ ($D$ is a
single cycle since $k_{12} \ge 1$; $C_3$ is a fundamental cycle), so by
(1) some edge $e$ at $v$ lies in $E(D) \cap E(C_3) = P_3 \cap X$. Thus
$v$ is an endpoint of an edge of the subpath $P_3 \cap X$, i.e. lies on
it. No stray shared vertex exists. □

*(3)* ($\Leftarrow$) By (2) the stray-vertex half of the
`pasting_meeting_structure`(3) criterion is automatic, and exactly one
nonempty intersection is the other half, so the iff there applies.
($\Rightarrow$) is `pasting_meeting_structure`(3) verbatim (it needs no
degree hypothesis). The length statement carries over. □

**Scope remarks.**

- The degree bound is sharp: at a vertex of degree $\ge 4$ two cycles
  CAN cross vertex-only (two edge-disjoint cycles through one vertex),
  and the proof of (2) uses nothing else. So the collapse is a genuinely
  subcubic phenomenon — consistent with the R24 census being
  cubic-sampled. Non-cubic minimum-degree-3 graphs are NOT covered; the
  reduction of the Erdős–Gyárfás problem to the (sub)cubic case remains
  a separate open item (Section 29 reduction-gap note).
- (1) is fully general (any two cycles, not just $D$ and a fundamental
  cycle) and reusable: e.g. it also shows that in a cubic graph any two
  fundamental cycles meet, vertex-wise, exactly along their shared-edge
  paths — the `fund_pair_overlap` census fact.

**Consequence for Q9 (meeting existence).** Combined with
`mixed_overlap_supply`(1) (in a 2-connected graph every tree edge of $D$
is covered by some back edge), meeting-existence for cubic graphs is now
exactly: *some even-gap back edge $B_3$ covers a tree edge of exactly
one segment of $D$ and none of the other two* — a pure
interval-covering statement on the three vertical segments, with no
vertex side conditions. The tuning targets T1–T3
(`pasting_value_interval`) are unchanged; they now sit on a fully proved
meeting foundation.

---

<!-- CHECK
# pasting_vertex_automatic: (a) two-cycle vertex-meeting fact — every
# shared vertex of the cycles D and C3 is incident to a shared edge;
# (b) collapsed criterion — D∩C3 single path IFF exactly one of the
# three segment intersections is edge-nonempty, with k' = its length.
# Cubic samples (deg == 3 everywhere, the boundary case of Δ ≤ 3).
import random

def sample_cubic(nn, rnd, tries=3000):
    for _ in range(tries):
        stubs = [v for v in range(nn) for _ in range(3)]
        rnd.shuffle(stubs)
        edges = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b or (min(a, b), max(a, b)) in edges:
                ok = False; break
            edges.add((min(a, b), max(a, b)))
        if not ok: continue
        el = list(edges)
        deg = [0] * nn
        for a, b in el: deg[a] += 1; deg[b] += 1
        if min(deg) == 3 and max(deg) == 3:
            adj = [[] for _ in range(nn)]
            for a, b in el: adj[a].append(b); adj[b].append(a)
            seen = {0}; stack = [0]
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if w not in seen: seen.add(w); stack.append(w)
            if len(seen) == nn: return el
    return None

def is_ancestor(u, v, depth, par):
    if depth[u] > depth[v]: return False
    x = v
    while depth[x] > depth[u]: x = par[x]
    return x == u

def dfs_tree(n, edges, r, shuffled_adj):
    depth = [-1] * n; par = [-1] * n
    depth[r] = 0; visited = [False] * n; visited[r] = True
    stack = [(r, iter(shuffled_adj[r]))]
    while stack:
        u, it = stack[-1]; adv = False
        for w in it:
            if not visited[w]:
                visited[w] = True; depth[w] = depth[u] + 1; par[w] = u
                stack.append((w, iter(shuffled_adj[w]))); adv = True; break
        if not adv: stack.pop()
    tree_mask = 0
    for i, (u, v) in enumerate(edges):
        if depth[u] == depth[v] + 1 and par[u] == v: tree_mask |= 1 << i
        elif depth[v] == depth[u] + 1 and par[v] == u: tree_mask |= 1 << i
    nontree = []
    for i, (u, v) in enumerate(edges):
        if not (tree_mask >> i & 1):
            a, b = (u, v) if depth[u] <= depth[v] else (v, u)
            if not is_ancestor(a, b, depth, par): return None
            nontree.append((b, a, depth[b] - depth[a]))
    return depth, par, nontree

def vpath_edges(lo, hi, par):
    es = set(); u = lo
    while u != hi:
        p = par[u]; es.add((min(u, p), max(u, p))); u = p
    return es

def fund_cycle_edges(sender, ancestor, par):
    es = vpath_edges(sender, ancestor, par)
    es.add((min(sender, ancestor), max(sender, ancestor)))
    return es

def lca(u, v, depth, par):
    while depth[u] > depth[v]: u = par[u]
    while depth[v] > depth[u]: v = par[v]
    while u != v: u = par[u]; v = par[v]
    return u

def single_cycle_len(sym):
    if not sym: return None
    deg = {}
    for u, v in sym: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if any(d != 2 for d in deg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    start = next(iter(deg)); seen = {start}; stk = [start]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(sym) if len(seen) == len(deg) else None

def path_len_of_intersection(cyc1, cyc2):
    es = cyc1 & cyc2
    if not es: return None
    vs1 = {v for e in cyc1 for v in e}
    vs2 = {v for e in cyc2 for v in e}
    shared_v = vs1 & vs2
    deg = {}
    for u, v in es: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if set(deg) != shared_v: return None
    ends = [v for v, d in deg.items() if d == 1]
    if len(ends) != 2 or any(d > 2 for d in deg.values()): return None
    adjP = {}
    for u, v in es:
        adjP.setdefault(u, []).append(v); adjP.setdefault(v, []).append(u)
    seen = {ends[0]}; stk = [ends[0]]
    while stk:
        u = stk.pop()
        for w in adjP[u]:
            if w not in seen: seen.add(w); stk.append(w)
    if len(seen) != len(deg): return None
    return len(es)

rng = random.Random(20260806 + 25)
pairs_seen = 0; triples_seen = 0
one_nonempty = 0; shared_vertex_checks = 0
for nn in (10, 12, 14, 16):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(100):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(3):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            depth, par, be = res
            m = len(be)
            fc = [fund_cycle_edges(s, a, par) for s, a, _ in be]
            pe = [vpath_edges(s, a, par) for s, a, _ in be]
            for i in range(m):
                s1, a1, g1 = be[i]
                for j in range(i + 1, m):
                    s2, a2, g2 = be[j]
                    D = fc[i] ^ fc[j]
                    if single_cycle_len(D) is None: continue
                    pairs_seen += 1
                    mm = lca(s1, s2, depth, par)
                    a_deep, a_sh = (a1, a2) if depth[a1] >= depth[a2] else (a2, a1)
                    A = vpath_edges(a_deep, a_sh, par)
                    L1 = vpath_edges(s1, mm, par)
                    L2 = vpath_edges(s2, mm, par)
                    Dverts = {v for e in D for v in e}
                    for z in range(m):
                        if z == i or z == j: continue
                        triples_seen += 1
                        P3 = pe[z]
                        C3 = fc[z]
                        C3verts = {v for e in C3 for v in e}
                        sharedE = D & C3
                        for v in (Dverts & C3verts):
                            shared_vertex_checks += 1
                            assert any(v in e for e in sharedE), \
                                (f"FALSIFIED(1): stray shared vertex v={v} with no shared incident edge "
                                 f"(n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})")
                        inters = [P3 & X for X in (A, L1, L2)]
                        nonempty = sum(1 for q in inters if q)
                        kk = path_len_of_intersection(D, C3)
                        pred = (nonempty == 1)
                        truth = kk is not None
                        assert pred == truth, \
                            (f"FALSIFIED(3): collapsed criterion mismatch pred={pred} truth={kk} "
                             f"(n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})")
                        if pred:
                            one_nonempty += 1
                            klen = max(len(q) for q in inters)
                            assert klen == kk, \
                                (f"FALSIFIED(3k): k' mismatch {klen} != {kk} "
                                 f"(n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})")
assert pairs_seen > 5000 and triples_seen > 30000, \
    f"probe vacuous: pairs={pairs_seen} triples={triples_seen}"
print(f"pairs={pairs_seen} triples={triples_seen} shared_vertex_checks={shared_vertex_checks} "
      f"one_nonempty={one_nonempty} "
      f"— two-cycle vertex-meeting fact and collapsed meeting criterion verified")
CHECK -->

## Summary

Proved (R25): in a graph of maximum degree $\le 3$, two cycles sharing a
vertex must share an edge at that vertex (2 + 2 > 3 pigeonhole on the
incident edges). Consequently the stray-vertex half of the
`pasting_meeting_structure`(3) criterion is automatic in subcubic
graphs, and the pasting hypothesis for $(B_1, B_2, B_3)$ holds **iff**
$P_3$ meets exactly one of the three segments $A, L_1, L_2$ in an edge —
the R24 vertex-automatic conjecture, now a theorem. Meeting-existence
for cubic graphs is reduced to a pure interval-covering question.
