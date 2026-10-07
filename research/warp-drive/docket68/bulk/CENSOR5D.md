# Wall D, the censorship theorem: a passage between two ends of a plane in a bulk (M-RULINGS items 136, 139, 141, 149; READ, computed and deduced; verified once; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)". The first draft did not say which spacetime the theorem is
applied to. It read "a thick plane keeps the null energy condition" as enough for a composite of two sheets. It filed the
far-field requirement under the wrong escape, and said the escapes were "exactly three". It also over-stated a control.
All are corrected (History).

## Why

- **DOORS.md, OPEN 1:** *"A censorship theorem for passage between asymptotic regions of a plane in a bulk. None was
  READ, so it would have to be proved."*
- **PASSAGE5D.md showed that the four-dimensional route cannot be lifted.** In five dimensions the passage is not a null
  line of the bulk.
- **This note supplies the theorem by a different route:** a published theorem for spacetimes with timelike boundaries,
  applied to your corridor with boundaries the board computes. It needs neither the generic condition nor completeness.
- **The instrument:** `censor5d.py`, which imports doors.py and passage5d.py by path. Selftest 4/4, about 2 s.
  - **Genuine checks:** two.
  - **Control:** one.
  - **Marked STRUCTURAL:** one.

## READ

- **Chruściel, Galloway and Solis, arXiv:0808.3233v2 ("CGS").**
- **p.3, the definition:** *"We define the null future inwards and outwards mean curvatures θ± of S as
  θ± := tr_γ(∇n±)"*, with n outward and the future null normals normalised by g(n, n±) = ±1.
- **pp.3–4, Theorem 3.1:**
  > *"Let t be a Cauchy time function on a space-time (M, g) with timelike boundary T = ∪ T_α, and satisfying the null
  > energy condition (NEC) … Suppose that there exists a component T₁ of T with compact level sets t|T₁ such that T₁ is
  > weakly inner future trapped with respect to t. If all connected components T_α, α ≠ 1, of T are inner past trapped
  > with respect to t, then J⁺(T₁) ∩ J⁻(T_α) = ∅ for T_α ≠ T₁."*
- **p.4, Remark 3.2:** *"The condition that at least one of the defining inequalities is strict is necessary."*
- **p.5, Theorem 3.5,** on the same premises: *"any causal curve included within ⟨⟨T⟩⟩ with end points on T can be
  deformed, keeping end points fixed, to a curve included in T"*.
- **pp.7–8, eqs. (4.6) and (4.10):** far level sets are inner future and past trapped when *"±θ± > 0"*.
- **p.9:** *"our approach to topological censorship in this work requires uniformity in time of the mean null extrinsic
  curvatures of the spheres"*.
- **How the board reads the conventions.**
  - Weakly inner future trapped means θ− ≤ 0. Inner past trapped means θ+ > 0, because the past inward normal is −n+.
  - So for far spheres the condition is ±θ± > 0.
  - Read literally, p.3's "changing ≤ to ≥" would suggest otherwise. The board's reading is the one consistent with
    eqs. (4.2), (4.6) and (4.10) and with p.3's Schwarzschild example.

## Theorem W (the board's application of CGS Theorem 3.1)

### The spacetime it is applied to

- **The theorem is applied to the mirror-doubled spacetime,** with the plane as an interior shell. It is not the one-sided
  bulk.
  - In the one-sided bulk, the plane is itself a timelike boundary that meets the far spheres. Their union is then one
    connected component with corners, and Theorem 3.1 says nothing.
- **Causal curves pass between the doubled spacetime and the one-sided bulk by reflection at the plane.**

### The premises

Let the doubled five-dimensional spacetime carry your corridor's plane, and suppose:

- **W1. Null energy holds pointwise on a smooth metric.**
  - CGS assume smoothness, so the thin plane is replaced by a thickening (H-THICK-COMPOSITE, the board's).
  - The thickening is of the face-to-face composite, and it must keep the null energy condition at every point.
  - That is stronger than censor.py's remark that "a thick plane keeps NEC". The composite's summed tension is positive
    (DOORS K1, on H-COMPOSITE-SURFACE). But position 2's sheet alone reads −(1/3)λ_RS·k_y², and DOORS.md warns that
    thickening the two sheets with different profiles could break the condition pointwise.
- **W2. The region M between two far boundaries T₁, T₂ is globally hyperbolic,** with a Cauchy time function t.
  - M has no other boundary components, or every other one is inner past trapped.
  - Other planes (MANYPLANES.md, items 123–124) and excised singular regions would count as components.
- **W3. The plane's end 1 and end 2 lie in two distinct ends of the bulk.** Each end is cut off by a far boundary whose
  time slices are compact and strictly untrapped (±θ± > 0), uniformly in time.

### The conclusion

- **Then no causal curve runs from T₁ to T₂** (CGS Theorem 3.1).
- **But your corridor's passage is such a curve.** In the doubled spacetime it lies on the plane, inside M, between its
  crossings of T₁ and T₂.
- **So the corridor cannot satisfy W1, W2 and W3 together.**
- **This holds however brief the hold.** The theorem binds the whole spacetime.

## What the mathematics gives

### C1. In a Randall–Sundrum II bulk, the far boundaries W3 asks for exist (computed)

- **Take g = (ℓ/z)²(−dt² + dx² + dw²), with z = ℓ + |w|.** This is the doubled form, with the plane at w = 0.
- **The 3-sphere centred on the plane,** |x|² + w² = R², has **±θ± = 3/R exactly, at every point, on either side.**
  - That is as untrapped as a sphere in flat space.
  - Its time slices are compact (S³).
  - **Derivation.** For static T, tr(∇T) = 0. So θ± = ±(div n − a_n), where a is the static observers' acceleration.
  - **The verifier's analytic form** is H = 3(ℓ + c)/(ℓρ) for a sphere centred at depth c. It stays positive across a
    smoothed even warp, so C1 survives a thick plane.
- **Control:** a sphere centred on the AdS boundary (z = 0) has θ± = 0 everywhere. It is marginal, so the strictness CGS
  Remark 3.2 calls necessary fails, and the check can fail.
- **Scope:** C1 is computed in pure Randall–Sundrum II. For a bulk that carries the corridor, W3 remains a hypothesis.

### C2. The passage crosses each far sphere once (STRUCTURAL)

- **On the plane, r = 2m + u² is monotone in |u| on each side of the throat.** The areal r matches the flat |x| only far
  out.

### C3. What the corridor needs in five dimensions

Your positive tension (item 139) and *"An NEC is never violated"* (items 117, 120) are what W1 rests on. With them, the
corridor needs at least one of four things:

- **(a) The plane's two ends lie in one end of the bulk.** They are then joined away from the corridor, through the deep
  bulk.
  - (a) is not free. With one end, CGS Theorem 3.5 applies on the same premises. The passage must then be deformable,
    with its ends fixed, into the single far boundary: the throat's handle has to be filled through the bulk.
  - Under H-BRIEF-HOLD, a corridor made from an ordinary plane in a globally hyperbolic spacetime cannot change the
    topology. So Theorem 3.5, not Theorem 3.1, is then the statement that governs.
- **(b) No far boundary has compact, strictly untrapped time slices, uniformly in time.**
  - This is where GLOBALBULK G3 points for a lasting corridor. A departure from Randall–Sundrum that reaches the bulk's
    far horizon over the core meets every sphere centred on the plane, since such a sphere reaches depth ℓ + R above its
    centre.
  - *First written:* G3 filed under (a) as "the same requirement", and (b) described as needing "an end whose far
    geometry does not behave even as a flat one does". Both withdrawn: a non-compact departure and one end of the bulk
    are different statements.
- **(c) The five-dimensional spacetime is not globally hyperbolic.**
- **(d) The thin plane is not the limit of a pointwise null-energy thickening of the composite.** W1 then fails in the
  form CGS need.

These are exhaustive only with W2's condition on other boundary components.

- **On the control.** *First written:* "a compact extra dimension gives CGS Theorem 5.2 directly, and forbids the
  passage". That over-claimed. censor.py says only that a compact internal space meets one of Theorem 5.2's premises.
  - Randall–Sundrum I's second plane has negative tension, so null energy fails there.
  - A warped interval with planes is not CGS's product form ℝ×N×Q (§4).
  - Withdrawn.

## What this does and does not show

- **It shows a censorship theorem that binds the corridor.**
  - W1 rests on a stated hypothesis about the composite.
  - W2 and W3 are named premises; C1 shows W3 can be met in Randall–Sundrum II.
- **It shows that in a globally hyperbolic bulk with a pointwise null-energy composite, the corridor's two ends cannot be
  two distinct, untrapped ends of the bulk.**
- **It does not decide which escape holds.**

## Your rulings this bears on

- **Item 127 (the positions coincide).** Escape (a) is a geometric form of the two ends not being separate places. That
  this is what item 127 describes is the board's reading, not shown here.
- **Items 139 and 117/120.** They supply W1's sign. H-THICK-COMPOSITE supplies its pointwise form.
- **Items 123–124 (many planes).** Other planes would be further boundary components. W2 requires them to be inner past
  trapped.

## Named hypotheses

- **Yours:**
  - H-P2-NEGATIVE-PLANE, M-PROVE-POSITIVE (139);
  - H-STATIC-PLANES (141);
  - H-NEC-COIN (117, 120);
  - H-INFINITE-CLOSED (136.9);
  - H-BRIEF-HOLD (86.5);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-COMPOSITE-SURFACE;
  - H-THICK-COMPOSITE;
  - H-ONE-PLANE-NEAR.

## OPEN

1. Which escape holds: (a), (b), (c) or (d).
2. Under (a): filling the throat's handle through the bulk (CGS Theorem 3.5), and how a brief hold could change the
   topology at all.
3. Under (b): whether a lasting corridor's non-compact departure (GLOBALBULK G3) leaves any far boundary untrapped.
4. The thin plane directly: CGS's proof with a distributional null energy condition (escape (d)).

## History (verifier, 2026-10-07)

Three must-fix and four should-fix, all applied:

1. **Which spacetime.** The theorem is applied to the mirror-doubled spacetime, with the plane as an interior shell.
2. **The thickening.** A pointwise null-energy thickening of the composite (H-THICK-COMPOSITE) replaces "a thick plane
   keeps NEC".
3. **The escapes.** G3's requirement is filed under (b), and (b) is restated broadly. (a) and a non-compact departure are
   distinguished.
4. **"Exactly three" over-claimed.** W2 now carries the condition on other boundary components, and the thin plane is a
   fourth escape (d).
5. **(a) is not free:** CGS Theorem 3.5.
6. **The compact-dimension control over-claimed.** Withdrawn.
7. **"Every premise met or named" over-stated C1.** C1 is pure Randall–Sundrum II; W3 remains a hypothesis.

Notes taken up: the convention mapping is stated; and C1 survives a smoothed even warp.
