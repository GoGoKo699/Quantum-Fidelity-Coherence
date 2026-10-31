# Learning the coherent-run tradeoff

Two sources repeatedly supply copies of their own fixed unknown pure states. A quantum processor may collect several copies, make a joint measurement, write down a classical result, and reset. How long must each coherent run be to estimate the states' similarity with the best possible total number of copies?

The distinction is between the quantum information available inside a run and the classical information retained afterwards. A reset removes the former; it does not erase the notebook. The project's central difficulty is to prove a lower bound even when that notebook guides every later measurement and source request.

## The common learning route

The [30-milestone map](map.md) defines the understanding targets and their dependencies. It uses **13 background/preliminaries milestones** to assemble the operational and mathematical framework, then **17 narrative/innovation milestones** to connect the estimator, converse, and interpretation. The map is determined by the scientific story and is independent of any reader's prior knowledge or progress.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [source-to-project bridge](bridge.md) points to specific parts of that book, translates notation and assumptions, and explains the missing steps to the theorem. It includes a complete two-copy measurement example and a four-copy collective comparison. Those examples provide a concrete starting point; reading the whole textbook is unnecessary.

| Milestones | Question that organizes the route | Main connection |
| --- | --- | --- |
| [M01–M07](map.md#m01) | What are the inputs, target, guarantee, and resource restriction? | Pure states and measurements become a precisely charged copy-estimation task. |
| [M08–M13](map.md#m08) | Which statistical and symmetry tools make this task tractable? | Testing, information inequalities, permutations, and common Haar orientation combine into the full experiment. |
| [M14–M17](map.md#m14) | How does collecting more copies before resetting improve an estimator? | A known collective measurement has a useful exact variance, followed by a uniform root-error and finite-precision guarantee. |
| [M18–M20](map.md#m18) | How much information can any measurement extract from one block? | Sector sufficiency and an exact Gram-matrix identity give a global divergence bound. |
| [M21–M26](map.md#m21) | Why does the converse remain valid for fixed inputs and adaptive requests? | Fixed stocks handle source choices; polynomial likelihood comparisons control the effect of a common orientation. |
| [M27–M30](map.md#m27) | What law follows, where does it apply, and what is inherited? | The two proof routes meet, with the dimension restriction, low-dimensional example, and attribution intact. |

## 1. Start with the target and the reset

Root fidelity is the magnitude of the inner product between the two pure-state vectors. Squared overlap is its square. A measurement may naturally estimate squared overlap, but the requested error is in root fidelity. Near orthogonal states, a small root-fidelity difference becomes an even smaller squared-overlap difference. This boundary behavior affects the number of copies required.

The run cap counts all source copies consumed before a complete quantum reset. A processor that keeps one unknown quantum register through many arrivals is still in one long run. At a permitted boundary, every retained or reserved quantum system must be jointly preparable from the complete classical history without the unknown inputs. This conditional requirement prevents hidden quantum information from surviving in correlations.

[M01–M13](map.md#m01) make these distinctions precise. The authoritative definitions are in the [model](../science/model.md); the [bridge's worked example](bridge.md#3-a-complete-two-copy-example) shows the copies, outcomes, reset, and final estimate in one small experiment.

## 2. Follow the constructive route

A two-copy SWAP measurement returns a noisy score whose mean is squared overlap. With several copies of each state available together, a collective measurement can use cross-copy symmetry to reduce the score variance. The project uses the collective Schur measurement and grouping idea already established by Fanizza and collaborators.

The next step is statistical: average independent run scores, clip the result to the allowed interval, and take a square root. The analysis must work uniformly, including at zero overlap. The finite algorithm also assigns explicit error budgets to circuit approximation and output rounding and counts the actual integer number of supplied copies.

This is the route through [M14–M17](map.md#m14) and the [estimator](../science/estimator.md). A variance calculation explains why the construction helps. It cannot by itself prove that every different strategy faces the same limitation.

## 3. Follow the impossibility route

The converse first asks how much one block can reveal when the pair's common orientation is unknown. Symmetry compresses its overlap dependence into a classical sector label. An exact kernel identity then limits the distinguishability of small nonzero root fidelity from zero for every block measurement.

The sources in the actual task stay fixed. Earlier outcomes can teach the protocol something about their orientation, and later runs may use that knowledge. Consequently, independently averaging the orientation anew in every run would analyze a different experiment. The proof supplies a comparison between the complete transcript distributions of the fixed and refreshed experiments, with an explicit dimension-dependent error.

Adaptive source selection introduces another issue: the final count from each source may depend on measurements. The proof groups complete runs and gives each group a sufficiently large fixed stock from both sources. Selecting from that stock simulates the original strategy, including variable run lengths and stopping. With these two issues resolved, an estimation-to-testing argument gives the lower bound.

[M18–M26](map.md#m18) connect these steps. The full proofs live in [block information](../science/block_information.md), [Haar comparison](../science/haar_comparison.md), and the [adaptive converse](../science/adaptive_converse.md).

## 4. Reunite the result with its scope

In the stated high-dimensional regime, constant-size coherent runs incur a fourth-power inverse-precision copy cost, while runs of inverse-square precision size attain inverse-square total-copy scaling. The [principal theorem](../science/model.md#3-main-theorem) gives the explicit finite-dimensional bounds and sufficient matching condition. Its [corollary](../science/model.md#4-the-sample-optimality-threshold) gives the necessary run length for optimal sample scaling under a milder dimension condition.

The dimension hypothesis is essential to interpreting the result. Pure qubits admit a single-copy tomography route with inverse-square scaling. The theorem also concerns pure copy sources and complete conditional resets; persistent quantum memory and coherent preparation oracles change the model.

[M27–M30](map.md#m27) synthesize the contribution and its boundaries. Finish with the [interpretation](../science/interpretation.md) and [related-work account](../references/related_work.md). The [verification guide](../verification/README.md) connects several algebraic claims to executable finite checks and explains why those checks complement the written universal proofs.

## Direct routes

- **A first concrete example:** [bridge Sections 3–4](bridge.md#3-a-complete-two-copy-example).
- **The fixed conceptual map:** [M01–M30](map.md).
- **The selected textbook and notation translation:** [source bridge](bridge.md#1-a-focused-route-through-the-anchor).
- **Exact statements and complete proofs:** [scientific account](../science/README.md).
- **Reproduction and evidence limits:** [verification](../verification/README.md).
