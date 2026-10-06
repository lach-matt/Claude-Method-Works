# How the corridor opens and closes (M-RULINGS item 113, second of three; deduced, computed and READ; verified once; SEATED (ledger.py section 8o); 2026-10-06)

*Seated in ledger.py section 8o on M's order of work (item 113); until then headed "… not seated …".*

*First headed* "(…; not verified; not seated; 2026-10-06)".

## What M said

- **Item 106:** *"Three distinct holds in one fluid wave motion, horizon position 1 only as the corridor opens, … upon
  the corridor closing the bits are then held only at the horizon of position 2"*.
- **Item 109:** *"A horizon cannot exist without the object of which it needs to exist"*.
- **Item 110:** *"Into position 2"*.
- **Item 111:** *"one energy read from two sides"*.
- **Item 86, answer 5:** *"however long is dictated for the travel. I suspect it is incredibly short, maybe even
  immeasurable but not zero. And this answer is also a relative one."*

Every number is printed by `opening.py`.
- **Selftest:** 6/6 checks, 2 genuine controls, with 7 STRUCTURAL lines printed and not counted.
- *First written* "7/7 checks, 2 genuine controls". Four of those checks restated two others, and their controls could
  not fail.

**The board's reading (R-VAIDYA-HOLDS, ungraded).** Each transition is modelled as null dust: radiation moving at light
speed, your "fluid wave". The metric is Vaidya's form, written here and computed; nothing about it is READ.
- **Opening, at position 1:** energy falls in, and the mass rises from 0 to the floor.
- **Closing, at position 2:** energy flows out, and the mass falls back to 0.

## What follows the work

- **1. Each piece satisfies every energy condition, when its mass runs the way you said.**
  - Falling in, the only nonzero component of the Einstein tensor is G_vv = 2m′/r². Flowing out, it is
    G_uu = −2m′/r² (sympy).
  - The matter is radiation moving in one direction, so its energy as seen along any direction has one sign. So the
    null, weak, strong and dominant energy conditions all hold exactly when the mass rises at the opening and falls at
    the closing.
  - Controls: the code's tests fail for radiation with charge (extra components appear) and for radiation in a universe
    with Λ (R = 4Λ).
  - *First written:* "the only curvature component is G_vv". It is the only Einstein-tensor component; the Weyl tensor
    is nonzero. The energy condition was tested only along radial directions.
- **2. Each piece has R = 0.**
  - Bronnikov–Kim's corridor has R = 0 too, but as vacuum on the brane, not as traceless matter.
  - Across the joins, R stays zero only if the join's surface stress is traceless (H-JUNCTION, OPEN).
  - *First written:* "The whole sequence … stays in the R = 0 class".
- **3. The corridor itself breaks the null energy condition on both sides of its horizon, so the joins are where that
  violation enters.**
  - For eq. (17), G^r_r − G^t_t = −2(2r₀ − 3m)(r − 2m)/(r²(2r − 3m)²) (sympy).
  - For the horizon members, the radial null condition fails at every radius except the horizon itself: outside it, and
    inside it, where the roles of time and radius swap. The density is still positive.
  - The radiation pieces end in an ordinary black hole of the same mass, not in the corridor. The corridor's exterior
    carries the violating stress out to infinity. So getting from the opening to the corridor still needs that
    violation.
  - D7 (a quantum limit on how long negative energy can be held) is met trivially by the radiation pieces, and it is
    silent on your main path anyway (LEDGER M-D68-87).
  - *First written:* "Unlike the corridor's static neck, neither transition needs negative energy, so … (D7) does not
    bind them".
- **4. The energy: in equals out by construction, and which mass is OPEN.**
  - Both mass functions run between 0 and the same final mass, by construction.
  - With that mass set by the floor, it is 4.59404002×10⁸ J × √N, or 2.405878326×10¹⁶ J for the core.
  - If the opening must supply the corridor's total (ADM) energy instead, that is up to 5/4 of it (PLANE.md point 2;
    H-MF-IS-AREA-MASS).
  - Position 2's horizon ends when its mass reaches zero. That is imposed by setting the mass to zero, matching your
    item 109.
