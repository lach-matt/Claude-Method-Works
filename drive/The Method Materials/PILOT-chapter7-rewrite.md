# Pilot rewrite — Chapter 7, "The construction of Λ"

**What this is.** A single chapter rewritten for a skeptical expert reader, set beside the original so you can verify that the substance is untouched. Every equation, constraint, number, and section-reference in the original is preserved. What is added is the connective explanation — expansions of shorthand, definitions of coined terms at first use, and the *reasons* the original states only by allusion. Nothing quantitative is restated in different terms.

**A note on what I did and did not change.** The eight coordinates, the seven constraints and their four origins, the closure proof, the counts (216, 976, 1,636, 2,394), the densities and caps, and every §-reference are carried verbatim. Where the original writes `ℛ`, `E(Λ) = 0`, "the tower," or "three results follow," I expanded these using the book's *own* definitions (§ references given), not my own gloss.

---

## ORIGINAL

> ## 7. The construction of Λ
> Λ is a set of eight-tuples. Each is a transition cell: a source configuration, a target configuration, and the electron count moved between them.
>
>      (n, ℓ, k, q, e, f, g, 2S)
>
> | n | source shell | ℓ | source subshell | k | source occupancy | q | electrons removed | e | target shell | f | target subshell | g | target occupancy | 2S | multiplicity |
>
> Five further coordinates — 2S′, v, 2J_c, K and 2J — extend Λ₈ to Λ₁₃ when target spin, seniority and angular-momentum coupling are carried explicitly; §12.11 builds the tower and fixes the order, which is J_c, then K, then J. Everything in this book that does not concern coupling is stated for Λ₈.
>
> One row of the table below is not like the others. Three origins — Pauli, the hydrogenic solution, counting — yield exact constraints. The fourth, vector coupling, yields an envelope: 2S ≤ k contains every physical multiplicity and admits values no k electrons can carry, at 48.5% density at the caps of §7.4. §12.11.3 states the dichotomy and §12.11.2 proves it is forced.
>
> ### 7.1 The constraints, and where each comes from
> Λ is not all of the eight-fold product. It is the subset satisfying: [ℓ≤n−1 hydrogenic; k≤2(2ℓ+1) Pauli; q≤k counting; f≤e−1 hydrogenic; g≤2(2f+1) Pauli; g≤q counting; 2S≤k vector coupling]. **Seven constraints, four origins, and nothing else.** … it is the reason the object's properties can be attributed to *indexing* rather than to physics smuggled in through a bound.
>
> ### 7.2 Every constraint is of one form
> Each constraint reads xᵢ ≤ φ(xⱼ) — one coordinate bounded by a monotone function of one other. None is a sum. None is a difference. … a set cut out by a sum bound is not closed. **Consequence, developed in Chapter 8:** the graph whose nodes are coordinates and whose edges are constraints is a **tree**.
>
> Figure 7.1. … Eight nodes, seven edges, connected — a tree, and therefore treewidth 1. Three results in this book follow from that fact alone.
>
> ### 7.3 Λ is closed
> For any two cells x, y ∈ Λ, both x ∨ y and x ∧ y … are again in Λ. *Proof.* Each constraint is xᵢ ≤ φ(xⱼ) with φ non-decreasing. … Meets are symmetric. ∎ And E(Λ) = 0, verified by direct computation at four cap settings — 216, 976, 1,636 and 2,394 cells — exact in one step and stable under a second application of ℛ.
>
> ### 7.4 A note on caps
> Λ is infinite; every count in this book is stated at explicit caps on n, e, ℓ and k. The counts change with the caps. The shape does not …

---

## REWRITTEN

## 7. The construction of Λ

The object this book is about, written Λ, is a set. Its members are not atoms, or states, or energy levels — they are *transitions*. A single member records one allowed move of electrons: a starting electron configuration, an ending configuration, and how many electrons made the move. Each such member is called a **cell**, and every cell is a list of eight numbers:

      (n, ℓ, k, q, e, f, g, 2S)

The eight entries split into three groups. The first three describe where the transition starts, the next describe how many electrons leave and where they land, and the last records a spin property of the result:

| coordinate | meaning |
|---|---|
| *n* | source shell (principal quantum number of the starting subshell) |
| ℓ | source subshell (its orbital angular momentum) |
| *k* | source occupancy (how many electrons occupy that starting subshell) |
| *q* | electrons removed (how many leave in the transition) |
| *e* | target shell |
| *f* | target subshell |
| *g* | target occupancy (how many electrons arrive) |
| 2*S* | multiplicity (twice the total spin of the target, kept as an integer) |

