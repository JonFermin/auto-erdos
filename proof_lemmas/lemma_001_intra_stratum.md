---
id: intra_stratum_bound
status: proved
depends_on: []
discharged_by_round: 4
introduced_at_round: 4
---

# Lemma: Intra-Stratum Subset Bound

**Statement.** For any set $A \subseteq \mathbb{N}$ and any integer $k \geq 1$,

$$\sum_{\substack{a \in A \\ \Omega(a) = k}} \frac{1}{a \log a} \leq \sum_{\substack{n \in \mathbb{N} \\ \Omega(n) = k}} \frac{1}{n \log n} = 1 - (c + o(1)) \frac{k^2}{2^k},$$

where $c \approx 0.0656$ is the constant from F3.

**Proof.**

The set $\{a \in A : \Omega(a) = k\}$ is a subset of $\{n \in \mathbb{N} : \Omega(n) = k\}$.
Since every term $1/(a \log a) > 0$,

$$\sum_{\substack{a \in A \\ \Omega(a) = k}} \frac{1}{a \log a} \leq \sum_{\substack{n \in \mathbb{N} \\ \Omega(n) = k}} \frac{1}{n \log n}.$$

By F3 (given fact), the right-hand side equals $1 - (c + o(1)) k^2 / 2^k$ with $c \approx 0.0656 > 0$.
This value is strictly less than 1 for all sufficiently large $k$. $\square$

**Remark.** This bound holds for any $A$ (primitivity is not required) and uses only
positivity of terms plus F3. The bound on each individual stratum is tight when $A$
contains all of $\{n : \Omega(n) = k\}$.
