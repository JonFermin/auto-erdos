---
id: same_leaf_sym_diff
status: proved
depends_on: []
discharged_by_round: 2
introduced_at_round: 2
---

# Lemma: same-leaf sym-diff formula

**Statement.** Let $T$ be a DFS tree of a connected graph $G$, and let $v$
be a DFS leaf (no tree children) with two back edges to ancestors
$u_1, u_2$ at depths $d_1 \le d_2$ (so $u_2$ is the deeper ancestor,
closer to $v$). Write $\delta_i = \operatorname{depth}(v) - d_i$ for the
depth-gaps ($\delta_1 \ge \delta_2 \ge 1$). The symmetric difference
$F_1 \triangle F_2$ of their fundamental cycles is a simple cycle of
length $\delta_1 - \delta_2 + 2 = d_2 - d_1 + 2$.

**Remark on scope.** The precondition requires both $u_1, u_2$ to be proper
non-parent ancestors: depth $d_i \le \operatorname{depth}(v) - 2$. In DFS on a
simple graph, back edges are always to proper ancestors and never to the
parent (the tree edge), so this is automatically satisfied for any genuine
DFS back edge. The case $d_2 = \operatorname{depth}(v) - 1$ would make
$(v, u_2)$ the tree edge, which is not a back edge.

**Proof.** Write $\Pi_i$ for the set of tree edges on the path from $v$
up to $u_i$. Since $u_2$ lies on the path from $v$ to $u_1$ (as $u_2$ is
a descendant of $u_1$ and an ancestor of $v$), we have
$\Pi_1 = \Pi_2 \cup \Pi_{12}$ where $\Pi_{12}$ is the set of tree edges
from $u_2$ (exclusive) up to $u_1$ (inclusive), $|\Pi_{12}| = d_2 - d_1$.

$F_i = \Pi_i \cup \{(v, u_i)\}$, so
$$F_1 \triangle F_2 = (\Pi_1 \triangle \Pi_2) \cup \{(v,u_1),(v,u_2)\}
  = \Pi_{12} \cup \{(v,u_1),(v,u_2)\}.$$

Degree check: $v$ has edges $(v,u_1)$ and $(v,u_2)$, degree $2$; $u_1$
has $(v,u_1)$ and the first $\Pi_{12}$ edge, degree $2$; $u_2$ has
$(v,u_2)$ and the last $\Pi_{12}$ edge, degree $2$; each intermediate
vertex of $\Pi_{12}$ has degree $2$. Connectivity: the edge-set traces the
cycle $v \to u_1 \to [\text{tree path down to }u_2] \to v$. Hence it is a
simple cycle of length $|\Pi_{12}| + 2 = (d_2 - d_1) + 2 =
(\delta_1 - \delta_2) + 2$. $\square$

**Corollary (depth-gap constraint).** If $G$ has no cycle of length $2^k$
for any $k \ge 2$ (i.e.\ $G$ is a hypothetical Erdős–Gyárfás
counterexample), then for every DFS leaf $v$ with back edges to ancestors
at depth-gaps $\delta_1 > \delta_2$:
$$\delta_1 - \delta_2 \notin \{2, 6, 14, 30, \ldots\} = \{2^k - 2 : k \ge 2\}.$$
Combined with the individual fundamental-cycle constraint
$\delta_i \notin \{3, 7, 15, 31, \ldots\} = \{2^k - 1 : k \ge 2\}$, these
are the necessary arithmetic conditions on depth-gap pairs at every DFS leaf.

**Scope.** This lemma covers only the case where $v$ is a leaf and both
back edges share the leaf as the descendant endpoint. General sym-diffs
(back edges from different DFS vertices, or where one fundamental cycle is
not nested inside the other) are covered by the broader pairwise
chain-locality CHECK in `lemma_dfs_chain_locality.md`.

<!-- CHECK
# Verify the same-leaf sym-diff length formula (d2-d1)+2 on a linear
# path DFS tree.  Back edges are to PROPER ancestors, so d2 <= dv-2
# (d2 = dv-1 would be the tree edge to the parent, excluded in DFS).

def sym_diff_length(dv, d1, d2):
    # d1 < d2 <= dv-2 < dv; path graph: vertex i at depth i, tree edges (i,i+1)
    assert d1 < d2 <= dv - 2 < dv, f"precondition failed: dv={dv},d1={d1},d2={d2}"

    def fund_path(u_d, v_d):
        # tree edges from v_d up to u_d, plus the back edge (u_d, v_d)
        edges = set()
        cur = v_d
        while cur != u_d:
            edges.add((cur - 1, cur))
            cur -= 1
        edges.add((u_d, v_d))  # back edge (u_d < v_d so already ordered)
        return edges

    F1 = fund_path(d1, dv)
    F2 = fund_path(d2, dv)
    sd = F1.symmetric_difference(F2)

    deg = {}
    for a, b in sd:
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
    assert all(d == 2 for d in deg.values()), f"Non-2 degree at dv={dv},d1={d1},d2={d2}: deg={deg}"
    assert len(sd) == (d2 - d1) + 2, f"Length mismatch: got {len(sd)}, expected {(d2-d1)+2}, dv={dv},d1={d1},d2={d2}"
    return len(sd)

checked = 0
for dv in range(4, 22):          # need dv >= 4 so d1 < d2 <= dv-2 has solutions
    for d1 in range(0, dv - 2):  # d1 <= dv-3 so d2 can be at most dv-2
        for d2 in range(d1 + 1, dv - 1):  # d2 in [d1+1, dv-2]
            result = sym_diff_length(dv, d1, d2)
            assert result == (d2 - d1) + 2
            checked += 1

assert checked > 1000
print(f"OK: same-leaf sym-diff formula verified on {checked} depth configurations")
CHECK -->

**Depth-gap arithmetic implication.** Let $\delta = \delta_2$ (the smaller
gap) and $\Delta = \delta_1 - \delta_2$ (the gap-difference). The
sim-diff cycle has length $\Delta + 2$. The individual-cycle constraint
forbids $\delta_2 = 2^k - 1$ (so $\delta_2 \ne 3, 7, 15, \ldots$) and
$\delta_1 = \delta_2 + \Delta \ne 2^k - 1$. The sym-diff constraint
forbids $\Delta = 2^k - 2$ (so $\Delta \ne 2, 6, 14, \ldots$). In a
counterexample, every DFS leaf with $\ge 2$ back edges must find a pair
$(\delta, \Delta)$ avoiding all three constraints simultaneously.

Small search: for $\delta_2, \delta_1 \le 30$, avoiding $\{3,7,15\}$ for
both and $\{2,6,14\}$ for the difference, the first valid pair is
$(\delta_2, \delta_1) = (1, 4)$ (difference $3$). Next: $(1,5)$,
$(2,4)$, $(2,5)$, etc. So valid pairs exist; the arithmetic constraints
alone do not rule out all configurations. The Q9 program seeks a structural
argument (min-degree and DFS leaf charge forcing) that prevents the
necessary pairs from all being simultaneously realizable in any finite
min-degree-3 graph.
