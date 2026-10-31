# Comparing fixed and refreshed Haar orientations

This section proves the transcript comparison needed for fixed unknown sources. A common Haar unitary is sampled once in the physical hard-instance experiment. Replacing it by independent Haar unitaries at successive reset boundaries defines a different, auxiliary experiment. The theorem below bounds the difference between those experiments for every permitted adaptive measurement strategy.

The argument combines an exact Haar–Gaussian polynomial norm comparison with the classical homogeneous Bombieri product inequality. One-sided likelihood comparison for adaptive measurements has precedent in the Haar-assembled-ensemble setting of Ye, Liu and Deng [4, Theorem 29]. We give the common-unitary proof, including its normalization and measurement-theoretic details.

## 1. Statement and operational setting

Fix integers $`d\ge 2`$, $`b\ge 1`$, and $`K\ge 1`$. Write

```math
\begin{aligned}
t&=4b,\qquad M=Kt,\qquad 0\le f\le1,\\
v_f&=e_1^{\otimes 2b}\otimes
\bigl(\sqrt f\,e_1+\sqrt{1-f}\,e_2\bigr)^{\otimes 2b},
\end{aligned}
\qquad\text{(1)}
```

Each of the $`K`$ superblocks receives a stock of $`2b`$ copies of each source. Thus its input is the normalized pure state

```math
v_f(U)=U^{\otimes t}v_f.
\qquad\text{(2)}
```

In the **stationary experiment**, one $`U\sim\mathrm{Haar}(U(d))`$ supplies every superblock. In the **refreshed experiment**, superblock $`j`$ receives $`v_f(U_j)`$, with the $`U_j`$ independent and Haar distributed. The overlap within each stock remains $`\sqrt f`$.

The measurement in a superblock can depend arbitrarily on the previous classical transcript. It can contain internal measurements, classically chosen source requests, known ancillas, and arbitrary processing of the supplied stock. Unused stock can be discarded. Every quantum output is discarded at the boundary; future controls depend only on classical information. Conditional on the classical history, the next quantum workspace must therefore be preparable in a known state without access to the unknown orientation.

A quantum register or entangled ancillary system carrying an unknown conditional state or correlation across a boundary is excluded. Known joint ancillary states specified by the classical history may be recreated and absorbed into the next superblock's measurement. In particular, an orientation-independent unconditional marginal of an entangled half reserved for later use does not establish a classical-only reset: its joint conditional state must satisfy the same known-state requirement. The condition concerns retained processor systems and ancillary aids, not new copies returned by later source requests.

Initial classical randomness is permitted and must be independent of $`U`$. Outcome spaces are standard Borel spaces, and instruments and controls are measurable, as in the usual probabilistic formulation of an adaptive protocol.

Let $`P_f^{\mathrm{stat}}`$ and $`P_f^{\mathrm{fresh}}`$ denote the laws of the complete reported classical transcript. Define

```math
(d)_{\uparrow s}=\prod_{r=0}^{s-1}(d+r),
\qquad
(d)_{\downarrow s}=\prod_{r=0}^{s-1}(d-r),
\qquad\text{(3)}
```

with an empty product equal to one.

**Theorem 1 — fixed-orientation comparison.** If $`M\le d/2`$, then the two transcript laws admit a common refinement whose densities satisfy

```math
p_f^{\mathrm{stat}}(\ell)
\ge \kappa\,p_f^{\mathrm{fresh}}(\ell),
\qquad
\kappa=
\frac{\bigl((d)_{\downarrow t}\bigr)^K}{(d)_{\uparrow M}}.
\qquad\text{(4)}
```

Consequently, with $`\mathrm{TV}(P,Q)=\sup_A|P(A)-Q(A)|`$,

```math
\begin{aligned}
\mathrm{TV}(P_f^{\mathrm{stat}},P_f^{\mathrm{fresh}})
&\le 1-\kappa\\
&\le 1-\exp\!\left[-\frac{M(t-1)+M(M-1)/2}{d}\right]\\
&\le \frac{M(t-1)+M(M-1)/2}{d}\\
&\le \frac{3M(M-1)}{2d}
\le \frac{3M^2}{2d}.
\end{aligned}
\qquad\text{(5)}
```

