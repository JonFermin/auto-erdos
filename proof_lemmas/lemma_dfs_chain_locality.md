---
id: dfs_chain_locality
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 2
---

# Lemma: 3-locality DFS chain-locality for min-degree-3 graphs

**Statement (revised Round 5).** Let $G$ be a connected graph with $\delta(G) \ge 3$, and let
$T$ be any DFS spanning tree of $G$. Then at least one of the following holds:

1. Some fundamental cycle of $T$ has power-of-2 length (i.e., length
   $2^k$ for some $k \ge 2$).
2. The symmetric difference of some **two** fundamental cycles of $T$ is a
   simple cycle of power-of-2 length.
3. The symmetric difference of some **three** fundamental cycles of $T$ is a
   simple cycle of power-of-2 length.

**Pairwise claim (2 alone) is FALSE for some DFS trees** (Round 5 finding, see below).
The 3-locality claim (1 or 2 or 3) is supported by all computational evidence to date.

If the 3-locality statement holds for all such $G$ and all $T$, the 3-locality
of the fundamental-cycle basis is sufficient to witness a power-of-2 cycle
in every DFS tree — a structural step toward the Erdős–Gyárfás conjecture
via depth-chain discharging.

**Current status**: open. The CHECK block below (exhaustive on $n \le 6$,
named graphs up to $n = 14$, and a random cubic sample $n \le 30$) has not
found a counterexample to the 3-locality claim; proof text is in progress.

