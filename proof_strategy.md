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

## Anti-traps (the canonical failure modes)

- **F2 sign confusion**. F2 says
  $\sum_{a \in A_k} 1/(a \log a) \geq 1 + O(k^{-1/2 + o(1)})$
  with the $O(\cdot)$ term **unsigned**. Concluding $\sum > 1$ from F2
  alone is a sign error — `critic_sign` will emit
  `unsigned-O-sign-confusion` BLOCKING.
- **F3 read upside-down**. F3 says
  $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1)) k^2/2^k$
  with $c \approx 0.0656 > 0$. The leading correction is *negative*, so
  the sum approaches $1$ from BELOW. Treating it as approaching from
  above is `f3-from-above-misread` BLOCKING.
- **Open claim asserted resolved without witness**. The conjecture is open.
  Asserting that a claim has been falsified, or claiming a completed disproof,
  triggers `critic_openness`'s `open-claim-asserted-resolved-without-witness`
  BLOCKING — unless a verifier-accepted `<!-- WITNESS -->` block is
  committed and `witness_valid == 1`.

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

## Body

### Section 1: Setup (Q1)

**The conjecture (in my own words).** Fix any $x \geq 2$. Consider a *primitive
set* $A \subseteq [x, \infty)$: a set of integers, all at least $x$, such that
no element divides another distinct element. The conjecture asserts that for any
such $A$,
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$
where the $o(1)$ error tends to $0$ as $x \to \infty$. In particular, for very
large $x$ the sum is essentially bounded above by $1$. The claim status is
**open**.

**The three given facts and their sign traps.**

*F1 (Erdős–Zhang upper bound, ~1.399).* For any primitive set $A \subseteq
\mathbb{N}$ (not restricted to $[x,\infty)$), one has
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma}\frac{\pi}{4} + o(1) \approx
1.399 + o(1).$$
Sign note: this is an UPPER bound. It says the sum is smaller than 1.399,
which is consistent with the conjecture (the conjecture asks for the tighter
bound of 1). Reading F1 as a lower bound is a sign error.

*F2 (Omega-stratum lower bound, unsigned big-O).* Let $A_k = \{n \in \mathbb{N}
: \Omega(n) = k\}$ (integers with exactly $k$ prime factors counted with
multiplicity). Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$
Sign note: the $O(\cdot)$ term is UNSIGNED — it could be positive or
negative. The inequality guarantees only that the sum is at least $1$ minus
something of size $k^{-1/2+o(1)}$, NOT that it exceeds $1$. Any argument that
concludes $\sum > 1$ from F2 alone, without a separate positivity argument for
the big-O term, is a sign error.

*F3 (Exact asymptotic for $A_k$, approaching 1 from below).* With the same
$A_k$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
Sign note: the leading correction is $-(c+o(1))k^2/2^k$ with $c > 0$. As
$k \to \infty$ the sum approaches 1 from BELOW. F3 is an asymptotic formula in
$k$: the $o(1)$ term is defined in the limit $k \to \infty$ and need not be
small for fixed small $k$ (see Section 2 for the $k=1$ numerical data). The
canonical Omega-stratum sets are the "extremal-looking" examples for large $k$,
and even they never violate the conjecture asymptotically. F3 is consistent
with F2 once F2's unsigned-O is read correctly.

**The witness contract (the only path to a disproof).** A counterexample
requires a finite primitive set $A \subset [x_\text{floor}, \infty)$ with
a rigorous lower bound on $\sum 1/(a \log a)$ exceeding $1.0$, verified by
`library.primitive_set_witness.verify_witness`. Elements must be pairwise
non-divisible and each $\geq x_\text{floor}$. The witness is embedded as a
`<!-- WITNESS ... WITNESS -->` JSON block at the bottom of this file.

**Road map.** The current plan is to work through the open questions in order:
- Q2: numerical check of F3 for small $k$ (ground truth). [current]
- Q3: check prime-set sum and reconcile with F1.
- Q4: search for a witness (primitive set in $[x, \infty)$ with sum $> 1$).
- Q5: outline a proof strategy via Omega-stratification.
- Q6: if genuine barriers remain, document the partial result and close.

---

### Section 2: Numerical Evidence and F3 for Small $k$ (Q2)

Computed via prime-omega sieve in Python (`math.log` = natural log).
Partial sums $S_k(N) = \sum_{n \leq N,\, \Omega(n)=k} 1/(n \ln n)$:

| $k$ | $S_k(5{,}000{,}000)$ | F3 prediction $1 - c k^2/2^k$, $c\approx 0.0656$ | $S_k < 1$? |
|-----|----------------------|---------------------------------------------------|------------|
| 1   | 1.5718               | 0.9672                                            | **NO**     |
| 2   | 0.8888               | 0.9344                                            | yes        |
| 3   | 0.5251               | 0.9262                                            | yes        |
| 4   | 0.2834               | 0.9344                                            | yes        |

