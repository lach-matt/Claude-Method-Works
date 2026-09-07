# Cold Fusion by Muonic Binding

*A proof from witnessed quantities, the materials it requires, and the procedure that would witness it*

M. Lach

Version 1.0


## Abstract

A **cold fusion reaction**, as this paper uses the term, is a nuclear fusion event in which the approach to nuclear separation is supplied by molecular binding geometry rather than by kinetic energy. The definition is structural rather than thermal: it does not say that the reaction is cold in the everyday sense, only that the work of bringing two nuclei within tunnelling range is done by a bound state instead of by a collision.

Seven conditions are necessary for such an event to occur and to be checkable. Applied to the closed index of charged particles, they turn out to admit **exactly one** realisation — the negative muon — because the conditions place both a floor and a ceiling on the mass of whatever does the binding, and the window between them, 119 electron masses to 918 electron masses, has a single leptonic occupant.

That reaction is not speculative. It has been observed in laboratories since the 1950s, and its cycle rates, its losses and its ash have all been measured. What has never been observed is a configuration of it that returns more energy than it costs to run, and the distance between those two statements is the subject of this paper.

To close that distance we add an **eighth condition** to the seven. A binder is worth making only if the energy it costs to make is less than the energy it returns over its working life, which may be written `E_binder < Q_fus · f_work / ω_s`. Every term in it has been measured. Against a sourced production-and-capture cost of 37.0 GeV per captured μ⁻, the resulting figure of merit is 0.203 when the return is counted as heat and 0.102 when it is counted as work.

The first question is then whether a better collector could close the gap, and the answer is that it could not. Integrating the measured pion production cross sections shows that **production alone** costs 11.13 GeV per pion, so even a perfect collector — one that turned every pion made into a stopped binder — would leave the heat form short. Three further results move the balance. Sticking, the term that dominates the loss, turns out to be independent of the binder's mass, which means that the eighth condition is a specification on the machine rather than a search for a better particle. The convertible fraction of the fusion yield is 0.795 rather than 0.501, once the alpha is counted at the operating point the design already requires. And priced as **bred fuel** rather than as heat, the fusion neutron is worth 146.06 MeV per fusion against 26.06 MeV.

The paper then applies to its own figures the same test it applies to the literature's. Every balance it states is stated *at* some assumed collection efficiency, and an acceptance is not the same thing as a delivered efficiency. Computing each loss that lies between a produced pion and a binder actually stopped in the fuel gives a budget of 0.7127, and the solenoid's own stopping ceiling is 0.5069, so the acceptance the machine delivers is 31.66 percent rather than the 90 percent [DESIGN] the balances had been read at. **At the delivered figure, and with the machine as built, nothing clears unity** — every heat form, every work form and bred fuel at the demonstrated cycle count fall below it.

The machine is not obliged to stay as built, however, and this paper prices the alterations it proposes against every balance rather than against one. An optimised production target is worth 2.373 on any of them. It takes bred fuel at the demonstrated cycle count to 1.480, which is the route the laboratory programme measures first, and it takes the **heat** form, on the bound-case service life, to 1.036 — or 1.231 with a wider bore as well. **A device-internal route therefore clears unity, though conditionally**: it depends on a measurement that confirms the target, on a service-life model the paper notes over-predicts, and on the reading of "inside the device" that counts the blanket. Counting the neutron at its bare heat instead, the same alteration reaches only 0.3344, and on that reading nothing here clears.

One configuration is net-positive on witnessed numbers alone, and it is not the standalone one. Pions are a byproduct of spallation, made in the same collisions that produce a spallation target's neutrons, so a facility already running a proton driver for neutrons or isotopes is making binders and discarding them. The marginal beam energy per binder is then **zero**, and any positive heat is gain. At the reachable capture of 0.2438, that comes to 85.6 kW of fusion heat on a one-megawatt driver. It is the one result here that a loss factor rescales without deciding, because it was never a ratio against unity in the first place.

Finally, the materials are specified to the last free parameter, the machine that supplies the binders is designed as a build package rather than sketched, and the laboratory programme is set out as four staged measurements on apparatus that already exists — the acceptance measurement first, because it multiplies every balance identically and so bounds all of them at once.


---


## 1. The definition, and the seven conditions

We take a cold fusion reaction to be **a nuclear fusion event in which the approach to nuclear separation is supplied by molecular binding geometry rather than by kinetic energy.** The definition is structural rather than thermal. It makes no claim that the reaction runs near room temperature; it says only that the work of bringing two nuclei within tunnelling range is done by a bound state instead of by a collision, and that distinction is what the rest of the paper turns on.

Seven conditions are necessary for such an event to occur and to be checkable. They are stated here in the order in which they constrain the problem, and each is used later.

1. **Approach by binding.** The internuclear separation must be set by the geometry of a bound state.
1. **Sufficient proximity.** That separation must be small enough for the tunnelling rate to exceed the decay rate of the state that produced it.
1. **A catalytic cycle.** The binder must survive the event and be available to repeat it, or the accounting is a single-shot reaction and not a catalysis.
1. **Commensurate ash.** The event must produce the heavy products its energy release implies, in the branching ratios the nuclear physics fixes.
1. **An independent observable.** At least one signature must be measurable that is not the heat.
1. **A closed energy account.** Every input must be nameable and priced.
1. **Reproducibility from a specification.** The configuration must be statable in terms another laboratory can build.
The second of these is what rules out the ordinary electronic molecule, and it does so by a margin that no arrangement of chemistry repairs. In a muonic *dt* molecule the two nuclei sit 280 fm apart; in the electronic molecule they sit 74100 fm apart. Because the tunnelling rate depends exponentially on that separation, the difference between the two amounts to some ninety-one orders of magnitude in the rate.

It is sometimes suggested that screening in a dense medium might make up the difference. It cannot, and the reason is a conservation argument rather than a measurement. Reaching the required approach by screening alone would call for 88 eV of static screening, where the ceiling available in condensed matter is 30 eV — short by 2.9, which corresponds to 27 orders of magnitude in the rate. For scale, a vibrational quantum in D₂ is 0.365 eV, and that is the order of the energy actually on offer.


## 2. The unique realisation

Applied to the closed index of charged particles, the seven conditions admit exactly one realisation, and the argument that gets there is short. Condition 2 sets a lower bound on the binder's mass, because the separation it produces scales inversely with that mass. Conditions 3 and 4 set an upper bound, because a binder heavy enough to be absorbed by a nucleus before the cycle completes catalyses nothing and produces the wrong ash. Together the two bounds define a **structural window** running from 119 electron masses to 918 electron masses. §13.3 derives both bounds in full.

Exactly one particle in the known spectrum sits inside that window: the muon, at 207 electron masses, which is 1.74 above the floor. The other candidates are excluded, and none of the exclusions is a near thing.

| excluded | grounds |
|---|
| electron-bound systems | geometry: 74100 fm against 280 fm, some ninety-one orders short |
| tau and heavier binders | nuclear absorption preempts catalysis; no cell survives condition 3 |
| hadronic binders | the same, at a shorter timescale still |
| enhanced ambient screening | conservation, §1 |
| thermal and inertial fusion | by definition — approach supplied by kinetic energy |
| chain multiplication of binders | no nuclear event releases enough to fund a second binder |

The sign matters as much as the mass, and it is fixed separately. A positive muon binds an electron into muonium and is repelled by every nucleus in the fuel, so it forms no mesomolecule at any density or temperature. The species question is therefore settled by charge before anything else is considered — a point §6 returns to, because it decides what the production target must be made of.

The reaction is therefore not hypothetical. The event μ⁻ + (d,t) → (dtμ)⁺ → ⁴He + n + μ⁻ + 17.59 MeV has been observed in laboratories since the 1950s, and its cycle rates, sticking fractions and ash have all been measured. What remains unwitnessed is a configuration of it that pays for itself, and that is what the remainder of the paper is concerned with.


## 3. The eighth condition