The bound is uniform in $`f`$, the number of outcomes, the classical computation, and every history-dependent choice of the measurement. It bounds transcript distributions, not the trace distance between the full stationary and refreshed quantum input states.

When an operational reduction supplies $`M\le8N`$ padded copies, the last bound in (5) is at most $`96N^2/d`$, subject to $`M\le d/2`$. Padding counts supplied stock, including unused copies and dummy superblocks. Its role is to place every branch in one fixed input space; it is not an assumption that the original algorithm uses a deterministic source allocation.

## 2. Exact norms of homogeneous matrix polynomials

Let $`\mathcal P_s`$ be the complex vector space of holomorphic homogeneous polynomials of degree $`s`$ in the $`d^2`$ entries of a matrix $`X`$. The zero polynomial is allowed. Let $`G`$ have independent centered circular complex Gaussian entries with

```math
\mathbb E G_{ij}\overline{G_{kl}}
=\frac1d\delta_{ik}\delta_{jl}.
\qquad\text{(6)}
```

Define the squared norms

```math
\|P\|_{\mathrm H}^2=\mathbb E_U|P(U)|^2,
\qquad
\|P\|_{\mathrm G}^2=\mathbb E_G|P(G)|^2.
\qquad\text{(7)}
```

There is no normalization of $`Gv`$ or of any Gaussian input vector. The Gaussian distribution is an integration device, not a physical source replacement. Dividing by a random norm would change the polynomial and would invalidate the following argument.

### 2.1 The multiplicity-free polynomial decomposition

Let $`V=\mathbb C^d`$. Schur–Weyl decomposition gives a unitary identification

```math
V^{\otimes s}
\cong
\bigoplus_{\substack{\lambda\vdash s\\\ell(\lambda)\le d}}
V_\lambda\otimes W_\lambda,
\qquad\text{(8)}
```

where $`V_\lambda`$ is the polynomial irreducible representation of $`U(d)`$, and $`W_\lambda`$ is the Specht representation of $`S_s`$. Write

```math
D_\lambda=\dim V_\lambda,
\qquad f^\lambda=\dim W_\lambda.
```

In this identification,

```math
X^{\otimes s}
=\bigoplus_\lambda S_\lambda(X)\otimes I_{W_\lambda},
\qquad
T_\pi=\bigoplus_\lambda I_{V_\lambda}\otimes\rho_\lambda(\pi),
\qquad\text{(9)}
```

where $`T_\pi`$ permutes tensor factors. The first identity defines the polynomial matrix $`S_\lambda(X)`$ also for singular $`X`$; its restriction to unitary $`X`$ is unitary.

Every degree-$`s`$ monomial is a matrix coefficient of $`X^{\otimes s}`$. Equation (9) therefore implies that $`\mathcal P_s`$ is spanned by the coefficient spaces

```math
\mathcal C_\lambda
=\mathrm{span}\{S_\lambda(X)_{ab}:1\le a,b\le D_\lambda\}.
\qquad\text{(10)}
```

Their restrictions to $`U(d)`$ are matrix coefficients of inequivalent irreducible representations. Haar orthogonality shows that they are linearly independent both within and between sectors. Hence

```math
\mathcal P_s=\bigoplus_\lambda\mathcal C_\lambda,
\qquad
\mathcal C_\lambda\cong V_\lambda^*\otimes V_\lambda.
\qquad\text{(11)}
```

This is the multiplicity-free Cauchy decomposition under left and right unitary actions. In particular, restriction to $`U(d)`$ has no kernel on $`\mathcal P_s`$. For each $`P\in\mathcal P_s`$, there are unique coefficient arrays $`A^\lambda`$ such that

```math
P(X)=\sum_\lambda\sum_{a,b=1}^{D_\lambda}
A^\lambda_{ab}S_\lambda(X)_{ab}.
\qquad\text{(12)}
```

Haar matrix-coefficient orthogonality immediately gives

