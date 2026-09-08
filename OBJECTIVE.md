# The objective, and the criteria it sets

**This file is the authoritative statement of what the project is for.** It was
stated by the author and is recorded here verbatim. Before it existed, four
criteria were referenced *by number* in three instruments — `materials.py`
adjudicates "criterion 4", `powersource.py` calls stability "the project's third
criterion", `buildpackage.py` quotes the fourth as speaking of "an initial
ignition" — and **no file stated them.** That is how a paper comes to be graded
against criteria nobody can read. Nothing here is inferred; where the work does
not meet a criterion, that is recorded below rather than softened.

## The objective, verbatim

> Identify a 'cold' self sustaining power source that requires no input of
> anything beyond the initial ignition. Must be scaled for civilization,
> baseline 1 million households. Should also supply the power to ignite further
> stations. Be entirely environmentally friendly — mitigations to environmental
> problems are addressed upfront before design. Contain built in fail-safes and
> have the ability to be restarted quickly after a shutdown. Must be cheap to
> start but put out a tremendous amount of energy, which will make this a long
> term sustainable power source.

## The criteria, as that objective sets them

| # | criterion | where it is adjudicated |
|---|---|---|
| ~~1~~ | ~~**'Cold'**~~ — **DROPPED by the author, and the reason is recorded rather than the word quietly removed.** 'Cold' is *proved* in `Cold_Fusion_Proof_v1.0` for muon-catalysed fusion, where the approach to nuclear separation is supplied by molecular binding geometry rather than by kinetic energy. The plant this project now builds carries **no fusion channel**, so the word had nothing left to attach to, and redefining it at plant level would have been a second and different definition wearing the first one's name. The word retires to the proof paper where it is earned. **The criterion is now: clean, efficient, self-sustaining.** | *retired — see the proof paper* |
| 2 | **Self-sustaining** — runs its own drive from its own output | `powersource.py --plant` |
| 3 | **No input beyond the initial ignition** | `materials.py --supply` |
| 4 | **Scaled for civilization**, baseline 1,000,000 households | `powersource.py --station` |
| 5 | **Ignites further stations** from its own output | `powersource.py --ignition` |
| 6 | **Entirely environmentally friendly**, mitigated before design | `environment.py` |
| 7 | **Built-in fail-safes** | `powersource.py --stability` |
| 8 | **Restartable quickly after shutdown** | `restart.py` — **minutes held molten, 6 h drained**; the clock is thermal, not neutronic |
| 9 | **Cheap to start**, and a tremendous output making it long-term sustainable | `startcost.py` — **32-day energy payback, EROI 460:1**; measured in energy, not money |

**Two decisions taken by the author, recorded here so that neither is re-argued and neither is
forgotten:** 'cold' is dropped from the objective (above), and **criteria 8 and 9 are adjudicated by
new instruments before phase 4 is drafted** rather than carried into the paper as open items. A paper
that states a criterion it cannot support is the failure mode this whole harness exists to prevent.

## Decisions taken, with their reasons

A refused or adopted option with its reason is a decision; one without is a gap.

**The operating point is k = 0.900, not the field's 0.95, and it is adopted for
intrinsic criticality safety.** Below **7.93 %** fissile the fuel salt's `k_inf`
falls under one, and an assembly whose `k_inf` is under one cannot be made
critical by any amount in any shape. Holding the design there means **no
accumulation of fuel salt anywhere on site can ever be critical when dry** — the
hazard class stops existing rather than being managed by procedure, and the
property is a fact about the material rather than about the operator. The
subcritical margin doubles to 10,000 pcm. There is no intermediate: `k_eff` is
capped at 0.900 by the property itself.

**The price is 2.86× the driver** — 84 MW to 240 MW for the same million
households — because at lower multiplication more of the plant's own electricity
recirculates into its accelerators. It was quoted at 2.05× when the decision was
put, **corrected to 2.76× before implementation**, and re-confirmed at the true
figure; it is 2.86× once the sizing charges the drivers the station actually
builds — see the driver decision below. The reason given for paying it: *"it's what sells a new plant to a
community, in an age when plants and data centers are being rejected."*

**Re-scaling the station does not recover that cost, and the re-scale was
undertaken to test whether it could.** The module size was set by a *pion*
production target, which route C does not have; of the four constraints that
fixed it at 4 MW, three vanish with the muon channel and only the **spallation
target's power** survives. Re-scaling to an ESS-class 5 MW target takes the
module count from 59 to 48, and to 24 at a 10 MW target — but **the beam is
240 MW at every row**, because it is set by the multiplication and the module
size only decides how it is divided. Re-scaling buys buildability, not energy.