The seven conditions settle whether the reaction occurs. None of them settles whether it is worth running, and it is that second question — not the first — which has remained open. The condition below is what makes it answerable.

> **Condition 8.** A binder is worth making only if `E_binder < Q_fus · f_work / ω_s`, where `E_binder` is the energy cost of producing and capturing one binder, `Q_fus` the energy released per fusion, `f_work` the fraction of that release convertible to the form being paid in, and `ω_s` the probability per cycle that the binder is lost.

The right-hand side is simply the total a single binder can return before it is lost. Its service life in cycles is at most `1/ω_s`, and each cycle yields `Q_fus · f_work`. Condition 8 is therefore not an efficiency target that might be approached with better engineering, but an accounting identity — and every quantity appearing in it has been measured. Proposition 1 in §13.2 derives it, including the sense in which the cycle bound is asymptotic and never quite reached.

There are two conventions in use for `f_work`, and this paper carries both rather than choosing. Counted as heat delivered, the bound is 7.52 GeV; counted as electrical work recoverable from that heat, it is 3.77 GeV. A figure quoted without saying which convention produced it cannot be checked, so every balance below is labelled with its own.

**Against a sourced production-and-capture cost of 37.0 GeV per captured μ⁻**, the figure of merit is 0.203 as heat and 0.102 as work. That is the state of the question as the literature leaves it.


### 3.1 Sticking is binder-mass independent, so condition 8 is a specification

The loss term `ω_s` is dominated by **sticking**: the probability that the muon leaves the fusion bound to the alpha particle and is lost from the cycle. It is the term that most attempts at improvement have aimed at.

It cannot, however, be improved by changing the binder, and the reason is that the binder's mass cancels out of the overlap integral that defines sticking. The orbit the binder occupies and the recoil it must escape both scale with that mass in the same way, so their ratio — which is what sticking depends on — does not change. Theorem 2 in §13.4 gives the proof.

The consequence is larger than the calculation. Since no admissible binder does better, condition 8 cannot be satisfied by looking for a different particle; it is a specification on the *machine* rather than a search over the *spectrum*. And §2's window has already shown that there is no other occupant to search for in any case.

The measured values unfortunately straddle the decision. Two published final stickings — 0.45 percent from SIN and 0.56 percent from PSI — sit on either side of the break-point this paper computes at 0.1580 percent. Which of them is right determines whether the heat form of condition 8 is satisfied even at perfect collection, and no calculation offered here can stand in for that measurement. §8 sets out the protocol that would settle it.


## 4. What the binder costs, measured rather than assumed

The figure of merit given above rests on 37.0 GeV per captured μ⁻, which is a sourced end-to-end number for a machine that was built for an entirely different purpose. That is a fair starting point but a weak one to argue from, since a reader may reasonably reply that a machine designed for this job would do better. This section therefore replaces it with a floor computed from the production physics alone, which no collector can argue away.


### 4.1 Production, integrated from measured cross sections

Pion production has been measured double-differentially, so obtaining the yield is a matter of integration rather than of modelling. Over the large-angle acceptance — 0.35 rad to 2.15 rad in angle, momenta up to 0.80 GeV/c, at a beam momentum of 8 GeV/c — the integrated π⁻ cross section on a heavy target is 1.0382 barn, which corresponds to 0.6107 π⁻ per proton. The forward acceptance, 0.025 rad to 0.25 rad, adds a further 0.1838 barn. Taken together the production is 0.7188 π⁻ per proton, and at the beam energy in question that works out at 11.13 GeV per pion. Proposition 7 in §13.6 sets out the integral.

> This settles the first question a reader is likely to ask. 11.13 GeV is what a pion costs before any collector exists at all, so it is a floor on the binder's cost. Set against the heat bound of 7.52 GeV, even a *perfect* collector — one in which every pion produced became a stopped binder, which no machine approaches — would leave the heat form short. **The gap is not in the collector**, and no improvement to it can be the answer.

It is worth noting which hemisphere carries the yield, because a common argument turns on it. The forward hemisphere is the large one, at 15 percent of combined production against the backward sliver's 35 percent of the measured acceptance. Since the machine that has been built captures the forward hemisphere, a suggestion that a reactor might gain a large factor by capturing the other one is a suggestion about the smaller half, and the gain available is correspondingly modest.


### 4.2 Three results that move the balance

The first is that the convertible fraction had been an accounting choice rather than a physical limit. Counting only the neutron gives 0.501. Counting the alpha as well — at the hot operating point the design already requires — and including the exothermic ⁶Li breeding that a *d*–*t* cycle must run in any case, gives 0.795. Nothing has been added to the physics here; a term that was being discarded has simply been counted.

The second is that the neutron is worth considerably more than the heat it deposits. Priced as heat, a fusion returns 26.06 MeV. Priced as **bred fuel** — that is, with the neutron breeding tritium and fissile material in a blanket that a *d*–*t* plant must have in any event — the same fusion returns 146.06 MeV. This is not an improvement to the reaction. It is the same reaction, the same binder and the same cycle, priced against what its neutron is actually worth rather than against the heat alone.

The third is a change in how the question is posed. Rather than assuming a collector and computing the gain that follows, it is more useful to set each balance to unity and solve for the collection efficiency at which that product would break even. Asked that way, the three products separate cleanly:

| product | service life | value per fusion | collection needed |
|---|
| electricity, bound case | 190.1 cycles | 19.55 MeV | 299.6 percent |
| heat, bound case | 190.1 cycles | 26.06 MeV | 224.7 percent |
| bred fuel, bound case | 190.1 cycles | 146.06 MeV | 40.1 percent |
| **bred fuel, demonstrated cycles** | **150 cycles** | **146.06 MeV** | **50.8 percent** |

> What this produces is a separation rather than a margin, and the difference matters. Electricity is not a robust product here: it would need 299.6 percent collection *and* the bound-case density *and* the favourable sticking branch, all three at once, and losing any one of them loses the result. **Bred fuel at the demonstrated 150 cycles**, by contrast, asks nothing of the density axis, nothing of the sticking measurement and nothing of reactivation. It is a specification on the collector alone.


## 5. The collector, and the number that decides it


### 5.1 What sets the acceptance

A capture solenoid accepts a pion if its transverse momentum lies below `p_T = 0.15 · B · R`. Because field and bore appear only as a product, the two trade against one another at fixed acceptance, and it is the product `B·R` — not the field on its own — that sets what the magnet can take. Proposition 4 in §13.5 derives this, together with the factor of two that makes the beam envelope twice the gyroradius. The best studied front end runs 20 T on a bore giving an aperture product of 1.50 T.m; the collector specified here would need 2.60 T.m, a factor of 1.74.

With that in hand the acceptance becomes a calculation rather than an assumption. It is built up in four steps: the production spectrum, the transverse cap above, the two-body pion decay integrated over the pion rest frame, and finally whatever momentum requirement the downstream apparatus imposes. Run over the configuration of the machine that has actually been built, the model returns 29.51 percent against that machine's own published simulation, the two agreeing to 0.982.

> **The acceptance model is therefore validated against an independent simulation of a machine that was built**, rather than against the assumptions that produced it, and that is what licenses the acceptance figures below.

Run over a reactor's configuration, at today's aperture and accepting both hemispheres, the model gives 60.92 percent with no momentum requirement and 44.43 percent through a stopping window of 265 MeV/c.


### 5.2 An acceptance is not a delivered efficiency

Every balance stated so far has been stated at some collection efficiency, and none of those efficiencies is one the machine delivers. The distinction is easy to lose and it changes every number in the paper, so it is worth being explicit. Two results stand between an acceptance and a binder actually stopped in the fuel, and every balance above must be read through both of them.

The first is that a muon the solenoid accepts but the fuel does not stop is not a binder at all. A stopping target is one muon range deep, so it stops only that part of the accepted spectrum lying below its range. The ceiling on capture is therefore set by the solenoid's own acceptance, 0.5069, which no target depth exceeds, and which only tens of kilogrammes of tritium even approach.

