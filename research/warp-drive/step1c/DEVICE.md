# Step 1c — the device: demand, present supply, the coupling route, the non-local branch and coherence (verified, corrected; seated 2026-10-05)

*Seated on M's "3, then 2. Then 1 last please" (rulings item 39): `ledger.py` docstring section 8d, M-D68-37/38/39 on RULED_BY_M, the OPEN list as S1C_OPEN. No board status moves. (First titled "not seated".)*

M ruled the order: 1a the specification theorem, 1b the balanced equation, 1c the device (`specthm.py` section 0).
M's original framing was "balancing an equation with the theory and math on one side, and the device engineering and
materials on the other side" (`ledger.py` section 0). Step 1b fixed the equation: I(A, before) = I(B, after), with
every matter and energy term an input or an output (`step1b/BALANCE.md`, seated). A device is whatever performs those
terms.

`demand.py` (6/6 checks, 2 of them controls, 4 STRUCTURAL; first 9/9 with 3 controls, see below) reads the
device's subsystems off the equation's rows and prices what each must deliver, per schedule. **Every figure is imported
from its owner.** Supply is read separately, in `supply.py` (below). M chose to read all three subsystems' supply
(rulings item 37: "All three (Recommended)"). *(First said "which subsystem comes first is M's choice", written
before M answered.)*

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
  of Faria's cases (1.24 and 1.98 m²). A day takes over 400 m². *(First said "agrees with `bsupply.py`'s own
  gathering time, checked to 1e-12". Both are E/(FT), so that is an identity, now STRUCTURAL, not an independent
  agreement.)*
