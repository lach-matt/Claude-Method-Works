# How the corridor opens and closes (M-RULINGS item 113, second of three; deduced, computed and READ; not verified; not seated; 2026-10-06)

## What M said

- **Item 106:** *"Three distinct holds in one fluid wave motion, horizon position 1 only as the corridor opens, … upon
  the corridor closing the bits are then held only at the horizon of position 2"*.
- **Item 109:** *"A horizon cannot exist without the object of which it needs to exist"*.
- **Item 110:** *"Into position 2"*.
- **Item 111:** *"one energy read from two sides"*.
- **Item 86, answer 5:** *"I suspect it is incredibly short, maybe even immeasurable but not zero"*.

Every number is printed by `opening.py`.
- **Selftest:** 7/7 checks, 2 genuine controls, with 5 STRUCTURAL lines printed and not counted.
- **Imported:** `chain.py` (the floor).

**The board's reading (R-VAIDYA-HOLDS, ungraded).** The opening and closing are each modelled as null dust: radiation
moving at light speed, your "fluid wave". The metric is Vaidya's form, written here; its curvature is computed, and
nothing about it is READ.
- **Opening:** energy falls in at position 1, and its mass m rises from 0 to the floor.
- **Closing:** energy flows out at position 2, and its mass falls from the floor to 0.

## What follows the work

- **1. Both holds need only positive energy.**
  - Falling in, the only curvature component is G_vv = 2m′/r² (sympy). The null energy condition holds exactly when the
    mass rises, which is the opening.
  - Flowing out, it is G_uu = −2m′/r². The condition holds exactly when the mass falls, which is the closing.
  - Controls: an opening that sheds mass, or a closing that gains it, violates the condition.
  - Unlike the corridor's static neck, neither transition needs negative energy. So the board's duration limit on
    negative energy (D7) does not bind them.
- **2. Both keep R = 0, like the corridor.** Null dust has R = 0 (sympy), the same condition as Bronnikov–Kim's
  corridor (escape.py, section 8m). The whole sequence of opening, corridor and closing stays in the R = 0 class.
- **3. The energy in is the energy out.**
  - The opening carries the floor in at position 1: 4.59404002×10⁸ J × √N, which is 2.405878326×10¹⁶ J for the core.
  - The closing carries the same energy out into position 2.
  - That is your item 110 (energy into position 2) and your item 111 (one energy).
  - Position 2's horizon ends when its mass reaches zero: the horizon at r = 2m shrinks to nothing. That is your item
    109.
- **4. The shortest opening is immeasurably short, but not zero.**
  - Suppose no flow can exceed Gibbons' maximum tension multiplied by c (H-MAX-POWER). Gibbons, READ: *"The tension or
    force between two bodies cannot exceed F_g = c⁴/4G"* (hep-th/0210109 p.2 eq. 1, a proposed principle). Extending it
    from force to power, c⁵/4G, is the board's step.
  - Then a hold lasts at least
    **2r_min/c = √(2N h G ln2/(π² c⁵)) = 5.0647×10⁻⁴⁴ s × √N**, which is **2.652×10⁻³⁶ s** for the core README.
  - That is your item 86 answer 5, computed.
  - A constant flow meets the bound exactly. A smooth profile needs πr_min/c = 4.166×10⁻³⁶ s.

## What is ruled out, as the boundary

- An opening that removes mass, or a closing that adds it, using positive energy.
- A hold shorter than 2r_min/c, under H-MAX-POWER.
- **The white hole's stability.** Classical white holes are unstable to matter falling in (Eardley 1974, NOT READ).
  Position 2's closing hold is a white-hole horizon (PLANE.md point 1), so its stability is OPEN.
- **The joins** (H-JUNCTION, not computed: OPEN):
  - how the falling-in hold at position 1 joins the corridor's interior;
  - how the flowing-out hold at position 2 joins it;
  - how position 2's mass rises during the opening.

## The walls, as this changes them

| wall | now |
|---|---|
| 1 formation | opening and closing need only positive energy, flowing at light speed (R-VAIDYA-HOLDS). The joins are OPEN |
| 9 the coupling | the device's role at opening is to supply the floor's energy as an inflow lasting at least 2r_min/c. What couples it to the corridor is OPEN |

## Named hypotheses

- **Yours:** H-THREE-HOLDS (106), H-HORIZON-NEEDS-OBJECT (109), H-ENERGY-INTO-P2 (110), H-ONE-ENERGY-TWO-SIDES (111),
  H-BRIEF-HOLD (86.5).
- **The board's:** R-VAIDYA-HOLDS; H-MAX-POWER; H-HORIZON-HOLDS and H-STRONG-BOUND (chain.py); H-JUNCTION.

## Sources READ

| source | route | used |
|---|---|---|
| Gibbons, hep-th/0210109v1 | alphaXiv | p.1, the maximal tension c⁴/4G (*"I suggest"*); p.2 eq. 1, the principle; a force, not a power |
| NOT READ | — | Vaidya 1951; Eardley 1974 |

## OPEN

1. The joins through the throat, and how position 2's mass rises during the opening.
2. The stability of position 2's white-hole horizon.
3. Whether a maximum power holds at all (H-MAX-POWER).
