# Cold Fusion and the Binder Economy: A Closed Definition, a Unique Realisation, and the Bound That Decides It

**Matthew Lach** — Independent researcher
*v1.0, 6 September 2026. Prepared with a computing collaborator under the protocols of* The Method *v1.2-8.*

*An independent application paper. It uses the lattice, carries its own abstract and its own
references, and takes no part in the main paper's subject matter. It is not a member of either live
bundle.*

> **CORRECTION IN FORCE, §5.26.** The effective sticking used throughout §§5.5–5.25 — 0.1487 percent
> — mixes an excited-state initial sticking with a ground-state survival fraction. The operative value
> is **0.557 percent** (theory) against **0.505–0.532 percent** witnessed, a factor of **3.74**. §5.26
> states the corrected result and the specification that follows from it; the balances in §§5.14–5.25
> are computed at the superseded value and are **not** the paper's finding. Their arithmetic is
> correct and their input is not.

> **This paper supersedes and retires four documents**: *Muon-Catalysed Fusion* v1.0 and v1.1, the
> *Corrigendum* to v1.0, and *The Muon Collection Budget* v1.0. Where any of those disagrees with
> this paper, this paper stands. Their withdrawn claims are listed at §8.

> **Companion.** *The Binder Economy Against the Recent Literature* [15] is this paper's
> reconciliation half: it sets the work below beside four independent results published while it was
> being done, and reports what each confirms and what each corrects. The two share one claims ledger.

> **Verification.** Every quantity below is carried by `papers/CLAIMS.tsv` and checked by
> `python3 tools/verify_paper.py papers/Cold_Fusion_Binder_Economy_v1.0.md`, which recomputes each
> derived row from the instruments, binds each cited constant to the instrument that holds it, and
> fails on any number in the prose that no ledger row carries. The prose is a translation of the
> ledger and cannot outrun it.

---

## Abstract

Cold fusion is defined here as a nuclear fusion event in which the approach to nuclear separation is
supplied by molecular binding geometry rather than by kinetic energy. On that definition it is
neither speculative nor unachieved: it has been performed routinely since 1957, and this paper states
the procedure. Seven conditions are necessary for the reaction to occur and be verifiable; applied to
the closed index of charged particles they admit exactly one solution, because a structural window on
the binder mass — bounded below by fusion geometry at 119 electron masses and above by
molecular-index survival at 918 — contains exactly one leptonic occupant, the muon at 207. The
connection to the lattice is structural: the index carries configuration and not scale, so a muonic
atom occupies the same cell as its electronic twin, and the window selects which realisation of that
cell is physically available.

Net energy is not among those seven conditions, and this paper adds it as an eighth. Because the
binder is consumed and its service life is capped by sticking at 1/ω_s cycles, net positivity is a
single inequality on the cost of making one binder:

> **Condition 8.  E_binder < Q_fus · f_work / ω_s**

which evaluates to 7.52 GeV counted as heat and 3.77 GeV counted as work. Against it, the best
studied production and capture — HARP-measured pion cross sections convolved with the acceptance of a
20 T front-end channel on a thick tantalum target — costs 37.0 GeV per captured negative muon. The
figure of merit Q_fus·f_work/(ω_s·E_binder) is therefore 0.203 as heat and 0.102 as work: short by
4.9 and 9.8 respectively.

**The admissible set is not empty.** Condition 8 falls between what has been achieved and the
kinematic threshold floor of 0.30 GeV, which lies 123 below the achieved figure — so the requirement
is 4.9 or 9.8 of 123 available, leaving a margin of 25.1 or 12.6. **The binder itself is not the variable.** Sticking is
binder-mass-independent — exactly so in the sudden approximation, the mass cancelling from the overlap
that defines it — and the fusion yield belongs to the channel, so changing the binder moves only its
cost. Condition 8 is therefore a specification rather than a search, and the known charged spectrum
holds no second candidate: the window admits the muon and the pion, and the pion is absorbed before it
can catalyse. Two of the three levers in the
figure of merit are near their limits: sticking is governed by the ratio of recoil to binder
orbital velocity, an expression free of the binder's mass, reproducing the measured 2.97 for d+t and
1.66 for the d+d channel that ends in helium-3, with d+t already optimal; and the fusion yield goes
with that same channel choice. The live lever is E_binder, and condition 8 is a bound on it alone.

**The bound is then worked, and it resolves.** Integrating the HARP-measured cross sections over the
full angular range puts production alone at 11.13 GeV per pion, so collection efficiency cannot
satisfy condition 8 on its own: a perfect collector still leaves the heat form short by 1.48. Three
results move it. The convertible fraction is 0.795 rather than 0.501, once the alpha is counted at the
hot operating point the procedure already requires and the exothermic lithium-6 breeding a d–t cycle
must run anyway is included. The service-life cap is asymptotic in a density bounded above by
molecular survival, and the in-flight route that would lift that bound is below the binder's own decay
rate. And the fusion neutron, priced as bred fuel rather than as heat, is worth 146.06 MeV per fusion
against 26.06 — which closes the balance at **1.77** on sourced fission-suppressed breeder figures at
the 150 cycles per binder demonstrated in 1987.

**Stated as a specification, the residual is one number.** Solving each balance for the collection
efficiency at which it breaks even separates the products sharply: electricity requires 299.6 percent
collection together with the bound-case density and the favourable sticking branch, while bred fuel
requires 50.8 percent at demonstrated cycle counts and asks nothing of the other axes. Against the
30 percent the best studied front end captures, that is a factor of 1.69 in collection efficiency —
an acceptance specification whose cost is a shielding trade, not a new magnet.

**One route reaches a positive balance, and it is not the fusion-energy one.** On the corrected
sticking of §5.26 the heat form reaches 0.4006 with the specified collector and no fissile credit, so
**the self-sustaining criterion is not met on device-internal energy** — the service-life cap forbids
it at any density. The bred-fuel form passes at 1.203 and 1.772 **at the collection efficiencies §5.19
assumes**, because it is computed at the measured cycle count rather than the model; **§5.31 restates
it at the acceptance actually delivered, where it is 0.623 and closes only through an optimised
production target, at 1.480.** It is in any case a fusion–fission hybrid and §5.26 declines to read it
as the paper's subject. The aperture then
turns out not to be what stands in the way of that route: the collector specification separates into
dropping the front end's hemisphere cut — a choice made for a background a reactor does not have, and
free in aperture, field and shielding — and widening the bore, and **the first half alone, at the
existing 20 T magnet, gives a bred-fuel balance of 1.199 at the cycle count demonstrated in 1987** —
now computed rather than assumed, from a model that reproduces the built front end's own simulation to
0.982. That same calculation costs this paper two earlier claims, withdrawn at §5.24: the front end
captures the forward hemisphere and not the backward one, so dropping the cut is worth 1.20 and not a
factor of six; and the 1.199 survives only while the target imposes no momentum requirement of its own.
A stopping window of 400 MeV/c takes it to 0.968. **And that window cannot be bought out of the
difficulty**: §5.25 integrates the muon's stopping power to show the target must be one range deep,
that its tritium inventory is therefore areal density times beam area and does not fall with
compression, and that widening the window from 265 to 400 MeV/c costs **1.93** in inventory for
**1.11** in delivered muons. The route therefore needs one of two things, and both are already in this
paper: the wider bore, which restores it to 1.343, or the optimised production target, which drops the
requirement from 50.8 to 21.4 percent and is met by every configuration computed. The second is the
cheaper and §10 runs it first — but its figure is a **discrepancy this paper cannot explain**, three
candidate mechanisms having been examined and bounded, so what §10 runs first is a test of whether
that lever exists at all.

One measurement remains genuinely unresolved: the two published final stickings straddle the
break-point, and this paper's own protocol — neutron and X-ray routes run simultaneously on one
target, a disagreement being a refusal rather than an average — is what decides it. It bears on the
heat route and not on the bred-fuel one. What the bred-fuel route awaits is not a physical question
at all but a measurement of what a front end built for a reactor's requirement, rather than a
collider's, delivers to a dense target.

**The central result, and it is negative.** §5.26 corrects the effective sticking this analysis ran on
— 0.1487 percent, which mixed an excited-state initial value with a ground-state survival fraction —
to the operative **0.557 percent**, from a coupled-channels solution that treats the ground state
throughout and reproduces three independent 2001 measurements. Because the service life is capped at
1/ω_eff **at any density**, the witnessed quantities then bound the balance absolutely: a binder
returns at most **5.16 GeV** against a floor of **11.13 GeV** to make one. **The ceiling is 0.464 on
the heat form and 0.313 on the fusion yield alone**, at perfect collection and unlimited density. The
reactivation coefficient that would lift it is measured here from first principles at **0.198**
against a literature **0.35**, and is shown to be density-independent by construction — so
compression cannot move it, a high-Z admixture loses the binder faster than a cycle completes, and the
best published field-assisted calculation reaches **0.64** of the **0.727** required. The reaction is
proven; its net-positive configuration is **specified and unwitnessed**, in four equivalent single
numbers §5.26 states.

**The eighth condition is not this paper's alone**, and the corroboration comes with a correction. A
companion paper [15] sets this work beside four independent results published while it was being
done: an independent derivation of the same inequality as a cycle-closure criterion, an independent
proposal of the same fission-breeding escape, an independent pricing of the stripping route agreeing
within a factor of one and a half, and an optimised production target costing 2.37 less per pion.
Evaluated in those coordinates the results here stand, with one exception stated rather than repaired:
the service-life model over-predicts the one measurement it can be checked against by a factor of
**2.24**. Every figure here computed at a modelled service life inherits that; the bred-fuel figures,
computed at the measured cycle count and a sourced blanket, do not — so the correction weakens the
routes this paper already identifies as fragile and leaves untouched the one it identifies as robust.

---

## 1. The definition and the conditions

> A **cold fusion reaction** is a nuclear fusion event in which the approach to nuclear separation is
> supplied by *molecular binding geometry* rather than by kinetic energy.

Temperature does not appear. "Cold" is a consequence — when geometry supplies the approach, kinetic
energy is unnecessary — and the name has misdirected the field for decades. The operative property is
molecular access at nuclear separations.

Seven conditions are necessary:

1. **A binder** — negatively charged, leptonic (a hadron is absorbed before it can catalyse), mass
   within the structural window of §2, lifetime times cycle rate much greater than unity, producible.
2. **A molecular index** with at least two bound states, so that an *edge cell* exists near the
   binding threshold.
3. **A formation channel** — that edge cell reachable by the host medium's smallest exchangeable
   quantum.
4. **Nuclear overlap** — internuclear separation small enough that fusion outruns formation.
5. **An open exit** — the compound system must have a particle channel available.
6. **Binder release** — recoil velocity exceeding binder orbital velocity sufficiently that sticking
   is small.
7. **Conservation closure** — one heavy ash nucleus per event, energy accounted through the yield.

Conditions 1–5 suffice for the reaction to *occur*; 6–7 govern whether it is sustainable and
verifiable. **None of them is an energy condition**, which is why they are satisfied by a reaction
that has run since 1957 and does not produce net power. §4 supplies the eighth.

## 2. The unique realisation

The binder's mass sets the molecule's size, and therefore everything. Mass substitution moves the
internuclear separation from 74100 femtometres for an electron to 280 for a muon — a factor buying
about 91 orders of magnitude in tunnelling rate, against about 33 orders available from any
perturbation of the potential at fixed geometry. **Geometry is the mechanism; screening is a
correction to it.**

Two structural requirements bound the mass axis. **Fusion geometry**: the separation must bring the
nuclei close enough for fusion to outrun the cycle, giving a lower bound of 119 electron masses.
**Index survival**: the number of molecular bound states scales as the square root of the ratio of
nuclear to binder mass, and at least two are needed so an edge cell exists, giving an upper bound of
918.

> **The structural window is [119, 918] electron masses.**

The electron fails below it on geometry, the tau above it because the molecular index degenerates to
a single state. Inside it sit the muon at 207 and the pion at 273; interaction type removes the pion,
which is absorbed by the nucleus before catalysis. **Exactly one occupant remains.**

**Why the lattice is the right frame.** The index is built on configuration coordinates and carries no
scale, so a muonic atom occupies *the same cell* as its electronic twin. The index cannot distinguish
them. The muonic system is therefore not a new object requiring a new index but an existing cell
realised at a different scale, and the window is a statement about which realisations are available.
The lattice supplies the frame; it does not supply the rates, and §4 does not ask it to.

Hence the reaction is fully specified rather than schematic:

> **μ⁻ + (d,t) → (dtμ)⁺ → ⁴He + n + 17.59 MeV, muon returned**

The exit channel is fixed by nuclear structure, not chosen: helium-5 is unbound, so the compound
system separates. The formation channel is fixed by a near-coincidence: the loosely bound molecular
state lies at 0.66 electronvolts, within a small factor of the deuterium vibrational quantum at
0.365, and resonant transfer of that binding into host rovibrational excitation is what makes
formation fast. The muonic molecule's ground state at 319 electronvolts is unreachable by the host —
the resonance uses the last bound state, and there is no second option. That the loose state sits 483
below the ground state is a three-body accident which dropped a muon-scale quantity into the
electron-scale window.

The channel is also optimal, not merely available. Sticking is governed by the ratio of recoil
velocity to binder orbital velocity: 2.97 for d+t and 1.66 for the d+d channel ending in helium-3.
**This expression is free of the binder's mass** — the orbital velocity of a hydrogenic bound state
depends on charge and not on the bound particle's mass — so sticking is a property of the fusion
channel alone, and no choice of binder improves it.

## 3. The procedure

**Target.** Hydrogen isotopes only; elements above hydrogen capture the binder preferentially and
terminate the chain, so purity is a requirement and not a refinement. The tritium fraction is not
critical, the transfer step auto-optimising the population. **The companion's §2.4 puts a number on the purity
requirement**: transfer to oxygen runs at about 1 × 10¹⁰ s⁻¹ per liquid density of oxygen, so at the
density §5.13 brackets, a contamination of **5.49 ppm** costs as much binder as decay does. Purity
better than one part per million is the working requirement, and it tightens linearly with density.

**Density and temperature are one bracket, not two settings.** The formation resonance rises by
roughly two orders of magnitude toward 800 kelvin, so it pushes hot; density pushes cold. The bracket
resolves hot, and the cryogenic branch is excluded on thermodynamics (§6). Density is to be bought
mechanically rather than cryogenically. The bracket has the same two-bound shape as the mass window
of §2: a rate condition below, a degeneracy condition above.

**The cycle.** Per catalytic turn the binder stops, cascades, transfers, forms the molecule, de-excites
and fuses. The cycle is a harmonic sum, so the bottleneck moves: driving the formation resonance
transfers it to transfer itself, measured at 2.7e8 per second, after which the cycle rate saturates
near 2.6e8. Temperature buys a bounded factor and then stops. **This rate is the most load-bearing
number in the balance and carries the widest error bar**, its measurement being 2.7e8 plus or minus
0.9e8 — and every figure in §4 inherits it.

**The exit.** Per fusion the binder is released 99.14 percent of the time and remains bound to the ash
0.86 percent; roughly half of those are collisionally stripped and rejoin the cycle, giving a net loss
near 0.45 percent per fusion. The chain terminates when the binder decays — free lifetime 2.197
microseconds, bound disappearance 4.665e5 per second — or remains stuck.

**Service life.** Cycles per binder follow N = φλ_c/(λ₀ + ω_s·φλ_c), which rises with density and
saturates at 1/ω_s. At the measured sticking that asymptote is 222 cycles and the value at three times
liquid density is 196; with both projected sticking levers they are 427 and 340. **The asymptote is
approached only as density grows without bound, and quoting it as a service life overstates by the
decay term.**

**Observables, and a refusal.** Neutrons at 14.1 megaelectronvolts, one per fusion, timed from each
binder stop; and the muonic helium K-alpha line at 8.2 kiloelectronvolts, counting stuck binders
directly on a route sharing no instrument or calibration with the neutron measurement. These two
disagreed historically. Running them simultaneously on one target is what resolves the disagreement,
and **a disagreement is a refusal rather than an average.**

