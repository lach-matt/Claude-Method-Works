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

A second correction goes with it, and it is larger. Every balance previously reported at a modelled "bound case" service life was computed at an effective sticking of 0.1487 percent [WITHDRAWN] — a value formed from two different states of the mesomolecule, and superseded by the record's own measurements. At the corrected value the same conditions return 190.1 cycles rather than 588.9, so **every bound-case figure ever reported here is high by 3.10**. The figures computed at the **measured** 150 cycles are untouched, because they never used the model, and that asymmetry decides the result.

**What it decides is that no heat form and no work form is self-sustaining.** The largest either reaches is 0.513, and only by granting the optimised production target, a wider bore, a wider stopping window and a fuel density never held, all at once. **Every device-internal figure above unity in the record is withdrawn**: each was the superseded sticking and nothing else.

**Two configurations survive, and they are different claims.** Priced as **bred fuel**, at the measured 150 cycles per binder — with no service-life model, no density above the one already reached and no choice between the two sticking measurements — the balance is 0.623 with the machine as built, **0.957** with both collector alterations and **1.480** through an optimised production target. It asks for less than anything else here, and its product leaves the device as fuel.

**And a self-sustaining power source is specified rather than merely sought.** Setting the balance to unity and solving for each term shows that two of the four are closed above by physics rather than by engineering — the service life at 198 cycles by the sticking, the collection at unity because it is a fraction — so the question reduces entirely to what one fusion is worth. It must be worth 152.7 MeV, or 64.3 MeV with the optimised target. No non-fissioning blanket supplies that; a **subcritical** blanket driven by the same neutrons supplies it at a multiplication factor between 0.469 and 0.770, against 0.95 for an accelerator-driven system and unity for a power reactor. **The energy is then heat, recovered on site, with nothing leaving the device** — the fusion supplying 27.4 percent of it and every one of the neutrons. That is a fusion-driven subcritical fission reactor and not a fusion power plant, and the paper says so where it says the rest. **Neither configuration has been assembled**; §6 to §9 specify them and §10 measures what is still open.

One configuration is net-positive on witnessed numbers alone, and it is not the standalone one. Pions are a byproduct of spallation, made in the same collisions that produce a spallation target's neutrons, so a facility already running a proton driver for neutrons or isotopes is making binders and discarding them. The marginal beam energy per binder is then **zero**, and any positive heat is gain. At the reachable capture of 0.2438, that comes to 85.6 kW of fusion heat on a one-megawatt driver. It is the one result here that a loss factor rescales without deciding, because it was never a ratio against unity in the first place.

Finally, the materials are specified to the last free parameter, the machine that supplies the binders is designed as a build package rather than sketched, and the laboratory programme is set out as four staged measurements on apparatus that already exists — the acceptance measurement first, because it multiplies every balance identically and so bounds all of them at once.


---


## 1. The definition, and the seven conditions

We take a cold fusion reaction to be **a nuclear fusion event in which the approach to nuclear separation is supplied by molecular binding geometry rather than by kinetic energy.** The definition is structural rather than thermal. It makes no claim that the reaction runs near room temperature; it says only that the work of bringing two nuclei within tunnelling range is done by a bound state instead of by a collision, and that distinction is what the rest of the paper turns on.

**Two things the term is not being used to mean.** It is not being used for the electrochemical claims of the late nineteen-eighties, which asserted an unexplained nuclear yield from a metal lattice and which nothing here bears on, supports or revisits. And it is not a new name for a new effect: the reaction the definition picks out is muon-catalysed fusion, a laboratory phenomenon since the nineteen-fifties, and §2 shows that the definition picks out that and nothing else. The word is used because the definition is a structural one and the reaction satisfies it — the approach really is done by binding rather than by heat — and a reader who prefers the field's own name for it will lose nothing by substituting it throughout.

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
|---|---|
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

It cannot, however, be improved by changing the binder, and the reason is that the binder's mass cancels out of the overlap integral that defines sticking. A heavier binder sits in a tighter orbit, but the momentum scale of that orbit rises in exact compensation, and the two changes cancel in the one combination the capture depends on. The recoil the binder must escape is set by the fusion kinematics and does not involve the binder at all. Theorem 2 in §13.4 gives the proof.

The consequence is larger than the calculation. Since no admissible binder does better, condition 8 cannot be satisfied by looking for a different particle; it is a specification on the *machine* rather than a search over the *spectrum*. And §2's window has already shown that there is no other occupant to search for in any case.

**The measured values then decide the heat form, and they decide it against.** At the production cost §4.1 measures, the heat form of condition 8 would be met at perfect collection only if the sticking were below 0.1580 percent. The two published final stickings — 0.45 percent from SIN and 0.56 percent from PSI — are both well above that, and so are the two effective values, 0.5050 percent and 0.5320 percent, that the measured reactivation returns. **The break-point does not lie between the two readings; it lies below both.** The heat form reaches 0.31 of what it needs on the more favourable of them and is short by a factor of 3.37 on the other, and no choice between them repairs it.

The consequence is worth drawing out, because it redirects the whole enquiry. If the two readings had straddled the break-point, a single bench measurement would have decided whether the reaction can pay for itself as heat. They do not, so it cannot. What the two readings differ about is a few percent of the service life; what decides the balance is the cost of the binder and the fraction of them collected — which is where §4 and §5 go, and why §10 measures the acceptance first. §8's protocol still runs, because the two routes to sticking disagreed historically and the operative value is worth pinning, but it settles a term rather than the question.


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
|---|---|---|---|
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
|---|---|---|
| escape from the production target | 0.8961 | large-angle pions leave sideways, so the escape path is the target's radius |
| pion decay completeness | 0.9000 | the fraction of accepted pions decaying inside the channel |
| muon survival in the channel | 0.9796 | against the muon decay length |
| scattering out of the transverse cap | 0.9021 | conservative: the whole kick taken off the cap |
| adiabatic transport | 1.000 [DESIGN] | unity **by design**, conditional on the bore schedule |
| **product** | **0.7127** |  |

**The delivered acceptance is therefore 31.66 percent** at today's aperture, or 37.62 percent at the wider bore — against the 90 percent [DESIGN] the balances were read at.

![Figure 5](papers/figures/fig5-budget.png)

**Figure 5.** What becomes of a hundred pions made in the target. Each step is a loss that can be computed rather than assumed, and the product of them is the difference between what the magnet accepts and what the fuel actually stops.


### 5.3 Every balance, at the acceptance delivered and the sticking the record supports

Two corrections stand between the figures the preprints at [18] printed and the ones below, and it is worth taking them in order because the second is the larger.

