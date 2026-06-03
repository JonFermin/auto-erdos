---
id: spf_reduction
status: proved
depends_on: [omega_stratification]
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 2 — Smallest-prime-factor reduction (spf-reduction)

**Statement**: Let $A \subset [x, \infty)$ be a primitive set. For each prime $p$, define
$A_p = \{a \in A : \mathrm{spf}(a) = p\}$ (elements of $A$ whose smallest prime factor is $p$).
Then:
1. $A = \bigsqcup_p A_p$ (disjoint union over primes).
2. For each prime $p$, the "fiber" $B_p = \{a/p : a \in A_p\}$ is a primitive set contained
   in $[x/p, \infty)$.
3. For each $a \in A_p$: $\frac{1}{a \log a} \leq \frac{1}{p} \cdot \frac{1}{(a/p) \log(a/p)}$.
4. Consequently:
   $$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{p} \frac{1}{p} \cdot \sum_{b \in B_p} \frac{1}{b \log b}.$$

**Proof**:

(1): Every $n \geq 2$ has a unique smallest prime factor, so the $A_p$ are disjoint and cover $A$.

(2): For any $a, b \in A_p$, write $a = pa'$ and $b = pb'$ with $a' = a/p, b' = b/p$.
If $a' | b'$, then $a = pa' | pb' = b$, contradicting primitivity of $A$. So $B_p = \{a' : a \in A_p\}$
is primitive. Each $a \in A_p \subseteq [x, \infty)$ satisfies $a/p \geq x/p$, so $B_p \subseteq [x/p, \infty)$.

(3): For $a \in A_p$ with $a = pb'$ and $b' = a/p \geq x/p \geq 2$ (for $p \leq x/2$):
$$\frac{1}{a \log a} = \frac{1}{pb' \log(pb')} = \frac{1}{pb' (\log p + \log b')} < \frac{1}{pb' \log b'} = \frac{1}{p} \cdot \frac{1}{b' \log b'}.$$
The strict inequality uses $\log p > 0$.

(4): Sum over $A_p$ and sum over primes:
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_p \sum_{a \in A_p} \frac{1}{a \log a} \leq \sum_p \frac{1}{p} \sum_{b \in B_p} \frac{1}{b \log b}. \quad \square$$

**Corollary (recursive form)**: Define
$$M(x) = \sup_{A \subset [x, \infty),\ A \text{ primitive}} \sum_{a \in A} \frac{1}{a \log a}.$$
Then Lemma 2 gives:
$$M(x) \leq \sum_{p \text{ prime}} \frac{1}{p} \cdot M(x/p). \tag{$\star$}$$

**This is the key functional inequality for the Erdős conjecture**.
If we can show that $(\star)$ forces $M(x) \leq 1 + o(1)$ as $x \to \infty$,
the conjecture follows. This is the content of Lemma 3 (open).

**Current obstacle**: The functional inequality $(\star)$ is an IMPLICIT recursion.
To solve it, we need an ansatz for $M$. The Erdős-Zhang bound ($M(x) \leq e^\gamma \pi/4 + o(1)$
≈ 1.399) is obtained from $(\star)$ by comparing with the "prime-indexed" bound
$M_{\text{primes}}(x) = \sum_{p \geq x} 1/(p \log p) \approx 1/\log x \to 0$.
However, tightening the bound from 1.399 to 1 requires sharper analysis of $(\star)$.
