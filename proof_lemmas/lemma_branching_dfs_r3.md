---
id: branching_dfs_r3
status: open
depends_on: [chain_locality_r3, shared_target_c4]
discharged_by_round: null
introduced_at_round: 15
---

# Lemma `branching_dfs_r3` (hard-path cubic branching DFS trees: shared-source yields po2-cycle ≤ 2 back edges)

**Scope note.** This lemma constructs cubic graphs with **girth 3** (contain
triangles). The Moore bound for girth ≥ 5 is NOT applicable here.

**Context.** `lemma_shared_target_c4` handles hard-path Hamiltonian-path cubic
DFS trees via the shared-target pair at the root (root receives 2 back edges).
For branching DFS trees (root has ≥ 2 tree children), the root receives ≤ 1
back edge, so no shared-target pair exists at the root. Instead, every leaf
sends exactly 2 back edges, providing a **shared-source pair** at every leaf.

## Structural duality: shared-target vs. shared-source

**Shared-target pair** (root of Hamiltonian-path DFS tree):
- Two back edges (k1, root) and (k2, root) share target = root
- Bridge length b = depth(k2) − depth(k1); cycle length = b + 2
- Hamiltonian-path root: k_T = 1 tree child, k_B = 2 back-edge targets → always a shared-target pair

**Shared-source pair** (any leaf of any cubic DFS tree):
- Two back edges (leaf, a1) and (leaf, a2) share source = leaf, depth(a1) < depth(a2)
- Bridge length b = depth(a2) − depth(a1); cycle length = b + 2
- Every cubic DFS leaf: 1 parent edge → 2 remaining = 2 back edges sent → always a shared-source pair

**Po2-cycle condition** (identical in both cases): b ∈ {2, 6, 14, 30} gives
cycle length ∈ {4, 8, 16, 32} with 2 back edges.

## Degree-forcing structure of branching cubic DFS trees

For a cubic DFS tree T with root r (degree 3 in G, no parent edge):

- **Root r**: k_T tree children + k_B back-edge targets from descendants = 3
  - Hamiltonian-path: k_T = 1, k_B = 2 → shared-target pair at root
  - Branching: k_T ≥ 2, k_B ≤ 1 → no shared-target pair at root
- **Branching vertex v** (k_T = 2, interior): 1 parent + 2 children = 3 edges; no back edges
- **Type-1 interior vertex v** (k_T = 1): 1 parent + 1 child = 2 tree edges; exactly 1 back edge (in or out)
- **Leaf v** (k_T = 0): 1 parent edge; **2 back edges sent to ancestors** (forced by cubic degree)

Every leaf is a shared-source vertex. Therefore, in any cubic DFS tree with ≥ 1
leaf (always true), ≥ 1 shared-source pair exists.

## Concrete hard-path branching example (n=10, girth=3)

**G10B**: 10-vertex cubic graph with caterpillar DFS tree (root 0 has 2 children).

DFS tree (root 0, branching at root):
- Left chain: 0 → 1 → 2 → 3 → 4 (depths 0,1,2,3,4; leaf = vertex 4)
- Right chain: 0 → 5 → 6 → 7 → 8 → 9 (depths 0,1,2,3,4,5; leaf = vertex 9)

Tree edges: {0-1, 1-2, 2-3, 3-4, 0-5, 5-6, 6-7, 7-8, 8-9}.

Back edges: {(4,0), (4,2), (9,5), (9,7), (3,1), (8,6)}.

Back-edge depth-gaps:
- (4,0): gap = 4−0 = 4.
- (4,2): gap = 4−2 = 2.
- (9,5): gap = 5−1 = 4.
- (9,7): gap = 5−3 = 2.
- (3,1): gap = 3−1 = 2.
- (8,6): gap = 4−2 = 2.

All gaps = {4,2,4,2,2,2}. None in {3,7,15,31}. Hard-path instance. ✓

**Girth of G10B = 3.** Triangle {1,2,3}: edges 1-2 (tree), 2-3 (tree), 1-3
(back edge (3,1)). Triangle {2,3,4}: edges 2-3 (tree), 3-4 (tree), 2-4
(back edge (4,2)). Moore bound for girth-5 graphs is inapplicable.

**Cubic degree verification**:
- v=0: {1(tree), 5(tree), 4(back)} → degree 3. ✓
- v=1: {0(tree), 2(tree), 3(back)} → degree 3. ✓
- v=2: {1(tree), 3(tree), 4(back)} → degree 3. ✓
- v=3: {2(tree), 4(tree), 1(back)} → degree 3. ✓
- v=4: {3(tree), 0(back), 2(back)} → degree 3. ✓
- v=5: {0(tree), 6(tree), 9(back)} → degree 3. ✓
- v=6: {5(tree), 7(tree), 8(back)} → degree 3. ✓
- v=7: {6(tree), 8(tree), 9(back)} → degree 3. ✓
- v=8: {7(tree), 9(tree), 6(back)} → degree 3. ✓
- v=9: {8(tree), 5(back), 7(back)} → degree 3. ✓

