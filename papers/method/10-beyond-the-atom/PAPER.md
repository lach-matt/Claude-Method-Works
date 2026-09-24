# Closure beyond the atom: the defect of an index, its zeros by theorem, and the electromagnetic quotient

**The closure defect of an index on ordered coordinates is decided by the shape of its membership rule and not by its subject: the operator's fixed points are exactly the sublattices of the box, so every index whose rule is a conjunction of bimonotone inequalities — the atomic lattice among them — closes by theorem; the defects that remain are either forced by a hole in the value set of a difference or count nameable cells that the coordinates cannot exclude; the defect moves under a relabelling of one coordinate and cannot rise under fibring by a coordinate; and a selection rule acts on the atomic index as a quotient rather than as an added coordinate, closing or opening it according to the convexity of the value set it names.**

**Matthew Lach** · Independent Researcher · 24 September 2026

---

## Abstract

A finite set X of cells over d ordered coordinates has a canonical superset ℛ(X): the cells of its own box that its monotone pairwise bounds admit. The closure defect E(X) = ∣ℛ(X)∣ − ∣X∣ counts what the coordinates imply and the set denies. This paper identifies ℛ: it is a closure operator on the observed box (proved and machine-checked over every subset of three named boxes), and its fixed points are exactly the sublattices of the box — a theorem of Queyranne and Tardella (2008) whose short proof is written out. Two consequences follow. A set cut from a box by inequalities of the form a·xᵢ − b·xⱼ ≥ c with a, b ≥ 0 is a sublattice, so the atomic lattice Λ (976 cells in a box of 6,912), its nine- and ten-coordinate extensions, a box ordering, a product grid over a spectroscopic survey and Janet's left-step table all have E = 0 as a theorem about their rules rather than as a measurement. And a set cut by a condition whose value set has a hole need not close: the χ = ±6 slice of the Kreuzer–Skarke list has E = 540 for that reason alone, and on the atomic index the spin rule ΔS = 0 keeps 526 cells at E = 0 while the orbital rule ∣Δℓ∣ = 1 keeps 840 at E = 750, with the witness printed. The defects that are measurements name their cells: 36 for the periodic table, 7 for the Gregorian calendar, 9 for the particle-bound nuclides through Z = 7 and 12 through Z = 10 (every one a nuclide NUBASE2020 lists as unbound), 2 for the AME2020 evaluation, 975 for the witnessed channels of the survey. The defect is a property of the coordinatisation: a relabelling of the months takes the calendar from 7 to 0, fibring by a coordinate never raises the total defect while a general partition can, and adjoining a coordinate never repairs an index. A redundancy convention — the largest ladder rung of an index removable at random with exact recovery — is reported with its rungs and trial counts and is not a law. Finally the electric-dipole rules act on the atomic index as a quotient onto a full 2 × 4 rectangle whose E = 0 says nothing, while adjoined as coordinates they give E = 9,278; and the followability of ground-configuration moves, previously reported as crossing between one element and the whole table, does not cross once the moves are restricted to physical one-electron transfers into a subshell with room.

---

## §0 · The result

**Closure is a property of an index's rule, not of its subject.**

The operator studied here takes a finite set X of d-tuples over ordered coordinates and returns the cells of its own box that its own monotone bounds admit. Nothing is supplied from outside: the alphabets are the values X realises, and the bounds are read off X. The defect E(X) = ∣ℛ(X)∣ − ∣X∣ is therefore a measurement of what the coordinates carry against what the set states, and it is defined for any such set whatever its subject.

**What is claimed.** Five things.

1. **ℛ is a closure operator on the observed box, and its fixed points are exactly the sublattices.** Theorem 1 (extensive, monotone, idempotent) is proved and machine-checked over every subset of three named boxes; Lemma 2 (ℛ(X) is a sublattice) is proved; Theorem 0 (ℛ(X) is the sublattice hull ⟨X⟩, so E(X) = 0 exactly when X is a sublattice of its box) is prior art — Queyranne and Tardella (2008), on Topkis (1976) and Veinott (1989) — and is proved here in six lines, then corroborated exhaustively on 766 subsets and three larger indexes; Theorem 2 (a full box closes) is proved and exhausted on 84 boxes. ℛ is a pairwise-consistency closure in the sense of constraint networks (Montanari 1974; Mackworth 1977; Freuder 1978) whose binary relations are the staircase, or connected row-convex, constraints of Deville, Barette and Van Hentenryck (1999).
2. **E is a property of the coordinatisation.** It changes under a permutation of one coordinate's value labels — the calendar, E = 7 before and 0 after (Theorem 3). A coordinate with no intrinsic order therefore has no defect of its own (Remark 1). Fibring by a coordinate never raises the total defect (Theorem 4) and iterating over the coordinates sends it to 0 (Corollary 2), so a stated E = 0 is a claim relative to a stated fibration; fibring by an arbitrary partition **can** raise it, and a three-cell witness is printed (Remark 3).
3. **Every zero in the catalogue is a theorem, and every non-zero is either forced or named.** Lemma 3 shows that cutting a sublattice by an inequality a·xᵢ − b·xⱼ ≥ c with a, b ≥ 0 leaves a sublattice. The atomic lattice Λ is the cut of a box by eight such inequalities, so E(Λ) = 0 follows from Theorem 0 (Proposition 2); so do the zeros of Λ₉, Λ₁₀, the box ordering, the product grid and Janet's table, and the full boxes close by Theorem 2. The Kreuzer–Skarke slice is open because a difference of its coordinates takes the values −3 and +3 and nothing between, and the join of two of its cells lands on the hole (Corollary 1 with a printed pair). The remaining defects are counts of cells that can be named: the periodic table's 36 gaps, the calendar's 7 missing days, the particle-bound nuclides' 9 (Z ≤ 7) and 12 (Z ≤ 10) unbound nuclides, the AME2020 evaluation's 2, and the 975 channels the survey's own alphabets admit and it has not measured. The catalogue does not separate closed from open by measurement; it shows what decides each.
4. **Redundancy is a sampled convention, reported as one.** The largest rung of a fixed ladder at which a random deletion is recovered exactly by ℛ in at least 8 of 10 seeded trials is 61% for Λ at eight coordinates, 20% for the product grid at three, and below the ladder's first rung for every two-coordinate index tried; every figure is printed with the rung passed, the rung failed and the trial counts. A projection of Λ to fewer coordinates lowers it, and a coordinate that is a function of two the index already carries takes it to 0 while opening the index (E = 20,808), which Corollary 3 explains. No correlation, fit or significance is claimed.
5. **A selection rule is a quotient.** The electric-dipole rules map Λ₉ onto a complete 2 × 4 rectangle, whose E = 0 says nothing about the rules (Theorem 2). Imposed as subsets they behave according to the convexity of the value set they name: ΔS = 0 gives a sublattice and E = 0, ∣Δℓ∣ = 1 gives a non-sublattice and E = 750, with the witness printed. Adjoined as coordinates they give E = 9,278 (Corollary 3). On the moves between occupied subshells of the 118 observed ground configurations, the source's reported crossing — allowed moves followable less often than forbidden ones within an element and more often across the table — is reproduced on the population it was computed on and does **not** occur on the 134 moves of that population that are physical one-electron transfers into a subshell with room; there the forbidden class leads in both scopes.

**What is not claimed.** The paper measures; it does not explain. Why Janet's 1928 ordering is a staircase and the classroom arrangement is not is a fact about two drawings of the same 118 elements, and the (n + ℓ) rule itself is not derived here (Madelung 1936; Löwdin 1969; Allen and Knight 2002). The 540 cells the Kreuzer–Skarke slice admits are not predictions: the slice is open by construction, and its defect says nothing about the list. The nine and twelve nuclide cells are named unbound nuclides, and reading them as the pairing and clustering terms of the semi-empirical mass formula (von Weizsäcker 1935) is an interpretation, not a derivation. The redundancy protocol is a convention whose rungs and trial counts are printed; the figures are **SAMPLED** and no law of dimension is claimed. The followability match used for the atomic moves is formal — it equates the number of electrons a move delivers with the number a subshell holds — and carries no physical reading; the paper prints what it gives on two populations and claims no crossing. Nothing here is a claim about the physics of the electric-dipole approximation. And which formal languages exist is not settled here (§6): the paper measures which of five operators return a cell decision on a given index and reports agreement among exactly those, discounting the one pair that agrees by theorem.

**Status words.** Seven are used and never merged.

| status | meaning |
|---|---|
| **PROVED** | a proof is written out below and every step is justified |
| **MACHINE-CHECKED** | Z3 returned unsat on the negation of an obligation whose variables range over every subset of a named finite box, with both guards passed |
| **EXHAUSTIVE** | a decision procedure visited every case in a stated finite family, and the family's size is printed |
| **MEASURED** | a number computed from cited data by a stated procedure — the paper's own result, its sample stated; never a proof |
| **SAMPLED** | a seeded pseudorandom sweep of a stated size; never exhaustive |
| **REFUTATION** | a claim disproved by an explicit witness, the witness printed |
| **CITED** | taken from the literature or a public database, with the source |

The ceiling that is real: the machine checks decide claims over named boxes of at most 27 cells, so nothing here carries that status at a larger box or at d > 3. Which obligations carry which status, over which boxes and families, is §7 and nowhere else.

---

## §1 · Definitions

Throughout d ≥ 1 is finite and X is a finite non-empty set of d-tuples of integers.

**D1 (index, cell, observed alphabet).** An **index** is a finite non-empty set X of d-tuples over d named coordinates. Its elements are **cells**. The **observed alphabet** at coordinate i is Aᵢ(X) := { xᵢ : x ∈ X }, a finite set of integers carrying the order of ℤ.

**D2 (box).** Box(X) := A₁(X) × ⋯ × A_d(X), the **ambient box**, is the product of the observed alphabets. As a product of finite chains it is a distributive lattice under the coordinatewise operations

> (x ∧ y)ᵢ = min(xᵢ, yᵢ),  (x ∨ y)ᵢ = max(xᵢ, yᵢ).

∣Box(X)∣ = ∏ᵢ ∣Aᵢ(X)∣ is reported beside every defect, because E = 0 carries information only when the box exceeds the cells. A subset of Box(X) closed under ∧ and ∨ is a **sublattice** of the box; ⟨X⟩ denotes the smallest sublattice of Box(X) containing X, the **sublattice hull** (Birkhoff 1940).

**D3 (envelope).** For i ≠ j and a ∈ Aⱼ(X),

> φᵢⱼ(a) := max { yᵢ : y ∈ X, yⱼ ≤ a }.

φᵢⱼ is the furthest coordinate i reaches when coordinate j is held at or below a. There are d(d − 1) envelopes. When the index must be named the envelope of X is written φᵢⱼ\[X\].

