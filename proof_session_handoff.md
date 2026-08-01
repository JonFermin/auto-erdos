# Session handoff (session s_0801-082519-6641)

**Stop reason**: Logical milestone — R17 complete. Token budget approaching limit.

**Current focus**: Q9 — analytic proof that the 4-mechanism taxonomy covers ALL
cubic DFS trees. The computational evidence now covers n≤18 (NONE=0 at all sizes).

**What was proved this round (R17)**:
1. `crossing_offset_parity` (new, proved): For any crossing pair B1=(s1,a1) and
   B2=(s2,a2) in strict crossing order, the crossing offset omega satisfies
   omega ≡ gap(B1)+gap(B2) (mod 2). Consequence: crossing mechanism can only
   fire from same-parity gap pairs. Opposite-parity crossing pairs give odd omega
   (never in PO2_DIFFS={2,6,14,...}). CHECK verified on 1024 crossing pairs.
2. `coverage_extended` updated to n=18: NONE=0 confirmed for 1200 DFS trees
   at n=18. Coverage: easy=91.6%, nested=8%, crossing=0.3%, triple=0.08%.
3. Section 24 added to proof_strategy.md: parity partition, unit-crossing-pair
   structure, sub-case analysis for all-odd vs all-even gap cases.

**Ledger updates auto-detected by proof_log_result.py**:
- `crossing_pair_formula`: open → proved (from R16 file update, now in ledger)
- `leaf_pair_witness`: open → proved (from R16 file update, now in ledger)
- `crossing_offset_parity`: new → proved (R17)
- `coverage_extended`: still open (computational, not analytic)
- `chain_locality_r3`: still open (the main target)

**qid in flight**: Q9 released (partial progress). Next session should re-claim Q9.

**Obstacle**: The analytic proof of 4-mechanism completeness requires showing
that in any cubic DFS tree, one of the 4 mechanisms fires. The parity constraint
from `crossing_offset_parity` simplifies the case analysis:
- All-odd-gaps: crossing offsets all even. Need omega=2 (unit-step crossing pair)
  or omega in {6,14,...} or triple. The unit-step crossing pair condition requires
  structural properties of cubic DFS trees that haven't been proved yet.
- All-even-gaps: easy never fires. Leaf-pair and crossing handle most cases.
- Mixed: crossing restricted to same-parity sub-pairs.

**Files modified this session**:
- proof_strategy.md (Section 24 added)
- proof_lemmas/lemma_crossing_offset_parity__0801-082519-6641.md (new, proved)
- proof_lemmas/lemma_coverage_extended__0801-080553-f19f.md (n=18 added to CHECK + summary)
- proof_open_questions.jsonl (Q9 claimed + released)
- proof_journal.jsonl (R17 round entry)

**Suggested next move (R18)**:
1. Re-claim Q9.
2. Focus on the all-odd-gaps sub-case: prove that unit-step crossing pairs
   (alpha=beta=1, giving omega=2 = C4) must exist in cubic DFS trees when
   easy + leaf-pair both fail.
3. Alternatively: try the all-even-gaps sub-case: show that if all gaps are
   even and no gap is in PO2_GAPS (which it can't be since PO2_GAPS are odd),
   then leaf-pair or crossing always fires.
4. Write a new CHECK-backed lemma for whichever sub-case you can prove.
5. Run proof_prepare.py with PROOF_TAG=erdos_gyarfas (not the default!) and
   proof_log_result.py to log the round.
