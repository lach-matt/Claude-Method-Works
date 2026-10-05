# Step 1c — the device: demand, and present supply read at source (not seated; 2026-10-05)

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

## The supply side, read at source (`supply.py`, 10/10 checks, 2 controls, 3 STRUCTURAL; M item 37: "All three (Recommended)")

Every supply figure is READ, with its source, place, route and a short phrase containing the number. Every rate is
computed from the read inputs. Each gap is demand ÷ best demonstrated supply for **one instrument**, which is also the
number of such instruments that would have to run in parallel. That count is printed, not claimed buildable.

| subsystem | best demonstrated (READ) | what it actually is |
|---|---|---|
| READ-A | atom probe tomography: over 50 M ions/h at about 40 % detection, so 1.39e4 detected ions/s and 3.47e4 atoms/s removed (PNNL EMSL LEAP 4000 XHR page). A measured brittle-oxide run: 150–300 ions/s (2501.11089v1) | **destroys the specimen it reads** (field evaporation, 2603.10276v1). That is H-RETIRE-A performed by the read, with H-READ-BEFORE-DAMAGE answered in the negative for this method |
| ASSEMBLE-B | optical tweezers: 1024 atoms in a median 9.6 ms of transport, so **1.07e5 atoms/s** as an upper bound, or 1.16e4/s with the 78.6 ms detection phase (Sturm et al. 2608.12021v1, re-read by the lead). 2024 atoms in 60 ms is 3.37e4/s (2412.14647v1; its time breakdown is labelled Simulated). STM: 64 vacancies per ~10 min, so 0.107/s (1604.02265v1) | atoms held in vacuum micrometres apart, **not a bonded solid**. The STM figure moves vacancies in a Cl layer at 1.5 K and adds no atom |
| CHANNEL | DSOC: 267 Mbps at 55e6 km and **8.3 Mbps at 400e6 km** (IEEE Photonics release, re-read by the lead); 25 Mbps at 226e6 km (nasa.gov). Voyager 1: 160 bps at 2.58e13 m | carried to 4.02e16 m under H-INVERSE-SQUARE at fixed hardware (Karmous et al. 2212.04933v4 eq. 2, READ): **8.2e-4 bits/s** from DSOC's farthest point, 6.6e-5 from Voyager |

| gap (one instrument) | 1 day | 1 year | 1 century |
|---|---|---|---|
| READ-A | 2.2e18 | **6.1e15** | 6.1e13 |
| ASSEMBLE-B | 7.3e17 | **2.0e15** | 2.0e13 |
| CHANNEL | 1.3e26 | **3.7e23** | 3.7e21 |

- **The 1/d² law, tested on the measured pair.** From 55e6 km to 400e6 km DSOC's rate fell less than 1/d² predicts:
  8.3 Mbps measured against 5.05 Mbps predicted, 1.64× the law. The near point is not photon-starved, so the farthest
  point is the anchor. A synthetic pair that obeys the law reads 1.00×, so the test does not manufacture the
  departure. Under H-INVERSE-SQUARE the channel closes only if the product of transmit power and the two aperture
  areas rises by the gap (Karmous eq. 2). That is a requirement on hardware, not a design.
- **Errors at scale.** At the demonstrated per-move error of 0.4–0.7 %, assembling 6.71e27 atoms misplaces 2.5e25 to
  4.7e25 of them (H-INDEPENDENT-ERRORS). An error-free assembly would have to find and correct those.
- **Which gap is largest is a reading, not a ranking.** The three are on different quantities and are not added
  (`ledger.py` section 3). The channel gap is carried under a scaling law at fixed hardware. The read and placement
  gaps are for operations that are not the device's: destructive reading, and placement into vacuum.
- **Blocked and reported, not routed around:** Gault et al. 2021, *Nature Reviews Methods Primers* (paywall); PubMed
  (reCAPTCHA); the full text of Biswas & Srinivasan, IEEE JSTQE 32(1) (sign-in; only the open abstract was read).

## Named hypotheses (supply)

H-ONE-INSTRUMENT, H-PARALLEL-INSTRUMENTS, H-INVERSE-SQUARE, H-FIXED-HARDWARE and H-INDEPENDENT-ERRORS.

## OPEN

1. A non-destructive atom-resolving read of a bulk object at any rate. None was found; AET reads about 1e4 atoms per
   particle at doses of 1e5 e⁻/Å² or more, with no acquisition time stated.
2. Placement into a bonded solid at any demonstrated rate. Phosphorus in silicon: 12 of 12 sites, with no rate given
   (2112.12200v2).
3. A link rate measured beyond 400e6 km on optical hardware. DSOC's 494e6 km contact states no rate.
4. STOCK-B: phosphorus at Proxima (carried from W3-O3).
5. Every Step 1b and wave-3 OPEN item, carried in `ledger.py` as W3S1B_OPEN.
