# A bounded-run estimator for root fidelity

Let two sources supply independent copies of fixed unknown pure states
$\rho=|\psi\rangle\langle\psi|$ and
$\sigma=|\phi\rangle\langle\phi|$ in $\mathbb C^d$, with $d\ge2$.
Write

$$
f=\operatorname{tr}(\rho\sigma)=|\langle\psi|\phi\rangle|^2,
\qquad F=\sqrt f.
$$

Every supplied copy is charged. A coherent run may consume at most $b$ copies in total, and all source-dependent quantum systems are discarded or reset before the next run. The complete source and reset contract is given in the [model](model.md). The construction below uses fixed runs and retains only a classical sum between them. It needs no classical state description, preparation unitary, inverse preparation, reflection about either state, or QRAM.

The collective Schur measurement and its repetition on groups of copies are inherited from Fanizza et al. [F], including their explicit grouped-measurement proposal and supplementary Eq. (130). This page derives a uniform finite-sample root-fidelity guarantee and accounts for numerical and circuit approximation. The unrestricted $\Theta(\epsilon^{-2})$ sample endpoint is already established by Wang and Zhang [W].

## 1. The observable measured in one run

Fix an integer $m\ge1$. A run receives $m$ copies of each source, in the state

$$
\rho^{\otimes m}\otimes\sigma^{\otimes m}.
$$

For tensor registers $a,b$, let $S_{a,b}$ be their swap operator. Define the Hermitian observable

$$
A_m=\frac1{m^2}\sum_{i=1}^m\sum_{j=1}^m S_{i,m+j}.
\tag{1}
$$

Its expectation is

$$
\mathbb E A_m=f.
\tag{2}
$$

Equation (1) denotes a measurement of the sum as one observable. The cross swaps need not commute, so measuring them separately would not implement this measurement.

### Exact variance

Expand $A_m^2$ as a sum over ordered pairs of cross swaps. There are three cases.

| Ordered pair of cross swaps | Number of terms | Expectation of their product |
| --- | ---: | ---: |
| The same swap twice | $m^2$ | $1$ |
| Exactly one common register | $2m^2(m-1)$ | $f$ |
| No common register | $m^2(m-1)^2$ | $f^2$ |

The first case uses $S_{a,b}^2=I$. In the second case, the product is a three-cycle. Its expectation is either $\operatorname{tr}(\rho^2\sigma)$ or $\operatorname{tr}(\rho\sigma^2)$, both equal to $f$ because the states are pure. In the third case the two swaps act on disjoint tensor factors, so the expectation factors. The counts sum to $m^4$, the number of ordered pairs.

Consequently,

$$
\mathbb E A_m^2
=\frac{1+2(m-1)f+(m-1)^2f^2}{m^2},
$$

and hence

$$
\boxed{\operatorname{Var}(A_m)
=\frac{1+2(m-1)f-(2m-1)f^2}{m^2}
\le \frac1{m^2}+\frac{2f}{m}.}
\tag{3}
$$

At orthogonal inputs the variance is exactly $m^{-2}$. At identical inputs it is zero. The $m^{-2}$ term near $f=0$ is the feature needed for uniform estimation of $\sqrt f$.

### Schur labels and the measured eigenvalue

The input is supported on

$$
\mathcal K_m=\operatorname{Sym}^m(\mathbb C^d)
\otimes\operatorname{Sym}^m(\mathbb C^d).
$$

The Schur sectors occurring in this subspace have two-row shapes

$$
\lambda_J=(m+J,m-J),\qquad J=0,1,\ldots,m.
$$

The multiplicity statement is proved in [Exact block information](block_information.md). Weak Schur sampling means measuring this partition label, without resolving the remaining representation registers.

To determine the value of $A_m$, introduce the central sum of all transpositions on $2m$ registers,

$$
C_{2m}=\sum_{1\le a<b\le2m}S_{a,b}.
$$

On a Schur sector of shape $\lambda$, its eigenvalue is the sum of box contents,

$$
c_\lambda=\sum_{(i,j)\in\lambda}(j-i)
=\frac12\sum_i\lambda_i(\lambda_i-2i+1).
$$

For the displayed two-row shape this gives

$$
\begin{aligned}
c_{\lambda_J}
&=\frac{(m+J)(m+J-1)+(m-J)(m-J-3)}2\\
&=m^2-2m+J(J+1).
\end{aligned}
$$

Each within-source swap is the identity on $\mathcal K_m$. The sum of the within-source transpositions therefore has eigenvalue
$2\binom m2=m^2-m$. Subtracting it from $C_{2m}$ leaves exactly the cross-swap sum in (1). Thus weak Schur sampling measures $A_m$ by returning the score

$$
\boxed{a_J=\frac{J(J+1)-m}{m^2}.}
\tag{4}
$$

In particular, $-1/m\le a_J\le1$. A negative score is a valid outcome of the unbiased observable; clipping is performed only after averaging runs. Since Schur projectors commute with every common unitary $U^{\otimes2m}$, the construction works for each fixed pair of source states and does not require physically randomizing their orientation.

