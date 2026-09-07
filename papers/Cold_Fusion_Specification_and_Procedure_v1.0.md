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
> heat at zero marginal beam cost — **176 kW** on a one-megawatt driver. **§5.2's own correction and
> §11's loss budget both bear on those two figures**: the reachable capture is **0.342**, not the
> 0.50 the 176 kW was computed at, and the budget takes it to **0.2438**, so the delivered figures
> are **8.56 percent** and **85.6 kW**. **The conclusion is untouched and only the magnitude moves** —
> the marginal beam energy is zero, so any positive number is gain. It is a net-positive reaction with
> no input per event and no input for the binder, and it is the only configuration found that is.

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
and nothing is selected — **1.37 × 10⁴** at the delivered capture of §5.2, which is the same argument
with the same conclusion.

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
| tritium inventory | ~**23.1 Ci** (≈2.4 mg) | **5.13 kg** at a 265 MeV/c window and the designed bore — §10.2 |
| target vessel | diamond anvil cell, **19.2 mm³** sample volume | one muon range deep: **33.9 g/cm²** areal density |
| pressure | to **933 MPa** | as required for density; inventory does not fall with compression |
| temperature | cryogenic to **500 K** design ceiling, **400 K** demonstrated | 800 K |
| gas handling | uranium storage beds, palladium permeator, helium glovebox at negative pressure | same class, scaled |
| purity control | permeator plus in-situ Raman; assay to better than **1 ppm** | same |
| binder source | existing beam, ~**1.0e8** μ⁻/s | **1.2e15** μ⁻/s for one megawatt |
| capture solenoid | none — use the facility's beamline | **20 T** peak, **14.01 T** at the target, aperture **1.50** or **2.60 T·m** — §8 designs it |
| decay channel and recompression | none | **34.1 m**, then back to **20 T** at the cell — §10.1 shows both are required |
| **production target** | none | high-Z, and a **free liquid-metal jet**: §9.4 shows the bore excludes every solid target |
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

**Column B is now designed rather than listed.** §§8–10 build it: the magnet, the circuit, the
conductor, the target, the lifetime, the plant, the decay channel and the fuel cell. Where this table
and those sections differ, **those sections govern** — and the one figure that moved is the tritium,
from the **3.59 kg** [1] computes at a 7.5 cm beam to **5.13 kg** at the designed bore recompressed to
20 T at the cell. §10.2 is why, and it is a cost of the design's own field choice rather than a new
requirement.

**The two columns differ by six orders of magnitude in binder flux and three in tritium, and that
difference is the subject of §4.** Column A is buildable now. Column B is designed and not built.

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

**Those two figures are stated at a capture of 0.50, and this section has just said 0.50 is not the
reachable one.** The correction above them is not carried into them, and §11's loss budget is not
carried into either. Both, applied:

| capture | binders per second | fusion heat |
|---|---|---|
| **0.50**, as printed above | 2.80 × 10¹⁴ | **176 kW** |
| **0.342**, this section's own ceiling at 3.59 kg | 1.918 × 10¹⁴ | **120.1 kW** |
| **0.2438**, that ceiling through §11's loss budget | 1.367 × 10¹⁴ | **85.6 kW** |

> **The conclusion is untouched and only the magnitude moves, and that asymmetry is the whole point of
> this configuration.** Every other balance in this work is a ratio against unity, so a factor of
> 0.7127 decides it. This one is not a ratio at all: the marginal beam energy per binder is **zero**,
> so *any* positive heat is gain and no loss factor can take it below unity. **85.6 kW of fusion heat
> at zero marginal beam cost is the same result as 176 kW**, reached by the same argument and arriving
> at a smaller number. It is the one figure in this work the acceptance census cannot falsify, because
> it was never conditional on an acceptance clearing a threshold.

> **This is a net-positive cold fusion reaction.** No input per event, no input for the binder, and
> real energy out. It is provable from witnessed quantities and it needs no number that has not been
> measured.

**And it dissolves this corpus's own flux gap.** Register R29 sets the requirement against delivered
muon beams — about **1.0 × 10⁸** per second today and **1.0 × 10¹⁰** planned — and finds a shortfall
of **1.2 × 10⁵**. Those are *momentum-selected, transported* beams, which discard almost everything
the target makes. In-situ capture at the production target is **2.80 × 10⁴** times the best planned
delivered beam — **1.37 × 10⁴** at the delivered capture above — because nothing is transported and
nothing is selected. **The flux gap is an artefact of buying muons rather than making them where they
are used**, and it stays dissolved by four orders of magnitude at either capture.

### 5.3 What this is, and what it is not

**It is a net-positive reaction.** Marginal energy in: zero. Energy out: **10.5 to 12.0 percent** of
the host beam on the corrected ceiling above, and **7.51 to 8.56 percent** through §11's loss budget.
That satisfies the project's criterion — self-sustaining, no input per event — at either figure, and
it is the only configuration found that does. **The criterion is the sign of the balance, not its
size**, which is why this is the one result the loss budget moves without deciding.

