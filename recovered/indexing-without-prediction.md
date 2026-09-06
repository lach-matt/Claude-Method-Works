# Indexing Without Prediction

## Maximality and Empirical Boundary of the Lach Elemental Lattice

---

**Status of this draft.** Prepared for independent review. Every numerical claim
below was computed during the development of this work and is reproducible from
the data sources cited in Appendix C. Section 15 lists claims made in earlier
versions of this framework that are withdrawn. Readers checking this work are
asked to attack Section 6.4 and Section 4.2 first; those are the two places
where the argument is thinnest and the authors know it.

---

## Abstract

We construct a lattice Λ₈ over atomic electron configurations, prove it maximal
in a precise sense, and establish empirically that its order structure supplies
no predictive information beyond the coordinates from which it is built.

Λ₈ is a closed distributive lattice of order dimension exactly eight, generated
by an admissibility condition requiring every constraint to take the form
*x ≤ φ(y)* with φ non-decreasing in a single coordinate and a constant floor.
We prove that no further axis can be *derived* from the eight electronic
coordinates: any function whose graph preserves closure must be a monotone
function of a single coordinate, hence redundant. The lattice is nonetheless
extensible by *independent* physical quantities — the parent ion's total angular
momentum, the total atomic angular momentum, the jK intermediate label, nuclear
spin — each contributing exactly one dimension. Λ₁₁ so constructed is injective
on every test case we have assembled.

Against this we set an empirical result of the opposite sign. A bracketing
method for Rydberg binding energies, derived entirely from *T = Z*²*R*/ν² and
using none of the lattice's order structure, produces containment intervals that
hold in 295 of 295 interior cells across hydrogen, four alkaline earths, three
alkali-like ions and a noble gas, spanning Z_eff = 1–3, ℓ = 0–5, single-, two-
and multi-limit systems, and both bound and autoionising regimes. Its
uncertainty estimate is derived rather than calibrated and returns ±1σ coverage
of 68.1%, 68.2% and 76.7% in the three limit regimes.

Six independent attempts to extract predictive uplift from the lattice's order —
rank aggregation, comparability, zero-shot subset selection, closure-as-existence,
join-based configuration mixing, and a derived ordinal coordinate — all failed,
each by a distinct and identifiable mechanism. We show these reduce to a single
theorem: on a product order, join, meet and comparability are definable from the
coordinates, so lattice quantities can restate the coordinates but never exceed
them. This theorem is indifferent to dimension and to how faithfully the lattice
represents the physics. Perfecting the index does not move the predictive
boundary.

The one thing that escapes the theorem is deductive containment, because a
bracket is not a function of the coordinates: it is an entailment of the order
relation given monotonicity. That is the sense in which an ordinal structure over
configuration space is useful, and the only sense we have been able to verify.

---

# Part 0 — Origin and Orientation

## 1. Introduction

### 1.1 Where this began

This framework began as a three-dimensional recoding of the periodic table. Each
element was assigned a triple (*n*, ℓ, *k*): the principal quantum number of the
subshell being filled, its orbital angular momentum, and the occupancy of that
subshell. Under the componentwise partial order, the set of such triples forms a
lattice, and the periodic table becomes a path through it.

The recoding is exact and it is not new physics — it is a bijective relabelling
of information already present in the Madelung filling order. Its interest was
pedagogical and structural: the periodic table's periodicity appears as a
projection of a three-dimensional object, and elements that are chemically
analogous are close in the lattice for a structural reason rather than by
convention.

Three subsequent additions produced the object studied here. Excited
configurations required distinguishing the subshell an electron *leaves* from
the one it *enters*, giving a second triple (*e*, *f*, *g*) — target shell,
target subshell, and number of electrons transferred. Ionisation required a
count *q* of electrons removed from the source. Spin multiplicity required a
coordinate *S*. The result is Λ₈, an eight-dimensional lattice whose cells index
electron configurations relative to a reference state.

The framework's earlier claims concerned prediction: that the lattice's order,
closure and dimension would constrain atomic properties in ways the coordinates
alone did not. This paper reports that those claims are false, establishes why
in a form we believe is a theorem rather than a limitation of effort, and
reports what survives.

### 1.2 What this paper claims

**Structural (Part I).** Λ₈ is closed under join and meet, has order dimension
exactly eight, and is maximal under derivation. It extends by one dimension per
independent physical degree of freedom. As an index of atomic energy levels it
achieves 86% coverage and, at eleven dimensions, injectivity on every test case.
The physical subset of the lattice is *not* a sublattice, and no choice of
coordinates makes it one.

**Empirical (Part II).** A four-rule bracketing method for Rydberg binding
energies, each rule derived from the definition *T = Z*²*R*/ν², produces
deductive containment verified on 295 interior cells with no exceptions, and an
uncertainty estimate that requires no calibration. Its domain is bounded by four
exclusions, each with an identified mechanism.

**Thesis (Part III).** The lattice's order structure contributes nothing to the
method. Six independent tests establish this, and a theorem about product orders
explains why. The theorem does not depend on the lattice's dimension or on how
faithfully it represents the physics, so improving the index — which we do in
Part I — leaves the predictive boundary exactly where it was.

### 1.3 What this paper does not claim

We do not claim novel physics. Every quantitative result in Part II is a
consequence of the Rydberg formula and the quantum defect; the lattice's role is
to make "interior on some axis" and "same channel" well defined. We do not claim
the method extends to properties other than energies; Section 11 reports two
attempts and both failed, for reasons we characterise. We do not claim the
maximality theorem in full generality; Section 4.2 states precisely the
hypothesis we have proven and the one we have only verified.

An earlier line of this work concerned applications to condensed-matter nuclear
phenomena. That material is removed entirely from this paper. It rested on
extensions of Λ₈ whose structural status we now know to be defective
(Appendix A), and revisiting it requires first resolving the multi-target
representation problem.

---

# Part I — Structure

## 2. Construction

### 2.1 The admissibility condition

