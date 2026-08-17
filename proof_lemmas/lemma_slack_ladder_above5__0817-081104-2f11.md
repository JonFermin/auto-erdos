---
id: slack_ladder_above5
status: disproved
depends_on: [paste8_samebranch_universal, paste8_projected_coords]
discharged_by_round: 46
introduced_at_round: 46
---

# Lemma `slack_ladder_above5` (DISPROVED at introduction, R46: the same-branch slack set is NOT gap-free above 5)

**DISPROOF (R46, same round as introduction — the designated SA
falsifier killed the claim in under 30 seconds of search time, before
any analytic effort was spent).** The falsifier `ladder_gap9_n14` is
the `chain1d_falsifier_n14` GRAPH re-rooted at vertex 0: pair-residual,
odd same-branch slack set $\{3, 5, 7, 11\}$ — max $= 11 \ge 5$ but
**9 is missing**. Independently re-verified with the set-based
enumerator (fundamental-cycle symmetric differences and explicit arc
computation, no projected-coordinate shortcut). Pinned in CHECK 3
below (CHECKs of disproved lemmas are runtime-skipped; kept for
audit).

Worse for any weakened ladder: a second confirmed falsifier
(cold-start SA, $n = 16$, root 2,
`par=[5,12,-1,4,11,6,1,2,10,0,9,7,13,3,8,10]`,
`edges=[(0,5),(0,9),(0,14),(1,6),(1,11),(1,12),(2,7),(2,8),(2,13),
(3,4),(3,12),(3,13),(4,7),(4,11),(5,6),(5,14),(6,15),(7,11),(8,10),
(8,14),(9,10),(9,15),(10,15),(12,13)]`) has odd set
$\{3, 5, 9, 11, 13\}$ — **7 missing**. SA also produced misses at 9
and 11 from multiple starts. Conclusion: **no odd slack value above 5
is universally forced; 5 stands alone.** The descent/pigeonhole route
to slack-5 attainment (H)+(D) is dead as stated. Both falsifiers
still contain slack 5 — `paste8_samebranch_universal` survives on
every state the SA visited (all runs, zero samebranch falsifiers).

**Method lesson (3rd instance of the pattern: chain1d R45,
full-interval R46, this).** Random-DFS censuses at $10^5$-tree scale
(124k census + 56k probe CHECK, 63 residual trees, zero ladder
violations) repeatedly fail to find what direct SA finds in seconds —
even a bare RE-ROOT of an existing pin was a falsifier. Never promote
a census regularity to a conjecture without running the SA falsifier
in the same round.

---

Original conjecture text follows (for the record).

