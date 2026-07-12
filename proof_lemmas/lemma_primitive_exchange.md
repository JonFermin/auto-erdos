# Lemma: primitive_exchange (counting-function dominance)

**Status**: open (key claim unproved; approach identified)
**Session**: s_0712-110453-a069 (Q11)
**Depends on**: globally_unblocked_size, fiber_sum_bound

---

## Integral representation

For any primitive $A \subset [x, \infty)$ and any $T > x$:
$$\sum_{a \in A} \frac{1}{a \log a}
= \int_x^{\infty} N_A(t)\,\frac{dt}{t \log^2 t}$$
where $N_A(t) := |\{a \in A : a \leq t\}|$ (the counting function of $A$).

**Proof**: Summation by parts / Abel's summation. Let $f(t) = 1/(t\log t)$. Then
$f'(t) = -(1+\log t)/(t \log t)^2 \approx -1/(t\log^2 t)$ for large $t$.
Abel's summation gives
$$\sum_{a \in A} f(a) = N_A(t)f(t)\Big|_{x^-}^{\infty} + \int_x^\infty N_A(t)(-f'(t))\,dt
= \int_x^\infty N_A(t)\,\frac{dt}{t\log^2 t}.$$
(The boundary term at $\infty$ vanishes since $N_A(t)/\log t \to 0$.)

---

## Key claim (open): counting-function dominance

**Claim $D_{k_0}$**: For all $t \geq x$:
$$N_A(t) \leq N_{B_{k_0}(x)}(t)$$
where $B_{k_0}(x) = \{n \geq x : \Omega(n) = k_0\} \cup \{n \in [x, x^{(k_0+1)/k_0}) : \Omega(n) = k_0+1,\;n \text{ globally } k_0\text{-unblocked}\}$
is the exchange construction.

**Consequence of $D_{k_0}$**: If Claim $D_{k_0}$ holds, then
$$\sum_{a \in A}\frac{1}{a\log a}
= \int_x^\infty N_A(t)\frac{dt}{t\log^2 t}
\leq \int_x^\infty N_{B_{k_0}(x)}(t)\frac{dt}{t\log^2 t}
= \sum_{b \in B_{k_0}(x)}\frac{1}{b\log b} \leq 1 + \frac{1}{k_0} = 1 + o(1).$$
This would CLOSE the conjecture.

---

## Evidence for $D_{k_0}$

**Small-$t$ regime** ($t \in [x, 2x)$): Elements of $A$ in $[x, 2x)$ with $\Omega(a) = k_0+1$
are globally $k_0$-unblocked (proof: any $k_0$-almost prime divisor $d$ of $a$ satisfies
$d = a/p \leq a/2 < x$, so no $k_0$-almost prime divisor $\geq x$ exists). Hence
$A \cap [x, 2x) \subset \{k_0\text{-almost primes}\} \cup \{(k_0+1)\text{-almost primes, unblocked}\} = B_{k_0}(x)$.
So $N_A(t) \leq N_{B_{k_0}(x)}(t)$ for $t \in [x, 2x)$ iff $A \cap [x, t] \subset B_{k_0}(x)$.
Since $A$ is primitive and all its elements in $[x,t]$ are in $B_{k_0}(x)$ for this range, $D_{k_0}$ holds in $[x, 2x)$.

**Obstacle at $t \geq 2x$**: Elements of $A$ with $\Omega(a) \geq k_0+2$ or globally $k_0$-blocked
$(k_0+1)$-almost primes appear at $t \geq 2x$. These are NOT in $B_{k_0}(x)$, so they increase
$N_A(t)$ beyond $N_{B_{k_0}(x)}(t)$. The claim $D_{k_0}$ would require showing these "extra"
elements of $A$ at $t \geq 2x$ are compensated by missing elements of $B_{k_0}(x)$ at those $t$-values —
specifically, that $A$ has fewer $k_0$-almost primes than $B_{k_0}(x)$ (which has ALL of them).

---

## Reduction: sufficient condition for $D_{k_0}$

**Sufficient condition**: For every $t \geq 2x$, the number of $k_0$-almost primes absent from
$A \cap [x, t]$ (i.e., in $B_{k_0}(x) \setminus A$, up to $t$) is at least the number of
"extra" elements of $A \cap [x, t]$ not in $B_{k_0}(x)$.

Let $M(t) = N_{B_{k_0}(x)}(t) - N_A(t)$. We want $M(t) \geq 0$ for all $t$. The increment is:
$$\Delta M(t) = \mathbf{1}[t \in B_{k_0}(x)] - \mathbf{1}[t \in A].$$

$M(t)$ increases when an element of $B_{k_0}(x) \setminus A$ is "hit" (missing from $A$ but
in $B_{k_0}$) and decreases when an element of $A \setminus B_{k_0}(x)$ is "hit".

The claim $D_{k_0}$ asks: does $M(t) \geq 0$ hold for all $t$?

For each $b \in A \setminus B_{k_0}(x)$ (an "extra" element), primitivity of $A$ forces the
absence of some $d \in B_{k_0}(x) \setminus A$ with $d < b$ (either $d | b$ or... actually
$d | b$ is the correct constraint if $d$ is a $k_0$-almost prime). So each extra element $b$
forces at least one "compensating" absent $d < b$. This means $M(b^-) \geq 1$ before $b$
is counted, then $M$ decrements by 1 at $b$, ending at $M(b) \geq 0$.

**This argument proves $D_{k_0}$** provided each extra $b \in A \setminus B_{k_0}(x)$ forces
at least one absent $d \in B_{k_0}(x) \setminus A$ with $d < b$!

---

## Does each extra element force an absent $k_0$-almost prime?

**Case 1**: $b \in A$ with $\Omega(b) = k_0 + 1$ and $b$ globally $k_0$-blocked.
Then some $k_0$-almost prime $d \geq x$ with $d | b$ satisfies $d \notin A$ (by primitivity,
since $d | b$ and $b \in A$). And $d < b$ (since $d | b$ and $b \neq d$). So $d \in B_{k_0}(x)
\setminus A$ with $d < b$. ✓ ($D_{k_0}$ holds for this case.)

**Case 2**: $b \in A$ with $\Omega(b) = k_0 + 1$ and $b \geq x^{(k_0+1)/k_0}$.
Lemma `large_elements_blocked` says $b$ is globally $k_0$-blocked, so Case 1 applies. ✓

**Case 3**: $b \in A$ with $\Omega(b) \geq k_0 + 2$.
Then $b$ has at least $k_0+2$ prime factors. Consider any $k_0$ of them: their product $d$ is
a $k_0$-almost prime $\geq 2^{k_0} = x$ (approximately). More precisely: choose the
$k_0$ SMALLEST prime factors of $b$ (counting multiplicity): $d = p_1 \cdots p_{k_0}$. Then
$d \leq b / p_{k_0+1} \leq b / 2 < b$. Is $d \geq x$? We need $d = p_1 \cdots p_{k_0} \geq x$.
Since $b \geq x$ and $b = d \cdot p_{k_0+1} \cdots p_{k_0+\ell}$ for $\ell \geq 2$ extra factors
(each $\geq 2$), we have $d = b/(p_{k_0+1}\cdots p_{k_0+\ell}) \leq b/4 < b$. But $d \geq x$
requires $b \geq 4x$ (roughly).

For $b \in [x, 4x)$ with $\Omega(b) \geq k_0+2$: there may be NO $k_0$-almost prime divisor
$d \geq x$ of $b$. In this range, $D_{k_0}$ may fail!

---

## Failure example for Case 3

Let $k_0 = 3$, $x = 8 = 2^3$. Consider $b = 2^5 = 32 \in [8, 4\cdot 8) = [8, 32]$
(boundary case). $\Omega(b) = 5 = k_0+2$. The $3$-almost prime divisors of $b$ are:
$2^3 = 8 \geq x$ ✓. So $d = 8 \in B_{k_0}(x) \setminus A$ (forced by $b \in A$).
So Case 3 works here.

Take $b = 12 = 2^2 \cdot 3 \in [8, 32)$. $\Omega(b) = 3 = k_0$. This is a $k_0$-almost prime itself,
so $b \in B_{k_0}(x)$. No problem.

Take $b = 24 = 2^3 \cdot 3 \in [8, 32)$. $\Omega(b) = 4 = k_0+1$, $b \geq 8 = x$.
$3$-almost prime divisors of $b$: $\{8, 12\}$. $8 \geq x = 8$ ✓, $12 \geq 8$ ✓.
So $24 \in A$ forces $8 \notin A$ or $12 \notin A$ (both? no, it forces both $8, 12 \notin A$
since $8|24$ and $12|24$). Either way, some $3$-almost prime $\geq x$ is absent from $A$. ✓

The Case 3 obstacle appears only for $b \in [x, 4x)$ with $\Omega(b) = k_0+2$ and
where ALL $k_0$-almost prime divisors of $b$ are $< x$. For $b = p_1\cdots p_{k_0+2}$ with all
$p_i$ small: product of any $k_0$ of them is $b/(p_{k_0+1} p_{k_0+2}) \leq b/4 < x$ iff $b < 4x$.
So the issue is $b \in [x, 4x)$ with ALL prime factors small (all $p_i$ close to 1). But prime
factors are $\geq 2$, so $b \geq 2^{k_0+2} = 4 \cdot 2^{k_0} \geq 4x$. So Case 3 cannot occur
in $[x, 4x)$! Because $\Omega(b) \geq k_0+2$ and $b \geq x$ already implies $b \geq 2^{k_0+2} \geq 4x$.

**Conclusion**: Case 3 never occurs in $[x, 4x)$ because $\Omega(b) \geq k_0+2$ with all
prime factors $\geq 2$ forces $b \geq 2^{k_0+2} \geq 4 \cdot 2^{k_0} \geq 4x$. And for
$b \geq 4x$ with $\Omega(b) \geq k_0+2$: choosing the $k_0$ smallest factors gives
$d = b/(p_{k_0+1}\cdots p_{\Omega(b)}) \leq b/4 < b$ but $d \geq ?$. We need $d \geq x$.
$d = b/(\text{product of extra factors}) \geq b/b^{?} ...$

Actually: for $b \geq 4x$ with $\Omega(b) = k_0+2$, the product of the two largest factors
is $\geq x$ (since $b/(p_1\cdots p_{k_0}) = p_{k_0+1}p_{k_0+2} \leq b/1 = b$, but
$p_1\cdots p_{k_0} \geq 2^{k_0} = x$). Wait: smallest $k_0$ factors $p_1 \leq p_2 \leq \cdots \leq p_{k_0}$ satisfy
$p_1\cdots p_{k_0} \leq b/p_{k_0+1}/p_{k_0+2} \leq b/4$. For this to be $\geq x$: $b/4 \geq x$
i.e. $b \geq 4x$. ✓ So for $b \geq 4x$ with $\Omega(b) = k_0+2$, the smallest-$k_0$-factor
product $d = p_1\cdots p_{k_0} \geq x$ (since $d \cdot p_{k_0+1} p_{k_0+2} = b \geq 4x$ and
$p_{k_0+1}, p_{k_0+2} \leq \sqrt{b}$ at most... hmm, this is not tight).

Let me verify: $b \geq 4x$ and $\Omega(b) = k_0+2$. Write $b = p_1\cdots p_{k_0} \cdot q_1 \cdot q_2$
with $q_1 \leq q_2$ (the two largest prime factors). Then $d_0 := p_1\cdots p_{k_0} = b/(q_1 q_2)$.
Is $d_0 \geq x$? We need $b/(q_1 q_2) \geq x$, i.e., $q_1 q_2 \leq b/x \leq b/x$. We know $q_1 q_2 \leq b/2^{k_0} \leq b/x$. ✓

So $d_0 = b/(q_1 q_2) \geq x$ whenever $q_1 q_2 \leq b/x$. Since $q_1 q_2 \leq b/2^{k_0} = b/x$ (as $2^{k_0} \leq x$), this holds! So in Case 3, $d_0 \geq x$. ✓

---

## Theorem: $D_{k_0}$ holds (sketch)

**Statement**: For any primitive $A \subset [x, \infty)$ and $k_0 = \lfloor \log_2 x \rfloor$:
$N_A(t) \leq N_{B_{k_0}(x)}(t)$ for all $t \geq x$.

**Proof sketch**:
For each $b \in A \setminus B_{k_0}(x)$, define $d(b)$ as the product of the $k_0$ smallest prime
factors of $b$ (counting multiplicity). We showed:
- $d(b) < b$ (since $b$ has more than $k_0$ prime factors),
- $d(b) \geq x$ (since $d(b) = b/(q_1\cdots q_\ell) \geq b/2^{\Omega(b)-k_0} \geq b/2^{\Omega(b)} \cdot 2^{k_0} \geq x$ — wait this needs verification),
- $d(b) \notin A$ (since $d(b) | b$ and $b \in A$ with $b \neq d(b)$; primitivity).

So $\phi: b \mapsto d(b)$ maps $A \setminus B_{k_0}(x) \to B_{k_0}(x) \setminus A$ with $d(b) < b$.

If $\phi$ is injective, then by an exchange argument $M(t) = N_{B_{k_0}(x)}(t) - N_A(t)$
decrements at each $b \in A \setminus B_{k_0}(x)$ only after having incremented at $d(b) < b$,
so $M(t) \geq 0$ for all $t$.

**Key gap**: Injectivity of $\phi$ (different elements of $A \setminus B_{k_0}$ may share the
same $d(b)$ image). This fails if two elements $b, b' \in A \setminus B_{k_0}$ have the same
$k_0$ smallest prime factors, i.e., $d(b) = d(b')$. In that case both $b$ and $b'$ block the
same $d \in B_{k_0}$, but $M(t)$ decrements twice at $b, b'$ while only incrementing once at $d$.

**Recovery**: If $\phi$ is not injective, then $d(b) = d(b') = d$ and $d | b$, $d | b'$.
Since $A$ is primitive: $b \nmid b'$ and $b' \nmid b$. But $b = d \cdot m$ and $b' = d \cdot m'$
with $m, m'$ coprime to each other (else one would divide the other). The sum $\sum_{b: d(b) = d} 1/(b\log b) \leq T_1(2)/d$ (fiber bound). The "decrement" to $M$ from all $b$'s with $d(b)=d$
is $|F_{k_0}(d, A \setminus B_{k_0})|$ (could be $\geq 2$), while the "increment" from $d$ is $1$.
So $M$ can go negative if $|F_{k_0}(d, A \setminus B_{k_0})| \geq 2$ for some $d$.

**Conclusion**: Claim $D_{k_0}$ (as stated) is FALSE in general. A single absent $k_0$-almost
prime $d$ can be "shared" by multiple elements of $A \setminus B_{k_0}$, causing $M(t)$ to go
negative. A weaker comparison is needed.

---

## Revised approach: weighted dominance

Instead of $N_A(t) \leq N_{B_{k_0}}(t)$, try the weighted version:
$$\int_x^t N_A(s)\,\frac{ds}{s\log^2 s} \leq \int_x^t N_{B_{k_0}}(s)\,\frac{ds}{s\log^2 s}$$
for all $t$.

This is equivalent to $\sum_{a \in A, a \leq t} 1/(a\log a) \leq \sum_{b \in B_{k_0}, b \leq t} 1/(b\log b)$
for all $t$ — a pointwise bound on the partial sums.

This is a STRONGER version but may be more tractable via the exchange map $\phi$, since each
exchange decreases the weighted sum (replacing $b$ by $d(b) < b$ gives $1/(d(b)\log d(b)) > 1/(b\log b)$
— i.e.\ the exchange INCREASES the sum, not decreases). So the weighted version also fails.

**Status**: Both $N_A \leq N_{B_{k_0}}$ (counting) and $\sum_{\leq t} 1/(a\log a) \leq \sum_{\leq t} 1/(b\log b)$ (weighted) fail as literal statements. The correct bound must use the TOTAL SUM and handle the case where the fiber has multiple elements.
