# The Tower over Λ: from Eight Coordinates to Thirteen

**An index of one-electron transitions extends coordinate by coordinate through six stages, every one of them a sublattice of its own box, because every bound it carries names a single already-present coordinate and is monotone in it; and what each adjoined coordinate costs is the gap between the exact set the physics prescribes and the least such bound that contains it — its monotone envelope, which exists, is unique and is computed fibre by fibre. Two coordinates inside one bound, the angular-momentum triangle, cannot be carried at all; a triangle with one side held constant cannot be carried either, but its least envelope is the band |a − b| ≤ 1, a sublattice for every constant, and that band, with a parity congruence as its whole loss, is what the last step of the tower carries.**

**Matthew Lach** · Independent Researcher · 24 September 2026

---

## Abstract

A one-electron transition of an atom can be written as a tuple of small non-negative integers: the shell, subshell and occupancy of the parent configuration, the number of electrons transferred, the shell, subshell and occupancy of the target, and the spins and couplings that the transition's angular momenta carry. The set of tuples admitted by the hydrogenic radial solution, the Pauli principle, counting and vector coupling is a finite subset Λ of a product of chains. This paper studies the sequence obtained by adjoining the angular-momentum coordinates one at a time: the target's spin, seniority, the core's total angular momentum, the core–orbit resultant and the total. Six stages result, of 976, 1,654, 2,535, 13,585, 70,905 and 199,130 cells, every one a sublattice of its own coordinate box and every one projecting exactly onto the stage below.

The paper proves the general facts behind that sequence for arbitrary caps. A coordinate bounded between two monotone functions, each of a single already-present coordinate, always extends a sublattice to a sublattice (Theorem 1 — a case of a standard fact about sublattices of products of chains, proved here because its shape is used again); for any prescribed exact set the smallest such extension containing it exists, is unique and is computed fibre by fibre — the monotone envelope (Theorem 2); the triangle region {|a − b| ≤ c ≤ a + b} is closed under coordinatewise maximum and not under coordinatewise minimum, with explicit witnesses for both of its inequalities (Theorem 3); the band Bₖ = {|a − b| ≤ k} is a sublattice for every constant k, while the three-variable region {|a − b| ≤ c} with c free is join-closed and is not (Theorem 4). Together these sort the exact set a new coordinate can carry (Theorem 5): an interval between monotone bounds of one coordinate each closes exactly; a triangle in two coordinates does not close; and a triangle with one side held constant does not close either, but its least envelope is the band, a sublattice of arity 1. In the tower every bound has arity 1, so every stage closes, and every one of the five adjoined coordinates is carried as an envelope of its exact set — realised shares 63.7, 44.7, 17.0, 31.4 and 64.4 per cent. At the last step the envelope is B₁ and the whole loss is a parity congruence: the exact doublet 2J = 2K ± 1 is carried as the triplet |2J − 2K| ≤ 1. The construction's bound is the least envelope at the tenth axis, at the thirteenth and, under the wider reading of its exact set, at the eleventh; at the ninth and the twelfth it is a larger member of the envelope family, the least envelopes admitting 1,638 and 60,320 cells against 1,654 and 70,905. Theorems 1, 3 and 4 and the closure half of Theorem 5 are machine-checked over the integers, so they hold at every cap and not at one box, with a non-vacuity guard and an encoding-fidelity guard passed first.

Three further structures are computed exactly. The constraint graph of the thirteenth stage has thirteen vertices and thirteen edges, cycle rank 1 from the tenth stage upward, girth 3, treewidth 2, and the transfer as the cut: no edge joins a parent coordinate to a target coordinate, so every path between the two blocks runs through it. Over that transfer every stage factorises with defect zero into a product of a parent section and a target section, the parent sections falling and the target sections rising; replacing the constant in the core–orbit bound by the cell's own subshell breaks the factorisation by 15,150 cells at the twelfth stage and 45,450 at the thirteenth, and imposing the exact triangle instead breaks closure outright, leaving 22,275 cells with a closure defect of 35,570. The first stage has seventeen join-irreducibles, twenty covering relations and exactly 1,113,045,672 maximal chains, counted by dynamic programming over the cover relations; the five stage-to-stage rank correspondences are gap-free intervals with monotone endpoints whose composition contains the direct correspondence with a slack of at most two rank units; and the first three stages are regenerated by minimum sets of 7, 8 and 9 cells, each found by exact branch and bound and each certified minimal by a solver over every subset of a dominance-reduced family of covering signatures.

---

## §0 · The result

**A coordinate's cost in this construction is the arity of its bounds, not the arity of the coordinate.**

Λ is a finite set of integer tuples. Each of its defining constraints has the shape xᵢ ≤ φ(xⱼ) with φ non-decreasing, and a set cut out by constraints of that shape is a sublattice of the product of chains it lives in: coordinatewise maximum and minimum of two members are again members. That is elementary and it is where the construction begins. The question this paper answers is what happens when the construction is continued — when the angular-momentum labels a spectroscopist would attach to the same transition are adjoined as further coordinates.

Five are adjoined, in the order in which a spectroscopic designation lists them: the target's total spin, the seniority of the target subshell, the total angular momentum of the parent term, the resultant of that momentum with the target's orbital momentum, and the total angular momentum of the whole. None of the five is carried exactly. Each is carried as a monotone envelope of its exact set, and what decides what the envelope costs turns out to be a purely combinatorial feature of the exact set — whether it is an interval between monotone bounds of one coordinate each — and not whether the coordinate is a count or a coupling.

**What is established.**

1. **The six stages and their closure.** The stages hold 976, 1,654, 2,535, 13,585, 70,905 and 199,130 cells. Each is a sublattice of its own coordinate box — PROVED by induction from Theorem 1, and independently EXHAUSTIVE two ways: the staircase operator of D6 returns each stage unchanged when swept over the whole ambient box, 6,912 cells at the first stage and 47,775,744 at the sixth, and at the first four stages every unordered pair of cells was tested directly, 97,323,996 pairs in all, with no failing meet or join. Each stage projects exactly onto the one below. The fill — cells over ambient box — falls strictly, 14.12% to 0.42%.

2. **The general theorems, for every cap.** Theorem 1 (one coordinate per bound), Theorem 2 (the monotone envelope: existence, uniqueness, and its computation fibre by fibre), Theorem 3 (the triangle: join-closed, meet-broken), Theorem 4 (the band Bₖ a sublattice for every constant k; the three-variable region with a free bound join-closed and not a sublattice) and Theorem 5 (what an exact set of each shape costs) are PROVED in full. Theorems 1, 3 and 4, and the join-closure and the meet-refutation of Theorem 5(iii), are MACHINE-CHECKED over the unbounded integers, so they hold at every cap rather than in one box; Theorem 1 is machine-checked a second time in finite-box form, over every subset of a 3 × 3 box and every monotone bound taking values in {−1, …, 2}. Theorem 2 is PROVED, and its content is EXHAUSTIVE at the five axes of Table 2; Theorem 5's instances in the tower are EXHAUSTIVE over the thirteen bounds. Both guards pass before any obligation is reported.

3. **The envelope at every adjoined axis.** Table 2 sets the exact fibre against the admissible one at each of the five axes: 1,054 of 1,654 cells realised at the ninth, 1,132 of 2,535 at the tenth, 2,310 (or 10,585, under the wider reading) of 13,585 at the eleventh, 22,275 of 70,905 at the twelfth and 128,225 of 199,130 at the thirteenth. The construction's bound is a member of Theorem 2's envelope family at every axis. It is the least member at the tenth axis, at the thirteenth and at the eleventh under the wider reading; at the ninth and the twelfth it is not, the least envelopes admitting 1,638 and 60,320 cells. At the thirteenth axis the exact set is the doublet 2J = 2K ± 1, the band B₁ is its least envelope, and the 70,905 cells between the two are one value per cell of the twelfth stage — the value 2J = 2K, excluded by parity at the 57,320 cells with 2K ≥ 1 and by the constant-side triangle itself at the 13,585 cells with 2K = 0. Neither exact thirteenth stage is a sublattice: above one cell of the twelfth stage, the cell with (2K, 2J) = (0, 1) and the cell with (1, 0) have their meet at (0, 0), which neither admits — REFUTATION, by that witness — and the staircase closure of either exact stage is exactly Λ₁₃.

4. **The constraint graph.** Thirteen vertices and thirteen edges at the top stage; cycle rank 0, 0, 1, 1, 1, 1 across the six; one triangle, first present at the tenth stage, on seniority, the target's occupancy and the target's spin; girth 3 from that stage and no cycle below it; treewidth 1, 1, 2, 2, 2, 2 by exact elimination search; the transfer the cut, in the sense that no edge joins a parent coordinate to a target coordinate. The single cycle is a coordinate with two parents whose bounds have one coordinate each — which costs the tree and costs nothing in closure. A single bound with two coordinates in it is the other thing entirely, and it is what breaks closure.

5. **The cylinder.** At every stage Λ ∩ {q = t} is exactly a product A(t) × B(t), and Σₜ |A(t)|·|B(t)| = |Λ| with defect zero. The parent sections fall and the target sections rise at every stage, the section sequence is log-concave and peaks at t = 2 at every stage, and the mean transfer rises from 1.4631 to 1.9159 up the tower. Two departures are priced: writing the core–orbit bound with the cell's own subshell rather than the cap costs 15,150 cells of factorisation at the twelfth stage and 45,450 at the thirteenth, 21.4% and 22.8% of the product; imposing the exact triangle there instead leaves 22,275 cells and breaks closure, with a closure defect of 35,570 and explicit failing meets.

6. **Rank, generators and chains.** The first stage is graded by the coordinate sum, with 18 rank values from 3 to 20, widest level 122 at rank 11, and |Λ| exactly eight times that level. Its seventeen join-irreducibles are exactly the seventeen cells min{x : xᵢ ≥ v}, one for each coordinate value above that coordinate's minimum; they carry twenty covering relations, and the number of down-sets of the resulting poset is 976, which is the Birkhoff correspondence verified rather than invoked. The number of maximal chains is **1,113,045,672**, computed by dynamic programming over the cover relations of the lattice itself, and every maximal chain has length 17.

7. **The bracket system.** For each of the five stage-to-stage projections, the set of ranks below a given rank above is a gap-free interval with both endpoints monotone, with maximum branching 4, 4, 6, 8 and 9. Composing the five brackets contains the direct bracket from the top stage to the first at every rank, with a slack of at most two rank units, and both routes cover the whole rank spectrum {3, …, 20} of the first stage.

8. **The seed.** The first stage is regenerated by the staircase from 7 of its cells, the second from 8 and the third from 9, each found by exact branch and bound over the covering signatures maximal under inclusion — 264, 442 and 688 of them. The minimality is MACHINE-CHECKED at all three stages: no 6, 7 or 8 cells witness every envelope step, decided by a solver over every subset of a dominance-reduced signature family (59, 61 and 63 signatures against 27, 28 and 29 steps), the two reductions being checked exact, and the non-vacuity and encoding-fidelity guards passed, before the solver is asked. The exhibited minima also realise every alphabet value, so the relaxation is tight. A greedy cover returns 7, 9 and 9, and the second of those is not the seed.

**What is not established here.** Every cell count is at one setting of the caps that make Λ finite, namely three shells for the parent and for the target, one unit of orbital angular momentum, three electrons of occupancy and one unit of target subshell — the counts change with the caps and the paper marks them as being at these caps. The structural results of §4 are proved for arbitrary caps and arbitrary bounds; the tables of §2, §6, §7, §8 and §9 are not. Nothing here bears on whether the thirteen coordinates are the right or the complete list for a physical transition; a fourteenth coordinate is outside the paper. The exact angular-momentum content used in §3 — which pairs (2S, 2L) occur in a subshell of equivalent electrons — is derived here by microstate enumeration and agrees with the standard tabulation, which is CITED; nothing in this paper measures a spectrum. The closure statements are statements about a set of integer tuples and its coordinatewise lattice operations; they are not claims that the atom realises every admitted tuple; §3 counts the gap between the two at every adjoined coordinate and §6 prices it at the twelfth. The last three coordinates are the labels of a one-electron coupling scheme, applied at every target occupancy as bookkeeping (§3); nothing here bears on which coupling scheme an atom realises.

**Status words.** Five are used and never merged.

| status | meaning |
|---|---|
| **PROVED** | a proof is written out below and every step is justified; a proof ends with ∎ |
| **MACHINE-CHECKED** | Z3 returned `unsat` on the negation of an obligation whose variables range over a named domain — the unbounded integers where stated, otherwise every subset of a named finite box or family — with the non-vacuity and encoding-fidelity guards passed first |
| **EXHAUSTIVE** | a decision procedure visited every case in a stated finite family, and the family's size is printed |
| **CITED** | taken from the literature, with the source |
| **REFUTATION** | a claim disproved by an explicit witness, which is printed |

The check program also prints GUARD. A GUARD is a soundness check on the checker — the two guards of §10, and the exactness checks of the seed's reductions — and is never the status of a result; Table 5 records each guard beside the rows it protects.

---

## §1 · Definitions

Throughout, d ≥ 2 is finite and all coordinates take values in ℤ.

**D1 (chain, box).** A **chain** is a finite non-empty totally ordered set of integers. For a finite non-empty set X of d-tuples, Aᵢ := { xᵢ : x ∈ X } is its **alphabet** at coordinate i, and

> Box(X) := ∏ᵢ Aᵢ,  the product of the alphabets over all d coordinates,

is its **box**. Under coordinatewise ∧ = min and ∨ = max, Box(X) is a lattice, since a subset of a chain is closed under min and max of its own elements.

**D2 (meet, join, sublattice).** For tuples x, y, write x ∧ y := (min(xᵢ, yᵢ))ᵢ and x ∨ y := (max(xᵢ, yᵢ))ᵢ. A set S ⊆ Box(S) is a **sublattice** if x ∧ y ∈ S and x ∨ y ∈ S for all x, y ∈ S. The paper says **closed** for this and for nothing else.

