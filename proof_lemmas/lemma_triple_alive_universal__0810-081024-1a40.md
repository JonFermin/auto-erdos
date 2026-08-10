---
id: triple_alive_universal
status: open
depends_on: [sup1_dead_tree, triple_sym_diff_structure, shortpaste_floor_line]
discharged_by_round: null
introduced_at_round: 34
---

# Lemma `triple_alive_universal` (conjecture + probe: every pair-residual tree fires via some triple, over ALL met-size channels)

**Setting.** $T$ a normal (Trémaux) spanning tree of a connected cubic
graph, back edges $B_1, \dots, B_m$ with fundamental cycles
$C_1, \dots, C_m$. $T$ is **pair-residual** if no $C_i$ and no
single-cycle $C_i \oplus C_j$ has power-of-2 length. $T$ is
**triple-alive** if some 3-subset $\{x, y, z\}$ has
$C_x \oplus C_y \oplus C_z$ a single cycle of power-of-2 length.

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual normal spanning tree of a connected cubic graph is
triple-alive.

**Why this replaces SUP-1 (R33 context).** The SUP-1 program restricted
the third edge to $k' = |D \cap C_3| = 1$ covers, short with matching
parity. `sup1_dead_tree` proves that restriction is unsatisfiable on
some pair-residual trees, while six triples still fire there through
$|D \cap C_3| \in \{2, 4\}$. Triple-aliveness is the honest,
mechanism-complete universal: for any pairing of the triple with
$D = C_x \oplus C_y$ a single cycle, the fired length is
$$L \;=\; |D| + |C_3| - 2\,|D \cap C_3|
      \;=\; |D| + \operatorname{gap}_3 + 1 - 2k'',$$
with no constraint on $k''$. Proving the claim (for $L$ hitting a
power of 2) subsumes SUP-8 and closes the tree-level supply gap of the
pasting program in one statement.