**D4 (closure, defect).**

> ℛ(X) := { x ∈ Box(X) : xᵢ ≤ φᵢⱼ(xⱼ) for all i ≠ j },  E(X) := ∣ℛ(X)∣ − ∣X∣.

ℛ is a closure operator in the sense of Moore (1910); Theorem 1 establishes that below. X is **closed** when E(X) = 0. A cell of ℛ(X) \ X is **admitted and absent**. For d = 1 the condition is empty and ℛ(X) = Box(X) = X.

**D5 (fibration by a coordinate).** For a coordinate i, the **fibration of X by coordinate i** is the partition of X into the fibres Xᵥ := { x ∈ X : xᵢ = v } for v ∈ Aᵢ(X). Its **fibred defect** is Σᵥ E(Xᵥ), each fibre closed in its own box. A fibration by several coordinates is obtained by fibring each fibre in turn; the fibration by all d coordinates is the partition into singletons. A partition of X that is not obtained this way is called a **general partition**, and Theorem 4 does not apply to it (Remark 3).

**D6 (binding envelope, coupling).** Write Mᵢ := max Aᵢ(X). The envelope φᵢⱼ **binds** when it is not the constant Mᵢ, that is, when φᵢⱼ(a) < Mᵢ for at least one a ∈ Aⱼ(X). A non-constant envelope need not exclude any cell of the box; binding is a property of the bound, not of the defect. The **coupling** of X is the fraction of the d(d − 1) envelopes that bind.

**D7 (redundancy — a convention).** Fix a seed. For a fraction t, draw a uniformly random subset of X of size ∣X∣ − ⌊t∣X∣⌋ and ask whether ℛ of it equals X exactly. Run ten independent trials. The rung t **passes** when at least 8 of the 10 trials recover X. The **redundancy** of X is the largest rung of the ladder 5, 10, 20, 30, 41, 50, 61, 70, 82, 90 per cent that passes, the ladder being climbed in increasing order and stopped at the first rung that fails; when the first rung removes no cell (⌊0.05·∣X∣⌋ = 0, which happens below 20 cells) no trial is run and the figure is reported as **below the ladder's resolution**. The ladder, the trial count and the acceptance of 8 in 10 are conventions of this paper, chosen once and not tuned; they are what reproduces the figures the redundancy protocol was previously reported with, and that reproduction is their only justification. Every figure is printed with the rung passed, the rung failed and the trial counts at each. Redundancy is **SAMPLED** and is a figure of the convention, not of the index.

**D8 (extension, quotient).** Let C = C₁ × ⋯ × Cₘ be a finite product of chains, with the coordinatewise meet and join, and let h : X → C. The **extension of X by h** is Xʰ := { (x, h(x)) : x ∈ X }, an index on d + m coordinates. The **quotient of X by h** is the image index h(X) ⊆ C on m coordinates. An extension keeps every cell of X distinct; a quotient identifies cells h cannot separate. For m = 1 the extension adjoins a single coordinate.

**D9 (followability — a formal match).** In an index whose cells are **moves** — a cell carrying a source subshell with an occupancy and a target subshell with a count of electrons delivered — a move is **followable** when its target subshell, at the count it delivers, equals the source subshell, at its occupancy, of some move of the index. The match equates a number of electrons delivered with a number of electrons held; it is a coincidence of two integers and not a succession of states, and the paper says so wherever it uses it. A **configurational** match, which asks instead for the target at the occupancy it holds after the move, is also computed (§5.5).

**D10 (bit cost).** For E > 0 the **bit cost** of an index is log₂ C(∣ℛ(X)∣, E), the length of a uniform code over the E-subsets of ℛ(X): the number of bits that name which E of the admitted cells are the absent ones. It is a description length under that code, not an entropy, and it is not additive over fibres.

**D11 (the five operators).** For a finite index X over d ≥ 2 ordered coordinates, with πᵢⱼ the projection onto coordinates i and j:

- **order**: ℛ(X), the staircase of D4;
- **algebra**: ⟨X⟩, the sublattice hull;
- **geometry**: { x ∈ Box(X) : (xᵢ, xⱼ) ∈ conv(πᵢⱼ X) for all i < j }, conv the convex hull in the plane (Carathéodory 1911; Schrijver 1986);
- **information**: the join-closure of the **generators** of X — a cell x ∈ X is a generator when x is not the coordinatewise join of the cells of X strictly below it (a cell with nothing below it is a generator); the operator returns the smallest join-closed subset of Box(X) containing the generators (Birkhoff 1937);
- **statistics**: { x ∈ Box(X) : πᵢⱼ(x) ∈ πᵢⱼ(X) for all i < j }, the cells all of whose pairwise projections are observed — the support of the maximum-entropy fit to the order-2 marginals where that fit exists (Ireland and Kullback 1968; Deming and Stephan 1940), and the set formula in any case; the fit may fail to exist (Haberman 1974), and only the set formula is used here.

Each returns a subset of Box(X) containing X (Lemma 4), and each has its own defect ∣L(X)∣ − ∣X∣. The languages **agree** on X when all five return the same set.

**Notation.** C(n, k) is the binomial coefficient. Λ denotes the atomic lattice of §3.1 and Λ₉, Λ₁₀ its nine- and ten-coordinate extensions. Y denotes a superset of X in Theorem 1; S a subset of a box in Theorems 5 and 6; 2S and 2S′ are twice a spin and are never sets. Coordinate tuples are written in the order their definition states.

---

## §2 · The operator

### 2.1 What ℛ is

**Lemma 1 (the envelope is total and isotone).** For every i ≠ j and a ∈ Aⱼ(X), φᵢⱼ(a) is defined; and a ≤ a′ implies φᵢⱼ(a) ≤ φᵢⱼ(a′).

*Proof.* By D1 there is y ∈ X with yⱼ = a, so { y ∈ X : yⱼ ≤ a } is non-empty and the maximum exists. If a ≤ a′ then { y ∈ X : yⱼ ≤ a } ⊆ { y ∈ X : yⱼ ≤ a′ }, and the maximum of a subset is at most the maximum of the set. ∎ **PROVED.**

**Theorem 1 (ℛ is a closure operator).** For every finite non-empty X: (a) X ⊆ ℛ(X); (b) X ⊆ Y implies ℛ(X) ⊆ ℛ(Y); (c) ℛ(ℛ(X)) = ℛ(X).

*Proof of (a).* Let x ∈ X. Then xᵢ ∈ Aᵢ(X) for each i, so x ∈ Box(X). For i ≠ j, x itself lies in { y ∈ X : yⱼ ≤ xⱼ }, so φᵢⱼ(xⱼ) ≥ xᵢ. Hence x ∈ ℛ(X).

*Proof of (b).* Let X ⊆ Y and x ∈ ℛ(X). Each Aᵢ(X) ⊆ Aᵢ(Y), so Box(X) ⊆ Box(Y) and x ∈ Box(Y). Fix i ≠ j. Since xⱼ ∈ Aⱼ(X) ⊆ Aⱼ(Y), the envelope φᵢⱼ\[Y\](xⱼ) is defined by Lemma 1. The candidate set { y ∈ X : yⱼ ≤ xⱼ } is contained in { y ∈ Y : yⱼ ≤ xⱼ }, so φᵢⱼ\[X\](xⱼ) ≤ φᵢⱼ\[Y\](xⱼ). Therefore xᵢ ≤ φᵢⱼ\[X\](xⱼ) ≤ φᵢⱼ\[Y\](xⱼ), and x ∈ ℛ(Y).

*Proof of (c).* By (a) and (b), ℛ(X) ⊆ ℛ(ℛ(X)). For the reverse, first note X ⊆ ℛ(X) ⊆ Box(X), so Aᵢ(ℛ(X)) = Aᵢ(X) for every i and the two sets have the same box. Next, φᵢⱼ\[ℛ(X)\] ≥ φᵢⱼ\[X\] by (b)'s inclusion argument; and conversely, if y ∈ ℛ(X) has yⱼ ≤ a then yᵢ ≤ φᵢⱼ\[X\](yⱼ) ≤ φᵢⱼ\[X\](a) by Lemma 1, so every candidate is bounded by φᵢⱼ\[X\](a) and φᵢⱼ\[ℛ(X)\](a) ≤ φᵢⱼ\[X\](a). The two envelope systems coincide, and with the same box the defining condition is the same condition. ∎ **PROVED**, and **MACHINE-CHECKED** over every subset of the boxes 3 × 3, 2 × 2 × 2 and 3 × 3 × 3, with the two guards of §7; (a) and (c) hypothesise only that X is non-empty, and (b)'s hypothesis is shown satisfiable non-trivially on each box.

**Lemma 2 (ℛ(X) is a sublattice of its box).** ℛ(X) is closed under coordinatewise ∧ and ∨.

*Proof.* Let x, y ∈ ℛ(X) and fix i ≠ j. For the join, (x ∨ y)ᵢ = max(xᵢ, yᵢ); say the maximum is xᵢ. Then xᵢ ≤ φᵢⱼ(xⱼ) ≤ φᵢⱼ(max(xⱼ, yⱼ)) = φᵢⱼ((x ∨ y)ⱼ) by Lemma 1. For the meet, (x ∧ y)ⱼ = min(xⱼ, yⱼ); say the minimum is yⱼ. Then (x ∧ y)ᵢ = min(xᵢ, yᵢ) ≤ yᵢ ≤ φᵢⱼ(yⱼ) = φᵢⱼ((x ∧ y)ⱼ). Both x ∨ y and x ∧ y lie in Box(X), since no new coordinate value is created. ∎ **PROVED.**

**Theorem 0 (the fixed points of ℛ are the sublattices; Queyranne and Tardella 2008).** For every finite non-empty X, ℛ(X) = ⟨X⟩. Consequently E(X) = 0 if and only if X is a sublattice of Box(X), and ℛ is the closure operator whose closed sets are exactly the sublattices of the box.

The identity is prior art. Queyranne and Tardella (2008), Theorem 11, prove that a sublattice of a finite product of chains is determined by its two-fold projections, each of which is a staircase; the result rests on Topkis (1976), Theorem 1, and on Veinott (1989), Corollary 11, and Baker and Pixley (1975) give the abstract form for any variety with a majority term, of which the lattice median is one. The proof of the direction Lemma 2 leaves open is short, and is written out so that nothing below rests on a citation.

