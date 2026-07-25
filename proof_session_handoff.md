# Session handoff (session s_0722-080706-a3ea)

**Stop reason**: logical milestone — two rounds completed (Q9 disproof + Q10 first-lemma)

**Current focus**: Q10 KL union-deficiency approach for Frankl union-closed conjecture.
Lemma `frankl_deficiency` is status: open — CHECK passes, analytic proof not yet done.

**Rounds this session**: 2 (rounds 2 and 3 on this branch; round 1 was Q9)
- Round 2: Q9 pairwise chain-locality DISPROVED, keep_progress
- Round 3: Q10 KL-deficiency first-lemma CHECK passes, keep_progress

**qids resolved this session**:
- Q9: CLOSED (dead end — pairwise chain-locality false at n=10 root=7)
- Q10: PARTIAL — first-lemma CHECK passed; analytic proof step open

**Key result (Round 2)**: n=10 cubic graph `nx.random_regular_graph(3,10,seed=12)`,
DFS root=7: fund cycle lengths [3,3,3,5,6,10], pairwise sym_diff lengths {0,5,6,7,9}
— no power of 2. Every C8 needs 3-way sym_diff. Q9 DFS discharging approach CLOSED.

**Key result (Round 3)**: The inequality log2|F| - H(A∪B) ≥ (1-p)^2/4 holds on:
- all union-closed families on {0,1,2,3} (exhaustive)
- power sets 2^U for |U|=1..7 (boundary p=1/2)  
- 500 random union-closed families n=2..7
Min margin ≈ 0.189 near p=0.5. Adversarial zone p∈[0.382,0.5) unreachable for small n
(Frankl known there), so the CHECK cannot witness a failure in the critical regime.

**Files modified this session**:
- proof_strategy.md (Section 5 updated: Q9 link; Section 6: Q9 disproof; Section 7: Q10 approach)
- proof_lemmas/lemma_chain_locality.md (created, status: disproved)
- proof_lemmas/lemma_frankl_deficiency.md (created, status: open)
- proof_open_questions.jsonl (Q9 claimed+resolved, Q10 claimed+resolved-partial)
- proof_journal.jsonl (2 round events)

**Records committed**:
- records/proof_erdos_gyarfas_7f11251e804c_b28657d.json (round 2, Q9 disproof)
- records/proof_erdos_gyarfas_80b054df11bb_c510d57.json (round 3, Q10 partial)

**Obstacle for next session**: The analytic proof of log2|F|-H(A∪B)≥(1-p)^2/4 is
the blocking step. The CHECK shows it holds in the safe regime (p≥0.5) but the
conjecture's interest is at p∈[0.382,0.5). Need an analytic bound.

**Suggested next move**:
1. Read proof_lemmas/lemma_frankl_deficiency.md and proof_strategy.md Section 7.
2. Attempt the analytic proof via chain rule: H(A∪B) = H(A) + H(B|A∪B) − H(B|A),
   bounding each conditional entropy using the element-frequency vector.
3. If analytic proof is too hard, try a direct SAT/ILP search for a family with
   p∈[0.382, 0.5) violating the bound — if found, the lemma is false and Q10 dies.
4. Alternative: Q11 (transitive symmetry counterexample screen) or Q12 (order-3
   sym_diff first-lemma for the remaining DFS approach).
