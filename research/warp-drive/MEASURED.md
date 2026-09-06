# MEASURED

### Warp Factory, run — the ceiling is 0.0218 c, and the prediction held

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Eighth of eight. **Supersedes the numeric ceiling of `SHIFT-CEILING.md`, `SHELL-PROFILE.md` and
`SOURCE-CODE.md`**, all three preserved unaltered.

> **Scope.** Writes nothing into `method/` or `drive/`. Warp Factory is cloned at run time, patched
> locally, and **never vendored**; `octave/` holds only shims and a driver written here.

---

## Abstract

`SOURCE-CODE.md` closed with a prediction and the observation that it needed MATLAB, which this
container does not have. It does not need MATLAB. **Warp Factory runs under GNU Octave 8.4** with five
shims and three one-line edits — and one of those three is a real bug, not a compatibility issue.

The published Warp Shell was rebuilt from the parameters in the authors' own example and evaluated on
two grids. Everything the series had inferred is now measured.

**The prediction held.** At `vWarp = 0.04` — the value in Fuchs *et al.*'s Table 1 — the null energy
condition is violated by **2.4 × 10³⁹ J m⁻³**, three orders of magnitude above the numerical floor and
identical on both grids.

**The noise floor is identified exactly.** At `vWarp = 0`, `0.01` and `0.02` the condition minima are
**bit-for-bit identical**: all of it is bare-shell truncation error and none of it comes from the
shift. It falls by 8.3× when the grid is halved. **Fuchs *et al.*'s claim of no violation at
`β = 0.02` is vindicated**, and the ~10³⁶ residual their Appendix A describes is exactly what it says
it is.

**The violations are not numerical.** At `vWarp = 0.030` the minimum is `−1.089 × 10³⁹` on both grids —
identical to four significant figures. Refinement moves the floor and leaves the violation untouched.

**The ceiling, measured: `vWarp = 0.0218`**, from a least-squares zero of the null minimum in its
linear regime, agreeing to **0.1 %** between the two grids.

> Fuchs *et al.* call `β = 0.02` *"very conservative"*. It is not. **It has 8.5 % of headroom.** And
> their Table 1 runs the same solution at 0.04, **84 % above the ceiling.**

**Every closed form in this series overestimated, as an upper bound must** — 3.46×, 2.67×, and finally
1.33×, each correction landing closer as an inferred input was replaced by a measured one. The last
one missed by a third because the binding constraint is not the `(t,x)` block alone.

**The series' answer to "how fast" is therefore 0.0218 c**, measured, not inferred — half the
published design speed of 0.04 c, and about a fifth of the first estimate this series produced.

---

## 1. Getting Warp Factory to run

### 1.1 The environment

`octave` 8.4.0 from the Ubuntu archive; no MATLAB, no Curve Fitting Toolbox, no Parallel Computing
Toolbox. The full recipe is in `octave/README.md`.

**Five shims** stand in for toolbox functions: `smooth` (moving average with symmetrically shrinking
end windows, which is what MATLAB's default does), `pagemtimes` (one call site, `Mᵀ·T·M` over 4×4
pages), and `isgpuarray` / `gpuArray` / `gather` as identities.

**Three edits to the clone.** Two are cosmetic: `string(x)` → `char(x)` in `verifyTensor.m`, and
`sum(X,'all')` → `sum(X(:))` in `getEulerianTransformationMatrix.m`.

### 1.2 The third edit is a bug

`Analyzer/utils/generateUniformField.m` takes a `tryGPU` argument and then **ignores it**, passing a
hard-coded `1` to `getEvenPointsOnSphere` in three places. That function's GPU branch calls
`zeros(...,'gpuArray')`.

> So `evalMetric(metric, 0, 1)` — the documented CPU path, and the default — still reaches a
> Parallel Computing Toolbox call. **On any MATLAB install without that toolbox, Warp Factory's CPU
> path does not run.** It works on the authors' machines because the toolbox is present, and the flag
> never gets exercised. Passing `tryGPU` through is a three-character fix.

Recorded here rather than repaired upstream; it is worth reporting to the authors.

### 1.3 The parameters, from their own example

`Examples/4 Warp Shell/W1_Warp_Shell.mlx` is a Live Script — a zip of XML — and its code extracts
cleanly:

```
R1 = 10;  R2 = 20;  Rbuff = 0;  sigma = 0;
m = R2/(2*G)*c^2*(1/3);        %  = 4.4886e27 kg
vWarp = 0.02;                  %  in betas
smoothFactor = 4000;
```

