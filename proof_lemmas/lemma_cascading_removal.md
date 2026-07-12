# Lemma: cascading_removal (B_{k_0}(x) is a sum maximum)

**Status**: proved (net exchange is negative); global max claim proved conditionally
**Session**: s_0712-110453-a069 (Q12)
**Depends on**: globally_unblocked_size, large_elements_blocked, fiber_sum_bound

---

## Setup

Fix $k_0 = \lfloor \log_2 x \rfloor$ and $x \geq 4$. Let $B = B_{k_0}(x)$ be the exchange
construction. For any primitive $A \subset [x,\infty)$, define:
- **Reverse exchange**: Add a globally $k_0$-blocked element $b = dp$ (with $d \geq x$ a
  $k_0$-almost prime, $p$ prime, $d \notin A$) to $A$ while maintaining primitivity.

Adding $b = dp$ to a primitive set $A$ requires removing all elements of $A$ that would violate
primitivity with $b$. These are exactly: all $a \in A$ with $a \mid b$ or $b \mid a$.

---

## Cascading removal theorem

**Theorem** (cascading_removal): Let $A$ be any primitive $A \subset [x,\infty)$ and $d \geq x$
a $k_0$-almost prime with $d \notin A$. Consider adding $b = dp$ (for prime $p > p_{\max}(d)$,
where $p_{\max}(d)$ is the largest prime factor of $d$) to $A$ while removing all violating elements.

The set of elements that must be removed from $A$ to add $b$ are:
1. All $a \in A$ with $a \mid b$: these have $\Omega(a) \leq k_0$ and $a \geq x$. The only
   such elements are the $k_0$-almost prime divisors of $b = dp$ that lie in $[x, \infty)$
   and are in $A$. These are:
   - $d$ itself (but $d \notin A$ by assumption — no removal needed).
   - $(d/q) \cdot p$ for each prime $q \mid d$ with $(d/q) \cdot p \geq x$: this is a
     $k_0$-almost prime (product of $k_0$ primes: $(k_0-1)$ factors from $d/q$ plus $p$).
     Denote $d_q := (d/q) \cdot p$.
2. All $a \in A$ with $b \mid a$: i.e., $a$ is a multiple of $dp$. Since $\Omega(dp) = k_0+1$
   and $a \geq dp \geq 2d \geq 2x$, such $a$ exist but removing them only decreases the sum.

**The removals in case (1)**: For each prime $q \mid d$ with $d_q = (d/q)p \geq x$:
since $d \geq x = 2^{k_0}$ and $q \geq 2$ and $p \geq 2$: $d_q = (d/q)p \geq (x/q)\cdot 2 \geq x$
iff $p/q \geq 1$ iff $p \geq q$. For primes $q \mid d$ with $q \leq p$: $d_q \geq x$. ✓

Since $p > p_{\max}(d) \geq q$ for all primes $q \mid d$: ALL $d_q = (d/q)p$ satisfy
$d_q \geq (d/q) \cdot q = d \geq x$. So ALL $\Omega(d) = k_0$ removals $d_q$ are $\geq x$.

---

## Net sum change from the reverse exchange

Starting from $A$ (with $d \notin A$ and fiber $F_d = \{e \in A : d \mid e, \Omega(e)=k_0+1\}$),
we perform: remove certain elements, add $b = dp$.

**Minimal reverse exchange** (only add $b$, remove violators):
- Add $b = dp$: $+1/(dp \log(dp))$.
- Remove $d_q = (d/q)p$ from $A$ (if $d_q \in A$) for each prime $q \mid d$: costs at most
  $-1/(d_q \log d_q) = -1/((d/q)p \log((d/q)p))$ per such $q$.

**Net change** (for $b = dp$ added, summing over all prime factors $q \mid d$ with $d_q \in A$):
$$\Delta_b = \frac{1}{dp \log(dp)} - \sum_{\substack{q \mid d,\, q \text{ prime} \\ d_q \in A}} \frac{1}{(d/q)p \log((d/q)p)}.$$

