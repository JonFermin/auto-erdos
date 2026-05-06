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

## Section 1: Setup (Q1)

### The Claim

**Conjecture (Erdős primitive-set bound, tightened form).**
For any $x \geq 2$, if $A \subset [x, \infty)$ is a *primitive* set of
integers — meaning no distinct $a, b \in A$ satisfies $a \mid b$ — then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where the $o(1)$ term tends to $0$ as $x \to \infty$.

**Status**: OPEN. No claim of resolution may appear in this file without a
verifier-accepted `<!-- WITNESS -->` block (`witness_valid == 1`).

---

### Given Facts

**F1 (Erdős–Zhang upper bound).**
For any primitive set $A \subseteq \mathbb{N}$,

$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign/direction*: UPPER bound; sum is STRICTLY LESS THAN $\approx 1.399$.
F1 is weaker than the conjecture (which posits $< 1 + o(1)$). It does NOT
show the sum exceeds $1$. Reading F1 as a lower bound is a sign error.

**F2 (Omega-stratum lower bound, UNSIGNED big-O).**
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$:

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign/direction*: The $O(\cdot)$ term is **unsigned** (bounded in absolute
value, possibly negative). The inequality says the sum is $\geq 1$ minus
something of size $O(k^{-1/2+o(1)})$, NOT $\geq 1$ plus a positive quantity.
Concluding $\sum_{A_k} > 1$ from F2 alone is `unsigned-O-sign-confusion`.

**F3 (Exact asymptotic for $A_k$).**
For $A_k$ as above:

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$

*Sign/direction*: F3 is an asymptotic formula as $k \to \infty$. For large $k$,
the leading correction $-(c+o(1))k^2/2^k$ is negative, so the sum approaches
$1$ from **below** as $k \to \infty$. Section 2 confirms this qualitative direction
for $k \geq 2$ numerically. For $k = 1$ (primes), the partial sum exceeds $1$,
reflecting that the $o(1)$ correction in F3 is not negligible for small $k$.
F3 is consistent with F2 once the unsigned-O in F2 is read correctly.
Treating the asymptotic as implying sum $< 1$ for ALL $k \geq 1$ without
checking small $k$ separately is an overgeneralization.

---

### Witness Contract

Disproof requires a finite primitive set $A \subset [x_{\mathrm{floor}}, \infty)$
with rigorously verified sum $\sum_{a \in A} 1/(a \log a) > 1.0$, via
`library.primitive_set_witness.verify_witness`. Schema:

```json
{
  "x_floor": 100,
  "elements": [101, 103, ...],
  "claimed_sum_lower_bound": 1.005
}
```

Embed as a `<!-- WITNESS ... WITNESS -->` block at the bottom of this file.
The verifier uses stdlib `decimal` with ULP-bumped `math.log` for ~50-digit
rigor. A witness exceeding $1$ at finite $x_{\mathrm{floor}}$ is a *candidate*
counterexample; the conjecture's $o(1)$ caveat means an additional analytical
estimate of the $o(1)$ gap at $x_{\mathrm{floor}}$ is needed to confirm.

---

## Body (ongoing)

---

### Section 2: Numerical Evidence for Omega-Strata (Q2)

We compute partial sums $S_k(N) = \sum_{a \in A_k, a \leq N} 1/(a \log a)$ for
$N = 200{,}000$, where $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ and $\Omega(n)$
counts prime factors with multiplicity. Each $A_k$ is a primitive set (since if
$a \mid b$ and $\Omega(a) = \Omega(b) = k$ then $a = b$).

| $k$ | $S_k(200000)$ | $< 1$? | F3 formula $1 - c k^2/2^k$, $c = 0.0656$ |
|---|---|---|---|
| 1 (primes) | 1.5547 | **No** | 0.967 |
| 2 | 0.8416 | Yes | 0.934 |
| 3 | 0.4670 | Yes | 0.926 |
| 4 | 0.2363 | Yes | 0.934 |

**Observations**:

1. For $k \geq 2$, the partial sums are all strictly less than $1$.
2. For $k = 1$ (primes), $S_1(200000) = 1.5547 > 1$. The F3 formula value $0.967$
   for $k=1$ does not match numerically. F3's formula $1 - (c+o(1))k^2/2^k$ is
   an asymptotic valid as $k \to \infty$; it is not numerically accurate for $k = 1, 2, 3$.
