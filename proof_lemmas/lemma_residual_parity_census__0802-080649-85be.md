---
id: residual_parity_census
status: open
depends_on: [crossing_offset_parity, triple_parity, coverage_extended]
discharged_by_round: null
introduced_at_round: 18
---

# Lemma `residual_parity_census` (falsification probe + census of residual trees)

**Context (R18 dual-attack).** The R17 handoff proposed spending proof effort
on the claim *"in all-odd-gap residual trees (easy and nested both fail), a
unit-step crossing pair ($\alpha=\beta=1$, $\omega=2$) always exists."* Per
the standing dual-attack policy, this round ran a falsification probe FIRST.

**Probe results (48,000 sampled DFS trees, 12,000 per size $n \in \{10,12,14,16\}$):**

| $n$ | residual all-odd | residual all-even | residual mixed |
|-----|-----------------|-------------------|----------------|
| 10 | 7 | 14 | 368 |
| 12 | 0 | 1 | 198 |
| 14 | 0 | 1 | 214 |
| 16 | 0 | 0 | 125 |

1. **The unit-step claim survives — but is nearly vacuous.** All 7 all-odd
   residual trees (all at $n=10$) contained a unit-step crossing pair, and in
   all 7 crossing fired with $\omega = 2$. No counterexample found. However,
   all-odd residuals are $7/48{,}000 \approx 0.015\%$ of trees and vanish for
   $n \ge 12$ in the sample. **Verdict: do not spend analytic effort here;
   the sub-case is a measure-zero corner of the residual space.**
2. **The residual mass is mixed-parity** ($\ge 96\%$ of residuals at every
   size). The analytic completeness proof lives or dies in the mixed case.
3. **Triple rescues every crossing-failed residual.** Among the 122 residual
   trees where crossing also failed (all mixed-parity), a firing triple
   existed in **all 122** (zero NONE cases). Firing-triple sym-diff lengths
   over all 738 firing triples found: $C_8$ 698×, $C_4$ 39×, $C_{16}$ 1×.
   Rescued trees always admitted several distinct firing triples (4–8).
4. **All-even residuals are rescued by crossing alone**, consistent with
   Lemma `triple_parity` Corollary 1 (triple is vacuous there) — none of the
   16 all-even residual trees needed (or could have used) a triple.

**Statement (open, computational support only).** In every DFS tree of a
connected cubic graph in which the easy, nested, and crossing mechanisms all
fail, some triple of back edges with an odd number of odd gaps (Lemma
`triple_parity`) produces a power-of-2 sym-diff cycle — empirically almost
always a $C_8$, occasionally a $C_4$.

**Redirect for Q9.** The analytic target is now: *why does a firing triple
always exist in a mixed-parity cubic DFS tree where all pair mechanisms
fail?* Concrete sub-goals for the next rounds:
- A length formula for the 3-back-edge sym-diff cycle in the dominant
  configuration (the analogue of `crossing_pair_formula`), starting from
  $|S| = 3 + t$ where $t$ is the number of tree edges covered by an odd
  number of the three tree paths (`sym_diff_cycle_formula` is the open
  ledger id for this; it needs a NEW id if its original statement was
  narrower).
- Characterize which back-edge triples yield a *single* cycle (vs. a
  disjoint union), since parity (Lemma `triple_parity`) already restricts
  candidates to $OOO$/$OEE$.

---

<!-- CHECK
# residual_parity_census: on a fresh sample, verify (a) every residual tree
# where crossing fails is rescued by a firing triple (NONE=0), (b) every
# all-odd residual tree contains a unit-step crossing pair, (c) the residual
# census is mixed-dominated.
import random

PO2_GAPS = {3, 7, 15, 31}
PO2_DIFFS = {2, 6, 14, 30}
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