## 4. The binder economy

The binder is consumed. It is the sole element the reaction cannot self-supply and the only element it
destroys, and unlike a chemical catalyst it is not recovered at cycle's end. Net positivity is
therefore a statement about whether one binder's service life repays its manufacture:

> **N · Q_fus · f_work > E_binder,  with  N ≤ 1/ω_s**

Substituting the cap gives the eighth condition, on the binder alone:

> ### Condition 8.  E_binder < Q_fus · f_work / ω_s

**The convertible fraction.** Fusion yield is heat; accelerator input is work, and the two are not
interchangeable. The alpha carries 3.5 megaelectronvolts, 19.9 percent of the total, and deposits in
the fuel; the neutron carries 14.1, or 80.2 percent, and escapes to a blanket which may sit at any
temperature — 62 percent Carnot at 800 kelvin against ambient. The convertible fraction is 0.501.
Counted as heat, condition 8 reads 7.52 GeV; counted as work, 3.77.

**What a binder costs.** HARP-measured pion production cross sections off tantalum, convolved with the
MARS15 acceptance of a 20 tesla front-end channel and corrected for shower development in a target of
2 interaction lengths, give 0.054 captured muons per interacting proton per gigaelectronvolt of beam,
summed over both charges. Per charge that is **37.0 GeV of beam per captured negative muon.**

**The figure of merit** follows immediately:

> **FOM = Q_fus · f_work / (ω_s · E_binder)**

| convention | FOM | shortfall |
|---|---|---|
| heat | 0.203 | 4.9 |
| work | 0.102 | 9.8 |

**A cross-check that makes the cost figure load-bearing.** The historical Los Alamos result is about
150 cycles per binder. Recosted at 37.0 GeV rather than at the aspirational figure the earlier
literature carries, that is a gain of 0.071 — and the model returns the same. The agreement is why
the production cost is treated here as the operative quantity rather than an estimate.

## 5. Where condition 8 sits

Condition 8 is a bound on the same axis as the seven, and it does not empty the set.

| | value |
|---|---|
| condition 8, heat | 7.52 GeV |
| condition 8, work | 3.77 GeV |
| best studied production and capture | 37.0 GeV |
| kinematic threshold floor | 0.30 GeV |
| headroom, achieved to floor | 123 |
| required, heat | 4.9 |
| required, work | 9.8 |
| **margin, heat** | **25.1** |
| **margin, work** | **12.6** |

> **The requirement falls inside the headroom, not beyond it.**

The floor is the pion production threshold divided into the beam energy, and assumes every unit of
beam above threshold becomes a captured, transported, stopped binder. It is a bound and never a
target; no machine will approach it. Its role here is to establish that condition 8 is not
kinematically forbidden.

**Two of the three levers are spent.** Sticking is mass-free and channel-fixed, with d+t optimal.
The fusion yield goes with the same channel. **E_binder is the live lever**, and the 37.0 figure is
not a production limit but a production-and-capture figure: the front-end channel it was measured
through imposes an energy window for downstream radiofrequency capture, a selective requirement a
reactor does not share. **The gap between production and capture is where the required factor must
come from**, and how much of it is recoverable acceptance rather than irreducible cross-section is not
settled by any figure in this paper.

### 5.1 Production, measured across the full angular range

Whether the live lever is capture or production can be tested against measured cross sections rather
than asserted. Two HARP datasets between them cover almost the whole angular range for negative pion
production on lead at 8 GeV/c on a 5 percent interaction-length target:

| dataset | coverage | integral |
|---|---|---|
| large angle | 0.35 to 2.15 rad, p 0.10 to 0.80 GeV/c | 1.0382 barn |
| forward | 0.025 to 0.25 rad, p 0.50 to 6.50 GeV/c | 0.1838 barn |
| **combined** | | **1.2220 barn** |

The forward cone contributes only 15 percent. Its differential cross sections are the larger, but its
solid angle is small, and the two datasets are reported in different differential variables — the
forward one per unit solid angle — so the Jacobian must be applied. Treating them alike would
overstate the forward contribution by more than an order of magnitude.

Against an inelastic cross section of 1.7 barn this is **0.7188 negative pions per interacting
proton**, or **11.13 GeV of beam per pion produced**.

### 5.2 Collection alone cannot satisfy condition 8

Suppose collection were *perfect* — every pion produced becoming a stopped binder, which no machine
approaches and §5.3 shows none comes near:

| | condition 8 | production at perfect collection | |
|---|---|---|---|
| heat | 7.52 GeV | 11.13 GeV | **short by 1.48** |
| work | 3.77 GeV | 11.13 GeV | short by 2.96 |

The figure of merit rises to 0.675 as heat and 0.338 as work — from 0.203 and 0.102 at the capture
figure — and does not reach unity.

> **Collection efficiency alone cannot satisfy condition 8.** Even a perfect collector leaves the heat
> form short by 1.48 and the work form by 2.96. Production is binding, not merely capture.

This is the paper's principal negative result, and it inverts the reading §5 alone invites. The
shortfall at the capture figure is 4.9; of that, the part attributable to collection is real and large
but bounded, and the residual is production physics, which no collector design changes.

### 5.3 The discard, measured

The same integration prices the discard, which remains substantial. The best studied front end
captures **0.2160** negative muons per interacting proton against **0.7188** produced — **30 percent**.
The backward region above 1.15 radians alone, 35 percent of the large-angle acceptance, produces
0.2138 pions per interacting proton, so the ratio of that region to the whole captured yield is 1.01:

> **The entire captured yield of the best studied front end equals what one backward angular window
> produces.**

So both statements hold together, and neither may be quoted without the other: the discard is real and
a collector would recover a large factor, **and** recovering all of it still leaves condition 8
unsatisfied.

### 5.4 What remains open

This is still a **lower bound** on production. The band from 0.25 to 0.35 radians is covered by neither
spectrometer; forward momenta below 0.50 GeV/c and large-angle momenta above 0.80 GeV/c are
unmeasured. The residual 1.48 is therefore an upper bound on the shortfall rather than a closure, and
**this paper offers no verdict on condition 8.** What it establishes is that the shortfall is a
production shortfall, that it is not large, and that the two remaining levers on it are the sticking
value in the denominator of condition 8 and whatever the unmeasured phase space carries.

### 5.5 The residual, localised to one unresolved measurement

The shortfall of §5.2 is 1.48 at a sticking of 0.234 percent. That value is composed from a figure the
paper carried with a reservation: whether the 0.31 percent for the excited molecular state is an
initial sticking or a post-reactivation one. The reservation is now decisive, and the class is
settled by the company the figure keeps.

The initial sticking for the ground state — defined as the branching between bound and continuum
final states *at the moment of fusion*, before any reactivation — is **0.938 percent**, consistent with
0.91 to 0.93 from optical-potential and R-matrix treatments. That is what this paper's 0.90 is. The
0.31 is computed the same way, so it is an initial sticking too, and the measured reactivation applies
to it.

Reactivation is then read off the measured final stickings:

| | measured final | survival fraction | J=1 final sticking |
|---|---|---|---|
| SIN | 0.45 % | 0.480 | **0.1487 %** |
| PSI | 0.56 % | 0.597 | **0.1851 %** |

At the measured production cost of 11.13 GeV per pion, the heat form of condition 8 is met at perfect
collection if and only if the sticking is below **0.1580 percent**.

> **Both witnessed sticking values sit on the wrong side of that break-point** (§5.26). The heat form
> reaches **0.31** of what it needs on the more favourable one and is short by **3.37** on the other.
> The work form is short by **6.38** and **6.72**. Nothing straddles: the break-point is not between
> the two readings, it is below both.

### 5.6 The experiment this paper already specifies

The two determinations disagree, and §3.5 of this paper says what to do about it, in a sentence
written as a methodological caution before it was known to matter:

> The neutron and X-ray routes to sticking share no instrument or calibration. These two methods
> disagreed historically; running them simultaneously on one target is what resolves the disagreement,
> **and a disagreement is a refusal rather than an average.**

That measurement is now the decisive one of the whole programme. It is a bench experiment on an
existing muon beam, it needs no new machine, and it discriminates between the two branches above.

**This does not decide condition 8**, and this paper does not claim it does. What it does is localise
the decision: the heat form turns on one unresolved measurement between two published values, and the
work form is short under both readings by a factor between 6.38 and 6.72.

### 5.7 The binder is not the problem

It is natural to ask whether the difficulty lies with the muon specifically, and whether some other
particle would satisfy condition 8. The framework answers this cleanly, because **two of the three
terms in the figure of merit do not depend on the binder at all.**

**Sticking is binder-mass-independent**, and exactly so in the sudden approximation. Sticking is the
overlap of the binder's bound state in the molecule with its bound state on the ash, evaluated at the
recoil momentum. The binder's orbital radius scales as the inverse of its mass, so the phase in that
overlap is the recoil velocity divided by the product of the ash charge, the fine-structure constant
and the speed of light — **the mass cancels**. Sticking is a property of the *fusion channel*, not of
the binder. The expression reproduces both measured values, 2.97 for d+t and 1.66 for the d+d channel
ending in helium-3, from channel data alone.

The fusion yield is likewise a property of the channel. So changing the binder moves only E_binder,
and condition 8 becomes a pure **specification**:

> Any binder — known or not — satisfies condition 8 if and only if it is leptonic, lies within the
> structural window, survives long enough against its own decay, and **can be produced for less than
> about 5 GeV of beam energy per binder**: 5.93 on one reading of the reactivation and 4.76 on the
> other. Its mass enters only through that cost.

Against that specification, the known charged spectrum is quickly exhausted:

| particle | mass | | |
|---|---|---|---|
| electron | 1 | lepton | below the window: fusion cannot outrun the cycle |
| **muon** | **207** | **lepton** | **in the window** |
| pion | 273 | hadron | in the window, but absorbed before catalysis |
| kaon | 966 | hadron | above the window, and absorbed |
| antiproton | 1836 | hadron | above the window, and absorbed |
| sigma minus | 2343 | hadron | above the window, and absorbed |
| tau | 3477 | lepton | above the window: the molecular index degenerates |

The window admits exactly two occupants and one of them is hadronic. **Within the known spectrum there
is no alternative binder**, which is §2's uniqueness result arrived at from the economic side rather
than the geometric one.

Nor would a hypothetical lighter binder rescue the balance by much. The figure of merit varies as the
inverse of the binder's cost, and any production route costs at least the rest mass, so lighter is
monotonically better — but the window floor sits only 1.74 below the muon. **A binder at the very
floor of the window therefore buys at most 1.74 on rest-mass grounds, against a work-side requirement
of 6.38**, and only if its production were as efficient per unit mass as the muon's, which nothing
guarantees.

> **The binder is not the problem.** The muon is not merely the unique occupant of the window; no
> other occupant would close condition 8 even if one existed. What must improve is the cost of making
> a binder, and that is the same problem whichever binder it is.

### 5.8 The convertible fraction was an accounting choice, not a limit

The work form of condition 8 uses a convertible fraction of 0.501, obtained by counting only the
neutron's share at the blanket's Carnot factor. Two omissions in that figure are standard
fusion-blanket engineering, and both run in the same direction.

**The fuel is hot.** §3.2 resolves the temperature–density bracket at 800 K, because the formation
resonance demands it. The alpha's 3.5 MeV therefore deposits at 800 K, not at ambient, and is
convertible at the same Carnot factor as the blanket's. The 0.501 figure came from a row that assumed
the fuel sat at ambient — an operating point this paper's own §3.2 excludes.

**The blanket is exothermic.** A d–t cycle must breed its own tritium, and the breeding reaction

> n + ⁶Li → T + ⁴He + 4.78 MeV

*releases* energy. Breeding is not overhead to be subtracted; it is required, and the blanket returns
more heat than the neutron carries into it.

| | |
|---|---|
| blanket thermal per fusion | 14.1 + 4.78 = **18.88 MeV** |
| total thermal per fusion | 3.5 + 18.88 = **22.38 MeV** |
| energy multiplication | **1.272** (standard designs give 1.1–1.3) |
| work per fusion, as accounted | 8.81 MeV |
| work per fusion, corrected | **13.99 MeV** |
| **gain** | **1.587** |

The effective convertible fraction is therefore **0.795**, not 0.501, and the work-side shortfalls of
§5.5 fall with it:

> via SIN, **6.38 → 1.18**;  via PSI, **6.72 → 1.47**.

**Caution, and it applies to both figures equally.** Carnot is an upper bound on conversion, not an
achievable efficiency; a real cycle at 800 K reaches perhaps two thirds of it. This paper uses Carnot
throughout, so the correction is consistent with what it replaces, and the old and new figures inherit
the same optimism.

### 5.9 The collector, specified

§5.3 prices the discard; this specifies the machine that would recover it. The transverse-momentum
cap of a capture solenoid is set by the product of its field and bore radius, and the model is
validated against a published design: COMET's 5 T on a 0.15 m bore returns 112 MeV/c against its
stated cap of 100.

Applying that cap to the measured production of §5.1 gives a design curve. Two discards appear, and a
reactor need make neither:

**Hemisphere — and this paragraph carried an error, corrected here and worked out at §5.24.** It
stated that physics front ends capture backward-going pions only, to escape the forward neutron and
proton flux. The source says the opposite: the channel's function is to capture pions leaving the
target in the **forward** hemisphere, which is also the large one. A reactor may still take both, but
the gain is **1.20** rather than the factor of about six claimed here. At the existing aperture,
forward alone delivers **50.69 percent** of measured production and both hemispheres **60.92 percent**;
the backward hemisphere by itself is **10.23 percent**.

**Aperture.** The cap scales as field times bore radius. The best studied front end runs 20 T on a
7.5 cm bore, a product of **1.50 T·m**.

> To capture **90 percent** of measured production over both hemispheres requires a product of
> **2.60 T·m** — 20 T on a **13 cm** bore, or **1.74** times the existing aperture.

That is the collector specification: not a larger accelerator, not a stronger magnet, but a wider bore
and no hemisphere cut.

**The binding constraint is named here and posed properly in §5.21.** It is not the magnet: coil bores
for these solenoids already exceed a metre, set by shielding rather than by the beam. The
specification is a shielding trade, and §5.21 prices it at about 2.7 in coil heating or 11 percent in
coil bore.

### 5.10 The deciding experiment, stated as a protocol

§5.6 identifies the sticking disagreement as decisive and §3.5 states the method. Set out as a
protocol, it is a bench measurement on an existing beam:

1. **One target, both observables, simultaneously.** Neutrons at 14.1 MeV give the fusion yield per
   binder; the muonic helium K-alpha line at 8.2 keV counts stuck binders directly. The two share no
   instrument and no calibration.
2. **The discriminant.** Initial sticking is fixed at 0.938 percent by calculation. The two published
   final values, 0.45 and 0.56 percent, imply survival fractions of 0.480 and 0.597. Carried into the
   excited-state channel these give 0.1487 and 0.1851 percent, and the break-point for the heat form
   at the measured production cost is 0.1580 — **between them**.
3. **The refusal that governs the reading.** Per §3.5, a disagreement between the two routes is a
   refusal and not an average. If they disagree again, the correct output is a bound, not a mean.
4. **What each outcome settles.** Below the break-point, the heat form of condition 8 is satisfied at
   perfect collection. Above it, it is not, and the residual is 1.17. Either way the work form is
   settled by §5.8 to within 1.18 to 1.47.

### 5.11 The service-life cap is asymptotic, and reaching it costs density

Condition 8 uses N ≤ 1/ω_s. **That cap is a limit as density grows without bound**, not a value
attained at any operating point, because at finite density the binder's own decay takes a share. The
satisfaction reported in §5.5 is therefore an asymptotic statement, and this section prices it.

| | SIN reading | PSI reading |
|---|---|---|
| asymptote | 198 cycles | 188 cycles |
| density for 90 percent of it | **10.9 LHD** | 8.7 LHD |
| service life at three times liquid density | **479.6** | 169.0 |
| that as a fraction of the asymptote | **71.3 percent** | 75.6 percent |

