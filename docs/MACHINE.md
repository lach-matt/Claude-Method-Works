# MACHINE.md — the capture solenoid as a build package

`tools/machine.py` finishes what `collector.py --magnet` names and does not do, and adds what a magnet
alone does not make a machine. Run it with no argument for the whole package; `--circuit`,
`--mechanics`, `--conductor`, `--target`, `--radiation`, `--failure`, `--plant`, `--integration` and
`--selftest` give the parts. It is written up as §9 of
`papers/Cold_Fusion_Specification_and_Procedure_v1.0.md`.

**It imports the design, it never restates it.** Every field, aperture and capture figure is read from
`collector` at run time, per the corpus rule that an instrument imports a seated member. `--selftest`
asserts the aperture product is still what the design says before it computes anything from it.

## The finding that made it a separate instrument

The production target must sit **inside** the capture bore. The bore is **10.7 cm** in radius. Every
megawatt-class facility solves target cooling with a rotating solid target of metre scale, and **none
of them fits**: a wheel reaching the demonstrated 0.45 kW/kg needs a radius of 0.355 m, **3.3× the
bore**. The bore cannot be opened to admit one without losing the capture the machine exists for.

What fits is a **free liquid-metal jet**, and that configuration was built and run at CERN as MERIT —
a free mercury jet in a 15 T solenoid, for this application.

## What a published simulation corrected

Back, arXiv:1104.2742, is FLUKA and MARS over a 4 MW, 8 GeV proton beam on a mercury jet in a 20 T
solenoid — this machine. Reading it changed three things and corroborated a fourth:

| | this work had | the source says |
|---|---|---|
| beam power into the target | 55 % assumed | **8.0 %** — wrong by **6.9×** |
| coil inner radius | 80.7 cm, from a shield of this work's choosing | **120 cm**; 63 cm was found *inadequate* |
| heat to the cold mass at 1 MW | 335 W reconstructed | **140 W** |
| stored energy at that radius | — | this work computes **1080 MJ**; the source says *"approaching 1 GJ"* |

The last row is the first independent check on any number in the design. The first three are
corrections, and the ledger rows they replace are marked `WITHDRAWN` rather than deleted.

**Two of the corrections ran in this work's favour and one against**, and both directions are
recorded: the coil life rose from a reconstructed 7–30 years to a sourced **253**, the jet's velocity
floor of 30 m/s was **withdrawn** because the corrected power removed it, and the stored energy more
than doubled.

## What is computed here

- **Circuit and quench** — 20 kA, L = 5.40 H, a 10 kV dump at 0.500 Ω giving τ = 10.8 s and 2160
  MIITs, against a copper hot-spot allowance of 64.0 s: a margin of **5.93×**. That margin is a
  consequence of the conservative current density and is spent if the winding is thinned; the two are
  one decision.
- **Mechanics** — 720 MN of axial compression at the midplane, which is only **49 MPa** across
  fourteen square metres of winding. An end-plate problem, not a conductor problem.
- **Conductor** — graded REBCO / Nb₃Sn / NbTi, 13.8 km in total with REBCO for the innermost fifth.
  The source's own design avoids HTS entirely with a resistive 6 T insert; both routes are named.
- **Radiation** — 0.39 MGy/yr peak against 100 MGy allowed: **253 years**.
- **Failure modes** — loss of field, loss of jet, and both, from the source's own table. The
  consequence for the build is that each must trip the beam and the shielding must be a *rated dump*.
- **Plant** — 144 W at 4.5 K, 38.4 kW of wall power, 16.3 days of cooldown.

## The fuel cell — `--channel` and `--cell`

That item is now done, and doing it changed two things the rest of the work had said.

**The cell cannot sit in the capture region.** A pion at the stopping window has a decay length of
14.82 m and the capture region is 1.5 m, so a **34.1 m decay channel** is required. The beam expands
adiabatically through it as 1/√B, and tritium as the square: a cell sitting in a 2 T channel would need
**51.3 kg** against 5.13 recompressed. **Recompression at the cell is a requirement, not an
optimisation**, and it is free — adiabatic compression conserves |p| and leaves the stopping range and
the momentum window untouched.

**And recompression prices a choice §8.2 made.** Dropping the target field to 14.01 T to bring the peak
inside reach widened the beam, which is more tritium: **7.32 kg** at the capture field against **5.13**
recompressed to 20 T. Neither cost was visible until the cell was designed.

**The density should be run low, which inverts the specification.** Pressure falls linearly with
density and length grows as its inverse; length is cheap. At 500 MPa a 300 MPa steel is **excluded
however thick it is made** — a monobloc cylinder cannot hold a pressure at its own allowable stress.
The design point is φ = 0.6: 140.8 MPa, a 3.2 m cell, r_o/r_i = 1.66.

