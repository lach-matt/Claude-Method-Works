# Uses priced against the first trip (M-RULINGS item 88, link 1; deduced and computed; verified once; not seated; 2026-10-06)

*First headed* "(M-RULINGS item 88, link 1; deduced and computed; not verified; not seated; 2026-10-06)".

## What M asked

- **Item 88:** *"3 then 4 then 2 then 1 please"*. This is link 1: S5 priced per reconstruction against D23's first trip.
  After how many uses does the route beat sending the thing itself, and what does that number depend on? This is
  DOCKET 56's owed instrument, on the faithful-copy path.
- **Item 89:** *"No costlier. Stock is stock. The cost is in how much information is transferred as a README (how big
  the file is)."* Carried as H-STOCK-IS-STOCK and H-COST-IN-README.
- **Item 86, answer 4** (H-ADDRESS-INPUT): the device at position 2 is required. It must itself travel there, at or
  below c (D23).

Every number is printed by `uses.py`.
- **Selftest:** 16/16 checks, 2 genuine controls and 2 contrasts, with 7 STRUCTURAL lines printed and not counted.
  *First written* "13/13 checks, 2 genuine controls and 1 contrast". Four of those checks could not fail, including
  one "control" (History).
- **Imported, never retyped:** the break-even identity, the trip energy, the channel floor, the dishes and the Proxima
  span from `seat.py`; the identity core and the snapshot counts from `faithful.py`; the port and g(x) from
  `carrier.py`.

## What follows the work

