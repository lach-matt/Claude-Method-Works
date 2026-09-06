# THE SOURCE CODE

### What reading Warp Factory changed, including a factor of two against this series

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Seventh of seven. **Supersedes numeric results in `SHIFT-CEILING.md` §3 and
`SHELL-PROFILE.md` §4**, both preserved unaltered.

> **Superseded in one number, and vindicated in its prediction, 2026-09-06.** `MEASURED.md` runs
> Warp Factory under Octave: the ceiling is **0.0218 c**, so §4's 0.0289 c over-estimates by 1.33x —
> the closest of the three. **§5's prediction held**: at `vWarp = 0.04` the NEC is violated by
> 2.4e39 J/m^3. And §7 lists MATLAB as the blocker; it was not one.

> **Scope.** Writes nothing into `method/` or `drive/`. Warp Factory is MIT-licensed and is **read,
> never copied**: the functions in `warpdrive.py` marked *restated* are Python statements of what the
> MATLAB computes, written for comparison, and the toolkit is cited.

---

## Abstract

Six papers in this series rest on two numbers read off Fuchs *et al.*'s plotted profiles and one
assumption about how their shift parameter relates to velocity. Warp Factory — the toolkit the
solution was built with — is public. Reading three of its files settles all three, and one of them
against this series.

**The pressure is corroborated.** `TOVconstDensity.m` is the interior-Schwarzschild closed form for a
uniform **sphere**, multiplied by the local density so that it vanishes in the cavity without an
explicit cut. Applied to a hollow shell it carries the total mass inward past the empty interior, so
it parts from a true shell integration by 3 % at the outer wall and 29 % at the inner. It gives
**0.0549 ρ** at mid-shell against `SHELL-PROFILE.md`'s **0.0504 ρ**. **Two independent methods, 9 %
apart, and both an order of magnitude below the 0.363 ρ read off fig. 9.** The correction in
`SHELL-PROFILE.md` §3 is confirmed from a second direction.

**The linearity assumption is justified from source.** The warp is applied in a single line —
`g_tx = −S_warp(r)·vWarp` — on a metric that is diagonal in the comoving frame. The perturbation is
*exactly* linear in the shift parameter, so the momentum flux is linear in it to first order. The
extrapolation `SHIFT-CEILING.md` §3 assumed on plausibility is now established.

**And the factor of two was wrong, in this series' favour.** `vWarp` is not half the velocity; it *is*
the velocity. With `γ_xx = 1` in the flat interior, `β^x = g_tx` and `dx/dt = +S·vWarp`, so inside the
shell `dx/dt = vWarp`. `β_warp` and `v_warp` are one parameter. **The velocity ceiling therefore
halves, from 0.058 c to 0.029 c.**

**One prediction follows, and it is cheap to test.** Fuchs *et al.* §4.1 verify physicality at
`β_warp = 0.02`; their Table 1 reports the Warp Shell at `v_warp = 0.04 c`. Same parameter, twice the
value. On the numbers here, 0.04 sits **above** the ceiling. Running Warp Factory on the Warp Shell at
`vWarp = 0.04` should show a null-energy-condition violation. The prediction turns on the one input
still read off a plot: it holds if the peak momentum flux at `β = 0.02` exceeds **0.264 ρ**, and the
eyeballed value is 0.363 ρ.

---

## 1. What was read

| file | bytes | what it settles |
|---|---|---|
| `Metrics/WarpShell/metricGet_WarpShellComoving.m` | 5,019 | how the warp is applied, and what `vWarp` means |
| `Metrics/utils/TOVconstDensity.m` | 189 | the pressure profile, in closed form |
| `Metrics/utils/compactSigmoid.m` | 281 | the shift's radial profile |
| `Metrics/utils/alphaNumericSolver.m` | 1,464 | the lapse, by cumulative trapezoid |

Helmerich & Fuchs, *Analyzing warp drive spacetimes with Warp Factory*, **CQG 41** (2024) 095009;
repository MIT-licensed at `github.com/NerdsWithAttitudes/WarpFactory`.

---

## 2. The pressure, corroborated

### 2.1 What they actually solve

`TOVconstDensity.m` is one line. Restated:

**`P(r) = ρ(r) c² · [ R√(R − r_s) − √(R³ − r_s r²) ] / [ √(R³ − r_s r²) − 3R√(R − r_s) ]`**

with `r_s = 2GM_total/c²` and `R = R₂`. Dividing through by `R^{3/2}` this is the standard interior
Schwarzschild solution for a **uniform sphere**:

`P = ρc² [√(1 − r_s r²/R³) − √(1 − r_s/R)] / [3√(1 − r_s/R) − √(1 − r_s r²/R³)]`

