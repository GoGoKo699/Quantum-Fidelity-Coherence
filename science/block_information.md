# Exact information in one common-orientation block

This page computes the complete distinguishability of a block containing a fixed number of copies from each of two pure-state sources, after averaging their common orientation. The orientation average is an auxiliary statistical experiment. Its use for several blocks of a single fixed source pair requires the comparison argument in the [adaptive converse](adaptive_converse.md); the one-block result alone does not justify refreshing a fixed pair between runs. The underlying fixed-source and complete-reset assumptions are specified in the [model](model.md).

Let $`r,s`$ be nonnegative integers, $`n=r+s`$, and $`d\ge2`$. The parameter is the squared overlap $`f\in[0,1]`$, so the root fidelity is $`F=\sqrt f`$. When both source counts are positive, take $`r\le s`$ by relabeling the sources and set

```math
|\psi\rangle=|e_1\rangle,
\qquad
|\phi_f\rangle=\sqrt f\,|e_1\rangle+\sqrt{1-f}\,|e_2\rangle.
```

For Haar-distributed $`U\in U(d)`$, define

```math
\omega_f^{r,s}
=\int U^{\otimes n}
\left(|\psi\rangle\langle\psi|^{\otimes r}
\otimes|\phi_f\rangle\langle\phi_f|^{\otimes s}\right)
U^{\dagger\otimes n}\,dU.
\qquad\text{(1)}
```

The common-orientation twirl, its two-row Schur decomposition, and sufficiency of the Schur label were derived for this overlap problem by Fanizza et al. [F]. We give the multiplicity and Gram-matrix calculations explicitly because they yield an exact chi-square kernel and a global relative-entropy bound without an asymptotic or small-overlap restriction.

## 1. The permutation module on subsets

Write $`[n]=\{1,\ldots,n\}`$. Let $`\mathcal M_t`$ be the Hilbert space with an orthonormal basis $`|A\rangle`$ indexed by all $`t`$-element subsets of $`[n]`$. The symmetric group $`S_n`$ acts by permuting elements of the subsets. In particular,

```math
\dim\mathcal M_r=L=\binom nr.
```

We first prove its multiplicity-free decomposition and the dimensions that enter the probability formulas.

### Up and down operators

For $`0\le t<n`$, define

```math
U_t|A\rangle=\sum_{x\notin A}|A\cup\{x\}\rangle,
\qquad D_{t+1}=U_t^\dagger.
```

Set $`D_0=0`$. Counting diagonal terms and one-element replacements gives

```math
D_{t+1}U_t-U_{t-1}D_t=(n-2t)I_{\mathcal M_t}.
\qquad\text{(2)}
```

Indeed, the first product returns $`|A\rangle`$ in $`n-t`$ ways and the second in $`t`$ ways. Their off-diagonal entries both equal one for a single-element replacement and zero otherwise. When $`t<n/2`$, (2) implies

```math
\|U_tx\|^2=\|D_tx\|^2+(n-2t)\|x\|^2,
```

so $`U_t`$ is injective. Consequently $`D_k`$ is surjective for $`1\le k\le r\le n/2`$, and the harmonic subspace

```math
\mathcal H_k=\ker D_k
```

has dimension

```math
h_k=\binom nk-\binom n{k-1},
\qquad \binom n{-1}=0.
\qquad\text{(3)}
```

Lift $`\mathcal H_k`$ to $`\mathcal M_r`$ by the injective map
$`U_{r-1}\cdots U_k`$, with the identity map when $`k=r`$. Denote its image by $`\mathcal E_k`$. Repeated use of (2) shows that, for $`h\in\mathcal H_k`$ and $`r>k`$,

```math
D_rU_{r-1}\cdots U_k h
=(r-k)(n-r-k+1)U_{r-2}\cdots U_k h.
\qquad\text{(4)}
```

For example, the first step has coefficient $`n-2k`$. The induction step adds $`n-2t`$ to the previous coefficient when passing from level $`t`$ to $`t+1`$, giving
$`(t+1-k)(n-t-k)`$, which is (4) at $`r=t+1`$.

Let $`J_1`$ be the adjacency matrix on $`r`$-subsets for a single-element replacement. Since

```math
U_{r-1}D_r=rI+J_1,
```

the space $`\mathcal E_k`$ is an eigenspace of $`J_1`$, with eigenvalue

