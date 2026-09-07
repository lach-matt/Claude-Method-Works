# `research/`

Original research produced **from** the corpus, never **into** it.

Nothing in this tree is a bundle member, a Register entry, or mirrored Drive content. Nothing here is
read by the §0 gate. `method/`, `drive/`, `extracted/` and `recovered/` are inputs to this tree and are
never written to by it — the chat-67 full hold governs, so a finding made here is **recorded, never
repaired** into a volume.

Each subdirectory holds one paper and the instrument that computes its numbers. Every instrument is
stdlib-only and takes a `--selftest` whose fixtures are the corpus's own printed figures and the
literature's own printed figures — never a number the paper invented. Run the selftest before trusting
a report.

| paper | instrument | subject |
|---|---|---|
| `warp-drive/WARP-DRIVE.md` | `warp-drive/warpdrive.py` | where a warp drive sits in the fifteen-letter violation index, what warp energy is, and which engine can be built |
| `warp-drive/ENGINE-ASSESSMENT.md` | `warp-drive/warpdrive.py` | *Warp Drive Theory* (the Drive design deliverable) checked against the physics it invokes |
| `warp-drive/ROTATING-SHELL.md` | `warp-drive/warpdrive.py` | whether counter-rotation can be carried onto a positive-energy warp shell, and what it costs |
| `warp-drive/SHIFT-CEILING.md` | `warp-drive/warpdrive.py` | a closed form for the shift-vector limit Fuchs et al. left open, and the top speed it implies |
| `warp-drive/SHELL-PROFILE.md` | `warp-drive/warpdrive.py` | the shell reconstructed by TOV integration; corrects the ceiling and gives the fill-fraction design rule |
| `warp-drive/ACCELERATION.md` | `warp-drive/warpdrive.py` | why a positive-ADM-mass drive cannot self-accelerate, and what starting one costs |
| `warp-drive/SOURCE-CODE.md` | `warp-drive/warpdrive.py` | what reading Warp Factory changed, including a factor of two against this series |
| `warp-drive/MEASURED.md` | `warp-drive/warpdrive.py` + `octave/` | Warp Factory actually run; the ceiling measured at 0.0218 c and the prediction confirmed |
| `warp-drive/WHAT-BINDS.md` | `warp-drive/warpdrive.py` + `octave/` | the fill curve measured — overturning a design rule — and where the NEC actually fails |
| `warp-drive/THE-DESIGN-EQUATION.md` | `warp-drive/warpdrive.py` + `octave/` | the three bounds composed into a design equation, and a measured 1.6x speed gain from one line |
| `warp-drive/DENSITY-IS-CLOSED.md` | `warp-drive/warpdrive.py` + `octave/` | shaped density built and measured: a closed lever, and the domain of the design equation |
| `warp-drive/SPHERICITY.md` | `warp-drive/warpdrive.py` + `octave/` | the sphericity cost measured, the oblate test attempted, and the control that invalidated it |
| `warp-drive/THE-BORROWED-WELL.md` | `warp-drive/warpdrive.py` | register 1206 read backwards; a closed form for transport without a drive |
| `warp-drive/THE-GR-FLYBY.md` | `warp-drive/grflyby.py` | the flyby in Schwarzschild geometry; the geometric bound dissolves and an IMBH is the minimum instrument |
| `warp-drive/NEC-CORRECTION.md` | `warp-drive/octave/` | the measured ceiling was an artefact twice over; the series' absolute figures withdrawn |
| **`warp-drive/THE-ENGINE.md`** | **`warp-drive/slingshot.py`** | **the redefinition: an engine is a coupler, not a source — 0.87 c in 11 minutes at 1 g, zero propellant** |
| **`warp-drive/THE-DRIVE.md`** | **`warp-drive/drivespec.py`** | **the drive specified: size was never varied — nuclear matter at 5 km, 1.11 M☉, 0.0476 c, flat interior** |
| **`warp-drive/COUPLING.md`** | **`warp-drive/coupling.py`** | **the drive is a coupling, not propulsion: ADM withdrawn, the CoM theorem put in its place, and a static well is a lens while a moving well is a pump** |
| **`warp-drive/NAVIGATION.md`** | **`warp-drive/navigate.py`** | **the steering law, from M's own three-body result: no trajectory exists, fly a braid word, and use a 25:1 binary** |
| `warp-drive/TARGET-1-RESULT.md` | `warp-drive/octave/run_proof*.m` | the warp state verified: four energy conditions positive, interior frame boosted 0.040000 c |
| **`warp-drive/index3.py`** | — | **the project indexed on its own three directives; the cell on all three axes, and the cell the closure predicted** |
| **`warp-drive/LAUNCHER`** | **`warp-drive/launcher.py`** | **what the shell can be, since it cannot be a drive: a geodesic launcher at 0 g — the drive is the infrastructure, not the ship** |
| **`warp-drive/GATE 1`** | **`warp-drive/gate1.py`** | **the build spec: degenerate matter from a neutron star, accretion power, the meridional schematic, and the two parameters that vary gate to gate** |
| **`warp-drive/RESIDUE`** | **`warp-drive/residue.py`** | **the three opens are one question; it closes in two directions and leaves one geometry to test** |
| **`warp-drive/OPEN GATE`** | **`warp-drive/torus.py`** | **the surviving architecture tested: hoop tension holds the bore open inside DEC, 5.89x margin at gate scale** |
| **`warp-drive/SPEC SHEET`** | **`warp-drive/gatespec.py`** | **living specification: 44 fields, 9 OPEN, 3 invalidated by the sphere-to-torus change — the sheet is the diagnostic** |
| **`warp-drive/GATE-CLOSED.md`** | **`warp-drive/octave/run_axial.m`** | **the gate dies: a shift cannot terminate in vacuum — Type IV in every cell, at every speed** |
| **`warp-drive/COSMO`** | **`warp-drive/cosmo.py`** | **the shared hypothesis: 5 of 8 bounds assume asymptotic flatness, and superluminal geodesic transport is already observed** |
| **`warp-drive/KERR`** | **`warp-drive/kerr.py`** | **NO-TAPER narrowed: a vacuum shift CAN decay asymptotically — Kerr drags at 0.5 c with T = 0, and J is the charge CM-THEOREM never forbade** |
| **`warp-drive/THE-LOOP.md`** | **`warp-drive/index3.py`** | **the project looped on angular momentum; the two visits together give the trichotomy, and the index now guards against it** |
| **`warp-drive/ELEMENTS`** | **`warp-drive/elements.py`** | **the object is what is shifted: the element sets the density, and f ≤ 1 caps every possible object at 0.0713 c** |
| **`warp-drive/VEHICLE 1`** | **`warp-drive/shipspec.py`** | **the surviving architecture specified: 41 fields, 11 open — the sheet now flies the k-lever, and its one unevidenced object is the companion, not the deflector** |
| **`warp-drive/GRADIENTS`** | **`warp-drive/gradients.py`** | **the gradient space is closed by classification — five types, one pumps, and the engine already runs on protons** |
| **`warp-drive/PERSON`** | **`warp-drive/person.py`** | **from a proton to a person: χ/τ_s is the only argument, and pulling the pass out to 94 r_s buys the deflector down into the LIGO catalogue** |
| **`warp-drive/STATION-KEEPING`** | **`warp-drive/stationkeep.py`** | **the Δv is zero — but the ladder is a conjecture, and the one Monte Carlo of it delivers 0.72× *one* encounter, not 1,090** |
| **`warp-drive/NEC-LADDER`** | **`warp-drive/necladder.py`** | **the NEC is not a boolean: five rungs, the world measured at rung 1 (Casimir), the index's core at rung 3 — and every no-go here was graded at rung 0** |
| **`warp-drive/BEAMED`** | **`warp-drive/beamed.py`** | **the coupling source is *built*, not found: 1000 t to 0.700 c is a published point design, and the roadblock is a bill (208 world-years) not a bound** |
| **`warp-drive/RESTATUS`** | **`warp-drive/restatus.py`** | **every architecture regraded by *how* it closed — of six this project reasoned to itself, zero are closed by measurement** |
| **`warp-drive/THE-DOOR`** | **`warp-drive/door.py`** | **"does not couple to real spacetime" withdrawn: it is h ≈ 4.5×10⁻²⁴, and §17.1's door — a construction is closed from *outside*, by measurement** |
| **`warp-drive/NEC-LAB`** | **`warp-drive/neclab.py`** | **the measurement, taken: the medium *can* carry the analogue NEC violation, at 3.15% of its stability margin — and the reason is structural** |
| **`warp-drive/DEVICE`** | **`warp-drive/device.py`** | **the parts list, every field tested as written: a 16.3 cm YIG-and-copper block at 8.22 GHz, v₀ = 0.222 c — four tests failed and changed the design; `--figure` draws it to scale** |
| `warp-drive/paper/PAPER.md` | — | ⚠ WITHDRAWN draft of the shell paper, kept as the record of what did not stand |

### The rung this project has been standing on

M asked whether there is an aspect of quantum entanglement the warp work is not accounting for. There
is, and the corpus already carries it. **The null energy condition is not a boolean.** The Method's
violation index grades it on five rungs (BUILD180, Part V §5.1):

> NEC null energy | intact / **pointwise** / ANEC arbitrarily small / macroscopic QI-bounded / QI-violating

and names our own place on it:

> *"Our position is (0, 1, 0, 0, 1, 0, 0, 0, 0), with two components fixed by **measurement**:
> S_corr = 1 because quantum mechanics violates Bell locality while respecting microcausality, and
> **NEC = 1 because Casimir energy is measured and violates the null energy condition pointwise**."*

**The world is measured at rung 1.** This project has spent its life at **rung 0** — TARGET-1's
achievement was "all four pointwise energy conditions positive everywhere", which is *stricter than
the universe*. GATE-CLOSED's fatal finding was that a compactly supported shift needs Type IV in
vacuum: that is rung ≥ 1, and rung 1 is laboratory equipment. **The index's own infeasible core is at
rung 3** — core `(X_exp=0, U_ghost=0, NEC_pt=3, EOM=2nd)`, one cell, E = 30 at nine letters and 816 at
fifteen. **Two free rungs between the measured world and the point where the index breaks, and this
project has used neither.**

Rung 2 is named and costed: Visser, Kar & Dadhich (PRL 90 201102), traversable wormholes with
*arbitrarily small* energy condition violations, quantified by `I_V = ∮(ρ + p_r) dV` over the
violating region — and the corpus's own status line, *"I_V can be made arbitrarily small by shrinking
that region, **which is why the NEC axis is graded by scale and not by violation-or-not**."*

**The entanglement enters in three places, and the corpus files all three.**

1. **Rung 1 *is* an entanglement effect.** Casimir energy is vacuum entanglement between boundaries.
   The rung the world stands on is bought with it.
2. **The quantum condition is an entropy bound, and the index has no letter for it.** Appendix D5:
   `⟨T_kk⟩ ≥ (ℏ/2π) S″_out`, the QNEC, with `S_out` the entanglement entropy outside a cut of a null
   surface. Classical NEC forbids negative `⟨T_kk⟩`; **QNEC permits it, budgeted by −S″_out**.
   Entanglement entropy is what pays for negative energy. The corpus's reason for filing it in an
   appendix: *"it does not enter the index as a charge, which is why it appears in the appendix and
   not in the edge list."*
3. **The top of the ladder is guarded by a correlation principle, not a gravitational one.** Two of
   the nine coordinates are quantum-correlation axes — `Sc` (CHSH: local ≤2 / quantum ≤2√2 /
   post-quantum ≤4) and `IC` (information causality) — and the constraint-language defect is the
   arity-4 rule **`NEC ≥ 3 → IC ∨ U ∨ X`**. Macroscopic exotic matter is not forbidden by gravity
   alone. And Audit 22 records that of IC's six term-sharing pairs, *"IC has never been checked once,
   and IC is load-bearing: it is the unique principle forbidding post-quantum correlations."*

**The edge list the compendium says is printed nowhere is in the repository.** Part V: *"the edge list
itself is not printed anywhere in this paper, and until it is, those five conditions are what stands
in its place."* It sits in `extracted/archives/method16-rp-b-data/vi_best.json`, seated by
`tools/consolidate.py` out of `method16_rp_B_data.tar.gz` — 17 rules, which Part V's own recompute note
names by filename. Loaded (never transcribed), it reproduces the printed figures exactly: **19,440-cell
box, 2,370 closed cells**. Five readings of the rule format were tried and exactly one gives 2,370.

**And a finding, recorded and not repaired.** That edge list *forbids the cell the paper names as our
own position*, by one rule: **`Sc ≥ 1 → L ≥ 1 ∨ DNd ≥ 2`** — quantum correlation at the Tsirelson rung
forcing nonlinear evolution or super-quantum discrimination. The world has `Sc = 1` with `L = 0` and
`DNd = 0`. This is *not* offered as physics: the corpus itself rules (V-table) that the violation
index's numbers *"enter as an instance of the operator, never as physics"*, computed *"over a
coordinate set that is demonstrably incomplete"*. The rungs are physics; the cell counts are the
operator; this row is a defect in a fitted rule set.

**What it costs this project.** Three of five measured results sit at rung 0. Two are **unplaced** —
GATE-CLOSED and the torus — for one reason: **`I_V` was never integrated**. GATE-CLOSED counted Type IV
cells and declared the branch dead. Counting cells answers *is the NEC violated*; the ladder asks *by
how much, over what scale*, and nobody here has computed that number.

> **The no-go this project has been obeying is a rung-0 no-go.**

One measurement would settle it: integrate `ρ + p_r` over the violating region of the GATE-CLOSED
shift configurations and place them on the ladder. Land at rung 1 or 2 and the corpus's own index does
not forbid them — the core is at 3.

### The engineering, and what it reverses

M's ruling: the math is not where this project is weak — the **engineering** is. Two fields named,
both read, and the result reverses the session's conclusion.

**The coupling family's inventory problem was self-inflicted.** Its architecture — no propellant,
momentum from an external source, owes no charge — *is beamed propulsion*, a costed discipline with
hardware already in fabrication. This project spent a session hunting the momentum source in the sky.
The engineering literature **builds** it:

| momentum source | terminal | payload |
|---|---|---|
| FOUND: catalogued 50 M☉ binary | 0.039 c | 2 m body |
| FOUND: unconfirmed 8,823 M☉ IMBH | 0.475 c | 2 m body |
| **BUILT: Starshot — $8.0B, in fabrication** | **0.200 c** | 1 g |
| **BUILT: Lubin DEEP-IN, crewed scale** | **0.700 c** | **1000 t** |

A thousand tonnes to 0.7 c is a *published point design* — 36 km reflector, 10 PW, 100 km array. The
heaviest thing this project ever costed on the found-object route was a 2 m body at 0.039 c.

**Mass is far cheaper than it looks.** At fixed sail areal density the sail grows with the payload, so
the beam stays inside it further, so the acceleration run grows too: **`v ∝ m^(−1/4)`**. A factor 10⁵
in payload mass costs **17.8×** in speed, not 10⁵. That exponent is Lubin's *"mild function of payload
mass"*, and it is the most encouraging number in the discipline.

**The invariant of the whole field:** `D_array × d_sail = λ × range` — acceleration ends where the
diffracted spot outgrows the sail. 0.026 AU for Starshot; 22,702 AU for the crewed design.

