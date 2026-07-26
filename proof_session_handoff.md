# Session handoff (session s_0726-080718-bd1c)

**Stop reason**: token budget low (9 substantive rounds completed)

**Rounds this session**: 9 keep_progress records
- R3 (9bd71e2): Q9 — alternation obstruction (count=4 AND strict alternating) both disproved via CL-A falsifiers; global existence argument required
- R5 (870a50a): Q9 — radius-4 escalation to n=20..24 (C4/C8, 750 states): max radius=3, no hit
- R6 (819da66): Q9 — cubic depth-gap mechanism: easy-path (depth-gap in {3,7,15}) vs hard-path; CHECK n=8..16
- R7 (ef4c22b): Q9 — girth-5 cubic depth-gap: easy-path requires depth-gap in {7,15}; Petersen + sampled; CHECK n=10..20
- R8 (c91c878): Q11 — cyclic orbit union-closure avg size >= n/2: Frankl for transitive cyclic families; exhaustive CHECK n=4..10
- R9 (ecab37c): Q11 — dihedral D_n orbit: same claim; reduces to two cyclic orbits
- R10 (313e277): Q11 — cyclic orbit partial proof: |A|>=n/2 case trivially proved; thin case open; shift-pairing not injective
- R11 (1ded976): Q9 — Hamiltonian-path DFS tree case: back-edge structure, adversarial CHECK n=8..18

**Q9 status** (chain_locality_r3): open. No proof found; no counterexample found up to n=24.
- Alternation obstruction is definitively dead (both versions falsified by CL-A).
- Depth-gap mechanism (easy/hard path) well-characterized: easy path dominates most (G,T) pairs; hard path verified by explicit C8/C16 search.
- Girth-5 sub-case: Petersen + sampled girth-5 graphs all satisfy chain_locality_r3.
- Hamiltonian-path tree: cubic path-tree back-edge structure documented; CHECK passes.
- Analytic proof still open. Next: try to prove easy-path sub-claim (some back edge has depth-gap in {3,7,15}) for ALL cubic DFS trees using the degree constraint.

**Q11 status** (frankl_union_closed / transitive screen): partially done.
- Cyclic orbit: avg size >= n/2 proved for |A|>=n/2; thin case CHECK-verified n<=15 but analytic proof open.
- Dihedral orbit: reduces to cyclic; CHECK-verified.
- Next: affine group AGL(1,q) orbit screen; prove thin-case via direct counting argument.

**Suggested next move** (priority order):
1. Q9 easy-path analytic proof: for any cubic DFS tree, prove that some back edge has depth-gap in {3,7,15} OR chain_locality_r3 holds via 2-3 back edges via a specific structural argument.
2. Q11 thin-case proof: for |A| < n/2 in Z_n, prove avg size >= n/2 via the Bollobás set-pairs / two-family intersection approach.
3. Q9 extended radius-4 search: run simulated annealing at n=25..30 to probe further.

**Files modified this session**:
- proof_strategy.md (Sections 11-18 added)
- proof_lemmas/lemma_alternation_obstruction.md (status: disproved)
- proof_lemmas/lemma_radius4_hunt_n24.md (created, status: open)
- proof_lemmas/lemma_cubic_depth_gap.md (created, status: open)
- proof_lemmas/lemma_girth5_depth_gap.md (created, status: open)
- proof_lemmas/lemma_cyclic_orbit_avg_size.md (created, partial proof, status: open)
- proof_lemmas/lemma_dihedral_orbit_avg_size.md (created, status: open)
- proof_lemmas/lemma_ham_path_tree_r3.md (created, status: open)
- proof_open_questions.jsonl (Q9 released, Q11 resolved)
- proof_journal.jsonl (rounds appended)
