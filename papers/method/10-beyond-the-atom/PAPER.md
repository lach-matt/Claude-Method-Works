# Closure beyond the atom: the defect of other indexes, redundancy, and the electromagnetic quotient

**The closure defect of an index on ordered coordinates is a property of the coordinatisation and not of its subject: measured on fourteen indexes from the periodic table to the Kreuzer–Skarke frontier it separates the closed from the open, a second measure — the fraction of a set removable with exact recovery — separates them again and is governed by dimension rather than by coupling, and a selection rule is shown to act on an index as a quotient rather than as an added coordinate.**

**Matthew Lach** · Independent Researcher · 21 September 2026

---

## Abstract

A finite set of cells over `d` ordered coordinates has a canonical superset: the cells its own monotone bounds admit. The closure operator ℛ that produces it is a Moore closure on the observed box, and the **closure defect** `E(X) = |ℛ(X)| − |X|` counts what the coordinates imply and the set denies. This paper establishes what ℛ is and what it requires, then measures E across fourteen indexes drawn from chemistry, nuclear physics, string compactification, atomic spectroscopy and civil convention. Four results are structural. ℛ recovers monotone bounds, so it applies to ordered coordinates only, and E is a property of the coordinatisation: the same 118 elements give E = 36 on the eighteen-column periodic table and E = 0 on Janet's left-step ordering, and any set of 365 cells can be relabelled onto a 5 × 73 rectangle with E = 0. Fibring an index cannot raise its total defect, and the finest fibration drives it to zero, so *E = 0* is a claim relative to a stated fibration and the coarser the fibration the stronger the claim. A coordinate adjoined to an index can never repair it: if the graph of a map `h` is closed under meet and join then so is the index, and for a closed index the graph is closed exactly when `h` preserves meet and join. The converse fails, with an explicit two-cell witness. The measurements: E = 0 for the atomic lattice Λ at 976 cells in a box of 6,912, for Janet's table, for a box ordering, for a chessboard and for the occupation vectors of independent string oscillators; E = 36 for the periodic table, 7 for the Gregorian calendar, 9 for the particle-bound light nuclides with every admitted-and-absent cell a named unbound nuclide, 2 for the 3,558 nuclides of the AME2020 evaluation, and 540 for the χ = ±6 slice of the Kreuzer–Skarke list. The second measure, **redundancy**, is the largest fraction of an index removable at random with exact recovery by ℛ: 61% for Λ at eight coordinates, 20% for a three-coordinate spectroscopic survey, 0% for every two-coordinate index tested. It is not explained by coupling, the fraction of coordinate pairs whose envelope binds (r² = 0.002 over six indexes), and it falls with dimension on a single object: Λ projected to its first `d` coordinates recovers 61%, 30%, 30%, 30%, 5%, 0% at `d` = 8 down to 3. Adjoining a coordinate that is a function of two the index already carries takes redundancy from 20% to 0% and raises the defect from 0 to 20,808. Finally the electric-dipole selection rules are applied to the nine-coordinate lattice Λ₉: their image on (|Δℓ|, |ΔS|) is the complete 2 × 4 rectangle, so its E = 0 is vacuous; the spin rule ΔS = 0 cuts 526 cells at E = 0; the parity rule |Δℓ| = 1 cuts 840 cells at E = 750, because {−1, +1} has a hole at zero and the preimage is not a sublattice; and the same rules produce a crossing — within one element a dipole-allowed transition is followable 11.6% of the time against 40.7% for a forbidden one, while across the 118 elements the order reverses, 89.7% against 77.9%.

---

## §0 · The result

**Closure is a property of an index, not of the atom.**

The operator studied here takes a finite set `X` of `d`-tuples over ordered coordinates and returns the cells its own monotone bounds admit. Nothing is supplied from outside: the alphabets are the values `X` realises, and the bounds are read off `X`. The defect `E(X) = |ℛ(X)| − |X|` is therefore a measurement of what the coordinates carry against what the set states, and it is defined for any such set whatever its subject.

**What is claimed.** Five things.

1. **ℛ is a closure operator on the observed box, and its fixed points are sublattices.** Extensive, monotone and idempotent (Theorem 1), and ℛ(X) is closed under coordinatewise meet and join (Lemma 2). A full box is a fixed point (Theorem 2). These are proved and machine-checked over every subset of three named boxes.
2. **E is a property of the coordinatisation.** It changes under a permutation of one coordinate's value labels — the calendar, E = 7 before and 0 after — and any set of `ab` cells admits a relabelling onto an `a × b` rectangle, where it is 0 (Theorem 3). A coordinate with no intrinsic order therefore has no defect of its own; ℛ applies to ordered coordinates only. Fibring never raises the total defect and the finest fibration sends it to 0 (Theorem 4, Corollary 2), so *E = 0* is a claim relative to a stated fibration.
3. **The catalogue separates.** Fourteen indexes are recomputed here, each with its coordinates, cell count, ambient box and defect (Table 1, Figure 2). Zero for the atomic lattice at eight, nine and ten coordinates, for Janet's left-step ordering, for a box ordering, for a chessboard, for a spectroscopic survey grid and for the occupation vectors of independent oscillators; non-zero for the periodic table (36), the calendar (7), the light particle-bound nuclides (9), the AME2020 nuclide set (2) and the Kreuzer–Skarke χ = ±6 slice (540).
4. **Redundancy is a second, independent measure, and dimension governs it.** Defined as the largest fraction of an index removable at random with exact recovery by ℛ, it is 61% at eight coordinates and 0% at two, and its correlation with coupling over six indexes is r² = 0.002. Only independent coordinates count: a derived coordinate doubles the envelope count, raises coupling, and takes redundancy to zero while opening a closed index.
5. **A selection rule is a quotient.** The electric-dipole rules map Λ₉ onto a complete 2 × 4 rectangle, whose E = 0 says nothing. Imposed as subsets they behave according to the convexity of the value set they name: ΔS = 0 gives a sublattice and E = 0, |Δℓ| = 1 gives a non-sublattice and E = 750, with the witness printed. Adjoined as coordinates they give E = 9,278. And they produce a measured crossing between composition inside one element and composition across the 118.

**What is not claimed.** The paper measures; it does not explain. Why Janet's 1928 ordering closes and the classroom arrangement does not is a fact about two drawings of the same 118 elements, and the (n + ℓ) rule itself is not derived here. The 540 cells the Kreuzer–Skarke slice admits are stated as predictions consistent with the published bounds, not as members of the catalogue: the catalogue itself was not read, and four consistency tests against the literature are weaker than a lookup. The nine cells the light nuclide chart admits and lacks are named unbound nuclides, and reading them as the pairing and clustering terms of the semi-empirical mass formula is an interpretation, not a derivation. Redundancy figures are **SAMPLED**: seeded pseudorandom trials at a stated size, never exhaustive. The claim that dimension governs redundancy rests on one object measured at six dimensions and five further indexes at two or three; it is a measurement, not a law. Nothing here is a claim about the physics of the electric-dipole approximation: the rules are taken as given and their action on an index is what is measured. And the question of which formal languages exist is not settled here (§6): the paper measures which of five operators return a cell decision on a given index and reports agreement among exactly those, and it refuses to count agreement at two coordinates as evidence at all.

**Status words.** Six are used and never merged.

| status | meaning |
|---|---|
| **PROVED** | a proof is written out below and every step is justified |
| **MACHINE-CHECKED** | Z3 returned `unsat` on the negation of an obligation whose variables range over every subset of a named finite box, with both guards passed |
| **EXHAUSTIVE** | a decision procedure visited every case in a stated finite family, and the family's size is printed |
| **SAMPLED** | a seeded pseudorandom sweep of a stated size; never exhaustive |
| **REFUTATION** | a claim disproved by an explicit witness, the witness printed |
| **CITED** | taken from the literature or a public database, with the source |

The ceiling that is real: the machine checks decide claims over named boxes of at most 27 cells, so nothing here carries that status at a larger box or at `d > 3`. Which obligations carry which status, over which boxes and families, is §7 and nowhere else.

---

## §1 · Definitions

Throughout `d ≥ 1` is finite and `X` is a finite non-empty set of `d`-tuples of integers.

**D1 (index, cell, observed alphabet).** An **index** is a finite non-empty set `X` of `d`-tuples over `d` named coordinates. Its elements are **cells**. The **observed alphabet** at coordinate `i` is `A_i(X) := { x_i : x ∈ X }`, a finite set of integers carrying the order of ℤ.

