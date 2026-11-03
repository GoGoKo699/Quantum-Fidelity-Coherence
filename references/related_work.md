# Related work and attribution

The contribution considered here is a uniform copy-complexity law for root fidelity between two fixed unknown pure states, subject to a cap on copies consumed between complete quantum resets. Classical adaptation is unrestricted. The [model](../science/model.md) gives the exact quantifiers and dimension conditions.

The comparisons below distinguish the established ingredients from the resource-constrained conclusion and its transfer to a four-state phase. They reflect a focused primary-source review through November 3, 2026; they are not a claim of exhaustive priority clearance.

## 1. Collective overlap measurements and grouping

**Fanizza, Rosati, Skotiniotis, Calsamiglia and Giovannetti**, *Beyond the Swap Test: Optimal Estimation of Quantum State Overlap*, Physical Review Letters 124, 060503 (2020), [arXiv:1906.10639v3](https://arxiv.org/pdf/1906.10639v3), [DOI](https://doi.org/10.1103/PhysRevLett.124.060503).

Their common-orientation average, two-row Schur decomposition, and optimal collective measurement are the direct foundations of the estimator and one-block analysis. Their treatment establishes the small-overlap advantage over independent SWAP tests. The main-text gate-complexity paragraph and supplementary Eq. (130) explicitly propose dividing copies into groups, measuring each group collectively, and processing the outcomes classically.

Accordingly, this repository does not claim a new collective overlap measurement or a new grouping strategy. Its upper-bound calculation uses that measurement to obtain a uniform finite-error guarantee for root fidelity, including rounding and synthesis error. The main added conclusion is a matching lower bound for every adaptive protocol under the complete-reset model. The uniform root-fidelity statement and its fixed-source adaptive converse are distinct from the local Fisher-information and Bayesian squared-overlap comparisons in that paper.

## 2. Unrestricted sample-optimal root fidelity

**Qisheng Wang and Zhicheng Zhang**, *Sample-Optimal Quantum Estimators for Pure-State Trace Distance and Fidelity via Samplizer*, ICALP 2026, LIPIcs 374, Article 154, [publisher full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.154/LIPIcs.ICALP.2026.154.html), [arXiv:2410.21201](https://arxiv.org/abs/2410.21201).

This work supplies the unrestricted $`\Theta(\epsilon^{-2})`$ sample endpoint for pure-state root fidelity, as well as the broader samplizer framework. The present result preserves that endpoint and identifies the coherent-run size needed to attain it. It makes no claim to improve the unrestricted copy complexity. The elementary two-dimensional testing lower bound is included directly in the [converse](../science/adaptive_converse.md).

## 3. Adaptive replica restrictions and likelihood domination

**Qi Ye, Zhenhuan Liu and Dong-Ling Deng**, *Exponential Advantage from One More Replica in Estimating Nonlinear Properties of Quantum States*, [arXiv:2509.24000v1](https://arxiv.org/pdf/2509.24000v1) (2025).

This work studies a hierarchy of replica-restricted measurements for nonlinear state properties. Theorem 29, Eqs. (25)–(30), and Lemma 30 provide a close methodological precedent: stationary random-state ensembles can be compared with independently averaged inputs through one-sided transcript likelihood bounds and symmetric-tensor product inequalities.

That likelihood strategy is credited here. The fixed-overlap pair used in this repository is generated from correlated columns of one common Haar unitary. It is not a literal instance of the paper's stated mixtures and tensors of independent Haar pure states. The [Haar comparison](../science/haar_comparison.md) supplies the required matrix-polynomial comparison explicitly, including its sector constants, adaptive normalization, and measurement refinement.

The comparison applies more generally to any fixed pure stock acted on by one common unitary. That extension retains the holomorphic homogeneous amplitudes, classical-only boundaries, and full refined-leaf likelihood comparison. It permits the four-source application in [loop phase](../science/loop_phase.md), once its phase-specific information bound has been supplied. This is a model-level distinction and a proved transfer argument. It is not a claim that resetting random orientations or using likelihood domination was previously unknown.

## 4. Related resources with different operational meaning

**Weiyuan Gong, Jonas Haferkamp, Qi Ye and Zhihan Zhang**, *On the sample complexity of purity and inner product estimation*, [arXiv:2410.12712v1](https://arxiv.org/pdf/2410.12712v1) (2024).

This work relates purity estimation with bounded quantum memory to inner-product estimation with bounded communication and unentangled measurements. The targets include mixed-state purity and squared Hilbert–Schmidt overlap. These comparisons concern persistent quantum width or communication, whereas the present resource counts copies consumed before all input-dependent quantum information is removed. A width constraint cannot simply be replaced by a run-length constraint. The symmetric-projector inequality appearing in this literature is also relevant background for the polynomial product argument.

**Tight Lower Bounds for State Tomography with Limited Entanglement**, [arXiv:2609.05718](https://arxiv.org/abs/2609.05718) (2026), is a further model-level comparator: its abstract describes tomography with bounded groups of fresh copies and adaptive measurements. The present task estimates one scalar for a pure-state pair. General mixed-state tomography bounds do not directly furnish this scalar lower bound. The accessible abstract was inspected; no theorem from its full text is invoked in any proof here.

## 5. Mathematical and implementation ingredients

**Hari Krovi**, *An efficient high dimensional quantum Schur transform*, Quantum 3, 122 (2019), [arXiv:1804.00055v2](https://arxiv.org/pdf/1804.00055v2), [DOI](https://doi.org/10.22331/q-2019-02-14-122).

Theorem 3 supplies a Schur transform with gate complexity polynomial in copy count, logarithmic Hilbert-space dimension, and logarithmic inverse approximation error. Section 3.1 specifies the operator-norm approximation convention. This inherited circuit result supplies the computational implementation in the estimator.

**A. Serebryakov and N. Simm**, *Schur Function Expansion in Non-Hermitian Ensembles and Averages of Characteristic Polynomials*, Annales Henri Poincaré 26, 1927–1974 (2025), [DOI](https://doi.org/10.1007/s00023-024-01483-6).

Eqs. (2.8) and (2.4) give Gaussian Schur character orthogonality and the hook-content factor. They verify the normalization used in the Haar–Gaussian comparison. The full matrix-coefficient calculation is reproduced by a direct Wick-contraction argument in the scientific account.

**Bernard Beauzamy, Enrico Bombieri, Per Enflo and Hugh L. Montgomery**, *Products of polynomials in many variables*, Journal of Number Theory 36, 219–245 (1990), [DOI](https://doi.org/10.1016/0022-314X(90)90075-3); and **J. M. Aldaz, A. Bravo and H. Render**, *The apolar inner product and a Bombieri-type inequality for polynomials*, Journal of Inequalities and Applications 2025, 90 (2025), [DOI](https://doi.org/10.1186/s13660-025-03343-1).

Homogeneous Gaussian/apolar norm supermultiplicativity is an inherited inequality. The latter paper states the normalization and product inequality in Eqs. (1)–(2). A symmetric-tensor proof is included here to expose the role of homogeneity and arbitrary complex coefficients.

## 6. Bargmann invariants, cycle tests and normalized functions

**Michał Oszmaniec, Daniel J. Brod and Ernesto F. Galvão**, *Measuring relational information between quantum states, and applications*, [arXiv:2109.10006v1](https://arxiv.org/pdf/2109.10006v1) (2021).

This work supplies the Bargmann-invariant framework, direct cycle tests for their real and imaginary parts, and a spanning-tree phase gauge for the Gram matrix. These are the primary operational precedents for the sister phase task. Invariant completeness does not determine the optimal information in a block, and the visibility of a specified cycle test does not bound every block measurement. The sparse four-copy calculation optimizes that information and finds the same leading $`c^8`$ rate already attained by a cycle measurement. The new run-length conclusion additionally requires a uniform growing-stock phase bound and a fixed-source adaptive transcript comparison.

**Yihui Quek, Eneet Kaur and Mark M. Wilde**, *Multivariate trace estimation in constant quantum depth*, Quantum 8, 1220 (2024), [arXiv:2206.15405v3](https://arxiv.org/pdf/2206.15405v3), [DOI](https://doi.org/10.22331/q-2024-01-10-1220).

Their parallel circuits show that a multivariate trace can be estimated at constant quantum circuit depth. Circuit depth and copies consumed before a complete reset are different resources. Additive trace precision is also a different requirement from the phase of a trace whose magnitude tends to zero. Their construction therefore neither supplies nor contradicts the present phase/reset converse.

**Hongshun Yao, Yingjian Liu, Tengxiang Lin and Xin Wang**, *Sample-Efficient Estimation of Nonlinear Quantum State Functions*, [arXiv:2412.01696v3](https://arxiv.org/html/2412.01696v3), version dated June 20, 2025.

The QSF framework estimates a normalized degree-$`n`$ polynomial using $`O(n/\delta^2)`$ copies for additive precision $`\delta`$ (Theorem 1). Its convention fixes the coefficient one-norm to one; rescaling an unnormalized target and controlling its approximation can introduce a normalization factor. Sections IV.1–IV.2 discuss the resulting coefficient and spectral conditioning. This is a relevant copy-access upper-bound framework, rather than a complete-reset lower bound. Its normalized additive guarantee cannot be read directly as uniform root-fidelity or weak-loop-phase precision without retaining those conditioning costs. In particular, phase accuracy for $`|B|=c^4`$ is not additive constant accuracy in $`B`$.

## 7. The proved sister relation and result ownership

[Quantum Holonomy Sampling](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling) supplies the discrete loop-phase task, the sparse four-state hard geometry, and a coherent copy-only construction using $`O(c^{-2})`$ copies at fixed loop length and phase accuracy. Its [phase block-information theorem](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling/blob/5502b63a6635ec24d8a0f082ca37846bdec35c3d/science/block-information.md) proves a uniform bound for arbitrary fixed source counts. Its [coherent-run converse](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling/blob/5502b63a6635ec24d8a0f082ca37846bdec35c3d/science/coherent-runs.md) combines that bound with this repository's general pure-stock comparison.

The resulting endpoint theorem is phase-specific: at fixed small circular accuracy, a uniform estimator with total copies $`N\le Cc^{-2}`$ must have $`b\ge c^{-2}/(128C^{1/3})`$ when $`d\ge9216C^2c^{-4}`$, for $`C\ge1`$. The coherent construction attains order $`c^{-2}`$ total copies and run length. A matching full phase tradeoff at every intermediate run cap and dimension is not asserted. At fixed finite dimension, separate-copy tomography attains $`O_d(c^{-2})`$ at fixed phase accuracy, so the dimension qualification is material.

Quantum Fidelity Coherence owns the root-fidelity tradeoff and the common-unitary adaptive transcript method. Quantum Holonomy Sampling owns the phase-specific information calculation, constructive phase algorithm and phase converse. The [local transfer account](../science/loop_phase.md) gives the source model, reset convention, imported bound, comparison and endpoint in one independently readable route. The relationship is a proved method transfer with a new task-specific input, not a substitution of overlap amplitude for root-fidelity accuracy.

## 8. Surviving conclusion and comparison limits

After these ingredients are credited, the conclusion is the sharp high-dimensional uniform root-fidelity law, the arbitrary-adaptation fixed-source converse, and the resulting necessary coherent-run size for optimal sample order. The finite-dimension restriction, pure-state source contract, and conditional complete-reset condition are material to that statement.

The sister application establishes that the same fixed-source comparison supports a phase theorem after the separate orbit-Gram bound has been proved. It preserves the independent ownership and precision conventions of the two tasks.

The comparison does not establish an optimal gate exponent, a persistent-memory-width theorem, a noisy-device result, or a matching law at every dimension. Those claims are not needed for the theorem and are not inferred from neighboring papers.

Structured citation metadata for the directly used sources is available in [sources.bib](sources.bib). Page-specific references identify the exact argument supported by each source.