*Proof.* ⟨X⟩ ⊆ ℛ(X): ℛ(X) is a sublattice of Box(X) containing X (Theorem 1(a), Lemma 2), and ⟨X⟩ is the smallest such. ℛ(X) ⊆ ⟨X⟩: let x ∈ ℛ(X). For each ordered pair i ≠ j the maximum in D3 is attained (Lemma 1), so there is a cell z⁽ⁱʲ⁾ ∈ X with z⁽ⁱʲ⁾ⱼ ≤ xⱼ and z⁽ⁱʲ⁾ᵢ = φᵢⱼ(xⱼ) ≥ xᵢ. For each i there is a cell w⁽ⁱ⁾ ∈ X with w⁽ⁱ⁾ᵢ = xᵢ, because xᵢ ∈ Aᵢ(X). Set

> u⁽ⁱ⁾ := w⁽ⁱ⁾ ∧ ⋀ⱼ≠ᵢ z⁽ⁱʲ⁾,

a meet of cells of X, hence in ⟨X⟩. Its coordinate i is min(xᵢ, minⱼ φᵢⱼ(xⱼ)) = xᵢ, since every φᵢⱼ(xⱼ) ≥ xᵢ; and for m ≠ i its coordinate m is at most z⁽ⁱᵐ⁾ₘ ≤ xₘ. So u⁽ⁱ⁾ ≤ x coordinatewise with equality at coordinate i. Then ⋁ᵢ u⁽ⁱ⁾ has coordinate i equal to max over l of u⁽ˡ⁾ᵢ, which is xᵢ because u⁽ⁱ⁾ᵢ = xᵢ and every other u⁽ˡ⁾ᵢ ≤ xᵢ. Hence x = ⋁ᵢ u⁽ⁱ⁾ ∈ ⟨X⟩. The consequence: E(X) = 0 means ℛ(X) = X, that is ⟨X⟩ = X, that is X is a sublattice. ∎ **PROVED**, and **EXHAUSTIVE** as a corroboration: over every non-empty subset of the boxes 3 × 3 and 2 × 2 × 2 — 766 sets — ℛ(X) equals ⟨X⟩ cell for cell and E(X) = 0 exactly when X is a sublattice; the same equality holds on three larger indexes computed here, the periodic table (90 cells, closure 126), the Kreuzer–Skarke slice (208, closure 748) and the orbital-rule set of §5.3 (840, closure 1,590).

**Corollary 1.** E(X) = 0 if and only if X is closed under coordinatewise meet and join. In particular, if some pair of cells of X has a join or a meet outside X then E(X) > 0. ∎

**Remark (what ℛ is called elsewhere).** ℛ tests each cell of the box against the two-fold projections of X, each of which is the staircase {(s, t) : s ≤ φᵢⱼ(t), t ≤ φⱼᵢ(s)}; that is a pairwise-consistency closure of a binary constraint network in the sense of Montanari (1974), Mackworth (1977) and Freuder (1978), the constraints being the connected row-convex class of Deville, Barette and Van Hentenryck (1999). Theorem 0 is the statement that on a product of chains the pairwise-consistent completion of X is the sublattice it generates. Caspard and Monjardet (2003) survey closure systems on a finite set in general; ℛ is one of them, and its family of closed sets is the family of sublattices of the box.

**Theorem 2 (a full box closes).** If X = Box(X) then ℛ(X) = X and E(X) = 0. In particular every singleton and every Cartesian product of chains is closed.

*Proof.* Let x ∈ Box(X) and i ≠ j. Because X is the full product, the tuple y with yᵢ = max Aᵢ(X), yⱼ = xⱼ and arbitrary admissible values elsewhere belongs to X, and yⱼ ≤ xⱼ. Hence φᵢⱼ(xⱼ) = max Aᵢ(X) ≥ xᵢ. So every cell of the box satisfies every condition, ℛ(X) = Box(X) = X. A singleton is the product of one-element chains. ∎ **PROVED**, and **EXHAUSTIVE** on the 84 boxes with 1 ≤ d ≤ 3 and side lengths 1 to 4.

**Remark 2.** For any finite X and any factorisation ∣X∣ = ab there is a bijection of X onto the a × b rectangle, and the image, being a full box, has defect 0 by Theorem 2. Two instances are computed: the 90 cells of the periodic table onto a 9 × 10 rectangle and the 365 of the calendar onto a 5 × 73 rectangle, both at E = 0. A defect is therefore never a property of the number of cells alone.

### 2.2 E belongs to the coordinatisation

**Theorem 3 (a relabelling changes the defect).** A permutation of the labels of a single coordinate can change the defect. Witness: the 365 cells (month, day) of the Gregorian calendar have E = 7; relabelling the twelve months in increasing order of length — the same 365 cells, the same incidence structure, only the labels moved — gives E = 0.

*Proof.* A computation: both sets are enumerated and both closures taken. ∎ **EXHAUSTIVE**, the two sets of 365 cells.

**Remark 1 (ordered coordinates only).** ℛ recovers monotone bounds. A coordinate whose values carry no intrinsic order must be given one before φᵢⱼ exists, and by Theorem 3 the defect depends on that choice. Where a coordinate is categorical — a kind, a language, a colour — the number E reports a property of the ranking chosen and is not a measurement of the index. The repair is to fibre over the categorical coordinate and close only the ordered coordinates inside each fibre (Theorem 4). Every coordinate of every index in this paper is a count, a date, a rank or a quantum number; the one coordinate that codes a nominal quantity — the block of a column of the periodic table in §6 — is coded by the orbital quantum number ℓ of that block, and the coding is printed there.

**Theorem 4 (fibring by a coordinate does not raise the total defect).** Let X be an index with d ≥ 2, let i be a coordinate, and let {Xᵥ : v ∈ Aᵢ(X)} be the fibration of X by coordinate i. Then the sets ℛ(Xᵥ) are pairwise disjoint, ⋃ᵥ ℛ(Xᵥ) ⊆ ℛ(X), and

> Σᵥ E(Xᵥ) ≤ E(X).

*Proof.* Each Xᵥ ⊆ X, so ℛ(Xᵥ) ⊆ ℛ(X) by Theorem 1(b). Every cell of ℛ(Xᵥ) lies in Box(Xᵥ), whose i-th factor is Aᵢ(Xᵥ) = {v}; so cells of ℛ(Xᵥ) and ℛ(X_w) differ in coordinate i whenever v ≠ w, and the closures are disjoint. Summing, Σᵥ ∣ℛ(Xᵥ)∣ = ∣⋃ᵥ ℛ(Xᵥ)∣ ≤ ∣ℛ(X)∣, while Σᵥ ∣Xᵥ∣ = ∣X∣ because the fibres partition X. Subtracting gives the inequality. Nothing in the argument depends on which coordinate i is. ∎ **PROVED**, and **MACHINE-CHECKED** — the inclusion ℛ(Xᵥ) ⊆ ℛ(X) only, the rest being the counting above — over every subset of 3 × 3, 2 × 2 × 2 and 3 × 3 × 3, fibred over every coordinate of each box (8 instances).

**Remark 3 (a general partition can raise it).** The inequality is special to fibring by a coordinate; it is the disjointness of the closures that carries it, and a general partition does not have that. Witness: X = {(0,0), (0,1), (1,0)} has ℛ(X) = the full 2 × 2 box and E(X) = 1. The partition {(0,1), (1,0)} ∪ {(0,0)} has fibred defect E({(0,1),(1,0)}) + E({(0,0)}) = 2 + 0 = 2 > 1: the first part's closure is again the whole box, and it overlaps the second part. **REFUTATION** of the claim "every partition has fibred defect at most E(X)", the witness verified by computation.

**Corollary 2 (E = 0 is relative to a fibration).** Fibre X by coordinate 1, then each fibre by coordinate 2, and so on to coordinate d. By Theorem 4 applied at each step inside each part, the fibred defect never increases along the chain; its last term is the fibration into singletons, whose defect is 0 since a singleton is a full box (Theorem 2). So refinement by coordinates alone drives the total defect to zero, and a statement "E = 0" is a statement about a set **relative to a declared fibration**: the coarser the fibration the stronger the claim, and the coarsest is the single fibre. ∎ **PROVED**, and **EXHAUSTIVE**: on every non-empty subset of 3 × 3 and 2 × 2 × 2 (766 sets) the chain of fibred defects is non-increasing and ends at 0.

Every defect reported in this paper is computed at the single fibre — one index, all coordinates ordered, no categorical axis — which is the strongest form available.

### 2.3 A coordinate cannot repair an index

**Theorem 5 (an extension never repairs).** Let S be a subset of a box B, C a finite product of chains, h : B → C any map, and Sʰ := { (x, h(x)) : x ∈ S } ⊆ B × C. If Sʰ is closed under the meet and join of B × C then S is closed under the meet and join of B.

*Proof.* Let a, b ∈ S. Then (a, h(a)) and (b, h(b)) lie in Sʰ, so their join (a ∨ b, h(a) ∨ h(b)) lies in Sʰ. Every element of Sʰ has first component in S, so a ∨ b ∈ S. The same argument with the meet gives a ∧ b ∈ S. ∎ **PROVED**. The proof uses only that C carries coordinatewise meet and join, so it holds for any m. **MACHINE-CHECKED** at m = 1 over every subset S of 3 × 3 with every h into a 3-chain, and every subset of 2 × 2 × 2 with every h into a 2-chain, with the two guards of §7.

**Theorem 6 (the criterion).** Let S ⊆ B be closed under meet and join, C a finite product of chains, and h : B → C. Then Sʰ is closed under meet and join **if and only if** h restricted to S preserves them: h(a ∨ b) = h(a) ∨ h(b) and h(a ∧ b) = h(a) ∧ h(b) for all a, b ∈ S.

*Proof.* (⇐) For a, b ∈ S, a ∨ b ∈ S by hypothesis and h(a ∨ b) = h(a) ∨ h(b), so (a, h(a)) ∨ (b, h(b)) = (a ∨ b, h(a) ∨ h(b)) = (a ∨ b, h(a ∨ b)) ∈ Sʰ; likewise for the meet. (⇒) Let a, b ∈ S. The join of their graph points is (a ∨ b, h(a) ∨ h(b)), which by hypothesis lies in Sʰ; every element of Sʰ is of the form (x, h(x)), and its first component here is a ∨ b, so its second component is h(a ∨ b). Hence h(a ∨ b) = h(a) ∨ h(b). Likewise for the meet. ∎ **PROVED**, again for any m, and **MACHINE-CHECKED** at m = 1 over the same two boxes, with the same guards.

**Refutation 1 (the converse of Theorem 5 fails, d = 2).** The claim "*if S is closed under meet and join then so is Sʰ*" is false. **Witness**, on the box 3 × 3 with C = {0, 1, 2}: take

> S = { (0,0), (1,1) },  h(0,0) = 1, h(x) = 0 for every other x.

