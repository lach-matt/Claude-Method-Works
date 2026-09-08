# Cold Fusion by Muonic Binding

*A structural definition, two uniqueness theorems, and the closed-form energy account*

M. Lach

Version 1.0


## Abstract

A **cold fusion reaction**, as this paper uses the term, is a nuclear fusion event in which the approach to nuclear separation is supplied by molecular binding geometry rather than by kinetic energy. The definition is structural rather than thermal: it does not say the reaction is cold in the everyday sense, only that the work of bringing two nuclei within tunnelling range is done by a bound state instead of by a collision. The reaction the definition picks out is muon-catalysed fusion, a laboratory phenomenon since the 1950s, and the paper's first result is that the definition picks out that and nothing else.

Seven conditions are necessary for such an event to occur and to be checkable. Applied to the closed index of charged particles they admit **exactly one** binder — the negative muon — because the conditions place both a floor and a ceiling on the binder's mass, and the window between them, 119 electron masses to 918 electron masses, has a single occupant. Of 13 charged particles scanned, 5 outlive the mesomolecular formation time and 2 lie inside the window; one survives the remaining test. The window's lower bound may move by a factor of 207 and its upper by 3.54 before that count changes.

A second uniqueness result closes the other half of the configuration. **The fuel is unique as well.** That *d*–*t* is the best mesomolecular fuel is not news to the field; what is set out here is the closed argument for it, over the whole candidate set at once. *d*–*t* maximises the energy returned per binder by a factor of 77.85 against the next candidate — and the runner-up uses *more* tritium rather than less. The figure of merit is not the energy release but the cycles a binder completes before it decays or sticks, `N = 1/(ω_s + λ_0/λ_c)`, which punishes a slow cycle exactly as it punishes a sticky one. The ordering survives every competitor's cycle rate being sent to infinity, leaving *d*–*t* ahead by a factor of 24.58, so it rests on the stickings alone.

The reaction is therefore not speculative, and its uniqueness is not assumed. What has never been observed is a configuration of it that returns more energy than it costs to run, and the distance between those two statements is what the rest of the paper measures. An **eighth condition** makes the question answerable: a binder is worth making only if `E_binder < Q_fus · f_work / ω_s`. It contains no fitted term: two are measured, one is integrated from measured cross sections, and the fourth is a conversion fraction computed at a stated operating point and carried in both of its conventions. Integrating the published pion production cross sections puts production alone at 11.13 GeV per pion, so even a perfect collector would leave the heat form short; sticking is shown to be independent of the binder's mass, so the condition is a specification on the machine rather than a search over the spectrum; and the break-point in sticking lies **below both** published readings rather than between them, so no choice between them repairs the heat form.

Stated at the acceptance the machine actually delivers rather than at an assumed collection, and at the sticking the record supports, **nothing clears unity at the production cost this paper integrates**. The closest is bred fuel at the demonstrated 150 cycles per binder, at 0.623 as built; with both specified collector alterations it reaches 0.957, short of unity by a factor of 1.045 and short by no term other than a loss budget that has never been measured end to end. One route does cross — bred fuel through a *published* optimisation of the production target, at 1.480 — and it crosses on an optimisation worth a factor of 2.373 that this paper prices and **declines to adopt**, because the gap between that optimisation and the integrated 11.13 GeV is a discrepancy the paper records and does not close.

A final result runs the other way and is reported as a quantity to measure rather than a result to build on. **A deuterium cell does not stay a deuterium cell**: one *d*–*d* branch makes tritium, *dtμ* forms far faster than *ddμ*, and the cell tritiates itself to an equilibrium of 0.6211 percent by atom. Such a cell holds less tritium than the specified one by a factor of 64.71 and needs no lithium and no breeding blanket, at the cost of a fusion yield a factor of 48.38 smaller per binder.

The paper closes with the reaction specified to the point where another laboratory could build it, the machine that would supply the binders, the procedure that would witness the configuration, and a statement of exactly what is proved and what is not. **The configuration in which the binder is a byproduct of a beam already running for another purpose is not priced here**; it changes the accounting rather than the reaction, and it is the subject of a separate paper.


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

It is sometimes suggested that screening in a dense medium might make up the difference. It cannot, and the reason is a conservation argument rather than a measurement. Reaching the required approach by screening alone would call for 88 eV of static screening, where the ceiling available in condensed matter is 30 eV — short by a factor of 2.9, which corresponds to 27 orders of magnitude in the rate. For scale, a vibrational quantum in D₂ is 0.365 eV, and that is the order of the energy actually on offer.


## 2. The unique realisation

Applied to the closed index of charged particles, the seven conditions admit exactly one realisation, and the argument that gets there is short. Condition 2 sets a lower bound on the binder's mass, because the separation it produces scales inversely with that mass. Conditions 3 and 4 set an upper bound, because a binder heavy enough to be absorbed by a nucleus before the cycle completes catalyses nothing and produces the wrong ash. Together the two bounds define a **structural window** running from 119 electron masses to 918 electron masses. §14.3 derives both bounds in full.

**Two** particles in the known spectrum sit inside that window, not one, and the second is removed by a test that is not about mass at all. The muon lies at 207 electron masses, a factor of 1.74 above the floor; the pion lies at 273 electron masses, inside the window and excluded because it is a hadron, absorbed by a nucleus long before a cycle completes. **One particle survives every test**, and §14.3 runs the scan in the order that constrains — lifetime first, because that is the cut whose set can be closed against the Review of Particle Physics without judgement, and mass only afterwards.

| excluded | grounds | consulted at |
|---|---|---|
| electron-bound systems | geometry: 74100 fm against 280 fm, some ninety-one orders short — the electron lies below the window | mass |
| the pion | a hadron: absorbed by a nucleus before the cycle completes, failing conditions 3 and 4 | the hadron test, **inside** the window |
| the kaon and the antiproton | above the window's ceiling at 966 electron masses and beyond | mass |
| the tau, the charged hyperons, the charmed and bottom hadrons, every resonance | too short-lived to reach the mesomolecular formation time, so excluded **before** a mass is consulted | lifetime |
| enhanced ambient screening | conservation, §1 | — |
| thermal and inertial fusion | by definition — approach supplied by kinetic energy | — |
| chain multiplication of binders | no nuclear event releases enough to fund a second binder | — |

None of the exclusions is a near thing, and §14.3's Corollary 1.0 prices how far the window's own bounds may move before the surviving set changes: a factor of 207 at the floor and 3.54 at the ceiling.

The sign matters as much as the mass, and it is fixed separately. A positive muon binds an electron into muonium and is repelled by every nucleus in the fuel, so it forms no mesomolecule at any density or temperature. The species question is therefore settled by charge before anything else is considered — a point §9 returns to, because it decides what the production target must be made of.

The reaction is therefore not hypothetical. The event μ⁻ + (d,t) → (dtμ)⁺ → ⁴He + n + μ⁻ + 17.59 MeV has been observed in laboratories since the 1950s, and its cycle rates, sticking fractions and ash have all been measured. What remains unwitnessed is a configuration of it that pays for itself, and that is what the remainder of the paper is concerned with.


## 3. The unique fuel

§2 closes the question of what may *hold* a mesomolecule. It says nothing about what the mesomolecule holds, and this paper had assumed *d*–*t* throughout without asking. That *d*–*t* is the best mesomolecular fuel is not news to the field; what is set out here is the closed argument for it, because the fuel is where this reaction's largest practical liability sits, and a uniqueness claim covering only half the configuration is not a uniqueness claim.

The candidate set closes the same way §2's did. A mesomolecular fuel is a **pair** of light nuclei that a muon can bind, and the hydrogen isotopes give exactly 6 such pairs. The helium pairs are listed beside them and excluded by the same arithmetic rather than by assertion.

**The figure of merit is not the energy release.** A muon is a reusable catalyst with exactly two ways of being lost — it decays, or it sticks to a fusion product — and what one muon is worth is therefore the number of cycles it completes before one of the two claims it. Writing `λ_c` for the cycle rate and `λ_0` for the free decay rate,

> **the cycles a binder completes are** `N = 1 / (ω_s + λ_0/λ_c)`,

