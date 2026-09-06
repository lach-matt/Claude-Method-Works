# The Muon Collection Budget: What a Catalysed-Fusion Binder Actually Costs

> **RETIRED — superseded by `papers/Cold_Fusion_Binder_Economy_v1.0.md` (6 September 2026).**
> Retained for provenance. Claims withdrawn from this document are listed at §8 of the
> superseding paper; where the two disagree, the superseding paper stands. This document
> is **not** governed by `papers/CLAIMS.tsv` and will not pass `tools/verify_paper.py`.

**Matthew Lach** — Independent researcher
*Draft v1.0, 6 September 2026. Prepared with a computing collaborator under the protocols of* The Method *v1.2-8.*

*An independent application paper, companion to* Muon-Catalysed Fusion *v1.1. Per the standing
architectural ruling it carries its own abstract and its own references, and takes no part in the
main paper's subject matter. It is not a member of either live bundle.*

---

## Abstract

The companion paper's §5.5 records that the per-stage collection budget behind muon-catalysed
fusion's energy balance does not exist, and that it decides the paper. This paper is that budget,
built from published figures for three machines, and it returns one result that changes the balance's
reference point rather than its arithmetic: **no machine achieves the 5 GeV per muon at which the
balance costs its binder.** The best published stopped-μ⁻ figure — Mu2e, a purpose-built μ⁻ facility
with three superconducting solenoids — is 0.0016 stopped μ⁻ per 8 GeV proton, or **5 TeV per stopped
muon, a factor of 1000 above the assumed figure.** The companion's 16.7× accelerator inefficiency is
therefore not the gap; it is the gap that would remain after a 1000× improvement nobody has made.

The consequence is not a defeat, because the same correction enlarges the headroom it has to spend.
Against the pion-production kinematic floor of 0.30 GeV per muon, the best present machine sits
16,667× high, while work-breakeven requires 2,551× — leaving a margin of **6.5×**. Decomposed against
three sourced boundaries, the chain resolves into a front-end block (production and capture, 185–437×),
a middle block (decay and transport, 15–36×), and one sourced stage (stopping fraction 40 %, 2.5×).
Taking the latter two to their ceilings, the front-end block must yield **15.3 %** of its loss and no
more; the remaining 84.7 % may stay production cross-section without costing the target. That figure
is independent of where the capture boundary is placed, because the capture term cancels between the
two blocks — so the wide spread in published capture yields does not propagate into it.

Two levers appear that the companion does not name. Solenoid pion capture is not hypothetical: MuSIC
demonstrated it at 400 W and measured **(9.0 ± 1.0) × 10⁴ μ⁻ s⁻¹ W⁻¹**, a factor of **257** over the
most intense conventional beamline, which is the collector the companion says has never been built,
built in prototype. And proton energy is itself a lever pointing upward: 8 GeV protons are **13.9×**
more energy-efficient per μ⁻ than the 392 MeV of the MuSIC demonstrator.

The paper decomposes what it can source and refuses what it cannot. The front-end block is reported
as a lump, because separating irreducible production cross-section from recoverable capture acceptance
requires a measurement no published figure here supplies — and that separation is the single
measurement on which the whole programme turns.

---

## 1. The question

The companion paper states an energy balance in which the binder — the muon — is bought continuously
and costs 94.8 % of what it liberates at 300 cycles. Its §4 prices that binder at 5 GeV per muon,
against a kinematic floor of 0.30 GeV set by the 300 MeV pion-production threshold, and calls the
16.7× ratio between them "the most tractable free parameter", with "none of it forbidden". Its §5.3
argues that the same chain carries the flux requirement, so that the energy and flux gaps are one
quantity at two thresholds.

Its §5.5 then records the open item plainly: *"the per-stage collection budget does not exist, and it
decides this paper."* This paper supplies as much of that budget as the published record allows.

## 2. The reference machines

Three machines bound the problem, and each is here for a different reason.

**PSI μE4** is the most intense conventional muon beamline: J_μ = 4 × 10⁸ μ/s at a proton beam power
of 1.2 MW, which the source states as J_μ/W_p = 3.5 × 10² μ s⁻¹ W⁻¹ [1]. It is the baseline, and it is
also precisely the *shape* of machine the companion's §5.3 argues a reactor must not be: optimised for
momentum purity and small emittance, both of which a reactor discards.

**MuSIC** at RCNP Osaka is a dedicated source built to demonstrate superconducting solenoid pion
capture — 392 MeV protons on a 20 cm graphite target, 400 W maximum, a 3.5 T pion capture solenoid
adiabatically graded to 2 T, and a curved transport solenoid [1]. Measured yields:

| | measured | note |
|---|---|---|
| μ⁺ and μ⁻ together | (10.4 ± 2.7) × 10⁵ μ s⁻¹ W⁻¹ | **not** the μCF-relevant figure |
| **μ⁻ only** | **(9.0 ± 1.0) × 10⁴ μ⁻ s⁻¹ W⁻¹** | the figure used throughout |

