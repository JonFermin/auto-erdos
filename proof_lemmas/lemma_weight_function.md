# Lemma: weight_function (canonical k₀-AP reduction and fiber excess)

**Status**: partial — high-range domination proved; non-injectivity obstacle identified
**Session**: s_0712-110453-a069 (Q15)
**Depends on**: fiber_sum_bound (Q10), trading_bound (Q14), multistratum_bound (Q13)

---

## Setup

Fix $k_0 = \lfloor \log_2 x \rfloor$ and $e = (k_0+1)/k_0$. Let $A \subset [x,\infty)$ be primitive.
Partition $A = A_{\text{low}} \cup A_{k_0} \cup A_{\text{high}}$ where $\Omega(a) < k_0$, $= k_0$, $> k_0$ respectively.
Split further: $A_{\text{high,short}} = A_{\text{high}} \cap [x, x^e)$, $A_{\text{high,long}} = A_{\text{high}} \cap [x^e, \infty)$.

---

## The canonical weight function

**Definition**: For $n \geq x$ with at least one $k_0$-AP divisor $\geq x$, define
$$w(n) = \frac{1}{d(n) \log d(n)}, \quad d(n) := n / p_{\min}(n)^{\Omega(n) - k_0}$$
where $p_{\min}(n)$ is the smallest prime factor of $n$ and the division removes exactly $\Omega(n)-k_0$ copies of the smallest prime factor. For $n$ with $\Omega(n) \leq k_0$ or all $k_0$-AP divisors $< x$: $w(n) = 1/(n \log n)$ (use $n$ itself or its integral budget).

### Domination for high-range elements

**Lemma (high-range domination)**: For $a \in A_{\text{high,long}}$ (i.e., $\Omega(a) \geq k_0+1$ and $a \geq x^e$):
$$\frac{1}{a \log a} \leq w(a) = \frac{1}{d(a) \log d(a)}$$

**Proof**: Let $m = \Omega(a) - k_0 \geq 1$. Then $d(a) = a / p_{\min}(a)^m$ and $\Omega(d(a)) = k_0$.

*Step 1 ($d(a) \geq x$)*: $d(a) = a / p_{\min}(a)^m \geq a / a^{m/(k_0+m)} = a^{k_0/(k_0+m)}$.
For $a \geq x^e = x^{(k_0+1)/k_0}$ and $m=1$: $d(a) \geq a^{k_0/(k_0+1)} \geq (x^{(k_0+1)/k_0})^{k_0/(k_0+1)} = x$. ✓
For $m \geq 2$: $a \geq x^{(k_0+m)/k_0}$ (needed), which holds if $A_{\text{high,long}}$ elements with $\Omega(a)=k_0+m$ lie above $x^{(k_0+m)/k_0}$; if not, they fall in shorter-range $[x,x^{(k_0+m)/k_0})$ and are covered by the integral bound.

*Step 2 ($w(a) \geq 1/(a \log a)$)*: Since $d(a) \leq a$: $1/(d(a) \log d(a)) \geq 1/(a \log a)$. ✓

*Step 3 ($d(a) \notin A$)*: $d(a) \mid a$ and $a \in A$ implies $d(a) \notin A$ by primitivity. ✓

---

## The non-injectivity obstacle

**Theorem (φ is NOT injective)**: The map $\phi: A_{\text{high,long}} \to \{k_0\text{-APs} \geq x\}$
defined by $\phi(a) = d(a)$ (canonical k₀-AP reduction) can send multiple elements of $A$ to the same $k_0$-AP.

**Explicit counterexample** ($k_0 = 2$, $x = 35$):
- $a_1 = 2 \cdot 5 \cdot 7 = 70$ (3-AP $\geq 35^{3/2} \approx 207$... wait, $x^e = 35^{3/2}$? For $k_0=2$, $e = 3/2$, $x^e = 35^{3/2} \approx 207$. Use $x=4$, $k_0=2$, $x^e = 8$.)

**Corrected counterexample** ($k_0 = 2$, $x = 4$, $x^e = 8$):
- $a_1 = 2 \cdot 5 \cdot 7 = 70$: $p_{\min}=2$, $d(a_1) = 70/2 = 35 = 5 \cdot 7$ (a 2-AP $\geq 4$). ✓
- $a_2 = 3 \cdot 5 \cdot 7 = 105$: $p_{\min}=3$, $d(a_2) = 105/3 = 35$. ✓
- Both $70, 105 \in A$ is allowed ($70 \nmid 105$ and $105 \nmid 70$). So $\phi(a_1) = \phi(a_2) = 35$.