**D3 (bound, parent, arity).** A **bound** on coordinate i is an inequality of the form xᵢ ≤ β(x) or xᵢ ≥ β(x) where β is a function of the remaining coordinates. The **parents of the bound** are the coordinates β actually depends on, and its **arity** is their number; a bound of arity 0 is a constant bound. The **parents of a coordinate** are the union of the parents of its bounds. The distinction between the arity of a bound and the number of parents of a coordinate is the subject of §4 and §5, and it is not a distinction without a difference: a coordinate can have two parents and every bound of arity 1.

**D4 (monotone).** A function φ : A → ℤ on a chain is **monotone** if a ≤ a′ implies φ(a) ≤ φ(a′). For a chain A, a monotone φ satisfies φ(max(a, a′)) = max(φ(a), φ(a′)) and φ(min(a, a′)) = min(φ(a), φ(a′)): it is a homomorphism for both operations. This one-line observation is the engine of Theorem 1.

**D5 (extension by an axis).** Let S be a set of d-tuples and let F assign to each x ∈ S a finite non-empty set F(x) ⊆ ℤ. The **extension of S by F** is

> S ⋉ F := { (x, y) : x ∈ S, y ∈ F(x) },

a set of (d+1)-tuples. Every stage of the tower is the extension of the one below by one such F.

**D6 (the staircase and the defect).** For i ≠ j and a ∈ Aⱼ put

> φᵢⱼ(a) := max { yᵢ : y ∈ X, yⱼ ≤ a },  undefined when that set is empty,

and

> ℛ(X) := { x ∈ Box(X) : xᵢ ≤ φᵢⱼ(xⱼ) for all i ≠ j },  E(X) := |ℛ(X)| − |X|.

ℛ(X) is what the pairwise extents of X admit: every cell of the box whose value at each coordinate is within reach of its value at each other. E(X) counts the cells the extents admit and X does not. E(X) = 0 says the extents describe X exactly.

**D7 (rank).** For an integer tuple x, r(x) := Σᵢ xᵢ. Where the set under study is graded by r — every cover raising r by 1 — r is a rank function in the order-theoretic sense; §7 verifies this for the first stage.

**D8 (constraint graph).** The **constraint graph** of a construction has the coordinates as vertices and an edge {i, j} whenever some bound on one of them has the other among its parents. Its **cycle rank** is |E| − |V| + c, with c the number of connected components; its **girth** is the length of a shortest cycle, undefined when there is none; its **treewidth** is the least width of a tree decomposition — Robertson and Seymour (1986), CITED — computed here by exact search over elimination orderings.

**D9 (the coordinates).** The thirteen coordinates, in the order in which they enter, with the shorthand used throughout:

| # | symbol | what it labels |
|----|-------|-----------------------------------------------------|
| 1 | n | the parent configuration's principal quantum number |
| 2 | ℓ | the parent subshell's orbital angular momentum |
| 3 | k | the number of electrons occupying that parent subshell |
| 4 | q | the number of electrons the transition transfers |
| 5 | e | the target configuration's principal quantum number |
| 6 | f | the target subshell's orbital angular momentum |
| 7 | g | the number of electrons the transition places in the target subshell |
| 8 | 2S | twice the parent's total spin |
| 9 | 2S′ | twice the target's total spin |
| 10 | v | the seniority of the target subshell |
| 11 | 2Jₚ | twice the total angular momentum of a term of the parent subshell ℓᵏ, as it stands before the transfer |
| 12 | 2K | twice the resultant of that momentum with the orbital angular momentum f of the target subshell, read as a single outer electron's |
| 13 | 2J | twice the total angular momentum, K coupled to a spin one-half |

All angular momenta are carried as twice their value so that every coordinate is an integer. **Λₛ** denotes the set of admissible s-tuples on the first s of these coordinates, and the six stages are Λ₈ ⋉ … = Λ₉, and so on to Λ₁₃.

**D10 (the bounds).** Λ₈ is the set of tuples (n, ℓ, k, q, e, f, g, 2S) of non-negative integers with

> 1 ≤ n ≤ nₘₐₓ,  0 ≤ ℓ ≤ min(ℓₘₐₓ, n − 1),  1 ≤ k ≤ min(kₘₐₓ, 4ℓ + 2),  0 ≤ q ≤ k,
> 1 ≤ e ≤ eₘₐₓ,  0 ≤ f ≤ min(fₘₐₓ, e − 1),  0 ≤ g ≤ min(4f + 2, q),  0 ≤ 2S ≤ k,

and the five extensions are

> 0 ≤ 2S′ ≤ g,  2S′ ≤ v ≤ g,  0 ≤ 2Jₚ ≤ φ̂(k),  0 ≤ 2K ≤ 2Jₚ + 2fₘₐₓ,  |2J − 2K| ≤ 1, 2J ≥ 0,

with φ̂ the monotone envelope of D12 below. Two readings of the twelfth bound must be kept apart and the paper keeps them apart throughout: fₘₐₓ is the **cap** on the sixth coordinate, a constant of the construction, and **not** the cell's own f. Written with the cap the bound has arity 1 — its only parent is 2Jₚ — and the tower closes and factorises. Written with the cell's own f the same bound has arity 2, and §5 and §6 price both differences exactly. The bounds on the last three coordinates are the labels of a one-electron coupling scheme; §3 says which, and what that assumes.

**D11 (the caps).** Every cell count in this paper is at

> (nₘₐₓ, eₘₐₓ, ℓₘₐₓ, kₘₐₓ, fₘₐₓ) = (3, 3, 1, 3, 1),

so that fₘₐₓ = 1 and the twelfth bound reads 0 ≤ 2K ≤ 2Jₚ + 2. Counts are cap-dependent; the theorems of §4 are not, and are proved for arbitrary bounds.

**D12 (terms, and the two envelopes read off them).** For a subshell of orbital angular momentum ℓ holding k equivalent electrons, terms(ℓᵏ) is the multiset of pairs (2S, 2L) obtained by **microstate enumeration**: list every choice of k of the 2(2ℓ+1) spin-orbitals, accumulate the resulting (2Mₗ, 2Mₛ), twice the projections of the total orbital and the total spin angular momentum — and strip complete (2S, 2L) blocks from the largest Mₗ downward until nothing is left. Two functions are read off this multiset and used as bounds:

> σ(ℓ, k) := max { 2S : (2S, 2L) ∈ terms(ℓᵏ) },  μ(ℓ, k) := max { 2S + 2L : (2S, 2L) ∈ terms(ℓᵏ) },

the largest spin and the largest total angular momentum a configuration of that shape can carry. φ̂(k) := max { μ(ℓ, k′) : ℓ ≤ ℓₘₐₓ, k′ ≤ k } is the **monotone envelope** of μ over the admitted parent shells — the running maximum, which is monotone in k by construction. §3 computes it, shows that it equals {1 ↦ 3, 2 ↦ 4, 3 ↦ 5} at the caps of D11, and shows why an envelope rather than μ itself is what the construction can carry.

**D13 (envelope step, slot, seed).** A triple (i, j, a) with i ≠ j and a ∈ Aⱼ is an **envelope step** of X when φᵢⱼ(a) ≠ φᵢⱼ(a′) for the predecessor a′ of a in Aⱼ, or when a is least in Aⱼ. A cell x ∈ X **witnesses** the step (i, j, a) when xⱼ ≤ a and xᵢ = φᵢⱼ(a). A pair (i, v) with v ∈ Aᵢ is a **slot** of X, and x **realises** it when xᵢ = v. A **seed** of X is a subset G ⊆ X with ℛ(G) = X, where ℛ(G) is computed as D6 says, in Box(G); seed(X) is the least size of a seed. §9 shows that G is a seed exactly when it witnesses every step and realises every slot, and computes the least size at the first three stages.

**D14 (the transfer decomposition).** Write A(t) := { (n, ℓ, k, 2S, 2Jₚ, 2K, 2J) : x ∈ Λ with q = t } for the **parent section** at transfer t and B(t) := { (e, f, g, 2S′, v) : x ∈ Λ with q = t } for the **target section**, each taken as a set of tuples and each restricted to the coordinates the stage carries. The construction **factorises over the transfer** when Λ ∩ { q = t } = A(t) × B(t) as sets, for every t.

---

## §2 · The six stages

Each stage is the extension of the one below by a single new coordinate, and the bounds are those of D10. The counts, computed by direct enumeration of the construction, are Table 1.

**Table 1. The tower at the caps of D11.** *Box* is the product of the alphabet sizes of the stage. *Fill* is |Λₛ| / |Box|. *Pairs* is the number of unordered pairs of distinct cells; the first four were tested one by one, the last two decided by the ambient sweep instead.

| stage | new coordinate | its bound | cells | box | fill | pairs |
|---|---|---|---|---|---|---|
| Λ₈ | — | — | 976 | 6,912 | 14.12% | 475,800 |
| Λ₉ | 2S′ | 0 ≤ 2S′ ≤ g | 1,654 | 27,648 | 5.98% | 1,367,031 |
| Λ₁₀ | v | 2S′ ≤ v ≤ g | 2,535 | 110,592 | 2.29% | 3,211,845 |
| Λ₁₁ | 2Jₚ | 0 ≤ 2Jₚ ≤ φ̂(k) | 13,585 | 663,552 | 2.05% | 92,269,320 |
| Λ₁₂ | 2K | 0 ≤ 2K ≤ 2Jₚ + 2fₘₐₓ | 70,905 | 5,308,416 | 1.34% | 2,513,724,060 |
| Λ₁₃ | 2J | ∣2J − 2K∣ ≤ 1 | 199,130 | 47,775,744 | 0.42% | 19,826,278,885 |

![](figures/stages.png)
**Figure 1.** Left: the cells of each stage, on a logarithmic axis. Right: the fill, the fraction of the ambient box the stage occupies, on a logarithmic axis. The object grows by a factor of 204 across the tower and the box it is written in grows by a factor of 6,912, so the fill falls strictly at every step, 14.12% to 0.42%.

**Proposition 1 (projection).** For s = 8, …, 12, deleting the last coordinate of Λₛ₊₁ gives exactly Λₛ, as a set.

*Proof.* Λₛ₊₁ = Λₛ ⋉ F for the F of D10, and every F(x) is a non-empty set of integers: [0, g], [2S′, g], [0, φ̂(k)], [0, 2Jₚ + 2fₘₐₓ] and [max(0, 2K − 1), 2K + 1] are each non-empty because in every case the lower limit is at most the upper — 2S′ ≤ g holds in Λ₉ by its own bound, and the other four have lower limit 0 or 2K − 1 ≤ 2K + 1. The projection of an extension by a set-valued map with non-empty values is the set that was extended. ∎ **PROVED**, and **EXHAUSTIVE**: verified as an equality of sets at all five projections.

**Proposition 2 (closure of every stage).** Every Λₛ, s = 8, …, 13, is a sublattice of Box(Λₛ), and E(Λₛ) = 0.

*Proof.* Λ₈ first. Each of its constraints is either a constant bound or has the form xᵢ ≤ φ(xⱼ) with φ monotone: ℓ ≤ n − 1, k ≤ 4ℓ + 2, q ≤ k, 2S ≤ k, f ≤ e − 1, g ≤ 4f + 2, g ≤ q, together with constant caps. Let x, y ∈ Λ₈ and fix such a constraint xᵢ ≤ φ(xⱼ).

*Join.* Put z = x ∨ y and suppose zᵢ = xᵢ (otherwise exchange x and y). Then zᵢ = xᵢ ≤ φ(xⱼ) ≤ φ(max(xⱼ, yⱼ)) = φ(zⱼ), the middle step by monotonicity.

*Meet.* Put w = x ∧ y and suppose wⱼ = xⱼ (otherwise exchange x and y; note the case split is now on j, not on i). Then wᵢ = min(xᵢ, yᵢ) ≤ xᵢ ≤ φ(xⱼ) = φ(wⱼ).

A constant bound c ≤ xᵢ ≤ C is preserved by both operations because min and max of two values in an interval lie in that interval. So Λ₈ is a sublattice.

Each of the five extensions has both of its bounds monotone in a single coordinate — 0 and g for 2S′; 2S′ and g for v; 0 and φ̂(k) for 2Jₚ, φ̂ monotone by D12; 0 and 2Jₚ + 2fₘₐₓ for 2K, with fₘₐₓ constant; 2K − 1 and 2K + 1 for 2J, together with the constant floor 0. Theorem 1 of §4 then carries the sublattice property up each step, and the tower closes by induction. Finally E(Λₛ) = 0 by Lemma 2 of §4: every bound of D10 is a constant, or is xᵢ ≤ ψ(xⱼ) or xᵢ ≥ ψ(xⱼ) with ψ monotone, which is all that lemma needs; the sweep of the whole ambient box confirms it at every stage. ∎ **PROVED**; **EXHAUSTIVE** three ways — the staircase swept over 6,912, 27,648, 110,592, 663,552, 5,308,416 and 47,775,744 ambient cells, returning each stage unchanged; every unordered pair tested at the first four stages, 475,800 + 1,367,031 + 3,211,845 + 92,269,320 = 97,323,996 pairs, zero failing meets and zero failing joins; and the counts of Table 1 reproduced from the construction.

> **Remark.** The two exhaustive routes are not the same check. The pair test decides the sublattice property directly and costs O(|Λ|²), which is 19.8 billion pairs at the top stage. The sweep decides ℛ(Λ) = Λ, which costs O(|Box|), and Lemma 1 of §4 shows that this implies the sublattice property. At the top stage the sweep is 47.8 million cells against 19.8 billion pairs, a factor of 415, which is why the upper stages are decided that way.