Let Λ be a subset of ℕ^d defined by a family of constraints. We call the family
**admissible** — the condition previously designated §9.4 — if every constraint
has the form

> *x_i* ≤ φ(*x_j*)  with φ non-decreasing, together with a constant floor
> *x_i* ≥ *c*.

**Proposition 2.1.** *An admissible constraint family defines a set closed under
componentwise join and meet.*

*Proof.* Let *a*, *b* ∈ Λ and consider *x_i* ≤ φ(*x_j*). For the join,
max(*a_i*, *b_i*) = *a_i* or *b_i*; say *a_i*. Then *a_i* ≤ φ(*a_j*) ≤
φ(max(*a_j*, *b_j*)) since φ is non-decreasing. For the meet,
min(*a_i*, *b_i*) ≤ *a_i* ≤ φ(*a_j*), and we require ≤ φ(min(*a_j*, *b_j*)).
Choose the index *m* ∈ {*a*, *b*} minimising *x_j*. Then min(*a_i*, *b_i*) ≤
*m_i* ≤ φ(*m_j*) = φ(min(*a_j*, *b_j*)). A constant floor is preserved by both
operations trivially. ∎

Two consequences shape everything that follows. A bound on a **sum** of two
coordinates is not of admissible form, and generally breaks closure — this is
what defeats the multi-target extension of Appendix A. A **varying floor** is
likewise inadmissible, and this is what places the physical selection rules
outside the language (Section 6.3).

### 2.2 The eight axes

| axis | meaning | bound | form |
|---|---|---|---|
| *n* | source shell | 1 ≤ *n* ≤ *N* | free root |
| ℓ | source subshell | ℓ ≤ *n* − 1 | non-decr. in *n* |
| *k* | source occupancy | 1 ≤ *k* ≤ 2(2ℓ+1) | non-decr. in ℓ |
| *q* | electrons removed | 0 ≤ *q* ≤ *k* | non-decr. in *k* |
| *e* | target shell | 1 ≤ *e* ≤ *E* | free root |
| *f* | target subshell | *f* ≤ *e* − 1 | non-decr. in *e* |
| *g* | electrons transferred | *g* ≤ min(*q*, 2(2*f*+1)) | min of two admissible |
| 2*S* | spin multiplicity | 0 ≤ 2*S* ≤ *k* | non-decr. in *k* |

Derived quantities include the net charge *c* = *q* − *g*, the electron count
*N* = C(*n*,ℓ) + *k* − *c*, and the target occupancy *G*. **These are derived
precisely because they cannot be coordinates**: each is a difference or sum of
two axes, hence not of admissible form. Section 4.3 makes this exact.

### 2.3 Closure and dimension

Closure follows from Proposition 2.1 and was additionally verified on 8 × 10⁶
sampled pairs at caps covering the observed data (*n* ≤ 6, ℓ ≤ 3, *e* ≤ 62,
*f* ≤ 3), with zero failures.

**Order dimension is exactly eight.** The upper bound is immediate: Λ₈ ⊆ ℕ⁸.
The lower bound follows from an explicit 8-box at

> (*n*, ℓ, *k*, *q*, *e*, *f*, *g*, 2*S*) = (3, 1, 2, 1, 2, 0, 0, 0)

all 2⁸ = 256 corners of which are admissible. The box is **cap-independent**: it
remains valid at cap settings (4,2,4,2), (6,3,8,3) and (8,4,12,4).

> **Figure 1.** The §9.4 constraint DAG. Nodes are axes; an edge *y* → *x*
> indicates *x* is bounded by φ(*y*). Two roots, *n* and *e*; the graph is a
> forest, not a chain. Reproduces the dependency structure that determines which
> axes can be independently varied.

> **Figure 2.** Projection of the 8-box onto three coordinate triples, showing
> all 256 corners present. Demonstrates dimension 8 visually.

### 2.4 A note on cell counts

Earlier versions of this framework reported |Λ₈| = 61,453 as a structural
invariant. It is not. That figure is the cell count at one particular choice of
caps (*n* ≤ 4, ℓ ≤ 2, *e* ≤ 5, *f* ≤ 2), and it changes with them. Every
quantity derived from it — the fraction of cells representing inward
transitions, the fraction "realisable" — is likewise a truncation artefact and
is withdrawn. The invariants of Λ₈ are its closure, its order dimension, and its
maximality; its cardinality is not among them.

## 3. Algebra and geometry, axis by axis

Each axis has an *algebra* — the bound that defines it and its admissible form —
and a *geometry* — the shape of the region it occupies. This section also
reports, for each axis, where it is actually exercised, which turns out to vary
enormously.

**3.1 *n*, the source shell.** Algebra: a free root; every electronic bound
descends from it. Geometry: a chain, 1 to *N*. Exercised: distinguishes species,
but is **constant within any one atom**. In the axis-ablation study (§3.10),
removing *n* from the index of a single species costs zero collisions.

**3.2 ℓ, the source subshell.** Algebra: ℓ ≤ *n* − 1, non-decreasing in *n*.
Geometry: a right triangle in the (*n*, ℓ) plane. Exercised: distinguishes
species and blocks; constant within an atom.

**3.3 *k*, the source occupancy.** Algebra: 1 ≤ *k* ≤ 2(2ℓ+1). Geometry: a
staircase whose width doubles-and-adds-four with ℓ — 2, 6, 10, 14. Exercised:
constant within an atom. *k* is the coordinate that bounds *q*, 2*S*, and (in
Λ₉ and above) the angular momentum axes, so it is structurally central while
being empirically inert within a species.

**3.4 *q*, electrons removed.** Algebra: 0 ≤ *q* ≤ *k*, a triangle nested inside
*k*. Geometry: for each *k*, a chain of length *k*+1. Exercised: separates
neutral from ionised species. Constant (*q* = 1) across all singly-excited
states of one atom.

**3.5 *e*, the target shell.** Algebra: a second free root. Geometry: a chain.
Exercised: **this is the workhorse.** Removing *e* from the Ca I index costs 13
collisions in 27 levels; from Kr I, 22 in 46. It is the axis the bracketing
method of Part II interpolates along, and the only axis that is load-bearing
both across and within species.

