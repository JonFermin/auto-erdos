---
id: sup1_iadj
status: disproved
depends_on: [sup1_end_edge, shortpaste_floor_line, pasting_cover_dichotomy, pasting_vertex_automatic, pasting_meeting_structure]
discharged_by_round: 33
introduced_at_round: 32
---

# Lemma `sup1_iadj` (Part 2 DISPROVED R33 — see `sup1_dead_tree`; Part 1's cover-structure geometry remains PROVED and reusable)

**DISPROVED (R33).** The headline claim (Part 2, the $I$-adjacent
supply conjecture) is false: `lemma_sup1_dead_tree__0810-081024-1a40.md`
pins a pair-residual normal spanning tree with NO SUP-1 witness of any
kind — in particular none at an $I$-adjacent edge. The R32 census
(92/92) was sampling luck. **Part 1 below is unaffected**: it is an
unconditional structure theorem about short covers through $I$-adjacent
edges (proved from the dichotomy + cubic geometry, with its consistency
CHECK retained). Any future use should cite it as "`sup1_iadj` Part 1";
if a round needs it as a standalone ledger id, re-issue it under a new
id (e.g. `iadj_cover_structure`) — do NOT re-open this id.

**Setting.** As in `pasting_cover_dichotomy`: pair $(B_1, B_2)$,
single-cycle $D$, overlap $k_{12} \ge 1$, segments
$A = [a_{\mathrm{sh}} .. a_{\mathrm{deep}}]$, $L_i = [m .. s_i]$,
cancelled interval $I = [a_{\mathrm{deep}} .. m]$. The
**$I$-adjacent boundary edges** of the pair are the (at most three)
edges of $D$ incident to an endpoint of $I$: the leg-top edges
$(m, c_i)$ ($c_i$ = child of $m$ on $L_i$; exists iff $L_i \ne
\emptyset$) and the $A$-bottom edge
$e_A = (a_{\mathrm{deep}}, \mathrm{par}(a_{\mathrm{deep}}))$ (exists
iff $A \ne \emptyset$). A **SUP-1 witness** is a cover $B_3$ with
$\operatorname{gap}_3 \le k_{12}+1$, $k' = 1$, and
$\operatorname{gap}_3 \equiv |D| + 1 \pmod 2$ (even $L$, hence
$L \ge 8$ when $|D| \ge 6$, `shortpaste_floor_line`).

## Part 1 — PROVED: structure of short covers at $I$-adjacent edges

Let $B_3 = (s_3, a_3)$ be any cover with
$\operatorname{gap}_3 \le k_{12} + 1$ (short) whose path $P_3$
contains an $I$-adjacent boundary edge. ($\Delta(G) \le 3$ throughout.)

**(S1)** $B_3$ pastes: $D \cap C_3$ is a single path meeting exactly
one segment (`pasting_cover_dichotomy` c1 — short covers cannot
straddle, since straddling forces
$\operatorname{gap}_3 \ge k_{12} + 2$; single-path by
`pasting_vertex_automatic`).

**(S2) Leg-top case.** If $(m, c_i) \in P_3$ and $A \ne \emptyset$,
then $a_3 \in V(I)$, and $D \cap C_3 \subseteq L_i$ with
$k' = 1 + \ell$, where $\ell \ge 0$ is the length of the common
descent of $P_3$ and $L_i$ below $c_i$ (the chain from $c_i$ to the
first vertex where $s_3$'s root-chain leaves $s_i$'s root-chain).