```math
\|P\|_{\mathrm H}^2
=\sum_\lambda\frac{\|A^\lambda\|_{\mathrm{HS}}^2}{D_\lambda}.
\qquad\text{(13)}
```

### 2.2 Gaussian normalization from Wick contraction

We derive the Gaussian coefficient norm explicitly. Fix a unit vector $`w\in W_\lambda`$, and let $`u_a\in V^{\otimes s}`$ denote the image of $`e_a\otimes w`$ under (8). Then

```math
S_\lambda(X)_{ab}=\langle u_a,X^{\otimes s}u_b\rangle.
\qquad\text{(14)}
```

For arbitrary $`u,v,u',v'\in V^{\otimes s}`$, complex Wick contraction with (6) gives

```math
\begin{aligned}
&\mathbb E_G\!\left[
\langle u,G^{\otimes s}v\rangle
\overline{\langle u',G^{\otimes s}v'\rangle}
\right]\\
&\hspace{1cm}=
d^{-s}\sum_{\pi\in S_s}
\langle u,T_\pi u'\rangle
\langle v',T_{\pi^{-1}}v\rangle.
\end{aligned}
\qquad\text{(15)}
```

For example, the corresponding entrywise identity pairs each of the $`s`$ unbarred entries with one barred entry, producing
$`d^{-s}\sum_\pi\prod_j\delta_{i_j,k_{\pi(j)}}\delta_{r_j,l_{\pi(j)}}`$.
This also fixes the variance normalization in (15).

If the two coefficients in (15) belong to different Schur sectors, the first inner product vanishes because $`T_\pi`$ preserves each sector. In the same sector, (9) turns the summand for coefficients $`(a,b)`$ and $`(c,e)`$ into

```math
\delta_{ac}\delta_{be}
\left|\langle w,\rho_\lambda(\pi)w\rangle\right|^2.
```

Finite-group Schur orthogonality gives

```math
\sum_{\pi\in S_s}
\left|\langle w,\rho_\lambda(\pi)w\rangle\right|^2
=\frac{s!}{f^\lambda}.
```

Thus

```math
\mathbb E_G\!\left[
S_\lambda(G)_{ab}\overline{S_\mu(G)_{ce}}
\right]
=\delta_{\lambda\mu}\delta_{ac}\delta_{be}
\frac{s!}{f^\lambda d^s},
\qquad\text{(16)}
```

and

```math
\|P\|_{\mathrm G}^2
=\sum_\lambda\frac{s!}{f^\lambda d^s}
\|A^\lambda\|_{\mathrm{HS}}^2.
\qquad\text{(17)}
```

This calculation proves the scalar on the whole coefficient sector, not just on its character.

### 2.3 Hook-content constant

For a box $`(i,j)`$ of a Young diagram, let its content be $`j-i`$ and its hook length be $`h_{ij}`$. The hook-length and hook-content formulas give

```math
f^\lambda=\frac{s!}{\prod_{(i,j)\in\lambda}h_{ij}},
\qquad
D_\lambda=
\prod_{(i,j)\in\lambda}\frac{d+j-i}{h_{ij}}.
\qquad\text{(18)}
```

Set

```math
[d]_\lambda=\prod_{(i,j)\in\lambda}(d+j-i).
\qquad\text{(19)}
```

Equations (13), (17), and (18) prove the exact sector identity

```math
\boxed{
\|P_\lambda\|_{\mathrm H}^2
=\frac{d^s}{[d]_\lambda}
\|P_\lambda\|_{\mathrm G}^2
\quad(P_\lambda\in\mathcal C_\lambda).
}
\qquad\text{(20)}
```

Both norms are orthogonal sums over $`\lambda`$. These formulas are consistent with the character identities in Serebryakov and Simm [1]: their Eq. (2.8), with identity external matrices, gives the unit-variance Ginibre character norm, and Eq. (2.4) identifies its hook-content factor. Rescaling their matrix by $`d^{-1/2}`$ gives $`\mathbb E|s_\lambda(G)|^2=[d]_\lambda/d^s`$; Haar character orthogonality gives one.

