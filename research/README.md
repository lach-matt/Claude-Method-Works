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
