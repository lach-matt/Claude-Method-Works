# TARGET 1 — CLOSED, frame-independently

Measurement record. Not a paper. Drivers: `octave/run_proof.m`, `octave/run_proof2.m`.

> ## Status
>
> Le (arXiv:2605.25417) raised two challenges: Q1 that a single-frame Eulerian
> contraction is not the test, and Q2 that a metric-first construction may have no
> well-posed matter source. **Q1 is now answered by exact Hawking–Ellis certification
> (§HE): the stress-energy is Type I everywhere with zero Type-IV cells, and all four
> conditions have large positive slack in bulk and transition at two resolutions.**
> Q2 is not answered and cannot be, by this apparatus. See §HE and §Q2.

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

## HE. Frame-independent certification — the actual test

`octave/run_he.m`. No observer sampling. At every grid point: take `T_ab` in the
orthonormal frame, raise one index with η (`T^a_b`, i.e. negate row 0), take the
eigenvalues. A complex pair means **Hawking–Ellis Type IV** — no rest frame exists and
WEC/DEC fail automatically. All real with a timelike eigenvector means **Type I**,
`diag(−ρ, p₁, p₂, p₃)`, and then the conditions are *exact algebra holding for every
observer*:

```
NEC  rho + p_i >= 0        DEC  rho - |p_i| >= 0
WEC  rho >= 0 and NEC      SEC  rho + sum p_i >= 0 and NEC
```

Minimum slack per region, `vWarp = 0.04`:

| region | NEC | WEC | **DEC** | SEC | Type IV |
|---|---|---|---|---|---|
| bulk, dx=1.0 | +5.517e39 | +5.517e39 | **+3.842e39** | +5.517e39 | **0** |
| bulk, dx=0.5 | +5.044e39 | +5.044e39 | **+4.021e39** | +5.044e39 | **0** |
| transition, dx=1.0 | +4.426e39 | +4.404e39 | **+4.284e39** | +4.426e39 | **0** |
| transition, dx=0.5 | +4.491e39 | +4.468e39 | **+4.340e39** | +4.491e39 | **0** |
| vacuum, dx=1.0 | −2.153e36 | −2.153e36 | −3.909e36 | −2.153e36 | 0 |
| vacuum, dx=0.5 | −2.552e35 | −2.578e35 | −4.212e35 | −2.552e35 | 0 |

**Zero Type-IV cells anywhere**, at either resolution, at every shift value. A rest frame
exists throughout, so the algebra above is the complete and exact statement of the
conditions — there is nothing left for an observer scan to find.

**DEC is the tightest condition**, which is exactly where Le reports single-frame analysis
fails (15–28 % of DEC-violating points missed). Here it is positive with slack 4.0e39 in
the bulk and 4.3e39 in the transition.

**The vacuum negatives converge away** at third order:

| | dx=1.0 | dx=0.5 | ratio |
|---|---|---|---|
| NEC | −2.153e36 | −2.552e35 | **8.44** |
| DEC | −3.909e36 | −4.212e35 | **9.28** |

A physical deficit converges to a finite negative; these fall ~8–9× for a 2× refinement.
Numerical, established by convergence.

**Verdict.** The Fuchs warp shell is Hawking–Ellis Type I and satisfies all four pointwise
energy conditions frame-independently, in the matter and across the source–vacuum
transition. Le's Q1 does not apply to this configuration — the Eulerian result was not
misleading, and the exact test agrees with it.

## Q2. What is still not answered

**Metric-first, not source-first.** `metricGet_WarpShellComoving` builds the *metric* and
reads `T` off the Einstein tensor. Le, following Barzegar, Buchert & Vigneron, prescribes
the *matter* and solves the Einstein constraints, grading eight constructions against five
criteria — of which **none passes**.

What §HE establishes is that the resulting `T` is *admissible matter*: Type I, positive
density, DEC-compliant. What it does not establish is that this matter is a **fluid with a
sensible equation of state**. Those are different requirements and only the first is met
here. Le's five criteria include "an explicit matter model", and this project has none.

**On the disagreement with Le's 600-configuration scan.** Le finds no admissible shell;
this finds one. The likeliest reconciliation is testable and is stated as a prediction
rather than a claim: Le attributes the geometric DEC deficit to **source-profile
regularity**, and Warp Factory smooths its profile very heavily (`smoothFactor = 4000`,
applied two to four times). If the deficit scales with profile sharpness, then reducing the
smoothing should make a transition-band DEC deficit appear. **Not yet run.** Note that Le's
deficit is described as independent of bubble velocity — and the negatives measured here
are also velocity-independent, which is either corroboration or coincidence and is not yet
separated.

## Q. Two challenges — superseded by §HE and §Q2

**Q1. Single-frame.** Every number here contracts in the Eulerian frame. Le's companion
work (arXiv:2602.18023) reports that single-frame Eulerian analysis **misses 15–28 % of
DEC-violating grid points**. The relevant test is frame-independent: the Hawking–Ellis
algebraic type of `T^a_b` and its observer-cap-free Type-I eigenvalue slacks. **Not done
here.** So "all four conditions satisfied" means "satisfied for Eulerian observers", which
is weaker than what the claim needs.

**Q2. Metric-first, not source-first.** `metricGet_WarpShellComoving` builds the *metric* and
reads `T` off the Einstein tensor. Le, following Barzegar, Buchert & Vigneron, prescribes the
*matter* and solves the Einstein constraints — and grades eight constructions against a
five-criterion standard, of which **none passes**. A metric-first construction need not
correspond to a well-posed matter model at all. **Le and this project may be measuring
different objects**, which is the most likely reason a 600-configuration frame-independent
scan "finds no admissible shell" while this one configuration reads clean.

**What Le agrees with.** That the bulk is compliant — *"the matter-filled bulk, which is
Hawking–Ellis Type I and compliant"* — and that failures, where they occur, sit at the smooth
source–vacuum transition. This project measured the same geography.

**What survives regardless.** Le finds a geodesic-integrated **ANEC positive for every
source-prescribed shell**, so the pointwise boundary failures do not appear in the average.
That is the condition topological censorship actually uses, so §NO-PORTAL is unaffected.

**Status:** the warp state is measured physical for Eulerian observers, at two resolutions,
including the transition band. It is **not certified frame-independently**, and that
certification is now the open item, ahead of the toroidal question.

## The transition band — the region this test originally masked out

`run_transition.m`, resolving 16–27 m in fine bins. TARGET-1's original masks were
shell 10.5–19.5 and vacuum 20.5–26.0, **excluding 19.5–20.5 — exactly the transition Le
names.** Re-run including it:

| band (m) | NULL, dx=1.0 | NULL, dx=0.5 | reading |
|---|---|---|---|
| 19.0–19.5 | +4.073e39 | +4.021e39 | converged, positive |
| **19.5–20.0** | **+3.467e39** | **+3.479e39** | **converged, positive** |
| **20.0–20.5** | **+2.942e39** | **+2.838e39** | **converged, positive** |
| 20.5–21.0 | +2.243e39 | +2.265e39 | converged, positive |
| 24.0–27.0 | −1.035e36 | −1.276e35 | **8.11× — converges away** |

The masked band was clean. And the outer negative now has the discriminator that was
missing: a physical failure converges to a finite negative value, this one falls 8× for a
2× refinement (~3rd order). In **this** configuration the outer negatives are numerical —
established by convergence, not asserted.

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