**Two requirements turn out to be one loop.** The fuel takes **21.65 kW** (5.52 from stopping muons,
16.13 from alphas that stay), needing **0.0372 kg/s** at ΔT = 100 K. Independently, tritium decay puts
**³He at 1 ppm every 18.8 minutes** against a 1 ppm purity spec. The flow the heat sets gives a
230-second turnover and holds ³He at **0.204 ppm** — already below what the specification demands.

## Coherence — `--coherence`

**A procedure that does not point at the machine is not a procedure.** The specification's §6 was
written before this design existed and named four things the machine does not have: a 2.60 T·m
collector where the design is 1.50, a 7.50 cm beam where the machine's is **8.96 cm** at the cell, a
cell "inside the solenoid bore" which §10.1 shows is impossible, and a forward-only acceptance for a
machine that has a mirror. Every apparatus figure §6 states is now computed here, so the two cannot
drift apart again.

**The three corrections very nearly cancel** — interception ×0.700, the mirror ×1.488, a finite decay
channel ×0.900, **net ×0.938** — and the committed prediction moves from 2.695e10 to **2.528e10**
neutrons per second. That it survives is not the point; that it was never checked until the machine
existed is.

**One machine, two bores.** The coil radius is sourced at 120 cm and both apertures fit inside it, so
the cold mass, the stored energy and the conductor are identical and only the shield thins. The wider
bore buys **1.188** in capture for **3.00** in tritium — and [1] §5.25 found that same trade at
**3.01** from a gyroradius argument alone. **This package reproduces it from a shield and a coil**,
sharing no step with it.

**And the mirror closes a loop with the laboratory programme.** [1] §10.1's committed band — 60.92,
49.16 and 44.43 percent — was computed by accepting *both hemispheres*, an instrumentation choice with
no mechanism. Because the required grade puts the loss cone outside every angle HARP measured,
**mirroring the backward hemisphere and accepting both are the same number**, reproduced to four
figures. That stage asserted a capability; this design is the magnet that supplies it.

## The end-to-end loss budget — `--budget`

**Q1 and Q6 were the last two open, both called "measurements". One was a calculation.**

**Q6 closes on geometry.** The pion absorption length is 15.9 cm in mercury and 10.8 cm in tungsten,
but the collector takes **large-angle** pions — 85.0 % of production — and a large-angle pion leaves
the target **sideways**. Its escape path is the target's *radius*, not its length. **A narrow target is
transparent however long it is**: 0.8961 for the published 30 cm × 8 mm jet, 0.8547 for a
652 × 5.1 mm rod, and 0.4040 for a 10 cm-radius block. The thick-target multiplicity that explains the
2.37 **survives to capture**, and the condition is that the target be long and thin — which the
published geometries already are.

**Q1 narrows to a budget.** Every loss between a produced π⁻ and a stopped binder:

| term | factor |
|---|---|
| target escape | 0.8961 |
| pion decay completeness | 0.9000 |
| muon survival in the channel | 0.9796 |
| scattering out of the transverse cap | 0.9021 (conservative) |
| adiabatic transport | 1.0000, by design |
| **product** | **0.7127** |

**It sharpens the prediction rather than softening it.** Stage A's committed η falls from 44.43 % to
**31.66 %** at the stopping window, and the margin over the 29.51 % that would falsify the model falls
from 1.51× to **1.073×**.

**And the two questions were coupled.** At 31.66 % the bred-fuel route does *not* close at the 50.8 %
its demonstrated-cycle balance needs; it closes at the 21.4 % the optimised production target needs —
and whether that gain is real was Q6. **The budget would have closed the route and Q6 re-opens it.**
Neither could be answered alone and leave the result standing.

## Every balance at what is delivered — `--balances`

**The budget has a consequence upstream, and it withdraws a headline claim.** [1] §5.19 states each
balance at 30 and 90 percent collection. **The 90 is unreachable** — the stopping ceiling is 0.5069 and
the budget delivers 0.3166 — so the table must be restated. The restatement is *exact*: the balance is
linear in collection, and §5.19's own two columns check it at 2.998–3.010 against 90/30 = 3.000.

| balance | as printed at 90 % | delivered 31.66 % | wider bore 37.62 % |
|---|---|---|---|
| heat, bound-case service life | **1.241** | **0.437** | 0.519 |
| bred fuel, demonstrated 150 cycles | 1.772 | 0.623 | 0.741 |
| bred fuel, bound-case service life | 6.96 | **2.449** | 2.909 |

**"The heat form passes at 1.241, so the self-sustaining criterion is met without leaving the device"
is withdrawn.** The figure was never wrong — it was stated *at 90 percent collection* and stands as
that conditional. Reading it end to end does not.

