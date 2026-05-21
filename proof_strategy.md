# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

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
  Phrases like "the conjecture is false" / "we disprove" trigger
  `critic_openness`'s `open-claim-asserted-resolved-without-witness`
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

---

## Section 1 — Setup

### 1.1 The Claim

**Erdős primitive-set conjecture (tightened form):**
For any primitive set $A \subset [x, \infty)$ (a set of positive integers,
no two of which are in a divisibility relation), we have
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$
where the $o(1)$ term tends to $0$ as $x \to \infty$.

Equivalently: for any $\varepsilon > 0$ there exists $X_\varepsilon$ such
that for all $x \geq X_\varepsilon$ and all primitive $A \subset [x,\infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq 1 + \varepsilon.$$

The conjecture is **open**. Proof-of-upper-bound strategies and
counterexample searches are both in scope for this attempt.

### 1.2 The Three Given Facts

**F1 — Erdős–Zhang upper bound (UPPER bound, ~1.399).**
For *any* primitive set $A \subseteq \mathbb{N}$ (not restricted to
$[x, \infty)$),
$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
Sign: strictly LESS THAN 1.399. This is an UPPER bound. It is consistent
with the conjecture (which aims for 1); it does not prove it (since 1.399 > 1).
A primitive set achieving sum close to 1.399 would disprove the conjecture.

**F2 — Omega-stratum lower bound (UNSIGNED big-O).**
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (numbers with exactly $k$
prime factors counted with multiplicity),
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$
**Critical sign warning**: the $O(\cdot)$ term is **unsigned** — it can
be positive or negative. This inequality does NOT imply the sum exceeds 1.
Concluding "sum > 1" from F2 alone is a **SIGN ERROR** (the classic
ChatGPT failure mode). F2 is consistent with F3 once unsigned-O is read
correctly.

**F3 — Exact asymptotic for $A_k$ (sum approaches 1 from BELOW).**
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
The correction $-(c+o(1))k^2/2^k$ is **negative** (since $c > 0$), so
$\sum_{A_k} < 1$ for every $k \geq 1$, approaching 1 from **below** as
$k \to \infty$. The canonical "extremal-looking" sets $A_k$ do NOT
violate the conjecture.

### 1.3 The Witness Contract

To claim a counterexample, one must exhibit a **finite** primitive set
$A \subset [x_\mathrm{floor}, \infty)$ with
$$\sum_{a \in A} \frac{1}{a \log a} > 1 \quad \text{(rigorously verified)}.$$
The verifier contract:
- `x_floor`: every element of `elements` must be $\geq x_\mathrm{floor}$.
- `elements`: list of distinct integers, pairwise non-divisible.
- `claimed_sum_lower_bound`: agent's own lower-bound claim; verifier
  recomputes rigorously from the actual elements.
The verifier `library.primitive_set_witness.verify_witness` is the sole
arbiter. `witness_valid == 1` is required before any disproof claim.

**Important caveat**: a witness at finite $x_\mathrm{floor}$ with sum > 1
is a genuine counterexample only if the $o(1)$ correction at that
$x_\mathrm{floor}$ is estimated to be small. A witness with sum 1.001 at
$x_\mathrm{floor} = 2$ is NOT convincing without a separate estimate of
the $o(1)$ gap.

---

## Section 2 — Numerical Exploration (Q2: F3 verification; Q3: primes sum)

### 2.1 Omega-stratum sums (F3 numerics)

*[To be filled in by Q2 round.]*

### 2.2 Sum over primes (Q3)

*[To be filled in by Q3 round.]*

---

## Section 3 — Witness Search (Q4)

*[To be filled in by Q4 round.]*

---

## Section 4 — Proof Strategy Outline (Q5)

*[To be filled in by Q5 round.]*

---

## Section 5 — Lemma Files

*Lemmas will be created in `proof_lemmas/lemma_*.md`.*