```math
\theta_k=(r-k)(s-k)-k.
\qquad\text{(5)}
```

For $`0\le k<r`$, $`\theta_k-\theta_{k+1}=n-2k>0`$. The spaces $`\mathcal E_k`$ are therefore mutually orthogonal. Their dimensions sum to

```math
\sum_{k=0}^r h_k=\binom nr=L,
```

so they exhaust $`\mathcal M_r`$.

### Irreducibility and partition labels

An operator commuting with all subset permutations has matrix entries constant on the orbits of ordered pairs $`(A,B)`$. Those orbits are indexed by
$`|A\setminus B|=0,\ldots,r`$. Thus the commutant of the $`S_n`$ action on $`\mathcal M_r`$ has dimension $`r+1`$.

The spaces $`\mathcal E_0,\ldots,\mathcal E_r`$ are $`r+1`$ nonzero invariant subspaces. For a finite-dimensional unitary representation with irreducible multiplicities $`m_\lambda`$, its commutant has dimension $`\sum_\lambda m_\lambda^2`$. Equality with $`r+1`$ therefore forces each $`\mathcal E_k`$ to be irreducible and forces the $`r+1`$ irreducibles to be pairwise inequivalent.

Their usual partition labels are $`(n-k,k)`$. One can identify the label directly. Choose $`k`$ disjoint pairs $`(a_i,b_i)`$ and form the nonzero vector in $`\mathcal M_k`$

```math
h=\prod_{i=1}^k\bigl(I-(a_i\ b_i)\bigr)
|\{a_1,\ldots,a_k\}\rangle.
\qquad\text{(6)}
```

Here $`(a_i\ b_i)`$ denotes the corresponding permutation action. This is the column-antisymmetrized tabloid, or polytabloid, for shape $`(n-k,k)`$, taking $`a_i`$ in the second row and $`b_i`$ above it. Also $`D_kh=0`$: for each term obtained by deleting the chosen element of one pair, the two choices in that pair cancel. The span of its permutations is the Specht module of that shape. It is contained in the already irreducible $`\mathcal H_k`$, so the two spaces coincide. Lifting preserves its representation type. We have proved

```math
\boxed{\mathcal M_r\cong
\bigoplus_{k=0}^r W_{(n-k,k)},
\qquad \dim W_{(n-k,k)}=h_k.}
\qquad\text{(7)}
```

The same conclusion also follows from the two-letter case of Young's rule; the argument above supplies the multiplicities and dimensions directly.

## 2. The physical Gram matrix and Schur probabilities

For every $`r`$-subset $`A`$, let $`|v_A(f)\rangle`$ be the physical tensor vector with $`|\psi\rangle`$ at positions in $`A`$ and $`|\phi_f\rangle`$ at the other positions. Define the intertwining map

```math
T_f:\mathcal M_r\longrightarrow(\mathbb C^d)^{\otimes n},
\qquad T_f|A\rangle=|v_A(f)\rangle.
```

It intertwines the two permutation actions because permuting tensor positions also permutes the source-label subset. Its Gram matrix is

```math
G_f=T_f^\dagger T_f,
\qquad
(G_f)_{A,B}=f^{|A\setminus B|}.
\qquad\text{(8)}
```

There are $`|A\setminus B|`$ factors of $`\langle\psi|\phi_f\rangle`$ and the same number of their conjugates. This also proves that (8) holds for any representatives with squared overlap $`f`$, irrespective of their relative phase.

For $`0\le j\le r`$, let $`J_j`$ have entry one when $`|A\setminus B|=j`$, and zero otherwise. Then

```math
G_f=\sum_{j=0}^r f^jJ_j,
\qquad J_0=I.
\qquad\text{(9)}
```

Because $`G_f`$ commutes with permutations and (7) is multiplicity-free, $`G_f`$ acts as a scalar $`R_k(f)`$ on $`\mathcal E_k`$. Let $`E_k`$ be that subspace's orthogonal projector. Its diagonal entries are equal by transitivity of the subset action, and their sum is $`h_k`$, so

```math
\langle A|E_k|A\rangle=h_k/L
\quad\text{for every }A.
\qquad\text{(10)}
```

Let $`\Pi_k`$ be the physical Schur projector for the partition $`(n-k,k)`$. Intertwining gives $`\Pi_kT_f=T_fE_k`$. Thus the Schur probability for any fixed source placement $`A_0`$ is