**Proposition 3 (strict fill decay).** The fill |Λₛ| / |Box(Λₛ)| is strictly decreasing in s over the six stages: 14.12%, 5.98%, 2.29%, 2.05%, 1.34%, 0.42%. **EXHAUSTIVE** at these caps.

The fill decay has a reason that does not depend on the caps. Adjoining a coordinate multiplies the box by the size of the new alphabet and multiplies the object by the mean size of the new fibre. A bounded coordinate has mean fibre strictly below its alphabet size unless every cell below it admits every value — that is, unless the bound is vacuous. So a coordinate that constrains anything lowers the fill. This is a statement about the construction, not a measurement, and it says nothing about the limit of a sequence continued past thirteen.

---

## §3 · What the coupling axes must carry

The five adjoined coordinates carry angular-momentum content fixed by the theory of equivalent electrons and by a coupling scheme. This section computes that content, says which scheme and what it assumes, and shows why the content cannot be carried as it stands.

**The terms of a subshell.** terms(ℓᵏ) is computed by microstate enumeration (D12). The construction is standard and is CITED to Condon and Shortley (1935), ch. VII, and Cowan (1981), ch. 4; the exclusion that makes the spin-orbitals distinct is Pauli's (1925), the vector-coupling rule that makes 2J run from |2L − 2S| to 2L + 2S in steps of two is Wigner's (1931), and the general classification of the terms of ℓᵏ is Racah's (1942b), all CITED. It is reproduced here because every bound below is read off its output and the paper recomputes what it prints. The first three cases of the p shell come out as

> terms(p¹) = { (1, 2) },  terms(p²) = { (0, 0), (0, 4), (2, 2) },  terms(p³) = { (1, 2), (1, 4), (3, 0) },

which are ²P; ¹S, ¹D, ³P; and ²P, ²D, ⁴S — the textbook anchors, EXHAUSTIVE over the enumeration.

**Proposition 4 (particle–hole symmetry).** terms(pᵏ) = terms(p⁶⁻ᵏ) for k = 1, 2. **EXHAUSTIVE.** The multiset of terms of a subshell and of its complement agree — the equivalence of a shell and its complement, Condon and Shortley (1935), ch. VII, and in the seniority-preserving form Racah (1943), both CITED; it is verified here on the shells the caps admit rather than assumed.

**Proposition 5 (the two realised maxima are not monotone).** With σ and μ as in D12,

| k, the number of equivalent electrons in the p subshell | 1 | 2 | 3 | 4 | 5 | 6 |
|------------------|--|--|--|--|--|--|
| σ(1, k), the largest 2S of pᵏ | 1 | 2 | 3 | 2 | 1 | 0 |
| μ(1, k), the largest 2S + 2L of pᵏ | 3 | 4 | 5 | 4 | 3 | 0 |

and σ(0, 1) = 1, σ(0, 2) = 0, μ(0, 1) = 1, μ(0, 2) = 0. Both rows rise to half filling and fall to zero at closure. **EXHAUSTIVE**, over the eight subshells the caps admit.

Neither row is monotone, and that is the obstruction. A bound xᵢ ≤ β(xⱼ) preserves the sublattice property when β is monotone (Theorem 1) and can fail when it is not (§4, the negative control). So the exact ceiling cannot be carried as a bound. What can be carried is its monotone envelope, and Theorem 2 says which one.

**Proposition 6 (the envelope of the realised maximum).** The running maximum of μ(1, ·) is 3, 4, 5, 5, 5, 5. It dominates μ(1, ·) everywhere and strictly exceeds it at k = 4, 5, 6. **EXHAUSTIVE.** At the caps of D11 only k ≤ 3 occurs, where the realised maximum is already monotone; there φ̂ = {1 ↦ 3, 2 ↦ 4, 3 ↦ 5} coincides with the realised maximum exactly. **That coincidence is a property of the caps and not of the bound**, and Proposition 6 is the demonstration: extend the caps by one electron of occupancy and the envelope separates from the extent.

**The spin ceiling, in closed form.** The exact spin ceiling of a subshell holding g electrons of orbital angular momentum f is min(g, 4f + 2 − g) — rising while the shell fills, falling once past half — and this reproduces σ(f, g) at every (f, g) the caps admit. **EXHAUSTIVE.** It is symmetric about half filling, hence non-monotone, hence not carriable; the construction carries 2S′ ≤ g, which dominates it since min(g, 4f+2−g) ≤ g.

**The core–orbit range.** At the caps, fₘₐₓ = 1, so the twelfth bound reads 2K ≤ 2Jₚ + 2, and over the construction max { 2K : 2Jₚ = j } = j + 2 for every j = 0, …, 5: the bound is attained and is not slack as a range. **EXHAUSTIVE.**

**What the last three coordinates label, and the scheme they come from.** The bound 0 ≤ 2Jₚ ≤ φ̂(k) is read off the terms of ℓᵏ, the parent subshell as it stands before the transfer. So 2Jₚ is the total angular momentum of a term of the parent configuration, not of the residual core ℓᵏ⁻ᑫ that the transfer leaves behind: at q = k the residual core is empty and its angular momentum is 0, while the bound still admits every value up to φ̂(k). The twelfth and thirteenth coordinates are then the labels of the J₁l coupling of Racah (1942a), CITED — the scheme in which a core of total angular momentum J₁ is coupled to the orbital angular momentum l of a single outer electron to give K, and K is coupled to that electron's spin one-half to give J = K ± ½ — with J₁ read as the parent term's J and l as the target subshell's f. That scheme is defined for one electron outside the core. The construction applies its labels at every target occupancy g ≤ 3, as bookkeeping: for g ≥ 2 the target's own term, with 2S′ as large as 3, would couple to the core and 2J would range from |2K − 2S′| to 2K + 2S′, which the thirteenth bound does not carry. The constant 1 in |2J − 2K| ≤ 1 is therefore the spin of one electron and a convention of the labelling, not a consequence of the cell's ninth coordinate; the results of this paper are about the tuples that labelling admits, and every count is at that reading. A reading in which the core is the residual ℓᵏ⁻ᑫ would replace φ̂(k) by a bound with two parents, k and q, and is not priced here.

### §3.1 · What the envelope costs, axis by axis

The envelope admits cells the exact physics does not. That gap is a count, and it is the quantity Theorem 2 makes into a definition. For each axis, the **admissible fibre** at a cell of the stage below is the interval the bound of D10 allows, and the **exact fibre** is the set vector coupling realises there. Summing both over the stage below gives Table 2.

**Table 2. The exact fibre, the admissible one, and the least envelope.** *Admitted* is the count under the construction's bound, which is the stage's own cell count; *least* is the count under Theorem 2's least envelope with the same parent indices; *realised* is the summed exact fibre, and the share is realised over admitted. *Empty* counts the cells of the stage below at which the exact fibre is empty — cells the envelope one step below admitted and no term realises — which contribute 0 to *realised* and are left out of the minima and maxima that define the least envelope. All at the caps of D11.

| axis | coordinate | admissible fibre | exact fibre | admitted | least | realised | share | empty |
|------|-------|---------|------------------|-------|------|-------|-----|-----|
| 9 | 2S′ | [0, g] | the 2S values of terms(fᵍ) | 1,654 | 1,638 | 1,054 | 63.7% | 0 |
| 10 | v | [2S′, g] | the seniorities v ≡ g (mod 2), v ≤ 4f + 2 − g, at which a term of spin 2S′ is new in fᵛ | 2,535 | 2,535 | 1,132 | 44.7% | 600 |
| 11 | 2Jₚ | [0, φ̂(k)] | the 2J of the terms of ℓᵏ carrying the cell's own 2S | 13,585 | 12,425 | 2,310 | 17.0% | 1,305 |
| 11 (wider) | 2Jₚ | [0, φ̂(k)] | the interval [0, μ(ℓ, k)], μ the largest 2J any term of ℓᵏ carries — an interval whose top is exact, not a set of physical values | 13,585 | 13,585 | 10,585 | 77.9% | 0 |
| 12 | 2K | [0, 2Jₚ + 2fₘₐₓ] | ∣2Jₚ − 2f∣ ≤ 2K ≤ 2Jₚ + 2f, 2K ≡ 2Jₚ (mod 2) | 70,905 | 60,320 | 22,275 | 31.4% | 0 |
| 13 | 2J | [max(0, 2K−1), 2K+1] | 2J = 2K ± 1 | 199,130 | 199,130 | 128,225 | 64.4% | 0 |

Every entry is EXHAUSTIVE over the stage below. The construction's interval is a member of Theorem 2's family at every axis — it contains the exact fibre at every cell, and its two bounds are monotone functions of one coordinate each — so the exact fibre is never larger than the admissible one; and the least member of the family, computed by Theorem 2(ii) with the construction's own parent indices (g at the ninth axis, 2S′ below and g above at the tenth, k at the eleventh, 2Jₚ at the twelfth, 2K at the thirteenth), is contained in the construction's interval cell by cell. The two coincide at the tenth axis, at the thirteenth, and at the eleventh under the wider reading. At the ninth the least envelope drops the value 0 at the sixteen cells with g = 3 — an odd number of electrons has half-integral spin, 2S′ ≡ g (mod 2) — and at the twelfth it raises the floor to 2Jₚ − 2 for 2Jₚ ≥ 3; at the eleventh under the strict reading it raises the floor to 1 at k = 3. Two rows are given for the eleventh axis because two different sets can be meant by *exact* there: the set of 2J the parent's terms carry given the cell's own parent spin, and the interval up to the largest 2J any term of the parent configuration carries. The first is the stricter and gives 17.0%; the second matches the bound's own shape and gives 77.9%, and it is an interval with an exact top rather than a set of physical values — p¹ has the single term ²P with 2J ∈ {1, 3}, and [0, 3] admits 0 and 2, which no term carries. The paper prints both and prefers neither.

The thirteenth row is the one to read against the thesis. Its exact fibre is the doublet 2J = 2K ± 1 everywhere except at 2K = 0, where it is the singleton {1} — 13,585 such cells, one for each cell of the eleventh stage. The admissible fibre is the triplet {2K−1, 2K, 2K+1} intersected with the non-negative integers, and it is the least envelope of the doublet: l⋆(a) = max(0, a − 1) and h⋆(a) = a + 1, by Theorem 2, and Theorem 5(iii) says why. So the last axis is carried as an envelope like the four before it, with a realised share of 64.4% and not 100%, and the loss is this axis's own. At every one of the 70,905 cells of the twelfth stage exactly one admitted value, 2J = 2K, is unphysical: at the 57,320 cells with 2K ≥ 1 because 2J must have the opposite parity to 2K, and at the 13,585 cells with 2K = 0 because the constant-side triangle |2K − 1| ≤ 2J ≤ 2K + 1 admits 1 alone there. Nothing about it is inherited through 2K, whose own envelope gap is the row above.

---

## §4 · The theorems

Everything in this section is stated for arbitrary chains, arbitrary bounds and arbitrary caps, and proved. Each is then machine-checked over the **unbounded integers**, so that the machine check is not a check at one setting of the caps: the solver is asked for a counterexample among all integer values of every variable and returns `unsat`. Two guards run first and the obligations are not reported unless both pass; §10 states them.

**Lemma 1 (the staircase produces a sublattice).** For any finite non-empty X, ℛ(X) is a sublattice of Box(X) containing X, and φᵢⱼ is monotone.

*Proof.* Monotonicity of φᵢⱼ first: if a ≤ a′ then {y ∈ X : yⱼ ≤ a} ⊆ {y ∈ X : yⱼ ≤ a′}, so the maximum over the second set is at least the maximum over the first. Containment: for x ∈ X and i ≠ j, x itself is a member of {y ∈ X : yⱼ ≤ xⱼ}, so φᵢⱼ(xⱼ) ≥ xᵢ; and x ∈ Box(X) by D1. Now take x, y ∈ ℛ(X) and fix i ≠ j.

*Join.* Let z = x ∨ y and suppose zᵢ = xᵢ. Then zᵢ = xᵢ ≤ φᵢⱼ(xⱼ) ≤ φᵢⱼ(max(xⱼ, yⱼ)) = φᵢⱼ(zⱼ) by monotonicity.

*Meet.* Let w = x ∧ y. Suppose wᵢ = xᵢ, so xᵢ ≤ yᵢ. If wⱼ = xⱼ then wᵢ = xᵢ ≤ φᵢⱼ(xⱼ) = φᵢⱼ(wⱼ). If wⱼ = yⱼ then wᵢ = xᵢ ≤ yᵢ ≤ φᵢⱼ(yⱼ) = φᵢⱼ(wⱼ). The case wᵢ = yᵢ is symmetric.

Both operations stay inside Box(X) because min and max of two members of a chain are members of it. ∎ **PROVED.**

> **Corollary.** If ℛ(X) = X then X is a sublattice of Box(X), and E(X) = 0. This is why the upper stages of §2 are decided by a sweep of the ambient box rather than by testing pairs: at the thirteenth stage the sweep is 47.8 million cells and the pair test 19.8 billion. The converse is not claimed and is not used.

**Lemma 2 (the staircase is exact on a set cut out by monotone one-coordinate bounds).** Let X be a non-empty finite set of d-tuples defined inside a product of chains by a finite list of constraints, each of one of three forms: a constant bound c ≤ xᵢ ≤ C; an upper bound xᵢ ≤ ψ(xⱼ); or a lower bound xᵢ ≥ ψ(xⱼ), with i ≠ j and every ψ monotone. Then ℛ(X) = X, and E(X) = 0.

