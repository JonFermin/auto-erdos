---
id: backedge_density
status: open
depends_on: [sym_diff_nested]
discharged_by_round: null
introduced_at_round: 7
---

# Lemma: back-edge density and forced same-branch pairs

**Goal.** Show that in any DFS tree $T$ of a connected min-degree-$3$ graph
$G$ on $n$ vertices, there are sufficiently many back edges — and sufficiently
many same-branch pairs — that the unified forbidden-gap system cannot be
satisfied in a counterexample.

## Part A (proved): back-edge count

**Claim A.** A connected simple graph $G$ with min-degree $\delta(G) \ge 3$
and $n$ vertices has at least $\lfloor n/2 \rfloor + 1$ back edges in any DFS
tree.

**Proof.** $|E(G)| \ge \lceil 3n/2 \rceil$ (handshaking, min-deg 3). A DFS
tree on $n$ vertices has exactly $n-1$ tree edges. So the number of back
edges is $|E(G)| - (n-1) \ge \lceil 3n/2 \rceil - n + 1 = \lfloor n/2 \rfloor
+ 1$. $\square$

## Part B (proved): DFS leaves and forced same-branch constraint

**Claim B.** Every DFS leaf $v$ of a min-degree-$3$ graph has at least $2$
back edges. Each pair of back edges from the same leaf is a same-branch pair
(the back edges both attach to ancestors of $v$, hence lie on the same
root-to-$v$ path). The unified sym-diff theorem applies: for each pair
$(\delta_1, \delta_2)$ with $\delta_1 > \delta_2$, the constraints
$\delta_i \notin \{3,7,15,\ldots\}$ and $\delta_1 - \delta_2 \notin \{2,6,14,\ldots\}$
must hold simultaneously.

**Proof.** $v$ is a DFS leaf so it has no tree children; its only tree edge
is the parent edge. With $\deg(v) \ge 3$, at least $2$ edges are back edges
(or forward/cross in directed DFS — but in undirected DFS all non-tree edges
are back edges). $\square$

## Part C (open): forcing a valid-pair absence

**Goal.** Show that in a counterexample on $n \le 64$ vertices (witness cap),
the forbidden system cannot be satisfied at all DFS leaves simultaneously.

**Current state.** Valid gap pairs $(\delta_2, \delta_1)$ satisfying
$\delta_i \notin \{3,7,15\}$ and $\delta_1-\delta_2 \notin \{2,6,14\}$
exist for small values: $(1,4), (1,5), (2,4), (2,5), (4,9), (4,10), \ldots$.
The smallest valid gap is $\delta = 1$ (back edge to grandparent, cycle
length 2 — but wait, $2 = 2^1$ is a power of 2! So $\delta = 1$ gives cycle
length 2, which cannot appear in a simple graph). So $\delta \ge 2$ is forced.

**Corrected forbidden set.** The individual constraint must exclude
$\delta + 1 \in \{4, 8, 16, 32, \ldots\}$ (cycle lengths that are powers of 2,
$\ge 4$), so $\delta \notin \{3, 7, 15, 31, \ldots\}$. Cycle length 2 cannot
occur in a simple graph. So the effective constraint is only on $\delta$
values that would produce cycles of length $4, 8, 16, 32$. Cycles of length
$2$ and $1$ don't exist in simple graphs.

**Small valid pairs with $\delta \ge 2$:**
- $(\delta_2, \delta_1) = (2, 4)$: $\delta_1 - \delta_2 = 2 \in \{2,6,14,\ldots\}$. FORBIDDEN by sym-diff constraint.
- $(2, 5)$: gaps 2 and 5 are both OK individually; diff $= 3$ not in $\{2,6,14\}$. VALID.
- $(4, 5)$: both OK individually; diff $= 1$ not forbidden. VALID.
- $(2, 6)$: $\delta_2 = 2$ OK; $\delta_1 = 6$ OK; diff $= 4 \notin \{2,6,14\}$. VALID.

So valid pairs with $\delta_2 \ge 2$ exist. The counting argument alone does
not close the gap. We would need to show that at some DFS leaf $v$, the
available gap values are restricted by the DFS tree structure to produce only
pairs that are forbidden.

**Structural obstacle.** A back edge from $v$ to its grandparent has $\delta = 1$,
giving a $C_2$ — impossible. So the minimum $\delta$ for any back edge is $2$
(triangle: $v$, parent($v$), grandparent($v$), $v$). But a triangle gives
cycle length 3, not a power of 2. So valid configurations do exist.

**Possible closing argument (open).** The constraints form a forbidden
integer set for depth-gap pairs. If one could show the forbidden set is
*density-1* (almost all pairs are forbidden) for some range, and that
DFS trees of min-degree-3 graphs force back-edge gaps to be DENSE in some
range (not all gap values occur: a range where valid gaps thin out), then
the argument might close. This is the direction for future rounds.

<!-- CHECK
# Verify Part A: back-edge count lower bound.
# Check that for small random graphs, back_edges >= floor(n/2) + 1.

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

# Exhaustive n=4..6: check back-edge count for every graph
pairs_by_n = {}
for n in (4, 5, 6):
    pairs_by_n[n] = [(i, j) for i in range(n) for j in range(i + 1, n)]

violations = 0
checked = 0
for n in (4, 5, 6):
    pairs = pairs_by_n[n]
    np2 = len(pairs)
    for mask in range(1 << np2):
        edges = [pairs[k] for k in range(np2) if (mask >> k) & 1]
        adj = make_adj(n, edges)
        if not is_connected(adj):
            continue
        if min(len(nb) for nb in adj) < 3:
            continue
        # Check for all DFS roots
        for src in range(n):
            parent, back = build_dfs(adj, src)
            lb = n // 2 + 1
            if len(back) < lb:
                violations += 1
        checked += 1

assert violations == 0, f"Back-edge lower bound violated on {violations} cases"
assert checked >= 10, f"Too few graphs checked: {checked}"
print(f"OK: back-edge count >= floor(n/2)+1 holds on {checked} graphs (exhaustive n<=6)")
CHECK -->

## Part D (open): gap-pair enumeration

**Observation.** For a DFS leaf $v$ with back-edge gaps $\delta_1 > \delta_2
\ge 2$, the pair must satisfy:
1. $\delta_1 \notin \{3, 7, 15\}$ (fundamental cycle length not power of 2),
2. $\delta_2 \notin \{3, 7, 15\}$,
3. $\delta_1 - \delta_2 \notin \{2, 6, 14\}$.

The valid pairs $(\delta_2, \delta_1)$ with both $\ge 2$ and $\le 31$ are
(enumerated): $(2,5), (2,6), (2,9), (2,10), (2,11), (2,12), (2,13), (4,5),
(4,6), (4,9), (4,10), (5,6), (5,9), (5,10), (5,11), (5,12), (5,13), \ldots$
(and other pairs not triggering constraints 1–3).

The conjecture would follow if one could show that in every min-degree-3
graph the DFS structure forces every leaf to have a pair in the FORBIDDEN
region — but the above valid pairs show this is false for individual leaves.
The argument would need to use multiple leaves or a global DFS structure
argument.
