---
id: p1_lichtman
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 1
---

# Lemma P1 — Primes maximize primitive-set sums

## Statement

For any $x \geq 2$ and any primitive set $A \subset [x, \infty)$:

$$S(A) = \sum_{a \in A} \frac{1}{a \log a} \leq \sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p}.$$

Equality is achieved by $A = \{p : p \geq x, p \text{ prime}\}$.

## Status

**Open** — a fully self-contained proof requires reproving Lichtman (2022).
What follows is a detailed sketch that identifies every gap.

**External reference:** Jared Duker Lichtman, *On a conjecture of Erdős about
primitive sets,* Proc. AMS 150(3):1025–1031, 2022.

## Proof strategy (Erdős–Zhang weight redistribution)

The idea, due to Erdős (1935) and sharpened by Zhang (1993) and Lichtman (2022),
is to redistribute each term $1/(a \log a)$ of $S(A)$ to a sum over primes
$p \geq x$, so that the redistributed mass at each prime $p$ is at most
$1/(p \log p)$. Summing over primes then gives the bound.

### Setup: Fundamental identity

For any integer $n \geq 2$ and any prime $p \mid n$, define:

$$f(n, p) = \frac{1}{n \log n} \cdot \frac{1/p}{\sum_{q \mid n} 1/q},$$

where the denominator sums over all prime factors $q$ of $n$ (without multiplicity).
By construction $\sum_{p \mid n} f(n, p) = 1/(n \log n)$.

### Key estimate (the heart of Lichtman's argument)

**Claim A:** For each prime $p$,

$$\sum_{\substack{n \geq x \\ p \mid n}} f(n, p) \leq \frac{1}{p \log p}.$$

If Claim A holds, then for any set $A \subset [x, \infty)$ (primitive or not):

$$S(A) = \sum_{a \in A} \frac{1}{a \log a} = \sum_{a \in A} \sum_{p \mid a} f(a, p)
\leq \sum_{p \geq x} \sum_{\substack{a \in A \\ p \mid a}} f(a, p)
\leq \sum_{p \geq x} \frac{1}{p \log p}.$$

The primitivity of $A$ is not used here — the bound would hold for any $A \subset [x, \infty)$.

### Why Claim A is insufficient

The redistribution $f(n, p)$ as defined above does NOT satisfy Claim A for
general $n \geq x$ — the sum over all multiples of $p$ in $[x, \infty)$ can exceed
$1/(p \log p)$. The Erdős–Zhang bound $S(A) < e^\gamma \pi/4 + o(1)$ (F1) comes
from a different weight where Claim A is replaced by a global bound using
partial summation and Mertens' theorem.

### Lichtman's actual argument

Lichtman uses a more refined weight. The key innovation is:

**For each prime $p \geq x$ and each primitive set $A \subset [x, \infty)$,**
the elements of $A$ divisible by $p$ form a set $B_p = \{a \in A : p \mid a\}$,
and $B_p / p = \{a/p : a \in B_p\}$ is ALSO a primitive set (since if $p \mid a$
and $a \mid b$ with $a, b \in A$, then $a/p \mid b/p$, and primitivity of $A$
excludes this).

**Step 1.** For each prime $p$, define the "p-contribution" of $A$ as:
$$C_p(A) = \sum_{a \in A, p \mid a} \frac{1}{a \log a}.$$

**Step 2.** Show $C_p(A) \leq 1/(p \log p)$ using:
- $B_p/p$ is a primitive set in $[x/p, \infty) \subset [1, \infty)$.
- Apply F1 (Erdős–Zhang) to $B_p / p$: $\sum_{b \in B_p/p} 1/(b \log b) < e^\gamma \pi/4 + o(1)$.
- Translate back: $C_p(A) = \sum_{a \in B_p} 1/(a \log a) = \sum_{b \in B_p/p} 1/((bp) \log(bp))$.

The translation from $1/(b \log b)$ to $1/((bp) \log(bp))$ needs the factor
$b \log b / (bp \log(bp))$, which requires a delicate estimate relating
$\log(bp)$ to $\log b + \log p$.

