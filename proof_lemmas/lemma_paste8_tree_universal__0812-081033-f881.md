---
id: paste8_tree_universal
status: open
depends_on: [sup8_tree_universal, shortpaste_floor_line, straddle_floor_line]
discharged_by_round: null
introduced_at_round: 38
---

# Lemma `paste8_tree_universal` (conjecture + probe: every pair-residual tree has a PASTE-channel $L = 8$ firing)

**Setting.** As in `sup8_tree_universal`: $T$ a pair-residual normal
spanning tree of a connected cubic graph. A triple $\{x, y, z\}$
**fires at 8 through the paste channel** if
$C_x \oplus C_y \oplus C_z$ is a single 8-cycle AND for some ordering
of the triple into (pair, cover) — $D = C_i \oplus C_j$ a single cycle,
$B_k$ the cover — the intersection $D \cap C_k$ is a **single arc**
(so `shortpaste_floor_line`'s exact line $g_3 = 2k' + 7 - |D|$ governs
the value).

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual normal spanning tree of a connected cubic graph has
some paste-channel $L = 8$ firing triple.

**Why this refinement matters.** By `straddle_floor_line`(1) every
usable pairing is paste (1 arc) or straddle (2 arcs), and both channels
now carry exact value lines. This claim says the straddle channel is
never NECESSARY for 8-supply: if it holds, the supply argument can
target the paste line alone — the channel where the proved structural
machinery is strongest (`pasting_vertex_automatic` makes $k'' = 1$
covers automatic pastes; `pasting_cover_dichotomy`(c1)–(c3) give cheap
paste certificates; `shortpaste_floor_line`(b) frees the arithmetic
half). It is strictly stronger than `sup8_tree_universal`, which is
strictly stronger than `triple_alive_universal`; failures cascade down
gracefully — a falsifier here would be the first residual tree whose
8-supply genuinely needs a straddle, redirecting effort to the straddle
8-line ($k_{12} + |L_j| + \Sigma = 5$) without touching the weaker
universals.

**Evidence.**

- Fresh channel census (seed 20260812+38; $n \in \{12..22\}$, 128,800
  trees, 43 pair-residual): **43/43 residual trees have a paste-8**;
  0 straddle-only trees, 0 trees without an 8.
- Both deterministic pins comply maximally: on `l8_exactness_dead`'s
  12-vertex tree and `sup1_dead_tree`'s 14-vertex tree, ALL $L = 8$
  triples (6/6 and 6/6) admit a 1-arc usable pairing — not a single
  $L = 8$ triple on either pin needs the straddle channel.
- Straddle-8s do coexist (the same census saw straddle-8 pairings on
  many of the 43 trees, dominated by $(k_{12}, |L_j|) = (1, 0)$ and
  $(3, 0)$) — the claim is about necessity, not absence.
