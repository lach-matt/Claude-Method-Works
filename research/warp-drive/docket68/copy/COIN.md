# The coin test (M-RULINGS items 117–118; deduced and computed; not verified; not seated; 2026-10-06)

## What M said

- **Item 117:** *"An NEC is never violated, between two entangled positions the NEC is like a coin, each position sits on
  a separate side. That action is that the coin flips. The NEC appears broken, but is not"* (H-NEC-COIN).
- **Item 118:** *"Yes, run it"*. The test is the null energy condition averaged along a whole path through the one-way
  corridor, from position 1's side to position 2's.

Every number is printed by `coin.py`.
- **Selftest:** 6/6 checks, 1 genuine control and 1 contrast, with 2 STRUCTURAL lines printed and not counted.
- **Imported:** `opening.py` (the corridor's radial combination, computed from eq. 17) and `escape.py` (R = 0, and its
  seated text).

## What the test finds

**In our plane's reading the test goes against the coin. In the bulk it agrees with the coin.** Both are shown, per item
82.

- **1. The energy along the path has one sign through the horizon.**
  - The energy a radial light-like path meets is **G_kk = −2E²(2r₀ − 3m)/(r(2r − 3m)²)** (sympy). It is finite at the
    horizon.
  - It is negative everywhere for the horizon members: −1.32 just outside the throat, −0.60 at the horizon, −0.044 at
    r = 3 (m = 1, r₀ = 1.8).
  - **The sign change I offered as a candidate coin flip was an artifact.** The static-frame combination (−0.0148
    outside, +0.0519 inside) changes sign only because of the frame's factor 1/(1 − 2m/r). The energy the path actually
    meets does not change sign. That candidate is withdrawn (OPENING.md).
- **2. The average along the whole passage is negative.**
  - Each leg, from infinity to the throat or from the throat to infinity, gives −0.957356 E for m = 1, r₀ = 1.8
    (geometric units). The whole passage gives **−1.914712 E**.
  - So in the plane's reading the violation is not a local feature: it holds along the whole path.
  - Control: an ordinary black hole (r₀ = 3m/2) meets no energy at all.
  - As r₀ approaches 3m/2 from above, each leg tends to −4/3 E, not 0. The negative energy gathers at the throat.
- **3. The bulk keeps the condition.**
  - `escape.py` (section 8m, seated, S3) found for these throats that *"the NEC holds -- on either sign of the tension.
    The bulk keeps only its vacuum energy (the NEC, saturated); E = -G carries the whole reading"*. That holds locally,
    under H-RS1; a global bulk is BULK5-O1, OPEN.
  - So the condition appears broken from our plane, along the whole passage, and is not broken in the full spacetime
    the plane sits in.
  - **That is the part of your coin the board can show.** The flip itself, the action, is not computed.

## Named hypotheses

- **Yours:** H-NEC-COIN (117), H-READING-ONLY (86.1), H-CORRIDOR-HORIZON (104).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-AVERAGED-NEC: the test you approved;
  - H-PLANE-READING: the four-dimensional reading of the brane's projected stress;
  - H-RS1: the scope of the bulk statement.

## OPEN

1. The flip: what in the geometry or the state is the coin turning over.
2. The bulk statement beyond the local one: a global bulk (BULK5-O1).