**It is not a standalone power plant, and §5.1 says why it cannot be.** The host beam still costs more
at the wall than the fusion returns, and no arrangement of a non-fissioning blanket changes that. What
the fusion does is **recover 10.5 to 12.0 percent of the beam** — 7.51 to 8.56 delivered — which on an
accelerator-driven system attacks that machine's dominant economic problem: the recirculating power
its accelerator consumes.

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

**This table was rewritten after §§8–10 designed the machine, and it named four things the machine
does not have.** What follows is the machine. `python3 tools/machine.py --coherence` prints it, and
every apparatus figure here is computed there rather than asserted.

| item | specification | where |
|---|---|---|
| host machine | a proton driver of ~**8 GeV** running for another product | §5.2 |
| production target | a free **liquid-metal jet**, 8 mm across at 27 mrad — *not* a rod or a wheel, which the bore excludes | §9.4 |
| capture solenoid | **20.0 T** peak, **14.01 T** at the target, grade **1.428**, aperture **1.50 T·m**, bore **10.71 cm** | §8 |
| shielding and coil | tungsten to a coil inner radius of **120.0 cm**; **1080 MJ** stored | §8.3, §9 |
| **decay channel** | **34.1 m**, without which no pion has decayed and no muon can stop | §10.1 |
| **recompression** | to **20 T** at the cell, which is a requirement and not an option | §10.1 |
| beryllium window | at **6 m**, stopping mercury vapour; a consumable | §9.4 |
| fuel cell | D–T 50/50, areal density **5.00 g/cm²**, radius **0.16 mm** | below |
| tritium inventory | **2.41 mg**, i.e. **23.2 Ci** | below |
| cell position | **after** the decay channel, in the recompression section — **not** in the capture bore | §10.1 |
| purification loop | continuous, removing ³He | §10.4 |
| neutron detection | array calibrated at 14.1 MeV, gated on the machine's pulse structure | §6.3 |
| X-ray detection | resolving **8.2 keV**, viewing the same sample volume | §6.3 |

**The four corrections.** §6 as first written named a **2.60 T·m** collector where the design is
**1.50 T·m** — the aperture at which the acceptance model is validated to 0.982; stood the cell in a
**7.50 cm** beam where the machine's is **8.96 cm** at the cell; put the cell "inside the solenoid
bore", which §10.1 shows is impossible; and used a forward-only acceptance for a machine that has a
mirror.

**Both bores are the same machine.** The coil radius is sourced at 120 cm and both apertures fit
inside it, so the cold mass, the stored energy and the conductor are identical — only the shield
thins, from 109.3 to 101.4 cm. The wider bore buys **1.188** in capture for **3.00** in tritium.
[1] §5.25 found that trade at **3.01** from the beam-envelope argument alone; **this package
reproduces it from the magnet**, and the two share no step — one is a gyroradius, the other a shield
and a coil.

**The cell is small on purpose, and the reason is the whole of [1] §5.25.** A stopping cell's tritium
is areal density times area, so it goes as the square of its radius — and so does the fraction of the
beam it intercepts. Rate and inventory fall together and their ratio is fixed. A cell of 0.16 mm
radius standing in the machine's **8.96 cm** beam intercepts **3.188e-6** of it and holds **2.41 mg**
of D–T. That is the inventory an existing collaboration already holds, licenses and has commissioned a
delivery system for. **No new tritium authorisation is required to run this.**

### 6.2 What it is not

**It is not a power demonstration.** At that interception the cell returns **71.2 mW**. The experiment
measures a *rate*, and the rate is what the accounting turns on; the power follows from the geometry
by a factor this section states rather than hides.

### 6.3 The measurement

1. **Establish the background with the cell empty**, at full beam, gated as in step 4. The spallation
   flash is prompt and enormous; everything here depends on separating a delayed signal from it.
2. **Fill with pure deuterium** to the same areal density. d–d fusion runs at a rate some four orders
   below d–t under the same catalysis, so this is a second null, not a signal.
3. **Fill with D–T at 50/50**, assayed to better than **1 ppm** high-Z, per §2 — and keep the
   purification loop running, because §10.4 shows the fuel is its own contaminant source and reaches
   1 ppm of ³He every **18.8 minutes** unpurified.
4. **Count both observables simultaneously, on one cell, gated from 1 μs to 10 μs after each proton
   pulse.** The muon lifetime is 2.2 μs and the catalytic cycle runs within it, so the fusion signal
   is delayed against a prompt spallation background by a window the machine's own pulse structure
   provides. §3.3's rule governs the two observables here exactly as it does there: they share no
   instrument and no calibration, and **a disagreement between them is a refusal, not an average.**
5. **Trip the beam on loss of either the jet or the field.** §9.6 is why: losing the field puts a large
   dose on the downstream coils, and losing the jet dumps 80 percent of beam power into the shielding.

### 6.4 Committed predictions

Stated before the run, at 1 MW on target and the witnessed cycle count of **150**, **computed from the
machine of §§8–10 and not from a hypothetical one**:

| quantity | committed value |
|---|---|
| binders stopped in the cell | **1.334e8** per second |
| 14.1 MeV neutrons | **2.002e10** per second |
| fusion heat in the cell | **56.4 mW** |
| ratio of the two observables | fixed by the witnessed sticking, **0.505** to **0.557 percent** |

