# Session handoff (session s_0515-080112-9d0a)

**Stop reason**: logical milestone — all 6 initial open questions resolved; 3 keep_progress rounds committed; approaching context limit.

**Current focus**: Partial result documented in proof_strategy.md. Three kept records under records/proof_primitive_set_erdos_*.json.

**What was accomplished this session**:
- Section 1: Claim + three given facts (F1/F2/F3) with sign disambiguations, witness contract.
- Section 2: Numerical evidence — A_k partial sums table (k=1..6, x_floor=2/100/1000/10000), prime-set sum behavior, witness search (found {2,3} at x_floor=2 but confirmed non-counterexample).
- Section 3: Proof structure — omega-stratification (Lemma 1), stratum-bound obstacle (Lemma 2), smallest-prime-factor sketch.
- Identified the CORE OBSTACLE: the per-stratum bound is insufficient (stratum sums diverge when summed over k); the antichain constraint is global. The smallest-prime-factor approach avoids this by grouping by P^-(a), but requires bounding sum_p C(p,x)/(p log p) <= 1 + o(1).

**Key technical findings**:
- F3 is a LARGE-k asymptotic only; for k=1 (primes), the full unrestricted sum is > 1. F3 is not a global upper bound for small k.
- For ANY x >= 3, no primitive subset of [x,∞) has sum > 1.0. The x_floor=2 witness {2,3} with sum 1.025 is consistent with the conjecture (o(1) slack at x=2 is large).
- The smallest-prime-factor approach (§3.3) is the promising direction: assign each a ∈ A to its smallest prime factor p; bound each bucket B_p separately; sum over p.

**Lemma files**:
- proof_lemmas/lemma_001_omega_stratification.md (status: open, essentially trivial)
- proof_lemmas/lemma_002_stratum_bound.md (status: open, identifies the difficulty)

**Obstacle for next session**: Proving sum_p C(p,x)/(p log p) <= 1 + o(1). This needs:
1. A count of integers m >= x/p with P^-(m) > p — related to the "smooth number" or "rough number" counting function.
2. An estimate that this count is approx. x/p * prod_{q<=p} (1 - 1/q) by inclusion-exclusion.
3. Combining with 1/(p log p) to get sum_p (density) ~ 1.

**Suggested next move**:
1. Read lemma_002_stratum_bound.md.
2. Create lemma_003_rough_number_density.md: state and attempt to prove the density estimate for integers with P^-(n) > p in [y,∞).
3. If the density estimate uses Mertens' theorem (sum_{p<=P} 1/p ~ log log P), note this is not in the fact ledger (F1/F2/F3 only) and hedge accordingly.
4. If progress stalls, write the rough-number density as a CONDITIONAL lemma (assuming Mertens) and note the condition.

**Files modified this session**:
- proof_strategy.md (Section 1 + Section 2 + Section 3)
- proof_lemmas/lemma_001_omega_stratification.md (created)
- proof_lemmas/lemma_002_stratum_bound.md (created)
- proof_open_questions.jsonl (Q1-Q6 all resolved)
- proof_journal.jsonl (rounds 1-3 logged)
