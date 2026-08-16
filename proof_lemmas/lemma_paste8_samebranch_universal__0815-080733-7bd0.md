---
id: paste8_samebranch_universal
status: open
depends_on: [paste8_tree_universal, leaf_pair_witness, crossing_pair_formula, fund_pair_overlap, shortpaste_floor_line]
discharged_by_round: null
introduced_at_round: 43
---

# Lemma `paste8_samebranch_universal` (conjecture + probe: every pair-residual tree has a paste-8 on a SAME-BRANCH pair)

**Setting.** $T$ a pair-residual normal spanning tree of a connected
cubic graph, as in `paste8_tree_universal`. Call a pair of back edges
$B_1 = (s_1, a_1)$, $B_2 = (s_2, a_2)$ **same-branch** if their senders
are comparable in tree order: $s_1 = s_2$ (a leaf pair, both back edges
of one DFS leaf) or one of $s_1, s_2$ is a strict ancestor of the other
(the nested and crossing pairs of the Section 61 taxonomy). Then all
four endpoints lie on one root chain $R$ (the root chain of the deeper
sender): anchors are ancestors of their senders, and comparable senders
share a chain.

**Vertical calculus (proved).** For a same-branch pair with
single-cycle $D = C_1 \oplus C_2$ (equivalently $k_{12} \ge 1$,
`fund_pair_overlap`):

1. **(Two-interval structure.)** The tree part of $D$ is
   $A \sqcup E$, where $A$ = the anchor interval (chain edges between
   $a_1$ and $a_2$) and $E$ = the sender interval (chain edges between
   $s_1$ and $s_2$; $E = \emptyset$ iff $s_1 = s_2$, $A = \emptyset$
   iff $a_1 = a_2$). Hence
   $|D| = |A| + |E| + 2 = |d(a_1)-d(a_2)| + |d(s_1)-d(s_2)| + 2$.
   *Proof.* $P_1$ and $P_2$ are depth-intervals on the common chain
   $R$; the symmetric difference of two overlapping (or nested)
   intervals on a line is the disjoint union of the interval between
   their left endpoints and the interval between their right
   endpoints. The cancelled overlap $I$ ($|I| = k_{12} \ge 1$)
   separates $A$ from $E$ on $R$. This unifies the proved
   same-sender ($|D| = \delta_1 - \delta_2 + 2$, `leaf_pair_witness`),
   nested, and crossing
   ($|D| = (d_{a_2}{-}d_{a_1}) + (d_{s_2}{-}d_{s_1}) + 2$,
   `crossing_pair_formula`) length formulas. $\square$

2. **(One-interval meets are automatic pastes.)** If a third back edge
   $B_3$'s tree path $P_3$ meets exactly one of $A, E$ in edges, then
   $D \cap C_3 = P_3 \cap (A \sqcup E)$ is a single arc: two vertical
   paths whose edge sets share a root chain intersect in a single
   depth-interval. If $P_3$ meets both $A$ and $E$, then (as in
   `pasting_cover_dichotomy`'s straddle branch) $P_3 \supseteq I$ and
   the intersection has two arcs — not a paste. $\square$

3. **(Slack form of the 8-line.)** For a paste cover as in (2) with
   $k' = |D \cap C_3| \ge 1$: $L = |D| + g_3 + 1 - 2k'$ and
   $$L = 8 \iff \underbrace{(|A| + |E| - k')}_{\text{$D$-tree edges
   missed}} + \underbrace{(g_3 - k')}_{\text{$P_3$ edges outside
   $D$}} = 5.$$
   *Proof.* $L - 3 = |A| + |E| + g_3 - 2k'$ since $|D| = |A|+|E|+2$.
   $\square$
   *Worked anchors (any re-derivation must reproduce these exactly).*
   Leaf pair $|A| = 3$, $E = \emptyset$, $|D| = 5$: cover $k' = 1$,
   $g_3 = 4$ gives $L = 5 + 4 + 1 - 2 = 8$, slack $(3-1)+(4-1) = 5$
   — on the line; cover $k' = 2$, $g_3 = 4$ gives
   $L = 5 + 4 + 1 - 4 = 6$, slack $(3-2)+(4-2) = 3 = L - 3$ — off
   the line. Chain pair $|A| = 2$, $|E| = 3$, $|D| = 7$: cover
   $k' = 3$, $g_3 = 6$ gives $L = 7 + 6 + 1 - 6 = 8$, slack
   $(5-3)+(6-3) = 5$ — on the line ($g_3 = 2k'+7-|D| = 6$,
   consistent with `shortpaste_floor_line`(4)).

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual normal spanning tree of a connected cubic graph
has a paste-channel $L = 8$ firing triple whose usable pairing is a
same-branch pair.

**Why this refinement matters.** Strictly stronger than
`paste8_tree_universal`, strictly weaker than the dead bounded-$k'$
forms — and it does NOT bound $k'$: on same-branch pairs
$k'$ scales with the met interval (observed same-branch min-$k'$
reaches 5 on the R41 pins), so it is compatible with the proved
unbounded-$k'$ burden (R40/R41). If it holds, the supply quantifier
collapses to ONE dimension: a witness is a root chain $R$, two back
edges whose depth-intervals on $R$ overlap, and a third back edge
whose path meets one of the two sym-diff intervals in an arc with
slack exactly 5 — pure interval arithmetic per chain, with no lca /
branching geometry. The analytic attack on Q71 then targets: (i) a
chain-selection rule, (ii) an interval-system counting argument for
slack-5 attainment.

