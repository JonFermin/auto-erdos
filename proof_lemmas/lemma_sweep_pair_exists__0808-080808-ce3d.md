---
id: sweep_pair_exists
status: open
depends_on: [tune8_short_paste, t3_min_overlap_short_paste, pasting_cover_dichotomy, pasting_vertex_automatic]
discharged_by_round: null
introduced_at_round: 29
---

# Lemma `sweep_pair_exists` (conjecture + probe: one pair's even value set is an interval containing 8)

**Setting.** As in `tune8_short_paste`: $T$ a pair-residual DFS tree of
a connected cubic graph. For a fixed pair $(B_1, B_2)$ with
$D = C_1 \triangle C_2$ a single cycle (overlap $k_{12} \ge 1$), the
**short-paste value set of the pair** is
$$S_p(T) = \{\, |D| + \operatorname{gap}_3 + 1 - 2k' \;:\; B_3 \text{ with }
\operatorname{gap}_3 \le k_{12}+1,\ D \cap C_3 \text{ a single path of }
k' \ge 1 \text{ edges} \,\},$$
and $E_p(T) = S_p(T) \cap 2\mathbb{Z}$ its even part.

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual tree $T$ admits a pair $p$ such that $E_p(T)$ is a
nonempty step-2 interval (no even gaps between its min and max) and
$8 \in E_p(T)$.

**Why this refines `tune8_short_paste`.** The R29 pre-census killed
every tree-level sweep route: the even part of the UNION
$\bigcup_p S_p(T)$ has gaps on 4/52 residual trees (e.g. $\{6,8,10,14\}$
missing 12), descent ($v \ge 10 \Rightarrow v-2$ present) fails on 3/52,
and the max-$k_{12}$ pair misses 8 on 22/52. The surviving structure is
*per-pair*: one pair's own even set sweeps an interval through 8. The
analytic burden localizes to (i) a selection rule for the pair, (ii)
interval-ness of that pair's cover-value sweep, (iii) endpoint bounds
$\min E_p \le 8 \le \max E_p$.

**Selection-rule negatives (R29 census, 52 residual trees).** The pair
of minimum $|D|$ works only 31/52; the pair of minimum
$\min E_p$ only 29/52; max-$k_{12}$ 30/52. Per-pair interval-ness is not
automatic: 84/637 pairs with even values have a gapped even set, and the
observed failures are exactly the $8$-skipping pattern
$E_p = \{6, 10\}$ ($|D| = 7$, $k_{12} \in \{4,5\}$: covers with
$\operatorname{gap}_3 = 2k'-2$ and $2k'+2$ exist but none with
$\operatorname{gap}_3 = 2k'$). In the widest sweep pair, 8 is an
ENDPOINT on 41/52 trees (typically the minimum) — so the analytic
target is min-attainment ($\min E_p = 8$ with $\max E_p \ge 8$), not a
mid-interval pigeonhole.

**Status.** Open. The CHECK below is the committed dual-attack probe:
an assertion failure exhibits a pair-residual tree where NO single pair
has an even-interval value set containing 8, sending the analytic
program back to the union-level `tune8_short_paste` statement.

---

<!-- CHECK
# sweep_pair_exists: every pair-residual cubic DFS tree has a pair
# (single-cycle D, overlap k12) whose short-paste even value set
# E_p = { |D|+gap3+1-2k' even : gap3 <= k12+1, D∩C3 single path k' }
# is a step-2 interval containing 8.
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


rng = random.Random(20260808 + 29)
trees_seen = 0
residual = 0
eight_is_min = 0
eight_interior_or_max = 0

for nn, trials in ((12, 4000), (14, 4000), (16, 4000),
                   (18, 2500), (20, 2500), (22, 2000)):
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

            best = None   # (lo, hi) of a witnessing sweep pair
            for x in range(m):
                if best: break
                for y in range(x + 1, m):
                    D = fc[x] ^ fc[y]
                    LD = single_cycle_len(D)
                    if LD is None: continue
                    k12 = (len(fc[x]) + len(fc[y]) - LD) // 2
                    vals = set()
                    for z in range(m):
                        if z == x or z == y: continue
                        kk = path_len_of_intersection(D, fc[z])
                        if kk is None: continue
                        g3 = len(fc[z]) - 1
                        if g3 <= k12 + 1:
                            vals.add(LD + g3 + 1 - 2 * kk)
                    ev = sorted(v for v in vals if v % 2 == 0)
                    if not ev or 8 not in vals: continue
                    lo, hi = ev[0], ev[-1]
                    if all(v in vals for v in range(lo, hi + 1, 2)):
                        best = (lo, hi); break
            assert best, \
                (f"FALSIFIED: pair-residual tree where NO pair has an "
                 f"even-interval short-paste value set containing 8 "
                 f"(n={nn}, edges={edges}, root={r})")
            if best[0] == 8: eight_is_min += 1
            else: eight_interior_or_max += 1

assert trees_seen > 10000, f"too few trees: {trees_seen}"
assert residual >= 20, f"too few residual trees sampled: {residual} — probe vacuous"
print(f"trees={trees_seen} residual={residual} "
      f"eight_is_min={eight_is_min} eight_interior_or_max={eight_interior_or_max} "
      f"— every pair-residual tree has a single pair whose even "
      f"short-paste value set is a step-2 interval containing 8")
CHECK -->

## Summary

Open computational conjecture with falsification probe, localizing the
`tune8_short_paste` analytic burden to a single pair: every
pair-residual cubic DFS tree admits a pair (single-cycle $D$, overlap
$k_{12}$) whose short-paste even value set is a step-2 interval
containing 8. R29 census (192k trees, 52 residuals): holds 52/52, while
every tree-level route is dead — union-of-pairs interval-ness fails
4/52, descent fails 3/52, max-$k_{12}$ selection misses 22/52, min-$|D|$
misses 21/52. 8 is typically the interval's MINIMUM (41/52), so the
analytic target is min-attainment plus per-pair interval-ness, and the
known per-pair failure mode is the $E_p = \{6,10\}$ gap
($\operatorname{gap}_3 \equiv 2k' \pmod 4$ classes both present at
$|D|=7$ but the middle class missing).
