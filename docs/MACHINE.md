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

## What is not done, and it is one thing

**The D–T cell's mechanical and thermal design beside a liquid-metal target in a 14 T field.** The
specification's §5.3 already said the cell "must sit in the production target's region, which is a
hostile place to put a cryogenic tritium cell and is not designed here." That is still true. It is
named rather than absorbed, and it is the fourth item for the laboratory programme.

## A limit of the publication standard, found here

`verify_paper.py` pass 3 matches a prose number against *any* ledger row carrying that value, not
against the row that ought to carry it. Three figures in an early draft of §9 were wrong by 1–5
percent and passed, because unrelated rows in a 660-row ledger happened to carry those values. They
were caught by recomputing each against its own named function. **A value test is not a binding
test.** Recorded in §9.9 and not repaired: binding prose to claim ids is a change to the standard.

## Re-verify

```
python3 tools/machine.py --selftest
python3 tools/machine.py
python3 tools/collector.py --magnet
python3 tools/verify_paper.py papers/Cold_Fusion_Specification_and_Procedure_v1.0.md
```
