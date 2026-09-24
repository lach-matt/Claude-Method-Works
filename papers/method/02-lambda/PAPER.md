# The Lattice of Subshell Transitions

**The eight-coordinate cells admitted by seven monotone bounds form a closed index of 976 cells — a distributive, modular, Sperner lattice with seventeen join-irreducibles and seventeen meet-irreducibles, carrying an interval metric, a void that factorises because its constraint graph is a tree, a single generating polynomial with F(1) = 976 and F(−1) = 2, a Möbius function in closed form that is non-zero exactly on the void-free unit hypercubes, and a minimum generating set of seven of its own cells, every such set containing a null transition, a full transfer and each of the three channels s → p, p → s and p → p.**

**Matthew Lach** · Independent Researcher · 24 September 2026

---

## Abstract

A subshell transition between atomic configurations is specified by eight integers: the shell, subshell and occupancy of the source, the number q of electrons removed from it, the shell and subshell of the target and the number g of electrons placed there, and the spin label 2S of the source. Four physical facts — the hydrogenic node count, the Pauli capacity, conservation of the moved electrons, and the addition of spins — cut the eight-fold product down to a set Λ, and each of them does so by one inequality of the same shape, one coordinate bounded by a non-decreasing function of one other; six of the seven inequalities are exact physical rules and the seventh, the spin bound, is the monotone envelope of one. A transition here is a change of configuration labels and not a spectral line: no selection rule, energy or intensity enters, and nothing is tested against measured spectra. This paper shows what that shape buys. Λ is a sublattice of its ambient box: machine-checked with all variables integer, so the result holds at every cap and not at one. At the caps used here Λ has 976 cells in a box of 6,912, it is distributive and its rank function is modular with equality, its largest antichain equals its largest rank level, and it is the lattice of down-sets of a seventeen-element poset whose twenty covering relations are the seven bounds read a second time. The number seventeen is Σᵢ(|Aᵢ| − 1), a closed form in the alphabets. A multiplicative distance d(x, y) = ∏ᵢ(|Δᵢ| + 1) counts the points of the box between two cells and equals a divisor count under a prime encoding; its logarithm is an ℓ¹ metric. Because the constraint graph is a tree — a caterpillar, a path of seven with one pendant — the number of cells in any coordinate box has a product form with no inclusion–exclusion, verified on all 1,944,000 sub-boxes; the whole index is one nested sum F whose coefficient function is its own membership predicate, with F(1) = 976 and F(−1) = 2. The Möbius function is ±1 on antichain differences — the sign the parity of the number of generators added — and zero elsewhere, verified against the defining recursion on all 116,138 comparable pairs. Its non-zero values sit exactly on the 19,079 comparable pairs whose box is a unit hypercube inside Λ, so it is decided by the same seven comparisons that decide containment, and it agrees with the number-theoretic Möbius function of N(y)/N(x) everywhere except on the 17,104 unit hypercubes that carry a void. Finally, seven cells generate the whole of Λ under the pairwise-envelope closure; an exhaustive branch-and-bound finds 24,585 minimum generating sets, exactly one cell lies in all of them, no covering obligation is met by a unique cell, no single cell can be removed from Λ without the closure restoring it, and every minimum generating set contains a null transition, a full transfer and each of the channels s → p, p → s and p → p. The closure defect and the closed-form generator count are re-measured at five further cap settings, from 216 to 19,109 cells, and hold at each.

---

## §0 · The result

**Seven inequalities of one shape make an index that is closed, that has a seventeen-letter alphabet, and that is recoverable from seven of its own cells.**

The object is a set Λ of eight-tuples of integers (§1). Every bound has the form xᵢ ≤ φ(xⱼ) with φ non-decreasing; six of the seven are physical facts stated exactly and the seventh, the spin bound 2S ≤ k, is the monotone envelope of one; and no bound is implied by the others — each excludes between 24 and 673 points of the ambient box that all six others admit (§1, Table 2). The envelope is chosen for shape and the paper says so: the exact spin rule is a congruence together with a ceiling in two coordinates, neither of which is a monotone bound in one coordinate, and §1 counts what the envelope admits — 503 of the 976 cells carry a spin label that no configuration of k equivalent electrons has. The work of this paper is to show what follows from the shape alone.

Of the results below, distributivity, rank modularity, the Birkhoff representation, order dimension equal to the width of the generating poset, maximal chains as linear extensions, the antichain form of the Möbius function and log d as an ℓ¹ metric are consequences of Λ being a sublattice of a product of chains; they are verified here on the instance and are not claimed as new. What is new is the object and what is measured on it: that seven bounds of this shape close exactly, the grading proved from the shape of the bounds, the tree factorisation verified on every sub-box, the localisation of F(−1) = 2 on the cells with k = 2, the void lift, the exact comparison of the two Möbius functions, and the exhaustive seed enumeration with its one common cell and no unique witness.

**Closed.** Λ is closed under coordinatewise maximum and minimum (Theorem 1). This is proved for every cap setting at once: the obligation is stated with the five caps and both cells as integer variables and discharged by an SMT solver, so it is not a fact about one box. The same is machine-checked for a single bound with the bounding function left uninterpreted and only monotonicity assumed (Lemma 1), which locates the hypothesis exactly: drop monotonicity and the claim is refuted; replace one bound by a bound on a sum and the claim is refuted, with an explicit witness (§9).

**Counted, at the stated caps.** With n, e ≤ 3, ℓ, f ≤ 1 and k ≤ 3, Λ has **976** cells in a box of **6,912** — 14.12% of it. The staircase closure returns Λ exactly, so its closure defect is **0**, and a second application changes nothing. Of the 976 cells, 165 move no electron (q = 0), 330 move one, 345 move two and 136 move three: 481 move two or three electrons, which is why the cells are subshell transitions and not one-electron ones.

| what | value | how |
|---|---|---|
| cells, box, density | 976 · 6,912 · 14.12% | EXHAUSTIVE |
| rank range, cover relations | 3 to 20 · 3,749 | EXHAUSTIVE |
| largest antichain = largest rank level | **122**, at rank 11 | EXHAUSTIVE |
| join-irreducibles = meet-irreducibles = Σᵢ(∣Aᵢ∣ − 1) | **17** | EXHAUSTIVE |
| down-sets of the generating poset | **976** of 2¹⁷ = 131,072 subsets | EXHAUSTIVE |
| covering relations among the generators | **20** — 9 within a coordinate, 11 between | EXHAUSTIVE |
| F(1), F(−1), F′(1)/F(1) | 976 · 2 · 10801/976 = 11.0666 | EXHAUSTIVE, exact |
| void-free pairs | 134,871 of 475,800 — 0.2835 | EXHAUSTIVE |
| maximal chains, each of 17 steps | 1,113,045,672 | EXHAUSTIVE |
| μ(x, y) ≠ 0 | on 19,079 of 116,138 comparable pairs, the void-free unit hypercubes | EXHAUSTIVE |
| minimum generating set | **7** cells; 24,585 such sets; 1 cell in all | EXHAUSTIVE |

**What is not claimed.** Λ without caps is infinite, and every *count* above is a count at one cap setting, named wherever it appears. The structural statements divide into two kinds and the paper never merges them. Theorem 1, Lemma 1 and the sufficient half of Theorem 13 are machine-checked over the integers and hold at every cap, and Lemma 2 over every subset of two named boxes; the written proofs of Theorems 3, 4, 6 (the form of the join-irreducibles and the closed count), 10, 11, 12, 13 and 16 and of Corollary 6 use no cap; Theorem 17 holds at any cap setting at which the closure defect is 0, which Theorem 2 establishes at six; Theorem 15 and Corollaries 7 and 8 are statements at the stated caps, since their proofs name cells and counts of that setting. Every count — 976, 122, 17, 20, 3,749, 24,585 and the rest — is a computation at the stated caps, and the closure defect and the generator count are re-measured at five further settings (Theorem 2) but no count is proved to persist. The seed of 7 is exact at the stated caps, by an exhaustive branch and bound and not by a heuristic; the general problem is NP-hard (its decision version is NP-complete, Karp 1972), and this paper makes no claim about its value at other caps. The physics enters only in §1, in one paragraph and one definition, and only to say where the seven bounds come from and what a cell records; nothing after them uses it.

**One finding worth stating in front.** Exactly one cell lies in all 24,585 minimum generating sets, and yet **no covering obligation is met by a unique cell** — the smallest witness set has four — so the elementary rule that forces a set into every minimum cover does not apply anywhere in this instance, and no single cell can be deleted from Λ without the closure putting it back (Corollary 8). What can be said locally is that the cell is the only common witness of three obligations; that no seed of seven can afford to meet those three with two cells is what the enumeration shows (§7). What every minimum seed shares is stated in Corollary 7 and proved from the covering criterion: a null transition, a full transfer at every occupancy, and each of the channels s → p, p → s and p → p — while an s → s cell appears in 17,403 of the 24,585 and is not forced.

**Status words.** Five, used exactly as follows and never merged.

| status | meaning |
|---|---|
| **PROVED** | a proof is written out below and every step is justified |
| **MACHINE-CHECKED** | an SMT solver returned `unsat` on the negation of an obligation whose variables range over every integer — hence over every cap — or over every subset of a named finite box, with both guards passed |
| **EXHAUSTIVE** | a decision procedure visited every case in a stated finite family, and the family is named |
| **SAMPLED** | a seeded pseudorandom sweep of a stated size; never exhaustive |
| **CITED** | taken from the literature, with the source |

---

## §1 · The index, and that it closes

**The physics, in one paragraph.** A bound electron in a hydrogen-like potential is labelled by a principal quantum number n (Bohr 1913) and an orbital angular momentum ℓ, and the radial equation has a solution only for ℓ ≤ n − 1 (Schrödinger 1926). A subshell of angular momentum ℓ holds at most 2(2ℓ + 1) = 4ℓ + 2 electrons, the number of one-electron states with that ℓ, made exclusive by the exclusion principle (Stoner 1924; Pauli 1925). A cell records a move: q electrons are removed from a source subshell holding k, and g of them are placed in a target subshell, so q ≤ k and g ≤ q. The coordinate g counts the electrons placed; the target is taken to begin empty — the index carries no coordinate for what was already there — and the Pauli bound g ≤ 4f + 2 therefore reads g as the target's occupancy after the move. The total spin of k electrons of spin ½ cannot exceed k/2, by the addition of angular momenta (Condon and Shortley 1935), so the spin label 2S (multiplicity 2S + 1) is bounded by k. That last bound is an envelope and not the rule: for k equivalent electrons in a subshell of angular momentum ℓ the rule is 2S ≡ k (mod 2) with 2S ≤ min(k, 4ℓ + 2 − k), the ceiling by particle–hole conjugation, and neither the congruence nor the two-coordinate ceiling has the form xᵢ ≤ φ(xⱼ) — a congruence is not monotone, and the ceiling names two coordinates — so neither is imposed. The envelope admits 503 of the 976 cells at the caps of D3 whose spin label no configuration of k equivalent electrons carries: 413 with 2S of the wrong parity, 180 above the particle–hole ceiling, 90 both; the 473 physical labels are 48.5% of Λ (§9). Those four facts are the origin of the seven inequalities below, six stated exactly and the seventh as an envelope. A transition here is a change of configuration labels and nothing more: no selection rule enters (Δℓ = ±1 would remove the s → s and p → p cells), no parity, energy or intensity enters, and nothing in this paper is tested against measured spectra. Everything after this paragraph and D1 is a statement about the resulting set of integer tuples.

**D1 (the coordinates).** A **cell** is an eight-tuple of integers

> x = (n, ℓ, k, q, e, f, g, 2S),

read as: a source subshell (n, ℓ) holding k electrons with spin label 2S, of which q are removed, and a target subshell (e, f) into which g of them are placed. The coordinates are indexed 1 to 8 in that order and xᵢ denotes the i-th. The model is exactly this and no more. A cell with g = q places every removed electron (461 cells); a cell with g < q — 515 of the 976 — records q − g electrons removed and not placed, and the index says nothing about where they go, having no coordinate for a second destination; a cell with q = 0 (165 cells) is a null transition, a source configuration with no move and, by g ≤ q, nothing placed; and 200 cells have (n, ℓ) = (e, f), source and target the same subshell, which the seven bounds admit because no bound compares a source label with a target label — the only bound joining the two ends is g ≤ q. The paper carries all 976 as cells of the index; which of them a spectroscopist would call a transition is not a question the index answers. All four counts are check lines (§9).

**D2 (the bounds).** The **seven bounds** are

> ℓ ≤ n − 1 · k ≤ 4ℓ + 2 · q ≤ k · f ≤ e − 1 · g ≤ 4f + 2 · g ≤ q · 2S ≤ k,