so that a *slow* cycle is punished by decay and a *sticky* one by sticking, and a fuel must escape both to be worth anything. Proposition 10 in §14.8 derives it. The free decay rate is 4.5517 × 10^5 s^-1.

| pair | cycles per muon | energy per muon |
|---|---|---|
| **d–t** | **113.08 cycles** | **1989.1 MeV** |
| t–t | 2.26 cycles | 25.55 MeV |
| p–t | 0.7117 cycles | 14.098 MeV |
| d–d | 2.36 cycles | 8.62 MeV |
| p–d | 1.0191 cycles | 5.595 MeV |
| d–³He | 0.1805 cycles | 3.311 MeV |
| p–³He | 0.0215 cycles | 0.0400 MeV |
| p–p | 0.00022 cycles | 0.00032 MeV |

The whole set is shown rather than summarised, because a uniqueness claim over a closed set is only checkable if the set is on the page. Two entries repay reading, and both are visible in the table itself. *p*–*t* completes **fewer** cycles than *d*–*d* and returns **more** energy per binder than it, its larger release per fusion outweighing its shorter catalytic life — which is what it means for the figure of merit to be neither column alone. And *p*–*d* completes just over one cycle, so the entries below *d*–*d* are behind rather than sterile.

> **Theorem 4 (uniqueness of the fuel).** Over the closed set of light-nucleus pairs a muon can bind, *d*–*t* maximises the energy returned per binder, by a factor of 77.85 against the next candidate. §14.8 proves it.

**And the ranking does not rest on the cycle rates.** They are literature bands rather than a single measurement for every pair, so a reader is entitled to ask what the ordering would survive. The answer is: all of it. Since a binder completes at most `1/ω_s` cycles whatever the cycle rate, no pair can return more than `Q/ω_s` per binder however fast it is made to run, and that ceiling consults no rate at all. The largest ceiling any competitor has is *t*–*t*'s, at 80.93 MeV — so *d*–*t*'s own value still leads by a factor of 24.58 with **every other pair's cycle rate sent to infinity**. Corollary 4.1 in §14.8 states it. Only the stickings are load-bearing after that, and the margin one of them would have to close is the same factor of 24.58.

Two features of that result matter more than the ranking itself.

**The runner-up uses more tritium, not less.** The second-placed pair is *t*–*t*, so nothing is gained on the reaction's principal liability by moving down the list. Against *d*–*d* — the only tritium-free pair with any cycle rate at all — *d*–*t* is ahead by factors of 230.76 on energy per binder and 95.77 on neutrons.

**So *d*–*t* is not a preference.** It is the only pair whose cycle is fast enough to outrun the muon and whose sticking is low enough to let it repeat, and every other admissible pair fails one of those two tests by more than an order of magnitude. Taken with §2, the reaction is unique in its binder and unique in its fuel, and neither uniqueness was assumed.

**What the ranking does not settle.** It ranks on energy returned per binder, which is the right objective for a machine that must pay for its binders and the wrong one for a machine judged on what it must hold. A designer weighing tritium inventory rather than yield is asking a different question, the ranking cannot see it, and §8 answers it.

**The model is used for ratios and never for an absolute.** Run on *d*–*t* it returns 113.08 cycles against the 150 cycles measured at Los Alamos, a fidelity of 0.7539. That is close enough to rank fuels against one another and not close enough to price a machine, so every balance in this paper uses the measured count and none uses the model's.


## 4. The eighth condition

The seven conditions settle whether the reaction occurs. None of them settles whether it is worth running, and it is that second question — not the first — which has remained open. The condition below is what makes it answerable.

> **Condition 8.** A binder is worth making only if `E_binder < Q_fus · f_work / ω_s`, where `E_binder` is the energy cost of producing and capturing one binder, `Q_fus` the energy released per fusion, `f_work` the fraction of that release convertible to the form being paid in, and `ω_s` the **sticking** probability per cycle.

`ω_s` is the sticking probability throughout this paper, and it is one of the binder's two loss channels rather than both of them: the other is free decay, which §3's figure of merit carries explicitly as `λ_0/λ_c`. Condition 8 omits it deliberately. A binder that also decays completes *fewer* cycles than `1/ω_s`, so the right-hand side is a ceiling on what one binder can return and the condition is **necessary** rather than sufficient — which is the direction that matters here, because every verdict this paper reaches on condition 8 is negative, and a negative verdict against a generous bound is stronger than one against a tight bound.

Condition 8 is therefore not an efficiency target that might be approached with better engineering but an accounting identity, and it contains no fitted quantity: `Q_fus` and `ω_s` are measured, `E_binder` is integrated in §5.1 from measured cross sections, and `f_work` is computed from a stated operating point and carried in both of its conventions rather than chosen. Proposition 1 in §14.2 derives it, including the two distinct reasons the cycle bound is never attained.

There are two conventions in use for `f_work`, and this paper carries both rather than choosing. Counted as heat delivered, the bound is 7.52 GeV; counted as electrical work recoverable from that heat, it is 3.77 GeV. A figure quoted without saying which convention produced it cannot be checked, so every balance below is labelled with its own.

**Against a sourced production-and-capture cost of 37.0 GeV per captured μ⁻**, the figure of merit is 0.203 as heat and 0.102 as work. That is the state of the question as the literature leaves it.


### 4.1 Sticking is binder-mass independent, so condition 8 is a specification

Sticking is the probability that the muon leaves the fusion bound to the alpha particle and is lost from the cycle. Of the binder's two loss channels it is the larger at the cycle rates this reaction runs at, and it is the one most attempts at improvement have aimed at — the other, free decay, is a property of the muon and cannot be aimed at at all.

It cannot, however, be improved by changing the binder, and the reason is that the binder's mass cancels out of the overlap integral that defines sticking. A heavier binder sits in a tighter orbit, but the momentum scale of that orbit rises in exact compensation, and the two changes cancel in the one combination the capture depends on. The recoil the binder must escape is set by the fusion kinematics and does not involve the binder at all. Theorem 2 in §14.4 gives the proof.

The consequence is larger than the calculation. Since no admissible binder does better, condition 8 cannot be satisfied by looking for a different particle; it is a specification on the *machine* rather than a search over the *spectrum*. And §2's window has already shown that there is no other occupant to search for in any case.

**The measured values then decide the heat form, and they decide it against.** At the production cost §5.1 measures, the heat form of condition 8 would be met at perfect collection only if the sticking were below 0.1580 percent. The two published final stickings — 0.45 percent from SIN and 0.56 percent from PSI — are both well above that, and so are the two effective values, 0.5050 percent and 0.5320 percent, that the measured reactivation returns. **The break-point does not lie between the two readings; it lies below both.** The heat form reaches 0.31 of what it needs on the more favourable of them and is short by a factor of 3.37 on the other, and no choice between them repairs it.

The consequence is worth drawing out, because it redirects the whole enquiry. If the two readings had straddled the break-point, a single bench measurement would have decided whether the reaction can pay for itself as heat. They do not, so it cannot. What the two readings differ about is a few percent of the service life; what decides the balance is the cost of the binder and the fraction of them collected — which is where §5 and §6 go, and why the acceptance is the first thing worth measuring. §11's protocol still runs, because the two routes to sticking disagreed historically and the operative value is worth pinning, but it settles a term rather than the question.


## 5. What the binder costs, measured rather than assumed

The figure of merit given above rests on 37.0 GeV per captured μ⁻, which is a sourced end-to-end number for a machine that was built for an entirely different purpose. That is a fair starting point but a weak one to argue from, since a reader may reasonably reply that a machine designed for this job would do better. This section therefore replaces it with a floor computed from the production physics alone, which no collector can argue away.


### 5.1 Production, integrated from measured cross sections

Pion production has been measured double-differentially, so obtaining the yield is a matter of integration rather than of modelling. Over the large-angle acceptance — 0.35 rad to 2.15 rad in angle, momenta up to 0.80 GeV/c, at a beam momentum of 8 GeV/c — the integrated π⁻ cross section on a heavy target is 1.0382 barn, which corresponds to 0.6107 π⁻ per proton. The forward acceptance, 0.025 rad to 0.25 rad, adds a further 0.1838 barn, which is 0.1081 π⁻ per proton — the two acceptances are quoted in different units in the source tables, so the cross sections do not add to the yield and the conversion is stated rather than left to the reader. Taken together the production is 0.7188 π⁻ per proton, and at the beam energy in question that works out at 11.13 GeV per pion. Proposition 7 in §14.6 sets out the integral.