**D2 (box).** `Box(X) := A_1(X) × ⋯ × A_d(X)`, the **ambient box**. As a product of finite chains it is a distributive lattice under the coordinatewise operations

> `(x ∧ y)_i = min(x_i, y_i)`,  `(x ∨ y)_i = max(x_i, y_i)`.

`|Box(X)| = ∏_i |A_i(X)|` is reported beside every defect, because `E = 0` carries information only when the box exceeds the cells.

**D3 (envelope).** For `i ≠ j` and `a ∈ A_j(X)`,

> `φ_ij(a) := max { y_i : y ∈ X, y_j ≤ a }`.

`φ_ij` is the furthest coordinate `i` reaches when coordinate `j` is held at or below `a`. There are `d(d − 1)` envelopes.

**D4 (closure, defect).**

> `ℛ(X) := { x ∈ Box(X) : x_i ≤ φ_ij(x_j) for all i ≠ j }`,  `E(X) := |ℛ(X)| − |X|`.

ℛ is a closure operator in the sense of Moore (1910); Theorem 1 establishes that below.

`X` is **closed** when `E(X) = 0`. A cell of `ℛ(X) \ X` is **admitted and absent**. For `d = 1` the condition is empty and `ℛ(X) = Box(X) = X`.

**D5 (fibration).** A **fibration** of `X` is a partition of `X` into non-empty parts. Fibring **by coordinate 1** is the partition `X_v := { x ∈ X : x_1 = v }` for `v ∈ A_1(X)`. The **fibred defect** of a fibration `{X_v}` is `Σ_v E(X_v)`, each fibre closed in its own box.

**D6 (binding envelope, coupling).** Write `M_i := max A_i(X)`. The envelope `φ_ij` **binds** when `φ_ij(a) < M_i` for at least one `a ∈ A_j(X)` — that is, when constraining coordinate `j` actually restricts coordinate `i`. The **coupling** of `X` is the fraction of the `d(d − 1)` envelopes that bind. An envelope that never binds imposes nothing.

**D7 (redundancy).** Fix a seed. For a fraction `t`, draw a uniformly random subset of `X` of size `|X| − ⌊t|X|⌋` and ask whether ℛ of it equals `X` exactly. Run `T` independent trials (`T = 10` for `|X| < 3000`, `T = 5` above). The fraction `t` **recovers** when at least 80% of its trials recover. The **redundancy** of `X` is the largest `t` in the ladder 5, 10, 20, 30, 41, 50, 61, 70, 82, 90 per cent that recovers, the ladder being climbed in increasing order and stopped at the first failure. Redundancy is **SAMPLED**; the seed and the per-rung trial counts are printed with every figure.

**D8 (extension, quotient).** Let `C = C_1 × ⋯ × C_m` be a finite product of chains, with the coordinatewise meet and join, and let `h : X → C`. The **extension of `X` by `h`** is `X^h := { (x, h(x)) : x ∈ X }`, an index on `d + m` coordinates. The **quotient of `X` by `h`** is the image index `h(X) ⊆ C` on `m` coordinates. An extension keeps every cell of `X` distinct; a quotient identifies cells `h` cannot separate. For `m = 1` the extension adjoins a single coordinate.

**D9 (composability).** In an index whose cells are **moves** — a cell carrying a source state and a target state — a cell is **followable** when its target state is the source state of some cell of the index. A cell that is not followable ends where nothing begins. The relevant source and target states are named where each such index is defined (§3.1, §5.5).

**D10 (bit cost).** For `E > 0` the **bit cost** of an index is `log₂ C(|ℛ(X)|, E)`, the number of bits needed to name which `E` of the admitted cells are the absent ones. It measures how much must travel alongside an index for a reader to reconstruct it from its coordinates.

**Notation.** `C(n, k)` is the binomial coefficient. Λ denotes the atomic lattice of §3.1 and Λ₉, Λ₁₀ its nine- and ten-coordinate extensions. Coordinate tuples are written in the order their definition states.

---

## §2 · The operator

### 2.1 What ℛ is

**Lemma 1 (the envelope is total and isotone).** For every `i ≠ j` and `a ∈ A_j(X)`, `φ_ij(a)` is defined; and `a ≤ a'` implies `φ_ij(a) ≤ φ_ij(a')`.

*Proof.* By D1 there is `y ∈ X` with `y_j = a`, so `{ y ∈ X : y_j ≤ a }` is non-empty and the maximum exists. If `a ≤ a'` then `{ y ∈ X : y_j ≤ a } ⊆ { y ∈ X : y_j ≤ a' }`, and the maximum of a subset is at most the maximum of the set. ∎ **PROVED.**

**Theorem 1 (ℛ is a closure operator).** For every finite non-empty `X`:

> (a) `X ⊆ ℛ(X)`;  (b) `X ⊆ S` implies `ℛ(X) ⊆ ℛ(S)`;  (c) `ℛ(ℛ(X)) = ℛ(X)`.

*Proof.* (a) Let `x ∈ X`. Then `x_i ∈ A_i(X)` for each `i`, so `x ∈ Box(X)`. For `i ≠ j`, `x` itself lies in `{ y ∈ X : y_j ≤ x_j }`, so `φ_ij(x_j) ≥ x_i`. Hence `x ∈ ℛ(X)`.

(b) Let `X ⊆ S` and `x ∈ ℛ(X)`. Each `A_i(X) ⊆ A_i(S)`, so `Box(X) ⊆ Box(S)` and `x ∈ Box(S)`. Fix `i ≠ j`. Since `x_j ∈ A_j(X) ⊆ A_j(S)`, the envelope `φ^S_ij(x_j)` is defined by Lemma 1. The candidate set `{ y ∈ X : y_j ≤ x_j }` is contained in `{ y ∈ S : y_j ≤ x_j }`, so `φ^X_ij(x_j) ≤ φ^S_ij(x_j)`. Therefore `x_i ≤ φ^X_ij(x_j) ≤ φ^S_ij(x_j)`, and `x ∈ ℛ(S)`.

(c) By (a) and (b), `ℛ(X) ⊆ ℛ(ℛ(X))`. For the reverse, first note `X ⊆ ℛ(X) ⊆ Box(X)`, so `A_i(ℛ(X)) = A_i(X)` for every `i` and the two sets have the same box. Next, `φ^{ℛ(X)}_ij ≥ φ^X_ij` by (b)'s inclusion argument; and conversely, if `y ∈ ℛ(X)` has `y_j ≤ a` then `y_i ≤ φ^X_ij(y_j) ≤ φ^X_ij(a)` by Lemma 1, so every candidate is bounded by `φ^X_ij(a)` and `φ^{ℛ(X)}_ij(a) ≤ φ^X_ij(a)`. The two envelope systems coincide, and with the same box the defining condition is the same condition. ∎ **PROVED**, and **MACHINE-CHECKED** over every subset of the boxes 3 × 3, 2 × 2 × 2 and 3 × 3 × 3, with the two guards of §7.

**Lemma 2 (ℛ(X) is a sublattice of its box).** `ℛ(X)` is closed under coordinatewise `∧` and `∨`.

*Proof.* Let `x, y ∈ ℛ(X)` and fix `i ≠ j`. For the join, `(x ∨ y)_i = max(x_i, y_i)`; say the maximum is `x_i`. Then `x_i ≤ φ_ij(x_j) ≤ φ_ij(max(x_j, y_j)) = φ_ij((x ∨ y)_j)` by Lemma 1. For the meet, `(x ∧ y)_j = min(x_j, y_j)`; say the minimum is `y_j`. Then `(x ∧ y)_i = min(x_i, y_i) ≤ y_i ≤ φ_ij(y_j) = φ_ij((x ∧ y)_j)`. Both `x ∨ y` and `x ∧ y` lie in `Box(X)`, since no new coordinate value is created. ∎ **PROVED.**

**Corollary 1.** If `E(X) = 0` then `X` is a sublattice of `Box(X)`. Consequently, if `X` is **not** a sublattice then `E(X) > 0`. ∎

**Proposition 1 (the converse, measured).** Over every non-empty subset of the boxes 3 × 3 and 2 × 2 × 2 — **766** sets in all — `X` is a sublattice of `Box(X)` **if and only if** `E(X) = 0`, and more strongly `ℛ(X)` equals the sublattice hull `⟨X⟩` cell for cell, with no exception. The same equality holds on three larger indexes computed here: the periodic table (126 cells), the Kreuzer–Skarke slice (748) and the parity set of §5.3 (1,590). **EXHAUSTIVE** on the stated families.

