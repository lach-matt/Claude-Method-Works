# `tools/cypher.py` — the cypher analysis run as a program

The cypher analysis is §33 of The Method 1.6: *given an object, ask each of the languages in turn
whether it can speak of it, and read the answer off the pattern of who answers and who does not.*
This is that procedure as a program.

```sh
python3 tools/cypher.py --selftest                       # against the corpus's own numbers
python3 tools/cypher.py --list-rosters
python3 tools/cypher.py --cells cells.tsv --name L_x --roster 1173
python3 tools/cypher.py --index spec.json --roster 1173 --pairs   # the C(n,2) arithmetic
python3 tools/cypher.py --index spec.json --roster 33.1 --json
```

Stdlib only, Python 3.11+. No dependencies, so an audit can run it from any tree.

**Limits.** `order`, `geometry` and `statistics` search the ambient product by depth-first
backtracking with early pruning, not by walking it. Every operator here is a conjunction of
constraints on few coordinates at a time — order and geometry on pairs, statistics on k-subsets —
so a constraint is tested the moment its last coordinate is bound and a failure prunes the whole
subtree. The indexes this runs on are sparse in their box (the tower falls from 14% fill at Λ₈ to
0.42% at Λ₁₃), so the search visits a small fraction of the product. A 4.8-million-cell box that
never completed under product enumeration now returns in about 17 seconds.

Older text, still true of the closures: `algebra` and
`information` iterate a closure quadratic in the working set. All are capped and all
refuse legibly: `--max-box` (default 8,000,000) and `--max-pairwise-cells` (default 8,000), with
`--algebra-budget` (default 20,000) bounding closure growth. The whole self-test takes about
thirty-five seconds.

## Why it exists

§33.2: **a language that falls silent is the finding.** An object every language describes is
well-posed and ordinary; an object some describe and others cannot is telling you what *kind* of
object it is, and the identity of the silent language names the kind. Run by hand this is
error-prone in one specific way — it is very easy to record "silent" for a language nobody
actually ran. Register 1172 found five such language/index pairs, and the Comparison Audit
carries them still.

## Three things it refuses to do

**1. It never prints SILENT for a language that was never run.** There are four states, not two:

| state | meaning |
| --- | --- |
| `SPEAKS` | the operator ran and returned an admitted set (or a declared witness) |
| `SILENT` | the operator ran and its precondition failed — *this is the finding* |
| `NOT-RUN` | nothing was measured. An assertion, not a result. |
| `REFUSED` | a resource cap was hit. The operator never ran; raise the cap and rerun. |

`REFUSED` exists because the alternative is worse than a crash. Without it a compute limit reads as
a silence, and a silence is a *finding* — the tool would manufacture "geometry is silent on this
index" out of a box that was merely too big to enumerate. The self-test asserts that no resource
refusal is ever reported as a silence.

**2. It never counts agreement at two coordinates as evidence.** Register 1175: at `d = 2` there
is one pair, so pairwise consistency and the cell coincide and every language agrees for no
reason. The periodic table, Janet and the calendar were all read this way and all reported
"agree". Such a run is marked `DEGENERATE` and the agreement verdict is withheld.

The trap is a false *agreement*, so that is all the guard withholds. A **disagreement** at low
dimension is real information and is reported — the Kreuzer–Skarke slice sits at `d = 2` and its
languages genuinely differ (order 540, geometry 545, information 498), which is a finding, not an
artefact. Statistics is silent there and the report says so.

**3. It never picks the roster for you.** `--roster` is required.

## The roster is data, and the docket is open

Which languages there are is **unruled**. The volumes print at least three rosters:

| roster | languages | note |
| --- | --- | --- |
| `1173` | order, algebra, analysis, geometry, information, statistics, documentary | Register 1173: logic is the *mechanism*, not a language. Five operator-bearing give C(5,2) = 10, statistics sixth, documentary seventh. |
| `33.1` | order, analysis, algebra, geometry, information, statistics | The roster the cypher's own chapter prints. |
| `20.2` | order, geometry, arithmetic, calculus, logic, constraint-language | The chapter §33.1 cites for its principle. Shares **two names** with §33.1's six. |

