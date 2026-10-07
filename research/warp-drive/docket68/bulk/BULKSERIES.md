# Wall C, second piece: the bulk off the corridor, computed order by order (M-RULINGS item 149; computed; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft re-implemented the series solver that
closedbulk.py already owns; it now imports that owner and is checked against it. The verifier later scoped the radius to
ℓ ≳ r₀ and added the ratio test's caveats (History).

## Where this starts

- **localbulk.py proved a local vacuum Randall–Sundrum bulk exists** in which your corridor is an exact plane with no
  matter on it. It is unique among analytic solutions, and its Taylor series is Maartens–Koyama's eq. (148).
- **closedbulk.py (seated) already builds that series** for the r₀ = 1.8m member, through y² by default.
- **This note works your corridor's own member, r₀ = 2m,** at the throat, which is also the horizon. It goes to higher
  order and estimates how far the series reaches.
- **The instrument:** `bulkseries.py`, which imports closedbulk.py and throatbulk.py by path. Selftest 6/6.
  - **Genuine checks:** four.
  - **Controls:** two (the black string; agreement with the seated owner).

## What the mathematics gives

### 1. The method (B1, and the owner)

- **The gauge.** Gaussian normal: ds² = dy² − A dt² + B dr² + C dΩ². Staticity and spherical symmetry carry over from
  the data (localbulk L4).
- **The equations.** Each component of the plane's metric obeys
  ½ ∂²_y h = R_μμ[h] + (∂_y h)²/(2h) − (K/2)∂_y h + (4/ℓ²)h, starting from h = eq. (17) and ∂_y h = −2h/ℓ.
- **Each order is explicit.** The solver here is faster than the owner's (seconds per order at fixed ℓ, against
  minutes).
- **Its two checks:**
  - it agrees with closedbulk.py's seated `build()` through y⁴ on your corridor;
  - **control:** Schwarzschild data return the black string, C = r²e^(−2y/ℓ), exactly at every order computed.

### 2. It reproduces Maartens–Koyama at the throat (B2)

- **In g̃ = e^(2y/ℓ)g, the throat's sphere reads C̃ = 4m² + y² + 2y³/ℓ.** That is throatbulk.py T6, imported.

### 3. The constraints stay satisfied off the plane (B3)

- **The Gauss (yy) and Codazzi (yr) constraints vanish order by order:**
  - through y² in the selftest;
  - through y⁷ at ℓ = r₀ and y⁸ in the flat-bulk limit, in the long runs.
- **This checks the Bianchi lemma that localbulk L4 cites.**

### 4. The throat, to higher order (B4)

The units are m = 1, so r₀ = 2.

| ℓ | C̃ at the throat |
|---|---|
| general (through y⁶) | 4 + y² + 2y³/ℓ + (ℓ² + 28)y⁴/(12ℓ²) + (ℓ² + 6)y⁵/(3ℓ³) + (3ℓ⁴ + 260ℓ² + 496)y⁶/(360ℓ⁴) |
| ℓ = r₀ (through y⁸) | 4 + y² + y³ + 2y⁴/3 + 5y⁵/12 + 11y⁶/40 + 79y⁷/420 + 2603y⁸/20160 |
| ℓ ≫ r₀ (through y¹⁰) | 4 + y² + y⁴/12 + y⁶/120 + 23y⁸/20160 + 37y¹⁰/259200 |

- **The selftest pins the y⁴ coefficient.** The rest of the general row comes from `--order 6`. The ℓ = r₀ and ℓ ≫ r₀
  rows come from the long runs, and the instrument records them as data (`RUN_ELL_R0`, `RUN_FLAT`).

- **The general row and the ℓ = r₀ row agree** where they overlap.
- **Every computed coefficient is positive, for every ℓ.** That is in g̃. The physical sphere is e^(−2y/ℓ)C̃, and it
  shrinks at first order (throatbulk T6).

### 5. How far the series reaches (B5)

- **`radius_estimates()` computes these from the recorded runs.**
- **What the estimate is, and is not.**
  - It estimates the radius from the last terms; it is not a bound.
  - It is for one component (C̃) at one point, r = 2m, where the static chart degenerates. A, B and other r may differ.
- **At ℓ = r₀:** the ratios run 0.625, 0.66, 0.684, 0.686 per order, still rising.
  - The last ratio gives about 1.46m. The root test gives about 1.29m.
  - So 1.46m (0.73 r₀) is, if anything, an upper estimate.
- **At ℓ ≫ r₀:** the ratios in y² run 0.083, 0.100, 0.137, 0.125, and they are not monotone.
  - In (y/r₀)² they are 0.33, 0.40, 0.55, 0.50.
  - The radius lies in about 2.70m to 3.16m, which is 1.35 to 1.58 r₀. The root test gives less, about 1.21 r₀.
- **So for ℓ ≳ r₀ the reach is of order r₀, and below it when ℓ = r₀.**
  - This replaces localbulk L5's "~min(r₀, ℓ)" for ℓ ≳ r₀ only. For ℓ < r₀ it is OPEN.
- **Every computed coefficient is positive.** If that persists, Pringsheim's theorem puts the singularity that limits
  the radius on the positive real y axis, at y about the radius. It is then a caustic of the Gaussian normal chart, or a
  curvature singularity: the first draft's "complex y" understated this.

## What this does and does not show

- **It shows the local bulk explicitly:** the series, the constraints holding off the plane, and how far the series
  reaches.
- **It does not show the global bulk.** Whether the singularity B5 points to is a coordinate caustic or a curvature
  singularity is not settled.
- **GLOBALBULK.md takes up what this means for the corridor.**

## Named hypotheses

- **Yours:**
  - H-STATIC-PLANES (141);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-ONE-PLANE-NEAR;
  - mirror symmetry in fixing K (localbulk.py).

## OPEN

1. Higher orders, for a firmer radius: the next two orders at ℓ = r₀ take about an hour.
2. The radius for ℓ < r₀, where H-ONE-BIT-SCALE sits.
3. The global bulk (GLOBALBULK.md).
4. Whether B5's singularity, at y about the radius, is a caustic of the chart or of the curvature.
5. A check of B4's y⁴ coefficient against Maartens–Koyama eq. (148)'s y⁴ term (p.27), as B2 checks y³.
6. The radius of A and B, and at other r. G1 needs the smallest radius over the whole slab, not one component at one
   point.

## History

- *First written* with its own series solver beside closedbulk.py's. It now imports closedbulk.py's `build()` and must
  agree with it through y⁴, which it does. The faster solver is kept for higher orders, and the owner checks it.

## History (verifier, 2026-10-07)

- **"Replaces localbulk L5" over-claimed.** It now holds for ℓ ≳ r₀ only.
- **The ratio-test caveats are added:** the ratios are still rising at ℓ = r₀, the root test gives a smaller radius,
  the flat-limit ratios are not monotone, and the estimate is for one component at one point.
- **Which claims the selftest pins** is now stated, separately from the long runs.
- **Under-claim taken up: positivity and Pringsheim.**
- **The recorded runs** are now data in the instrument. GLOBALBULK imports them rather than copying numbers.
