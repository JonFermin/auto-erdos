---
id: crossing_offset_parity
status: proved
depends_on: [crossing_pair_formula]
discharged_by_round: 17
introduced_at_round: 17
---

# Lemma `crossing_offset_parity` (parity constraint on crossing mechanism)

**Statement.** Let $T$ be a DFS spanning tree of a graph $G$ and let
$B_1=(s_1,a_1)$ and $B_2=(s_2,a_2)$ be two back edges in strict crossing
order
$$d(a_1) < d(a_2) < d(s_1) < d(s_2).$$
Define the crossing offset
$$\omega = (d(a_2)-d(a_1)) + (d(s_2)-d(s_1)).$$
Then
$$\omega \;\equiv\; \operatorname{gap}(B_1) + \operatorname{gap}(B_2) \pmod{2},$$
where $\operatorname{gap}(B_i) = d(s_i) - d(a_i)$.

**Corollary 1 (crossing parity).** The crossing mechanism (sym-diff of
$B_1$ and $B_2$) produces a power-of-2 cycle only when
$\omega \in \{2,6,14,30,\ldots\}$ (all even). Therefore:

- If $\operatorname{gap}(B_1)$ and $\operatorname{gap}(B_2)$ have **opposite parity**
  (one odd, one even), then $\omega$ is **odd**, so $\omega \notin
  \{2,6,14,30,\ldots\}$, and the crossing mechanism **cannot fire** for
  this pair.

- If both gaps are **even**, then $\omega$ is **even** — crossing can fire.

- If both gaps are **odd**, then $\omega$ is **even** — crossing can fire.

**Corollary 2 (all-odd-gaps structural simplification).** If every
back-edge in $T$ has odd depth-gap, then every crossing offset is even.
The crossing mechanism will fire (for some pair) iff some crossing pair
has $\omega \in \{2,6,14,30,\ldots\}$.

**Corollary 3 (mixed-parity partition).** Partition back edges into
$E$ (even gap) and $O$ (odd gap). The crossing mechanism can only fire
from $E$-$E$ or $O$-$O$ crossing pairs; mixed $E$-$O$ pairs
produce odd offset and are useless for crossing.

## Proof

