---
id: share1_c16_compose
status: proved
depends_on: []
discharged_by_round: 62
introduced_at_round: 62
---

# Lemma `share1_c16_compose` (PROVED — R62; stronger than the Q82 target)

**Claim (general cubic composition law).** Let $G$ be a cubic (simple)
graph and let $A, B$ be two distinct cycles of $G$ sharing exactly one
edge $uv$. Then $V(A) \cap V(B) = \{u, v\}$, and the symmetric
difference $A \triangle B$ is a single cycle of length $|A| + |B| - 2$.

**Corollary (the Q82(i) statement, and its payoff).** In a cubic graph
with girth $\ge 5$ and no $C_8$, two distinct $9$-cycles sharing
exactly one edge share no other vertex, and their sym-diff is a
$C_{16}$. Hence in a **$C_{16}$-free** class member, every pair of
distinct $9$-cycles shares $0$ or $\ge 2$ edges — in particular any two
$9$-cycles through a common edge share $\ge 2$ edges (per-edge
rigidity, landing exactly where `pendant_9_cap` died). Likewise
$9 \times 10$ share-$1$ pairs are impossible in a $C_{17}$-free member
and $10 \times 10$ in a $C_{18}$-free member.

**Note.** No girth or $C_8$-freeness is needed for the lemma itself:
cubicity alone does everything. The R61 first-order arc arithmetic
(the $18$ surviving quadruples $(a_1, a_2, b_1, b_2)$) analyzed a
configuration that **cannot occur in a cubic graph**: it posited an
extra shared vertex $w$ of arc-degree $4$, and $\deg_G(w) = 3$. The
$18$-window second-order program is hereby closed as vacuous.

## Proof

Let $A, B$ be distinct cycles with $E(A) \cap E(B) = \{uv\}$.

**Step 1 (no extra shared vertex).** Suppose
$w \in V(A) \cap V(B)$ with $w \notin \{u, v\}$. Cycle $A$ uses
exactly $2$ of the $3$ edges incident to $w$, and so does $B$. By
pigeonhole ($2 + 2 > 3$) there is an edge $f \ni w$ with
$f \in E(A) \cap E(B)$. Since $w \notin \{u, v\}$, $f \ne uv$, so
$|E(A) \cap E(B)| \ge 2$ — contradicting share-exactly-one. Hence
$V(A) \cap V(B) = \{u, v\}$.

**Step 2 (composition).** $P_A := A - uv$ and $P_B := B - uv$ are
$u$–$v$ paths of lengths $|A| - 1$ and $|B| - 1$ respectively, edge-
disjoint (the only shared edge was $uv$) and, by Step 1, internally
vertex-disjoint. The union of two internally-disjoint $u$–$v$ paths is
a single cycle, of length $(|A| - 1) + (|B| - 1) = |A| + |B| - 2$; and
$P_A \cup P_B = A \triangle B$ since $uv$ is the unique shared edge.
$\blacksquare$

For the corollary: two $9$-cycles give $|A| + |B| - 2 = 16$. If the
graph is $C_{16}$-free this is impossible, so no share-$1$ pair of
$9$-cycles exists, i.e. all pairs share $0$ or $\ge 2$ edges. The
$C_{17}$/$C_{18}$ variants are the same arithmetic. $\blacksquare$

## Empirical confirmation (dual-attack order respected: probes first)

Run this round BEFORE the proof was written up:

- **Exhaustive, all cubic graphs on $8$ vertices**: all $19{,}320$
  connected labeled cubic graphs, ALL cycle pairs sharing exactly one
  edge — $710{,}640$ pairs — have no extra shared vertex and
  single-cycle sym-diff of length $|A| + |B| - 2$ (CHECK 1, ~10 s).
  This covers every cycle-length combination realizable at $n = 8$,
  including graphs of girth $3$ and $4$ — confirming the hypothesis-free
  form of the lemma.
