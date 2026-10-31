# What the coherence requirement means

The [main theorem](model.md) identifies the size of coherent runs needed for uniformly accurate root-fidelity estimation in high dimension. Its upper bound uses an existing collective measurement. Its converse shows that changing the measurement adaptively, while retaining only classical information between runs, cannot improve the order of the copy cost.

## 1. Precision and coherent processing

In the matching dimension regime,

```math
N_b(\epsilon,d)
=\Theta\!\left(\epsilon^{-2}+\frac{1}{b\epsilon^4}\right).
\qquad\text{(1)}
```

The two terms have different roles. The first is the intrinsic cost of learning a continuous parameter from independent quantum inputs. The second is the penalty for resetting the quantum information too often.

| Run cap, with integer rounding understood | Total-copy order |
| --- | --- |
| $`b=\Theta(1)`$, $`b\ge2`$ | $`\epsilon^{-4}`$ |
| $`b=\Theta(\epsilon^{-\alpha})`$, $`0<\alpha<2`$ | $`\epsilon^{-(4-\alpha)}`$ |
| $`b=\Omega(\epsilon^{-2})`$ | $`\epsilon^{-2}`$ |

Each row refers to a family of dimensions satisfying the theorem's sufficient condition. At a fixed small dimension, the table need not apply.

The construction collects $`m`$ copies from each source, obtains one Schur label, and resets. Near orthogonality its cross-SWAP score has variance $`1/m^2`$. With $`K`$ runs, an error of order $`\epsilon`$ in root fidelity requires resolving squared overlap on the scale $`\epsilon^2`$. The variance contribution is therefore of order $`1/(Km^2\epsilon^4)`$. Since the total copies are $`2mK`$, the resulting cost is of order $`1/(m\epsilon^4)`$ until the intrinsic $`\epsilon^{-2}`$ cost takes over.

This explains the upper bound. The reason it is optimal is stronger: the [block identity](block_information.md) bounds the information of every possible run measurement, and the [fixed-source comparison](haar_comparison.md) controls the benefit obtainable from learning the common orientation through the classical history.

## 2. Why the estimation target matters

The root fidelity is $`F=\sqrt f`$, where $`f=\mathrm{tr}(\rho\sigma)`$. For nearly orthogonal pairs, changing $`F`$ by order $`\epsilon`$ changes $`f`$ by order $`\epsilon^2`$.

For squared overlap itself, a two-copy SWAP measurement has outcomes in $`\{-1,1\}`$, mean $`f`$, and variance at most one. Repeating it $`O(\delta^{-2})`$ times estimates $`f`$ to additive error $`\delta`$ with constant success. A run cap of two already suffices for that dimension-independent rate.

The present theorem uses an additive error in $`F`$, uniformly down to $`F=0`$. Substituting $`\delta=\epsilon`$ would answer a different question. Substituting $`\delta=\epsilon^2`$ in the SWAP estimate is valid for the root target but costs $`O(\epsilon^{-4})`$ copies, exactly the constant-run regime in (1).

The pointwise and average-case questions are also distinct. A promise that $`F`$ is bounded away from zero removes the square-root singularity from local error propagation. A prior supported mostly on tiny fidelities can make the constant estimate zero successful at coarse additive accuracy. Neither observation contradicts the uniform minimax theorem.

## 3. Why the dimension restriction is real

The converse bounds the advantage of a shared fixed orientation by a term of order $`N^2/d`$. The sharp curve follows when the dimension is large enough that classical observations from the number of available copies cannot overcome this bound.

There is a concrete low-dimensional contrast. For two pure qubits, separate single-copy Pauli measurements already permit root-fidelity estimation with $`O(\epsilon^{-2})`$ copies:

1. Estimate the three Bloch coordinates of each state to Euclidean error at most $`\delta`$, using repeated $`X,Y,Z`$ measurements. Six groups of independent bounded outcomes suffice with $`O(\delta^{-2})`$ total copies and joint success probability at least $`2/3`$, by Hoeffding's inequality and a union bound.
2. Normalize each nonzero estimated Bloch vector to length one; for a zero estimate, choose any fixed unit vector. On the successful event, the initial vector estimate differs from the true unit vector by at most $`\delta<1`$, so it is nonzero and normalization increases that difference to at most $`2\delta`$.
3. The corresponding pure-qubit estimate is within trace distance $`\delta`$ of the true state. For pure vectors, optimal phase alignment gives Euclidean vector error at most $`\sqrt2`$ times that trace distance.
4. The reverse triangle inequality for the inner product then bounds the root-fidelity error by $`2\sqrt2\,\delta`$. Choose $`\delta=\epsilon/(4\sqrt2)`$, making this error at most $`\epsilon/2`$, and round the resulting fidelity to a finite binary value within $`\epsilon/2`$. This proves the claim with the same $`O(\epsilon^{-2})`$ copy count.

Every copy in this construction can be measured and discarded immediately. Thus a dimension-independent $`\Omega(\epsilon^{-4})`$ lower bound for bounded runs would be false. The dimension condition in the high-dimensional theorem is part of its substance.

For an $`n`$-qubit input, the dimension is $`2^n`$. The theorem is consequently relevant to families in which precision and run size scale polynomially with $`n`$ while dimension grows exponentially. This is an interpretation of the stated inequalities, not an additional algorithmic speedup claim.

## 4. Classical information and quantum memory

The converse allows unlimited classical data and unrestricted choices based on it. It applies even if a run uses a different measurement after every previous outcome. The complete-reset condition is what prevents those choices from carrying an unmeasured quantum state into the future.

A small persistent quantum register can violate this condition while using little simultaneous memory. Conversely, a run can use a large workspace and still obey the constraint if all source-dependent quantum information is removed at its end. The result therefore identifies a resource in the temporal organization of measurements; it is not a lower bound on qubit width.

Independent-copy access is equally important. If the source instead supplied coherent preparation and its inverse, amplitude-estimation or reflection-based methods would operate in a different query model. The theorem counts supplied unknown-state copies and does not identify those queries with free copies.

## 5. What is added to the earlier collective-measurement picture

Fanizza et al. already showed that collective overlap measurements outperform independent SWAP tests near small overlap, and they explicitly proposed grouping copies. The upper-bound measurement and that implementation idea are inherited.

The result here specifies the whole high-dimensional copy tradeoff under a complete-reset constraint and proves it against arbitrary adaptive protocols. It also gives a necessary run size for retaining the unrestricted optimal copy order. The mathematical comparison is finite-error and uniform, so its conclusion does not depend on applying a regular Fisher-information approximation at a boundary point.

The [related-work account](../references/related_work.md) also credits the earlier likelihood-comparison strategy, the polynomial inequalities, and the efficient Schur transform. These ingredients support the theorem without turning into claims of new algorithms or new inequalities.