**Refinement kill recorded (do NOT revisit).** The leaf-pair-only
form ("some LEAF pair carries a paste-8") is DEAD: deterministically
falsified on `viol3_n40`, `surv_thin_n32`, `surv_kp5_n32` (CHECK 1
pins leaf count 0 on all three) and on 5 of 21 sampled residual trees
(seed 20260815). Same-sender pairs are insufficient; strict-ancestor
sender pairs are the load-bearing extension.

**Evidence.**

- **All 8 pinned residual trees comply** (CHECK 1, deterministic):
  usable-pairing counts over all $L=8$ triples, as
  (leaf, chain, branched): `l8_exactness_dead` (1, 8, 3),
  `sup1_dead_tree` (1, 11, 0), `viol1_n30` (4, 16, 4),
  `viol2_n30` (1, 12, 3), `viol3_n40` (0, 12, 0),
  `surv_thin_n32` (0, 4, 0), `surv_kp5_n32` (0, 8, 0),
  `surv_kp5_n40` (1, 6, 1). Same-branch (leaf+chain) $> 0$ on every
  pin.
- **On the four hardest pins the witnesses are EXCLUSIVELY
  same-branch**: `viol3_n40`, `surv_thin_n32`, `surv_kp5_n32` have
  branched count 0 (and `sup1_dead_tree` too) — under adversarial
  pressure (R40 residuality-SA, R41 anti-availability-SA) the
  surviving paste-8 channel is the same-branch one. Same-branch is
  not a convenience subclass; it is where the hard witnesses live.
- **Fresh census** (seed 20260815+43, $n \in \{12..22\}$, 124,000
  trees, 31 pair-residual): 31/31 have a same-branch paste-8
  (CHECK 2). In the exploratory run (seed 20260815, 21 residuals),
  16/21 witnesses were already on a leaf pair; all 5 leaf-failures
  had chain-pair witnesses.
- **Direct adversarial attack survived (R44, same session)**: two
  independent SA runs whose lexicographic energy penalized
  SAME-BRANCH paste-8 availability itself (residuality violations
  first, then #same-branch paste-8 pairings; cubic 2-opt keeping
  girth $\ge 5$ + DFS re-root/re-order; $n \in [30, 48]$; 70% of
  restarts warm-started from the 8 pinned residual trees), ~1.1M SA
  iterations total, visiting 385k + 351k pair-residual states:
  **zero falsifiers**. Availability bottomed at **4 same-branch
  pairings — and the minimum state found by BOTH runs independently
  is exactly the `surv_thin_n32` pin** (same graph, same tree), whose
  same-branch pairing count 4 is already deterministically pinned in
  CHECK 1. The R41-hardened tree is simultaneously the same-branch
  availability floor: directed pressure could not separate the
  same-branch channel from the generic paste-8 channel.
- **Honest limitations**: cold-start SA reaches pair-residuality
  rarely above $n = 26$, so the R44 walks explored mainly the
  2-opt/re-root neighborhoods of the 8 warm-start pins (plus
  occasional cold finds); $n \in \{44, 48\}$ contributed no cold
  residual states, and coverage above $n = 40$ is thin. The claim
  remains unproven and universally quantified — sampling can only
  falsify.