> This settles the first question a reader is likely to ask. 11.13 GeV is what a pion costs before any collector exists at all, so it is a floor on the binder's cost. Set against the heat bound of 7.52 GeV, even a *perfect* collector — one in which every pion produced became a stopped binder, which no machine approaches — would leave the heat form short. **The gap is not in the collector**, and no improvement to it can be the answer.

It is worth noting which hemisphere carries the yield, because a common argument turns on it. The machine that has been built captures the **forward** hemisphere, and it is sometimes suggested that a reactor could gain a large factor by capturing the backward one as well. Run through the acceptance model of §6.1 that gain is 1.20 — worth having, and not a factor of several. The two acceptance windows the integration above uses are not hemispheres and should not be read as though they were: the forward window contributes 15 percent of combined production, while the backward sliver is 35 percent of the *measured acceptance*, which is a different denominator.


### 5.2 Three results that move the balance

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


## 6. The collector, and the number that decides it


### 6.1 What sets the acceptance

A capture solenoid accepts a pion if its transverse momentum lies below `p_T = 0.15 · B · R`. Because field and bore appear only as a product, the two trade against one another at fixed acceptance, and it is the product `B·R` — not the field on its own — that sets what the magnet can take. Proposition 4 in §14.5 derives this, together with the factor of two that makes the beam envelope twice the gyroradius. The best studied front end runs 20 T on a bore giving an aperture product of 1.50 T.m; the collector specified here would need 2.60 T.m, a factor of 1.735 — and Corollary 9.1 in §14.7 is why that factor is not free: the beam widens with the bore, so the fuel target's tritium inventory rises as its square.

With that in hand the acceptance becomes a calculation rather than an assumption. It is built up in four steps: the production spectrum, the transverse cap above, the two-body pion decay integrated over the pion rest frame, and finally whatever momentum requirement the downstream apparatus imposes. Run over the configuration of the machine that has actually been built, the model returns 29.51 percent against that machine's own published simulation, the two agreeing to 0.982.

> **The acceptance model is therefore validated against an independent simulation of a machine that was built**, rather than against the assumptions that produced it, and that is what licenses the acceptance figures below.

Run over a reactor's configuration, at today's aperture and accepting both hemispheres, the model gives 60.92 percent with no momentum requirement and 44.43 percent through a stopping window of 265 MeV/c.


### 6.2 An acceptance is not a delivered efficiency

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

**The delivered acceptance is therefore 31.66 percent** at today's aperture, or 37.62 percent at the wider bore — against the 90 percent [DESIGN] figure at which the preprints at [18] read them, and which §7 restates every one of them away from.

![Figure 1](papers/figures/fig5-budget.png)

**Figure 1.** What becomes of a hundred pions made in the target. Each step is a loss that can be computed rather than assumed, and the product of them is the difference between what the magnet accepts and what the fuel actually stops.


## 7. Every balance, at the acceptance delivered and the sticking the record supports

Two corrections stand between the figures the preprints at [18] printed and the ones below, and it is worth taking them in order because the second is the larger.

**The first is the acceptance**, and §6.2 has just made it. The second is the **service life**, and it comes from the preprints' own later sections rather than from anything new here. Every balance printed there was computed at one of two service lives: the **measured** 150 cycles per binder, and a modelled "bound case". Reading the printed table backwards through the balance — Proposition 1 in §14.2 fixes its form, and the table's own columns check it — the bound case is 588.9 cycles. That is the model run at an effective sticking of 0.1487 percent [WITHDRAWN], a value formed by multiplying an excited-state initial sticking by a survival fraction measured on the **ground** state — two different states. Fusion occurs from the ground state, and the record's own measured values are 0.5050 percent and 0.5320 percent; at the favourable one the same density returns 190.1 cycles instead of 588.9. **Every bound-case figure in the record is therefore high by a factor of 3.10.**

> **The rows computed at the measured cycle count are untouched by that**, because they never used the model at all — and that asymmetry, more than any other single fact in this paper, decides which route survives.

Restating is exact rather than approximate: the balance is linear in collection (Proposition 6 in §14.5) and proportional to the service life, so each cell below is one multiplication. The left column is the machine as built; the right is the same machine with both collector alterations of §7.1 — the wider bore and the wider stopping window — which together deliver 48.61 percent.

| balance | delivered, as built, 31.66 percent | with both collector alterations, 48.61 percent |
|---|---|---|
| heat, at the measured 150 cycles | 0.111 | 0.171 |
| heat, the model at 8.5 × liquid | 0.141 | 0.216 |
| heat, the model at φ = 3 | 0.131 | 0.201 |
| work, at the measured 150 cycles | 0.083 | 0.128 |
| work, the model at 8.5 × liquid | 0.106 | 0.162 |
| **bred fuel, at the measured 150 cycles** | 0.623 | **0.957** |
| bred fuel, the model at 8.5 × liquid | 0.790 | 1.212 |

> **Nothing clears unity with the machine as built**, and the closest is bred fuel at the measured cycle count, at 0.623. **With both collector alterations that route reaches 0.957** — short of unity by a factor of 1.045, and short of it by no other term than the loss budget, which is the one quantity in the whole column that has never been measured. The figures reported at ninety percent collection in the preprints at [18] are withdrawn as end-to-end results, and so are the bound-case figures that rest on the superseded sticking. Each stands as the conditional it was stated at.


### 7.1 What the specified alterations do to every balance

§7 states the balances at the production cost §5.1 measures. A third alteration is specified in this paper — an **optimised production target** — and unlike the two collector alterations it does not change the collection at all. It moves `E_binder`, and because a balance has the form `N · V · η / E_binder` it therefore multiplies **every** balance by the same factor: from 11.13 GeV to 4.69 GeV, which is worth 2.373. Corollary 6.1 in §14.5 makes this explicit.

> **The factor checks against the requirement it moves.** §5.2 puts bred fuel at the measured cycle count at 50.8 percent collection; through the optimised target that requirement is 21.4 percent, and 50.8 ÷ 2.373 returns it.

| balance, through the optimised target | delivered, as built | with both collector alterations |
|---|---|---|
| heat, at the measured 150 cycles | 0.264 | 0.405 |
| heat, the model at 8.5 × liquid | 0.334 | **0.513** |
| work, at the measured 150 cycles | 0.198 | 0.304 |
| work, the model at 8.5 × liquid | 0.251 | 0.385 |
| **bred fuel, at the measured 150 cycles** | **1.480** | **2.271** |
| bred fuel, the model at 8.5 × liquid | 1.874 | 2.877 |

![Figure 2](papers/figures/fig4-range.png)

**Figure 2.** The range the reaction is expected to fall in. Each row is one way of pricing the same reaction; the bar runs from what the machine as built delivers to what it delivers with all three alterations. Anything reaching the line at unity pays for itself. Only bred fuel does, and the rows at the measured cycle count use no service-life model at all.

**Two things fall out of that table, and the second qualifies the first.**

> **No heat form and no work form clears unity anywhere in this paper.** The largest either reaches is **0.513**, and it is reached only by granting, simultaneously, the optimised production target, the wider bore, the wider stopping window *and* a fuel density of 8.5 × liquid that no experiment has held. **A device that returns its energy as heat or as work is not self-sustaining on anything this paper can construct**, and that is a closed statement rather than an open question: Theorem 3 in §14.4 shows the same thing from the other direction. **Bred fuel is the one row that crosses unity, and it crosses only through the optimised target.** At 1.480 with that target alone and **2.271** with all three alterations, the row uses **no service-life model, no density above the one already reached, and no choice between the two sticking measurements** — its inputs are the 150 cycles measured at Los Alamos, the sourced blanket of §5.2 and the collection the machine of §10 delivers. **But it does not cross on this paper's own production cost.** At the 11.13 GeV §5.1 integrates, the same route reaches 0.623 as built and 0.957 with both collector alterations, short of unity by a factor of 1.045; **everything above unity in the table above is bought by the 4.69 GeV optimisation**, which this paper prices and declines to adopt.