**The first is the acceptance**, and §5.2 has just made it. The second is the **service life**, and it comes from the preprints' own later sections rather than from anything new here. Every balance printed there was computed at one of two service lives: the **measured** 150 cycles per binder, and a modelled "bound case". Reading the printed table backwards through the balance — Proposition 1 in §13.2 fixes its form, and the table's own columns check it — the bound case is 588.9 cycles. That is the model run at an effective sticking of 0.1487 percent [WITHDRAWN], a value formed by multiplying an excited-state initial sticking by a survival fraction measured on the **ground** state — two different states. Fusion occurs from the ground state, and the record's own measured values are 0.5050 percent and 0.5320 percent; at the favourable one the same density returns 190.1 cycles instead of 588.9. **Every bound-case figure in the record is therefore high by 3.10.**

> **The rows computed at the measured cycle count are untouched by that**, because they never used the model at all — and that asymmetry, more than any other single fact in this paper, decides which route survives.

Restating is exact rather than approximate: the balance is linear in collection (Proposition 6 in §13.5) and proportional to the service life, so each cell below is one multiplication. The left column is the machine as built; the right is the same machine with both collector alterations of §5.4 — the wider bore and the wider stopping window — which together deliver 48.61 percent.

| balance | delivered, as built, 31.66 percent | with both collector alterations, 48.61 percent |
|---|---|---|
| heat, at the measured 150 cycles | 0.111 | 0.171 |
| heat, the model at 8.5 × liquid | 0.141 | 0.216 |
| heat, the model at φ = 3 | 0.131 | 0.201 |
| work, at the measured 150 cycles | 0.083 | 0.128 |
| work, the model at 8.5 × liquid | 0.106 | 0.162 |
| **bred fuel, at the measured 150 cycles** | 0.623 | **0.957** |
| bred fuel, the model at 8.5 × liquid | 0.790 | 1.212 |

> **Nothing clears unity with the machine as built**, and the closest is bred fuel at the measured cycle count, at 0.623. **With both collector alterations that route reaches 0.957** — short of unity by 1.045, and short of it by no other term than the loss budget, which is the one quantity in the whole column that has never been measured. The figures reported at ninety percent collection in the preprints at [18] are withdrawn as end-to-end results, and so are the bound-case figures that rest on the superseded sticking. Each stands as the conditional it was stated at.

![Figure 5](papers/figures/fig5-budget.png)

**Figure 5.** What becomes of a hundred pions made in the target. Each step is a loss that can be computed rather than assumed, and the product of them is the difference between what the magnet accepts and what the fuel actually stops.


### 5.4 What the specified alterations do to every balance

§5.3 states the balances at the production cost §4.1 measures. A third alteration is specified in this paper — an **optimised production target** — and unlike the two collector alterations it does not change the collection at all. It moves `E_binder`, and because a balance has the form `N · V · η / E_binder` it therefore multiplies **every** balance by the same factor: from 11.13 GeV to 4.69 GeV, which is worth 2.373. Corollary 6.1 in §13.5 makes this explicit.

> **The factor checks against the requirement it moves.** §4.2 puts bred fuel at the measured cycle count at 50.8 percent collection; through the optimised target that requirement is 21.4 percent, and 50.8 ÷ 2.373 returns it.

| balance, through the optimised target | delivered, as built | with both collector alterations |
|---|---|---|
| heat, at the measured 150 cycles | 0.264 | 0.405 |
| heat, the model at 8.5 × liquid | 0.334 | **0.513** |
| work, at the measured 150 cycles | 0.198 | 0.304 |
| work, the model at 8.5 × liquid | 0.251 | 0.385 |
| **bred fuel, at the measured 150 cycles** | **1.480** | **2.271** |
| bred fuel, the model at 8.5 × liquid | 1.874 | 2.877 |

![Figure 4](papers/figures/fig4-range.png)

**Figure 4.** The range the reaction is expected to fall in. Each row is one way of pricing the same reaction; the bar runs from what the machine as built delivers to what it delivers with all three alterations. Anything reaching the line at unity pays for itself. Only bred fuel does, and the rows at the measured cycle count use no service-life model at all.

**Two things fall out of that table, and they point in opposite directions.**

> **No heat form and no work form clears unity anywhere in this paper.** The largest either reaches is **0.513**, and it is reached only by granting, simultaneously, the optimised production target, the wider bore, the wider stopping window *and* a fuel density of 8.5 × liquid that no experiment has held. **A device that returns its energy as heat or as work is not self-sustaining on anything this paper can construct**, and that is a closed statement rather than an open question: §9.1 shows the same thing from the other direction, as a theorem. **Bred fuel at the measured cycle count clears unity, and it asks for the least of anything here.** At 1.480 with the target alone and **2.271** with all three alterations, it uses **no service-life model, no density above the one already reached, and no choice between the two sticking measurements**. Its inputs are the 150 cycles measured at Los Alamos, the sourced blanket of §4.2, the production cost integrated from measured cross sections in §4.1, and the collection the machine of §7 delivers. **That is the configuration this paper offers as self-sustaining and unwitnessed**, and §12 states exactly which of its terms have been measured and which have not.

**One condition travels with it and is not yet discharged.** 4.69 GeV is a published optimisation of the production target. This paper prices what it is worth without adopting it as a figure of its own, and §10 Stage C is the measurement that would settle it. Without it the same route reaches 0.957 — which is 1.045 short, and short by less than the uncertainty on the one term in it nobody has measured.


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
|---|---|---|
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
|---|---|
| neutrons at 14.1 MeV | fusion events, hence cycles per binder |
| the muonic-helium K-alpha at 8.2 keV | binders stuck to the alpha, hence the sticking directly |

![Figure 7](papers/figures/fig7-measurement.png)

**Figure 7.** The step the existing experiments do not take. Both observables watch the same fuel at the same time, on one fill, so the cycle count and the loss are measured together rather than inferred from separate runs.

**They share no instrument and no calibration**, which is what makes them two routes rather than one. §8.4 commits in advance to treating a disagreement between them as a **refusal** rather than as an average, and §9.3 applies the same rule to the two routes that read a subcritical `k`.


### 6.3 Bill of materials

Column A witnesses the reaction. Column B is the reactor-scale target the balance is computed against, given so the two are never confused.