### 2.4 Uniform bounds and their extrema

For $`0\le s\le d`$,

```math
(d)_{\downarrow s}\le[d]_\lambda\le(d)_{\uparrow s}.
\qquad\text{(21)}
```

Here is a direct justification of both extrema. To increase the content product, remove the last box from the bottommost nonempty row below the first and append it to the first row. This preserves a Young diagram. Its old content is $`\lambda_r-r`$, whereas its new content is the previous first-row length $`\lambda_1`$, which is larger. Repeating reaches the one-row diagram $`(s)`$. To decrease the product, choose the lowest row of length at least two, remove its last box, and append a new last row of length one. This also preserves the diagram. If its previous number of rows is $`\ell`$, the new content is $`-\ell`$, smaller than the removed content. Repeating reaches $`(1^s)`$. Since $`s\le d`$, all factors encountered are positive and the final column has allowable length.

For every $`P\in\mathcal P_s`$, (20) and (21) therefore imply

```math
\boxed{
\frac{d^s}{(d)_{\uparrow s}}\|P\|_{\mathrm G}^2
\le\|P\|_{\mathrm H}^2
\le\frac{d^s}{(d)_{\downarrow s}}\|P\|_{\mathrm G}^2.
}
\qquad\text{(22)}
```

The opposite directions of the two factorials are material. For $`P(X)=X_{11}^2`$, the Haar/Gaussian ratio is $`d/(d+1)`$. For a $`2\times2`$ determinant minor it is $`d/(d-1)`$. Thus neither direction can be replaced by a common inequality with ratio one.

## 3. The complex homogeneous product inequality

**Lemma 2 — Gaussian Bombieri inequality.** Let $`Z\in\mathbb C^q`$ have independent circular Gaussian coordinates of variance $`\sigma^2>0`$. For homogeneous complex polynomials $`P_1,\ldots,P_K`$,

```math
\mathbb E\left|\prod_{j=1}^K P_j(Z)\right|^2
\ge\prod_{j=1}^K\mathbb E|P_j(Z)|^2.
\qquad\text{(23)}
```

This is the homogeneous apolar/Bombieri product inequality [2,3]. We include a tensor proof to make clear that arbitrary complex coefficients are allowed.

It suffices to prove the two-factor statement. Let $`P`$ and $`Q`$ have degrees $`a`$ and $`c`$, and choose symmetric tensors $`u\in\mathrm{Sym}^a(\mathbb C^q)`$ and $`v\in\mathrm{Sym}^c(\mathbb C^q)`$ such that

```math
P(z)=\langle u,z^{\otimes a}\rangle,
\qquad Q(z)=\langle v,z^{\otimes c}\rangle.
```

Gaussian contraction gives

```math
\mathbb E|P(Z)|^2=a!\sigma^{2a}\|u\|^2,
\qquad
\mathbb E|Q(Z)|^2=c!\sigma^{2c}\|v\|^2,
\qquad\text{(24)}
```

and, writing $`w=u\otimes v`$,

```math
\mathbb E|P(Z)Q(Z)|^2
=\sigma^{2(a+c)}
\sum_{\pi\in S_{a+c}}\langle w,T_\pi w\rangle.
\qquad\text{(25)}
```

The vector $`w`$ is invariant under the subgroup $`H=S_a\times S_c`$, which permutes the two tensor groups separately. Every permutation lies in a double coset $`H\tau_k H`$, where $`0\le k\le\min(a,c)`$ and $`\tau_k`$ swaps $`k`$ selected positions between the groups. One can see this by permuting within each group to align all positions crossing from one group to the other, and then permuting the remaining positions internally. The matrix element in (25) is therefore constant on each such double coset.

Let $`R_{u,k}`$ and $`R_{v,k}`$ be the unnormalized $`k`$-factor reduced density operators of $`|u\rangle\langle u|`$ and $`|v\rangle\langle v|`$. The swap identity gives

```math
\langle w,T_{\tau_k}w\rangle
=\mathrm{Tr}(R_{u,k}R_{v,k})\ge0.
\qquad\text{(26)}
```

