
---

# PART II — THE LAW

---

# 7. Closure

Everything in this part follows from one condition.

> **An index X ⊆ ∏ᵢ Aᵢ is CLOSED if, for all *x*, *y* ∈ X, both *x* ∨ *y* and
> *x* ∧ *y* lie in X**, where join and meet are taken coordinatewise.

The coordinates must be **totally ordered** — chains. That restriction is
real and is discussed in §7.3.

## 7.1 The characterisation

> **Theorem 7.1 (A.4).** X is closed **iff** X = 𝓡(X), where 𝓡 reconstructs
> value sets and pairwise monotone bounds from X's own extension.

*Proof.* (⇐) 𝓡(X) is an intersection of sets {*x* : *xᵢ* ≤ φ(*xⱼ*)} with φ
non-decreasing, each closed under ∧ and ∨; so 𝓡(X) is closed, and if it
equals X then X is closed. (⇒) X ⊆ 𝓡(X) always, since each *x* ∈ X witnesses
its own bounds. For the reverse, each bound *yᵢ* ≤ φ̂ᵢⱼ(*yⱼ*) supplies a
witness *w* ∈ X with *wᵢ* ≥ *yᵢ* and *wⱼ* ≤ *yⱼ*; closure under ∧ and ∨ of the
witness family produces *y* itself. ∎

**Verified on 200 random constructions, 200 agreements** — random subsets (0
closed, 0 fixed points), lattice closures (40 and 40), random down-sets (16
and 16). Where they disagree they disagree together; there is no case of one
without the other.

**Note the down-set row.** Sum-bounded sets like {*a* + *b* ≤ *q*} are *not*
closed, and 𝓡 reports it correctly. §10.3 explains why sums are excluded.

## 7.2 𝓡 is a closure operator

Extensive, monotone, idempotent — **150 of 150 on all three axioms.**

So **E(X) = |𝓡(X)| − |X| is a closure defect**, a standard object in Galois
theory, formal concept analysis and database dependency theory.

**This book claims no novelty for the machinery.** What is offered is the
application: computing the closure defect of an *index*, and finding that the
periodic table's is 36 while Λ's is 0.

## 7.3 The scope, stated exactly

Theorem 7.1 requires each coordinate to be **presented as a chain.** That is
not the same as requiring the factors to be chains: any distributive factor
can be so presented, by Birkhoff, as the down-sets of its join-irreducibles —
one chain per irreducible.

**What fails is bundling.** 𝓡 reconstructs coordinate by coordinate, so
folding two chains into one non-chain coordinate hides structure from it. In
tests, the same sets presented bundled and presented decomposed both gave
80/80 agreement — the theorem survives, but only when the presentation
respects it.

## 7.4 The three consequences

Closure yields three properties, developed in the next three chapters:

| | | | |
|---|---|---|---|
| **S — reference** | S1 alphabet | S2 order | S3 bounds |
| **D — defence** | D1 𝒟_phys | D2 𝒟_def | D3 χ total |
| **E — extension** | E1 cells | E2 axes | E3 constraints |

**Nine mechanisms.** Six follow from closure without further hypothesis. Two
require something constructed — a tree, and disjoint derivations. One, E3, is
an exact criterion that took three wrong statements to reach.

**And E is derived**: every extension question reduces to S and D. It carries
no independent content, in the same way that the cost surface of Chapter 14
carries none beyond ν.

---

# 8. Self-reference

> **A closed index contains its own definition.**

To rebuild an index from nothing but a bag of tuples, three things are needed.
They are independent, and only one of them is hard.

## 8.1 S1 — the alphabet

> Âᵢ(X) = { *xᵢ* : *x* ∈ X }

A projection. **Always succeeds, no conditions.**

## 8.2 S3 — the bounds

> φ̂ᵢⱼ(*v*) = max{ *xᵢ* : *x* ∈ X, *xⱼ* ≤ *v* }

Read off the cells. For Λ₈ that is 56 functions, all recovered, and 𝓡(Λ) = Λ
exactly. **Always succeeds given the order.**

## 8.3 S2 — the order, which is the hard one

Given the alphabet but not the ordering of its values, can the ordering be
recovered?