**Three corrections took it there:** interception ×**0.700** because the machine's beam is wider than
§6 assumed; the mirror ×**1.488** because the machine has one and §6 did not; and the **end-to-end loss
budget** of §11 at ×**0.7127**, which replaces the bare decay factor this section first used. **Net
×0.743.**

> **The prediction survives being pointed at the real machine, and it falls by a quarter doing it.**
> The first two corrections nearly cancelled; the third does not, and §11 is where it comes from.

**And it still scales linearly with one number that has not been measured.** The acceptance is
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

Nine open questions were carried. **Seven of them were calculations this work could already do**, and
sorting them into categories was not the same as doing them. This section does six; §11 does the
seventh and narrows the last but one to a number. **One remains, and it is a measurement.**
`python3 tools/collector.py --open` and `python3 tools/mucf.py --selftest` reproduce every figure.

| | question | status | what it returned |
|---|---|---|---|
| Q1 | the acceptance has never been measured end to end | **narrowed to a budget** | §11 computes every loss term between a produced π⁻ and a stopped binder: product **0.7127**, end-to-end **31.66 %**. What remains is the measurement itself, now committed to a number **1.073×** above its own falsification floor |
| Q2 | which sticking branch is operative | **closed** | inverting the witnessed 150 cycles gives **0.517–0.547 %**, inside the measured trio and below theory |
| Q3 | the service-life model over-predicts by **2.24** | **closed** | at the corrected sticking it returns **150.5** cycles against 150 measured |
| Q4 | fuel purity is bounded by no experiment here | **closed** | the fuel behind the 150 carried at most **10.93 ppm**, below the **31.10 ppm** parity level |
| Q5 | the temperature axis is confounded | **closed** | every balance already runs the cycle rate *at* its ceiling, so deconfounding can raise nothing |
| Q6 | the **2.37** is unexplained | **closed** | a normalisation, not a physics gain: **2.389** interacting nucleons reproduce it to 0.8 %, and §11.1 shows the gain survives to capture at **0.8961** because a narrow target is transparent sideways |
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

**Q1 is narrowed, and what narrows it is two withdrawals rather than a new result.**

**The first.** An earlier version of this section put a floor under the acceptance by taking a 5 T
machine's captured yield as a lower *estimate* of a 20 T machine's, and reported the gap — first
2131×, then 5.97× — as uncertainty. It is not uncertainty; it is two different machines. That span was
never a statement about how well the acceptance is known, and it is withdrawn.

**The second is this section's own, from the pass that made the first withdrawal.** Replacing the span
with a "second corroboration at a quarter of the field" compared the model's **forward** hemisphere
against a machine whose transport solenoid takes *"backward-emitted secondary pions and muons"* [6].
In the hemisphere that machine actually uses, the model returns **0.0073** π⁻ per interacting proton
against its published **0.061–0.144** — low by **14.1×**, not inside the range. The forward number
lands inside by coincidence, which is exactly how the error was made.

**What that failure establishes is a scope limit, and it is worth more than the corroboration would
have been.** A graded capture solenoid magnetically *mirrors* forward-going particles into a backward
channel — it is why such machines are graded — and [1] §5.24's model has no mirror term, only a
transverse momentum cap. **Against a graded field the model is a lower bound, not an estimate**, by a
factor it cannot state.

> **The acceptance model has one validation, at one configuration: 0.982, forward capture, 20 T on a
> 7.5 cm bore — which is the configuration §6 specifies.** It may not be quoted as validated anywhere
> else.

So the width of what is known is the width of one agreement:

| | binders/s at 1 MW | fusion heat, fraction of host beam |
|---|---|---|
| at the specified aperture, modelled | **1.918e14** | **12.01 %** |
| scaled by the one validation | 1.884e14 | **11.80 %** |

with an **unquantified conservative bias** from the missing mirror term, and nothing measured.

**What is open is unchanged by any of this.** Nothing has been run end to end and weighed. Two
withdrawn claims and one validated simulation do not add up to a measurement, and [1] §10.1 — Stage A
— is the measurement. **No calculation in this work stands in for it, and this section stops trying.**

> **Eight of nine closed, one narrowed to a budget. The one that still moves a number is the
> measurement itself** — η, end to end — **and §11 computes every loss it is asked to find, so [1]
> §10.1 now tests a stated number rather than an unknown factor.**

**The answer's magnitude is 11.80 to 12.01 percent of the host beam** at the specified aperture, on one
validated simulation and no measurement. The sign is open at no value of any of it: at the low end and
*one* fusion per binder — a case no measurement supports and every measurement exceeds — it still
returns **0.07866 percent**. Positive.

## 8. The capture solenoid, designed

[1] §5.30 records that the acceptance model captures the forward hemisphere and carries no magnetic
mirror term, so against a graded field it is a lower bound by a factor it cannot state. **A graded
field is not an accident of other people's machines. It is what a capture solenoid is.** This section
designs one, which supplies the term, and the term is worth **1.299**.

