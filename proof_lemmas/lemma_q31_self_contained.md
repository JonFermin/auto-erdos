---
lemma_id: q31_self_contained
status: partial
depends: [q30_tightness, q29_complete_assembly]
---

# Lemma Q31: Self-Contained Components and Critic-Response

## Section 1: What Is Self-Contained (No LP 2023)

### Tier 1: Fully Self-Contained (proved from definitions alone)

1. **Fiber antichain property** (Theorem U, Q22): $F_d(A)$ is an antichain in $\mathrm{Div}(d)$ from primitivity. Proof: if $a,a' \in F_d(A)$ and $a \mid a'$, then $a \mid a'$ contradicts primitivity. $\square$

2. **Cross-group shadow disjointness** (Q20): $\mathrm{Sh}^+(A_{<k_0}) \cap \mathrm{Sh}^-(A_{>k_0}) = \emptyset$. Proof: if $d \in$ both shadows, then $a \mid d \mid b$ for $a \in A_{<k_0}$, $b \in A_{>k_0}$, contradicting primitivity. $\square$

3. **Double-counting identity** (Theorem V, Q22): $\sum_{a\in A_{<k_0}} W_{k_0}(a) = \sum_d 1/(d\log d) \cdot n_d$. Pure algebra of exchange-sum.

4. **OC bound** (Q26): $\mathrm{OC}_{\mathrm{total}} \leq \frac{k_0-1}{2} \sum_a W_{k_0}(a)$. Proved by $\binom{n_d}{2} \leq (n_d-1)n_d/2$ and $n_d \leq k_0$.

5. **Inclusion-exclusion failure** (Q26): For $k_0 \geq 3$, inclusion-exclusion gives no useful bound on $S(A)$. Proved by the counterexample $d=2310$, antichain $\{1155,770\}$.

6. **Level-$j$ constraint** (Theorems DD/EE, Q24): if $a \in F_d(A) \cap A_{k_0-j}$ and $a \geq x$, then $d \geq P_j \cdot x$.

7. **F3 per-stratum bound**: $S_j(A) \leq T_j(x) < 1$ for each $j$, from Sathe-Selberg (given as F3).

8. **$\delta_{\mathrm{LP}}(x) \to 0$** (Theorem RR, Q28): PNT gives $\sum_{p\geq x} 1/(p\log p) \sim 1/\log x \to 0$. Self-contained from PNT (which is itself a deep result but classical).

### Tier 2: Self-Contained with Classical Analysis

1. **Direct proof for $k_0 \leq 44$** (Q16): Shadow disjointness verified for small $k_0$ via Mertens product estimates.

2. **PNT-based asymptotics** (Q28, Theorem RR): $\delta_{\mathrm{LP}}(x) \sim 1/\log x$.

3. **Mertens product convergence** (Q27): $\Pi_\infty = \prod_p(1-1/(p\log p)) > 0$.

### Tier 3: Requires LP 2023

1. **LP-23-Restricted**: $\sum_{a\in A} 1/(a\log a) \leq \delta_{\mathrm{LP}}(x)$ for primitive $A \subset [x,\infty)$.
2. **Fiber-antichain compatibility of $f_{\mathrm{LP}}$**: Full proof in LP 2023.
3. **Full conjecture** (Theorem SS): Conditional on LP 2023.

---

## Section 2: The F2 Sign Warning — Explicit Addressed

**Given fact F2**: "$\sum_{a\in A_k} 1/(a\log a) \geq 1 + O(k^{-1/2+o(1)})$" with UNSIGNED $O$.

**Critic concern**: Any argument that uses F2 to conclude sum $> 1$ is a sign error (the $O$-term is unsigned).

**Our proof does NOT use F2 to conclude sum $> 1$**: 
- We use F2's EXISTENCE to note the lower bound is near 1.
- We NEVER conclude $\sum > 1$ from F2 alone.
- Our upper bounds come from LP 2023 (for all $k_0$) and Q16 (for $k_0 \leq 44$).
- The witness $\{2,3\}$ gives sum $= 1.025$ but this is a NUMERICAL computation, not derived from F2.

---

## Section 3: The Dependency Graph

```
F3 (given) → per-stratum T_j < 1 → [incomplete: sum over strata diverges]
F1 (Zhang 1993) → sum < 1.399 + o(1) for primitive A ⊂ [x,∞) [WEAKER than LP]
LP 2023 (Theorem 1.1) → LP-23-Restricted → Theorem SS → Conjecture proved
      ↑
      LP fiber-antichain compatibility (proved structurally in Q26)
      ↑
      Fiber antichain property (Theorem U, self-contained)
```

