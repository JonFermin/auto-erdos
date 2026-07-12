# Lemma: large_elements_blocked (converse of globally_unblocked_size)

**Status**: proved
**Session**: s_0712-110453-a069 (Q9)
**Depends on**: globally_unblocked_size

---

## Statement

Fix $k \geq 1$ and $x \geq 2$. If $b \geq x^{(k+1)/k}$ and $\Omega(b) \geq k+1$, then $b$
is globally $k$-blocked: some $k$-almost prime $d \in [x,\infty)$ divides $b$.

## Proof

Contrapositive of Lemma `globally_unblocked_size`. That lemma states: if $b \geq x$,
$\Omega(b) \geq k+1$, and no $k$-almost prime in $[x,\infty)$ divides $b$, then $b < x^{(k+1)/k}$.

Taking the contrapositive: if $b \geq x^{(k+1)/k}$ and $\Omega(b) \geq k+1$, then some
$k$-almost prime $d \in [x,\infty)$ divides $b$. $\square$

## Consequence: Universal element bound

Combining with Lemma `globally_unblocked_size`:

- Every $b \in [x,\infty)$ with $\Omega(b) \geq k+1$ is either (i) globally $k$-unblocked,
  in which case $b < x^{(k+1)/k}$, or (ii) globally $k$-blocked by some $d \in [x,\infty)$
  with $\Omega(d) = k$.

This dichotomy holds for every primitive $A \subset [x,\infty)$ and every element $b \in A$
with $\Omega(b) \geq k+1$.

## Universal interval bound (proved)

For any primitive $A \subset [x,\infty)$ and $k \geq 1$:
$$\sum_{\substack{a \in A \\ \Omega(a) \geq k+1}} \frac{1}{a \log a}
  = \underbrace{\sum_{\substack{a \in A,\;\Omega(a) \geq k+1 \\ a \text{ globally } k\text{-unblocked}}}}_{\leq\; 1/k \;\text{(Lemma globally\_unblocked\_sum)}}
  + \underbrace{\sum_{\substack{a \in A,\;\Omega(a) \geq k+1 \\ a \text{ globally } k\text{-blocked}}}}_{\text{(open)}}.$$

The unblocked sum is bounded. The blocked sum remains open (fiber obstacle: multiple elements
of $A$ can share a blocking $k$-almost prime $d \notin A$, and the fiber
$\{b \in A : d \mid b\}$ can sum to more than $1/(d \log d)$).

## Remark on the $\Omega(b) \leq k$ case

For elements of $A$ with $\Omega(b) \leq k$, Lemma `large_elements_blocked` does not apply.
Such elements need not be globally $k$-blocked (e.g.\ a prime $p \geq x^{(k+1)/k}$ has
$\Omega(p) = 1 \leq k$ for $k \geq 1$ and is not $k$-blocked). Their sum is bounded by
$\sum_{j=1}^{k} T_j(x)$, which for fixed $k$ is $o(1)$ by Lemma `large_floor_vanish`.
