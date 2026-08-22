---
id: pasting_cover_dichotomy
status: proved
depends_on: [fund_pair_overlap, pasting_meeting_structure, pasting_vertex_automatic]
discharged_by_round: null
introduced_at_round: 26
---

# Lemma `pasting_cover_dichotomy` (a cover of $D$ either pastes or straddles the cancelled interval)

**Setting.** As in `pasting_meeting_structure`: overlapping pair
$B_1 = (s_1,a_1)$, $B_2 = (s_2,a_2)$ with $k_{12} \ge 1$ shared tree
edges, single-cycle $D = C_1 \triangle C_2$, segments
$A = [a_{\mathrm{sh}} .. a_{\mathrm{deep}}]$, $L_i = [m .. s_i]$
($m = \operatorname{lca}(s_1,s_2)$), and cancelled interval
$I = [a_{\mathrm{deep}} .. m]$ ($|I| = k_{12}$, `fund_pair_overlap`(1)).
Call $B_3 = (s_3,a_3) \notin \{B_1,B_2\}$ a **cover** (of the pair) if
$P_3$ shares at least one edge with $A \sqcup L_1 \sqcup L_2$ — i.e.
$B_3$ covers some tree edge of $D$.

**Claim.** Every cover satisfies exactly one of:

1. **(Pasting.)** $P_3$ meets exactly one of $A, L_1, L_2$ in edges —
   and then, for $\Delta(G) \le 3$, $D \cap C_3$ is a single path
   (`pasting_vertex_automatic`(3)): $B_3$ pastes.
2. **(Straddling.)** $P_3$ meets exactly two, necessarily $A$ and one
   leg $L_i$; and then all of the following hold:
   - $I \subseteq P_3$ (the cover contains the whole cancelled interval);
   - $a_3$ is a strict ancestor of $a_{\mathrm{deep}}$, and $s_3$ lies
     strictly below $m$ in the same child subtree of $m$ as $s_i$;
   - $P_3 \cap A$ contains $A$'s deepest edge (incident to
     $a_{\mathrm{deep}}$) and $P_3 \cap L_i$ contains $L_i$'s top edge
     $(m, c_i)$;
   - $\operatorname{gap}_3 \ge k_{12} + 2$.

**Corollaries (existence criteria).** A cover pastes whenever ANY of:
(c1) $\operatorname{gap}_3 \le k_{12} + 1$; (c2) $a_3$ is not a strict
ancestor of $a_{\mathrm{deep}}$; (c3) $s_3$ is not strictly below $m$.

**Proof.** By `pasting_meeting_structure`(2), at most two of the three
intersections are nonempty, and $P_3 \cap L_1$, $P_3 \cap L_2$ cannot
both be nonempty ($P_3$ descends into at most one child subtree of
$m$). A cover has $\ge 1$ nonempty. So the count is 1 (pasting) or 2
with the two being $A$ and one leg $L_i$ (straddling).

