# Lemma: multistratum_bound (bounding multi-stratum primitive sets)

**Status**: partial (pure-k₀ case proved; multi-stratum obstacle documented; global weight needed)
**Session**: s_0712-110453-a069 (Q13)
**Depends on**: fiber_sum_bound, large_elements_blocked, globally_unblocked_size, cascading_removal

---

## Setup and goal

Fix $k_0 = \lfloor \log_2 x \rfloor$. We seek to prove: for any primitive $A \subset [x,\infty)$,
$$S(A) := \sum_{a \in A} \frac{1}{a \log a} \leq T_{k_0}(x) \leq 1 + \frac{1}{k_0}.$$

The lemma `cascading_removal` proved this when $A$ consists only of $k_0$-almost primes and
$(k_0+1)$-almost primes (the "pure $k_0$" case). The remaining gap is the **divisors-in-$A$ case**:
when $a \in A$ with $\Omega(a) = j < k_0$ and $a \mid d$ for some $k_0$-almost prime $d \geq x$
not in $A$.

---

## Proved: the pure-$k_0$ partial result

**Theorem (pure-$k_0$ case)**: If $A \subset \{n \geq x : \Omega(n) = k_0\}$ (all elements
of $A$ are $k_0$-almost primes), then $A$ is automatically primitive (no two $k_0$-almost primes
divide each other), and:
$$S(A) \leq T_{k_0}(x) := \sum_{\substack{n \geq x \\ \Omega(n) = k_0}} \frac{1}{n \log n}
\leq 1 + \frac{1}{k_0}.$$

The upper bound $T_{k_0}(x) \leq 1 + 1/k_0$ is established by Sathe-Selberg (see
`lemma_stratum_sub_bound.md` and Section 2 of `proof_strategy.md`).

**Proof**: Immediate, since $A \subseteq \{k_0\text{-almost primes } \geq x\}$ and no two
$k_0$-almost primes are comparable in divisibility (they have the same number of prime factors).
$\square$

---

## The divisors-in-$A$ obstacle (exchange approach fails)

**Why the cascading exchange breaks down**: In `lemma_cascading_removal.md`, the forward exchange
adds $d$ (a $k_0$-almost prime $\geq x$) while removing:
- Fiber elements: $b \in A$ with $d \mid b$, Ω(b) = k_0+1$ — removal decreases sum by
  $\leq T_1(2)/d$ (fiber_sum_bound), and the exchange net change is $> 0$ in this case.
- **Divisors**: $a \in A$ with $a \mid d$, $a \neq d$ — i.e., $\Omega(a) < k_0$ and $a \geq x$.

For the divisor case: $a \mid d$, $a < d$ (since $a \neq d$), $a \geq x$. Because $a < d$:
$$\frac{1}{a \log a} > \frac{1}{d \log d}.$$
So removing $a$ costs MORE than the gain from adding $d$, making $\Delta < 0$.

**Concrete example**: $x = 64$, $k_0 = 6$. Let $a = 2 \cdot 5 \cdot 7 = 70 \geq 64$
($\Omega(a) = 3$). Let $d = 2 \cdot 5 \cdot 7 \cdot 3 \cdot 11 \cdot 13 = 70 \cdot 429 = 30030$
($\Omega(d) = 6$). Then $a \mid d$, $1/(a \log a) \approx 1/(70 \cdot 4.25) \approx 0.00336$,
while $1/(d \log d) \approx 1/(30030 \cdot 10.3) \approx 3.2 \times 10^{-6}$.
Adding $d$ and removing $a$ is a net LOSS of $\approx 0.00336$.

**Conclusion**: Lower-stratum elements ($\Omega < k_0$) that divide absent $k_0$-almost primes
are MORE valuable per element than the $k_0$-almost primes themselves. The exchange map
$A \to (A \setminus \{a, \text{fiber}\}) \cup \{d\}$ is sum-DECREASING when $a \in A$,
$a \mid d$, $a < d$.

---

## Why A cannot overload lower strata: the global weight argument

The exchange approach fails element-by-element, but the GLOBAL structure of a primitive set
prevents $A$ from having too many lower-stratum elements.

**Key constraint**: For $a \in A$ with $\Omega(a) = j < k_0$, primitivity forces:
EVERY $k_0$-almost prime $d \geq x$ with $a \mid d$ is ABSENT from $A$.

