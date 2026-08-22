---
id: fund_pair_overlap
status: proved
depends_on: [triple_sym_diff_structure, sym_diff_nested, crossing_pair_formula]
discharged_by_round: 21
introduced_at_round: 21
---

# Lemma `fund_pair_overlap` (unified pair sym-diff characterization: single cycle iff tree paths share an edge)

**Setting.** $T$ is a DFS (Trémaux) spanning tree of a connected simple
graph $G$, rooted at $r$; depths $d(\cdot)$; write $u \sqsubseteq v$ for
"$u$ is an ancestor of $v$ or $u = v$" (equivalently, $u$ lies on the tree
path from $r$ to $v$). For a back edge $B_i = (s_i, a_i)$ with
$a_i \sqsubset s_i$, let $P_i = \operatorname{TreePath}(s_i, a_i)$ (edge
set), $C_i = \{B_i\} \cup P_i$ its fundamental cycle, and
$\operatorname{gap}_i = d(s_i) - d(a_i) = |P_i| \ge 2$. Let $B_1 \ne B_2$
be back edges and $D = C_1 \triangle C_2$.

**Statement.**

1. **(Intersection structure.)** The intersection subgraph
   $(V(C_1) \cap V(C_2),\ E(C_1) \cap E(C_2))$ is one of: the empty graph,
   a single vertex, or a single vertical tree path of length $k \ge 1$.
   Explicitly: it is nonempty iff the anchors are comparable
   ($a_1 \sqsubseteq a_2$ WLOG) and $a_2 \sqsubseteq m$ where
   $m = \operatorname{lca}(s_1, s_2)$, in which case
   $$V(C_1) \cap V(C_2) = \{v : a_2 \sqsubseteq v \sqsubseteq m\}, \qquad
     E(C_1) \cap E(C_2) = E(\operatorname{TreePath}(a_2, m)),$$
   the full vertical chain from the **deeper anchor** $a_2$ down to $m$,
   with
   $$k := |E(C_1) \cap E(C_2)| = d(m) - d(a_2) \ge 0.$$
2. **(Single-cycle iff overlap.)** $D$ is a single simple cycle **iff**
   $k \ge 1$, i.e. iff $P_1$ and $P_2$ share at least one tree edge; and
   then
   $$|D| = \operatorname{gap}_1 + \operatorname{gap}_2 + 2 - 2k .$$
   If $k = 0$ with one shared vertex, $D = C_1 \cup C_2$ has a degree-4
   vertex; if $V(C_1) \cap V(C_2) = \emptyset$, $D$ is a disjoint union of
   two cycles. In neither case is $D$ a single simple cycle.
3. **(Subsumption.)** The nested configuration
   ($a_1 \sqsubseteq a_2 \sqsubset s_2 \sqsubseteq s_1$) has $m = s_2$,
   $k = \operatorname{gap}_2$, giving
   $|D| = \operatorname{gap}_1 - \operatorname{gap}_2 + 2$
   (Lemmas `same_leaf_sym_diff`, `sym_diff_nested`); the strict crossing
   configuration ($d(a_1) < d(a_2) < d(s_1) < d(s_2)$ on one branch) has
   $m = s_1$, $k = d(s_1) - d(a_2)$, giving
   $|D| = (d(a_2) - d(a_1)) + (d(s_2) - d(s_1)) + 2$
   (Lemma `crossing_pair_formula`). **Branching pairs** — senders $s_1, s_2$
   in different subtrees below $m$, excluded by both earlier lemmas — are
   covered uniformly: they give a single cycle exactly when the deeper
   anchor is a strict ancestor of $m$.
4. **(Parity.)** $|D| \equiv \operatorname{gap}_1 + \operatorname{gap}_2
   \pmod 2$: a mixed pair (one odd, one even gap) with $k \ge 1$ yields a
   single cycle of **odd** length; a same-parity pair yields even length.
5. **(Supply corollary for the pasting mechanism.)** In any DFS tree
   containing an odd-gap back edge and an even-gap back edge whose tree
   paths share an edge, there is a mixed pair with single-cycle sym-diff
   $D$ of odd length — the raw material required by the $OEE$ pasting
   rescue of `triple_sym_diff_structure`(6). In particular, if any leaf
   (or any vertex) of $T$ **sends** two back edges of opposite gap parity,
   the pair overlaps (both paths contain the edge from the sender to its
   parent, so $k \ge 1$) and supplies such a $D$ with
   $|D| = |\operatorname{gap}_1 - \operatorname{gap}_2| + 2$.

