# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Section 1: Setup (Q1)

### The Claim

**Erdős's Primitive-Set Conjecture (tightened form):** For any $x \geq 2$,
if $A \subset [x, \infty)$ is a *primitive set* of positive integers (no
distinct element of $A$ divides another), then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$

where the $o(1)$ term tends to $0$ as $x \to \infty$.

**Status:** Open. No proof or disproof is known. This file must not assert
resolution without a verifier-accepted `<!-- WITNESS -->` block.

### Given Facts (with sign disambiguations)

**F1 (Erdős–Zhang upper bound, citation: Erdős 1935; Zhang 1993):**
For any primitive set $A \subseteq \mathbb{N}$,

$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1)
\approx 1.399 + o(1).$$

*Sign disambiguation:* This is an UPPER bound (sum strictly less than
~1.399). It is consistent with the conjecture (which posits an even
tighter bound of 1). Do NOT misread it as a lower bound.

**F2 (Omega-stratum lower bound, UNSIGNED big-O):**
If $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly
$k$ prime factors counted with multiplicity), then

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign disambiguation:* The big-O term $O(k^{-1/2+o(1)})$ is **UNSIGNED** —
it could be positive or negative; it is only bounded in absolute value by
$C k^{-1/2+o(1)}$ for some constant $C$. This fact does NOT imply the sum
exceeds 1. Concluding "sum $> 1$" from F2 alone is a sign error. (This is
the canonical failure mode of the ChatGPT writeup that motivated this
problem: it read the unsigned-O as positive and immediately claimed a
contradiction.)

**F3 (exact asymptotic, approaches 1 from BELOW):**
For $A_k$ as above,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$

*Sign disambiguation:* The correction $-(c+o(1))k^2/2^k$ is **negative**
(since $c > 0$). So $\sum_{a \in A_k} 1/(a \log a) < 1$ for all $k \geq 1$,
approaching 1 from BELOW as $k \to \infty$. Even the "extremal-looking"
set $A_k$ satisfies the conjecture.

*Consistency note:* F3 is consistent with F2 once the unsigned-O in F2 is
read correctly. F3 pins down the sign of the correction (it is negative),
showing the O-term in F2 is in fact negative for the full set $A_k$.

### Witness Contract (sole path to a disproof claim)

A claim of disproof requires a `<!-- WITNESS -->` block in this file whose
JSON payload passes `library.primitive_set_witness.verify_witness`. The
verifier enforces:

1. Every element is an integer $\geq x_{\mathrm{floor}} \geq 2$.
2. Elements are pairwise non-divisible (no element divides another).
3. A *rigorous* Decimal lower bound on $\sum_{a \in A} 1/(a \log a)$
   (using 4-ULP-bumped log values at 80-digit precision) strictly exceeds
   the **witness threshold of 1.0**.

If and only if `verify_witness` returns `is_valid=True`, the gatekeeper
sets `witness_valid = 1` and the status `keep_disproof`.

### Anti-traps

- **F2 sign confusion:** Never conclude sum $> 1$ from F2 alone.
- **F3 upside-down:** F3's sum approaches 1 from BELOW — evidence for,
  not against, the conjecture.
- **Open claim without witness:** Until `witness_valid == 1`, no phrase
  asserting disproof may appear here.

---

## Section 2: Numerical Evidence (Q2)

*(Planned — verify F3 for k = 1, 2, 3, 4 numerically.)*

---

## Section 3: Primes-Sum Distinction (Q3)

*(Planned — document the primes-from-2 finite sum ~1.6366 and why this is
consistent with F1.)*

---

## Section 4: Witness Search (Q4)

*(Planned — record any witness found or document why none was found for
x_floor = 100, 1000, 10000.)*

---

## Section 5: Proof Structure Outline (Q5)

*(Planned — lemma decomposition, stratum argument.)*

---

## Witness format (the only path to a counterexample claim)

A claim of disproof MUST be backed by a finite primitive set whose sum is
rigorously verified to exceed `witness_threshold` by
`library.primitive_set_witness.verify_witness`. To commit a witness,
embed exactly one block of the form:

```
<!-- WITNESS
{
  "x_floor": 100,
  "elements": [101, 103, 107, 109, ...],
  "claimed_sum_lower_bound": 1.005
}
WITNESS -->
```

at the bottom of this file. `proof_prepare.py` parses the JSON, runs the
deterministic verifier, and sets `witness_valid` accordingly. No witness
block ⇒ `witness_valid = 0` ⇒ no counterexample claim is possible.
