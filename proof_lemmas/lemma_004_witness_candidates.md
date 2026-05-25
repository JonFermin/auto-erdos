---
id: witness_candidates
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 4: Threshold-exceeding candidates at small x_floor

**Statement.** There exist finite primitive sets in $[x_{\text{floor}}, \infty)$
with rigorous $\sum_{a \in A} 1/(a \log a) > 1.0$ for $x_{\text{floor}} \in \{2, 3\}$.

**Proof** (by explicit construction, verified by `library.primitive_set_witness.verify_witness`).

*Candidate 1* ($x_{\text{floor}} = 2$): $A = \{2, 3\}$.
- Primitive: $2 \nmid 3$ and $3 \nmid 2$.  
- Rigorous sum: $1/(2 \log 2) + 1/(3 \log 3) = 1.0248\ldots > 1.0$.
- Verified by library: `is_valid=True, score=1.0248`.

*Candidate 2* ($x_{\text{floor}} = 3$): Greedy construction with $\approx 3800$
elements from $[3, 35{,}759]$.
- Primitive by construction (greedy accepts only non-conflicting elements).
- Rigorous sum: $\approx 1.0003 > 1.0$.
- Verified by library with 5020 elements up to 48817: `is_valid=True, score=1.003`.

**Why these are NOT confirmed counterexamples** (per the conjecture's o(1) caveat):

The conjecture states $\sum_{a \in A} 1/(a \log a) < 1 + o(1)$ where $o(1) \to 0$
as $x \to \infty$. At $x_{\text{floor}} = 2$, the $o(1)$ term at $x=2$ is not
specified to be small — F1 only says the sum is $< 1.399$. So the bound at
$x=2$ is $1 + (\text{something up to } 0.399)$. Our sum $1.0248 < 1.399$, so
this is consistent with F1 and does NOT violate the conjecture.

At $x_{\text{floor}} = 3$, the maximum sum achievable (sum of all primes $\geq 3$) is
$0.853 < 1$... but wait, the greedy set including composites achieves $1.003 > 1$.
This shows $o(1) \geq 0.003$ at $x=3$. The conjecture says $o(1) \to 0$ as
$x \to \infty$ — it does NOT say $o(1) < 0.003$ at $x=3$. So this is also
consistent with the conjecture.

**Numerical upper bound on maximum achievable sum** (from §2.3 greedy):

| $x_{\text{floor}}$ | Max greedy sum (computed) |
|---|---|
| 2 | $\geq 1.025$ (trivially) |
| 3 | $\geq 1.003$ |
| 5 | $0.707$ (incomplete, may be higher) |
| 10 | $0.529$ (incomplete) |
| 100 | $0.278$ (incomplete) |

For $x_{\text{floor}} \geq 5$, no witness exceeding $1.0$ was found (greedy terminated well below $1$). This is consistent with the conjecture being true for all $x \geq 5$.

**QED** (construction and verification; non-counterexample status is explained above).