That `ℛ(X) = ⟨X⟩` on any finite product of chains is established in *The Hierarchy Law of Mathematical Languages* (Lach 2026) and is **CITED**; only the easy inclusion `⟨X⟩ ⊆ ℛ(X)` is proved here, as Lemma 2. Nothing below depends on the cited direction: every use is of Corollary 1, which is proved.

**Theorem 2 (a full box closes).** If `X = Box(X)` then `ℛ(X) = X` and `E(X) = 0`. In particular every singleton and every Cartesian product of chains is closed.

*Proof.* Let `x ∈ Box(X)` and `i ≠ j`. Because `X` is the full product, the tuple `y` with `y_i = max A_i(X)`, `y_j = x_j` and arbitrary admissible values elsewhere belongs to `X`, and `y_j ≤ x_j`. Hence `φ_ij(x_j) = max A_i(X) ≥ x_i`. So every cell of the box satisfies every condition, `ℛ(X) = Box(X) = X`. A singleton is the product of one-element chains. ∎ **PROVED**, and **EXHAUSTIVE** on the 84 boxes with `1 ≤ d ≤ 3` and side lengths 1 to 4.

### 2.2 E belongs to the coordinatisation

**Theorem 3 (the defect is not a property of the cells).**

> (a) For any finite `X` and any factorisation `|X| = ab` there is a bijection of `X` onto the `a × b` rectangle, and the image has defect 0.
> (b) A permutation of the labels of a single coordinate can change the defect. Witness: the 365 cells (month, day) of the Gregorian calendar have `E = 7`; relabelling the twelve months in increasing order of length — the same 365 cells, the same incidence structure, only the labels moved — gives `E = 0`.

*Proof.* (a) A rectangle `{0,…,a−1} × {0,…,b−1}` is a full box of `ab` cells; any bijection carries `X` onto it, and Theorem 2 gives defect 0. (b) is a computation: both sets are enumerated and both closures taken. ∎ (a) **PROVED**; (b) **EXHAUSTIVE**, the two sets of 365 cells. Two further instances of (a) are computed: the 90 cells of the periodic table onto a 9 × 10 rectangle, and the 365 of the calendar onto a 5 × 73 rectangle, both at `E = 0`.

**Corollary (ordered coordinates only).** ℛ recovers monotone bounds. A coordinate whose values carry no intrinsic order must be given one before `φ_ij` exists, and by Theorem 3(b) the defect depends on that choice. Where a coordinate is genuinely categorical — a kind, a language, a colour — the number `E` reports a property of an arbitrary ranking and is not a measurement of the index. The repair is to fibre over the categorical axes and close only the ordered coordinates inside each fibre. Every index in this paper has all coordinates ordered: they are counts, dates, ranks and quantum numbers.

**Theorem 4 (fibration does not raise the total defect).** Let `X` be an index with `d ≥ 2` and let `{X_v}_{v ∈ A_1(X)}` be its fibration by coordinate 1. Then the sets `ℛ(X_v)` are pairwise disjoint, `⋃_v ℛ(X_v) ⊆ ℛ(X)`, and

> `Σ_v E(X_v) ≤ E(X)`.

*Proof.* Each `X_v ⊆ X`, so `ℛ(X_v) ⊆ ℛ(X)` by Theorem 1(b). Every cell of `ℛ(X_v)` lies in `Box(X_v)`, whose first factor is `A_1(X_v) = {v}`; so cells of `ℛ(X_v)` and `ℛ(X_w)` differ in their first coordinate whenever `v ≠ w`, and the closures are disjoint. Summing, `Σ_v |ℛ(X_v)| = |⋃_v ℛ(X_v)| ≤ |ℛ(X)|`, while `Σ_v |X_v| = |X|` because the fibres partition `X`. Subtracting gives the inequality. ∎ **PROVED**, and **MACHINE-CHECKED** (the inclusion `ℛ(X_v) ⊆ ℛ(X)`) over every subset of 3 × 3, 2 × 2 × 2 and 3 × 3 × 3.

**Corollary 2 (E = 0 is relative to a fibration).** For any index `X` whatever, the fibration into singletons has fibred defect 0, since a singleton is a full box (Theorem 2). Refining a fibration by coordinate 1 therefore drives the total defect to zero by refinement alone. It follows that a statement "`E = 0`" is a statement about a set **relative to a declared fibration**, and the coarser the fibration the stronger the claim. The coarsest is the single fibre. ∎

Every defect reported in this paper is computed at the single fibre — one index, all coordinates ordered, no categorical axis — which is the strongest form available.

### 2.3 A coordinate cannot repair an index

**Theorem 5 (an extension never repairs).** Let `S` be a subset of a box `B`, `C` a finite product of chains, `h : B → C` any map, and `S^h := { (x, h(x)) : x ∈ S } ⊆ B × C`. If `S^h` is closed under the meet and join of `B × C` then `S` is closed under the meet and join of `B`.

*Proof.* Let `a, b ∈ S`. Then `(a, h(a))` and `(b, h(b))` lie in `S^h`, so their join `(a ∨ b, h(a) ∨ h(b))` lies in `S^h`. Every element of `S^h` has first component in `S`, so `a ∨ b ∈ S`. The same argument with the meet gives `a ∧ b ∈ S`. ∎ **PROVED**. The proof uses only that `C` carries coordinatewise meet and join, so it holds for any `m`. **MACHINE-CHECKED** at `m = 1` over every subset `S` of 3 × 3 with every `h` into a 3-chain, and every subset of 2 × 2 × 2 with every `h` into a 2-chain.

**Theorem 6 (the criterion).** Let `S ⊆ B` be closed under meet and join, `C` a finite product of chains, and `h : B → C`. Then `S^h` is closed under meet and join **if and only if** `h` restricted to `S` preserves them: `h(a ∨ b) = h(a) ∨ h(b)` and `h(a ∧ b) = h(a) ∧ h(b)` for all `a, b ∈ S`.

*Proof.* (⇐) For `a, b ∈ S`, `a ∨ b ∈ S` by hypothesis and `h(a ∨ b) = h(a) ∨ h(b)`, so `(a, h(a)) ∨ (b, h(b)) = (a ∨ b, h(a) ∨ h(b)) = (a ∨ b, h(a ∨ b)) ∈ S^h`; likewise for the meet. (⇒) Let `a, b ∈ S`. The join of their graph points is `(a ∨ b, h(a) ∨ h(b))`, which by hypothesis lies in `S^h`; every element of `S^h` is of the form `(x, h(x))`, and its first component here is `a ∨ b`, so its second component is `h(a ∨ b)`. Hence `h(a ∨ b) = h(a) ∨ h(b)`. Likewise for the meet. ∎ **PROVED**, again for any `m`, and **MACHINE-CHECKED** at `m = 1` over the same two boxes.

**Refutation 1 (the converse of Theorem 5 fails, `d = 2`).** The claim "*if `S` is closed under meet and join then so is `S^h`*" is false. **Witness**, on the box 3 × 3 with `C = {0, 1, 2}`: take

> `S = { (0,0), (1,1) }`,  `h(0,0) = 1`, `h(x) = 0` for every other `x`.

`S` is closed: `(0,0) ∧ (1,1) = (0,0) ∈ S` and `(0,0) ∨ (1,1) = (1,1) ∈ S`. But `S^h = { ((0,0), 1), ((1,1), 0) }`, and the join of its two elements is `((1,1), 1)`, which is not in `S^h` because `h(1,1) = 0`. ∎ **REFUTATION**; the witness is verified by enumeration, and Z3 independently reports the converse satisfiable over every `S` and `h` on that box.

**Refutation 2 (the same at `d = 3`).** On the box 2 × 2 × 2 with `C = {0, 1}`: `S = { (0,0,0), (1,1,1) }`, closed; `h(0,0,0) = 1` and `h = 0` elsewhere. The join of the two graph points is `((1,1,1), 1) ∉ S^h`. ∎ **REFUTATION**, verified the same two ways.

**Corollary 3 (the price of a derived coordinate).** Let `X` be closed, `E(X) = 0`, `C` a finite product of chains, and let `h : X → C` fail to preserve the meet or the join at some pair of cells of `X` whose meet or join is in `X`. Then `E(X^h) > 0`.

