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
