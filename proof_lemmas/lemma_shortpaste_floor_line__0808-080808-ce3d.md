---
id: shortpaste_floor_line
status: proved
depends_on: [triple_sym_diff_structure, pasting_cover_dichotomy, tune8_short_paste]
discharged_by_round: null
introduced_at_round: 30
---

# Lemma `shortpaste_floor_line` (proved: parity, floor, and the exact-8 line for short-paste values)

**Setting.** $T$ a DFS tree of a connected cubic graph; $(B_1, B_2)$ a
pair with $D = C_1 \triangle C_2$ a single cycle; $B_3$ a third back
edge whose fundamental cycle $C_3$ meets $D$ in a single path $P$ of
$k' \ge 1$ edges; $g_3 := |C_3| - 1$ ($\operatorname{gap}_3$). The
pasted cycle $C_1 \triangle C_2 \triangle C_3 = D \triangle C_3$ has
length
$$L \;=\; |D| + |C_3| - 2k' \;=\; |D| + g_3 + 1 - 2k'.$$

**Claims (all proved below).**

1. **(Parity)** $L$ is even iff $g_3 \equiv |D| + 1 \pmod 2$: an odd
   $|D|$ forces even $g_3$, an even $|D|$ forces odd $g_3$.
2. **(Overlap bound)** $g_3 \ge k'$, and $g_3 \ge 2$.
3. **(Floor)** If $L$ is even and $k' \le |D| - 6$, then $L \ge 8$.
4. **(Line)** $L = 8$ iff $g_3 = 2k' + 7 - |D|$.

**Proofs.**

*1.* $L = |D| + g_3 + 1 - 2k' \equiv |D| + g_3 + 1 \pmod 2$; $L$ even
iff $|D| + g_3$ odd, i.e. $g_3 \equiv |D| + 1 \pmod 2$. $\square$

*2.* $P \subseteq C_3$ and $P$ is a path while $C_3$ is a cycle, so
$P \subsetneq C_3$ as edge sets, giving $k' = |P| < |C_3| = g_3 + 1$,
i.e. $g_3 \ge k'$. In a simple graph $|C_3| \ge 3$, so $g_3 \ge 2$.
$\square$

