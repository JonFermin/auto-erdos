---
id: straddle_floor_line
status: proved
depends_on: [fund_pair_overlap, pasting_meeting_structure, pasting_cover_dichotomy, shortpaste_floor_line]
discharged_by_round: null
introduced_at_round: 37
---

# Lemma `straddle_floor_line` (proved: arc dichotomy, exact slack formula, floor, and the 8-line for straddling covers)

**Setting.** As in `pasting_cover_dichotomy`: $T$ a normal (DFS)
spanning tree of a connected cubic graph; overlapping pair
$B_1 = (s_1, a_1)$, $B_2 = (s_2, a_2)$ with $k_{12} \ge 1$ shared tree
edges and $D = C_1 \triangle C_2$ a single cycle; segments
$A = [a_{\mathrm{deep}} .. a_{\mathrm{sh}}]$,
$L_i = [s_i .. m]$ ($m = \operatorname{lca}(s_1, s_2)$), cancelled
interval $I = [a_{\mathrm{deep}} .. m]$, $|I| = k_{12}$; so
$|D| = |A| + |L_1| + |L_2| + 2$. A third back edge $B_3 = (s_3, a_3)
\notin \{B_1, B_2\}$ with $D \cap C_3 \ne \emptyset$ is a cover; write
$k'' = |D \cap C_3|$, $g_3 = |C_3| - 1$, and
$\tilde L = |D \oplus C_3|$ (the sym-diff **edge count** — when
$D \oplus C_3$ is a single cycle, i.e. the pairing fires, $\tilde L$ is
its length, and the identity $\tilde L = |D| + g_3 + 1 - 2k''$ always
holds as edge counting).

For a **straddling** cover met on leg $L_i$ (unmet leg $L_j$), define
$w = \operatorname{lca}(s_3, s_i)$, $y = d(a_{\mathrm{deep}}) - d(a_3)$,
$k_A = |P_3 \cap A|$, $k_L = |P_3 \cap L_i|$, and the four **slacks**

$$\alpha_A = |A| - k_A, \quad \beta_A = y - k_A, \quad
\alpha_L = |L_i| - k_L = d(s_i) - d(w), \quad
\beta_L = d(s_3) - d(w).$$

**Claims (all proved below).**

1. **(Arc dichotomy — upgrades the R35 observed arc bound to a
   theorem.)** For every cover, each of $P_3 \cap A$, $P_3 \cap L_1$,
   $P_3 \cap L_2$ is a single (possibly empty) path, so the number of
   arcs of $D \cap C_3$ equals the number of segments met, which is 1
   (pasting) or 2 (straddling) by `pasting_cover_dichotomy`. In the
   straddling case the two arcs are vertex-disjoint: one in $A$
   (containing $A$'s deepest edge), one in $L_i$ (containing $L_i$'s top
   edge), and $k'' = k_A + k_L$ with $k_A, k_L \ge 1$.
2. **(Exact straddle formula.)** All four slacks are $\ge 0$ and
   $$\tilde L \;=\; k_{12} + 3 + |L_j| + \alpha_A + \beta_A + \alpha_L + \beta_L.$$
3. **(Coupling.)** $\alpha_A \cdot \beta_A = 0$: the anchor either stops
   inside $A$ (then $\beta_A = 0$) or overshoots above
   $a_{\mathrm{sh}}$ (then $k_A = |A|$, $\alpha_A = 0$).
4. **(Floor.)** $\tilde L \ge k_{12} + 3 + |L_j| \ge 4$. Moreover
   $\tilde L = 4$ forces $(k_{12}, |L_j|) = (1, 0)$ and all four slacks
   $= 0$; the straddle undershoot region $\tilde L \in \{4, 6\}$
   requires $k_{12} + |L_j| + \Sigma \le 3$, hence $k_{12} \le 3$.
5. **(8-line.)** $\tilde L = 8$ iff
   $k_{12} + |L_j| + \alpha_A + \beta_A + \alpha_L + \beta_L = 5$.
   Necessary conditions: $k_{12} \le 5$ and $|L_j| \le 4$.

