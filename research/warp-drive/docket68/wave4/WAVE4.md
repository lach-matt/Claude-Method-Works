# DOCKET 68 wave 4: what Step 1c left open, priced (verified once, corrected; not seated; 2026-10-05)

This wave opened on M-RULINGS item 40: "2 then 1 please". It is a D68 wave 4 first, then DOCKET 68's close and the
Q-1s prior-art gate. Each instrument imports its owners by path (seat, aperture and light through
`step1c/demand.py`; `step1c/coherence.py`). Every outside figure is READ at source, with its route recorded.

| item | file | selftest |
|---|---|---|
| W4A, the transmitted power (S1C-O8) | `linkbudget.py` | 6/6, 1 control, 3 STRUCTURAL |
| W4B, the fault-tolerant memory (H-FT-MEMORY) | `ftmemory.py` | 8/8, 1 control, 2 STRUCTURAL |

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

  With every optic read, the channel at the floor quantum needs more than the Sun's output. This conclusion is
  **fragile**, and the conditions below are what it rests on:
  - A beam narrower than **0.14″** onto 7 m², or 0.0037″ onto 46 cm², would need less than the Sun's output.
  - No coherent source at 263 keV is READ (H-NO-COHERENT-SOURCE). Whether an XFEL-class divergence of about 1 µrad,
    known only from memory and not read, can be had at that quantum is **OPEN**.
  - NuSTAR's 58″ is measured after ground reconstruction of its mast motion, so for a transmitted beam it is a best
    case (H-TX-OPTIC).
  - The beam-profile factor is order unity and OPEN (H-BEAM-PROFILE).
- **The diffraction-limited rows are at the floor quantum, not a minimum over quanta.** The floor quantum minimises
  received power, not transmitted power. At fixed apertures under diffraction, higher quanta lower the transmitted
  power roughly as 1/E: the verifier's band-limited stand-in gives 1.2e18 W at 263 keV and 1.1e13 W at 1 GeV. The
  minimum over quanta is OPEN, because seat's floor cannot be evaluated off its optimum. Figure-limited, the floor
  quantum is about optimal.

## W4B: a fault-tolerant memory for the quantum payload

This applies to a **quantum payload that must be stored**. That means a midpoint source (hold L/c), or a payload
streamed over a schedule: there Bob holds the earliest qubits until the last ones arrive, even with the source at Alice,
unless reassembly is itself progressive and coherent (H-INSTANT-ASSEMBLY, OPEN). It does not apply to a bit payload.

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
  - **1.7e5 physical qubits for every atom of the object**, which needs no hypothesis;
  - an energy of **1.8e24 J (1.35e16 W)** at T_CMB, at one erasure per syndrome bit. This overstates the floor
    somewhat, because sparse syndromes carry less than a bit each. Ideal refrigeration is already inside it, and real
    dissipation is excluded;
  - a mass, conditional on one atom of 1 u per qubit, of 1.9e6 kg, 2.7e4 times the object. With electron-spin qubits it
    would be 15 times the object.
- **The tolerance hardly matters**, because the distance grows only logarithmically with it:

| allowed expected failures | distance | physical qubits | mass at 1 u, × the object |
|---|---|---|---|
| 1 | 245 | 1.1e33 | 2.7e4 |
| 1e9 | 191 | 6.9e32 | 1.65e4 |
| 0.1 % of the payload | 95 | 1.7e32 | 4.1e3 |
| 50 % of the payload | 77 | 1.1e32 | 2.7e3 |

- **Streamed over 1 yr:** distance 241 and 1.1e33 physical qubits.
- **With the 1e-10 floor measured on one device's repetition codes, the memory fails**: 1.2e32 expected logical
  failures. The surface code's own floor is unmeasured. Holding needs the floor removed (H-NO-BURST-FLOOR).
- **History, kept:** the verifier found three earlier statements wrong:
  - a CONTROL that passed through a clamp;
  - the mass led with as a floor;
  - "refrigeration excluded and larger".

## Named hypotheses

- **W4A:** H-FRIIS-IDEAL, H-EQUAL-APERTURES, H-AT-FLOOR-QUANTUM, H-HOLEVO-STANDIN, H-FOCUS-AT-QUANTUM, H-BEAM-FIGURE,
  H-BEAM-PROFILE, H-TX-OPTIC, H-NO-COHERENT-SOURCE, H-FIGURE-AT-QUANTUM, and seat.py's H-EM-CARRIER, H-FEW-MODES and
  H-ONE-POL.
- **W4B:** H-LAMBDA-HOLDS, H-ONE-FAILURE, H-LANDAUER-PER-SYNDROME-BIT, H-ONE-ATOM-PER-QUBIT, H-NO-BURST-FLOOR and
  H-INSTANT-ASSEMBLY, plus coherence.py's and demand.py's.

## OPEN

1. A focusing optic at the floor quantum (263 keV at a year; 96 MeV at a day) with a measured figure.
2. The origin and removal of the 1e-10 burst floor.
3. Whether Λ holds to distance 245.
4. The real dissipation of either subsystem.
5. A coherent source at the floor quantum (H-NO-COHERENT-SOURCE).
6. The minimum transmitted power over quanta.
7. The streamed hold (H-INSTANT-ASSEMBLY).