This is docket **20x-04** (six languages against seven) and **20x-09** (C(5,2) against C(6,2)),
both open and awaiting a ruling. The tool takes no position: it runs whichever roster you name and
marks every language it cannot map as `NOT-RUN`. Under `--roster 20.2`, four of six read
`NOT-RUN` — which is the docket, made visible rather than smoothed over.

## The operators

Every verdict carries a **status**. `PINNED` means the corpus defines the operator at the
precision a program needs. `ADOPTED` means the definition was reconstructed from the corpus's own
language-pairings plus the cited literature, corroborated by reproducing recorded numbers, and
adopted by ruling. The provenance is kept rather than flattened to `PINNED`, so a later ruling can
still move it. `DECLARED` means the language answers in a currency other than an admitted set.

| language | status | operator |
| --- | --- | --- |
| **order** | `PINNED` | ℛ, §32.4.1. `ℛ(X) = {x ∈ box : xᵢ ≤ φᵢⱼ(xⱼ) ∀ i≠j}`, `φᵢⱼ(a) = max{yᵢ : y ∈ X, yⱼ ≤ a}`. Matches the seated instrument `rclose.py`. Moore 1910; Deville, Barette & Van Hentenryck 1999. |
| **statistics** | `PINNED` | Max-entropy on the order-*k* marginals. IPF sends a cell to zero exactly when one of its *k*-projections is unobserved, so the support *is* the *k*-wise marginal support. Register 1174; Deming & Stephan 1940; Ireland & Kullback 1968. |
| **geometry** | `ADOPTED` | The integer points of the polytope `A x ≤ b`, relaxed to the two-variable rows the method's `A` actually has: admit `x` when every 2-D shadow `(xᵢ, xⱼ)` lies in the convex hull of that shadow of `X`. Carathéodory 1911; Schrijver 1986. |
| **algebra** | `ADOPTED` | The sublattice closure — iterate coordinatewise meet and join to a fixed point. §7.3; Birkhoff, *Lattice Theory* (1940). |
| **information** | `ADOPTED` | The seed and its regrowth: take the join-irreducible elements of X and close them under join. Birkhoff 1937 — every element of a finite distributive lattice is a join of join-irreducibles, so a distributive index regenerates from its seed exactly. This is the compendium's own object: *"the matrix A and nothing more, from which all 976 cells regenerate."* It also reports per coordinate whether removing it loses cells, and flags a coordinate that individuates every cell as a **key, not an axis** — register 1356, the fault that voided Λ_ladder's closure. |
| **analysis** | `DECLARED` | Not an admission operator: it asks whether a continuous law exists, answered by a fit or by the absence of a derivative. Must be declared with a witness, else `NOT-RUN`. |
| **documentary** | `PINNED` | Silent by construction. No closure mechanism exists — it returns a citation, not a binary, which is why it earns no operator row. P20's table; register 1173. |

## The five, measured

Which languages are operator-bearing is not declared to the tool — it is **measured**. Register
1173's own test is *"a language earns its row when logic can operate on it and get a binary
back"*, so the tool counts a language as operator-bearing on an index when it actually returned an
admitted set, and computes C(n,2) from that. `--pairs` prints the claim beside the measurement.

Run against Λ under `--roster 1173`:

```
operator-bearing, CLAIMED by roster 1173 (5): order, algebra, analysis, geometry, information
    -> C(5,2) = 10, roster asserts 10
operator-bearing, MEASURED on this index (5): algebra, geometry, information, order, statistics
    -> C(5,2) = 10
    claimed but returns no binary: analysis
    measured but not claimed:      statistics

10 of 10 pairs agree.
```

**The count survives and the membership does not.** C(5,2) = 10 still closes, and all ten pairs
agree on Λ — but the five are not the five register 1173 names. `statistics` returns a binary per
cell and is operator-bearing by 1173's own criterion; `analysis` does not, and leaves the five.

The two special rows are therefore `analysis` and `documentary`, and they are special for
**different reasons** — which is the part register 1173's three levels do not yet cover:

* **documentary** has no mechanism at all. It returns a citation. It is `SILENT` by construction.
* **analysis** has a mechanism — a fit — but it returns a *magnitude*, an R² or a slope, not a
  binary. Logic cannot operate on it to get a cell decision, so it cannot join the pairwise
  arithmetic, but its silence is a real finding when it comes (a finite set of surds has no
  derivative) and must be declared with a witness rather than assumed.