together with the floors n ≥ 1, e ≥ 1, k ≥ 1 and ℓ, f, q, g, 2S ≥ 0. The floor k ≥ 1 is a definitional restriction, not a bound: a cell is a transition and a transition needs a mover. Each of the seven has the form xᵢ ≤ φ(xⱼ) with φ non-decreasing and with exactly two coordinates named. None is a sum and none is a difference. Six are exact physical rules and the seventh, 2S ≤ k, is the envelope described above; the shape is the same for all seven, and the shape is what the paper uses.

| bound | origin | form | kind |
|---|---|---|---|
| ℓ ≤ n − 1 | hydrogenic radial solution | ℓ bounded by n | exact |
| k ≤ 4ℓ + 2 | Pauli capacity of a subshell | k bounded by ℓ | exact |
| q ≤ k | counting: no more may be removed than are present | q bounded by k | exact |
| f ≤ e − 1 | hydrogenic radial solution, on the target | f bounded by e | exact |
| g ≤ 4f + 2 | Pauli capacity, on the target | g bounded by f | exact |
| g ≤ q | counting: no more may be placed than were removed | g bounded by q | exact |
| 2S ≤ k | addition of k spins ½ on the source | 2S bounded by k | envelope: the rule 2S ≡ k (mod 2), 2S ≤ min(k, 4ℓ + 2 − k) admits 473 of the 976 cells |

: **Table 1 — the seven bounds and where each comes from.**

**D3 (the caps, and the ambient box).** A **cap setting** is a tuple (nₘₐₓ, eₘₐₓ, ℓₘₐₓ, kₘₐₓ, fₘₐₓ) of positive integers. Throughout this paper the caps are **(3, 3, 1, 3, 1)** unless another setting is named. The **alphabets** are then

> A₁ = {1,2,3} · A₂ = {0,1} · A₃ = {1,2,3} · A₄ = {0,1,2,3} · A₅ = {1,2,3} · A₆ = {0,1} · A₇ = {0,1,2,3} · A₈ = {0,1,2,3},

and the **ambient box** is B = A₁ × … × A₈, a product of eight chains, of size **6,912**. At a general cap setting the alphabets are A₁ = {1, …, nₘₐₓ}, A₂ = {0, …, ℓₘₐₓ}, A₃ = {1, …, kₘₐₓ}, A₄ = A₇ = A₈ = {0, …, kₘₐₓ}, A₅ = {1, …, eₘₐₓ} and A₆ = {0, …, fₘₐₓ}: q, g and 2S take the cap of k, since each is bounded by k or by q and no cap of its own is needed.

**D4 (Λ).** Λ := { x ∈ B : x satisfies the seven bounds of D2 }.

**D5 (the lattice operations).** For x, y ∈ B write x ∨ y for the coordinatewise maximum and x ∧ y for the coordinatewise minimum, and x ≤ y for the coordinatewise order. B is a lattice under these; a subset S ⊆ B is a **sublattice** when x, y ∈ S implies x ∨ y ∈ S and x ∧ y ∈ S.

**D6 (rank).** rank(x) := Σᵢ xᵢ.

**Theorem 1 (Λ is a sublattice).** For every cap setting and every x, y ∈ Λ, both x ∨ y and x ∧ y lie in Λ.

*Proof.* Take a bound xᵢ ≤ φ(xⱼ) with φ non-decreasing, and let z = x ∨ y. Then zᵢ = max(xᵢ, yᵢ) is one of the two, say zᵢ = xᵢ. Since x ∈ Λ, xᵢ ≤ φ(xⱼ), and since xⱼ ≤ max(xⱼ, yⱼ) = zⱼ and φ is non-decreasing, φ(xⱼ) ≤ φ(zⱼ). Hence zᵢ ≤ φ(zⱼ). If instead zᵢ = yᵢ the same argument runs with y in place of x. For the meet, let w = x ∧ y and let the *second* coordinate decide: wⱼ = min(xⱼ, yⱼ) is one of the two, say wⱼ = xⱼ. Then wᵢ ≤ xᵢ ≤ φ(xⱼ) = φ(wⱼ). If wⱼ = yⱼ the same runs with y. The floors and caps are conditions on one coordinate at a time and each is an interval, so they survive max and min. Every one of the seven bounds is of this shape, so both z and w satisfy all seven. ∎ **PROVED**, and **MACHINE-CHECKED**: the negation of the implication, with the five caps and all sixteen cell coordinates as integer variables, is `unsat`. Both guards pass (§9), and two negative controls are refuted in §9 — the claim fails if monotonicity is dropped, and it fails if any one bound is replaced by a bound on a sum.

**Lemma 1 (one monotone bound, with φ uninterpreted).** Let φ : ℤ → ℤ be non-decreasing and let R = {(a, b) ∈ ℤ² : a ≤ φ(b)}. Then R is a sublattice of ℤ².

*Proof.* The argument of Theorem 1, restricted to one bound. ∎ **PROVED**, and **MACHINE-CHECKED** with φ an uninterpreted function symbol constrained only by ∀u,v. u ≤ v → φ(u) ≤ φ(v), and a, b integer: `unsat`. Dropping the monotonicity axiom makes the same query `sat`, so monotonicity is not a convenience of the proof but the hypothesis.

**D7 (the envelope, and the closure operator).** For a finite X ⊆ ℤ⁸ with alphabets Aᵢ(X) = {xᵢ : x ∈ X} and box B(X) = ∏ᵢ Aᵢ(X), the **envelope** of X is

> φ̂ᵢⱼ(a; X) := max{ yᵢ : y ∈ X, yⱼ ≤ a }  for i ≠ j and a ∈ Aⱼ(X),

and the **staircase closure** is ℛ(X) := { x ∈ B(X) : xᵢ ≤ φ̂ᵢⱼ(xⱼ; X) for all i ≠ j }; the set after the semicolon is dropped when it is clear. X is **closed** when ℛ(X) = X; the **closure defect** is E(X) := |ℛ(X)| − |X|. That ℛ is a closure operator in the sense of Moore (1910) — extensive, monotone and idempotent — is established in the companion paper on the closure law (Lach 2026) and is not used below; this paper uses only the definition. The fact behind the definition is older: a sublattice of a product of chains is determined by its two-fold projections (Baker and Pixley 1975; Bergman 1977), and ℛ reads X through exactly those projections, one envelope per ordered pair of coordinates.

**Lemma 2 (a fixed point of ℛ is a sublattice).** If ℛ(X) = X then X is closed under ∨ and ∧.

*Proof.* Each defining condition of ℛ(X) is a bound xᵢ ≤ φ̂ᵢⱼ(xⱼ) and each envelope φ̂ᵢⱼ is non-decreasing by construction, being a maximum over a set that grows with its argument. So ℛ(X) is an intersection of sets of the form of Lemma 1, restricted to a box; an intersection of sublattices of a lattice is a sublattice, and B(X) is itself a sublattice of ℤ⁸. ∎ **PROVED**, and **MACHINE-CHECKED** over the subsets of two boxes: for every one of the 2⁹ subsets of a 3 × 3 box, and every one of the 2²⁷ subsets of a 3 × 3 × 3 box, the implication "X is a fixed point of ℛ and realises every value of every coordinate ⟹ X is closed under ∨ and ∧" is `unsat` under negation.

**Theorem 2 (the index is exactly its own closure).** At the caps of D3, |Λ| = 976, ℛ(Λ) = Λ and E(Λ) = 0; a second application of ℛ changes nothing.

*Proof.* Computation. Λ is built twice, by nested enumeration in the order of Theorem 14 and by sieving all 6,912 points of the box against the seven bounds, and the two agree cell for cell. The staircase closure of the result has 976 cells and is equal to Λ as a set, and ℛ(ℛ(Λ)) = Λ. ∎ **EXHAUSTIVE** (6,912 box points; the closure is computed over the same box). The same two computations at five further cap settings — (2,2,1,2,1), (3,3,1,4,1), (4,3,1,4,1), (4,4,2,4,1) and (4,4,2,6,2), with 216, 1,636, 2,394, 5,157 and 19,109 cells — return defect 0 at each; the closed-form count of join-irreducibles of Theorem 6 is verified at the same five settings, at 11, 21, 22, 24 and 33. **EXHAUSTIVE**, the settings named.

| bound | g ≤ q | q ≤ k | k ≤ 4ℓ+2 | ℓ ≤ n−1 | 2S ≤ k | f ≤ e−1 | g ≤ 4f+2 | *k ≥ 1* |
|---|---|---|---|---|---|---|---|---|
| points excluded by it alone | **673** | 575 | 564 | 308 | 300 | 200 | **24** | *25* |

: **Table 2 — no bound is redundant.** For each bound, the number of ambient points that satisfy the other six and fail only this one.

Every entry is positive, so no bound follows from the rest, and the ranking is itself informative: the bound that removes most is g ≤ q, the only one relating a target coordinate to a source coordinate. **EXHAUSTIVE** over the 6,912 box points (and, for the floor, over the 9,216 points of the box extended to k = 0).

**Corollary 1 (the one coupling).** The coordinate g is the only one carrying two bounds, g ≤ min(q, 4f + 2). Dropping the Pauli half leaves 1,000 cells; the 24 lost all have f = 0 and g = 3 — three electrons in an s subshell.

*Proof.* Computation over the box; the 24 are exhibited by their coordinates. ∎ **EXHAUSTIVE** (6,912 box points).

**Lemma 3 (the constraint graph is a caterpillar).** Let G have the eight coordinates as nodes and one edge per bound, joining the two coordinates it names. Then G is connected with 8 nodes and 7 edges, hence a tree, with degree sequence 1,1,1,2,2,2,2,3: it is the path e — f — g — q — k — ℓ — n with 2S pendant at k, a caterpillar (Harary and Schwenk 1973). Orient each edge from the bounded coordinate to the bounding one — ℓ → n, k → ℓ, q → k, 2S → k, f → e, g → f, g → q — and the oriented graph has no directed cycle.

*Proof.* Each of the seven bounds names exactly two coordinates, so G has exactly seven edges; a traversal from n reaches all eight nodes, so G is connected; a connected graph on 8 nodes with 7 edges is a tree. The degrees are read off the seven bounds, and removing the three leaves n, e and 2S leaves the path f — g — q — k — ℓ, so G is a caterpillar. A directed cycle in any orientation of G would be a cycle in G, and a tree has none. ∎ **PROVED** and **EXHAUSTIVE** (the graph is built from D2, traversed, and the orientation tested).

![**Figure 1.** The constraint graph: eight coordinates, seven bounds, one edge per bound, each edge labelled with its inequality; the plate writes the two Pauli bounds as 2(2ℓ + 1) and 2(2f + 1), which are 4ℓ + 2 and 4f + 2. The graph is connected with seven edges on eight nodes, so it is a tree, and its degree sequence 1,1,1,2,2,2,2,3 makes it a caterpillar — a path of seven with one pendant, 2S at k. Every consequence in §4 and §5 is a consequence of that shape.](figures/fig1-constraint-tree.png)

---

## §2 · Structure

Throughout this section Λ is at the caps of D3 and the numbers are counts at those caps.

**D8 (irreducibles, and the Sperner property).** In a finite lattice, y **covers** x when x < y and no z has x < z < y. A cell is **join-irreducible** when it covers exactly one cell, and **meet-irreducible** when exactly one cell covers it. A finite graded poset has the **Sperner property** when no antichain is larger than its largest rank level.

**Theorem 3 (distributive).** Λ is a distributive lattice.

*Proof.* In a chain, min(a, max(b, c)) = max(min(a, b), min(a, c)): the three orderings of a, b, c are checked directly, and there are no others. Hence the ambient box B, a product of chains with coordinatewise operations, is distributive. By Theorem 1, Λ is a sublattice of B and its ∨ and ∧ are the restrictions of B's, so the identity restricts to Λ — a sublattice of a distributive lattice is distributive (Birkhoff 1940; Davey and Priestley 2002, CITED). ∎ **PROVED**; the chain identity is **EXHAUSTIVE** over all 289 triples of values drawn from the eight alphabets, and a **SAMPLED** sweep of 200,000 cell triples (seed 20260921) found no failure.

**Theorem 4 (graded, and modular with equality).** rank is a grading of Λ: the unique minimum is (1,0,1,0,1,0,0,0) at rank 3, the unique maximum is (3,1,3,3,3,1,3,3) at rank 20, there are 3,749 covering relations and every one raises rank by exactly 1. Moreover, for every x, y ∈ Λ,

> rank(x ∨ y) + rank(x ∧ y) = rank(x) + rank(y).

