Let
$$
S=\{1,2,34,84,105,111,125,164,186,201,204,250,252,259,315,319,344,357,387,431,441,457,465,476,488,493\}.
$$
Set
$$
T:=S-1=\{0,1,33,83,104,110,124,163,185,200,203,249,251,258,314,318,343,356,386,430,440,456,464,475,487,492\}.
$$
The map \(x\mapsto x+1\) is a bijection \(T\to S\), so it preserves cardinality, and it also preserves pair-sum collisions:
$$
(x+1)+(y+1)=(u+1)+(v+1)\iff x+y=u+v.
$$
Thus \(S\) is a Sidon set if and only if \(T\) is a Sidon set. All arithmetic below is in \(\mathbb Z\); there is no modular reduction anywhere.

I will prove the stronger fact that all positive differences between distinct elements of \(T\) are distinct.

Lemma. Let \(A=\{a_1<\cdots<a_n\}\subset \mathbb Z\). If all positive differences \(a_j-a_i\) with \(i<j\) are distinct, then all sums \(a_i+a_j\) with \(i<j\) are distinct.

Proof. Suppose
$$
a_i+a_j=a_k+a_\ell,\qquad i<j,\ k<\ell.
$$
If \(\{i,j\}=\{k,\ell\}\), then because both pairs are written in increasing order, \((i,j)=(k,\ell)\), so there is no collision. Suppose instead that the two pairs are different. After swapping the two pairs if necessary, we may assume \(a_i<a_k\). Then
$$
a_\ell-a_j=a_k-a_i.
$$
The right-hand side is positive, so \(a_\ell>a_j\), and both sides are positive differences of elements of \(A\). These two differences come from different ordered pairs, namely \((a_i,a_k)\) and \((a_j,a_\ell)\), because \(a_i<a_k\). This contradicts the assumption that all positive differences are distinct. Therefore no such nontrivial sum collision exists. \(\square\)

So it is enough to check that the positive differences in \(T\) are all distinct. For each starting element of \(T\), the differences to the later elements are:

- \(0:\) \(1,33,83,104,110,124,163,185,200,203,249,251,258,314,318,343,356,386,430,440,456,464,475,487,492\).
- \(1:\) \(32,82,103,109,123,162,184,199,202,248,250,257,313,317,342,355,385,429,439,455,463,474,486,491\).
- \(33:\) \(50,71,77,91,130,152,167,170,216,218,225,281,285,310,323,353,397,407,423,431,442,454,459\).
- \(83:\) \(21,27,41,80,102,117,120,166,168,175,231,235,260,273,303,347,357,373,381,392,404,409\).
- \(104:\) \(6,20,59,81,96,99,145,147,154,210,214,239,252,282,326,336,352,360,371,383,388\).
- \(110:\) \(14,53,75,90,93,139,141,148,204,208,233,246,276,320,330,346,354,365,377,382\).
- \(124:\) \(39,61,76,79,125,127,134,190,194,219,232,262,306,316,332,340,351,363,368\).
- \(163:\) \(22,37,40,86,88,95,151,155,180,193,223,267,277,293,301,312,324,329\).
- \(185:\) \(15,18,64,66,73,129,133,158,171,201,245,255,271,279,290,302,307\).
- \(200:\) \(3,49,51,58,114,118,143,156,186,230,240,256,264,275,287,292\).
- \(203:\) \(46,48,55,111,115,140,153,183,227,237,253,261,272,284,289\).
- \(249:\) \(2,9,65,69,94,107,137,181,191,207,215,226,238,243\).
- \(251:\) \(7,63,67,92,105,135,179,189,205,213,224,236,241\).
- \(258:\) \(56,60,85,98,128,172,182,198,206,217,229,234\).
- \(314:\) \(4,29,42,72,116,126,142,150,161,173,178\).
- \(318:\) \(25,38,68,112,122,138,146,157,169,174\).
- \(343:\) \(13,43,87,97,113,121,132,144,149\).
- \(356:\) \(30,74,84,100,108,119,131,136\).
- \(386:\) \(44,54,70,78,89,101,106\).
- \(430:\) \(10,26,34,45,57,62\).
- \(440:\) \(16,24,35,47,52\).
- \(456:\) \(8,19,31,36\).
- \(464:\) \(11,23,28\).
- \(475:\) \(12,17\).
- \(487:\) \(5\).

This table has
$$
25+24+\cdots+1=\binom{26}{2}=325
$$
entries, which is exactly the number of positive differences \(t_j-t_i\) with \(i<j\). Hence every positive difference in \(T\) appears once in the display. A direct inspection of the full display shows that no value is repeated. Therefore all \(325\) positive differences are distinct.

By the lemma, all sums \(t_i+t_j\) with \(i<j\) are distinct, so \(T\) is a Sidon set. Since translation by \(+1\) preserves pair-sum collisions, \(S=T+1\) is also a Sidon set. This proves validity.

For the size claim, the elements of \(S\) are written in strictly increasing order,
$$
1<2<34<84<105<111<125<164<186<201<204<250<252<259<315<319<344<357<387<431<441<457<465<476<488<493\le 500.
$$
So there are no duplicates, and every element lies in \([1,500]\). Counting them as two blocks of \(13\),
$$
(1,2,34,84,105,111,125,164,186,201,204,250,252),
$$
$$
(259,315,319,344,357,387,431,441,457,465,476,488,493),
$$
gives
$$
|S|=13+13=26.
$$

Finally, let \(F(500)\) denote the maximum size of a Sidon subset of \([1,500]\). Since \(S\subseteq[1,500]\) is valid and has \(26\) elements,
$$
F(500)\ge 26.
$$
The previous literature lower bound was \(23\), so this is a strict improvement:
$$
F(500)\ge 26>23.
$$
Thus the displayed construction is valid, has exactly \(26\) elements, and improves the lower bound for `sidon_500` by \(3\).
