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

**Every free parameter, fixed.**

| parameter | value | why it is fixed there |
|---|---|---|
| fuel | deuterium–tritium | the d+t channel has the highest yield per unit sticking of any muonic channel |
| ratio | 50/50 by number | not critical; the transfer step auto-optimises the population |
| **purity** | better than **1 ppm** high-Z | transfer to a contaminant runs at **1.0e10** s⁻¹ per liquid density of it; at the bracketed density **5.49 ppm** costs as much binder as decay does |
| temperature | **800 K** | the Vesman resonance transfers the dtμ loose state's **0.66 eV** into a **0.36 eV** host vibrational quantum; the rate rises toward this point |
| **cycle-rate ceiling** | **2.6e8** s⁻¹ | the cycle is a harmonic sum, so driving the resonance moves the bottleneck to transfer, verified at **2.7e8**. Temperature buys **3.6** and then stops |
| density | as high as the cell reaches | the cycle rate scales with it; the service life does not, being capped by sticking |
| binder | μ⁻ | §1 above |
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
| production target | none | tungsten or tantalum, thick |
| neutron detection | array calibrated at 14.1 MeV | — |
| X-ray detection | resolving **8.2 keV**, viewing the same sample volume | — |
| blanket | none | ⁶Li-bearing, **1.6×** neutron energy multiplication |

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

| capture efficiency | fusion heat, as a fraction of beam energy |
|---|---|
| **30 %**, today's front end | **10.5 %** |
| **50 %** | **17.6 %** |
| **90 %**, the specified collector | **31.6 %** |

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

**It is a net-positive reaction.** Marginal energy in: zero. Energy out: 10 to 32 percent of the host
beam. That satisfies the project's criterion — self-sustaining, no input per event — and it is the
only configuration found that does.

**It is not a standalone power plant, and §5.1 says why it cannot be.** The host beam still costs more
at the wall than the fusion returns, and no arrangement of a non-fissioning blanket changes that. What
the fusion does is **recover 10 to 32 percent of the beam**, which on an accelerator-driven system
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

---

## References

1. M. Lach, *Cold Fusion and the Binder Economy: A Closed Definition, a Unique Realisation, and the
   Bound That Decides It*, v1.0 — the companion paper, which carries the derivations.
2. M. Lach, *The Binder Economy Against the Recent Literature*, v1.0 — the reconciliation companion.
3. M. Kamimura, Y. Kino and T. Yamashita, Phys. Rev. C **107**, 034607 (2023).
4. E. Koukina *et al.* (MuFusE Collaboration), arXiv:2606.19304; J. D. Kalow *et al.*, arXiv:2606.05333.
5. M. Lach, *The Method* v1.2-8 — *The Lach Cylinder: an index of transitions*.