## 2. A uniform conversion from squared overlap to root fidelity

Perform $K$ independent runs of the measurement in (4). Let $X_t$ be the score in run $t$, and set

$$
\overline X=\frac1K\sum_{t=1}^KX_t,
\qquad
\widehat F=\sqrt{\Pi_{[0,1]}(\overline X)},
\tag{5}
$$

where $\Pi_{[0,1]}$ clips a real number to $[0,1]$.

**Lemma 1 (uniform square-root error).** For every $0<\eta\le1$ and every $f\in[0,1]$,

$$
\Pr\{|\widehat F-\sqrt f|>\eta\}
\le\frac1{Km^2\eta^4}+\frac2{Km\eta^2}.
\tag{6}
$$

**Proof.** First, for any real $x$,

$$
\left|\sqrt{\Pi_{[0,1]}(x)}-\sqrt f\right|>\eta
\quad\Longrightarrow\quad
|x-f|>\eta\max\{\sqrt f,\eta\}.
\tag{7}
$$

To see this, suppose $f\ge\eta^2$. An upper root error requires an increase in the clipped squared value of more than
$2\eta\sqrt f+\eta^2$, which is at least $\eta\sqrt f$.
A lower root error, when possible, requires a decrease of more than
$2\eta\sqrt f-\eta^2\ge\eta\sqrt f$.
If $f<\eta^2$, a lower root error is impossible, and an upper root error requires an increase greater than $\eta^2$.
Finally, clipping cannot increase the distance from $f\in[0,1]$, so the same lower bound applies to $|x-f|$.

Independence of the runs and (3) give

$$
\operatorname{Var}(\overline X)
\le\frac1{Km^2}+\frac{2f}{Km}.
$$

Apply Chebyshev's inequality at the threshold in (7):

$$
\begin{aligned}
\Pr\{|\widehat F-\sqrt f|>\eta\}
&\le
\frac{1/(Km^2)+2f/(Km)}{\eta^2\max\{f,\eta^2\}}\\
&\le\frac1{Km^2\eta^4}+\frac2{Km\eta^2}.
\end{aligned}
$$

This bound includes $f=0$; no division by the unknown root fidelity is used. $\square$

The lower-tail threshold in (7) is essential. The expression
$\eta^2+2\eta\sqrt f$ is an upper-tail squared displacement and cannot be used as a symmetric threshold.

## 3. A fully specified finite-precision algorithm

**Theorem 2 (bounded-run upper bound).** Let $d\ge2$, let $b\ge2$ be an integer, and let $0<\epsilon\le1/8$. There is an algorithm that consumes at most $b$ source copies in each run and returns a finite binary number $\widetilde F$ such that, for every fixed pair of pure states,

$$
\Pr\{|\widetilde F-F|\le\epsilon\}\ge\frac34.
$$

Its worst-case total number of supplied copies satisfies

$$
\boxed{N\le\frac{160}{\epsilon^2}
+\frac{576}{b\epsilon^4}.}
\tag{8}
$$

The constants leave room for both numerical rounding and circuit synthesis. They are not optimized. The complementary lower bounds, including fully adaptive runs, are proved in the [adaptive converse](adaptive_converse.md).

**Algorithm and proof.** Set

$$
\eta=\epsilon/2,
\qquad
m=\min\left\{\left\lfloor\frac b2\right\rfloor,
\left\lceil\eta^{-2}\right\rceil\right\},
\qquad
K=\left\lceil\frac6{m^2\eta^4}+\frac{12}{m\eta^2}\right\rceil.
\tag{9}
$$

Acquire exactly $m$ copies of each source per run. Measure the Schur label, retain its integer score numerator $J(J+1)-m$, and discard all quantum registers before acquiring the next run's copies. For ideal measurements, (6) and the choice of $K$ give failure probability at most $1/6$ at root error $\eta$.

It suffices that the implemented outcome distribution in each run is within total variation

$$
\delta=\frac1{12K}
\tag{10}
$$

of the ideal Schur-label distribution. Replacing the runs one at a time changes the joint label distribution by at most $K\delta=1/12$. Deterministic classical postprocessing cannot increase this distance. Thus the implemented exact-arithmetic value in (5) exceeds root error $\eta$ with probability at most $1/6+1/12=1/4$.

All score arithmetic can be exact. Maintain the integer

$$
Z=\sum_{t=1}^KJ_t(J_t+1),
\qquad
\overline X=\frac{Z-Km}{Km^2}.
\tag{11}
$$

After clipping this rational value, compute its square root to absolute error at most $\eta$. For example, binary bisection with exact integer comparisons gives a lower binary approximation with

$$
q=\left\lceil\log_2(2/\epsilon)\right\rceil
$$

fractional bits and error at most $2^{-q}\le\eta$. The triangle inequality then gives the claimed $\epsilon$ error and success probability.

There are exactly $N=2mK$ source copies, $mK$ from each source. In particular, the budget is a deterministic worst-case bound. Since $2m\le b$, every run obeys the required cap. The ceiling in (9) gives

