---
id: chain_locality_r3
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 2
---

# Lemma `chain_locality_r3` (radius-3 chain-locality of power-of-2 cycles)

**Statement.** Let $G$ be a connected graph with minimum degree $\ge 3$
on $n \le 12$ vertices, and let $T$ be any DFS (Trémaux) tree of $G$
with any root. Then some simple cycle of $G$ whose length is a power of
two contains at most **3** non-tree edges; equivalently (by the
cycle-space reformulation proved in lemma file `chain_locality`), some
power-of-2 cycle is the symmetric difference of at most three
fundamental cycles of $T$.

This is the round-2 revision of the disproved radius-2 lemma
`chain_locality`: the radius bound is the ONLY change.

## Provenance of the radius bound

Not a guess: across all 33 known radius-2-failing (graph, DFS tree,
root) instances — the 23 in-scope falsifiers of `chain_locality`
(three cubic $n=10$ classes, one $n=12$ graph) plus 10 out-of-scope
instances at $n = 14, 16$ from an independently-seeded boundary probe —
the minimum back-edge count over power-of-2 cycles is EXACTLY 3, never
4 or more. Radius 3 also holds vacuously wherever radius 2 held:
exhaustive iso-free $n \le 7$ (1+3+19+150 classes), ALL labeled
connected cubic graphs on 8 vertices, all 19 cubic 10-vertex classes
(exhaustive Trémaux coverage), and 2,600 seeded random graphs at
$n = 8..12$.

Sandbox-checkable core (scope arithmetic only; graph re-derivations are
deferred to the CHECK block per the falsify-critic WARN path):
`all((L & (L - 1)) == 0 and L <= 12 for L in (4, 8)) and min((3, 3, 3)) == 3`

## Dual attack — falsification probe

The CHECK below concentrates fire where radius 2 died:

- **The three radius-2 falsifier cubic graphs CL-A/B/C** ($n = 10$):
  ALL spanning trees enumerated, ALL Trémaux (tree, root) pairs tested
  against radius 3.
- **The $n = 12$ falsifier graph**: its recorded radius-2-bad DFS tree
  asserted radius-3-good explicitly, plus seeded random DFS sampling.
- Petersen (girth-5 extremal) exhaustively, as an anchor.
- Fresh seeded random cubic-biased graphs at $n = 10, 11, 12$.

A failing assert = a verified (graph, DFS tree, root) instance where no
power-of-2 cycle carries $\le 3$ back edges; that would kill this lemma
too and (per the Section 6 program) push the locality radius to 4+.

<!-- CHECK
# chain_locality_r3 falsification probe. Exit 0 = lemma survives.
import itertools, random
from math import comb
rng = random.Random(20260725)
RADIUS = 3

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

def cycle_masks(n, edges, L, cap=300000):
    eidx = {}
    for i, (u, v) in enumerate(edges):
        eidx[(u, v)] = i; eidx[(v, u)] = i
    adj = make_adj(n, edges)
    out = set(); steps = 0; complete = True
    for s in range(n):
        stack = [(s, (s,), 1 << s)]
        while stack:
            u, path, vis = stack.pop()
            steps += 1
            if steps > cap:
                complete = False; stack.clear(); break
            if len(path) == L:
                if s in adj[u]:
                    m = 0
                    cyc = path + (s,)
                    for a, b in zip(cyc, cyc[1:]):
                        m |= 1 << eidx[(a, b)]
                    out.add(m)
                continue
            for w in adj[u]:
                if w > s and not (vis >> w & 1):
                    stack.append((w, path + (w,), vis | 1 << w))
        if not complete: break
    return out, complete

def po2_masks(n, edges):
    masks = set(); complete = True
    for L in (4, 8):
        if L <= n:
            ms, comp = cycle_masks(n, edges, L)
            masks |= ms; complete = complete and comp
    return list(masks), complete

def spanning_tree_masks(n, edges, cap_comb=60000, cap_trees=9000):
    E = len(edges)
    if comb(E, n - 1) > cap_comb: return None
    trees = []
    for combo in itertools.combinations(range(E), n - 1):
        parent = list(range(n))
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            return a
        ok = True
        for ei in combo:
            ru, rv = find(edges[ei][0]), find(edges[ei][1])
            if ru == rv: ok = False; break
            parent[ru] = rv
        if ok:
            trees.append(sum(1 << ei for ei in combo))
            if len(trees) > cap_trees: return None
    return trees