**Which half of that table is this paper's, and it is the first.** 4.69 GeV is a *published* optimisation of the production target, worth a factor of 2.373 on every balance; §5.1 integrates 11.13 GeV from measured cross sections and that is the figure this paper stands behind. The two are a discrepancy §12 records and does not close, and a normalisation measurement on one target — pions per beam particle against pions per interaction, nothing else changed — is what would settle it. **Until it is made, the reading this paper offers is the first column: the best route reaches 0.957 against the unity it must clear, falls short by a factor of 1.045, and falls short by no term other than a loss budget nobody has measured end to end.**


---


## 8. A deuterium cell does not stay a deuterium cell

§3 ranked the pairs as though a cell could be charged with one of them and left alone. It cannot, and the exception is worth a section because it is the only route by which this reaction's tritium liability falls by more than a rounding.

One branch of the *d*–*d* reaction makes tritium. `d + d → t + p` runs at very nearly half of all *d*–*d* events, and *dtμ* forms some eighty times faster than *ddμ*, so tritium produced in a deuterium cell is consumed preferentially the moment it exists. **A deuterium cell therefore tritiates itself**, and it does so until production balances burn. That is not a choice available to the designer; it is what the cell does.

The balance is one line. Writing `f_dt` and `f_dd` for the shares of fusions that run on each pair, production is `½ f_dd` per fusion and consumption is `f_dt`, so

> `½ f_dd = f_dt` with `f_dd + f_dt = 1`, giving **`f_dt` = 0.3333** and `f_dd` = 0.6667,

and the tritium concentration that produces that split follows from the two formation rates. Proposition 11 in §14.8 carries the derivation. The result is the number this section exists for.

| at the equilibrium |  |
|---|---|
| tritium, atom fraction | 0.6211 percent |
| tritium, mass fraction | 0.9273 percent |
| cycles per muon | 3.51 cycles |
| energy per fusion | 8.297 MeV |
| energy per muon | 29.09 MeV |
| neutrons per muon | 2.337 neutrons |

> **A cell that makes its own tritium holds a factor of 64.71 less of it** than the *d*–*t* cell §9 specifies — a percent rather than half — and it needs no external tritium, no lithium and no breeding blanket to hold that inventory against decay. **What it costs is the reaction's yield, by a factor of 48.38 in neutrons per binder.**

**Two things are not claimed here.** The equilibrium above is a first-order balance between two formation rates and two branching ratios, and it is offered as a quantity to measure rather than as a result to build on. And it runs against a known effect this paper does not compute: the other *d*–*d* branch makes ³He, muon transfer to ³He is fast, and ³He is an established poison in deuterium cells. Counting it would lower every entry in the table above by an amount only a measurement can fix.

**The reaction is the same reaction.** The binder is the muon, §2's theorem is untouched, the cycle is the cycle, and the ash is the ash the branching ratios fix. What changes is the charge in the cell — which is to say that §3's ranking answers *which pair returns most per binder*, and this section answers a different question that the ranking cannot see.


## 9. The reaction, specified

This section states **what must be procured, built or assayed** to run the reaction. Every free parameter is fixed from a witnessed measurement, and each row states why it is fixed there rather than being asserted.

**The event.**

> μ⁻ + (d, t) → (dtμ)⁺ → ⁴He + n + μ⁻ + 17.59 MeV

The binder is not consumed. It is released and forms the next muonic molecule, and the cycle repeats until the muon decays or is lost to the alpha.

![Figure 3](papers/figures/fig1-cycle.png)

**Figure 3.** The catalytic cycle, and the two ways it ends. A single binder repeats the loop until it decays or is lost to the alpha; everything the paper prices is a consequence of how many times it goes round.


### 9.1 Every free parameter, fixed

| parameter | value | why it is fixed there |
|---|---|---|
| fuel | deuterium–tritium | Theorem 4 — it maximises the energy returned per binder over the closed candidate set, and by Corollary 4.1 no rival can be made to catch it |
| ratio | 50/50 by number | not critical; the transfer step auto-optimises the population |
| **purity** | better than 1 ppm [DESIGN] high-Z | transfer to a contaminant runs at 1.0 × 10^10 s^-1 at 1 LHD of oxygen; at the bracketed density 5.49 ppm costs as much binder as decay does |
| temperature | 800 K | the Vesman resonance transfers the *dtμ* loose state's 0.66 eV into a 0.365 eV host vibrational quantum |
| **cycle-rate ceiling** | 2.6 × 10^8 s^-1 | the cycle is a harmonic sum, so driving the resonance moves the bottleneck to transfer, capped at 2.7 × 10^8 s^-1 |
| density | as high as the cell reaches | the cycle rate scales with it; the service life does not, being capped by sticking |
| **binder** | **μ⁻**, the negative muon | §2 — the positive one forms muonium and catalyses nothing at any density or temperature |
| binder source, to witness | an existing muon beam | no new machine is required to witness the reaction |

> **The binder is not "a muon"; it is the negative one, and it has exactly one parent — π⁻ decay.** Every yield in this paper is a π⁻ yield for that reason, and §9.3 carries the consequence into what the production target must be made of.


### 9.2 The two observables, and they must be simultaneous

| observable | what it counts |
|---|---|
| neutrons at 14.1 MeV | fusion events, hence cycles per binder |
| the muonic-helium K-alpha at 8.2 keV | binders stuck to the alpha, hence the sticking directly |

![Figure 4](papers/figures/fig7-measurement.png)

**Figure 4.** The step the existing experiments do not take. Both observables watch the same fuel at the same time, on one fill, so the cycle count and the loss are measured together rather than inferred from separate runs.

**They share no instrument and no calibration**, which is what makes them two routes rather than one. §11.4 commits in advance to treating a disagreement between them as a **refusal** rather than as an average.


### 9.3 Bill of materials

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
| **production target** | none | high-Z, and a **free liquid-metal jet** — §10.3 |
| neutron detection | array calibrated at 14.1 MeV | — |
| X-ray detection | resolving 8.2 keV, viewing the same sample volume | — |
| blanket, as a **breeder** | none | ⁶Li-bearing, 1.6 neutron energy multiplication, fission-suppressed |

**The production target's material is set by the charge, not only by the yield.** Measured off the production tables for both signs, a lead target returns a π⁻/π⁺ ratio of 0.973 against aluminium's 0.732 — a factor of 1.329. At equal *total* charged-pion yield a low-Z target therefore delivers less of the sign that can catalyse, and the low-momentum π⁻ excess a collector's window sits in appears in the heavy targets and not in the light ones at all. **The requirement was previously met without being stated**, and a specification that does not state it could be met by a target that fails it.


### 9.4 What is witnessed here, and what is not

**The reaction is witnessed.** It has run in laboratories since the 1950s; the highest yield on record is 150 cycles per binder, and the final sticking has been observed directly in two independent experiments — 0.45 percent at SIN and 0.56 percent at PSI — from which the measured reactivation gives the two effective values §4.1 works with.

**What is unwitnessed is this configuration** — that fuel, at that purity, at 800 K, with **both observables running on one target at once.** No experiment has held all of those at the same time. That is the whole of what §9 to §11 are for.


---


## 10. The machine that supplies the binders

A procedure that would witness the *net-positive* configuration needs a machine capable of supplying binders at the required rate, and no such machine has been built. This section designs it. The design follows from the collection model of §6 rather than being introduced independently, so that the two cannot drift apart.

![Figure 5](papers/figures/fig2-machine.png)

**Figure 5.** The binder source, and the three alterations this paper proposes to it. The machine below the line is the one that has been built and simulated; the three callouts above it are what this paper would change, and each is priced in the text.


### 10.1 What the aperture fixes

The transverse cap is `p_T = 0.15 · B · R`, so **field and bore trade against each other at fixed capture**. Holding the built front end's aperture of 1.50 T.m and taking the peak field to 20 T at an upstream plug, the target field is 14.01 T and the warm bore is 10.7 cm — against a delivered beam envelope at the target of 10.71 cm, which is what a particle born on axis reaches at twice its gyroradius.