Two things worth noting. **`smoothFactor = 4000` is published** — `SHELL-PROFILE.md` §7 listed it as
unstated, and it was, in the paper; it is in the example. On the `10⁵`-point radial sample over
`0–50.7 m` that is a span of ~2.0 m for `P` and ~3.6 m for `ρ`, applied four times, on a shell 10 m
thick. **The smoothing is substantial.** And the comment `% in betas` settles `SOURCE-CODE.md` §4 from
the authors' own hand: `vWarp` is `β`.

### 1.4 One exact economy

`metricGet_WarpShellComoving` sets `g_tx = −S_warp(r)·vWarp` on a metric that is otherwise diagonal,
and nothing else in the build depends on `vWarp`. So the metric can be built **once** and `g_tx`
rescaled per shift value — exactly, not approximately. A twelve-value sweep costs one two-minute build
plus twelve six-second evaluations.

---

## 2. The measurements

Grid `2(R₂+10)·s` square by 5 deep, boundary trimmed as the authors' own plots trim it.

**Table 1 — `dx = 1.0 m` (60 × 60 × 5).** *(MEASURED.)*

| `vWarp` | `ρ_max` [J m⁻³] | `\|f\|/ρ` | `\|p\|/ρ` | null | weak | strong | dominant |
|---|---|---|---|---|---|---|---|
| 0.000 | 1.3616e40 | 0.0000 | 0.1935 | −1.926e36 | −3.212e36 | −2.878e36 | −2.554e36 |
| 0.010 | 1.3615e40 | 0.1506 | 0.1933 | −1.926e36 | −3.212e36 | −2.878e36 | −2.554e36 |
| **0.020** | 1.3618e40 | 0.3011 | 0.1927 | **−1.926e36** | −3.212e36 | −2.878e36 | −2.554e36 |
| 0.022 | 1.3619e40 | 0.3312 | 0.1926 | −5.076e37 | −5.076e37 | −2.878e36 | −2.554e36 |
| 0.024 | 1.3620e40 | 0.3613 | 0.1924 | −3.072e38 | −3.072e38 | −2.878e36 | −2.554e36 |
| 0.030 | 1.3623e40 | 0.4514 | 0.1918 | −1.089e39 | −1.089e39 | −2.878e36 | −2.554e36 |
| **0.040** | 1.3629e40 | 0.6014 | 0.1907 | **−2.432e39** | −2.432e39 | −1.979e39 | −4.888e39 |
| 0.045 | 1.3633e40 | 0.6763 | 0.1903 | −3.121e39 | −3.121e39 | −3.101e39 | −6.158e39 |

**Table 2 — `dx = 0.5 m` (120 × 120 × 5).** *(MEASURED.)*

| `vWarp` | `ρ_max` | `\|f\|/ρ` | null | strong |
|---|---|---|---|---|
| 0.000 | 1.3593e40 | 0.0000 | **−2.317e35** | −1.273e35 |
| 0.020 | 1.3597e40 | 0.3013 | **−2.317e35** | −1.273e35 |
| 0.025 | 1.3600e40 | 0.3765 | −4.347e38 | −1.273e35 |
| 0.030 | 1.3603e40 | 0.4516 | −1.089e39 | −1.273e35 |
| 0.040 | 1.3611e40 | 0.6015 | −2.435e39 | −2.085e39 |

**`ρ_max = 1.36 × 10⁴⁰ J m⁻³`** against the paper's plotted ~1.4 × 10⁴⁰ and `SHELL-PROFILE.md`'s
computed 1.376 × 10⁴⁰. Three routes, same number.

---

## 3. Numerical or physical: the question settles itself

### 3.1 The floor

At `vWarp = 0`, `0.01` and `0.02` the minima are **identical to every digit printed**. A bare shell
carries no shift, so whatever it shows is truncation error — and the shift contributes *nothing above
it* until 0.022. Halving the grid takes the floor from `−1.926e36` to `−2.317e35`, a factor of **8.3**,
consistent with the solver's mixed-order finite differences. **Falls under refinement: numerical.**

### 3.2 The violations

| `vWarp` | `dx = 1.0 m` | `dx = 0.5 m` | ratio |
|---|---|---|---|
| 0.030 | −1.0890e39 | −1.0890e39 | **1.0000** |
| 0.040 | −2.4320e39 | −2.4350e39 | 0.9988 |

**Unchanged under refinement: physical.** The two behaviours are cleanly separated, and no
interpretation is needed to tell them apart.

### 3.3 Linearity, confirmed a third time

`(|f|/ρ)/vWarp` = 15.06, 15.06, 15.05, 15.05 across the sweep. The source said the shift enters
linearly; the measurement agrees to four figures.

---

## 4. The ceiling

Least-squares zero of the null minimum over its linear regime above the floor:

| grid | threshold |
|---|---|
| `dx = 1.0 m` | 0.02180 |
| `dx = 0.5 m` | 0.02178 |
| agreement | **0.1 %** |

