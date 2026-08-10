---
id: sup1_dead_tree
status: proved
depends_on: [sym_diff_cycle_formula, shortpaste_floor_line]
discharged_by_round: 33
introduced_at_round: 33
---

# Lemma `sup1_dead_tree` (PROVED — counterexample): a pair-residual normal spanning tree with NO SUP-1 witness

**Statement.** There exists a cubic graph $G_0$ on 14 vertices and a
normal (Trémaux) spanning tree $T_0$ of $G_0$ such that:

1. $T_0$ is **pair-residual**: no fundamental cycle and no 2-subset
   symmetric difference is a single cycle of power-of-2 length;
2. $T_0$ admits **no SUP-1 witness whatsoever**: for every pair of back
   edges whose symmetric difference $D$ is a single cycle with
   $|D| \ge 6$ and $k_{12} \ge 1$, and every third back edge $B_3$,
   NOT all three of ($k' = 1$, $\operatorname{gap}_3 \le k_{12}+1$,
   $\operatorname{gap}_3 \equiv |D|+1 \bmod 2$) hold;
3. yet $T_0$ **is triple-alive**: six triples of back edges have 3-way
   symmetric differences that are single cycles of length exactly 8.

**Consequences (all falsified as universals over pair-residual trees):**

- **SUP-1 itself** (`sup1_end_edge`'s core claim, "holds 189/189" in
  R31) is FALSE: clause 2 above kills every k'=1 short-parity cover,
  in particular the end-edge and min-gap refinements of R31.
- **`sup1_iadj` Part 2** (the $I$-adjacent supply conjecture, 92/92 in
  R32) is FALSE a fortiori.
- The R31/R32 censuses (189/189, 92/92) were sampling luck: SUP-1-dead
  residual trees are rare — one appeared among $\approx 250$ residual
  trees scanned across five seeds (564k + 152k trees), and 0/167
  residuals on three fresh seeds — but they exist.

**The pinned object.** $G_0$ has edge list (14 vertices, 21 edges,
3-regular, connected):

```
(5,13) (0,2) (10,12) (1,3) (7,10) (6,8) (4,8) (3,6) (3,12) (5,9) (4,11)
(0,1) (9,10) (1,2) (9,13) (0,4) (2,7) (6,13) (5,11) (11,12) (7,8)
```

$T_0$ is rooted at 11 with parent array (index = vertex):

```
par = [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5]
```

$T_0$ is a depth-13 path-like tree; its 8 back edges have fundamental
cycle lengths $[3, 6, 6, 6, 3, 14, 6, 6]$ — none a power of 2, no pair
sym-diff a power-of-2 single cycle, and the exhaustive scan over all
$\binom{8}{2}$ pairs $\times$ 6 third-edges finds no SUP-1 witness
(also: no $k$-subset of back edges for $k \in \{5,6,7,8\}$ gives a
power-of-2 single cycle; $k=3$ gives six firing triples, $k=4$ fires
as well).