The last inequality holds because both reduced operators are positive semidefinite; it does not require real amplitudes. The zero-crossing double coset is exactly $`H`$, has $`a!c!`$ elements, and contributes $`a!c!\|u\|^2\|v\|^2`$. Keeping that contribution in (25) and dropping the nonnegative others proves the two-factor inequality using (24). Induction proves (23).

For unit coordinate variance, the Gaussian norm is the apolar norm:

```math
\mathbb E\left|\sum_\alpha c_\alpha Z^\alpha\right|^2
=\sum_\alpha\alpha!|c_\alpha|^2.
\qquad\text{(27)}
```

This is the normalization in [3, Eqs. (1)–(2)]. At variance $`\sigma^2`$, a homogeneous degree-$`a`$ squared norm gains the factor $`\sigma^{2a}`$, so degree addition preserves the constant one in (23). Homogeneity is used here and in the tensor proof. The constant-one product inequality is not valid for arbitrary collections of inhomogeneous polynomials.

## 4. From measurements to homogeneous likelihoods

### 4.1 Compression of a superblock

Let $`h`$ be a fixed previous classical history, including the initial random seed if present. Because no unknown quantum system crosses the boundary, the whole next superblock is a quantum-to-classical channel on

```math
\mathcal H=(\mathbb C^d)^{\otimes t},
\qquad D=\dim\mathcal H=d^t.
```

Its known ancillas and all internal operations can be absorbed into a POVM $`E_{j,h}`$ on $`\mathcal H`$. Source calls selected after intermediate measurements are allowed: all copies are already available in the supplied stock, and the algorithm selects the appropriate unused register. Unused registers and the superblock's final quantum systems are traced out in this compression.

The resulting POVM depends on $`h`$, but it has no additional dependence on $`U`$. Conditioning an unnormalized measurement effect on a complete classical branch does not introduce a quantum posterior into the next superblock.

For a finite outcome $`y`$, decompose its positive effect as

```math
E_{j,h}(y)=\sum_a |w_{j,h,y,a}\rangle\langle w_{j,h,y,a}|.
\qquad\text{(28)}
```

The refined outcome $`(y,a)`$ has probability

```math
\left|\left\langle w_{j,h,y,a},U^{\otimes t}v_f\right\rangle\right|^2.
\qquad\text{(29)}
```

The extra label $`a`$ is kept only for analysis; future controls use the original history and ignore it. Forgetting the label recovers the original protocol exactly. A dummy superblock that originally discards all its stock corresponds to the effect $`I`$; its rank-one refinement is also a valid POVM, with the additional outcome ignored.

For every fixed refined history, the amplitude in (29) is a holomorphic homogeneous degree-$`t`$ polynomial in $`U`$'s entries. Its coefficients may depend arbitrarily on the previous outcomes. They are fixed numbers when that history is evaluated. We use joint, unnormalized outcome probabilities; dividing by previous outcome probabilities is neither necessary nor permitted in this polynomial representation.

### 4.2 Measurable refinement for continuous outcomes

The same argument works without assuming a finite outcome set. For each history $`h`$, define a probability measure

```math
\mu_{j,h}(B)=\frac{\mathrm{Tr}E_{j,h}(B)}{D}.
\qquad\text{(30)}
```

In finite input dimension, the POVM has a positive operator-valued density

```math
H_{j,h}(y)=\frac{dE_{j,h}}{d\mu_{j,h}}(y),
\qquad H_{j,h}(y)\succeq0,
\qquad\mathrm{Tr}H_{j,h}(y)=D
\qquad\text{(31)}
```

for $`\mu_{j,h}`$-almost every $`y`$. For a measurable family of POVMs on standard Borel spaces, finite-dimensional Radon–Nikodym densities can be chosen jointly measurable in history and outcome. This can be done entrywise; positivity and the trace identity hold outside a kernel-null set. The positive square root is a continuous function of a positive matrix, so it preserves measurability.

Using a fixed orthonormal basis $`e_1,\ldots,e_D`$ of $`\mathcal H`$, put

