---
id: triple_sym_diff_structure
status: proved
depends_on: [triple_parity, crossing_pair_formula]
discharged_by_round: 19
introduced_at_round: 19
---

# Lemma `triple_sym_diff_structure` (length formula, single-cycle criterion, and the pasting mechanism)

**Setting.** $T$ is a DFS (Trémaux) spanning tree of a connected simple graph
$G$, rooted at $r$. For a back edge $B_i = (s_i, a_i)$ ($a_i$ a proper
ancestor of $s_i$), write $P_i = \operatorname{TreePath}(s_i, a_i)$ for its
vertical tree path (edge set), $C_i = \{B_i\} \cup P_i$ for its fundamental
cycle, and $\operatorname{gap}_i = d(s_i) - d(a_i) = |P_i| \ge 2$ (a gap-1
back edge would be parallel to a tree edge, impossible in a simple graph).
Let $B_1, B_2, B_3$ be distinct back edges and
$S = C_1 \triangle C_2 \triangle C_3$.

**Statement.**

1. **(Length formula.)** $|S| = 3 + t$, where
   $t = \#\{\text{tree edges covered by an odd number of } P_1, P_2, P_3\}$.
2. **(Parity consistency.)** $t \equiv \operatorname{gap}_1 +
   \operatorname{gap}_2 + \operatorname{gap}_3 \pmod 2$; hence (1) rederives
   `triple_parity`(2).
3. **(Single-cycle criterion.)** $S$ is a nonempty even subgraph, hence an
   edge-disjoint union of simple cycles, and for every vertex $v$,
   $\deg_S(v) = b(v) + \tau(v)$ where $b(v)$ is the number of $B_i$ incident
   to $v$ and $\tau(v)$ the number of odd-covered tree edges incident to $v$.
   $S$ is a **single simple cycle** iff $S$ is connected and every vertex of
   $S$ has degree exactly $2$.
4. **(Pasting lemma — general.)** Let $X, Y$ be simple cycles in a graph
   whose intersection **subgraph** $(V(X) \cap V(Y),\ E(X) \cap E(Y))$ is a
   single path of length $k \ge 1$. Then $X \triangle Y$ is a single simple
   cycle of length $|X| + |Y| - 2k$.
5. **(Triple pasting criterion.)** Suppose some pair, say $(B_1, B_2)$, has
   sym-diff $D = C_1 \triangle C_2$ a single simple cycle (e.g. via the
   nested or crossing pair lemmas), and the intersection subgraph
   $D \cap C_3$ is a single path of length $k \ge 1$. Then
   $$S \text{ is a single simple cycle of length } |D| + \operatorname{gap}_3 + 1 - 2k.$$
6. **(Mixed-parity rescue shape.)** If $(B_1, B_2)$ is a *mixed* pair (one
   odd, one even gap) with $D$ a single cycle, then $|D|$ is odd, and under
   the hypotheses of (5), $|S| \equiv \operatorname{gap}_3 \pmod 2$: the
   triple can fire (even $|S|$, a power of $2$) only when
   $\operatorname{gap}_3$ is **even**, i.e. the triple is $OEE$ — exactly
   the parity class `triple_parity` singles out as the only cross-parity
   mechanism. Dually, a same-parity pair ($|D|$ even) pastes to a firing
   $S$ only with odd $\operatorname{gap}_3$ ($OOO$ or $EEO$).

**Proof.**

(1) The three back edges are distinct non-tree edges and each lies in
exactly one of the three fundamental cycles (its own), so each survives the
sym-diff (`triple_parity`(1)). A tree edge lies in $C_i$ iff it lies in
$P_i$, so it survives iff it is covered by an odd number of the $P_i$.
$\square$

(2) Writing $c_m$ for the number of tree edges covered exactly $m$ times,
$t = c_1 + c_3$ and $\sum_i |P_i| = c_1 + 2c_2 + 3c_3 \equiv c_1 + c_3
\pmod 2$. Since $|P_i| = \operatorname{gap}_i$, $t \equiv \sum_i
\operatorname{gap}_i \pmod 2$, and $|S| = 3 + t \equiv \sum_i
\operatorname{gap}_i + 1 \pmod 2$. $\square$

(3) $S$ is a symmetric difference of cycles, hence lies in the cycle space
of $G$: every vertex has even degree. It is nonempty by (1). A nonempty
even subgraph decomposes into edge-disjoint simple cycles (extract cycles
greedily). The degree formula is immediate from the edge census in (1). A
single simple cycle is connected with all degrees $2$; conversely a
connected finite graph in which every vertex has degree $2$ is a simple
cycle. $\square$

