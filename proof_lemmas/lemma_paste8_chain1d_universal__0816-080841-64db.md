---
id: paste8_chain1d_universal
status: disproved
depends_on: [paste8_samebranch_universal, paste8_tree_universal, shortpaste_floor_line, fund_pair_overlap]
discharged_by_round: 45
introduced_at_round: 45
---

# Lemma `paste8_chain1d_universal` (DISPROVED at introduction: the fully 1-D refinement fails at n = 14 — the cover MUST sometimes come from a foreign branch)

**DISPROVED (same round, R45).** The census below found the class
universal in-sample (8/8 pins, 25/25 fresh residuals, CHECKs 1–2
pass), but the designated falsifier — anti-chain1d SA (lexicographic
energy: residuality violations, then #fully-1-D paste-8 pairings),
run per the standing dual-attack policy BEFORE any analytic effort —
killed the claim in under 20 seconds of SA time, at $n = 14$:

- **Falsifier `chain1d_falsifier_n14`** (pinned in
  `paste8_samebranch_universal` CHECK 3, which now guards the
  surviving fallback): $n = 14$, root $= 1$,
  `par = [4,-1,1,11,8,13,13,2,7,10,12,4,3,9]`, edges
  `[(0,1),(0,2),(0,4),(1,2),(1,3),(2,7),(3,11),(3,12),(4,8),(4,11),
  (5,9),(5,11),(5,13),(6,7),(6,12),(6,13),(7,8),(8,10),(9,10),
  (9,13),(10,12)]` — cubic, connected, 8 back edges, pair-residual
  (0 violations), **6 same-branch paste-8 witnesses, 0 fully 1-D**:
  in every witness the cover's sender is on a branch incomparable
  with the pair's deeper sender. Independently re-verified with the
  census enumerator (triple-first) and the pair-first searcher.
- The falsifier's graph has girth 3 (triangle 0-1-2) — it surfaced
  because the R45 SA harness's local girth check was (accidentally)
  leaky, so the walk explored the FULL cubic class rather than the
  girth $\ge 5$ subclass the R40–R44 harnesses used. The tree-level
  universals quantify over ALL connected cubic graphs (the existing
  pins already contain 4-cycles), so the falsifier is legitimate;
  but note the class discrepancy: no girth $\ge 5$ chain1d falsifier
  is known yet, and the R44 anti-same-branch hardening was run only
  in the girth $\ge 5$ class (see the samebranch lemma's R45
  wide-class evidence bullet).
- **Witness anatomy on the falsifier** (all 6): leaves are
  $\{0 (d5), 5 (d11), 6 (d11)\}$; every cover is a FOREIGN back edge
  whose tree path climbs into the pair's chain from a sibling branch
  and meets $A$ or $E$ in its upper (on-chain) segment. Observed
  slack splits: $(0,5) \times 2$, $(3,2) \times 4$; arcs in $A$
  (4 witnesses) and $E$ (2).

**Go-forward reframing (this is the analytic content that survives).**
The pair side of the 1-D formulation stands — the pair lives on one
chain with $A, I, E$ consecutive depth intervals. The cover side must
use the PROJECTED interval system: for ANY back edge $B_3 = (s_3,
a_3)$ whose tree path meets the chain $R$, the on-chain part of $P_3$
is the depth interval $[d(a_3), d(x_3)]$ where $x_3$ is the deepest
common ancestor of $s_3$ with (the relevant leaf of) $R$; its
off-chain part contributes $g_3 - (\text{on-chain length})$ to the
slack but never to the arc. The supply question for
`paste8_samebranch_universal` is therefore STILL per-chain interval
arithmetic — but over the richer projected family, and
`chain1d_falsifier_n14` proves the enrichment is sometimes strictly
necessary. Q74 carries this forward.

## Original conjecture text (retained as audit trail; the CHECK blocks below are skipped at runtime now that status is disproved)

**Setting.** $T$ a pair-residual normal spanning tree of a connected
cubic graph, as in `paste8_tree_universal` /
`paste8_samebranch_universal`. Call a paste-8 firing triple
$(B_1, B_2; B_3)$ (usable pairing $\{B_1, B_2\}$, cover $B_3$)
**fully 1-D** if the three senders $s_1, s_2, s_3$ are pairwise
comparable in tree order — equivalently, all three back edges have
their senders (hence also their anchors, which are ancestors of the
senders) on ONE root chain $R$. Since $s_1, s_2$ comparable is the
same-branch condition and ancestors of a vertex form a chain, the
triple is fully 1-D iff $s_3$ is comparable with the deeper of
$s_1, s_2$.

**Fully-1-D calculus (immediate from the proved same-branch vertical
calculus).** Fix the chain $R$ and write each back edge as the depth
interval $J_i = [d(a_i), d(s_i)]$ on $R$ ($g_i = |J_i|$ edges). For a
same-branch pair, $D$'s tree part is $A \sqcup E$ with the cancelled
overlap $I$ between them, $A \cup I \cup E$ a single interval
(consecutive: $A$, then $I$, then $E$ by depth). A fully 1-D cover is
a THIRD interval $J_3$ on the same line, so:

1. the paste condition ($D \cap C_3$ a single arc) is exactly "$J_3$
   meets $A \sqcup E$ in edges but does not bridge across $I$" — an
   interval that straddles $I$ with edges on both sides meets $D$ in
   two arcs (the straddle branch of `pasting_cover_dichotomy`);
2. $k' = |J_3 \cap A|$ or $|J_3 \cap E|$ — plain 1-D interval
   intersection lengths;
3. the 8-line is the slack identity
   $(|A| + |E| - k') + (g_3 - k') = 5$.

A fully 1-D witness is therefore SIX integers — the endpoint depths
of three intervals on one line — subject to pure interval arithmetic:
the entire branching geometry of the tree drops out. The analytic
supply question becomes: *does the depth-interval system of some root
chain of every pair-residual tree contain two overlapping intervals
plus a third meeting exactly one sym-diff part with slack exactly 5?*

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual normal spanning tree of a connected cubic graph
has a paste-channel $L = 8$ firing triple that is fully 1-D.

**Relation to the ladder.** Strictly stronger than
`paste8_samebranch_universal` (which constrains only $s_1, s_2$),
strictly weaker than the dead bounded-$k'$ / leaf-pair-only forms. It
does NOT bound $k'$ (the cover interval can meet almost all of $A
\sqcup E$), so it is compatible with the proved unbounded-$k'$ burden
(R40/R41).

