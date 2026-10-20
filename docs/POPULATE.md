# `tools/populate.py` — an element on every axis of every index

Give it a ground-state atomic number and it returns that element, and every ion of it, on every
coordinate the books define.

```sh
python3 tools/populate.py --element K
python3 tools/populate.py --z 19 --charge 1
python3 tools/populate.py --element Fe --json
python3 tools/populate.py --axes            # every axis, and where it comes from
python3 tools/populate.py --equation        # the method equation against the index
python3 tools/populate.py --check-B         # the Pauli bound against both configuration tables
python3 tools/populate.py --selftest
```

Stdlib only, Python 3.9+.

## The two halves

Register 1206 names the architecture: *"the two halves of the method equation meet for the first
time on this index"* — **ℛ places cells and the channel equation values them.** This runs both.

ℛ is imported from `tools/cypher.py`, where it is the `PINNED` order operator of §32.4.1, rather
than reimplemented. The channel equation is register 1205's final form. The observed ground
configurations are `LW1-ground.py`, a seated bundle member (register 1306, NIST ASD 5.12, *read* not
computed), and the tower is `tower-2.py`; both are imported **by path** and never transcribed, per
`CLAUDE.md` §5.

## What it populates

| group | axes | status |
| --- | --- | --- |
| identity | Z, symbol, configuration, ground level, electron-count check | `READ` |
| per subshell | n, ℓ, occupancy, capacity 2(2ℓ+1), n+ℓ, full? | `DERIVED` / `PINNED` |
| layout | periodic table 2-D (period, group), 3-D (+block), Janet (n+ℓ, ℓ) | `DERIVED` |
| structural half | ℛ over the layout: 90 held, 126 admitted, E = 36 | `PINNED` |
| channels, per ion | charge, Nₑ, ℓ, mult, p, n₀, B, δ measured, δ by equation, residual, grade, witness, bound | `READ` + `PINNED` |
| collapse | C(Z, ℓ) | `RECOVERED` |
| Λ₈ | the element's cells as the record builds them (every transition among its occupied subshells) | `RECOVERED` |
| ionisation ladder | the steps between the ions as transition cells, the seven constraints, the caps each needs | `RECONSTRUCTED` |
| **series limit** | the measured ionisation limit, its uncertainty and its provenance | `READ` / `FITTED` |
| equation domain | per channel: validated, or extrapolated and why (the record's rule over the csv's notes) | `DERIVED` |
| ground basis | Z = 103 to 108: NIST holds the ground level alone; the ionisation energy's basis | `READ` |

`--axes` prints the full inventory with a source for every row.

## The series limit — the twenty-sixth axis

The limit is the quantum defect's own denominator, `δ = n − Z√(R/(limit − level))`, and for a long
time it was the one input the index used without indexing. **It is never computed here.** Register
3249 is what happens when it is: Li III's limit was written as the bare Coulomb `Z²R = 987,635.841`
and every channel moved when it was fitted from the series instead — **987,662.29 ± 0.36, higher by
26.45**. The compendia state the rule outright, that the limit *"must be measured, not computed"* and
that writing it as a formula is *"the single most damaging thing that can be done to a channel."*

So the axis is `READ` where a source printed the value and `FITTED` where a run recovered it, and it
is **`None` where neither** — thirteen stages are banked out of every stage of every element: the
four of the registers, and since 2026-10-17 the nine neutral limits COORDINATES-2.13 prints in the
bound note of its 25 rows from the 2026-08-14 NIST fetch (B, Na, Al, Ga, In, Cs, Lu, Tl and Fr I),
`READ`. The CSV prints them with no unit; they are cm⁻¹, because each equals NIST's ionisation
energy for that spectrum in cm⁻¹ to every printed digit and the rows' defects recompute from NIST's
levels only in that unit (`tools/seriesdefect.py`, below). An absent
limit is not filled in: register 2469 withdrew ten Ba III channels built on an invented one, because
*"a quantum defect is n − Z√(R/(limit − level)) and is meaningless without it."* Absent means
levels-only.

**And the deficit is where QED sits on this index.** Register 3253: *"the QED was real and it was in
the LIMIT, not in the levels."* Measured against the **reduced-mass** baseline `Z²R_M` — register 3357
needed the reduced mass twice, once in the defect and once in the baseline, a bare `Z²R∞` baseline
implying a spurious `Z^6.4` — the deficits are `103.94`, `329.80`, `816.68` at `Z = 3, 4, 5` and the
`Z⁴` law holds. Register 3353 identifies what they are: **the Sommerfeld–Dirac relativistic term less
the 1s Lamb shift**, at a ratio of **0.8849 ± 0.0069**, constant to under one per cent. The selftest
pins all of it, including the wrong baseline, so the `Z^6.4` fault cannot creep back.

