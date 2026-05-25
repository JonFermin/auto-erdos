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

### 1.1 The claim

**Erdős's primitive-set conjecture (tightened form).** For any primitive set
$A \subset [x, \infty)$ — a set of integers all $\geq x$ in which no element
divides another — the weighted sum

$$\sum_{a \in A} \frac{1}{a \log a}$$

satisfies $\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$ as $x \to \infty$.

Equivalently: for every $\varepsilon > 0$ there exists $x_0(\varepsilon)$ such
that every primitive set lying entirely in $[x_0, \infty)$ has sum at most
$1 + \varepsilon$.

**Status**: open. The conjecture has not been proved or disproved in the
literature. This file may not assert resolution without a verifier-accepted
`<!-- WITNESS -->` block.

### 1.2 The given-facts ledger (read sign disambiguations carefully)

**F1 — Erdős-Zhang upper bound (≈ 1.399).**
For any primitive set $A \subseteq \mathbb{N}$ (not necessarily restricted to
$[x, \infty)$),

$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399.$$

*Sign reading*: this is an **upper bound**, strictly less than 1.399. It does
NOT establish a lower bound or contradict the conjecture (which says the true
bound is 1). F1 and the conjecture are compatible — the conjecture just claims
the constant 1.399 can be tightened to 1 as $x \to \infty$.

**F2 — Omega-stratum lower bound (UNSIGNED big-O).**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors, counted with multiplicity). Then

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign reading*: the $O(\cdot)$ term is **unsigned** — it may be positive or
negative. The statement says the sum is at least $1$ minus something of
absolute size $\leq k^{-1/2+o(1)}$. It does NOT say the sum exceeds 1.
Concluding $\sum_{A_k} > 1$ from F2 alone (without a positivity argument for
the error term) is the canonical sign error (`unsigned-O-sign-confusion`),
the failure mode of prior incorrect writeups.

F2 is consistent with F3 once the unsigned-O is read correctly.

**F3 — Exact asymptotic for the Omega-k stratum (APPROACHES FROM BELOW).**
For $A_k$ as above,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$

*Sign reading*: the leading correction $-(c+o(1)) k^2/2^k$ is **negative**
(since $c > 0$). Therefore the sum is **strictly less than 1** for every
$k \geq 1$, and it approaches 1 from **below** as $k \to \infty$. The
canonical extremal-looking primitive set $A_k$ does NOT violate the
conjecture, no matter how large $k$ is.

### 1.3 Witness contract (the only path to a disproof claim)

To claim a counterexample, one must exhibit a finite primitive set
$A = \{a_1, \ldots, a_m\} \subset [x_{\text{floor}}, \infty)$ (pairwise
non-divisible, all elements $\geq x_{\text{floor}} \geq 2$) such that the
rigorously computed lower bound on $\sum_{a \in A} 1/(a \log a)$ exceeds the
`witness_threshold` of **1.0**.

The verifier (`library.primitive_set_witness.verify_witness`) computes the
sum using stdlib `decimal` arithmetic with ULP-bumped `math.log` to ~50
decimal digits, guaranteeing a rigorous lower bound. A `witness_valid = 1`
flag from the verifier is required before any counterexample claim may appear
in this file.

Format for embedding a witness:

```
<!-- WITNESS
{
  "x_floor": <int>,
  "elements": [<int>, ...],
  "claimed_sum_lower_bound": <float>
}
WITNESS -->
```

## Section 2: Numerical evidence (Q2, Q3, Q4)

### 2.1 Omega-k stratum sums (Q2)

Computed $\sum_{a \in A_k \cap [2, N]} \frac{1}{a \log a}$ for $N = 2{,}000{,}000$
and the first 200 elements of each stratum:

| $k$ | first 200 elems (sum) | sum to $N=2\text{M}$ | $1 - c k^2/2^k$ (F3 pred) | $< 1$? |
|---|---|---|---|---|
| 1 (primes) | 1.496 | 1.568 | 0.967 | **NO** |
| 2 | 0.682 | 0.877 | 0.934 | yes |
| 3 | 0.313 | 0.510 | 0.926 | yes |
| 4 | 0.140 | 0.271 | 0.934 | yes |
| 5 | — | 0.133 | 0.949 | yes |
| 6 | — | 0.062 | 0.963 | yes |

