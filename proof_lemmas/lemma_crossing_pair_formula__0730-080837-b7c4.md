---
id: crossing_pair_formula
status: open
depends_on: [sym_diff_nested]
discharged_by_round: null
introduced_at_round: 15
---

# Lemma `crossing_pair_formula` (crossing back-edge sym-diff cycle formula)

**Statement (proved).** Let $T$ be a DFS spanning tree of a graph $G$. Let
$e_1 = (s_1, a_1)$ and $e_2 = (s_2, a_2)$ be two back edges satisfying the
**strict same-branch crossing** conditions:

$$d_{a_1} < d_{a_2} < d_{s_1} < d_{s_2}$$
$$a_2 \text{ is an ancestor of } s_1 \quad\text{(equivalently, }a_1, a_2, s_1
\text{ are on a single root-to-} s_1 \text{ path)}$$
$$s_1 \text{ is an ancestor of } s_2 \quad\text{(so all four vertices lie on
a single root-to-} s_2 \text{ path)}$$

where $d_u = \operatorname{depth}(u)$ and $s_i$ is the deeper endpoint
(sender) of each back edge. Then

$$C_{(s_1,a_1)} \oplus C_{(s_2,a_2)} = \text{simple cycle of length }
(d_{a_2}-d_{a_1}) + (d_{s_2}-d_{s_1}) + 2.$$

**Proof.** Write $A = \operatorname{TreePath}(a_1, s_1)$ and
$B = \operatorname{TreePath}(a_2, s_2)$ for the two fundamental cycles'
tree-edge sets. In the strict crossing ordering $d_{a_1}<d_{a_2}<d_{s_1}<d_{s_2}$,
the depth ranges $[d_{a_1}, d_{s_1})$ and $[d_{a_2}, d_{s_2})$ overlap in
$[d_{a_2}, d_{s_1})$, so

$$A \cap B = \operatorname{TreePath}(a_2, s_1),$$
$$A \triangle B = \underbrace{\operatorname{TreePath}(a_1, a_2)}_{\text{depth } [d_{a_1},d_{a_2})} \;\cup\;
\underbrace{\operatorname{TreePath}(s_1, s_2)}_{\text{depth } [d_{s_1},d_{s_2})},$$

a disjoint union (the two path segments are at non-overlapping depth ranges).
Both back edges survive (each appears in exactly one fundamental cycle). The
surviving edge set is therefore

$$\operatorname{TreePath}(a_1,a_2) \;\cup\; \operatorname{TreePath}(s_1,s_2)
\;\cup\; \{(s_1,a_1),\,(s_2,a_2)\}.$$

**Degree check.**

| Vertex | Edges in surviving set | Degree |
|--------|----------------------|--------|
| $a_1$ | TreePath end + back $(s_1,a_1)$ | **2** |
| internal on $\operatorname{TreePath}(a_1,a_2)$ | two tree edges | **2** |
| $a_2$ | TreePath end + back $(s_2,a_2)$ | **2** |
| $s_1$ | TreePath end + back $(s_1,a_1)$ | **2** |
| internal on $\operatorname{TreePath}(s_1,s_2)$ | two tree edges | **2** |
| $s_2$ | TreePath end + back $(s_2,a_2)$ | **2** |

Every vertex has degree exactly 2; no other vertices are present.

**Connectivity.** The explicit cycle is

$$a_1 \xrightarrow{T} a_2 \xrightarrow{(s_2,a_2)} s_2 \xrightarrow{T} s_1
\xrightarrow{(s_1,a_1)} a_1,$$

visiting all vertices in the surviving edge set. Hence the edge set is a
**single simple cycle**.

**Cycle length** $= (d_{a_2}-d_{a_1}) + 1 + (d_{s_2}-d_{s_1}) + 1
= (d_{a_2}-d_{a_1}) + (d_{s_2}-d_{s_1}) + 2$. $\square$

---

## Corollary (po2 condition)

The cycle $C_{(s_1,a_1)} \oplus C_{(s_2,a_2)}$ is a **power-of-2 cycle** if
and only if

$$(d_{a_2}-d_{a_1}) + (d_{s_2}-d_{s_1}) \;\in\; \{2,\,6,\,14,\,30,\,\ldots\}
= \{2^k - 2 : k \ge 2\}.$$

The simplest case is $(d_{a_2}-d_{a_1}) = (d_{s_2}-d_{s_1}) = 1$: total
offset $= 2$, cycle length $= 4$ (C4).

---

## Correction of the R6 unified sym-diff theorem

The R6 "unified sym-diff theorem" (proof\_strategy Section 9) claimed:
*"In all same-branch cases (nested, crossing, same-leaf) the length is
$(\delta_1 - \delta_2) + 2$."*

