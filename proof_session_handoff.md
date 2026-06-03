# Session handoff (session s_0603-080714-20c2)

**Stop reason**: logical milestone — all seed questions Q1–Q6 addressed; Lemma 3 identified as open

**Current focus**: Lemma 3 — proving M(x) ≤ 1 + o(1) from the functional inequality (*):
  M(x) ≤ sum_{p ≤ x} M(x/p) / p

**Partial results achieved this session**:
- Section 1: Claim, F1/F2/F3 with sign notes, witness contract
- Section 2: F3 numerics for k=1..4 (F3 accurate only for large k; primes' full sum ≈ 1.6366)
- Section 3: Sum over all primes = 1.6366 (convergent, consistent with F1 for large x)
- Section 4: No witness for x_floor ≥ 100 (consistent with conjecture)
- Section 5: spf-reduction gives (*); L1 (trivial) and L2 (spf-reduction) proved; L3 open

**Lemma status**:
- lemma_001.md (omega_stratification): status: proved
- lemma_002.md (spf_reduction): status: proved — gives functional inequality (*)
- lemma_003.md (functional_ineq_bound): status: open — the hard step

**qid status**: Q1–Q6 all resolved. No qids in flight.

**Key obstacle**: The functional inequality (*) is correctly derived, but closing
  M(x) ≤ 1 + o(1) from it requires a new idea. The obvious ansätze (M = C/log x,
  M = 1 + h(x) with h→0) fail. The cross-fiber primitivity constraint in Lemma 2 is
  dropped in (*), and recovering it seems to require the full strength of Lichtman-Pomerance.

**Suggested next move for next session**:
1. Read lemma_003.md (functional_ineq_bound).
2. Try the Lichtman-Pomerance sieve approach: for each prime p, define the
   "p-contribution" f_p(A) = sum_{a in A, p|a} 1/(a log a). Show f_p(A) ≤ 1/(p log p).
   If proven, summing over p gives sum_a 1/(a log a) ≤ sum_p 1/(p log p) ≈ 1.636,
   which recovers F1-type bound but not the tight bound 1.
3. Alternatively: explore whether the conjecture can be proved for specific families
   (all A with min-element ≥ x²) where the bound tightens faster.
4. If Lemma 3 remains stuck after 5 more rounds, set status: abandoned and declare
   the proof attempt as a partial result.

**Files modified this session**:
- proof_strategy.md (Sections 1–5 added)
- proof_lemmas/lemma_001.md (created, proved)
- proof_lemmas/lemma_002.md (created, proved)
- proof_lemmas/lemma_003.md (created, open)
- proof_open_questions.jsonl (Q1–Q6 all resolved)
- proof_journal.jsonl (1 entry)
