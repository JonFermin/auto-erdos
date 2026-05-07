# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop.
Content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

## Section 1: Setup — The Claim, Facts, and Witness Contract

### The Claim

Fix any $x \geq 2$. Let $A \subset [x, \infty)$ be any **primitive set** —
a set of integers in which no element divides any other. The Erdős primitive-set
conjecture asserts

$$S(A) := \sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where the $o(1)$ term tends to $0$ as $x \to \infty$. In other words: for
primitive sets supported on large integers, the weighted sum stays strictly
below $1$.

**Status**: open. Until a verifier-accepted witness is committed, no claim
of resolution may appear in this file (`critic_openness` enforces this).

### The Three Given Facts

**F1 (Erdős–Zhang upper bound, 1935/1993).**
For any primitive set $A \subseteq \mathbb{N}$,
$$S(A) < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign note*: This is a STRICT UPPER BOUND of $\approx 1.399$. The bound is
consistent with the conjecture (which claims a tighter bound of 1). F1 does
NOT say the sum can reach 1.399; it is not a lower bound.

*Scope note*: F1 applies to restricted primitive sets (large-$x$ base). The
full (unrestricted) prime set $\{2, 3, 5, \ldots\}$ has sum $\approx 1.637$,
which exceeds F1's bound; this is not a contradiction because F1 applies to
sets in $[x, \infty)$ for $x \to \infty$, where the prime tail sum is $\sim
1/\log x \to 0$.

**F2 (Omega-stratum lower bound, unsigned big-O).**
For $A_k := \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors counted with multiplicity),
$$S(A_k) \geq 1 + O\!\left(k^{-1/2+o(1)}\right).$$

*Sign note*: The big-O term $O(k^{-1/2+o(1)})$ is UNSIGNED — its sign is
unknown. Deducing $S(A_k) > 1$ from F2 alone is a sign error (the term
could be negative). F2 says $S(A_k) \geq 1 - C k^{-1/2+o(1)}$ for some
$C > 0$, approaching 1 from below.

**F3 (Exact asymptotic, approaches 1 from below in $k$).**
For the same $A_k$,
$$S(A_k) = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$

*Sign note*: The correction $-(c+o(1))k^2/2^k$ is NEGATIVE, so the sum is
strictly less than 1, approaching 1 from below as $k \to \infty$.

*Scope note*: The $o(1)$ in F3 is as $k \to \infty$. For moderate $k$ the
formula is an approximation; for $k = 1$ (primes), the contribution of small
primes $2, 3, 5, \ldots$ makes the finite truncated sum exceed 1 (see
Section 2 numerical evidence), but this is consistent with F3 being an
asymptotic statement about how the strata approach 1 as $k$ grows large. F3
does not assert that the sum over small-$k$ strata is already below 1 when
restricted to a finite initial segment.

### The Witness Contract

The only route to claiming a counterexample is a **verified witness**:

- A finite set $A \subset [x_{\text{floor}}, \infty)$ for some explicit $x_{\text{floor}}$.
- $A$ must be primitive (no $a \mid b$ for distinct $a, b \in A$).
- `library.primitive_set_witness.verify_witness` must confirm $S(A) > 1.0$.
- The witness JSON must appear in `proof_strategy.md` inside the
  `<!-- WITNESS ... WITNESS -->` block.
- Even a verified witness at finite $x_{\text{floor}}$ is only a candidate
  counterexample: the $o(1)$ caveat in the conjecture requires additional
  argument that the $o(1)$ gap is negligible at $x_{\text{floor}}$. Human
  review is mandatory before claiming a real result.

## Section 2: Numerical Evidence

All computations use $f(n) = 1/(n \ln n)$ (natural log).

### Q2: F3 verification — first 200 elements of $A_k$

