---
id: paste8_projected_coords
status: proved
depends_on: [fund_pair_overlap, pasting_meeting_structure, paste8_samebranch_universal]
discharged_by_round: 46
introduced_at_round: 46
---

# Lemma `paste8_projected_coords` (proved): the same-branch paste predicate is pure interval arithmetic in projected coordinates

**Setting.** $T$ a normal (DFS) spanning tree of a connected cubic
graph, $(B_1, B_2)$ a **same-branch** pair (senders comparable) with
single-cycle sym-diff $D$ (`fund_pair_overlap`: $k_{12} \ge 1$). Write
$s_d$ for the deeper sender, $s_{sh}$ for the shallower,
$a_{dp}, a_{sh}$ for the deeper/shallower anchor, and let
$R = [\mathrm{root} \,..\, s_d]$ be the root path to $s_d$. All four
endpoints lie on $R$, and (`paste8_samebranch_universal`, vertical
calculus part 1) the tree part of $D$ is $A \sqcup E$ with
$A = [d(a_{sh}), d(a_{dp})]$, $E = [d(s_{sh}), d(s_d)]$, separated by
the cancelled overlap $I = [d(a_{dp}), d(s_{sh})]$ of length
$k_{12} \ge 1$ (depth intervals on $R$; lengths = differences).

**Definitions (projection).** For any third back edge
$B_3 = (s_3, a_3)$ let $x_3 = \operatorname{lca}(s_3, s_d)$, the vertex
where $s_3$'s root path leaves $R$ ($x_3 = s_3$ when $s_3 \in R$;
$x_3 = s_d$ when $s_3$ is a strict descendant of $s_d$). The
**projected interval** of $B_3$ on $R$ is
$\pi(B_3) = [d(a_3), d(x_3)]$ and its **off-chain weight** is
$\mathrm{off}(B_3) = g_3 - (d(x_3) - d(a_3))$, where $g_3 = |P_3|$ is
$B_3$'s gap.

**Claim (all parts proved below).** Suppose $D \cap C_3$ is a single
arc of $k' \ge 1$ edges (a paste cover, `pasting_meeting_structure`).
Then:

1. **(Anchoring.)** $a_3 \in R$, $d(a_3) < d(x_3)$ (so $\pi(B_3)$ has
   $\ge 1$ edge), and $\mathrm{off}(B_3) \ge 0$ with equality iff
   $s_3 \in R$.
2. **(The identity.)** As edge sets on $R$,
   $$D \cap C_3 \;=\; \pi(B_3) \cap A \quad\text{or}\quad
     \pi(B_3) \cap E,$$
   whichever is nonempty — and exactly one is. In particular
   $k' = |\pi(B_3) \cap A| + |\pi(B_3) \cap E|$ and the single-arc
   condition for a back edge whose projection is anchored on $R$ is
   simply "$\pi(B_3)$ meets exactly one of $A, E$ in an edge".
