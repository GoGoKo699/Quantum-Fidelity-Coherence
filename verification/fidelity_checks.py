"""Finite mathematical consistency checks; not universal proofs."""
import itertools
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np


def cycles(p):
    seen = set()
    out = 0
    for i in range(len(p)):
        if i in seen:
            continue
        out += 1
        j = i
        while j not in seen:
            seen.add(j)
            j = p[j]
    return out


def haar_gaussian_covariance(d, t, columns=2):
    """Check all homogeneous monomials in the first columns, via Weingarten."""
    perms = list(itertools.permutations(range(t)))
    inv = [tuple(p.index(i) for i in range(t)) for p in perms]
    gram = np.array([[float(d ** cycles(tuple(a[b[i]] for i in range(t))))
                      for b in perms] for a in inv])
    wg = np.linalg.inv(gram)
    mon = list(itertools.combinations_with_replacement(range(d * columns), t))
    rows = [tuple(v // columns for v in x) for x in mon]
    cols = [tuple(v % columns for v in x) for x in mon]
    h = np.zeros((len(mon), len(mon)))
    gdiag = np.array([math.prod(math.factorial(n) for n in Counter(x).values()) / d**t for x in mon])
    for i in range(len(mon)):
        for j in range(i, len(mon)):
            rp = np.array([all(rows[i][k] == rows[j][p[k]] for k in range(t)) for p in perms], float)
            cp = np.array([all(cols[i][k] == cols[j][p[k]] for k in range(t)) for p in perms], float)
            h[i, j] = h[j, i] = rp @ wg @ cp
    normalized = h / np.sqrt(gdiag[:, None] * gdiag[None, :])
    vals = np.linalg.eigvalsh(normalized)
    lo = d**t / math.prod(d + j for j in range(t))
    hi = d**t / math.prod(d - j for j in range(t))
    assert vals[0] >= lo - 1e-10
    assert vals[-1] <= hi + 1e-10
    return {'d': d, 'degree': t, 'columns': columns, 'monomials': len(mon),
            'observed_min': float(vals[0]), 'observed_max': float(vals[-1]),
            'bound_min': lo, 'bound_max': hi}


def swap_statistic(m, f):
    """Direct 2m-qubit tensor calculation, independent of counting formula."""
    psi = np.array([1., 0.])
    phi = np.array([math.sqrt(f), math.sqrt(1-f)])
    v = np.array([1.])
    for z in [psi] * m + [phi] * m:
        v = np.kron(v, z)
    tensor = v.reshape((2,) * (2*m))
    av = sum(np.swapaxes(tensor, i, m+j).reshape(-1)
             for i in range(m) for j in range(m)) / m**2
    mean = float(v @ av)
    var = float(av @ av - mean**2)
    predicted = (1 + 2*(m-1)*f - (2*m-1)*f*f) / m**2
    assert abs(mean-f) < 1e-12
    assert abs(var-predicted) < 1e-12
    return max(abs(mean-f), abs(var-predicted))


def johnson_kernel(r, s, f, g):
    subsets = [set(x) for x in itertools.combinations(range(r+s), r)]
    dist = np.array([[len(a-b) for b in subsets] for a in subsets])
    gf, gg = f**dist, g**dist
    actual = float(np.sum(gf * gg.T) / len(subsets))
    expected = sum(math.comb(r,j)*math.comb(s,j)*(f*g)**j for j in range(min(r,s)+1))
    assert abs(actual-expected) < 1e-10
    assert np.linalg.eigvalsh(gf)[0] >= -1e-10
    return abs(actual-expected)


if __name__ == '__main__':
    results = {
        'purpose': 'Finite checks only; universal statements require analytical proof.',
        'haar_gaussian': [haar_gaussian_covariance(d,t) for d,t in [(3,2),(3,3),(4,3),(5,3)]],
        'swap_statistic_max_residual': max(swap_statistic(m,f) for m in range(1,6)
                                             for f in [0.,.0001,.01,.2,.7,1.]),
        'johnson_kernel_max_residual': max(johnson_kernel(r,s,f,g) for r in range(1,4)
                                           for s in range(r,5) for f,g in [(.0,.3),(.01,.1),(.2,.7),(1.,1.)]),
        'status': 'passed'
    }
    out = Path(__file__).with_name('fidelity_checks_results.json')
    out.write_text(json.dumps(results, indent=2)+'\n')
    print(json.dumps(results, indent=2))
