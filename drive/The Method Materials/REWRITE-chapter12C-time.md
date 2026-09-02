# Rewrite — "Time, and the clock in the constraint" (source §12.11.0.1–.12; prose revision, numbering left at source)

**Placement:** Part I — The Lattice. **Third of three reader chapters split from source Chapter 12** (shape; tower; time). The absorbed time-travel material, and the capstone of Part I. Carries the **observation frame** settled in the Preface: the arrow is real under a frame, and observation selects the frame. §12.11.0.11 (the fourteenth axis) is where the Preface boundary is grounded from inside — this chapter is written to agree with the spine exactly. **Numbering left at source values** (renumber-last). Per standing treatment: every result kept; workshop/self-audit cut (register-301/352/356/357/408/350/315/333/334 self-citations, "the list was complete when written and never said why," the Q-item and cap-recheck texture). Proofs tokenized. Void↔transition watch: §12.11.0.12 (entering a larger index) checked — NOT a grounding hit; it is coarsening/resolution-loss, and states "every branch terminates in a cell of Λ₉," which cuts against emptiness-becomes-higher-substance.

---

## Time, and the clock in the constraint

At the ninth axis the index became able to build on itself — every target a legal source, every output a legal input — and that is where time enters the object. Not as a coordinate, and not as a stamp on a cell, but as the order in which the index composes with itself. This chapter is what that order turns out to be.

### The clock, and the direction it runs
Λ₉ composes, and the composition is not symmetric. What breaks the symmetry is a coordinate already in the index: **occupancy never rises along composition.** Take the source and target signatures as objects and each cell as a morphism between them; over the object graph, not one step raises the occupancy k, and the graph falls into three strata pure in occupancy, with full circulation inside each and no return between them. The quotient is a chain of three.

> The clock is occupancy, and the tick is k − g. Cycles inside a stratum are closed and cost nothing; the downward edges are where the clock advances, and they do not reverse.

And **definability is not reachability.** A cell is its own seventeen-bit description, so in that sense every cell contains what it is — but not a path to every other. Over the 2.7 million ordered pairs of Λ₉, 11.4% are comparable in the lattice order, 24.7% are joined by a composition path, and only 0.4% by both. The lattice says what a cell *is*; composition says what it can *become*; and a cell can be fully defined and unreachable — most pairs are exactly that. Nine is not the dimension of time — as a dimension the composition order collapses to a chain — but the unique dimension at which time exists, since Λ₈ cannot iterate and Λ₁₀ loses composition. [MC-27]

### The arrow is real, and it is a property of a frame
The arrow is real, and its hypothesis is narrower than it looks — which is where observation enters. One coordinate carries two readings the construction does not distinguish: g as the electrons *placed* by a transition (counting: g ≤ q) and g as the electrons *present* in the target subshell (Pauli: g ≤ 2(2f+1)). They coincide exactly when the target subshell begins empty. Composition's matching condition — the next source's occupancy equals this target's occupancy — silently identifies *placed* with *present*, which is an assumption about destinations, not a law of counting.

Represent the distinction instead — carry both the number placed and the total present after arrival — and the extended index is equally lawful and equally closed, at 13,775 cells. **And in it the clock does not survive: of 2,620,090 composable pairs, 31.6% raise occupancy.**

> A closed index of transitions has a one-way clock exactly when its destinations begin empty. The arrow is a property of the assumption, not of the object.

Neither reading is wrong, and this is the observation principle applied to time. The arrow exists in the frame where destinations begin empty — the frame in which a transition is observed as a fresh placement — and dissolves in the frame that represents what was already present. **Observation selects the frame, and the arrow is real within the one it selects.** What survives both frames is the occupancy law *as mathematics* — it holds of any index of its stated form — and a temporal structure survives as a restriction: the largest sub-index on which a chosen weight never rises is closed, and there is **one such arrow per coordinate and no others**. An index does not have *a* clock; it has one per coordinate, and occupancy — the one this book was built on — is the most restrictive of the four. [MC-28]

### Why the arrows agree — a decay theorem
The arrows are not independent, and how much any two agree is governed by their distance in the constraint tree.