**3.6 *f*, the target subshell.** Algebra: *f* ≤ *e* − 1, a second right
triangle independent of the (*n*, ℓ) one. Geometry: the Λ₈ region is therefore a
product of two triangles, not a single simplex — this is the clearest sense in
which the lattice is not merely a relabelled periodic table. Exercised: 7
collisions on removal for Ca I, 22 for Kr I. Load-bearing.

**3.7 *g*, electrons transferred.** Algebra: *g* ≤ min(*q*, 2(2*f*+1)) — the
intersection of two triangles, a wedge. Geometry: the only axis bounded by two
others simultaneously. Exercised: **zero collisions on removal.** For
singly-excited states *g* = *q* = 1 universally, so the axis is exercised only by
doubly-excited configurations, of which the observational record contains few.

**3.8 2*S*, spin.** Algebra: 0 ≤ 2*S* ≤ *k*. Geometry: a chain over *k*.
Exercised: 5 collisions on removal for Ca I. Load-bearing where LS coupling
holds; **undefined** for jK-coupled systems such as Kr I, where the paper must
substitute the parent's *J*.

**3.9 The collective whole.** Λ₈ is a product of two triangular regions —
(*n*, ℓ) and (*e*, *f*) — with occupancy chains hung from each, and a wedge
(*g*) linking them. It is *not* a simplex, *not* a hypercube, and *not* a chain
product; the two roots make it a forest-shaped constraint graph with a single
cross-link. The simplest complete picture is Figure 3.

> **Figure 3.** Λ₈ decomposed: the (*n*, ℓ, *k*) source block, the
> (*e*, *f*, *g*) target block, the *q* chain joining them, and the 2*S* chain.
> Arrows show the §9.4 dependencies. One cross-link only: *g* depends on both
> *q* and *f*.

**3.10 Axis ablation.** Removing each axis in turn from the index and counting
collisions gives a direct measurement of what each contributes.

| axis | Ca I (27 levels) | Kr I (46 levels) |
|---|---|---|
| *n*, ℓ, *k*, *q*, *g* | 0 collisions | 0 collisions |
| *e* | **13** | **22** |
| *f* | **7** | **22** |
| 2*S* | **5** | undefined |
| 2*J*_c | 0 (fixed) | **20** |
| 2*J* | **12** | **35** |

Six of ten coordinates are constant within a species and discriminate only
*across* species. Only *e* and *f* appear in both roles — which is precisely why
the method of Part II interpolates in *e* at fixed *f* and uses no other axis.

> **Figure 4.** Ablation bar chart, Ca I and Kr I side by side.

## 4. Maximality under derivation

### 4.1 The theorem

**Theorem 4.1.** *Let L be a product of finite chains and h : L → ℤ a function
whose graph {(x, h(x))} is closed under componentwise join and meet. Then h is a
monotone function of a single coordinate.*

*Proof.* Closure requires *h*(*x* ∨ *y*) = max(*h*(*x*), *h*(*y*)) and
*h*(*x* ∧ *y*) = min(*h*(*x*), *h*(*y*)); in particular *h* is monotone. Each
sublevel set *h*⁻¹(≤*v*) is then a down-set closed under join, hence — *L* being
finite — principal: *h*⁻¹(≤*v*) = ↓*m_v* for some *m_v*, and *m*₀ ≤ *m*₁ ≤ ⋯

Suppose *m_v* and *m*_{*v*+1} differ in two coordinates *i* ≠ *j*. Put
*x* = *m_v* + *e_i* and *y* = *m_v* + *e_j*. Both lie below *m*_{*v*+1} and
neither below *m_v*, so *h*(*x*) = *h*(*y*) = *v*+1. But *x* ∧ *y* = *m_v*,
which has *h* ≤ *v*, contradicting the meet rule. Hence consecutive *m* differ
in exactly one coordinate.

Suppose further that *m*₁ = *m*₀ + *e_i* and *m*₂ = *m*₁ + *e_j* with *i* ≠ *j*.
Put *x* = *m*₀ + *e_j*, so *h*(*x*) = 2, and *y* = *m*₁, so *h*(*y*) = 1. Then
*x* ∧ *y* = *m*₀ with *h* = 0, while the meet rule demands
min(2, 1) = 1. Contradiction. So all increments use the same coordinate, and
*h* is a monotone function of that coordinate alone. ∎

**Corollary 4.2.** *No ninth axis derived from the eight electronic coordinates
can be adjoined to Λ₈ while preserving closure and raising the dimension.* Any
such axis is either inadmissible or, being a monotone relabelling of a single
existing coordinate, order-redundant.

**Exhaustive verification.** Over all monotone *h* into a three-valued chain:
17 of 17 closure-preserving functions on a 3 × 3 product depend on at most one
coordinate; 12 of 12 on 2 × 2 × 2. No counterexamples.

### 4.2 The caveat, stated plainly

Λ₈ is a **sublattice** of a product of chains, not a full product. The proof's
step "*m_v* + *e_i* ∈ *L*" requires that incrementing a single coordinate stays
inside *L*, and Λ₈ is not interval-closed: (1, 2) violates ℓ ≤ *n* − 1 while
lying componentwise between (1, 0) and (3, 2).

**Theorem 4.1 is therefore proven for products of chains and verified but not
proven for Λ₈.** Every candidate we have tested on Λ₈ behaves as the theorem
predicts, and we know of no counterexample; we do not have a proof. A reviewer
looking for the weakest link in Part I should look here.

### 4.3 Rejected candidates

Each of the following was proposed as a ninth axis in earlier work and each
fails, with the failure now attributable to Theorem 4.1 rather than to
case-by-case testing.

