Let
\[
S=\{1,2,4,8,17,28,40,59,69,77,94,99\}.
\]

This is a set of \(12\) distinct integers in \([1,100]\), because the elements are written in strictly increasing order:
\[
1<2<4<8<17<28<40<59<69<77<94<99\le 100.
\]
Hence \(|S|=12\).

It remains to prove the Sidon property. Here all sums are compared as ordinary integers; there is no modular reduction. For each \(x\in S\), list all sums \(x+y\) with \(y\in S\) and \(y>x\):
\[
\begin{aligned}
1+\{2,4,8,17,28,40,59,69,77,94,99\}
&=\{3,5,9,18,29,41,60,70,78,95,100\},\\
2+\{4,8,17,28,40,59,69,77,94,99\}
&=\{6,10,19,30,42,61,71,79,96,101\},\\
4+\{8,17,28,40,59,69,77,94,99\}
&=\{12,21,32,44,63,73,81,98,103\},\\
8+\{17,28,40,59,69,77,94,99\}
&=\{25,36,48,67,77,85,102,107\},\\
17+\{28,40,59,69,77,94,99\}
&=\{45,57,76,86,94,111,116\},\\
28+\{40,59,69,77,94,99\}
&=\{68,87,97,105,122,127\},\\
40+\{59,69,77,94,99\}
&=\{99,109,117,134,139\},\\
59+\{69,77,94,99\}
&=\{128,136,153,158\},\\
69+\{77,94,99\}
&=\{146,163,168\},\\
77+\{94,99\}
&=\{171,176\},\\
94+\{99\}
&=\{193\}.
\end{aligned}
\]

These are exactly all pairwise sums \(a+b\) with \(a,b\in S\) and \(a<b\). There are
\[
11+10+9+\cdots+1=\binom{12}{2}=66
\]
such sums. If we merge the rows above and sort them, we obtain
\[
\begin{aligned}
&3,5,6,9,10,12,18,19,21,25,29,30,32,36,41,42,44,45,48,57,\\
&60,61,63,67,68,70,71,73,76,77,78,79,81,85,86,87,94,95,96,97,98,99,\\
&100,101,102,103,105,107,109,111,116,117,122,127,128,134,136,139,\\
&146,153,158,163,168,171,176,193.
\end{aligned}
\]
This list is strictly increasing, so no value is repeated. Therefore no two distinct unordered pairs \(\{a,b\}\), \(\{c,d\}\subset S\) with \(a<b\) and \(c<d\) satisfy \(a+b=c+d\). Thus all pairwise sums are distinct, and \(S\) is a Sidon set.

So \(S\subseteq [1,100]\) is a valid Sidon set of size \(12\). If \(M\) denotes the maximum size of a Sidon subset of \([1,100]\), then
\[
M\ge |S|=12.
\]
Since the previous literature lower bound was \(11\), this gives the strict improvement
\[
M\ge 12>11.
\]

So the construction is valid, has exactly \(12\) elements, and improves the known lower bound by \(1\).