`python3 tools/collector.py --magnet` reproduces every figure here.

### 8.1 The mirror, from the adiabatic invariant and nothing else

A pion's transverse momentum obeys p_T²/B = constant while |p| is conserved, so a pion travelling into
a rising field loses longitudinal momentum and reflects when it reaches zero:

> **reflected ⟺ sin θ ≥ √(B_t / B_max)**

and it returns with the same p_T and its p_z reversed — into the same transverse cap and the same
two-body decay integral as a forward pion at π − θ. Nothing is fitted and nothing is added to the
model but this one test.

| B_max/B_t | loss cone | captured μ⁻ per π⁻ produced | |
|---|---|---|---|
| 1.05 | 77.4° | 0.3833 | ×1.121 |
| 1.15 | 68.8° | 0.4172 | ×1.220 |
| 1.35 | 59.4° | **0.4443** | ×1.299 |
| **1.428** | 56.8° | **0.4443** | **×1.299** — saturates |
| 3.00 | 35.3° | 0.4443 | ×1.299 |

**It saturates, and the reason is a fact about the data rather than about magnets.** HARP's large-angle
table stops at **2.15 rad**, where sin θ = **0.837**. Once √(B_t/B_max) falls below that, the loss cone
no longer touches any *measured* production, and a deeper grade buys nothing this work can count.

> **The grade is a specification, not a search: 1.428, and no more.** That is the same shape as [1]
> §5.7's finding that sticking is binder-mass-independent and §5.28's that the target is fixed by the
> charge — a parameter that looked like a lever and turns out to be a requirement with a number on it.

**And it closes a loop with [1] §10.1.** That stage's committed band — **60.92**, **49.16** and
**44.43 percent**, at no window, 400 MeV/c and 265 MeV/c — was computed by accepting *both hemispheres*
of pion emission, an instrumentation choice with no mechanism attached. Because the required grade puts
the loss cone outside every angle HARP measured, **mirroring the backward hemisphere and accepting both
hemispheres are the same number**, and the mirror reproduces that band **to four figures**. The
laboratory programme asserted a capability; this section is the magnet that supplies it.

### 8.2 What frees the design: B·R sets capture, not B

The transverse cap is 0.15·B·R. **The field and the bore trade against each other at fixed capture**, so
the target field can be dropped and the bore grown — which is what brings the *peak* field, 1.428×
higher, inside what a magnet holds. Holding the front end's own **1.50 T·m**:

| | |
|---|---|
| peak field, upstream plug | **20.0 T** |
| target field | **14.01 T** (grade 1.428) |
| warm bore radius | **10.7 cm** |
| delivered beam envelope there | **10.71 cm** — fills the bore, by construction |
| gyroradius at the transverse cap | 5.35 cm |
| adiabatic taper, 10 gyro-orbits | **1.79 m** |
| magnetic length of the capture region | 1.50 m |

The envelope matching the bore is not a coincidence: a particle born on axis reaches twice its
gyroradius, and the cap was set so that it does.

### 8.3 The cold mass

| | |
|---|---|
| coil inner radius | **120.0 cm** — `SOURCED`, see below |
| tungsten shield | 109.3 cm |
| amp-turns | **23.9 MA-turns** |
| hoop stress allowed | 300 MPa |
| engineering current density | **12.5 A/mm²**, from σ = B·J·r |
| winding radial build | 127.3 cm |
| stored energy, field volume | **1080 MJ** — a lower bound |

**The coil radius is not this work's choice, and an earlier version of this section made it one.** That
version put a 70 cm shield around the bore, reaching an 80.7 cm coil radius and 489 MJ. A published
FLUKA and MARS study of this same target station — a 4 MW, 8 GeV beam on a mercury jet in a 20 T
solenoid [7] — found a 63 cm coil radius **inadequate** and doubled it to **120 cm** to bring the coil
heat load below a kilowatt. **The 70 cm shield is withdrawn.** At 120 cm the stored energy is
**1080 MJ**, and that study's own figure for the same geometry is *"approaching 1 GJ"* — which is the
first independent check on any number in this design.

The current density assumes **the conductor carries the whole hoop load**; a steel former raises it and
thins the winding in proportion. The conservative choice is quoted, and at **12.5 A/mm²** it sits below
the **23.2** that study's superconducting coils run at.

### 8.4 The plant

| | |
|---|---|
| heat to the cold mass at 1 MW | **140 W** — `SOURCED` [7], 0.56 kW at 4 MW over nineteen coils |
| refrigeration wall power | **37.3 kW** at 4.5 K, Carnot fraction 0.25 |

That heat load also replaces a reconstruction: this work had assumed 30 percent of beam power entering
the shield and computed 335 W. The measured-by-simulation figure is 140 W, and it is quoted instead.

### 8.5 What the mirror is worth to the answer

| | captured and stopped, per π⁻ produced | fusion heat, fraction of host beam |
|---|---|---|
| forward capture only, as §6 and §7 compute it | 0.3420 | **12.01 %** |
| **with the mirror** | **0.4443** | **15.61 %** |

