# Quantum Fidelity Coherence

How many unknown-state copies must be processed coherently before a complete quantum reset to estimate their similarity efficiently?

This repository develops a matching high-dimensional copy law for estimating **root fidelity** between two fixed unknown pure states. Each coherent run consumes at most $b$ total source copies; only classical information survives between runs. Measurements and source requests may adapt to the complete classical history.

## Main result

For additive root-fidelity error $\epsilon$, constant success probability, $b\ge2$, and sufficiently large Hilbert-space dimension,

$$
N_b(\epsilon,d)
=\Theta\!\left(
\frac{1}{\epsilon^2}+\frac{1}{b\epsilon^4}
\right).
$$

A sufficient dimension condition is

$$
d\ge\left(\epsilon^{-2}+\frac{1}{b\epsilon^4}\right)^2.
$$

Constant-size coherent runs require order $\epsilon^{-4}$ copies. Runs of order $\epsilon^{-2}$ copies attain the unrestricted order $\epsilon^{-2}$ total-copy cost. The converse allows unlimited classical memory and arbitrary classical adaptation.

The resource $b$ counts **copies consumed between complete resets**. It does not measure simultaneous qubit width. The source contract supplies independent copies, with classical request labels, and no preparation unitaries or their inverses.

The [principal theorem](science/model.md) states the exact model, finite-dimensional bounds, and a milder dimension condition for the necessary run size at optimal sample cost.

## Read the science

| Question | Authoritative page |
| --- | --- |
| What is the exact task and resource model? | [Model and principal result](science/model.md) |
| Which estimator attains the rate? | [Bounded-run estimator](science/estimator.md) |
| How much information can any one run reveal? | [Exact block information](science/block_information.md) |
| Why can the lower bound handle fixed unknown states? | [Haar comparison](science/haar_comparison.md) |
| How are arbitrary source choices and stopping covered? | [Adaptive converse](science/adaptive_converse.md) |
| What does the threshold mean, and where does it cease to apply? | [Interpretation](science/interpretation.md) |

The [science index](science/README.md) gives the connected proof route. The [related-work account](references/related_work.md) credits the earlier collective measurement, grouping strategy, unrestricted endpoint, likelihood method, and implementation tools.

## Verification

The [verification guide](verification/README.md) documents reproducible checks of direct tensor moments, Johnson-matrix spectra and kernels, and small Haar–Gaussian polynomial covariance matrices. These finite calculations check specific algebraic consequences; the universal claims rest on the written proofs.

## Scope

The result concerns fixed pure-state inputs, a uniform additive error in root fidelity, and a classical-only boundary between coherent runs. A matching bound at every dimension, a persistent-memory-width lower bound, and a device-noise model are outside the theorem. A pure-qubit example in the interpretation page demonstrates why a dimension-free bounded-run lower bound would be false.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
