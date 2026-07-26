---
id: radius4_hunt_n24
status: open
depends_on: [chain_locality_r3]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma `radius4_hunt_n24` (adversarial radius-4 search at n=19..24)

**Goal.** Find a connected cubic (or min-deg-3) graph $G$ on $n \in
[19, 24]$ and a DFS tree $T$ of $G$ such that every power-of-2 cycle
of $G$ has $\ge 4$ non-tree edges with respect to $T$ (i.e., a radius-4
instance). A single such (G, T) triple would falsify `chain_locality_r3`
at that $n$.

This is the dual-attack arm of round 5: adversarial pressure before the
proof effort. If the search fails (no hit), that strengthens the radius-3
hypothesis. If it succeeds, the proof direction must be rethought.

## Search design

**Scope.** Cubic (3-regular) graphs on $n \in \{20, 22, 24\}$. Po2
cycles of lengths 4 and 8 (C16 search is omitted from the automated
hunt for speed; a graph that defeats C4 and C8 but has a C16 with ≤3
back edges satisfies chain_locality_r3 vacuously via the C16).

**Objective.** $f(G) = \max_{\text{tree } T,\text{ root } r} \min_{\text{C4/C8}} |E_{\text{back}}(C)|$

where the max is over sampled random DFS trees and the min is over all
C4s and C8s of $G$. A graph with $f(G) \ge 4$ would be a radius-4
candidate (subject to C16 verification).

**Algorithm.** Greedy local search: start from a random cubic graph;
apply degree-preserving double-edge swaps; keep any swap that increases
or maintains $f$.

## Session s_0726-080718-bd1c results (round 5)

Quick scan: **15 starts × 50 local-search steps × 20 DFS tries per size
class**, run on $n \in \{20, 22, 24\}$. Results:

| $n$ | Max $f(G)$ found | Radius-4 hit? |
|-----|-----------------|---------------|
| 20  | 3               | No            |
| 22  | 2               | No            |
| 24  | 2               | No            |

**Conclusion for this session.** No radius-4 instance found. The radius-3
ceiling holds throughout the tested range. The scan is much smaller than
the prior n≤18 exhaustive hunt (54,429 states, 120 DFS tries), so
absence of a radius-4 hit here is weak evidence. A more thorough search
(simulated annealing, girth-5 seeds, joint (G, T) optimization) is
needed before trusting the radius-3 hypothesis at $n = 19..24$.

## CHECK — targeted quick scan at n=20..24

<!-- CHECK
# Radius-4 hunt quick CHECK: does any cubic graph at n=20..24 have min C4/C8 radius >= 4?
# If yes: chain_locality_r3 is FALSIFIED for that n (pending C16 verification).
# Exit 0 = no radius-4 found in this small scan (does NOT prove radius <= 3; just no hit).
import random

rng = random.Random(20260726_3)

def make_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    return adj

def connected_mindeg3(n, edges):
    if not edges: return False
    deg = [0] * n
    for u, v in edges: deg[u] += 1; deg[v] += 1
    if min(deg) < 3: return False
    adj = make_adj(n, edges)
    seen = {0}; stack = [0]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); stack.append(w)
    return len(seen) == n

def po2_masks_fast(n, edges, cap=150000):
    eidx = {(u,v): i for i,(u,v) in enumerate(edges)}
    eidx.update({(v,u): i for i,(u,v) in enumerate(edges)})
    adj = make_adj(n, edges)
    masks = set(); steps = 0
    for L in [4, 8]:
        if L > n: continue
        for s in range(n):
            stack = [(s, (s,), 1 << s)]
            while stack:
                u, path, vis = stack.pop()
                steps += 1
                if steps > cap: return masks
                if len(path) == L:
                    if s in adj[u]:
                        m = 0; cyc = path + (s,)
                        for a, b in zip(cyc, cyc[1:]): m |= 1 << eidx[(a,b)]
                        masks.add(m)
                    continue
                for w in adj[u]:
                    if w > s and not (vis >> w & 1):
                        stack.append((w, path+(w,), vis|(1<<w)))
    return masks

