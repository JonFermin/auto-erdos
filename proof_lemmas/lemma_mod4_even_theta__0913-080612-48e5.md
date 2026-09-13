---
id: mod4_even_theta
status: proved
depends_on: []
discharged_by_round: 87
introduced_at_round: 87
---

# Lemma `mod4_even_theta` (proved — the theta parity pigeonhole, and the C16-ear mod-4 corollary)

**Context.** This lemma is the technique-mining deliverable of
Q0905-082429-2's committed STEP 0 (literature check on the mod-4
invariant program). The literature verdict itself is recorded in the
"Literature ledger" section below and in proof_strategy.md Section
127; the lemma proper (T1, T2, C1) is fully self-contained and does
not depend on any citation except where explicitly stated (C1 cites
the Dean–Lesniak–Saito theorem).

## T1 — Theta parity pigeonhole

**Setting.** A *theta graph* $\Theta(a,b,c)$ consists of two
distinct vertices $x, y$ joined by three internally vertex-disjoint
paths $P_1, P_2, P_3$ of lengths $a, b, c \ge 1$ (edge counts), at
most one of length $1$ (simple graph). Its cycles are exactly the
three path-pair unions, of lengths $a+b$, $a+c$, $b+c$.

**Statement.**
(i) If $a, b, c$ are all even, then $\Theta(a,b,c)$ contains a
cycle of length $\equiv 0 \pmod 4$.
(ii) If $a, b, c$ are all odd, then $\Theta(a,b,c)$ contains a
cycle of length $\equiv 0 \pmod 4$ **unless**
$a \equiv b \equiv c \pmod 4$, in which case all three cycles are
$\equiv 2 \pmod 4$.
(iii) (Sharpness of the parity hypothesis) In the mixed-parity case
exactly one cycle is even — the union of the two same-parity paths —
and it is $\equiv 0 \pmod 4$ iff those two lengths are congruent
mod 4; no unconditional conclusion holds.

**Proof.**
(i) Each of $a, b, c$ is $\equiv 0$ or $2 \pmod 4$. By pigeonhole
two of them are congruent mod 4, say $a \equiv b$. Then
$a + b \equiv 2a \equiv 0 \pmod 4$ since $a$ is even. The cycle
$P_1 \cup P_2$ has length $a + b \equiv 0 \pmod 4$.
(ii) Each of $a, b, c$ is $\equiv 1$ or $3 \pmod 4$. If both
residues occur, a path $\equiv 1$ and a path $\equiv 3$ give a cycle
of length $\equiv 1 + 3 \equiv 0 \pmod 4$. If only one residue
occurs, every pair sums to $1+1 = 2$ or $3+3 = 6$, i.e.
$\equiv 2 \pmod 4$ in both cases.
(iii) If, say, $a \not\equiv b \pmod 2$ then $a+b$ is odd; the only
even cycle is the pair with equal parities, and evenness mod 4 of a
sum of two same-parity numbers is exactly congruence mod 4 of the
summands (even case: $u \equiv v \pmod 4 \Rightarrow u+v \equiv 2u
\equiv 0$; if $u \not\equiv v$, $u + v \equiv 2 \pmod 4$; odd case:
$u \equiv v \Rightarrow u+v \equiv 2$, $u \not\equiv v \Rightarrow
u+v \equiv 0$ — note the odd case REVERSES, which is why (ii) reads
"unless all congruent"). $\square$

**Slogan.** *An all-even theta always carries a 0-mod-4 cycle; an
all-odd theta carries one exactly when its path lengths are not all
congruent mod 4.* The all-even case is pure pigeonhole on
$\{0, 2\}$; nothing about the host graph is used.

## T2 — C16-ear mod-4 corollary

**Setting.** $C$ a chordless $16$-cycle in a graph $G$, $e$ an ear
(a path with interior off $C$) of length $\ell \ge 2$ between
$C$-vertices at arc distance $d$, $1 \le d \le 15$. Then
$C \cup e = \Theta(d,\, 16-d,\, \ell)$ with cycle lengths
$16$, $d + \ell$, $16 - d + \ell$.

**Statement.** Suppose $d$ and $\ell$ are both even.
(a) If $d + \ell \equiv 0 \pmod 4$, then **both** ear cycles have
length $\equiv 0 \pmod 4$.
(b) If $d + \ell \equiv 2 \pmod 4$, then both ear cycles are
$\equiv 2 \pmod 4$ and the only 0-mod-4 cycle in $C \cup e$ is $C$
itself.