3. **(Slack in projected coordinates.)** $L = |D| + g_3 + 1 - 2k' = 8$
   iff
   $$\underbrace{(|A| + |E| - k')}_{\text{$D$-edges missed}}
     + \underbrace{(d(x_3) - d(a_3) - k')}_{\text{on-chain
     $P_3$-excess}} + \mathrm{off}(B_3) = 5.$$

**Consequence (Q74 handle (i) closed).** The paste-8 predicate on a
same-branch pair is a function of the **projected system on $R$
alone**: the pair's intervals $A, I, E$ plus, for each back edge, the
projected interval $\pi$ and scalar weight $\mathrm{off}$. No lca or
branching geometry survives — the entire same-branch supply question
(`paste8_samebranch_universal`) is now interval combinatorics on a
line, with foreign covers entering as intervals carrying a nonnegative
weight that spends slack. (`chain1d_falsifier_n14` shows the foreign
intervals are sometimes strictly necessary.)

## Proof

**(1)** $P_3$ is the vertical path $[a_3 \,..\, s_3]$, a sub-chain of
$s_3$'s root path $\mathrm{anc}(s_3)$. The vertex sets of
$\mathrm{anc}(s_3)$ and $R = \mathrm{anc}(s_d) \cup \{s_d\}$ are both
ancestor chains, and their intersection is the ancestor chain of
$x_3 = \operatorname{lca}(s_3, s_d)$, i.e. $[\mathrm{root} .. x_3]$.
Hence the edges of $P_3$ on $R$ are exactly those of
$[a_3 .. x_3]$ when $d(a_3) < d(x_3)$, and none otherwise (both $a_3$
and $x_3$ lie on $\mathrm{anc}(s_3)$, so they are comparable; if
$d(a_3) \ge d(x_3)$ then $P_3$ descends from $a_3$ entirely outside
$R$). The arc $D \cap C_3$ is contained in $A \sqcup E \subseteq E(R)$
and in $P_3$, so it is nonempty only if $P_3$ has edges on $R$,
forcing $a_3 \in R$ and $d(a_3) < d(x_3)$. Finally
$g_3 = |[a_3..x_3]| + |[x_3..s_3]| = (d(x_3) - d(a_3)) +
\mathrm{off}(B_3)$ with $\mathrm{off}(B_3) = d(s_3) - d(x_3) \ge 0$,
zero iff $x_3 = s_3$ iff $s_3 \in R$. $\square$

**(2)** $D \cap C_3$ contains no back edges ($B_3 \ne B_1, B_2$ and
$B_1, B_2 \notin C_3$), so $D \cap C_3 = P_3 \cap (A \sqcup E)$. By
(1) the edges of $P_3$ on $R$ are $[a_3..x_3] = \pi(B_3)$, and
$A, E \subseteq E(R)$, so
$D \cap C_3 = (\pi \cap A) \sqcup (\pi \cap E)$. These two edge sets
are depth intervals separated by the $k_{12} \ge 1$ edges of $I$, so
they lie in different components whenever both are nonempty. The
single-arc hypothesis therefore forces exactly one to be nonempty, and
the arc equals it; $k'$ is its length. (Conversely, if exactly one is
nonempty the intersection is a single vertical interval; the
stray-vertex condition is automatic in cubic trees by
`pasting_vertex_automatic`.) $\square$

**(3)** Substitute $|D| = |A| + |E| + 2$ and
$g_3 = (d(x_3) - d(a_3)) + \mathrm{off}(B_3)$ into
$L - 3 = |A| + |E| + g_3 - 2k'$
(`paste8_samebranch_universal` part 3). $\square$

**Worked anchors (any re-derivation must reproduce these exactly).**
On `chain1d_falsifier_n14` every one of the 6 same-branch paste-8
witnesses has a foreign cover; the slack splits
$(|A|{+}|E|{-}k',\ g_3{-}k')$ are $(0,5) \times 2$ and
$(3,2) \times 4$, and the foreign term decomposes as
$g_3 - k' = (d(x_3) - d(a_3) - k') + \mathrm{off}$ with
$\mathrm{off} \ge 1$. Across the R46 census (9 pins + 43 fresh
residual trees, 567 same-branch paste-8 witnesses) the identity in (2)
held with zero exceptions, and foreign off-chain weights were
$\mathrm{off} \in \{1{:}81,\ 2{:}17,\ 3{:}4,\ 4{:}3\}$ — small but
nonzero, confirming off spends slack without entering the arc.

<!-- CHECK
# paste8_projected_coords CHECK (deterministic, 9 pinned trees): for
# EVERY same-branch pair with single-cycle D and EVERY third back edge
# meeting D in a single arc (any L, not just 8), verify
#   arc == [d(a3), d(x3)] ∩ side  (side = the unique one of A, E met),
#   k' == that overlap length, a3 on R, d(a3) < d(x3), off >= 0,
# and that pi meets exactly one of A, E.
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

