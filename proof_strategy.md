# Proof attempt — `primitive_set_erdos`

Round log: Q1 (setup), Q2 (numerical evidence for F3), Q4 (witness search).

---

# Section 1: Setup (Q1)

## 1.1 The Conjecture

**Claim.** For any $x \geq 2$, if $A \subset [x, \infty)$ is a primitive set of integers
(no distinct element divides another), then

$$f(A) \;:=\; \sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where the $o(1)$ term tends to $0$ as $x \to \infty$.

**Status**: open. This remains an unproved conjecture.

## 1.2 Given Facts (Ledger)

### F1 — Erdős–Zhang upper bound

**Ledger statement:** For any primitive set $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

**Sign:** This is a strict upper bound — the sum lies *strictly less than* $e^\gamma \pi/4 + o(1)$.
The constant $e^\gamma \pi/4 \approx 1.399$ does not furnish a lower bound of any kind.

### F2 — Omega-stratum lower bound (unsigned correction)

**Ledger statement:** If $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$, then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$

**Sign:** The big-$O$ term is **unsigned** — it may be positive or negative. Concluding
$f(A_k) > 1$ from F2 alone would be a sign error (the correction might be negative).

### F3 — Exact asymptotic for Omega-strata (approaches 1 from below)

**Ledger statement:** For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k}, \quad c \approx 0.0656,$$
as $k \to \infty$.

**Sign:** The correction $-(c+o(1))k^2/2^k$ is **negative** ($c > 0$), so the sum is strictly less
than 1 for large $k$ and approaches 1 from *below*.

## 1.3 Witness Contract

A candidate counterexample is a finite primitive set $A \subset [x_{\text{floor}}, \infty)$
whose rigorously verified sum $f(A)$ strictly exceeds $1.0$ (the `witness_threshold`).

Verified by `library.primitive_set_witness.verify_witness` using Decimal arithmetic at
80-digit precision:

| Field | Constraint |
|---|---|
| `x_floor` | `int >= 2`; every element of `elements` must be $\geq x_{\text{floor}}$ |
| `elements` | `list[int]`; pairwise non-divisible; each element $\geq x_{\text{floor}}$ |
| `claimed_sum_lower_bound` | `float`; the rigorous verifier recomputes independently |

---

# Section 2: Numerical Evidence for F3 (Q2)

## 2.1 F3 Asymptotic Values

The formula $1 - 0.0656 \cdot k^2 / 2^k$ predicts the following limiting values:

| $k$ | $1 - 0.0656 \cdot k^2/2^k$ |
|---|---|
| 1 | $1 - 0.0656 \cdot 1/2 \approx 0.9672$ |
| 2 | $1 - 0.0656 \cdot 4/4 \approx 0.9344$ |
| 3 | $1 - 0.0656 \cdot 9/8 \approx 0.9262$ |
| 4 | $1 - 0.0656 \cdot 16/16 \approx 0.9344$ |

## 2.2 Truncated Sums over First 200 Elements of $A_k$

We computed truncated sums over the first 200 elements of $A_k$ (ordered by size):

| $k$ | Truncated sum | Largest element |
|---|---|---|
| 1 | 1.4965 (first 200 primes) | $p_{200} = 1223$ |
| 2 | 0.682 | 669 |
| 3 | 0.313 | 805 |
| 4 | 0.140 | 1292 |

**Observation for $k=1$:** The first 200 primes sum to $1.4965 > 1$. This is consistent with
F3: the formula $1 - ck^2/2^k$ is an asymptotic as $k \to \infty$; for $k=1$ the $o(1)$
correction in $c + o(1)$ is large (the asymptotic is not yet in force). For $k \geq 2$
the truncated sums are well below 1.

**Observation for $k \geq 2$:** These are partial sums; full infinite sums over $A_k$ would be
closer to the F3 asymptotic values, but still below 1 per F3's sign.

---

# Section 3: Witness Search — Negative Result (Q4)

We searched for a finite primitive $A \subset [x_{\text{floor}}, \infty)$ with rigorously
verified $f(A) > 1.0$, using `library.primitive_set_witness.verify_witness`.

| $x_{\text{floor}}$ | Witness found? | Notes |
|---|---|---|
| 100 | No | Prime tail sum over $[100, 200000]$ is numerically $\approx 0.133$ |
| 1000 | No | Prime tail sum over $[1000, 200000]$ is numerically $\approx 0.062$ |
| 10000 | No | Prime tail sum over $[10000, 200000]$ is numerically $\approx 0.027$ |

The prime tail sums (computed by sieve to $N = 200{,}000$) are all well below 1.0, so no
candidate based on primes alone can reach the witness threshold at these $x_{\text{floor}}$
values. The witness search also tried small non-prime primitive sets at each threshold and
found no witness.

---

# Section 4: Open Questions

**This remains open.** The following are unresolved after this exploration:

1. **Proof of the bound $1 + o(1)$**: The gap between F1 ($e^\gamma\pi/4 \approx 1.399$) and
   the conjectured tight bound ($1$) is not resolved. A proof would require either an
   omega-stratification argument or a new analytic technique.

2. **Stratification lemma** (Q5): A stratification approach would bound
   $\sum_{a \in A,\, \Omega(a)=k} 1/(a \log a)$ for each stratum and sum over $k$.
   F3 gives the right asymptotic for the full strata $A_k$, but bounding contributions
   from arbitrary primitive sets (not full strata) requires an additional argument.

3. **Witness at large $x_{\text{floor}}$**: No witness found empirically at
   $x_{\text{floor}} \in \{100, 1000, 10000\}$. The conjecture appears to hold in this range.
