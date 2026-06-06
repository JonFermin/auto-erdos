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
  Asserting that it has been disproved, or that a counterexample has been
  constructed, without a verifier-accepted `<!-- WITNESS -->` block triggers
  `critic_openness`'s `open-claim-asserted-resolved-without-witness`
  BLOCKING. Do not write resolution-language unless `witness_valid == 1`.

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

### Section 1 — Setup

**Claim (Erdős primitive-set conjecture, tightened form)**

For any $x \geq 2$, if $A \subset [x, \infty)$ is a *primitive set* of
integers — meaning no distinct element of $A$ divides another — then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where $o(1) \to 0$ as $x \to \infty$.  In other words, the sum over any
primitive subset of $[x, \infty)$ is eventually below 1.

**Primitive set definition.** A set $A \subseteq \mathbb{N}$ is primitive
if for all $a, b \in A$ with $a \neq b$, $a \nmid b$. Examples: sets of
integers all having the same number of prime factors (the $A_k$ strata),
any antichain in the divisibility poset.

---

**Given facts ledger** (READ-ONLY; citations fixed in `proofs/primitive_set_erdos.json`)

**F1 — Erdős–Zhang upper bound** (Erdős 1935; Zhang 1993):
For *any* primitive set $A \subseteq \mathbb{N}$ (no floor on elements),
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \tfrac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
*Sign note*: This is an UPPER bound, strictly less than $\approx 1.399$.
It is CONSISTENT with the conjecture (which claims a tighter bound of 1
for primitive sets bounded away from 1).  Misreading F1 as a lower bound
is a sign error.

**F2 — $A_k$ stratum lower bound (UNSIGNED big-O)** (cited as fact F2):
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly
$k$ prime factors, counted with multiplicity).  Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$
**Critical sign disambiguation**: The $O(\cdot)$ term is *unsigned* — its
sign is unknown, so the bound only says the sum is within $|O(k^{-1/2+o(1)})|$
of 1, either above or below.  Any argument that concludes $\text{sum} > 1$
from F2 alone, without a separate positivity proof for the correction, is
a SIGN ERROR and will be rejected by `critic_sign`.

**F3 — $A_k$ stratum exact asymptotic** (cited as fact F3):
For $A_k$ as above,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$
*Sign note*: The leading correction $-(c+o(1))k^2/2^k$ is NEGATIVE for all
$k \geq 1$.  Therefore the sum approaches 1 **from below** as $k \to \infty$.
This is consistent with F2 once F2's unsigned-O is read correctly: F3
shows the unsigned $O(k^{-1/2})$ is in fact negative to leading order.
F3 directly rules out $A_k$ as a counterexample for any $k$.

---

**Witness contract** (the only path to claiming a counterexample)

To disprove the conjecture one must exhibit a finite primitive set
$A \subset [x_\text{floor}, \infty)$ (all elements $\geq x_\text{floor} \geq 2$,
pairwise non-divisible) whose sum $\sum_{a \in A} 1/(a \log a)$ exceeds
the threshold $\tau = 1.0$, as *rigorously verified* by
`library.primitive_set_witness.verify_witness`.  The claim must be
embedded in a `<!-- WITNESS ... WITNESS -->` block in this file;
`proof_prepare.py` parses the JSON, re-runs the verifier, and sets
`witness_valid = 1` only if every check passes.

The $o(1)$ caveat in the conjecture means a finite witness exceeding 1.0
is suggestive but not necessarily conclusive — a human reviewer must
additionally estimate how large the $o(1)$ gap is at the witness's
$x_\text{floor}$ before calling it a true counterexample.  However, any
witness with $\sum > 1 + \varepsilon$ for $\varepsilon$ bounded away from
zero and $x_\text{floor}$ large would be very strong evidence.

Witness schema:
```json
{
  "x_floor": "<int >= 2>",
  "elements": "<list[int], pairwise non-divisible, each >= x_floor>",
  "claimed_sum_lower_bound": "<float, verifier recomputes rigorously>"
}
```

---

**Roadmap**

- Q2+Q3: *see Section 2 below* — numerical evidence for F3 and the prime sum.
- Q4: *see Section 3 below* — witness search results.
- Q5: Outline a stratified proof structure via $\Omega$-strata.

---

### Section 2 — Numerical observations: $A_k$ truncated sums and the prime set (Q2 + Q3)

All numbers below are computations, not facts from the given-facts ledger.
They are labeled as observations and are consistent with (but not derived
from) F1, F2, and F3.

#### 2.1 Truncated sums for $k = 1, 2, 3, 4$

