# Reproducible verification

The analytical statements are proved in [science](../science/README.md). The scripts here check concrete consequences by different finite constructions: direct tensor operations, explicit Gram-matrix diagonalization, and Weingarten integration of polynomial covariances.

## Run

From the repository root, using Python 3.12:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/fidelity_checks.py
python3 verification/block_checks.py
```

The recorded run used Python 3.12.14 and NumPy 2.3.5. If the pinned dependency is already installed, no installation is needed. Each script exits unsuccessfully on a failed assertion and prints its metrics. Run normally, without Python's assertion-disabling optimization flag.

The scripts write ignored local result files beside themselves. The committed [expected_results.json](expected_results.json) records the observed metrics and hashes of the checked source scripts. Floating-point residuals may vary slightly with the numerical library; the stated tolerances, rather than exact residual bytes, define the checks.

## What is checked

| Calculation | Independent construction | Scope and observed outcome |
| --- | --- | --- |
| Cross-SWAP moments | Build the full pure tensor vector and apply register permutations directly | $`m=1,\ldots,5`$, six squared overlaps including both endpoints; maximum residual $`4.45\times10^{-16}`$ |
| Johnson kernel | Build subset-distance Gram matrices and take their trace products | Balanced and unbalanced finite counts; maximum residual $`6.67\times10^{-16}`$; positive semidefiniteness checked |
| Johnson eigenvalues | Diagonalize the full Gram matrix and compare with the explicit two-row eigenvalue/multiplicity list | 60 cases; maximum residual $`2.87\times10^{-14}`$ |
| Haar–Gaussian norm comparison | Construct the full homogeneous-monomial covariance on two matrix columns using Weingarten inversion, then compare generalized eigenvalues | $`(d,t)=(3,2),(3,3),(4,3),(5,3)`$, with 21, 56, 120 and 220 monomials; all tested norms inside the proved bounds |
| Integer copy budget | Evaluate the actual ceilings in the finite-precision algorithm | 16,376 pairs of error and run-cap parameters; all obey the stated copy and run bounds |

The tensor and Gram checks compare different mathematical representations of the same quantities. The copy-budget check protects the implementation of integer rounding; its role is narrower than the operator and covariance checks.

## Limits of this evidence

These are finite deterministic numerical checks. They do not certify all dimensions, all protocols, or all complex polynomials. In particular, an exponential number of adaptive histories is handled by the written likelihood argument, not by simulation.

The proof review covers the source-access contract, conditional reset rule, arbitrary within-run allocation and stopping, Haar/Gaussian sector constants, continuous-outcome refinement, and the direction of the square-root error bound. The implementation account invokes Krovi's published Schur-transform algorithm; no complete gate-level circuit or noisy-device experiment is supplied.

Repository navigation and source mathematics are reviewed separately from these numerical checks. A local pass is not evidence that a hosting renderer displays every formula correctly.