| item | A — bench demonstration | B — reactor scale |
|---|---|---|
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
| blanket, as a **breeder** | none | ⁶Li-bearing, 1.6 neutron energy multiplication, fission-suppressed |
| blanket, as a **power source** | none | the same, **fission-permitting**: fissile or fertile loading to `k` = 0.469 – 0.770 — §9.2 |
| reactivity instrumentation | none | pulsed neutron source, source-jerk drive and a correlation channel, per §9.3 |

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
|---|---|---|
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
|---|---|---|
| cycles per binder | of order 150 cycles, ceiling 198 cycles | the service life, and whether the sticking cap is real |
| effective sticking, X-ray route | 0.5050 percent to 0.5320 percent | the operative loss term |
| effective sticking, neutron route | the same, within error | **if the two disagree, report a bound — do not average** |
| purity dependence | binder loss rising linearly in high-Z contamination | separates purity from temperature and density |
| temperature dependence | cycle rate rising toward 800 K, then flat | tests the ceiling that transfer imposes |

**A null at any step is a bound.** A cycle count below 150 cycles bounds the service life from above. A disagreement between the two sticking routes is a refusal, and the correct output is an interval. An absent purity dependence means the impurity channel is smaller than modelled, and every balance in §5 improves by a stated factor.


---


## 9. The net-positive configuration


### 9.1 The standalone case is closed by theorem, not by measurement

Considered as a purpose in itself, the reaction cannot pay for its own binders, and this is a theorem rather than an empirical result. Taking the most favourable admissible value of every term at once, the best balance available to the binder the window admits is 0.807 — short of unity. And because sticking does not depend on the binder's mass (§3.1), a different occupant of the window would not improve on it: there is no particle left to look for and no collector that can be built to change it. Theorem 3 in §13.4 gives the proof.

**That theorem is about the binder paying for itself as a power source**, and §5.3 has shown the same thing from the arithmetic: no heat form and no work form reaches unity at the delivered acceptance under any alteration specified here. What §5.3 also shows is where the closure stops — priced as bred fuel rather than as heat, the same reaction on the same measured cycle count does clear it. §9.2 gives the other configuration the theorem does not close, and for the same structural reason: it does not buy its binders at all.


### 9.2 The self-sustaining power source, solved rather than reported

§5 states what each configuration returns. It does not state what a **self-sustaining power source** would have to be, and those are different questions: the first has an answer of the form *this one fails*, and the second has an answer of the form *this is what one looks like*. The project asked for the second. This section sets the balance to unity and solves it.

The balance has four terms — `G = N · V · η / E_binder` — and they are not alike. **Two of them are bounded above by something no engineering moves.** The service life is capped at 198 cycles by the sticking (Proposition 1 in §13.2), and the collection is a fraction, so it cannot exceed one. **The other two are bounded by nothing proved anywhere in this paper.** Solving for each in turn, with the others held at the best configuration §5.3 reaches:

| term | what unity requires | against | verdict |
|---|---|---|---|
| service life `N` | 878.7 cycles | a cap of 198 cycles | **forbidden**, by 4.44 |
| collection `η` | 284.7 percent | a fraction cannot exceed unity | **forbidden** |
| production cost `E_binder` | 1.900 GeV per pion | 11.13 GeV measured, 4.69 GeV optimised | open |
| **value per fusion `V`** | **152.7 MeV** | 26.06 MeV from the sourced blanket | **open** |

> **So a self-sustaining power source is a statement about what a fusion is worth, and about nothing else.** Two of the four axes are closed by the physics, and of the two that remain the production cost cannot carry the requirement alone — 1.900 GeV is below even the optimised 4.69 GeV. The question is therefore entirely: **can a blanket return 152.7 MeV per fusion?**

**A non-fissioning blanket cannot, and this paper has said so.** Returning the alpha, the neutron's energy and the exothermic ⁶Li breeding, less the multiplier's endotherm, gives the 26.06 MeV of §4.2. No arrangement of (n,2n) multipliers approaches the requirement. That much of the preprint at [20] §5.1 stands.

**What does not stand is the clause that follows it**, which reads that the requirement is *"reachable only by fission, which changes the product rather than the yield."* **It does not change the product.** Fission in a **subcritical** blanket driven by the fusion neutrons releases its energy as **heat, on site, inside the device** — which is exactly the product the whole exercise is for. A blanket that fissions is not a different machine selling something else; it is the same machine recovering more of what its own neutrons are worth.


#### What a subcritical blanket returns, derived

A source neutron entering a subcritical assembly of multiplication factor `k` is multiplied to `1/(1 − k)` neutrons in circulation. One of those is the source neutron itself, so `1/(1 − k) − 1` were born in fission, and each fission makes `ν` of them. Hence the fissions per source neutron and the energy they release are


$$F \;=\; \frac{1}{\nu}\left(\frac{1}{1-k}-1\right) \;=\; \frac{k}{\nu\,(1-k)}, \qquad E \;=\; F\,E_f$$

with `ν` = 2.9 per fission and `E_f` = 200 MeV. Two sourced inputs, one identity, and no fitted parameter. Proposition 10 in §13.9 gives it in full.

**The relation checks against a blanket this paper already uses.** The sourced fission-suppressed design multiplies the neutron's energy by 1.6, and attributing the whole of that to fission — an overstatement, since some is ⁶Li exotherm — puts it at `k` ≤ 0.246. A design built to *suppress* fission sits deeply subcritical, which is where it should sit, and which is the check that the relation is in the right regime before it is asked anything.


#### The specification

| configuration | value per fusion required | subcritical `k` required | the fusion's share |
|---|---|---|---|
| the machine as built | 234.3 MeV | 0.770 | 7.5 percent |
| with both collector alterations | 152.7 MeV | 0.684 | — |
| with the optimised production target | 98.7 MeV | 0.580 | — |
| **with all three alterations** | **64.3 MeV** | **0.469** | **27.4 percent** |

> **Every one of those is deeply subcritical, and that is the result.** For scale, an accelerator-driven subcritical system is designed around `k` = 0.95, where the same relation returns 1310.3 MeV per source neutron, and a power reactor runs at unity. **The requirement is met at a `k` between 0.469 and 0.770** — far below the ADS design point and further below criticality, which is a safety margin as well as an engineering one. **A self-sustaining power source exists in these numbers, it returns its energy as heat with nothing leaving the device, and it does not require an advance on anything.**

**Two things travel with that, and both are said here rather than left to a reader.**

**The fusion supplies a minority of the energy.** At the least demanding configuration it is 27.4 percent; at the most demanding, 7.5 percent. What the fusion supplies in full is the **neutrons** — every one of them, at 14.1 MeV, which is the energy at which they drive fast fission in fertile material that a fission spectrum does not reach. **The device is a fusion-driven subcritical fission reactor**, and calling it a fusion power plant would be false. It is a self-sustaining power source on this paper's own criterion, which is the criterion that was asked for: it returns more energy than the beam that drives it, as heat, on site.

