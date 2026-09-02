# Rewrite — Chapter 4 (was Chapter 6), "The periodic table is not a closed index"

**Placement:** opens **Part I — The Lattice**. First subject-matter chapter. Figures 6.1/6.2 → 4.1/4.2; sections §6.x → §4.x. **Calibration:** subject-matter forward, per the settled Preface (the method is the protagonist; results are its payoff). Self-correction commentary ("the book previously said X, now Y") is cut to the workshop record per the standing rule; every result is kept and stated as a clean finding. The §4.2 time passage carries the observation-frame reading settled in the Preface. Numbers, §-refs, and register citations preserved.

---

## 4. The periodic table is not a closed index

Take the periodic table at its word. Its coordinates are period and group; its cells are the elements. Ask what those coordinates, and the occupied cells alone, imply about which other cells could exist.

The answer is thirty-six cells that do not.

| | |
|---|---|
| main-table cells (lanthanides and actinides set aside) | 90 |
| cells the structure admits | 126 |
| **external definition cost E(X)** | **36** |

The thirty-six are (p1, g2) through (p1, g17), (p2, g3) through (p2, g12), and (p3, g3) through (p3, g12) — **the gaps in the short periods, every one of them.**

This is not a defect in the periodic table. It is a fact about what the periodic table's coordinates can and cannot carry. Period and group locate an element; they do not encode why period 1 has room for two elements and period 4 for eighteen. That information travels alongside the table, in the schooling of whoever reads it.

### 4.1 What "the structure admits" means
The reconstruction is mechanical. Given a set of cells X on coordinates (x₁, …, x_d), read off two things: the **value sets** Âᵢ(X) = { xᵢ : x ∈ X } — which values occur — and the **bounds** φ̂ᵢⱼ(v) = max{ xᵢ : x ∈ X, xⱼ ≤ v } — how far one coordinate reaches given another. Then form

    ℛ(X) = { x ∈ ∏ Âᵢ(X) : xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j }

No outside knowledge enters. ℛ(X) is what a reader could reconstruct from the cells alone, and

    E(X) = |ℛ(X)| − |X|

is the gap: cells the structure implies and the index denies. For the periodic table it is 36. For Λ, built in the next chapter, it is 0.

![Figure 4.1](figures/figure-4.1.png)

*Figure 4.1. The external definition cost of seven indices. Four are self-defining. The calendar's seven cells are the content of "Thirty days hath September"; the periodic table's thirty-six are the gaps in the short periods.*

![Figure 4.2](figures/figure-4.2.png)

*Figure 4.2. Blue: the ninety cells the table holds. Red: the thirty-six its own coordinates admit and it denies. A reader given only the occupied cells would reconstruct all one hundred and twenty-six.*

### 4.1.1 A known layout costs nothing
E is a property of a layout, not of chemistry. On the drawn eighteen-column table with all 118 elements, the thirty-six decompose into two kinds — and the split turns on where helium is drawn:

| the thirty-six | count |
|---|---|
| forbidden by ℓ ≤ n−1 — 1d (10), 1p (5), 2d (10) | **25** |
| deferred by the Madelung order — 3d (10), and period 1 group 2 | **11** |

The 1p block contributes five and not six because helium occupies group 18 itself, and the slot helium vacates — period 1, group 2 — is a *deferred* cell rather than a forbidden one, since ℓ = 0 there satisfies ℓ ≤ n−1. Two constraints cast a shadow of twenty-five, and eleven further cells could hold an element and do not.

**E is not a property of the elements. It is a property of where helium is drawn.**

| helium at | cells | E |
|---|---|---|
| group 18 | 90 | **36** |
| group 2 | 90 | **20** |

The mechanism is the envelope: φ̂(group | period ≤ 1) is 18 when helium sits at group 18 and 2 when it sits at group 2, so the entire first row of gaps exists only under the standard placement. Helium's position is the most argued question in periodic-table design — IUPAC places it at 18; the left-step form and a quantum-chemical case place it at 2, at the cost of the atomic-number triad He(2), Ne(10), Ar(18). E measures what that choice costs to specify, and the difference is sixteen cells. Register 448.