**The deficit belongs to one-electron stages only.** `Z²R_M` is the limit of a one-electron ion, so
`limit_deficit()` returns `None` unless the charge is Z. Before that guard (2026-10-17) the report gave
the two banked many-electron stages, B IV and P IV, "deficits" of −651,301 and −24,274,907 cm⁻¹
against a baseline that is not theirs, and called them the relativistic term less the Lamb shift.

## Status, carried and not flattened

In `cypher.py`'s vocabulary, extended by one:

- **`READ`** — a measurement, from a member or the mirror.
- **`PINNED`** — the corpus defines it at the precision a program needs.
- **`DERIVED`** — arithmetic on a `READ` or `PINNED` quantity, nothing added.
- **`RECOVERED`** — *not stated in any member*, but recovered by measurement from the index's own
  computed column and consistent with what the registers say about it qualitatively.
- **`RECONSTRUCTED`** — the corpus states the object and its behaviour but not the form a program
  needs; reconstructed here, measured, and kept as such so a later ruling can move it.

## Three things it refuses to do

**1. It never prints a value without its status.** A `RECOVERED` defect and a `READ` one are
different objects and the report never merges them.

**2. It never silently places an element outside the caps.** Λ at §7.4's caps — (n, e, ℓ, k, f) =
(3, 3, 1, 3, 1) — admits almost no real element. Rather than truncate, the report says `OUTSIDE` and
names the cap that fails:

```
    Ar->Cl     (3, 1, 6, 1, 3, 1, 0, '-') 7/7      OUTSIDE: needs k>=6
    P->Si      (3, 1, 3, 1, 3, 1, 0, '-') 7/7      within 7.4
```

Every one of those cells satisfies all seven of §7.1's constraints — `7/7` — and is still not a cell
of Λ₈ *at these caps*. That distinction is §7.4's whole point and the report keeps it visible.

**3. It never repairs a disagreement.** Where the recomputed value differs from the recorded one the
report carries both. G0c: *when a reconstruction disagrees with the record, the finding is about the
reconstruction.*

## C(Z), recovered

Register 1190 says the collapse coordinate is *"read off the periodic table, not fitted — one
lookup"*, and register 1188 gives thresholds exactly: *the n+ℓ = 5 block opens at Z = 21 (Sc) and 3d
collapses at 21; the n+ℓ = 7 block opens at 57 (La) and 4f at 57.* **No member states its form.**

It did not have to be guessed. COORDINATES-2.13's computed column is generated by this equation, so
C can be **inverted out of it**, and it comes back exact:

| ℓ | C = 0.125 | 0.250 | 0.375 | **0.500** | 0.625 | 0.750 | 0.875 | 1.000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Z = 2 | 3 | 4 | **5** | 6 | 7 | 8 | 9 |
| 2 | Z = 18 | 19 | 20 | **21** | 22 | 23 | 24 | 25 |
| 3 | Z = 54 | 55 | 56 | **57** | 58 | 59 | 60 | 61 |

```
C(Z, ℓ) = clamp( 0.5 + (Z − Z₀(ℓ)) / 8 , 0 , 1 )        Z₀ = {1: 5, 2: 21, 3: 57}
```

A **linear ramp eight wide, reaching exactly 0.5 at the Janet boundary** and saturating four beyond
it — and zero above ℓ = 3, which the index agrees with: every ℓ ≥ 4 channel inverts to C = 0 exactly.

That is register 1189 in closed form. It says *"the collapse is a rapid transition, **not a step**"*
and gives Ca I nd = 0.908 at Z = 20 as the pre-collapse maximum of the compendium. An indicator
makes that zero; the ramp makes it C(20, 2) = 0.375, already a third of the way up. **The first
implementation here was an indicator, and the index rejected it** — K I's nd channel computes to
0.293 in the CSV and 0.000 under a step.

ℓ = 1's threshold at boron falls out of the same rule — Z₀ is the Janet block opening for that ℓ —
and is not stated anywhere.

## The equation, reproduced

With the recovered C in place, the two branches reproduce **98.45%** of COORDINATES-2.13's 102,553
computed rows to within 5 × 10⁻⁴, under the configuration table the index was built on. Nothing was
fitted to the column; the coefficients are register 1205's, digit for digit. That is the evidence
the recovery is right, and it is a self-test fixture.

Against the **measured** channels (`--equation`):

```
channels compared: 358        rms 0.1809   R2 0.9656   median |error| 0.0587
  l = 4   n = 36    rms 0.0139
```

Register 1205 records rms 0.1610, R² 0.9741 and ℓ ≥ 4 rms 0.0150 on **284** channels, Z = 2 to 90,
charge 1 to 10. COORDINATES-2.13 now holds 358 measured channels, so the samples are not the same
and the numbers are not expected to match exactly. The report says so rather than claiming the
recorded figures.