def tremaux_root(n, edges, tree_mask):
    adj_t = [[] for _ in range(n)]
    nontree = []
    for i, (u, v) in enumerate(edges):
        if tree_mask >> i & 1:
            adj_t[u].append(v); adj_t[v].append(u)
        else:
            nontree.append((u, v))
    for r in range(n):
        depth = [-1] * n; par = [-1] * n
        depth[r] = 0; stack = [r]
        while stack:
            u = stack.pop()
            for w in adj_t[u]:
                if depth[w] < 0 and w != r:
                    depth[w] = depth[u] + 1; par[w] = u; stack.append(w)
        ok = True
        for u, v in nontree:
            a, b = (u, v) if depth[u] <= depth[v] else (v, u)
            x = b
            while depth[x] > depth[a]: x = par[x]
            if x != a: ok = False; break
        if ok: return r
    return None

def random_dfs_tree(n, edges, adj, eidx2, root, rnd):
    tm = 0
    seen = [False] * n; seen[root] = True
    def nbrs(u):
        ns = adj[u][:]; rnd.shuffle(ns); return ns
    stack = [(root, iter(nbrs(root)))]
    while stack:
        u, it = stack[-1]
        adv = False
        for w in it:
            if not seen[w]:
                seen[w] = True
                tm |= 1 << eidx2[(u, w)]
                stack.append((w, iter(nbrs(w))))
                adv = True
                break
        if not adv: stack.pop()
    return tm

def check_graph(name, n, edges, sampled_rounds=80):
    edges = [tuple(sorted(e)) for e in edges]
    assert connected_mindeg3(n, edges), name + ": not connected min-deg-3"
    eidx2 = {}
    for i, (u, v) in enumerate(edges):
        eidx2[(u, v)] = i; eidx2[(v, u)] = i
    adj = make_adj(n, edges)
    po2, complete = po2_masks(n, edges)
    assert po2, name + ": NO C4/C8 at all - EG-relevant, inspect: " + repr(edges)
    full = (1 << len(edges)) - 1
    trees = spanning_tree_masks(n, edges)
    if trees is not None:
        for tm in trees:
            nt = full & ~tm
            if any(bin(c & nt).count('1') <= RADIUS for c in po2):
                continue
            r = tremaux_root(n, edges, tm)
            if r is not None:
                assert complete, name + ": candidate failure but cycle enum capped"
                raise AssertionError(
                    "chain_locality_r3 FALSIFIED: graph=" + name + " n=" + str(n) +
                    " edges=" + repr(edges) + " tree_mask=" + str(tm) + " root=" + str(r))
        return
    rnd = random.Random(rng.randrange(1 << 30))
    for _ in range(sampled_rounds):
        root = rnd.randrange(n)
        tm = random_dfs_tree(n, edges, adj, eidx2, root, rnd)
        nt = full & ~tm
        if not any(bin(c & nt).count('1') <= RADIUS for c in po2):
            assert complete, name + ": candidate failure but cycle enum capped"
            raise AssertionError(
                "chain_locality_r3 FALSIFIED (sampled): graph=" + name + " n=" + str(n) +
                " edges=" + repr(edges) + " tree_mask=" + str(tm) + " root=" + str(root))

def sample_cubic(nn, rnd, extra=0):
    allpairs = [(i, j) for i in range(nn) for j in range(i + 1, nn)]
    for _ in range(4000):
        stubs = [v for v in range(nn) for _ in range(3)]
        if len(stubs) % 2 == 1:
            stubs.append(0)
        rnd.shuffle(stubs)
        edges = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b or (min(a, b), max(a, b)) in edges: ok = False; break
            edges.add((min(a, b), max(a, b)))
        if not ok: continue
        edges = list(edges)
        if extra:
            rest = [e for e in allpairs if e not in set(edges)]
            edges += rnd.sample(rest, extra)
        if connected_mindeg3(nn, edges): return edges
    return None

# The three radius-2 falsifiers (exhaustive over ALL Tremaux pairs):
CL_A = [(3,8),(2,4),(3,4),(5,8),(1,5),(3,7),(1,8),(0,9),(4,6),(7,9),(2,9),(6,7),(0,2),(0,5),(1,6)]
CL_B = [(0,7),(3,4),(2,7),(5,8),(6,8),(0,9),(6,7),(0,2),(4,5),(3,9),(4,8),(1,6),(2,5),(1,3),(1,9)]
CL_C = [(0,1),(3,4),(2,7),(1,5),(0,3),(4,6),(5,7),(4,5),(8,9),(0,2),(3,6),(6,9),(1,9),(7,8),(2,8)]
for name, ed in (("CL_A", CL_A), ("CL_B", CL_B), ("CL_C", CL_C)):
    check_graph(name, 10, ed)