**The necessary condition is provable and dimension-free.** Say *u* **may
precede** *v* on axis *i* if, for every *p* in the fibre over *u* and every
*q* in the fibre over *v*, the meet lies in F(*u*) and the join in F(*v*).

> **Lemma.** If X is closed and *u* < *v* on axis *i*, then *u* may precede
> *v*.
>
> *Proof.* Take *x* with *xᵢ* = *u* and *y* with *yᵢ* = *v*. Then *x* ∧ *y*
> has *i*-coordinate *u*, so its other coordinates lie in F(*u*); and *x* ∨ *y*
> has *i*-coordinate *v*, so its other coordinates lie in F(*v*). ∎
>
> Nothing in the argument uses *d* = 2.

**At *d* = 2 the converse also holds** and the criterion is exact: X is closed
under some order iff "may precede" is a total order, and that order **is** the
relabelling. Verified on 120 sets; 274 of 274 constructed total orders give
closed sets.

**Above *d* = 2 the converse fails.** Being a total order on every axis
separately is necessary and not sufficient — the axes' requirements can be
mutually incompatible. That is developed in §11.4, because it is a limitation
rather than a mechanism.

## 8.4 What does work above *d* = 2: propagation along the tree

**If the constraint graph is a tree**, each axis is constrained only by its
parent. Root anywhere, fix the root by brute force, and extend with
backtracking.

> **Λ's orders are recovered from a scrambled bag of cells: 20 of 20**, at two
> cap settings, on 216 and 976 cells with all eight axes independently
> permuted.

**Cost Σᵢ|Aᵢ|!, never the product ∏ᵢ|Aᵢ|!.**

Two earlier methods failed on the same task, and the failures are instructive.
Alternating refinement across all eight axes at once: **0 of 12.** Greedy
propagation without backtracking: 42% and 25%. **The tree says only neighbours
interact; a method that ignores that recovers nothing.**

## 8.5 So: Λ contains its own order

The unqualified claim — *the index contains its own definition* — holds for Λ
because its constraint graph is a tree. **For an index whose graph has cycles,
S2 is open**, and Chapter 20 states what is known.

**The qualified claim is unconditional:** 𝓡(X) = X recovers alphabet and
bounds for any closed index, relative to a given order.

---

# 9. Self-defence

> **A closed index contains its own contradiction.**

## 9.1 The counting argument

Let *p* be the parameters an index assigns and *q* = Φ(*p*) the quantities
derived from them.

> **𝒟 = dim *q* − rank ∂Φ/∂*p* ≥ dim *q* − dim *p***

*Proof.* The Jacobian is dim *q* × dim *p*; its rank exceeds neither. ∎

**Verified on seven dimension pairs and 420 random nonlinear maps.** No
closure required, no smoothness beyond differentiability.

> **Corollary. dim *q* > dim *p* ⇒ 𝒟 ≥ 1.**

𝒟 counts functionally independent relations the derived quantities must
satisfy. **Each is a test the index must pass.** For Λ with
*p* = (*T*, *n*, *Z*, σ) and *q* = (ν, δ, *V*, *r*, *w*, *e*), rank is 4 and
**𝒟 = 2**, spanned by

> **(a) *V* = 4ν/3   (b) *w* = *V* · *e***

## 9.2 The split, and it is canonical

(a) holds under the Rydberg law and fails under power-4, exponential and
logarithmic laws. (b) holds under all four.

> **𝒟 = 𝒟_phys + 𝒟_def**, physical relations and definitional identities

**Tested under four unrelated perturbations, verdicts identical.** The split
is not an artefact of which law one chooses to vary.

## 9.3 D1 — 𝒟_phys catches a wrong value in the data

**Worked case.** Two species in this work, Al II and K II, were first computed
with *Z*_eff = 1. Both have doubly charged cores.

> **The bracket held 56 of 56 either way.** Containment depends only on
> monotonicity of *T*, and *Z* cancels from it entirely.

What failed were the quantities the method does not use. δ̄ came out near 4.9
with a spread of several units — impossible for a Rydberg series, where δ is
near-constant. *V* departed from 4ν/3 by a **median of 50%**, where Na I gives
0.2%.

Corrected to *Z*_eff = 2: δ̄ = 1.271 with spread 0.047, *V* to **0.86%**.

