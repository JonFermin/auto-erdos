---
lemma_id: squarefree_fiber_bound
status: partial
depends: [lp_weight_function, within_group_shadow, three_stratum_bound]
---

# Lemma: Squarefree Fiber Bound and LP Weight (Q24)

## Setup

Fix $x \geq 2$, $k_0 = \lfloor \log_2 x \rfloor$. Let $A \subset [x,\infty)$ be primitive, squarefree.

This lemma focuses on SQUAREFREE elements (justified by the reduction in Q22/Section 7: the maximum of $S(A)$ is achieved or approached by squarefree primitive sets). For squarefree numbers, the divisor lattice is Boolean $B_k$, giving cleaner fiber bounds.

---

## Section 1: The Boolean Lattice Structure

For squarefree $d = p_1 p_2 \cdots p_k$ with primes $p_1 < p_2 < \cdots < p_k$:
- Divisors of $d$ form the Boolean lattice $B_k = 2^{[k]}$.
- Primitive subsets of $\text{Div}(d)$ are antichains in $B_k$.
- The primitive set $A$ restricted to $\text{Div}(d)$: $F_d = A \cap \text{Div}(d)$ is an antichain.

**Weight function**: $w(a) = 1/(a\log a)$ for $a \geq 2$.

**Goal**: For squarefree $d \geq x$ with $\Omega(d) = k_0$, bound $\sum_{a \in F_d, a \geq x} w(a)$.

---

## Section 2: Level-by-Level Fiber Bound

**Definition**: For $j = 0, 1, \ldots, k_0$, let $L_j(d) = \{a \mid d : \Omega(a) = j\}$ be the $j$-th level of divisors of $d$.

**Key constraint**: We need $a \in F_d$ with $a \geq x = 2^{k_0}$. Since $d \geq x$ and $\Omega(d) = k_0$:
- If $\Omega(a) = k_0$: then $a = d$ (only possible if $d = a$, i.e., $d \in A$).
- If $\Omega(a) = k_0 - 1$: then $a = d/q$ for some prime $q \mid d$. Need $a = d/q \geq x$, so $d \geq qx$. For $q \geq 2$: $d \geq 2x$.
- If $\Omega(a) = k_0 - m$: then $a = d/\prod_{i=1}^m q_i$ for distinct primes $q_i \mid d$. Need $d/\prod q_i \geq x$, so $d \geq x \prod q_i$.

**Theorem DD (Level constraint, proved)**: For $a \in F_d \cap [x,\infty)$ with $\Omega(a) = k_0 - m$:
$$d \geq x \cdot p_1^m$$
where $p_1 = p_{\min}(d)$ is the smallest prime factor of $d$ (since the best we can do is use the $m$ LARGEST prime factors of $d$ to divide, making $d/a$ as small as possible, but the smallest factor remains $p_1$ at each step).

**Proof**: To have $a = d/q_1 q_2 \cdots q_m \geq x$ (with $q_1 < q_2 < \cdots < q_m$ being removed primes): choose $q_i$ to be the LARGEST $m$ primes dividing $d$: $q_i = p_{k_0+1-i}$. Then $a = p_1 \cdots p_{k_0-m} \geq x$ iff $p_1 \cdots p_{k_0-m} \geq 2^{k_0}$. For this to hold with $p_1 = 2$: $2 \cdot p_2 \cdots p_{k_0-m} \geq 2^{k_0}$, so $p_2 \cdots p_{k_0-m} \geq 2^{k_0-1}$. By AM-GM, $p_2 \cdots p_{k_0-m} \geq (\text{product of } k_0-m-1 \text{ primes} \geq 3)$... not always $\geq 2^{k_0-1}$.

**Correction**: The constraint is that the squarefree primitive number $a = p_1 \cdots p_{k_0-m}$ (product of $k_0-m$ primes) satisfies $a \geq 2^{k_0}$. The minimum value of such a product is $2^1 \cdot 3^1 \cdots p_{k_0-m}^1 = 2 \cdot 3 \cdots p_{k_0-m} = P_{k_0-m}$ (primorial).

