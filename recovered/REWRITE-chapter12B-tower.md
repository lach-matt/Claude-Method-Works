# Rewrite — "The tower — Λ₉ to Λ₁₃" (source §12.11 tower sections; prose revision, numbering left at source)

**Placement:** Part I — The Lattice. **Second of three reader chapters split from source Chapter 12** (shape; tower; time). This is the tower — the construction of the higher indices and what each coordinate costs. Draws on §12.11 intro, §12.11.0, §12.11.1 (axis table), §12.11.2 (excluded forms), §12.11.3/.3.1 (the dichotomy, law-vs-extent), §12.11.4 (path-dependence), §12.11.5 (the boundary), §12.11.6 (the false prediction), **and §12.11.8 (the electromagnetic index — relocated in as the chapter's final section per M's ruling; it was orphaned inside source Chapter 13 but is tower material by number and content)**. The time material (§12.11.0.1–.2, .7–.12) goes to the third chapter. **Numbering left at source values** (renumber-last). Per standing treatment: every result kept and stated with the confidence the workshop earned; the workshop itself (vocabulary-debt fixes, density re-derivations under variation, Q-item closures, "previously printed/withdrawn" self-corrections, register-250/434/230/325 self-audits) cut to the working record — where it also feeds the [MC-NN] compendium expansions. Proofs tokenized.

> **REVISION NOTE (this session):** the only change from the approved tower chapter is the inclusion of one new final section, **"The electromagnetic index was inside Λ all along"** (source §12.11.8), carrying three new owed expansions **[MC-36], [MC-37], [MC-38]**. All prose through [MC-26] is the approved text, unchanged. Source §12.11.7 "What the tower leaves open" was cut entirely to the working record (Q-item closures, self-duality self-audit, build-glyph mechanics, register-209, figure inventory) and is not carried here.

---

## The tower — Λ₉ to Λ₁₃

The ninth axis was added by analogy. Four more follow, and what they return is not five facts about five coordinates but one law, met five times, and a shape that survives it.

### The ninth axis makes transitions compose
Λ₈'s two ends are not the same shape. Its source is (n, ℓ, k, 2S) — four coordinates — and its target is (e, f, g) — three. A transition's output is therefore not a legal input, so **Λ₈ cannot be iterated**: no cascade, no sequence, no second step. The asymmetry is a missing spin.

The ninth axis supplies it. 2S′ ≤ g gives the target its own multiplicity, and the target end becomes (e, f, g, 2S′) under exactly the source's constraint forms — f ≤ e−1 against ℓ ≤ n−1, g ≤ 4f+2 against k ≤ 4ℓ+2, 2S′ ≤ g against 2S ≤ k. All 1,654 targets of Λ₉ are now legal sources. Define b ∘ a when a's target equals b's source; the composite runs a's source to b's target, transferring min(q_a, q_b) — no more than was taken, no more than arrives.

**Λ₉ is closed under composition, exhaustively — 41,682 composable pairs, zero failures** — and associative. It is therefore not merely a lattice of transitions but a **category** of them: composition is time, an order between cells rather than a stamp on one.

And Λ₉ is the *only* stage of the tower that composes. Composition needs the target's coordinate set matched by a source set of the same shape; every axis above the ninth attaches to one end or to the joint object, and the shapes part company:

| stage | target | source | composes |
|---|---|---|---|
| Λ₈ | (e, f, g) | (n, ℓ, k, 2S) | no — 3 against 4 |
| **Λ₉** | **(e, f, g, 2S′)** | **(n, ℓ, k, 2S)** | **yes — 41,682 pairs, 0 failures** |
| Λ₁₀ | (e, f, g, 2S′, v) | (n, ℓ, k, 2S) | no — no source seniority exists |
| Λ₁₁ | + 2J_c | + 2J_c on the source alone | no |
| Λ₁₂ | K binds core to orbit — joint | — | no — not an end coordinate |
| Λ₁₃ | 2J binds K to spin — joint | — | no |

So the tower carries **three gradings, not two**. The dichotomy below sorts the axes into counting and coupling — exact and envelope. Composability sorts them more strictly still: it is lost at axis 10, one step *before* exactness is, because v is a counting coordinate that closes exactly and yet has no source counterpart. An axis can be exact and not composable; none is composable and not exact. Λ₉ sits alone at the top of the stricter grading.

The ninth axis was added for seniority and arrived carrying this: an index gained a temporal structure as a side effect of a spectroscopic coordinate — the sharpest instance in this book of the thesis that surplus is what an index defends itself with. [MC-22]

![Figure 12.4](figures/figure-12.4.png)

*Figure 12.4. The constraint tree of the full tower: two caterpillars glued at k–q, counting axes rimmed dark (exact bounds), coupling axes in the accent (envelopes) — the dichotomy drawn — with the forbidden f···K bridge dashed and priced at the boundary below.*

### The axes, and what each one sees

| axis | coordinate | bound | cells | density | what it distinguishes |
|---|---|---|---|---|---|
| 9 | 2S′ | 2S′ ≤ g | 1,654 | 63.7% | the target's multiplicity |
| 10 | v | 2S′ ≤ v ≤ g | 2,535 | 44.7% | pairing depth — seniority |
| 11 | 2J_c | 2J_c ≤ φ̂(k) | 13,585 | 17.0% | the core's fine structure |
| 12 | K | 2K ≤ 2J_c + 2f_max | 70,905 | 31.4% | core–orbit orientation |
| 13 | 2J | \|2J − 2K\| ≤ 1 | 199,130 | 64.4% | the outer electron's spin bit |