**Setting.** $T$ a pair-residual normal spanning tree of a connected
cubic graph. The **same-branch slack set** is
$$S(T) = \{\, |A| + |E| + g_3 - 2k' \,\}$$
over all same-branch pairs with single-cycle sym-diff $D$
(`fund_pair_overlap`, $k_{12} \ge 1$) and all third back edges meeting
$D$ in a single arc of $k' \ge 1$ edges. By
`paste8_samebranch_universal` part 3, slack $= L - 3$, so slack
$5 \in S(T)$ iff $T$ has a same-branch paste-8. Write
$S_{\mathrm{odd}}(T)$ for the odd part.

**Claim (open, universally quantified — sampling can only falsify).**
For every pair-residual normal spanning tree of a connected cubic
graph: $\max S_{\mathrm{odd}}(T) \ge 5$ and
$$\{5, 7, 9, \dots, \max S_{\mathrm{odd}}(T)\} \subseteq
  S_{\mathrm{odd}}(T).$$

**Relation to the program.** Strictly stronger than
`paste8_samebranch_universal` (it implies $5 \in S(T)$). Its value is
the induced proof decomposition, the R23 (T1)–(T3) program transported
to projected coordinates (`paste8_projected_coords`):

- **(H) High endpoint**: some same-branch config attains ODD slack
  $\ge 5$. Candidate: minimal-overlap covers ($k' = 1$) with long
  $g_3$; a residual tree's gaps avoid $\{3, 7, 15, 31\}$ and cubic
  DFS trees have deep chains.
- **(D) Descent**: from any config of odd slack $s \ge 7$, produce one
  of slack $s - 2$. In projected coordinates a $-2$ step is: extend
  the arc by one edge ($k' \mathrel{+}= 1$, needs
  $\pi \cap \mathrm{side}$ to have room on both terms), or shorten
  the pair ($|A| + |E| \mathrel{-}= 2$), or swap $B_3$ for a cover
  with $g_3 - 2$ — all local moves on the interval system of ONE
  root chain.

(H) + (D) $\Rightarrow 5 \in S(T) \Rightarrow$
`paste8_samebranch_universal` $\Rightarrow$ `paste8_tree_universal`'s
supply on the same-branch channel.

**The full-interval strengthening is DEAD (do NOT revisit).** The
unrestricted form "$S_{\mathrm{odd}}(T)$ is a step-2 interval" is
falsified by the pinned tree `ladder_gap3_n16` (CHECK 1): its odd
slack set is $\{1, 5, 7, 9, 11\}$ — slack 1 is attainable while
slack 3 is NOT. Descent can fail below 5; the claim is deliberately
anchored at 5. (This also warns that (D)'s descent move needs the
$s \ge 7$ hypothesis — whatever obstructs $1 \leftarrow 3$ descent on
`ladder_gap3_n16` must be shown impossible above 5.)

**Evidence (R46 census, session s_0817-081104-2f11).**

- All 9 pinned trees comply, with exact odd slack sets asserted in
  CHECK 1: `l8_exactness_dead` $\{1,3,5,7\}$, `sup1_dead_tree`
  $\{3..11\}$, `viol1_n30` $\{3..25\}$, `viol2_n30` $\{3..25\}$,
  `viol3_n40` $\{3..31\}$, `surv_thin_n32` $\{3..25\}$,
  `surv_kp5_n32` $\{5..27\}$, `surv_kp5_n40` $\{3..33\}$,
  `chain1d_falsifier_n14` $\{3,5,7,9\}$ (all step-2 ranges). The
  hardened pins have wide gap-free ladders — adversarial pressure on
  paste-8 availability did not thin the slack ladder.
- Census seed 20260817+46 ($n \in \{12..22\}$, 124,000 trees, 43
  fresh pair-residual): 43/43 satisfy the ladder; exactly ONE
  (`ladder_gap3_n16`) violates the full-interval form.
- Fresh-seed probe (CHECK 2, seed 20260817+146): every sampled
  pair-residual tree satisfies the ladder.

**Designated falsifier (run BEFORE analytic effort — standing dual-attack
policy, R45 lesson).** Wide-class SA (no girth floor, per R45), energy
= (residuality violations, then #odd slack values in
$[5, \max]$ missing from $S_{\mathrm{odd}}$ — maximize gaps), moves =
cubic 2-opt + DFS re-root, warm restarts from `ladder_gap3_n16` (the
only known tree where ANY odd gap occurs) and the 8 pins. If SA finds
a residual tree with a gap above 5, this lemma dies and the descent
program retargets the gap anatomy.

<!-- CHECK
# slack_ladder_above5 CHECK 1 (deterministic pins): exact odd
# slack sets on the 9 standing pins + the new ladder_gap3_n16 pin.
# ladder_gap3_n16 has odd set {1,5,7,9,11}: full-interval form DEAD
# (3 missing), ladder-above-5 holds.
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

def slack_odd(nn, edges, root, par):
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
    m = len(fc); sl = set()
    for i in range(m):
        s1 = be[i][0]
        for j in range(i + 1, m):
            s2 = be[j][0]
            if not (s1 == s2 or is_anc(s1, s2) or is_anc(s2, s1)): continue
            D = set(fc[i] ^ fc[j])
            if single_cycle_len(D) is None: continue
            for z in range(m):
                if z == i or z == j: continue
                arc = D & pe[z]
                if not arc or n_arcs(arc) != 1: continue
                sl.add(len(D) - 2 + len(pe[z]) - 2 * len(arc))
    return sorted(s for s in sl if s % 2 == 1)

PINS = [
    ("l8_exactness_dead", 12,
     [(4, 10), (1, 2), (5, 11), (0, 10), (5, 8), (3, 7), (6, 8), (2, 10),
      (1, 4), (0, 6), (6, 7), (4, 5), (8, 9), (2, 9), (1, 7), (3, 9),
      (0, 11), (3, 11)],
     10, [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0], [1, 3, 5, 7]),
    ("sup1_dead_tree", 14,
     [(5, 13), (0, 2), (10, 12), (1, 3), (7, 10), (6, 8), (4, 8), (3, 6),
      (3, 12), (5, 9), (4, 11), (0, 1), (9, 10), (1, 2), (9, 13), (0, 4),
      (2, 7), (6, 13), (5, 11), (11, 12), (7, 8)],
     11, [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5],
     [3, 5, 7, 9, 11]),
    ("viol1_n30", 30,
     [(0, 18), (0, 22), (0, 27), (1, 9), (1, 18), (1, 29), (2, 4), (2, 5),
      (2, 20), (3, 6), (3, 17), (3, 29), (4, 25), (4, 28), (5, 12), (5, 27),
      (6, 8), (6, 11), (7, 9), (7, 14), (7, 27), (8, 19), (8, 20), (9, 12),
      (10, 15), (10, 16), (10, 24), (11, 15), (11, 23), (12, 13), (13, 23),
      (13, 26), (14, 21), (14, 26), (15, 21), (16, 17), (16, 22), (17, 20),
      (18, 19), (19, 26), (21, 25), (22, 28), (23, 25), (24, 28), (24, 29)],
     20,
     [27, 9, 4, 29, 28, 2, 3, 14, 19, 12, 16, 6, 5, 23, 21, 10, 17, 20, 19,
      26, -1, 15, 0, 11, 29, 23, 13, 7, 22, 1], list(range(3, 26, 2))),
    ("viol2_n30", 30,
     [(0, 3), (0, 16), (0, 17), (1, 5), (1, 19), (1, 20), (2, 10), (2, 22),
      (2, 28), (3, 12), (3, 19), (4, 20), (4, 21), (4, 23), (5, 11), (5, 28),
      (6, 11), (6, 24), (6, 26), (7, 11), (7, 27), (7, 29), (8, 18), (8, 23),
      (8, 29), (9, 12), (9, 20), (9, 24), (10, 13), (10, 23), (12, 25),
      (13, 18), (13, 21), (14, 15), (14, 27), (14, 28), (15, 17), (15, 26),
      (16, 21), (16, 25), (17, 22), (18, 24), (19, 26), (22, 29), (25, 27)],
     25,
     [17, 5, 10, 12, 21, 11, 26, 29, 23, 20, 13, 7, 9, 18, 28, 14, 25, 15,
      24, 3, 1, 16, 17, 4, 6, -1, 19, 14, 2, 8], list(range(3, 26, 2))),
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
      28, 39, 31], list(range(3, 32, 2))),
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
      -1, 23, 1, 12, 29, 0, 19, 3, 4, 8, 14, 21, 10, 26],
     list(range(3, 26, 2))),
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
      20, 12, 9, 24, 14, 10, 3, 0, 5, 2, 19, 8, 21, 25],
     list(range(5, 28, 2))),
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
      18, 31, 15], list(range(3, 34, 2))),
    ("chain1d_falsifier_n14", 14,
     [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 7), (3, 11), (3, 12),
      (4, 8), (4, 11), (5, 9), (5, 11), (5, 13), (6, 7), (6, 12),
      (6, 13), (7, 8), (8, 10), (9, 10), (9, 13), (10, 12)],
     1, [4, -1, 1, 11, 8, 13, 13, 2, 7, 10, 12, 4, 3, 9], [3, 5, 7, 9]),
    ("ladder_gap3_n16", 16,
     [(6, 15), (3, 4), (4, 12), (5, 13), (0, 5), (8, 12), (1, 6), (8, 15),
      (2, 11), (1, 15), (7, 10), (6, 14), (3, 9), (4, 11), (0, 7), (10, 11),
      (2, 13), (3, 5), (12, 14), (0, 9), (8, 10), (2, 9), (1, 13), (7, 14)],
     5, [7, 6, 13, 9, 3, -1, 15, 10, 12, 2, 11, 4, 14, 5, 7, 8],
     [1, 5, 7, 9, 11]),
]

