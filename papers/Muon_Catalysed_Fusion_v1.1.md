# Muon-Catalysed Fusion: Definition, Procedure, and the Collection Chain

> **RETIRED — superseded by `papers/Cold_Fusion_Binder_Economy_v1.0.md` (6 September 2026).**
> Retained for provenance. Claims withdrawn from this document are listed at §8 of the
> superseding paper; where the two disagree, the superseding paper stands. This document
> is **not** governed by `papers/CLAIMS.tsv` and will not pass `tools/verify_paper.py`.

**Matthew Lach** — Independent researcher
*Draft v1.1, 6 September 2026. Prepared with a computing collaborator under the protocols of* The Method *v1.2-8.*
*Supersedes v1.0 (1 August 2026), which superseded the exploratory drafts v0.1–v0.14 of* Cold Fusion Under a Closed Index.

*An independent application paper. Per the standing architectural ruling, it uses the lattice
without forming part of the main paper's subject matter, and carries its own abstract and its own
references. It is not a member of either live bundle, and no claim in it is audited by them.*

---

## Abstract

Cold fusion is defined here as a nuclear fusion event in which the approach to nuclear separation
is supplied by molecular binding geometry rather than by kinetic energy. On that definition it is
neither speculative nor unachieved: it has been performed routinely since 1957, and this paper
states the procedure. Seven necessary conditions are given; applied to the closed index of charged
particles they admit exactly one solution, μ⁻ + (d,t) → (dtμ)⁺ → ⁴He + n + μ⁻ + 17.59 MeV, because
a structural window on the binder mass — bounded below by fusion geometry and above by
molecular-index survival — contains one leptonic occupant. The connection to the lattice is
structural rather than decorative: Λ carries configuration and not scale, so a muonic atom occupies
*the same cell* as its electronic twin, and the muonic realisation of that cell is what the window
selects. The procedure is then given in full: target requirements, the cycle with pinned rates, the
exit branching, the two observables, and the failure signatures.

**This version revises §3.2, §4 and §5 of v1.0.** v1.0 stated two independent gaps between the
demonstrated reaction and useful power, and computed the first of them over the sticking and
density axes with the muon production cost E_μ held fixed. Three revisions follow. **First, the
energy threshold is dominated by E_μ, not by sticking**: at the 0.30 GeV kinematic floor, *measured*
sticking already returns Q ≈ 13, and the sticking levers matter only because E_μ sits at 5 GeV.
**Second, v1.0's Q counted fusion heat against electrical work**; only 50.1 % of the yield is
convertible, so the plant-relevant threshold is E_μ < 1.96 GeV — a 2.55× accelerator improvement
against 16.7× of stated headroom — rather than the 3.90 GeV that the heat convention gives.
**Third, and governing the other two, the two gaps are not independent.** The 5 GeV figure is the
cost per muon *produced* and already assumes the collection chain is solved; a real beamline
*delivers* one muon per 874 TeV of driver energy, a factor of 1.75 × 10⁵ which is the flux gap
(1.2 × 10¹⁵ / 10¹⁰ = 1.2 × 10⁵) seen from the other end. They are one chain read at two thresholds.
The consequence is a sharper statement of what is missing than v1.0's "a machine that does not
exist": neither beam power nor pion production is short — PSI runs 1.4 MW and 1 MW at 590 MeV
already yields ~10¹⁵ π⁻/s — and what does not exist is a **collector**, whose design objective is
the inverse of every muon channel ever built. **A fourth correction follows from pricing that
collector** (§4.2): the 5 GeV per muon at which v1.0 costs the binder is aspirational rather than
achieved, the best published figure being 5 TeV per stopped μ⁻ — which leaves §5's algebra intact,
moves its reference point by three orders, and in the same motion enlarges the headroom to 16,667×
against a requirement of 2,551×. Separately, the cryogenic operating branch is excluded
on thermodynamics, and ambient electron-screened fusion remains excluded by conservation.

---

## 1. Definition

> A **cold fusion reaction** is a nuclear fusion event in which the approach to nuclear separation
> is supplied by *molecular binding geometry* rather than by kinetic energy.