Two things follow that the paper does not spell out:

1. **The vacuum interior is automatic.** `P ∝ ρ(r)`, and `ρ = 0` for `r < R₁`, so the pressure
   vanishes in the cavity with no explicit cut. The paper's *"this pressure is set to zero for
   r < R₁"* describes a consequence of the formula's shape, not a separate step.
2. **It is a uniform-sphere formula applied to a hollow shell.** `M(end)` is the *total* mass at every
   radius, so the enclosed mass is overstated wherever the interior is empty. The correct shell
   integration uses `m(r) = M(r³ − R₁³)/(R₂³ − R₁³)`.

This is not a fault. The paper is explicit that this is the **initial guess** — step (ii) of five —
and that the true stress-energy is read back from the Einstein tensor after the metric is built
(step iv). It is a documented approximation to a starting profile.

### 2.2 The comparison

*(COMPUTED, published parameters.)*

| `r` [m] | Warp Factory closed form | shell TOV (`SHELL-PROFILE.md`) | ratio |
|---|---|---|---|
| 18 | 0.0238 | 0.0231 | 1.030 |
| 16 | 0.0451 | 0.0423 | 1.067 |
| **15** (mid-shell) | **0.0549** | **0.0504** | **1.089** |
| 12 | 0.0805 | 0.0680 | 1.184 |
| 10 (inner wall) | 0.0945 | 0.0732 | 1.290 |

They agree at the outer wall, where the cavity is far away and the enclosed mass is nearly total, and
part inward exactly as the approximation predicts. **The divergence is the signature of the missing
cavity, and its direction and magnitude are both what they should be** — which is the best available
check that the reconstruction in `SHELL-PROFILE.md` was done correctly.

> **The point that matters:** 0.0549 and 0.0504. Two independent methods, 9 % apart at the binding
> radius, and both roughly seven times below the 0.363 ρ that `SHIFT-CEILING.md` read off fig. 9.
> The hoop-spike explanation in `SHELL-PROFILE.md` §3 stands, and the bulk pressure is now known from
> the authors' own code.

---

## 3. The warp is one line

`metricGet_WarpShellComoving.m`, with `doWarp` set:

```
Metric.tensor{1,2} = Metric.tensor{1,2} − Metric.tensor{1,2}.*ShiftMatrix − ShiftMatrix*vWarp
```

The shell metric is diagonal in the comoving frame, so `g_tx = 0` going in, and the whole statement
reduces to

**`g_tx = − S_warp(r) · vWarp`**

with `S_warp` the compact sigmoid: exactly 1 inside `R₁ + R_buff`, exactly 0 outside `R₂ − R_buff`, no
tails. *(Verified in `compact_sigmoid()`.)*

### 3.1 Linearity, established

The metric perturbation is **exactly** linear in `vWarp`. The Einstein tensor is linear in second
derivatives of the metric and quadratic in first derivatives, so the induced momentum flux is linear
in `vWarp` to first order with `O(v²)` corrections. At the operating point `v = 0.02` those
corrections are at the `4 × 10⁻⁴` level.

> `SHIFT-CEILING.md` §5 listed "linearity in the shift is an assumption" among the things that could
> loosen its bound. **It is not an assumption any more**, and the extrapolation from 0.02 to ~0.03
> stays well inside the linear regime.

### 3.2 Compact support, and the Schwarzschild exterior

`S_warp` is identically zero outside `R₂ − R_buff`. The shift therefore contributes **nothing** to the
exterior metric, which stays Schwarzschild exactly. `ROTATING-SHELL.md` §2 argued that counter-rotation
is required to preserve that exterior; the shift, unlike rotation, never threatened it.

---

## 4. The factor of two, against this series

`vWarp` enters as `g_tx = −S·vWarp`. In ADM form `g_tx = γ_xx β^x`, and the interior is flat, so
`γ_xx = 1` and `β^x = −S·vWarp`. A worldline at rest with respect to the shifted frame has

**`dx/dt = −β^x = + S·vWarp`**

which inside the shell (`S = 1`) is `vWarp`. **`vWarp` is the drive's coordinate velocity in units of
`c`, and `β_warp` is the same number.**

`SHIFT-CEILING.md` §3 and `SHELL-PROFILE.md` §4 both took `v/β = 2`, inferred from Fuchs *et al.*'s
Table 1 caption reading `v_warp = 0.04 c` beside a text passage naming `β_warp = 0.02`. **That
inference was wrong.** The two numbers are not a ratio; they are two different runs.

