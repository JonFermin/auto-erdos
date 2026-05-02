# Session handoff (s_0502-171208-b80e)

**Stop reason**: Session 4 budget. One round (12) added Section 11 â€”
the rigorous single-stratum calculation.

**Round 12 main finding**

Sigma_{A_k}(t) ~ (log log t)^k / k!  (from Landau + partial summation,
substitution v = log log u). By Stirling, max over k attained at
k* = log log t, giving max = (log t) / sqrt(2 pi log log t) â€” exactly
Behrend's bound. So A_k saturates Behrend at the unique t where
log log t = k, and is sub-Behrend by a Gaussian factor exp(-xi^2/(2k))
elsewhere.

This SHARPENS the picture from session 3 (Section 10): single-stratum
primitive sets cannot saturate Behrend at multiple t. The
"stratum-aware" picture is rigorous on the single-stratum case; the
open question is whether multi-stratum primitive sets, after
primitivity exclusion (Section 11.4), still fail to saturate
Behrend uniformly.

**State at close**

- 12 keep_progress rounds total. Sections 1-11 in proof_strategy.md.
- Q1-Q11 resolved. lemma_003 has the CST conjecture.
- 12 records under records/.

**Suggested next move**

The most useful single next step would be a calculation of the
multi-stratum case: take A = A_{k_1} âˆª (A_{k_2} restricted by
p_min(b) <= x^{1/k_1}), compute Sigma_A(t), see if it saturates
Behrend at any t. Likely answer: no â€” the p_min restriction prunes
A_{k_2} so heavily that the union is still sub-Behrend everywhere.

Failing that: accept that this is at the edge of what the autonomous
loop can do without literature. Document the Section-11 partial
result as the loop's stopping point. Run exit-4 by hitting the round
cap (currently 50; 12 used).