Temperature does not appear. "Cold" is a consequence — when geometry supplies the approach, kinetic
energy is unnecessary — and the name has misdirected the field for decades. The operative property
is *molecular access at nuclear separations*.

Seven conditions are necessary:

1. **A binder** — negatively charged, leptonic (a hadron is absorbed before it can catalyse), mass
   within the structural window of §2, lifetime × cycle rate ≫ 1, producible.
2. **A molecular index** with at least two bound states, so that an *edge cell* exists near the
   binding threshold.
3. **A formation channel** — that edge cell reachable by the host medium's smallest exchangeable
   quantum.
4. **Nuclear overlap** — internuclear separation small enough that fusion outruns formation.
5. **An open exit** — the compound system must have a particle channel available.
6. **Binder release** — the recoil velocity must exceed the binder's orbital velocity sufficiently
   that sticking is small.
7. **Conservation closure** — one heavy ash nucleus per event, energy accounted through Q.

Conditions 1–5 suffice for the reaction to *occur*; 6–7 govern whether it is sustainable and
verifiable.

## 2. The unique realisation

The binder's mass sets the molecule's size, and therefore everything. Mass substitution moves the
internuclear separation from 74,100 fm (electron) to ~280 fm (muon) — a factor buying ~91 orders of
magnitude in tunnelling rate, against ~33 orders available from any perturbation of the potential at
fixed geometry. **Geometry is the mechanism; screening is a correction to it.**

Two structural requirements bound the mass axis. **Fusion geometry**: the separation must bring the
nuclei close enough for fusion to outrun the cycle, giving m > 119 mₑ. **Index survival**: the number
of molecular bound states scales as √(M_nuclear/m_binder), and at least two are needed so an edge
cell exists, giving m < 918 mₑ.

> **The structural window is [119, 918] mₑ.**

The electron fails below it (geometry), the tau above it (the molecular index degenerates to a single
state). Inside it sit the muon (207 mₑ) and the pion (273 mₑ); a second filter — interaction type —
removes the pion, which is absorbed by the nucleus before catalysis. **Exactly one occupant remains**,
interior to the window by 1.74× and 4.44×, so the conclusion survives reasonable movement of either
criterion.

### 2.1 Why the lattice is the right frame  *(expanded in v1.1)*

Λ is built on configuration coordinates — (n, ℓ, k, q, e, f, g, 2S) — and carries no scale. A muonic
atom therefore occupies **the same cell** as its electronic twin: same n, same ℓ, same k, throughout.
The index cannot distinguish them, because the index carries configuration and not scale. This is the
same structural property as the Z-blindness already recorded for the bracket, extended to mass.

The consequence is that the muonic system is not a new object requiring a new index. It is an
**existing Λ cell realised at 207× scale**, and the structural window of §2 is a statement about which
realisations of that cell are physically available. The lattice supplies the frame; it does not supply
the rates, and §5 does not ask it to.

Hence the reaction is fully specified rather than schematic:

> **μ⁻ + (d,t) → (dtμ)⁺ → ⁴He + n + μ⁻ + 17.59 MeV**

The exit channel is fixed by nuclear structure, not chosen: ⁵He is unbound, so the compound system has
no bound configuration to occupy and separates as ⁴He + n. The formation channel is fixed by a
near-coincidence: the dtμ (J = 1, v = 1) state is bound by only 0.66 eV, within a factor of 1.8 of the
D₂ vibrational quantum (0.365 eV), and resonant transfer of that binding into host rovibrational
excitation is what makes formation fast. The muonic molecule's ground state, 319 eV deep, is
unreachable by the host — **the resonance uses the last bound state, and there is no second option.**
That the loose state sits 483× below the muonic ground state is a three-body accident which dropped a
muon-scale quantity into the electron-scale window; without it, muon catalysis would be a curiosity.

The channel is also optimal and not merely available. Sticking is governed by the ratio of recoil
velocity to binder orbital velocity: 2.97 for d + t giving ~1 % sticking, 1.66 for d + d giving ~15 %.
d + t is the unique light channel where the overlap is small.

