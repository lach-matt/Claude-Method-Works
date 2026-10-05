# Does Chung–Freese's higher dimension change gravity on our plane? (BULK2-O6; computed on M's order, item 67; not verified; not seated; 2026-10-05)

## What M asked

`SEARCHES.md` left this OPEN: whether Chung–Freese's warped shape changes gravity on our plane at the lengths the
torsion balances test. M (item 67): *"run this computation please"*.

It is worked by deduction from named premises (M-DEDUCE, item 64). H-HIGHER-CORRIDOR, H-BULK-PAIRING and
H-UNOBSERVED-UNBUILT are carried as M's hypotheses, never as results. O9 stays OPEN.

Every number below is printed by `cfgravity.py`.
- **Selftest:** 6/6 checks, 2 of them controls, with 3 STRUCTURAL lines printed and not counted.
- **Owners it asks:** `bulk.py`, `pairing.py` and `searches.py`.

## How it is computed

1. **The bulk is a perfect fluid** (H-CF-FLUID). `pairing.py` computed Chung–Freese's bulk stress-energy as
   (−6, −3, −3, −3, −3)k². That is an isotropic perfect fluid; Chung–Freese do not say what it is made of.
2. **Gravitational waves in that bulk obey the plain wave equation** (computed, check 1). For a transverse-traceless
   perturbation of Chung–Freese's metric, the linearised Einstein tensor is exactly −½ times the wave operator. A
   perfect fluid does not source such a perturbation, so the wave equation holds.
3. **The static modes have a closed form** (deduced, then checked against an independent numerical solution: check 2):
   μ_n = nπk / (e^{kL} − 1).
   This is the inverse of the hidden plane's static length, which the warp makes long.
4. **Each mode adds a Yukawa term to Newton's law** on our plane.
   - Its range is 1/μ_n. For large n its strength approaches **2e^{−kL}** (check 3), times 4/3 for a massive graviton
     (H-TENSOR-4/3).
   - **Control:** with no warp (k → 0) this gives one flat extra dimension, with strength 8/3 and range R. That is exactly
     the value Kapner et al. state for a single extra dimension (READ, p.4).
5. **Summed, the modes give a power law, not a single Yukawa:** δ(r) ≈ 8(1 − e^{−kL}) / (3πkr) (check 5).
6. **The test** (H-PERCENT). Lee et al. call their work "percent-level measurements of G_N at separations down to about
   50 μm" (p.2, READ). This is read as a requirement that the deviation at 52 μm be at most about 1 %. That is a criterion,
   not a fit to their data.

## The result, for pairing.py's designs at the illustrative L = 1 mm

| trip on our clock | kL | 1/k | deviation from Newton at 52 μm | at 1 mm | at 3 mm | under H-PERCENT |
|---|---|---|---|---|---|---|
| 1 year | 1.45 | 691 μm | 8.3 | 0.21 | 0.010 | excluded |
| 1 day | 7.35 | 136 μm | 2.2 | 0.11 | 0.038 | excluded |
| 1 hour | 10.52 | 95 μm | 1.6 | 0.081 | 0.027 | excluded |
| 1 second | 18.71 | 53 μm | 0.87 | 0.045 | 0.015 | excluded |

**So yes: at the illustrative 1 mm spacing, Chung–Freese's bulk changes gravity on our plane by far more than the
torsion balances allow.** Gravity at those lengths would be partly five-dimensional.

**The design survives with a thinner bulk.** Keeping the deviation at 52 μm within about 1 % needs:

| trip on our clock | 1/k at most | plane spacing L at most |
|---|---|---|
| 1 year | 12.1 μm | 17.5 μm |
| 1 day | 0.66 μm | 4.9 μm |
| 1 hour | 0.62 μm | 6.5 μm |
| 1 second | 0.61 μm | 11.5 μm |

The trip time barely depends on L, because the crossing term 2L/c is negligible against these times. So the designs stand
at these smaller spacings, with a stronger warp per metre.

## For M

- **The computation is done, and it gives a sharp answer.** If the two planes were 1 mm apart, the warp would make our own
  gravity measurably five-dimensional at tabletop distances, and the torsion balances would have seen it. They didn't.
- **The corridor shape survives, but thinner.** A Chung–Freese corridor whose planes are at most about 5–17 μm apart
  passes the same test. It gives the same trip times (one second to one year for the Proxima span on our clock), with a
  steeper warp.
- **This puts a real experimental edge on your two-plane picture.** Below about 10 μm of separation the balances can't yet
  see it. Lee et al. write that "environmental vibrations prevented us from probing separations smaller than 52μm"
  (p.5). Better short-range gravity experiments would test exactly this corridor.

## Named hypotheses

- **H-CF-FLUID:** Chung–Freese's bulk matter is a perfect fluid, as their stress-energy is.
- **H-ORBIFOLD:** the bulk is symmetric about each plane.
- **H-TENSOR-4/3:** the massive-graviton factor. It is not derived for a bulk with unwarped time; it scales every
  deviation by 4/3 and changes no verdict.
- **H-NO-BENDING:** brane bending and any radion are left out.
- **H-PERCENT:** the 1 % criterion.
- **Carried from pairing.py:** H-CF-STATIC and H-L-ILLUSTRATIVE.
- **M's:** H-HIGHER-CORRIDOR, H-BULK-PAIRING and H-UNOBSERVED-UNBUILT.

## OPEN

1. A fit of the power-law deviation to Lee et al.'s data (their supplemental material is not READ). That would replace
   H-PERCENT.
2. The brane-bending and radion contributions (H-NO-BENDING).
3. The massive-graviton tensor factor in a bulk where time is not warped (H-TENSOR-4/3).
4. What makes up Chung–Freese's bulk fluid, which violates the null energy condition (`PAIRING.md`, BULK2-O2).