def check_tree(name, nn, edges, root, par, counters):
    edges = [tuple(sorted(e)) for e in edges]
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
    def is_anc(u, v):
        if depth[u] > depth[v]: return False
        x = v
        while depth[x] > depth[u]: x = par[x]
        return x == u
    def lca(u, v):
        a, b = u, v
        while depth[a] > depth[b]: a = par[a]
        while depth[b] > depth[a]: b = par[b]
        while a != b: a = par[a]; b = par[b]
        return a
    def fcyc(s, a):
        es = set(); u = s
        while u != a:
            p = par[u]; es.add((min(u, p), max(u, p))); u = p
        es.add((min(s, a), max(s, a)))
        return es
    be = []
    for e in edges:
        if e in tre: continue
        u, v = e
        a, b = (u, v) if depth[u] <= depth[v] else (v, u)
        assert is_anc(a, b), "non-ancestral non-tree edge"
        be.append((b, a))
    fc = [fcyc(s, a) for s, a in be]
    pe = [c - {(min(s, a), max(s, a))} for c, (s, a) in zip(fc, be)]
    m = len(fc)
    for i in range(m):
        s1, a1 = be[i]
        for j in range(i + 1, m):
            s2, a2 = be[j]
            if not (s1 == s2 or is_anc(s1, s2) or is_anc(s2, s1)):
                continue
            D = set(fc[i] ^ fc[j])
            if single_cycle_len(D) is None: continue
            sd = s1 if depth[s1] >= depth[s2] else s2
            A_lo = min(depth[a1], depth[a2]); A_hi = max(depth[a1], depth[a2])
            E_lo = min(depth[s1], depth[s2]); E_hi = depth[sd]
            assert (A_hi - A_lo) + (E_hi - E_lo) + 2 == len(D)
            for z in range(m):
                if z == i or z == j: continue
                arc = D & pe[z]
                if not arc or n_arcs(arc) != 1: continue
                kp = len(arc); s3, a3 = be[z]; g3 = len(pe[z])
                x3 = lca(s3, sd)
                # (1) anchoring
                assert is_anc(a3, sd) or a3 == sd, f"{name}: a3 not on R"
                assert depth[a3] < depth[x3], f"{name}: empty projection"
                off = g3 - (depth[x3] - depth[a3])
                assert off >= 0, f"{name}: negative off"
                assert (off == 0) == (x3 == s3), f"{name}: off/onR mismatch"
                # (2) identity: arc == proj ∩ side, exactly one side met
                p_lo, p_hi = depth[a3], depth[x3]
                capA = (max(p_lo, A_lo), min(p_hi, A_hi))
                capE = (max(p_lo, E_lo), min(p_hi, E_hi))
                lenA_ov = max(0, capA[1] - capA[0])
                lenE_ov = max(0, capE[1] - capE[0])
                assert (lenA_ov > 0) != (lenE_ov > 0), \
                    f"{name}: pi meets both/neither of A, E"
                lo, hi = (capA if lenA_ov else capE)
                ds = sorted(min(depth[u], depth[v]) for u, v in arc)
                assert (ds[0], ds[-1] + 1) == (lo, hi) and kp == hi - lo \
                    and len(ds) == kp, f"{name}: arc != proj∩side"
                counters[0] += 1
                if (A_hi - A_lo) + (E_hi - E_lo) + g3 + 3 - 2 * kp == 8:
                    counters[1] += 1