**What survives is one route:** bred fuel through an optimised production target, requirement 21.4 %
against 31.66 delivered — a balance of **1.480**, and 1.758 at the wider bore. That route depended on
whether the optimised target's gain is real, which is what `--budget` answers on geometry. Everything
else falls below unity.

## The acceptance census — `--census`

`--balances` restated **one** table. The same question belongs to every figure the two live papers
state at an assumed collection, and asking it by eye is not a method, so `--census` asks it against
the files. **46 sites**, each carrying the figure the paper prints, the acceptance it prints it at,
and a grade — and `--selftest` asserts that every one of the 46 still occurs in the file that prints
it and that every section named is still a heading there. The census cannot drift away from what it
censuses without failing.

| grade | rows | what it means |
|---|---|---|
| CONDITIONAL | 9 | the site states its assumption in the same sentence — it stands as printed |
| RESTATED | 29 | a reader would carry it away as end-to-end; every one falls |
| REQUIREMENT | 3 | [1] §5.22's inverse question — a requirement does not move |
| NOT-LINEAR | 4 | a break-even density or a sticking boundary; restating is not a multiplication |
| WITHDRAWN | 1 | a sentence rather than a number |

**Three of the RESTATED rows are divisors and grow.** The companion's §2.2 converts another group's
figure of merit into this paper's coordinates by *dividing* — 1.64, 2.25, 3.33 — and a lower delivered
acceptance makes those **2.30, 3.16, 4.67**. A restatement running the other way is exactly what a
hand pass gets wrong, which is why the kind exists.

**Completeness is measured, not claimed.** A hand-built census has one failure mode: the site nobody
noticed. So `--census` reads every line in either paper naming a collection assumption, takes every
number on it, and requires each to be censused, computed by the census, or exempt for a stated reason.
**Residue 0** — and it was not 0 when the check was written. It added the last eight rows (§5.9's
50.69 and 10.23, the three divisors, §5.25's 2.076) and caught a rounding: 0.854, not the 0.855 first
printed.

**The census does not find that the papers are wrong.** Most rows are conditionals stated as
conditionals, and those stand. What it finds is the reading.

**Three routes reach the same two numbers and that is the check.** §5.24's 0.875 is an *acceptance
over a requirement* and takes the loss budget as a factor of 0.7127; §5.19's 1.772 is a *balance at an
assumed efficiency* and takes delivered ÷ 0.90. Different arithmetic, different rows, different
sections — **0.6236** against **0.6234**, agreeing to **1.0003**. Separately §5.25's 2.076 restates to
**1.4795** against the 1.480 reached from the requirement side. Neither pair was built from the other.

**The one row graded WITHDRAWN** is [1] §5.21's *"comfortably inside the §5.9 collector … not an open
physical question"*. The stopping ceiling is 0.5069, so the §5.9 collector is not a shielding trade
away — it is unreachable. The sentence is withdrawn; the route survives only through the optimised
production target, at 1.480.

**One row the census corrected outside the papers.** Asked what [1] §5.22 prints for the electricity
requirement, the file says **299.6 percent**; this repository's `CLAUDE.md` had carried **96.7** from
an earlier draft, and so had `directives.py`'s D27. The papers were right and the summaries were
stale — which is the case for censusing files rather than memory, and the reason `docfigures.py`
exists.

**What the census refuses.** Four rows are a break-even density and two boundaries on sticking. The
balance is not linear in either, so the census names them rather than scaling them. **An un-restated
row is a finding, not an omission.**

## What is not done

Nothing in the physics. What is not here is a **fabrication package**: drawings, tolerances, weld and
joint design, the tritium plant's licensing case, and a quench analysis run in a magnet code rather
than on a hot-spot integral. That is engineering-office work on a design that exists.

## A limit of the publication standard, found here

`verify_paper.py` pass 3 matches a prose number against *any* ledger row carrying that value, not
against the row that ought to carry it. Three figures in an early draft of §9 were wrong by 1–5
percent and passed, because unrelated rows in a 660-row ledger happened to carry those values. They
were caught by recomputing each against its own named function. **A value test is not a binding
test.** Recorded in §9.9 and not repaired: binding prose to claim ids is a change to the standard.

## Re-verify

```
python3 tools/machine.py --selftest
python3 tools/machine.py --channel --cell
python3 tools/machine.py --coherence      # the spec sheet the procedure must quote
python3 tools/machine.py --budget         # every loss term, and the two questions it couples
python3 tools/machine.py --balances       # the balances at the acceptance actually delivered
python3 tools/machine.py --census         # every figure stated at an assumed acceptance, graded
python3 tools/machine.py
python3 tools/collector.py --magnet
python3 tools/verify_paper.py papers/Cold_Fusion_Specification_and_Procedure_v1.0.md
```
