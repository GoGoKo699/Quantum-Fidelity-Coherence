# Scientific account

The question is how many unknown-state copies must be processed before a complete quantum reset to retain optimal root-fidelity sample complexity.

The answer is a matching high-dimensional law for fixed pure inputs, including arbitrary classical adaptation. The proof separates information available within one coherent run from information about the common orientation accumulated across runs.

## Reading route

| Page | Main content |
| --- | --- |
| [Model and principal result](model.md) | Source contract, conditional reset rule, minimax error, finite-dimension bounds, and the optimal-copy threshold |
| [Bounded-run estimator](estimator.md) | Cross-SWAP variance, Schur outcome score, uniform root-error conversion, finite output, and gate/error accounting |
| [Exact block information](block_information.md) | Subset representations, Johnson eigenvalues, Schur sufficiency, exact chi-square kernel, and global relative entropy |
| [Haar comparison](haar_comparison.md) | Full polynomial-sector normalization, Bombieri inequality, measurable transcript refinement, and fixed-versus-refreshed comparison |
| [Adaptive converse](adaptive_converse.md) | Padded superblocks, arbitrary internal source choices and stopping, explicit lower-bound constants, and sample-optimality threshold |
| [Interpretation](interpretation.md) | Precision dependence, the low-dimensional contrast, and the operational meaning of a complete reset |

For a short route, read the model, estimator Sections 1–3, adaptive converse Sections 1–5, and interpretation. The two representation-theoretic pages supply the complete supporting arguments.

## Proof dependencies

The upper bound uses the exact moments of a single collective observable and an inherited efficient Schur transform. The lower bound uses an exact block-divergence calculation, an algebraic stationary-to-refreshed transcript comparison, and a fixed-stock simulation. The latter avoids treating adaptively selected source counts as if they had been fixed before a measurement.

The [related-work account](../references/related_work.md) identifies the imported ingredients. The [verification guide](../verification/README.md) provides finite checks of the operator moments, Gram spectra, and polynomial norms. Those checks complement the analytical arguments; they do not replace them.
