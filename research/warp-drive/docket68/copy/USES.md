# Uses priced against the first trip (M-RULINGS item 88, link 1; deduced and computed; not verified; not seated; 2026-10-06)

## What M asked

- **Item 88:** *"3 then 4 then 2 then 1 please"*. This is link 1: S5 priced per reconstruction against D23's first trip.
  After how many uses does the route beat sending the thing itself, and what does that number depend on? This is
  DOCKET 56's owed instrument, on the faithful-copy path.
- **Item 89:** *"No costlier. Stock is stock. The cost is in how much information is transferred as a README (how big
  the file is)."* Carried as H-STOCK-IS-STOCK and H-COST-IN-README.
- **Item 86, answer 4** (H-ADDRESS-INPUT): the device at position 2 is required. It must itself travel there, at or
  below c (D23).

Every number is printed by `uses.py`.
- **Selftest:** 13/13 checks, 2 genuine controls and 1 contrast, with 4 STRUCTURAL lines printed and not counted.
- **Imported, never retyped:** the break-even identity, the trip energy, the channel floor and the Proxima span from
  `seat.py`; the identity core and the snapshot counts from `faithful.py`; the port from `carrier.py`.

## What follows the work

- **1. Under your ruling, the break-even is a mass ratio.**
  - seat.py's identity: k\* = m_set K / (m_pay K − E_rec), with K = (γ−1)c² (H-KINETIC). As E_rec → 0, k\* → m_set/m_pay
    (sympy).
  - Under H-COST-IN-README, E_rec counts the README only. Its received-energy floor for the identity core (2.74×10¹⁵
    bits) over one year is 1.15×10⁻¹¹ J (seat.channel_floor, LNM's one-dimensional law).
  - That is 27 orders below the trip it replaces: 3.17×10¹⁶ J for 70 kg at 0.1 c.
  - **So the route beats sending the thing itself after m_set / 70 kg uses, at every speed computed.** A device as
    heavy as the payload pays back on the first use; one a thousand times heavier pays back after a thousand.
  - What moves k\* is the device's mass, and no instrument specifies it (seat: m_set "NOT SPECIFIED ANYWHERE"). The
    values in the table are DECLARED illustrations.

  | device mass (DECLARED) | k\* at 0.1 c, core README, one-year schedule |
  |---|---|
  | 70 kg | 1 |
  | 700 kg | 10 |
  | 7 t | 100 |
  | 70 t | 1,000 |

- **2. "How big the file is" has an exact form.**
  - On the one-dimensional floor the energy goes as N²/T. Measured on the imported function: double the file and the
    cost multiplies by 4.000000; double the time and it multiplies by 0.500000.
  - Distance does not enter that floor (×1.000000 at ten times the distance). It enters only the time.
- **3. The README has a budget, and the core is far inside it.**
  - Over one year, the file can grow to 1.4×10²⁸ bits at 0.1 c (1.4×10²⁷ at 0.01 c) before its cost moves k\* by 1 %.
  - The unpriced recipe, and the brain outside the cortex (faithful.py OPEN 1–2), fit inside that unless they exceed
    the core by more than twelve orders at 0.1 c.
  - **Loss budget.** The floor is for *received* energy. The transmitted energy, with diffraction loss, may exceed it by
    a factor of 2.7×10²⁵ (0.1 c, one year) before k\* moves by 1 %.
- **4. The snapshot is the contrast.**
  - The board's largest snapshot count (1.09×10²⁹ bits) over one year costs 1.8×10¹⁶ J on the same floor.
  - At 0.01 c that exceeds the trip it replaces, so on that schedule S5 never pays back. At 0.1 c it multiplies k\* by
    2.3.
  - Over 100 years it pays back again (k\* = 2.4 × the mass ratio at 0.01 c), since the floor falls as 1/T.
  - The identity core pays back at the mass ratio at every speed and schedule computed.
  - **On a given schedule, the README's size decides whether the route can pay at all, and the device's mass decides
    when.**
- **5. Each use has a time budget.**
  - After the first, a use beats shipping in time when transmission plus build is less than (D/c)(1/β − 1).
  - That gives 38.2 years at 0.1 c, 17.0 at 0.2 c, 1.06 at 0.8 c, and none at c.
  - **A gravitational port never fits.** carrier.py's fastest rotor loads the core in 6.7×10¹² s at the capacity
    ceiling, past even the 0.01 c budget of 420 years.
  - An electromagnetic README fits, because its transmission time is a schedule, chosen against point 2's 1/T.
  - *First written* "fits that budget at 0.1 c only for a rotor arm of 13.5 m or more (one bit per graviton)". That was
    zeromode's H-BIT-PER-GRAVITON ladder, which carrier.py's verifier found fails above an arm of 1.8 m.
- **6. The first use is no faster than the first trip.** The device must arrive first, at the same speeds (D23).

## What is not priced, as the boundary

- **The fabrication energy E_fab** is not computed anywhere on the board (seat.DOCKET56_OWED).
  - Under your ruling it is drawn at position 2 from local supply (H-FAB-LOCAL), so it is not in E_rec.
  - If it had to be shipped it would enter E_rec, and seat.erec_ceiling is the line it would have to stay under:
    3.17×10¹⁶ J per use at 0.1 c.
- **The transmitted energy** is not floored (seat's H-FEW-MODES). Point 3's loss budget states how large the loss may be.
- **The build time t_build** is OPEN. It sits inside point 5's time budget.
- **The comparator ignores deceleration** (H-KINETIC). A rocket equation would raise both sides, and favours neither.

## For M

- **Your ruling makes the route's economics simple.** Once stock is stock and the cost is the README, the README is so
  cheap that the break-even is the device's mass over the payload's: k\* = m_set/70 kg. The question that decides
  when the route pays is how heavy the device at position 2 must be. No instrument answers that yet.
- **"How big the file is" has a precise form: the energy goes as the square of the file's size over the time allowed.**
  The core sits more than twelve orders inside the budget. A full snapshot can stop the route paying at all on a short
  schedule.
- **The README should go by light, not by a gravitational port.** Through the port it takes at least about 2×10⁵ years
  per copy, against a per-use budget of decades.

## Named hypotheses

- **M's:** H-STOCK-IS-STOCK, H-COST-IN-README (item 89); H-ADDRESS-INPUT (item 86).
- **This file's:** H-FAB-LOCAL; H-README-IS-CORE (the README's size is the cortical core, and the recipe is not
  priced); H-SAME-SPEED (the device travels at the payload's speed, as seat's identity assumes); M_SET_ILLUSTRATIVE.
- **seat's:** H-KINETIC, H-EM-CARRIER, H-ONE-POL, H-FEW-MODES. **faithful's:** H-WIRING-SUFFICES and the inputs of the
  core. **carrier's:** H-BANDWIDTH-F.

## Sources

No new outside source. Every outside number comes through an owner that READ it: LNM via `seat.py`, Giovannetti et al.
via `carrier.py`, and the identity core's inputs via `faithful.py`.

## OPEN

1. m_set: the mass of the device at position 2 (DOCKET 56 owed; NOT SPECIFIED ANYWHERE).
2. E_fab, and whether it is drawn locally (H-FAB-LOCAL).
3. The transmitted energy of the README link, with diffraction (the loss budget is computed; the loss is not).
4. t_build, the time to construct a copy.
5. The recipe's size (H-README-IS-CORE).
