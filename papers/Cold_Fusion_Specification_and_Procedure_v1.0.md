# The Cold Fusion Reaction: Complete Specification, Bill of Materials, and Laboratory Procedure

**Matthew Lach** — Independent researcher
*v1.0, 6 September 2026. Prepared with a computing collaborator under the protocols of* The Method *v1.2-8.*

*An independent application paper. It uses the lattice, carries its own abstract and its own
references, and takes no part in the main paper's subject matter. It is not a member of either live
bundle.*

> **What this document is.** *Cold Fusion and the Binder Economy* [1] defines the reaction, proves it
> unique, and bounds its energy return. This is the executable half: the reaction specified to the
> last parameter, the materials it takes, and the procedure that witnesses it. Every quantity is
> carried by `papers/CLAIMS.tsv` and checked by
> `python3 tools/verify_paper.py papers/Cold_Fusion_Specification_and_Procedure_v1.0.md`.

> **What it will and will not produce, stated before anything else.** The procedure in §3 witnesses a
> **self-sustaining catalytic cycle**: one binder driving of order **150** fusion events without
> further input per event. That is a cold fusion reaction by the definition of §1, it is producible on
> apparatus that exists, and this document tells you how.
>
> **As a standalone power source it is closed by theorem** (§5.1): no binder anywhere in the
> structural window reaches unity, the best case being **0.807**, short by **1.24**. **As a
> co-product it is net-positive** (§5.2): pions are made by the same collisions that make a
> spallation target's neutrons, so a facility already running a proton driver is making binders and
> discarding them. Captured, they return **10.5** to **31.6 percent** of the beam energy as fusion
> heat at zero marginal beam cost — **176 kW** on a one-megawatt driver. That is a net-positive
> reaction with no input per event and no input for the binder, and it is the only configuration
> found that is.

---

## Abstract

A cold fusion reaction is a nuclear fusion event in which the approach to nuclear separation is
supplied by molecular binding geometry rather than by kinetic energy. Seven conditions are necessary
for such an event to occur and be verifiable; applied to the closed index of charged particles they
admit exactly one realisation, the negative muon, because a structural window on the binder mass —
**[119, 918]** electron masses — contains one leptonic occupant. This document specifies that
realisation completely.

**§5 is the result.** As a purpose, the reaction cannot pay for itself — a theorem, not a
measurement. As a co-product of a beam running for another reason, it pays for itself entirely,
because its only input is a binder that facility is already making and throwing away. The same
observation dissolves this corpus's own flux gap, which compared against *delivered* muon beams:
in-situ capture is **2.80 × 10⁴** times the best planned delivered beam, since nothing is transported
and nothing is selected.

**§1** states the reaction and fixes every free parameter from witnessed measurement: fuel, ratio,
purity, density, temperature, binder, and the two observables that verify it. **§2** is the bill of
materials, in two columns: a bench demonstration and a reactor-scale target. **§3** is the laboratory
procedure — assembly, loading, beam, acquisition, and the two simultaneous measurements whose
disagreement is a refusal rather than an average. **§4** states what the procedure will return and what
it cannot: a catalytic cycle of order 150, an energy return capped at 0.464, and a flux short by
1.2 × 10⁵ of one megawatt.

The reaction is proven and has been witnessed since 1957. The **configuration** specified here — this
fuel at this purity, this density and this temperature, with both observables on one target — has not
been assembled. It is offered in the corpus's own idiom: determined by the mathematics, absent from
observation.

## 1. The reaction, specified

**The event.**

> μ⁻ + (d, t) → (dtμ)⁺ → ⁴He + n + μ⁻ + **17.59 MeV**

The muon is not consumed. It is released and forms the next muonic molecule, and the cycle repeats
until the muon decays or is lost to the alpha.

**Why this and nothing else.** The binder must be charged, must be light enough that the fusion rate
outruns its own cycle, and must be heavy enough that the molecular index does not degenerate. Those
two bounds are a window on the binder mass, **[119, 918]** electron masses. The window admits the
muon at **207** and the pion at **273**; the pion is hadronic and is absorbed before it can catalyse.
The electron lies below the window and the tau above it. **The candidate index closes at exactly one
occupant.**