- **1. Under your ruling, what sets the break-even is the device's mass.**
  - seat.py's identity: k\* = m_set K / (m_pay K − E_rec), with K = (γ−1)c² (H-KINETIC). As E_rec → 0, k\* → m_set/m_pay
    (sympy).
  - Under H-COST-IN-README, E_rec counts the README. Its received-energy floor for the identity core (2.74×10¹⁵ bits)
    over one year is 1.15×10⁻¹¹ J, 27 orders below the trip it replaces (3.17×10¹⁶ J for 70 kg at 0.1 c).
  - **A floor is a lower bound, so every k\* printed is a lower bound.** The floor raises k\* above the mass ratio by at
    most 4×10⁻²⁶ at the speeds computed (0.01–0.8 c).
  - Whether k\* actually stays near the mass ratio depends on the link's loss. It stays within 1 % while the
    transmitted/received factor stays below 2.7×10²⁵ (0.1 c, one year).
  - **Through one declared optical link** (1 µm, 10 THz, seat's 100 m dishes at both ends; point 7), the core costs
    6.3×10⁸ J to *transmit*: 2×10⁻⁸ of the 0.1 c trip, and 2×10⁻⁶ at 0.01 c.
  - **So the route beats sending the thing itself after about m_set / 70 kg uses, if the link loses no more than that
    budget allows.** No instrument specifies m_set (seat: "NOT SPECIFIED ANYWHERE"). The table's values are DECLARED,
    and it is seat's identity evaluated, not a finding.

  | device mass (DECLARED) | k\* (lower bound) at 0.1 c, core README, one-year schedule |
  |---|---|
  | 70 kg | 1: breaks even at the first use, beats sending from the second |
  | 700 kg | 10 |
  | 7 t | 100 |
  | 70 t | 1,000 |

  - *First written* "So the route beats sending the thing itself after m_set / 70 kg uses, at every speed computed. A
    device as heavy as the payload pays back on the first use." The floor was read as E_rec's value, and k = 1 would
    need E_rec < 0.
- **2. "How big the file is", on the received floor.**
  - On LNM's one-dimensional floor the energy goes as N²/T. Measured on the imported function: double the file and the
    cost multiplies by 4.000000; double the time and it multiplies by 0.500000.
  - Distance does not enter that floor. It enters the time budget, and the transmitted energy through the loss: the
    optical link's transmissivity falls as 1/d².
  - A real link at fixed apertures need not follow N²/T. The optical link's energy grows exponentially in the bits per
    mode-use.
  - *First written* "has an exact form" and "Distance … enters only the time".
- **3. The README has a budget, and the core is inside it on both links computed.**

  | link | README size at which k\* moves 1 % (0.1 c, one year) | above the core |
  |---|---|---|
  | received floor (lossless) | 1.4×10²⁸ bits | 12.7 orders |
  | the declared optical link (transmitted) | 2.4×10²⁰ bits | 4.9 orders |

  - The unpriced recipe, and the brain outside the cortex (faithful.py OPEN 1–2), must fit inside the budget of
    whatever link is built.
  - **H-FEW-MODES is now checked, not inherited.** At every budget there is less than one transverse mode at kT (at most
    0.265).
- **4. The snapshot is the contrast.**
  - The board's largest snapshot count (1.09×10²⁹ bits) over one year floors at 1.8×10¹⁶ J at one polarisation, and
    9.1×10¹⁵ J at two (LNM as printed).
  - **At 0.01 c either exceeds the trip it replaces (57.7× and 28.8×), so the floor alone rules S5 out on that
    schedule.**
  - At 0.1 c it raises k\* to at least 1.40 × the mass ratio (2.34 at one polarisation).
  - Over 100 years the floor no longer forbids payback.
  - **Through the optical link** the snapshot needs 3×10⁷ to 3×10⁸ bits per mode-use to arrive in one year, an energy of
    order 10^(9×10⁶) J. At 20 bits per use it needs 1.5 to 17 million years.
  - For the core, the floor forbids payback at no speed or schedule computed.
  - **On a given schedule the README's size can rule the route out. Whether it pays also needs the link's loss and,
    without H-FAB-LOCAL, E_fab. When it pays is set by the device's mass.**
  - *First written* "At 0.1 c it multiplies k\* by 2.3", "Over 100 years it pays back again", "The identity core pays
    back at the mass ratio at every speed and schedule computed", and "the README's size decides whether the route can
    pay at all, and the device's mass decides when".
- **5. Each use has a time budget, and the budget puts a floor under the route.**
  - After the first, a use beats shipping in time only when t_read + T_tx + t_build < (D/c)(1/β − 1). That is 38.2
    years at 0.1 c, 17.0 at 0.2 c, 1.06 at 0.8 c, and none at c. t_read and t_build are OPEN, and set to 0 here.
  - The budget caps T_tx, so a use that wins on time costs at least E_1d(N, budget). This lifts seat's "prices a
    schedule, not the route" for such uses.
  - **For the largest snapshot, that route floor reaches the trip below 6.8×10⁻⁴ c (5.2×10⁻⁶ c for the smallest).
    Below those speeds no use wins on both time and energy.** For the core it is negligible at every speed (at most
    4×10⁻²⁶ of the trip).
  - The 100-year schedules at 0.8, 0.2 and 0.1 c exceed their time budgets. Those uses lose on time, whatever they
    cost.
  - **Through zeromode's rotor family at the g(N) ceiling, no port fits the budget above 2.0×10⁻⁵ c (6 km/s), which
    includes every speed computed here (0.01–0.8 c).** At 10⁻⁵ c a 1.8 m rotor does fit: that is the control.
  - An electromagnetic README fits.
  - *First written* "A gravitational port never fits", which is false below 2.0×10⁻⁵ c. Before that it read "fits that
    budget at 0.1 c only for a rotor arm of 13.5 m or more (one bit per graviton)". That was zeromode's
    H-BIT-PER-GRAVITON ladder, which carrier.py's verifier found fails above an arm of 1.8 m.
- **6. The first use is no faster than the first trip,** under H-SAME-SPEED (D23 gives only ≤ c), and is later by
  t_build. *First written* "at the same speeds (D23)".

## What is not priced, as the boundary

- **The fabrication energy E_fab** is not computed anywhere on the board (seat.DOCKET56_OWED). This file reads your
  ruling as: E_fab is drawn at position 2 and is not counted against the trip (H-FAB-LOCAL). That is this file's
  reading, not your words, and it means not counted, not zero. If E_fab had to be shipped it would enter E_rec, and
  seat.erec_ceiling is the line it would have to stay under: 3.17×10¹⁶ J per use at 0.1 c. *First written* "Under your
  ruling it is drawn at position 2 from local supply (H-FAB-LOCAL)".
- **Erasure** (seat's "(+ erasure)" term; measure's H-ERASE at 310 K) is 8×10⁻⁶ J for the core and 3×10⁸ J for the
  largest snapshot. Both are named and printed, and both are negligible against the trip. *First* dropped silently.
- **The transmitted energy** is computed for one declared optical link only. Other carriers, pointing and loss beyond
  diffraction are not priced.
- **t_read and t_build** are OPEN. They sit inside point 5's time budget.
- **The comparator ignores deceleration** (H-KINETIC). A rocket equation would raise both sides and favours neither.

## For M

- **Your ruling makes the route's economics turn on one number: how heavy the device at position 2 must be.** With
  stock as stock and the cost in the README, the README is cheap on every link computed. The break-even is then at
  least the device's mass over the payload's (k\* ≥ m_set/70 kg). Through the declared optical link it is within
  2×10⁻⁶ of that. No instrument yet says what m_set is.
- **"How big the file is" bites in two ways.**
  - On the received floor the energy goes as the square of the file's size over the time allowed.
  - Through a real optical link it grows exponentially once the file needs many bits per mode-use. That is why the
    core is cheap (6.3×10⁸ J) while a full snapshot cannot be sent in a year at any energy. Over ten million years
    it can.
  - The README budget of that link is 2.4×10²⁰ bits, about five orders above the core. That is the room the recipe and
    the rest of the body have to fit into.
- **The time budget gives a route-level price.** A use has to win on time as well, so its README cannot be stretched
  over an arbitrarily long schedule. For a snapshot this rules out every use below about 7×10⁻⁴ c. For the core it is
  never binding.
- **The README should go by light.** Through zeromode's rotors it takes at least about 2×10⁵ years per copy, which
  fits the per-use budget only for trips slower than 6 km/s.

## Named hypotheses

- **M's:** H-STOCK-IS-STOCK, H-COST-IN-README (item 89); H-ADDRESS-INPUT (item 86). Carried, not decided.
- **This file's:**
  - H-FAB-LOCAL (a reading of your ruling);
  - H-LOSSLESS (the tables' transmitted = received);
  - H-README-IS-CORE;
  - H-SAME-SPEED;
  - H-OPTICAL-LINK (1 µm, 10¹³ Hz, 100 m dishes, ideal receiver: DECLARED);
  - M_SET_ILLUSTRATIVE.
- **seat's:** H-KINETIC, H-EM-CARRIER, H-ONE-POL, H-FEW-MODES (checked). **measure's:** H-ERASE.
- **faithful's:** H-WIRING-SUFFICES and the core's inputs. The core is an estimate, so every energy here is "floor given
  N".
- **carrier's:** H-BANDWIDTH-F.

## Sources

| source | route | used |
|---|---|---|
| Giovannetti, Guha, Lloyd, Maccone, Shapiro, Yuen, quant-ph/0308012v2 | alphaXiv (READ in carrier.py's pass) | g(x), the capacity (eq. 4, p.1); one mode (eq. 14, p.3); the far-field transmissivity D(ω) = A_t A_r (ω/2πcL)², "the transmissivity achieved by the optimal spatial mode" (p.3) |
| Lachmann, Newman, Moore (via `seat.py`'s READ) | board | the one-dimensional floor (eq. 8) |

## OPEN

1. m_set: the mass of the device at position 2 (DOCKET 56 owed; NOT SPECIFIED ANYWHERE).
2. E_fab, and whether it is drawn locally (H-FAB-LOCAL).
3. A link actually designed: carrier frequency, bandwidth, apertures, pointing and loss. The optical figures are one
   DECLARED case.
4. t_read and t_build.
5. The recipe's size (H-README-IS-CORE).

## History (verifier, 2026-10-06; first-written claims kept above, each where it stood)

- **The received floor was used as E_rec's value.** It is a lower bound. Every k\* is now a lower bound, and the claim
  that the route pays is conditional on the link's loss.
- **Four checks could not fail:** the trip energy against seat.erec_ceiling (the same function), the 9 × light-time
  budget, the β = 1 "control" (both the algebra of 1/β − 1), and the distance half of U3. They are now STRUCTURAL. The
  U6 control is now a speed at which a rotor *does* fit. The first control uses 1.5 × the trip, because exact float
  equality held only by rounding.
- **"A gravitational port never fits"** is now scoped to speeds above 2.0×10⁻⁵ c.
- **H-FAB-LOCAL** was written as your ruling; it is this file's reading. The erasure term is now named.
- **Also corrected:**
  - the snapshot multiplier depended on H-ONE-POL, and both polarisations are now printed;
  - H-FEW-MODES is now checked rather than inherited;
  - t_read is now in the time budget;
  - "pays back on the first use" became "breaks even at the first, beats sending from the second";
  - point 6 had cited D23 for H-SAME-SPEED.
- **Added from the verifier's estimates, now computed:** the optical link's transmitted energy and budget, and the
  route-level floor with its crossover speeds.
