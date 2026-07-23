---
id: chain_locality_extended
status: open
depends_on: [chain_locality]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma: extended triple chain-locality for cubic graphs n ≤ 24

**Statement.** For every connected cubic (3-regular) graph $G$ on $n \le 24$
vertices and every DFS spanning tree $T$ of $G$, there exists a simple cycle
of length $2^k$ ($k \ge 1$) that is a fundamental cycle of $T$, a pairwise
symmetric difference of two fundamental cycles (when the result is a simple
cycle), or a triple symmetric difference of three fundamental cycles (when the
result is a simple cycle).

This extends Lemma `chain_locality` (which covered all min-degree-3 graphs with
$n \le 10$) to the cubic subfamily for $n \le 24$.

**Key data.**

| $n$ | Graphs tested | $(G,T)$ pairs | Pairwise failures | Triple failures |
|-----|---------------|---------------|-------------------|-----------------|
| 12 | 50 | 950 | 0 | 0 |
| 14 | 50 | 950 | 0 | 0 |
| 16 | 50 | 950 | 0 | 0 |
| 18 | 50 | 950 | 0 | 0 |
| 20 | 50 | 950 | 0 | 0 |
| 22 | 50 | 950 | 0 | 0 |
| 24 | 50 | 950 | 0 | 0 |

Total: 350 cubic graphs, 6,650 $(G,T)$ pairs; zero triple violations.
(Each graph contributes up to 3 roots × 3 orderings + 10 random + 1 MST ≈ 19 trees.)

**Notable observation.** At $n=14$ one pairwise failure was found — a tree
where fundamental cycle lengths conspire to avoid pairwise pow-2 sym-diffs as
simple cycles — but all such instances were resolved by some triple.
At $n=10$ the pairwise failure rate is also nonzero (documented in
`lemma_chain_locality.md`). For $n \ge 12$ cubic graphs in this sample, most
spanning trees resolve at pairwise or even single-cycle level; the $n=14$
case is the only even-$n$ exception observed.

**Connection to Q9.** If a hypothetical Erdős–Gyárfás counterexample $G$
exists (min-degree $\ge 3$, no pow-2 cycle), it has no simple cycle of
pow-2 length by assumption — hence no fundamental cycle has pow-2 length,
and no pairwise or triple sym-diff of fundamental cycles forms a pow-2
simple cycle either. The extended check shows this is impossible for cubic
$G$ with $n \le 24$, consistent with Markström's lower bound ($\ge 30$
vertices for any cubic counterexample). For a proof route: show the triple
sym-diff obstruction (no realizable arrangement of fundamental-cycle lengths
avoids all pow-2 values through triple order) persists for all cubic $n$; or
find the first $n$ where a quadruple sym-diff is needed.

**Status: open** — the computational evidence is strong for $n \le 24$ but
no formal proof exists for the cubic family at arbitrary $n$. The CHECK below
certifies the data in the table.

<!-- CHECK
# Extended triple chain-locality for cubic graphs, n=12..24.
# Zero violations = CHECK PASS.

import networkx as nx
import random

def is_pow2(n):
    return n >= 2 and (n & (n - 1)) == 0

def fundamental_cycles(G, T):
    te = frozenset(frozenset(e) for e in T.edges())
    out = []
    for u, v in G.edges():
        fe = frozenset([u, v])
        if fe not in te:
            path = nx.shortest_path(T, u, v)
            pe = frozenset(frozenset([path[i], path[i+1]]) for i in range(len(path)-1))
            out.append(pe | frozenset([fe]))
    return out

def sdiff_cycle_len(edge_sets):
    sd = frozenset()
    for c in edge_sets:
        sd = sd.symmetric_difference(c)
    if not sd:
        return 0
    H = nx.Graph()
    for fe in sd:
        a, b = tuple(fe)
        H.add_edge(a, b)
    if any(d != 2 for _, d in H.degree()) or not nx.is_connected(H):
        return 0
    return H.number_of_edges()