> **The bracket verifies the data. *V* verifies the indexing.**
>
> An index carrying only what its method consumes would have passed
> fifty-six wrong cells.

## 9.4 D2 — 𝒟_def catches a wrong derivation, but only under two routes

**An identity is vacuous if its terms are computed along the same path.**
*w* = *V*·*e* cannot fail if *V* is *defined* as *w*/*e*. It becomes
diagnostic when *w* comes from the levels and *V* from the law.

> **𝒟_def is realised iff a quantity is reachable by two disjoint paths, and
> the defence is the DISAGREEMENT between them — not the relation.**

**Worked case, and it is the author's own error.** In first stating relation
(b) I wrote *w* = 3ν·*e*. The two values — 540.0 from the levels, 1215.0 from
the mis-stated law — appeared on the same printed line.

> **The check caught the check. 𝒟 ≥ 1 does not require the auditor to be
> right.**

**Worked case, in an apparatus.** Antiprotonic helium, cell (35,33):

| route | value |
|---|---|
| measured directly | 804,633,059.0 ± 8.2 MHz |
| two-photon minus a different single-photon | 804,633,057.8 ± 10.6 MHz |

**Agreement at 0.09σ, with no shared measurement.** One laser resonance
against a two-photon resonance minus an unrelated one. That is
path-disjointness realised in hardware.

**And a constraint on where 𝒟_def can come from.** Λ's constraint graph is a
tree, so there is exactly **one** path between any two coordinates. The
constraints supply **no** redundancy. 𝒟_def must be built from derived
quantities, deliberately.

## 9.5 D3 — totality catches a missing value

> **Theorem.** If Λ is closed, χ_Λ : ∏Aᵢ → {0,1} is **total**: membership is
> decided for every ambient point by a finite conjunction of decidable
> comparisons.
>
> *Proof.* Each bound compares two elements of a chain. Λ is a finite
> intersection of such conditions. ∎

**Verified on 30,000 uniformly sampled ambient points: values {0,1}, nothing
undecided.**

**Worked case.** A species was misidentified — Na II read as neutral neon, and
the wrong ionisation limit applied. Every channel had *T* = *I* − *E* ≤ 0 and
**every one was refused at entry.**

> **Totality does not detect that error. It forbids it.** The computation
> never ran.

**Worked case, the other way.** A guard in the author's code returned `None`
when an alphabet exceeded a cap, and the caller coerced `None` to `False`.
That produced "3 reorderable of 85 trials," which produced "almost never
reorderable," which produced a false dismissal of an entire line of evidence.

> **One silent discard propagated through three conclusions, none of which
> looked wrong**, because the arithmetic was consistent throughout.

**𝒟 ≥ 1 cannot catch that.** Every relation checks out on data that was never
measured. Only totality closes the hole, because *undetermined* is not in the
codomain.

## 9.6 The three defences are disjoint

| mechanism | catches | worked case |
|---|---|---|
| 𝓡(Λ) = Λ | rules not recoverable from cells | periodic table, E = 36 |
| 𝒟 ≥ 1 | a wrong value in data or derivation | wrong *Z*; *w* = 3ν·*e* |
| χ_Λ total | a missing value coerced to a real one | the cap discard |

**No mechanism catches another's class**, and this work supplied an instance
of each.

---

# 10. Extension

> **A closed index determines what may be added to it.**

Three operations, and only three: change the cells, change the axes, change
the constraints.

## 10.1 E1 — which cells may be added

> Λ ∪ {*x*} is closed **iff** for every *y* ∈ Λ, both *x*∨*y* and *x*∧*y* lie
> in Λ ∪ {*x*}

**100% over 288 tests.** A cell may be added exactly when it sits in a hole
whose joins and meets fall back into the lattice.

## 10.2 E2 — which axes may be adjoined

> Λ × *h* is closed **iff** *h* is a lattice homomorphism

**100% over 424 tests.** Projections, maxima, minima and constants qualify;
sums, products and differences do not.

**And a theorem in the other direction:**

> **Theorem 10.1 (adjunction never repairs).** For any *h* : *S* → *H*, with
> *S*′ = {(*x*, *h*(*x*))}: **S′ closed ⇒ S closed.**
>
> *Proof.* For *x*, *y* ∈ *S*, the join of (*x*,*h*(*x*)) and (*y*,*h*(*y*))
> is (*x*∨*y*, *h*(*x*)∨*h*(*y*)). If *S*′ is closed this lies in *S*′, so
> *x*∨*y* ∈ *S*. Meets likewise. ∎
>
> **Contrapositive: a non-closed set cannot be repaired by adjoining any
> function of its coordinates.** Tested on seven functions including the
> identity and a constant; none repairs.

**Three repair routes remain**, and only three: **enlarge** (add cells),
**restrict** (remove cells), **reorder** (change neither). The calendar of
Chapter 1 is repaired by reordering, at a cost of usability.

## 10.3 E3 — which constraints may be imposed

This one took three wrong statements to reach, which is recorded in
Chapter 18. The criterion is:

> **{ *h* ≤ *q* } is closed ⟺ *h*(*x*∨*y*) ≤ *q* for all *x*, *y* with
> *h*(*x*), *h*(*y*) ≤ *q***

**100% over 2,513 tests, nine functions.**

**The essential feature is that it is *q*-dependent.** Admissibility belongs
to the *pair* (*h*, *q*), not to *h* alone — which is why *a* + *b* ≤ 3 can be
closed where *a* + *b* ≤ 4 is not, and why every *q*-free criterion attempted
before this one failed.

**Meet never breaks it.** For monotone *h* with *h*(*x*), *h*(*y*) ≤ *q*,
*x*∧*y* ≤ *x* gives *h*(*x*∧*y*) ≤ *q* at once. **Only the join can break it**,
and it does so when the join raises *h* above both arguments.

> **Sums and products fail because a join raises every coordinate at once**,
> and anything accumulating across coordinates accumulates the raises.

**Λ's seven constraints are all safe by inspection**: each reads one
coordinate, or a minimum of two. **None sums.** That is why Λ is closed and
the periodic table is not — and it is checkable without touching a cell.

## 10.4 E is derived

| mechanism | fixed by |
|---|---|
| E1 addable cells | S3, the recovered bounds |
| E2 adjoinable axes | D3, totality — *h* must create no third state |
| E3 imposable constraints | S2, the recovered order |

**Every extension question reduces to S and D.** E carries no independent
content — exactly as the cost surface of Chapter 14 carries none beyond ν.

---

# 11. What the law forbids

The results of this chapter are the strongest in the book, and every one of
them is negative.

## 11.1 An index carries what its coordinates carry, and no more

> **Theorem 11.1.** The σ-algebra generated by Λ's order equals the σ-algebra
> generated by its coordinates.

No quantity is extractable from the ordering that is not already a function of
the coordinates. **Perfecting the index cannot add information**, because
there is none to add.

## 11.2 ν is inadmissible as an axis

ν = *e* − δ is a **difference**, and differences are non-monotone in the cell
order. **86 violations** at the caps tested.

So the quantity on which the whole of Part III depends **cannot be a
coordinate of Λ.** It lives over the lattice, not in it. Chapter 6's "over,
not graded by" is the same fact stated geometrically.

## 11.3 Depth is not a coordinate function

The number of measured members in a channel is not a function of the
coordinates at all. **It is a property of the literature**, and Chapter 12
makes that precise.

## 11.4 Closure is not locally determined

**This is the deepest limitation, and it was found by trying to evade it.**

> Closure is **not** implied by every proper projection being a fixed point of
> 𝓡.

**Explicit counterexample at *d* = 3, *c* = 2, six cells:**

> *S* = {(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,1), (1,1,0)}
>
> Every proper projection is a 𝓡-fixed point, yet
> **(1,0,1) ∨ (1,1,0) = (1,1,1) ∉ *S***

And the counterexamples are common — roughly **one in five** sets passing all
proper-projection tests fails closure.

**The mechanism.** The two cells agree on axis 0 and disagree on *both*
others. The join disagrees in a **combination**, and no lower-dimensional
projection can see a combination it does not contain.

> **Closure is a *d*-dimensional condition. No projection of it will serve as
> a criterion — not per-axis, not per-pair.**

**Consequence for verification:** a wrong choice can pass every local test and
fail only at the top. Chapter 20 states what this costs.

## 11.5 The pole

The cost of a guarantee, derived in Chapter 14, has a pole at *p* = 1 — the
exponent at which an observable is linear.

> **A straight line has no curvature. There is no interpolation error to
> price, so a guarantee costs infinitely more than the thing it guarantees.**

**The method has no domain at *p* = 1.** It is the only hard singularity in
the structure; every other limit is a threshold with data on both sides.

## 11.6 Why the negatives are the contribution

Λ is a bijective recoding of existing quantum numbers. It adds no physics. A
reader will observe this within a page, and they will be right.

**That is the point.** A recoding that adds nothing and still exhibits
closure, self-reference, self-defence and these five limitations is
demonstrating a property of **indexing**, not of atoms. If Λ contained new
physics the results would be about atoms and worth much less.

---

# 12. Retrieval as a lattice problem

> **Data can be retrieved in pieces; the index navigates.**

This is usually read as advice. It is the self-defence theorem again, with a
different failure mode.

## 12.1 The formalisation

Let **C** be the cells wanted and **S** = {*S*₁ … *S_k*} the sources, each a
subset of **C**, with **A**(*Sᵢ*) recording accessibility.

> *c* is **retrievable** iff ∃*i* : *c* ∈ *Sᵢ* ∧ **A**(*Sᵢ*)
>
> **route set R(*c*) = { *i* : *c* ∈ *Sᵢ* }**, **retrieval redundancy
> ρ(*c*) = |R(*c*)|**

**ρ = 1 is fragile. ρ ≥ 2 survives the loss of any single source.**

> **𝒟_def ≥ 1** — two disjoint derivations survive a computational error
> **ρ ≥ 2** — two disjoint sources survive an access failure

**Same structure. Different failure mode.**

## 12.2 A paywall blocks a source, not a cell

**Worked case.** The target was a transition frequency in antiprotonic helium.

| source | status |
|---|---|
| *Nature* **475**, 484 (2011) | **paywalled** |
| *Phys. Rev. Lett.* **96**, 243401 (2006) | **paywalled** |
| arXiv:1304.4330 | **open** — the *Nature* paper entire |
| **arXiv:1203.5425 (CODATA 2010)** | **open — Table XII, all fifteen frequencies, both papers** |
| arXiv:1308.1711, an unrelated citing paper | **open** — corroborates to 0.1 MHz |
| CERN CDS | open |

**ρ = 6. Two blocked, four open.** The cell was retrieved and the two-path
check on it closed at 0.09σ.

## 12.3 The secondary can be better than the primary

CODATA's Table XII carries both papers **with an extra digit the journals did
not print**, supplied privately by the experimenters to reduce rounding error.

> **The index does not merely route around an obstruction. It sometimes finds
> a better cell than the one that was blocked.**

## 12.4 The retrieval graph is self-referencing

Each fetched compilation names its successors. The aluminium compilation's
introduction lists its own sister volumes verbatim; the beryllium compilation
cites the zinc one; the aluminium reference list supplies nickel and copper.

**Three coverage gaps in this work's census were filled from documents already
in hand, with no new search.**

## 12.5 Where it fails, and the number that describes it

Four documents in this work were not retrieved: Edlén's *Handbuch* chapter
(1964), Ritz's *Physikalische Zeitschrift* paper (1908), Paschen & Götze
(1922), Dunz (1911). **ρ ≤ 2 for each, every route closed.**

Not for lack of effort — nine searches, correct citations, the right platform
identified and free. **Pre-digital print has low retrieval redundancy.**

> **ρ is a property of the literature, not of the searcher. A cell in a 1908
> German periodical has ρ ≈ 1. A cell in a 2011 physics paper has ρ ≈ 6.**

**A century of open deposition raised ρ roughly sixfold**, and that is exactly
what separated the two outcomes.

## 12.6 The procedure

1. Enumerate target cells from the index **before** searching.
2. List route candidates per cell — primary, preprint, review, compilation,
   citing paper, deposit, database.
3. Prefer high-ρ cells; they cost less and often carry more.
4. Read every retrieved source for its successors.
5. When a route is blocked, move along the route set; do not re-attempt.
6. **Record ρ for cells that fail.** A blocked ρ = 1 cell is a *stated* gap,
   not an unexplained absence.

**The author violated step 1 badly**, on his own problem, after writing this
chapter. That is recorded in Chapter 18.