## 3. The procedure

### 3.1 Stage A — the binder factory

See §4. Produce μ⁻ and stop them within the fuel volume.

### 3.2 Stage B — the target  *(revised in v1.1)*

**Purity.** Hydrogen isotopes only. Elements with Z > 1 capture muons preferentially and terminate the
chain; ppm-level purity is a requirement, not a refinement.

**Tritium fraction.** Not critical. The transfer step auto-optimises the population, which is why the
measured record spans c_t = 2–95 % without a sharp optimum.

**Density and temperature — one bracket, not two settings.** v1.0 gave these as separate
recommendations: density "as high as the cryogenics permit" and temperature "high, not low". They are
opposed, and stating them separately concealed the opposition. λ_dtμ rises resonantly by roughly two
orders of magnitude toward 800 K, so the resonance pushes hot; hydrogen is liquid at 20 K and gaseous
above 33 K, so density pushes cold.

**The bracket resolves hot, and the cryogenic branch is excluded** — see §6.2. The operating point is
**high temperature at high pressure**, of order kilobars for 1 LHD at 800 K, and density is to be
bought *mechanically rather than cryogenically*. The JINR scan (0.2–1.2 LHD at 20–800 K) is the only
dataset spanning this window, and it is exactly this window being explored.

The bracket has the same two-bound shape as the mass window of §2: bounded below by a rate condition
(the formation resonance) and above by a degeneracy condition (the fluid ceasing to be dense).

### 3.3 Stage C — the cycle

Per catalytic turn, at φ = 1.2:

| step | rate (s⁻¹) | time | note |
|---|---|---|---|
| muon stops by ionisation | 10⁹ | 1 ns | once only |
| capture into a high-n muonic orbit | 10¹² | 1 ps | |
| cascade to 1s | 10¹² | 1 ps | |
| transfer μd → μt (48 eV more bound) | **(2.7 ± 0.9) × 10⁸** | 3.7 ns | **the cap** |
| dtμ formation, Vesman resonant | 10⁸ → 1.5 × 10¹⁰ | 10 ns → 0.07 ns | temperature-dependent |
| Auger de-excitation to the fusing state | 10¹¹ | 10 ps | |
| **d + t fusion at ~280 fm** | 10¹² | 1 ps | |

The cycle is a harmonic sum, so **the bottleneck moves**. At low temperature, formation is
rate-determining and the cycle takes 13.6 ns (λ_c ≈ 7.3 × 10⁷ s⁻¹). Driving the resonance transfers
the bottleneck to muon transfer, after which **λ_c saturates near 2.6 × 10⁸ s⁻¹** — temperature buys a
factor of ~3.6 and then stops.

**λ_c is the single most load-bearing number in the balance and carries the widest error bar**: it
descends from a transfer rate measured at (2.7 ± 0.9) × 10⁸, a ±33 % band. Every figure in §5 inherits
it, and a central value quoted without it is the most quotable number here and the least defended.

### 3.4 Stage D — the exit

Per fusion: **99.14 %** the muon is released and re-enters Stage C; **0.86 %** it remains bound to the
⁴He as (μ⁴He)⁺ recoiling at 0.043c. Of those, roughly half are collisionally stripped and rejoin the
cycle, giving a net loss near 0.45 % per fusion and a sticking ceiling of ~222 turns. The chain
terminates when the muon decays (τ = 2.197 μs; bound-muon disappearance 4.665 × 10⁵ s⁻¹) or remains
stuck.

The ~222 figure is an **asymptote**, approached only as φ → ∞; it omits muon decay. The
decay-corrected service life is N = φλ_c/(λ₀ + ω_s·φλ_c), which returns 167 at φ = 1.2 and 196 at
φ = 3. §5 uses the decay-corrected value throughout and states where the asymptotic one would differ.

### 3.5 Stage E — observables

**Neutrons.** 14.1 MeV, one per fusion, timed from each muon stop. The decay slope gives
Λ = λ₀ + ω_s·φλ_c; the yield per muon gives N.

