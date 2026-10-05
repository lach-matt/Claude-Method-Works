# Does Chung–Freese's higher dimension change gravity on our plane? (BULK2-O6; computed on M's order, item 67; verified once; not seated; 2026-10-05)

*First headed* "(BULK2-O6; computed on M's order, item 67; not verified; not seated; 2026-10-05)".

## What M asked

`SEARCHES.md` left this OPEN: whether Chung–Freese's warped shape changes gravity on our plane at the lengths the
torsion balances test. M (item 67): *"run this computation please"*.

It is worked by deduction from named premises (M-DEDUCE, item 64). H-HIGHER-CORRIDOR, H-BULK-PAIRING and
H-UNOBSERVED-UNBUILT are carried as M's hypotheses, never as results. O9 stays OPEN.

Every number is printed by `cfgravity.py`.
- **Selftest:** 9/9 checks, 2 of them controls, with 4 STRUCTURAL lines printed and not counted.
- **Verification:** verified once, with its findings applied (History).

## How it is computed

1. **Newton's law on our plane comes from the lapse, g₀₀ = 1 + 2Φ** (computed, check 1). For any static perturbation,
   the linearised R^0_0 is exactly ΔΦ, with Δ = e^{2ku}∂_z² + ∂_u² − 3k∂_u; the background R^0_0 = 0. The 5D Einstein
   equation then ties Φ to the bulk matter's response.
2. **The bulk matter responds** (computed, check 4). Chung–Freese's bulk is an isotropic perfect fluid (`pairing.py`).
   Hydrostatics fixes its pressure response, δp = −(ρ+p)Φ, which is never zero because ρ + p < 0. That is the same
   negative-energy-type condition `PAIRING.md` found.
3. **So the lapse picks up a mass term** (deduced): (Δ − m²)Φ = source, with m² = (4 + 2/c_s²)k², where c_s² is the
   fluid's sound speed squared.

   | the fluid's c_s² | m²/k² | what happens to Newton's law on our plane |
   |---|---|---|
   | +1 or +1/3 (ordinary stiff fluids) | +6, +10 | screened: it dies out beyond about 1/k |
   | −1 | +2 | screened |
   | **−1/2** | **0** | **survives** |
   | −1/4 | −4 | unstable |

   Newton's law survives only if the bulk fluid has c_s² = −1/2 exactly: the background's own p/ρ. A fluid like that is
   itself unstable to short waves. This file names that requirement **H-CF-FLUID**, and everything below assumes it. The
   planes' own matter must also respond in step; that is named **H-PLANE-EOS**, from the verifier's junction reading,
   not re-run here.
4. **The modes.** Under that premise the lapse obeys Δ, which is the same operator the graviton waves obey (check 2).
   - The static modes have a closed form, μ_n = nπk / (e^{kL} − 1): the inverse of the conformal length ∫e^{ku}du. Checked
     against an independent numerical solution (check 5).
   - Each mode adds a Yukawa term of strength approaching 2e^{−kL} (check 7). All modes share the same source factor, so
     the factor between them is 1 (computed).
   - A factor of 4/3 applies only if something restores pure 4D coupling to the zero mode, such as a stabilised radion
     (**H-STABILISED**; "the volume of the extra dimensions must be stabilized by radions", Adelberger et al. p.2).
   - **Control:** with no warp, each mode has strength 2. Under H-STABILISED that becomes Kapner et al.'s 8/3 for one
     extra dimension (READ, p.4; valid when the dimension is smaller than the closest separation tested) (check 6).
5. **Summed, the modes give δ(r) ≈ 2(1 − e^{−kL}) / (πkr)** (check 8). That is a 1/r² term in the potential, the
   five-dimensional law, not a single Yukawa.
6. **Two tests, both READ.**
   - Lee et al.: "percent-level measurements of G_N at separations down to about 50 μm" (p.2), read as |δ(52 μm)| ≲ 1 %
     (**H-PERCENT**). The calibration at 17–19 cm sees δ ≲ 3×10⁻⁴, so absorbing a constant into G changes nothing.
   - Adelberger et al. (Table I, p.3) fitted Kapner's data, which run from 55 μm to 9.53 mm, to exactly this shape:
     |β₂| ≤ 4.5×10⁻⁴ (68 %). That fit applies only where the power law spans the data.

## The result, at the illustrative L = 1 mm

| trip on our clock | 1/k | deviation at 52 μm (×4/3 if stabilised) | at 1 mm | at 3 mm | β₂ | verdict |
|---|---|---|---|---|---|---|
| 1 year | 691 μm | 6.2 (8.3) | 0.15 | 0.007 | 0.34 (fit not applicable: conformal length 2.3 mm) | excluded |
| 1 day | 136 μm | 1.7 (2.2) | 0.086 | 0.028 | 0.087 | excluded |
| 1 hour | 95 μm | 1.2 (1.6) | 0.061 | 0.020 | 0.060 | excluded |
| 1 second | 53 μm | 0.65 (0.87) | 0.034 | 0.011 | 0.034 | excluded |