The $k_0$-almost prime multiples of $a$ that are $\geq x$: since $a \geq x$ and
$d = a \cdot q_1 \cdots q_{k_0-j}$ ($k_0 - j$ additional prime factors, each $\geq 2$):
$$d \geq a \cdot 2^{k_0-j} \geq x \cdot 2^{k_0-j}.$$

The sum of $1/(d \log d)$ over all such $d$ (which are all absent from $A$):
$$W(a) := \sum_{\substack{d \geq x,\, \Omega(d)=k_0 \\ a \mid d}} \frac{1}{d \log d}
= \frac{1}{a} \sum_{\substack{m \geq x/a,\, \Omega(m)=k_0-j \\ \gcd(m, \text{rad}(a)/?)}}
\frac{1}{m \log(am)}.$$

For fixed $a$: $W(a) \approx T_{k_0-j}(x/a) / a$ (rough; this is a sum over $(k_0-j)$-almost
primes $\geq 1$, scaled by $1/a$).

**Heuristic bound**: For $j = k_0 - 1$ (one level below): $W(a) \approx T_1(x/a)/a \approx
1/(a \log(x/a))$. Since $a \geq x$: $\log(x/a) \leq 0$ (we need $x/a \leq 1$).
For $a = x$: $W(x) = T_1(1)/x \approx \infty$?... this is not the right calculation.

Let me redo: for $a \geq x$ with $\Omega(a) = j < k_0$, the $(k_0-j)$-almost prime
multiples of $a$ that are $\geq x$ are just the $(k_0-j)$-almost prime multiples of $a$
(since $d \geq a \geq x$ automatically). So:
$$W(a) = \frac{1}{a} \cdot \sum_{\substack{m \geq 1 \\ \Omega(m) = k_0-j}} \frac{1}{m \log(am)}.$$

This sum converges (sum over $(k_0-j)$-almost primes, weighted by $1/(am \log am)$).

**Needed inequality**: To close the proof via global weights, we need:
$$\frac{1}{a \log a} \leq C \cdot W(a) \quad \text{for some absolute constant } C > 0.$$

Equivalently: $\sum_{m: \Omega(m)=k_0-j} 1/(m \log(am)) \geq (\log a)/C$.

Since $\log(am) \leq \log a + \log m \leq 2\log m$ when $m \geq a$ (which happens for large $m$):
$$W(a) \geq \frac{1}{a} \sum_{\substack{m \geq a \\ \Omega(m) = k_0-j}} \frac{1}{m \cdot 2\log m}
= \frac{T_{k_0-j}(a)}{2a}.$$

By Sathe-Selberg: $T_{k_0-j}(a) \sim \frac{(\log\log a)^{k_0-j-1}}{(k_0-j-1)!} \cdot \frac{1}{\log a}$.

So $W(a) \gtrsim \frac{(\log\log a)^{k_0-j-1}}{(k_0-j-1)! \cdot a \log a}$.

And $\frac{1/(a \log a)}{W(a)} \lesssim \frac{(k_0-j-1)!}{(\log\log a)^{k_0-j-1}}$.

For $k_0 - j = 1$ (i.e., $j = k_0 - 1$): ratio $\lesssim 1/1 = 1$... this is $O(1)$ but not
enough. We need a ratio $\leq 1$ to prove $1/(a\log a) \leq W(a)$, i.e., the "budget" of
excluded $k_0$-almost primes exceeds the gained element.

**For $j = k_0 - 1$**: $W(a) \gtrsim T_1(a)/(2a) \sim 1/(2a\log a)$. So $W(a) \gtrsim
\frac{1}{2} \cdot \frac{1}{a \log a}$. NOT enough to dominate $1/(a \log a)$ by factor $>1$.

**For $j < k_0 - 1$**: $W(a) \gtrsim T_{k_0-j}(a)/(2a) \gg 1/(a \log a)$ since $T_{k_0-j}$
can be larger than $1/\log a$ for appropriate $(k_0-j)$. E.g., for $k_0 - j = \lfloor \log_2 a
\rfloor$: $T_{k_0-j}(a) \approx 1$ (maximum). In this case $W(a) \gg 1/(a \log a)$.