(Parity remark: $\tilde L \equiv |D| + g_3 + 1 \pmod 2$ exactly as in
`shortpaste_floor_line`(P1) — the congruence uses only
$\tilde L = |D| + g_3 + 1 - 2k''$, which is arc-count-agnostic.)

**Proofs.**

*1.* Above $a_{\mathrm{deep}}$ the tree chain is unique, and both
anchors lie on the senders' common root-chain (`fund_pair_overlap`(1)),
so $A = [a_{\mathrm{deep}} .. a_{\mathrm{sh}}]$ and the portion of
$P_3$ above $a_{\mathrm{deep}}$ (namely $[a_{\mathrm{deep}} .. a_3]$,
$y$ edges, nonempty since $a_3$ is a strict ancestor of
$a_{\mathrm{deep}}$ by `pasting_cover_dichotomy`(b2)) are two intervals
on one chain sharing the endpoint $a_{\mathrm{deep}}$; their
intersection is the interval of $k_A = \min(y, |A|) \ge 1$ edges
starting at $a_{\mathrm{deep}}$ — a single path. Below $m$: $P_3$'s
lower portion $[s_3 .. m]$ and $L_i = [s_i .. m]$ are vertical chains
with the common endpoint $m$; two root-chains coincide exactly above
their lca, so the intersection is the interval $[w .. m]$ of
$k_L = d(w) - d(m)$ edges — a single path, and $k_L \ge 1$ because
$s_3, s_i$ lie in the same child subtree of $m$
(`pasting_cover_dichotomy`(b4)), putting $w$ strictly below $m$.
For a pasting cover the single met segment is one of these two
intervals-on-a-chain (or a leg), and the same
two-vertical-paths-intersect-in-a-path argument applies. Vertex
disjointness of the two straddle arcs: the $A$-arc's vertices have
depth $\le d(a_{\mathrm{deep}})$, the leg arc's have depth $\ge d(m) >
d(a_{\mathrm{deep}})$. Since $D \cap C_3 = P_3 \cap (A \sqcup L_1
\sqcup L_2)$ ($P_3$ is tree edges; $B_3 \notin \{B_1, B_2\}$; $I$ is
cancelled, $I \not\subseteq D$), $k'' = k_A + k_L$. $\square$