*Proof.* $s_3$ lies in $c_i$'s subtree (its chain contains
$(m, c_i)$), so above $m$ the chain of $s_3$ is THE common root chain
through $I$, $a_{\mathrm{deep}}$, $A$. If $a_3$ were a strict ancestor
of $a_{\mathrm{deep}}$, then $P_3 \supseteq I \cup
\{(a_{\mathrm{deep}}, \mathrm{par}(a_{\mathrm{deep}}))\}$; the latter
is an $A$-edge (nonempty $A$ puts $a_{\mathrm{sh}}$ strictly above
$a_{\mathrm{deep}}$), so $P_3$ meets both $A$ and $L_i$ — straddling,
contradicting shortness. Hence
$d(a_{\mathrm{deep}}) \le d(a_3) \le d(m)$, i.e. $a_3 \in V(I)$.
Consequently $P_3$ contains no edge above $a_{\mathrm{deep}}$, so it
meets no $A$-edge; below $m$ it descends only into $c_i$'s subtree, so
it meets no $L_j$-edge ($j \ne i$; $c_j \ne c_i$ since
$m = \operatorname{lca}(s_1, s_2)$); $I$-edges and side-branch edges
are not in $D$. So $D \cap P_3 \subseteq L_i$, and the met set is
$(m, c_i)$ plus the common descent below $c_i$: $k' = 1 + \ell$.
$\square$

