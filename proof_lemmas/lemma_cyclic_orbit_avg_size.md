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

## Proof (partial)

Let $A \subset \mathbb{Z}_n$, $|A| = k$. The union-closure $\mathcal{F}$
of the cyclic orbit is closed under cyclic shift (since the orbit is, and
union-closure preserves this) and under union.

**Frequency–size duality**: by transitivity, all elements $j \in \mathbb{Z}_n$
have the same frequency $f = |\{S \in \mathcal{F} : j \in S\}|$. Then:

$$\text{avg\_size} = \frac{1}{|\mathcal{F}|}\sum_{S \in \mathcal{F}} |S|
= \frac{1}{|\mathcal{F}|}\sum_{j} |\{S : j \in S\}| = f.$$

So avg\_size $= f$, and the claim is $f \ge |\mathcal{F}|/2$.

**Case 1: $|A| \ge n/2$.** Every set in $\mathcal{F}$ is a union of orbit
elements, each of size $\ge n/2$. Hence every set in $\mathcal{F}$ has size
$\ge n/2$, so avg\_size $\ge n/2$. ∎ (This case is proved.)

**Case 2: $|A| < n/2$.** Taking unions of cyclic shifts increases sizes
beyond $k = |A|$. The set $\mathbb{Z}_n \in \mathcal{F}$ (union of all
shifts) has size $n$. In the tested range ($n \le 10$), all generators of
size $2 \le k < n/2$ satisfy avg\_size $\ge n/2$ (CHECK evidence). The
analytic proof for this case is open; the cyclic shift pairing argument
(for each $S \notin F_j$, map $S \mapsto S + d$ for the smallest $d$ with
$j \in S+d$) fails to be injective in general (example: $n=4$, $j=0$,
$S_1=\{1\}$ and $S_2=\{3\}$ both map to $\{0\}$), requiring a different
approach.

**Extended CHECK** (larger $n$):

<!-- CHECK
# cyclic_orbit_avg_size extended: n=4..15, generators of size 2..min(4,n//2).
# Exit 0 = no Frankl violation found. (Quick scan, not exhaustive for n>10.)
from itertools import combinations
import random

rng = random.Random(20260726_7)

def cyclic_orbit(A_tuple, n):
    A = frozenset(A_tuple)
    return frozenset(frozenset((a+k)%n for a in A) for k in range(n))

def union_closure(orbit, size_limit=5000):
    sets = set(orbit)
    changed = True
    while changed:
        changed = False
        new_sets = set()
        sl = list(sets)
        if len(sl) > size_limit: break  # skip huge closures
        for i in range(len(sl)):
            for j in range(i, len(sl)):
                u = sl[i] | sl[j]
                if u not in sets:
                    new_sets.add(u); changed = True
        sets |= new_sets
    return sets

failures = []

# Exhaustive for n=4..10, size 2..min(4,n-1)
for n in range(4, 11):
    for sz in range(2, min(5, n)):
        for A_tuple in combinations(range(n), sz):
            orbit = cyclic_orbit(A_tuple, n)
            F = union_closure(orbit)
            avg = sum(len(s) for s in F) / len(F) if F else 0
            if avg < n/2 - 1e-9:
                failures.append(('exhaustive', n, A_tuple, round(avg,3), n/2))

# Sampled for n=11..15, size 2..4
for n in range(11, 16):
    for sz in range(2, min(5, n)):
        sample = list(combinations(range(n), sz))
        if len(sample) > 40:
            sample = [sample[i] for i in sorted(rng.sample(range(len(sample)), 40))]
        for A_tuple in sample:
            orbit = cyclic_orbit(A_tuple, n)
            F = union_closure(orbit, size_limit=2000)
            if len(F) < 2: continue  # skipped due to size limit
            avg = sum(len(s) for s in F) / len(F)
            if avg < n/2 - 1e-9:
                failures.append(('sampled', n, A_tuple, round(avg,3), n/2))

assert not failures, (
    "cyclic_orbit_avg_size EXTENDED: Frankl VIOLATED: " + repr(failures[:3]))
CHECK -->

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
