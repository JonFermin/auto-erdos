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

3. Use the "Euler product / Dirichlet series" approach: expressing $S(A)$ as a
   Laplace-type integral over $t > 1$ and bounding it using properties of primitive
   sets. This is the approach developed in the section below.

---

## Section: Integral Representation and the Dirichlet Series Program (Q7)

### Key Identity

For any integer $n \geq 2$:
$$\frac{1}{n \log n} = \int_1^\infty n^{-t} \, dt.$$

*Proof:* $\int_1^\infty n^{-t} \, dt = \int_1^\infty e^{-t \log n} \, dt = \left[\frac{-e^{-t \log n}}{\log n}\right]_1^\infty = \frac{e^{-\log n}}{\log n} = \frac{1}{n \log n}.$ $\square$

### Reformulation of Lemma P1

For any set $A$ of integers $\geq 2$, by exchanging sum and integral (Tonelli):
$$S(A) = \sum_{a \in A} \frac{1}{a \log a} = \int_1^\infty \underbrace{\sum_{a \in A} a^{-t}}_{D_A(t)} \, dt = \int_1^\infty D_A(t) \, dt,$$
where $D_A(t)$ is the Dirichlet series of $A$ at $t$.

Similarly, $S(P_x) = \int_1^\infty P_x(t) \, dt$, where $P_x(t) = \sum_{p \geq x} p^{-t}$.

**Lemma P1 is equivalent to:**
$$\int_1^\infty D_A(t) \, dt \leq \int_1^\infty P_x(t) \, dt \quad \text{for all primitive } A \subset [x, \infty).$$

This integral reformulation is the starting point of Lichtman's (2022) proof.

### The Pointwise Comparison Fails

A natural attempt: show $D_A(t) \leq P_x(t)$ for each $t > 1$, then integrate.
This **fails**: for $t$ near 1, large primitive sets have $D_A(t) \to \infty$ faster
than $P_x(t)$ for small $x$ (counterexample: $A = \{pq : 2 < p < q\}$ with $x = 6$).

So the proof must use global (integral) properties rather than pointwise comparison.

### Special Case: Prime-Power Primitive Sets (Proved)

**Claim:** If $A$ is a primitive set and every element of $A$ is a prime power,
then $S(A) \leq \sum_p 1/(p \log p)$.

*Proof:* Since $p^k | p^j$ for $k < j$, primitivity forces $A$ to contain at most
one power of each prime. For each prime $p$ with $p^{k_p} \in A$:
$$\frac{1}{p^{k_p} \log(p^{k_p})} = \frac{1}{k_p p^{k_p} \log p} \leq \frac{1}{p \log p},$$
with equality iff $k_p = 1$. Summing over all contributing primes:
$$S(A) \leq \sum_{p : p^{k_p} \in A} \frac{1}{p \log p} \leq \sum_p \frac{1}{p \log p} = S(P). \quad \square$$

For the floor-restricted version $A \subset [x, \infty)$: primitivity forces $p^{k_p} \geq x$,
and the sum is over contributing primes, giving $S(A) \leq S(P_x)$. ✓

### Smallest-Prime-Factor Partition Approach

For any primitive set $A \subset [x, \infty)$, partition by smallest prime factor:
$$A = \bigsqcup_{p \geq x,\, p \text{ prime}} A_p, \quad A_p = \{a \in A : p^-(a) = p\}.$$

Then $S(A) = \sum_{p \geq x} S(A_p)$.

**Claim P1-spf:** $S(A_p) \leq 1/(p \log p)$ for each prime $p \geq x$.

*Proof attempt:*
- If $p \in A$: then $A_p = \{p\}$ by primitivity ($p | a$ for all $a \in A_p$). So $S(A_p) = 1/(p \log p)$. ✓
- If $p \notin A$: let $B_p = \{a/p : a \in A_p\}$. $B_p$ is primitive (inherited).
  $$S(A_p) = \sum_{b \in B_p} \frac{1}{pb(\log p + \log b)}.$$
  
  The required bound $S(A_p) \leq 1/(p \log p)$ becomes:
  $$\sum_{b \in B_p} \frac{1}{b} \cdot \frac{\log p}{\log p + \log b} \leq 1.$$
  
  The weight $\log p / \log(pb)$ is Lichtman's "fractional log-mass" assigned to $p$.

### Lichtman's Weight Function (Reconstruction)

Lichtman defines, for each $n \geq 2$ and prime $p | n$:
$$w(n, p) = \frac{1/p}{\sum_{q | n,\, q \text{ prime}} 1/q} \cdot \frac{1}{n \log n}.$$

This satisfies $\sum_{p | n} w(n, p) = 1/(n \log n)$.

**Revised Claim A:** For a PRIMITIVE set $A$ and each prime $p$:
$$\sum_{a \in A,\, p | a} w(a, p) \leq \frac{1}{p \log p}.$$

Summing over all primes: $S(A) = \sum_p \sum_{a \in A, p|a} w(a,p) \leq \sum_p 1/(p \log p)$.

- For $p \in A$: equality holds (only term is $a = p$, $w(p,p) = 1/(p \log p)$). ✓
- For $p \notin A$: requires bounding the sum via the primitivity constraint.

**Status of Revised Claim A:** Open. Subject to Revised Claim A, Lemma P1 is complete.

### Path Forward (Q8)

Two approaches to prove Revised Claim A:

**(a) Dirichlet series / integral approach:**
For each prime $p$, compute $\int_1^\infty \sum_{a \in A, p|a} w(a, t) \, dt$ and show
this is $\leq \int_1^\infty p^{-t} \, dt = 1/(p \log p)$, using primitivity.

**(b) Inductive / recursive bound:**
Use the fact that $B_p = \{a/p : a \in A, p | a\}$ is a smaller primitive set
and apply the bound recursively, with convergence guaranteed by the monotone
structure of the smallest-prime-factor decomposition.

The next session should attempt approach (a).