Let $\alpha = d(a_2)-d(a_1) \ge 1$, $\beta = d(s_2)-d(s_1) \ge 1$,
and $\gamma = d(s_1)-d(a_2) \ge 1$ (the "inner" depth separation of $B_1$
inside $B_2$'s anchor). Then:

$$\operatorname{gap}(B_1) = d(s_1) - d(a_1) = \alpha + \gamma,$$
$$\operatorname{gap}(B_2) = d(s_2) - d(a_2) = \beta + \gamma.$$

Therefore:
$$\operatorname{gap}(B_1) + \operatorname{gap}(B_2) = \alpha + \beta + 2\gamma = \omega + 2\gamma.$$

Since $2\gamma$ is even:
$$\omega \equiv \operatorname{gap}(B_1) + \operatorname{gap}(B_2) \pmod{2}. \qquad \square$$

## Additional parity analysis: all-even-gaps case

If every back-edge gap is even, we can write each gap as $2g_i$. Then:
- $\alpha = d(a_2)-d(a_1)$ and $\beta = d(s_2)-d(s_1)$ can be arbitrary
  positive integers (not constrained to be even).
- So crossing offsets $\omega = \alpha + \beta$ can be ANY integer $\ge 2$.
  Even offsets can fire; odd offsets cannot.

For the leaf-pair mechanism in the all-even case: the leaf $L$ has two
back edges with gaps $\delta_1 > \delta_2$, both even. Their difference
$\delta_1 - \delta_2$ is also even. The leaf-pair mechanism fires iff
$\delta_1 - \delta_2 \in \{2,6,14,30,\ldots\}$ (all even). So it can
fire.

## Combined parity classification

| Gap parity class | Easy fires? | Nested/leaf-pair offset parity | Crossing offset parity |
|---|---|---|---|
| All odd, some ∈ PO2\_GAPS | Yes (easy) | — | — |
| All odd, none ∈ PO2\_GAPS | No | Even (odd−odd) | Even |
| All even, some ∈ PO2\_GAPS | No (all even ≢ 3 mod 4) | Even (even−even) | Even or odd |
| All even, none ∈ PO2\_GAPS | No | Even | Even or odd |
| Mixed: some odd, some even | If odd gap ∈ PO2\_GAPS | Mixed (even or odd) | Even (same-parity pairs), odd (mixed pairs) |

*Note*: PO2\_GAPS = $\{3,7,15,31,\ldots\}$ are all $\equiv 3 \pmod{4}$,
hence all **odd**. So if all gaps are even, the easy mechanism never fires.

**The hardest case**: all gaps even and none equal to $2^k-1$. In this
case, easy fails, leaf-pair differences are even (may or may not hit
PO2\_DIFFS), crossing offsets have both parities (even and odd), and the
parity constraint doesn't reduce the search space much.

## Analytic consequence for the all-odd-gaps sub-case

From Corollary 2, the all-odd-gaps sub-case with easy failing reduces to:
1. **Leaf-pair**: does some leaf have $\delta_1 - \delta_2 \in
   \{2,6,14,\ldots\}$? (Both $\delta_1,\delta_2$ odd → difference even; can be
   in PO2\_DIFFS.)
2. **Crossing**: does some same-parity crossing pair have $\omega \in
   \{2,6,14,\ldots\}$? (All crossing offsets are even.)
3. **Triple**: does some triple of back edges give a po2 sym-diff cycle?

The crossing mechanism is particularly tractable in this sub-case because
all crossing offsets are even; we need even values in $\{2,6,14,\ldots\}$.

**Minimum crossing offset**: The minimum possible crossing offset is
$\omega = \alpha + \beta \ge 1 + 1 = 2$. The value $\omega = 2$ is in
PO2\_DIFFS (it gives a $C_4$). So if ANY crossing pair exists with
$\alpha = \beta = 1$ (anchor-adjacent: $d(a_2) = d(a_1)+1$, and
sender-adjacent: $d(s_2) = d(s_1)+1$), then crossing fires with a
$C_4$.

**Structural implication**: For crossing to fail entirely in the all-odd
case, every crossing pair must have $\omega \ge 4$ (the next even number)
AND $\omega \notin \{6,14,30,\ldots\}$ for the pairs where $\omega \ge 4$.

<!-- CHECK
# crossing_offset_parity: verify parity formula omega ≡ gap1+gap2 (mod 2)
# and that opposite-parity crossing pairs always give odd omega (never in PO2_DIFFS).
import random

rng = random.Random(20260801 + 17)
PO2_DIFFS = {2, 6, 14, 30, 62}

violations = 0
total_crossing_pairs = 0
opposite_parity_po2_violations = 0


def make_adj(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    return adj


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


def compute_dfs(n, edges, adj, root, rnd):
    depth = [-1] * n; parent = [-1] * n
    tree_set = set()
    seen = [False] * n; seen[root] = True; depth[root] = 0
    def nbrs(u): ns = adj[u][:]; rnd.shuffle(ns); return ns
    stack = [(root, iter(nbrs(root)))]
    while stack:
        u, it = stack[-1]; adv = False
        for w in it:
            if not seen[w]:
                seen[w] = True; depth[w] = depth[u] + 1; parent[w] = u
                tree_set.add((min(u,w), max(u,w)))
                stack.append((w, iter(nbrs(w)))); adv = True; break
        if not adv: stack.pop()
    nontree = []
    for u, v in edges:
        if (min(u,v), max(u,v)) not in tree_set:
            if depth[u] > depth[v]:
                nontree.append((u, v, depth[u]-depth[v]))
            else:
                nontree.append((v, u, depth[v]-depth[u]))
    return depth, parent, nontree


def is_ancestor(u, v, depth, par):
    if depth[u] > depth[v]: return False
    x = v
    while depth[x] > depth[u]: x = par[x]
    return x == u


for nn in [10, 12, 14]:
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(20):
        edges = sample_cubic(nn, rnd)
        if edges is None: continue
        adj = make_adj(nn, edges)
        for root in range(min(3, nn)):
            depth, parent, nontree = compute_dfs(nn, edges, adj, root, rnd)
            be = list(nontree)

            for i in range(len(be)):
                for j in range(i+1, len(be)):
                    s1, a1, g1 = be[i]; s2, a2, g2 = be[j]
                    # Check both orientations for crossing
                    for sa, aa, sb, ab, ga, gb in [(s1,a1,s2,a2,g1,g2),(s2,a2,s1,a1,g2,g1)]:
                        if (depth[aa] < depth[ab] < depth[sa] < depth[sb] and
                                is_ancestor(ab, sa, depth, parent) and
                                is_ancestor(sa, sb, depth, parent)):
                            # This is a valid crossing pair with (sa,aa) as B1, (sb,ab) as B2
                            alpha = depth[ab] - depth[aa]
                            beta  = depth[sb] - depth[sa]
                            gamma = depth[sa] - depth[ab]
                            omega = alpha + beta
                            total_crossing_pairs += 1

                            # Verify parity formula
                            expected_parity = (ga + gb) % 2
                            actual_parity   = omega % 2
                            if expected_parity != actual_parity:
                                violations += 1
                                print(f"PARITY VIOLATION: n={nn} gaps={ga},{gb} omega={omega}")

                            # Verify: opposite-parity pairs never give omega in PO2_DIFFS
                            if ga % 2 != gb % 2:  # opposite parity
                                if omega in PO2_DIFFS:
                                    opposite_parity_po2_violations += 1
                                    print(f"OPPOSITE-PARITY HITS PO2_DIFFS: omega={omega} gaps={ga},{gb}")

assert violations == 0, f"Parity formula violated {violations} times"
assert opposite_parity_po2_violations == 0, \
    f"Opposite-parity crossing pair hit PO2_DIFFS {opposite_parity_po2_violations} times"

print(f"Total crossing pairs checked: {total_crossing_pairs}")
print(f"Parity violations: {violations} (expected 0)")
print(f"Opposite-parity crossing PO2_DIFFS hits: {opposite_parity_po2_violations} (expected 0)")
print("crossing_offset_parity: all checks passed.")
CHECK -->

## Summary

**Proved**: For any crossing pair of back edges in a DFS tree, the
crossing offset $\omega = (d(a_2)-d(a_1)) + (d(s_2)-d(s_1))$ satisfies
$\omega \equiv \operatorname{gap}(B_1) + \operatorname{gap}(B_2) \pmod{2}$.

**Consequence**: The crossing mechanism never fires from opposite-parity
gap pairs. The parity-partition $\{E, O\}$ of back edges restricts
crossing to $E$-$E$ and $O$-$O$ pairs. This is a structural constraint
that simplifies the analysis of when crossing fails.

**Open**: Show that in all-odd-gaps cubic DFS trees where easy + leaf-pair
fail, some $O$-$O$ crossing pair achieves $\omega \in \{2,6,14,\ldots\}$.
The minimum achievable $\omega$ is 2 (unit-step crossing pair), which IS
in PO2\_DIFFS. The difficulty is showing such a unit-step pair must exist
in the residual cases.
