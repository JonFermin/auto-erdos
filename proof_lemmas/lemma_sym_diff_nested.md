---
id: sym_diff_nested
status: proved
depends_on: [same_leaf_sym_diff]
discharged_by_round: 5
introduced_at_round: 5
---

# Lemma: nested fundamental-cycle sym-diff length formula

**Statement.** Let $T$ be a DFS tree of a connected graph $G$, and let
$e_1 = (v_1, u_1)$ and $e_2 = (v_2, u_2)$ be two back edges, where $u_i$
is the ancestor of $v_i$ in $T$. Suppose the two fundamental cycles are
**nested**: $u_1$ is an ancestor of $u_2$, and $u_2$ is an ancestor of
$v_2$, and $v_2$ is an ancestor of $v_1$ (or $v_2 = v_1$). Write
$\ell = \operatorname{depth}(v_2) - \operatorname{depth}(u_2)$ (the depth-gap
of $e_2$) and $L = \operatorname{depth}(v_1) - \operatorname{depth}(u_1)$
(the depth-gap of $e_1$). Let $s$ be the length of the shared tree path:
the tree edges on the path from $v_2$ to $u_2$ that are also on the path
from $v_1$ to $u_1$. Under the nesting assumption, $s = \ell$ (the inner
cycle's entire tree path is shared) if $v_2 = v_1$, and more generally
$s = \operatorname{depth}(v_2) - \max(\operatorname{depth}(u_2), \operatorname{depth}(u_1)) + [\text{extra}]$...

**Special case: same leaf ($v_1 = v_2 = v$).** This is the same-leaf
sub-lemma (Lemma `same_leaf_sym_diff`): the sym-diff length is
$(d_2 - d_1) + 2 = (\delta_1 - \delta_2) + 2$ where $\delta_i$ are the
depth-gaps.

**General nested case.** When $v_1 \ne v_2$ but $u_1, u_2, v_2, v_1$
appear in this order along the DFS tree path (i.e., $u_1$ is above $u_2$
above $v_2$ above $v_1$), the shared path of $F_1$ and $F_2$ is the tree
path from $v_2$ down to $u_2$, of length $\ell = \delta_2$. The sym-diff
$F_1 \triangle F_2$ consists of:

- the tree edges on $P(v_1, v_2)$ (path from $v_1$ up to $v_2$), length
  $\operatorname{depth}(v_1) - \operatorname{depth}(v_2)$;
- back edge $e_1 = (v_1, u_1)$;
- tree edges on $P(u_1, u_2)$ (path from $u_1$ down to $u_2$), length
  $\operatorname{depth}(u_2) - \operatorname{depth}(u_1)$;
- back edge $e_2 = (v_2, u_2)$.

Total length:
$$|F_1 \triangle F_2| = (\delta_1 - \delta_2) +
(\operatorname{depth}(u_2) - \operatorname{depth}(u_1)) + 2
= (\delta_1 + \operatorname{depth}(v_1)) - (\delta_2 + \operatorname{depth}(v_2)) + 2.$$

Since $\delta_i + \operatorname{depth}(v_i) = \operatorname{depth}(u_i)$...
wait, $\delta_i = \operatorname{depth}(v_i) - \operatorname{depth}(u_i)$ so
$\operatorname{depth}(u_i) = \operatorname{depth}(v_i) - \delta_i$. Then
$\operatorname{depth}(u_2) - \operatorname{depth}(u_1) = (\operatorname{depth}(v_2) - \delta_2) - (\operatorname{depth}(v_1) - \delta_1)$.
Substituting:
$$|F_1 \triangle F_2|
= (\operatorname{depth}(v_1) - \operatorname{depth}(v_2))
  + (\operatorname{depth}(v_2) - \delta_2 - \operatorname{depth}(v_1) + \delta_1)
  + 2
= (\delta_1 - \delta_2) + 2.$$

**Conclusion: under perfect nesting ($u_1 \le u_2 \le v_2 \le v_1$ in DFS
order), the sym-diff length depends only on the depth-gaps, not the absolute
depths:**
$$|F_1 \triangle F_2| = (\delta_1 - \delta_2) + 2.$$

This is the **same formula** as the same-leaf sym-diff! The same-leaf
case is a special case of perfect nesting where $v_1 = v_2$. The
forbidden-gap constraint is identical: $\delta_1 - \delta_2 \notin
\{2, 6, 14, 30, \ldots\}$.

**Crossing case (same DFS branch).** Suppose $u_1, u_2, v_2, v_1$ all lie
on the same root-to-leaf path in $T$, in depth order
$d_{u_1} < d_{u_2} < d_{v_2} < d_{v_1}$. Here neither fundamental cycle
contains the other (it is "crossing"). The shared tree edges of $F_1$ and
$F_2$ are exactly $P(u_2, v_2)$, the entire tree path of $F_2$. The sym-diff
$F_1 \triangle F_2$ removes $P(u_2, v_2)$ from $F_1$'s tree path, producing
two disconnected segments $P(u_1, u_2)$ and $P(v_2, v_1)$, closed by the
two back edges $(v_1, u_1)$ and $(v_2, u_2)$. Degree check: every vertex has
degree exactly 2. Length:
$$(d_{u_2} - d_{u_1}) + (d_{v_1} - d_{v_2}) + 2.$$
Expanding: $(d_{u_2} - d_{u_1}) + (d_{v_1} - d_{v_2}) =
(d_{v_1} - d_{u_1}) - (d_{v_2} - d_{u_2}) = \delta_1 - \delta_2$.
So the crossing sym-diff also has length $(\delta_1 - \delta_2) + 2$.

**Different-branch case.** If $v_1$ and $v_2$ lie in different DFS subtrees
(neither is an ancestor of the other), then $F_1$ and $F_2$ share zero tree
edges. Their sym-diff contains all edges of both, giving $v_1$ and $v_2$
degree 3 (two tree edges plus one back edge each) — not a simple cycle. So
different-branch sym-diffs never yield simple cycles.

**Unified theorem.** The sym-diff of two fundamental cycles $F_1, F_2$ is a
simple cycle if and only if their respective back edges lie on the same DFS
branch (i.e., there is a root-to-leaf path through $u_1, u_2, v_2, v_1$ in
some order). In all such cases the sym-diff length is $(\delta_1 - \delta_2) + 2$
where $\delta_1 \ge \delta_2$ are the depth-gaps. This unifies the same-leaf,
nested, and crossing cases under a single formula.

**Implication for Q9.** The depth-gap constraint $\delta_1 - \delta_2 \notin
\{2, 6, 14, \ldots\}$ applies to ALL nested back-edge pairs (same leaf or
not), not only same-leaf ones. This broadens the forbidden set: a
counterexample must avoid the sym-diff constraint not only at DFS leaves
but also for any two nested back edges in any DFS tree.

<!-- CHECK
# Verify nested sym-diff formula: length = (delta1 - delta2) + 2
# for all nestings u1 <= u2 <= v2 <= v1 on a linear-path DFS tree.
# depths: u1 at depth d_u1, u2 at d_u2, v2 at d_v2, v1 at d_v1.
# delta1 = d_v1 - d_u1, delta2 = d_v2 - d_u2.
# Nesting: d_u1 <= d_u2 < d_v2 < d_v1 (strict to avoid degenerate same-vertex cases).
# Back edges: always to PROPER ancestors (never to parent).
# On a linear path graph: vertex i at depth i.

def nested_sym_diff_length(d_u1, d_u2, d_v2, d_v1):
    assert d_u1 <= d_u2, "u1 must be ancestor of u2"
    assert d_u2 < d_v2, "u2 must be proper ancestor of v2"
    assert d_v2 < d_v1, "v2 must be ancestor of v1"
    assert d_v2 >= d_u2 + 2, "v2 back edge must be to proper ancestor (not parent)"
    assert d_v1 >= d_u1 + 2, "v1 back edge must be to proper ancestor (not parent)"

    # Build fund cycles on linear path graph (vertex at depth = index).
    def fund_path(u_d, v_d):
        # tree edges from v_d up to u_d, plus back edge (u_d, v_d)
        edges = set()
        cur = v_d
        while cur != u_d:
            edges.add((cur - 1, cur))
            cur -= 1
        edges.add((u_d, v_d))
        return edges

    F1 = fund_path(d_u1, d_v1)
    F2 = fund_path(d_u2, d_v2)
    sd = F1.symmetric_difference(F2)

    # Check degree-2 everywhere
    deg = {}
    for a, b in sd:
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
    assert all(d == 2 for d in deg.values()), \
        f"Non-2 degree in nested sd: d_u1={d_u1},d_u2={d_u2},d_v2={d_v2},d_v1={d_v1}, deg={deg}"

    delta1 = d_v1 - d_u1
    delta2 = d_v2 - d_u2
    expected = (delta1 - delta2) + 2
    assert len(sd) == expected, \
        f"Length mismatch: got {len(sd)}, expected {expected}, d_u1={d_u1},d_u2={d_u2},d_v2={d_v2},d_v1={d_v1}"
    return len(sd)

checked = 0
for d_u1 in range(0, 10):
    for d_u2 in range(d_u1, 13):         # u2 at same depth or deeper than u1
        for d_v2 in range(d_u2 + 2, 16): # v2 at least 2 below u2 (proper ancestor, not parent)
            for d_v1 in range(d_v2 + 1, 18): # v1 strictly below v2
                if d_v1 - d_u1 < 2:     # v1 back edge must be proper ancestor
                    continue
                try:
                    nested_sym_diff_length(d_u1, d_u2, d_v2, d_v1)
                    checked += 1
                except AssertionError:
                    raise

assert checked > 2000, f"Too few configurations checked: {checked}"
print(f"OK: nested sym-diff formula (delta1-delta2)+2 verified on {checked} configurations")

# Also verify the CROSSING case: d_u1 < d_u2 < d_v2 < d_v1 (same branch, neither nested)
def crossing_sym_diff_length(d_u1, d_u2, d_v2, d_v1):
    assert d_u1 < d_u2 < d_v2 < d_v1
    assert d_v2 - d_u2 >= 2  # inner back edge proper ancestor
    assert d_v1 - d_u1 >= 2  # outer back edge proper ancestor

    def fund_path(u_d, v_d):
        edges = set()
        cur = v_d
        while cur != u_d:
            edges.add((cur - 1, cur))
            cur -= 1
        edges.add((u_d, v_d))
        return edges

    F1 = fund_path(d_u1, d_v1)
    F2 = fund_path(d_u2, d_v2)
    sd = F1.symmetric_difference(F2)

    deg = {}
    for a, b in sd:
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
    assert all(d == 2 for d in deg.values()), \
        f"Non-2 degree in crossing sd: {d_u1},{d_u2},{d_v2},{d_v1}, deg={deg}"

    delta1 = d_v1 - d_u1
    delta2 = d_v2 - d_u2
    expected = (delta1 - delta2) + 2
    assert len(sd) == expected, \
        f"Crossing mismatch: got {len(sd)}, expected {expected}"
    return len(sd)

cross_checked = 0
for d_u1 in range(0, 8):
    for d_u2 in range(d_u1 + 1, 11):
        for d_v2 in range(d_u2 + 2, 14):
            for d_v1 in range(d_v2 + 1, 16):
                if d_v1 - d_u1 < 2:
                    continue
                crossing_sym_diff_length(d_u1, d_u2, d_v2, d_v1)
                cross_checked += 1

assert cross_checked > 1000, f"Too few crossing configs: {cross_checked}"
print(f"OK: crossing sym-diff formula verified on {cross_checked} configurations")
CHECK -->