Total: 9 (tree) + 6 (back) = 15 = 3·10/2. ✓

## Shared-source C4 witnesses in G10B

**Leaf 4** (depth 4) sends back edges to ancestors at depths 0 and 2 (bridge = 2 − 0 = 2):
- C4 cycle: 0 → 1 → 2 → 4 → 0.
  Edges: 0-1 (tree), 1-2 (tree), 2-4 (back), 4-0 (back). Length = 4 = 2². ✓

**Leaf 9** (depth 5) sends back edges to ancestors at depths 1 (vertex 5) and 3 (vertex 7) (bridge = 3 − 1 = 2):
- C4 cycle: 5 → 6 → 7 → 9 → 5.
  Edges: 5-6 (tree), 6-7 (tree), 7-9 (back), 9-5 (back). Length = 4 = 2². ✓

## General shared-source mechanism

**Claim.** If leaf L has back edges to ancestors a1, a2 with depth(a1) < depth(a2)
and depth(a2) − depth(a1) = b ∈ {2, 6, 14, 30}, then the symmetric difference of
the fundamental cycles of the two back edges gives a po2-cycle of length b+2 ∈
{4, 8, 16, 32} using exactly 2 back edges.

**Cycle**: a1 →(tree path, b steps)→ a2 →(back edge a2-L)→ L →(back edge L-a1)→ a1.
Length = b + 2. Back-edge count = 2 ≤ 3. chain_locality_r3 holds for this pair. ✓

**Open sub-question**: In any hard-path branching cubic DFS tree, does every leaf
always have bridge length b ∈ {2, 6, 14, 30}? Or can all leaf bridges avoid
{2, 6, 14, 30} (requiring a 3-back-edge argument)?

## CHECK — hard-path branching cubic DFS trees; chain_locality_r3 via shared-source

<!-- CHECK
# branching_dfs_r3: verify G10B; sample hard-path caterpillar branching cubic DFS trees;
# check chain_locality_r3; measure shared-source coverage.
import random
from collections import defaultdict
from itertools import permutations

PO2_GAPS = {3, 7, 15, 31}
PO2_LENS = {4, 8, 16, 32}

# --- Verify G10B explicitly ---
G10B_n = 10
G10B_tree = [(0,1),(1,2),(2,3),(3,4),(0,5),(5,6),(6,7),(7,8),(8,9)]
G10B_back = [(4,0),(4,2),(9,5),(9,7),(3,1),(8,6)]
G10B_all = G10B_tree + G10B_back
G10B_depth = {0:0,1:1,2:2,3:3,4:4,5:1,6:2,7:3,8:4,9:5}

deg = [0]*G10B_n
for u,v in G10B_all:
    deg[u]+=1; deg[v]+=1
assert all(d==3 for d in deg), "G10B not cubic: "+repr(deg)

gap_vals = [G10B_depth[u]-G10B_depth[v] if G10B_depth[u]>G10B_depth[v]
            else G10B_depth[v]-G10B_depth[u] for u,v in G10B_back]
assert set(gap_vals) & PO2_GAPS == set(), "G10B not hard-path: "+repr(set(gap_vals)&PO2_GAPS)

adj10B = [set() for _ in range(G10B_n)]
for u,v in G10B_all:
    adj10B[u].add(v); adj10B[v].add(u)
assert 3 in adj10B[1] and 1 in adj10B[3] and 2 in adj10B[1], "Triangle {1,2,3} missing"

back_set10B = {(min(u,v),max(u,v)) for u,v in G10B_back}
c4a = {(0,1),(1,2),(2,4),(0,4)}
assert c4a & back_set10B == {(0,4),(2,4)}, "C4 via leaf 4 wrong"
c4b = {(5,6),(6,7),(7,9),(5,9)}
assert c4b & back_set10B == {(5,9),(7,9)}, "C4 via leaf 9 wrong"

# --- Sampler for hard-path caterpillar branching cubic DFS trees ---
rng = random.Random(20260727_4)

def make_caterpillar(l, r):
    """Build depth dict and tree edges for caterpillar: root=0, left l, right r."""
    depth = {0: 0}
    for k in range(1, l+1): depth[k] = k
    for k in range(1, r+1): depth[l+k] = k
    tree = [(0,1)] + [(k,k+1) for k in range(1,l)] + [(0,l+1)] + [(l+k,l+k+1) for k in range(1,r)]
    return depth, tree

def is_anc_of(u, v, l, depth):
    """True if u is a proper ancestor of v in caterpillar tree."""
    if depth[u] >= depth[v]: return False
    if u == 0: return True
    u_left = 1 <= u <= l
    v_left = 1 <= v <= l
    return u_left == v_left  # must be on same chain (both left or both right)