*Proof.* For integers a, b, max(a, b) + min(a, b) = a + b — one of the two is the maximum and the other the minimum. Summing that identity over the eight coordinates and using that ∨ and ∧ are coordinatewise (Theorem 1) gives the displayed equality. For the grading, the claim is that if y covers x in Λ then y − x is a unit vector. This is not true of every sublattice of a box — the two-element chain {(0,0), (1,1)} is a sublattice of {0,1}² in which (1,1) covers (0,0) at rank distance 2 — so the argument must use the shape of the bounds. Call the bounded coordinate of a bound xᵢ ≤ φ(xⱼ) a child of the bounding coordinate j. Let x < y in Λ and let S be the set of coordinates at which they differ. The child relation restricted to S has no directed cycle (Lemma 3), so some i ∈ S has no child in S. Put z := y − eᵢ, the cell y with coordinate i lowered by one. It lies in the ambient box, since zᵢ = yᵢ − 1 ≥ xᵢ. Every bound in which i is the bounded coordinate holds at z: zᵢ < yᵢ ≤ φ(yⱼ) = φ(zⱼ). Every bound in which i is the bounding coordinate, xₘ ≤ φ(xᵢ) with m a child of i, also holds at z: m ∉ S, so zₘ = yₘ = xₘ ≤ φ(xᵢ) ≤ φ(yᵢ − 1) = φ(zᵢ), because xᵢ ≤ yᵢ − 1 and φ is non-decreasing. Every other bound is unchanged. So z ∈ Λ and x ≤ z < y; if y covers x this forces z = x, that is y = x + eᵢ, and rank rises by exactly 1. The extremes are computed. ∎ **PROVED**; **EXHAUSTIVE** on all 475,800 unordered pairs, zero violations, and on all 3,749 cover relations, which the check finds from the order alone — x < y with no cell between — and then tests, every one being a unit step.

The equality matters. Matroid rank and entropy are *sub*modular — the left side is at most the right. Λ's rank meets the equality, which is the graded signature of modularity: a finite lattice is modular if and only if it is graded and its rank function satisfies the equality (Birkhoff 1940; Davey and Priestley 2002, CITED). Distributivity is the stronger property and is Theorem 3's. The pair condition is the cheaper test — O(N²) against the O(N³) of the triple law — and a failure of it would refute distributivity, but a pass does not establish it: the diamond M₃ is modular and not distributive.

**Theorem 5 (Sperner).** The largest antichain of Λ has 122 elements, and 122 is the size of the largest rank level, which is rank 11: Λ has the Sperner property.

*Proof.* The rank sequence, at ranks 3 to 20, is

> 1, 5, 15, 34, 59, 87, 108, 121, **122**, 115, 100, 79, 57, 37, 21, 10, 4, 1,

summing to 976, and it is log-concave at every interior rank — aᵣ² ≥ aᵣ₋₁aᵣ₊₁ — hence, having no internal zero, unimodal (Stanley 1989, CITED). Each rank level is an antichain, so the largest antichain is at least 122. For the upper bound, Dilworth's theorem (1950), CITED, says the largest antichain equals the minimum number of chains covering the poset, and by König's theorem (1931) the minimum chain cover of an N-element poset is N minus a maximum matching in the bipartite graph of its strict order — the reduction of Fulkerson (1956), CITED. That matching, computed by the Hopcroft–Karp algorithm (1973), CITED, has 854 edges, so the minimum chain cover is 976 − 854 = 122 and no antichain exceeds it. So the largest antichain is a rank level, the property named for Sperner's theorem (1928) on the Boolean lattice. It has to be computed: the ambient box, a product of chains, is Sperner (Proctor, Saks and Sturtevant 1980; Stanley 1980), but a sublattice of a Sperner poset need not inherit the property. ∎ **EXHAUSTIVE** (the exact matching over all 115,162 strict comparabilities) and **CITED** (Dilworth; König; Fulkerson; Hopcroft–Karp).

Λ is **not** rank-symmetric. The centre of mass of the rank sequence is 10801/976 = 11.0666 against the midpoint 11.5, a skew of −0.43. Low ranks are cut by the floors n ≥ 1, e ≥ 1, k ≥ 1 and high ranks by the seven bounds; there are more ceilings than floors, and the sequence is pruned harder at the top.

![**Figure 2.** The rank sequence over all 976 cells. It is log-concave, hence unimodal, hence Sperner, with the largest level 122 at rank 11. It is not symmetric: the centre of mass 11.07 sits below the midpoint 11.5 by 0.43.](figures/fig2-rank-sequence.png)

**Theorem 6 (seventeen letters, in closed form).** Λ has exactly 17 join-irreducibles and exactly 17 meet-irreducibles, and

> |J(Λ)| = Σᵢ (|Aᵢ| − 1) = 2 + 1 + 2 + 3 + 2 + 1 + 3 + 3 = 17.

Every join-irreducible has the form

> j(i, v) := min{ x ∈ Λ : xᵢ ≥ v },

one for each coordinate i and each value v of Aᵢ above that coordinate's minimum, and the minimum exists.

*Proof.* Fix a coordinate i and a value v ∈ Aᵢ above the minimum of Aᵢ. The set Sᵥ := {x ∈ Λ : xᵢ ≥ v} is non-empty, since every value of every alphabet is realised by some cell (Theorem 2 rebuilds Λ from the box and finds every alphabet value present), and it is closed under ∧ by Theorem 1, so it has a least element m := j(i, v), the meet of all its members. Some cell of Λ has i-coordinate exactly v; it lies in Sᵥ, so m lies below it and mᵢ ≤ v; hence mᵢ = v.

m is join-irreducible. It is not the bottom cell, whose i-coordinate is the minimum of Aᵢ, below v; so m covers at least one cell. Suppose m covered two distinct cells a and b. Neither lies below the other, since b < a < m would contradict b ⋖ m; so a < a ∨ b ≤ m, and a ⋖ m forces a ∨ b = m, which lies in Λ by Theorem 1. Then v = mᵢ = max(aᵢ, bᵢ), so one of a, b has i-coordinate v, lies in Sᵥ and is strictly below m — contradicting the minimality of m. So m covers exactly one cell.

Conversely let j be join-irreducible with unique lower cover j⁻. By Theorem 4, j = j⁻ + eᵢ for some coordinate i; put v := jᵢ, which lies above the minimum of Aᵢ because the i-coordinate of j⁻ is v − 1, a value of Aᵢ. Then j ∈ Sᵥ, and j is its least element: let x ∈ Sᵥ and suppose j ≰ x. Then z := j ∧ x lies in Λ, is strictly below j, and has zᵢ = min(jᵢ, xᵢ) = v. Every cell strictly below j lies below some cell that j covers — the last step of a maximal chain from z to j is a cover of j — hence z ≤ j⁻ and zᵢ ≤ v − 1, a contradiction. So j = j(i, v).

The map (i, v) ↦ j(i, v) is injective. Put m = j(i, v); by Theorem 4 its unique lower cover is m − eᵢ′ for some coordinate i′. If i′ ≠ i then (m − eᵢ′)ᵢ = v, so m − eᵢ′ lies in Sᵥ strictly below m, against the minimality of m; hence i′ = i, the unique lower cover of m is m − eᵢ, and i is read off that cover while v is mᵢ. The join-irreducibles are therefore in bijection with the pairs (i, v), and their number is Σᵢ(|Aᵢ| − 1). The meet-irreducible count is computed and equals 17. ∎ **PROVED** for the form and the closed count; **EXHAUSTIVE** for the equality of the two counts (976 cells, both cover sets computed from the order), and the closed count is re-verified at five further cap settings (Theorem 2), where the lower covers are taken as unit steps by Theorem 4.

| letter | generator | rank | weight | forces |
|---|---|---|---|---|
| n ≥ 2 | (2,0,1,0,1,0,0,0) | 4 | 856 | — |
| k ≥ 2 | (1,0,2,0,1,0,0,0) | 4 | 826 | — |
| q ≥ 1 | (1,0,1,1,1,0,0,0) | 4 | 811 | — |
| e ≥ 2 | (1,0,1,0,2,0,0,0) | 4 | 784 | — |
| 2S ≥ 1 | (1,0,1,0,1,0,0,1) | 4 | 657 | — |
| ℓ ≥ 1 | (2,1,1,0,1,0,0,0) | 5 | 616 | n ≥ 2 |
| g ≥ 1 | (1,0,1,1,1,0,1,0) | 5 | 491 | q ≥ 1 |
| n ≥ 3 | (3,0,1,0,1,0,0,0) | 5 | 428 | n ≥ 2 |
| f ≥ 1 | (1,0,1,0,2,1,0,0) | 5 | 400 | e ≥ 2 |
| e ≥ 3 | (1,0,1,0,3,0,0,0) | 5 | 392 | e ≥ 2 |
| q ≥ 2 | (1,0,2,2,1,0,0,0) | 6 | 481 | q ≥ 1, k ≥ 2 |
| 2S ≥ 2 | (1,0,2,0,1,0,0,2) | 6 | 338 | 2S ≥ 1, k ≥ 2 |
| k ≥ 3 | (2,1,3,0,1,0,0,0) | 7 | 376 | k ≥ 2, ℓ ≥ 1 |
| g ≥ 2 | (1,0,2,2,1,0,2,0) | 8 | 171 | g ≥ 1, q ≥ 2 |
| q ≥ 3 | (2,1,3,3,1,0,0,0) | 10 | 136 | q ≥ 2, k ≥ 3 |
| 2S ≥ 3 | (2,1,3,0,1,0,0,3) | 10 | 94 | 2S ≥ 2, k ≥ 3 |
| g ≥ 3 | (2,1,3,3,2,1,3,0) | 15 | 16 | g ≥ 2, q ≥ 3, f ≥ 1 |

: **Table 3 — the seventeen letters.** *rank* is rank(j); *weight* is the number of the 976 cells that lie above j; *forces* lists the letters implied by it (Theorem 8).

The alphabet is not uniform: n ≥ 2 is set in 856 of the 976 cells and g ≥ 3 in sixteen, so one letter carries 87.7% of the object and another 1.6%.

**Theorem 7 (Birkhoff, verified).** Let P be the 17-element poset of join-irreducibles ordered by ≤, and for x ∈ Λ let D(x) := { j ∈ P : j ≤ x }. Then D is a bijection from Λ onto the set of down-sets of P, and D(x ∨ y) = D(x) ∪ D(y), D(x ∧ y) = D(x) ∩ D(y).

*Proof.* Birkhoff's representation theorem (1937), CITED, gives the isomorphism for any finite distributive lattice, and Λ is one by Theorem 3. The instance is verified rather than assumed: all 2¹⁷ = 131,072 subsets of P are tested, exactly 976 are down-sets, the 976 sets D(x) are distinct, and the two operations correspond on all 475,800 pairs with no exception. ∎ **CITED** (the theorem) and **EXHAUSTIVE** (131,072 subsets; 475,800 pairs).

Writing a cell as the 17-bit word of its letters, join is bitwise OR, meet is bitwise AND, and Λ is 976 of the 131,072 available words: 17 bits carried per cell against log₂ 976 = 9.9307 needed to index them, a surplus of 7.0693 bits, and a density of 0.7446% in the space the cells are written in.

**Theorem 8 (twenty implications, and they are the seven bounds again).** P has exactly 20 covering relations. Nine are **within** a coordinate — a letter c ≥ v forces c ≥ v − 1, which is the chain on the alphabet of c — and eleven are **between** coordinates:

> ℓ ≥ 1 → n ≥ 2 · f ≥ 1 → e ≥ 2 · g ≥ 1 → q ≥ 1 · k ≥ 3 → ℓ ≥ 1 · q ≥ 2 → k ≥ 2 · 2S ≥ 2 → k ≥ 2 · g ≥ 2 → q ≥ 2 · q ≥ 3 → k ≥ 3 · 2S ≥ 3 → k ≥ 3 · g ≥ 3 → q ≥ 3 · g ≥ 3 → f ≥ 1.

Each is one way a bound of D2 binds at one value, and those twenty implications alone cut the 131,072 words down to exactly the 976 cells, nothing else being imposed.

*Proof.* The covering relations of P are computed from the order on the seventeen cells. The classification into within and between is by the coordinate each letter names. For the cut: a 17-bit word satisfies all twenty implications if and only if its set of bits is a down-set of P — an implication along a cover is exactly the down-set condition at that cover, and the cover relations generate the order — and by Theorem 7 the down-sets are the cells. The enumeration confirms it directly: of 131,072 words, 976 satisfy the twenty. ∎ **PROVED** and **EXHAUSTIVE** (131,072 words).

![**Figure 3.** The seventeen generators, at their ranks in Λ, with the twenty covering relations: nine within one coordinate (solid) and eleven between coordinates (dashed). The grey number below each generator is the number of the 976 cells lying above it, from 856 at n ≥ 2 to 16 at g ≥ 3. Every cell of Λ is the down-set of generators beneath it, and every down-set is a cell.](figures/fig3-generating-poset.png)