**X-rays.** The (μ⁴He)⁺ K_α line at 8.2 keV counts stuck muons directly, on a route sharing no
instrument or calibration with the neutron measurement. These two methods disagreed historically;
running them simultaneously on one target is what resolves the disagreement, and a disagreement is a
refusal rather than an average.

### 3.6 Stage F — failure modes

| symptom | cause |
|---|---|
| yield far below expectation | Z > 1 contamination capturing muons |
| Λ near the free-muon 4.665 × 10⁵ s⁻¹ | muons not stopping in the fuel |
| yield falling over hours | helium ash accumulating — circulate the target |
| low λ_c at low temperature | resonance mismatch — *raise* the temperature |
| neutron and X-ray sticking disagree | refusal; resolve before any claim |

**Minimal demonstration.** Pure D₂ requires no tritium licence and yields ~4 fusions per muon, giving
~2 × 10⁴ neutrons/s at 10⁴ μ/s stopping — an unambiguous signal within minutes. This demonstrates the
*reaction*; it demonstrates nothing about Q, for the reason given in §5.4.

## 4. The binder factory

The accelerator is not preamble. It is **the sole source of the one element the reaction cannot
self-supply, and the only element the reaction destroys.** Fuel, geometry, resonance and exit channel
are supplied by nature or purchased once; the binder is purchased continuously.

**Chain.** A1 proton driver above the 300 MeV pion threshold; A2 production target, p + N → π⁻ + X;
A3 capture (magnetic horn or solenoid — the largest single loss); A4 decay channel; A5 transport;
A6 stopping within the fuel volume.

**Floor plan.** Two decay lengths set the machine's geometry: a 200 MeV/c pion travels 11.2 m before
decaying, while a 100 MeV/c muon travels 624 m. The decay channel must therefore be ~11 m, and muon
transport over tens of metres is nearly lossless. The 56× ratio between those lengths is what makes
the machine possible.

**Energy budget.** The kinematic floor at perfect collection is 0.30 GeV per muon; the figure used
throughout §5 is 5 GeV — an inefficiency of 16.7×, distributed across pion yield, capture solid angle,
decay acceptance, transport and stopping fraction. None of it is forbidden, which makes E_μ the most
tractable free parameter.

> **Caution, added after §4.2 was computed: 5 GeV is aspirational, not achieved.** It is the figure the
> μCF literature carries as a target for a dedicated source, and §5 uses it for continuity with v1.0.
> No machine delivers it. See §4.2 and the companion budget paper: every Q in §5 is conditional on a
> reference point three orders below the state of the art.

### 4.1 What the 5 GeV figure assumes  *(new in v1.1)*

**5 GeV is the cost per muon *produced*, and it presumes stages A3–A6 are solved.** It is not what a
machine delivers. PSI runs a ~1.4 MW driver and its beamlines deliver ~10¹⁰ μ/s, which is

> 1.4 MW ÷ 10¹⁰ μ/s = 1.4 × 10⁻⁴ J = **874 TeV per delivered muon**, a factor **1.75 × 10⁵** above
> the 5 GeV figure.

v1.0 did not distinguish these, and the distinction governs §5. It is also self-consistent with v1.0's
own table in the intended direction: at 5 GeV per muon, 1 MW of driver beam yields 1.25 × 10¹⁵ μ/s,
which is exactly what 1 MW of fusion requires — Q ≈ 1 falls straight out, *provided* the collection
chain delivers what the driver produces.

### 4.2 What machines actually cost  *(added in v1.1)*

The best published stopped-μ⁻ figure is Mu2e's **0.0016 stopped μ⁻ per 8 GeV proton** — that is
**5 TeV per stopped muon, a factor of 1,000 above the 5 GeV §5 assumes.** MuSIC, the dedicated
solenoid-capture source, measures (9.0 ± 1.0) × 10⁴ μ⁻ s⁻¹ W⁻¹, or 69 TeV per μ⁻; PSI's μE4 beamline
sits at ~18 PeV per muon.