**The bore is derived rather than chosen**, and the same derivation reproduces three published geometries that were not used to build it: 7.50 cm, 30.0 cm and 13.0 cm.


### 10.2 The mirror, and why the grade is a specification

A magnetic mirror will reflect a pion emitted into the backward hemisphere provided its pitch angle satisfies `sin θ ≥ √(B_target / B_max)`. The grade required to reach every angle the production data covers is therefore fixed by that data's own angular limit, and it comes to a field grade of **1.428** — no more, because that is simply where the measurement ends. Proposition 5 in §14.5 derives the condition from the adiabatic invariant.

> This has the same shape as §4.1's finding about sticking: a parameter that had looked like a lever turns out on inspection to be a requirement with a number attached to it. One consequence is worth noting — mirroring the backward hemisphere and simply accepting both hemispheres come to the same number, which is why §6.1's acceptances are stated over both.


### 10.3 The circuit, the cold mass, and the constraint that decides the target

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

![Figure 6](papers/figures/fig3-target.png)

**Figure 6.** Why the production target must be a free liquid-metal jet. The capture field sets the bore, the bore sets the space the target may occupy, and the rotating solid wheel that every megawatt-class facility uses does not fit inside it.


### 10.4 The fuel cell, and where it can sit

The fuel cell cannot sit in the capture region, and where it does sit has a cost. The decay channel is 34.1 m long at the stopping window, and the beam must then be recompressed to 20 T at the cell if the fuel is to intercept it. It is that recompression which sets the tritium inventory at 5.13 kg, rather than the 10.79 kg a wider bore would require.

One point about that inventory is easily missed and is worth stating plainly: it does not fall with compression. Because the target must be one muon range deep, its tritium content is the areal density multiplied by the beam area. Compressing the fuel raises the density and shortens the target in exact proportion, so density buys length rather than inventory. Proposition 9 in §14.7 gives the argument.


---


## 11. The laboratory procedure

This section is the procedure that would witness the configuration §9 specifies. **Standing conventions**, and they are committed before any run: a null is a bound, so every step is written to yield a number even when it fails; a disagreement between the two observables is a **refusal, not an average**; and every prediction is committed before the measurement, so neither can be adjusted afterwards.


### 11.1 Assembly

1. Build the target cell to hold 19.2 mm3 at up to 933 MPa and up to 500 K. Braze diamond to metal; use no polymers anywhere the fuel touches, and construct everything past the permeator from tritium-compatible material.
1. Enclose the gas system in a helium glovebox at negative pressure, with continuous cleanup and secondary containment on every uranium bed.
1. Mount the cell on a stage that translates it into and out of the beam axis without breaking containment.
1. Site the neutron array and the X-ray detector so that **both view the same sample volume at the same time.** This is the step the existing experiments do not take, and it is the point of the procedure.

### 11.2 Loading

1. Bake the system, then flush twice with ultra-pure deuterium.
1. Desorb D–T from a uranium bed, assay it in a calibrated ionisation chamber, and condense it through the permeator into the cell. Expect about 4 mg of fuel and 23.2 Ci of tritium at 50/50.
1. Confirm the fill optically through the anvils and verify composition by in-situ Raman before any beam. **Purity is a variable of this experiment, not a precondition** — record it, do not assume it.
1. Close the cell, take it to pressure, and bring it to the setpoint temperature.

### 11.3 The measurement

1. Admit the muon beam, tuned to stop in the fuel rather than in the anvils.
1. Acquire neutrons at 14.1 MeV and the 8.2 keV K-alpha **simultaneously, on one fill.**
1. Repeat across a **purity series** at fixed density and temperature. The existing record confounds purity with density and temperature — its cleanest data are also its coldest and densest — and this series is what separates them.
1. Repeat across a **density series** at fixed purity, and a **temperature series** toward the 800 K operating point.

### 11.4 What each outcome settles, committed in advance

| quantity | what this paper predicts | what it settles |
|---|---|---|
| cycles per binder | of order 150 cycles, ceiling 198 cycles | the service life, and whether the sticking cap is real |
| effective sticking, X-ray route | 0.5050 percent to 0.5320 percent | the operative loss term |
| effective sticking, neutron route | the same, within error | **if the two disagree, report a bound — do not average** |
| purity dependence | binder loss rising linearly in high-Z contamination | separates purity from temperature and density |
| temperature dependence | cycle rate rising toward 800 K, then flat | tests the ceiling that transfer imposes |

**A null at any step is a bound.** A cycle count below 150 cycles bounds the service life from above. A disagreement between the two sticking routes is a refusal, and the correct output is an interval. An absent purity dependence means the impurity channel is smaller than modelled, and every balance in §6 improves by a stated factor.


---


## 12. Limits, and what this paper does not claim

Each item below is a limit on what the foregoing establishes. None of them is resolved by argument in this paper, and where a measurement would settle one, that measurement is named. §14.9 lists the three that bear most directly on the results.

**The operative sticking is unresolved between two measurements**, though not in a way that changes the heat form's verdict. 0.5050 percent and 0.5320 percent are the two effective values the measured reactivation returns, and both lie above the break-point at 0.1580 percent, so the heat form fails at perfect collection on either. What the disagreement leaves open is the service life, and with it every balance that depends on it. §11's protocol settles it, and nothing here stands in for that.

**Every collection figure here is an acceptance rather than a delivered efficiency** until an end-to-end count of stopped binders per pion produced has been made. §6.2 computes the losses between the two and §7 restates every balance through them, but a computed budget is not a measurement, and the margin over the falsification floor is 1.073.

**The fuel scan's cycle rates and stickings are literature bands, not one measurement each.** They are measured for *d*–*t*, *d*–*d* and *t*–*t* and order-of-magnitude for the pairs that catalyse almost nothing, and §3's table prints them as they stand. Corollary 4.1 bounds what that costs: the ranking survives every competitor's cycle rate being sent to infinity, so only the stickings are load-bearing, and a competitor would have to be a factor of 24.58 less sticky than the record says before the ordering could move. What the bands do reach is the *size* of the margins quoted in §3, not the order of the table.

**Every balance assumes perfectly pure fuel.** At the bound case, 5.49 ppm of high-Z contamination costs as much binder as decay does. The purity series of §11.3 is what measures it.

**The temperature axis is confounded in the existing record.** The cleanest published data are also the coldest and densest, so temperature, purity and density cannot be separated from what exists. That is a fault in the record rather than in the reaction, and §11.3 is written to separate them.

**Every modelled service life here rests on a density no experiment has reached**, and after §7's correction it buys very little. The model itself is in good order — at the density that *has* been reached it returns 152.8 cycles against the 150 cycles measured, a ratio of 1.019 — but the rows that use it assume 8.5 times liquid where 1.2 has been held, and even granted that they return only 190.1 cycles against 150 cycles measured. **The model is worth a factor of about a quarter and an unreached density to obtain it**, which is why every result this paper offers is stated at the measured count, and why §7's surviving route uses the model nowhere.

**The optimised production target is a discrepancy that cannot be closed by argument.** A published optimisation costs 4.69 GeV per pion against the 11.13 GeV integrated in §5.1. Three candidate mechanisms were examined and bounded; what survives is a **normalisation** — pions per beam particle against pions per interaction — needing 2.389 interacting nucleons, which reproduces the optimised figure closely and which a deuteron on a long target supplies. **A normalisation measurement on one target would settle it: pions per beam particle against pions per interaction, with nothing else changed.**

**And the standalone configuration is closed rather than open.** Theorem 3 in §14.4 is a theorem, and no measurement in §11 can overturn it. What a measurement can decide is the bred-fuel route, which is the one this paper leaves standing, and the production cost that route turns on.


---


## 13. What is proved

Each of the following is a theorem or a derivation from measured inputs. None of them depends on a measurement this paper proposes, and none can be overturned by one.

