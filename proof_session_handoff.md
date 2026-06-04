# Session handoff (session s_0604-080657-e722)

**Stop reason**: logical milestone (Lemma 1 proved, 3 rounds kept as partial_result) + token budget

**Proof tag**: primitive_set_erdos

**Current state of proof_strategy.md**: 4 sections complete.
- Section 1: Setup (claim, F1/F2/F3 sign disambiguations, witness contract)
- Section 2: Numerical evidence — restricted tail sums S_k(x) < 1 for x_floor ≥ 3 (verified at x=3,10,100,1000,10000)
- Section 3: Witness search — {2,3} verified at x_floor=2 (sum=1.025>1, but o(1) at x=2 is large and NOT a disproof). No witness found for x_floor ≥ 3.
- Section 4: Proof outline — Lemma 3 ("primes maximize the sum") is the key open gap.

**Lemma files**:
- lemma_001_stratum_tail_bound.md: status=proved. Lemma 1 is established (each k-stratum restricted sum → 0 as x → ∞ for fixed k).
- lemma_002_cross_stratum.md: status=open. The "local exchange" argument (replacing prime p in A with composite pm gives smaller sum) is not yet proved.

**qids in flight**: none (Q1-Q6 all resolved).

**Key obstacle for the next session**: Prove Lemma 2's "local exchange" claim: for any primitive A ⊆ [x, ∞) and any non-prime element b ∈ A, there exists a modified set A' that: (a) is still primitive, (b) replaces b with a prime, and (c) has sum ≥ sum(A). If this exchange can always be done, then the all-primes set A* maximizes the sum (Lemma 3), and since sum(A*) = Σ_{p ≥ x} 1/(p log p) → 0 < 1, the conjecture follows.

**Files modified this session**:
- proof_strategy.md (all 4 sections written from the stub)
- proof_lemmas/lemma_001_stratum_tail_bound.md (created, status: proved)
- proof_lemmas/lemma_002_cross_stratum.md (created, status: open)
- proof_open_questions.jsonl (Q1-Q6 claimed and resolved)
- proof_journal.jsonl (3 round events)

**Suggested next move**:
1. Read proof_lemmas/lemma_002_cross_stratum.md, "Current obstacle" section.
2. Try the local exchange: for b = p1 * p2 * ... * pk ∈ A (composite, Ω(b)=k), show Σ_{a ∈ A} 1/(a log a) ≤ Σ_{a ∈ A'} 1/(a log a) where A' = (A \ {b}) ∪ {p1} and p1 is the smallest prime factor of b (assuming p1 ∉ A).
3. The key calculation is: 1/(p1 log p1) vs. 1/(b log b) + [lost elements from exclusions by p1 vs. b].
4. If exchange fails (i.e., removing b to add p1 hurts), document WHY in lemma_002_cross_stratum.md.