$$
N\le2m+\frac{12}{m\eta^4}+\frac{24}{\eta^2}.
\tag{12}
$$

For integer $b\ge2$, $\lfloor b/2\rfloor\ge b/3$. Also
$m\le\lceil\eta^{-2}\rceil\le2\eta^{-2}$, and

$$
\frac1m
=\max\left\{\frac1{\lfloor b/2\rfloor},
\frac1{\lceil\eta^{-2}\rceil}\right\}
\le\frac3b+\eta^2.
$$

Substitution in (12) yields

$$
N\le\frac{40}{\eta^2}+\frac{36}{b\eta^4}
=\frac{160}{\epsilon^2}+\frac{576}{b\epsilon^4},
$$

proving (8). Capping $m$ at $\lceil\eta^{-2}\rceil$ prevents an unnecessarily large allowed $b$ from forcing extra copies. $\square$

## 4. Gate, workspace, and precision account

Assume each supplied $d$-dimensional register is encoded in
$\ell=\lceil\log_2d\rceil$ qubits with known computational-basis encoding. This specifies how source registers are manipulated; it supplies no circuit for preparing their unknown states. One can embed them in dimension $2^\ell$, since the Schur-label projectors are central permutation projectors and restrict to the same projectors on the original tensor subspace.

Krovi's Theorem 3 [K] implements the Schur transform on $n$ such registers with an elementary-gate count polynomial in $n$, $\log d$, and $\log(1/\xi)$. Section 3.1 of that paper specifies $\xi$ as operator-norm approximation error. Measuring the partition output implements weak Schur sampling. This is an inherited implementation result; no new transform synthesis is needed here.

For completeness, suppose ideal and implemented transforms satisfy
$\|S-\widetilde S\|_{\mathrm{op}}\le\xi$, including their initialized ancillas. For every input state $\tau$, the triangle inequality and unitary invariance of the trace norm give

$$
\|S\tau S^\dagger-\widetilde S\tau\widetilde S^\dagger\|_1
\le2\xi.
$$

Measurement therefore produces distributions at total variation distance at most $\xi$. Taking $\xi=1/(24K)$ is sufficient for (10). An output label outside the valid two-row set can be assigned $J=0$; this is a deterministic postprocessing whose ideal probability of being used is zero and whose error is already covered by the same distance bound.

Thus the resource bounds, with $m,K$ as in (9), are as follows.

| Resource | Bound |
| --- | --- |
| Total source copies | Exactly $2mK$, bounded by (8) |
| Copies consumed before a reset | Exactly $2m\le b$ |
| Source registers held in a run | $2m\ell$ qubits |
| Additional initialized workspace | $\operatorname{poly}(m,\ell,\log K)$ qubits suffice |
| Elementary quantum gates in all runs | $K\operatorname{poly}(m,\ell,\log K)$ |
| Classical record retained between runs | $O(\log K+\log m)$ bits for the score sum and counters |
| Output precision | $q=O(\log\epsilon^{-1})$ fractional bits |

The workspace bound follows, conservatively, by allocating at most polynomially many qubits to the inherited polynomial-size circuit. Score updates and the final square root require polynomial classical bit operations in $K$, $\log m$, and $\log\epsilon^{-1}$. All workspace carrying source information is reset with its run. Neither a small persistent quantum register nor additional source copies are hidden in the implementation.

These are computational gate and synthesis-precision bounds in an ideal universal gate model. They do not assert gate optimality or a device-noise tolerance theorem. In particular, the sample theorem's resource $b$ measures total copies consumed before reset, rather than a bound on the number of qubits simultaneously stored.

## References

**[F]** M. Fanizza, M. Rosati, M. Skotiniotis, J. Calsamiglia, and V. Giovannetti, *Beyond the Swap Test: Optimal Estimation of Quantum State Overlap*, Physical Review Letters **124**, 060503 (2020). [Primary manuscript, arXiv:1906.10639v3](https://arxiv.org/pdf/1906.10639). The collective measurement and its sufficiency appear in Eqs. (6)–(7); grouped measurements appear in the main-text gate-complexity discussion and supplementary Eq. (130).

**[K]** H. Krovi, *An efficient high dimensional quantum Schur transform*, Quantum **3**, 122 (2019). [Published article](https://doi.org/10.22331/q-2019-02-14-122); [primary manuscript, arXiv:1804.00055v2](https://arxiv.org/pdf/1804.00055). See Theorem 3 and Section 3.1 for the dimension-efficient gate bound and precision convention.

**[W]** Q. Wang and Z. Zhang, *Sample-Optimal Quantum Estimators for Pure-State Trace Distance and Fidelity via Samplizer*, ICALP 2026, LIPIcs **374**, Article 154. [Primary full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.154/LIPIcs.ICALP.2026.154.html); [arXiv:2410.21201](https://arxiv.org/abs/2410.21201). Theorem 1 states the unrestricted pure-state root-fidelity upper bound; Section 8 discusses sample optimality.
