---
id: pasting_rescue_census
status: open
depends_on: [triple_sym_diff_structure, triple_parity]
discharged_by_round: null
introduced_at_round: 19
---

# Lemma `pasting_rescue_census` (conjecture + falsification probe: pasting rescues every pair-residual tree)

**Setting.** As in `triple_sym_diff_structure`. Call a DFS tree $T$ of a
cubic graph **pair-residual** if (i) no fundamental cycle has power-of-2
length (easy mechanism fails), and (ii) no pair of back edges has
$C_i \triangle C_j$ equal to a single simple cycle of power-of-2 length
(all pair mechanisms — nested, crossing, same-vertex, and any branching
pair configuration — fail). This is mechanism-agnostic and strictly
contains the R18 "crossing-failed residual" class.

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual DFS tree of a connected cubic graph admits

1. a triple of back edges whose sym-diff $S$ is a single simple cycle of
   power-of-2 length (taxonomy completeness at radius 3), and moreover
2. a firing triple that **factors through the pasting criterion** of
   `triple_sym_diff_structure`(5): some pair of the triple has
   single-cycle sym-diff $D$ with $D \cap C_3$ a single path of length
   $k \ge 1$ (so $|S| = |D| + \operatorname{gap}_3 + 1 - 2k$).

**Status.** Open. The CHECK below is a falsification probe (dual-attack
standing policy): an assertion failure exhibits a concrete pair-residual
tree with no firing triple (falsifying 4-mechanism completeness) or one
whose every firing triple evades pasting (falsifying pasting
exhaustiveness). It also prints a census of the rescuing configuration's
shape — pair parity class (mixed vs same), $|D|$, $\operatorname{gap}_3$,
$k$ — which is the empirical input for the R20+ analytic existence
argument.

**Why the claim is plausible.** R18's census: 122/122 crossing-failed
residual trees were triple-rescued. R19's census: 2604/2604 sampled firing
triples factor through pasting. `triple_sym_diff_structure`(6) explains
the parity bookkeeping: mixed pairs give odd $|D|$, and an even-gap third
back edge corrects the parity; the free parameters
$(\operatorname{gap}_3, k)$ give the length room to hit $8$.

---

<!-- CHECK
# pasting_rescue_census: find pair-residual cubic DFS trees; assert each
# admits a firing triple AND a firing triple that factors through pasting.
# Census the rescuing configuration shapes.
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


rng = random.Random(20260803 + 20)
trees_seen = 0
residual = 0
residual_parity = {"mixed": 0, "all_even": 0, "all_odd": 0}
shape_census = {}   # (pair_parity, gap3_parity, L) -> count
k_census = {}

for nn in (12, 14, 16):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(5000):
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
            gaps = [g for _, _, g in be]
            # easy mechanism: any PO2 fundamental cycle?
            if any(len(c) in PO2_LENS for c in fc): continue
            # any pair mechanism (mechanism-agnostic): single PO2 pair sym-diff?
            pair_fires = False
            for i in range(m):
                for j in range(i + 1, m):
                    if single_cycle_len(fc[i] ^ fc[j]) in PO2_LENS:
                        pair_fires = True; break
                if pair_fires: break
            if pair_fires: continue
            residual += 1
            odd = sum(1 for g in gaps if g % 2 == 1)
            cls = "mixed" if 0 < odd < m else ("all_odd" if odd == m else "all_even")
            residual_parity[cls] += 1
            # search firing triples + pasting factorization
            found_firing = False
            found_pasting = False
            for i in range(m):
                for j in range(i + 1, m):
                    for k3 in range(j + 1, m):
                        sym = fc[i] ^ fc[j] ^ fc[k3]
                        L = single_cycle_len(sym)
                        if L not in PO2_LENS: continue
                        found_firing = True
                        for (x, y, z) in ((i, j, k3), (i, k3, j), (j, k3, i)):
                            D = fc[x] ^ fc[y]
                            LD = single_cycle_len(D)
                            if LD is None: continue
                            kk = path_len_of_intersection(D, fc[z])
                            if kk is None: continue
                            assert L == LD + len(fc[z]) - 2 * kk
                            if not found_pasting:
                                pp = ("mixed_pair"
                                      if (gaps[x] % 2) != (gaps[y] % 2)
                                      else "same_pair")
                                g3p = "odd_g3" if gaps[z] % 2 else "even_g3"
                                key = (pp, g3p, L)
                                shape_census[key] = shape_census.get(key, 0) + 1
                                k_census[kk] = k_census.get(kk, 0) + 1
                            found_pasting = True
            assert found_firing, \
                (f"FALSIFIED(1): pair-residual tree with NO firing triple "
                 f"(n={nn}, edges={edges}, root={r})")
            assert found_pasting, \
                (f"FALSIFIED(2): firing triples exist but none factors "
                 f"through pasting (n={nn}, edges={edges}, root={r})")

assert trees_seen > 10000, f"too few trees: {trees_seen}"
assert residual >= 15, f"too few residual trees sampled: {residual} — probe vacuous"
print(f"trees={trees_seen} residual={residual} parity={residual_parity} "
      f"shapes={sorted(shape_census.items())} k_census={sorted(k_census.items())} "
      f"— every pair-residual tree pasting-rescued")
CHECK -->

## Summary

Open computational conjecture with falsification probe: every pair-residual
cubic DFS tree (no PO2 fundamental cycle, no single-PO2-cycle pair
sym-diff of ANY configuration) admits a firing triple, and one that
factors through the `triple_sym_diff_structure` pasting criterion. The
probe would exhibit a concrete counterexample tree on failure; on success
it prints the shape census (pair parity, third-gap parity, cycle length,
overlap $k$) that the analytic existence argument must reproduce.