*2.* $P_3 = [s_3 .. a_3]$ is a vertical path through $m$ and
$a_{\mathrm{deep}}$ (it contains $I$, `pasting_cover_dichotomy`(b1)),
so $g_3 = x + k_{12} + y$ with $x = d(s_3) - d(m)$. Chains give
$x = k_L + \beta_L$ (split $[s_3..m]$ at $w$) and $y = k_A + \beta_A$
(claim 3's case split below), and $|A| = k_A + \alpha_A$,
$|L_i| = k_L + \alpha_L$ by definition. Substituting into the identity:
$$\tilde L = |D| + g_3 + 1 - 2k''
= (|A| + |L_i| + |L_j| + 2) + (x + k_{12} + y) + 1 - 2(k_A + k_L)$$
$$= (|A| - k_A) + (y - k_A) + (|L_i| - k_L) + (x - k_L) + |L_j| + k_{12} + 3
= \alpha_A + \beta_A + \alpha_L + \beta_L + |L_j| + k_{12} + 3.$$
Nonnegativity: $\alpha_A, \beta_A \ge 0$ since $k_A = \min(y, |A|)$;
$\alpha_L = d(s_i) - d(w) \ge 0$ and $\beta_L = d(s_3) - d(w) \ge 0$
since $w = \operatorname{lca}(s_3, s_i)$. $\square$

*3.* If $y \le |A|$: $k_A = y$, so $\beta_A = 0$. If $y > |A|$:
$k_A = |A|$, so $\alpha_A = 0$ (and $\beta_A = y - |A| =
d(a_{\mathrm{sh}}) - d(a_3)$, the overshoot above $a_{\mathrm{sh}}$).
Either way $y = k_A + \beta_A$. $\square$

*4.* Drop the (nonnegative) slacks from Claim 2 and use $k_{12} \ge 1$,
$|L_j| \ge 0$. Equality $\tilde L = 4$ forces every dropped term to
vanish and $k_{12} = 1$. For $\tilde L \in \{4, 6\}$:
$k_{12} + |L_j| + \Sigma = \tilde L - 3 \le 3$. $\square$

*5.* Immediate from Claim 2; the necessary conditions from
$k_{12} \ge 1$ and slacks $\ge 0$. $\square$

**Worked anchors (both $n = 10$, seed-20260812 sweep; re-verified
deterministically in CHECK 1).**

- *8-line instance*: root 1,
  $B_1 = (2, 1)$, $B_2 = (0, 3)$, $B_3 = (7, 8)$; $m = 4$,
  $a_{\mathrm{deep}} = 3$, $a_{\mathrm{sh}} = 1$, $k_{12} = 1$,
  $|A| = 5$, $|L_1| = 1$, $|L_2| = 2$, met leg $L_2$, $w = 7$,
  $y = 3$, $k_A = 3$, $k_L = 1$, so $k'' = 4$ and slacks
  $(\alpha_A, \beta_A, \alpha_L, \beta_L) = (2, 0, 1, 0)$. Formula:
  $1 + 3 + 1 + 2 + 0 + 1 + 0 = 8$; identity cross-check:
  $|D| = 10$, $g_3 = 5$, $\tilde L = 10 + 5 + 1 - 2 \cdot 4 = 8$. Both
  give 8, and $D \oplus C_3$ is a single 8-cycle (fires).
- *Floor-tight instance*: root 4, $B_1 = (3, 0)$, $B_2 = (1, 4)$,
  $B_3 = (3, 4)$; $m = 1$, $k_{12} = 1$, $|A| = 4$, $|L_1| = 4$,
  $|L_2| = 0$, met leg $L_1$, $w = 3$, $y = 4$, $k_A = 4$, $k_L = 4$,
  $k'' = 8$, all four slacks $= 0$. Formula: $1 + 3 + 0 + 0 = 4$;
  identity: $|D| = 10$, $g_3 = 9$, $10 + 9 + 1 - 16 = 4$. The
  $\tilde L = 4$ configuration is exactly the rigid one Claim 4
  predicts: $(k_{12}, |L_j|) = (1, 0)$, zero slack.

**Consequences for the program.**

- **(a) The value theory is now COMPLETE on both channels.** By Claim
  1 every usable pairing's third edge either pastes ($D \cap C_3$ a
  single path — `shortpaste_floor_line` gives the exact value line
  $g_3 = 2k' + 7 - |D|$) or straddles (Claims 2–5 give the exact value
  line $k_{12} + |L_j| + \Sigma = 5$). No third channel exists. The
  R35 census's "arc bound $\le 2$, observed 8,307/8,307" is no longer
  an empirical fact but a corollary.