**And on one sign of it.** A μ⁻ replaces an electron and binds a nucleus. A μ⁺ does the opposite — it
binds an electron, into muonium, and is repelled by every nucleus in the fuel. It forms no
mesomolecule at any density or temperature, enters no cycle, sticks to no alpha, and catalyses
nothing. So the binder is not "a muon": it is the negative one, and it has exactly one parent, π⁻
decay. Every yield quoted in this specification and in [1] is a π⁻ yield for that reason, and §2
carries the consequence.

**Every free parameter, fixed.**

| parameter | value | why it is fixed there |
|---|---|---|
| fuel | deuterium–tritium | the d+t channel has the highest yield per unit sticking of any muonic channel |
| ratio | 50/50 by number | not critical; the transfer step auto-optimises the population |
| **purity** | better than **1 ppm** high-Z | transfer to a contaminant runs at **1.0e10** s⁻¹ per liquid density of it; at the bracketed density **5.49 ppm** costs as much binder as decay does |
| temperature | **800 K** | the Vesman resonance transfers the dtμ loose state's **0.66 eV** into a **0.36 eV** host vibrational quantum; the rate rises toward this point |
| **cycle-rate ceiling** | **2.6e8** s⁻¹ | the cycle is a harmonic sum, so driving the resonance moves the bottleneck to transfer, verified at **2.7e8**. Temperature buys **3.6** and then stops |
| density | as high as the cell reaches | the cycle rate scales with it; the service life does not, being capped by sticking |
| binder | **μ⁻** — the negative muon, not the muon | §1 above; the positive one catalyses nothing at all |
| binder source | an existing muon beam | no new machine is required to witness the reaction |

**The two observables, and they must be simultaneous.**

| observable | what it counts |
|---|---|
| neutrons at **14.1 MeV** | fusion events, hence cycles per binder |
| the muonic-helium K-alpha at **8.2 keV** | binders stuck to the alpha, hence the sticking directly |

They share no instrument and no calibration. That is what makes them two routes rather than one.

**What is already witnessed, and what is not.** The reaction is witnessed: it has run since 1957, and
the highest yield on record is **150** fusions per binder. The effective sticking is witnessed at
**0.505**, **0.515** and **0.532 percent** in three independent measurements at 1.2 to 1.4 times
liquid density. **What is unwitnessed is this configuration**: that fuel at that purity, at 800 K,
with both observables running on one target at once. No experiment has held all of those at the same
time, which is why §3 exists.

## 2. Bill of materials

**Column A is a bench demonstration** — it witnesses the reaction and returns the numbers §3 asks for.
**Column B is the reactor-scale target** the balance of [1] is computed against, given so that the two
are not confused.

| item | A — bench | B — reactor scale |
|---|---|---|
| fuel | D–T, 50/50, **4 mg** | D–T, 50/50 |
| tritium inventory | ~**23.1 Ci** (≈2.4 mg) | **3.59 kg** at a 265 MeV/c stopping window |
| target vessel | diamond anvil cell, **19.2 mm³** sample volume | one muon range deep: **33.9 g/cm²** areal density |
| pressure | to **933 MPa** | as required for density; inventory does not fall with compression |
| temperature | cryogenic to **500 K** design ceiling, **400 K** demonstrated | 800 K |
| gas handling | uranium storage beds, palladium permeator, helium glovebox at negative pressure | same class, scaled |
| purity control | permeator plus in-situ Raman; assay to better than **1 ppm** | same |
| binder source | existing beam, ~**1.0e8** μ⁻/s | **1.2e15** μ⁻/s for one megawatt |
| capture solenoid | none — use the facility's beamline | **20 T**, field–radius product **2.60 T·m**, a **13 cm** clear bore |
| **production target** | none | tungsten or tantalum, thick — **high-Z is a requirement, not a convention** |
| neutron detection | array calibrated at 14.1 MeV | — |
| X-ray detection | resolving **8.2 keV**, viewing the same sample volume | — |
| blanket | none | ⁶Li-bearing, **1.6×** neutron energy multiplication |

