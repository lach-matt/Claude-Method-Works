# M1's open piece: position 2's plane across the whole static bulk, and what (Z) asks of a thin plane (computed, deduced and standard-not-READ; not verified by a separate session; not seated; 2026-10-10)

*First headed* 2026-10-10, worked in the conversation. Instrument: `lemmas/p2_full.py` (selftest 4/4 on four
columns in 63 s; `--full` runs all 32; mutants 2/2). It imports `lemmas/b4_static.py` by path.

## What you said

- **197:** *"A plane on its own can read eq. (17) smoothly only if it carries extra matter. - because it sees its own
  reflection, not the other plane"*.
- **138:** each universe has its own bulk and laws. Position 2's plane has its own universe's bulk beyond it.
- **183 / seated (Z):** "never violated" holds net along each light ray.
- **198** (your guess): the README forms the corridor, with no partner.

## Plain words first

- **ITEM197 met M1 in the throat.** Facing position 2's plane, our plane needs no added matter. M1 needs a *whole*
  position-2 plane across the bulk, so this takes the simplest one: a plane at constant depth below ours, mirrored.
  It runs through the full static bulk at all 32 radii, from 2.005m to 32m.
- **Its energy is positive** at every radius, for depths up to 1.5m. **Its tangential null energy is positive
  everywhere.**
- **Its radial null energy, ρ + p_r, is slightly negative at every radius.** It tends to zero at the throat, where
  ITEM197's symmetry makes it exactly zero, and it tends to zero far out.
- **Your (Z) rules that out for a thin plane** (deduced). A light ray crossing a thin plane at a shallow angle picks
  up the plane's null energy divided by the sine of that angle. As the angle flattens, a negative value becomes
  unboundedly negative, and nothing else along the ray can cancel it. So "net along each light ray" forces the null
  energy to be non-negative at every point and in every direction along a thin plane.
  - This settles what `R1-COVER.md` left open (H-POINTWISE-NEC-ON-P2, "undecided under (Z)"). For a thin plane it
    follows from (Z).
- **So the mirrored constant-depth plane is refuted as M1's position-2 plane** (deduced from the computed values). So
  are R1-COVER's pieces that reach across the whole cover, which break the same condition.
- **What remains for M1** is a position-2 plane with your own bulk beyond it, not a mirror (138, 197's *"the other
  plane"*), or a shaped one. The far side then adds its own share, and the radial deficit is small (at worst about
  0.2 in these units, under 2×10⁻³ at the throat). OPEN.
- **No status moves; nothing is seated.**

## The facts

- **TS** [deduced; thin-shell formalism, standard-not-READ; computed check].
  - Crossing a thin plane with surface stress S, a light ray gains ∫T(k,k)dλ = S(k∥, k∥)/|n·k|.
  - As it grazes, k∥ tends to a null vector k₀ tangent to the plane, and |n·k| → 0. The contribution tends to
    S(k₀,k₀)/0⁺. Elsewhere the bulk is vacuum, and other planes are crossed at finite angles.
  - So (Z) needs S(k₀,k₀) ≥ 0 for every tangent null k₀. The exception is a second singular source on the same rays,
    such as S15's coincident pair, and 198's way in does not supply one.
  - Check: with S(k₀,k₀) = −0.01 the integral runs −0.0115, −0.11, −1.0 and −10 at angles 0.5, 0.1, 0.01 and 0.001.
    The control with S(k₀,k₀) = +0.01 grows positive.
- **S1** [computed]. b4_static's exact series at order 40, with Padé [10/10] checked against [9/10] in y². Every
  reported point agrees to 10⁻⁴.

  | radius | y₂ = 0.5m: ρ, ρ+p_r, ρ+p_θ | y₂ = 1.5m: ρ, ρ+p_r, ρ+p_θ |
  |---|---|---|
  | 2.005m | +0.115, −0.0011, +0.25 | +0.189, −0.0016, +0.84 |
  | 2.1m | +0.075, −0.016, +0.17 | +0.152, −0.053, +0.56 |
  | 3m | +0.0058, −0.013, +0.018 | +0.0086, −0.044, +0.043 |
  | 10m | +1.7e−5, −2.8e−4, +1.7e−4 | +4.7e−5, −8.3e−4, +5.1e−4 |

  Units are 2/κ² with m = 1. At y₂ = 2.0m the energy turns negative for r = 2.22–2.8m.

## What it does not show

- **The flat limit only** (ℓ ≫ r₀, which is where the window lies). At finite ℓ, a mirrored position-2 plane far out
  is the RS1 sheet −σ; with 139 (1)'s quarter tension its remainder there would be −3σ/4, another reason the mirror
  is not your configuration.
- **One shape** (constant depth) and **one junction** (mirror). A shaped plane, and position 2's own bulk beyond it,
  are not computed.
- **A Padé heuristic**, not a bound. Static.

## OPEN

1. M1 with position 2's own bulk beyond its plane (138). Given the plane's intrinsic metric, the far side's
   extrinsic curvature has one free function after its Gauss and Codazzi constraints. Whether it can supply
   (k_t − k_r) ≥ the slab's deficit, keep ρ ≥ 0, and give a regular bulk beyond is the next computation.
2. A shaped position-2 plane, y = Y(r).

## Named hypotheses (the board's)

- **H-THIN-PLANE:** our planes are thin shells, as in RS.
- **TS:** the thin-shell lemma above, a deduction.

## History

- 2026-10-10: first headed on M's "let's continue the work on the chain here". The first scan flipped g_tt's sign in a
  positivity flag (the stresses were unaffected) and failed on near-flat columns (r ≥ 12m, singular Padé). Both were
  fixed before anything was read off. Not seated.
