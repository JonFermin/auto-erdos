---
id: zhang_extremal
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 4
---

## Lemma zhang_extremal: Zhang's Extremal Bound and Its Implications

**Statement (F1, Zhang 1993)**: For any primitive set $A \subseteq [x, \infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399,
\quad x \to \infty.$$

**What this does for the conjecture**: F1 establishes a non-trivial finite
upper bound on the sum, but the Erdős conjecture posits a tighter bound of $1$.
The gap between $1.399$ and $1$ is the mathematical content that remains open.

**Connection to primes**: A result closely related to Zhang is that the prime
set $A_1$ appears to extremize $f(A) = \sum_{a \in A} 1/(a \log a)$ over all
primitive $A \subseteq \mathbb{N}$: $f(A_1) \approx 1.637 > 1.399$. Note that
$f(A_1) > 1.399$ because $A_1$ includes small primes ($x_{\rm floor} = 2$), so
F1 does not directly bound $f(A_1)$.

**Key implication**: the "1" in the Erdős conjecture corresponds to the
asymptotic behavior: for primes $\geq x$, $\sum_{p \geq x} 1/(p \log p) \approx
1/\log x \to 0$. The supremum over all primitive $A \subseteq [x, \infty)$
should converge to 1 (not 0) because one can always use a "dense" primitive
set (e.g., all integers in $[x, 2x)$) to get sum $\approx 1/\log x$, then
combine with $A_k$ for large $k$ (which are asymptotically more efficient).

**Current obstacle**: The gap between F1's $1.399$ bound and the conjecture's
bound of $1$ has not been closed. Improving F1 to any bound $< 1.399$ for
primitive $A \subseteq [x, \infty)$ would be progress; getting to $1$ is the
conjecture. The known proof techniques (Mertens-type product estimates, sieve
methods) yield F1 but not the conjectured 1.
