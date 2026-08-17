---
id: pastePO2_samebranch_universal
status: open
depends_on: [triple_alive_universal, fund_pair_overlap, paste8_projected_coords, pasting_vertex_automatic]
discharged_by_round: null
introduced_at_round: 46
---

# Lemma `pastePO2_samebranch_universal` (conjecture + probe: every pair-residual tree has a same-branch paste at SOME power of 2)

**Setting.** $T$ a pair-residual normal spanning tree of a connected
cubic graph; same-branch pairs, sym-diff intervals $A, I, E$, covers,
arcs, and slack $= |A| + |E| + g_3 - 2k' = L - 3$ as in
`paste8_samebranch_universal` (whose PROVED vertical-calculus parts
1-3 and the PROVED `paste8_projected_coords` are length-agnostic and
carry over verbatim).

**Claim (open, universally quantified -- sampling can only falsify).**
Every pair-residual normal spanning tree of a connected cubic graph
admits a same-branch pair with single-cycle sym-diff $D$ and a third
back edge meeting $D$ in a single arc with
$$\mathrm{slack} \in \{1, 5, 13, 29\} \qquad (L \in \{4, 8, 16, 32\}).$$

By the pasting criterion (`triple_sym_diff_structure`(5)) such a
config exhibits an actual simple cycle of power-of-2 length, so this
claim implies the EGC conclusion on every pair-residual tree -- it is
the SET-VALUED successor of the dead `paste8_samebranch_universal`,
forced by `sb_falsifier_n18` (R46): there the value set holes out at
8 but the tree pastes at 16 through chain pairs (slack 13), so the
correct universal must quantify over the PO2 set, not a single length.

**Why same-branch (still).** On every falsifier and pin known, ALL
PO2 firing triples factor through same-branch pastings
(`sb_falsifier_n18`: 4/4 at $L = 16$; the 8 original pins: paste-8s
with same-branch > 0 everywhere; census R43: hard trees are
exclusively same-branch). The branching geometry has never been
necessary; the projected-coordinate language stays fully 1-D.

**Refinement kills inherited (do NOT revisit).** Single-length forms
are dead: $L = 8$ (`sb_falsifier_n18`), $L = 8$ exact-triple
(`sup8_tree_universal`), any-class $L = 8$
(`paste8_tree_universal`). Structured-slack forms are dead:
full-interval and ladder-above-5 (`ladder_gap3_n16`,
`ladder_gap9_n14`). Fully-1-D covers are dead
(`chain1d_falsifier_n14`). Leaf-only pairs are dead. What this claim
keeps: the same-branch pair class + the PO2 value SET.

**Evidence (R46).**

- All 12 pinned trees comply; the attained subsets of
  $\{1, 5, 13, 29\}$ are asserted exactly in CHECK 1. Notably
  `sb_falsifier_n18` attains ONLY 13 -- the set-valued claim is
  genuinely weaker than any fixed-length claim.
- Every pair-residual tree in the R46 censuses (63 fresh across two
  seeds, $n \le 22$) attains slack 5; the falsifiers show 5 alone is
  not universal but the set is (so far).
- Designated SA falsifier (SAME round, per standing policy): wide
  class, energy = (residuality violations, then #same-branch configs
  with slack in $\{1, 5, 13, 29\}$), cubic 2-opt + re-root, warm
  restarts from all 12 pins, 2 seeds x ~6.7 min -- see the round
  narrative (Section 86 addendum 2) for the outcome.

<!-- CHECK
# pastePO2_samebranch_universal CHECK 1 (deterministic, 12 pins): the
# attained subset of {1, 5, 13, 29} among same-branch pasting slacks,
# asserted exactly.  Non-empty on every pin (the claim); on
# sb_falsifier_n18 it is {13} alone (single-length forms dead).
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

def sb_slacks(nn, edges, root, par):
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
    PO2 = {4, 8, 16, 32}
    assert all(len(c) not in PO2 for c in fc), "fund cycle fires"
    for i in range(m):
        for j in range(i + 1, m):
            assert single_cycle_len(set(fc[i] ^ fc[j])) not in PO2, "pair fires"
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
    return sl