- **Reading and channel cross over.** The channel's received-power floor falls as 1/T², and the read floor as 1/T.
  The **floors** are equal at T* = **10.4 years** for a 1 Å photon read, **857 years** for an electron read, and
  1.58e6 years for a neutron read. Below T* the channel floor is the larger; above it, the read floor is. This
  compares floors only: the transmitted power is not established (`seat.channel_floor`), and at these apertures it
  exceeds the received power many times over. The pattern is read off the table independently of T*: the channel
  floor is larger at a day and a year, and smaller at a century. *(The equality at T* and the "control" at 2T* follow
  from T*'s definition; they were first counted and are now STRUCTURAL.)*
- **What the energy figures do not show is throughput.** The device must read and place 2.13e20 atoms per second and
  carry 3.0e20 to 3.5e21 bits per second for a one-year transfer, or 7.8e22 atoms per second for a day. These are
  demands. Whether present instruments deliver them, or how far short they fall, is **not read here**. That is the
  supply side, and it is the next step.

## Named hypotheses

- **This file's own:** H-SCHEDULE (every rate belongs to a schedule, not to the route), H-UNIFORM-RATE, H-PARALLEL.
- **The owners':** H-PROBE, H-EM-CARRIER, H-FEW-MODES, H-ONE-POL, H-HALF-WAVE, H-RESET, H-VALENCE, H-STOCK-FORM,
  H-COLLECT, H-AT-ORBIT, H-STEADY, H-CI-PROXY, H-RETIRE-A, H-LOCALITY.

## The supply side, read at source (`supply.py`, 14/14 checks, 2 controls, 3 STRUCTURAL; M item 37: "All three (Recommended)")

Every supply figure is READ, with its source, place, route and a short phrase containing the number. Every rate is
computed from the read inputs. Each gap is demand ÷ best demonstrated supply for **one instrument**, which is also the
number of such instruments that would have to run in parallel. That count is printed, not claimed buildable. Step 1c
was verified in both directions on 2026-10-05; the findings are applied, and the first-written figures are kept below
and in each file's HISTORY.

| subsystem | best demonstrated (READ) | what it actually is |
|---|---|---|
| READ-A | atom probe tomography, an **instrument specification**: over 50 M ions/h at about 40 % detection, so **1.39e4 atoms read per s** (3.47e4 removed). PNNL EMSL LEAP 4000 XHR page. A measured brittle-oxide run reached 150–300 ions/s, 50–90 times lower (2501.11089v1) | the read removes each atom from the specimen (field evaporation, 2603.10276v1). **60 % of removed atoms are never detected, so never read.** A specimen is a needle about 100 × 100 × 300 nm, and preparing a bulk object into such needles is not priced (H-NO-PREP) |
| ASSEMBLE-B | optical tweezers: 1024 atoms in a median 9.6 ms of transport, so **1.07e5 atoms/s** as an upper bound, or 1.16e4/s with the 78.6 ms detection phase (Sturm et al. 2608.12021v1, re-read by the lead). Lin et al. (2412.14647v1): 2024 atoms took two rounds of 60 ms each, and that time is from a breakdown labelled Simulated, so 1.69e4/s as a claim. STM: 64 vacancies per ~10 min, so 0.107/s (1604.02265v1) | atoms held in vacuum micrometres apart, **not a bonded solid**. The STM figure moves vacancies in a Cl layer at 1.5 K and adds no atom |
| CHANNEL | DSOC: 267 Mbps at 55e6 km, 25 Mbps at 226e6 km and **8.3 Mbps at 400e6 km** (IEEE Photonics release, re-read by the lead; nasa.gov). Voyager 1: 160 bps at 2.58e13 m | carried to 4.02e16 m under H-INVERSE-SQUARE at fixed hardware (Karmous et al. 2212.04933v4 eq. 2, READ): **8.2e-4 bits/s** from DSOC's farthest point, 6.6e-5 from Voyager |

| gap (one instrument) | 1 day | 1 year | 1 century |
|---|---|---|---|
| READ-A (atoms read) | 5.6e18 | **1.5e16** | 1.5e14 |
| ASSEMBLE-B | 7.3e17 | **2.0e15** | 2.0e13 |
| CHANNEL (species count) | 1.3e26 | **3.7e23** | 3.7e21 |

On the 0.1 Å count the 1-year channel gap is 4.2e24. *(The READ-A gap was first computed on atoms removed: 6.1e15 at a
year. That overstated the read by 2.5×.)*

- **The 1/d² carry cuts both ways.**
  - The measured 226e6–400e6 km pair obeys 1/d² to within 4 %. The 55e6–400e6 km pair departs from it by 1.64×,
    because the near point is not photon-starved. The farthest point is the anchor, which is the choice most
    favourable to the device.
  - **Optimistic for the hardware.** At Proxima the DSOC link would receive about 6e-3 signal photons per second
    (ideal Friis, a ceiling: H-FRIIS-IDEAL). With background and dark counts, capacity falls faster than 1/d².
  - **Pessimistic against physics.** The board's own channel floor, inverted at that same received power (7.7e-22 W),
    allows about 4e6 bps. That needs quanta of any frequency to be beamable, which these apertures cannot do.
- **Linear closure is excluded.** The 1-year demand is 3.0e20 bps. That is above the 1550 nm carrier frequency
  (1.93e14 Hz), and the link has 1.9e-22 transverse modes: Karmous eq. 3's bandwidth saturation. Against the board's
  channel floor (any carrier), the received power would have to rise by **at least 5.7e27** at a year (7.6e32 at a day,
  5.7e23 at a century). That is more than the rate gap. The floor's quantum at a year is 2.63e5 eV (`aperture.py`),
  against 0.80 eV at 1550 nm (H-FIXED-CARRIER). *(First said "closes only if the product of transmit power and the two
  aperture areas rises by the gap". That assumed rate linear in received power, which these figures exclude.)*
- **Errors at scale, on one basis.** Kalff's 1 wrong hop in 264 is a raw per-hop error, which the program corrected by
  re-planning. A vacancy took 264/64 = 4.1 hops, so the raw error per placement is 1.55 %. The tweezers' figure is
  0.7 % per move. Over 6.71e27 atoms that is **4.7e25 to 1.0e26 misplaced** (H-INDEPENDENT-ERRORS), which an
  error-free assembly would have to find and correct. *(First printed as "0.4–0.7 % per move", which mixed a per-hop
  figure with per-move ones.)*
- **What the read does, stated without overreach either way.** Atom probe tomography reads each detected atom as it
  removes it, so destruction itself is not H-READ-BEFORE-DAMAGE's failure. That hypothesis concerns damage that
  scrambles the configuration before it is read. What fails is that 60 % of the atoms are removed unread, plus
  reconstruction error. The ions on the detector are stock in neither H-STOCK-FORM form, so the read does not perform
  H-RETIRE-A. *(First said "H-RETIRE-A performed by the read" and "H-READ-BEFORE-DAMAGE answered in the negative".
  The first overstated for M, the second against.)*
- **Which gap is largest is a reading, not a ranking.** The three are on different quantities and are not added
  (`ledger.py` section 3). The read and placement gaps are for operations that are not the device's.
- **Blocked and reported, not routed around:** Gault et al. 2021, *Nature Reviews Methods Primers* (paywall); PubMed
  (reCAPTCHA); the full text of Biswas & Srinivasan, IEEE JSTQE 32(1) (sign-in; only the open abstract was read).

## The coupling route (`coupling.py`, 9/9 checks, 2 controls, 3 STRUCTURAL; M item 38: "Take the coupling route"; verified once, corrected)

This sets the channel aside and prices the wave-3 coupling as the device's link: H = J(|A⟩⟨B| + |B⟩⟨A|), with transfer
time π/(2J) (`corridor.py`).

- **What locality bounds is time, not J.** Wave 3 showed the coupling is a channel: under a fixed J, A's starting
  state changes B's statistics.
  - An **instantaneous** coupling across L gives B the probability sin²(Jt) > 0 before L/c, at every J > 0. At the
    century J (4.98e-10 rad/s per pair), B holds 4.4e-3 by L/c: a signal outside the light cone.
  - So under H-LOCALITY an instantaneous coupling across 4.24 ly is excluded **at every J**. That includes one set up in
    advance, because A's state alone signals; H-PREESTABLISHED does not rescue it.
  - A **retarded** coupling is allowed at any J and completes no sooner than L/c = 4.25 years. Schedules shorter than
    that are excluded whatever J is.
  - The 4.25-year threshold is the light time, not an engineering limit. `corridor.before_light`'s πc/(2L)
    (ħJ = 7.7e-24 eV) is where an instantaneous coupling would *complete* before light. It is not a ceiling on J.
- **The demand.**
  - **Parallel:** I couplings, one per qubit, each spanning L, at J = π/(2T) per pair.
  - **Serial:** one coupling carrying all I qubits at J = I·π/(2T): 312 keV at a year, 3.12 keV at a century (species
    count).
- **The supply, read at source.** The only direct couplings measured, with no carrier between the qubits, are
  near-field dipolar exchange falling as 1/R³, measured out to **50 µm or less**:
  - Rydberg atoms: C3 = 7950 ± 130 MHz·µm³ (Barredo et al. 1408.1055v2, re-read by the lead). It reproduces their
    measured 0.52 MHz swap at 30 µm within the paper's 5 % calibration of R.
  - Magnetic dipole between two ions: J/2π ≈ 1.8 mHz at 2.4 µm (Kotler et al. 1312.4881v1).
- **Where the direct law stops.** The 1/R³ law holds only at distances small compared with the transition's wavelength.
  The boundary is λ/2π: **5.2 mm** for Barredo's 9.131 GHz transition and **3.9 m** for Kotler's 12.34 MHz splitting.
  - Beyond it, the coupling is the retarded far-field term. At L that is J_far = 2πC3k²/L = **4.6e-20 rad/s** for
    Barredo's parameters (H-FAR-FIELD-ORIENTATION): **1.1e10 short** of the century demand per pair.
  - It acts only after L/c: it is photon exchange, which is the channel M set aside.
  - **Over years it is void (H-COHERENCE).** The Rydberg state decays at about 1e4 per second, 2.2e23 times J_far,
    so the log of the survival probability over a century is −3.1e13. No coherence time is priced anywhere else on
    the board, and leaving it unpriced would have flattered the century schedule.
- **What a near-field coupling at L would take, computed.**
  - For λ/2π to equal L, the transition would have to be at 1.19 nHz or below (a period of 27 years).
  - For near-field exchange to give the century J at L, the dipole would have to be 0.0195 C·m. For charge e, that is
    a separation of 1.2e17 m, which is **3.0 times L itself**.
- **Mediated couplings are not direct.**
  - Phonon-mediated ion couplings (α 0.63–1.19 measured; 0–3 claimed, Richerme et al. 1401.5088v1) need the crystal
    to span L (H-MEDIATOR-SPANS). No ion spacing was read, so they are not carried.
  - Photon-mediated remote transfer over 5 m (Magnard et al. 2008.01642v1) is a channel. Its 28 ns propagation is
    estimated from group velocities, not measured.
- **So the coupling route, priced.** Under H-LOCALITY it reduces to the channel: retarded, at the light time or
  later, with the far-field coupling strength above. Without locality, through an instantaneous coupling
  (H-DIRECT-COUPLING), any J serves, which is the clash wave 3 named.
- **Hypotheses:** H-LOCALITY, H-PREESTABLISHED (shown not to rescue an instantaneous coupling), H-NEAR-FIELD,
  H-FAR-FIELD-ORIENTATION, H-COHERENCE, H-MEDIATOR-SPANS, H-DIRECT-COUPLING and H-STATE-AS-BITS.
- **History (first written, kept):**
  - "J ≤ πc/(2L)" was stated as a locality ceiling on J, with "a century is not excluded". That is **withdrawn** for an
    instantaneous coupling: the verifier showed it signals at that J.
  - The best direct coupling was carried to L by 1/R³ as 7.7e-58 rad/s, "6.5e47 short". That carry is outside the
    law's validity, and it understated the coupling by (kL)² = 5.9e37.
  - "No present mechanism couples two qubits directly beyond millimetres" was replaced by the measured range and the
    dipole argument.
  - Four counted checks were identities or duplicates.
  - A guessed threshold failed.
  - Two ids in the reader's brief were wrong.

## The non-local branch, as M's hypothesis (`nonlocal.py`, 7/7 checks, 1 control, 5 STRUCTURAL; M item 39: "3, then 2. Then 1 last please"; verified once, corrected)

**H-NONLOCAL-COUPLING:** an instantaneous term J(|A⟩⟨B| + |B⟩⟨A|) across spacelike L. It is wave 3's H-DIRECT-COUPLING
with H-LOCALITY dropped. It is linear quantum mechanics with a non-local Hamiltonian, and not H-SETTLE, which is
nonlinear and local: that is the board's other signalling branch, with its own bounds from wave 2.

- **What it would have to be.**
  - **A channel, at any J.**
  - **Free of causal loops.** This rests on latticectc's H1–H3, with each coupling carried as a translation
    identification of the two positions (H-CORRIDOR-MAP, newly named). Two couplings close a loop **iff their span is
    timelike, i.e. iff no single frame makes both simultaneous**. Asked of latticectc's search: its witnesses close
    one, and a spacelike-span pair keyed to different frames does not. Loop-freedom therefore needs every coupling
    simultaneous in one common frame, which is M's H-FRAME.
  - **For the device:** 9.5e27 couplings each spanning L, at 4.98e-10 rad/s per pair for a century or 1.82e-5 for a
    day.
- **What it contradicts.** It contradicts relativistic microcausality. It does not contradict non-relativistic linear
  quantum mechanics, which routinely carries instantaneous terms. **But those are approximations of a retarded field
  theory, so the non-contradiction carries no evidential weight for the hypothesis.** It does not contradict
  `nosig.py`, which concerns entanglement without a coupling term.
- **What measurement would test it.** There are two protocols and two maps.
  - **Spacelike** (t ≤ r/c), at the century J, with trials = 4/δ² for two settings at 2σ:
    - second-order map, δ = sin²(Jt): δ = 4.4e-3 at L (2.0e5 trials), 4.1e-19 at Earth–Moon;
    - first-order map, δ ≈ Jt: 6.4e-8 at Earth–Moon (9.8e14 trials), 2.5e-5 at 1 au.
  - **Timelike**, under H-J-DISTANCE-FREE with crosstalk controlled: at the day J a full transfer takes one day at any
    separation, so a local test is possible. Its burden is shutting out every retarded channel.
- **What present tests allow.** These are the measured no-signalling checks of spacelike Bell tests, read at source;
  every bound is conditional.
  - **Readings A/B** (population transfer): J ≤ **6.6e3–6.9e3 rad/s** (NIST; which data aggregate is OPEN, so both are
    printed), up to 6.95e5 (Vienna, reading B).
  - **Reading C** (first order): **J ≤ 11.2 rad/s** (Vienna) and 13.2 (NIST).
  - The tightest is **3.6e8×** the day demand per pair under A/B and **6.1e5×** under C. So present tests do not exclude
    H-NONLOCAL-COUPLING at the device's strength, under these conditions:
    - H-J-DISTANCE-FREE;
    - H-SETTING-DEPENDENCE: if Alice's photon is present under both settings, a test bounds nothing;
    - H-UNIVERSAL-COUPLING: the Bell-test systems carry the device's coupling at all;
    - H-LAB-FRAME: the preferred frame must move below 0.80–0.98c along each test's axis.
  - **If J falls with distance as r^−α, the tightest bound carried to L excludes the device for α > 0.60 (day) or
    α > 0.92 (century).** Whether the speed-free routes make J distance-free is OPEN. Eldredge's L-independence is a
    collective many-site effect, not a distance-free pairwise J.
  - Munich's Apr 7 run shows a 2.5σ marginal difference (p = 0.014). The authors read it as no evidence of signalling,
    and it is recorded as such. Delft reports no statistic in its main text.
- **The speed-of-influence bounds** (Salart 2008, ≥ 5.4e4 c; Yin 2013, ≥ 1.38e4 c) are lower bounds on v. Bancal et
  al. (1110.3795, read by the verifier) show any finite-speed model of correlations signals. **A lower bound on v
  cannot exclude v = ∞ in a preferred frame**, so these bounds do not exclude the branch. Bancal names the CMB frame
  and finds no evidence ruling a privileged frame out, which supports carrying H-FRAME.
- **Hypotheses:** H-NONLOCAL-COUPLING, H-FRAME, H-CORRIDOR-MAP, H-SPACELIKE-WINDOW, H-J-DISTANCE-FREE, H-COUPLING-MAP
  (readings A, B, C; none favoured), H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING, H-LAB-FRAME and H-SHOT-NOISE.
- **Carried as a hypothesis, neither shown nor dismissed.**
- **History (first written, kept):**
  - "Two couplings keyed to different frames close a loop" was too broad.
  - "Testable only at separations comparable to L" holds only for the spacelike protocol under the second-order map.
  - Trials were first computed as 1/(4δ²).
  - The bounds were first stated without their conditions or reading C (3.8e8× first, 6.1e5× under C).
  - "True of the speed-free routes" is now OPEN.
  - The speed bounds were first set aside for the wrong reason.
  - Three counted checks were identities.

## H-COHERENCE, priced (`coherence.py`, 8/8 checks, 1 control, 3 STRUCTURAL; M item 39, part 2; verified once, corrected)

- **Where coherence is a demand: it depends on the arrangement and the payload.**
  - **Under R-QUANTUM**, put the pair source a distance x from Alice. Bob's stored hold is **2x/c**:
    - **0** with the source at Alice. Bob's half is then in flight for L/c, and flight in vacuum does not dephase
      (H-VACUUM-FLIGHT), so the burden moves to loss, which is the link budget's.
    - **L/c** at the midpoint (H-MIDPOINT-SOURCE).
    - **2L/c** with the source at Bob.
  - **Under H-STATE-AS-BITS**, Bob measures in the computational basis on arrival and corrects the recorded outcome
    later, so his hold is 0 at any x.
  - So **a stored hold is a demand only for a quantum payload with the source away from Alice.**
  - The retarded coupling route must stay coherent for the whole interaction, π/(2J_far) = 3.5e19 s, far beyond L/c.
  - **Under R-CLASSICAL**, dephasing sets no demand. Storing bits carries classical retention costs, correctable
    without a capacity cliff (H-CLASSICAL-RETENTION).
- **The demand at the midpoint hold, by overhead k** (encoded qubits per logical qubit, so k also multiplies the
  memories). The capacity is 1 − h₂(p). The dephasing channel is degradable (Devetak & Shor quant-ph/0311131v3, read
  by the verifier); the closed form is computed here.

| overhead k | T2 needed | × the best measured (180 min) |
|---|---|---|
| 2 | 5.4e8 s (17 yr) | 5.0e4 |
| 1e6 | 2.0e7 s | 1.8e3 |
| 1e12 | 9.8e6 s | 909 |
| 1e27 | 4.3e6 s | 401 |
| 1e100 | 1.2e6 s | 108 |

  Without correction, keeping all 9.5e27 qubits intact needs T2 ≥ 6.4e35 s.
- **The supply, read at source.**

| memory | T2 | how obtained | qubits |
|---|---|---|---|
| ³¹P⁺ in ²⁸Si, 1.2 K (Saeedi et al. 2303.17734v1, re-read by the lead) | 180 min | measured single exponential; a lower bound (pulse errors) | ensemble, one stored state |
| ³¹P⁺ in ²⁸Si, 298 K | 39 min | measured; a lower bound | ensemble |
| ¹⁵¹Eu³⁺:Y₂SiO₅ spin (Ma et al. 2012.14605v3) | 2.68 h | measured (CPMG) | ensemble, one mode |
| ¹⁵¹Eu³⁺:Y₂SiO₅ (Zhong et al. 2015) | 370 min | abstract only (Nature paywalled) | ensemble |
| one ¹⁷¹Yb⁺ ion (Wang et al. 2008.00251v1) | 5487 s | **extrapolated** from data out to ~16 min | 1 |
| 6139 Cs atoms (Manetsch et al. 2403.12021v4) | 12.6 s | measured, under XY16 at reduced depth (3.19 s at full depth) | 6139 |

- **The gap.** The midpoint hold spans 1.24e4 e-folds of the best measured T2. Every memory reaches capacity 0, and the
  best falls short by 108 to 5e4 across overheads from 2 to 1e100.
- **Bias, stated.**
  - The pure exponential is lenient to the memory: a stretched decay falls faster.
  - The spins per ensemble-stored qubit are unpriced (H-ENSEMBLE-PER-QUBIT), which favours the device.
  - Every T2 above is measured under active dynamical decoupling, which is control, not correction.
- **H-NO-REFRESH and what it hides.** Active fault-tolerant correction below threshold gives logical lifetimes that grow
  exponentially with code distance, so years are not excluded in principle. The open question is an operations and
  energy demand on 9.5e27 × k physical qubits (H-FT-MEMORY, OPEN, unpriced).
- **Hypotheses:** H-STORED-HOLD, H-MIDPOINT-SOURCE (a choice, not the minimum), H-VACUUM-FLIGHT, H-PURE-DEPHASING,
  H-EXP-DECAY, H-DEPHASING-CAPACITY, H-NO-REFRESH, H-FT-MEMORY, H-ENSEMBLE-PER-QUBIT, H-CLASSICAL-RETENTION and
  H-STATE-AS-BITS.
- **History (first written, kept):**
  - "H-MIDPOINT-SOURCE, the arrangement that minimises the hold" was wrong: a source at Alice gives 0.
  - "The retarded coupling route has the same hold" understated it.
  - "5.0e4 short" rested on overhead 2 alone.
  - The capacity was first marked named-not-read.
  - Two identities were counted, and a control did not exercise its check.
  - "1.24e4 e-folds short of the hold" was mis-worded.
  - The reader's brief carried a wrong id: 1301.6567 is Wolfowicz et al.; Saeedi et al. is 2303.17734v1.

## Named hypotheses (supply)

H-ONE-INSTRUMENT, H-PARALLEL-INSTRUMENTS, H-INVERSE-SQUARE, H-FIXED-HARDWARE, H-FIXED-CARRIER, H-FRIIS-IDEAL, H-NO-PREP
and H-INDEPENDENT-ERRORS.

## OPEN

1. An atom-resolving read of a bulk object that reads every atom it removes, or removes none, at any rate. None was found; AET reads about 1e4 atoms per
   particle at doses of 1e5 e⁻/Å² or more, with no acquisition time stated.
2. Placement into a bonded solid at any demonstrated rate. Phosphorus in silicon: 12 of 12 sites, with no rate given
   (2112.12200v2).
3. A link rate measured beyond 400e6 km on optical hardware. DSOC's 494e6 km contact states no rate.
4. STOCK-B: phosphorus at Proxima (carried from W3-O3).
5. Every Step 1b and wave-3 OPEN item, carried in `ledger.py` as W3S1B_OPEN.