Computed $s_k(N) = \sum_{\substack{a \leq N \\ \Omega(a)=k}} \frac{1}{a \ln a}$ for $N = 200\,000$.
"First-200" column uses the 200 smallest elements of $A_k$.

| $k$ | $s_k(\text{first 200})$ | $s_k(200\,000)$ |
|-----|-------------------------|-----------------|
| 1 (primes, starting at 2) | **1.4965** | **1.5547** |
| 2 (semiprimes, starting at 4) | 0.6819 | 0.8416 |
| 3 (starting at 8) | 0.3134 | 0.4670 |
| 4 (starting at 16) | 0.1403 | 0.2363 |

**Observation for $k=1$**: the truncated sum grows as $N$ increases (every term
is positive) and is already $> 1$ from the first two primes alone ($1/(2 \ln 2) +
1/(3 \ln 3) \approx 0.721 + 0.303 = 1.025 > 1$).  The partial sum at $N=200\,000$
is $1.5547$, still growing.

**Observation for $k = 2, 3, 4$**: partial sums are well below 1 at
$N = 200\,000$ and growing toward 1 as more terms are included; consistent with
F3's large-$k$ prediction that each full-stratum sum approaches 1 from below.

**Note on F3 scope**: F3's asymptotic $1 - (c+o(1))k^2/2^k$ describes the
large-$k$ behavior ($o(1) \to 0$ as $k \to \infty$).  The numerical values in
the table are partial sums (up to $N = 200\,000$), not the full infinite stratum
sums; no comparison between these partial sums and F3's formula is intended here.

#### 2.2 The prime set sum (Q3)

The set $P = \{2, 3, 5, 7, 11, \ldots\}$ of all primes is a primitive set
(no prime divides another distinct prime).  Its partial sum at $N = 200\,000$ is
$s_1(200\,000) = 1.5547$.  The sum is still increasing; the partial sum
already exceeds 1 from the first two primes $\{2, 3\}$.

Note: F1's bound of $e^\gamma\pi/4 + o(1)$ is an asymptotic as $\min(A) \to \infty$;
for primes starting at 2, the $o(1)$ is not small and the bound does not apply
in the form $\approx 1.399$ here.  These numerical computations are observations
about the $k=1$ stratum behavior; they are not claims derived from F1.

---

### Section 3 — Witness search (Q4)

Tested via `library.primitive_set_witness.verify_witness` (threshold $\tau = 1.0$):

| Candidate | $x_\text{floor}$ | Rigorous lower bound | Valid? |
|-----------|-----------------|----------------------|--------|
| $\{2, 3\}$ | 2 | **1.0248** | **yes** |
| All primes in $[100, \sim5000]$ | 100 | 0.1282 | no |
| All integers in $[100, 199]$ | 100 | 0.1408 | no |

No witness was found for $x_\text{floor} \geq 100$.  For $x_\text{floor} = 1000$ and
$x_\text{floor} = 10000$ the sums are smaller still.

The $\{2, 3\}$ case is verified: the rigorous lower bound $1.0248 > 1.0$.
However, by the conjecture's $o(1)$ caveat, this requires the $o(1)$ correction
at $x = 2$ to be $< 0.0248$ for it to constitute a genuine counterexample.
Given that $s_1(200\,000) = 1.5547$ (the prime-set sum from 2 is much larger
than 1), the correction at $x = 2$ is substantial — $\{2, 3\}$ is not a
genuine counterexample.

**Open question**: can any primitive set $A \subset [x_\text{floor}, \infty)$ with
$x_\text{floor} \geq 3$ achieve sum $> 1$?  Computations suggest the answer is no
(all tested candidates fall far below 1), but no rigorous proof is committed
to this file.

---

### Section 4 — Proof structure via $\Omega$-stratification (Q5)

#### 4.1 Overview

By Lemma `stratification`, any primitive $A \subset [x, \infty)$ decomposes as
$A = \bigsqcup_k A_k$ where $A_k = A \cap \{n : \Omega(n) = k\}$, and
$\sum_{a \in A} 1/(a \ln a) = \sum_k \sum_{a \in A_k} 1/(a \ln a)$.

A stratified proof would bound each $\sum_{A_k}$ term and then sum.
The key difficulty is that the naive stratum bounds are not summable
(see Lemma `large_k_strata` for details): the sum $\sum_{k \geq 1} T_k(x)$
(where $T_k(x)$ bounds the $k$-th stratum contribution) diverges because
each term is $\leq 1$ but there are infinitely many strata.

**The primitive constraint is essential.** The stratification alone does not
give a bound — the cross-stratum interaction (see Lemma `cross_stratum_interaction`)
is what makes the problem tractable.

#### 4.2 Lemma roadmap

