# Session handoff (session s_0803-080758-2226)

**Stop reason**: Logical milestone — two keep_progress rounds (R19, R20).

**Current focus**: Q9 — analytic proof that the 4-mechanism taxonomy covers
all cubic DFS trees. The triple mechanism is now UNDERSTOOD structurally;
what remains is an existence argument.

**What was proved this session**:

R19 — `triple_sym_diff_structure` (proved, 6 parts):
1. |S| = 3 + t (t = tree edges covered by an odd number of the three
   sender→anchor paths); rederives triple_parity(2).
2. S is always a nonempty even subgraph; single simple cycle iff
   connected and 2-regular; deg_S(v) = b(v) + τ(v).
3. **Pasting lemma**: simple cycles X, Y whose intersection SUBGRAPH is a
   single path of length k ≥ 1 sym-diff to a single cycle of length
   |X| + |Y| − 2k. (The subgraph condition — shared vertices exactly the
   path's vertices — is essential; shared off-path vertices give degree-4.)
4. **Triple pasting criterion**: pair sym-diff D a single cycle (mixed
   parity ALLOWED — this is the blind spot of the pair taxonomy, which
   only asks for PO2 length) + third back edge with D ∩ C₃ a single
   k-path ⇒ S single cycle of length |D| + gap₃ + 1 − 2k.
5. Parity bookkeeping: mixed pair (odd |D|) fires only with even gap₃
   (OEE); same-parity pair (even |D|) only with odd gap₃ (OOO/EEO).

R20 — `pasting_rescue_census` (open, probe unfalsified):
- 120,000 DFS trees (n ∈ {12,14,16}); 54 pair-residual trees (no PO2
  fundamental cycle, no single-PO2-cycle pair sym-diff in ANY pair
  configuration, incl. branching pairs).
- ALL 54 are mixed-parity; ALL 54 admit a firing triple factoring through
  pasting. Shapes: mixed-pair+even-g3 → C8 36×, C16 1×;
  same-pair+odd-g3 → C8 17×. k spread 1..7 (no concentration).

**qid in flight**: Q9 released with partial progress. Next session
re-claims Q9.

**Suggested next move (R21) — the analytic existence argument, split**:
1. **Supply**: prove that a mixed-parity pair-residual tree contains a
   pair of back edges with single-cycle sym-diff D in a parity class
   with a legal third back edge. Candidate route: in a cubic DFS tree
   every non-root internal vertex has exactly one back edge over it
   (degree bookkeeping, cf. Sections 8–10 branch bounds); take an
   odd-gap and an even-gap back edge whose paths overlap — the pasting
   lemma applied to C₁, C₂ (X=C₁, Y=C₂!) says overlapping-in-a-path
   pairs ALWAYS give single-cycle D.
2. **Tuning**: show |D| + gap₃ + 1 − 2k hits {4,8,16,32} for some legal
   (B₃, k). k is NOT free — it is determined by (D, B₃) — so the
   quantifier is over third back edges; R18 saw 4–8 firing triples per
   rescued tree, suggesting slack. Try: bound the range of
   |D| + gap₃ + 1 − 2k over available B₃ and show it must cross a power
   of 2 with the right parity (all candidate values have the SAME parity
   — steps of 2 — so hitting is a range/pigeonhole question, not parity).
3. If tuning at radius 3 stalls: consider whether pair-residual trees
   have bounded |D| options (the census could be extended to record
   min/max of the tunable value).
4. Run everything with PROOF_TAG=erdos_gyarfas. Critics are stochastic;
   an infra 'critic_unavailable: internal' blocking finding is transient —
   re-run proof_prepare (happened this session, second run was clean).

**Files modified this session**:
- proof_lemmas/lemma_triple_sym_diff_structure__0803-080758-2226.md (new, proved)
- proof_lemmas/lemma_pasting_rescue_census__0803-080758-2226.md (new, open probe)
- proof_strategy.md (Sections 26, 27)
- notes channel: pasting insight appended (proof_notes_erdos_gyarfas.md)
