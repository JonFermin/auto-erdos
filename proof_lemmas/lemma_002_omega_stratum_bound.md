---
id: omega_stratum_bound
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 2 — Omega-stratum contribution bound for restricted sets

**Statement (conjectured).** Let $A_k^x = \{a \in [x, \infty) : \Omega(a) = k\}$
be the $k$-th Omega-stratum restricted above $x$. Then
$$f(A_k^x) := \sum_{a \in A_k^x} \frac{1}{a \log a} \leq g(x, k)$$
for some explicit $g(x, k)$ with $\sum_{k \geq 1} g(x, k) \leq 1 + o(1)$.

**Why this would suffice.** If we can bound each stratum contribution $f(A_k^x)$
by $g(x, k)$ such that the sum over $k$ is $\leq 1 + o(1)$, then for any
primitive $A \subset [x, \infty)$:
$$f(A) = \sum_{k \geq 1} f(A_k^x \cap A) \leq \sum_{k \geq 1} f(A_k^x) \leq \sum_{k \geq 1} g(x, k) \leq 1 + o(1).$$
(The second inequality uses $A_k^x \cap A \subseteq A_k^x$, so the sum
over a subset is at most the full stratum sum.)

**What we know (from F3).** For the FULL stratum $A_k^0 = \{n \geq 1 : \Omega(n) = k\}$,
$f(A_k^0) = 1 - (c + o(1)) k^2/2^k$ with $c \approx 0.0656 > 0$. Summing
over $k$: $\sum_{k \geq 1} f(A_k^0) = \sum_k (1 - (c+o(1))k^2/2^k)$ diverges
(infinitely many terms, each close to 1). So the FULL stratum approach does
not directly bound the sum for restricted sets.

**Key difficulty.** For the restricted stratum $A_k^x$, the contribution of
each element $a \in A_k^x$ is $1/(a \log a)$ where $a \geq x$. Hence each
term is $\leq 1/(x \log x)$. The count $|A_k^x \cap [x, 2x]|$ can be
estimated by the Selberg-Delange method: roughly
$$|\{a \in [x, 2x] : \Omega(a) = k\}| \approx \frac{x}{\log x} \cdot \frac{(\log \log x)^{k-1}}{(k-1)!}.$$
So
$$f(A_k^x \cap [x, 2x]) \approx \frac{x}{\log x} \cdot \frac{(\log \log x)^{k-1}}{(k-1)!} \cdot \frac{1}{x \log x} = \frac{(\log \log x)^{k-1}}{(k-1)! \log^2 x}.$$
Summing over dyadic intervals $[2^j x, 2^{j+1} x]$ for $j = 0, 1, 2, \ldots$
and over $k$:
$$f(A_k^x) \lesssim \frac{1}{\log^2 x} \sum_{j \geq 0} \frac{(\log \log(2^j x))^{k-1}}{(k-1)! \cdot 2^j} \approx \frac{(\log \log x)^{k-1}}{(k-1)! \log^2 x} \cdot \frac{2^j x / x}{2^j}.$$
This estimate is getting complicated. Summing over all $k$:
$$\sum_{k \geq 1} f(A_k^x) \lesssim \frac{e^{\log \log x}}{\log^2 x} = \frac{\log x}{\log^2 x} = \frac{1}{\log x} \to 0.$$

Wait — this estimate gives $\sum_k f(A_k^x) \lesssim 1/\log x \to 0$, which
would actually PROVE the conjecture (the sum over all $k$ is $\leq 1/\log x$)!
But this analysis is rough and has errors. Let me flag the obstacles.

**Current obstacle.** The Selberg-Delange approach gives the SUM over all
elements of $A_k^x$ (not restricted to a primitive set). A primitive set
$A \cap A_k^x$ is a SUBSET of $A_k^x$, so $f(A \cap A_k^x) \leq f(A_k^x)$.
The upper bound $\sum_k f(A_k^x) \lesssim 1/\log x$ would suffice!

But the careful calculation above might have errors in the dyadic-sum
estimates. In particular: the $1/\log^2 x$ factor vs. the sums that
might sum to $\log x$, giving $1/\log x$. Need to track constants carefully.

**Next step.** Make the Selberg-Delange estimate rigorous for a fixed $k$, then
sum carefully over $k$. Alternatively, cite the Granville-Koukoulopoulos (2022)
paper which reportedly proved the tighter bound $f(A) \leq f(\mathcal{P}_x)$
for primitive $A \subset [x, \infty)$, which itself equals $\sim 1/\log x \to 0$.
If that result is in the literature, we can cite it as a "given" (if it's in
the ledger) or note it as an open problem (if not in the ledger).
