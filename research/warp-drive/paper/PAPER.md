> ## ⚠ WITHDRAWN — do not cite
>
> Every absolute figure in this paper descends from a measurement that is now known to be an
> artefact. The 0.0218 c ceiling was the **grid-boundary truncation error at r = 27.23 m, outside
> the shell**, constant at every shift value including zero; and Warp Factory's null path lowers
> orthonormal-frame indices with the coordinate metric. Corrected, the threshold is ≈ 0.045 c —
> about **twice** what this paper reports. The criticism of Fuchs *et al.* Table 1 is withdrawn
> with it. §6's "most significant open item" (the null-vector objection) was **itself wrong** and is
> withdrawn. The ratios are unvalidated pending a re-measure that is not being spent.
>
> See **`../NEC-CORRECTION.md`**. This draft is kept as the record of what was claimed and why it
> did not stand; the project's live result is **`../THE-ENGINE.md`**.

# A design equation for constant-velocity warp shells

### Profile optimisation, a measured 1.7× improvement, and a bound on the class

**M. Lach** · with a computing collaborator, under the protocols of The Method v1.6
Draft v1.0, 6 September 2026

---

## Abstract

Fuchs *et al.* (2024) exhibited the first constant-velocity warp drive satisfying the null, weak,
dominant and strong energy conditions: a stable matter shell with positive ADM mass carrying a shift
vector on its interior. They left the shift's upper limit explicitly open. We derive a design
equation for that family from the ADM momentum constraint,

  **v_max = Φ(f) · f / k̂**,  **k̂ = κ · C · G(γ)**,

where **Φ** is the flux ratio at which the null energy condition fails (a property of the shell),
**C = max|S″|d²** characterises the shift profile, and **G(γ) = (γ²+γ+1)/(γ−1)** the shell geometry
`γ = R₂/R₁`. The derivation reproduces a measured `1/f` scaling and predicts the radius at which the
condition fails to 3 %.

Two closed-form optima follow. `G` is minimised at **γ = 1+√3**, where volume dilution `(γ³−1)`
balances gradient smoothing `(γ−1)²`. And for any monotone shift with vanishing endpoint derivatives,
**max|S″| ≥ 4/d²** — a bang-bang bound. The published profile sits at 9.841/d²; a raised cosine sits
at exactly **π²/2** and is one line of code.

Reproducing the published solution under free software and replacing only the shift profile, the
threshold rises from **0.0218 c to 0.0349 c (1.599×)**, against 1.578× predicted from the flux
reduction alone — agreement to 1.3 %. `Φ` moves 1.3 % across the swap, confirming that shell and
profile factorise. With the geometry optimum the total is **1.73×**.

We bound the class. Sweeping compactness measures `Φ(f)` falling from 0.522 to 0.333 and gives
**v_max ≲ 0.047 c** for uniform-density spherical shells with a single monotone shift. Density shaping
is measured and closed: concentrating mass cuts `k` by 1.76× and cuts `Φ` by 2.68×, because local
compactness and `Φ` are not independent — so the factorisation holds over the shift profile and not
over the density. Sphericity remains untested; the load is measured to be an equatorial belt carrying
3.3× the polar value.

Finally we note that the family's ceiling is not its binding constraint. ADM 4-momentum conservation
forbids self-acceleration at positive ADM mass, the propellant floor is `ΔP·c` for massless exhaust —
29 Earth masses at 100 % conversion — and the required shell mass grows as `v^1.4`, so cost scales as
**v^2.4**: every speed improvement worsens the barrier. A flyby past an existing compact object
delivers the same geodesic transport for nothing, at **Δv = c√(r_s/b)** in weak field and
**Δv = 2U/(1+U²)** in strong field.

---

## 1. Introduction

Warp drives are exotic solutions of general relativity providing geodesic transport: a passenger is
carried between two points along a geodesic, feeling no acceleration, while the surrounding metric is
modified. Alcubierre's original construction requires macroscopic negative energy density, and
Santiago, Schuster & Visser [4] proved that every generic Natário warp drive violates the null energy
condition — hence also the weak, strong and dominant conditions.

Fuchs *et al.* [3] escaped this by leaving the Natário class. Their construction is a stable matter
shell with a Schwarzschild exterior and positive ADM mass, with a shift vector added on the interior;
it satisfies all four pointwise energy conditions and provides the geodesic transport of the
Alcubierre metric at constant subluminal velocity. Their published operating point is `β = 0.02` in
units of `c`, which they describe as "very conservative", and they state:

> *"there is an upper limit to the magnitude of the shift vector that keeps the warp drive physical.
> This upper limit is a future direction of work."*

This paper supplies that limit, the design equation behind it, and a bound on the family.

---

## 2. The design equation

### 2.1 Derivation