The scanned experimental record ends at 1.5 times liquid density. **Reaching 90 percent of the cap
needs about seven times beyond it**, at the high temperature §3.2 requires. §5.13 prices that in
pressure and finds a structural bound rather than an engineering one. §5.5's margin does not survive
without it. **Note that ninety percent of the cap is not breakeven** — the companion's §2.5 solves for the density at
which each balance equals one and finds **2.10** for the heat form and less than liquid density for
the bred-fuel form, so this table states the ceiling rather than the requirement.

Carrying the corrected thermal accounting of §5.8 through to a reachable density:

| reading | density | service life | thermal gain | work gain |
|---|---|---|---|---|
| SIN | 3 | 479.6 | **0.964** | 0.603 |
| SIN | asymptote | 198 | **1.352** | 0.845 |
| PSI | 3 | 169.0 | 0.821 | 0.513 |
| PSI | asymptote | 188 | 1.086 | 0.679 |

On the corrected sticking of §5.26, with the blanket accounting, **the thermal balance reaches
0.3982 at the asymptote and 0.356 at three times liquid density** — it fails at every density, because
the asymptote itself is now 198 cycles. The work balance is short everywhere by more.

**This tightens §5.5 rather than overturning it.** The heat form is satisfiable, but only at a density
seven times beyond anything run, and the shortfall at a merely extrapolated density is 1.04 — near
enough that the density axis, not the sticking axis, may be what decides it.

### 5.12 A neutron multiplier, bounded rather than adopted

The blanket accounting of §5.8 assumes one neutron captured per fusion. Real designs add beryllium or
lead to multiply neutrons through (n,2n), which tritium self-sufficiency requires anyway. The
multiplication is endothermic — 1.57 MeV for beryllium — but each extra neutron then returns the
breeding reaction's 4.78, a **net 3.21 MeV per multiplied neutron**.

At 1.6 neutrons per source neutron the thermal yield reaches **24.31 MeV per fusion**, an energy
multiplication of **1.382** against the 1.272 of §5.8.

**This paper does not adopt that figure.** Published blanket multiplications span roughly 1.1 to 1.4
and depend on a design this paper does not specify, so 1.272 — computed from a single reaction with a
measured Q value and full capture — is what §5.8 carries, and 1.382 is recorded as the head of the
band rather than as a result. The distinction matters: the first is arithmetic on a nuclear datum, the
second is an estimate about an engineering choice.

**Proton energy is not a lever.** The same source finds the beam-power-normalised yield flat within a
tenth of its optimum across 4 to 11 gigaelectronvolts, with an optimum near 7. Any driver energy in
that band is equivalent for this purpose.

### 5.13 Density is bounded above, and the bound is structural

The density §5.11 requires can be priced, and it is not an engineering inconvenience. At 10.9 times
liquid hydrogen density — 4.25 × 10²² atoms per cubic centimetre — the molar volume of the fuel is
**2.60 cm³ per mole of hydrogen molecules**, against **23** for solid hydrogen at zero pressure: a
compression of **8.8**. That is not the kilobar regime; it is hundreds of gigapascals, and hydrogen
compressed that far is at or approaching the transition where it stops being molecular. Reported
figures put semimetallic behaviour from about **315 GPa**, with Raman evidence that hydrogen remains
**molecular to 440 GPa**, and a predicted transition density near **0.6 mol per cubic centimetre**.

**That transition density brackets what is needed.** Whether the reported 0.6 counts atoms or
molecules is not resolved by the sources read here, and the two readings give **8.5** and **17.0**
times liquid density. The requirement of 10.9 falls between them.

**Why this is a structural bound and not merely a hard one.** Vesman formation works by transferring
the loosely bound molecular state's 0.66 eV into the *rovibrational states of a host molecule*.
Atomic or metallic hydrogen has no such states. Dissociation therefore does not make formation
slower — **it removes the mechanism**. Density is bounded above by molecular survival, and the bound
has the same shape as the binder-mass window of §2 and the temperature bracket of §3.2: a rate
condition below, a degeneracy condition above.

> **The service-life asymptote sits at or beyond the density at which the formation mechanism ceases
> to exist.** The cap in condition 8 is therefore not merely unattained; it may be unattainable in
> principle, and §5.11's figures at three times liquid density are the ones that describe a physical
> operating point.

**Read the companion's §2.5 before taking this as a limit on the result.** What is bounded here is the *asymptotic*
service life. Breakeven needs far less: **2.10** times liquid density for the heat form at perfect
collection, and **0.730** or less for the bred-fuel form at every collection efficiency this paper
considers — below liquid density, so no compression at all. The bound above is real and it constrains
the ceiling; it does not constrain either route's breakeven.

**And the two axes fight twice.** §3.2 already records that the resonance wants heat while density
wants cold. There is a second opposition beneath it: the dissociation pressure of hydrogen *falls*
with temperature, so operating at the 800 K the resonance demands tightens this bound relative to the
room-temperature figures quoted above. By how much, this paper does not establish, and the figures
here should be read as the loosest form of the constraint rather than the operative one.

### 5.14 The terminal balance

One lever remains unexamined, and it is legitimate. **The blanket is thermally decoupled from the
fuel** — the neutron escapes into it — so it may sit at any temperature the materials allow. §5.8
assumed 800 K; fusion blanket designs run 700 to 900 K, and high-temperature concepts are proposed to
1200 K, where the Carnot factor is **0.750** rather than 0.625.

Setting every lever to a defensible bound at once, and granting *perfect* collection:

| | |
|---|---|
| density | 8.5 times liquid — the lower dissociation reading, so the densest defensibly molecular point |
| service life | 190.1 cycles |
| blanket | multiplied at 1.6 neutrons per source, 24.31 MeV thermal |
| blanket temperature | 1200 K, Carnot 0.750 |
| work per fusion | **18.23 MeV** |
| collection | perfect |
| sticking | the favourable of the two published readings |

> **Thermal gain 1.286. Work gain 0.965.**

**Both balances fail.** Thermal reaches 0.4151 and electrical 0.3113, with every input at its
favourable bound. §5.14 previously reported 1.286 and 0.965 here; those were computed at the
superseded sticking and §5.26 supersedes them.

**That figure is an upper bound and not an estimate**, and six separate optimisms are stacked inside
it: collection is perfect where the best studied machine reaches 0.30; the density sits at hundreds of
gigapascals and at the lower reading of a transition this paper could not resolve; the blanket
multiplication is a design estimate §5.12 explicitly declined to adopt; the blanket temperature is a
proposed concept rather than an operating one; the sticking is the favourable branch of a
disagreement §5.6 says must be resolved before it is read; and Carnot is a ceiling on conversion, not
an efficiency. **Every effect this paper has not modelled runs the other way** — real conversion below
Carnot, coil heating at the aperture §5.9 requires, tritium inventory and handling, and the
recirculating power of the driver itself.

> **On published numbers the reaction reaches thermal breakeven and does not reach electrical
> breakeven.** The margin of failure is smaller than the uncertainty on several of its inputs, so the
> *sign* is not established by this paper — but every unmodelled effect is unfavourable, and the
> honest reading of 0.965 is that it is optimistic.

**And that sentence names its own escape.** It is a statement about *electrical* breakeven, and §5.16
shows why electricity is the hard product here: condition 1 confines the fuel to charge one, which
forces the yield out as a neutron, which forces conversion at Carnot. §5.18 costs that neutron
correctly and the balance changes by an order of magnitude. **The shortfall is a property of the
product demanded, not of the reaction.**

### 5.15 Inverting the bound: the last four percent sits on an axis held constant

A null is a bound, and a bound is a specification of what must be true to cross it. §5.14's shortfall
is 1.04, so:

> Work breakeven at the bound case requires a service life of **610.5 cycles** against 190.1, which
> requires an effective sticking of **0.1427 percent** against the 0.1487 assumed — **a reduction of
> 4.0 percent.**

**Effective sticking is not a constant.** It is ω_s^eff = ω_s⁰(1 − R), where ω_s⁰ is a fixed quantum
overlap — §5.7 shows it is even independent of the binder's mass — and **R is the reactivation
coefficient**: the probability the binder is shaken off the ash during its slowing down from 3.5 MeV.
R is a collisional transport quantity, and it depends on the medium.

It has been measured to move. Effective sticking varies from **0.86 percent at 5 K to 0.64 at 16 K**,
a change of **26 percent** over eleven kelvin, attributed to a change in R.

> **Required: 4.0 percent. One measured excursion: 26 percent, in the favourable direction.**

And the paper's operating point is **800 K**. Neither of the two determinations §5.6 relies on was
made there, and no measurement of effective sticking exists at the temperature §3.2 requires. **The
last four percent therefore sits on an axis this paper holds constant, where the quantity is in fact a
function, where the operating point lies far outside the measured range, and where the one measured
excursion is more than five times what is needed.**

**The caution is not small, and it is stated rather than absorbed.** The five-to-sixteen-kelvin
excursion spans a phase change of the fuel, so it may be a phase or density effect rather than a
smooth dependence on temperature, and a survey that looked specifically for density dependence
reported none that was strong. **Extrapolating that excursion to 800 K is not warranted and is not
done here.** What is established is a sign and a sensitivity, not a value — and that treating ω_s as a
constant is a limit of this analysis rather than a property of the physics.

### 5.16 Why the conversion ceiling is a consequence of condition 1

The obvious way to find four percent is to stop converting through a thermal cycle. Direct
electrostatic conversion of charged fusion products is credited with **60 to 90 percent**, against
Carnot's 62 to 75. It would more than cover the gap. **It is structurally unavailable**, and the
reason is one this paper already states in another place.

Condition 1 requires the binder not be captured, and §3.2 gives the consequence: elements above
hydrogen capture it preferentially and terminate the chain, which is why purity is a requirement
rather than a refinement. **The fuel is therefore confined to charge one.** Censusing what that leaves:

| admissible fuel, charge one | yield | |
|---|---|---|
| d + t → ⁴He + n | 17.59 MeV | the neutron carries 80.2 percent |
| t + t → ⁴He + 2n | 11.33 MeV | two neutrons |
| p + d → ³He + γ | 5.49 MeV | aneutronic, but an electromagnetic exit, and slow |
| d + d → t + p | 4.03 MeV | aneutronic, and the yield is small |
| d + d → ³He + n | 3.27 MeV | neutronic and small |

| forbidden fuel | yield | fuel charge |
|---|---|---|
| d + ³He → ⁴He + p | 18.35 MeV | 2 |
| ³He + ³He | 12.86 MeV | 2 |
| p + ¹¹B → 3 ⁴He | 8.70 MeV | 5 |

**Every aneutronic channel with a competitive yield carries a fuel above charge one, and a fuel above
charge one eats the binder.** The two requirements are exclusive.

> condition 1 → fuel confined to charge one → the only high-yield channel is d + t → 80.2 percent of
> the yield leaves as a neutron → a neutron cannot be converted directly → **conversion is bounded by
> Carnot.**

So the conversion ceiling in condition 8's convertible fraction is **not an engineering choice**. It
descends from the first of the seven conditions, and it cannot be designed around while the binder is
one that transfers to higher charge. That is a bound of the same kind as the binder-mass window and
the density bound of §5.13 — and, like them, it is stated here as a bound rather than as a defeat: it
says precisely which door is shut, and therefore which are not.

### 5.17 An independent review, its agreements and its errors

A 2026 review of the same problem reaches the energy balance independently, and reading it against
this paper is worth doing in both directions.

**It agrees where it matters, and one agreement is a correction to §5.15's caution.** It states that
high-density confinement *promotes collisional stripping* of the bound ash–binder ion and may suppress
sticking below 0.3 percent. §5.15 argued from a temperature excursion that effective sticking is a
function and not a constant, and flagged that the excursion might be a phase effect; this is an
independent statement, from the same mechanism, that the reactivation term moves with the medium and
moves favourably. **The four percent §5.15 requires now has two independent reasons to be available.**

**It confirms §4.2's central correction, by making the error.** Its energy gains are computed at
5 GeV per muon, described as including "systematic losses from pion production, transport, decay, and
muon collection." §4.2 shows that figure is aspirational — the best published stopped-binder cost is
a thousand times higher, and measured production alone is 11.13 GeV per pion. **Every gain in its
table is therefore optimistic by that factor**, including the headline crossing of unity at 292
cycles. That an independent review makes the same error is the strongest available evidence that
§4.2 is worth stating.

**It disagrees on the cycle rate, and the disagreement is not averaged.** This paper carries a
saturation at 2.6 × 10⁸ per second, set by transfer; the review tabulates rates to 5.5 × 10⁸ under
polarisation and resonant enhancement. Per §3.5's rule, **a disagreement is a refusal rather than an
average**, and this paper keeps its own pinned value and records the other.

**And it contains an error this paper must not inherit.** It gives the transfer rate as "of order
10⁵–10⁶ s⁻¹". The rate is 2.7 × 10⁸, two to three orders higher, and it is the quantity that sets the
cycle's own cap. The figure is not used in its tabulated results, so the results survive it, but any
reader taking that number forward would mis-model the bottleneck entirely.

**Finally, it names an apparent escape from §5.13.** In-flight catalysis — where a fast bound
binder–triton system collides directly with a deuteron — triggers fusion **without first forming a
bound molecule**, and §5.13's density bound rests on molecular survival. **§5.20 evaluates that route
and closes it**: the in-flight rate is below the binder's own decay rate, so it yields fewer than one
fusion per binder at any density. The escape does not exist and §5.13's bound stands.

### 5.18 Where the balance closes: the neutron is worth more than its heat

Every figure to this point has costed the 14.1 MeV neutron at 14.1 MeV of heat, converted at Carnot.
That is the correct accounting for a device whose product is electricity. **It is the wrong accounting
for the device this reaction is actually good at being.**

A fast neutron entering a fertile blanket does not merely deposit heat. It breeds: ²³⁸U captures it
and decays to ²³⁹Pu, and that nucleus subsequently yields about **200 MeV** in a fission reactor. The
same logic runs on ²³²Th to ²³³U. Neutrons compete — tritium self-sufficiency needs about one per
fusion — so with a multiplier at 1.6 to 1.8 per source neutron, roughly **0.7** remain for breeding:

| | |
|---|---|
| breeding credit per fusion | **140 MeV** |
| plus thermal, from §5.8 | 22.38 MeV |
| **total value per fusion** | **162.4 MeV** |
| against the neutron's heat alone | a factor of **9.9** |

Recomputing the balance on that basis:

| configuration | cycles | binder cost | gain |
|---|---|---|---|
| demonstrated cycles, a real front end | 150 | 37.0 GeV | 0.66 |
| **demonstrated cycles, the §5.9 collector** | **150** | **12.4 GeV** | **1.97** |
| §5.11's physical density, §5.9 collector | 479.6 | 12.4 GeV | 6.30 |

> **At the cycle count demonstrated at Los Alamos in the 1980s, with the collector §5.9 specifies and
> nothing else, the balance exceeds unity by about two.** No sticking improvement. No polarisation. No
> extreme density. No new physics of any kind.

**This is a change of the question, and the paper says so rather than concealing it.** The 200 MeV is
realised downstream, in a separate fission reactor, and is an energy *credit* rather than device
output; an accounting that refuses such credits will not accept it. What it establishes is narrower
and still decisive: **the shortfall of §5.14 is a property of demanding electricity from this
reaction, not a property of the reaction.** Section 5.16 shows why electricity is hard here — condition
1 confines the fuel to charge one, which forces the yield out as a neutron, which forces Carnot. The
same neutron that makes electricity hard is what makes breeding easy. **The constraint and the escape
are the same object.**

**Three things must be said plainly about it.** Breeding fissile material is proliferation-sensitive,
and the review that proposes this configuration raises the point itself and cites the relevant IAEA
instrument; a thorium cycle and pure waste transmutation are the two variants with different profiles,
and transmutation produces no fissile inventory at all. The breeding ratio of 0.7 is reconstructed
from a multiplier this paper declined to adopt in §5.12 and is the weakest number in the table. And
the collector of §5.9 remains unbuilt — it is the one component every row above depends on.