**§6 and §7 are not restated at 15.61 percent.** They describe a machine with no mirror, which is not a
machine anyone builds — so their figures are an *under-specification of the apparatus*, and this
section is where the apparatus is specified. Both numbers stand, and which one applies is a fact about
which magnet is built.

### 8.6 What this is not

It is a physics design and a set of engineering requirements. It is not a build package, and three
things are named here and not done:

1. **Quench and energy extraction** at 489 MJ. That is a serious design item in its own right and it
   is not attempted.
2. **Conductor grading** between an HTS insert and an LTS outsert, with the field margin and the
   stability analysis that goes with it.
3. **The shielding.** ~~Whose one `RECONSTRUCTED` input belongs to a transport simulation this work
   does not run.~~ **Done, and by that simulation rather than by this work**: [7] is it, and §9 carries
   what it returns. The shield is 109.3 cm and the coil radius 120 cm because that study says so.

## 9. The build package

§8 designs the field and the cold mass. A field is not a machine. This section is what the magnet
alone does not supply: the circuit, the conductor, the target, the lifetime, the plant, the failure
modes and the integration. `python3 tools/machine.py` reproduces all of it.

**One finding here overturns a choice the magnet design implied, and it is the reason this is a
section rather than a paragraph:** the production target must sit **inside** the capture bore, the bore
is **10.7 cm** in radius, and that excludes the rotating solid target every megawatt-class facility
uses.

### 9.1 Circuit, quench and energy extraction

Stored energy is **1080 MJ**. The operating current is the choice that governs everything after it,
because inductance falls as 1/I²:

| I_op | L | dump at 10 kV | MIITs | hot-spot margin |
|---|---|---|---|---|
| 10 kA | 21.6 H | τ = 21.6 s | 1080 | 2.96× |
| **20 kA** | **5.40 H** | **τ = 10.8 s** | **2160** | **5.93×** |
| 30 kA | 2.40 H | τ = 7.20 s | 3240 | 8.89× |

At 20 kA: dump resistance **0.500 Ω**, peak dump power **200 MW** transiently into the resistor, copper
current density **25.0 A/mm²** at 50 percent copper, hot-spot allowance **64.0 s** against a dump of
10.8 s. Ramp in four hours needs **7.50 V** and a **150 kW** supply.

**The margin is a consequence of the conservative current density, and the two are one decision.**
§8.3's 12.5 A/mm² came from a hoop-stress limit with the conductor carrying the whole load. That same
choice puts the copper current density low, and the hot-spot allowance goes as its inverse square.
Raising J with a steel former would thin the winding **and** spend this margin.

### 9.2 Mechanics

| | |
|---|---|
| magnetic pressure at 20 T | 159.2 MPa |
| axial compression at the midplane | **720 MN** (73 kilotonnes) |
| winding cross-section | 14.72 m² |
| axial stress in the winding | **48.9 MPa**, against 300 MPa hoop |
| cold mass | **177 t** (winding only) |
| cooldown enthalpy | 14.1 GJ, 300 → 4.5 K |

The axial load is large and the axial *stress* is not: it spreads over fourteen square metres. It is an
end-plate and tie-rod problem, not a conductor problem — and [7] reports inter-coil forces of 1 to 10
kilotonnes for the same geometry, which is the same problem decomposed differently.

### 9.3 Conductor, graded

Field falls through the winding, so each superconductor is used only where it can carry current:

| band | r_in | r_out | conductor |
|---|---|---|---|
| REBCO | 1.200 m | 1.455 m | **1.99 km** |
| Nb₃Sn | 1.455 m | 1.965 m | 5.13 km |
| NbTi | 1.965 m | 2.473 m | 6.66 km |

**13.8 km** total at **1194 turns**. REBCO is needed for the innermost fifth only — 1.99 km, which is
procurable; fusion magnets order hundreds of kilometres.

**And there is a sourced alternative that uses no HTS at all.** [7]'s design of this same station
reaches 20 T as a **resistive copper insert of about 6 T inside a superconducting outsert of about
14 T**, Nb₃Sn for the inner nine coils and NbTi beyond, at 16.6 A/mm² in the copper and 23–40 in the
superconductor. It buys away the HTS procurement and pays in resistive power and in the **405 kW**
those copper coils absorb from the cascade. Both routes are real; this work computes the
all-superconducting one and names the other rather than choosing.

### 9.4 The target, and the constraint that decides it

**The power split is sourced, and it replaces a reconstruction this work made that was wrong by a
factor of 6.9.** [7] puts **319 kW of 4 MW** into the jet — **8.0 percent**, not the 55 percent assumed
— with **53.7 percent** into the shielding and **10.1 percent** into the resistive coils.

| | |
|---|---|
| into the jet | **80 kW** at 1 MW |
| target length | 20.6 cm, two interaction lengths |
| **available bore radius** | **10.7 cm** |

**A static rod is excluded, and so is the rotating wheel.** A 1 cm rod runs at **64 kW/kg** against a
demonstrated 0.45. A wheel reaching that demonstrated figure needs a radius of **0.355 m** — **3.3×
the bore.** The capture solenoid's aperture is the whole reason the pions are captured at all, so the
bore cannot be opened to admit a wheel without losing the capture the machine exists for.