A skeptic will immediately ask two things: why *eight* numbers, and why *these* eight. The answer to the first is that eight is the smallest set that fixes a transition unambiguously once spin coupling is set aside; the answer to the second is the subject of §7.1, and it is the crux of the whole construction — every one of the eight is bounded by a physical law, and by nothing else.

Eight coordinates suffice only as long as the finer structure of angular momentum is not carried explicitly. When it must be — when target spin, seniority (a label distinguishing states of the same configuration and spin), and the coupling of angular momenta are tracked — five further coordinates are adjoined: 2S′, v, 2J_c, K and 2J. This extends the eight-coordinate object, written **Λ₈**, to a thirteen-coordinate object, **Λ₁₃**. The sequence of objects between them (Λ₈, Λ₉, …, Λ₁₃) is what the book calls **the tower**; §12.11 builds it and fixes the order in which the coupling coordinates are adjoined — first J_c (the core's angular momentum), then K (the intermediate coupling), then J (the total). This chapter, and everything in the book that does not concern angular-momentum coupling, is stated for the base object Λ₈. Where "Λ" appears without a subscript, Λ₈ is meant.

One feature of the construction has to be pointed out before the constraints are listed, because it is the single place where the object is not exact. Of the four physical origins that will bound the coordinates, three — the Pauli exclusion principle, the hydrogenic radial solution, and plain counting — give *exact* bounds: a coordinate either can or cannot take a value, with no slack. The fourth, angular-momentum (vector) coupling, does not. The bound it supplies, 2S ≤ k, is an **envelope**: it contains every multiplicity that k electrons can physically carry, but it also admits some values that no arrangement of k electrons actually realises. Measured at the counting caps defined in §7.4, this envelope is satisfied by 48.5% of the cells it nominally allows — that is, fewer than half of the spin values it permits are physically attainable. This is not a defect to be hidden; it is a structural fact with consequences, and the book confronts it directly: §12.11.3 states the exact-versus-envelope dichotomy and §12.11.2 proves the envelope is forced — that no exact bound of the required form exists for spin.

### 7.1 The constraints, and where each comes from

Λ is not the full set of all possible eight-tuples. If it were, it would contain physically impossible transitions. It is instead the subset of the eight-fold product that satisfies seven inequalities, each traceable to one physical origin:

|  | constraint | origin |
|---|---|---|
| 1 | ℓ ≤ n − 1 | hydrogenic radial solution |
| 2 | k ≤ 2(2ℓ + 1) | Pauli exclusion |
| 3 | q ≤ k | counting — cannot remove more electrons than are present |
| 4 | f ≤ e − 1 | hydrogenic radial solution |
| 5 | g ≤ 2(2f + 1) | Pauli exclusion |
| 6 | g ≤ q | counting — cannot place more electrons than were removed |
| 7 | 2S ≤ k | vector coupling |

Constraints 1 and 4 say a subshell's angular momentum cannot reach its shell number — a fact of the hydrogen solution. Constraints 2 and 5 are the Pauli limit on how many electrons a subshell holds, 2(2ℓ+1). Constraints 3 and 6 are bookkeeping: you cannot remove more than are there, nor deposit more than you removed. Constraint 7 is the spin envelope discussed above.

**Seven constraints, four origins, and nothing else.** This exhaustiveness is the load-bearing claim of the chapter, and it should be read as a claim, open to challenge: no constraint defining Λ comes from anywhere but Pauli, the hydrogenic radial solution, counting, or angular-momentum coupling. There is no adjustable parameter, no empirical cutoff, no term inserted to make the object come out a particular way. The reason this matters is not aesthetic. It is what licenses the argument of Part III, where properties of Λ are attributed to the fact that it is a well-formed *index* rather than to physics quietly imported through the back door of a bound. If any constraint had a fifth origin — a fitted number, say — that argument would collapse, because one could no longer tell whether a property of Λ was a property of indexing or an artefact of the smuggled physics.

### 7.2 Every constraint is of one form

Look again at the seven constraints. Every one has the identical shape:

      xᵢ ≤ φ(xⱼ)

— a single coordinate bounded above by a function of a *single* other coordinate, and that function is monotone (non-decreasing). Not one constraint is a sum of coordinates; not one is a difference. This uniformity is not a matter of how the constraints happen to be written down. Chapter 17 shows it is forced: a set carved out by a bound that added two coordinates together would fail to be closed in the sense made precise in §7.3, and closure is non-negotiable for what follows.

The uniformity has an immediate structural consequence, developed fully in Chapter 8. Draw a graph whose nodes are the eight coordinates and whose edges join two coordinates whenever a constraint binds one to the other. Because every constraint links exactly one coordinate to one other, this graph is a **tree** — connected, with no cycles.

![Figure 7.1](figures/figure-7.1.png)

Figure 7.1. Each of the seven constraints binds one coordinate to one other. The result is eight nodes joined by seven edges, connected and acyclic: a tree. A tree has **treewidth 1** — the lowest possible non-trivial value of the graph-complexity measure that governs how hard it is to reason over the object. Three results later in the book follow from this single fact, and it is worth naming them now so the reader knows the tree is doing real work rather than decorating the page. They are (all developed in Chapter 8): first, **the void needs no sieve** — a tree has no cycles, so counting the cells requires no inclusion–exclusion correction, and Chapter 10 gives a closed-form count; second, **the coordinate order is recoverable** — the orders on the eight coordinates can be reconstructed from an unlabelled collection of cells by propagating along the tree, demonstrated at 20 of 20 in Chapter 15; and third, **the constraint graph offers no redundancy** — there is exactly one path between any two nodes, so the two-independent-route protection the object uses to defend itself (Chapter 16) cannot come from the constraints and must come from derived quantities instead. The third is a genuine restriction on how the object can be built, visible three chapters before it is needed.

### 7.3 Λ is closed

The property everything above has been pointing at is **closure**. Take any two cells x and y in Λ. Form two new cells: their coordinatewise maximum x ∨ y (take, in each of the eight positions, the larger of the two values) and their coordinatewise minimum x ∧ y. The claim is that both of these are again cells of Λ — the object is closed under these two operations.

*Proof.* It suffices to check that x ∨ y satisfies each constraint; meets are identical by symmetry. Every constraint has the form xᵢ ≤ φ(xⱼ) with φ non-decreasing. Consider any constraint, and suppose the i-th coordinate of x ∨ y is inherited from x, i.e. (x∨y)ᵢ = xᵢ. Then

    (x∨y)ᵢ = xᵢ ≤ φ(xⱼ) ≤ φ(max(xⱼ, yⱼ)) = φ((x∨y)ⱼ)

The first inequality holds because x itself is in Λ; the second because φ is non-decreasing and max(xⱼ, yⱼ) ≥ xⱼ. So the constraint survives. If instead the i-th coordinate came from y, the same argument runs with y in place of x. Every constraint holds for x ∨ y, so x ∨ y ∈ Λ. Meets are symmetric. ∎

Closure is exactly the condition that makes Λ a *lattice*, and it is the technical hinge on which Part III turns.

There is a second, computational way to say the same thing, and it is the sense in which the book most often uses closure. Define ℛ(X), the **reconstruction** of a set of cells X, to be everything that X's own coordinatewise bounds imply must also be present — the closure of X under the max/min operations, built from X's own projections and nothing external. (ℛ is defined precisely in §11 / Appendix A; the point here is that no outside knowledge enters — ℛ(X) is what a reader could rebuild from the cells alone.) Then define

      E(X) = |ℛ(X)| − |X|

the count of cells the structure implies but that are missing from X — the gap between what X's own bounds demand and what X actually contains. A set is closed exactly when E(X) = 0: nothing is implied that is not already present.

For Λ, **E(Λ) = 0**, verified not by the proof alone but by direct computation at four different counting-cap settings, where Λ has 216, 976, 1,636 and 2,394 cells respectively. At each, the reconstruction adds nothing (E = 0), the result is reached in a single application of ℛ, and it is stable under a second application — ℛ(ℛ(Λ)) = ℛ(Λ) — confirming Λ is a genuine fixed point of the reconstruction, not merely closed by coincidence at one size.

### 7.4 A note on caps

Λ as defined is infinite: n and e range over all shells without limit. Every *count* in this book is therefore stated at explicit finite caps on n, e, ℓ and k — the four numbers 216, 976, 1,636 and 2,394 above are four such cap settings. The counts depend on the caps and change with them; wherever a number is cap-dependent it is marked as such. The *shape*, however, does not depend on the caps — a claim made precise in Chapter 8, where the pattern generating the cells is shown to be identical across a twenty-eight-fold range in total cell count. Every structural claim in the book has been checked at no fewer than four cap settings, so that no property rests on an accident of where the counting happened to stop.