For a shift `β^x = −S(r)·v` on a nearly flat spatial metric, the extrinsic curvature is
`K_ij ∼ ∂₍ᵢβⱼ₎ ∼ vS′`, and the ADM momentum constraint gives an Eulerian momentum flux

  `f = T^{0x} ∼ (c²v/8πG)·|S″|`.

Against a shell of uniform density `ρ = 3Mc²/4π(R₂³−R₁³)`, with `r_s = 2GM/c² = f·R₁` for horizon
fill fraction `f`, `|S″| ∼ C/d²` and `d = (γ−1)R₁`:

  **`k̂ ≡ (|f|/ρ)/v · f = κ · C · G(γ)`**,  **`G(γ) = (γ³−1)/(γ−1)² = (γ²+γ+1)/(γ−1)`**.

Since `k̂` is independent of fill, `(|f|/ρ)/v ∝ 1/f`. Two independent checks:

1. **Measured:** `k·f` = 8.96 → 10.81 across a ninefold mass range — constant to 21 %.
2. **The failure locus.** Because `f ∝ S″`, the condition must fail where `|S″|` peaks, *not* at
   mid-shell where `S″` crosses zero. For the published profile that peak is at **12.18 m**; the
   measured failure is at **12.51 m**. This also explains the sign reversal in momentum density that
   [3] reports near mid-shell: it is `S″` changing sign at the inflection.

Calibration gives `κ = 0.145` against the sketch's `1/3`; the derivation fixes the scaling, not the
O(1) constant.

### 2.2 The geometry optimum

`G(γ)` has an interior minimum because growing `γ` dilutes density as `(γ³−1)` and smooths the shift
gradient as `(γ−1)²`. Setting `dG/dγ = 0` gives `γ² − 2γ − 2 = 0`:

  **`γ_opt = 1 + √3 ≈ 2.7321`, `G_min = 3 + 2√3 ≈ 6.4641`**

against `G(2) = 7` as published — a gain of **1.083×**. The published ratio is nearly optimal, and
this lever is essentially exhausted.

### 2.3 A bound on the shift profile

For `S(0)=1`, `S(1)=0`, `S′(0)=S′(1)=0` on `t ∈ [0,1]`, minimise `max|S″|`. The bang-bang solution
takes `S″ = −a` then `+a`, switching at `t = ½`; integrating, `S(1) = 1 − a/4 = 0`, so `a = 4`:

  **No shift profile has `max|S″| < 4/d²`.**

| profile | `max\|S″\|d²` | continuity |
|---|---|---|
| bang-bang (the bound) | 4.000 | `S″` discontinuous |
| **raised cosine `(1+cos πt)/2`** | **π²/2 = 4.935** | `C¹` |
| quintic smootherstep | 5.774 | `C²` |
| cubic smoothstep | 5.999 | `C¹` |
| **published `compactSigmoid`, σ=0** | **9.841** | `C^∞` |

The raised cosine's value is exactly `π²/2`, since `S″ = −(π²/2)cos(πt)/d²`. Raising the published
profile's sharpness parameter is strongly counterproductive: `σ = 2, 6, 20` give 23.9, 97.4, 743.9.

---

## 3. Method

The published solution was rebuilt with Warp Factory [5] under **GNU Octave 8.4** — no MATLAB, no
Curve Fitting or Parallel Computing Toolbox — using five shims and three one-line edits. Parameters
are those of the authors' own example: `R₁ = 10 m`, `R₂ = 20 m`, `R_buff = 0`, `σ = 0`,
`smoothFactor = 4000`, `m = R₂c²/2G × ⅓ = 4.4886 × 10²⁷ kg`.

Since the shift enters the build only as `g_tx = −S(r)·vWarp` on an otherwise diagonal metric, the
metric is built **once** and `g_tx` rescaled per shift value — exact, not approximate.

**Numerical and physical effects separate cleanly.** At `vWarp = 0, 0.01, 0.02` the condition minima
are **bit-for-bit identical**: all of it is bare-shell truncation error and none comes from the shift.
Halving the grid takes the floor from −1.926e36 to −2.317e35 (8.3×). The violations above threshold do
**not** move: at `vWarp = 0.030` both grids give −1.0890e39, identical to four figures.

**Two observations about the published work.** (i) `generateUniformField` ignores its `tryGPU`
argument and hard-codes GPU allocation, so the documented CPU path cannot run without the Parallel
Computing Toolbox. (ii) Their §4.1 verifies physicality at `β = 0.02`; their Table 1 reports the same
solution at `v_warp = 0.04`. These are one parameter — the example comments `vWarp` as *"in betas"* —
and §5 shows 0.04 exceeds the threshold.

---

## 4. Results

### 4.1 The ceiling, measured

Least-squares zero of the null-condition minimum in its linear regime:

| grid | threshold |
|---|---|
| `dx = 1.0 m` | 0.02180 |
| `dx = 0.5 m` | 0.02178 |

**`v_max = 0.0218 c`**, agreeing to 0.1 % across a factor of two in resolution. The published
operating point has **8.5 % headroom**, not a conservative margin; Table 1's 0.04 runs **84 % over**.

### 4.2 The profile improvement

Same shell, same mass, same grid; only the shift profile replaced:

| | `C` | `k` | `v_crit` |
|---|---|---|---|
| published `compactSigmoid` | 9.841 | 15.060 | 0.02180 c |
| **raised cosine** | π²/2 | 9.542 | **0.03487 c** |

**Gain 1.599×**, against **1.578×** predicted from the flux reduction alone — **1.3 %**. And the
factorisation test: `Φ = k·v_crit` is 0.3283 and 0.3327, moving **1.3 %**. Shell and profile separate.

With `γ = 1+√3` the compounded improvement is **1.73×**, taking 0.0218 c → **0.0378 c**.

The analytic ratio 9.841/4.935 = 1.994 exceeds the measured 1.578 because the code's own smoothing
erodes profile differences by 1.264×; the raised cosine is at or near the practical optimum.

### 4.3 A bound on the class

Sweeping fill fraction, `Φ` falls from 0.522 to 0.333 while `k·f` stays near-constant, so the ceiling
rises **4.7×** across fill 0.1 → 0.9 (0.0058 → 0.0277 c). With the cosine profile and the geometry
optimum:

  **`v_max ≲ 0.047 c`** for a uniform-density spherical shell with a single monotone shift.

### 4.4 Density shaping is closed

A TOV integrator for arbitrary `ρ(r)` and a shaped-shell builder (validated against the published
shell to 0.05 %) give:

| shape | `k` | `Φ` | `v_crit` | vs uniform |
|---|---|---|---|---|
| uniform | 9.542 | 0.3327 | 0.03487 | 1.000 |
| `\|cos πt\|` | 11.169 | 0.3967 | 0.03552 | 1.019 |
| `(1−t)¹` | 5.409 | 0.1250 | 0.02311 | **0.663** |
| `(1−t)²` | 3.771 | 0.0524 | 0.01389 | **0.398** |

Inner-weighting cuts `k` by 1.76× **and cuts `Φ` by 2.68×**: concentrating mass raises the local
compactness, and `Φ` falls with compactness. **The factorisation holds over the shift profile
(spread 1.3 %) and not over the density (spread 657 %).**

### 4.5 Sphericity: measured, untested

The load is an equatorial belt. Binding ratio by angle from the direction of motion: 0.1363 at the
pole, **0.4508 at 75°**, with only the transverse ray failing. Peak/mean = **1.197×**; peak/pole 3.31.

An ellipsoidal deformation was attempted and **failed its `vWarp = 0` control** — the deformed metric
violates before the drive is switched on, by 1,239× and 2,376×, identically at every `vWarp`.
Evaluating spherical metric functions at a deformed coordinate does not give a valid matter
distribution. **The lever is untested, not closed**, and a valid test requires constraint-solved
initial data.

---

## 5. The barrier the ceiling is not

**ADM 4-momentum is conserved** for an isolated asymptotically flat system up to radiated flux. A
shell with positive ADM mass therefore **cannot self-accelerate** — and positive ADM mass is precisely
what lets it satisfy the energy conditions. The Alcubierre drive appears to self-accelerate only
because `M_ADM = 0`, the same truncation that forces its negative energy. **The two properties are one
quantity read twice.**

The floor for supplying `ΔP = γMv` is `E ≥ ΔP·c` for massless exhaust — the same for gravitational
waves as for photons. For the published shell at 0.0378 c that is **29 Earth masses annihilated at
100 % efficiency**, 1.55 × 10⁴³ J. Since `M ∝ v^{1.42}` from the measured curve, **propulsion cost
scales as `v^{2.4}`**: unlike a rocket, whose dry mass is fixed, here the ship grows with the target
speed. **Every improvement in §4 worsens the barrier in §5.**

### 5.1 The transport can be borrowed

The requirement is a potential gradient plus geodesic motion in it, and it need not be manufactured.
For a flyby past a deflector moving at `U`, maximising `Δv = 2U sin(θ/2)` against
`tan(θ/2) = GM/bc²U²` gives `sin 2t = 1` — the optimal turn is exactly 90° — and

  **`Δv_max/c = √(r_s/b)`**   (weak field).

In Schwarzschild geometry the deflection **diverges at the capture boundary** (661° at 1.0001 `b_crit`
for `v = 0.35 c`), so a full reversal is reachable at every approach speed and the geometric bound
dissolves:

  **`Δv = 2U/(1+U²)`**   (strong field), limited by the deflector's speed.

