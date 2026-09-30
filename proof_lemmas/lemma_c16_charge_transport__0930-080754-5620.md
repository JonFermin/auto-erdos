---
id: c16_charge_transport
status: proved
depends_on: []
discharged_by_round: 103
introduced_at_round: 103
---

# Lemma `c16_charge_transport` (proved — the general-$n$ charge identity for chordless $C_{16}$s; "$\mu(H) \le 1$" is a finite-size artifact, and $k = 0$ is confined to $n \le 32 + s_C$)

**Setting.** $G$ a finite simple graph, $\delta(G) \ge 3$, $C$ a
CHORDLESS $16$-cycle in $G$, $H := G - V(C)$. Write $n = |V(G)|$,
$s := \sum_{v \in G}(\deg v - 3) \ge 0$ (total excess degree),
$s_C := \sum_{v \in C}(\deg v - 3) \ge 0$ (excess on the cycle),
$c(H)$ = number of components of $H$, $\mu(H) = e(H) - |V(H)| + c(H)$
(cycle rank), and $k$ = number of $0$-spoke vertices of $H$ (vertices
with no neighbour on $C$ — for cubic $G$ this is the branch-vertex
count of the incumbent program, per (B0)/(Z) of
`c16_branch_vertex_arithmetic`).

**Statement.**

- **(i) (charge identity)**
  $$\mu(H) \;=\; \frac{n}{2} - 16 + c(H) + \frac{s}{2} - s_C.$$
- **(ii) (the $k$-window)** $k \ \ge\ n - 32 - s_C$. Equivalently,
  $k = 0$ forces $n \le 32 + s_C$; for cubic $G$, $k = 0$ forces
  $n \le 32$.
- **(iii) (the $\mu$-law is finite-size)** For cubic $G$,
  (i) reads $\mu(H) = n/2 - 16 + c(H)$, i.e.
  $c(H) - \mu(H) = (32 - n)/2$ — the incumbent (B1) constant at each
  fixed $n$. Hence $\mu(H) \ge 2$ for EVERY cubic $G$ with a chordless
  $C_{16}$ once $n \ge 34$, and at $n = 32$, $\mu(H) = c(H)$; the
  explicit cubic $C_4/C_8$-free witness in CHECK B realizes
  $n = 32$, $k = 0$, $\mu(H) = c(H) = 2$. So "$\mu(H) \le 1$", proved
  by enumeration at $n \in \{24, 26\}$ (R100/R101), is a small-$n$
  counting effect, NOT a law of the class.

**Proof.** (i): Since $C$ is chordless, every edge at a $C$-vertex is
either one of the $16$ cycle edges or a spoke into $H$; a $C$-vertex
$v$ sends $\deg(v) - 2$ spokes, so the spoke count is
$\sum_{v \in C}(\deg v - 2) = 16 + s_C$. By handshake
$e(G) = \tfrac{1}{2}\sum_v \deg v = (3n + s)/2$. Therefore
$$e(H) = e(G) - 16 - (16 + s_C) = \frac{3n + s}{2} - 32 - s_C,$$
and with $|V(H)| = n - 16$:
$$\mu(H) = e(H) - (n - 16) + c(H)
        = \frac{n}{2} - 16 + \frac{s}{2} - s_C + c(H). \qquad$$
(ii): The spoke feet lie in $H$ and number at most $16 + s_C$ (with
multiplicity; distinct feet only fewer), so at least
$(n - 16) - (16 + s_C)$ vertices of $H$ carry no spoke. (iii):
substitute $s = s_C = 0$; $c(H) \ge 1$ gives $\mu(H) \ge n/2 - 15
\ge 2$ at $n \ge 34$; CHECK B pins the $n = 32$ realization.
$\square$

**Provenance.** Surfaced by the 2026-09-30 ideation pass
(analogy-miner proposal P8, a Four-Colour-Theorem port; Judge RIGOR's
crown at 9/10, hand re-derived there); this round re-proves it from
scratch and re-verifies the witness with independent code. It is the
$n$-scaling form of the incumbent fixed-$n$ constant (B1).

**Consequences for the open core (rescope, R103).**

