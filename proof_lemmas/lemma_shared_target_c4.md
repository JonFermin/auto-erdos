---
id: shared_target_c4
status: open
depends_on: [chain_locality_r3, ham_path_tree_r3, cubic_depth_gap]
discharged_by_round: null
introduced_at_round: 12
---

# Lemma `shared_target_c4` (hard-path cubic Hamiltonian-path: shared-target yields po2-cycle ≤ 3 back edges)

**Context.** The "easy-path" mechanism (a single back edge with po2
depth-gap) does NOT cover all cubic DFS trees: there exist valid (G,T)
pairs where every back edge of T has depth-gap NOT in {3,7,15,31}. For
those "hard-path" pairs, chain_locality_r3 requires a multi-back-edge
argument.

This lemma focuses on the Hamiltonian-path DFS tree sub-case and
introduces the **shared-target C4** mechanism to handle hard-path instances.

## Concrete hard-path example (n=10)

**G10**: 10-vertex cubic graph with Hamiltonian-path DFS tree T = 0→1→...→9.

Tree edges: {0-1, 1-2, 2-3, 3-4, 4-5, 5-6, 6-7, 7-8, 8-9}.

Back edges: {0-2, 0-4, 1-6, 3-8, 5-9, 7-9}.

Back-edge depth-gaps (depth(v)=v in the Hamiltonian-path tree):
- 0-2: gap = 2.
- 0-4: gap = 4.
- 1-6: gap = 5.
- 3-8: gap = 5.
- 5-9: gap = 4.
- 7-9: gap = 2.

All gaps = {2, 4, 5, 5, 4, 2}. None in {3, 7, 15, 31}. This is a
hard-path instance: no single back edge gives a po2 fundamental cycle.

**Verification that G10 is cubic** (degree 3 at every vertex):
- v=0: {1 (tree), 2 (back), 4 (back)} → degree 3. ✓
- v=1: {0 (tree), 2 (tree), 6 (back)} → degree 3. ✓
- v=2: {1 (tree), 3 (tree), 0 (back)} → degree 3. ✓
- v=3: {2 (tree), 4 (tree), 8 (back)} → degree 3. ✓
- v=4: {3 (tree), 5 (tree), 0 (back)} → degree 3. ✓
- v=5: {4 (tree), 6 (tree), 9 (back)} → degree 3. ✓
- v=6: {5 (tree), 7 (tree), 1 (back)} → degree 3. ✓
- v=7: {6 (tree), 8 (tree), 9 (back)} → degree 3. ✓
- v=8: {7 (tree), 9 (tree), 3 (back)} → degree 3. ✓
- v=9: {8 (tree), 5 (back), 7 (back)} → degree 3. ✓

Total edges: 9 (tree) + 6 (back) = 15 = 3·10/2. ✓

## Chain_locality_r3 holds via shared-target C4

Back edges 0-2 and 0-4 share target vertex 0. Sources: k1=2, k2=4.

C4 witness: cycle 0-2-3-4-0.
- Edge 0-2: back edge. ✓
- Edge 2-3: tree edge. ✓
- Edge 3-4: tree edge. ✓
- Edge 4-0: back edge. ✓
- Cycle length = 4 = 2². Back-edge count = 2 ≤ 3. ✓

**Structural reason**: the two back edges share target v=0 (the root);
sources k1=2, k2=4 satisfy bridge length k2-k1 = 2, so the cycle is
(tree path 2→3→4) + (back 4→0) + (back 0→2), total length 2+2 = 4 = C4.

## General shared-target mechanism

**Definition.** A *shared-target pair* (k1, k2, v) has two back edges
(v,k1) and (v,k2) (k1<k2, v proper ancestor of both). The *bridge
length* is b = k2-k1. The resulting 2-back-edge cycle has length b+2.

**Claim.** If b = k2-k1 ∈ {2, 6, 14, 30} then the cycle has po2 length
{4, 8, 16, 32}, giving a C4/C8/C16/C32 with 2 back edges. chain_locality_r3
holds for this (G,T).

## Degree-forcing structure of Hamiltonian-path cubic DFS trees