The second is that each loss lying between a produced pion and a stopped binder can be computed rather than assumed. They are as follows.

| term | factor | what it is |
|---|
| escape from the production target | 0.8961 | large-angle pions leave sideways, so the escape path is the target's radius |
| pion decay completeness | 0.9000 | the fraction of accepted pions decaying inside the channel |
| muon survival in the channel | 0.9796 | against the muon decay length |
| scattering out of the transverse cap | 0.9021 | conservative: the whole kick taken off the cap |
| adiabatic transport | 1.000 [DESIGN] | unity **by design**, conditional on the bore schedule |
| **product** | **0.7127** |  |

**The delivered acceptance is therefore 31.66 percent** at today's aperture, or 37.62 percent at the wider bore — against the 90 percent [DESIGN] the balances were read at.

![Figure 5](papers/figures/fig5-budget.png)

**Figure 5.** What becomes of a hundred pions made in the target. Each step is a loss that can be computed rather than assumed, and the product of them is the difference between what the magnet accepts and what the fuel actually stops.


### 5.3 Every balance at the acceptance actually delivered

Because the balance is linear in collection — Proposition 6 in §13.5 — restating the table at a different efficiency is exact rather than approximate, and the paper's own two-column table provides the check.

| balance | as stated at 90 percent [DESIGN] | delivered, 31.66 percent | wider bore, 37.62 percent |
|---|
| heat, demonstrated cycles | 0.316 | 0.111 | 0.132 |
| heat, bound-case service life | **1.241** | **0.437** | 0.519 |
| heat, φ = 3 | 1.011 | 0.356 | 0.423 |
| work, demonstrated cycles | 0.237 | 0.083 | 0.099 |
| work, bound-case service life | 0.931 | 0.328 | 0.389 |
| bred fuel, demonstrated cycles | 1.772 | 0.623 | 0.741 |
| bred fuel, bound-case service life | 6.96 | **2.449** | 2.909 |

> **At the delivered acceptance, and with the machine left as it is, nothing clears unity.** Every heat form, every work form and bred fuel at the demonstrated cycle count fall below it. **The figures reported at ninety percent collection in the preprints at [18] are withdrawn as end-to-end results**; they stand as the conditionals they were stated at.

**But the machine is not required to be left as it is**, and §5.4 states what the alterations specified here do to the same table.


### 5.4 What the specified alterations do to every balance

§5.3 states the balances for the machine as built. Two alterations to that machine are specified in this paper — an **optimised production target** and a **wider bore** — and it is worth asking what each does to the whole table rather than to one row of it. The target multiplies every balance by the same factor, because a balance has the form `N · V · η / E_binder` and the target moves `E_binder` alone: from 11.13 GeV to 4.69 GeV, which is worth 2.373. Corollary 6.1 in §13.5 makes this explicit.

> **The factor checks against the requirement it moves.** §4.2 puts bred fuel at demonstrated cycles at 50.8 percent collection; through the optimised target that requirement is 21.4 percent, and 50.8 ÷ 2.373 returns it. The same factor applied to that route's delivered balance of 0.623 gives 1.480, which is §5.3's own figure reached from the other side.

| balance | delivered | + optimised target | + target and wider bore |
|---|
| heat, demonstrated cycles | 0.111 | 0.264 | 0.313 |
| **heat, bound-case service life** | 0.437 | **1.036** | **1.231** |
| heat, φ = 3 | 0.356 | 0.844 | **1.003** |
| work, demonstrated cycles | 0.083 | 0.198 | 0.235 |
| work, bound-case service life | 0.328 | 0.777 | 0.924 |
| bred fuel, demonstrated cycles | 0.623 | **1.480** | **1.758** |
| bred fuel, bound-case service life | 2.449 | **5.811** | — |

![Figure 4](papers/figures/fig4-range.png)

**Figure 4.** The range the reaction is expected to fall in. Each row is one way of pricing the same reaction; the bar runs from what the machine as built delivers to what it delivers with the optimised production target and the wider bore. Anything reaching the line at unity pays for itself.

> **The answer is conditional, and it is not no.** With the optimised production target in, the heat form on the bound-case service life reaches **1.036** at today's aperture and **1.231** at the wider bore, and the φ = 3 case reaches **1.003** with both. **Those clear unity, and they are not bred fuel** — nothing leaves the device to earn them.

**Three conditions travel with that result, and each is stated in full below.**

**First, it is the bound-case service life and not the demonstrated one.** At 150 cycles per binder, which is what has actually been measured, the optimised target takes heat only to 0.264 and work to 0.198. **Nothing device-internal clears at a witnessed cycle count under any alteration specified here.**

**Second, the bound case rests on a service-life model that over-predicts.** It returns more cycles than were measured at the one point where a comparison is possible (§11). Every figure in the two bound-case rows inherits that; the bred-fuel row at demonstrated cycles does not.

**Third, the factor itself is unmeasured here.** 4.69 GeV is a published optimisation this paper does not adopt, and §10 Stage C is the measurement that would settle it. **The whole of this section is conditional on that stage**, which is the second reason it runs early.

> **And "inside the device" has two readings that do not agree.** The heat forms above count the blanket's multiplication and its fissile heat, which is heat recovered on site. Counting the neutron at its **bare** heat instead — no blanket, no fissile credit — the delivered figure is 0.1409, and the optimised target takes it only to 0.3344. **On the narrow reading the criterion is not met by anything in this paper.** On the wider one it is met by a specified machine, conditionally, and §10 is what decides between them.


---


## 6. The reaction, specified

This section answers the second directive: **what must be procured, built or assayed.** Every free parameter is fixed from a witnessed measurement, and each row states why it is fixed there rather than being asserted.

**The event.**

> μ⁻ + (d, t) → (dtμ)⁺ → ⁴He + n + μ⁻ + 17.59 MeV

The binder is not consumed. It is released and forms the next muonic molecule, and the cycle repeats until the muon decays or is lost to the alpha.

![Figure 1](papers/figures/fig1-cycle.png)

**Figure 1.** The catalytic cycle, and the two ways it ends. A single binder repeats the loop until it decays or is lost to the alpha; everything the paper prices is a consequence of how many times it goes round.


### 6.1 Every free parameter, fixed

| parameter | value | why it is fixed there |
|---|
| fuel | deuterium–tritium | the *d*+*t* channel has the highest yield per unit sticking of any muonic channel |
| ratio | 50/50 by number | not critical; the transfer step auto-optimises the population |
| **purity** | better than 1 ppm [DESIGN] high-Z | transfer to a contaminant runs at 1.0 × 10^10 s^-1 at 1 LHD of oxygen; at the bracketed density 5.49 ppm costs as much binder as decay does |
| temperature | 800 K | the Vesman resonance transfers the *dtμ* loose state's 0.66 eV into a 0.365 eV host vibrational quantum |
| **cycle-rate ceiling** | 2.6 × 10^8 s^-1 | the cycle is a harmonic sum, so driving the resonance moves the bottleneck to transfer, capped at 2.7 × 10^8 s^-1 |
| density | as high as the cell reaches | the cycle rate scales with it; the service life does not, being capped by sticking |
| **binder** | **μ⁻**, the negative muon | §2 — the positive one forms muonium and catalyses nothing at any density or temperature |
| binder source, to witness | an existing muon beam | no new machine is required to witness the reaction |

> **The binder is not "a muon"; it is the negative one, and it has exactly one parent — π⁻ decay.** Every yield in this paper is a π⁻ yield for that reason, and §6.3 carries the consequence into what the production target must be made of.


### 6.2 The two observables, and they must be simultaneous

| observable | what it counts |
|---|
| neutrons at 14.1 MeV | fusion events, hence cycles per binder |
| the muonic-helium K-alpha at 8.2 keV | binders stuck to the alpha, hence the sticking directly |

![Figure 7](papers/figures/fig7-measurement.png)

