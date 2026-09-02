# Rewrite — Chapter 6 (was Chapter 8), "What Λ is — distributive, modular, Sperner"

**Placement:** Part I — The Lattice, third chapter. Establishes Λ's order-theoretic identity. Old Ch 8 → 6; §8.x → §6.x; Figures 8.1/8.2 → 6.1/6.2. The cap-convention paragraph (old §8.0) is moved to front matter. Per standing treatment: every result kept; self-audit/self-correction commentary cut; each theorem sketched here and pointed to its full expansion in the Mathematical Compendium via an [MC-NN] token keyed to OWED-EXPANSIONS.md (the token reads as a citation; the register tracks which expansions still need authoring). Forward-references from Chapter 5 to "Chapter 8" become "Chapter 6". Cross-refs to chapters not yet reached keep current numbers.

---

## 6. What Λ is — distributive, modular, Sperner

Chapter 5 built Λ and showed it is closed. This chapter says what kind of object closure made it. The answer is a chain of order-theoretic properties, each measured, each with a consequence the later book uses.

### 6.1 Distributive
Λ is a sublattice of a product of chains, and every such sublattice is distributive:

      a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)

Verified on 4,000 randomly drawn triples, no failures. The proof — that the product-of-chains embedding forces the distributive law — is carried in the Mathematical Compendium [MC-02].

This is the least surprising fact in the chapter and the most load-bearing: distributivity is what admits Birkhoff's representation, which §6.3 uses to compress the whole object to seventeen generators.

### 6.2 Rank is conserved
Λ has a conservation law, and it is exact:

      rank(a ∨ b) + rank(a ∧ b) = rank(a) + rank(b)

**Verified on all 475,800 pairs: zero violations.**

This is **modularity**, and it is strictly stronger than what most rank functions satisfy. Matroid rank is *sub*modular — the left side is only ≤ the right; entropy is submodular too. Λ's rank is modular, with equality, and that equality is the signature of distributivity. Join and meet redistribute rank without creating or destroying it: taking the join of two cells raises the rank by exactly what taking the meet lowers it, the way energy is conserved under a canonical transformation. The derivation — that modular equality holds for this rank function, and is equivalent to distributivity on a graded lattice — is carried in the Mathematical Compendium [MC-03].

And it is a cheaper test than §6.1's. Distributivity checked over triples is an operation on three cells at a time; modularity of rank is a pairwise condition, and on a graded lattice with this rank function the two are equivalent:

| test | sample | time |
|---|---|---|
| distributive law, triples | 4,000 | 0.0375 s |
| **modular rank, pairs** | 4,000 | **0.0188 s** |

Both hold. The pairwise test is the one to run first, because a failure of modularity is a failure of distributivity and it is found in half the work.

### 6.3 Seventeen generators
By Birkhoff's theorem, a finite distributive lattice is the lattice of down-sets of its poset of join-irreducibles. For Λ at caps (3, 3, 1, 3), k ≥ 1:

      976 cells ← 17 join-irreducibles, 20 covering relations

and the correspondence is exact: **all 976 down-sets of the seventeen-element poset are precisely the 976 cells** — a fifty-seven-fold compression. The construction of the poset and the proof of the exact down-set correspondence are carried in the Mathematical Compendium [MC-04].

The covering relations are the physics made visible:

| cover | reads |
|---|---|
| *e* = 2 ⋖ *e* = 2, *f* = 1 | a target subshell requires its shell |
| *k* = 2 ⋖ *k* = 2, *q* = 2 | you may remove what you have |
| *n* = 2 ⋖ *n* = 2, ℓ = 1 ⋖ *n* = 2, ℓ = 1, *k* = 3 | shell before subshell before occupancy |

And the shape is cap-independent. Across six settings from 976 to 27,873 cells the generator count grows — 17, 23, 31, 32 — while the *patterns* hold at fifteen, none new and none lost; only their multiplicities change. That is what licenses stating the poset once.

![Figure 6.1](figures/figure-6.1.png)

*Figure 6.1. The seventeen join-irreducibles and their twenty covering relations. Every one of the 976 cells is a down-set of this poset, and every down-set is a cell — a fifty-seven-fold compression, exact. The covers are the constraints of §5.1 made visible: shell before subshell before occupancy, and a target subshell requiring its shell.*

### 6.4 Sperner, and not symmetric
The largest antichain in Λ equals its largest rank level — the **Sperner property** — verified exactly at five cap settings by Dilworth's theorem and bipartite matching, no exceptions. At caps (3, 3, 1, 3), k ≥ 1 the maximum is 122, at rank 11. The rank sequence is **log-concave**, hence unimodal, which is why Sperner holds as a consequence rather than by coincidence. The log-concavity computation and the Dilworth/matching argument are carried in the Mathematical Compendium [MC-05].

But Λ is **not rank-symmetric**, so it has no symmetric chain decomposition, and the classical result for divisor lattices does not transfer. The asymmetry is itself a measurement:

      centre of mass 11.07 against midpoint 11.5 — skew −0.43, over all 976 cells at caps (3, 3, 1, 3), k ≥ 1

Low ranks are cut by floors (*n* ≥ 1, *k* ≥ 1, *e* ≥ 1); high ranks by caps (ℓ ≤ *n*−1, *k* ≤ 2(2ℓ+1), *q* ≤ *k*, *g* ≤ *q*). There are more caps than floors, so the top is pruned harder, and the skew is a measure of how much more Pauli constrains than counting does.

Nor is Λ self-dual. Under the reflection x ↦ max − x, coordinate by coordinate, only 8 of the 976 cells have their image back in Λ. This reflection is not decoration: restricted to one occupancy coordinate it is particle–hole conjugation, terms(ℓᵏ) = terms(ℓ^(4ℓ+2−k)) exactly, and §10.11.2 shows it is one of the three machines that price every coupling axis. The two sides of the object are genuinely distinguishable, which Chapter 10 develops.

![Figure 6.2](figures/figure-6.2.png)

*Figure 6.2. The rank sequence over all 976 cells is log-concave, hence unimodal, hence Sperner. It is not symmetric: the centre of mass sits below the midpoint by 0.43, because Λ has more caps than floors.*

### 6.5 The constraint graph is a tree
Eight coordinates, seven constraints, connected in a single line:

      e — f — g — q — k — ℓ — n,  with 2S attached to k

**Treewidth 1.** Three consequences run through the rest of the book.

**The void needs no sieve.** A tree has no cycles, so there is nothing for inclusion–exclusion to correct, and Chapter 8 gives the cell count in closed form.

**The order is recoverable.** Chapter 13 recovers Λ's coordinate orders from an unlabelled bag of cells by propagation along this tree — 20 of 20.

**The graph offers no redundancy.** There is exactly one path between any two coordinates. So the two-route protection the object uses to defend itself (Chapter 14) cannot come from the constraints — it must come from derived quantities instead. That is a real limit on how the object can defend itself, and it is visible here, several chapters before it is needed.

### 6.6 Order dimension
Λ₈ has order dimension exactly 8, rising by one per adjoined axis, with no redundant coordinate: every axis carries information no combination of the others supplies. The order dimension of a finite distributive lattice is the width of its poset of join-irreducibles (Dilworth), so dim(Λ₈) = 8 follows from §6.3's seventeen generators rather than standing on its own; the width computation is carried in the Mathematical Compendium [MC-06].

Λ occupies **14.1%** of its own bounding box — 976 cells of 6,912.