*3.* Suppose $L$ even, $k' \le |D| - 6$. Two cases on the parity of
$k'$ relative to $|D|$:
- $k' \equiv |D| \pmod 2$: by Claim 1, $g_3 \equiv |D| + 1 \not\equiv
  k' \pmod 2$, so $g_3 \ge k'$ (Claim 2) improves to $g_3 \ge k' + 1$.
  Then $L \ge |D| + (k'+1) + 1 - 2k' = |D| + 2 - k' \ge |D| + 2 -
  (|D| - 6) = 8$.
- $k' \not\equiv |D| \pmod 2$: then $k' \ne |D| - 6$ (which has the
  parity of $|D|$), so $k' \le |D| - 7$, and
  $L \ge |D| + k' + 1 - 2k' = |D| + 1 - k' \ge |D| + 1 - (|D|-7) = 8$.
$\square$

*4.* Immediate from $L = |D| + g_3 + 1 - 2k'$. $\square$

**Consequences for the Q9 program.**

- **(a) The undershoot region is confined**: even pasted values
  $L \in \{4, 6\}$ (present on 6/52 resp. 45/52 residual trees, R29
  census) require $k' \ge |D| - 5$ — near-maximal overlap. Any
  analytic construction that keeps $k' \le |D| - 6$ CANNOT undershoot
  8; min-attainment (R29 split, part iii) reduces to hitting the line.
- **(b) T3's arithmetic half is now free**: take ANY pair with
  $|D| \ge 6$ and ANY short cover with $k' = 1$, and suppose $L$ even.
  If $|D|$ is odd (so $|D| \ge 7$; odd values are never powers of two),
  Claim 1 gives $g_3$ even $\ge 2$, so
  $L = |D| + g_3 - 1 \ge |D| + 1 \ge 8$. If $|D|$ is even ($\ge 6$),
  $g_3$ is odd $\ge 3$, so $L \ge |D| + 2 \ge 8$. Hence
  `t3_min_overlap_short_paste` reduces to pure SUPPLY:
  *every pair-residual tree has a pair with $|D| \ge 6$ admitting a
  $k' = 1$ short cover* — no arithmetic left; only $|D| \in \{3, 5\}$
  pairs escape the argument. (Both parity families of R27 are covered
  uniformly — the lone even-$|D|$-family census tree is no longer a
  special case.)
- **(c) `tune8_short_paste` is EQUIVALENT to line-hitting**: exists a
  pair and short cover ($g_3 \le k_{12} + 1$) with
  $g_3 = 2k' + 7 - |D|$. With Claim 2's window
  $\max(2, k') \le g_3$, per-$|D|$ realizable $(k', g_3)$ lines:
  $|D| = 7$: $(1,2), (2,4), (3,6), \dots$; $|D| = 9$: $(2,2), (3,4),
  \dots$; $|D| = 6$: $(1,3), (2,5), \dots$; $|D| = 5$: $(1,4), (2,6),
  \dots$; $|D| = 3$: $(1,6), \dots$. Triangle-free graphs kill only
  the $g_3 = 2$ entries. The short criterion $g_3 \le k_{12}+1$
  couples each entry to a minimum pair overlap
  $k_{12} \ge 2k' + 6 - |D|$.

**Status.** Proved (elementary arithmetic + the two structural facts
$P \subsetneq C_3$ and $|C_3| \ge 3$). The CHECK below is a
formalization-consistency probe: it re-derives Claims 1–4 against every
short-paste config extracted by the census machinery on sampled trees,
guarding against a drift between the prose definitions and the
extraction code used by `tune8_short_paste` / `sweep_pair_exists`.

---

<!-- CHECK
# shortpaste_floor_line: consistency of the proved claims against the
# census extraction code. For every short-paste config on sampled DFS
# trees (no residual filter needed — the claims are unconditional):
#   P1  L even  <=>  g3 == |D|+1 (mod 2)
#   P2  g3 >= k'  and  g3 >= 2
#   P3  L even and k' <= |D|-6  =>  L >= 8
#   P4  L == 8  <=>  g3 == 2k' + 7 - |D|
import random

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

rng = random.Random(20260808 + 30)
configs = 0
line_hits = 0
for nn, trials in ((12, 1200), (14, 1200), (16, 1200)):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(trials):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        r = rnd.randrange(nn)
        shuffled = [list(adj[v]) for v in range(nn)]
        for v in range(nn): rnd.shuffle(shuffled[v])
        res = dfs_tree(nn, edges, r, shuffled)
        if res is None: continue
        depth, par, be = res
        m = len(be)
        fc = [fund_cycle_edges(s, a, par) for s, a, _ in be]
        for x in range(m):
            for y in range(x + 1, m):
                D = fc[x] ^ fc[y]
                LD = single_cycle_len(D)
                if LD is None: continue
                for z in range(m):
                    if z == x or z == y: continue
                    kk = path_len_of_intersection(D, fc[z])
                    if kk is None: continue
                    g3 = len(fc[z]) - 1
                    L = LD + g3 + 1 - 2 * kk
                    configs += 1
                    assert (L % 2 == 0) == (g3 % 2 == (LD + 1) % 2), \
                        f"P1 parity fails: |D|={LD} g3={g3} k'={kk} L={L}"
                    assert g3 >= kk and g3 >= 2, \
                        f"P2 overlap bound fails: |D|={LD} g3={g3} k'={kk}"
                    if L % 2 == 0 and kk <= LD - 6:
                        assert L >= 8, \
                            f"P3 floor fails: |D|={LD} g3={g3} k'={kk} L={L}"
                    assert (L == 8) == (g3 == 2 * kk + 7 - LD), \
                        f"P4 line fails: |D|={LD} g3={g3} k'={kk} L={L}"
                    if L == 8: line_hits += 1

assert configs > 5000, f"too few configs checked: {configs} — probe vacuous"
assert line_hits > 50, f"too few L=8 configs seen: {line_hits}"
print(f"configs={configs} line_hits={line_hits} — parity/overlap/floor/line "
      f"claims consistent with the census extraction code")
CHECK -->

## Summary

Proved arithmetic backbone for the Q9 tuning program: pasted length
$L = |D| + g_3 + 1 - 2k'$ satisfies (parity) even $L$ forces
$g_3 \equiv |D|+1 \bmod 2$; (overlap) $g_3 \ge \max(k', 2)$; (floor)
even-$L$ configs with $k' \le |D| - 6$ never undershoot 8; (line)
$L = 8$ iff $g_3 = 2k' + 7 - |D|$. Consequences: the $L \in \{4,6\}$
undershoots require near-maximal overlap $k' \ge |D| - 5$;
`t3_min_overlap_short_paste` reduces to pure supply (any $k'=1$ short
cover of any pair with $|D| \ge 7$, or $|D| \ge 6$ even, gives even
$L \ge 8$); and `tune8_short_paste` is equivalent to hitting the
diophantine line with a short cover, with per-$|D|$ windows
$(k', g_3) = (k', 2k'+7-|D|)$, $g_3 \ge \max(2, k'+1)$ [parity-adjusted],
coupled to pair overlap via $k_{12} \ge g_3 - 1 = 2k' + 6 - |D|$.