PINS = [
    ("l8_exactness_dead", 12,
     [(4, 10), (1, 2), (5, 11), (0, 10), (5, 8), (3, 7), (6, 8), (2, 10),
      (1, 4), (0, 6), (6, 7), (4, 5), (8, 9), (2, 9), (1, 7), (3, 9),
      (0, 11), (3, 11)],
     10, [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0]),
    ("sup1_dead_tree", 14,
     [(5, 13), (0, 2), (10, 12), (1, 3), (7, 10), (6, 8), (4, 8), (3, 6),
      (3, 12), (5, 9), (4, 11), (0, 1), (9, 10), (1, 2), (9, 13), (0, 4),
      (2, 7), (6, 13), (5, 11), (11, 12), (7, 8)],
     11, [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5]),
    ("viol1_n30", 30,
     [(0, 18), (0, 22), (0, 27), (1, 9), (1, 18), (1, 29), (2, 4), (2, 5),
      (2, 20), (3, 6), (3, 17), (3, 29), (4, 25), (4, 28), (5, 12), (5, 27),
      (6, 8), (6, 11), (7, 9), (7, 14), (7, 27), (8, 19), (8, 20), (9, 12),
      (10, 15), (10, 16), (10, 24), (11, 15), (11, 23), (12, 13), (13, 23),
      (13, 26), (14, 21), (14, 26), (15, 21), (16, 17), (16, 22), (17, 20),
      (18, 19), (19, 26), (21, 25), (22, 28), (23, 25), (24, 28), (24, 29)],
     20,
     [27, 9, 4, 29, 28, 2, 3, 14, 19, 12, 16, 6, 5, 23, 21, 10, 17, 20, 19,
      26, -1, 15, 0, 11, 29, 23, 13, 7, 22, 1]),
    ("viol2_n30", 30,
     [(0, 3), (0, 16), (0, 17), (1, 5), (1, 19), (1, 20), (2, 10), (2, 22),
      (2, 28), (3, 12), (3, 19), (4, 20), (4, 21), (4, 23), (5, 11), (5, 28),
      (6, 11), (6, 24), (6, 26), (7, 11), (7, 27), (7, 29), (8, 18), (8, 23),
      (8, 29), (9, 12), (9, 20), (9, 24), (10, 13), (10, 23), (12, 25),
      (13, 18), (13, 21), (14, 15), (14, 27), (14, 28), (15, 17), (15, 26),
      (16, 21), (16, 25), (17, 22), (18, 24), (19, 26), (22, 29), (25, 27)],
     25,
     [17, 5, 10, 12, 21, 11, 26, 29, 23, 20, 13, 7, 9, 18, 28, 14, 25, 15,
      24, 3, 1, 16, 17, 4, 6, -1, 19, 14, 2, 8]),
    ("viol3_n40", 40,
     [(0, 7), (0, 36), (0, 38), (1, 16), (1, 24), (1, 35), (2, 16), (2, 33),
      (2, 34), (3, 5), (3, 12), (3, 20), (4, 13), (4, 29), (4, 34), (5, 18),
      (5, 21), (6, 19), (6, 21), (6, 32), (7, 14), (7, 33), (8, 18), (8, 22),
      (8, 26), (9, 17), (9, 21), (9, 28), (10, 14), (10, 15), (10, 36),
      (11, 18), (11, 28), (11, 29), (12, 24), (12, 34), (13, 22), (13, 25),
      (14, 23), (15, 19), (15, 35), (16, 23), (17, 26), (17, 35), (19, 20),
      (20, 37), (22, 36), (23, 38), (24, 33), (25, 27), (25, 39), (26, 32),
      (27, 30), (27, 32), (28, 37), (29, 31), (30, 31), (30, 37), (31, 39),
      (38, 39)],
     1,
     [36, -1, 33, 5, 34, 21, 19, 0, 18, 17, 14, 29, 24, 4, 23, 10, 2, 35,
      11, 20, 3, 9, 13, 16, 1, 39, 8, 32, 11, 31, 27, 30, 6, 7, 12, 15, 22,
      28, 39, 31]),
    ("surv_thin_n32", 32,
     [(0, 17), (0, 21), (0, 23), (1, 20), (1, 23), (1, 28), (2, 17), (2, 19),
      (2, 27), (3, 9), (3, 25), (3, 28), (4, 16), (4, 22), (4, 26), (5, 7),
      (5, 8), (5, 26), (6, 10), (6, 11), (6, 12), (7, 15), (7, 24), (8, 25),
      (8, 27), (9, 12), (9, 20), (10, 30), (10, 31), (11, 13), (11, 17),
      (12, 21), (13, 24), (13, 31), (14, 16), (14, 28), (14, 30), (15, 18),
      (15, 25), (16, 18), (18, 20), (19, 23), (19, 24), (21, 29), (22, 27),
      (22, 29), (26, 31), (29, 30)],
     18,
     [17, 28, 27, 9, 22, 7, 11, 15, 5, 20, 31, 13, 6, 24, 16, 25, 18, 2,
      -1, 23, 1, 12, 29, 0, 19, 3, 4, 8, 14, 21, 10, 26]),
    ("surv_kp5_n32", 32,
     [(0, 1), (0, 9), (0, 25), (1, 7), (1, 15), (2, 3), (2, 18), (2, 27),
      (3, 24), (3, 29), (4, 5), (4, 15), (4, 16), (5, 26), (5, 31), (6, 16),
      (6, 23), (6, 25), (7, 8), (7, 19), (8, 27), (8, 29), (9, 20), (9, 22),
      (10, 17), (10, 23), (10, 31), (11, 28), (11, 29), (11, 30), (12, 13),
      (12, 15), (12, 19), (13, 18), (13, 26), (14, 22), (14, 23), (14, 30),
      (16, 24), (17, 22), (17, 27), (18, 20), (19, 28), (20, 21), (21, 24),
      (21, 30), (25, 31), (26, 28)],
     7,
     [1, 15, 18, 29, 16, 31, 23, -1, 7, 22, 17, 28, 13, 26, 30, 4, 6, 27,
      20, 12, 9, 24, 14, 10, 3, 0, 5, 2, 19, 8, 21, 25]),
    ("surv_kp5_n40", 40,
     [(0, 10), (0, 31), (0, 32), (1, 20), (1, 22), (1, 36), (2, 7), (2, 17),
      (2, 33), (3, 22), (3, 34), (3, 35), (4, 25), (4, 27), (4, 29), (5, 18),
      (5, 27), (5, 33), (6, 26), (6, 33), (6, 38), (7, 13), (7, 16), (8, 25),
      (8, 26), (8, 39), (9, 32), (9, 34), (9, 36), (10, 15), (10, 16),
      (11, 19), (11, 31), (11, 35), (12, 23), (12, 32), (12, 37), (13, 29),
      (13, 30), (14, 16), (14, 19), (14, 30), (15, 23), (15, 39), (17, 24),
      (17, 28), (18, 21), (18, 37), (19, 20), (20, 34), (21, 24), (21, 25),
      (22, 30), (23, 24), (26, 35), (27, 38), (28, 36), (28, 37), (29, 39),
      (31, 38)],
     31,
     [32, 20, 33, 22, 25, 27, 38, 16, 39, 36, 0, 35, 37, 7, 19, 23, 14, 2,
      5, 11, 34, 24, 30, 12, 17, 21, 8, 4, 36, 13, 13, -1, 9, 6, 3, 26, 1,
      18, 31, 15]),
    ("chain1d_falsifier_n14", 14,
     [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 7), (3, 11), (3, 12),
      (4, 8), (4, 11), (5, 9), (5, 11), (5, 13), (6, 7), (6, 12),
      (6, 13), (7, 8), (8, 10), (9, 10), (9, 13), (10, 12)],
     1, [4, -1, 1, 11, 8, 13, 13, 2, 7, 10, 12, 4, 3, 9]),
]

counters = [0, 0]
for name, nn, edges, root, par in PINS:
    check_tree(name, nn, edges, root, par, counters)
assert counters[0] >= 300, f"too few covers checked: {counters[0]}"
assert counters[1] == 91, f"paste-8 witness count changed: {counters[1]}"
print(f"projected-coordinate identity holds on all {counters[0]} "
      f"same-branch single-arc covers across the 9 pins "
      f"({counters[1]} of them paste-8 witnesses)")
CHECK -->

## Summary

Proved: for a same-branch pair on root chain $R$, every paste cover
$B_3$ — foreign or not — acts on $R$ through its projected interval
$\pi(B_3) = [d(a_3), d(\operatorname{lca}(s_3, s_d))]$ alone: the arc
is exactly $\pi \cap A$ or $\pi \cap E$ (whichever is nonempty; the
single-arc condition is "exactly one"), $k'$ is that overlap length,
and the off-chain tail of $B_3$ enters the $L = 8$ slack identity as a
nonnegative scalar weight. Hence the same-branch paste-8 predicate is
pure interval arithmetic in the projected system on one root chain —
Q74's handle (i). Verified deterministically on all 9 pins (this
CHECK) and on 43 fresh residual trees / 567 witnesses in the R46
census (zero exceptions).
