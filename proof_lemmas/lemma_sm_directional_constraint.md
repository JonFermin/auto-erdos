---
id: sm_directional_no_div
status: proved
depends_on: []
discharged_by_round: 6
introduced_at_round: 6
---

# Lemma: Upward cross-$p$ divisibility is structurally forbidden

**Statement**: Let $A \subset [x, \infty)$ be any set of integers (not
necessarily primitive), and let $p < q$ be distinct primes both $< x$.
For any $a \in A$ with $p_{\min}(a) = p$ and any $a' \in A$ with
$p_{\min}(a') = q$, we have $a \nmid a'$.

**Proof**:

Write $a = pb$ where $b = a/p$ and $p_{\min}(b) \geq p$. Write $a' = qb'$
where $b' = a'/q$ and $p_{\min}(b') \geq q$.

Suppose for contradiction that $a \mid a'$, i.e.\ $pb \mid qb'$.
Then $p \mid qb'$.

Since $p$ is prime, either $p \mid q$ or $p \mid b'$.

- $p \mid q$: impossible since $p < q$ and $q$ is prime, so the only
  positive divisors of $q$ are $1$ and $q$; as $p \geq 2 > 1$ and $p < q$,
  we have $p \nmid q$.

- $p \mid b'$: impossible since $p_{\min}(b') \geq q > p$, meaning $p$ is
  strictly smaller than every prime factor of $b'$, so $p \nmid b'$.

Both cases yield a contradiction, so $pb \nmid qb'$, i.e.\ $a \nmid a'$. $\square$

**Note**: This proof uses no primitivity assumption on $A$. The constraint
is purely structural: the minimum prime factors $p < q$ force divisibility
to be impossible in the upward direction.

**Directional asymmetry**:

- **Upward** ($p < q$): $a \nmid a'$ is STRUCTURAL (this lemma).
- **Downward** ($p < q$): $a' \nmid a$ requires PRIMITIVITY of $A$ (not structural).

**What downward divisibility would require**: If $qb' \mid pb$ with $p < q$,
then since $\gcd(q, p) = 1$ (distinct primes) we get $q \mid b$. And since
$p < q \leq p_{\min}(b')$ gives $p \nmid b'$ and $p \nmid q$, we get
$\gcd(p, qb') = 1$, so $qb' \mid b$. Since $b' \geq 2$ (proved in
`lemma_sm_prime_grouping.md`: $b' = 1$ would require $a' = q < x$,
contradicting $a' \geq x$), downward divisibility forces $b \geq qb' \geq 2q$.

**Cross-set consequence**: Primitivity of $A_{\mathrm{sm}}$ (that no element
divides another) reduces to:
- Upward ($p < q$): always satisfied structurally — no condition on $A$.
- Downward ($p < q$): $qb' \nmid b$ for all $b \in B(p)$, $b' \in B(q)$.
  Equivalently, no element of $B(p)$ is divisible by $qb'$ for any $b' \in B(q)$.

This is a cross-set sieve condition: $B(p)$ avoids the set $\{qb' : b' \in B(q)\}$
of multiples (in the divisibility sense) for all $q > p$.