*Proof.* ℛ(X) ⊇ X by Lemma 1, so it suffices to show that a cell x ∈ ℛ(X) satisfies every constraint. A constant bound: x ∈ Box(X), so xᵢ lies in the alphabet Aᵢ(X), every member of which satisfies c ≤ xᵢ ≤ C. An upper bound xᵢ ≤ ψ(xⱼ): x ∈ ℛ(X) gives xᵢ ≤ φᵢⱼ(xⱼ) = max { yᵢ : y ∈ X, yⱼ ≤ xⱼ }, and every such y has yᵢ ≤ ψ(yⱼ) ≤ ψ(xⱼ), by the constraint at y and the monotonicity of ψ; so xᵢ ≤ ψ(xⱼ). A lower bound xᵢ ≥ ψ(xⱼ): x ∈ ℛ(X) gives xⱼ ≤ φⱼᵢ(xᵢ), and the maximum defining φⱼᵢ(xᵢ) is attained by some y ∈ X with yᵢ ≤ xᵢ and yⱼ = φⱼᵢ(xᵢ) ≥ xⱼ; then ψ(xⱼ) ≤ ψ(yⱼ) ≤ yᵢ ≤ xᵢ, the first step by monotonicity and the second by the constraint at y. So x satisfies every constraint, and x ∈ X. ∎ **PROVED.**

> The lemma uses the shape of the bounds and nothing about the constraint graph: it holds at every stage, at every cap, with or without the cycle of §5. Every bound of D10 is of one of the three forms — the two lower bounds are 2S′ ≤ v, with ψ the identity, and 2J ≥ 2K − 1 — so E(Λₛ) = 0 at all six stages is a consequence of Lemma 2, and with Lemma 1 it is a second proof that each stage is a sublattice, independent of the induction through Theorem 1. The sweep of §2 confirms it. A related fact in the vocabulary of constraint satisfaction is that a network of max-closed constraints is decided by arc consistency, whatever its graph — Jeavons and Cooper (1995), CITED; the sets here are both max-closed and min-closed.

Sublattices of a product of chains cut out by inequalities between monotone functions of single coordinates are a standard object — Topkis (1978; 1998, ch. 2), CITED, whose sublattice constructions underlie the monotone comparative statics of Milgrom and Shannon (1994), CITED. Theorem 1 is that fact stated for the extension of a sublattice by one coordinate, and Theorem 4(i) is its two-coordinate instance; both are CITED, and both are proved here because the proofs are short and their shape is used again in Theorems 3 and 5.

**Theorem 1 (a coordinate whose every bound has arity 1).** Let S be a sublattice of Box(S) on coordinates 1, …, d. Let j and j′ be coordinate indices, not necessarily distinct, and let

> lo : Aⱼ → ℤ  and  hi : Aⱼ′ → ℤ

be monotone with lo(xⱼ) ≤ hi(xⱼ′) for every x ∈ S. Then

> S⁺ := { (x, y) : x ∈ S, lo(xⱼ) ≤ y ≤ hi(xⱼ′) }

is a sublattice of Box(S⁺).

*Proof.* S⁺ is non-empty because each fibre is non-empty. Take (x, y) and (u, w) in S⁺.

*Join.* Its join is (x ∨ u, max(y, w)), and x ∨ u ∈ S because S is a sublattice. For the upper bound, y ≤ hi(xⱼ′) and w ≤ hi(uⱼ′), so

> max(y, w) ≤ max( hi(xⱼ′), hi(uⱼ′) ) = hi( max(xⱼ′, uⱼ′) ) = hi( (x ∨ u)ⱼ′ ),

the middle equality being D4 applied to the monotone hi on the chain Aⱼ′. For the lower bound, D4 applied to lo gives

> lo( (x ∨ u)ⱼ ) = lo( max(xⱼ, uⱼ) ) = max( lo(xⱼ), lo(uⱼ) ) ≤ max(y, w),

since lo(xⱼ) ≤ y and lo(uⱼ) ≤ w.

*Meet.* Its meet is (x ∧ u, min(y, w)) with x ∧ u ∈ S, and the two displays run the other way: min(y, w) ≥ min(lo(xⱼ), lo(uⱼ)) = lo(min(xⱼ, uⱼ)) = lo((x ∧ u)ⱼ) and min(y, w) ≤ min(hi(xⱼ′), hi(uⱼ′)) = hi((x ∧ u)ⱼ′).

So both lie in S⁺. ∎ **PROVED**, and **MACHINE-CHECKED** twice: over the unbounded integers, with the two parent indices j and j′ carried as separate variables, the monotonicity hypothesis stated at the points where it is used and no bound on any variable; and in finite-box form over every one of the 2⁹ subsets of a 3 × 3 box that is closed, against every monotone h with values in {−1, 0, 1, 2}.

> **Where the hypothesis bites.** Monotonicity is not decoration. Drop it and the conclusion is false: the negative control asks the solver whether max(y, y′) ≤ h(x) at the larger x follows from y ≤ h(x), y′ ≤ h(x′) alone, and the solver returns a model. This is the reason §3's realised ceilings, which rise and then fall, cannot be carried as bounds.

> **Two parents, one per bound.** In Theorem 1 j and j′ may differ. The tenth coordinate is exactly that case: 2S′ ≤ v ≤ g has two parents and each of its two bounds has arity 1, so the theorem applies and the stage closes. What the second parent costs is a cycle in the constraint graph (§5) and nothing else. The cost that closure notices is a single bound of arity 2, and that is Theorem 3.

**Theorem 2 (the monotone envelope, existence and uniqueness).** Let S be a sublattice of Box(S), let j and j′ be coordinate indices, not necessarily distinct, and let F assign to each cell x ∈ S a finite non-empty set F(x) ⊆ ℤ; F may depend on every coordinate of x. For monotone l : Aⱼ → ℤ and h : Aⱼ′ → ℤ write S ⋉ [l, h] := { (x, y) : x ∈ S, l(xⱼ) ≤ y ≤ h(xⱼ′) }, and let 𝔈 be the family of all such sets that contain S ⋉ F. Then

> **(i)** 𝔈 is non-empty and every member of it is a sublattice;
>
> **(ii)** 𝔈 has a least member under inclusion, namely S ⋉ [l⋆, h⋆] with
>
> l⋆(a) := min { min F(x) : x ∈ S, xⱼ ≥ a },  h⋆(b) := max { max F(x) : x ∈ S, xⱼ′ ≤ b },
>
> for a ∈ Aⱼ and b ∈ Aⱼ′;
>
> **(iii)** S ⋉ [l⋆, h⋆] = S ⋉ F if and only if F(x) = [l⋆(xⱼ), h⋆(xⱼ′)] ∩ ℤ for every x ∈ S;
>
> **(iv)** the number of cells the least envelope admits and F does not is Σ ( h⋆(xⱼ′) − l⋆(xⱼ) + 1 − |F(x)| ), the sum over x ∈ S.

*Proof.* (i) The constant functions l ≡ min over x of min F(x) and h ≡ max over x of max F(x) are monotone and their interval contains every F(x), so 𝔈 ≠ ∅; and each member is a sublattice by Theorem 1, whose hypothesis l(xⱼ) ≤ h(xⱼ′) holds at every x because the fibre contains F(x).

**(ii)** l⋆ is monotone: as a increases the set { x : xⱼ ≥ a } shrinks, so its minimum does not decrease. h⋆ is monotone: as b increases the set { x : xⱼ′ ≤ b } grows, so its maximum does not decrease. Each set is non-empty, because a ∈ Aⱼ and b ∈ Aⱼ′ are values some cell takes. Taking x itself in each definition gives l⋆(xⱼ) ≤ min F(x) and h⋆(xⱼ′) ≥ max F(x), so F(x) ⊆ [l⋆(xⱼ), h⋆(xⱼ′)] and S ⋉ [l⋆, h⋆] ∈ 𝔈. Now let S ⋉ [l, h] ∈ 𝔈 be arbitrary. Containment forces l(xⱼ) ≤ min F(x) and h(xⱼ′) ≥ max F(x) for every x ∈ S. For a ∈ Aⱼ and any x with xⱼ ≥ a, monotonicity of l gives l(a) ≤ l(xⱼ) ≤ min F(x); taking the minimum over all such x gives l(a) ≤ l⋆(a). Symmetrically, for b ∈ Aⱼ′ and any x with xⱼ′ ≤ b, h(b) ≥ h(xⱼ′) ≥ max F(x), so h(b) ≥ h⋆(b). Hence [l⋆(xⱼ), h⋆(xⱼ′)] ⊆ [l(xⱼ), h(xⱼ′)] at every x, and S ⋉ [l⋆, h⋆] ⊆ S ⋉ [l, h]. A least member of a family ordered by inclusion is unique.

**(iii)** The two sets have the same first d coordinates, so they agree exactly when their fibres agree at every x, which is the stated condition.

**(iv)** The fibres are disjoint across cells of S, so the counts add. ∎ **PROVED.**

> **When a fibre is empty.** At the tenth and eleventh axes the exact fibre is empty at some cells — 600 and 1,305 of them, cells the envelope one step below admitted and no term of the physics realises. There the theorem is applied with the minima and maxima of (ii) taken over the cells with a non-empty fibre. The proof is unchanged provided l⋆(xⱼ) ≤ h⋆(xⱼ′) at every cell of S, so that every fibre of the envelope is non-empty, and the check verifies that at both axes. Such a cell contributes 0 to the realised count of Table 2 and h⋆ − l⋆ + 1 to the envelope's.

> **What the theorem does and does not say about the tower.** Theorem 2 is what "envelope" means in this paper: the envelope exists for *any* prescribed exact set, it is the *smallest* thing of the admissible shape that contains it, and (iv) counts what the smallest costs. The construction's bound at each axis is a member of 𝔈 — Table 2 verifies the containment cell by cell — but it is not always the least member. It is the least at the tenth axis, at the thirteenth and at the eleventh under the wider reading; at the ninth and the twelfth it admits 16 and 10,585 cells more than the least envelope does. Table 2's *least* column is clause (ii) evaluated at each axis with the construction's own parent indices, and clause (iv) is the difference between that column and the *realised* one.

**Theorem 3 (the triangle exclusion).** Let

> T := { (a, b, c) ∈ ℤ³ : a ≥ 0, b ≥ 0, c ≥ 0, |a − b| ≤ c ≤ a + b }.

Then T is closed under coordinatewise maximum and is not closed under coordinatewise minimum, and each of its two inequalities is broken by an explicit meet.

*Proof of join-closure.* Take u = (a₁, b₁, c₁) and w = (a₂, b₂, c₂) in T and write A = max(a₁, a₂), B = max(b₁, b₂), C = max(c₁, c₂); all three are non-negative.

*Upper.* C = cₜ for some t ∈ {1, 2}, and cₜ ≤ aₜ + bₜ ≤ A + B.

*Lower.* A = aₜ for some t. Then A − B ≤ aₜ − bₜ ≤ |aₜ − bₜ| ≤ cₜ ≤ C. Exchanging the roles of a and b gives B − A ≤ C. Hence |A − B| ≤ C. So (A, B, C) ∈ T. ∎

*Refutation of meet-closure.* Both inequalities fail, and one witness is exhibited for each.

> (0, 1, 1) ∧ (1, 0, 1) = (0, 0, 1) — both operands lie in T; the meet has c = 1 > 0 = a + b, so the **upper** bound fails: a total angular momentum manufactured from two zeros.
>
> (4, 0, 4) ∧ (2, 2, 0) = (2, 0, 0) — both operands lie in T; the meet has |a − b| = 2 > 0 = c, so the **lower** bound fails.

∎ **PROVED**; **MACHINE-CHECKED** (join-closure, over the unbounded integers, all caps at once); **REFUTATION** (meet-closure, the solver returning a model, and the two witnesses above verified independently).

> **Why max survives and min does not.** In the vocabulary of constraint satisfaction, T is a max-closed relation that is not min-closed — Jeavons and Cooper (1995) and Jeavons, Cohen and Gyssens (1997), CITED — and Theorem 4 says the same of C. T is cut out by one upper bound on c and one lower bound on c, and the coordinatewise maximum moves every coordinate in the direction each bound is slack on: raising a and b can only loosen c ≤ a + b, and raising c can only loosen |a − b| ≤ c, while the competing movement is dominated by the argument above. The coordinatewise minimum does the opposite on both, and there is no compensation, because the minimum takes a from one operand and c from the other and so forgets that c was built from that operand's own a and b.

**Theorem 4 (the bands).** For an integer constant k ≥ 0 let Bₖ := { (a, b) ∈ ℤ² : a ≥ 0, b ≥ 0, |a − b| ≤ k }, and let C := { (a, b, c) ∈ ℤ³ : a ≥ 0, b ≥ 0, c ≥ 0, |a − b| ≤ c }. Then

> **(i)** Bₖ is a sublattice, for every k ≥ 0;
>
> **(ii)** C is closed under coordinatewise maximum;
>
> **(iii)** C is **not** closed under coordinatewise minimum.

*Proof of (i).* Bₖ is cut out by a ≤ b + k and b ≤ a + k, each a bound of arity 1 whose right-hand side is monotone in its single parent, so Theorem 1 applies in both directions. The direct argument is four lines. Write A = max(a₁, a₂) and B = max(b₁, b₂). Choose t with A = aₜ; then B ≥ bₜ, so A − B ≤ aₜ − bₜ ≤ |aₜ − bₜ| ≤ k. Exchanging the roles of a and b gives B − A ≤ k, so |A − B| ≤ k and the join lies in Bₖ. For the meet write A′ = min(a₁, a₂), B′ = min(b₁, b₂), choose t with B′ = bₜ; then A′ ≤ aₜ, so A′ − B′ ≤ aₜ − bₜ ≤ k, and the exchanged argument gives B′ − A′ ≤ k. Non-negativity is preserved by both operations. ∎

*Proof of (ii).* This is the *Lower* half of Theorem 3's join argument, which used only |a − b| ≤ c and not c ≤ a + b. ∎