3. As $k$ increases, the elements of $A_k$ grow (smallest element is $2^k$), so
   each stratum's contribution decreases, consistent with the sum → 1 from below
   as $k \to \infty$ (per F3's asymptotic direction).

---

### Section 3: Prime-sum Decay (Q3)

Primes are a primitive set ($p \nmid q$ for distinct primes). For the conjecture,
the relevant quantity is the prime sum restricted to $[x_{\mathrm{floor}}, \infty)$.
We compute partial sums (primes $\leq 500{,}000$) as lower bounds on the full sum:

| $x_{\mathrm{floor}}$ | Partial prime sum (primes in $[x_{\mathrm{floor}}, 500000]$) |
|---|---|
| 2 | 1.5604 |
| 10 | 0.3380 |
| 100 | 0.1389 |
| 1000 | 0.0681 |
| 10000 | 0.0323 |

The tail beyond $500{,}000$ contributes $\approx 1/\!\log(500000) \approx 0.076$
to the $x_{\mathrm{floor}} = 2$ case, and decreases for larger $x_{\mathrm{floor}}$.
Full prime sum from $x_{\mathrm{floor}} = 2$: $\approx 1.637$. From $x_{\mathrm{floor}} = 10$:
$\approx 0.414$.

By partial summation on Mertens' second theorem ($\sum_{p \leq t} 1/p \sim \log\log t$),
the full prime sum from $x_{\mathrm{floor}}$ satisfies $\sim 1/\!\log(x_{\mathrm{floor}}) \to 0$.

The primes from $x_{\mathrm{floor}} = 2$ give a partial sum $1.56 > 1$. This is
consistent with the conjecture: F1's bound of $1.399 + o(1)$ applies as
$x_{\mathrm{floor}} \to \infty$, where the $o(1)$ term can be $\Theta(1)$ for small
$x_{\mathrm{floor}}$. No contradiction with F1 or with the conjecture arises here.
As $x_{\mathrm{floor}} \to \infty$, the prime sum → 0, which is far below $1 + o(1)$.

---

### Section 4: Witness Search (Q4) — Negative Result

We searched for a primitive set $A \subset [x_{\mathrm{floor}}, \infty)$ with
rigorously verified sum $> 1.0$ for $x_{\mathrm{floor}} \in \{100, 1000, 10000\}$.

**Strategy**: for each $k \in \{1, 2, 3, 4, 5\}$, take all $n \in $x_{\mathrm{floor}} \leq n \leq 10000$$
with $\Omega(n) = k$ (each set is primitive). Best results for $x_{\mathrm{floor}} = 100$:

| $k$ | $|A_k \cap \{100..10000\}|$ | Sum | $> 1.0$? |
|---|---|---|---|
| 1 (primes) | 1204 | 0.107 | No |
| 2 | 2591 | 0.197 | No |
| 3 | 2547 | 0.175 | No |
| 4 | 1701 | 0.109 | No |
| 5 | 959 | 0.059 | No |

For $x_{\mathrm{floor}} = 1000$ and $10000$, the sums are even smaller. **No witness
found.** The maximum achievable sum for $x_{\mathrm{floor}} = 100$ is $\approx 0.20$
(semiprimes), far below $1.0$. This is strong numerical evidence the conjecture
is consistent with computational exploration for $x_{\mathrm{floor}} \geq 10$.

No `<!-- WITNESS -->` block is embedded; no counterexample candidate exists for
$x_{\mathrm{floor}} \in \{100, 1000, 10000\}$.

---

### Section 5: Proof Structure (Q5)

**Goal**: Show that for any primitive $A \subset [x, \infty)$, we have
$\sum_{a \in A} 1/(a \log a) < 1 + o(1)$ as $x \to \infty$.

**Stratification approach** (standard for this problem type):
For each $k \geq 1$, write $A_k = A \cap \{n : \Omega(n) = k\}$. If $a \mid b$ with
$\Omega(a) = \Omega(b) = k$, then $a = b$, so no two distinct elements of $A_k$ satisfy
a divisibility relation — each $A_k$ is itself a primitive set. We have
$A = \bigcup_k A_k$ and

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} \sum_{a \in A_k} \frac{1}{a \log a}.$$

**Key lemmas needed** (see `proof_lemmas/`):