**`vWarp_max = 0.0218`** — and since `vWarp` is the drive's coordinate velocity in units of `c`
(`SOURCE-CODE.md` §4, confirmed by the example's own comment), **the velocity ceiling of the published
Warp Shell is 0.0218 c.** *(MEASURED.)*

| | value | |
|---|---|---|
| published operating point | 0.0200 | headroom **1.085 ×** |
| measured ceiling | **0.0218** | |
| Table 1 operating point | 0.0400 | **84 % over** |

> Fuchs *et al.* describe `β_warp = 0.02` as *"very conservative"* and *"likely not an upper limit as
> optimizations could be considered."* The first is wrong — there is 8.5 % of margin — and the second
> is right only in the sense that a different shell might do better. **This one cannot.**

And the flux ratio at the ceiling is **0.327 ρ**, against the closed form's 0.525. **The `(t,x)` block
is not what binds**; something in the transverse structure fails first, which is why every closed form
here overestimated.

---

## 5. The series, scored against measurement

| paper | input quality | predicted `v_max` | over by |
|---|---|---|---|
| `SHIFT-CEILING.md` | pressure eyeballed, `v = 2β` inferred | 0.0750 | 3.46 × |
| `SHELL-PROFILE.md` | pressure computed, `v = 2β` inferred | 0.0579 | 2.67 × |
| `SOURCE-CODE.md` | pressure computed, `v = β` from source | 0.0289 | 1.33 × |
| **`MEASURED.md`** | **measured** | **0.0218** | — |

Each correction landed closer, and each closed the gap by replacing an inference with a measurement.
**Every one was an over-estimate**, which is what `SHIFT-CEILING.md` §5 promised a
necessary-but-not-sufficient bound would be. The bound was honest about its direction throughout; it
was simply loose, and only measurement could say by how much.

> The general lesson is unglamorous and worth stating: **three of this series' inputs were inferred
> where they were available to be measured**, and the source was public the whole time. The cost was
> a factor of 3.4 in the headline number.

---

## 6. Results

**1.** Warp Factory runs under GNU Octave 8.4 with five shims and three one-line edits; MATLAB is not
required. *(MEASURED.)*

**2.** One of those edits is a genuine bug: `generateUniformField` ignores its `tryGPU` argument and
hard-codes GPU allocation, so **the documented CPU path cannot run without the Parallel Computing
Toolbox.** *(MEASURED from source — worth reporting upstream.)*

**3.** `smoothFactor = 4000` is published in the authors' example, and `vWarp` is commented
*"in betas"* — confirming `SOURCE-CODE.md` §4 from their own hand and closing an open item.
*(MEASURED.)*

**4.** The noise floor is exactly identified: minima at `vWarp = 0, 0.01, 0.02` are bit-identical and
fall 8.3× under refinement. **Fuchs *et al.*'s no-violation claim at `β = 0.02` is vindicated.**
*(MEASURED.)*

**5.** The violations above 0.022 are grid-independent to four figures. **Physical, not numerical.**
*(MEASURED.)*

**6. The prediction of `SOURCE-CODE.md` §5 held.** At `vWarp = 0.04` the NEC is violated by
2.4 × 10³⁹ J m⁻³. *(MEASURED.)*

**7. The measured ceiling is `vWarp = 0.0218`, i.e. 0.0218 c**, agreeing to 0.1 % across two grids.
The published operating point has **8.5 % headroom**, not the "very conservative" margin claimed, and
Table 1 runs 84 % over it. *(MEASURED — the series' final number.)*

**8.** The binding constraint is **not** the `(t,x)` block: the flux at the ceiling is 0.327 ρ against
a closed-form 0.525 ρ. Every closed form here overestimated, by 3.46×, 2.67× and 1.33× as inferred
inputs were replaced. *(MEASURED.)*

---

## 7. Open

| item | state |
|---|---|
| what actually binds at 0.327 ρ | the transverse structure, presumably; identifying the failing component needs a pointwise map, not a minimum |
| a third grid | two agree to 0.1 %; a `dx = 0.25 m` run would cost ~20 min and is unlikely to move it |
| whether a different shell profile raises the ceiling | the fill-fraction sweep of `SHELL-PROFILE.md` §5 was never run through Warp Factory; it could be, now |
| reporting the `generateUniformField` bug upstream | not done here |
| acceleration | untouched, and still the field's foremost open problem (`ACCELERATION.md`) |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 59 fixtures
python3 research/warp-drive/warpdrive.py               # full report
cat research/warp-drive/octave/README.md               # the Octave recipe
```

The measured tables are banked in `warpdrive.py` as `MEASURED`, with the threshold fit, the
grid-independence checks and the linearity check as fixtures. Re-running the Octave sweep reproduces
them; the fixtures assert them without needing Octave present.