**Corollary (k'=1 criteria, leg-top).** $k' = 1$ iff $P_3$ and $L_i$
diverge at $c_i$; sufficient: $s_3 = c_i$, or $|L_i| = 1$ (i.e.
$s_i = c_i$), or the child of $c_i$ on $P_3$ differs from the child of
$c_i$ on $L_i$.

**(S3) $A$-bottom case.** If $e_A \in P_3$, then
$D \cap C_3 \subseteq A$ is a single path containing $e_A$ with
$$k' \;=\; d(a_{\mathrm{deep}}) - \max(d(a_3), d(a_{\mathrm{sh}})),$$
and if both legs are nonempty, $s_3$ does not lie strictly below $m$.

*Proof.* $P_3$ runs from $s_3$ (in $a_{\mathrm{deep}}$'s subtree)
through $a_{\mathrm{deep}}$ up to $a_3$ (a strict ancestor of
$a_{\mathrm{deep}}$, since $e_A \in P_3$). Above $a_{\mathrm{deep}}$
the chain is $A$'s chain up to $\min$-depth
$\max(d(a_3), d(a_{\mathrm{sh}}))$ (edges above $a_{\mathrm{sh}}$ are
not in $D$), giving the $k'$ formula, and the met $A$-run is
contiguous containing $e_A$. Below $a_{\mathrm{deep}}$: side branches
off $V(I)$ and $I$-edges are not in $D$; if $s_3$ were strictly below
$m$ with both legs nonempty, then (cubic: $m$ has at most two
children, and $c_1, c_2$ are two distinct children, so ALL children of
$m$ are leg children) $s_3$'s chain would contain some $(m, c_i)$, so
$P_3$ would meet $L_i$ as well as $A$ — straddling, contradicting
shortness. $\square$

**Corollary (k'=1 criteria, $A$-bottom).** $k' = 1$ iff
$a_3 = \mathrm{par}(a_{\mathrm{deep}})$ or $|A| = 1$.

**(S4)** Combining with `shortpaste_floor_line`: a short cover of an
$I$-adjacent boundary edge with $k' = 1$ and
$\operatorname{gap}_3 \equiv |D| + 1 \pmod 2$ on a pair with
$|D| \ge 6$ yields an even short-paste value $L \ge 8$.

## Part 2 — DISPROVED (R33): the $I$-adjacent supply conjecture

**Claim (disproved — counterexample in `sup1_dead_tree`).**
Every pair-residual tree admits a pair with $|D| \ge 6$ and an
$I$-adjacent boundary edge $e$ such that the MINIMUM-GAP cover of $e$
is a SUP-1 witness.

This sharpens `sup1_end_edge` (whose witness could sit on any of six
boundary edges): the witness always lives at the boundary of the
cancelled interval, where Part 1 pins the cover's geometry to the
$I$-window.

**Census (R32, seed 20260809+532, 152k trees, 42 residuals).**
$I$-adjacent min-gap rule: **42/42**; even allowing any (non-min-gap)
cover of a far end edge, NO tree required a far edge (0 occurrences).

**Quantifier negatives (R32 scoping census, seed 20260809+432, 37
residuals — recorded so no session chases them).**
- $\forall$-pair versions are DEAD: "every $|D| \ge 6$ pair admits the
  min-gap rule" fails on every tree (0/37); even "every $|D| \ge 6$
  pair admits SOME SUP-1 witness" fails 0/37. Per-pair rates: rule
  211/698 pairs, SUP-1 245/698.
- Max-$k_{12}$ pair selection: 10/37 only.
- Working pairs usually work through exactly ONE end edge (157/211
  single-edge; 46 double; 8 more). The pair choice is genuinely
  load-bearing; no greedy statistic found so far survives.

**Status.** Part 1 proved (elementary, from the dichotomy + cubic
geometry) — CHECK 2 (retained below) is its formalization-consistency
probe. Part 2 DISPROVED at R33 by `sup1_dead_tree`; its sampling probe
(formerly CHECK 1) was removed.

---

<!-- R33: CHECK 1 (the fixed-seed sampling probe for Part 2) formerly
here asserted the I-adjacent supply universal; it passed only by
sampling luck and was removed when Part 2 was disproved (see
lemma_sup1_dead_tree__0810-081024-1a40.md for the deterministic
counterexample).  CHECK 2 below tests Part 1 (proved) and stays. -->

<!-- CHECK
# sup1_iadj CHECK 2 (consistency probe, Part 1): for EVERY short cover
# of an I-adjacent boundary edge on sampled trees:
#   S2 (leg-top, A nonempty): a3 in V(I); met set ⊆ L_i single path
#      containing (m,c_i); k' = 1 + common descent below c_i.
#   S3 (A-bottom): met set ⊆ A single path containing e_A;
#      k' = d(a_deep) - max(d(a3), d(a_sh)); if both legs nonempty,
#      s3 not strictly below m.
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


def lca(u, v, depth, par):
    while depth[u] > depth[v]: u = par[u]
    while depth[v] > depth[u]: v = par[v]
    while u != v: u = par[u]; v = par[v]
    return u


def chain_edges(lo, hi, par):
    es = set(); u = lo
    while u != hi:
        p = par[u]; es.add((min(u, p), max(u, p))); u = p
    return es


rng = random.Random(20260809 + 732)
checked = 0
legtop_checked = 0
abottom_checked = 0

for nn, trials in ((12, 2500), (14, 2500), (16, 2500), (18, 1500)):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(trials):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(4):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            depth, par, be = res
            m = len(be)
            fc = [fund_cycle_edges(s, a, par) for s, a, _ in be]
            for x in range(m):
                for y in range(x + 1, m):
                    D = fc[x] ^ fc[y]
                    LD = single_cycle_len(D)
                    if LD is None: continue
                    k12 = (len(fc[x]) + len(fc[y]) - LD) // 2
                    if k12 < 1: continue
                    s1, a1, _ = be[x]; s2, a2, _ = be[y]
                    mm = lca(s1, s2, depth, par)
                    a_sh, a_deep = (a1, a2) if depth[a1] <= depth[a2] else (a2, a1)
                    A = chain_edges(a_deep, a_sh, par)
                    legtops = {}
                    for i_leg, snd in ((0, s1), (1, s2)):
                        if snd == mm: continue
                        c = snd
                        while par[c] != mm: c = par[c]
                        legtops[(min(mm, c), max(mm, c))] = (snd, c)
                    eA = None
                    if a_deep != a_sh:
                        p = par[a_deep]
                        eA = (min(a_deep, p), max(a_deep, p))
                    legs = {0: chain_edges(s1, mm, par), 1: chain_edges(s2, mm, par)}
                    for z in range(m):
                        if z in (x, y): continue
                        g3 = len(fc[z]) - 1
                        if g3 > k12 + 1: continue  # only SHORT covers
                        s3, a3, _ = be[z]
                        P3 = fc[z] - {(min(s3, a3), max(s3, a3))}
                        met = D & fc[z]
                        # leg-top case
                        for e, (snd, c) in legtops.items():
                            if e not in P3 or not A: continue
                            legtop_checked += 1; checked += 1
                            assert depth[a_deep] <= depth[a3] <= depth[mm], \
                                f"S2 a3 not in I: n={nn} root={r} edges={edges}"
                            Li = legs[0] if (snd == s1) else legs[1]
                            assert met <= Li and e in met, \
                                f"S2 met set escapes L_i: n={nn} root={r} edges={edges}"
                            # common descent below c
                            ell = 0
                            u1, u2 = s3, snd
                            ch3 = set(); u = s3
                            while u != c and depth[u] > depth[c]: ch3.add(u); u = par[u]
                            chL = set(); u = snd
                            while u != c and depth[u] > depth[c]: chL.add(u); u = par[u]
                            # walk down from c along both chains
                            common = ch3 & chL
                            # length of common prefix below c = number of shared
                            # vertices forming a chain from c downward
                            uu = c; ell = 0
                            while True:
                                nxt = [w for w in adj[uu]
                                       if w in common and depth[w] == depth[uu] + 1
                                       and par[w] == uu]
                                if not nxt: break
                                uu = nxt[0]; ell += 1
                            assert len(met) == 1 + ell, \
                                (f"S2 k' formula fails: met={len(met)} ell={ell} "
                                 f"n={nn} root={r} edges={edges}")
                        # A-bottom case
                        if eA is not None and eA in P3:
                            abottom_checked += 1; checked += 1
                            assert met <= A and eA in met, \
                                f"S3 met set escapes A: n={nn} root={r} edges={edges}"
                            kf = depth[a_deep] - max(depth[a3], depth[a_sh])
                            assert len(met) == kf, \
                                (f"S3 k' formula fails: met={len(met)} kf={kf} "
                                 f"n={nn} root={r} edges={edges}")
                            if s1 != mm and s2 != mm:
                                below = (depth[s3] > depth[mm]
                                         and is_ancestor(mm, s3, depth, par))
                                assert not below, \
                                    (f"S3 s3 strictly below m: n={nn} root={r} "
                                     f"edges={edges}")

assert legtop_checked > 500, f"too few leg-top configs: {legtop_checked}"
assert abottom_checked > 500, f"too few A-bottom configs: {abottom_checked}"
print(f"checked={checked} (legtop={legtop_checked}, abottom={abottom_checked}) "
      f"— S2/S3 cover-structure claims consistent with extraction code")
CHECK -->

## Summary

Two-part lemma at the cancelled interval's boundary. PROVED (Part 1):
a SHORT cover ($\operatorname{gap}_3 \le k_{12}+1$) through an
$I$-adjacent boundary edge is geometrically pinned — leg-top covers
anchor inside $I$ and meet only that leg with
$k' = 1 + (\text{common descent below } c_i)$; $A$-bottom covers meet
only $A$ with $k' = d(a_{\mathrm{deep}}) - \max(d(a_3),
d(a_{\mathrm{sh}}))$; explicit $k' = 1$ criteria at both. DISPROVED
(Part 2, R33): the $I$-adjacent min-gap supply conjecture — and every
weaker SUP-1 universal above it — fails on the pinned counterexample in
`sup1_dead_tree`. The R32 census (92/92, no far-edge tree observed) was
sampling luck. Quantifier negatives remain valid dead ends:
$\forall$-pair variants dead (0/37 both), max-$k_{12}$ selection dead
(10/37). Part 1's geometry survives for reuse in whatever supply
statement replaces SUP-1 (wider $k'$ channels or graph-level
quantification).