**Census (R34).** Four seeds, 571k sampled DFS trees, **176/176**
pair-residual trees triple-alive (144 across seeds 555/666/777 at
$n \in \{12..26\}$, 32 at the committed probe's seed):

| channel structure of the tree's firing triples | count |
|---|---|
| both $k''=1$ and $k'' \ge 2$ pairings fire (mixed) | 151 |
| only $k'' = 1$ channels fire | 13 |
| only $k'' \ge 2$ channels fire | 12 |

**Both sub-channels are individually insufficient** — 13 trees would
be missed by a $k'' \ge 2$-only rule, 12 by a $k''=1$-only rule (the
latter includes `sup1_dead_tree`'s pinned tree). Any analytic proof
must genuinely handle the disjunction. Every observed firing triple
admits at least one pairing whose 2-subset sym-diff is a single cycle
(the "no usable pairing" case never occurred).

**Analytic frame (R35+ targets).**

1. The $k''=1$ half is the old paste machinery (R23–R30: value
   interval, floor/line) — its supply fails alone but its arithmetic
   is proved and reusable where a $k''=1$ witness exists (and the
   parked R33 selection rule finds one 123/123 on alive trees).
2. The $k'' \ge 2$ half needs its own value analysis. On
   `sup1_dead_tree`'s tree the two firing shapes were ($|D| = 6$,
   $\operatorname{gap}_3 = 5$, $k'' = 2$) and ($|D| = 10$,
   $\operatorname{gap}_3 = 5$, $k'' = 4$) — both give $L = 8$ with the
   cover NOT short in the first shape. `pasting_cover_dichotomy`'s
   straddle alternative (which the SUP-1 program discarded as
   failure) is expected to be exactly the $k'' \ge 2$ producer:
   straddling covers meet two segments and have larger met sets.
3. Census the joint distribution $(|D|, \operatorname{gap}_3, k'')$ of
   firing triples on residual trees to find which identities pin
   $L = 8$ (all observed firings at $L = 8$; no $L \in \{4, 16, 32\}$
   firing has been recorded on a residual tree yet — worth asserting
   or refuting at scale).

<!-- CHECK
# triple_alive_universal CHECK 1 (deterministic anchor): the pinned
# SUP-1-dead tree from lemma_sup1_dead_tree is triple-alive with six
# firing triples, all L=8.
edges = [(5, 13), (0, 2), (10, 12), (1, 3), (7, 10), (6, 8), (4, 8), (3, 6),
         (3, 12), (5, 9), (4, 11), (0, 1), (9, 10), (1, 2), (9, 13), (0, 4),
         (2, 7), (6, 13), (5, 11), (11, 12), (7, 8)]
edges = [tuple(sorted(e)) for e in edges]
root = 11
nn = 14
par = [1, 2, 7, 12, 0, 11, 3, 8, 6, 13, 9, -1, 10, 5]
PO2_LENS = {4, 8, 16, 32}

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

tre = {(min(v, par[v]), max(v, par[v])) for v in range(nn) if v != root}
be = []
for u, v in [e for e in edges if e not in tre]:
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
    for u, v in sym: dg[u] = dg.get(u, 0) + 1; dg[v] = dg.get(v, 0) + 1
    if any(d != 2 for d in dg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    start = next(iter(dg)); sn = {start}; st = [start]
    while st:
        u = st.pop()
        for w in adjS[u]:
            if w not in sn: sn.add(w); st.append(w)
    return len(sym) if len(sn) == len(dg) else None

fc = [fund_cycle_edges(s, a) for s, a in be]
m = len(fc)
firing = [(x, y, z)
          for x in range(m) for y in range(x + 1, m) for z in range(y + 1, m)
          if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) == 8]
assert len(firing) == 6, f"expected 6 firing triples on the anchor, got {len(firing)}"
print(f"anchor OK: sup1_dead_tree's pinned tree is triple-alive ({len(firing)} triples, L=8)")
CHECK -->

<!-- CHECK
# triple_alive_universal CHECK 2 (falsification probe): every sampled
# pair-residual cubic DFS tree is triple-alive.  Fixed seed; an assert
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
    tree_mask = 0
    for i, (u, v) in enumerate(edges):
        if depth[u] == depth[v] + 1 and par[u] == v: tree_mask |= 1 << i
        elif depth[v] == depth[u] + 1 and par[v] == u: tree_mask |= 1 << i
    nontree = []
    for i, (u, v) in enumerate(edges):
        if not (tree_mask >> i & 1):
            a, b = (u, v) if depth[u] <= depth[v] else (v, u)
            if not is_ancestor(a, b, depth, par): return None
            nontree.append((b, a, depth[b] - depth[a]))
    return depth, par, nontree


def fund_cycle_edges(sender, ancestor, par):
    path = set(); u = sender
    while u != ancestor:
        p = par[u]; path.add((min(u, p), max(u, p))); u = p
    path.add((min(sender, ancestor), max(sender, ancestor)))
    return path


def single_cycle_len(sym):
    if not sym: return None
    deg = {}
    for u, v in sym: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if any(d != 2 for d in deg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    start = next(iter(deg)); seen = {start}; stk = [start]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(sym) if len(seen) == len(deg) else None


rng = random.Random(20260810)
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
            fc = [fund_cycle_edges(s, a, par) for s, a, d in be]
            if any(len(c) in PO2_LENS for c in fc): continue
            pair_fire = False
            for i in range(m):
                for j in range(i + 1, m):
                    if single_cycle_len(fc[i] ^ fc[j]) in PO2_LENS:
                        pair_fire = True; break
                if pair_fire: break
            if pair_fire: continue
            residual += 1
            fired = False
            for x in range(m):
                if fired: break
                for y in range(x + 1, m):
                    if fired: break
                    for z in range(y + 1, m):
                        if single_cycle_len(fc[x] ^ fc[y] ^ fc[z]) in PO2_LENS:
                            fired = True; break
            assert fired, \
                (f"FALSIFIED triple_alive_universal: pair-residual tree with "
                 f"no firing triple (n={nn}, root={r}, par={par}, "
                 f"edges={edges})")

assert trees_seen > 100000, f"too few trees: {trees_seen}"
assert residual >= 25, f"too few residual trees: {residual} — probe vacuous"
print(f"trees={trees_seen} residual={residual} — every pair-residual tree "
      f"is triple-alive")
CHECK -->

## Summary

The post-SUP-1 supply universal: every pair-residual normal spanning
tree of a cubic graph admits SOME triple of back edges whose 3-way
sym-diff is a single power-of-2 cycle, with no restriction on the met
size $k''$. Census 176/176 across four seeds (571k trees); channel
split shows both the $k''=1$ (old paste) and $k'' \ge 2$ (straddle)
sub-channels are individually insufficient — 12 trees fire only
through $k'' \ge 2$ (including `sup1_dead_tree`'s pinned anchor,
verified deterministically in CHECK 1), 13 only through $k'' = 1$.
Proving this claim subsumes SUP-8 and closes tree-level supply; the
$k'' \ge 2$ side needs a value theory the program does not yet have
(R35 target: joint $(|D|, \operatorname{gap}_3, k'')$ census; expected
producer: the straddle branch of `pasting_cover_dichotomy`).