*Refutation of (iii).* (2, 0, 2) and (2, 2, 0) both lie in C; their meet is (2, 0, 0), and |2 − 0| = 2 > 0. ∎ **PROVED**; (i) and (ii) **MACHINE-CHECKED** over the unbounded integers, (i) with k itself a free integer variable so that the claim is decided for every constant at once; (iii) **REFUTATION**, the solver returning a model and the witness above verified independently.

> **The difference between Bₖ and C is the difference between a constant and a coordinate.** In Bₖ the second side of the band is a number, so a ≤ b + k is monotone in b; in C it is a free coordinate, so |a − b| ≤ c is a single bound of arity 2 and Theorem 1 does not apply. The same sentence, read in the other direction, is what the thirteenth axis of the tower carries: its bound |2J − 2K| ≤ 1 is B₁, a sublattice of arity 1, and the 1 is a constant — the spin one-half of a single outer electron in the coupling scheme whose labels the construction uses (§3). What B₁ is not is the exact set: the physics prescribes the doublet 2J = 2K ± 1, and Theorem 5(iii) says how B₁ stands to it.

**Theorem 5 (what an exact set of each shape costs).** Let S be a sublattice of Box(S) and let a new coordinate y carry an exact set F(x), finite and non-empty, at each x ∈ S.

> **(i)** If F(x) = [lo(xⱼ), hi(xⱼ′)] ∩ ℤ for monotone lo, hi of one coordinate each, then S ⋉ F is a sublattice: the axis closes exactly, and S ⋉ F is its own least envelope.
>
> **(ii)** If F(x) = { y : |xᵢ − xⱼ| ≤ y ≤ xᵢ + xⱼ } for two coordinates i ≠ j of S, and S realises the coordinate patterns of Theorem 3's two witnesses, then S ⋉ F is join-closed and is not meet-closed; its least envelope (Theorem 2) is a sublattice and is strictly larger.
>
> **(iii)** If F(x) = { y : |xᵢ − k| ≤ y ≤ xᵢ + k } for one coordinate i of S and an integer constant k ≥ 1, and the alphabet Aᵢ contains 0 and k, then S ⋉ F is join-closed and is not meet-closed; its least envelope is S ⋉ Bₖ := { (x, y) : x ∈ S, y ≥ 0, |y − xᵢ| ≤ k }, the band of Theorem 4 about xᵢ — a sublattice, of arity 1 — and it is strictly larger than S ⋉ F.

*Proof.* (i) is Theorem 1; and S ⋉ F ∈ 𝔈 is then the least member of 𝔈, since every member contains it.

**(ii)** Join-closure and the failure of meet-closure are Theorem 3 transported along (x, y) ↦ (xᵢ, xⱼ, y), which sends meets to meets and joins to joins because both are coordinatewise; the hypothesis that S realises the witness patterns is what makes the two witnesses of Theorem 3 lift to cells of S ⋉ F, and §6 exhibits such a pair. The envelope is Theorem 2 applied to F, and it is strictly larger because S ⋉ F is not a sublattice while S ⋉ [l⋆, h⋆] is.

**(iii)** *Join.* Take (x, y), (u, w) ∈ S ⋉ F and suppose max(xᵢ, uᵢ) = xᵢ (otherwise exchange the two). Then |max(xᵢ, uᵢ) − k| = |xᵢ − k| ≤ y ≤ max(y, w), and max(y, w) ≤ max(xᵢ + k, uᵢ + k) = max(xᵢ, uᵢ) + k; with x ∨ u ∈ S, the join lies in S ⋉ F. *Meet.* Choose x ∈ S with xᵢ = 0 and x′ ∈ S with x′ᵢ = k. Then (x, k) ∈ S ⋉ F, since |0 − k| = k ≤ k ≤ 0 + k, and (x′, 0) ∈ S ⋉ F, since |k − k| = 0 ≤ 0 ≤ 2k. Their meet is (x ∧ x′, 0), and (x ∧ x′)ᵢ = min(0, k) = 0, so membership would need |0 − k| ≤ 0, which fails for k ≥ 1. *Envelope.* F depends on x through xᵢ alone, so Theorem 2 with j = j′ = i gives l⋆(a) = min { |a′ − k| : a′ ∈ Aᵢ, a′ ≥ a } and h⋆(a) = max { a′ + k : a′ ∈ Aᵢ, a′ ≤ a } = a + k. Since k ∈ Aᵢ, for a ≤ k the minimum is attained at a′ = k and is 0; for a > k every a′ ≥ a has |a′ − k| = a′ − k ≥ a − k, attained at a′ = a. So l⋆(a) = max(0, a − k), and [l⋆(a), h⋆(a)] = { y ≥ 0 : |y − a| ≤ k } is the fibre of S ⋉ Bₖ. It is a sublattice by Theorem 2(i) — or directly by Theorem 1, with the two bounds y ≤ xᵢ + k and y ≥ xᵢ − k, each monotone of arity 1, and the constant floor 0. It is strictly larger: at a cell with xᵢ = 0 the envelope admits y = 0 and F does not. ∎ **PROVED**; the join-closure of (iii) **MACHINE-CHECKED** over the unbounded integers with k itself a free variable; its failure of meet-closure a **REFUTATION**, by the solver's model and by the witness (0, k) ∧ (k, 0) = (0, 0) verified for k = 1, …, 6; its envelope **EXHAUSTIVE** on the alphabets {0, …, M} for every k ≤ 6 and every k ≤ M ≤ 10, 56 cases.

> **The dichotomy, stated once.** An exact set closes exactly if and only if it is an interval between monotone bounds of one coordinate each: (i) is the "if", and Theorem 2(iii) is the "only if" against the envelope family. Everything else is carried as an envelope, and the shape of the exact set decides what the envelope costs. A triangle in two coordinates, (ii), and a triangle with one side constant, (iii), both fail meet-closure; the second is the cheaper, because its envelope is a band of arity 1 and its loss is confined to the cells with xᵢ < k. What the last axis of the tower adds to (iii) is a parity congruence, and §3.1 prices both.

**Corollary 1 (the tower).** Every one of the thirteen bounds of D10 is a constant or a monotone function of a single coordinate, so every bound has arity at most 1 and every stage closes (Proposition 2). None of the five adjoined coordinates carries its exact set: at each of the five axes the exact fibre is strictly smaller than the least envelope, so by Theorem 2(iii) it is not an interval between monotone one-coordinate bounds, and each axis is carried as a member of the envelope family. The shape of the exact set differs at each. At the ninth it is the spin set of the target's terms, which carries the parity 2S′ ≡ g (mod 2) and whose ceiling is non-monotone beyond the caps (Proposition 5 and the closed form min(g, 4f + 2 − g)); at the tenth, the set of occupancies at which a term is new, which is not an interval; at the eleventh, the set of 2J the parent's terms carry, whose ceiling is non-monotone beyond the caps (Proposition 5); at the twelfth, a triangle of arity 2 with a congruence, which by Theorem 5(ii) cannot be carried at all; at the thirteenth, a triangle with one side the constant 1, with a congruence, which by Theorem 5(iii) cannot be carried either and whose least envelope is B₁ — the bound the construction carries. **EXHAUSTIVE** over the thirteen bounds and the five axes of Table 2.

> **A coordinate cannot be smuggled in as a derived quantity.** Adjoining a function h of the existing coordinates keeps the object a sublattice only if the graph {(x, h(x))} is one, and taking joins there forces h(x ∨ x′) = max(h(x), h(x′)) — h must be a join homomorphism. A difference of two coordinates is not one. On the first stage, h = e − q has h(x ∨ x′) = 0 at x = (1,0,1,0,1,0,0,0) and x′ = (1,0,1,1,1,0,0,0), while max(h(x), h(x′)) = 1. **REFUTATION**, by that witness. Every coordinate above the eighth therefore has to enter as a *bounded axis* and pay the price Theorem 2 names; there is no cheaper door.

---

## §5 · The constraint graph

The constraint graph (D8) records which coordinates appear in which bounds. Reading it off D10 gives seven edges at the first stage and one or two more at each step:

| stage | the edges its new bounds add |
|--|-----------------------------|
| Λ₈ | n–ℓ, ℓ–k, k–q, k–2S, e–f, f–g, q–g |
| Λ₉ | g–2S′ |
| Λ₁₀ | 2S′–v, g–v |
| Λ₁₁ | k–2Jₚ |
| Λ₁₂ | 2Jₚ–2K |
| Λ₁₃ | 2K–2J |

The twelfth stage contributes **one** edge, not two. Its bound is 2K ≤ 2Jₚ + 2fₘₐₓ, and fₘₐₓ is the cap of D11 — a constant of the construction — so 2Jₚ is the bound's only parent (D3, D10). That reading is what §2 and §6 measure, and it is the reading the rest of this section reports.

![](figures/constraint-graph.png)
**Figure 2.** The constraint graph at the thirteenth stage. Thirteen vertices and thirteen edges. Rims mark the two kinds of coordinate: the eight of the first stage in the first colour, and the five adjoined coordinates — each carried as a monotone envelope of its exact set, Table 2 — in the second. The one independent cycle is the triangle on 2S′, g and v, drawn in the third colour; it is the tenth coordinate's two parents happening to be adjacent. Deleting q leaves exactly two connected pieces, the parent block and the target block; no edge joins the two blocks directly, so every path between them runs through q.

**Table 3. The graph, stage by stage.** Cycle rank is |E| − |V| + c; treewidth is exact, by search over elimination orderings.

| stage | vertices | edges | components | cycle rank | triangles | girth | treewidth |
|---|---|---|---|---|---|---|---|
| Λ₈ | 8 | 7 | 1 | 0 | 0 | — | 1 |
| Λ₉ | 9 | 8 | 1 | 0 | 0 | — | 1 |
| Λ₁₀ | 10 | 10 | 1 | 1 | 1 | 3 | 2 |
| Λ₁₁ | 11 | 11 | 1 | 1 | 1 | 3 | 2 |
| Λ₁₂ | 12 | 12 | 1 | 1 | 1 | 3 | 2 |
| Λ₁₃ | 13 | 13 | 1 | 1 | 1 | 3 | 2 |

**Proposition 7 (the shape of the graph).** At every stage the graph is connected. At the first two stages it is a tree — eight vertices and seven edges, then nine and eight. From the tenth stage it has cycle rank exactly 1, girth exactly 3, and exactly one triangle, namely {2S′, g, v}; its treewidth is 1 at the first two stages and 2 thereafter. At the thirteenth stage the degree sequence has k and g at 4 and n, e, 2S, 2J as leaves. **EXHAUSTIVE**, over the six stages, with the triangle census taken over all C(13, 3) = 286 vertex triples at the top stage and the treewidth by exact elimination search.

**Proposition 8 (the transfer is the cut).** Partition the coordinates into the **parent block** P = {n, ℓ, k, 2S, 2Jₚ, 2K, 2J}, the **target block** T = {e, f, g, 2S′, v}, and the transfer q alone. Then at every stage no edge joins a vertex of P to a vertex of T, the only edges at q are k–q and q–g, and deleting q leaves exactly two components — P and T, each restricted to the coordinates the stage carries, and each connected. Every path from P to T passes through q.

*Proof.* Read the edge list. Of the thirteen bounds, eleven name two coordinates of the same block — six inside P and five inside T — and the remaining two name q: g ≤ q names q and a coordinate of T, and q ≤ k names q and a coordinate of P. So no edge is a P–T edge, and q has degree 2 with one neighbour in each block. P is connected at every stage: n–ℓ–k with 2S pendant at k, and k–2Jₚ–2K–2J appended one vertex at a time from the eleventh stage. T is connected at every stage: e–f–g, with 2S′ and v attached to g from the ninth and tenth. Hence the deletion of q leaves those two connected pieces and nothing else, and every P–T path uses q. ∎ **PROVED**, and **EXHAUSTIVE**: verified at all six stages by deleting q and computing the component containing e, which is T exactly, every time.

**Proposition 9 (what the arity-2 reading would cost the graph).** Writing the twelfth bound with the cell's own f in place of the cap adds the edge f–2K. The thirteenth stage then has 13 vertices and **14** edges, and the cycle-rank sequence becomes 0, 0, 1, 1, 2, 2. The triangle count, the treewidth, the girth and the degrees of k and g are unchanged; the only degrees that move are those of f and 2K. **EXHAUSTIVE**, computed by substituting that one edge and rebuilding.

So the arity of that bound is visible in the graph as exactly one edge and one unit of cycle rank, and §6 prices the same difference in cells.

> **Cycle rank and closure are two different costs.** The single independent cycle arrives at the tenth stage, where v is bounded below by 2S′ and above by g, two coordinates already joined by an edge. That coordinate has two parents, and it costs the tree: treewidth rises from 1 to 2. What a tree buys, for a network of *arbitrary* binary constraints, is that arc consistency alone decides membership — Freuder (1982), CITED, with the consistency vocabulary of Freuder (1978) and the tree-clustering view of width in Dechter and Pearl (1989), both CITED — and at treewidth 2 that guarantee is not available for arbitrary constraints. The construction never needed it: E(Λₛ) = 0 at all six stages by Lemma 2, which uses the monotone shape of the bounds and nothing about the graph, and the same conclusion is available for max-closed networks whatever their graph (Jeavons and Cooper 1995, CITED). So what the cycle removes is a guarantee the construction does not use, and the cost that closure does notice is a different one: a single bound of arity 2, which Theorem 5(ii) shows cannot preserve the sublattice property at all. **A coordinate with two parents is cheap; a bound with two parents is not.**

---

## §6 · The cylinder over the transfer

The fourth coordinate, q, is the number of electrons a transition moves. Proposition 8 says it is where the two sides of the construction meet. This section shows what that costs and what it buys.

**Proposition 10 (exact factorisation).** At every stage, and for every value t of the transfer,