- **5. A floor on the opening's duration, under a published conjecture.**
  - Barrow & Gibbons, 1408.1820v3 p.2 eq. 2 (READ by a verifier): *"the closely related conjecture that there is a
    maximum power defined by P_max = cF_max = c⁵/4G, the so-called Dyson Luminosity … or some multiple of it to account
    for geometrical factors O(1)"*. On p.3 the factor *"does not seem to be so precisely determined"*.
  - The conjecture bounds radiation reaching infinity. Applying it to inflow is the board's extension
    (H-MAX-POWER-INFLOW).
  - Then the opening lasts at least
    **2r_min/c = √(2N h G ln2/(π² c⁵)) = 0.9394372787 t_P √N = 5.0647×10⁻⁴⁴ s × √N**, where t_P is the Planck time.
    That is **2.652×10⁻³⁶ s** for the core.
  - With the Planck luminosity c⁵/G as the limit instead, it is 6.631×10⁻³⁷ s, so the bound is uncertain by a factor
    of 4.
  - This is a floor on the opening, beside your answer 5. The hold itself is *"however long is dictated for the
    travel"*, and relative. The time is measured at position 1 (H-HOLD-FRAME).
  - For a README of only a few bits the bound falls below the Planck time, and the model no longer applies.
  - *First written:* "your item 86 answer 5, computed"; and "extending it to power … is the board's step", although
    maximum power is READ, as a conjecture.
- **6. The closing is not bounded by that conjecture.** Cardoso et al., 1803.03271v2 App. B p.9 (READ by a verifier),
  treat outflow of exactly this kind: *"The luminosity of this spacetime … is unbounded … not a counter-example …
  because the radiation comes out of a past horizon"*. Position 2's closing is that case, a white hole.
- **7. The horizon holds the README only as it grows.**
  - During the opening, the horizon at r = 2m is still growing, so it is not yet a fixed surface.
  - Under H-HORIZON-HOLDS (taken as the apparent horizon), its capacity is N × (m/m_final)². So the whole README sits on
    position 1's horizon only at the end of the opening.
  - At the closing it shrinks as (1 − f)² N, where f is the fraction of the energy already emitted. That forces position
    2 to read the README before its horizon ends (your H-SPLIT-AT-P2).

## Your answers (item 115)

- *"It ends; energy moved"*: position 1's horizon ends at the closing, and its energy is the one energy that travels to
  position 2.
- *"When fully realized"*: position 2's horizon arises from the corridor then, and not before.
- *"The README itself"*: the opening's inflow is the README.

So the black hole left at position 1 and position 2's white-hole past are set aside on your path. They stay below as the
boundary. Your one-entangled-state accounting (item 111) is the accounting.

**What follows: the README, sent as the inflow, must be back-loaded.**
- **The capacity schedule.** The premises are H-INFLOW-IS-README, H-HORIZON-HOLDS, R-VAIDYA-HOLDS, H-STRONG-BOUND and
  H-DEVICE-SIZES. Under them, the bits delivered cannot run ahead of the growing horizon's capacity.
  - When a fraction φ of the energy has arrived, that capacity is N × φ². So the first half of the energy can carry at
    most a quarter of the README.
  - The closing mirrors it: when half the energy has left, at least three quarters of the README must already have been
    read or have left.
  - A corridor wider than the floor would relax this.
- **Bits per quantum.** Each quantum carries more than hc/r_min, because its wavelength must be shorter than r_min
  (H-EIKONAL). So there are at most N ln2/(4π²) quanta, and **each must carry at least 4π²/ln2 = 56.955 bits, for any
  README size**. That holds by construction: it is Bekenstein's bound, saturated.
  - With wavelengths below the growing horizon's radius (H-EIKONAL-GROWING), the bound is at least 8π²/ln2 = 113.91
    bits each.
- **What that needs of each mode** rests on Holevo's bound (NOT READ), so it is OPEN. With the prior entanglement your
  path assumes, superdense coding doubles the bits per mode (also NOT READ).