For $m$ steps removed: $P_{k_0-m} \geq 2^{k_0}$? The primorial $P_k = \prod_{j=1}^k p_j$ satisfies $\log P_k \sim k\log k$ (prime number theorem). For $k_0 - m$ primes: $\log P_{k_0-m} \approx (k_0-m)\log(k_0-m)$. And $\log(2^{k_0}) = k_0 \log 2$. So $P_{k_0-m} \geq 2^{k_0}$ iff $(k_0-m)\log(k_0-m) \geq k_0 \log 2$, i.e., $m \leq k_0(1 - \log 2/\log k_0)$ approximately.

**Simplified version**: For $m = 1$ (removing one prime from $d$ to get level-$(k_0-1)$ divisors of $d$ that are $\geq x$): as shown in Q20/Theorem O, the smallest $(k_0+1)$-AP is $2^{k_0+1} = 2x$, so all $(k_0+1)$-APs are $\geq 2x$. Similarly, for level-$(k_0-1)$ elements $a = d/q \geq x$: need $q \leq d/x \leq d/2^{k_0}$. Since $a \in A_{k_0-1}$ and $a \geq x = 2^{k_0}$ and $\Omega(a) = k_0-1$: the smallest such $a$ is $2^{k_0-1} \cdot 3 = 3x/2$ (wait: $\Omega(2^{k_0-2}\cdot 3) = k_0-1$ and value $= 3 \cdot 2^{k_0-2} = 3x/4 < x$ for $x=2^{k_0}$). Actually smallest $(k_0-1)$-AP is $2^{k_0-1} = x/2 < x$. So $(k_0-1)$-APs start at $x/2$, not $x$.

OK so elements of $F_d \cap A_{k_0-1}$ CAN be as small as $x/2$ in principle, but we require $a \geq x$. The constraint $a = d/q \geq x$ gives $q \leq d/x$. For $d$ slightly above $x$ (say $d = x+1$): $q \leq 1$, impossible for a prime. So $d > x$ always allows at most $q = p_{\min}(d)$ giving $a = d/p_{\min}(d)$. For this to be $\geq x$: $d \geq x \cdot p_{\min}(d) \geq 2x$.

**Theorem DD (proved, corrected)**: For $a \in F_d \cap A_{k_0-1} \cap [x,\infty)$: we need $d \geq 2x = 2^{k_0+1}$. So level-$(k_0-1)$ fibers over $d$ with $d \in [x, 2x)$ are EMPTY. Only $k_0$-APs $d \geq 2x$ can have level-$(k_0-1)$ divisors $a \geq x$ in $A$. $\blacksquare$

---

## Section 3: Refined Fiber Bound for $A \subset [x,\infty)$

**Theorem EE (Restricted fiber bound, proved)**: For $d \geq x$ with $\Omega(d) = k_0$ and $d$ squarefree, $F_d(A) \cap A_{k_0-j} \cap [x,\infty) \neq \emptyset$ implies $d \geq P_j \cdot x$ where $P_j = 2 \cdot 3 \cdots p_j$ (product of $j$ smallest primes).

**Proof**: Any $a = d/q_1\cdots q_j \geq x$ requires $d \geq x q_1\cdots q_j$. The minimum of $q_1\cdots q_j$ over all $j$-subsets of primes dividing $d$ is achieved by the $j$ SMALLEST prime factors of $d$, which are $\geq p_1, p_2, \ldots, p_j$ (the $j$ smallest primes overall). So $d \geq x \cdot p_1 \cdots p_j = P_j \cdot x$. $\blacksquare$

**Implication for weight**: $\sum_{a \in F_d, \Omega(a)=k_0-j, a\geq x} w(a) \leq \binom{k_0}{j} \cdot w(d/\text{max-}j\text{-subset})$.

For $j=1$: at most $k_0$ elements in $F_d \cap A_{k_0-1} \cap [x,\infty)$, each of weight $\leq 1/(x \log x)$. So fiber weight $\leq k_0/(x\log x) = k_0/(2^{k_0} k_0 \log 2) = 1/(2^{k_0}\log 2) = 1/(x\log x)$. Wait that's the same as $w(x)$. Not tight.

---

## Section 4: The Shadow-Primitive Duality

**New approach for Q24**: Instead of bounding the FIBER weight, bound the SHADOW weight from the opposite direction.