**Proof.**

(1) *Vertices.* $V(C_i) = \{v : a_i \sqsubseteq v \sqsubseteq s_i\}$ (the
back edge joins two vertices of the vertical path and adds none). Suppose
$v \in V(C_1) \cap V(C_2)$. Then $a_1 \sqsubseteq v$ and
$a_2 \sqsubseteq v$, so $a_1, a_2$ both lie on the root path of $v$ and
are comparable; WLOG $a_1 \sqsubseteq a_2$ (relabel). Also
$v \sqsubseteq s_1$ and $v \sqsubseteq s_2$, so $v$ is a common
ancestor-or-self of $s_1, s_2$; the set of those is exactly
$\{v : v \sqsubseteq m\}$, $m = \operatorname{lca}(s_1, s_2)$. Hence
$v \in \{u : a_2 \sqsubseteq u \sqsubseteq m\}$. Conversely, if the
anchors are comparable ($a_1 \sqsubseteq a_2$) and
$a_2 \sqsubseteq v \sqsubseteq m$, then $a_1 \sqsubseteq a_2 \sqsubseteq v$
and $v \sqsubseteq m \sqsubseteq s_i$ ($i = 1, 2$), so
$v \in V(C_1) \cap V(C_2)$. The set $\{v : a_2 \sqsubseteq v \sqsubseteq m\}$
is a contiguous vertical chain (a depth interval on the root path of $m$),
possibly empty (when $a_2 \not\sqsubseteq m$) or a single vertex (when
$a_2 = m$).

*Edges.* $E(C_1) \cap E(C_2) = P_1 \cap P_2$ (the back edges are distinct
non-tree edges, and $P_i$ consists of tree edges). A tree edge
$(v, \operatorname{par}(v))$ lies in $P_i$ iff
$a_i \sqsubset v \sqsubseteq s_i$. So it lies in both iff
$a_2 \sqsubset v \sqsubseteq m$ (same computation as above, with the strict
inequality at the top). These are exactly the edges of the chain
$\{v : a_2 \sqsubseteq v \sqsubseteq m\}$: every shared vertex $v$ with
$d(v) > d(a_2)$ contributes its parent edge, whose other endpoint
$\operatorname{par}(v)$ is again a shared vertex. Hence the intersection
subgraph is the full path on the shared vertex chain: empty, one vertex
($a_2 = m$), or a path of length $k = d(m) - d(a_2) \ge 1$. $\square$

(2) If $k \ge 1$: by (1) the intersection subgraph of the two simple
cycles $C_1, C_2$ is a single path of length $k \ge 1$, so the pasting
lemma (`triple_sym_diff_structure`(4)) applies verbatim and gives that
$D = C_1 \triangle C_2$ is a single simple cycle of length
$|C_1| + |C_2| - 2k = \operatorname{gap}_1 + \operatorname{gap}_2 + 2 - 2k$.

If $k = 0$ and $V(C_1) \cap V(C_2) = \{a_2\}$ (one shared vertex, no
shared edge): no edge cancels in the sym-diff, so $D = C_1 \cup C_2$, and
$\deg_D(a_2) = 4$ (two $C_1$-edges and two $C_2$-edges at $a_2$, all
distinct since no edge is shared). A simple cycle is 2-regular, so $D$ is
not one. If $V(C_1) \cap V(C_2) = \emptyset$: $D = C_1 \sqcup C_2$ is
disconnected, not a single cycle. $\square$

(3) *Nested*: $a_1 \sqsubseteq a_2 \sqsubset s_2 \sqsubseteq s_1$ gives
$m = \operatorname{lca}(s_1, s_2) = s_2$ and
$k = d(s_2) - d(a_2) = \operatorname{gap}_2 \ge 2 \ge 1$, so
$|D| = \operatorname{gap}_1 + \operatorname{gap}_2 + 2 - 2\operatorname{gap}_2$.
*Crossing*: all four vertices on one branch with
$d(a_1) < d(a_2) < d(s_1) < d(s_2)$ and $a_2 \sqsubseteq s_1 \sqsubseteq s_2$
gives $m = s_1$, $k = d(s_1) - d(a_2) \ge 1$, and the formula rearranges to
`crossing_pair_formula`. *Branching*: nothing in (1)–(2) required
$s_1, s_2$ comparable — only $m = \operatorname{lca}(s_1, s_2)$ enters.
$\square$

(4) Immediate from (2): $2 - 2k$ is even. $\square$