| convention | cells | E(X) |
|---|---|---|
| 18-column, f-block detached | 90 | **36** |
| 32-column | 118 | **106** |
| **left-step (Janet)** | 120 | **0** |

**The Janet left-step table is closed.** Order the blocks f, d, p, s and define the period by *n* + ℓ, and the same elements cost nothing to specify. The thirty-six belong to the drawing that hangs in classrooms; a known alternative costs none — exactly as §4.3 shows for the calendar, where E = 7 is the price of keeping January first.

One caution. E(periodic table) = 36 carries no independent defence: the order and geometry routes to it are one computation written twice, because the table has no separately stated constraints to check the recovered ones against. Only Λ's E = 0 is defended, and only because Λ's constraints are given in §5.1 before any cell is enumerated.

### 4.2 It is not a peculiarity of chemistry
The same computation on other indices:

| index | \|X\| | E(X) | self-defining |
|---|---|---|---|
| a box ordering, l ≥ w ≥ h | 56 | 0 | yes |
| the drawn nuclide band, between drip lines | 383 | 0 | yes |
| a chessboard | 64 | 0 | yes |
| Λ | 976 | 0 | yes |
| a subnet with a hole | 248 | 8 | no |
| the calendar, (month, day) | 365 | 7 | no |
| the periodic table | 90 | 36 | no |

A chart drawn between two monotone drip lines has E = 0, and it has E = 0 necessarily: ℛ is idempotent (§32.4.1), so a drawn band's closure is a theorem, not a finding about nuclei. The measurement is the other object. Taking the particle-bound nuclides themselves over Z ≤ 9 — the chart as nature draws it rather than as a textbook does — gives **E = 9**, and the nine cells are named:

    He-5, He-7, Li-10, Be-8, Be-13, B-9, B-16, B-18, C-21

Every one is a known unbound nuclide sitting inside the band its own neighbours define, and the band is exactly ℛ of the measurement — the drawn chart is the closure of the real one. What the nine are is content the coordinates cannot carry. Be-8 is unbound because it is two alpha particles and nothing else — clustering. He-5, He-7, Li-10 and Be-13 are unbound by one neutron against an even-paired core — pairing. The coordinate pair (Z, N) knows how many protons and neutrons a nuclide has and cannot know that four of them prefer to be an alpha, or that the last one is unpaired. **The nine cells are the pairing and clustering terms of the mass formula, counted** — the same shape as the calendar's seven and the periodic table's thirty-six: a defect that names a real mechanism the index has no axis for. Register 298.

The same shape appears a third time, in chemistry, where it can be watched arriving. An index may bracket a quantity only along an axis the quantity is monotone on. Give first ionization energies to that test as bare numbers, with no shell model attached:

| period 2 | Li 5.392 · Be 9.323 · B 8.298 · C 11.260 · N 14.534 · O 13.618 · F 17.423 · Ne 21.565 |
| period 3 | Na 5.139 · Mg 7.646 · Al 5.986 · Si 8.152 · P 10.487 · S 10.360 · Cl 12.968 · Ar 15.760 |

Monotonicity fails at Be→B and N→O, and again at Mg→Al and P→S — the same two positions in both periods. Those are the s² → p¹ subshell opening and the p³ → p⁴ first pairing: the two anomalies every general-chemistry course teaches, located from the numbers alone. Twelve interior cells, four steps refused, **67% admissible.** It is a retrodiction, not a discovery — both have been explained since the 1920s. What earns it a place here is that it is *mechanical*: where an index refuses, a mechanism is entering that the coordinates do not carry, and the refusal map says where without being told what. The periodic table's thirty-six, the measured nuclide chart's nine, and these four are one phenomenon counted in three subjects. Register 308.