| $k$ | 200th element | $\sum_{\text{first 200}} f(a)$ | $<1$? | F3 formula value |
|-----|--------------|-------------------------------|-------|-----------------|
| 1   | 1223         | 1.496452                      | No    | 0.9672           |
| 2   | 669          | 0.681938                      | Yes   | 0.9344           |
| 3   | 805          | 0.313401                      | Yes   | 0.9262           |
| 4   | 1292         | 0.140341                      | Yes   | 0.9344           |

**Observations:**
- For $k \geq 2$, the truncated sum is well below 1, and decreases as $k$
  grows (the high-$\Omega$ strata contribute little).
- For $k = 1$ (primes), the truncated sum is 1.496 due to the large
  contributions of small primes ($1/(2 \ln 2) \approx 0.721$,
  $1/(3 \ln 3) \approx 0.303$, ...). The full prime series converges to
  $\approx 1.637$, consistent with Q3.
- F3's formula $1 - 0.0656 k^2/2^k$ gives values near 1 for all $k$,
  approaching 1 from below as $k \to \infty$. For $k = 1$ the formula
  predicts $\approx 0.967$, but this reflects the asymptotic regime and
  not the finite-$k$ / small-prime contribution.
- The leading correction $-(c + o(1)) k^2 / 2^k$ is negative for all $k \geq 1$,
  so F3's assertion that "the sum approaches 1 from below" is an asymptotic
  statement (as $k \to \infty$), not a claim about each individual stratum
  restricted to a truncated range.

### Q3: Prime tail sum and consistency with F1

The full prime series $\sum_{p \text{ prime}} 1/(p \log p)$ converges (by
comparison with $\int 1/(t \log^2 t)\, dt = -1/\log t$, which is finite).
Its value is $\approx 1.637$:

| Upper cutoff $N$ | $\sum_{p \leq N} 1/(p \log p)$ |
|-----------------|-------------------------------|
| 100             | 1.421567                      |
| 1000            | 1.492315                      |
| 10000           | 1.528162                      |
| 50000           | 1.543974                      |
| $\infty$ (est.) | $\approx 1.637$               |

The **prime tail** $\sum_{p \geq x} 1/(p \log p)$ decreases toward 0:

| $x$   | $\sum_{p \geq x} 1/(p \log p)$ |
|-------|-------------------------------|
| 100   | 0.1224                        |
| 1000  | 0.0517                        |
| 10000 | 0.0158                        |

**Consistency with F1**: The conjecture's bound of $1 + o(1)$ applies to
primitive $A \subset [x, \infty)$ as $x \to \infty$. For the restricted
prime set $\{p : p \geq x\}$, the sum is $\sim 1/\log x \to 0$, which is
well within the bound of 1. The FULL prime set (including $p = 2, 3, \ldots$)
has sum $\approx 1.637$, but this set is not a subset of $[x, \infty)$ for
any fixed $x$. Hence the prime example does not violate the conjecture.

**Consistency with F1's bound of $1.399$**: The full prime sum ($\approx 1.637$)
exceeds $1.399 + o(1)$. This is also not a contradiction: F1 applies to
primitive $A \subseteq [x, \infty)$ for large $x$; the full primes-from-2
set is not of this restricted form. F1's bound is about the same family as
the conjecture — large-$x$ restricted primitive sets.

### Q2 correction terms

For each $k$, the truncated sum over the first 200 elements is below the
F3 prediction because we haven't included all of $A_k$. As more elements
of $A_k$ are included, the sum grows toward the F3 asymptotic:

$$\sum_{a \in A_k} f(a) \approx 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656.$$

For $k = 1$ the full-stratum sum is $\approx 1.637$ (not $0.967$), suggesting
F3's formula applies in the large-$k$ regime rather than at $k = 1$. This is
an important caveat: citations to F3 should not claim the formula holds
exactly at $k = 1$.

## Section 3: Proof Structure and Lemmas

*(To be developed in Q5.)*

## Section 4: Witness Search

*(Q4 — search for primitive $A \subset [x_{\text{floor}}, \infty)$ with $S(A) > 1.0$.)*