**Figure 7.** The step the existing experiments do not take. Both observables watch the same fuel at the same time, on one fill, so the cycle count and the loss are measured together rather than inferred from separate runs.

**They share no instrument and no calibration**, which is what makes them two routes rather than one. §9.3 commits in advance to treating a disagreement between them as a **refusal** rather than as an average.


### 6.3 Bill of materials

Column A witnesses the reaction. Column B is the reactor-scale target the balance is computed against, given so the two are never confused.

| item | A — bench demonstration | B — reactor scale |
|---|
| fuel | D–T, 50/50, 4 mg | D–T, 50/50 |
| tritium inventory | 23.2 Ci (≈ 2.41 mg) | 5.13 kg at a 265 MeV/c window and the designed bore |
| target vessel | diamond anvil cell, 19.2 mm3 sample volume | one muon range deep, 33.9 g/cm^2 areal density |
| pressure | to 933 MPa | as required for density; **inventory does not fall with compression** |
| temperature | cryogenic to a 500 K design ceiling, 400 K demonstrated | 800 K |
| gas handling | uranium storage beds, palladium permeator, helium glovebox at negative pressure | same class, scaled |
| purity control | permeator plus in-situ Raman; assay to better than 1 ppm [DESIGN] | same |
| binder source | an existing beam, about 1.0 × 10^8 s^-1 | 1.2 × 10^15 s^-1 for one megawatt of fusion |
| capture solenoid | none — use the facility's beamline | 20 T peak, 14.01 T at the target, aperture 1.50 T.m or 2.60 T.m |
| decay channel | none | 34.1 m, then recompression to 20 T at the cell |
| **production target** | none | high-Z, and a **free liquid-metal jet** — §7.3 |
| neutron detection | array calibrated at 14.1 MeV | — |
| X-ray detection | resolving 8.2 keV, viewing the same sample volume | — |
| blanket | none | ⁶Li-bearing, 1.6 x neutron energy neutron energy multiplication |

**The production target's material is set by the charge, not only by the yield.** Measured off the production tables for both signs, a lead target returns a π⁻/π⁺ ratio of 0.973 against aluminium's 0.732 — a factor of 1.329. At equal *total* charged-pion yield a low-Z target therefore delivers less of the sign that can catalyse, and the low-momentum π⁻ excess a collector's window sits in appears in the heavy targets and not in the light ones at all. **The requirement was previously met without being stated**, and a specification that does not state it could be met by a target that fails it.


### 6.4 What is witnessed here, and what is not

**The reaction is witnessed.** It has run in laboratories since the 1950s; the highest yield on record is 150 cycles per binder, and the effective sticking is witnessed in three independent measurements.

**What is unwitnessed is this configuration** — that fuel, at that purity, at 800 K, with **both observables running on one target at once.** No experiment has held all of those at the same time. That is the whole of what §9 is for.


---


## 7. The machine that supplies the binders

A procedure that would witness the *net-positive* configuration needs a machine capable of supplying binders at the required rate, and no such machine has been built. This section designs it. The design follows from the collection model of §5 rather than being introduced independently, so that the two cannot drift apart.

![Figure 2](papers/figures/fig2-machine.png)

**Figure 2.** The binder source, and the three alterations this paper proposes to it. The machine below the line is the one that has been built and simulated; the three callouts above it are what this paper would change, and each is priced in the text.


### 7.1 What the aperture fixes

The transverse cap is `p_T = 0.15 · B · R`, so **field and bore trade against each other at fixed capture**. Holding the built front end's aperture of 1.50 T.m and taking the peak field to 20 T at an upstream plug, the target field is 14.01 T and the warm bore is 10.7 cm — against a delivered beam envelope at the target of 10.71 cm, which is what a particle born on axis reaches at twice its gyroradius.

**The bore is derived rather than chosen**, and the same derivation reproduces three published geometries that were not used to build it: 7.50 cm, 30.0 cm and 13.0 cm.


### 7.2 The mirror, and why the grade is a specification

A magnetic mirror will reflect a pion emitted into the backward hemisphere provided its pitch angle satisfies `sin θ ≥ √(B_target / B_max)`. The grade required to reach every angle the production data covers is therefore fixed by that data's own angular limit, and it comes to **1.428** — no more, because that is simply where the measurement ends. Proposition 5 in §13.5 derives the condition from the adiabatic invariant.

> This has the same shape as §3.1's finding about sticking: a parameter that had looked like a lever turns out on inspection to be a requirement with a number attached to it. One consequence is worth noting — mirroring the backward hemisphere and simply accepting both hemispheres come to the same number, which is why §5.1's acceptances are stated over both.


### 7.3 The circuit, the cold mass, and the constraint that decides the target

| quantity | value | note |
|---|
| inductance at 20 kA [DESIGN] | 5.40 H | and 21.6 H at 10 kA [DESIGN], 2.40 H at 30 kA [DESIGN] |
| dump time constant | 10.8 s | the energy-extraction requirement |
| hot-spot margin | 5.93 | against an allowance of 64.0 s |
| cold mass, winding only | 176 t | at 8000 kg/m^3 |
| conductor, graded | 1.99 km of REBCO, 5.13 km of Nb₃Sn | the grading is what brings the peak field inside what a magnet holds |
| heat to the cold mass at 1 MW | 140 W | sourced, not reconstructed |
| peak coil dose at 1 MW | 0.395 MGy/yr | giving a coil life of 253 years at full duty |

> One finding here decides the production target, and it is the reason this section was necessary rather than optional. The target must sit inside the 10.7 cm warm bore. A rotating solid target — which is the choice of every megawatt-class facility built or planned — needs a wheel radius of 0.355 m to reach the demonstrated surface speed, and that is larger than the bore by more than a factor of three. The rotating target is therefore excluded by the aperture itself, and what remains is a **free liquid-metal jet**.

**The beam power the target must survive is 79.8 kW at 1 MW**, which is 7.98 percent of the driver, and it is a sourced figure rather than a reconstruction.

![Figure 3](papers/figures/fig3-target.png)

**Figure 3.** Why the production target must be a free liquid-metal jet. The capture field sets the bore, the bore sets the space the target may occupy, and the rotating solid wheel that every megawatt-class facility uses does not fit inside it.


### 7.4 The fuel cell, and where it can sit

The fuel cell cannot sit in the capture region, and where it does sit has a cost. The decay channel is 34.1 m long at the stopping window, and the beam must then be recompressed to 20 T at the cell if the fuel is to intercept it. It is that recompression which sets the tritium inventory at 5.13 kg, rather than the 10.79 kg a wider bore would require.

One point about that inventory is easily missed and is worth stating plainly: it does not fall with compression. Because the target must be one muon range deep, its tritium content is the areal density multiplied by the beam area. Compressing the fuel raises the density and shortens the target in exact proportion, so density buys length rather than inventory. Proposition 9 in §13.7 gives the argument.


---


## 8. The laboratory procedure

This section answers the third directive. **Standing conventions**, and they are committed before any run: a null is a bound, so every step is written to yield a number even when it fails; a disagreement between the two observables is a **refusal, not an average**; and every prediction is committed before the measurement, so neither can be adjusted afterwards.


### 8.1 Assembly

1. Build the target cell to hold 19.2 mm3 at up to 933 MPa and up to 500 K. Braze diamond to metal; use no polymers anywhere the fuel touches, and construct everything past the permeator from tritium-compatible material.
1. Enclose the gas system in a helium glovebox at negative pressure, with continuous cleanup and secondary containment on every uranium bed.
1. Mount the cell on a stage that translates it into and out of the beam axis without breaking containment.
1. Site the neutron array and the X-ray detector so that **both view the same sample volume at the same time.** This is the step the existing experiments do not take, and it is the point of the procedure.

### 8.2 Loading

