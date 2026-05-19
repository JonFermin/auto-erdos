# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Setup

- **Claim**: see `proofs/primitive_set_erdos.json` field `claim_latex`. The
  conjecture is that for any primitive set $A \subset [x, \infty)$ the sum
  $\sum_{a \in A} 1/(a \log a)$ is bounded above by $1 + o(1)$ as $x \to \infty$.
- **Status**: open. Until a verifier-accepted witness is committed, no claim
  of resolution may appear in this file (`critic_openness` enforces this).
- **Given facts ledger**: see `proofs/primitive_set_erdos.json` field
  `given_facts`. The proof may cite F1 (Erdős-Zhang upper bound ≈ 1.399),
  F2 (Omega-stratum lower bound with UNSIGNED big-O — read carefully),
  F3 (exact asymptotic showing canonical extremal sum approaches 1 from
  BELOW). Citations to facts not in the ledger trigger `critic_ledger`.

## Guard rails (avoid these failure modes)

- **F2 sign confusion**: the big-O term in F2 is unsigned; it does NOT
  imply the sum exceeds 1.
- **F3 direction**: the leading correction in F3 is negative; the sum
  approaches 1 from *below*.
- **Resolution without witness**: no claim of resolution may appear here
  until `proof_prepare.py` has accepted a `<!-- WITNESS -->` block with
  `witness_valid == 1`. Unverified resolution assertions are caught
  automatically.

## Section 1: Setup (Q1)

### The Claim

Erdős's primitive-set conjecture asserts: for any primitive set
$A \subseteq [x, \infty)$ (where "primitive" means no element of $A$ divides
another distinct element of $A$), the Erdős function

$$f(A) = \sum_{a \in A} \frac{1}{a \log a}$$

satisfies $f(A) < 1 + o(1)$ as $x \to \infty$.

In other words, once we restrict to integers all at least as large as $x$,
the sum is bounded near 1, and this bound tightens as $x$ grows.

**Status**: open conjecture. No resolution may be claimed without a
verifier-accepted witness block (see below).

### Given Facts (with Sign Disambiguations)

**F1 (Erdős–Zhang upper bound, Zhang 1993)**:
For *any* primitive set $A \subseteq \mathbb{N}$ (no floor constraint),
$$f(A) = \sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign note*: This is an **upper** bound. It says the sum is *less than*
approximately 1.399, which is consistent with the conjecture (which
conjectures an even tighter upper bound of 1 + o(1) for the $x$-floored
version). F1 does NOT say the sum is close to 1.399 from below; it gives
a ceiling.

**F2 (Omega-stratum lower bound)**:
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ be the set of integers
with exactly $k$ prime factors (counted with multiplicity). Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$

*Sign note*: The $O(\cdot)$ term here is **unsigned** — it could be
positive or negative. The statement means the sum is at least
$1 - C k^{-1/2+o(1)}$ for some fixed constant $C > 0$, NOT that it
exceeds 1. Concluding $f(A_k) > 1$ from F2 alone is a sign error.

**F3 (Exact asymptotic for $A_k$)**:
For the same $A_k$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},$$
where $c \approx 0.0656 > 0$.