for name, nn, edges, root, par, expect in PINS:
    got = slack_odd(nn, edges, root, par)
    assert got == expect, f"{name}: odd slack set {got} != {expect}"
    assert got[-1] >= 5 and all(
        s in got for s in range(5, got[-1] + 1, 2)), f"{name}: ladder FAILS"
gap = slack_odd(*[p[1:5] for p in PINS if p[0] == "ladder_gap3_n16"][0])
assert 1 in gap and 3 not in gap, "ladder_gap3_n16 anomaly changed"
print("pins OK: odd slack sets exact on all 10; ladder-above-5 holds "
      "everywhere; ladder_gap3_n16 pins the death of the full-interval "
      "form (1 attainable, 3 not)")
CHECK -->

<!-- CHECK
# slack_ladder_above5 CHECK 3 (deterministic pin, ladder_gap9_n14 —
# the DISPROOF): the chain1d_falsifier_n14 graph re-rooted at 0 is
# pair-residual with odd same-branch slack set {3, 5, 7, 11}: max 11,
# 9 MISSING (ladder falsified), 5 present (samebranch survives).
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

nn = 14; root = 0
par = [-1, 0, 1, 12, 8, 11, 13, 2, 6, 13, 7, 3, 10, 5]
edges = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 7), (3, 11), (3, 12),
         (4, 8), (4, 11), (5, 9), (5, 11), (5, 13), (6, 8), (6, 12),
         (6, 13), (7, 8), (7, 10), (9, 10), (9, 13), (10, 12)]
