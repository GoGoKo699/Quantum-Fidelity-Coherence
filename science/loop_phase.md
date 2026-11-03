# Applying complete-reset comparison to loop phase

The fixed-source transcript method extends beyond the root fidelity of two states. For a sparse cycle of four unknown pure states, it proves that copy-optimal weak-overlap phase estimation requires coherent runs consuming order $`c^{-2}`$ copies in a sufficient large-dimension regime. The phase-specific information calculation is owned by the sister project [Quantum Holonomy Sampling](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling); this page explains the transfer and its operational consequence.

## 1. Sources, target and reset rule

Four classically labeled sources return independent copies of fixed unknown pure states in $`\mathbb C^d`$. Their sparse Gram matrix is

```math
G_\phi=I+c\left(e^{-i\phi/4}S+e^{i\phi/4}S^\dagger\right),
\qquad 0\lt c\le\frac14,\qquad d\ge4,
```

where $`S|j\rangle=|j+1\rangle`$ with cyclic indices. Its forward adjacent entries are $`c e^{i\phi/4}`$, opposite entries vanish, and

```math
B=\prod_{j=1}^4\langle\psi_j|\psi_{j+1}\rangle=c^4e^{i\phi}.
```

The target is the circular phase $`\phi=\arg B`$. One realization is $`|\psi_j(\phi)\rangle=G_\phi^{1/2}|j\rangle`$, embedded in $`\mathbb C^d`$. The hard ensemble applies one common Haar unitary $`U`$ to all four vectors and keeps that same $`U`$ for every subsequent source request. Every ensemble member is a legal tuple of fixed pure sources.