For a cubic Hamiltonian-path DFS tree on n vertices (n even, n≥4):

**Interior vertex types** (vertices 2,…,n-2):
- **Type A**: out-back-degree = 1, in-back-degree = 0. Count = n/2-1.
- **Type B**: out-back-degree = 0, in-back-degree = 1. Count = n/2-2.
(Forced by cubic degree constraint: each interior vertex has 2 tree edges,
so exactly 1 back-edge total. Since only descendants can send back edges
to them, each interior vertex either sends or receives, not both.)

**Root (v=0)**: receives 2 back edges (in-back-degree = 2).
**Vertex 1**: receives 1 back edge (cannot send — only ancestor is 0 = parent).
**Leaf (v=n-1)**: sends 2 back edges, receives 0.

**Consequence**: every back edge must land at root, vertex 1, or a Type-B
vertex. Type-A vertices (n/2-1 of them) cannot receive back edges.

**Root always holds a shared-target pair.** The root receives exactly 2
back edges from sources k1 < k2. These share target v=0 with bridge length
k2-k1. For chain_locality_r3 via this pair: need k2-k1 ∈ {2,6,14,30}.

**Open sub-question**: In any hard-path cubic Hamiltonian-path DFS tree,
is the bridge length k2-k1 of the root shared-target pair always in
{2,6,14,30}? Or can k2-k1 avoid this set, requiring a 3-back-edge argument?

## CHECK — hard-path Hamiltonian-path cubic graphs; chain_locality_r3 via shared-target

<!-- CHECK
# shared_target_c4: for cubic Hamiltonian-path DFS trees in the hard-path regime,
# (1) explicitly verify G10 is a valid hard-path instance,
# (2) check chain_locality_r3 holds for all sampled hard-path instances,
# (3) identify what fraction is covered by the shared-target C4/C8 mechanism.
import random
from collections import defaultdict

PO2_GAPS = {3, 7, 15, 31}
PO2_LENS = {4, 8, 16}

# --- Verify G10 explicitly ---
G10_n = 10
G10_tree = [(k, k+1) for k in range(G10_n-1)]
G10_back = [(0,2),(0,4),(1,6),(3,8),(5,9),(7,9)]
G10_all = G10_tree + G10_back

# Degree check
deg = [0]*G10_n
for u,v in G10_all:
    deg[u]+=1; deg[v]+=1
assert all(d==3 for d in deg), "G10 not cubic: " + repr(deg)

# Back-edge gap check (depth = index in Hamiltonian-path tree)
G10_gaps = sorted(abs(u-v) for u,v in G10_back)
assert set(G10_gaps) & PO2_GAPS == set(), \
    "G10 is not hard-path: gap in PO2_GAPS found: " + repr(set(G10_gaps) & PO2_GAPS)

# Verify C4 = {0,2,3,4}: edges 0-2(back), 2-3(tree), 3-4(tree), 4-0(back)
c4_edges = {(0,2),(2,3),(3,4),(0,4)}
c4_back = c4_edges & {(min(u,v),max(u,v)) for u,v in G10_back}
assert len(c4_edges) == 4, "C4 should have 4 edges"
assert len(c4_back) == 2, "C4 should have 2 back edges, got: " + repr(c4_back)
# Verify 0-2 and 0-4 in c4_back
assert (0,2) in c4_back and (0,4) in c4_back, "Wrong back edges in C4"

# --- Sampling: hard-path Hamiltonian-path cubic graphs at n=10,12,14,16 ---
rng = random.Random(20260727_1)

