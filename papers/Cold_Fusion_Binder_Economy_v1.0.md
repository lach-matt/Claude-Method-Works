# Cold Fusion and the Binder Economy: A Closed Definition, a Unique Realisation, and the Bound That Decides It

**Matthew Lach** — Independent researcher
*v1.0, 6 September 2026. Prepared with a computing collaborator under the protocols of* The Method *v1.2-8.*

*An independent application paper. It uses the lattice, carries its own abstract and its own
references, and takes no part in the main paper's subject matter. It is not a member of either live
bundle.*

> **This paper supersedes and retires four documents**: *Muon-Catalysed Fusion* v1.0 and v1.1, the
> *Corrigendum* to v1.0, and *The Muon Collection Budget* v1.0. Where any of those disagrees with
> this paper, this paper stands. Their withdrawn claims are listed at §8.

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
critical, the transfer step auto-optimising the population.

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

> **The two measured sticking values straddle that break-point.** Via SIN's reactivation the heat form
> is satisfied by 1.06; via PSI's it is short by 1.17. The work form remains short under both — 1.88
> and 2.34.

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
work form is short under both readings by a factor between 1.88 and 2.34.

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
of 1.88**, and only if its production were as efficient per unit mass as the muon's, which nothing
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

> via SIN, **1.88 → 1.18**;  via PSI, **2.34 → 1.47**.

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

**Hemisphere.** Physics front ends capture backward-going pions only, to escape the forward neutron
and proton flux. A reactor's target *is* its detector; it has no backgrounds to escape and may capture
both hemispheres. At the existing aperture that alone takes capture from **10.3 percent to 61 percent**
of measured production — a factor of about six, from a discard made for reasons a reactor does not
share.

**Aperture.** The cap scales as field times bore radius. The best studied front end runs 20 T on a
7.5 cm bore, a product of **1.50 T·m**.

> To capture **90 percent** of measured production over both hemispheres requires a product of
> **2.60 T·m** — 20 T on a **13 cm** bore, or **1.74** times the existing aperture.

That is the collector specification: not a larger accelerator, not a stronger magnet, but a wider bore
and no hemisphere cut.

**The binding constraint is named and not modelled here.** Nuclear heating in the coils scales with
aperture. MuSIC ran 0.6 W of deposited power against 4 W of cooling at a 400 W beam; at megawatt
drivers that margin is the design problem, and nothing in this paper addresses it.

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
| asymptote | 672 cycles | 540 cycles |
| density for 90 percent of it | **10.9 LHD** | 8.7 LHD |
| service life at three times liquid density | **479.6** | 408.3 |
| that as a fraction of the asymptote | **71.3 percent** | 75.6 percent |

The scanned experimental record ends at 1.5 times liquid density. **Reaching 90 percent of the cap
needs about seven times beyond it**, at the high temperature §3.2 requires. §5.13 prices that in
pressure and finds a structural bound rather than an engineering one. §5.5's margin does not survive
without it.

Carrying the corrected thermal accounting of §5.8 through to a reachable density:

| reading | density | service life | thermal gain | work gain |
|---|---|---|---|---|
| SIN | 3 | 479.6 | **0.964** | 0.603 |
| SIN | asymptote | 672 | **1.352** | 0.845 |
| PSI | 3 | 408.3 | 0.821 | 0.513 |
| PSI | asymptote | 540 | 1.086 | 0.679 |

So on the favourable reading of the sticking, with the corrected blanket accounting, **the thermal
balance passes at the asymptote by 1.352 and falls short at three times liquid density by 1.04.** The
work balance is short everywhere, between 1.18 and 1.95.

**This tightens §5.5 rather than overturning it.** The heat form is satisfiable, but only at a density
seven times beyond anything run, and the shortfall at a merely extrapolated density is 1.04 — near
enough that the density axis, not the sticking axis, may be what decides it.

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

**And the two axes fight twice.** §3.2 already records that the resonance wants heat while density
wants cold. There is a second opposition beneath it: the dissociation pressure of hydrogen *falls*
with temperature, so operating at the 800 K the resonance demands tightens this bound relative to the
room-temperature figures quoted above. By how much, this paper does not establish, and the figures
here should be read as the loosest form of the constraint rather than the operative one.

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

### 5.14 The terminal balance

One lever remains unexamined, and it is legitimate. **The blanket is thermally decoupled from the
fuel** — the neutron escapes into it — so it may sit at any temperature the materials allow. §5.8
assumed 800 K; fusion blanket designs run 700 to 900 K, and high-temperature concepts are proposed to
1200 K, where the Carnot factor is **0.750** rather than 0.625.

Setting every lever to a defensible bound at once, and granting *perfect* collection:

| | |
|---|---|
| density | 8.5 times liquid — the lower dissociation reading, so the densest defensibly molecular point |
| service life | 588.9 cycles |
| blanket | multiplied at 1.6 neutrons per source, 24.31 MeV thermal |
| blanket temperature | 1200 K, Carnot 0.750 |
| work per fusion | **18.23 MeV** |
| collection | perfect |
| sticking | the favourable of the two published readings |

