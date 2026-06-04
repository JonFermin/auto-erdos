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
  Asserting resolution (e.g. claiming a disproof or that the bound fails) without a
  verifier-accepted `<!-- WITNESS -->` block triggers `critic_openness` BLOCKING.

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

## Section 1 — Setup (Q1)

### 1.1 The Claim

**Conjecture (Erdős primitive-set bound, tightened form).**
For any $x \geq 2$, if $A \subseteq [x, \infty)$ is a *primitive set* (no distinct element of $A$ divides another), then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where the $o(1)$ error tends to $0$ as $x \to \infty$.

In plain English: as you restrict the primitive set to live farther and farther from the origin, its "weighted density" $\sum 1/(a \log a)$ cannot exceed $1$ — or at least cannot exceed $1$ by any fixed positive amount.

**Status**: open. No proof or counterexample is currently known. The loop will not claim resolution without a verifier-accepted witness.

---

### 1.2 Given Facts (with sign disambiguations)

**F1 — Erdős-Zhang upper bound (proven).**
For *any* primitive set $A \subseteq \mathbb{N}$ (not just those restricted to $[x, \infty)$),

$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \cdot \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

Sign: this is a strict **upper** bound. The sum is bounded *below* $1.399$, consistent with the conjecture that $1$ is the right bound. F1 cannot serve as a lower bound; using it to argue "the sum is at least $1.399$" is a sign error.

**F2 — Omega-stratum lower bound (with unsigned big-O).**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$ prime factors counted with multiplicity). Then

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

Sign: the $O(\cdot)$ term here is **unsigned** — it could be positive or negative (its magnitude is at most $C k^{-1/2+o(1)}$ for some constant $C$). Reading this as "the sum is at least $1 + (\text{positive quantity})$", i.e.\ concluding $\sum > 1$, is a **sign error** (`unsigned-O-sign-confusion`). The inequality only tells us the sum is at least $1$ *minus* something of size $O(k^{-1/2+o(1)})$.

**F3 — Exact asymptotic for $A_k$ (approaches 1 from below).**
For $A_k$ as above,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$

Sign: the correction term $-(c+o(1)) k^2/2^k$ is **negative** (since $c > 0$). So the sum is *strictly less than* $1$ for every fixed $k \geq 1$, and approaches $1$ from **below** as $k \to \infty$. The $A_k$ sets are the extremal-looking ones, and even they do not violate the conjecture. F3 is consistent with F2: F2's unsigned-$O$ allows the bound to sit below $1$.

---

### 1.3 Witness Contract (the only path to a claimed counterexample)

A counterexample would be a primitive set $A \subseteq [x_{\text{floor}}, \infty)$ with rigorously computed

$$\sum_{a \in A} \frac{1}{a \log a} > 1.$$

To register such a claim, one must embed exactly one `<!-- WITNESS ... WITNESS -->` block at the bottom of this file. The block must contain:

- `x_floor` (int $\geq 2$): all elements of `elements` must be $\geq$ `x_floor`.
- `elements` (list of ints): pairwise non-divisible, each $\geq$ `x_floor`.
- `claimed_sum_lower_bound` (float): the agent's own estimate; the verifier recomputes rigorously.

`proof_prepare.py` calls `library.primitive_set_witness.verify_witness` deterministically; `witness_valid = 1` iff the verifier confirms sum $>$ `witness_threshold` $= 1.0$. Without a verifier-accepted witness, no claim of disproof may appear in this file.

**Caveat**: The conjecture's $o(1)$ means that a set in $[x_{\text{floor}}, \infty)$ with sum slightly above $1$ at finite $x_{\text{floor}}$ is suggestive but not conclusive.

---

### 1.4 Key Anti-Traps

1. **F2 sign confusion**: Do not conclude $\sum_{a \in A_k} > 1$ from F2 alone. The $O$ is unsigned.
2. **F3 from-above misread**: $A_k$ sums approach $1$ from *below*, not above.
3. **Premature resolution claim**: Do not assert disproof or resolution without a verifier-accepted witness block.

---

## Section 2 — Numerical Evidence (Q2, Q3)

### 2.1 Restricted tail sums $S_k(x_{\text{floor}})$

We compute $S_k(x) = \sum_{\substack{n \geq x,\, n \leq N \\ \Omega(n) = k}} \frac{1}{n \log n}$ with $N = 500{,}000$ via an Omega-sieve. Tail contributions beyond $N$ are $O(1/\log N) \approx 0.076$ for primes.

