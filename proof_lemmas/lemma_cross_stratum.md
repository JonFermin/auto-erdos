---
id: cross_stratum
status: open
depends_on: [stratum_tail]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma: Cross-stratum primitivity constraint

**Statement** (target): For a primitive set $A \subset [x, \infty)$, the
combined contribution

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^\infty \sum_{\substack{a \in A \\ \Omega(a)=k}} \frac{1}{a \log a}$$

satisfies the bound $< 1 + o(1)$ as $x \to \infty$.

**Why lemma `stratum_tail` is not enough**: Lemma `stratum_tail` shows
$\sum_k S_k(x) \leq 1 + o(1)$, where $S_k(x)$ is the sum over ALL of $A_k \cap [x, \infty)$. But $A$ can use at most a subset of each stratum. The inequality

$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_k S_k(x) \approx 1 + o(1)$$

is NOT directly useful because $\sum_k S_k(x) = 1 + o(1)$ is tight — the
bound is exactly 1, and we need STRICT less than to prove the conjecture.
The primitivity of $A$ must force some slack.

**Key observation**: In a primitive set $A$, if $a \in A$ with $\Omega(a) = k$,
then no multiple $ma$ (for integer $m \geq 2$) can be in $A$. In particular:
- If $a \in A_k' := A \cap A_k$ and $p$ is any prime, then $pa \notin A$
  (since $a | pa$). So each element $a$ of $A_k'$ "blocks" infinitely many
  elements from higher strata.

**Approach via Erdős's original argument**:
Erdős's 1935 proof of the upper bound (F1) used: for each prime $p$, let
$f(p) = \{a \in A : p \text{ is the smallest prime factor of } a\}$. The sets
$f(p)$ partition $A$. For each $p$, the set $f(p)$ is a primitive set of
integers whose smallest prime factor is $p$, hence each element is $\geq p$.
Erdős showed $\sum_{a \in f(p)} 1/(a \log a) \leq 1/(p \log p)$ via a clever
induction on the largest element.

If this bound $\sum_{a \in f(p)} 1/(a \log a) \leq 1/(p \log p)$ were proved,
then $\sum_{a \in A} 1/(a \log a) = \sum_p \sum_{a \in f(p)} \frac{1}{a \log a}
\leq \sum_p \frac{1}{p \log p} \approx 1.637$. This is exactly Zhang's F1 bound.

For the TIGHTER conjecture (bound $= 1$ instead of $1.637$): one needs to
show $\sum_{a \in f(p)} 1/(a \log a) \leq 1/(p \log p)$ with EQUALITY only
in the limit as $p \to \infty$ (where $f(p) = \{p\}$ is the extremal case).

**Obstacle**: The tighter bound requires understanding when $f(p)$ can be "dense"
near $p$, i.e., containing elements close to $p$. The conjecture says that for
large $p$ (i.e., elements in $[x, \infty)$), no such dense configuration exists.

The precise statement needed: for $A \subset [x, \infty)$ primitive,
$\sum_{a \in f(p)} 1/(a \log a) \leq (1 + o(1))/(p \log p)$ where $o(1) \to 0$
as $p \geq x \to \infty$.

**Current obstacle**: I have not found a proof of this sub-bound. The Erdős
argument gives $\leq 1/(\log p - \log\log p)$ (by a Mertens-type estimate),
which is slightly larger than $1/(p \log p)$. Closing the gap between
$1/(p \log p)$ and $1/(p(\log p - \log \log p))$ seems to require the
main difficulty of the conjecture.