**Evidence (R45 census, session s_0816-080841-64db).**

- **All 8 pinned residual trees comply** (CHECK 1, deterministic):
  (fully-1-D, all same-branch) paste-8 pairing counts:
  `l8_exactness_dead` (6, 9), `sup1_dead_tree` (12, 12),
  `viol1_n30` (16, 20), `viol2_n30` (10, 13), `viol3_n40` (12, 12),
  `surv_thin_n32` (4, 4), `surv_kp5_n32` (8, 8),
  `surv_kp5_n40` (6, 7). Fully-1-D $> 0$ on every pin.
- **On the four hardest pins the same-branch witnesses are 100%
  fully 1-D**: `sup1_dead_tree` 12/12, `viol3_n40` 12/12,
  `surv_thin_n32` 4/4, `surv_kp5_n32` 8/8 — the same
  "hard pins live exclusively in the refined class" signature that
  picked out the same-branch class in R43. In particular the R44
  availability-floor tree `surv_thin_n32` carries ONLY fully 1-D
  witnesses.
- **Fresh census** (seed 20260816+45, 84,000 trees, 25
  pair-residual): 25/25 have a fully 1-D paste-8; on 13/25 ALL
  same-branch witnesses are fully 1-D. (The committed CHECK 2 replays
  a trial-count-reduced PREFIX of the same per-size-class streams:
  68,800 trees, 23 residuals, 23/23 — the per-class sub-seeds are
  identical, so its residuals are a subset of the census's.) Same stream also confirmed:
  every chain-selection rule tested (deepest-leaf chain, max-sender
  chain, max-overlapping-pairs chain) locates a same-branch witness
  on 25/25 — the witness chain is not scarce.
- **Chain ubiquity on the pins**: on all 8 pins EVERY root chain
  (i.e. every leaf's root path) carries a same-branch witness
  (pins have 1–4 leaves; the fresh census did not tabulate the
  every-chain property, only the three selection rules).
- **Honest limitations**: not yet SA-hardened against fully-1-D
  availability specifically (the R44 runs penalized same-branch
  availability; anti-chain1d energy is the designated next
  falsifier). Census sizes $n \le 22$ plus pins $n \le 40$; the
  claim remains unproven and universally quantified.

**Refinement-death watch.** Two prior refinements of this strength
died under adversarial pressure (`paste8_k2_universal` at R40,
leaf-pair-only at R43) while two survived it (`paste8_tree_universal`
R41, `paste8_samebranch_universal` R44). Spend NO analytic effort on
the fully-1-D form before an anti-chain1d SA run; the fallback target
remains `paste8_samebranch_universal`, whose witnesses only need the
PAIR on one chain.

<!-- CHECK
# paste8_chain1d_universal CHECK 1 (deterministic pins): on all 8
# pinned pair-residual trees, over all L=8 triples (triple sym-diff a
# single 8-cycle) and usable pairings (D single cycle, cover meets D
# in one arc), count (fully_1d, samebranch) -- fully_1d = the three
# senders pairwise comparable; samebranch = the pair's two senders
# comparable.  Assert exact counts; fully_1d > 0 on every pin; on
# sup1_dead_tree / viol3_n40 / surv_thin_n32 / surv_kp5_n32 ALL
# same-branch witnesses are fully 1-D.
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

def audit(name, nn, edges, root, par, exp_1d, exp_sb):
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
        if e in tre: continue
        u, v = e
        a, b = (u, v) if depth[u] <= depth[v] else (v, u)
        assert is_anc(a, b), "non-ancestral non-tree edge"
        be.append((b, a))
    fc = [fcyc(s, a) for s, a in be]
    m = len(fc)
    n_1d = n_sb = 0
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
                    if not comp(s1, s2): continue
                    n_sb += 1
                    sd = s1 if depth[s1] >= depth[s2] else s2
                    if comp(be[k][0], sd): n_1d += 1
    assert (n_1d, n_sb) == (exp_1d, exp_sb), \
        f"{name}: (fully_1d, samebranch) = ({n_1d}, {n_sb}) != " \
        f"({exp_1d}, {exp_sb})"
    assert n_1d > 0, f"{name}: NO fully 1-D paste-8 -- falsified"
    print(f"{name}: fully_1d={n_1d} samebranch={n_sb}")

audit("l8_exactness_dead", 12,
      [(4, 10), (1, 2), (5, 11), (0, 10), (5, 8), (3, 7), (6, 8), (2, 10),
       (1, 4), (0, 6), (6, 7), (4, 5), (8, 9), (2, 9), (1, 7), (3, 9),
       (0, 11), (3, 11)],
      10, [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0], 6, 9)
audit("sup1_dead_tree", 14,
      [(5, 13), (0, 2), (10, 12), (1, 3), (7, 10), (6, 8), (4, 8), (3, 6),
       (3, 12), (5, 9), (4, 11), (0, 1), (9, 10), (1, 2), (9, 13), (0, 4),
       (2, 7), (6, 13), (5, 11), (11, 12), (7, 8)],
      11, [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5], 12, 12)
audit("viol1_n30", 30,
      [(0, 18), (0, 22), (0, 27), (1, 9), (1, 18), (1, 29), (2, 4), (2, 5),
       (2, 20), (3, 6), (3, 17), (3, 29), (4, 25), (4, 28), (5, 12), (5, 27),
       (6, 8), (6, 11), (7, 9), (7, 14), (7, 27), (8, 19), (8, 20), (9, 12),
       (10, 15), (10, 16), (10, 24), (11, 15), (11, 23), (12, 13), (13, 23),
       (13, 26), (14, 21), (14, 26), (15, 21), (16, 17), (16, 22), (17, 20),
       (18, 19), (19, 26), (21, 25), (22, 28), (23, 25), (24, 28), (24, 29)],
      20,
      [27, 9, 4, 29, 28, 2, 3, 14, 19, 12, 16, 6, 5, 23, 21, 10, 17, 20, 19,
       26, -1, 15, 0, 11, 29, 23, 13, 7, 22, 1], 16, 20)
audit("viol2_n30", 30,
      [(0, 3), (0, 16), (0, 17), (1, 5), (1, 19), (1, 20), (2, 10), (2, 22),
       (2, 28), (3, 12), (3, 19), (4, 20), (4, 21), (4, 23), (5, 11), (5, 28),
       (6, 11), (6, 24), (6, 26), (7, 11), (7, 27), (7, 29), (8, 18), (8, 23),
       (8, 29), (9, 12), (9, 20), (9, 24), (10, 13), (10, 23), (12, 25),
       (13, 18), (13, 21), (14, 15), (14, 27), (14, 28), (15, 17), (15, 26),
       (16, 21), (16, 25), (17, 22), (18, 24), (19, 26), (22, 29), (25, 27)],
      25,
      [17, 5, 10, 12, 21, 11, 26, 29, 23, 20, 13, 7, 9, 18, 28, 14, 25, 15,
       24, 3, 1, 16, 17, 4, 6, -1, 19, 14, 2, 8], 10, 13)
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
       28, 39, 31], 12, 12)
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
       -1, 23, 1, 12, 29, 0, 19, 3, 4, 8, 14, 21, 10, 26], 4, 4)
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
       20, 12, 9, 24, 14, 10, 3, 0, 5, 2, 19, 8, 21, 25], 8, 8)
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
       18, 31, 15], 6, 7)
