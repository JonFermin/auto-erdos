---
id: tune8_short_paste
status: open
depends_on: [t3_min_overlap_short_paste, pasting_value_interval, pasting_cover_dichotomy, pasting_vertex_automatic, triple_sym_diff_structure, fund_pair_overlap]
discharged_by_round: null
introduced_at_round: 28
---

# Lemma `tune8_short_paste` (conjecture + probe: direct tuning to 8 inside the short-paste class)

**Setting.** As in `t3_min_overlap_short_paste`: $T$ a pair-residual DFS
tree of a connected cubic graph; legal pasting configs $(B_1,B_2,B_3)$
with $D = C_1 \triangle C_2$ a single cycle ($k_{12} \ge 1$), $C_3$
meeting $D$ in a single path of $k' \ge 1$ edges, pasted length
$L = |D| + \operatorname{gap}_3 + 1 - 2k'$.

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual tree $T$ admits a legal pasting config with BOTH:

1. **short-paste criterion**: $\operatorname{gap}_3 \le k_{12} + 1$
   (pasting guaranteed position-free, by `pasting_cover_dichotomy`);
2. **exact tuning**: $|D| + \operatorname{gap}_3 + 1 - 2k' = 8$,
   equivalently $|D| + \operatorname{gap}_3 = 7 + 2k'$.

**Consequence.** $8 \in V(T)$ **directly**: the pasted triple cycle
$C_1 \triangle C_2 \triangle C_3$ is a $C_8$ of $G$. This subsumes the
entire R23 pigeonhole program for Q9's tuning half — T1 (interval-ness)
and the endpoint bounds T2/T3 become unnecessary for existence; they
remain as a fallback route should this claim be falsified at larger $n$.

**k' caveat (from calibration).** Restricting additionally to $k' = 1$
FAILS on 3 of 51 calibration residuals — unlike the T3-side lemma, exact
tuning needs the $k'$ freedom (the analytic argument must not fix
$k' = 1$; observed $k'$ in minimal $L=8$ realizations spans $1..4$).

**Status.** Open. Calibration (standalone, 2026-08-07, seed
20260807+28): 192k sampled DFS trees over $n \in \{12,\dots,22\}$, 51
pair-residual trees — the joint config exists on **51/51**; min
$\operatorname{gap}_3$ over a tree's $L=8$ realizations is 2 on 45/51
and 4 on 6/51. The CHECK below is the committed dual-attack probe: an
assertion failure exhibits a pair-residual tree where exact tuning
escapes the short-paste class, reactivating the T1/T2/T3 route.

---

<!-- CHECK
# tune8_short_paste: every pair-residual cubic DFS tree admits a legal
# pasting config with gap3 <= k12+1 and |D| + gap3 + 1 - 2k' == 8 — a
# position-free short-paste config whose pasted triple cycle is a C_8.
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


rng = random.Random(20260807 + 28)
trees_seen = 0
residual = 0
k1_suffices = 0
needs_k_ge2 = 0

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

            hits = []   # k' of short-paste configs with L == 8
            for x in range(m):
                for y in range(x + 1, m):
                    D = fc[x] ^ fc[y]
                    LD = single_cycle_len(D)
                    if LD is None: continue
                    k12 = (len(fc[x]) + len(fc[y]) - LD) // 2
                    for z in range(m):
                        if z == x or z == y: continue
                        kk = path_len_of_intersection(D, fc[z])
                        if kk is None: continue
                        g3 = len(fc[z]) - 1
                        if g3 <= k12 + 1 and LD + g3 + 1 - 2 * kk == 8:
                            hits.append(kk)
            assert hits, \
                (f"FALSIFIED: pair-residual tree with NO short-paste config "
                 f"tuned to 8 (n={nn}, edges={edges}, root={r})")
            if 1 in hits: k1_suffices += 1
            else: needs_k_ge2 += 1

assert trees_seen > 10000, f"too few trees: {trees_seen}"
assert residual >= 20, f"too few residual trees sampled: {residual} — probe vacuous"
print(f"trees={trees_seen} residual={residual} "
      f"k1_suffices={k1_suffices} needs_k_ge2={needs_k_ge2} "
      f"— every pair-residual tree has a short-paste config with pasted "
      f"length exactly 8")
CHECK -->

## Summary

Open computational conjecture with falsification probe, collapsing the
R23 pigeonhole program: every pair-residual cubic DFS tree admits a
legal pasting config with $\operatorname{gap}_3 \le k_{12}+1$ (pasting
guaranteed position-free by `pasting_cover_dichotomy`) whose pasted
triple cycle has length exactly 8 — so $8 \in V(T)$ directly, no
interval-ness or endpoint bounds needed. Calibration: 51/51 residual
trees over 192k sampled DFS trees ($n \le 22$); fixing $k' = 1$ fails
on 3/51, so the analytic argument must keep the $k'$ freedom.