- **The R57 pin** ($n = 28$, girth $5$, $C_8$-free): all share-$1$
  pairs from $\{9, 10\}$-cycles — $154$ ($9 \times 9$) $+ 462$
  ($9 \times 10$) $+ 350$ ($10 \times 10$) $= 966$ pairs, exactly the
  R61 counts — compose (CHECK 2). The R61 measurement $3{,}738/3{,}738$
  across all five known class members is now explained, not just
  observed.

## What this changes (handoff to the counting layer, Q83)

`c8free_c16_floor` now has a proof mechanism with one leg rigorous:
any $\{C_4, C_8, C_{16}\}$-free cubic graph has all $9$-cycle pairs
sharing $0$ or $\ge 2$ edges. The remaining question is purely
extremal: **how large can a family of $9$-cycles pairwise sharing
$0$ or $\ge 2$ edges be on $3n/2$ edges, given girth $\ge 5$ and
$C_8$-freeness — and how many $9$-cycles must a class member at
$30 \le n \le 32$ have?** The pin realizes share-$1$ freely ($154$
pairs among its $34$ nine-cycles); a $C_{16}$-free member must have a
share-$1$-free $9$-cycle family. Note the floor question does NOT
follow from this lemma alone: a class member with few or no $9$-cycles
evades the mechanism, so the counting layer must couple to a supply
lower bound (the criticality-side witness supply of R60, or a direct
counting argument).

<!-- CHECK
# CHECK 1 — exhaustive over ALL 19,320 connected labeled cubic graphs
# on 8 vertices: every pair of cycles sharing exactly one edge has no
# extra shared vertex and single-cycle sym-diff of length |A|+|B|-2.
# ~10 s. Also validates the enumerator (19,320 count) and covers girth
# 3/4 graphs, confirming the lemma needs no girth/C8 hypothesis.
import itertools
from collections import deque

def bfs_dist(adj, n, s):
    d = [n+1]*n; d[s] = 0; q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] > d[v] + 1:
                d[w] = d[v] + 1; q.append(w)
    return d