Straddling case. $P_3 = [s_3 .. a_3]$ is a vertical path containing an
edge of $A$ (both endpoints at depth $\le d(a_{\mathrm{deep}})$) and an
edge of $L_i$ (deeper endpoint at depth $> d(m)$). A vertical path
passes through exactly one vertex per depth in its span, so $P_3$'s
span includes all depths from $\le d(a_{\mathrm{deep}}) - 1$ (the
shallower endpoint of the met $A$-edge) to $\ge d(m) + 1$. The vertices
of $P_3$ at depths $d(a_{\mathrm{deep}}), \dots, d(m)$ are the
ancestors of $s_3$ at those depths. Since $P_3$ contains an $L_i$-edge,
$s_3$'s root-chain passes through that edge, hence through $m$ and then
through $I$'s chain (the chain above $m$ is unique); so those vertices
are exactly $V(I)$, and every edge of $I$ lies on $P_3$:
$I \subseteq P_3$. The chain above $a_{\mathrm{deep}}$ is $A$'s chain
(both anchors lie on the common root-chain of the senders,
`fund_pair_overlap`(1)). Every edge of $A$ lies strictly above
$a_{\mathrm{deep}}$, so for $P_3$ to meet one, $P_3$ must contain at
least one edge above $a_{\mathrm{deep}}$ — i.e. $a_3$ is a strict
ancestor of $a_{\mathrm{deep}}$ — and the first such edge (the one
incident to $a_{\mathrm{deep}}$ from above) is $A$'s deepest edge,
hence $A$'s deepest edge $\in P_3 \cap A$. Below $m$: $P_3$'s
chain enters one child subtree of $m$; to meet an edge of $L_i$ (all in
$c_i$'s subtree, $c_i$ = the child of $m$ on $L_i$) the chain must pass
$(m, c_i)$, so that top edge is in $P_3 \cap L_i$, $s_3$ lies strictly
below $m$ in $c_i$'s subtree, and (with $s_i$ in the same subtree) the
b4 condition holds. Finally $P_3 \supseteq \{\text{one edge above }
a_{\mathrm{deep}}\} \cup I \cup \{(m, c_i)\}$ gives
$\operatorname{gap}_3 = |P_3| \ge 1 + k_{12} + 1$. The corollaries are
the contrapositives. $\square$

**Consequence for Q9 (meeting existence).** Meeting-existence for a
pair is now: *some cover avoids straddling*. Straddling is expensive —
the cover must span the entire cancelled interval plus an edge on each
side — so short back edges ($\operatorname{gap} \le k_{12}+1$) covering
any $D$-edge paste automatically.

**Census finding (important negative).** In the CHECK below (2-edge-
connected cubic samples, so coverage of every tree edge is guaranteed),
per-PAIR existence FAILS at a visible rate: ~3% of single-cycle pairs
have NO pasting cover at all, and ~16% have no even-gap pasting cover
(even $\operatorname{gap}_3$ is what makes $L$ even when $|D|$ is odd).
So the tuning argument (T2/T3) must quantify over pairs per TREE — "for
every pair-residual tree SOME pair admits an even-gap pasting cover" —
consistent with `pasting_value_interval`'s per-tree census ($8 \in
V(T)$, 53/53), and per-pair shortcuts are dead. Recorded so no future
session burns a round trying to prove per-pair existence.

---

<!-- CHECK
# pasting_cover_dichotomy: every cover of a tree edge of D either
# pastes (exactly one segment met) or straddles: meets A + exactly one
# leg, contains ALL of I=[a_deep..m], anchor strictly above a_deep,
# sender strictly below m in the met leg's child subtree, includes A's
# deepest edge and the leg's top edge, and gap3 >= k12+2.
# Census: per-pair availability of (even-gap) pasting covers.
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

def vpath_edges(lo, hi, par):
    es = set(); u = lo
    while u != hi:
        p = par[u]; es.add((min(u, p), max(u, p))); u = p
    return es

def fund_cycle_edges(sender, ancestor, par):
    es = vpath_edges(sender, ancestor, par)
    es.add((min(sender, ancestor), max(sender, ancestor)))
    return es

def lca(u, v, depth, par):
    while depth[u] > depth[v]: u = par[u]
    while depth[v] > depth[u]: v = par[v]
    while u != v: u = par[u]; v = par[v]
    return u

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

def anc_at_depth(v, d, depth, par):
    x = v
    while depth[x] > d: x = par[x]
    return x

def is_bridgeless(nn, edges, adj):
    # 2-edge-connected check via simple DFS lowlink
    disc = [-1]*nn; low = [0]*nn; timer = [0]; bridge = [False]
    def it_dfs(root):
        stack = [(root, -1, iter(adj[root]))]
        disc[root] = low[root] = timer[0]; timer[0] += 1
        while stack:
            u, pe, itr = stack[-1]
            done = True
            for w in itr:
                if disc[w] == -1:
                    disc[w] = low[w] = timer[0]; timer[0] += 1
                    stack.append((w, u, iter(adj[w])))
                    done = False; break
                elif w != pe:
                    low[u] = min(low[u], disc[w])
                elif w == pe:
                    # cubic simple graph: at most one edge to parent
                    pass
            if done:
                stack.pop()
                if stack:
                    p = stack[-1][0]
                    low[p] = min(low[p], low[u])
                    if low[u] > disc[p]: bridge[0] = True
    it_dfs(0)
    return not bridge[0]