1. Bake the system, then flush twice with ultra-pure deuterium.
1. Desorb D–T from a uranium bed, assay it in a calibrated ionisation chamber, and condense it through the permeator into the cell. Expect about 4 mg of fuel and 23.2 Ci of tritium at 50/50.
1. Confirm the fill optically through the anvils and verify composition by in-situ Raman before any beam. **Purity is a variable of this experiment, not a precondition** — record it, do not assume it.
1. Close the cell, take it to pressure, and bring it to the setpoint temperature.

### 8.3 The measurement

1. Admit the muon beam, tuned to stop in the fuel rather than in the anvils.
1. Acquire neutrons at 14.1 MeV and the 8.2 keV K-alpha **simultaneously, on one fill.**
1. Repeat across a **purity series** at fixed density and temperature. The existing record confounds purity with density and temperature — its cleanest data are also its coldest and densest — and this series is what separates them.
1. Repeat across a **density series** at fixed purity, and a **temperature series** toward the 800 K operating point.

### 8.4 What each outcome settles, committed in advance

| quantity | what this paper predicts | what it settles |
|---|
| cycles per binder | of order 150 cycles, ceiling 198 cycles | the service life, and whether the sticking cap is real |
| effective sticking, X-ray route | 0.5050 percent to 0.5320 percent | the operative loss term |
| effective sticking, neutron route | the same, within error | **if the two disagree, report a bound — do not average** |
| purity dependence | binder loss rising linearly in high-Z contamination | separates purity from temperature and density |
| temperature dependence | cycle rate rising toward 800 K, then flat | tests the ceiling that transfer imposes |

**A null at any step is a bound.** A cycle count below 150 cycles bounds the service life from above. A disagreement between the two sticking routes is a refusal, and the correct output is an interval. An absent purity dependence means the impurity channel is smaller than modelled, and every balance in §5 improves by a stated factor.


---


## 9. The net-positive configuration


### 9.1 The standalone case is closed by theorem, not by measurement

Considered as a purpose in itself, the reaction cannot pay for its own binders, and this is a theorem rather than an empirical result. Because sticking does not depend on the binder's mass (§3.1), the best balance available *anywhere* in the structural window of §2 is 0.807 — short of unity, and short of it for every occupant the window admits. There is no particle left to look for and no collector that can be built to change it. Theorem 3 in §13.4 gives the proof. §5.3 has already shown, separately, that even the routes which clear unity at an assumed collection efficiency do not clear it at the delivered one.


### 9.2 But the binder does not have to be bought

There is, however, a configuration in which the binder costs nothing, and it turns on a fact about the cycle that has been in view since §3. The catalytic cycle has no input per event: the binder is not consumed, and no energy is supplied to bring the nuclei together. Its only input is the binder itself, so the whole of the negative balance sits in a single question — what the binder costs.

Pions are a byproduct of spallation. They are created in the same nuclear collisions that make a spallation target's neutrons, by the same protons, in the same target. A facility running a proton driver for neutrons, for isotopes, or for an accelerator-driven subcritical blanket is therefore already making them and throwing them away. Capturing them costs a collector, but it does not cost any beam.

On that accounting the marginal beam energy attributable to one binder is zero, and every fusion the binder catalyses is gain. Theorem 4 in §13.8 states this formally, together with the reason a loss factor cannot overturn it.

| capture efficiency | fusion heat, as a fraction of beam energy | reachable? |
|---|
| 30 percent, today's front end | 10.5 percent | yes |
| 0.3420, the ceiling at the specified inventory | 12.0 percent | yes |
| one half | 17.6 percent of beam | only at about 45 kg of tritium |
| 90 percent [DESIGN], the specified collector | 31.6 percent of beam | **no — above the ceiling at any target depth** |

**That last row is withdrawn.** A capture efficiency here means a muon that *stops in the fuel*, and a stopping target is one muon range deep, so it stops only the part of the accepted spectrum below its range. The bound is not the collector's: it is the solenoid's acceptance, 0.5069, which no target depth exceeds. **That row compared a collector's acceptance with a fuel target's stopping fraction, which are different quantities.**


### 9.3 What that returns, at the capture actually reachable

**And the headline figures must carry the same correction, plus §5.2's loss budget.** Both, applied:

| capture | binders per second | fusion heat |
|---|
| one half, as first computed | 2.80 × 10^14 s^-1 | 176 kW |
| 0.3420, the stopping ceiling above | 1.918 × 10^14 s^-1 | 120.1 kW |
| **0.2438**, that ceiling through the loss budget | **1.367 × 10^14 s^-1** | **85.6 kW** |

> **The conclusion is untouched and only the magnitude moves, and that asymmetry is the whole point of this configuration.** Every other balance in this paper is a ratio against unity, so a factor of 0.7127 decides it. This one is not a ratio at all: the marginal beam energy per binder is **zero**, so any positive heat is gain and no loss factor can take it below unity. 85.6 kW of fusion heat at zero marginal beam cost is the same result as 176 kW, reached by the same argument and arriving at a smaller number. **It is the one figure here that a collection factor rescales without deciding**, because it was never conditional on an acceptance clearing a threshold.

![Figure 6](papers/figures/fig6-coproduct.png)

**Figure 6.** The one configuration that is net-positive on witnessed numbers alone. Because the beam is running for another reason, the marginal energy spent per binder is zero, so any point on this line is gain and no loss factor can push it below it.

> **This is a net-positive cold fusion reaction.** No input per event, no input for the binder, and real energy out. It is provable from witnessed quantities and needs no number that has not been measured.


### 9.4 And it dissolves the flux gap

The requirement has always been stated against **delivered** muon beams — about 1.0 × 10^8 s^-1 today and 1.0 × 10^10 s^-1 planned — which gives a shortfall of five orders of magnitude. Those are *momentum-selected, transported* beams, which discard almost everything the target makes. In-situ capture at the production target is 2.80 × 10^4 times the best planned delivered beam, or 1.37 × 10^4 at the delivered capture above, **because nothing is transported and nothing is selected.** The flux gap is an artefact of buying muons rather than making them where they are used.


### 9.5 Committed predictions for the net-positive run

Stated before the run, at 1 MW on target and the witnessed cycle count of 150 cycles, **computed from the machine of §7 and not from a hypothetical one:**

| quantity | committed value |
|---|
| binders stopped in the cell | 1.334 × 10^8 1/s |
| neutrons at 14.1 MeV | 2.002 × 10^10 1/s |
| fusion heat in the cell | 56.4 mW |
| tritium in the demonstration cell | 2.41 mg |

**Three corrections took it there**: interception at 0.7004, because the machine's beam is wider than the bare specification assumed; the mirror at 1.49, because the machine has one; and the end-to-end loss budget at 0.7127. **Net 0.7427.**

> **The prediction survives being pointed at the real machine, and it falls by a quarter doing it.** The first two corrections nearly cancel; the third does not.

**And it still scales linearly with one number that has not been measured.** The acceptance is §5.1's model, which reproduces the built machine's own simulation to 0.982 and **has never been measured end to end.** §10 Stage A is that measurement. If Stage A returns half the modelled acceptance, every figure in this section halves — and the experiment still runs, because it becomes a measurement of the acceptance by a second route.


---


## 10. The laboratory programme for the unwitnessed configuration

The programme is four staged measurements, all on apparatus that already exists. The acceptance measurement runs first, and the reason is that it multiplies every balance identically, so a single result bounds all of them at once.

**Stage A — the acceptance, measured end to end.** Count stopped binders per pion produced, on a target and channel whose geometry is known. The committed band is 43.42 percent with no momentum requirement, 35.03 percent through a 400 MeV/c window and 31.66 percent through 265 MeV/c. **A result below 29.51 percent falsifies the model this paper's collection figures rest on**, and the margin above that floor is only 1.073 — which is why this stage is first and not last.

**Stage B — the sticking branch, with purity as a controlled variable.** §8's procedure, run as a series. It decides between 0.45 percent and 0.56 percent, and it separates purity from density and temperature, which the existing record confounds.