> Λ ∩ { q = t } = A(t) × B(t)  as sets,  and  Σₜ |A(t)| · |B(t)| = |Λ|,

with defect zero. **EXHAUSTIVE** at all six stages for the sum, and as a set identity at the first and the thirteenth.

*Proof.* Delete q from the constraint graph. By Proposition 8 the remainder splits into the parent component and the target component, so no bound of D10 other than the two bounds at q — q ≤ k and g ≤ q — names coordinates from both, and each of those is a bound on one side alone once q is fixed. Hence for a fixed t the admissibility of the parent coordinates and the admissibility of the target coordinates are independent conditions, and the fibre is their product. Summing over t partitions Λ. ∎ **PROVED**, and **EXHAUSTIVE** as stated.

**Table 4. The sections, at three stages.** |A(t)| is the number of distinct parent tuples at transfer t, |B(t)| the number of distinct target tuples.

| t | Λ₈: ∣A∣ × ∣B∣ | product | Λ₁₁: ∣A∣ × ∣B∣ | product | Λ₁₃: ∣A∣ × ∣B∣ | product |
|---|---|---|---|---|---|---|
| 0 | 33 × 5 | 165 | 163 × 5 | 815 | 2,294 × 5 | 11,470 |
| 1 | 33 × 10 | 330 | 163 × 20 | 3,260 | 2,294 × 20 | 45,880 |
| 2 | 23 × 15 | 345 | 123 × 50 | 6,150 | 1,794 × 50 | 89,700 |
| 3 | 8 × 17 | 136 | 48 × 70 | 3,360 | 744 × 70 | 52,080 |
| | **total** | **976** | | **13,585** | | **199,130** |

![](figures/sections-plate.png)
**Figure 3.** The four sections of the cylinder drawn at square-root-of-cell scale, the thirteenth stage solid and the first dashed inside it. The sections read 2,294 × 5, 2,294 × 20, 1,794 × 50 and 744 × 70 against 33 × 5, 33 × 10, 23 × 15 and 8 × 17.

![](figures/profile.png)
**Figure 4.** The same four sections as a profile, on a logarithmic axis, at the thirteenth stage (solid) and the first (dotted). The parent side falls and the target side rises at both scales; the section itself peaks at t = 2, at 89,700 cells at the top stage and 345 at the bottom.

**Proposition 11 (the profile).** At every one of the six stages: |A(t)| is non-increasing in t, |B(t)| is non-decreasing, the sequence of section sizes is log-concave, and it attains its maximum at t = 2. The mean transfer ⟨q⟩ = Σₜ t·|A(t)|·|B(t)| / |Λ| rises up the tower:

| stage | Λ₈ | Λ₉ | Λ₁₀ | Λ₁₁ | Λ₁₂ | Λ₁₃ |
|---|---|---|---|---|---|---|
| ⟨q⟩ | 1.4631 | 1.6850 | 1.8304 | 1.8874 | 1.9141 | 1.9159 |

**EXHAUSTIVE** at these caps. No value of the transfer improves both sides: raising it costs the parent and pays the target, monotonically, at every stage.

### §6.1 · What the arity-2 bound costs, in cells

Three readings of the twelfth bound are available, and the paper prices all three at the same caps. Write j = 2Jₚ and let f be the cell's own target subshell.

| reading | bound on 2K | arity | cells at Λ₁₂ | cells at Λ₁₃ | closed? | factorises? |
|---|---|---|---|---|---|---|
| the cap | 0 ≤ 2K ≤ j + 2fₘₐₓ | 1 | 70,905 | 199,130 | **yes**, E = 0 | **yes**, defect 0 |
| the cell's own f, upper bound only | 0 ≤ 2K ≤ j + 2f | 2 | 55,755 | 153,680 | no, E = 12,675 | no, defect 15,150 and 45,450 |
| the exact triangle with parity | ∣j − 2f∣ ≤ 2K ≤ j + 2f, 2K ≡ j (mod 2) | 2 | 22,275 | 64,290 | no, E = 35,570 | — |

**Proposition 12 (the price of the second parent).** Replacing the cap by the cell's own subshell in the twelfth bound leaves 55,755 cells at the twelfth stage against a section product of 70,905, a factorisation defect of **15,150 cells, 21.4% of the product**; at the thirteenth stage 153,680 against 199,130, a defect of **45,450 cells, 22.8%**. The same replacement breaks closure: the staircase returns 12,675 cells the construction does not hold. **EXHAUSTIVE** at these caps; **REFUTATION** for the closure claim.

**Proposition 13 (the exact triangle does not close).** Imposing the full triangle |2Jₚ − 2f| ≤ 2K ≤ 2Jₚ + 2f with the parity congruence 2K ≡ 2Jₚ (mod 2) leaves 22,275 cells at the twelfth stage. That set is not a sublattice. Of its 248,076,675 unordered pairs, **52,767,450 have a meet outside it and 28,742,850 have a join outside it**, and its closure defect is E = 35,570 — larger than the set itself. An explicit failing meet, in the coordinate order of D9:

> (1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 4, 4) ∧ (1, 0, 1, 0, 2, 1, 0, 0, 0, 0, 2, 0) = (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0),

whose (2Jₚ, 2f, 2K) = (2, 0, 0) violates |2Jₚ − 2f| ≤ 2K. **REFUTATION**, and this is Theorem 3's second witness realised inside the construction, which is the hypothesis Theorem 5(ii) requires.

> The join failures are worth separating from the meet failures. Theorem 3 says the triangle *without* the congruence is join-closed; here joins fail too, 28.7 million of them, and the reason is the congruence 2K ≡ 2Jₚ (mod 2), which is not an inequality at all and is preserved by neither operation. So the twelfth axis's exact content carries two independent obstructions — a bound of arity 2 and a congruence — and the construction's envelope drops both.


---

## §7 · Rank, generators and maximal chains

This section is about the first stage as a lattice in its own right. Everything in it is at the caps of D11.

**Lemma 3 (distributivity).** Every Λₛ is a distributive lattice.

*Proof.* A product of chains is distributive, since min and max on a totally ordered set satisfy both distributive laws and the operations on a product act coordinatewise. A sublattice of a distributive lattice is distributive, because the identities are inherited (Birkhoff 1967; Davey and Priestley 2002; Grätzer 2011, CITED for the standard facts). Λₛ is a sublattice of Box(Λₛ) by Proposition 2, and it is non-empty and finite, so it has a least and a greatest element — the coordinatewise minimum and maximum of all its cells, which lie in it by repeated meet and join. ∎ **PROVED**; the bottom and the top of the first stage are (1,0,1,0,1,0,0,0) at rank 3 and (3,1,3,3,3,1,3,3) at rank 20, **EXHAUSTIVE**. Conversely every finite distributive lattice embeds in a product of chains, as many as the width of its poset of join-irreducibles — Dilworth (1950), CITED — so distributivity singles nothing out; what is particular to Λₛ is that the chains of its embedding are the coordinates themselves.

**Proposition 15 (grading).** For every stage, the rank r(x) = Σᵢ xᵢ takes its least value 3. The numbers of distinct rank values are 18, 21, 24, 29, 36 and 44 across the six stages. On the first stage the rank sequence, from rank 3 to rank 20, is

> 1, 5, 15, 34, 59, 87, 108, 121, **122**, 115, 100, 79, 57, 37, 21, 10, 4, 1,

which is log-concave, and whose widest level is 122 at rank 11 — so |Λ₈| = 976 = 8 × 122 exactly. The second stage's widest level is 185 at rank 12. **EXHAUSTIVE** at these caps.

**Definition (generator).** For a coordinate i and a value v ∈ Aᵢ above the least value of Aᵢ, the **generator** G(i, v) is the coordinatewise minimum of { x ∈ Λ₈ : xᵢ ≥ v }.

**Proposition 16 (the seventeen generators are the join-irreducibles).** Every G(i, v) is a cell of Λ₈, and the generators are exactly the join-irreducible elements of Λ₈. Their number is

> Σᵢ (|Aᵢ| − 1) = (3−1) + (2−1) + (3−1) + (4−1) + (3−1) + (2−1) + (4−1) + (4−1) = 17,

and for every cell x,

> |{ G : G a generator, G ≤ x }| = r(x) − 3.

Hence Λ₈ is graded by r − 3, every covering relation of Λ₈ is a unit step in one coordinate, and the partial order the generators inherit has exactly **20** covering relations.

*Proof that G(i, v) is a cell.* The set { x ∈ Λ₈ : xᵢ ≥ v } is non-empty, since v ∈ Aᵢ, and is closed under meet: if xᵢ ≥ v and yᵢ ≥ v then (x ∧ y)ᵢ ≥ v. A non-empty finite meet-closed subset of Λ₈ contains its own coordinatewise minimum, which is the meet of all its members. ∎

*Proof that the generators are the join-irreducibles.* Let G = G(i, v) and suppose G = a ∨ b with a, b ∈ Λ₈. Then Gᵢ = max(aᵢ, bᵢ) ≥ v, so one of a, b — say a — has aᵢ ≥ v, hence a ≥ G by the minimality of G in { x : xᵢ ≥ v }; with a ≤ G this gives a = G. So G is join-irreducible, and it is not the bottom, since v exceeds the least value of Aᵢ. Conversely, let p be join-irreducible and not the bottom. For each coordinate i at which pᵢ exceeds the least value of Aᵢ, G(i, pᵢ) ≤ p, since p ∈ { x : xᵢ ≥ pᵢ }. The join of these generators is ≤ p, and its i-th coordinate is ≥ pᵢ at every such i and equals the least value of Aᵢ elsewhere, as p's does; so it equals p. A join-irreducible element that is a join of generators is one of them. ∎ **PROVED.**

*The count and the grading.* That the seventeen generators are distinct, that |{ G ≤ x }| = r(x) − 3 at all 976 cells, and that the generator poset has 20 covering relations, are **EXHAUSTIVE**. In a finite distributive lattice the rank of x is the number of join-irreducibles below it (Birkhoff 1937; Davey and Priestley 2002, CITED), so the grading of Λ₈ is r − 3. A cover therefore raises r by exactly 1, and since a cover x ⋖ y has x ≤ y coordinatewise, it raises exactly one coordinate by exactly 1 — a unit step. That is what justifies finding lower covers by testing the eight unit decrements for membership, which is how the check finds them; and found that way, the seventeen generators are the seventeen cells with exactly one lower cover, **EXHAUSTIVE** — a second verification of join-irreducibility, against the proof above.

**Proposition 17 (Birkhoff, verified).** The lattice of down-sets of the seventeen-element generator poset has exactly **976** elements, one for each cell of Λ₈. **EXHAUSTIVE**, by direct enumeration of the down-sets.

This is Birkhoff's representation theorem — a finite distributive lattice is the lattice of down-sets of its poset of join-irreducibles, Birkhoff (1937), CITED — computed rather than invoked, on this lattice.

**Theorem 6 (the maximal chains).** The saturated chains from the bottom of Λ₈ to its top number exactly

> **1,113,045,672**,

and every one of them has length 17.

*Proof.* By Proposition 16 the map x ↦ { G : G ≤ x } carries Λ₈ isomorphically onto the down-sets of the generator poset P (Proposition 17), and it carries r(x) − 3 to the size of the down-set. A saturated chain from bottom to top is therefore a sequence of down-sets each obtained from the last by adding one element of P, which is precisely a linear extension of P (Stanley 2012, ch. 3, CITED for the correspondence); and its length is |P| = 17 = r(top) − r(bot) = 20 − 3. The count is the number of paths from the bottom to the top in the Hasse diagram of Λ₈, which satisfies the recursion

> c(bot) = 1,  c(x) = Σ { c(y) : y a lower cover of x },

well-founded because r strictly decreases along lower covers. Evaluating it over all 976 cells in order of rank gives the stated number. ∎ **PROVED**, and **EXHAUSTIVE**: the recursion evaluated at every cell, with lower covers found by testing the eight unit decrements for membership. A **negative control** is reported by the selftest: counting the chains of the *ambient box* instead — the multinomial on the coordinate spans, 17!/(2!1!2!3!2!1!3!3!) — gives a different number, so the count is not an artefact of ignoring membership.

---

## §8 · The bracket system

The stages are related by projection (Proposition 1). The rank of D7 is defined on all of them, and this section asks what the rank of a cell at one stage says about the rank of its projection at the stage below. The answer is never a single value; it is always an interval, and the intervals compose.

**Definition (the stage bracket).** For s = 9, …, 13 and an integer m, let π delete the last coordinate and put

> βₛ(m) := { r(π(x)) : x ∈ Λₛ, r(x) = m }.

Its **branching** at m is |βₛ(m)|.

**Proposition 18 (each stage bracket is a monotone gap-free interval).** For every s = 9, …, 13 and every rank m realised at that stage, βₛ(m) is a set of consecutive integers, and both min βₛ and max βₛ are non-decreasing in m. The largest branching is 4, 4, 6, 8 and 9 respectively — growing with height. **EXHAUSTIVE**, over all cells of all five stages: 1,654 + 2,535 + 13,585 + 70,905 + 199,130.

![](figures/brackets.png)
**Figure 5.** The five stage brackets and their composite. In each of the first five panels the shaded band is [min βₛ(m), max βₛ(m)] against m; in the sixth the shaded band is the composition of all five and the solid outline is the direct bracket from the thirteenth stage to the first. The composite contains the direct bracket everywhere, and exceeds it by at most two rank units.

**Definition (the direct bracket).** δ(m) := { r(x₁, …, x₈) : x ∈ Λ₁₃, r(x) = m }, the ranks of the eight-coordinate projection of a top-stage cell of rank m.

**Proposition 19 (composition, and its slack).** Write βₛ[a, b] := [ min βₛ(m), max βₛ(m) ], the minimum and the maximum taken over m ∈ [a, b], for the image of an interval. Then for every rank m of the thirteenth stage,

