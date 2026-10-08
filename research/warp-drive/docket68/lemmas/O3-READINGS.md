# Item 159: both readings of where the write sits, tested (computed, READ and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `o3_readings.py`, selftest 7/7.

## What you said

- **Item 159:** *"test both options"*. The two options are:
  - **(i)** the write happens inside a hold after the corridor stands;
  - **(ii)** the write is the opening itself, the README flowing in.
- **Also bearing on the test:** item 158 (2) *"Exactly as long as the write needs  I should think"*; item 127 (1)
  *"yes"* (the planes coincide, the extra dimension included); item 138 (the bulk is multi-universal).

## The one number both readings share

- **The write's length.** `o3_write.py` puts the write at **2.0×10⁵ clocks** at the example README (Z = 108.75). Even
  without H-README-ALONE it is 630 clocks.
- **What each reading has to carry.** Whichever reading holds, the bulk has to stay regular for that long.

## Reading (i): the write inside a standing corridor (R1) — refuted

- **The bulk is forced.** With eq. (17) held on the plane, the static bulk is forced in the board's locally analytic
  class (B4b).
- **It cannot last long enough.** That bulk reaches its singular surface by about 18 clocks. Both 2.0×10⁵ and 630 are
  past it.
- **Where the refutation applies.** It is refuted at the example README, and for every README above about 25·Z bits.
- **A tension besides (deduced).** Under your 115 (c) and H-PULL-IS-COST, the corridor's mass *is* the README's energy.
  A corridor standing before its README arrives needs that energy to arrive ahead of the bits it carries.

## The black string's instability, computed (R2)

**Sources READ:** Gregory–Laflamme hep-th/9301052; Gregory hep-th/0004101; Lehner–Pretorius 1006.5960.

**The equation.**
- GL print the equation for the black string's unstable mode, their eq. (10), p.7. It is transcribed at D = 4.
- One sign, as extracted from the PDF, contradicts GL's own stated horizon exponents. Moving that one term outside the
  bracket restores them exactly, to −1 ± Ω. So the transcription is fixed by GL's own text, and the extracted form is
  kept as a control that fails.

**How it is solved.**
- The equation is integrated from the horizon's regular branch and steered around a point on the real axis where its
  leading coefficient vanishes.
- An unstable mode is found where the growing solution at infinity cancels.

**The result:**

| μ·r₊ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.85 |
|---|---|---|---|---|---|---|---|---|---|
| Ω·r₊ | 0.052 | 0.080 | 0.091 | 0.091 | 0.083 | 0.069 | 0.048 | 0.022 | 0.008 |

- **The fastest mode:** Ω·r₊ = 0.0923 at μ·r₊ ≈ 0.35.
- **The critical wavenumber:** μ·r₊ = 0.876. Beyond it there are no unstable modes.

**Controls against READ figures:**
- Lehner–Pretorius's critical *L/R* ≈ 7.2 is μ·r₊ = 0.873. Ours is 0.876, within 0.4%.
- Gregory's GM = 1 range, 0 < m < 0.45, with the most favoured mode near 0.2, is μ·r₊ < 0.9 with the peak near 0.4.
  Ours brackets both.
- Two different integration settings agree to 10⁻³.

## Reading (ii): the write as the opening (R3) — refuted in the board's model

- **The model.** The board models the opening as ingoing Vaidya (`opening.py`, R-VAIDYA-HOLDS). The plane then holds
  Schwarzschild of mass m(v), and `b4_static.py`'s own control shows the board's solver returning the black string
  for Schwarzschild data.
- **Quasi-static.** Over a 2.0×10⁵-clock opening the mass changes at 10⁻⁴ of the instability's growth rate (0.046 per
  clock). So the string is effectively at rest, and unstable, throughout.
- **The growth.** Over the opening's last half alone, assuming a linear ramp (H-LINEAR-RAMP), it grows by
  **4.6×10³ e-folds**.
  - A seed as small as 10⁻¹⁰⁰ needs only 230.
  - So a horizon present for **2.5%** of the opening is enough.
- **Then the nonlinear stage.** Lehner–Pretorius's simulation ends the nonlinear cascade about **107 clocks** later
  (80/(1 − 1/4)), in a naked curvature singularity (READ, pp.3–4).

## The escapes, named (R4; deduced, none shown)

**(a) An extremal opening.**
- Gregory: the instability's *"only exception"* is extremal solutions (READ for charged branes, not shown for the
  corridor).
- If the opening passes through extremal members instead of Schwarzschild ones, then by B4b's uniqueness the bulk
  tracks the static extremal bulk. The long opening's reach then meets its singular surface, as in reading (i).
- Not shown to help.

**(b) A wall within the instability's reach.**
- Gregory's eq. (11): a second wall close enough switches the instability off. In the flat limit that is closer than
  π/μ_c = 3.6 r₊ = 7.2 m (deduced).
- Your 127 puts position 2's plane at the same place as position 1's, so it is not that wall.
- The other planes of your 138 are candidates.

**(c) Leaving the flat limit.**
- Reading (i)'s singular surface was computed at ℓ ≫ r₀. k's scale is B6′, nature's.
- Gregory shows the single-wall Randall–Sundrum string stays unstable, so this bears on reading (i) at most.

## Verdict

- **Both readings fail under the board's models in the flat limit.** On each, the bulk does not stay regular through
  the write: (i) reaches the static bulk's singular surface, and (ii) breaks up the black string into a naked
  singularity.
- **The routes left** run through structure your rulings already name: the other planes of 138, an extremal opening,
  and k's scale. Each is B4d's to compute.

## Named hypotheses

- **Yours:** 115 (c), 127, 138, 158 (2), 159.
- **The board's:**
  - those of `o3_write.py`;
  - R-VAIDYA-HOLDS and H-LINEAR-RAMP (reading (ii));
  - B4b's locally analytic class and uniqueness (reading (i), escape (a));
  - the flat limit;
  - H-PULL-IS-COST.