- **Above-floor adversarial evidence (R40)**: 20/20 pair-residual trees
  constructed by simulated annealing at $n \in \{30, 32, 36, 40\}$,
  girth $\ge 5$ (where rejection sampling finds nothing), all have a
  paste-8 — including the three trees that DISPROVE the $k' \le 2$
  refinement `paste8_k2_universal` (their min paste-8 $k'$ is 3–4).
  First evidence above the $n \ge 30$ minimal-counterexample floor.

- **Direct adversarial attack survived (R41, Q70)**: two independent SA
  runs whose energy PENALIZED availability itself (lexicographic:
  residuality violations first, then #paste-8 / #L=8 / #po2-firing
  triples), n in [30, 64], girth >= 5, ~2.9M SA iterations total:
  **261 pair-residual trees constructed (138 + 123), zero without a
  paste-8** — and zero without an L=8, zero without a po2 firing, so
  the whole ladder survives. Anti-paste8 pressure squeezed availability
  to as little as TWO L=8 triples on one n=32 tree (both paste,
  pinned in CHECK 3) but never to zero. In ALL 261 trees, every L=8
  firing triple admits a paste pairing — the straddle channel was
  never necessary anywhere, even under pressure. Min paste k' reached
  **5** (at n=32 AND n=40, pinned): forced-large overlap arcs appear
  under adversarial pressure already at n=32, confirming the
  unbounded-k' burden is intrinsic, not a large-n artifact.
- **Top-of-box extension (R42, Q72)**: a third SA run targeting
  n in {58, 60, 62, 64} with doubled restart budgets constructed 13
  more pair-residual trees (3 at n=58, 10 at n=60, independently
  re-audited): all 13 keep a paste-8 (anti-paste8 pressure bottomed at
  5 paste-8 triples), zero straddle-only L=8 triples again. Adversarial
  coverage now reaches n=60; **274/274 total**. n in {62, 64} remains
  unreached — pair-residual states are too sparse there even for 140s
  restarts (0 residuals in ~1.1M SA iterations); closing the last two
  even values needs a warm-started or structure-seeded search, noted
  as residual risk rather than evidence.

<!-- CHECK
# paste8_tree_universal CHECK 1 (deterministic pins): on both pinned
# residual trees, EVERY L=8 firing triple admits a 1-arc (paste)
# usable pairing: 6/6 on the l8_exactness_dead tree (n=12, root 10)
# and 6/6 on the sup1_dead_tree tree (n=14, root 11).
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

def audit(name, nn, edges, root, par, expect8):
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
    m = len(fc)
    n8 = 0; paste8 = 0
    for x in range(m):
        for y in range(x + 1, m):
            for z in range(y + 1, m):
                if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) != 8: continue
                n8 += 1
                for (i, j, k) in ((x, y, z), (x, z, y), (y, z, x)):
                    D = fc[i] ^ fc[j]
                    if single_cycle_len(D) is None: continue
                    if n_arcs(D & fc[k]) == 1:
                        paste8 += 1; break
    assert (n8, paste8) == (expect8, expect8), \
        f"{name}: expected {expect8}/{expect8} paste-realizable, got {paste8}/{n8}"
    print(f"{name}: {paste8}/{n8} L=8 triples paste-realizable")

audit("l8_exactness_dead pin", 12,
      [(4, 10), (1, 2), (5, 11), (0, 10), (5, 8), (3, 7), (6, 8), (2, 10),
       (1, 4), (0, 6), (6, 7), (4, 5), (8, 9), (2, 9), (1, 7), (3, 9),
       (0, 11), (3, 11)],
      10, [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0], 6)
audit("sup1_dead_tree pin", 14,
      [(5, 13), (0, 2), (10, 12), (1, 3), (7, 10), (6, 8), (4, 8), (3, 6),
       (3, 12), (5, 9), (4, 11), (0, 1), (9, 10), (1, 2), (9, 13), (0, 4),
       (2, 7), (6, 13), (5, 11), (11, 12), (7, 8)],
      11, [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5], 6)
print("pins OK: neither pinned residual tree needs the straddle channel")
CHECK -->

<!-- CHECK
# paste8_tree_universal CHECK 2 (falsification probe): every sampled
# pair-residual cubic DFS tree has an L=8 firing triple realized
# through a 1-arc (paste) usable pairing. Fresh seed (20260812);
# an assert failure prints the tree for pinning.
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


rng = random.Random(20260812)
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
            has_paste8 = False
            for x in range(m):
                if has_paste8: break
                for y in range(x + 1, m):
                    if has_paste8: break
                    for z in range(y + 1, m):
                        if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) != 8:
                            continue
                        for (i, j, k) in ((x, y, z), (x, z, y), (y, z, x)):
                            D = fc[i] ^ fc[j]
                            if single_cycle_len(D) is None: continue
                            if n_arcs(D & fc[k]) == 1:
                                has_paste8 = True; break
                        if has_paste8: break
            assert has_paste8, \
                (f"FALSIFIED paste8_tree_universal: pair-residual tree with "
                 f"no paste-channel L=8 firing (n={nn}, root={r}, par={par}, "
                 f"edges={edges})")