`beamed.py` reproduces **both** published point designs from one relativistic integrator (Starshot's
0.2 c, Lubin's 0.7 c in 144 days), which is what validates it. And it prices the roadblock:

| case | β | days | run (AU) | beam (J) | world-years |
|---|---|---|---|---|---|
| Starshot 1 g | 0.200 | 0.001 | 0.02 | 1.13e13 | — |
| 100 t to 0.2 c | 0.200 | 13.1 | 245 | 1.13e21 | 1.9 |
| 100 t to 0.5 c | 0.500 | 55.4 | 3,002 | 4.79e21 | 8.0 |
| **1000 t to 0.7 c** | **0.700** | **144** | **12,526** | **1.25e23** | **208** |

Not physics. Not materials. **Energy at planetary scale, delivered coherently through an aperture, for
months.** Sail efficiency runs 16–29%: most of the beam leaves with the reflected photons, and that
shortfall *is* the Doppler factor — it cannot be engineered away, only outrun by going faster.

> **The roadblock has the shape of a bill, not a bound.**

**Particle communication engineering closes a branch.** Hippke (2017) benchmarks every carrier against
photons, and one law decides it:

> particle beam `θ = 1/γ` — **no aperture term at all** — against photon `θ = 1.22λ/D`

At a 1 m aperture these meet at 82 nm, so focusing TeV particles costs **7×10¹⁰** times the energy of
a mirror. Neutrinos are worse: 10¹⁰ times a photon's beam width, and the only demonstrated link runs
at **0.1 bit/s** through 240 m of rock (Stancil 2012). Hippke covers the hypotheticals too — nothing
known or speculated exceeds keV photons *"by more than a factor of a few"*. **So any architecture
needing two coordinated ends pays the full light-travel time, and no carrier shortens it.** Settled,
and not by this tree.

The one place matter beats light is **bulk, not speed**: inscribed matter carries ~10¹¹ bits/J at
0.1 c against a photon channel needing kilometre apertures to match. *If something must be moved
rather than said, move it* — which is the same sentence as beamed propulsion, reached from the
communication side.

**A recorded fault.** The sail integrated in *distance* is singular at β = 0 and returned efficiencies
above 100%. Caught by an identity check (beam energy must exceed kinetic energy), fixed by integrating
in time. The identity is now in the selftest.

### Every architecture, regraded by how it closed

Not re-arguing any of them. One question of each closure: **what kind of thing closed it?**

| kind | meaning | count | which |
|---|---|---|---|
| **MEASURED** | an experiment says no; only a better experiment reopens it | **1** | κ(x) |
| **STRUCTURAL** | a theorem with no hypothesis the world fails | 1 | swimmer |
| **HYPOTHETICAL** | a theorem whose hypothesis is *not satisfied here* | **3** | translate, gate, Kerr |
| **COSTED** | not closed — priced | 2 | slingshot, beamed |
| **OPEN** | not closed, not priced | 2 | shell, analogue |

**Six of the nine came from this project's own reasoning. Of those, zero are closed by measurement,
five are hypothetical or costed, and three were reopened this session** by reading the hypothesis
instead of the conclusion — TRANSLATE (isolation), GATE (rung 0), SLINGSHOT (binding).

The single MEASURED closure came from outside and kills a concept this tree never held: **Rodal 2025
(arXiv:2507.09724)** closes material-dependent gravitational coupling `κ(x)` on the contracted Bianchi
identity plus MICROSCOPE (`η ≤ 1.1×10⁻¹⁵`), Cassini (`|γ−1| ≤ 2.3×10⁻⁵`), PSR J0337+1715
(`η_N ≤ 2×10⁻⁶`) and Eöt-Wash. There is no hypothesis to escape there — the experiments were done.

> **The obstruction is not a wall. It is a habit of banking the strict answer to a stricter question
> than the one asked.**

### The concept that proves its own math

*"A good engineering concept proves the underlying math used to engineer it."* That concept exists,
and it is **analogue gravity**.

**Smolyaninov** (Phys. Rev. B **84**, 113103, 2011) maps the Alcubierre line element one-to-one onto a
medium's electromagnetic response — permittivity ε, permeability μ, and a magnetoelectric coupling
`g_x` under the thermodynamic stability bound

> **g_x² ≤ (ε − 1)(μ − 1)**  →  **v₀ ≤ c/4**

Light in that medium follows geodesics of the emulated metric. Build it and the geometry's kinematics
— the wall, the boosted interior, the horizon structure — stop being solver output and become bench
measurement.

Three things make it the next move rather than a curiosity:

1. **Rodal's measured no-go explicitly does not reach it.** His own §3.3: *"Analog models do not alter
   the Einstein–Hilbert action or violate the Bianchi identity."* The one hard closure on the sheet
   carves it out.
2. **Its ceiling is c/4** — six times the found-object route's 0.039 c — and it is a *material* bound.
   ε, μ and `g_x` are engineering parameters; the bound moves when the materials do.
3. **It transports nothing, and that is the point.** This project has asserted the warp state exists
   *from a solver*. An analogue makes the assertion a measurement — the one thing directive 1 has
   never had.

### The sentence I got wrong

I wrote: *"What it does not do is couple to real spacetime. The analogue proves the kinematics, not
the gravitation."* **Withdrawn.** It was wrong twice.

**Wrong dynamically — I never computed it.** An analogue is real matter in real spacetime and its
stress-energy gravitates like anything else's. For a 1 m³, 3-tonne metamaterial slab: `h ≈ 4.46×10⁻²⁴`;
the pump field at 1 GW/m² weighs 3.7×10⁻¹⁷ kg; the apparatus would need 6.7×10²⁶ kg (≈6.6 Neptunes)
for `h ~ 1`; the emulated shift exceeds the real one by 5.6×10²². So the coupling is tiny and
dominated by rest mass — but *"does not couple"* was never a statement about the world. It was a
number I declined to compute.

**Wrong methodologically, and this is worse — the corpus rules on it and I wrote past the ruling.**
BUILD180's tower-limit argument:

> *"closure cannot tell a measurement from a relabel … **What distinguishes them is the door (§17.1):
> an axis must be an independent degree of freedom**, and a relabel, being dependent, fails it. …
> **That is the step inside lacks and outside supplies**, and it decides L."*
> — and its close: *"The existence of the limit is the law's; **its value is the world's**."*

A construction cannot certify itself. My sentence dismissed the one mechanism the corpus says decides,
and this project has spent a session deriving values that are the world's to supply.

Where I'd state the principle more narrowly, once: a system couples through `T_μν` whether or not
anyone looks — the slab gravitates unobserved, and decoherence entangles systems with environments
with no observer. What observation is *uniquely* necessary for is **closing a construction from
outside it**, which is §17.1's door exactly, and on that the correction stands unqualified.

**The test that replaces the sentence:**

> A result from an analogue is a **MEASUREMENT** iff it tests a consequence derived from the
> *background-field structure* that was **not built into the medium's construction**. Otherwise it is
> a **RELABEL**.

Five of seven analogue claims pass that door, and **four are already done**. Steinhauer's sonic
horizon in a rubidium BEC (Nature **569**, 688) emits an approximately thermal spectrum **at the
temperature Hawking's formula sets from the surface gravity**, its Hawking pair is **entangled**, and
an inner horizon **stimulates emission** as predicted. None of that is built into a BEC — you engineer
a flow profile. The door was passed, for gravitational physics derived on a background.

> **The analogue is not a simulation of the math. It is where the math is answerable by the world
> rather than by the solver.**

**The one that passes the door and has not been taken:** whether the medium can carry the analogue of
the NEC violation, and at what cost. The geometry demands it; the material has never been asked. It is
the same quantity this project has argued about from a solver all session.

**And the entanglement thread closes.** The QNEC says `⟨T_kk⟩ ≥ (ℏ/2π) S″_out` — entanglement entropy
outside a null cut is what licenses negative energy, and the corpus files it in an appendix, out of the
index. **Steinhauer measured the Hawking pair entangled across the horizon. That is the same `S_out`.**
The quantity the QNEC says pays for negative energy has already been measured, in an analogue, across
a horizon.

What stays true, narrowly: an analogue does not *gravitate* the emulated shift, so claiming propulsion
from one is the error Rodal killed. It measures.

### The measurement, taken

**Q: can the medium carry the analogue NEC violation, and at what cost?** Smolyaninov's own paper is
where the gap sits — *"Since energy conditions violations do not appear to be a problem in this case,
metamaterial realization of the warp drive is possible."* Asserted, never computed.

**A: yes, and it costs 3.15% of the stability margin. The reason is structural.**

First, **c/4 re-derived rather than quoted.** Eq (10) is `βf̃ ≤ (n−1)/n²`; its derivative in `n` is
`(2−n)/n³`, zero at **n = 2**, giving exactly **1/4**. But that is the *leading-order* figure. Carried
through the full Eqs (6) and (7), the margin at `f̃ = 1` goes negative before β reaches 0.25:

| | |
|---|---|
| exact saturation | **β = 0.245826** |
| margin at exactly c/4 | **−0.063247** — unstable |

A 1.7% correction, recorded because a bound quoted to two figures should hold at two figures.

**Then the answer, and it is a theorem, not a number.** The stability margin
`m = (ε−1)(μ−1) − g_x²` is a function of **f̃ alone** — no derivative of f̃ appears in it — and it is
strictly monotone decreasing. So:

> **The margin minimum is always at max f̃ — outside, where the profile is flat.**
> **The NEC violation goes as (df̃/dx̃)², so its peak is always strictly inside the wall.**
> **For any monotone shape function the two cannot coincide.**

Checked on three:

| shape | NEC peak at f̃ | margin min at f̃ | coincide |
|---|---|---|---|
| Lorentzian | 0.2500 (at x = a/√3, analytic) | 0.9994 | no |
| tanh | 0.5000 | 1.0000 | no |
| quartic | 0.3750 | 1.0000 | no |

**The material is stressed by the shift. The geometry violates the NEC with the shift's *gradient*.
They live in different places.** At the design limit, on Smolyaninov's own profile: margin **+1.000**
with no shift, **+0.9685** where the geometry asks most, **0.000** where the material is worst off.
Just inside saturation the ratio between those two is **27**.

> **The medium can carry the analogue NEC violation. It is not what costs. What costs is the
> asymptotic shift — and that is what c/4 already prices.**

**What it settles:** the energy-condition objection does not transfer to the analogue, now for a
computed reason. Smolyaninov was right and did not show it.

**What it does not:** the remaining cost is materials, and it is the one he *did* quantify — classical
magnetoelectrics (Cr₂O₃, multiferroics) sit two orders of magnitude below the Eq (9) limit, so the
build needs the engineered split-ring-plus-magnetised-ferrite design, non-reciprocal and
bi-anisotropic, with loss compensation. An inventory of parts, not a bound. And it remains an
analogue: it does not gravitate the emulated shift.

Under `door.py`'s test this is a **measurement, not a relabel** — the requirement came from the
geometry and was not designed into the material, which is exactly why it could have come out the
other way, and did not.

### The parts list, tested as it was written

Not a spec sheet with a test appendix — every row carries its own test and verdict. **Two failed on
the first pass and changed the design.** They are the argument for the discipline.

**The design point.** A benchtop microwave block. Nothing in it is an "advanced material".

| | |
|---|---|
| emulated warp speed v₀ | **0.2224 c** — derated 9.5% (4.8% registration + 5% safety) |
| background index n | 2.0 — argmax of (n−1)/n² |
| ε = μ at the wall | 2.2331 |
| magnetoelectric g_x | 1.1093 |
| operating frequency | **5.784 GHz** — set by the ferrite, not chosen |
| unit cell / wall / radius | 2.32 mm / 2.32 cm (10 cells) / 9.28 cm |
| **device span** | **23.2 cm** |

**Tests that passed.** *YIG ferrite*: 4πM_s = 1750 G at 0.30 T bias gives FMR at 8.40 GHz; the
required g_x = 1.109 is reached at 5.784 GHz — **1,869 YIG linewidths off resonance**, which is why
the loss stays low. *Split rings*: ε = μ = 2.23 is modest, needing rings resonant at 6.83 GHz, 18%
above operating. *Loss*: 6.1% across the whole block at Q = 10³, 0.6% at Q = 10⁴; Q = 10² (47%) needs
the gain-medium compensation Smolyaninov cites.

**TEST 4 FAILED AND CHANGED A PART.** The ferrite *fixes* the operating frequency, so the rings aren't
free to be any size. A conventional **single-gap** split ring of the required 2 mm diameter:
`L = 1.47 nH`, `C_gap = 1.24 fF` → **f₀ = 118 GHz. Sixteen times too high.** The gap capacitance of a
single split is femtofarads and nowhere near enough. The fix is a **broadside-coupled** ring — two
rings facing across a thin high-permittivity substrate, so the capacitance is the ring-to-ring overlap:
`ε_r = 20, h = 0.5 mm → C = 356 fF → f₀ = 6.95 GHz`. In range. *Found by pricing the part; a layout
drawn from the required f₀ alone would have been fabricated before anyone noticed.*

**TEST 5 FAILED AND ADDED A DESIGN RULE.** The wall is only ten unit cells, so the profile is
quantised. If the split-ring layer and the ferrite layer are **mis-registered by one cell** — g_x one
step ahead of ε — the stability bound is violated at the outermost step: **margin −0.355**. Fatal
there and nowhere else, because that cell sits at *zero margin by construction* at the design limit.
Two fixes, and the design takes both: co-locate the ferrite inside the ring (Smolyaninov's own Fig. 2
geometry, which now has a reason rather than a convenience), and **derate**:

| cells across wall | safe v₀/c | derate | wall |
|---|---|---|---|
| 5 | 0.2244 | 8.7% | 1.0 cm |
| **10** | **0.2341** | **4.8%** | **2.1 cm** |
| 20 | 0.2397 | 2.5% | 4.2 cm |

*A built device that skipped this would have shown an unexplained instability at its outer boundary,
and a one-cell offset between two lithography layers is close to undiagnosable after the fact.*

**And a third, from the selftest itself.** `safe_beta()` bisects to *zero* margin — it finds where the
mis-registered cell just touches the bound. The selftest refused to call zero positive, which is the
discipline working: **a bisected boundary is not a design point.** The design now sits 5% inside it.

**TEST 6 FAILED: ε = μ is a constraint on the ring gap.** Smolyaninov's Eq (11) has `ε−1 ∝ d²` and
`μ−1 ∝ S²ω²/c²`, so ε = μ **iff `d = Sω/c`**. The gap is not a design knob — it is fixed by the ring
area and the operating frequency. Every geometry I had "chosen" was actually determined.

**TEST 7 FAILED, AND MOVED THE WHOLE DESIGN.** The ferrite must be graded, and grading the *bias*
would drift the FMR across the block — so grade the **fill** at constant bias. But YIG's own
`ε_r = 15` drags each cell's permittivity up by `14f`, and the ε budget is only 1.233. **Fill ≤ 8.8%.**
That forces the ferrite to supply a *bulk* g_x of 13.8 rather than 1.11, which pulls the operating
point from 5.78 GHz to **8.22 GHz** and from 1,869 linewidths off FMR to **128**. Still safe, 15×
tighter, and the whole geometry chain moved with it.

**And then TEST 4 failed a second time.** The higher frequency shrank the unit cell from 2.32 mm to
1.63 mm, and the 2 mm ring carried over from the first pass no longer fit. **Ring radius and substrate
thickness are now derived, not assumed** — `r = 0.9(cell/2 − w)` and `h` solved so the broadside
resonance lands exactly on target. That is the cascade the discipline is for: one upstream change
invalidated a part that had already passed.

**The design point as it now stands:**

| | |
|---|---|
| v₀ / ε=μ / g_x | 0.2224 c / 2.2331 / 1.1093 |
| operating frequency | **8.221 GHz**, 128 YIG linewidths off FMR |
| ferrite fill / bulk g_x | 8.0% / 13.84 |
| cell / wall / radius | 1.633 mm / 1.633 cm / 6.53 cm |
| ring r / gap / substrate | 0.555 mm / 0.167 mm / ε_r 20 at 0.353 mm |
| **device span** | **16.3 cm** |

**TEST 8 FAILED, AND THE GEOMETRY WAS WRONG.** Smolyaninov's Eq (2) is explicitly **1+1
dimensional** — y and z are flat spectators and the shift is carried by x alone. The device is a
**stack graded along one axis**, not a spherical bubble. The first figure drew a sphere and was wrong.
Transverse extent is free, set by beam aperture.

**TEST 9 REFRAMED WHAT THE DEVICE IS.** A magnetised ferrite's Polder tensor gives
`μ − 1 = ω_m ω₀/(ω₀²−ω²)` — **the same expression as g_x**. So one inclusion supplies all three
responses, and at 8% fill the ferrite carries **90% of ε−1, μ−1 and all of g_x**. The split rings
supply ~10%. This is a **graded magnetised-YIG composite with rings as a stabilising correction**, not
an SRR metamaterial with ferrite inclusions. The ferrite alone has only 1.2% stability margin —
**the rings are what supply the margin**. And because one physical inclusion carries all three,
they cannot mis-register against each other, which removes most of TEST 5's failure mode.

**TEST 12: the loss model was wrong, and the fix isn't where I expected.** A single Q for the whole
block gave 6%. Weighting by actual share gives **20.6%** — ferrite-dominated, and *better rings don't
help* (Q = 100 → 27%, Q = 1000 → 20.6%). Raising the background index n doesn't help either: the fill
ceiling rises as (ε−1) and the required g_x rises with it, so the bulk g_x and the detuning are
**invariant under n — an exact cancellation**. What's left is a single figure of merit:

> **FOM = M_s / ((ε_r − 1) ΔH)** — high saturation magnetisation, low permittivity, narrow linewidth.

| ferrite | μ₀M_s | ε_r | ΔH | tan δ | FOM |
|---|---|---|---|---|---|
| YIG, standard | 0.175 T | 15 | 0.50 Oe | 0.0088 | 250 |
| **YIG, premium sphere** | 0.175 T | 15 | **0.20 Oe** | **0.0035** | **625** |
| Li ferrite | 0.370 T | 16 | 2.0 Oe | 0.0178 | 123 |
| NiZn spinel | 0.400 T | 12 | 5.0 Oe | 0.0302 | 73 |

Premium YIG spheres (ΔH ≤ 0.2 Oe) are catalogue parts. With those and a shorter interior:
**5.8% loss.**

**The design as it now stands:**

| | |
|---|---|
| v₀ / ε=μ / g_x | 0.2224 c / 2.2331 / 1.1093 |
| operating frequency | 8.221 GHz, **320** YIG linewidths off FMR |
| ferrite fill / bulk g_x / share | 8.0% / 13.84 / **90%** |
| cell / wall / ring r / gap | 1.633 mm / 1.633 cm / 0.555 mm / 0.167 mm |
| **geometry** | **bar, 9.8 × 8.2 × 8.2 cm** — graded along x only |
| loss across the stack | **5.8%** |

### And then the test that decides whether it proves anything

**The observable is enormous.** For propagation along the shift a bi-anisotropic medium gives
`n± = √(εμ) ± g_x` = 3.342 and 1.124 — forward 0.299 c, backward 0.890 c. Over the 9.8 cm bar that is
a **0.725 ns non-reciprocal delay, 2,146° of phase** at 8.221 GHz. A VNA resolves 0.01°, so it is
unmissable by five orders of magnitude. And no graded-index bar can do it: Lorentz reciprocity forces
`S21 = S12` in any reciprocal medium.

**But it is a relabel.** `n± = ε ± g_x` is bi-anisotropic Maxwell. It confirms you built the medium
you designed. Under `door.py`'s test that is not a measurement of the metric.

**So what would be? A horizon. And a horizon is forbidden.** A horizon at normal incidence needs the
shift to reach the medium's own light speed, `v₀ ≥ c/n`. Smolyaninov's stability bound caps it at
`v₀ ≤ c(n−1)/n²`. So a horizon requires

> `(n−1)/n² ≥ 1/n` ⟺ `n−1 ≥ n` ⟺ **`−1 ≥ 0`**

**False for every n.** The thermodynamic stability condition that makes the analogue buildable is the
same condition that forbids it a horizon. The closest approach is `(n−1)/n`, which reaches 1 only as
`n → ∞`, and the ferrite caps `n ≤ ε_r = 15` — **93.3%, never 100%.**

| n | v₀ max | v₀/(c/n) | θ_c | ferrite fill |
|---|---|---|---|---|
| 2 | 0.250 c | 0.500 | 60.0° | 0.07 |
| 10 | 0.090 c | 0.900 | 25.8° | 0.64 |
| **15** | 0.062 c | **0.933** | 21.0° | 1.00 (pure ferrite) |
| 20 | — | 0.950 | — | impossible (fill > 1) |

What survives is the **one-way angular horizon** at `θ_c = arccos(v₀n/c) = 60.22°` — genuinely
metric-like, because total internal reflection is reciprocal and this is not.

**And the quantum measurement is too cold.** Analogue Hawking temperature at the design point is
`T_H = ℏκ/2πk_B` = **4.96 mK**, below a dilution refrigerator's routine 10 mK base. `T_H ∝ β·f`, so
moving to ~100 GHz in an 8 mm device would give **60 mK** — measurable, but that is a superconducting
magnet at 3.6 T, microfabricated rings, and a different experiment.

> **Verdict: the hardware closes. The epistemics do not.** The device is buildable from catalogue
> parts and would work. It would confirm that we built the medium we designed. It would not prove the
> metric, and the bound that makes it stable is the bound that stops it.

`THE-DEVICE` is regraded in the index from (+1,+1,+1) to **(0,+1,+1)** — buildable, yields numbers,
identifies no warp energy — and `ANALOGUE` is narrowed to match.

> **Across three passes: one part replaced twice, one derating, one safety factor, four "chosen"
> dimensions that were determined, one geometry withdrawn, one loss model replaced, and one claim of
> proof withdrawn.**

`device.py --figure` emits `figures/device-scale.svg` from `design()`, so the drawing cannot drift
from the sheet — it now draws the stack.

## `warp-drive/`

Seats the warp drive — cited twice in `method/members/Transitions.md` and never named again — as an
object threshold in that paper's own index, and computes its energy budget and engine specification
against the primary literature.

```
python3 research/warp-drive/warpdrive.py --selftest   # 104 fixtures
python3 research/warp-drive/warpdrive.py              # the full report
```

`WARP-DRIVE.md` answers the question from the index and the literature. `ENGINE-ASSESSMENT.md`
reviews `drive/The Method Materials/warp drive theory.pdf` — the design deliverable, seated in the
mirror by `drive_sync.py --adopt` at status `ok-adopted` — against the same physics, and computes
every claim in it that is computable.

`pdftext.py` beside them is not an audit instrument and takes no selftest: it is a PDF text extractor
written because this container has neither poppler nor `pypdf`, and because the producer of that file
puts page layout in `q`/`cm`/`Q` graphics transforms, encodes glyphs as two-byte hex through
`/ToUnicode`, and emits spaces as explicit glyphs. It tracks the full CTM and never inserts a space
heuristically.

The fourteen papers run in order. `WARP-DRIVE.md` places the object and gives the buildable
specification. `ENGINE-ASSESSMENT.md` reviews M's design deliverable against it.
`ROTATING-SHELL.md` takes the one idea in that deliverable which survived review and carries it onto
the buildable solution. `SHIFT-CEILING.md` answers the one number Fuchs et al. named as open — how
far the shift vector can be pushed before the drive stops being physical — and finds a closed form.
`SHELL-PROFILE.md` then replaces that paper's eyeballed input with a TOV integration and corrects it
downward, and `ACCELERATION.md` prices the problem all five defer. A paper is never edited to match a
later finding: `SHIFT-CEILING.md` and `SHELL-PROFILE.md` carry notes naming what superseded them, and
every state stands. `SOURCE-CODE.md` is where the series corrects itself — it reads the authors'
published toolkit and finds two of this series' own inferences wrong, both in the flattering
direction. `MEASURED.md` then runs that toolkit under GNU Octave and replaces every inferred number
with a measured one, and `WHAT-BINDS.md` measures the two things that paper left open — overturning
a design rule this series had published, and raising one careful question about the instrument
everything downstream depends on. `THE-DESIGN-EQUATION.md` then applies **P8** — *any true answer,
good or bad, is a bound*, and *three bounds on one object are a coordinate* (`The_Method_1_6-2.md`
§2.15, §2.17.3) — to the bounds the first nine established, and turns them from a limit into a design
equation with a measured 1.6x gain and a bound on the whole family. `DENSITY-IS-CLOSED.md` then
builds the first of the two levers that bound named, measures it, and closes it — leaving one. `SPHERICITY.md` measures what that last one costs, attempts
it, and reports the attempt invalidated by its own control: the lever is untested rather than closed,
and the class bound is not final. `THE-BORROWED-WELL.md` then applies **register 1206** — *"E_W = 0
was the Method equation reporting that no STEP could carry a value"* — reads the design equation
backwards, and finds that the transport the shell manufactures can be borrowed instead, in closed
form and for nothing.

The instrument copies the fifteen-letter closure rules verbatim from `recovered/objects15.py` with a
provenance comment, per the standing rule that an instrument imports a seated form and never silently
reimplements one. It reproduces `TRANSITIONS` §7.1's printed 18,888 / 18,072 / 816 before reporting
anything.


## The turn

The first fourteen papers asked whether a **warp shell** can be built and answered by optimising the
only object that satisfies all four energy conditions while carrying a shift. The answer was no, by
10³¹ — and two papers later it became clear the ceiling those papers measured was an artefact of a
bad slice and a mis-lowered index (`NEC-CORRECTION.md`). Correcting it doubles the ceiling and
changes nothing: a 2× correction to a number 31 orders from useful is not a result.

The assumption those papers never examined is that an engine **sources** the metric it uses. Both
lethal facts — the 10³¹ gap and the ADM no-self-acceleration theorem — follow from it alone.
`THE-ENGINE.md` drops it. An engine is a **coupler**: a device that modulates its coupling to a
gradient it did not make. Built of ordinary matter, it satisfies every energy condition trivially,
because there is nothing exotic in it to check.

Two couplers are assessed. The **curvature swimmer** (Wisdom 2003) is a real effect and a dead
engine, bounded by `Δs ≤ A·a_tide/c²` ≈ 10⁻¹⁵ m per cycle — recorded as a bound. The **binary
slingshot** is live: a black hole binary is a flywheel already spinning, the fractional gain in γ per
pass does not saturate, and a steered vehicle keeps the first-order law a random population loses.
Worked point design: **0.87 c in 11 minutes at 1 g with zero propellant**, off two 27,900 M☉ holes.

Its honest limit is not physics but **inventory** — the engine is a found object, and no
intermediate-mass black hole binary is confirmed nearby. That reduces the question to an
observational one, which LISA is built to answer.

**And then most of the inventory problem dissolved.** Zhang's law is a law about *test particles*;
a person differs from a proton by having extent, and `person.py` finds that the extent enters
through exactly one group — the **fragility** `χ = √(extent / survivable tide)` against the
deflector's `τ_s = r_s/c`. The closest survivable pass is `k = (χ/τ_s)^(2/3)` r_s and nothing else
about either body enters. The consequence is a scaling identity: **a 2 m person at a 50 M☉ binary
and a proton at a 1.2 × 10⁹ kg one are the same mission** — same `k`, same gain, same 1,090 passes —
because `χ` rises by 8.2 × 10²² between them and so does the mass. The mission clock is the only
thing that differs, and it differs as `M`.

That turns the deep pass into a *choice*. Deflector mass falls as `k^{-3/2}` while passes rise only
as `k`, so trading gain for distance is a **3:2 exchange in your favour**: pulling the pass from
3 r_s out to 94.4 takes the deflector from 8,823 M☉ down to **50 M☉ — GW150914 was 36 + 29**. The
worked case is a person to 0.87 c in **4.3 hours at 1 g**, 1,090 passes off two catalogued holes,
zero propellant.

Two bounds came with it. The binary must *survive* the mission: orbits-to-merger goes as `β⁻⁵` and
passes as `1/β`, so the margin goes as `β⁻⁴` and **β ≤ 0.0587** — Zhang's headline `β = 0.2` misses
by 132×, and it is the clock that forbids it, not the mass. And the IMBH did not vanish, it *moved*:
Routh's `μ < (9−√69)/18` means a 50 M☉ deflector with a stable L4/L5 parking point needs a
**1,248 M☉** companion. The intermediate-mass hole is a **parking requirement, not a tidal one** —
which puts the whole remaining question on the station-keeping Δv, a number this tree has never
computed.

**Then a bill arrived that turned out not to be owed.** Every sheet in this tree carried one OPEN
row — the station-keeping Δv across N passes, "the number that decides whether the ship needs an
engine". `stationkeep.py` computed it and produced a theorem: a payload only returns for another
pass if it is gravitationally **bound**, bound means `E/m < 1` which *is* its γ at infinity, so
before the last pass `γ ≤ 1` and the terminal speed is set by **one** pass regardless of N. The
ladder was dead, 0.87 c was unreachable, and holding the payload for 1,090 passes cost **6.711 c**
of Δv.

**The arithmetic was right and the premise was wrong, and the literature says so — including the
paper this project's own gain law came from.** `E/m` is conserved in a *static* field. A binary is
not static:

- **Zhang 2020 §3.3** (arXiv:2001.09385): *"for a particle to escape the binary, it is not sufficient
  to just have enough energy. The particle has to consistently move in the same outward direction
  over a period of time. Such escape attempts are however frustrated by the rapidly shifting
  gravitational potential in the vicinity of the binary, due to the BHs moving about."*
- **Shipley & Dolan 2016** (CQG 33 175001, arXiv:1603.04469): a binary spacetime admits more than one
  fundamental null orbit and therefore **"an uncountably infinite set of perpetual null orbits"**. A
  photon cannot be more unbound than it is, and it can still fail to escape a pair. That alone
  disposes of "bound" as the return criterion.
- The dihole chaos Zhang cites: null geodesics in a two-black-hole field admit going-around sequences
  *"of arbitrary length — in fact, even infinitely lengthy ones where the geodesics do not ever escape
  or fall into either BH exist."*

**N is unbounded. The ladder stands and no Δv is owed: the binary turns the payload around for
free.** That is what the second body is for — and `stationkeep.py`'s static arithmetic, which was
never wrong, is exactly why one deflector cannot do the job: a single hole holds a payload for
**four passes** and then charges 6.18 × 10⁻³ c to get it back.

**The leading-face question is answered too, and Fermi answered it in 1949.** No converging-mirror
geometry is needed: aberration crowds incoming particles onto the head-on direction in the hole's
comoving frame, so accelerating encounters outnumber decelerating ones. Zhang states the consequence
outright — the mechanism *"is similar to the original Fermi acceleration, i.e., being of **second
order**"*.

**And that is the real bill.** Zhang's 50%-at-0.2 c is optimised over the entry phase φ₀ and the
angular momentum L. A payload that cannot choose those takes Fermi's average instead: one more
factor of β_A in the gain, hence **1/β_A times the passes**.

| β_A | N steered | N random | margin steered | margin random |
|---|---|---|---|---|
| 0.050 | 654 | 13,068 | 1.90 | 0.10 |
| **0.030** | **1,090** | **36,330** | **14.67** | **0.44** |
| 0.020 | 1,636 | 81,762 | 74.24 | 1.49 |

At the design point the unsteered payload wants 36,330 passes against 15,990 orbits before merger.
**The binary merges with the payload still aboard.**

> **Steering is not an optimisation of this architecture. It is the mechanism.**

`navigate.py`'s braid word finally has a job description: hold the first-order branch. And the open
item is no longer a fuel number but **ν, Zhang's per-pass vanquish probability** — the chance of
being swallowed by a hole or leaving early. For a *population* he estimates trajectories reaching
N = 1000 are suppressed by `(1−ν)⁹⁰⁰` (10⁻²⁷¹ at ν = ½), and argues ν *declines* as the payload
becomes more light-like. For a *vehicle* nobody has computed it — not here, and not in a literature
that is about cosmic rays rather than crews.

Two independent figures from the older three-body literature bracket the regime and neither
contradicts it. Aarseth's classical slingshot condition (arXiv:astro-ph/0511565, Eq. 3) is
`v_f = √(G M_t / 2a)`, which in this tree's variables is exactly `√2 β_A` — 0.289 c at the tightest
binary that can exist — and he notes close-pericentre encounters exceed it *"by a considerable
amount"*, which is precisely the optimised branch. Mikkola & Valtonen (1990) put the limiting
ejection speed for *black hole pairs* at ~10,000 km/s = 0.0334 c, an empirical ceiling from
galactic-nucleus mergers where GW inspiral caps how hard the binary gets — the same merger clock,
seen from the other end.

**And then it turned out somebody had already run the simulation.** The 1,090-pass ladder is a
*conjecture* this project inherited. Zhang derives `N_min = 50…1000` as a **requirement**, not an
outcome — and notes those values are *"already larger than the number of deflection events seen for
the arbitrary (generic) trajectories"* in his own Fig. 1. **Acevedo & Ritz (2026, arXiv:2603.08781)**
evolve an ensemble of three-body systems to ejection or capture, first-principles Monte Carlo, over
exactly this process.

This tree reproduces their published Sgr A* system to 0.2%:

| | this tree | their printed value |
|---|---|---|
| companion orbital speed | 4,843 km/s | 4,850 |
| primary escape at R_orb | 6,849 km/s | 6,860 |
| single-encounter maximum | 11,518 km/s | 11,500 |

**And their simulation then delivers 8,300 km/s — 0.72× *one* encounter.** It does not compound; it
falls short. For equal-mass compact binaries, where the spheres of influence overlap, they report
ejections exceeding the single-encounter estimate *"by an order unity factor"*. Order unity. Not 10⁹.

> **The ladder is a conjecture. The only end-to-end simulation of it does not see it.**

That is not a refutation of Zhang — his per-encounter law is derived and stands, and A&R's Eq. 2.10
is its Newtonian limit. It refutes the **architecture** this project built on top of it, which needed
1,090 consecutive optimised encounters and treated them as merely improbable rather than unobserved.

**A conservation law says the same thing, more weakly and far more certainly.** A circular binary is
invariant along its helical Killing vector, so a geodesic conserves the relativistic Jacobi constant
`𝒥 = ε − Ω·ℓ` (in numerical relativity, the first law `δM = Ω δJ`). Energy grows only if angular
momentum grows with it, and `ℓ` is set at the encounters where `|ℓ| ≤ γ r_enc`. With
`β_co = Ω r_enc/c`:

> **γ_f ≤ γ_i (1 + β_co)/(1 − β_co)** — and **N does not appear**.

It is true and it is useless: in A&R's system it permits 75,000 km/s where they measure 8,300 — 9×
too loose. Recorded anyway, because a loose bound that is certainly true outranks a tight one that is
not, and because this is the law the withdrawn theorem mistook for a binding-energy budget.

**One more constraint, and it is pure geometry.** The two holes are two scattering centres only while
`a > 2 k r_s`, i.e. `β_A < 1/(2√(2k))`. At Zhang's deep pass `k = 3` that is **0.2041 — identically
the ISCO limit**, because `a > 6 r_s` per component *is* `a ≥ 3 r_s` of the pair. Two constraints,
one constraint.

| k (r_s) | deflector | β_A max | measured ceiling |
|---|---|---|---|
| 2.0 | 16,209 M☉ | 0.250 | 0.598 c |
| 3.0 | 8,823 M☉ | 0.204 | 0.475 c |
| 30 | 279 M☉ | 0.065 | 0.093 c |
| **94.4** | **50 M☉ — catalogued** | **0.036** | **0.039 c** |

A 2 m body at 1 g reaches **0.039 c** off the catalogued pair and **0.475 c** off an 8,823 M☉ one —
the IMBH is worth 12× the terminal speed. `shipspec.py` now carries 0.866 c as **ASSUMED** with the
measured figure beside it.

**A recorded fault, kept executable.** A first pass at this fixed the pass distance at a constant
fraction of the binary *separation* (`r_p = a/3`) and read off `M ∝ β³` — a person at 51 M☉ and
β = 0.03. The mass was very nearly right and the reasoning was wrong: `a/3` is 92.6 r_s out, where
an ultrarelativistic particle bends by 1.24°, and the gain there is 6.5 × 10⁻⁴ per pass rather than
the 0.075 the saturated law asserts — **overstated 115.7×**. `person.retracted_beta3_gain()`
recomputes the refutation so it cannot be quietly re-derived.

**A second scaling error, found later and larger than the first.** Every mass and density figure in
the first fifteen papers was quoted at the published example's `R₁ = 10 m`, and the size was never
varied. But `M ∝ R` while `ρ ∝ 1/R²`, so "666,000 × nuclear density" describes a 20 m ship and not
warp shells. `THE-DRIVE.md` runs the trade: there is **no material that makes a small warp shell**,
and **nuclear matter makes a 5 km one** — 1.11 M☉, 0.0476 c, flat interior, all four energy
conditions satisfied, by internal circulation at 0.330 c geared 6.94:1. That is the original
Architecture B topology at the right scale. The bill is ~10⁴⁶ J twice over and a neutron star: one
stellar catastrophe, not 10³¹.

## The 1+1D reduction was flat all along

Two 2026 papers, read this pass, moved the project further than the previous fifteen instruments
combined. One closes the metamaterial route; the other opens the first route with no exotic matter
anywhere in it.

### `twist.py` — `E = −Ω²/(8πG)`

`device.py` had produced a complete parts list for a Smolyaninov analogue: 8.221 GHz, a 9.80 cm
graded YIG stack, 5.756% loss, 107 selftest checks, and one hard negative — TEST 16, that
Brown–Hornreich–Shtrikman stability forbids an analogue horizon for **every** background index,
since a horizon needs `v₀ ≥ c/n` and stability caps `v₀ ≤ c(n−1)/n²`, and `(n−1)/n² ≥ 1/n ⟺ −1 ≥ 0`.
That was read as the wall the design hit. **It was the wrong wall, twice over.**

**First: a horizon was never required.** A forward-directed null ray in bubble-comoving coordinates
has `dx′/dt = v_s(f−1) + c`, which vanishes at `f* = 1 − c/v_s`. Since `f ∈ [0,1]`, that locus exists
**iff `v_s ≥ c`**. The horizon is the signature of the superluminal case, and it is a pathology, not
a feature — Krasnikov, and Everett and Roman, show the crew cannot create, steer or stop the bubble
from inside precisely because of it. A subluminal warp drive has no horizon and needs none. TEST 16
was arithmetically right: the analogue simply declines to emulate the uncontrollable regime.

**Second, and this is the finding.** For the Alcubierre metric the Eulerian energy density and the
coordinate vorticity of the shift are the same object:

> **E = −Ω²/(8πG)**

Negative energy is not a price paid alongside the transport. It **is** the twist, squared. Barzegar,
Buchert and Vigneron (arXiv:2602.16495) prove the consequence as their **Theorem III.15**:
*a coordinate vorticity-free Alcubierre warp drive is Minkowski.*

And `Ω² = (y²+z²)/(4r_s²)·V_s²·f′²` vanishes identically at `y = z = 0`.

> **Smolyaninov's 1+1D reduction is the on-axis line of the bubble, and on that line the Alcubierre
> warp drive is flat spacetime.**

He reduces to one spatial dimension, in his own words, "to avoid unnecessary mathematical
complications." The reduction retains precisely the locus where there was nothing. The device is not
wrong — the 2,146° of non-reciprocity it produces is a real material property, faithfully measured.
The claim that it measures **metric** content is what falls. This supersedes `RELABEL-ONLY`, which
said the observable was a relabel; this says the *target* was flat.

Three independent routes, all executed in the file:

| route | statement | check |
|---|---|---|
| gauge | `dT = dt + v dx/(c²−v²)` diagonalises the 1+1D metric globally | coefficient residual exactly 0 at five `v` |
| dimension | `ξ ∧ dξ` is a 3-form, identically zero on a 2-manifold | closed form vs. finite differences, 6.1×10⁻¹¹ |
| literature | the wedge **is** BBV's Ω | ratio 1.000000000 at five off-axis points |

The tortoise time `T = t + ∫v dx/(c²−v²)` is global iff there is no horizon; where `v` crosses `c`
transversally it diverges logarithmically, and the file **measures the rate** — 0.5975, 0.5997,
0.5995 per decade against the predicted `1/(2u′(x₀)) = 0.6`. So in 1+1D the only non-gauge content
of the metric is a horizon, and stability forbids that. Gauge or forbidden: there is no third case.

**What would fix it, stated so it can be costed.** An analogue must be at least **2+1D**, with the
shift graded *transversely* (`∂_y f ≠ 0`). One encouraging number: the twist peaks at `f = 0.6226`,
where `neclab.py`'s stability margin is **+0.7555**, against **+0.0000** at `f → 1` where the medium
is worst off. The two extrema are disjoint — exactly the structure `neclab.py` found for the NEC
violation. `ANALOGUE-2D` is now the only OPEN row on the architecture sheet with a stated experiment
attached.

### `warpshell.py` — the first architecture with no negative energy in it

An T. Le, *Steering a warp drive without exotic matter* (arXiv:2606.22531), exhibits an exact
solution that is simultaneously an exactly Riemann-flat passenger cavity, **accelerating** by a
covariant matter-derived proper acceleration, and dominant-energy admissible **observer-robustly in
bulk and shell** — not merely for the comoving Eulerian observer, the failure mode
Santiago–Schuster–Visser exposed. The exterior is the exact Kinnersley photon rocket; the cavity is
vacuum; the shell is what the field equations return. Bulk energy conditions collapse to `n₂ ≥ 0`.

**This project's `CM-THEOREM` is not refuted. It is paid.** Le's Theorem 1 is its exact GR form: an
asymptotically flat, dominant-energy drive with a confined source changes its Bondi four-momentum
*only* by radiating to null infinity. The escape from "no isolated system moves its own centre of
mass" is to stop being isolated.

The control law is closed form, `−ṁ ≥ 3m|a|`, integrating to `m_f/m₀ = e^{−3Δη}` with a universal
Tsiolkovsky constant 3. An ideal photon rocket — the best any rocket can be — has the same law with
constant 1. So the warpshell's mass ratio is the **cube** of an ideal photon rocket's. And since
`e^{−Δη}` is the square root of the relativistic Doppler factor, the budget has an exact closed form
in β, derived in the file rather than quoted:

> **flyby:** `m_f/m₀ = [(1−β)/(1+β)]^{3/2}`  **cruise and stop:** `m_f/m₀ = [(1−β)/(1+β)]³`

— the same Doppler factor `beamed.py` already uses for the sail, cubed. At β = 0.2, out and stop,
that is exactly **8/27**: the ship radiates 70.4% of its rest mass. At β = 0.5 it is exactly **1/27**.
Le's own worked burn is Δη = 0.24, and `1 − e^{−0.72} = 51.32%`, reproducing his "about half".

| β | Δη total | m_f/m₀ | radiated | ideal photon rocket | penalty |
|---|---|---|---|---|---|
| 0.05 | 0.10008 | 0.740633 | 25.94% | 0.904762 | 1.22× |
| 0.10 | 0.20067 | 0.547708 | 45.23% | 0.818182 | 1.49× |
| 0.20 | 0.40546 | **0.296296** | 70.37% | 0.666667 | 2.25× |
| 0.50 | 1.09861 | **0.037037** | 96.30% | 0.333333 | 9.00× |

**What it does not buy, stated first.** Not superluminal. Not reactionless. And **no free fall** —
"passengers feel proper acceleration, not the zero-g free fall of an idealized Alcubierre interior."
What vanishes is the *tidal* tensor: the cavity is exactly flat, so there is no differential
stretching. That is the entire warp feature, and it is not the popular one.

**And the real wall is not the budget.** The realized tangential-pressure wall sits exactly on the
Poisson–Visser marginal curve `V″(R) = 0` — a radial displacement is a neutral zero mode with
e-folding time of order a light-crossing time. Taking `τ_efold ≈ R/c` and `τ_burn = cΔη/a`, the
burn-outruns-instability criterion reduces to

> **Δη ≤ aR/c² = λ ≤ g(x)**

Le's own worked burn (Δη = 0.24, λ_max = 0.12) misses this by a factor 2 — consistent with his
statement that the safe corner is "restricted". A **habitable** design misses it by rather more:

| design | shortfall | verdict |
|---|---|---|
| Le App. K worked burn | 2.0 | fails |
| 1 g, 1 km cavity | 1.8×10¹² | fails |
| 1 g, 10 m cavity | **1.8×10¹⁴** | fails |
| 10⁶ g, 10 m cavity | 1.8×10⁸ | fails |

To pass at 1 g with Δη = 0.2 the cavity must be 1.83×10¹⁵ m — **12,253 AU, a fifth of a light-year**
across. At R = 10 m the ship must pull 1.83×10¹⁴ g. `τ_efold ≈ R/c` is Le's order of magnitude and
not a coefficient, but a fourteen-order shortfall is not an O(1) problem. The escape he names is a
slightly stiffer wall, strictly stable at no cost in dominant-energy margin — and he is explicit
that it is "a nearby model, not the realized one."

**The dispute is recorded and not adjudicated.** BBV catalogue 37 errors across the physical-warp-
drive literature and are severe about Lentz, Bobrick–Martire, Fell–Heisenberg and Fuchs et al.;
their hypotheses are the metric-first, prescribed-shift class. Le's construction is worldtube-first
and built explicitly to answer their covariance and interpretable-matter demands. What is executable
in `warpshell.py` is the arithmetic of the budget and the windows, not the standing of the
construction. Worth noting since this project cites SSV as a closure: BBV report minor errors in
Santiago–Schuster–Visser itself, at their Errors 9 and 29.

### Where the three directives now stand

`index3.py` holds **96 findings** over 14 distinct cells, `E(X) = 0` still, and the new cells changed
no coordinate that was already occupied. `NO-EXOTIC` is the ninth cell affirmative on all three axes
and the first that carries no negative energy at any point. `ONE-AXIS-FLAT` is `(−1,−1,−1)`, joining
`EM-GAP` at the bottom of the lattice.

> **Directive Y has an affirmative answer with a real spec.** An accelerating, positive-energy,
> dominant-energy-admissible warp drive exists as an exact solution of general relativity. It is
> subluminal, it is a rocket, it costs the cube of an ideal photon rocket's mass ratio, and what it
> buys is an exactly tidally flat cabin. Its open problem is marginal linear stability of the
> realized wall — which, on the light-crossing criterion, excludes the habitable regime by fourteen
> orders of magnitude. That is the wall now, and it is a stability problem, not an energy problem.

## Stability was structural, so the fix was — and then the method equation was asked what it is for

### `wall.py` — how much stiffer, and is that matter causal

Le's own escape clause is one sentence: *"A slightly stiffer, still-admissible wall is strictly
stable at no cost in the surface dec margin, which is junction-fixed and independent of the
equation-of-state slope, so strict stability and strict dominant energy decouple."* He does not price
it. `wall.py` does, from the Poisson–Visser thin-shell linearisation built from scratch — Minkowski
inside, Schwarzschild outside, Lanczos junction, `V(R) = 1 − [m_s/2R + m/m_s]²`.

The derivation validates before it concludes: the static surface stress it returns reproduces **Le's
Eq (17)** — `8πR(σ₀−p₀) = −(5s−1)(s−1)/(2s)` — at five values of x, with the surface-DEC root landing
on **24/25 to 9×10⁻¹⁶**. Then, with `β² = dp/dσ` the surface equation-of-state slope:

> **strictly stable ⟺ β² > β²_crit(x) = (1−s)(3s²+2s+1) / (4s²(1+3s))**, `s = √(1−x)`

exactly the zero of `V″(R₀)`. It is cheap, and two values are exact closed forms:

| x = 2m/R | β²_crit | c_s | which limit |
|---|---|---|---|
| 0.3 | 0.079332 | 0.282 c | Le's operating point |
| 2/3 | **(√3−1)/2** = 0.366025 | 0.605 c | Einstein–Vlasov |
| 4/5 | **√5 − 3/2** = 0.736068 | 0.858 c | the wall's own limit |
| 0.843742 | 1 | c | causal ceiling, root of `15s³+3s²−s−1` |

**The entire operative window `x < 4/5` lies below the causal ceiling.** Strict stability is available
everywhere the wall is realizable, with subluminal sound. And the decoupling is not taken on faith:
`σ₀` and `p₀` come out of the junction as functions of `(s, R)` alone — `β²` does not appear until the
second derivative — so `V(R₀) = 0` and `V′(R₀) = 0` hold identically in `β²`, checked at four values.

**Then the constraint inverts.** A marginal wall runs away, so the burn must *beat* it. A stable wall
oscillates at `ω = √(V″/2)`, so the burn must merely not *resonate* with it — and the period is
checked by integrating `R̈ = −V′/2` directly and timing it, matching `2π/√(V″/2)` to 2×10⁻⁵.

| design | marginal wall (needs ≤ 1) | stiff wall (needs ≫ 1) |
|---|---|---|
| Le App. K worked burn | fails by 2.0 | adiabatic by only 2.4 |
| 1 g, 1 km cavity | fails by 1.8×10¹² | adiabatic by 2.2×10¹² |
| **1 g, 10 m cavity** | **fails by 1.8×10¹⁴** | **adiabatic by 2.2×10¹⁴** |

The same ratio, times `W`, on the other side. The habitable regime was never near the boundary — it
was fourteen orders from it, and which side depends entirely on the sign of `V″`. The corollary is
the sanity check: the relativistic corner a marginal wall handles best is the one a stiff wall
handles worst. It also lines up with Le's Prop. 6, which proves the time-evolved assembly for **slow**
fixed-axis burns — the stiff wall and the dynamical existence proof want the same regime.

**A bonus theorem, and it is the opposite of what I went looking for.** Since
`d(σ−p)/dR = (1−β²)σ′ < 0`, the margin falls as the shell expands, so I expected a finite amplitude
at which a swinging shell breaks dominant energy. There is none:

> **β²_crit − p₀/σ₀ = x / (4s²(1+3s)) > 0** exactly, for every `x ∈ (0,1)`, checked to 10⁻¹³.

Any strictly stable wall automatically sits above `p₀/σ₀`, which is precisely the threshold for the
DEC basin to be unbounded. **Stability does not merely cost nothing in dominant energy; it buys it.**

Still open, and stated as such: exhibiting admissible matter (Vlasov below 2/3, anisotropic elastic
on 2/3–4/5) that actually realizes `β² ≥ β²_crit`; and the flux-coupled dynamic stability of the
*radiating* shell, which Le leaves open. What is closed here is the frozen-background linear radial
mode — the one he identifies as marginal, and no more.

### `pathmetric.py` — the method equation, run on spacetime

The equation has two halves and the corpus names both: structurally `E(X) = |ℛ(X)| − |X|`, metrically
`E_W(X) = |W(X)| − |X|` with `W` the least-cost reachable set under a step set — prior art **Dijkstra
1959, Freuder 1978**. `M` states the job outright: *"the Method equation partitions an index into
three populations: interior captures, the working overlap, and exterior predictions."*

**And the corpus also names which half spacetime gets.** §12.11.1.3: *an index has a time column
exactly when its cells are moves.* Events are configurations, so the time column goes and — the
corpus's own words — *"the flow becomes the geodesic flow of the Jacobi–Maupertuis metric. Time
returns as a quadrature carrying the transcendental part."* §12.11.4's *"precision is path-dependent;
physics is not"* is named there as the geodesic equation itself. So "spacetime is an index" is not an
analogy to argue; it is a selector the corpus already applies. Which makes the first job checking the
tool, not using it.

**It checks out exactly.** For static `ds² = −V²dt² + g_ij dx^i dx^j` the Jacobi metric is
`J_ij = (E² − m²V²)/V² · g_ij`, and its orbit equation reproduces Schwarzschild's at 3,000 random
`(r, E, L)` to **1.6×10⁻¹⁵** against the natural scale, with the Jacobi conserved quantity equal to
`L` exactly. Its two degeneracies are surfaces physics already knows — `V = E/m`, the turning point,
which for the three-body index is **Hill's 1878 zero-velocity surface where the corpus says the
geodesic flow stops**; and `V = 0`, where the massless (optical) metric `E²g/V²` blows up.

> **The horizon this project kept hitting is the zero-velocity surface of the method equation's own
> metric half.** Not a warp pathology — a Jacobi degeneracy, classical since Hill.

**And then it measures the shift, and the answer is negative.** `twist.py` proved the 1+1D warp metric
is static, so the metric half applies directly. Light in the original Painlevé–Gullstrand time obeys
`dt = dx/(c+v)` forward and `dx/(c−v)` back:

| measure | with shift | flat | |
|---|---|---|---|
| forward one-way | 5.205581 | 6.000000 | **shorter by 13.2%** |
| backward one-way | 8.660476 | 6.000000 | longer |
| **round trip** | **13.866057** | **12.000000** | **LONGER by 15.6%** |

and the round trip equals the optical length `∫2c dx/(c²−v²)` to 10⁻⁶. The excess is a strict
pointwise inequality with a closed form:

> **2c/(c²−v²) − 2/c = 2v²/(c(c²−v²)) > 0** for every `v ≠ 0`

So on the gauge-invariant measure — the only one the metric half offers — **any 1+1D shift makes the
path strictly longer**, and the one-way saving is exactly the simultaneity convention `twist.py`
already showed to be a global gauge choice. Three instruments now say the same thing about 1+1D by
three unrelated routes: the shift is gauge, it carries no twist, and it costs distance. In 3+1D the
metric is not static, so there is no global `T`, no optical metric of this form, and no round-trip
theorem — the third time the same dimensional boundary has decided a question in this series.

**A fault in the corpus, recorded and not repaired.** Checking the lattice half against its own
statement turned one up. `M`'s "The lattice metric" (proved M §9.2; Monjardet 1981) defines
`d(x,y) = Π(|xᵢ−yᵢ|+1)` and writes: *"Equality holds on an axis iff st = 0, i.e. y lies between x and
z there, so global equality iff y ∈ [x∧z, x∨z] — y on a geodesic."* The first clause is right and the
gloss after *"i.e."* is strictly weaker. Per-axis equality needs `|a−c| = st+s+t`, and `|a−c| ≤ s+t`
always, so it forces `st = 0` — `yᵢ` **equals** `xᵢ` or `zᵢ`, not merely lies between. One dimension
suffices: `x=0, y=1, z=2` has `y` between, and `d(x,z) = 3` against `d(x,y)d(y,z) = 4`.

> **The geodesic set is the vertex set of the box spanned by x and z, not the interval.**

On Λ's eight axes, two cells three apart on each have an interval of 65,536 cells and a geodesic set
of 256 — and 6,561× at five apart. The corpus's own check could not have caught it: it reports *"4,000
of 4,000 sampled triples satisfy the **inequality**"*, and the inequality is not in question — zero
violations here too, over all 2,744 triples of `index3`'s cells and 4,000 random 8-tuples. Nothing
sampled the equality condition. No member is edited.

The reason is worth stating because it bears on the question asked. `log(|Δ|+1)` is **strictly
concave**, so the metric rewards one long step and penalises subdivision: an index of this kind is
**not a length space**, and its first step costs `log 2` however fine you try to make it. A continuum
has no such quantum — which is exactly why §12.11.1.3 routes spacetime to the other half.

## Not dissolved — and the audit nearly closed the warpshell

"The obstructions have moved" is not "the obstructions have dissolved", and a build planned on the
first sentence while believing the second fails on the back end. `obstruct.py` is the ledger, with
every row recomputed from its owning instrument rather than transcribed, so a status cannot go stale
when the instrument beneath it moves. Of eleven obstructions:

| status | n | which |
|---|---|---|
| **DISSOLVED** | 2 | HORIZON-REQUIRED, EXOTIC-MATTER |
| **RELOCATED** — still true, renamed | 3 | CM-THEOREM, ENERGY, FELT-ACCEL |
| **CLOSED-NEGATIVE** | 3 | ANALOGUE-1D, SHIFT-SHORTENS, SELF-SOURCED |
| **CONDITIONAL** | 2 | WALL-STABILITY, NONRADIAL |
| **UNTESTED** | 1 | MAPPING-2D |

Only two dissolved, and one of those (exotic matter) by leaving the architecture SSV quantify over
rather than by beating them. The rest became bills or conditions — which is progress of a different
kind, and worth naming as such.

### β² was never a knob

`wall.py`'s first pass treated the equation-of-state slope as a design choice. **It is not.** For a
counter-rotating (Einstein–Vlasov) shell the junction already fixes `p₀/σ₀ = v²/2`, so `v² = (1−s)/(2s)`
is set by `x` alone; with each particle conserving angular momentum under a radial perturbation,
`u = γv ∼ 1/R` and the *supplied* stiffness is

> **β²_vlasov(x) = u²(3u²+4) / (2(1+u²)(3u²+2))**

| x | supplied | required | |
|---|---|---|---|
| → 0 | | | ratio → **exactly 4/3** |
| 0.3 | 0.090800 | 0.079332 | stable by 14% — Le's own point |
| 0.4 | 0.130697 | 0.122892 | stable by 6% |
| **0.46898** | | | **crossover** |
| 2/3 | 0.281089 | 0.366025 | unstable |
| 4/5 | 0.399187 | 0.736068 | unstable, badly |

Good news exactly where it is needed and bad news in the high-compactness corner — the corner a
*marginal* wall handled best. The earlier framing was wrong and is recorded that way round.

**And the radial criterion is confirmed independently.** Converted to Pitre–Schneider–Poisson's
adiabatic index via `Γ = β²(μ+p)/p`, this tree's `β²_crit` reproduces LeMaitre–Poisson's published
`Γ₁ = (4−6C+2√(1−2C))/(4(1−2C))` **to 10⁻¹⁵ at every x from 10⁻⁶ to 0.8**, both tending to 3/2 in the
Newtonian limit. Independent derivation, same answer.

### The row I flagged as untested, tested — and it nearly ended it

`obstruct.py` named NONRADIAL as the row most likely to break the next build: Poisson–Visser is a
*radial* linearisation and `wall.py` was nothing but. It breaks.

**Pitre, Schneider & Poisson, [arXiv:2604.05980](https://arxiv.org/abs/2604.05980), Phys. Rev. D** —
*"Self-gravitating thin shells are dynamically unstable on all angular scales."* A static thin shell,
Minkowski inside, Schwarzschild outside — **Le's static anchor exactly** — carries an even-parity
matter mode with purely imaginary positive frequency **for all ℓ ≥ 2, all compactness, and all
adiabatic index**, surviving even the Newtonian limit.

> **β² does not appear in the unstable branch. Stiffening the wall fixes the radial mode and does
> nothing to ℓ ≥ 2.**

What saves it is that the growth rate is *self-gravitational*. Their Fig. 1 gives
`Im{ω}(R³/M)^{1/2} ≈ 0.6`, roughly flat in both `M/R` and `Γ`, so `ω ≈ 0.6√(GM/R³)` — and a diffuse
shell grows slowly. Against a burn of duration `cΔη/a`, the e-folding count `N = 0.6√(GM/R³)·cΔη/a`
turns out to be a ceiling on **mean density alone**:

> **ρ̄ < 3a² / (4πG(0.6cΔη)²) = 2.658×10⁻⁴ kg/m³** for a 1 g burn to Δη = 0.2

| design | e-foldings during the burn | |
|---|---|---|
| 1,000 t at R = 10 m | 948 | torn apart hundreds of times over |
| 1,000 t at R = 965 m | 1.0 | marginal |
| 1,000 t at R = 4.48 km | 0.1 | **survives** |

About 1/4000 of air density. At R = 4.48 km the compactness is `x ≈ 3×10⁻²⁵`, so every dominant-energy
window clears by decades, the counter-rotating wall is stable, and the burn is adiabatic by twelve
orders. **There is a corner, and its shape is big and diffuse.** A thousand-tonne, nine-kilometre-wide
structure is a strange spacecraft, but it is a spacecraft.

Two escapes from the theorem itself are open and neither is claimed: Pitre *et al.* assume **vacuum**
on both sides where Le's exterior is outgoing null dust, and they treat an **infinitesimally thin**
shell where Le's realized wall has finite thickness — their own conclusion is phrased about objects
*"that feature a thin shell at its surface"*.

> The count moved while the ledger was being written, and in the worst direction before it recovered:
> NONRADIAL went from untested, to nearly fatal, to conditional, in one search. That is the argument
> for keeping the ledger.

**One row remains genuinely untested, and it is the analogue's.** `MAPPING-2D`: `twist.py` showed an
analogue must be at least 2+1D, Smolyaninov derives only 1+1D, and the Brown–Hornreich–Shtrikman
bound the whole design rests on constrains *one* magnetoelectric component where a transversely graded
medium has more. It may tighten, loosen, or not apply. **ANALOGUE-2D is not a design awaiting
fabrication; it is a derivation awaiting a derivation.**

## The hardware is a materials question, and the corpus has a spectral index to screen against

`device.py`'s ferrite figure of merit is `Ms/((ε_r−1)ΔH)`, and two of those three are atomic-spectra
quantities before they are engineering ones. `Ms` is set by the magnetic ion's spin. `ΔH` — the FMR
linewidth — is set by spin–lattice relaxation, which needs spin–orbit coupling to connect the spin to
the lattice at all. So the screen writes itself:

> **Maximise S. And kill L, because first-order spin–orbit dies with it.**

That is a query on the ground *term*, which is exactly what `LW1-ground.py` holds — register 1306,
NIST ASD 5.12, `READ` not computed, imported by path and never transcribed.

### The screen, validated before it is used

Hund's rules are checked against the seated terms first. Of the 108 neutrals, 78 have exactly one open
shell, and the rules reproduce the observed NIST term symbol for **74**. The four that differ are not
disagreements — NIST writes Pb in *jj*-coupling as `(1/2,1/2)₀` and gives Sg, Bh and Hs by J alone,
and Hund returns J = 0, 0, 5/2, 4 for those four, matching every one. **Agreement on J is 78 of 78.**

Run over every open shell in the table, exactly four are S-states, and that is the complete list for
every element there is:

| shell | S | term | |
|---|---|---|---|
| s¹ | 1/2 | ²S₁/₂ | |
| p³ | 3/2 | ⁴S₃/₂ | |
| **d⁵** | **5/2** | ⁶S₅/₂ | **YIG's Fe³⁺** |
| **f⁷** | **7/2** | ⁸S₇/₂ | **Eu²⁺, Gd³⁺ — the only way up** |

> **The incumbent is optimal in its shell and there is exactly one way past it.** Fe³⁺ is the d-shell
> S-state, which is why YIG has the narrowest linewidth of any magnetic material and why sixty years
> of microwave engineering never left it. The only ions with more spin *and* no orbital moment are the
> f⁷ pair, at S = 7/2 — beating d⁵ by exactly 7/5. Nothing else exists.

### What the screen then found in `device.py`

Serha, Dubs & Chumak, *Magnetic Materials for Quantum Magnonics*
([arXiv:2510.09331](https://arxiv.org/abs/2510.09331)), Table II gives bulk YIG at 8 GHz:
`Ms @ RT | →0 K = 140 | 200 kA/m` and `ΔB @ RT | →0 K = 0.03 | 0.02 mT`.

**`device.py` carried the room-temperature Ms (0.175 T ↔ 140 kA/m) beside the cryogenic linewidth.**
The device runs in a dilution refrigerator — its own analogue Hawking temperature is 4.96 mK — so both
must be the cold values. Corrected and propagated:

| | was | now | |
|---|---|---|---|
| ferrite figure of merit | 625.0 | **897.6** | +42.9% |
| ferrite loss tangent | 0.003163 | **0.002203** | −30.4% |
| detuning | 319.5 | **461.1** linewidths | further from resonance |
| operating point | 8.221 GHz | 8.142 GHz | cell 1.633 → 1.649 mm |

Twenty-eight of `device.py`'s pinned fixtures moved with it. **β, ε, g_x and the fill did not** —
those are set by the Smolyaninov mapping and the stability bound rather than by the material, which is
exactly the right thing to have been invariant. A mismatched pair of table lookups, worth nearly half
the ferrite.

### And a design decision that was right for a reason it never gave

The same table shows the failure mode that dominates thin-film magnonics at millikelvin, and it is not
the ferrite. GGG is paramagnetic; it orders at low temperature and couples to the YIG spin system:

| | ΔB → 0 K | cost vs bulk sphere |
|---|---|---|
| bulk YIG sphere | 0.02 mT | — |
| YIG on GGG | 0.85 mT | 41.5× |
| YIG on YSGG | 0.75 mT | **78.9×** |
| YIG on YSGAG | 0.25 mT | 13.6× |

`device.py` specifies a YIG *sphere*, so it sits on the top row and the problem never arises — but it
never said that was why. **And the middle rows carry a trap**: YSGG has the better linewidth of the two
and the worse figure of merit, because the merit divides by ΔH and multiplies by Ms, and YSGG's Ms is
95 kA/m against GGG's 205. *A linewidth table alone would have picked the wrong substrate.*

### The prize behind f⁷, priced and not claimed

EuO is the f⁷ material: Eu²⁺, 4f⁷, ⁸S₇/₂, `Ms ≈ 1900 kA/m` — **9.5× YIG's cold value** — with
`T_c = 69 K`, which is irrelevant to a device already at millikelvin. If its linewidth could be brought
to YIG's, the figure of merit would be 5214 against 897.6:

> **a ceiling of 5.8×, and it is a crystal-growth problem rather than a physics one.**

It cannot be reached today and this is not claimed. YIG's 0.02 mT is sixty years of crystal growth, not
a property of Fe³⁺; the europium-chalcogenide FMR literature is Dillon & Olsen 1964 and Eastman 1968;
and the 2026 review that supplies every number above surveys europium chalcogenides and still puts only
YIG in its benchmark table. Worse, the classic result that **rare-earth impurities broaden YIG's line**
(Dillon & Nielsen 1959; Spencer, LeCraw & Clogston 1959) is a warning aimed squarely at this idea —
though Gd³⁺ and Eu²⁺ are the exception that proves it, being the only rare earths with L = 0.

That is a genuine engineering finding of a kind this project has not had before: **a target with a
number on it and a named discipline that owns it.**

## `plebanski.py` — the last untested row, and the mapping was never the problem

`obstruct.py` had one row left as UNTESTED: `MAPPING-2D`, described as "a derivation awaiting a
derivation" on the grounds that `twist.py` requires ≥2+1D, Smolyaninov derives only 1+1D, and no 2+1D
version is published. **That framing was wrong in a useful way.** The general mapping has existed
since 1960 — Plebanski's constitutive relations, the foundation of transformation optics:

> **ε^ij = μ^ij = −√(−g) g^ij / g₀₀   ·   w_i = −g₀ᵢ / g₀₀**

with `D = εE + w×H`, `B = μH − w×E`. Any metric is a medium, in full 3+1D. Applied to Alcubierre and
computed from the numerical inverse and determinant rather than by hand:

> **ε_xx = 1 exactly · ε_yy = ε_zz = 1/(1−v²) · w_x = −v/(1−v²)**

**The medium is anisotropic wherever the shift is nonzero.** That is precisely the transverse
structure `twist.py` said a 2+1D analogue must carry — present by construction in the honest mapping,
and absent from Smolyaninov's isotropic `ε = μ`. So the 1+1D reduction is the thing that needed
arguing for, not the 3+1D version.

### And Brown–Hornreich–Shtrikman forbids it, except beyond the horizon

`w` lies along x, so it couples (E_y, H_z) and (E_z, H_y), and the anisotropic BHS condition is
`w_x² ≤ (ε_yy−1)(μ_zz−1)`. Substituting the exact values:

> `w² = v²/(1−v²)²` against a bound of `v⁴/(1−v²)²` — admissible iff **v² ≤ v⁴, i.e. |v| ≥ c**

| v | w² | bound | |
|---|---|---|---|
| 0.10 | 0.0102 | 0.000102 | FORBIDDEN |
| 0.50 | 0.4444 | 0.1111 | FORBIDDEN |
| 0.99 | 2474.9 | 2425.7 | FORBIDDEN |
| 1.50 | 1.44 | 3.24 | admissible |

**The exact 3+1D Alcubierre medium is thermodynamically forbidden everywhere it is subluminal, and
admissible only at or beyond the horizon** — the exact inverse of the 1+1D case, where `device.py`'s
TEST 16 found stability capping v *below* the horizon. Both routes are closed, for opposite reasons:

| | what BHS allows | what the metric holds |
|---|---|---|
| **1+1D** | v < c(n−1)/n², horizon forbidden | pure gauge — nothing to emulate |
| **3+1D** | only \|v\| ≥ c, the unsteerable regime | real content, medium forbidden |

**The obvious escape is closed too.** A conformal rescaling `g → Ω²g` leaves null geodesics alone, so
it is where one looks for headroom. It gives none: ε and w are **conformally invariant**, verified at
Ω = 0.5, 1, 2, 7.3, 100 to twelve digits, because the `Ω⁴` from `√(−g)` and the `Ω⁻²` from `g^ij`
cancel the `Ω²` from `g₀₀`. `ε_xx = 1` is not a choice of units; it is the mapping's answer.

### So where does Smolyaninov's admissible medium come from?

Not from this mapping. Run Plebanski on his own 1+1D metric and it returns `ε = 1`, `w = −v/(1−v²)`,
BHS-forbidden exactly as above — **not** his `ε = μ = n/√(1−(nβf)²)`. The square root is the tell: his
medium emulates the metric whose light speed is `c/n` rather than `c`, and the background index is
where the `(ε−1)` headroom comes from. That is legitimate — an analogue may emulate a rescaled metric
— but it is a *substitution*, not the mapping, and it has never been shown to survive in 3+1D where ε
must also become anisotropic.

> `MAPPING-2D` is therefore no longer untested. It closed negative, and left behind a sharp question
> in place of a vague one: **does the index-n embedding that rescues 1+1D also rescue the anisotropic
> 3+1D medium, given that the exact mapping is forbidden at every subluminal v and conformal freedom
> buys nothing?**

**The ledger now has no UNTESTED row.** Of eleven obstructions: two dissolved, three relocated, **four
closed negative**, two conditional, none unexamined. That is not the same as everything being open —
it means nothing is left where a build could be surprised from behind.

## `dispersive.py` — the exemption, tested, and it was the wrong exemption

The question was whether **gain** lifts Brown–Hornreich–Shtrikman, since BHS assumes passivity. The
answer is that **passivity was never the problem. Staticity was.**

BHS 1968 bounds the *equilibrium* magnetoelectric susceptibility by requiring the free energy
`F = ½(εE² + μH²) + αEH` to be positive definite. That is a thermodynamic statement about a **static**
response. `neclab.py`, `device.py` and `plebanski.py` all apply it at a working frequency to a
magnetised ferrite, which is dispersive — and it is the wrong bound there.

### It is demonstrably the wrong bound, and the refutation is a catalogue

A magnetised ferrite has the Polder response `μ−1 = ω_mω₀/(ω₀²−ω²)`, `κ = ω_mω/(ω₀²−ω²)`. **Above
resonance, |κ| > |μ−1|** — violating BHS by factors of 1.0005, 1.2, 2.0 and 5.0 at ω/ω₀ = 1.001, 1.2,
2, 5. Above-resonance ferrites are ordinary, stable, passive components sold by the reel. The static
bound forbids a regime that exists.

### What replaces it is satisfied identically

At a working frequency the positivity that matters is of the **Brillouin stored energy**, which carries
`d(ωε)/dω` rather than `ε` (Landau & Lifshitz §80). Generalised to the bianisotropic case — marked
`RECONSTRUCTED`, since BHS's own derivation is static:

> `|d(ωα)/dω|² ≤ (d(ωε)/dω − 1)(d(ωμ)/dω − 1)`

For Polder both sides are closed-form and checked against finite differences at six frequencies:
`d(ωμ)/dω − 1 = ω_mω₀(ω₀²+ω²)/D²` and `d(ωκ)/dω = 2ωω_mω₀²/D²`, whose ratio is

> **2ωω₀/(ω₀²+ω²) ≤ 1 ⟺ 0 ≤ (ω₀−ω)²**

**True at every frequency, with equality exactly at resonance.** The dispersive condition is never
violated by a real ferrite and saturates only where the medium is lossy anyway. The static one is
violated by half the spectrum.

### What that costs this project's two closures

Both rested on the static bound: `neclab`'s **c/4 ceiling** (β ≤ 0.245826 at n = 2), and
`plebanski`'s **3+1D subluminal prohibition** (`v² ≤ v⁴`, which was the whole of `MAPPING-2D`'s
negative closure). Priced against `device.py`'s own ferrite at the corrected cold magnetization:

| | β | g_x bulk | detuning | ferrite loss |
|---|---|---|---|---|
| current design | 0.2224 | 13.84 | 461 lw | 0.00220 |
| n = 2.0, 99% of horizon | 0.4950 | 99.50 | 126 lw | 0.01584 |
| **n = 1.2, 99% of horizon** | **0.8250** | 59.70 | 211 lw | **0.00950** |

> **A factor 3.7 in β for a factor 4.3 in ferrite loss — and the loss is still under one per cent.**
> The c/4 ceiling was not a material limit. It was a static bound applied to a dispersive device.

### What does *not* reopen, and this matters more than what does

**`twist.py` is untouched.** In 1+1D the shift is pure gauge, `E = −Ω²/(8πG)` vanishes on the axis, and
the emulated geometry is Minkowski **at any β**. A faster 1+1D analogue emulates flat spacetime faster.
`ANALOGUE-1D` stays CLOSED-NEGATIVE and nothing here revives it.

What reopens is the **3+1D route** — exactly where `twist.py` said the content is. `plebanski.py`'s
mapping stands (it is Plebanski 1960, not a bound) and its anisotropy stands; only its BHS verdict
falls. `MAPPING-2D` moves UNTESTED → CLOSED-NEGATIVE → **DISSOLVED**, and `ANALOGUE-2D` is upgraded on
the architecture sheet with a mapping and a ceiling instead of an aspiration.

**And the gain question is moot.** Gain would exempt the medium from a bound that does not apply to it,
at the cost of noise and of converting a thermodynamic condition into a dynamical one — the trade
`wall.py` already made twice. Passive dispersion is free and sufficient.

### The shape worth noticing

Both live routes were closed by a **static positivity condition**, and both loosen when the dynamics is
put in. The warpshell: the centre-of-mass theorem forbids self-acceleration for an *isolated* system,
and the escape is to radiate. The analogue: BHS forbids the coupling for an *equilibrium* medium, and
the escape is to disperse. Same shape, different physics — **and neither one is a material.**

## `shape.py` — the pattern as an instrument, and the honest accounting of it

A shape is cheaper than a material: it is a property of the mathematics, so it can be checked against
every closure at once without buying anything. Two closures fell to the same move, and the move was not
a material — the centre-of-mass theorem forbids self-acceleration for an **isolated** system and the
escape is to radiate; BHS forbids the coupling for an **equilibrium** medium and the escape is to
disperse. Same shape:

> **A no-go built on a static positivity condition loosens when the dynamics is put back in.** The
> static form is a special case, and a project that measures the special case reports a bound the
> general case does not have.

### The caveat comes first, because it is the whole point

The pattern was **induced from the cases that moved**. So the four hits are not evidence for it — they
are the sample it was fitted to, and quoting them as confirmation is the error of fitting a curve and
then citing the points. `evidence_available()` returns **0**, deliberately. The only evidence a shape
like this can earn is a prediction that lands, and the predictions are written down so a later pass
cannot re-derive one and quietly count it as a hit.

### The domain is narrower than "every closure", and there are controls

The shape applies only to no-goes whose content is a **positivity or conservation condition**. Three
closures are carried as controls, and the file checks that the shape does *not* claim them:

| control | how it closed | should it move? |
|---|---|---|
| KAPPA | **measured** — MICROSCOPE, Cassini, PSR J0337, Eöt-Wash | no — the experiments were done |
| SWIMMER | **kinematic** — Δs ≤ A·a_tide/c² | no — c² is a constant of nature |
| HORIZON | **geometric** — f* = 1 − c/v_s ∈ [0,1) iff v_s ≥ c | already gone, and not by this route |

`predicts_a_control()` returns `[]`. A pattern that predicted those would be wrong.

### The fitted sample (four), and the predictions (three)

| | static form | dynamical counterpart | |
|---|---|---|---|
| CM-THEOREM | isolated | Bondi flux balance at null infinity | MOVED |
| ADM | static slice, spatial infinity | Bondi four-momentum | MOVED |
| BHS | equilibrium free energy | Brillouin `d(ωε)/dω` | MOVED |
| SSV | pointwise NEC, vacuum exterior | non-vacuum exterior | MOVED |
| **GATE-CLOSED** | pointwise, 165/165 + 210/210 + 154/154 | ANEC/AWEC, and the untaken `I_V` | **PREDICTED** |
| **NEC-LADDER** | pointwise NEC | QNEC, `⟨T_kk⟩ ≥ (ℏ/2π)S″_out` | **PREDICTED** |
| **WALL-RADIAL** | frozen-background linearisation | flux-coupled radiating shell | **PREDICTED** |

**Prediction 2 has a standing decision against it, and that is the finding rather than an oversight.**
The corpus records QNEC in Appendix D5 and *deliberately* does not make it a letter of the violation
index. The shape says ask; the corpus has already answered "not as a letter". Those are compatible — a
measurement is not a letter — and the tension is recorded here rather than resolved.

### The index refused a row, correctly

`NO-EVIDENCE` — the statement that the shape has earned nothing yet — was first seated as a finding at
`(0,0,0)`. `index3.py` rejected it: distinct cells went 14 → 15, and the null cell is declared **not a
finding**, being the lattice bottom. It answers no directive, so it belongs in SUPPORT. The index
caught a bookkeeping error about the epistemics of its own newest instrument, which is the closest
thing to a self-test this tree has.

## The shape has mass — and that withdraws the corner

The shape as first written was incomplete. *"Static positivity loosens under dynamics"* is a statement
about the **form** of a bound and says nothing about the object the bound is on. But the object has
mass, its mass gravitates, and relaxing a bound by changing the object can change what the object **is**.

That had already happened here, unnoticed, in this session's own work.

### The corner, withdrawn

`wall.py` escaped the ℓ ≥ 2 shell instability by reading its constraint as a ceiling on **mean density**
and going "big and diffuse". That reading treats M and R as independent. They are not — the same mass
sets the density *and* the compactness:

> `x = 2GM/(Rc²)` and `ρ̄ = M/((4/3)πR³)` ⟹ **`x = (8πG/3)ρ̄R²/c²`**

so holding ρ̄ at the ceiling makes self-gravity a function of radius alone. Tabulated:

| x = 2m/R | R (m) | M (M☉) | binding fraction |
|---|---|---|---|
| 10⁻²⁴ | 7.8×10² | 2.6×10⁻²⁵ | 0 |
| 10⁻⁶ | 7.8×10¹¹ | 2.6×10² | 5×10⁻⁷ |
| **0.0396** | 1.5×10¹⁴ | **2.1×10⁹** | **0.01** |
| 0.3 (Le's point) | 4.3×10¹⁴ | 4.3×10¹⁰ | 0.082 |

> **To be both stable against ℓ ≥ 2 and meaningfully self-gravitating — a one per cent binding
> fraction — the object must be two billion solar masses spread over a thousand AU.**

And the 1,000-tonne, 4.48 km design that passed the density ceiling sits at **x = 3.3×10⁻²⁵**, binding
fraction 8×10⁻²⁶, with a wall of **3.97 g/m²** — *half the areal density of kitchen foil* — under
1.5×10⁻¹¹ N/m of tension. It is a Mylar balloon nine kilometres across. Its cavity is exactly flat, but
**a spherical shell's interior is exactly flat by Birkhoff at any compactness whatever**, so that
property is shared with every balloon and is not a warp feature.

> **The escape corridor exits the category.** Le's own line is that *"a sufficiently idealized hulled
> rocket … lies outside the exact class W"*, and the diffuse limit walks the warpshell straight into it.
> The ℓ ≥ 2 instability is not escapable while the object remains self-gravitating — which is what
> "warpshell" means.

The arithmetic of the density ceiling stands. What is withdrawn is the reading that a habitable design
survives it. It survives as a balloon.

### The shape gains a second clause

> **A bound relaxed by changing the object must be checked against what the object was for. An escape
> that exits the category is not an escape.**

`shape.py` now carries `EXITED` as a fourth state and `category_preserved()` as the test. The four
fitted cases pass it — radiating does not stop a warpshell being a warpshell, dispersing does not stop
a ferrite being a ferrite — but `WALL-NONRADIAL` fails, and it was this session's own claim.

That is the first thing the shape has actually caught rather than been fitted to: not a prediction
landing, but a false escape found. `index3.py` regrades `DENSITY-CEILING` from (0,+1,+1) to (0,−1,+1)
and seats `CORNER-EXITS` at (−1,−1,−1) beside `EM-GAP` and `ONE-AXIS-FLAT`.

## `bench.py` — the one thing here that goes on a table

Everything above is a closure or a bound. This is the piece someone could build.

### The problem it solves

`device.py` measured 2,146° of non-reciprocity and this project recorded it as `RELABEL-ONLY`:
enormous, real, and a property of the medium rather than of any metric. What was missing was an
observable that **cannot be relabelled**. There is one, and it is old:

> A stationary metric is **static** exactly when the clock-synchronisation gap around every closed loop
> vanishes. That gap is `∮w·dl` with `w_i = −g₀ᵢ/g₀₀` — Plebanski's magnetoelectric vector — and by
> Stokes it is nonzero iff `curl w` is, which is the twist.

**Measure the loop, not the line.** A one-way phase is a synchronisation convention. A closed-loop
phase is not, and no re-clocking removes it.

### The experiment: one rig, two samples

| sample | grading | predicted loop phase |
|---|---|---|
| **A (control)** | longitudinal only, `w = w_x(x)` | **exactly 0** |
| **B** | longitudinal **+ transverse** | `2k₀∮w·dl` |

The null is not a small number — it is a dimension theorem, and it holds at any β, any grading depth,
any frequency. A *uniform* w also gives zero, being curl-free, so a bulk offset in the sample cannot
fake the signal. **Two independent reasons for the null; one for the signal.**

### The signal budget, at the corrected operating point

8.1418 GHz, λ = 1.649 cm in medium, the same `2k₀` that gives device.py's 2,146° over 9.89 cm:

| loop side | transverse contrast | phase | vs a 1 mdeg VNA |
|---|---|---|---|
| 1 cm | 1.00 | 195.5° | 2.0×10⁵ |
| 1 cm | 0.01 | 2.0° | 2.0×10³ |
| 5 cm | 0.10 | 97.8° | 9.8×10⁴ |
| 9 cm | 0.01 | 17.6° | 1.8×10⁴ |

**It is not signal-limited.** Even one per cent of transverse contrast over a one-centimetre loop is
three orders above a commercial network analyser. The limit is whether the sample can be built with a
clean transverse grade, which is fabrication with a known answer. The rig is a dilution refrigerator
and a VNA — equipment that exists in a few hundred laboratories.

### What it would settle, and what it would not

It settles `ANALOGUE-2D`, the only route left open, by measuring the one thing that distinguishes it
from `ANALOGUE-1D`. A nonzero loop phase in B against a zero in A is the first laboratory demonstration
that an engineered medium carries an **irremovable** shift — the property `twist.py` identified as the
entire content of a warp metric, and the property no 1+1D analogue can have.

**It transports nothing. It violates no energy condition in real spacetime. It does not make a warp
drive nearer.** It measures, on a bench, the quantity thirty-seven instruments were needed to identify
as the only one that mattered.

And it tests three corrections to a published literature at once — a null in A confirms that
Smolyaninov-class 1+1D analogues emulate Minkowski; the operating point depends on the BHS bound being
static and therefore misapplied; and the sample is built from Plebanski's 3+1D mapping. All three are
cheap to check and all three are wrong in the literature as it stands.

> **That is the practical output of this project: one bench experiment, three corrections, and a
> catalogue of things not to spend money on.**

## `warpenergy.py` — DIRECTIVE 1, CLOSED

The first of the three things this project set out to do was **identify warp energy**. The answer was
produced in `twist.py` and not recognised as the answer, because it arrived as an identity about
vorticity rather than as a quantity. It is both.

### What it is

> **E = −Ω²/(8πG)**

The Eulerian energy density of an Alcubierre warp drive and the coordinate vorticity of its shift are
**the same object** — not proportional, equal, with Ω squared and a minus sign.

> **Warp energy is not a new kind of energy and it is not a property of any matter. It is the negative
> of the squared twist of the shift, fixed by geometry alone.**

Nothing about a material enters. Give the shape function and the velocity, and the energy is determined
exactly, before any question of what the drive is made of. That is why every *"which exotic matter"*
question in this literature is the wrong question: **the geometry has already spent the energy.**

### How much

With `(y²+z²)/r_s² = sin²θ` and `∫₀^π sin³θ dθ = 4/3`, the angular part collapses:

> **M_warp = −(v_s²/12G) ∫₀^∞ f′(r)² r² dr** kg, exact

checked against a direct three-dimensional integration of the density itself at three (R, σ) to
**5×10⁻¹²** relative. For a thin wall the radial integral → `R²σ/3` — confirmed to five figures at
σR = 20, 100, 400 — so with wall thickness D:

> **M_warp ≈ −v_s²R² / (36 G D)**

**The energy is a surface effect, not a volume one: area over thickness.** Doubling the bubble costs
four times; halving the wall costs twice. The wall is the whole bill, and R is not the lever.

| R | D | v_s/c | M_warp (kg) | M_warp (M☉) |
|---|---|---|---|---|
| 100 m | 1 m | 1 | −3.74×10²⁹ | −0.188 |
| 100 m | 1 mm | 1 | −3.74×10³² | −188 |
| 100 m | 10² ℓ_P | 1 | −2.31×10⁶² | −1.16×10³² |
| 100 m | ℓ_P | 1 | −2.31×10⁶⁴ | −1.16×10³⁴ |
| 100 m | 1 m | 0.1 | −3.74×10²⁷ | −0.0019 |

**The famous 10⁶²–10⁶⁵ kg is a statement about the wall, not about warp drives.** At a metre-thick wall
and a tenth of light speed the bill is a thousandth of a solar mass — still absurd, and **thirty-five
orders below the number usually quoted**. What drives it to 10⁶² is the Planck-scale wall that Pfenning
and Ford's quantum inequality demands.

### And that is where directive 1 hands off

D is set by a **quantum inequality**, and the state-dependent successor to quantum inequalities is the
**QNEC**, `⟨T_kk⟩ ≥ (ℏ/2π)S″_out`, which licenses negative energy wherever the outward entanglement
entropy is concave. That is exactly `shape.py`'s **prediction 2**, recorded before this file was
written. So directive 1's answer does not merely close directive 1 — it names which of the three
outstanding predictions is load-bearing, and it is the one the corpus has a standing decision about.

### Where the three directives now stand

| | axis | affirmative | bounded | verdict |
|---|---|---|---|---|
| **1** | identify warp energy | 44 | 4 | **MET** — closed form, verified, and it is geometric |
| **2** | can a warp drive be built | 33 | 53 | **not met** — the one positive-energy construction is ℓ≥2 unstable while self-gravitating |
| **3** | engineer the specs | 82 | 11 | **not met** — no surviving engine; a bench instrument, not a drive |

Directive 1 is met. Two remain, and directive 1's own answer says where to push: the wall thickness is
the entire cost, the wall thickness is fixed by a static quantum inequality, and that inequality has a
dynamical form nobody here has asked.

## `nullbound.py` — the reason warp drives are "impossible" is the wrong instrument

`warpenergy.py` closed directive 1 and handed off one sentence: the entire cost is the wall, and the
wall thickness is set by a quantum inequality. Pfenning and Ford's is the one everybody quotes, and it
bounds D at about 10² Planck lengths — which is what turns 0.19 solar masses into 10⁶² kg.

> **That bound comes from a *timelike* quantum inequality, and the quantity being bounded is *null*.**

### The corpus had already banked why that matters

Not this file's finding — the Register's, at **5537**, reached independently there:

> Fewster & Roman, Phys. Rev. D 67 (2003) 044003: for the massless minimally coupled scalar in
> **four-dimensional** Minkowski space, weighted averages of the null-contracted stress tensor along a
> null geodesic are **unbounded from below** on Hadamard states. **There are no quantum inequalities
> along null geodesics in 4D.** In two dimensions they exist.

Register 5541 then prices every finite replacement: Wall 2010 spends *completeness*, Kontou & Olum
spend *timelike smearing*, and the Smeared NEC of Freivogel & Krommydas spends a *UV cutoff*, making
the bound finite and explicitly computable. **The SNEC is the instrument this comparison needs.**

### And then the thickness cancels, exactly

Two 1/D² laws meet, and both also carry 1/G.

| | |
|---|---|
| **required** | `ρ = −v_s²/(144πG D²)` — R cancels, checked at R = 10, 100, 1000 m |
| **allowed** (SNEC) | `\|⟨T_kk⟩\| ≤ 2B/(G D²)` — Gaussian of width D gives `∫(g′)² = 1/(2D²)` |
| **ratio** | **`v_s²/(288πB) = v_s²/9`** at Freivogel–Krommydas's `B = 1/(32π)` |

**D² cancels. G cancels. What is left is a pure number in v_s.** Verified constant to twelve figures
across D from 1 mm to the Planck length — **thirty-two orders of magnitude, one ratio.**

| v_s | ratio | |
|---|---|---|
| 0.1 c | 0.0011 | admissible, **900× margin** |
| 1.0 c | 0.111 | admissible, 9× margin |
| 3.0 c | 1.000 | saturated |
| 4.0 c | 1.778 | forbidden |

> **The wall-thickness bound is an artefact of the timelike instrument.** On the null-smeared condition
> a metre-thick wall and a Planck-thick wall are equally admissible, and what is bounded is the
> **velocity**. Pfenning–Ford demand D ≲ 1.6×10⁻³³ m; a one-solar-mass budget at R = 100 m and 0.1 c
> wants D ≈ 1.9 mm — a gap of 1.2×10³⁰ that the null condition simply does not impose.

### Four O(1) exposures, all named, none of them structural

1. **E vs T_kk** — the required figure is the Eulerian density, the bound is on the null component. Both
   ∝ v_s²f′², so the 1/D² structure is untouched, but their ratio is an O(1) not computed here.
2. **B is not a theorem** — Freivogel & Krommydas argue B ≤ 1/(32π) holographically.
3. **The SNEC itself is a conjecture** with holographic support.
4. **The Gaussian** gives 1/(2D²); another sampling function gives another O(1).

So `v_s²/9` carries perhaps an order either way — and at 0.1 c there are nearly three orders of margin.
Even with B ten times smaller, saturation is still at 0.95 c. **The structural claim survives all four:
both sides go as 1/(GD²), so the thickness cancels whatever the O(1)s are, and a bound on D cannot be
what a null condition says.**

**This does not build a warp drive.** It removes the specific reason everybody gives for why one
cannot be built.

### shape.py scores it as a half, not a hit

`shape.py` predicted — before `nullbound.py` existed — that the energy-condition family was where a
static bound would loosen, and named QNEC as the counterpart. The move that landed is
**timelike-QI → null-SNEC**: same family, *different member*. SNEC is state-independent; QNEC is
state-dependent and **still unasked**. `evidence_available()` goes 0 → **0.5**, and the row is scored
`PARTIAL` rather than `MOVED` — because scoring it whole would be exactly the fitting error the file
exists to avoid.

## `designpoint.py` — spending the breakthrough, and `paper/CLAIMS.md`

`nullbound.py` removed the wall-thickness bound. This is what that buys.

### The design equation

`M = −v_s²R²/(36GD)` is exact, and with D free the only remaining ceiling is that the cavity must
actually be flat — a shape function needs σR ≳ 3, so D ≲ R/3. Substituting:

> **M = −β²c²R/(12G) = −1.1222×10²⁶ · β² · R kg**

**Linear in R, quadratic in β, and with no D in it at all.** The wall thickness enters through 1/D and
leaves through the flatness ceiling, and what survives is a one-line spec — the first `directive 3` has
ever had. The compactness at the floor is `x = β²/6`, so 0.0017 at a tenth of light speed: nowhere near
compact, and none of `wall.py`'s shell bounds bind on it.

| R | β | M | | x |
|---|---|---|---|---|
| 1 m | 0.01 | −1.12×10²² kg | ≈ Pluto | 0.00002 |
| 1 m | 0.1 | −1.12×10²⁴ kg | 0.19 M⊕ | 0.0017 |
| 100 m | 0.1 | −1.12×10²⁶ kg | **18.8 M⊕** | 0.0017 |
| 100 m | 0.5 | −2.81×10²⁷ kg | 470 M⊕ | 0.042 |

### The change of category

| | mass | vs observable universe |
|---|---|---|
| Pfenning–Ford wall, R = 100 m, v_s = c | 2.31×10⁶² kg | **1.5 × 10⁹ universes** |
| D free, R = 100 m, β = 0.1 | 1.12×10²⁶ kg | 7.5 × 10⁻²⁸ |

A factor of **2 × 10³⁶** — and more importantly a change of *kind*. The standing objection to warp
drives is not that they are expensive. It is that they require more mass-energy than the universe
contains, which is not an engineering problem but an impossibility. **That objection is gone.** What
replaces it is planetary, and planetary is an engineering problem.

### The gap that remains, and it is not a bound

Nobody can make 10²² kg of negative energy. The best laboratory source is Casimir: 1 m² at 10 nm gives
−4.334×10⁻⁴ J, a mass equivalent of 4.82×10⁻²¹ kg. The remaining gap is **2.3×10⁴²**.

> **That is a gap in capability, not a gap against a law.** Every previous statement of the warp-drive
> problem put a *theorem* between the design and the build. There is no theorem there now — there is a
> number, and the number is large. Those are different situations, and this project has not been in the
> second one before.

**What must be said with it:** the energy is still *negative*, and planetary-scale negative energy has
no known source. This is the Alcubierre class — metric-first, pointwise NEC-violating — **not** the
warpshell, whose ℓ≥2 obstruction is untouched. The SNEC's four O(1) exposures all still apply. And a
horizon still forbids control above β = 1, so the space this opens is the **subluminal** one — which is
also where the SNEC has its largest margin. Those two agree, which is worth noticing.

### `paper/CLAIMS.md`

The paper register now exists: every claim the project would defend in print, each naming its
instrument, whether it is new, what it corrects, and **what would falsify it**. H1 (the timelike/null
misapplication) and H2 (the change of category) are flagged for the abstract. It also carries an
explicit *not claimed* section — that no warp drive is being asserted, that the warpshell remains
blocked, and that QNEC proper is still unasked and scored 0.5 rather than 1.

**Directive scorecard:** 1 **MET**. 2 moved from *no* to *the standing objection does not hold*. 3 has
a design equation for the first time. None of that is a warp drive, and the register says so in its own
section.

## `typefour.py` — the objection that replaces it, and it is harder

If the standing objection no longer holds, what does? The answer is not about how much.

> **Hawking–Ellis Type IV.** A stress-energy is classified by the eigenvalue structure of `T^μ_ν`.
> **Type I** is diagonalisable with a timelike eigenvector — it has a *rest frame*, and every substance
> anyone has handled is Type I, the Casimir vacuum included. **Type II** is the defective null case:
> radiation, null dust, Le's photon-rocket exterior. **Type IV has a complex eigenvalue pair**, which
> means there is **no observer, anywhere, for whom it has a rest frame.** Nothing known is Type IV.

### The measurement, validated twice before it is believed

The stress-energy is computed from scratch — metric on a grid, finite-differenced to Christoffels,
differenced again to Riemann, contracted to Ricci and Einstein, divided by 8π; then Faddeev–LeVerrier
for the characteristic polynomial and Durand–Kerner for its roots, in complex arithmetic. A
doubly-differenced metric is exactly the pipeline that returns confident nonsense, so:

- **Vacuum.** ‖T‖ = 2.2×10⁻⁶ at the bubble centre, 2.5×10⁻⁸ at r = 2, and **exactly 0** at r = 3. That
  is the noise floor, six orders below every signal.
- **The closed form.** `T⁰⁰` for the Eulerian observer must equal BBV Eq (3.48), which `twist.py` holds
  independently as `−Ω²/(8πG)`. It does, **to 10⁻⁶** at five off-axis points, returning 5×10⁻⁹ on the
  axis where the closed form is exactly zero.

| (x, y) | ‖T‖ | \|Im\|/‖T‖ | type |
|---|---|---|---|
| (0.60, 0.00) | 0.00612 | 0.1435 | **IV** |
| (0.90, 0.30) | 0.15909 | 0.6425 | **IV** |
| (1.00, 0.20) | 0.28861 | 0.2585 | **IV** |
| (1.20, 0.30) | 0.01897 | 0.6937 | **IV** |

Seven of seven. The imaginary parts are 14–69% of the tensor's own norm and **stable to six figures**
as h changes by 4×, which noise is not. This reproduces the classification in Le's Table 1 by an
independent route.

### Why no energy-condition result can reach it

Every energy condition — NEC, WEC, DEC, ANEC, the quantum inequalities, SNEC, QNEC — is an inequality
on a **contraction** of `T_μν` with some vector. Type IV is a statement about its **eigenvectors**. You
can make the contractions as small as you like and the eigenvalues stay complex.

> The old objection was *"you need more energy than exists."* That is gone. The objection that replaces
> it is *"the thing you need has no rest frame"* — and it is the harder of the two.

### And it exposes the real shape of the problem, which is a trade

| | budget | matter |
|---|---|---|
| **Alcubierre class** | tractable — 18.8 M⊕ | **Type IV**, unknown to physics |
| **warpshell** | tractable | **Type I**, dominant-energy, observer-robust |

…and the warpshell is ℓ≥2 unstable while self-gravitating. **Neither architecture has both, and the two
obstructions are unrelated.** That is a cleaner statement of where warp drive stands than "it needs
10⁶² kg," and it is the first time this project has been able to say what the actual choice is.

The route out of Type IV is known and not free: **stop prescribing the metric.** Le's worldtube-first
construction installs interpretable matter region by region and gets Type I — and lands squarely on the
other obstruction. BBV make the same point as methodology: reading off whatever stress-energy a chosen
metric returns *"can manufacture sources with no interpretation as physical matter."* **Type IV is what
that sentence looks like when it is measured.**

**Not claimed:** that Type IV is *impossible*. It is **unknown**, which is weaker and honest — no
theorem forbids it, and Hawking–Ellis is a taxonomy rather than a law.

### The index gained a cell

`TYPE-IV` is the sole occupant of **(+1, −1, −1)** — a coordinate none of the previous 130 findings had
touched. It is the cell for *warp energy identified, and its algebraic kind is the reason for both
negative answers.* `E(X) = 0` still holds, so the closure demanded nothing new. And `pathmetric.py`'s
mismatch count moved 204 → 252 with the cell count 14 → 15, because it measures the corpus's lattice
condition over **this project's** cells — a fixture that tracks the index by design.

## `anec.py` — QNEC asked properly, and it withdraws this session's headline

Taking the three open items in order, the first is QNEC. Its first act is to overturn my own claim.

### The error, precisely

SNEC is `∫⟨T_kk⟩g²dλ ≥ −(4B/G)∫(g′)²dλ`, and it must hold for **every** sampling function.
`nullbound.py` evaluated it at **one** width — the wall thickness D — noticed both sides go as 1/D²,
and concluded the thickness cancels into permission. The arithmetic was right; the reasoning was not.
**D is the width at which the bound is loosest.** The right-hand side falls as 1/w² while the left
falls only as 1/w once w exceeds the wall:

| w | ∫T_kk g² | bound | |
|---|---|---|---|
| 0.10 | −9.29×10⁻⁵ | −1.760 | ok |
| 0.50 | −5.93×10⁻³ | −7.92×10⁻² | ok |
| **1.00** | −2.43×10⁻² | −1.99×10⁻² | **VIOLATED** |
| 20.0 | −8.11×10⁻³ | −2.84×10⁻⁶ | **VIOLATED** |

Crossover at **w = 0.927** — of order the *bubble radius*, against a wall of ~0.125. One width is not a
scan, and I chose the flattering one.

### And QNEC settles it, because it is a theorem

`⟨T_kk⟩ ≥ (ℏ/2π)S″` integrates along a complete generator to `∫⟨T_kk⟩dλ ≥ 0` — **ANEC** — since the
boundary entropy variation vanishes for a localised, asymptotically vacuum bubble. Measured on
`typefour.py`'s validated stress tensor, contracted with the null `k^μ = (1, v+1, 0, 0)`:

| y | 0.0 | 0.2 | 0.3 | 0.5 | 0.8 |
|---|---|---|---|---|---|
| ∫T_kk dx | −0.081 | −0.087 | −0.095 | −0.129 | −0.344 |

**Negative on every ray. ANEC is violated, so QNEC forbids the configuration.** And QNEC is a *theorem*
in QFT (Bousso–Fisher–Leichenauer–Wall; Balakrishnan–Faulkner–Khandker–Wang; Ceyhan–Faulkner) where
SNEC is a conjecture — the instrument that closes this is stronger than the one that appeared to open it.

### What survives, and it is not nothing

Fewster & Roman stands: **no null quantum inequalities in 4D**. Pfenning & Ford's bound really is a
**timelike** instrument, and its bound on the wall thickness really is an artefact of that. The 1/D²
cancellation is real arithmetic.

> **So the thickness genuinely does drop out — into prohibition, not permission.** ANEC is violated at
> *every* thickness, so D was never the obstruction and removing its bound buys nothing. The 10⁶² kg was
> the wrong statement of the problem. The right statement is worse, and does not involve D at all.

Which is the same shape as `typefour.py`: **both surviving obstructions are D-independent and both are
about the kind of matter, not the amount.** Two independent objections, neither touched by any argument
about energy budgets. In `index3.py` they share a cell — `ANEC-VIOLATED` joins `TYPE-IV` at
**(+1, −1, −1)**: *warp energy identified, and what identifies it is what forbids the build and the spec.*

### `shape.py`'s first tested prediction failed

The shape said a static positivity condition loosens when the dynamics is restored. Applied to the
energy conditions, the dynamical form is QNEC — and QNEC is locally looser (it permits `⟨T_kk⟩ < 0`
where `S″ < 0`) and **globally no looser at all**, because it integrates to ANEC. On the case it was
applied to, the prediction points the wrong way.

`evidence_available()` returns to **0** and `NEC-LADDER` is scored **FAILED**, not PARTIAL. That is the
first real test the shape has had and it did not pass it — recorded that way, because a pattern that
only ever gets credit is not an instrument.

`nullbound.py` and `designpoint.py` are kept executable with their conclusions struck, per this tree's
practice; `paper/CLAIMS.md` strikes H1 and H2 in place rather than deleting them, and **H3 — the
two kind-not-amount objections — becomes the headline.**

## `universal.py` — not which element, but which state

The question *"what element permits warp travel"* has no answer, and the reason is now precise: **both
surviving obstructions quantify over all matter.** Type IV says no substance has the required algebra;
ANEC says no substance makes the integral positive. Neither mentions an element, so neither can be
answered by naming one.

> The question with a shape is: **what physics makes an ordinary Type-I element behave as the geometry
> requires?** That is a question about *states*, and every element has the same states available to its
> fields.

### Type IV is already realized — by a state

Not hypothetically. Martín-Moruno & Visser (Phys. Rev. D 103, 124003): *"For test fields it is not too
difficult to get a type IV stress-energy via quantum vacuum polarization effects — for example, the
**Unruh quantum vacuum state** for a massless scalar field in the Schwarzschild background."*
Abdolrahimi, Page & Tzounis showed it is Type IV **everywhere outside the horizon**.

Reproduced here from their Appendix B, the (1+1) Schwarzschild Unruh state with `z = 2m/r`:

| z | Γ | type |
|---|---|---|
| 0.2 | −0.819 | **IV** |
| 0.5 | −2.438 | **IV** |
| 0.8 | +7.05 | I |
| 1.05 | −288.9 | **IV** |
| 1.20 | +67.3 | I |

Sign changes at exactly **1/√3, 1, 2/√3**, matching their published intervals.

> **A vacuum *state*, belonging to no element and to every element's fields.** That is the universal
> answer's shape: Type IV is not a substance anyone must find.

### But back-reaction is where it bites — and that is the real result

The same paper proves that once the stress-energy must **source** its geometry self-consistently,
Type I is forced in four cases. A warp drive must source its own geometry, so this is the list that
matters — **and the bubble is outside every entry on it:**

| MMV forces Type I when… | bubble? | why not |
|---|---|---|
| static, domain of outer communication | **no** | their proof needs block-diagonalisability, which is **zero twist** |
| on any Killing horizon | **no** | subluminal drives have none |
| axis of a **circular** stationary axisymmetric spacetime | **no** | `g_tx = −v` flips under t → −t while x does not — **not circular**, verified at three points |
| Bianchi I, FLRW, single-mode Bianchi | **no** | a localised bubble is not homogeneous |

That third row also resolves what looked like a contradiction: `typefour.py` measures Type IV **on the
axis**, h-converged to six figures, where their axis theorem would say Type I. **Non-circularity is
why** — and it is not a loophole.

### The universal statement

Put it together with BBV's Theorem III.15 — a vorticity-free Alcubierre drive **is** Minkowski:

> **twist = 0** ⟹ Minkowski (BBV) **and** block-diagonalisable ⟹ Type I (MMV)
> **twist ≠ 0** ⟹ it transports **and** it is outside every Type-I theorem

**Type IV is not an accident of Alcubierre's ansatz. It is forced by the same geometric property that
makes the object a warp drive at all.** A warp drive that were Type I would have zero twist and would
be flat space.

That is element-independent in both directions, which is what was asked for. It says nothing about
materials because there is nothing about materials to say.

### What is open, and what this does not touch

**Open, and it is one sharp question:** whether a *self-consistent* Type IV solution exists — Type IV
that sources its own geometry rather than riding a fixed background. MMV close with *"This list is not
necessarily exhaustive, and we are actively seeking further examples,"* so the warp case is **unsettled
rather than excluded.** No theorem covers it; no construction exhibits it.

**Not touched:** the Unruh result is a **test field** on a fixed background — precisely the case MMV
distinguish from back-reaction, and that distinction is the whole content of their paper. And **ANEC is
independent and still violated.** Its element-independent escape (achronality) has not been examined.

---

## Pass 12 — `selfconsistent.py`: the sharp question, answered at first order

The previous pass closed with exactly one open item: **does a Type IV stress-energy ever source its
own geometry, rather than riding a fixed background?** That is the whole of the distinction MMV draw,
and their own closing sentence — *"This list is not necessarily exhaustive"* — is why it was unsettled
rather than excluded.

### The answer, and it has a name

**Yes, at first order in ℏ, and the solution is an evaporating black hole.**

Abdolrahimi, Page & Tzounis (*Phys. Rev. D* **100**, 124038; arXiv:1607.05280) put the Unruh-state
`⟨T_μν⟩` on the right-hand side of the semiclassical Einstein equation and solve for the metric — an
approximate time-dependent metric in ingoing Eddington–Finkelstein coordinates for an evaporating
non-rotating hole, as a first-order perturbation of Schwarzschild. Their result:

> *"We believe that we are the first to show that a conformally coupled massless scalar field in the
> Unruh state has a stress-energy tensor that is Hawking–Ellis Type IV everywhere outside the horizon
> of a slowly evaporating Schwarzschild black hole, so that there are no observers anywhere outside
> that see zero energy flux."*

So the standing rebuttal to H3 — *nothing known is Type IV, and back-reaction forces Type I anyway* —
**is false as stated.** Something known is Type IV, it sources a metric, and if Hawking radiation is
real the configuration occurs in nature around every evaporating hole there is.

### Why MMV's theorems do not forbid it, and it is the same reason as the bubble's

| MMV's Type-I-forced case | evaporating hole |
|---|---|
| static | **no** — the mass depends on retarded time, `μ′ = −α/μ²` |
| Killing horizon | **no** — an evaporating horizon is dynamical |
| circular axisymmetric, on axis | **no** — the outgoing flux breaks circularity |
| Bianchi homogeneous | **no** |

`universal.py` established the bubble is non-circular because `g_tx` flips under `(t,φ)→(−t,−φ)` while
`x` does not. The hole's flux breaks it the same way. **A time-dependent flux is not
block-diagonalisable** — one structural fact, two escapes.

### The magnitude, which is now the live question

APT's scaling is exact: at fixed `z = 2m/r` the orthonormal components go as `μ⁻⁴`, and the flux
component is closed form, `f(z) = αz²/(16π(1−z))` with `α = 3.7474×10⁻⁵`. Against `warpenergy.py`'s
requirement `ρ = β²/(144πD²)` in Planck units at the flatness-limited wall `D = R/3`:

| bubble | matching BH | `r_s` | `T_H` |
|---|---|---|---|
| R = 1 m, β = 0.001 | 1.126×10¹⁰ kg | 1.67×10⁻¹⁷ m | 1.09×10¹³ K |
| R = 1 m, β = 0.01 | 3.562×10⁹ kg | 5.29×10⁻¹⁸ m | 3.45×10¹³ K |
| **R = 1 m, β = 0.1** | **1.126×10⁹ kg** | 1.67×10⁻¹⁸ m | 1.09×10¹⁴ K |
| R = 10 m, β = 0.1 | 3.562×10⁹ kg | 5.29×10⁻¹⁸ m | 3.45×10¹³ K |
| R = 100 m, β = 0.1 | 1.126×10¹⁰ kg | 1.67×10⁻¹⁷ m | 1.09×10¹³ K |

**Primordial-black-hole masses, not absurd ones.** A billion kilogrammes is a mountain, and the
required Type IV strength is what such an object carries in its Hawking flux as a matter of course.
The match scales only as `R^{1/2}` — a hundredfold bigger ship costs a tenfold heavier equivalent.

### The scope, drawn deliberately tight

Encoded as `selfconsistent.SCOPE` and asserted by its selftest, so it cannot drift:

1. **First order in ℏ, not exact.** APT compute `⟨T⟩` on the *unperturbed* background and use it to
   source the perturbation; they never iterate to a fixed point where `⟨T⟩[g] = G[g]/8π`. MMV's
   theorems are statements about **exact** solutions. There is no contradiction in either direction —
   APT do not refute MMV, MMV do not exclude APT. **Answered at first order. Open at exact order.**
2. **Conformally coupled massless scalar.** For spin 1 APT are explicit that they are *"not certain"*:
   Type IV only for `z < 0.044`, and possibly nowhere if the disputed `k₃` term vanishes.
3. **Configuration is not matched.** The hole's Type IV is a spherically symmetric **radial** flux; the
   bubble needs a **twisted** one. Same type, same strength, different shape, and nothing here arranges
   one into the other. **A magnitude match is not a construction.**
4. **ANEC is untouched**, independent, and still violated on every ray.

### Why this is not the `nullbound` episode again

That headline was withdrawn because it rested on my own inference from a scan I had not run. This
rests on a published, peer-reviewed, back-reacting calculation with an explicit metric, and the claim
being made is **narrower than the paper's own**. Different epistemic position — and the scope list
above is drawn tight for exactly the same reason.

### Seated

- `index3.py` — 144 findings, still 15 cells. `SOURCES-ITSELF` (+1,+1,0), `MAGNITUDE-MATCH` (+1,0,+1),
  `CONFIG-UNMATCHED` (0,−1,−1), `EXACT-ORDER-OPEN` (0,−1,0). `SELF-CONSISTENT-OPEN` **stays as it was
  asked** — a status is never flattened.
- `obstruct.py` — 15 rows. New row `TYPEIV-SOURCES`, **CONDITIONAL**: false at first order, open at
  exact, with the boundary named. `TYPE-IV` itself stays **OPEN**: what survives is the configuration.
  The verdict block is now computed from the ledger rather than transcribed.
- `paper/CLAIMS.md` — **H4**, flagged for the abstract, with its four-item scope.

---

## Pass 13 — `achronal.py`: the order language, and it closes the escape against us

The previous pass ended by naming one item worth doing: whether the ANEC-violating rays are
**achronal**. The instrument is built, it ran, and the answer is no escape — with a mechanism that
makes the closure worth more than the escape would have been.

### The corpus named the error before the physics did

Register 1173 of The Method 1.6 states the hierarchy:

> **LOGIC IS NOT A LANGUAGE. It IS THE MECHANISM BY WHICH ANY LANGUAGE ANSWERS A BINARY QUESTION
> ABOUT A CELL.** *Three levels, not one list: **binary** is the type; a **language** is a coordinate
> system with a closure operator; **logic** is binary → language → binary.* **A language earns its row
> when logic can operate on it and get a binary back.**

By that test `analysis` does not earn a row — it has a mechanism but returns a **magnitude**, not a
cell decision. ANEC is an analysis statement, and `anec.py` duly returned magnitudes. But **the
obstruction is a binary**: *this spacetime is forbidden*. The theorem that supplies the binary —
Graham & Olum 2007 — has a second hypothesis, **achronality**, and achronality is an **order**
statement: a set is achronal iff it is an **antichain** in the chronology relation.

Three of the corpus's rules land on the same spot:

| rule | what it said about our ANEC row |
|---|---|
| register 1173 | analysis returns a magnitude; the prohibition is a binary |
| register 1172 / `cypher.py` refusal #1 | *never print a verdict for a language nobody ran.* The **order** language was `NOT-RUN`. 1172 found five such pairs; this was a sixth, in **our** tree |
| §33.5 | *"Never fit across a language boundary"* — the rule the book says is enforced in code and blocks the most |

### The order operator, concretely

A null geodesic is achronal exactly up to its first **conjugate point**. For a shear-free congruence
Raychaudhuri collapses to a Sturm–Liouville problem with no `θ²` in it:

`u″ = −(R_kk/2)·u = −4πT_kk·u`,  `u(0) = 0`,  `u′(0) = 1`

a conjugate point being the next zero of `u`. Dropping shear is **conservative** — `σ² ≥ 0` only helps
focusing, so a ray called achronal here stays achronal with shear restored. `T_kk` is the same field
`anec.py` integrates, but along **true null geodesics** (RK4, `g(k,k)` held below 10⁻⁶) rather than the
fixed-`y` coordinate lines `anec.py` sampled. That difference is real: on the `y = 0.3` ray the
coordinate line gives `−0.0946` and the geodesic `−0.0603`. Both negative; not the same number.

### The result

| `v_s` | ANEC-violating rays | of those, non-achronal |
|---|---|---|
| 0.3 c | 9 | **0** |
| 0.5 c | 8 | **0** |
| 0.8 c | 8 | **0** |

**25 violating rays, zero escapes.** And the anti-correlation is the equation itself: where
`T_kk < 0` the Jacobi equation is **defocusing**, `u` is convex, and it is pushed *away* from the zero
a conjugate point requires. **The quantity that violates ANEC is the quantity that protects
achronality. You cannot buy one with the other.**

On the inner rays it is not even a measurement:

> **Lemma.** If `T_kk ≤ 0` along a null geodesic then it has no conjugate point, hence is achronal.
> *Proof.* `u″ = −4πT_kk·u ≥ 0` wherever `u ≥ 0`. With `u(0) = 0`, `u′(0) = 1`, `u` is initially
> positive and convex, so `u′` is non-decreasing, so `u′ ≥ 1` and `u ≥ λ > 0`. No zero. ∎

Exact for `y ≲ 0.3`, where `max T_kk` is `0` on the axis and `+9.3×10⁻¹²` at `y = 0.3` — noise. It is
**not** the whole story further out: at `y = 0.6, 0.7, 0.75` the ray crosses both signs — `T_kk` reaches
`+0.24` while the integral is still `−0.05` to `−0.14` — so there the verdict is **measured**. Not
marginal: exit slope `5.9` to `10.4` against a threshold of `0`.

### What survives, and it is sharper than what was removed

**The prohibition now rests entirely on the achronal ANEC in 4D *curved* spacetime, with no
configurational dodge left — and that condition is unproven.** Graham & Olum proved it in flat
spacetime in 2007; the self-consistent curved-space version has stood **nineteen years, no proof, no
counterexample**. `WARP-DRIVE.md` §6 recorded that before this pass. It is load-bearing after it.

Two limits stated rather than buried: shear is dropped (conservative) and vorticity is zero; and the
scan covers impact parameter for `+x` rays at three speeds — it is **not** a proof over all null
geodesics. A ray family the scan does not contain is `NOT-RUN`, never absent.

### Seated

- `index3.py` — 149 findings, still 15 cells. `ACHRONAL` joins `TYPE-IV` and `ANEC-VIOLATED` in
  (+1,−1,−1); plus `DEFOCUS-PROTECTS`, `ACHRONAL-LEMMA`, `UNPROVEN-LOAD`, `LANGUAGE-BOUNDARY`.
- `obstruct.py` — 16 rows. New `ACHRONALITY`, **CLOSED-NEGATIVE**: the escape was looked for and is
  not there. The `ANEC` row is amended to say it **hardened**, not softened.
- `paper/CLAIMS.md` — **H5** and **H5′**, flagged for the abstract, plus the methodological finding.

---

## Pass 14 — `transit.py`: travel → turn → seat, and M's both-ends prediction

M proposed a three-part structure and predicted something falsifiable about it. Both are tested here.

> **PART 1 TRAVEL** — set the optimal conditions for transition. First principles, including
> observability. **PART 2 TURN** — the turning mechanism that allows seating; a condition requirement,
> met iff part 1 is fully defined and stated for input. **PART 3 SEAT** — seating and closure.
> Both sets of coordinates must be known at the onset of part 1 so part 2 can initialize, and part 2
> fails if the input data doesn't provide enough for part 3.
>
> And: **the mathematical expression is visible at both ends with the same binary chain.**

### The structure is not a metaphor here

`achronal.py` had already reduced the causal question to a Sturm–Liouville problem, and it has exactly
this shape:

| part | the mathematics |
|---|---|
| **1 travel** | `u(0) = 0`, `u′(0) = 1` at departure **plus a declared arrival**. A two-point problem in initial-value clothing — which is *why* the far endpoint cannot be discovered later: without it there is nothing for part 2 to test against. |
| **2 turn** | does `u` turn and return to zero? The **conjugate point** is that turn. It fails — returns no length at all — when part 1's conditions do not focus enough to reach one. |
| **3 seat** | the turn lands **on** the declared arrival: `u(L_declared) = 0`. Closure. |

Observability is met the way parts 1 and 3 demand: a conjugate **length** is an affine invariant of the
congruence, not a coordinate separation. Two observers disagree about where B is and agree about `L`.

### The prediction — proved, then measured

> **Theorem.** If `u″ + qu = 0` with `u(0) = u(L) = 0`, then `v(x) := u(L−x)` solves `v″ + q̃v = 0` for
> the path read from the far end, `q̃(x) = q(L−x)`, with `v(0) = v(L) = 0`. **The same pair is
> conjugate.** ∎

The Jacobi operator is self-adjoint — absorbing `θ²` leaves no first-derivative term — so departure and
arrival are interchangeable and the turn is one object seen from two ends.

| `y0` | `L` (A→B) | `L` (B→A) | \|diff\| |
|---|---|---|---|
| 0.8 | 9.9975835361 | 9.9975835361 | 1.1e-14 |
| 0.9 | 5.3760386939 | 5.3760386939 | 5.3e-14 |
| 1.0 | 5.2600374222 | 5.2600374222 | 5.2e-14 |
| 1.1 | 5.5028056987 | 5.5028056987 | 5.7e-14 |
| 1.2 | 6.4050733902 | 6.4050733902 | 9.1e-14 |

and **0.00e+00 exactly** on a deliberately asymmetric control potential with no geometry in it. The
four-binary chain — turn / seats / achronal / ANEC sign — is identical at both ends on every ray.
**The prediction holds.**

*A note on how it was nearly missed.* The first attempt marched the Jacobi field backward from the
detected zero — **a step**, accumulating — and gave answers off by 0.09 to 0.285. Bisection on the
conjugate length — a closed form on the boundary condition, no walking — gave 1e-14. That is register
1206's own sentence happening again: *"The equation is not a step — it is a closed form on the index's
own coordinates, and that is what closes the gap."*

### And the structure then excludes two things

**Exclusion 1 — the turn lives in the energy-condition-*satisfying* sector.** `u″ = −4πT_kk·u` turns
`u` back only where `T_kk > 0`. Negative `T_kk` is convex, and convex never returns. So part 2
succeeds only on rays that **satisfy** ANEC and fails on every ray that violates it — `DEFOCUS-PROTECTS`
read the other way round. **The exotic sector cannot seat.** General: it is the sign of the equation.

**Exclusion 2 — and that sector arrives late.**

| `y0` | turn | `t − |dx|` | |
|---|---|---|---|
| 0.8 | 9.990 | +8.931e-01 | **LATE** |
| 1.0 | 5.250 | +1.320e-02 | **LATE** |
| 1.2 | 6.390 | +7.066e-04 | **LATE** |
| 1.5 | none | −1.243e-04 | early — **but it does not turn** |
| 2.0 | none | −5.044e-08 | early — **but it does not turn** |

Positive Shapiro delay, which is what positive energy always gives. The early leads are real and
converged to five figures across an 8× refinement, and they belong to rays that never turn.

**TURN ⟹ LATE. EARLY ⟹ NO TURN.** On this metric no configuration has both.

### What it is and is not

**Is:** a coherent, correctly gated, computable frame whose both-ends prediction is exactly true, and
which produced two exclusions the previous frame could not see.

**Is not:** a transport mechanism. A conjugate point is a **light focus** — a null congruence leaving A
and reconverging at B. It says B sits on a degenerate boundary of A's causal future. It carries no
payload, and nothing here claims it does.

**And not** a result about all metrics. Exclusion 1 is general; **exclusion 2 is measured on the
Alcubierre bubble at `v_s = 0.5 c`**, and another `T_kk` distribution is `NOT-RUN`, never absent.

### Seated

- `index3.py` — 153 findings, still 15 cells: `BOTH-ENDS`, `GATED-STRUCTURE`, `TURN-NEEDS-ORDINARY`,
  `TURN-IS-LATE`.
- `obstruct.py` — 17 rows. New `TURN-ADVANTAGE`, **CLOSED-NEGATIVE**.
- `paper/CLAIMS.md` — **H6** with both exclusions.

---

## Pass 15 — `seatindex.py`: the conjugate point as an index, and what seats universally

> *"The whole focus is now the conjugate point. We must identify what conditions/parameters do and do
> not allow for universal transport. This is again an index, and we are looking for the conditions
> that maximize universal transport."*

`transit.py` reduced seating to one equation — `u″ = −qu`, `q = 4πT_kk`, `u(0) = 0`, the turn being
the next zero. So "what conditions seat" is a question about `q` alone, and it has **two sharp
classical bounds that bracket it from either side.**

| | condition | force |
|---|---|---|
| **Sturm** (sufficient) | `q ≥ m` on a contiguous `ℓ ≥ π/√m`, i.e. **`m·ℓ² ≥ π²`** | seats **universally** |
| **Lyapunov** (necessary) | `L·∫q⁺ > 4` | below it **nothing** seats, whatever the shape |

### "Universal" is doing real work

Sturm's condition is universal in the strict sense: **the zero occurs inside the focusing stretch**,
so nothing outside can prevent it. Measured at exactly `m·ℓ² = π²`, over five approach distances
crossed with surrounding potentials of `0`, `−5` and `−20` — **15/15 seat.**

Below the frontier it breaks: **Sturm 0.49 → 1 failure, Sturm 0.25 → 7**, and the failures are always
*short approach plus hostile outside*. That combination is exactly what a fixed approach hides, and
it is why the first version of this test was wrong — I held `c = 1.0` and got "universal" for a
sub-Sturm slab. A favourable approach carries a small `u` into the slab and needs less focusing.
Sufficiency is a theorem; **the exact frontier of universality is `NOT-RUN`**, not absent.

### Register 1206's three populations, run rather than assumed

The resemblance was flagged `NOT-RUN` two passes ago. Run:

| population | cells | seat |
|---|---|---|
| **interior capture** (`m·ℓ² ≥ π²`) | 64 | **64** |
| **working overlap** | 84 | 75 — *and 9 do not, which is what makes it the overlap* |
| **exterior** (Lyapunov-excluded) | 12 | **0** |

Exact, not suggestive.

### Which coordinates the index needs

The information language's test, run on four candidates:

| coordinate | verdict |
|---|---|
| `m` strength | **axis** — keeps cells |
| `ℓ` extent | **axis** — and it enters as `ℓ²`, not `ℓ` |
| `L` total length | **axis** — it is the Lyapunov denominator |
| `c` position | **FOLDS** about the midpoint — `c` and `L−ℓ−c` are the same cell |

The fold is `transit.py`'s reversal theorem **spent as a coordinate saving**: self-adjointness halves
the index rather than shrinking it. M's both-ends prediction paying a second dividend.

### What maximizes it

On the frontier the focusing budget is `∫q = m·ℓ = π²/ℓ`, so **the cost of a universal seat falls as
`1/ℓ` without limit.** Long and weak beats short and strong. With total length `L` the cheapest
universal seat uses all of it: `ℓ = L`, `m = π²/L²`, budget `π²/L`.

### And the matter that meets it is ordinary

`q = (4πG/c⁴)T_kk`, so the universal condition in SI is

**`T_kk ≥ πc⁴/(4Gℓ²) = 9.5053×10⁴³ / ℓ² Pa`**

| `ℓ` | `T_kk` needed | vs nuclear (~10³⁵ Pa) |
|---|---|---|
| 1 m | 9.51×10⁴³ Pa | 9.5×10⁸ × |
| 1 km | 9.51×10³⁷ Pa | 951 × |
| **100 km** | **9.51×10³³ Pa** | **0.095 ×** |
| 1000 km | 9.51×10³¹ Pa | 0.00095 × |

**Positive, energy-condition-satisfying, and below nuclear density beyond about 100 km.** This is the
sector `transit.py`'s exclusion 1 forced us into, and it turns out to be **inhabited** — matter that
seats a conjugate point exists in nature.

### The gap, stated plainly

**Universal seating is not universal transport.** A seat is a light focus: a null congruence leaves A
and reconverges at B. It carries no payload. And exclusion 2 stands — every turning ray arrives late.
This pass answers *"what conditions seat, universally"* exactly, and *"what conditions transport"* not
at all. The index is the right index; it is not yet the index of transport.

### Seated

- `index3.py` — 159 findings, still 15 cells: `UNIVERSAL-SEAT`, `NOTHING-BELOW`, `THREE-POPULATIONS`,
  `LONG-AND-WEAK`, `ORDINARY-MATTER`, `C-FOLDS`.
- `paper/CLAIMS.md` — **H7**.

---

## Pass 16 — `composite.py`: the intersection is not empty, and I had dropped the term that finds it

M asked whether one device should transition both space and time. The answer I gave was "it must be
two subsystems, because seating needs `R_kk > 0` and advance needs `R_kk < 0`." **That reasoning was
wrong, and this pass says why.**

### The dropped term

`achronal.py`, `transit.py` and `seatindex.py` all wrote focusing as `u″ = −(R_kk/2)u`, dropping shear
because `σ² ≥ 0` only helps focusing, so ignoring it is conservative. **Conservative for an existence
claim about one ray. Fatal for a search.** The full statement (Gao & Wald 2000, eq. 13):

`G″/G = −½[σ_ab σ^ab + R_ab k^a k^b]`

| term | order in the source | needs positive energy? |
|---|---|---|
| **Ricci** `R_kk = 8πT_kk` | **linear** | **yes** |
| **Weyl** `σ²` | **quadratic** | **no** |

**Ricci focusing needs positive energy. Weyl focusing is sign-blind.** A negative mass shears a
congruence exactly as hard as a positive mass of the same magnitude — while the Shapiro delay, being
linear, flips sign with it.

### Measured

Linearised static metric `Φ = −M/r`, either sign. Christoffels, Riemann and the optical tidal matrix
all by finite difference from the metric. Full Jacobi **matrix** `A″ = −T·A`, `A(0)=0`, `A′(0)=I` on a
parallel-propagated screen; conjugate point at `det A = 0`, which includes shear by construction.

| `M` | conjugate point | `t − \|dx\|` | |
|---|---|---|---|
| +2.0×10⁻³ | λ = 55.17 | +5.12×10⁻² | seats, late |
| **−2.0×10⁻³** | **λ = 56.50** | **−3.76×10⁻²** | **SEATS AND EARLY** |

Both signs seat within 2.4% of the same λ — the focusing is quadratic. Only the arrival flips.
Converged to four figures over a 4× refinement.

**Validations**, each against a number this pipeline did not produce:

| | check | result |
|---|---|---|
| 1 | light deflection vs `4M/b` | **0.03%** at `b = 0.2` |
| 2 | tidal matrix traceless (vacuum ⟹ pure Weyl) | `1.6×10⁻⁴`, **`h`-independent** — the metric's own `O(Φ²)`, not the difference |
| 3 | antisymmetric delay vs analytic Shapiro | **0.6%** |

### The window

`t − |dx| = (Shapiro, ∝M, flips) + (path lengthening, ∝M², never flips)`. Seating wants `|M|` large,
advance wants it small.

| `\|M\|` (negative) | conjugate | `t − \|dx\|` | |
|---|---|---|---|
| 2.0×10⁻⁴ | none | −4.35×10⁻³ | early, no seat |
| 1.0×10⁻³ | none | −2.04×10⁻² | early, no seat |
| **2.0×10⁻³** | **56.50** | **−3.76×10⁻²** | **SEATS + EARLY** |
| **5.0×10⁻³** | **45.58** | **−7.18×10⁻²** | **SEATS + EARLY** |
| **1.0×10⁻²** | **42.83** | **−7.97×10⁻²** | **SEATS + EARLY** |
| 2.0×10⁻² | 41.50 | +4.11×10⁻² | seats, LATE |
| 4.0×10⁻² | 40.83 | +6.16×10⁻¹ | seats, LATE |

**About a decade wide**, advance largest just under the upper edge. The answer to "where do they meet"
is not a point — it's a band.

### Why the earlier passes found nothing

Not only the dropped shear. **The Alcubierre bubble's focusing is Ricci-dominated** — the rays that
turn are the rays crossing positive `T_kk`. So `achronal.py`'s 25-ray result and `transit.py`'s
**TURN ⟹ LATE** are correct *for that object* and say nothing about this one. A compact source focuses
through **Weyl, in vacuum**, under a different sign rule. The results don't conflict; they're about
different terms of the same equation.

### The causal bookkeeping closes

The early ray travels **entirely through vacuum** — `T_kk = 0` on the whole path, ANEC violated
nowhere along it — and **past its conjugate point it is not achronal**, so Graham–Olum's hypothesis
fails. **That is exactly the escape `achronal.py` searched for and did not find.** It wasn't in the
Alcubierre family. Consistent with Olum (PRL 81, 3567): advance requires negative energy, and this
configuration supplies it — **off the payload's path**.

### Two process notes worth keeping

**The error that cost two runs, now a test:** a source *inside* the focal length `b²/4M` forms no real
image. My first runs put the source at 5 with a focal length of 11 and reported "no seat." Nothing
about the physics changed when I moved it to 40.

**And the citation correction:** Gao–Wald is the wrong authority for "no time advance" — their
Theorem 1 explicitly declines that interpretation (*"it is difficult to make a strong argument for
this interpretation"*). The right one is **Olum, PRL 81, 3567 (1998)**, which they cite.

### Not claimed — five things, and the list is the point

1. **Negative mass is assumed, not derived.** Self-consistency is only what `selfconsistent.py` gives, at first order in ℏ.
2. **Linearised weak field.** The window's upper edge is where the quadratic term bites, which is also where linearisation gets questionable. Its location is **indicative**.
3. **The focus is astigmatic.** Traceless tidal matrix ⟹ `det A = 0` is a *line* focus. Enough to break achronality; not a point-to-point image.
4. **No payload.** Null-geodesic optics. The timelike channel the conjugate point opens has not been integrated.
5. **One geometry.** The two-region concentric device is **`NOT-RUN`**. This establishes its enabling mechanism is real, not that the device closes.

### Seated

- `index3.py` — 164 findings: `WEYL-IS-SIGNBLIND`, `SEATS-AND-EARLY`, `THE-WINDOW`, `DROPPED-TERM`, `VACUUM-PATH`.
- `obstruct.py` — 18 rows. New `SEAT-MEETS-TRANSPORT`, **DISSOLVED** — the fourth dissolution, and the first since `EXOTIC-MATTER`. `TURN-ADVANTAGE` amended: reopened and answered.
- `paper/CLAIMS.md` — **H8**, the paper's central result.