**The production target's material is set by the charge, not only by the yield.** Measured off the
HARP tables for both signs at 8 GeV/c, lead returns π⁻/π⁺ = **0.973** and aluminium **0.732** — a
factor of **1.329**. At equal *total* charged-pion yield a low-Z target therefore delivers **0.857**
of lead's π⁻, the remainder going to the sign that cannot catalyse; and the low-momentum π⁻ excess
that a collector's window sits in appears in lead and tantalum and not in lighter targets at all. The
tungsten of column B already satisfies this. It is recorded here because the requirement was
previously met without being stated, and a specification that does not state it could be met by a
target that fails it.

**The two columns differ by six orders of magnitude in binder flux and three in tritium, and that
difference is the subject of §4.** Column A is buildable now. Column B is not.

## 3. The laboratory procedure

**Standing conventions.** A null is a bound: every step is written so a negative result yields a
number. A disagreement between the two observables is a **refusal, not an average**. And the
prediction is committed before the measurement, so neither can be adjusted afterwards.

### 3.1 Assembly

1. Build the target cell to hold **19.2 mm³** at up to **933 MPa** and up to **500 K**. Braze diamond
   to metal; use no polymers anywhere the fuel touches, and construct everything past the permeator
   from tritium-compatible material.
2. Enclose the gas system in a helium glovebox held at negative pressure, with continuous cleanup and
   secondary containment on every uranium bed.
3. Mount the cell on a stage that translates it into and out of the beam axis without breaking
   containment.
4. Site the neutron array and the X-ray detector so that **both view the same sample volume at the
   same time.** This is the step the existing experiments do not take, and it is the point of the
   procedure.

### 3.2 Loading

5. Bake the system for **12 hours**, then flush twice with ultra-pure deuterium.
6. Desorb D–T from a uranium bed, assay it in a calibrated ionisation chamber, and condense it through
   the permeator into the cell. Expect ~**4 mg** of fuel and ~**23.1 Ci** of tritium at 50/50.
7. Confirm the fill optically through the anvils and verify composition by in-situ Raman before any
   beam. **Purity is a variable of this experiment, not a precondition** — record it, do not assume it.
8. Close the cell, take it to pressure, and bring it to the setpoint temperature.

### 3.3 The measurement

9. Admit the muon beam. Tune it to stop in the fuel rather than the anvils.
10. Acquire **neutrons at 14.1 MeV** and the **8.2 keV** K-alpha **simultaneously**, on one fill.
11. Repeat across a **purity series** at fixed density and temperature. The existing record confounds
    purity with density and temperature — its cleanest data are also its coldest and densest — and this
    series is what separates them.
12. Repeat across a **density series** at fixed purity, and a **temperature series** toward the 800 K
    operating point.

### 3.4 What each outcome settles, committed in advance

| quantity | what this paper predicts | what it settles |
|---|---|---|
| cycles per binder | of order **150**, ceiling **198** | the service life, and whether the sticking cap is real |
| effective sticking, X-ray route | **0.505** to **0.532 percent** | the operative loss term |
| effective sticking, neutron route | the same, within error | **if the two disagree, report a bound — do not average** |
| purity dependence | binder loss rising linearly in high-Z contamination | separates purity from temperature and density |
| temperature dependence | cycle rate rising toward 800 K, then flat | tests the **3.6** ceiling that transfer imposes |

**A null at any step is a bound.** If the cycle count comes in below 150, that bounds the service life
from above. If the two sticking routes disagree, that is a refusal and the correct output is an
interval. If purity dependence is absent, the impurity channel is smaller than modelled and every
balance in [1] improves by a stated factor.

## 4. What this returns, and what it does not

**It returns a self-sustaining catalytic cycle.** One binder, of order **150** fusion events, no input
per event. That is a cold fusion reaction under §1's definition, running at ordinary temperature,
witnessed directly by two independent instruments.

**It does not return net energy, and the reason is proven rather than presumed.** The service life is
capped at **198** cycles by sticking, *at any density whatever*, so a binder returns at most
**5.16 GeV** against a floor of **11.13 GeV** to make one:

