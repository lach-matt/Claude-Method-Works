# DENSITY IS CLOSED

### The shaped-density lever, built and measured — and the domain of the design equation

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Eleventh of eleven. **Refutes the estimate of `THE-DESIGN-EQUATION.md` §6(a)** and **narrows its
factorisation**; that paper is preserved unaltered.

> **Scope.** Writes nothing into `method/` or `drive/`.

---

## Abstract

`THE-DESIGN-EQUATION.md` closed by naming two assumptions left to break, and priced the first —
shaped density — at **up to 1.57×**, on the argument that the pointwise constraint `|f|/ρ` is
equalised by putting mass where the flux is. Warp Factory has only the uniform-sphere closed form, so
this required a new metric builder with a TOV integrator for arbitrary `ρ(r)`. Built, validated
against the published shell to **0.05 %**, and measured:

| shape | `k` | `Φ` | `v_crit` | vs uniform |
|---|---|---|---|---|
| **uniform** | 9.542 | 0.3327 | **0.03487 c** | 1.000 × |
| `\|cos πt\|` (mass at both edges) | 11.169 | 0.3967 | 0.03552 c | 1.019 × |
| `(1−t)¹` (inner-weighted) | 5.409 | 0.1250 | 0.02311 c | **0.663 ×** |
| `(1−t)²` | 3.771 | 0.0524 | 0.01389 c | **0.398 ×** |

**The estimate was wrong and the lever is closed.** Symmetric shaping gains 1.9 %, inside noise.
Inner-weighting — which the measured flux profile appears to ask for — makes things **substantially
worse**.

**The mechanism is the finding.** Inner-weighting cuts `k` by 1.76×, exactly as intended. It also cuts
`Φ` by **2.68×**. Concentrating mass raises the *local* compactness, and `Φ` falls with compactness —
the same `Φ(fill)` curve `WHAT-BINDS.md` measured across whole shells, now acting locally. The two
effects move **together**, and the density one loses.

> **So the design equation has a domain.** `Φ` is independent of the **shift profile** — measured
> spread **1.3 %** — and is *not* independent of the **density profile**, where it spans **657 %**.
> `v_max = Φ/k` factorises over the shift and not over the density. **Uniform density is at or near
> its own optimum**, which is presumably why the published solution uses it.

A second, smaller finding falls out of the radial diagnostic: **the "uniform" shell is not uniform.**
Four passes of a 3.6 m moving average on a 10 m wall turn the box into a bump peaking at `r = 15.5 m`,
while the flux peaks at `r = 11.5 m`. The mismatch is real and it is *not* fixable by adding mass at
`r = 11.5`, for the reason above.

**One of the two escape routes is closed.** The class bound of ≈ 0.047 c stands, and only
**sphericity** remains.

---

## 1. What had to be built

Warp Factory's `TOVconstDensity.m` is the interior-Schwarzschild closed form for a uniform **sphere**
(`SOURCE-CODE.md` §2). It cannot represent a shaped shell at all. Two new files:

- **`octave/profile/tovShaped.m`** — the TOV equation integrated inward from `P(R₂) = 0` by Heun
  stepping, for arbitrary `ρ(r)`.
- **`octave/profile/metricGet_ShapedShell.m`** — the same construction as
  `metricGet_WarpShellComoving`, calling Warp Factory's `sph2cartDiag`, `legendreRadialInterp`,
  `alphaNumericSolver` and `compactSigmoid`, with exactly one physical change: the density shape.

**Validation.** At `δ = 1` the shape reduces to uniform and the builder must reproduce the published
shell. *(MEASURED.)*

| | Warp Factory builder | this builder, `δ = 1` |
|---|---|---|
| `ρ_max` | 1.3616e40 | 1.3616e40 |
| `\|f\|/ρ` at `v = 0.030` | 0.2868 | **0.2866** |
| `\|f\|/ρ` at `v = 0.040` | 0.3821 | **0.3819** |
| numerical floor | −1.926e36 | −1.926e36 |

Agreement to **0.05 %**. The one systematic difference is `|p|/ρ` — 0.162 here against 0.189 theirs —
because this builder integrates the true shell TOV where theirs uses the uniform-sphere
approximation. That difference was already quantified in `SOURCE-CODE.md` §2.

---

## 2. The prediction, and why it failed

### 2.1 The argument that motivated it

The constraint is pointwise: `|f(r)| ≤ (ρ(r) + p_x(r))/2`. With `f ∝ |S″|` and a uniform `ρ`, margin
is wasted everywhere `|S″|` is below its peak. Setting `ρ ∝ |S″|` equalises the ratio; for a raised
cosine `|S″| ∝ |cos πt|`, whose mean is `2/π` of its peak, giving **1.57×**.

### 2.2 Where it broke

`|cos πt|` peaks at `t = 0` **and** `t = 1` — both shell edges, symmetrically. The flux does not. The
radial diagnostic, along the transverse axis at `v = 0.035` *(MEASURED)*:

| `r` [m] | `ρ` | `\|f\|` | `\|f\|/ρ` | |
|---|---|---|---|---|
| 9.50 | 5.655e39 | 1.478e39 | 0.2614 | |
| 10.50 | 8.167e39 | 3.648e39 | 0.4467 | |
| **11.50** | 1.043e40 | **4.557e39** | **0.4367** | **← binds** |
| 12.50 | 1.210e40 | 3.860e39 | 0.3190 | |
| 14.50 | 1.352e40 | 1.115e39 | 0.0825 | |
| **15.50** | **1.352e40** | 3.412e38 | 0.0252 | **← ρ peaks** |
| 17.50 | 1.208e40 | 2.597e39 | 0.2150 | |
| 19.50 | 8.104e39 | 2.422e39 | 0.2989 | |