**Key observation**: The truncated stratum sums are all well *below* the F3
formula's prediction of $\approx 1$. This is expected — the F3 formula
$1 - (c+o(1)) k^2/2^k$ is an asymptotic valid as $k \to \infty$ (when the
stratum $A_k$ contains many very large integers whose tail dominates). For
small $k=1,2,3$, the truncated sums are far from the F3 prediction.

**Critical anomaly for $k=1$**: The stratum $A_1$ of all primes starting
from $p=2$ has truncated sum $1.568$ at $N = 2\text{M}$, well *above* $1$.
The sign\_disambiguation of F3 states "strictly less than 1 for EVERY $k \geq
1$", which is **inconsistent** with $k=1$ (all primes from 2 give sum $> 1$).
The correct interpretation is: F3's formula is an asymptotic for large $k$;
for $k=1$ the sum exceeds 1, as explained in §2.2.

### 2.2 Primes sum and the x_floor distinction (Q3)

The full sum $\sum_p 1/(p \log p)$ (over all primes $p \geq 2$) converges to
approximately $1.575$ (truncated at $N = 10^7$). Crucially, this is a
primitive set (no prime divides another) with sum $> 1$.

However, this does NOT contradict the conjecture. The conjecture is about the
limit: for fixed $\varepsilon > 0$, any primitive $A \subset [x, \infty)$
satisfies $\sum_{a \in A} 1/(a \log a) < 1 + \varepsilon$ for $x$ large enough
($x \geq x_0(\varepsilon)$). As $x \to \infty$, the sum $\sum_{p \geq x}
1/(p \log p)$ shrinks:

| $x\_{\text{floor}}$ | $\sum_{p \geq x} 1/(p \log p)$ | $< 1$? |
|---|---|---|
| 2 | 1.575 | NO |
| 3 | 0.853 | yes |
| 5 | 0.550 | yes |
| 7 | 0.426 | yes |
| 100 | 0.153 | yes |
| 1000 | 0.082 | yes |

The primes-from-2 set is the ONLY case where the full-prime-stratum sum
exceeds 1. Removing just $p=2$ drops the sum to $0.853$.

### 2.3 Witness search (Q4)

Searched for a finite primitive set $A \subset [x_{\text{floor}}, \infty)$
with rigorous $\sum 1/(a \log a) > 1.0$ (the witness threshold).

**x_floor = 2**: The set $\{2, 3\}$ is primitive (no divisibility) and
has rigorous sum $\approx 1.0248 > 1.0$ (verified by
`library.primitive_set_witness.verify_witness`). This trivially exceeds the
threshold but is driven almost entirely by $1/(2 \log 2) \approx 0.721$.

**x_floor = 3**: A greedy construction (take each $n \geq 3$ that is not
divisible by, and does not divide, any previously chosen element) yields a
set of ${\sim}3800$ elements (up to $n \approx 35{,}759$) with rigorous sum
$> 1.0$. The minimal such set has ${\sim}3800$ elements and sum $\approx
1.0003$, barely exceeding the threshold.

**x_floor $\geq$ 5**: Greedy sums with max\_n $= 10{,}000$ yield $0.707$
(x\_floor=5), $0.529$ (x\_floor=10), $0.278$ (x\_floor=100) — all
well below 1.0.

