# The converse for fixed sources and adaptive runs

This page proves the lower bounds in the [model and main theorem](model.md). In particular, it closes the distinction between fresh random orientations in a one-block calculation and the same unknown state pair used throughout the actual experiment.

Write $`f=F^2`$. All relative entropies use natural logarithms, and total variation is one half of the $`L^1`$ distance. The proof uses the [exact block bound](block_information.md) and the [fixed-orientation transcript comparison](haar_comparison.md).

## 1. Two hard ensembles

Let $`U`$ be Haar distributed on $`U(d)`$, sampled once. For a parameter $`f\in[0,1]`$, define

```math
|\psi_U\rangle=Ue_1,
\qquad
|\phi_{f,U}\rangle
=U\bigl(\sqrt f\,e_1+\sqrt{1-f}\,e_2\bigr).
\qquad\text{(1)}
```

Every realization is a fixed pair of pure states with root fidelity $`\sqrt f`$. Both hypotheses use the same distribution of the common orientation. In the physical experiment the chosen $`U`$ stays fixed for all source calls.

Let $`P_f`$ denote the complete classical transcript law of an arbitrary allowed algorithm on this ensemble. The algorithm may be noncovariant, keep an unbounded classical record, and adapt to that record.

For $`0<\epsilon\le1/8`$, take

```math
f_0=0,
\qquad f_1=16\epsilon^2.
\qquad\text{(2)}
```

Their root fidelities are $`0`$ and $`4\epsilon`$. A uniformly successful estimator distinguishes them by declaring hypothesis 1 exactly when its output exceeds $`2\epsilon`$. Under hypothesis 0, a successful estimate is at most $`\epsilon`$; under hypothesis 1 it is at least $`3\epsilon`$. Each error is at most $`1/3`$, also after averaging over $`U`$. Therefore

```math
\mathrm{TV}(P_{16\epsilon^2},P_0)\ge\frac13.
\qquad\text{(3)}
```

This is a lower bound from a prior supported entirely on legal fixed inputs. It does not assume that the estimator itself uses a random orientation.

## 2. A fixed-stock simulation of arbitrary source choices

Equation (3) already rules out a zero-copy protocol: without source requests its transcript law is the same under both hypotheses. We may therefore suppose the protocol uses at most $`N\ge1`$ source copies along every history. Set

```math
\beta=\min\{b,N\},
\qquad
K=\left\lceil\frac N\beta\right\rceil.
\qquad\text{(4)}
```

All original runs consume at most $`\beta`$ copies. Concatenate complete successive runs until at least $`\beta`$ copies have been consumed, or until the algorithm terminates. Call each such group a superblock.

Immediately before adding its final original run, a nonempty unfinished superblock has consumed fewer than $`\beta`$ copies. The next run consumes at most $`\beta`$. Thus every superblock consumes fewer than $`2\beta`$ copies. Zero-copy terminal processing is absorbed into classical postprocessing and does not create another nonempty group. On a history with $`L\ge1`$ nonempty superblocks, each of the first $`L-1`$ consumes at least $`\beta`$ copies and the last consumes at least one. Hence $`(L-1)\beta+1\le N`$, so $`L\le\lceil N/\beta\rceil=K`$. A history using no copies has no nonempty superblocks and satisfies the same upper bound.

For every superblock, presupply **$`2\beta`$ copies of each source**, in a known ordering. Simulate any source request by selecting an unused register from its requested source. Even an allocation that asks only for one source fits this stock. Unused registers are discarded when the superblock ends.

This is a mathematical simulation. Presupplying unused copies increases the resources available to the analysis but does not force the original algorithm to inspect them. It represents every possible original within-run source choice as one instrument on a fixed input space, with coefficients depending only on the previous classical history.

If the protocol terminates early, append dummy superblocks that discard their stocks and produce deterministic coarse outcomes. Retain the original output, and ignore all dummy outcomes. There are then exactly $`K`$ stocks, each containing

```math
t=4\beta
\quad\text{copies, with total padded count}\quad
M=4\beta K\le4(N+\beta)\le8N.
\qquad\text{(5)}
```