**The station is now sized by closing the loop on its own drivers, and the
open-loop sizing is kept as a function rather than as a paragraph.** The beam
must be solved for before the number of drivers is known, so the sizing charged
**one** driver's standby where the re-scaled station builds **twelve**. Eleven
unbilled standbys are 36.7 MW electric — more than the whole-module round-up
returns — so **every re-scaled station landed below the million households it
was sized for**, 975,546 at the ESS row. At the ADS convention the same sizing
was right, which is why the fault went unseen until the beam was 2.86× larger.
`station()` now walks up from the open-loop figure, which is a floor and never
an over-estimate, and returns the base station unchanged.

**What closes the shortfall was already bought.** Drivers come in whole 20 MW
machines and the beam did not fill them, so 10 MW of installed driver capacity
stood idle. At the ESS row **the station that meets the baseline and the station
that strands no capacity are the same station** — 48 modules, 240 MW, twelve
drivers, 1,019,486 households — and no target row needs a new driver. The
stranded beam is the cheapest in the plant (**5.009** net MW per beam MW against
**4.343** for the module that buys a driver), because the standby is already
paid. It is also the **only lever in this work that buys output and spends no
safety**: k is composition, so more source neutrons leave the 10,000 pcm margin
and the always-subcritical property untouched. And it is **bounded** — worth
exactly the 10 MW that was stranded and not one MW more.

**The route C driver is SNS and MYRRHA class on energy and on nothing else,
and the sentence that said otherwise is corrected.** `P[MW] = I[mA]·E[GeV]`
exactly, so at fixed beam power the current is inversely proportional to the
energy. A 20 MW driver at 8 GeV is **2.50 mA** — 1.05× the highest average
proton current ever operated, at the record rather than past it. The same
machine at route C's ~1 GeV is **20 mA**: **8.4×** that record and **5.0×** the
highest ever designed. The 1 W/m beam-loss budget runs the same way, the
allowance going with length and the length with energy, so the 8 GeV machine is
the forgiving one — 1.8× tighter than SNS against 14.3× at 1 GeV. **What route C
buys is length**, 4.2 km of linac against 28.8 km, a factor of 6.9; what it
costs is a machine nobody has built at a current nobody has designed for, and
the two do not cancel because they are not the same kind of quantity. Held to a
current that has been designed for, route A's driver count barely moves (12 → 8)
and route C's multiplies (14 → 69). **The standby cost of that is not priced**:
`REF_STANDBY_KW` is a band for a driver of unstated size and nothing here scales
it with machine size — owed before any route is priced on its accelerator count.
The route decision is **not** reopened on this; what is removed is the sentence
that made route C's driver sound like an ordinary order.

**The ceiling on adding beam is owed, not computed, and that is recorded rather
than filled.** Net is *exactly* linear in beam at a fixed driver count, so the
model will return more output for more beam without limit; that is a property of
the model and not of the plant. The blanket is not split, so beam is power
density in **one** blanket, and the baseline-meeting station runs at **1.39×**
the thermal power at which every downstream inventory is computed — `materials.py`
derives the salt flow, the salt and heavy-metal inventories and the drain tank
from `station()`'s thermal figure, and `restart.py` takes the decay heat from the
same one, so all of them are understated by that factor. **The reading that the
1.39 was a factor on the power density is withdrawn**: the salt inventory is flow
times loop transit and the flow is set by the heat, so a bigger station holds
proportionally more salt and the density does not move. `--blanket` carries the
correction and the bound; the residue is named there.

## The phases

1. Define the math in full and prove it.
2. Design concepts, material identification, storage requirements.
3. Facility build package.
4. Draft the proposal/paper.
5. Adversarial audits.

## Two rules this file inherits, and they govern everything above

**A status is never flattened.** Where a criterion is met on one term and failed
on another, both are stated. `materials.py` already says of criterion 3 that it
"holds ON FUEL and fails ON CONSUMABLES AND PARTS … and it is not what was asked
for" — that sentence stands, and no paper may quote the first half alone.

**A finding is recorded, never repaired.** A criterion that is not met is written
down as not met. It is the author's decision whether to relax the criterion,
change the design, or publish the shortfall; it is never the writer's to make by
choosing a kinder word.