| candidate | form | join fail | meet fail | verdict |
|---|---|---|---|---|
| *h* = *n* | projection | 0 | 0 | closed but redundant, no 9-box |
| *h* = 2*n* | monotone in *n* | 0 | 0 | closed but redundant |
| *h* = *n* + ℓ | two coordinates | 42,492 | 42,492 | breaks closure |
| *h* = *q* − *g* (net charge *c*) | difference | 284,858 | 284,858 | breaks closure |
| *h* = *k* − *q* | difference | 406,400 | 406,400 | breaks closure |
| *h* = *e* − *f* | difference | 266,440 | 266,440 | breaks closure |
| *h* = ⌊*C*/*e*²⌋ (energy proxy) | anti-monotone | 503,404 | 503,404 | breaks closure |

The energy proxy deserves separate comment because it was the original
motivation for a ninth "output" axis. It fails for a reason sharper than
inadmissibility: energy *decreases* with *e* while the order *increases*, so an
energy-valued coordinate is anti-monotone and pairs of cells acquire no upper
bound at all. **A metric quantity that increased with the coordinates might well
be admissible.** The obstruction is the sign, not the metricity — a correction
to the earlier §22.2 analysis.

## 5. Extension by independent quantities

### 5.1 Three classes

Theorem 4.1 constrains only *functions of the existing coordinates*. Quantities
that are physically independent escape it. Candidates fall into three classes:

- **(a) Functions of existing coordinates.** Inadmissible unless monotone in a
  single coordinate, in which case redundant. Theorem 4.1.
- **(b) Independent, bounded by an existing coordinate.** Admissible if and only
  if the bound has §9.4 form. Contributes exactly one dimension.
- **(c) Independent, bounded by a constant.** The admissible set is a direct
  product; closure is automatic; contributes one dimension.

### 5.2 Λ₉, Λ₁₀, Λ₁₁

**Parent-ion angular momentum (class b).** The same electronic cell can leave
the residual ion in different *J* states, so *J*_c is not a function of the
eight. With the bound 2*J*_c ≤ *k* — non-decreasing in a single coordinate — the
enlarged set is **closed exactly**: 6,989 cells, all 24,419,566 pairs tested,
zero failures. A 9-box exists at (3,1,5,4,3,1,3,2,1). **Order dimension 9.**

**Total atomic angular momentum (class b).** With 2*J* ≤ 2*k*, closure holds on
2,041,470 cells with zero failures and a 10-box at (3,1,2,1,2,0,0,0,0,0).
**Order dimension 10.**

**jK intermediate label (class b).** Required for jK-coupled systems; bounded
loosely by 2*K* ≤ 2*k*.

**Nuclear spin (class c).** Bounded by a constant; the set is a direct product;
closure automatic.

### 5.3 What extension buys and costs

| lattice | Kr I core-*J* collisions | Ca I fine-structure collisions |
|---|---|---|
| Λ₈ | 3 (of 3 cells) | 1 |
| Λ₉ | **0** | 1 |
| Λ₁₀ | 0 | **0** |
| Λ₁₁ | 0 | 0 |

On a 46-level Kr I test set: Λ₈ gives 7 cells with 39 collisions; Λ₉, 11 cells
with 35; Λ₁₀, 34 cells with 12; **Λ₁₁, 46 cells with 0**.

The cost is looseness. Each class-(b) bound admits more than the physics
requires: the true range for total *J* is the triangle rule
|*J*_c − *j*| ≤ *J* ≤ *J*_c + *j*, whose **lower bound varies with the cell**,
and §9.4 permits only constant floors. Measured on a bounded enumeration, the
physically realisable fraction is 23.3% at eight dimensions, 9.0% at nine, 1.7%
at ten.

> **Figure 5.** Collisions cleared against dimension, with the physical fraction
> on a second axis — the two curves crossing is the trade.

## 6. The lattice as an index

### 6.1 Coverage

For each species we map observed configurations to Λ cells and count how many
map at all.

| species | mapped | coverage |
|---|---|---|
| Kr I | 9/9 | 100% |
| Sc III | 8/8 | 100% |
| Ba II | 10/10 | 100% |
| Sr I | 9/10 | 90% |
| Ca I | 12/15 | 80% |
| Ti I | 6/11 | 55% |
| **total** | **54/63** | **86%** |

Every failure is a **multi-subshell configuration** — two occupied non-source
subshells, which a single (*e*, *f*, *g*) triple cannot name. Coverage is a
representational limit and **no additional coordinate repairs it**; the natural
repair, a second target triple, breaks the lattice (Appendix A).

### 6.2 Injectivity

Three collision types, each cleared by a specific axis:

| type | example | resolved by | at |
|---|---|---|---|
| core *J* | Kr I (²P°₃⁄₂)5s vs (²P°₁⁄₂)5s | 2*J*_c | Λ₉ |
| fine structure | Ca I 4s4d ³D₁,₂,₃ | 2*J* | Λ₁₀ |
| jK label | Kr I 5p ²[1/2] vs ²[3/2], same *J* | *K* | Λ₁₁ |

The first is consequential beyond bookkeeping. The two Kr I channels converge on
limits **5,370 cm⁻¹ apart**, and the method of Part II requires knowing which.
**Λ₈ cannot supply that assignment**; in the work reported here it was read from
the ASD configuration string. Λ₉ supplies it.

### 6.3 The physical set is not a sublattice

The physically realisable cells of Λ₈ are those satisfying the spin selection
rules: 2*S* ≡ *k* (mod 2), and 2*S* ≤ min(*k*, 2(2ℓ+1) − *k*).

**This set is not closed.** In the (*k*, 2*S*) plane, (1,1) and (2,0) are both
physical; their join (2,1) is not, because 2*S* must be even when *k* is even.
Failures: 1 at ℓ = 0, 15 at ℓ = 1, 70 at ℓ = 2.

The obstruction is structural. A **congruence** is not an inequality, and §9.4
admits only inequalities with constant floors. The selection rules of atomic
physics — spin parity, hole symmetry, the triangle rule — are none of them of
that form.

### 6.4 Offset coordinates: faithful but not closed

*This section reports a negative result obtained late in the work and it
corrects an intermediate claim.*

One may attempt to bring the selection rules inside the language by
reparameterisation. Replace 2*S* by the paired-unit count *m* = (*k* − 2*S*)/2,
so that 2*S* = *k* − 2*m* carries the parity of *k* automatically; replace 2*J*
by the triangle offset *t* = (2*J* − |2*J*_c − 2*j*|)/2, so that the triangle
rule is satisfied by construction. Each transformation is bijective, so the
dimension is unchanged and Theorem 4.1 is untouched.

Tested **in isolation**, each works: the (*k*, *m*) plane is closed at every ℓ,
and the (*J*_c, *j*, *t*) block is closed with 140 cells and zero failures.

**Assembled into one lattice, they do not.** Exhaustive test on 1,431 cells and
all 1,023,165 pairs: **222,075 join failures and 11,696 meet failures.** The
cause is visible in the bounds: *m* has a floor that varies with *k*, and
2*J*_c ≤ *k* − *q* is *decreasing* in *q*. Both violate §9.4. Isolated closure
does not imply joint closure.

What the offset coordinates do achieve is worth recording. All 1,431 cells decode
to genuine physical states — zero violations — and the encoding is injective,
1,903 distinct states with no duplicates. **Offset coordinates are a faithful and
injective parameterisation of the physical set that is not a lattice.**

The conclusion, then, is unavoidable and should be stated as the section's
result: **one may have closure or faithfulness, not both.** The lattice properly
contains the physics; the physics is not a sublattice; and no relabelling
repairs this, because the obstruction is the varying floor and not the choice of
origin.

---

# Part II — A Bracketing Method for Rydberg Energies

## 7. Derivation

Every rule below follows from one expression:

> *T* = *Z*_eff² *R* / ν²,  ν = *n* − δ(*n*, ℓ, core)

where *T* is the binding energy of the outer electron relative to its series
limit and δ the quantum defect. The method uses the lattice only to make two
notions well defined: which cells belong to the same **channel** (fixed source,
fixed parent state, fixed *f*), and which cells are **interior** on an axis.

## 8. The four rules

> **Rule 1 — Interiority.** Predict only cells with measured neighbours on both
> sides along some axis, and only cells belonging to the same Rydberg sequence
> as those neighbours.
>
> **Rule 2 — Variable.** Read the interpolation variable off *T* = *Z*²*R*/ν²
> for the axis in question: *E* along *n* within a series; interval ratios along
> *J*; geometric in *T* along the core shell.
>
> **Rule 3 — Separation.** Report the deductive bracket separately from the
> inferential point estimate. Given monotonicity, the true value cannot lie
> outside [max below, min above].
>
> **Rule 4 — Uncertainty.** Fit δ locally by a Ritz expansion δ = δ₀ + δ₂/*n*²
> and take σ = 2*R Z*_eff² · SE_pred / ν³ from the fit's prediction standard
> error.

**Rule 1's second clause is not redundant.** Sc III 3d is interior in *n* within
ℓ = 2, yet including it inflates the median error by 3.2× because it is the
collapsed ground state rather than a sequence member. The operational test is
that its defect departs from its neighbours' by 0.14 where they depart from each
other by 0.008 — a factor of 17.

**Justification of each rule by ablation:**

| rule violated | cost |
|---|---|
| extrapolate rather than interpolate | rms 248 → 928 cm⁻¹ (3.7×), *n* = 91 |
| wrong interpolation variable | rms 248 → 589 cm⁻¹ (2.4×) |
| pooled σ instead of per-cell | ±1σ coverage 96.2% instead of 68% |
| include collapsed orbital | median error 12.8 → 41.3 cm⁻¹ (3.2×) |

## 9. Verification

**295 interior cells, bracket exact in every one.**

| regime | cells | bracket | ±1σ | median error |
|---|---|---|---|---|
| H I (*Z*_eff = 1) | 5 | 5/5 | — | **0.006 cm⁻¹** |
| Mg/Ca/Sr/Ba I, Ca/Sr/Ba II | 226 | 226/226 | 68.1% | 1.05 |
| Ca I 3d channel (autoionising) | 22 | 22/22 | 68.2% | 9.37 |
| Kr I (multi-limit p-block) | 30 | 30/30 | 76.7% | 3.54 |
| Sc III (*Z*_eff = 3) | 11 | 11/11 | 54.5% | 12.8 |

Spanning *Z*_eff = 1, 2, 3; ℓ = 0 through 5; single-, two- and multi-limit
systems; bound and autoionising states.

**On independence.** These 295 cells are drawn from approximately **22
channels**. Cells within a channel share neighbours, so successive brackets are
correlated and 295 should not be read as 295 independent tests. The honest
figure is 295 cells across 22 channels.

**On the bracket's robustness.** Perturbing the series limit by ±5 cm⁻¹ leaves
bracket coverage unchanged at 15/15 in a test case, because the bracket uses only
measured neighbours. The point estimate and σ require the limit; **the bracket
does not**. Similarly, "interior" requires that neighbours exist, not that they
be adjacent: with *n* = 8–16 removed from a Ba I series, cell 17 still brackets
correctly, at width 2,012 cm⁻¹ instead of 400.

**On the neighbour count.** The Ritz fit uses the *k* nearest members. Sensitivity:
rms 14.0 / 17.1 / 15.8 / 15.5 / 15.5 cm⁻¹ for *k* = 3, 4, 6, 8, 10. No strong
preference; *k* = 6 was chosen arbitrarily and the paper reports the sensitivity
rather than presenting it as derived.

> **Figure 6.** Defect sequences δ(*n*) for six channels across four species,
> showing the smooth Ritz behaviour on which Rule 4 rests.
>
> **Figure 7.** |error| against σ_pred, log–log, with ±1σ and ±2σ bands and the
> 68% / 95% reference lines. 295 points.
>
> **Figure 8.** The bracket construction, schematic: measured neighbours, the
> deductive interval, the inferential estimate with its σ.

## 10. Domain and exclusions

**Verified domain.** Binding energies of Rydberg series: one electron outside a
core in a definite state, channel by channel, with the channel's limit supplied
by the configuration label. Interior cells only, excluding collapsed orbitals.

**Four exclusions, each with a mechanism.**

**(i) Sign-changing quantities.** Any property built from a matrix element that
passes through zero cannot be monotone. Sr I 5s²¹S₀ → 5s*n*p ¹P₁ reduced
transition probabilities collapse by a **factor of 60** at *n* = 6 and recover —
a Cooper-type node. Bracket coverage across the node: 79%. Away from it: 100%
on 11 cells.

**(ii) Asymptotically constant quantities.** Fine-structure splittings reduced by
ν³ are constant to ~0.5% across a series, and the adjacent steps fall below
measurement noise (1.6%). Bracket coverage: **35.3%**. Zero of 17 adjacent steps
are resolvable. A constant is not monotone.

**(iii) Systems without interior cells.** Ti I: 23 channels, 26 members, **zero
interior cells**. No channel reaches three members, because the ionisation limit
near 55,000 cm⁻¹ sits below the onset of severe level density, and above
~42,000 cm⁻¹ the levels are 40–50% configuration-mixed and have no assignable
parent. The method declines rather than errs.

**(iv) Collapsed orbitals.** Excluded by the defect-departure test of Rule 1.

> **Figure 9.** Three failure panels: the Sr ¹P₁ node; the flat Δ_fs·ν³
> sequence with its noise band; the Ti I channel inventory showing zero interior
> cells.
>
> **Figure 10.** Domain map: *Z*_eff × ℓ grid, cells shaded by count, with
> excluded regions hatched and labelled by mechanism.

## 11. Predictions

### 11.1 Verified

**Kr II ²P°₁⁄₂ fine-structure splitting.** Derived from three ℓ channels of the
Kr I (²P°₁⁄₂) series and committed *before* the measurement entered the analysis:
**5,591 ± 500 cm⁻¹**. Measured: **5,370.10 cm⁻¹**. Error +221 cm⁻¹, 4.1%,
within the stated interval.

*Full disclosure on the interval.* The three channel estimates were 6,061,
5,679 and 5,031, giving sd = 521. The quoted ±500 is therefore approximately
1σ, not the conventional 2σ (which would be ±1,030). The measured value lies
0.4σ from the mean. The prediction is correct; the interval was tighter than
convention and this should have been stated at the time.

### 11.2 Open

Recorded here so they can be checked against future measurement.

**Ba I 5d² ¹G₄.** Deductive bracket from the term ordering
³F < ¹D < ³P < ¹G < ¹S: **[23,694, 26,757] cm⁻¹**. No point estimate is offered;
see §15 for why the estimate attempted during this work is withdrawn.

**Ba I 6s*n*f, missing members.** Bracket and Ritz estimate:

| level | bracket (cm⁻¹) | estimate |
|---|---|---|
| 6s8f | [39,678, 40,614] | 40,238 |
| 6s13f | [41,251, 41,648] | 41,367 |
| 6s14f | [41,251, 41,648] | 41,461 |
| 6s15f | [41,251, 41,648] | 41,536 |
| 6s16f | [41,251, 41,648] | 41,597 |

Leave-one-out validation on the same series: 15/15 bracket coverage, rms
20.5 cm⁻¹, with sub-wavenumber accuracy for *n* ≥ 17.

**Ti II a⁴F intervals**, derived from the Ti I 4f and 5g manifolds resolved by
core *J*, which agree to 0.7 cm⁻¹: **94.3, 131.9, 167.3 cm⁻¹** for
*J* = 3/2→5/2→7/2→9/2. Corresponding limits: 55,044.3 / 55,138.5 / 55,270.0 /
55,437.4 cm⁻¹. Internal check: taking δ(5g) = 0 gives δ(4f) = 0.0508, 0.0508,
0.0506, 0.0506 across the four independent channels.

---

# Part III — Indexing Without Prediction

## 12. The theorem

**Theorem 12.1.** *On a product order, join, meet and comparability are
definable from the coordinates.*

Explicitly: (*a* ∨ *b*)_i = max(*a_i*, *b_i*), (*a* ∧ *b*)_i =
min(*a_i*, *b_i*), and *a* ≤ *b* ⟺ ⋀_i (*a_i* ≤ *b_i*). Every lattice-theoretic
quantity is therefore a function of the coordinates, and can restate them but
cannot exceed them.

Two properties of this theorem drive Part III. It is **indifferent to
dimension**: Λ₁₁ is as constrained as Λ₈. And it is **indifferent to
faithfulness**: perfecting the index, as Part I does, moves nothing.

## 13. Six mechanisms

Six independent attempts to extract predictive uplift, each failing by a
distinct route.

**13.1 Rank aggregation.** Using rank(*a* ∧ *b*) and rank(*a* ∨ *b*) as
predictors of configuration mixing: LOO rmse 1.643 against 0.812 for a linear
model in Δ*q*, Δ*f* — worse than predicting the mean (data sd 0.940). *Mechanism:*
rank is a **sum over axes**, and summing discards which axis moved. Mixing
depends on which subshell is involved (*f* = 1 versus *f* = 2); rank cannot see
it. This is not a consequence of a loose index; it holds at any faithfulness.

**13.2 Comparability.** Comparable cells order energies correctly in 65 of 65
Ca I pairs, and select a 52.1% subset with 100% accuracy using no training data.
*Mechanism:* energy is separately monotone in every coordinate — 49
single-coordinate pairs, zero violations — so *a* ≤ *b* ⟹ *E*(*a*) ≤ *E*(*b*) is
a **theorem given monotonicity**, not an empirical finding. And monotonicity is a
coordinate property that a positive-weight linear model encodes directly, which
is why the control reached 99.9%.

**13.3 Zero-shot subset selection.** The lattice selects a reliable subset with
no labels; a fitted linear model needs 40 labels to approach it. *Mechanism:* a
**naive positive-weight sum**, with all weights set to +1 and no fitting, matches
it exactly — 100% at identical coverage, zero labels. The prior involved is
identical in both cases: "energy increases with excitation on every axis."

**13.4 Closure as existence.** Observed configurations are closed under meet more
than chance allows — Mg I *p* = 0.006, Ca I 0.031, Sr I and Ba I < 0.0001,
against a marginal-matched null. *Mechanism:* spectroscopists measure
**downward-closed regions**. Every Rydberg series is followed from its lowest
member upward, so the observed set is a lower set by construction. The
join/meet asymmetry that motivated the test appears only in sparse data (Mg, Ca)
and vanishes in dense (Sr, Ba, where join and meet are both significant and
nearly equal).

**13.5 Join-based configuration mixing.** For divalent atoms, roughly 62% of
pairs have **no upper bound at all**, at every valence count tested (*k* = 2, 3,
4). *Mechanism:* joining two doubly-excited configurations requires transferring
the union of their target electrons, but *q* ≤ *k*. The join is not ambiguous;
it does not exist. Raising *k* does not help, because it adds admissible states
as fast as it adds joins.

**13.6 A derived ordinal coordinate.** Collapsing four verified monotonicities
into κ = (*q*, *n*_core, −*n*, −ℓ) gives 2163/2163 monotone, 31.2% of pairs
comparable, and containment across species and charge simultaneously. *Mechanism:*
every component is a coordinate; the construction restates Theorem 12.1 rather
than escaping it. Its one apparent violation traced to a transcription error in
the input data (Appendix D).

## 14. What escapes

Deductive containment escapes Theorem 12.1, and it is the only thing we have
found that does.

A bracket is not a function of the coordinates. It is an **entailment**: given
that the property is monotone in the order, the true value at an unmeasured cell
*cannot* lie outside the interval formed by its measured neighbours. A regression
returns a point and a confidence interval that fails some fraction of the time;
the order returns containment that holds by construction. The distinction is
between inference and deduction, and it is why Part II's bracket never failed in
295 cells while every point-estimate claim in this work required qualification.

This also explains the asymmetry noticed in the compositional test of Section 9.
Propagating **point values** through the chain *n* → *I* → δ → *E* amplifies a
334 cm⁻¹ input error by a factor of 1.3 × 10⁶, because d*I*/dδ ≈ 75,000 cm⁻¹.
Propagating **intervals** through the same chain does not amplify at all: each
level's width is set by the spacing of its own measured neighbours, not
inherited from below. Monotone maps compose exactly on intervals and
catastrophically on points.