The source describes the μ⁻ yield as "an improvement of about 1 000 over existing facilities" [1]. The
two must never be interchanged: they differ by 11.6×, and μCF requires μ⁻.

**Mu2e** at Fermilab gives the best published stopped-μ⁻ figure: **0.0016 stopped μ⁻ per 8 GeV proton**
on the production target, with about 40 % of muons exiting the beamline stopping in the target [2].

**COMET** supplies the intermediate boundary the others do not resolve: **0.061–0.144 (π⁻ + μ⁻) per
8 GeV proton at 3 m from the target**, captured in a 5 T solenoid of 30 cm inner bore, taking pions
emitted backward with transverse momentum below 100 MeV/c [3].

## 3. The correction: 5 GeV is aspirational

A yield in muons per watt is an energy per muon. Converting:

| machine | GeV per muon | status |
|---|---|---|
| PSI μE4 (physics beamline, μ⁺) | 17,800,000 | measured |
| MuSIC (solenoid capture, μ⁻) | 69,400 | measured |
| **Mu2e (dedicated μ⁻, stopped)** | **5,000** | design |
| companion §4 assumed | 5.00 | **aspirational** |
| kinematic floor (pion threshold) | 0.30 | bound |

> **The figure the energy balance assumes is 1,000× below anything any machine has achieved.**

This is a correction to the companion's §4 and §4.1, not to its algebra. Every Q in that paper is
correctly computed *given* 5 GeV; none of them is reachable at any machine's actual cost per muon. The
companion described 5 GeV as "achieved" and "verified"; it is neither. It is a figure the μCF
literature carries as a target for a dedicated source, and this paper reclassifies it accordingly.

The companion's own §4.1 took one step in this direction, distinguishing muons *produced* from muons
*delivered* and noting that a real beamline delivers at 874 TeV per muon. That step was right and did
not go far enough: even a machine built expressly to stop μ⁻, with none of a physics beamline's
discards, costs 5 TeV.

## 4. The budget

Against work-breakeven at 1.96 GeV per stopped μ⁻ (companion §5.2):

| | |
|---|---|
| present best (Mu2e-class) | 5,000 GeV/μ⁻ |
| target | 1.96 GeV/μ⁻ |
| **required improvement** | **2,551×** |
| **bound (to the kinematic floor)** | **16,667×** |
| margin | **6.5×** |

Decomposed against the three sourced boundaries — protons in, captured π⁻/μ⁻ at 3 m, stopped μ⁻:

| block | stages | loss | status |
|---|---|---|---|
| **1** | A1–A3 production + capture | 185–437× | **lumped** |
| **2** | A4–A5 decay + transport | 15–36× | **lumped** |
| — | A6 stopping fraction (40 %) | 2.5× | sourced |

The three multiply to 16,667× exactly, closing on the total.

### 4.1 The allocation, and a cancellation

A6 offers at most 2.5×, so at least 1,020× must come from blocks 1 and 2. Taking A6 and block 2 each
to their own ceiling — perfect stopping in a thick fuel volume, lossless decay and transport — the
front-end block must yield

> **15.3 % of its loss, and no more.**

The remaining **84.7 %** may remain production cross-section without costing the target.

**This figure does not depend on where the capture boundary is placed.** Block 1 is (ideal/capture) and
block 2 is (capture/exiting), so the capture term cancels in their product. The published spread of
0.061–0.144 π⁻ per proton — better than a factor of two — therefore does not propagate into the
allocation at all. That is worth stating because it is the one place in this chain where a wide
literature uncertainty turns out not to matter.

### 4.2 Why A6 is not bounded at 40 % for a reactor

Mu2e stops 40 % of beamline-exit muons in a thin aluminium foil, and the thinness is a physics
requirement of *that* experiment: the conversion electron must escape. A μCF reactor has the opposite
constraint. Its fuel volume is the stopping medium, may be made arbitrarily thick, and wants every
muon that ranges out anywhere inside it. A6 is therefore the one stage where the reactor's objective
strictly dominates the experiment's, and where approaching unity is a geometry choice rather than a
physics limit. The budget above takes A6 to 1.0 for exactly this reason.

## 5. Two levers the companion does not name

**Solenoid capture is demonstrated, not hypothetical.** The companion's §5.3 says the collector "has
never been built, because none has ever been built wanting to". That is true of a reactor-scale
collector and false of the principle: MuSIC built one at 400 W and measured a **257×** gain in μ⁻ per
watt over the most intense conventional beamline. The scheme the companion asks for exists in
prototype, and its measured gain is a quarter of the 1,020× that blocks 1 and 2 must supply.

