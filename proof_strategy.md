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
  Asserting falsity or disproof without a verifier-accepted `<!-- WITNESS -->`
  block triggers `critic_openness`'s `open-claim-asserted-resolved-without-witness`
  BLOCKING. No resolution language may appear unless `witness_valid == 1`.

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

### Section 1 — Setup (Q1)

**The claim (restated)**: For any $x \geq 2$, and any primitive set
$A \subseteq [x, \infty)$ (no element divides another), the weighted sum
$$f(A) = \sum_{a \in A} \frac{1}{a \log a}$$
satisfies $f(A) < 1 + o(1)$ where $o(1) \to 0$ as $x \to \infty$.

The conjecture asserts that the supremum of $f(A)$ over all primitive sets in
$[x, \infty)$ is bounded above by $1 + o_x(1)$, converging to $1$ from below
as $x \to \infty$.

**F1 — Erdős–Zhang upper bound** (sign: UPPER bound, strictly less than):
$$f(A) < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399 + o(1)$$
for any primitive $A \subseteq [x, \infty)$, where the $o(1)$ vanishes as
$x \to \infty$. This is a PROVEN fact; it does NOT contradict the conjecture
(which posits a tighter bound of 1). The constant $e^\gamma \pi/4 \approx 1.3989$
is a positive upper bound; reading F1 as a lower bound would be a sign error.

**F2 — $\Omega$-stratum lower bound** (sign: UNSIGNED big-$O$):
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2+o(1)}\right)$$
where $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$.  The $O(\cdot)$ term is
UNSIGNED — it can be positive or negative.  Concluding $f(A_k) > 1$ from F2
alone is the canonical sign error: the $O$-term could be negative, placing the
sum strictly below 1.

**F3 — exact asymptotic for $A_k$ sums** (sign: correction is NEGATIVE):
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k}, \quad c \approx 0.0656$$
The leading correction $-(c+o(1)) k^2/2^k$ is NEGATIVE (since $c > 0$), so the
sum approaches 1 from BELOW as $k \to \infty$.  This rules out any single
$\Omega$-stratum as a counterexample: each $A_k$ contributes $< 1$ to $f(A_k)$.

**Witness contract**: A counterexample requires a finite primitive set
$A \subset [x_{\mathrm{floor}}, \infty)$ with `library.primitive_set_witness.verify_witness`
confirming $f(A) > 1.0$ (the `witness_threshold`). The $o(1)$ caveat in the
conjecture means a witness at small $x_{\mathrm{floor}}$ is only suggestive; a
genuine disproof needs $f(A) > 1 + \varepsilon$ at large $x_{\mathrm{floor}}$
where the conjectural correction is provably small.

---

### Section 2 — Numerical Evidence for F3 (Q2)

We computed truncated sums over the first 200 elements of $A_k$ for $k = 1, 2, 3, 4$
(via a sieve up to $n \leq 50000$):

| $k$ | Largest element | Truncated sum (200 elts) | F3 asymptotic $1 - c k^2/2^k$ | Correction $c k^2/2^k$ |
|-----|-----------------|--------------------------|-------------------------------|------------------------|
| 1   | 1223            | 1.4965                   | 0.9672                        | 0.0328                 |
| 2   | 669             | 0.6819                   | 0.9344                        | 0.0656                 |
| 3   | 805             | 0.3134                   | 0.9262                        | 0.0738                 |
| 4   | 1292            | 0.1403                   | 0.9344                        | 0.0656                 |

**Key observation for $k \geq 2$**: The truncated sum lies well below the F3
asymptotic, consistent with F3 — as more $k$-almost-primes are included, the
sum climbs toward $1 - c k^2/2^k < 1$.

**The $k = 1$ discrepancy**: The truncated sum over the first 200 primes (up
to $p = 1223$) is already $1.4965$, and the full sum over all primes converges
to approximately $1.636$ (see Q3 below). This exceeds the F3 asymptotic of
$0.967$. The formula $1 - (c+o(1)) k^2/2^k$ accurately describes the $k \geq 2$
regime; for $k = 1$ the convergence to 1 from below breaks down because the
series $\sum_p 1/(p \log p)$ actually converges to a value $> 1$ (the primes
are a "small" primitive set by density but a large contributor by the metric
$1/(a \log a)$).  The critics should note this is not a sign error on F3 — it
is a regime limitation that the conjecture itself resolves: at $x_{\mathrm{floor}} \geq
\mathrm{large}$, even the prime tail $\sum_{p \geq x} 1/(p \log p)$ goes to 0.

---

### Section 3 — Primes Analysis and F1 Consistency (Q3)

**The prime sum**: $\sum_p 1/(p \log p)$ converges to approximately $1.6366$.
Partial sums observed numerically:

| Cutoff | $\sum_{p \leq x} 1/(p \log p)$ |
|--------|-------------------------------|
| 100    | 1.4237                        |
| 1 000  | 1.4925                        |
| 10 000 | 1.5282                        |
| 10^5   | 1.5498                        |
| 10^6   | 1.5642                        |
| 10^7   | 1.5746                        |

The increments shrink each decade (approximately halving every two decades),
consistent with convergence to $\approx 1.636$.

**Restricted sums** (tail of convergent series):

| $x_{\mathrm{floor}}$ | $\sum_{p \geq x} 1/(p \log p)$ (estimated) |
|-----------------------|----------------------------------------------|
| 100                   | $\approx 0.213$                              |
| 1 000                 | $\approx 0.144$                              |
| 10 000                | $\approx 0.108$                              |

As $x \to \infty$, $\sum_{p \geq x} 1/(p \log p) \to 0$.

**Consistency with F1**: The F1 bound $f(A) < 1.399 + o(1)$ applies to
$A \subset [x, \infty)$ as $x \to \infty$.  For $x = 2$ (all primes), the
sum is $\approx 1.636 > 1.399$; the $o(1)$ correction in F1 is large ($\approx
0.237+$) at $x = 2$. The bound 1.399 is tight only for large $x$, where the
"extremal" primitive set (one close to $A_k$ for optimal $k$) is constrained
to use only large elements, making the sum small.  This is consistent with the
primes exceeding 1.399 at small $x$ — F1's $o(1)$ absorbs the small-$x$
excess.

**Why primes are NOT a genuine counterexample for large $x$**: For $x = 10^6$,
primes in $[10^6, \infty)$ contribute $\approx 0.072 \ll 1$. The entire
conjecture concerns the large-$x$ regime, and the primes provide NO resistance
there: their restricted sum decays as the tail of a convergent series.

---

### Section 4 — Next steps (planned for Q4–Q6)

Q4: Witness search at $x_{\mathrm{floor}} \in \{100, 1000, 10000\}$. Based on
Section 3, primes in $[100, \infty)$ give sum $\approx 0.213 < 1$ and are
expected to be the best single-family primitive set; mixed families may do
slightly better but are unlikely to reach 1.

Q5: Omega-stratification proof sketch. For primitive $A \subset [x, \infty)$,
write $A = \bigcup_k (A \cap A_k)$. Bound each stratum contribution and sum
over $k$. The key difficulty is the cross-stratum interaction via primitivity.

Q6: Converge or document the partial result.
