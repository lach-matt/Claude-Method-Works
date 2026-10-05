# DOCKET 68 wave 4: what Step 1c left open, priced (not yet verified; not seated; 2026-10-05)

This wave opened on M-RULINGS item 40: "2 then 1 please". It is a D68 wave 4 first, then DOCKET 68's close and the
Q-1s prior-art gate. Each instrument imports its owners by path (seat, aperture and light through
`step1c/demand.py`; `step1c/coherence.py`). Every outside figure is READ at source, with its route recorded.

| item | file | selftest |
|---|---|---|
| W4A, the transmitted power (S1C-O8) | `linkbudget.py` | 6/6, 2 controls, 3 STRUCTURAL |
| W4B, the fault-tolerant memory (H-FT-MEMORY) | `ftmemory.py` | 7/7, 1 control, 2 STRUCTURAL |

## W4A: the transmitted power the channel needs

`seat.channel_floor` establishes a floor on **received** power only. Here the transmitted power is computed at the
floor's own quantum.

- **At 1 yr** (species count, one polarisation), the received floor is 4.39e6 W at a quantum of **263 keV**, a
  wavelength of 4.7 pm.
- **Diffraction-limited** (H-FRIIS-IDEAL):
  - Equal apertures of **491 m** make the link single-mode; above that size, the transmitted power is the received
    floor.
  - Below single-mode, at fixed apertures the transmitted power is the same at every schedule. That is an identity: the
    received power and the mode number both go as 1/T². For DSOC's hardware it is 2.1e17 W (5.5e-10 L☉), and for 10 m
    apertures 2.6e13 W.
- **But no optic is diffraction-limited at these energies.** The figures below were READ at source:
  - NuSTAR's mirrors stop at **78.4 keV**, and its PSF measured in flight is a **58″** half-power diameter, set by
    figure errors (1301.7307v1).
  - Above that, the only optic ever flown is the CLAIRE Laue lens: 170 keV, a ~3 keV band, 511 cm² geometric area at 9 %
    efficiency, and 33 photons from the Crab (1007.4308v3, a secondary account).
  - ASTENA's 30″ and 7 m² are **design** figures (2302.09272v1, 2309.11187v1).
  - The crystal alignment actually achieved is a Bragg-angle error averaging 101″, against the 10″ requirement
    (2309.11187v1).
- **Figure-limited at 1 yr** (H-BEAM-FIGURE, H-TX-OPTIC, H-FIGURE-AT-QUANTUM):

| optic | beam spot radius at L | transmitted power |
|---|---|---|
| NuSTAR's measured 58″, CLAIRE's flown 46 cm² | 5.65e12 m | **9.6e34 W = 2.5e8 L☉** |
| 58″ measured, 7 m² design | 5.65e12 m | 6.3e31 W = 1.6e5 L☉ |
| 30″ design, 7 m² design | 2.92e12 m | 1.7e31 W = 4.4e4 L☉ |

  With every optic read, the channel at the floor quantum needs more than the Sun's output.

## W4B: a fault-tolerant memory for the quantum payload

This applies only to a quantum payload with the pair source away from Alice (`coherence.py`). At the midpoint the hold
is L/c.

- **Measured** surface-code figures (Google Quantum AI 2408.13687v1, re-read by the lead):
  - ε₇ = 1.43e-3 logical error per cycle;
  - Λ = 2.14;
  - a 1.1 µs cycle;
  - 2d² − 1 physical qubits per logical qubit;
  - a **measured logical error floor of about 1e-10 per cycle**, from correlated bursts once an hour, origin not
    understood.
- **Species count over the midpoint hold** (1.22e14 cycles; H-LAMBDA-HOLDS, H-ONE-FAILURE):
  - code distance **245**;
  - **1.1e33 physical qubits**;
  - a Landauer floor at T_CMB of **1.8e24 J (1.35e16 W)**, excluding real dissipation and refrigeration;
  - a minimum mass, at one atom of 1 u per qubit, of **1.9e6 kg, which is 2.7e4 times the object**.
- **With the measured 1e-10 floor the memory fails**: 1.2e32 expected logical failures. Holding needs the floor removed
  (H-NO-BURST-FLOOR).

## Named hypotheses

- **W4A:** H-FRIIS-IDEAL, H-EQUAL-APERTURES, H-AT-FLOOR-QUANTUM, H-FOCUS-AT-QUANTUM, H-BEAM-FIGURE, H-TX-OPTIC,
  H-FIGURE-AT-QUANTUM, and seat.py's H-EM-CARRIER, H-FEW-MODES and H-ONE-POL.
- **W4B:** H-LAMBDA-HOLDS, H-ONE-FAILURE, H-LANDAUER-FLOOR, H-ONE-ATOM-PER-QUBIT and H-NO-BURST-FLOOR, plus
  coherence.py's and demand.py's.

## OPEN

1. A focusing optic at the floor quantum (263 keV at a year; 96 MeV at a day) with a measured figure.
2. The origin and removal of the 1e-10 burst floor.
3. Whether Λ holds to distance 245.
4. The real dissipation and the refrigeration cost of either subsystem.