1. **A cold fusion reaction exists and has been witnessed.** The definition of §1 is structural, and the reaction it picks out has run in laboratories since the 1950s. Its cycle rates, its sticking fractions and its ash have all been measured.
1. **The binder is unique.** The seven conditions place a floor and a ceiling on the binder's mass, and the window between them, 119 electron masses to 918 electron masses, has exactly one occupant in the charged spectrum (Theorem 1, §14.3). Of 13 charged particles scanned, 5 outlive the mesomolecular formation time, 2 lie inside the window, and one survives the hadron test.
1. **The fuel is unique.** Over the closed set of pairs a muon can bind, *d*–*t* maximises the energy returned per binder by a factor of 77.85 against the next candidate (Theorem 4, §14.8) — and the runner-up uses more tritium rather than less. **That ranking is not a near thing either**: it survives every competitor's cycle rate being sent to infinity, leaving *d*–*t* ahead by a factor of 24.58 (Corollary 4.1).
1. **The window is not a near thing.** Its lower bound may move by a factor of 207 and its upper by 3.54 before the count of occupants changes.
1. **An eighth condition decides whether the reaction is worth running**, and it contains no free parameter and no fitted one (Proposition 1, §14.2). Two of its terms are measured, one is integrated from measured cross sections, and the fourth is a conversion fraction computed at a stated operating point and carried in both of its conventions.
1. **Sticking does not depend on the binder's mass** (Theorem 2, §14.4), so condition 8 is a specification on the machine and not a search over the spectrum. There is in any case no other occupant of the window to search for.
1. **The production floor is measured rather than modelled.** Integrating the published double-differential cross sections puts production alone at 11.13 GeV per pion, which is a cost no collector can argue away.
1. **The acceptance model is validated against an independent simulation** of a machine that was built, agreeing to 0.982.
1. **The standalone configuration is closed** (Theorem 3, §14.4): at the production floor, no admissible binder pays for itself as heat at any collector. The break-point sits at 0.1580 percent and lies **below both** published sticking readings, so no choice between them repairs it.
1. **Nothing clears unity at this paper's own production cost.** The closest is bred fuel at the measured 150 cycles, at 0.623 as built; with both collector alterations of §7.1 it reaches 0.957, short of unity by a factor of 1.045 and short by no term other than the loss budget, which is the one quantity in the column that has never been measured.
1. **One route does cross unity, and it crosses on a figure this paper declines to adopt.** Through a *published* optimisation of the production target at 4.69 GeV — worth a factor of 2.373 on every balance against the 11.13 GeV §5.1 integrates — bred fuel at the measured cycle count reaches 1.480, and 2.271 with all three alterations. **That factor is a discrepancy §12 records and does not close**, so the route is reported and not claimed, and a normalisation measurement on one target is what would settle it.
> **The reaction is proved and it is witnessed. Its binder is unique, its fuel is unique, and its energy account is closed in the sense that every term in it is named and priced. What is not proved is that any device-internal configuration of it returns more than it costs at a production cost this paper is willing to stand behind** — §7 states how far short the best one falls, and the item immediately above states the one route that crosses and whose figure it crosses on. That is the whole of the claim, and no part of it is larger than the evidence behind it.

**What this paper does not do.** It does not price the configuration in which the binder is a byproduct of a beam already running for another purpose, and it does not price a blanket. Both change the accounting rather than the reaction, both are the subject of a separate paper, and neither is needed for anything claimed above.


## 14. The mathematics, in full

The body of the paper states results and points at where they come from. This section carries the derivations themselves, so that each may be checked without reconstructing it. **Where a statement is a theorem it is proved; where it is a derivation resting on measured inputs, it is labelled a proposition and its inputs are named.** Nothing is called proved that is not.


### 14.1 Notation

| symbol | meaning |
|---|---|
| $m_b$ | the mass of the binding particle, in electron masses |
| $a_b$ | the radius of the binder's orbit about a nucleus |
| $R_{dt}$ | the internuclear separation in the bound state |
| $\lambda_f$ | the fusion rate from the bound state |
| $\lambda_0$ | the binder's free decay rate |
| $\lambda_c$ | the cycle rate: fusions per unit time from one binder |
| $\omega_s$ | **sticking**: the probability, per cycle, that the binder is lost to a fusion product. It is one of the binder's two loss channels; the other is free decay, carried as $\lambda_0/\lambda_c$ |
| $N$ | the service life: the number of fusions one binder catalyses |
| $Q_{fus}$ | the energy released per fusion |
| $f_{work}$ | the fraction of that release recovered in the form being paid in |
| $V$ | the value of one fusion, $Q_{fus}\,f_{work}$ |
| $E_b$ | the energy cost of producing and capturing one binder |
| $\eta$ | the collection efficiency: stopped binders per pion produced |
| $E_\pi$ | the energy cost of producing one pion |


### 14.2 The eighth condition, derived

**Proposition 1 (the cycle identity).** *A binder is worth making if and only if*

> $E_b \;<\; N\,Q_{fus}\,f_{work}$, *and since* $N \le 1/\omega_s$, *the necessary condition is* $E_b < Q_{fus}\,f_{work}/\omega_s$.

*Derivation.* The catalytic cycle has no input per event: the binder is not consumed by the fusion, and no energy is supplied to the fuel to bring the nuclei together, that work being done by the bound state. The only input is therefore the binder itself, at a cost $E_b$. A binder that catalyses $N$ fusions returns $N\,Q_{fus}\,f_{work}$, so the account closes exactly when the return exceeds the cost.

For the bound: let $p$ be the probability that the binder survives one complete cycle against sticking, so $\omega_s = 1 - p$. The number of cycles is geometrically distributed and its expectation is $N = p/(1-p)$, which is exactly one cycle short of $1/\omega_s$ — so the cap is attained neither at any $\omega_s$ nor in the limit, and it is tight to a relative error of $\omega_s$ rather than absolutely.

That is the first of two reasons $N < 1/\omega_s$, and the smaller one. The second is that sticking is not the binder's only loss channel: it also decays, at a rate that does not care whether a cycle is in progress, and Proposition 10 in §14.8 carries both losses together as $N = 1/(\omega_s + \lambda_0/\lambda_c)$. Both effects run the same way, so $1/\omega_s$ remains an upper bound and condition 8 remains **necessary**. **The cap is never attained**, which is why §7 distinguishes the demonstrated cycle count from the bound. ∎

**Remark.** The inequality is an accounting identity rather than an efficiency target: it contains no free parameter and no fitted one. Two of its terms are measured, one is integrated from measured cross sections in §5.1, and the fourth is a conversion fraction computed at a stated operating point and carried in both conventions; §4 gives the values.


### 14.3 The structural window on the binder mass

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

**This matters for what §14.3 does and does not establish.** The bounds themselves are carried from the earlier treatment and are not recomputed here; Propositions 2 and 3 give the scaling arguments that produce them but not the numerical crossing. Corollary 1.0 is what makes that acceptable: the theorem's conclusion survives an error of two hundred in the lower bound and three and a half in the upper.

**Corollary 1.1.** *Every yield in this paper is a $\pi^-$ yield*, and the production target's material is constrained by the charge ratio it returns and not only by its total yield — which §9.3 states as a specification.


### 14.4 Sticking does not depend on the binder's mass

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

> *Proof.* By Theorem 1 the structural window has exactly one admissible occupant, so $\omega_s$ is the muonic value and $N \le 1/\omega_s$ is the bound it sets. $Q_{fus}$ and $f_{work}$ are properties of the fuel and the plant, not of the binder — and the fuel is not a free choice either, since by Theorem 4 no other admissible pair returns as much per binder, and by Corollary 4.1 none can be made to. The right-hand side of Proposition 1 is therefore fixed on both axes rather than on one. The left-hand side, $E_b$, is bounded **below** by the cost of producing the parent particle, which §14.6 puts at 11.13 GeV per pion and which no collector can reduce. Taking the most favourable admissible values of every term simultaneously, the best balance available is 0.807 — less than unity.

>

> That closes the configuration for the muon. It closes the *search* as well, and this is where Theorem 2 does its work: to leading order $\omega_s$ carries no dependence on the binder's mass at all, so a hypothetical occupant elsewhere in the window would inherit the same bound rather than improve on it. The residual priced above runs toward less sticking only for a **heavier** binder, and the window's one heavier candidate is a hadron, excluded by conditions 3 and 4 before its sticking is ever consulted. **The configuration is therefore closed by the structure of the window rather than by any measurement**, and no experiment in §11 can overturn it. ∎