**Proof.** $16 - d + \ell \equiv \ell - d \equiv (d + \ell) - 2d
\pmod 4$, and $2d \equiv 0 \pmod 4$ because $d$ is even. So both
ear cycles are congruent to $d + \ell$ mod 4, and (a), (b) read off.
$\square$

**Remark (relation to E2).** The R85 exclusion law E2 in
`c16_d1_ear_cover` ($c + s \notin \{4, 8\}$ on menus) is the
power-of-2 shadow of this arithmetic at specific small lengths; T2
is the residue-level statement: an even ear at even distance sends
BOTH of its cycles into the same mod-4 class simultaneously. In a
graph avoiding all power-of-2 cycle lengths, case (a) therefore
forces $d + \ell$ and $16 - d + \ell$ both into
$\{12, 20, 24, 28, 36, \dots\}$ (multiples of 4 that are not powers
of 2).

## C1 — CONDITIONAL corollary for the EGC counterexample profile

**Ledger discipline.** The antecedent L-DLS below is an EXTERNAL
theorem that is NOT in `proofs/erdos_gyarfas.json:given_facts`
(which carries only F1–F3). C1 is therefore stated and proved as an
*implication with external antecedent*: the implication itself is
internal and self-contained, but its conclusion is NOT available as
a step in any internal proof of this attempt until the maintainer
adds DLS 1993 to the spec ledger (flagged in Section 127) — or the
antecedent is re-proved internally. Nothing elsewhere in this
attempt cites C1's conclusion as established.

**Statement.** Let $G$ be any counterexample to the Erdős–Gyárfás
conjecture: $\delta(G) \ge 3$ and $G$ has no cycle of length $2^k$.
**IF** the Dean–Lesniak–Saito theorem holds (L-DLS below: minimum
degree $\ge 2$ with at most two degree-2 vertices forces a cycle
$\equiv 0 \pmod 4$), **THEN**:
(a) $G$ contains a cycle of length $\equiv 0 \pmod 4$; since no
power of 2 is a cycle length of $G$, that length lies in
$\{12, 20, 24, 28, 36, 40, \dots\}$.
(b) The same holds for EVERY subgraph $H \subseteq G$ with
$\delta(H) \ge 2$ and at most two vertices of degree 2 — 0-mod-4
supply is ubiquitous in a counterexample, and all of it avoids
powers of 2.
(c) $S_4(G) := \{\text{cycle lengths of } G \text{ divisible by }
4\} \ne \emptyset$: item (i) of the Q0905-082429-2 dyadic
decomposition follows, with no computation needed.

**Proof.** (a), (c): L-DLS applied to $G$ (min degree $\ge 3$ means
zero degree-2 vertices) gives a cycle $\equiv 0 \pmod 4$; the
smallest multiples of 4 are 4, 8, 16 (powers of 2, excluded), then
12, 20, 24, 28 are the non-powers below 32. (b): L-DLS applied to
$H$; a cycle of $H$ is a cycle of $G$, so it avoids powers of 2 in
$G$'s length set. $\square$

## Literature notes (EXTERNAL context — not in the given-facts ledger, not citable by internal proof steps)

None of the items below is in `proofs/erdos_gyarfas.json:given_facts`
(F1–F3). They are recorded here ONLY as (a) the STEP 0 verdict that
re-scoped Q0905-082429-2 — a program-steering decision, not a proof
step — and (b) the antecedent of the conditional C1. No lemma
status, no internal claim, and no proof section treats any of them
as established. Maintainer action that would upgrade them to
citable: add entries to the spec's `given_facts` (the spec is
read-only to sessions by design).

Transcribed 2026-09-13 from search abstracts (full texts
egress-blocked in this container); T1/T2 above are independent of
all of these. Confidence: L-DLS corroborated by three independent
snippets; the rest single-source, re-verify before any use.

- **L-DLS** (N. Dean, L. Lesniak, A. Saito, *Cycles of length 0
  modulo 4 in graphs*, Discrete Mathematics, 1993): every graph
  with minimum degree $\ge 2$ and at most two vertices of degree 2
  contains a cycle of length $\equiv 0 \pmod 4$. Corollary:
  $\delta \ge 3$ suffices. **Hence L_mod4 — the target of
  Q0905-082429-2 — is a 1993 theorem, and that qid's falsifier arm
  (a mod-4-avoiding min-degree-3 graph would be a complete EGC
  counterexample) is void: no falsifier exists.**
- **Dean's conjecture** ($\delta \ge k \Rightarrow$ a cycle
  $\equiv 0 \bmod k$) is known true for all $k \ne 5$ (status as
  reported by Choi–Chu 2026).