**And the comparison a builder will ask for first is made, in §9.4.** The same beam spent on a **spallation**-driven subcritical system would also multiply, and the answer turns out to rest on the structure rather than on the arithmetic: the muon channel is *additive* to spallation rather than an alternative to it, because the same protons make both in the same target. What it can cost is the target's own yield, and §9.4 states how much of that it may cost before it stops paying.


### 9.3 How the specification is measured

**The quantity the specification names is `k`, and `k` is measured rather than computed.** It is one of the oldest measurements in reactor physics and it is made on subcritical assemblies as a matter of routine, by at least three methods that share no instrument:

1. **Pulsed-neutron, by the Sjöstrand area method.** Pulse the assembly and separate the prompt decay from the delayed background in the detector's time spectrum; their area ratio gives reactivity in dollars directly, with no calibration of detector efficiency.
1. **Source jerk.** Withdraw the source from a steady subcritical state and read the prompt drop against the delayed-neutron plateau.
1. **Noise, by Rossi-α or Feynman-α.** Read the prompt decay constant from the correlation in the detector counts alone, with no perturbation of the assembly at all.
**Two of those must agree.** The rule §8.4 applies to sticking applies here for the same reason: a disagreement between two methods that share no calibration is a refusal, not an average.

**The prediction is committed in advance.** For a blanket built to the specification above, the measured `k` must lie between 0.469 and 0.770 according to which alterations the machine carries, and the energy multiplication read from the assembly's own heat balance must agree with `F = k/(ν(1 − k))` at the `ν` of its fuel. **A measured `k` below 0.469 falsifies the power-source configuration** and leaves the bred-fuel route of §5.4 standing, which needs no fission at all.


### 9.4 Against spallation on the same beam

A reader who has followed §9.2 will ask the obvious question, and it is the right one: **the same protons could drive a subcritical blanket by spallation alone, without any of this.** Why buy a capture solenoid, a fuel cell and a tritium inventory to make neutrons a spallation target makes for nothing?

**The question has a structure worth stating before any number is put to it.** The muon channel does not *replace* spallation. The same protons strike the same target and make **both** — pions and spallation neutrons, in the same collisions, as §9.2's whole argument depends on. So the muon channel is **additive in neutrons**, and there is no *instead* to price. Adding it cannot reduce what spallation already delivers.

**What it can reduce is the target.** A target the pions can escape from is narrow — §7.3's transparency argument fixes its radius, and the machine's bore constrains it further — and a narrow target is a poorer spallation source than the thick one a facility would otherwise choose. **That is the whole of the trade**, and it reduces to a single question: how much spallation yield does transparency cost?

Set the two side by side. A spallation-optimised target returns `Y` neutrons per proton. A pion-transparent one returns `Y(1 − f)`, and adds the muon channel's fusion neutrons on top. The muon channel is a net gain whenever


$$f \;<\; \dfrac{w\,Y_{fus}}{Y}, \qquad Y_{fus} \;=\; Y_{\pi}\,\eta\,N$$

and the left-hand side is what §4.1's pion yield, §5.3's collection and the measured cycle count already fix: **52.41 per proton** with both collector alterations, 34.14 per proton with the machine as built.

| what a spallation-optimised target returns | transparency may cost up to |
|---|---|
| 100 neutrons per proton | 52.4 percent |
| 150 neutrons per proton | 34.9 percent |
| 250 neutrons per proton | 21.0 percent |

> **Read that as a requirement on the target, because that is what it is.** The muon channel adds neutrons unless making the target transparent to pions costs more than the figure beside the yield — and even against a very productive spallation target the requirement is only that transparency stay under 21.0 percent.

**The estimate is conservative in three places, and each runs the same way.** It counts a 14.1 MeV neutron as worth exactly one spallation neutron, where in a fast blanket it is worth more, because 14.1 MeV drives fast fission in fertile material and (n,2n) that a spallation spectrum reaches less of. It does not count the alpha, which the muon route returns as heat directly. And it treats the transparency penalty as a straightforward loss, which in a **blanket-coupled** system it is not: a neutron or a secondary that escapes a narrow target is not lost, it enters the blanket. A narrow target costs a *neutron source* its yield because the neutrons must reach moderators; it costs a blanket-coupled system much less, because the blanket is what surrounds the target in the first place.

> **So the comparison that §11 recorded as unmade is now made, and it does not go against the muon channel.** What remains open is narrower and is stated as such: **what a spallation-optimised target at 8 GeV actually yields, and what transparency actually costs it.** Neither figure is derived in this paper, both are ordinary target-design calculations, and §10 Stage D measures the pair on one apparatus — the same beam and the same blanket, with the fuel cell in and out.


### 9.5 But the binder does not have to be bought

There is, however, a configuration in which the binder costs nothing, and it turns on a fact about the cycle that has been in view since §3. The catalytic cycle has no input per event: the binder is not consumed, and no energy is supplied to bring the nuclei together. Its only input is the binder itself, so the whole of the negative balance sits in a single question — what the binder costs.

Pions are a byproduct of spallation. They are created in the same nuclear collisions that make a spallation target's neutrons, by the same protons, in the same target. A facility running a proton driver for neutrons, for isotopes, or for an accelerator-driven subcritical blanket is therefore already making them and throwing them away. Capturing them costs a collector, but it does not cost any beam.

On that accounting the marginal beam energy attributable to one binder is zero, and every fusion the binder catalyses is gain. Theorem 4 in §13.8 states this formally, together with the reason a loss factor cannot overturn it.

| capture efficiency | fusion heat, as a fraction of beam energy | reachable? |
|---|---|---|
| 30 percent, today's front end | 10.5 percent | yes |
| 0.3420, the ceiling at the specified inventory | 12.0 percent | yes |
| one half | 17.6 percent of beam | on the physics, yes — but at about 45 kg of tritium, which §11 records as an unpriced condition |
| 90 percent [DESIGN], the specified collector | 31.6 percent of beam | **no — above the ceiling at any target depth** |

**That last row is withdrawn.** A capture efficiency here means a muon that *stops in the fuel*, and a stopping target is one muon range deep, so it stops only the part of the accepted spectrum below its range. The bound is not the collector's: it is the solenoid's acceptance, 0.5069, which no target depth exceeds. **That row compared a collector's acceptance with a fuel target's stopping fraction, which are different quantities.**


### 9.6 What that returns, at the capture actually reachable

**And the headline figures must carry the same correction, plus §5.2's loss budget.** Both, applied:

