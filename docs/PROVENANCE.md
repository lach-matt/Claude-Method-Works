# PROVENANCE.md — what every number in the design rests on

`python3 tools/provenance.py` · `--assumed` · `--selftest` · stdlib only

## Why it exists

The design's mathematics is exact. Every relation in this work is a theorem or arithmetic —
`P = I·E`, `F = k/(ν(1−k))`, `G = N·V·η/E_π`, `k_eff = k_inf/(1+M²B²)` — and worked to any precision
they stay exact.

**What is not exact, and what the mathematics does not contain, is its own constants.** ν = 2.9 is a
measurement. The 25–30 neutrons per GeV deposited is a measurement. η_acc is a band across real
machines. The driver's standby load is not a measurement at all — and `explore.py` showed that one
unmeasured constant carries more consequence than every free design choice put together.

So this censuses them: every module-level constant in the twelve design instruments, classified by
what its own file says it rests on.

| class | meaning |
|---|---|
| `SOURCED` | a published measurement |
| `DERIVED` | computed from others rather than stated |
| `ASSUMED` | a value chosen because one was needed |
| `RECONSTRUCTED` | measured out of the corpus rather than out of the world |
| `DESIGN` | a decision, with its reason recorded elsewhere |
| `UNANNOTATED` | **this census cannot tell** |

**`UNANNOTATED` is not a finding of absence** and may not be read as one. Many are conversions and
exact definitions — seconds in a year, atoms in a kilogram, atomic masses — which have no provenance
to state because they are not measurements. The census says only that it cannot classify them.

## The census

**408 module-level constants across 12 design instruments.**

| status | count | share |
|---|---:|---:|
| SOURCED | 82 | 20.1 % |
| DERIVED | 1 | 0.2 % |
| RECONSTRUCTED | 1 | 0.2 % |
| ASSUMED | 18 | 4.4 % |
| UNANNOTATED | 306 | 75.0 % |

## The join with `explore.py`, which is the point of the file

`explore.py` ranks the axes by how much they move the answer and says nothing about what they rest on.
This census says what they rest on and nothing about which matter. **Neither is the finding. The join
is:**

| axis | swing | constant | provenance |
|---|---:|---|---|
| multiplication k | 10.48× | `K_DESIGN` | DERIVED |
| accelerator efficiency | 2.00× | `ETA_ACC_HI` | **UNANNOTATED** |
| driver power | 1.81× | `LINAC_BEAM_MW` | ASSUMED |
| muon channel | 1.15× | — | n/a |
| stopping window | 1.14× | `STATION_WINDOW_MEV` | **UNANNOTATED** |
| driver standby | 1.07× | `REF_STANDBY_KW` | **UNANNOTATED** |
| module power | 1.02× | `MODULE_BEAM_MW` | SOURCED |

**Three of the axes that move this plant rest on a constant carrying no provenance at all** — not
SOURCED, not ASSUMED, nothing. They were invisible to the ASSUMED inventory *precisely because nobody
wrote ASSUMED beside them*, which is the failure mode an inventory of stated assumptions has and
cannot fix from the inside.

**The sharpest was the driver standby — and it has since been measured** (`powersource --standby`),
which is what a census is for. The constant itself is unchanged and still unannotated; what changed is
that there are now two published machines beside it. Replacing the value is a design change and
belongs to the author, not to the census.

**The sharpest is the driver standby.** `explore.py`'s largest interaction runs through it — 19.25×
against a product of 1.93 — its band's low end says `SOURCED band`, and the value the whole design
actually uses says only *"mid-band driver fixed load"*. **A mid-point of a sourced band is not itself
sourced**, and the file had not said which it was.

Nothing is repaired. Writing `ASSUMED` beside `ETA_ACC_HI` would be *choosing* a status, which is the
flattening this project forbids; the census names them and the author decides what each actually is.

## The ASSUMED inventory

18 constants, of which `explore.py` has an axis on 1 — **a residue of 17**. That is the question
`explore.py` could not ask of itself: it measured the exposure of the axes it was given, and there are
more.

`SAFETY_FACTOR` · `COOLING_RISE_K` · `BREEDER_THICK_M` · `BUFFER_DT_K` · `BUFFER_TRIP_S` ·
`LI6_ENRICH` · `PB_OPERATING_C` · `SALT_DT_K` · `SALT_RESIDENCE_S` · `TARGET_RESIDENCE_S` ·
`FISSILE_FRACTION` · `F_LI_DESIGN` · `HOUSEHOLD_KW` · `LEAK_PARASITIC_LO` · **`LINAC_BEAM_MW`** ·
`BOIL_MARGIN_C` · `TRACE_HEAT_MW` · `CAPACITY_FACTOR`

Two of them are already known to matter and are corroborated from elsewhere: `FISSILE_FRACTION` is the
band `fuelchoice.py` found *was never derived and does not pass*, and `LEAK_PARASITIC_LO` is the
leakage that `materials.py --fertile` found decides whether thorium works at all.

**The residue is not priced here.** Most of these do not reach the beam — they set an inventory, a
schedule or a margin rather than the balance. What it makes them is *candidates*, and each has to be
put on an axis to be priced. **Guessing which matter is the error this whole census exists to stop.**

## Two things the classifier had to learn, and both are pinned

**A constant's own words beat a paragraph above it.** Reading the trailing comment and the block above
as one text let a paragraph that merely *discussed* the design overrule a value's stated source —
`SPALL_TARGET_MW`, every row of it marked `SOURCED`, came back graded `DESIGN`. The two are returned
apart and the constant's own words decide.

**The block above is capped at four lines.** An unbounded walk upwards swallows whole explanatory
paragraphs, and a paragraph that discusses an assumption then grades the *next* constant as one:
`LINAC_CLASS`, a table every row of which is sourced, came back `ASSUMED` because the paragraph
introducing `LINAC_BEAM_MW` sits above it. A dedicated note is short; an essay is context for a
section, not an annotation of one value.

## The reading that matters for the project

**Precision in the mathematics is worth 1.45×** — `explore.py`'s redesign ceiling. **Provenance in the
constants is worth the plant.** They are not the same quantity, and no amount of the first supplies
the second: absolute precision applied to a number nobody measured returns a precisely wrong answer,
with more confidence attached to it than it had before.
