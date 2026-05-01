# Session handoff (s_0501-121629-b2a4)

**Stop reason**: Partial result reached on the worklist's full Q1-Q6.
The conjecture status remains **open**. This was the first-session
test of `AUTOERDOS_PROOF_CRITICS=0` (critics-off, witness-only mode).

**What this session produced**

- proof_strategy.md, Sections 1-6 (final partial-result form):
  setup, F3 numerical evidence, prime-tail decay, witness search,
  Omega-stratification structure with three lemmas, status & gap
  summary.
- proof_lemmas/lemma_001_truncated_low_strata.md (status: open)
- proof_lemmas/lemma_002_high_strata_below_one.md (status: open)
- proof_lemmas/lemma_003_cross_stratum.md (status: open) â€” the gap.
- 6 keep_progress rows in proof_results.tsv (one crash row at tail
  from a convergence-detection probe; ignore on resume).
- 6 records under records/proof_primitive_set_erdos_*.json.

**Key findings worth remembering**

- F3 ($S(A_k) = 1 - (c+o(1)) k^2/2^k$) is **asymptotic in $k$**, not
  a finite-$k$ identity. At $k=1$, $S(A_1) = S(\mathcal{P})
  \approx 1.6366$, the prime constant â€” completely violating the
  formula. The conjecture survives because truncation to $[x,
  \infty)$ kills the small-prime tail at rate $O(1/\log x)$.
- Witness search is empirically negative at $x \in \{100, 10^3,
  10^4\}$: largest sum found was $S \approx 0.32$ via a
  smallest-first greedy primitive sieve over $[100, 10^7]$.
- The conjecture reduces to **Lemma 3** (`cross_stratum_primitivity`),
  which IS the conjecture itself. Per-stratum bounds (Lemmas 1, 2)
  cannot close it because $\sum_k S(A_k)$ diverges â€” primitivity must
  be exploited cross-stratum, and the standard ErdÅ‘s-Zhang
  log-Mertens weighting saturates at $1.399$, not $1$.

**Critics-off mode tested**

Every round ran in <0.001s wall-clock through `proof_prepare.py`
(skipping the five LLM critics). The witness verifier and the
resolution-string defense-in-depth in `_compute_verdict_hint` both
remained active and behaved as expected: every commit-without-witness
got `witness_valid=0`; the body never tripped resolution-strings, so
verdict was `open` or `partial_result` throughout.

**Suggested next move (on resume)**

If extending: attack the candidate weighting plan in
`proof_lemmas/lemma_003_cross_stratum.md` â€” a stratum-aware weight
that rescales each $a \in A^{(k)}$ by the F3 deficit $(1 - c k^2/2^k)$
and seeks a global bound. This is the most promising opening, though
likely the missing technique is more subtle.

If declaring done: run the archive block in the skill's Step 5. The
partial-result records are kept under records/.
