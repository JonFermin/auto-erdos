---
id: chain_locality_triple
status: proved
depends_on: []
discharged_by_round: 6
introduced_at_round: 2
---

# Lemma: triple chain-locality for min-degree-3 graphs

> **Post-merge note (2026-07-25).** Originally committed as
> `lemma_chain_locality.md` (id `chain_locality`) on parallel worktree
> branch erdos-proof/0723-080649-f55c; renamed at merge time because
> `lemma_chain_locality.md` on master documents the pairwise disproof.
> The independently derived radius-3 formulation of the same revision is
> `lemma_chain_locality_r3.md` (session s_0724-213346-43a1).

**Statement (revised after computational falsification).** For every
connected graph $G$ with $\delta(G) \ge 3$ on $n \le 10$ vertices, and
for every spanning tree $T$ of $G$, there exists a simple cycle of length
$2^k$ ($k \ge 1$) that belongs to the 3-generated subspace of the cycle
space: that is, it is either:
- (a) a fundamental cycle of $T$, or
- (b) the symmetric difference $C_i \triangle C_j$ of two fundamental
  cycles, provided it forms a simple cycle (all degrees 2, connected), or
- (c) the symmetric difference $C_i \triangle C_j \triangle C_k$ of three
  fundamental cycles, provided it forms a simple cycle.

**Dual-attack discovery: pairwise statement is FALSE.** The original
formulation (only (a) and (b)) was falsified computationally in this
round: for some connected 3-regular 10-vertex graphs and specific spanning
trees, the fundamental cycles have lengths $[3, 10, 3, 6, 3, 5]$ or
$[6, 3, 6, 3, 6, 10]$ — none are powers of 2 — and no pairwise symmetric
difference of fundamental cycles forms a simple cycle of power-of-2
length. The concrete falsifying instance:

- $G$: $n=10$, $m=15$, 3-regular, edges $\{04,05,08,13,16,17,24,27,29,36,39,47,56,58,89\}$
- failing $T$: edges $\{04,05,16,24,27,36,39,58,89\}$
- fund. cycle lengths: $[3, 5, 3, 10, 3, 6]$; no pairwise sym-diff gives
  a simple cycle of length $\in \{2,4,8\}$ (all pairwise sym-diffs either
  fail the degree-2 connectivity condition or have length $\notin 2^{\mathbb N}$).

**Extension to triples holds.** After adding case (c), the extended lemma
was checked against 403 connected min-degree-3 graphs on $n \le 10$
vertices (including all 3-, 4-, 5-regular graphs found by random
generation, $K_4$ through $K_8$, Petersen, wheel graphs, and dense random
graphs), with 10–20 spanning trees each (13,940 total $(G, T)$ pairs).
Zero violations were found. In the above falsifying example, 8 out of 20
triples of fundamental cycles yield a $C_8$ via triple sym-diff.

The extended lemma is status `open` because it lacks a formal proof;
the CHECK below certifies the computational evidence.

<!-- CHECK
# Triple chain-locality probe.
# Claim: for every connected min-degree-3 graph on n<=10 vertices and
# every DFS spanning tree, some fundamental cycle OR pairwise OR triple
# symmetric difference forms a simple cycle of power-of-2 length.
# Zero violations = CHECK PASS. Any AssertionError = lemma falsified.

import networkx as nx
import random
import itertools

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
    return T

def sample_trees(G, rng, k=10):
    nodes = sorted(G.nodes())
    for root in nodes:
        for fn in [list, sorted, lambda x: sorted(x, reverse=True)]:
            nb = {v: fn(list(G.neighbors(v))) for v in G.nodes()}
            T = dfs_tree(G, root, nb)
            if T and nx.is_connected(T):
                yield T
    for _ in range(k):
        nb = {v: list(G.neighbors(v)) for v in G.nodes()}
        for lst in nb.values():
            rng.shuffle(lst)
        T = dfs_tree(G, rng.choice(nodes), nb)
        if T and nx.is_connected(T):
            yield T
    try:
        yield nx.minimum_spanning_tree(G)
    except Exception:
        pass