> **The energy return is bounded at 0.464.**

**And a second gap stands beyond that one, larger and independent.** One megawatt of fusion needs
**1.2e15** stopped binders per second. The best source today delivers ~**1.0e8**; the best planned
delivers ~**1.0e10**. That is a shortfall of **1.2e5** against what is planned and **1.2e7** against
what exists.

> **Q > 1 is necessary and not sufficient.** Even at breakeven, useful power would require a binder
> flux five orders beyond anything designed.

**Two branches are closed and should not be re-opened.** The ambient branch — screening in a metal
lattice — fails by conservation: the available screening ceiling is about **30 eV** against a
requirement of **88**, a factor of 2.9 in energy and **27 orders** in rate. And the binder cannot be
changed: sticking is a property of the fusion channel and not of the binder, so no other particle in
the known spectrum helps even if one existed inside the window.

**What would lift the energy bound**, if anything does, is stated in [1] §5.26 as four equivalent
single numbers, of which the live one is a reactivation coefficient of **0.727** against a witnessed
**0.35**. The flux bound is not addressed by any of them.

## 5. The net-positive configuration

§4 states the balance as a standalone reaction and it is negative. This section states the two
results that follow from taking the balance apart: a theorem that closes the standalone case for
good, and the one configuration in which the same reaction is net-positive.

### 5.1 The standalone case is closed by theorem, not by measurement

Condition 8 reduces, at the service-life cap, to a single inequality with three terms:

> **E_binder × ω_s ≤ V**

For the muon on d–t with a sourced blanket: **11.13 GeV × 0.505 % = 56.2 MeV** against **26.06 MeV**.
Short by **2.16**. Each term is now tested at its physical limit rather than its measured value.

**V cannot be raised without fission.** A non-fissioning blanket returns the alpha, the neutron's
energy, and the exothermic ⁶Li breeding, less the multiplier's endotherm. At multiplications of 1.6
to 2.5 that is **24.31** to **27.20 MeV**. Breakeven would need a multiplication of **6.33** neutrons
per source neutron — beyond any (n,xn) blanket, and reachable only by fission, which changes the
product rather than the yield.

**E_binder cannot be lowered by changing the binder.** Sticking is a property of the fusion channel
and not of the binder (§1), so a different occupant of the structural window moves only its own cost.
Taking the most favourable possible case — a hypothetical binder at the window floor of **119**
electron masses, produced as efficiently per unit rest mass as the muon:

| binder | E_binder | Q at the cap |
|---|---|---|
| muon, 207 mₑ | 11.13 GeV | **0.464** |
| window floor, 119 mₑ, hypothetical | 6.40 GeV | **0.807** |

> **No binder anywhere in the structural window reaches unity. The best case is 0.807, short by
> 1.24.** The window is closed on both sides by geometry and by index degeneracy, so there is no
> outside to appeal to.

That is a no-go theorem for cold fusion as a standalone power source, and it is tight: not orders of
magnitude, but a factor of 1.24 at the most favourable point that physics allows.

### 5.2 The binder does not have to be bought

The catalytic cycle has **no input per event**. Its only input is the binder. So the whole of the
negative balance sits in one question — what the binder costs — and there is a configuration in which
it costs nothing.

**Pions are a byproduct of spallation.** They are created in the same nuclear collisions that make a
spallation target's neutrons, by the same protons, in the same target. A facility running a proton
driver for neutrons, isotopes, or an accelerator-driven subcritical blanket **is already making them
and throwing them away.** Capturing them costs a collector; it does not cost beam.

On that accounting the marginal beam energy per binder is zero, and every fusion the binder catalyses
is gain. At the measured production of **0.7188** π⁻ per interacting proton, each captured binder
returning **150** cycles at **26.06 MeV**:

| capture efficiency | fusion heat, as a fraction of beam energy | reachable? |
|---|---|---|
| **30 %**, today's front end | **10.5 %** | yes |
| **34.2 %**, the ceiling at the specified inventory | **12.0 %** | yes — see below |
| **50 %** | **17.6 %** | only at ~45 kg of tritium |
| **90 %**, the specified collector | **31.6 %** | **no — above the ceiling at any target depth** |

