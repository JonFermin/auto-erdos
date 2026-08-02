---
id: triple_parity
status: proved
depends_on: [crossing_offset_parity]
discharged_by_round: 18
introduced_at_round: 18
---

# Lemma `triple_parity` (parity constraint on the triple mechanism)

**Setting.** $T$ is a DFS spanning tree of a graph $G$; for a back edge
$B_i = (s_i, a_i)$, its fundamental cycle $C_i$ consists of $B_i$ together
with the tree path from $s_i$ up to $a_i$, so $|C_i| = \operatorname{gap}(B_i) + 1$
where $\operatorname{gap}(B_i) = d(s_i) - d(a_i)$.

**Statement.** Let $B_1, B_2, B_3$ be three distinct back edges of $T$ with
fundamental cycles $C_1, C_2, C_3$ (as edge sets), and let
$S = C_1 \triangle C_2 \triangle C_3$ be their symmetric difference. Then:

1. **(Back edges survive.)** All three back edges $B_1, B_2, B_3$ lie in $S$.
2. **(Size parity.)**
   $$|S| \;\equiv\; \operatorname{gap}(B_1) + \operatorname{gap}(B_2) + \operatorname{gap}(B_3) + 1 \pmod 2.$$
3. **(Firing parity.)** If $S$ is a single simple cycle whose length is a
   power of $2$ (the triple mechanism fires), then
   $\operatorname{gap}(B_1) + \operatorname{gap}(B_2) + \operatorname{gap}(B_3)$ is **odd** —
   i.e. the triple contains an **odd number of odd-gap back edges** (one or three).

**Proof.**

(1) Each back edge $B_i$ is a non-tree edge, and it belongs to exactly one of
the three fundamental cycles, namely its own $C_i$ (the other two fundamental
cycles consist of a different back edge plus tree edges). An element belonging
to exactly one of three sets survives their symmetric difference. $\square$

(2) For finite sets, $|A \triangle B| = |A| + |B| - 2|A \cap B| \equiv |A| + |B| \pmod 2$,
and iterating, $|C_1 \triangle C_2 \triangle C_3| \equiv |C_1|+|C_2|+|C_3| \pmod 2$.
Substituting $|C_i| = \operatorname{gap}(B_i)+1$ gives
$|S| \equiv \sum_i \operatorname{gap}(B_i) + 3 \equiv \sum_i \operatorname{gap}(B_i) + 1 \pmod 2$. $\square$

(3) Powers of $2$ that are cycle lengths ($4, 8, 16, 32, \ldots$) are even, so
firing forces $|S|$ even; by (2) this forces $\sum_i \operatorname{gap}(B_i)$ odd.
An integer sum of three terms is odd iff an odd number of the terms is odd. $\square$

**Corollary 1 (all-even-gap trees: triple is vacuous).** If every back edge of
$T$ has even depth-gap, then every 3-subset has even gap-sum, so the triple
mechanism **never fires**. Combined with the easy mechanism being vacuous there
(PO2 gaps $\{3,7,15,31,\ldots\}$ are all odd), coverage of all-even-gap trees
must come from **nested or crossing alone**.

**Corollary 2 (full parity accounting).** Writing $O$/$E$ for the odd-/even-gap
back edges, the four mechanisms are parity-restricted as follows:

| Mechanism | fires only from | reason |
|---|---|---|
| easy | $O$ (gap $\in \{3,7,15,31\}$) | PO2 gaps are odd |
| nested | $O$-$O$ or $E$-$E$ pairs | diff must be even ($\in \{2,6,14,30\}$) |
| crossing | $O$-$O$ or $E$-$E$ pairs | Lemma `crossing_offset_parity` |
| triple | $OOO$, $OEE$ triples | this lemma |

In particular a mixed tree's coverage burden splits: pair mechanisms live
inside the parity classes; the triple mechanism is the only one that can
combine both classes ($OEE$), which explains why the crossing-failed residual
trees (empirically all mixed-parity, see `residual_parity_census`) are the
ones that need it.

**Corollary 3 (search-space reduction).** In coverage verification, triples
with even gap-sum can be pruned before computing any symmetric difference
(a $\ge 2\times$ reduction; on random gap profiles half of all triples).

---

<!-- CHECK
# triple_parity: verify (1) back edges survive every 3-way sym-diff,
# (2) the size-parity formula, (3) no firing triple has even gap-sum,
# (4) in all-even-gap trees no triple fires, on sampled cubic DFS trees.
import random

PO2_LENS = {4, 8, 16, 32}