(4) Since $E(X) \cap E(Y)$ is a nonempty connected subset of the cycle $X$,
it is a contiguous arc of $X$; call the path $P$, with endpoints $p \ne q$
(distinct since $k \ge 1$). Let $\bar X = X \setminus E(P)$ and
$\bar Y = Y \setminus E(P)$ be the complementary arcs: each is a $p$–$q$
path, of lengths $|X| - k \ge 1$ and $|Y| - k \ge 1$, with internal vertex
sets $V(X) \setminus V(P)$ and $V(Y) \setminus V(P)$ respectively. A common
internal vertex of $\bar X$ and $\bar Y$ would lie in
$(V(X) \cap V(Y)) \setminus V(P) = \emptyset$ — so $\bar X$ and $\bar Y$
are internally vertex-disjoint. They are edge-disjoint: a common edge would
lie in $E(X) \cap E(Y) = E(P)$, excluded. (In particular they cannot both
be the single edge $pq$.) Hence $\bar X \cup \bar Y$ is a simple cycle of
length $|X| + |Y| - 2k$, and $X \triangle Y = \bar X \cup \bar Y$ because
exactly the edges of $P$ appear in both. $\square$

(5) $\triangle$ is associative: $S = D \triangle C_3$. $D$ and $C_3$ are
simple cycles; $B_3 \notin D$ (the only non-tree edges of $C_1 \cup C_2$
are $B_1, B_2$), so $E(D) \cap E(C_3)$ consists of tree edges and the
hypothesis matches (4) with $X = D$, $Y = C_3$, $|C_3| =
\operatorname{gap}_3 + 1$. $\square$

(6) For a mixed pair, $|D| \equiv \operatorname{gap}_1 +
\operatorname{gap}_2 \equiv 1 \pmod 2$ (sym-diff preserves size parity and
$|C_i| = \operatorname{gap}_i + 1$). Then $|S| = |D| + \operatorname{gap}_3
+ 1 - 2k \equiv \operatorname{gap}_3 \pmod 2$. Powers of two that occur as
cycle lengths are even. The same computation with $|D|$ even gives
$|S| \equiv \operatorname{gap}_3 + 1$. $\square$

**Remarks.**

- **(Necessity is NOT claimed.)** (5) is a *sufficient* condition. If
  $E(D) \cap E(C_3) = \emptyset$ then $S = D \cup C_3$ is disconnected or
  has a degree-4 vertex — never a single simple cycle — but when the
  intersection subgraph has several components, $S$ may or may not be a
  single cycle; those configurations are outside (5) and are measured
  empirically by the CHECK census below.
- **(Why this matters for Q9.)** In a mixed-parity residual tree, pair
  mechanisms fail *to fire* (no PO2 length), but mixed nested/crossing
  pairs still produce single sym-diff cycles $D$ of **odd** length —
  invisible to the pair taxonomy, which only asks for PO2. Pasting a third
  even-gap back edge converts $D$ into an even-length cycle
  $|D| + \operatorname{gap}_3 + 1 - 2k$, with $k$ a free parameter ranging
  over the overlap; this is a concrete route to $8$. The R18 census
  (rescue lengths $C_8$ 698×) is consistent with this mechanism; the CHECK
  below measures directly what fraction of firing triples factor through
  (5).

---

<!-- CHECK
# triple_sym_diff_structure: falsification probe.
# (a) |S| = 3 + t on every sampled triple;
# (b) S always an even subgraph; single-cycle detector == (connected & 2-regular);
# (d) pasting on fundamental-cycle pairs whose intersection subgraph is a path;
# (e) triple pasting length formula whenever its hypotheses hold;
# census: fraction of firing triples that factor through pasting.
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