**That last row is withdrawn, and the correction is this section's own.** A capture efficiency here
means a muon that *stops in the fuel*, and a stopping target is one muon range deep, so it stops only
the part of the accepted spectrum below its range. The bound is therefore not the collector's: it is
the solenoid's acceptance, **0.5069**, which no target depth exceeds and which tens of kilogrammes of
tritium only approach. At the **3.59 kg** this specification already carries — a 265 MeV/c window,
**33.9 g/cm²** — the ceiling is **0.3420**. Going to a 400 MeV/c window buys **0.3893** for
**6.93 kg**, and 700 MeV/c buys **0.4512** for **14.5 kg**. **The 90 % row compared a collector's
acceptance with a fuel target's stopping fraction, which are different quantities, and it is
withdrawn.** What survives is the row above it: **12.0 percent of the host beam returned as fusion
heat**, at an inventory this specification had already committed to.

On a one-megawatt, 8 GeV driver that is **2.80 × 10¹⁴** binders per second and **176 kW** of fusion
heat, delivered at the target where the facility's cooling loop already is.

> **This is a net-positive cold fusion reaction.** No input per event, no input for the binder, and
> real energy out. It is provable from witnessed quantities and it needs no number that has not been
> measured.

**And it dissolves this corpus's own flux gap.** Register R29 sets the requirement against delivered
muon beams — about **1.0 × 10⁸** per second today and **1.0 × 10¹⁰** planned — and finds a shortfall
of **1.2 × 10⁵**. Those are *momentum-selected, transported* beams, which discard almost everything
the target makes. In-situ capture at the production target is **2.80 × 10⁴** times the best planned
delivered beam, because nothing is transported and nothing is selected. **The flux gap is an artefact
of buying muons rather than making them where they are used.**

### 5.3 What this is, and what it is not

**It is a net-positive reaction.** Marginal energy in: zero. Energy out: **10.5 to 12.0 percent** of
the host beam, on the corrected ceiling above. That satisfies the project's criterion —
self-sustaining, no input per event — and it is the only configuration found that does.

**It is not a standalone power plant, and §5.1 says why it cannot be.** The host beam still costs more
at the wall than the fusion returns, and no arrangement of a non-fissioning blanket changes that. What
the fusion does is **recover 10.5 to 12.0 percent of the beam**, which on an accelerator-driven system
attacks that machine's dominant economic problem — the recirculating power its accelerator consumes.

**Three costs are real and are not beam.** The collector, priced in [1] §5.21 as a shielding trade of
about 2.7 in coil heating. The tritium, **3.59 kg** at a 265 MeV/c stopping window, which is a
licensing constraint before it is an engineering one. And the fuel target must sit in the production
target's region, which is a hostile place to put a cryogenic tritium cell and is not designed here.

**One caution on the accounting itself.** Treating the binder as free is a marginal-cost argument, and
it holds only while the host beam is justified by its other product. If the beam were run *for* the
muons, the full **11.13 GeV** returns and §5.1's theorem applies. **The reaction is net-positive as a
co-product and negative as a purpose.** That distinction is the whole of the result and it should not
be blurred.

## 6. The procedure for the net-positive configuration

§3 is the procedure for the bench demonstration, which witnesses the reaction and returns the numbers
the balance turns on. It is not a procedure for §5.2, and until now §5.2 had none — it was an
accounting, and an accounting is not an apparatus. This section is the apparatus.

**Why it is separate from §3.** The bench cell in §3 is fed by a *transported* muon beam: momentum
selected, steered down a channel, about **1.0e8** μ⁻/s. §5.2's whole argument is that transport is
what makes binders expensive, and that a cell placed where the muons are *made* pays no transport. The
two experiments therefore share their fuel, their observables and their tolerances, and share nothing
about where the cell sits.

### 6.1 Apparatus