**This is incorrect for strict crossing pairs.** For crossing pairs, the
correct formula is $(d_{a_2}-d_{a_1}) + (d_{s_2}-d_{s_1}) + 2$, which in
general does NOT equal $|\delta_1 - \delta_2| + 2$. Specifically:

$$|\delta_1-\delta_2| = |(d_{s_1}-d_{a_1})-(d_{s_2}-d_{a_2})|
= |(d_{a_2}-d_{a_1}) - (d_{s_2}-d_{s_1})|,$$

which equals $(d_{a_2}-d_{a_1})+(d_{s_2}-d_{s_1})$ only when one of the
two offsets is 0 (i.e.\ $a_1=a_2$ — same-vertex — or $s_1=s_2$ — same
sender, which is impossible since $d_{s_1}<d_{s_2}$). In general, the
crossing formula gives a strictly **larger** cycle length than $|\delta_1-\delta_2|+2$.

**Example.** CL-A with Hamiltonian-path tree rooted at 1 (back edges
$(7,3,\delta=5)$ and $(6,4,\delta=5)$, depths $d_{a_1}=3, d_{a_2}=4,
d_{s_1}=8, d_{s_2}=9$): crossing formula gives $(4-3)+(9-8)+2 = 4$ (C4),
while the nested formula would give $|5-5|+2 = 2$ (invalid — no cycle of
length 2 exists).

The **nested formula** $|\delta_1-\delta_2|+2$ remains correct for: same-vertex
pairs ($s_1=s_2$), and proper nested pairs
($d_{a_1}\le d_{a_2}$, $d_{s_2}\le d_{s_1}$). For crossing pairs the
correct formula is the one proved in this lemma.

---

## Updated coverage taxonomy for chain\_locality\_r3

Adding the crossing mechanism to the prior taxonomy
(Sections 13, 19 of proof\_strategy):

| Mechanism | Condition | Cycle length | Back edges | Radius |
|-----------|-----------|-------------|-----------|--------|
| Easy-path | Some gap $\in\{3,7,15,\ldots\}$ | $\delta+1$ | 1 | 1 |
| Nested/same-vertex | $|\delta_1-\delta_2| \in\{2,6,14,\ldots\}$ | $|\delta_1-\delta_2|+2$ | 2 | 2 |
| Crossing | $(d_{a_2}-d_{a_1})+(d_{s_2}-d_{s_1}) \in\{2,6,14,\ldots\}$ | offset$+2$ | 2 | 2 |
| Triple (double-sender) | $|d_x-d_b|\in\{0,4,12,\ldots\}$ | $|d_x-d_b|+4$ | 3 | 3 |

**Exhaustive counts** for CL-A/B/C (all valid Trémaux trees):

| Graph | Trees | Easy | Nested | Crossing | Triple | None |
|-------|-------|------|--------|----------|--------|------|
| CL-A | 356 | 272 (76.4%) | 72 (20.2%) | 8 (2.2%) | 4 (1.1%) | 0 |
| CL-B | 378 | 276 (73.0%) | 72 (19.0%) | 24 (6.3%) | 6 (1.6%) | 0 |
| CL-C | 360 | 228 (63.3%) | 96 (26.7%) | 24 (6.7%) | 12 (3.3%) | 0 |

The **triple (3-back-edge) residual** is now 1.1–3.3% (down from the
prior estimate of 8.3%), after correctly accounting for crossing pairs.

---

<!-- CHECK
# crossing_pair_formula: verify formula correctness and coverage taxonomy.
# For each (G,T) pair:
#   - Easy: some back edge has po2 depth-gap.
#   - Nested: some same-branch nested or same-vertex pair has po2 |delta1-delta2|+2.
#   - Crossing: some strict-crossing pair has po2 (da2-da1)+(ds2-ds1)+2.
#   - Triple: some 3-back-edge sym-diff is a po2 cycle.
#   - None: FAIL (chain_locality_r3 violated).
# Also verify: formula matches actual sym-diff cycle length for all crossing pairs.
import itertools, random, sys

rng = random.Random(20260730_15)

PO2_GAPS = {3, 7, 15, 31}
PO2_DIFF = {2, 6, 14, 30}   # 2^k-2 (nested and crossing po2 condition)


def make_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    return adj


def connected_cubic(n, edges):
    deg = [0]*n
    for u, v in edges: deg[u] += 1; deg[v] += 1
    if min(deg) < 3 or max(deg) > 3: return False
    adj = make_adj(n, edges)
    seen = {0}; stack = [0]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); stack.append(w)
    return len(seen) == n