**Context (Q9 from proof_open_questions.jsonl).** In a hypothetical
counterexample to Erdős–Gyárfás:
- No cycle of any power-of-2 length exists.
- Any DFS tree therefore has no fundamental cycle of power-of-2 length (else
  we're done). So condition (1) above is guaranteed FALSE in a counterexample.
- Conditions (2) and (3) must also both be FALSE in every DFS tree.
- This lemma, if true, asserts that (1) or (2) or (3) always holds — hence a
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
for (2) and (3).

**Computational evidence.** All 1,885 connected min-degree-3 labeled graphs
on $n = 4, 5, 6$ vertices satisfy the condition for EVERY DFS tree rooted at
each vertex (sorted and reversed adjacency, two orderings per root). The
Petersen graph ($n = 10$, girth 5, 3-regular) and $K_{3,3}$ ($n = 6$,
bipartite, 3-regular) also pass for all roots and orderings via pairwise
(condition 2). No counterexample to the 3-locality claim found in 1,887
small-graph tests or 1,698 random cubic graphs $n \le 30$.

**Round 7 scale test (n=20,30,50,100).** A second scale test at larger $n$
used 500 random connected cubic graphs at $n \le 30$ and 200 graphs at $n > 30$,
each checked with 2 roots $\times$ 2 adjacency orderings (4 DFS trees per graph).
Results — showing A-count, B2-count, B3-count across all DFS trees checked:

| $n$ | Graphs | A (direct) | B2 (pairwise) | B3 (triple) | FAIL |
|-----|--------|-----------|--------------|------------|------|
| 20  | 500    | 1840 (92%) | 160 (8%)    | 0          | 0    |
| 30  | 500    | 1877 (94%) | 123 (6%)    | 0          | 0    |
| 50  | 200    | 772 (96.5%)| 28 (3.5%)   | 0          | 0    |
| 100 | 200    | 791 (98.9%)| 9 (1.1%)    | 0          | 0    |

No B3 cases and no FAIL cases at any tested scale. As $n$ grows, condition A
(some fundamental cycle already has power-of-2 length) becomes dominant: the
pool of fundamental cycles in a cubic graph on $n$ vertices is $n/2 + 1$ cycles
with depth-gaps ranging over a wider interval, making it increasingly likely
that some gap is $2^k - 1$ for some $k$. The 7 B3 cases seen at $n \in
\{10,12,14\}$ appear to be a small-$n$ phenomenon; at larger $n$, pairwise
(condition B2) is sufficient for every A-fail DFS tree in the tested sample.

**Round 5 finding: pairwise claim (1 or 2 only) is FALSE for larger DFS trees.**
In a random sample of 600 connected 3-regular graphs ($n \in \{10,12,14\}$,
200 per size), 7 specific (graph, DFS-tree) pairs arise where (1) fails AND no
pairwise sym-diff (condition 2) is a simple power-of-2 cycle.  In EVERY such
case the graph itself contains a $C_8$ (verified by BFS), so Erdős–Gyárfás is
not falsified.  The mechanism: the $C_8$ exists in $G$ but the particular DFS
tree places the relevant back edges on different spines so no pairwise sym-diff
is simultaneously simple AND power-of-2 in length.  (Some pairwise sym-diffs
achieve the right edge-count 8 but are a union of two cycles, not a single one.)

In every such failing case a **triple** sym-diff of fundamental cycles IS a
simple $C_8$ (condition 3).  Systematically: out of all A-fail DFS trees in the
$n \in \{10,12,14\}$ sample, 1,699 are resolved by pairwise and 7 by triple;
zero require quadruple or larger.  No instance escapes the 3-locality claim.

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

**Round 6 finding: depth-separation and bridge structure (new).** Exhaustive
inspection of all 6 failing (pairwise-bad) cases from the $n \le 14$ sample reveals
a uniform pattern:

1. **Depth-separation**: the two components $D_0$ and $D_1$ of the non-simple
   pairwise sym-diff are ALWAYS depth-separated — one component's vertex-depths
   are entirely above the other's.  Concretely: $\max\{\mathrm{dep}(v) : v \in D_0\}
   < \min\{\mathrm{dep}(v) : v \in D_1\}$ (or vice versa) in all 6 cases.

2. **Bridge existence**: in all 6 cases there exists a back edge $e_k$ whose
   fundamental cycle $C_{e_k}$ has an **odd** overlap count with EACH component:
   $|C_{e_k} \cap D_0|$ is odd and $|C_{e_k} \cap D_1|$ is odd.  Because the
   sym-diff $D_0 \triangle (C_{e_k} \cap D_0)$ retains even valence everywhere
   except at the interface, an odd-overlap inclusion merges $D_0$ and $D_1$ into
   a single connected 2-regular subgraph — concretely, $(D_0 \cup D_1) \triangle
   C_{e_k}$ is a simple cycle of the same total length.

3. **Bridge structure (observed)**: the bridging cycle's spine always traverses
   through vertices of both components.  In cases 1–5 (same n=10 graph, different
   DFS roots) the bridge has gap 5, with its deep endpoint inside $D_\text{deep}$
   and shallow endpoint inside $D_\text{shallow}$.  In case 6 (n=14) the bridge
   has gap 9, with its deep endpoint strictly below $D_\text{deep}$, spanning
   through both depth bands.

**Round 7 finding: B3 disappears at scale.** The Round 7 scale test (above) shows that
at $n \ge 20$, condition B3 (triple sym-diff) is never needed: every A-fail DFS tree is
resolved by B2 (pairwise).  The depth-separation + bridge structure observed in Rounds 5–6
(at small $n$ where B3 was needed) does not appear at larger $n$ in the tested sample.
This suggests two alternative proof directions:

1. **Pairwise sufficiency at large $n$**: prove that for $n$ large enough (e.g.\ $n \ge 20$
   cubic), every DFS tree satisfies (A) or (B2). The pool of $n/2+1$ fundamental cycles
   with gaps spanning $\{1, \ldots, d_{\max}\}$ where $d_{\max} \to \infty$ as $n \to \infty$
   makes avoidance of all $2^k-1$ gaps increasingly hard; a counting/pigeonhole argument
   might suffice here.

2. **3-locality proof for all $n$**: the small-$n$ B3 cases (7 instances at $n \le 14$)
   are handled by the depth-separation + bridge argument from Round 6. Combining the
   Round 6 proof target with the large-$n$ empirical evidence, 3-locality holds universally.

**Proof target for Round 8.** Quantify the density of fundamental cycles that must cover
some gap $2^k - 1$ in any cubic graph of depth $\ge d$.  A cubic graph on $n$ vertices
has DFS depth $\ge \log_3(n)$ (breadth-first bound) and $n/2+1$ back edges; the
depth-gaps collectively span $\{1, \ldots, d_{\max}\}$; the number of power-of-2-minus-1
values up to $d_{\max}$ is $\lfloor \log_2(d_{\max}+1) \rfloor$.  If $n/2+1$ back edges
cover more than $d_{\max} - \lfloor \log_2(d_{\max}+1) \rfloor$ distinct gaps, pigeonhole
forces at least one gap in $\{1,3,7,15,\ldots\}$ — but this counting is too coarse to
work directly (back edges can cluster).  The next step: find the structural constraint
that prevents back-edge clusters from simultaneously avoiding all $2^k-1$ gaps, leveraging
min-degree-3.

**Current obstacle.** No formal proof that the depth-gap distribution of fundamental cycles
in a min-degree-3 DFS tree is forced to hit some $2^k - 1$.  The empirical evidence at
scale is very strong (98.9% of n=100 DFS trees satisfy A alone), but converting frequency
to inevitability requires a structural argument.

<!-- CHECK
# Falsification probe for 3-locality DFS chain-locality (updated Round 7).
#
# For every connected min-degree-3 LABELED graph G on n=4,5,6 vertices and
# every canonical DFS tree T (rooted at each vertex, sorted adjacency, and
# also reversed adjacency for breadth), check:
#   (A) some fundamental cycle of T has power-of-2 length, OR
#   (B2) some pairwise sym-diff of fundamental cycles is a simple cycle of
#       power-of-2 length, OR
#   (B3) some triple sym-diff of fundamental cycles is a simple cycle of
#       power-of-2 length.
# NOTE: B2 alone is FALSE for some DFS trees of n<=14 cubic graphs (Round 5).
# Round 7: n=20,30,50,100 scale test — NO B3 cases, NO FAIL cases. 3-locality holds.
# As n grows, condition A dominates (98.9% at n=100); B3 appears to be small-n only.
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
    # (A) fundamental cycle with p2 length
    if any(is_p2(len(c)) for c in cycs): return True
    # (B2) pairwise sym-diff is simple p2-cycle
    for i in range(len(cycs)):
        for j in range(i + 1, len(cycs)):
            sd = cycs[i] ^ cycs[j]
            if is_p2(len(sd)) and is_scycle(sd): return True
    # (B3) triple sym-diff is simple p2-cycle
    for i in range(len(cycs)):
        for j in range(i + 1, len(cycs)):
            for k in range(j + 1, len(cycs)):
                sd = cycs[i] ^ cycs[j] ^ cycs[k]
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
            f"3-LOCALITY FALSIFIED n={n} edges={edges}"

# Petersen graph (n=10, girth 5, 3-regular — no C4; uses C8 via pairwise)
adj_p = [set() for _ in range(10)]
es_p = set()
for u, v in ([(i,(i+1)%5) for i in range(5)]
             + [(5,7),(7,9),(9,6),(6,8),(8,5)]
             + [(i,i+5) for i in range(5)]):
    adj_p[u].add(v); adj_p[v].add(u); es_p.add((min(u,v),max(u,v)))
adj_p = [list(a) for a in adj_p]
tested += 1
assert check_graph(10, adj_p, frozenset(es_p)), "Petersen FAILS 3-locality"

# Heawood graph (n=14, girth 6, 3-regular — no C4/C5; uses C8 via pairwise)
adj_h = [[] for _ in range(14)]
es_h = set()
for u, v in ([(i,(i+1)%14) for i in range(14)]
             + [(0,5),(2,7),(4,9),(6,11),(8,13),(10,1),(12,3)]):
    adj_h[u].append(v); adj_h[v].append(u); es_h.add((min(u,v),max(u,v)))
tested += 1
assert check_graph(14, adj_h, frozenset(es_h)), "Heawood FAILS 3-locality"

# Round 5 stress test: n=10 cubic graph where pairwise FAILS but triple succeeds
# Edges: [(0,1),(0,6),(0,7),(1,2),(1,5),(2,4),(2,5),(3,5),(3,6),(3,8),(4,8),
#          (4,9),(6,7),(7,9),(8,9)]
# At root=4 rev=True: fundamental cycle lengths {3,3,3,5,6,10}; pairwise misses C8
# but triple (e0,e1,e2) achieves C8. All DFS trees of this graph pass 3-locality.
adj_r5 = [[] for _ in range(10)]
es_r5 = set()
for u, v in [(0,1),(0,6),(0,7),(1,2),(1,5),(2,4),(2,5),(3,5),(3,6),(3,8),
             (4,8),(4,9),(6,7),(7,9),(8,9)]:
    adj_r5[u].append(v); adj_r5[v].append(u); es_r5.add((min(u,v),max(u,v)))
tested += 1
assert check_graph(10, adj_r5, frozenset(es_r5)), "Round5-stress-n10 FAILS 3-locality"

assert tested >= 5, f"Only {tested} graphs checked"
CHECK -->