> **This is a hard geometric exclusion, and it survives the factor-of-6.9 correction** — the margin was
> 23× on the wrong deposition figure and is 3.3× on the sourced one. That it survives is the only
> reason it may still be stated.

**What fits is a free liquid-metal jet, and it has been run.** [7]'s jet is **8 mm** across at **27
mrad** to a beam of 1.2 mm rms, the angle chosen to optimise *low-momentum* pions — which is this
work's own requirement, arrived at independently in §8.1.

| mercury jet, 8 mm | 10 m/s | 20 m/s | 30 m/s |
|---|---|---|---|
| mass flow | 6.8 kg/s | 13.6 kg/s | 20.4 kg/s |
| temperature rise | **84 K** | 42 K | 28 K |

Mercury boils at 357 °C, so every velocity above about 10 m/s clears it. **The correction relaxed this
requirement**: on the wrong deposition figure the jet needed 30 m/s, and that velocity floor is
withdrawn. The configuration — a free mercury jet crossing a high-field solenoid bore under a pulsed
proton beam — is not a novelty of this design: it was built and run at CERN as **MERIT**, in a 15 T
solenoid, for this application [8]. [7] adds that a solid or **powdered tungsten** jet gives similar
radiation levels, so the jet need not be mercury; **it must be a jet**.

The jet brings one item the magnet does not: a **beryllium window at 6 m** to stop mercury vapour
reaching the channel, taking **0.9 DPA/yr** and replaced on schedule. It is a consumable, and the
build must carry it.

### 9.5 Radiation lifetime

| | |
|---|---|
| heat to the cold mass | **140 W** at 1 MW, nineteen coils |
| peak power density | **0.05 mW/g**, against ITER's 0.17 |
| peak dose | **0.39 MGy/yr** at 1 MW |
| allowed integrated dose | **100 MGy** |
| **coil life** | **253 years** at full duty |
| displacements per atom | 3.0e-4 /yr against a critical 1.9e-3 |

All sourced from [7], and all far better than this work first reconstructed — because those coils
carry **ceramic** insulation rather than organic, and the limit is an order of magnitude higher than
the epoxy figure assumed. This work's own reconstruction, from the heat load and an assumed
peak-to-mean of 10, returns **0.64** of the published dose; the published figure is the one quoted.

### 9.6 Failure modes

[7] simulated both that matter. **Loss of field**: jet-and-pool deposition rises ~2.5× and the
downstream coils take a large dose, mitigated by a conic shielding extension from 3 to 6 m. **Loss of
jet**: ~80 percent of beam power dumps into the tungsten-carbide shielding and beam-pipe casing.
**Both at once**: nearly half the beam power thermally shocks the mercury pool, with splash velocities
approaching 50 m/s.

> The consequence for the build is the useful part: **the jet and the field must each trip the beam,
> and the shielding must be a rated dump and not only a shield.**

### 9.7 The plant

Steady load at 4.5 K is **144 W** — 140 radiation plus 4 in HTS current leads — for **38.4 kW** of wall
power. Cooldown is 14.1 GJ, **16.3 days** on a 10 kW 80 K circuit. Bore vacuum **1e-4 Pa**, set by
target outgassing rather than by muon scattering. HTS leads at 0.1 W/kA cost 4 W where conventional
leads would cost forty times that: the cheapest decision in the package.

### 9.8 Integration, and the one thing still undone

Three things share a bore of 10.7 cm radius, in this order along the axis:

1. **the liquid-metal jet**, its nozzle and its catcher, crossing at 27 mrad so the jet does not run
   down the muon channel;
2. **the field taper**, 1.79 m of it, where the mirrored pions turn round and where nothing may
   obstruct them;
3. **the D–T cell**, one muon range deep, at 800 K, in a radiation field, with tritium containment —
   beside a mercury loop.

> **The fuel cell beside the jet is the one item in this package that is neither computed nor referred
> to a machine that exists.** §5.3 already said the cell "must sit in the production target's region,
> which is a hostile place to put a cryogenic tritium cell and is not designed here." That is still
> true. It is named rather than absorbed, and it is the fourth item for [1] §10.

Everything else above is either computed from a conserved quantity or taken from a published
simulation or experiment of this same machine.

### 9.9 A weakness in this work's own verifier, found while writing this section

`verify_paper.py` pass 3 requires that every number in the prose appear in the ledger. **It matches a
value against *any* row carrying it, not against the row that ought to carry it.** Three figures in an
early draft of §9.3 and §9.7 — a conductor length, a total, and a wall power — were wrong by 1 to 5
percent and *passed*, because unrelated rows elsewhere in a 660-row ledger happened to carry those
values. They were caught by recomputing each figure against its own named function, not by the
harness.

> **A value test is not a binding test**, and the publication standard of §7 of [1] should be read
> with that limit in view. It is recorded here rather than repaired: binding each prose figure to a
> claim id would require marking up the prose, which is a change to the standard and not a fix to a
> paper. The three figures are corrected above.

## 10. The fuel cell, and where it can sit