print("pins OK: every pinned residual tree has a fully 1-D paste-8; on "
      "the 4 hardest pins ALL same-branch witnesses are fully 1-D")
CHECK -->

<!-- CHECK
# paste8_chain1d_universal CHECK 2 (falsification probe): every sampled
# pair-residual cubic DFS tree has a paste-8 whose THREE senders are
# pairwise comparable (fully 1-D).  Fresh seed (20260816+45); an assert
# failure prints the tree for pinning.  Direct pair-first search with
# early exit.
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


def has_chain1d_paste8(nn, be, fc, pe, depth, par):
    m = len(be)
    def comp(u, v):
        return (u == v or is_ancestor(u, v, depth, par)
                or is_ancestor(v, u, depth, par))
    for i in range(m):
        s1 = be[i][0]
        for j in range(i + 1, m):
            s2 = be[j][0]
            if not comp(s1, s2): continue
            D = set(fc[i] ^ fc[j])
            if single_cycle_len(D) is None: continue
            Dlen = len(D)
            sd = s1 if depth[s1] >= depth[s2] else s2
            for z in range(m):
                if z == i or z == j: continue
                if not comp(be[z][0], sd): continue
                arc = D & pe[z]
                if not arc or n_arcs(arc) != 1: continue
                kp = len(arc)
                if Dlen + len(pe[z]) + 1 - 2 * kp == 8:
                    assert single_cycle_len(set(fc[i] ^ fc[j] ^ fc[z])) == 8
                    return True
    return False