This does not alter §5's algebra, and it does not alter the finding that the two thresholds share one
chain. It relocates the reference point, and it enlarges the headroom in the same motion: against the
0.30 GeV floor the best present machine is 16,667× high, of which work-breakeven requires 2,551×,
leaving a margin of 6.5×. Two levers follow that this paper does not otherwise name — solenoid pion
capture, demonstrated by MuSIC at a 257× gain over a conventional beamline, and proton energy, where
8 GeV protons prove 13.9× more efficient per μ⁻ than 392 MeV. The per-stage allocation is the subject
of the companion paper.

**Flow, not batch.** A chemical catalyst is recovered at cycle's end; the muon decays regardless of
what it is doing. The accelerator must therefore run continuously at the muon loss rate, and the fuel
must circulate to clear helium ash. No steady state conserves binder inventory.

**The binder cost is the structural fact.** At 300 cycles and 5 GeV the binder costs 94.8 % of what it
liberates. And no nuclear process known releases enough per event to fund a muon at the kinematic
floor: d + t is short by 17×, d + d by 13×, and even U-235 fission by 2×. Chain multiplication is
therefore thermodynamically excluded, and μCF must *recycle* one binder N times rather than *multiply*
binders as fission does. This is a property of the muon's mass against the nuclear energy scale, not
of the d–t channel — **no choice of fuel moves μCF into a self-multiplying regime.**

## 5. The gap  *(rewritten in v1.1)*

v1.0 stated two gaps and called them independent. They are one chain read at two thresholds, and this
section states the chain.

### 5.1 The energy threshold, on three axes

Service life and binder cost meet in one inequality: **viable iff N > E_μ / Q_fus** — the service life
must exceed the binder's cost in units of event yield. N is a *sticking* quantity; E_μ is an
*accelerator* quantity.

At **measured** sticking (0.45 %, SIN), with no polarisation, no J = 1 mixture and no sticking work of
any kind:

| | crossover E_μ for Q = 1 (heat) | accelerator improvement required |
|---|---|---|
| φ = 1.2 (within the scanned record) | 2.93 GeV | **1.70×** of 16.7× available |
| φ = 3.0 (extrapolated) | 3.45 GeV | **1.45×** |
| N = 222 (asymptotic ceiling, decay omitted) | 3.90 GeV | **1.28×** |

At the 0.30 GeV kinematic floor, measured sticking returns **Q ≈ 13**. The energy threshold is
therefore **accelerator-dominated**: the sticking levers of v1.0 matter only because E_μ sits at 5 GeV.
Read as a sticking problem, breakeven needs *both* levers; read as the inequality, it needs *either*
both levers *or* a sub-2× accelerator improvement — and the second is the smaller ask by a wide margin.
The accelerator deficit is 4.3× the sticking deficit, in joules per muon.

### 5.2 Heat and work are not interchangeable

v1.0's Q counts 17.59 MeV of fusion **heat** against GeV of electrical **work**. Only part of the yield
is convertible: the α's 3.5 MeV (19.9 %) deposits in the fuel, while the neutron's 14.1 MeV (80.2 %)
escapes to a blanket which may sit at any temperature — at 800 K against 300 K ambient, 62 % Carnot.
The convertible fraction is **50.1 %**.

**Work-breakeven is E_μ < 1.96 GeV — a 2.55× accelerator improvement**, still inside the 16.7 %
headroom but twice the heat-convention ask, and it is the correct threshold for a plant.

### 5.3 The collection threshold, and why it is the same chain

The requirement for 1 MW of fusion at N = 300 is 1.2 × 10¹⁵ μ/s, against ~10⁸ /s at PSI today and
~10¹⁰ /s planned. That is 1.2 × 10⁵ — and §4.1's 874 TeV per delivered muon against 5 GeV per muon
produced is 1.75 × 10⁵. **These are the same quantity seen from two ends.**

What is missing is therefore specific, and it is not scale:

- **Not beam power.** 1 MW of proton beam exists; PSI runs 1.4 MW.
- **Not pion production.** 1 MW at 590 MeV is ~10¹⁶ protons/s; at ~0.1 π⁻ per proton that is ~10¹⁵
  π⁻/s — the requirement, to within a factor of order one.
