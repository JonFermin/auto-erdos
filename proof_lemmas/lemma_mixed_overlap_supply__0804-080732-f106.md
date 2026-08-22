---
id: mixed_overlap_supply
status: proved
depends_on: [fund_pair_overlap]
discharged_by_round: 22
introduced_at_round: 22
---

# Lemma `mixed_overlap_supply` (2-connected graphs admit no back-edge parity segregation)

**Setting.** $G$ a 2-connected simple graph on $n \ge 3$ vertices, $T$ a
DFS (Trémaux) spanning tree rooted at $r$; notation as in
`fund_pair_overlap`: back edge $B = (s, a)$ with $a \sqsubset s$, vertical
path $P_B = \operatorname{TreePath}(s, a)$, $\operatorname{gap}(B) =
d(s) - d(a) \ge 2$. Say $B$ **covers** a tree edge $e$ if $e \in P_B$, and
call a pair of back edges **overlapping** if their paths share a tree edge.

**Statement.**

1. **(No parity segregation.)** If the back-edge gap multiset contains
   both an odd and an even gap ("mixed-parity tree"), then some odd-gap
   back edge and some even-gap back edge overlap.
2. **(Supply corollary.)** Consequently, by `fund_pair_overlap`(2)+(4),
   every mixed-parity DFS tree of a 2-connected graph contains a mixed
   pair whose sym-diff $D = C_1 \triangle C_2$ is a single simple cycle of
   **odd** length — the raw material required by the $OEE$ pasting rescue
   route of `triple_sym_diff_structure`(6). The supply half of the Q9
   existence program is closed for 2-connected graphs.
3. **(Sharpness.)** 2-connectedness cannot be dropped: bridged
   compositions of a block whose DFS gaps are all odd with a block whose
   DFS gaps are all even give mixed-parity DFS trees of bridged
   (min-degree-3-preserving) graphs with no overlapping mixed pair, since
   no back-edge path crosses the bridge.

**Proof.**

Suppose, for contradiction, that $T$ is mixed-parity but no odd-gap back
edge overlaps an even-gap back edge ("segregation").

*Step 1 — every tree edge is covered, and gets a well-defined parity
color.* Let $e = (v, c)$ be a tree edge ($c$ a child of $v$). We use the
standard DFS facts for 2-connected graphs:

- **(a) The root has exactly one child.** If $r$ had children
  $c_1 \ne c_2$, then — since a DFS tree of an undirected graph has no
  cross edges — every non-tree edge joins an ancestor–descendant pair, so
  no edge joins the subtrees $T_{c_1}$ and $T_{c_2}$; every path between
  them passes through $r$, making $r$ a cut vertex, contradicting
  2-connectedness ($n \ge 3$).
- **(b) Low-point property.** For every non-root vertex $v$ and every
  child $c$ of $v$, some back edge $B$ has sender in $T_c$ and anchor a
  **strict** ancestor of $v$. Otherwise every edge leaving
  $T_c \cup \{v\}$ ends at $v$ (tree edge $(v,c)$, or back edges into
  $v$), so removing $v$ disconnects $T_c$ from
  $par(v) \ne \emptyset$ — a cut vertex, contradiction.