**Remark.** Theorem 3 is what makes the co-product configuration the interesting one: it does not contradict the theorem, because it does not pay for the binder at all.


### 14.5 The collector

**Proposition 4 (the aperture product).** *A solenoid of field $B$ and clear radius $R$ accepts a pion of transverse momentum up to $p_T^{max} = 0.15\,B\,R$, in T, m and GeV/c; hence field and bore trade against one another at fixed acceptance, and only their product matters.*

*Derivation.* A particle of transverse momentum $p_T$ in an axial field $B$ has gyroradius $r_g = p_T/(0.3\,B)$ in the same units. A particle born on the axis reaches a maximum distance $2 r_g$ from it, so it is contained if $2 p_T/(0.3 B) \le R$, which rearranges to the stated cap. **The beam envelope is therefore $2 r_g$ and not $r_g$** — a factor of two that also fixes the bore of the fuel cell, and which is validated in §10.1 against three published geometries the derivation did not use. ∎

**Proposition 5 (the mirror condition and the grade it requires).** *A pion emitted into the backward hemisphere at pitch angle $\theta$ is reflected forward by a field rising from $B_t$ to $B_{max}$ if and only if* $\sin\theta \ge \sqrt{B_t/B_{max}}$. *The grade sufficient to reflect every angle the production data covers is therefore* $B_{max}/B_t = 1/\sin^2\theta_{max}$, *which is* 1.428.

*Derivation.* In a slowly varying axial field the magnetic moment $\mu = p_\perp^2/2mB$ is an adiabatic invariant and the kinetic energy is conserved, so $p_\perp^2/B$ is constant along a trajectory. A particle turns where $p_\perp = p$, that is where $B = B_t/\sin^2\theta$. It is reflected before reaching $B_{max}$ exactly when $B_t/\sin^2\theta \le B_{max}$, which is the stated condition. Taking $\theta_{max}$ as the largest angle the production measurements cover gives the grade, and **because the data end there, so does the requirement**: the grade is fixed by the measurement rather than chosen. ∎

**Proposition 6 (linearity in collection).** *Every balance in this paper is proportional to $\eta$, so restating one at a different collection efficiency is exact rather than approximate.*

*Derivation.* Write the balance as $G = N\,V\,\eta/E_\pi$. Here $N$ is a property of the fuel and the sticking, $V$ of the plant, and $E_\pi$ of the production target; none of them depends on $\eta$. Hence $G \propto \eta$ and $G(\eta_2) = G(\eta_1)\,\eta_2/\eta_1$ identically. The tables of §7 are computed this way, and the two-column table the preprints at [18] printed at thirty and ninety percent collection provides the check: every row's ratio lies between 2.998 and 3.010, against an exact three. §7's own two columns are the delivered figures 31.66 percent and 48.61 percent, which are not in that ratio and are not the fixture. ∎

**Corollary 6.1.** *An alteration that changes $E_\pi$ alone multiplies every balance by the same factor* $E_\pi^{old}/E_\pi^{new}$. This is what §7.1 computes, and the same corollary explains why that factor moves the bred-fuel requirement from 50.8 percent to 21.4 percent.


### 14.6 The production floor

