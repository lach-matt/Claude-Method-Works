# Wall D, the censorship theorem: a passage between two ends of a plane in a bulk (M-RULINGS items 139, 141, 149; READ, computed and deduced; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## Why

- **DOORS.md, OPEN 1:** *"A censorship theorem for passage between asymptotic regions of a plane in a bulk. None was
  READ, so it would have to be proved."*
- **PASSAGE5D.md settled what the corridor's own geometry decides.** It also said a censorship theorem was still missing.
- **This note supplies one.** It is a published theorem for spacetimes with timelike boundaries, applied to your corridor
  with boundaries the board computes.
- **The instrument:** `censor5d.py`, which imports doors.py and passage5d.py by path. Selftest 4/4, about 2 s.
  - **Genuine checks:** two.
  - **Control:** one.
  - **Marked STRUCTURAL:** one.

## READ

- **Chruściel, Galloway and Solis, arXiv:0808.3233v2 ("CGS").**
- **p.3, the definition:** *"We define the null future inwards and outwards mean curvatures θ± of S as
  θ± := tr_γ(∇n±)"*.
- **pp.3–4, Theorem 3.1:**
  > *"Let t be a Cauchy time function on a space-time (M, g) with timelike boundary T = ∪ T_α, and satisfying the null
  > energy condition (NEC) … Suppose that there exists a component T₁ of T with compact level sets t|T₁ such that T₁ is
  > weakly inner future trapped with respect to t. If all connected components T_α, α ≠ 1, of T are inner past trapped
  > with respect to t, then J⁺(T₁) ∩ J⁻(T_α) = ∅ for T_α ≠ T₁."*
- **p.4, Remark 3.2:** *"The condition that at least one of the defining inequalities is strict is necessary."*
- **pp.7–8, eqs. (4.6) and (4.10):** far level sets are inner future and past trapped when *"±θ± > 0"*.
- **p.9:** *"our approach to topological censorship in this work requires uniformity in time of the mean null extrinsic
  curvatures of the spheres"*.

## Theorem W (the board's application of CGS Theorem 3.1)

### The premises

Let a five-dimensional spacetime carry your corridor's plane, and suppose:

- **W1. Null energy holds everywhere.**
  - A positive-tension plane meets it: DOORS K1, on H-COMPOSITE-SURFACE. Your item 139 makes ours positive.
  - CGS assume a smooth metric. So a thin plane is read as the limit of a thick one: H-THICK-PLANE, the board's.
    censor.py had already found that a thick plane keeps the null energy condition.
- **W2. The region between two far boundaries T₁, T₂ is globally hyperbolic,** with a Cauchy time function t.
- **W3. The plane's end 1 and end 2 lie in two distinct ends of the bulk.** Each end is cut off by a far boundary whose
  time slices are compact and untrapped (±θ± > 0), uniformly in time.

### The conclusion

- **Then no causal curve runs from T₁ to T₂** (CGS Theorem 3.1).
- **But your corridor's passage is such a curve.** It crosses end 1's far sphere inward and end 2's far sphere outward.
  - PASSAGE5D P6 adds timelike curves through the bulk between the two ends.
- **So the corridor cannot satisfy W1, W2 and W3 together.**

## What the mathematics gives

### C1. The boundaries W3 asks for exist, and are exactly as untrapped as in flat space (computed)

- **Take a Randall–Sundrum II bulk,** g = (ℓ/z)²(−dt² + dx² + dw²) with z = ℓ + |w| (the plane at w = 0).
- **The 3-sphere centred on the plane,** |x|² + w² = R², has **±θ± = 3/R exactly, at every point, on either side.**
  - That is as untrapped as a sphere in flat space.
  - Its time slices are 3-spheres, which are compact.
  - **Derivation.** For static T, tr(∇T) = 0. So θ± = ±(div n − a_n), where a is the static observers' acceleration.
    The warp's contributions cancel to leave 3/R.
- **Control:** a sphere centred on the AdS boundary (z = 0) has θ± = 0 everywhere.
  - It is marginal. It is the minimal surface of anti-de Sitter.
  - So the strictness CGS Remark 3.2 calls necessary fails, and the check can fail.

### C2. The passage crosses each far sphere once (STRUCTURAL)

- **On the plane, r = 2m + u² is monotone in |u| on each side of the throat.**

### C3. What the corridor needs in five dimensions

- **Your positive tension meets W1.** Your *"An NEC is never violated"* (items 117, 120) keeps that route closed. So
  Theorem W leaves exactly three ways for the corridor to exist:
  - **(a) The plane's two ends lie in one end of the bulk.**
    - They are then joined away from the corridor, through the deep bulk, where the bulk ends.
    - GLOBALBULK G3 reached the same requirement from the far field, independently: a lasting corridor needs its
      departure from Randall–Sundrum to reach the bulk's far horizon.
  - **(b) The far boundaries are not untrapped uniformly in time.** In Randall–Sundrum II they are, at 3/R (C1). So this
    needs an end whose far geometry does not behave even as a flat one does.
  - **(c) The five-dimensional spacetime is not globally hyperbolic.**
- **Control (READ in censor.py).** With a compact extra dimension, CGS Theorem 5.2 applies directly and forbids the
  passage. Your answer 9 (item 136) makes the dimension unbounded, so that control does not bind.

## What this does and does not show

- **It shows a censorship theorem that binds the corridor,** with every premise either met (W1, C1, C2) or named (W2, W3).
- **It shows that in a globally hyperbolic bulk the corridor's two ends cannot be two separate ends of the bulk.**
  - They must be one end, joined through the deep bulk.
  - Alternatively, a far end must fail to be untrapped.
- **It does not decide which escape holds, or whether one can.** In particular, whether a bulk exists in which the
  plane's two ends are one end of the bulk (a) is wall C's global question.

## Your rulings this bears on

- **Item 127 (the positions coincide).** Escape (a) is a geometric form of the two ends not being separate places. That
  this is what your item 127 describes is the board's reading, not shown here.
- **Item 136, answer 9 (an unbounded extra dimension).** It is what keeps CGS Theorem 5.2 from forbidding the passage
  outright.
- **Items 139 and 117/120.** With them, W1 is met, so the null energy route is closed.

## Named hypotheses

- **Yours:**
  - H-P2-NEGATIVE-PLANE, M-PROVE-POSITIVE (139);
  - H-STATIC-PLANES (141);
  - H-NEC-COIN (117, 120);
  - H-INFINITE-CLOSED (136.9);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-COMPOSITE-SURFACE;
  - H-THICK-PLANE;
  - H-ONE-PLANE-NEAR.

## OPEN

1. Which escape holds: (a) one end of the bulk, (b) far ends not untrapped, or (c) no global hyperbolicity.
2. A bulk in which the plane's two ends are one end of the bulk, joined through the deep bulk. This is wall C's global
   bulk.
3. The thin plane directly, without H-THICK-PLANE: CGS's proof with a distributional null energy condition.