| capture | binders per second | fusion heat |
|---|---|---|
| one half, as first computed | 2.80 × 10^14 s^-1 | 176 kW |
| 0.3420, the stopping ceiling above | 1.918 × 10^14 s^-1 | 120.1 kW |
| **0.2438**, that ceiling through the loss budget | **1.367 × 10^14 s^-1** | **85.6 kW** |

> **The conclusion is untouched and only the magnitude moves, and that asymmetry is the whole point of this configuration.** Every other balance in this paper is a ratio against unity, so a factor of 0.7127 decides it. This one is not a ratio at all: the marginal beam energy per binder is **zero**, so any positive heat is gain and no loss factor can take it below unity. 85.6 kW of fusion heat at zero marginal beam cost is the same result as 176 kW, reached by the same argument and arriving at a smaller number. **It is the one figure here that a collection factor rescales without deciding**, because it was never conditional on an acceptance clearing a threshold.

![Figure 6](papers/figures/fig6-coproduct.png)

**Figure 6.** The one configuration that is net-positive on witnessed numbers alone. Because the beam is running for another reason, the marginal energy spent per binder is zero, so any point on this line is gain and no loss factor can push it below it.

> **This is a net-positive cold fusion reaction.** No input per event, no input for the binder, and real energy out. It is provable from witnessed quantities and needs no number that has not been measured.


### 9.7 And it dissolves the flux gap

The requirement has always been stated against **delivered** muon beams — about 1.0 × 10^8 s^-1 today and 1.0 × 10^10 s^-1 planned — which gives a shortfall of five orders of magnitude. Those are *momentum-selected, transported* beams, which discard almost everything the target makes. In-situ capture at the production target is 2.80 × 10^4 times the best planned delivered beam, or 1.37 × 10^4 at the delivered capture above, **because nothing is transported and nothing is selected.** The flux gap is an artefact of buying muons rather than making them where they are used.


### 9.8 Committed predictions for the net-positive run

Stated before the run, at 1 MW on target and the witnessed cycle count of 150 cycles, **computed from the machine of §7 and not from a hypothetical one:**

| quantity | committed value |
|---|---|
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

**Stage D — the integrated demonstration.** The net-positive configuration of §9, on a spallation driver already running, against the committed predictions of §9.8.

> The order is not arbitrary, and each stage earns its place. Stage A multiplies everything downstream of it. Stage C decides whether the route that clears unity at the delivered acceptance exists at all. Stage B decides a factor *within* a route rather than whether the route is there. And Stage D is the demonstration itself, which cannot be interpreted before Stage A has run.


---


## 11. Limits, and what this paper does not claim

Each item below is a limit on what the foregoing establishes. None of them is resolved by argument in this paper, and where a measurement would settle one, that measurement is named. §13.10 lists the three that bear most directly on the results.

**The operative sticking is unresolved between two measurements**, though not in a way that changes the heat form's verdict. 0.5050 percent and 0.5320 percent are the two effective values the measured reactivation returns, and both lie above the break-point at 0.1580 percent, so the heat form fails at perfect collection on either. What the disagreement leaves open is the service life, and with it every balance that depends on it. §8's protocol settles it, and nothing here stands in for that.

**Every collection figure here is an acceptance rather than a delivered efficiency** until Stage A runs. §5.2 computes the losses between the two and §5.3 restates every balance through them, but a computed budget is not a measurement, and the margin over the falsification floor is 1.073.

**Every balance assumes perfectly pure fuel.** At the bound case, 5.49 ppm of high-Z contamination costs as much binder as decay does. The purity series of §8.3 is what measures it.

**The temperature axis is confounded in the existing record.** The cleanest published data are also the coldest and densest, so temperature, purity and density cannot be separated from what exists. That is a fault in the record rather than in the reaction, and §8.3 is written to separate them.

**Every modelled service life here rests on a density no experiment has reached**, and after §5.3's correction it buys very little. The model itself is in good order — at the density that *has* been reached it returns 152.8 cycles against the 150 cycles measured, a ratio of 1.019 — but the rows that use it assume 8.5 times liquid where 1.2 has been held, and even granted that they return only 190.1 cycles against 150 cycles measured. **The model is worth a factor of about a quarter and an unreached density to obtain it**, which is why every result this paper offers is stated at the measured count, and why §5.3's surviving route uses the model nowhere.

**Two target figures the comparison against spallation turns on are not derived here.** §9.4 makes that comparison and finds it does not go against the muon channel — the channel is additive rather than alternative, and the only trade is what pion-transparency costs the target's spallation yield. But the two numbers that would close it are ordinary target-design calculations this paper does not perform: **what a spallation-optimised target at 8 GeV actually yields**, and **what transparency actually costs it**. §9.4 states the requirement in the form a target designer can check, and §10 Stage D measures the pair on one apparatus.

**The tritium inventory a plant would hold is very large, and this paper does not price holding it.** Because the target must be one muon range deep, and because Proposition 9 shows that compression does not reduce the requirement, the standing inventory is 5.13 kg at the designed bore, 10.79 kg at the wider one, and about 45 kg to approach the acceptance ceiling. Those are kilogrammes of tritium in one target, against 2.41 mg in the demonstration cell of §6.3 — a step of six orders of magnitude between the experiment this paper specifies and the plant its balances describe. An inventory at that scale is a licensing, supply and containment problem of a different kind from anything in §7, and one this paper neither solves nor costs. It bears asymmetrically on the routes: the bred-fuel configuration breeds its own tritium once running and so needs the inventory only to start, while the heat and work forms need it throughout and earn nothing back. **Nothing in §10 measures it**, because §10 runs at the milligramme scale, and it should be read as a condition on any plant built from these results rather than as a term in any balance stated here.

**The optimised production target is a discrepancy that cannot be closed by argument.** A published optimisation costs 4.69 GeV per pion against the 11.13 GeV integrated in §4.1. Three candidate mechanisms were examined and bounded; what survives is a **normalisation** — pions per beam particle against pions per interaction — needing 2.389 interacting nucleons, which reproduces the optimised figure closely and which a deuteron on a long target supplies. **Stage C measures it.**

**And the standalone configuration is closed rather than open.** §9.1 is a theorem, and no measurement in §10 can overturn it. What §10 can decide is the co-product configuration and the bred-fuel route, which are the two that survive.


---


## 12. What is proved, and what is unwitnessed

The two are different, and the difference is the whole shape of this paper. A quantity that has been measured and a quantity that has been computed are not the same kind of thing; nor are a proof with no free parameter and a configuration nobody has assembled. This section sorts every result in the paper into those categories, so that a reader may check the claim against the evidence for it without reconstructing the argument.


### 12.1 Proved, with no free parameter

