# Session handoff (s_0502-164339-cf5f)

**Stop reason**: Session 3 token budget. One substantive analytical
round (round 11) added Section 10 â€” Erdos-Zhang structural sketch.

**Round 11 main finding**

The standard Erdos-Zhang (EZ) chain has FOUR steps:

1. (EZ-1) Integral representation 1/log(a) = int_a^inf dt/(t log^2 t).
2. (EZ-2) Switch sum/integral (Tonelli â€” exact).
3. (EZ-3) Apply Behrend's theorem on Sigma_A(t) = sum_{a in A, a<=t} 1/a.
4. (EZ-4) Integrate the bound â€” yields e^gamma pi/4.

Steps 1, 2, 4 are exact. Step 3 is the only locus of potential slack:
Behrend's bound is sharp pointwise, but a single primitive A cannot
saturate it at EVERY t simultaneously. F3 quantifies this:
S(A_k) = 1 - c k^2/2^k is BELOW Behrend's pointwise integral.

**Restated CST conjecture (stratum-aware Behrend)**

For primitive A, t |-> Sigma_A(t) cannot saturate Behrend's worst case
at every t. If it saturates near t_0 with stratum A_{k_0}, it is
sub-saturated by at least c k_0^2/2^{k_0} at all relevant t.

If true, integrating through (EZ-4) replaces the EZ ceiling 1.399 by
1.399 - 6c * (integration_weight) â‰ˆ 1 â€” exactly the conjecture.

**State at close**

- 11 keep_progress rounds total (sessions 1+2+3).
- 11 records under records/proof_primitive_set_erdos_*.json.
- Q1-Q10 all resolved. Sections 1-10 in proof_strategy.md.
- proof_lemmas/lemma_003_cross_stratum.md has the CST conjecture.

**Suggested next move (specific now)**

The next session has a narrow target: try to either

(a) PROVE stratum-aware Behrend for a tractable special case (e.g.
    A = single stratum A_k truncated to [x, N]; verify the saturation
    bound holds), or

(b) REFUTE it by constructing a primitive A whose Sigma_A(t) does
    saturate Behrend at MULTIPLE t simultaneously across strata.

(a) is structural; (b) is empirical (a search with multi-t saturation
as the objective).

If neither pans out, document the impasse and call exit 4 round-cap
or a manual session_end "pivot to literature search needed".
