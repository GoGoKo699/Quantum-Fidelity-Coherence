# Related work and attribution

The contribution considered here is a uniform copy-complexity law for root fidelity between two fixed unknown pure states, subject to a cap on copies consumed between complete quantum resets. Classical adaptation is unrestricted. The [model](../science/model.md) gives the exact quantifiers and dimension conditions.

The comparisons below distinguish the established ingredients from the resource-constrained conclusion. They reflect a focused primary-source review through October 31, 2026; they are not a claim of exhaustive priority clearance.

## 1. Collective overlap measurements and grouping

**Fanizza, Rosati, Skotiniotis, Calsamiglia and Giovannetti**, *Beyond the Swap Test: Optimal Estimation of Quantum State Overlap*, Physical Review Letters 124, 060503 (2020), [arXiv:1906.10639v3](https://arxiv.org/pdf/1906.10639v3), [DOI](https://doi.org/10.1103/PhysRevLett.124.060503).

Their common-orientation average, two-row Schur decomposition, and optimal collective measurement are the direct foundations of the estimator and one-block analysis. Their treatment establishes the small-overlap advantage over independent SWAP tests. The main-text gate-complexity paragraph and supplementary Eq. (130) explicitly propose dividing copies into groups, measuring each group collectively, and processing the outcomes classically.

Accordingly, this repository does not claim a new collective overlap measurement or a new grouping strategy. Its upper-bound calculation uses that measurement to obtain a uniform finite-error guarantee for root fidelity, including rounding and synthesis error. The main added conclusion is a matching lower bound for every adaptive protocol under the complete-reset model. The uniform root-fidelity statement and its fixed-source adaptive converse are distinct from the local Fisher-information and Bayesian squared-overlap comparisons in that paper.

## 2. Unrestricted sample-optimal root fidelity

**Qisheng Wang and Zhicheng Zhang**, *Sample-Optimal Quantum Estimators for Pure-State Trace Distance and Fidelity via Samplizer*, ICALP 2026, LIPIcs 374, Article 154, [publisher full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.154/LIPIcs.ICALP.2026.154.html), [arXiv:2410.21201](https://arxiv.org/abs/2410.21201).

This work supplies the unrestricted $\Theta(\epsilon^{-2})$ sample endpoint for pure-state root fidelity, as well as the broader samplizer framework. The present result preserves that endpoint and identifies the coherent-run size needed to attain it. It makes no claim to improve the unrestricted copy complexity. The elementary two-dimensional testing lower bound is included directly in the [converse](../science/adaptive_converse.md).

## 3. Adaptive replica restrictions and likelihood domination

**Qi Ye, Zhenhuan Liu and Dong-Ling Deng**, *Exponential Advantage from One More Replica in Estimating Nonlinear Properties of Quantum States*, [arXiv:2509.24000v1](https://arxiv.org/pdf/2509.24000v1) (2025).

This work studies a hierarchy of replica-restricted measurements for nonlinear state properties. Theorem 29, Eqs. (25)–(30), and Lemma 30 provide a close methodological precedent: stationary random-state ensembles can be compared with independently averaged inputs through one-sided transcript likelihood bounds and symmetric-tensor product inequalities.

That likelihood strategy is credited here. The fixed-overlap pair used in this repository is generated from correlated columns of one common Haar unitary. It is not a literal instance of the paper's stated mixtures and tensors of independent Haar pure states. The [Haar comparison](../science/haar_comparison.md) supplies the required matrix-polynomial comparison explicitly, including its sector constants, adaptive normalization, and measurement refinement.

This is a model-level distinction and a proved transfer argument. It is not a claim that resetting random orientations or using likelihood domination was previously unknown.

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

## 6. Surviving conclusion and comparison limits

After these ingredients are credited, the conclusion is the sharp high-dimensional uniform root-fidelity law, the arbitrary-adaptation fixed-source converse, and the resulting necessary coherent-run size for optimal sample order. The finite-dimension restriction, pure-state source contract, and conditional complete-reset condition are material to that statement.

The comparison does not establish an optimal gate exponent, a persistent-memory-width theorem, a noisy-device result, or a matching law at every dimension. Those claims are not needed for the theorem and are not inferred from neighboring papers.

Structured citation metadata for the directly used sources is available in [sources.bib](sources.bib). Page-specific references identify the exact argument supported by each source.