**Summary of the weight argument**:
- If $a \in A$ has $\Omega(a) = j$ with $k_0 - j \geq \lfloor \log_2 a \rfloor$ (i.e., the
  "gap" from $j$ to $k_0$ is large relative to $a$): $W(a) \gg 1/(a \log a)$, so having $a \in A$
  "costs" enough in excluded $k_0$-almost primes to compensate. ✓
- If $a \in A$ has $\Omega(a) = j$ close to $k_0$ (say $j = k_0 - 1$): $W(a) \approx
  \frac{1}{2a \log a}$, which is half the gain. NOT sufficient alone. ✗

---

## The key missing step: cross-level weight domination

The global weight $W(a)$ counts excluded budget at level $k_0$ only. To fully account for
lower-stratum elements, we need a **multi-level** argument:

**Proposed Lemma (open)**: For any primitive $A \subset [x,\infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{k=1}^{\infty} \left( \text{allocation}_k \right)$$

where $\text{allocation}_k$ is the contribution of the $k$-stratum, bounded by a "budget" that
respects cross-stratum cancellations.

**One approach**: Choose a fixed $k$-assignment function $\kappa: [x,\infty) \to \mathbb{Z}_{\geq 1}$
such that $\kappa(n)$ records the "effective stratum" of $n$, and for any primitive $A$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_k T_k(x) \cdot \mathbf{1}[k = k^*(x)] + o(1)$$
where $k^*(x) = k_0$.

This would follow from the Erdős-Zhang theorem (which Lichtman-Pomerance proved): the
$k_0$-almost primes maximize the sum. Their proof is analytic (Sathe-Selberg + sieve), not
combinatorial.

---

## Partial results proved in this lemma

1. **(Proved)** Pure-$k_0$ case: $A \subseteq \{k_0\text{-almost primes} \geq x\}$
   $\Rightarrow S(A) \leq T_{k_0}(x) \leq 1 + 1/k_0$.

2. **(Proved)** Small lower-stratum contributions: For fixed $j < k_0$,
   $\sum_{a \in A, \Omega(a)=j} 1/(a\log a) \leq T_j(x) \to 0$ as $x \to \infty$.
   (Each fixed stratum $j \neq k_0$ contributes $o(1)$ to $S(A)$.)

3. **(Partial)** Weight argument: For $a \in A$ with $\Omega(a) = j \leq k_0 - 2$:
   The budget of excluded $k_0$-almost primes $W(a) \geq c/(\log\log a)^C \cdot 1/(a\log a)$,
   which is $\gg 1/(a\log a)$ for many $a$. The $j = k_0 - 1$ case is the hard case.

4. **(Open)** The $j = k_0 - 1$ case requires a tighter cross-stratum argument. See Q14.

---

## What Q14 should prove

The critical gap: elements of $A$ at stratum $k_0 - 1$ (one level below).

A $(k_0-1)$-almost prime $a \geq x$ in $A$ excludes all primes $p$ from $A$ such that $ap$ is a
$k_0$-almost prime ≥ x (but $ap$ is always a $k_0$-almost prime and $ap \geq a \geq x$).

The sum of excluded $k_0$-almost primes: $W(a) = \sum_{p \text{ prime}} 1/(ap \log(ap)) \leq
T_1(2)/a$.

And $1/(a \log a) \leq ?$ vs $T_1(2)/a = c/a$.

Since $a \geq x$: $1/(a\log a) \leq 1/(x \log x)$, while $T_1(2)/a \leq T_1(2)/x$.
The ratio is $T_1(2) \cdot \log a \geq T_1(2) \log x$. So $W(a) \geq (\log a / T_1(2)) \cdot
1/(a \log a) \gg 1/(a\log a)$. Wait:

$W(a) \geq T_1(2)/a$? Let me recheck: $W(a) = \sum_p 1/(ap\log(ap)) \leq T_1(2)/a$
(fiber_sum_bound). The upper bound is $T_1(2)/a$; I need a LOWER bound on $W(a)$.

Lower bound on $W(a)$: $W(a) \geq \sum_{p: p > 2} 1/(ap \log(ap)) \geq \sum_{p>2} 1/(ap \cdot 2\log(ap)/\log 2)$...
this is getting messy. A simpler lower bound: $W(a) \geq 1/(ap_0 \log(ap_0))$ for any single
prime $p_0$. Taking $p_0 = 2$: $W(a) \geq 1/(2a\log(2a))$.

Is $1/(2a\log(2a)) \geq c \cdot 1/(a\log a)$? Yes: $1/(2\log(2a)) \geq 1/(2 \cdot 2\log a) =
1/(4\log a)$ for $a \geq 4$. So $W(a) \geq 1/(4a\log a) < 1/(a\log a)$.

The LOWER bound on $W(a)$ is $\geq 1/(4 a\log a)$, which is $1/4$ of the gain. Not enough.

We need a large $W(a)$: using many primes $p$:
$W(a) = \sum_p 1/(ap\log(ap)) \geq \frac{1}{a} \sum_p \frac{1}{p \cdot (log a + \log p)}$
$\geq \frac{1}{a \cdot 2\log a} \sum_p \frac{1}{p}$ for $p \leq a$.

But $\sum_{p \leq a} 1/p \sim \log\log a$. So $W(a) \gtrsim \frac{\log\log a}{2a\log a}$.

And $1/(a\log a) / W(a) \lesssim \frac{2}{\log\log a} \to 0$ as $a \to \infty$.

**For large $a$: $1/(a\log a) / W(a) \to 0$.** So the budget of excluded $k_0$-almost primes
asymptotically dominates the gain from having $a \in A$! ✓

**For small $a$ (i.e., $a \approx x$)**: We need $a \to \infty$ as $x \to \infty$, which holds
since $a \geq x \to \infty$. So $\log\log a \geq \log\log x \to \infty$.

---

## Theorem (asymptotic multi-stratum bound, proved)

**Theorem**: For any primitive $A \subset [x,\infty)$ with elements at stratum $j = k_0 - 1$:
$$\frac{1/(a\log a)}{W(a)} \lesssim \frac{2}{\log\log x} \to 0 \quad \text{as } x \to \infty.$$

This means: for each $(k_0-1)$-almost prime $a \in A$, the budget $W(a)$ of excluded
$k_0$-almost primes is $\gg 1/(a\log a)$. However, this is an ASYMPTOTIC statement; it doesn't
give a uniform bound for finite $x$.

---

## Proof of the asymptotic bound S(A) ≤ 1 + o(1) (conditional sketch)

**Strategy**: Assign each element $a \in A$ to its "natural stratum" $\Omega(a)$. The contribution
of strata $j \neq k_0$ to $S(A)$ is:

$$S_{\neq k_0}(A) = \sum_{j \neq k_0} S_j(A) \leq \sum_{j \neq k_0} T_j(x).$$

For fixed $j$, $T_j(x) \to 0$ as $x \to \infty$ (by Sathe-Selberg, since $j \neq k_0(x)$
and $k_0(x) \to \infty$). Specifically:
- For $j < k_0$: $T_j(x) \sim \frac{(\log\log x)^{j-1}}{(j-1)!\log x} \to 0$ since $\log\log x = o(\log x)$.
- For $j > k_0$: same asymptotic, $\to 0$.

The TOTAL contribution of all non-$k_0$ strata:
$$S_{\neq k_0}(A) \leq \sum_{j \neq k_0} T_j(x) = T(x) - T_{k_0}(x)$$

where $T(x) = \sum_{n\geq x, \Omega(n)\leq K} 1/(n\log n)$ for some cutoff $K$.

**Issue**: Without a cross-stratum constraint, $\sum_{j\neq k_0} T_j(x)$ could be large.
But BY PRIMITIVITY: if $a \in A$ with $\Omega(a) = j < k_0$ and $a \geq x$, then all elements
$b \in A$ with $\Omega(b) = j+1$ must satisfy $a \nmid b$. The excluded $(j+1)$-almost primes
account for "budget" that offsets $a$'s contribution.

**Key bound** (proved above): $W_{j+1}(a) := \sum_{b: \Omega(b)=j+1, a|b} 1/(b\log b) \geq
\frac{\log\log x}{C \cdot a\log a}$ for large $x$.

So: $\frac{1}{a\log a} \leq \frac{C}{\log\log x} \cdot W_{j+1}(a)$.

Summing over $a \in A$ at stratum $j$:
$$S_j(A) \leq \frac{C}{\log\log x} \sum_{a \in A, \Omega(a)=j} W_{j+1}(a)
\leq \frac{C}{\log\log x} \cdot T_{j+1}(x).$$

(The last step: $\sum_a W_{j+1}(a) \leq T_{j+1}(x)$ because each $(j+1)$-almost prime $b$
is counted in $W_{j+1}(a)$ for AT MOST ONE $a \in A$ by primitivity of $A$.)

Wait — is the last step correct? For each $(j+1)$-almost prime $b \geq x$, define $a(b) :=
b/p$ for the LARGEST prime $p | b$. Then $b \in W_{j+1}(a)$ iff $a | b$, i.e., $b$ is a
multiple of $a$. A given $b$ is counted in $\sum_a W_{j+1}(a)$ for all $a \in A$ with $a | b$
and $\Omega(a) = j$. By primitivity: there can be AT MOST ONE such $a$ in $A$ (since if $a_1, a_2
\in A$ both divide $b$, then $a_1 | b$ and $a_2 | b$, but not necessarily $a_1 | a_2$ — so
we can't rule out multiple $a$'s dividing $b$). 

Actually: if $a_1, a_2 \in A$ are both $j$-almost primes and $a_1 | b$, $a_2 | b$ (each is a
divisor of $b$ with $\Omega = j$), primitivity of $A$ does NOT force $a_1 = a_2$. E.g.,
$b = 2 \cdot 3 \cdot 5 \cdot 7$ (4-almost prime), $a_1 = 2 \cdot 3$ (2-almost prime), $a_2 =
5 \cdot 7$ (2-almost prime). Then $a_1 | b$ and $a_2 | b$, and $a_1 \nmid a_2$, $a_2 \nmid a_1$.
Primitivity of $A$ allows $\{a_1, a_2\} \subset A$!

**Flaw**: The bound $\sum_a W_{j+1}(a) \leq T_{j+1}(x)$ assumes each $b$ is counted at most
once, but it can be counted multiple times.

**Fix**: Each $b$ can be counted at most $\Omega(b) = j+1$ times (once for each $j$-almost prime
divisor of $b$). So $\sum_{a \in A} W_{j+1}(a) \leq (j+1) \cdot T_{j+1}(x)$.

Then: $S_j(A) \leq \frac{C(j+1)}{\log\log x} \cdot T_{j+1}(x)$.

And the total:
$$S(A) = S_{k_0}(A) + \sum_{j < k_0} S_j(A) + \sum_{j > k_0} S_j(A)$$
$$\leq T_{k_0}(x) + \sum_{j=1}^{k_0-1} \frac{C(j+1)}{\log\log x} T_{j+1}(x) + \text{(upper strata)}.$$

For $j < k_0$: $T_{j+1}(x) \to 0$ as $x \to \infty$. Sum over $j$:
$$\sum_{j=1}^{k_0-1} \frac{C(j+1)}{\log\log x} T_{j+1}(x) \leq \frac{C \cdot k_0}{\log\log x} \cdot
\max_{j < k_0} T_{j+1}(x) \cdot (k_0-1).$$

With $k_0 \sim \log x / \log\log x$ and... this sum can still be large.

**The estimate fails to close**: The factor $k_0/\log\log x \sim \log x/(\log\log x)^2$, times
a stratum sum, may not go to 0.

---

## Status and remaining gap

**What is proved**:
1. Pure-$k_0$ case: $S(A) \leq T_{k_0}(x) \leq 1 + 1/k_0$. ✓
2. Per-element asymptotic: each lower-stratum element's contribution $\ll W(a)$ (excluded budget). ✓
3. Single-element exchange analysis: exchange fails for divisors (net $\Delta < 0$). ✓

**What is NOT proved**:
- The TOTAL of all lower-stratum contributions is $o(1)$.
- A uniform bound (for finite $x$) rather than asymptotic.

**Gap analysis**: The multi-stratum bound fails because:
- Lower-stratum elements can contribute more per element ($j < k_0$: bigger $1/(a\log a)$).
- The budget accounting (step "each $b$ counted once") fails — multiple $A$-elements can share
  the same $(j+1)$-level budget.
- The $j+1 \to j+2 \to \ldots \to k_0$ chain needs to be iterated, and each level multiplies by
  an extra factor, losing the bound.

**Proposed Q14**: Direct analytic bound on $S(A)$ using Sathe-Selberg, without exchange.
Specifically: prove $\sum_{j=1}^\infty S_j(A) \leq T_{k_0}(x) + o(1)$ by computing the
total allowed contribution of each stratum using the cross-stratum constraint more carefully
(e.g., via Möbius inversion or a sieve).