Each of these is a theorem or a derivation from measured inputs, and no measurement in §10 can overturn any of them.

1. **A cold fusion reaction exists and has been witnessed.** The definition of §1 is structural, its seven conditions admit exactly one binder (Theorem 1), and the cycle it names has been measured in laboratories since the 1950s.
1. **An eighth condition decides whether it is worth running**, and it contains no free parameter (Proposition 1). Every term in it has been measured.
1. **Sticking does not depend on the binder's mass** (Theorem 2), so condition 8 is a specification on the machine and not a search over the spectrum.
1. **The standalone configuration is closed** (Theorem 3): no admissible binder pays for itself as a power source, at any collector.
1. **Where the binder is a byproduct of a beam already running, the configuration returns net energy** (Theorem 4), and no loss factor can take it below unity, because it was never a ratio against one.
1. **No heat form and no work form is self-sustaining on a non-fissioning blanket**, in any configuration this paper can construct. The largest either reaches is 0.513, granting the optimised production target, the wider bore, the wider stopping window and an unreached fuel density all at once.
1. **Two of the balance's four terms are closed above by physics rather than by engineering** — the service life at 198 cycles by the sticking, and the collection at unity because it is a fraction — so a self-sustaining power source is a statement about what a fusion is worth, and about nothing else. §9.2 solves it.

### 12.2 Proved above unity, and unwitnessed

**Two configurations return more energy than they cost. The first is a power source and the second is a breeder, and they are not the same claim.**

**The power source.** Setting the balance to unity and solving, the value recovered per fusion must reach 152.7 MeV with both collector alterations, or 64.3 MeV with the optimised production target as well. A non-fissioning blanket cannot supply that. A **subcritical** blanket driven by the same fusion neutrons supplies it at a multiplication factor between 0.469 and 0.770 — deeply subcritical, against 0.95 for an accelerator-driven system and unity for a power reactor. **The energy is heat, recovered on site, with nothing leaving the device.** The fusion supplies between 7.5 percent and 27.4 percent of it and all of the neutrons, so the device is a fusion-driven subcritical fission reactor rather than a fusion power plant, and §9.2 says so in those words. What is unwitnessed is the assembly; the quantity it turns on is `k`, which §9.3 measures by three routes that share no instrument.

**The breeder, which needs no fission at all.** Its balance is 1.480 through an optimised production target, 2.271 with the two collector alterations as well, and 0.957 with no target factor at all. Every term in it is set out below, with what is known about each.

| term | value | how it is known |
|---|---|---|
| service life | 150 cycles per binder | **measured**, Los Alamos; no model is used |
| value per fusion | 146.06 MeV | **sourced**, a fission-suppressed breeder blanket |
| production cost | 11.13 GeV per pion | **derived**, integrating measured cross sections (§4.1) |
| collection, as built | 44.43 percent | **computed** by a model reproducing an independent simulation to 0.982 |
| loss budget | 0.7127 | **computed**, never measured — §10 Stage A |
| production target factor | 2.373 | **published**, mechanism explained in §4.2 — §10 Stage C |

> **Two terms in that table have not been measured, and both are named with the measurement that settles them.** Neither is a gap in the mathematics: the balance is an identity, and every quantity entering it either has a measurement behind it or has an experiment specified that would supply one. **What has never happened is that anyone has assembled the configuration and run it.** That is the sense in which this result is unwitnessed, and it is the only sense.

Two things about that sentence need saying precisely, because both are easy to read as more than they are.

> **What "self-sustaining" means here, stated exactly.** The account closes: the configuration returns more energy than the beam spent to make its binders. It does **not** mean the device powers itself from its own output — the product is fissile material and tritium bred in the blanket, which leaves the device as fuel and yields its energy in a reactor that burns it. A device whose product is energy in the form of heat or of work is **not** self-sustaining on anything in this paper, and §12.1 states that as a closed result rather than an open one. The two claims are different and neither stands in for the other.

And the second is the size of what is left open.

> **The residual, if both unmeasured terms were to go the wrong way, is small.** Set the production target aside entirely — take the measured production cost of §4.1 and nothing better — and the same route reaches 0.957, short of unity by 1.045. The whole of that shortfall lies inside the loss budget, which is the one term in the column that has never been measured at all.


### 12.3 Specified, and buildable now

1. **The materials are fixed to the last free parameter** — fuel, density, temperature, purity, geometry, binder species — as a bill of materials rather than a sketch (§6).
1. **The machine that supplies the binders is designed as a build package**, to a circuit, a cold mass, a conductor grading, a target and a failure analysis (§7).
1. **The procedure that would witness the unwitnessed configuration is stated** (§8), with its predictions committed in advance and a rule that a disagreement between two routes is a refusal rather than an average.
1. **The programme that would close the two unmeasured terms is four staged measurements on apparatus that already exists** (§10), the acceptance first, because it multiplies every balance identically and so bounds all of them at once.

### 12.4 Not claimed

**That either configuration is the best use of the beam.** §9.4 shows the muon channel is additive rather than alternative, and states what transparency may cost before it stops paying — but the two target figures that would close the comparison are not derived here, and §11 says which.

**That a plant follows from the demonstration.** The step from the cell of §6.3 to the inventory of §11 is six orders of magnitude in tritium, and this paper prices none of it.

**That the reaction is cold in the everyday sense.** §1 says what the term is used to mean here and what it is not.

> **The reaction is proved from what has been witnessed. One configuration of it returns more energy than it costs, and every term in that balance is measured, sourced, or has a stated experiment that would measure it. The instructions for witnessing it are §6 to §8, and the measurements that would close its two open terms are §10.** That is the whole of the claim, and no part of it is larger than the evidence behind it.


---


## 13. The mathematics, in full

The body of the paper states results and points at where they come from. This section carries the derivations themselves, so that each may be checked without reconstructing it. **Where a statement is a theorem it is proved; where it is a derivation resting on measured inputs, it is labelled a proposition and its inputs are named.** Nothing is called proved that is not.


### 13.1 Notation

| symbol | meaning |
|---|---|
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

**Proposition 2 (the lower bound exists, and its direction).** *Condition 2 — that the tunnelling rate exceed the decay rate of the state producing it — places a lower bound on $m_b$, and that bound rises as the binder is made lighter.*

*Derivation.* In a hydrogenic bound state the orbit radius scales inversely with the reduced mass, $a_b \propto 1/m_b$, and the internuclear separation of the mesomolecule follows it, $R_{dt} \propto 1/m_b$. The barrier penetration factor is exponential in $\sqrt{R_{dt}}$, so $\lambda_f$ rises steeply with $m_b$ while $\lambda_0$ does not. Condition 2 requires $\lambda_f > \lambda_0$, and because one side of that inequality is monotone in $m_b$ and the other is not, there is exactly one crossing. That crossing is the floor. ∎

