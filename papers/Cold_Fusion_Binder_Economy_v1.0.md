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
is 4.9 or 9.8 of 123 available, leaving a margin of 25.1 or 12.6. Two of the three levers in the
figure of merit are already near their limits: sticking is governed by the ratio of recoil to binder
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

**Proton energy is not a lever.** The same source finds the beam-power-normalised yield flat within a
tenth of its optimum across 4 to 11 gigaelectronvolts, with an optimum near 7. Any driver energy in
that band is equivalent for this purpose.

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

## 9. Limits

The captured-yield figure is a simulation convolved with measured cross sections, not an end-to-end
measurement, and its front-end acceptance embeds a selective requirement a reactor does not share —
which is precisely why §5 declines to convert it into a production limit. The sticking levers are
projections and one of them rests on an unresolved figure. The cross-check against the historical
result is an agreement of two calculations sharing an input, not an independent confirmation. The
velocity-ratio expression reproduces two measured sticking values and is used for no third. And this
paper computes no absolute rate: it prices a binder and compares that price to a bound, which is the
whole of its claim.

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