def sample_cubic(n, rnd, tries=3000):
    for _ in range(tries):
        stubs = [v for v in range(n) for _ in range(3)]
        rnd.shuffle(stubs)
        edges = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i+1]
            if a == b or (min(a,b),max(a,b)) in edges: ok = False; break
            edges.add((min(a,b), max(a,b)))
        if not ok: continue
        el = list(edges)
        if connected_cubic(n, el): return el
    return None


def spanning_trees(n, edges, cap=20000):
    E = len(edges); trees = []
    for combo in itertools.combinations(range(E), n-1):
        parent = list(range(n))
        def find(a, p=parent):
            while p[a] != a: p[a] = p[p[a]]; a = p[a]
            return a
        ok = True
        for ei in combo:
            ru, rv = find(edges[ei][0]), find(edges[ei][1])
            if ru == rv: ok = False; break
            parent[ru] = rv
        if ok:
            trees.append(sum(1 << ei for ei in combo))
            if len(trees) > cap: return None
    return trees


def tremaux_root(n, edges, tm):
    adj_t = [[] for _ in range(n)]; nte = []
    for i, (u,v) in enumerate(edges):
        if tm >> i & 1: adj_t[u].append(v); adj_t[v].append(u)
        else: nte.append((u, v))
    for r in range(n):
        d = [-1]*n; par = [-1]*n; d[r] = 0; stk = [r]
        while stk:
            u = stk.pop()
            for w in adj_t[u]:
                if d[w] < 0 and w != par[u]:
                    d[w] = d[u]+1; par[w] = u; stk.append(w)
        ok = True
        for u, v in nte:
            a, b = (u,v) if d[u] <= d[v] else (v,u)
            if d[b] < 0: ok = False; break
            x = b
            while d[x] > d[a]: x = par[x]
            if x != a: ok = False; break
        if ok: return r, d, par
    return None, None, None


def cycle_len_of_edgeset(sym):
    adj = {}
    for u, v in sym:
        adj.setdefault(u, []).append(v); adj.setdefault(v, []).append(u)
    if not adj: return 0
    if any(len(vs) != 2 for vs in adj.values()): return None
    st = min(adj); fi = adj[st][0]; path = [st, fi]; pv = st; cu = fi
    while True:
        nxt = [w for w in adj[cu] if w != pv]
        if len(nxt) != 1: return None
        nxt = nxt[0]
        if nxt == st: break
        path.append(nxt); pv = cu; cu = nxt
    return len(path)


def is_anc(u, v, dep, prnt):
    x = v
    while dep[x] > dep[u]: x = prnt[x]
    return x == u


def fund_edges(s, a, par):
    e = set(); c = s
    while c != a: p = par[c]; e.add((min(c,p), max(c,p))); c = p
    e.add((min(s,a), max(s,a))); return e


def triple_po2(nt, par, depth):
    for (s1,a1,g1),(s2,a2,g2),(s3,a3,g3) in itertools.combinations(nt, 3):
        sym = (fund_edges(s1,a1,par)
               .symmetric_difference(fund_edges(s2,a2,par))
               .symmetric_difference(fund_edges(s3,a3,par)))
        cl = cycle_len_of_edgeset(sym)
        if cl in {4, 8, 16, 32}: return True
    return False


