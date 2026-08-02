# Session handoff (session s_0802-080649-85be)

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