1. Open-core item 2 ("$\mu(H) \le 1$ as a general-$n$ lemma via the
   B3 menu") is DEAD AS STATED by (iii). The honest general-$n$
   restatement is a bound on $c(H)$ and excess degree — e.g. "every
   component of $H$ meets $C$" ($k$-flavoured) or per-component
   absorption bounds; the $\mu$-value itself grows linearly in $n$.
2. Open-core item 1 (the $k = 0$ mechanism) is a FINITE question by
   (ii): for cubic $G$ the whole $k = 0$ branch lives in
   $24 \le n \le 32$ ($n$ even). Moreover $\mu(H) \ge 0$ turns (i)
   into a POSITIVITY constraint on such a graph's outside structure:
   for cubic $G$, $c(H) \ge 16 - n/2$, so a $k = 0$ carrier's outside
   graph $H$ has at least $16 - n/2$ components — at least $2$ at
   $n = 28$, at least $1$ at $n = 30$, unconstrained at $n = 32$
   (the CHECK B witness has $c(H) = 2$). In particular a $k = 0$
   graph at $n = 28$ CANNOT have connected $H$. The $n = 26$ scarcity
   (1 of 178) therefore does NOT indicate a general-$n$ scarcity law;
   it is the window's near-empty lower edge. Only the $n = 32$
   witness is independently verified here (CHECK B); whether the
   $n = 28, 30$ interior is actually inhabited (subject to the
   component constraint above) is a finite enumeration — the concrete
   remaining content of open-core item 1 — not an asymptotic
   argument.
3. Any general-$n$ supply/floor argument (Q81) must budget for
   $\mu(H) \sim n/2$ independent outside cycles; arguments that
   implicitly assume a forest-like or unicyclic $H$ cannot survive
   past $n = 32$.

<!-- CHECK
# CHECK A - the charge identity and the k-window on 300+ seeded random
# C16-carrying graphs with general degrees (C = 0..15 kept chordless).
import random
def comps(vs, adj):
    vs = set(vs); seen = set(); c = 0
    for v in vs:
        if v in seen: continue
        c += 1; st = [v]; seen.add(v)
        while st:
            u = st.pop()
            for w in adj[u]:
                if w in vs and w not in seen: seen.add(w); st.append(w)
    return c
rng = random.Random(7)
tested = 0
for _ in range(400):
    n = rng.randint(22, 40)
    adj = [set() for _ in range(n)]
    def add(a, b): adj[a].add(b); adj[b].add(a)
    for i in range(16): add(i, (i + 1) % 16)
    ok = True
    for v in range(n):
        guard = 0
        while len(adj[v]) < 3 and guard < 500:
            guard += 1
            w = rng.randrange(16, n) if v < 16 or rng.random() < 0.8 else rng.randrange(n)
            if w != v and w not in adj[v] and not (v < 16 and w < 16): add(v, w)
        if len(adj[v]) < 3: ok = False; break
    if not ok: continue
    s = sum(len(adj[v]) - 3 for v in range(n))
    sC = sum(len(adj[v]) - 3 for v in range(16))
    Hv = list(range(16, n))
    eH = sum(1 for u in Hv for w in adj[u] if w in Hv and w > u)
    c = comps(Hv, adj)
    mu = eH - (n - 16) + c
    k = sum(1 for h in Hv if not (adj[h] & set(range(16))))
    assert 2 * mu == n - 32 + s - 2 * sC + 2 * c, (n, mu, s, sC, c)
    assert k >= n - 32 - sC, (n, k, sC)
    tested += 1
assert tested >= 300, tested
CHECK -->

<!-- CHECK
# CHECK B - the explicit n=32 witness: cubic, C = (0..15) chordless,
# NO C4 and NO C8 anywhere, k = 0, c(H) = 2, mu(H) = 2 - the mu-law
# falsifier at the top of the k=0 window. (Ideation P8's graph,
# re-verified with independent code.)
E_OUT = [(16,18),(16,19),(17,21),(17,23),(18,27),(19,22),(20,26),(20,28),(21,30),(22,24),
         (23,31),(24,27),(25,29),(25,31),(26,29),(28,30)]
adj = [set() for _ in range(32)]
for i in range(16):
    adj[i] |= {(i + 1) % 16, (i - 1) % 16, 16 + i}
    adj[16 + i].add(i)
for a, b in E_OUT:
    adj[a].add(b); adj[b].add(a)
assert all(len(x) == 3 for x in adj)
for i in range(16):
    assert adj[i] == {(i + 1) % 16, (i - 1) % 16, 16 + i}   # C chordless, one spoke each
def has_len(targets):
    cap = max(targets)
    for s in range(32):
        stack = [(s, 1 << s, 1)]
        while stack:
            v, mask, d = stack.pop()
            for w in adj[v]:
                if w == s and d in targets: return True
                if w > s and not (mask >> w) & 1 and d < cap:
                    stack.append((w, mask | 1 << w, d + 1))
    return False
assert not has_len({4}), "C4 present"
assert not has_len({8}), "C8 present"
Hv = list(range(16, 32))
k = sum(1 for h in Hv if not (adj[h] & set(range(16))))
eH = sum(1 for u in Hv for w in adj[u] if w in Hv and w > u)
seen = set(); c = 0
for v in Hv:
    if v in seen: continue
    c += 1; st = [v]; seen.add(v)
    while st:
        u = st.pop()
        for w in adj[u]:
            if w in Hv and w not in seen: seen.add(w); st.append(w)
mu = eH - 16 + c
assert (k, eH, c, mu) == (0, 16, 2, 2), (k, eH, c, mu)
assert mu == 32 // 2 - 16 + c    # identity instance at s = s_C = 0
CHECK -->

<!-- CHECK
# CHECK C - consistency with the incumbent fixed-n constant (B1):
# cubic identity c(H) - mu(H) = (32 - n)/2 gives 4 at n=24 and 3 at
# n=26, matching c16_branch_vertex_arithmetic / c16_n26_classification.
for n, expect in ((24, 4), (26, 3), (32, 0)):
    assert (32 - n) // 2 == expect
# and the mu >= 2 threshold for cubic: n/2 - 16 + c >= 2 with c >= 1
# holds for all n >= 34
for n in range(34, 66, 2):
    assert n // 2 - 16 + 1 >= 2
CHECK -->

<!-- CHECK
# CHECK D - the positivity constraint on a cubic k=0 carrier: mu(H) >= 0
# with the identity mu = n/2 - 16 + c forces c(H) >= 16 - n/2. So the
# minimum component count of H over the k=0 window is:
for n, cmin in ((24, 4), (26, 3), (28, 2), (30, 1), (32, 0)):
    assert 16 - n // 2 == cmin
# hence a k=0 graph at n=28 needs c(H) >= 2 (connected H is impossible):
# the tuple (n=28, c=1) would give mu = -1 < 0, excluded.
assert 28 // 2 - 16 + 1 < 0
# and every VALID (n, c) with c >= max(1, 16 - n/2) yields mu >= 0:
for n in range(24, 34, 2):
    cmin = max(1, 16 - n // 2)
    for c in range(cmin, cmin + 4):
        assert n // 2 - 16 + c >= 0
CHECK -->
