# C, first part: the corridor read on one static plane (M-RULINGS items 127, 138, 140, 141; READ and computed; verified once; not seated; 2026-10-07)

*First headed* "C, first part: the corridor on one static plane, and k from the corridor (… not verified …)". **Its
numeric window for k and its "throat widens" result failed verification and are withdrawn** (History).

## Where this starts, and the premise it rests on

- **Item 141:** the planes are static, and a stable throat forms between them.
- **Item 140:** *"Our math is not dependent on k, k is dependent on our work."*
- **static.py:** static and face to face, your two planes act as one Randall–Sundrum II plane at long range (zero modes
  only).
- **This reads the corridor on that one static plane** (H-RS2-ONE-PLANE, the board's).
  - The corridor is Bronnikov–Kim eq. (17) at r₀ = 2m (H-BK-CORRIDOR, the board's).
  - Reading "a stable throat" as a static corridor during the hold is also the board's (H-STABLE-THROAT).
- **That premise stands against your item 138:** *"you assume the bulk is contained to a single plain. It is not."*
  - Your other planes are not in this calculation.
  - MK p.16: *"the gravitational influence of the second brane is felt via its contribution to E_μν"*, the bulk's field
    read on the plane. So other planes could add exactly the field this note finds missing.
  - Everything below holds only under the one-plane reduction.
- **The instrument:** `throatbulk.py`. Selftest 11/11.
  - **Controls:** one (Schwarzschild).
  - **Contrasts:** one (a large black hole).
  - **Marked STRUCTURAL:** three.
- **READ:** Maartens–Koyama, *Living Rev. Rel.* 13 (2010) 5, arXiv:1004.3962v2 ("MK"), pp.10, 16, 26–29.

## What passes

### 1. Your corridor is a no-matter plane, its curvature read from the bulk (T1)

- **MK eq. (143), p.26:** a plane with no matter on it obeys R_μν = −E_μν, where E is the bulk's Weyl curvature read on
  the plane. Its curvature scalar must vanish.
- **Eq. (17) has R = 0.** That is how Bronnikov–Kim's family is built (STRUCTURAL), so it is a solution of that kind.
- **A misprint found in the source.** MK's eq. (151) as printed fails their own eq. (160) in the case F = H.
  - With a factor H on F′/F, it passes eq. (160), and it agrees with tracelessness on eq. (17).
  - The board uses the corrected form.

### 2. At its throat, the corridor asks the bulk for a full-strength field (T2)

- **The corridor's bulk reading at the throat is E^θ_θ = −1/r₀².** That is the throat's own curvature scale, with no
  suppression.
- **One static plane gives much less to anything large against ℓ.**
  - A region whose curvature length L is much larger than ℓ reads E only of order ℓ²/L⁴. That is MK eq. (41)'s
    correction.
  - Figueras–Wiseman (READ in KSCALE.md) say the same at leading order: such a plane is Ricci-flat.
- **So a throat much larger than ℓ is excluded:** the plane could not give it the field it needs.
- **Control:** the Schwarzschild member of eq. (17) reads E = 0.

### 3. A throat much smaller than ℓ sits in five-dimensional gravity (T3, heuristic)

- **Below ℓ the field is five-dimensional.** MK eqs. (40) and (41)'s leading terms meet at r = ℓ.
- **Eq. (17) is four-dimensional**, so its throat should not be much smaller than ℓ.
- **This is a heuristic in MK's own style.** MK fix the tidal charge with eq. (40) in the strong field, p.28.
- **Carrying it from small black holes to a wormhole throat is the board's step** (H-5D-TRANSFER).

### 4. So, on one static plane, ℓ is of the order of the throat (T4)

- **Under these premises the bulk's curvature length ℓ = 1/k must be of the order of r₀ = r_min(N).**
  - This is KSCALE.md's way out (c), *"Only r₀ ~ ℓ is open"*, now reached from the corridor's side.
  - It is an order of magnitude. No factor is claimed.
- **At the board's example README:** r_min = 3.976×10⁻²⁸ m, so k is of order 2.5×10²⁷ m⁻¹.
- **Read per README, this makes k depend on N** (H-K-PER-README, the board's reading). That is the board's application,
  not your item 127.
  - Item 127 frames variation as our universe against a counterfactual one, not as one README against another.
  - **Its costs:**
    - the bulk's curvature changes from one passage to the next;
    - so does the 5D Planck mass at fixed G (MK eq. 27);
    - two corridors at once would need two k's;
    - item 127's first step, k's value in our current state, is not supplied, because our current state holds no
      corridor (item 129).

### 5. That bulk is classical for many bits, and static is self-consistent (T5)

- **The bulk is classical for many bits.** With ℓ ~ r_min, its curvature length against the 5D Planck length is about
  8.5×10⁴ at the example README. At one bit it is 0.60, not classical (kderive.py K2 and K4: H-MANY-BITS).
- **Static is self-consistent for a near-instantaneous hold.** Light crosses ℓ in about 1.3×10⁻³⁶ s at the example
  README. A static treatment stays self-consistent even for a "near instantaneous" hold (item 136 E). That answers
  kderive's withdrawn objection about static results.

### 6. Just off the plane (T6)

- **MK eq. (148)** gives the bulk off a no-matter plane in g̃ = e^{2|y|/ℓ}g, the metric with the warp factor removed.
- **In g̃, your throat's sphere grows away from the plane: g̃_θθ(r₀, y) = 4m² + y² + 2y³/ℓ.** That is because
  E_θθ(r₀) = −1.
- **Contrast (READ):** a large black hole's E_θθ → 2mℓ²/(3r³) > 0, so its g̃ sphere shrinks (MK's "pancake-like").
- **The physical sphere includes the warp factor, and it shrinks at first order: 4m² − 8m²y/ℓ** (STRUCTURAL).
- **So the throat flares relative to the black-string profile, opposite to a black hole, while its physical area
  still falls into the bulk.**
- **MK's caution, p.27:** *"However, note that the horizon shape is tubular in Gaussian normal coordinates."* At
  r₀ = 2m the throat sits on the horizon, and the expansion is short-range only.

## What it costs, under the one-plane reduction

- **The corridor's far-field signature is no longer predicted.**
  - On one static plane, any localized object's far field is Schwarzschild's (γ = 1).
  - So KSCALE.md's candidate observables are not predicted: light bending 9/8, time delay 9/8, perihelion 13/12, under
    M-DERIVE-OBSERVABLE.
  - So are plane.py's far-field mass readings (Komar m, the ADM total): the far mass is unknown.
- **Measurement cannot confirm a k of order 10²⁷ m⁻¹.** That is beyond any test of gravity. Your H-K-BY-MEASUREMENT
  (item 136, answer 8) says measurement would confirm, and for this k it cannot.
- **The exact relation between k and r₀ needs the full bulk solved off the plane.** None is known for eq. (17).
  - MK p.29, for static black holes: they are *"found if the horizon is small compared to ℓ, but no numerical
    convergence can be achieved close to ℓ"*. That is exactly where this puts the throat.
  - Figueras–Wiseman (READ in OUTSIDE.md) built static Randall–Sundrum II black holes up to about 20ℓ. Their method is
    the natural one to try.

## What this does and does not show

- **It shows, on one static plane:**
  - eq. (17) is a no-matter plane solution;
  - at its throat it asks the bulk for a field at the throat's full strength;
  - so a throat much larger than ℓ is excluded;
  - by a heuristic, one much smaller is too;
  - the bulk is classical for many bits, and static is self-consistent.
- **It does not show:**
  - a factor between k and r₀;
  - that a bulk carrying eq. (17) exists;
  - **anything with your other planes (item 138).** They could supply the field the one plane lacks, and they are the
    next thing to compute.

## Named hypotheses

- **Yours:**
  - H-STATIC-PLANES (141);
  - M-K-FROM-THE-WORK (140);
  - H-MULTIVERSAL-BULK (138), not used here and against this note's premise;
  - H-INFINITE-PLANES (123–124);
  - H-COEFF-FROM-CURRENT (127);
  - H-K-BY-MEASUREMENT (136).
- **The board's:**
  - H-RS2-ONE-PLANE (against item 138);
  - H-BK-CORRIDOR;
  - H-STABLE-THROAT;
  - H-FACE-TO-FACE;
  - H-5D-TRANSFER;
  - H-K-PER-README;
  - H-VACUUM-AS-SOURCE (a no-matter corridor compared with a mass-sourced field);
  - H-LR-ZERO-MODE's scope (static.py);
  - H-MANY-BITS.

## OPEN

1. **Your other planes (item 138):** what they add to the bulk's field on ours, with the planes static. This is where
   the corridor's missing far field could come from.
2. The full static bulk off the plane (Figueras–Wiseman's method), and the factor between k and r₀.
3. The transition from eq. (17) near the throat to the far field.

## History (verifier, 2026-10-07)

Sixteen findings, all applied:

1. **"The throat widens" ignored the warp factor.** MK's eqs. (148) and (154) are for g̃. The physical sphere shrinks at
   first order. Eq. (154) as printed is dimensionally inconsistent; the board now uses eq. (148), whose y² coefficient
   is −E_θθ. MK's "tubular" caution is quoted.
2. **The meeting radius r_× = 1.633ℓ, and the window it gave, are withdrawn.**
   - MK eq. (155) is a weak-field far form, not a ceiling on what one plane supplies.
   - The corridor's full ψ vanishes at the throat, so with it the "edge" disappears for every ℓ.
   - Only "r₀ of order ℓ" survives, now argued from E at the throat.
3. **Item 138 was ignored.** The one-plane premise is now named as the board's and against your ruling, and the other
   planes' contribution is the first OPEN item.
4. **H-BK-CORRIDOR** is the board's, not yours.
5. **"k varies with N" was the board's reading of item 127**, and was presented as yours. It is now H-K-PER-README, with
   its costs.
6. **"The corridor now fixes the scale, to within a factor of order one" was over-claimed.** It is now a conditional
   order of magnitude.
7. **The selftest under-marked STRUCTURAL.** The transcription match and the pure arithmetic are marked or removed. The
   weak control "far above the floor" is dropped.
8. **Unnamed hypotheses are named:** H-RS2-ONE-PLANE, H-VACUUM-AS-SOURCE, H-5D-TRANSFER, and the zero-mode scope.
9. **The losses are stated:** the γ = 5/4 observables, and the far-field mass readings.
10. **MK p.29's caution at r ~ ℓ, and Figueras–Wiseman's method**, are cited.
11. **Eq. (151) is MK's misprint**, witnessed by their own eq. (160). The board's form was right, and the corrected one
    is now checked.
12. **T3 is labelled a heuristic.**
13. **The upper side now uses E at the throat** with Figueras–Wiseman's leading-order statement, in the right direction.
14. **Static is self-consistent** at ℓ ~ r₀, from the light-crossing time.
15. **The measured bound** is no longer described as the strongest one read. That k cannot be confirmed by measurement
    is now stated.
16. **"No bulk solution … for every such brane metric"** went beyond MK. It is now scoped to eq. (17).