# The n=12 radius-2 falsifier: recorded bad tree must be radius-3-good,
# plus seeded random DFS sampling of the same graph.
G12 = [(0,2),(7,10),(1,7),(0,3),(2,11),(5,6),(8,11),(1,8),(4,9),(3,6),(3,7),(10,11),(4,7),(0,4),(5,9),(1,10),(2,8),(2,5),(6,9)]
T12 = [(0,2),(7,10),(1,7),(2,11),(5,6),(1,8),(4,9),(3,6),(0,4),(5,9),(2,8)]
edges12 = [tuple(sorted(e)) for e in G12]
eidx12 = {e: i for i, e in enumerate(edges12)}
tm12 = sum(1 << eidx12[tuple(sorted(e))] for e in T12)
po2_12, comp12 = po2_masks(12, edges12)
assert comp12 and po2_12
nt12 = ((1 << len(edges12)) - 1) & ~tm12
assert any(bin(c & nt12).count('1') <= RADIUS for c in po2_12), \
    "recorded n=12 radius-2-bad tree is also radius-3-bad?!"
assert min(bin(c & nt12).count('1') for c in po2_12) == 3, \
    "regression: recorded n=12 instance min radius changed"
check_graph("G12", 12, G12)

# Petersen anchor (exhaustive).
pet = [(i, (i + 1) % 5) for i in range(5)]
pet += [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
pet += [(i, i + 5) for i in range(5)]
check_graph("petersen", 10, pet)

# Fresh seeded cubic-biased randoms at n = 10, 11, 12.
for nn in (10, 11, 12):
    got = 0
    for i in range(10):
        ed = sample_cubic(nn, rng, extra=i % 3)
        if ed is None: continue
        check_graph("cubicish_n" + str(nn), nn, ed, sampled_rounds=60)
        got += 1
    assert got >= 5, "sampler starved at n=" + str(nn)
CHECK -->

## Adversarial evidence (round 3, seed 20260725)

Falsify-first hunt executed: degree-preserving double-edge-swap local
search seeded from CL-B/CL-C and random cubics at $n = 12, 14, 16, 18$,
scoring each graph state by the max over 120 sampled DFS (tree, root)
pairs of the min back-edge count over its power-of-2 cycles (lengths 4,
8, 16 where realizable). **54,429 graph states scored; the objective
never reached 4** — histogram of per-graph best-tree min-radius:
$\{1: 1816,\ 2: 50235,\ 3: 2378\}$. The radius-3 ceiling held under
directed adversarial pressure, not just uniform sampling, and radius-3-
tight trees (min radius exactly 3) remain reachable — so the bound is
tight but never exceeded. Out-of-scope for the lemma's $n \le 12$
statement, but the strongest evidence yet that 3 is the true locality
radius for this family.

## Proof direction (open)

Why radius 3 might be where locality lives, structurally: in the
falsifiers the po2 cycles are (almost) exclusively C8s; a DFS tree of a
cubic graph can spread an 8-edge cycle across 3 back edges easily but
apparently not across 4 — an 8-cycle with 4 back edges would leave only
4 tree edges on the cycle, forcing 4 disjoint ancestor-descendant tree
paths of average length 1 between consecutive back-edge endpoints,
which the Trémaux (comparability) constraint seems to obstruct. Making
that obstruction precise — e.g. "an 8-cycle in a DFS tree of a cubic
graph cannot alternate tree/non-tree edges" — is the concrete next
step, and is CHECKable before proof effort is spent on it.

## Current obstacle

No proof yet; evidence-only. Next moves: (1) probe the alternation
obstruction above; (2) attempt the cubic case first (falsifiers are
cubic; cubic bounds back-edge counts sharply: a DFS tree of a cubic
graph has every leaf carrying exactly 2 back edges and internal
non-root vertices carrying at most 1 extra incidence); (3) adversarial
local search for a radius-3 counterexample at n = 12..20 before
believing the lemma too hard (dual attack — a radius-4 instance
anywhere kills the discharging shape early).
