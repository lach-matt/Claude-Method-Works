# A carrier through the bulk (M-RULINGS item 88, link 2; deduced, computed and READ; not verified; not seated; 2026-10-06)

## What M asked

- **Item 88:** *"3 then 4 then 2 then 1 please"*. This is link 2: a carrier through the bulk (O6), measured against
  D13, which says information travels at or below c in the metric its carrier propagates in.
- **Item 89:** *"The cost is in how much information is transferred as a README (how big the file is)"*, carried as
  H-COST-IN-README.

The faithful copy's README (`faithful.py`: an identity core of order 10¹⁵ bits) has to cross from position 1 to
position 2. A carrier through the bulk moves in the bulk's metric, so D13 alone does not bound it on our plane.

Every number is printed by `carrier.py`.
- **Selftest:** 7/7 checks, 1 genuine control and 1 contrast, with 2 STRUCTURAL lines printed and not counted.
- **Imported:** the port rate from `zeromode.py` and the identity core from `faithful.py`.

## What follows the work

- **1. The condition for a faster-than-light corridor is now named exactly.**
  - A path through the bulk between two points of one plane can arrive before light along the plane only if the bulk
    breaks the plane's 4D Poincaré symmetry. That means one of three things:
    - time and space are warped differently;
    - the bulk is compact, with the planes moving relative to each other;
    - the bulk changes in time.
  - **Computed, exactly:** in every static bulk that keeps that symmetry, every causal curve obeys |dx| ≤ dt in the
    plane's coordinates. That holds for one warp factor on the plane's coordinates, with any number of extra
    dimensions: RS1 (ours under H-RS1), RS2, and ADD's flat bulk. On a null curve, (dx/dt)² = 1 − g dy² e⁻²ᴬ/dt².
  - **Checked numerically:** random causal curves in RS1's warp and in a two-dimensional warp never exceed 1.
  - **Control:** warp time and space differently, and the same test finds a shortcut (|dx|/dt = 1.41).
  - **So your corridor, if it beats light, is a place where the bulk is warped unequally for time and space.**
- **2. The corridor must be local, not a property of the whole bulk.**
  - Gravitons are the bulk carrier RS1 has. Those from GW170817 arrived with light: the speed difference is between
    −3×10⁻¹⁵ and +7×10⁻¹⁶ of c, over at least 26 Mpc (READ).
  - A bulk warped unequally everywhere would have shown there. A corridor confined to a device's neighbourhood need
    not.
  - On the Proxima line, a global asymmetry could save at most 9.4×10⁻⁸ s (H-BOUND-TRANSFERS).
- **3. The port is where your cost lands.**

  | gravitational port (zeromode's rotor, same tip speed and density) | time to load the identity core (2.74×10¹⁵ bits) |
  |---|---|
  | 1 m | 5.4×10¹⁴ s (17 million years) |
  | 10 m | 5.4×10⁹ s |
  | 100 m | 5.4×10⁴ s |
  | 1 km | 0.54 s |

  - These assume one bit per graviton (zeromode's H-BIT-PER-GRAVITON).
  - Under H-COST-IN-README the trip's cost is this port time, and it scales with the README. The faithful copy's
    3.5×10¹²-fold reduction is exactly the factor between loading the snapshot and loading the core.

## What is ruled out, as the boundary

- **In RS1 as the board seats it, the README crosses at or below c.** RS1 keeps 4D Poincaré symmetry by construction:
  the tensions are "required in order to obtain a solution that respects four-dimensional Poincare invariance", as
  `crossing.py` READ it. So D13 extends to bulk carriers in every such bulk, and the trip takes the port time plus at
  least the light time.
- **The escape classes are the board's own open items.**
  - A bulk warped unequally needs an exotic bulk fluid to keep Newton's law on our plane (BULK3-O5), and may need NEC
    violation somewhere (BULK2-O2).
  - A compact bulk with moving planes needs our boost relative to the preferred frame, which is unmeasured (O7).
  - A time-dependent bulk is not modelled.

## For M

- **This turns your corridor into a geometric condition that can be tested.** It must warp time and space unequally,
  and do so locally. Everything else the bulk does keeps the README at light speed.
- **The cost sits at the port, as you said.** It is set by the README's size: millions of years through a lab-scale
  gravitational emitter, about half a second through a kilometre-scale one. Detecting single gravitons at the far end
  is unpriced.

## Named hypotheses

- **H-STATIC-WARP**; **H-RS1** (carried); **H-BOUND-TRANSFERS**; **H-BIT-PER-GRAVITON** (zeromode's).
- **M's:** H-COST-IN-README, H-ADDRESS-INPUT, H-INFORMATION-CROSSES.

## Sources READ

| source | route | used |
|---|---|---|
| LIGO–Virgo, Fermi-GBM, INTEGRAL, 1710.05834v2 | alphaXiv | the speed bound (abstract p.1; eq. 1, p.6, D = 26 Mpc, a 10 s emission window); the 1.74 ± 0.05 s delay (p.1) |
| Randall–Sundrum (via `crossing.py`'s READ) | board | the 4D Poincaré invariance the tensions are required for |

## OPEN

1. A corridor geometry that breaks the symmetry locally, with its energy conditions (with BULK2-O2 and BULK3-O5).
2. A time-dependent bulk.
3. A port faster than gravitational emission: the stabilisation scalar (BULK3-O3), or the planes' own fields at the
   corridor's mouth.
4. One bit per graviton, at sending and at receiving (detecting single gravitons).
5. In a bulk that keeps the symmetry, the trip takes the port time plus at least the light time.
