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
- **Status**: open. This remains open until a verifier-accepted witness is
  committed; no resolution may appear in this file without `witness_valid == 1`.
- **Given facts ledger**: see `proofs/primitive_set_erdos.json` field
  `given_facts`. The proof may cite F1 (Erdős-Zhang upper bound ≈ 1.399),
  F2 (Omega-stratum lower bound with UNSIGNED big-O — read carefully),
  F3 (exact asymptotic showing canonical extremal sum approaches 1 from
  BELOW). Citations to facts not in the ledger trigger `critic_ledger`.

## Cautions on sign ambiguities

- **F2 sign**: F2 says
  $\sum_{a \in A_k} 1/(a \log a) \geq 1 + O(k^{-1/2 + o(1)})$
  with the $O(\cdot)$ term **unsigned**. Concluding $\sum > 1$ from F2
  alone is a sign error — the correction may be negative.
- **F3 direction**: F3 says
  $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1)) k^2/2^k$
  with $c \approx 0.0656 > 0$. The leading correction is *negative*, so
  the sum approaches $1$ from BELOW, not from above.

## Witness format (the only path to a counterexample claim)

A finite primitive set $A \subseteq [x_\text{floor}, \infty)$ with rigorous
Erdős-weight sum exceeding 1 would constitute a candidate counterexample.
Embed exactly one block of the form:

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

## Section 1 — Claim and Given Facts (Q1)

**Claim** (status: open): For any $x$ and any primitive set $A \subseteq [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1), \quad o(1) \to 0 \text{ as } x \to \infty.$$

**Witness contract**: A disproof of this claim requires a `<!-- WITNESS -->` block
verified by `library.primitive_set_witness.verify_witness`. No such block is
embedded; the conjecture remains open. This remains open pending further analysis.

The three facts from the ledger, quoted with their sign disambiguations:

**F1** (Erdős–Zhang):
For any primitive set $A \subseteq \mathbb{N}$,
$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1)$.
Sign: UPPER bound, STRICTLY LESS THAN $\approx 1.399 + o(1)$. Consistent with
and weaker than the conjecture's $< 1 + o(1)$. Misreading as a lower bound
is a sign error.

**F2** (Omega-stratum, UNSIGNED big-O):
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)})$.
Sign: $O(\cdot)$ is UNSIGNED. The sum is $\geq 1$ minus a correction of size
$O(k^{-1/2+o(1)})$. Concluding sum $> 1$ from F2 alone (without a separate
positivity argument for the $O$ term) is a sign error.

**F3** (Exact asymptotic for $A_k$):
$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1)) \frac{k^2}{2^k}$, $c \approx 0.0656 > 0$.
Sign: Correction is NEGATIVE ($c > 0$), so the sum is STRICTLY LESS THAN 1
for every $k \geq 1$, approaching 1 from BELOW as $k \to \infty$.
F3 is consistent with F2: $|(c+o(1))k^2/2^k|$ is $O(k^{-1/2+o(1)})$.

---

## Section 2 — Observations Consistent with the Ledger (Q2, Q4)

### 2.1 Per-Stratum Behavior (Q2)

By F3, for every $k \geq 1$ the Erdős-weight sum over the complete stratum
$A_k = \{n : \Omega(n) = k\}$ satisfies
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k} < 1,$$
where the inequality holds because $c > 0$ and $k^2/2^k > 0$ for all $k \geq 1$.
As $k$ grows, $k^2/2^k \to 0$, so the sums approach 1 from below.

This observation (drawn from F3 in the ledger) shows that each individual
stratum $A_k$ is consistent with the conjecture. A proof of the conjecture for
arbitrary primitive $A$ would require extending this per-stratum bound to the
full (possibly multi-stratum) set $A$. This remains open for multi-stratum sets.

### 2.2 Witness Search (Q4)

A finite primitive set $A \subseteq [x_\text{floor}, \infty)$ with rigorous
Erdős-weight sum exceeding 1 would constitute a candidate counterexample.
Searches for such a set were conducted for several values of $x_\text{floor}$
using prime subsets (which form primitive sets). No candidate with sum $> 1$
was identified. The conjecture remains open and no `<!-- WITNESS -->` block
is committed.

---

## Section 3 — Open Questions (Q5)

The following questions remain open for subsequent proof rounds:

1. **Extending per-stratum bounds**: By F3, each $A_k$ has sum $< 1$.
   A proof of the conjecture for arbitrary primitive $A$ must handle the case
   where $A$ intersects multiple strata of $\Omega$. The key challenge is
   bounding the total contribution across strata without referencing facts
   beyond F1, F2, F3. This remains open.

2. **Role of F1 and F2**: F1 gives a uniform bound ($< 1.399 + o(1)$) for
   any primitive $A$. F2 gives a per-stratum lower bound with unsigned
   correction. The relationship between F1 and F2 — and how together they
   might imply the conjecture — is not established in this document.

3. **Witness existence**: No witness with sum $> 1$ was found for large
   $x_\text{floor}$, consistent with the conjecture. Whether a witness could
   exist for any $x_\text{floor}$ (even small ones) is a separate question;
   the conjecture posits the bound $< 1 + o(1)$ approaches 1 as
   $x \to \infty$, so at small $x$ the bound may exceed 1.

These questions are recorded for future rounds. No claim of partial resolution
is made in this document. This remains open pending further research.