assert trees_seen > 100000, f"too few trees: {trees_seen}"
assert residual >= 25, f"too few residual trees: {residual} -- probe vacuous"
print(f"trees={trees_seen} residual={residual} -- every pair-residual tree "
      f"has a paste-channel L=8 firing triple")
CHECK -->

<!-- CHECK
# paste8_tree_universal CHECK 3 (R41 adversarial-survivor pins): three
# pair-residual trees constructed by SA whose energy PENALIZED paste-8 /
# any-8 / any-po2 availability (Q70 ladder-hardening).  All three keep a
# paste-8 despite direct pressure: surv_thin_n32's availability was
# squeezed to exactly TWO L=8 triples (both paste-realizable, min k'=2);
# surv_kp5_n32 and surv_kp5_n40 have min paste k' = 5 -- the largest
# observed, and already at n=32, so large forced k' is NOT a large-n
# phenomenon.  On all three, EVERY L=8 triple admits a paste pairing.
# Fully deterministic: rebuilds each tree from its pinned
# (edges, root, par); asserts cubic + girth>=5 + normal + pair-residual.
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

def audit(name, nn, edges, root, par, exp_po2, exp_l8, exp_min_kp):
    edges = [tuple(sorted(e)) for e in edges]
    assert len(edges) == 3 * nn // 2 and len(set(edges)) == len(edges)
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
    po2 = l8 = p8 = 0; min_kp = None
    for x in range(m):
        for y in range(x + 1, m):
            for z in range(y + 1, m):
                L = single_cycle_len(fc[x] ^ fc[y] ^ fc[z])
                if L not in PO2: continue
                po2 += 1
                if L != 8: continue
                l8 += 1
                pasted = False
                for (i, j, k) in ((x, y, z), (x, z, y), (y, z, x)):
                    D = fc[i] ^ fc[j]
                    if single_cycle_len(D) is None: continue
                    inter = D & fc[k]
                    if inter and n_arcs(inter) == 1:
                        pasted = True
                        kp = len(inter)
                        if min_kp is None or kp < min_kp: min_kp = kp
                if pasted: p8 += 1
    assert (po2, l8) == (exp_po2, exp_l8), \
        f"{name}: (po2, l8) = ({po2}, {l8}) != ({exp_po2}, {exp_l8})"
    assert p8 == l8, f"{name}: straddle-only L=8 triple present ({p8}/{l8})"
    assert p8 > 0, f"{name}: NO paste-8 -- claim falsified, pin separately"
    assert min_kp == exp_min_kp, f"{name}: min k' {min_kp} != {exp_min_kp}"
    print(f"{name}: n={nn} pair-residual, po2={po2}, L8={l8} (all paste), "
          f"min k'={min_kp}")

