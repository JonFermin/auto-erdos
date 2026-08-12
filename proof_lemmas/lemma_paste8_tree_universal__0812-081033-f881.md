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

## Summary

The channel-sharpened supply conjecture, motivated by the R38 census:
every pair-residual normal spanning tree of a cubic graph has an
$L = 8$ firing triple realized through a 1-arc (paste) usable pairing,
so the straddle channel — though present — is never necessary for
8-supply. Unfalsified at 43/43 fresh-census residual trees plus both
deterministic pins (where ALL 12 $L = 8$ triples are paste-realizable).
If proved, the supply program collapses to the paste 8-line
$g_3 = 2k' + 7 - |D|$ where the strongest structural machinery lives;
if falsified, the pinned tree redirects effort to the straddle 8-line
without touching the weaker universals below it.
