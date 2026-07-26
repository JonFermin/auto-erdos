---
id: cyclic_orbit_avg_size
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 8
---

# Lemma `cyclic_orbit_avg_size` (cyclic orbit union-closure: average member size ≥ n/2)

**Statement.** Let $A$ be any nonempty subset of $\mathbb{Z}_n$ (integers
mod $n$), $n \ge 2$. Let $\mathcal{F}$ be the union-closure of the cyclic
orbit $\{A, A+1, A+2, \ldots, A+(n-1)\}$ where $A+k = \{a+k \bmod n : a
\in A\}$. Then

$$\frac{1}{|\mathcal{F}|} \sum_{S \in \mathcal{F}} |S| \;\ge\; \frac{n}{2}.$$

**Significance.** For a transitive family (one on which a group acts),
Frankl's union-closed conjecture ("some element appears in $\ge |\mathcal{F}|/2$
sets") is equivalent to avg member size $\ge n/2$ (by the
frequency–size duality: $\sum_e \text{freq}(e) = |\mathcal{F}| \cdot
\text{avg\_size}$, and uniform frequency $f$ gives $n \cdot f = |\mathcal{F}|
\cdot \text{avg\_size}$, so $f \ge |\mathcal{F}|/2$ iff avg\_size $\ge n/2$).
The cyclic orbit generates a transitive family, so this lemma is the Frankl
conjecture restricted to transitive union-closures of cyclic orbits.

## Proof sketch (analytic direction, not yet complete)

Let $A \subset \mathbb{Z}_n$, $|A| = k$. The cyclic orbit $\{A+j : j \in
\mathbb{Z}_n\}$ has exactly $n/\gcd_A$ distinct members (where $\gcd_A$ is
the "period" of $A$, i.e., the smallest positive $d$ such that $A = A+d$).
Its union-closure $\mathcal{F}$ is union-closed and transitive under cyclic
shift.

**Lower bound on avg size**: every set in $\mathcal{F}$ is a union of
cyclic shifts of $A$, hence a subset of $\mathbb{Z}_n$ with size $\ge k$.
The avg size in the orbit is $k$ (all orbit members have size $k$). As we
take unions, sizes increase; $\mathbb{Z}_n$ (size $n$) is always in
$\mathcal{F}$ (union of all shifts). A simple argument:

$$\text{avg\_size} = \frac{1}{|\mathcal{F}|} \sum_{S \in \mathcal{F}} |S|
= \frac{1}{|\mathcal{F}|} \sum_{j \in \mathbb{Z}_n} |\{S \in \mathcal{F}
: j \in S\}| = \text{freq}(j)$$

where the last equality uses transitivity (all frequencies equal). So
avg\_size $\ge n/2$ iff freq$(j) \ge |\mathcal{F}|/2$ for any fixed $j$.

The claim reduces to: in the union-closure of any cyclic orbit, every
element is in at least half the sets. This is a non-trivial claim; the
CHECK establishes it for small $n$ and generators of moderate size.

## CHECK — exhaustive probe at small n

<!-- CHECK
# cyclic_orbit_avg_size: does every union-closure of a cyclic orbit have avg member size >= n/2?
# Equivalently: every element frequency >= |F|/2?
# Exhaustive for n=4..10, generators (A subsets of Z_n) of size 2..min(4,n-1).
# Exit 0 = lemma holds on all tested instances.
from itertools import combinations

def cyclic_orbit(A_tuple, n):
    A = frozenset(A_tuple)
    return frozenset(frozenset((a+k)%n for a in A) for k in range(n))

def union_closure(orbit):
    sets = set(orbit)
    changed = True
    while changed:
        changed = False
        new = set()
        sl = list(sets)
        for i in range(len(sl)):
            for j in range(i, len(sl)):
                u = sl[i] | sl[j]
                if u not in sets:
                    new.add(u); changed = True
        sets |= new
    return sets

def avg_member_size(F):
    if not F: return 0
    return sum(len(s) for s in F) / len(F)

failures = []
for n in range(4, 11):
    for sz in range(2, min(5, n)):
        for A_tuple in combinations(range(n), sz):
            orbit = cyclic_orbit(A_tuple, n)
            F = union_closure(orbit)
            avg = avg_member_size(F)
            if avg < n/2 - 1e-9:
                failures.append((n, A_tuple, avg, n/2))

assert not failures, (
    "cyclic_orbit_avg_size: FALSIFIED for n,A,avg,threshold=" + repr(failures[:3]))
CHECK -->

## Expected outcome

The claim holds for all tested $(n, A)$: the union-closure of any cyclic
orbit has average member size $\ge n/2$. A failure would be an explicit
Frankl counterexample for a transitive cyclic family — which would resolve
Frankl's conjecture negatively, an extraordinary result.

## Connection to Q11 (transitive counterexample screen)

This lemma is the quantitative first step of Q11. If it holds universally,
it says: the transitive cyclic family construction CANNOT yield a Frankl
counterexample. The Q11 program then screens more general transitive
families (dihedral, affine, PSL(2,q)) for counterexamples — this lemma
prunes the cyclic case.

## Status

Hypothesis open pending CHECK. No analytic proof yet; the frequency-duality
reduction is documented above.