*Proof.* `X` is a sublattice of its box by Corollary 1, so the hypothesis of Theorem 6 is met and every meet and join of cells of `X` lies in `X`. By Theorem 6 the extension `X^h` is then not a sublattice of its own box, which is `Box(X) × C`, itself a product of chains. By Corollary 1, contrapositively, `E(X^h) > 0`. ∎ **PROVED.**

Corollary 3 is the structural content of two measurements made below: adjoining `|Δℓ|` and `|ΔS|` to Λ₉ (§5.4) and adjoining the electron count to a spectroscopic survey grid (§4.4). Neither map preserves the join, and neither extension is closed.

---

## §3 · The catalogue

Fourteen indexes are built and closed. Each is defined here by its coordinates and its membership rule; each cell count, box and defect in Table 1 is recomputed.

### 3.1 The atomic lattice and its tower

Λ has eight integer coordinates `(n, ℓ, k, q, e, f, g, 2S)`. A cell is a one-electron transfer: `q` electrons are taken from the subshell `(n, ℓ)`, which holds `k` of them, and `g` of them are placed in the subshell `(e, f)`; `2S` is twice the source total spin. The membership rule is eight inequalities, none of them introduced here:

> `ℓ ≤ n − 1` (the hydrogenic bound, Bohr 1913), `k ≤ 4ℓ + 2` and `k ≥ 1` (Stoner's subshell capacity of 1924, made exclusive by Pauli 1925), `q ≤ k`, `f ≤ e − 1`, `g ≤ 4f + 2`, `g ≤ q`, `2S ≤ k` (the capacity with Hund's first rule, 1925).


At the caps `n, e ∈ {1,2,3}`, `ℓ, f ∈ {0,1}`, `k, q, g, 2S ∈ {0,…,3}` this gives **976 cells in a box of 6,912, E = 0**. Λ₉ adjoins the target multiplicity `2S′` with `2S′ ≤ g`: **1,654 cells in a box of 27,648, E = 0**. Λ₁₀ adjoins the seniority `v` with `2S′ ≤ v ≤ g`: **2,535 cells in a box of 110,592, E = 0**.

Λ is an index of **moves**, so D9 applies to it. A cell's **source end** is `(n, ℓ, k, 2S)` — the subshell electrons leave, its occupancy and the source spin — and its **target end** is `(e, f, g, 2S′)`, the subshell they arrive in, how many arrive and the target spin. A cell is followable when its target end equals the source end of some cell of the index. On Λ₈ **no cell is followable**, and necessarily so: Λ₈ has no `2S′`, so its target end carries three components against the source end's four and the two can never be equal. Λ₉ supplies the missing component, and **1,169 of its 1,654 cells (70.7%)** become followable; Λ₁₀ gives **2,050 of 2,535 (80.9%)**. The state indexes of §3.2 and §3.3 cannot have the property at all: a cell there is one position, and there is nothing to compose.

### 3.2 The same 118 elements, twice

**The periodic table** (Mendeleev 1869; the eighteen-column arrangement is one of the thousand-odd periodic systems published since — Scerri 2016), coordinates (period, group), one cell per element of the arrangement with the f-block detached: **90 cells in a box of 126, E = 36**. The 36 admitted-and-absent cells are exactly period 1 groups 2 to 17, period 2 groups 3 to 12 and period 3 groups 3 to 12 — the gaps of the short periods, every one of them (Figure 1). They are supplied to a reader from outside the table; that is what the defect counts.

The 36 are placement-sensitive. Drawing helium at group 2 instead of group 18, on the same 90 elements, gives **E = 20**. The mechanism is the envelope: `φ(group | period ≤ 1)` is 18 under the standard placement and 2 under the alternative, so the whole first row of admitted-and-absent cells exists only under the first. The difference of sixteen cells is the cost of specifying that choice.

**Janet's left-step ordering** (Janet 1929, the table first published in 1928), coordinates (n + ℓ, Z), the same 118 elements ordered on the Madelung sum: **118 cells in a box of 944, E = 0**. The two indexes have the same subject and different defects. That is Theorem 3 demonstrated on one object rather than argued.

![**Figure 1.** The eighteen-column periodic table as an index on (period, group). Blue: the 90 cells the table holds. Red: the 36 its own coordinates admit and it denies — period 1 groups 2 to 17, period 2 groups 3 to 12, period 3 groups 3 to 12. A reader given only the occupied cells would reconstruct all 126.](figures/figure-1-periodic-table.png)

### 3.3 Convention, order, and a full product

**The Gregorian calendar**, coordinates (month, day), the 365 cells of a common year: **365 cells in a box of 372, E = 7**. The seven admitted-and-absent cells are (2, 29), (2, 30), (2, 31), (4, 31), (6, 31), (9, 31) and (11, 31) — February's three missing days and the four thirty-day months' thirty-firsts. The index fails to close for one reason: the number of days is not monotone in the month index. Relabelling the months in order of length repairs it exactly (Theorem 3(b)), and produces a calendar no one can use. The seven is the price of keeping January first.

**A box ordering**, coordinates `(l, w, h)` with `l ≥ w ≥ h` over five values: **35 cells in a box of 125, E = 0**. A genuine constraint that still closes.

**A chessboard**, coordinates (rank, file): **64 cells in a box of 64, E = 0**. No constraint at all. Between the two, `E = 0` is shown to carry information only when the box exceeds the cells, which is why Table 1 reports the box in every row.

### 3.4 The nuclide chart, on two populations

The nuclide chart has coordinates `(Z, N)`. Two different populations are indexed, and they give different defects; both are reported.

**The particle-bound light nuclides** — those that do not immediately emit a nucleon — at five proton-number cutoffs:

| cutoff | cells | admitted | E |
|---|---|---|---|
| Z ≤ 5 | 27 | 33 | 6 |
| Z ≤ 6 | 40 | 48 | 8 |
| Z ≤ 7 | 52 | 61 | **9** |
| Z ≤ 9 | 75 | 84 | **9** |
| Z ≤ 10 | 87 | 96 | **9** |

The nine admitted-and-absent cells at `Z ≤ 7` are **He-5, He-7, Li-10, Be-8, Be-13, B-9, B-16, B-18, C-21**. Every cell named at one cutoff persists at every larger one, and none is added after `Z ≤ 7`: the defect is a property of the measurement, not of the window. Each of the nine is a known unbound nuclide interior to the region its own neighbours define. Be-8 is unbound because it is two alpha particles; He-5, He-7, Li-10 and Be-13 are unbound by one neutron against an even-paired core. `(Z, N)` records how many protons and neutrons a nuclide has and cannot record that four of them prefer to be an alpha particle, or that the last neutron is unpaired. Reading the nine as the pairing and clustering terms of the semi-empirical mass formula is an interpretation of the cells, and is marked as such.

**The AME2020 evaluation (Wang, Huang, Kondev, Audi and Naimi 2021), Table I** — 3,558 rows, `Z` from 0 to 118, of which 2,550 carry a measured mass and 1,008 an extrapolated one — gives 3,558 distinct `(Z, N)` cells and **E = 2** at every cutoff `Z ≤ 20, 50, 82, 92, 118`. The two admitted-and-absent cells are `(0, 0)`, which is empty, and `(2, 0)`, the diproton, which is unbound and is the textbook failure of the pairing term. The number is 2 and not 9 because the population is different: the AME2020 set is not the particle-bound set, and includes unbound and extrapolated species that fill most of the region the smaller chart leaves open. The stability across cutoffs, the nameability of the cells and their reading as a pairing failure survive on both populations; the count does not transfer between them, and the two rows of Table 1 are two different indexes.

### 3.5 The Kreuzer–Skarke frontier

Coordinates `(h¹¹, h²¹)`, the two Hodge numbers of a Calabi–Yau threefold. The complete list of reflexive four-dimensional polytopes is that of Kreuzer and Skarke (2002), whose construction rests on Batyrev's polar duality (1994); the list itself was not read here. One slice of it is stated exactly in the literature: Candelas, de la Ossa, He and Szendrői (2008) record that the points with Euler characteristic `χ = 2(h¹¹ − h²¹) = ±6` have Hodge numbers `(h, h+3)` and `(h+3, h)` for `13 ≤ h ≤ 128`, with the exclusions `h = 102, 103, 115, 117` and `119` to `126`. That is **208 cells in a box of 12,544**, and

