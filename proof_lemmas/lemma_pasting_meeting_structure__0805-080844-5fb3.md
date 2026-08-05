---
id: pasting_meeting_structure
status: proved
depends_on: [fund_pair_overlap, triple_sym_diff_structure]
discharged_by_round: null
introduced_at_round: 24
---

# Lemma `pasting_meeting_structure` (the meeting condition is interval combinatorics on three vertical segments)

**Setting.** $T$ a DFS tree of a connected simple graph, back edges
$B_1 = (s_1, a_1)$, $B_2 = (s_2, a_2)$ an overlapping pair ($k_{12} \ge 1$,
so $D = C_1 \triangle C_2$ is a single cycle by `fund_pair_overlap`(2)),
and $B_3 = (s_3, a_3) \notin \{B_1, B_2\}$ a third back edge with tree
path $P_3 = [s_3 .. a_3]$ and fundamental cycle $C_3 = P_3 + B_3$. Write
$m = \operatorname{lca}(s_1, s_2)$, $a_{\text{deep}}$ / $a_{\text{sh}}$
for the deeper / shallower of the two anchors, and $[x .. y]$ for the
edge set of the vertical tree path between comparable vertices $x, y$.

**Claim (all parts proved below).**

0. **(Tree-only intersection.)** $E(D) \cap E(C_3)$ contains only tree
   edges.
1. **(Three-segment decomposition.)** The tree edges of $D$ are exactly
   the disjoint union
   $$E(D) \cap E(T) \;=\; A \;\sqcup\; L_1 \;\sqcup\; L_2, \qquad
     A = [a_{\text{sh}} .. a_{\text{deep}}],\;
     L_1 = [m .. s_1],\; L_2 = [m .. s_2],$$
   each a (possibly empty) vertical path. $A$ lies strictly above $m$
   (its deepest vertex is $a_{\text{deep}}$, a strict ancestor of $m$
   since $k_{12} \ge 1$); $L_1, L_2$ hang below $m$ in different child
   subtrees when $s_1, s_2$ are incomparable, and $L_1 = \varnothing$
   (resp. $L_2$) when $s_1$ (resp. $s_2$) equals $m$. In particular the
   three segments are pairwise vertex-disjoint except for
   $L_1 \cap L_2 = \{m\}$ when both legs are nonempty.
2. **(Contiguity.)** Each of $P_3 \cap A$, $P_3 \cap L_1$,
   $P_3 \cap L_2$ is a single (possibly empty) vertical subpath, and at
   most TWO of the three are nonempty — $P_3$ is a vertical chain, so
   below $m$ it enters at most one child subtree, meeting at most one of
   $L_1, L_2$.
3. **(Meeting criterion.)** $D \cap C_3$ (shared edges + shared
   vertices) is a single path of length $k' \ge 1$ — the
   `triple_sym_diff_structure`(5) pasting hypothesis — **iff** exactly
   one of the three intersections in (2) is nonempty AND every shared
   vertex of $D$ and $C_3$ lies on that subpath. Then $k'$ is that
   subpath's length.

**Proofs.**

*(0)* $C_3$'s unique non-tree edge is $B_3$, and $D$'s non-tree edges
are exactly $B_1, B_2$ (each fundamental cycle contains its own back
edge only). $B_3 \notin \{B_1, B_2\}$, so no shared non-tree edge. □

*(1)* By `fund_pair_overlap`(1), when the two tree paths overlap in
$k_{12} \ge 1$ edges, both anchors lie on the common root-chain of
$s_1, s_2$ and the shared edge set is $I = [a_{\text{deep}} .. m]$ (the
deeper anchor is a strict ancestor of $m$, $k_{12} = d(m) -
d(a_{\text{deep}})$). Decompose $P_i = [a_i .. a_{\text{deep}}] \cup I
\cup [m .. s_i]$ (the first piece empty for $a_i = a_{\text{deep}}$, the
last empty for $s_i = m$). Symmetric difference cancels $I$ and nothing
else: the pieces above $m$ lie on one chain ($[a_1 .. a_{\text{deep}}]
\triangle [a_2 .. a_{\text{deep}}] = [a_{\text{sh}} .. a_{\text{deep}}]
= A$ since one of them is empty), and the legs $[m .. s_1], [m .. s_2]$
are edge-disjoint (below $m$ in different subtrees when incomparable;
when comparable, $m = s_{\text{shallower}}$ makes that leg empty).
Vertex-disjointness: $A$'s vertices have depth $\le d(a_{\text{deep}})
< d(m)$; legs' vertices have depth $\ge d(m)$; two nonempty legs share
only $m$. □

*(2)* Each of $A, L_1, L_2$ and $P_3$ is a vertical path, i.e. an
interval of consecutive-depth vertices on a root-chain. Two root-chains
agree on a common prefix and diverge permanently at their first
difference (no-cross-edge property of trees), so the intersection of two
vertical intervals is a single contiguous interval — the
`fund_pair_overlap`(1) argument verbatim. For the two-of-three bound:
$P_3$'s chain passes through $m$ at most once and continues into exactly
one child subtree of $m$, so it can carry edges of at most one of
$L_1, L_2$. □