The discriminating run is the periodic table at three coordinates, where the same five give
**1 of 10** pairs agreeing — order and algebra alone, both at E = 100, against geometry 83,
information 24 and statistics 0.

## Coordinates must be ordinal, and the order matters

ℛ is a monotone staircase closure, so every coordinate needs a value order. §20.3 is the reason:
written as a congruence the parity rule gives `E = 750`; written in spectroscopic naming the same
law is monotone and `E = 0`. *The notation was the coordinate that made the rule expressible.*

The tool infers numeric order where it can. Where it cannot it falls back to lexicographic **and
warns** — a lexicographic fallback silently changes E. Declare the order in a JSON spec:

```json
{
  "name": "L_x",
  "coordinates": ["period", "group", "block"],
  "value_order": {"block": ["s", "p", "d", "f"]},
  "cells": [[1, 1, "s"], [1, 18, "p"]],
  "declared": {"analysis": {"speaks": true, "witness": "Moseley R^2 = 0.998 (reg 1380)"}},
  "outputs": ["delta"]
}
```

`outputs` drives the **singleton criterion** (§33.4): an index is closed when its output class is
a singleton. Two outputs mean the observer is still choosing which to read, and ℛ cannot see it —
Λ_var passes ℛ with both δ and n\* present because both land in the same cell. Declare more than
one and the report says `SINGLETON FAILS`.

## `K.langclose`

The theorem-shaped result of register 1176 — **E(X) = 0 if and only if the languages agree** —
is Beeri, Fagin, Maier & Yannakakis (1983) read as an equivalence: global and local closures
coincide exactly on acyclic structures. The tool tests it on every run and reports `holds` or
`FAILS`. A disagreement between languages at `E = 0` is the one thing the cypher forbids, so a
`FAILS` is a result worth a register entry, not a bug to route around.

Note that register 1176's own basis is six indexes and three operators. The defect census flags
its "without exception" as `C9-OVERGENERALISATION-WORD` (row 1321). "Theorem-shaped" is the
right hedge.

## `--selftest`

The fixtures are the corpus's own recorded numbers. Failures are reported, never tuned away.

| fixture | asserted | source |
| --- | --- | --- |
| Λ, 8 coordinates at the caps of §7.4 | 976 cells, box 6,912, `E = 0` in order, geometry, algebra, information and statistics | §7.4, §10, MC "closed under coordinatewise ∨ and ∧"; "the integer points of the polytope `A x ≤ b` are the lattice exactly" |
| Λ, statistics by marginal order | order-1 admits 6,912; order-2 admits 976 | register 1174 |
| periodic table, period × group | 90 cells, `E = 36` | §21.1; DEFERRED records 90 cells at E = 36 |
| periodic table, + block | `E(order) = 100` against `E(statistics) = 0`; information 24 | register 1175 |
| Janet, n+ℓ × ℓ | `E = 0` | register 1175 |
| calendar, month × day | 365 cells, box 372, `E = 7` | §21.1; IoI *The calendar* |
| box ordering, `l ≥ w ≥ h` | 35 cells, box 125, `E = 0`, **all 10 pairs agree** | register 1176's own agreeing fixture |
| Λ, all pairs | **all 10 pairs agree** | register 1176 |
| Kreuzer–Skarke, χ = ±6 slice | 208 cells, `E(order) = 540`; 498 join and 498 meet failures of 21,528 pairs; what ℛ admits carries 112 diagonal cells from (13,13) to (131,131), 5 distinct χ, and h¹¹+h²¹ from 26 to 262 | §31.3.4; Candelas, de la Ossa, He & Szendrői, *Triadophilia*, ATMP **12** (2008) 429 |
| nuclide chart, (Z, N) | 52 cells at Z ≤ 7, `E = 9`, and the nine admitted-and-absent cells named **exactly**: He-5, He-7, Li-10, Be-8, Be-13, B-9, B-16, B-18, C-21 — stable at 9 across four proton-number cutoffs (Z ≤ 7, 8, 9, 10) | IoI *The nuclide chart*; registers 298, 388, 390; AME2020 |
| the box seed law | a full box `c^d` seeds at `d + c − 2`, verified by exhaustive minimum-seed search at (2,2), (3,2), (4,2), (2,3), (3,3) | MC §S, the box seed law |
| the Carathéodory bound | `seed ≥ breadth = d` for a product of `d` chains, on every box tested | MC §S; Carathéodory 1911 |
| degeneracy guard | fires at `d = 2`, not at `d = 3` | register 1175 |