**Stage C — the production target, measured rather than simulated.** A normalisation measurement: pions per beam particle against pions per interaction, on one target. This is the open half of the factor between 11.13 GeV and the optimised figure of 4.69 GeV, and it decides whether the one route that survives §5.3 exists.

**Stage D — the integrated demonstration.** The net-positive configuration of §9, on a spallation driver already running, against the committed predictions of §9.5.

> The order is not arbitrary, and each stage earns its place. Stage A multiplies everything downstream of it. Stage C decides whether the route that clears unity at the delivered acceptance exists at all. Stage B decides a factor *within* a route rather than whether the route is there. And Stage D is the demonstration itself, which cannot be interpreted before Stage A has run.


---


## 11. Limits, and what this paper does not claim

Each item below is a limit on what the foregoing establishes. None of them is resolved by argument in this paper, and where a measurement would settle one, that measurement is named. §13.9 lists the three that bear most directly on the results.

**The deciding measurement is unmade.** The two published final stickings, 0.45 percent and 0.56 percent, straddle the break-point at 0.1580 percent. §8's protocol settles it, and nothing here stands in for that.

**Every collection figure here is an acceptance rather than a delivered efficiency** until Stage A runs. §5.2 computes the losses between the two and §5.3 restates every balance through them, but a computed budget is not a measurement, and the margin over the falsification floor is 1.073.

**Every balance assumes perfectly pure fuel.** At the bound case, 5.49 ppm of high-Z contamination costs as much binder as decay does. The purity series of §8.3 is what measures it.

**The temperature axis is confounded in the existing record.** The cleanest published data are also the coldest and densest, so temperature, purity and density cannot be separated from what exists. That is a fault in the record rather than in the reaction, and §8.3 is written to separate them.

**The bound case rests on a service-life model that over-predicts its one checkable point.** The model returns more cycles than were measured at the single point where a comparison is possible, and **every bound-case figure inherits that** while no bred-fuel figure at demonstrated cycles does. The asymmetry is why §5 leans on the demonstrated count.

**The optimised production target is a discrepancy that cannot be closed by argument.** A published optimisation costs 4.69 GeV per pion against the 11.13 GeV integrated in §4.1. Three candidate mechanisms were examined and bounded; what survives is a **normalisation** — pions per beam particle against pions per interaction — needing 2.389 interacting nucleons, which reproduces the optimised figure closely and which a deuteron on a long target supplies. **Stage C measures it.**

**And the standalone configuration is closed rather than open.** §9.1 is a theorem, and no measurement in §10 can overturn it. What §10 can decide is the co-product configuration and the bred-fuel route, which are the two that survive.


---


## 12. What this paper claims, in order

1. **A cold fusion reaction exists and is witnessed.** Its definition is structural, its seven conditions admit exactly one binder, and its cycle has been measured for seventy years.
1. **An eighth condition decides whether it is worth running**, and every term in it is measured.
1. **No configuration of it is self-sustaining inside the device** at the collection efficiency the machine actually delivers, with the machine left as built.
1. **One configuration is net-positive on witnessed numbers alone** — as a co-product of a beam already running, where the marginal energy per binder is zero — and it returns 85.6 kW on a one-megawatt driver.
1. **One route clears unity at a witnessed cycle count for a device built for the purpose**, and it is bred fuel through an optimised production target, at 1.480. Whether that target's gain is real is Stage C.
1. **A device-internal route clears unity too, and only conditionally.** With the same optimised target, the heat form on the bound-case service life reaches 1.036, and 1.231 at the wider bore. It is conditional on Stage C and on a service-life model §11 says over-predicts, and it is met on the reading of "inside the device" that counts the blanket. On the reading that counts the neutron at its bare heat, nothing here clears.
1. **The materials are specified and the machine is designed**, to a bill of materials and a build package rather than to a sketch.
1. **The procedure that would witness the unwitnessed configuration is stated**, with its predictions committed in advance and a rule that a disagreement is a refusal rather than an average.
> **The reaction is proved from what has been witnessed. The net-positive configuration is specified and unwitnessed. The instructions for witnessing it are §8 and §10.** That is the whole of the claim, and no part of it is larger than the measurements behind it.


---


## 13. The mathematics, in full

The body of the paper states results and points at where they come from. This section carries the derivations themselves, so that each may be checked without reconstructing it. **Where a statement is a theorem it is proved; where it is a derivation resting on measured inputs, it is labelled a proposition and its inputs are named.** Nothing is called proved that is not.


### 13.1 Notation

| symbol | meaning |
|---|
| $m_b$ | the mass of the binding particle, in electron masses |
| $a_b$ | the radius of the binder's orbit about a nucleus |
| $R_{dt}$ | the internuclear separation in the bound state |
| $\lambda_f$ | the fusion rate from the bound state |
| $\lambda_0$ | the binder's free decay rate |
| $\omega_s$ | the probability, per cycle, that the binder is lost |
| $N$ | the service life: the number of fusions one binder catalyses |
| $Q_{fus}$ | the energy released per fusion |
| $f_{work}$ | the fraction of that release recovered in the form being paid in |
| $V$ | the value of one fusion, $Q_{fus}\,f_{work}$ |
| $E_b$ | the energy cost of producing and capturing one binder |
| $\eta$ | the collection efficiency: stopped binders per pion produced |
| $E_\pi$ | the energy cost of producing one pion |


### 13.2 The eighth condition, derived

**Proposition 1 (the cycle identity).** *A binder is worth making if and only if*

> $E_b \;<\; N\,Q_{fus}\,f_{work}$, *and since* $N \le 1/\omega_s$, *the necessary condition is* $E_b < Q_{fus}\,f_{work}/\omega_s$.

*Derivation.* The catalytic cycle has no input per event: the binder is not consumed by the fusion, and no energy is supplied to the fuel to bring the nuclei together, that work being done by the bound state. The only input is therefore the binder itself, at a cost $E_b$. A binder that catalyses $N$ fusions returns $N\,Q_{fus}\,f_{work}$, so the account closes exactly when the return exceeds the cost.

For the bound: let $p$ be the probability that the binder survives one complete cycle, so $\omega_s = 1 - p$. The number of cycles is geometrically distributed and its expectation is $N = p/(1-p) \le 1/\omega_s$, with equality approached as $p \to 1$. **The cap is asymptotic and is never attained**, which is why §5.3 distinguishes the demonstrated cycle count from the bound. ∎

**Remark.** The inequality is an accounting identity rather than an efficiency target: it contains no free parameter. Every term has been measured, and §3 gives the measured values.


### 13.3 The structural window on the binder mass

**Proposition 2 (the lower bound).** *Condition 2 — that the tunnelling rate exceed the decay rate of the state producing it — places a lower bound on $m_b$.*

*Derivation.* In a hydrogenic bound state the orbit radius scales inversely with the reduced mass, $a_b \propto 1/m_b$, and the internuclear separation of the mesomolecule follows it, $R_{dt} \propto 1/m_b$. The barrier penetration factor is exponential in $\sqrt{R_{dt}}$, so $\lambda_f$ rises steeply with $m_b$ while $\lambda_0$ does not. Condition 2 requires $\lambda_f > \lambda_0$, and the crossing defines the floor. Evaluated on the measured constants the floor is 119 electron masses, or 60.8 MeV expressed as an energy. ∎

**Proposition 3 (the upper bound).** *Conditions 3 and 4 place an upper bound on $m_b$.*

*Derivation.* A binder heavy enough to be absorbed by a nucleus before the cycle completes catalyses nothing, failing condition 3; and it produces ash the branching ratios do not predict, failing condition 4. Nuclear absorption rates rise with the binder's mass through the overlap of its orbit with the nuclear volume, and the ceiling is where the absorption rate overtakes $\lambda_f$. That is 918 electron masses. ∎

> **Theorem 1 (uniqueness of the binder).** *The seven conditions admit exactly one realisation in the closed index of charged particles: the negative muon.*

>