```math
\begin{aligned}
p_k(f)
&=\|\Pi_kT_f|A_0\rangle\|^2\\
&=\langle A_0|E_kG_fE_k|A_0\rangle
=\frac{h_k}{L}R_k(f).
\end{aligned}
\qquad\text{(11)}
```

These are also the Schur probabilities of $`\omega_f^{r,s}`$, since the projectors commute with the common unitary. At $`f=0`$, all the physical vectors in (8) are orthonormal, so $`G_0=I`$ and

```math
\boxed{p_k(0)=h_k/L>0.}
\qquad\text{(12)}
```

### An explicit form of each eigenvalue

Although the kernel calculation below does not require individual eigenvalues, they can be obtained without diagonalizing a matrix. Lift the vector (6) to
$`w=U_{r-1}\cdots U_kh`$. Its coefficient at an $`r`$-subset $`A`$ is

```math
w(A)=(r-k)!\prod_{i=1}^k
\bigl(\mathbf1_{a_i\in A}-\mathbf1_{b_i\in A}\bigr).
\qquad\text{(13)}
```

Choose $`A_0`$ to contain every $`a_i`$, no $`b_i`$, and $`r-k`$ further elements. Then $`w(A_0)=(r-k)!`$. To calculate $`(G_fw)(A_0)`$, only subsets $`B`$ selecting exactly one element of each pair contribute. Selecting $`b_i`$ instead of $`a_i`$ changes the coefficient's sign and adds one to the subset distance, so summing these choices gives $`(1-f)^k`$.

Of the $`n-2k`$ unpaired elements, $`r-k`$ belong to $`A_0`$ and $`s-k`$ do not. A distance $`j`$ on these remaining elements can be obtained in
$`\binom{r-k}{j}\binom{s-k}{j}`$ ways. Dividing by $`w(A_0)`$ therefore gives

```math
\boxed{R_k(f)=(1-f)^k
\sum_{j=0}^{r-k}\binom{r-k}{j}\binom{s-k}{j}f^j.}
\qquad\text{(14)}
```

The formula includes $`k=0`$ and $`k=r`$, with the usual empty-product convention. At $`f=1`$, it is understood by continuity. For balanced counts $`r=s=m`$, put $`J=m-k`$; (14) becomes the polynomial form of the two-row overlap distribution in [F].

## 3. Why the Schur label contains all the block information

Schur–Weyl decomposition writes the full tensor space as

```math
(\mathbb C^d)^{\otimes n}
\cong\bigoplus_{\lambda:\ell(\lambda)\le d}
V_\lambda^{(d)}\otimes W_\lambda,
\qquad\text{(15)}
```

where common unitaries act on $`V_\lambda^{(d)}`$, and permutations act on $`W_\lambda`$. Let $`H=S_r\times S_s`$ be the subgroup preserving the two source blocks. The input vector is fixed by $`H`$. The module $`\mathcal M_r`$ is the permutation module on the cosets of $`H`$, namely $`\mathrm{Ind}_H^{S_n}\mathbf1`$. Frobenius reciprocity and (7) therefore give

```math
\dim W_\lambda^H=
\begin{cases}
1,&\lambda=(n-k,k),\ 0\le k\le r,\\
0,&\text{otherwise}.
\end{cases}
\qquad\text{(16)}
```

Choose a unit vector $`|\eta_k\rangle`$ in this one-dimensional invariant subspace. Its choice depends on the known placement of the source blocks, not on $`f`$. Each sector of the input vector consequently has the form
$`|\xi_k(f)\rangle\otimes|\eta_k\rangle`$, where
$`\|\xi_k(f)\|^2=p_k(f)`$.

Haar averaging removes cross terms between inequivalent unitary irreducibles and replaces an operator within $`V_{(n-k,k)}^{(d)}`$ by its trace times the normalized identity. With
$`D_k^{(d)}=\dim V_{(n-k,k)}^{(d)}`$, this gives

```math
\boxed{\omega_f^{r,s}=\bigoplus_{k=0}^r p_k(f)\tau_k,
\qquad
\tau_k=\frac{I_{V_{(n-k,k)}^{(d)}}}{D_k^{(d)}}
\otimes|\eta_k\rangle\langle\eta_k|.}
\qquad\text{(17)}
```

