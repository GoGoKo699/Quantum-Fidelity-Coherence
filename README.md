# Quantum Fidelity Coherence

How many unknown-state copies must be processed coherently before a complete quantum reset to estimate their similarity efficiently?

This repository develops a matching high-dimensional copy law for estimating **root fidelity** between two fixed unknown pure states. Each coherent run consumes at most $`b`$ total source copies; only classical information survives between runs. Measurements and source requests may adapt to the complete classical history.

## Sister result: coherence for a loop phase

[Quantum Holonomy Sampling](https://github.com/GoGoKo699/Quantum-Holonomy-Sampling) asks how many copies are needed to estimate the phase around a loop of unknown pure states. Together the projects show that, for a sparse four-state cycle and fixed small phase error, copy-optimal $`N=O(c^{-2})`$ estimation requires runs consuming $`b=\Omega(c^{-2})`$ copies in a sufficient large-dimension regime. Here $`c`$ is the neighboring overlap amplitude.

The scientific exchange is precise: this repository owns the **fixed-source adaptive transcript comparison**, extended to arbitrary fixed pure stocks; Holonomy owns the **phase-specific block-information theorem** and coherent upper bound. The root-fidelity formula below is not a phase theorem. The [loop-phase application](science/loop_phase.md) states the distinct assumptions, dimension condition, proof route and fixed-dimensional tomography exception, with versioned links to the authoritative phase proofs.

## Main result

For additive root-fidelity error $`\epsilon`$, constant success probability, $`b\ge2`$, and sufficiently large Hilbert-space dimension,

```math
N_b(\epsilon,d)
=\Theta\!\left(
\frac{1}{\epsilon^2}+\frac{1}{b\epsilon^4}
\right).
```

A sufficient dimension condition is

```math
d\ge\left(\epsilon^{-2}+\frac{1}{b\epsilon^4}\right)^2.
```

Constant-size coherent runs require order $`\epsilon^{-4}`$ copies. Runs of order $`\epsilon^{-2}`$ copies attain the unrestricted order $`\epsilon^{-2}`$ total-copy cost. The converse allows unlimited classical memory and arbitrary classical adaptation.

The resource $`b`$ counts **copies consumed between complete resets**. It does not measure simultaneous qubit width. The source contract supplies independent copies, with classical request labels, and no preparation unitaries or their inverses.

The [principal theorem](science/model.md) states the exact model, finite-dimensional bounds, and a milder dimension condition for the necessary run size at optimal sample cost.

## Read the science

| Question | Authoritative page |
| --- | --- |
| What is the exact task and resource model? | [Model and principal result](science/model.md) |
| Which estimator attains the rate? | [Bounded-run estimator](science/estimator.md) |
| How much information can any one run reveal? | [Exact block information](science/block_information.md) |
| Why can the lower bound handle fixed unknown states? | [Haar comparison](science/haar_comparison.md) |
| How are arbitrary source choices and stopping covered? | [Adaptive converse](science/adaptive_converse.md) |
| How does the transcript method establish a phase-specific sister result? | [Loop-phase application](science/loop_phase.md) |
| What does the threshold mean, and where does it cease to apply? | [Interpretation](science/interpretation.md) |

The [science index](science/README.md) gives the connected proof route. The [related-work account](references/related_work.md) credits the earlier collective measurement, grouping strategy, unrestricted endpoint, likelihood method, and implementation tools.

## Learn the project

The [learning guide](learning/README.md) starts from the estimation task and connects the two sides of the proof. Its [30-milestone map](learning/map.md) moves from the background framework to the estimator, the adaptive converse, and the theorem's limits.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [source-to-project bridge](learning/bridge.md) identifies the relevant sections, translates notation and assumptions, and explains which additional arguments this project supplies. The learning route is shared scientific material; no prior completion of the textbook is assumed.

## Verification

The [verification guide](verification/README.md) documents reproducible checks of direct tensor moments, Johnson-matrix spectra and kernels, and small Haar–Gaussian polynomial covariance matrices. These finite calculations check specific algebraic consequences; the universal claims rest on the written proofs.

From the repository root, with Python 3.12:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/fidelity_checks.py
python3 verification/block_checks.py
```

## Scope

The result concerns fixed pure-state inputs, a uniform additive error in root fidelity, and a classical-only boundary between coherent runs. A matching bound at every dimension, a persistent-memory-width lower bound, and a device-noise model are outside the theorem. A pure-qubit example in the interpretation page demonstrates why a dimension-free bounded-run lower bound would be false.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
