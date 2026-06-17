# Session handoff (session s_0617-145025-99ae)

**Stop reason**: token budget low after 7 rounds (Q32-Q37)

**Session results**: All 7 rounds kept as keep_progress. Records committed.

**Current focus**: Proving the Erdős primitive-set conjecture via partial results.
Committed 35 cumulative results (Sections 26-31 new this session).

**Key new results this session**:
1. Q32: `mertens_reduction` — sum 1/(a log a) ≤ (1/log x) sum 1/a; Reciprocal Conjecture (RC) implication
2. Q33: `log_polynomial_density` (|A∩A_k|≤k^m(log x)^α → sum→0); `near_full_density` (|A∩A_k|≤2^k/k^m → D(A)<∞ → sum→0)
3. Q34: `single_stratum_conjecture` (F3-based, sum<1 strict); `range_integral_bound` (A⊆[x,x^C) → sum≤logC+o(1)); `doubly_exponential_range` (conjecture for each A⊆[x^{e^n},x^{e^{n+1}}))
4. Q35: `T_recursion` T(x)≤1+T(x^e); `T_monotone_and_bounded`; banding barrier documented
5. Q36: shadow fraction framework; `elementary_shadow_lower` (p=2 bound); obstruction theorem (banding fails due to T*=lim T(x)=lim T(x^e))
6. Q37: `column_primitive_bound` (|A∩A_k|≤1 → sum≤1 exactly via power series sum1/(k2^k)=log2); `bounded_multiplicity` (≤M per stratum → sum≤M); `power_series_improvement` (column-prim → sum→0)

**Current open frontier** (Section 31 summary):
- Proved: all cases with |A∩A_k| = O(2^k/k^ε) (any polynomial savings per stratum)
- Open: |A∩A_k| = Θ(2^k) (full density strata), elements above x^e, D(A) = ∞
- Banding approach (T(x)≤1+T(x^e)) fails: both T(x) and T(x^e) share same limit T*
- Shadow bound needs Mertens; column-primitive (≤1 per stratum) gives sum≤1 exactly

**Obstacle**: The banding recursion T(x)≤C+T(x^e) always gives T*≤C+T* (trivially true).
Any proof of T*≤1 needs strict decrease T(x^e)≤T(x)-δ(x) with Σδ(x)≥T*-1 — requires Mertens.

**Files modified this session**:
- proof_strategy.md (Sections 26-31 added: Q32-Q37)
- proof_open_questions.jsonl (Q32-Q37 claimed/resolved, plus Q38 pending)
- proof_journal.jsonl (7 new round entries)
- proof_results.tsv (6 new logged rows: Q32-Q37)
- records/ (7 new committed records)

**Suggested next moves for Q38**:
Option A — Multiplicative function approach: Treat sum 1/(a log a) as integral of a^{-s} at s=1.
The formal identity sum_{a∈A} 1/(a log a) = ∫_1^∞ F_A(s) ds requires F_A to converge near s=1.
For primitive A, F_A has specific factorization properties that might give a bound via F1/F2/F3.

Option B — F2 as a global constraint: F2 bounds the FULL stratum sum from below.
For multi-stratum A, A can use at most a fraction of each stratum before the lower bound (F2)
for the complement contradicts the total weight constraint (F1: total < 1.399).
This might give a new inequality coupling stratum sizes.

Option C — Turán-type inequality: The primitivity constraint defines a hypergraph. The
Turán density of divisibility-free sets might be bounded by a variant of the LYM inequality.
For the "width" of the primitive set, LYM gives sum_{a∈A} 1/|A_k| ≤ 1 (where k=Ω(a)).
If |A_k| ≥ (some bound), then this translates to sum 1/(a log a) ≤ something.

Option D — Computer search for near-extremal examples: Run proof_prepare with critics on
(try shorter proof to avoid timeout) and check if any new witness can be found.
Currently witness_valid=0 (no witness block found in proof_strategy.md).

**For next session**: Start with Option B (F2 global constraint) or Option C (LYM-type inequality).
The LYM inequality for primitive sets says: for primitive A, sum_{a∈A} 1/(a log a) is
bounded by... (LYM for posets). This requires knowing the "layer sizes" |A_k|, which connects
to our stratum density results. This might be the cleanest elementary path forward.

**qids in flight**: Q38 not yet opened. All prior qids Q1-Q37 resolved.

**Session count**: 25 rounds logged / 50 cap. 25 rounds remain.
