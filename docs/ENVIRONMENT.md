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

## Two grades per row, and the second is the one that matters

`before` is the impact with nothing done about it; `after` is what is left once the named mitigation
is **built**. **A mitigation that does not move the grade is not a mitigation**, and printing both is
what stops one from being claimed. Grades are `BENEFIT`, `NEGLIGIBLE`, `MINOR`, `MODERATE`, `MAJOR`,
`DOMINANT`, and they carry a **sign** — four rows run the other way.

Each row also names a **carrier**: the item in `buildpackage.py` that takes the mitigation into the
build. The selftest fails a carrier that exists in one file and not the other, in both directions —
**a mitigation that lives only in the register is prose, and prose does not get built.**

## What the mitigation pass moved

```
BEFORE   BENEFIT 4   NEGLIGIBLE 1   MINOR 4   MODERATE 9   MAJOR 4   DOMINANT 1
AFTER    BENEFIT 4   NEGLIGIBLE 9   MINOR 8   MODERATE 1   MAJOR 1   DOMINANT 0
```

It moved by **changing the plant, not the prose**. Five design changes did it:

- **The target became molten lead.** Mercury's vapour pressure at its operating temperature is about
  eight orders of magnitude above lead's, so a mercury breach is a *release* and a lead breach is a
  *puddle*. HARP's pion production data — which this design actually integrates — was measured on
  **lead**, so the substitution also makes the machine and its own source data the same material.
  Pure lead, not lead-bismuth, because LBE breeds Po-210 from Bi-209. **It deletes the beryllium
  window with it**, since that window exists only to stop mercury vapour. Cost: 1.271× target length,
  and trace heating that becomes a safety system because lead freezes at 327 °C.
- **Dry cooling, adopted rather than offered.** Zero water at 5 % of gross output; the module count
  was raised to absorb it.
- **A 2,691 t nitrate-salt thermal buffer** on the secondary, which closes the beam-trip thermal item
  the build package had carried open. CSP plants build stores at this tonnage routinely.
- **The biological shield is sized** — as an *attenuation factor*, which is computable without a
  site, where a dose is not.
- **Reduced-activation steel** inside the shield, which sets the decommissioning waste class a
  century later and cannot be chosen afterwards.

## The two rows that do not clear

**Tritium inventory stays `MAJOR`.** It is the fusion channel's fuel. The design attacks it from
every side that exists — smallest cell the physics allows, the narrow window the scale-up forced, N
separate cells rather than one — and one further lever (25 T recompression) is named and left as a
requirement. `--tradeoff` prices the only thing that would clear it: **deleting the muon channel
costs 8 % more beam and 1,540 pcm of subcritical margin**, and takes the tritium, the ⁶Li, the cells
and the capture solenoids with it. **That file does not decide it** — the fusion is the project's
subject and the arithmetic is put where whoever decides can see it.

**Proliferation stays `MODERATE`.** Four things answer it and none is reassurance: no
separated-plutonium stream anywhere in the flowsheet by architecture; a salt too radioactive to
handle outside a hot cell; continuous accountancy because the fuel is a fluid; and the station is a
net *destroyer* of separated plutonium. What keeps it at `MODERATE` is that the equilibrium isotopic
vector is a depletion result this work does not compute, so the denaturing argument is a requirement
and not a fact.

The selftest refuses a self-congratulatory register: more adverse rows than beneficial ones; the
worst row before *and* after mitigation is the design's own doing; no residual may be worse than the
grade it mitigates; the rows that did not move must be ones that could not; nothing may be left at
`DOMINANT`; and proliferation may not be claimed below `MODERATE`.

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