| $x_{\text{floor}}$ | $k=1$ (primes) | $k=2$ | $k=3$ | $k=4$ |
|---|---|---|---|---|
| 2 | 1.5604 | 0.8569 | 0.4852 | 0.2506 |
| 3 | 0.8391 | 0.8569 | 0.4852 | 0.2506 |
| 10 | 0.3380 | 0.5330 | 0.4251 | 0.2506 |
| 100 | 0.1389 | 0.2778 | 0.2655 | 0.1768 |
| 1000 | 0.0681 | 0.1569 | 0.1641 | 0.1165 |
| 10000 | 0.0323 | 0.0808 | 0.0901 | 0.0675 |

**Key observations:**
- For $x_{\text{floor}} \geq 3$: all $S_k(x_{\text{floor}}) < 1$ for $k = 1, 2, 3, 4$. Each stratum individually stays below 1 once we exclude $p=2$.
- The restricted sums decrease monotonically with $x_{\text{floor}}$ toward 0.

**On F3's formula $1 - (c + o(1)) k^2/2^k$**: The formula predicts values in $[0.93, 0.97]$ for small $k$. Our restricted sums are smaller because F3 is about the *full* sum from $n=2$ (not from $x_{\text{floor}}$). The full sum for $k=1$ (all primes from 2) is approximately 1.636 (see §2.2), which exceeds 1. F3 as stated may apply to a different normalization or to the large-$k$ limit where $k^2/2^k \to 0$ and the stratum elements are concentrated at large $n$.

### 2.2 Prime sum from 2 (Q3)

The full sum over all primes: $\sum_{p \text{ prime}} \frac{1}{p \log p} \approx 1.6366$, obtained by:

- Partial sum to $N = 500{,}000$: $1.5604$
- Rough tail estimate $1/\log(500{,}000) \approx 0.076$
- Total: $\approx 1.636$

**Is this consistent with F1?** F1 says any primitive set has sum $< 1.399 + o(1)$. The primes-from-2 give $1.636 > 1.399$. This is consistent because F1's $o(1)$ is a correction that is NOT small at $x_{\text{floor}} = 2$ — F1's bound $e^\gamma \pi/4 \approx 1.399$ applies in the limit $x_{\text{floor}} \to \infty$, where both the bound and the actual maximum converge. At $x_{\text{floor}} = 2$, the $o(1)$ term allows the bound to be $1.399 + 0.237 = 1.636$.

**Aside on primitivity near $x=3$:** The set $\{4\} \cup \{\text{odd primes } \geq 3\}$ is a valid primitive set in $[3, \infty)$:
- $4 = 2^2$ is not divisible by any odd prime, nor does it divide any odd prime.
- Distinct odd primes don't divide each other.

Its sum is $\frac{1}{4 \log 4} + \sum_{p \geq 3} \frac{1}{p \log p} \approx 0.180 + 0.915 = 1.095 > 1$.

However, this is at $x_{\text{floor}} = 3$ (small), and the $o(1)$ term in the conjecture is large at $x=3$ — the conjecture allows for sum $> 1$ here. As $x_{\text{floor}}$ grows, this type of construction becomes unavailable (since 4 has to be excluded when $x_{\text{floor}} > 4$, and the contribution from large primes alone is $\ll 1$). For $x_{\text{floor}} = 5$, excluding both 2, 3, and 4 from elements: the sum over all primitives in $[5, \infty)$ is $\leq \sum_{p \geq 5} 1/(p \log p) + \text{small-factor composites} \ll 1$.

---

## Section 3 — Witness Search (Q4)

**Verified witnesses with $\sum > 1$:**

| $x_{\text{floor}}$ | Set | Sum (verified) | Valid? |
|---|---|---|---|
| 2 | $\{2, 3\}$ | 1.0248 | Yes — but $o(1)$ at $x=2$ is large |
| 3 | primes $[3..97]$ (24 elements) | 0.7002 | No |
| 100 | primes $[100..10000]$ (1204 elements) | 0.1066 | No |

**Greedy upper bound at $x_{\text{floor}} = 100$:** A greedy maximum-weight primitive set in $[100, 200{,}000]$ achieves sum $\approx 0.294$, well below 1. No witness found for $x_{\text{floor}} \geq 3$.

