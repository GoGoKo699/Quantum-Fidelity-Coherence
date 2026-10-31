"""Finite Johnson-spectrum and integer-budget consistency checks.

Run from the repository root: python3 verification/block_checks.py
These finite checks supplement, and do not replace, the analytical proofs.
"""
from pathlib import Path


import itertools
import json
import math

import numpy as np


def check_johnson_spectrum():
    """Compare direct Gram-matrix spectra with the asserted eigenvalue list."""
    worst = 0.0
    cases = 0
    for r in range(1, 4):
        for s in range(r, 6):
            n = r + s
            subsets = [set(a) for a in itertools.combinations(range(n), r)]
            distance = np.array([[len(a - b) for b in subsets] for a in subsets])
            for f in (0.0, 0.01, 0.3, 0.9, 1.0):
                actual = np.linalg.eigvalsh(f**distance)
                predicted = []
                for k in range(r + 1):
                    h = math.comb(n, k) - (math.comb(n, k - 1) if k else 0)
                    eigenvalue = (1 - f)**k * sum(
                        math.comb(r - k, j) * math.comb(s - k, j) * f**j
                        for j in range(r - k + 1)
                    )
                    predicted.extend([eigenvalue] * h)
                residual = float(np.max(np.abs(actual - np.sort(predicted))))
                assert residual < 1e-10, (r, s, f, residual)
                worst = max(worst, residual)
                cases += 1
    return cases, worst


def check_copy_budget():
    """Check the integer ceilings and finite-precision copy-bound constants."""
    for exponent in range(3, 11):
        eps = 2.0**(-exponent)
        eta = eps / 2
        for b in range(2, 2049):
            m = min(b // 2, math.ceil(eta**-2))
            K = math.ceil(6 / (m * m * eta**4) + 12 / (m * eta**2))
            assert 2 * m * K <= 160 / eps**2 + 576 / (b * eps**4)
            assert 2 * m <= b
    return 8 * 2047


if __name__ == "__main__":
    cases, worst = check_johnson_spectrum()
    budgets = check_copy_budget()
    result = {
        "johnson_eigenvalue_cases": cases,
        "maximum_eigenvalue_residual": worst,
        "copy_bound_cases": budgets,
        "status": "passed",
    }
    Path(__file__).with_name("block_checks_results.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))