## 15. Discussion

### 15.1 The thesis, restated against the strongest premise

We began this work expecting the lattice's order to constrain physics. It does
not, and the reason is not that our index was too coarse. Over the course of
this work the index was **improved to exactness** — injective at eleven
dimensions, resolving core *J*, fine structure and the jK label — and the
predictive boundary did not move by one cell. Theorem 12.1 is indifferent to
dimension and to faithfulness.

The useful formulation is therefore: **an ordinal structure over configuration
space supplies indexing, and indexing is not prediction.** What the lattice
contributes to Part II is the well-definedness of "same channel" and "interior on
some axis" — real contributions, since without them the method could not be
stated — and nothing further. All quantitative content descends from
*T* = *Z*²*R*/ν².

### 15.2 Why energies and nothing else

*T* = *Z*²*R*/ν² is strictly monotone in every coordinate, has no zeros or
stationary points, varies by orders of magnitude across a series, and is
measured to 10⁻³ cm⁻¹. The bracket requires all four properties. We tested the
two nearest alternatives and each fails on a different one: dipole matrix
elements have zeros (§10 i), fine-structure splittings are asymptotically
constant (§10 ii). We know of no other atomic observable with all four.

### 15.3 Claims withdrawn

Stated explicitly so that readers of earlier versions are not misled.