- **Choi–Chu 2026** (arXiv:2605.02731): for $k \in \{3,4\}$,
  minimum degree $\ge 2$ with at most $k-2$ degree-2 vertices
  suffices; all exceptional graphs with $\le 3$ degree-2 vertices
  and no 0-mod-$k$ cycle are characterized (for $k=3$: generated
  from $K_{2,3}$ by three operations).
- **Győri–Li–Salia–Tompkins–Varga–Zhu line** (arXiv:2312.09999;
  see also arXiv:2507.12798 for the 2-connected characterization):
  every even theta graph contains a 0-mod-4 cycle (T1(i) is our
  self-contained proof of the pigeonhole core); every non-planar
  graph contains a 0-mod-4 cycle; a bipartite $n$-vertex graph with
  no 0-mod-4 cycle has at most $3(n-2)/2$ edges.

**Consequence for the program** (steering, not proof). Q0905-082429-2's
residual value after STEP 0: (1) the dyadic decomposition's item (i)
is settled in the literature (conditionally here, via C1(c)); items
(ii) ($\max S_4 \ge 2 \min S_4$) and (iii) (no
gap $> 4$ in $S_4$ straddling a power of 2) are the genuine open
content, and both are now statements about a set the literature
guarantees nonempty; (2) the
prior falsification effort on L_mod4 (exhaustive $n \le 7$, 21k
random cubic) was rediscovery of a known theorem and should never
be re-run; (3) the non-planarity fact means any EGC counterexample
restricted to a planar subgraph is where 0-mod-4 cycles could
conceivably be scarce — the supply in C1(b) is subgraph-local, not
just global.

<!-- CHECK
# CHECK 1 - T1 on REAL theta graphs: for all path length triples
# (a,b,c), 2<=a<=b<=c<=7, build Theta(a,b,c) as an explicit graph,
# enumerate ALL simple cycles by DFS (no reliance on the "exactly
# three cycles" claim), and verify: cycle length multiset is exactly
# {a+b,a+c,b+c}; the all-even pigeonhole (i); the all-odd law (ii).
def theta(a, b, c):
    # vertices: 0=x, 1=y; internal vertices numbered from 2
    adj = {0: set(), 1: set()}
    nxt = 2
    for L in (a, b, c):
        prev = 0
        for i in range(L - 1):
            adj[nxt] = set()
            adj[prev].add(nxt); adj[nxt].add(prev)
            prev = nxt; nxt += 1
        adj[prev].add(1); adj[1].add(prev)
    return adj

def all_cycle_lengths(adj):
    # enumerate simple cycles via DFS from each root, canonical form dedup
    seen = set()
    verts = sorted(adj)
    def dfs(root, v, path, onpath):
        for w in adj[v]:
            if w == root and len(path) >= 3:
                key = frozenset(zip(path, path[1:] + [root]))
                # canonicalize as edge set (undirected)
                key = frozenset(frozenset(e) for e in key)
                seen.add((len(path), key))
            elif w not in onpath and w > root:
                onpath.add(w)
                dfs(root, w, path + [w], onpath)
                onpath.discard(w)
    for r in verts:
        dfs(r, r, [r], {r})
    from collections import Counter
    return sorted(l for (l, k) in seen)

from collections import Counter
for a in range(2, 8):
    for b in range(a, 8):
        for c in range(b, 8):
            lens = all_cycle_lengths(theta(a, b, c))
            assert Counter(lens) == Counter([a+b, a+c, b+c]), (a, b, c, lens)
            z4 = any(l % 4 == 0 for l in lens)
            if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
                assert z4, ("T1(i) falsified", a, b, c)
            if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
                assert z4 == (not (a % 4 == b % 4 == c % 4)), ("T1(ii)", a, b, c)

# CHECK 2 - T2 arithmetic over the full (d, ell) box:
for d in range(1, 16):
    for ell in range(2, 25):
        cyc = [16, d + ell, 16 - d + ell]
        if d % 2 == 0 and ell % 2 == 0:
            if (d + ell) % 4 == 0:
                assert cyc[1] % 4 == 0 and cyc[2] % 4 == 0, (d, ell)
            else:
                assert cyc[1] % 4 == 2 and cyc[2] % 4 == 2, (d, ell)

# CHECK 3 - C1(a) profile: multiples of 4 below 44 that are not
# powers of 2 are exactly 12,20,24,28,36,40.
assert [m for m in range(4, 44, 4) if m & (m - 1)] == [12, 20, 24, 28, 36, 40]

print("CHECK ok: T1 on real thetas (2<=a<=b<=c<=7) | T2 (d,ell) box | C1 profile")
-->