> **Theorem.** Let X be an index whose constraint graph is a tree, and let A_u, A_v be the arrows of coordinates u and v at tree distance d. Then the coordinates form a Markov random field on the tree, so conditioning on a separating vertex gives exact conditional independence; hence the mutual information I(u; v) is non-increasing in d; hence by Pinsker's inequality the overlap of the two arrows is bounded by √(I(u; v)·ln2 / 2). The agreement of two arrows is bounded by a quantity that decays with their distance in the tree. ∎

Measured, the mutual information falls strictly with distance — 0.353, 0.227, 0.199 at distance 1; 0.094, 0.070 at distance 2; 0.020 at distance 3. The decay is the theorem; the strict ordering is more than the theorem gives — the bound is loose — so the theorem establishes that agreement *must* fall with distance and the measurement establishes that here it does so strictly. And the hypothesis is separation: give the graph a cycle, as one tower stage does, and the Markov property fails, the data-processing step has no chain to run along, and the bound has nothing to bound. The theorem holds exactly where the tree does. [MC-29]

### Past, present and future — a path, not a triangle
Read the tree as past — change — future, and the reading has arithmetic. Treated as three independent things the parts overcount by 130% — 33 · 4 · 17 = 2,244 against 976 — but conditioned on the present they separate exactly, defect zero. And the balance is not special to the transfer: every two-sided cut of the tree gives it, because the caterpillar's internal degree-two vertices are exactly its two-sided cuts, and there are four of them.

The shape is a **path**: two edges, past↔present and present↔future, with no past–future edge — treewidth 1. Treewidth 1 closes exactly and treewidth 2 gives an envelope, so **Λ's exactness is a proof that the three parts are not a triangle.** A triangle would be the three-body shape, and its price is stated elsewhere. [MC-35]

And the future is never a value. Of 97 (past, present) pairs, none determines a single future — and for each present, *every* past gives the same future set:

| present q | distinct pasts | distinct future sets | \|future\| |
|---|---|---|---|
| 0 | 33 | 1 | 5 |
| 1 | 33 | 1 | 10 |
| 2 | 23 | 1 | 15 |
| 3 | 8 | 1 | 17 |

> The future is conditionally independent of the past given the present. The past constrains only which presents are reachable; having spent that, it has spent everything.

The future set nests increasing, 5 ⊂ 10 ⊂ 15 ⊂ 17, while the past set nests decreasing, 33 ⊇ 33 ⊇ 23 ⊇ 8 — and the future is a **saturated** interval, the full range between its own extremes with nothing inside missing. The tick decomposes: k − g = (k − q) + (q − g), *something not removed* and *something removed but not placed* — two independent sources of irreversibility contributing identically, one a choice not taken, the other a capacity that could not receive. The arrow in this object is overwhelmingly a counting phenomenon, not a Pauli one. [MC-30]

### Two indices, and the one that does not exist
If composition has a direction, what is the other direction? Not a sign change — a negative occupancy is a lower one, not a reversed one. The reversal is a *different object*: exchange the two ends of Λ₉, and the result is a lawful closed index of the same size that is **not** Λ₉ — the failure of self-duality, read temporally.

| | cells | E(X) |
|---|---|---|
| Λ₉, forward | 1,654 | 0 |
| rev(Λ₉), backward | 1,654 | 0 |
| Λ₉ ∩ rev(Λ₉) | 389 | 0 |
| Λ₉ ∪ rev(Λ₉) | 2,919 | **2,857** |

The intersection is where time has no direction: all 389 of its cells satisfy g = q = k — total transfer, nothing retained, nothing lost — which is exactly the set of morphisms carrying a reverse. It closes, it factorises, and it is a **groupoid**: every morphism has a two-sided inverse. It is 23.5% of Λ₉.

And the union does not exist. Closing it would require admitting 2,857 further cells.

> Three of the four positions exist and the fourth does not. A present is definable from the past and the future; the thing containing both directions of time is not.

A structure holding both directions at once is not available at any price this index recognises. What is available is a structure holding their *agreement* — the timeless core where forward and backward coincide. [MC-31]