Two things are visible and neither was anticipated:

1. **The shell is not uniform.** `ρ` runs 5.7e39 → 1.35e40 → 8.1e39 across the wall. Four passes of
   `smooth()` at span ≈ 3.6 m on a 10 m wall make the box a bump. The published density profile is a
   *smoothing artefact* as much as a design choice.
2. **The flux binds at `r = 11.5` and the density peaks at `r = 15.5`.** The mismatch is asymmetric —
   inner — so a symmetric shape cannot address it. Hence the 1.9 %.

---

## 3. The mechanism: `Φ` and `ρ` are coupled

Inner-weighting `(1−t)^p` addresses the mismatch directly, and makes things worse. *(MEASURED.)*

| | `k` cut | `Φ` cut | net |
|---|---|---|---|
| `(1−t)¹` | 1.76 × *(good)* | **2.68 ×** *(bad)* | **1.52 × worse** |
| `(1−t)²` | 2.53 × *(good)* | **6.39 ×** *(bad)* | **2.52 × worse** |

The `k` reduction is real and is exactly what was wanted: `ρ_max` rises to 2.17e40 and 2.82e40, and
`|f|/ρ_max` falls to 0.19 and 0.13. **And the threshold falls anyway**, because `Φ` collapses.

> **Why.** `Φ` is the flux ratio at which the null energy condition fails, and `WHAT-BINDS.md` §1
> measured it falling with fill — 0.522 at fill 0.1 to 0.333 at 0.667 — i.e. **`Φ` falls with
> compactness**. Concentrating mass inward raises the compactness *locally*, so it lowers `Φ`
> *locally*, at exactly the radius the extra mass was placed to protect. The two effects are not
> independent and the density one is the weaker.

This is the same physics that made the fill curve steep, seen at a different scale. It was in front of
us and the estimate in `THE-DESIGN-EQUATION.md` §6(a) simply did not apply it.

---

## 4. The domain of the factorisation

The design equation `v_max = Φ(shell)/k(profile)` was validated in `THE-DESIGN-EQUATION.md` §5.1 by
showing `Φ` unchanged across a shift-profile swap. That test was sound and its scope was narrower than
the equation was then used at. *(MEASURED.)*

| `Φ` varied across | spread | verdict |
|---|---|---|
| **shift profiles** (`compactSigmoid` → raised cosine) | **1.3 %** | independent |
| **density profiles** (uniform → `\|cos\|` → `(1−t)¹` → `(1−t)²`) | **657 %** | **not independent** |

> **`v_max = Φ/k` factorises over the shift profile and not over the density profile.** The
> 1.599× profile gain stands untouched; the 1.57× density estimate never had a basis, because it
> assumed a separation that does not hold in that direction.

---

## 5. Results

**1.** A TOV integrator for arbitrary `ρ(r)` and a shaped-shell metric builder were written, and
reproduce the published shell at `δ = 1` to **0.05 %**. *(MEASURED.)*

**2. Symmetric shaping `|cos πt|` gains 1.9 %** — inside noise. *(MEASURED.)*

**3. Inner-weighting is strictly worse:** 0.663× at `(1−t)¹`, 0.398× at `(1−t)²`. *(MEASURED.)*

**4. The mechanism:** inner-weighting cuts `k` by 1.76× and `Φ` by 2.68×. Concentrating mass raises
local compactness; `Φ` falls with compactness; the two move together and density loses.
*(MEASURED — the paper's principal result.)*

**5. The factorisation has a domain.** `Φ` spread is 1.3 % across shift profiles and 657 % across
density profiles. `v_max = Φ/k` holds over the shift and not the density. *(MEASURED.)*

**6.** The published "uniform" shell is a **bump**, peaking at `r = 15.5 m` — a smoothing artefact —
while the flux binds at `r = 11.5 m`. *(MEASURED.)*

**7. Uniform density is at or near its own optimum.** Of four shapes tried it is beaten only within
noise, and beaten badly by nothing. *(MEASURED.)*

**8. Escape route (a) is closed.** The class bound of ≈ 0.047 c stands and **only sphericity
remains.** *(Recorded, per P8.)*

---

## 6. Open

| item | state |
|---|---|
| **oblate shell** | the one remaining lever, and now the only one. The binding locus is on the transverse axis, which is exactly what flattening attacks |
| whether a shape exists that beats uniform at all | four were tried, spanning symmetric and inner-weighted; a two-parameter search is possible and the coupling argument suggests it will not pay |
| outer-weighted shapes `t^p` | not tried. The coupling argument predicts the same failure with the roles reversed, but that is a prediction, not a measurement |
| reducing `smoothFactor` with an already-smooth profile | the raised cosine is `C¹` and may not need span-3.6 m smoothing; less smoothing would sharpen `S″` (bad) but preserve shaping (good), and the balance is unmeasured |
| the null-vector question | unchanged; scales every absolute number and no ratio |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 84 fixtures
python3 research/warp-drive/warpdrive.py               # full report
```

`octave/run_shaped.m` produces §2–§3 (set `WF_DELTA`), `octave/run_ratio.m` the diagnostic in §2.2.
The builder is `octave/profile/metricGet_ShapedShell.m` with `octave/profile/tovShaped.m`.