S is closed: (0,0) ∧ (1,1) = (0,0) ∈ S and (0,0) ∨ (1,1) = (1,1) ∈ S. But Sʰ = { ((0,0), 1), ((1,1), 0) }, and the join of its two elements is ((1,1), 1), which is not in Sʰ because h(1,1) = 0. ∎ **REFUTATION**; the witness is verified by enumeration, and Z3 independently finds an S and an h on that box satisfying the negation of the converse.

**Refutation 2 (the same at d = 3).** On the box 2 × 2 × 2 with C = {0, 1}: S = { (0,0,0), (1,1,1) }, closed; h(0,0,0) = 1 and h = 0 elsewhere. The join of the two graph points is ((1,1,1), 1) ∉ Sʰ. ∎ **REFUTATION**, verified the same two ways.

**Corollary 3 (the price of a derived coordinate).** Let X be closed, E(X) = 0, C a finite product of chains, and let h : X → C fail to preserve the meet or the join at some pair of cells of X. Then E(Xʰ) > 0.

*Proof.* X is a sublattice of its box by Corollary 1, so every meet and join of cells of X lies in X, and the hypothesis of Theorem 6 is met. Theorems 5 and 6 take h on the whole box; extend h from X to Box(X) arbitrarily, which changes nothing, since both proofs use h only on S = X. By Theorem 6 the extension Xʰ is then not a sublattice of Box(X) × C, which is a product of chains and is the box of Xʰ or contains it. A subset of a product of chains that is not closed under its meet and join is not closed under those of any sub-box either, so Xʰ is not a sublattice of Box(Xʰ), and by Corollary 1, E(Xʰ) > 0. ∎ **PROVED.**

Corollary 3 is the structural content of two measurements made below: adjoining ∣Δℓ∣ and ∣ΔS∣ to Λ₉ (§5.4) and adjoining the electron count to the product grid (§4.4). Neither map preserves the join, and neither extension is closed.

### 2.4 Rules of sublattice shape

**Lemma 3 (a bimonotone cut of a sublattice is a sublattice).** Let X be a sublattice of a product of chains, let i ≠ j be coordinates, let a, b ≥ 0 be integers and c ∈ ℤ. Then

> X′ := { x ∈ X : a·xᵢ − b·xⱼ ≥ c }

is a sublattice. The cases a = 0 or b = 0 are the one-coordinate bounds xⱼ ≤ c′ and xᵢ ≥ c′, and the inequality a·xᵢ − b·xⱼ ≤ c is the same shape with the roles of i and j exchanged.

*Proof.* Let x, y ∈ X′. Their join and meet are in X because X is a sublattice. For the join, let yⱼ ≤ xⱼ without loss of generality, so (x ∨ y)ⱼ = xⱼ; then a·(x ∨ y)ᵢ − b·(x ∨ y)ⱼ = a·max(xᵢ, yᵢ) − b·xⱼ ≥ a·xᵢ − b·xⱼ ≥ c, using a ≥ 0. For the meet, let xᵢ ≤ yᵢ without loss of generality, so (x ∧ y)ᵢ = xᵢ; then a·xᵢ − b·min(xⱼ, yⱼ) ≥ a·xᵢ − b·xⱼ ≥ c, using b ≥ 0. ∎ **PROVED.** The inequalities of this shape are the bimonotone linear inequalities of Queyranne and Tardella (2006), and the lemma is the finite-chain case of their observation that such inequalities cut sublattices.

**Corollary 4 (the convexity criterion).** Let X be a sublattice of its box, g(x) = xᵢ − xⱼ a difference of two coordinates, and C ⊆ ℤ an interval. Then { x ∈ X : g(x) ∈ C } is a sublattice. In particular, for any two cells a, b, the values g(a ∨ b) and g(a ∧ b) lie in the closed interval between g(a) and g(b).

*Proof.* An interval [lo, hi] is the conjunction xᵢ − xⱼ ≥ lo and xⱼ − xᵢ ≥ −hi, two cuts of Lemma 3's shape applied in turn (an unbounded interval is one cut). For the last sentence apply the first to the sublattice generated by a and b with C the interval between g(a) and g(b). ∎ **PROVED**, and the interval property is **EXHAUSTIVE** for Δℓ and ΔS on all 1,367,031 pairs of Λ₉ (§5), with zero violations.

**Proposition 2 (the closed rows of the catalogue are closed by theorem).** Each of the following is a sublattice of a product of chains and therefore has E = 0 by Theorem 0:

- **Λ**, the set of cells of the box {1,2,3} × {0,1} × {1,2,3} × {0,…,3} × {1,2,3} × {0,1} × {0,…,3} × {0,…,3} that satisfy the eight inequalities of §3.1, each of which has the shape of Lemma 3: n − ℓ ≥ 1, 4ℓ − k ≥ −2, k ≥ 1, k − q ≥ 0, e − f ≥ 1, 4f − g ≥ −2, q − g ≥ 0, k − 2S ≥ 0;
- **Λ₉** = the cells (x, 2S′) of Λ × {0,…,3} with g − 2S′ ≥ 0, and **Λ₁₀** = the cells (x, 2S′, v) of Λ₉ × {0,…,3} with v − 2S′ ≥ 0 and g − v ≥ 0;
- **the box ordering**, the cells of {0,…,4}³ with l − w ≥ 0 and w − h ≥ 0;
- **the product grid** of §3.7, the product of three alphabets cut by Z − c ≥ 1;
- **Janet's table** as an index on (n + ℓ, Z): for each value s of n + ℓ the Z values form an interval [α(s), β(s)] with α and β non-decreasing in s.

*Proof.* A product of chains is a sublattice of itself (Theorem 2 gives it as a closed set; closure under ∧ and ∨ is immediate). Each of the first four sets is that product cut by finitely many inequalities of Lemma 3's shape, so each is a sublattice of the product, and a sublattice of the product contained in its own box is a sublattice of that box, the operations being the same. For Janet: let (s, Z) and (s′, Z′) be cells with s ≤ s′. Their join is (s′, max(Z, Z′)): max(Z, Z′) ≥ Z′ ≥ α(s′), and max(Z, Z′) ≤ max(β(s), β(s′)) = β(s′). Their meet is (s, min(Z, Z′)): min(Z, Z′) ≤ Z ≤ β(s), and min(Z, Z′) ≥ min(α(s), α(s′)) = α(s). Both are cells. Theorem 0 then gives E = 0 in each case. ∎ **PROVED**; that each index is the set its clause describes is **EXHAUSTIVE** (§7), and each E = 0 is recomputed in Table 1.

The proposition is the reason Table 1's zeros carry no surprise: Λ closes because its membership rule is a conjunction of eight bimonotone inequalities, not because of anything about atoms; the grid closes because its one condition is bimonotone; Janet's table closes because its columns are intervals that move monotonically. What would have been a finding — a closed index whose rule is not of sublattice shape — does not occur in this catalogue.

---

## §3 · The catalogue

Sixteen rows are built and closed — fifteen indexes, the particle-bound nuclides taken at two cutoffs. Each is defined here by its coordinates and its membership rule; each cell count, box and defect in Table 1 is recomputed. They fall into three groups, and the group is stated before the number: **closed by theorem** (Proposition 2 or Theorem 2), **open with the admitted-and-absent cells named**, and **open by construction** (a hole in the value set of a difference, Corollary 1).

### 3.1 The atomic lattice and its tower — closed by theorem

Λ has eight integer coordinates (n, ℓ, k, q, e, f, g, 2S). A cell is a **transfer type**: q electrons are taken from the subshell (n, ℓ), which holds k of them, and g of them are placed in the subshell (e, f); q runs to 3 and g to q, so a cell may move up to three electrons and the q − g not placed are not tracked; q = g = 0 and (n, ℓ) = (e, f) are cells; 2S is twice the source total spin. The membership rule is eight inequalities, none of them introduced here:

> ℓ ≤ n − 1 (the hydrogenic bound, Bohr 1913), k ≤ 4ℓ + 2 and k ≥ 1 (Stoner's subshell capacity of 1924, made exclusive by Pauli 1925), q ≤ k, f ≤ e − 1, g ≤ 4f + 2, g ≤ q, 2S ≤ k (the capacity with Hund's first rule, 1925).

At the caps n, e ∈ {1,2,3}, ℓ, f ∈ {0,1}, k, q, g, 2S ∈ {0,…,3} this gives **976 cells in a box of 6,912, E = 0**. Λ₉ adjoins the target multiplicity 2S′ with 2S′ ≤ g: **1,654 cells in a box of 27,648, E = 0**. Λ₁₀ adjoins the seniority v with 2S′ ≤ v ≤ g: **2,535 cells in a box of 110,592, E = 0**. All three zeros are Proposition 2: every inequality is bimonotone.

### 3.2 The same 118 elements, twice

**The periodic table** (Mendeleev 1869; the eighteen-column arrangement is one of the thousand-odd periodic systems published since — Scerri 2016), coordinates (period, group), one cell per element of the arrangement with the f-block detached: **90 cells in a box of 126, E = 36** — open, with the cells named. The 36 admitted-and-absent cells are exactly period 1 groups 2 to 17, period 2 groups 3 to 12 and period 3 groups 3 to 12 — the gaps of the short periods, every one of them (Figure 1). They are supplied to a reader from outside the table; that is what the defect counts.

The 36 are placement-sensitive. Drawing helium at group 2 instead of group 18, on the same 90 elements, gives **E = 20**. The mechanism is the envelope: φ_group,period(1), the largest group reached at period 1, is 18 under the standard placement and 2 under the alternative, so the whole first row of admitted-and-absent cells exists only under the first. The difference of sixteen cells is the cost of specifying that choice.

**Janet's left-step table** (Janet 1928), coordinates (n + ℓ, Z), the same 118 elements ordered on the Madelung sum: **118 cells in a box of 944, E = 0** — closed by theorem, because each n + ℓ column is an interval of Z and the intervals are consecutive (Proposition 2). The two indexes have the same subject and different defects. That is Theorem 3's point demonstrated on one object rather than argued.

![**Figure 1.** The eighteen-column periodic table as an index on (period, group). Blue: the 90 cells the table holds. Red: the 36 its own coordinates admit and it denies — period 1 groups 2 to 17, period 2 groups 3 to 12, period 3 groups 3 to 12. A reader given only the occupied cells would reconstruct all 126.](figures/figure-1-periodic-table.png)

### 3.3 Convention, order, and a full product

**The Gregorian calendar**, coordinates (month, day), the 365 cells of a common year: **365 cells in a box of 372, E = 7** — open, with the cells named. The seven admitted-and-absent cells are (2, 29), (2, 30), (2, 31), (4, 31), (6, 31), (9, 31) and (11, 31) — February's three missing days and the four thirty-day months' thirty-firsts. The index fails to close for one reason: the number of days is not monotone in the month index, so the columns are not a staircase. Relabelling the months in order of length repairs it exactly (Theorem 3), and produces a calendar no one can use. The seven is the price of keeping January first.