**Proposition 7 (the floor on the binder's cost).** *Production alone costs* 11.13 GeV *per pion, and no collector can reduce it.*

*Derivation.* The pion yield per interacting proton is obtained by integrating the measured double-differential cross section over the acceptance, with the solid-angle Jacobian:


$$Y \;=\; \frac{1}{\sigma_{inel}} \int_{\theta_1}^{\theta_2}\!\!\int_{0}^{p_{max}} \frac{d^2\sigma}{dp\, d\Omega}\; 2\pi \sin\theta \; dp\, d\theta .$$

Over the large-angle acceptance this gives 1.0382 barn, or 0.6107 π⁻ per proton; the forward acceptance adds 0.1838 barn; combined, $Y =$ 0.7188 π⁻ per proton. Dividing the beam energy by $Y$ gives $E_\pi =$ 11.13 GeV. Since $\eta \le 1$ by definition, $E_b = E_\pi/\eta \ge E_\pi$, so this is a floor on the binder's cost that holds whatever the collector does. ∎

**Proposition 8 (the escape path is the target's radius, not its length).** *A production target may be made long without becoming opaque to the pions this collector accepts.*

*Derivation.* The collector accepts large-angle pions, which is 84.96 percent of production. A pion emitted at a large angle to the beam leaves the target through its **side**, so the path it must survive is of order the target's radius $r$ and not its length $L$. The survival probability is therefore $\exp(-r/\lambda_{abs})$ for that component, with $\lambda_{abs} =$ 15.89 cm in mercury — the metal of the published jet this checks against, rather than the lead §9.3's charge-ratio requirement calls for — against $(\lambda_{abs}/L)\,[1 - \exp(-L/\lambda_{abs})]$ for the forward component. Weighting by the large-angle fraction gives 0.8961 for the published geometry. **A narrow target is transparent however long it is**, which is why lengthening it to raise the yield does not defeat itself. ∎


### 14.7 The fuel target

**Proposition 9 (the tritium inventory does not fall with compression).** *The inventory required is areal density times beam area, and is therefore independent of the fuel's density.*

*Derivation.* A muon stops only if the target is at least one continuous-slowing-down range deep, so the requirement is on the **areal** density $x = \rho L$ obtained by integrating the stopping power, $x = \int_0^{p_{max}} (dE/dx)^{-1}\, dE$, which is 33.9 g/cm^2 at a 265 MeV/c window. The inventory is $M = x \cdot A$ with $A$ the beam's cross-sectional area. Compressing the fuel raises $\rho$ and shortens $L$ in exact proportion, leaving $x$ — and hence $M$ — unchanged. **Density buys length, not inventory.** ∎

**Corollary 9.1.** Because $A = \pi(2r_g)^2$ by Proposition 4, widening the bore widens the beam and so raises the inventory as the square of the aperture. That is the cost the wider bore is priced at in §10.4, and it is why the two alterations of §7.1 are not equally cheap.


### 14.8 The catalytic figure of merit, and the two uniqueness theorems

**Proposition 10 (cycles per binder).** A binder in a cycle of rate $\lambda_c$, lost per cycle with probability $\omega_s$ and independently with rate $\lambda_0$, completes


$$N \;=\; \frac{1}{\omega_s \;+\; \lambda_0/\lambda_c}$$

cycles in expectation.

*Proof.* Per cycle the binder survives sticking with probability $1-\omega_s$ and survives decay with probability $\lambda_c/(\lambda_c+\lambda_0)$ to first order in the cycle time. The two losses are independent, so the per-cycle survival is their product and the number of cycles is geometric with that parameter. To first order in the two small quantities its mean is $1/(\omega_s + \lambda_0/\lambda_c)$. Both terms are losses per cycle expressed in the same units, and the expression is symmetric in them: a cycle slow against the decay rate is punished exactly as a sticky one is. ∎

**Remark.** The two limits are the ones quoted in the literature separately. As $\lambda_c \to \infty$ the expression returns the sticking ceiling $1/\omega_s$; as $\omega_s \to 0$ it returns the decay ceiling $\lambda_c/\lambda_0$. The first of those is the point at which this proposition and Proposition 1 must be read together: Proposition 1's exact mean is one cycle below $1/\omega_s$ and this one reaches it, because this expression is first-order in the two loss terms and discards exactly that offset. They agree to first order, the difference is one cycle in the ceiling 198 cycles itself, and every figure in this paper is quoted from the measured count rather than from either. Neither ceiling alone is the operative bound for any real fuel, which is why fuels ranked on sticking alone rank wrongly.

**Theorem 4 (uniqueness of the fuel).** Over the closed set of pairs drawn from $\{p, d, t\}$ together with the helium pairs, $d$–$t$ maximises $N \cdot Q$.

*Proof.* The set is finite and closed: two nuclei drawn with repetition from the three hydrogen isotopes give 6 pairs, and the helium pairs are enumerated beside them. $Q$ is fixed by the masses. For $\lambda_c$ and $\omega_s$ the inputs are the muon-catalysis literature's own bands — measured for $d$–$t$, $d$–$d$ and $t$–$t$, and order-of-magnitude for the pairs that catalyse almost nothing — and the paper states them as bands rather than as measurements. Evaluating Proposition 10 on each and multiplying by $Q$ gives the table of §3, whose maximum is $d$–$t$ at 1989.1 MeV against 25.55 MeV for the next entry — a factor of 77.85. The ordering is a finite comparison over the tabulated inputs and contains no free parameter. ∎

The bands are the weakest input in that proof, so the next result removes half of them from it.

> **Corollary 4.1 (the ranking does not consult the cycle rates).** *Every competitor's cycle rate may be sent to infinity without changing the maximum.*

>

> *Proof.* By Proposition 10, $N \le 1/\omega_s$ for any $\lambda_c$, with equality in the limit $\lambda_c \to \infty$. Hence $N\,Q \le Q/\omega_s$, a ceiling in which no cycle rate appears. The largest such ceiling over the competitors is $t$–$t$'s, at 80.93 MeV, and $d$–$t$'s own tabulated value 1989.1 MeV exceeds it by a factor of 24.58. The maximum is therefore unchanged under any upward revision of any competitor's cycle rate whatsoever. ∎

**What that leaves load-bearing.** Only the stickings, and only through the ceiling $Q/\omega_s$. A competitor would have to be shown 24.58 times less sticky than the band records before the ordering could move — not faster, less sticky — and Theorem 2 has already shown that sticking is a property of the fusion kinematics rather than something a design may choose.

**Corollary 4.2.** No pair without tritium comes within a factor of 230.76 of $d$–$t$ on energy per binder, so the reaction's tritium requirement is not an artefact of the choice of fuel. It follows from the fuel being unique.

**Proposition 11 (the self-tritiating equilibrium).** A cell charged with pure deuterium reaches a steady state in which a fraction $f_{dt} = 1/3$ of fusions run on $d$–$t$.

*Proof.* The branch $d + d \to t + p$ carries a branching ratio of one half, so tritium is produced at $\tfrac12 f_{dd}$ per fusion. Every $d$–$t$ fusion consumes one triton, so tritium is destroyed at $f_{dt}$ per fusion. In steady state the two are equal, and with $f_{dd} + f_{dt} = 1$ this gives $\tfrac12(1 - f_{dt}) = f_{dt}$, hence $f_{dt} = 1/3$. The concentration producing that split follows from $f_{dt}/f_{dd} = \lambda_{dt} c_t / (\lambda_{dd}(1 - c_t))$, which returns 0.6211 percent; the mixed cycle rate and sticking are the branch-weighted means, and Proposition 10 then gives 3.51 cycles. ∎

**What the proposition does not establish.** It is a two-branch balance and it omits ³He, which the other $d$–$d$ branch produces and to which muon transfer is fast. Including that channel would reduce 3.51 cycles by an amount this paper does not compute, so §8 states the equilibrium as a quantity to measure. The *sign* of the result — that a deuterium cell holds a percent of the tritium a $d$–$t$ cell holds rather than half — does not depend on the omitted term, because ³He poisoning removes binders and does not add tritium.


### 14.9 What is not proved

Three things in this paper are **not** theorems, and are marked as such wherever they appear.

**The delivered acceptance is computed, not measured.** §6.2's loss budget is a product of five terms, each derived, but the product has never been measured end to end. An end-to-end count of stopped binders per pion produced is that measurement, and until it runs every figure downstream of it is conditional.

**The optimised production target's factor is taken from the literature, not reproduced here.** The 4.69 GeV of §7.1 is a published optimisation. Three candidate mechanisms for the discrepancy against this paper's 11.13 GeV were examined and bounded, and what survives is a normalisation requiring 2.389 interacting nucleons. A normalisation measurement on one target measures it.

**The operative sticking is unresolved between two published measurements.** 0.5050 percent and 0.5320 percent are the two effective values in the record, and no argument here chooses between them; both lie above the break-point at 0.1580 percent, so the choice moves the service life rather than the heat form's verdict. §11's protocol chooses, and §11.4 commits in advance to reporting a bound rather than an average if the two routes disagree.


## 15. References

1. M. G. Catanesi *et al.* (HARP Collaboration), Phys. Rev. C **77**, 055207; A. Bolshakova *et al.*, *Large-angle production of charged pions by 3 GeV/c–12.9 GeV/c protons on beryllium, aluminium and lead targets*, Eur. Phys. J. C **63**, 549 — Tables 5–8, both charges; and M. Apollonio *et al.*, *Forward production of charged pions with incident protons on nuclear targets at the CERN PS*, Phys. Rev. C **80**, 035208 — Tables XXII, XXIII and XXXII, both charges. **The production integration of §5.1 is taken from these tables and from nothing else.**
1. J. Strait, N. V. Mokhov and S. I. Striganov, *Towards the optimal energy of the proton driver for a neutrino factory and muon collider*, Phys. Rev. ST Accel. Beams **13**, 111001 — Table II and §V. **The front-end simulation the acceptance model of §6.1 is validated against.**
1. S. Cook *et al.*, *MuSIC: delivering the world's most intense muon beam*, arXiv:1610.07850; Phys. Rev. Accel. Beams **20**, 030101.
1. Mu2e Collaboration, *Mu2e Conceptual Design Report*, FERMILAB-TM-2545, arXiv:1211.7019.
1. COMET Collaboration, *COMET Phase-I Technical Design Report*, arXiv:1812.09018.
1. K. Oishi *et al.*, *Development of the Range Counter for the COMET Phase-α Experiment*, arXiv:2505.07464 — §1, which states the backward-emission capture and the thin production target.
1. J. J. Back, *Energy deposition studies for the Neutrino Factory target station*, JINST, arXiv:1104.2742 — FLUKA and MARS over a 4 MW, 8 GeV proton beam on a free mercury jet in a 20 T solenoid. **The sourced deposition, coil heating and radiation-lifetime figures of §10.3.**
1. K. T. McDonald *et al.*, *The MERIT high-power target experiment at the CERN PS*, IPAC 2010, p. 3527 — the free mercury jet run in a 15 T solenoid.
1. Variational three-body calculation of muon-alpha sticking, Phys. Rev. A **34**, 2536.
1. S. E. Koonin and M. Nauenberg, *Nature* **339**, 690.
1. M. Kamimura, Y. Kino and T. Yamashita, *Comprehensive study of muon-catalyzed nuclear reaction processes in the dtμ molecule*, Phys. Rev. C **107**, 034607 (2023).
1. R. Spencer Kelly, L. J. F. Hart and S. J. Rose, *An investigation of efficient muon production for use in muon catalyzed fusion*, J. Phys. Energy **3**, 035003. **The optimised production target §12 declines to adopt, and which a normalisation measurement would settle.**
1. X. Yin, W. Kou and X. Chen, *Muon-Catalyzed Nuclear Fusion: Physical Mechanism, Bottleneck Breakthroughs, and an Engineering Pathway*, arXiv:2605.26432 — Table I and §IV.B.
1. W. Kou and X. Chen, *A Lawson-inspired Cycle-Closure Criterion for Deuterium–Tritium Muon-Catalyzed Fusion*, arXiv:2607.10989 — Eqs. (11)–(13) and Table I. **An independent derivation of §4's eighth condition, reached without reference to this work.**
1. W. Kou and X. Chen, *External-Field-Assisted Muon Reactivation in Muon-Catalyzed Fusion: A Rate-Network Criterion for Reducing Alpha Sticking*, arXiv:2606.07077.
1. E. Koukina *et al.* (MuFusE Collaboration), *Design and Commissioning of a Deuterium-Tritium Gas Delivery System for Muon Catalyzed Fusion in a Diamond Anvil Cell*, arXiv:2606.19304; and J. D. Kalow *et al.*, arXiv:2606.05333. **The diamond-anvil cell and gas system of §9.3 column A.**
1. M. Lach, *The Method* v1.2–8 — *The Lach Cylinder: an index of transitions*.
1. M. Lach, *Cold Fusion and the Binder Economy*, v1.0; *The Binder Economy Against the Recent Literature*, v1.0; *Cold Fusion: Specification and Procedure*, v1.0. **Superseded by this paper wherever the two differ.**

---