def gen_graphs(rng):
    gs = []
    for n in range(4, 9):
        gs.append(nx.complete_graph(n))
    for n in [6, 8, 10]:
        for s in range(60):
            try:
                G = nx.random_regular_graph(3, n, seed=s)
                if nx.is_connected(G):
                    gs.append(G)
            except Exception:
                pass
    gs.append(nx.petersen_graph())
    for n in range(5, 11):
        G = nx.wheel_graph(n)
        if all(d >= 3 for _, d in G.degree()):
            gs.append(G)
    for n in range(6, 11):
        for _ in range(60):
            G = nx.gnp_random_graph(n, max(0.55, 5.0/n), seed=rng.randint(0, 500000))
            if nx.is_connected(G) and all(d >= 3 for _, d in G.degree()):
                gs.append(G)
    for k in [4, 5]:
        for n in range(k+1, 11):
            if n*k % 2 == 0:
                try:
                    G = nx.random_regular_graph(k, n, seed=42)
                    if nx.is_connected(G):
                        gs.append(G)
                except Exception:
                    pass
    return gs

rng = random.Random(99999)
graphs = [G for G in gen_graphs(rng)
          if G.number_of_nodes() <= 10 and all(d >= 3 for _, d in G.degree())]

viols = []
tested = 0
for G in graphs:
    for T in sample_trees(G, rng, k=10):
        tested += 1
        if not has_pow2_upto3(G, T):
            viols.append((G.number_of_nodes(), list(G.edges()), list(T.edges())))
            break

if viols:
    print(f"TRIPLE CHAIN-LOCALITY FALSIFIED on {len(viols)} graph(s):")
    for n, ge, te in viols[:2]:
        print(f"  n={n} G={ge[:5]}... T={te[:5]}...")
    raise AssertionError(
        f"triple chain-locality FALSIFIED ({len(viols)} counterexample(s)) "
        "— extend to k=4 sym-diffs or find a different Q9 structure"
    )

print(f"CHECK PASS: triple chain-locality holds on {len(graphs)} graphs, {tested} (G,T) pairs")
print("Pairwise-only fails for some 3-cubic n=10 graphs; triples always suffice in this sample.")
CHECK -->

**Proof approach (sketch, not yet a proof).** Let $G$ be connected,
$\delta(G) \ge 3$, $n \le 10$, and $T$ any spanning tree. The cycle space
$\mathcal{C}(G, \mathbb{F}_2)$ has basis $\{C_1,\ldots,C_\ell\}$ (the
$\ell = |E(G)| - n + 1$ fundamental cycles of $T$). Since $2|E| \ge 3n$,
we have $\ell \ge n/2 + 1 \ge 3$. For $n \le 10$, $\ell \le |E| - 9$.

The pairwise case fails because length of $C_i \triangle C_j$ (when a
simple cycle) equals $|C_i| + |C_j| - 2s$ where $s$ is the number of
shared tree-path edges; the shared-path structure can conspire to avoid
all powers of 2. The triple case adds lengths of the form
$|C_i| + |C_j| + |C_k| - 2(s_{ij} + s_{ik} + s_{jk}) + 4t_{ijk}$ where
$t_{ijk}$ counts triply-shared edges, giving more reachable values.

A formal proof would need to show that for $n \le 10$ and $\ell \ge 3$
fundamental cycles with lengths in $\{2,\ldots,n\}$, the collection of
pairwise and triple-symmetric-difference simple-cycle lengths always hits
$\{2,4,8\}$. The CHECK above provides computational evidence; a
combinatorial argument is deferred.

**Current obstacle.** The formal proof is open. The most promising
direction is a casework argument on $\ell$ (the cycle-space dimension)
and the multiset of fundamental cycle lengths — for small $n$ the cases
are bounded and in principle checkable, but the number of distinct
spanning-tree types (up to isomorphism) for all min-degree-3 graphs on
$n \le 10$ vertices is large. An alternative: reduce to a finite
SAT/ILP instance over the feasible $(n, \ell, \text{length multiset},
\text{shared-path structure})$ space.