**A box ordering**, coordinates (l, w, h) with l ≥ w ≥ h over five values: **35 cells in a box of 125, E = 0** — closed by theorem (two bimonotone cuts, Proposition 2).

**A chessboard**, coordinates (rank, file): **64 cells in a box of 64, E = 0** — closed by Theorem 2, and carrying no information, because its box is its cells. Between the two, E = 0 is shown to carry information only when the box exceeds the cells, which is why Table 1 reports the box in every row.

### 3.4 The nuclide chart, on two populations — open, with the cells named

The nuclide chart has coordinates (Z, N). Two different populations are indexed, and they give different defects; both are reported.

**The particle-bound light nuclides**, derived from NUBASE2020 (Kondev, Wang, Huang, Naimi and Audi 2021): a ground state with Z ≥ 1 is taken as particle-bound when the evaluation neither marks it particle-unstable nor lists prompt emission of one or more nucleons or of an α particle as its first decay mode. The derivation is mechanical and the list is not typed by hand. At six proton-number cutoffs:

| cutoff | cells | admitted | E | cells added to the nine |
|---|---|---|---|---|
| Z ≤ 5 | 27 | 33 | 6 | — |
| Z ≤ 6 | 40 | 48 | 8 | — |
| Z ≤ 7 | 52 | 61 | **9** | — |
| Z ≤ 8 | 64 | 73 | **9** | — |
| Z ≤ 9 | 77 | 86 | **9** | — |
| Z ≤ 10 | 94 | 106 | **12** | F-16, F-28, F-30 |

The nine admitted-and-absent cells at Z ≤ 7 are **He-5, He-7, Li-10, Be-8, Be-13, B-9, B-16, B-18, C-21**; the three added at Z ≤ 10 are **F-16, F-28, F-30**. Every cell named at one cutoff persists at every larger one, and every one of the twelve is a ground state the evaluation lists as particle-unbound: the defect names real nuclides, not unlisted cells, at every cutoff. The count is not stable across cutoffs: the three fluorine cells appear only when neon enters, because their neutron numbers 7, 19 and 21 are first realised by Ne-17, Ne-29 and Ne-31, and the box is the product of the observed alphabets (D2). What is stable is the reading, not the number. Be-8 is unbound because it is two α particles; He-5, He-7, Li-10 and Be-13 are unbound by one neutron against an even-paired core; the diproton is absent from this population altogether because it is a hole at the edge, not in the interior. (Z, N) records how many protons and neutrons a nuclide has and cannot record that four of them prefer to be an α particle, or that the last neutron is unpaired. Reading the twelve as the pairing and clustering terms of the semi-empirical mass formula (von Weizsäcker 1935) is an interpretation of the cells, and is marked as such.

**The AME2020 evaluation (Huang, Wang, Kondev, Audi and Naimi 2021; Wang, Huang, Kondev, Audi and Naimi 2021), Table I** — 3,558 rows, Z from 0 to 118, of which 2,550 carry a measured mass and 1,008 an extrapolated one — gives 3,558 distinct (Z, N) cells and **E = 2** at every cutoff Z ≤ 20, 50, 82, 92, 118. The two admitted-and-absent cells are (0, 0), which is the bottom of the box — admitted by the closure of any set containing the neutron (0, 1) and the proton (1, 0), and an artefact of indexing the neutron rather than a nuclide — and (2, 0), the diproton, the one admitted-and-absent nuclide. The diproton is unbound because the nucleon–nucleon interaction in the spin-singlet channel is too weak to bind (the deuteron binds only in the triplet) and the Coulomb repulsion adds to that; it is a failure of any smooth mass formula at A = 2, not of one term of it. The number is 2 and not 9 because the population is different: the AME2020 set is not the particle-bound set, and includes unbound and extrapolated species that fill most of the region the smaller chart leaves open. The nameability of the cells survives on both populations; the count does not transfer between them, and the two rows of Table 1 are two different indexes.

### 3.5 The Kreuzer–Skarke slice — open by construction

Coordinates (h(1,1), h(2,1)), the two Hodge numbers of a Calabi–Yau threefold, usually written with the superscripts 1,1 and 2,1. The complete list of reflexive four-dimensional polytopes is that of Kreuzer and Skarke (2002), whose construction rests on Batyrev's polar duality (1994); the list itself was not read here. One slice of it is stated exactly in the literature: Candelas, de la Ossa, He and Szendrői (2008) record that the points with Euler characteristic χ = 2(h(1,1) − h(2,1)) = ±6 — the slice of interest to them because ∣χ∣ = 6 is the three-generation condition — have Hodge numbers (h, h+3) and (h+3, h) for 13 ≤ h ≤ 128, with the exclusions h = 102, 103, 115, 117 and 119 to 126. That is **208 cells in a box of 12,544**, and

> **E = 540**, from 498 join failures and 498 meet failures among the 21,528 pairs.

The defect is forced by the slicing and says nothing about the list. On the slice the difference h(1,1) − h(2,1) takes exactly the two values −3 and +3: a value set with a hole at every integer between, so Corollary 4 does not apply, and Corollary 1 needs only one pair. The join of (13, 16) and (16, 13) is (16, 16), whose difference is 0; it is not on the slice, so E > 0 before any property of the list is consulted. This is the same mechanism that opens the orbital rule in §5.3. The 540 admitted cells are what the box and the two lines determine — 112 of them on the diagonal from (13, 13) to (131, 131), carrying five Euler characteristics χ ∈ {0, ±2, ±4}, with h(1,1) + h(2,1) from 26 to 262 — and they are printed as the closure of a slice, not as predictions about Calabi–Yau threefolds. The region between the two lines is one the published plot shows as densely occupied, so a lookup would find most of them; the paper draws nothing from that, because the defect was fixed by the slicing before the lookup.

### 3.6 Independent oscillators — closed by Theorem 2

The transverse oscillators of the bosonic string are free (Green, Schwarz and Witten 1987), so the admissible occupation vectors over any finite set of modes form a full product and close by Theorem 2 with E = 0. A finite instance is computed: three independent oscillators capped at occupancy 3, a 4³ box, E = 0. This is the degenerate end of the phenomenon: Λ closes because its rule is bimonotone, and a free system closes because its coordinates do not couple at all. Nothing about the string's spectrum enters.

### 3.7 A product grid over a spectroscopic survey, and the survey itself

Coordinates (Z, core charge, ℓ). Each cell is a Rydberg channel — a fixed parent core (core charge is the charge of the parent ion, one more than the ionisation stage), a fixed orbital angular momentum, the principal quantum number running. Two indexes are built from a survey of measured channels over 28 elements.

**The product grid** is the product of the 28 elements, the ten core charges {1, 2, 3, 4, 5, 6, 9, 11, 15, 16} and the eight ℓ values s to k that the survey holds, restricted to charge < Z: **1,744 cells in a box of 2,240, E = 0** — closed by theorem, because its one condition Z − c ≥ 1 is a bimonotone cut of a product (Proposition 2). Its zero is a property of the construction, and the redundancy figures of §4 that use it are figures of the construction.

**The witnessed channels** — the 285 cells of the grid that a measured channel actually occupies — form an index of their own: **285 cells in a box of 1,960** (28 elements, 10 charges, 7 values of ℓ), and its closure has 1,260 cells, so **E = 975** — open. The 975 admitted-and-absent cells are channels the survey's own alphabets and bounds admit and the survey does not hold: a statement about what has been measured under the survey's caps, expressed as a defect. This is the row that describes the survey; the grid's zero describes the grid.

### 3.8 Table 1

**Table 1.** Every index of this paper, its group, coordinates, cell count, ambient box and closure defect. Every box is the product of the observed alphabets (D2), including the two nuclide boxes.

| index | group | coordinates | cells | box | E |
|---|---|---|---|---|---|
| Λ, the atomic lattice | closed by theorem (Prop. 2) | (n, ℓ, k, q, e, f, g, 2S) | 976 | 6,912 | **0** |
| Λ₉ | closed by theorem (Prop. 2) | Λ with 2S′ | 1,654 | 27,648 | **0** |
| Λ₁₀ | closed by theorem (Prop. 2) | Λ₉ with the seniority v | 2,535 | 110,592 | **0** |
| Janet's left-step table | closed by theorem (Prop. 2) | (n + ℓ, Z) | 118 | 944 | **0** |
| a box ordering | closed by theorem (Prop. 2) | (l, w, h), l ≥ w ≥ h | 35 | 125 | **0** |
| the product grid | closed by theorem (Prop. 2) | (Z, core charge, ℓ) | 1,744 | 2,240 | **0** |
| a chessboard | full box (Thm 2) | (rank, file) | 64 | 64 | **0** |
| the dipole image | full box (Thm 2) | (∣Δℓ∣, ∣ΔS∣) | 8 | 8 | **0** |
| three capped oscillators | full box (Thm 2) | occupation per mode | 64 | 64 | **0** |
| the AME2020 nuclides | open, cells named | (Z, N) | 3,558 | 21,182 | **2** |
| the Gregorian calendar | open, cells named | (month, day) | 365 | 372 | **7** |
| particle-bound nuclides, Z ≤ 7 | open, cells named | (Z, N) | 52 | 119 | **9** |
| particle-bound nuclides, Z ≤ 10 | open, cells named | (Z, N) | 94 | 180 | **12** |
| the periodic table | open, cells named | (period, group) | 90 | 126 | **36** |
| the witnessed channels | open, cells named | (Z, core charge, ℓ) | 285 | 1,960 | **975** |
| Kreuzer–Skarke, χ = ±6 | open by construction | (h(1,1), h(2,1)) | 208 | 12,544 | **540** |

![**Figure 2.** The closure defect of the sixteen rows of Table 1, cells beside each label, grouped as the table groups them. The nine zeros are theorems (Proposition 2, Theorem 2); the seven non-zeros are either counts of named cells or, for the Kreuzer–Skarke slice, forced by a hole in the value set of a difference.](figures/figure-2-defects.png)

### 3.9 What a defect costs to transmit

The bit cost of D10 puts the defects on a common scale: it is the length of the message a reader needs beside the coordinates in order to recover the index exactly, under a uniform code over the E-subsets of the closure.

| index | ∣ℛ(X)∣ | E | bit cost |
|---|---|---|---|
| the AME2020 nuclides | 3,560 | 2 | 22.6 |
| particle-bound nuclides, Z ≤ 7 | 61 | 9 | 34.0 |
| the Gregorian calendar | 372 | 7 | 47.4 |
| the periodic table | 126 | 36 | 105.1 |
| Kreuzer–Skarke, χ = ±6 | 748 | 540 | 633.0 |

