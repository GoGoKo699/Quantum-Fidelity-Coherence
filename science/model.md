# Model and principal result

How much joint quantum processing is necessary to estimate the similarity of two unknown quantum inputs? The answer depends on what information survives between acquisitions. We study the number of copies consumed before the processor must return to a state containing only classical information about the inputs.

The statistical target is **root fidelity**. For pure states this is the magnitude of their inner product. Taking a square root changes the uniform estimation problem near orthogonal states, so the target and error convention must be specified before comparing sample costs.

## 1. Sources, error, and charged resources

There are two fixed, unknown unit vectors $|\psi\rangle,|\phi\rangle\in\mathbb C^d$, $d\ge2$, with density operators $\rho$ and $\sigma$. A source request returns one independent register in $\rho$ or $\sigma$, according to a **classical** request label. All requests in the entire experiment concern the same pair of states.

The request label may be chosen using classical randomness, earlier runs, and measurements made within the current run. A source does not supply a coherent controlled preparation, a preparation inverse, a reflection about its state, a conjugated copy, or a classical description. A superposition of source labels with phase-coherent preparation would be a different access model.

Define

$$
F=|\langle\psi|\phi\rangle|,
\qquad f=F^2=\operatorname{tr}(\rho\sigma).
\tag{1}
$$

A protocol must return a finite classical estimate $\widehat F$ satisfying

$$
\Pr_{\psi,\phi}\{|\widehat F-F|\le\epsilon\}\ge\frac23
\quad\text{for every fixed pair }(\psi,\phi).
\tag{2}
$$

Probability is over measurements and the protocol's own randomness. A minimax guarantee such as (2) includes nearly orthogonal pairs; it is neither an average over typical states nor a pointwise asymptotic variance statement.

Each supplied copy is counted. The total copy budget $N$ is a deterministic upper bound along every execution history, including histories on which the estimate fails. We do not substitute an expected stopping cost for this budget.

## 2. The complete-reset constraint

Fix an integer $b\ge2$. The protocol is divided into coherent runs. Each run consumes at most $b$ total copies from the two sources. Within that cap it may use arbitrary joint quantum operations, known ancillas, measurements, feedback, and classical choices of subsequent source requests. Run lengths and stopping decisions may depend on the observed data.

At a boundary, **the complete classical history is the only input-dependent resource carried forward**. More precisely, conditioned on that history, the joint state of every quantum register retained by the processor or set aside as an aid for later runs must be a state specified by the protocol independently of the unknown input pair. Such a state can be freshly prepared at the next run. This permits history-dependent known ancillas but rules out an unknown quantum posterior surviving the reset. The condition applies to retained workspace and ancillary aids, not to new copies returned by later source requests.

The condition concerns joint conditional states, not only single-register marginals. For example, an entangled half set aside for later use may have an input-independent unconditional marginal while retaining input information conditional on earlier outcomes. Such a resource crosses the quantum boundary and is excluded.

Classical memory, computation, and adaptation are unrestricted in the lower bound. Source-independent advice can be incorporated into a run's measurement. Standard Borel outcome spaces and measurable instruments are allowed. Protocols terminate almost surely; operations or empty runs that acquire no source copies can be absorbed into the relevant quantum-to-classical channel or classical postprocessing.

The resource $b$ is therefore **consumed copies per complete quantum reset**. It is not the simultaneous number of stored copies, the number of elementary gates, the duration of a run, or an entanglement-depth bound on one prepared state. A small unknown quantum register carried through many arrivals belongs to a long coherent run.

Let $N_b(\epsilon,d)$ be the smallest worst-case copy budget among protocols obeying these rules and (2).

## 3. Main theorem

**Theorem 1.** For integers $d\ge2$, $b\ge2$, and $0<\epsilon\le1/8$,

$$
\boxed{
\max\left\{
\frac{1}{144\epsilon^2},
\frac{1}{65536}
\min\left\{\sqrt d,\frac{1}{b\epsilon^4}\right\}
\right\}
\le N_b(\epsilon,d)
\le
\frac{160}{\epsilon^2}+\frac{576}{b\epsilon^4}.
}
\tag{3}
$$

