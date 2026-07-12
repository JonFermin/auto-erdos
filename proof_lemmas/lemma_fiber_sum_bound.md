# Lemma: fiber_sum_bound

**Status**: proved (single-level fiber); open (multi-level total)
**Session**: s_0712-110453-a069 (Q10)
**Depends on**: large_elements_blocked, globally_unblocked_size

---

## Definitions

For any primitive $A \subset [x,\infty)$, $k \geq 1$, and $k$-almost prime $d \in [x,\infty)$
with $d \notin A$, define the **$k$-fiber of $d$ in $A$** at stratum $k+1$:
$$F_k(d, A) := \{b \in A : d \mid b,\; \Omega(b) = k+1\}.$$

Since $\Omega(d) = k$ and $d \mid b$ with $\Omega(b) = k+1$, every $b \in F_k(d,A)$
has the form $b = dp$ for some prime $p$ (one additional prime factor beyond $d$).

## Lemma `fiber_sum_bound` (proved)

**Statement**: For any primitive $A \subset [x,\infty)$, $k \geq 1$, and $k$-almost prime
$d \in [x,\infty)$ with $d \notin A$:
$$\sum_{b \in F_k(d,A)} \frac{1}{b \log b}
  = \sum_{\substack{p \;\text{prime} \\ dp \in A}} \frac{1}{dp \log(dp)}
  \;\leq\; \frac{T_1(2)}{d},$$
where $T_1(2) = \sum_{p \;\text{prime}} \frac{1}{p \log p}$ is a universal finite constant.

**Proof**: For any prime $p$: $\log(dp) = \log d + \log p \geq \log p > 0$, so
$1/(dp \log(dp)) \leq 1/(dp \log p)$. Summing over primes $p$ with $dp \in A$ (a subset of all primes):
$$\sum_{\substack{p \;\text{prime} \\ dp \in A}} \frac{1}{dp \log(dp)}
  \leq \sum_{\substack{p \;\text{prime} \\ dp \in A}} \frac{1}{dp \log p}
  \leq \frac{1}{d} \sum_{p \;\text{prime}} \frac{1}{p \log p}
  = \frac{T_1(2)}{d}. \quad \square$$

**Remark on $T_1(2)$**: By the prime number theorem, $\pi(x) \sim x/\log x$, and
partial summation gives $\sum_{p \leq x} 1/(p \log p) = O(1/\log x) \to 0$ as $x \to \infty$
(Wait: ∑_{p ≤ x} 1/(p log p) ≈ ∫_2^x dt/(t (log t)^2) = [−1/log t]_2^x → 1/log 2 as x → ∞).
So $T_1(2) = \sum_p 1/(p \log p) = 1/\ln 2 + O(1)$ (finite). The exact value is irrelevant;
what matters is finiteness.

---

## Corollary: total fiber sum over all blocking $d$'s at stratum $k+1$

Summing over all $k$-almost primes $d \geq x$ with $d \notin A$:
$$\sum_{\substack{d \geq x,\;\Omega(d)=k \\ d \notin A}} \sum_{b \in F_k(d,A)} \frac{1}{b \log b}
  \leq \sum_{\substack{d \geq x,\;\Omega(d)=k \\ d \notin A}} \frac{T_1(2)}{d}
  \leq T_1(2) \cdot \sum_{\substack{d \geq x \\ \Omega(d)=k}} \frac{1}{d}.$$

**Obstacle**: The sum $\sum_{d \geq x, \Omega(d)=k} 1/d$ is NOT bounded by $T_k(x)$ in a
useful way. Specifically:
$$\sum_{\substack{d \geq x \\ \Omega(d)=k}} \frac{1}{d}
  = \sum_{\substack{d \geq x \\ \Omega(d)=k}} (\log d) \cdot \frac{1}{d \log d}
  \leq (\log \text{max}\{d : ...\}) \cdot T_k(x),$$
but $\log d$ is UNBOUNDED as $d$ ranges over $k$-almost primes, so this bound is vacuous.

The correct comparison: for $k = k_0 = \lfloor \log_2 x \rfloor$, the $k_0$-almost primes
$d \geq x$ start at $d \approx x$ (since $2^{k_0} \approx x$). The sum $\sum_{d \geq x,
\Omega(d)=k_0} 1/d$ is related to (but larger than) $T_{k_0}(x)$ by a factor of $\approx \log x$.
Multiplied by $T_1(2) \approx 1/\ln 2 \approx 1.44$, this gives a bound of $\approx 1.44 \log x$
on the total blocked sum — which DIVERGES as $x \to \infty$. The fiber approach is therefore
insufficient to close the conjecture.

---

## Where the fiber approach fails

The fundamental issue: the fiber approach bounds the contribution of EACH blocking prime $d$
separately by $T_1(2)/d$. But the SUM of $T_1(2)/d$ over all $k_0$-almost primes $d \geq x$
is approximately $T_1(2) \cdot \sum_{d \geq x, \Omega(d)=k_0} 1/d$, which is $\Omega(\log x)$
(diverges). A multiplicative improvement by a factor $1/\log x$ would be needed to close the gap.

Such an improvement would require using the PRIMITIVE STRUCTURE more globally: not just that
each individual fiber is small ($\leq T_1(2)/d$), but that the TOTAL collection of blocked
elements across all fibers is controlled. The fiber approach treats each $d$ independently
and loses the cross-fiber primitivity constraint.

---

## What the fiber bound does give

The Lemma `fiber_sum_bound` implies: for each $k$-almost prime $d \geq x$ with $d \notin A$,
the "missed budget" from $d$ being absent from $A$ (i.e., $0$ instead of $1/(d \log d)$)
covers AT MOST $T_1(2)/d / (1/(d \log d)) = T_1(2) \cdot \log d$ units of fiber contribution.

For small $d \approx x$: $T_1(2) \cdot \log x$ units per missing $d$. The total for all
missing $d$'s in $[x, 2x)$ (at most $T_{k_0}(x) \cdot (2x \log x / 1)$ of them... this is
getting circular).

**Conclusion**: The fiber bound is proved but is insufficient to close Q10. A new approach
is needed for the total blocked sum. See Q11 for the proposed global weight argument.