The calendar's 47.4 bits is the content of the rhyme *Thirty days hath September*, which exists because the coordinates cannot carry the month lengths and is exactly seven cells long.

---

## §4 · Redundancy

The defect asks what an index fails to say. Redundancy asks the opposite question: how much of an index can be thrown away and still recovered from what is left. It is answered here by a convention (D7), and the answer is a rung of a ladder, never a percentage measured to the digit.

### 4.1 The measure

D6 and D7 give two numbers per index. **Coupling** counts the envelopes that bind: an envelope φᵢⱼ that equals max Aᵢ(X) everywhere imposes nothing, and a pair of coordinates joined only by such envelopes is, as far as ℛ can see, independent. **Redundancy** is the largest ladder rung at which a random deletion is recovered in at least 8 of 10 trials. Every figure below was taken at seed 20260809 with ten trials per rung, and is printed with the rung passed, the rung failed and the counts at each, which is how close each pass was.

### 4.2 The six rows

**Table 2.** Coupling and redundancy on six indexes. d(d − 1) is the envelope count; the last column is the trial log, rung: recovered of ten, up to the first failure.

| index | d | envelopes | coupling | redundancy | trial log |
|---|---|---|---|---|---|
| Λ | 8 | 56 | 28.6% | **61%** | «R1-Lambda» |
| the product grid | 3 | 6 | 16.7% | **20%** | «R1-grid» |
| a box ordering | 3 | 6 | 50.0% | below 5% | «R1-box» |
| Janet as a down-set | 2 | 2 | 50.0% | below 5% | «R1-janet» |
| the periodic table | 2 | 2 | 0.0% | below 5% | «R1-pt» |
| the Gregorian calendar | 2 | 2 | 0.0% | below 5% | «R1-cal» |

The Janet row is not the 118-cell index of Table 1 but the left-step table read as the down-set of the 118-element filling along n + ℓ — 724 cells, E = 0 — a choice made so that a deletion has interior cells to remove; the 118-cell form has coupling 100% and fails the first rung too. The choice is a convention of the same standing as the ladder.

**What the rows show, and what is not claimed.** The box ordering and the Janet down-set both couple at 50% and recover nothing; the product grid couples at 16.7% and recovers a fifth; Λ couples at 28.6% and recovers three fifths. Coupling therefore does not order redundancy. No regression, correlation coefficient or significance is reported: six points whose ordinate is quantised to a ten-rung ladder and sits below the first rung at four of them support no fit.

### 4.3 Dimension, on one object

ℛ works on pairwise envelopes, so an index of dimension d has d(d − 1) of them — 56 for Λ, 6 at three coordinates, 2 in a plane. The comparison across six different subjects confounds dimension with everything else about them, so the measurement is repeated on a **single object**, Λ projected onto its first d coordinates with its constraints unchanged:

| d | cells | E | redundancy | trial log |
|---|---|---|---|---|
| 8 | 976 | 0 | **61%** | «R3-8» |
| 7 | 319 | 0 | **30%** | «R3-7» |
| 6 | 165 | 0 | **30%** | «R3-6» |
| 5 | 99 | 0 | **30%** | «R3-5» |
| 4 | 33 | 0 | **5%** | «R3-4» |
| 3 | 12 | 0 | below resolution | no trial: ⌊0.05 × 12⌋ = 0 |

Every projection is itself closed, so the comparison is between closed indexes throughout and is not contaminated by a change of defect. The rung reached is non-decreasing in d. This is one object at six dimensions, with the cell count falling alongside the dimension, which the design does not separate from it; it is a measurement of the convention on one object, not a law.