The states $`\tau_k`$ have mutually orthogonal supports and are independent of $`f`$. All these sectors exist for $`d\ge2`$. The dimension $`D_k^{(d)}`$ in (17) is the unitary-irrep dimension, whereas $`h_k`$ in (3) is the symmetric-group-irrep dimension; they play different roles.

For any POVM $`\{M_y\}`$, define

```math
Q(y\mid k)=\mathrm{tr}(M_y\tau_k).
```

This is a stochastic kernel independent of $`f`$, and its output law on (17) is

```math
\Pr_f\{Y=y\}=\sum_k Q(y\mid k)p_k(f).
\qquad\text{(18)}
```

For a general outcome space, use the Markov kernel
$`Q(dy\mid k)=\mathrm{tr}(M(dy)\tau_k)`$. The same argument then uses integrals instead of sums over outcomes.

A fixed source-independent ancilla, arbitrary within-block operations, and their final classical transcript can all be incorporated into an effective POVM on the block. Equation (18) therefore proves statistical sufficiency for every such operation, not only invariant measurements.

There is also no loss in replacing the quantum relative entropy by the classical one. Since the normalized sector states in (17) are the same for both parameters,

```math
D(\omega_f^{r,s}\|\omega_0^{r,s})
=D(p(f)\|p(0)).
\qquad\text{(19)}
```

On sector $`k`$, the log-likelihood difference is the scalar
$`\log p_k(f)-\log p_k(0)`$; the terms involving $`D_k^{(d)}`$ cancel. All logarithms here and below are natural logarithms, and relative-entropy sums use the convention $`0\log0=0`$.

## 4. Exact chi-square kernel

**Theorem 1 (block kernel).** For all $`f,g\in[0,1]`$,

```math
\boxed{\sum_{k=0}^r\frac{p_k(f)p_k(g)}{p_k(0)}
=\sum_{j=0}^r\binom rj\binom sj(fg)^j.}
\qquad\text{(20)}
```

**Proof.** Equations (11)–(12) and the common spectral decomposition of the Gram matrices give

```math
\sum_k\frac{p_k(f)p_k(g)}{p_k(0)}
=\frac1L\sum_k h_kR_k(f)R_k(g)
=\frac1L\mathrm{tr}(G_fG_g).
\qquad\text{(21)}
```

Every $`J_j`$ is a real symmetric matrix. Its row sum is

```math
v_j=\binom rj\binom sj,
```

because one chooses $`j`$ elements to remove from an $`r`$-subset and $`j`$ elements to add from its $`s`$-element complement. Distinct $`J_i,J_j`$ have disjoint matrix supports, so

```math
\mathrm{tr}(J_iJ_j)
=\sum_{A,B}(J_i)_{A,B}(J_j)_{B,A}
=L v_j\,\mathbf1_{i=j}.
\qquad\text{(22)}
```

Substitute (9) in (21) and apply (22) to obtain (20). $`\square`$

Using
$`\chi^2(p\|q)=\sum_k(p_k-q_k)^2/q_k`$, (20) at $`g=f`$ yields

```math
\boxed{1+\chi^2(p(f)\|p(0))
=\sum_{j=0}^r\binom rj\binom sj f^{2j}.}
\qquad\text{(23)}
```

In particular, the leading nonconstant term is $`rsf^2`$. The identity remains valid at $`f=1`$: the distribution is supported entirely on the fully symmetric sector, and both sides equal $`\binom nr`$ by Vandermonde's identity. Neither (20) nor (23) has a hidden dimension-dependent factor.

## 5. A global relative-entropy bound

**Corollary 2.** For every $`f\in[0,1]`$,

```math
\boxed{D(\omega_f^{r,s}\|\omega_0^{r,s})
=D(p(f)\|p(0))\le rsf^2.}
\qquad\text{(24)}
```

The same upper bound holds for the relative entropy between the outcomes of any common block POVM.

**Proof.** Jensen's inequality under the law $`p(f)`$ gives

```math
\begin{aligned}
D(p(f)\|p(0))
&=\mathbb E_{k\sim p(f)}
\log\frac{p_k(f)}{p_k(0)}\\
&\le\log\sum_k\frac{p_k(f)^2}{p_k(0)}
=\log\bigl(1+\chi^2(p(f)\|p(0))\bigr).
\end{aligned}
\qquad\text{(25)}
```