**Corollary 2 (order dimension 7).** The order dimension of Λ is 7 — seven linear extensions realise the order and no six do — although Λ has eight coordinates.

*Proof.* For a finite distributive lattice the order dimension equals the width of its poset of join-irreducibles (Dilworth 1950, CITED; the dimension is that of Dushnik and Miller 1941, and Trotter 1992 is the reference for it). That width is computed to be 7, certified both ways by the same matching argument as Theorem 5. The antichain is {k ≥ 2, q ≥ 1, 2S ≥ 1, n ≥ 3, ℓ ≥ 1, e ≥ 3, f ≥ 1} — one letter from each coordinate except g — and the seven chains are n ≥ 2 < n ≥ 3; k ≥ 2 < q ≥ 2 < q ≥ 3; q ≥ 1 < g ≥ 1 < g ≥ 2; e ≥ 2 < e ≥ 3; 2S ≥ 1 < 2S ≥ 2 < 2S ≥ 3; ℓ ≥ 1 < k ≥ 3; f ≥ 1 < g ≥ 3. Why g contributes nothing: every letter g ≥ v lies above the atom q ≥ 1, because g ≤ q, so no antichain of letters can take a g-letter together with a q-letter below it, and the coordinate q is already represented. The order pays seven dimensions for eight axes. ∎ **CITED** and **EXHAUSTIVE** (the width of a 17-element poset, by exact matching, with both certificates written out).

**Corollary 3 (maximal chains).** Every maximal chain of Λ runs from the bottom cell to the top cell in exactly 17 covering steps, and there are **1,113,045,672** of them.

*Proof.* Under Theorem 7 a covering step adds exactly one generator to the down-set D(x), so a maximal chain from bottom to top lists the seventeen generators in an order in which each appears after everything below it in P — a linear extension of P — and conversely every linear extension gives a maximal chain; this is the standard correspondence for finite distributive lattices (Stanley 2012, CITED). Hence every maximal chain has |P| = 17 steps, which is also rank(top) − rank(bottom) = 20 − 3 by Theorem 4. The number of chains is the number of paths in the cover graph from bottom to top, counted by summing, in rank order, over the lower covers of each cell. ∎ **PROVED** (the correspondence **CITED**) and **EXHAUSTIVE** (the count over all 976 cells).

**Theorem 9 (the reflection).** Let σ(x) := top − x coordinatewise, with top = (3,1,3,3,3,1,3,3). Then σ maps exactly **8** of the 976 cells back into Λ, and σ has **no** fixed point in Λ. The eight are

> (1,0,1,1,1,0,1,1) · (1,0,1,1,2,1,1,1) · (2,1,1,1,1,0,1,1) · (1,0,2,2,1,0,2,2)
> (2,1,1,1,2,1,1,1) · (1,0,2,2,2,1,2,2) · (2,1,2,2,1,0,2,2) · (2,1,2,2,2,1,2,2)

at ranks 6, 8, 8, 10, 10, 12, 12, 14 — all even.

*Proof.* Computation over the 976 cells. That no cell is fixed is immediate as well as computed: σ(x) = x requires 2xᵢ = topᵢ in every coordinate, and top has odd entries (n = 3, k = 3, q = 3, e = 3, g = 3, 2S = 3), so no integer solution exists. The eight all have q = k, g = q and 2S = q, with (n, ℓ) and (e, f) each at (1,0) or (2,1): their source and target halves mirror one another, which is why the reflection returns them to Λ. Since rank(σx) = 20 − rank(x) and 20 is even, σ preserves rank parity, and it permutes the eight within their even ranks. ∎ **PROVED** (no fixed point) and **EXHAUSTIVE** (976 cells).

So Λ is not self-dual, and the failure is by a single witness: the rank sequence read forwards begins 1, 5, 15, 34 and read backwards begins 1, 4, 10, 21. They part at rank 4 and never rejoin. §5 shows this is the same fact as F(−1) = 2.

---

## §3 · The interval metric

**D9 (the prime encoding).** With pᵢ the i-th prime, N(x) is the positive integer whose exponent at pᵢ is xᵢ for every i — the product of the eight prime powers with exponents n, ℓ, k, q, e, f, g and 2S. Then x ≤ y iff N(x) divides N(y), N(x ∨ y) = lcm(N(x), N(y)), N(x ∧ y) = gcd(N(x), N(y)), and rank(x) = Ω(N(x)), the number of prime factors of N(x) with multiplicity. So Λ is a sublattice of the divisor lattice of a single integer.

**D10 (the interval measure).** For x, y ∈ Λ,

> d(x, y) := τ( lcm(N(x), N(y)) / gcd(N(x), N(y)) ),

with τ the divisor-counting function.

**Theorem 10 (five forms).** For all x, y ∈ Λ the following five quantities are equal:

> (1) the number of points of the ambient box in the interval [x ∧ y, x ∨ y];
> (2) ∏ᵢ (|xᵢ − yᵢ| + 1);
> (3) τ( N(x)N(y) / gcd(N(x), N(y))² );
> (4) τ(a·b), where N(x)/N(y) = a/b in lowest terms;
> (5) ∏ₚ (|vₚ(ρ)| + 1), the product over the eight primes, where ρ = N(x)/N(y) and vₚ is the p-adic valuation.

In particular d(x, x) = 1.

*Proof.* Under D9 the exponent of pᵢ in ρ = N(x)/N(y) is exactly xᵢ − yᵢ, so the pᵢ-adic valuation of ρ has absolute value |xᵢ − yᵢ| and (5) = (2). The quotient lcm/gcd has exponent |xᵢ − yᵢ| at pᵢ, so its divisor count is ∏(|xᵢ−yᵢ|+1) and d as defined in D10 equals (2); the same exponent vector arises in (3) and in (4), since cancelling to lowest terms removes exactly the gcd. Finally the box interval [x ∧ y, x ∨ y] is the product of the intervals [min(xᵢ,yᵢ), max(xᵢ,yᵢ)], of lengths |xᵢ − yᵢ| + 1, so (1) = (2). With x = y every factor is 1 and the product is 1: a point has no volume, but it is one point and it counts itself. ∎ **PROVED**, and **EXHAUSTIVE** on all 475,800 pairs, zero disagreements among the five.

**Theorem 11 (d is a multiplicative metric; log d is a metric).** For all x, y, z ∈ Λ: d(x,y) = d(y,x); d(x,y) ≥ 1 with equality iff x = y; and

> d(x, z) ≤ d(x, y) · d(y, z).

Consequently log d is a metric on Λ, and it is the ℓ¹ metric of the per-axis distances log(|Δᵢ| + 1).

*Proof.* Symmetry and d ≥ 1 are immediate from form (2), and d = 1 forces every factor to be 1, hence every |xᵢ − yᵢ| = 0. For the triangle inequality it suffices to prove the one-coordinate statement, for integers a, b, c:

> |a − c| + 1 ≤ (|a − b| + 1)(|b − c| + 1).

Write u = |a − b|, v = |b − c|. The ordinary triangle inequality on ℤ gives |a − c| ≤ u + v, and (u+1)(v+1) = uv + u + v + 1 ≥ u + v + 1 because uv ≥ 0. So |a − c| + 1 ≤ u + v + 1 ≤ (u+1)(v+1). Taking the product over the eight coordinates gives d(x,z) ≤ d(x,y)d(y,z), since each factor on the left is bounded by the product of the corresponding two on the right. Taking logarithms turns the product into a sum and the multiplicative inequality into the additive one, so log d(x,y) = Σᵢ log(|xᵢ − yᵢ| + 1) is a sum of per-axis terms each satisfying the triangle inequality: an ℓ¹ metric — a metric on a poset of the kind surveyed by Monjardet (1981). ∎ **PROVED**; the one-coordinate inequality is **EXHAUSTIVE** over all 289 value triples drawn from the eight alphabets, and a **SAMPLED** sweep of 200,000 cell triples (seed 20260922) found no failure of the multiplicative form.

Two features of the geometry follow from the form and are worth naming. A ball {y : d(x,y) ≤ D} is not a box: in two coordinates its boundary is the hyperbola (1 + Δ₁)(1 + Δ₂) = D. And each axis is a log-distorted chain — the first step costs log 2 = 0.6931 and the tenth costs log(11/10) = 0.0953 — so the measure is sensitive at short range and flat at long range, which is what a *count of cells* does and a difference does not.

