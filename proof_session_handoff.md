
# Session handoff

> **MERGE NOTE.** master now contains two parallel Erdős–Gyárfás
> proof lines that forked before Section 19 and were merged by
> PR #37 then PR #38:
>
> - **Sections 19–57** (rounds R19–R33, sessions through
>   s_0729-131551-1d91) — DHS Hamiltonian-path model, depth-3/4
>   analysis, Theorems A/C, n=18 census.
> - **Sections 58–64** (rounds R13–R18, sessions through
>   s_0802-080649-85be) — 4-mechanism DFS taxonomy, coverage to
>   n=18, crossing/triple parity lemmas. Renumbered from 19–25
>   at merge time.
>
> The two round numberings are independent. Both handoffs are
> retained below; reconcile them before the next round.

---

## Handoff A — Sections 58–64 line (most recent, s_0802-080649-85be)


**Stop reason**: Logical milestone — R18 complete (keep_progress). Token budget approaching limit.

**Current focus**: Q9 — analytic proof that the 4-mechanism taxonomy covers ALL
cubic DFS trees. R18 completed the parity accounting and redirected the
analytic program to the mixed-parity triple mechanism.

**What was proved this round (R18)**:
1. `triple_parity` (new, proved): for three distinct back edges, the 3-way
   fundamental-cycle sym-diff S contains all three back edges (each lives in
   exactly one fundamental cycle), and |S| ≡ gap1+gap2+gap3+1 (mod 2). Hence
   the triple mechanism fires only on triples with an ODD number of odd gaps
   (OOO or OEE), and NEVER fires in an all-even-gap tree. This completes the
   parity accounting for all 4 mechanisms (easy: odd gap; nested/crossing:
   same-parity pairs; triple: OOO/OEE).
2. `residual_parity_census` (new, open/computational): falsification probe of
   the R17-proposed unit-step claim over 48,000 trees. Verdict: unfalsified
   but nearly vacuous — all-odd residuals are 7/48,000 (~0.015%), all at n=10,
   all rescued by a unit-step omega=2 crossing. Residual mass is >=96%
   mixed-parity. Every crossing-failed residual (122/122, all mixed) is
   rescued by a triple; rescue lengths: C8 698x, C4 39x, C16 1x.

**Also this round (critic-driven repairs to proof_strategy.md)**:
- Section 9's superseded R6 "unified sym-diff theorem" and "complete
  constraint system" now carry explicit supersession/scope-correction notes
  (Section 22 formulas are canonical for crossing pairs).
- Section 24's R17 error corrected: all-even gaps => crossing offsets are
  ALWAYS even (the old text said "odd or even").
- Moore-bound/Petersen girth claims recast as machine-verified enumeration
  results (the CHECK is load-bearing, classical theorems are only intuition).
- Frankl Sections 7/14-16 marked as cross-problem archive, not load-bearing
  for Erdős–Gyárfás.

**qid in flight**: Q9 released with partial progress. Next session should
re-claim Q9.

**Obstacle**: The analytic completeness proof now needs the triple mechanism
understood in the mixed-parity case. Parity says candidate triples are
OOO/OEE; empirics say a firing one always exists when pair mechanisms fail,
almost always giving a C8.

**Suggested next move (R19)**:
1. Re-claim Q9.
2. Prove a length formula for the 3-back-edge sym-diff cycle: |S| = 3 + t
   where t = number of tree edges covered by an odd number of the three
   sender->anchor tree paths. Then characterize when S is a SINGLE cycle
   (vs disjoint union) — start from the R15 crossing-order case analysis.
   Note the open ledger id `sym_diff_cycle_formula` covers a narrower
   configuration; a general statement needs a NEW lemma id.
3. Use the census data shape: rescued triples in the probe were plentiful
   (4-8 per tree) — suggests an averaging/counting existence argument rather
   than an explicit construction.
4. Run proof_prepare.py with PROOF_TAG=erdos_gyarfas (not the default!).
   Note: critics are stochastic; if a blocking finding targets pre-R18 text,
   fix it in-place (that is in-scope round work) and re-run.

---

## Handoff B — Sections 19–57 line (s_0729-131551-1d91)


**Stop reason**: logical milestone — Theorem C proved, n=18 census complete

**Rounds this session**: R29–R33 (5 rounds, all keep_progress)

**Current focus**: Depth-4 resolution for Case A cubic graphs.

## What was proved this session

**Theorem A (Section 55)**: sd=1 (C4 at depth-3) is IMPOSSIBLE in Case A.
Proof: matching constraint forces A3=[t1,k2) making e3 share vertex t1 with e1.

**Cycle Bound (Section 55)**: sd=13 (C16) requires n≥16; for n≤15 sd=5 is unique.

**Connectivity Theorem (Section 54)**: XOR of 3 back edges is single cycle iff c≥1
(c = |(A1△A2)∩A3| ≥ 1).

**Theorem C (Section 57)**: The 4 special back edges (r1,r2,l1,l2) form a
single depth-4 cycle iff ov = max(0, min(a2,s2)-max(a1,s1)) ≥ 1.
When ov≥1: L4 = (a2-a1)+(s2-s1)-2·ov+4.
When ov=0: two disjoint cycles of lengths (a2-a1+2) and (s2-s1+2).

## n=18 findings (Section 56)

Census (a1+a2≤24): 4985 sd=5 (C8), 1491 sd=13 (C16), **18 depth-3 failures**.
The 18 failures have NO depth-1/2/3 resolution. Both verified examples resolve
at depth-4:
- ex1 [(2,0),(6,0),(17,5),(17,15),...]: ov=1 → Theorem C gives C16 ✓
- ex2 [(2,0),(6,0),(17,11),(17,15),...]: ov=0 → interior quadruple gives C8 ✓

## Key open questions (what to do next)

**Q71** (PRIORITY): For Case A assignments with ov=0, prove that some depth-4
quadruple involving interior edges always gives a po2 cycle. This is the
remaining gap for the depth-4 universality argument.

Approach: When ov=0, the root gap [a1,a2) and leaf gap [s1,s2) are disjoint.
Consider triples of interior edges {e_i} with one root edge:
  (a1,0)+e_i+e_j+e_k: analyze the XOR interval and find po2 length.

**Q72** (after Q71): Verify depth≤4 universality for n=14,16,18 (all Case A).
Run full enumeration (not just a1+a2≤24) and check:
  failures = [a for a in all_case_A_assignments(n) if not any_depth4_po2(a)]

**Q73**: For larger n (n=20,22), does depth-4 still suffice, or do depth-5+ cases
appear? This will reveal whether the depth bound is truly uniform.

## Files modified this session

- proof_strategy.md: Sections 53–57 added (Lemma G, connectivity, Theorem A,
  Section 55 sd=1 impossible, Section 56 n=18 census, Section 57 Theorem C)
- proof_open_questions.jsonl: Q67 claimed and resolved this session

## Status of lemma files

No new lemma files created; all results in proof_strategy.md.

## Suggested first move for next session

1. Read proof_session_handoff.md (this file).
2. Read Section 57 in proof_strategy.md (last ~150 lines).
3. Work on Q71: prove depth-4 universality for ov=0 Case A.
   Try: pick one interior edge e_i, combine with r1=(a1,0), r2=(a2,0), e_j:
   need (a2-a1)+(g_i)+g_j - 2*intersections ∈ {0,4,12,28}. Show always achievable.
4. Run depth-4 universality check: python code enumerating all n=14 Case A and
   checking if any quadruple gives single-cycle po2.