## Two findings in the spectra index, measured to the row

**1. The `B` column was built on a withdrawn configuration table.** `--check-B` computes the Pauli
bound `B = min(p, n₀ − ℓ − 1)` (register 1141) under both tables, over the rows whose core the
observed table holds:

```
  rows with an integer B and a core inside the table: 99687
  B from the OBSERVED configurations (register 1306):   98583  98.89%
  B from AUFBAU configurations:                         99687  100.00%

  every integer row with Z <= 118: 101303; aufbau reproduces 101303
```

Plain Madelung aufbau, with no exception patched and n₀ the first entirely unoccupied n, reproduces
**every** integer B the column holds. Every disagreement with the observed table lands where the two
tables part company — the cores of La (244 rows), **Pd** (144), Ce, Ac, Th, Gd, **Lr** (60), Pa, U,
Np, Cm. Pd and Lr are the two cases register 1306 names explicitly when it withdraws the aufbau table:

> Every previous version built configurations by aufbau and patched exceptions by hand; that table
> was wrong at Pd — aufbau plus my patch gave [Kr]4d⁹5s and the truth is [Kr]4d¹⁰ with no 5s — and
> at Lr, which is [Rn]5f¹⁴7s²7p.

Register 1306 corrected the configurations. **COORDINATES-2.13 was never rebuilt on them**, and
nothing in `DEFERRED.md` or `DOCKET.md` records that it is outstanding. `--config aufbau` reproduces
the index as it stands; `--config observed` (the default) computes what register 1306 implies, and
the site shows that B with the CSV's beside it, every disagreement (1,104 rows) marked.

**2. The `B` column is overloaded, three ways** (`csv_B_reading()`):

| reading | rows | what the value is | status |
| --- | ---: | --- | --- |
| `bound` | 101,303 | the Pauli bound on the aufbau table | `READ` |
| `range` | 25 | the **range** (max − min) of the series' quantum defects, whose median is the row's δ | `RECOVERED` |
| `zero` | 3,504 | 0 in every row of Z = 119 and 120: the bound on neither table | `READ` |

The 25 are the measured rows of the 2026-08-14 NIST fetch. Until 2026-10-17 they were described as
"a dispersion of the median defect", which was never measured. `tools/seriesdefect.py` measures it.
It takes each series' members from NIST's own levels (`tables/nist-levels/`, nine spectra), with the
printed limit in cm⁻¹ and the Rydberg reduced by the standard atomic weight, and reproduces the
printed member count, n range, δ as the median and B as the range in **25 of 25** rows, to the five
decimals printed. With R∞ no δ reproduces, and with ¹¹B's mass in place of boron's standard weight
the boron rows fail, so the source's conventions are fixed too. The 3,504 zeros were not noticed
before: `--check-B` once reported them as 1,308 rows "neither table reproduces". `csv_bound()` returns
`None` for both readings that are not bounds, so neither is ever compared with one.

## The equation's domain, per channel

"The equation is VALIDATED in the verified-plus-possible region and EXTRAPOLATED outside it"
(registers 1193–1194), and since 2026-10-17 every channel says which (`channel_domain()`, `DERIVED`).
The rule is register 1192's: a channel is outside where the element has no long-lived isotope
(Z > 103), the ion is above charge 10, the core is open-shell at 3, 16 or 119 parents, or the series
is unresolved above ng. The parent count is a property of the stage, read from the CSV's note on any
row of it (a measured row carries no note of its own). An unresolved series applies only where
nothing in the channel is measured.

`domain_census()` holds the reading against the registers' own figures:

| | measured here | the record |
| --- | ---: | ---: |
| unmeasured cells, Z > 103 | 24,312 | 24,312 (register 1192) |
| unmeasured cells, charge > 10 | 61,748 | 61,748 |
| unmeasured cells, series unresolved | 5,366 | 5,367 |
| unmeasured cells, open-shell core | 5,481 | 5,476 |
| measured rows outside: three-parent, sixteen-parent, charge > 10 | 24, 15, 12 | 24, 15, 12 (register 1193) |
| rms residual, measured rows inside (before the 2026-08-14 fetch) | 0.1475 over 282 | 0.147 (register 1205's re-test), over 277 |

The two largest exclusions and all 51 of register 1193's are exact. The last two cell counts differ
by 1 and 5, and the in-region set has five rows more than the record's 277. The CSV is a later state
than the survey, and the rows that moved are not identified. The 25 rows of the 2026-08-14 fetch fall
inside the domain, with an rms of 0.377.

## Λ₈, and how an element maps onto its cells

Chapter 7 makes a Λ₈ cell a **transition**: a source configuration, a target configuration and the
electron count moved between them. So an element is not a cell, and the book says which cells
stand for it. §12.11.1.6 (main L3318): *"Λ has no Z. Every constraint is internal to one atom … Building
cells (Z, n, ℓ, k, q, e, f, g) from real occupied subshells gives 4,325"* (register 628).

`element_cells(Z)` builds them by the record's own rule, the enumeration in `close_L118.py`'s `run()`
(the instrument behind register 529's 18,288 tests, in the restore point at
`extracted/archives/restore-point-2-13/`):

- the source is an occupied subshell (n, ℓ) with its real occupancy k;
- the target is another subshell (e, f) the same atom holds;
- q = 1 … k electrons are moved, and g = 1 … min(q, 4f + 2) placed.

The table is read from that file by path, after its md5 is checked; its tail runs the test pass and
exits, so only the table is executed. The cells are **`RECOVERED`**. `element_cells_census()`
reproduces every figure the record prints of them: 118 elements, 247 subshells, 18,288 tests, 4,325
cells, 982 composable within one element and 3,686 across the table, and register 629's
selection-rule splits. `--element-cells-E` re-measures E = 972,862 with Z and 28,503 without it, in
about three minutes.

Λ closes because it has no Z. For Z = 1 to 108 every subshell the record's table lists carries
`LW1-ground.py`'s occupancy. The selftest checks that, and that every cell satisfies the six
constraints decidable without 2S. Fifteen elements have one listed subshell and so no cell. See
`docs/CAVEATS.md`.

**The ionisation ladder** (`ionisation_cells`) is a different object, kept beside the cells as a
`RECONSTRUCTED` reading: the steps between an element's ions, read off the observed configurations.
At each step the electrons lost leave a source subshell, and the subshell that differs identifies the
target. It stood in the record's place until 2026-10-18; an earlier search had looked for a ruling only
in the governance files, and missed the book's own construction. 2S is left `None` where the ion's
term is not carried: the envelope 2S ≤ k admits values no k electrons can hold (§7.1), so it may not
be inferred. Measured: all **5,778** ladder steps of Z = 1 to 108 satisfy the six decidable
constraints, and **1,107** lie within §7.4's standing caps.

## `--selftest`

137 fixtures. The seated members as imported (108 elements, 108 of 108 electron counts, |Λ₈| = 976
and the whole tower 1,654 / 2,535 / 13,585 / 70,905 / 199,130); chapter 6's ninety main-table cells
and the twenty-eight set aside; **ℛ reproducing the thirty-six by identity**, not merely by count —
(p1,g2)…(p1,g17), (p2,g3)…(p2,g12), (p3,g3)…(p3,g12); the Janet blocks opening at Sc, La and Ac;
the recovered ramp at all three ℓ; the hydrogenic channel returning **exactly** zero at Nₑ = 1
(register 5193: the (Nₑ−1)/Nₑ factor vanishes identically, so no parameter can move it); the Pauli
bound at He I and Be I; §7.1's seven constraints firing and failing where they should; and the
equation reproducing the computed column under both configuration tables. Since 2026-10-17 also:
n₀'s reading reproducing all 101,303 integer B values on the aufbau table, with the other reading
held below 90 %; the B column's three readings counted (101,303 / 25 / 3,504); the nine neutral
limits held against the CSV's notes; the deficit refused at every stage that is not one-electron;
the ground basis of Lr to Hs; and the domain census against registers 1192 and 1193. Since
2026-10-18, the record's element cells against registers 529, 628 and 629.

Current state: `SELFTEST OK`.

## Known gaps

- **The tower above Λ₈ is not populated per element.** 2S′, v, 2J_c, 2K and 2J need the ion's term
  and coupling scheme; the ground *level* is carried in `LW1-ground.py` but parsing `4I*15/2` into a
  coupling assignment is a separate instrument.
- **Elements above Z = 108 are not populated.** `LW1-ground.py` stops at hassium because NIST's
  neutral ground levels do (its neutral rows end at Hs I; Mt and Ds appear only as ions), not because
  measurement does — measurement stops earlier. From Lr to Hs NIST holds the ground level of each
  neutral spectrum and no excited level, and the ionisation energy it prints is measured only for Lr:
  ab initio for Rf and Db, semi-empirical for Sg, Bh and Hs (`GROUND_ONLY`, read 2026-10-17). The
  record carries those six as `ground_basis`. COORDINATES-2.13 carries rows to Z = 120; those
  channels report no configuration, and their B column holds 0 throughout.

**Closed on 2026-10-17** (see `docs/CAVEATS.md`): n₀'s reading, once `RECONSTRUCTED` at 97.7 % against
87.0 % on the observed table, is `RECOVERED` at 101,303 of 101,303 on the column's own table; the
equation's domain, once "not re-stated per channel", is now stated on every channel.
- **The ionisation ladder is a reconstruction beside the record's cells.** See above.