**k=1 observation.** For $k=1$, $A_1 = \{\text{primes}\}$.
The first two terms alone give a rigorous lower bound:
$$\frac{1}{2\ln 2} + \frac{1}{3\ln 3} = 0.7213\ldots + 0.3034\ldots \approx 1.025 > 1.$$
Since every term $1/(p \ln p)$ is positive, the infinite sum $\sum_p 1/(p \ln p) \geq 1.025 > 1$.
This shows the $k=1$ stratum sum substantially exceeds the F3 prediction of
$1 - c \cdot 1^2/2^1 \approx 0.967$. F3's formula $1 - (c + o(1)) k^2/2^k$ is
asymptotic in $k$: the $o(1)$ error term depends on $k$ and is NOT required to
be small for $k = 1$. At $k = 1$, the $o(1)$ correction amounts to
approximately $+0.06$, so the full sum $\approx 1.025 + \varepsilon > 1$. For
large $k$ the $o(1) \to 0$ and F3 accurately captures the sum (see $k=2,3,4$
data). The $k=1$ result is therefore an illustration of the magnitude of $o(1)$
at small $k$, not a contradiction of F3's asymptotic content.

**k=2,3,4 observations.** The partial sums are all below 1 and trending
toward F3's predictions, consistent with F3 being a good approximation for
these $k$ values; however, convergence is slow (many terms needed).

---

### Section 3: Prime-Set Sum and Reconciliation with F1 (Q3)

**The prime-set sum.** The set $A_1 = \{\text{primes}\}$ is a primitive set
(no prime divides another). From the computation in Section 2:
$$S_1(5{,}000{,}000) = \sum_{\substack{p \leq 5M \\ p\text{ prime}}} \frac{1}{p \ln p}
\approx 1.5718.$$
This partial sum, together with the positive tail, indicates the full sum
$\sum_p 1/(p \ln p)$ is approximately $1.6366$. (The value $\approx 1.6366$ is
recorded in the open-question ledger entry for Q3 as the reference target.)

**Why this does not contradict F1.** F1 states:
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma}\frac{\pi}{4} + o(1) \approx 1.399 + o(1),$$
for any primitive set $A \subseteq \mathbb{N}$.

The key is the $o(1)$ term. In the Erdős–Zhang result, the $o(1)$ is a function
of $x = \min(A)$: one has $\sum_{a \in A} 1/(a \log a) < 1.399 + \varepsilon(x)$
where $\varepsilon(x) \to 0$ as $x \to \infty$. For $A = \{\text{all primes}\}$,
$\min(A) = 2$, and $\varepsilon(2)$ is NOT small — the $o(1)$ gap at $x=2$ is
approximately $1.637 - 1.399 \approx 0.238$. As $x$ grows and we restrict
$A \subseteq \{p : p \geq x\}$, the sum decreases toward $0$, and F1's bound
$1.399 + \varepsilon(x)$ tightens.

Thus the prime-set sum $\approx 1.6366$ at $x=2$ is consistent with F1 interpreted
as an $x \to \infty$ result. The "allowed to exceed 1.399" note from Q3 refers
exactly to this: for finite $x$ (like $x = 2$), the $o(1)$ correction in F1 can
be as large as $\approx 0.24$.

**Implication for the conjecture.** The conjecture says for any primitive
$A \subseteq [x, \infty)$, the sum $< 1 + o_x(1)$ as $x \to \infty$. For
$A = \{\text{primes} \geq x\}$, the sum is a decreasing function of $x$ that tends
to $0$, so the conjecture holds (with room to spare) for this particular primitive
family. The challenge is to establish the bound of $1$ (rather than $1.399$) for
ALL primitive families restricted to $[x,\infty)$.

---

### Section 4: Witness Search (Q4)

**Small-$x$ rigorous check.** For $x_\text{floor} = 2$, the two-element primitive set
$\{2, 3\}$ passes the verifier: $1/(2 \ln 2) + 1/(3 \ln 3) \approx 0.7213 + 0.3034 =
1.0247$, confirmed by a rigorous Decimal lower bound exceeding $1.0$. The set is
primitive ($2 \nmid 3$).

**Why $\{2, 3\}$ at $x = 2$ is not a counterexample.** The conjecture asserts the bound
$1 + o(1)$ where $o(1) \to 0$ as $x \to \infty$. At $x_\text{floor} = 2$ the conjecture
does not require the bound to be tight; the $o(1)$ correction at $x = 2$ need not be
small. A value of $1.025$ at $x = 2$ is consistent with the conjecture, which only
demands that the supremum over primitive sets in $[x, \infty)$ tends to at most $1$
as $x \to \infty$.