(5) If a vertex $v$ sends two back edges $B_1 = (v, a_1)$,
$B_2 = (v, a_2)$ with $a_1 \sqsubset a_2$ (anchors are both strict
ancestors of $v$, hence comparable and distinct since $G$ is simple), then
$m = \operatorname{lca}(v, v) = v$ and $k = d(v) - d(a_2) =
\operatorname{gap}_2 \ge 2$, so $D$ is a single cycle of length
$\operatorname{gap}_1 - \operatorname{gap}_2 + 2$; opposite parities make
this odd by (4). The general overlap statement is (2) + (4). $\square$

**Remarks.**

- **(Why this matters for Q9 — the supply half.)** The R20 program needs,
  in every mixed-parity pair-residual tree, a pair with single-cycle
  sym-diff $D$ whose parity class admits a legal third back edge. This
  lemma converts that existential into a concrete overlap condition:
  *a mixed pair supplies odd-length raw material iff an odd-gap and an
  even-gap back edge have edge-overlapping vertical paths* — and the
  overlap parameter is explicit,
  $k = d(\operatorname{lca}(s_1, s_2)) - d(\text{deeper anchor})$. In a
  min-degree-3 graph every DFS-tree leaf sends $\ge 2$ back edges (a leaf
  has one tree edge; simple graphs forbid gap-1 back edges, so all other
  incident edges are back edges FROM the leaf), and same-sender pairs
  always overlap ($k = \operatorname{gap}_{\text{inner}}$). So supply
  fails only if **every** multi-back-edge sender sends gaps of one parity
  AND no cross-sender mixed pair overlaps — a strong global parity
  segregation that the R22 probe should target directly.