deg = {}
for u, v in edges: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
assert all(deg[v] == 3 for v in range(nn)), "not cubic"
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
def fcyc(s, a):
    es = set(); u = s
    while u != a:
        p = par[u]; es.add((min(u, p), max(u, p))); u = p
    es.add((min(s, a), max(s, a)))
    return es
be = []
for e in edges:
    e = tuple(sorted(e))
    if e in tre: continue
    u, v = e
    a, b = (u, v) if depth[u] <= depth[v] else (v, u)
    assert is_anc(a, b), "non-ancestral non-tree edge -- not a DFS tree"
    be.append((b, a))
fc = [fcyc(s, a) for s, a in be]
pe = [c - {(min(s, a), max(s, a))} for c, (s, a) in zip(fc, be)]
m = len(fc)
PO2 = {4, 8, 16, 32}
assert all(len(c) not in PO2 for c in fc), "fc violation"
for i in range(m):
    for j in range(i + 1, m):
        assert single_cycle_len(set(fc[i] ^ fc[j])) not in PO2, "pair fires"
sl = set()
for i in range(m):
    s1 = be[i][0]
    for j in range(i + 1, m):
        s2 = be[j][0]
        if s1 != s2 and not (is_anc(s1, s2) or is_anc(s2, s1)): continue
        D = set(fc[i] ^ fc[j])
        if single_cycle_len(D) is None: continue
        for z in range(m):
            if z == i or z == j: continue
            arc = D & pe[z]
            if not arc or n_arcs(arc) != 1: continue
            sl.add(len(D) - 2 + len(pe[z]) - 2 * len(arc))
odd = sorted(s for s in sl if s % 2 == 1)
assert odd == [3, 5, 7, 11], f"odd slack set changed: {odd}"
assert 9 not in sl and 5 in sl, "disproof shape changed"
print("ladder_gap9_n14 OK: pair-residual, odd slacks {3,5,7,11} -- 9 "
      "missing above 5 (slack_ladder_above5 DISPROVED), 5 present "
      "(paste8_samebranch_universal survives)")
