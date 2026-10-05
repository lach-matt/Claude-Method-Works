# Step 1c — the device: what each part must deliver (demand only; not seated; 2026-10-05)

M ruled the order: 1a the specification theorem, 1b the balanced equation, 1c the device (`specthm.py` section 0).
M's original framing was "balancing an equation with the theory and math on one side, and the device engineering and
materials on the other side" (`ledger.py` section 0). Step 1b fixed the equation: I(A, before) = I(B, after), with
every matter and energy term an input or an output (`step1b/BALANCE.md`, seated). A device is whatever performs those
terms.

`demand.py` (9/9 checks, 3 of them controls, 2 STRUCTURAL) reads the device's subsystems off the equation's rows and
prices what each must deliver, per schedule. **Every figure is imported from its owner. No supply is read here.** What
present engineering delivers for each subsystem is the next step, and which subsystem comes first is M's choice.

## The subsystems, from the equation's rows

| subsystem | row(s) | what it must do |
|---|---|---|
| READ-A | IN-A-READ | read I bits of the object at A |
| CHANNEL | IN-CHANNEL, IN-CHANNEL-E | carry I bits (R-CLASSICAL), or 2 bits per qubit (R-QUANTUM), from A to B |
| COUPLING | wave 3's alternative to CHANNEL | the A–B coupling (`corridor.py`); every speed-free route clashes with H-LOCALITY |
| ASSEMBLE-B | IN-B-ASSEMBLE, OUT-B-HEAT | place the atoms and write the I bits at B |
| POWER-B | B's local terms | the collector at Proxima b (`bsupply.py`) |
| STOCK-B | IN-B-STOCK | D25's stock gate: 749.1 kg of CI feedstock, binder P, unmeasured at Proxima (OPEN) |
| RETIRE-A | OUT-A-RESIDUE | A's matter retired as stock (H-RETIRE-A, M's hypothesis); its energy is OPEN |

## What they must deliver (species count unless stated; H-SCHEDULE, H-UNIFORM-RATE, H-PARALLEL)

| | 1 day | 1 year | 1 century |
|---|---|---|---|
| READ-A, bits/s (species to 0.1 Å) | 1.1e23 – 1.26e24 | 3.01e20 – 3.45e21 | 3.01e18 – 3.45e19 |
| READ-A and ASSEMBLE-B, atoms/s | 7.77e22 | 2.13e20 | 2.13e18 |
| READ-A, 1 Å probe floor power: photon / electron / neutron | 1.54e8 / 1.87e6 / 1.02e3 W | 4.22e5 / 5.13e3 / 2.79 W | 4.22e3 / 51.3 / 0.0279 W |
| CHANNEL, received-power floor (one / two polarisations) | 5.86e11 / 2.93e11 W | 4.39e6 / 2.2e6 W | 439 / 220 W |
| CHANNEL, smallest opening | 6.46e-15 m | 2.36e-12 m | 2.36e-10 m |
| COUPLING, ħJ for the whole object in T | 114 MeV | 312 keV | 3.12 keV |
| ASSEMBLE-B, reset floor (species to 0.1 Å) | 2.87 – 32.8 W | 7.86e-3 – 0.0899 W | 7.86e-5 – 8.99e-4 W |
| ASSEMBLE-B, chemical ceiling (a ceiling, not a value) | 4.17e5 W | 1.14e3 W | 11.4 W |
| POWER-B, collector for the chemical ceiling (Faria central / low L*) | 451 / 722 m² | 1.24 / 1.98 m² | 0.0124 / 0.0198 m² |

The theorem floor on reading is 0 W at every schedule (openterms T1). The probe floors hold under H-PROBE. The
reset-floor collector is under 0.04 m² at every schedule.

## What the table shows, computed

- **On energy, B's local demand is small.** At a year, a collector of under 2 m² covers the chemical ceiling at both
  of Faria's cases (1.24 and 1.98 m²). A day takes over 400 m². This agrees with `bsupply.py`'s own gathering time,
  checked to 1e-12.
- **Reading and channel cross over.** The channel's received-power floor falls as 1/T², and the read floor as 1/T.
  They are equal at T* = **10.4 years** for a 1 Å photon read, **857 years** for an electron read, and 1.58e6
  years for a neutron read. Below T* the channel floor is the larger power; above it, the read floor is. The crossover
  was checked against both owners afresh, with a control at 2T*.
- **What the energy figures do not show is throughput.** The device must read and place 2.13e20 atoms per second and
  carry 3.0e20 to 3.5e21 bits per second for a one-year transfer, or 7.8e22 atoms per second for a day. These are
  demands. Whether present instruments deliver them, or how far short they fall, is **not read here**. That is the
  supply side, and it is the next step.

## Named hypotheses

- **This file's own:** H-SCHEDULE (every rate belongs to a schedule, not to the route), H-UNIFORM-RATE, H-PARALLEL.
- **The owners':** H-PROBE, H-EM-CARRIER, H-FEW-MODES, H-ONE-POL, H-HALF-WAVE, H-RESET, H-VALENCE, H-STOCK-FORM,
  H-COLLECT, H-AT-ORBIT, H-STEADY, H-CI-PROXY, H-RETIRE-A, H-LOCALITY.

## OPEN (the supply side, none read yet)

1. READ-A: the throughput of present atom-resolving reads (bits per second, atoms per second, and damage per atom).
2. ASSEMBLE-B: the throughput of present atom-placing methods (atoms per second, with error rates).
3. CHANNEL: the rate of present deep-space links over 4.24 ly.
4. STOCK-B: phosphorus at Proxima (carried from W3-O3).
5. Every Step 1b and wave-3 OPEN item, carried in `ledger.py` as W3S1B_OPEN.