> δ(m) ⊆ β₉[ β₁₀[ β₁₁[ β₁₂[ β₁₃[m, m] ] ] ] ],

the composed bracket contains the direct one; the excess is at most **2** rank units at the lower end and **0** at the upper; δ(m) is itself a gap-free interval at every m; and both the direct image and the composed image cover the whole rank spectrum of the first stage, {3, 4, …, 20}. **EXHAUSTIVE**, over all 199,130 cells of the thirteenth stage.

> **What the bracket system says.** Each projection loses information, and the loss has a shape: not an error, and not a single wrong value, but a resolution. The rank of a thirteen-coordinate cell determines its eight-coordinate rank only up to an interval, and composing the five one-step statements gives an interval that contains the true one and is wider by at most two units. That the composed answer contains the direct one is what makes the five statements usable as a chain; that the slack is bounded, and bounded by 2 rather than by the sum of five branchings, is what makes the chain worth composing.

---

## §9 · The seed

How much of the first stage must one hold to recover all of it? The staircase ℛ of D6 answers, and the answer is seven cells.

**Lemma 4 (a seed is a cover of the steps and the slots).** Let X satisfy ℛ(X) = X and let G ⊆ X be non-empty; write φᵢⱼ for the boundary functions of X (D6) and φᴳᵢⱼ for those of G. Then ℛ(G) = X **if and only if** G realises every slot of X and witnesses every envelope step of X (D13).

*Proof.* (⇒) Suppose ℛ(G) = X. Slots: ℛ(G) ⊆ Box(G) by D6 and G ⊆ X, so Box(X) = Box(ℛ(G)) ⊆ Box(G) ⊆ Box(X); hence Aᵢ(G) = Aᵢ(X) for every i, which says every slot is realised. Steps: fix i ≠ j and a ∈ Aⱼ. Every x ∈ X = ℛ(G) with xⱼ ≤ a satisfies xᵢ ≤ φᴳᵢⱼ(xⱼ) ≤ φᴳᵢⱼ(a), the second step by monotonicity of φᴳᵢⱼ (Lemma 1); taking the maximum over such x gives φᵢⱼ(a) ≤ φᴳᵢⱼ(a), and G ⊆ X gives the reverse. So φᴳᵢⱼ(a) = φᵢⱼ(a), and the maximum defining φᴳᵢⱼ(a) is attained by some g ∈ G with gⱼ ≤ a and gᵢ = φᵢⱼ(a) — a witness of (i, j, a), whether or not a is a step.

(⇐) Suppose G realises every slot and witnesses every step. The slots give Box(G) = Box(X), so ℛ(G) and ℛ(X) are cut from the same box, and it remains to show φᴳᵢⱼ = φᵢⱼ on Aⱼ for all i ≠ j. At a step point a there is x ∈ G with xⱼ ≤ a and xᵢ = φᵢⱼ(a), so φᴳᵢⱼ(a) ≥ φᵢⱼ(a); and G ⊆ X gives φᴳᵢⱼ(a) ≤ φᵢⱼ(a). Hence equality at every step point. Now take any b ∈ Aⱼ and let a ≤ b be the largest step point at or below b; one exists because the least element of Aⱼ is a step point by D13. By the definition of a step there is no step in (a, b], so φᵢⱼ is constant there and φᵢⱼ(b) = φᵢⱼ(a). Both functions are non-decreasing (Lemma 1), so

> φᵢⱼ(a) = φᴳᵢⱼ(a) ≤ φᴳᵢⱼ(b) ≤ φᵢⱼ(b) = φᵢⱼ(a),

and the two agree at b. Same box, same boundary functions: ℛ(G) = ℛ(X) = X. ∎ **PROVED**, and supported by a **GUARD**: on 40 pseudorandom subsets of Λ₈ (seed 11), "witnesses every step" agreed with "regenerates Λ₈ under an independently written staircase over the fixed box of Λ₈" in 40 of 40 cases, "witnesses every step and realises every slot" agreed with "regenerates Λ₈ under the staircase over the subset's own box" in 40 of 40, and the exhibited seed with one cell removed failed both.

So seed(X) is the optimum of a minimum set cover: the elements are the steps and the slots, the sets are the cells, and a cell covers what it witnesses and realises. Minimum set cover is NP-complete in general — Karp (1972), CITED — and the instances here are solved exactly by branch and bound, with the minimality certified a second time by a solver.

**Theorem 7 (the seed of the first three stages).** seed(Λ₈) = 7, seed(Λ₉) = 8, seed(Λ₁₀) = 9.

*Proof.* Two halves, an exhibit and a lower bound, at each stage.