Use the [complete-reset rule](model.md#2-the-complete-reset-constraint) with four labels and an integer $`b\ge1`$: a run consumes at most $`b`$ copies in total, including copies already measured or discarded. The worst-case total copy cap is $`N`$. At a boundary, only classical input-dependent history survives. All retained quantum systems must have known joint conditional states specified by that history. Source labels, measurements and stopping may adapt to the history; classical memory and computation are unrestricted. Preparation unitaries, their inverses and coherent source-label access are not supplied.

Thus $`b`$ measures consumed copies per complete reset. It does not measure simultaneous storage, gate depth or elapsed laboratory time.

## 2. The additional phase information bound

Let $`\omega_\phi^{\mathbf r}`$ be the common-Haar average of one stock containing $`r_j`$ copies of label $`j`$, and put $`t=\sum_jr_j`$. The phase-specific block theorem is

```math
D\!\left(\omega_\phi^{\mathbf r}\middle\Vert
\omega_\theta^{\mathbf r}\right)
\le\frac83\,t^4c^8e^{4tc^2}.
\qquad\text{(1)}
```

This is uniform in the multiplicities and in both phases. The [authoritative block-information proof](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling/blob/36297ca5f51fbfa361f5cd5184e901fb66b3b46e/science/block-information.md) reduces the stock to its permutation-orbit Gram matrix $`C_\phi`$. On the subspace with the prescribed label counts, scalar Jensen gives $`C_\phi\succeq e^{-2tc^2}I`$. An entry can depend on the phase only after at least four labels change around the cycle. Counting these entries and bounding quantum relative entropy by the corresponding chi-square expression proves (1).

For exactly one copy of each label, the optimal invariant block quantum Fisher information is

```math
\mathcal F_4(\phi)=2c^8\bigl[1+O(c^4)\bigr],
```

uniformly in $`\phi`$. The complete four-copy family commutes after its representation reduction, so one phase-independent spectral measurement attains that information. This is an optimum over the block measurements, rather than a lower bound inferred from the visibility $`c^4`$ of a chosen cycle test. The ordinary cycle measurement already attains the leading information rate.

Equation (1), rather than an extrapolation of the four-copy asymptotic expansion, supplies the uniform control needed when run lengths grow with $`c^{-1}`$. It is not a consequence of the root-fidelity block bound in this repository.

## 3. From fresh stocks to actual fixed sources

Set $`\beta=\min\{b,N\}`$ and $`K=\lceil N/\beta\rceil`$. Group complete runs until at least $`\beta`$ copies have been consumed, or until termination. Every group uses fewer than $`2\beta`$ copies. Supplying $`2\beta`$ copies of each of the four labels therefore simulates all its adaptive source choices on one fixed input space. Pad early termination with dummy groups.

There are $`K`$ stocks, each with $`t=8\beta`$ copies, and their total padded count obeys $`M\le16N`$. Let $`P_\phi`$ be the actual fixed-orientation transcript law, and let $`Q_\phi`$ be the auxiliary law with independent common orientations in successive stocks. The [general pure-stock comparison](haar_comparison.md#1-statement-and-operational-setting) gives

```math
\mathrm{TV}(P_\phi,Q_\phi)
\le\frac{384N^2}{d},
\qquad d\ge32N.
\qquad\text{(2)}
```

The comparison retains arbitrary classical adaptation. At a specified refined history, the next stock's measurement amplitude is a homogeneous degree-$`t`$ polynomial in $`U`$. Haar–Gaussian norm comparison and the homogeneous Bombieri inequality control the joint leaf likelihoods. They do not assume that classical history contains no information about the fixed orientation.

Under the auxiliary law, the next stock is independent of earlier history. Conditional quantum-to-classical data processing, (1), and the classical divergence chain rule give

```math
D(Q_\phi\Vert Q_\theta)
\le\frac{65536}{3}\,N\beta^3c^8e^{32\beta c^2}.
```

Applying Pinsker and paying (2) once for each phase yields the fixed-source theorem

```math
\boxed{
\mathrm{TV}(P_\phi,P_\theta)
\le
\sqrt{\frac{32768}{3}}\,c^4\sqrt{Nb^3}\,e^{16bc^2}
+\frac{768N^2}{d},
\qquad d\ge32N.
}
\qquad\text{(3)}
```

The [full phase converse](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling/blob/36297ca5f51fbfa361f5cd5184e901fb66b3b46e/science/coherent-runs.md) owns the detailed statement, padding argument and consequences. Equations (1)–(3) show the precise exchange between the projects: the phase stock has a new information bound, while the fixed-source comparison method is shared.

## 4. The coherence threshold and its limits

Fix circular accuracy $`0\lt\epsilon\le\pi/16`$ and success probability at least $`2/3`$ for every fixed source tuple in the sparse family above. Phases $`0`$ and $`4\epsilon`$ have disjoint success intervals, so successful estimation requires transcript total variation at least $`1/3`$.

**Corollary.** If a permitted estimator has $`N\le Cc^{-2}`$ copies, where $`C\ge1`$, and

```math
d\ge9216C^2c^{-4},
```

then

```math
\boxed{b\ge\frac{c^{-2}}{128C^{1/3}}.}
\qquad\text{(4)}
```

Indeed, if $`\eta=bc^2\lt1/(128C^{1/3})`$, the first term of (3) is below $`\sqrt{e^{1/4}/192}\lt0.082`$, while its dimension term is at most $`1/12`$. Their sum contradicts the testing requirement. The constants and dimension condition are conservative sufficient conditions.

The sister project's coherent algorithm uses $`O(c^{-2})`$ copies at fixed loop length and fixed accuracy. Running it without a reset attains $`b=O(c^{-2})`$. Thus the copy-optimal consumed-copy coherence threshold is $`b=\Theta(c^{-2})`$ in the stated large-dimension regime. Keeping a small quantum register coherent across many arrivals can satisfy this long-run requirement; no simultaneous-memory-width lower bound follows.

For any fixed $`b\ge4`$, (3) also gives the $`\Omega_b(c^{-8})`$ lower exponent when the dimension term is sufficiently small. Repeated four-copy cycle measurements attain $`O(c^{-8})`$ copies at fixed accuracy. A matching formula throughout the intermediate-$`b`$ regime is not asserted.

The dimension qualification is essential. At fixed finite $`d`$, separate-copy tomography can estimate each source to error of order $`c\epsilon`$ using $`O_d(c^{-2}\epsilon^{-2})`$ copies, then infer the loop phase from classical estimates. Hence a claim that every dimension requires diverging coherent runs would be false.

## 5. Attribution and reading route

The replica hierarchy and adaptive Haar-likelihood precedent of [Ye, Liu and Deng](https://arxiv.org/pdf/2509.24000v1), particularly Theorem 29 and Lemma 30, are inherited foundations. [Oszmaniec, Brod and Galvão](https://arxiv.org/pdf/2109.10006v1) supply the Bargmann-invariant framework, spanning-tree phase gauge and direct cycle test. Neither attribution is replaced by this phase/reset theorem.

Read the [root-fidelity model](model.md) and [general Haar comparison](haar_comparison.md) for this repository's own contribution. Read the sister project's [block information](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling/blob/36297ca5f51fbfa361f5cd5184e901fb66b3b46e/science/block-information.md) and [coherent-run converse](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling/blob/36297ca5f51fbfa361f5cd5184e901fb66b3b46e/science/coherent-runs.md) for the authoritative phase proofs. The targets and their precision conventions remain distinct: root fidelity concerns two-state overlap magnitude, while this application concerns the argument of a four-state product.
