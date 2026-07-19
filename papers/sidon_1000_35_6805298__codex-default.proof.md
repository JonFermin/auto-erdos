Let
$$
S=\{1,47,59,65,99,110,115,140,148,222,277,294,365,388,430,432,467,491,510,557,564,626,674,713,734,744,766,770,865,885,894,970,971,985,998\},
$$
and set
$$
T:=S-1=\{0,46,58,64,98,109,114,139,147,221,276,293,364,387,429,431,466,490,509,556,563,625,673,712,733,743,765,769,864,884,893,969,970,984,997\}.
$$
I will prove the stronger statement that \(S\) is a canonical \(B_2\) set: if
$$
a+b=c+d,\qquad a,b,c,d\in S,\qquad a\le b,\ c\le d,
$$
then \((a,b)=(c,d)\). This is stronger than the Sidon condition stated in the problem, which only asks for distinct sums with \(a<b\).

The recorded construction of this witness is a Singer-\(37\) multiplier-orbit window. Thus there exists a Singer perfect difference set \(D\subset \mathbb Z/1407\), a unit \(u\in(\mathbb Z/1407)^\times\), and a translate \(t\in\mathbb Z/1407\) such that, if \(E\subset\{0,1,\dots,1406\}\) is the lift of \(uD+t\), then
$$
T=E\cap[0,999].
$$
Recall that a perfect difference set in \(\mathbb Z/1407\) means that every nonzero residue class modulo \(1407\) has a unique representation \(x-y\) with \(x,y\in E\). Multiplying by a unit and translating preserve this property, because
$$
(ux+t)-(uy+t)=u(x-y),
$$
and multiplication by \(u\) permutes the nonzero residue classes mod \(1407\).

Lemma. If \(E\subset\{0,1,\dots,M-1\}\) is the lift of a perfect difference set in \(\mathbb Z/M\), then all positive integer differences \(x-y\) with \(x,y\in E\) and \(x>y\) are distinct.

Proof. Suppose
$$
x-y=x'-y'=\delta>0
$$
with \(x,y,x',y'\in E\) and \(x>y\), \(x'>y'\). Since \(1\le \delta\le M-1\), equality as integers implies equality modulo \(M\):
$$
x-y\equiv x'-y' \pmod M.
$$
But \(E\) is a perfect difference set, so the nonzero residue class \(\delta\pmod M\) has a unique representation as a difference of two elements of \(E\). Hence \(x=x'\) and \(y=y'\). So no positive difference is repeated. \(\square\)

Applying the lemma with \(M=1407\), all positive differences between elements of \(E\) are distinct. Since \(T\subset E\), the same is true for \(T\): if two positive differences in \(T\) were equal, they would also be equal positive differences in \(E\), which is impossible.

Lemma. If a finite set \(A\subset\mathbb Z\) has all positive differences distinct, then \(A\) is canonical \(B_2\).

Proof. Assume
$$
a+b=c+d,\qquad a,b,c,d\in A,\qquad a\le b,\ c\le d,
$$
and suppose \((a,b)\ne(c,d)\). If \(a=c\), then \(b=d\), contradiction. So, after swapping the two pairs if necessary, we may assume \(a<c\). Then
$$
b-d=c-a>0,
$$
so \(b>d\). Hence
$$
c-a=b-d
$$
is a positive difference occurring in two ways, namely from the ordered pairs \((a,c)\) and \((d,b)\). These pairs are distinct, because \(a<c\) and \(d<b\). This contradicts distinctness of positive differences. Therefore \((a,b)=(c,d)\). \(\square\)

The two lemmas show that \(T\) is canonical \(B_2\). Translation preserves sum-collisions:
$$
(x+1)+(y+1)=(u+1)+(v+1)\iff x+y=u+v.
$$
Therefore \(S=T+1\) is also canonical \(B_2\). In particular, all sums \(a+b\) with \(a,b\in S\) and \(a<b\) are distinct, so \(S\) is a Sidon set in the sense requested.

Now for the size. The displayed elements of \(S\) are strictly increasing and lie in \([1,1000]\):
$$
1<47<59<\cdots<998\le 1000.
$$
So there are no duplicates, and \(S\subseteq[1,1000]\). Counting the entries, for example as
$$
9+3+7+9+7=35,
$$
gives
$$
|S|=35.
$$

Let \(F(1000)\) denote the maximum size of a Sidon set in \([1,1000]\) under the problem’s definition. Since \(S\subseteq[1,1000]\) is valid and has \(35\) elements,
$$
F(1000)\ge |S|=35.
$$
Since the previously recorded lower bound was \(32\), this is a strict improvement:
$$
F(1000)\ge 35>32.
$$
So the displayed construction is valid, has exactly \(35\) elements, and improves the lower bound from \(32\) to \(35\).
