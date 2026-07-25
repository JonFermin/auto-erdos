---
id: frankl_deficiency
status: open
depends_on: []
discharged_by_round: ~
introduced_at_round: 3
---

# Lemma: KL union-deficiency lower bound (Q10 first lemma)

**Statement.** Let $\mathcal{F}$ be a finite union-closed family with $|\mathcal{F}| \ge 2$
(so it contains at least two distinct sets, and the empty set may or may not be present).
Let $A, B$ be drawn independently and uniformly at random from $\mathcal{F}$.
Define the **union entropy** $H = H(A \cup B)$ (Shannon entropy in bits of the
distribution of $A \cup B$ over $\mathcal{F}$, which is well-defined because
$\mathcal{F}$ is union-closed), and let
$$p = \max_{x} \Pr[x \in A] = \max_{x} \frac{|\{S \in \mathcal{F} : x \in S\}|}{|\mathcal{F}|}$$
be the maximum element frequency.  Then
$$\log_2 |\mathcal{F}| - H(A \cup B) \;\ge\; \frac{(1 - p)^2}{4}.$$

**Why this matters for the Frankl conjecture.** The standard Frankl conjecture
asks whether $p \ge 1/2$ for every union-closed family with $|\mathcal{F}| \ge 2$.
The Chase–Lovett 2020 approach (and the Gilmer 2022 breakthrough at $p \ge 0.01$)
both work through information-theoretic inequalities on $H(A \cup B)$.  The
bound above — if provable — provides a *quantitative* KL deficiency: the
distribution of $A \cup B$ is bounded away from uniform on $\mathcal{F}$ by
at least $(1-p)^2/4$ bits of KL divergence.  This is *stronger* than the
Chase–Lovett barrier direction (which shows the 1/2 bound is tight for their
linearised functional) because it is exact rather than approximate.

Proof direction: the natural approach is to show
$$\sum_{C \in \mathcal{F}} \Pr[A \cup B = C] \log_2 \frac{\Pr[A \cup B = C]}{1/|\mathcal{F}|} \ge \frac{(1-p)^2}{4}$$
using the structure of union-closed families.  A concrete inequality-chain
attempt: let $U = A \cup B$.  For any fixed $C$, $\Pr[U = C] \ge
\Pr[A = C, B = C] = 1/|\mathcal{F}|^2$, but also $\Pr[U = C] \le
\Pr[A = C \text{ or } B = C] \le 2/|\mathcal{F}|$, so the distribution is not
too concentrated.  The KL divergence lower bound must somehow use the
union-closure and the element-frequency constraint.

**Limitation (documented pre-proof).** The numerical CHECK below tests the
inequality exhaustively on all union-closed families of small ground set size
($|U| \le 4$, exhaustive) and on random union-closed families of larger ground
sets.  Because Frankl's conjecture is KNOWN to hold for small families (it was
verified for $|U| \le 11$ by Bosnjak–Marić 2008 and extended further by
computer), every tested family automatically has some element with $p \ge 1/2$.
The adversarial case — a family with $p \in [0.382, 0.5)$ that would stress the
bound — is unreachable for small $n$.  The CHECK therefore only validates the
"safe" regime ($p \ge 0.5$) and cannot witness a failure in the adversarial zone.
This limitation is recorded; a proof cannot rely on the CHECK alone.

---

<!-- CHECK
# Q10 first-lemma: KL union-deficiency CHECK
# Tests: log2|F| - H(A union B) >= (1-p)**2/4
# for all union-closed families in three test suites.
# A non-zero exit means the inequality was VIOLATED on some family.
import math, random, itertools

def is_union_closed(F):
    Fs = frozenset(F)
    for A in Fs:
        for B in Fs:
            if (A | B) not in Fs:
                return False
    return True

def union_entropy(F):
    n = len(F)
    counts = {}
    for A in F:
        for B in F:
            C = A | B
            counts[C] = counts.get(C, 0) + 1
    total = n * n
    H = 0.0
    for cnt in counts.values():
        if cnt > 0:
            p = cnt / total
            H -= p * math.log2(p)
    return H

def max_freq(F, universe):
    n = len(F)
    best = 0
    for x in universe:
        cnt = sum(1 for S in F if x in S)
        if cnt > best:
            best = cnt
    return best / n

def check_ineq(F, universe):
    if len(F) < 2:
        return True
    log2_n = math.log2(len(F))
    H = union_entropy(F)
    p = max_freq(F, universe)
    lhs = log2_n - H
    rhs = (1 - p) ** 2 / 4
    return lhs >= rhs - 1e-9

# Suite 1: all union-closed families on ground set {0,1,2,3} containing
# the empty set (equivalently: sub-lattices of 2^{0,1,2,3}).
violations = 0
universe4 = list(range(4))
elems4 = [frozenset(S) for S in itertools.chain.from_iterable(
    itertools.combinations(universe4, r) for r in range(5))]

for size in range(2, len(elems4) + 1):
    for subset in itertools.combinations(elems4, size):
        if is_union_closed(subset):
            if not check_ineq(list(subset), universe4):
                violations += 1

# Suite 2: power sets 2^U for |U| = 1..7 (union-closed, p=1/2 for all
# non-empty U, so these are boundary cases).
for k in range(1, 8):
    universe = list(range(k))
    F = [frozenset(S) for S in itertools.chain.from_iterable(
        itertools.combinations(universe, r) for r in range(k + 1))]
    if not check_ineq(F, universe):
        violations += 1

# Suite 3: random union-closed families for larger ground sets.
# Generate random collections, close under union, check.
random.seed(42)
for trial in range(500):
    k = random.randint(2, 7)
    universe = list(range(k))
    base_elems = [frozenset(S) for S in itertools.chain.from_iterable(
        itertools.combinations(universe, r) for r in range(k + 1))]
    # Pick a random subset and close under union.
    seed_size = random.randint(1, min(8, len(base_elems)))
    seed = random.sample(base_elems, seed_size)
    # Union-close: repeatedly take unions until stable.
    F = set(seed)
    changed = True
    while changed:
        changed = False
        for A in list(F):
            for B in list(F):
                C = A | B
                if C not in F:
                    F.add(C)
                    changed = True
    F = list(F)
    if len(F) < 2:
        continue
    if not check_ineq(F, universe):
        violations += 1

assert violations == 0, (
    f"VIOLATION: KL deficiency inequality log2|F|-H(AuB) >= (1-p)^2/4 "
    f"fails on {violations} family/families"
)
CHECK -->
