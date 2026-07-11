# Construction recipes for record caps in AG(n,3)

Explicit point data for n=7 (236), n=8 (496 and 512), n=9 (1082), n=10 (2432) is
already in this directory (see SOURCES.md). This file documents the *constructions*
so they can be re-implemented from scratch in Python, and gives the machinery
relevant to pushing n=10 beyond 2432.

## 0. Conventions

AG(n,3) = F_3^n; a cap is S with no three distinct a,b,c, a+b+c = 0 (mod 3).
PG(k-1,3): points are 1-dim subspaces {v, 2v} of F_3^k; a projective cap has no
three points collinear, equivalently no three pairwise-independent representatives
with a linear dependency.

## 1. Doubling: N-cap in PG(k-1,3)  ->  2N-cap in AG(k,3)

For each projective cap point take BOTH nonzero vectors v and 2v of its line.
Proof of cap property: a+b+c=0 with b=2a forces c=0 (not in the set); three
distinct lines with a dependency contradict the projective cap.

This single rule, fed with Edel's generator matrices, produces all the classical
affine records:

| PG cap (Edel's site)     | doubled affine cap        |
|--------------------------|---------------------------|
| 56-cap in PG(5,3) (Hill) | 112-cap in AG(6,3) (optimal) |
| 248-cap in PG(7,3)       | 496-cap in AG(8,3)        |
| 541-cap in PG(8,3)       | 1082-cap in AG(9,3)       |
| 1216-cap in PG(9,3)      | 2432-cap in AG(10,3)      |

(For n=7 the 236-cap is NOT a doubling; it is the affine part of the 248-cap in
PG(7,3): keep the 236 columns off the hyperplane at infinity, normalize last
coordinate to 1, drop it.)

## 2. Edel's extended product (Theorem 5 of "Extensions of generalized product caps")

Ingredients over q=3:
- Caps A_0, A_1, ..., A_c in AG(n,3), 0 not in A_i, satisfying property (EL)
  (three technical collinearity-avoidance conditions between the blocks).
- Sets B_0, B = B_1 u ... u B_c of vectors in F_3^{m+1} that are systems of
  representatives of caps in PG(m,3) satisfying (ER), where the points extending
  <B_1> and <B_2> (i.e., compatible with both) form B_0.

Then K = union_i (A_i : B_i) is a cap in PG(n+m,3) with sum_i |A_i||B_i| points,
and K is AFFINE (in AG(n+m,3)) if the <B_i> all avoid a common hyperplane.

The workhorse instance (q=3, n=6): the doubled Hill cap in AG(6,3) written as
H = D u R and H' = D' u R where
- D  = the 20 weight-3 vectors of F_3^6 whose supports are the blocks of a fixed
  2-(6,3,2) design and D' = the other 20 weight-3 vectors (choose the design so
  D consists of, e.g., supports {124,235,346,451,512,136,245,356,146,256} —
  any 2-(6,3,2) design works; each of the 10 supports carries 2^? sign patterns...
  in practice: D = weight-3 vectors with support in the design and an even number
  of 2s, see ExtProd.pdf Definition 6),
- R  = the weight-6 vectors with an even number of 2s, R' = the rest,
- A_0 = the 12 weight-1 vectors, A_1 = H = D u R, A_2 = H' = D' u R.
Then |A_1| = |A_2| = 112, |A_0| = 12, |A_1 n A_2| = |R| = 32, and (A_0, A_1, A_2)
satisfies (EL). Key identity: H + H' = F_3^6 \ A_0.

Applications (all in ExtProd.pdf Section 3):
- m=1: B_1 = B_2 = one point each, B_0 = 1 affine / 2 projective points
  -> 236-cap in AG(7,3) = 112*2 + 12*1  and 248-cap in PG(7,3) = 112*2 + 12*2.
- m=3: B_1 u B_2 = the 10 points of an elliptic quadric (ovoid) in PG(3,3) split
  via squares/nonsquares of F_9 (B_1 = {(0,0,1)} u {(Q,1,1)}, B_2 = {(0,1,0)} u
  {(N,2,1)} where Q = squares, N = nonsquares of F_9 written over F_3^2, ovoid
  points (x : N(x) : 1), N(x) = x^4), B_0 = the 8 points (Q:0:1),(N:1:0)
  -> 1216-cap in PG(9,3) = 112*10 + 12*8.
- m=5: B = representatives of the Hill 56-cap split as <B_1> = <R>, <B_2> = <D>,
  B_0 = 16 points from <R'> -> 6464-cap in PG(11,3) = 112*56 + 12*16.

## 3. Capsets / admissible sets (recursive layer; for large n)

Definition 9 + Lemma 10 of ExtProd: a "capset" S subset {0,...,c}^l selects which
block A_{s_i} goes in which coordinate section; S(A_0,...,A_c) is a cap in
AG(l*n, 3). Explicit computer-found examples are on Edel's live site:
http://www.yvesedel.de/Matritzen/CAPs/Is/Iindex.html
(I2(9,2), I2(10,3), I2(9,4), I2(9,5), I2(10,6), tilde-I2(11,2), tilde-I2(10,5)).
These only matter for n >= 18 (products of the 6-dim family), not for n <= 10.

## 4. Status of n = 10

- Doubled 1216-cap = 2432 points, VERIFIED, and verified COMPLETE (no point of
  F_3^10 can be added; `build_n10.py`).
- The affine part of Edel's 2744-cap in PG(10,3) is only 2228 (its max dual
  weight), so that route is worse.
- The task's target 2474 has no findable published source (see SOURCES.md); if a
  2474-cap exists it likely requires either (a) a >1216-cap in PG(9,3) plus
  doubling (2474 = 2*1237: a 1237-cap in PG(9,3) would suffice — none is
  published), or (b) an extended-product with an improved B-side in AG(4,3)/PG(4,3),
  or (c) expurgate-and-extend on the 2432-cap: remove some points of the doubled
  cap and re-extend by more than were removed (a local-search project, not a
  documented construction).
- Best documented explicit caps in AG(10,3), in order: 2432 (doubling, this dir),
  2240 = 112 x 20 (product of AG(6,3)-optimal cap with AG(4,3)-optimal cap;
  direct product of caps is a cap), 2228 (affine part of (2744,10,3)).
- For search seeding: 2·512 = 1024-cap in AG(9,3) or 512 x 4 = 2048-cap in
  AG(10,3) products from the FunSearch 512-cap are DOMINATED by the Edel-derived
  caps above; the FunSearch cap only helps at n=8.

## 5. Direct product (used for the 2240 fallback)

If A is a cap in AG(m,3) and B a cap in AG(n,3) then A x B is a cap in
AG(m+n,3) of size |A||B| (projecting a dependency to either factor forces all
three equal there or a violation). E.g. 112 x 20 = 2240 in AG(10,3).