- **(Tuning restated with explicit $k$.)** With
  $|D| = \operatorname{gap}_1 + \operatorname{gap}_2 + 2 - 2k_{12}$ and
  the pasting length $|S| = |D| + \operatorname{gap}_3 + 1 - 2k'$, a
  firing triple needs
  $\operatorname{gap}_1 + \operatorname{gap}_2 + \operatorname{gap}_3 + 3
  - 2(k_{12} + k') \in \{4, 8, 16, 32\}$ — all quantities now explicit
  tree-depth data. The tuning question (R21+) is whether the achievable
  values of $k_{12} + k'$ over legal configurations sweep an interval wide
  enough to hit a power of 2 of the correct parity.
- **(Scope note.)** (2) characterizes single-cycle pair sym-diffs
  completely; it does NOT claim $D$'s length is a power of 2 — in
  pair-residual trees it never is (that is the definition of
  pair-residual). No claim about the conjecture itself is made.

---

<!-- CHECK
# fund_pair_overlap: falsification probe.
# On sampled cubic DFS trees, for EVERY pair of back edges:
#  (1) intersection subgraph of the two fundamental cycles is empty, a
#      single vertex, or a single path; shared edges = consecutive pairs
#      of the shared vertex chain (|E| = max(0, |V|-1));
#  (1') shared chain == [deeper anchor .. lca(s1,s2)] exactly;
#  (2) sym-diff is a single simple cycle IFF >= 1 shared edge, and then
#      |D| = gap1 + gap2 + 2 - 2k;
#  (5) same-sender pairs always overlap with k = inner gap.
# Census: trees with a mixed (odd+even gap) overlapping pair; mixed
# overlapping pairs at a single sender.
import random

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

def is_anc(u, v, depth, par):
    # ancestor-or-self
    x = v
    while depth[x] > depth[u]: x = par[x]
    return x == u

def lca(u, v, depth, par):
    while depth[u] > depth[v]: u = par[u]
    while depth[v] > depth[u]: v = par[v]
    while u != v: u = par[u]; v = par[v]
    return u

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
            if not is_anc(a, b, depth, par): return None
            nontree.append((b, a, depth[b] - depth[a]))  # (sender, anchor, gap)
    return depth, par, nontree

def fund_cycle_edges(sender, ancestor, par):
    path = set(); u = sender
    while u != ancestor:
        p = par[u]; path.add((min(u, p), max(u, p))); u = p
    path.add((min(sender, ancestor), max(sender, ancestor)))
    return path

def single_cycle_len(sym):
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

rng = random.Random(20260804 + 21)
pairs_checked = 0
overlap_pairs = 0
mixed_overlap_pairs = 0
trees_seen = 0
trees_with_mixed_overlap = 0
trees_mixed_parity = 0
same_sender_pairs = 0
kmax = 0

for nn in (10, 12, 14, 16):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(40):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(5):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            depth, par, be = res
            m = len(be)
            trees_seen += 1
            gaps = [g for _, _, g in be]
            mixed_tree = any(g % 2 for g in gaps) and any(g % 2 == 0 for g in gaps)
            if mixed_tree: trees_mixed_parity += 1
            fc = [fund_cycle_edges(s, a, par) for s, a, _ in be]
            vsets = [{v for e in c for v in e} for c in fc]
            tree_mixed_overlap = False
            for i in range(m):
                si, ai, gi = be[i]
                for j in range(i + 1, m):
                    sj, aj, gj = be[j]
                    pairs_checked += 1
                    es = fc[i] & fc[j]
                    vs = vsets[i] & vsets[j]
                    # (1) predicted shared chain
                    anc_cmp = is_anc(ai, aj, depth, par) or is_anc(aj, ai, depth, par)
                    if not anc_cmp:
                        assert not vs, f"incomparable anchors but shared vertices: {vs}"
                    if vs:
                        A = ai if depth[ai] >= depth[aj] else aj  # deeper anchor
                        mm = lca(si, sj, depth, par)
                        assert is_anc(A, mm, depth, par), \
                            "shared vertices but deeper anchor not ancestor-or-self of lca"
                        chain = set(); x = mm
                        while True:
                            chain.add(x)
                            if x == A: break
                            x = par[x]
                        assert vs == chain, f"shared vertices != [A..lca] chain"
                        assert len(es) == len(vs) - 1, \
                            f"intersection not a path: |E|={len(es)} |V|={len(vs)}"
                        assert len(es) == depth[mm] - depth[A], "k != d(lca)-d(A)"
                    else:
                        assert not es, "shared edges without shared vertices"
                    k = len(es)
                    kmax = max(kmax, k)
                    # (2) single cycle iff k >= 1, with length formula
                    L = single_cycle_len(fc[i] ^ fc[j])
                    if k >= 1:
                        assert L is not None, f"overlap k={k} but sym-diff not single cycle"
                        assert L == gi + gj + 2 - 2 * k, \
                            f"length formula failed: L={L} g1={gi} g2={gj} k={k}"
                        overlap_pairs += 1
                        if (gi % 2) != (gj % 2):
                            mixed_overlap_pairs += 1
                            tree_mixed_overlap = True
                    else:
                        assert L is None, "no shared edge but sym-diff is a single cycle"
                    # (5) same-sender pairs overlap with k = inner gap
                    if si == sj:
                        same_sender_pairs += 1
                        assert k == min(gi, gj) and k >= 2, \
                            f"same-sender pair k={k} gaps={gi},{gj}"
            if mixed_tree and tree_mixed_overlap:
                trees_with_mixed_overlap += 1

assert pairs_checked > 3000, f"too few pairs: {pairs_checked}"
assert overlap_pairs > 300, f"overlap under-sampled: {overlap_pairs}"
assert same_sender_pairs > 20, f"same-sender under-sampled: {same_sender_pairs}"
assert kmax >= 3, "k range too small to exercise the formula"
frac = trees_with_mixed_overlap / max(1, trees_mixed_parity)
print(f"pairs={pairs_checked} overlap={overlap_pairs} "
      f"mixed_overlap={mixed_overlap_pairs} same_sender={same_sender_pairs} "
      f"kmax={kmax} mixed_trees={trees_mixed_parity} "
      f"mixed_trees_with_mixed_overlap={trees_with_mixed_overlap} ({frac:.1%}) "
      f"— all structure assertions hold")
CHECK -->

## Summary

Proved (elementary, unconditional): in a DFS tree the intersection
subgraph of two fundamental cycles is always empty, a single vertex, or a
single vertical path — never anything messier — with the shared chain
running exactly from the deeper anchor to $\operatorname{lca}(s_1, s_2)$.
Consequently $C_1 \triangle C_2$ is a single simple cycle **iff** the two
tree paths share an edge, with uniform length
$\operatorname{gap}_1 + \operatorname{gap}_2 + 2 - 2k$; this subsumes the
nested and crossing pair formulas and extends them to branching pairs.
Supply corollary: any odd-gap/even-gap pair with overlapping paths — in
particular any sender emitting back edges of both parities — yields the
odd single-cycle raw material for the $OEE$ pasting rescue. The CHECK
verifies the iff, the chain characterization, and the length formula on
every back-edge pair of sampled cubic DFS trees.