*Sign note*: The leading correction term is $-(c+o(1)) k^2/2^k$ with
$c > 0$, so the sum is **strictly less than 1** for every finite $k \geq 1$,
and approaches 1 **from below** as $k \to \infty$. F3 is compatible with
both F2 (once F2's unsigned big-O is read correctly) and with the conjecture
(the canonical extremal-looking primitive set $A_k$ does NOT violate it).

### Witness Contract

A disproof of the conjecture requires exhibiting a finite primitive set
$A \subseteq [x_{\text{floor}}, \infty)$ with $f(A) > 1.0$, verified
rigorously by `library.primitive_set_witness.verify_witness`. If such a
witness is found, it must be embedded as a `<!-- WITNESS ... WITNESS -->`
block in this file (see the template in the header). The verifier recomputes
$f(A)$ exactly (using Python's arbitrary-precision arithmetic via `math.log`)
and checks pairwise non-divisibility.

Parameters:
- `x_floor`: integer $\geq 2$; every element of `elements` must be $\geq x_{\text{floor}}$.
- `elements`: list of integers, pairwise non-divisible, each $\geq x_{\text{floor}}$.
- `claimed_sum_lower_bound`: float; the verifier recomputes independently.

The conjecture's $o(1)$ caveat means a finite-$x$ witness that just barely
exceeds 1.0 might be misleading — the true supremum of $f(A)$ over all
primitive $A \subseteq [x, \infty)$ might still tend to $\leq 1$ as
$x \to \infty$. The openness critic will flag any premature conclusion.

### Proof Strategy Overview

Two independent threads to pursue in parallel:

**Thread A (search for counterexample)**: Try to find a primitive
$A \subseteq [x_{\text{floor}}, \infty)$ with $f(A) > 1.0$. Start with
greedy construction at $x_{\text{floor}} \in \{100, 1000, 10000\}$. If
this fails (consistent with the conjecture being true), document why.

**Thread B (structural proof)**: Attempt to bound $f(A)$ for arbitrary
primitive $A$ via Omega-stratification. The key question is: given F3's
exact formula, can we control the cross-stratum interaction?

## Section 3: Counterexample Search (Q4)

Attempted to find a primitive set $A \subseteq [x_{\text{floor}}, \infty)$
with $f(A) > 1.0$ for $x_{\text{floor}} \in \{2, 100, 1000, 10000\}$ using
the rigorous verifier in `library.primitive_set_witness`.

### Constructions tried

| Construction | $x_{\text{floor}}$ | $\|A\|$ | $f(A)$ | $> 1$? |
|---|---|---|---|---|
| Primes $[2, 10^6)$ first 1000 | 2 | 1000 | 1.5253 | **Yes** |
| $\{2,3\}$ | 2 | 2 | 1.0248 | **Yes** |
| Band $[100, 200)$ | 100 | 100 | 0.1408 | No |
| Band $[100, 200)$ + outer primes | 100 | 5100 | 0.2337 | No |
| Greedy in $[100, 200001)$ | 100 | 9935 | 0.2992 | No |
| Band $[1000, 2000)$ | 1000 | 1000 | 0.0957 | No |
| Greedy in $[1000, 200001)$ | 1000 | 16466 | 0.1979 | No |
| Band $[10000, 20000)$ | 10000 | 10000 | 0.0726 | No |

### Interpretation

**$x_{\text{floor}} = 2$**: Several primitive sets (including the trivial
$\{2,3\}$) exceed 1.0. The verifier accepts these. Whether they constitute
meaningful counterexamples depends on the $o(1)$ tolerance at $x=2$, which
is not established by the given facts ledger. The conjecture says $f(A) < 1 + o(1)$
where $o(1) \to 0$ as $x \to \infty$; at $x=2$ the tolerance is an open
sub-question. We flag these as potential counterexamples and defer the
question of the $o(1)$ value at $x=2$ to open question Q6.

**$x_{\text{floor}} \in \{100, 1000, 10000\}$**: All constructions tried
give $f(A) \ll 1$. The best result is $\approx 0.30$ at $x=100$ via a greedy
algorithm. No witness with $f(A) > 1$ was found at any of these floors.

### Conclusion from Thread A

Thread A is **negative**: no counterexample found for large floors. The
numerical evidence is consistent with the conjecture being true. Proceed with
Thread B (structural proof via $\Omega$-stratification).

## Section 2: Numerical Evidence for F3 (Q2)

We compute truncated Omega-stratum sums $S_k(N) = \sum_{n \leq N, \Omega(n)=k} 1/(n \log n)$
for $N = 100{,}000$ and the first-200-elements version to build intuition.

### F3 asymptotic formula values

$$f(A_k) \approx 1 - 0.0656 \cdot k^2 / 2^k$$

| k | prediction | predicted correction |
|---|------------|----------------------|
| 2 | 0.9344 | $-0.0656$ |
| 3 | 0.9262 | $-0.0738$ |
| 4 | 0.9344 | $-0.0656$ |
| 5 | 0.9488 | $-0.0513$ |
| 6 | 0.9631 | $-0.0369$ |
| 10 | 0.9897 | $-0.0102$ |

*Note: k=1 is omitted because F3's $k=1$ prediction requires a normalization
not yet clarified (see below); the table above is for $k \geq 2$ where F3
clearly applies.*

All tabulated values are $< 1$. F3's formula $1 - (c+o(1))k^2/2^k$ with
$c > 0$ gives a negative correction for all finite $k \geq 2$. The formula
approaches 1 from below as $k \to \infty$. The table, not the formula,
is just numerical illustration.

### Truncated sums $S_k(N)$ for $N = 100{,}000$ (no floor)

| k | count$(n \leq N)$ | $S_k(100000)$ | $< 1$? |
|---|-------------------|---------------|--------|
| 1 | 9592 | 1.5498 | **No** |
| 2 | 23378 | 0.8288 | Yes |
| 3 | 25556 | 0.4522 | Yes |
| 4 | 18744 | 0.2249 | Yes |

**Observation**: For $k=1$ (primes from $n=2$), the truncated sum exceeds 1.
This is **not** a contradiction — the conjecture concerns primitive sets
$A \subseteq [x, \infty)$ as $x \to \infty$; it says nothing about
primitive sets starting from $n = 2$. For $k \geq 2$ the sum is already
comfortably below 1.

### Floor-constrained tail sums $S_k(N; x_0) = \sum_{n=x_0}^{N} 1/(n \log n) \cdot \mathbf{1}[\Omega(n)=k]$

For $x_0 = 100$ and $N = 100{,}000$:

| k | $S_k(100000; 100)$ |
|---|---------------------|
| 1 | 0.1282 |
| 2 | 0.2497 |
| 3 | 0.2325 |
| 4 | 0.1511 |

For $x_0 = 1000$:

| k | $S_k(100000; 1000)$ |
|---|----------------------|
| 1 | 0.0575 |
| 2 | 0.1288 |
| 3 | 0.1311 |
| 4 | 0.0908 |

**Key observation**: All floor-constrained single-stratum sums are well
below 1 for both floors. As $x_0 \to \infty$, each single-stratum truncated
sum $S_k(N; x_0)$ tends to 0 with $N$ fixed and $x_0$ growing. **This does
not imply the conjecture's bound is 0** — the conjecture is about the
supremum over ALL primitive subsets of $[x, \infty)$, not just single-stratum
sets. The relationship between single-stratum tail sums and the sup over all
primitive sets is an open sub-claim (see Thread B).

**Puzzle**: The numerical data suggests the sums are much smaller than 1 for
large floors, yet F3 claims the asymptotic is $1 - \epsilon$. This discrepancy
suggests F3 is NOT about $A_k \cap [x, \infty)$ with $x$ fixed and
$N \to \infty$; instead it likely refers to the FULL $A_k$ (sum over all $n$
with $\Omega(n) = k$) or a specific normalization (see open question Q6).

**For $k = 1$**: The truncated sum $S_1(N)$ (primes up to $N$) grows slowly
with $N$ and exceeds 1 for $N \geq 5$ (second prime = 3 already gives sum
$> 1$ with $p=2$). So F3 cannot be about the raw truncated sum for $k=1$.
F3's applicability at $k=1$ requires clarification of the normalization;
we treat the $k=1$ row in the table as indicative only.

**Provisional conclusion**: F3's formula $1 - (c+o(1))k^2/2^k$ is an
asymptotic result valid as $k \to \infty$ whose exact meaning requires
clarification (see open question Q6). For $k \geq 2$: both the truncated
sum from $n=2$ and the F3 formula give values $< 1$. For $k=1$: the
truncated sum $S_1(N)$ grows slowly with $N$ (exceeding 1 for small $N$),
so F3's $k=1$ claim applies to a normalization not yet identified. We treat
$k \geq 2$ as the reliable range of F3 for this proof attempt.
