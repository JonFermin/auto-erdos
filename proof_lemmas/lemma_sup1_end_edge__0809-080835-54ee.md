---
id: sup1_end_edge
status: disproved
depends_on: [shortpaste_floor_line, pasting_cover_dichotomy, pasting_vertex_automatic, t3_min_overlap_short_paste]
discharged_by_round: 33
introduced_at_round: 31
---

# Lemma `sup1_end_edge` (DISPROVED R33 — see `sup1_dead_tree`)

**DISPROVED (R33).** `lemma_sup1_dead_tree__0810-081024-1a40.md` pins a
14-vertex cubic graph with a normal spanning tree that is pair-residual
and admits NO SUP-1 witness at all (exhaustively verified, 16 eligible
pairs $\times$ 6 third edges) — so the core SUP-1 claim, the end-edge
refinement, and the min-gap rule below are all false as universals.
The R31 censuses (189/189 across four seeds) were sampling luck; the
dead-tree rate is roughly 1 in a few hundred residual trees. The tree
still fires via triples with $|D \cap C_3| \in \{2,4\}$ — the $k'=1$
restriction is what dies, not the triple mechanism. The original
statement and census record are preserved below for the negative-result
trail.

**Setting.** $T$ a pair-residual DFS tree of a connected cubic graph.
For a pair $(B_1, B_2)$ with single-cycle $D = C_1 \triangle C_2$
(overlap $k_{12} \ge 1$), $D$'s tree edges decompose into the segments
$A = [a_{\mathrm{sh}} .. a_{\mathrm{deep}}]$, $L_1 = [m .. s_1]$,
$L_2 = [m .. s_2]$ ($m = \operatorname{lca}(s_1, s_2)$;
`pasting_meeting_structure`). An **end edge** of a segment is an edge
incident to one of its two boundary vertices ($a_{\mathrm{sh}}$ or
$a_{\mathrm{deep}}$ for $A$; $m$ or $s_i$ for $L_i$). A **SUP-1
witness** for the pair is a back edge $B_3$ with
$\operatorname{gap}_3 \le k_{12} + 1$ (short), $D \cap C_3$ a single
edge ($k' = 1$), and $|D| + \operatorname{gap}_3$ odd (so
$L = |D| + \operatorname{gap}_3 - 1$ is even, hence $L \ge 8$ by
`shortpaste_floor_line`(3) whenever $|D| \ge 6$... in fact directly:
$|D|$ odd $\ge 7$ gives $L \ge |D| + 1 \ge 8$; $|D|$ even $\ge 6$ gives
$L \ge |D| + 2 \ge 8$).

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual tree $T$ admits a pair with $|D| \ge 6$ and a SUP-1
witness whose met edge is an **end edge** of its segment. Moreover the
witness can be selected by the **min-gap rule**: for some pair
($|D| \ge 6$) and some end edge $e$, the minimum-gap back edge covering
$e$ is itself a SUP-1 witness.

**Consequence.** With `shortpaste_floor_line`(b), the claim closes the
T3 leg of the Q9 tuning program: every pair-residual tree has an even
short-paste value $\ge 8$, i.e. $V_e(T) \not\subseteq \{4, 6\}$ and
$V_e(T) \ne \emptyset$ (`t3_min_overlap_short_paste` discharges modulo
this supply statement).

**Census (R31, three independent seeds, $n \in \{12..24\}$, 480k
sampled DFS trees total, 152 pair-residual).**

- SUP-1 (some pair $|D| \ge 6$ with a $k'=1$ short even-$L$ cover):
  **152/152**. No tree needed the odd-$L$-only fallback (0 occurrences
  of "$k'=1$ short covers exist but never with even $L$").
- End-edge witness: **89/89** (checked on seeds 1 and 3).
- Min-gap selection rule over all end edges: **89/89**.
- **Falsified finer variants** (do NOT chase these): leg-TOP-only
  (met edge incident to $m$) fails 3/63 on seed 2; leg-BOTTOM-only
  (incident to a sender) fails 1/39; $A$-end-only fails 1/39. The
  end-edge disjunction over all six boundary edges is the survivor,
  not any single boundary.
- Witness arithmetic (seed 2, first witness per tree): min gap
  $\operatorname{gap}_3 \in \{2 (33), 4 (21), 5 (4), 9 (2)\}$;
  $|D| \in \{6..13\}$ dominated by odd (7: 26, 9: 20); $k_{12}$ spans
  $2..10$. For leg-top witnesses the cover's anchor $a_3$ lies in the
  cancelled interval $I = [a_{\mathrm{deep}} .. m]$ **60/60**, and
  $s_3 = c_i$ (the child of $m$ on the leg) 47/60.

**Analytic traction (why end edges — partial, not yet proved).** A
short cover pastes (`pasting_cover_dichotomy` c1), so its met set is a
single path inside ONE segment ($\Delta \le 3$:
`pasting_vertex_automatic`). For the leg-top edge $(m, c_i)$: a cover
containing it with $a_3$ a strict ancestor of $a_{\mathrm{deep}}$ would
contain the whole chain $I$ plus $A$'s deepest edge, i.e. straddle,
forcing $\operatorname{gap}_3 \ge k_{12} + 2$ — so every SHORT cover of
the leg-top edge anchors inside $I$ (consistent with the 60/60 census
line). Its $k'$ is the number of $L_i$-edges below $c_i$ on $P_3$;
$s_3$'s chain diverging from $L_i$ immediately below $c_i$ (e.g.
$s_3 = c_i$) gives $k' = 1$ automatically. The remaining analytic
burden: (i) existence of a covering back edge of an end edge that is
short with the right parity — 2-edge-connectedness supplies SOME cover
of every tree edge, but shortness is NOT automatic (90 non-short
$k'=1$ even-$L$ end-edge covers observed on seed 3); (ii) the parity
class $\operatorname{gap}_3 \equiv |D| + 1 \pmod 2$.

**Status.** DISPROVED at R33 — the dual-attack probe strategy worked as
designed, one round late: a wider-seed sweep found the counterexample
the committed fixed-seed probe missed.

---

<!-- R33: the committed sampling probe formerly here asserted the SUP-1
universal on fixed seeds; it passed only by sampling luck.  Removed when
the claim was disproved (see lemma_sup1_dead_tree__0810-081024-1a40.md,
whose CHECK verifies the counterexample deterministically).  A passing
probe for a disproved universal would be actively misleading. -->

## Summary

DISPROVED (R33) by `sup1_dead_tree`: a pinned pair-residual normal
spanning tree of a 14-vertex cubic graph admits no SUP-1 witness at
all, killing the core claim, the end-edge refinement, and the min-gap
rule as universals. The R31 census (189/189 over four seeds) was
sampling luck. What remains true and reusable: the anchor-in-$I$
geometry of short leg-top covers (proved independently as `sup1_iadj`
Part 1), and all the falsified-variant negatives recorded above. The
supply program must widen beyond $k' = 1$ (the counterexample fires
via $|D \cap C_3| \in \{2, 4\}$ triples) or move the quantifier to the
graph level.