By (b) applied to $(v, c)$ when $v$ is non-root, the low-point back edge
covers $(v, c)$; when $v = r$, by (a) $c$ is the unique root child
$c_0$, and (b) applied to any child $c'$ of $c_0$ produces a back edge
from $T_{c'}$ with anchor $\sqsubset c_0$, i.e. anchor $= r$, whose path
passes through $c_0$ and covers $(r, c_0)$. (If $c_0$ has no children,
$n = 2$, excluded.) So every tree edge is covered by at least one back
edge. Under segregation, no tree edge is covered by back edges of both
parities — otherwise those two back edges would overlap at that edge. So
each tree edge $e$ has a well-defined color
$\chi(e) \in \{\text{odd}, \text{even}\}$, the common gap parity of all
back edges covering it.

*Step 2 — adjacent tree edges have equal colors.* Let $v$ be a non-root
vertex with parent edge $e_{\uparrow} = (par(v), v)$ and let $c$ be any
child of $v$, $e_{\downarrow} = (v, c)$. The low-point back edge $B$ of
(b) has sender $s \in T_c$ and anchor $a \sqsubset v$, so its vertical
path runs $s \to \cdots \to c \to v \to par(v) \to \cdots \to a$ and
covers **both** $e_{\downarrow}$ and $e_{\uparrow}$. Hence
$\chi(e_{\downarrow}) = \operatorname{par}(B) = \chi(e_{\uparrow})$.

Now take any two adjacent tree edges, sharing vertex $v$. If one is the
parent edge of $v$, the other is a child edge and Step 2 applies. If both
are child edges $(v, c_1), (v, c_2)$: if $v \ne r$ both equal
$\chi(e_{\uparrow})$ by Step 2; the case $v = r$ cannot occur by (a).
So $\chi$ is constant on each pair of adjacent edges of the connected
tree $T$, hence constant on all of $E(T)$.

*Step 3 — contradiction.* Every back edge $B$ has
$\operatorname{gap}(B) \ge 2 \ge 1$ (a gap-1 back edge would be parallel
to a tree edge in a simple graph — in fact gap $\ge 2$; all we need is
$P_B \ne \emptyset$), so $B$ covers some tree edge and
$\operatorname{par}(B) = \chi(\text{that edge})$ — the constant color.
So all back-edge gaps have one parity, contradicting mixed parity.
$\square$ (1)

(2) By (1) pick overlapping back edges $B_1$ (odd gap) and $B_2$ (even
gap); `fund_pair_overlap`(2) makes $C_1 \triangle C_2$ a single simple
cycle of length $\operatorname{gap}_1 + \operatorname{gap}_2 + 2 - 2k$,
odd by `fund_pair_overlap`(4). $\square$

(3) Construction sketch (not needed for (1)–(2); recorded for scope). Take
disjoint graphs $H_1, H_2$, each with a marked degree-2 vertex $w_i$ and
all other degrees $\ge 3$, and add the bridge $w_1 w_2$. A DFS started in
$H_1$ traverses $H_1 \cup \{w_1\}$, crosses the bridge once as a tree
edge, and traverses $H_2$; every back edge has both endpoints in the same
$H_i$ side (the bridge lies on no cycle), so no back-edge path contains
the bridge and no pair overlaps across it. If the two sides' DFS gaps
have pure opposite parities, the whole tree is mixed-parity with no
overlapping mixed pair. All-even-gap and (rarer) all-odd-gap DFS trees of
min-degree-3 blocks were both observed in the R18 census, so the
hypothesis class is nonempty. $\square$

**Remarks.**

- **(What remains of Q9 existence.)** Supply is now closed analytically
  for 2-connected graphs (random cubic graphs are a.a.s. 3-connected,
  matching the 777/777 R21 census; predominantly-cubic EGC candidate
  counterexamples per F3 are the relevant class, and any block
  decomposition confines cycles to blocks). The open core is **tuning**:
  over the available mixed pairs $(B_1, B_2)$ and third back edges $B_3$
  with $D \cap C_3$ a single path of length $k'$, show
  $\operatorname{gap}_1 + \operatorname{gap}_2 + \operatorname{gap}_3 + 3
  - 2(k_{12} + k')$ hits $\{4, 8, 16, 32\}$ in pair-residual trees.
- **(Scope note.)** No claim about the Erdős–Gyárfás conjecture itself is
  made: this lemma supplies odd single-cycle sym-diffs in mixed-parity
  DFS trees of 2-connected graphs; whether a power-of-2 cycle results
  depends on the (open) tuning step.

---

<!-- CHECK
# mixed_overlap_supply: falsification probe.
# On sampled cubic 2-connected DFS trees:
#  (a) root has exactly one child;
#  (b) low-point property: every non-root vertex's every child subtree
#      sends a back edge strictly above the vertex;
#  (c) every tree edge is covered by >= 1 back edge;
#  (d) THE CONCLUSION: every mixed-parity tree has an overlapping
#      odd/even pair (direct check, independent of the proof).
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

def two_connected(nn, edges):
    # brute force: connected after deleting any single vertex
    adj = [[] for _ in range(nn)]
    for a, b in edges: adj[a].append(b); adj[b].append(a)
    for x in range(nn):
        rest = [v for v in range(nn) if v != x]
        if not rest: continue
        seen = {rest[0]}; stk = [rest[0]]
        while stk:
            u = stk.pop()
            for w in adj[u]:
                if w != x and w not in seen: seen.add(w); stk.append(w)
        if len(seen) != nn - 1: return False
    return True

def is_anc(u, v, depth, par):
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
            if not is_anc(a, b, depth, par): return None
            nontree.append((b, a, depth[b] - depth[a]))
    return depth, par, nontree

def path_edges(sender, ancestor, par):
    path = set(); u = sender
    while u != ancestor:
        p = par[u]; path.add((min(u, p), max(u, p))); u = p
    return path

rng = random.Random(20260804 + 22)
trees = 0
mixed_trees = 0
mixed_with_overlap = 0
lowpoint_checked = 0
edges_covered_checked = 0

for nn in (10, 12, 14, 16, 18):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(40):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        if not two_connected(nn, edges): continue
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(4):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            depth, par, be = res
            trees += 1
            # (a) root has exactly one child
            root_children = [v for v in range(nn) if par[v] == r]
            assert len(root_children) == 1, \
                f"2-connected DFS root with {len(root_children)} children"
            # (b) low-point property
            children = [[] for _ in range(nn)]
            for v in range(nn):
                if par[v] >= 0: children[par[v]].append(v)
            for v in range(nn):
                if v == r: continue
                for c in children[v]:
                    # subtree of c
                    sub = {c}; stk = [c]
                    while stk:
                        u = stk.pop()
                        for w in children[u]: sub.add(w); stk.append(w)
                    ok = any(s in sub and depth[a] < depth[v] for s, a, _ in be)
                    assert ok, f"low-point fails at v={v} child={c}"
                    lowpoint_checked += 1
            # (c) every tree edge covered
            cover = {}
            paths = []
            for s, a, g in be:
                pe = path_edges(s, a, par)
                paths.append((pe, g % 2))
                for e in pe: cover.setdefault(e, set()).add(g % 2)
            for v in range(nn):
                if v == r: continue
                e = (min(v, par[v]), max(v, par[v]))
                assert e in cover, f"uncovered tree edge {e}"
                edges_covered_checked += 1
            # (d) the conclusion
            gaps = [g for _, _, g in be]
            if any(g % 2 for g in gaps) and any(g % 2 == 0 for g in gaps):
                mixed_trees += 1
                # overlap exists iff some tree edge is covered by both parities
                # (that IS the overlap witness), verify equivalently via pairs
                both = any(len(ps) == 2 for ps in cover.values())
                pair_overlap = any(
                    p1 & p2 and par1 != par2
                    for i, (p1, par1) in enumerate(paths)
                    for (p2, par2) in paths[i + 1:])
                assert both == pair_overlap, "cover/pair overlap mismatch"
                assert pair_overlap, \
                    "MIXED TREE WITH NO OVERLAPPING MIXED PAIR — lemma falsified"
                mixed_with_overlap += 1

assert trees > 200, f"too few trees: {trees}"
assert mixed_trees > 100, f"too few mixed trees: {mixed_trees}"
print(f"trees={trees} mixed={mixed_trees} mixed_with_overlap={mixed_with_overlap} "
      f"lowpoint_checks={lowpoint_checked} coverage_checks={edges_covered_checked} "
      f"— root/lowpoint/coverage/conclusion all hold")
CHECK -->

## Summary

Proved (elementary, unconditional): in a DFS tree of a 2-connected simple
graph, back-edge parity segregation is impossible — if both odd and even
gaps occur, an odd-gap and an even-gap back edge must share a tree edge.
Proof: 2-connectedness forces every tree edge to be covered (low-point
property, one-child root); a segregated coloring of tree edges by covering
parity would be locally constant across adjacent edges (the low-point back
edge over each vertex covers both its parent and child edges) hence
globally constant, contradicting mixed parity. With `fund_pair_overlap`
this closes the supply half of the Q9 pasting-existence program for
2-connected graphs: mixed-parity trees always contain a mixed pair with
odd single-cycle sym-diff. 2-connectedness is sharp (bridged
compositions). The open core is now the tuning step only.
