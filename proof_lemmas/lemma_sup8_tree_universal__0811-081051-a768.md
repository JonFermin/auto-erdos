---
id: sup8_tree_universal
status: disproved
depends_on: [triple_alive_universal, l8_exactness_dead]
discharged_by_round: 46
introduced_at_round: 36
---

# Lemma `sup8_tree_universal` (conjecture + probe: every pair-residual tree has an $L = 8$ firing triple)

**DISPROVED (R46, session s_0817-081104-2f11).** `sb_falsifier_n18` (pinned with full data in `lemma_paste8_samebranch_universal` CHECK 4) is a pair-residual tree whose PO2 firing triples are ALL at $L = 16$ — it has NO firing triple at $L = 8$: the full pasting value set is $V(T) = \{6, 7, 9, \dots, 16\}$, holed exactly at 8. The $L = 8$ exclusivity that shaped R23–R46 is dead; the honest universal is `triple_alive_universal` (any PO2), which this tree satisfies at 16 via chain (same-branch) pastings — see `pastePO2_samebranch_universal`.


**Setting.** As in `triple_alive_universal`: $T$ a normal spanning tree
of a connected cubic graph, pair-residual (no fundamental cycle and no
single-cycle 2-subset sym-diff of power-of-2 length). A triple
$\{x,y,z\}$ **fires at $L$** if $C_x \oplus C_y \oplus C_z$ is a single
cycle of length $L \in \{4, 8, 16, 32\}$.

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual normal spanning tree of a connected cubic graph has
some firing triple at $L = 8$ **exactly**.

**Relation to the R35 fork.** `l8_exactness_dead` killed the
per-firing form (firings at $L = 4$ and $L = 16$ exist), so this
per-tree form is the strongest 8-specific supply statement left. It is
strictly stronger than `triple_alive_universal`; the two split the
analytic burden:

- if THIS claim holds, the value theory only ever has to produce 8 —
  the R23 tuning reduction ("targets only 8, never 16 or 32", Section
  48) becomes unconditional, and the $k'' \ge 2$ straddle analysis can
  fix its target length;
- if it dies, the pinned tree will show which residual trees must be
  served by 4, 16, or 32 instead, and `triple_alive_universal` (the
  full disjunction) remains the honest universal.

**Evidence (R35 census).** 295/295 tracked residual trees had 8 among
their firing lengths (sets: $\{8\}$ 225x, $\{4,8\}$ 31x, $\{8,16\}$
36x, $\{4,8,16\}$ 3x); adding R34's 176 trees (all of whose observed
firings were $L = 8$) gives 471/471 across ten seeds. Both pinned
deterministic anchors — `sup1_dead_tree`'s 14-vertex tree (6/6 firings
at 8) and `l8_exactness_dead`'s 12-vertex tree (6/7 at 8) — comply.

**Evidence (R41 ladder-hardening).** Two independent adversarial SA
runs biased AGAINST 8-availability (energy penalizing #L=8 triples on
pair-residual trees; also the anti-paste8 and anti-po2 variants),
$n \in [30, 64]$, girth $\ge 5$: **261/261 constructed pair-residual
trees have an $L = 8$ firing triple** — zero falsifiers. The
anti-sup8 energy drove one n=44 tree (run 1) down to a single L=8
triple, never to zero. Strongest above-floor evidence to date.

<!-- CHECK
# sup8_tree_universal CHECK 1 (deterministic anchor): the pinned
# l8_exactness_dead tree (which fires at L=4) nonetheless has six
# L=8 firing triples.
edges = [(4, 10), (1, 2), (5, 11), (0, 10), (5, 8), (3, 7), (6, 8), (2, 10),
         (1, 4), (0, 6), (6, 7), (4, 5), (8, 9), (2, 9), (1, 7), (3, 9),
         (0, 11), (3, 11)]
edges = [tuple(sorted(e)) for e in edges]
root = 10
nn = 12
par = [10, 4, 9, 7, 5, 11, 8, 1, 9, 3, -1, 0]

