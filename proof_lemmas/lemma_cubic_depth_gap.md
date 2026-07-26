---
id: cubic_depth_gap
status: open
depends_on: [chain_locality_r3]
discharged_by_round: null
introduced_at_round: 6
---

# Lemma `cubic_depth_gap` (depth-gap mechanism for chain_locality_r3 in cubic graphs)

**Goal.** Investigate whether chain_locality_r3 holds in cubic DFS trees
via the *fundamental-cycle mechanism*: a single back edge $(u,v)$ with
depth-gap $\text{depth}(u) - \text{depth}(v) \in \{3, 7, 15, 31\}$
directly witnesses a C4/C8/C16/C32 with **exactly 1 back edge**, making
chain_locality_r3 trivially true.  If this mechanism applies to all (G, T)
pairs, chain_locality_r3 follows for cubic graphs without any global
minimum argument.  If it fails for some pair, the pair still gives data on
what harder argument is needed.

## Setup

**Cubic DFS tree back-edge budget** (well-known):

- $G$ cubic, $n$ vertices ($n$ even, $n \ge 4$).
- $|E(G)| = 3n/2$;  tree edges = $n-1$; back edges $= n/2 + 1$.
- Leaf in $T$: degree 3 in $G$, 1 parent tree edge, 0 children → **2
  back edges**.
- Internal non-root: 1 parent + $k$ children + $(2-k)$ back edges;
  $k \in \{1,2\}$, so back edges $\in \{0,1\}$.
- Root: $k$ children + $(3-k)$ back edges, $k \in \{1,2,3\}$.

Each back edge $(u,v)$ ($v = $ ancestor of $u$) defines a *fundamental
cycle* of length $\delta(u,v) + 1$ where $\delta(u,v) = \text{depth}(u) -
\text{depth}(v)$ is the *depth-gap*. This cycle has exactly 1 back edge.

**Easy path vs hard path**: if any back edge has depth-gap $\in \{3,7,15,
31\}$, chain_locality_r3 holds via 1 back edge (easy path). Otherwise,
chain_locality_r3 must hold via non-fundamental cycles (hard path).

## Hypothesis

*For every cubic graph $G$ on $n \le 24$ vertices and every DFS tree $T$,
some back edge of $T$ has depth-gap in $\{3, 7, 15\}$.*

(Depth-gap 31 requires $n \ge 32$; excluded from the range tested.)

If true: chain_locality_r3 holds via 1-back-edge witnesses for all cubic
$n \le 24$. If false: identify the (G, T) pairs where only the hard path
applies, and measure how chain_locality_r3 still holds there.

## CHECK — depth-gap coverage probe

<!-- CHECK
# cubic_depth_gap: does every cubic DFS tree have a back edge with depth-gap in {3,7,15}?
# Exit 0 = claim holds over sampled graphs (chain_locality_r3 also verified in all cases).
# If assert fires: the pair (edges, tree_mask, root) is a counterexample to the easy-path hypothesis
#   (but NOT to chain_locality_r3 — that must be checked separately).
import random

rng = random.Random(20260726_5)

PO2_GAPS = {3, 7, 15}  # depth-gaps for C4, C8, C16 fundamental cycles

def make_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    return adj

def connected_cubic(n, edges):
    deg = [0] * n
    for u, v in edges: deg[u] += 1; deg[v] += 1
    if min(deg) < 3 or max(deg) > 3: return False
    adj = make_adj(n, edges)
    seen = {0}; stack = [0]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); stack.append(w)
    return len(seen) == n

def sample_cubic(nn, rnd, tries=2000):
    for _ in range(tries):
        stubs = [v for v in range(nn) for _ in range(3)]
        rnd.shuffle(stubs)
        edges = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i+1]
            if a == b or (min(a,b),max(a,b)) in edges: ok = False; break
            edges.add((min(a,b),max(a,b)))
        if not ok: continue
        el = list(edges)
        if connected_cubic(nn, el): return el
    return None

def dfs_tree_and_depths(n, edges, adj, root, rnd):
    eidx = {(min(u,v),max(u,v)): i for i,(u,v) in enumerate(edges)}
    depth = [-1]*n; depth[root] = 0
    tree_mask = 0
    def nbrs(u): ns = adj[u][:]; rnd.shuffle(ns); return ns
    stack = [(root, iter(nbrs(root)))]
    seen = [False]*n; seen[root] = True
    while stack:
        u, it = stack[-1]; adv = False
        for w in it:
            if not seen[w]:
                seen[w] = True
                depth[w] = depth[u] + 1
                tree_mask |= 1 << eidx[(min(u,w),max(u,w))]
                stack.append((w, iter(nbrs(w)))); adv = True; break
        if not adv: stack.pop()
    return tree_mask, depth

