# Wall C, third piece: what the global bulk must do, for a held corridor and for a lasting one (M-RULINGS items 86, 136, 149; computed, deduced and READ; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you said

- **Item 136 E:** the hold is *"Instantaneous or near instantaneous"*.
- **Item 86, answer 5 (H-BRIEF-HOLD):** *"incredibly short, maybe even immeasurable but not zero"*, and *"this answer is
  also a relative one"*.
- **Item 149:** *"You have to work the math now"*.
- **The instrument:** `globalbulk.py`. It imports throatbulk.py, kscale.py and stability.py by path. Selftest 6/6.
  - **Genuine checks:** four.
  - **Control:** one.
  - **Marked STRUCTURAL:** one.

## What passes

### 1. A held corridor needs only the local bulk (G1)

- **Finite propagation** (standard, not READ). In harmonic gauge the Einstein equations are hyperbolic. A region's
  development depends only on the data in its past domain of dependence.
- **Take a spacelike slice through the throat** inside the local bulk, reaching a distance δ into the bulk.
  - The plane's points within about δ/c of that slice, in proper time, lie in its domain of dependence.
  - So nothing in the global bulk can reach them.
- **δ is the series radius** (BULKSERIES.md B5), and the clock is m/c (stability.py S3). So the local bulk alone decides a
  hold of up to:
  - **about 1.46 clocks when ℓ = r₀;**
  - **about 2.8 clocks when ℓ ≫ r₀.**
  - At the board's example README that is **1.0×10⁻³⁶ s to 1.9×10⁻³⁶ s.**
- **This is an estimate of order, from a ratio test** (H-DELTA-ORDER, the board's).
  - Your *"relative"* bears on it. The time is a proper time near the throat; measured in the far region's time it is
    longer.
  - The Gaussian normal chart is also limited near a horizon (Maartens–Koyama p.27, READ in THROATBULK.md).
- **Under H-BRIEF-HOLD, then, whether a global bulk exists does not bear on the corridor during its hold.**
  - Over such a hold, stability.py's exact identity changes the second derivative by about a quarter of its natural
    size per clock.
  - The white-hole blueshift grows as v², not exponentially (STABILITY.md S5b).

## What does not pass: a lasting static corridor

### 2. Eq. (17) on the whole plane cannot sit in a Randall–Sundrum II bulk with a compact core (G2)

- **Your corridor's own Weyl term at large r** is r²E^θ_θ = −m/(4r) (computed with throatbulk.py's corrected
  Maartens–Koyama eqs. 150–152). It is a tail independent of ℓ.
- **A black hole on a Randall–Sundrum II plane** reads +2ℓ²m/(3r³) (Maartens–Koyama eq. 155, READ in throatbulk.py).
- **Their ratio is −(3/8)(r/ℓ)².** They have opposite signs, and the ratio is unbounded as r grows.
  - **Control:** the Schwarzschild member reads no Weyl term at all.
- **Equivalently:** γ = 5/4 for your corridor (kscale.py, Casadio–Fabbri–Mazzacurati eq. 8), against γ = 1 + O(ℓ²/r²)
  for that bulk (Maartens–Koyama p.26, eq. 41).
- **This holds at every r₀, because the far field always lies at r ≫ ℓ.**
  - So KSCALE.md's way out (c), r₀ ~ ℓ, does not survive for a lasting corridor. KSCALE.md left it open, and it closes
    here.
  - STATIC.md already found γ = 1 at long range for static planes face to face. G2 is the same conflict, stated for the
    bulk.
- **One step is the board's extension (H-COMPACT-CORE).** A compact non-linear core near the throat acts, at r ≫ ℓ, as a
  compact source in the linear theory. That is the board's extension of the linear results READ.

### 3. So the two readings of the hold part (G3)

- **Under H-BRIEF-HOLD,** the global bulk does not bear on the corridor during the hold (G1).
- **A lasting corridor** needs a bulk whose departure from Randall–Sundrum is not compact: one that reaches the bulk's
  far horizon, as the black string's does (Maartens p.19, READ in CLOSEDBULK.md and MANYPLANES.md). No such bulk is
  built here.

## Named hypotheses

- **Yours:**
  - H-BRIEF-HOLD (86.5), with its *"relative"*;
  - item 136 E;
  - H-STATIC-PLANES (141);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-ONE-PLANE-NEAR;
  - H-COMPACT-CORE;
  - H-DELTA-ORDER;
  - H-NO-LASTING-FIELD (STATIC.md). G1 is what that hypothesis needs in the bulk.

## OPEN

1. A lasting corridor's bulk: a departure from Randall–Sundrum reaching the far horizon. Is it regular?
2. G1 made exact: the domain of dependence computed in the bulk series' own metric, rather than estimated from its radius.
3. How the hold starts and ends. G1 covers the hold itself, not its making (CHAIN.md's H-PRIOR-SETUP).
