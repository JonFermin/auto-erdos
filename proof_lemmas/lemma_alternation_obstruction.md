---
id: alternation_obstruction
status: disproved
depends_on: [chain_locality_r3]
discharged_by_round: 4
introduced_at_round: 4
---

# Lemma `alternation_obstruction` — **DISPROVED**

Two versions of an alternation obstruction for C8s in DFS trees were
probed and both are false. The probing is logged here as a dead-end
record to prevent rediscovery.

## Version 1: Count=4 obstruction (FALSE)

**Claim (false)**: no C8 in any Trémaux tree of any connected
min-degree-3 graph has exactly 4 non-tree edges.

**Falsifier** (CL-A, tree_mask 2975, root 0):

- Graph: $n=10$ cubic graph with edges
  $\{(3,8),(2,4),(3,4),(5,8),(1,5),(3,7),(1,8),(0,9),(4,6),(7,9),(2,9),(6,7),(0,2),(0,5),(1,6)\}$
- DFS tree: `tree_mask=2975`, root 0, depths
  $\{0{:}0,\ 1{:}8,\ 2{:}5,\ 3{:}5,\ 4{:}4,\ 5{:}7,\ 6{:}3,\ 7{:}2,\ 8{:}6,\ 9{:}1\}$
- C8: cycle $1\text{-}8\text{-}3\text{-}7\text{-}9\text{-}2\text{-}4\text{-}6\text{-}1$,
  back edges $\{(3,7),(1,8),(2,9),(1,6)\}$ — **4 back edges**
- Pattern around cycle: **B-T-B-T-B-T-T-B** (not strictly alternating)

In this (CL-A, tree_mask=2975) pair, the 10 C8s have back-edge counts
$\{1{:}1,\ 3{:}4,\ 4{:}3,\ 5{:}2\}$; the minimum is 1 (a fundamental
C8), so chain_locality_r3 holds.

## Version 2: Strict alternating obstruction (FALSE)

**Claim (false)**: no C8 in any Trémaux tree of any connected
min-degree-3 graph has the perfect alternating pattern T-B-T-B-T-B-T-B
(back edges at equidistant positions forming a perfect matching in $C_8$).

**Falsifier** (also CL-A, different tree):

- Same graph CL-A as above
- C8: cycle $[0,2,9,7,3,8,1,5]$ with edges
  $(0,2),(2,9),(7,9),(3,7),(3,8),(1,8),(1,5),(0,5)$
- Back edges: $\{(2,9),(3,7),(1,8),(0,5)\}$ — positions 1,3,5,7 in the
  cycle order (odd positions), making pattern **T-B-T-B-T-B-T-B**
- The back edges form a perfect matching in $C_8$: this IS the strict
  alternating pattern.

## Consequence for chain_locality_r3

**chain_locality_r3 is not falsified.** In both (graph, tree) pairs
above, there exist C8s with back-edge count $\le 3$ (even $= 1$ in the
first pair). The alternation frame was proposed as a mechanism explaining
WHY chain_locality_r3 holds, not as a result required by it.

The probes show: C8s with 4 back edges (count=4) and even C8s with the
perfect alternating pattern (T-B-T-B-T-B-T-B) are realizable in DFS
trees of min-degree-3 graphs. These C8s coexist with lower-count C8s in
the same (graph, tree) pair; chain_locality_r3 holds because of the
EXISTENCE of a low-count C8, not because all C8s have low count.

## Structural consequence: mechanism must be global

The alternation frame sought a PER-CYCLE reason why C8s cannot have
$\ge 4$ back edges. This is false. The correct characterization of
chain_locality_r3 must be a GLOBAL EXISTENCE argument: "every (min-deg-3
graph, DFS tree) pair has at least one power-of-2 cycle with $\le 3$
back edges" — not "every C8 individually has $\le 3$ back edges."

The proof approach must therefore show that the MINIMUM over all po2
cycles is $\le 3$, not bound each cycle individually. This is a weaker
per-cycle claim but a harder global existence claim.

## Next steps (post-disproof)

Per the handoff suggestion:
1. **Radius-4 escalation**: extend the adversarial hunt from $n \le 18$
   to $n = 19..24$ with joint (graph, tree) simulated annealing. A hit
   at radius 4 falsifies chain_locality_r3 entirely. A null result
   strengthens the radius-3 conjecture.
2. **Cubic case proof**: in a DFS tree of a cubic graph, every leaf
   carries exactly 2 back edges (back-edge budget is sharp). The
   existence of a low-count po2 cycle in this setting might be provable
   by a pigeonhole argument on the leaf back-edge gap constraints.
3. **Theta-lift voltage obstruction**: Q8 notes channel records a lead
   on why theta lifts always have a short voltage-sum relation; that
   structural argument might generalize beyond the lift family.