- **R45: survives on the chain1d falsifier, and the fully-1-D
  strengthening is DEAD.** `paste8_chain1d_universal` (all three
  senders on one chain) was disproved at introduction by
  `chain1d_falsifier_n14` (CHECK 3 below): a pair-residual $n = 14$
  tree with 6 same-branch witnesses — every one with a FOREIGN
  cover (sender incomparable with the pair's deeper sender) — and 0
  fully 1-D ones. Two consequences for THIS lemma: (i) it is now the
  terminal member of the refinement ladder — leaf-only (below) and
  chain1d (above) are both dead, so same-branch is pinched between
  falsified neighbors; (ii) any proof must let the cover enter the
  pair's chain from a sibling branch — the projected-interval
  formulation (Q74), not the senders-on-chain one. NOTE the class
  caveat: the falsifier's graph has girth 3; the R44 anti-same-branch
  hardening ran in the girth $\ge 5$ class only. A wide-class (no
  girth floor) anti-same-branch SA is the R45-designated next
  falsifier for this lemma itself.

<!-- CHECK
# paste8_samebranch_universal CHECK 1 (deterministic pins): on all 8
# pinned pair-residual trees, count usable pairings of L=8 triples by
# pair class -- leaf (equal senders), chain (comparable senders),
# branched (incomparable) -- and assert the exact counts, in particular
# same-branch (leaf+chain) > 0 everywhere and branched == 0 on
# sup1_dead_tree, viol3_n40, surv_thin_n32, surv_kp5_n32.
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

def audit(name, nn, edges, root, par, exp_leaf, exp_chain, exp_br, exp_minkp):
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
    m = len(fc)
    leaf = chain = br = 0; minkp = None
    for x in range(m):
        for y in range(x + 1, m):
            for z in range(y + 1, m):
                if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) != 8: continue
                for (i, j, k) in ((x, y, z), (x, z, y), (y, z, x)):
                    D = fc[i] ^ fc[j]
                    if single_cycle_len(D) is None: continue
                    arc = D & fc[k]
                    if not arc or n_arcs(arc) != 1: continue
                    s1, s2 = be[i][0], be[j][0]
                    if s1 == s2: leaf += 1; vert = True
                    elif is_anc(s1, s2) or is_anc(s2, s1):
                        chain += 1; vert = True
                    else: br += 1; vert = False
                    if vert:
                        kp = len(arc)
                        if minkp is None or kp < minkp: minkp = kp
    assert (leaf, chain, br, minkp) == (exp_leaf, exp_chain, exp_br, exp_minkp), \
        f"{name}: (leaf, chain, branched, min_kp) = " \
        f"({leaf}, {chain}, {br}, {minkp}) != " \
        f"({exp_leaf}, {exp_chain}, {exp_br}, {exp_minkp})"
    assert leaf + chain > 0, f"{name}: NO same-branch paste-8 -- falsified"
    print(f"{name}: leaf={leaf} chain={chain} branched={br} "
          f"samebranch_min_kp={minkp}")

audit("l8_exactness_dead", 12,
      [(4, 10), (1, 2), (5, 11), (0, 10), (5, 8), (3, 7), (6, 8), (2, 10),
       (1, 4), (0, 6), (6, 7), (4, 5), (8, 9), (2, 9), (1, 7), (3, 9),
       (0, 11), (3, 11)],
      10, [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0], 1, 8, 3, 1)
audit("sup1_dead_tree", 14,
      [(5, 13), (0, 2), (10, 12), (1, 3), (7, 10), (6, 8), (4, 8), (3, 6),
       (3, 12), (5, 9), (4, 11), (0, 1), (9, 10), (1, 2), (9, 13), (0, 4),
       (2, 7), (6, 13), (5, 11), (11, 12), (7, 8)],
      11, [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5], 1, 11, 0, 2)
audit("viol1_n30", 30,
      [(0, 18), (0, 22), (0, 27), (1, 9), (1, 18), (1, 29), (2, 4), (2, 5),
       (2, 20), (3, 6), (3, 17), (3, 29), (4, 25), (4, 28), (5, 12), (5, 27),
       (6, 8), (6, 11), (7, 9), (7, 14), (7, 27), (8, 19), (8, 20), (9, 12),
       (10, 15), (10, 16), (10, 24), (11, 15), (11, 23), (12, 13), (13, 23),
       (13, 26), (14, 21), (14, 26), (15, 21), (16, 17), (16, 22), (17, 20),
       (18, 19), (19, 26), (21, 25), (22, 28), (23, 25), (24, 28), (24, 29)],
      20,
      [27, 9, 4, 29, 28, 2, 3, 14, 19, 12, 16, 6, 5, 23, 21, 10, 17, 20, 19,
       26, -1, 15, 0, 11, 29, 23, 13, 7, 22, 1], 4, 16, 4, 3)