def check_coverage(name, n, edges_raw, all_trees=True, sample_roots=0):
    edges = [tuple(sorted(e)) for e in edges_raw]
    adj = make_adj(n, edges)

    if all_trees:
        trees = spanning_trees(n, edges)
        assert trees is not None, f"{name}: too many spanning trees"
    else:
        trees = None

    rnd = random.Random(rng.randrange(1 << 30))
    stats = {'easy': 0, 'nested': 0, 'crossing': 0, 'triple': 0, 'none': 0}
    formula_errors = []

    def process(tm):
        r0, depth, par = tremaux_root(n, edges, tm)
        if r0 is None: return
        nt = []
        for i, (u,v) in enumerate(edges):
            if not (tm >> i & 1):
                if depth[u] > depth[v]: nt.append((u,v,depth[u]-depth[v]))
                else: nt.append((v,u,depth[v]-depth[u]))

        # Easy
        if any(g in PO2_GAPS for _,_,g in nt):
            stats['easy'] += 1; return

        # Nested / same-vertex
        for (s1,a1,g1),(s2,a2,g2) in itertools.combinations(nt, 2):
            da1,ds1,da2,ds2 = depth[a1],depth[s1],depth[a2],depth[s2]
            nested = (da1<=da2 and ds2<=ds1) or (da2<=da1 and ds1<=ds2)
            if s1==s2 or nested:
                if abs(g1-g2)+2 in {4,8,16,32}:
                    stats['nested'] += 1; return

        # Crossing: strict dA < dA2 < dS < dS2 with same-branch ancestry
        for (s1,a1,g1),(s2,a2,g2) in itertools.combinations(nt, 2):
            da1,ds1,da2,ds2 = depth[a1],depth[s1],depth[a2],depth[s2]
            for dA,A,dS,S,dA2,A2,dS2,S2 in [
                    (da1,a1,ds1,s1,da2,a2,ds2,s2),
                    (da2,a2,ds2,s2,da1,a1,ds1,s1)]:
                if (dA < dA2 < dS < dS2
                        and is_anc(A2, S, depth, par)
                        and is_anc(S, S2, depth, par)):
                    offset = (dA2-dA)+(dS2-dS)
                    if offset in PO2_DIFF:
                        # Verify formula against actual sym-diff
                        e1 = fund_edges(s1,a1,par)
                        e2 = fund_edges(s2,a2,par)
                        sym = e1.symmetric_difference(e2)
                        actual = cycle_len_of_edgeset(sym)
                        expected = offset + 2
                        if actual != expected:
                            formula_errors.append((name, offset, actual, expected))
                        else:
                            stats['crossing'] += 1; return

        # Triple
        if triple_po2(nt, par, depth):
            stats['triple'] += 1; return

        stats['none'] += 1
        print(f"FAIL: {name} tm={tm} root={r0} gaps={sorted(g for _,_,g in nt)}",
              file=sys.stderr)

    if trees is not None:
        for tm in trees: process(tm)
    else:
        eidx = {(min(u,v),max(u,v)): i for i,(u,v) in enumerate(edges)}
        for _ in range(sample_roots):
            root = rnd.randrange(n)
            tm = 0; seen = [False]*n; seen[root] = True
            stk2 = [(root, iter(adj[root][:])), ]
            while stk2:
                u2, it2 = stk2[-1]; adv = False
                for w2 in it2:
                    if not seen[w2]:
                        seen[w2] = True
                        tm |= 1 << eidx[(min(u2,w2),max(u2,w2))]
                        stk2.append((w2, iter(adj[w2][:]))); adv = True; break
                if not adv: stk2.pop()
            process(tm)

    total = sum(stats.values())
    assert formula_errors == [], f"Crossing formula errors: {formula_errors[:3]}"
    assert stats['none'] == 0, f"{name}: {stats['none']} failures"
    print(f"{name} ({total} trees): easy={stats['easy']} nested={stats['nested']} "
          f"crossing={stats['crossing']} triple={stats['triple']}")
    return stats


CL_A = [(3,8),(2,4),(3,4),(5,8),(1,5),(3,7),(1,8),(0,9),(4,6),(7,9),(2,9),(6,7),(0,2),(0,5),(1,6)]
CL_B = [(0,7),(3,4),(2,7),(5,8),(6,8),(0,9),(6,7),(0,2),(4,5),(3,9),(4,8),(1,6),(2,5),(1,3),(1,9)]
CL_C = [(0,1),(3,4),(2,7),(1,5),(0,3),(4,6),(5,7),(4,5),(8,9),(0,2),(3,6),(6,9),(1,9),(7,8),(2,8)]
pet = [(i,(i+1)%5) for i in range(5)] + [(5+i,5+(i+2)%5) for i in range(5)] + [(i,i+5) for i in range(5)]

for nm, eg in [('CL_A',CL_A),('CL_B',CL_B),('CL_C',CL_C),('petersen',pet)]:
    check_coverage(nm, 10, eg, all_trees=True)

# Sampled cubics n=10,12
for nn in [10, 12]:
    rnd2 = random.Random(rng.randrange(1 << 30))
    for trial in range(6):
        eg2 = sample_cubic(nn, rnd2)
        if eg2 is None: continue
        check_coverage(f"cubic_n{nn}_t{trial}", nn, eg2, all_trees=False, sample_roots=100)
CHECK -->

## Summary

**Proved** (this lemma): For two back edges in strict crossing configuration
($d_{a_1}<d_{a_2}<d_{s_1}<d_{s_2}$), their fundamental-cycle sym-diff is
a simple cycle of length $(d_{a_2}-d_{a_1})+(d_{s_2}-d_{s_1})+2$.

**Correction**: The R6 "unified theorem" formula $|\delta_1-\delta_2|+2$ applies
only to nested and same-vertex pairs, NOT to crossing pairs.

**Updated taxonomy**: 4 mechanisms cover all tested cubic DFS trees. The
triple (3-back-edge) residual is now 1–3% of trees, down from the prior 8.3%
estimate that had incorrectly included crossing pairs.

**Open**: Prove that the 4-mechanism taxonomy covers 100% of all cubic DFS
trees (not just the tested instances). The crossing-pair po2 condition
$(d_{a_2}-d_{a_1})+(d_{s_2}-d_{s_1}) \in \{2,6,14,\ldots\}$ is a separate
existence claim from the nested and triple conditions.