PINS = [
    ('l8_exactness_dead', 12, [(4, 10), (1, 2), (5, 11), (0, 10), (5, 8), (3, 7), (6, 8), (2, 10), (1, 4), (0, 6), (6, 7), (4, 5), (8, 9), (2, 9), (1, 7), (3, 9), (0, 11), (3, 11)],
     10, [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0],
     [1, 5]),
    ('sup1_dead_tree', 14, [(5, 13), (0, 2), (10, 12), (1, 3), (7, 10), (6, 8), (4, 8), (3, 6), (3, 12), (5, 9), (4, 11), (0, 1), (9, 10), (1, 2), (9, 13), (0, 4), (2, 7), (6, 13), (5, 11), (11, 12), (7, 8)],
     11, [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5],
     [5]),
    ('viol1_n30', 30, [(0, 18), (0, 22), (0, 27), (1, 9), (1, 18), (1, 29), (2, 4), (2, 5), (2, 20), (3, 6), (3, 17), (3, 29), (4, 25), (4, 28), (5, 12), (5, 27), (6, 8), (6, 11), (7, 9), (7, 14), (7, 27), (8, 19), (8, 20), (9, 12), (10, 15), (10, 16), (10, 24), (11, 15), (11, 23), (12, 13), (13, 23), (13, 26), (14, 21), (14, 26), (15, 21), (16, 17), (16, 22), (17, 20), (18, 19), (19, 26), (21, 25), (22, 28), (23, 25), (24, 28), (24, 29)],
     20, [27, 9, 4, 29, 28, 2, 3, 14, 19, 12, 16, 6, 5, 23, 21, 10, 17, 20, 19, 26, -1, 15, 0, 11, 29, 23, 13, 7, 22, 1],
     [5, 13]),
    ('viol2_n30', 30, [(0, 3), (0, 16), (0, 17), (1, 5), (1, 19), (1, 20), (2, 10), (2, 22), (2, 28), (3, 12), (3, 19), (4, 20), (4, 21), (4, 23), (5, 11), (5, 28), (6, 11), (6, 24), (6, 26), (7, 11), (7, 27), (7, 29), (8, 18), (8, 23), (8, 29), (9, 12), (9, 20), (9, 24), (10, 13), (10, 23), (12, 25), (13, 18), (13, 21), (14, 15), (14, 27), (14, 28), (15, 17), (15, 26), (16, 21), (16, 25), (17, 22), (18, 24), (19, 26), (22, 29), (25, 27)],
     25, [17, 5, 10, 12, 21, 11, 26, 29, 23, 20, 13, 7, 9, 18, 28, 14, 25, 15, 24, 3, 1, 16, 17, 4, 6, -1, 19, 14, 2, 8],
     [5, 13]),
    ('viol3_n40', 40, [(0, 7), (0, 36), (0, 38), (1, 16), (1, 24), (1, 35), (2, 16), (2, 33), (2, 34), (3, 5), (3, 12), (3, 20), (4, 13), (4, 29), (4, 34), (5, 18), (5, 21), (6, 19), (6, 21), (6, 32), (7, 14), (7, 33), (8, 18), (8, 22), (8, 26), (9, 17), (9, 21), (9, 28), (10, 14), (10, 15), (10, 36), (11, 18), (11, 28), (11, 29), (12, 24), (12, 34), (13, 22), (13, 25), (14, 23), (15, 19), (15, 35), (16, 23), (17, 26), (17, 35), (19, 20), (20, 37), (22, 36), (23, 38), (24, 33), (25, 27), (25, 39), (26, 32), (27, 30), (27, 32), (28, 37), (29, 31), (30, 31), (30, 37), (31, 39), (38, 39)],
     1, [36, -1, 33, 5, 34, 21, 19, 0, 18, 17, 14, 29, 24, 4, 23, 10, 2, 35, 11, 20, 3, 9, 13, 16, 1, 39, 8, 32, 11, 31, 27, 30, 6, 7, 12, 15, 22, 28, 39, 31],
     [5, 13, 29]),
    ('surv_thin_n32', 32, [(0, 17), (0, 21), (0, 23), (1, 20), (1, 23), (1, 28), (2, 17), (2, 19), (2, 27), (3, 9), (3, 25), (3, 28), (4, 16), (4, 22), (4, 26), (5, 7), (5, 8), (5, 26), (6, 10), (6, 11), (6, 12), (7, 15), (7, 24), (8, 25), (8, 27), (9, 12), (9, 20), (10, 30), (10, 31), (11, 13), (11, 17), (12, 21), (13, 24), (13, 31), (14, 16), (14, 28), (14, 30), (15, 18), (15, 25), (16, 18), (18, 20), (19, 23), (19, 24), (21, 29), (22, 27), (22, 29), (26, 31), (29, 30)],
     18, [17, 28, 27, 9, 22, 7, 11, 15, 5, 20, 31, 13, 6, 24, 16, 25, 18, 2, -1, 23, 1, 12, 29, 0, 19, 3, 4, 8, 14, 21, 10, 26],
     [5, 13]),
    ('surv_kp5_n32', 32, [(0, 1), (0, 9), (0, 25), (1, 7), (1, 15), (2, 3), (2, 18), (2, 27), (3, 24), (3, 29), (4, 5), (4, 15), (4, 16), (5, 26), (5, 31), (6, 16), (6, 23), (6, 25), (7, 8), (7, 19), (8, 27), (8, 29), (9, 20), (9, 22), (10, 17), (10, 23), (10, 31), (11, 28), (11, 29), (11, 30), (12, 13), (12, 15), (12, 19), (13, 18), (13, 26), (14, 22), (14, 23), (14, 30), (16, 24), (17, 22), (17, 27), (18, 20), (19, 28), (20, 21), (21, 24), (21, 30), (25, 31), (26, 28)],
     7, [1, 15, 18, 29, 16, 31, 23, -1, 7, 22, 17, 28, 13, 26, 30, 4, 6, 27, 20, 12, 9, 24, 14, 10, 3, 0, 5, 2, 19, 8, 21, 25],
     [5, 13]),
    ('surv_kp5_n40', 40, [(0, 10), (0, 31), (0, 32), (1, 20), (1, 22), (1, 36), (2, 7), (2, 17), (2, 33), (3, 22), (3, 34), (3, 35), (4, 25), (4, 27), (4, 29), (5, 18), (5, 27), (5, 33), (6, 26), (6, 33), (6, 38), (7, 13), (7, 16), (8, 25), (8, 26), (8, 39), (9, 32), (9, 34), (9, 36), (10, 15), (10, 16), (11, 19), (11, 31), (11, 35), (12, 23), (12, 32), (12, 37), (13, 29), (13, 30), (14, 16), (14, 19), (14, 30), (15, 23), (15, 39), (17, 24), (17, 28), (18, 21), (18, 37), (19, 20), (20, 34), (21, 24), (21, 25), (22, 30), (23, 24), (26, 35), (27, 38), (28, 36), (28, 37), (29, 39), (31, 38)],
     31, [32, 20, 33, 22, 25, 27, 38, 16, 39, 36, 0, 35, 37, 7, 19, 23, 14, 2, 5, 11, 34, 24, 30, 12, 17, 21, 8, 4, 36, 13, 13, -1, 9, 6, 3, 26, 1, 18, 31, 15],
     [5, 13, 29]),
    ('chain1d_falsifier_n14', 14, [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 7), (3, 11), (3, 12), (4, 8), (4, 11), (5, 9), (5, 11), (5, 13), (6, 7), (6, 12), (6, 13), (7, 8), (8, 10), (9, 10), (9, 13), (10, 12)],
     1, [4, -1, 1, 11, 8, 13, 13, 2, 7, 10, 12, 4, 3, 9],
     [5]),
    ('ladder_gap3_n16', 16, [(6, 15), (3, 4), (4, 12), (5, 13), (0, 5), (8, 12), (1, 6), (8, 15), (2, 11), (1, 15), (7, 10), (6, 14), (3, 9), (4, 11), (0, 7), (10, 11), (2, 13), (3, 5), (12, 14), (0, 9), (8, 10), (2, 9), (1, 13), (7, 14)],
     5, [7, 6, 13, 9, 3, -1, 15, 10, 12, 2, 11, 4, 14, 5, 7, 8],
     [1, 5]),
    ('ladder_gap9_n14', 14, [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 7), (3, 11), (3, 12), (4, 8), (4, 11), (5, 9), (5, 11), (5, 13), (6, 8), (6, 12), (6, 13), (7, 8), (7, 10), (9, 10), (9, 13), (10, 12)],
     0, [-1, 0, 1, 12, 8, 11, 13, 2, 6, 13, 7, 3, 10, 5],
     [5]),
    ('sb_falsifier_n18', 18, [(0, 8), (0, 16), (0, 17), (1, 2), (1, 5), (1, 7), (2, 15), (2, 17), (3, 5), (3, 10), (3, 12), (4, 6), (4, 12), (4, 14), (5, 7), (6, 14), (6, 16), (7, 8), (8, 15), (9, 11), (9, 12), (9, 13), (10, 13), (10, 15), (11, 13), (11, 14), (16, 17)],
     8, [17, 7, 1, 12, 6, 3, 16, 5, -1, 11, 15, 13, 9, 10, 4, 8, 0, 2],
     [13]),
]

for name, nn, edges, root, par, expect in PINS:
    got = sorted(sb_slacks(nn, edges, root, par) & {1, 5, 13, 29})
    assert got == expect, f"{name}: PO2-slack subset {got} != {expect}"
    assert got, f"{name}: NO same-branch PO2 paste -- falsified"
print("pins OK: every pinned pair-residual tree has a same-branch "
      "pasting config with slack in {1, 5, 13, 29}; sb_falsifier_n18 "
      "attains only 13")
CHECK -->

## Summary

The set-valued successor of the dead single-length paste universals:
every pair-residual normal spanning tree of a connected cubic graph
has a same-branch pasting config whose slack lies in
$\{1, 5, 13, 29\}$ (equivalently, a power-of-2 cycle obtained by
pasting a cover onto a comparable-sender pair). Implies the EGC
conclusion on pair-residual trees; refines `triple_alive_universal`
along the mechanism that every known witness and falsifier actually
uses. Unfalsified on all 12 pins (including every falsifier that
killed its predecessors) and all census residuals; the R46-designated
wide-class SA falsifier ran the same round it was introduced.