![**Figure 3.** Left: the redundancy rung reached against the number of coordinates, measured on Λ projected onto its first d, at seed 20260809; the d = 3 projection has 12 cells and is below the ladder's resolution. Right: redundancy against coupling over the six indexes of Table 2; the four indexes below the first rung are drawn at 0. Points that coincide carry both labels.](figures/figure-3-redundancy.png)

### 4.4 Only independent coordinates count

A coordinate that is a function of coordinates the index already carries adds no information, and obliges ℛ to reproduce it exactly. Adjoining the electron count Nₑ = Z − c + 1 to the three-coordinate product grid, a function of two coordinates it already holds:

| quantity | before | after |
|---|---|---|
| coordinates | 3 | 4 |
| envelopes | 6 | 12 |
| coupling | 16.7% | 33.3% |
| redundancy | **20%** | below 5% |
| E | **0** | **20,808** |

The envelope count doubles and the coupling rises — both movements that a reading of coupling as a proxy for reconstructibility would call favourable. Recovery instead fails at the very first rung, and the index stops being closed.

Corollary 3 says why, and its hypothesis is verified rather than assumed. Nₑ is decreasing in the core charge, so it does not preserve the join; the witness is the pair of cells (Z, c, ℓ) = (3, 1, 0) and (5, 4, 0), both in the grid, with Nₑ = 3 and Nₑ = 2. Their join is (5, 4, 0), also in the grid, with Nₑ = 2, while the join of the two values is 3. A closed index extended by a map that fails to preserve the join is not closed.

---

## §5 · The electromagnetic quotient

The electric-dipole selection rules for a one-electron jump are two statements about the change in orbital angular momentum and in total spin: Δℓ = ±1, which follows from the rank of the dipole operator and the parity of the orbitals (Condon and Shortley 1935, chapter IV; Cowan 1981), and ΔS = 0 in LS coupling (Russell and Saunders 1925), both with their group-theoretic ground in Wigner (1927). Laporte's rule (1924) is the parity rule — even terms combine only with odd — of which Δℓ = ±1 is the one-electron form. This section applies the two rules to Λ₉ and measures what they do to it.

### 5.1 Two differences

On Λ₉, write

> Δℓ(c) := f − ℓ,  ΔS(c) := 2S′ − 2S.

Both are differences of two coordinates of the index. On Λ₉ at these caps ℓ and f take only 0 and 1, so ∣Δℓ∣ ∈ {0, 1}, and the two classes — Δℓ = 0, parity conserved, and ∣Δℓ∣ = 1, the electric-dipole class E1 — hold **814 and 840 cells** of the 1,654. No multipole label is attached to the Δℓ = 0 class: a jump between two different subshells with the same ℓ is parity-conserving and is not a magnetic-dipole transition, which connects levels of one configuration.

### 5.2 The spin rule cuts a sublattice

ΔS = 0 names the value set C = {0}, an interval. By Corollary 4 the cells it keeps form a sublattice of Λ₉, hence of their own box, and by Theorem 0 they are closed:

> the spin rule imposed on Λ₉ keeps **526 cells at E = 0**.

The zero is a theorem (Corollary 4 with Theorem 0) and is recomputed.

### 5.3 The orbital rule does not, and here is the witness

∣Δℓ∣ = 1 names the value set C = {−1, +1}, which has a hole at zero and is not an interval. Corollary 4 does not apply, and the set is in fact not a sublattice.

**Refutation 3 (the orbital-rule set is not a sublattice).** The claim "*the cells of Λ₉ with ∣Δℓ∣ = 1 are closed under join*" is false. **Witness**: the two cells

> a = (n, ℓ, k, q, e, f, g, 2S, 2S′) = (1, 0, 1, 0, 2, 1, 0, 0, 0),  Δℓ(a) = +1,
> b = (2, 1, 1, 0, 1, 0, 0, 0, 0),  Δℓ(b) = −1,

both of which satisfy ∣Δℓ∣ = 1. Their coordinatewise join is

> a ∨ b = (2, 1, 1, 0, 2, 1, 0, 0, 0),  Δℓ(a ∨ b) = 1 − 1 = 0,

which fails ∣Δℓ∣ = 1 and so leaves the set. ∎ **REFUTATION**, the witness found by exhaustive search over the pairs of the 840 cells and verified by direct evaluation.

By Corollary 1 the orbital-rule set therefore has a positive defect, and the measurement is

> the orbital rule imposed on Λ₉ keeps **840 cells at E = 750**.

The contrast with §5.2 is exactly the convexity of the value set, and nothing else: both rules are conditions on a difference of two coordinates of the same index, and the Kreuzer–Skarke slice of §3.5 is the same phenomenon on two coordinates.

### 5.4 Quotient, not extension

The two rules define a map

> κ : Λ₉ → ℤ × ℤ,  κ(c) = (∣Δℓ(c)∣, ∣ΔS(c)∣).

The absolute value is taken because the rules are stated on magnitudes; the sign of ΔS, which distinguishes a rise from a fall of the multiplicity, is discarded by κ and is carried by ΔS itself in §5.2.

**The image is a complete rectangle.** ∣Δℓ∣ takes the values 0 and 1 and ∣ΔS∣ the values 0, 1, 2 and 3, and every one of the eight combinations is realised, with the multiplicities

| | ∣ΔS∣ = 0 | 1 | 2 | 3 | total |
|---|---|---|---|---|---|
| ∣Δℓ∣ = 1 (E1) | 264 | 342 | 180 | 54 | 840 |
| Δℓ = 0 | 262 | 337 | 171 | 44 | 814 |

All 1,654 cells map somewhere, and the image is the full 2 × 4 box. Its defect is therefore **E = 0 by Theorem 2**, and that zero carries no information about the rules: it closes because it is a box. What the full rectangle does say is one physical thing — on Λ₉ the two quantities are independent, every combination of an orbital change with a spin change occurring. Any claim that "the electromagnetic index is closed" is a claim about the shape of that image and nothing more.

**The extension is a different object, and it is open.** Adjoining the same two quantities to Λ₉ as coordinates gives an index of eleven coordinates on the same 1,654 cells, with

> E = 9,278.

Adjoining ∣Δℓ∣ alone gives E = 1,654; adjoining ∣ΔS∣ alone gives E = 3,812.

Corollary 3 accounts for all three, and its hypothesis is exhibited for each map rather than inferred from the defect. For ∣Δℓ∣ the witness is Refutation 3's pair: both members have ∣Δℓ∣ = 1, their join has ∣Δℓ∣ = 0, and 0 is not the join of 1 with 1. For ∣ΔS∣ the witness is

> (1, 0, 1, 0, 1, 0, 0, 1, 0) and (1, 0, 1, 1, 1, 0, 1, 0, 1), with ∣ΔS∣ = 1 each,

whose join (1, 0, 1, 1, 1, 0, 1, 1, 1) is again a cell of Λ₉ and has ∣ΔS∣ = 0. The same pair witnesses the failure for the two maps taken together. A selection rule divides an index; it does not extend one, and the difference between the two readings is 9,278 cells.

### 5.5 Followability of ground-configuration moves, on two populations

The measurement that follows is on a different population, built from the observed ground configurations of all **118 elements** as NIST tabulates them, including its assignments for the ambiguous heavy elements (Kramida, Ralchenko, Reader and the NIST ASD Team 2024). A cell is a move between two distinct occupied subshells of one element: (Z, n, ℓ, k, q, e, f, g), where the subshell (n, ℓ) of element Z holds k electrons, 1 ≤ q ≤ k of them are taken, and 1 ≤ g ≤ min(q, 4f + 2) of those are placed in another occupied subshell (e, f) of the same element. There are **4,325** such cells, all distinct. This is the population on which a crossing was previously reported, and it is unphysical in two ways that its rule does not see: the bound 4f + 2 is the target's capacity and not its room, so **2,923** of the 4,325 moves deliver more electrons than the target subshell can still hold (2,203 of them into a subshell that is already full), and **2,819** move more than one electron, to which the one-electron rules do not apply. The **physical population** is the subset with q = g = 1 and at least one vacancy in the target: **134** moves.

Followability is the formal match of D9: a move is followable when its target (e, f), at the count g it delivers, equals the source (n, ℓ), at its occupancy k, of some move. Two scopes are measured: *within one element*, where the matching move must belong to the same Z; and *across the table*, where it may belong to any of the 118. The match is a coincidence of two integers — electrons delivered against electrons held — and carries no physical reading; it is the bookkeeping the earlier figures rest on, reproduced here so that the comparison is exact.

**Table 3.** Followability by selection class on both populations. Percentages are of the class's own cell count.

| class | unfiltered: cells | within one element | across the 118 | physical: cells | within one element | across the 118 |
|---|---|---|---|---|---|---|
| all cells | 4,325 | 982 (22.7%) | 3,686 (85.2%) | 134 | 21 (15.7%) | 72 (53.7%) |
| ∣Δℓ∣ = 1 (allowed) | 2,673 | 309 (**11.6%**) | 2,399 (**89.7%**) | 59 | 7 (**11.9%**) | 24 (**40.7%**) |
| ∣Δℓ∣ ≠ 1 (forbidden) | 1,652 | 673 (**40.7%**) | 1,287 (**77.9%**) | 75 | 14 (**18.7%**) | 48 (**64.0%**) |
| Δℓ even | 606 | 233 (38.4%) | 544 (89.8%) | 50 | 12 (24.0%) | 34 (68.0%) |
| Δℓ odd | 3,719 | 749 (20.1%) | 3,142 (84.5%) | 84 | 9 (10.7%) | 38 (45.2%) |

**On the unfiltered population the order reverses** between the scopes — allowed below forbidden within an element (11.6% against 40.7%), allowed above forbidden across the table (89.7% against 77.9%) — which is the crossing as it was reported. **On the physical population it does not**: the forbidden class leads within one element (18.7% against 11.9%) and across the table (64.0% against 40.7%) alike. The crossing is a property of the 2,923 moves the Pauli principle excludes and the 2,819 that move more than one electron; on the moves to which the electric-dipole rules apply there is no crossing, and the paper claims none. The parity split (Δℓ even against odd) does not cross on either population.

A configurational match — the target at the occupancy it holds after the move, k_target + g, against the source (n, ℓ, k) of some move — is also computed. Within one element it is zero for every class on both populations, necessarily: every move in the population starts from a ground configuration, and no ground configuration is another's successor by one move. Across the table, on the physical population, the allowed class is followable in 3 of 59 cells (5.1%) and the forbidden in 20 of 75 (26.7%): the same order, no crossing.

![**Figure 4.** Followable fraction by selection class, within one element (blue) and across the 118 elements (orange). Left: the unfiltered population of 4,325 moves, on which the allowed and forbidden bars change order between the scopes. Right: the 134 physical one-electron moves into a subshell with room, on which they do not.](figures/figure-4-crossing.png)

---

## §6 · Which languages can speak of an index

An index can be closed in more than one sense, and the senses are the formal languages a question about it may be posed in. Five operators are measured here (D11). Each takes a finite index and returns an admitted superset, so each returns a decision per cell and the results can be compared cell for cell.

**Lemma 4 (each operator returns a superset of X).** For each of the five operators L of D11, X ⊆ L(X) ⊆ Box(X).

*Proof.* Order: Theorem 1(a). Algebra: ⟨X⟩ contains X by definition. Geometry and statistics: a cell x ∈ X has (xᵢ, xⱼ) ∈ πᵢⱼ(X) ⊆ conv(πᵢⱼ X) for every pair, so x satisfies both set formulas. Information: order the cells of X by the coordinatewise order and argue by induction on height; a generator is in the join-closure by definition, and a non-generator x is the coordinatewise join of the cells of X strictly below it, each of which is in the join-closure by induction, so x is too. Every operator's output is a subset of Box(X) because joins, hulls and the set formulas create no new coordinate value. ∎ **PROVED**; that no operator drops a cell of its index is also **EXHAUSTIVE** on the four indexes below.

**What the measurement refuses to report, and why it matters.** Three refusals bind every number in this section.

1. A language that was not run is not silent. A language that returns no cell decision on an index is reported as not run, and never as a measured silence. Only a language whose operator ran and whose precondition failed counts as a finding.
2. **Agreement at two coordinates is not evidence.** At d = 2 there is exactly one coordinate pair, so pairwise consistency and cell membership coincide and every pairwise operator agrees for no reason at all. Such a run is marked degenerate and its agreement is withheld. This is checked: the two-coordinate periodic table is degenerate and the three-coordinate one is not. Every agreement figure below is at d ≥ 3.
3. **The roster is not settled and is not settled here.** Which formal languages there are, and how many of them bear an operator, is an open question. The measurement therefore counts a language as operator-bearing **on the index in front of it** — it returned a cell decision — and computes the pair count from that, rather than asserting a list.

**A pair that agrees by theorem.** Order and algebra return the same set on every finite index, by Theorem 0. Of the C(5,2) = 10 pairs among the five, that one is therefore not evidence of anything, and the figures below count it separately: the informative count is over the **four distinct operators** — order (= algebra), geometry, information, statistics — with C(4,2) = 6 pairs.

**The measurement on Λ.** All five operators return an admitted set on Λ, and each returns E = 0. All 10 of the 10 pairs agree; discounting the order–algebra pair, **6 of 6**. The same holds on the box ordering (6 of 6) and on Λ₉ (6 of 6).

Two further readings are special, and they are special for different reasons. A **documentary** reading returns a citation rather than a cell decision; it has no mechanism at all and is silent by construction. An **analysis** reading has a mechanism — a fit — but returns a magnitude, an R² or a slope, not a decision about a cell; it cannot join the pairwise arithmetic, and it is reported as not run unless a witness is declared. The count of five is thus measured, not assumed, and the five it counts are order, algebra, geometry, information and statistics.

**The discriminating case.** The periodic table at three coordinates — (period, group, ℓ), where the third coordinate is the orbital quantum number of the block of the column in the eighteen-column arrangement: ℓ = 0 for columns 1 and 2, ℓ = 2 for columns 3 to 12, ℓ = 1 for columns 13 to 18, helium carrying its column's value — separates the operators completely:

| language | order | algebra | geometry | information | statistics |
|---|---|---|---|---|---|
| defect | 100 | 100 | 83 | 24 | **0** |

The third coordinate is a function of the second and is ordered by ℓ; it is a choice of order on three blocks (Remark 1), the choice is stated, and the numbers are the numbers for that choice. Of the ten pairs one agrees — order with algebra, the pair that agrees by theorem — and **0 of the 6** pairs among the distinct operators agree. The statistics reading gives zero because a set formula on the pairwise projections cannot see a hole: every pairwise projection of every absent cell is realised somewhere, so nothing is excluded. Agreement among the languages is thus not automatic, and where it holds it is a fact about the index.

**Agreement and closure.** If every operator returns E = 0 then every operator returns X itself (Lemma 4), so all five agree: that direction is immediate. The converse — that agreement forces every defect to be zero — is not proved here and is not true in general: five operators can agree on a common proper superset of X. What is measured is that on the four indexes here with d ≥ 3 — Λ, the box ordering, Λ₉ and the three-coordinate periodic table — the five agree exactly when all five defects are zero, three cases to one. Four indexes are not a law, and the paper states none. The containments that do hold among these operators on every finite index are the subject of a separate manuscript (Lach 2026), cited for that and for nothing in this paper's proofs; Beeri, Fagin, Maier and Yannakakis (1983) is the classical source for the reading of pairwise agreement as a closure condition.

---

## §7 · Verification record

The verification program prints one row per obligation and all pass; in self-test mode four negative controls are added, each of which must be reported as refuted and is. The row count and the distribution by status are those of the program's own summary, «SUMMARY».

**By object.**

| object | PROVED | MACHINE-CHECKED (box) | EXHAUSTIVE / MEASURED (family) | SAMPLED / CITED / REFUTATION |
|---|---|---|---|---|
| Lemma 1, the envelope | ✓ | — | — | — |
| Theorem 1, closure operator | ✓ | ✓ 3 obligations: every subset of 3×3, 2×2×2, 3×3×3 | — | — |
| Lemma 2, ℛ(X) a sublattice | ✓ | — | — | — |
| Theorem 0, fixed points are sublattices | ✓ (prior art, proof written) | — | **766 subsets** of 3×3 and 2×2×2; 3 indexes of 90, 208, 840 cells | CITED (Queyranne and Tardella 2008) |
| Theorem 2, a full box closes | ✓ | — | **84 boxes**, 1 ≤ d ≤ 3, sides 1–4; Remark 2's two rectangles | — |
| Theorem 3, relabelling | — | — | the calendar, 365 cells twice | — |
| Theorem 4, fibring by a coordinate | ✓ | ✓ 1 obligation, the inclusion only, 8 instances over three boxes and every coordinate | — | — |
| Remark 3, a general partition | — | — | — | REFUTATION, the three-cell witness |
| Corollary 2, iterated fibration | ✓ | — | the chain on 766 subsets | — |
| Theorem 5, extension never repairs | ✓ | ✓ 2 obligations: (3×3, h into a 3-chain), (2×2×2, h into a 2-chain) | — | — |
| Theorem 6, the criterion | ✓ | ✓ 2 obligations, same two boxes | — | — |
| Refutations 1 and 2 | — | Z3 finds a witness for the negation on both boxes | witness verified by enumeration | REFUTATION |
| Corollary 3 | ✓ | — | its hypothesis exhibited for all four maps used (§4.4, §5.4) | — |
| Lemma 3, bimonotone cut; Corollary 4 | ✓ | — | interval property on **1,367,031 pairs** of Λ₉, two maps, 0 violations | — |
| Proposition 2, closed by theorem | ✓ | — | Λ = box ∩ eight cuts (976 cells, equal to the tower's); Λ₉, Λ₁₀; the box ordering; the grid; Janet's intervals | — |
| Table 1, sixteen rows | — | — | every cell of every index, closure computed in full | AME2020, NUBASE2020 CITED |
| the periodic table's 36 | — | — | the 36 named and matched; helium at 2 gives 20 | — |
| the nuclide populations | — | — | MEASURED: six cutoffs from NUBASE2020, every absent cell an unbound nuclide; 3,558 AME2020 rows at 5 cutoffs | the excerpt's checksum |
| Kreuzer–Skarke, 540 cells | — | — | 21,528 pairs; the value set {−3, +3}; the witness pair | the slice CITED |
| the survey | — | — | MEASURED: the grid 1,744 / 2,240 / 0; the witnessed channels 285 / 1,960 / 975 | — |
| Refutation 3, the orbital witness | — | — | exhaustive pair search over 840 cells | REFUTATION |
| Table 2, §4.3, §4.4, redundancy | — | — | coupling exact on every envelope; every projection closed | **SAMPLED**, seed 20260809, logs printed |
| §5.4, quotient and extensions | — | — | all 1,654 cells, three extensions closed in full; a join-failure witness for each map | — |
| §5.5, followability | — | — | MEASURED: all 4,325 moves and the 134 physical ones, five classes, two scopes, two matches | ground configurations CITED |
| §6, the five languages | — | — | four indexes at d ≥ 3, ten pairs and six distinct pairs each; Lemma 4's superset property | — |

**The exhausted families, named.** 84 boxes: every shape with 1 ≤ d ≤ 3 and every side in 1 to 4. 766 subsets: every non-empty subset of 3 × 3 (511) and of 2 × 2 × 2 (255). 1,367,031 pairs: every unordered pair of distinct cells of Λ₉. 21,528 pairs: every unordered pair of the 208 Kreuzer–Skarke cells. 4,325 moves: every ordered pair of distinct occupied subshells of every one of the 118 ground configurations, with every admissible (q, g); 134 of them physical. The closures of Table 1 are computed cell by cell over the full ambient box in every case.

**The two guards on every machine check.** *Non-vacuity*: the hypothesis of each obligation is shown satisfiable before the obligation is reported — for Theorem 1(b) that X lies strictly inside Y which lies strictly inside the box, on each of the three boxes; for Theorem 1(a), 1(c) and Theorem 4 the hypothesis is only that X (and a fibre) is non-empty; for Theorems 5 and 6 that a closed graph with S proper and h non-constant on S exists, on each box. *Encoding fidelity*: the Z3 formula for membership in ℛ, evaluated concretely on 3,087 cells drawn from random instances over four shapes, agrees with the operator under test in every case; that operator, on 300 further random instances over five shapes, agrees cell for cell with an independent implementation of D3 and D4 written from the definitions; and the three predicates of Theorems 5 and 6 — S closed, the graph of h closed, h a homomorphism on S — evaluated under 240 random assignments of (S, h) over the two boxes, agree with an enumerative decision in every case. An obligation is not reported if either guard fails.

**The negative controls.** Four deliberately false claims are stated in self-test mode and each is reported as refuted: that the periodic table's defect is 35; that a closed S forces a closed graph; that the fidelity guard passes a reference implementation with one cell deliberately added; and that the calendar recovers from a 5% random deletion. A green run is therefore evidence and not a restatement.

**What is not machine-checked, and why.** Every number in §3, §4 and §5 is a computation over a finite index, decided by enumeration and not of a shape a solver settles at any useful size: Λ₉ has 1,654 cells in a box of 27,648, three orders of magnitude beyond the boxes of §2. The redundancy figures are sampled by construction — the quantity is defined by random deletion — and no exhaustive version of them is claimed. The interpretation of the nuclide cells as pairing and clustering is a reading of computed cells and carries no status word. The containment law cited in §6 is not proved here and nothing here depends on it.

---

## References

- Allen, L. C. and Knight, E. T. (2002). The Löwdin challenge: origin of the n + l, n (Madelung) rule for filling the orbital configurations of the periodic table. *International Journal of Quantum Chemistry* **90**, 80–88.
- Baker, K. A. and Pixley, A. F. (1975). Polynomial interpolation and the Chinese remainder theorem for algebraic systems. *Mathematische Zeitschrift* **143**, 165–174.
- Batyrev, V. V. (1994). Dual polyhedra and mirror symmetry for Calabi–Yau hypersurfaces in toric varieties. *Journal of Algebraic Geometry* **3**, 493–535.
- Beeri, C., Fagin, R., Maier, D. and Yannakakis, M. (1983). On the desirability of acyclic database schemes. *Journal of the ACM* **30**, 479–513.
- Birkhoff, G. (1937). Rings of sets. *Duke Mathematical Journal* **3**, 443–454.
- Birkhoff, G. (1940). *Lattice Theory*. American Mathematical Society Colloquium Publications **25**, New York.
- Bohr, N. (1913). On the constitution of atoms and molecules. *Philosophical Magazine* **26**, 1–25.
- Candelas, P., de la Ossa, X., He, Y.-H. and Szendrői, B. (2008). Triadophilia: a special corner in the landscape. *Advances in Theoretical and Mathematical Physics* **12**, 429–473.
- Carathéodory, C. (1911). Über den Variabilitätsbereich der Fourierschen Konstanten von positiven harmonischen Funktionen. *Rendiconti del Circolo Matematico di Palermo* **32**, 193–217.
- Caspard, N. and Monjardet, B. (2003). The lattices of closure systems, closure operators, and implicational systems on a finite set: a survey. *Discrete Applied Mathematics* **127**, 241–269.
- Condon, E. U. and Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge University Press, Cambridge.
- Cowan, R. D. (1981). *The Theory of Atomic Structure and Spectra*. University of California Press, Berkeley.
- Deming, W. E. and Stephan, F. F. (1940). On a least squares adjustment of a sampled frequency table when the expected marginal totals are known. *Annals of Mathematical Statistics* **11**, 427–444.
- Deville, Y., Barette, O. and Van Hentenryck, P. (1999). Constraint satisfaction over connected row convex constraints. *Artificial Intelligence* **109**, 243–271.
- Freuder, E. C. (1978). Synthesizing constraint expressions. *Communications of the ACM* **21**, 958–966.
- Green, M. B., Schwarz, J. H. and Witten, E. (1987). *Superstring Theory, Volume 1: Introduction*. Cambridge University Press, Cambridge.
- Haberman, S. J. (1974). *The Analysis of Frequency Data*. University of Chicago Press, Chicago.
- Huang, W. J., Wang, M., Kondev, F. G., Audi, G. and Naimi, S. (2021). The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures. *Chinese Physics C* **45**, 030002.
- Hund, F. (1925). Zur Deutung verwickelter Spektren, insbesondere der Elemente Scandium bis Nickel. *Zeitschrift für Physik* **33**, 345–371.
- Ireland, C. T. and Kullback, S. (1968). Contingency tables with given marginals. *Biometrika* **55**, 179–188.
- Janet, C. (1928). *La classification hélicoïdale des éléments chimiques*. Imprimerie Départementale de l'Oise, Beauvais.
- Kondev, F. G., Wang, M., Huang, W. J., Naimi, S. and Audi, G. (2021). The NUBASE2020 evaluation of nuclear physics properties. *Chinese Physics C* **45**, 030001.
- Kramida, A., Ralchenko, Yu., Reader, J. and the NIST ASD Team (2024). *NIST Atomic Spectra Database*, version 5.12. National Institute of Standards and Technology, Gaithersburg. DOI 10.18434/T4W30F.
- Kreuzer, M. and Skarke, H. (2002). Complete classification of reflexive polyhedra in four dimensions. *Advances in Theoretical and Mathematical Physics* **4**, 1209–1230.
- Lach, M. (2026). *The Hierarchy Law of Mathematical Languages*. Manuscript.
- Laporte, O. (1924). Die Struktur des Eisenspektrums. *Zeitschrift für Physik* **23**, 135–175.
- Löwdin, P.-O. (1969). Some comments on the periodic system of the elements. *International Journal of Quantum Chemistry* **3** (S3A), 331–334.
- Mackworth, A. K. (1977). Consistency in networks of relations. *Artificial Intelligence* **8**, 99–118.
- Madelung, E. (1936). *Die mathematischen Hilfsmittel des Physikers*, 3rd edition. Springer, Berlin.
- Mendeleev, D. (1869). Über die Beziehungen der Eigenschaften zu den Atomgewichten der Elemente. *Zeitschrift für Chemie* **12**, 405–406.
- Montanari, U. (1974). Networks of constraints: fundamental properties and applications to picture processing. *Information Sciences* **7**, 95–132.
- Moore, E. H. (1910). *Introduction to a Form of General Analysis*. Yale University Press, New Haven.
- Pauli, W. (1925). Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren. *Zeitschrift für Physik* **31**, 765–783.
- Queyranne, M. and Tardella, F. (2006). Bimonotone linear inequalities and sublattices of Rⁿ. *Linear Algebra and its Applications* **413**, 100–120.
- Queyranne, M. and Tardella, F. (2008). Sublattices of product spaces: hulls, representations and counting. *Discrete Mathematics* **308**, 1508–1523.
- Russell, H. N. and Saunders, F. A. (1925). New regularities in the spectra of the alkaline earths. *Astrophysical Journal* **61**, 38–69.
- Scerri, E. R. (2016). *A Tale of Seven Scientists and a New Philosophy of Science*. Oxford University Press, Oxford.
- Schrijver, A. (1986). *Theory of Linear and Integer Programming*. Wiley, Chichester.
- Stoner, E. C. (1924). The distribution of electrons among atomic levels. *Philosophical Magazine* **48**, 719–736.
- Topkis, D. M. (1976). The structure of sublattices of the product of n lattices. *Pacific Journal of Mathematics* **65**, 525–532.
- Veinott, A. F., Jr. (1989). Representation of general and polyhedral subsemilattices and sublattices of product spaces. *Linear Algebra and its Applications* **114–115**, 681–704.
- von Weizsäcker, C. F. (1935). Zur Theorie der Kernmassen. *Zeitschrift für Physik* **96**, 431–458.
- Wang, M., Huang, W. J., Kondev, F. G., Audi, G. and Naimi, S. (2021). The AME 2020 atomic mass evaluation (II). Tables, graphs and references. *Chinese Physics C* **45**, 030003.
- Wigner, E. (1927). Einige Folgerungen aus der Schrödingerschen Theorie für die Termstrukturen. *Zeitschrift für Physik* **43**, 624–652.