| | ceiling / ρ | `β_max` | `v_max` |
|---|---|---|---|
| `SHIFT-CEILING.md` §3 (eyeballed `p`, `v = 2β`) | 0.6817 | 0.0375 | 0.0750 c |
| `SHELL-PROFILE.md` §4 (computed `p`, `v = 2β`) | 0.5252 | 0.0289 | 0.0579 c |
| **this paper (computed `p`, `v = β` from source)** | **0.5252** | **0.0289** | **0.0289 c** |

*(COMPUTED.)* The velocity ceiling has now moved twice, both times downward, and both times because an
input this series inferred rather than measured turned out to be measurable.

---

## 5. A prediction against the published toolkit

Fuchs *et al.* §4.1: *"Varying the values of β_warp, we find that the addition of shift inside the
shell is possible for β_warp = 0.02 without any energy condition violation."*

Fuchs *et al.* Table 1: *"Comparison of time delay between different warp models and the matter shell
for v_warp = 0.04 c"*, with the Warp Shell row reporting δt = 7.6 ns.

Since `β_warp` and `v_warp` are one parameter (§4), the physicality check was performed at 0.02 and the
time-delay comparison reported at 0.04. The paper does not say the check was repeated at the higher
value.

On the numbers here, **0.04 sits above the ceiling of 0.0289**. So:

> **Prediction.** Run Warp Factory's `metricGet_WarpShellComoving` with the published parameters and
> `vWarp = 0.04`, then `getEnergyConditions`. The null energy condition should be violated somewhere
> in the shell — most likely near mid-shell, where the momentum flux peaks.

**What would falsify it.** The ceiling scales with the peak momentum flux at the reference point, and
that single number is still read off a plot. `β = 0.04` remains safe if the peak flux at `β = 0.02` is
below **0.264 ρ** *(COMPUTED)*. The eyeballed value is 0.363 ρ, which is why the prediction points the
way it does — but a plot axis running to 5 × 10³⁹ does not prove the curve reaches it, and if the true
peak is under three-quarters of the axis the prediction fails.

**This is the cheapest open item in the series.** One run of a published toolkit with a published
metric settles it, and settles the ceiling for every paper here at the same time.

---

## 6. Results

**1.** Warp Factory's pressure is the interior-Schwarzschild **uniform-sphere** closed form scaled by
local density, applied to a hollow shell and documented as an initial guess. *(MEASURED from source.)*

**2.** It gives **0.0549 ρ** at mid-shell against the shell integration's **0.0504 ρ** — 9 % apart, and
parting inward exactly as a missing cavity predicts. **`SHELL-PROFILE.md`'s correction is confirmed
independently**, and the 0.363 ρ eyeball is refuted twice over. *(COMPUTED.)*

**3.** The warp is `g_tx = −S_warp(r)·vWarp`, one line, on a diagonal metric. The perturbation is
exactly linear in the shift, so the linear extrapolation is established rather than assumed.
*(MEASURED + INFERRED.)*

**4.** `S_warp` has compact support, so the shift contributes nothing to the exterior and the
Schwarzschild matching is exact. *(MEASURED.)*

**5.** **`vWarp` is the drive velocity; `v = β`, not `2β`.** This series assumed otherwise in two
papers. **The velocity ceiling halves to 0.029 c.** *(MEASURED from source — a correction to this
series, not to anyone else's.)*

**6.** Physicality was verified at `β = 0.02`; Table 1 reports `v_warp = 0.04`. On these numbers 0.04
exceeds the ceiling, giving a **falsifiable prediction** that one run of the published toolkit
settles. It flips if the peak flux at `β = 0.02` is below 0.264 ρ. *(COMPUTED.)*

**7.** Three of the series' inputs were inferred where they could have been measured, and the source
was public throughout. **Two of the three inferences were wrong, and both in the flattering
direction.** *(Recorded.)*

---

## 7. Open

| item | state |
|---|---|
| the peak momentum flux at `β = 0.02` | the last eyeballed input in the series, and now the hinge of §5 |
| the prediction at `vWarp = 0.04` | needs MATLAB and a Parallel Computing Toolbox licence; not available in this container |
| the true anisotropic profile | still requires their step (iv), reading `T_µν` back from the built metric |
| the smoothing span | now known to be a free parameter — `smooth()` applied four times, span `1.79·smoothFactor` for ρ and `smoothFactor` for `P`. `smoothFactor` itself is set per run and is not published for the figures |
| whether the `O(v²)` terms matter by `v = 0.03` | estimated at `4 × 10⁻⁴` at the operating point; not computed at the ceiling |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 51 fixtures
python3 research/warp-drive/warpdrive.py               # full report
```

The restated functions carry the Warp Factory filename they restate. They are for comparison and are
not a port; the toolkit itself is MATLAB and is cited, not vendored.