> **E = 540**, from 498 join failures and 498 meet failures among the 21,528 pairs.

The geometry is elementary. The slice is two parallel lines; the join of `(h, h+3)` and `(h+3, h)` is `(h+3, h+3)`, which lies on neither, so ℛ immediately names the diagonal between them. Of the 540 admitted cells, **112 lie on the diagonal**, running from `(13,13)` to `(131,131)`; the admitted cells carry exactly five Euler characteristics, `χ ∈ {0, ±2, ±4}`; and `h¹¹ + h²¹` runs from 26 to 262.

Four consistency tests against the published characterisation of the catalogue are recomputed: every one of the 540 has `h¹¹ ≥ 1`, `h²¹ ≥ 1`, and `h¹¹ + h²¹ ≤ 502`, the published maximum. None falls in the thinly populated tip where a prediction would be refuted. This is weaker than a lookup and it is not nothing: the closure of a slice proposes 540 Hodge pairs, and none of them is excluded by what the literature states about the file. The index proposes; it is not thereby right.

### 3.6 The string partition function

The transverse oscillators of the bosonic string give an index with multiplicity: a cell is an occupation vector over the modes `(n, i)`, `n ≥ 1`, `i ∈ {1,…,24}`, graded by `N = Σ n · occ(n, i)`. The degeneracy at level `N` is the coefficient of `q^N` in `∏_{n≥1} (1 − q^n)^{−24}` (Green, Schwarz and Witten 1987). The coefficients are computed two ways and agreed for `N ≤ 16`: by expanding the product, and by the Euler-type recurrence `d(N) = (24/N) Σ_{k=1}^{N} σ(k) d(N−k)` with `σ` the sum of divisors. They give `d(1) = 24`, `d(2) = 324`, `d(3) = 3,200`, `d(14) = 156,883,829,400`.

The set of admissible occupation vectors is a **full product**: each oscillator's occupancy is free of every other's. By Theorem 2 it closes, `E = 0`, and the closure adds nothing. A finite instance is computed as a check — three independent oscillators capped at occupancy 3, `E = 0`. This is the degenerate end of the phenomenon: Λ closes because its coordinates couple only along a tree, and the string's modes close because they do not couple at all.

### 3.7 A spectroscopic survey grid

Coordinates `(Z, core charge, ℓ)`. Each cell is a Rydberg channel — a fixed parent core, a fixed orbital angular momentum, the principal quantum number running. The grid taken here is the product of the 28 elements, the ten core charges `{1, 2, 3, 4, 5, 6, 9, 11, 15, 16}` and the eight `ℓ` values `s` to `k` that the survey holds, restricted to `charge < Z`: **1,744 cells in a box of 2,240, E = 0**. Of these, **285** are actually witnessed by a measured channel in the survey. That difference is a statement about what has been measured and about the cap chosen, not a closure defect: the grid is a fixed point of ℛ, and reading the unwitnessed count as `E` would say the index is open when it is closed.

### 3.8 Table 1

**Table 1.** Every index of this paper, its coordinates, cell count, ambient box and closure defect. Cells with no box entry are the two nuclide populations, whose box is set by the largest `Z` and `N` present and is not a meaningful comparator.

| index | coordinates | cells | box | E |
|---|---|---|---|---|
| Λ, the atomic lattice | (n, ℓ, k, q, e, f, g, 2S) | 976 | 6,912 | **0** |
| Λ₉ | Λ with 2S′ | 1,654 | 27,648 | **0** |
| Λ₁₀ | Λ₉ with the seniority v | 2,535 | 110,592 | **0** |
| Janet's left-step ordering | (n + ℓ, Z) | 118 | 944 | **0** |
| a box ordering | (l, w, h), l ≥ w ≥ h | 35 | 125 | **0** |
| a chessboard | (rank, file) | 64 | 64 | **0** |
| the survey grid | (Z, core charge, ℓ) | 1,744 | 2,240 | **0** |
| the dipole image | (\|Δℓ\|, \|ΔS\|) | 8 | 8 | **0** |
| three capped oscillators | occupation per mode | 64 | 64 | **0** |
| the AME2020 nuclides | (Z, N) | 3,558 | — | **2** |
| the Gregorian calendar | (month, day) | 365 | 372 | **7** |
| particle-bound nuclides, Z ≤ 7 | (Z, N) | 52 | — | **9** |
| the periodic table | (period, group) | 90 | 126 | **36** |
| Kreuzer–Skarke, χ = ±6 | (h¹¹, h²¹) | 208 | 12,544 | **540** |

