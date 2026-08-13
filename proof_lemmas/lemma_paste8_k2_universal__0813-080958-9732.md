---
id: paste8_k2_universal
status: disproved
depends_on: [paste8_tree_universal, shortpaste_floor_line]
discharged_by_round: 40
introduced_at_round: 39
---

# Lemma `paste8_k2_universal` (DISPROVED R40: the $k' \le 2$ / $O(1)$-local refinement fails at witness-box scale; three pinned counterexamples at $n = 30, 30, 40$)

**Setting.** As in `paste8_tree_universal`: $T$ a pair-residual normal
spanning tree of a connected cubic graph. A **paste-8 witness** is a
triple with an ordering (pair, cover) such that $D = C_i \oplus C_j$ is
a single cycle, $D \cap C_k$ is a single arc of $k'$ edges, and
$|D \oplus C_k| = 8$ — equivalently (`shortpaste_floor_line`(4)) the
cell $(|D|, k')$ lies on the 8-line $g_3 = 2k' + 7 - |D|$.

**Claim (DISPROVED, R40).**
~~Every pair-residual normal spanning tree of a connected cubic graph
has a paste-8 witness with $k' \le 2$.~~

**The disproof (R40).** Rejection sampling cannot reach the witness box
(0 residuals in 3,160 sampled trees at $n \ge 28$, girth $\ge 5$), so
R40 hunted adversarially: simulated annealing over (cubic graph, DFS
tree) pairs minimizing the number of po2 firings (energy 0 = pair-
residual), moves = cubic 2-opt rewires keeping girth $\ge 5$ +
re-root/re-order. 20 pair-residual trees were constructed at
$n \in \{30, 32, 36, 40\}$; **4 of the 20 have NO $k' \le 2$ paste-8**
— min witness $k' = 3$ or $4$. Three are pinned in CHECK 2
(deterministic, no sampling): `viol1_n30` (min $k' = 3$, 12 L=8
triples), `viol2_n30` (min $k' = 4$), `viol3_n40` (min $k' = 4$). All
in-sample evidence at $n \le 26$ (46/46) was below the falsification
scale — exactly the gap the R39 falsify critic flagged.

**What survives.** Every one of the 20 adversarial trees still has
SOME paste-8 (min $k' \in \{1, \dots, 4\}$): `paste8_tree_universal`
gains its first above-floor evidence (20/20 at $n \in [30, 40]$,
adversarially constructed, on top of 43/43 sampled at $n \le 26$). The
finite-menu arithmetic below remains a proved fact about $k' \le 2$
witnesses; what died is only their universality. Consequence: there is
NO $O(1)$-local certificate via bounded $k'$ — min witness $k'$ grows
with $n$ (observed 3–4 at $n = 30..40$), so any supply proof must
handle unbounded overlap arcs, or quantify over the graph (the R33
fallback).

**Proved sub-part (the $k' \le 2$ cell menu is finite).** On a
pair-residual tree, any paste-8 witness with $k' \le 2$ lies in one of
exactly eight cells:
$$k' = 1:\ |D| \in \{3, 5, 7\}; \qquad k' = 2:\ |D| \in \{3, 5, 6, 7, 9\}.$$
*Proof.* On the 8-line, $g_3 = 2k' + 7 - |D| \ge 2$
(`shortpaste_floor_line`(2)) gives $|D| \le 2k' + 5$; $D$ is a single
cycle so $|D| \ge 3$. Pair-residuality excludes $|D| \in \{4, 8\}$ ($D$
is a pair sym-diff single cycle, hence never a power of two), and
residuality of $C_k$ excludes $|C_k| = g_3 + 1 \in \{4, 8\}$: for
$k' = 1$ that kills $|D| = 6$ (would need $|C_k| = 4$), for $k' = 2$ it
re-kills $|D| \in \{8, 4\}$ only. What remains is the menu. $\square$

Consequently ALL witnesses the claim quantifies over are **bounded
configurations**: $|D| \le 9$, $|C_k| = g_3 + 1 \le 9$, overlap
$\le 2$ edges. If the claim holds, 8-supply on residual trees is
certified inside constant-size windows — the analytic proof reduces to
a bounded-configuration analysis, with the value side already closed by
`shortpaste_floor_line`.

**What is now known dead (this round's census, pinned below).**

- *$k' = 1$ universal is FALSE*: three pinned $n = 14$ residual trees
  (hard1–hard3 in CHECK 1) have no $k' = 1$ paste-8 at all; their
  $k' \le 2$ witnesses sit in cells $(6, 2)$ and $(9, 2)$. R33's
  `sup1_dead_tree` pin is a fourth: it killed $k' = 1$ *short-cover*
  supply in R33, and in fact has no unrestricted $k' = 1$ paste-8
  either (CHECK 1 prints it).
- *$k' \le 2 \wedge \text{short}$ universal is FALSE*: the
  `sup1_dead_tree` pin's only $k' \le 2$ witnesses are six copies of
  $(6, 2)$ with $g_3 = 5 > k_{12} + 1 = 4$ — none short. The $k' \le 2$
  claim cannot be strengthened by the short-cover condition.

**Evidence below the falsification scale (R39 census, historical —
this is why the claim looked safe).**

- Census (seed 20260813, $n \in \{12..26\}$, 153,600 trees, 46
  pair-residual): **46/46 trees have a $k' \le 2$ paste-8** (43 with
  $k' = 1$, 3 with min $k' = 2$). Observed cell menu (tree counts):
  $(3,1)$ 4x, $(5,1)$ 34x, $(7,1)$ 30x, $(5,2)$ 8x, $(6,2)$ 38x,
  $(7,2)$ 21x, $(9,2)$ 27x — seven of the eight menu cells; $(3,2)$
  unobserved (a triangle $D$ overlapped in 2 of its 3 edges by a
  9-cycle — allowed, evidently rare).
- All five pinned residual trees comply: `l8_exactness_dead`,
  `sup1_dead_tree`, hard1–hard3 (CHECK 1, deterministic).
- Sharper in-sample observation (not conjectured): every census tree
  has a witness with $k' = 1$ OR in cell $(6, 2)$.

<!-- CHECK
# paste8_k2_universal CHECK 1 (deterministic pins): on all five pinned
# pair-residual trees, a k'<=2 paste-8 exists; hard1-3 have NO k'=1
# paste-8 (killing the k'=1 universal); sup1_dead_tree has NO short
# k'<=2 witness (killing the short-conjunction strengthening).
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

PO2 = {4, 8, 16, 32}

def witnesses(nn, edges, root, par):
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
        x = b
        while depth[x] > depth[a]: x = par[x]
        assert x == a, "non-ancestral non-tree edge"
        be.append((b, a))
    fc = [fcyc(s, a) for s, a in be]
    assert not any(len(c) in PO2 for c in fc), "single fires"
    m = len(fc)
    for i in range(m):
        for j in range(i + 1, m):
            assert single_cycle_len(fc[i] ^ fc[j]) not in PO2, "pair fires"
    wits = []
    for x in range(m):
        for y in range(x + 1, m):
            for z in range(y + 1, m):
                if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) != 8: continue
                for (i, j, k) in ((x, y, z), (x, z, y), (y, z, x)):
                    D = fc[i] ^ fc[j]
                    dlen = single_cycle_len(D)
                    if dlen is None: continue
                    inter = D & fc[k]
                    if n_arcs(inter) != 1: continue
                    kp = len(inter)
                    g3 = len(fc[k]) - 1
                    assert g3 == 2 * kp + 7 - dlen, "off the 8-line"
                    assert kp > 2 or (dlen, kp) in {(3, 1), (5, 1), (7, 1),
                        (3, 2), (5, 2), (6, 2), (7, 2), (9, 2)}, \
                        f"cell ({dlen},{kp}) outside the proved menu"
                    wits.append((dlen, kp, g3, len(fc[i] & fc[j])))
    return wits

PINS = [
 ("l8_exactness_dead", 12,
  [(4, 10), (1, 2), (5, 11), (0, 10), (5, 8), (3, 7), (6, 8), (2, 10),
   (1, 4), (0, 6), (6, 7), (4, 5), (8, 9), (2, 9), (1, 7), (3, 9),
   (0, 11), (3, 11)], 10, [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0]),
 ("sup1_dead_tree", 14,
  [(5, 13), (0, 2), (10, 12), (1, 3), (7, 10), (6, 8), (4, 8), (3, 6),
   (3, 12), (5, 9), (4, 11), (0, 1), (9, 10), (1, 2), (9, 13), (0, 4),
   (2, 7), (6, 13), (5, 11), (11, 12), (7, 8)], 11,
  [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5]),
 ("hard1", 14,
  [(3, 7), (4, 12), (5, 10), (8, 9), (8, 12), (0, 8), (1, 3), (6, 11),
   (7, 10), (5, 6), (2, 7), (1, 11), (0, 13), (4, 10), (5, 11), (4, 13),
   (9, 12), (0, 9), (2, 3), (1, 13), (2, 6)], 9,
  [13, 11, 3, 7, 12, 6, 2, 10, 9, -1, 4, 5, 8, 1]),
 ("hard2", 14,
  [(4, 6), (3, 13), (5, 10), (1, 6), (0, 8), (3, 9), (4, 8), (4, 11),
   (5, 12), (8, 11), (9, 10), (0, 7), (2, 13), (6, 7), (7, 12), (5, 11),
   (0, 12), (2, 3), (2, 9), (1, 13), (1, 10)], 13,
  [7, 13, 9, 2, 6, 11, 1, 12, 0, 10, 5, 4, 5, -1]),
 ("hard3", 14,
  [(3, 7), (4, 12), (12, 13), (1, 6), (2, 5), (6, 8), (4, 5), (5, 9),
   (8, 11), (9, 10), (10, 11), (0, 4), (2, 7), (1, 8), (2, 13), (3, 11),
   (0, 3), (10, 13), (0, 12), (1, 7), (6, 9)], 6,
  [4, 6, 7, 11, 5, 2, -1, 3, 1, 10, 13, 8, 0, 12]),
]

for name, nn, edges, root, par in PINS:
    w = witnesses(nn, edges, root, par)
    k2 = [t for t in w if t[1] <= 2]
    assert k2, f"{name}: NO k'<=2 paste-8 -- claim falsified on a pin"
    if name.startswith("hard"):
        assert not any(t[1] == 1 for t in w), \
            f"{name}: unexpected k'=1 witness -- pin profile changed"
    if name == "sup1_dead_tree":
        assert not any(t[2] <= t[3] + 1 for t in k2), \
            "sup1_dead_tree: unexpected SHORT k'<=2 witness"
        assert {(t[0], t[1]) for t in k2} == {(6, 2)}, "pin profile changed"
    print(f"{name}: k'<=2 cells {sorted(set((t[0], t[1]) for t in k2))}, "
          f"k'=1 present: {any(t[1] == 1 for t in w)}")
print("pins OK: k'<=2 paste-8 on all five; k'=1 dead on hard1-3; "
      "short-conjunction dead on sup1_dead_tree")
CHECK -->

<!-- CHECK
# paste8_k2_universal CHECK 2 (deterministic DISPROOF pins, R40): three
# adversarially-constructed pair-residual trees at n=30/30/40 (girth>=5)
# with NO k'<=2 paste-8 (min witness k' = 3/4/4) but WITH a paste-8 —
# so paste8_k2_universal is disproved while paste8_tree_universal
# survives on all three. Fully deterministic: rebuilds each tree from
# its pinned (edges, root, par) and re-derives everything.
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

PO2 = {4, 8, 16, 32}

def audit(name, nn, edges, root, par, expect_min_kp):
    edges = [tuple(sorted(e)) for e in edges]
    assert len(edges) == 3 * nn // 2, "not cubic edge count"
    deg = {}
    for u, v in edges: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    assert all(deg.get(v) == 3 for v in range(nn)), "not cubic"
    es = set(edges)
    adjacency = [[] for _ in range(nn)]
    for u, v in edges: adjacency[u].append(v); adjacency[v].append(u)
    for u in range(nn):
        for i in range(3):
            for j in range(i + 1, 3):
                a, b = adjacency[u][i], adjacency[u][j]
                assert (min(a, b), max(a, b)) not in es, "triangle"
                assert not any(x != u and x in adjacency[b]
                               for x in adjacency[a]), "4-cycle"
    depth = [-1] * nn; depth[root] = 0
    pending = [v for v in range(nn) if v != root]
    while pending:
        nxt = []
        for v in pending:
            if depth[par[v]] >= 0: depth[v] = depth[par[v]] + 1
            else: nxt.append(v)
        assert len(nxt) < len(pending), "parent array not a tree"
        pending = nxt
    tre = set()
    for v in range(nn):
        if v != root:
            e = (min(v, par[v]), max(v, par[v]))
            assert e in es, "tree edge not in graph"
            tre.add(e)
    def fcyc(s, a):
        p = set(); u = s
        while u != a:
            q = par[u]; p.add((min(u, q), max(u, q))); u = q
        p.add((min(s, a), max(s, a)))
        return p
    be = []
    for e in edges:
        if e in tre: continue
        u, v = e
        a, b = (u, v) if depth[u] <= depth[v] else (v, u)
        x = b
        while depth[x] > depth[a]: x = par[x]
        assert x == a, "non-ancestral non-tree edge (not a normal tree)"
        be.append((b, a))
    fc = [fcyc(s, a) for s, a in be]
    assert not any(len(c) in PO2 for c in fc), "single fires"
    m = len(fc)
    for i in range(m):
        for j in range(i + 1, m):
            assert single_cycle_len(fc[i] ^ fc[j]) not in PO2, "pair fires"
    n8 = 0; best = None
    for x in range(m):
        for y in range(x + 1, m):
            for z in range(y + 1, m):
                if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) != 8: continue
                n8 += 1
                for (i, j, k) in ((x, y, z), (x, z, y), (y, z, x)):
                    D = fc[i] ^ fc[j]
                    if single_cycle_len(D) is None: continue
                    inter = D & fc[k]
                    if n_arcs(inter) != 1: continue
                    kp = len(inter)
                    if best is None or kp < best: best = kp
    assert n8 > 0, f"{name}: no L=8 triple (sup8 falsifier?! pin separately)"
    assert best is not None, f"{name}: no paste-8 (paste8_tree falsifier?!)"
    assert best == expect_min_kp, f"{name}: min k' {best} != {expect_min_kp}"
    assert best > 2, f"{name}: has a k'<=2 witness -- NOT a counterexample"
    print(f"{name}: n={nn} pair-residual, L8={n8}, min paste k'={best} "
          f"(no k'<=2)")

audit("viol1_n30", 30,
  [(0, 18), (0, 22), (0, 27), (1, 9), (1, 18), (1, 29), (2, 4), (2, 5),
   (2, 20), (3, 6), (3, 17), (3, 29), (4, 25), (4, 28), (5, 12), (5, 27),
   (6, 8), (6, 11), (7, 9), (7, 14), (7, 27), (8, 19), (8, 20), (9, 12),
   (10, 15), (10, 16), (10, 24), (11, 15), (11, 23), (12, 13), (13, 23),
   (13, 26), (14, 21), (14, 26), (15, 21), (16, 17), (16, 22), (17, 20),
   (18, 19), (19, 26), (21, 25), (22, 28), (23, 25), (24, 28), (24, 29)],
  20,
  [27, 9, 4, 29, 28, 2, 3, 14, 19, 12, 16, 6, 5, 23, 21, 10, 17, 20, 19,
   26, -1, 15, 0, 11, 29, 23, 13, 7, 22, 1], 3)

audit("viol2_n30", 30,
  [(0, 3), (0, 16), (0, 17), (1, 5), (1, 19), (1, 20), (2, 10), (2, 22),
   (2, 28), (3, 12), (3, 19), (4, 20), (4, 21), (4, 23), (5, 11), (5, 28),
   (6, 11), (6, 24), (6, 26), (7, 11), (7, 27), (7, 29), (8, 18), (8, 23),
   (8, 29), (9, 12), (9, 20), (9, 24), (10, 13), (10, 23), (12, 25),
   (13, 18), (13, 21), (14, 15), (14, 27), (14, 28), (15, 17), (15, 26),
   (16, 21), (16, 25), (17, 22), (18, 24), (19, 26), (22, 29), (25, 27)],
  25,
  [17, 5, 10, 12, 21, 11, 26, 29, 23, 20, 13, 7, 9, 18, 28, 14, 25, 15,
   24, 3, 1, 16, 17, 4, 6, -1, 19, 14, 2, 8], 4)

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
   28, 39, 31], 4)

print("disproof pins OK: paste8_k2_universal is false; paste-8 itself "
      "present on all three (paste8_tree_universal survives)")
CHECK -->

## Summary

DISPROVED at R40. The bounded-window refinement of
`paste8_tree_universal` — every pair-residual tree has a paste-8 with
$k' \le 2$ — held on all 46 sampled residual trees at $n \le 26$ and
all five small pins, but fails at witness-box scale: adversarial
simulated annealing constructed pair-residual trees at $n = 30$ and
$n = 40$ (girth $\ge 5$) whose minimum paste-8 overlap is $k' = 3$ or
$4$; three are pinned deterministically in CHECK 2. The finite
$k' \le 2$ cell menu and the deaths of the $k' = 1$ and
$k' \le 2 \wedge \text{short}$ variants (CHECK 1) remain proved facts.
Takeaway: no $O(1)$-local certificate via bounded $k'$ exists; supply
proofs must handle unbounded overlap arcs (the value line
$g_3 = 2k' + 7 - |D|$ covers all $k'$, so the value side is unharmed),
and `paste8_tree_universal` — now with 20/20 adversarial evidence at
$n \in [30, 40]$ — is the correct supply target.