def sample_branching_hard(nn, rng, max_trials=5000):
    for _ in range(max_trials):
        l = rng.randint(2, nn-3)
        r = nn-1-l
        if r < 2: continue
        depth, tree = make_caterpillar(l, r)
        ll, rl = l, l+r

        # Valid non-parent ancestors for each leaf
        def leaf_valid_ancs(leaf, l, r, depth):
            if 1 <= leaf <= l:  # left leaf
                cands = list(range(0, leaf-1))
            else:  # right leaf
                cands = [0] + list(range(l+1, leaf-1))
            d = depth[leaf]
            return [u for u in cands if (d - depth[u]) not in PO2_GAPS]

        ll_ancs = leaf_valid_ancs(ll, l, r, depth)
        rl_ancs = leaf_valid_ancs(rl, l, r, depth)
        if len(ll_ancs) < 2 or len(rl_ancs) < 2: continue

        for _a in range(30):
            ll_t = sorted(rng.sample(ll_ancs, 2))
            rl_t = sorted(rng.sample(rl_ancs, 2))
            back = [(ll, t) for t in ll_t] + [(rl, t) for t in rl_t]

            # Root: receives exactly 1 back edge; interior: 1 slot each
            slots = {0: 1}
            for v in range(1, l): slots[v] = 1
            for v in range(l+1, l+r): slots[v] = 1

            ok = True
            for _, t in back:
                if t not in slots: ok = False; break
                slots[t] -= 1
                if slots[t] == 0: del slots[t]
            if not ok: continue

            rem = list(slots.keys())
            if len(rem) % 2 != 0: continue

            # Try to pair remaining interior vertices as ancestor-descendant pairs
            found = False
            for _p in range(60):
                rng.shuffle(rem)
                extra = []
                ok2 = True
                for i in range(0, len(rem), 2):
                    a, b = rem[i], rem[i+1]
                    if is_anc_of(a, b, l, depth):
                        gap = depth[b]-depth[a]
                        if gap in PO2_GAPS: ok2=False; break
                        extra.append((b,a))
                    elif is_anc_of(b, a, l, depth):
                        gap = depth[a]-depth[b]
                        if gap in PO2_GAPS: ok2=False; break
                        extra.append((a,b))
                    else:
                        ok2 = False; break
                if ok2:
                    found = True
                    back = back + extra
                    break
            if found: return back, depth, tree, l, r
    return None

def shared_source_po2(back_edges, depth):
    src_tgts = defaultdict(list)
    for u,v in back_edges:
        du, dv = depth[u], depth[v]
        if du > dv: src_tgts[u].append(v)
        else: src_tgts[v].append(u)
    for src, tgts in src_tgts.items():
        if len(tgts) >= 2:
            ds = sorted(depth[t] for t in tgts)
            for i in range(len(ds)):
                for j in range(i+1, len(ds)):
                    if (ds[j]-ds[i]+2) in PO2_LENS: return True
    return False

def po2_min_radius(nn, tree_edges, back_edges, cap=40000):
    all_edges = tree_edges + back_edges
    adj = [[] for _ in range(nn)]
    for u,v in all_edges:
        adj[u].append(v); adj[v].append(u)
    back_set = {(min(u,v),max(u,v)) for u,v in back_edges}
    min_rad = None
    steps = 0
    for L in [4,8,16]:
        if L > nn: continue
        for s in range(nn):
            stack = [(s,(s,),1<<s)]
            while stack:
                u,path,vis = stack.pop()
                steps += 1
                if steps > cap: return min_rad
                if len(path)==L:
                    if s in adj[u]:
                        cyc = path+(s,)
                        r = sum(1 for a,b in zip(cyc,cyc[1:]) if (min(a,b),max(a,b)) in back_set)
                        if min_rad is None or r < min_rad: min_rad = r
                        if min_rad==0: return 0
                    continue
                for w in adj[u]:
                    if w > s and not (vis>>w&1):
                        stack.append((w,path+(w,),vis|(1<<w)))
    return min_rad

total = 0
ss_covered = 0
for nn in [10, 12, 14, 16]:
    for _ in range(60):
        result = sample_branching_hard(nn, rng)
        if result is None: continue
        back, depth, tree, l, r = result
        total += 1
        mr = po2_min_radius(nn, tree, back)
        assert mr is not None and mr <= 3, (
            "chain_locality_r3 VIOLATION in hard-path branching cubic DFS tree! "
            "n="+str(nn)+" l="+str(l)+" r="+str(r)+" back="+repr(back)+" min_rad="+repr(mr))
        if shared_source_po2(back, depth): ss_covered += 1

assert total > 0, "No hard-path branching instances found — check sampler"
CHECK -->

## Status

G10B verified: hard-path (gaps ∈ {4,2,4,2,2,2}), girth 3, branching DFS tree
(root has 2 children), chain_locality_r3 holds via shared-source C4 at both
leaves. CHECK block validates chain_locality_r3 for sampled hard-path branching
caterpillar cubic DFS trees at n=10..16.

Open sub-question: whether shared-source mechanism covers ALL hard-path branching
cubic DFS trees, or whether 3-back-edge arguments are needed when all leaf
bridges avoid {2,6,14,30}.
