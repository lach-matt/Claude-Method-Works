# `tools/environment.py` — impacts, assessed and mitigated

Every impact the station has that a reader would want assessed: what it is, how big, who receives
it, how long it lasts, and what is done about it. Nothing is asserted as safe.

## The refusal that shapes the whole file

**It computes no dose.** A dose needs site meteorology, a stack height, a population distribution
and a pathway model, and a station with no site has none of those. Every radiological row is
therefore a **source term** and a **requirement on release** — which is what a licence actually
tests — never a reassurance about a consequence. The selftest enforces this against the *rendered
output*, not the source: no dose unit may ever be printed, checked on word boundaries so the check
does not trip over its own text.

## Two graded columns

Each row carries a **grade** — `BENEFIT`, `NEGLIGIBLE`, `MINOR`, `MODERATE`, `MAJOR`, `DOMINANT` —
and each mitigation carries a status: `PRACTICE` (routine in an existing industry at this scale),
`DESIGNED` (in this design, buildable from what exists), `REQUIREMENT` (a target whose means are
not demonstrated here). The grade carries a **sign**, because three rows run the other way.

The selftest refuses a self-congratulatory register: it asserts there are more adverse rows than
beneficial ones, that the `DOMINANT` row is the design's own doing, that proliferation is graded
`MAJOR` and its mitigation is *not* called `DESIGNED`, and that every mitigation is a sentence
rather than a word.

## The shape of the result

**One `DOMINANT` row, and it is tritium inventory** — set by the muon range and not by the power, so
it is the price of the fusion channel and of nothing else. The design attacks the inventory rather
than the release: the cell is the smallest the physics allows, and the station holds it as N
separate cells rather than one.

**One `NEGLIGIBLE` row that is worth more than the rest.** There is no criticality accident to
mitigate. The blanket is subcritical by a whole fast core's control worth, so cutting the beam stops
it, and the freeze-plug drain says the same thing again without power or a signal. This is the one
place where the design is *categorically* safer than a reactor rather than incrementally.

**Three `BENEFIT` rows, two from one fact.** The fuel is enrichment tails: already mined, already
stored as a liability. No ore is moved, no mill tailings are made, no enrichment is run — and most of
nuclear power's material footprint is in a front end this station does not have.

**The actinides are the waste result.** A solid-fuel reactor buries its unburnt heavy metal and its
minor actinides, and those set a repository's design life. Online processing returns them to the
salt and burns them, so what leaves is fission products — three hundred years rather than three
hundred thousand. That follows from the chemistry the *neutron budget* already forced.

**Proliferation is stated plainly and graded `MAJOR`.** A fast blanket breeding Pu-239 in a liquid
fuel with an online chemical plant is, on its face, the worst proliferation geometry in civil power.
Three things answer it — no separated-plutonium stream anywhere in the flowsheet, a salt too
radioactive to handle outside a hot cell, and continuous accountancy because the fuel is a fluid —
and its status stays `REQUIREMENT`, because a flowsheet described is not a flowsheet built.

## One number to read carefully

Construction CO₂ comes out **305× below the sourced PWR figure**. That is not a finding about the
design; it is a measure of how little of a life-cycle assessment is structural steel. The figure
counts the solenoids, cryomodule structure and coil shielding from `materials.py`'s bill and nothing
else. It is a **floor**, and the report says so at the point of printing it.

## Four decisions a builder cannot revisit

Low-cobalt, low-niobium steel inside the shield (Co-60 and Nb-94 decide the decommissioning waste
class forty years later). A salt flowsheet that separates nothing. Modularity as a *safety case* —
the bounding tritium release is one cell because the station is N cells. And the cooling route,
which is a site decision that constrains the site.

## Running it

```
python3 tools/environment.py                the impact register
python3 tools/environment.py --radiological the source terms
python3 tools/environment.py --waste        what leaves, and for how long
python3 tools/environment.py --conventional chemical, thermal, water, land
python3 tools/environment.py --benefit      the rows that run the other way
python3 tools/environment.py --proliferation
python3 tools/environment.py --mitigation   the plan, consolidated
python3 tools/environment.py --selftest
```
