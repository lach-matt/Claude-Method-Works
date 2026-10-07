# Wall C, first piece: a bulk carrying the corridor exists near the plane (M-RULINGS item 149; derived and computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## Where this starts

- **Wall C asked for a five-dimensional bulk carrying your corridor.** The record said none was known (residue/STATUS.md;
  Maartens–Koyama p.27).
- **On static, face-to-face planes, the pair is one Randall–Sundrum II plane at long range** (static.py S2b). So the
  question is the corridor on one such plane, with no matter on it:
  - the plane's metric is eq. (17) at r₀ = 2m;
  - its extrinsic curvature is K_μν = −(1/ℓ)·g_μν, by the junction condition with mirror symmetry and the
    Randall–Sundrum tension (Maartens–Koyama eq. 68 with T = 0, READ in throatbulk.py);
  - the bulk is vacuum with Λ₅ = −6/ℓ².
- **The instrument:** `localbulk.py`. Selftest 4/4.
  - **Genuine checks:** two.
  - **Control:** one.
  - **Marked STRUCTURAL:** one.

## What the mathematics gives

### 1. Your corridor satisfies both conditions a plane must meet to be carried by a bulk (L1, L2)

- **The Gauss condition.** For a plane in this bulk, R⁽⁴⁾ = 2Λ₅ + K² − K·K. With K = −g/ℓ the right side is
  −12/ℓ² + 16/ℓ² − 4/ℓ² = 0 (STRUCTURAL). So the condition is that the plane's curvature scalar vanishes.
  - **Eq. (17) at r₀ = 2m has R⁽⁴⁾ = 0 exactly** (computed). The condition holds.
  - **Control:** a plane metric with R⁽⁴⁾ ≠ 0 (Schwarzschild–de Sitter, R = 12/L²) fails it.
- **The Codazzi condition, D^μK_μν − D_νK = 0,** holds identically when K is proportional to g.

### 2. The corridor's geometry is smooth through its horizon (L3)

- **In coordinates adapted to the horizon (u = √(r − 2m)),** dρ/du is a power series beginning √(2m): √(2m) + √2·u²/√m −
  ….
- **So the radius and the metric functions are analytic straight through the horizon** (computed). Nothing singular
  stands in the data.

### 3. So a bulk exists near the plane, and it is unique (L4)

- **The plane's metric and its extrinsic curvature together are analytic data,** on a surface that is not
  characteristic, satisfying both conditions.
- **By the Cauchy–Kovalevskaya theorem** (standard, not READ), the five-dimensional equations then have a unique local
  analytic solution off the plane.
- **So a bulk exists in which your corridor is an exact Randall–Sundrum plane with no matter on it.**
  - Dahia and Romero (READ in BULKWARP.md) give local embedding for any analytic metric. The board's step adds that it
    holds with the Randall–Sundrum extrinsic curvature, because your corridor satisfies the Gauss condition.

### 4. How far it reaches (L5)

- **The first correction off the plane, −E·y²** (Maartens–Koyama eq. 148), is of order y²/r₀² at the throat. So the
  local solution is controlled out to a distance of order the throat's size. That is an estimate, not a bound.

## What this does and does not show

- **It shows that a bulk carrying your corridor exists near the plane, and is unique there.** Wall C's record said no
  bulk was known. Near the plane, one now is.
- **It does not show the global bulk.**
  - Whether the local solution continues, regular, all the way to where the bulk ends is not settled.
  - Building a bulk outward from the plane is not well posed in the sense of stability. Anderson (READ in BULKWARP.md):
    the embedding theorem *"offers no guarantee of continuous dependence on the data and … disregards causality"*.
  - The global bulk needs a boundary-value construction, the method Figueras and Wiseman used for static black holes on
    such a plane (READ in OUTSIDE.md).
- **The censorship question (wall D) turns on the global bulk.** It stays open with it.

## Named hypotheses

- **Yours:**
  - H-STATIC-PLANES (141);
  - H-BK-CORRIDOR's corridor, eq. (17), as your corridor (the board's identification);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-FACE-TO-FACE;
  - H-COMPOSITE-SURFACE (one RS II plane at long range);
  - H-ANALYTIC-DATA (the data analytic; computed at the horizon, assumed elsewhere — they are rational in r away from
    the horizon).

## OPEN

1. The global bulk: a boundary-value construction (Figueras–Wiseman's method).