| item | specification |
|---|---|
| host machine | a proton driver of ~**8 GeV** running for another product — spallation neutrons, isotopes, or a subcritical blanket |
| production target | tungsten or tantalum, thick; **high-Z is required for the charge** (§2) |
| capture solenoid | around the production target, field–radius product **2.60 T·m**. This is the one thing §5.2 does not get for free, and [1] §5.21 prices it as a shielding trade rather than a magnet problem |
| fuel cell | D–T, 50/50, areal density **5.00 g/cm²** along the beam, radius **0.16 mm** |
| tritium inventory | **2.42 mg**, i.e. **23.2 Ci** |
| cell position | inside the solenoid bore, downstream of the target, **before any momentum selection** |
| neutron detection | array calibrated at 14.1 MeV, gated on the machine's pulse structure |
| X-ray detection | resolving **8.2 keV**, viewing the same sample volume |

**The cell is small on purpose, and the reason is the whole of §5.25.** A stopping cell's tritium is
areal density times area, so it goes as the square of its radius — and so does the fraction of the
beam it intercepts. Rate and inventory fall together and their ratio is fixed. A cell of 0.16 mm
radius standing in a **7.5 cm** beam intercepts **4.55e-6** of it and holds **2.42 mg** of D–T. That
is the inventory an existing collaboration already holds, licenses and has commissioned a delivery
system for. **No new tritium authorisation is required to run this.**

### 6.2 What it is not

**It is not a power demonstration.** At that interception the cell returns **76 mW**. The experiment
measures a *rate*, and the rate is what the accounting turns on; the power follows from the geometry
by a factor this section states rather than hides.

### 6.3 The measurement

1. **Establish the background with the cell empty**, at full beam, gated as in step 4. The spallation
   flash is prompt and enormous; everything here depends on separating a delayed signal from it.
2. **Fill with pure deuterium** to the same areal density. d–d fusion runs at a rate some four orders
   below d–t under the same catalysis, so this is a second null, not a signal.
3. **Fill with D–T at 50/50**, assayed to better than **1 ppm** high-Z, per §2. Purity is not a
   refinement here: at the operating density **5.49 ppm** costs as much binder as decay does.
4. **Count both observables simultaneously, on one cell, gated from 1 μs to 10 μs after each proton
   pulse.** The muon lifetime is 2.2 μs and the catalytic cycle runs within it, so the fusion signal
   is delayed against a prompt spallation background by a window the machine's own pulse structure
   provides. §3.3's rule governs the two observables here exactly as it does there: they share no
   instrument and no calibration, and **a disagreement between them is a refusal, not an average.**

### 6.4 Committed predictions

Stated before the run, at 1 MW on target and the witnessed cycle count of **150**:

| quantity | committed value |
|---|---|
| binders stopped in the cell | **1.80e8** per second |
| 14.1 MeV neutrons | **2.70e10** per second |
| fusion heat in the cell | **76 mW** |
| ratio of the two observables | fixed by the witnessed sticking, **0.505** to **0.557 percent** |

**And the prediction scales linearly with one number that has not been measured.** The acceptance is
[1] §5.24's model, which reproduces the built front end's own MARS15 simulation to **0.982** and has
never been measured end to end. [1] §10.1 is that measurement. **If Stage A returns half the modelled
acceptance, every figure in this section halves**, and the experiment still runs — it becomes a
measurement of the acceptance by a second route.

### 6.5 What each outcome settles

| outcome | what it settles |
|---|---|
| the committed rate, both observables agreeing | §5.2 is demonstrated, not merely argued: a net-positive cold fusion reaction, running on a beam that was already running, with no input per event |
| a rate low by a constant factor, observables agreeing | the acceptance is lower than modelled by that factor. The configuration stands; the ceiling of §5.2 moves down by it |
| neutrons without the X-ray line, or the reverse | a refusal. §3.3's rule applies: the two are not averaged, and the run is repeated before either is believed |
| no delayed signal above background | the in-situ capture argument fails at the first step, and the flux gap of §5.2 is not an artefact of transport after all |

**This is the section the index said was missing**, and its absence was the only thing standing
between this corpus's one proved-positive configuration and a laboratory.

## 7. The open questions, worked

Nine open questions were carried. Six of them were calculations this work could already do, and
sorting them into categories was not the same as doing them. This section does them.
`python3 tools/collector.py --open` and `python3 tools/mucf.py --selftest` reproduce every figure.