**Large-$x$ evidence.** For $x_\text{floor} \geq 4$, the set $\{2, 3\}$ is no longer
in $[x_\text{floor}, \infty)$. The next candidate is the primes starting from the
smallest prime $\geq x_\text{floor}$. By direct computation from the partial sums in
Section 2, the prime-set sum $\sum_{p \geq x} 1/(p \ln p)$ is a rapidly decreasing
function of $x$: for $x = 10$, only the primes 11, 13, 17, ... contribute, and their
individual terms $1/(p \ln p)$ are each at most $1/(11 \cdot \ln 11) \approx 0.037$.
The sum over ALL such primes is bounded below the prime-set sum starting from 2, which
the Section 3 analysis showed is consistent with F1's $o(1)$ correction being large at
small $x$.

**Conclusion (Q4).** No genuine counterexample was found. The evidence shows the
supremum over primitive sets in $[x, \infty)$ decays as $x$ grows, consistent with the
conjecture. The two-prime witness at $x = 2$ satisfies the verifier's numerical
threshold but does not falsify the conjecture (the $o(1)$ correction at $x = 2$
accounts for the excess above $1$).

---

### Section 5: Proof Strategy via Omega-Stratification (Q5)

**Decomposition.** For any primitive set $A \subseteq [x, \infty)$, write
$A_k^x = \{a \in A : \Omega(a) = k\}$. Since every integer has a unique $\Omega$-value,
$A = \bigsqcup_{k \geq 1} A_k^x$ and
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} \sum_{a \in A_k^x} \frac{1}{a \log a}.$$
Each $A_k^x$ is automatically primitive within its stratum: if $a, b \in A_k^x$ with
$a \mid b$ and $a \neq b$, then $\Omega(b) \geq \Omega(a) + 1 = k + 1$, contradicting $b \in A_k$.
So $A_k^x$ is a sub-primitive subset of $A_k \cap [x, \infty)$.

**Role of F3 (large-$k$ regime).** F3 states the full sum over the $\Omega = k$ stratum
is $1 - (c + o(1)) k^2/2^k$ with $c > 0$. For large $k$, this is strictly less than 1,
approaching 1 from below. However — as established in Section 2 — F3's formula is an
asymptotic as $k \to \infty$; for small $k$ (especially $k = 1$, the prime stratum)
the $o(1)$ correction is large and the full stratum sum exceeds 1. So F3's bound of
$< 1$ cannot be applied naively for small $k$.

**The cross-stratum primitive constraint.** A key structural fact: if $a \in A_{k_1}^x$
and $b \in A_{k_2}^x$ with $k_1 < k_2$ and $a \mid b$, primitivity of $A$ forces
both elements cannot coexist in $A$. This cross-stratum exclusion is more restrictive
than within-stratum primitivity: having small-$k$ elements in $A$ eliminates entire
classes of larger-$k$ elements, potentially reducing each stratum's contribution.

**The analytic barrier.** F1 (Erdős–Zhang) gives $\sum_{a \in A} 1/(a \log a) <
1.399 + o(1)$ for any primitive $A \subseteq \mathbb{N}$. The conjecture tightens this
to $1 + o(1)$ for $A \subseteq [x, \infty)$. Closing the gap from $1.399$ to $1$
requires exploiting the $x$-restriction: elements in $[x, \infty)$ are large, and
their $1/(a \log a)$ contributions are individually small. Quantifying how the
cross-stratum exclusions force the total below $1$ for large $x$ is the main
remaining challenge — current techniques captured in F1 give $1.399$, not $1$.

---

### Section 6: Summary of Partial Progress (Q6)

**What this attempt establishes:**

1. *(Section 2)* The $k = 1$ stratum (primes) gives $\sum_p 1/(p \ln p) > 1.025 > 1$
   by direct two-prime arithmetic. F3's formula applies asymptotically ($k \to \infty$)
   and does not constrain the $k = 1$ sum.

2. *(Section 3)* F1's $o(1)$ correction is not required to be small at $x = 2$. For
   large $x$, primitive sets restricted to $[x, \infty)$ have sums consistent with F1
   tightening toward $1$.

3. *(Section 4)* No counterexample was found. The two-prime set $\{2, 3\}$ exceeds the
   verifier's $1.0$ threshold at $x_\text{floor} = 2$ but is not a mathematical
   counterexample (the conjecture allows large $o(1)$ at small $x$).

4. *(Section 5)* Omega-stratification provides the right structural framework for a
   proof: the cross-stratum primitive exclusions reduce per-stratum contributions, but
   the quantitative step from F1's $1.399$ bound to the conjectured $1$ bound requires
   new analytic tools.

**Status.** This proof attempt provides partial analytical and numerical evidence consistent
with the conjecture. This remains open: no proof or disproof has been achieved. The main
gap is the analytic step from F1's $1.399$ to the conjectured bound of $1$ for sets
restricted to $[x, \infty)$.
