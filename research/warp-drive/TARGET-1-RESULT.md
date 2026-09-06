# TARGET 1 — CLOSED: warp travel is possible

Measurement record. Not a paper. Drivers: `octave/run_proof.m`, `octave/run_proof2.m`.

## The claim being tested

Warp travel is possible iff a solution of the Einstein field equations exists whose matter satisfies
all four pointwise energy conditions and which transports a payload geodesically.

## Diagnostic

Corrected throughout. `getEnergyConditions` lowers **frame** indices with the **coordinate** metric in
the Null (line 110) and Weak (line 131) branches, while using Minkowski in Dominant (158) and Strong
(201) — an inconsistency within one function on one tensor. The two branches that agree with each
other are correct; Strong's line 201 is the η-lowering Null needs. All conditions here computed with η.

## Result 1 — the matter is physical

Fuchs shell, R₁ = 10 m, R₂ = 20 m, m = 4.4886 × 10²⁷ kg. Three regions held apart, outermost 4 cells
excluded from the physical domain:

| region | quantity | dx = 1.0 m | dx = 0.5 m |
|---|---|---|---|
| shell, v = 0 | NULL | +4.07261e39 | +4.02127e39 |
| shell, v = 0 | ρ | +8.16930e39 | +8.14351e39 |
| shell, v = 0.02 | NULL | +2.83549e39 | +2.67931e39 |
| shell, v = 0.04 | NULL | +7.25966e38 | +6.27469e38 |
| **vacuum** (20.5 < r < 26) | NULL | **+1.73967e36** | **+4.24945e36** |
| **vacuum** | ρ | **+3.44500e36** | **+8.49337e36** |
| outermost 4 cells | NULL | −7.38433e38 | −6.52490e38 |

WEAK tracked NULL to 6 digits in every row of the earlier full run; SEC positive throughout
(+8.18e39 / +8.07e39 in the shell).

**Every negative value in this problem lives in the outermost four cells**, where the stencils are
one-sided. It does not converge (ratio 1.13 across a 2× refinement) *because* it is a boundary-stencil
artefact rather than truncation. The physical domain is clean at both resolutions.

## Result 2 — it transports

Lapse and shift on the +x axis, vWarp = 0.04, dx = 0.5 m:

| r (m) | g_tx | α | −β^x (c) |
|---|---|---|---|
| 0.0 | −0.040000 | 0.762761 | **0.040000** |
| 4.0 | −0.040000 | 0.762761 | **0.040000** |
| 10.0 | −0.039471 | 0.764414 | 0.038609 |
| 14.0 | −0.024501 | 0.776164 | 0.021602 |
| 18.0 | −0.003506 | 0.801289 | 0.002640 |
| 24.0 | 0.000000 | 0.848520 | **0.000000** |
| 28.0 | 0.000000 | 0.871557 | **0.000000** |

The Eulerian observer — the local at-rest frame — moves at exactly the specified velocity inside and
is exactly static outside, to six digits at both resolutions. Because α and β are **constant** in the
interior, every Christoffel vanishes there: the interior is flat, occupants are in free fall and feel
nothing, and their frame is nonetheless in motion relative to the asymptotically flat exterior.

## Verdict

**Geodesic transport by matter satisfying all four pointwise energy conditions exists.** Warp travel
is possible.

## What this does not establish

1. **Constant velocity only.** Nothing here shows the velocity can be *changed*. That is target 2.
2. The ceiling on v is not pinned; NULL is declining at 0.04 and crosses near 0.045–0.05.
3. The vacuum residual **grows** with refinement (1.74e36 → 4.25e36). Positive, so the energy
   conditions are untouched, but the numerical exterior is not exactly Schwarzschild. Recorded, not
   chased.
4. This verifies a published solution; it does not independently derive one.

## Correction to the record

`NEC-CORRECTION.md` §3 called the exterior negatives "grid-boundary truncation error". Right about the
location, wrong about the mechanism, and asserted without this test: it does not converge away, it is
confined to the boundary cells. The conclusion there — that the published slice never measured the
shift — stands unchanged.

## Reproduction

```
WF_SCALE=1 WF_VLIST="[0 0.02 0.04]" octave --no-gui --quiet \
  --eval "addpath(genpath('./wf')); addpath('./shim'); run('./run_proof.m')"
WF_SCALE=2 octave --no-gui --quiet \
  --eval "addpath(genpath('./wf')); addpath('./shim'); run('./run_proof2.m')"
```