![**Figure 4.** The interval measure — the plate's own title calls it the occupancy measure, the same d. (a) A pair of cells spans a box and d counts its points, not its volume. (b) Why d(x,x) = 1: volume vanishes on a degenerate box and a point count never does. (c) Balls are hyperbolic, with boundary (1 + Δ₁)(1 + Δ₂) = D. (d) Each axis is a log-distorted chain: the first step costs log 2 and the tenth log(11/10).](figures/fig4-interval-measure.png)

**Remark.** d measures the *box* between two cells, not the part of it that lies in Λ. The difference is the subject of §4.

---

## §4 · The void, and why it needs no sieve

**D11 (a coordinate box, and the void).** For lo ≤ hi in the ambient box, the **coordinate box** is [lo, hi] := ∏ᵢ [loᵢ, hiᵢ], of size ∣[lo, hi]∣ = ∏ᵢ(hiᵢ − loᵢ + 1), its number of points. For x, y ∈ Λ the **void** is

> void(x, y) := d(x, y) − | [x ∧ y, x ∨ y] ∩ Λ |,

the points of the box between x and y that the bounds exclude.

Lemma 3 of §1 gives the constraint graph; this section uses that it is a tree.

**Theorem 12 (the count factorises, with no inclusion–exclusion).** For every coordinate box [lo, hi], with each coordinate ranging over its interval [loᵢ, hiᵢ] further clipped by the bound written beside it,

> ∣[lo, hi] ∩ Λ∣ = Σ over e of Σ over f ≤ e − 1 of Σ over g ≤ 4f + 2 of Σ over q ≥ g of Σ over k ≥ q of N₂ₛ(k) · Σ over ℓ with k ≤ 4ℓ + 2 of Nₙ(ℓ),

where the two leaves are intervals clipped by their one bound,

> N₂ₛ(k) = max(0, min(hi₈, k) − lo₈ + 1),  Nₙ(ℓ) = max(0, hi₁ − max(lo₁, ℓ + 1) + 1).

Every partial sum in the display — read from the inside out, the coordinates are eliminated in the order 2S, n, ℓ, k, q, g, f, e — is a function of a **single** coordinate, and no term is subtracted.

*Proof.* Write the count as a sum over the box of a product of seven indicator factors, one per edge:

> |[lo, hi] ∩ Λ| = Σ over z ∈ [lo, hi] of ∏ over edges (i, j) of [ zᵢ ≤ φᵢⱼ(zⱼ) ].

Because G is a tree, it always has a leaf. Summing out a leaf coordinate touches only the single factor on its one edge, and produces a quantity that depends on the leaf's neighbour alone; deleting the leaf leaves a smaller tree, which again has a leaf. Iterating eight times consumes every coordinate, and at no step does any intermediate depend on two coordinates — the variable elimination of graphical models along a tree (Lauritzen 1996, CITED). Explicitly for Λ: 2S is a leaf at k and n a leaf at ℓ, and summing them out gives N₂ₛ(k) and Nₙ(ℓ), each an interval clipped by its one bound and each a function of one neighbour; then ℓ, k, q, g and f are eliminated in turn, each the leaf of what remains — ℓ into a function of k, k into a function of q, q into a function of g, g into a function of f, f into a function of e — and the last sum is over e. That is the display, and every partial sum in it has one argument. The single-argument property belongs to a leaf order: were g eliminated while q and f were both still live, its partial sum max(0, min(hi₇, q, 4f + 2) − lo₇ + 1) would depend on both, g being the one coordinate with two bounds. The count is the same in every order, because a tree has no cycle: no configuration is counted twice and no correction term arises. ∎ **PROVED**, and **EXHAUSTIVE**: the elimination is compared with direct enumeration on **every one of the 1,944,000 coordinate boxes of the ambient box**, with zero disagreements.

The converse is the content of the statement. A constraint graph has induced width 1 if and only if it is a forest (Freuder 1982), CITED; with a cycle present, some elimination order must produce an intermediate in two coordinates, and the route back to single-coordinate counts is a Möbius sieve over the cycle's constraints, alternating in sign. An index whose constraint graph is a tree has its box counts in closed form; one with a cycle does not.

**Theorem 13 (containment in seven comparisons).** A coordinate box lies entirely inside Λ if and only if, for each of the seven bounds xᵢ ≤ φ(xⱼ),

> hiᵢ ≤ φ(loⱼ).

*Proof.* (⇐) Let lo ≤ w ≤ hi. For each bound, wᵢ ≤ hiᵢ ≤ φ(loⱼ) ≤ φ(wⱼ) by monotonicity, since loⱼ ≤ wⱼ. The floors and caps hold because lo and hi are in the ambient box and w lies between them. So w ∈ Λ. (⇒) Suppose some bound has hiᵢ > φ(loⱼ). The point w with wᵢ = hiᵢ, wⱼ = loⱼ and wₘ = loₘ elsewhere lies in [lo, hi] and violates that bound, so it is not in Λ. ∎ **PROVED**; the sufficient direction is **MACHINE-CHECKED** with lo, hi, the test point and all five caps as integer variables (`unsat` under negation), and the equivalence is **EXHAUSTIVE** on the same 1,944,000 coordinate boxes.

**Proposition 1 (how much of the void there is, and that the seven events are positively dependent).** Over all 475,800 unordered pairs of distinct cells, the box [x ∧ y, x ∨ y] lies wholly inside Λ for **134,871** of them — a void-free fraction of **0.2835**. Among the 115,162 strictly comparable pairs, whose box is the interval [x, y], it lies inside Λ for **31,604**, a fraction of 0.2744. The seven individual containment events of Theorem 13 hold at rates from **0.6995** (g ≤ q) to **0.9806** (g ≤ 4f + 2); their product, which is what independence would give, is **0.2013**. The joint rate exceeds it by a factor of **1.4081**.

*Proof.* Direct computation of all seven indicators and the joint event on every pair. ∎ **EXHAUSTIVE** (475,800 pairs; 115,162 comparable pairs). A heuristic reading of the direction, not measured here: each comparison hiᵢ ≤ φ(loⱼ) is a *narrowness* condition on the coordinates it touches — it holds when the box is thin in those coordinates and fails as they widen — so two comparisons sharing a coordinate tend to hold together, and comparisons sharing no coordinate contribute no such term. This paper measures the size of the lift and neither decomposes nor explains it.

![**Figure 5.** (a) What each bound removes on its own: the ambient points that satisfy the other six and fail only this one, from 673 for g ≤ q down to 24 for g ≤ 4f + 2. Every entry is positive, so no bound is redundant. (b) The seven containment events of Theorem 13 over all 475,800 pairs, their product 0.2013 and the joint rate 0.2835 — a lift of 1.4081.](figures/fig5-void.png)

---

## §5 · The single expression

**D12 (the rank polynomial).** F(z) := Σᵣ aᵣ zʳ, where aᵣ is the number of cells of rank r — an integer polynomial, the sum over the cells of z raised to the rank.

**Theorem 14 (Λ is one nested sum).** At the caps of D3,

> F(z) = Σ over n = 1..3 of zⁿ · Σ over ℓ = 0..min(1, n−1) of zˡ · Σ over k = 1..min(3, 4ℓ+2) of zᵏ  
> · [ Σ over 2S = 0..min(3, k) of z²ˢ ] · Σ over q = 0..min(3, k) of z<sup>q</sup>  
> · Σ over e = 1..3 of zᵉ · Σ over f = 0..min(1, e−1) of zᶠ · Σ over g = 0..min(3, q, 4f+2) of zᵍ,

and this equals D12 coefficient by coefficient. Setting every exponent variable separately, the same nesting in eight variables z₁,…,z₈ has the property that the coefficient of z₁ⁿ ⋯ z₈²ˢ is 1 if that cell is in Λ and 0 if it is not: the coefficient function of the expression *is* the membership predicate.

*Proof.* The nesting is the elimination order of Theorem 12 read as a generating function rather than a count: each variable's range is the interval its bounds leave given the variables already fixed, and because the constraint graph is a tree those ranges depend on one earlier variable each — except g, whose range depends on q and f, which is why exactly one bracket in the display carries a min of two arguments. The sum therefore enumerates every admissible tuple once and no other tuple, so its coefficient of zʳ is the number of cells of rank r, and in the eight-variable form its coefficient at a monomial is the indicator of that cell. ∎ **PROVED**, and **EXHAUSTIVE**: the nested form and the direct sum agree at every rank 3 to 20, in exact integer arithmetic.

> F(z) = z³ + 5z⁴ + 15z⁵ + 34z⁶ + 59z⁷ + 87z⁸ + 108z⁹ + 121z¹⁰ + 122z¹¹ + 115z¹² + 100z¹³ + 79z¹⁴ + 57z¹⁵ + 37z¹⁶ + 21z¹⁷ + 10z¹⁸ + 4z¹⁹ + z²⁰.

**Corollary 4 (the three specialisations).** F(1) = 976; F(−1) = 2; F′(1)/F(1) = 10801/976 = 11.0666…, the mean rank, which sits 0.4334 below the midpoint 11.5 of the rank range.

*Proof.* Exact integer and rational evaluation of the coefficient list. ∎ **EXHAUSTIVE**, exact.

**Lemma 4 (the detachable leaf).** 2S appears in exactly one bound, so its sum closes geometrically and multiplies out:

> Σ over 2S = 0..k of z²ˢ = (1 − zᵏ⁺¹) / (1 − z).

Removing 2S projects Λ onto a set of **319** seven-coordinate cells (n, ℓ, k, q, e, f, g); each of them carries exactly k + 1 values of 2S, so that Σ (k + 1) over the 319 is 976; and the projection is itself closed, with defect 0.

*Proof.* The finite geometric series, for z ≠ 1. The bound on 2S is 2S ≤ k alone, and k ≤ 3 is the cap on 2S as well, so above a fixed seven-coordinate cell the admissible values of 2S are exactly 0, 1, …, k, which is k + 1 of them; the projection is closed under ∨ and ∧ because these act coordinatewise and dropping a coordinate commutes with them, and its staircase closure is computed and returns it. ∎ **PROVED**; the identity is verified in exact rational arithmetic at 60 points — six degrees k = 0..5 against ten distinct rationals — which exceeds the degree in the one variable, so a rational function agreeing there agrees identically; the projection, its 319 cells, the k + 1 spins over each and its defect 0 are **EXHAUSTIVE**.

Spin multiplicity is algebraically inert here: it scales the count of each seven-coordinate cell by k + 1 and changes no structure, which is what a leaf of a tree does.

**Theorem 15 (why F(−1) = 2, and why it is not 0).** At the caps of D3, let Φ(z) := ∏ᵢ (Σ over v ∈ Aᵢ of zᵛ) be the rank polynomial of the ambient box. Then Φ(1) = 6,912 and **Φ(−1) = 0**. The residue F(−1) = 2 is therefore created by the bounds and not inherited from the box; it is carried entirely by the cells with k = 2.

*Proof.* A coordinate whose alphabet is a run of consecutive integers of **even** length contributes Σ(−1)ᵛ = 0 to the product. Five of the eight alphabets have even size — ℓ and f with two values each, and q, g and 2S with four each — so Φ(−1) = 0, five times over. If the coordinates were free the alternating sum would vanish. They are not free: ℓ is clipped by n, f by e, k by ℓ, q by k, g by q and by f, and 2S by k, so no vanishing factor ever appears on its own and the elimination of Theorem 12 at z = −1 leaves a residue. Splitting that residue by the source occupancy gives 0 at k = 1, **+2** at k = 2 and 0 at k = 3. The mechanism is Lemma 4: the spin factor at z = −1 is Σ over 2S = 0..k of (−1)²ˢ, which is 1 for k even and 0 for k odd, so every cell with odd k cancels against its own spin sum, and the whole of F(−1) lives on the k = 2 cells. ∎ **PROVED** and **EXHAUSTIVE** (the box polynomial Φ and the split by k, exact integers).

**Corollary 5 (F is not palindromic, and that is Theorem 9 again).** A graded poset is self-dual only if its rank polynomial is palindromic. Read forwards the coefficients begin 1, 5, 15, 34, 59, 87; read backwards they begin 1, 4, 10, 21, 37, 57. They part at rank 4 — five against four — and never rejoin. So Λ admits no rank-reversing automorphism, of which Theorem 9's reflection is one instance: that theorem exhibits the eight cells the reflection returns and the zero it fixes.

*Proof.* Comparison of the coefficient list with its reverse; the first index at which they differ is computed. ∎ **EXHAUSTIVE.**

![**Figure 6.** F(z) read forwards as bars and backwards as the dashed line. They part company at the second level — 5 against 4 — and never rejoin. A rank polynomial is palindromic if and only if the poset is self-dual, so this one picture carries both the asymmetry of the rank sequence and the failure of the reflection.](figures/fig6-rank-polynomial.png)

![**Figure 7.** The constraint graph read in the nesting order of Theorem 14 — n, ℓ, k, 2S, q, e, f, g — a path of seven with one pendant. An arrow runs from a coordinate to one whose range it bounds, and the two Pauli bounds k ≤ 4ℓ + 2 and g ≤ 4f + 2 are marked. That shape is why a single nesting exists with one bracketed factor. The pendant 2S factors out as a geometric sum (Lemma 4); g is the only coordinate with two parents, and the min it forces — g ≤ min(q, 4f + 2) — is the one non-product term in the whole expression.](figures/fig7-caterpillar.png)

---

## §6 · The Möbius function

**D13 (the Möbius function).** For x ≤ y in Λ, μ(x, x) := 1 and μ(x, y) := −Σ μ(x, z), the sum over x ≤ z < y.

**Theorem 16 (closed form).** For x ≤ y in Λ, write Q := D(y) ∖ D(x) for the set of generators added (D of Theorem 7). Then

> μ(x, y) = (−1)ᵐ with m = |Q| if Q is an antichain in P, and 0 otherwise.

*Proof.* By Theorem 7 the interval [x, y] of Λ is isomorphic to the interval [D(x), D(y)] of down-sets of P, which is isomorphic to the lattice 𝒪(Q) of down-sets of the induced subposet on Q: a down-set of P between D(x) and D(y) is D(x) together with a down-set of Q, and the correspondence is an order isomorphism.

If Q is an antichain, every subset of Q is a down-set, so 𝒪(Q) is the Boolean lattice of all subsets of Q, whose Möbius value from bottom to top is (−1)ᵐ.

If Q is not an antichain, the atoms of 𝒪(Q) are the principal down-sets {m} of the elements m minimal in Q, and their join is the set of minimal elements of Q. Since Q is not an antichain some element of Q lies strictly above a minimal one, so that set is a proper subset of Q: the join of the atoms is not the top. Joins are monotone, so no subset of the atoms joins to the top either. By the corollary of the crosscut theorem — in a finite lattice, if 1̂ is not a join of atoms then μ(0̂, 1̂) = 0 (Rota 1964, the corollary to his Theorem 3; Stanley 2012, Corollary 3.9.5), CITED — μ(0̂, 1̂) = 0 in 𝒪(Q), and hence μ(x, y) = 0. The closed form is the textbook Möbius function of a finite distributive lattice (Stanley 2012, §3.9); what this paper adds is the instance, verified below. ∎ **PROVED** (using Birkhoff, CITED, and Rota, CITED).

**Verification.** The closed form is substituted into the defining recursion of D13 and the identity Σ μ(x, z) over x ≤ z ≤ y equals 1 when x = y and 0 otherwise is tested on **all 116,138 comparable pairs** of Λ — 115,162 strict and 976 with x = y — with **zero** violations. Every value is in {−1, 0, +1}. Separately, the crosscut step of the proof is checked directly on all 24,164 distinct intervals that occur: the join of the atoms equals the top exactly when Q is an antichain, and exactly then is the interval Boolean, of size 2 to the |Q|. **EXHAUSTIVE**, both.

**Corollary 6 (the Möbius function in coordinates, and against arithmetic).** For x ≤ y in Λ, μ(x, y) ≠ 0 if and only if every yᵢ − xᵢ ≤ 1 and the coordinate box [x, y] lies inside Λ; and then μ(x, y) = (−1)ᵐ with m = rank(y) − rank(x). Consequently, with μℤ the number-theoretic Möbius function and N the encoding of D9, μ(x, y) = μℤ(N(y)/N(x)) for every comparable pair except those whose box [x, y] is a unit hypercube not contained in Λ, where μℤ is ±1 and μ is 0.

*Proof.* Write Q = D(y) ∖ D(x) and m = rank(y) − rank(x); by Theorem 7 and Theorem 4, |Q| = m, since each covering step adds one generator and raises rank by one. By Theorem 16, μ(x, y) ≠ 0 iff Q is an antichain, iff the interval [x, y] of Λ is the Boolean lattice of all subsets of Q — for if a < b in Q then {b} is a subset of Q that is not a down-set, so 𝒪(Q) has fewer than 2ᵐ elements, while an antichain has all of them. Suppose the interval is Boolean. Its atoms are the cells covering x, each of the form x + eᵢ by Theorem 4, and distinct atoms use distinct coordinates; the top y is the join of the atoms, which is coordinatewise maximum, so y − x is the sum of eᵢ over a set I of m coordinates and every yᵢ − xᵢ ≤ 1. The Boolean lattice has 2ᵐ elements, all in [x, y] ∩ Λ, and the coordinate box [x, y] has exactly 2ᵐ points, so the box lies inside Λ. Conversely, if every yᵢ − xᵢ ≤ 1 and the box lies inside Λ, then [x, y] ∩ Λ is the whole box, a Boolean lattice of rank m, so Q is an antichain and μ = (−1)ᵐ. For the arithmetic statement: N(y)/N(x) has exponent yᵢ − xᵢ at pᵢ, so it is squarefree iff every yᵢ − xᵢ ≤ 1, and then μℤ of it is (−1)ᵐ, otherwise 0. So the two functions agree wherever the box is not a unit hypercube (both 0) and on every void-free unit hypercube (both (−1)ᵐ), and differ exactly on unit hypercubes with a void. ∎ **PROVED**, and **EXHAUSTIVE** on all 116,138 comparable pairs: μ is non-zero on 19,079 of them, exactly the void-free unit hypercubes; it agrees with μℤ on 99,034 and differs on 17,104, every one a unit hypercube with a void.

Whether the box [x, y] lies inside Λ is the seven comparisons of Theorem 13, so μ(x, y) is decided by fifteen comparisons of coordinates — the seven of Theorem 13 and the eight unit tests yᵢ − xᵢ ≤ 1 — and one parity: no recursion and no poset.

**Remark.** The practical content is that no recursion is needed. A 976-element lattice has 116,138 comparable pairs, and every Möbius value among them is read off a 17-element poset by one antichain test on at most 17 elements, or, by Corollary 6, off the coordinates alone.

---

## §7 · The seed

**D14 (a seed).** G ⊆ Λ is a **seed** of Λ when ℛ(G) = Λ, with ℛ the staircase closure of D7 taken over G's own box. seed(Λ) is the least |G| over all seeds.

**Theorem 17 (generating is covering).** At any cap setting at which E(Λ) = 0 — the six of Theorem 2 among them — G ⊆ Λ is a seed of Λ if and only if

> (a) for every coordinate i and every value v ∈ Aᵢ(Λ), some cell of G has xᵢ = v, and
> (b) for every ordered pair i ≠ j and every a ∈ Aⱼ(Λ), some cell y ∈ G has yⱼ ≤ a and yᵢ = φ̂ᵢⱼ(a; Λ).

*Proof.* (⇒) Suppose ℛ(G) = Λ. ℛ(G) sits inside G's own box, so G realises every value Λ does, which is (a). For (b): φ̂ᵢⱼ(a; G) ≤ φ̂ᵢⱼ(a; Λ) always, since G ⊆ Λ; if the inequality were strict at some (i, j, a) then the cell z of Λ attaining φ̂ᵢⱼ(a; Λ) — with zⱼ ≤ a and zᵢ = φ̂ᵢⱼ(a; Λ) > φ̂ᵢⱼ(a; G) ≥ φ̂ᵢⱼ(zⱼ; G), the last step by monotonicity of the envelope in its argument — would fail G's own bound and so lie outside ℛ(G), contradicting ℛ(G) = Λ.
(⇐) Under (a) and (b), G and Λ have the same box and the same envelopes, and ℛ depends on its argument only through those two; so ℛ(G) = ℛ(Λ), which is Λ because E(Λ) = 0 — Theorem 2, at the caps of D3. ∎ **PROVED**; and **SAMPLED** in both directions: on 80 random subsets of sizes 4 to 10 (seed 20260923), none of which is a cover, none closes; and 40 of the 24,585 minimum covers of Theorem 18 (seed 20260924) all close (§9).

So seed(Λ) is a **minimum set cover**: the elements to cover are the **alphabet slots** of (a) and the **envelope steps** of (b), and a cell covers the elements it witnesses. Because each φ̂ᵢⱼ is non-decreasing in a, it is a step function, and only the least argument realising each of its values needs covering — the running maximum is constant between steps. Counting them gives **102 elements**: 25 alphabet slots and 77 envelope steps, against 976 sets.

**Theorem 18 (seed(Λ) = 7).** At the caps of D3, seed(Λ) = 7. There are exactly **24,585** minimum seeds. Exactly **one** cell — (2,1,3,3,2,1,3,0), which is the generator g ≥ 3 — lies in all of them, and **no** element of the 102 is witnessed by a unique cell: the smallest witness set has four.

*Proof.* By Theorem 17 the problem is exactly minimum set cover, which is NP-hard in general — its decision version is NP-complete (Karp 1972), CITED — so the search must be exact rather than heuristic and must be shown exhaustive. Three steps.

*Reduction.* If the witness set of element e₁ contains the witness set of e₂, then any cover of e₂ covers e₁ and e₁ may be discarded without changing which subsets are covers — so the reduction preserves both the minimum and the *set* of minimum covers. Applying it leaves **27** critical elements. Grouping the 976 cells by which of the 27 they witness leaves **245** distinct signatures; two cells with the same signature are interchangeable in any cover, so covers are enumerated over signatures and each is expanded by the product of its multiplicities.

*Lower bound.* If a family of elements has pairwise disjoint witness sets, then every cover needs a distinct set for each, so the size of such a family is a lower bound. A greedy pass over the 27 critical elements, smallest witness set first, exhibits **5** pairwise disjoint ones; so seed(Λ) ≥ 5.

*Exhaustiveness.* The search branches on an **uncovered element**: at every node it picks one element not yet covered and recurses once on each signature that witnesses it. Every cover must contain at least one such signature, so no cover is missed and the enumeration is complete; the branch is cut when the current depth plus the disjoint-element bound on the elements still uncovered exceeds the limit, which discards only branches that cannot reach a cover within the limit. Run at limits 1 through 6 the search returns nothing, so no seed of six cells exists; run at limit 7 it returns 13,468 signature-covers, which expand to **24,585** covers by cells. One cell lies in every one of them; and scanning the 102 elements, none has a witness set of size 1, the smallest having 4. ∎ **EXHAUSTIVE** (the search visits every case; the limits 1 to 7 are all run) and **CITED** (Karp).

**Remark on what the seed is not.** The greedy heuristic for set cover (Johnson 1974; Chvátal 1979) certifies an upper bound and nothing else, which is why the search above is exact. The elementary rule that puts a set in every minimum cover — that it is the only witness of some element — applies to nothing here: every element of the 102 is witnessed by at least four cells, and yet one cell is in all 24,585 minimum covers. What can be said locally is this: the cell witnesses 26 of the 102 elements, no one or two of those single it out, and three do — the slots n = 2 and e = 2, with 428 and 392 witnesses, and the step "g at 2S ≤ 0", whose value 3 has four witnesses, meet in exactly this cell. A minimum seed that omits it must therefore spend at least two cells on those three elements; that no seed of seven can afford to is what the enumeration shows, and this paper does not reduce that to a local certificate. The complement of the statement is also measured: **370** of the 976 cells appear in at least one minimum cover, the median such cell appears in 59 of them — 0.24% — and the distribution is heavy-tailed, the second-most-common cell appearing in 14,492, or 58.9%.

**Corollary 7 (what every seed contains).** Every seed of Λ — minimum or not — contains a cell with q = 0 (a null transition), a cell with q = k for each k ∈ {1, 2, 3} (a full transfer at every occupancy), a cell with (ℓ, f) = (0, 1), one with (ℓ, f) = (1, 0) and one with (ℓ, f) = (1, 1) — the channels s → p, p → s and p → p. An s → s cell, (ℓ, f) = (0, 0), is not forced: it appears in 17,403 of the 24,585 minimum seeds.

*Proof.* By Theorem 17 a seed covers every alphabet slot and every envelope step. The slot q = 0 needs a cell with q = 0. For the ordered pair (i, j) = (q, k), the envelope at a is the largest q among cells with k ≤ a, which is a for a = 1, 2, 3; so every a is a step, and a cell covering it has k ≤ a and q = a, hence q = k = a, since q ≤ k. For the pair (f, ℓ) at a = 0, the envelope is the largest f among cells with ℓ = 0, which is 1, attained by (1,0,1,0,2,1,0,0); 0 is the least argument and so a step, and a cell covering it has ℓ = 0 and f = 1. For the pair (ℓ, f) at a = 0 the envelope is 1 likewise, and a covering cell has f = 0 and ℓ = 1. The slot g = 3 needs a cell with g = 3, and then q = 3 by g ≤ q, k = 3 by q ≤ k, ℓ = 1 because k ≤ 4ℓ + 2 fails at ℓ = 0, and f = 1 because g ≤ 4f + 2 fails at f = 0: a p → p cell. The count for s → s is computed over all 24,585 minimum seeds. ∎ **PROVED**, and **EXHAUSTIVE** over the 24,585 minimum seeds, where each forced kind — the null transition, q = k at each of k = 1, 2, 3, and the three channels — appears in 24,585 of 24,585.

**Corollary 8 (no cell is removable).** For every cell x ∈ Λ, ℛ(Λ ∖ {x}) = Λ.

*Proof.* By Theorem 17, ℛ(Λ ∖ {x}) = Λ if and only if Λ ∖ {x} covers every element, that is, if and only if no element is witnessed by x alone; and by Theorem 18 every witness set has at least four cells. ∎ **PROVED** from Theorem 18's count, and **EXHAUSTIVE** directly: all 976 deletions are run through the closure operator and every one returns Λ.

So every cell of Λ is implied by the other 975. In the language of convex geometries — closure spaces in which every closed set is the hull of its extreme points (Edelman and Jamison 1985) — ℛ on Λ has no extreme point at all, and the seed of seven is as far from a unique generating set as it could be, which is what lets 24,585 minimum seeds coexist.

The compression is the headline. 976 cells are recoverable from 7 of them, a ratio of 139 to 1; the disjoint-witness bound certifies 5 and the search closes the gap to 7. Against the seventeen join-irreducibles of §2 the seed is smaller, and for a stated reason: ℛ fills a box up to its envelopes, where the lattice join reaches only the down-set of what it is given, so the staircase closure is the stronger operator and needs less to start from.

![**Figure 8.** (a) The 370 of 976 cells that appear in at least one minimum seed, ordered by how many of the 24,585 seeds hold them; the scale is logarithmic and one cell sits at 100%. (b) The same as a distribution: the median cell appears in 0.24% of the minimum seeds and one in all of them.](figures/fig8-seed.png)

---

## §8 · What this index is an instance of

The properties established here are not properties of atoms. Every one of them was derived from the *shape* of the constraint system and not from its content: that each bound is monotone, that each names two coordinates, and that the resulting graph has no cycle. Monotonicity gives closure (Theorem 1, and Lemma 1 with the bounding function uninterpreted); two coordinates per bound give a graph; the absence of cycles gives the product form of the count (Theorem 12), the single nested expression (Theorem 14), and the containment test in seven comparisons (Theorem 13). Distributivity, modularity, the Birkhoff correspondence and the closed-form Möbius function then follow from being a sublattice of a product of chains. The companion paper on the closure law (Lach 2026) takes that observation as its subject: it asks which sets are fixed points of the staircase closure, what the defect E(X) measures when they are not, and which constraint forms can and cannot appear in a system whose admissible set is closed. Λ is that paper's worked instance and this one is its measurement — an index that closes exactly, whose defect is zero at the stated caps and at the five further settings named in Theorem 2, and whose every structural feature is traceable to one of the three shape facts above. The physics chose the seven bounds; the shape of those bounds chose everything else.

---

## §9 · Verification record

Every number printed above is recomputed by the accompanying checks, which discharge **77 rows, 0 failures** — 5 guards, 5 machine-checked obligations, 54 exhaustive families, 4 seeded samples and 9 citations — in about a minute, and a separate pass adds six negative controls, all refuted. The object under test is the same construction throughout, imported rather than restated; the reference implementations used by the guards are written independently; the solver is Z3 (de Moura and Bjørner 2008).

**Which results carry a written proof.** PROVED, with every step in the text: Theorems 1, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16 and 17, Lemmas 1, 2, 3 and 4, Corollaries 3, 6, 7 and 8, and the no-fixed-point half of Theorem 9. CITED where a theorem of the literature is used and not reproved: Birkhoff's representation (Theorem 7), that a sublattice of a distributive lattice is distributive and that rank modularity characterises modular lattices (Theorems 3 and 4), Dilworth's theorem with König's and Fulkerson's reduction, the Hopcroft–Karp algorithm and Stanley's log-concavity criterion (Theorem 5), Dilworth's dimension theorem (Corollary 2), the linear-extension correspondence (Corollary 3), Freuder's width criterion (the converse remark after Theorem 12), the corollary of Rota's crosscut theorem (Theorem 16) and Karp's NP-completeness of set cover (Theorem 18). Everything else — every count — is EXHAUSTIVE, with its family in the table below, or SAMPLED with its size and seed. The table lists every row the check prints, under the check's own label and in the check's own order, transliterated to Unicode where the check writes ASCII (Lambda → Λ, Moebius → Möbius, König, ≤, ≥, →, and the bar ∣).

| obligation, as the check labels it | status | family, box, witness or value, as the check prints it |
|---|---|---|
| non-vacuity, integer obligation | GUARD | hypothesis satisfiable with two distinct cells and caps ≥ 3: sat |
| non-vacuity, monotone-bound obligation | GUARD | a monotone φ with two distinct admissible pairs exists: sat |
| non-vacuity, subset obligation | GUARD | a PROPER non-empty fixed point of R exists in the 3x3x3 box: True |
| encoding fidelity, membership | GUARD | 7312 cases compared, 0 disagreements, 0 skipped |
| encoding fidelity, staircase | GUARD | 1352 cells compared against the closure operator under test, 0 disagreements, 0 skipped |
| Theorem 1, Λ is a sublattice | MACHINE-CHECKED | all 21 variables INTEGER (5 caps, 2 cells of 8): unsat |
| Lemma 1, one monotone bound is closed | MACHINE-CHECKED | φ uninterpreted, monotone; a,b INTEGER: unsat |
| Theorem 13, seven comparisons suffice | MACHINE-CHECKED | lo, hi, w and 5 caps all INTEGER: unsat |
| Lemma 2, E(X) = 0 implies X is a sublattice | MACHINE-CHECKED | every one of 2⁹ subsets of the 3x3 box: unsat |
| Lemma 2, E(X) = 0 implies X is a sublattice | MACHINE-CHECKED | every one of 2²⁷ subsets of the 3x3x3 box: unsat |
| Theorem 2, ∣Λ∣ = 976 | EXHAUSTIVE | the construction and a fresh sieve of all 6912 box points agree: 976 cells, 14.12% of the box |
| Theorem 2, the cell list, both directions | EXHAUSTIVE | 976 rows; rebuilt-not-printed 0, printed-not-rebuilt 0, order identical: True |
| Table 2, no bound is redundant | EXHAUSTIVE | marginal exclusions l ≤ n-1: 308, k ≤ 4l+2: 564, q ≤ k: 575, f ≤ e-1: 200, g ≤ 4f+2: 24, g ≤ q: 673, 2S ≤ k: 300, k ≥ 1: 25 over the 9216 points of the box extended to k = 0 |
| Corollary 1, the one coupling | EXHAUSTIVE | drop the Pauli half: 1000 cells, the 24 lost all have f = 0 and g = 3 |
| D1, electrons moved | EXHAUSTIVE | q = 0: 165 cells, q = 1: 330 cells, q = 2: 345 cells, q = 3: 136 cells; 481 of 976 move two or three electrons |
| D1, the model of a cell | EXHAUSTIVE | g = q (every removed electron placed) in 461 cells, g < q (removed and not placed) in 515, g = 0 in 485; source and target the same subshell, (n, l) = (e, f), in 200 |
| Table 1, the spin envelope | EXHAUSTIVE | 2S ≤ k admits 503 of the 976 cells whose 2S no k-electron configuration carries: 413 with 2S of the wrong parity (2S ≠ k mod 2), 180 above the particle-hole bound 2S ≤ 4l+2-k, 90 both; the 473 physical spin labels are 48.5% of Λ |
| Theorems 2 and 6, further cap settings | EXHAUSTIVE | 22121: 216 cells, E = 0, 11 join-irreducibles (lower covers as unit steps, by Theorem 4) = the sum over i of (∣Ai∣ - 1) = 11; 33141: 1636 cells, E = 0, 21 join-irreducibles (lower covers as unit steps, by Theorem 4) = the sum over i of (∣Ai∣ - 1) = 21; 43141: 2394 cells, E = 0, 22 join-irreducibles (lower covers as unit steps, by Theorem 4) = the sum over i of (∣Ai∣ - 1) = 22; 44241: 5157 cells, E = 0, 24 join-irreducibles (lower covers as unit steps, by Theorem 4) = the sum over i of (∣Ai∣ - 1) = 24; 44262: 19109 cells, E = 0, 33 join-irreducibles (lower covers as unit steps, by Theorem 4) = the sum over i of (∣Ai∣ - 1) = 33 |
| Theorem 2, E(Λ) = 0 | EXHAUSTIVE | the staircase closure returns 976 cells, defect 0, set equality True |
| Theorem 2, R is idempotent on Λ | EXHAUSTIVE | a second application changes nothing: True |
| Theorem 1, closure on every pair | EXHAUSTIVE | all 475800 unordered pairs: 0 escapes under join or meet |
| Theorem 4, rank is modular | EXHAUSTIVE | all 475800 pairs: 0 violations of rank(a ∨ b) + rank(a ∧ b) = rank a + rank b |
| Theorem 3, the chain identity | EXHAUSTIVE | 289 coordinate triples over the eight alphabets: 0 failures |
| Theorem 3, distributivity on cell triples | SAMPLED | 200000 of the 929714176 ordered cell triples (976 cubed), seed 20260921: 0 failures |
| Theorem 4, Λ is graded | EXHAUSTIVE | 3749 cover relations found from the order alone (x < y with no cell between); 3749 of them are unit steps, y - x a unit vector, and 3749 raise rank by 1; bottom 10101000 rank 3, top 31333133 rank 20 |
| Theorem 5, Λ is Sperner | EXHAUSTIVE | largest antichain 122 (maximum matching 854, minimum chain cover 122) = largest rank level 122 at rank 11; the rank sequence is log-concave: True |
| Theorem 6, seventeen irreducibles | EXHAUSTIVE | 17 join-irreducible, 17 meet-irreducible, the sum over i of (∣Ai∣ - 1) = 17, and every join-irreducible is min{x : x[c] ≥ v} |
| Table 3, the seventeen letters | EXHAUSTIVE | n ≥ 2 at rank 4 in 856 cells; k ≥ 2 at rank 4 in 826 cells; q ≥ 1 at rank 4 in 811 cells; e ≥ 2 at rank 4 in 784 cells; 2S ≥ 1 at rank 4 in 657 cells; n ≥ 3 at rank 5 in 428 cells; l ≥ 1 at rank 5 in 616 cells; e ≥ 3 at rank 5 in 392 cells; f ≥ 1 at rank 5 in 400 cells; g ≥ 1 at rank 5 in 491 cells; q ≥ 2 at rank 6 in 481 cells; 2S ≥ 2 at rank 6 in 338 cells; k ≥ 3 at rank 7 in 376 cells; g ≥ 2 at rank 8 in 171 cells; q ≥ 3 at rank 10 in 136 cells; 2S ≥ 3 at rank 10 in 94 cells; g ≥ 3 at rank 15 in 16 cells; the heaviest letter carries 87.7% of the cells and the lightest 1.6% |
| Theorem 7, the Birkhoff correspondence | EXHAUSTIVE | all 2¹⁷ = 131072 subsets tested: 976 are down-sets; cell → down-set is a bijection onto them |
| Theorem 7, join is OR and meet is AND | EXHAUSTIVE | all 475800 pairs, both operations: 0 failures |
| Theorem 8, twenty implications | EXHAUSTIVE | 20 covering relations in the generating poset: 9 within a coordinate, 11 between |
| Theorem 8, the twenty implications written out | EXHAUSTIVE | n ≥ 3 → n ≥ 2; l ≥ 1 → n ≥ 2; q ≥ 2 → k ≥ 2; 2S ≥ 2 → k ≥ 2; k ≥ 3 → k ≥ 2; g ≥ 1 → q ≥ 1; q ≥ 2 → q ≥ 1; e ≥ 3 → e ≥ 2; f ≥ 1 → e ≥ 2; 2S ≥ 2 → 2S ≥ 1; k ≥ 3 → l ≥ 1; g ≥ 3 → f ≥ 1; g ≥ 2 → g ≥ 1; g ≥ 2 → q ≥ 2; q ≥ 3 → q ≥ 2; 2S ≥ 3 → 2S ≥ 2; q ≥ 3 → k ≥ 3; 2S ≥ 3 → k ≥ 3; g ≥ 3 → g ≥ 2; g ≥ 3 → q ≥ 3 |
| Theorem 8, the twenty implications cut the space | EXHAUSTIVE | of 131072 seventeen-bit words, 976 satisfy all twenty and nothing else is imposed |
| Corollary 2, order dimension 7 | EXHAUSTIVE | the generating poset has width 7, certified by a chain partition of the same size |
| Corollary 2, the two certificates | EXHAUSTIVE | antichain {k ≥ 2, q ≥ 1, 2S ≥ 1, n ≥ 3, l ≥ 1, e ≥ 3, f ≥ 1}; chains n ≥ 2 < n ≥ 3 ∣ k ≥ 2 < q ≥ 2 < q ≥ 3 ∣ q ≥ 1 < g ≥ 1 < g ≥ 2 ∣ e ≥ 2 < e ≥ 3 ∣ 2S ≥ 1 < 2S ≥ 2 < 2S ≥ 3 ∣ l ≥ 1 < k ≥ 3 ∣ f ≥ 1 < g ≥ 3 |
| Corollary 3, maximal chains | EXHAUSTIVE | 1113045672 maximal chains, every one of 17 covering steps, counted over all 976 cells |
| Theorem 9, the reflection | EXHAUSTIVE | 8 of 976 cells have their image under x → top - x in Λ; 0 are fixed; they are 10111011 10112111 21111011 10221022 21112111 10222122 21221022 21222122 at ranks 6,8,8,10,10,12,12,14 |
| Theorem 7, the bit accounting | EXHAUSTIVE | 17 bits carried per cell, 9.9307 needed to index 976 cells, surplus 7.0693; Λ is 0.7446% of the 2¹⁷ words |
| Theorem 10, five forms of d | EXHAUSTIVE | all 475800 pairs: 0 disagreements among interval count, coordinate product, two-integer, one-rational and p-adic forms |
| Theorem 10, d(x, x) = 1 | EXHAUSTIVE | all 976 cells: 0 exceptions |
| Theorem 11, the coordinate triangle | EXHAUSTIVE | 289 value triples over the eight alphabets: 0 failures of ∣a-c∣+1 ≤ (∣a-b∣+1)(∣b-c∣+1) |
| Theorem 11, the multiplicative triangle on cell triples | SAMPLED | 200000 of the 929714176 ordered cell triples (976 cubed), seed 20260922: 0 failures |
| Theorem 11, the log-distorted chain | EXHAUSTIVE | per-axis cost log(∣Δ∣+1): first step log 2 = 0.6931, tenth step log(11/10) = 0.0953 |
| Theorem 12, the tree factorisation | EXHAUSTIVE | every one of the 1944000 sub-boxes of the ambient box: 0 disagreements with direct enumeration |
| Theorem 13, containment, both directions | EXHAUSTIVE | the same 1944000 sub-boxes: 0 disagreements with the enumerated count |
| Proposition 1, the void is non-negative | EXHAUSTIVE | all 475800 pairs: 0 boxes hold more cells than they have points |
| Proposition 1, the void-free fraction | EXHAUSTIVE | 134871 of 475800 pairs, 0.2835; the seven rates run 0.6995 (g ≤ q) to 0.9806 (g ≤ 4f+2), their product 0.2013, the lift 1.4081 |
| Proposition 1, comparable pairs whose interval is a box | EXHAUSTIVE | 31604 of the 115162 strictly comparable pairs, 0.2744 |
| Lemma 3, the constraint graph is a caterpillar | EXHAUSTIVE | 8 nodes, 7 edges, connected: a tree; degree sequence 11122223; removing the 3 leaves leaves a path: True; oriented from bounded to bounding coordinate it has no directed cycle: True |
| Theorem 14, the nested form is the rank polynomial | EXHAUSTIVE | coefficient by coefficient over ranks 3 to 20, exact integers: True |
| Corollary 4, F(1) = 976 and F(-1) = 2 | EXHAUSTIVE | exact integer evaluation; F′(1)/F(1) = 10801/976 = 11.0666, against the midpoint 23/2: skew -0.4334 |
| Theorem 15, the free box vanishes at z = -1 | EXHAUSTIVE | Φ(1) = 6912, Φ(-1) = 0; 5 of the eight alphabets have even size (l, q, f, g, 2S) |
| Theorem 15, the residue localises on k = 2 | EXHAUSTIVE | the alternating sum F(-1) splits by source occupancy as k=1: +0, k=2: +2, k=3: +0 |
| Lemma 4, the detachable leaf | EXHAUSTIVE | the geometric identity on 60 exact rational points, degrees 0 to 5, 0 failures |
| Lemma 4, the spin projection | EXHAUSTIVE | 319 seven-coordinate cells, every one carrying exactly k + 1 values of 2S (sum 976); the projection is closed, defect 0 |
| Corollary 5, F is not palindromic | EXHAUSTIVE | forwards and backwards first part at rank 4, 5 against 4 |
| Theorem 16, the Möbius function | EXHAUSTIVE | the closed form satisfies the defining recursion on all 116138 comparable pairs (115162 strict); 0 violations; values [-1, 0, 1] |
| Theorem 16, the crosscut condition | EXHAUSTIVE | 24164 distinct intervals: the join of the atoms is the top exactly when the added generators form an antichain, and then the interval is Boolean; 0 exceptions |
| Corollary 6, the Möbius function in coordinates | EXHAUSTIVE | all 116138 comparable pairs: mu is non-zero on 19079, exactly the 19079 void-free unit hypercubes; it equals the arithmetic Möbius function of N(y)/N(x) on 99034 pairs and differs on 17104, every one a unit hypercube with a void |
| Theorem 17, the covering instance | EXHAUSTIVE | 102 elements: 25 alphabet slots and 77 envelope steps; 976 sets, one per cell |
| Theorem 17, covering is generating | SAMPLED | 80 random subsets of size 4 to 10, seed 20260923: 0 of them are covers, and 0 disagreements with the closure operator under test |
| Theorem 18, seed(Λ) = 7 | EXHAUSTIVE | branch and bound over 27 critical elements and 245 distinct witness signatures; lower bound 5; minimum 7; 13468 signature covers expanding to 24585 minimum covers; 976/7 = 139.4 |
| Theorem 18, one cell in every minimum cover | EXHAUSTIVE | 1 cell lies in all 24585 minimum covers — 21332130 — and 0 of the 102 elements is witnessed by a unique cell; the smallest witness set has 4 cells |
| Theorem 18, a local account of the common cell | EXHAUSTIVE | the cell witnesses 26 of the 102 elements; no one or two of them single it out, and three do: slot n = 2 (428 witnesses); slot e = 2 (392 witnesses); step g at 2S ≤ 0, value 3 (4 witnesses) |
| Corollary 7, what every minimum seed contains | EXHAUSTIVE | null transition, q = 0 in 24585 of 24585; full transfer, q = k = 1 in 24585 of 24585; full transfer, q = k = 2 in 24585 of 24585; full transfer, q = k = 3 in 24585 of 24585; s → p in 24585 of 24585; p → s in 24585 of 24585; p → p in 24585 of 24585; s → s in 17403 of 24585 |
| Corollary 8, no cell is removable | EXHAUSTIVE | R(Λ minus x) = Λ for all 976 cells through the closure operator under test, 0 exceptions |
| Theorem 18, the minimum covers close | SAMPLED | 40 of the 24585 minimum covers, seed 20260924, run through the closure operator under test: 0 failures |
| Theorem 18, the covers by cell | EXHAUSTIVE | 370 of 976 cells appear in a minimum cover; the median such cell in 59 (0.24%), the second most common in 14492 (58.9%), one in all 24585 |
| Birkhoff (1937) | CITED | a finite distributive lattice is the down-sets of its poset of join-irreducibles |
| Birkhoff (1940); Davey and Priestley (2002) | CITED | a sublattice of a distributive lattice is distributive; a finite lattice is modular iff it is graded with a modular rank function |
| Dilworth (1950) | CITED | the minimum chain cover equals the largest antichain |
| Dushnik and Miller (1941) | CITED | order dimension; for a distributive lattice it is the width of the generating poset |
| Rota (1964) | CITED | the crosscut theorem for the Möbius function, and its corollary: if the top is not a join of atoms then mu(bottom, top) = 0 |
| Karp (1972) | CITED | minimum set cover is NP-hard; its decision version is NP-complete |
| Fulkerson (1956) | CITED | Dilworth's theorem from König's: the minimum chain cover is n minus a maximum matching of the strict order |
| Stanley (1989) | CITED | a log-concave sequence with no internal zero is unimodal |
| Stanley (2012) | CITED | the maximal chains of a finite distributive lattice are the linear extensions of its poset of join-irreducibles |

**The exhausted families, named.** 6,912: every point of the ambient box at the caps of D3. 9,216: the same box extended to k = 0, for the floor's marginal count. 475,800: every unordered pair of distinct cells. 115,162: every strictly comparable ordered pair; 116,138 with the diagonal. 131,072: every subset of the seventeen generators. 289: every triple of values drawn from one of the eight alphabets, summed over the eight. 1,944,000: every coordinate box [lo, hi] of the ambient box, that is every choice of lo ≤ hi in each of the eight alphabets. 24,164: every distinct generator-set difference D(y) ∖ D(x) over comparable pairs. 24,585: every minimum seed, enumerated through 13,468 signature covers. 976: every single-cell deletion; also every cell, for the counts by q, by g and by spin label of §0 and §1. 929,714,176: every ordered triple of cells, 976³, the family the two SAMPLED sweeps of 200,000 draw from. The five further cap settings are named in their row.

**The two guards on every machine-checked claim.** *Non-vacuity* — the hypothesis of each obligation is shown satisfiable, and with a non-triviality demand: two distinct cells and caps at least 3 for the integer obligation; a monotone φ with two distinct admissible pairs for Lemma 1; a **proper** non-empty fixed point of ℛ inside the 3×3×3 box for Lemma 2. *Encoding fidelity* — the solver's membership formula is compared with an independently written implementation on every one of the 6,912 box points and on 400 random integer tuples drawn from a range wider than the box, 7,312 comparisons, **0** disagreements and **0** skipped; and the subset harness's staircase predicate is compared cell by cell against the same closure operator used in Theorem 2, 1,352 comparisons over three box shapes, **0** disagreements and **0** skipped. An obligation is not reported unless both guards pass.

**The negative controls, all refuted.** Six, run as a separate pass (83 rows in all). (1) Replace one bound by a bound on a sum, g + q ≤ 3: the solver returns `sat` with the explicit witness x = (3,1,3,3,3,0,0,0), y = (2,1,3,1,2,1,1,1), whose join (3,1,3,3,3,1,1,1) has g + q = 4 — a sum bound does not close; the witness is verified concretely, so the printed pair does not depend on which model the solver returns. (2) Drop monotonicity from Lemma 1: `sat`. (3) Assert the Möbius closed form without its antichain condition: refuted on 13,489 pairs of a sweep, where the true value is 0 and the unconditional formula gives ±1. (4) Claim a union of sublattices is a sublattice: refuted, 2 escaping joins in the union of two principal down-sets at incomparable generators. (5) Claim seed(Λ) = 6: refuted by the exhaustive search at limit 6. (6) Claim every coordinate box is full: refuted, the whole box holds 976 of 6,912 points.

**What is not machine-checked, and why.** The counts of §2 to §7 are computations at one cap setting (five further settings for the defect and the generator count) and are not of a shape a solver decides; they carry EXHAUSTIVE with their family named. Theorem 5's upper bound rests on Dilworth's theorem and an exact maximum matching, not on a solver. Theorem 16's proof uses two cited theorems whose own proofs are in the literature; what is checked here is the instance, on every comparable pair. Theorem 18 is an exhaustive search whose completeness is argued in its proof and not certified by an external tool: the branching rule is complete because every cover must contain a set witnessing the chosen uncovered element, and the pruning bound is valid because pairwise-disjoint elements require distinct sets. Distributivity on cell triples and the multiplicative triangle on cell triples are **SAMPLED**, each 200,000 triples with its seed stated, because the full family has 976³ = 929,714,176 ordered triples; in both cases the general statement is PROVED and the sample is a transcription check, not the evidence. Theorem 17's covering criterion is PROVED, and the two SAMPLED rows beside it are transcription checks that between them test both directions: none of the 80 random subsets is a cover and none closes, and 40 minimum covers all close. The grading of Theorem 4 is PROVED for every cap; at the base caps the check finds the 3,749 covers from the order alone and confirms every one is a unit step, while at the five further settings the join-irreducible count takes lower covers as unit steps, which the proved theorem licenses.

---

## References

- Birkhoff, G. (1937). Rings of sets. *Duke Mathematical Journal* **3**, 443–454.
- Baker, K. A. and Pixley, A. F. (1975). Polynomial interpolation and the Chinese remainder theorem for algebraic systems. *Mathematische Zeitschrift* **143**, 165–174.
- Bergman, G. M. (1977). On the existence of subalgebras of direct products with prescribed d-fold projections. *Algebra Universalis* **7**, 341–356.
- Birkhoff, G. (1940). *Lattice Theory*. American Mathematical Society Colloquium Publications 25, New York.
- Bohr, N. (1913). On the constitution of atoms and molecules. *Philosophical Magazine* **26**, 1–25.
- Chvátal, V. (1979). A greedy heuristic for the set-covering problem. *Mathematics of Operations Research* **4**, 233–235.
- Condon, E. U. and Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge University Press, Cambridge.
- Davey, B. A. and Priestley, H. A. (2002). *Introduction to Lattices and Order*, 2nd edition. Cambridge University Press, Cambridge.
- de Moura, L. and Bjørner, N. (2008). Z3: an efficient SMT solver. In *Tools and Algorithms for the Construction and Analysis of Systems*, Lecture Notes in Computer Science 4963, Springer, 337–340.
- Dilworth, R. P. (1950). A decomposition theorem for partially ordered sets. *Annals of Mathematics* **51**, 161–166.
- Dushnik, B. and Miller, E. W. (1941). Partially ordered sets. *American Journal of Mathematics* **63**, 600–610.
- Edelman, P. H. and Jamison, R. E. (1985). The theory of convex geometries. *Geometriae Dedicata* **19**, 247–270.
- Freuder, E. C. (1982). A sufficient condition for backtrack-free search. *Journal of the ACM* **29**, 24–32.
- Fulkerson, D. R. (1956). Note on Dilworth's decomposition theorem for partially ordered sets. *Proceedings of the American Mathematical Society* **7**, 701–702.
- Harary, F. and Schwenk, A. J. (1973). The number of caterpillars. *Discrete Mathematics* **6**, 359–365.
- Hopcroft, J. E. and Karp, R. M. (1973). An n⁵⁄² algorithm for maximum matchings in bipartite graphs. *SIAM Journal on Computing* **2**, 225–231.
- Johnson, D. S. (1974). Approximation algorithms for combinatorial problems. *Journal of Computer and System Sciences* **9**, 256–278.
- Karp, R. M. (1972). Reducibility among combinatorial problems. In R. E. Miller and J. W. Thatcher, eds., *Complexity of Computer Computations*, Plenum, New York, 85–103.
- König, D. (1931). Gráfok és mátrixok. *Matematikai és Fizikai Lapok* **38**, 116–119.
- Lach, M. (2026). The Closure Law of a Finite Index. This collection.
- Lauritzen, S. L. (1996). *Graphical Models*. Oxford University Press, Oxford.
- Monjardet, B. (1981). Metrics on partially ordered sets — a survey. *Discrete Mathematics* **35**, 173–184.
- Moore, E. H. (1910). *Introduction to a Form of General Analysis*. Yale University Press, New Haven.
- Pauli, W. (1925). Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren. *Zeitschrift für Physik* **31**, 765–783.
- Proctor, R. A., Saks, M. E. and Sturtevant, D. G. (1980). Product partial orders with the Sperner property. *Discrete Mathematics* **30**, 173–180.
- Rota, G.-C. (1964). On the foundations of combinatorial theory I. Theory of Möbius functions. *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete* **2**, 340–368.
- Schrödinger, E. (1926). Quantisierung als Eigenwertproblem (Erste Mitteilung). *Annalen der Physik* **79**, 361–376.
- Sperner, E. (1928). Ein Satz über Untermengen einer endlichen Menge. *Mathematische Zeitschrift* **27**, 544–548.
- Stanley, R. P. (1980). Weyl groups, the hard Lefschetz theorem, and the Sperner property. *SIAM Journal on Algebraic and Discrete Methods* **1**, 168–184.
- Stanley, R. P. (1989). Log-concave and unimodal sequences in algebra, combinatorics, and geometry. *Annals of the New York Academy of Sciences* **576**, 500–535.
- Stanley, R. P. (2012). *Enumerative Combinatorics, Volume 1*, 2nd edition. Cambridge University Press, Cambridge.
- Stoner, E. C. (1924). The distribution of electrons among atomic levels. *Philosophical Magazine* **48**, 719–736.
- Trotter, W. T. (1992). *Combinatorics and Partially Ordered Sets: Dimension Theory*. Johns Hopkins University Press, Baltimore.