1. **|Λ₈| = 61,453 as an invariant.** A truncation artefact; all derived region
   fractions likewise.
2. **"Zero invention" as a substantive property of Λ₈.** The set measured at 0%
   completion cost was defined by §9.4 chain constraints, and such a set is
   closed by construction. The measurement was tautological. The genuinely
   physical set has *nonzero* completion cost at every dimension (§6.3).
3. **The physical set as a sublattice.** False; spin parity breaks join.
4. **Offset coordinates as a repair.** They are faithful and injective but do not
   form a lattice (§6.4).
5. **Ca I 3d² ¹D₂ at 48,800–49,000 cm⁻¹.** Wrong by ≈ 1,000 cm⁻¹. It places ¹D
   above ³P, which for d² requires *C*/*B* > 5, outside the observed range. The
   revised unperturbed position is 47,539–48,213 cm⁻¹. The error was caught by
   the term-ordering constraint, not by the three fitted analyses that produced
   it.
6. **A point estimate for Ba I 5d² ¹G₄.** Three methods gave 24,163, 23,852 and
   22,094 cm⁻¹, the last outside its own deductive bracket. Withheld-term
   validation fails by 1,330 cm⁻¹. Only the bracket survives.
7. **Maximality without qualification.** Λ₈ is maximal *under derivation*; it is
   extensible by independent quantities (§5).
8. **The h-axis impossibility as a general result.** It is an instance of
   Theorem 4.1 — *h* was defined as a function of outputs, hence of the
   coordinates. Independent quantities are not so constrained, which is why
   *J*_c succeeds where *h* fails.

### 15.4 Open questions

Theorem 4.1 for sublattices of products of chains (§4.2). Whether any atomic
observable other than energy satisfies the four conditions of §15.2. Whether the
multi-subshell coverage gap admits a representation that preserves closure —
Appendix A shows the obvious route does not. And whether the bracketing method
transfers to non-atomic ordered systems, which we have not attempted.

---

# Appendices

## Appendix A — The multi-target extension and why it fails

The 86% coverage ceiling of §6.1 is caused by configurations with two occupied
non-source subshells. The natural repair is a second target triple
(*e*₂, *f*₂, *g*₂), giving Λ₁₁ (or Λ₁₅ with a second source). It fails, and the
failure is instructive.

**Ordering the targets is free.** The canonicalisation *e*₁ ≤ *e*₂ is admissible:
φ is the identity, non-decreasing in a single coordinate. Zero join and meet
failures.

**Conservation is not.** The physical requirement *g*₁ + *g*₂ ≤ *q* is a bound on
a **sum**, hence outside §9.4, and it breaks closure: 89,864 join failures in
979,300 sampled pairs, with meets unaffected. The counterexample is two lines —
*a* = (*g*₁=1, *g*₂=0, *q*=1) and *b* = (*g*₁=0, *g*₂=1, *q*=1) each satisfy
conservation, and their join transfers two electrons having removed one.

**Dropping conservation restores closure** (45,690 cells, zero failures) and
produces a lattice describing configurations that cannot exist.

**The conserving set is not a sublattice but is "almost" a lattice.** With
sufficient headroom, 133,542 of 133,542 interior pairs have a unique least upper
bound — the join exists, but is *not* componentwise max: *q* rises to admit both
transfers. Physically, the join of two transfer states requires removing another
electron.

**With two sources the uniqueness fails too.** Conservation becomes
*g*₁ + *g*₂ ≤ *q*₁ + *q*₂, a sum on both sides; 2.1% of pairs acquire multiple
minimal upper bounds, because the required extra ionisation can be taken from
either source. The resulting object is a **graded bounded poset**, self-dual in
its failures, neither a join- nor a meet-semilattice.

**And the slot representation is not faithful.** Sorted pairs and multisets are
in bijection but the bijection is **not a lattice homomorphism**: for 3d¹ and
4p², multiset union gives three transferred electrons and the sorted-pair join
gives two. A single-target configuration must be padded to fill two slots, and
two *different* single-target configurations then collide in the same slot,
merging targets that should remain distinct.

This is why Appendix A is an appendix. The extension is not a foundation for
further work until the representation problem is solved.

## Appendix B — Computational methods

All computations in Python 3 with NumPy and SciPy. Closure tests either
exhaustive over all pairs (stated where so) or on uniform random samples of
900–8,000,000 pairs with the sample size reported. Box searches enumerate all
2^d corners of candidate base cells. Null models for the closure-as-existence
tests of §13.4 are of two kinds: uniform random subsets of the physical envelope
matched in size, and marginal-matched subsets drawn with probability
proportional to the observed frequency of each coordinate value, the latter
constructed specifically to absorb observational-completeness effects.

Ritz fits use ordinary least squares on δ against 1/*n*², with σ from the
standard prediction error including the leverage term
*s*·√(1 + 1/*k* + (*x*₀ − *x̄*)²/*S*_xx).

## Appendix C — Data provenance

| source | used for |
|---|---|
| NIST ASD (Kramida et al., ver. 5.12) | Ca I/II, Sr II, Kr I/II, Sc III, Ti I levels |
| Sansonetti & Nave, JPCRD **39**, 033103 (2010) | Sr I levels and transition probabilities |
| Curry, JPCRD **33**, 725 (2004) | Ba I/II levels, Landé factors |
| Martin, Musgrove, Kotochigova & Sansonetti (NIST SRD 111) | ground configurations, ionisation energies |
| NIST Handbook of Basic Atomic Spectroscopic Data | H I, Mg I levels |
| Rafiq, Kalyar & Baig, J. Phys. B **40**, 3181 (2007) | Mg I 3s*n*d ¹D₂ series |
| Cowley (Michigan) compilation | successive ionisation energies |

Levels are quoted as published; centres of gravity are (2*J*+1)-weighted.

## Appendix D — Errors found and corrected during this work

Recorded because the method by which they were caught is part of the result.

**Ba I 6s11f mis-keyed as 6s8f.** Detected by the derived ordinal coordinate of
§13.6 producing four order violations, all involving one cell. The datum implies
δ = −2.84 as *n* = 8, which is impossible, and δ = +0.16 as *n* = 11, which is
correct for an f orbital. Corrected, the coordinate is 2163/2163 monotone.

**Ca I 3d² ¹D₂ position.** Detected by the d² term-ordering constraint
(¹D < ³P iff *C*/*B* < 5), which three fitted analyses had not applied.