**Key bound**:
$$\frac{1}{(d/q)p \log((d/q)p)} \geq \frac{1}{dp \log(dp)} \cdot \frac{d}{d/q} \cdot \frac{\log(dp)}{\log((d/q)p)}
= \frac{q \cdot \log(dp)}{\log((d/q)p)} \cdot \frac{1}{dp\log(dp)}.$$

Since $q \geq 2$ and $\log(dp)/\log((d/q)p) \leq \log(dp)/\log(p) \to 1^+$ as $p \to \infty$
(but $\geq 1$ since $dp > (d/q)p$): each removed term is $\geq q \cdot \frac{1}{dp\log(dp)}$.

For a single prime factor $q \mid d$ with $d_q \in A$:
$$\Delta_b \leq \frac{1}{dp\log(dp)} - \frac{q}{dp\log(dp)} \cdot \frac{\log(dp)}{\log((d/q)p)} < 0.$$

Since $q \geq 2 > 1$: $\Delta_b < 0$ whenever at least one $d_q \in A$.

**If $d_q \notin A$ for all prime $q \mid d$**: Then $\Delta_b = +1/(dp\log dp) > 0$. But then
$(d/q)p \notin A$ for all $q \mid d$. This means the fiber of $(d/q)p$ in $A$ might contain
$dp$ itself! But we're ADDING $dp$, so it's not in $A$ yet. After adding $dp$, $(d/q)p$ (absent
from $A$) now has $dp$ in its fiber, which is consistent.

---

## Which direction does the exchange go?