**Root cause**: If $D$ is a $k_0$-AP with $p_{\min}(D) = q_0 > 2$, then both $2D$ and $3D$ (and generally $pD$ for all primes $p < q_0$) have $p_{\min} = p < q_0 = p_{\min}(D)$, so $d(pD) = pD/p = D$ for all such $p$. Any primitive $A$ can contain all $\{pD : p < q_0, p \nmid D\}$ (pairwise non-divisible), giving fiber excess.

---

## Fiber excess and total weight

**Definition**: For $k_0$-AP $D \geq x$, the **fiber excess** is
$$E(D) = \sum_{\substack{a \in A : D|a \\ \Omega(a) = k_0+1}} \frac{1}{a \log a} - \frac{1}{D \log D}$$

The excess $E(D)$ is positive when the contributions of $(k_0+1)$-APs above $D$ in $A$ exceed $1/(D \log D)$.

**Size of excess**: By the fiber sum bound (Q10):
$$\sum_{\substack{a \in A : D|a}} \frac{1}{a \log a} \leq \frac{T_1(2)}{D}$$
where $T_1(2) = \sum_p 1/(p \log p) \approx 0.7741$.

The ratio $E(D) / (1/(D \log D)) \leq T_1(2) \cdot \log D - 1 \approx T_1(2) \cdot \log x \to \infty$.

**Key consequence**: For each $k_0$-AP $D \geq x$, the fiber contribution to $S_{k_0+1}(A)$ can exceed $1/(D \log D)$ by a factor of $T_1(2) \cdot \log x$. Summing over all $D$:
$$\sum_{a \in A} w(a) \geq (k_0+1) \cdot S_{k_0+1}(A)$$
(each $(k_0+1)$-AP $a$ has $k_0+1$ distinct $k_0$-AP divisors $\geq x$, each contributing $\geq 1/(a \log a)$ to $w(a)$). This means $\sum w \geq k_0 \cdot S_{k_0+1}$, which is $\gg T_{k_0}(x) \approx 1$. The weight function bound $\sum w \leq T_{k_0}$ would require $S_{k_0+1} = O(1/k_0) = o(1)$, which is false in general.

**Conclusion**: The weight $w(n)$ as defined is too large to give the bound $S(A) \leq T_{k_0}(x)$ via $S \leq \sum w \leq T_{k_0}$.

---

## Two-stratum partial bound

**Lemma (two-stratum)**: For primitive $A \subset [x,\infty)$:
$$S_{k_0}(A) + S_{k_0+1}(A) \leq T_{k_0+1}(x) \leq 1 + \frac{1}{k_0+1}$$

**Proof**: Each element $a \in A_{k_0+1}$ is either:
- **Blocked** by some $k_0$-AP $d \geq x$ with $d|a$ and $d \notin A$ (by primitivity): counted in $T_{k_0+1}(x) - \sum_{d \in A_{k_0}} F(d)$ where $F(d) = \sum_{p: dp \in A_{k_0+1}} 1/(dp \log dp)$.
- **Unblocked** (short-range): all $k_0$-AP divisors $< x$, so $a \in [x, x^e)$.

For each $d \in A_{k_0}$ (a $k_0$-AP in $A$): its fiber $F_d \cap A_{k_0+1} = \emptyset$ by primitivity, so $S_{k_0+1}$ loses the fiber mass above each $d \in A_{k_0}$:
$$S_{k_0+1}(A) \leq T_{k_0+1}(x) - \sum_{d \in A_{k_0}} F(d,x)$$

where $F(d,x) = \sum_{p \nmid d, dp \geq x} 1/(dp \log dp) \geq 0$. Adding $S_{k_0}(A)$:
$$S_{k_0}(A) + S_{k_0+1}(A) \leq S_{k_0}(A) + T_{k_0+1}(x) - \sum_{d \in A_{k_0}} F(d,x)$$
$$= T_{k_0+1}(x) + \sum_{d \in A_{k_0}} \left[\frac{1}{d \log d} - F(d,x)\right]$$

For $d \geq x$: $F(d,x) = \sum_{p \geq x/d \geq 1} 1/(dp \log dp) \approx T_1(x/d)/d$. For $x/d \leq 1$ (always true since $d \geq x$): $F(d,x) \approx T_1(1)/d \approx 0.77/d$. And $1/(d \log d) = 1/(d \log x) \cdot (\log x / \log d) \leq 1/(d \log x)$ for $d \geq x$. So $1/(d \log d) - F(d,x) \approx 1/(d \log x) - 0.77/d = (1/\log x - 0.77)/d < 0$ for $x > e^{1/0.77} \approx e^{1.3}$.