*Lower.* Drop the slots and ask only for a set of cells witnessing every step: 77 steps at the first stage, 105 at the second, 138 at the third. Any seed does this (Lemma 4), so the least such set bounds the seed below. Two cells that witness the same set of steps are interchangeable, so the instance is a set cover over the **distinct covering signatures** — 808, 1,376 and 2,111 of them — and a signature contained in another may always be replaced by the larger without growing a cover, so the optimum may be sought among the signatures **maximal under inclusion**: 264, 442 and 688. Branch and bound over those families returns **7, 8 and 9**. It is exact in the sense that every branch not pruned by the bound is visited, and the bound is this: with c signatures chosen, m steps still uncovered and M the largest number of them any one signature covers, at least ⌈m / M⌉ more signatures are needed, so the branch is abandoned when c + ⌈m / M⌉ is at least the best cover found, and also when c + 1 is, since a non-empty remainder needs at least one more. The same optimum is certified a second time by a solver, on an instance reduced by two exact steps whose exactness the check verifies rather than assumes: a step that is witnessed by every cell witnessing some other step may be dropped, since covering the second covers the first, which leaves 27, 28 and 29 steps; and, after that restriction, signatures are again replaced by the maximal ones, leaving 59, 61 and 63. Asked whether any 6, 7 or 8 of those signatures cover the kept steps, the solver returns `unsat` at each stage — reported only after a non-vacuity guard (the same clauses are satisfiable with 7, 8 or 9 signatures, and the solver's model is a cover) and an encoding-fidelity guard (the clause set, evaluated at concrete assignments, agrees with the direct cover test on the exhibited minimum carried into the reduced instance, on that cover with each member removed, and on 40 random subsets of the reduced family) have passed. The lower bound is therefore 7, 8 and 9.

*Upper.* The minimum step cover found by the branch and bound is exhibited at each stage, and it happens also to realise every slot — 25, 29 and 33 of them. By Lemma 4 it is a seed, so seed(Λₛ) is at most 7, 8 and 9, and the relaxation is tight. This was confirmed twice more by running two independently written staircases over the exhibited set — one over the fixed box of the stage, one over the set's own box — and comparing the output to the stage cell by cell. ∎ **EXHAUSTIVE** (branch and bound over the maximal signatures, family sizes printed) and **MACHINE-CHECKED** (the minimality, at all three stages, over every subset of the reduced signature family, both reductions and both guards checked).

Two further figures are reported beside the theorem because each is a bound a reader can check by hand. A **packing** is a set of steps no cell witnesses two of; a cover needs one cell per packed step, so the largest packing bounds the seed below. The largest packings, found by exact search, have **6, 7 and 8** steps — one short of the seed at every stage, so the seed is not decided by that bound and the branch and bound is doing work. And the **greedy** cover of steps and slots — take at each turn the cell covering the most uncovered elements — returns **7, 9 and 9**: at the second stage it is one above the minimum, which is the ordinary behaviour of greedy on set cover — its ratio to the optimum is bounded by a logarithm of the largest set and by nothing better, Johnson (1974), Lovász (1975) and Chvátal (1979), CITED — and not a property of the lattice. **EXHAUSTIVE**, both.

> **What three exact values do and do not say.** The seed rises by one at each of the three stages — 7, 8, 9 — while the cell count rises 976, 1,654, 2,535, and the compression |Λ|/seed is 139, 207 and 282. Three points fix no law; the paper claims none. What the values do settle is that the seed at the second stage is 8 and not 9, and that a greedy figure is an upper bound and not a seed.

> **Seventeen generators and seven cells are two different compressions.** The seventeen of §7 generate Λ₈ under the lattice join, and they are forced: they are exactly the join-irreducibles, so no smaller set generates under ∨. The seven generate it under ℛ, which is the stronger operator — it fills the box its own pairwise extents allow, where the join reaches only the down-set — and seven is what that stronger operator costs. Neither number bounds the other, and the two should not be read as competing measurements of the same thing.

---

## §10 · Verification record

Every number printed above is recomputed by the paper's check program, which imports the construction by path and never copies it; the reference implementations used by the guards are written independently inside the check program itself. The program reports one line per obligation under exactly one of the status words of §0, and it exits non-zero on any failure; the solver is Z3 (de Moura and Bjørner 2008, CITED), version 5.1.0. **The run behind this paper reports 148 obligations — 115 EXHAUSTIVE, 9 MACHINE-CHECKED, 10 REFUTATION, 14 GUARD — with 0 failures**, and the selftest's six negative controls are all refuted. Below, *family* names what an EXHAUSTIVE row visited, *domain* names what a MACHINE-CHECKED row ranged over, and *witness* is what a REFUTATION prints.

**Table 5. The verification record, by object.**

| object | status | family, domain or witness |
|---|---|---|
| Lemma 1, ℛ(X) is a sublattice | PROVED | — |
| Lemma 2, the staircase is exact on monotone one-coordinate bounds | PROVED | — (the sweep of Prop. 2 confirms its instance at every stage) |
| Lemma 3, distributivity | PROVED; EXHAUSTIVE | the coordinatewise extremes of Λ₈ are cells: (1,0,1,0,1,0,0,0) at rank 3 and (3,1,3,3,3,1,3,3) at rank 20 |
| Lemma 4, a seed is a cover of steps and slots | PROVED; GUARD | 40 pseudorandom subsets of Λ₈, seed 11: cover-of-steps ⇔ regeneration in the fixed box, 40/40; cover-of-steps-and-slots ⇔ regeneration in the subset's own box, 40/40; the seed minus one cell fails both |
| **Theorem 1**, one coordinate per bound | CITED; PROVED; MACHINE-CHECKED ×2 | the unbounded integers, 10 free variables (x₁, x₂ for the lower bound's parent, u₁, u₂ for the upper bound's, y₁, y₂, l₁, l₂, h₁, h₂), monotonicity stated at the points that occur, `unsat`; and the finite-box form, every closed subset of a 3 × 3 box (2⁹ subsets) against every monotone h into {−1, 0, 1, 2} |
| **Theorem 2**, the monotone envelope | PROVED; EXHAUSTIVE | the least envelope at the five axes of Table 2, seven readings, with the construction's parent indices: l⋆ and h⋆ monotone, l⋆ ≤ h⋆ at every cell, the exact fibre inside the least envelope and the least envelope inside the construction's interval, cell by cell; the counts 1,638 / 2,535 / 12,425 / 13,585 / 60,320 / 199,130 and the empty fibres 0 / 600 / 1,305 / 0 / 0 / 0; the band equal to Λ₁₃ as a set and to the least envelope of the doublet |
| **Theorem 3**, the triangle | PROVED; MACHINE-CHECKED (join); REFUTATION (meet) | join: the unbounded integers, 6 free variables, `unsat`; meet: the solver's model a₁=0, b₁=4, c₁=4, a₂=1, b₂=2, c₂=3, and the two witnesses (0,1,1)∧(1,0,1) = (0,0,1), (4,0,4)∧(2,2,0) = (2,0,0) re-verified in ordinary arithmetic |
| **Theorem 4**, the bands | CITED (i); PROVED; MACHINE-CHECKED (i), (ii); REFUTATION (iii) | (i) the unbounded integers with k itself a free variable, `unsat`; (ii) the unbounded integers, `unsat`; (iii) the witness (2,0,2)∧(2,2,0) = (2,0,0) |
| **Theorem 5**, the cost of each shape; Corollary 1 | PROVED; MACHINE-CHECKED (iii, join); REFUTATION (iii, meet); EXHAUSTIVE | (iii): the unbounded integers with k a free variable, `unsat`; the solver's model, and (0,k)∧(k,0) = (0,0) verified for k = 1, …, 6; the envelope on {0, …, M} for k ≤ 6, k ≤ M ≤ 10, 56 cases; the thirteen bounds of D10; the exact fibre strictly inside the least envelope at every axis; the two exact thirteenth stages, 128,225 and 185,545 cells, the meet witness (…,0,1) ∧ (…,1,0) = (…,0,0) leaving both, their staircase defects 70,905 and 13,585 with ℛ of each equal to Λ₁₃; the excess 70,905 = 57,320 + 13,585; the sixteen cells with g = 3; 2S′ ≡ g (mod 2) in every spin set |
| the derived-quantity remark of §4 | REFUTATION | h = e − q on Λ₈: h((1,0,1,0,1,0,0,0) ∨ (1,0,1,1,1,0,0,0)) = 0 ≠ max(1, 0) |
| Prop. 1, projection | PROVED; EXHAUSTIVE | the five projections Λₛ₊₁ → Λₛ, s = 8, …, 12, as set equalities |
| **Prop. 2**, every stage closes | PROVED; EXHAUSTIVE ×2 | the staircase swept over 6,912 / 27,648 / 110,592 / 663,552 / 5,308,416 / 47,775,744 ambient cells; every unordered pair at the first four stages, 475,800 / 1,367,031 / 3,211,845 / 92,269,320 pairs, 0 failing meets and 0 failing joins; the pair counts 2,513,724,060 and 19,826,278,885 at the last two, decided by the sweep |
| Table 1 and Figure 1 | EXHAUSTIVE | the six counts, the six boxes, the six fills, no duplicate cell at any stage; the growth factors 204 and 6,912 and the ratio 415 |
| Prop. 3, fill decay | EXHAUSTIVE | six stages |
| Props. 4–6, the terms and their maxima | EXHAUSTIVE; CITED | terms(ℓᵏ) for the eight subshells the caps admit and pᵏ to k = 6: terms(p¹, p², p³), φ̂ = {1:3, 2:4, 3:5} as the running maximum of D12, μ(0, 1) = 1 and μ(0, 2) = 0, max 2J(pᵏ) = 3,4,5,4,3,0, max 2S(pᵏ) = 1,2,3,2,1,0, max 2S(sᵏ) = 1, 0, terms(pᵏ) = terms(p⁶⁻ᵏ), min(g, 4f+2−g) at every (f, g), the envelope 3,4,5,5,5,5; the construction of the term multiset is CITED |
| the core–orbit range | EXHAUSTIVE | max{2K : 2Jₚ = j} = j + 2 for j = 0, …, 5 over Λ₁₂ |
| **Table 2**, the envelope gap | EXHAUSTIVE | every cell of the stage below at each axis: 1,054 / 1,654; 1,132 / 2,535; 2,310 / 13,585 and 10,585 / 13,585; 22,275 / 70,905; 128,225 / 199,130 with 13,585 cells at 2K = 0; the exact fibre never larger than the admissible one; the least column as under Theorem 2 |
| Props. 7–8, the constraint graph | PROVED (8); EXHAUSTIVE | six stages: the edge list against an independent transcription of the bounds; vertices 8–13; edges 7, 8, 10, 11, 12, 13; connected; cycle rank (0,0,1,1,1,1); one triangle 2S′–g–v from the tenth stage, over all C(13,3) = 286 triples at the top; treewidth (1,1,2,2,2,2) by exact elimination search; girth 3 from the tenth stage; degrees at the top; q a cut vertex, no parent–target edge, exactly two components after deleting q |
| Prop. 9, the two-parent reading | EXHAUSTIVE | the same six graphs with the edge f–2K substituted: 14 edges, cycle rank (0,0,1,1,2,2), triangles, treewidth, girth and the hub degrees unchanged, only f and 2K moving |
| Prop. 10, exact factorisation; Table 4; Figures 3–4 | PROVED; EXHAUSTIVE | six stages for Σₜ ∣A(t)∣·∣B(t)∣ = ∣Λ∣; the set identity Λ ∩ {q = t} = A(t) × B(t) at every t of the first and thirteenth stages; the sections 33×5 / 33×10 / 23×15 / 8×17, 815 / 3,260 / 6,150 / 3,360 and 11,470 / 45,880 / 89,700 / 52,080 |
| Prop. 11, the profile and ⟨q⟩ | EXHAUSTIVE | six stages, four transfers each: monotone sides, log-concave sections peaking at t = 2, the six values of ⟨q⟩ from 1.4631 to 1.9159 |
| Prop. 12, the price of the second parent | EXHAUSTIVE; REFUTATION | the cell's-own-f construction at the twelfth and thirteenth stages: 55,755 and 153,680 cells against products 70,905 and 199,130, defects 15,150 (21.4%) and 45,450 (22.8%); its staircase defect E = 12,675 |
| Prop. 13, the exact triangle does not close | EXHAUSTIVE; REFUTATION | 22,275 cells, ∣ℛ∣ = 57,845, E = 35,570, 64,290 cells at the thirteenth stage; all 248,076,675 unordered pairs, 52,767,450 failing meets and 28,742,850 failing joins, each count pinned; the exhibited failing meet |
| Props. 15–17, rank, generators, Birkhoff | PROVED (16); CITED; EXHAUSTIVE | rank values 18, 21, 24, 29, 36, 44 with bottom rank 3 at every stage; the rank sequence of Λ₈ and its widest level 122 at rank 11, Λ₉'s 185 at rank 12, log-concavity, 976 = 8 × 122; alphabet sizes 3,2,3,4,3,2,4,4 summing to 25; every generator a cell, the 17 join-irreducibles equal to the 17 generators, ∣{G ≤ x}∣ = r(x) − 3 at all 976 cells, 20 covering relations, 976 down-sets by enumeration |
| **Theorem 6**, 1,113,045,672 maximal chains | PROVED; EXHAUSTIVE | the recursion evaluated at all 976 cells, lower covers found by testing the eight unit decrements for membership; every chain of length 17; the negative control of the selftest (the ambient box's multinomial, 205,837,632,000, is not this number) |
| Props. 18–19, the bracket system; Figure 5 | EXHAUSTIVE | all cells of the five upper stages, 1,654 + 2,535 + 13,585 + 70,905 + 199,130 = 287,809: gap-free monotone intervals, branching 4, 4, 6, 8, 9; all 199,130 top-stage cells for the composition: containment, slack 2 below and 0 above, the direct bracket gap-free, both routes covering {3, …, 20} |
| **Theorem 7**, the seed 7, 8, 9 | EXHAUSTIVE; MACHINE-CHECKED | branch and bound over the 264 / 442 / 688 maximal covering signatures (808 / 1,376 / 2,111 distinct) of the 77 / 105 / 138 steps; the minimum realising all 25 / 29 / 33 slots; regeneration under two independent staircases, in the fixed box and in the seed's own box; the solver refuting a 6- / 7- / 8-cover over every subset of the reduced family, 59 / 61 / 63 signatures against 27 / 28 / 29 kept steps, `unsat` three times; the two reductions, the non-vacuity guard and the encoding-fidelity guard checked as GUARDs at every stage |
| the packing and greedy figures of §9 | EXHAUSTIVE | the largest packing by exact search, 6 / 7 / 8 steps, each checked against every cell; the greedy rule on steps and slots, 7 / 9 / 9; the requirement counts 77 + 25, 105 + 29, 138 + 33; the compressions 139, 207, 282 |

**The two guards, stated.** No MACHINE-CHECKED row — of §4 or of §9 — is reported unless both pass, and the check program refuses to print any of them otherwise.

*Non-vacuity.* Satisfiability checks, each asking the solver for a model of the hypothesis alone with the degenerate cases excluded: Theorem 1's hypothesis with the new coordinate strictly inside both of its bounds at both points, the two parents' values moving in opposite directions and both bounds strictly monotone there; Theorem 3's with two distinct non-degenerate triples; Theorem 4's two hypotheses and Theorem 5(iii)'s, each with two distinct non-degenerate members; the finite-box hypothesis with the subset S neither empty nor the whole box and the bound h non-constant; and, for each of the three seed instances, the cover clauses together with a cover of the stated size, whose model the check reads back and verifies to be a cover. All are satisfiable, so no implication is vacuously true.

*Encoding fidelity.* The predicates the solver is given are themselves evaluated at concrete integers — substituted and simplified to a constant — and compared with independently written implementations in ordinary arithmetic: the triangle region on every cell of the cap-6 box and on 400 random pairs, the region {|a − b| ≤ c} on the cap-8 box and 300 pairs, the bands Bₖ for k ≤ 3 and the constant-side triangle for k ≤ 3 on their cap boxes and random pairs, and Theorem 1's hypothesis and conclusion at 600 random points and on 450 pairs of cells drawn from the random instances below — **10,176 evaluations, 0 disagreements**. Beside that, the concrete references are checked against the imported triangle instrument and against brute force: the triangle region at cap 6 built twice and compared cell by cell, with **2,862** failing meets and **0** failing joins by both routes; {|a − b| ≤ c} at cap 8 with **12,654** failing meets; the bands closed at cap 7; the constant-side triangle join-closed and not meet-closed at cap 7. Theorem 1's construction is exercised directly: on **150** pseudorandomly generated sublattices (seed 5) of boxes of shapes 3×3, 4×3, 3×3×3 and 2×4×3, each extended by a random pair of monotone bounds, a brute-force pair scan finds **0** failures, and the same scan with the bounds deliberately made non-monotone catches a failure **136** times, so the guard is capable of returning a failure. For the seed instances the clause set is evaluated at concrete assignments over the reduced family and compared with the direct cover test: on the exhibited minimum carried into the reduced instance, on that cover with each member removed, and on 40 random subsets, with no disagreement, and with at least one deletion answered "does not cover".

*The reductions.* The three solver obligations of Theorem 7 run on a reduced instance, and the reductions are checked before the solver is asked: every covering signature sits inside a maximal one (set dominance), every step is witnessed by every cell that witnesses one of the kept steps (element dominance), and set dominance again on the restricted signatures. A failure of any of these, or of either guard, would leave the obligation unreported.

**The negative controls.** The selftest runs the guards and then six deliberately false claims, each of which must be reported as refuted, so that a clean run is evidence rather than a restatement: that the region with the upper bound only, {c ≤ a + b}, has the triangle's failure counts (it has 2,254 failing meets against the triangle's 2,862, so the fidelity guard separates them); that the triangle region is meet-closed; that Theorem 1 holds without the monotonicity hypothesis; that the triangle with one side constant is meet-closed; that the twelfth stage under the exact triangle is closed; and that the maximal chains can be counted without testing membership. All six are refuted.

**What is not machine-checked, and why.** Theorem 2 is an order-theoretic statement about a family of sets indexed by two arbitrary monotone functions on arbitrary chains; it is proved, and its content is exercised at the five axes of Table 2, where the least envelope is constructed, compared with the construction's bound, and its excess counted. Theorem 6's count and Propositions 15 to 19 are enumerations over a named finite object, not decision problems, and they carry EXHAUSTIVE with the family printed. Proposition 8 is proved from the edge list and checked at all six stages, but the claim that no *other* vertex separates the two blocks is not made: k, g, ℓ and f are cut vertices of the graph too, and the proposition is about the parent–target cut alone. The branch and bound of Theorem 7 is exhaustive in the sense that every branch not pruned by a valid bound is visited; what the solver adds is a second, independent decision of the same minimality on the reduced instance.

**What is at the caps, and what is not.** Every cell count, every section, every rank profile, every graph figure and every seed in this paper is at the single cap setting of D11. Theorems 1 to 5 and Lemmas 1 to 4 are at no caps: they are proved for arbitrary chains and arbitrary monotone bounds, and the four that a solver can decide are decided over the unbounded integers. Propositions 4 to 6 are at the caps as stated and are the reason the distinction matters: φ̂ coincides with the realised maximum at these caps and separates from it one electron further up.

---

## References

- Birkhoff, G. (1937). Rings of sets. *Duke Mathematical Journal* **3**(3), 443–454.
- Birkhoff, G. (1967). *Lattice Theory*, 3rd edition. American Mathematical Society Colloquium Publications 25, Providence.
- Chvátal, V. (1979). A greedy heuristic for the set-covering problem. *Mathematics of Operations Research* **4**(3), 233–235.
- Condon, E. U. and Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge University Press, Cambridge.
- Cowan, R. D. (1981). *The Theory of Atomic Structure and Spectra*. University of California Press, Berkeley.
- Davey, B. A. and Priestley, H. A. (2002). *Introduction to Lattices and Order*, 2nd edition. Cambridge University Press, Cambridge.
- Dechter, R. and Pearl, J. (1989). Tree clustering for constraint networks. *Artificial Intelligence* **38**(3), 353–366.
- Dilworth, R. P. (1950). A decomposition theorem for partially ordered sets. *Annals of Mathematics* **51**(1), 161–166.
- de Moura, L. and Bjørner, N. (2008). Z3: an efficient SMT solver. In C. R. Ramakrishnan and J. Rehof (eds), *Tools and Algorithms for the Construction and Analysis of Systems*, Lecture Notes in Computer Science 4963, Springer, Berlin, 337–340.
- Freuder, E. C. (1978). Synthesizing constraint expressions. *Communications of the ACM* **21**(11), 958–966.
- Freuder, E. C. (1982). A sufficient condition for backtrack-free search. *Journal of the ACM* **29**(1), 24–32.
- Grätzer, G. (2011). *Lattice Theory: Foundation*. Birkhäuser, Basel.
- Jeavons, P. G. and Cooper, M. C. (1995). Tractable constraints on ordered domains. *Artificial Intelligence* **79**(2), 327–339.
- Jeavons, P., Cohen, D. and Gyssens, M. (1997). Closure properties of constraints. *Journal of the ACM* **44**(4), 527–548.
- Johnson, D. S. (1974). Approximation algorithms for combinatorial problems. *Journal of Computer and System Sciences* **9**(3), 256–278.
- Karp, R. M. (1972). Reducibility among combinatorial problems. In R. E. Miller and J. W. Thatcher (eds), *Complexity of Computer Computations*, Plenum Press, New York, 85–103.
- Lovász, L. (1975). On the ratio of optimal integral and fractional covers. *Discrete Mathematics* **13**(4), 383–390.
- Milgrom, P. and Shannon, C. (1994). Monotone comparative statics. *Econometrica* **62**(1), 157–180.
- Pauli, W. (1925). Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren. *Zeitschrift für Physik* **31**(1), 765–783.
- Racah, G. (1942a). On a new type of vector coupling in complex spectra. *Physical Review* **61**, 537.
- Racah, G. (1942b). Theory of complex spectra. II. *Physical Review* **62**(9–10), 438–462.
- Racah, G. (1943). Theory of complex spectra. III. *Physical Review* **63**(9–10), 367–382.
- Robertson, N. and Seymour, P. D. (1986). Graph minors. II. Algorithmic aspects of tree-width. *Journal of Algorithms* **7**(3), 309–322.
- Stanley, R. P. (2012). *Enumerative Combinatorics, Volume 1*, 2nd edition. Cambridge University Press, Cambridge.
- Topkis, D. M. (1978). Minimizing a submodular function on a lattice. *Operations Research* **26**(2), 305–321.
- Topkis, D. M. (1998). *Supermodularity and Complementarity*. Princeton University Press, Princeton.
- Wigner, E. P. (1931). *Gruppentheorie und ihre Anwendung auf die Quantenmechanik der Atomspektren*. Vieweg, Braunschweig.