> **What this establishes and what it does not.** The argument establishes that a floor exists, that it is unique, and that it lies above the electron. **The numerical value 119 electron masses — or 60.8 MeV as an energy — is carried from the earlier treatment and is not recomputed here**, and this paper does not claim otherwise. Corollary 1.0 is why that is tolerable: Theorem 1's conclusion survives this floor being wrong by a factor of 207.

**Proposition 3 (the upper bound exists, and its direction).** *Conditions 3 and 4 place an upper bound on $m_b$, and that bound falls as the binder is made heavier.*

*Derivation.* A binder heavy enough to be absorbed by a nucleus before the cycle completes catalyses nothing, failing condition 3; and it produces ash the branching ratios do not predict, failing condition 4. Nuclear absorption rates rise with the binder's mass through the overlap of its orbit with the nuclear volume — the orbit shrinking as $1/m_b$ while the nucleus does not — so the two rates cross once. That crossing is the ceiling. ∎

> **Again, existence and direction rather than value.** The numerical ceiling 918 electron masses is carried from the earlier treatment. Theorem 1's conclusion survives this ceiling being wrong by a factor of 3.54.

**The admissibility test, stated before it is applied.** A particle may serve as a binder only if all four of the following hold. It must be **negatively charged**, so that it binds to a nucleus rather than to an electron. Its **mass** must lie in the structural window. Its **lifetime** must exceed the mesomolecular formation time, which at liquid density is of order 1 × 10^-9 s — a particle that decays before the molecule forms never enters the cycle at all. And it must **not be strongly interacting**, because a hadron in a mesomolecule is absorbed by the nucleus long before the cycle completes, which fails conditions 3 and 4 together.

> **Theorem 1 (uniqueness of the binder).** *Exactly one particle in the charged spectrum satisfies all four tests: the negative muon.*

>

> *Proof.* The lifetime test is applied first, because it is the one whose set can be closed. A binder must outlive the mesomolecular formation time, which at liquid density is 1 × 10^-9 s. **Exactly 5 charged particles in the Review of Particle Physics do**: the electron and the antiproton, which are stable, and the muon, the pion and the kaon. That cut is a published lifetime against a fixed threshold, so it can be checked for completeness without judgement. Every other charged particle decays before the molecule forms — the charged hyperons by roughly an order of magnitude, the tau, the charmed and bottom hadrons and every resonance by more — and so is excluded before its mass is ever consulted.

>

> Of those 5, **2 lie inside the window**: the muon at 207 electron masses and the pion at 273 electron masses. The electron lies below it; the kaon at 966 electron masses and the antiproton lie above it. Of the two inside, the pion is a hadron and is absorbed before the cycle completes. **1 therefore survives all four tests.**

>

> The sign is fixed separately and not by mass. A $\mu^+$ binds an electron into muonium and is repelled by every nucleus in the fuel; it forms no mesomolecule at any density or temperature. Hence the binder is the **negative** muon, and it has exactly one parent, $\pi^-$ decay. ∎

A reader may reasonably ask how much of that rests on the two numbers the window is drawn at, since neither is recomputed here. The answer is that it rests on them hardly at all.