§9 named one item it did not do: the D–T cell's mechanical and thermal design beside a liquid-metal
target in a high field. This section does it. `python3 tools/machine.py --channel --cell` reproduces
every figure, and two of the results change things §9 and the specification had already said.

### 10.1 The cell cannot sit in the capture region

A pion must decay before its muon can stop, and at the stopping window a pion's decay length is
**14.82 m**. The capture region is 1.5 m long.

| π momentum | decay length | 90 % decayed by |
|---|---|---|
| 100 MeV/c | 5.59 m | **12.9 m** |
| 200 MeV/c | 11.18 m | 25.8 m |
| 265 MeV/c | 14.82 m | **34.1 m** |

**A decay channel of 34.1 m is required**, and the muons survive it easily — their own decay length
there is **1652 m**.

**And the beam expands through it, which is the expensive part.** Adiabatic invariance grows the
envelope as 1/√B and the tritium inventory as its square:

| channel field | beam envelope | tritium *if the cell sat there* |
|---|---|---|
| 1 T | 40.08 cm | **102.5 kg** |
| 2 T | 28.34 cm | 51.3 kg |
| 5 T | 17.92 cm | 20.5 kg |

> **Recompression at the cell is not an optimisation, it is a requirement** — and it is free, because
> adiabatic compression conserves \|p\| and therefore leaves the stopping range and the momentum
> window exactly where they were.

### 10.2 Recompression is a lever on tritium, and it prices §8.2

| cell field | beam envelope | tritium at a 265 MeV/c window |
|---|---|---|
| 10 T | 12.67 cm | 10.25 kg |
| 14.01 T (the capture field) | 10.71 cm | 7.32 kg |
| **20 T** | **8.96 cm** | **5.13 kg** |
| 30 T | 7.32 cm | 3.42 kg |

**§8.2 dropped the target field to 14.01 T to bring the peak inside reach.** That widened the beam, and
a wider beam is more tritium — **7.32 kg** at the capture field against **5.13 kg** recompressed to
20 T. **The field reduction had a cost, and recompression pays it back.** Neither was visible until the
cell was designed, which is the argument for designing it.

### 10.3 The density should be low, which inverts the specification

Pressure falls linearly with density; cell length grows as its inverse. **Length is cheap and pressure
is not.**

| φ | pressure at 800 K | cell depth | monobloc vessel at 300 MPa |
|---|---|---|---|
| 0.222 | 52.1 MPa | 864.4 cm | r_o/r_i = 1.19 |
| 0.400 | 93.9 MPa | 479.8 cm | 1.38 |
| **0.600** | **140.8 MPa** | **319.8 cm** | **1.66** |
| 1.000 | 234.7 MPa | 191.9 cm | 2.86 |

§2 says "density: as high as the cell reaches". **On the demonstrated cycle count the bred-fuel balance
breaks even at 0.222 of liquid density** ([1] §5.27), so the cell need not reach high at all — and the
reason to avoid it is hard rather than economic:

> At **500 MPa a 300 MPa steel is excluded however thick it is made.** A monobloc cylinder cannot hold
> a pressure equal to its own allowable stress at any wall thickness; the Lamé ratio diverges. **Run
> the cell as low as the balance allows**, and §2's instruction is corrected to that.

The pressures quoted are ideal-gas and are therefore a **lower bound** — real D–T at these densities is
strongly non-ideal — which is why the design point is 0.6 with margin rather than at a limit.

### 10.4 The heat, and a second requirement that turns out to be the same one

| | |
|---|---|
| muons stopping per second | 1.918e14 |
| kinetic energy each brings | **179.6 MeV** |
| stopping power into the fuel | **5.52 kW** |
| alpha heating, 150 cycles × 3.5 MeV | **16.13 kW** — the alpha stays in the fuel |
| **total into the fuel** | **21.65 kW** |
| neutrons leaving to the blanket | 65 kW |
| **flow to remove it** | **0.0372 kg/s** at ΔT = 100 K |

**The fuel must flow. And helium-3 says so independently.** Tritium decays at **1.824e18** per second
in a 5.13 kg inventory, so **³He reaches 1 ppm every 18.8 minutes** — against the 1 ppm high-Z purity
§2 requires, in a fuel that is its own contaminant source.

> **Two requirements arrived from different directions and one loop meets both.** The flow that carries
> 21.65 kW out carries the fuel through the purifier, and the rate the heat sets — 0.0372 kg/s, a
> 230-second turnover — holds ³He at **0.204 ppm**, already below what the specification demands. The
> cell's design closes on itself.

### 10.5 What is now undone

Nothing in the physics. The package is complete to the level of a physics design with engineering
requirements. What is **not** here is a fabrication package: drawings, tolerances, weld and joint
design, the tritium plant's own licensing case, and a quench analysis run in a magnet code rather than
on a hot-spot integral.

**That is engineering-office work on a design that exists, which is a different thing from a design
that does not.**

## 11. The end-to-end loss budget, and the two questions it couples

§7 left two questions open and called both measurements rather than calculations. **One of them was a
calculation.** This section does it, and doing it sharpens the other rather than softening it.
`python3 tools/machine.py --budget` reproduces every figure.

