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
| 3 | **No input beyond the initial ignition** — **met on materials and on parts, conditional on Requirement 4 (the waste form returns chlorine)** | `materials.py --supply`, `--criterion3` |
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

**The design space has been searched, and it is narrow.** `tools/explore.py` varies every axis the
design has and finds that **one dominates and is closed by the safety decision** (multiplication k, at
10.48×), the next is an engineering choice (accelerator efficiency, 2.00×) and the third is an assumed
constant (driver power, 1.81×) — **and nothing else moves the answer by more than fifteen percent**.
Pairs are worse than the singles suggest: **three pairs take the plant to no closure at all**, so the
design point is near several cliffs and not one. **The dominant axis sits on the sharpest**: the plant
closes only above **k = 0.777** against a design point of 0.900, at an elasticity of **−16.7**.

**So the plant is not short of redesigns; it is short of measurements, and those are two different
shortages.** Redesigning everything that is open to redesign is worth **1.45×**. Being wrong about the
constants nobody has measured is worth **19.2×** in the other direction, and with the accelerator
efficiency at the low end of its own sourced band as well the plant does not close at all. **No
optimum is reported**, because an optimum over a space whose largest free swing is an unmeasured
constant is a statement about the constant. **The order to work in is measurement first**, and the
three are named: the driver standby's scaling law; the wall-plug-to-beam efficiency at this power; and
the transport calculation on the fissile fraction, which is what actually places k. Only after those
three is a redesign a design decision rather than a guess about a measurement.

**And the constants have been censused, because the mathematics does not contain them.**
`tools/provenance.py` reads every module-level constant in the twelve design instruments — **408** of
them — and classifies each by what its own file says it rests on. The finding is not the count but the
**join with the search**: three of the axes that move this plant rest on a constant carrying **no
provenance at all**, among them the driver standby, through which the largest interaction in the whole
design runs at 19.25×. They were invisible to an inventory of stated assumptions *because nobody wrote
ASSUMED beside them*. Nothing was repaired — writing a status beside a constant would be choosing one,
which is the flattening this file forbids.

**Precision in the mathematics is worth 1.45×. Provenance in the constants is worth the plant.** They
are not the same quantity, and no amount of the first supplies the second.

**The first of the three measurements has been made, and it worked exactly as the ordering predicted.**
The driver standby is published in the *cryogenics* literature — SNS and ESS both state a cryoplant
capacity beside a beam power — and it gives **1.86 to 2.98 MW per machine**, against the design's
assumed 1.0 MW. It refutes one candidate scaling law outright (ESS's beam is 3.57× SNS's and its
cryoplant 1.20×, so the load does not track beam power) and leaves the other bounded rather than
unbounded. **`explore.py`'s exposure fell from 19.2× to 1.81×.**

**And it did not merely shrink the uncertainty — it converted it into a requirement.** At the measured
standby, **a station built out of drivers of the largest class ever operated does not close at all**.
The 20 MW driver is not a convenience to apologise for; it is a requirement, and the plant cannot be
built from machines that exist. That is a harder statement than the design was making, and it is
measured rather than assumed.

**A decision is owed here and is the author's.** `REF_STANDBY_KW` still carries 1.0 MW, which the
measurement puts below both real machines. Raising it is a *design change* and the instruments will
not make one: the measurement sits beside the constant, and whether the design adopts it, and at which
end of the band, is recorded here when it is taken.

**And the reading that "measurement comes first" is now half an answer, corrected by the author.** For
a term that *can* be measured first, it is right — the driver standby was, and it took a morning. But
a first-of-a-kind has terms that cannot be: nobody has run a 20 MW proton linac, so nobody has
published what one's fixed load does, and waiting for that measurement is waiting for the machine the
measurement is for. **That is circular, and treating every unmeasured constant as a blocker would stop
every first article ever built.** The engineering answer is to bound the term and design through it,
which is what `explore.py --basis` now does.

**The basis is one inequality and it is per unit of beam** — `G(k)·η_th·(1−dry) > 1/η_acc`. Positive
and the plant delivers net electricity; zero or below and no station of any size does. **Standby,
driver size and module size do not appear in it**: they set how much beam a station needs and cannot
set whether beam helps. So **of the terms nobody has measured, only two can decide whether the plant
exists** — k and the accelerator efficiency — and the rest decide only its size.

**The design's margin against non-existence is 0.1330 in k, and the one-group model's own uncertainty
on an absolute k is 0.1350. They are the same number.** That is not a reason to stop; it is the
specification the transport calculation must meet, and it makes the design basis three requirements
rather than three measurements:

1. **k_eff ≥ 0.767** at η_acc = 0.30, transport-grade — and ≥ 0.838 if the accelerator comes in at the
   bottom of its band.
2. **η_acc ≥ 0.516** buys twice the model's uncertainty in margin. **Not knowing k precisely is
   answered by specifying a better accelerator** — a purchase rather than a discovery.
3. **The driver shall be 20 MW at 8 GeV.** A requirement, not a preference: at the measured standby a
   station of drivers of the largest class ever operated does not close. **No machine of this class
   exists.**

**And the price is stated rather than hidden: a design basis is not a witness.** It says the
mathematics closes across the range the constants could take and that these requirements are what make
it close. It does not say the machine has been seen to. **Every first article is built on exactly
this, and the honest ones say so** — which is the standing under which the power-source paper is
written, and the reason the mathematics is held to the standard it is.

**Criterion 3 is closed on materials, and it was closed by changing the plant.**
Two streams arrived at the gate for ever, and both were design choices rather
than laws:

- **Liquid nitrogen**, 200 t/yr, which the file itself called *"the one utility
  feed"*. First closed by liquefying it on site — nitrogen is 78 % of the air
  here — at **8.1 kW**, 0.00071 % of net. **Then deleted outright**: the shields
  run on the **helium cryoplant at 45 K**, as the reference machine's do, which
  removes a fluid, a plant and an inventory rather than adding one to feed a
  line. **A supply line is better removed than fed.** Two things were computed
  first. The row was **never a cooling duty** — 200 t/yr through nitrogen's
  latent heat is **1,261 W** against a reference machine's **10.8 kW** shield
  load, so it was makeup on a loop already closed and **the shield heat had
  never been in the inventory at all**. And **77 K loses to 45 K**: nitrogen is
  the cheaper refrigerant per watt, but a hotter shield radiates at the cold
  mass, radiation goes as T⁴, and a watt at 2 K costs fifty times a watt at
  45 K — they trade exactly at **0.88 %** of the 2 K load being shield
  radiation, and a real cryomodule is above that. **A break-even, not a
  preference.**
- **Salt-processing reagents**, which had been named but never specified and so
  never priced. The fission-product removal is now specified **electrical** —
  helium sparge on the recirculating inventory, noble metals plated out, vacuum
  distillation for the alkali and alkaline-earth chlorides, electrowinning for
  the lanthanides, any chemical reductant regenerated electrolytically on site.
  The cost is **bounded rather than designed**: distilling the *whole* 505 t
  inventory three times a year — far more than a slipstream cleanup needs —
  comes to **0.15 MW**, or **0.013 %** of net. A bound is computed because the
  process is not the instrument's to choose, and a negligible bound means the
  choice need not be made to proceed.

**One line was deleted and the other became electricity, which the plant makes.**
What is left is **0.15 MW against 1,141 MW net — 0.013 %** — so nothing else in
the design moves. And the deletion had a second consequence: the shield heat it
was carrying is inside the cryoplant, which sent `powersource --standby` back to
count a circuit it had missed.

**What remains is two rows and both are parts**: the fission-product removal
system (still the single most demanding unbuilt item here) and the krypton-85
capture bed. **No material stream arrives at the gate any more** — not fuel, not
fertile, not tritium, not lithium, not coolant, not reagent, not cryogen.

**And then "fails on parts" was itself corrected, by the author, and the
correction is right.** A part is **designed to spec and built to meet the
mathematics** — it is the *output* of the engineering-materials phase, not an
input the plant needs. The criterion asks whether the thing needs **feeding**,
and a specification is not a feed. Calling it a failure treated the next phase's
deliverable as this phase's shortfall.

**What the question survives as is sharper and answerable: a part is made of
something.** So the test is what the parts stream *consumes*. Nickel alloy,
graphite, refractory electrodes, vacuum plant, steel cylinders — **ordinary**,
and no criterion about self-sufficiency was written to exclude the existence of
industry; the krypton charcoal is regenerated by warming rather than consumed.

**One material is not ordinary, and it hides in the process rather than the
part.** Fission products live in the salt as chlorides and leave as chlorides,
and every atom of that chlorine is **Cl-37 enriched**. Bounded by charge
conservation at **592 kg/yr** — 0.32 % of the inventory a year, **12.9 % over the
life** — and stated as a *bound*, not a process figure, because the real number
needs a valence distribution and a process holdup this work does not compute.
(The inventory it divides by is the row `fuelchoice.py` found understates, so the
share errs high, which is the direction a bound should err in.)

**And the electrical cleanup already returns it**, which is the second reason to
have specified it: electrowinning deposits the lanthanide as metal and evolves
chlorine back into the salt. A **chloride** waste form carries it out of the
building; an **oxide** or metal form leaves it behind.

> **Requirement 4** — the waste form shall return chlorine to the salt. Unmet, it
> is a 592 kg/yr Cl-37 line and 13 % of the inventory over the life. Met,
> criterion 3 closes on materials with nothing left over.

**So criterion 3 is met, conditional on one requirement handed forward.** Read
literally — no input of *anything* — it still cannot be met by any physical
object, because a machine that never needs a spare part is not a machine. Read as
it was plainly meant, it is met. **The criterion was never reworded**: the design
was changed, and then the residue was computed instead of shrugged at.

**A numbering error was corrected in the same pass.** `materials.py` adjudicated
"criterion 4" throughout, which is the number it had before 'cold' was dropped
and everything below it moved up. The table above is authoritative and the file
now agrees with it. **The verdict never changed — only the label on it** — and
this is exactly the failure `OBJECTIVE.md` was written to stop.

## The phases

1. Define the math in full and prove it.
2. Design concepts, material identification, storage requirements.
3. Facility build package.
4. Draft the proposal/paper.
5. Adversarial audits.

## Two rules this file inherits, and they govern everything above

**A status is never flattened.** Where a criterion is met on one term and failed
on another, both are stated. `materials.py` said of criterion 3 that it "holds
ON FUEL and fails ON CONSUMABLES AND PARTS … and it is not what was asked for".
**The consumables half has since been closed by changing the design rather than
the sentence** (below); what stands now is "holds on every material stream, fails
on parts alone", and no paper may quote the first half of *that* alone either.

**A finding is recorded, never repaired.** A criterion that is not met is written
down as not met. It is the author's decision whether to relax the criterion,
change the design, or publish the shortfall; it is never the writer's to make by
choosing a kinder word.