audit("viol2_n30", 30,
      [(0, 3), (0, 16), (0, 17), (1, 5), (1, 19), (1, 20), (2, 10), (2, 22),
       (2, 28), (3, 12), (3, 19), (4, 20), (4, 21), (4, 23), (5, 11), (5, 28),
       (6, 11), (6, 24), (6, 26), (7, 11), (7, 27), (7, 29), (8, 18), (8, 23),
       (8, 29), (9, 12), (9, 20), (9, 24), (10, 13), (10, 23), (12, 25),
       (13, 18), (13, 21), (14, 15), (14, 27), (14, 28), (15, 17), (15, 26),
       (16, 21), (16, 25), (17, 22), (18, 24), (19, 26), (22, 29), (25, 27)],
      25,
      [17, 5, 10, 12, 21, 11, 26, 29, 23, 20, 13, 7, 9, 18, 28, 14, 25, 15,
       24, 3, 1, 16, 17, 4, 6, -1, 19, 14, 2, 8], 1, 12, 3, 4)
audit("viol3_n40", 40,
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
       28, 39, 31], 0, 12, 0, 4)
audit("surv_thin_n32", 32,
      [(0, 17), (0, 21), (0, 23), (1, 20), (1, 23), (1, 28), (2, 17), (2, 19),
       (2, 27), (3, 9), (3, 25), (3, 28), (4, 16), (4, 22), (4, 26), (5, 7),
       (5, 8), (5, 26), (6, 10), (6, 11), (6, 12), (7, 15), (7, 24), (8, 25),
       (8, 27), (9, 12), (9, 20), (10, 30), (10, 31), (11, 13), (11, 17),
       (12, 21), (13, 24), (13, 31), (14, 16), (14, 28), (14, 30), (15, 18),
       (15, 25), (16, 18), (18, 20), (19, 23), (19, 24), (21, 29), (22, 27),
       (22, 29), (26, 31), (29, 30)],
      18,
      [17, 28, 27, 9, 22, 7, 11, 15, 5, 20, 31, 13, 6, 24, 16, 25, 18, 2,
       -1, 23, 1, 12, 29, 0, 19, 3, 4, 8, 14, 21, 10, 26], 0, 4, 0, 2)
audit("surv_kp5_n32", 32,
      [(0, 1), (0, 9), (0, 25), (1, 7), (1, 15), (2, 3), (2, 18), (2, 27),
       (3, 24), (3, 29), (4, 5), (4, 15), (4, 16), (5, 26), (5, 31), (6, 16),
       (6, 23), (6, 25), (7, 8), (7, 19), (8, 27), (8, 29), (9, 20), (9, 22),
       (10, 17), (10, 23), (10, 31), (11, 28), (11, 29), (11, 30), (12, 13),
       (12, 15), (12, 19), (13, 18), (13, 26), (14, 22), (14, 23), (14, 30),
       (16, 24), (17, 22), (17, 27), (18, 20), (19, 28), (20, 21), (21, 24),
       (21, 30), (25, 31), (26, 28)],
      7,
      [1, 15, 18, 29, 16, 31, 23, -1, 7, 22, 17, 28, 13, 26, 30, 4, 6, 27,
       20, 12, 9, 24, 14, 10, 3, 0, 5, 2, 19, 8, 21, 25], 0, 8, 0, 5)
audit("surv_kp5_n40", 40,
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
       18, 31, 15], 1, 6, 1, 5)
print("pins OK: every pinned residual tree has a same-branch paste-8; "
      "on sup1_dead_tree/viol3_n40/surv_thin_n32/surv_kp5_n32 the "
      "witnesses are EXCLUSIVELY same-branch (branched = 0)")
CHECK -->

<!-- CHECK
# paste8_samebranch_universal CHECK 2 (falsification probe): every
# sampled pair-residual cubic DFS tree has a paste-8 whose usable
# pairing is a same-branch pair (senders equal or ancestor-comparable).
# Fresh seed (20260815+43); an assert failure prints the tree for
# pinning.  Direct pair-first search with early exit (~15s).
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


