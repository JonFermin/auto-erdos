---
id: dihedral_orbit_avg_size
status: open
depends_on: [cyclic_orbit_avg_size]
discharged_by_round: null
introduced_at_round: 9
---

# Lemma `dihedral_orbit_avg_size` (dihedral orbit union-closure: Frankl for D_n)

**Statement.** Let $D_n$ be the dihedral group of order $2n$ acting on
$[n] = \{0, 1, \ldots, n-1\}$ (rotations $r_k: i \mapsto i+k \bmod n$
and reflections $s: i \mapsto -i \bmod n$). For any nonempty $A \subset
[n]$, let $\mathcal{F}$ be the union-closure of the $D_n$-orbit of $A$:

$$\text{Orbit}_{D_n}(A) = \{r_k(A) : k \in \mathbb{Z}_n\} \cup \{s \circ r_k(A) : k \in \mathbb{Z}_n\}.$$

**Claim.** avg member size of $\mathcal{F} \ge n/2$.

## Relationship to `cyclic_orbit_avg_size`

The $D_n$-orbit is a union of two cyclic orbits: the orbit under rotations
(= cyclic orbit of $A$) and the orbit under reflections-then-rotations
(= cyclic orbit of $s(A) = \{-i \bmod n : i \in A\}$). The union-closure
of the $D_n$-orbit is the union-closure of both cyclic orbits combined.

Since union-closure is monotone (adding more generators can only enlarge
$\mathcal{F}$ and increase average sizes by adding larger sets), the
dihedral claim is not stronger than the cyclic claim: adding the reflected
orbit to the generator set doesn't decrease avg size.

However, the $D_n$-orbit may have fewer distinct elements than $2n$ if $A$
is "palindromic" (i.e., $s(A) = r_k(A)$ for some $k$), so the family
structure is nontrivial.

## CHECK — exhaustive probe at small n

<!-- CHECK
# dihedral_orbit_avg_size: union-closure of D_n orbit has avg member size >= n/2?
# D_n acts on {0,...,n-1} by rotations (i->i+k mod n) and reflections (i->-i mod n).
# Exhaustive for n=4..10, generators A of size 2..min(4,n-1).
from itertools import combinations

def dihedral_orbit(A_tuple, n):
    A = frozenset(A_tuple)
    orbit = set()
    for k in range(n):
        orbit.add(frozenset((a+k)%n for a in A))    # rotation
        orbit.add(frozenset((-a+k)%n for a in A))   # reflection then rotation
    return frozenset(orbit)

def union_closure(orbit):
    sets = set(orbit)
    changed = True
    while changed:
        changed = False
        new_sets = set()
        sl = list(sets)
        for i in range(len(sl)):
            for j in range(i, len(sl)):
                u = sl[i] | sl[j]
                if u not in sets:
                    new_sets.add(u); changed = True
        sets |= new_sets
    return sets

def avg_member_size(F, n_universe):
    if not F: return 0
    return sum(len(s) for s in F) / len(F)

failures = []
for n in range(4, 11):
    for sz in range(2, min(5, n)):
        for A_tuple in combinations(range(n), sz):
            orbit = dihedral_orbit(A_tuple, n)
            F = union_closure(orbit)
            avg = avg_member_size(F, n)
            if avg < n/2 - 1e-9:
                failures.append((n, A_tuple, avg, n/2))

assert not failures, (
    "dihedral_orbit_avg_size: FRANKL CONJECTURE FAILED for D_n orbit: "
    "(n, A, avg, threshold)=" + repr(failures[:3]))
CHECK -->

## Analytic status

The dihedral case reduces to the cyclic case: the $D_n$ orbit is the union
of two cyclic orbits (orbit of $A$ and orbit of $\text{Reflect}(A)$). Their
union-closure contains both cyclic union-closures, so avg size is weakly
larger than for either cyclic closure alone.

**Open**: prove avg size $\ge n/2$ analytically for the dihedral case.

## Affine groups (next step)

After the dihedral case, screen $\text{AGL}(1, q)$ (affine group of the
line over $\mathbb{F}_q$) and $\text{PSL}(2, q)$ orbits, as described in
Q11's summary. These groups are larger and generate denser orbits. The same
CHECK structure applies; the union-closure computation may be slower for
large $q$.

## Status

Hypothesis open pending CHECK. Connected to Q11's transitive counterexample
screen: if dihedral union-closures always satisfy avg $\ge n/2$, the search
for Frankl counterexamples must go beyond dihedral generators.