rng = random.Random(20260806 + 26)
pairs_seen = 0; covers_seen = 0; pasting_covers = 0; straddling = 0
pair_with_even_pasting = 0; pair_with_any_pasting = 0
for nn in (10, 12, 14, 16):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(90):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        if not is_bridgeless(nn, edges, adj): continue
        for _ in range(3):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            depth, par, be = res
            m = len(be)
            fc = [fund_cycle_edges(s, a, par) for s, a, _ in be]
            pe = [vpath_edges(s, a, par) for s, a, _ in be]
            for i in range(m):
                s1, a1, g1 = be[i]
                for j in range(i + 1, m):
                    s2, a2, g2 = be[j]
                    D = fc[i] ^ fc[j]
                    if single_cycle_len(D) is None: continue
                    pairs_seen += 1
                    mm = lca(s1, s2, depth, par)
                    a_deep, a_sh = (a1, a2) if depth[a1] >= depth[a2] else (a2, a1)
                    k12 = depth[mm] - depth[a_deep]
                    assert k12 >= 1
                    A = vpath_edges(a_deep, a_sh, par)
                    L1 = vpath_edges(s1, mm, par)
                    L2 = vpath_edges(s2, mm, par)
                    I = vpath_edges(mm, a_deep, par)
                    # deepest A-edge (incident a_deep); top edges of legs (incident mm)
                    eA_bot = (min(a_deep, par[a_deep]), max(a_deep, par[a_deep])) if A else None
                    has_even = False; has_any = False
                    for z in range(m):
                        if z == i or z == j: continue
                        s3, a3, g3 = be[z]
                        P3 = pe[z]
                        inters = [P3 & X for X in (A, L1, L2)]
                        ne = [q for q in range(3) if inters[q]]
                        if not ne: continue
                        covers_seen += 1
                        if len(ne) == 1:
                            pasting_covers += 1
                            has_any = True
                            if g3 % 2 == 0: has_even = True
                            continue
                        straddling += 1
                        assert ne == [0, 1] or ne == [0, 2], \
                            f"FALSIFIED(b0): two segments met are not A+leg: {ne} (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                        li = ne[1]  # 1 or 2
                        s_i = s1 if li == 1 else s2
                        Lseg = L1 if li == 1 else L2
                        assert I <= P3, \
                            f"FALSIFIED(b1): straddling cover does not contain I (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                        assert depth[a3] < depth[a_deep], \
                            f"FALSIFIED(b2): anchor not strictly above a_deep (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                        assert depth[s3] > depth[mm], \
                            f"FALSIFIED(b3): sender not strictly below m (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                        assert anc_at_depth(s3, depth[mm] + 1, depth, par) == anc_at_depth(s_i, depth[mm] + 1, depth, par), \
                            f"FALSIFIED(b4): sender not in met leg's child subtree (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                        assert g3 >= k12 + 2, \
                            f"FALSIFIED(b5): gap3 < k12+2 (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                        assert eA_bot in inters[0], \
                            f"FALSIFIED(b6): A-intersection misses A's deepest edge (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                        c_i = anc_at_depth(s_i, depth[mm] + 1, depth, par)
                        eL_top = (min(mm, c_i), max(mm, c_i))
                        assert eL_top in inters[li], \
                            f"FALSIFIED(b7): leg-intersection misses leg's top edge (n={nn}, edges={edges}, root={r}, i={i}, j={j}, z={z})"
                    if has_any: pair_with_any_pasting += 1
                    if has_even: pair_with_even_pasting += 1
assert pairs_seen > 4000 and covers_seen > 8000, \
    f"probe vacuous: pairs={pairs_seen} covers={covers_seen}"
print(f"pairs={pairs_seen} covers={covers_seen} pasting={pasting_covers} straddling={straddling} "
      f"pair_with_any_pasting={pair_with_any_pasting} pair_with_even_pasting={pair_with_even_pasting} "
      f"— cover dichotomy verified (census: even-gap pasting per pair = "
      f"{pair_with_even_pasting}/{pairs_seen})")
CHECK -->

## Summary

Proved (R26): a back edge covering a tree edge of $D$ either meets
exactly one segment (and pastes, in subcubic graphs, by
`pasting_vertex_automatic`) or "straddles": it meets $A$ plus exactly
one leg, its path contains the whole cancelled interval $I$, includes
$A$'s deepest and the leg's topmost edge, and has
$\operatorname{gap}_3 \ge k_{12} + 2$. Covers with gap
$\le k_{12} + 1$, or anchored at/below $a_{\mathrm{deep}}$, or sent
from at/above $m$, always paste. Census: per-pair even-gap pasting
covers are MISSING for ~16% of pairs — meeting-existence and tuning
must be per-tree, not per-pair.
