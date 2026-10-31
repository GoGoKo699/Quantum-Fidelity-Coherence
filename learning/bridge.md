# From Watrous to Quantum Fidelity Coherence

Two sources each repeatedly produce copies of their own fixed unknown pure state. The task is to estimate how similar those states are while limiting how many source copies can contribute to one uninterrupted quantum computation. A classical notebook may grow without limit. The question is how often the quantum processor can be completely reset before that restriction increases the number of copies needed.

The single educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**, [DOI: 10.1017/9781316848142](https://doi.org/10.1017/9781316848142). The [author's book page](https://jhwatrous.github.io/books-and-courses.html) provides a manuscript and chapter links. That manuscript is supplied for personal use and may not be redistributed; this repository links to it and supplies original explanations.

This bridge identifies the portions of the book that support the problem, translates its conventions, and explains the additional arguments supplied by the project. The [30-milestone map](map.md) organizes the complete conceptual route. The [scientific account](../science/README.md) remains authoritative for theorem statements and proofs.

## 1. A focused route through the anchor

These are entry points within one book, not a requirement to read it from beginning to end. Section numbers below refer to the author's standard-layout manuscript.

| Book location | What to take from it | Project connection |
| --- | --- | --- |
| [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), Sections 2.1 and 2.1.2 | Registers, density operators, pure states, and compound systems | Interpret a source call as one supplied register in the [model](../science/model.md). |
| [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), Sections 2.2.1 and 2.3.1 | Channels, replacement channels, measurements, and classical outcomes | Understand how an entire run becomes a measurement on its input stock, and why a reset must remove all conditional quantum information. |
| [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), Section 3.2.1, following Definition 3.11 | Root fidelity and its pure-state specialization | Identify the parameter being estimated before comparing sample bounds. |
| [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), Section 3.1.1 | Distinguishing two states and the operational role of the trace norm | Turn an accurate estimator into a binary test in the [adaptive converse](../science/adaptive_converse.md). |
| [Chapter 5](https://jhwatrous.github.io/TQI.5.pdf), Sections 5.1.1–5.1.2 and 5.2.3 | Relative entropy, classical Pinsker inequality, and quantum data processing; especially Theorems 5.15 and 5.35 | Interpret the [block-information bound](../science/block_information.md) and the information accumulated by a classical transcript. |
| [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), Section 7.1, especially 7.1.1 | Permutations of tensor factors and symmetric subspaces | Understand why identical copies carry permutation symmetry and why SWAP observables are natural. |
| [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), Section 7.2.1 | Uniform spherical and Haar measures | Understand a common random orientation and distinguish averaging over that orientation from physically changing the sources. |

The book supplies the language of states, measurements, distinguishability, and symmetry. The detailed two-row Schur analysis, Johnson kernel, homogeneous-polynomial comparison, and adaptive fixed-stock reduction are developed in the project and its primary research references.

## 2. Translate the conventions before using a theorem

### Root fidelity and squared overlap

Watrous defines fidelity using the trace norm of a product of positive square roots. For this project's pure states, that convention gives

```math
F(\rho,\sigma)
=\left\|\sqrt\rho\sqrt\sigma\right\|_1
=|\langle\psi|\phi\rangle|.
```

Here the supplied states are

```math
\rho=|\psi\rangle\langle\psi|,
\qquad
\sigma=|\phi\rangle\langle\phi|.
```

The project reserves a lowercase symbol for their squared overlap:

```math
f=\mathrm{tr}(\rho\sigma)=F^2.
```

An additive error in one parameter is not the same requirement as an additive error in the other. Near orthogonality, root fidelities zero and a small positive value of order epsilon have squared overlaps separated only by order epsilon squared. This is why the square root must be handled uniformly at zero in the [estimator](../science/estimator.md).

### Distances and logarithms

The project uses trace distance with the factor one half, and the same convention for classical total variation:

```math
T(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1,
\qquad
\mathrm{TV}(p,q)=\tfrac12\sum_y|p_y-q_y|.
```

A measurement cannot produce classical total variation larger than the input trace distance. For equal prior probabilities, the optimal binary-testing success is one half plus one half of the appropriate distance. These are the operational connections developed in Watrous Section 3.1.1.

Watrous uses base-two logarithms for entropy. The project's relative entropies use natural logarithms. If the book's value is denoted by a subscript 2, the conversion is

```math
D_{\mathrm{nat}}=(\ln 2)D_2.
```

Thus the classical Pinsker inequality appears here as

```math
\mathrm{TV}(p,q)\le\sqrt{D_{\mathrm{nat}}(p\Vert q)/2}.
```

Data processing has the same direction under either convention; numerical constants involving entropy require this conversion.

### Objects and resources

| Notion in the anchor | Meaning in this project |
| --- | --- |
| A finite-dimensional register | One source copy has Hilbert-space dimension `d`; the dimension is distinct from the number of copies. |
| A pure state, written as a unit vector or its rank-one density operator | Each source has one fixed unknown state, and successive requests return independent identical copies. |
| A measurement with positive effects summing to the identity | One run may contain an arbitrary circuit and intermediate measurements; its final classical transcript is described by an effective measurement on the supplied copies. |
| A channel replacing an input by a specified state | At a boundary, the joint state of all retained or reserved processor systems must be preparable from the classical history, without additional unknown quantum information. |
| A permutation of tensor factors | A SWAP exchanges two source registers; sums of such operators can be measured collectively. |
| Haar averaging | The proof averages a common unitary acting on both states. It preserves their overlap and describes a prior over legal fixed inputs. |

The run cap `b` counts **total source copies consumed between complete resets**. It does not count simultaneous qubits, circuit depth, or physical duration. A small quantum memory retained across many source arrivals is part of one long coherent run. Checking each retained register's unconditional marginal is insufficient: joint correlations and states conditional on the complete classical history also matter. The [model](../science/model.md) states the exact boundary condition.

The textbook's general channel formalism does not grant additional source access. This project supplies no preparation unitary, its inverse, reflection about an unknown state, coherent source-selection query, or QRAM.

## 3. A complete two-copy example

Take two states in a two-dimensional subspace:

```math
|\psi\rangle=|0\rangle,
\qquad
|\phi\rangle=\tfrac12|0\rangle+\tfrac{\sqrt3}{2}|1\rangle.
```

Their root fidelity is one half and their squared overlap is one quarter. These expressions specify the example for analysis; the measurement need not know them.

A run requests one copy from each source and measures the SWAP operator `S`. It has outcomes +1 and −1, with projectors

```math
\Pi_+=(I+S)/2,
\qquad
\Pi_-=(I-S)/2.
```

The identity

```math
\mathrm{tr}\bigl(S(\rho\otimes\sigma)\bigr)
=\mathrm{tr}(\rho\sigma)=f
```

gives the probabilities

```math
\Pr(+1)=(1+f)/2=5/8,
\qquad
\Pr(-1)=(1-f)/2=3/8.
```

Each run consumes two copies. After recording its sign, the processor discards both quantum registers and any source-dependent workspace. Only the classical record remains.

For a concrete possible record, suppose eight runs produce five positive signs and three negative signs. The mean score is

```math
\overline X=(5-3)/8=1/4.
```

Clip this mean to the interval from zero to one, then take its square root. The resulting estimate is one half. This particular record happens to give the true value; eight runs do not provide an arbitrary-precision guarantee. Other records give different estimates. The procedure uses 16 total copies and obeys a run cap of two. In general, its single-run score has mean `f` and variance `1-f²`; the [estimator's uniform error bound](../science/estimator.md#2-a-uniform-conversion-from-squared-overlap-to-root-fidelity) controls repetition for every possible input pair.

This example can be embedded in any dimension at least two. Its simple support does not establish the dimension condition in a worst-case lower bound.

## 4. What collective processing changes

With two copies from each source, a four-copy run measures

```math
A_2=(S_{1,3}+S_{1,4}+S_{2,3}+S_{2,4})/4.
```

This is one observable. The individual swaps in the sum do not all commute; performing four separate SWAP measurements would be a different operation. The existing collective Schur measurement implements the observable by reading a sector label and assigning its corresponding score.

At orthogonal inputs, the three possible scores and probabilities are:

| Score | Probability |
| ---: | ---: |
| −1/2 | 1/3 |
| 0 | 1/2 |
| 1 | 1/6 |

The scores have mean zero and variance one quarter. A two-copy SWAP score at orthogonality has variance one. More generally, a run containing `m` copies from each source has variance exactly `1/m²` at orthogonality. The project derives the full variance formula in [estimator Section 1](../science/estimator.md#1-the-observable-measured-in-one-run).

This variance reduction explains the constructive benefit of collecting more copies before resetting. Averaging independent runs suppresses noise further, while the square-root conversion determines how accurate the squared-overlap estimate must be. The finite algorithm also budgets circuit approximation, output rounding, and all supplied copies.

The collective measurement, its small-overlap advantage, and grouping copies were established by **Fanizza et al.** The present argument uses that construction; it does not claim a new SWAP or Schur measurement. **Krovi's** Schur transform supplies the gate-efficiency ingredient, and **Wang–Zhang** established the unrestricted root-fidelity sample endpoint. The [related-work account](../references/related_work.md) gives the exact primary references and claim boundaries.

## 5. The steps from textbook tools to a universal converse

An estimator supplies an upper bound. Proving that every allowed adaptive strategy needs comparable resources requires more than evaluating that estimator's variance.

**First, quantify all the information in a single random-orientation block.** A common unitary rotates both sources, preserving their overlap. Permutation symmetry organizes the averaged state into orthogonal sectors whose normalized internal states are independent of the overlap. Every measurement therefore reads a classical postprocessing of the sector label. The [block calculation](../science/block_information.md) derives an exact chi-square kernel and concludes that a block with source counts `r` and `s` has relative entropy at most `rsF⁴` against orthogonal inputs. Watrous supplies symmetry and data processing; the explicit sector probabilities and kernel require the project's additional calculation.

**Second, preserve the distinction between fixed and refreshed sources.** In the physical problem, the source pair stays fixed. Earlier classical observations can reveal its orientation. Resetting the processor does not reset that classical knowledge. Treating each run as an independent orientation average would skip a necessary argument. The [Haar comparison](../science/haar_comparison.md) instead controls the complete transcript law using homogeneous polynomial norms and the Bombieri product inequality. Its error is of order total copies squared divided by dimension. This is a bound on accessible classical transcripts under the reset rule, not a claim that the two unrestricted quantum input states are close.

**Third, cover adaptive requests and stopping.** A strategy may decide which source to request during a run. Its final source counts cannot simply be substituted into a theorem whose input allocation was fixed in advance. The [adaptive converse](../science/adaptive_converse.md#2-a-fixed-stock-simulation-of-arbitrary-source-choices) groups complete runs and supplies a sufficiently large fixed stock from each source. The original strategy can select unused registers from that stock. Padding and discarded copies make the argument apply to every history while preserving the original output law.

**Finally, reduce estimation to testing.** Two legal fixed-pair ensembles have root fidelities zero and four times the requested error. Uniformly accurate estimates distinguish them with constant advantage. The block-information bound, fixed-orientation comparison, and data processing limit that advantage when the copy budget is too small. A separate two-state trace-distance argument supplies the intrinsic inverse-square precision cost at every dimension.

The representation and polynomial arguments are research-level proof steps. The anchor makes their objects and purpose accessible, but does not by itself prove this resource-constrained result. The project states and proves the required comparisons and credits the inherited inequalities and earlier adaptive likelihood method.

## 6. Read the conclusion with its assumptions

For integer run caps at least two, error at most one eighth, and a sufficiently large dimension, the resulting total-copy order is

```math
N_b(\epsilon,d)
=\Theta\!\left(\epsilon^{-2}+\frac{1}{b\epsilon^4}\right).
```

A sufficient dimension condition is

```math
d\ge\left(\epsilon^{-2}+\frac{1}{b\epsilon^4}\right)^2.
```

The [principal theorem](../science/model.md#3-main-theorem) gives explicit upper and lower constants and the finite-dimensional gap. It also gives a milder dimension condition for the narrower conclusion that optimal total-copy scaling needs runs of inverse-square precision size.

The dimension qualification changes the answer. For pure qubits, separate single-copy tomography followed by suitable normalization achieves inverse-square precision scaling for root fidelity; the [worked argument](../science/interpretation.md#3-why-the-dimension-restriction-is-real) explains why this is compatible with the high-dimensional theorem. The present law is not a matching formula at every dimension.

The result concerns uniform error in root fidelity, pure fixed copy sources, and complete conditional resets. Mixed states, coherent preparation access, persistent quantum memory, and device noise require their own models and analyses. With those boundaries in view, continue through the [milestone map](map.md), or go directly to the [connected scientific proof](../science/README.md).