depth = [-1] * nn
depth[root] = 0
pending = [v for v in range(nn) if v != root]
while pending:
    nxt = []
    for v in pending:
        if depth[par[v]] >= 0: depth[v] = depth[par[v]] + 1
        else: nxt.append(v)
    assert len(nxt) < len(pending)
    pending = nxt

def is_ancestor(u, v):
    if depth[u] > depth[v]: return False
    x = v
    while depth[x] > depth[u]: x = par[x]
    return x == u

tre = set()
for v in range(nn):
    if v != root:
        tre.add((min(v, par[v]), max(v, par[v])))
be = []
for e in edges:
    if e in tre: continue
    u, v = e
    a, b = (u, v) if depth[u] <= depth[v] else (v, u)
    assert is_ancestor(a, b)
    be.append((b, a))

def fund_cycle_edges(sender, ancestor):
    path = set(); u = sender
    while u != ancestor:
        p = par[u]; path.add((min(u, p), max(u, p))); u = p
    path.add((min(sender, ancestor), max(sender, ancestor)))
    return path

def single_cycle_len(sym):
    if not sym: return None
    dg = {}
    for u, v in sym:
        dg[u] = dg.get(u, 0) + 1
        dg[v] = dg.get(v, 0) + 1
    if any(dg[x] != 2 for x in dg): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v)
        adjS.setdefault(v, []).append(u)
    start = sorted(dg)[0]; sn = {start}; st = [start]
    while st:
        u = st.pop()
        for w in adjS[u]:
            if w not in sn: sn.add(w); st.append(w)
    return len(sym) if len(sn) == len(dg) else None

fc = [fund_cycle_edges(s, a) for s, a in be]
m = len(fc)
n8 = 0
for x in range(m):
    for y in range(x + 1, m):
        for z in range(y + 1, m):
            if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) == 8: n8 += 1
assert n8 == 6, f"expected 6 L=8 firing triples on the anchor, got {n8}"
print(f"anchor OK: the L=4-firing pinned tree still has {n8} L=8 triples")
CHECK -->

<!-- CHECK
# sup8_tree_universal CHECK 2 (falsification probe): every sampled
# pair-residual cubic DFS tree has a firing triple at L == 8 EXACTLY.
# Fresh seed (distinct from triple_alive_universal CHECK 2); an assert
# failure prints the tree (graph + root + parent array) for pinning.
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


rng = random.Random(20260811)
trees_seen = 0
residual = 0

for nn, trials in ((12, 4000), (14, 4000), (16, 3000),
                   (18, 2000), (20, 1500), (22, 1200)):
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
            has8 = False
            for x in range(m):
                if has8: break
                for y in range(x + 1, m):
                    if has8: break
                    for z in range(y + 1, m):
                        if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) == 8:
                            has8 = True; break
            assert has8, \
                (f"FALSIFIED sup8_tree_universal: pair-residual tree with "
                 f"no L=8 firing triple (n={nn}, root={r}, par={par}, "
                 f"edges={edges})")

assert trees_seen > 100000, f"too few trees: {trees_seen}"
assert residual >= 25, f"too few residual trees: {residual} -- probe vacuous"
print(f"trees={trees_seen} residual={residual} -- every pair-residual tree "
      f"has an L=8 firing triple")
CHECK -->

## Summary

The per-tree SUP-8 conjecture, split off from `triple_alive_universal`
after R35 killed the per-firing $L = 8$ exactness: every pair-residual
normal spanning tree of a cubic graph has SOME firing triple whose
3-way sym-diff is a single cycle of length exactly 8. Unfalsified at
471/471 residual trees across ten seeds (R34 + R35 censuses) plus both
deterministic pinned anchors. If proved, the value theory's target
length is fixed at 8 and the R23 tuning reduction becomes
unconditional; if falsified, the program falls back to the full
power-of-2 disjunction of `triple_alive_universal`.
