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

**Next step for proof.** Identify why (2) is always achievable when (1) fails:
- When no fundamental cycle has power-of-2 length, the DFS leaf must carry
  $\ge 2$ back edges.
- Their tree paths to ancestors overlap in a shared suffix; the sym-diff
  cycle length is $\delta_1 + \delta_2 - 2\ell + 2$.
- A depth/divisibility argument should force some choice of back-edge pair
  and overlap length to achieve a power-of-2 sum.

**Current obstacle.** The divisibility step is non-trivial: $\delta_1 +
\delta_2 - 2\ell + 2 = 2^k$ can be read as $(\delta_1 - \ell) + (\delta_2 -
\ell) = 2^k - 2$, i.e., two non-negative integers summing to $2^k - 2$.
We need to show that for at least one DFS leaf with $\ge 2$ back edges,
some pair satisfies this. A pigeonhole or parity argument may work; see
next session.

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

assert tested >= 5, f"Only {tested} graphs checked"
CHECK -->