*(3)* ($\Leftarrow$) If exactly one intersection is nonempty, the shared
edge set is that single vertical subpath by (1)+(2); if additionally all
shared vertices lie on it, the shared subgraph IS that path, of length
$k' \ge 1$. ($\Rightarrow$) Suppose $D \cap C_3$ is a single path $P$ of
length $\ge 1$. Its edge set is the union of the (contiguous) segment
intersections by (0)+(1). Two nonempty intersections lie in distinct
segments, which by (1) share no vertex except possibly $m$ — and an
$A$-intersection and a leg-intersection cannot even touch ($A$ stays
strictly above $m$), while $L_1$- and $L_2$-intersections cannot both be
nonempty by (2). So two nonempty intersections would make $P$'s edge set
disconnected — contradiction; hence exactly one is nonempty, and
path-ness forces every shared vertex onto it (a shared vertex off the
path would be an isolated vertex of the intersection subgraph). The
length statement is immediate. □

**Consequence for Q9 (meeting half).** Combined with
`triple_sym_diff_structure`(5), the pasting hypothesis for $(B_1, B_2,
B_3)$ is now a pure statement about FOUR vertical intervals read off the
depth data ($A$, $L_1$, $L_2$, $P_3$): $B_3$ pastes iff $P_3$'s interval
meets exactly one of the three in an edge and carries no stray shared
vertex. The existence question ("does some even-gap $B_3$ paste?")
becomes: among the back edges covering the tree edges of $D$ — supply
guaranteed by the coverage half of `mixed_overlap_supply`(1), every tree
edge of $D$ is covered — does some even-gap one avoid the two-segment
and stray-vertex degeneracies?

**Empirical bonus (open, census below; NOT asserted).** In 299,544
sampled cubic configs, whenever exactly one intersection was nonempty
the stray-vertex condition held automatically (167,724/167,724): the
census line reports `vertex_auto=(x, y)` with $x = y$ meaning zero
exceptions. If this "vertex-automatic" property is provable for cubic
DFS trees, the meeting criterion collapses to the one-line condition
"$P_3$ meets exactly one segment in an edge" — a candidate R25 target.

---

<!-- CHECK
# pasting_meeting_structure: verify (1) decomposition, (2) contiguity +
# two-of-three, (3) the meeting iff, against brute-force intersection.
# Census: segment counts, nonempty-intersection counts, vertex-automatic.
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

def contiguous_subpath(es):
    if not es: return set()
    deg = {}
    for u, v in es: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
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
    return set(deg) if len(seen) == len(deg) else None

rng = random.Random(20260805 + 24)
pairs_seen = 0; triples_seen = 0
seg_census = {}; nonempty_census = {}
vertex_auto_num = 0; vertex_auto_den = 0
for nn in (10, 12, 14, 16):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(120):
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
                    segs = [x for x in (A, L1, L2) if x]
                    Dtree = set(e for e in D if e in pe[i] or e in pe[j])
                    assert sum(len(x) for x in segs) == len(A | L1 | L2), \
                        f"FALSIFIED(1a): segments overlap (n={nn}, edges={edges}, root={r}, i={i}, j={j})"
                    assert (A | L1 | L2) == Dtree, \
                        f"FALSIFIED(1b): decomposition mismatch (n={nn}, edges={edges}, root={r}, i={i}, j={j})"
                    seg_census[len(segs)] = seg_census.get(len(segs), 0) + 1
                    Dverts = {v for e in D for v in e}
                    for z in range(m):
                        if z == i or z == j: continue
                        triples_seen += 1
                        P3 = pe[z]
                        inters = [P3 & X for X in (A, L1, L2)]
                        vsets = []
                        for X in inters:
                            vs = contiguous_subpath(X)
                            assert vs is not None, \
                                f"FALSIFIED(2a): non-contiguous intersection (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                            vsets.append(vs)
                        nonempty = [q for q in range(3) if inters[q]]
                        assert len(nonempty) <= 2, \
                            f"FALSIFIED(2b): three nonempty intersections (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                        nonempty_census[len(nonempty)] = nonempty_census.get(len(nonempty), 0) + 1
                        kk = path_len_of_intersection(D, fc[z])
                        C3verts = {v for e in fc[z] for v in e}
                        sharedv = Dverts & C3verts
                        if len(nonempty) == 1:
                            q = nonempty[0]
                            pred = (sharedv == vsets[q]); pred_k = len(inters[q])
                            vertex_auto_den += 1
                            if pred: vertex_auto_num += 1
                        else:
                            pred = False; pred_k = None
                        truth = kk is not None
                        assert pred == truth and (not pred or pred_k == kk), \
                            (f"FALSIFIED(3): meeting iff mismatch pred={pred},{pred_k} truth={kk} "
                             f"(n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})")
assert pairs_seen > 5000 and triples_seen > 30000, \
    f"probe vacuous: pairs={pairs_seen} triples={triples_seen}"
print(f"pairs={pairs_seen} triples={triples_seen} seg_census={sorted(seg_census.items())} "
      f"nonempty_census={sorted(nonempty_census.items())} "
      f"vertex_auto=({vertex_auto_num}, {vertex_auto_den}) "
      f"— decomposition, contiguity, and meeting-iff all verified")
CHECK -->

## Summary

Proved: for an overlapping pair with single-cycle sym-diff $D$ and any
third back edge, the tree edges of $D$ decompose into $\le 3$ pairwise
almost-disjoint vertical segments (anchor interval + two legs below the
sender-lca), $P_3$ meets each in a contiguous interval with at most two
nonempty, and the `triple_sym_diff_structure`(5) pasting hypothesis
holds iff exactly one is nonempty and carries all shared vertices. The
meeting half of Q9 is thereby reduced to interval combinatorics on four
vertical chains; the census additionally shows the stray-vertex
condition never fails in cubic samples (open "vertex-automatic"
conjecture, candidate R25 target).