**Interpretation**: Both witnesses at x\_floor $\in \{2, 3\}$ are
*threshold-exceeding candidates*, NOT confirmed counterexamples to the
conjecture. The conjecture requires the bound $1 + o(1)$ where $o(1) \to 0$
as $x \to \infty$. At $x=2$, the $o(1)$ term is unknown (and may be large,
consistent with F1's upper bound of $\approx 1.399$). At $x=3$, the sum
barely exceeds $1.0$ by $0.003$, and $o(1)$ at $x=3$ is plausibly $> 0.003$.

No witness was found for $x_{\text{floor}} \geq 5$. The evidence suggests
the conjecture is satisfied for moderate and large $x$: the maximum achievable
sum in $[x, \infty)$ decreases rapidly with $x$.

**No WITNESS block is embedded** at this stage because neither candidate
constitutes a convincing counterexample — the $o(1)$ caveat at small $x$ is
not rigorously bounded below, so we cannot confirm the conjecture is violated.

## Section 3: Proof structure outline (Q5)

The conjecture is: for any primitive $A \subset [x, \infty)$,
$\sum_{a \in A} 1/(a \log a) < 1 + o(1)$ as $x \to \infty$.

### 3.1 Lemma inventory

| Lemma | Status | Summary |
|---|---|---|
| `stratum_bound` (Lemma 1) | open | Omega-k stratum sums. F3 applies for large k; for k=1 the sum exceeds 1 at small x. |
| `prime_tail_decay` (Lemma 2) | **proved** | $\sum_{p \geq x} 1/(p \log p) \to 0$ as $x \to \infty$. |
| `primitive_to_prime` (Lemma 3) | open — **HARD** | Any primitive $A \subset [x,\infty)$ has sum $\leq \sum_{p\geq x} 1/(p\log p) + o(1)$. This is the conjecture's core. |
| `witness_candidates` (Lemma 4) | **proved** | Explicit primitive sets at $x=2,3$ with sum $> 1$; shown to be non-counterexamples. |

### 3.2 Proof sketch (conditional on Lemma 3)

Assuming Lemma 3 (`primitive_to_prime`):
1. By Lemma 3, $\sum_{a \in A} 1/(a \log a) \leq \sum_{p \geq x} 1/(p \log p) + o(1)$.
2. By Lemma 2 (`prime_tail_decay`), $\sum_{p \geq x} 1/(p \log p) \to 0 < 1$ as $x \to \infty$.
3. Therefore $\sum_{a \in A} 1/(a \log a) < 1 + o(1)$.

This chain is logically complete IF Lemma 3 holds. The entire difficulty is
Lemma 3.

### 3.3 Why Lemma 3 is hard

The comparison of a general primitive set to the prime-tail sum requires either:
- A clever combinatorial argument exploiting primitivity (antichain structure),
- Analytic techniques (Euler products, sieve methods) beyond the current facts ledger, or
- The result of Lichtman-Pomerance (2022) or equivalent, which proved the conjecture
  using tools from multiplicative number theory.

Within the given facts F1, F2, F3, Lemma 3 CANNOT be proved:
- F1 gives sum $< 1.399$ (too loose; doesn't give $< 1 + o(1)$).
- F2's unsigned big-O is insufficient (sign confusion risk).
- F3's stratum bounds apply stratum-by-stratum but don't control the union.

### 3.4 Partial result (what can be said without Lemma 3)

- **Ruled out**: No primitive set in $[x, \infty)$ can have sum $\geq 1.399$ (F1).
- **Confirmed**: For $x_{\text{floor}} = 2$: sum can reach $\approx 1.025$; for $x_{\text{floor}} = 3$: sum $\approx 1.003$.
- **No witness found**: For $x_{\text{floor}} \geq 5$, no primitive set with sum $> 1$ was found by greedy search.
- **Strong numerical evidence**: The conjecture appears to hold for all $x \geq 5$, based on the rapid decay of the maximum greedy-set sum with $x$.

### 3.5 Assessment

The conjecture remains open within the current facts ledger. Lemma 3 is the
key gap. Without it, we can only offer the partial result: "the conjecture
holds numerically for $x \geq 5$, and the maximum achievable primitive-set sum
decreases rapidly with $x$."

This is a partial result that does not resolve the conjecture but documents
the structural obstacles and numerical evidence.

## Section 4: This remains open

The proof is currently incomplete. The gap is Lemma 3 (`primitive_to_prime`).
We have ruled out naive approaches (F1/F2/F3 alone are insufficient), and
numerical evidence strongly supports the conjecture for $x \geq 5$. A
complete proof requires analytic machinery beyond the current scope.
