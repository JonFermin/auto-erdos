# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Metadata

- **Claim**: For any primitive $A \subseteq [x,\infty)$, $\sum_{a\in A} 1/(a\log a) < 1+o(1)$.
- **Status**: open (harness enforces; no resolution claim without a verified witness).
- **Given facts**: F1 (Erdős-Zhang UB ≈ 1.399), F2 (Omega-stratum LB, unsigned-O), F3 (exact asym for $A_k$, approaches 1 from below).

## Witness format

A counterexample witness must be embedded as a `<!-- WITNESS ... WITNESS -->`
block at the bottom of this file and pass `library.primitive_set_witness.verify_witness`.

---

## Section 1: Setup (Q1)

### The conjecture

**Erdős's primitive-set conjecture** (tightened form): For any integer
$x \geq 2$ and any **primitive set** $A \subseteq [x, \infty)$ — a set of
integers $\geq x$ in which no element divides another — we have
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
where $o(1) \to 0$ as $x \to \infty$.

Restated: in the limit of large floor $x$, no primitive subset of
$[x, \infty)$ can have a weighted sum $\sum 1/(a \log a)$ exceeding $1$.
The conjecture asserts $1$ is a universal asymptotic upper bound.

This is an **open problem** as of this proof attempt. This file contains
no claim of proof or refutation without a verifier-accepted witness block.

### Given facts with sign notes

**F1 — Erdős-Zhang upper bound** (Erdős 1935; Zhang 1993):
For *any* primitive set $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399.$$

Sign note (UPPER bound): the sum is bounded *above* by $\approx 1.399$.
This is weaker than but consistent with the conjecture (bound of $1+o(1)$).
F1 cannot serve as a lower bound; any argument that reads it as a lower
bound would contradict F1 itself.

**F2 — Omega-stratum lower bound** (given fact F2):
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2+o(1)}\right).$$

Sign note (UNSIGNED big-$O$): The error term $O(k^{-1/2+o(1)})$ is
unsigned — it may be positive or negative. F2 alone does NOT imply
the sum exceeds $1$. Any argument concluding "sum $> 1$" from F2 alone
is a sign error (the ChatGPT failure mode for this problem).

**F3 — Exact asymptotic for $A_k$** (given fact F3):
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$

Sign note (correction is NEGATIVE): Since $c > 0$, the term
$-(c+o(1)) k^2/2^k$ is negative, so the sum is strictly less than $1$
and approaches $1$ from **below** as $k\to\infty$. F3 resolves F2's
ambiguity: the unsigned-$O$ is in fact negative for $A_k$. The canonical
extremal stratum never violates the conjecture.

### Witness contract

A counterexample claim requires a finite primitive set
$A \subseteq [x_\text{floor}, \infty)$ for which
`library.primitive_set_witness.verify_witness` confirms:
1. Every element is $\geq x_\text{floor}$.
2. $A$ is primitive (no element divides another).
3. Rigorous sum $\sum_{a\in A} 1/(a\log a) > 1.0$ (the threshold).

Without a verifier-accepted `<!-- WITNESS -->` block in this file, no
refutation claim may be made. The $o(1)$ caveat in the conjecture means
a witness at finite $x_\text{floor}$ barely exceeding $1$ requires
separate argument that the $o(1)$ slack at that scale is negligible.

### Roadmap

| Round | Q   | Goal |
|-------|-----|------|
| 1     | Q1  | This Setup section (current) |
| 2     | Q2  | Numerical check: truncated sums for $A_k$, $k=1,2,3,4$ |
| 3     | Q3  | Primes sum: approach to $\approx 1.6366$, consistency with F1 |
| 4     | Q4  | Witness search at $x_\text{floor} \in \{100, 1000, 10000\}$ |
| 5+    | Q5  | Proof sketch: Omega-stratification + lemma decomposition |
| final | Q6  | Partial result if full proof is out of reach |