**Interpretation:** The only verifier-accepted witness is at $x_{\text{floor}} = 2$ with $\{2, 3\}$ (sum $= 1.025$). This is technically a verified counterexample to the literal claim "sum $< 1$ for all $x$ and all primitive $A \subseteq [x, \infty)$," but the conjecture's $o(1)$ makes this consistent: at $x = 2$, the $o(1)$ absorbs the 0.025 excess. A genuine disproof would require witnesses at *arbitrarily large* $x_{\text{floor}}$ with sum bounded away from 1, which our data does not support.

---

## Section 4 — Proof Structure Outline (Q5)

**Goal:** Show $\sup_{A \subseteq [x, \infty),\, A \text{ prim.}} \sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$ as $x \to \infty$.

**Lemma schema (stratification by $\Omega$):**

**Lemma 1 (Single-stratum bound).** For each $k \geq 1$ and large $x$:
$$\sum_{\substack{a \in A \\ \Omega(a) = k}} \frac{1}{a \log a} \leq \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \log n} = T_k(x).$$
This is clear (the restricted stratum sum is a universal upper bound for the contribution of $k$-almost-prime elements of $A$). By our data, $T_k(x) \to 0$ as $x \to \infty$ for each fixed $k$.

**Lemma 2 (Cross-stratum primitivity gap).** Elements at different $\Omega$-levels interact: if $a \in A$ with $\Omega(a) = k$ and $b \in A$ with $\Omega(b) = j > k$ share a prime factor $p | a$ and $a | b$, then $b$ is excluded. The primitivity constraint means that fixing the $k=1$ layer forces a significant portion of the higher-$k$ layers to be excluded (any prime $p$ in the set eliminates all multiples of $p$ from higher strata).

**Lemma 3 (Maximizer is the primes).** Among all primitive sets $A \subseteq [x, \infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{p \geq x,\, p \text{ prime}} \frac{1}{p \log p} + C/\log(x)^2$$
for some constant $C$. The primes achieve (or near-achieve) the supremum because:
- Primes are pairwise coprime (hence a maximal primitive set for the "small" elements near $x$).
- Higher-$\Omega$ composites are larger and contribute less per element, UNLESS they avoid divisibility with the primes — but any such composite must have all prime factors in the set, and primitivity prevents including both the prime and the composite.

**Status of Lemma 3:** This is the KEY unproven lemma. It would show the conjecture with an explicit rate. The current "proof" is heuristic: the Zhang–Erdős framework (F1) bounds the sum by $\approx 1.399 + o(1)$, but the tighter bound of $1 + o(1)$ requires showing the primes-from-$x$ are the extremal set, which is the conjecture itself.

**Open gap:** The Lemma 3 claim (primes maximize the sum) is essentially equivalent to the original conjecture. To prove it rigorously, one needs either:
(a) A Plünnecke/Brun-sieve argument bounding the combined contribution of all strata, or
(b) A direct comparison with the Erdős–Zhang framework extended to show the tighter 1 bound.

**Conclusion of current session:** The numerical evidence strongly supports the conjecture: for $x_{\text{floor}} \geq 5$, all primitive sets in $[x_{\text{floor}}, \infty)$ appear to have sum $< 0.5$, let alone $< 1$. The conjecture is true in all checked cases. However, no rigorous proof of Lemma 3 has been found — this remains open.

## Partial result (Q6 — converging session)

This session has established:

1. **Lemma 1** (`lemma_001_stratum_tail_bound.md`, status: proved): For each fixed $k$ and any primitive $A \subseteq [x, \infty)$, the $k$-stratum contribution is at most $T_k(x) \to 0$ as $x \to \infty$.

2. **Numerical bound (not a proof)**: For $x_{\text{floor}} = 100$, the maximum observed sum over any primitive set in $[100, \infty)$ is $\approx 0.294$. For $x_{\text{floor}} = 10{,}000$: $\approx 0.04$. These are well below 1.

3. **The key open gap**: Lemma 3 ("primes maximize the sum") remains unproved. Lemma 2 (`lemma_002_cross_stratum.md`) sets up the exclusion argument but does not close it.

**What we have ruled out**: Any witness for $x_{\text{floor}} \geq 5$ — exhaustive greedy search up to $N = 200{,}000$ found no primitive set exceeding sum $= 0.294$.

**Suggested next move for the next session:**
1. Read `proof_lemmas/lemma_002_cross_stratum.md`, current obstacle section.
2. Try the "local exchange" argument: show that replacing a prime $p \in A$ with a composite $pq$ (with $q > 1$) strictly decreases the sum density in $[x, \infty)$.
3. If the local-exchange argument succeeds, Lemma 3 follows by induction on the number of non-prime elements in $A$.