**Case A** ($d \in B_{k_0}$, $d \notin A$, some $d_q \in A$): The reverse exchange
(add $dp$, remove some $d_q$'s from $A$) has $\Delta_b < 0$. So $A$ with the fibers and
without $d$ has SMALLER sum than $A$ with $d$ and without fibers. Adding back $d$ (the
forward exchange) INCREASES the sum.

**Case B** ($d \in B_{k_0}$, $d \notin A$, no $d_q \in A$): In this case, the reverse
exchange (add $dp$) has $\Delta_b > 0$. But this means $A$ gains $dp$ for free (no removal
needed). However, this case requires that $(d/q)p \notin A$ for all prime $q \mid d$. Since
$(d/q)p$ is a $k_0$-almost prime $\geq x$ (absent from $A$), it might itself have fibers in $A$.

---

## Theorem: B_{k_0}(x) achieves the maximum

**Claim**: For any primitive $A \subset [x, \infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{b \in B_{k_0}(x)} \frac{1}{b \log b} \leq 1 + \frac{1}{k_0}.$$

**Proof sketch via exchange**:

We use the forward exchange (replace a globally $k_0$-blocked element $b \in A$ by its
blocking $d$, removing $b$ and the full fiber of $d$ in $A$, then adding $d$):

For $d \notin A$ with fiber $F_d = \{e \in A : d \mid e, \Omega(e)=k_0+1\}$:
Define the "fiber swap": $A^{(d)} = (A \setminus F_d) \cup \{d\}$.

$A^{(d)}$ is primitive: $d$ is added; any $a \in A \setminus F_d$ satisfies $a \nmid d$ (since
$\Omega(a) \geq 1$ and $a \neq d$ and $a \geq x$; if $a \mid d$ then $\Omega(a) \leq k_0$,
but $a$ could be a prime factor of $d$, in which case $a < d$ and $a | d$: this IS a violation!).

**Issue**: $A^{(d)}$ might not be primitive if $A$ contains an element $a$ with $a \mid d$
(i.e., $a$ is a proper divisor of $d$ in $A$). Since $\Omega(d) = k_0$ and $a \mid d$ with
$a \neq d$: $\Omega(a) < k_0$. Such $a \in A$ divides $d$ — so we'd need to remove $a$ too.

**Multi-level fiber swap** (correct): To add $d$, remove ALL elements of $A$ that divide $d$
or are multiples of $d$ (the fiber). Define:
$$A^{[d]} = (A \setminus \{a : d \mid a \text{ or } a \mid d\}) \cup \{d\}.$$

Sum change: $+1/(d\log d) - \sum_{a \in A: d\mid a \text{ or } a \mid d} 1/(a \log a)$.

Since all $a \in A$ with $d \mid a$ satisfy $a \geq 2d$ (as $a \neq d$ and $d \mid a$):
$1/(a\log a) \leq 1/(2d \log(2d)) < 1/(2d \log d) = \frac{1}{2} \cdot 1/(d\log d)$. So the
multiples of $d$ in $A$ collectively contribute $< 1/(d\log d)/2$ to the removed sum.

For $a \in A$ with $a \mid d$ (divisors of $d$ in $A$): $a < d$ and $a \geq x$, so $a \in [x, d)$.
But $d \geq x$ and $a < d$. These are divisors of $d$ in $[x, d)$; can they be large?
For $d = x = 2^{k_0}$: the only divisors are $2^j$ for $j < k_0$, and $2^j < x$ for $j < k_0$.
So for $d = x$: NO divisors of $d$ in $[x, d)$ exist. ✓ For general $d > x$: divisors of $d$ in
$[x, d)$ could exist (e.g., if $d = 3x$ and $x$ is prime, then $x \mid 3x = d$). If $x \in A$:
then $x$ and $3x$ both in $A$ would violate primitivity (x | 3x), so $x \notin A$ in this case.
So if $d$ has a divisor $a \geq x$ in $A$, then $a \in A$ and $a \mid d$ already forces $d \notin A$
(by primitivity). Since we assumed $d \notin A$, this is consistent — but $a$ itself might be in $A$.
In the swap $A^{[d]}$, we'd remove $a$ (costing $-1/(a \log a)$ with $a < d$, hence removing MORE).

**Conclusion on the swap sign**: The net change from $A \to A^{[d]}$ is:
$$\Delta = +\frac{1}{d\log d} - \underbrace{\sum_{a \in A: d\mid a} \frac{1}{a\log a}}_{\leq T_1(2)/d} - \underbrace{\sum_{a \in A: a \mid d, a < d} \frac{1}{a\log a}}_{\geq 0}.$$

If $\sum_{a \in A: d\mid a} 1/(a\log a) + \sum_{a \mid d, a<d, a\in A} 1/(a\log a) < 1/(d\log d)$:
then $\Delta > 0$ (swap increases sum). Otherwise $\Delta \leq 0$.

**Key case**: If A has NO element dividing $d$ and NO element divisible by $d$ (i.e., $d$ is
"isolated" from $A$ in the divisibility order): then $\Delta = +1/(d\log d) > 0$. But this
means $d$ is compatible with $A$, so we could just add $d$ to $A$ directly! Then $A \cup \{d\}$
has larger sum — contradicting $A$ being a sum maximizer.

**Conclusion**: A sum maximizer $A^*$ must include EVERY $k_0$-almost prime $d \geq x$ (otherwise
we could add $d$ if it's compatible, increasing the sum) OR the fiber/divisor elements of $d$
in $A^*$ prevent adding $d$ (i.e., $A^*$ already has something that $d$ would violate).

If $A^*$ includes every compatible $k_0$-almost prime: $A^* \supset \{k_0\text{-almost primes}\geq x\}$,
plus globally $k_0$-unblocked $(k_0+1)$-almost primes $\subset B_{k_0}(x)$. So $A^* \subset B_{k_0}(x)$
(by primitivity: blocked elements can't coexist with their blocking d). Thus $\text{sum}(A^*) \leq \text{sum}(B_{k_0}(x)) \leq 1 + 1/k_0$. $\square$

---

## Status and gaps

**What's proved**: The cascading removal analysis shows the net exchange change is negative when
$d_q \in A$ for some $q \mid d$. This shows $B_{k_0}$ is a local maximum in a specific exchange
neighborhood.

**Gap**: The above "conclusion" has a logical gap: the existence of a sum maximizer $A^*$ is not
guaranteed (the supremum may not be achieved). And even if $A^*$ exists, the argument "add $d$
if compatible" needs to be made rigorous (compatible might require a finite sequence of additions).

**Rigorous version needed**: Show that for ANY sequence of $\leq n$ elements, the sum
$\sum_{a \in A} 1/(a\log a) \leq 1 + 1/k_0 + o(1)$ directly, without relying on the
existence of a maximizer. This requires a direct upper bound argument.

**See also**: `proof_open_questions.jsonl` Q13 for the rigorous completion.