**How the tree still fires (why only the k'=1 channel is dead).** The
six firing triples all produce $L = 8$ through met-path sizes
$k'' = |D \cap C_3| \in \{2, 4\}$:

| triple | pairing $|D|$ | $k_{12}$ | $\operatorname{gap}_3$ | $|D \cap C_3|$ | short? | $L$ |
|---|---|---|---|---|---|---|
| (1,2,3) | 6 | 3 | 5 | 2 | no | $6+6-2\cdot 2 = 8$ |
| (1,5,6) | 10 | 5 | 5 | 4 | yes | $10+6-2\cdot 4 = 8$ |

(and four more of the same two shapes). In the first shape the cover is
NOT short ($5 > k_{12}+1 = 4$) and meets 2 edges; in the second it is
short but meets 4 edges. Both lie outside the $k' = 1$ paste class that
the entire SUP-1 program (R23–R32) tuned; on this tree the $k'=1$
class supplies nothing, while $k'' \in \{2,4\}$ covers fire six times.

**Graph-level escape.** $G_0$ itself contains cycles of every length in
$\{3,5,6,\ldots,14\}$, including 8 — it is no Erdős–Gyárfás
counterexample. Of 1000 sampled DFS trees of $G_0$ (random root +
order), 976 are non-residual (a single or pair mechanism fires), 23 are
residual-but-SUP-1-alive, 1 is residual-and-SUP-1-dead. The DFS-tree
quantifier, not the graph, is what breaks.

*Proof.* The CHECK block below verifies every clause deterministically
(no sampling): normality of $T_0$, 3-regularity and connectivity of
$G_0$, pair-residuality, exhaustive absence of SUP-1 witnesses,
existence of a firing triple, and an explicit 8-cycle in $G_0$.
$\square$

<!-- CHECK
# sup1_dead_tree: deterministic verification of the pinned counterexample.
# No sampling, no RNG — every clause checked exhaustively.

edges = [(5, 13), (0, 2), (10, 12), (1, 3), (7, 10), (6, 8), (4, 8), (3, 6),
         (3, 12), (5, 9), (4, 11), (0, 1), (9, 10), (1, 2), (9, 13), (0, 4),
         (2, 7), (6, 13), (5, 11), (11, 12), (7, 8)]
edges = [tuple(sorted(e)) for e in edges]
root = 11
nn = 14
par = [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5]
PO2_LENS = {4, 8, 16, 32}

# --- graph sanity: cubic, connected, 21 distinct edges
assert len(set(edges)) == 21
deg = [0] * nn
adj = [[] for _ in range(nn)]
for u, v in edges:
    deg[u] += 1; deg[v] += 1; adj[u].append(v); adj[v].append(u)
assert all(d == 3 for d in deg)
seen = {0}; stk = [0]
while stk:
    u = stk.pop()
    for w in adj[u]:
        if w not in seen: seen.add(w); stk.append(w)
assert len(seen) == nn

# --- rebuild depths; verify par is a spanning tree rooted at root
depth = [-1] * nn
depth[root] = 0
assert par[root] == -1
pending = [v for v in range(nn) if v != root]
while pending:
    nxt = []
    for v in pending:
        if depth[par[v]] >= 0: depth[v] = depth[par[v]] + 1
        else: nxt.append(v)
    assert len(nxt) < len(pending), "par array is not a tree"
    pending = nxt

def is_ancestor(u, v):
    if depth[u] > depth[v]: return False
    x = v
    while depth[x] > depth[u]: x = par[x]
    return x == u

tre = {(min(v, par[v]), max(v, par[v])) for v in range(nn) if v != root}
assert tre <= set(edges) and len(tre) == nn - 1
# --- normality: every non-tree edge joins ancestor/descendant
be = []
for u, v in [e for e in edges if e not in tre]:
    a, b = (u, v) if depth[u] <= depth[v] else (v, u)
    assert is_ancestor(a, b), f"non-tree edge {u, v} not back — tree not normal"
    be.append((b, a))
m = len(be)
assert m == 8

def fund_cycle_edges(sender, ancestor):
    path = set(); u = sender
    while u != ancestor:
        p = par[u]; path.add((min(u, p), max(u, p))); u = p
    path.add((min(sender, ancestor), max(sender, ancestor)))
    return path

def single_cycle_len(sym):
    if not sym: return None
    dg = {}
    for u, v in sym: dg[u] = dg.get(u, 0) + 1; dg[v] = dg.get(v, 0) + 1
    if any(d != 2 for d in dg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    start = next(iter(dg)); sn = {start}; st = [start]
    while st:
        u = st.pop()
        for w in adjS[u]:
            if w not in sn: sn.add(w); st.append(w)
    return len(sym) if len(sn) == len(dg) else None

def path_len_of_intersection(cyc1, cyc2):
    es = cyc1 & cyc2
    if not es: return None
    vs1 = {v for e in cyc1 for v in e}
    vs2 = {v for e in cyc2 for v in e}
    shared_v = vs1 & vs2
    dg = {}
    for u, v in es: dg[u] = dg.get(u, 0) + 1; dg[v] = dg.get(v, 0) + 1
    if set(dg) != shared_v: return None
    ends = [v for v, d in dg.items() if d == 1]
    if len(ends) != 2 or any(d > 2 for d in dg.values()): return None
    adjP = {}
    for u, v in es:
        adjP.setdefault(u, []).append(v); adjP.setdefault(v, []).append(u)
    sn = {ends[0]}; st = [ends[0]]
    while st:
        u = st.pop()
        for w in adjP[u]:
            if w not in sn: sn.add(w); st.append(w)
    if len(sn) != len(dg): return None
    return len(es)

fc = [fund_cycle_edges(s, a) for s, a in be]
assert sorted(len(c) for c in fc) == [3, 3, 6, 6, 6, 6, 6, 14]

# --- clause 1: pair-residual
assert not any(len(c) in PO2_LENS for c in fc)
for i in range(m):
    for j in range(i + 1, m):
        assert single_cycle_len(fc[i] ^ fc[j]) not in PO2_LENS

# --- clause 2: NO SUP-1 witness (exhaustive over pairs x third edges)
wits = 0
pairs_scanned = 0
for x in range(m):
    for y in range(x + 1, m):
        D = fc[x] ^ fc[y]
        LD = single_cycle_len(D)
        if LD is None or LD < 6: continue
        k12 = (len(fc[x]) + len(fc[y]) - LD) // 2
        if k12 < 1: continue
        pairs_scanned += 1
        for z in range(m):
            if z in (x, y): continue
            kk = path_len_of_intersection(D, fc[z])
            g3 = len(fc[z]) - 1
            if kk == 1 and g3 <= k12 + 1 and (LD + g3) % 2 == 1:
                wits += 1
assert pairs_scanned >= 10, f"vacuous: only {pairs_scanned} eligible pairs"
assert wits == 0, f"SUP-1 witness found — counterexample claim wrong ({wits})"

# --- clause 3: triple-alive, with the documented mechanism shapes
firing = []
for x in range(m):
    for y in range(x + 1, m):
        for z in range(y + 1, m):
            L = single_cycle_len(fc[x] ^ fc[y] ^ fc[z])
            if L in PO2_LENS: firing.append((x, y, z, L))
assert len(firing) == 6, f"expected 6 firing triples, got {len(firing)}"
assert all(L == 8 for _, _, _, L in firing)
# every firing triple works only through |D ∩ C3| in {2,4} (never k'=1)
for x, y, z, L in firing:
    metsizes = set()
    for (i, j, k) in ((x, y, z), (x, z, y), (y, z, x)):
        D = fc[i] ^ fc[j]
        if single_cycle_len(D) is None: continue
        metsizes.add(len(D & fc[k]))
    assert metsizes <= {2, 4, 8} and 1 not in metsizes

# --- graph has an explicit 8-cycle (no E-G counterexample):
# from the firing triple (1,2,3): sym-diff of those fundamental cycles
c8 = fc[1] ^ fc[2] ^ fc[3]
assert single_cycle_len(c8) == 8 and c8 <= set(edges)

print(f"sup1_dead_tree verified: pair-residual normal tree, "
      f"{pairs_scanned} eligible pairs, 0 SUP-1 witnesses, "
      f"6 firing triples (all L=8 via |D∩C3| in {{2,4}})")
CHECK -->

## Summary

Deterministic counterexample killing the SUP-1 universal (and with it
R31's end-edge/min-gap refinements and `sup1_iadj` Part 2): a
14-vertex cubic graph with a pinned normal spanning tree that is
pair-residual and admits NO $k'=1$ short-parity cover on any
$|D| \ge 6$ pair — yet six triples fire at $L = 8$ through
$|D \cap C_3| \in \{2, 4\}$ covers. The $k'=1$ paste channel is
provably insufficient as tree-level supply; the triple mechanism as a
whole is not touched. Program consequences: (a) tree-level supply must
widen to all met-path sizes ("triple-aliveness"), or (b) the
quantifier must move to the graph level (976/1000 DFS trees of $G_0$
are non-residual — the graph escapes trivially).