def single_cycle_len(sym):
    # length if sym is a single simple cycle, else None
    if not sym: return None
    deg = {}
    for u, v in sym: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if any(d != 2 for d in deg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    start = next(iter(deg)); seen = {start}; stk = [start]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(sym) if len(seen) == len(deg) else None


def path_len_of_intersection(cyc1, cyc2):
    # length k if the intersection SUBGRAPH of two cycles is a single path
    # of length >= 1, else None. Requires: shared-vertex set == path's
    # vertices (no off-path shared vertices), shared edges form a path.
    es = cyc1 & cyc2
    if not es: return None
    vs1 = {v for e in cyc1 for v in e}
    vs2 = {v for e in cyc2 for v in e}
    shared_v = vs1 & vs2
    deg = {}
    for u, v in es: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if set(deg) != shared_v: return None
    ends = [v for v, d in deg.items() if d == 1]
    if len(ends) != 2 or any(d > 2 for d in deg.values()): return None
    adjP = {}
    for u, v in es:
        adjP.setdefault(u, []).append(v); adjP.setdefault(v, []).append(u)
    seen = {ends[0]}; stk = [ends[0]]
    while stk:
        u = stk.pop()
        for w in adjP[u]:
            if w not in seen: seen.add(w); stk.append(w)
    if len(seen) != len(deg): return None
    return len(es)


rng = random.Random(20260803 + 19)
triples_checked = 0
pairs_pasted = 0
triples_pasted = 0
firing = 0
firing_via_pasting = 0
firing_len_census = {}

for nn in (10, 12, 14):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(30):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(6):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            depth, par, be = res
            m = len(be)
            fc = [fund_cycle_edges(s, a, par) for s, a, _ in be]
            bedge = [tuple(sorted((s, a))) for s, a, _ in be]
            tpath = [fc[i] - {bedge[i]} for i in range(m)]
            # (d) pasting on fundamental-cycle pairs
            for i in range(m):
                for j in range(i + 1, m):
                    k = path_len_of_intersection(fc[i], fc[j])
                    if k is not None:
                        L = single_cycle_len(fc[i] ^ fc[j])
                        assert L == len(fc[i]) + len(fc[j]) - 2 * k, \
                            f"pair pasting failed: L={L} |X|={len(fc[i])} |Y|={len(fc[j])} k={k}"
                        pairs_pasted += 1
            # triples
            for i in range(m):
                for j in range(i + 1, m):
                    for k3 in range(j + 1, m):
                        triples_checked += 1
                        sym = fc[i] ^ fc[j] ^ fc[k3]
                        # (a) length formula |S| = 3 + t
                        cov = {}
                        for p in (tpath[i], tpath[j], tpath[k3]):
                            for e in p: cov[e] = cov.get(e, 0) + 1
                        t = sum(1 for c in cov.values() if c % 2 == 1)
                        assert len(sym) == 3 + t, \
                            f"length formula failed: |S|={len(sym)} t={t}"
                        # back edges survive (re-check of triple_parity(1))
                        for idx in (i, j, k3):
                            assert bedge[idx] in sym
                        # (b/c) even subgraph
                        degc = {}
                        for u, v in sym:
                            degc[u] = degc.get(u, 0) + 1; degc[v] = degc.get(v, 0) + 1
                        assert all(d % 2 == 0 for d in degc.values()), \
                            "sym-diff not an even subgraph"
                        L = single_cycle_len(sym)
                        # (e) triple pasting: try all 3 pair-decompositions
                        via = False
                        for (x, y, z) in ((i, j, k3), (i, k3, j), (j, k3, i)):
                            D = fc[x] ^ fc[y]
                            LD = single_cycle_len(D)
                            if LD is None: continue
                            kk = path_len_of_intersection(D, fc[z])
                            if kk is None: continue
                            triples_pasted += 1
                            assert L is not None and \
                                L == LD + len(fc[z]) - 2 * kk, \
                                (f"triple pasting failed: L={L} |D|={LD} "
                                 f"|C3|={len(fc[z])} k={kk}")
                            via = True
                        if L in PO2_LENS:
                            firing += 1
                            firing_len_census[L] = firing_len_census.get(L, 0) + 1
                            if via: firing_via_pasting += 1

assert triples_checked > 3000, f"too few triples: {triples_checked}"
assert pairs_pasted > 100, f"pair pasting under-sampled: {pairs_pasted}"
assert triples_pasted > 100, f"triple pasting under-sampled: {triples_pasted}"
assert firing > 0, "no firing triple sampled — census vacuous"
frac = firing_via_pasting / firing
print(f"triples={triples_checked} pair_pastings={pairs_pasted} "
      f"triple_pastings={triples_pasted} firing={firing} "
      f"via_pasting={firing_via_pasting} ({frac:.1%}) "
      f"firing_lens={sorted(firing_len_census.items())} — "
      f"all structure assertions hold")
CHECK -->

## Summary

Proved (elementary, unconditional): the 3-back-edge sym-diff has size
$3 + t$ ($t$ = odd-covered tree edges); it is always a nonempty even
subgraph, and is a single simple cycle iff connected and 2-regular; two
simple cycles whose intersection subgraph is a single path of length $k$
sym-diff to a single cycle of length $|X|+|Y|-2k$ (pasting); consequently a
pair with single-cycle sym-diff $D$ plus a third back edge meeting $D$ in a
single path gives a single cycle of length
$|D| + \operatorname{gap}_3 + 1 - 2k$. Mixed pairs have odd $|D|$, so
pasting an even-gap third back edge is the concrete $OEE$ rescue mechanism
for mixed-parity residual trees. The CHECK verifies every claim on sampled
cubic DFS trees and measures how often firing triples factor through
pasting.