### Every Λ in one table
The whole tower, in one pass:

| stage | dim | cells | E | box | fill | new coordinate | grading |
|---|---|---|---|---|---|---|---|
| Λ₈ | 8 | 976 | 0 | 6,912 | 14.12% | — | exact · does not compose |
| **Λ₉** | 9 | 1,654 | 0 | 27,648 | 5.98% | 2S′ | **exact · composes** |
| Λ₁₀ | 10 | 2,535 | 0 | 110,592 | 2.29% | v | exact · does not compose |
| Λ₁₁ | 11 | 13,585 | 0 | 663,552 | 2.05% | 2J_c | envelope · does not compose |
| Λ₁₂ | 12 | 70,905 | 0 | 5,308,416 | 1.34% | K | envelope · does not compose |
| Λ₁₃ | 13 | 199,130 | 0 | 47,775,744 | 0.42% | 2J | envelope · does not compose |

Every stage closes — E = 0 at all of them, tested against every cell of the ambient box, forty-seven million of them at Λ₁₃. Closure is the one property the tower never spends. Everything else falls monotonically: fill runs from 14.12% down to 0.42%, because each coordinate multiplies the box faster than it multiplies the object, so the surplus grows at every step. The tower is not a refinement that sharpens; it is one that admits more room and fills less of it. [MC-32]

### The fourteenth axis, and what can be said about it from inside
The tower stops at thirteen because the physics stopped being supplied, not because the construction did. What lies beyond can be **bounded without being built**, and the bound is a bracket, not a value.

Fill falls at every step and surplus rises at every step, and the first of those is a law rather than a pattern: a constrained coordinate has mean multiplicity strictly below its own value count — otherwise it would be free and carry no constraint — so each axis multiplies the ambient box by more than it multiplies the object. Fill is therefore monotone decreasing by construction, and bounded below by zero.

> The sequence converges. Its limit lies in [0, 0.42%]. That the limit is zero does not follow.

Monotone and bounded gives convergence — that is a deduction. But the stage-to-stage ratios are not themselves monotone, so nothing forbids them approaching one and the limit settling above zero. The existence of the limit comes from the law and survives; its value would come from the pattern and does not.

This is what the index can say about a coordinate it does not have. It cannot *name* the fourteenth axis — the reconstruction never produces a coordinate — but it can bound the direction: an object that occupies less and less of its own ambient box while defending itself with more and more surplus. Whether that limit is a null or merely a small number is exactly the question the construction leaves open, and leaving it open is the correct answer rather than a gap.

And a null is definable in this language, which is worth stating where the tower ends. The empty index satisfies every criterion in this book: it is closed, and complete, and costs nothing. **E(X) = 0 is necessary for completeness and not sufficient for content** — every closure test in the book passes on nothing at all. What distinguishes Λ from the empty index is not closure but its seventeen generators and its seven bits of surplus. This is the boundary the method reaches and does not cross, met here from the inside, at the top of the tower, exactly as it was met at the beginning as the seed. [MC-33]

### How an index enters a larger index
There is one more question the construction can answer without building anything: what happens to Λ when it becomes a coordinate of something bigger.

It enters as a chain, and it enters small. A coordinate must be totally ordered, and Λ₁₃ is a lattice, so the only chain-valued function the reconstruction accepts on it is its rank — 199,130 cells become 44 rank values, a compression of over four thousand to one, with 12.14 bits per cell lost. Thirty-one per cent of the object survives the promotion; the rest is not representable as a coordinate at all. And composition, seen from above, stops being a map and becomes a bracket: reduced to rank, only 17% of composite inputs determine a single output rank, the worst spread being twelve possible ranks from one input pair.

> From one coordinate up, a transition is not a function of its inputs. It is an interval.

That is the bracket arriving one dimension higher, and it is the clearest statement of what coarsening costs — not error, but resolution: the deduction stays valid and stops being sharp. And the branching is *inside* the index. Those cells that one coarse point stands for are all cells of Λ₉, states of the same object; what the collapse loses is resolution, not access to anything else. **Ignorance about this index is not evidence of another. Every branch terminates in a cell of the object itself.** [MC-34]