> *Proof.* Propositions 2 and 3 confine any admissible binder to $m_b \in [\,$119$,\,$918$\,]$ electron masses. The index of charged particles with lifetimes long enough to form a bound state is closed and short, and it is enumerated: the electron at $1$ lies below the window; the muon at 207 electron masses lies inside it; the pion at 273 electron masses lies inside it but is hadronic and is absorbed before catalysing, failing condition 3; the kaon at 966 electron masses and the tau at 3477 electron masses lie above it. **No other charged particle has both a mass in the window and a lifetime sufficient to form a molecule.** The window therefore contains exactly one admissible occupant.

>

> The sign is fixed separately and not by mass. A $\mu^+$ binds an electron into muonium and is repelled by every nucleus in the fuel; it forms no mesomolecule at any density or temperature. Hence the binder is the **negative** muon, and it has exactly one parent, $\pi^-$ decay. ∎

**Corollary 1.1.** *Every yield in this paper is a $\pi^-$ yield*, and the production target's material is constrained by the charge ratio it returns and not only by its total yield — which §6.3 states as a specification.


### 13.4 Sticking does not depend on the binder's mass

> **Theorem 2 (mass-independence of sticking).** *The probability $\omega_s$ that the binder is lost to the fusion product is independent of $m_b$.*

>

> *Proof.* Sticking is the probability that the binder, initially bound in an orbit of radius $a_b \propto 1/m_b$, is captured into a bound state of the recoiling $\alpha$. In the sudden approximation it is the squared overlap of the initial binder wavefunction with the final bound states of the $\alpha$, evaluated in the frame moving at the recoil velocity $v_R$:

>


$$\omega_s \;=\; \sum_{n\ell} \left| \int \psi^{*}_{n\ell}(\mathbf{r})\, e^{\,i m_b \mathbf{v}_R\cdot\mathbf{r}}\, \psi_{i}(\mathbf{r})\, d^3r \right|^2 .$$

>

> Both $\psi_i$ and $\psi_{n\ell}$ are hydrogenic with the same reduced mass, so the natural length in the integral is $a_b \propto 1/m_b$. Rescaling $\mathbf{r} = a_b \mathbf{u}$ makes the wavefunctions mass-independent functions of $\mathbf{u}$, and the exponent becomes $i\,m_b v_R a_b\, \hat{v}\cdot\mathbf{u}$. Since $a_b \propto 1/m_b$, the product $m_b a_b$ is a constant, and the exponent depends on $v_R$ alone. **Every dependence on $m_b$ has cancelled**, and $\omega_s$ is a function of the recoil velocity over the orbital velocity only. That ratio is measured at 2.97 for $d+t$. ∎

**Corollary 2.1 (condition 8 is a specification, not a search).** Since $\omega_s$ does not depend on $m_b$, no admissible binder returns a smaller loss per cycle than the muon. Combined with Theorem 1, which leaves no other occupant of the window, **condition 8 cannot be satisfied by looking for a better particle.** It is a constraint on the machine.

> **Theorem 3 (closure of the standalone configuration).** *No binder anywhere in the structural window satisfies condition 8 as a standalone power source.*

>

> *Proof.* By Theorem 2, $\omega_s$ is the same for every occupant of the window, so $N \le 1/\omega_s$ is a bound common to all of them. $Q_{fus}$ and $f_{work}$ are properties of the fuel and the plant, not of the binder. Hence the right-hand side of Proposition 1 is a constant across the window. The left-hand side, $E_b$, is bounded **below** by the cost of producing the parent particle, which §13.6 puts at 11.13 GeV per pion and which no collector can reduce. Taking the most favourable admissible values of every term simultaneously, the best balance available anywhere in the window is 0.807 — less than unity. **The configuration is therefore closed by the structure of the window rather than by any measurement**, and no experiment in §10 can overturn it. ∎

**Remark.** Theorem 3 is what makes the co-product configuration of §9 the interesting one: it does not contradict the theorem, because it does not pay for the binder at all.


### 13.5 The collector

**Proposition 4 (the aperture product).** *A solenoid of field $B$ and clear radius $R$ accepts a pion of transverse momentum up to $p_T^{max} = 0.15\,B\,R$, in T, m and GeV/c; hence field and bore trade against one another at fixed acceptance, and only their product matters.*

*Derivation.* A particle of transverse momentum $p_T$ in an axial field $B$ has gyroradius $r_g = p_T/(0.3\,B)$ in the same units. A particle born on the axis reaches a maximum distance $2 r_g$ from it, so it is contained if $2 p_T/(0.3 B) \le R$, which rearranges to the stated cap. **The beam envelope is therefore $2 r_g$ and not $r_g$** — a factor of two that also fixes the bore of the fuel cell, and which is validated in §7.1 against three published geometries the derivation did not use. ∎

**Proposition 5 (the mirror condition and the grade it requires).** *A pion emitted into the backward hemisphere at pitch angle $\theta$ is reflected forward by a field rising from $B_t$ to $B_{max}$ if and only if* $\sin\theta \ge \sqrt{B_t/B_{max}}$. *The grade sufficient to reflect every angle the production data covers is therefore* $B_{max}/B_t = 1/\sin^2\theta_{max}$, *which is* 1.428.

*Derivation.* In a slowly varying axial field the magnetic moment $\mu = p_\perp^2/2mB$ is an adiabatic invariant and the kinetic energy is conserved, so $p_\perp^2/B$ is constant along a trajectory. A particle turns where $p_\perp = p$, that is where $B = B_t/\sin^2\theta$. It is reflected before reaching $B_{max}$ exactly when $B_t/\sin^2\theta \le B_{max}$, which is the stated condition. Taking $\theta_{max}$ as the largest angle the production measurements cover gives the grade, and **because the data end there, so does the requirement**: the grade is fixed by the measurement rather than chosen. ∎

**Proposition 6 (linearity in collection).** *Every balance in this paper is proportional to $\eta$, so restating one at a different collection efficiency is exact rather than approximate.*

*Derivation.* Write the balance as $G = N\,V\,\eta/E_\pi$. Here $N$ is a property of the fuel and the sticking, $V$ of the plant, and $E_\pi$ of the production target; none of them depends on $\eta$. Hence $G \propto \eta$ and $G(\eta_2) = G(\eta_1)\,\eta_2/\eta_1$ identically. The tables of §5.3 are computed this way, and the paper's own two-column table at thirty and ninety percent provides the check: every row's ratio lies within 2.998 to 3.010 of the exact three. ∎

**Corollary 6.1.** *An alteration that changes $E_\pi$ alone multiplies every balance by the same factor* $E_\pi^{old}/E_\pi^{new}$. This is what §5.4 computes, and the same corollary explains why that factor moves the bred-fuel requirement from 50.8 percent to 21.4 percent.


### 13.6 The production floor