![**Figure 2.** The closure defect of eleven of the indexes of Table 1, cells beside each label. The three closed at zero with a box far exceeding their cells — Janet at 118 in 944, the box ordering at 35 in 125, Λ at 976 in 6,912 — carry information; the chessboard at 64 in 64 does not, because its box is its cells. The largest defect is the Kreuzer–Skarke slice's 540, which arises because the slice is two parallel lines and their join is the diagonal between them.](figures/figure-2-defects.png)

### 3.9 What a defect costs to transmit

The bit cost of D10 puts the defects on a common scale: it is the length of the message a reader needs beside the coordinates in order to recover the index exactly.

| index | \|ℛ(X)\| | E | bit cost |
|---|---|---|---|
| the AME2020 nuclides | 3,560 | 2 | 22.6 |
| particle-bound nuclides, Z ≤ 7 | 61 | 9 | 34.0 |
| the Gregorian calendar | 372 | 7 | 47.4 |
| the periodic table | 126 | 36 | 105.1 |
| Kreuzer–Skarke, χ = ±6 | 748 | 540 | 633.0 |

The calendar's 47.4 bits is the content of the rhyme *Thirty days hath September*, which exists because the coordinates cannot carry the month lengths and is exactly seven cells long.

---

## §4 · Redundancy

The defect asks what an index fails to say. Redundancy asks the opposite question: how much of an index can be thrown away and still recovered from what is left.

### 4.1 The measure

D6 and D7 give two numbers per index. **Coupling** counts the envelopes that bind: an envelope `φ_ij` that equals `max A_i(X)` everywhere imposes nothing, and a pair of coordinates joined only by such envelopes is, as far as ℛ can see, independent. **Redundancy** is the largest fraction removable at random with exact recovery in at least 80% of trials. Redundancy is a sampled quantity and is reported with its seed and per-rung trial counts; every figure below was taken at seed 20260809, ten trials per rung, every index reported here being below the 3,000-cell threshold of D7.

### 4.2 The six rows

**Table 2.** Coupling and redundancy on six indexes. `d(d−1)` is the envelope count.

| index | d | envelopes | coupling | redundancy |
|---|---|---|---|---|
| Λ | 8 | 56 | 28.6% | **61%** |
| the survey grid | 3 | 6 | 16.7% | **20%** |
| a box ordering | 3 | 6 | 50.0% | **0%** |
| Janet as a down-set | 2 | 2 | 50.0% | **0%** |
| the periodic table | 2 | 2 | 0.0% | **0%** |
| the Gregorian calendar | 2 | 2 | 0.0% | **0%** |

The Janet row is the left-step table read as the down-set of the 118-element filling along `n + ℓ` — 724 cells, `E = 0` — rather than the 118 cells of Table 1, so that the sampling has something to remove; the 118-cell form has coupling 100% and redundancy 0%.

**Coupling does not explain redundancy.** The least-squares fit of redundancy on coupling over these six rows gives

> `r² = 28227/16524095 = 0.0017`, reported as **0.002**, with `p = 0.94` on four degrees of freedom.

The `r²` is computed in exact rational arithmetic; the `p`-value uses the closed form of the Student `t` distribution at `ν = 4`, checked against trapezoidal quadrature of its density to 5.5 × 10⁻¹⁴. The rows themselves make the point without the arithmetic: the box ordering and Janet both couple at 50% and recover nothing, while the survey grid couples at 16.7% and recovers a fifth.

### 4.3 Dimension, on one object

ℛ works on pairwise envelopes, so an index of dimension `d` has `d(d−1)` of them — 56 for Λ, 6 at three coordinates, 2 in a plane. With two envelopes there is almost nothing to reconstruct from. The comparison across six different subjects confounds dimension with everything else about them, so the measurement is repeated on a **single object**, Λ projected onto its first `d` coordinates with its constraints unchanged:

| d | cells | E | redundancy |
|---|---|---|---|
| 8 | 976 | 0 | **61%** |
| 7 | 319 | 0 | **30%** |
| 6 | 165 | 0 | **30%** |
| 5 | 99 | 0 | **30%** |
| 4 | 33 | 0 | **5%** |
| 3 | 12 | 0 | **0%** |

Every projection is itself closed, so the comparison is between closed indexes throughout and is not contaminated by a change of defect. Redundancy is non-decreasing in `d`, and falls by a factor of twelve between eight coordinates and four. This is one object at six dimensions; it is a measurement, not a law, and the cell counts fall with `d` as well, which the design does not separate from the dimension.

![**Figure 3.** Left: redundancy against the number of coordinates, measured on Λ projected onto its first d, at seed 20260809. Every projection is closed. Right: redundancy against coupling over the six indexes of Table 2; the least-squares fit gives r² = 0.002. Points that coincide carry both labels.](figures/figure-3-redundancy.png)

### 4.4 Only independent coordinates count

A coordinate that is a function of coordinates the index already carries adds no information, and obliges ℛ to reproduce it exactly. Adjoining the electron count `N_e = Z − c + 1` to the three-coordinate survey grid, a function of two coordinates it already holds:

| quantity | before | after |
|---|---|---|
| coordinates | 3 | 4 |
| envelopes | 6 | 12 |
| coupling | 16.7% | 33.3% |
| redundancy | **20%** | **0%** |
| E | **0** | **20,808** |

The envelope count doubles and the coupling rises — both movements that a reading of coupling as a proxy for reconstructibility would call favourable. Recovery instead fails at the very first rung, 5%, and the index stops being closed.

Corollary 3 says why, and its hypothesis is verified rather than assumed. `N_e` is decreasing in the core charge, so it does not preserve the join; the witness is the pair of cells `(Z, c, ℓ) = (3, 1, 0)` and `(5, 4, 0)`, both in the grid, with `N_e = 3` and `N_e = 2`. Their join is `(5, 4, 0)`, also in the grid, with `N_e = 2`, while the join of the two values is 3. A closed index extended by a map that fails to preserve the join is not closed.

---

## §5 · The electromagnetic quotient

The electric-dipole selection rules for a one-electron jump are two statements about the change in orbital angular momentum and in total spin: `Δℓ = ±1` (Laporte 1924) and `ΔS = 0` in LS coupling (Russell and Saunders 1925), both with their group-theoretic ground in Wigner (1927). This section applies them to Λ₉ and measures what they do to it.

### 5.1 Two differences

On Λ₉, write

> `Δℓ(c) := f − ℓ`,  `ΔS(c) := 2S′ − 2S`.

Both are differences of two coordinates of the index. On Λ₉ at these caps `ℓ` and `f` take only 0 and 1, so `|Δℓ| ∈ {0, 1}`: the multipole assignment `|Δℓ| = 0 → M1`, `|Δℓ| = 1 → E1` (Condon and Shortley 1935) covers every cell, and the two classes hold **814 and 840 cells** of the 1,654.

**Lemma 3 (the interval property).** Let `g(x) = x_i − x_j` for coordinates `i ≠ j`. For any two cells `a, b`, both `g(a ∨ b)` and `g(a ∧ b)` lie in the closed interval between `g(a)` and `g(b)`.

*Proof.* Write `s₁ = a_i`, `s₂ = b_i`, `t₁ = a_j`, `t₂ = b_j`, and `g₁ = s₁ − t₁ = g(a)`, `g₂ = s₂ − t₂ = g(b)`.

*The join.* `g(a ∨ b) = max(s₁, s₂) − max(t₁, t₂)`. Choose `m ∈ {1, 2}` with `s_m = max(s₁, s₂)` and `n ∈ {1, 2}` with `t_n = max(t₁, t₂)`. Since `t_n ≥ t_m`,

> `g(a ∨ b) = s_m − t_n ≤ s_m − t_m = g_m`;

and since `s_m ≥ s_n`,

> `g(a ∨ b) = s_m − t_n ≥ s_n − t_n = g_n`.

So `g_n ≤ g(a ∨ b) ≤ g_m` with `m, n ∈ {1, 2}`, which places `g(a ∨ b)` between `min(g₁, g₂)` and `max(g₁, g₂)`.

*The meet.* `g(a ∧ b) = min(s₁, s₂) − min(t₁, t₂)`. Choose `m` with `s_m = min(s₁, s₂)` and `n` with `t_n = min(t₁, t₂)`. Since `t_n ≤ t_m`, `g(a ∧ b) = s_m − t_n ≥ s_m − t_m = g_m`; and since `s_m ≤ s_n`, `g(a ∧ b) = s_m − t_n ≤ s_n − t_n = g_n`. Again the value lies between `g₁` and `g₂`. ∎ **PROVED**, and **EXHAUSTIVE** for `Δℓ` and `ΔS` on all **1,367,031** pairs of Λ₉, with zero violations.

**Corollary 4 (the convexity criterion).** Let `X` be a sublattice of its box, `g` a difference of two coordinates, and `C ⊆ ℤ` an interval. Then `{ x ∈ X : g(x) ∈ C }` is a sublattice.

*Proof.* Let `a, b` lie in the set. By Lemma 3, `g(a ∨ b)` lies between `g(a)` and `g(b)`, both of which are in the interval `C`, so `g(a ∨ b) ∈ C`; and `a ∨ b ∈ X` since `X` is a sublattice. The same for the meet. ∎ **PROVED.**

### 5.2 The spin rule cuts a sublattice

`ΔS = 0` names the value set `C = {0}`, an interval. By Corollary 4 the cells it keeps form a sublattice, and the measurement is that they are also closed:

> the spin rule imposed on Λ₉ keeps **526 cells at E = 0**.

Corollary 1 runs the other way, so the 526 at zero is a measurement and not a consequence of Corollary 4; under the identity of Proposition 1 the two statements are the same one, and that direction is cited rather than proved here.

### 5.3 The parity rule does not, and here is the witness

`|Δℓ| = 1` names the value set `C = {−1, +1}`, which has a hole at zero and is not an interval. Corollary 4 does not apply, and the set is in fact not a sublattice.

**Refutation 3 (the parity set is not a sublattice).** The claim "*the cells of Λ₉ with `|Δℓ| = 1` are closed under join*" is false. **Witness**: the two cells

> `a = (n, ℓ, k, q, e, f, g, 2S, 2S′) = (1, 0, 1, 0, 2, 1, 0, 0, 0)`,  `Δℓ(a) = +1`,
> `b = (2, 1, 1, 0, 1, 0, 0, 0, 0)`,  `Δℓ(b) = −1`,

both of which satisfy `|Δℓ| = 1`. Their coordinatewise join is

> `a ∨ b = (2, 1, 1, 0, 2, 1, 0, 0, 0)`,  `Δℓ(a ∨ b) = 1 − 1 = 0`,

which fails `|Δℓ| = 1` and so leaves the set. ∎ **REFUTATION**, the witness found by exhaustive search over the pairs of the 840 cells and verified by direct evaluation.

By Corollary 1 the parity set therefore has a positive defect, and the measurement is

> the parity rule imposed on Λ₉ keeps **840 cells at E = 750**.

The contrast with §5.2 is exactly the convexity of the value set, and nothing else: both rules are conditions on a difference of two coordinates of the same index.

### 5.4 Quotient, not extension

The two rules define a map

> `κ : Λ₉ → ℤ × ℤ`,  `κ(c) = (|Δℓ(c)|, |ΔS(c)|)`.

**The image is a complete rectangle.** `|Δℓ|` takes the values 0 and 1 and `|ΔS|` the values 0, 1, 2 and 3, and every one of the eight combinations is realised, with the multiplicities

| | \|ΔS\| = 0 | 1 | 2 | 3 | total |
|---|---|---|---|---|---|
| **E1**, \|Δℓ\| = 1 | 264 | 342 | 180 | 54 | 840 |
| **M1**, \|Δℓ\| = 0 | 262 | 337 | 171 | 44 | 814 |

All 1,654 cells map somewhere, and the image is the full 2 × 4 box. Its defect is therefore **E = 0 by Theorem 2, and vacuously**: it closes because it is a box, not because the selection rules constrain it. Any claim that the electromagnetic index is closed is a claim about the shape of the image and carries no information about the rules.

**The extension is a different object, and it is open.** Adjoining the same two quantities to Λ₉ as coordinates gives an index of eleven coordinates on the same 1,654 cells, with

> `E = 9,278`.

Adjoining `|Δℓ|` alone gives `E = 1,654`; adjoining `|ΔS|` alone gives `E = 3,812`.

Corollary 3 accounts for all three, and its hypothesis is exhibited for each map rather than inferred from the defect. For `|Δℓ|` the witness is Refutation 3's pair: both members have `|Δℓ| = 1`, their join has `|Δℓ| = 0`, and 0 is not the join of 1 with 1. For `|ΔS|` the witness is

> `(1, 0, 1, 0, 1, 0, 0, 1, 0)` and `(1, 0, 1, 1, 1, 0, 1, 0, 1)`, with `|ΔS| = 1` each,

whose join `(1, 0, 1, 1, 1, 0, 1, 1, 1)` is again a cell of Λ₉ and has `|ΔS| = 0`. The same pair witnesses the failure for the two maps taken together. A selection rule divides an index; it does not extend one, and the difference between the two readings is 9,278 cells.

**A second, independent measurement on the same cells.** Whether a cell is dipole-allowed (`|Δℓ| = 1` and `ΔS = 0`: **264** of the 1,654) and whether it is followable in the sense of D9 (**1,169** of the 1,654) are almost unrelated. The binary entropy of "allowed" is `H = 0.633` bits, and the mutual information (Shannon 1948) between "allowed" and "followable" is **0.0004 bits** — six parts in ten thousand of what is available. Selection and composition are separate structures on the same index.

### 5.5 The crossing

The measurement that follows is on a different population, built from the observed ground configurations of all **118 elements**, as tabulated by NIST (Kramida, Ralchenko, Reader and the NIST ASD Team 2024). A cell is a move between two distinct occupied subshells of one element: `(Z, n, ℓ, k, q, e, f, g)`, where the subshell `(n, ℓ)` of element `Z` holds `k` electrons, `1 ≤ q ≤ k` of them are taken, and `1 ≤ g ≤ min(q, 4f+2)` of those are placed in another occupied subshell `(e, f)` of the same element. There are **4,325** such cells, all distinct.

A move is **followable** when its target — the subshell `(e, f)` at the occupancy `g` it delivers — is itself the source subshell, at that occupancy, of some move in the population. Two scopes are measured: *within one element*, where the matching move must belong to the same `Z`; and *across the table*, where it may belong to any of the 118.

**Table 3.** Followability by selection class. Percentages are of the class's own cell count.

| class | cells | followable within one element | followable across the 118 |
|---|---|---|---|
| all cells | 4,325 | 982 (**22.7%**) | 3,686 (**85.2%**) |
| dipole-allowed, \|Δℓ\| = 1 | 2,673 | 309 (**11.6%**) | 2,399 (**89.7%**) |
| forbidden, \|Δℓ\| ≠ 1 | 1,652 | 673 (**40.7%**) | 1,287 (**77.9%**) |
| parity-conserving, Δℓ even | 606 | 233 (**38.4%**) | 544 (89.8%) |
| parity-changing, Δℓ odd | 3,719 | 749 (**20.1%**) | 3,142 (84.5%) |

**The crossing is the second and third rows.** Within one element a dipole-allowed move is followable 11.6% of the time against the forbidden 40.7%; across the 118 elements the order reverses, 89.7% against 77.9%. The rule that forbids composition inside an atom is the rule that enables it between atoms.

The parity split reproduces half of this and not the other half. Splitting instead on the parity of `Δℓ` gives 38.4% against 20.1% within one element — the same direction, conserving above changing — but across the table the order does **not** reverse: 89.8% against 84.5%, conserving still above changing. The crossing proper belongs to the `|Δℓ| = 1` split, and the parity split is a weaker companion to its within-element half only. Both figures are printed because the difference between them is a result.

![**Figure 4.** The crossing. Followable fraction by selection class, within one element (blue) and across the 118 elements (orange), over the 4,325 moves between occupied subshells of the observed ground configurations. The dipole-allowed and forbidden bars change order between the two scopes; the parity bars do not.](figures/figure-4-crossing.png)

---

## §6 · Which languages can speak of an index

An index can be closed in more than one sense, and the senses are the formal languages a question about it may be posed in. Five operators are measured here. Each takes a finite index and returns an admitted superset, so each returns a decision per cell and the results can be compared cell for cell.

**D11 (the five operators).** For a finite index `X` over `d ≥ 2` ordered coordinates:

- **order**: `ℛ(X)`, the staircase of D4.
- **algebra**: `⟨X⟩`, the smallest subset of `Box(X)` containing `X` and closed under `∧` and `∨` — the generated sublattice (Birkhoff 1940).
- **geometry**: `{ x ∈ Box(X) : (x_i, x_j) ∈ conv(π_ij X) for all i < j }`, where `π_ij` is the projection onto coordinates `i` and `j` and `conv` the convex hull in the plane (Carathéodory 1911; Schrijver 1986).
- **information**: the join-irreducible elements of `X`, closed under `∨`.
- **statistics**: `{ x ∈ Box(X) : π_ij(x) ∈ π_ij(X) for all i < j }`, the support of the maximum-entropy distribution on the order-2 marginals, which iterative proportional fitting sends to zero exactly when a pairwise projection is unobserved (Deming and Stephan 1940).

Each returns a superset of `X`, and each has its own defect `|L(X)| − |X|`. The languages **agree** on `X` when all five return the same set.

**What the measurement refuses to report, and why it matters.** Three refusals bind every number in this section.

1. A language that was not run is not silent. A language that returns no cell decision on an index is reported as not run, and never as a measured silence. Only a language whose operator ran and whose precondition failed counts as a finding.
2. **Agreement at two coordinates is not evidence.** At `d = 2` there is exactly one coordinate pair, so pairwise consistency and cell membership coincide and every pairwise operator agrees for no reason at all. Such a run is marked degenerate and its agreement is withheld. This is checked: the two-coordinate periodic table is degenerate and the three-coordinate one is not. Every agreement figure below is at `d ≥ 3`.
3. **The roster is not settled and is not settled here.** Which formal languages there are, and how many of them bear an operator, is an open question. The measurement therefore counts a language as operator-bearing **on the index in front of it** — it returned a cell decision — and computes the pair count from that, rather than asserting a list.

**The measurement on Λ.** All five operators return an admitted set on Λ, and each returns `E = 0`. There are `C(5,2) = 10` pairs, and **all ten agree**. The same holds on the box ordering (10 of 10) and on Λ₉.

Two further readings are special, and they are special for different reasons. A **documentary** reading returns a citation rather than a cell decision; it has no mechanism at all and is silent by construction. An **analysis** reading has a mechanism — a fit — but returns a magnitude, an `R²` or a slope, not a decision about a cell; it cannot join the pairwise arithmetic, and it is reported as not run unless a witness is declared. The count `C(5,2) = 10` is thus measured, not assumed, and the five it counts are order, algebra, geometry, information and statistics.

**The discriminating case.** The periodic table at three coordinates — (period, group, block), the block being a function of the group — separates the five completely:

| language | order | algebra | geometry | information | statistics |
|---|---|---|---|---|---|
| defect | 100 | 100 | 83 | 24 | **0** |

**One of the ten pairs agrees**, order with algebra. The statistics reading gives zero because a maximum-entropy distribution on the pairwise marginals cannot see a hole: every pairwise projection of every absent cell is realised somewhere, so nothing is excluded. Agreement among the languages is thus not automatic, and where it holds it is a fact about the index.

**The relation between agreement and closure.** On the four indexes here with `d ≥ 3` — Λ, the box ordering, Λ₉ and the three-coordinate periodic table — the five languages agree exactly when all five defects are zero, three cases to one. That is one instance of a general law, which is not proved here: the law relating the containments among these five operators, and which of them hold in every finite index against which vary from one index to the next, is established in *The Hierarchy Law of Mathematical Languages* (Lach 2026) and is **CITED**. What is measured here is four indexes, and four indexes are not a law.

---

## §7 · Verification record

The verification program runs **102 obligations** and all pass; in self-test mode it runs 106, the four added being negative controls that must be reported as refuted and are. The distribution by status, in the plain run:

| status | count |
|---|---|
| MACHINE-CHECKED | 8 |
| EXHAUSTIVE | 78 |
| SAMPLED | 9 |
| REFUTATION | 2 |
| GUARD | 5 |

**By object.**

| object | PROVED | MACHINE-CHECKED (box) | EXHAUSTIVE (family) | SAMPLED / CITED |
|---|---|---|---|---|
| Lemma 1, the envelope | ✓ | — | — | — |
| Theorem 1, closure operator | ✓ | ✓ 3 obligations: every subset of 3×3, 2×2×2, 3×3×3 | — | — |
| Lemma 2, ℛ(X) a sublattice | ✓ | — | — | — |
| Proposition 1, the converse | — | — | **766 subsets** of 3×3 and 2×2×2; 3 larger indexes | the general identity **CITED** |
| Theorem 2, a full box closes | ✓ | — | **84 boxes**, 1 ≤ d ≤ 3, sides 1–4 | — |
| Theorem 3, coordinatisation | ✓ (a) | — | (b) the calendar, 365 cells twice; 2 rectangles | — |
| Theorem 4, fibration | ✓ | ✓ 3 obligations, same three boxes | — | — |
| Theorem 5, extension never repairs | ✓ | ✓ 2 obligations: (3×3, h into a 3-chain), (2×2×2, h into a 2-chain) | — | — |
| Theorem 6, the criterion | ✓ | ✓ 2 obligations, same two boxes | — | — |
| Refutations 1 and 2 | — | Z3 reports the converse satisfiable on both boxes | witness verified by enumeration | — |
| Corollary 3 | ✓ | — | its hypothesis exhibited for all four maps used (§4.4, §5.4) | — |
| Table 1, fourteen indexes | — | — | every cell of every index, closure computed in full | — |
| the periodic table's 36 | — | — | the 36 named and matched | — |
| the nuclide populations | — | — | 5 cutoffs; 3,558 AME2020 rows at 5 cutoffs | AME2020 **CITED** |
| Kreuzer–Skarke, 540 cells | — | — | 21,528 pairs; 540 cells against 3 published bounds | the slice **CITED** |
| string degeneracies | — | — | N ≤ 16 by two independent routes | — |
| Lemma 3, interval property | ✓ | — | **1,367,031 pairs** of Λ₉, two maps, 0 violations | — |
| Corollary 4, convexity | ✓ | — | — | — |
| Refutation 3, the parity witness | — | — | exhaustive pair search over 840 cells | — |
| Tables 2 and 3, redundancy | — | — | coupling exact on every envelope | **SAMPLED**, seed 20260809 |
| §4.2, r² and p | — | — | exact rational r²; quadrature agrees to 5.5 × 10⁻¹⁴ | — |
| §5.4, quotient and extensions | — | — | all 1,654 cells, three extensions closed in full; a join-failure witness for each map | — |
| §5.5, the crossing | — | — | all 4,325 moves, five classes, two scopes | ground configurations **CITED** |
| §6, the five languages | — | — | four indexes at d ≥ 3, ten pairs each | — |

**The exhausted families, named.** 84 boxes: every shape with `1 ≤ d ≤ 3` and every side in 1 to 4. 766 subsets: every non-empty subset of 3 × 3 (511) and of 2 × 2 × 2 (255). 1,367,031 pairs: every unordered pair of distinct cells of Λ₉. 21,528 pairs: every unordered pair of the 208 Kreuzer–Skarke cells. 4,325 moves: every ordered pair of distinct occupied subshells of every one of the 118 ground configurations, with every admissible `(q, g)`. The closures of Table 1 are computed cell by cell over the full ambient box in every case.

**The two guards on every machine check.** *Non-vacuity*: the hypothesis of each obligation is shown satisfiable before the obligation is reported — for Theorem 1(b) that `X` lies strictly inside `S` which lies strictly inside the box; for Theorems 5 and 6 that a closed graph with `S` proper and `h` non-constant exists. *Encoding fidelity*: the Z3 formula for membership in ℛ, evaluated concretely on 3,087 cells drawn from random instances over four shapes, agrees with the operator under test in every case; and that operator, on 300 further random instances over five shapes, agrees cell for cell with an independent implementation of D3 and D4 written from the definitions. An obligation is not reported if either guard fails.

**The negative controls.** Four deliberately false claims are stated in self-test mode and each is reported as refuted: that the periodic table's defect is 35; that a closed `S` forces a closed graph; that the fidelity guard passes a reference implementation with one cell deliberately added; and that the calendar recovers from a 5% random deletion. A green run is therefore evidence and not a restatement.

**What is not machine-checked, and why.** Every number in §3, §4 and §5 is a computation over a finite index, decided by enumeration and not of a shape a solver settles at any useful size: Λ₉ has 1,654 cells in a box of 27,648, three orders of magnitude beyond the boxes of §2. The redundancy figures are sampled by construction — the quantity is defined by random deletion — and no exhaustive version of them is claimed. The interpretation of the nine nuclide cells as pairing and clustering, and of the 540 Kreuzer–Skarke cells as predictions, are readings of computed cells and carry no status word at all. The hierarchy law cited in §6 is not proved here.

---

## References

- Batyrev, V. V. (1994). Dual polyhedra and mirror symmetry for Calabi–Yau hypersurfaces in toric varieties. *Journal of Algebraic Geometry* **3**, 493–535.
- Birkhoff, G. (1940). *Lattice Theory*. American Mathematical Society Colloquium Publications **25**, New York.
- Bohr, N. (1913). On the constitution of atoms and molecules. *Philosophical Magazine* **26**, 1–25.
- Candelas, P., de la Ossa, X., He, Y.-H. and Szendrői, B. (2008). Triadophilia: a special corner in the landscape. *Advances in Theoretical and Mathematical Physics* **12**, 429–473.
- Carathéodory, C. (1911). Über den Variabilitätsbereich der Fourierschen Konstanten von positiven harmonischen Funktionen. *Rendiconti del Circolo Matematico di Palermo* **32**, 193–217.
- Condon, E. U. and Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge University Press, Cambridge.
- Deming, W. E. and Stephan, F. F. (1940). On a least squares adjustment of a sampled frequency table when the expected marginal totals are known. *Annals of Mathematical Statistics* **11**, 427–444.
- Green, M. B., Schwarz, J. H. and Witten, E. (1987). *Superstring Theory, Volume 1: Introduction*. Cambridge University Press, Cambridge.
- Hund, F. (1925). Zur Deutung verwickelter Spektren, insbesondere der Elemente Scandium bis Nickel. *Zeitschrift für Physik* **33**, 345–371.
- Janet, C. (1929). *Considérations sur la structure du noyau de l'atome*. Imprimerie Départementale de l'Oise, Beauvais.
- Kramida, A., Ralchenko, Yu., Reader, J. and the NIST ASD Team (2024). *NIST Atomic Spectra Database*, version 5.12. National Institute of Standards and Technology, Gaithersburg. DOI 10.18434/T4W30F.
- Kreuzer, M. and Skarke, H. (2002). Complete classification of reflexive polyhedra in four dimensions. *Advances in Theoretical and Mathematical Physics* **4**, 1209–1230.
- Lach, M. (2026). *The Hierarchy Law of Mathematical Languages*.
- Laporte, O. (1924). Die Struktur des Eisenspektrums. *Zeitschrift für Physik* **23**, 135–175.
- Mendeleev, D. (1869). Über die Beziehungen der Eigenschaften zu den Atomgewichten der Elemente. *Zeitschrift für Chemie* **12**, 405–406.
- Moore, E. H. (1910). *Introduction to a Form of General Analysis*. Yale University Press, New Haven.
- Pauli, W. (1925). Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren. *Zeitschrift für Physik* **31**, 765–783.
- Russell, H. N. and Saunders, F. A. (1925). New regularities in the spectra of the alkaline earths. *Astrophysical Journal* **61**, 38–69.
- Scerri, E. R. (2016). *A Tale of Seven Scientists and a New Philosophy of Science*. Oxford University Press, Oxford.
- Schrijver, A. (1986). *Theory of Linear and Integer Programming*. Wiley, Chichester.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal* **27**, 379–423 and 623–656.
- Stoner, E. C. (1924). The distribution of electrons among atomic levels. *Philosophical Magazine* **48**, 719–736.
- Wang, M., Huang, W. J., Kondev, F. G., Audi, G. and Naimi, S. (2021). The AME 2020 atomic mass evaluation (II). Tables, graphs and references. *Chinese Physics C* **45**, 030003.
- Wigner, E. (1927). Einige Folgerungen aus der Schrödingerschen Theorie für die Termstrukturen. *Zeitschrift für Physik* **43**, 624–652.
