# `tools/buildpackage.py` — everything but the drawings

Phase 3 of the build. What a team would be handed to start work: a specification sheet, a build
sequence with its critical path, a commissioning and charging procedure, interface control
between subsystems, the operating envelope and its protections, an acceptance test per subsystem,
and a register of what has never been built.

It stops exactly where drawings begin — no dimensioned schematic, no winding cross-section, no
P&ID, no civil layout. Those need a design office and the measurements §10 Stage A to D return.
The selftest asserts the refusal mechanically: **no drawing library may be imported**, and the
file may define **no design constant of its own**.

## Seven sections

1. **Specification** — every fixed parameter with the instrument that owns it.
2. **Sequence** — build order, and five long-lead items.
3. **Commissioning** — charging and first power, in eight steps.
4. **Interfaces** — eleven handovers, each with what the upstream side must guarantee.
5. **Envelope** — limits, control, and four trips in the order they act.
6. **Acceptance** — nine tests, each with what a shortfall costs.
7. **Gaps** — what has never been built, against the nearest thing that has.

## What building it found

**The critical path is not the magnet.** Four of the five long-lead items are *isotopes*, and two
of them — Cl-37 in tens of tonnes and ⁶Li in over a tonne — have **no industrial production line
anywhere**. A programme that treats this as a machine to be built discovers in year three that it
has no blanket. Stage A therefore runs before any concrete: it multiplies every balance
identically and so bounds all of them at once.

**There is no ignition.** The project's fourth criterion speaks of "an initial ignition" and the
word does not apply: the device has no threshold to cross and no burning state to reach. It
starts when the beam starts and stops when the beam stops — the same fact that makes it stable.
What the criterion names is a **charging** operation. The eight commissioning steps are ordered so
that everything reversible precedes C5, the step after which the building is a tritium facility
for the rest of its life; the selftest asserts that ordering rather than asserting `True`.

**The coil is life-limiting exactly at the plant's life.** The two radiation figures in
`machine.py` are one design, and the identity proves it: inverting the coil life for the shield
thickness that produced it returns **0.790 m at every beam power**. At the reference power the
insulation reaches its dose limit at 39.9 years against a 40 year plant life. Dose is linear in
beam power, so any power increase shortens the plant inversely unless the shield grows with it.

**The tightest interface in the plant is blanket → breeder zone**, where criterion 4 is decided;
the interface that sets the plant's *size* is the 20 T recompression, because the cell radius
follows from the field and the tritium holding follows from the radius.

## What it declines to compute

Beam-trip thermal cycling. A high-power proton linac trips often; how many interruptions the
intermediate loop tolerates is **not computed here** and is recorded as a genuine open item.

## Running it

```
python3 tools/buildpackage.py                 the whole package
python3 tools/buildpackage.py --spec          specification sheet
python3 tools/buildpackage.py --sequence      build order and long leads
python3 tools/buildpackage.py --commissioning charging and first power
python3 tools/buildpackage.py --interfaces    what each subsystem hands on
python3 tools/buildpackage.py --envelope      operating limits and trips
python3 tools/buildpackage.py --acceptance    how each subsystem is proved
python3 tools/buildpackage.py --gaps          what has never been built
python3 tools/buildpackage.py --selftest
```