The treatments agree in weak field (GR/Newtonian = 1.002 at `b = 2205 r_s`) and differ by up to 2.04×
in strong field. A full-reversal pass sits at a few `r_s`, and tides at fixed `b/r_s` scale as `1/M²`,
so the deflector is bounded **below**: at `U = 0.35 c` and 1 g across a 20 m payload, **M ≥ 8,570 M☉**.

**A ten-solar-mass black hole at 1 g already gives 0.0410 c** — exceeding the best shell in §4 — at
zero construction cost and zero propellant, geodesically. The §4 target needs only a **700 r_s** pass.

---

## 6. Discussion and limitations

**The energy-condition diagnostic.** Warp Factory contracts the covariant stress-energy with
`k = (1, n̂)` built in the coordinate basis — null in Minkowski. At the failure locus the lapse is
`α = 0.769` and those vectors have `|g_µν k^µ k^ν|` up to 0.494: they are **spacelike**, not null. We
do not claim an error; we report a measurement and pose the question. **Consequence:** every *ratio*
in §4 uses one instrument throughout and is robust — the 1.599 ×, the factorisation, the fill curve,
and the finding that Table 1 exceeds its own threshold. Every *absolute* identification with the null
energy condition inherits the question. **This is the paper's most significant open item.**

**Other limitations.** The class bound assumes uniform density and sphericity; the first is measured
and closed, the second untested. `Φ(f)` is measured on one shell family. Strong-field flyby results
use Schwarzschild, not Kerr, and patched conics rather than a three-body integration. A slingshot
amplifies rather than starts: arrival is a separate, cheaper problem, uncosted here.

**Interpretation.** The shell's mass is the price of not having a potential well. Where a well exists,
geodesic transport is free and the shell is redundant; where none exists, one must *be* the well, at
`c²/2G = 6.7 × 10²⁶ kg` per metre of ship — and then nothing can move what has been built.

---

## 7. Conclusions

1. A design equation for constant-velocity warp shells, derived from the ADM momentum constraint,
   reproducing a measured `1/f` scaling and predicting the failure locus to 3 %.
2. `γ_opt = 1+√3` and `max|S″| ≥ 4/d²`, both closed form.
3. A **1.599×** measured improvement from the shift profile alone, predicted to 1.3 %; **1.73×** with
   the geometry optimum. The published ceiling of **0.0218 c** rises to **0.0378 c**.
4. A class bound of **≈ 0.047 c**; density shaping closed with its mechanism; sphericity untested and
   worth ≥ 1.197×.
5. The published operating point has 8.5 % headroom, and Table 1 of [3] runs 84 % over its own
   threshold.
6. The ceiling is not the binding constraint: ADM conservation forbids self-acceleration, and cost
   scales as `v^{2.4}`.
7. The same transport is available by flyby at `Δv = c√(r_s/b)` (weak field) or `2U/(1+U²)` (strong
   field), for nothing.

---

## References

[1] M. Alcubierre, *The warp drive: hyper-fast travel within general relativity*, CQG **11** (1994) L73.
[2] A. Bobrick & G. Martire, *Introducing physical warp drives*, CQG **38** (2021) 105009.
[3] J. Fuchs, C. Helmerich, A. Bobrick, L. Sellers, B. Melcher & G. Martire, *Constant velocity physical warp drive solution*, CQG **41** (2024) 095009.
[4] J. Santiago, S. Schuster & M. Visser, *Generic warp drives violate the null energy condition*, PRD **105** (2022) 064038.
[5] C. Helmerich, J. Fuchs *et al.*, *Analyzing warp drive spacetimes with Warp Factory*, Classical and Quantum Gravity (2024). Code: github.com/NerdsWithAttitudes/WarpFactory (MIT). *Volume and page not verified from the published article — this container has no journal access, and the volume/page printed for [3] is not this paper's. Every claim made here about Warp Factory is measured from the source at that URL, never quoted from the article.*
[6] M. J. Pfenning & L. H. Ford, *The unphysical nature of "warp drive"*, CQG **14** (1997) 1743.
[7] K. D. Olum, *Superluminal travel requires negative energies*, PRL **81** (1998) 3567.

## Code and reproduction

```
python3 research/warp-drive/warpdrive.py --selftest   # 104 fixtures
python3 research/warp-drive/grflyby.py  --selftest    #  10 fixtures
cat research/warp-drive/octave/README.md              # the Octave recipe
```

All instruments are stdlib-only Python. Warp Factory is cloned at run time and never vendored; the
shims, drivers and profile overrides are in `research/warp-drive/octave/`. Every number in §2–§5 is a
fixture. The fourteen working papers behind this one, including three self-corrections and two
withdrawn estimates, are in `research/warp-drive/`.
