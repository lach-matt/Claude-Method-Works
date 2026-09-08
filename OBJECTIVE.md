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
2. **η_acc ≥ 0.516** buys twice the model's uncertainty in margin — **and the measurement has since
   arrived, and it is not a purchase.** The best grid-to-beam any machine has ever returned is
   **20.0 %** (ESS, pulsed SRF) and **18.3 %** (PSI, CW normal-conducting); 0.516 is **2.58×** that,
   above even a component model's projection for a CW superconducting machine nobody has built. **At
   the measured 20 % the margin at k = 0.900 is 0.0615 — less than half the model's own 0.135.** The
   design's assumed 0.30 is above everything measured. **Requirement 2 is a projection, not a
   purchase.**
3. **The driver shall be 20 MW at 8 GeV.** A requirement, not a preference: at the measured standby a
   station of drivers of the largest class ever operated does not close. **No machine of this class
   exists.**

**All three measurements `explore.py` ordered have been attempted, and the third was made on the
wrong material and withdrawn.** The first (driver standby) turned a soft unknown into a hard
requirement. The second (wall-plug-to-beam) came back at the *bottom* of its band and closed the escape
route the basis leaned on. The third was the gate.

**The attempt and the withdrawal.** The one-group model's *"not reliable to better than roughly fifteen
percent"* was an assertion, and the design's whole margin against non-existence equalled it. The one
published benchmark of a fast molten salt with a k from two independent Monte Carlo codes is the
SAMOFAR/EVOL MSFR — LiF–ThF₄–UF₄, k_eff = 1.04364 (OpenMC) and 1.04338 (Serpent 2) — and run on it the
model bounds its own error between **+1.22 %** and **−6.88 %**. That result was used for one pass to
replace the fifteen with a seven, and the design basis was restated on it. **That was wrong, on a rule
the author stated plainly: do not test on a material you do not intend to use.** The benchmark is a
*fluoride* salt on a *thorium* cycle with *U-233* fissile; this design is a *chloride* salt on a
*uranium* cycle with *Pu-239* fissile, sharing neither halide, nor fertile, nor fissile nuclide. A
model can agree on one material and disagree on another for reasons that have nothing to do with its
method. **The seven percent is withdrawn; the fifteen stands, asserted, where it was.**

**What replaces it is not another check but the state of knowledge on the actual material, and it is
worse.** There is **no critical benchmark for a fast chloride salt** — the Molten Chloride Reactor
Experiment, the first critical fast-spectrum chloride-salt reactor, is being built to make one and has
not run. Its nuclear-data-induced uncertainty in k_eff is **2,161 pcm (0.0216 in k)**, falling to
886 pcm after the proposed experiments. **And the data are known to be wrong rather than merely
uncertain**: recent measurements of the ³⁵Cl(n,p) cross section disagree with the evaluations *outside
the bounds of their own covariance matrices*, and Los Alamos has been charged with re-measuring it.

**One thing runs the design's way and it was chosen for another reason entirely.** The discrepant
nuclide is **Cl-35**, and this salt is **Cl-37 enriched** — specified to stop parasitic absorption,
long before anyone here knew Cl-35 carried the material's largest nuclear-data uncertainty. **A
mitigation this work got for free and takes no credit for.**

**The design basis, restored and on the right material:**

| η_acc | margin at 0.900 | vs the asserted method error (0.1350) | vs nuclear data (0.0216) |
|---:|---:|---:|---:|
| 0.20 — every machine measured | 0.0615 | 0.46× | 2.85× |
| 0.30 — the design's assumption | 0.1330 | **0.99×** | 6.15× |
| 0.40 — a better machine | 0.1992 | 1.48× | 9.22× |

**The nuclear data are not the problem** — the margin covers them 6.2× at the design's own
accelerator. **The method is, and it is still asserted.**

