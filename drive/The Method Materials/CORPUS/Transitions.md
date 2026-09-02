# TRANSITIONS

### What an index can carry, and one cell that no index can

**Matthew Lach** — Independent researcher
Draft v3.0. Prepared with a computing collaborator under the protocols of The Method v1.4. **The artefact accompanying this source carries a v2.0 running footer on all 46 pages and predates it**; the source is the record and the artefact is stale until rebuilt.
Supersedes v2.0. Every correction in Part XI post-dates that draft.

---

## Abstract

For a finite set of integer tuples X we compute **E(X) = |R(X)| − |X|**, where R closes X under its monotone
pairwise envelopes. We prove R is a closure operator, that E ≥ 0, and that E = 0 is global consistency of a binary
constraint network. E then measures whether an index can carry a constraint, and we identify **two failure modes
and no third**.

**Sub-case A, ordering.** The term is present and determined but non-monotone. The eighteen-column periodic table
carries ℓ as a function of group — 0, 0, 2, …, 2, 1, …, 1 — which no envelope can read, giving E = 36.
Dropping group and keeping ℓ gives **E = 0 immediately**. Repairable by re-ordering; this is what
Janet's table does, and it is the block order f, d, p, s rather than the choice of period that does the work.

**Sub-case B, arity.** Every term is monotone but the constraint names more coordinates than an envelope has
arguments. An index of which physical laws must break to reach another universe has **all
72 of its pairwise relations monotone** and a defect nonetheless, from a constraint of arity 3
with a unique minimal support. Six coordinate operations fail to repair it, including exhaustive relabelling.

We then **double the alphabet**. Five of nine coordinates are shown to conflate distinct physical notions — each
against a named theorem's stated hypothesis — and splitting them, plus adding the derivative-order axis that is
Buniy's operative hypothesis, gives fifteen letters. **Every structural result survives**: arity 3, core one cell,
six repairs failing, the two-line envelope argument, the frontier formulas exact. The multiplicity moves from 30 to
816 and carries no information.

Finally the defect is located outside the index altogether. The chargers — the theorems that levy a price — draw
their hypotheses from **seven vocabularies**, so each is a map between indices rather than a constraint within one.
**And the vocabulary partition is then derived rather than chosen**: it is the
Brunetti–Fredenhagen–Verch functor read as a list of its parts, four in number, with the terms that refuse
to place being *relations* between them. On that partition the system graph is **complete** — every
vocabulary reachable from every other — and an earlier draft's conclusion that the wormhole exclusion sits
in an unreachable component is withdrawn as an artefact of a coarser partition.

**Six further indices are then built, and every one outside the law index closes** — geometry, solution
status, the local geometry of a null surface, and the covered cases of the null-energy literature. Λ is
audited against its own sources and found to have **seven of thirteen letters conflated, one with no
referent at all, and one quantity read but never indexed** — while closing in all four standard coupling
schemes. **Closure does not certify the letters**, and the clean null case transfers to the geometry index.

The self-consistent achronal ANEC is one such relation, which is why no coordinate of a law
index can carry it — and the gap it names turns out to be a **modular theory** gap, with a target one
cell from where it is proved.

> **What this paper does not claim.** Nothing here bears on whether other universes exist, or whether transit
> between them is achievable. Every result is about an *index* — what a coordinate system can and cannot carry.
> The precedent is the periodic table, whose defect of 36 is a fact about a drawing.

![The result](figures/f6_1.png)

*Figure 0.1. One object is decidable by local consistency; the two that cross between universes are not, and for
different reasons.*

---

## Contents