| Lemma | Status | Role |
|-------|--------|------|
| `stratification` | **proved** | Exact decomposition $A = \bigsqcup A_k$ |
| `large_k_strata` | open | Each stratum's contribution is at most the full-stratum sum; naive term-by-term sum does not converge |
| `prime_stratum_obstacle` | open | The $k=1$ (prime) stratum is the main obstacle; the total over all strata cannot be naively summed |
| `cross_stratum_interaction` | open (hard) | Primitive constraint between strata; the key to bounding the total |

#### 4.3 What's easy vs. hard

**Easy (given the ledger)**:
- Lemma `stratification` (proved above).
- For any $A$, the contribution from elements of $A$ with $\Omega(a)=k$ is at most the corresponding sum over the entire $k$-th stratum (since $A \cap A_k \subseteq A_k$).
- F3 shows each full-stratum sum approaches 1 from below as $k \to \infty$.

**Hard (open, not asserted)**:
- The cross-stratum interaction: bounding the total contribution when a primitive set spans multiple strata.  The primitive constraint prevents certain combinations but its quantitative strength is not established from F1/F2/F3 alone.

#### 4.4 Proposed direction for a future session (speculative, not asserted)

A possible approach to the cross-stratum interaction is via Dirichlet series:
one could attempt to represent $1/(a \ln a)$ as an integral and bound the
resulting Dirichlet series for a primitive set $A$.  The approach used in
the proof of F1 (Erdős-Zhang) is known to use multiplicative structure.
No claim is made here about the feasibility or completeness of this approach;
it is noted purely as a potential direction for future sessions.

---

### Section 5 — Partial result and status summary (Q6)

**This proof attempt converged on a partial result after session 1.**
The conjecture remains open; here is what was established and what remains open.

#### 5.1 What was established (this session)

1. **Setup and ledger** (Section 1): The claim, F1/F2/F3 with sign
   disambiguations, and witness contract are fully documented.

2. **Numerical evidence** (Sections 2–3):
   - The $k=1$ stratum (primes) has partial sum $s_1(200\,000) = 1.5547 > 1$;
     the sum exceeds 1 from the first two primes $\{2,3\}$ alone.
   - For $k = 2, 3, 4$, partial sums are well below 1 (0.84, 0.47, 0.24 resp.).
   - F3's formula $1 - (c+o(1))k^2/2^k$ is a large-$k$ asymptotic;
     for $k=1$ it is far from the actual (large) value.
   - No witness with $x_\text{floor} \geq 100$ was found; $\{2,3\}$ with
     $x_\text{floor}=2$ is a verifier-accepted witness (sum 1.0248) but
     is not a genuine counterexample due to the $o(1)$ slack at $x=2$.

3. **Proof structure** (Section 4):
   - Lemma `stratification`: proved ($A = \bigsqcup_k A_k$ decomposition).
   - Lemma `large_k_strata`: identified — the naive stratum-by-stratum bound
     DIVERGES; the primitive constraint is essential.
   - Lemma `prime_stratum_obstacle`: identified — for $x \geq 3$ the prime
     contribution is bounded, but the bound is not in the ledger.
   - Lemma `cross_stratum_interaction`: identified as the CORE HARD PROBLEM
     — quantifying how the primitive constraint between strata prevents the
     sum from exceeding $1 + o(1)$.

#### 5.2 What was ruled out

- **The stratum-sum-only approach** (sum each $T_k(x)$ independently) is
  RULED OUT as a path to the bound: the sum $\sum_k T_k(x)$ diverges.
  The primitive constraint MUST be used.

- **Witnesses with $x_\text{floor} \geq 100$**: none found numerically;
  all tested candidates scored far below 1.0.

- **The primes as a genuine counterexample**: for $x_\text{floor} \geq 3$,
  the primes give sum $< 1$; the $\{2,3\}$ witness at $x_\text{floor}=2$ is
  not a genuine counterexample (the $o(1)$ term at $x=2$ is large).

#### 5.3 What remains open (hard)

The core challenge is Lemma `cross_stratum_interaction`: proving that the
primitive constraint between strata is strong enough to give a total bound
$< 1 + o(1)$.  The suggested approach (Euler product on $D_A(s)$) requires:
- Establishing $D_A(1+t)$ bounds for primitive $A \subset [x, \infty)$.
- Integrating the bound over $t \in [0, \infty)$.
- Showing the result is $< 1 + o(1)$ with $o(1) \to 0$ as $x \to \infty$.

This is consistent with the approach used to prove F1 (the Erdős-Zhang 1.399
bound) and is the most promising next direction.

**Status**: partial result. The proof infrastructure is in place; the hard
analytical work on Lemma `cross_stratum_interaction` is the next session's task.