> **Corollary 1.0 (the result does not depend on the window's exact bounds).** *Any window whose lower bound lies between the electron and the muon, and whose upper bound lies between the pion and the kaon, admits exactly the same set.*

>

> *Proof.* The admitted set is decided by the **gaps** in the spectrum rather than by the bounds. The nearest particle below the muon is the electron, and the nearest above the pion is the kaon; no charged particle with a usable lifetime lies between. The lower bound may therefore move by a factor of 207 and the upper by 3.54 without changing the answer. ∎

**This matters for what §13.3 does and does not establish.** The bounds themselves are carried from the earlier treatment and are not recomputed here; Propositions 2 and 3 give the scaling arguments that produce them but not the numerical crossing. Corollary 1.0 is what makes that acceptable: the theorem's conclusion survives an error of two hundred in the lower bound and three and a half in the upper.

**Corollary 1.1.** *Every yield in this paper is a $\pi^-$ yield*, and the production target's material is constrained by the charge ratio it returns and not only by its total yield — which §6.3 states as a specification.


### 13.4 Sticking does not depend on the binder's mass

> **Theorem 2 (mass-independence of sticking).** *In the sudden approximation, and to leading order in the binder's mass over the alpha's, the probability $\omega_s$ that the binder is lost to the fusion product is independent of $m_b$.*

>

> *Proof.* Sticking is the probability that the binder, initially bound in an orbit of radius $a_b \propto 1/m_b$, is captured into a bound state of the recoiling $\alpha$. In the sudden approximation it is the squared overlap of the initial binder wavefunction with the final bound states of the $\alpha$, evaluated in the frame moving at the recoil velocity $v_R$:

>


$$\omega_s \;=\; \sum_{n\ell} \left| \int \psi^{*}_{n\ell}(\mathbf{r})\, e^{\,i m_b \mathbf{v}_R\cdot\mathbf{r}}\, \psi_{i}(\mathbf{r})\, d^3r \right|^2 .$$

>

> Both $\psi_i$ and $\psi_{n\ell}$ are hydrogenic with the same reduced mass, so the natural length in the integral is $a_b \propto 1/m_b$. Rescaling $\mathbf{r} = a_b \mathbf{u}$ makes the wavefunctions mass-independent functions of $\mathbf{u}$, and the exponent becomes $i\,m_b v_R a_b\, \hat{v}\cdot\mathbf{u}$. Since $a_b \propto 1/m_b$, the product $m_b a_b$ is a constant, and the exponent depends on $v_R$ alone. **Every dependence on $m_b$ has cancelled**, and $\omega_s$ is a function of the recoil velocity over the orbital velocity only. That ratio is measured at 2.97 for $d+t$. ∎

**One step in that proof is an approximation, and it is worth pricing rather than passing over.** The rescaling uses $a_b \propto 1/m_b$, which is exact for the reduced mass $\mu = m_b m_\alpha/(m_b + m_\alpha)$ only when $m_b \ll m_\alpha$. Restoring it, the exponent carries a factor $m_b/\mu = 1 + m_b/m_\alpha$, so **the whole of the residual mass dependence enters through that one ratio and nothing else**. At the muon the ratio is 0.02835; at the ceiling of the structural window it is 0.1259, and nowhere in between is it larger. Its direction is worth noting too: a larger exponent oscillates faster and reduces the overlap, so the residual makes a *heavier* binder stick *less* — which is the direction that would help. **Theorem 1 leaves no heavier admissible binder to exploit it**, and the theorem below is stated over the occupant the window actually has rather than over a hypothetical one.

**Corollary 2.1 (condition 8 is a specification, not a search).** Since $\omega_s$ does not depend on $m_b$, no admissible binder returns a smaller loss per cycle than the muon. Combined with Theorem 1, which leaves no other occupant of the window, **condition 8 cannot be satisfied by looking for a better particle.** It is a constraint on the machine.

> **Theorem 3 (closure of the standalone configuration).** *The admissible binder does not satisfy condition 8 as a standalone power source, and no other particle is available to.*

>

> *Proof.* By Theorem 1 the structural window has exactly one admissible occupant, so $\omega_s$ is the muonic value and $N \le 1/\omega_s$ is the bound it sets. $Q_{fus}$ and $f_{work}$ are properties of the fuel and the plant, not of the binder, so the right-hand side of Proposition 1 is fixed. The left-hand side, $E_b$, is bounded **below** by the cost of producing the parent particle, which §13.6 puts at 11.13 GeV per pion and which no collector can reduce. Taking the most favourable admissible values of every term simultaneously, the best balance available is 0.807 — less than unity.

>

> That closes the configuration for the muon. It closes the *search* as well, and this is where Theorem 2 does its work: to leading order $\omega_s$ carries no dependence on the binder's mass at all, so a hypothetical occupant elsewhere in the window would inherit the same bound rather than improve on it. The residual priced above runs toward less sticking only for a **heavier** binder, and the window's one heavier candidate is a hadron, excluded by conditions 3 and 4 before its sticking is ever consulted. **The configuration is therefore closed by the structure of the window rather than by any measurement**, and no experiment in §10 can overturn it. ∎

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

> *Proof.* Let the driver deliver power $P$ for a purpose that does not depend on the pions, and let $\mu$ be the marginal **beam** energy attributable to one binder. Pions are produced in the same nuclear collisions that make the target's neutrons, by the same protons, in the same target; capturing them requires a collector but no additional beam. Hence $\mu = 0$.

>

> The fusion heat returned is $H = n_\mu N Q_{fus}$ with $n_\mu = \Phi_\pi \eta_{stop}$ the rate of stopped binders. The net return is $H - n_\mu \mu = H > 0$ for any $\eta_{stop} > 0$.

>

> **The balance is therefore not a ratio against unity**, and this is what distinguishes it from every other configuration in the paper. A loss factor $f \in (0,1]$ applied to $\eta_{stop}$ rescales $H$ to $fH$, which is smaller and still positive. Applying §5.2's budget takes the returned fraction from 12.0 percent to 8.56 percent of the driver's beam energy, and 85.6 kW on a 1 MW driver — **a different number and the same conclusion.** ∎

The premise of that theorem is about **beam**, and a reader is owed what it does not cover.

> **The premise is about beam, and there is a second cost the theorem does not carry.** Capturing the pions means putting a capture solenoid and a free liquid-metal jet around the host's production target, and a host running that target for **neutrons** may get fewer of them, or get them with a different spectrum, than it would from the target it would otherwise have chosen. That is a real cost and **this paper does not price it**, because it depends on a host design this paper does not specify.

>

> What can be said is the condition under which it does not matter. Writing $L$ for the fraction of the host's own product lost to the change and $V_{host}$ for the value of that product, the configuration is net-positive whenever $H > L\,V_{host}$. With $H$ at 8.56 percent of the beam energy, **a host losing less than that fraction of its own output is ahead**, and one losing more is not. §10 Stage D is where a specific host would measure $L$; until then the co-product result should be read as *net-positive on beam*, which is what is proved, rather than *net-positive for the facility*, which is not.

**Remark.** Theorem 4 does not contradict Theorem 3. Theorem 3 forbids a configuration that must buy its own binders from paying for itself; Theorem 4 describes one that does not buy them.


### 13.9 The subcritical blanket

**Proposition 10 (the energy a subcritical assembly returns per source neutron).** *In an assembly of multiplication factor* $k < 1$ *driven by an external neutron source, the fissions per source neutron and the energy they release are*


$$F \;=\; \dfrac{k}{\nu\,(1-k)}, \qquad E \;=\; F\,E_f$$

*with* $\nu$ *the neutrons released per fission and* $E_f$ *the energy released per fission.*

*Derivation.* Let one source neutron enter the assembly. Each generation of neutrons produces `k` times as many as the one before it, so the total number in circulation over all generations is the geometric sum $\sum_{i \ge 0} k^i = 1/(1-k)$, which converges precisely because the assembly is subcritical. One of those is the source neutron itself, so $1/(1-k) - 1 = k/(1-k)$ were born in fission. Each fission releases $\nu$ neutrons, so the number of fissions is that count divided by $\nu$, which is $F$; and each releases $E_f$. ∎

**Corollary 10.1 (the inversion).** *The multiplication factor required to return a given energy per source neutron is* $k = r/(1+r)$ *with* $r = E\,\nu/E_f$, *and it is below unity for every finite* $E$. This is what §9.2 solves, and the fact that it is below unity for any finite requirement is why the question is how far below rather than whether.

> **What Proposition 10 does not carry.** It is a point-kinetics statement: it assumes one multiplication factor for the whole assembly and takes no account of where the source sits in it, of leakage, or of the spectrum. A real blanket's source is central and its neutrons enter at 14.1 MeV rather than at a fission spectrum's mean, both of which raise the yield above this estimate for the same `k`. **The proposition is therefore used here as a requirement and not as a prediction**, and §9.3 states the measurement that would replace it.


### 13.10 What is not proved

Three things in this paper are **not** theorems, and are marked as such wherever they appear.

**The delivered acceptance is computed, not measured.** §5.2's loss budget is a product of five terms, each derived, but the product has never been measured end to end. §10 Stage A is that measurement, and until it runs every figure downstream of it is conditional.

**The optimised production target's factor is taken from the literature, not reproduced here.** The 4.69 GeV of §5.4 is a published optimisation. Three candidate mechanisms for the discrepancy against this paper's 11.13 GeV were examined and bounded, and what survives is a normalisation requiring 2.389 interacting nucleons. §10 Stage C measures it.

**The operative sticking is unresolved between two published measurements.** 0.5050 percent and 0.5320 percent are the two effective values in the record, and no argument here chooses between them; both lie above the break-point at 0.1580 percent, so the choice moves the service life rather than the heat form's verdict. §8's protocol chooses, and §8.4 commits in advance to reporting a bound rather than an average if the two routes disagree.


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

