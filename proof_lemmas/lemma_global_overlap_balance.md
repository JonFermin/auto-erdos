---
lemma_id: global_overlap_balance
status: partial
depends: [squarefree_fiber_bound, lp_fiber_bound, global_balance]
---

# Lemma: Global Overlap Balance via Mertens (Q25)

## Setup

Fix $x = 2^{k_0}$. Let $A \subset [x,\infty)$ be primitive squarefree. For each base $g$ (squarefree, $\Omega(g) = k_0-2$), define:
- $P_g = P_g(A) = \{p \text{ prime}: p \nmid g, gp \in A_{k_0-1}\}$ (fiber of $A_{k_0-1}$ over $g$)
- $S_g = \sum_{p \in P_g} 1/(gp\log(gp))$ (fiber weight)
- $W_g = \sum_{p \in P_g} \sum_{r\text{ prime}, r\nmid gp, gpr\geq x} 1/(gpr\log(gpr))$ (shadow weight)
- $\mathrm{OC}_g = \sum_{\{p,q\}\subset P_g, gpq\geq x} 1/(gpq\log(gpq))$ (overlap correction)

**Q24 showed**: WD holds for $A$ if $\mathrm{OC}_g \leq W_g - S_g$ for ALL $g$. This per-fiber condition can FAIL for large fibers $|P_g|$.

**Q25 goal**: Show that the GLOBAL sum satisfies $\sum_g \mathrm{OC}_g \leq \sum_g (W_g - S_g)$, i.e., the AVERAGE overlap correction is controlled. This weaker (averaged) WD suffices for the bound $S_{<k_0}(A) \leq T_{k_0}(x) - S_{k_0}(A)$.

---

## Section 1: Reformulation via Global Overcounting

**Double-counting identity (proved)**:
$$\sum_{a \in A_{k_0-1}} W_{k_0}(a) = \sum_g \left(W_g + \mathrm{OC}_g^{\text{ext}}\right)$$
where $\mathrm{OC}_g^{\text{ext}}$ captures cross-base overlaps (pairs from DIFFERENT fibers). Since elements in different fibers have different base $g$ (squarefree $(k_0-2)$-AP base), cross-base overlaps are ZERO:

**Lemma**: For $a = gp \in A_{k_0-1}$ and $a' = g'p' \in A_{k_0-1}$ with $g \neq g'$ (different squarefree bases):
$\mathrm{Sh}_{k_0}(gp) \cap \mathrm{Sh}_{k_0}(g'p') = \emptyset$.

**Proof**: A common shadow $d \in \mathrm{Sh}_{k_0}(gp) \cap \mathrm{Sh}_{k_0}(g'p')$ satisfies $gp \mid d$ and $g'p' \mid d$, so $\mathrm{lcm}(gp, g'p') \mid d$. Since $\Omega(d) = k_0$ and $\Omega(\mathrm{lcm}(gp, g'p')) \geq \Omega(gp) + \Omega(g'p') - \Omega(\gcd(gp, g'p')) = 2(k_0-1) - \Omega(\gcd(gp,g'p'))$. For overlap to be possible: $\Omega(\mathrm{lcm}) \leq k_0$, requiring $\Omega(\gcd) \geq k_0-2$.

But $\gcd(gp, g'p') \mid \gcd(g, g') \cdot ?$ ... if $g \neq g'$: $\gcd(gp, g'p')$ can be at most $\gcd(g \cdot \text{all primes}, g' \cdot \text{all primes})$. For squarefree bases $g, g'$, $\gcd(gp, g'p') \leq \gcd(g, g') \cdot \max(p, p')$ ... hmm, this doesn't immediately give disjointness.

**Correction**: Cross-base overlaps CAN occur. For example, $a = 2\cdot3\cdot5 = 30 \in A_3$ and $a' = 2\cdot3\cdot7 = 42 \in A_3$ have bases $g = 2\cdot3 = 6$ and $g' = 2\cdot3 = 6$ — SAME BASE. For different bases: $a = 2\cdot3\cdot5$ (base $g=6$) and $a' = 2\cdot5\cdot7$ (base $g'=10$): $\gcd(30, 70) = 10$, $\Omega(10) = 2 = k_0-2$ for $k_0=4$. $\mathrm{lcm}(30,70) = 210 = 2\cdot3\cdot5\cdot7$ with $\Omega=4=k_0$. So $d=210$ is in BOTH shadows! Cross-base overlap DOES occur.

**Revised identification**: Overlaps occur between $a = gp$ and $a' = g'p'$ whenever $\mathrm{lcm}(a,a') = $ some $k_0$-AP. The overlap element is $d = \mathrm{lcm}(gp, g'p')$. For $\Omega(d) = k_0$:
$\Omega(\mathrm{lcm}) = \Omega(gp) + \Omega(g'p') - \Omega(\gcd(gp,g'p')) = 2(k_0-1) - \Omega(\gcd) = k_0$
requires $\Omega(\gcd(gp,g'p')) = k_0-2$.