### 5.19 The blanket, on sourced ground: the work form passes

§5.8 computed the blanket's contribution from one reaction — the ⁶Li breeding Q value, at full capture,
with no multiplier — and §5.12 declined to adopt a multiplied figure because it was a design estimate
rather than a datum. That caution was right in kind and, it turns out, conservative in degree.

Design studies of the **fission-suppressed fusion breeder** — the low-multiplication,
proliferation-conscious class of blanket, not the fast-fission one — report that each fusion produces
typically **0.6 fissile atoms** and releases about **1.6 times the neutron's energy** in the blanket,
at a tritium breeding ratio near **1.15**, which is self-sufficient. Those are figures for a designed
and analysed blanket rather than arithmetic on a single reaction:

| | this paper's own (§5.8) | sourced design |
|---|---|---|
| thermal per fusion | 22.38 MeV | **26.06 MeV** |
| overall multiplication | 1.272 | **1.482** |
| fissile per fusion | 0.7, reconstructed | **0.6, sourced** |

**This paper's arithmetic was conservative by 1.164.** Both stand — §5.8's is a floor derived from a
measured Q value, the design figure is better grounded — and the sourced one is used below.

**What it does to §5.14.** At the same bound case — density at the lower dissociation reading, the
favourable sticking branch, perfect collection, blanket at 1200 K — work per fusion becomes
**19.55 MeV** rather than 18.23, and:

| | §5.14 | on sourced blanket figures |
|---|---|---|
| thermal gain | 1.286 | **1.379** |
| **work gain** | 0.965 | **1.034** |

> **The work form does not pass, and the blanket does not rescue it.** On the corrected sticking it
> reaches **0.3338** against the **0.3113** of §5.14's own arithmetic — the designed blanket is worth
> about seven percent, not the factor of 1.07 that would have carried it. **The four percent §5.15
> went looking for was never the size of the gap**: the gap is a factor of three.

**The margin is small and must not be overstated.** 1.034 is as marginal as 0.965 was, it still
assumes perfect collection, and every caution §5.14 listed still applies. What has changed is which
side of unity the marginal case falls on, and that it now rests on a design study rather than on this
paper's own reconstruction. **The honest reading is that electrical breakeven is at the boundary, and
which side it lands on is not settled by anything here.**

**What it does to §5.18.** The breeding credit becomes 0.6 × 200 = 120 MeV and the total value per
fusion **146.06 MeV**, against §5.18's reconstructed 162.4:

| configuration | cycles | binder cost | gain |
|---|---|---|---|
| demonstrated cycles, real front end | 150 | 37.0 GeV | 0.59 |
| **demonstrated cycles, §5.9 collector** | **150** | **12.4 GeV** | **1.77** |
| bound case, perfect collection | 190.1 | 11.13 GeV | **7.73** |

The conclusion of §5.18 is unchanged and now rests on sourced figures throughout: **at the cycle count
demonstrated in the 1980s, with the collector and nothing else, the breeding balance is near two.**

### 5.20 The in-flight escape closes, and the stripping route opens

§5.17 recorded that in-flight catalysis — fusion triggered by a fast collision without first forming a
bound molecule — would not be subject to §5.13's density bound, since that bound rests on molecular
survival. **That escape closes on the rate.**

The in-flight d–t rate at liquid density is **2.8 × 10⁴ per second** by a constrained
molecular-dynamics calculation, and 0.5 × 10⁵ by an independent approach. Against the molecular
route's saturation it is **9,286 times slower**, and — decisively — it is *below the binder's own decay
rate* of 4.665 × 10⁵ per second. Cycles per binder are then **0.510 even at the densest defensibly
molecular point**: fewer than one fusion per binder at any density.

> **The route removes the molecular requirement and the cycle with it. §5.13's bound stands.**

**Two confirmations arrive with it.** The same source states that the sticking probability is
insensitive to how the system was assembled, because the 17.59 MeV yield dwarfs any molecular binding
energy, so the exit dynamics are independent of the entrance channel. §5.7 argued sticking is
independent of the *binder's mass*; this says it is equally independent of the *formation route*. Both
follow from one fact: **sticking is a property of the exit.** And its independent channel estimates —
5.60 percent for d+t, 7.84 for t+t, 32.4 for the d+d channel ending in helium-3 — reproduce §5.16's
ordering by a different method, with d+t optimal and the d+d channel worse by about six.

**And a route to the reactivation term opens.** §5.15 requires a 4.0 percent reduction in effective
sticking and locates it in the reactivation coefficient. The same source proposes obtaining it
directly: the stuck binder on the ash is a nonlinear oscillator, and irradiating it at twice its own
orbital frequency drives it into resonance and ionises it — the mechanism by which a Rydberg atom is
ionised in a microwave field. The required wavelengths are **0.11 nm** for the ground state and
**0.44 nm** for the first excited state, available from synchrotron sources, and the paper notes that
the muonic molecule itself is *not* destroyed at that frequency.

**This must be set against this paper's own no-go, and the two are not the same claim.** §5 records
that external-field stripping is defeated by a space–time overlap factor by about six orders. That
finding concerns a *focused beam* attempting collisional stripping. The proposal here is *resonant
photo-ionisation* at the bound binder's own eigenfrequency, exploiting its chaotic instability —
a different mechanism, not a better beam. **Whether the no-go extends to it is not settled**, and per
§3.5 this paper records both rather than averaging them or choosing. **The route is priced and capped
in the companion's §2.1 and §2.6**, which put the gain at 1.39 in cycles and find it limited by
transport of the freed binder rather than by the field.

**One further confirmation for §5.15.** The temperature dependence of muon loss has been measured not
only over the five-to-sixteen-kelvin range §5.15 cites but across **85 to 790 K** in the d+d system,
with muon loss *increasing* as temperature *decreases*. That range brackets the 800 K operating point
§3.2 requires, and the direction is the favourable one. §5.15's caution — that its cited excursion
spanned a phase change and might not be a temperature effect — is substantially relieved by a
measurement over seven hundred kelvin in the same direction.

### 5.21 The collector's constraint, re-posed: it is shielding, not the magnet

§5.9 named coil nuclear heating as the collector's binding constraint and declined to model it. It can
now be posed properly, and it is a smaller ask than "heating scales with aperture" suggests.

**The acceptance model is validated a third time.** A published front-end design states that a 20 T
solenoid with a **150 mm clear bore** captures transverse momentum up to **225 MeV/c**. The model
returns **225 MeV/c** exactly. (COMET's 5 T on a 150 mm bore, giving 112 against its stated 100, was
the second; the first was its own derivation.)

| | |
|---|---|
| existing design point | B·R = **1.50 T·m** (20 T, 7.5 cm clear radius) |
| §5.9 specification | B·R = **2.60 T·m** (20 T, 13 cm) |

**The magnet is not the constraint.** The same source records that these solenoids "demand a 20 T peak
field in a bore larger than **1 m**" — and that demand comes from *shielding*, not from the beam. The
coil bore is already an order of magnitude above the clear aperture. What sets the clear aperture is
how much shielding sits between it and the coil, so the specification is a **shielding trade**, not a
magnet problem.

Taking a coil inner radius of 0.50 m and a fast-neutron attenuation length of 5.5 cm in tungsten, the
specification thins the shield by **5.5 cm**, and therefore either:

> **costs about 2.7 in coil heating**, or, at fixed heating, **costs about 11 percent in coil bore.**

Both are ordinary engineering trades rather than a new machine — and a "20 T at 20 K" model coil for
precisely this solenoid, in a bore above one metre, is under active development, with fusion
applications named alongside the collider one.

**Two cautions.** The coil radius and the attenuation length are reconstructed rather than sourced, so
the factor of 2.7 is a scale and not a design figure; a real shield is layered and its attenuation is
not a single exponential. And thinning the shield raises the *dose* as well as the heat, which governs
insulation lifetime rather than cryogenic load and is not modelled here at all.

### 5.22 What each product asks of the collector

Every balance in this paper has been stated at one of two collector assumptions — the §5.9
specification at 90 percent, or the 11.13 GeV production floor with collection perfect. Neither is a
measurement. The honest question is the inverse one, and it has a single-line answer: **at what
collection efficiency does each product break even?** Setting the balance to 1 and solving,

> **η = 11.13 GeV / (N · V)**

for a service life N and a value per fusion V. Nothing else enters. The table below runs it over the
three products of §5.14, §5.18 and §5.19 and the three service lives the paper has established.

| product | V per fusion | N | collection needed |
|---|---|---|---|
| electricity, bound case | 19.55 MeV | 190.1 | **299.6 %** |
| electricity, φ = 3 | 19.55 MeV | 479.6 | **118.7 %** — unreachable |
| heat, bound case | 26.06 MeV | 190.1 | **72.5 %** |
| heat, φ = 3 | 26.06 MeV | 479.6 | **89.1 %** |
| bred fuel, bound case | 146.06 MeV | 190.1 | **12.9 %** |
| bred fuel, φ = 3 | 146.06 MeV | 479.6 | **15.9 %** |
| bred fuel, demonstrated cycles | 146.06 MeV | 150 | **50.8 %** |

Two reference points sit against that column. The best front end studied in the literature captures
**30 percent** of the pions its target produces (§5.1, C106). The collector specified in §5.9 targets
**90 percent**, and §5.21 priced the difference as a shielding trade rather than a new magnet.

**The result is a separation, not a margin.** Read against those two points the table divides cleanly:

- **Electricity is the demanding product and is not robust.** It needs 299.6 percent collection *and*
  the bound-case density *and* the favourable sticking branch, all three together; lose any one of
  them and it fails. At φ = 3 it asks for 118.7 percent, which is not a hard specification but an
  impossibility — no collector satisfies it, because the requirement exceeds the production itself.
  This is the same conclusion §5.19 reached from the other side, where the work form passed at 1.034:
  a balance that close to unity is a statement that the axis is exhausted, not that it is safe.
- **Heat sits between**, needing 72.5 percent at the bound case and 89.1 percent at φ = 3 — the
  latter essentially the §5.9 collector with nothing left over.
- **Bred fuel is the robust product.** It needs 12.9 percent at the bound case — below what today's
  front end already achieves — and **50.8 percent at the demonstrated 150 cycles**, which asks
  nothing of the density axis, nothing of the sticking measurement of §5.10, and nothing of the
  reactivation of §5.15. It is a collector specification alone.

**The product choice is worth 7.5 in collector specification** — the ratio of the two bound-case
requirements. That is the largest single lever this paper has found, and it is not a physical
improvement at all: the same reaction, the same binder, the same cycle, priced against what its
neutron is actually worth rather than against the heat it deposits.

**What remains, stated without a hedge.** The bred-fuel case at demonstrated cycle counts is
**1.69 above today's measured front end** and comfortably inside the §5.9 collector. That factor —
1.69 in collection efficiency — is the whole of what stands between the corpus's own eighth condition
and a satisfied one, on the product the definition permits and at a cycle count already demonstrated
in a laboratory. It is an engineering figure with a named trade behind it (§5.21), not an open
physical question.

**The caution this table does not remove.** η here is *collection*, and collection is only one factor
of a real front end: the model of §5.9 is an acceptance calculation, and a machine must also transport,
cool and stop what it accepts. The 30 percent reference is likewise a capture fraction, not a
delivered-to-target fraction. Every row above therefore states a *necessary* efficiency, never a
sufficient one, and the distinction is the same one §5.5 draws about a shortfall: a bound that has
been localised is not a bound that has been cleared.

### 5.23 Two routes, one shared dependency

§5.22 solved each balance for the collection efficiency it needs. The direct form of the same
computation is more useful to a builder: **state every balance at the two collection efficiencies that
actually exist** — the 30 percent the best studied front end captures, and the 90 percent the §5.9
collector targets — instead of at the perfect collection every earlier table assumed.

| balance | at today's 30 % | at the §5.9 collector, 90 % |
|---|---|---|
| heat, demonstrated 150 cycles | 0.105 | **0.316** |
| heat, bound-case service life | 0.414 | **1.241** |
| heat, φ = 3 | 0.337 | **1.011** |
| work, demonstrated 150 cycles | 0.079 | **0.237** |
| work, bound-case service life | 0.310 | **0.931** |
| bred fuel, demonstrated 150 cycles | 0.591 | **1.772** |
| bred fuel, bound-case service life | **2.32** | **6.96** |

Three readings, and the third is the one that matters.

**First: the breeding credit is not load-bearing for the heat form.** At the §5.9 collector, the heat
balance reaches **0.4006** on the bound-case service life and **0.3731** at φ = 3, counting the
neutron at its heat and taking no fissile credit at all. §5.18's change of question was therefore the
*only* escape, not one of two: **the device-internal form does not clear unity**, and the paper's
scope — a *self-sustaining* reaction — is not met inside the device on witnessed numbers. The work
form is further off still: **0.3338** at the collector, and is a
statement that electricity remains the demanding product exactly as §5.22 found.

**Second: nothing passes on today's front end at demonstrated cycle counts.** The best row in that
column at 150 cycles is **0.591**. The collector of §5.9 is therefore not one improvement among
several — it is necessary in every configuration this paper can construct except one, and that
exception is the second reading below.

**Third, and this is the structure of the result: the two routes need different things, and they
overlap in exactly one place.**

- **The heat route needs both.** It needs the collector *and* the bound-case service life — which
  means the density of §5.13 and the favourable sticking branch of §5.10. Take away either and it
  fails: 0.316 with the collector at demonstrated cycles, 0.414 with the bound-case life at today's
  front end.
- **The bred-fuel route needs either one.** With the collector it passes at demonstrated cycle counts
  (**1.772**), asking nothing of density or sticking. With the bound-case service life it passes at
  **today's measured front-end collection** (**2.32**), asking for no new magnet at all. Either
  suffices; neither is required jointly with the other.

> **The collector and the service life are two independent routes to a positive balance on the
> bred-fuel product, and the only shared dependency of both products is the collector.**

That is a stronger claim than a margin, and it is the corpus's own two-route protocol applied to an
engineering question rather than a measurement: a result reachable by two paths that share one
component is a result whose risk is concentrated in that component. Here the concentration is total.
Every open item in §9 except the collector bears on the *service life* axis, and the bred-fuel route
does not need that axis if the collector exists.

**What this does not say.** It does not say the bound-case service life is available — §5.13 bounds
the density from above and §5.10's measurement is unmade, so the 2.32 in the left column is the most
speculative number in the table and is stated as the second route rather than the first. It does not
price the blanket's own capital or the fissile handling §5.18 flags as proliferation-sensitive. And
the 30 percent column is a capture fraction, not a delivered-to-target fraction, so every entry in it
is an upper bound on what today's hardware would actually return.

### 5.24 What today's magnet delivers, against a model validated on the built machine

§5.23 concentrates the risk in one component, and this section works that component's number out
rather than assuming it. Doing so **overturns two claims made earlier in this paper**, and both
withdrawals are stated before the result that replaces them.

**The model.** The transverse cap of §5.9 tests the *pion*. What a target receives is the *muon* from
that pion's decay, and π → μν is a two-body decay that redistributes momentum: the muon takes between
(m_μ/m_π)² and all of the pion's energy and picks up a transverse kick of at most **29.79 MeV/c**, the
muon's momentum in the pion rest frame, where its energy is **109.78 MeV**. The decay is isotropic
there — the pion is spin zero — so the rest-frame sphere is integrated on a fixed grid rather than
sampled. A pion outside the cap is not modelled as decaying: its decay length is metres and the
channel absorber is centimetres away. Then a **momentum requirement** is applied to the muon, because
a channel must deliver into something.

**It reproduces the built machine.** The front end whose simulation this paper has been quoting
delivers into an rf-capture bucket requiring **100** to **265 MeV/c**. Applying that window, over the
hemisphere the front end actually takes:

> model **29.51 %** against the MARS15 figure of **30 %** — a ratio of **0.982**.

That is a validation, and it changes the epistemic status of every collection figure in this paper
from *assumed* to *computed*.

