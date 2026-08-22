---
id: t3_min_overlap_short_paste
status: open
depends_on: [pasting_value_interval, pasting_cover_dichotomy, pasting_vertex_automatic, triple_sym_diff_structure, fund_pair_overlap]
discharged_by_round: null
introduced_at_round: 27
---

# Lemma `t3_min_overlap_short_paste` (conjecture + probe: T3 via a min-overlap short-paste config)

**Setting.** As in `pasting_value_interval`. $T$ a DFS tree of a connected
cubic graph, pair-residual (no PO2 fundamental cycle, no pair with
single-PO2-cycle sym-diff). For a legal pasting config
$(B_1, B_2, B_3)$: $D = C_1 \triangle C_2$ a single cycle
($k_{12} = (|C_1|+|C_2|-|D|)/2 \ge 1$ overlap edges), $C_3$ meets $D$ in
a single path of $k' \ge 1$ edges, and the pasted cycle has length
$L = |D| + \operatorname{gap}_3 + 1 - 2k'$.

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual tree $T$ admits a legal pasting config with ALL of:

1. **min overlap**: $k' = 1$ — $C_3$ meets $D$ in a single edge, so
   $L = |D| + \operatorname{gap}_3 - 1$;
2. **short-paste criterion**: $\operatorname{gap}_3 \le k_{12} + 1$ — the
   FIRST sufficient pasting condition of `pasting_cover_dichotomy`, the
   one that needs no anchor/sender position information;
3. **tuned high and even**: $|D| + \operatorname{gap}_3 \ge 9$ odd, so
   $L \ge 8$ is even.

**Consequences.** (a) $v_{\max}(T) \ge 8$ — the T3 endpoint of the R23
tuning program holds per-tree, witnessed inside the provable-criterion
class; (b) $V_e(T) \not\subseteq \{6\}$ and $V_e(T) \ne \emptyset$ — the
per-tree meeting-existence question (R26 census killed the per-pair
version) is answered by the same config.

**Parity-family caveat (from calibration).** The odd-$|D|$ family
($|D|$ odd, $\operatorname{gap}_3$ even) realizes the config on 61 of 62
calibration residuals — but ONE residual tree required the even-$|D|$
family ($|D|$ even $\notin \{4,8,16,32\}$, $\operatorname{gap}_3$ odd).
An analytic proof of this lemma must therefore NOT assume $|D|$ odd;
the mixed-parity supply route (`mixed_overlap_supply`) alone cannot be
the whole story. This confirms the R26 handoff's suspicion that the
second family is load-bearing, not optional.

**Why this shape is the right analytic target.** With $k' = 1$ the
value formula degenerates to $L = |D| + \operatorname{gap}_3 - 1$ — no
overlap bookkeeping. With $\operatorname{gap}_3 \le k_{12}+1$ pasting is
guaranteed by the dichotomy's positional-free criterion, so a proof only
needs EXISTENCE of (pair, cover) with the arithmetic in (3), not any
anchor/sender analysis. Calibration minimal realizations concentrate on
$(\lvert D\rvert, \operatorname{gap}_3, k', k_{12})$ =
$(\text{odd} \ge 7,\, 2,\, 1,\, \ge 1)$ — a short back edge pasted on
one edge of a long odd $D$ — with $\operatorname{gap}_3 \in \{4, 5\}$
fallbacks on 7/62 trees (min-$\operatorname{gap}_3$ census 2:55, 4:5,
5:2). $\operatorname{gap}_3 = 2$ means $C_3$ is a triangle; since a
counterexample graph may be triangle-free, the analytic argument should
target the criterion class, not the triangle special case.

**Status.** Open. Calibration (standalone, 2026-08-07): 192k sampled DFS
trees over $n \in \{12,\dots,22\}$, 62 pair-residual trees — the joint
config exists on **62/62**; $V_e$ empty or $\subseteq \{6\}$ on **0**
trees. The CHECK below is the committed dual-attack probe: an assertion
failure exhibits a pair-residual tree where the joint (min-overlap,
short-paste, even $\ge 8$) route is unavailable, which would kill this
reduction and send T3 back to the anchor/sender criteria.

---

<!-- CHECK
# t3_min_overlap_short_paste: every pair-residual cubic DFS tree admits a
# legal pasting config with k'=1, gap3 <= k12+1, |D|+gap3 >= 9 odd
# (hence pasted length L = |D|+gap3-1 >= 8 even). Also assert V_e is
# never empty and never a subset of {6}.
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


rng = random.Random(20260807 + 27)
trees_seen = 0
residual = 0
joint_oddD = 0
joint_evenD_only = 0

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

            Ve = set()
            joint = []   # (LD, g3) of realizations with k'=1, short, L>=8 even
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
                        L = LD + g3 + 1 - 2 * kk
                        if L % 2 == 0:
                            Ve.add(L)
                            if kk == 1 and g3 <= k12 + 1 and L >= 8:
                                joint.append((LD, g3))
            assert Ve, \
                (f"FALSIFIED(meeting): pair-residual tree with EMPTY V_e "
                 f"(n={nn}, edges={edges}, root={r})")
            assert not Ve <= {6}, \
                (f"FALSIFIED(T3-refined): V_e subset of {{6}}: Ve={sorted(Ve)} "
                 f"(n={nn}, edges={edges}, root={r})")
            assert joint, \
                (f"FALSIFIED(joint): no k'=1 short-paste even-L>=8 config; "
                 f"Ve={sorted(Ve)} (n={nn}, edges={edges}, root={r})")
            if any(LD % 2 == 1 for LD, g3 in joint):
                joint_oddD += 1
            else:
                joint_evenD_only += 1

assert trees_seen > 10000, f"too few trees: {trees_seen}"
assert residual >= 20, f"too few residual trees sampled: {residual} — probe vacuous"
print(f"trees={trees_seen} residual={residual} "
      f"joint_oddD={joint_oddD} joint_evenD_only={joint_evenD_only} "
      f"— every pair-residual tree admits a k'=1, gap3<=k12+1, even-L>=8 "
      f"pasting config")
CHECK -->

## Summary

Open computational conjecture with falsification probe, refining T3 of
the R23 tuning program: every pair-residual cubic DFS tree admits a
legal pasting config with $k'=1$ (min overlap),
$\operatorname{gap}_3 \le k_{12}+1$ (the position-free sufficient paste
criterion of `pasting_cover_dichotomy`), and $|D| + \operatorname{gap}_3
\ge 9$ odd — hence a pasted cycle of even length $\ge 8$, giving
$v_{\max}(T) \ge 8$ and non-empty $V_e(T) \not\subseteq \{6\}$ per-tree.
Calibration: 62/62 residual trees over 192k sampled DFS trees
($n \le 22$); the odd-$|D|$ family suffices on 61/62, and exactly one
tree requires the even-$|D|$/odd-$\operatorname{gap}_3$ family — so the
analytic proof must cover both parity families.
