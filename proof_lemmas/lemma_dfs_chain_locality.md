---
id: dfs_chain_locality
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 2
---

# Lemma: pairwise DFS chain-locality for min-degree-3 graphs

**Statement.** Let $G$ be a connected graph with $\delta(G) \ge 3$, and let
$T$ be any DFS spanning tree of $G$. Then at least one of the following holds:

1. Some fundamental cycle of $T$ has power-of-2 length (i.e., length
   $2^k$ for some $k \ge 2$).
2. The symmetric difference of some two fundamental cycles of $T$ is a
   simple cycle of power-of-2 length.

If the statement holds for all such $G$ and all $T$, the pairwise locality
of the fundamental-cycle basis is sufficient to witness a power-of-2 cycle
in every DFS tree — a structural step toward the Erdős–Gyárfás conjecture
via depth-chain discharging.

**Current status**: open. The CHECK block below (exhaustive on $n \le 6$,
and targeted named graphs up to $n = 10$) has not found a counterexample;
proof text is in progress.

**Context (Q9 from proof_open_questions.jsonl).** In a hypothetical
counterexample to Erdős–Gyárfás:
- No cycle of any power-of-2 length exists.
- Any DFS tree therefore has no fundamental cycle of power-of-2 length (else
  we're done). So condition (1) above is guaranteed FALSE in a counterexample.
- Condition (2) then must also be FALSE in every DFS tree of a counterexample.
- This lemma, if true, asserts that (1) or (2) always holds — hence a
  counterexample cannot exist, which would prove the conjecture.

The "depth-chain" connection: back edges in a DFS tree have depth-gaps
$\delta = \mathrm{depth}(u) - \mathrm{depth}(v)$ for a back edge $(u,v)$.
Fundamental cycle length equals $\delta + 1$. For (1) to produce a
$2^k$-cycle, we need a back edge with $\delta = 2^k - 1$. For (2), two
back edges with gaps $\delta_1, \delta_2$ and shared tree-path prefix of
length $\ell$ produce a sym-diff cycle of length
$(\delta_1 + 1) + (\delta_2 + 1) - 2\ell = 2^k$ when the parameters align.
Min-degree-3 forces DFS leaves to carry $\ge 2$ back edges (all three
incident edges of a DFS leaf go to ancestors), creating the raw material
for (2).

**Computational evidence.** All 1,885 connected min-degree-3 labeled graphs
on $n = 4, 5, 6$ vertices satisfy the condition for EVERY DFS tree rooted at
each vertex (sorted and reversed adjacency, two orderings per root). The
Petersen graph ($n = 10$, girth 5, 3-regular) and $K_{3,3}$ ($n = 6$,
bipartite, 3-regular) also pass for all roots and orderings. No
counterexample found in 1,887 graphs tested.

**Spine-pair condition (when is the sym-diff a simple cycle?).** For back edges
$e_1 = (u_1, v_1)$ and $e_2 = (u_2, v_2)$ with $d_{u_i} > d_{v_i}$ and $d_{u_1} \ge
d_{u_2}$ (wlog), the symmetric difference $C_{e_1} \triangle C_{e_2}$ is a simple
cycle if and only if all four vertices lie on one root-to-vertex path and the depth
intervals $[d_{v_1}, d_{u_1}]$ and $[d_{v_2}, d_{u_2}]$ overlap (share $\ge 1$ tree
edge).  There are two structural sub-cases, both giving
$$|C_{e_1} \triangle C_{e_2}| = |d_{u_1} - d_{u_2}| + |d_{v_1} - d_{v_2}| + 2.$$

- *Nested* ($d_{v_1} \le d_{v_2}$, so $d_{v_1} \le d_{v_2} \le d_{u_2} \le d_{u_1}$):
  interval of $e_2$ sits inside interval of $e_1$.  Setting $a = d_{u_1} - d_{u_2} \ge 0$
  and $b = d_{v_2} - d_{v_1} \ge 0$: $\text{sd\_len} = a+b+2$ and
  $\delta_1 - \delta_2 = a+b$ (gap difference equals $a+b$).
  Special cases: *same-deep* ($u_1 = u_2$, $a = 0$); *same-shallow* ($v_1 = v_2$, $b = 0$).

- *Crossing* ($d_{v_1} > d_{v_2}$, so $d_{v_2} < d_{v_1} < d_{u_2} < d_{u_1}$):
  the two intervals overlap in $[d_{v_1}, d_{u_2}]$ but neither contains the other.
  Setting $A = d_{u_1} - d_{u_2} \ge 1$ and $B = d_{v_1} - d_{v_2} \ge 1$:
  $\text{sd\_len} = A+B+2$ and $\delta_1 - \delta_2 = A - B$ (gap difference can be
  zero when $A = B$, i.e.\ the two back edges have the **same gap**).  The minimal
  case $A = B = 1$ (adjacent spine vertices with the same-gap back edges) gives
  $\text{sd\_len} = 4$ with $\delta_1 = \delta_2$.

Condition (2) requires $|d_{u_1}-d_{u_2}| + |d_{v_1}-d_{v_2}| = 2^k - 2$ for some
$k \ge 2$.  For $k=2$ (a $C_4$ sym-diff): either two nested back edges with gap
difference 2, or two crossing back edges with $A = B = 1$ (same gap, adjacent spine
positions).

**Diagnostic (n=4..6, 1,174 DFS-tree instances where (A) fails, Round 3--4).**
- Gap sets appearing: $\{2,4\}$ (310 cases), $\{2,4,5\}$ (852), $\{2,5\}$ (12).
- Every satisfying pair for (B) has $\text{sd\_len} = 4$ ($C_4$, $k=2$).
  Of 1,174 satisfying pairs: 800 are nested ($|\delta_1 - \delta_2| = 2$, i.e.\
  gap difference 2), and 374 are crossing ($A = B = 1$, same gap, adjacent spine).
- Same-leaf analysis fails: leaves with ancestor depths $\{0,1,4\}$ have no
  same-deep $C_4$ (depth-differences 1, 3, 4 — none equal 2).  The 374 crossing
  pairs use a different mechanism: parent of the leaf carries the same-gap back edge.

**Crossing-pair structural observation.** For a DFS leaf $\ell$ with a back edge of
gap $g$ (to ancestor at depth $d_\ell - g$), if the parent $p = \mathrm{par}(\ell)$
also has a back edge of the **same gap** $g$ (to depth $d_p - g = d_\ell - g - 1$):
the pair $\{e_\ell, e_p\}$ is a crossing pair with $A = B = 1$, and their sym-diff
is a $C_4$.  The min-degree constraint forces $p$ to have $\ge 1$ back edge (since
$p$ has 2 tree edges — to $\ell$ and to $\mathrm{par}(p)$ — so needs $\ge 1$ more
to reach degree 3).

**Next step for proof.** Show that in every min-degree-3 DFS tree where (A) fails,
SOME spine pair $(e_1, e_2)$ achieves $|d_{u_1}-d_{u_2}| + |d_{v_1}-d_{v_2}| =
2^k-2$.  The key cases to unify:
(i) Some leaf has two back edges whose gaps differ by 2 (nested $C_4$).
(ii) Some consecutive spine pair $(w, \mathrm{child}(w))$ shares a back-edge gap
    (crossing $C_4$).
(iii) When neither holds for $C_4$, back-edge gaps lie in $\{g : g \equiv 0
    \pmod{4}\} \cup \{5, 9, 13, \ldots\}$ with no same-gap adjacent pair; then
    gap-difference 6 or 14 should be forced by the density of back edges, giving
    $C_8$ or $C_{16}$.

**Current obstacle.** No single argument covers all three cases simultaneously.  The
antichain $\{4, 8, 12, 16\}$ (gaps all $\equiv 0 \pmod 4$, no pair with difference
in $\{2, 6, 14\}$) shows that same-spine gap analysis alone is insufficient without
also using the parent's back edges.  A full proof must integrate the global spine
structure: track gap multisets along the root-to-leaf path and show that the
forbidden-gap constraint $(\delta \notin \{3,7,15,\ldots\})$ combined with
$\delta(G) \ge 3$ always forces at least one of (i), (ii), (iii) above.

<!-- CHECK
# Falsification probe for pairwise DFS chain-locality.
#
# For every connected min-degree-3 LABELED graph G on n=4,5,6 vertices and
# every canonical DFS tree T (rooted at each vertex, sorted adjacency, and
# also reversed adjacency for breadth), check:
#   (A) some fundamental cycle of T has power-of-2 length, OR
#   (B) some pairwise sym-diff of fundamental cycles is a simple cycle of
#       power-of-2 length.
# A failing instance would falsify the lemma.
import sys
from itertools import combinations
from collections import defaultdict
sys.setrecursionlimit(10000)

def is_p2(n):
    return n >= 4 and not (n & (n - 1))

def dfs_info(adj_s, n, root):
    par = [-1] * n
    dep = [-1] * n
    dep[root] = 0
    stk = [(root, 0)]
    while stk:
        v, i = stk[-1]
        if i == len(adj_s[v]):
            stk.pop(); continue
        w = adj_s[v][i]
        stk[-1] = (v, i + 1)
        if dep[w] < 0:
            par[w] = v; dep[w] = dep[v] + 1; stk.append((w, 0))
    return par, dep

def fund_cyc_set(edges_norm, par, dep, n):
    tree = {(min(v, par[v]), max(v, par[v])) for v in range(n) if par[v] >= 0}
    cycs = []
    for e in edges_norm:
        if e in tree: continue
        u, v = e
        a, b = (u, v) if dep[u] >= dep[v] else (v, u)
        c = {e}
        cur = a
        while cur != b:
            p = par[cur]; c.add((min(cur, p), max(cur, p))); cur = p
        cycs.append(frozenset(c))
    return cycs

def is_scycle(fs):
    if len(fs) < 3: return False
    dg = defaultdict(int); nb = defaultdict(list)
    for u, v in fs:
        dg[u] += 1; dg[v] += 1; nb[u].append(v); nb[v].append(u)
    if any(d != 2 for d in dg.values()): return False
    vs = set(dg); vis = set(); stk = [next(iter(vs))]
    while stk:
        x = stk.pop()
        if x in vis: continue
        vis.add(x)
        for y in nb[x]:
            if y not in vis: stk.append(y)
    return vis == vs

def chain_locality_ok(cycs):
    if any(is_p2(len(c)) for c in cycs): return True
    for i in range(len(cycs)):
        for j in range(i + 1, len(cycs)):
            sd = cycs[i] ^ cycs[j]
            if is_p2(len(sd)) and is_scycle(sd): return True
    return False

def check_graph(n, adj, edges_norm):
    for rev in (False, True):
        adj_s = [sorted(a, reverse=rev) for a in adj]
        for root in range(n):
            par, dep = dfs_info(adj_s, n, root)
            if any(dep[v] < 0 for v in range(n)): continue
            cycs = fund_cyc_set(edges_norm, par, dep, n)
            if not chain_locality_ok(cycs):
                return False
    return True

tested = 0
for n in range(4, 7):
    pairs = list(combinations(range(n), 2))
    ne = len(pairs)
    for mask in range(1 << ne):
        edges = [pairs[i] for i in range(ne) if (mask >> i) & 1]
        adj = [[] for _ in range(n)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        if any(len(adj[v]) < 3 for v in range(n)): continue
        vis = bytearray(n); stk = [0]; vis[0] = 1; cnt = 1
        while stk:
            x = stk.pop()
            for y in adj[x]:
                if not vis[y]: vis[y] = 1; cnt += 1; stk.append(y)
        if cnt < n: continue
        tested += 1
        edges_norm = frozenset((min(u,v), max(u,v)) for u, v in edges)
        assert check_graph(n, adj, edges_norm), \
            f"CHAIN-LOCALITY FALSIFIED n={n} edges={edges}"

# Petersen graph (n=10, girth 5, 3-regular — girth-5 so no C4, must use C8)
adj_p = [set() for _ in range(10)]
es_p = set()
for u, v in ([(i,(i+1)%5) for i in range(5)]
             + [(5,7),(7,9),(9,6),(6,8),(8,5)]
             + [(i,i+5) for i in range(5)]):
    adj_p[u].add(v); adj_p[v].add(u); es_p.add((min(u,v),max(u,v)))
adj_p = [list(a) for a in adj_p]
tested += 1
assert check_graph(10, adj_p, frozenset(es_p)), "Petersen FAILS chain-locality"

# Heawood graph (n=14, girth 6, 3-regular — girth 6 so no C4/C5;
#   any power-of-2 sym-diff must achieve C8 or longer from a nested pair)
adj_h = [[] for _ in range(14)]
es_h = set()
for u, v in ([(i,(i+1)%14) for i in range(14)]          # outer 14-cycle
             + [(0,5),(2,7),(4,9),(6,11),(8,13),(10,1),(12,3)]):  # chords
    adj_h[u].append(v); adj_h[v].append(u); es_h.add((min(u,v),max(u,v)))
tested += 1
assert check_graph(14, adj_h, frozenset(es_h)), "Heawood FAILS chain-locality"

assert tested >= 5, f"Only {tested} graphs checked"
CHECK -->