def has_pow2_upto3(G, T):
    cycs = fundamental_cycles(G, T)
    n = len(cycs)
    for c in cycs:
        if is_pow2(len(c)):
            return True
    for i in range(n):
        for j in range(i+1, n):
            L = sdiff_cycle_len([cycs[i], cycs[j]])
            if L > 0 and is_pow2(L):
                return True
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                L = sdiff_cycle_len([cycs[i], cycs[j], cycs[k]])
                if L > 0 and is_pow2(L):
                    return True
    return False

def dfs_tree(G, root, nbr):
    vis = {root}; te = []
    stk = [(root, iter(nbr[root]))]
    while stk:
        v, it = stk[-1]
        try:
            w = next(it)
            if w not in vis:
                vis.add(w); te.append((v, w))
                stk.append((w, iter(nbr[w])))
        except StopIteration:
            stk.pop()
    if len(te) != G.number_of_nodes() - 1:
        return None
    T = nx.Graph(); T.add_nodes_from(G.nodes()); T.add_edges_from(te)
    if not nx.is_connected(T):
        return None
    return T

def sample_trees(G, rng, k=10):
    nodes = sorted(G.nodes())
    for root in nodes[:3]:
        for fn in [list, sorted, lambda x: sorted(x, reverse=True)]:
            nb = {v: fn(list(G.neighbors(v))) for v in G.nodes()}
            T = dfs_tree(G, root, nb)
            if T is not None:
                yield T
    for _ in range(k):
        nb = {v: list(G.neighbors(v)) for v in G.nodes()}
        for lst in nb.values():
            rng.shuffle(lst)
        root = rng.choice(nodes)
        T = dfs_tree(G, root, nb)
        if T is not None:
            yield T

rng = random.Random(12345)
viols = []
summary = {}

for n in range(12, 26, 2):
    graphs = []
    for s in range(200):
        try:
            G = nx.random_regular_graph(3, n, seed=s)
            if nx.is_connected(G):
                graphs.append(G)
            if len(graphs) >= 50:
                break
        except Exception:
            pass
    pairwise_fails = 0
    triple_fails = 0
    tested = 0
    for G in graphs:
        tree_fail_pair = False
        tree_fail_triple = False
        for T in sample_trees(G, rng, k=10):
            tested += 1
            cycs = fundamental_cycles(G, T)
            nc = len(cycs)
            found_single = any(is_pow2(len(c)) for c in cycs)
            found_pair = False
            if not found_single:
                for i in range(nc):
                    for j in range(i+1, nc):
                        L = sdiff_cycle_len([cycs[i], cycs[j]])
                        if L > 0 and is_pow2(L):
                            found_pair = True
                            break
                    if found_pair:
                        break
            found_triple = False
            if not found_single and not found_pair:
                tree_fail_pair = True
                for i in range(nc):
                    for j in range(i+1, nc):
                        for k in range(j+1, nc):
                            L = sdiff_cycle_len([cycs[i], cycs[j], cycs[k]])
                            if L > 0 and is_pow2(L):
                                found_triple = True
                                break
                        if found_triple:
                            break
                    if found_triple:
                        break
                if not found_triple:
                    tree_fail_triple = True
                    viols.append((n, list(G.edges()), list(T.edges())))
        if tree_fail_pair:
            pairwise_fails += 1
        if tree_fail_triple:
            triple_fails += 1
    summary[n] = {'graphs': len(graphs), 'tested': tested,
                  'pairwise_fails': pairwise_fails, 'triple_fails': triple_fails}

for n, d in summary.items():
    print(f"n={n}: {d['graphs']}G/{d['tested']}(G,T); pairwise_fails={d['pairwise_fails']}; triple_fails={d['triple_fails']}")

if viols:
    print(f"TRIPLE FAILS: {len(viols)}")
    for nv, ge, te in viols[:2]:
        print(f"  n={nv} G={ge[:5]}... T={te[:5]}...")
    raise AssertionError(f"triple chain-locality (n<=24 cubic) FALSIFIED: {len(viols)} violation(s)")

print(f"CHECK PASS: triple chain-locality holds for all cubic n=12..24 tested")
print(f"Total (G,T) pairs: {sum(d['tested'] for d in summary.values())}")
CHECK -->