def po2_cycles_min_backedge(n, edges, tree_mask, cap=100000):
    eidx = {(min(u,v),max(u,v)): i for i,(u,v) in enumerate(edges)}
    adj = make_adj(n, edges)
    full = (1 << len(edges)) - 1
    nt = full & ~tree_mask
    min_rad = None
    steps = 0
    for L in [4, 8, 16]:
        if L > n: continue
        for s in range(n):
            stack = [(s, (s,), 1 << s)]
            while stack:
                u, path, vis = stack.pop()
                steps += 1
                if steps > cap: return min_rad
                if len(path) == L:
                    if s in adj[u]:
                        m = 0; cyc = path + (s,)
                        for a, b in zip(cyc, cyc[1:]): m |= 1 << eidx[(min(a,b),max(a,b))]
                        r = bin(m & nt).count('1')
                        if min_rad is None or r < min_rad: min_rad = r
                        if min_rad == 0: return 0
                    continue
                for w in adj[u]:
                    if w > s and not (vis >> w & 1):
                        stack.append((w, path+(w,), vis|(1<<w)))
    return min_rad

hard_path_count = 0
easy_path_count = 0
total = 0

for nn in [8, 10, 12, 14, 16]:
    rnd = random.Random(rng.randrange(1<<30))
    for trial in range(6):
        edges = sample_cubic(nn, rnd)
        if edges is None: continue
        eidx = {(min(u,v),max(u,v)): i for i,(u,v) in enumerate(edges)}
        adj = make_adj(nn, edges)
        for root in range(min(3, nn)):
            tm, depth = dfs_tree_and_depths(nn, edges, adj, root, rnd)
            # Check easy path: any back edge with depth-gap in PO2_GAPS?
            easy = False
            for i,(u,v) in enumerate(edges):
                if not (tm >> i & 1):
                    g = abs(depth[u]-depth[v])
                    if g in PO2_GAPS: easy = True; break
            if easy:
                easy_path_count += 1
            else:
                # Hard path: verify chain_locality_r3 still holds
                min_rad = po2_cycles_min_backedge(nn, edges, tm)
                assert min_rad is not None and min_rad <= 3, (
                    "cubic_depth_gap: chain_locality_r3 VIOLATION on hard-path instance: "
                    "n=" + str(nn) + " edges=" + repr(edges) + " root=" + str(root) +
                    " tree_mask=" + str(tm) + " min_rad=" + repr(min_rad))
                hard_path_count += 1
            total += 1

# Report balance (informational, not a guard)
# easy=~X, hard=~Y out of total
CHECK -->

## Preliminary findings

*(To be filled after CHECK runs.)*

The CHECK tests the easy-path hypothesis on 6 random cubic graphs × 5 size
classes × 3 roots = 90 (G, T) pairs.  For each "hard" instance (no
po2-depth-gap back edge), chain_locality_r3 is verified explicitly — so
the CHECK cannot pass while chain_locality_r3 is violated.

## Expected outcomes and consequences

| Outcome | Meaning |
|---------|---------|
| All pairs are easy-path | Fundamental-cycle mechanism suffices; chain_locality_r3 is provable for cubic $n \le 24$ if the easy path extends to larger $n$ |
| Some pairs are hard-path, chain_locality_r3 still holds | Need a second argument for the hard pairs; identify their structure |
| Hard-path pair violates chain_locality_r3 | `chain_locality_r3` is falsified for some $n > 12$ (radius pushes to ≥ 4) |

## Next steps

1. If many hard-path pairs: study their tree structure (are they always
   "tall" trees with large max depth?).
2. If easy path dominates: prove the depth-gap hypothesis analytically for
   cubic DFS trees (pigeonhole on leaf back-edge gaps?).
3. Connect to Markström's $n \ge 30$ lower bound: for $n < 30$, Gyárfás
   conjecture holds; is the depth-gap mechanism responsible?

## Status

Hypothesis open pending CHECK. check_locality_r3 separately verified in
all hard-path cases found by this probe.