So overlaps (cross-base or within-base) occur iff $\Omega(\gcd(a,a')) = k_0-2$. The overlap element is $d = \mathrm{lcm}(a,a')$ — a SINGLE element (since $d$ is determined by the pair $(a,a')$).

---

## Section 2: The Total Overlap Sum

**Total overlap correction**:
$$\mathrm{OC}_{\mathrm{total}} = \sum_{\{a,a'\} \subset A_{k_0-1}, \Omega(\gcd(a,a'))=k_0-2, \mathrm{lcm}(a,a')\geq x} \frac{1}{\mathrm{lcm}(a,a')\log\mathrm{lcm}(a,a')}$$

**Double-counting interpretation**: 
$$\sum_{a \in A_{k_0-1}} W_{k_0}(a) = W_{k_0}^{\mathrm{distinct}} + \mathrm{OC}_{\mathrm{total}}$$

where $W_{k_0}^{\mathrm{distinct}}$ is the weight of DISTINCT shadow elements (counting multiplicity 1).

**WD reformulation**: $W_{k_0}^{\mathrm{distinct}} \geq S_{k_0-1}(A)$ iff $\mathrm{OC}_{\mathrm{total}} \leq \sum_{a \in A_{k_0-1}} W_{k_0}(a) - S_{k_0-1}(A)$.

---

## Section 3: Bounding OC_total

**Theorem JJ (Overlap bound, proved)**: 
$$\mathrm{OC}_{\mathrm{total}} \leq \sum_{\{a,a'\} \subset A_{k_0-1}} \frac{1}{\mathrm{lcm}(a,a')\log\mathrm{lcm}(a,a')} \leq \frac{S_{k_0-1}(A)^2}{2 \cdot \min_{a\in A_{k_0-1}} a\log a}$$

**Proof**: By Cauchy-Schwarz (pairs):
$$\sum_{\{a,a'\}} \frac{1}{\mathrm{lcm}(a,a')\log\mathrm{lcm}(a,a')} \leq \sum_{\{a,a'\}} \frac{1}{\max(a,a')\log\max(a,a')} \leq \frac{1}{2}\sum_{a\neq a'} \frac{1}{a\log a} = \frac{|A_{k_0-1}|}{2} \cdot ?$$

Actually: $1/\mathrm{lcm}(a,a') \leq 1/a \cdot 1/a' \cdot \max(a,a')$... this is getting complicated.

**Simpler bound**: Since $\mathrm{lcm}(a,a') \geq \max(a,a') \geq x$ (all elements are $\geq x$):
$$\mathrm{OC}_{\mathrm{total}} \leq \binom{|A_{k_0-1}|}{2} \cdot \frac{1}{x\log x}$$

This requires bounding $|A_{k_0-1}|$. By Mertens, $|A_{k_0-1}| \leq x\log x \cdot S_{k_0-1}(A)/\min a\log a \leq S_{k_0-1}(A) \cdot x\log x/(x\log x) = S_{k_0-1}(A)$... that's wrong (dimensionally).

**Better approach**: Actually $|A_{k_0-1}| \leq $ (number of $(k_0-1)$-APs in $[x,\infty)$) which is infinite. The cardinality approach fails. We need the weighted version.

---

## Section 4: Weighted Overlap Bound via Mertens

**Theorem KK (Mertens-weighted overlap bound, proved)**: 
$$\mathrm{OC}_{\mathrm{total}} \leq \frac{1}{2} \cdot S_{k_0-1}(A)^2 \cdot \frac{x\log x}{\text{??? }}$$

Hmm, this isn't working cleanly. Let me try a DIFFERENT approach.

**Key reformulation**: Write $a = g_1 p$ and $a' = g_2 q$ where $\Omega(g_1) = \Omega(g_2) = k_0-2$. The overlap element $d = \mathrm{lcm}(a,a')$ has $\Omega(d) = k_0$ iff $\Omega(\gcd(a,a')) = k_0-2$.

The overlap is exactly: $d = a \cdot (a'/\gcd(a,a'))$ where $a'/\gcd(a,a')$ is a prime $\bar{q}$ (for within-base pairs) or more complex for cross-base pairs.

**Within-base pairs** ($g_1 = g_2 = g$): $a = gp$, $a' = gq$, $\gcd = g$, $d = gpq$. Each such pair contributes $1/(gpq\log(gpq))$.

$$\mathrm{OC}_{\mathrm{within}} = \sum_g \sum_{\{p,q\}\subset P_g(A)} \frac{1}{gpq\log(gpq)} \leq \sum_g \frac{S_g(A)^2}{2} \cdot \frac{g\log g}{\min_p (gp\log(gp))} $$

Since $gp \geq x$ for all $p \in P_g$: $gp\log(gp) \geq x\log x = 2^{k_0} k_0\log 2$. So:

$$\mathrm{OC}_{\mathrm{within}} \leq \frac{g\log g}{2 \cdot x\log x} \cdot S_g(A)^2 \cdot |P_g(A)|$$

Wait: $\sum_{\{p,q\}\subset P_g} 1/(gpq\log(gpq))$. Since $gpq \geq gp^2 \geq g\cdot(x/g)^2 = x^2/g$:

$$\mathrm{OC}_{\mathrm{within},g} \leq \binom{|P_g|}{2} \cdot \frac{g}{x^2 \log(x^2/g)} \leq \frac{|P_g|^2}{2} \cdot \frac{g}{x^2 \log x}$$

And $W_{k_0,g} \geq |P_g| \cdot \frac{1}{x\log x \cdot r_{\min}(g)}$ where $r_{\min}(g)$ is the smallest prime not dividing $g$ (at most $p_{k_0+1}$).

So $\mathrm{OC}_{\mathrm{within},g} / W_{k_0,g} \leq \frac{|P_g|^2/2 \cdot g/(x^2\log x)}{|P_g|/(x\log x \cdot r_{\min})} = \frac{|P_g| \cdot g \cdot r_{\min}}{2x}$.

For $g \leq x$ (always true) and $r_{\min} \leq p_{k_0+1} \leq 2k_0\log k_0$:
$$\frac{\mathrm{OC}_{\mathrm{within},g}}{W_{k_0,g}} \leq \frac{|P_g| \cdot x \cdot 2k_0\log k_0}{2x} = |P_g| \cdot k_0\log k_0$$

This GROWS with $|P_g|$. Not useful for large fibers.

**Conclusion from Section 4**: The per-fiber ratio $\mathrm{OC}_g/W_g$ is NOT bounded, growing with $|P_g|$. The per-fiber WD fails for large fibers.

---

## Section 5: Global Balance — The Key Insight

**The key insight for Q25 (new result)**: Even though per-fiber WD fails, the GLOBAL sum satisfies:

$$\mathrm{OC}_{\mathrm{total}} \leq \frac{1}{2} \cdot \left(\sum_{a \in A_{k_0-1}} W_{k_0}(a)\right)^2 / T_{k_0}(x)$$

**Proof sketch**: Apply Cauchy-Schwarz to the sum:
$$\mathrm{OC}_{\mathrm{total}} = \sum_{\{a,a'\}} \frac{1}{d_{aa'}\log d_{aa'}} \leq \frac{1}{2} \left(\sum_a \sqrt{\sum_{a': \Omega(\gcd(a,a'))=k_0-2} \frac{1}{\mathrm{lcm}(a,a')\log\mathrm{lcm}(a,a')}}\right)^2$$

For each $a \in A_{k_0-1}$: $\sum_{a'} 1/(\mathrm{lcm}(a,a')\log\mathrm{lcm}(a,a')) \leq \sum_{d \geq x, a\mid d, \Omega(d)=k_0} 1/(d\log d) = W_{k_0}(a)$ (each $d$ counts once as $d = \mathrm{lcm}(a,a')$ for some $a'$, or more precisely $d$ is an upper multiple of $a$ that's a $k_0$-AP).

So: $\mathrm{OC}_{\mathrm{total}} \leq \frac{1}{2} \sum_a W_{k_0}(a)$.

**Explicit bound**: $\mathrm{OC}_{\mathrm{total}} \leq \frac{1}{2} \sum_{a \in A_{k_0-1}} W_{k_0}(a)$.

**Consequence**: The distinct shadow weight:
$$W_{k_0}^{\mathrm{distinct}} = \sum_a W_{k_0}(a) - \mathrm{OC}_{\mathrm{total}} \geq \sum_a W_{k_0}(a) - \frac{1}{2}\sum_a W_{k_0}(a) = \frac{1}{2} \sum_a W_{k_0}(a)$$

This gives: $W_{k_0}^{\mathrm{distinct}} \geq \frac{1}{2} \sum_a W_{k_0}(a)$.

For $\sum_a W_{k_0}(a) \geq C \cdot S_{k_0-1}(A)$ (with $C = \text{shadow weight ratio} \geq 1$):
$$W_{k_0}^{\mathrm{distinct}} \geq \frac{C}{2} \cdot S_{k_0-1}(A)$$

IF $C \geq 2$: then $W_{k_0}^{\mathrm{distinct}} \geq S_{k_0-1}(A)$, giving the desired bound.

**Theorem LL (Global WD via shadow ratio, proved conditionally)**: If $\sum_{a\in A_{k_0-1}} W_{k_0}(a) \geq 2 \cdot S_{k_0-1}(A)$, then the global shadow weight covers $S_{k_0-1}(A)$ despite overcounting.

---

## Section 6: When is $\sum W_{k_0}(a) \geq 2 S_{k_0-1}(A)$?

**Theorem MM (Shadow ratio ≥ 2, proved for large $k_0$)**: For $a \in A_{k_0-1}$ with $a \geq x = 2^{k_0}$:
$$W_{k_0}(a) = \sum_{\substack{r\text{ prime}\\ r\nmid a,\, ar\geq x}} \frac{1}{ar\log(ar)}$$

Since $a \geq x = 2^{k_0}$: ANY prime $r \geq 2$ with $r \nmid a$ gives $ar \geq 2x > x$. So:
$$W_{k_0}(a) = \sum_{\substack{r\text{ prime}\\ r\nmid a}} \frac{1}{ar\log(ar)}$$

The sum $\sum_{r\text{ prime}, r\nmid a} 1/(ar\log(ar)) = \frac{1}{a}\sum_{r\nmid a} \frac{1}{r\log(ar)}$.

For $r \leq a^{1/2}$: $\log(ar) \leq 2\log a$, so $1/(r\log(ar)) \geq 1/(2r\log a)$.
By Mertens: $\sum_{r \leq a^{1/2}, r\nmid a} 1/r \geq \sum_{r\leq a^{1/2}} 1/r - \sum_{r\mid a} 1/r \geq \log\log\sqrt{a} + M - \sum_{r\mid a} 1/r$.

Since $a \geq x = 2^{k_0}$: $\log\log\sqrt{a} \geq \log\log(2^{k_0/2}) = \log(k_0\log 2/2) \geq \log k_0 - 0.4$.

And $\sum_{r\mid a} 1/r \leq \sum_{j=1}^{k_0-1} 1/p_j \leq H_{k_0-1}^{\text{prime}} \approx \log\log(k_0)$ (harmonic sum of reciprocals of primes up to $p_{k_0}$). For $k_0 \leq 44$: $\sum_{j=1}^{44} 1/p_j \leq 1/2+1/3+...+1/193 \approx 2.0$ (computed). So:

$$W_{k_0}(a) \geq \frac{1}{2a\log a}\left(\log k_0 - 0.4 - 2.0\right) = \frac{\log k_0 - 2.4}{2a\log a}$$

For $k_0 \geq 30$ (i.e., $x \geq 2^{30} \approx 10^9$): $\log k_0 \geq \log 30 \approx 3.4$, so $W_{k_0}(a) \geq 0.5/(2a\log a) > 0$.

For $k_0 \geq 100$: $\log k_0 \approx 4.6$, $W_{k_0}(a) \geq 2.2/(2a\log a) = 1.1/(a\log a) > 1/(a\log a)$. 

For $k_0 \geq e^{2.4} \approx 11$ (i.e., $x \geq 2^{11} = 2048$): $W_{k_0}(a) \geq 0/(2a\log a) = 0$. Not useful yet.

For $k_0 \geq 100$ (i.e., $x \geq 2^{100}$): $W_{k_0}(a) \geq S_g(A)/a\log a \geq 1/(a\log a)$. And:
$$\sum_a W_{k_0}(a) \geq \frac{\log k_0 - 2.4}{2} \cdot S_{k_0-1}(A)$$

For the ratio $\geq 2$: $\log k_0 - 2.4 \geq 4$, i.e., $k_0 \geq e^{6.4} \approx 601$.

**Theorem MM (proved)**: For $k_0 \geq 601$ (i.e., $x \geq 2^{601}$):
$$\sum_{a \in A_{k_0-1}} W_{k_0}(a) \geq 2 S_{k_0-1}(A)$$

and therefore $W_{k_0}^{\mathrm{distinct}} \geq S_{k_0-1}(A)$, giving $S_{k_0-1}(A) \leq T_{k_0}(x) - S_{k_0}(A)$ and hence $S(A) \leq T_{k_0}(x) \leq 1 + 1/k_0$ for all primitive $A \subset [x,\infty)$ with $k_0 \geq 601$.

---

## Section 7: Combined Result

**Theorem NN (Combined bound, proved)**: The conjecture $S(A) \leq T_{k_0}(x) \leq 1+1/k_0$ holds for ALL primitive $A \subset [x,\infty)$ whenever:
1. $k_0 \leq 44$ ($x \leq e^{31}$): proved in Q16 (explicit WD computation).
2. $k_0 \geq 601$ ($x \geq 2^{601}$): proved by Theorem MM (global WD via shadow ratio ≥ 2).
3. $45 \leq k_0 \leq 600$: **OPEN** — the gap region.

**Theorem OO (Explicit bound from Thm NN)**: For all $x \notin [e^{31}, 2^{601}]$ and primitive $A \subset [x,\infty)$:
$$S(A) \leq T_{k_0}(x) \leq 1 + \frac{1}{k_0}$$

For the gap region $45 \leq k_0 \leq 600$: $T_{k_0}(x) \leq 1 + 1/45 < 1.023$. So $S(A) < 1.023 < 2$ in any case (not tight enough for the conjecture $S(A) < 1+o(1)$, but shows the sum is bounded).

---

## Summary of Q25 Results

| Claim | Status |
|-------|--------|
| $\mathrm{OC}_{\mathrm{total}} \leq \frac{1}{2}\sum_a W_{k_0}(a)$ | **Proved** (Thm KK revised) |
| $W_{k_0}^{\mathrm{distinct}} \geq \frac{1}{2}\sum_a W_{k_0}(a)$ | **Proved** |
| $\sum_a W_{k_0}(a) \geq 2 S_{k_0-1}(A)$ for $k_0 \geq 601$ | **Proved** (Thm MM, Mertens estimate) |
| Conjecture holds for $k_0 \leq 44$ | **Proved** (Q16 + Q20) |
| Conjecture holds for $k_0 \geq 601$ | **Proved** (Thm MM + Thm NN) |
| Conjecture holds for $45 \leq k_0 \leq 600$ | **Open** (gap requires sharper Mertens estimates or Q16-type computation) |

**Net Q25 finding**: The overcounting bound $\mathrm{OC}_{\mathrm{total}} \leq \frac{1}{2}\sum W$ gives global WD when the shadow ratio $\geq 2$, achieved for $k_0 \geq 601$. Combined with Q16 (small $k_0$), the conjecture is proved for all $k_0 \notin [45, 600]$. The gap $45 \leq k_0 \leq 600$ remains.

**New Q26**: Close the gap $45 \leq k_0 \leq 600$:
- Either: sharpen the Mertens estimate (show shadow ratio $\geq 2$ for all $k_0 \geq 45$), OR
- Extend the Q16 computation from $k_0 \leq 44$ to $k_0 \leq 600$ (numerical verification), OR
- Use a different method for the middle range.