def has_samebranch_paste8(nn, be, fc, pe, depth, par):
    m = len(be)
    for i in range(m):
        s1 = be[i][0]
        for j in range(i + 1, m):
            s2 = be[j][0]
            if s1 != s2 and not (is_ancestor(s1, s2, depth, par)
                                 or is_ancestor(s2, s1, depth, par)):
                continue
            D = set(fc[i] ^ fc[j])
            if single_cycle_len(D) is None: continue
            Dlen = len(D)
            for z in range(m):
                if z == i or z == j: continue
                arc = D & pe[z]
                if not arc or n_arcs(arc) != 1: continue
                kp = len(arc)
                if Dlen + len(pe[z]) + 1 - 2 * kp == 8:
                    assert single_cycle_len(set(fc[i] ^ fc[j] ^ fc[z])) == 8
                    return True
    return False


rng = random.Random(20260815 + 43)
trees_seen = 0; residual = 0
for nn, trials in ((12, 4000), (14, 4000), (16, 3000),
                   (18, 2000), (20, 1500), (22, 1000)):
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
            assert has_samebranch_paste8(nn, be, fc, pe, depth, par), \
                (f"FALSIFIED paste8_samebranch_universal: pair-residual "
                 f"tree with no same-branch paste-8 (n={nn}, root={r}, "
                 f"par={par}, edges={edges})")

assert trees_seen > 100000, f"too few trees: {trees_seen}"
assert residual >= 25, f"too few residual trees: {residual} -- probe vacuous"
print(f"trees={trees_seen} residual={residual} -- every pair-residual tree "
      f"has a same-branch paste-8")
CHECK -->

<!-- CHECK
# paste8_samebranch_universal CHECK 3 (deterministic pin,
# chain1d_falsifier_n14, added R45): the tree that DISPROVED the
# fully-1-D strengthening paste8_chain1d_universal.  Assert it is
# pair-residual, has EXACTLY 6 same-branch paste-8 (pair, cover)
# combos -- so this lemma survives on it -- and 0 of them fully 1-D
# (every cover's sender incomparable with the pair's deeper sender).
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

nn = 14; root = 1
par = [4, -1, 1, 11, 8, 13, 13, 2, 7, 10, 12, 4, 3, 9]
edges = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 7), (3, 11), (3, 12),
         (4, 8), (4, 11), (5, 9), (5, 11), (5, 13), (6, 7), (6, 12),
         (6, 13), (7, 8), (8, 10), (9, 10), (9, 13), (10, 12)]
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
def comp(u, v):
    return u == v or is_anc(u, v) or is_anc(v, u)
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
n_sb = n_1d = 0
for i in range(m):
    s1 = be[i][0]
    for j in range(i + 1, m):
        s2 = be[j][0]
        if not comp(s1, s2): continue
        D = set(fc[i] ^ fc[j])
        if single_cycle_len(D) is None: continue
        sd = s1 if depth[s1] >= depth[s2] else s2
        for z in range(m):
            if z == i or z == j: continue
            arc = D & pe[z]
            if not arc or n_arcs(arc) != 1: continue
            if len(D) + len(pe[z]) + 1 - 2 * len(arc) == 8:
                n_sb += 1
                if comp(be[z][0], sd): n_1d += 1
assert (n_sb, n_1d) == (6, 0), f"(samebranch, fully_1d) = ({n_sb}, {n_1d})"
print("chain1d_falsifier_n14 OK: pair-residual, 6 same-branch paste-8 "
      "(this lemma survives), 0 fully 1-D (chain1d disproved)")
CHECK -->

## Summary

The 1-dimensional supply refinement, motivated by the R43 witness-shape
census: every pair-residual normal spanning tree of a cubic graph has a
paste-8 whose usable pairing is a SAME-BRANCH pair (senders equal or
ancestor-comparable), so the branching geometry of the general pasting
machinery is never necessary for 8-supply. On same-branch pairs the
proved vertical calculus makes $D$ = two depth-intervals on one root
chain plus the two back edges, all one-interval meets automatic pastes,
and the 8-line the slack identity "missed $D$-edges + off-$D$ path
edges = 5". Unfalsified on all 8 deterministic pins (where the four
hardest carry ONLY same-branch witnesses) and 31/31 fresh-census
residual trees; the leaf-pair-only strengthening is pinned dead. Not
yet SA-hardened against same-branch availability specifically — that is
the designated next falsifier.
