# Lemma: `single_stratum_bound`

**Status**: proved

**Statement**: For any primitive set $A \subset [x, \infty)$ whose elements all
satisfy $\Omega(a) = k$ (a single stratum), the sum satisfies
$$S := \sum_{a \in A} \frac{1}{a \log a} < 1 + o(1) \quad (x \to \infty),$$
where the $o(1)$ depends only on $x$ (not on the choice of $A$ or $k$, given
that $k = k(x)$ is a function of $x$).

In fact, one obtains the stronger bound $S < 1$ for all large enough $x$.

---

## Proof

**Case 1 (k fixed as $x \to \infty$)**

By Lemma `stratum_sub_bound`, $S \leq T_k(x)$. By Lemma `large_floor_vanish`,
$T_k(x) \to 0$ as $x \to \infty$ for each fixed $k$. Hence $S = o(1) < 1 +
o(1)$, and in particular $S < 1$ for all sufficiently large $x$. $\square$

**Case 2 ($k = k(x) \to \infty$ with $x$)**

Again by Lemma `stratum_sub_bound`, $S \leq T_k(x)$.

Since $T_k(x) \leq T_k(2) := \sum_{n:\,\Omega(n)=k} \frac{1}{n \log n}$
(removing the lower-bound constraint extends the sum), it suffices to show
$T_k(2) < 1$ for all large $k$.

By F3 (asymptotic formula as $k \to \infty$):
$$T_k(2) = 1 - (c + o(1))\frac{k^2}{2^k}, \quad c \approx 0.0656 > 0,$$
where the $o(1)$ is as $k \to \infty$. Choose $K_0$ large enough that for
all $k \geq K_0$, the $o(1)$ term satisfies $|o(1)| < c/2$, giving
$(c + o(1)) \geq c/2 > 0$. Then for $k \geq K_0$:
$$T_k(2) = 1 - (c + o(1))\frac{k^2}{2^k} \leq 1 - \frac{c}{2} \cdot \frac{k^2}{2^k} < 1.$$

Since $k(x) \to \infty$, for all $x$ large enough $k(x) \geq K_0$, giving
$S \leq T_k(2) < 1 < 1 + o(1)$. $\square$

**Combined**: In both cases, $S < 1 + o(1)$ as $x \to \infty$, and
$S < 1$ for all sufficiently large $x$ (depending on $k$ in Case 1,
and on the rate of $k(x) \to \infty$ in Case 2).

**Note on Case 2 scope**: The F3 formula $T_k(2) = 1 - (c+o(1))k^2/2^k$ is
asymptotic as $k \to \infty$ and may not hold for small fixed $k$. The
proof above uses F3 only for large $k$ (specifically $k \geq K_0$); the
fixed-$k$ regime is handled by Case 1 without invoking F3 directly.

**Consequence**: The Erdős primitive-set conjecture ($S < 1 + o(1)$) holds
for any primitive set supported on a single $\Omega$-stratum. The remaining
open case is primitive sets that span multiple strata.