```math
z_{j,h,y,a}=\sqrt D\,H_{j,h}(y)^{1/2}e_a,
\qquad
\nu_{j,h}(dy,a)=\frac1D\mu_{j,h}(dy),
\quad a\in[D].
\qquad\text{(32)}
```

The measure $`\nu_{j,h}`$ is a probability kernel. Relative to it, the refined POVM has rank-one density $`|z_{j,h,y,a}\rangle\langle z_{j,h,y,a}|`$, because

```math
\sum_{a=1}^D\frac1D
|z_{j,h,y,a}\rangle\langle z_{j,h,y,a}|
=H_{j,h}(y).
\qquad\text{(33)}
```

Consequently its outcome density for input (2) is

```math
|P_{j,\ell}(U)|^2,
\qquad
P_{j,\ell}(X)
=\langle z_{j,h,y,a},X^{\otimes t}v_f\rangle.
\qquad\text{(34)}
```

The same reference kernels $`\nu_{j,h}`$ apply to the stationary and refreshed experiments. Although the realized history is random and orientation dependent, the kernel as a function of a specified history is determined by the protocol alone.

Adjoining the source-independent initial seed, and successively using these kernels, defines one reference probability measure on refined transcript space. It need not be the actual law of either experiment. The actual laws have densities with respect to this measure, obtained by multiplying the conditional densities in (34). This construction handles uncountably many possible histories without a union bound over them.

## 5. Leaf domination and total variation

Fix a refined transcript $`\ell`$, including the initial seed. Suppress $`\ell`$ from the polynomial notation. For the stationary experiment, conditioning first on its one Haar unitary gives

```math
p_f^{\mathrm{stat}}(\ell)
=\mathbb E_U\prod_{j=1}^K|P_j(U)|^2
=\left\|\prod_{j=1}^K P_j\right\|_{\mathrm H}^2.
\qquad\text{(35)}
```

For the refreshed experiment, the unitary entering superblock $`j`$ is independent of its previous history. Hence

```math
p_f^{\mathrm{fresh}}(\ell)
=\prod_{j=1}^K\mathbb E_U|P_j(U)|^2
=\prod_{j=1}^K\|P_j\|_{\mathrm H}^2.
\qquad\text{(36)}
```

Independence is used in (36) only for the auxiliary experiment. There is no analogous factorization in (35).

The product polynomial has degree $`M=Kt`$. Apply the lower bound of (22) at degree $`M`$, then (23) to the $`d^2`$ Gaussian matrix entries, and finally the upper bound of (22) at degree $`t`$, rearranged for each factor:

```math
\begin{aligned}
p_f^{\mathrm{stat}}(\ell)
&\ge \frac{d^M}{(d)_{\uparrow M}}
\left\|\prod_j P_j\right\|_{\mathrm G}^2\\
&\ge \frac{d^M}{(d)_{\uparrow M}}
\prod_j\|P_j\|_{\mathrm G}^2\\
&\ge \frac{d^M}{(d)_{\uparrow M}}
\left(\frac{(d)_{\downarrow t}}{d^t}\right)^K
\prod_j\|P_j\|_{\mathrm H}^2\\
&=\frac{\bigl((d)_{\downarrow t}\bigr)^K}
{(d)_{\uparrow M}}
p_f^{\mathrm{fresh}}(\ell).
\end{aligned}
\qquad\text{(37)}
```

Zero factors cause no division problem: every step is an inequality between nonnegative quantities. The measure-theoretic construction above makes (37) an almost-everywhere density statement. Integrating it proves the measure domination $`P_f^{\mathrm{stat}}\ge\kappa P_f^{\mathrm{fresh}}`$ on refined transcripts.

Both measures are normalized because both experiments are complete POVM protocols on normalized pure states. For $`0\le\kappa<1`$, domination means

```math
P_f^{\mathrm{stat}}
=\kappa P_f^{\mathrm{fresh}}+(1-\kappa)R
\qquad\text{(38)}
```

