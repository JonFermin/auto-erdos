---
id: lemma_single_stratum
title: "Lemma 4 — Single-Stratum Bound"
status: proved
depends_on: [F1, F3, Prop_8.2]
qid: Q12
---

## Statement

**Lemma 4 (Single-Stratum Bound).** Let x ≥ 2. For any primitive set A ⊆ A_k ∩ [x, ∞):

  S_k := Σ_{a ∈ A} 1/(a log a) < 1 + o(1)  as x → ∞.

More precisely:

- Case k = 1 (primes): S_1 = T_1(x) → 0 as x → ∞. In particular S_1 < 1.
- Case k ≥ 2: S_k ≤ T_k(x) ≤ (full A_k sum) = 1 − (c+o(1))k²/2^k < 1.

## Proof

**Setup.** Since A ⊆ A_k, every element of A has exactly k prime factors (with multiplicity). Primitivity is automatic for single-stratum sets when k = 1 (no prime divides another prime). For k ≥ 2 we use only the bound S_k ≤ T_k(x).

**Case k = 1** (A consists of primes in [x, ∞)).
Any primitive A ⊆ P ∩ [x, ∞) has:
  S_1 ≤ T_1(x) = Σ_{p ≥ x, p prime} 1/(p log p).
By Proposition 8.2 (see Section 8 of proof_strategy.md), T_1(x) → 0 as x → ∞.
Hence S_1 < 1 for all sufficiently large x. □

**Case k ≥ 2** (A ⊆ k-almost primes in [x, ∞)).
Since A ⊆ A_k and all elements are ≥ x:
  S_k ≤ Σ_{n ∈ A_k, n ≥ x} 1/(n log n) ≤ Σ_{n ∈ A_k} 1/(n log n).

By given fact F3: Σ_{n ∈ A_k} 1/(n log n) = 1 − (c+o(1))k²/2^k, where c ≈ 0.0656 > 0.

For k ≥ 2: 1 − (c+o(1))k²/2^k < 1.

In detail, for k = 2: 1 − (c+o(1))·4/4 = 1 − c·(1+o(1)) < 1.
For k ≥ 3: 1 − (c+o(1))k²/2^k → 1 from below, but the correction is positive. □

## Significance

This lemma proves the single-stratum case of Erdős's conjecture. The conjecture for
general primitive A reduces to the cross-stratum interaction: how much of the budget is
"shared" across strata when A has elements at multiple k-levels.

Specifically, Lemma 4 shows the bottleneck is NOT any single stratum—each is individually
strictly less than 1. The challenge is that summing across strata can approach 1 in the
limit (since Σ_k [full A_k sum] = Σ_k [1 − correction_k] > 1).

## Open consequence

The gap between "each S_k < 1" and "Σ_k S_k < 1 + o(1)" is the cross-stratum competition
analyzed in Sections 7–9. The key missing ingredient remains: a Mertens/PNT-type lower
bound on T_1(a) to establish SSC, or an alternative comparison route (PEX).