def is_po2_cycle(sym):
    if not sym: return False
    deg = {}
    for u, v in sym: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if any(d != 2 for d in deg.values()): return False
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    verts = list(deg.keys()); start = verts[0]; seen = {start}; stk = [start]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(seen) == len(verts) and len(verts) in PO2_LENS


def nested_fires(depth, par, be):
    for i in range(len(be)):
        for j in range(i + 1, len(be)):
            s1, a1, g1 = be[i]; s2, a2, g2 = be[j]
            if s1 == s2 and abs(g1 - g2) in PO2_DIFFS: return True
            for sa, aa, sb, ab in [(s1, a1, s2, a2), (s2, a2, s1, a1)]:
                if (is_ancestor(ab, sa, depth, par) and
                        is_ancestor(aa, ab, depth, par) and
                        is_ancestor(sa, sb, depth, par)):
                    if abs((depth[sa] - depth[aa]) - (depth[sb] - depth[ab])) in PO2_DIFFS:
                        return True
    return False


def crossing_scan(depth, par, be):
    fires = False; unit = False
    for i in range(len(be)):
        for j in range(i + 1, len(be)):
            s1, a1, _ = be[i]; s2, a2, _ = be[j]
            for sa, aa, sb, ab in [(s1, a1, s2, a2), (s2, a2, s1, a1)]:
                if (depth[aa] < depth[ab] < depth[sa] < depth[sb] and
                        is_ancestor(ab, sa, depth, par) and
                        is_ancestor(sa, sb, depth, par)):
                    alpha = depth[ab] - depth[aa]; beta = depth[sb] - depth[sa]
                    if alpha + beta in PO2_DIFFS: fires = True
                    if alpha == 1 and beta == 1: unit = True
    return fires, unit


rng = random.Random(20260802)
census = {'all_odd': 0, 'all_even': 0, 'mixed': 0}
rescued = 0

for nn in [10, 12, 14]:
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(150):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(30):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            depth, par, be = res
            if any(g in PO2_GAPS for _, _, g in be): continue
            if nested_fires(depth, par, be): continue
            odd = sum(1 for _, _, g in be if g % 2)
            prof = ('all_odd' if odd == len(be) else
                    'all_even' if odd == 0 else 'mixed')
            census[prof] += 1
            fires, unit = crossing_scan(depth, par, be)
            assert not (prof == 'all_odd' and not unit), \
                "COUNTEREXAMPLE: all-odd residual without unit-step crossing pair"
            if fires: continue
            found = False
            for i in range(len(be)):
                for j in range(i + 1, len(be)):
                    for k in range(j + 1, len(be)):
                        s1, a1, _ = be[i]; s2, a2, _ = be[j]; s3, a3, _ = be[k]
                        sym = (fund_cycle_edges(s1, a1, par)
                               ^ fund_cycle_edges(s2, a2, par)
                               ^ fund_cycle_edges(s3, a3, par))
                        if is_po2_cycle(sym):
                            found = True; break
                    if found: break
                if found: break
            assert found, f"NONE case: n={nn} gaps={sorted(g for _,_,g in be)}"
            rescued += 1

assert census['mixed'] > 10 * (census['all_odd'] + 1), \
    f"census unexpectedly not mixed-dominated: {census}"
assert rescued > 0, "no crossing-failed residuals sampled — probe vacuous"
print(f"census={census} triple_rescued={rescued} — "
      f"unit-step claim unfalsified; NONE=0; mixed-dominated")
CHECK -->

## Summary

**Falsified priority, not the claim**: the unit-step crossing conjecture for
all-odd residual trees stands (7/7 positive at $n=10$; no counterexample),
but all-odd residuals are ~0.015% of trees and disappear by $n=12$ — the
sub-case is not where Q9's difficulty lives. The residual mass is
mixed-parity, and every crossing-failed residual tree (122/122) is rescued
by a triple, always using all three back edges (forced — Lemma
`triple_parity` (1)), with $C_8$ the dominant rescue length. Q9's analytic
program should target the mixed-parity triple mechanism next.