**Step 3.** The diagonalization. Actually, Lichtman's proof does NOT proceed via
Step 2 directly — using F1 at each prime gives a bound of $e^\gamma \pi/4$, not 1.
The sharp bound of 1 (the prime-sum value) requires a different argument.

Lichtman's actual proof uses an induction/recursion on the structure of the
primitive set, combined with the following key lemma from his paper:

**Lichtman's Key Lemma:** For any $x \geq 2$ and primitive $A \subset [x, \infty)$,

$$S(A) \leq S(P(x)) := \sum_{p \geq x} \frac{1}{p \log p},$$

where $P(x) = \{p : p \geq x, p \text{ prime}\}$.

*Proof idea (Lichtman):* By induction on the "complexity" of $A$. The base case
$A \subset \{x\}$ is trivial. The key inductive step: if $A$ contains a composite
element $n = p \cdot m$ (with $p$ the smallest prime factor of $n$), replace $n$
in $A$ by all prime factors of $n$ in $[x, \infty)$. Show this replacement does
not decrease the sum (using the inequality $1/(n \log n) \leq \sum_{p | n} 1/(p \log p) \cdot (\text{weight})$).
Iterate until $A$ consists only of primes — obtaining $P(x)$.

The formal version of this "greedy replacement" argument is the core of Lichtman's
paper. The key inequality needed is:

$$\frac{1}{n \log n} \leq \frac{1}{\text{(some combination of prime terms)}},$$

which Lichtman proves using the concavity of $\log$ and the AM-GM inequality for the
prime factorization of $n$.

### Current obstacle

To complete a self-contained proof, we need to:

1. Make Lichtman's "greedy replacement" rigorous: define the replacement precisely
   and verify it (a) preserves primitivity and (b) does not decrease $S$.

2. Establish the key inequality: for any $n$ with smallest prime factor $p$,
   $$\frac{1}{n \log n} \leq \frac{1}{p \log p} - \frac{1}{(n/p) \log(n/p)}.$$
   If true, replacing $n$ by $\{p\} \cup (A \setminus \{n\})$ and adding $n/p$ to a
   separate pile eventually yields the prime set.

   **Status:** This inequality is FALSE in general ($n = 4$, $p = 2$: LHS $= 1/(4 \log 4) \approx 0.180$; $1/(2 \log 2) - 1/(2 \log 2) = 0$). So the naive greedy replacement does not work.

3. Alternatively, use the "Euler product / Dirichlet series" approach that Lichtman
   actually uses in the paper: expressing $S(A)$ as a special value of a Dirichlet
   series and bounding it using properties of primitive sets in that formalism.

**Next move:** Try the following weaker-but-tractable version of Lemma P1:

**Weak P1:** For $x \geq 3$ and any primitive $A \subset [x, \infty)$, $S(A) < 1$.

*Proof idea:* Use the fact (proved in Lemma P3) that $S(P(3)) < 1$, and note that
any primitive set in $[3, \infty)$ has $S(A) \leq S(P(3)) < 1$ IF Lemma P1 holds.
This is circular — but if we can prove Weak P1 DIRECTLY (e.g. by the Erdős–Zhang
bound F1 noting that $e^\gamma \pi/4 \approx 1.399$ is not tight enough, and by
directly bounding $S(A) \leq 1/(3 \log 3) + 1/(5 \log 5) + \ldots$), this would suffice.

Actually, F1 gives $S(A) < 1.399$ for any primitive set. This does NOT imply $< 1$
for $x \geq 3$. A tighter bound is needed.

**Alternative path (Mertens product approach):** For a primitive $A \subset [x, \infty)$,
bound $S(A)$ using the Mertens product $\prod_{p \leq x} (1 - 1/p)^{-1} \sim e^\gamma \log x$.
This gives $S(A) \leq \sum_{n \geq x} 1/(n \log n) \cdot [\text{correction}]$, and by
comparison with the prime sum, one can attempt to bound $S(A) \leq$ prime-sum.

This approach requires more work. Leaving as the central open sub-problem for the
next session.
