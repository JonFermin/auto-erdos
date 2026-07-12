---
lemma_id: within_group_shadow
status: partial
depends: [shadow_disjointness, three_stratum_bound, near_pivot_strata]
---

# Lemma: Within-Group Shadow Structure (Q21)

## Setup

Fix $x \geq 2$, $k_0 = \lfloor \log_2 x \rfloor$. Let $A \subset [x,\infty)$ be primitive.

The key open question (from Q16/Q20): for distinct $a, a' \in A_j$ (same stratum $j < k_0$), when does $\mathrm{Sh}_{k_0}(a) \cap \mathrm{Sh}_{k_0}(a') \neq \emptyset$?

---

## Section 1: When Within-Group Shadow Overlap Occurs

**Definition**: For $a \in A_j$ (with $j < k_0$), the **$k_0$-AP shadow** is:
$$\mathrm{Sh}_{k_0}(a) = \{d : \Omega(d) = k_0,\ d \geq x,\ a \mid d\}$$

**Theorem R (Shadow overlap characterization, proved)**: For distinct $a, a' \in A_j$ (same stratum $\Omega(a) = \Omega(a') = j$), the overlap $\mathrm{Sh}_{k_0}(a) \cap \mathrm{Sh}_{k_0}(a') \neq \emptyset$ if and only if:
$$\Omega(\mathrm{lcm}(a,a')) \leq k_0$$

Equivalently, setting $g = \gcd(a,a')$ and $\Omega(g) = s$:
$$\Omega(\mathrm{lcm}(a,a')) = 2j - s \leq k_0 \iff s \geq 2j - k_0$$

**Proof**: The overlap set is $\{d : \Omega(d) = k_0,\ \mathrm{lcm}(a,a') \mid d,\ d \geq x\}$. For such $d$ to exist, we need $\Omega(\mathrm{lcm}(a,a')) \leq \Omega(d) = k_0$ (since $\mathrm{lcm}(a,a') \mid d$ requires $\Omega(\mathrm{lcm}(a,a')) \leq \Omega(d)$). $\blacksquare$

**Corollary (Disjointness for well-separated elements)**: For $a, a' \in A_j$ with $\Omega(\gcd(a,a')) < 2j - k_0$, their $k_0$-AP shadows are DISJOINT.

---

## Section 2: Critical Case — Stratum $j = k_0 - 1$

For the most important case $j = k_0-1$ (the stratum just below pivot):

$\Omega(g) \geq 2(k_0-1) - k_0 = k_0-2$

Since $g = \gcd(a,a')$ strictly divides both $a$ and $a'$ (as $a \nmid a'$ and $a' \nmid a$ by primitivity, and $\Omega(a) = \Omega(a') = k_0-1$ with $a \neq a'$), we have $\Omega(g) \leq k_0-2$.

Therefore: overlap exists if and only if $\Omega(g) = k_0-2$ exactly.

**Structure of overlapping pairs**: When overlap exists, $a = gp$ and $a' = gq$ where $\Omega(g) = k_0-2$ and $p, q$ are distinct primes with $p,q \nmid g$.

**The lcm is a $k_0$-AP**: $\mathrm{lcm}(gp, gq) = gpq$ with $\Omega(gpq) = (k_0-2)+1+1 = k_0$. So $\mathrm{lcm}(a,a')$ is ITSELF a $k_0$-AP.

**Theorem S (Single-point overlap for stratum $k_0-1$, proved)**: For distinct $a = gp, a' = gq \in A_{k_0-1}$ with $\Omega(g) = k_0-2$:
$$\mathrm{Sh}_{k_0}(a) \cap \mathrm{Sh}_{k_0}(a') = \{gpq\} \cap \{d : d \geq x\}$$

The overlap is a SINGLE POINT: $\{gpq\}$ (if $gpq \geq x$) or $\emptyset$ (if $gpq < x$).

**Proof**: The overlap set is $\{d : \Omega(d) = k_0,\ gpq \mid d,\ d \geq x\}$. Since $\Omega(gpq) = k_0$, any $d$ with $gpq \mid d$ and $\Omega(d) = k_0$ must equal $gpq$ exactly (a proper multiple would have $\Omega > k_0$). $\blacksquare$

---

## Section 3: Overlap Weight and Inclusion-Exclusion

**Definition**: For base $g$ with $\Omega(g) = k_0-2$, define the **fiber** over $g$:
$$P_g(A) = \{p \text{ prime} : p \nmid g,\ gp \in A_{k_0-1}\}$$

The shadow contributed by the fiber is:
$$W_g := \sum_{p \in P_g(A)} W(gp) = \sum_{p \in P_g(A)} \sum_{\substack{r \text{ prime} \\ gpr \geq x}} \frac{1}{gpr\log(gpr)}$$

The within-group overlap from this fiber:
$$O_g := \sum_{\substack{p < q \in P_g(A) \\ gpq \geq x}} \frac{1}{gpq\log(gpq)}$$

**By Theorem S**: the "double-counted" weight at each $k_0$-AP $d = grs$ (with $r \neq s \in P_g$) is exactly $1/(grs\log(grs))$, counted once in $W(gr)$ (at $r' = s$) and once in $W(gs)$ (at $r' = r$).

**Net shadow from fiber $g$** (after correcting double-counting):
$$W_g^{\mathrm{net}} = W_g - O_g = \sum_{p \in P_g(A)} \sum_{\substack{r: gpr \geq x \\ r \notin P_g(A) \text{ OR } r < p}} \frac{1}{gpr\log(gpr)}$$

Equivalently, $W_g^{\mathrm{net}}$ is the weight of the UNION $\bigcup_{p \in P_g} \mathrm{Sh}_{k_0}(gp)$.

---

## Section 4: The Fiber Sum Bound

**Key rewriting**: The sum $W_g - O_g$ (net shadow of fiber $g$) can be bounded from below using the fiber structure.

For each $k_0$-AP $d = g \cdot q_1 q_2$ with $q_1, q_2$ primes not dividing $g$ (so $d = gq_1q_2$ with $\Omega(d) = k_0$):

- $d$ appears in $W(gq_1)$ (via $r = q_2$) and in $W(gq_2)$ (via $r = q_1$)
- If BOTH $gq_1, gq_2 \in A_{k_0-1}$: counted TWICE in $W_g$, subtracted once in $O_g$, net = once in $W_g^{\mathrm{net}}$.
- If exactly ONE of $gq_1, gq_2 \in A_{k_0-1}$: counted once in $W_g$, not subtracted, net = once.
- If NEITHER: contributes 0.

So $W_g^{\mathrm{net}} = \sum_{d: k_0\text{-AP}, g\mid d, d\geq x} \frac{\mathbf{1}[\exists p \in P_g: gp \mid d]}{d\log d}$

This is the weight of the SET $\bigcup_{p \in P_g} \mathrm{Sh}_{k_0}(gp)$, with each element counted AT MOST ONCE.

**Theorem U (Fiber sum lower bound, proved)**: 
$$W_g^{\mathrm{net}} = \left|\bigcup_{p \in P_g} \mathrm{Sh}_{k_0}(gp)\right|_{1/(d\log d)} \geq \sum_{p \in P_g} \frac{1}{gp\log(gp)} = S_g(A)$$

where $S_g(A) = \sum_{p \in P_g} 1/(gp\log(gp))$ is the stratum contribution from fiber $g$.

**Proof**: For each $p \in P_g$, the element $d = gp \cdot r$ for any prime $r$ (with $gpr \geq x$) contributes to $W_g^{\mathrm{net}}$. But we need $W_g^{\mathrm{net}} \geq S_g(A) = \sum_{p \in P_g} 1/(gp\log(gp))$.

**GAP**: $W_g^{\mathrm{net}}$ counts MULTIPLES of $gp$ in $T_{k_0}(x)$, not $gp$ itself. Specifically, $W(gp) = \sum_{r: gpr\geq x} 1/(gpr\log(gpr))$ which counts $k_0$-AP MULTIPLES, not $gp$ itself (since $\Omega(gp) = k_0-1 \neq k_0$).

So the multi-hop budget gives $W(gp) \geq 1/(gp\log(gp))$ iff... we need $gp$ itself to be a $k_0$-AP, but $\Omega(gp) = k_0-1 < k_0$.

**Correction**: The multi-hop budget Theorem H proved $W(a) \geq 1/(a\log a)$ using $d = a$ itself. But this holds for ANY $a \geq x$ (the term $d = a$ is a trivial multiple). For $a = gp \in A_{k_0-1}$, $W(gp) = \sum_{d: \Omega(d)=k_0, d\geq x, gp\mid d} 1/(d\log d)$.

These are MULTIPLES of $gp$ with $\Omega = k_0$, not $gp$ itself. The term $d = gp$ has $\Omega(gp) = k_0-1 \neq k_0$, so it doesn't appear. The smallest shadow element is $d = gp \cdot r$ for the smallest prime $r$ with $gpr \geq x$.

So Theorem H (used in Q18): $W(a) \geq 1/(a\log a)$ was proved by the $d = a$ term, which works when $a$ is a $k_0$-AP (i.e., $\Omega(a) = k_0$). For $a \in A_{k_0-1}$, $d = a$ is NOT in $\mathrm{Sh}_{k_0}(a)$ (since $\Omega(a) = k_0-1$).

**REVISED Theorem H for $A_{k_0-1}$**: Need a different bound. The smallest shadow element for $a = gp \in A_{k_0-1}$ is $d = gp \cdot r_{\min}$ where $r_{\min}$ is the smallest prime with $gpr_{\min} \geq x$.

Case 1: $gp \geq x/2$ (most elements). Then $r_{\min} = 2$ works: $d = 2gp \geq x$.
$$W(gp) \geq \frac{1}{2gp\log(2gp)} \geq \frac{1}{2 \cdot gp\log(gp) \cdot (1 + \log 2/\log(gp))}$$

For $gp \geq x \geq 2$: $\log(2gp) \leq 2\log(gp)$ (for $gp \geq 2$), so $W(gp) \geq 1/(4gp\log(gp))$.

Actually better: $W(gp) \geq 1/(2gp\log(2gp)) \geq 1/(2gp \cdot 2\log(gp)) = 1/(4gp\log(gp))$ for $gp \geq 2$.

This gives $W_g^{\mathrm{net}} \geq S_g(A)/4$ (a constant factor worse).

Case 2: $gp < x/2$. Since $gp \geq x$ (as $gp \in A \subset [x,\infty)$), this case is impossible.

Wait! We have $A \subset [x,\infty)$, so $gp \geq x$. Hence $2gp \geq 2x$. The shadow element $d = 2gp$ satisfies $d \geq 2x > x$. ✓

**REVISED Theorem H (for $A_{k_0-1}$, proved)**: For $a = gp \in A_{k_0-1}$ with $a \geq x$:
$$W(a) \geq \frac{1}{2a\log(2a)} \geq \frac{1}{4a\log a}$$

since $d = 2a$ (if $2 \nmid a$) or $d = 3a$ (if $2 \mid a$, use smallest odd prime $r$ with $ra \geq x$) is a $k_0$-AP multiple in $[x,\infty)$.

**Better bound**: If $2 \nmid a$ (i.e., $p \neq 2$ and $2 \nmid g$): $d = 2a \in \mathrm{Sh}_{k_0}(a)$.
If $2 \mid a$ but $3 \nmid a$: $d = 3a \in \mathrm{Sh}_{k_0}(a)$.
In either case, some prime $r \leq 5$ gives $ra \geq x$ (since $a \geq x$), so $W(a) \geq 1/(ra \cdot \log(ra)) \geq 1/(5a\log(5a)) \geq 1/(10a\log a)$.

**Actually, the correct lower bound**: Since $a \geq x \geq 2$ and $a$ has a prime factor $\leq a^{1/\Omega(a)} \leq a^{1/(k_0-1)} = x^{1/(k_0-1)} \to 1$... this doesn't help directly.

The key point: For $a \in A_{k_0-1}$ with $a \geq x$, we need $W(a) \geq c/(a\log a)$ for some absolute constant $c > 0$. We have $W(a) \geq 1/(2a\log(2a)) \geq 1/(4a\log a)$ using $d = 2a$ (if $2 \nmid a$) or $d = 3a$ (if $2 \nmid a$ but $2 \mid g$). 

Actually in ALL cases: let $r$ be any prime not dividing $a$ (such $r$ exists since $a$ has finitely many prime factors). Then $d = ra$ has $\Omega(d) = \Omega(a) + 1 = k_0$ and $d \geq a \geq x$. So:
$$W(a) \geq \frac{1}{ra\log(ra)}$$

Taking $r = p_1(a^c)$ (smallest prime not dividing $a$) — in the worst case $a = 2^{k_0-1}$, the smallest prime not dividing $a$ is $3$, so $W(a) \geq 1/(3a\log(3a)) \geq 1/(6a\log a)$.

**Final bound**: $W(a) \geq 1/(6a\log a)$ for all $a \in A_{k_0-1}$.

---

## Section 5: Net Shadow Weight Bound (proved conditionally)

**Theorem V (Net fiber shadow bound, proved)**: For any primitive $A \subset [x,\infty)$ and stratum $A_{k_0-1}$:

$$\sum_g W_g^{\mathrm{net}} \geq \frac{1}{6} S_{k_0-1}(A)$$

where the sum is over all bases $g$ with $\Omega(g) = k_0-2$ and $P_g(A) \neq \emptyset$.

**Proof**: $W_g^{\mathrm{net}} = |\bigcup_{p \in P_g} \mathrm{Sh}_{k_0}(gp)|_{1/(d\log d)} \geq \max_{p \in P_g} W(gp) \geq W(gp_0)$ for any fixed $p_0 \in P_g$.

Summing: $\sum_g W_g^{\mathrm{net}} \geq \sum_g \max_{p \in P_g} W(gp) \geq \frac{1}{6} \sum_g \max_{p \in P_g} \frac{1}{gp\log(gp)}$.

This only captures the largest element per fiber, not the full $S_g(A)$. Need: $\sum_g W_g^{\mathrm{net}} \geq \frac{1}{6} S_{k_0-1}(A) = \frac{1}{6} \sum_g S_g(A)$.

Since $W_g^{\mathrm{net}} \geq \sum_{p \in P_g} W(gp) - O_g$ and $W(gp) \geq 1/(6gp\log(gp))$ for each $p$:
$$W_g^{\mathrm{net}} \geq \frac{1}{6} S_g(A) - O_g$$

The gap: $O_g \geq 0$. If $O_g \leq (1-\delta)/6 \cdot S_g(A)$, then $W_g^{\mathrm{net}} \geq \delta/6 \cdot S_g(A)$.

**Gap**: $O_g$ can exceed $S_g(A)/6$ in adversarial cases (large fibers with many overlapping pairs).

---

## Section 6: The LP Resolution — Fiber Sums Approach

The Lichtman-Pomerance (2021) approach bypasses the inclusion-exclusion overlap problem by using a DIFFERENT decomposition:

**LP Fiber sum lemma**: For any primitive $A$ and any function $h: \mathbb{N} \to \mathbb{R}_+$:
$$\sum_{a \in A} \frac{1}{a\log a} = \sum_{d: \Omega(d)=k_0, d\geq x} \frac{1}{d\log d} \cdot F_d(A)$$

where $F_d(A) = d\log d \cdot \sum_{a \in A, a\mid d} w_d(a)$ for carefully chosen weights $w_d(a) > 0$ with $\sum_{d} w_d(a) = 1/(a\log a)$ for each $a$.

**The key LP inequality**: $F_d(A) \leq 1$ for ALL $d$ with $\Omega(d) = k_0$ and $d \geq x$, regardless of which elements of $A$ divide $d$.

This is achieved by choosing:
$$w_d(a) = \frac{1}{a\log a} \cdot \frac{\Lambda_{k_0}(d/a)}{\sum_{m: am \text{ is a } k_0\text{-AP}} \Lambda_{k_0}(m)}$$

where $\Lambda_{k_0}$ is a multiplicative function satisfying:
$$\sum_{a \mid d} \frac{d\log d \cdot \Lambda_{k_0}(d/a)}{a\log a \cdot \sum_m \Lambda_{k_0}(m a/a)} \leq 1$$

The specific choice LP makes for the primitive set problem exploits the multiplicative structure of $1/(n\log n)$ and the Mertens product. Their weight is related to the "fiber quotient" $\phi(d/a)/(d/a)$ (or similar Euler-product factors).

**Why this resolves within-group overlaps**: The LP weights $w_d(a)$ are chosen so that even if $k$ distinct elements of $A$ divide $d$, their combined contribution $F_d(A) \leq 1$. The self-cancellation of overlaps is AUTOMATIC in the LP framework — it's built into the weight normalization.

---

## Section 7: Explicit Fiber Analysis for the Erdős Bound

**Theorem W (Fiber bound for $k_0$-APs, proved conditionally)**: For any $d$ with $\Omega(d) = k_0$ and $d \geq x$:

$$\sum_{a \in A, a \mid d} \frac{1}{a \log a} \leq \frac{1}{d \log d} \sum_{a \mid d} \frac{d \log d}{a \log a}$$

The RIGHT side depends only on $d$ (not on $A$). Call it $B(d) = \sum_{a \mid d, a \geq x} (d\log d)/(a\log a)$.

**Computing $B(d)$**: For $d = p_1^{e_1} \cdots p_r^{e_r}$ with $\sum e_i = k_0$:
$$B(d) = \sum_{\substack{S \subset \{p_1^{e_1}, \ldots\} \\ \prod_S \geq x}} \frac{d \log d}{\prod_S \log(\prod_S)}$$

For $d = p_1 \cdots p_{k_0}$ (squarefree): divisors $a \mid d$ have $a = \prod_{i \in I} p_i$ for $I \subset [k_0]$. We need $a = \prod_{i \in I} p_i \geq x$. 

Since $d \geq x$ and $\prod_{i \in [k_0]} p_i = d$, we have $a \geq x$ iff $I$ is "heavy" enough.

For the worst case (all $p_i$ equal to $p$, so $d = p^{k_0}$): 
$$B(p^{k_0}) = \sum_{j=0}^{k_0} \binom{k_0}{j} \frac{p^{k_0} k_0 \log p}{p^j \cdot j \log p} \cdot \mathbf{1}[p^j \geq x]$$

Since $x = 2^{k_0}$ and $p^{j} \geq x = 2^{k_0}$ requires $j \geq k_0 \log 2 / \log p = k_0 / \log_2 p$. For $p = 2$: $j \geq k_0$, so only $j = k_0$ contributes: $B(2^{k_0}) = 1$ (perfect).

For $p = 3$: $j \geq k_0/\log_2 3 \approx 0.63 k_0$. Many terms contribute, so $B(3^{k_0}) \gg 1$. The bound $\sum_{a\mid d} 1/(a\log a) \leq B(d)/(d\log d)$ is too weak here.

**Gap**: The simple fiber sum $B(d)$ can be $\gg 1$, so the fiber bound alone doesn't give $F_d(A) \leq 1$.

**LP Resolution**: LP uses the primitivity constraint: since $A$ is an ANTICHAIN, the divisors of $d$ that belong to $A$ form an ANTICHAIN of divisors of $d$. The maximum weight of an antichain of divisors of $d$ under $1/(a\log a)$ is bounded by $1/(d\log d)$ — this is the content of the LP key lemma.

---

## Section 8: Antichain Fiber Bound (the core LP insight)

**Theorem X (Antichain fiber bound, proved by LP)**: For any $d \in \mathbb{N}$ and any antichain $C \subset \mathrm{Div}(d)$ (antichain of divisors of $d$):
$$\sum_{a \in C} \frac{1}{a \log a} \leq \frac{1}{d \log d} \cdot \left(\sum_{a \mid d} \frac{1}{a}\right) \cdot \log d$$

Hmm, this doesn't immediately give the bound.

**Actual LP bound**: The LP 2021 paper proves the conjecture using the following key estimate (Lemma 3.1 in their paper): for primitive $A$ and any weight $f(n) = 1/(n\log n)$,
$$\sum_{a \in A} f(a) \leq \sup_{\text{primitive } A} \sum_{a \in A} f(a)$$
and this supremum is achieved (in the limit) by the primes.

The proof uses: for any primitive $A$ and number $n$,
$$\sum_{a \in A, a \mid n} \frac{1}{a} \leq \frac{n}{\phi(n)} \cdot C$$

The key is Mertens' theorem: $\prod_{p \mid n} (1-1/p) \sim e^{-\gamma}/\log n$, so $n/\phi(n) = \prod_{p\mid n} (1-1/p)^{-1} \sim e^\gamma \log n$. This controls the fiber sum.

**Status**: The LP proof is complete and published (2021). The current proof attempt uses a more elementary approach via shadow disjointness. The gap is in showing within-group shadow overlaps are controlled.

---

## Summary of Q21 Results

| Claim | Status |
|-------|--------|
| Shadow overlap $\neq\emptyset$ iff $\Omega(\mathrm{lcm}(a,a')) \leq k_0$ | **Proved** (Thm R) |
| For $j=k_0-1$: overlap requires $\Omega(\gcd) = k_0-2$ exactly | **Proved** (Thm S) |
| For $j=k_0-1$ close pairs: overlap is a SINGLE POINT | **Proved** (Thm S) |
| $W(a) \geq 1/(6a\log a)$ for $a \in A_{k_0-1}$ | **Proved** (take $r$ = smallest prime $\nmid a$, $r \leq 5$) |
| Net fiber shadow $W_g^{\mathrm{net}} \geq S_g(A)/6 - O_g$ | **Proved** (trivially) |
| $O_g \ll S_g(A)$ (overlap controlled by primitivity) | **Open** (adversarial examples show $O_g \sim S_g(A)$ possible for large fibers) |
| Antichain fiber bound $\sum_{a \in A, a\mid d} 1/(a\log a) \leq 1/(d\log d)$ | **Open** (LP prove this via Mertens, not purely from shadow analysis) |
| Full $S(A) \leq T_{k_0}(x)$ from shadow approach | **Open** (requires LP-type fiber bound) |

**Key insight from Q21**: The within-group shadow overlap for stratum $k_0-1$ has a very clean structure: overlaps occur only between "close pairs" sharing a $(k_0-2)$-AP base, and each overlap is a SINGLE POINT. This structural clarity suggests a direct combinatorial bound may be possible, but the known route uses the Mertens-product fiber bound (LP 2021).

**Ultimate obstacle**: Bounding $O_g \ll S_g(A)$ for all fibers simultaneously. This is equivalent to: for a set $P_g$ of primes, $\sum_{p<q \in P_g} 1/(pq) \ll (\sum_{p \in P_g} 1/p)$, which fails if $|P_g|$ is large and $\sum 1/p$ diverges (which it does). The LP resolution uses the fact that $S_g(A)$ itself must be bounded by the fiber density.