for a probability measure $`R`$. It follows that their total variation distance is at most $`1-\kappa`$. The case $`\kappa=1`$ gives equality of the measures. Discarding the refinement labels, seed, internal outcomes, or any other transcript information cannot increase total variation. This proves the first inequality in (5) for the original reported transcript as well.

To bound the constant, write

```math
\kappa=
\frac{\prod_{j=1}^K\prod_{r=0}^{t-1}(1-r/d)}
{\prod_{r=0}^{M-1}(1+r/d)}.
\qquad\text{(39)}
```

For $`0\le x\le1/2`$,
$`-\log(1-x)\le2x`$, and for $`x\ge0`$, $`\log(1+x)\le x`$.
The condition $`M\le d/2`$ therefore gives

```math
\begin{aligned}
-\log\kappa
&\le \frac{2K}{d}\sum_{r=0}^{t-1}r
+\frac1d\sum_{r=0}^{M-1}r\\
&=\frac{Kt(t-1)+M(M-1)/2}{d}\\
&=\frac{M(t-1)+M(M-1)/2}{d}\\
&\le\frac{3M(M-1)}{2d}.
\end{aligned}
\qquad\text{(40)}
```

Together with $`1-e^{-x}\le x`$, this completes the proof of Theorem 1.

## 6. Scope of the comparison

The theorem concerns fixed pure sources and arbitrary classical adaptation between complete resets. It is not obtained by imposing covariance on the algorithm, bounding its number of outcomes, or restricting the information in its classical record. The probability of a very rare history is controlled by the same leafwise inequality as every other history.

Only the following structural facts enter the proof: the padded block input is a pure tensor polynomial in one common unitary; each boundary leaves a classical history and no unknown quantum state; and the total polynomial degree is at most half the dimension. Neither preparation-unitary access nor controlled source superpositions, inverse queries, or conjugate-state inputs are part of this copy model.

The algebraic comparison also holds for predetermined unequal block degrees $`t_1,\ldots,t_K`$, with $`M=\sum_jt_j`$ and

```math
\kappa=\frac{\prod_j(d)_{\downarrow t_j}}{(d)_{\uparrow M}},
\qquad
-\log\kappa\le
\frac{\sum_jt_j(t_j-1)+M(M-1)/2}{d}.
\qquad\text{(41)}
```

The fixed-stock version avoids needing this extension for adaptive stopping or allocation. It also avoids treating normalized conditional state amplitudes as polynomials. A sharper comparison at small dimension, or a model that retains quantum memory between blocks, requires a different argument.

## References

1. A. Serebryakov and N. Simm, **Schur Function Expansion in Non-Hermitian Ensembles and Averages of Characteristic Polynomials**, *Annales Henri Poincare* **26**, 1927–1974 (2025). [DOI: 10.1007/s00023-024-01483-6](https://link.springer.com/article/10.1007/s00023-024-01483-6). Equation (2.8) gives Ginibre character orthogonality; Eq. (2.4) supplies the hook-content factor. Their Ginibre entries have variance one, whereas (6) has variance $`1/d`$.
2. B. Beauzamy, E. Bombieri, P. Enflo and H. L. Montgomery, **Products of polynomials in many variables**, *Journal of Number Theory* **36**, 219–245 (1990). [DOI: 10.1016/0022-314X(90)90075-3](https://doi.org/10.1016/0022-314X(90)90075-3).
3. J. M. Aldaz, A. Bravo and H. Render, **The apolar inner product and a Bombieri-type inequality for polynomials**, *Journal of Inequalities and Applications* **2025**, 90 (2025). [DOI: 10.1186/s13660-025-03343-1](https://link.springer.com/article/10.1186/s13660-025-03343-1). Equations (1) and (2) state the homogeneous product inequality and the apolar normalization.
4. Q. Ye, Z. Liu and D.-L. Deng, **Exponential Advantage from One More Replica in Estimating Nonlinear Properties of Quantum States**, [arXiv:2509.24000v1](https://arxiv.org/pdf/2509.24000v1) (2025). Theorem 29, Eqs. (25)–(30), and Lemma 30 give a related adaptive likelihood and symmetrizer argument for Haar-assembled ensembles.