Zero-probability terms are omitted from this expectation. The denominator is positive by (12). For every integer $`j\ge0`$,

```math
\binom rj\binom sj
\le\frac{(rs)^j}{(j!)^2}
\le\frac{(rs)^j}{j!}.
```

Consequently (23) is at most $`\exp(rsf^2)`$. Taking the logarithm in (25) proves (24), using (19). Classical or quantum data processing proves the POVM statement. $`\square`$

If $`r=0`$ or $`s=0`$, the twirl contains copies from only one source and is independent of $`f`$. Its divergence is zero, consistent with (24). Thus the corollary extends to all nonnegative source counts.

With total variation defined as one half of the $`\ell_1`$ distance, Pinsker's inequality also gives

```math
\mathrm{TV}(P_f,P_0)\le f\sqrt{rs/2}
\qquad\text{(26)}
```

for every block outcome distribution. Since $`f=F^2`$, the entropy bound is $`rsF^4`$ in the root-fidelity parameter. Crucially, (24) is global: it does not assume that $`rf`$, $`sf`$, or $`rsf^2`$ is small.

## 6. Adaptive use in the refreshed experiment

Here is the direct chain-rule consequence, with its allocation assumption stated explicitly. Suppose each block receives a fresh independent common Haar orientation. From the previous classical transcript $`h`$, a protocol chooses nonnegative source counts $`r_t(h),s_t(h)`$, with

```math
r_t(h)+s_t(h)\le b,
```

and then applies any POVM to that fixed stock. Assume the total chosen stock is at most $`N`$ along every transcript. Counts and measurements may depend arbitrarily on earlier blocks, but the stock for a block is fixed before observing that block.

Conditional on $`h`$, (24) and data processing bound the next outcome divergence by
$`r_t(h)s_t(h)f^2`$. The relative-entropy chain rule therefore gives

```math
\begin{aligned}
D(P_f^{\mathrm{fresh}}\|P_0^{\mathrm{fresh}})
&\le f^2\,\mathbb E_f\sum_t r_t s_t\\
&\le \frac{bf^2}{4}\,\mathbb E_f\sum_t(r_t+s_t)\\
&\le\frac{Nb f^2}{4}.
\end{aligned}
\qquad\text{(27)}
```

The middle inequality uses
$`rs\le(r+s)^2/4\le b(r+s)/4`$. Early stopping can be padded with deterministic zero-copy outcomes, which add no divergence. Thus

```math
\mathrm{TV}(P_f^{\mathrm{fresh}},P_0^{\mathrm{fresh}})
\le f\sqrt{Nb/8}.
\qquad\text{(28)}
```

If the source allocation itself is chosen adaptively during a block, its final counts cannot simply be inserted into (24). Such an operation is instead bounded by first supplying a sufficient fixed stock and using data processing; the unused copies are discarded. For example, any operation that consumes fewer than $`2b`$ copies in total can be simulated using $`2b`$ presupplied copies from each source. Its refreshed-block divergence is then at most $`4b^2f^2`$, independently of its internal source choices, intermediate measurements, or stopping rule.

Equations (27)–(28) concern independent orientations across blocks. In the physical fixed-source problem, earlier outcomes can reveal the common orientation. The [adaptive converse](adaptive_converse.md) controls that information and uses fixed-stock superblocks to handle adaptive source choices and run lengths.

## References

**[F]** M. Fanizza, M. Rosati, M. Skotiniotis, J. Calsamiglia, and V. Giovannetti, *Beyond the Swap Test: Optimal Estimation of Quantum State Overlap*, Physical Review Letters **124**, 060503 (2020). [Primary manuscript, arXiv:1906.10639v3](https://arxiv.org/pdf/1906.10639). Eqs. (6)–(7) give the twirled overlap state and Schur distribution; the supplementary representation-theory and fixed-overlap sections derive their structure. Grouping the optimal measurement is already proposed in the main text and supplementary Eq. (130).

**[K]** H. Krovi, *An efficient high dimensional quantum Schur transform*, Quantum **3**, 122 (2019). [Published article](https://doi.org/10.22331/q-2019-02-14-122); [primary manuscript, arXiv:1804.00055v2](https://arxiv.org/pdf/1804.00055). Sections 2.6–2.7 give Schur–Weyl and permutation-module conventions; the proof above specializes the subset module and makes the multiplicity calculation explicit.
