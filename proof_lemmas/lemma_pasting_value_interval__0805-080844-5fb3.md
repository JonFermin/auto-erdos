---
id: pasting_value_interval
status: open
depends_on: [triple_sym_diff_structure, fund_pair_overlap, pasting_rescue_census]
discharged_by_round: null
introduced_at_round: 23
---

# Lemma `pasting_value_interval` (conjecture + falsification probe: the pasting value set is a step-2 interval containing 8)

**Setting.** As in `pasting_rescue_census`. For a DFS tree $T$ of a
connected cubic graph, the **pasting value set** is

$$V(T) \;=\; \bigl\{\, |D| + \operatorname{gap}_3 + 1 - 2k' \;:\;
   (B_1,B_2,B_3) \text{ a legal pasting config} \,\bigr\},$$

where a *legal pasting config* is an unordered pair $\{B_1,B_2\}$ of back
edges whose sym-diff $D = C_1 \triangle C_2$ is a single simple cycle
(`fund_pair_overlap`: iff the tree paths overlap in $k_{12} \ge 1$ edges),
together with a third back edge $B_3 \notin \{B_1,B_2\}$ whose fundamental
cycle meets $D$ in a single path of $k' \ge 1$ edges. By
`triple_sym_diff_structure`(4–5), every $L \in V(T)$ is realized as the
length of a single simple cycle in $G$ (namely
$C_1 \triangle C_2 \triangle C_3$). Write
$V_e(T) = \{ L \in V(T) : L \text{ even} \}$.

**Claim (open, universally quantified — sampling can only falsify).**
For every **pair-residual** tree $T$ (no PO2 fundamental cycle, no pair of
back edges with single-PO2-cycle sym-diff, as in `pasting_rescue_census`):

1. **(Tuning to 8.)** $8 \in V(T)$.
2. **(Interval structure.)** $V_e(T)$ is a step-2 interval:
   $V_e(T) = \{v_{\min}, v_{\min}+2, \dots, v_{\max}\}$ with no gaps.

Together with $v_{\min} \le 8 \le v_{\max}$ (implied by 1+2), this is the
exact pigeonhole structure the Q9 tuning argument needs: it reduces
"some triple fires at a PO2" to the two endpoint bounds
$v_{\min} \le 8$ and $v_{\max} \ge 8$ plus interval-ness.

**Status.** Open. The CHECK below is the R23 dual-attack probe (standing
policy): an assertion failure exhibits a concrete pair-residual tree whose
value set either misses 8 (killing the tuning-to-8 formulation — the
analytic argument would have to target 16/32 as well) or has a gap
(killing the pure pigeonhole route). It extends the R20 probe, which
recorded only the first firing shape per tree, not the full value set.

**Calibration evidence (standalone runs, 2026-08-05).** 240k sampled DFS
trees over $n \in \{12,\dots,22\}$ yielded 53 pair-residual trees:
$8 \in V$ in **53/53**, $V_e$ a perfect step-2 interval in **53/53**,
$v_{\min} \in \{4,6,8\}$ (always $\le 8$), $v_{\max} \in \{10,\dots,18\}$
growing with $n$ — the interval *widens* with $n$, so the containment of
8 gets slacker, not tighter, at scale. Value sets moreover typically
contain consecutive integers (both parities), and $k'$ sweeps $1..12$ —
the $\pm1$ freedom in $k'$ across adjacent configs is the visible source
of interval-ness.

---

<!-- CHECK
# pasting_value_interval: for every pair-residual cubic DFS tree, compute
# the FULL pasting value set V = {|D| + gap3 + 1 - 2k'} over legal
# (pair, B3) configs; assert 8 in V and that the even part of V is a
# step-2 interval. Census min/max endpoints.
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


def path_len_of_intersection(cyc1, cyc2):
    es = cyc1 & cyc2
    if not es: return None
    vs1 = {v for e in cyc1 for v in e}
    vs2 = {v for e in cyc2 for v in e}
    shared_v = vs1 & vs2
    deg = {}
    for u, v in es: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if set(deg) != shared_v: return None
    ends = [v for v, d in deg.items() if d == 1]
    if len(ends) != 2 or any(d > 2 for d in deg.values()): return None
    adjP = {}
    for u, v in es:
        adjP.setdefault(u, []).append(v); adjP.setdefault(v, []).append(u)
    seen = {ends[0]}; stk = [ends[0]]
    while stk:
        u = stk.pop()
        for w in adjP[u]:
            if w not in seen: seen.add(w); stk.append(w)
    if len(seen) != len(deg): return None
    return len(es)


rng = random.Random(20260805 + 23)
trees_seen = 0
residual = 0
vmin_census = {}
vmax_census = {}

for nn, trials in ((12, 5000), (14, 5000), (16, 5000),
                   (18, 3000), (20, 3000), (22, 3000)):
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
            fc = [fund_cycle_edges(s, a, par) for s, a, _ in be]
            if any(len(c) in PO2_LENS for c in fc): continue
            pair_fires = False
            for i in range(m):
                for j in range(i + 1, m):
                    if single_cycle_len(fc[i] ^ fc[j]) in PO2_LENS:
                        pair_fires = True; break
                if pair_fires: break
            if pair_fires: continue
            residual += 1
            V = set()
            for x in range(m):
                for y in range(x + 1, m):
                    D = fc[x] ^ fc[y]
                    LD = single_cycle_len(D)
                    if LD is None: continue
                    for z in range(m):
                        if z == x or z == y: continue
                        kk = path_len_of_intersection(D, fc[z])
                        if kk is None: continue
                        V.add(LD + len(fc[z]) - 2 * kk)
            Ve = sorted(v for v in V if v % 2 == 0)
            assert 8 in V, \
                (f"FALSIFIED(1): pair-residual tree with 8 not in value set "
                 f"V={sorted(V)} (n={nn}, edges={edges}, root={r})")
            assert Ve == list(range(Ve[0], Ve[-1] + 2, 2)), \
                (f"FALSIFIED(2): even value set has a gap: Ve={Ve} "
                 f"(n={nn}, edges={edges}, root={r})")
            vmin_census[Ve[0]] = vmin_census.get(Ve[0], 0) + 1
            vmax_census[Ve[-1]] = vmax_census.get(Ve[-1], 0) + 1

assert trees_seen > 10000, f"too few trees: {trees_seen}"
assert residual >= 20, f"too few residual trees sampled: {residual} — probe vacuous"
print(f"trees={trees_seen} residual={residual} "
      f"vmin_census={sorted(vmin_census.items())} "
      f"vmax_census={sorted(vmax_census.items())} "
      f"— every pair-residual tree: 8 in V, even values a step-2 interval")
CHECK -->

## Summary

Open computational conjecture with falsification probe: for every
pair-residual cubic DFS tree, the pasting value set
$V = \{|D| + \operatorname{gap}_3 + 1 - 2k'\}$ over legal (pair, third)
configs contains 8, and its even part is a gap-free step-2 interval. This
is the pigeonhole skeleton of the Q9 tuning argument: interval-ness plus
the endpoint bounds $v_{\min} \le 8 \le v_{\max}$ imply a firing triple.
Calibration: 53/53 residual trees over $n \le 22$ satisfy both, with the
interval widening as $n$ grows.