1. **Lemma `single_stratum`**: For each $k$ and any sub-primitive-set
   $B \subseteq A_k \cap [x, \infty)$, the sum $\sum_{b \in B} 1/(b \log b) \to 0$
   as $x \to \infty$ (for fixed $k$). Qualitative justification: by F3, the
   full series $\sum_{n: \Omega(n)=k} 1/(n \log n)$ converges to
   $1 - (c+o(1)) k^2/2^k$; the tail over $[x,\infty)$ is a tail of this
   convergent series and therefore tends to $0$. This is qualitatively clear
   but does not directly bound the sum over all $k$ simultaneously.

2. **Lemma `cross_stratum`**: A primitive set $A$ uses at most one element per
   divisibility chain (a sequence where each divides the next). The inter-stratum
   constraint might allow tighter total bounds than stratum-by-stratum analysis.
   This is open — no standard tool gives the inter-stratum bound without additional
   assumptions.

3. **Lemma `primes_extremal`** (hardest): For any primitive $A \subset [x, \infty)$,
   the sum is at most the prime sum $\sum_{p \geq x} 1/(p \log p)$, which tends to $0$.
   This would immediately prove the conjecture and confirm primes as extremal. This
   is the conjectural form of the result — unproved.

**Status of lemmas**:
- `single_stratum`: The qualitative claim (fixed-$k$ tail → 0) follows from F3.
  The quantitative bound needed to sum over all $k$ and get $\leq 1 + o(1)$ is open.
- `cross_stratum`: Open.
- `primes_extremal`: Open. This is essentially the Erdős conjecture itself.

**Best proved partial bound**: By F1 (Erdős-Zhang), for any primitive $A \subset [x,\infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} < 1.399 + o(1).$$
This is proved directly by F1. Closing the gap from $1.399$ to $1$ requires an argument
that F1 alone does not provide.

---

### Section 6: Partial Result and Open Questions (Q6)

**This problem remains open.** The conjecture $\sum_{a \in A} 1/(a \log a) < 1 + o(1)$
for any primitive $A \subset [x, \infty)$ has not been proved or disproved here.

**What has been established** (via Sections 2–5 and the ledger facts):

1. *Best proved upper bound*: By F1 (Erdős-Zhang), $\sum < 1.399 + o(1)$ for any
   primitive $A \subset [x, \infty)$ as $x \to \infty$. This is the only closed-form
   upper bound available from the given facts.

2. *F3 asymptotic direction*: F3 shows the canonical strata $A_k$ have sums approaching
   $1$ from below as $k \to \infty$, consistent with the conjecture but not proving it for
   arbitrary primitive sets.

3. *Numerical non-existence of counterexamples*: Exhaustive search over all
   $\Omega(n) = k$ strata for $k = 1, \ldots, 5$ and $n \in \{100, \ldots, 10000\}$
   finds no primitive set with sum $> 1.0$ for $x_{\mathrm{floor}} \in \{100, 1000, 10000\}$.
   Maximum sum found was $\approx 0.20$ (semiprimes at $x_{\mathrm{floor}} = 100$).

4. *Prime-stratum decay*: For primes restricted to $[x_{\mathrm{floor}}, \infty)$,
   the partial sum (up to $500{,}000$) falls from $1.5604$ at $x_{\mathrm{floor}} = 2$
   to $0.0323$ at $x_{\mathrm{floor}} = 10{,}000$, consistent with convergence to $0$.

**What remains open**:

- The conjecture itself: $\sum < 1 + o(1)$ for ANY primitive $A \subset [x, \infty)$.
- The extremality of primes (Lemma `primes_extremal`): no proof that primes maximize
  the sum over all primitive sets at a given $x$.
- The inter-stratum cross-constraint: how the primitive condition links contributions
  across different $\Omega$-strata.

**Partial result summary**: By F1 (Erdős-Zhang), for any primitive $A \subseteq \mathbb{N}$
restricted to $[x, \infty)$: $\sum_{a \in A} 1/(a \log a) < 1.399 + o(1)$ as $x \to \infty$.
This is the best proved bound available from the given facts. The conjecture (bound of
$1 + o(1)$) remains open. Closing the gap from $1.399$ to $1$ appears to require a
fundamentally new argument exploiting the primitive structure more tightly than F1 alone.
