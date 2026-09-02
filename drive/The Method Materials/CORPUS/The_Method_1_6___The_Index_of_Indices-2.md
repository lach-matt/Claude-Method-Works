
# THE METHOD 1.6 — THE INDEX OF INDICES

Generated on 2026-08-15 by `indices.py`. **Every index this work builds
on or beside the atomic index — what it holds, whether it closes, whether it carries time, and
what role it plays for Λ.** Measured where measurable; where an index is named and never built,
that is stated rather than filled in.

---

# I · THE ATOMIC INDEX ITSELF

**Λ = { (n, ℓ, k, q, e, f, g, 2S) ∈ ℤ⁸ : eight constraints, at caps }.**

![**Figure 1.** Λ₈'s constraint graph. Seven bounds on eight coordinates — a caterpillar with 2S pendant at k. Every edge is a single monotone inequality except one: g ≤ min(q, 4f+2) gives g two parents and is the only non-product term in the expression.](figures-compendia/fig-i3-lambda8.png)

A cell is a **transition**: a source subshell (n, ℓ) holding k electrons, q of them moving, into a
target subshell (e, f) that ends with g, at spin 2S. **Not a state — a move.** Everything else in
this document follows from that.

| constraint | reads |
|---|---|
| **ℓ ≤ n − 1** | hydrogenic — the subshell fits its shell |
| **k ≤ 4ℓ + 2** | **Pauli** — the subshell's capacity |
| **q ≤ k** | conservation of the removed — you cannot take more than is held |
| **f ≤ e − 1** | hydrogenic again, on the target |
| **g ≤ 4f + 2** | **Pauli** again, on the target |
| **g ≤ q** | conservation of the placed |
| **2S ≤ k** | the multiplicity a subshell can carry |
| **k ≥ 1** | *definitional* — a transition needs a mover |

**The one coupling is g ≤ min(q, 4f+2)**, the single non-product term in the generating function,
and it is the Pauli principle. Remove it and 976 becomes 1,000; the 24 excluded cells all have
f = 0 and g = 3 — three electrons in an s orbital.

---

# II · THE TOWER

**Each stage adds one axis and inherits every bound below.**

| stage | cells | axes | composable | fraction | the axis added |
|---|---|---|---|---|---|
| **Λ₈** | 976 | 8 | 0 | **0.0000** | — |
| **Λ₉** | 1,654 | 9 | 1,169 | **0.7068** | 2S′ ≤ g |
| **Λ₁₀** | 2,535 | 10 | 2,050 | **0.8087** | 2S′ ≤ v ≤ g |
| **Λ₁₁** | 13,585 | 11 | 9,450 | **0.6956** | 2J_c ≤ φ̂(k) |
| **Λ₁₂** | 70,905 | 12 | 46,740 | **0.6592** | 2K ≤ 2J_c + 2f_max |
| **Λ₁₃** | 199,130 | 13 | 127,070 | **0.6381** | \|2J − 2K\| ≤ 1 |

![**Figure 2.** The composable fraction at each stage of the tower. Λ₈ composes not at all, four source coordinates against three target; the two counting axes raise the fraction to 0.8087 at Λ₁₀; each of the three coupling axes lowers it.](figures-compendia/fig-i1-tower.png)

> **Counting axes raise the composable fraction; coupling axes lower it. No exception.**

**Λ₈ composes not at all** — four source coordinates against three target. **Λ₁₀ is the peak at
80.87%**, and every stage after it falls. **The non-composable cells are exactly those with g = 0**
at the peak, since k ≥ 1 forbids an empty target being a source.

---

# III · THE INDEXES DRAWN BESIDE IT

| index | coordinates | cells | box | E | kind |
|---|---|---|---|---|---|
| the periodic table | (period, group) | 90 | 126 | **36** | **state** |
| Janet's left-step | (n+ℓ, Z) | 118 | 944 | **0** | **state** |
| the calendar | (month, day) | 365 | 372 | **7** | **state** |
| a box ordering | (l, w, h) | 35 | 125 | **0** | **state** |
| a chessboard | (rank, file) | 64 | 64 | **0** | **state** |

> **Reading the table.** *E = 0 carries information only when the ambient box exceeds the cells*, which
> is why box is reported beside every defect. **E is the closure defect, not the difference between the
> two columns** — Janet's left-step and the box ordering both close at E = 0 inside boxes far larger
> than their cell counts, while the chessboard closes at E = 0 because its box IS its cells.

![**Figure 3.** Every index this work builds or draws, as cells against defect. Circles are transition indexes: their cells are moves and carry a time column. Squares are state indexes: a cell is one position and composition does not arise.](figures-compendia/fig-i2-landscape.png)

**None of these is a transition index, so none can carry a time column.** A state cell has one
position; the question *is my target another cell's source* does not arise.

**Janet closes at E = 0 and the classroom table does not.** That is a fact about the two tables
**in coordinates chemists fixed for other reasons** — §21.6 shows any composite count has SOME
coordinate system where E = 0, so the result is that Janet's 1928 ordering, chosen for shell
filling, happens to close.

---

# IV · THE VIOLATION INDEX

**The companion paper's object, indexed over nine letters.** It is here because it is the one
index this work reasons about without holding — **its cells are not printed anywhere**, and what
follows is everything that is.

| letter | meaning | rungs |
|---|---|---|
| **X** | exotic matter required | 4 |
| **S** | semiclassical corrections | 3 |
| **IC** | initial conditions | 3 |
| **U** | unitarity | 3 |
| **NEC** | null energy condition points | 5 |
| **L** | locality | 2 |
| **SD** | superdeterminism | 2 |
| **DNc** | dynamical, continuous | 3 |
| **DNd** | dynamical, discrete | 3 |

**4 · 3 · 3 · 3 · 5 · 2 · 2 · 3 · 3 = 19,440**, and the index holds **2,370** — 12.19% density.

## What the companion prints

| object | threshold | cells | reachable |
|---|---|---|---|
| classical black hole | `none` | 2,370 | 1,410 |
| Hawking-evaporating | `NEC ≥ 1` | 2,196 | 1,410 |
| Planck-scale wormhole | `NEC ≥ 2` | 1,764 | 1,134 |
| macroscopic wormhole | `NEC ≥ 3` | 1,146 | 738 |
| universal horizon | `X ≥ 2` | 1,374 | 840 |
| time machine | `X = 3` | 558 | 360 |

**Twelve numbers, and one column is a second predicate on the same cells.** Differenced, the
cells give NEC = 0 at 174, NEC = 1 at 432, NEC = 2 at 618, NEC ≥ 3 at 1,146. **All 174 cells at
NEC = 0 are unreachable** — removing them removes no reachable cell — and **exactly 64% of NEC = 1
and 64% of NEC = 2 cells are reachable**, 276 of 432 and 396 of 618.

## Its defect, and the one constraint printed

**E = 30, collapsing as 1 × 30** — one core cell repeated across the free coordinates — with the
core at **(X = 0, U = 0, NEC = 3)**. At fifteen letters: 18,072 cells, **E = 816 = 1 × 816.**
**Multiplicities 3, 5, 10, 30 at 4, 5, 7 and 9 coordinates**, and 5 is not a product of any two
rung counts, so **the edge list constrains the free letters as well as the support.**

**The constraint the companion prints**, at arity 3:

> **NEC ≥ 3 ∧ X = 0 → U ≥ 1** — cells 2,370, E = 30, core 1

with three variants: `NEC ≥ 3 → U ≥ 1` at arity 2 giving **E = 0**, and `NEC ≥ 3 ∧ U = 0 → X ≥ 1`
and `NEC ≥ 3 → (IC ∨ U ∨ X)` both giving E = 30. **A jurisdicted forcing and an unjurisdicted
disjunction give identical defects; arity 2 gives none.**

## What is not printed, and what nine searches established

**The edge list itself.** §5.7 of the companion says so outright. Nine searches were run against
the twelve numbers; the best holds **cells exactly 2,370 at distance 29**, with the whole residual
on the NEC interior — **NEC ≥ 2 sixteen too high, NEC ≥ 3 nine too low, missing in opposite
directions.**

**Eight alphabets were tried and none moved it**: simple implications, disjunctive heads,
conjunctive bodies, all 47 single-rule edits, four alternative rung readings, two threshold
semantics, seeding at NEC = 3, and weighted sums with gated deviations. **The rungs and the ≥
reading are confirmed correct** — every alternative is two orders of magnitude worse.

    **And the reachable column reduces to the same missing artefact.** Three local
    readings of reachability give ~99% against a printed 60%; the companion's own
    `here?` column says reachable means reachable FROM HERE, directed from one
    position in a transition graph. **Both columns need the edge list.**

---

# V · THE INDEXES BUILT FROM IT

Each of these exists because Λ exists — it indexes something Λ's cells have, or something the
act of building Λ produced.

## The electromagnetic quotient

**Λ modulo the dipole selection rules** — Δℓ = ±1, ΔS = 0, parity. A quotient, not a subset:
cells are identified when the rules cannot distinguish them.

**Its E = 0 is VACUOUS** — §12.11.8 — because the image is a complete rectangle. **It closes
because it is a box, not because the selection rules constrain it.**

![**Figure 4.** The crossing. Within one atom a dipole-allowed transition is followable 11.6% of the time against 40.7% for a forbidden one; across the 118 elements the order reverses, 89.7% against 77.9%. The rule that forbids composition inside an atom enables it between atoms.](figures-compendia/fig-i4-crossing.png)

**Its measured role is the crossing.** Within one element, EM-allowed transitions compose at
**11.6%** against the forbidden **40.7%**. Across the 118 elements the order reverses — **89.7%
against 77.9%.** *The rule that forbids composition inside an atom is the rule that enables it
between atoms.*

## The time index

**Not a coordinate. The second column.** §12.11.0: composition IS the temporal order — a cell's
source end is a before, its target end an after, and q is what changed between them.

**An index has a time column exactly when its cells are moves.** Λ₈ 976/0, Λ₉ 1,654/1,169,
Λ₁₀ 2,535/2,050 — and the periodic table and the calendar **cannot have one**, because a state
cell has one position and there is nothing to compose.

**What Λ lacks is not a clock but a denominator** — claims per session — which §12.11.1.1 now
supplies. *A date must never enter Λ: a transition is a type, and types are not dated.*

## The space index

**The first column.** What the index holds, as against what it can compose. **Λ has no spatial
coordinate**: n and e are shell numbers, not positions, and nothing in the eight is a place.

**The nearest thing to a spatial reading is the observability one**: an observer's register is
Λ-valued because observation IS an atomic state change, so an unregistered event is an
admitted-and-absent cell and **E(local register) measures what is not yet real to that observer.**
*That is a definition with a falsifiable consequence and it is not yet built.*

## Λ₃ — the three-body index

**The second index built from physics rather than from Λ** (the first is Λ_spectra), and the first whose subject is classical. Chapter 36; register 1713–1724.

| coordinate | values | bound |
|---|---|---|
| stratum | KAM, per, chaos, erg, coll | five, exhaustive |
| E | ℝ | sign fixes bounded/unbounded |
| L | ℝ | — |
| masses | ℝ₊³ | 13 order-types; symmetry order 6, 2, 1 |

![**Figure 5.** The tower read downward: 12 → 4 → 2 → 1 inputs.](figures/fig3_tower.png)

**E(Λ₃) = 0.** Certificate (§18.4.1): the shape map, three dropped coordinates. *Its cells are configurations, not moves, so it carries no time column — the flow is the geodesic flow of the Jacobi–Maupertuis metric, and time is a quadrature (§12.11.1.3).* Named at §12.11.2 as the maximal case of what Chapter 18 forbids; built, and the completeness is the impossibility theorem read as an index.
## The nucleon index

**The measured nuclide chart, indexed by proton and neutron count.** Chemistry's index is Λ; the nucleus has its own, and it is the one place a second physical index is built alongside the atomic one. Register 298, 388, 390.

| coordinate | values | bound |
|---|---|---|
| Z | ℤ₊ | proton number |
| N | ℤ₊ | neutron number |

**E = 9**, on the particle-bound nuclides at low Z — those that do not immediately emit a nucleon — stable across four proton-number cutoffs. Closing that chart admits nine cells it lacks: **He-5, He-7, Li-10, Be-8, Be-13, B-9, B-16, B-18, C-21**, each a known unbound nuclide interior to the chart. Be-8 is unbound because it is two alpha particles — clustering; He-5, He-7, Li-10 and Be-13 are unbound by one neutron against an even-paired core — pairing. **The nine are the pairing and clustering terms of the mass formula, counted** — content the coordinates cannot carry, since (Z, N) records proton and neutron count and not whether four nucleons form an alpha. The defect appears by Z ≤ 7 and none is added after, so it is a property of the measurement, not of the cutoff. The drawn chart between its drip lines is ℛ of the measured one, E = 0 by idempotence.

## The Kreuzer–Skarke frontier

**The Calabi–Yau catalogue, indexed by its two Hodge numbers.** An index the method reaches outside atomic physics — the reflexive-polytope list of string compactifications, drawn beside Λ to show the operator travels. §31.3.

| coordinate | values | bound |
|---|---|---|
| h¹¹ | ℤ₊ | first Hodge number |
| h²¹ | ℤ₊ | second Hodge number |

**E = 540 on a specifiable slice.** The full catalogue is a file this work could not read, but one slice is stated exactly in print: the χ = ±6 points, with Hodge numbers (h, h+3) and (h+3, h) for 13 ≤ h ≤ 128 and named exclusions — **208 cells**. Closing it admits **540 cells**, from 498 join failures and 498 meet failures of 21,528 pairs. The 540 are predictions, not a defect: the join of (h, h+3) and (h+3, h) is (h+3, h+3), so ℛ fills the diagonal the two Hodge-pair sequences bound. The admitted cells carry five distinct Euler characteristics, χ ∈ {0, ±2, ±4}, with 112 on the diagonal from (13, 13) to (131, 131) and h¹¹ + h²¹ from 26 to 262. Each is a Hodge pair the catalogue must contain if the pair set is closed under Batyrev's duality; every one satisfies the published bounds h¹¹ ≥ 1, h²¹ ≥ 1 and h¹¹ + h²¹ ≤ 502, so none is refuted, but the file to confirm them is missing. The index proposes; it is not thereby right.

## The string partition function

**The generating function of string state degeneracies, read as an index with multiplicity.** Where Λ's cells are present or absent, this index's cells carry a count — the number of string states at each level. §31.2.3.

| coordinate | values | bound |
|---|---|---|
| mode occupation | ℤ₊ per oscillator (n, i), n ≥ 1, i ∈ 1…24 | independent |
| level | N = Σ n · occ(n, i) | the graded total |

**E = 0**, because the modes are independent. The partition function ∏ₙ (1 − qⁿ)⁻²⁴ = Σ d(N) qᴺ counts the states at level N as the 24-coloured partitions of N — a part of size n available in each of the 24 transverse dimensions — giving d(1) = 24, d(2) = 324, d(3) = 3,200, and d(14) = 156,883,829,400. The admissible set of occupation vectors is a full product, each oscillator's occupancy free of every other's, and a product closes trivially: ℛ adds nothing, so E = 0. It closes for the reason dual to Λ's — Λ's coordinates couple along a tree and close in one pass; the string's modes do not couple at all, which is the degenerate case of the three closure conditions where independence stands in for the tree. The two are the same theorem at its two ends: an index closes when its coordinates are free, and it closes when they couple only along a tree, and nothing between.


## The languages

**A language is a coordinate system; translation is re-coordinatisation; E is the cost.**

| language | closure operator | delete | add |
|---|---|---|---|
| order | ℛ | restored | absorbed |
| geometry | monotone polyhedron | restored | absorbed |
| algebra / logic | ideal, Gröbner basis | still derivable | T·h enters the ideal |
| analysis | coefficients of F | restored | absorbed |
| information | description length | E_bits stays 0 | **grows** |
| **statistics** | max-entropy on the marginals | restored | **grows** |
| documentary | **none — no algorithm** | — | — |

**Six agree on Λ at 976 and all ten pairs hold** — C(5,2), a complete graph, not a ladder.
**Statistics was tested and qualifies with a caveat**: it recovers Λ at 976 and E = 0, but gives
**E = 0 on the periodic table where ℛ gives 36** — *marginals cannot see a hole.* It agrees with
the others only where there is nothing to disagree about.

## The book's own indexes

| index | coordinates | cells | E | what it holds |
|---|---|---|---|---|
| the audits | object<source<artefact<outside · what · how · depends | 21 | **16** | twenty-two audits |
| the register | corroboration ≤ φ̂(repair) | 33 | **6** | the corrections |
| Q | blocks · obstacle · cost · depends | 8 | **5** | what the book does not know |
| the protocols | trigger · object · failure · earned | 19 | **105** | twenty-four protocols |
| the constraints | parents · form · carried · source · role | 15 | **21 / E₄ 6** | every constraint in the book |
| the mathematics | kind · language · status · verification · precedent | 77 | **0** | fibred, twenty-four fibres (27 over sixteen when this table was first printed; main §D.5.10) |
| the numbers | fibre · kind · role | — | **40** | every figure the book prints |
| **the channel survey** | **Z · core charge · ℓ** | **1,664** | **1,351** | **596 Rydberg channels across 313 cells** |

**These exist because the book exists, not because Λ does** — but they are built by Λ's method,
and the audits index's two frontier cells are the same pair ℛ₄ refuses at §14.5.6, reached by two
computations sharing no code.

---

## How much of an index determines the rest

**Remove cells at random and ask whether ℛ puts them back.** The largest fraction removable with exact recovery is a property of the index, and it had never been measured for any of these.

| index | dimension | envelopes | coupling | **redundancy** |
|---|---|---|---|---|
| Λ | 8 | 56 | 29% | **61%** |
| Λ_spectra^obs | 3 | 6 | 17% | **20%** |
| a box ordering | 3 | 6 | 50% | 0% |
| Janet | 2 | 2 | 50% | 0% |
| the periodic table | 2 | 2 | 0% | 0% |
| the calendar | 2 | 2 | 0% | 0% |

**Coupling does not explain it.** The fraction of coordinate pairs whose envelope actually constrains gives **r² = 0.002, p = 0.94** against redundancy: Janet and the box ordering both couple at 50% and recover nothing, while Λ_spectra^obs couples at 17% and recovers a fifth. *That conjecture was stated before the measurement and is wrong.*

**DIMENSION explains it, and the projection test shows so on a single object.** Λ restricted to its own first d coordinates, constraints unchanged:

        d = 8   61%        d = 5   30%
        d = 7   30%        d = 4    5%
        d = 6   30%        d = 3    0%

ℛ works on **pairwise** envelopes, so an index of dimension d carries d(d−1) of them — **56 for Λ, 6 for Λ_spectra^obs, 2 for a plane.** With two envelopes there is almost nothing to reconstruct from, and that is what the operator is rather than a fact about any subject.

**But only INDEPENDENT coordinates count.** Adding the electron count Nₑ = Z − c + 1 to Λ_spectra^obs — a function of two coordinates it already has — takes redundancy from **20% to 0%**, while doubling the envelopes and raising coupling from 17% to 33%. *A derived coordinate adds no information and obliges ℛ to reproduce it exactly, so recovery becomes strictly harder.* Registers 1119–1122.


---

## The channel survey — Λ_spectra^obs

**Coordinates: Z · core charge · ℓ.** Each cell is a Rydberg channel — a fixed parent core, a fixed ℓ, n running. The compendium holds **596 channels across 313 of the survey's 1,664 cells**.

**This is not the coordinate index, and the two were once both called Λ_spectra.** Λ_spectra proper is the four-coordinate index (Z, charge, ℓ, 2S+1) at 104,832 cells with **E = 0** — see *Λ_spectra — the channel index*, below. Λ_spectra^obs is the three-coordinate **survey of what has been measured**. The column beside each cap below is grid minus held — the **unwitnessed** count — and *not* a closure defect: reading it as E would say the index is open when it is a fixed point. R 1657.

**Where its alphabets come from, and why that differs from Λ.** Λ's coordinates are bounded by the physics — ℓ < n, k ≤ 4ℓ+2 — and all 118 ground configurations are known within its caps, so Λ is complete at 976 cells. **Λ_spectra^obs is not.** Rydberg series are unbounded in n and ℓ runs to n−1, so the index is **infinite unless capped**, and every cap is a decision. Three defensible ones give:

| alphabet | grid | unwitnessed |
|---|---|---|
| as measured — charge [1, 2, 3, 4, 5, 6, 9, 11, 15, 16] | 1,664 | 1,351 |
| charge 1 to Z−1 over the elements held | 4,376 | 4,148 |
| all 118 elements, ℓ 0–7 | 55,224 | 54,996 |

**All three grids are closed** — each is a fixed point of ℛ, verified by double projection. The number beside each is what has *not* been measured under that cap, so it is a result about the cap and about the state of the literature; it is never a closure defect. *Registers 959–962, 1657.*

**What the index says about cells it does not hold.** Every cell carries a grade, and the grade records how far the statement travelled:

| grade | cells | what it means |
|---|---|---|
| MEASURED | 205 | a defect computed from levels |
| BRACKETED | 5 | bounded above and below by DIFFERENT mechanisms |
| BOUNDED | 42 | bounded on one side, adjacent to a measurement |
| PROPAGATED | 954 | a bound inherited through a chain of 2 to 13 steps |
| FORMAL | 73 | the only bound is one a mechanism already implies |
| UNCONSTRAINED | 33 | **no statement at all** |

**97.5% of the index carries a defensible statement.** The three relations that propagate are **the l-collapse (register 693)** along ℓ, **the isoelectronic ladder (register 708)** along an isoelectronic sequence, and **the same-element ladder (register 963)** along the charge states of one element. *Registers 963–965, 981.*

![**Figure 6.** Λ_spectra^obs as a lattice: element across, ℓ into the page, ionisation stage up. Green: measured. Orange: bounded from two sides by different mechanisms. Gold: bounded from one. Faint markers: cells the structure admits with no measurement. The occupied region is a wedge at low Z and low ℓ, where long Rydberg series have been tabulated.](figures-compendia/fig-spectra-lattice.png)

**And the last 33 are of three kinds, only two of which a capture can fix.** **Ar I** holds one cell at d — an ordinary gap. **P I, Cd I and Ti II** hold six each, eighteen cells at ℓ ≥ 2, wanting a longer capture. **Sc I and Ti I have no Rydberg series at all** — their levels are 3d.4s.4p and 3d².4s mixtures with no n running, so their **fourteen** cells are unreachable by any capture. One, eighteen and fourteen make the 33. *Registers 983, 984.* **The ceiling is 98.9%, not 100%** — (1,312 − 14) / 1,312 — **and that is a fact about the open-shell transition metals rather than about the collection.**


---

# VI · THE INDEXES NAMED AND NOT BUILT

**§29.1: the absence is not evidence.** These were named in the course of the work and no index
exists for them. Saying so is the point of this section.

**Sound.** Phonon modes are discrete and indexable — ω, lattice momentum, polarisation, occupation
— but they index a **material**, not an atom. **No such index is built here**, and it would sit
beside Λ rather than inside it, since Λ has no coordinate a lattice vibration could occupy.

**Frequency.** A transition's frequency is ΔE/h, and ΔE is not a coordinate of Λ — **§6.2 gives
first ionisation energies to the bracket and the bracket REFUSES**, at Be→B, N→O, Mg→Al and P→S,
four steps of twelve. *That refusal is the book's most direct statement about frequency: the
coordinates cannot bracket it, and where they refuse a mechanism is entering.*

**The multiverse.** §32.6.1 places this outside all four of the book's indexes, with the
destination coordinate, because §E.1.4 shows **the open set cannot express an unclosable question.**
*It is not an index that has not been built. It is the shape of a question this work cannot pose*
— and Theorem 18.1 is why: Λ's order structure contributes nothing predictively beyond what the
coordinates supply, and its coordinates are n, ℓ, k, q, e, f, g, 2S.

---

# VII · THE FULL TABLES

**Every index small enough to print, printed.** The tower above Λ₈ runs to 199,130 cells at Λ₁₃
and is given by its construction instead; the violation index has no cells to give.

## Λ₈ — all 976 cells

| # | n | ℓ | k | q | e | f | g | 2S |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 2 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| 3 | 1 | 0 | 1 | 0 | 2 | 0 | 0 | 0 |
| 4 | 1 | 0 | 1 | 0 | 2 | 0 | 0 | 1 |
| 5 | 1 | 0 | 1 | 0 | 2 | 1 | 0 | 0 |
| 6 | 1 | 0 | 1 | 0 | 2 | 1 | 0 | 1 |
| 7 | 1 | 0 | 1 | 0 | 3 | 0 | 0 | 0 |
| 8 | 1 | 0 | 1 | 0 | 3 | 0 | 0 | 1 |
| 9 | 1 | 0 | 1 | 0 | 3 | 1 | 0 | 0 |
| 10 | 1 | 0 | 1 | 0 | 3 | 1 | 0 | 1 |
| 11 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| 12 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 13 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| 14 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 15 | 1 | 0 | 1 | 1 | 2 | 0 | 0 | 0 |
| 16 | 1 | 0 | 1 | 1 | 2 | 0 | 0 | 1 |
| 17 | 1 | 0 | 1 | 1 | 2 | 0 | 1 | 0 |
| 18 | 1 | 0 | 1 | 1 | 2 | 0 | 1 | 1 |
| 19 | 1 | 0 | 1 | 1 | 2 | 1 | 0 | 0 |
| 20 | 1 | 0 | 1 | 1 | 2 | 1 | 0 | 1 |
| 21 | 1 | 0 | 1 | 1 | 2 | 1 | 1 | 0 |
| 22 | 1 | 0 | 1 | 1 | 2 | 1 | 1 | 1 |
| 23 | 1 | 0 | 1 | 1 | 3 | 0 | 0 | 0 |
| 24 | 1 | 0 | 1 | 1 | 3 | 0 | 0 | 1 |
| 25 | 1 | 0 | 1 | 1 | 3 | 0 | 1 | 0 |
| 26 | 1 | 0 | 1 | 1 | 3 | 0 | 1 | 1 |
| 27 | 1 | 0 | 1 | 1 | 3 | 1 | 0 | 0 |
| 28 | 1 | 0 | 1 | 1 | 3 | 1 | 0 | 1 |
| 29 | 1 | 0 | 1 | 1 | 3 | 1 | 1 | 0 |
| 30 | 1 | 0 | 1 | 1 | 3 | 1 | 1 | 1 |
| 31 | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| 32 | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| 33 | 1 | 0 | 2 | 0 | 1 | 0 | 0 | 2 |
| 34 | 1 | 0 | 2 | 0 | 2 | 0 | 0 | 0 |
| 35 | 1 | 0 | 2 | 0 | 2 | 0 | 0 | 1 |
| 36 | 1 | 0 | 2 | 0 | 2 | 0 | 0 | 2 |
| 37 | 1 | 0 | 2 | 0 | 2 | 1 | 0 | 0 |
| 38 | 1 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| 39 | 1 | 0 | 2 | 0 | 2 | 1 | 0 | 2 |
| 40 | 1 | 0 | 2 | 0 | 3 | 0 | 0 | 0 |
| 41 | 1 | 0 | 2 | 0 | 3 | 0 | 0 | 1 |
| 42 | 1 | 0 | 2 | 0 | 3 | 0 | 0 | 2 |
| 43 | 1 | 0 | 2 | 0 | 3 | 1 | 0 | 0 |
| 44 | 1 | 0 | 2 | 0 | 3 | 1 | 0 | 1 |
| 45 | 1 | 0 | 2 | 0 | 3 | 1 | 0 | 2 |
| 46 | 1 | 0 | 2 | 1 | 1 | 0 | 0 | 0 |
| 47 | 1 | 0 | 2 | 1 | 1 | 0 | 0 | 1 |
| 48 | 1 | 0 | 2 | 1 | 1 | 0 | 0 | 2 |
| 49 | 1 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| 50 | 1 | 0 | 2 | 1 | 1 | 0 | 1 | 1 |
| 51 | 1 | 0 | 2 | 1 | 1 | 0 | 1 | 2 |
| 52 | 1 | 0 | 2 | 1 | 2 | 0 | 0 | 0 |
| 53 | 1 | 0 | 2 | 1 | 2 | 0 | 0 | 1 |
| 54 | 1 | 0 | 2 | 1 | 2 | 0 | 0 | 2 |
| 55 | 1 | 0 | 2 | 1 | 2 | 0 | 1 | 0 |
| 56 | 1 | 0 | 2 | 1 | 2 | 0 | 1 | 1 |
| 57 | 1 | 0 | 2 | 1 | 2 | 0 | 1 | 2 |
| 58 | 1 | 0 | 2 | 1 | 2 | 1 | 0 | 0 |
| 59 | 1 | 0 | 2 | 1 | 2 | 1 | 0 | 1 |
| 60 | 1 | 0 | 2 | 1 | 2 | 1 | 0 | 2 |
| 61 | 1 | 0 | 2 | 1 | 2 | 1 | 1 | 0 |
| 62 | 1 | 0 | 2 | 1 | 2 | 1 | 1 | 1 |
| 63 | 1 | 0 | 2 | 1 | 2 | 1 | 1 | 2 |
| 64 | 1 | 0 | 2 | 1 | 3 | 0 | 0 | 0 |
| 65 | 1 | 0 | 2 | 1 | 3 | 0 | 0 | 1 |
| 66 | 1 | 0 | 2 | 1 | 3 | 0 | 0 | 2 |
| 67 | 1 | 0 | 2 | 1 | 3 | 0 | 1 | 0 |
| 68 | 1 | 0 | 2 | 1 | 3 | 0 | 1 | 1 |
| 69 | 1 | 0 | 2 | 1 | 3 | 0 | 1 | 2 |
| 70 | 1 | 0 | 2 | 1 | 3 | 1 | 0 | 0 |
| 71 | 1 | 0 | 2 | 1 | 3 | 1 | 0 | 1 |
| 72 | 1 | 0 | 2 | 1 | 3 | 1 | 0 | 2 |
| 73 | 1 | 0 | 2 | 1 | 3 | 1 | 1 | 0 |
| 74 | 1 | 0 | 2 | 1 | 3 | 1 | 1 | 1 |
| 75 | 1 | 0 | 2 | 1 | 3 | 1 | 1 | 2 |
| 76 | 1 | 0 | 2 | 2 | 1 | 0 | 0 | 0 |
| 77 | 1 | 0 | 2 | 2 | 1 | 0 | 0 | 1 |
| 78 | 1 | 0 | 2 | 2 | 1 | 0 | 0 | 2 |
| 79 | 1 | 0 | 2 | 2 | 1 | 0 | 1 | 0 |
| 80 | 1 | 0 | 2 | 2 | 1 | 0 | 1 | 1 |
| 81 | 1 | 0 | 2 | 2 | 1 | 0 | 1 | 2 |
| 82 | 1 | 0 | 2 | 2 | 1 | 0 | 2 | 0 |
| 83 | 1 | 0 | 2 | 2 | 1 | 0 | 2 | 1 |
| 84 | 1 | 0 | 2 | 2 | 1 | 0 | 2 | 2 |
| 85 | 1 | 0 | 2 | 2 | 2 | 0 | 0 | 0 |
| 86 | 1 | 0 | 2 | 2 | 2 | 0 | 0 | 1 |
| 87 | 1 | 0 | 2 | 2 | 2 | 0 | 0 | 2 |
| 88 | 1 | 0 | 2 | 2 | 2 | 0 | 1 | 0 |
| 89 | 1 | 0 | 2 | 2 | 2 | 0 | 1 | 1 |
| 90 | 1 | 0 | 2 | 2 | 2 | 0 | 1 | 2 |
| 91 | 1 | 0 | 2 | 2 | 2 | 0 | 2 | 0 |
| 92 | 1 | 0 | 2 | 2 | 2 | 0 | 2 | 1 |
| 93 | 1 | 0 | 2 | 2 | 2 | 0 | 2 | 2 |
| 94 | 1 | 0 | 2 | 2 | 2 | 1 | 0 | 0 |
| 95 | 1 | 0 | 2 | 2 | 2 | 1 | 0 | 1 |
| 96 | 1 | 0 | 2 | 2 | 2 | 1 | 0 | 2 |
| 97 | 1 | 0 | 2 | 2 | 2 | 1 | 1 | 0 |
| 98 | 1 | 0 | 2 | 2 | 2 | 1 | 1 | 1 |
| 99 | 1 | 0 | 2 | 2 | 2 | 1 | 1 | 2 |
| 100 | 1 | 0 | 2 | 2 | 2 | 1 | 2 | 0 |
| 101 | 1 | 0 | 2 | 2 | 2 | 1 | 2 | 1 |
| 102 | 1 | 0 | 2 | 2 | 2 | 1 | 2 | 2 |
| 103 | 1 | 0 | 2 | 2 | 3 | 0 | 0 | 0 |
| 104 | 1 | 0 | 2 | 2 | 3 | 0 | 0 | 1 |
| 105 | 1 | 0 | 2 | 2 | 3 | 0 | 0 | 2 |
| 106 | 1 | 0 | 2 | 2 | 3 | 0 | 1 | 0 |
| 107 | 1 | 0 | 2 | 2 | 3 | 0 | 1 | 1 |
| 108 | 1 | 0 | 2 | 2 | 3 | 0 | 1 | 2 |
| 109 | 1 | 0 | 2 | 2 | 3 | 0 | 2 | 0 |
| 110 | 1 | 0 | 2 | 2 | 3 | 0 | 2 | 1 |
| 111 | 1 | 0 | 2 | 2 | 3 | 0 | 2 | 2 |
| 112 | 1 | 0 | 2 | 2 | 3 | 1 | 0 | 0 |
| 113 | 1 | 0 | 2 | 2 | 3 | 1 | 0 | 1 |
| 114 | 1 | 0 | 2 | 2 | 3 | 1 | 0 | 2 |
| 115 | 1 | 0 | 2 | 2 | 3 | 1 | 1 | 0 |
| 116 | 1 | 0 | 2 | 2 | 3 | 1 | 1 | 1 |
| 117 | 1 | 0 | 2 | 2 | 3 | 1 | 1 | 2 |
| 118 | 1 | 0 | 2 | 2 | 3 | 1 | 2 | 0 |
| 119 | 1 | 0 | 2 | 2 | 3 | 1 | 2 | 1 |
| 120 | 1 | 0 | 2 | 2 | 3 | 1 | 2 | 2 |
| 121 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 122 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| 123 | 2 | 0 | 1 | 0 | 2 | 0 | 0 | 0 |
| 124 | 2 | 0 | 1 | 0 | 2 | 0 | 0 | 1 |
| 125 | 2 | 0 | 1 | 0 | 2 | 1 | 0 | 0 |
| 126 | 2 | 0 | 1 | 0 | 2 | 1 | 0 | 1 |
| 127 | 2 | 0 | 1 | 0 | 3 | 0 | 0 | 0 |
| 128 | 2 | 0 | 1 | 0 | 3 | 0 | 0 | 1 |
| 129 | 2 | 0 | 1 | 0 | 3 | 1 | 0 | 0 |
| 130 | 2 | 0 | 1 | 0 | 3 | 1 | 0 | 1 |
| 131 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| 132 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 133 | 2 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| 134 | 2 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 135 | 2 | 0 | 1 | 1 | 2 | 0 | 0 | 0 |
| 136 | 2 | 0 | 1 | 1 | 2 | 0 | 0 | 1 |
| 137 | 2 | 0 | 1 | 1 | 2 | 0 | 1 | 0 |
| 138 | 2 | 0 | 1 | 1 | 2 | 0 | 1 | 1 |
| 139 | 2 | 0 | 1 | 1 | 2 | 1 | 0 | 0 |
| 140 | 2 | 0 | 1 | 1 | 2 | 1 | 0 | 1 |
| 141 | 2 | 0 | 1 | 1 | 2 | 1 | 1 | 0 |
| 142 | 2 | 0 | 1 | 1 | 2 | 1 | 1 | 1 |
| 143 | 2 | 0 | 1 | 1 | 3 | 0 | 0 | 0 |
| 144 | 2 | 0 | 1 | 1 | 3 | 0 | 0 | 1 |
| 145 | 2 | 0 | 1 | 1 | 3 | 0 | 1 | 0 |
| 146 | 2 | 0 | 1 | 1 | 3 | 0 | 1 | 1 |
| 147 | 2 | 0 | 1 | 1 | 3 | 1 | 0 | 0 |
| 148 | 2 | 0 | 1 | 1 | 3 | 1 | 0 | 1 |
| 149 | 2 | 0 | 1 | 1 | 3 | 1 | 1 | 0 |
| 150 | 2 | 0 | 1 | 1 | 3 | 1 | 1 | 1 |
| 151 | 2 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| 152 | 2 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| 153 | 2 | 0 | 2 | 0 | 1 | 0 | 0 | 2 |
| 154 | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 0 |
| 155 | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 1 |
| 156 | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 2 |
| 157 | 2 | 0 | 2 | 0 | 2 | 1 | 0 | 0 |
| 158 | 2 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| 159 | 2 | 0 | 2 | 0 | 2 | 1 | 0 | 2 |
| 160 | 2 | 0 | 2 | 0 | 3 | 0 | 0 | 0 |
| 161 | 2 | 0 | 2 | 0 | 3 | 0 | 0 | 1 |
| 162 | 2 | 0 | 2 | 0 | 3 | 0 | 0 | 2 |
| 163 | 2 | 0 | 2 | 0 | 3 | 1 | 0 | 0 |
| 164 | 2 | 0 | 2 | 0 | 3 | 1 | 0 | 1 |
| 165 | 2 | 0 | 2 | 0 | 3 | 1 | 0 | 2 |
| 166 | 2 | 0 | 2 | 1 | 1 | 0 | 0 | 0 |
| 167 | 2 | 0 | 2 | 1 | 1 | 0 | 0 | 1 |
| 168 | 2 | 0 | 2 | 1 | 1 | 0 | 0 | 2 |
| 169 | 2 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| 170 | 2 | 0 | 2 | 1 | 1 | 0 | 1 | 1 |
| 171 | 2 | 0 | 2 | 1 | 1 | 0 | 1 | 2 |
| 172 | 2 | 0 | 2 | 1 | 2 | 0 | 0 | 0 |
| 173 | 2 | 0 | 2 | 1 | 2 | 0 | 0 | 1 |
| 174 | 2 | 0 | 2 | 1 | 2 | 0 | 0 | 2 |
| 175 | 2 | 0 | 2 | 1 | 2 | 0 | 1 | 0 |
| 176 | 2 | 0 | 2 | 1 | 2 | 0 | 1 | 1 |
| 177 | 2 | 0 | 2 | 1 | 2 | 0 | 1 | 2 |
| 178 | 2 | 0 | 2 | 1 | 2 | 1 | 0 | 0 |
| 179 | 2 | 0 | 2 | 1 | 2 | 1 | 0 | 1 |
| 180 | 2 | 0 | 2 | 1 | 2 | 1 | 0 | 2 |
| 181 | 2 | 0 | 2 | 1 | 2 | 1 | 1 | 0 |
| 182 | 2 | 0 | 2 | 1 | 2 | 1 | 1 | 1 |
| 183 | 2 | 0 | 2 | 1 | 2 | 1 | 1 | 2 |
| 184 | 2 | 0 | 2 | 1 | 3 | 0 | 0 | 0 |
| 185 | 2 | 0 | 2 | 1 | 3 | 0 | 0 | 1 |
| 186 | 2 | 0 | 2 | 1 | 3 | 0 | 0 | 2 |
| 187 | 2 | 0 | 2 | 1 | 3 | 0 | 1 | 0 |
| 188 | 2 | 0 | 2 | 1 | 3 | 0 | 1 | 1 |
| 189 | 2 | 0 | 2 | 1 | 3 | 0 | 1 | 2 |
| 190 | 2 | 0 | 2 | 1 | 3 | 1 | 0 | 0 |
| 191 | 2 | 0 | 2 | 1 | 3 | 1 | 0 | 1 |
| 192 | 2 | 0 | 2 | 1 | 3 | 1 | 0 | 2 |
| 193 | 2 | 0 | 2 | 1 | 3 | 1 | 1 | 0 |
| 194 | 2 | 0 | 2 | 1 | 3 | 1 | 1 | 1 |
| 195 | 2 | 0 | 2 | 1 | 3 | 1 | 1 | 2 |
| 196 | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 |
| 197 | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 1 |
| 198 | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 2 |
| 199 | 2 | 0 | 2 | 2 | 1 | 0 | 1 | 0 |
| 200 | 2 | 0 | 2 | 2 | 1 | 0 | 1 | 1 |
| 201 | 2 | 0 | 2 | 2 | 1 | 0 | 1 | 2 |
| 202 | 2 | 0 | 2 | 2 | 1 | 0 | 2 | 0 |
| 203 | 2 | 0 | 2 | 2 | 1 | 0 | 2 | 1 |
| 204 | 2 | 0 | 2 | 2 | 1 | 0 | 2 | 2 |
| 205 | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 |
| 206 | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 1 |
| 207 | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 2 |
| 208 | 2 | 0 | 2 | 2 | 2 | 0 | 1 | 0 |
| 209 | 2 | 0 | 2 | 2 | 2 | 0 | 1 | 1 |
| 210 | 2 | 0 | 2 | 2 | 2 | 0 | 1 | 2 |
| 211 | 2 | 0 | 2 | 2 | 2 | 0 | 2 | 0 |
| 212 | 2 | 0 | 2 | 2 | 2 | 0 | 2 | 1 |
| 213 | 2 | 0 | 2 | 2 | 2 | 0 | 2 | 2 |
| 214 | 2 | 0 | 2 | 2 | 2 | 1 | 0 | 0 |
| 215 | 2 | 0 | 2 | 2 | 2 | 1 | 0 | 1 |
| 216 | 2 | 0 | 2 | 2 | 2 | 1 | 0 | 2 |
| 217 | 2 | 0 | 2 | 2 | 2 | 1 | 1 | 0 |
| 218 | 2 | 0 | 2 | 2 | 2 | 1 | 1 | 1 |
| 219 | 2 | 0 | 2 | 2 | 2 | 1 | 1 | 2 |
| 220 | 2 | 0 | 2 | 2 | 2 | 1 | 2 | 0 |
| 221 | 2 | 0 | 2 | 2 | 2 | 1 | 2 | 1 |
| 222 | 2 | 0 | 2 | 2 | 2 | 1 | 2 | 2 |
| 223 | 2 | 0 | 2 | 2 | 3 | 0 | 0 | 0 |
| 224 | 2 | 0 | 2 | 2 | 3 | 0 | 0 | 1 |
| 225 | 2 | 0 | 2 | 2 | 3 | 0 | 0 | 2 |
| 226 | 2 | 0 | 2 | 2 | 3 | 0 | 1 | 0 |
| 227 | 2 | 0 | 2 | 2 | 3 | 0 | 1 | 1 |
| 228 | 2 | 0 | 2 | 2 | 3 | 0 | 1 | 2 |
| 229 | 2 | 0 | 2 | 2 | 3 | 0 | 2 | 0 |
| 230 | 2 | 0 | 2 | 2 | 3 | 0 | 2 | 1 |
| 231 | 2 | 0 | 2 | 2 | 3 | 0 | 2 | 2 |
| 232 | 2 | 0 | 2 | 2 | 3 | 1 | 0 | 0 |
| 233 | 2 | 0 | 2 | 2 | 3 | 1 | 0 | 1 |
| 234 | 2 | 0 | 2 | 2 | 3 | 1 | 0 | 2 |
| 235 | 2 | 0 | 2 | 2 | 3 | 1 | 1 | 0 |
| 236 | 2 | 0 | 2 | 2 | 3 | 1 | 1 | 1 |
| 237 | 2 | 0 | 2 | 2 | 3 | 1 | 1 | 2 |
| 238 | 2 | 0 | 2 | 2 | 3 | 1 | 2 | 0 |
| 239 | 2 | 0 | 2 | 2 | 3 | 1 | 2 | 1 |
| 240 | 2 | 0 | 2 | 2 | 3 | 1 | 2 | 2 |
| 241 | 2 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| 242 | 2 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| 243 | 2 | 1 | 1 | 0 | 2 | 0 | 0 | 0 |
| 244 | 2 | 1 | 1 | 0 | 2 | 0 | 0 | 1 |
| 245 | 2 | 1 | 1 | 0 | 2 | 1 | 0 | 0 |
| 246 | 2 | 1 | 1 | 0 | 2 | 1 | 0 | 1 |
| 247 | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 0 |
| 248 | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 1 |
| 249 | 2 | 1 | 1 | 0 | 3 | 1 | 0 | 0 |
| 250 | 2 | 1 | 1 | 0 | 3 | 1 | 0 | 1 |
| 251 | 2 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 252 | 2 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 253 | 2 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
| 254 | 2 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |
| 255 | 2 | 1 | 1 | 1 | 2 | 0 | 0 | 0 |
| 256 | 2 | 1 | 1 | 1 | 2 | 0 | 0 | 1 |
| 257 | 2 | 1 | 1 | 1 | 2 | 0 | 1 | 0 |
| 258 | 2 | 1 | 1 | 1 | 2 | 0 | 1 | 1 |
| 259 | 2 | 1 | 1 | 1 | 2 | 1 | 0 | 0 |
| 260 | 2 | 1 | 1 | 1 | 2 | 1 | 0 | 1 |
| 261 | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 0 |
| 262 | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 1 |
| 263 | 2 | 1 | 1 | 1 | 3 | 0 | 0 | 0 |
| 264 | 2 | 1 | 1 | 1 | 3 | 0 | 0 | 1 |
| 265 | 2 | 1 | 1 | 1 | 3 | 0 | 1 | 0 |
| 266 | 2 | 1 | 1 | 1 | 3 | 0 | 1 | 1 |
| 267 | 2 | 1 | 1 | 1 | 3 | 1 | 0 | 0 |
| 268 | 2 | 1 | 1 | 1 | 3 | 1 | 0 | 1 |
| 269 | 2 | 1 | 1 | 1 | 3 | 1 | 1 | 0 |
| 270 | 2 | 1 | 1 | 1 | 3 | 1 | 1 | 1 |
| 271 | 2 | 1 | 2 | 0 | 1 | 0 | 0 | 0 |
| 272 | 2 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| 273 | 2 | 1 | 2 | 0 | 1 | 0 | 0 | 2 |
| 274 | 2 | 1 | 2 | 0 | 2 | 0 | 0 | 0 |
| 275 | 2 | 1 | 2 | 0 | 2 | 0 | 0 | 1 |
| 276 | 2 | 1 | 2 | 0 | 2 | 0 | 0 | 2 |
| 277 | 2 | 1 | 2 | 0 | 2 | 1 | 0 | 0 |
| 278 | 2 | 1 | 2 | 0 | 2 | 1 | 0 | 1 |
| 279 | 2 | 1 | 2 | 0 | 2 | 1 | 0 | 2 |
| 280 | 2 | 1 | 2 | 0 | 3 | 0 | 0 | 0 |
| 281 | 2 | 1 | 2 | 0 | 3 | 0 | 0 | 1 |
| 282 | 2 | 1 | 2 | 0 | 3 | 0 | 0 | 2 |
| 283 | 2 | 1 | 2 | 0 | 3 | 1 | 0 | 0 |
| 284 | 2 | 1 | 2 | 0 | 3 | 1 | 0 | 1 |
| 285 | 2 | 1 | 2 | 0 | 3 | 1 | 0 | 2 |
| 286 | 2 | 1 | 2 | 1 | 1 | 0 | 0 | 0 |
| 287 | 2 | 1 | 2 | 1 | 1 | 0 | 0 | 1 |
| 288 | 2 | 1 | 2 | 1 | 1 | 0 | 0 | 2 |
| 289 | 2 | 1 | 2 | 1 | 1 | 0 | 1 | 0 |
| 290 | 2 | 1 | 2 | 1 | 1 | 0 | 1 | 1 |
| 291 | 2 | 1 | 2 | 1 | 1 | 0 | 1 | 2 |
| 292 | 2 | 1 | 2 | 1 | 2 | 0 | 0 | 0 |
| 293 | 2 | 1 | 2 | 1 | 2 | 0 | 0 | 1 |
| 294 | 2 | 1 | 2 | 1 | 2 | 0 | 0 | 2 |
| 295 | 2 | 1 | 2 | 1 | 2 | 0 | 1 | 0 |
| 296 | 2 | 1 | 2 | 1 | 2 | 0 | 1 | 1 |
| 297 | 2 | 1 | 2 | 1 | 2 | 0 | 1 | 2 |
| 298 | 2 | 1 | 2 | 1 | 2 | 1 | 0 | 0 |
| 299 | 2 | 1 | 2 | 1 | 2 | 1 | 0 | 1 |
| 300 | 2 | 1 | 2 | 1 | 2 | 1 | 0 | 2 |
| 301 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 0 |
| 302 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 |
| 303 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 2 |
| 304 | 2 | 1 | 2 | 1 | 3 | 0 | 0 | 0 |
| 305 | 2 | 1 | 2 | 1 | 3 | 0 | 0 | 1 |
| 306 | 2 | 1 | 2 | 1 | 3 | 0 | 0 | 2 |
| 307 | 2 | 1 | 2 | 1 | 3 | 0 | 1 | 0 |
| 308 | 2 | 1 | 2 | 1 | 3 | 0 | 1 | 1 |
| 309 | 2 | 1 | 2 | 1 | 3 | 0 | 1 | 2 |
| 310 | 2 | 1 | 2 | 1 | 3 | 1 | 0 | 0 |
| 311 | 2 | 1 | 2 | 1 | 3 | 1 | 0 | 1 |
| 312 | 2 | 1 | 2 | 1 | 3 | 1 | 0 | 2 |
| 313 | 2 | 1 | 2 | 1 | 3 | 1 | 1 | 0 |
| 314 | 2 | 1 | 2 | 1 | 3 | 1 | 1 | 1 |
| 315 | 2 | 1 | 2 | 1 | 3 | 1 | 1 | 2 |
| 316 | 2 | 1 | 2 | 2 | 1 | 0 | 0 | 0 |
| 317 | 2 | 1 | 2 | 2 | 1 | 0 | 0 | 1 |
| 318 | 2 | 1 | 2 | 2 | 1 | 0 | 0 | 2 |
| 319 | 2 | 1 | 2 | 2 | 1 | 0 | 1 | 0 |
| 320 | 2 | 1 | 2 | 2 | 1 | 0 | 1 | 1 |
| 321 | 2 | 1 | 2 | 2 | 1 | 0 | 1 | 2 |
| 322 | 2 | 1 | 2 | 2 | 1 | 0 | 2 | 0 |
| 323 | 2 | 1 | 2 | 2 | 1 | 0 | 2 | 1 |
| 324 | 2 | 1 | 2 | 2 | 1 | 0 | 2 | 2 |
| 325 | 2 | 1 | 2 | 2 | 2 | 0 | 0 | 0 |
| 326 | 2 | 1 | 2 | 2 | 2 | 0 | 0 | 1 |
| 327 | 2 | 1 | 2 | 2 | 2 | 0 | 0 | 2 |
| 328 | 2 | 1 | 2 | 2 | 2 | 0 | 1 | 0 |
| 329 | 2 | 1 | 2 | 2 | 2 | 0 | 1 | 1 |
| 330 | 2 | 1 | 2 | 2 | 2 | 0 | 1 | 2 |
| 331 | 2 | 1 | 2 | 2 | 2 | 0 | 2 | 0 |
| 332 | 2 | 1 | 2 | 2 | 2 | 0 | 2 | 1 |
| 333 | 2 | 1 | 2 | 2 | 2 | 0 | 2 | 2 |
| 334 | 2 | 1 | 2 | 2 | 2 | 1 | 0 | 0 |
| 335 | 2 | 1 | 2 | 2 | 2 | 1 | 0 | 1 |
| 336 | 2 | 1 | 2 | 2 | 2 | 1 | 0 | 2 |
| 337 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 0 |
| 338 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 1 |
| 339 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 2 |
| 340 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 0 |
| 341 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 |
| 342 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 |
| 343 | 2 | 1 | 2 | 2 | 3 | 0 | 0 | 0 |
| 344 | 2 | 1 | 2 | 2 | 3 | 0 | 0 | 1 |
| 345 | 2 | 1 | 2 | 2 | 3 | 0 | 0 | 2 |
| 346 | 2 | 1 | 2 | 2 | 3 | 0 | 1 | 0 |
| 347 | 2 | 1 | 2 | 2 | 3 | 0 | 1 | 1 |
| 348 | 2 | 1 | 2 | 2 | 3 | 0 | 1 | 2 |
| 349 | 2 | 1 | 2 | 2 | 3 | 0 | 2 | 0 |
| 350 | 2 | 1 | 2 | 2 | 3 | 0 | 2 | 1 |
| 351 | 2 | 1 | 2 | 2 | 3 | 0 | 2 | 2 |
| 352 | 2 | 1 | 2 | 2 | 3 | 1 | 0 | 0 |
| 353 | 2 | 1 | 2 | 2 | 3 | 1 | 0 | 1 |
| 354 | 2 | 1 | 2 | 2 | 3 | 1 | 0 | 2 |
| 355 | 2 | 1 | 2 | 2 | 3 | 1 | 1 | 0 |
| 356 | 2 | 1 | 2 | 2 | 3 | 1 | 1 | 1 |
| 357 | 2 | 1 | 2 | 2 | 3 | 1 | 1 | 2 |
| 358 | 2 | 1 | 2 | 2 | 3 | 1 | 2 | 0 |
| 359 | 2 | 1 | 2 | 2 | 3 | 1 | 2 | 1 |
| 360 | 2 | 1 | 2 | 2 | 3 | 1 | 2 | 2 |
| 361 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 0 |
| 362 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| 363 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 2 |
| 364 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 3 |
| 365 | 2 | 1 | 3 | 0 | 2 | 0 | 0 | 0 |
| 366 | 2 | 1 | 3 | 0 | 2 | 0 | 0 | 1 |
| 367 | 2 | 1 | 3 | 0 | 2 | 0 | 0 | 2 |
| 368 | 2 | 1 | 3 | 0 | 2 | 0 | 0 | 3 |
| 369 | 2 | 1 | 3 | 0 | 2 | 1 | 0 | 0 |
| 370 | 2 | 1 | 3 | 0 | 2 | 1 | 0 | 1 |
| 371 | 2 | 1 | 3 | 0 | 2 | 1 | 0 | 2 |
| 372 | 2 | 1 | 3 | 0 | 2 | 1 | 0 | 3 |
| 373 | 2 | 1 | 3 | 0 | 3 | 0 | 0 | 0 |
| 374 | 2 | 1 | 3 | 0 | 3 | 0 | 0 | 1 |
| 375 | 2 | 1 | 3 | 0 | 3 | 0 | 0 | 2 |
| 376 | 2 | 1 | 3 | 0 | 3 | 0 | 0 | 3 |
| 377 | 2 | 1 | 3 | 0 | 3 | 1 | 0 | 0 |
| 378 | 2 | 1 | 3 | 0 | 3 | 1 | 0 | 1 |
| 379 | 2 | 1 | 3 | 0 | 3 | 1 | 0 | 2 |
| 380 | 2 | 1 | 3 | 0 | 3 | 1 | 0 | 3 |
| 381 | 2 | 1 | 3 | 1 | 1 | 0 | 0 | 0 |
| 382 | 2 | 1 | 3 | 1 | 1 | 0 | 0 | 1 |
| 383 | 2 | 1 | 3 | 1 | 1 | 0 | 0 | 2 |
| 384 | 2 | 1 | 3 | 1 | 1 | 0 | 0 | 3 |
| 385 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 0 |
| 386 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 1 |
| 387 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 2 |
| 388 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 3 |
| 389 | 2 | 1 | 3 | 1 | 2 | 0 | 0 | 0 |
| 390 | 2 | 1 | 3 | 1 | 2 | 0 | 0 | 1 |
| 391 | 2 | 1 | 3 | 1 | 2 | 0 | 0 | 2 |
| 392 | 2 | 1 | 3 | 1 | 2 | 0 | 0 | 3 |
| 393 | 2 | 1 | 3 | 1 | 2 | 0 | 1 | 0 |
| 394 | 2 | 1 | 3 | 1 | 2 | 0 | 1 | 1 |
| 395 | 2 | 1 | 3 | 1 | 2 | 0 | 1 | 2 |
| 396 | 2 | 1 | 3 | 1 | 2 | 0 | 1 | 3 |
| 397 | 2 | 1 | 3 | 1 | 2 | 1 | 0 | 0 |
| 398 | 2 | 1 | 3 | 1 | 2 | 1 | 0 | 1 |
| 399 | 2 | 1 | 3 | 1 | 2 | 1 | 0 | 2 |
| 400 | 2 | 1 | 3 | 1 | 2 | 1 | 0 | 3 |
| 401 | 2 | 1 | 3 | 1 | 2 | 1 | 1 | 0 |
| 402 | 2 | 1 | 3 | 1 | 2 | 1 | 1 | 1 |
| 403 | 2 | 1 | 3 | 1 | 2 | 1 | 1 | 2 |
| 404 | 2 | 1 | 3 | 1 | 2 | 1 | 1 | 3 |
| 405 | 2 | 1 | 3 | 1 | 3 | 0 | 0 | 0 |
| 406 | 2 | 1 | 3 | 1 | 3 | 0 | 0 | 1 |
| 407 | 2 | 1 | 3 | 1 | 3 | 0 | 0 | 2 |
| 408 | 2 | 1 | 3 | 1 | 3 | 0 | 0 | 3 |
| 409 | 2 | 1 | 3 | 1 | 3 | 0 | 1 | 0 |
| 410 | 2 | 1 | 3 | 1 | 3 | 0 | 1 | 1 |
| 411 | 2 | 1 | 3 | 1 | 3 | 0 | 1 | 2 |
| 412 | 2 | 1 | 3 | 1 | 3 | 0 | 1 | 3 |
| 413 | 2 | 1 | 3 | 1 | 3 | 1 | 0 | 0 |
| 414 | 2 | 1 | 3 | 1 | 3 | 1 | 0 | 1 |
| 415 | 2 | 1 | 3 | 1 | 3 | 1 | 0 | 2 |
| 416 | 2 | 1 | 3 | 1 | 3 | 1 | 0 | 3 |
| 417 | 2 | 1 | 3 | 1 | 3 | 1 | 1 | 0 |
| 418 | 2 | 1 | 3 | 1 | 3 | 1 | 1 | 1 |
| 419 | 2 | 1 | 3 | 1 | 3 | 1 | 1 | 2 |
| 420 | 2 | 1 | 3 | 1 | 3 | 1 | 1 | 3 |
| 421 | 2 | 1 | 3 | 2 | 1 | 0 | 0 | 0 |
| 422 | 2 | 1 | 3 | 2 | 1 | 0 | 0 | 1 |
| 423 | 2 | 1 | 3 | 2 | 1 | 0 | 0 | 2 |
| 424 | 2 | 1 | 3 | 2 | 1 | 0 | 0 | 3 |
| 425 | 2 | 1 | 3 | 2 | 1 | 0 | 1 | 0 |
| 426 | 2 | 1 | 3 | 2 | 1 | 0 | 1 | 1 |
| 427 | 2 | 1 | 3 | 2 | 1 | 0 | 1 | 2 |
| 428 | 2 | 1 | 3 | 2 | 1 | 0 | 1 | 3 |
| 429 | 2 | 1 | 3 | 2 | 1 | 0 | 2 | 0 |
| 430 | 2 | 1 | 3 | 2 | 1 | 0 | 2 | 1 |
| 431 | 2 | 1 | 3 | 2 | 1 | 0 | 2 | 2 |
| 432 | 2 | 1 | 3 | 2 | 1 | 0 | 2 | 3 |
| 433 | 2 | 1 | 3 | 2 | 2 | 0 | 0 | 0 |
| 434 | 2 | 1 | 3 | 2 | 2 | 0 | 0 | 1 |
| 435 | 2 | 1 | 3 | 2 | 2 | 0 | 0 | 2 |
| 436 | 2 | 1 | 3 | 2 | 2 | 0 | 0 | 3 |
| 437 | 2 | 1 | 3 | 2 | 2 | 0 | 1 | 0 |
| 438 | 2 | 1 | 3 | 2 | 2 | 0 | 1 | 1 |
| 439 | 2 | 1 | 3 | 2 | 2 | 0 | 1 | 2 |
| 440 | 2 | 1 | 3 | 2 | 2 | 0 | 1 | 3 |
| 441 | 2 | 1 | 3 | 2 | 2 | 0 | 2 | 0 |
| 442 | 2 | 1 | 3 | 2 | 2 | 0 | 2 | 1 |
| 443 | 2 | 1 | 3 | 2 | 2 | 0 | 2 | 2 |
| 444 | 2 | 1 | 3 | 2 | 2 | 0 | 2 | 3 |
| 445 | 2 | 1 | 3 | 2 | 2 | 1 | 0 | 0 |
| 446 | 2 | 1 | 3 | 2 | 2 | 1 | 0 | 1 |
| 447 | 2 | 1 | 3 | 2 | 2 | 1 | 0 | 2 |
| 448 | 2 | 1 | 3 | 2 | 2 | 1 | 0 | 3 |
| 449 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 0 |
| 450 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 1 |
| 451 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 2 |
| 452 | 2 | 1 | 3 | 2 | 2 | 1 | 1 | 3 |
| 453 | 2 | 1 | 3 | 2 | 2 | 1 | 2 | 0 |
| 454 | 2 | 1 | 3 | 2 | 2 | 1 | 2 | 1 |
| 455 | 2 | 1 | 3 | 2 | 2 | 1 | 2 | 2 |
| 456 | 2 | 1 | 3 | 2 | 2 | 1 | 2 | 3 |
| 457 | 2 | 1 | 3 | 2 | 3 | 0 | 0 | 0 |
| 458 | 2 | 1 | 3 | 2 | 3 | 0 | 0 | 1 |
| 459 | 2 | 1 | 3 | 2 | 3 | 0 | 0 | 2 |
| 460 | 2 | 1 | 3 | 2 | 3 | 0 | 0 | 3 |
| 461 | 2 | 1 | 3 | 2 | 3 | 0 | 1 | 0 |
| 462 | 2 | 1 | 3 | 2 | 3 | 0 | 1 | 1 |
| 463 | 2 | 1 | 3 | 2 | 3 | 0 | 1 | 2 |
| 464 | 2 | 1 | 3 | 2 | 3 | 0 | 1 | 3 |
| 465 | 2 | 1 | 3 | 2 | 3 | 0 | 2 | 0 |
| 466 | 2 | 1 | 3 | 2 | 3 | 0 | 2 | 1 |
| 467 | 2 | 1 | 3 | 2 | 3 | 0 | 2 | 2 |
| 468 | 2 | 1 | 3 | 2 | 3 | 0 | 2 | 3 |
| 469 | 2 | 1 | 3 | 2 | 3 | 1 | 0 | 0 |
| 470 | 2 | 1 | 3 | 2 | 3 | 1 | 0 | 1 |
| 471 | 2 | 1 | 3 | 2 | 3 | 1 | 0 | 2 |
| 472 | 2 | 1 | 3 | 2 | 3 | 1 | 0 | 3 |
| 473 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 0 |
| 474 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 1 |
| 475 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 2 |
| 476 | 2 | 1 | 3 | 2 | 3 | 1 | 1 | 3 |
| 477 | 2 | 1 | 3 | 2 | 3 | 1 | 2 | 0 |
| 478 | 2 | 1 | 3 | 2 | 3 | 1 | 2 | 1 |
| 479 | 2 | 1 | 3 | 2 | 3 | 1 | 2 | 2 |
| 480 | 2 | 1 | 3 | 2 | 3 | 1 | 2 | 3 |
| 481 | 2 | 1 | 3 | 3 | 1 | 0 | 0 | 0 |
| 482 | 2 | 1 | 3 | 3 | 1 | 0 | 0 | 1 |
| 483 | 2 | 1 | 3 | 3 | 1 | 0 | 0 | 2 |
| 484 | 2 | 1 | 3 | 3 | 1 | 0 | 0 | 3 |
| 485 | 2 | 1 | 3 | 3 | 1 | 0 | 1 | 0 |
| 486 | 2 | 1 | 3 | 3 | 1 | 0 | 1 | 1 |
| 487 | 2 | 1 | 3 | 3 | 1 | 0 | 1 | 2 |
| 488 | 2 | 1 | 3 | 3 | 1 | 0 | 1 | 3 |
| 489 | 2 | 1 | 3 | 3 | 1 | 0 | 2 | 0 |
| 490 | 2 | 1 | 3 | 3 | 1 | 0 | 2 | 1 |
| 491 | 2 | 1 | 3 | 3 | 1 | 0 | 2 | 2 |
| 492 | 2 | 1 | 3 | 3 | 1 | 0 | 2 | 3 |
| 493 | 2 | 1 | 3 | 3 | 2 | 0 | 0 | 0 |
| 494 | 2 | 1 | 3 | 3 | 2 | 0 | 0 | 1 |
| 495 | 2 | 1 | 3 | 3 | 2 | 0 | 0 | 2 |
| 496 | 2 | 1 | 3 | 3 | 2 | 0 | 0 | 3 |
| 497 | 2 | 1 | 3 | 3 | 2 | 0 | 1 | 0 |
| 498 | 2 | 1 | 3 | 3 | 2 | 0 | 1 | 1 |
| 499 | 2 | 1 | 3 | 3 | 2 | 0 | 1 | 2 |
| 500 | 2 | 1 | 3 | 3 | 2 | 0 | 1 | 3 |
| 501 | 2 | 1 | 3 | 3 | 2 | 0 | 2 | 0 |
| 502 | 2 | 1 | 3 | 3 | 2 | 0 | 2 | 1 |
| 503 | 2 | 1 | 3 | 3 | 2 | 0 | 2 | 2 |
| 504 | 2 | 1 | 3 | 3 | 2 | 0 | 2 | 3 |
| 505 | 2 | 1 | 3 | 3 | 2 | 1 | 0 | 0 |
| 506 | 2 | 1 | 3 | 3 | 2 | 1 | 0 | 1 |
| 507 | 2 | 1 | 3 | 3 | 2 | 1 | 0 | 2 |
| 508 | 2 | 1 | 3 | 3 | 2 | 1 | 0 | 3 |
| 509 | 2 | 1 | 3 | 3 | 2 | 1 | 1 | 0 |
| 510 | 2 | 1 | 3 | 3 | 2 | 1 | 1 | 1 |
| 511 | 2 | 1 | 3 | 3 | 2 | 1 | 1 | 2 |
| 512 | 2 | 1 | 3 | 3 | 2 | 1 | 1 | 3 |
| 513 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 0 |
| 514 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 1 |
| 515 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 2 |
| 516 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 3 |
| 517 | 2 | 1 | 3 | 3 | 2 | 1 | 3 | 0 |
| 518 | 2 | 1 | 3 | 3 | 2 | 1 | 3 | 1 |
| 519 | 2 | 1 | 3 | 3 | 2 | 1 | 3 | 2 |
| 520 | 2 | 1 | 3 | 3 | 2 | 1 | 3 | 3 |
| 521 | 2 | 1 | 3 | 3 | 3 | 0 | 0 | 0 |
| 522 | 2 | 1 | 3 | 3 | 3 | 0 | 0 | 1 |
| 523 | 2 | 1 | 3 | 3 | 3 | 0 | 0 | 2 |
| 524 | 2 | 1 | 3 | 3 | 3 | 0 | 0 | 3 |
| 525 | 2 | 1 | 3 | 3 | 3 | 0 | 1 | 0 |
| 526 | 2 | 1 | 3 | 3 | 3 | 0 | 1 | 1 |
| 527 | 2 | 1 | 3 | 3 | 3 | 0 | 1 | 2 |
| 528 | 2 | 1 | 3 | 3 | 3 | 0 | 1 | 3 |
| 529 | 2 | 1 | 3 | 3 | 3 | 0 | 2 | 0 |
| 530 | 2 | 1 | 3 | 3 | 3 | 0 | 2 | 1 |
| 531 | 2 | 1 | 3 | 3 | 3 | 0 | 2 | 2 |
| 532 | 2 | 1 | 3 | 3 | 3 | 0 | 2 | 3 |
| 533 | 2 | 1 | 3 | 3 | 3 | 1 | 0 | 0 |
| 534 | 2 | 1 | 3 | 3 | 3 | 1 | 0 | 1 |
| 535 | 2 | 1 | 3 | 3 | 3 | 1 | 0 | 2 |
| 536 | 2 | 1 | 3 | 3 | 3 | 1 | 0 | 3 |
| 537 | 2 | 1 | 3 | 3 | 3 | 1 | 1 | 0 |
| 538 | 2 | 1 | 3 | 3 | 3 | 1 | 1 | 1 |
| 539 | 2 | 1 | 3 | 3 | 3 | 1 | 1 | 2 |
| 540 | 2 | 1 | 3 | 3 | 3 | 1 | 1 | 3 |
| 541 | 2 | 1 | 3 | 3 | 3 | 1 | 2 | 0 |
| 542 | 2 | 1 | 3 | 3 | 3 | 1 | 2 | 1 |
| 543 | 2 | 1 | 3 | 3 | 3 | 1 | 2 | 2 |
| 544 | 2 | 1 | 3 | 3 | 3 | 1 | 2 | 3 |
| 545 | 2 | 1 | 3 | 3 | 3 | 1 | 3 | 0 |
| 546 | 2 | 1 | 3 | 3 | 3 | 1 | 3 | 1 |
| 547 | 2 | 1 | 3 | 3 | 3 | 1 | 3 | 2 |
| 548 | 2 | 1 | 3 | 3 | 3 | 1 | 3 | 3 |
| 549 | 3 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 550 | 3 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| 551 | 3 | 0 | 1 | 0 | 2 | 0 | 0 | 0 |
| 552 | 3 | 0 | 1 | 0 | 2 | 0 | 0 | 1 |
| 553 | 3 | 0 | 1 | 0 | 2 | 1 | 0 | 0 |
| 554 | 3 | 0 | 1 | 0 | 2 | 1 | 0 | 1 |
| 555 | 3 | 0 | 1 | 0 | 3 | 0 | 0 | 0 |
| 556 | 3 | 0 | 1 | 0 | 3 | 0 | 0 | 1 |
| 557 | 3 | 0 | 1 | 0 | 3 | 1 | 0 | 0 |
| 558 | 3 | 0 | 1 | 0 | 3 | 1 | 0 | 1 |
| 559 | 3 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| 560 | 3 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 561 | 3 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| 562 | 3 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 563 | 3 | 0 | 1 | 1 | 2 | 0 | 0 | 0 |
| 564 | 3 | 0 | 1 | 1 | 2 | 0 | 0 | 1 |
| 565 | 3 | 0 | 1 | 1 | 2 | 0 | 1 | 0 |
| 566 | 3 | 0 | 1 | 1 | 2 | 0 | 1 | 1 |
| 567 | 3 | 0 | 1 | 1 | 2 | 1 | 0 | 0 |
| 568 | 3 | 0 | 1 | 1 | 2 | 1 | 0 | 1 |
| 569 | 3 | 0 | 1 | 1 | 2 | 1 | 1 | 0 |
| 570 | 3 | 0 | 1 | 1 | 2 | 1 | 1 | 1 |
| 571 | 3 | 0 | 1 | 1 | 3 | 0 | 0 | 0 |
| 572 | 3 | 0 | 1 | 1 | 3 | 0 | 0 | 1 |
| 573 | 3 | 0 | 1 | 1 | 3 | 0 | 1 | 0 |
| 574 | 3 | 0 | 1 | 1 | 3 | 0 | 1 | 1 |
| 575 | 3 | 0 | 1 | 1 | 3 | 1 | 0 | 0 |
| 576 | 3 | 0 | 1 | 1 | 3 | 1 | 0 | 1 |
| 577 | 3 | 0 | 1 | 1 | 3 | 1 | 1 | 0 |
| 578 | 3 | 0 | 1 | 1 | 3 | 1 | 1 | 1 |
| 579 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| 580 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| 581 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 2 |
| 582 | 3 | 0 | 2 | 0 | 2 | 0 | 0 | 0 |
| 583 | 3 | 0 | 2 | 0 | 2 | 0 | 0 | 1 |
| 584 | 3 | 0 | 2 | 0 | 2 | 0 | 0 | 2 |
| 585 | 3 | 0 | 2 | 0 | 2 | 1 | 0 | 0 |
| 586 | 3 | 0 | 2 | 0 | 2 | 1 | 0 | 1 |
| 587 | 3 | 0 | 2 | 0 | 2 | 1 | 0 | 2 |
| 588 | 3 | 0 | 2 | 0 | 3 | 0 | 0 | 0 |
| 589 | 3 | 0 | 2 | 0 | 3 | 0 | 0 | 1 |
| 590 | 3 | 0 | 2 | 0 | 3 | 0 | 0 | 2 |
| 591 | 3 | 0 | 2 | 0 | 3 | 1 | 0 | 0 |
| 592 | 3 | 0 | 2 | 0 | 3 | 1 | 0 | 1 |
| 593 | 3 | 0 | 2 | 0 | 3 | 1 | 0 | 2 |
| 594 | 3 | 0 | 2 | 1 | 1 | 0 | 0 | 0 |
| 595 | 3 | 0 | 2 | 1 | 1 | 0 | 0 | 1 |
| 596 | 3 | 0 | 2 | 1 | 1 | 0 | 0 | 2 |
| 597 | 3 | 0 | 2 | 1 | 1 | 0 | 1 | 0 |
| 598 | 3 | 0 | 2 | 1 | 1 | 0 | 1 | 1 |
| 599 | 3 | 0 | 2 | 1 | 1 | 0 | 1 | 2 |
| 600 | 3 | 0 | 2 | 1 | 2 | 0 | 0 | 0 |
| 601 | 3 | 0 | 2 | 1 | 2 | 0 | 0 | 1 |
| 602 | 3 | 0 | 2 | 1 | 2 | 0 | 0 | 2 |
| 603 | 3 | 0 | 2 | 1 | 2 | 0 | 1 | 0 |
| 604 | 3 | 0 | 2 | 1 | 2 | 0 | 1 | 1 |
| 605 | 3 | 0 | 2 | 1 | 2 | 0 | 1 | 2 |
| 606 | 3 | 0 | 2 | 1 | 2 | 1 | 0 | 0 |
| 607 | 3 | 0 | 2 | 1 | 2 | 1 | 0 | 1 |
| 608 | 3 | 0 | 2 | 1 | 2 | 1 | 0 | 2 |
| 609 | 3 | 0 | 2 | 1 | 2 | 1 | 1 | 0 |
| 610 | 3 | 0 | 2 | 1 | 2 | 1 | 1 | 1 |
| 611 | 3 | 0 | 2 | 1 | 2 | 1 | 1 | 2 |
| 612 | 3 | 0 | 2 | 1 | 3 | 0 | 0 | 0 |
| 613 | 3 | 0 | 2 | 1 | 3 | 0 | 0 | 1 |
| 614 | 3 | 0 | 2 | 1 | 3 | 0 | 0 | 2 |
| 615 | 3 | 0 | 2 | 1 | 3 | 0 | 1 | 0 |
| 616 | 3 | 0 | 2 | 1 | 3 | 0 | 1 | 1 |
| 617 | 3 | 0 | 2 | 1 | 3 | 0 | 1 | 2 |
| 618 | 3 | 0 | 2 | 1 | 3 | 1 | 0 | 0 |
| 619 | 3 | 0 | 2 | 1 | 3 | 1 | 0 | 1 |
| 620 | 3 | 0 | 2 | 1 | 3 | 1 | 0 | 2 |
| 621 | 3 | 0 | 2 | 1 | 3 | 1 | 1 | 0 |
| 622 | 3 | 0 | 2 | 1 | 3 | 1 | 1 | 1 |
| 623 | 3 | 0 | 2 | 1 | 3 | 1 | 1 | 2 |
| 624 | 3 | 0 | 2 | 2 | 1 | 0 | 0 | 0 |
| 625 | 3 | 0 | 2 | 2 | 1 | 0 | 0 | 1 |
| 626 | 3 | 0 | 2 | 2 | 1 | 0 | 0 | 2 |
| 627 | 3 | 0 | 2 | 2 | 1 | 0 | 1 | 0 |
| 628 | 3 | 0 | 2 | 2 | 1 | 0 | 1 | 1 |
| 629 | 3 | 0 | 2 | 2 | 1 | 0 | 1 | 2 |
| 630 | 3 | 0 | 2 | 2 | 1 | 0 | 2 | 0 |
| 631 | 3 | 0 | 2 | 2 | 1 | 0 | 2 | 1 |
| 632 | 3 | 0 | 2 | 2 | 1 | 0 | 2 | 2 |
| 633 | 3 | 0 | 2 | 2 | 2 | 0 | 0 | 0 |
| 634 | 3 | 0 | 2 | 2 | 2 | 0 | 0 | 1 |
| 635 | 3 | 0 | 2 | 2 | 2 | 0 | 0 | 2 |
| 636 | 3 | 0 | 2 | 2 | 2 | 0 | 1 | 0 |
| 637 | 3 | 0 | 2 | 2 | 2 | 0 | 1 | 1 |
| 638 | 3 | 0 | 2 | 2 | 2 | 0 | 1 | 2 |
| 639 | 3 | 0 | 2 | 2 | 2 | 0 | 2 | 0 |
| 640 | 3 | 0 | 2 | 2 | 2 | 0 | 2 | 1 |
| 641 | 3 | 0 | 2 | 2 | 2 | 0 | 2 | 2 |
| 642 | 3 | 0 | 2 | 2 | 2 | 1 | 0 | 0 |
| 643 | 3 | 0 | 2 | 2 | 2 | 1 | 0 | 1 |
| 644 | 3 | 0 | 2 | 2 | 2 | 1 | 0 | 2 |
| 645 | 3 | 0 | 2 | 2 | 2 | 1 | 1 | 0 |
| 646 | 3 | 0 | 2 | 2 | 2 | 1 | 1 | 1 |
| 647 | 3 | 0 | 2 | 2 | 2 | 1 | 1 | 2 |
| 648 | 3 | 0 | 2 | 2 | 2 | 1 | 2 | 0 |
| 649 | 3 | 0 | 2 | 2 | 2 | 1 | 2 | 1 |
| 650 | 3 | 0 | 2 | 2 | 2 | 1 | 2 | 2 |
| 651 | 3 | 0 | 2 | 2 | 3 | 0 | 0 | 0 |
| 652 | 3 | 0 | 2 | 2 | 3 | 0 | 0 | 1 |
| 653 | 3 | 0 | 2 | 2 | 3 | 0 | 0 | 2 |
| 654 | 3 | 0 | 2 | 2 | 3 | 0 | 1 | 0 |
| 655 | 3 | 0 | 2 | 2 | 3 | 0 | 1 | 1 |
| 656 | 3 | 0 | 2 | 2 | 3 | 0 | 1 | 2 |
| 657 | 3 | 0 | 2 | 2 | 3 | 0 | 2 | 0 |
| 658 | 3 | 0 | 2 | 2 | 3 | 0 | 2 | 1 |
| 659 | 3 | 0 | 2 | 2 | 3 | 0 | 2 | 2 |
| 660 | 3 | 0 | 2 | 2 | 3 | 1 | 0 | 0 |
| 661 | 3 | 0 | 2 | 2 | 3 | 1 | 0 | 1 |
| 662 | 3 | 0 | 2 | 2 | 3 | 1 | 0 | 2 |
| 663 | 3 | 0 | 2 | 2 | 3 | 1 | 1 | 0 |
| 664 | 3 | 0 | 2 | 2 | 3 | 1 | 1 | 1 |
| 665 | 3 | 0 | 2 | 2 | 3 | 1 | 1 | 2 |
| 666 | 3 | 0 | 2 | 2 | 3 | 1 | 2 | 0 |
| 667 | 3 | 0 | 2 | 2 | 3 | 1 | 2 | 1 |
| 668 | 3 | 0 | 2 | 2 | 3 | 1 | 2 | 2 |
| 669 | 3 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| 670 | 3 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| 671 | 3 | 1 | 1 | 0 | 2 | 0 | 0 | 0 |
| 672 | 3 | 1 | 1 | 0 | 2 | 0 | 0 | 1 |
| 673 | 3 | 1 | 1 | 0 | 2 | 1 | 0 | 0 |
| 674 | 3 | 1 | 1 | 0 | 2 | 1 | 0 | 1 |
| 675 | 3 | 1 | 1 | 0 | 3 | 0 | 0 | 0 |
| 676 | 3 | 1 | 1 | 0 | 3 | 0 | 0 | 1 |
| 677 | 3 | 1 | 1 | 0 | 3 | 1 | 0 | 0 |
| 678 | 3 | 1 | 1 | 0 | 3 | 1 | 0 | 1 |
| 679 | 3 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 680 | 3 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 681 | 3 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
| 682 | 3 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |
| 683 | 3 | 1 | 1 | 1 | 2 | 0 | 0 | 0 |
| 684 | 3 | 1 | 1 | 1 | 2 | 0 | 0 | 1 |
| 685 | 3 | 1 | 1 | 1 | 2 | 0 | 1 | 0 |
| 686 | 3 | 1 | 1 | 1 | 2 | 0 | 1 | 1 |
| 687 | 3 | 1 | 1 | 1 | 2 | 1 | 0 | 0 |
| 688 | 3 | 1 | 1 | 1 | 2 | 1 | 0 | 1 |
| 689 | 3 | 1 | 1 | 1 | 2 | 1 | 1 | 0 |
| 690 | 3 | 1 | 1 | 1 | 2 | 1 | 1 | 1 |
| 691 | 3 | 1 | 1 | 1 | 3 | 0 | 0 | 0 |
| 692 | 3 | 1 | 1 | 1 | 3 | 0 | 0 | 1 |
| 693 | 3 | 1 | 1 | 1 | 3 | 0 | 1 | 0 |
| 694 | 3 | 1 | 1 | 1 | 3 | 0 | 1 | 1 |
| 695 | 3 | 1 | 1 | 1 | 3 | 1 | 0 | 0 |
| 696 | 3 | 1 | 1 | 1 | 3 | 1 | 0 | 1 |
| 697 | 3 | 1 | 1 | 1 | 3 | 1 | 1 | 0 |
| 698 | 3 | 1 | 1 | 1 | 3 | 1 | 1 | 1 |
| 699 | 3 | 1 | 2 | 0 | 1 | 0 | 0 | 0 |
| 700 | 3 | 1 | 2 | 0 | 1 | 0 | 0 | 1 |
| 701 | 3 | 1 | 2 | 0 | 1 | 0 | 0 | 2 |
| 702 | 3 | 1 | 2 | 0 | 2 | 0 | 0 | 0 |
| 703 | 3 | 1 | 2 | 0 | 2 | 0 | 0 | 1 |
| 704 | 3 | 1 | 2 | 0 | 2 | 0 | 0 | 2 |
| 705 | 3 | 1 | 2 | 0 | 2 | 1 | 0 | 0 |
| 706 | 3 | 1 | 2 | 0 | 2 | 1 | 0 | 1 |
| 707 | 3 | 1 | 2 | 0 | 2 | 1 | 0 | 2 |
| 708 | 3 | 1 | 2 | 0 | 3 | 0 | 0 | 0 |
| 709 | 3 | 1 | 2 | 0 | 3 | 0 | 0 | 1 |
| 710 | 3 | 1 | 2 | 0 | 3 | 0 | 0 | 2 |
| 711 | 3 | 1 | 2 | 0 | 3 | 1 | 0 | 0 |
| 712 | 3 | 1 | 2 | 0 | 3 | 1 | 0 | 1 |
| 713 | 3 | 1 | 2 | 0 | 3 | 1 | 0 | 2 |
| 714 | 3 | 1 | 2 | 1 | 1 | 0 | 0 | 0 |
| 715 | 3 | 1 | 2 | 1 | 1 | 0 | 0 | 1 |
| 716 | 3 | 1 | 2 | 1 | 1 | 0 | 0 | 2 |
| 717 | 3 | 1 | 2 | 1 | 1 | 0 | 1 | 0 |
| 718 | 3 | 1 | 2 | 1 | 1 | 0 | 1 | 1 |
| 719 | 3 | 1 | 2 | 1 | 1 | 0 | 1 | 2 |
| 720 | 3 | 1 | 2 | 1 | 2 | 0 | 0 | 0 |
| 721 | 3 | 1 | 2 | 1 | 2 | 0 | 0 | 1 |
| 722 | 3 | 1 | 2 | 1 | 2 | 0 | 0 | 2 |
| 723 | 3 | 1 | 2 | 1 | 2 | 0 | 1 | 0 |
| 724 | 3 | 1 | 2 | 1 | 2 | 0 | 1 | 1 |
| 725 | 3 | 1 | 2 | 1 | 2 | 0 | 1 | 2 |
| 726 | 3 | 1 | 2 | 1 | 2 | 1 | 0 | 0 |
| 727 | 3 | 1 | 2 | 1 | 2 | 1 | 0 | 1 |
| 728 | 3 | 1 | 2 | 1 | 2 | 1 | 0 | 2 |
| 729 | 3 | 1 | 2 | 1 | 2 | 1 | 1 | 0 |
| 730 | 3 | 1 | 2 | 1 | 2 | 1 | 1 | 1 |
| 731 | 3 | 1 | 2 | 1 | 2 | 1 | 1 | 2 |
| 732 | 3 | 1 | 2 | 1 | 3 | 0 | 0 | 0 |
| 733 | 3 | 1 | 2 | 1 | 3 | 0 | 0 | 1 |
| 734 | 3 | 1 | 2 | 1 | 3 | 0 | 0 | 2 |
| 735 | 3 | 1 | 2 | 1 | 3 | 0 | 1 | 0 |
| 736 | 3 | 1 | 2 | 1 | 3 | 0 | 1 | 1 |
| 737 | 3 | 1 | 2 | 1 | 3 | 0 | 1 | 2 |
| 738 | 3 | 1 | 2 | 1 | 3 | 1 | 0 | 0 |
| 739 | 3 | 1 | 2 | 1 | 3 | 1 | 0 | 1 |
| 740 | 3 | 1 | 2 | 1 | 3 | 1 | 0 | 2 |
| 741 | 3 | 1 | 2 | 1 | 3 | 1 | 1 | 0 |
| 742 | 3 | 1 | 2 | 1 | 3 | 1 | 1 | 1 |
| 743 | 3 | 1 | 2 | 1 | 3 | 1 | 1 | 2 |
| 744 | 3 | 1 | 2 | 2 | 1 | 0 | 0 | 0 |
| 745 | 3 | 1 | 2 | 2 | 1 | 0 | 0 | 1 |
| 746 | 3 | 1 | 2 | 2 | 1 | 0 | 0 | 2 |
| 747 | 3 | 1 | 2 | 2 | 1 | 0 | 1 | 0 |
| 748 | 3 | 1 | 2 | 2 | 1 | 0 | 1 | 1 |
| 749 | 3 | 1 | 2 | 2 | 1 | 0 | 1 | 2 |
| 750 | 3 | 1 | 2 | 2 | 1 | 0 | 2 | 0 |
| 751 | 3 | 1 | 2 | 2 | 1 | 0 | 2 | 1 |
| 752 | 3 | 1 | 2 | 2 | 1 | 0 | 2 | 2 |
| 753 | 3 | 1 | 2 | 2 | 2 | 0 | 0 | 0 |
| 754 | 3 | 1 | 2 | 2 | 2 | 0 | 0 | 1 |
| 755 | 3 | 1 | 2 | 2 | 2 | 0 | 0 | 2 |
| 756 | 3 | 1 | 2 | 2 | 2 | 0 | 1 | 0 |
| 757 | 3 | 1 | 2 | 2 | 2 | 0 | 1 | 1 |
| 758 | 3 | 1 | 2 | 2 | 2 | 0 | 1 | 2 |
| 759 | 3 | 1 | 2 | 2 | 2 | 0 | 2 | 0 |
| 760 | 3 | 1 | 2 | 2 | 2 | 0 | 2 | 1 |
| 761 | 3 | 1 | 2 | 2 | 2 | 0 | 2 | 2 |
| 762 | 3 | 1 | 2 | 2 | 2 | 1 | 0 | 0 |
| 763 | 3 | 1 | 2 | 2 | 2 | 1 | 0 | 1 |
| 764 | 3 | 1 | 2 | 2 | 2 | 1 | 0 | 2 |
| 765 | 3 | 1 | 2 | 2 | 2 | 1 | 1 | 0 |
| 766 | 3 | 1 | 2 | 2 | 2 | 1 | 1 | 1 |
| 767 | 3 | 1 | 2 | 2 | 2 | 1 | 1 | 2 |
| 768 | 3 | 1 | 2 | 2 | 2 | 1 | 2 | 0 |
| 769 | 3 | 1 | 2 | 2 | 2 | 1 | 2 | 1 |
| 770 | 3 | 1 | 2 | 2 | 2 | 1 | 2 | 2 |
| 771 | 3 | 1 | 2 | 2 | 3 | 0 | 0 | 0 |
| 772 | 3 | 1 | 2 | 2 | 3 | 0 | 0 | 1 |
| 773 | 3 | 1 | 2 | 2 | 3 | 0 | 0 | 2 |
| 774 | 3 | 1 | 2 | 2 | 3 | 0 | 1 | 0 |
| 775 | 3 | 1 | 2 | 2 | 3 | 0 | 1 | 1 |
| 776 | 3 | 1 | 2 | 2 | 3 | 0 | 1 | 2 |
| 777 | 3 | 1 | 2 | 2 | 3 | 0 | 2 | 0 |
| 778 | 3 | 1 | 2 | 2 | 3 | 0 | 2 | 1 |
| 779 | 3 | 1 | 2 | 2 | 3 | 0 | 2 | 2 |
| 780 | 3 | 1 | 2 | 2 | 3 | 1 | 0 | 0 |
| 781 | 3 | 1 | 2 | 2 | 3 | 1 | 0 | 1 |
| 782 | 3 | 1 | 2 | 2 | 3 | 1 | 0 | 2 |
| 783 | 3 | 1 | 2 | 2 | 3 | 1 | 1 | 0 |
| 784 | 3 | 1 | 2 | 2 | 3 | 1 | 1 | 1 |
| 785 | 3 | 1 | 2 | 2 | 3 | 1 | 1 | 2 |
| 786 | 3 | 1 | 2 | 2 | 3 | 1 | 2 | 0 |
| 787 | 3 | 1 | 2 | 2 | 3 | 1 | 2 | 1 |
| 788 | 3 | 1 | 2 | 2 | 3 | 1 | 2 | 2 |
| 789 | 3 | 1 | 3 | 0 | 1 | 0 | 0 | 0 |
| 790 | 3 | 1 | 3 | 0 | 1 | 0 | 0 | 1 |
| 791 | 3 | 1 | 3 | 0 | 1 | 0 | 0 | 2 |
| 792 | 3 | 1 | 3 | 0 | 1 | 0 | 0 | 3 |
| 793 | 3 | 1 | 3 | 0 | 2 | 0 | 0 | 0 |
| 794 | 3 | 1 | 3 | 0 | 2 | 0 | 0 | 1 |
| 795 | 3 | 1 | 3 | 0 | 2 | 0 | 0 | 2 |
| 796 | 3 | 1 | 3 | 0 | 2 | 0 | 0 | 3 |
| 797 | 3 | 1 | 3 | 0 | 2 | 1 | 0 | 0 |
| 798 | 3 | 1 | 3 | 0 | 2 | 1 | 0 | 1 |
| 799 | 3 | 1 | 3 | 0 | 2 | 1 | 0 | 2 |
| 800 | 3 | 1 | 3 | 0 | 2 | 1 | 0 | 3 |
| 801 | 3 | 1 | 3 | 0 | 3 | 0 | 0 | 0 |
| 802 | 3 | 1 | 3 | 0 | 3 | 0 | 0 | 1 |
| 803 | 3 | 1 | 3 | 0 | 3 | 0 | 0 | 2 |
| 804 | 3 | 1 | 3 | 0 | 3 | 0 | 0 | 3 |
| 805 | 3 | 1 | 3 | 0 | 3 | 1 | 0 | 0 |
| 806 | 3 | 1 | 3 | 0 | 3 | 1 | 0 | 1 |
| 807 | 3 | 1 | 3 | 0 | 3 | 1 | 0 | 2 |
| 808 | 3 | 1 | 3 | 0 | 3 | 1 | 0 | 3 |
| 809 | 3 | 1 | 3 | 1 | 1 | 0 | 0 | 0 |
| 810 | 3 | 1 | 3 | 1 | 1 | 0 | 0 | 1 |
| 811 | 3 | 1 | 3 | 1 | 1 | 0 | 0 | 2 |
| 812 | 3 | 1 | 3 | 1 | 1 | 0 | 0 | 3 |
| 813 | 3 | 1 | 3 | 1 | 1 | 0 | 1 | 0 |
| 814 | 3 | 1 | 3 | 1 | 1 | 0 | 1 | 1 |
| 815 | 3 | 1 | 3 | 1 | 1 | 0 | 1 | 2 |
| 816 | 3 | 1 | 3 | 1 | 1 | 0 | 1 | 3 |
| 817 | 3 | 1 | 3 | 1 | 2 | 0 | 0 | 0 |
| 818 | 3 | 1 | 3 | 1 | 2 | 0 | 0 | 1 |
| 819 | 3 | 1 | 3 | 1 | 2 | 0 | 0 | 2 |
| 820 | 3 | 1 | 3 | 1 | 2 | 0 | 0 | 3 |
| 821 | 3 | 1 | 3 | 1 | 2 | 0 | 1 | 0 |
| 822 | 3 | 1 | 3 | 1 | 2 | 0 | 1 | 1 |
| 823 | 3 | 1 | 3 | 1 | 2 | 0 | 1 | 2 |
| 824 | 3 | 1 | 3 | 1 | 2 | 0 | 1 | 3 |
| 825 | 3 | 1 | 3 | 1 | 2 | 1 | 0 | 0 |
| 826 | 3 | 1 | 3 | 1 | 2 | 1 | 0 | 1 |
| 827 | 3 | 1 | 3 | 1 | 2 | 1 | 0 | 2 |
| 828 | 3 | 1 | 3 | 1 | 2 | 1 | 0 | 3 |
| 829 | 3 | 1 | 3 | 1 | 2 | 1 | 1 | 0 |
| 830 | 3 | 1 | 3 | 1 | 2 | 1 | 1 | 1 |
| 831 | 3 | 1 | 3 | 1 | 2 | 1 | 1 | 2 |
| 832 | 3 | 1 | 3 | 1 | 2 | 1 | 1 | 3 |
| 833 | 3 | 1 | 3 | 1 | 3 | 0 | 0 | 0 |
| 834 | 3 | 1 | 3 | 1 | 3 | 0 | 0 | 1 |
| 835 | 3 | 1 | 3 | 1 | 3 | 0 | 0 | 2 |
| 836 | 3 | 1 | 3 | 1 | 3 | 0 | 0 | 3 |
| 837 | 3 | 1 | 3 | 1 | 3 | 0 | 1 | 0 |
| 838 | 3 | 1 | 3 | 1 | 3 | 0 | 1 | 1 |
| 839 | 3 | 1 | 3 | 1 | 3 | 0 | 1 | 2 |
| 840 | 3 | 1 | 3 | 1 | 3 | 0 | 1 | 3 |
| 841 | 3 | 1 | 3 | 1 | 3 | 1 | 0 | 0 |
| 842 | 3 | 1 | 3 | 1 | 3 | 1 | 0 | 1 |
| 843 | 3 | 1 | 3 | 1 | 3 | 1 | 0 | 2 |
| 844 | 3 | 1 | 3 | 1 | 3 | 1 | 0 | 3 |
| 845 | 3 | 1 | 3 | 1 | 3 | 1 | 1 | 0 |
| 846 | 3 | 1 | 3 | 1 | 3 | 1 | 1 | 1 |
| 847 | 3 | 1 | 3 | 1 | 3 | 1 | 1 | 2 |
| 848 | 3 | 1 | 3 | 1 | 3 | 1 | 1 | 3 |
| 849 | 3 | 1 | 3 | 2 | 1 | 0 | 0 | 0 |
| 850 | 3 | 1 | 3 | 2 | 1 | 0 | 0 | 1 |
| 851 | 3 | 1 | 3 | 2 | 1 | 0 | 0 | 2 |
| 852 | 3 | 1 | 3 | 2 | 1 | 0 | 0 | 3 |
| 853 | 3 | 1 | 3 | 2 | 1 | 0 | 1 | 0 |
| 854 | 3 | 1 | 3 | 2 | 1 | 0 | 1 | 1 |
| 855 | 3 | 1 | 3 | 2 | 1 | 0 | 1 | 2 |
| 856 | 3 | 1 | 3 | 2 | 1 | 0 | 1 | 3 |
| 857 | 3 | 1 | 3 | 2 | 1 | 0 | 2 | 0 |
| 858 | 3 | 1 | 3 | 2 | 1 | 0 | 2 | 1 |
| 859 | 3 | 1 | 3 | 2 | 1 | 0 | 2 | 2 |
| 860 | 3 | 1 | 3 | 2 | 1 | 0 | 2 | 3 |
| 861 | 3 | 1 | 3 | 2 | 2 | 0 | 0 | 0 |
| 862 | 3 | 1 | 3 | 2 | 2 | 0 | 0 | 1 |
| 863 | 3 | 1 | 3 | 2 | 2 | 0 | 0 | 2 |
| 864 | 3 | 1 | 3 | 2 | 2 | 0 | 0 | 3 |
| 865 | 3 | 1 | 3 | 2 | 2 | 0 | 1 | 0 |
| 866 | 3 | 1 | 3 | 2 | 2 | 0 | 1 | 1 |
| 867 | 3 | 1 | 3 | 2 | 2 | 0 | 1 | 2 |
| 868 | 3 | 1 | 3 | 2 | 2 | 0 | 1 | 3 |
| 869 | 3 | 1 | 3 | 2 | 2 | 0 | 2 | 0 |
| 870 | 3 | 1 | 3 | 2 | 2 | 0 | 2 | 1 |
| 871 | 3 | 1 | 3 | 2 | 2 | 0 | 2 | 2 |
| 872 | 3 | 1 | 3 | 2 | 2 | 0 | 2 | 3 |
| 873 | 3 | 1 | 3 | 2 | 2 | 1 | 0 | 0 |
| 874 | 3 | 1 | 3 | 2 | 2 | 1 | 0 | 1 |
| 875 | 3 | 1 | 3 | 2 | 2 | 1 | 0 | 2 |
| 876 | 3 | 1 | 3 | 2 | 2 | 1 | 0 | 3 |
| 877 | 3 | 1 | 3 | 2 | 2 | 1 | 1 | 0 |
| 878 | 3 | 1 | 3 | 2 | 2 | 1 | 1 | 1 |
| 879 | 3 | 1 | 3 | 2 | 2 | 1 | 1 | 2 |
| 880 | 3 | 1 | 3 | 2 | 2 | 1 | 1 | 3 |
| 881 | 3 | 1 | 3 | 2 | 2 | 1 | 2 | 0 |
| 882 | 3 | 1 | 3 | 2 | 2 | 1 | 2 | 1 |
| 883 | 3 | 1 | 3 | 2 | 2 | 1 | 2 | 2 |
| 884 | 3 | 1 | 3 | 2 | 2 | 1 | 2 | 3 |
| 885 | 3 | 1 | 3 | 2 | 3 | 0 | 0 | 0 |
| 886 | 3 | 1 | 3 | 2 | 3 | 0 | 0 | 1 |
| 887 | 3 | 1 | 3 | 2 | 3 | 0 | 0 | 2 |
| 888 | 3 | 1 | 3 | 2 | 3 | 0 | 0 | 3 |
| 889 | 3 | 1 | 3 | 2 | 3 | 0 | 1 | 0 |
| 890 | 3 | 1 | 3 | 2 | 3 | 0 | 1 | 1 |
| 891 | 3 | 1 | 3 | 2 | 3 | 0 | 1 | 2 |
| 892 | 3 | 1 | 3 | 2 | 3 | 0 | 1 | 3 |
| 893 | 3 | 1 | 3 | 2 | 3 | 0 | 2 | 0 |
| 894 | 3 | 1 | 3 | 2 | 3 | 0 | 2 | 1 |
| 895 | 3 | 1 | 3 | 2 | 3 | 0 | 2 | 2 |
| 896 | 3 | 1 | 3 | 2 | 3 | 0 | 2 | 3 |
| 897 | 3 | 1 | 3 | 2 | 3 | 1 | 0 | 0 |
| 898 | 3 | 1 | 3 | 2 | 3 | 1 | 0 | 1 |
| 899 | 3 | 1 | 3 | 2 | 3 | 1 | 0 | 2 |
| 900 | 3 | 1 | 3 | 2 | 3 | 1 | 0 | 3 |
| 901 | 3 | 1 | 3 | 2 | 3 | 1 | 1 | 0 |
| 902 | 3 | 1 | 3 | 2 | 3 | 1 | 1 | 1 |
| 903 | 3 | 1 | 3 | 2 | 3 | 1 | 1 | 2 |
| 904 | 3 | 1 | 3 | 2 | 3 | 1 | 1 | 3 |
| 905 | 3 | 1 | 3 | 2 | 3 | 1 | 2 | 0 |
| 906 | 3 | 1 | 3 | 2 | 3 | 1 | 2 | 1 |
| 907 | 3 | 1 | 3 | 2 | 3 | 1 | 2 | 2 |
| 908 | 3 | 1 | 3 | 2 | 3 | 1 | 2 | 3 |
| 909 | 3 | 1 | 3 | 3 | 1 | 0 | 0 | 0 |
| 910 | 3 | 1 | 3 | 3 | 1 | 0 | 0 | 1 |
| 911 | 3 | 1 | 3 | 3 | 1 | 0 | 0 | 2 |
| 912 | 3 | 1 | 3 | 3 | 1 | 0 | 0 | 3 |
| 913 | 3 | 1 | 3 | 3 | 1 | 0 | 1 | 0 |
| 914 | 3 | 1 | 3 | 3 | 1 | 0 | 1 | 1 |
| 915 | 3 | 1 | 3 | 3 | 1 | 0 | 1 | 2 |
| 916 | 3 | 1 | 3 | 3 | 1 | 0 | 1 | 3 |
| 917 | 3 | 1 | 3 | 3 | 1 | 0 | 2 | 0 |
| 918 | 3 | 1 | 3 | 3 | 1 | 0 | 2 | 1 |
| 919 | 3 | 1 | 3 | 3 | 1 | 0 | 2 | 2 |
| 920 | 3 | 1 | 3 | 3 | 1 | 0 | 2 | 3 |
| 921 | 3 | 1 | 3 | 3 | 2 | 0 | 0 | 0 |
| 922 | 3 | 1 | 3 | 3 | 2 | 0 | 0 | 1 |
| 923 | 3 | 1 | 3 | 3 | 2 | 0 | 0 | 2 |
| 924 | 3 | 1 | 3 | 3 | 2 | 0 | 0 | 3 |
| 925 | 3 | 1 | 3 | 3 | 2 | 0 | 1 | 0 |
| 926 | 3 | 1 | 3 | 3 | 2 | 0 | 1 | 1 |
| 927 | 3 | 1 | 3 | 3 | 2 | 0 | 1 | 2 |
| 928 | 3 | 1 | 3 | 3 | 2 | 0 | 1 | 3 |
| 929 | 3 | 1 | 3 | 3 | 2 | 0 | 2 | 0 |
| 930 | 3 | 1 | 3 | 3 | 2 | 0 | 2 | 1 |
| 931 | 3 | 1 | 3 | 3 | 2 | 0 | 2 | 2 |
| 932 | 3 | 1 | 3 | 3 | 2 | 0 | 2 | 3 |
| 933 | 3 | 1 | 3 | 3 | 2 | 1 | 0 | 0 |
| 934 | 3 | 1 | 3 | 3 | 2 | 1 | 0 | 1 |
| 935 | 3 | 1 | 3 | 3 | 2 | 1 | 0 | 2 |
| 936 | 3 | 1 | 3 | 3 | 2 | 1 | 0 | 3 |
| 937 | 3 | 1 | 3 | 3 | 2 | 1 | 1 | 0 |
| 938 | 3 | 1 | 3 | 3 | 2 | 1 | 1 | 1 |
| 939 | 3 | 1 | 3 | 3 | 2 | 1 | 1 | 2 |
| 940 | 3 | 1 | 3 | 3 | 2 | 1 | 1 | 3 |
| 941 | 3 | 1 | 3 | 3 | 2 | 1 | 2 | 0 |
| 942 | 3 | 1 | 3 | 3 | 2 | 1 | 2 | 1 |
| 943 | 3 | 1 | 3 | 3 | 2 | 1 | 2 | 2 |
| 944 | 3 | 1 | 3 | 3 | 2 | 1 | 2 | 3 |
| 945 | 3 | 1 | 3 | 3 | 2 | 1 | 3 | 0 |
| 946 | 3 | 1 | 3 | 3 | 2 | 1 | 3 | 1 |
| 947 | 3 | 1 | 3 | 3 | 2 | 1 | 3 | 2 |
| 948 | 3 | 1 | 3 | 3 | 2 | 1 | 3 | 3 |
| 949 | 3 | 1 | 3 | 3 | 3 | 0 | 0 | 0 |
| 950 | 3 | 1 | 3 | 3 | 3 | 0 | 0 | 1 |
| 951 | 3 | 1 | 3 | 3 | 3 | 0 | 0 | 2 |
| 952 | 3 | 1 | 3 | 3 | 3 | 0 | 0 | 3 |
| 953 | 3 | 1 | 3 | 3 | 3 | 0 | 1 | 0 |
| 954 | 3 | 1 | 3 | 3 | 3 | 0 | 1 | 1 |
| 955 | 3 | 1 | 3 | 3 | 3 | 0 | 1 | 2 |
| 956 | 3 | 1 | 3 | 3 | 3 | 0 | 1 | 3 |
| 957 | 3 | 1 | 3 | 3 | 3 | 0 | 2 | 0 |
| 958 | 3 | 1 | 3 | 3 | 3 | 0 | 2 | 1 |
| 959 | 3 | 1 | 3 | 3 | 3 | 0 | 2 | 2 |
| 960 | 3 | 1 | 3 | 3 | 3 | 0 | 2 | 3 |
| 961 | 3 | 1 | 3 | 3 | 3 | 1 | 0 | 0 |
| 962 | 3 | 1 | 3 | 3 | 3 | 1 | 0 | 1 |
| 963 | 3 | 1 | 3 | 3 | 3 | 1 | 0 | 2 |
| 964 | 3 | 1 | 3 | 3 | 3 | 1 | 0 | 3 |
| 965 | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 0 |
| 966 | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 1 |
| 967 | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 2 |
| 968 | 3 | 1 | 3 | 3 | 3 | 1 | 1 | 3 |
| 969 | 3 | 1 | 3 | 3 | 3 | 1 | 2 | 0 |
| 970 | 3 | 1 | 3 | 3 | 3 | 1 | 2 | 1 |
| 971 | 3 | 1 | 3 | 3 | 3 | 1 | 2 | 2 |
| 972 | 3 | 1 | 3 | 3 | 3 | 1 | 2 | 3 |
| 973 | 3 | 1 | 3 | 3 | 3 | 1 | 3 | 0 |
| 974 | 3 | 1 | 3 | 3 | 3 | 1 | 3 | 1 |
| 975 | 3 | 1 | 3 | 3 | 3 | 1 | 3 | 2 |
| 976 | 3 | 1 | 3 | 3 | 3 | 1 | 3 | 3 |

**976 rows. F(1) = 976, F(−1) = 2, E = 0, density 0.1412 of a box of 6,912.**

## The periodic table — all 90 cells, (period, group)

| period | groups occupied |
|---|---|
| 1 | 1, 18 |
| 2 | 1, 2, 13, 14, 15, 16, 17, 18 |
| 3 | 1, 2, 13, 14, 15, 16, 17, 18 |
| 4 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| 5 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| 6 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| 7 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |

**90 cells in a box of 126. E = 36** — and the 36 are the cells the coordinates admit and no
element occupies, which must be supplied from outside.

## Janet — all 118, (n+ℓ, Z)

| n+ℓ | atomic numbers |
|---|---|
| 1 | 1–2 (2) |
| 2 | 3–4 (2) |
| 3 | 5–12 (8) |
| 4 | 13–20 (8) |
| 5 | 21–38 (18) |
| 6 | 39–56 (18) |
| 7 | 57–88 (32) |
| 8 | 89–118 (30) |

**118 cells, E = 0.** The same 118 elements as the table above, reordered by n+ℓ.

## The calendar — 365 cells, (month, day)

| month | days | month | days |
|---|---|---|---|
| January | 31 | July | 31 |
| February | 28 | August | 31 |
| March | 31 | September | 30 |
| April | 30 | October | 31 |
| May | 31 | November | 30 |
| June | 30 | December | 31 |

**365 cells in a box of 372. E = 7** — February's missing 29th, 30th and 31st, and the four thirty-day
months' 31sts. **365 = 5 · 73, and 73 exceeds every rung**, so it is genuinely constrained.

## A box ordering — all 35, l ≥ w ≥ h

| l ≥ w ≥ h |
|---|
| 0·0·0  1·0·0  1·1·0  1·1·1  2·0·0  2·1·0  2·1·1 |
| 2·2·0  2·2·1  2·2·2  3·0·0  3·1·0  3·1·1  3·2·0 |
| 3·2·1  3·2·2  3·3·0  3·3·1  3·3·2  3·3·3  4·0·0 |
| 4·1·0  4·1·1  4·2·0  4·2·1  4·2·2  4·3·0  4·3·1 |
| 4·3·2  4·3·3  4·4·0  4·4·1  4·4·2  4·4·3  4·4·4 |

**35 cells in a box of 125, E = 0.** 35 = 5 · 7 and 7 exceeds the rung of 5: a real constraint.

---

# VIII · WHAT EACH INDEX IS, AND WHAT ONLY IT CONTRIBUTES

**Λ is the only index here built from physics.** The rest are built from Λ, from the act of building Λ, or from drawing the same subject another way. *This section states for each one: what it is, where it comes from in the published record, and the one thing it contributes to the atomic index that no other index can.*

---

## Λ — the atomic index

**What it is.** Eight integer coordinates (n, ℓ, k, q, e, f, g, 2S) under eight inequalities, 976 cells, E = 0.

**Where it comes from.** The constraints are not this work's: ℓ ≤ n−1 is the hydrogen solution (Bohr 1913; Schrödinger 1926); k ≤ 4ℓ+2 is Stoner's subshell capacity (1924) made exclusive by Pauli (1925); 2S ≤ k is Pauli with Hund's first rule (1925). **Λ assembles them; it introduces none.**

**What only it contributes.** *The transfer.* Λ is the only index here whose cells are MOVES rather than positions — a cell carries a source subshell, a target subshell and a count transferred. **Everything about composition, time columns and categories follows from that and from nothing else in this compendium.**

## The tower Λ₈…Λ₁₃

**What it is.** Λ with the coupling quantum numbers adjoined one at a time — seniority, the core J, K, then J. Cell counts 976, 1654, 2535, 13585, 70905, 199130, E = 0 at every stage.

**Where it comes from.** Each axis is Racah or Condon & Shortley: seniority is Racah, *Theory of complex spectra III*, Phys. Rev. **63** (1943) 367–382; the core J and the recoupling coefficients are Racah, Phys. Rev. **62** (1942) 438–462; the jK and LK schemes are Condon & Shortley (1935), ch. X.

**What only it contributes.** *The price of an axis.* The tower is the only construction here that adds one coordinate at a time and measures what each costs and buys — **cycle rank, composability, exactness, and the point at which the tree becomes a graph.** No single index can show that; it takes a sequence.

## The periodic table — (period, group)

**What it is.** 90 cells in a box of 126, E = **36**.

**Where it comes from.** Mendeleev, *Über die Beziehungen der Eigenschaften zu den Atomgewichten der Elemente*, Z. Chem. **12** (1869) 405–406. At least a thousand periodic systems have been published since (van Spronsen; Scerri, *A Tale of Seven Scientists*, 2016).

**What only it contributes.** *The control.* It is the one index whose coordinates were fixed by other people for other reasons, long before this work, and which nonetheless supplies **118 elements and 18,288 constraint tests with zero failures.** **An index built by the author cannot be a control; this one can.**

## Janet's left-step table — (n+ℓ, Z)

**What it is.** The same 118 elements, ordered on n+ℓ. 118 cells in a box of 944, E = **0**.

**Where it comes from.** Charles Janet, *Considérations sur la structure du noyau de l'atome*, Beauvais (1929), with the table first published in **1928**. *Janet recognised the (n+ℓ) rule before Madelung, who arrived at it around 1926 and did not publish until 1936.* The shell-length sequence 2, 2, 8, 8, 18, 18, 32, 32 follows from the rule by the Klechkovski–Hakala formulas.

**What only it contributes.** *That E is coordinate-relative, demonstrated on one subject rather than argued.* The periodic table and Janet index THE SAME 118 elements and give E = 36 and E = 0. **No pair of indexes anywhere else in this work makes that point as cleanly, because no other pair shares its subject exactly.**

**And an open problem sits underneath it.** *Why* the n+ℓ ordering holds is unresolved — Löwdin's challenge, still open; see Allen & Knight, *The Löwdin challenge: origin of the n+l, n (Madelung) rule*, Int. J. Quantum Chem. **90** (2003) 80–88. **This work uses the ordering and does not explain it**, and the orbital-collapse result (registers 1187–1190) is a measurement against Janet's boundaries, not a derivation of them.

## The nuclide chart — (Z, N)

**What it is.** The measured nuclides indexed by proton and neutron count, E = **9**.

**Where it comes from.** The chart is Segrè's, in use since the 1940s; the values are the AME2020 evaluation.

**What only it contributes.** *A defect whose cells are identifiable physics.* The nine cells are the mass formula's pairing and clustering terms. **It is the only index here where E > 0 and every missing cell can be named**, which is what makes the defect a measurement rather than a score.

## The calendar — (month, day)

**What it is.** 365 cells in a box of 372, E = **7**.

**Where it comes from.** The Gregorian reform of 1582, on the Julian arrangement of 46 BC. *The month lengths are a political inheritance, not a natural one.*

**What only it contributes.** *A subject with no physics in it at all.* The calendar shows the operator working on an object whose constraints are entirely conventional, **and 365 = 5 · 73 with E = 7 is the price of keeping January first.** No other index here separates the method from the physics so completely.

## The box ordering and the chessboard

**What they are.** ℓ ≥ w ≥ h over five values: 35 cells in 125, E = 0. And (rank, file): 64 cells in 64, E = 0.

**What only they contribute.** *The floor and the ceiling.* The chessboard is a full product — E = 0 because there is no constraint at all. The box ordering is a genuine constraint that still closes. **Between them they show that E = 0 carries information only when the ambient box exceeds the cells**, which is why the compendium reports box alongside every defect.

## The electromagnetic quotient

**What it is.** Λ₉ under the dipole selection rules: |Δℓ| = 1 and ΔS = 0.

**Where it comes from.** The parity rule is Laporte, Z. Phys. **23** (1924) 135; the spin rule is Russell & Saunders, Astrophys. J. **61** (1925) 38; both have their group-theoretic ground in Wigner, Z. Phys. **43** (1927) 624.

**What only it contributes.** *That a selection rule is a QUOTIENT and not an extension.* Adjoining the multipole and ΔS as coordinates gives E = 3; taking the image gives E = 0. **It is the only index here that demonstrates the difference between adding a coordinate and dividing by one.**

## Λ_spectra — the channel index

**What it is.** (Z, charge, ℓ, 2S+1) over 104,832 cells, with a defect for each.

**Where it comes from.** Quantum defect theory is Seaton, MNRAS **118** (1958) 504–518, and Rep. Prog. Phys. **46** (1983) 167–257. *A published survey of the same object exists*: Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables **35** (1986) 473–486, Hartree–Slater, for all ionisation stages of all ions with Z ≤ 50.

**What only it contributes.** *Values.* Every other index here holds cells and asks whether they close. **Λ_spectra holds cells that carry NUMBERS**, which is why it is the only index on which the Method equation's metric half — E_W — has anything to measure at all (registers 1196–1199).

## The violation index

**What it is.** The companion paper's object over nine and fifteen letters, with a core of three conditions whose joint failure is irreducible.

**Where it comes from.** The conditions are physics — the null energy condition (Penrose 1965), ghost states (Pais & Uhlenbeck 1950), the equations of motion. *The core is a MINIMAL UNSATISFIABLE SUBSET* in the sense of Chinneck & Dravnieks, *Locating minimal infeasible constraint sets in linear programs*, ORSA J. Comput. **3** (1991) 157–168.

**What only it contributes.** *An index this work reasons about without holding.* Its cells are not printed anywhere. **It is the only test of whether the method says anything when the object is out of reach**, and the answer is that it locates a three-condition core from published summary numbers alone.

## Λ_phys — the parameter index

**What it is.** Every number the work takes from physics, on four coordinates — kind (exact → fitted), source (mathematics → this work), domain (universal → one species, and the three-body problem's own range), and how many registered objects rest on it. **27 parameters** (22 before Chapters 35 and 36 added c, the three-body masses, E, L and G).

**Where it comes from.** The parameters are Rydberg 1890, Bohr 1913, Stoner 1924, Pauli 1925, Hund 1925, Fermi 1928, Hartree 1928, Janet 1928, Mayer & Mayer 1933, Goeppert-Mayer 1941, Seaton 1958, Edlén 1964, Griffin, Andrew & Cowan 1969, CODATA 2018 — and eight numbers fitted here. *The Physics Compendium holds them in full, each with a definition, a dated source and a failure mode.*

**What only it contributes.** *Where the work would break first.* Every other index here asks whether a set of cells closes. **Λ_phys asks what the whole construction rests on, and the answer is a shape:** eight of the twenty-seven parameters are this work's own, **none of them is universal**, seven of the eight hold only in a region or for one species — and, on the one rule the Physics Compendium now prints, the two carrying the most objects are the lattice's own exact bounds, the angular-momentum bound (72 objects) and the subshell capacity (66), with the aufbau ordering (18) next; the earlier reading — the ionisation limit 25, the aufbau ordering 19, the Janet boundary 15, on a rule never printed — stands in that compendium as the prior state (register 1740).

**And three of its failure modes are MEASURED rather than anticipated** — Seaton's ratio at 1.25 where the dipole term gives 1.00, the Thomas–Fermi exponent rising from 0.84 to 1.52 with charge against a single fitted 0.494, and the exchange coefficient whose fitted sign is opposite to the measured one.

## The languages

**What they are.** Six readings of one index — order, analysis, algebra, geometry, information, statistics — with documentary as a seventh that has no operator.

**Where they come from.** Each operator is standard in its own field: closure from Moore (1910), max-entropy on marginals from Deming & Stephan (1940) and Csiszár (1975), conditional independence from Dawid (1979).

**What only they contribute.** *That translation is re-coordinatisation and E is its cost.* **And the agreement theorem: E(X) = 0 if and only if the languages agree** — six indexes, three operators, no exception (register 1176).

## The book's own indexes

**What they are.** The book at chapter resolution (E = 578) and at part resolution (E = 0); the register (E = 6 at 68.8% density); the reference index (38 cells, E = 0, and not a tree); the term index at the back of the main volume (57 terms over 44 specialisation relations, 311 locations, E = 0 as a down-set — regenerated from the text at this build).

**What only they contribute.** *The method self-applied.* **This is the only place where E > 0 is a theorem about SHAPE rather than a gap in collection** — the book's chapters do not close because chapters are not a coordinate system, and saying so with a number is the point.

---

## Λ₃ — the three-body index

**What it is.** Five strata on ℳ_{E,L} over three unspecified masses; E = 0.

**Where it comes from.** The classes are Chazy 1922; disjointness is Saari 1971/73 and Painlevé for n = 3; the assembly into one index with a certificate is this work's (register 1713).

**What only it contributes.** *A complete index whose completeness IS the impossibility theorem.* E = 0 read as Poincaré: by §25.6 a complete index with no time column predicts nothing, and that is Brudno's rate on the chaotic stratum, not a failure of the method (register 1714, 1724).

## The one-line summary

| index | the one thing only it gives |
|---|---|
| **Λ** | the transfer — cells that are moves |
| **the tower** | the price of an axis, measured one at a time |
| **the periodic table** | a control the author did not build |
| **Janet** | E is coordinate-relative, on one subject |
| **the nuclide chart** | a defect whose every cell is nameable physics |
| **the calendar** | a subject with no physics in it |
| **box and chessboard** | the floor and ceiling of what E = 0 means |
| **the EM quotient** | quotient versus extension |
| **Λ_spectra** | values, so the metric defect has something to measure |
| **the violation index** | reasoning about an index without holding it |
| **Λ_phys** | where the work would break first |
| **the languages** | translation as re-coordinatisation |
| **the book's own** | E > 0 as a theorem about shape |
| **Λ₃** | a complete index whose completeness *is* the impossibility theorem — E = 0 read as Poincaré |

**Λ and Λ₃ are the only ones built from physics. The rest are built from Λ, from the act of building Λ, or from drawing the same subject another way — and that is the claim: an index is a coordinate system, and the coordinates come from the subject or from nowhere.**

# IX · THE INDEXES BUILT IN THE LÖWDIN WORK

*Registers 1249–1429. **Fifteen indexes: fourteen closed — Λ_ladder now among them
— and Λ_spectra closing at the limit with eleven named cells.** The fourteen closed are stated
below; Λ_spectra is stated in Part VIII. Each is stated the same way:
what it indexes, its coordinates, the axis order that closes it, what it refuses,
and the one thing it contributes.*

---

## Λ_law — the laws of the channel equation

**What it is.** Seven laws on (law, carrier). **E = 0** at carrier order
**u < p < ℓ−ℓ_core < Z−T**, and 288 of 120,960 orderings reach it.

**What only it contributes.** *The carrier.* The order is monotone in how LOCAL
the variable is — u is the whole atom, p counts one ℓ's shells, ℓ−ℓ_core compares
two angular momenta, Z−T is one distance to one threshold. **The index says which
law runs in which variable, and fitting a law in the wrong carrier is what took
the ℓ-spread from a spurious r² 0.868 to a real 0.356.**

## Λ_const — the constants

**What it is.** Fourteen constants on (role, carrier), role order
**exponent < centre < width < scale**. **E = 0** at 2 of 576 orderings.

**What only it contributes.** *That `standing` cannot be a coordinate.* With
attributed/derived/measured/fitted on an axis the index cannot close at any
ordering; without it, it closes at once. **An index whose coordinates mix the
object with the observer cannot close, because the observer's axis has no order
the object respects.** The same fault recurs as `origin` in Λ_var, `kind` in
Λ_phys and `state` in Λ_ladder.

**And the role axis orders by how much physics a number has absorbed.** Every
CENTRE in the system is a small integer or half-integer — 2, 2, 2.5, −1.5, 5.4 —
and no SCALE is.

## Λ_var — the variables

**What it is.** Twelve variables on (body, role), body order
**nucleus < core < core+rydberg < nucleus+core < rydberg**. **E = 0.**

**What only it contributes.** *That there is no nucleus + rydberg cell.* Not one
variable relates them directly: every quantity connecting the Rydberg electron to
the nucleus — c, u — is a nucleus–core quantity that the Rydberg electron then
reads. **That is the screening statement appearing as a structural fact of the
index rather than a modelling choice, and it is the three-body factorisation:
nucleus–core gives c and u, core–Rydberg gives p, n₀ and T, and the Rydberg
electron's own ℓ closes it.**

**And the singleton rule.** Λ_var passes ℛ with both δ and n\* present, because
both land in the same cell — **only a second criterion sees it. An index is closed
when its output class is a singleton; two outputs mean the observer is still
choosing which to read.**

## Λ_ryd — the Rydberg series

**What it is.** Five cells on (Ritz order, ℓ, sign). **E = 0** once δ₂ is
reclassified as INTERMEDIATE — it is fitted from the series, never measured.

**What only it contributes.** *The n-dependence Λ_spectra discards.* A channel's
δ is not one number but a convergent sequence — Cd I's ns series gives 3.7171,
3.6835, 3.6719, 3.6665, 3.6637, 3.6621, 3.6610. **Λ_spectra holds δ₀; Λ_ryd holds
δ₂ and δ₄.**

**And the sign of δ₂ is penetration, not ℓ**: 0 of 3 positive at p = 0, 2 of 2 at
p = 5. **Seaton's ratio is valid where p = 0 at 1.15 ± 0.21 and UNDEFINED where
p ≥ 1** — a domain, not a failure.

## Λ_charge — the roles of the charge

**What it is.** Nine occurrences on (role, carrier, sign, regime), nine distinct
cells, **E = 0**, and dropping any single role also gives 0.

**What only it contributes.** *That c is three coordinates in one symbol.* The
charge appears inside u = ln(Nₑ/c^(2/3)), as the base of c^(−x), and inside the
exponent x itself. **Every degeneracy found was between a charge term and
something else, and this index says why: one symbol occupying three positions,
and any fit letting two of them float will trade them.**

**A warning the index also carries**: declaring the three roles as coordinates in
Λ_spectra raises E from 1929 to 13,605. **A closed sub-index says its roles are
well-posed; it says nothing about whether the parent index wants them.**

## Λ_cross — the crossing values

**What it is.** The value at which an ordering flips,
**a_cross = Δn(√p_g + √p_r)/(p_g − p_r)** — nineteen distinct surds across the
table, including 1/√3, 1/√2, 1, 1/(√3−1), 1+1/√2 and 1/(√2−1). **E = 0** on
(Δn, ℓ_g).

**What only it contributes.** *An index with no statistics language.* Order,
algebra (closed in ℚ(√p) for p ≤ 7) and geometry all speak of it; **analysis and
statistics do not.** A quantity that is ordinal, algebraic and geometric but not
analytic is an INTEGER OBJECT: it cannot be fitted and needs no fitting.

**And it is the one index whose unfixable cell is fixed anyway** — a node count
needs no measurement. **Nine of eleven unfixable cells across the work are
expectation values ⟨Ψ|Ô|Ψ⟩; Λ_cross is the exception, and it is the only index
with no statistics language. The two facts are the same fact.**

## Λ_descent — the charge dependence

**What it is.** a(c) on (c, regime). **E = 0.**

**What only it contributes.** *The only place a fit belongs.* Order and analysis
both speak of it, information says c adds everything, and statistics answers yes.
**Every fit made was applied to the WHOLE of a — the crossing and the
descent together — and that is why the constants kept absorbing each other: half
the object has no analysis language, and the fitted parameters were competing to
represent a set of surds.**

## Λ_phys — the parameters, rebuilt

**What it is.** Twenty-one parameters of real atoms on (source, domain),
**E = 0**, at source order **standard < mathematics < literature < this work** and
domain order **universal < all elements < a region < one species**.

**What only it contributes.** *That no parameter of this work is universal.* The
closing grid is a staircase and the diagonal is the whole content: CODATA
constants are universal, this work's numbers hold on a region or all elements and
never universally. **A pooled fit across regions asserts a universal parameter,
which the closed index says does not exist — that is a structural prohibition,
not a stylistic preference, and it is what `domain_protocol.py` enforces.**

**Rebuilt on three rulings**: `kind` is the same axis as `source`; `arity` is a
property of the book, not the parameter; and parameters that are artefacts of the
METHOD are not physics of real atoms.

## Λ_amp — the electron–electron term

**What it is.** The Slater integrals: for each subshell pair, F^k for k even up to
2min(ℓ,ℓ′) and G^k for k ≡ ℓ+ℓ′ (mod 2) from |ℓ−ℓ′| to ℓ+ℓ′. **Twenty cells,
E = 0**, a perfect triangle **0 ≤ i ≤ ℓ**.

**What only it contributes.** *That the rank is not a free coordinate.* Indexed on
the multipole rank k the index gives E = 1 and the single defect is **F¹ — a term
parity forbids.** Reindexed on POSITION WITHIN SEQUENCE it closes. **The same
fault as `breadth` in Λ_chem: an axis whose values are constrained by another
axis.**

**And its structure explains the Slater result exactly**: at s/s the exchange G⁰
IS the direct F⁰, so dropping exchange costs nothing; at f/f it discards four
independent quantities. **The count of lost integrals is the count of failures —
5 of 5 s-block brackets threaded, 0 of 1 f.**

## Λ_PCA — physics ⊕ charge ⊕ amplitude, merged

**What it is.** Nine cells on (source, domain) with the domain refined by the
charge regime: **universal < all elements < low < neutral < hydrogenic < one
species**. **E = 0.**

**What only it contributes.** *The per-atom calibration.* A parameter's domain
reads as a SET OF ATOMS, so for any (Z, c) the index states which parameters
apply to it. **And the closing order puts `low` — charge 2 — BEFORE the neutral,
which the ladders independently confirm: c = 2 is the only charge with two-sided
brackets, the narrowest domain and therefore the most particular.**

**A correction recorded here**: merging Λ_phys and Λ_charge on identified axis
NAMES raised E from 6 to 11 and I concluded they were not one object. That was
against a malformed Λ_phys. **Merged on `domain ≡ regime` alone, after the
rebuild, they close.**

## Λ_chem — the chemical properties

**What it is.** Forty-two chemical properties of a species on (kind, seat, PCA
dependency). **E = 0 on fourteen cells** over the subvalence and valence shells.

- **kind**: count · symmetry · size · energy · rate
- **seat**: the nucleus · the core · the subvalence shell · the valence shell ·
  **the aggregate**
- **PCA**: which of physics, charge or amplitude the property supplies

**What only it contributes.** *That twelve of the forty-two are properties of
MATTER IN BULK and not of an isolated atom* — density, melting point, hardness,
crystal structure, conductivity, colour of the metal, smell, taste, metallic
character, reactivity. **With eleven hand-picked properties the index could not
say this; it appeared the moment every property was demanded.**

**And its closure states PCA's own boundary.** E climbs **0 → 3 → 8 → 11 → 19** as
the core, the nucleus and the aggregate are added. **PCA's domain is the
subvalence and valence shells, and the index declares it by degrading
monotonically outside it** — as Seaton's ratio is valid at p = 0 and undefined
beyond.

**The last defect cell, found by exhaustive reordering.** All 1,440 orderings give
minimum E = 1 and none reaches zero: the cell is **symmetry × the valence shell ×
a charge role**. The fill is the ground TERM, which changes with charge —
Nₑ = 20 gives ¹S₀ → ³D₁ → ³F₂ → ³F₂ and Nₑ = 38 the identical sequence.
**Every ladder table carried the term symbol; the configurations were recorded and
the terms were not.**

## Λ_t — the corridor position

**What it is.** Twelve cells on (ℓ, n) holding **t = (a − L)/(U − L)**, where a
sits in its corridor. **E = 3.**

| ℓ \ n | 2 | 3 | 4 | 5 | 6 | 7 | limit |
|---|---|---|---|---|---|---|---|
| **s** | 0.268 | 0.335 | 0.266 | 0.218 | 0.257 | 0.195 | — |
| **p** | · | 1.120 | 1.049 | 1.022 | 1.002 | · | **1.0000** |
| **d** | · | · | 1.819 | 1.433 | · | · | **1.7321** |

**What only it contributes.** *That the ℓ axis carries the LIMIT and the n axis
the APPROACH.* t converges to √(ℓ(ℓ+1)/2), the centrifugal term — 6p sits 0.2%
above it — and the gap falls **0.120 → 0.049 → 0.022 → 0.002** along n.

**And q is not a coordinate.** With the Pauli fraction in the radicand, t barely
moves across a subshell: 6p gives 1.0237, 1.0417, 1.0009, 1.0036, 0.9946, 0.9940
across all six occupancies.

**Its three defect cells are 7p, 6d and 7d** — real absences, each a subshell
whose corridor is one-sided or whose ionisation energy is not held.

## Λ_ladder — the ladders themselves

**What it is.** The walks, on (seat, kind, Zcross). **FOURTEEN ladders in three
families — six species, six state, two X-ray — nine cells, E = 0. IT CLOSES.**
Registers 1356, 1374, 1375, 1384, 1427.

Two relations, three ladders each — **Z = Nₑ + c − 1** on Λ, and **A = Z + N** on
the nuclide chart. Only two of three are independent either side, so no ladder
varies Z alone: forbidden by arithmetic, not by lack of data.

| family | ladder | fixes | reaches | held |
|---|---|---|---|---|
| species | isoelectronic | Nₑ | valence | 11 of 11 |
| species | the walk | c | valence | 106 of 106 |
| species | ionisation | Z | subvalence | 15 of 108 |
| species | isotopic | Z, Nₑ, c | nucleus | **1 rung traced** |
| species | isotonic | N | nucleus | none — NEW |
| species | isobaric | A | nucleus | none — NEW |
| state | the Rydberg series | the species | valence | every δ held |
| state | the ℓ-ladder | species, n | valence | 62 pairs |
| state | the term ladder | species, cfg | valence | 66 pairs |
| state | the outer-j ladder | species, cfg | valence | the j-splitting (register 754) |
| state | the parent-term | the species | core | 12 of 15 |
| state | the isomeric | Z, N, e⁻ | nucleus | none — NEW |

**What only it contributes.** *That a coordinate individuating the cells is a KEY,
not an axis.* At four ladders `fixes` was injective by construction — a ladder IS
named by what it holds fixed — so one cell per row, and **E = 0 was FORCED: 2% of
admissible arrangements could refuse.** At six, ionisation and isotopic both fix
Z, and the zero becomes earnable. That is the dual of the defining letter (§21.6.1), where a
single-valued coordinate contributes no envelope; this is the other end of the
same degeneracy.

**IT CLOSES, and both blocking reasons are resolved.** The E = 1 defect stood at
**(subvalence, counting, across elements)** — Moseley's ladder, in a direction
ionisation does not go. That defect is what demanded Λ_xray, and Λ_xray filled it:
Moseley enters at subvalence as counting/across, the Kα doublet as coupling/within.
**Only the subvalence seat closes** — nucleus gives 1, core 2, valence 1 — and the
seat is settled from OUTSIDE the closure rather than by it, since Λ_PCA excluded
the core independently, on different coordinates, before this was computed. The
physics agrees: a Kα line is not a property of the 1s shell but a transition
*between* shells, so the seat is where the transition spans, not where the hole
sits. **Contingency: 90% of comparable nine-cell sets refuse, so the zero is
earned** (R 1427).

**And the five shared cells are four findings and one separation** (R 1428). Two
pairs are ONE OBJECT and the index is right to merge them — isotonic fixes N and
isobaric fixes A with A = Z + N; isoelectronic fixes Nₑ and the walk fixes c with
Z = Nₑ + c − 1. That is *charge is one symbol in three positions*, one level up.
Two are separated by axes already in the index but not among the three that close:
isotopic is species where the isomeric is state; the Rydberg series fixes the
species where the ℓ-ladder fixes species and n. **The fifth was the real
ambiguity** — the term ladder and the outer-j ladder — and they are five tower
stages apart, nested rather than parallel: the term ladder moves 2S, Λ₈'s own
letter, while the outer-j ladder moves 2J, which arrives only at Λ₁₃. Adding the
tower stage as a fourth axis separates that pair and only that pair, but costs
closure, E going 0 → 1. **So the stage is the discriminator, not an axis** (R 1429).

## Λ_xray — the inner shell

**What it is.** The dipole-allowed inner-shell transitions, on
(Δn, Δℓ, jtype_hole). **33 lines through the N shell → 9 cells, E = 0.**
Register 1378.

**Where it comes from.** Built with no new data. **Λ's cell IS a transition** —
source subshell into target subshell — and its constraints impose no order between
n and e, so a downward transition was already inside its alphabet; only the caps
excluded it. The electric/magnetic multipole selection rules (§12.11.8) give the dipole rule, the recoupling bound (§12.11.1) the j triangle. The six K-shell
lines emerge as the classical set unadjusted: K-L2 and K-L3 are Kα₂ and Kα₁,
K-M2 and K-M3 are Kβ₃ and Kβ₁, K-N2 and K-N3 are Kβ₂. Energies are NIST SRD 128,
Deslattes *et al.*, *Rev. Mod. Phys.* **75** (2003) 35–99.

**What only it contributes.** *That thirty-three named lines are nine transition
types.* Seventy-two of 165 three-coordinate systems reach E = 0 and **every one
collapses to exactly nine cells** — Kα, Lα and Mα are one type read at three
depths, which Siegbahn notation hides.

**And it settles what Λ_cross's silences mean.** The two close on the same shape —
differences plus one endpoint — and the cypher separates them:

| language | Λ_cross | Λ_xray |
|---|---|---|
| order | speaks | speaks, E = 0 |
| geometry | speaks | speaks |
| statistics | **silent** | **speaks** — pairwise marginals recover all 9 |
| analysis | **silent** | **speaks** — Moseley, R² = 0.998 |

*Λ_cross remains the only integer object: cells AND values fixed by arithmetic.
Λ_xray has integer cells and measured values.* Registers 1379, 1380, 1385.

## The one-line summary, extended

| index | the one thing only it gives |
|---|---|
| **Λ_law** | the carrier — which variable a law runs in |
| **Λ_const** | that `standing` cannot be a coordinate |
| **Λ_var** | no nucleus + rydberg cell — the three-body factorisation |
| **Λ_ryd** | the n-dependence Λ_spectra discards |
| **Λ_charge** | c is three coordinates in one symbol |
| **Λ_cross** | an index with no statistics language |
| **Λ_descent** | the only place a fit belongs |
| **Λ_phys** | no parameter of this work is universal |
| **Λ_amp** | the rank is not a free coordinate |
| **Λ_PCA** | the per-atom calibration |
| **Λ_chem** | twelve of forty-two properties are not an atom's at all |
| **Λ_t** | ℓ carries the limit, n carries the approach |
| **Λ_ladder** | that a coordinate individuating the cells is a key, not an axis |
| **Λ_xray** | thirty-three named lines are nine transition types |
| **Λ_chain** | Λ's input column as a derived object — the order from the equation, one constant |
| **Λ_cinf** | that the periodic table is not a solution of the non-relativistic equation |
| **Λ_V5** | every contested competition widens under correlation |
| **Λ_j120** | Λ's falsification frontier, twelve rows wide |
| **Λ₃** | masses enter through six numbers; structure is mass-free — the three-body factorisation, closed |

**Fourteen close.** Λ_xray is new and closes at nine transition types. **Λ_ladder
now closes too** — fourteen ladders, nine cells, E = 0, once the X-ray pair is
seated at subvalence (R 1427), its five shared cells resolving as four findings
and one separation (R 1428–1429).

**Λ_spectra closes at the LIMIT** — not for want of the principal number, as
register 1341 supposed. The index runs to the last available species and stops:
98 cells, E = 58, of which 38 need more electrons than any atom has. **The
remaining twenty are within the limit, and eleven of those are the Madelung
exceptions, each nameable** (R 1395, corrected at R 1426).

# X · THE INDEXES BUILT IN THE LÖWDIN SOLUTION

*Registers 1701–1712; Chapter 35. Four indexes the solution builds beside Λ — what each holds, whether it closes, whether it carries time, and what role it plays for Λ. The template differs from Part IX's by design: these are transition indexes, and closure and time are the questions they exist to answer.*

## Λ_chain — the derived filling index

**What it holds.** 119 rows, one per element Z = 2–120: entrant channel, entrant
depth, margin, and the full frontier candidate spectrum of the V^{N−1} walk;
provenance per row (SCORED 107, UNWITNESSED 12).

![**Figure 7.** A cell of Λ_chain as a move: the carried state enters, the field is built, the spectrum is read, the deepest channel is the move, and the output state seeds the next cell.](figures/figaddioichain.png)

![**Figure 8.** The provenance of Λ_chain, cell by cell: 107 scored, 12 unwitnessed, with the five contested rows and the three derived exceptions marked.](figures/figaddioiprovenance.png)

**Does it close?** As an index of rows, trivially — one cell per Z, none refused.
The substantive closure is different in kind and stronger: **the chain closes on
itself.** Each row is built from the previous row's derived output, so a single
wrong cell breaks every cell after it, and 107 of 107 is therefore one score, not
107 (register 1701–1702).

**Does it carry time?** Yes, in this compendium's exact sense: **its cells are
moves** — the step Z−1 → Z, adding one electron to a channel — so it carries a
time column, standing beside Λ as a second transition index in the collection,
and the first whose moves are **totally ordered**. *Chapter 34 proved the table
needs a carried state; Λ_chain is that state, carried by the equation.*

**Role for Λ.** It supplies, from first principles, the one thing Chapter 6
proved Λ cannot supply for itself: the aufbau ordering. **Λ's input column is now
a derived object.** Every configuration Λ indexes is generated by Λ_chain with
one constant, and the two agree everywhere Λ has an element.

---

## Λ_cinf — the counterfactual twin

**What it holds.** The identical 107-row walk at c → ∞.

**Does it close?** As Λ_chain does, on itself.

**Does it carry time?** Yes — the same move-cells as Λ_chain, in the same total order.

**Role for Λ.** None as data, everything as contrast: **eleven of its entrants
differ from Λ_chain's, and all eleven are wrong against nature.** It exists to
state that Λ's subject is relativistic, and it is quarantined from every other
use (register 1706).

---

## Λ_V5 — the contested-row closure

**What it holds.** Five rows — Z = 38, 56, 72, 89, 105 — each carrying the
complete second-order correlation differential over the mean-field margin, with
declared envelopes.

**Does it close?** Yes, by exhaustion: the five rows are *all* the rows whose
margins are small enough to be at risk, and the criterion selecting them is
stated, not curated.

**Does it carry time?** No. It is a still photograph of the walk's five closest
calls.

**Role for Λ.** It is the warrant that Λ_chain's mean field carries the exact
equation's order: **every contested competition widens under correlation**
(register 1705). Without this index the derivation would be conditional in a
place it is now checked.

---

## Λ_j120 — the unwitnessed extension

**What it holds.** Twelve rows, Z = 109–120: entrant, depth, margin, and the
spin-orbit worst case each margin clears.

**Does it close?** Its cells do; its **values are unwitnessed** — the grade this
book already owns for a bound the world has not yet supplied. Nothing in it is
defected for want of trying.

**Does it carry time?** Yes — move-cells, Λ_chain's own order continued past the last measurement.

**Role for Λ.** It is Λ's falsification frontier. The day a superheavy ground
configuration is measured, exactly one row here either scores or fails, and
either outcome is information the whole structure inherits (register 1712).

---

*One line for the map: Λ_chain stands to Λ as derivation stands to arrangement.
Λ holds the configurations; Λ_chain says why they are the ones held — and says it
from the equation, with one number, carrying the state that closure alone could
never carry.*

---

# XI · TRANSITIONS, THE COMPLETE TABLE

**Every section of the source, not only the ones the book leans on.** *Transitions* v3.0 is the
origin of the closure operator R, the excess E, and the two failure modes on which Part IV of this
compendium and Chapter 12 of the main volume both rest. Thirty of its sections are load-bearing
here, and the main volume's Appendix G sets those thirty out with the objects that stand on each.
This section is the other half of that address: **all seventy-seven sections, in order, with what
each states and whether this work rests on it.**

**Why the forty-seven are printed at all.** An index of indices that lists only what a work used
tells a reader nothing about what it declined. The forty-seven are the paper's own ordering
arguments, its withdrawals, its axis index and its open join — several of them corrections to
sections this book *does* use, and one of them, §10.2, a correction to §2.8 that reverses a claim
about the measure. A reader who wants to know whether a result of this book was picked from a
larger field or was the only thing on offer can only answer that from the complete list.

**The count.** Seventy-seven sections; thirty relied on, forty-seven not. The paper remains the
origin and is named as such throughout; this table and Appendix G are the address.

| § | what it states | in this work |
|---|---|---|
| 0.1 | Five working protocols, the first of which is commit before looking: a position is written down before any retrieval, and the retrieval scores it. | not used |
| 0.2 | The Admission Law. An entry's grade bounds the operations it may enter; a derived entry carries the minimum grade of its inputs, and no derivation raises a grade. | not used |
| 0.3 | A biconditional licenses a merge only if it holds at every rung of the graded axis. Merging on a fact true at one point and then grading the axis is the error. | not used |
| 0.4 | Operator reliability, measured. Predictions aimed at logical structure scored 4/4 on three consecutive tests; predictions of how a field regards a claim scored 1/4, and that class was barred from entering. | not used |
| 1.1 | The definitions: the value sets, the monotone upper envelope φ̂ᵢⱼ of one coordinate against another, R(X) as every point of the observed box respecting all envelopes, and E(X) as its excess. | not used |
| 1.2 | X ⊆ R(X), and therefore E ≥ 0. Extensivity, proved. | **rests on it** — Appendix G |
| 1.3 | R is a closure operator — extensive, monotone, idempotent. The closed sets form a Moore family. | **rests on it** — Appendix G |
| 1.4 | R is the closure of a binary constraint network under monotone binary projections, and E(X) = 0 exactly when the network is globally consistent. | **rests on it** — Appendix G |
| 1.5 | X ⊆ BPC(X) ⊆ R(X), so E > 0 is in principle ambiguous between genuine inconsistency and envelope coarseness. Computed for every object in the paper, R = BPC exactly and the ambiguity does not arise. | not used |
| 1.6 | The two failure modes — order and arity — and the third case: a vocabulary may not be indexable at all. | **rests on it** — Appendix G |
| 1.7 | Six blindnesses of the closure. A derived coordinate cannot repair it: the box grows by that coordinate's value count while \ | **rests on it** — Appendix G |
| 1.8 | The closure rule. A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other. | **rests on it** — Appendix G |
| 1.9 | E requires density, asymmetrically. E = 0 is informative at any density; E > 0 at low density measures sparsity and nothing else. | **rests on it** — Appendix G |
| 1.10 | The two named theorems covering Λ — Freuder 1982 and Montanari 1974. Neither reaches either violation index. | **rests on it** — Appendix G |
| 2.1 | The tower closes at every level for every statistics order. Parastatistics of order m gives capacity m(4ℓ+2); m = 1 reproduces the canonical tower exactly. | **rests on it** — Appendix G |
| 2.1b | Closure is not scheme-contingent. Rebuilt in LS, LK, jK and jj: the coupling scheme is not a coordinate. | **rests on it** — Appendix G |
| 2.2 | Λ₉'s constraint graph is a tree of nine nodes and eight edges, so Freuder applies. The admissible Pauli cut gains a cycle and loses the guarantee. Λ₉ is the last tree level. | **rests on it** — Appendix G |
| 2.3 | All six density values reproduce once three non-obvious exact sets are used — the spin set of f^g by microstate enumeration at axis 9, terms genuinely new at occupancy v at axis 10, and the J values of terms of ℓᵏ at axis 11. | not used |
| 2.4 | Closure and exactness are incompatible. The exact coupling triangle is ternary, outside the closure-preserving class: Λ₁₂ falls 70,905 → 22,275 and E goes 0 → 35,570. | **rests on it** — Appendix G |
| 2.5 | Four monotone variants of the ℓ-bound close and two non-monotone variants do not. The decisive pair, ℓ ≤ ⌊n/2⌋ and ℓ ≤ \|n−3\|, have identical cardinality at 32,535 cells and opposite outcomes: monotonicity is the discriminant, not cardinality. | not used |
| 2.6 | The Standard-Model Extension lifts the Coulomb accidental degeneracy but moves no quantum number, because ℓ ≤ n−1 follows from node counting. The lattice does not individuate universes by Lorentz structure. | not used |
| 2.7 | Transit admissibility is directional. Outward is unobstructed; inward is not, because a cell with occupancy beyond our Pauli bound fails the one-dimensional index before any question of joint structure arises. | not used |
| 2.8 | Three things locate a transition and the index certifies only the first. The lattice says what exists; the order says what is near, and only 24.2% of the 475,800 pairs of Λ₈ cells are ordered by componentwise domination; the measure says what it costs, and it is external. | not used |
| 3.1 | The eighteen-column table has E = 36, and re-indexing period as n + ℓ is not what repairs it — neither is contiguity. ℓ is fully determined by group: s at 1–2, d at 3–12, p at 13–18. | not used |
| 3.2 | Of the 36, twenty-five — 1d, 1p and 2d — could never hold an element, being forbidden by ℓ ≤ n−1: the footprint of a law the coordinate system has no axis for. The remaining eleven are 3d, deferred past 4s by the Madelung order, and period 1 group 2. | not used |
| 3.3 | The periodic table is not an analogy for the violation index; it is the other failure mode, and having both is what makes the distinction visible. Ordering failures are repairable because re-ordering acts on one relation at a time. | not used |
| 4.1 | Λ₉ is the transit level. 1,169 of 1,654 cells are composable — the first level at which a transition has a defined endpoint, and the last that is a tree. | **rests on it** — Appendix G |
| 4.2 | The composition graph is the line digraph of a quiver on 33 atomic states, with 27,027 edges. A loop sits at every vertex, so return is available in one step. | **rests on it** — Appendix G |
| 4.3 | Girth exactly 4. Unit-step adjacency coincides with the covering relation at 6,658 edges either way, so the lattice is gap-free. | **rests on it** — Appendix G |
| 4.4 | Molecular transit. Feasibility decays geometrically at 2.51 per atom; the Helly number is at least 5 and at most 144. | **rests on it** — Appendix G |
| 5.1 | The coordinates of the violation index, and the position this work occupies in it — two components fixed by measurement rather than choice. | **rests on it** — Appendix G |
| 5.2 | Chronology violation requires the causal ladder, non-unitarity at the Lindblad rung and arbitrarily small ANEC violation — and not signalling, cloning, nonlinearity or loss of microcausality, each of which appears under Deutsch's prescription and not otherwise. | not used |
| 5.3 | 2,370 cells, E = 30, all of it genuine global-consistency failure. The excess is exactly 1 × 30 and the core is a single cell. | **rests on it** — Appendix G |
| 5.4 | The failing triple is the unique minimal support. Arity exactly 3, one generator; no single literature pays for it. | **rests on it** — Appendix G |
| 5.5 | The repair space is closed, and both directions fail for opposite reasons: adding fails because the box inflates, merging fails because the envelopes coarsen. Two lines cover all six repairs. | not used |
| 5.6 | Objects are thresholds. Of the 1,146 cells permitting a macroscopic wormhole, 1,116 pay with a preferred frame, 714 with non-unitarity and 756 with signalling — and none pays with nothing. | not used |
| 5.7 | The defect does not scale. The core is one cell at every resolution, and the multiplicity moves non-arithmetically. | **rests on it** — Appendix G |
| 6.1 | Of the nine coordinates, five are fully conflated, two partially, and two are clean. | not used |
| 6.2 | Every conflation merges an inert rung with a potent one, and that is not coincidence: the index was graded from papers about what breaks, and the papers that matter for atomic structure are about what holds. Two different literatures. | not used |
| 6.3 | None of the five was findable from inside. All surfaced from a specific question about a named theorem; inspecting the coordinate list finds none of them. | not used |
| 6.4 | Audit 22. For every coordinate whose term appears in a cited theorem, state what the theorem means by it, state what the rung means, and record match, conflation or unchecked. Its output is a debt, not a pass. | not used |
| 6.5 | The corrected alphabet — what becomes expressible once the conflated letters are split. | **rests on it** — Appendix G |
| 7.1 | Every structural result survives at fifteen letters: E = 816, one cell, arity 3. | **rests on it** — Appendix G |
| 7.2 | Recomputed under the documented nine-letter conventions the linearisation figure reproduces exactly at 7,734; the slide figure does not, and the earlier 8,856 is refuted outright, the operation acting on a three-coordinate object whose box is at most 40. | not used |
| 7.3 | The frontier formulas in closed form, d(c) and s(c), verified on 1,500 sampled cells with zero distance mismatches. | not used |
| 7.4 | The spin-statistics hypotheses have three letters and no proxies. 900 of 18,072 cells — 5.0% — have the Pauli lattice guaranteed, and we are among them; for the rest parastatistics becomes available and Λ₈ can be 1,600 rather than 976. | not used |
| 8.1 | A charge relation has three parts, not two: trigger, what incurs the charge; currency, what may pay; and jurisdiction, where the charger has standing to collect. | not used |
| 8.2 | A jurisdicted forcing and an unjurisdicted disjunction are the same object. A theorem holding only under a scope condition is inherently ternary, and no further physics removes the scope. | **rests on it** — Appendix G |
| 8.3 | Buniy's jurisdiction is necessary, and the counterexample is the ghost condensate of Creminelli, Luty, Nicolis and Senatore (2006). It escapes through higher-derivative structure, not Lorentz violation: the Lagrangian is manifestly Lorentz-invariant and the vacuum breaks the symmetry. | not used |
| 8.4 | The vocabularies. A locally covariant QFT is a functor with exactly four parts, which replaces the seven-vocabulary partition. | **rests on it** — Appendix G |
| 8.5 | Retained as history, not current analysis. Built on the seven-vocabulary partition that §8.4 derives away and §12.3 withdraws, and kept because §8.6's correction is only legible against what it corrects. | not used |
| 8.6 | An earlier draft placed the exclusion of macroscopic wormholes in a component the law index cannot reach, and made that the reason six repairs failed. Rebuilt on the four derived vocabularies, that is wrong: the system is connected and the severance was an artefact. | not used |
| 8.6b | Graham–Olum is listed by the charger index as firing and should be conditional. A conjecture with a sufficiency proof is a third category the index does not have. | not used |
| 8.7 | Retained as history. No configuration is a connected tree; Hartman must drop V2 rather than V3, and reducing Wall backfires because its V1–V5 edge is coupling's only connection. | not used |
| 8.8 | Checked twice, including through an adjacent literature: the general ANEC-from-causality argument is flat-space, and curved-space results exist only with a V2 condition retained. | not used |
| 9.1 | Three measures, and the third did not exist. E measures what an index cannot carry; the vocabulary debt measures what it has not checked it carries correctly, 32 of 48; nothing measured what was never named at all, and seven law-classes appear in cited sources with no letter. | not used |
| 9.2 | The axis index itself — nine cells in a box of 5,184. | not used |
| 9.3 | Pair-completion. The nine leave four value-directions unoccupied, and every hand-found axis outside the box occupies a pair — never one direction, never three. | not used |
| 10.1 | Every vocabulary index closes; the charger index does not. The defect sits in V1, on the V1–V3 edge, and in the partition itself. | **rests on it** — Appendix G |
| 10.2 | §2.8 is corrected. A faithful measure exists and compresses 976 cells to eighteen values, because any strictly monotone function of the coordinates is automatically faithful. | not used |
| 10.3 | Λ audited. The conflation rates of Λ and the violation index are proportionally indistinguishable; the causes differ, V1 conflating because two literatures used one word. | not used |
| 10.4 | Six independent curved-space routes to the ANEC. Five require a Killing field or a horizon generated by one; the sixth yields a weighted bound instead. | **rests on it** — Appendix G |
| 10.4b | The one open cell. Following §10.4's target down gives a single surface class and a single condition, and the target is a boundary point rather than a region; an isolated horizon has Θ = 0 exactly. | not used |
| 10.4c | C1, computed. The presymplectic potential on a null surface contains no transverse derivative, so Ω is block diagonal and the algebra factorises over generators. | **rests on it** — Appendix G |
| 10.4d | C2, the open condition — whether the state respects the decomposition. Independent of the Hadamard condition, which says nothing at finite transverse separation. | **rests on it** — Appendix G |
| 10.4e | Half-sided modular inclusion is the converter from algebra to geometry: Borchers and Wiesbrock return the affine group acting on a line. | **rests on it** — Appendix G |
| 10.5 | Status is one bit per vocabulary and the partition forces one-hot — every term is physical in exactly one vocabulary, or in none. | **rests on it** — Appendix G |
| 10.6 | The chain, primary-sourced, with a fifth caveat on T0: Reeh–Schlieder is a theorem in Minkowski space, proved from analyticity, the spectrum condition and the action of the Poincaré group, and in curved spacetime it is a property established for free massive fields. | not used |
| 10.7 | Five instances of one shape, the last stated as physics rather than bookkeeping: gauge redundancy is the bookkeeping needed to describe subsystems relationally in a gauge-invariant system. | not used |
| 12.1 | The promotion ledger. Everything promoted is about the method and everything held is either a general claim or a physical number — the instrument is better characterised than anything it measured. | not used |
| 12.2 | Twelve claims withdrawn with their causes, among them defect 60, an unbounded Helly number, projection-covariance as a scaling law, and the defect growing with jurisdiction count. | not used |
| 12.3 | The withdrawals post-dating the previous draft, several of which correct claims that draft asserts. | not used |
| 12.4 | The numeric debt. Of six claims carried with no dataset behind them, five clear on recomputation and one is corrected — refuted by a bound, the slide operation acting on a three-coordinate object whose defect cannot exceed 40. | not used |
| 12.5 | Audit 23 is the only external validation in the construction and it passes: ten published LS term tables reproduced exactly, zero microstate discrepancies against C(4ℓ+2, k). | not used |
| 12.6 | Thirty instances of one class — a conclusion drawn from a comparison that was not licensed. The arithmetic was correct in every case; the warrant was not. | not used |
| 12.7 | Four of the seven propositions are refuted, two unassertable and one conditional. None closes the index, and with Buniy's jurisdiction established as necessary, P5's conditionality no longer decides the matter. | not used |
| 13.1 | For a product with no linking constraint every cross-envelope is vacuous, so R(A × B) = R(A) × R(B). With E(Λ) = 0 the join of Λ with the violation index gives E = 976 × 30 = 29,280: the defect is extensive. | not used |

**Reading the third column.** *Rests on it* means at least one object of this work — a lemma
label, a chapter, or a Register entry — cites that section; Appendix G names which. *Not used*
means no object cites it, and carries no judgement on the section: §12.5's external validation and
§13.1's extensivity result are both sound and both simply outside what this book claims.