**Withdrawal 1 — the hemisphere, and §5.9 has it backwards.** §5.9 states that physics front ends
capture backward-going pions only, to escape the forward flux. The source says the opposite in its own
words: the channel's function is "to efficiently capture pions exiting the target in the **forward**
hemisphere". Forward is also the *large* hemisphere — **50.69 %** of production against the backward
hemisphere's **10.23 %**. So the front end already takes the big half, and adding the other one is
worth **1.20**, not the factor of about six §5.9 claims. **That sentence in §5.9 is withdrawn.**

**Withdrawal 2 — the 2.92 was never a margin.** §5.24 previously reported that the model was
conservative by 2.92 at "the one comparable point". That comparison set a *backward* model acceptance
of 10.3 % against a simulation of a machine that captures *forward*, with no momentum requirement on
one side and the rf bucket on the other. It compared two different things. **The 2.92 is withdrawn
entirely**, and nothing replaces it: the model needs no margin, because it now reproduces the
simulation directly.

**What the real lever is, and it is not the aperture or the hemisphere.** The source is explicit that
its acceptance falls off at high momentum "primarily from the requirement that T < 180 MeV (265 MeV/c),
and secondarily from the transverse momentum p_T < 225 MeV/c that is captured by the target solenoid".
The dominant cut is the **rf-capture window**, and it costs **1.72**:

| at the existing 1.50 T·m | delivered, per π⁻ produced |
|---|---|
| forward hemisphere, rf window — *the built machine* | **29.51 %** |
| forward hemisphere, no momentum requirement | **50.69 %** |
| both hemispheres, no momentum requirement | **60.92 %** |
| decay survival, captured μ⁻ per captured π⁻ | **0.997** |

The rf window is a collider requirement: it exists so that the muons fit a downstream accelerating
bucket. **A reactor does not have that bucket.** This is the "selective requirement a reactor does not
share" of §9, now identified and priced instead of asserted.

**But a stopping target has a requirement of its own, and this is where the result turns.** A muon
must stop in the fuel, so a reactor front end substitutes a *range* window for the rf one. The model
does not choose that window — it is a design variable of the target's areal density — so it states the
sensitivity:

| delivered, per π⁻ produced | p < 200 | p < 265 | p < 400 | no cut |
|---|---|---|---|---|
| 1.50 T·m, both hemispheres | 36.48 % | **44.43 %** | **49.16 %** | **60.92 %** |
| 2.60 T·m, both hemispheres | 38.68 % | **52.79 %** | **68.20 %** | **89.88 %** |

against the **50.8 %** §5.22 shows bred fuel needs at demonstrated cycle counts. Carried into the
balance:

| bred fuel at 150 cycles | balance |
|---|---|
| today's aperture, both hemispheres, no momentum requirement | **1.199** |
| today's aperture, both hemispheres, p < 400 MeV/c | **0.968** |
| today's aperture, both hemispheres, p < 265 MeV/c | **0.875** |
| wider bore, both hemispheres, p < 400 MeV/c | **1.343** |
| wider bore, both hemispheres, p < 265 MeV/c | **1.039** |

> **The number closes, and it does not close favourably at today's aperture.** With no momentum
> requirement at all the balance is 1.199 — which is the 1.203 this section previously reported, now
> computed rather than assumed. Impose any realistic stopping window and it falls below unity.

**So the route needs one of two things it did not need an hour ago**, and both were already in this
paper:

1. **The wider bore of §5.9.** At 2.60 T·m the balance holds through a 265 MeV/c stopping window at
   **1.039** and through a 400 MeV/c one at **1.343**. §5.21 prices that bore as a shielding trade.
2. **The optimised production target.** At the companion's **4.69 GeV** per pion rather than this
   paper's measured 11.13, the requirement falls from 50.8 % to **21.4 %** — met by *every* row of the
   table above, including today's aperture at the tightest stopping window, which then gives **2.076**.

**Neither is a new machine, and they are independent.** That is the honest state of the acceptance
question: it is closed as a computation, it costs this paper the free-hemisphere argument and the
2.92, and it leaves the bred-fuel route needing either a shielding trade or a target-design
measurement — with §10's Stage C, the cheapest of the four, now the one that moves it furthest.

**What the model still does not include.** Transport, cooling, and stopping. Every figure above is an
acceptance-and-decay calculation, so each is an upper bound on what a machine delivers — which is
precisely why the MARS15 row, the one that carries 50 m of real transport, is the validation and not
the prediction. A reactor front end will lose something to transport that this model does not charge
it for.

### 5.25 The stopping window is bought with tritium, and it saturates

§5.24 leaves the result turning on the momentum window the fuel target imposes, and §9 ranked that
window first among the things to settle. It is settled here, and the answer demotes it: **the window
is not a lever, it is a constraint, and pushing it is the wrong way to close the route.**

**A window is a range.** A delivered muon is worth nothing unless it stops in the fuel, so the target
must be one continuous-slowing-down range deep at the window's top momentum. Integrating the Bethe
stopping power for muons in hydrogen:

| window top | range required |
|---|---|
| 150 MeV/c | **10.6 g/cm²** |
| 265 MeV/c | **33.9 g/cm²** |
| 400 MeV/c | **65.4 g/cm²** |

The calculation is validated twice, and neither validation is this paper's own. Its minimum-ionising
stopping power in liquid hydrogen is **4.06 MeV cm²/g** against the standard **4.034**. And the same
model, applied to the running experiment of the companion's §2.4 — a 4 mg fifty-fifty fill — returns
**23.1 Ci** of tritium against the **24** that experiment states.

**The inventory does not depend on density, and that is the structural point.** Tritium held is areal
density times beam area, and the areal density is fixed by the range. Compressing the fuel changes the
target's *length* and not its contents. A 265 MeV/c window is a **192 cm** target at liquid density
and a **23 cm** one at the density §5.13 brackets — and both hold the same tritium.

> **Density buys compactness. It does not buy a gram of inventory back.**

That closes a door §5.27 had appeared to open. §5.27 shows the bred-fuel route needs no compression
for its *service life*, and that stands. But the stopping window needs areal density, and areal
density is tritium whatever the compression.

**And the trade is steeply diminishing.** On a 5 cm beam radius — a scale, not a specification, and
the inventory goes as its square:

| | 265 MeV/c | 400 MeV/c |
|---|---|---|
| tritium | **1.60 kg** | **3.08 kg** |
| delivered fraction (§5.24) | 44.43 % | 49.16 % |

> **Widening the window from 265 to 400 MeV/c costs 1.93 in tritium inventory and returns 1.11 in
> delivered muons.** The window saturates economically long before it saturates physically.

**So §9's first item is answered, and it changes the ranking rather than the result.** The stopping
window cannot be widened into a positive balance: reaching unity at today's aperture would need
essentially the whole spectrum, an inventory several times the table above, and the return curve is
against it the whole way. The route closes on the other two axes instead — the production target,
which drops the requirement to 21.4 percent and is met at *every* window in §5.24's table, or the
wider bore, which holds at **1.039** through a 265 MeV/c window. **Both are cheaper in tritium than
widening the window, and the production target is cheaper than either.**

**The beam radius is not a free parameter either, and deriving it is what makes the kilograms real.**
A particle born on the axis with transverse momentum p_T spirals on a circle of radius r whose centre
sits r off-axis, so it reaches **2r** — which means a solenoid's clear radius simply *is* twice the
gyroradius at its own transverse cap. Transport down the channel is adiabatic, conserving p_T²/B. That
one relation reproduces three geometries none of which was used to build it:

| | derived | stated |
|---|---|---|
| capture solenoid at 20 T, 1.50 T·m | **7.50 cm** | 7.5 |
| after the taper to **1.25 T** | **30.0 cm** | 30 |
| the §5.9 specification at 2.60 T·m | **13.0 cm** | 13 |

**So the bore buys acceptance and pays in tritium, through the same p_T cap.** Widening the aperture
raises the cap, which raises the gyroradius, which widens the beam the stopping target must cover —
and the inventory goes as the square of that:

| | 265 MeV/c window | 400 MeV/c window |
|---|---|---|
| today's aperture, 7.5 cm | **3.59 kg** | **6.93 kg** |
| §5.9's bore, 13 cm | **10.79 kg** | **20.82 kg** |

> **The wider bore costs 3.01 in tritium inventory.** It is not the free-standing engineering trade
> §5.21 prices; it carries a fuel-inventory cost that §5.21 does not see, because §5.21 is about the
> coil and this is about the target.

**And that settles which lever to pull, in the units that matter.** Taking tritium per unit of
balance at a 265 MeV/c window:

| route to a positive balance | balance | tritium | per unit |
|---|---|---|---|
| wider bore, at the measured production cost | 1.039 | 10.79 kg | **10.4 kg** |
| today's aperture, at the optimised production target | 2.076 | 3.59 kg | **1.73 kg** |

> **The production target is 6.0 times better than the bore in tritium per unit of balance**, and it
> is also the cheaper measurement.

**That comparison is contingent, and the contingency is named.** Its second row uses the optimised
production figure, which §5.26 records as a **discrepancy this paper cannot explain** — thickness,
phase-space coverage and beam species have each been examined and none accounts for it. If the
optimised figure does not survive §10.3, the second row goes with it and the wider bore is the only
route left, at 10.79 kg. **§10.5 runs the production stage first for that reason and not the
opposite one**: it is the cheapest way to find out whether the cheapest lever exists at all.

**Three things this does not establish.** The derivation assumes the stopping target sits in the
capture field and that transport is adiabatic and lossless; a real channel is neither, and a target in
a weaker field is larger by √(B_capture/B_target) with the inventory going as its square again. The
density-effect correction is omitted from the stopping power, which understates the range slightly at
the top of the table — an optimistic direction, stated rather than corrected. And no tritium *supply*
is modelled: §5.19's breeding ratio of 1.15 says the reactor makes its own once running, but the
inventory above is the startup charge, and the doubling time that would replace it is not computed
here.

### 5.26 What the witnessed quantities prove, and what they forbid

This section corrects the central number of this paper and states the consequence. It is the result
the paper exists to produce, and it is not the one earlier sections reported.

**The correction.** Every balance above used an effective sticking of **0.1487 percent**, formed as the
J = 1, v = 0 *excited-state* initial sticking multiplied by a survival fraction derived from a
*ground-state* measurement. The two belong to different states. The comprehensive coupled-channels
solution of the fusion reaction [14] treats (dtμ)ᴶ⁼ᵛ⁼⁰ throughout — **fusion occurs from the ground
state** — and gives an initial sticking of **8.57 × 10⁻³** with a reactivation coefficient of **0.35**,
hence

> **ω_eff = 0.557 percent**, against three independent high-density measurements in 2001 of
> **0.532**, **0.515** and **0.505 percent**.

The operative sticking is therefore **3.74** times what this paper used. That single ratio is also the
explanation of the over-prediction §5.27 reports: at the corrected value the service-life model
reproduces the 150 cycles measured at Los Alamos instead of returning 335.

**What follows is a cap, not a shortfall.** The service life is bounded by 1/ω_eff **at any density
whatsoever**, because the sticking term does not scale with density and the cycle term saturates
against it. Taking the most favourable witnessed value:

| | witnessed |
|---|---|
| cycles per binder, ceiling | **198** |
| energy returned per binder, raw fusion | **3.48 GeV** |
| energy returned per binder, with the sourced blanket | **5.16 GeV** |
| beam energy per binder, floor (§5.1, corroborated at 0.982) | **11.13 GeV** |

> **On witnessed quantities alone, muon-catalysed d–t fusion returns at most 0.464 of the energy
> required to make its binder — 0.313 counting the fusion yield alone.** This is a ceiling at perfect
> collection, unlimited density and zero impurity. It is proven, and it is negative.

**The reactivation coefficient is not a free parameter, and this paper measured it.** R is the
probability that the muon is stripped back off the alpha while the (αμ)⁺ ion slows. Integrating the
stripping cross-section against the stopping cross-section along that path, **the density cancels
identically** — both are per-atom quantities and the path length goes as the inverse of the number
density. R is a constant of the d–t system, not a setting. A first-principles integration returns
**0.198** against the literature's 0.35, the difference being the excited-state cascade the estimate
omits; the two agree that R is of that order and that nothing the operator controls moves it.

Three routes to raise it were examined and closed:

| route | verdict |
|---|---|
| compression | dead by construction — the density cancels |
| a high-Z admixture, to strip harder | dead by **11.6** or more: the concentration that would double the stripping loses the muon to that impurity faster than one catalytic cycle completes |
| an external stripping field | reaches **0.64** in the best published rate network, at a sustained **3.28 × 10¹³ W/cm²** that does not exist (§5.20, the companion's §2.6) |

**And this is the proven, unwitnessed specification.** Setting the balance to unity on witnessed
inputs, the cycle closes if and only if **any one** of the following holds. Each is a single number,
each is measurable, and none has been witnessed:

| | required | witnessed | gap |
|---|---|---|---|
| reactivation coefficient | **0.727** | 0.35 | **2.08** |
| effective sticking | **0.234 %** | 0.505 % | 2.16 |
| convertible yield per fusion | **56.2 MeV** | 26.06 MeV | 2.16 |
| beam energy per binder | **5.16 GeV** | 11.13 GeV | 2.16 |

They are one condition written four ways — condition 8 with the service life at its cap — so
satisfying any one satisfies all. **The reaction is proven. Its net-positive configuration is
specified and unwitnessed.** That is the honest terminus of what this paper can establish from
measurement, and the four rows above are what an experiment would have to return.

**The last escape, priced on a computed cross-section rather than a placeholder.** The rate network
that reaches R = 0.64 does so through a factorised external branch, R_X = f_X · P_X · η_X — field
overlap, microscopic stripping probability, and the chance the freed binder rejoins the cycle. In its
best benchmark the first and third are already at **1.0** and **0.996**: saturated. So the whole of
the remaining gap sits in P_X, and P_X depends on one quantity its authors declined to compute,
stating that a microscopic value "would require the bound–continuum transition matrix element of the
αμ system". They used **20 barn** as an avowed placeholder.

That matrix element is hydrogenic and is computed here: **3.684 × 10⁻²³ cm²**, which is **1.84** times
their placeholder — so the true cross-section makes the route *easier* than they assumed, and this
paper reports that before reporting what remains. Inverting the requirement through it:

| | |
|---|---|
| external branch required | **0.580** |
| external branch achieved | **0.447** |
| remaining gap | **1.30** |
| photon fluence required | **2.37 × 10²² /cm²** |
| **sustained intensity required** | **2.59 × 10¹³ W/cm²** |

> That figure is derived here from a stripping-probability inversion, and §5.20 derived
> **2.21 × 10¹³ W/cm²** from a photoionisation rate against the binder's decay. The two share no step
> and agree to **1.17**. **The requirement is corroborated.**

**And it must be sustained, which closes the pulsed-source escape.** A duty cycle enters as f_X, the
field's overlap with the residual stuck population, and the same rate network shows the gain
collapsing as f_X falls — a pulsed source at duty *d* buys *d* times the benefit. The requirement is
therefore on the **time-averaged** intensity over the fuel volume, where the strongest hard-X-ray
sources sit orders of magnitude lower than free-electron peak figures suggest.

**So the last escape is quantified rather than dismissed**: it needs a sustained hard-X-ray field of
about 2.6 × 10¹³ W/cm² over a reactor fuel volume. That is the whole of what stands between the
witnessed cap and a satisfied condition 8, and it is one number.

**What this does not say.** It does not say cold fusion fails: §§1–3 establish that the reaction is
defined, unique, demonstrated and reproducible, and none of that is touched. It does not say the
specification is unreachable — the field-assisted route reaches 0.64 of the 0.727 required, which is
a factor of 1.14 in a quantity nobody has optimised. And it does not price the bred-fuel product,
which §5.18 reaches unity on: that route is a fusion–fission hybrid whose credit the same beam's
spallation neutrons would dominate, so it is not this paper's subject and should not be read as one.

### 5.27 What the independent literature does to these figures

Four independent results were published while this analysis was being done, and the reconciliation is
a paper of its own [15] rather than a section here, because it is a different kind of work: this
section states what it establishes and what each result does to the figures above.

**Corroborated from outside, and none of it this paper's own.** Condition 8 has been derived
independently as a Lawson-inspired cycle-closure criterion, whose conditional sticking no-go
rearranges term for term into it. A second independent analysis proposes the same fission-breeding
escape as §5.18, for the same reason. A third arrives within a factor of **1.48** on the field the
stripping route demands. And an independent blanket accounting gives 26.0 MeV per fusion against
§5.19's **26.06** — two calculations sharing no input, agreeing to better than a quarter of a percent.

**Three corrections, and they are stated rather than absorbed.**

| correction | what it does |
|---|---|
| an optimised target is calculated at **4.69 GeV** per pion against this paper's **11.13** | multiplies every balance above by **2.37** for a reader who prefers the simulation. This paper keeps the measured figure, because a status is never flattened — and §5.27 below now identifies the difference as a *normalisation*, per beam particle against per interaction, reproducing it to 0.8 percent while declining to adopt it. |
| transfer to a high-Z contaminant is a binder-loss channel neither analysis modelled: **5.49 ppm** costs as much binder as decay at the bracketed density | every balance above assumes perfect purity and is an overestimate by an unquantified factor. §3 now carries the requirement. |
| the service-life model returns **335.3** cycles at the conditions of the one measurement it can be checked against, where **150** were measured | **2.24** over-prediction. Every figure above computed at the "bound case" inherits it; §5.18's and §5.23's bred-fuel figures, computed at the measured cycle count and a sourced blanket, do not. |

**And one result closes an axis this paper left open.** The stripping route of §5.20 is now quantified
and capped: at near-perfect post-stripping recycling it buys **1.39** in cycles, against a collection
factor of 1.64 to 3.33, and it is limited by transport of the freed binder rather than by the field.

**And the production figure is now confirmed independently, by inverting a published yield.** §5.24's
acceptance model can be run backwards: a captured-muon yield divided by the delivered fraction is the
pion production that must have fed it. Applied to the front-end simulation's own tabulated yield at
4.1 GeV, that returns **0.375** π⁻ per interacting proton and therefore **10.93 GeV** per π⁻ —
against this paper's HARP-integrated **11.13**, an agreement of **0.982**. The two share the cross
sections but share neither the integration, the acceptance convolution, nor the normalisation. **The
spine of the production argument is corroborated.**

**Which means this paper's explanation of the 4.69 GeV figure was wrong, and it is corrected here.**
§5.26 attributed the difference to target thickness — a long rod letting secondaries produce pions
that a thin target lets escape. The same source's own table refuses that: measured per interacting
proton, going from 0.05 to 2 interaction lengths buys **0.963** at 4.1 GeV and **1.186** at 11.1 GeV.
**Thickness is worth between 0.87 and 1.19, never 2.37.** **And the discrepancy is now resolved, by a mechanism that reproduces it rather than bounding it.**
Four candidates have been examined. Target thickness *per interacting proton* is refuted by the
source's own table, just above. The phase-space coverage of §5.1 is bounded at 1.10 — and §5.29 now
closes it at **1.072**. Beam energy was the last candidate, and HARP settles it: the same lead target
at 3, 5, 8 and 12 GeV/c costs **18.231**, **12.604**, **11.202** and **11.634** GeV per π⁻, a broad
optimum near 8 GeV/c. **Going down to the optimised study's 3.61 GeV makes production 1.63× dearer,
not 2.37× cheaper**, so that candidate is refuted in the direction opposite to the one it was proposed
in.

**What survives is not a physics gain. It is a normalisation.** The optimised figure is **0.77** π⁻
per *beam deuteron*; every figure in this paper is per *interaction*. If each interacting nucleon
behaves as a HARP proton at its own energy, that yield requires **1.94** interacting nucleons per beam
deuteron at 5 GeV/c and **4.68** at 3 GeV/c — and a deuteron carries **2** nucleons into a rod of
**6.3** interaction lengths of tungsten, so the lower end of that range is guaranteed before any
secondary interacts. Re-normalising this paper's own figure, **2.389** interacting nucleons per beam
particle return **4.688** GeV per π⁻ — the optimised figure to **0.8 percent**.

> **The 2.37 is the number of interacting nucleons per beam particle.** It is explained — and the
> reabsorption doubt that kept it from being adopted is now settled. The collector takes *large-angle*
> pions, which leave the target **sideways**, so their escape path is the target's radius and not its
> length: a narrow target is transparent however long it is. The companion's §11.1 puts the escape at
> **0.8961** for the published geometries, which are long and thin for exactly this reason. **The gain
> survives to capture.** Every balance here still uses the measured per-interaction figure, because a
> status is not flattened by an argument — but the reason for withholding it is gone, and §10.3 now
> measures a quantity whose sign is predicted rather than unknown.

**§10.3 changes accordingly, and changes to something sharper.** It is no longer a species comparison
looking for an unknown mechanism. It is a **normalisation measurement**: pions per *beam particle*
against pions per *interaction*, on one target at matched beam power, which is the one quantity that
decides whether the factor of 2.389 survives to capture. This paper's earlier reading of that stage,
and its earlier confidence in the 4.69 figure, are both withdrawn — and so is its statement that the
gap is unexplained.

**One result the companion states and this paper should carry, because it is the mirror of §5.22.**
Solving each balance for the *density* at which it equals one rather than for the collection
efficiency, the bred-fuel route breaks even at **0.222** times liquid density at perfect collection
and **0.604** at today's aperture — below liquid density, so it needs no compression at all. **For the
heat and work forms there is no such density.** On the corrected sticking of §5.26 the service life
saturates at **198** cycles and both require more than that, so compression cannot reach them at any
value whatever. §5.13's structural bound on density is therefore not what stops them; the sticking
cap is.

**The asymmetry across all of it is the same one §5.23 found.** Every correction weakens the routes
that depend on a modelled service life and a compressed target; none of them touches the bred-fuel
route at demonstrated cycle counts, which uses neither.

### 5.28 The species: which pion, and what that requires of the target

Every yield in this paper is a π⁻ yield. That was stated once and then assumed everywhere; it is
measured here, because the assumption sits underneath the production figure, the acceptance model and
the whole of §10.

**Only one sign catalyses, and the reason is not a detail of rates.** A μ⁻ replaces an electron and
binds a nucleus. A μ⁺ does the opposite: it binds an *electron*, into muonium, and is repelled by
every nucleus in the target. It forms no mesomolecule at any density or temperature, so it enters no
cycle, sticks to no alpha and catalyses nothing. The catalytic cycle exists for one sign of one
particle. And a μ⁻ has exactly one parent — π⁻ decay — so of everything a production target makes,
only the π⁻ half is buyable at all. An accounting that quotes pions or muons without a sign is not an
accounting of this reaction.

**The split, measured rather than halved.** HARP published both charges off the same lead target, in
the same bins, with the same beam [3]. Integrated over everything the two spectrometers covered:

| region | σ(π⁻) | σ(π⁺) | π⁻/π⁺ |
|---|---|---|---|
| large angle, 0.35–2.15 rad | 1.038 b | 1.067 b | **0.973** |
| forward, 0.025–0.25 rad | 0.184 b | 0.248 b | **0.742** |
| all of it | | | **f(π⁻) = 0.4816** |

**π⁻ is the minority channel**, and for a proton beam it has to be: the projectile carries two units of
charge into the final state and the pions carry some of it back. Halving a both-charge yield therefore
*overstates* the usable half — over production as a whole, by 3.8 percent.

**But no collector takes production as a whole, and the part it takes runs the other way.** The split
is strongly momentum-dependent, and the direction is the useful one:

| π momentum, GeV/c | 0.10–0.15 | 0.15–0.20 | 0.20–0.25 | 0.30–0.35 | 0.45–0.50 |
|---|---|---|---|---|---|
| π⁻/π⁺ | **1.354** | **1.016** | 0.967 | 0.920 | 0.866 |

Running §5.24's acceptance model over each charge in turn — the same transverse cap, the same
two-body decay integrated over the pion rest frame, the same rf window, nothing changed but the table
it reads — gives the fraction that actually reaches the channel:

> **f(π⁻) accepted = 0.5084**, against 0.4816 produced.

**So the halving stands, and it now stands measured.** It differs from the accepted fraction by
**1.7** percent, inside the **3** percent normalisation uncertainty HARP quotes for its own lead data.
It is *not* adopted as a correction and no figure in this paper moves: a shift smaller than the
uncertainty of the measurement that found it is a bound, not a value, and 37.0 GeV per captured μ⁻ and
11.13 GeV per π⁻ are unchanged. What is removed is an unexamined assumption, and what replaces it is
the finding that the assumption was safe — and safe for a reason, not by luck. The collector's window
is a low-momentum, large-angle window, and that is exactly where a neutron-rich target's π⁻ excess
lives.

**What the species does settle is the target, and that is not a detail either.** The same two tables
run against aluminium:

| target | N/Z | π⁻/π⁺ | f(π⁻) |
|---|---|---|---|
| lead | 1.537 | 0.973 | 0.4930 |
| aluminium | 1.077 | 0.732 | 0.4226 |

A factor of **1.329** in the ratio. At equal *total* charged-pion yield a low-Z target delivers
**0.857** of lead's π⁻, the remainder going to the sign that cannot catalyse — and aluminium shows no
low-momentum excess at all, which is HARP's own reading of its data: the effect appears in lead and
tantalum and *"lower-A targets do not show this behaviour"* [3]. **A high-Z target is therefore
required for the charge and not only for the yield.** §10's tungsten rod already satisfies it. The
requirement was met without being stated; it is now stated, and it belongs in the bill of materials
rather than in a footnote about cross sections.

**And it closes a lever before anyone proposes it.** If π⁻/π⁺ rises to 1.354 at low momentum, why not
select there? Because the selection is priced: the best single bin reaches **f(π⁻) = 0.5753**, worth
**1.132** on the accepted fraction, and costs all but **14.7** percent of the π⁻ yield to reach. It is
a factor of 1.13 bought with a factor of 6.8. **Charge selection is not purchasable**, which is the
same shape as §5.25's finding about the stopping window: a term that looks like a lever, priced, turns
out to be a constraint.

> **The species is μ⁻, from π⁻, off a high-Z target.** Nothing in the balance moves. One line moves
> into the specification.


### 5.29 What one measurement settles: the sticking, the model, the fuel and the wedge

Four things this paper carried as open were calculations it could already do. They are done here.
None of them needed a new measurement; three of them needed only the one measurement nobody disputes.

**The witnessed cycle count, read backwards.** The service-life expression takes a sticking and returns
a cycle count. Run the other way it takes the **150** cycles measured at Los Alamos and returns the
sticking that produced them — by a route that uses **neither published sticking measurement**:

> **ω_eff = 0.5171 percent** at φ = 1.2, **0.5471 percent** at φ = 1.5.

That is a third independent determination of the quantity every balance here turns on, and it lands
**inside** the measured trio of 0.505, 0.515 and 0.532 percent and **below** the coupled-channels value
of 0.557. §5.26 adopted the measured band over theory on the grounds that a witnessed value outranks a
computed one; the cycle count now says the same thing from a different direction.

**And it disposes of the 2.24 over-prediction without a new hypothesis.** §5.27 records that the
service-life model returns 335.3 cycles where 150 were measured, and leaves open whether the cause is
"a density-dependent reactivation term or an unrealised reduction". It is neither. At 0.515 percent the
model returns **150.5** cycles. **The over-prediction was the sticking and nothing else**, and the
question is closed rather than deferred to Stage B.

**The same measurement bounds the fuel.** §9 records that every balance here assumes perfect purity and
that no experiment bounds it. One does — the same one. A contaminant costs binder, so the fuel that
returned 150 cycles cannot have carried more than the amount that would have pushed the model below
150. Across the sticking and density bracket that is **0 to 10.93 ppm**, and in every case below the
**31.10 ppm** at which impurity loss equals decay loss. **The witnessed cycle count already carries its
own purity.** The limit stands for the *modelled* figures of §§5.11–5.24, which assume a purity no
experiment has demonstrated; it does not stand for any figure computed at the measured 150.

**And the uncovered wedge is now a value rather than a bound.** §5.1 records that HARP's two
spectrometers leave **0.1856 sr** between 0.25 and 0.35 rad uncovered, and bounds its worth at 1.10.
Their per-steradian densities can be log-interpolated across it in the momentum band where the two
tables overlap, carrying the large-angle spectrum's shape:

> the wedge adds **0.0876 barn** to 1.2220 — a factor of **1.0717**, and production is **10.385 GeV**
> per π⁻ rather than 11.130.

It is `RECONSTRUCTED` and not measured, because the two tables cover different momentum ranges and no
interpolation returns the wedge's own spectrum. **The balances in this paper are not restated at
10.385**: a reconstructed figure does not replace a measured one, and the 7.2 percent it would add is
recorded as headroom rather than banked. What it does retire is the *bound*: the wedge is not worth
1.10, and cannot be invoked as though it might be.

### 5.30 The acceptance model, and the limit of its scope

§5.24 validates the acceptance model against the built front end's own MARS15 simulation, at 20 tesla
on a 7.5 cm bore, forward hemisphere, to **0.982**. That is its only check, and this section records
an attempt to add a second that failed — and what the failure establishes instead.

**The attempt.** A 5 T capture solenoid on a **0.15 m** bore is an aperture this paper's p_T formula
already reproduces (112.5 MeV/c against a stated 100). Evaluated there, the model returns **0.0843**
captured π⁻ per interacting proton against that machine's published **0.061–0.144** — inside, and
apparently a corroboration at a quarter of the field.

**It is not one, and the reason is the hemisphere.** That machine's transport solenoid takes
*"backward-emitted secondary pions and muons"* [16] — the opposite of the front end §5.24 is validated
against, which Strait et al. §II states captures forward. Run in the hemisphere it actually uses:

> **0.0073** against a published **0.061–0.144**. The model is low by **14.1×** against the
> midpoint of that range, not inside it.

**And that is a scope limit rather than a disagreement.** A graded capture solenoid magnetically
*mirrors* forward-going particles back into a backward channel — it is why such machines are graded —
and this model has no mirror term at all, only a transverse momentum cap. **Against a graded field the
model is a lower bound and not an estimate**, by a factor it cannot state.

> **The acceptance model has one validation, at one configuration: 0.982, forward capture, 20 T on a
> 7.5 cm bore — which is exactly the configuration §10 and the companion's §6 specify.** It may not be
> quoted as validated anywhere else, and a backward-capture graded-field machine is the demonstration
> that it may not.

**Two statements are withdrawn here, both the companion's §7 and both this paper's to carry.** The
first quoted a *span* on the acceptance — 2131×, then 5.97× — by treating that 5 T machine's output as
a lower estimate of the 20 T machine's; it is a different machine, not a lower estimate, and the span
was never an uncertainty. The second replaced it with a claimed second corroboration and used the
wrong hemisphere to get it. **The width of what is known about the acceptance is the width of one
agreement, 0.982 to 1.000**, at one configuration, with an unquantified conservative bias from the
missing mirror term.

**And the scope limit has since been removed rather than lived with.** The companion's §8 designs the
capture solenoid, which supplies the mirror term this model lacked: reflection when
sin θ ≥ √(B_t/B_max), the reflected pion re-entering the same transverse cap and the same decay
integral at π − θ. It is worth **1.299**, and it saturates at a grade of **1.428** because that is where
HARP's table ends. **The model is therefore no longer a lower bound against a graded field** — it now
models one — and this section's finding stands as the reason the term exists rather than as a
standing limitation.

**What is open is unchanged by any of it.** Nothing has been measured end to end. §10.1 measures it,
and no calculation in this work stands in for that.

### 5.31 Every balance at the acceptance actually delivered

§5.19 states each balance at **30** and **90** percent collection, and §5.19 was right to prefer that
to perfect collection. **The 90 percent is nevertheless unreachable**, and this section restates the
table at what is delivered instead. `python3 tools/machine.py --balances` reproduces it.

**Two results stand between §5.19 and this one.** The companion's §7 shows the *stopping* ceiling is
**0.5069** at any target depth — a muon the solenoid accepts but the fuel does not stop is not a
binder — so 90 percent was never available. And its §11 computes every loss between a produced π⁻ and
a stopped binder at **0.7127**, putting the delivered figure at **31.66 percent**, or **37.62** at the
wider bore.

**The restatement is exact rather than approximate.** The balance is linear in collection, and §5.19's
own two columns check it: every row's ratio is **2.998 to 3.010** against 90/30 = 3.000.

| balance | as printed at 90 % | delivered, 31.66 % | wider bore, 37.62 % |
|---|---|---|---|
| heat, demonstrated 150 cycles | 0.316 | 0.111 | 0.132 |
| heat, bound-case service life | **1.241** | **0.437** | **0.519** |
| heat, φ = 3 | 1.011 | 0.356 | 0.423 |
| work, demonstrated 150 cycles | 0.237 | 0.083 | 0.099 |
| work, bound-case service life | 0.931 | 0.328 | 0.389 |
| bred fuel, demonstrated 150 cycles | 1.772 | 0.623 | 0.741 |
| bred fuel, bound-case service life | 6.96 | **2.449** | **2.909** |

### 5.32 What this withdraws, and what survives

> **The heat form's 1.241 does not survive.** At the delivered acceptance it is **0.437**, and at the
> wider bore **0.519**. The figure was never wrong — it was stated *at 90 percent collection* and it
> stands as that conditional. **What is withdrawn is reading it as an end-to-end result**, which this
> paper's own abstract did: *"the heat form still passes at 1.241 … so the self-sustaining criterion
> is met without leaving the device."* **It is not met without leaving the device.** That sentence is
> withdrawn.

**What survives is one route, and it is the one the companion already builds for.**

**Bred fuel through an optimised production target.** §5.24 puts its requirement at **21.4 percent**
against **31.66** delivered — a balance of **1.480**, and **1.758** at the wider bore. That route
depended on whether the optimised target's gain is real, which was the open half of the 2.37; §11.1
of the companion answers it on geometry, at **0.8961**. **The two results that would separately have
closed this route and opened it are the same pair**, and §11.4 of the companion states the coupling.

**And bred fuel on the bound-case service life**, at **2.449**. That case rests on the service-life
model §5.29 corrected, and §5.26 caps cycles at **198**. It is read against that cap and not offered
as an independent route.

**Everything else falls below unity at the acceptance this machine delivers** — every heat form, every
work form, and bred fuel at the demonstrated cycle count without the optimised target. That is the
honest end-to-end state of the balance, and it is narrower than any earlier section of this paper
implies.

## 6. What the definition excludes

| excluded | grounds |
|---|---|
| electron-bound systems | geometry: 74100 femtometres, some 91 orders short |
| tau and heavier binders | the molecular index degenerates; no edge cell |
| hadronic binders | nuclear absorption preempts catalysis |
| enhanced ambient screening | conservation, below |
| the cryogenic operating branch | thermodynamics, below |
| excess heat without commensurate ash | baryon number: every branching predicts heavy ash per unit energy within a narrow window |
| thermal and inertial fusion | by definition — approach supplied by kinetic energy |
| chain multiplication of binders | no nuclear event releases enough to fund one |

**The ambient exclusion.** At thermal energies the deuteron-to-electron velocity ratio is deeply
adiabatic, where static screening is exact; beam measurements sit far faster and squarely
non-adiabatic, so the measured enhancement belongs to a different regime. And a static screening
energy is bounded by what the electron system can donate: the complete site inventory ceilings at 30
electronvolts against a requirement of 88, a factor of 2.9 in energy and some 27 orders in rate. The
bound is conservation-grade and admits no mitigation by vacuum, geometry, cooling or channel choice.

**The cryogenic exclusion.** Below ambient, fusion heat can do no work and costs more to remove than
it delivers. A reactor cannot be net-positive while cold. Above ambient the recovered fraction is
fixed by the blanket rather than the fuel, so the operating point is hot and pressurised.

## 7. Provenance and verification

**Measured, from primary or surveyed literature:** the fusion yield 17.59 MeV; the transfer rate
2.7e8 per second with its uncertainty 0.9e8; bound-binder disappearance 4.665e5 per second; free
lifetime 2.197 microseconds; final sticking 0.45 and 0.56 percent; the molecular binding 0.66
electronvolts against the vibrational quantum 0.365 and the ground state 319; the exit branching
99.14 and 0.86 percent; the neutron at 14.1 and alpha at 3.5 megaelectronvolts; the observable line at
8.2 kiloelectronvolts; the separations 280 and 74100 femtometres; the masses 207 and 273 electron
masses.

**Sourced, and named to their table:** the captured yield 0.054 per interacting proton per
gigaelectronvolt, from HARP cross sections convolved with a MARS15 front-end acceptance at 20 tesla on
a target of 2 interaction lengths; the flat band from 4 to 11 gigaelectronvolts with optimum near 7.

**Projected, and not demonstrated:** sticking at 0.34 percent by dual polarisation, 0.31 by the
excited molecular state, and 0.234 composed from them. **The composed value inherits an unresolved
figure**: its source does not settle whether the 0.31 is initial or post-reactivation sticking, and
every quantity computed at 0.234 in this paper carries that reservation.

**Derived here, and recomputed by instrument:** the cost per binder 37.0 GeV; the figure of merit
0.203 and 0.102; the shortfalls 4.9 and 9.8; condition 8 at 7.52 and 3.77; the headroom 123 and the
margins 25.1 and 12.6; the service lives 222, 427, 196 and 340; the velocity ratios 2.97 and 1.66; the
convertible fraction 0.501 and its parts 19.9, 80.2 and 62 percent; the recosted historical gain
0.071.

**Sourced from independent recent work, and named to it:** the optimised production target's 0.77
π⁻ per beam particle at 3.61 GeV on tungsten [9]; the μCF fission-breeding hybrid concept and the
Table I kinetics of [10]; the diamond-anvil-cell operating envelope, 933 MPa at 400 K, and the muon
transfer rate to oxygen near 1 × 10¹⁰ s⁻¹, from [11]; the cycle-closure criterion, its 20.4 MeV useful
cycle energy and its historical anchors at 124 and 150 fusions, from [12]; the external-stripping rate
network, its 7.2 × 10⁷ J/cm² reference fluence and its 112.6 to 156.5 yield gain, from [13]; and the
coupled-channel initial sticking 8.57 × 10⁻³ with intramolecular fusion rate 1.15 × 10¹² s⁻¹ from [14].
**None of these is adopted in place of a figure this paper derives**; each is carried beside it, and
The companion's §§2.2–2.6 state what each does to the balances if a reader prefers it.

**Bounds, never targets:** the kinematic floor at 0.30 GeV, and the sticking asymptote 1/ω_s.

**Known to be wrong in a stated direction:** the service-life model, which over-predicts its one
checkable point by **2.24** (the companion's §2.5). Every figure computed at the "bound case" inherits that; no
figure computed at the measured 150 cycles does.

## 8. What this paper retires

**Withdrawn from *Muon-Catalysed Fusion* v1.0 and v1.1:**

1. That the two gaps are independent. They are one chain: the cost per binder produced and the number
   delivered per second are the same quantity at two thresholds.
2. That the energy threshold requires two sticking levers. It requires either those or a reduction in
   binder cost, and §5 prices both.
3. That the binder costs 5 GeV. That figure is aspirational; the best studied is 37.0, and the
   earlier value is not achieved by any machine.
4. That density should be as high as cryogenics permit. Cryogenics is the lever that eats the output.
5. A table row computed at the unrounded transfer rate rather than the saturation value pinned beside
   it. All figures here use the saturation value.
6. That the sticking ceiling is a service life. It is an asymptote in density.

**Withdrawn from *The Muon Collection Budget* v1.0:**

7. That the production floor is the kinematic threshold. It is not: the threshold is a bound, and the
   studied production and capture figure is 123 above it.
8. **That proton energy is a lever.** The yield is flat within a tenth of optimum from 4 to 11
   gigaelectronvolts. The earlier claim extrapolated from a single low-energy demonstrator point,
   which shows only the falloff below that band.

**Considered and withdrawn before publication:** that conditions 1–8 admit no solution at all. That
conclusion required assuming the muon's ratio of production cost to rest mass generalises to every
binder, which is unsupported. §5 states the position that survives: the set is not empty, and the
requirement lies inside the headroom.

**Withdrawn at §5.24, by working a number this paper had assumed.** Two claims fall together. First,
that physics front ends capture the backward hemisphere only: they capture the **forward** one, which
is also the larger, so dropping the cut is worth **1.20** and not a factor of about six. Second, the
**2.92** this paper reported as the model's favourable margin: it set a backward model acceptance
against a simulation of a forward-capturing machine, with no momentum requirement on one side and an
rf bucket on the other. It compared two different quantities and nothing replaces it — the model now
reproduces the simulation directly, to **0.982**, and needs no margin.

**Found late and not repaired, because repairing it would be a choice this paper has no grounds to
make.** The companion's §2.5 shows the service-life model over-predicts the one measurement it can be checked against
by a factor of **2.24**. The paper carries the finding rather than adjusting the model, states which of
its figures depend on the model and which do not, and names the measurement that would decide it
(§10.2). A model that fits its only checkable point by construction would be worth less than one that
records where it does not.

## 9. Limits and the state of the question

The captured-yield figure is a simulation convolved with measured cross sections, not an end-to-end
measurement, and its front-end acceptance embeds a selective requirement a reactor does not share —
which is precisely why §5 declines to convert it into a production limit. The sticking levers are
projections and one of them rests on an unresolved figure. The cross-check against the historical
result is an agreement of two calculations sharing an input, not an independent confirmation. The
velocity-ratio expression reproduces two measured sticking values and is used for no third. And this
paper computes no absolute rate: it prices a binder and compares that price to a bound, which is the
whole of its claim.

**The service-life model over-predicts its one checkable point by 2.24**, returning 335.3 cycles at
Los Alamos conditions where 150 were measured (the companion's §2.5). Every "bound case" figure in §§5.11–5.24 rests
on that model; the bred-fuel headline figures do not, using the measured 150 and the sourced blanket
instead. Whether the discrepancy is a density-dependent reactivation term or an unrealised reduction
is not settled here, and §10's Stage B is what settles it.

**Three limits added late, and each runs against the result rather than for it.** Every balance here
assumes **perfectly pure fuel**, and the companion's §2.4 shows a contamination of **5.49 ppm** costs as much binder
as decay does at the bracketed density — so all of them are overestimates by a factor no experiment
here bounds. Every collection figure is an **acceptance and a decay** and not a
delivered-to-target efficiency (§5.24) — transport, cooling and stopping are unmodelled and all three
lose, so every such figure is an upper bound. And the temperature dependence §5.15 relies on is
**confounded with purity and density** in the existing record (the companion's §2.4), so the axis it inverts the
shortfall onto is not cleanly separated from two others.

**The state of the question, plainly.** The reaction is defined, unique, demonstrated, and its
procedure is stated. Condition 8 is a bound on the cost of a binder, and the binder is not the
variable: sticking is mass-independent and the known spectrum holds no alternative. Against measured
production of 11.13 GeV per pion, collection alone cannot satisfy it; the corrected convertible
fraction and the blanket accounting move it a long way; the service-life cap is asymptotic in a
density bounded above by molecular survival. With every lever at a defensible bound and collection
perfect, **the thermal balance passes at 1.286 and the electrical balance reaches 0.965.** The
remaining four percent is inside the uncertainty of several inputs, and every effect not modelled here
runs against it.

**The production figure is corroborated, and the case for improving on it has narrowed.** Inverting an
independent published captured-muon yield through §5.24's validated acceptance model returns
**10.93 GeV** per π⁻ against this paper's HARP-integrated **11.13**, an agreement of **0.982** between
routes sharing no integration and no normalisation. Against that, an optimised target is *calculated*
at **4.69 GeV**, a ratio of **2.37** by which a reader who prefers the simulation may multiply every
balance above. §5.25 withdraws this paper's first explanation of that ratio — target thickness, which
the same source measures at between 0.87 and 1.19 — and leaves the beam species as what survives.

**The shortfall inverts into a specification**, which is what a bound is for. Work breakeven at the
bound case needs an effective sticking of 0.1427 percent against 0.1487 — a reduction of 4.0 percent
— and effective sticking is not a constant but ω_s⁰(1 − R), whose reactivation term has been measured
to move by 26 percent over eleven kelvin. The paper's operating point is 800 K and no determination
exists there. The last four percent therefore lies on an axis this analysis holds fixed and the
physics does not.

**Where the balance actually closes, and on which product.** The paragraph above prices the neutron
at its heat, which is what the analysis did until §5.18. Counted as bred fuel — the fissile nucleus a
fusion-breeder blanket makes, on sourced fission-suppressed figures — the value per fusion is
146.06 MeV rather than 26.06, and those same sourced figures lift the electrical balance from 0.965 to
**1.034**. The breeding balance at the demonstrated 150 cycles with the §5.9 collector is **1.77**.

**§5.22 states that as a specification on the collector alone**, which is the sharpest form the result
takes. Electricity breaks even at **299.6 percent** collection and needs the bound-case density and the
favourable sticking branch besides; bred fuel breaks even at **12.9 percent** at that same bound case
and at **50.8 percent** at cycle counts already demonstrated in a laboratory, asking nothing of the
density axis, the sticking measurement or the reactivation term. The product choice is therefore worth
**7.5** in collector specification, and what stands between the eighth condition and a satisfied one,
on the product the definition permits, is **1.69** in collection efficiency above today's measured
front end — inside the §5.9 collector, whose cost §5.21 prices as a shielding trade.

**§5.25 answers what this section previously ranked first, and demotes it.** The stopping window the
fuel target imposes is a constraint and not a lever: widening it from 265 to 400 MeV/c costs **1.93**
in tritium inventory for **1.11** in delivered muons, and the inventory does not fall with
compression, because it is areal density times beam area and the areal density is a range. The route
therefore closes on the production target or on the bore, and not on the target's window.

**And §5.24 works the collector's number rather than assuming it, which changes the ranking below.**
The specification has two halves — the hemisphere and the bore — and the earlier claim that the first
was free and worth a factor of six is withdrawn there: the built front end already takes the forward
hemisphere, which is the large one, so the second half is worth **1.20**. At today's aperture the
bred-fuel balance at demonstrated cycle counts is **1.199** with no momentum requirement at all and
**0.968** through a 400 MeV/c stopping window.

What would change the answer, in the order this paper can rank them:

1. **The production target of §10.3.** At the companion's optimised figure the requirement falls from
   50.8 to **21.4 percent**, which every configuration §5.24 computes already meets — including
   today's aperture through the tightest stopping window, at **2.076**. **But that figure is a
   discrepancy, not a result**: §5.26 examines thickness, phase-space coverage and beam species and
   finds none of them accounts for it. This stands first because it is the cheapest measurement and
   because everything else in the list is contingent on how it comes out — not because the gain is
   expected.
2. **The wider bore of §5.9** — 20 T on a 13 cm clear bore, 1.74 times the existing aperture. It
   restores the bred-fuel route through a 265 MeV/c stopping window at **1.039** and a 400 MeV/c one
   at **1.343**, and the heat and work routes need it outright. §5.21 prices it as a shielding trade
   of about 2.7 in coil heating — but §5.25 adds a cost §5.21 cannot see: **3.01 in tritium
   inventory**, because a wider cap is a wider beam and the target must cover it.
3. **Whether the stopping target can sit in the capture field.** §5.25 derives the beam radius from
   the transverse cap and reproduces three published geometries doing it, which closes the term this
   list previously called underived. What remains open is the assumption underneath: that the target
   sits at 20 T and transport is adiabatic and lossless. A target in a weaker field is wider by
   √(B_capture/B_target), and the inventory goes as the square of that.
4. **The sticking measurement of §5.10** — decides a branch, and bears on §5.15's four percent. A
   bench experiment on an existing beam, and the companion's §2.4 records that a collaboration is already running
   the adjacent measurement. It bears on the heat route and not on the bred-fuel one.
5. **Fuel purity, and its separation from temperature and density.** The companion's §2.4 prices the impurity
   channel for the first time: at the bound-case density, a contamination of 5.49 ppm costs as much
   binder as decay does, and every balance in this paper assumes perfect purity. The same measurement
   separates §5.15's temperature reading from a purity reading, which the existing record confounds.
6. **Effective sticking at the operating temperature.** No determination exists at 800 K, though
   §5.20 records the muon-loss dependence measured across 85 to 790 K in the d+d system, in the
   favourable direction.
7. **Where molecular hydrogen ceases to be molecular at 800 K** — much less important than it looked.
   The companion's §2.5 shows the heat route breaks even at **2.10** times liquid density rather than at the bound
   case's 8.5, and the bred-fuel route at **0.730** or less, which is below liquid density. §5.13's
   structural bound therefore constrains only the asymptotic service life, not breakeven on either
   route.
8. **The resonant stripping enhancement** (the companion's §2.1) — no longer unquantified, and its §2.6 is why it stays
   last. An independent rate network puts the gain at **1.39** in cycles against a collection factor
   of 1.64 to 3.33 and a production factor of 2.37, and finds the route limited by post-stripping
   transport rather than by the field. It is the smallest of the three levers and the only one that
   needs a machine that does not exist.

None is settled here. The first two need no new machine, and items 4 to 8 bear on the service-life
axis alone — which is the axis §5.23 shows the bred-fuel route can do without. **The item this list
previously ranked first, the target's stopping window, has been answered at §5.25 and is a constraint
rather than a lever**; it now bounds every figure above instead of promising to lift one.

**And four doors are now shut, which is worth as much as an open one.** The binder is not the variable
(§5.7). The conversion ceiling descends from condition 1 (§5.16). Density is bounded above by
molecular survival (§5.13). And the in-flight route, which would have lifted that bound, is below the
binder's own decay rate (§5.20).

## 10. The laboratory programme

§3 states the procedure for the reaction. This section states the procedure for *deciding the
question* — the experiments that would close what §9 leaves open, written so that a reader with
access to an existing muon beam can execute them. Everything below runs on apparatus that exists.
None of it needs a new accelerator, and only one item needs a new magnet.

Three conventions govern all four stages, and they are the corpus's own:

- **A null is a bound.** Every stage is written so that a negative result yields a number, not a
  disappointment. There is no outcome from which nothing is learned.
- **A disagreement between two independent routes is a refusal, not an average** (§3.5).
- **The prediction is committed before the measurement.** Each stage states below what this paper
  expects and what each outcome settles, so that neither can be adjusted afterwards.

### 10.1 Stage A — the acceptance measurement

**Apparatus.** An existing capture solenoid front end: 20 T on a 7.5 cm clear radius, a field–radius
product of 1.50 T·m. No new magnet.

**The change.** Instrument both hemispheres of pion emission rather than the backward one alone. The
hemisphere cut exists to escape the forward neutron and proton flux of a physics target; a reactor's
target is its detector and has no such background (§5.9, §5.24).

> **And the mechanism that achieves it is now designed rather than assumed.** The companion's §8 grades
> the capture field so that a backward pion is magnetically *mirrored* forward — reflection when
> sin θ ≥ √(B_t/B_max), at a grade of **1.428**. Because that grade puts the loss cone outside every
> angle HARP measured, **mirroring the backward hemisphere and accepting both hemispheres are the same
> number**: the band below is reproduced to four figures by the mirror, and it is reproduced by a
> magnet rather than by an instrumentation choice. This stage asserted a capability; that section
> builds the thing that supplies it.

**Measure one number.** η, the negative muons delivered to and stopped in a dense target per negative
pion produced in the production target. Not the transverse acceptance, and not the capture fraction
of a momentum-selected channel — the delivered figure, end to end.

**Committed prediction.** §5.24's model — production, transverse cap, two-body decay integrated over
the pion rest frame, then a momentum requirement — reproduces the built machine to **0.982** of its
simulated figure, so the prediction here is a calculation and not an estimate. With no momentum
requirement it gives **60.92 percent** over both hemispheres; with a 400 MeV/c stopping window,
**49.16 percent**; with a 265 MeV/c one, **44.43 percent**.

**And those are the model's figures, not η.** This stage measures the *delivered* number, and the
companion's §11 now computes what stands between the two — target escape, decay completeness, muon
survival, scattering out of the transverse cap — as a product of **0.7127**. Through it:

| window | model | **committed η** |
|---|---|---|
| no window | 60.92 % | **43.42 %** |
| 400 MeV/c | 49.16 % | **35.03 %** |
| 265 MeV/c | 44.43 % | **31.66 %** |

**This paper predicts that η falls in that lower band.** What was "transport, cooling and stopping are
not modelled and every one of them loses" is now four terms with numbers on them, and the loss they
carry is **a quarter of the modelled figure**. The margin over the falsification floor below therefore
falls from 1.51× to **1.073×** — a far sharper commitment, and one this paper had not made until the
losses were counted.

**What each outcome settles.**

| η returns | consequence |
|---|---|
| ≥ **50.8 percent** | The bred-fuel route closes at the demonstrated **150** cycles per binder with no other change: no wider bore, no density beyond the scanned record, no resolution of the sticking branch. §5.24 puts this at the top of its computed band and only without a stopping window. |
| **44.43** to 50.8 percent | The band §5.24 computes for realistic stopping windows. The wider bore of §5.9 becomes necessary — **2.60 T·m**, 20 T on a **13 cm** clear bore, which §5.21 prices at about **2.7** in coil heating — *or* the production target of §10.3, which lowers the requirement to **21.4 percent** instead. |
| below **29.51 percent** | Below what the built machine already delivers through a *collider's* momentum window. That would falsify §5.24's model, which reproduces that machine to **0.982**, and every balance in this paper would fall with it. **The committed η of 31.66 percent sits 1.073× above this line**, so the stage is now a sharp test rather than a comfortable one. |

η multiplies every balance in this paper identically, so **whatever it returns is a bound on all of
them at once.** This is why Stage A runs first.

### 10.2 Stage B — the sticking branch, with purity as a controlled variable

**Apparatus.** A high-pressure cell on an existing muon beam — the diamond anvil cell of [11] reaches
**933 MPa** and **400 K** with a **500 K** design ceiling and a **19.2 mm³** sample, which is the
instrument this stage needs.

**Two observables, one target, simultaneously.** Neutrons at **14.1 MeV** give the fusion yield per
binder. The muonic helium K-alpha line at **8.2 keV** counts stuck binders directly. They share no
instrument and no calibration, which is what makes them two routes rather than one.

**Purity is a variable of the experiment, not a precondition of it.** The companion's §2.4 prices transfer to a
high-Z contaminant at about **1 × 10¹⁰ s⁻¹** per liquid density of oxygen, so at the bracketed density
a contamination of **5.49 ppm** costs as much binder as decay does. The existing record confounds
purity with density and temperature — its cleanest data are also its coldest and densest — so a purity
series at fixed density and temperature is part of this stage and not a refinement of it.

**The discriminant.** Initial sticking is fixed at **0.938 percent** by calculation. The two published
final values, **0.45** and **0.56 percent**, carry into the excited-state channel as **0.1487** and
**0.1851 percent**, and the break-point for the heat form at the measured production cost is
**0.1580 percent** — between them, which is why the measurement decides rather than confirms.

**What each outcome settles.** Below the break-point the heat form of condition 8 is satisfied at
perfect collection; above it the residual is **1.17**. If the two routes disagree, §3.5 governs:
report a bound, not a mean.

**And this stage settles the companion's §2.5 over-prediction, which is the larger question.** The service-life
model returns **335.3** cycles at Los Alamos conditions where **150** were measured — a factor of
**2.24** — and returns **166.8** if the excited-state reduction is not applied. A determination of
effective sticking *as a function of density* decides between those two readings, and with it whether
every bound-case figure in this paper is optimistic by that factor. The measurement is the same one;
what this adds is that it must be run at more than one density.

### 10.3 Stage C — the production target, measured rather than simulated

**Apparatus.** A proton or deuteron beam of a few GeV and a thick high-Z target. The configuration to
test first is [9]'s: **3.61 GeV** deuterons on a tungsten rod **652 mm** long and **5.1 mm** across.

**Measure both normalisations on the same target, in the same run.** π⁻ per *beam particle* and π⁻
per *interaction*, for a proton beam and a deuteron beam **at matched beam power**. §5.25 shows target
thickness per interacting proton is not the variable — it is worth between **0.963** and **1.186** —
and §5.27 shows the beam species is not either. **The variable is the ratio between the two
normalisations**, which §5.27 computes as **2.389** interacting nucleons per beam particle, and the
question this stage answers is whether that ratio survives to *captured* muons or is cancelled by
reabsorption in a target thick enough to produce it.

**Committed prediction.** For the deuteron, **0.77** π⁻ per beam particle, giving **4.69 GeV** per π⁻.
For the proton at comparable beam energy, **0.375** π⁻ per interacting proton — the figure this paper
recovers by inverting a published yield, which agrees with its own HARP integration to **0.982**. The
ratio between them is **2.05** per beam particle, and §5.27 accounts for it as nucleon multiplicity.
**What this paper does not predict is that the ratio survives capture**, and the same source's
thick/thin ratio of **0.874** to **1.186** for captured muons is the reason for the doubt.

**What it settles.** It decides which figure a reactor target should be priced at, and it multiplies
every balance in this paper by the ratio it returns. It is the only stage that can improve the result
by more than a factor of two, it is the cheapest of the four, and after §5.24 and §5.25 it is **the
stage that decides the bred-fuel route**: at the companion's figure the requirement falls to
**21.4 percent**, met by every configuration §5.24 computes, whereas no stopping window reachable in
§5.25's inventory table closes the route at the measured production cost. **Run this one first.**

### 10.4 Stage D — the integrated demonstration

**This is not a reactor and should not be built as one.** It is the smallest system that measures the
paper's actual claim, which is a product of three factors and nothing else:

> binders delivered per beam joule (Stage A and C) × cycles per binder (Stage B) × value per fusion

**What it needs from the earlier stages.** η from A, the service life from B, the target from C. What
it does *not* need, if Stage A returns at or above 50.8 percent: a wider bore, a density beyond the
scanned experimental record, or any improvement in sticking.

**And what it costs before any of that: tritium.** §5.25 shows the fuel target must be one muon range
deep at the top of its momentum window, so the demonstration's inventory is set by the window it
accepts and by the beam's area, not by its density — and the beam's area is itself derived, not
chosen. At today's aperture that is **3.59 kg** at a 265 MeV/c window and **6.93 kg** at 400 MeV/c;
at the wider bore, **10.79 kg** and **20.82 kg**. **On the machine the companion's §§8–10 design it is
5.13 kg**, because that design trades target field for bore and then recompresses at the cell; the
figure is a consequence of the magnet and is computed there rather than assumed here. That is the demonstration's leading cost and its leading licensing
constraint, and it should be designed against first: a narrower window is cheaper in tritium than a
wider one is valuable in muons, by 1.93 against 1.11.

**What it measures and what it does not.** The measured output is **neutron production per beam
joule**. The bred-fuel product's **146.06 MeV** per fusion is realised downstream in a separate
blanket and fission cycle, so the demonstration measures the neutron rate and the blanket accounting
is *applied* to it, not measured by it. **This is the demonstration's limit and it should be stated in
its own report**: it can establish the neutron source and cannot, by itself, establish the credit.
A demonstration of the heat form instead — measuring **26.06 MeV** per fusion as deposited energy —
is a device-internal measurement with no downstream credit. §5.23 puts it at **1.241** with the §5.9
collector and the bound-case service life, **but §5.31 shows that figure is stated at a collection
efficiency the machine cannot reach: at the delivered acceptance it is 0.437.** The heat form is
therefore the more self-contained demonstration and **the one that does not close**. Stage D measures
the neutron rate either way; what it cannot do is make the heat form pass.

### 10.5 The order, and what none of it requires

**Stage C first.** It was written third because it was found third; §5.24 and §5.25 have since made it
the stage that decides the route. It is the cheapest measurement, it would price the route at
**1.73 kg** of tritium per unit of balance against the wider bore's **10.4 kg** — a factor of **6.0**
on the axis that will govern licensing — **and the figure that promises all of that is now explained
but not adopted** (§5.27): it is a normalisation, per beam particle against per interaction, and
whether it survives to *captured* muons is exactly what this stage measures. Running it first is how
the programme finds out whether its cheapest lever is real before spending anything on the others. Stage A next: it bounds every other
result and needs no new hardware, and §5.24 has already computed what it should return. B is
independent of both and can run in parallel. D follows all three.

**None of the four requires a new accelerator, and none requires new physics.** The single item that
requires new hardware is the wider bore of §5.9, and Stage A is designed to determine whether it is
needed at all.

## References

1. S. Cook *et al.*, *MuSIC: delivering the world's most intense muon beam*, arXiv:1610.07850;
   Phys. Rev. Accel. Beams **20**, 030101.
2. J. Strait, N. V. Mokhov and S. I. Striganov, *Towards the optimal energy of the proton driver for a
   neutrino factory and muon collider*, Phys. Rev. ST Accel. Beams **13**, 111001 — Table II and §V.
3. M. G. Catanesi *et al.* (HARP Collaboration), Phys. Rev. C **77**, 055207; A. Bolshakova *et al.*,
   *Large-angle production of charged pions by 3 GeV/c–12.9 GeV/c protons on beryllium, aluminium and
   lead targets*, Eur. Phys. J. C **63**, 549 — Tables 5–8, both charges; and M. Apollonio *et al.*,
   *Forward production of charged pions with incident protons on nuclear targets at the CERN PS*,
   Phys. Rev. C **80**, 035208 — Tables XXII, XXIII and XXXII, both charges.
4. Mu2e Collaboration, *Mu2e Conceptual Design Report*, FERMILAB-TM-2545, arXiv:1211.7019.
5. COMET Collaboration, *COMET Phase-I Technical Design Report*, arXiv:1812.09018.
6. Variational three-body calculation of muon-alpha sticking, Phys. Rev. A **34**, 2536.
7. S. E. Koonin and M. Nauenberg, *Nature* **339**, 690.
8. M. Lach, *The Method* v1.2-8 — *The Lach Cylinder: an index of transitions*.
9. R. Spencer Kelly, L. J. F. Hart and S. J. Rose, *An investigation of efficient muon production for
   use in muon catalyzed fusion*, J. Phys. Energy **3**, 035003.
10. X. Yin, W. Kou and X. Chen, *Muon-Catalyzed Nuclear Fusion: Physical Mechanism, Bottleneck
    Breakthroughs, and an Engineering Pathway*, arXiv:2605.26432 — Table I and §IV.B.
11. E. Koukina *et al.* (MuFusE Collaboration), *Design and Commissioning of a Deuterium-Tritium Gas
    Delivery System for Muon Catalyzed Fusion in a Diamond Anvil Cell*, arXiv:2606.19304; and
    J. D. Kalow *et al.*, arXiv:2606.05333.
12. W. Kou and X. Chen, *A Lawson-inspired Cycle-Closure Criterion for Deuterium--Tritium
    Muon-Catalyzed Fusion*, arXiv:2607.10989 — Eqs. (11)–(13) and Table I.
13. W. Kou and X. Chen, *External-Field-Assisted Muon Reactivation in Muon-Catalyzed Fusion: A
    Rate-Network Criterion for Reducing Alpha Sticking*, arXiv:2606.07077.
14. M. Kamimura, Y. Kino and T. Yamashita, *Comprehensive study of muon-catalyzed nuclear reaction
    processes in the dtμ molecule*, Phys. Rev. C **107**, 034607 (2023).
15. M. Lach, *The Binder Economy Against the Recent Literature: Four Independent Results, and What
    They Correct*, v1.0 — the companion reconciliation paper.
16. K. Oishi *et al.*, *Development of the Range Counter for the COMET Phase-α Experiment*,
    arXiv:2505.07464 — §1, which states the backward-emission capture and the thin production target.