- **(b) What `sup8_tree_universal` still needs is pure supply +
  firing**: on every pair-residual tree, some pair + cover sits on one
  of the two 8-lines AND $D \oplus C_3$ is a single cycle. The
  arithmetic no longer constrains anything; both lines have rich
  realizable solution sets (census: 6,331 fired straddle-8s across
  the seed-20260812 sweep, on top of the k''=1 line's 1,497 from R35).
- **(c) Cheap necessary conditions for straddle-8**: a pair can host a
  straddle-8 only if $k_{12} \le 5$ and $|L_j| \le 4$ — and the
  dominant observed pattern has $|L_j| = 0$ (an ancestor-type pair,
  one sender on the other's root-chain).

**Status.** Proved (interval combinatorics on tree chains + the three
cited structural lemmas). CHECK 1 re-derives both worked anchors
deterministically; CHECK 2 is a randomized formalization-consistency
census asserting Claims 1–5 on every straddle configuration extracted
by the census machinery.

---

<!-- CHECK
# straddle_floor_line CHECK 1 (deterministic worked anchors): recompute
# both n=10 anchors from raw graph data; assert every stated quantity.
def build(nn, edges, root, par):
    depth = [-1] * nn; depth[root] = 0
    pending = [v for v in range(nn) if v != root]
    while pending:
        nxt = []
        for v in pending:
            if depth[par[v]] >= 0: depth[v] = depth[par[v]] + 1
            else: nxt.append(v)
        assert len(nxt) < len(pending)
        pending = nxt
    tre = set()
    for v in range(nn):
        if v != root: tre.add((min(v, par[v]), max(v, par[v])))
    assert tre <= set(edges)
    return depth, tre

def vpath(lo, hi, par):
    es = set(); u = lo
    while u != hi:
        p = par[u]; es.add((min(u, p), max(u, p))); u = p
    return es

def fcyc(s, a, par):
    es = vpath(s, a, par); es.add((min(s, a), max(s, a))); return es

def lca(u, v, depth, par):
    while depth[u] > depth[v]: u = par[u]
    while depth[v] > depth[u]: v = par[v]
    while u != v: u = par[u]; v = par[v]
    return u

def scl(sym):
    if not sym: return None
    dg = {}
    for u, v in sym: dg[u] = dg.get(u, 0) + 1; dg[v] = dg.get(v, 0) + 1
    if any(d != 2 for d in dg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    st = next(iter(dg)); seen = {st}; stk = [st]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(sym) if len(seen) == len(dg) else None

def slacks(nn, edges, root, par, B1, B2, B3):
    depth, _ = build(nn, edges, root, par)
    s1, a1 = B1; s2, a2 = B2; s3, a3 = B3
    m = lca(s1, s2, depth, par)
    a_deep, a_sh = (a1, a2) if depth[a1] >= depth[a2] else (a2, a1)
    k12 = depth[m] - depth[a_deep]
    A = vpath(a_deep, a_sh, par)
    L1 = vpath(s1, m, par); L2 = vpath(s2, m, par)
    D = fcyc(s1, a1, par) ^ fcyc(s2, a2, par)
    assert scl(D) is not None and len(D) == len(A) + len(L1) + len(L2) + 2
    P3 = vpath(s3, a3, par); C3 = fcyc(s3, a3, par)
    met = [q for q, X in enumerate((A, L1, L2)) if P3 & X]
    assert len(met) == 2 and met[0] == 0, f"not a straddle: {met}"
    li = met[1]
    s_i = s1 if li == 1 else s2
    Li, Lj = (L1, L2) if li == 1 else (L2, L1)
    w = lca(s3, s_i, depth, par)
    kL = depth[w] - depth[m]
    y = depth[a_deep] - depth[a3]
    kA = min(y, len(A))
    assert kA == len(P3 & A) and kL == len(P3 & Li)
    assert len(D & C3) == kA + kL
    aA = len(A) - kA; bA = y - kA
    aL = len(Li) - kL; bL = depth[s3] - depth[w]
    assert aA * bA == 0 and min(aA, bA, aL, bL) >= 0
    Lt = len(D ^ C3)
    assert Lt == k12 + 3 + len(Lj) + aA + bA + aL + bL
    assert Lt == len(D) + (len(C3) - 1) + 1 - 2 * (kA + kL)
    return (k12, len(A), len(L1), len(L2), li, w, y, kA, kL,
            aA, bA, aL, bL, len(D), Lt, scl(D ^ C3))

# anchor 1: the 8-line instance
e1 = [(0, 7), (2, 4), (1, 2), (3, 4), (6, 8), (0, 3), (0, 6), (4, 7),
      (8, 9), (5, 9), (7, 8), (1, 6), (2, 5), (1, 9), (3, 5)]
r1 = slacks(10, [tuple(sorted(e)) for e in e1], 1,
            [7, -1, 4, 5, 3, 9, 1, 4, 6, 8], (2, 1), (0, 3), (7, 8))
assert r1 == (1, 5, 1, 2, 2, 7, 3, 3, 1, 2, 0, 1, 0, 10, 8, 8), r1

# anchor 2: the floor-tight L=4 instance
e2 = [(0, 1), (3, 4), (2, 7), (5, 8), (4, 9), (0, 3), (1, 4), (2, 9),
      (1, 7), (8, 9), (2, 6), (5, 6), (0, 5), (3, 6), (7, 8)]
r2 = slacks(10, [tuple(sorted(e)) for e in e2], 4,
            [5, 0, 7, 6, -1, 8, 2, 1, 9, 4], (3, 0), (1, 4), (3, 4))
assert r2 == (1, 4, 4, 0, 1, 3, 4, 4, 4, 0, 0, 0, 0, 10, 4, 4), r2

print("anchors OK: 8-line instance (slacks 2,0,1,0; k12=1, |Lj|=1) -> 8; "
      "floor-tight instance (all slacks 0; k12=1, |Lj|=0) -> 4")
CHECK -->

<!-- CHECK
# straddle_floor_line CHECK 2 (randomized consistency census): on every
# straddle configuration over sampled cubic DFS trees, assert
#   C1  arcs of D&C3 == segments met (<= 2); k'' = kA + kL
#   C2  |D^C3| == k12 + 3 + |Lj| + aA + bA + aL + bL, slacks >= 0
#   C3  aA * bA == 0
#   C4  |D^C3| >= k12 + 3 + |Lj| >= 4; == 4 only if k12==1, |Lj|==0, slacks 0
#   C5  |D^C3| == 8  <=>  k12 + |Lj| + sum(slacks) == 5
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
    tree = set()
    for v in range(n):
        if v != r: tree.add((min(v, par[v]), max(v, par[v])))
    nontree = []
    for e in edges:
        if e in tree: continue
        u, v = e
        a, b = (u, v) if depth[u] <= depth[v] else (v, u)
        if not is_ancestor(a, b, depth, par): return None
        nontree.append((b, a))
    return depth, par, nontree

def vpath_edges(lo, hi, par):
    es = set(); u = lo
    while u != hi:
        p = par[u]; es.add((min(u, p), max(u, p))); u = p
    return es

def fund_cycle_edges(s, a, par):
    es = vpath_edges(s, a, par); es.add((min(s, a), max(s, a))); return es

def lca(u, v, depth, par):
    while depth[u] > depth[v]: u = par[u]
    while depth[v] > depth[u]: v = par[v]
    while u != v: u = par[u]; v = par[v]
    return u

def single_cycle_len(sym):
    if not sym: return None
    dg = {}
    for u, v in sym: dg[u] = dg.get(u, 0) + 1; dg[v] = dg.get(v, 0) + 1
    if any(d != 2 for d in dg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    st = next(iter(dg)); seen = {st}; stk = [st]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(sym) if len(seen) == len(dg) else None

def n_arcs(es):
    if not es: return 0
    adjP = {}
    for u, v in es:
        adjP.setdefault(u, []).append(v); adjP.setdefault(v, []).append(u)
    seen = set(); comps = 0
    for s in list(adjP):
        if s in seen: continue
        comps += 1; seen.add(s); stk = [s]
        while stk:
            u = stk.pop()
            for w in adjP[u]:
                if w not in seen: seen.add(w); stk.append(w)
    return comps

rng = random.Random(20260812 + 37)
covers = 0; straddles = 0; fired = 0; l8 = 0; floor4 = 0
for nn in (10, 12, 14, 16):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(80):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(2):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            depth, par, be = res
            m = len(be)
            fc = [fund_cycle_edges(s, a, par) for s, a in be]
            pe = [vpath_edges(s, a, par) for s, a in be]
            for i in range(m):
                s1, a1 = be[i]
                for j in range(i + 1, m):
                    s2, a2 = be[j]
                    D = fc[i] ^ fc[j]
                    if single_cycle_len(D) is None: continue
                    mm = lca(s1, s2, depth, par)
                    a_deep, a_sh = (a1, a2) if depth[a1] >= depth[a2] else (a2, a1)
                    k12 = depth[mm] - depth[a_deep]
                    A = vpath_edges(a_deep, a_sh, par)
                    L1 = vpath_edges(s1, mm, par)
                    L2 = vpath_edges(s2, mm, par)
                    for z in range(m):
                        if z == i or z == j: continue
                        s3, a3 = be[z]
                        P3 = pe[z]
                        inters = [P3 & X for X in (A, L1, L2)]
                        ne = [q for q in range(3) if inters[q]]
                        if not ne: continue
                        covers += 1
                        DC3 = D & fc[z]
                        assert n_arcs(DC3) == len(ne) <= 2, \
                            f"C1 arcs != segments (n={nn}, root={r}, edges={edges}, be=({be[i]},{be[j]},{be[z]}))"
                        if len(ne) == 1: continue
                        straddles += 1
                        li = ne[1]
                        s_i = s1 if li == 1 else s2
                        Li = L1 if li == 1 else L2
                        Lj = L2 if li == 1 else L1
                        w = lca(s3, s_i, depth, par)
                        kL = depth[w] - depth[mm]
                        y = depth[a_deep] - depth[a3]
                        kA = min(y, len(A))
                        assert kA == len(inters[0]) and kL == len(inters[li]) \
                            and len(DC3) == kA + kL, \
                            f"C1 split fails (n={nn}, root={r}, edges={edges})"
                        aA = len(A) - kA; bA = y - kA
                        aL = len(Li) - kL; bL = depth[s3] - depth[w]
                        assert min(aA, bA, aL, bL) >= 0
                        assert aA * bA == 0, \
                            f"C3 coupling fails (n={nn}, root={r}, edges={edges})"
                        S = aA + bA + aL + bL
                        Lt = len(D ^ fc[z])
                        assert Lt == k12 + 3 + len(Lj) + S, \
                            f"C2 formula fails: {Lt} != {k12}+3+{len(Lj)}+{S} (n={nn}, root={r}, edges={edges}, be=({be[i]},{be[j]},{be[z]}))"
                        assert Lt >= k12 + 3 + len(Lj) >= 4, "C4 floor fails"
                        if Lt == 4:
                            floor4 += 1
                            assert k12 == 1 and len(Lj) == 0 and S == 0, \
                                "C4 rigidity fails"
                        assert (Lt == 8) == (k12 + len(Lj) + S == 5), "C5 fails"
                        if single_cycle_len(D ^ fc[z]) is not None:
                            fired += 1
                            if Lt == 8: l8 += 1

assert covers > 20000 and straddles > 5000, \
    f"probe vacuous: covers={covers} straddles={straddles}"
assert fired > 2500 and l8 > 250, f"too few fired: {fired} l8={l8}"
print(f"covers={covers} straddles={straddles} fired={fired} l8={l8} "
      f"floor4={floor4} — arc dichotomy, slack formula, coupling, floor, "
      f"and 8-line consistent on every straddle configuration")
CHECK -->

## Summary

Proved value theory for the straddle channel, completing the two-channel
program: (arc dichotomy) $D \cap C_3$ always has $\le 2$ arcs — exactly
the number of segments met — upgrading R35's 8,307/8,307 observation to
a theorem; (formula) a straddling cover satisfies $\tilde L = |D \oplus
C_3| = k_{12} + 3 + |L_j| + \alpha_A + \beta_A + \alpha_L + \beta_L$
with four nonnegative slacks and the coupling $\alpha_A \beta_A = 0$;
(floor) $\tilde L \ge k_{12} + 3 + |L_j| \ge 4$, with $\tilde L = 4$
forcing the rigid zero-slack $(1, 0)$ configuration; (8-line) $\tilde L
= 8$ iff $k_{12} + |L_j| + \Sigma = 5$, so straddle-8 needs $k_{12} \le
5$, $|L_j| \le 4$. Together with `shortpaste_floor_line` (the 1-arc
channel), every usable pairing's value is now governed by an exact
diophantine line; `sup8_tree_universal` reduces to supply + firing.
