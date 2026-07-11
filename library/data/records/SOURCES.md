# Explicit cap sets in AG(n,3) — sources and provenance

All point files below are **verified**: `verify_files.py` (in this directory) re-reads
every `cap_ag*.txt` from disk and checks that all points are distinct, use digits
{0,1,2}, and that for every pair (a,b) the completing point c = -(a+b) mod 3 is not a
third distinct member. Last run: all files OK.

File format: one point per line, n digits from {0,1,2} (coordinate i of the point =
i-th digit). A cap set = no three distinct points summing to 0 mod 3 componentwise.

## Primary data source

Yves Edel's cap data pages. The old Heidelberg site
(`https://www.mathi.uni-heidelberg.de/~yves/Matritzen/CAPs/CAPMatIndex.html`) is **dead
(404)**, but the identical site is **live** at his personal domain:

- Index: http://www.yvesedel.de/Matritzen/CAPs/CAPMatIndex.html
  (Wayback snapshot of the Heidelberg original, 2025-01-01, saved here as
  `capmatindex.html`: http://web.archive.org/web/20250101191611/https://www.mathi.uni-heidelberg.de/~yves/Matritzen/CAPs/CAPMatIndex.html)
- Generator matrices used (raw HTML saved in this directory):
  - `raw_(248,7,3).html`  <- http://www.yvesedel.de/Matritzen/CAPs/Matrizen/(248,7,3).html   (248-cap in PG(7,3))
  - `raw_(541,8,3).html`  <- http://www.yvesedel.de/Matritzen/CAPs/Matrizen/(541,8,3).html   (541-cap in PG(8,3))
  - `raw_(1216,9,3).html` <- http://www.yvesedel.de/Matritzen/CAPs/Matrizen/(1216,9,3).html  (1216-cap in PG(9,3))
  - `raw_(2744,10,3).html`<- http://www.yvesedel.de/Matritzen/CAPs/Matrizen/(2744,10,3).html (2744-cap in PG(10,3), downloaded but not used in final files)

Each page gives a (k, N) matrix over F_3 whose N columns are representatives of the
points of an N-cap in PG(k-1,3), written as k rows of N digits.

## Per-file provenance and conversion

### cap_ag7_3_236.txt — 236-cap in AG(7,3)  [matches record LB 236]
From the (248,7,3) matrix (8 rows x 248 cols). Edel notes "the last row of the check
matrix is a word of maximal weight": exactly 236 columns have last coordinate 1 (the
other 12 lie on the hyperplane at infinity). Conversion (`extract_and_verify.py`):
keep columns with nonzero last coordinate, scale so the last coordinate is 1 (multiply
by 2 mod 3 if needed; here all were already 1), drop the last coordinate. Soundness:
three affine points with a+b+c=0 would lift to (a,1)+(b,1)+(c,1)=0, i.e. three
collinear points of the projective cap — impossible. Construction origin: Edel,
"Extensions of generalized product caps" (Des. Codes Cryptogr. 31 (2004)), Section 3
(doubled Hill cap + Theorem 5, m=1); first found by Calderbank–Fishburn (1994).

### cap_ag8_3_496.txt — 496-cap in AG(8,3)  [matches record LB used as capset_n8 baseline]
Doubling construction applied to the (248,7,3) matrix (`double_and_verify.py`): for
each of the 248 projective points take BOTH nonzero representatives v and 2v in F_3^8,
giving 2*248 = 496 affine points. Soundness: if a+b+c=0 with b=2a then c=0 (excluded);
three distinct projective lines would be collinear in PG(7,3) — impossible.
This "standard doubling" (cap in PG(k-1,3) -> 2N-cap in AG(k,3)) is the construction
Edel attributes for the affine records (same trick that makes the 112-cap in AG(6,3)
the "doubled Hill cap").

### cap_ag8_3_512_funsearch.txt — 512-cap in AG(8,3)  [actual current record for n=8]
Explicit construction transcribed verbatim from Google DeepMind's FunSearch repo:
https://github.com/google-deepmind/funsearch/blob/main/cap_set/cap_set.ipynb
(cell "Explicit construction of a 512-cap in n = 8 dimensions"; saved here as
`funsearch_capset.ipynb`). Reference: Romera-Paredes et al., "Mathematical discoveries
from program search with large language models", Nature 625 (2024) 468-475. This
BEATS the 496 baseline; 512 > 496 is the biggest known n=8 cap.
Rebuilt and verified by `build_funsearch_512.py`.

### cap_ag9_3_1082.txt — 1082-cap in AG(9,3)  [matches record LB 1082]
Doubling construction applied to the (541,8,3) matrix: 2*541 = 1082 affine points in
AG(9,3) (`double_and_verify.py`). The 541-cap in PG(8,3) is from Bierbrauer–Edel,
"Large caps in projective Galois spaces" (survey; `CapSurvey.pdf` in this directory,
from http://www.yvesedel.de/Papers/CapSurvey.pdf). The FunSearch notebook explicitly
confirms 1082 as "the largest known cap set for n = 9".

### cap_ag10_3_2432.txt — 2432-cap in AG(10,3)  [best explicit construction found; see caveat]
Doubling construction applied to the (1216,9,3) matrix: 2*1216 = 2432 affine points in
AG(10,3) (`build_n10.py`). The 1216-cap in PG(9,3) is from Edel, "Extensions of
generalized product caps" (112*10 + 12*8 ovoid-based extended product; `ExtProd.pdf` /
`ExtProd.txt` in this directory, from http://www.yvesedel.de/Papers/ExtProd.pdf).

**Caveat on the 2474 target:** the task (and this repo's `problems/capset_n10.json`)
state the n=10 record as "2474 (Edel)". An extensive search found NO published source
for 2474: it is absent from Edel's cap index and all his downloadable papers (ExtProd,
RCap, smallCaps, CapSurvey — all text-searched), from Tyrrell 2022, Elsholtz–Lipnik
2022, Elsholtz–Pach 2020, the FunSearch paper/repo, and the web at large. A 2021 TU
Delft thesis table of best known lower bounds lists n=9: 1064, n=10: **2240** (products);
doubling Edel's 1216-cap gives 2432 > 2240 and is, as far as this search can tell, the
best *documented explicit* cap in AG(10,3). Note 2432 = 2*1216 and 2474 = 2432 + 42;
however `build_n10.py` shows the doubled 2432-cap is **complete** (zero unblocked
points), so 2474 is not a completion of it. The 2474 baseline appears to have entered
this repo's problem JSON without a citation (initial scaffold commit) and may be
incorrect. Alternative documented lower bounds for n=10 are all smaller:
2228 (affine part of the (2744,10,3) PG cap, max dual weight 2228), 2240 = 112*20
(product), 2164 = 2*1082.

## Verification scripts in this directory

- `extract_and_verify.py` — parses the PG matrices, extracts affine parts (n=7).
- `double_and_verify.py`  — doubling for n=8 (496) and n=9 (1082).
- `build_n10.py`          — doubling for n=10 (2432) + completeness/greedy-extension check.
- `build_funsearch_512.py`— FunSearch explicit 512-cap (n=8).
- `verify_files.py`       — independent re-verification of all cap_ag*.txt files from disk.

Run any of them with: `uv run python <script>` from C:\Users\honsf\DEVELOP\auto-erdos.