**And a ninth subject enters without a coordinate being added for it: time.** Every subject above is a thing indexed; time is not — a date must never enter Λ (§F.4.3), since a transition is a type and types are not dated. What enters instead is **composition**: an order between cells rather than a stamp on one. Λ₉ is closed under composition on all its composable pairs, associative, and is therefore a category of transitions — and composition is time, a coordinate the book already carried, read as an order (register 313).

What makes it a subject rather than a metaphor is that it is measured. **Occupancy never rises along composition** — zero of 739 steps — so the object graph falls into three eras pure in occupancy, circulation total inside each and impossible between them, with 904 of 1,654 cells conservative. That gives the index a direction. But the direction is a reading under a frame, and the frame is an act of observation: it holds when each transition's destination is taken to begin empty. Represent occupied destinations instead — an index that is equally lawful and equally closed — and 31.6% of composable steps run the other way, with no global direction at all. **Neither reading is wrong. The arrow is a property of what the observer takes as the starting state**, and observation is what selects between the two. This is the book's own boundary, met early: an index says what a thing is, and where it must have been between two observations; it does not say what a thing will become. The clock runs toward the state that has spent something, and reading it backwards reads toward the fuller, earlier one — the past. An index can say where something must have been between two observations; it cannot say where it will be after the last. Register 348.

The calendar's seven are (2,29), (2,30), (2,31), (4,31), (6,31), (9,31) and (11,31). That is the content of *Thirty days hath September* — the rhyme exists because the calendar's coordinates cannot carry the month lengths, and it is exactly seven cells long.

### 4.2.1 The nuclide chart's defect, recomputed under variation
The measured chart's E = 9 is stated to the book's highest standard — the method named with its input set, the inputs printed, and the result recomputed at four proton-number cutoffs rather than once. Take the measured nuclides as cells (Z, N), close under the monotone envelopes of §4.1, and count what the closure admits and the chart lacks:

| Z ≤ | nuclides | admitted | E | the cells admitted and absent |
|---|---|---|---|---|
| 5 | 27 | 33 | 6 | He-5, He-7, Li-10, Be-8, Be-13, B-9 |
| 6 | 40 | 48 | 8 | …and B-16, B-18 |
| 7 | 52 | 61 | **9** | …and C-21 |
| 9 | 80 | 89 | **9** | unchanged |

Every cell named at one cutoff persists at every larger one, and none is added after Z ≤ 7. The defect is not an artefact of where the chart was cut: the boundary was moved four times and the nine cells did not move, so they are a property of the measurement rather than of the window. Registers 388, 390.

### 4.3 The calendar can be repaired, and the repair is instructive
The calendar fails for one reason: the number of days is not monotone in the month, because February has 28. Relabel the months in order of length — February, April, June, September, November, January, March, … — and E drops to 0. The 365 cells are identical; only the labels move. And the repaired calendar is useless: a calendar whose months run in order of length is self-defining and unusable.

So the trade is explicit, and it has a number:

    E(X) = 7 is the price of keeping January first.

Non-closure is not always a fault. It is sometimes a purchase — usability bought with definitional self-sufficiency. What this book supplies is the price tag, not the verdict.

### 4.4 What follows
So the defect is not chemistry's alone. In four subjects it named the same thing — a real mechanism the coordinates could not carry — and in each it could be counted exactly. The natural question is whether an index can be built that has none of it: not a table patched until the gaps are hidden, but one whose own coordinates admit every cell they imply and deny nothing.

That index exists. It is the same 118 elements, re-coordinated, and its cost is zero. It adds no physics and predicts no measurement; what it removes is the thirty-six. But an index that denies nothing turns out to be a stranger object than an index that merely counts well — it cannot help containing its own definition, it cannot host a contradiction, and it fixes exactly what may be added to it. The rest of Part I builds it. What comes after shows that its E = 0 is not a tidy virtue standing alone, but the root from which two further properties grow — and that the same construction, followed upward, carries a clock it was never given.