The identity channel on the original coarse transcript is exact. Intermediate resets inside a superblock remain part of its instrument. At a superblock boundary there is still only classical input-dependent information, because the boundary was placed at an original reset or after termination.

Known history-dependent quantum ancillas can be incorporated into the instrument. The model excludes quantum information in retained systems or reserved entangled aids across the boundary; their presence would invalidate this reduction to a conditional POVM.

## 3. Introduce, then control, the refreshed experiment

For analysis, replace the common $`U`$ by a fresh independent Haar unitary at each superblock. Both sources within a stock use the same new unitary, so the squared overlap remains $`f`$. Let $`Q_f`$ be the resulting transcript law under the same conditional instruments.

The fixed and refreshed distributions are generally different. Earlier outcomes in the physical experiment can reveal information about the one fixed orientation. The following comparison bounds that advantage rather than discarding it.

### 3.1 Stationary versus refreshed

If $`d\ge16N`$, then (5) implies $`M\le d/2`$. The fixed-stock theorem in [Haar comparison](haar_comparison.md#1-statement-and-operational-setting), with its parameter $`b`$ replaced by $`\beta`$, gives

```math
\mathrm{TV}(P_f,Q_f)
\le\frac{3M^2}{2d}
\le\frac{96N^2}{d}
\quad\text{for every }f\in[0,1].
\qquad\text{(6)}
```

It applies to arbitrary classical histories and to the fine-grained instrument outcomes. Forgetting padding and refinement labels cannot increase total variation, so (6) applies to the actual reported transcript.

### 3.2 Information accumulated under refreshed orientations

Conditional on any earlier history, the next refreshed stock is the common-orientation average of $`2\beta`$ copies of each source. The [block relative-entropy bound](block_information.md#5-a-global-relative-entropy-bound) gives

```math
D(\omega_f^{2\beta,2\beta}\Vert
\omega_0^{2\beta,2\beta})
\le4\beta^2f^2.
\qquad\text{(7)}
```

The conditional instrument is the same function of the specified history under both hypotheses. Quantum-to-classical data processing therefore bounds its conditional outcome divergence by the same quantity, even when source requests, intermediate measurements, and stopping decisions inside that instrument are adaptive.

The relative-entropy chain rule gives

```math
\begin{aligned}
D(Q_f\Vert Q_0)
&\le4K\beta^2f^2\\
&\le8N\beta f^2,
\end{aligned}
\qquad\text{(8)}
```

where $`K\le N/\beta+1\le2N/\beta`$. Dummy coarse outcomes add zero information; using (7) for them remains a valid upper bound. The common classical random seed has the same distribution under both hypotheses and adds zero initial divergence.

Pinsker's inequality yields

```math
\mathrm{TV}(Q_f,Q_0)
\le2f\sqrt{N\beta}.
\qquad\text{(9)}
```

### 3.3 Return to fixed sources

Use (6) once for $`f`$ and once for zero. The triangle inequality with (9) gives the central testing bound:

```math
\boxed{
\mathrm{TV}(P_f,P_0)
\le
2f\sqrt{N\min\{b,N\}}
+\frac{192N^2}{d},
\qquad d\ge16N.
}
\qquad\text{(10)}
```

The first term is information accumulated from coherent stocks. The second controls the benefit of learning their shared orientation through earlier classical outcomes. In particular, the one-block calculation has not been applied independently to a fixed source without justification.

## 4. Lower bounds at finite dimension

### 4.1 The coherence-dependent term

Suppose, toward contradiction, that an estimator satisfying the model has

```math
N<2^{-16}\min\left\{\sqrt d,\frac{1}{b\epsilon^4}\right\}.
\qquad\text{(11)}
```

For $`d\ge2`$, this implies $`16N\lt d`$, so (10) is applicable. Substituting $`f=16\epsilon^2`$ and using $`\beta\le b`$,

```math
\begin{aligned}
\mathrm{TV}(P_{16\epsilon^2},P_0)
&\le32\epsilon^2\sqrt{Nb}
+192N^2/d\\
&<32\sqrt{2^{-16}}+192\,2^{-32}\\
&=\frac18+192\,2^{-32}<\frac13.
\end{aligned}
\qquad\text{(12)}
```

This contradicts (3). Consequently

```math
\boxed{
N_b(\epsilon,d)\ge
2^{-16}\min\left\{\sqrt d,\frac{1}{b\epsilon^4}\right\}.
}
\qquad\text{(13)}
```

The argument is valid even when the displayed lower bound is below one; in that regime it is simply weak. It does not extend the sharp large-dimension law to all finite dimensions.

### 4.2 An unconditional precision term

The $`\epsilon^{-2}`$ lower bound needs neither Haar averaging nor a reset constraint. Consider the two fixed pairs

```math
|\psi\rangle=e_1,\qquad
|\phi_0\rangle=e_2,\qquad
|\phi_1\rangle=
4\epsilon e_1+\sqrt{1-16\epsilon^2}\,e_2.
\qquad\text{(14)}
```

Give the algorithm the description of $`\psi`$ for free. Presupply $`N`$ copies of $`\phi_h`$ and enough copies of the known $`\psi`$ to simulate every requested source call. This grants at least as much information as any adaptive protocol using at most $`N`$ total copies. Its transcript distinguishability is at most the trace distance of the two pure product inputs:

```math
\begin{aligned}
\mathrm{TV}(P_1,P_0)
&\le
\frac12\left\|
|\phi_1\rangle\langle\phi_1|^{\otimes N}
-
|\phi_0\rangle\langle\phi_0|^{\otimes N}
\right\|_1\\
&=\sqrt{1-(1-16\epsilon^2)^N}\\
&\le4\epsilon\sqrt N.
\end{aligned}
\qquad\text{(15)}
```

The last step uses $`1-(1-x)^N\le Nx`$ for $`x\in[0,1]`$. Root fidelity again differs by $`4\epsilon`$, so successful estimation requires total variation at least $`1/3`$. It follows that

```math
\boxed{N_b(\epsilon,d)\ge\frac1{144\epsilon^2}.}
\qquad\text{(16)}
```

Both alternatives lie in a two-dimensional subspace, so (16) holds for every $`d\ge2`$. This elementary argument agrees with the known unrestricted sample-optimality results; see [related work](../references/related_work.md).

Combining (13), (16), and the [finite-precision estimator](estimator.md#3-a-fully-specified-finite-precision-algorithm) proves the main theorem.

## 5. The sample-optimality threshold

Suppose $`N\le C_0\epsilon^{-2}`$ with $`C_0\ge1`$ and $`d\ge2304C_0^2\epsilon^{-4}`$. These assumptions imply $`d\ge16N`$. They also give

```math
\frac{192N^2}{d}\le\frac1{12}.
```

Combining (3) and (10) gives

```math
\frac14
\le32\epsilon^2\sqrt{N\min\{b,N\}}
\le32\epsilon^2\sqrt{Nb}.
```

Squaring and rearranging,

```math
b\ge\frac1{16384N\epsilon^4}
\ge\frac1{16384C_0\epsilon^2}.
\qquad\text{(17)}
```

This proves the stated necessity at dimension of order $`\epsilon^{-4}`$, with a sufficiently large constant depending on the allowed sample prefactor. Choosing $`b`$ of order $`\epsilon^{-2}`$ in the estimator supplies the matching order of coherent processing.

## 6. What the converse does and does not use

No covariance restriction is imposed on the estimator. No bound is placed on classical memory or computation. Intermediate measurements, random source allocation, rare histories, and early stopping are all included.

The two material restrictions are the copy-only source contract and the classical-only reset boundary. A persistent quantum register changes the statistical architecture. A coherent preparation oracle changes the source contract. Neither resource is supplied by independent copies, and neither is covered by (10).

The dimension term comes from a proved stationary-to-refreshed comparison. It identifies the range where this mechanism establishes sharpness. Improving the finite-dimensional frontier would require additional analysis; removing this term from the headline without such an argument would be unjustified.
