---
id: paste8_k2_universal
status: open
depends_on: [paste8_tree_universal, shortpaste_floor_line]
discharged_by_round: null
introduced_at_round: 39
---

# Lemma `paste8_k2_universal` (conjecture + probe: every pair-residual tree has a paste-8 witness with $k' \le 2$ — an $O(1)$-local supply certificate)

**Setting.** As in `paste8_tree_universal`: $T$ a pair-residual normal
spanning tree of a connected cubic graph. A **paste-8 witness** is a
triple with an ordering (pair, cover) such that $D = C_i \oplus C_j$ is
a single cycle, $D \cap C_k$ is a single arc of $k'$ edges, and
$|D \oplus C_k| = 8$ — equivalently (`shortpaste_floor_line`(4)) the
cell $(|D|, k')$ lies on the 8-line $g_3 = 2k' + 7 - |D|$.

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual normal spanning tree of a connected cubic graph has
a paste-8 witness with $k' \le 2$.

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

**Evidence for the claim.**

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
# paste8_k2_universal CHECK 2 (falsification probe): every sampled
# pair-residual cubic DFS tree has a paste-8 witness with k' <= 2.
# Fresh seed (20260814); an assert failure prints the tree for pinning.
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


def fund_cycle_edges(sender, ancestor, par):
    path = set(); u = sender
    while u != ancestor:
        p = par[u]; path.add((min(u, p), max(u, p))); u = p
    path.add((min(sender, ancestor), max(sender, ancestor)))
    return path


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


rng = random.Random(20260814)
trees_seen = 0
residual = 0

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
            fc = [fund_cycle_edges(s, a, par) for s, a in be]
            if any(len(c) in PO2_LENS for c in fc): continue
            pair_fire = False
            for i in range(m):
                for j in range(i + 1, m):
                    if single_cycle_len(fc[i] ^ fc[j]) in PO2_LENS:
                        pair_fire = True; break
                if pair_fire: break
            if pair_fire: continue
            residual += 1
            has_k2 = False
            for x in range(m):
                if has_k2: break
                for y in range(x + 1, m):
                    if has_k2: break
                    for z in range(y + 1, m):
                        if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) != 8:
                            continue
                        for (i, j, k) in ((x, y, z), (x, z, y), (y, z, x)):
                            D = fc[i] ^ fc[j]
                            if single_cycle_len(D) is None: continue
                            inter = D & fc[k]
                            if n_arcs(inter) == 1 and len(inter) <= 2:
                                has_k2 = True; break
                        if has_k2: break
            assert has_k2, \
                (f"FALSIFIED paste8_k2_universal: pair-residual tree with "
                 f"no k'<=2 paste-8 (n={nn}, root={r}, par={par}, "
                 f"edges={edges})")

assert trees_seen > 100000, f"too few trees: {trees_seen}"
assert residual >= 25, f"too few residual trees: {residual} -- probe vacuous"
print(f"trees={trees_seen} residual={residual} -- every pair-residual tree "
      f"has a k'<=2 paste-8 witness")
CHECK -->

## Summary

The bounded-window refinement of `paste8_tree_universal`, motivated by
the R39 cell census: every pair-residual tree has a paste-8 witness
with overlap arc $k' \le 2$, hence (proved menu) with $|D| \le 9$ and
cover length $\le 9$ — an $O(1)$-local certificate. The natural
stronger forms are dead against pins: $k' = 1$ fails on three pinned
$n = 14$ trees, and $k' \le 2 \wedge \text{short}$ fails on
`sup1_dead_tree`. Unfalsified at 46/46 census trees plus all five pins;
if proved, the supply argument reduces to a bounded-configuration
analysis with the value side already closed by `shortpaste_floor_line`.