> **Thermal gain 1.286. Work gain 0.965.**

**The thermal balance passes. The electrical balance falls short by 1.04** — by four percent, with
every input at its favourable bound.

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

> Work breakeven at the bound case requires a service life of **610.5 cycles** against 588.9, which
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

**Finally, it names an escape from §5.13.** In-flight catalysis — where a fast bound binder–triton
system collides directly with a deuteron — triggers fusion **without first forming a bound molecule**.
§5.13's density bound rests on molecular survival because Vesman formation needs a molecular host. A
route that needs no host is not bounded that way. This paper does not evaluate that route, and notes
only that §5.13's bound is a bound on *this* mechanism rather than on catalysis as such.

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

> **The work form passes on sourced blanket figures.** §5.14 reported it failing by 1.04 on this paper's own conservative
> arithmetic; on a designed blanket it clears by 1.034. **The four percent §5.15 went looking for was
> already in the blanket**, and needed no change to sticking, density, or collection at all.

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
| bound case, perfect collection | 588.9 | 11.13 GeV | **7.73** |

The conclusion of §5.18 is unchanged and now rests on sourced figures throughout: **at the cycle count
demonstrated in the 1980s, with the collector and nothing else, the breeding balance is near two.**

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

**Bounds, never targets:** the kinematic floor at 0.30 GeV, and the sticking asymptote 1/ω_s.

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

## 9. Limits and the state of the question

The captured-yield figure is a simulation convolved with measured cross sections, not an end-to-end
measurement, and its front-end acceptance embeds a selective requirement a reactor does not share —
which is precisely why §5 declines to convert it into a production limit. The sticking levers are
projections and one of them rests on an unresolved figure. The cross-check against the historical
result is an agreement of two calculations sharing an input, not an independent confirmation. The
velocity-ratio expression reproduces two measured sticking values and is used for no third. And this
paper computes no absolute rate: it prices a binder and compares that price to a bound, which is the
whole of its claim.

**The state of the question, plainly.** The reaction is defined, unique, demonstrated, and its
procedure is stated. Condition 8 is a bound on the cost of a binder, and the binder is not the
variable: sticking is mass-independent and the known spectrum holds no alternative. Against measured
production of 11.13 GeV per pion, collection alone cannot satisfy it; the corrected convertible
fraction and the blanket accounting move it a long way; the service-life cap is asymptotic in a
density bounded above by molecular survival. With every lever at a defensible bound and collection
perfect, **the thermal balance passes at 1.286 and the electrical balance reaches 0.965.** The
remaining four percent is inside the uncertainty of several inputs, and every effect not modelled here
runs against it.

**The shortfall inverts into a specification**, which is what a bound is for. Work breakeven at the
bound case needs an effective sticking of 0.1427 percent against 0.1487 — a reduction of 4.0 percent
— and effective sticking is not a constant but ω_s⁰(1 − R), whose reactivation term has been measured
to move by 26 percent over eleven kelvin. The paper's operating point is 800 K and no determination
exists there. The last four percent therefore lies on an axis this analysis holds fixed and the
physics does not.

What would change the answer, in the order this paper can rank them:

1. **The sticking measurement of §5.10** — decides a branch, and now also bears on §5.15's four
   percent. A bench experiment on an existing beam.
2. **Effective sticking at the operating temperature.** No measurement exists at 800 K. §5.15 shows
   the required change is five times smaller than one already observed, in the same direction.
3. **The collector of §5.9** — decides how much of the measured discard is recoverable.
4. **Where molecular hydrogen ceases to be molecular at 800 K** — decides whether the density §5.13
   requires exists at all.

None is settled here. The first three need no new machine.

**And two doors are shut, which is worth as much as an open one.** The binder is not the variable
(§5.7): sticking is mass-independent and the known spectrum holds no alternative. The conversion
ceiling is not an engineering choice (§5.16): it descends from condition 1 through the confinement of
the fuel to charge one, and closes direct conversion for as long as the binder is one that transfers
to higher charge.

## References

1. S. Cook *et al.*, *MuSIC: delivering the world's most intense muon beam*, arXiv:1610.07850;
   Phys. Rev. Accel. Beams **20**, 030101.
2. J. Strait, N. V. Mokhov and S. I. Striganov, *Towards the optimal energy of the proton driver for a
   neutrino factory and muon collider*, Phys. Rev. ST Accel. Beams **13**, 111001 — Table II and §V.
3. M. G. Catanesi *et al.* (HARP Collaboration), Phys. Rev. C **77**, 055207; A. Bolshakova *et al.*,
   Eur. Phys. J. C **63**, 549.
4. Mu2e Collaboration, *Mu2e Conceptual Design Report*, FERMILAB-TM-2545, arXiv:1211.7019.
5. COMET Collaboration, *COMET Phase-I Technical Design Report*, arXiv:1812.09018.
6. Variational three-body calculation of muon-alpha sticking, Phys. Rev. A **34**, 2536.
7. S. E. Koonin and M. Nauenberg, *Nature* **339**, 690.
8. M. Lach, *The Method* v1.2-8 — *The Lach Cylinder: an index of transitions*.