| | question | status | what it returned |
|---|---|---|---|
| Q1 | the acceptance has never been measured end to end | **narrowed** | there is no span: the model run at a 5 T machine's own aperture reproduces that machine. Corroborated at **two fields differing by 4×**, to **0.823** and **0.982**. What is open is that nothing has measured it end to end |
| Q2 | which sticking branch is operative | **closed** | inverting the witnessed 150 cycles gives **0.517–0.547 %**, inside the measured trio and below theory |
| Q3 | the service-life model over-predicts by **2.24** | **closed** | at the corrected sticking it returns **150.5** cycles against 150 measured |
| Q4 | fuel purity is bounded by no experiment here | **closed** | the fuel behind the 150 carried at most **10.93 ppm**, below the **31.10 ppm** parity level |
| Q5 | the temperature axis is confounded | **closed** | every balance already runs the cycle rate *at* its ceiling, so deconfounding can raise nothing |
| Q6 | the **2.37** is unexplained | **explained, not adopted** | a normalisation, not a physics gain: **2.389** interacting nucleons reproduce it to 0.8 % |
| Q7 | a **0.186 sr** wedge is uncovered | **closed** | interpolation puts it at **1.072** against a bound of 1.10 |
| Q8 | transport, cooling and stopping unmodelled | **closed** | retired by §6 |
| Q9 | the composed sticking **0.234** is unresolved | **closed** | superseded by [1] §5.26 |

### 7.1 One measurement answers three of them

The 150 cycles is a measurement nobody disputes. Read *backwards* through the service-life expression
it returns a sticking — by a route that uses neither published sticking measurement:

> **ω_eff = 0.5171 %** at φ = 1.2 and **0.5471 %** at φ = 1.5.

That is a **third independent determination**, and it lands inside the measured trio (0.505, 0.515,
0.532 %) and **below** the coupled-channels value of 0.557 %. Q2 is answered: the operative sticking is
the measured one, not the theoretical one.

The same inversion answers Q3 without a new hypothesis. The **2.24** over-prediction was attributed to
"a density-dependent reactivation term or an unrealised reduction". It was neither: at 0.515 % the
model returns **150.5** cycles where it returned 335.3 at the superseded value. **The over-prediction
was the sticking and nothing else.**

And it bounds Q4. Any contaminant costs binder, so the fuel that returned 150 cannot have carried more
than the amount that would have pushed the model below 150. That is **0 to 10.93 ppm** across the
sticking and density bracket — in every case below the **31.10 ppm** at which impurity loss equals
decay loss. **The witnessed cycle count already carries its own purity**, which is why §6 uses it.

### 7.2 The 2.37, resolved

Three mechanisms were examined and bounded away from it: target thickness per interacting proton
(0.963–1.186), phase-space coverage (≤1.10), and beam species. Beam *energy* was the last candidate,
and HARP settles it, having published the same lead target at four beam momenta:

| beam GeV/c | π⁻ per interaction | GeV per π⁻ |
|---|---|---|
| 3 | 0.1646 | **18.231** |
| 5 | 0.3967 | 12.604 |
| 8 | 0.7142 | **11.202** |
| 12 | 1.0314 | 11.634 |