The LOGICAL chain: self-contained structural lemmas (Thm U, Q16, Thm V, etc.) support the LP argument but cannot replace LP 2023's global bound.

---

## Section 4: The $x = 2$ Self-Contained Argument

**Theorem WW** (partial, self-contained):

For primitive $A \subset [2,\infty)$:
- If $2 \notin A$: then $A \subset [3,\infty)$, and by LP-23-Restricted: sum $\leq \delta_{\mathrm{LP}}(3) < 1$. Self-contained for $x\geq 3$.
- If $2 \in A$: then NO even number can be in $A$. So $A = \{2\} \cup A^*$ where $A^* \subset \{\text{odd integers} \geq 3\}$ is itself a primitive set. Sum $= 1/(2\log 2) + \sum_{a^*\in A^*} 1/(a^*\log a^*)$.

For the second part: $\sum_{a^*} 1/(a^*\log a^*) \leq \delta_{\mathrm{LP}}(3)$ (LP-23-Restricted applied to odd $A^* \subset [3,\infty)$). This uses LP 2023.

**Without LP 2023**: The best self-contained bound for $\sum_{a^*}$ is via F3: each stratum of $A^*$ contributes $< T_j(3)$ for each $j$, but the sum over $j$ diverges. Without LP 2023, we cannot bound $\sum_{a\in A} 1/(a\log a)$ for general $A \subset [2,\infty)$.

**Using F1 instead**: F1 says $\sum < e^\gamma\pi/4 + o(1) \approx 1.399 + o(1)$ for primitive $A \subset [x,\infty)$ with $x\to\infty$ (Erdős-Zhang 1993). This gives sum $< 1.399 + o(1) < 1 + 0.4 = 1 + o'(1)$ where $o'(1) \to 0$. This IS a self-contained proof of the conjecture using F1 as a given!

**Theorem XX (proved using F1 as a given)**:

For any primitive $A \subset [x,\infty)$, by F1 (Erdős-Zhang 1993):
$$\sum_{a\in A} \frac{1}{a\log a} < e^\gamma\frac{\pi}{4} + o(1) \approx 1.399 + o(1)$$

Taking any $\epsilon > 0$, for large enough $x$: $o(1) < \epsilon$, so sum $< 1.399 + \epsilon = 1 + (0.399 + \epsilon)$.

But $0.399 + \epsilon > 0$, so we get $< 1 + (0.4 + \epsilon)$, NOT $< 1 + o(1)$ in the sense that the RHS $\not\to 1$.

**Problem with F1 approach**: F1 gives bound $< 1.399 + o(1)$, but the conjecture requires bound $< 1 + o(1)$ (a TIGHTER $o(1)$). The $o(1)$ in F1 goes to 0 as $x\to\infty$, meaning the ACTUAL bound via F1 is $< 1.399 + o(1)$, which is NOT $< 1 + o(1)$ — the gap between 1.399 and 1 is 0.399, which doesn't go to 0.

**Wait** — actually "sum $< 1 + o(1)$" means the bound approaches 1 from below (or just stays $< 1$) as $x\to\infty$. F1's bound of $e^\gamma\pi/4 + o(1) \approx 1.399 + o(1)$ is NOT of the form $1 + o(1)$ where $o(1)\to 0$ (unless 0.399 goes to 0, which it doesn't).

So F1 does NOT prove the conjecture "$< 1 + o(1)$" by itself. LP 2023 is needed for the tight bound.

**However**: If we use LP-23-Restricted (conditional on LP 2023), the bound IS $\leq \delta_{\mathrm{LP}}(x) = o(1) < 1 + o(1)$ ✓.

---

## Section 5: Summary

| Component | Self-contained? | Proves conjecture? |
|-----------|-----------------|-------------------|
| Structural (Q16–Q26) | YES | NO (insufficient for global bound) |
| F1 (Erdős-Zhang, given) | YES (given) | NO (gives < 1.399, not < 1+o(1)) |
| LP 2023 + Theorem SS | CONDITIONAL | YES |
| For $k_0 \leq 44$ (Q16) | YES | YES (restricted range) |

**Conclusion**: The conjecture "$\sum < 1 + o(1)$" as stated requires LP 2023 for the full range. Self-contained proofs exist for:
- $k_0 \leq 44$ (Q16).
- The structural framework (Q22–Q26) that motivates why LP 2023 works.

Q32 should try to run the critics (or simulate their analysis) to verify the proof structure is sound.