- **A collector.** No machine collects and stops a large fraction of what it produces, because none has
  ever been built wanting to.

| | physics beamline | μCF reactor |
|---|---|---|
| momentum spread | dp/p ~ 1–3 % | anything that stops in the fuel |
| emittance | small, for tracking | irrelevant |
| beam spot | mm, defined | the whole fuel volume |
| backgrounds | minimised | irrelevant — the target *is* the detector |

Every one of those is a **deliberate discard**, made for reasons a reactor does not share. A physics
beamline selects a thin slice of a broad phase space; a reactor wants the whole distribution. The
design objective is the inverse of every muon channel ever built: **maximise stopped count, discard
nothing, accept any momentum that ranges out inside the fuel.**

Essentially all of the 1.75 × 10⁵ sits in stages A3–A6 — capture solid angle, decay acceptance,
transport, stopping fraction.

### 5.4 What this forbids

**A reachable muon rate is not evidence of a self-sustaining reaction.** One watt of fusion needs
~1.8 × 10⁹ delivered μ/s, which is inside the ~10¹⁰ /s planned; but costed at the 874 TeV a beamline
delivers today, that demonstration runs at **Q ≈ 3 × 10⁻⁶**. There is no low-power configuration in
which Q > 1 falls out. The minimal demonstration of §3.6 demonstrates the reaction and says nothing
about the balance.

### 5.5 The open item

**The per-stage collection budget is supplied by the companion paper, and one measurement in it
decides this one.** Taking stopping and transport to their ceilings, the front-end production-and-
capture block must yield **15.3 %** of its loss; the other 84.7 % may remain production cross-section.
Whether that 15.3 % is recoverable acceptance or irreducible cross-section is unmeasured, and it is
the quantity on which the programme turns. "None of it is
forbidden" is a statement about physics, not about engineering. A6 admits any momentum that ranges out
in the fuel; A3 is named the largest single loss; A4 is bounded by the 11.2 m / 624 m geometry. What is
required is a stage-by-stage accounting with a defensible ceiling on each, against which the 1.75 × 10⁵
can be allocated or shown to be unallocatable. Until it exists, the honest statement is that the
problem is well posed and unsolved, not that it is solved.

## 6. What the definition excludes

| excluded | grounds |
|---|---|
| electron-bound systems (ambient "cold fusion") | geometry: 74,100 fm separation, ~91 orders short |
| tau and heavier binders | the molecular index degenerates; no edge cell |
| π⁻, K⁻, p̄, Σ⁻ | nuclear absorption preempts catalysis |
| enhanced ambient screening | conservation (§6.1) |
| **the cryogenic operating branch** | **thermodynamics (§6.2) — new in v1.1** |
| excess heat without commensurate ash | baryon number: any d–d branching deposits 3.76 × 10⁻⁸ – 2.74 × 10⁻⁷ mol of heavy ash per watt-day, a window 7.29× wide whose ends are the extremal channels |
| d + d with γ-dominant branching | selection rule: s-wave d + d is 0⁺ → 0⁺, which emits no single photon |
| thermal and inertial fusion | by definition — approach supplied by kinetic energy |
| chain multiplication of binders | no nuclear event funds a muon (§4) |

### 6.1 The ambient exclusion

Enhanced electron screening in metals has been proposed as an ambient route. It is excluded by
conservation on two independent grounds.

**Adiabaticity.** At thermal energies the ratio of deuteron to electron velocity is 1.0 × 10⁻³ —
deeply adiabatic, where static screening is not an approximation but exact. Beam measurements sit at
0.63, some 620× faster and squarely non-adiabatic, where a fitted screening parameter absorbs
stopping-power and straggling effects that have no ambient counterpart. The measured enhancement
belongs to a different regime.

**Energy audit.** A static screening energy is bounded by what the electron system can donate. The
complete site inventory is: Thomas–Fermi 29 eV, plasmon ~9, Fermi 5–10, cohesive 4–8, zero-point 0.1,
kT 0.026. The ceiling is ~30 eV against a requirement of 88 eV for a detectable p + d rate — a factor
2.9 in energy, 27 orders in rate.