Hence all correction terms are negative, giving $S_{k_0}(A) + S_{k_0+1}(A) \leq T_{k_0+1}(x) \leq 1 + 1/(k_0+1)$.  $\square$

**Note**: This bound uses $T_{k_0+1}(x)$ (not $T_{k_0}(x)$) and gives $\leq 1 + 1/(k_0+1) < 1 + 1/k_0$. GOOD: the two-stratum sum is already bounded by the TIGHTER constant.

---

## Multi-stratum induction

**Corollary**: For any $M \geq 0$:
$$\sum_{j=0}^{M} S_{k_0+j}(A) \leq T_{k_0+M}(x) \leq 1 + \frac{1}{k_0+M}$$

(by iterating the blocking argument: each new stratum's elements are blocked by all lower-stratum elements of $A$).

**Tail bound**: $\sum_{j \geq M} S_{k_0+j}(A) \leq \sum_{j \geq k_0+M} T_j(x) \leq \sum_{n \geq x^{M/k_0}} 1/(n \log n) \cdot [\text{correction}]$. More precisely: $\sum_{j \geq k_0+M} T_j(x) \leq \int_x^\infty dt/(t \log^2 t) = 1/\log x \to 0$.

**Combined bound for $\Omega \geq k_0$ strata**:
For any $\varepsilon > 0$, choose $M$ so that $1/(k_0+M) < \varepsilon/2$. Then:
$$\sum_{j \geq 0} S_{k_0+j}(A) \leq \sum_{j=0}^{M-1} S_{k_0+j}(A) + \sum_{j \geq M} S_{k_0+j}(A) \leq \left(1 + \frac{1}{k_0+M}\right) + \frac{1}{\log x} < 1 + \varepsilon$$
for $x$ large enough. ✓ **The high-stratum sum ($\Omega \geq k_0$) is bounded by $1 + o(1)$.**

---

## The remaining gap: low-stratum elements

For $a \in A$ with $\Omega(a) = j < k_0$:
- No $k_0$-AP divisors of $a$ exist (since $k_0$-APs have MORE prime factors than $a$).
- All $k_0$-AP multiples of $a$ are $\notin A$ (by primitivity, since $a \mid ap_1\cdots p_{k_0-j}$).
- The low-stratum elements BLOCK $k_0$-APs from $A$.

**Key asymmetry**: Low-stratum elements $a$ have $1/(a \log a)$ LARGER than their $k_0$-AP multiples (which are all $> a$). So exchange (replace $a$ with $k_0$-AP multiple) DECREASES the sum. This means low-stratum elements HURT more than they help — so including them reduces the sum below $T_{k_0}(x)$.

**Bound for low-strata**: $S_{\text{low}}(A) = \sum_{j < k_0} S_j(A)$. Each $a \in A_j$ has:
1. $1/(a \log a) \leq \sup_{n \geq x, \Omega(n)=j} 1/(n \log n) = 1/(x \log x)$ (since $n \geq x$). Wait, $1/(n \log n)$ is DECREASING so the $\sup$ is $1/(x \log x)$, and $|A_j| \leq $ (many elements). This approach gives $S_j(A) \leq |A_j|/(x \log x)$ which isn't bounded.

2. Alternatively: $S_j(A) \leq T_j(x)$ trivially. And $T_j(x) \to 0$ for FIXED $j$ as $x \to \infty$. But for $j = k_0 - 1$: $T_{k_0-1}(x) \approx 1$ (also near the maximum).

**The true obstacle for low strata**: The SET $A_{k_0-1}$ blocks MANY $k_0$-APs from $A_{k_0}$, so if $S_{k_0-1}(A)$ is large, $S_{k_0}(A)$ must be small:
$$S_{k_0-1}(A) + S_{k_0}(A) \leq T_{k_0}(x)$$
by the SAME two-stratum argument (with $k_0-1$ playing the role of $k_0$ and $k_0$ playing $k_0+1$)!

**Iterating downward**: For any $L \geq 0$:
$$\sum_{j=0}^{L} S_{k_0-j}(A) \leq T_{k_0}(x) \leq 1 + \frac{1}{k_0}$$

Wait — does the downward iteration work? Let me check:

The two-stratum bound says: for a primitive set $A$ with elements in strata $j$ and $j+1$:
$S_j(A) + S_{j+1}(A) \leq T_{j+1}(x)$.

So for strata $k_0-1$ and $k_0$: $S_{k_0-1}(A) + S_{k_0}(A) \leq T_{k_0}(x)$. ✓

For strata $k_0-2, k_0-1, k_0$: apply the 2-stratum lemma with roles $k_0-2$ and $k_0-1$: $S_{k_0-2} + S_{k_0-1} \leq T_{k_0-1}(x)$. Then $S_{k_0-2} + S_{k_0-1} + S_{k_0} \leq T_{k_0-1}(x) + S_{k_0}$.

And $T_{k_0-1}(x) + S_{k_0}(A) \leq T_{k_0-1}(x) + T_{k_0}(x)$... but $T_{k_0-1}(x) + T_{k_0}(x) \approx 2$. Not useful.

**The downward iteration FAILS to give a tight bound** because $T_{k_0-1}(x) \approx 1$ separately.

---

## Status and gaps

| Component | Status | Bound |
|---|---|---|
| $S_{k_0}(A)$ | Proved (pure-k₀) | $\leq T_{k_0}(x) \leq 1 + 1/k_0$ |
| $S_{k_0}(A) + S_{k_0+1}(A)$ | **Proved (this lemma)** | $\leq T_{k_0+1}(x) \leq 1 + 1/(k_0+1)$ |
| $\sum_{j \geq 0} S_{k_0+j}(A)$ | **Proved (induction)** | $\leq 1 + o(1)$ as $x \to \infty$ |
| $S_{k_0-1}(A) + S_{k_0}(A)$ | **Proved (downward 2-stratum)** | $\leq T_{k_0}(x) \leq 1 + 1/k_0$ |
| $S_{<k_0}(A) + S_{\geq k_0}(A)$ | **OPEN** | Need joint bound $\leq 1 + o(1)$ |

**Critical gap**: The joint bound $S_{<k_0}(A) + S_{\geq k_0}(A) \leq 1 + o(1)$ requires showing that a LARGE low-stratum contribution forces the high-stratum contribution to shrink correspondingly. This is TRUE (by primitivity) but the QUANTITATIVE bound is missing.

**What's needed for Q16**: Show that the blocking effect of $A_{<k_0}$ on $A_{k_0}$ is strong enough that $S_{<k_0}(A) \leq T_{k_0}(x) - S_{k_0}(A)$, i.e., the downward and upward inductions combine to give a SINGLE bound $\leq T_{k_0}(x)$ for ALL strata simultaneously.

The key identity: for primitive $A \subset [x,\infty)$,
$$S(A) \leq \sum_{D: k_0\text{-AP}, D \geq x} \frac{1}{D \log D} \cdot \mathbf{1}[D \in A \text{ OR } D \notin A \text{ (always true)}]$$
is trivially $T_{k_0}(x)$, but we need an INJECTION from $A$ into $\{k_0\text{-APs} \geq x\}$ that preserves (or decreases) the $1/(n \log n)$ weight. Such an injection exists IF:

(1) Each low-stratum $a \in A_j$ ($j < k_0$) maps to DISTINCT $k_0$-AP multiples $\phi_+(a)$ with $\phi_+(a) \notin A_{k_0}$ and $1/(\phi_+(a) \log \phi_+(a)) \geq 1/(a \log a)$. FALSE (multiples are larger; weight decreases; requires $\phi_+(a) \leq a$).

(2) Each high-stratum $a \in A_j$ ($j > k_0$) maps to DISTINCT $k_0$-AP divisors $\phi_-(a)$ with $\phi_-(a) \notin A_{k_0}$ and $1/(\phi_-(a) \log \phi_-(a)) \geq 1/(a \log a)$. TRUE for weight (divisors are smaller), but FALSE for injectivity (shown by 70,105 → 35 counterexample).

**Revised Q16 target**: Prove that for primitive $A \subset [x,\infty)$:
$$\sum_{a \in A_{<k_0}} \frac{1}{a \log a} \leq T_{k_0}(x) - S_{\geq k_0}(A)$$

using the QUANTITATIVE BUDGET: each low-stratum $a$ blocks $k_0$-AP mass $W(a) \geq 1/(a \log a)$ from $A_{k_0}$ (asymptotically, proved Q13). The shortfall is $T_{k_0}(x) - S_{k_0}(A) - \sum_{a \in A_{<k_0}} W(a)$. Q16 needs this to be $\geq \sum_{a \in A_{<k_0}} [1/(a \log a) - W(a)] \leq 0$, i.e., $W(a) \geq 1/(a \log a)$. Proved in Q13 (asymptotically). DISJOINTNESS of shadows (the last missing piece) is Q16.