- **A consistency check:** with the README as the inflow, its carried mass E_min/c² (item 108) is the inflow's own
  energy.
- *First written:* "When a fraction e …"; "each quantum must carry at least 57 bits. That needs many-level modes, not
  single qubits".

## Tensions, and what is ruled out

*Set aside on your path by item 115, and kept as the null-dust model's own reading:*

- **Position 1 keeps its mass.** In this model nothing lowers position 1's mass after the opening, so a black hole forms
  there and stays. That conflicts with item 106 (at the closing, the bits are on position 2's horizon only) and with
  item 109 applied to position 1, unless your one-entangled-state accounting (item 111) applies. OPEN.
- **Position 2 has a white-hole past.** Run backwards, the outflow is an ordinary hole of the final mass with a past
  horizon. Under per-universe bookkeeping, position 2 carried that mass before the opening, which conflicts with items
  109 and 106. OPEN.
- **White holes are unstable** to matter falling in (Eardley 1974, NOT READ). OPEN.
- **What the inflow is.**
  - Its wavelengths must be much shorter than r_min (3.976×10⁻²⁸ m for the core). So each quantum carries far more than
    hc/r_min = 499.6 J, and there are at most about 4.8×10¹³ of them.
  - The device must be a spherically converging emitter around position 1 (wall 9).
  - It is the README (your item 115).
- **The joins** (H-JUNCTION). OPEN.

## The walls, as this changes them

| wall | now |
|---|---|
| 1 formation | opening and closing each satisfy every energy condition (R-VAIDYA-HOLDS). The corridor's violation must enter at the joins. OPEN |
| 9 the coupling | the device supplies the floor's energy as a converging inflow, lasting at least 2r_min/c under H-MAX-POWER-INFLOW (premises H-STRONG-BOUND, H-HORIZON-HOLDS). What couples it to the corridor is OPEN |

## Named hypotheses

- **Yours:** H-P1-HORIZON-ENDS, H-P2-HORIZON-AT-REALIZATION, H-INFLOW-IS-README (115); H-THREE-HOLDS (106), H-HORIZON-NEEDS-OBJECT (109), H-ENERGY-INTO-P2 (110), H-ONE-ENERGY-TWO-SIDES (111),
  H-BRIEF-HOLD (86.5).
- **The board's:** R-VAIDYA-HOLDS; H-EIKONAL, H-EIKONAL-GROWING; H-DEVICE-SIZES (the final horizon at the floor);
  H-MAX-POWER-INFLOW; H-HOLD-FRAME; H-MF-IS-AREA-MASS; H-HORIZON-HOLDS (the apparent
  horizon); H-STRONG-BOUND; H-JUNCTION; H-QUASISTATIC; H-ASYMPTOTIC-FLAT-ENDS (set against H-ONE-ENERGY-TWO-SIDES).

## Sources READ

| source | route | used |
|---|---|---|
| Gibbons, hep-th/0210109v1 | alphaXiv | p.1 abstract; p.2 eq. 1, maximum force c⁴/4G (a proposed principle) |
| Barrow & Gibbons, 1408.1820v3 | alphaXiv (a verifier) | p.2 eq. 2, maximum power c⁵/4G (a conjecture, factor O(1)); p.3 factor not settled |
| Cardoso, Ikeda, Moore, Yoo, 1803.03271v2 | alphaXiv (a verifier) | p.1; p.3 the conjecture (no past horizons); App. B p.9, unbounded outflow from a past horizon |
| NOT READ | — | Vaidya 1951; Eardley 1974 |

## OPEN

1. The joins through the throat, where the corridor's energy-condition violation enters.
2. Position 1's kept mass and position 2's white-hole past. *Answered, item 115: position 1's horizon ends with the
   energy moved; position 2's arises at realization. A dynamical model in which both happen is OPEN.*
3. Whether the inflow carries the README. *Answered, item 115: it is the README. It must be back-loaded, at 57 bits or
   more per quantum.*
4. Whether a maximum power holds, and its factor.
