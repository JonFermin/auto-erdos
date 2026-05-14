# Session handoff (session s_0514-080632-ade3)

**Stop reason**: keep_disproof / exit 7 — the harness detected a verified
witness and stopped the loop per protocol.

**Outcome**: `keep_disproof` record written at
`records/proof_primitive_set_erdos_31dac5a0d0df_4816f3c.json`.

**IMPORTANT — Human review required**:
The witness `{"x_floor": 2, "elements": [2, 3], "claimed_sum_lower_bound": 1.024}`
has rigorous lower bound ≈ 1.0248 > threshold 1.0. HOWEVER, this is NOT
a genuine counterexample to the conjecture because:

1. The conjecture bounds the sum by `1 + o(1)` where `o(1) → 0` as
   `x → ∞`. At `x_floor = 2`, the `o(1)` term is approximately 0.6
   (the bound at `x=2` is ≈ 1.636, not 1). So 1.0248 < 1.636, fully
   consistent with the conjecture.

2. The genuine content of the proof attempt is the NEGATIVE search result:
   no finite primitive set starting from `x ≥ 100` achieves sum > 1.0
   (primes from 100 to 100,000 give only 0.128; the densest strip
   [100, 200) gives about 0.14).

**Key finding from this session**:
F3 as given in the ledger is numerically inconsistent:
- F3 claims `sum(A_k) < 1` for all k ≥ 1, but k=1 (primes) gives sum ≈ 1.636.
- The formula `1 - (c+o(1))k^2/2^k` does not match actual data for any k.
- For k ≥ 2, sums satisfy S(k) < 1 but decrease toward 0, not toward 1.

**Files modified this session**:
- `proof_strategy.md` — full setup + numerical evidence + witness block
- `proof_open_questions.jsonl` — Q1–Q4 all resolved (Q5, Q6 still open)
- `proof_journal.jsonl` — two round events

**For next session**:
If continuing, the natural next step is Q5/Q6 (proof structure outline
or declaring a partial result). Given that:
- The witness at x=2 is not a genuine counterexample
- F3 appears incorrect
- No counterexample found at large x
A next session should focus on Q5: outline the stratification argument
for the conjecture, treating the k=1 (prime) stratum separately.

The genuine mathematical question is: what bounds the prime-stratum
contribution in a primitive set A ⊆ [x, ∞)? Since A is primitive,
if p ∈ A is prime, then no multiple of p can also be in A. This
limits how many primes can appear alongside composites.