PINS = [
# surv_thin_n32: thin survivor: anti-paste8 SA pressed availability to TWO L=8 triples, both paste
 ("surv_thin_n32", 32,
  [(0, 17), (0, 21), (0, 23), (1, 20), (1, 23), (1, 28), (2, 17), (2,
   19), (2, 27), (3, 9), (3, 25), (3, 28), (4, 16), (4, 22), (4, 26),
   (5, 7), (5, 8), (5, 26), (6, 10), (6, 11), (6, 12), (7, 15), (7,
   24), (8, 25), (8, 27), (9, 12), (9, 20), (10, 30), (10, 31), (11,
   13), (11, 17), (12, 21), (13, 24), (13, 31), (14, 16), (14, 28),
   (14, 30), (15, 18), (15, 25), (16, 18), (18, 20), (19, 23), (19,
   24), (21, 29), (22, 27), (22, 29), (26, 31), (29, 30)],
  18,
  [17, 28, 27, 9, 22, 7, 11, 15, 5, 20, 31, 13, 6, 24, 16, 25, 18, 2,
   -1, 23, 1, 12, 29, 0, 19, 3, 4, 8, 14, 21, 10, 26],
  22, 2, 2),
# surv_kp5_n32: min paste k' = 5 already at n=32
 ("surv_kp5_n32", 32,
  [(0, 1), (0, 9), (0, 25), (1, 7), (1, 15), (2, 3), (2, 18), (2, 27),
   (3, 24), (3, 29), (4, 5), (4, 15), (4, 16), (5, 26), (5, 31), (6,
   16), (6, 23), (6, 25), (7, 8), (7, 19), (8, 27), (8, 29), (9, 20),
   (9, 22), (10, 17), (10, 23), (10, 31), (11, 28), (11, 29), (11, 30),
   (12, 13), (12, 15), (12, 19), (13, 18), (13, 26), (14, 22), (14,
   23), (14, 30), (16, 24), (17, 22), (17, 27), (18, 20), (19, 28),
   (20, 21), (21, 24), (21, 30), (25, 31), (26, 28)],
  7,
  [1, 15, 18, 29, 16, 31, 23, -1, 7, 22, 17, 28, 13, 26, 30, 4, 6, 27,
   20, 12, 9, 24, 14, 10, 3, 0, 5, 2, 19, 8, 21, 25],
  43, 4, 5),
# surv_kp5_n40: min paste k' = 5 at n=40
 ("surv_kp5_n40", 40,
  [(0, 10), (0, 31), (0, 32), (1, 20), (1, 22), (1, 36), (2, 7), (2,
   17), (2, 33), (3, 22), (3, 34), (3, 35), (4, 25), (4, 27), (4, 29),
   (5, 18), (5, 27), (5, 33), (6, 26), (6, 33), (6, 38), (7, 13), (7,
   16), (8, 25), (8, 26), (8, 39), (9, 32), (9, 34), (9, 36), (10, 15),
   (10, 16), (11, 19), (11, 31), (11, 35), (12, 23), (12, 32), (12,
   37), (13, 29), (13, 30), (14, 16), (14, 19), (14, 30), (15, 23),
   (15, 39), (17, 24), (17, 28), (18, 21), (18, 37), (19, 20), (20,
   34), (21, 24), (21, 25), (22, 30), (23, 24), (26, 35), (27, 38),
   (28, 36), (28, 37), (29, 39), (31, 38)],
  31,
  [32, 20, 33, 22, 25, 27, 38, 16, 39, 36, 0, 35, 37, 7, 19, 23, 14, 2,
   5, 11, 34, 24, 30, 12, 17, 21, 8, 4, 36, 13, 13, -1, 9, 6, 3, 26, 1,
   18, 31, 15],
  54, 4, 5),
]
for row in PINS:
    audit(*row)
print("R41 survivor pins OK: paste-8 survives direct adversarial pressure; "
      "no straddle-only L=8 anywhere; min paste k' reaches 5 at n=32")
CHECK -->

## Summary

The channel-sharpened supply conjecture, motivated by the R38 census:
every pair-residual normal spanning tree of a cubic graph has an
$L = 8$ firing triple realized through a 1-arc (paste) usable pairing,
so the straddle channel — though present — is never necessary for
8-supply. Unfalsified at 43/43 fresh-census residual trees, both deterministic
pins (where ALL 12 $L = 8$ triples are paste-realizable), 20/20 R40
adversarial trees at $n \in [30, 40]$, and — under DIRECT adversarial
pressure on availability itself — 261/261 SA-hardened trees at
$n \in [30, 56]$ (R41), where every $L = 8$ triple everywhere admits a
paste pairing and min paste $k'$ reaches 5.
If proved, the supply program collapses to the paste 8-line
$g_3 = 2k' + 7 - |D|$ where the strongest structural machinery lives;
if falsified, the pinned tree redirects effort to the straddle 8-line
without touching the weaker universals below it.
