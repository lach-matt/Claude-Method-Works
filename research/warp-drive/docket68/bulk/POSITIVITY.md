# The energy is positive: a proof for the coinciding planes (M-RULINGS item 139; READ and computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you said

- **Item 139, answer 1:** position 2's plane is the negative-tension one, a quarter of ours, and ours is positive:
  *"yes"*.
- **Answer 2:** *"positive, and you have to prove it."*
- **The instrument:** `positivity.py`. Selftest 8/8. It imports multiplane.py and censor.py.

## The obstacle

- **A negative-tension plane that is free to move makes the mode that moves it, the radion, carry negative kinetic
  energy.** Pilo–Rattazzi–Zaffaroni, hep-th/0004028v2 (READ): eq. (2.16), and p.11, *"the need for a non-decoupling
  massless and ghost-like radion is always associated with the presence of a brane of negative tension."*
- **Computed:** with the planes apart (r = k_L⁻¹/2, k_R = 3k_L/4), the radion's coefficient is C_r = −219.7 (in units
  M = k_L = 1), negative (Q1).

## The proof, step by step

1. **Your planes coincide (item 127), on the mirror plane.**
   - The bulk's two sides are mirror images. The mirror plane is the one place each side maps onto itself.
   - **A sheet there cannot move off it.** A displacement f is identified with −f, so the only part that survives is
     (f + (−f))/2 = 0 (Q2).
   - Pilo–Rattazzi–Zaffaroni p.3 (READ) state this for a negative-tension plane at such a point: *"the negative energy
     mode associated with its fluctuations in the transverse direction is projected out."*
   - **So the coinciding planes carry no radion, and so no negative-kinetic mode.**
2. **The two coinciding sheets act as one surface.**
   - Israel's condition is linear in the stress (LOOSE.md L4). The surface's tension is the sum: **+4/3 − 1/3 = +1**
     times the one-plane value (Q3).
   - On that surface the null energy is S_AB·k^A·k^B = λ·k_y², with λ > 0. It is **never negative, for every null
     vector**.
3. **Position 2's sheet taken alone would read −(1/3)·λ·k_y² < 0.**
   - But it never exists alone: it is always one face of a surface whose total tension is positive.
   - **This is your item 117 as geometry:** *"An NEC is never violated, between two entangled positions the NEC is like
     a coin, each position sits on a separate side."* Each sheet is one side. Read alone, position 2's breaks the
     condition; the coin as a whole never does.
4. **The bulk between is vacuum with a cosmological constant.** Its null energy is 0 (Q4).
5. **So on the coinciding planes:**
   - no mode carries negative kinetic energy (step 1);
   - the null energy condition holds on the surface (step 2);
   - and it holds in the bulk (step 4).
   - **The energy is positive in every part the board can compute.**

## What it costs, and why your rulings already pay it

- **With no radion, a lasting source on this plane has Einstein's long-range field, γ = 1** (Q5). So eq. (17)'s
  static γ = 5/4 would not form here.
- **Your rulings already have the corridor near-instantaneous** (items 86 answer 5, 94, 136 E), so no lasting far field
  is needed. The static γ = 5/4 belongs to a geometry that never lasts long enough to show it.
- **Contrast:** a free negative plane (r > 0) does give γ = 5/4, but with a ghost (multiplane.py M3). Positive energy
  and a lasting γ = 5/4 exclude each other. Your rulings choose positive energy and a momentary corridor.

## What this does and does not prove

- **It proves three things on the coinciding planes:**
  - the mode that made the energy negative is absent;
  - the null energy condition holds on the surface and in the bulk;
  - position 2's negative tension is never seen alone.
- **It does not prove a full positive-energy theorem** (a Witten-type proof that the total energy is non-negative for
  every configuration of this bulk). That is the stronger statement, and it is not done.
- **Not covered:**
  - the tower of massive gravitons, normally healthy in such bulks, not read here;
  - the corridor's own geometry during the hold;
  - any matter on the sheets.
- **Step 1 is structural.** The algebra is one line. Its weight is PRZ's statement, READ, that a plane at the fixed
  point has no transverse mode.
- **A caution for C.** Two sheets at one fixed point, with tensions +4/3 and −1/3, is the board's configuration. It is
  not read in any source. PRZ's footnote 6 (p.9, READ) discusses a composite pair of planes at a fixed point, with a
  radion of positive kinetic term in the sign-flipped case. That is the nearest the literature comes.

## Named hypotheses

- **The board's:**
  - H-FIXED-POINT-COINCIDENCE (both sheets at the mirror plane);
  - H-COMPOSITE-SURFACE (the sheets act as one surface, by Israel's linearity).
- **Yours:**
  - H-P2-NEGATIVE-PLANE and M-PROVE-POSITIVE (139);
  - H-PLANES-COINCIDE (127);
  - H-NEC-COIN (117), H-NEC-NEVER-VIOLATED (120, 123);
  - the near-instantaneous corridor (86, 94, 136).

## OPEN

1. A full positive-energy theorem for this bulk.
2. The massive graviton tower's norm, READ.
3. The corridor's geometry during the hold, in this bulk (C).
