# SPHERICITY

### The cost measured, the test attempted, and the control that invalidated it

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Twelfth of twelve. **Reopens** the class bound of `THE-DESIGN-EQUATION.md` §6, which
`DENSITY-IS-CLOSED.md` had left resting on one untested assumption.

> **Scope.** Writes nothing into `method/` or `drive/`.

---

## Abstract

`DENSITY-IS-CLOSED.md` closed one of the two assumptions defining the shell family and left
sphericity as the last. This paper measures what sphericity costs, attempts to break it, and reports
that **the attempt failed its own control** — so the lever is **untested, not closed**, and the class
bound is not final.

**The cost is real and it is measured.** Mapping the binding ratio by angle from the direction of
motion, on the uniform sphere with the raised-cosine shift at `v = 0.035`:

| `θ` | `\|f\|/ρ` | vs pole | min null |
|---|---|---|---|
| 0° (along motion) | **0.1363** | 1.00 × | +4.04e38 |
| 45° | 0.3236 | 2.37 × | +2.95e38 |
| 75° | **0.4508** | 3.31 × | +1.54e37 |
| 90° (transverse) | 0.4467 | 3.28 × | **−1.01e38** |

> **The load is an equatorial belt.** The polar caps carry a third of it, and only the transverse ray
> actually fails. **The design is limited by a belt while paying for a whole sphere.**

Peak over solid-angle-weighted mean: **1.197×** — what pure redistribution of the load would buy.
Peak over polar: 3.31×, an unreachable ceiling.

**The attempt.** An oblate shell thickening the wall exactly where it binds:
`R₂eff = R₂(1 + e·sin²α)`, with the spherical radial functions evaluated at a rescaled shell
coordinate. At `e = 0` it reproduces the sphere exactly — floor, `ρ_max` and the −1.01e38 at
`v = 0.035` all match.

**The control failed.** At `e = 0.3` and `0.6`, the **`vWarp = 0` floor is already violating** —
−2.39e39 and −4.58e39, 1,200× and 2,400× the spherical floor — and the violation is **identical at
every `vWarp`**. All of it is the deformation and none of it is the warp.

> Evaluating spherical metric functions at a deformed coordinate does not produce a valid matter
> distribution. It is not a solution of anything. **Reporting "oblate shells fail" from this run would
> be reporting an artefact**, and the `vWarp = 0` control is what caught it.

**So the class bound of ≈ 0.047 c is not final.** Density is closed; sphericity is measured to be
worth **at least 1.197×** and is genuinely open. A valid test means solving the Hamiltonian and
momentum constraints for an oblate matter distribution — numerical-relativity initial data, not a
deformed metric.

---

## 1. What sphericity costs

### 1.1 The measurement

`WHAT-BINDS.md` found the NEC failing at `r = 12.5 m` on the transverse axis. That located a point.
This maps the whole angular dependence: rays at `θ = 0…90°` from `+x`, in the `z`-centre plane, taking
the maximum binding ratio and the minimum null value along each. *(MEASURED, uniform sphere,
raised-cosine shift, `v = 0.035`, `dx = 1.0 m`.)*

| `θ` [deg] | max `\|f\|/ρ` | at `r` [m] | min null |
|---|---|---|---|
| 0 | 0.1363 | 14.00 | +4.041e38 |
| 15 | 0.1516 | 11.75 | +3.115e38 |
| 30 | 0.2389 | 10.50 | +3.175e38 |
| 45 | 0.3236 | 10.00 | +2.947e38 |
| 60 | 0.4033 | 10.50 | +2.815e38 |
| 75 | **0.4508** | 10.50 | +1.540e37 |
| 90 | 0.4467 | 10.00 | **−1.011e38** |

Two things worth noting beyond the headline. The ratio rises monotonically and roughly as `sin θ`,
which is what a shift along `x` acting on a radial profile should produce. And **only the `θ = 90°`
ray actually fails** — `θ = 75°` is at +1.54e37, within a factor of ten of zero. The failure is not a
point defect; it is a belt about to fail along its whole width.

### 1.2 What redistribution would be worth

| | value |
|---|---|
| peak ratio | 0.4508 |
| solid-angle-weighted mean | 0.3767 |
| polar ratio | 0.1363 |
| **peak / mean** | **1.197 ×** |
| peak / pole | 3.307 × |

*(COMPUTED.)* **1.197×** is what a reshaping that merely *equalises* the existing load would buy —
the honest lower figure. The 3.31× assumes every angle could be brought to the polar value, which no
redistribution achieves.

> A reshaping could in principle beat 1.197×, because thickening the belt **reduces** flux
> (`|S″| ∝ 1/d²`) rather than moving it around. That is the case for trying, and it is what §2
> attempted.

**Worth recording against the literature:** Bobrick–Martire report ~10× energy reduction from
flattening an *Alcubierre* drive. The positive-energy shell has far less to gain, because its load is
only 1.2× peaky in the solid-angle mean. The two objects are not comparable on this axis, and the
Alcubierre figure should not be carried across.

---

## 2. The attempt, and its control

### 2.1 The construction

Thicken the wall in the belt and leave the poles alone. With motion along `+x`:

`R₂eff(α) = R₂(1 + e·sin²α)`,  `sin²α = (y²+z²)/r²`
`u = R₁ + (r−R₁)(R₂−R₁)/(R₂eff−R₁)`

and evaluate the spherical `A(u)`, `B(u)`, `S(u)`. `e = 0` recovers the sphere identically.

**This is not a solution of the Einstein equations**, and was never claimed to be. It is a metric
handed to the solver so that the energy conditions can be *tested* on it. Reverse-engineering a metric
and reading off `T` is legitimate **provided the conditions are tested rather than asserted** — which
is precisely the failure Santiago–Schuster–Visser identified in Lentz. Hence the control.

### 2.2 The control

**The `vWarp = 0` run must reproduce the spherical floor.** If the deformed shell violates with no
warp at all, the deformation itself is unphysical and nothing downstream means anything.

*(MEASURED.)*

| `e` | `ρ_max` | floor at `v = 0` | vs sphere | at `v = 0.055` |
|---|---|---|---|---|
| **0.0** | 1.3616e40 | −1.926e36 | 1.0 × | *(control passes)* |
| 0.3 | 1.8135e40 | **−2.386e39** | **1,239 ×** | −2.386e39 |
| 0.6 | 2.2000e40 | **−4.577e39** | **2,376 ×** | −4.577e39 |

**The control fails, and fails unambiguously.** Two things make it conclusive:

1. The `v = 0` floor is three orders of magnitude above the spherical one.
2. The violation is **identical at every `vWarp`** — −2.386e39 at 0, 0.035, 0.045 and 0.055 alike. The
   shift contributes *nothing above it*. All of it is geometry.

### 2.3 What the run does *not* show

It is worth being explicit, because the surface numbers look encouraging and are meaningless:
`|f|/ρ` fell to 0.097 at `e = 0.3` and 0.052 at `e = 0.6` — exactly the flux reduction the design
equation predicts from a thicker belt. **None of that can be quoted.** It sits on top of a metric that
already violates every condition before the drive is switched on.

> **The lever is untested, not closed.** By P8 the bound here is on *the construction method*, not on
> oblate shells: *evaluating spherical metric functions at a deformed coordinate does not produce a
> valid matter distribution.*

---

## 3. What a valid test requires

The spherical shell works because Birkhoff hands you the exterior and TOV hands you the interior. An
oblate shell has neither. A valid test must **solve the constraint equations** rather than deform a
solution:

- solve the **Hamiltonian constraint** for the conformal factor on an oblate matter distribution;
- solve the **momentum constraint** for the extrinsic curvature consistent with the shift;
- then evaluate the energy conditions on the result.

That is standard numerical-relativity **initial data** — an elliptic solve on a 3D grid — and it is a
genuinely larger piece of work than anything in this series so far. It is also the only route that
would settle the question, and the measurement in §1 says the question is worth settling.

---

## 4. Results

**1.** The binding load is an **equatorial belt**: 0.1363 at the pole against 0.4508 at 75°, a
**3.31×** span, with only the transverse ray actually failing. *(MEASURED — new.)*

**2.** Peak over solid-angle mean is **1.197×**; peak over pole 3.31×. Redistribution is worth at
least the former. *(COMPUTED.)*

**3.** Bobrick–Martire's ~10× from flattening an Alcubierre drive **does not carry across** — this
object's load is only 1.2× peaky in the mean. *(INFERRED.)*

**4.** An ellipsoidal deformation was built and **failed its `vWarp = 0` control** by 1,239× and
2,376×, with the violation independent of `vWarp`. *(MEASURED.)*

**5. The test is invalid and the lever is untested, not closed.** The bound is on the method:
deforming a spherical solution does not give a valid matter distribution. *(Recorded, per P8.)*

**6. The class bound of ≈ 0.047 c is therefore not final.** Density is closed; sphericity is open and
worth at least 1.197×. *(Recorded.)*

**7.** The `vWarp = 0` control is what made the difference between a result and an artefact, and it
cost one extra row per run. *(Method note.)*

---

## 5. Open

| item | state |
|---|---|
| **oblate initial data** | the real remaining work: solve the Hamiltonian and momentum constraints for an oblate shell, then test. Everything else in this series has been build-and-measure; this is a genuine numerical-relativity problem |
| how much better than 1.197× a thicker belt could do | unknown, and only a valid solve answers it. The flux argument says `\|S″\| ∝ 1/d²`, so more than redistribution — but that is an argument, not a measurement |
| whether an angle-dependent *shift* helps without deforming the shell | `S(r,θ)` keeps the metric spherical and the interior flat; the profile lever is worth at most 1.23× and only in the belt, so probably not, but it is cheap to test |
| the null-vector question | unchanged; scales every absolute number and no ratio |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 90 fixtures
python3 research/warp-drive/warpdrive.py               # full report
```

`octave/run_angular.m` produces §1; `octave/run_oblate.m` with `WF_ECC` produces §2, and
`octave/profile/metricGet_OblateShell.m` is the deformed builder — kept, with its control failure
recorded, because the next attempt should start by not repeating it.