The bound is conservation-grade and admits no mitigation by vacuum, geometry, cooling, or channel
choice. Independently, were the beam-measured U_e a static potential of the Debye form, PdD would run
2.4 × 10¹⁶ d–d fusions/s per mole — an unambiguously lethal neutron flux from every palladium
deuteride sample ever made. The historical neutron silence excludes it by ~16 orders, and the silence
is a bound that kills a model.

### 6.2 The cryogenic exclusion  *(new in v1.1)*

Below ambient, fusion heat is not merely expensive to remove; it can do no work at all. At 20 K the
recovered work is zero and the removal cost is 10.4× the heat removed. **A μCF reactor cannot be
net-positive while cold.**

| fuel T | blanket T | recovered | cooling | net |
|---|---|---|---|---|
| 20 K | 800 K | 0.501 | 10.446 | **−9.945** |
| 100 K | 800 K | 0.501 | 2.089 | −1.588 |
| 300 K | 800 K | 0.501 | 0.000 | +0.501 |
| 800 K | 800 K | 0.501 | 0.000 | +0.501 |

Fuel temperature stops mattering at ambient: above it there is no refrigeration cost, and the recovered
fraction is fixed by the *blanket*, not the fuel. The output side therefore wants the fuel at or above
ambient and is indifferent above that; the resonance wants 800 K; density alone wants cold. The bracket
of §3.2 resolves at high temperature and high pressure, and the cryogenic branch falls on
thermodynamics alone — no accelerator or sticking improvement rescues it.

## 7. Provenance

**Verified against primary or surveyed literature:** the transfer rate (2.7 ± 0.9) × 10⁸ s⁻¹;
λ_dtμ > 10⁸ s⁻¹ rising to (100–150) × 10⁸ at 800 K; bound-muon disappearance 4.665 × 10⁵ s⁻¹; LHD
4.25 × 10²² atoms/cm³; dtμ separation ~280 fm; dtμ (J=1,v=1) binding 0.66 eV; sticking 0.90 % (S state)
and 0.31 % (J=1,v=0) by variational three-body calculation, measured 0.45 ± 0.05 % (SIN) and
0.56 ± 0.04 % (PSI); ~150 cycles and Q ≈ 0.53 at Los Alamos; scientific breakeven at 284 fusions per
muon; E_μ ≈ 5 GeV at PSI and J-PARC MUSE; PSI driver ~1.4 MW and beamline delivery ~10¹⁰ μ/s; dual-
polarisation estimates ω_s 0.45 → 0.34 %, λ_c +30–50 %, cycles 148 → 193; scanned ranges PSI 0.01–1.5
LHD at c_t 2–95 % and T 13–300 K, JINR 0.2–1.2 LHD at T 20–800 K; the screened molecular D₂ rate
3 × 10⁻⁶⁴ s⁻¹; sticking ~1 % for dtμ against ~15 % for ddμ; the external-field reactivation criterion.

**Computed for this paper:** the structural window [119, 918] mₑ; λ_c saturation at 2.6 × 10⁸ s⁻¹ from
the harmonic sum; breakeven sticking thresholds 0.202/0.262/0.292 %; decay lengths 11.2 m and 624 m;
the 0.30 GeV kinematic floor and 16.7× inefficiency; flux requirements 1.2 × 10¹²/10¹⁵/10¹⁸ s⁻¹; the
ash bracket 3.76 × 10⁻⁸ – 2.74 × 10⁻⁷ mol per watt-day at width 7.29; the adiabaticity ratios
1.0 × 10⁻³ and 0.63; the ~30 eV static screening ceiling against an 88 eV requirement; the muonic ⁴He
1s binding 10.9 keV and 1s→2p resonance 8.20 keV.

**Reclassified in v1.1:** E_μ = 5 GeV per muon, described in v1.0 as achieved and verified, is
**aspirational** — no machine delivers it, and the best published figure is 1,000× above it (§4.2).