The upper bound returns finite binary output and allows approximate elementary-gate implementations, with success at least $3/4$. Its constants are deliberately conservative. The lower bound allows arbitrary run measurements and unlimited classical adaptation.

In particular, put

$$
X_b(\epsilon)=\epsilon^{-2}+\frac{1}{b\epsilon^4}.
\tag{4}
$$

Whenever $d\ge X_b(\epsilon)^2$,

$$
\boxed{
N_b(\epsilon,d)=\Theta\!\left(
\epsilon^{-2}+\frac{1}{b\epsilon^4}
\right),
}
\tag{5}
$$

with constants independent of $b,d,\epsilon$ in the stated domain. This is a sufficient dimension condition, not a claimed necessary threshold. More directly, the second term in (3) becomes $1/(65536b\epsilon^4)$ as soon as $\sqrt d\ge1/(b\epsilon^4)$.

The gap between the two sides of (3) at smaller dimensions is explicit. No matching minimax formula for every $d$ is claimed.

### Proof route

The [estimator](estimator.md) measures the collective cross-SWAP observable using weak Schur sampling and gives the upper bound, including output and circuit errors.

The [one-block information calculation](block_information.md) shows that a fresh common-orientation block with $r$ and $s$ copies has relative entropy at most $rsF^4$ between root fidelity $F$ and zero.

The [Haar comparison](haar_comparison.md) bounds how much an adaptive classical transcript can distinguish a single fixed orientation from independent orientations across padded runs.

The [adaptive converse](adaptive_converse.md) combines these facts while handling source choices, variable run lengths, and stopping. It also proves the unconditional $\epsilon^{-2}$ bound directly.

## 4. The sample-optimality threshold

The principal operational consequence needs a milder dimension assumption than the sufficient condition for the whole curve.

**Corollary 2.** Suppose a permitted protocol satisfies (2), uses at most $N\le C_0\epsilon^{-2}$ copies for some $C_0\ge1$, and

$$
d\ge2304C_0^2\epsilon^{-4}.
\tag{6}
$$

Then its run cap must satisfy

$$
\boxed{
b\ge\frac{1}{16384C_0\epsilon^2}.
}
\tag{7}
$$

Conversely, choosing $b$ of order $\epsilon^{-2}$ in the estimator achieves total copies of order $\epsilon^{-2}$. Thus optimal sample scaling requires coherent runs of that order in this dimension regime. The constants in (6)–(7) are proof constants, not proposed hardware design values.

The [converse](adaptive_converse.md#5-the-sample-optimality-threshold) gives the derivation. The [interpretation](interpretation.md) explains the distinction from ordinary squared-overlap estimation and the limits of the resource claim.

## 5. Computational and physical scope

The lower bound is information theoretic. It gives arbitrary computation for free, so classical computational power cannot evade it within the model.

The upper bound has a computational implementation when each source register has a known encoding in $\lceil\log_2d\rceil$ qubits. For $m$ copies of each state per run and $K$ runs, it uses

$$
2mK\ \text{copies},\qquad
K\,\operatorname{poly}(m,\log d,\log K)\ \text{elementary gates}.
\tag{8}
$$

The polynomial Schur transform is inherited from Krovi; its approximation and ancillary-workspace costs are included in the [estimator's resource account](estimator.md#4-gate-workspace-and-precision-account). An external physical preparation cost per source copy multiplies the charged copy count. No state-loading operation is supplied without charge.

The theorem treats pure, identical copies and ideal quantum operations with controlled synthesis error. It establishes a copy tradeoff under an explicit reset rule. Gate optimality, noisy-source robustness, arbitrary mixed states, simultaneous-memory-width tradeoffs, and fidelity to a classically specified reference are separate problems.

## Attribution

Fanizza et al. already established the collective overlap measurement, its efficient implementation, the qualitative small-overlap advantage, and explicit grouping with classical processing. Wang–Zhang established the unrestricted root-fidelity sample endpoint. The result here concerns the matching resource-constrained law and the converse against every allowed adaptive protocol. See the [related-work account](../references/related_work.md) for the exact shared foundations and differences.