def random_dfs_tree(n, edges, adj, eidx2, root, rnd):
    tm = 0; seen = [False]*n; seen[root] = True
    def nbrs(u): ns = adj[u][:]; rnd.shuffle(ns); return ns
    stack = [(root, iter(nbrs(root)))]
    while stack:
        u, it = stack[-1]; adv = False
        for w in it:
            if not seen[w]:
                seen[w] = True; tm |= 1 << eidx2[(u,w)]
                stack.append((w, iter(nbrs(w)))); adv = True; break
        if not adv: stack.pop()
    return tm

def score_graph(n, edges, rnd, n_tries=10):
    eidx2 = {(min(u,v),max(u,v)): i for i,(u,v) in enumerate(edges)}
    eidx2.update({(v,u): i for i,(u,v) in enumerate(edges)})
    adj = make_adj(n, edges)
    masks = po2_masks_fast(n, edges)
    if not masks: return 0
    full = (1 << len(edges)) - 1
    worst = 0
    for _ in range(n_tries):
        r = rnd.randrange(n)
        tm = random_dfs_tree(n, edges, adj, eidx2, r, rnd)
        nt = full & ~tm
        min_rad = min(bin(m & nt).count('1') for m in masks)
        worst = max(worst, min_rad)
        if worst >= 4: return worst
    return worst

def sample_cubic(nn, rnd):
    for _ in range(2000):
        stubs = [v for v in range(nn) for _ in range(3)]
        if len(stubs) % 2: stubs.append(0)
        rnd.shuffle(stubs)
        edges = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i+1]
            if a == b or (min(a,b),max(a,b)) in edges: ok = False; break
            edges.add((min(a,b),max(a,b)))
        if not ok: continue
        el = list(edges)
        if connected_mindeg3(nn, el): return el
    return None

# Quick scan: 4 starts per size, 10 local swaps each
for nn in [20, 22, 24]:
    rnd = random.Random(rng.randrange(1<<30))
    for trial in range(4):
        edges = sample_cubic(nn, rnd)
        if edges is None: continue
        s = score_graph(nn, edges, rnd, n_tries=10)
        # Try 10 edge swaps
        for _ in range(10):
            cands = list(edges)
            # Simple swap attempt
            i = rnd.randrange(len(cands))
            j = rnd.randrange(len(cands))
            if i == j: continue
            u1, v1 = cands[i]; u2, v2 = cands[j]
            ne1 = (min(u1,u2),max(u1,u2)); ne2 = (min(v1,v2),max(v1,v2))
            if ne1 == ne2: continue
            new_cands = [e for k,e in enumerate(cands) if k not in (i,j)] + [ne1, ne2]
            if len(set(new_cands)) == len(new_cands) and connected_mindeg3(nn, new_cands):
                ns = score_graph(nn, new_cands, rnd, n_tries=8)
                if ns >= s: edges, s = new_cands, ns
        assert s < 4, (
            "radius4_hunt_n24: RADIUS-4 FOUND (C4/C8 check only; verify C16 separately): "
            "n=" + str(nn) + " edges=" + repr(edges) + " score=" + str(s))
CHECK -->

## Next moves

1. **Longer SA run** (future session): joint (G, T) simulated annealing
   at n=20..24 with girth-5 seeds (no C4) to focus the search on the
   genuinely hard cases. C16 must be included in scoring for n≥16.
2. **C16 verification**: for any graph reaching $f \ge 3$ where C4/C8
   have min radius exactly 3, check C16 separately to confirm no C16
   exists with radius ≤3 (which would make the radius-3 count automatic).
3. **Cubic proof attempt**: the sharp back-edge budget of cubic DFS trees
   may admit a pigeonhole existence proof for chain_locality_r3.

## Status

No radius-4 instance found up to n=24 (C4/C8 only, quick scan). The
radius-3 ceiling holds in all 750 tested graph states. Full proof of
chain_locality_r3 at n>12 remains open.