**Computed for v1.1:** Q ≈ 13 at the kinematic floor at measured sticking; the crossover E_μ at
2.93/3.45/3.90 GeV under the three service-life conventions; the convertible fraction 0.501 and
work-breakeven at 1.96 GeV (2.55×); the cryogenic penalty table of §6.2; 874 TeV per delivered muon and
the identity of 1.75 × 10⁵ with the flux gap's 1.2 × 10⁵. Reproduced by `tools/mucf.py`, whose
`--selftest` is fixtured on v1.0's own Table 5.1 and on each figure above.

**Carried with reservation:** step rates other than transfer are order-of-magnitude; the internuclear
separation from a hydrogenic estimate was 28 % high before correction; **whether the 0.31 % J = 1 figure
is initial or post-reactivation sticking is not resolved by its source**, and the composed 0.234 % rests
on it; the muonic-molecule state table is recalled; the window edges depend on the two criteria stated
in §2, though the muon is interior to any reasonable choice; the ~10¹⁰ μ/s delivery figure is a
beamline capability rather than a fundamental limit, which is the whole content of §5.3.

## 8. Corrections from v1.0

1. **§5's "two independent gaps" is withdrawn.** They are one collection chain at two thresholds
   (§4.1, §5.3). v1.0's own figures are self-consistent; the framing was not.
2. **§5.1's conclusion that two sticking levers are required is narrowed.** It holds only with E_μ
   frozen at 5 GeV. Either both levers *or* a sub-2× accelerator improvement suffices (§5.1).
3. **§5.1's Q is heat against work.** The plant threshold is 1.96 GeV, not 3.90 (§5.2).
4. **§3.2's "density as high as the cryogenics permit" is withdrawn** and replaced by the
   temperature–density bracket resolved at high temperature and pressure (§3.2, §6.2).
5. **Table 5.1's ω_s = 0.234 % row was computed at λ_c ≈ 2.7 × 10⁸**, the unrounded transfer rate,
   rather than the 2.6 × 10⁸ saturation pinned in §3.3. At the pinned value the row reads
   0.92 / 1.09 / 1.20 rather than 0.93 / 1.10 / 1.21 and still clears breakeven at φ ≥ 2. The
   conclusion survives; the row was marginally optimistic against its own parameter.
6. **The ~222 sticking ceiling is an asymptote**, not a service life; §5 uses the decay-corrected N.
7. **§4's 5 GeV per muon is reclassified from achieved to aspirational.** The best published
   stopped-μ⁻ figure is 5 TeV. §5's algebra is unaffected; its reference point is not (§4.2).
8. An earlier claim that fusion is confined to the molecular ground state was withdrawn in v1.0
   against the variational result for J = 1, and an earlier framing treating energy-positivity as the
   sole remaining requirement was corrected by the flux gap. Both stand withdrawn.

## References

1. M. Lach, *The Method* v1.2-8 — *The Lach Cylinder: an index of transitions*.
2. μCF cycle parameters: transfer, formation, disappearance rates; LHD; scanned density, concentration
   and temperature ranges (PSI, JINR, TRIUMF programmes).
3. Variational three-body calculation of μ–α sticking, S state and J = 1, v = 0
   (Phys. Rev. A **34**, 2536, 1986).
4. Measured final sticking: SIN 0.45 ± 0.05 %, PSI 0.56 ± 0.04 % (direct observation, ionisation
   chamber).
5. μCF energy balance: ⟨E_μ⟩ ≈ 5 GeV; ~150 cycles at Los Alamos; Q ≈ 0.53; breakeven ≈ 284 fusions per
   muon.
6. Dual polarisation of fuel nuclei and muon beam: ω_s and λ_c estimates (2026 μCF review).
7. External-field-assisted muon reactivation: rate-network criterion and no-go condition (2026).
8. S. E. Koonin and M. Nauenberg, *Nature* **339**, 690 (1989) — screened fusion rates in isotopic
   hydrogen molecules.
9. PSI high-intensity proton facility and HIMB upgrade; J-PARC MUSE — driver power and surface-muon
   delivery rates.