rng = random.Random(20260816 + 45)
trees_seen = 0; residual = 0
for nn, trials in ((12, 2500), (14, 2500), (16, 1600),
                   (18, 1000), (20, 600), (22, 400)):
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
            assert has_chain1d_paste8(nn, be, fc, pe, depth, par), \
                (f"FALSIFIED paste8_chain1d_universal: pair-residual "
                 f"tree with no fully 1-D paste-8 (n={nn}, root={r}, "
                 f"par={par}, edges={edges})")

assert trees_seen > 50000, f"too few trees: {trees_seen}"
assert residual >= 12, f"too few residual trees: {residual} -- probe vacuous"
print(f"trees={trees_seen} residual={residual} -- every pair-residual tree "
      f"has a fully 1-D paste-8")
CHECK -->

## Summary

DISPROVED at introduction (R45): the fully 1-D refinement — every
pair-residual tree has a paste-8 with all three senders on one root
chain — is universal in-sample (8/8 pins with the 4 hardest carrying
ONLY fully 1-D witnesses, 25/25 fresh residuals; CHECKs 1–2 passed)
but false: `chain1d_falsifier_n14` is pair-residual with 6
same-branch witnesses, all of whose covers come from a foreign
branch, and 0 fully 1-D ones. The designated falsifier was run
BEFORE analytic effort, per the standing dual-attack policy, and
killed the claim in seconds. What survives: the pair side of the 1-D
formulation, with the cover drawn from the PROJECTED interval system
of the chain — carried forward as Q74 under
`paste8_samebranch_universal` (fallback target, unharmed: 6
witnesses on the falsifier).