**Proton energy is a lever, and it points upward.** MuSIC's 392 MeV protons yield 69,400 GeV per μ⁻;
Mu2e's 8 GeV protons yield 5,000. Per unit of beam energy, **8 GeV protons are 13.9× more efficient at
making a stopped μ⁻ than 392 MeV protons** — because near threshold most of the beam energy cannot
make a pion at all. The companion's §4 specifies "A1 proton driver above the 300 MeV pion threshold",
which is the correct floor and a poor operating point. Whether the optimum lies at 8 GeV or higher is
not settled here, and it is a cheap thing to settle.

## 6. What must be measured

**One measurement decides this programme: the split of block 1 between π⁻ production cross-section and
capture acceptance.** Cross-section is fixed by nuclear physics and no design changes it. Acceptance
is solid angle, field strength, bore radius, target geometry and shielding taper — all engineerable,
and all of them the quantities MuSIC and COMET were built to explore.

The budget needs 15.3 % of block 1. If more than 84.7 % of the front-end loss is cross-section, the
target is unreachable and the paper's conclusion inverts. If less, it is reachable and the remaining
work is beam optics. **Nothing else in the chain carries this weight**, because A6 is a geometry choice
and block 2's ceiling is already inside what is needed.

Three subsidiary quantities follow: the acceptance of a capture solenoid as a function of field and
bore, above MuSIC's 3.5 T and COMET's 5 T; the transport efficiency of a curved solenoid taking the
*whole* momentum distribution rather than a selected slice; and the stopping fraction achievable in a
thick, circulating, high-pressure fuel volume at 800 K.

## 7. Consequences for the energy balance

1. **The companion's §4 and §4.1 require correction.** 5 GeV per muon is aspirational, not achieved.
   Every Q it reports is conditional on a reference point 1,000× below the state of the art.
2. **The companion's "16.7× of headroom, none of it forbidden" understates the task by 1,000× and
   overstates the difficulty of the remainder.** The true distance from the best machine to the floor
   is 16,667×, and only 2,551× of it is required.
3. **The two-gaps-are-one-chain finding survives intact and is strengthened.** Both thresholds sit in
   the same six stages; this paper prices them.
4. **The flux figures in the companion's §5.3 are unaffected in form and worse in magnitude.** A
   demonstration costed at a real machine's cost per muon runs further below Q = 1 than the companion
   states.

## 8. Limits

Mu2e's 0.0016 is a design expectation, not a commissioning measurement. COMET's capture yields are
simulation-derived and model-dependent, spanning better than a factor of two across hadron production
models — though §4.1 shows that spread cancels out of the allocation. MuSIC's figures are measured but
at 400 W, and per-watt yields need not scale linearly to megawatt drivers, where target heating, space
charge and radiation load in the capture coils all enter; MuSIC's own coils sat at 0.6 W of nuclear
heating against 4 W of cooling at 400 W, a margin that does not survive naive scaling. The source
states PSI μE4 as 3.5 × 10² μ s⁻¹ W⁻¹ where 4 × 10⁸ / 1.2 MW recomputes to 3.3 × 10², a 5 % rounding,
carried as stated. The 0.30 GeV kinematic floor is a threshold bound and assumes every 300 MeV of beam
becomes a captured, transported, stopped muon; no machine will approach it, and it is used here only
as a bound, never as a target. Blocks 1 and 2 are lumped and are not represented as per-stage figures.

## References

1. S. Cook *et al.*, *MuSIC: delivering the world's most intense muon beam*, arXiv:1610.07850 (2016);
   Phys. Rev. Accel. Beams **20**, 030101 (2017). Muon yields per watt, pion capture solenoid
   parameters, PSI μE4 comparison.
2. Mu2e Collaboration, *Mu2e Conceptual Design Report*, FERMILAB-TM-2545, arXiv:1211.7019 (2012), and
   subsequent Mu2e technical documentation. Stopped-μ⁻ yield per proton and stopping fraction.
3. COMET Collaboration, *COMET Phase-I Technical Design Report*, arXiv:1812.09018 (2018);
   Y. Kuno, *Prog. Theor. Exp. Phys.* (2013) 022C01. Pion capture solenoid parameters and captured
   π⁻ + μ⁻ yields per proton.
4. M. Yoshida *et al.*, *Superconducting Solenoid Magnets for the MuSIC Project*, IEEE Trans. Appl.
   Supercond. **21**, 1752 (2011).
5. M. Lach, *Muon-Catalysed Fusion: Definition, Procedure, and the Collection Chain*, v1.1 (2026) —
   the companion paper.
6. T. Prokscha *et al.*, *Nucl. Instrum. Meth. A* **595**, 317 (2008) — the PSI μE4 beamline.

*All figures in §§3–5 are computed by `tools/collector.py` (stdlib only); `--selftest` asserts each
published figure above against its recomputation and reports the one 5 % divergence rather than
silencing it.*
