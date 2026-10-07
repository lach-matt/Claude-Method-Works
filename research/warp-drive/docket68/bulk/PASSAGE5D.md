# Wall D, the theorem: what the bulk makes of the passage (M-RULINGS item 149; proved, computed and READ; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## Why this theorem

- **DOORS.md, OPEN 1:** *"A censorship theorem for passage between asymptotic regions of a plane in a bulk. None was
  READ, so it would have to be proved."*
- **This note proves what your corridor's own geometry decides,** and names exactly what it leaves open.
- **The instrument:** `passage5d.py`, which imports bulkseries.py and copy/coin.py by path. Selftest 7/7, about 6 s.
  - **Genuine checks:** five.
  - **Controls:** two (the black string; a non-umbilic foil).
  - **Marked STRUCTURAL:** P1, which has no check.

## The setting

- **The corridor** is eq. (17) at r₀ = 2m.
- **It sits on a Randall–Sundrum plane,** K = c·g with c constant, of either sign.
- **The bulk is vacuum with Λ₅.** localbulk.py proved such a bulk exists near the plane, and bulkseries.py computed it.
- **The passage γ** is the plane's radial light ray from end 1, through the throat, to end 2.
  - In stability.py's chart it is v = const, with affine parameter λ = −ρ. It is complete.
  - With r = 2m + u², u > 0 is side 1 and u < 0 is side 2.

## Theorem D

### P1. The passage is a light ray of the bulk (STRUCTURAL)

- **Its acceleration off the plane is K(k, k) = c·g(k, k) = 0.** This is UMBILIC.md U1.

### P2. Along the passage, the bulk's null energy is zero, and its pull toward the bulk is exactly the plane's deficit

- **The identity:** R⁵(n,k,n,k) = −R⁴(k,k) = 2r″/r = (m/2)/((r − 3m/2)²·r), which is positive everywhere on the passage.
- **Proof:**
  - R⁵(k,k) is the sum of R⁵(e,k,e,k) over the transverse frame. It is zero in a vacuum-Λ bulk, since g(k,k) = 0.
  - Gauss gives R⁵(e,k,e,k) = R⁴(e,k,e,k) for e tangent to the plane. The K-terms are c²·(g(e,e)g(k,k) − g(e,k)²) = 0.
  - For this congruence R⁴(k,k) = −2r″/r (Raychaudhuri, with no shear).
- **Computed from the bulk series rather than assumed.**
  - **Control:** the black string reads 0 for both.
  - **Foil:** a first-order term that is not umbilic breaks the identity. The residual is −2δr/(ℓ²(r − 2m)).
- **What this means.** The plane's apparent violation of null energy is, point by point, the bulk's tidal pull in the
  normal direction. The total in five dimensions is zero.
  - This makes exact the board's reading of your items 117 and 120 (DOORS K2): the condition holds in five dimensions
    and only appears violated on the plane.
- **It also settles one premise.** The five-dimensional generic condition holds along the whole passage. censor.py C3 had
  left it "plausible".

### P3. Integrated, the bulk's pull equals the plane's averaged deficit

- **Q = ∫R⁵(n,k,n,k) dλ = 8/(3m) − (4/(3√3·m))·artanh(√3/2) = 1.652872/m** (exact closed form, computed).
- **That is exactly minus the plane's averaged null energy over both legs.** It equals 2 × 0.826436 from coin.py's closed
  form (imported).

### P4. Lemma (Sturm; proved here)

- **Statement.** If q ≥ 0 is integrable on the whole line and ∫q > 0, then J″ + qJ = 0 has a solution with two zeros.
- **Proof.**
  - Take the quadratic form I[f] = ∫(f′² − qf²).
  - Let f = 1 on [−L, L], falling linearly to 0 over a further length L² on each side. Then I[f] = 2/L² − ∫qf², which
    tends to −Q < 0.
  - A negative form on [a, b] with f(a) = f(b) = 0 means a conjugate pair inside (Jacobi).
- **Witness for the corridor's q:** I[f] = −1.594 at L = 6 (computed).

### P5. The conjugate points, computed

- **A point p of the passage on side 1 has a conjugate point toward the bulk if and only if it lies beyond
  r_* = 2.21007m.** That is 0.69107m of affine parameter before the throat.
- **Its conjugate point lies on side 2.** It moves inward as p recedes, and tends to r_* on side 2 as p goes to end 1's
  infinity.

| p on side 1 | its conjugate point on side 2 |
|---|---|
| r = 2.25m | r = 29.5m |
| r = 3m | r = 3.43m |
| r = 27m | r = 2.254m |
| r = 902m | r = 2.211m |

- **Two separate routes give r_*:**
  - the limit from end 1, u = −0.45835;
  - the zero of end 2's asymptotically constant solution, u = +0.45834.
  - They agree, mirrored across the throat.
- **Points nearer than r_* on side 1, and all of side 2, have no conjugate point.**

### P6. So the passage is not the fastest route in five dimensions

- **The standard result** (Hawking–Ellis Prop. 4.5.12, standard, not READ): beyond a conjugate point, a light ray is
  joined to its starting point by a timelike curve, inside any neighbourhood of the segment.
- **Here that curve runs on the bulk side,** because the Jacobi field's normal part is positive between the pair. The
  segment is compact, so it lies within the local bulk.
  - Keeping the curve on one side of the plane adapts the standard proof to a bulk with a boundary. That adaptation is
    the board's.
- **So every point of end 1 beyond r_* is joined by a timelike curve through the bulk to points of end 2.** The bulk is
  a faster route between your plane's two ends than the passage itself.

## Corollary: what censorship can still say

- **In five dimensions, the plane's two ends are joined by timelike curves through the bulk.**
- **Two premises of a five-dimensional censorship theorem are now met:**
  - **null energy:** for the composite plane, DOORS K1 (positive tension, H-COMPOSITE-SURFACE);
  - **the generic condition:** along the passage (P2).
- **So if a five-dimensional topological censorship theorem holds for a bulk bounded by a plane, the corridor can meet it
  only through its remaining premises.** No such theorem is READ or proved here. The remaining premises are:
  - global hyperbolicity of the five-dimensional spacetime;
  - the plane's two ends being distinct ends of it.
- **Those are wall C's global questions** (GLOBALBULK.md). Wall D now reduces to them, and to nothing else.

## Your rulings this bears on

- **Item 117 and item 120 (H-NEC-COIN; "An NEC is never violated").** P2 is the exact form of the board's reading of
  them: in five dimensions the null energy along the passage is zero, and the plane's deficit is the bulk's pull.
- **Item 127 (the positions coincide).** If the two ends are one end of the bulk, censorship's last premise fails, and
  nothing READ forbids the passage. Whether they are is not decided here.
- **DOORS K4 (the channel).** P6 gives the board a timelike route between the two asymptotic regions, through the bulk.
  Whether it can carry the README is not worked here.

## Named hypotheses

- **Yours:**
  - H-STATIC-PLANES (141);
  - H-NEC-COIN (117, 120);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-ONE-PLANE-NEAR;
  - H-COMPOSITE-SURFACE (for the corollary's energy premise);
  - the one-sided adaptation of Hawking–Ellis 4.5.12 (P6).

## OPEN

1. A five-dimensional topological censorship theorem for a bulk bounded by a plane. Neither READ nor proved; the
   corollary says which premises it would turn on.
2. Wall C's global premises: global hyperbolicity, and whether the plane's two ends are distinct ends of the bulk.
3. Whether the bulk's timelike route (P6) can carry a README.