**Regex parsing failure.** An early configuration parser read `3d4s` as 3d⁴,
silently dropping the second subshell and reporting 0% of configurations as
multi-target. Detected by manual inspection of a case known to be two-target.

**Bracket direction for decreasing sequences.** For a decreasing property the
tightest bracket takes the maximum over cells *above* in *n* and the minimum over
cells *below*; the reverse returns the global extremes. The error inflated a
reported width from 11% to 114%.

**Pooled σ.** Quoting a single σ across series with genuinely different defect
scatter (a 370× range) produced 96.2% coverage at nominal ±1σ and was
misinterpreted as heavy tails. Per-cell σ gives 68.1%.

**Anchoring on a published estimate.** A point prediction for Ba I 5d² ¹G₄ was
developed with a literature value visible from the first computation. Three
methods were tried and the selection among them was not independent of that
value; the finally reported range was 38% narrower than the inputs supported.
The episode is the reason §11.2 reports a bracket and no estimate, and the
reason the Kr II prediction of §11.1 was committed in writing before the
measurement was requested.

---

## Acknowledgement of computational assistance

Substantial parts of the analysis reported here — the closure and dimension
tests, the ablation studies, the 295-cell verification, the failure diagnostics
of Part III, and several of the corrections in Appendix D — were carried out in
dialogue with an AI system (Claude, Anthropic), which executed the computations
and served as an adversarial check on intermediate conclusions. The system does
not hold authorship: authorship entails accountability that it cannot bear.
Its errors, several of which are recorded in Appendix D, were caught by the
same process that caught the human ones, and the division of credit between
participants is not cleanly separable. What can be said precisely is that no
numerical claim in this paper rests on unexamined output: each was recomputed,
attacked, and in a number of cases withdrawn.