Current state: `SELFTEST OK`.

That the three `ADOPTED` operators each reproduce a number recorded independently of them is the
evidence for their definitions, and is why they were adopted. Λ's 976 cells regenerate from
**18 join-irreducibles** — the strongest of the three, because nothing was fitted to it. If a
later ruling contradicts one, the operator changes and the self-test is what will catch it.

## A worked reading, from the repository's own data

`method/members/MEMBERS-126.tsv` holds 562 Rydberg series members over eight species. Deriving
`(Z, charge, ℓ, 2S+1)` from `species` and `designation` gives 33 distinct channels, and the cypher
reads them:

| language | admits | E |
|---|---|---|
| order | 150 | 117 |
| algebra | 150 | 117 |
| geometry | 108 | 75 |
| information | 98 | 65 |
| statistics | 47 | 14 |

**1 of 10 pairs agree** — order and algebra — and `K.langclose` holds: the languages disagree and
E > 0. The same shape appears on the periodic table at three coordinates: order and algebra
agreeing, statistics tightest, everything else apart. Two objects is not a law, and the defect
census flags exactly this kind of generalisation (`C9-OVERGENERALISATION-WORD`) — it is recorded
here as an observation to test, not a finding.

The derivation above drops 161 of the 562 members, and that is the second finding below rather
than a fault in the parse.

## The seed

`min_seed(ix, cap)` computes the least `G` with `ℛ(G) = X` — NP-hard in general (§14.5.7), so it
is exhaustive to a cap. The **box seed law**, `d + c − 2`, and its Carathéodory lower bound
(`seed ≥ breadth = d` for a product of `d` chains; MC §S) are asserted in the self-test.

It is not the geometry evidence. That is the Peck/Sperner check below, against Stanley 1980. Λ's
own seed is recorded at 7 and is **not** computed here: the search is exponential, and a greedy
search for a 7-cell generator did not find one within budget. That is a limit of the search, not
evidence against the 7, and it is not pursued.

## The tower

Λ₈, Λ₉, Λ₉′ and Λ₁₀ are fixtures and reproduce exactly — 976, 1,654, 1,561 and 2,535 cells in
boxes of 6,912, 27,648, 27,648 and 110,592. The volumes record `E = 0` at every stage **in order**;
the self-test asserts `E = 0` in **all five** operator-bearing languages at each, which is stronger
than what is recorded.

**Λ₁₁ to Λ₁₃ are not blocked on compute.** Λ₁₂'s box is 5.3 million and Λ₁₃'s 47.7 million, and
the pruned search reaches that scale. They are blocked on *definition*: Λ₁₁ adjoins `2J_c ≤ φ̂(k)`
and Λ₁₂ `2K ≤ 2J_c + 2f_max`, both envelopes, and the volumes say the exact sets "are not the
obvious ones" — the core's J at the eleventh is restricted to terms carrying the cell's own
multiplicity, not all terms of ℓᵏ. That is not stated to the precision a program needs.

## What outside literature predicts, and where it parts from the book

The corpus attributes Λ's shape to Sperner (1928), Dilworth (1950), Birkhoff (1937) and
**Stanley (1980)** — whose theorem is that the order-ideal lattice of a product of chains is
*Peck*: rank-symmetric, rank-unimodal and strongly Sperner. The book's own claim is that this
transfers **only in part**. Measured:

| prediction | measured | |
| --- | --- | --- |
| rank sequence over ranks 3–20 | `1, 5, 15, 34, 59, 87, 108, 121, 122, 115, 100, 79, 57, 37, 21, 10, 4, 1` | exact |
| rank-unimodal, log-concave at every interior rank | holds | ✓ |
| **strongly Sperner** — largest antichain = largest rank level | 122, certified by a Dilworth chain partition computed as a bipartite matching | ✓ |
| `976 = 8 × 122` | holds | ✓ |
| Birkhoff seed — Λ is the down-sets of its join-irreducibles | **17** | ✓ |
| **rank-symmetric** | **fails** — 8 of 976 survive `x ↦ max − x`, none fixed | Peck does not transfer whole |

Sperner survives and symmetry does not, exactly as the book says. Two things came out of running it:

- **The rank skew is mislabelled, and the sign is the wrong way round.** MC §8.4 prints *"centre of
  mass 11.0666 vs midpoint 11.5, skew −0.43"* and attributes it to *"the third standardised moment
  of a rank distribution, Gauss (1809)"*. The rank sequence reproduces exactly, and the third
  standardised moment of it is **+0.14**, not −0.43. The printed −0.43 is `11.0666 − 11.5`, the
  displacement of the centre of mass from the midpoint — a real quantity, correctly computed, but
  not the moment cited. Read as a skew it reports the asymmetry backwards: Λ's right tail is the
  longer one, nine steps down from the peak against eight on the left.
- **Two sections disagree about the same eight cells.** §8.4's rank-skew entry says *"only 8 of 976
  cells **fixed** by x ↦ max − x"*; the Sperner entry says *"8 of 976 cells **survive** … none
  fixed"*. Measurement supports the second: 8 survive, 0 are fixed.

Both are recorded here rather than repaired — the volumes are the store of record.

## Known gaps

- **The calendar at three coordinates is not built.** The 2-D calendar is a fixture and reproduces
  at `E = 7`. Register 1175's rebuild adjoins weekday as a third coordinate, and which weekday
  mapping it used is not stated precisely enough to reproduce.
- **`k ≥ 1` and the two boxes.** The eight marginal-exclusion counts of MC §11 reproduce exactly —
  but only on a **9,216**-cell box with `k` from 0. On the 6,912-cell ambient box quoted beside
  them, `k ≥ 1` can never fail and excludes 0, not 25. Both boxes are legitimate (6,912 is the box
  after the floor is applied); the table and the box quoted next to it are measured on different
  ones.
- **The violation index cannot be built, and the corpus says so first.** The IoI calls it *"the one
  index this work reasons about without holding — its cells are not printed anywhere."* That is
  confirmed rather than worked around. Its nine letters and rungs ARE printed, and the box
  reproduces exactly at **19,440**; so does one recorded reading — the arity-2 variant
  `NEC ≥ 3 → U ≥ 1` gives **E = 0**. But the printed arity-3 constraint
  `NEC ≥ 3 ∧ X = 0 → U ≥ 1`, taken as a *definition*, yields 18,792 cells at `E = 648`, not the
  recorded 2,370 cells at `E = 30`. The constraint is a model applied to the index, not the index,
  and the 2,370 cells are not recoverable from anything in print. No cell set is fabricated to
  close the gap.
- **`arithmetic`, `calculus`, `constraint-language`, `logic`** have no ruled operator mapping and
  read `NOT-RUN` under `--roster 20.2`.
- **Register 1177's geometry percentages are not reproducible, and not because the operator is
  wrong.** They read *70% of the faces and 28% of the corners* against Λ_spectra at E(order) =
  6,195. Λ_spectra proper — `(Z, charge, ℓ, 2S+1)` over 104,832 cells — now **closes at E = 0**,
  so those numbers describe a superseded state of the index, before register 1139's Hund
  constraint was carried in (register 1178 records the step down: order 6,195 → 2,879, statistics
  806 → 429, geometry 3,773 → 1,984). This is docket 15's class, retired-basis, at a new object.
  The cell set of the superseded state is not in the tree, so the check cannot be run at all.
- **`2S+1` is not defined on every channel it is asked of.** Of the 562 members in
  `MEMBERS-126.tsv`, 266 are LS-coupled, 135 jK-coupled — both carry a multiplicity — and **161
  are jj-coupled** (`ns (3/2,1/2)* J=1`), which has none. All 161 are **Si I**, 161 of that
  species' 228 members. An index keyed on `(Z, charge, ℓ, 2S+1)` therefore cannot hold 71% of
  Si I's measured series, and drops them without saying so. Adjacent to register 1356's class — a
  coordinate that does not individuate every cell of the object it is put on.

- **The two pairs the volumes never exhibit.** Under the *measured* five, C(5,2) = 10 closes on Λ.
  Under the five register 1173 *names*, MC's ten-pair enumeration exhibits only eight of the
  required ten — `algebra–analysis` and `geometry–information` appear nowhere in the four volumes,
  and two of the ten it does exhibit (`logic–algebra`, `logic–analysis`) rest on logic, which 1173
  demotes from a language. The measurement above is the cleaner route to the same count.