CHECK -->

<!-- CHECK
# slack_ladder_above5 CHECK 2 (falsification probe, fresh seed
# 20260817+146): every sampled pair-residual cubic DFS tree has odd
# same-branch slack set gap-free from 5 to its max, with max >= 5.
# An assert failure prints the tree for pinning.  (~10s)
import random

PO2 = {4, 8, 16, 32}


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


def vpath(lo, hi, par):
    es = set(); u = lo
    while u != hi:
        p = par[u]; es.add((min(u, p), max(u, p))); u = p
    return es


def single_cycle_len(sym):
    if not sym: return None
    dg = {}
    for u, v in sym: dg[u] = dg.get(u, 0) + 1; dg[v] = dg.get(v, 0) + 1
    if any(dg[x] != 2 for x in dg): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    start = sorted(dg)[0]; sn = {start}; st = [start]
    while st:
        u = st.pop()
        for w in adjS[u]:
            if w not in sn: sn.add(w); st.append(w)
    return len(sym) if len(sn) == len(dg) else None


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


rng = random.Random(20260817 + 146)
trees_seen = 0; residual = 0
for nn, trials in ((12, 2500), (14, 2500), (16, 2000), (18, 1000)):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(trials):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(8):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            trees_seen += 1
            depth, par, be = res
            m = len(be)
            fc = []; pe = []
            for s, a in be:
                p = vpath(s, a, par)
                pe.append(frozenset(p))
                q = set(p); q.add((min(s, a), max(s, a)))
                fc.append(frozenset(q))
            if any(len(c) in PO2 for c in fc): continue
            pair_fire = False
            for i in range(m):
                for j in range(i + 1, m):
                    if single_cycle_len(set(fc[i] ^ fc[j])) in PO2:
                        pair_fire = True; break
                if pair_fire: break
            if pair_fire: continue
            residual += 1
            sl = set()
            for i in range(m):
                s1 = be[i][0]
                for j in range(i + 1, m):
                    s2 = be[j][0]
                    if s1 != s2 and not (
                            is_ancestor(s1, s2, depth, par)
                            or is_ancestor(s2, s1, depth, par)):
                        continue
                    D = set(fc[i] ^ fc[j])
                    if single_cycle_len(D) is None: continue
                    for z in range(m):
                        if z == i or z == j: continue
                        arc = D & pe[z]
                        if not arc or n_arcs(arc) != 1: continue
                        sl.add(len(D) - 2 + len(pe[z]) - 2 * len(arc))
            odd = sorted(s for s in sl if s % 2 == 1)
            ladder = (len(odd) > 0 and odd[-1] >= 5
                      and all(s in sl for s in range(5, odd[-1] + 1, 2)))
            assert ladder, \
                (f"FALSIFIED slack_ladder_above5: odd slacks {odd} "
                 f"(n={nn}, root={r}, par={par}, edges={edges})")

assert trees_seen > 40000, f"too few trees: {trees_seen}"
assert residual >= 20, f"too few residual trees: {residual} -- vacuous"
print(f"trees={trees_seen} residual={residual} -- odd same-branch slack "
      f"set gap-free from 5 to max on every pair-residual tree")
CHECK -->

## Summary

DISPROVED at introduction (R46). The census-suggested claim — odd
same-branch slack set gap-free from 5 to its max — was killed by its
designated SA falsifier within seconds: `ladder_gap9_n14` (the
`chain1d_falsifier_n14` graph re-rooted at 0, CHECK 3) is
pair-residual with odd slacks $\{3,5,7,11\}$, missing 9; a second
falsifier misses 7. No odd slack above 5 is universally forced — 5
stands alone, so the descent route (H)+(D) to slack-5 attainment is
dead, while `paste8_samebranch_universal` itself survived every SA
state. Third consecutive census-regularity killed by SA (chain1d,
full-interval, this): census scale $10^5$ random DFS trees is NOT
evidence — even a re-root of a standing pin was a falsifier.