def sample_cubic(nn, rnd, tries=3000):
    for _ in range(tries):
        stubs = [v for v in range(nn) for _ in range(3)]
        rnd.shuffle(stubs)
        edges = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b or (min(a, b), max(a, b)) in edges:
                ok = False; break
            edges.add((min(a, b), max(a, b)))
        if not ok: continue
        el = list(edges)
        deg = [0] * nn
        for a, b in el: deg[a] += 1; deg[b] += 1
        if min(deg) == 3 and max(deg) == 3:
            adj = [[] for _ in range(nn)]
            for a, b in el: adj[a].append(b); adj[b].append(a)
            seen = {0}; stack = [0]
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if w not in seen: seen.add(w); stack.append(w)
            if len(seen) == nn: return el
    return None


def is_ancestor(u, v, depth, par):
    if depth[u] > depth[v]: return False
    x = v
    while depth[x] > depth[u]: x = par[x]
    return x == u


def dfs_tree(n, edges, r, shuffled_adj):
    depth = [-1] * n; par = [-1] * n
    depth[r] = 0; visited = [False] * n; visited[r] = True
    stack = [(r, iter(shuffled_adj[r]))]
    while stack:
        u, it = stack[-1]; adv = False
        for w in it:
            if not visited[w]:
                visited[w] = True; depth[w] = depth[u] + 1; par[w] = u
                stack.append((w, iter(shuffled_adj[w]))); adv = True; break
        if not adv: stack.pop()
    tree_mask = 0
    for i, (u, v) in enumerate(edges):
        if depth[u] == depth[v] + 1 and par[u] == v: tree_mask |= 1 << i
        elif depth[v] == depth[u] + 1 and par[v] == u: tree_mask |= 1 << i
    nontree = []
    for i, (u, v) in enumerate(edges):
        if not (tree_mask >> i & 1):
            a, b = (u, v) if depth[u] <= depth[v] else (v, u)
            if not is_ancestor(a, b, depth, par): return None
            nontree.append((b, a, depth[b] - depth[a]))
    return depth, par, nontree


def fund_cycle_edges(sender, ancestor, par):
    path = set(); u = sender
    while u != ancestor:
        p = par[u]; path.add((min(u, p), max(u, p))); u = p
    path.add((min(sender, ancestor), max(sender, ancestor)))
    return path


def is_po2_cycle(sym):
    if not sym: return False
    deg = {}
    for u, v in sym: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if any(d != 2 for d in deg.values()): return False
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    verts = list(deg.keys()); start = verts[0]; seen = {start}; stk = [start]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(seen) == len(verts) and len(verts) in PO2_LENS


rng = random.Random(20260802 + 18)
triples_checked = 0
firing_seen = 0
all_even_trees = 0

for nn in [10, 12, 14]:
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(40):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(10):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            depth, par, be = res
            all_even = all(g % 2 == 0 for _, _, g in be)
            if all_even: all_even_trees += 1
            fc = [fund_cycle_edges(s, a, par) for s, a, _ in be]
            for i in range(len(be)):
                for j in range(i + 1, len(be)):
                    for k in range(j + 1, len(be)):
                        g3 = be[i][2] + be[j][2] + be[k][2]
                        sym = fc[i] ^ fc[j] ^ fc[k]
                        triples_checked += 1
                        # (1) back edges survive
                        for idx in (i, j, k):
                            s, a, _ = be[idx]
                            assert tuple(sorted((s, a))) in sym, \
                                "back edge missing from 3-way sym-diff"
                        # (2) size parity
                        assert len(sym) % 2 == (g3 + 1) % 2, \
                            f"size parity violated: |S|={len(sym)} gapsum={g3}"
                        if is_po2_cycle(sym):
                            firing_seen += 1
                            # (3) firing forces odd gap-sum
                            assert g3 % 2 == 1, \
                                f"firing triple with EVEN gap-sum {g3}"
                            # (4) all-even trees never fire
                            assert not all_even, \
                                "triple fired inside an all-even-gap tree"

assert triples_checked > 5000, f"too few triples sampled: {triples_checked}"
assert firing_seen > 0, "no firing triple sampled — check is vacuous"
print(f"triples={triples_checked} firing={firing_seen} "
      f"all_even_trees={all_even_trees} — all parity assertions hold")
CHECK -->

## Summary

Proved (elementary, unconditional): every 3-way fundamental-cycle sym-diff
contains all three back edges; its size is congruent to
$\operatorname{gap}_1+\operatorname{gap}_2+\operatorname{gap}_3+1 \bmod 2$; hence
the triple mechanism fires only on triples with an odd number of odd-gap
back edges, and never fires in an all-even-gap tree. This is the triple-
mechanism analogue of `crossing_offset_parity` and completes the parity
accounting of all four mechanisms (easy: odd gap; nested/crossing:
same-parity pair; triple: $OOO$ or $OEE$).