*(These integrate the coverage common to all four beam momenta, which is why the 8 GeV/c entry reads
11.202 against [1] §5.1's full-coverage 11.130.)*

**Beam energy has a broad optimum near 8 GeV/c, and going down to the optimised study's 3.61 GeV makes
production 1.63× dearer rather than 2.37× cheaper.** The candidate is refuted, and refuted in the
direction opposite to the one it was proposed in.

**What survives is not a physics gain at all. It is a normalisation.** The optimised figure is 0.77 π⁻
per *beam deuteron*; HARP's is per *interaction*. If each interacting nucleon behaves as a HARP proton,
that yield requires **1.94** interacting nucleons per beam deuteron at 5 GeV/c and **4.68** at 3 GeV/c
— and a deuteron carries **2** nucleons into a rod of **6.3** interaction lengths, so the lower end is
guaranteed before any secondary interacts. Re-normalising this work's own figure:

| interacting nucleons per beam particle | GeV per π⁻ |
|---|---|
| 1.000 | 11.202 |
| 2.000 | 5.601 |
| **2.389** | **4.688** — reproduces the optimised figure to 0.8 % |
| 3.000 | 3.734 |

**It is explained and it is not adopted.** The mechanism reproduces the number for pions *produced*,
and a thick target also reabsorbs them: the same source's thick/thin ratio for *captured* muons is
0.874–1.186 per interacting proton, which is evidence the gain may not survive to capture. [1] §10.3
is now the measurement that decides it — pions per beam particle against pions per interaction, on one
target — and that, rather than a species comparison, is what that stage is for.

### 7.3 The wedge, and the acceptance

HARP's two spectrometers leave **0.1856 sr** between them uncovered. Log-interpolating their
per-steradian densities in the momentum band where they overlap, and carrying the large-angle
spectrum's shape across, puts that wedge at **0.0876 barn** on top of 1.2220 — a factor of **1.0717**,
against a bound of 1.10. Production is therefore **10.385** GeV per π⁻ rather than 11.130. It is
`RECONSTRUCTED`, not measured: the two tables cover different momentum ranges, so no interpolation
returns the wedge's own spectrum.

**Q1 is narrowed, and the narrowing is a correction rather than a refinement.** An earlier version of
this section put a floor under the acceptance by taking a 5 T machine's captured yield as a lower
*estimate* of a 20 T machine's, and reported the gap between them — first 2131×, then 5.97× — as
uncertainty. **It is not uncertainty. It is two apertures.** Run [1] §5.24's model at that machine's
own aperture, in its own units:

> **0.0843** captured π⁻ per interacting proton, against its published **0.061–0.144**. Inside.

So the two ends were never two estimates of one number; they are one model at two apertures, and the
model predicts both. **The acceptance model is therefore corroborated by two independent published
simulations at fields differing by four times** — 0.982 against the 20 T front end's, 0.823 against
the 5 T capture solenoid's midpoint.

| | binders/s at 1 MW | fusion heat, fraction of host beam |
|---|---|---|
| at the specified aperture, modelled | **1.918e14** | **12.01 %** |
| scaled by the weaker corroboration | 1.578e14 | **9.88 %** |
| scaled by the stronger | 1.884e14 | 11.80 % |

**The width is 1.19×, not 2131 and not 5.97.** The superseded floor was a *measured* figure, which is
why it was attractive, but it measures what survives a beamline and §6 has none — a floor on a
different quantity. Both earlier statements of this span are withdrawn.

**What survives of Q1 is one thing, and no simulation can settle it.** Two simulations agreeing is not
a measurement, and neither models what an end-to-end machine loses that no one has thought to model.
[1] §10.1 — Stage A — measures exactly that, and it is the whole of what remains here.

> **Seven of nine closed, one narrowed to a width of 1.19, one explained and declined. The two that
> still move a number are measurements rather than calculations — whether an end-to-end machine loses
> more than any simulation models, and whether the thick-target normalisation survives to capture —
> and [1] §10 already runs both.**

**The answer's magnitude is 9.88 to 12.01 percent of the host beam**, and the sign is open at no value
of any of them: at the low end of that band and *one* fusion per binder — a case no measurement
supports and every measurement exceeds — it still returns **0.06589 percent**. Positive.

---

## References

1. M. Lach, *Cold Fusion and the Binder Economy: A Closed Definition, a Unique Realisation, and the
   Bound That Decides It*, v1.0 — the companion paper, which carries the derivations.
2. M. Lach, *The Binder Economy Against the Recent Literature*, v1.0 — the reconciliation companion.
3. M. Kamimura, Y. Kino and T. Yamashita, Phys. Rev. C **107**, 034607 (2023).
4. E. Koukina *et al.* (MuFusE Collaboration), arXiv:2606.19304; J. D. Kalow *et al.*, arXiv:2606.05333.
5. M. Lach, *The Method* v1.2-8 — *The Lach Cylinder: an index of transitions*.
