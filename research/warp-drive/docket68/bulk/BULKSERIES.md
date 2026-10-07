# Wall C, second piece: the bulk off the corridor, computed order by order (M-RULINGS item 149; computed; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft re-implemented the series solver that
closedbulk.py already owns; it now imports that owner and is checked against it (History).

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
  - through y⁷ at ℓ = r₀;
  - through y⁸ in the flat-bulk limit.
- **This checks the Bianchi lemma that localbulk L4 cites.**

### 4. The throat, to higher order (B4)

The units are m = 1, so r₀ = 2.

| ℓ | C̃ at the throat |
|---|---|
| general (through y⁶) | 4 + y² + 2y³/ℓ + (ℓ² + 28)y⁴/(12ℓ²) + (ℓ² + 6)y⁵/(3ℓ³) + (3ℓ⁴ + 260ℓ² + 496)y⁶/(360ℓ⁴) |
| ℓ = r₀ (through y⁸) | 4 + y² + y³ + 2y⁴/3 + 5y⁵/12 + 11y⁶/40 + 79y⁷/420 + 2603y⁸/20160 |
| ℓ ≫ r₀ (through y¹⁰) | 4 + y² + y⁴/12 + y⁶/120 + 23y⁸/20160 + 37y¹⁰/259200 |

- **The general row and the ℓ = r₀ row agree** where they overlap.
- **Every computed coefficient is positive, for every ℓ.** That is in g̃. The physical sphere is e^(−2y/ℓ)C̃, and it
  shrinks at first order (throatbulk T6).

### 5. How far the series reaches (B5)

- **This is a ratio test on the last terms.** It estimates the radius, it is not a bound, and it is the radius of this
  representation, not where the bulk ends.
- **At ℓ = r₀:** successive ratios settle at 0.684 and 0.686 per order. The radius is about **1.46m, which is 0.73 r₀**.
- **At ℓ ≫ r₀:** the ratios in (y/r₀)² run 0.33, 0.40, 0.55, 0.50. The radius is about **1.4 r₀**.
- **So the reach is of order r₀, and below it when ℓ = r₀.** This replaces localbulk L5's "~min(r₀, ℓ)", which was an
  estimate from two terms.

## What this does and does not show

- **It shows the local bulk explicitly:** the series, the constraints holding off the plane, and how far the series
  reaches.
- **It does not show the global bulk.** A finite radius of convergence can come from a singularity at complex y, so it
  says nothing on its own about whether the bulk ends regularly.
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
2. The radius for ℓ < r₀.
3. The global bulk (GLOBALBULK.md).

## History

- *First written* with its own series solver beside closedbulk.py's. It now imports closedbulk.py's `build()` and must
  agree with it through y⁴, which it does. The faster solver is kept for higher orders, and the owner checks it.