def all_cycles(adj, n, Lmax):
    out = []
    for s in range(n):
        dist = bfs_dist(adj, n, s)
        stack = [(u, (1 << s) | (1 << u), [s, u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) >= 3 and path[1] < path[-1]:
                        out.append(frozenset(
                            frozenset((path[i], path[(i+1) % len(path)]))
                            for i in range(len(path))))
                    continue
                if w < s or (mask >> w) & 1:
                    continue
                if len(path) + dist[w] >= Lmax:
                    continue
                stack.append((w, mask | (1 << w), path + [w]))
    return out

def is_single_cycle(edges):
    deg = {}
    for e in edges:
        for v in e: deg[v] = deg.get(v, 0) + 1
    if any(d != 2 for d in deg.values()): return False
    verts = list(deg)
    nbr = {v: [] for v in verts}
    for e in edges:
        a, b = tuple(e); nbr[a].append(b); nbr[b].append(a)
    seen = {verts[0]}; q = deque([verts[0]])
    while q:
        v = q.popleft()
        for w in nbr[v]:
            if w not in seen: seen.add(w); q.append(w)
    return len(seen) == len(verts)

def check_graph(adj, n, Lmax):
    cycles = all_cycles(adj, n, Lmax)
    k = 0
    for A, B in itertools.combinations(cycles, 2):
        shared = A & B
        if len(shared) != 1: continue
        k += 1
        VA = set(v for e in A for v in e); VB = set(v for e in B for v in e)
        uv = set(next(iter(shared)))
        assert not ((VA & VB) - uv), (adj, sorted(map(sorted, A)), sorted(map(sorted, B)))
        sd = A ^ B
        assert is_single_cycle(sd) and len(sd) == len(A) + len(B) - 2, \
            (adj, sorted(map(sorted, A)), sorted(map(sorted, B)))
    return k

def is_connected(adj, n):
    seen = [False]*n; seen[0] = True; q = deque([0]); c = 1
    while q:
        v = q.popleft()
        for w in adj[v]:
            if not seen[w]: seen[w] = True; c += 1; q.append(w)
    return c == n

total = 0; pairs_total = 0
def rec(adj, v):
    global total, pairs_total
    if v == 8:
        if is_connected(adj, 8):
            global_counts = check_graph(adj, 8, 9)
            total += 1
            pairs_total += global_counts
        return
    need = 3 - len(adj[v])
    if need == 0:
        rec(adj, v + 1); return
    cands = [w for w in range(v + 1, 8) if len(adj[w]) < 3 and w not in adj[v]]
    for combo in itertools.combinations(cands, need):
        for w in combo: adj[v].append(w); adj[w].append(v)
        rec(adj, v + 1)
        for w in combo: adj[v].pop(); adj[w].remove(v)
rec([[] for _ in range(8)], 0)
assert total == 19320, total
assert pairs_total == 710640, pairs_total
CHECK -->

<!-- CHECK
# CHECK 2 — the R57 pin: every share-1 pair from {9,10}-cycles has no
# extra shared vertex and composes; pair counts must be exactly the
# R61-measured 154/462/350 (9x9 / 9x10 / 10x10).
import itertools
from collections import deque

def bfs_dist(adj, n, s):
    d = [n+1]*n; d[s] = 0; q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] > d[v] + 1:
                d[w] = d[v] + 1; q.append(w)
    return d

def all_cycles(adj, n, Lmax):
    out = []
    for s in range(n):
        dist = bfs_dist(adj, n, s)
        stack = [(u, (1 << s) | (1 << u), [s, u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) >= 3 and path[1] < path[-1]:
                        out.append(frozenset(
                            frozenset((path[i], path[(i+1) % len(path)]))
                            for i in range(len(path))))
                    continue
                if w < s or (mask >> w) & 1:
                    continue
                if len(path) + dist[w] >= Lmax:
                    continue
                stack.append((w, mask | (1 << w), path + [w]))
    return out

def is_single_cycle(edges):
    deg = {}
    for e in edges:
        for v in e: deg[v] = deg.get(v, 0) + 1
    if any(d != 2 for d in deg.values()): return False
    verts = list(deg)
    nbr = {v: [] for v in verts}
    for e in edges:
        a, b = tuple(e); nbr[a].append(b); nbr[b].append(a)
    seen = {verts[0]}; q = deque([verts[0]])
    while q:
        v = q.popleft()
        for w in nbr[v]:
            if w not in seen: seen.add(w); q.append(w)
    return len(seen) == len(verts)

E28 = [(0, 11), (0, 19), (0, 27), (1, 17), (1, 19), (1, 21), (2, 9), (2, 13),
       (2, 14), (3, 22), (3, 24), (3, 25), (4, 5), (4, 7), (4, 26), (5, 14),
       (5, 18), (6, 7), (6, 8), (6, 20), (7, 13), (8, 14), (8, 25), (9, 17),
       (9, 24), (10, 16), (10, 21), (10, 27), (11, 15), (11, 16), (12, 19),
       (12, 23), (12, 26), (13, 18), (15, 22), (15, 26), (16, 25), (17, 23),
       (18, 23), (20, 21), (20, 24), (22, 27)]
adj = [[] for _ in range(28)]
for u, v in E28: adj[u].append(v); adj[v].append(u)
cyc = [c for c in all_cycles(adj, 28, 11) if len(c) in (9, 10)]
assert sum(1 for c in cyc if len(c) == 9) == 34
assert sum(1 for c in cyc if len(c) == 10) == 56
counts = {(9, 9): 0, (9, 10): 0, (10, 10): 0}
for A, B in itertools.combinations(cyc, 2):
    shared = A & B
    if len(shared) != 1: continue
    VA = set(v for e in A for v in e); VB = set(v for e in B for v in e)
    uv = set(next(iter(shared)))
    assert not ((VA & VB) - uv)
    sd = A ^ B
    assert is_single_cycle(sd) and len(sd) == len(A) + len(B) - 2
    counts[tuple(sorted((len(A), len(B))))] += 1
assert counts == {(9, 9): 154, (9, 10): 462, (10, 10): 350}, counts
CHECK -->