Every design at 1 mm fails H-PERCENT by a factor of 65 or more. Where the fit applies (day, hour, second), its β₂ is 75
to 190 times Adelberger et al.'s fitted bound. Gravity at those lengths would be partly five-dimensional.

**The design survives with a thinner bulk:**

| trip on our clock | spacing L at most (H-PERCENT) | under H-STABILISED | by the β₂ fit | the NEC-violating density rises |
|---|---|---|---|---|
| 1 year | 18.8 μm | 17.5 μm | not applicable | ×3×10³ |
| 1 day | 6.4 μm | 4.9 μm | 5.2 μm (fit's range not fully spanned) | ×2×10⁴ |
| 1 hour | 8.6 μm | 6.5 μm | 7.4 μm | ×1×10⁴ |
| 1 second | 15.3 μm | 11.5 μm | 13.2 μm | ×4×10³ |

The needed warp kL barely depends on L, so the same trip times stand at these spacings, at the cost of a steeper warp.
The bulk's density, which violates the null energy condition, scales as k² and rises by (1 mm/L)².

## For M

- **The computation is done, and it found more than it was asked.**
- **First, a new price.** Chung–Freese's warped corridor can only keep Newton's law on our own plane if its bulk is a
  very particular fluid, one whose sound speed squared is exactly −½. For any other fluid our gravity would either fade
  out at short range or run away. That fluid is itself unstable to short waves. So the warped shape carries a further
  price beyond its negative-energy-type matter: a fine-tuned, unstable filling. Chung–Freese call their solution
  fine-tuned (p.8); this is a concrete form of that.
- **Second, if that fluid is granted:** at a 1 mm spacing our gravity would be measurably five-dimensional at tabletop
  distances. The torsion balances found Newton ("Newtonian gravity gave an excellent fit to our data", Lee p.1), so that
  is excluded by factors of 65 or more.
- **Third, a thinner corridor survives.** With planes about 5 to 19 μm apart it gives the same trip times, from one second
  to one year for the Proxima span on our clock. The cost is a warp, and a negative-energy-type density, thousands of
  times stronger.
- **This is a real experimental edge.** A corridor just under these limits predicts a 1 % excess of gravity at 52 μm,
  right at the edge of what Lee et al. resolved. They write that "environmental vibrations prevented us from probing
  separations smaller than 52μm" (p.5). Shorter separations, or better precision, would test exactly this corridor.

## Named hypotheses

- **H-CF-FLUID:** the bulk is a barotropic fluid with c_s² = −1/2. Under any other perfect fluid the result does not
  stand.
- **H-PLANE-EOS:** the planes' matter responds as the verifier's junction reading has it.
- **H-ORBIFOLD:** the bulk is symmetric about each plane.
- **H-STABILISED:** the ×4/3 factor.
- **H-PERCENT:** the 1 % criterion.
- **Carried from pairing.py:** H-CF-STATIC and H-L-ILLUSTRATIVE.
- **M's:** H-HIGHER-CORRIDOR, H-BULK-PAIRING and H-UNOBSERVED-UNBUILT.

## OPEN

1. A fluid, or a field, that realises c_s² = −1/2 stably. Without one, Chung–Freese's warped corridor does not keep
   Newton's law on our plane.
2. The planes' junction conditions re-run here (H-PLANE-EOS).
3. The zero mode's spatial part, which sets how much light bends (the PPN γ). It is a solar-system test, not computed.
4. A full fit of the power-law deviation to Lee et al.'s data. A fitted bound for Kapner's data is READ and gives
   spacings within about 20 % of H-PERCENT's.

## History (verifier, 2026-10-05; first-written claims kept)

- **The potential was first derived from the wave mode alone.** It read *"gamma obeys box gamma = 0 (DEDUCED from S1 and
  H-CF-FLUID)"*. Newton's law comes from the lapse, and there the fluid does respond unless c_s² = −1/2. The mass term
  for any other fluid is now deduced, and H-CF-FLUID is sharpened to that one value.
- **Every Yukawa was first multiplied by 4/3** (H-TENSOR-4/3), and H-NO-BENDING was named. The computed factor is 1, and
  ×4/3 needs a stabilised radion. Brane bending cannot enter, because time is unwarped.
  - The first figures were the ×4/3 ones: deviations of 0.87–8.3 at 52 μm, and spacings of 4.9–17.5 μm.
  - The computed figures are 0.65–6.2 and 6.4–18.8 μm.
- **The first control could not fail.** With the perturbation in g_xx, δG^x_y vanishes by symmetry. The control now
  compares against the flat operator.
- **"The hidden plane's static length, which the warp makes long."** It is a conformal length, not a proper one.
- **"Below about 10 μm of separation the balances can't yet see it."** That confused the plane spacing with the test
  separation.