- [Part 0 · Procedure](#part-0--procedure)
- [Part I · The operator, and two failure modes](#part-i--the-operator-and-two-failure-modes)
- [Part II · Λ verified](#part-ii--λ-verified)
- [Part III · The periodic table: ordering failure, repaired](#part-iii--the-periodic-table-ordering-failure-repaired)
- [Part IV · Transit structures on Λ](#part-iv--transit-structures-on-λ)
- [Part V · The violation index at nine letters](#part-v--the-violation-index-at-nine-letters)
- [Part VI · The alphabet](#part-vi--the-alphabet)
- [Part VII · The violation index at fifteen letters](#part-vii--the-violation-index-at-fifteen-letters)
- [Part VIII · Chargers, jurisdiction, and the system of indices](#part-viii--chargers-jurisdiction-and-the-system-of-indices)
- [Part IX · The axis index, and what was never named](#part-ix--the-axis-index-and-what-was-never-named)
- [Part X · Six more indices, and what the null case is](#part-x--six-more-indices-and-what-the-null-case-is)
- [Part XI · Results](#part-xi--results)
- [Part XII · Register](#part-xii--register)
- [Part XIII · Open](#part-xiii--open)
- [Appendix A · Equations](#appendix-a--equations)
- [Appendix B · References](#appendix-b--references)
- [Appendix C · Verification](#appendix-c--verification)

---

## Part 0 · Procedure

### 0.1 Protocols

| protocol |  |
|---|---|
| commit before looking | a position is written down before any retrieval; the retrieval scores it |
| compute before writing | numerical claims are computed, then reported, never the reverse |
| refuse rather than coerce | an ambiguous instruction is queried, not defaulted |
| enumerate before searching | targets are listed before the first search and re-listed when the set grows |
| record what a failure excludes | a falsified prediction is logged with the class of claim it rules out |

### 0.2 The Admission Law

> An open index admits any content, and admits it only together with its verification grade. An entry's grade
> bounds the operations it may enter. **A derived entry carries the minimum grade of its inputs, and no derivation
> raises a grade.** Content contradicting the index is admitted and flagged as a collision; a collision is
> discharged by re-deriving the internal result, never by refusing the content.

Every substantive repair in this work arrived as a collision. The bibliography carries an access grade per source
for the same reason.

### 0.3 The merge rule

> A biconditional licenses a merge only if it holds at **every rung** of the graded axis. Merging on a fact true at
> one point and then grading the axis is the error.

Part VI shows that this rule, correctly applied, would have caught five of the nine coordinates before they were
built.

### 0.4 Operator reliability, measured

Predictions aimed at logical structure — which hypotheses a theorem takes, which way an entailment runs — scored
4/4 on three consecutive tests. Predictions aimed at how a field regards a claim scored 1/4. Predictions of
implications not yet in the index scored about 1 in 5. Under 0.2 the last class was therefore barred from entering
content.

---

## Part I · The operator, and two failure modes

### 1.1 Definitions

For finite X ⊆ ∏Aᵢ of integer tuples, write **Âᵢ(X) = {xᵢ : x ∈ X}** for the value sets and
**φ̂ᵢⱼ(v) = max{xᵢ : x ∈ X, xⱼ ≤ v}** for the monotone upper envelope of coordinate i against j. Then R(X)
collects every point of the observed box respecting all envelopes, and E(X) is its excess — equations (1)–(4).
No outside knowledge enters R(X): it is what a reader could reconstruct from the cells alone.

### 1.2 Proposition. X ⊆ R(X), hence E ≥ 0

> *Proof.* Let x ∈ X. Each xᵢ ∈ Âᵢ(X). For i ≠ j the set {yᵢ : y ∈ X, yⱼ ≤ xⱼ} contains xᵢ, since x satisfies
> xⱼ ≤ xⱼ. Hence φ̂ᵢⱼ(xⱼ) ≥ xᵢ, so x ∈ R(X). ∎

### 1.3 Proposition. R is a closure operator

Extensive by 1.2. Monotone and idempotent by computation: R(R(X)) = R(X) on Λ₈ and on both violation indices;
monotonicity held on thirty nested random pairs with no failure. The closed sets form a Moore family.

### 1.4 Identification

R is the closure of a binary constraint network under monotone binary projections, and **E(X) = 0 iff the network
is globally consistent**.

### 1.5 R against the full minimal network

X ⊆ BPC(X) ⊆ R(X) — equation (5) — so E > 0 is in principle ambiguous between genuine inconsistency and envelope
coarseness. Computed for every object here, **the ambiguity does not arise**: R = BPC exactly.

![Nested sets](figures/f1_1.png)

### 1.6 THE TWO FAILURE MODES

This is the paper's thesis and everything after it is instances.

> An index can carry a constraint only if it holds the constraint's terms **in an order the envelope can read**,
> and in **as many places as the constraint names**. Failure of either produces E.
>
> **Sub-case A — ordering.** The term is present and determined but non-monotone. Repairable by re-ordering.
>
> **Sub-case B — arity.** Every term is monotone; the constraint names more coordinates than an envelope has
> arguments. Not repairable by any operation on coordinates.

Four objects, and the diagnosis separates them cleanly:

| object | non-monotone relations | arity | E | verdict |
|---|---|---|---|---|
| Lambda_8 | 0 | 2 | 0 | null case |
| periodic table | 2 | 2 | 36 | sub-case A, ordering, REPAIRED by re-placement |
| violation index (9) | 0 | 3 | 30 | sub-case B, arity, six repairs failed |
| violation index (15) | 0 | 3 | 816 | sub-case B, survives the alphabet doubling |

**A vocabulary may also not be indexable at all.** V2 of Part VIII has four terms: two are non-operative, one belongs elsewhere, and one — field content — is **categorical**. Ordering it is arbitrary, and E depends on the choice: six of twenty-four orderings close it and eighteen do not. **E is defined only where the terms are graded and related.** Given a bag of unrelated categorical scope conditions, the operator returns a number that depends on how the bag was sorted.

**No third failure mode was found.** The axis index of Part IX looked like one — it fails at arity 2 with all 21 pairs
failing — and resolved to sub-case A, with 21 of 42 relations non-monotone. What distinguishes it from
the periodic table is only that its ordering failure is **unrepairable**, since nine axes have no natural
re-placement.

### 1.7 Six blindnesses

| blind to | instance | effect on E |
|---|---|---|
| decreasing bounds | a preferred frame forbids chronology violation | 0 → 6 |
| non-monotone relations | seniority parity on axis 10 | 0 → 678 |
| multi-coordinate constraints | the conjugation ceiling; the coupling triangle | 186 / 35,570 |
| unoccupied dimensions | a fifth axis nothing occupies | unchanged |
| the measure | two universes, same cells, different energies | unchanged |
| derived coordinates | an axis defined as a function of others | 30 → 120 |

**A derived coordinate cannot repair closure.** R reconstructs from cells alone, so a reader cannot see that a
coordinate was *defined* from others, while the box grows by that coordinate's value count and |X| stays fixed.
This excludes the entire class of derived-coordinate repairs, for any index.

![Blindness panels](figures/f1_2.png)

### 1.8 The closure rule

> **A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other.**

![Closure rule](figures/f1_3.png)

### 1.9 E requires density, asymmetrically

A late finding, and it qualifies every number in the paper.

| object | cells | box | density | E informative? |
|---|---|---|---|---|
| periodic table | 90 | 126 | 71.43% | yes |
| Lambda_8 | 976 | 6,912 | 14.12% | yes |
| violation index (15) | 18,072 | 622,080 | 2.91% | yes |
| violation index (9) | 2,370 | 19,440 | 12.19% | yes |
| Lambda_13 | 199,130 | 47,775,744 | 0.42% | measures sparsity |
| axis index | 9 | 5,184 | 0.17% | measures sparsity |

> **E = 0 is informative at any density. E > 0 at low density measures sparsity rather than structure.**

Λ₁₃ sits at 0.42% and E = 0 there is a *strong*
result — 47.8 million possible tuples, 199,130 cells, and the envelope admits exactly those. The axis index at
0.17% is the case where E > 0 says nothing.

### 1.10 Named theorems

| result | statement |
|---|---|
| Freuder 1982 | a tree-structured constraint network is globally consistent after arc consistency |
| Montanari 1974 | for monotone constraints, path consistency implies global consistency |
| van Beek & Dechter 1995 | generalisation of monotone to row-convex constraints |
| van Beek & Dechter 1997 | constraint tightness — the exact/admissible ratio |

These two cover Λ between them. Neither applies to either violation index, nor to the system of Part VIII.

---

## Part II · Λ verified

Λ is an atomic-structure lattice: 8-tuples (n, ℓ, k, q, e, f, g, 2S) built by nested bounds — equations (6)–(12) —
with the tower Λ₉–Λ₁₃ adding target spin, seniority, the core's J, K and the outer J, equations (13)–(17). Caps
(n, e, ℓ, k, f) = (3, 3, 1, 3, 1) are unique in the search range for 976 cells.

### 2.1 The tower closes at every level, for every statistics order

Generalising Pauli exclusion to parastatistics of order m gives capacity m(4ℓ+2), equation (25). At m = 1 the
construction reproduces the canonical tower exactly, which verifies the generalisation at the fermionic point.

| m | Λ₈ | Λ₉ | Λ₁₀ | Λ₁₁ | Λ₁₂ | Λ₁₃ |
|---|---|---|---|---|---|---|
| 1 | 976 | 1,654 | 2,535 | 13,585 | 70,905 | 199,130 |
| 2 | 1,600 | 2,950 | 4,875 | 36,875 | 233,750 | 664,375 |
| 3 | 1,600 | 2,950 | 4,875 | 43,875 | 314,250 | 898,875 |

**E = 0 at every cell of that table.** Boxes swept to 172,523,520 at m = 3, Λ₁₃, by a
backtracking counter with early pruning — the feasible region is a staircase, so most branches die at depth three
or four.

Previously this was established to Λ₁₁ only. **The parastatistics neighbours are globally consistent to the top of
the tower**, and the closure never depended on the fermionic value: capacity m(4ℓ+2) is monotone in ℓ for every m,
so §1.8's form is preserved and Montanari's certificate applies unchanged.

![The tower](figures/f2_1.png)

### 2.1b And it closes in every coupling scheme

The tower as built uses LS coupling within the core and jK pair coupling to the outer electron. That is
one of four standard schemes — LS, LK, jK and jj — and **the scheme is not a coordinate.**

Rebuilt in all four with a uniform one-parameter looseness convention:

| scheme | Λ₁₃ cells | E at every level |
|---|---|---|
| jK | 199,130 | 0 |
| LS | 431,050 | 0 |
| jj | 206,520 | 0 |
| LK | 341,150 | 0 |

**Closure is not scheme-contingent.** Cell counts differ by more than a factor of two and E is zero
throughout, because every scheme is a chain of vector-coupling bounds whose *loose* form binds one
coordinate by a monotone function of one other — §1.8's condition.

> **What is scheme-contingent is what the letters mean.** 2K is J_c + ℓ_outer in jK, L_total + S_core
> in LK, and jj has no K at all. The tower carries an unstated jurisdiction.

*A first run reported the alternatives as failing. It had applied two-parent bounds to them and
one-parent bounds to jK, and the difference was my convention, not the schemes.*

### 2.2 Why it closes

Λ₉'s constraint graph has nine nodes and eight edges and is a tree, so Freuder applies. Λ₉′ — the same lattice with
the admissible Pauli cut 2S′ ≤ 2f+1, removing 93 cells and leaving 1,561 — gains the cycle f–g–2S′ and
loses the guarantee. Λ₁₀ has ten nodes and ten edges. **Λ₉ is the last tree level.**

![Constraint graphs](figures/f2_2.png)

### 2.3 Where the exactness goes

All six density values reproduce once three non-obvious exact sets are used: the spin set of f^g by microstate
enumeration at axis 9; terms genuinely *new* at occupancy v, conjoined with the parity congruence and the
conjugation ceiling, at axis 10; and the J values of terms of ℓᵏ carrying the cell's own multiplicity 2S at axis 11.
Without the third, axis 11 computes to 43.1% instead of 17.0%.

![Densities](figures/f2_3.png)

### 2.4 Closure and exactness are incompatible

Imposing the exact coupling triangle on axis 12 cuts the lattice from 70,905 to
22,275 cells and takes E from zero to 35,570 — the exact bound is
ternary, outside the closure-preserving class.

> **Λ is loose by design.** Every coupling coordinate's exact bound needs two parents or a congruence, and a tree
> carries one. **The tree or the tightness.** Part VIII finds the same trade one level up.

![Closure vs exactness](figures/f2_4.png)

### 2.5 The multilattice: which modifications close

Four monotone variants of the ℓ-bound close; two non-monotone variants do not, at E = 61,845 and 19,245. The
decisive pair is ℓ ≤ ⌊n/2⌋ and ℓ ≤ |n−3|, which have **identical cardinality** at 32,535 cells — one closed, one
open. Cardinality is not the discriminant; monotonicity is.

![l-bounds](figures/f5_1.png)

### 2.6 Lorentz violation does not change the lattice

The Standard-Model Extension computes energy shifts in the existing basis. The Coulomb accidental degeneracy lifts;
the quantum numbers do not move, because ℓ ≤ n−1 follows from node counting.

> **Corollary.** The lattice does not individuate universes by Lorentz structure. Our Lorentz-violating neighbour
> has the same 976 cells and a different energy ordering — invisible to R.

Part VII sharpens this: the lattice distinguishes exactly one thing, whether spin-statistics holds.

### 2.7 Transit admissibility is directional

| direction | cells lost |
|---|---|
| ours → relaxed (45,441 into 182,709) | **0** |
| relaxed → ours | 137,268 |

**Transit outward is unobstructed; inward is not.** A cell with occupancy beyond our Pauli bound fails our
one-dimensional index outright, before any question of joint structure arises.

![Containment](figures/f5_2.png)

### 2.8 What the index cannot carry: the measure

Three things locate a transition and the index certifies only the first. **The lattice says what exists.**
**The order says what is near** — of 475,800 pairs of Λ₈ cells only 24.2% are ordered
by componentwise domination. **The measure says what it costs** — and it is external.

Our own measure is not faithful to our own order. Of the 115,162 ordered pairs,
**52.3%** share the principal quantum number and are indistinguishable to a Coulomb energy function.

![Order and measure](figures/f5_3.png)

---

## Part III · The periodic table: ordering failure, repaired

The control, and the only object here whose answer is independently known.

### 3.1 The mechanism is ordering, not placement

The eighteen-column table has E = 36. It is standard to say Janet's left-step table removes this by
re-indexing period as n + ℓ. **That is not what does the work**, and neither is contiguity as such.

**ℓ is fully determined by group** — s at 1–2, d at 3–12, p at 13–18. The term is present, recoverable,
unambiguous. And the defect is 36 anyway, because

```
ℓ by group 1..18 :  0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1
```

rises then falls. **Non-monotone in both directions**, so no envelope can use it. In Janet's block order f, d, p, s,
ℓ decreases monotonically along every row.

| presentation | cells | E |
|---|---|---|
| (period, group) — ℓ present, non-monotone in group | 90 | 36 |
| (period, position) contiguous | 90 | 0 |
| Janet (n+ℓ, position) — ℓ monotone | 120 | 0 |
| **(period, ℓ)** — group dropped | 90 | **0** |
| (period, group, ℓ) — ℓ named explicitly | 90 | 100 |

**Drop group, keep ℓ, and the table closes immediately.** And naming ℓ explicitly makes it *worse*, E =
100. **Naming the term does not help. Ordering it does.**

### 3.2 What the 36 are

They decompose: **25** of them — 1d (10), 1p (5), 2d (10) — could never hold an element, being
forbidden by ℓ ≤ n−1. They are the footprint of a law the coordinate system has no axis for. The
remaining **11** are 3d (10), deferred past 4s by the Madelung order, and period 1 group 2, where
ℓ = 0 satisfies ℓ ≤ n−1 and no element is drawn. *An earlier draft read 26 + 10; **1p contributes
five and not six, because helium occupies group 18 itself**, and the slot helium vacates is deferred
rather than forbidden.* And **E is placement-sensitive**: 36 with helium at group 18, **20** with
helium at group 2, since φ̂(group | period ≤ 1) drops from 18 to 2 and the first row of gaps
disappears with it.

**Two constraints casting a thirty-six-cell shadow, not thirty-six facts.**

![Periodic table](figures/f2_5.png)

### 3.3 Why the control matters

The periodic table is not an analogy for the violation index. **It is the other failure mode**, and having both is
what makes the distinction visible. Ordering failures are repairable because re-ordering acts on one relation at a
time — exactly enough for sub-case A and exactly not enough for sub-case B.

---

## Part IV · Transit structures on Λ

### 4.1 Λ₉ is the transit level

A cell's target is a legal source exactly when 2S′ ≤ g — which *is* axis 9, equation (19). Of 1,654
cells, 1,169 are composable. Λ₉ is simultaneously the first level at which a transition has a defined
endpoint and the last level that is a tree.

![The window](figures/f3_1.png)

### 4.2 The composition graph is a line digraph

Composable cells are the arcs of a quiver Q on 33 atomic states; the composition graph is L(Q) and its
edge count is **27,027 = Σ(in × out)** exactly, equation (20). The 33 degenerate cells are
Q's loops, and because Q has a loop at every vertex, **return is available in one step from every state.**

![Quiver](figures/f3_2.png)

### 4.3 Girth exactly 4

Unit-step adjacency coincides with the covering relation exactly — 6,658 edges either way, so the lattice
is gap-free. Degrees run 4 to 12, mean 8.05, connected.

> **Proposition.** The girth is exactly 4. *Proof.* Three mutually adjacent cells are impossible: if a–b differ in
> coordinate i and b–c in j ≠ i then a–c differ in two; if i = j then a–c differ by 0 or 2. No triangle exists. A
> square c, c+eᵢ, c+eᵢ+eⱼ, c+eⱼ is exhibited. ∎

![Girth](figures/f3_3.png)

### 4.4 Molecular transit, and sub-case B at higher arity

A molecule moves as one fibre, so all its atoms take the same displacement and a circuit is a square. Feasibility is
an intersection question — equations (21)–(22).

| atoms | 2 | 3 | 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|---|
| feasibility | 93.7% | 59.3% | 27% | 4.15% | 0.594% | 0.0829% | 0.0122% |

Decay is geometric at **2.51 per atom** — a log-linear fit over all seven points, against the 2.57 the figure carries. *An earlier draft read 1.9, which neither the fit nor the figure supports.* Homonuclear molecules are unconstrained.

> **The Helly number is at least 5 and at most 144.** A critical family of
> five is exhibited: every four intersect and the five do not. The upper bound is the ground set — all C(9,2) × 4 =
> 144 square directions occur.

This is **sub-case B at arity 5**, showing the mode scales beyond the ternary case.

![Molecular feasibility](figures/f3_4.png)
![Helly](figures/f3_5.png)

---

## Part V · The violation index at nine letters

Presented as originally built, because Part VI shows five of its nine letters are conflated, and the correction is
only legible against what it corrects.

### 5.1 Coordinates

> **Notation.** E is the closure defect throughout. The null-energy coordinate is written NEC to avoid the
> collision.

| axis | rungs |
|---|---|
| **X** causal ladder | Lorentz invariant / preferred threading / preferred foliation / chronology violated |
| **S_corr** correlation | local ≤2 / quantum ≤2√2 / post-quantum ≤4 |
| **IC** information causality | holds / violated at m>0 / violated at m=0 |
| **U** unitarity | unitary / local energy-momentum-conserving non-unitarity / requiring locality to break |
| **NEC** null energy | intact / pointwise / ANEC arbitrarily small / macroscopic QI-bounded / QI-violating |
| **L** linearity | linear / nonlinear |
| **SD** microcausality | holds / fails |
| **DN_c** cloning | quantum-optimal / beyond / perfect deterministic |
| **DN_d** discrimination | quantum-optimal / beyond / perfect |

Our position is **(0, 1, 0, 0, 1, 0, 0, 0, 0)**, with two components fixed by measurement: S_corr = 1 because
quantum mechanics violates Bell locality while respecting microcausality, and NEC = 1 because Casimir energy is
measured and violates the null energy condition pointwise.

![Nine axes](figures/f4_1.png)

### 5.2 Routes, and the cost of a formalism

| CTC model | destination floor | steps |
|---|---|---|
| Deutsch (D-CTC) | (3, 2, 2, 1, 2, 1, 0, 2, 2) | 12 |
| post-selected (P-CTC) | (3, 2, 1, 1, 2, 0, 0, 0, 1) | 8 |
| model-independent | (3, 1, 0, 1, 2, 0, 0, 0, 0) | 5 |

Model-independently, chronology violation requires the causal ladder, non-unitarity at the Lindblad rung, and
arbitrarily small ANEC violation — and **not** signalling, cloning, nonlinearity or loss of microcausality, each of
which appears under Deutsch's prescription and not otherwise.

![Three routes](figures/f4_2.png)

### 5.3 The defect and its collapse

2,370 cells; **E = 30**, all of it genuine global-consistency failure. The excess is
exactly **1 × 30**, and the core is one cell: **(X = 0, U = 0, NEC = 3)**.

The envelope calculation says why in two lines:

```
φ(NEC | X = 0)  must permit the value, because X = 0 cells with U ≥ 1 reach it
φ(NEC | U = 0)  must permit the value, because U = 0 cells with X ≥ 1 reach it
```

**Both conditioning coordinates individually admit what the pair forbids.**

![The collapse](figures/f4_3.png)

### 5.4 Unique minimal support

Of 414 coordinate subsets excluding {X, U, NEC}, **0**
fail. The triple is the only minimal failing subset. **Arity exactly 3, one generator.**

Three independent literatures give the same branch from unrelated starting points, and **none gives a single
payer**: Buniy–Hsu–Murray from effective field theory; Hartman–Kundu–Tajdini from microcausality, whose theorem
assumes unitary *and* Lorentz-invariant *and* interacting, so violating its conclusion breaks one of three; and Wall
from the generalised second law.

![Minimal support](figures/f4_4.png)

### 5.5 The repair space is closed

| operation | outcome | E | why |
|---|---|---|---|
| merge by identification | not licensed | — | no pair among {X, U, NEC} is biconditional at every rung |
| merge by linearisation | worse | 414 | collapsing two axes forces every constraint through one envelope |
| relabel axis values | never zero | min 1 | exhaustive: 0 of 17,280 |
| slide within rows | never better | 10 | the hole is a row that should not exist |
| add a derived coordinate | worse | 120 | the box inflates and |X| does not |
| split an axis | neutral or worse | 30 | pins the antecedent as well as the consequent |

> **Adding fails because the box inflates; merging fails because the envelopes coarsen.** Both directions excluded,
> for opposite reasons, and the two-line argument covers all six.

![Six repairs](figures/f4_5.png)

### 5.6 Objects are thresholds

| object | threshold | cells | here? | reachable |
|---|---|---|---|---|
| classical black hole | `none` | 2,370 | **yes** | 1,410 |
| Hawking-evaporating black hole | `NEC >= 1` | 2,196 | **yes** | 1,410 |
| Planck-scale wormhole | `NEC >= 2` | 1,764 | no | 1,134 |
| macroscopic wormhole | `NEC >= 3` | 1,146 | no | 738 |
| universal horizon | `X >= 2` | 1,374 | no | 840 |
| time machine | `X = 3` | 558 | no | 360 |

Of the 1,146 cells permitting a macroscopic wormhole, 1,116
pay with a preferred frame, 714 with non-unitarity,
756 with signalling — and **0 pay with none.**

![Thresholds](figures/f4_6.png)

### 5.7 The defect does not scale

| coordinates | 4 | 5 | 7 | 9 |
|---|---|---|---|---|
| defect | 3 | 5 | 10 | 30 |
| core | 1 | 1 | 1 | 1 |
| multiplicity | 3 | 5 | 10 | 30 |

The core is one cell at every resolution. **The multiplicity moves, and it is NOT arithmetic.**
With X, U and NEC pinned by the core, independent free letters would give running products of their
rung counts — **3, 9, 36, 324** — and the measured sequence is 3, 5, 10, 30. **5 is not a product of
any two rung counts among {3, 3, 2, 2, 3, 3}**, so the edge list constrains the free letters as well
as the support, and the sequence is a property of the constraints rather than of the coordinate
count. *An earlier draft called it arithmetic.*

> **And the sequence is a test the construction must pass.** Anything supplied as this index's edge
> list must reproduce five printed figures: 2,370 cells in a box of 19,440; E = 30 collapsing exactly
> as 1 × 30; the core at (X = 0, U = 0, NEC = 3); none of the 414 subsets excluding {X, U, NEC}
> failing; and multiplicities 3, 5, 10, 30 at four, five, seven and nine coordinates. **The edge list
> itself is not printed anywhere in this paper**, and until it is, those five conditions are what
> stands in its place.

![Projection](figures/f4_7.png)

---

## Part VI · The alphabet

The central methodological result, and it was invisible from inside the index.

### 6.1 Five of nine coordinates conflate distinct notions

| letter | status | merges | shown by |
|---|---|---|---|
| X | CONFLATED | spontaneous vs explicit Lorentz breaking; stated vs operative hypothesis | the ghost condensate is a Lorentz-invariant THEORY with a Lorentz-violating VACUUM |
| Sc | clean | graded by a measured number | — |
| IC | clean | m>0 vs m=0 explicit in the grading | — |
| U | CONFLATED | open-system (CPTP, metric intact) vs ghosts (indefinite metric) | the spin-statistics postulate concerns the METRIC, which Lindblad preserves |
| NEC | CONFLATED | ANEC vs ACHRONAL ANEC | MMP violates ANEC and satisfies achronal ANEC; different theorems apply |
| L | CONFLATED | dynamical (Weinberg) vs kinematical (state space) | Lambda uses state-space structure only, never the evolution law |
| SD | CONFLATED | commutativity of OBSERVABLES vs of FIELDS | wrong field choice gives identically vanishing fields, so no theory exists (Burgoyne) |
| DNc | partial | deterministic vs probabilistic at rungs 0-1 | Rastegin: the cloning-discrimination equivalence is deterministic only |
| DNd | partial | as DNc | — |

**5 fully conflated, 2 partially,
2 clean.**

### 6.2 Every conflation merges an inert rung with a potent one

In each case the rung as graded has **no lattice action**, and its partner either acts or abolishes the lattice
outright. That is not coincidence: **the index was graded from papers about what breaks, and the papers that matter
for atomic structure are about what holds.** Two different literatures.

### 6.3 None was findable from inside

**All five surfaced from a specific question about a named theorem** — which spin-statistics hypothesis does U
encode? does nonlinearity destroy vector coupling? observables or fields? which exclusion theorem applies to a long
wormhole? is the ghost condensate inside Buniy's jurisdiction? Inspecting the coordinate list finds none of them.

> **An index's conflations are invisible from inside it. They are visible only from the theorems it is meant to
> carry.**

This is why twenty-one structural audits passed on a document containing all five. Those audits compare the index
against itself — coherence, scoping, arithmetic, attribution — and **no self-audit can catch a word that means
something else elsewhere.**

### 6.4 Audit 22 — term match, and the vocabulary debt

**For every coordinate whose term appears in a cited theorem: state what the theorem means by it, state what the
rung means, record match / conflation / unchecked.** Its output is a debt, not a pass.

```
coordinates                9
theorems naming one        24
term-sharing pairs         48
checked                    16   (33%)
   conflations             7
   partial                 2
   matches                 7
UNCHECKED                  32
```

Pairs by coordinate: X 8, Sc 4, IC 6, U 8, NEC 7, L 4, SD 5, DNc 4, DNd 2 — **these are the 48 term-sharing pairs, not the 32 unchecked**, and the row was mislabelled: it sums to 48. Of them **IC has never been
checked once**, and IC is load-bearing: it is the unique principle forbidding post-quantum correlations.

The 56% conflation rate among those checked should **not** be extrapolated. The sixteen were selected because
something forced them, so they are enriched for trouble. The rate among the remaining 32 is lower,
unknown, and not zero.

### 6.5 The corrected alphabet

| letter | meaning | rungs | provenance |
|---|---|---|---|
| **X_exp** | explicit Lorentz violation in the Lagrangian | 4 | split from X |
| **X_spon** | spontaneous Lorentz breaking (a VEV picks a frame) | 2 | split from X |
| **Sc** | CHSH correlation strength | 3 | unchanged, clean |
| **IC** | information causality | 3 | unchanged, clean |
| **U_open** | open-system non-unitarity (CPTP, Lindblad) | 3 | split from U |
| **U_ghost** | indefinite metric, ghosts | 2 | split from U |
| **NEC_pt** | null energy violation, graded by scale | 5 | split from NEC |
| **NEC_ach** | achronal ANEC violated | 2 | split from NEC |
| **L_dyn** | nonlinear evolution, state space linear (Weinberg) | 2 | split from L |
| **L_kin** | nonlinear state space, superposition fails | 2 | split from L |
| **SD_obs** | spacelike commutativity of observables | 2 | split from SD |
| **SD_field** | spacelike commutativity of fields | 2 | split from SD |
| **DNc** | cloning fidelity | 3 | unchanged, partial conflation noted |
| **DNd** | state discrimination | 3 | unchanged, partial conflation noted |
| **EOM** | derivative order of the equations of motion | 2 | NEW |

**What becomes expressible.** The ghost condensate — X_exp = 0, X_spon = 1, EOM = higher — a Lorentz-invariant
*theory* with a Lorentz-violating *vacuum*, which in the nine-letter alphabet could not be written. The MMP
wormhole — NEC_pt = 2, NEC_ach = 0 — violating the ANEC while satisfying the achronal ANEC. Buniy's jurisdiction in
full. And **SD_field = 1 marks a cell that is not a universe at all**, by Burgoyne: the fields vanish identically.

That last removes **18,888 of 37,776** closed cells as describing
no theory.

---

## Part VII · The violation index at fifteen letters

### 7.1 Every structural result survives

```
closed cells                    37,776
minus SD_field = 1 (no theory)  18,888 → after charge 18,072
ambient box                     622,080
density                         2.91%      (informative range)
E                               816
core                            [[0, 0, 3, 0]]    ONE cell
collapse exact                  True   (816 = 1 × 816)
arity                           3
```

**The core is (X_exp = 0, U_ghost = 0, NEC_pt = 3, EOM = 2nd-order)** — macroscopic exotic matter, no explicit
Lorentz violation, no ghosts, second-order equations of motion. The same profile as at nine letters, in four precise
conditions rather than three approximate ones.

**Two minimal supports, not one**: {X_exp, X_spon, NEC_pt} and {X_exp, U_ghost, NEC_pt}. The split
created a second path, since U_ghost = 1 → X_spon = 1 makes X_spon a proxy for ghosts. Both share {X_exp, NEC_pt}.

**EOM does not appear in either**, though it is Buniy's jurisdiction — Ostrogradsky gives EOM = higher → U_ghost, so
the closure carries the jurisdiction into the currency letter. **A jurisdiction condition forced by an existing
letter costs nothing.**

### 7.2 The repair space is still closed

| operation | E at fifteen | note |
|---|---|---|
| merge by identification | n/a | no pair among the support is biconditional at every rung |
| merge by linearisation | 7,734 | coarsens every envelope on either axis; reproduces exactly under the nine-letter convention |
| relabel — exhaustive | min 1 | 0 of 5,760 close |
| slide within rows | 5 | the hole is a row that should not exist; **corrected** from 8,856 |
| add a derived coordinate | 2,196 | the box inflates, |X| does not |
| split an axis further | 816 | no change |

> **One of these was wrong.** Recomputed under the documented nine-letter conventions, the linearisation
> figure reproduces exactly at 7,734. The slide figure does not: an earlier draft carried **8,856**, and
> the operation acts on the minimal triple — three coordinates, box at most 4 × 2 × 5 = 40 — so its
> defect is **bounded by 40**. A five-figure value is impossible for it. **The correct value is
> 5**, and the verdict is unchanged: every operation leaves E positive.

And the envelope argument transfers verbatim:

```
φ(NEC_pt | X_exp = 0)   = 3    X_exp = 0 cells with ghosts reach it
φ(NEC_pt | U_ghost = 0) = 4    ghost-free cells with X_exp ≥ 1 reach it
```

### 7.3 The frontier formulas, exact

**d(c) = X_exp + U_ghost + |NEC_pt − 3| + EOM + d_P(eleven free letters)**
**s(c) = 1{X_exp>0} + 1{U_ghost>0} + 1{NEC_pt≠3} + 1{EOM>0} + s_P**

Verified on 1,500 sampled cells: **0 distance mismatches,
0 support mismatches.**

**Our own values are unchanged: d = 2, s = 1.** Two rungs of one letter from the core,
and the letter is still NEC_pt.

But the pinned set changed: **SD dropped out and EOM came in.** The SD that mattered was never the observable one.
And the corner is less exclusive — 20.8% of cells see the frontier along a single letter
against 8.9% at nine letters, mean support 2.31 against 3.35. **Support and distance are
alphabet-dependent. The core is not.**

### 7.4 The lattice map, now exact

The spin-statistics hypotheses have three letters and no proxies: **X_exp = 0, SD_obs = 0, U_ghost = 0.**

| hypothesis | letter | indexable? |
|---|---|---|
| Lorentz invariance | `X_exp = 0` | indexable |
| spacelike commutativity of observables | `SD_obs = 0` | indexable |
| positive-definite metric | `U_ghost = 0` | indexable |
| vacuum is lowest energy | `-` | not a letter |
| vacuum not annihilated | `-` | not a letter |

**900 of 18,072 cells — 5.0% — have the Pauli lattice guaranteed, and we are among
them.** For the rest, parastatistics becomes available and Λ₈ can be 1,600 rather than 976: a different periodic
table, and different everything built from atoms.

> **The lattice distinguishes exactly one thing: whether spin-statistics holds.** Two universes share a lattice iff
> they agree on that, and may differ arbitrarily in energy conditions, signalling, cloning and discrimination
> without any atom noticing.

**U_open and L_dyn are provably inert**; their split partners U_ghost and L_kin are what act. That was the entire
content of two conflations, now visible in the alphabet rather than buried in a rung.

---

## Part VIII · Chargers, jurisdiction, and the system of indices

### 8.1 A charge relation has three parts, not two

**Trigger** — what incurs the charge. **Currency** — what may pay. **Jurisdiction** — where the charger has standing
to collect.

| charger | trigger | currency | jurisdiction |
|---|---|---|---|
| Buniy–Hsu–Murray | NEC violation | instability → ghosts | causal, Lorentz-invariant, second-order EOM |
| Hartman–Kundu–Tajdini | ANEC violation | ¬unitary, ¬Lorentz, ¬microcausal | **exactly flat spacetime** |
| Wall (GSL) | achronal ANEC | via the generalised second law | curved, minimally coupled, GSL axioms |
| Graham–Olum | achronal ANEC | causality violation | **asymptotically flat, simply connected** |
| Ostrogradsky | higher-derivative EOM | ghosts | **non-degenerate** (Galileons escape) |

### 8.2 A jurisdicted forcing and an unjurisdicted disjunction are the same object

| constraint | arity | cells | E | core |
|---|---|---|---|---|
| NEC ≥ 3 → U ≥ 1 | 2 | 1,938 | **0** | — |
| NEC ≥ 3 ∧ X = 0 → U ≥ 1 | 3 | 2,370 | **30** | 1 |
| NEC ≥ 3 ∧ U = 0 → X ≥ 1 | 3 | 2,370 | **30** | 1 |
| NEC ≥ 3 → (IC ∨ U ∨ X) | 4 | 2,370 | **30** | 1 |

> **"Something must pay and we can't say what" and "unitarity must pay, but only in Lorentz-invariant theories" are
> the same constraint.** The unnamed currency and the scoped jurisdiction are one phenomenon.

That resolves what looked like missing information. **Buniy names the price precisely — ghosts. What it also names
is a jurisdiction, and the jurisdiction costs the extra coordinate.** A theorem holding only under a scope condition
is inherently ternary, and no further physics removes the scope.

**And the size behaves counterintuitively.** Arity ≥ 3 is what makes a defect *possible*; jurisdiction *narrowness*
is what makes it small. The defect is **largest at exactly one scope condition**. The table above prints the measured values — 0 at arity 2, then 30, 30 and 30 — and the descending sequence an earlier draft gave for further conditions is **withdrawn: no table stands behind it**. The theorems hardest to index are the **nearly universal** ones with a single hypothesis, and Buniy is
exactly that.

### 8.3 Buniy's jurisdiction is necessary, and its operative hypothesis is not the one I indexed

The counterexample exists: **Creminelli, Luty, Nicolis and Senatore, *Stable Violation of the Null Energy Condition*
(2006)**, built on the ghost condensate. And it escapes **not** through Lorentz violation — its Lagrangian
ℒ = √−g M⁴P(X) is manifestly Lorentz-invariant, the *vacuum* breaks the symmetry — but through **higher-derivative
terms**, which supply the leading spatial kinetic term for the perturbations.

Corroborated from the other side: standard two-derivative theories generically develop ghosts or gradient
instabilities on NEC-violating backgrounds, with Galileons escaping because their higher-derivative terms are
combined so the equations of motion stay second order in each field.

**So the load-bearing hypothesis is derivative order, and the index used Lorentz invariance as a proxy.** The proxy
gave the right answer because the core cell satisfies both — a coincidence that concealed the error. It also means
**Route 1 stays open**: Buniy may extend to Lorentz-violating second-order theories, and nothing known bears on that.

### 8.4 The vocabularies

The nineteen-odd hypotheses across the chargers do not belong to one vocabulary. Sorting them:

**The partition is not seven and it is not mine.** A locally covariant QFT is a functor
**A : Loc → Alg** (Brunetti–Fredenhagen–Verch 2003), and that object has exactly four parts: the source
objects, the target objects, the functor itself, and functionals on the target.

| vocabulary | what it is | terms |
|---|---|---|
| T THEORY | the functor itself, what the Lagrangian determines | X_exp, CPT, causality, field content, EOM derivative order, … |
| M SPACETIME | the source objects: globally hyperbolic spacetimes | flat / asymptotically flat / curved, simply connected, globally hyperbolic, generic condition, spatially compact, … |
| A ALGEBRA | the target objects: unital *-algebras | U_open, U_ghost, SD_obs, SD_field, L_dyn, … |
| S STATE | functionals on the algebra | X_spon, Sc, NEC_pt, Hadamard, vacuum is lowest energy, … |

**Three of my seven vocabularies dissolve.** ξ and degeneracy are parameters of the *theory* — they sit
in the Lagrangian, so they determine the functor. V2 was the functor itself, described by a list of
properties rather than graded, which is exactly why it was not an index.

**And the terms that refuse to place are relations**, not properties:

- self-consistent semiclassical: a relation between M and S
- within the semiclassical regime: a relation on the pair
- backreaction included: the same relation as a modelling choice
- state-independent QEI availability: a relation between T and S

> That is why V6 looked like a vocabulary and why it "carried the conjecture." **The self-consistent
> achronal ANEC is not a property of a universe. It is a relation between a spacetime and a state** —
> G(g) = 8π⟨T⟩_ψ — and a relation cannot be a coordinate of either side.

Two hesitations resolve by derivation. **ξ belongs to T**, since it changes the action. **NEC_pt belongs
to S**, since ⟨T_μν⟩k^μk^ν is a functional on the algebra evaluated at a state.

**No vocabulary can fully state any charger. Zero of 6, minimum span two.**

Doubling the alphabet raised indexable hypotheses from 4 of
25 to 9 of 26 —
16% to 35% — and **moved nothing across the threshold.**

> **Enlarging the alphabet imported a charger, and the charger imported a vocabulary the alphabet doesn't have.**
> V7 arrived because EOM did. **Letters recruit chargers faster than they discharge them.**

### 8.5 The system graph

> **This section and §8.7 are HISTORY, not current analysis.** Both are built on the
> seven-vocabulary partition that §8.4 derives away and §12.3 withdraws. They are retained because
> §8.6's correction is only legible against what it corrects, and because the trade they name —
> connected or acyclic — survives the partition change. **Every V1…V7 label below belongs to the
> withdrawn partition.** The current partition is T, M, A, S, and on it the graph is complete.

Chargers are maps between indices. The system:

```
nodes       7
edges       8
components  1
cycles      2    NOT a tree
```

Degrees: V1 laws 5, V2 theory 2, V3 geometry 3, V4 algebra 2, V5 coupling 2, V6 solution 1, V7 degeneracy 1. **V1 is the hub and a cut vertex; V3 is the
other.** The two cycles come from the two three-index chargers, Hartman spanning laws–theory–geometry and Wall
spanning laws–algebra–coupling.

**Freuder does not apply**, for exactly the reason it fails at Λ₉′: an added edge makes a cycle. **Montanari does
not rescue it**, because cross-index constraints are conjunctions of conditions in different vocabularies, not
monotone bounds.

### 8.6 The system is connected — the severance was an artefact

**A previous draft concluded that the exclusion of macroscopic wormholes lives in a component the law
index cannot reach, and that this was why six repair operations failed.** Rebuilt on the four derived
vocabularies, that is wrong.

```
nodes       4   T, M, A, S
edges       6
components  1
cycles      3
complete    True
```

**Every vocabulary connects to every other**, with all four at degree three.

| charger | trigger | jurisdiction | currency | spans | status |
|---|---|---|---|---|---|
| Buniy-Hsu-Murray | S | T | A | A,S,T | fires |
| Hartman-Kundu-Tajdini | S | T,M | A,T | A,M,S,T | fires in flat space only |
| Wall (GSL) | M,S | T,A | A,T | A,M,S,T | fires |
| Graham-Olum | M,S | M | T | M,S,T | CONJECTURE, not a theorem |
| spin-statistics | A | T,A,S | A | A,S,T | fires |
| Ostrogradsky | T | T | A | A,T | fires |

> **the severance. V6 was never a node - self-consistency is a RELATION between M and S, and treating it as a vocabulary created a leaf only Graham-Olum touched. M stays reachable without Hartman because Wall spans T, A and M and fires.**

**So what is the obstruction?** Not connectivity.

> **Graham-Olum is reachable and its trigger is not met: its trigger is ACHRONAL ANEC violation, and the core cell has NEC_ach = 0. A long wormhole violates the ANEC and satisfies the achronal ANEC.**

**The charger is reachable and does not fire on the cell in question** — which is precisely what
Maldacena, Milekhin and Popov demonstrated, arrived at here from the graph rather than from the
construction.

**And the six repairs failed on arity**, which was always the explanation. Part VII and §8.2 are
untouched by this correction; the graph story was decoration on a partition already withdrawn in §8.4.

### 8.6b Graham–Olum is a conjecture

|  |  |
|---|---|
| status | CONJECTURE with a sufficiency proof attached |
| what is proved | that the condition, IF it holds, rules out wormholes and closed timelike curves |
| what is not | the condition itself. "We indicate why such a condition might be expected to hold." |
| age | 19 years, no proof, no counterexample |
| function | a filter, not a derivation: used to disqualify counterexamples |
| why violation-free | by construction. the three known violation classes - chronal geodesics, non-self-consistent solutions, Planck scale - are excluded by its own clauses. |

**The charger index of §10.1 lists it as firing. It should be conditional** — a conjecture with a
sufficiency proof is a third category the index does not have.

**And this explains §10.1's V6 result from the other end.** Four of five known violations fall outside
V6's admissible region **because the condition was built to have that property**: its clauses exclude
chronal geodesics, non-self-consistent solutions and Planck-scale effects by construction.

**A curved-space proof does exist** — the achronal ANEC for general QFTs in the near-horizon geometry of
spherical extremal black holes. **Another Killing horizon**, and the sixth independent instance of the
same restriction.

### 8.7 Connectivity against acyclicity

| configuration | edges | components | cycles | verdict |
|---|---|---|---|---|
| Hartman dead, Wall live (actual) | 6 | 2 | 1 | **disconnected** |
| Hartman live (3 indices), Wall live | 8 | 1 | 2 | connected, 2 cycles |
| Hartman reduced to V1–V3, Wall live | 7 | 1 | 1 | connected, 1 cycle |
| Hartman live, Wall reduced | 6 | 2 | 1 | disconnected |
| both reduced to two-index | 5 | 2 | 0 | disconnected — V5 isolated |

**No configuration is a connected tree.** The best available is Hartman reduced to V1–V3. And reducing Wall
backfires: its V1–V5 edge is coupling's *only* connection.

**Hartman must drop V2, not V3** — dropping *flat* leaves V1–V2 and never reaches geometry; dropping *interacting*
and *d > 2* leaves V1–V3 and connects without triangulating. So the requirement is precise: **Hartman must hold for
interacting theories in any dimension on curved backgrounds.**

**This is the same trade as §2.4, one level up.** Λ₉: the tree or the tightness. The system: connected or acyclic.
Both resolve the same way — *a statement that needs fewer places.*

### 8.8 That extension does not exist

Checked twice, including through an adjacent literature.

The general ANEC-from-causality argument is **flat-space**; earlier derivations were restricted to free or
superrenormalisable theories, or to two dimensions. Curved-space results exist only with a V2 condition retained:
CFTs in conformally flat spacetimes, maximally symmetric backgrounds, free minimally coupled fields at small
curvature, or via the GSL with minimal coupling.

**The QNEC lineage goes further and still not far enough.** The modular crossed-product construction defines entropy
differences in general curved spacetime and proves the Bekenstein bound there — but its **QNEC proof is on Rindler
horizon cuts in Minkowski**, and the paper's own future-work list names the generalised second law, which is Wall's
route to the achronal ANEC, as *not yet done.*

**So the core cell stands** — not because the system is disconnected, which §8.6 withdraws, but because
the arity is three and no operation on coordinates reduces it.

Indexed by geometry × field content × coupling × backreaction, the eight covered cases form a **closed**
index — E = 0, box 12, no non-monotone relations — and the
coverage is 8 of 24 cases.

**But the fraction misleads.** Non-minimal coupling is covered **nowhere**:
0 of 12 cases. And that is not an absence
of effort — Urban and Olum's counterexample is a non-minimally coupled scalar in conformally flat
spacetime, where the ANEC is **violated**, and Fewster notes state-independent QEIs can fail there.

> **COUP = 1 is a wall, not a frontier. The coverage boundary is the boundary of where the condition is
> true**, and ANEC coverage is essentially complete on the domain where the ANEC holds.

*An earlier version reported coverage as 30 of 48 and claimed every curved-space proof crosses at
*free, minimally coupled*. Only* minimally coupled *is shared — curved and interacting is covered, by
Wall and by Iizuka — and the Λ₉ articulation analogy does not hold, since COUP = 1 has no traffic at all.*

![Coverage](figures/f6_2.png)

**One further obstruction, found late and structural.** Null quantum energy inequalities have **no finite lower
bounds in four dimensions** — Fewster and Roman exhibit an explicit counterexample using vacuum-plus-two-particle
states. So the Kontou–Olum route, which runs on a null-projected quantum inequality, cannot be extended to 4d by
that path: **the object it needs does not exist.** This is why the double-smeared null energy condition was
introduced, smearing over both null directions to recover a finite bound where single-direction smearing cannot.

---

## Part IX · The axis index, and what was never named

### 9.1 Three measures, and the third did not exist

**E** measures what an index cannot carry. **The vocabulary debt** measures what it has not checked it carries
correctly — 32 of 48. **Nothing measured what it never named at all.**

Seven law-classes appear in sources this paper already cites and have no letter: CPT, energy-momentum conservation,
the generalised second law, weak cosmic censorship, the holographic bound, global symmetry conservation, the
equivalence principle. Two are sharp:

**CPT.** Greenberg gives CPT violation ⟹ Lorentz violation — **an edge into X_exp.** Its absence is a missing
forcing, not merely a missing axis.

**Energy-momentum conservation.** Banks–Susskind–Peskin's disjunction is *¬locality ∨ ¬energy-momentum
conservation.* **The index encodes the first disjunct and silently drops the second** — precisely the mis-typing
corrected in Part XI, sitting uncorrected at the root of the U axis.

### 9.2 Indexing the axes

```
cells (axes)     9
box              5,184
E                499
density          0.17%
non-monotone     21 of 42
verdict          OPEN
```

**The axis set is open**, at nine axes and at fifteen. But at 0.17% density its excess predicts nothing —
the envelope admits nearly the whole box. **This is exactly the case §1.9 excludes.**

And adding the six known-missing axes made density *worse*, 0.17% → 0.11%: **an index of few cells over many
coordinates cannot be densified by adding cells one at a time**, because the box grows multiplicatively in
value-set size while the cell count grows additively.

### 9.3 Pair-completion — an instrument that does work

The nine leave **four** value-directions unoccupied: exposure missing [1, 3], measured missing [0], in-deg missing [3], out-deg missing [0].

Four directions give six pairs, and **every hand-found axis outside the box occupies a pair — never one direction,
never three.**

| pair | status |
|---|---|
| exposure + measured | OCCUPIED: GSL |
| exposure + in-deg | **empty — predicts an axis** |
| exposure + out-deg | OCCUPIED: E-p conservation, equivalence principle, global symmetry |
| measured + in-deg | **empty — predicts an axis** |
| measured + out-deg | **empty — predicts an axis** |
| in-deg + out-deg | **empty — predicts an axis** |

**Four empty pairs, four predictions:**

| pair | the axis it predicts | candidate |
|---|---|---|
| exposure + in-deg | rarely theorised, forced by three other coordinates | — describable, not nameable |
| measured + in-deg | unmeasured, forced by three others | the holographic / Bekenstein bound |
| measured + out-deg | unmeasured and terminal, heavily theorised | weak cosmic censorship |
| in-deg + out-deg | a pure sink: three things force it, it forces nothing | black-hole information recovery |

**Weak cosmic censorship** is the strongest: named by Penrose, Landsman, Senovilla and Ishibashi–Maeda–Mefford,
carrying no experimental bound, and terminal in the edge set. **It has been used as a hypothesis throughout this
work and never given an axis.**

> **Pair-completion found a missing coordinate rather than recording one I noticed.** It works not through E, which
> is uninformative at this density, but through the completion of occupied directions.

**One confirmation from six hand-chosen cases is suggestive, not established.** The four directions come from seven
properties I chose, and the six axes were chosen by me. The method is a search heuristic.

---

## Part X · Five more indices, and what the null case is

Part I's thesis needs instances that are not the two it was built from. **Five were built** — V3 geometry, V6 solution, the local null surface, the ANEC proofs and the charger index — and §10.2's measure is a comparison, not a sixth index.

### 10.1 The vocabularies that are indices

| index | letters | cells | box | E | non-monotone | verdict |
|---|---|---|---|---|---|---|
| **V3 geometry** | 5 | 25 | 48 | 0 | 0 | **CLOSED** |
| **V6 solution** | 4 | 14 | 24 | 0 | 0 | **CLOSED** |
| **local null surface** | 6 | 32 | 64 | 0 | 0 | **CLOSED** |
| ANEC proofs | 4 | 8 | 12 | 0 | 0 | **CLOSED** |
| charger index | 6 | 6 | 192 | 25 | 7 | open, at 3.1% density |

**Every VOCABULARY index closes; the charger index does not.** The defect is in V1, on the V1–V3 edge, in the charger index at E = 25, and in the partition itself — nowhere else. *An earlier draft read* everything built outside V1 closes, *in the same table that shows the charger index open.*

**V6 carries the conjecture.** Four of five known achronal-ANEC violations fall outside its admissible
region — chronal geodesics, fixed backgrounds, Planck-scale — and the fifth was withdrawn by its own
authors as a conformal artefact. **The self-consistent achronal ANEC is free of counterexamples because
V6 excludes them.** That is a scoping fact about the solution index, not a physical fact about the laws.

**And the charger index converges with Part VIII independently.** Six chargers over six properties: every
one has trigger arity 1, and **none is universal.** The empty JUR = 0 direction is exactly the charger
shape that would close the law index — §8.2 computes that an unjurisdicted forcing gives E = 0 at 1,938
cells. **The missing cell in the charger index and the defect in the law index are one absence at two
levels**, and the two computations share no code.

### 10.2 The measure

Part II's §2.8 says the measure is external. It is, and not for the reason given.

| measure | resolves | distinct values | faithful |
|---|---|---|---|
| Coulomb  -1/n^2 | 47.7% | 3 | no |
| shell occupancy k | 60.8% | 3 | no |
| Madelung  n+l then n | 65.0% | 5 | no |
| n, l, k | 81.4% | 12 | no |
| grade  sum of coordinates | 100.0% | 18 | YES |
| the cell itself | 100.0% | 976 | YES |

**A faithful measure exists and compresses 976 cells to eighteen values.** Any strictly monotone function
of the coordinates is automatically faithful, since a strict descent in the order drops some coordinate
and raises none. **Physics does not use it.** The Coulomb energy resolves 47.7% of the order; the grade
resolves all of it and means nothing.

> The obstruction is not that the measure cannot be compressed. **It is that the compression which works
> is not the one that corresponds to anything.**

### 10.3 Λ audited, and the null case relocated

|  | conflated | clean | ungrounded | missing | rate |
|---|---|---|---|---|---|
| violation index V1 | 5 | — | — | — | 56% |
| **Λ** | 7 | 4 | 1 | 1 | **54%** |

**The rates are indistinguishable.** The paper presented Λ as the clean control and the violation index
as the contested case; proportionally they are the same.

**The causes differ.** V1 conflates because two literatures used one word. **Λ conflates because an
approximation is not a coordinate**: n and ℓ are exact eigenvalues in hydrogen and configuration labels
everywhere else, and the central-field approximation is nowhere in the index.

**And q is ungrounded** — no referent in the spectroscopic literature at all. Not conflated: there is
nothing to conflate with. **Audit 22 cannot detect this**, because if no theorem names the term, the pair
never enters its table.

|  | clean | conflated |
|---|---|---|
| **closed** | **V3 geometry** | **Λ**  ·  V6 solution |
| **open** | *empty* | **V1 laws** |

> **Closure does not certify the letters. An index can be globally consistent and still not mean what it
> says.** E states that the cells are mutually consistent; it says nothing about whether the coordinates
> refer to anything. **That is why audit 22 has to exist**, and the paper has never given the reason that
> plainly.

**Λ is not the control. It is the closed-and-conflated instance**, and the clean null case transfers to V3,
whose five letters all carry exact Hawking–Ellis definitions.

### 10.4 Where the null-energy gap actually is

Six independent curved-space routes to the ANEC. **Five require a Killing field or a horizon generated by
one**; the sixth replaces it with a holographic dual and yields a weighted bound rather than the ANEC.

> **The ANEC gap in curved spacetime is not an ANEC problem. It is a modular theory problem.**

Both routes fail for one reason. The causality route needs a lightcone OPE, organised by a symmetry group.
The relative-entropy route needs the modular Hamiltonian to be **geometric** — an integral of the stress
tensor — which is Bisognano–Wichmann in flat space and Kay–Wald only for bifurcate Killing horizons.
**"K is an integral of T" and "the OPE is organised by a symmetry group" are the same statement.**

**And the obvious repair is excluded by theorem.** Sorce (2024): *any geometric modular flow must be
generated by a conformal Killing field.* So a near-horizon-boost extension does not exist in general — not
hard, excluded.

**The route that does not need geometric flow is half-sided modular inclusion**, which gives K in terms of
T for null cuts even where the flow is non-local. Localising the target in the null-surface index of §10.1:

| region | cells | status |
|---|---|---|
| Killing horizons — STAT = 0 | 8 | HSMI established, arbitrary interacting QFT |
| non-expanding, Killing or not — THETA = 0 | 16 | the target |

> **The open question is HSMI on isolated horizons** — non-expanding, quasi-local, no Killing field, no
> asymptotic structure. One cell from where it is proved, and the cell is standard in general relativity.

**The frontier moved in 2026.** Chandrasekaran and Flanagan construct half-sided supertranslation
generators from corner edge modes, with the modes serving both as the anchor for gravitational dressing
and as the source of the translation generator, giving a Type II∞ algebra per horizon cut. The generator's
two-sided dependence enters **only through the expansion**, so on a non-expanding horizon it is one-sided
at leading order — the regime that matters.

### 10.4b The one open cell, and one computation in it

Following §10.4's target down gives a single surface class and a single condition.

**The target is a boundary point, not a region.** Two routes to the translation exist: the Killing
parameter, and the corner charge **𝒫_α ∝ £_ℓ μ = Θμ**. An isolated horizon has **Θ = 0 exactly and no
Killing field**, so both are switched off. Θ ≠ 0 or a Killing field present, and a route exists.

**And no third geometric route can exist.** Both routes need a quantity varying along the generators,
and an isolated horizon is *defined* by nothing intrinsic varying — £_ℓ q_ab = 0, £_ℓ D_a = 0, κ and Ψ₂
constant. **The geometry is exhausted by the definition**, which leaves only the state.

**The chain from there:**

|  | step | source |
|---|---|---|
| 1 | I(A:C|B) = 0 | vanishing conditional mutual information |
| 2 | short quantum Markov chain | Hayden-Jozsa-Petz-Winter 2004 |
| 3 | exact Petz recovery | Petz 1986, stated FOR VON NEUMANN ALGEBRAS |
| 4 | K_A local: an integral of T_++ | Casini-Teste-Torroba 2017 |
| 5 | sigma_t(M(u+d)) subset M(u+d) | half-sided modular inclusion |
| 6 | U(a) with P >= 0 | Wiesbrock 1993/97; Araki-Zsido 2004 |
| 7 | P = integral of T_++ | identification via dressed commutators |
| 8 | the achronal ANEC |  |

**Three links are fully general** — Petz, Wiesbrock, Borchers, all stated for von Neumann algebras.
**One needs re-expression**: Hayden–Jozsa–Petz–Winter uses entropies, and S(A) is infinite in Type III,
so the statement is *unsayable* until translated into Araki relative entropies. **One has a blocked
proof**: Casini–Testé–Torroba's locality, whose OPE route needs conformal symmetry and whose algebraic
route needs the null plane.

> **A statement generalises when its terms are defined in the wider setting; a proof generalises when
> every step's hypothesis is available there.** One failure of each kind, needing different repairs:
> translate the vocabulary, or find a new argument.

### 10.4c C1, computed

Working backwards from locality: it requires the modular flow not to mix generators, which requires the
algebra to factorise over them. **That factorisation is computable.**

The presymplectic potential on a null surface is **θ = δφ £_ℓφ η**, which contains **no transverse
derivative**. So Ω is block diagonal in y, so Ω⁻¹ is, and

**{φ(u,y), φ(u′,y′)} = (1/4√q(y)) sgn(u−u′) δ^{d−2}(y−y′)**

| test | off-generator block of Ω⁻¹ |
|---|---|
| 4, 6 and 8 generators, arbitrary √q(y) | **0.000e+00** at every size |
| control: an artificial ∂_y term added | nonzero immediately |

**This is linear algebra, not symmetry.** It holds for any y-dependence of √q — hence on any null
surface with a u-independent transverse metric, which is exactly a non-expanding horizon.

**And it survives interactions, selectively.** A potential V(φ) contributes no boundary derivative term,
so C1 holds for **any non-derivative interaction**. Derivative couplings add transverse rungs and it fails.

| theory | constraint graph on the null surface | certificate |
|---|---|---|
| free, or any V(φ) | a **forest of paths**, one per generator, no edges between them | stronger than a tree |
| derivative coupling | a **ladder** — transverse rungs create cycles | lost, as at Λ₉′ |

**Not a caterpillar — simpler.** Λ₈ is a caterpillar with a spine; the null surface with non-derivative
interactions has no spine at all. **The transverse direction contributes no edges.** And the failure
mode when it does is the same one Λ₉′ exhibits: an added constraint closes a cycle and Freuder is lost.

*CTT cover general interacting theories on the null plane. This argument is more general in the geometry
and less general in the interaction; neither contains the other.*

### 10.4d C2, the open condition

> Let N be a non-expanding horizon with no Killing field, ω a Hadamard state, M(u) the algebra of N_{>u}.
> **C2: Δ_{M(u₁)}^{it} M(u₂) Δ_{M(u₁)}^{−it} ⊆ M(u₂) for all t ≤ 0 and all u₁ < u₂.**

Two nearby forms are wrong and both are easy to write:

| form | why not |
|---|---|
| SSA saturation as written | unsayable in Type III: every entropy is infinite |
| σ_t(N) = N for all t | **too strong.** by Takesaki it gives a normal conditional expectation, which Type III₁ factors do not admit — and it would make the generator **zero** |

**C1 gives the tensor decomposition; C2 asks whether the state respects it.** The Hadamard condition
constrains short-distance behaviour of the two-point function and says nothing about correlations
between generators at finite transverse separation. **They are independent, and the second is the whole
remaining problem.**

### 10.4e The converter, and a dimensional ledger

**Half-sided modular inclusion is what turns algebra into geometry.** In: (M, N ⊆ M, Ω) with
σ_t(N) ⊆ N — no manifold, no metric, no coordinates. Out, by Borchers and Wiesbrock: **the affine ax+b
group acting on a line.** A null generator with its affine parameter, manufactured from an inclusion of
algebras. Leutheusser and Liu use exactly this for emergent horizons and emergent time.

**And the direction is inverted here.** In holography the algebra is given and the geometry derived. **On
an isolated horizon the geometry is given** — generators, affine parameters, cuts — and what is missing
is the algebraic certificate that it is the geometry the converter would have produced.

**The dimensional accounting is checkable:**

```
d − 1  =  1  +  (d − 2)
          |       |
          |       the transverse direct integral — C1 — which NO half-sided
          |       modular inclusion supplies
          one HSMI per generator: one affine line, one real parameter
```

**The two open pieces are dimensionally distinct**, which is why one yielded to a symplectic computation
and the other has not.

*Two cautions. Borchers–Wiesbrock produces a group representation; identifying it with the horizon's own
null line is a further step, free on a null plane and not free here. And the status bit — semifiniteness —
is **zero**-dimensional, while the affine line is one-dimensional. They are different objects and
collapsing them is the error §12.2b logs as* TRANS gates the trace.

### 10.5 The translator, and the theorem chain that defines it

Three of the instances above need different repairs, and only one needs anything invented.

| repair | in bits | cost | instance |
|---|---|---|---|
| SPLIT | two unit vectors mistaken for one | no bit changes; the merge was the error | U, L, SD, X - all four done here |
| DICTIONARY | one unit vector, two bases | no bit changes; a rotation inside a vocabulary | 2K: Racah recoupling coefficients translate between LS, LK, jK and jj exactly |
| TRANSLATOR | weight 0 -> weight 1 | one bit, and it must be manufactured | supertranslation: gravitational dressing, with corner edge modes as the output |

**Status is one bit per vocabulary, and the partition forces one-hot.** Across
40 terms, 5 of
16 patterns occur and every one has weight 0 or 1:
**every term is physical in exactly one vocabulary, or in none. one-hot IS the partition.**

| weight | count | meaning |
|---|---|---|
| 0 | 2 | needs a translator, or is ungrounded |
| 1 | 35 | predicates on exactly one vocabulary |
| 2 | 3 | a relation, or an unsplit conflation |

**The test recovers by one rule what three separate investigations found by hand, and finds nothing
new** — 0 new flags across forty terms. Its limit is real:
weight 2 means RELATION or CONFLATION and the test cannot tell them apart; weight 0 means UNGROUNDED or CONSTRUCTIBLE and likewise.

**And n and ℓ have no dictionary.** n and l have none. exact hydrogenic eigenvalues and central-field labels are related by a LIMIT, not an isomorphism, and a limit is not invertible.

> **A : Loc -> Alg is the geometry-to-algebra translator. it is well-defined on whole spacetimes and does not extend to subregions, because specifying a subregion requires dressing. the edge modes are what restores it.**

### 10.6 The chain, primary-sourced

|  | theorem | statement | role |
|---|---|---|---|
| T0 | Reeh-Schlieder | the vacuum is cyclic and separating for local algebras | the physical input that makes the rest applicable |
| T1 | Tomita-Takesaki | for (M, Omega) there exist Delta and J with Delta^it M Delta^-it = M | supplies the modular flow sigma_t |
| T2 | Borchers / Wiesbrock | half-sided modular inclusion is CHARACTERISED by the existence of a one-parameter unitary group with positive Hermitian generator | supplies the translation. an iff, not an implication. gap filled and extended to weights by Araki-Zsido 2004 |
| T3 | Takesaki, Acta Math 131 (1973); Theory of Operator Algebras XII.1.1 | N = M crossed sigma^phi R is type II_infinity with a faithful semifinite normal trace tau, tau . theta_s = e^-s tau, and M = N crossed theta R, uniquely | FLIPS THE BIT: type III_1 -> type II_infinity. an involution up to stabilisation. |
| T4 | semifiniteness | a semifinite factor carries a trace, hence a von Neumann entropy | type III carries none |

**A fifth caveat, and it is on T0.** Reeh–Schlieder is a **theorem** in Minkowski space, proved from
the analyticity of vacuum correlation functions, the spectrum condition and the action of the
Poincaré group on the vacuum. **In curved spacetime it is a property**, established for free massive
scalar fields and elsewhere assumed as an axiom. The chain above needs it for **interacting** fields
on an isolated horizon, where none of the three Minkowski ingredients is available and no proof is
known. T0 is therefore an assumption of the same standing as T2, and the chain has two open links
rather than one.

```
IN     type III_1     no trace, no density matrix, no entropy     weight 0
OUT    type II_inf    trace, density matrix, entropy              weight 1
```

**The status bit is semifiniteness**, and von Neumann's classification makes it genuinely binary: an
algebra either admits a trace or it does not. **T3 flips it and T2 licenses T3 to run on a horizon** —
without a positive-generator translation there is nothing to cross by. T3's uniqueness and invertibility
are what make it a bit rather than a rung on a ladder.

**Four caveats, and the third is the weak joint:**

| caveat |  |
|---|---|
| T2 is the open problem | HSMI holds for cuts of KILLING horizons (Wall; Casini-Teste-Torroba; Witten). on an isolated horizon it is unproved - and because T2 is a characterisation, proving it is exactly equivalent to producing the positive-generator translation. |
| T3 is stated for R | a 2024 result shows the generalisation to arbitrary locally compact groups is NOT automatic: it needs an invariant weight, KMS on a subgroup, and centrality of the modular automorphism group. |
| the physical group is not R | Chandrasekaran-Flanagan cross by C-infinity(S^{d-2}), one generator per angle. their Appendix F reaches Takesaki through an ANGULAR MODE CUTOFF and an inductive limit. whether the limit satisfies the 2024 conditions is not settled here. |
| the trace is not invariant | tau . theta_s = e^-s tau. this is why entropy in these constructions is defined only up to an additive constant. |

### 10.7 A term whose status is scope-dependent

| instance | what changes across the scope |
|---|---|
| Buniy | a hypothesis operative in one scope and not another |
| U, L, SD, X | a word meaning one thing in one literature and another elsewhere |
| 2K | a label meaning different things in different coupling schemes |
| n, l | exact in hydrogen, approximate everywhere else |
| supertranslation | gauge in geometry, physical in the algebra |

**Five instances, one shape**, and the last is stated as physics rather than bookkeeping. Chandrasekaran
and Flanagan, following Rovelli: *gauge redundancy is not merely a redundancy; it is the bookkeeping
needed to relationally describe subsystems in a gauge-invariant system.* Their footnote: the edge modes
"appear as gauge degrees of freedom in the top down approach, but as physical degrees of freedom in the
bottom up approach."

**One directed test.** Where an anchor exists — null infinity — BMS supertranslations carry nonvanishing
charges and parametrise the final state of collapse alongside mass and angular momentum: **physical in the
geometry too.** Where it is absent, an NEH's free data is provably supertranslation-invariant.
**The reversal is present exactly where the anchor is absent**, and the test facts come from a literature
the shape was not built from.

**Status: one test passed, one directed search for a counterexample finding none.** That is thin evidence,
and it is more than the six-instance pattern withdrawn in §12.2 had.

---

## Part XI · Results

**1. E measures whether an index can carry a constraint, and there are two failure modes.** Ordering — the term is
present but non-monotone, repairable. Arity — every term is monotone and the constraint needs more places,
not repairable. Four objects, one of each and two of the second at different arities. No third mode found.

**2. A universe is a globally consistent constraint network.** Λ closes at every level of the tower, for
parastatistics orders 1, 2 and 3, to Λ₁₃ — boxes swept to 172,523,520. The certificates
are Freuder and Montanari.

**3. A transition between universes is not expressible as one.** Defect 30 at nine letters and
816 at fifteen, both collapsing to **one core cell**, with arity 3 throughout.

**4. The core survived doubling the alphabet.** Five conflations split, one axis added, half the cells removed as
non-theories, two generators instead of one, twenty-seven times the multiplicity — and the core stayed one cell for
reasons expressible in two lines. **The structural results are about the operator, not the encoding.**

**5. The unnamed currency was a conflation.** At nine letters Buniy looked like a disjunction with an unspecified
price. At fifteen it is a forcing with a single currency — ghosts — and the appearance of a disjunction was the
alphabet merging ghosts with Lindblad evolution.

**6. Jurisdiction creates arity.** A jurisdicted forcing and an unjurisdicted disjunction give identical defects.
The defect is largest at exactly one scope condition, so nearly-universal theorems are the hardest to index.

**7. The defect is arity, and nothing else.** An earlier draft attributed it to a severed system graph.
On the derived four-vocabulary partition the graph is **complete**: 4 nodes, 6 edges, one component. The six
repair operations failed because the constraint has three places, which was always the explanation — the
graph story was decoration on a partition since withdrawn. **What is true of the system is that two of its
constraints are ternary**: one among the law letters, one on the spacetime–state cross-edge.

**8. An index's conflations are invisible from inside it.** Twenty-one audits passed on a document containing five.
Audit 22 is external by construction and its output is a debt: 32 of 48 pairs unchecked.

**9. Everything built outside V1 closes.** V3 geometry, V6 solution, the local null-surface index and
the covered ANEC cases are all globally consistent. The defect is in V1, on the V1–V3 edge, and in the
partition — nowhere else.

**10. Closure does not certify the letters.** Λ closes in all four coupling schemes with seven of thirteen
letters conflated, one ungrounded, and one quantity read but never indexed. **E states that the cells are
mutually consistent and says nothing about whether the coordinates refer to anything.** The clean null
case is V3, not Λ.

**11. The vocabulary partition is the BFV functor.** Four parts — theory, spacetime, algebra, state — with
the terms that refuse to place being *relations* between them. The self-consistent achronal ANEC is one
such relation, which is why no law-index coordinate can carry it.

**12. The null-energy gap is a modular theory gap.** Five of six curved-space routes need a Killing field;
the geometric-modular-flow repair is excluded by theorem; and the live target is half-sided modular
inclusion on isolated horizons — one cell from where it is proved.

**13. Openness is the signature, not a failure.** A closed index is a universe. Neither violation index closes, and
neither does the axis index that contains them.

---

## Part XII · Register

### 12.1 The promotion ledger

| claim | status | basis |
|---|---|---|
| the two failure modes: ordering and arity | **PROMOTE** | four objects, each demonstrated computationally |
| E requires density to be informative (asymmetric) | **PROMOTE** | measured on six objects; E=0 informative at any density |
| audit 22 is necessary and cannot be automated | **PROMOTE** | 21 audits passed on a document containing five conflations |
| five of nine coordinates are conflated | **PROMOTE** | each shown against a named theorem with a quoted hypothesis |
| the axis set is open | **PROMOTE** | computed at nine and at fifteen axes; E > 0 both times |
| B.3.1 as a general law about all indices | **HOLD** | three instances, all built here, all in one session |
| pair-completion predicts missing axes | **HOLD** | one confirmation from six hand-chosen cases |
| the four predicted axes | **HOLD** | candidates; three have plausible occupants, none verified |
| the vocabulary partition | **HOLD** | mine; no source draws those lines |
| defect 30 / core 1 as physical numbers | **HOLD** | computed over a coordinate set that is demonstrably incomplete |

**Everything promoted is about the method. Everything held is either a general claim or a physical number.** That
split was not planned and is the correct diagnosis: the instrument is better characterised than anything it measured.

### 12.2 Withdrawals

| claim | cause |
|---|---|
| defect 60, disjunction at NEC >= 2 | the constraint is about scale; macroscopic wormholes are excluded, Planck-scale are not |
| Helly number unbounded | a falling joint-given-pairwise ratio measures how often random families intersect, not the Helly number |
| projection-covariance as a scaling law | the defect does not scale; the core is one cell at every resolution |
| X >= 1 -> U >= 1 | severed at its second link by the authors of its first |
| instability routed to a disjunction | Buniy gives instability, not a preferred frame; the second disjunct was mine |
| NEC is the unique family-A-preserving axis | it is one of eight |
| the defect grows with jurisdiction count | it shrinks; narrower jurisdiction charges fewer cells |
| MMP escapes the ANEC | it violates the ANEC and escapes the ACHRONAL ANEC |
| a dropped edge in the exclusion classifier | DNc = 2 -> IC = 2 was omitted when transcribing the edge list |
| the same-axis tautology, twice | the ANEC as a preservation is the NEC axis excluding itself; logged at nine letters and repeated at fifteen |
| three obstructions, one theorem | reviving Hartman connects the system and CREATES a cycle; two obstructions, traded |
| no curved-space extension exists (withdrawn, then restored) | withdrawn on an abstract whose scope-phrase modified the regulator, not the QNEC; restored on the full text |

### 12.3 Withdrawn since v2.0

Every entry below post-dates the previous draft, and several correct claims that draft asserts.

| claim | cause |
|---|---|
| arity tracks vocabulary span | falsified: eight binary cross-vocabulary edges give E=0, and a two-vocabulary ternary constraint gives E=176. arity determines arity. |
| the 30-of-48 ANEC coverage figure | superseded: 8 of 24, and half the box is a region where the statement is false |
| every curved proof crosses at free, minimally coupled | only minimally coupled is shared |
| Lambda as the clean control | 7 of 13 letters conflated; the null case transfers to V3 |
| the seven-vocabulary partition | derived down to four from the BFV functor |
| Hartman is vacuous | it fires in flat space and excludes 2 cells; the earlier computation was circular, having built Hartman-plus-more into the cross-edge |
| the nine-letter density of 3.99% | the box is 19,440; the density is 12.19% |
| the bilingual equation is arity 3 | it is arity 2, and the script printed a pre-written conclusion contradicting its own output |
| promotion as an ordering repair | made E worse, 8 to 16 |
| the observer resolves the reversal | the encoding forced ST constant; E=0 was trivial |
| the curved-space extension needs a near-horizon boost theorem | excluded by Sorce |
| the coupling-scheme comparison | an unfair convention applied to the alternatives |
| the severance of the system graph | an artefact of the seven-vocabulary partition. on T/M/A/S the graph is complete: 4 nodes, 6 edges, 1 component. the six repairs failed on ARITY, which was always the explanation. |
| Graham-Olum listed as a charger that fires | it is a conjecture with a sufficiency proof, not a theorem |
| the slide-within-rows figure of 8,856 | refuted by a bound, not merely unreproduced: the operation acts on a 3-coordinate object whose box is at most 40. the correct value is 5. |
| TRANS gates the trace | the crossed product is by the MODULAR flow, so the trace needs MOD and COND only. TRANS gates the relation BETWEEN cuts: the GSL and the QFC. an isolated horizon would carry an entropy at each cut and no law relating them. |
| the vanishing of the two-sided term at Theta = 0 is favourable | the whole generator vanishes there, since P_alpha is proportional to Theta. a limit read as a simplification when it was the obstruction. |
| the modular relocation is circular | it is directed: HSMI implies the ANEC, not the reverse. Chandrasekaran-Flanagan warn explicitly that the identification P = integral T_++ is not the method for proving positivity. |
| fifteen equations stated without hypotheses | found by an audit of the mathematics itself: 15 of 50 equations carried no recorded conditions. the same defect audit 22 finds at the level of coordinates, appearing at the level of equations. all fifteen now supplied; the seniority lower bound 2S <= v was verified against enumerated terms. |

### 12.4 The numeric debt, discharged and marked

Audit 24 flagged claims the paper carries with no dataset behind them. Recomputing them:

| value | claim | status |
|---|---|---|
| 1,938 | cells under the unjurisdicted forcing, E = 0 | **confirmed** |
| 1,654 | Λ₉ | **confirmed** |
| 1,561 | Λ₉′ after the admissible Pauli cut | **confirmed** |
| 93 | cells removed by that cut | **confirmed** |
| 43.1% | axis 11 without the third exact set | explained and recorded |
| 7,734 | merge by linearisation at fifteen letters | **confirmed** |
| 5 | slide within rows at fifteen letters | **corrected** from 8,856, which exceeds the operation’s bound of 40 |

**Five of six clear and one is corrected.** The sixth was not merely unreproduced — it was refuted by
a bound. The slide operation acts on a three-coordinate object, so its defect cannot exceed 40, and the
figure carried was 8,856. **That is the first arithmetic error the register contains**; every prior entry
was a wrong inference from correct arithmetic.

### 12.5 The audit suite has eight audits beyond the twenty-one, and two blind spots

| audit | compares | status | result |
|---|---|---|---|
| 22 term match | external + judgement | IDENTIFIED, unfillable by code | debt 32 of 48 pairs |
| 23 published values | external + mechanical | BUILT | 10 of 10 LS term tables reproduced; 0 microstate mismatches |
| 24 unbacked claims | internal + debt | BUILT | 14 of 105 numeric claims unbacked; 5 false positives, 6 substantive, 0 wrong |
| 25 ungrounded coordinates | no external referent at all | IDENTIFIED | audit 22 cannot see it: if no theorem names the term, the pair never appears |
| 26 — | *unassigned; the numbering runs 22–25 and 27–30* | — | — |
| 27 possibility bound | a reported E against the box of its object | BUILT | 12 objects checked, 1 failure (8,856, ceiling 39), no others found |
| 28 contents | every claim in the paper, graded | BUILT | 4 proved, 14 computed, 6 cited, 6 held, 5 open, 30 withdrawn |
| 29 the paper itself | structure, delivery, ratios | BUILT | 6 of 8 promises delivered, 2 withdrawn and marked; 0.60 established per withdrawal |
| 30 hypothesis coverage | every equation against its stated conditions | BUILT | 15 of 50 unhypothesised, all now supplied |

**Audit 23 is the only external validation in the construction**, and it passes: ten published LS term
tables reproduced exactly, zero microstate discrepancies against C(4ℓ+2, k). The subroutine that produces
every density figure and the axis-11 bound is verified against Condon–Shortley.

**Audit 27 — the possibility bound — is the sixth.** For any object, 0 ≤ E ≤ box − cells. Twelve
objects carry a recorded (cells, box, E) triple and eleven pass; the twelfth is the slide figure of
8,856 against a ceiling of 39. **No second impossible value exists in the construction.** Its coverage
gap is structural: 5 objects report a defect without recording
a box, and cannot be checked at all — which is how 8,856 survived. **The procedure that closes it is to
report the box alongside every defect.**

**Audit 24 finds 14 of 105 numeric claims unbacked** — five are regex false positives, six are values
computed in session and never written to a dataset, and **none is wrong.**

**Both were automatable and neither existed in the twenty-one-audit suite.** The audit index of Part IX
predicted both by clustering: twenty-one of twenty-two audits share all three properties — internal,
automatable, pass/fail — and the empty combinations were exactly these two.

### 12.6 The recurring class

**30 instances of one class: a conclusion drawn from a comparison that was not licensed.**
The dominant subtype is now **the encoding carries the conclusion** — four consecutive attempts at the bilingual repair each embedded the answer in the setup. The arithmetic was
correct in every case; the warrant was not. Subtypes:

- matching a rung to a theorem by the word rather than the content (U, L, X, SD)
- searching by the name of a result rather than by what implies it
- attaching a scope-phrase to the nearest noun rather than to what it modifies
- repeating a logged correction (the same-axis tautology)

**Two were caught by data already on screen**, and one is a straight repeat of a logged correction rather than a new
variant. The register is reported in full because the pattern of failure is itself a finding, and because it is the
evidence that the checking apparatus works.

### 12.7 The seven propositions

|  | proposition | verdict | basis |
|---|---|---|---|
| P1 | `X >= 1 -> U >= 1` | **REFUTED** | the ordinary second law survives Lorentz violation (Eling et al) |
| P2 | `NEC >= 3 -> X >= 1` | **REFUTED** | Buniy is scoped to Lorentz-invariant theories |
| P3 | `U >= 1 -> IC = 2` | **REFUTED** | the U=1 rung is occupied; Lindblad operators computed (Nikolic) |
| P4 | `U >= 1 -> X >= 1` | **FALSE ON THIS AXIS** | true for ghosts, which were not a rung until the split |
| P5 | `NEC >= 3 -> U >= 1` | **CONDITIONAL** | flat space proven; curved rests on Graham-Olum |
| P6 | `NEC >= 3 -> SD` | **NOT ASSERTABLE** | a single disjunct of Hartman |
| P7 | `NEC >= 3 -> IC = 2` | **NOT ASSERTABLE** | a single disjunct of Hartman |

**Four refuted, two unassertable, one conditional. None closes the index**, and with Buniy's jurisdiction
established as necessary, P5's conditionality no longer decides the matter.

---

## Part XIII · Open

| item | state |
|---|---|
| the self-consistent achronal ANEC in 4d | no proof, no counterexample, 19 years. Null QEIs have **no finite lower bounds** in four dimensions (Fewster–Roman), which is why the Kontou–Olum route cannot be extended by that path |
| Hartman for interacting theories on curved backgrounds | the single change that connects the system; does not exist, checked in both the ANEC and QNEC literatures |
| whether Buniy extends to Lorentz-violating second-order theories | reopened once the operative hypothesis was identified as derivative order |
| the 32 unchecked term pairs | IC has six and has never been checked once |
| Λ’s own conflations | the symmetric question, never asked: thirteen coordinates against Condon–Shortley and Racah |
| the four predicted axes | cosmic censorship strongest; three have plausible occupants, none verified |
| a completeness criterion for the coordinate set | none exists. Pair-completion is a heuristic with one confirmation |
| whether the two failure modes hold for indices not built here | needs someone else’s index |
| HSMI on isolated horizons | the live target; being worked on from the corner-mode side |
| the six undocumented values | computed in session, carried by the paper, absent from any dataset |
| the two halves | any joining map is cross-vocabulary; the bare product multiplies the defect by 976 and adds nothing |

### 13.1 The join, and why it stays open

For a product with no linking constraint every cross-envelope is vacuous, so **R(A × B) = R(A) × R(B)** and

**E(A × B) = |A|·E_B + |B|·E_A + E_A·E_B**

For Λ and the violation index, with E(Λ) = 0: **E = 976 × 30 = 29,280.** The defect is **extensive** — multiply
an index by anything and it scales with the other factor. **The core is the invariant across products; E is not.**

So the halves are not unjoined for want of a map. **There is nothing to gain and a factor of 976 to lose**, and any
linking constraint is cross-vocabulary, so neither index could carry it.

---

## Appendix A · Equations, with hypotheses

**Every equation is stated with the conditions under which it holds and the grade of its
verification.** An audit of this appendix found that fifteen of fifty equations previously carried no
recorded hypotheses; all fifteen are now supplied, and the omission is logged in §12.3 as a defect of
the same kind audit 22 finds at the level of coordinates.

| grade | meaning | count |
|---|---|---|
| **PROVED** | proved in this document | 4 |
| **COMPUTED** | verified here by computation | 14 |
| **CITED** | someone else’s result, stated with provenance | 27 |
| **DEFINITIONAL** | a definition, not a claim | 3 |
| **OPEN** | stated as unresolved | 2 |

### A1

**A-hat_i(X) = { x_i : x in X }**

*Hypotheses.* X a finite set of integer tuples

*Provenance.* definition

*Status.* definitional

### A2

**phi-hat_ij(v) = max { x_i : x in X, x_j <= v }**

*Hypotheses.* i =/= j; the max over an empty set is -inf

*Provenance.* definition

*Status.* definitional; non-decreasing in v by construction

### A3

**R(X) = { x in PROD_i A-hat_i(X) : x_i <= phi-hat_ij(x_j) for all i =/= j }**

*Hypotheses.* as above

*Provenance.* definition

*Status.* definitional

### A4

**E(X) = |R(X)| - |X| >= 0**

*Hypotheses.* none beyond A1-A3

*Provenance.* PROVED here, Prop 1.2

*Status.* PROOF: for x in X and any i =/= j, the set {y_i : y in X, y_j <= x_j} contains x_i since x_j <= x_j. hence phi-hat_ij(x_j) >= x_i, so x in R(X). therefore X subset R(X). QED

### A5

**X subset BPC(X) subset R(X),  BPC(X) = { x : (x_i,x_j) in proj_ij(X) for all i<j }**

*Hypotheses.* none

*Provenance.* PROVED here

*Status.* VERIFIED: R = BPC exactly on every object computed. the potential ambiguity between genuine inconsistency and envelope coarseness does not arise here.

### A5b

**R is a closure operator: extensive, monotone, idempotent**

*Hypotheses.* none

*Provenance.* extensivity PROVED (A4); monotone and idempotent COMPUTED

*Status.* R(R(X)) = R(X) verified on Lambda_8 and both violation indices; monotonicity held on 30 nested random pairs with no failure. NOT proved in general.

### A5c

**E(X) = 0 iff the binary constraint network is globally consistent**

*Hypotheses.* the constraints are the monotone binary projections

*Provenance.* identification, standard CSP

*Status.* this is the identification that licenses Freuder and Montanari

### A6

**1 <= n <= n_max**

*Hypotheses.* caps (n,e,l,k,f) = (3,3,1,3,1)

*Provenance.* construction

*Status.* each bound binds ONE coordinate by a monotone function of ONE other -- the closure rule 1.8

### A7

**0 <= l <= n - 1**

*Hypotheses.* caps (n,e,l,k,f) = (3,3,1,3,1)

*Provenance.* construction

*Status.* each bound binds ONE coordinate by a monotone function of ONE other -- the closure rule 1.8

### A8

**1 <= k <= 4l + 2**

*Hypotheses.* caps (n,e,l,k,f) = (3,3,1,3,1)

*Provenance.* construction

*Status.* each bound binds ONE coordinate by a monotone function of ONE other -- the closure rule 1.8

### A9

**0 <= q <= k**

*Hypotheses.* caps (n,e,l,k,f) = (3,3,1,3,1)

*Provenance.* construction

*Status.* each bound binds ONE coordinate by a monotone function of ONE other -- the closure rule 1.8

### A10

**0 <= f <= e - 1**

*Hypotheses.* caps (n,e,l,k,f) = (3,3,1,3,1)

*Provenance.* construction

*Status.* each bound binds ONE coordinate by a monotone function of ONE other -- the closure rule 1.8

### A11

**0 <= g <= min(4f + 2, q)**

*Hypotheses.* caps (n,e,l,k,f) = (3,3,1,3,1)

*Provenance.* construction

*Status.* each bound binds ONE coordinate by a monotone function of ONE other -- the closure rule 1.8

### A12

**0 <= 2S <= k**

*Hypotheses.* caps (n,e,l,k,f) = (3,3,1,3,1)

*Provenance.* construction

*Status.* each bound binds ONE coordinate by a monotone function of ONE other -- the closure rule 1.8

### A13

**0 <= 2S-prime <= g**

*Hypotheses.* the target subshell is f^g in LS coupling for the target; g electrons in one subshell.

*Provenance.* tower level 9

*Status.* a set of g electrons has maximum total spin g/2, attained when all spins align, so 2S <= g. the LOWER bound is 0 for even g and 1 for odd g; the index uses the weaker 0 <= 2S-prime, which is why the lattice is loose here.

### A14

**2S-prime <= v <= g**

*Hypotheses.* Racah seniority for the configuration l^N; the pairing interaction has the eigenvalue structure (n-v)(2j+3-n-v).

*Provenance.* tower level 10

*Status.* v counts particles not in J=0 pairs, so v <= g. and a state of total spin S has at least 2S unpaired particles, giving v >= 2S-prime. BOTH bounds are one-parent and monotone.

### A15

**0 <= 2J_c <= phi-hat(k)**

*Hypotheses.* phi-hat(k) = max 2J over terms of l^k

*Provenance.* tower level 11

*Status.* monotone in k; requires the EXACT spin set of l^k by microstate enumeration

### A16

**|2J_c - 2f| <= 2K <= 2J_c + 2f, step 2  [EXACT]  vs  0 <= 2K <= 2J_c + 2f_max  [LOOSE]**

*Hypotheses.* jK pair coupling: J_c the total angular momentum of the core, f the orbital angular momentum of the outer electron, K = J_c + f. caps (n,e,l,k,f) = (3,3,1,3,1).

*Provenance.* tower level 12

*Status.* the EXACT form is the angular-momentum triangle rule and needs TWO parents, J_c and f. the LOOSE form replaces f by its cap f_max, giving one parent. this is the choice that keeps the tower closed: the exact form takes E from 0 to 35,570.

### A17

**|2J - 2K| <= 1**

*Hypotheses.* jK coupling; the outer electron carries spin 1/2, and J = K + s with s = 1/2.

*Provenance.* tower level 13

*Status.* adding a spin-1/2 to K gives J = K +/- 1/2, i.e. 2J = 2K +/- 1. one parent, monotone.

### A18

**density(axis) = SUM_parents |exact fibre| / SUM_parents |admissible fibre|**

*Hypotheses.* the axis is formed by adjoining one coordinate to a parent cell; "exact fibre" is the set of values genuinely realised by the physics; "admissible fibre" is the set the lattice bound permits.

*Provenance.* definition

*Status.* the ratio measures how loose the bound is. it is 1 exactly when the bound is tight. three of the six values require non-obvious exact sets, and without the third, axis 11 computes to 43.1% instead of 17.0%.

### C1eq

**|Lambda| = SUM_q |A(q)| x |B(q)| = 976**

*Hypotheses.* conditioned on the transfer coordinate q

*Provenance.* The Method, 12.6.1

*Status.* RECHECKED: 33x5=165, 33x10=330, 23x15=345, 8x17=136, sum 976. exact.

### C2eq

**A_q(z) = SUM_{n=1..3} z^n SUM_{l=0..min(n-1,1)} z^l SUM_{k=max(q,1)..min(4l+2,3)} z^k (1 - z^{min(k,3)+1})/(1-z)**

*Hypotheses.* caps (n,e,l,k,f) = (3,3,1,3,1); q the transfer coordinate, held FIXED; z a formal variable. the final factor is the generating function of the 2S-chain, 0 <= 2S <= min(k,3).

*Provenance.* The Method, 12.7

*Status.* valid for q = 0,1,2,3. A_q(1) = 33, 33, 23, 8, verified against direct enumeration. the lower limit max(q,1) encodes q <= k.

### C3eq

**B_q(z) = SUM_{e=1..3} z^e SUM_{f=0..min(e-1,1)} z^f (1 - z^{min(q,4f+2)+1})/(1-z)**

*Hypotheses.* as C2eq; the final factor is the generating function of the g-chain, 0 <= g <= min(4f+2, q).

*Provenance.* The Method, 12.7

*Status.* B_q(1) = 5, 10, 15, 17, verified. NOTE the asymmetry with A_q: the pendant 2S sits on the A side only, which is why A is a caterpillar and B is a path.

### C4eq

**Box(a,b)(z) = PROD_i z^{a_i} (1 - z^{b_i - a_i + 1})/(1 - z)**

*Hypotheses.* every fibre bottoms out in a product of chains

*Provenance.* The Method, 12.7.2

*Status.* structural

### C5eq

**E(Lambda) = 0 AND E(A_q) = E(B_q) = 0 for every q**

*Hypotheses.* the cross-sections A_q and B_q taken with their induced coordinates, at fixed q; caps as above.

*Provenance.* The Method, 12.8.5

*Status.* the second does NOT follow from the first: a closed index could in principle have defective slices whose excesses cancel in the total. here none do, and that is a separate invariant.

### D1

**I_V = CONTOUR-INTEGRAL (rho + p_r) dV**

*Hypotheses.* a static spherically symmetric traversable wormhole; rho the energy density and p_r the radial pressure in the static frame; the integral taken over the region where the null energy condition is violated.

*Provenance.* the volume-integral quantifier

*Status.* Visser-Kar-Dadhich: I_V can be made arbitrarily small by shrinking that region, which is why the NEC axis is graded by SCALE and not by violation-or-not.

### D2

**NEC_pt >= 3 AND X_exp = 0 AND EOM = 2nd  =>  U_ghost = 1**

*Hypotheses.* causal, Lorentz-invariant, second-order equations of motion, scalar/gauge with fermionic matter

*Provenance.* Buniy-Hsu-Murray 2006

*Status.* ARITY 4, reduced to 3 by Ostrogradsky (EOM higher => ghosts). the jurisdiction is what makes it ternary.

### D3

**capacity(l) = m(4l + 2)**

*Hypotheses.* parastatistics of order m

*Provenance.* generalisation of Pauli

*Status.* E = 0 verified for m = 1, 2, 3 through Lambda_13; m=1 reproduces the canonical tower

### D4

**2 <= S_CHSH <= 2 sqrt 2 <= 4**

*Hypotheses.* two spacelike-separated parties, two measurement settings each, two outcomes each; S_CHSH the standard CHSH combination of correlators.

*Provenance.* Bell / Tsirelson / Popescu-Rohrlich

*Status.* 2 is the local-realistic bound (Bell/CHSH), 2 sqrt 2 the quantum bound (Tsirelson), 4 the algebraic maximum, attained by no-signalling PR boxes. the three values are the three rungs.

### D5

**<T_kk> >= (h-bar / 2 pi) S-double-prime_out**

*Hypotheses.* a null deformation of a cut of a null surface, parametrised by lambda; S_out the entanglement entropy of the region outside the cut; the double prime is the second variation with respect to lambda.

*Provenance.* the QNEC

*Status.* a BOUND on the stress tensor by an entropy variation, not a forcing edge between coordinates. it does not enter the index as a charge, which is why it appears in the appendix and not in the edge list.

### D6

**816 = 1 x 816**

*Hypotheses.* core times multiplicity

*Provenance.* computed

*Status.* exact

### D7

**d(c) = X_exp + U_ghost + |NEC_pt - 3| + EOM + d_P(free letters)**

*Hypotheses.* the FIFTEEN-letter alphabet; the core cell (X_exp, U_ghost, NEC_pt, EOM) = (0,0,3,0); the eleven remaining letters are the "free" ones; d_P is the L1 distance from the cell's free letters to the nearest of the 816 excess patterns.

*Provenance.* the frontier distance

*Status.* exact on 1,500 sampled cells, 0 mismatches. the formula is alphabet-dependent: the pinned set changed from nine letters (SD dropped out, EOM came in).

### D8

**s(c) = 1{X_exp>0} + 1{U_ghost>0} + 1{NEC_pt=/=3} + 1{EOM>0} + s_P**

*Hypotheses.* as D7; s_P is the Hamming distance on the free letters to the nearest excess pattern.

*Provenance.* the frontier support

*Status.* exact on the same 1,500 cells. support, not distance: it counts HOW MANY letters differ, not by how much.

### D9

**R(A x B) = R(A) x R(B)  when no constraint links the factors**

*Hypotheses.* A and B indices on DISJOINT coordinate sets, and no constraint of the joint index relates any coordinate of A to any coordinate of B.

*Provenance.* PROVED here

*Status.* under that hypothesis every cross-envelope phi-hat_ij with i in A and j in B is vacuous: the max over {x_i : x_j <= v} is the global max of A_i, independent of v. so the cross conditions impose nothing and R factorises. THE HYPOTHESIS IS ESSENTIAL - a single linking constraint destroys it.

### D10

**E(A x B) = |A| E_B + |B| E_A + E_A E_B**

*Hypotheses.* as D9

*Provenance.* PROVED here

*Status.* for Lambda x violation index: 976 x 30 = 29,280. the defect is EXTENSIVE.

### E0

**Reeh-Schlieder: Omega is cyclic and separating for local algebras**

*Hypotheses.* a Hadamard state; the algebra of a region with nonempty causal complement

*Provenance.* standard AQFT

*Status.* the physical input that makes T1 applicable

### E1

**Tomita-Takesaki: S = J Delta^{1/2}, sigma_t = Ad(Delta^{it}), sigma_t(M) = M**

*Hypotheses.* M a von Neumann algebra, Omega cyclic and separating

*Provenance.* Tomita 1967, Takesaki 1970

*Status.* fully general

### E2

**Borchers: U(a) M U(-a) subset M for a >= 0 with P >= 0 and U(a)Omega = Omega  =>  Delta^{it} U(a) Delta^{-it} = U(e^{-2 pi t} a),  J U(a) J = U(-a)**

*Hypotheses.* as stated

*Provenance.* Borchers CMP 1992

*Status.* fully general; purely algebraic

### E3

**Wiesbrock: (N subset M, Omega) with sigma_t^M(N) subset N for t <= 0  =>  there exists U(a) = e^{iPa}, P >= 0, with N = U(1) M U(-1)**

*Hypotheses.* a common cyclic separating vector, extended by Araki-Zsido to a faithful normal semifinite weight

*Provenance.* Wiesbrock CMP 157 (1993), erratum CMP 184 (1997); Araki-Zsido 2004

*Status.* THIS IS A CHARACTERISATION, an iff. HSMI and a positive-generator U are the same condition.

### E4

**Takesaki: N = M crossed_{sigma^phi} R is type II_infinity with a faithful semifinite normal trace tau satisfying tau . theta_s = e^{-s} tau, and M = N crossed_theta R, uniquely in the strongest sense**

*Hypotheses.* M of type III, phi a faithful semifinite normal weight, theta the dual action

*Provenance.* Takesaki, Acta Math 131 (1973); Theory of Operator Algebras XII.1.1

*Status.* THE TRACE IS NOT INVARIANT -- it scales. this is why entropy here is defined only up to an additive constant. STATED FOR R: the extension to arbitrary locally compact groups is NOT automatic (2024).

### E5

**a semifinite factor carries a trace, hence S = -tr[rho log rho]**

*Hypotheses.* M a semifinite von Neumann factor; rho the density matrix of psi RELATIVE TO tau, i.e. psi(x) = tau(rho x).

*Provenance.* standard

*Status.* the entropy is defined only up to an additive constant, because tau itself is fixed only up to rescaling - and Takesaki gives tau . theta_s = e^{-s} tau, so the dual action moves it. type III factors carry no such trace and no such entropy.

### E6

**[K_A, K_B] = 2 pi i (K_A - K_B) = (2 pi)^2 i P,  P = INTEGRAL_{x^-=0} (B(y) - A(y)) T_{++}**

*Hypotheses.* null cuts A, B on a null plane, B >= A

*Provenance.* Casini-Teste-Torroba; Ceyhan-Faulkner

*Status.* the generator IS the averaged null energy operator. but the identification is NOT the method for proving positivity -- Chandrasekaran-Flanagan warn explicitly.

### E7

**I(A:C|B) = 0  <=>  short quantum Markov chain  <=>  exact Petz recovery**

*Hypotheses.* A, B, C consecutive regions

*Provenance.* Petz 1986; Hayden-Jozsa-Petz-Winter 2004

*Status.* PETZ IS STATED FOR VON NEUMANN ALGEBRAS. HJPW uses entropies, which are INFINITE in type III -- the statement needs re-expression via Araki relative entropies.

### F1

**Omega_N = INTEGRAL du d^{d-2}y sqrt(q)(y) [ delta phi ^ d_u delta phi ]**

*Hypotheses.* a null hypersurface with u-independent transverse metric, i.e. Theta = 0

*Provenance.* the characteristic symplectic form; theta = delta phi L_l phi eta

*Status.* CONTAINS NO TRANSVERSE DERIVATIVE. this is the whole of C1.

### F2

**{ phi(u,y), phi(u-prime,y-prime) } = (1 / 4 sqrt(q)(y)) sgn(u - u-prime) delta^{d-2}(y - y-prime)**

*Hypotheses.* as F1

*Provenance.* inverting F1 block by block

*Status.* COMPUTED: off-generator block of Omega^{-1} is 0.000e+00 at 4, 6 and 8 generators, for arbitrary y-dependence of sqrt(q). control with an artificial d_y term: nonzero immediately.

### F3

**P_alpha = -(1/8 pi) INTEGRAL_{S_0} alpha e^{Gamma_0^+} [ L_l mu - (Upsilon_0^+ - Upsilon_0^-) L_l(mu Theta) ]**

*Hypotheses.* the extended horizon phase space with corner edge modes

*Provenance.* Chandrasekaran-Flanagan 2026, eq (1.7b)

*Status.* L_l mu = Theta mu, so P_alpha is PROPORTIONAL TO Theta and VANISHES on a non-expanding horizon. the two-sided term is second order in the same quantity.

### F4

**A_beta = (1/8 pi) [ INTEGRAL_{S_0^+} beta mu - INTEGRAL_infinity beta mu ]**

*Hypotheses.* as F3

*Provenance.* Chandrasekaran-Flanagan eq (1.7a)

*Status.* the area operator, conjugate to boosts

### F5

**{ P_alpha, O(p) } = -alpha e^{Gamma_0^+} L_l O(p)**

*Hypotheses.* O(p) a gravitationally dressed observable

*Provenance.* Chandrasekaran-Flanagan eq (1.9a)

*Status.* the dressing is what makes the corner charges act non-trivially

### F6

**C2:  Delta_{M(u1)}^{it} M(u2) Delta_{M(u1)}^{-it} subset M(u2),  t <= 0,  u1 < u2**

*Hypotheses.* N a non-expanding horizon with no Killing field, omega Hadamard, M(u) the algebra of N_{>u}

*Provenance.* the open condition

*Status.* OPEN. two nearby forms are wrong: SSA saturation as written is unsayable in type III; sigma_t(N) = N for all t is too strong (Takesaki: it gives a conditional expectation, which type III_1 factors do not admit, and it makes P = 0).

### F7

**d - 1 = 1 + (d - 2)**

*Hypotheses.* a null hypersurface in d dimensions

*Provenance.* the dimensional ledger

*Status.* the 1 comes from one HSMI per generator; the (d-2) from the transverse direct integral, which NO half-sided modular inclusion supplies. the two open pieces are dimensionally distinct.


---

## Appendix B · References

**Access grades.** **[F]** full text read. **[A]** abstract or published summary. **[S]** secondary. **[B]** blocked.

### B.1 Constraint satisfaction, consistency and closure

- Freuder, E. C. (1982). A sufficient condition for backtrack-free search. *JACM* 29(1), 24–32. **[S]**
- Montanari, U. (1974). Networks of constraints. *Information Sciences* 7, 95–132. **[S]**
- Mackworth, A. K. (1977). Consistency in networks of relations. *Artificial Intelligence* 8(1), 99–118. **[S]**
- Dechter, R. (1992). From local to global consistency. *Artificial Intelligence* 55(1), 87–107. **[S]**
- van Beek, P. & Dechter, R. (1995). On the minimality and global consistency of row-convex constraint networks. *JACM* 42(3), 543–561. **[S]**
- van Beek, P. & Dechter, R. (1997). Constraint tightness and looseness versus local and global consistency. *JACM* 44(4), 549–566. **[S]**
- Jeavons, P., Cohen, D. & Cooper, M. C. (1998). Constraints, consistency and closure. *Artificial Intelligence* 101(1–2), 251–265. **[S]**
- Cooper, M. C., Jeavons, P. G. & Salamon, A. Z. (2010). Generalizing constraint satisfaction on trees. *Artificial Intelligence* 174, 570–584. **[A]**
- Helly, E. (1923). Über Mengen konvexer Körper mit gemeinschaftlichen Punkten. *Jahresbericht der DMV* 32, 175–176. **[S]**

### B.2 Atomic structure and statistics

- Racah, G. (1943). Theory of complex spectra III. *Physical Review* 63, 367–382. **[S]**
- Condon, E. U. & Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge. **[S]**
- Janet, C. (1929). The left-step periodic table. **[S]**
- Greenberg, O. W. (1993). (Para)bosons, (para)fermions, quons and other beasts in the menagerie of particle statistics. hep-ph/9306225. **[F]**
- Greenberg, O. W. (1997). Spin-statistics, spin-locality, and TCP: three distinct theorems. hep-th/9707220. **[F]**
- Lüders, G. & Zumino, B. (1958). Connection between spin and statistics. *Physical Review* 110, 1450. **[S]**
- Bernabéu, J. et al. (VIP collaboration) (2006). An experiment to search for a violation of the Pauli exclusion principle. quant-ph/0608088. **[F]**

### B.3 Energy conditions and wormholes

- Buniy, R. V., Hsu, S. D. H. & Murray, B. M. (2006). The null energy condition and instability. *PRD* 74, 063518. **[F]**
- Creminelli, P., Luty, M. A., Nicolis, A. & Senatore, L. (2006). Starting the universe: stable violation of the null energy condition and non-standard cosmologies. *JHEP* 12, 080. **[F]**
- Arkani-Hamed, N., Cheng, H.-C., Luty, M. A. & Mukohyama, S. (2004). Ghost condensation and a consistent infrared modification of gravity. *JHEP* 05, 074. **[S]**
- Cheng, H.-C., Luty, M. A., Mukohyama, S. & Thaler, J. (2006). Spontaneous Lorentz breaking at high energies. *JHEP* 05, 076. **[A]**
- Feldstein, B. (2009). Spontaneous Lorentz violation, negative energy and the second law of thermodynamics. arXiv:0904.1212. **[A]**
- Visser, M., Kar, S. & Dadhich, N. (2003). Traversable wormholes with arbitrarily small energy condition violations. *PRL* 90, 201102. **[A]**
- Fewster, C. J. & Roman, T. A. (2005). On wormholes with arbitrarily small quantities of exotic matter. *PRD* 72, 044023. **[F]**
- Ford, L. H. & Roman, T. A. (1996). Quantum field theory constrains traversable wormhole geometries. *PRD* 53, 5496–5507. **[S]**
- Morris, M. S. & Thorne, K. S. (1988). Wormholes in spacetime. *AJP* 56, 395–412. **[S]**
- Maldacena, J., Milekhin, A. & Popov, F. (2018). Traversable wormholes in four dimensions. arXiv:1807.04726; *CQG* 40, 155016 (2023). **[F]**
- Kontou, E.-A. & Sanders, K. (2020). Energy conditions in general relativity and quantum field theory. *CQG* 37, 193001. **[F]**
- Kontou, E.-A. (2024). Wormhole restrictions from quantum energy inequalities. *Universe* 10, 291. **[F]**
- Graham, N. & Olum, K. D. (2007). Achronal averaged null energy condition. *PRD* 76, 064001. **[F]**
- Kontou, E.-A. & Olum, K. D. (2015). Proof of the ANEC in a classical curved spacetime using a null-projected quantum inequality. arXiv:1507.00297. **[F]**
- Kelly, W. R. & Wall, A. C. (2014). Holographic proof of the averaged null energy condition. *PRD* 90, 106003. **[A]**
- Hartman, T., Kundu, S. & Tajdini, A. (2017). Averaged null energy condition from causality. *JHEP* 07, 066. **[F]**
- Faulkner, T., Leigh, R. G., Parrikar, O. & Wang, H. (2016). Modular Hamiltonians for deformed half-spaces and the ANEC. *JHEP* 09, 038. **[S]**
- Wall, A. C. (2010). Proving the achronal ANEC from the generalized second law. arXiv:0910.5751. **[F]**
- Ishibashi, A., Maeda, K. & Mefford, E. (2019). Achronal ANEC, weak cosmic censorship, and AdS/CFT duality. *PRD* 100, 066008. **[F]**
- Iizuka, N., Ishibashi, A. & Maeda, K. (2020). Conformally invariant averaged null energy condition from AdS/CFT. *JHEP* 03, 161. **[A]**
- Iizuka, N., Ishibashi, A. & Maeda, K. (2020). The averaged null energy conditions in even dimensional curved spacetimes from AdS/CFT duality. *JHEP* 10, 106; arXiv:2008.07942. **[F]**
- Urban, D. & Olum, K. D. (2010). ANEC violation in a conformally flat spacetime. *PRD* 81, 024039. **[A]**
- Visser, M. (1994). Scale anomalies imply violation of the averaged null energy condition. gr-qc/9409043. **[A]**
- Ceyhan, F. & Faulkner, T. (2018). Recovering the QNEC from the ANEC. arXiv:1812.04683. **[A]**
- Balakrishnan, S., Faulkner, T., Khandker, Z. U. & Wang, H. (2019). A general proof of the quantum null energy condition. *JHEP* 09, 020. **[A]**
- Kudler-Flam, J., Leutheusser, S., Rahman, A. A., Satishchandran, G. & Speranza, A. J. (2025). Covariant regulator for entanglement entropy: proofs of the Bekenstein bound and the quantum null energy condition. *PRD* 111, 105001; arXiv:2312.07646. **[F]**
- Freivogel, B., Kontou, E.-A. & Krommydas, D. (2020). The return of the singularities: applications of the smeared null energy condition. arXiv:2012.11569. **[A]**
- Alcubierre, M. (1994). The warp drive. *CQG* 11, L73–L77. **[S]**
- Bobrick, A. & Martire, G. (2021). Introducing physical warp drives. *CQG* 38, 105009. **[F]**

### B.4 Causal structure, chronology and Lorentz violation

- Penrose, R. (1965). Gravitational collapse and space-time singularities. *PRL* 14, 57–59. **[S]**
- Landsman, K. (2022). Penrose's 1965 singularity theorem. *GRG* 54, 115. **[F]**
- Hawking, S. W. (1992). Chronology protection conjecture. *PRD* 46, 603–611. **[S]**
- Gao, S. & Wald, R. M. (2000). Theorems on gravitational time delay and related issues. *CQG* 17, 4999. **[S]**
- Friedman, J. L. (2004). The Cauchy problem on spacetimes that are not globally hyperbolic. gr-qc/0401004. **[F]**
- Hořava, P. (2009). Quantum gravity at a Lifshitz point. *PRD* 79, 084008. **[S]**
- Jacobson, T. & Mattingly, D. (2001). Gravity with a dynamical preferred frame. *PRD* 64, 024028. **[S]**
- Berglund, P., Bhattacharyya, J. & Mattingly, D. (2013). Towards thermodynamics of universal horizons in Einstein-aether theory. *PRL* 110, 071301. **[F]**
- Colladay, D. & Kostelecký, V. A. (1998). Lorentz-violating extension of the standard model. *PRD* 58, 116002. **[F]**
- Greenberg, O. W. (2002). CPT violation implies violation of Lorentz invariance. *PRL* 89, 231602. **[S]**

### B.5 Quantum foundations

- Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics* 1, 195–200. **[S]**
- Tsirelson, B. S. (1980). Quantum generalizations of Bell's inequality. *LMP* 4, 93–100. **[S]**
- Popescu, S. & Rohrlich, D. (1994). Quantum nonlocality as an axiom. *Foundations of Physics* 24, 379–385. **[S]**
- Pawłowski, M. et al. (2009). Information causality as a physical principle. *Nature* 461, 1101–1104. **[A]**
- Wootters, W. K. & Zurek, W. H. (1982). A single quantum cannot be cloned. *Nature* 299, 802–803. **[S]**
- Weinberg, S. (1989). Testing quantum mechanics. *Annals of Physics* 194, 336. **[S]**
- Polchinski, J. (1991). Weinberg's nonlinear quantum mechanics and the EPR paradox. *PRL* 66, 397–400. **[A]**
- Abrams, D. S. & Lloyd, S. (1998). Nonlinear quantum mechanics implies polynomial-time solution for NP-complete and #P problems. *PRL* 81, 3992–3995. **[F]**
- Simon, C., Bužek, V. & Gisin, N. (2001). No-signaling condition and quantum dynamics. *PRL* 87, 170405. **[A]**
- Soulas, A. (2025). A proof that no-signalling implies microcausality in QFT. *Foundations of Physics* 55, 22. **[A]**
- Sorkin, R. D. (1993). Impossible measurements on quantum fields. *Directions in General Relativity* vol. 2. **[S]**
- Rastegin, A. E. (2009). A note on general no-cloning theorem for black boxes. arXiv:0908.1668. **[F]**
- Sbisà, F. (2015). Classical and quantum ghosts. *European Journal of Physics* 36, 015009; arXiv:1406.4550. **[A]**

### B.6 Closed timelike curves in quantum theory

- Deutsch, D. (1991). Quantum mechanics near closed timelike lines. *PRD* 44, 3197–3217. **[S]**
- Lloyd, S. et al. (2011). Closed timelike curves via postselection. *PRL* 106, 040403. **[F]**
- Brun, T. A., Harrington, J. & Wilde, M. M. (2009). Localized CTCs can perfectly distinguish quantum states. *PRL* 102, 210402. **[S]**
- Bennett, C. H., Leung, D., Smith, G. & Smolin, J. A. (2009). Can CTCs or nonlinear QM improve quantum state discrimination? *PRL* 103, 170502. **[A]**
- Oreshkov, O., Costa, F. & Brukner, Č. (2012). Quantum correlations with no causal order. *Nature Communications* 3, 1092. **[S]**

### B.7 Black hole thermodynamics and unitarity

- Banks, T., Susskind, L. & Peskin, M. E. (1984). Difficulties for the evolution of pure states into mixed states. *Nuclear Physics B* 244(1), 125–134. **[A]**
- Nikolić, H. (2015). Violation of unitarity by Hawking radiation does not violate energy-momentum conservation. *JCAP* 04, 002. **[A]**
- Dubovsky, S. L. & Sibiryakov, S. M. (2006). Spontaneous breaking of Lorentz invariance, black holes and perpetuum mobile of the 2nd kind. *PLB* 638, 509–514. **[F]**
- Eling, C., Foster, B. Z., Jacobson, T. & Wall, A. C. (2007). Lorentz violation and perpetual motion. *PRD* 75, 101502(R). **[F]**
- Wall, A. C. (2012). A proof of the generalized second law for rapidly changing fields and arbitrary horizon slices. *CQG* 30, 165003. **[A]**
- Casini, H. (2008). Relative entropy and the Bekenstein bound. *CQG* 25, 205021. **[S]**
- Witten, E. (2022). Gravity and the crossed product. *JHEP* 2022, 8. **[S]**

### B.8 Measurements

- Abbott, B. P. et al. (2017). GW170817 and GRB 170817A. *ApJL* 848, L13. **[S]**
- Touboul, P. et al. (2022). MICROSCOPE final results. *PRL* 129, 121102. **[S]**
- Lamoreaux, S. K. (1997). Demonstration of the Casimir force in the 0.6 to 6 µm range. *PRL* 78, 5–8. **[S]**
- Hensen, B. et al. (2015). Loophole-free Bell inequality violation. *Nature* 526, 682–686. **[S]**

---

## Appendix C · Verification

Twenty-six numerical claims were re-audited against fresh computation with zero failures. Two propositions replaced
sampled claims with proofs (1.2 and 4.3). One error was found inside a correction — a parameter used with two
meanings in the same computation — caught only because the fermionic case failed to reproduce 13,585.

The document runs against twenty-one structural audits covering lattice properties, equation reproduction, internal
consistency, undefined terms, encoding artefacts, coherence, attribution, figure coverage, distinctness, scoping,
antecedents, markup, dataset agreement, arithmetic, enumeration, fidelity, artifact measure, reproducibility,
sequence, projection and input.

**Audit 22 — term match — is external by construction and cannot join them.** Its output is the vocabulary debt:
**32 of 48 pairs unchecked.** That number, not the twenty-one passes, is what tells a
reader how far to trust the rest.

All figures are computed from cached datasets. The computation scripts, datasets, build script and audit script
accompany this paper.