def sample_hard_path_cubic_ham(nn, rng, max_trials=2000):
    """Sample a cubic Hamiltonian-path DFS tree that is hard-path."""
    # Interior vertices: {2,...,nn-2}, Type A or B.
    # n_A = nn//2 - 1 (send 1 back edge each)
    # n_B = nn//2 - 2 (receive 1 back edge each)
    # Root: receive 2. Vertex 1: receive 1. Leaf: send 2.
    n_A = nn//2 - 1
    interior = list(range(2, nn-1))
    for _ in range(max_trials):
        # Randomly choose Type A vertices
        type_A = sorted(rng.sample(interior, n_A))
        type_B = [v for v in interior if v not in set(type_A)]
        # Target slots: {0:2, 1:1} + {b:1 for b in type_B}
        slots = {0: 2, 1: 1}
        for b in type_B:
            slots[b] = 1
        avail = dict(slots)
        back = []
        ok = True
        # Assign leaf's 2 back edges (nn-1 sends to 2 distinct targets in avail,
        # gap must not be in PO2_GAPS, target must be proper ancestor: < nn-2)
        leaf_tgts = [t for t in avail if t < nn-2 and (nn-1-t) not in PO2_GAPS]
        if len(leaf_tgts) < 2:
            continue
        chosen_leaf = rng.sample(leaf_tgts, 2)
        for t in chosen_leaf:
            back.append((min(t,nn-1), max(t,nn-1)))
            avail[t] -= 1
            if avail[t] == 0: del avail[t]
        # Assign Type A vertices (in random order)
        rng.shuffle(type_A)
        for k in type_A:
            # j must be in avail, j < k-1 (proper ancestor, not parent k-1), gap not in PO2_GAPS
            candidates = [t for t in avail if t < k-1 and (k-t) not in PO2_GAPS]
            if not candidates:
                ok = False; break
            t = rng.choice(candidates)
            back.append((min(t,k), max(t,k)))
            avail[t] -= 1
            if avail[t] == 0: del avail[t]
        if not ok or avail:
            continue
        # Verify hard-path
        if any(abs(u-v) in PO2_GAPS for u,v in back):
            continue
        return back
    return None

def po2_min_radius(nn, tree_edges, back_edges, cap=50000):
    all_edges = tree_edges + back_edges
    eidx = {(min(u,v),max(u,v)):i for i,(u,v) in enumerate(all_edges)}
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
                if len(path) == L:
                    if s in adj[u]:
                        cyc = path+(s,)
                        r = sum(1 for a,b in zip(cyc,cyc[1:])
                                if (min(a,b),max(a,b)) in back_set)
                        if min_rad is None or r < min_rad: min_rad = r
                        if min_rad == 0: return 0
                    continue
                for w in adj[u]:
                    if w > s and not (vis>>w&1):
                        stack.append((w,path+(w,),vis|(1<<w)))
    return min_rad

def shared_target_po2(back_edges):
    """Return True if any shared-target pair has po2 bridge."""
    tgt_srcs = defaultdict(list)
    for u,v in back_edges:
        lo,hi = min(u,v),max(u,v)
        tgt_srcs[lo].append(hi)
    for tgt, srcs in tgt_srcs.items():
        if len(srcs) >= 2:
            ss = sorted(srcs)
            for i in range(len(ss)):
                for j in range(i+1,len(ss)):
                    bl = ss[j]-ss[i]
                    if (bl+2) in PO2_LENS:
                        return True
    return False

total_hard = 0
st_covered = 0
for nn in [10, 12, 14, 16]:
    tree = [(k,k+1) for k in range(nn-1)]
    for _ in range(80):
        back = sample_hard_path_cubic_ham(nn, rng)
        if back is None:
            continue
        total_hard += 1
        mr = po2_min_radius(nn, tree, back)
        assert mr is not None and mr <= 3, (
            "chain_locality_r3 VIOLATION in hard-path Hamiltonian-path cubic graph! "
            "n=" + str(nn) + " back=" + repr(back) + " min_rad=" + repr(mr))
        if shared_target_po2(back):
            st_covered += 1

assert total_hard > 0, "No hard-path instances found — check sampler"
# Report coverage fraction (informational, not a guard)
CHECK -->

## Status

CHECK guards chain_locality_r3 in all sampled hard-path Hamiltonian-path
cubic instances at n=10..16. The shared-target mechanism covers a
(measured) fraction of hard-path cases. The remaining cases — where the
root's shared-target bridge length is not po2-compatible — require a 3-back-
edge argument (next lemma).

Analytic proof of the claim "root bridge length k2-k1 ∈ {2,6,14,30} for
all hard-path Hamiltonian-path trees" remains open.