### 11.1 Q6 closes on geometry

Whether a thick target's multiplicity gain survives to *captured* muons was the open half of §7's Q6.
It does, and the argument is geometric rather than simulated.

The pion absorption length is **15.9 cm** in mercury and **10.8 cm** in tungsten. But **the collector
takes large-angle pions** — **85.0 percent** of production, [1] §5.1 — **and a large-angle pion leaves
the target sideways.** Its escape path is the target's *radius*, not its length:

| target | sideways | forward | weighted escape |
|---|---|---|---|
| the published jet, 30 cm × 8 mm | 0.9751 | 0.4495 | **0.8961** |
| the optimised rod, 652 × 5.1 mm | 0.9767 | 0.1654 | **0.8547** |
| a 20.6 cm rod, 2 cm across | 0.9116 | 0.4467 | 0.8417 |
| a 10 cm-radius block | 0.3964 | 0.4467 | **0.4040** |

> **A narrow target is transparent however long it is.** The multiplicity that explains the 2.37
> survives to capture at **0.8961**, and the condition is that the target be long and *thin*. The
> published geometries already are — 652 mm by 5.1 mm, 30 cm by 8 mm — which is not a coincidence but
> the same argument, arrived at by whoever designed them.

### 11.2 The budget

| term | factor | what it is |
|---|---|---|
| target escape | **0.8961** | §11.1 |
| pion decay completeness | 0.9000 | the channel is cut at 90 % by choice, §10.1 |
| muon survival in the channel | 0.9796 | 34.1 m against a 1652 m decay length |
| scattering out of the transverse cap | **0.9021** | conservative: the whole kick taken off the cap |
| adiabatic transport | 1.0000 | unity **by design**, conditional on the bore schedule |
| **product** | **0.7127** | |

The scattering term is a 4 mm path through mercury — **0.84** radiation lengths, giving a **12.39
MeV/c** transverse kick against a 225 MeV/c cap. The kick is random in direction and so broadens
rather than shifts; taking the whole of it off the cap is the conservative reading and the one quoted.

**Not modelled, and named rather than omitted:** the beryllium window's **1.18 MeV** and **1.20 MeV/c**,
both carried as negligible; field errors and non-adiabatic transitions, which are a magnet calculation;
the jet's magnetohydrodynamic distortion, which is what MERIT was built to measure; and collimation,
which is a layout this design does not fix.

### 11.3 It sharpens Stage A rather than softening it

[1] §10.1 measures η — the **delivered** figure, end to end — and committed to the model's band. The
budget is what stands between the two:

| window | model | end to end |
|---|---|---|
| no window | 60.92 % | **43.42 %** |
| 400 MeV/c | 49.16 % | 35.03 % |
| 265 MeV/c | **44.43 %** | **31.66 %** |
| *falsification floor* | | *29.51 %* |

**The margin over the number that would falsify the model falls from 1.51× to 1.073×.** A prediction
that close to its own falsification is a far sharper commitment, and that is the budget working as it
should: **it did not make the answer better.**

### 11.4 And the two questions were coupled

At **31.66 percent** the bred-fuel route does **not** close at the **50.8 percent** its
demonstrated-cycle balance needs. It closes at the **21.4 percent** the *optimised* production target
needs — and whether that target's gain is real was Q6, answered in §11.1 at 0.8961.

> **The budget would have closed the route, and Q6 re-opens it.** Neither question could be answered
> alone and leave the result standing. Answering both together is what leaves it standing, and that
> coupling was invisible while both were called "measurements" and set aside.

The co-product balance of §5.2 moves with it: fusion heat falls from **15.61** to **11.12 percent** of
the host beam. The sign does not move, and cannot: the marginal beam cost is still zero.

---

## References

1. M. Lach, *Cold Fusion and the Binder Economy: A Closed Definition, a Unique Realisation, and the
   Bound That Decides It*, v1.0 — the companion paper, which carries the derivations.
2. M. Lach, *The Binder Economy Against the Recent Literature*, v1.0 — the reconciliation companion.
3. M. Kamimura, Y. Kino and T. Yamashita, Phys. Rev. C **107**, 034607 (2023).
4. E. Koukina *et al.* (MuFusE Collaboration), arXiv:2606.19304; J. D. Kalow *et al.*, arXiv:2606.05333.
5. M. Lach, *The Method* v1.2-8 — *The Lach Cylinder: an index of transitions*.
6. K. Oishi *et al.*, *Development of the Range Counter for the COMET Phase-α Experiment*,
   arXiv:2505.07464 — §1, which states the backward-emission capture.
7. J. J. Back, *Energy deposition studies for the Neutrino Factory target station*, JINST,
   arXiv:1104.2742 — FLUKA and MARS over a 4 MW, 8 GeV proton beam on a free mercury jet in a 20 T
   solenoid: tables 1–4, the increased-shielding geometry, and the radiation-damage estimates.
8. K. T. McDonald *et al.*, *The MERIT high-power target experiment at the CERN PS*, IPAC 2010,
   p. 3527 — the free mercury jet run in a 15 T solenoid.