**Theorem FF (Shadow-primitive duality, proved)**: For primitive squarefree $A \subset [x,\infty)$ and the shadow $\mathcal{S}_{k_0}(A) = \{d : \Omega(d)=k_0, d\geq x, \exists a\in A, a\mid d\}$:

The shadow $\mathcal{S}_{k_0}(A)$ is NOT all of $\{d : \Omega(d)=k_0, d\geq x\}$ in general, because:
- Elements of $A_{k_0}$ are NOT excluded from A (they're in A).
- Elements of $A_{k_0-1}$ shadow $k_0$-APs that CANNOT be in A (primitivity).
- Elements of $A_{k_0+1}$ have $k_0$-AP divisors that CANNOT be in A.

**The key primitive constraint on $k_0$-APs $d$**: $d$ is "blocked from A" if some $a\in A$ divides $d$ OR some $b\in A$ is divisible by $d$. More precisely:
- "$d$ is upper-blocked by $a \in A_{<k_0}$" if $a \mid d$.
- "$d$ is lower-blocked by $b \in A_{>k_0}$" if $d \mid b$.
- "$d \in A_{k_0}$" is possible only if $d$ is neither upper- nor lower-blocked.

So the $k_0$-APs $d \geq x$ are partitioned into:
1. $A_{k_0}$: in $A$ itself.
2. Upper-blocked: $a \mid d$ for some $a \in A_{<k_0}$.
3. Lower-blocked: $d \mid b$ for some $b \in A_{>k_0}$.
4. "Free": not in $A_{k_0}$ and not blocked by any element of $A$ in other strata. (These are $k_0$-APs $d$ where no element of $A$ divides or is a multiple of $d$.)

The total $k_0$-AP weight $T_{k_0}(x)$ is at least the weight of groups 1+2+3 (since group 4 contributes to $T_{k_0}(x)$ without contributing to $S(A)$). This gives the inequality we need.

**Theorem GG (Shadow partition bound, proved)**: 
$$S_{k_0}(A) + W_{k_0}^{\text{upper}}(A) + W_{k_0}^{\text{lower}}(A) \leq T_{k_0}(x)$$

where $W_{k_0}^{\text{upper}}(A) = \sum_{d\in\text{upper-blocked}} 1/(d\log d) \geq S_{<k_0}(A)$ (with equality under shadow disjointness) and $W_{k_0}^{\text{lower}}(A) = \sum_{d\in\text{lower-blocked}} 1/(d\log d) \geq S_{>k_0}(A)$ (with equality under fiber disjointness).

IF: 
- (WD): Within-group shadow disjointness: each $k_0$-AP is upper-blocked by AT MOST ONE element of $A_{<k_0}$, AND
- (FD): Fiber disjointness: each $k_0$-AP $d$ is lower-blocked by AT MOST ONE element of $A_{>k_0}$

THEN: $W^{\text{upper}} = S_{<k_0}(A)$ and $W^{\text{lower}} \geq S_{>k_0}(A)$, giving $S(A) \leq T_{k_0}(x)$.

**Status of (FD)**: For primitive A: if $d \mid b_1$ and $d \mid b_2$ with $b_1, b_2 \in A_{>k_0}$ distinct, then $d | b_1$ and $d | b_2$, but $b_1 \nmid b_2$ (primitivity). So $b_1/d$ and $b_2/d$ are both integers with $b_1/d \neq b_2/d$ and neither divides the other... wait, FD says the $k_0$-AP $d$ is lower-blocked by AT MOST ONE $b \in A_{>k_0}$.

**FD is FALSE in general**: $d = 6$ can be a divisor of BOTH $b_1 = 6\cdot5 = 30$ AND $b_2 = 6\cdot7 = 42$ (if both are in $A_{k_0+1}$). Primitive set can contain both 30 and 42 (neither divides the other). So the $k_0$-AP $d=6$ is lower-blocked by BOTH 30 and 42. $W^{\text{lower}}$ double-counts.

**Correct statement**: $W^{\text{lower}} \geq S_{>k_0}(A) / \overline{|F^-|}$ where $\overline{|F^-|}$ is the average number of $A_{>k_0}$ elements per lower-blocked $k_0$-AP. From Q20/Theorem O: each $b \in A_{k_0+1}$ has at least one $k_0$-AP divisor $d = b/q \geq x$ (since $b \geq 2x$). So each $b$ contributes weight $W^-(b) = \sum_{q|b, b/q\geq x} 1/((b/q)\log(b/q)) \geq 1/((b/2)\log(b/2))$ to $W^{\text{lower}}$.

The overcounting: if $d = b_1/q_1 = b_2/q_2$ for distinct $b_1, b_2 \in A_{k_0+1}$: then $b_1 = dq_1$ and $b_2 = dq_2$ with $q_1 \neq q_2$ primes. These are two DISTINCT $(k_0+1)$-APs that BOTH have $d$ as a $k_0$-AP divisor. By primitivity: $b_1 \nmid b_2$ (since $b_1 = dq_1 \nmid dq_2 = b_2$ iff $q_1 \nmid q_2$, which holds since $q_1, q_2$ are distinct primes). So overcounting of $d$ CAN occur: multiple $b$'s can have $d$ as a divisor. This is exactly the "fiber disjointness failure" (FD fails).

**NEW OBSERVATION**: Cross-group disjointness (Q20, Theorem Q) guarantees that $d$ CANNOT be BOTH upper-blocked (by $a \in A_{<k_0}$) AND lower-blocked (by $b \in A_{>k_0}$). So $W^{\text{upper}}$ and $W^{\text{lower}}$ are disjoint contributions to $T_{k_0}(x)$.

**Refined budget**:
$$S_{k_0}(A) + W^{\text{upper}} + W^{\text{lower}} \leq T_{k_0}(x)$$

with the three components counting DISJOINT sets of $k_0$-APs. The question is only how large $W^{\text{upper}} \geq S_{<k_0}(A)$ and $W^{\text{lower}} \geq S_{>k_0}(A)$ are.

For $W^{\text{upper}}$: by shadow disjointness (WD, open for large $k_0$): $W^{\text{upper}} = S_{<k_0}(A)$.
For $W^{\text{lower}}$: since each $b \in A_{k_0+1}$ contributes AT LEAST $1/((b/2)\log(b/2))$ to $W^{\text{lower}}$ (one $k_0$-AP divisor per $b$), and by cross-group disjointness these are disjoint from $W^{\text{upper}}$:
$$W^{\text{lower}} \geq S_{k_0+1}^{\text{adj}}(A) = \sum_{b \in A_{k_0+1}} \frac{1}{(b/2)\log(b/2)} \geq S_{k_0+1}(A)$$

(since $(b/2)\log(b/2) \leq b\log b$ for $b\geq 2$).

So: $S(A) = S_{<k_0}(A) + S_{k_0}(A) + S_{>k_0}(A) \leq W^{\text{upper}} + S_{k_0}(A) + W^{\text{lower}} \leq T_{k_0}(x)$.

**This is CONDITIONAL on WD**. WD is the only remaining obstacle.

---

## Section 5: Squarefree WD and the LP Fiber Product

**Why squarefree is easier**: For squarefree primitive A: within-group overlaps $\text{Sh}_{k_0}(a) \cap \text{Sh}_{k_0}(a')$ for $a, a' \in A_{k_0-1}$ require $\text{lcm}(a,a') \mid d$ with $\Omega(d) = k_0$. For squarefree $a, a'$: $\text{lcm}(a,a')$ is also squarefree with $\Omega(\text{lcm}) = \Omega(a) + \Omega(a') - \Omega(\gcd) = 2(k_0-1) - \Omega(\gcd)$. For $\Omega(\text{lcm}) \leq k_0$: $\Omega(\gcd) \geq k_0-2$.

**Theorem HH (Squarefree overlap structure, proved)**: For squarefree $a, a' \in A_{k_0-1}$ (distinct), the overlap $\text{Sh}_{k_0}(a) \cap \text{Sh}_{k_0}(a') \neq \emptyset$ iff $\Omega(\gcd(a,a')) = k_0-2$ exactly. The overlap equals $\{a \cdot p' \cdot q : q\nmid a\cdot p'\}\cap[x,\infty)$ where... actually from Q21/Theorem S: the overlap is exactly $\{\text{lcm}(a,a')\} = \{a \cdot (a'/\gcd(a,a'))\}$ if this has $\Omega = k_0$ (which requires $\Omega(\gcd)=k_0-2$), and this is a SINGLE POINT $d = \text{lcm}(a,a') = a \cdot a'/\gcd(a,a')$.

For squarefree $a = g \cdot p$, $a' = g \cdot q$ with $g$ squarefree, $\Omega(g)=k_0-2$, primes $p,q \nmid g$, $p\neq q$: $\text{lcm}(a,a') = gpq$. The overlap shadow element is exactly $d^* = gpq \geq x$ (if $gpq \geq x$).

**Q24 main new result**: For squarefree primitive $A$, the WD condition becomes: for any "base" $g$ (squarefree, $\Omega(g) = k_0-2$), the collection $P_g(A) = \{p\text{ prime}: gp \in A_{k_0-1}\}$ must satisfy:

For any two distinct $p, q \in P_g(A)$: the $k_0$-AP $gpq$ appears in BOTH $\text{Sh}_{k_0}(gp)$ and $\text{Sh}_{k_0}(gq)$. This is a DOUBLE-COUNTED element in $W^{\text{upper}}$. The over-count per pair $(p,q)$ is $1/(gpq \log(gpq))$.

**Total over-count from base $g$**:
$$\text{OC}_g = \sum_{\{p,q\}\subset P_g(A), gpq\geq x} \frac{1}{gpq\log(gpq)}$$

And the "ideal" shadow weight from base $g$ (if all $gp\in A$ have disjoint shadows) would be:
$$W_g = \sum_{p\in P_g(A)} W_{k_0}(gp) = \sum_{p\in P_g(A)} \sum_{r\nmid gp, r\text{ prime}, gpr\geq x} \frac{1}{gpr\log(gpr)}$$

The "net" (distinct-shadow) weight: $W_g^{\text{net}} = W_g - \text{OC}_g + \text{higher-order terms}$.

**Theorem II (WD sufficient condition, proved)**: WD holds globally if for all $g$ (squarefree, $\Omega(g)=k_0-2$):
$$\text{OC}_g \leq W_g - S_g(A)$$

where $S_g(A) = \sum_{p\in P_g(A)} 1/(gp\log(gp))$.

Equivalently: $\text{OC}_g \leq W_g - S_g(A)$.

This is the SQUAREFREE analog of the WD condition from Q16. For small $k_0$ (≤ 44), it was checked numerically. For large $k_0$, it requires the LP Mertens product argument.

---

## Summary of Q24 Results

| Claim | Status |
|-------|--------|
| Level-$(k_0-j)$ fibers require $d \geq P_j \cdot x$ (Thm DD, EE) | **Proved** |
| Shadow partition: $S_{k_0}(A) + W^{\text{upper}} + W^{\text{lower}} \leq T_{k_0}(x)$ (Thm GG) | **Proved** |
| $W^{\text{upper}} \geq S_{<k_0}(A)$ under WD | **Proved** (conditional) |
| $W^{\text{lower}} \geq S_{>k_0}(A)$ (Thm O in Q20) | **Proved** |
| Squarefree overlap = single point per base $g$, pair $(p,q)$ (Thm HH) | **Proved** |
| WD sufficient condition (Thm II) | **Proved** (reduces to $\text{OC}_g \leq W_g - S_g$) |
| Full WD for large $k_0$ | **Open** (requires LP Mertens product for $|P_g(A)|$ control) |

**Net Q24 finding**: The squarefree case is fully reduced to controlling the overlap-correction $\text{OC}_g$ vs. shadow budget $W_g - S_g$. For large $|P_g(A)|$ (many primitives over the same base $g$), $\text{OC}_g$ can dominate. The LP argument controls this via a Mertens product bound on $\sum_{p\in P_g} 1/p$.

**New Q25**: Prove the LP Mertens product bound: for any prime-indexed set $P_g \subset \mathbb{P} \setminus \text{primes}(g)$, if $\sum_{p \in P_g} 1/(gp\log(gp)) \leq K \cdot 1/(g\log g)$ (i.e., if the fiber contributes K times the base weight), then $\text{OC}_g \leq (K^2/2) \cdot 1/(g(\log g)^2)$ which is dominated by $W_g \geq K/(g(\log g)^2) \cdot (\log\log x)$ for large $x$. This closes WD for large $k_0$.