Every bound is admissible; every stage is closed — verified exhaustively against every cell of its ambient box, not merely sampled — and every stage projects exactly onto the one below. Each coordinate is a physical degree of freedom no function of the coordinates below it can express, which is the condition every legitimate axis must satisfy. And Λ₉ is not the tightest object the language allows: a tighter spin bound closes at 1,561 cells but only by giving the constraint graph its first cycle, so the choice is **the tree or the tightness** — the language offers both only up to 1,561 against 1,654 cells. [MC-23]

### Three excluded forms, and the fold has a name
Two constraint forms were already excluded — sums and differences. The tower requires excluding a third: **symmetric bounds**. The exact ceiling of every coupling axis is symmetric under particle-hole conjugation, terms(ℓᵏ) = terms(ℓ^(4ℓ+2−k)) — verified exactly for every k on the p and d shells — and a symmetric non-constant function is not monotone, so the admissible form cannot carry it.

The envelope gap decomposes into three distinct machines: the **reflection** (particle-hole conjugation), the **congruence** (fermion parity), and the **triangle** (coupling additivity — one sum and one difference, the two earlier exclusions wearing physics). No coupling axis escapes all three. One half of the triangle survives — the region |2L−2S| ≤ 2J ≤ 2L+2S is join-closed and meet-broken at every cap, certainty surviving upward and dying downward — which is the object's skew stated as an inequality. [MC-24]

### The dichotomy
> Counting coordinates close exactly. Coupling coordinates close as envelopes. There is no third kind in this object.

The origins table has four rows. Pauli, the hydrogenic solution, and counting give single-coordinate exact bounds — which is why E(Λ) = 0 was available at all. Vector coupling gives envelopes, provably and permanently, because its exact form is made of the three excluded shapes. **The price of certainty is not paid once at the door; it is paid per coupling axis.**

And the surplus is not waste. Every envelope cell is a tripwire: a measured term assigned a nonphysical coupling pair lands in the gap and is caught before any energy is read. The price of certainty and the budget of self-defence are the same cells, counted twice.

### A bound from the law, or a bound from the extent
The dichotomy has a sharper form, and it is the deepest statement in the chapter. Sort the thirteen bounds by *where each is taken from*:

Axes 9 and 10 take their bounds from laws that exist independently of Λ — vector coupling, seniority. Axis 11 takes its bound from Λ itself: 2J_c ≤ φ̂(k), where φ̂ is the envelope of the largest fine-structure actually realised at each occupancy. It is not derived; it is observed — φ̂ = {1:3, 2:4, 3:5}, which are exactly the maxima the set exhibits, because φ̂ *is* the envelope of the set's own extent.

> A bound taken from the law closes exactly. A bound taken from the extent closes only to an envelope.

That is why exactness is lost at the eleventh axis and not before it. And it says what E(X) measures. The reconstruction ℛ builds its bounds from a set's own projections — it is an extent-bound operator throughout. So **E(X) = |ℛ(X)| − |X| is the price of describing a set by its extent rather than by its law**: the count of what the pattern admits and the law does not. E(X) = 0 says the two coincide — the extent *is* the law for that set, which is self-reference stated as arithmetic rather than as a property. [MC-25]

### Precision is path-dependent; physics is not
The exact J-set of a channel is the same whether J is reached through K or directly — recoupling holds, 12 of 12 pairs. But the envelopes differ: 64.4% through K, 39.4% direct. The envelope does not commute with recoupling. **The index remembers the route; the atom does not.**

### The shape survives, and it has a boundary
Every stage of the tower still factorises exactly over the transfer — log-concave, unimodal, peak at q = 2, with the sectioned count equal to the direct count at zero defect — so the object is still a cylinder, because every coupling axis hangs off one side of the tree. The mean transfer rises, ⟨q⟩ = 1.4631 → 1.887, as coupling multiplicity re-weights the profile.

The boundary is one specific bound. The exact law for K is 2K ≤ 2J_c + 2f with f the cell's own — a bound with **two parents**, one on each side of the cylinder. That is the first bridge between the cylinder's two ends other than q, and it breaks the factorisation by 15,150 cells at Λ₁₂ and 45,450 at Λ₁₃ — 21.4% and 22.8% of the product. The book takes the one-parent form instead, 2K ≤ 2J_c + 2f_max with f_max the cap, which preserves the tree and the cylinder at the cost of admitting, for the cells below the cap, a little more than the law does.

> The tree is the cylinder; tightening K is the move that spends it. The title of this book is a property of envelope precision.

![Figure 12.5](figures/figure-12.5.png)

*Figure 12.5. The solid in silhouette: plan (parent) and side (target) views, Λ₁₃ filled against Λ₈ dashed. The parent side thins toward q = 3 while the target thickens — the transfer trade, seen as shape, at both scales of the tower.*

### An index whose one prediction is false, and why that is a result
The E1 selection rule on (2J, 2J′), |Δ2J| ≤ 2, is a closed index. Remove the one transition nature forbids — J = 0 ↛ 0 — and closure fails by exactly four meets at every cap, all four the same forbidden cell: (0,1) ∧ (1,0) = (0,0). The defect is E = 1, and the one cell the reconstruction restores is the one the atom vetoes — the photon's unit of angular momentum, with the parity half of the rule a congruence that breaks joins, the photon's odd parity.

This is the calibration the book owes its reader on what E measures: **E(X) counts proposals, not guarantees.** Here is an index whose single proposal is known false, vetoed by structure the index does not carry. That is not a failure of the method — it is the method reporting, precisely, the one thing it cannot see, and naming what would have to be added to see it. [MC-26]