**So the project has exactly one uncertainty left and it is precisely named: the one-group method
error on this composition.** What closes it is a **transport calculation on this salt** — a
*computation*, not an experiment. `tools/deck.py` writes the OpenMC and Serpent decks for it, from the
design's own numbers, with **the prediction registered in each deck's header before the run**.

**Writing that deck found a fault, and then a flag.**

**The fault.** `criticality.py` publishes the always-subcritical threshold at **7.93 %**, computed at
the **eutectic** (34 mol % UCl₃). The design's salt is **18.9 mol %**. The threshold on the material
the design actually holds is **8.35 %**. **The safety property was published for a material the design
does not use** — the same error the fluoride benchmark was withdrawn for, one level down. It runs the
safe way (the band is wider, not narrower), and `k = 0.900` survives untouched because it is
`k_inf = 1` through the leakage allowance rather than a fissile fraction.

**The flag, and it is on the right material.** The commercial MCFR states that **first plants start
with 12 % enrichment**. A power reactor is *critical*, so its `k_inf = 1` crossing lies **below** that
— 10.80–11.64 % across a wide leakage band — while this model puts the U-235 crossing at **14.66 %** in
the same salt. **The model demands 1.26–1.36× more fissile than published practice does**: the safe
direction for a reactor, the **unsafe** direction for a criticality-safety *threshold*. Scaled by that,
the Pu-239 threshold would be **6.15–6.63 %** against the design's operating **8.35 %** — **the design
would sit above its own threshold** — and **the two claims may not be simultaneously satisfiable**: at
6.15 % the plant does not close, at 6.63 % it needs 2,010 MW of beam against 240.

**It is a flag and not a result**, and its three cautions are load-bearing — the MCFR's composition is
unstated, 12 % is a start-up figure whose geometry and leakage are unpublished, and scaling the Pu-239
threshold by the U-235 conservatism assumes the model errs by the same multiple on both nuclides.
**What it is worth is its direction**: the transport calculation is not a formality. It decides whether
the design as it stands is internally consistent, and **phase 4 proceeds when it is done.**

**And the material itself is now an open decision rather than a forced one.** `materials.py` called
the chemistry **forced** in three links — fast spectrum, therefore liquid fuel, therefore a salt,
therefore a chloride. `tools/fuelform.py` tests each. **Two are weaker than stated.**

**Link 3 breaks.** The always-subcritical property is **not bought by the salt**: `k_inf` is a ratio
of macroscopic cross sections and every one scales with density, **so density cancels**. What sets the
threshold is the fissile fraction and what the carrier absorbs. Across eight candidate fuel forms the
crossing runs **7.21 % to 9.71 % — a spread of 1.35** — and the design's own salt is the **second
worst** at 8.35 %, needing 1.16× more fissile than bare oxide for the same property. **MOX in
lead-bismuth crosses lower, at 8.08 %.**

**Link 2 is weaker than it looks.** *"The fuel must be liquid"* is really *"fission products must come
out"*, and **EBR-II closed its own fuel cycle on site for thirty years** with solid metal fuel and
batch pyroprocessing. Batch is not online and the difference is real — a lower equilibrium
fission-product inventory — but it is not a forcing, and **this work has never priced it.**

**Link 1 stands.** Nothing challenges the fast spectrum.

**And the column that decides it is provenance.** The design's chloride is the **only candidate with
NONE in both operating history and criticality benchmarks**. The two accelerator-driven systems
actually being built — **MYRRHA and CiADS** — chose **MOX in lead-bismuth**, behind which stand
Phénix, Superphénix, BN-600, BN-800, Joyo and FFTF.

**So the salt uniquely buys one thing — online fission-product removal — and uniquely costs
provenance.** If `deck.py --provenance`'s flag holds, the design is paying its entire provenance budget
for a safety property it does not get, which is available at a lower fissile fraction in a material
with sixty years of operating history. **The decision is the author's, and it is now a decision rather
than an inheritance.**

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