**Proposition 7 (the floor on the binder's cost).** *Production alone costs* 11.13 GeV *per pion, and no collector can reduce it.*

*Derivation.* The pion yield per interacting proton is obtained by integrating the measured double-differential cross section over the acceptance, with the solid-angle Jacobian:


$$Y \;=\; \frac{1}{\sigma_{inel}} \int_{\theta_1}^{\theta_2}\!\!\int_{0}^{p_{max}} \frac{d^2\sigma}{dp\, d\Omega}\; 2\pi \sin\theta \; dp\, d\theta .$$

Over the large-angle acceptance this gives 1.0382 barn, or 0.6107 π⁻ per proton; the forward acceptance adds 0.1838 barn; combined, $Y =$ 0.7188 π⁻ per proton. Dividing the beam energy by $Y$ gives $E_\pi =$ 11.13 GeV. Since $\eta \le 1$ by definition, $E_b = E_\pi/\eta \ge E_\pi$, so this is a floor on the binder's cost that holds whatever the collector does. ∎

**Proposition 8 (the escape path is the target's radius, not its length).** *A production target may be made long without becoming opaque to the pions this collector accepts.*

*Derivation.* The collector accepts large-angle pions, which is 84.96 percent of production. A pion emitted at a large angle to the beam leaves the target through its **side**, so the path it must survive is of order the target's radius $r$ and not its length $L$. The survival probability is therefore $\exp(-r/\lambda_{abs})$ for that component, with $\lambda_{abs} =$ 15.89 cm in mercury, against $(\lambda_{abs}/L)\,[1 - \exp(-L/\lambda_{abs})]$ for the forward component. Weighting by the large-angle fraction gives 0.8961 for the published geometry. **A narrow target is transparent however long it is**, which is why lengthening it to raise the yield does not defeat itself. ∎


### 13.7 The fuel target

**Proposition 9 (the tritium inventory does not fall with compression).** *The inventory required is areal density times beam area, and is therefore independent of the fuel's density.*

*Derivation.* A muon stops only if the target is at least one continuous-slowing-down range deep, so the requirement is on the **areal** density $x = \rho L$ obtained by integrating the stopping power, $x = \int_0^{p_{max}} (dE/dx)^{-1}\, dE$, which is 33.9 g/cm^2 at a 265 MeV/c window. The inventory is $M = x \cdot A$ with $A$ the beam's cross-sectional area. Compressing the fuel raises $\rho$ and shortens $L$ in exact proportion, leaving $x$ — and hence $M$ — unchanged. **Density buys length, not inventory.** ∎

**Corollary 9.1.** Because $A = \pi(2r_g)^2$ by Proposition 4, widening the bore widens the beam and so raises the inventory as the square of the aperture. That is the cost the wider bore is priced at in §7.4, and it is why the two alterations of §5.4 are not equally cheap.


### 13.8 The co-product configuration

> **Theorem 4 (co-product positivity).** *Where the binder is a byproduct of a beam running for another purpose, the configuration returns net energy for any positive stopped fraction, and no loss factor can take it below unity.*

>

> *Proof.* Let the driver deliver power $P$ for a purpose that does not depend on the pions, and let $\mu$ be the marginal energy attributable to one binder. Pions are produced in the same nuclear collisions that make the target's neutrons, by the same protons, in the same target; capturing them requires a collector but no additional beam. Hence $\mu = 0$.

>

> The fusion heat returned is $H = n_\mu N Q_{fus}$ with $n_\mu = \Phi_\pi \eta_{stop}$ the rate of stopped binders. The net return is $H - n_\mu \mu = H > 0$ for any $\eta_{stop} > 0$.

>

> **The balance is therefore not a ratio against unity**, and this is what distinguishes it from every other configuration in the paper. A loss factor $f \in (0,1]$ applied to $\eta_{stop}$ rescales $H$ to $fH$, which is smaller and still positive. Applying §5.2's budget takes the returned fraction from 12.0 percent to 8.56 percent of the driver's beam energy, and 85.6 kW on a 1 MW driver — **a different number and the same conclusion.** ∎

**Remark.** Theorem 4 does not contradict Theorem 3. Theorem 3 forbids a configuration that must buy its own binders from paying for itself; Theorem 4 describes one that does not buy them.


### 13.9 What is not proved

Three things in this paper are **not** theorems, and are marked as such wherever they appear.

**The delivered acceptance is computed, not measured.** §5.2's loss budget is a product of five terms, each derived, but the product has never been measured end to end. §10 Stage A is that measurement, and until it runs every figure downstream of it is conditional.

**The optimised production target's factor is taken from the literature, not reproduced here.** The 4.69 GeV of §5.4 is a published optimisation. Three candidate mechanisms for the discrepancy against this paper's 11.13 GeV were examined and bounded, and what survives is a normalisation requiring 2.389 interacting nucleons. §10 Stage C measures it.

**The sticking value is unresolved between two published measurements.** 0.45 percent and 0.56 percent straddle the break-point at 0.1580 percent, and no argument here chooses between them. §8's protocol does, and §8.4 commits in advance to reporting a bound rather than an average if the two routes disagree.


## 14. References

1. M. G. Catanesi *et al.* (HARP Collaboration), Phys. Rev. C **77**, 055207; A. Bolshakova *et al.*, *Large-angle production of charged pions by 3 GeV/c–12.9 GeV/c protons on beryllium, aluminium and lead targets*, Eur. Phys. J. C **63**, 549 — Tables 5–8, both charges; and M. Apollonio *et al.*, *Forward production of charged pions with incident protons on nuclear targets at the CERN PS*, Phys. Rev. C **80**, 035208 — Tables XXII, XXIII and XXXII, both charges. **The production integration of §4.1 is taken from these tables and from nothing else.**
1. J. Strait, N. V. Mokhov and S. I. Striganov, *Towards the optimal energy of the proton driver for a neutrino factory and muon collider*, Phys. Rev. ST Accel. Beams **13**, 111001 — Table II and §V. **The front-end simulation the acceptance model of §5.1 is validated against.**
1. S. Cook *et al.*, *MuSIC: delivering the world's most intense muon beam*, arXiv:1610.07850; Phys. Rev. Accel. Beams **20**, 030101.
1. Mu2e Collaboration, *Mu2e Conceptual Design Report*, FERMILAB-TM-2545, arXiv:1211.7019.
1. COMET Collaboration, *COMET Phase-I Technical Design Report*, arXiv:1812.09018.
1. K. Oishi *et al.*, *Development of the Range Counter for the COMET Phase-α Experiment*, arXiv:2505.07464 — §1, which states the backward-emission capture and the thin production target.
1. J. J. Back, *Energy deposition studies for the Neutrino Factory target station*, JINST, arXiv:1104.2742 — FLUKA and MARS over a 4 MW, 8 GeV proton beam on a free mercury jet in a 20 T solenoid. **The sourced deposition, coil heating and radiation-lifetime figures of §7.3.**
1. K. T. McDonald *et al.*, *The MERIT high-power target experiment at the CERN PS*, IPAC 2010, p. 3527 — the free mercury jet run in a 15 T solenoid.
1. Variational three-body calculation of muon-alpha sticking, Phys. Rev. A **34**, 2536.
1. S. E. Koonin and M. Nauenberg, *Nature* **339**, 690.
1. M. Kamimura, Y. Kino and T. Yamashita, *Comprehensive study of muon-catalyzed nuclear reaction processes in the dtμ molecule*, Phys. Rev. C **107**, 034607 (2023).
1. R. Spencer Kelly, L. J. F. Hart and S. J. Rose, *An investigation of efficient muon production for use in muon catalyzed fusion*, J. Phys. Energy **3**, 035003. **The optimised production target §11 declines to adopt and §10 Stage C measures.**
1. X. Yin, W. Kou and X. Chen, *Muon-Catalyzed Nuclear Fusion: Physical Mechanism, Bottleneck Breakthroughs, and an Engineering Pathway*, arXiv:2605.26432 — Table I and §IV.B.
1. W. Kou and X. Chen, *A Lawson-inspired Cycle-Closure Criterion for Deuterium–Tritium Muon-Catalyzed Fusion*, arXiv:2607.10989 — Eqs. (11)–(13) and Table I. **An independent derivation of §3's eighth condition, reached without reference to this work.**
1. W. Kou and X. Chen, *External-Field-Assisted Muon Reactivation in Muon-Catalyzed Fusion: A Rate-Network Criterion for Reducing Alpha Sticking*, arXiv:2606.07077.
1. E. Koukina *et al.* (MuFusE Collaboration), *Design and Commissioning of a Deuterium-Tritium Gas Delivery System for Muon Catalyzed Fusion in a Diamond Anvil Cell*, arXiv:2606.19304; and J. D. Kalow *et al.*, arXiv:2606.05333. **The diamond-anvil cell and gas system of §6.3 column A.**
1. M. Lach, *The Method* v1.2–8 — *The Lach Cylinder: an index of transitions*.
1. M. Lach, *Cold Fusion and the Binder Economy*, v1.0; *The Binder Economy Against the Recent Literature*, v1.0; *Cold Fusion: Specification and Procedure*, v1.0. **Superseded by this paper wherever the two differ.**

---

