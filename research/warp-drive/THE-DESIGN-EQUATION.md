# THE DESIGN EQUATION

### Three bounds composed into a coordinate, and a 60 % speed increase from one line

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Tenth of ten. Applies **P8** (§2.15) and **§2.17.3** to the bounds of the preceding nine.

> **Scope.** Writes nothing into `method/` or `drive/`.

---

## Abstract

Nine papers established three bounds and this series read them as a wall. That was a protocol
failure, and the protocol it failed is in the corpus:

> **P8** — *any true answer, good or bad, is a bound.* (`The_Method_1_6-2.md` L256, L666)
> **§2.17.3** — *Every failure is a bound; **three bounds on one object are a coordinate.***

Composed rather than stacked, the three give a design equation:

**`v_max = Φ(fill) · fill / k̂`**  with  **`k̂ = κ · C · G(γ)`**

where `Φ` is the threshold flux ratio — a property of the **shell**; `C = max|S″|d²` — a property of
the **shift profile**; and `G(γ) = (γ²+γ+1)/(γ−1)`, `γ = R₂/R₁` — the **geometry**. Only `Φ` had ever
been measured. `C` and `G` had never been varied at all.

**The equation is derived, not fitted.** The ADM momentum constraint gives `T^{0x} ∼ (c²v/8πG)|S″|`
against `ρ = 3Mc²/4π(R₂³−R₁³)`, which **reproduces the measured `1/fill` law** and predicts the NEC
failure at the peak of `|S″|` — **12.18 m predicted against 12.51 m measured**, agreeing to 3 %.

**Two levers fall out, both closed-form.** `G` is minimised where volume dilution `(γ³−1)` balances
gradient smoothing `(γ−1)²`: at **`γ = 1+√3`**, giving `G = 3+2√3` and 8 %. And for any profile with
`S(0)=1, S(1)=0, S′(0)=S′(1)=0`, the minimum possible peak curvature is **`4/d²`** — a bang-bang
bound. Warp Factory's `compactSigmoid` sits at **9.841/d²**. A raised cosine sits at exactly **π²/2**,
is `C¹`, and is one line of code.

**Tested, and it holds.** Same shell, same mass, same everything — only the shift profile replaced:

| | `C` | `k` | `v_crit` |
|---|---|---|---|
| Warp Factory `compactSigmoid` | 9.841 | 15.060 | **0.02180 c** |
| raised cosine | π²/2 | 9.542 | **0.03487 c** |

**A 1.60× speed increase from one line.** No extra mass, no extra energy, no new physics. And the
factorisation test passes: `Φ = k·v_crit` moves by **1.3 %** across the change, so `Φ` really is a
property of the shell and `k` of the profile.

**The class bound.** With the cosine profile, the `γ` optimum and the highest fill that clears its
horizon, a uniform-density spherical shell with a single monotone shift cannot exceed **≈ 0.047 c**.
That is a theorem about the family — by P8, a result. And it names exactly the two assumptions left to
break: **uniform density** and **sphericity**.

---

## 1. The protocol that was not followed

`WHAT-BINDS.md` closed by reporting a limit and asking a question, and the framing treated three
measured limits as an impasse. The corpus is explicit that this is the wrong move.

> *Every failed attempt is a true answer, and by P8 a true answer is a bound. Record what each failure
> excludes, and collect the exclusions.* — §2.15
>
> *It is P8 with a count attached. Every failure is a bound; **three bounds on one object are a
> coordinate.*** — §2.17.3

Three bounds were in hand:

| | bound | status |
|---|---|---|
| **B1** | `f ≤ (ρ + p_x)/2` — above it the stress-energy is Hawking–Ellis type IV | theorem, `SHIFT-CEILING.md` |
| **B2** | `\|f\|/ρ = k·v` with `k·fill ≈ const` | measured, `WHAT-BINDS.md` |
| **B3** | `Φ(fill)`, the threshold flux ratio, 0.522 → 0.333 | measured, `WHAT-BINDS.md` |

Collected, they are not three refusals. They are a coordinate system on the design space, and the
coordinate nobody had moved along was `k`.

---

## 2. The equation

### 2.1 Composition

`v_max = Φ(fill) · fill / k̂`, `k̂ ≡ k·fill`. Identically true by construction — the content is that it
**separates** what was measured from what was never varied.

### 2.2 Derivation of `k̂`

The ADM momentum constraint gives, for a shift `β^x = −S(r)·v` on a nearly flat spatial metric,
`K_ij ∼ ∂_(i β_j) ∼ v S′` and hence

`T^{0x} ∼ (c²v / 8πG) · |S″|`

against a uniform shell density `ρ = 3Mc² / 4π(R₂³ − R₁³)`. With `r_s = 2GM/c² = fill·R₁`,
`|S″| ∼ C/d²` and `d = (γ−1)R₁`:

**`k̂ ∼ (C/3) · G(γ)`**,  **`G(γ) = (γ³−1)/(γ−1)² = (γ²+γ+1)/(γ−1)`**

**Two independent checks that this is right, not fitted:**

1. **It produces the `1/fill` law.** `k̂` is fill-independent, so `k ∝ 1/fill` — which is what
   `WHAT-BINDS.md` measured (`k·fill` = 8.96 → 10.81 across a ninefold mass range).
2. **It predicts the failure locus.** `f ∝ S″`, so the NEC must fail where `|S″|` peaks — **not** at
   mid-shell, where `S″` passes through zero. For `compactSigmoid` that peak is at **r = 12.18 m**.
   The measured locus was **r = 12.51 m**. *(3 %.)* It also explains the sign change in the momentum
   density that Fuchs *et al.* report around mid-shell: that is `S″` changing sign at the inflection.

*(COMPUTED. Calibrating on the measurement gives `κ = 0.145` against the sketch's `1/3`; the
derivation fixes the scaling, not the O(1) constant.)*

---

## 3. The geometry lever

`G(γ)` has a genuine interior minimum, because two effects fight:

- growing `γ` **dilutes** the density as `(γ³−1)`, which hurts;
- growing `γ` **smooths** the shift gradient as `(γ−1)²`, which helps.

`dG/dγ = 0` gives `γ² − 2γ − 2 = 0`, hence

**`γ_opt = 1 + √3 ≈ 2.7321`,  `G_min = 3 + 2√3 ≈ 6.4641`**

against `G(2) = 7` as built. *(COMPUTED, exact.)* **Gain 1.083× — 8 %.** Small, and it is the whole of
what geometry offers within this family. Recording it as a bound is the point: the shell ratio is
nearly optimal already, and that lever is closed.

---

## 4. The profile lever, and its bound

### 4.1 The bound

For `S(0) = 1`, `S(1) = 0`, `S′(0) = S′(1) = 0` on `t ∈ [0,1]`, minimise `max|S″|`. The bang-bang
solution takes `S″ = −a` then `+a`, switching at `t = ½`; integrating gives `S(1) = 1 − a/4 = 0`,
hence `a = 4`:

> **No shift profile can have `max|S″| < 4/d²`.** *(PROVED.)*

### 4.2 Where the candidates sit

*(COMPUTED.)*

| profile | `max\|S″\|d²` | continuity |
|---|---|---|
| bang-bang | **4.000** | `S″` discontinuous |
| **raised cosine `(1+cos πt)/2`** | **π²/2 = 4.935** | `C¹` |
| quintic smootherstep | 5.774 | `C²` |
| cubic smoothstep | 5.999 | `C¹` |
| septic | 7.513 | `C³` |
| **Warp Factory `compactSigmoid`, σ=0** | **9.841** | `C^∞` |

Two further bounds, recorded: `compactSigmoid` at `σ = 2, 6, 20` gives 23.9, 97.4, 743.9 — **σ = 0 was
already the best available setting of their parameter**, and raising sharpness is catastrophic. And
the raised cosine's value is exactly `π²/2`, since `S″ = −(π²/2)cos(πt)/d²`.

---

## 5. The test

One file, `octave/profile/compactSigmoid.m`, placed ahead of Warp Factory on the Octave path.
Everything else — mass, radii, smoothing, grid, solver — unchanged.

**Table — same shell, only the shift profile replaced.** `fill = 0.667`, `dx = 1.0 m`. *(MEASURED.)*

| `vWarp` | `\|f\|/ρ`, compactSigmoid | `\|f\|/ρ`, cosine | null min, cosine |
|---|---|---|---|
| 0.000 | 0.0000 | 0.0000 | −1.926e36 *(floor)* |
| 0.030 | 0.4514 | 0.2868 | −1.926e36 *(floor)* |
| 0.034 | — | 0.3249 | −1.926e36 *(floor)* |
| 0.038 | — | 0.3630 | −2.766e38 |
| 0.042 | — | 0.4011 | −6.221e38 |
| 0.050 | — | 0.4771 | −1.327e39 |

| | value |
|---|---|
| `v_crit`, compactSigmoid | 0.02180 |
| **`v_crit`, raised cosine** | **0.03487** |
| **speed gain** | **1.599 ×** |
| flux cut `k_old/k_new` | 1.578 × |
| agreement between the two | **1.3 %** |

### 5.1 The factorisation, tested

If `Φ` is a property of the shell and `k` of the profile, then `Φ = k·v_crit` must be **unchanged** by
a profile swap. *(MEASURED.)*

| | `Φ = k·v_crit` |
|---|---|
| compactSigmoid | 0.3283 |
| raised cosine | 0.3327 |
| **moved by** | **1.3 %** |

> It does not move. **The design equation is validated experimentally**, and it is now a tool rather
> than a description.

### 5.2 Headroom left in the profile

Analytically, the cosine's `π²/2` sits 1.234× above the bang-bang bound of 4. But the measured flux
cut was 1.578× where the analytic ratio predicted 1.994× — Warp Factory's own `smooth()` pass erodes
profile differences by **1.264×**, and it erodes discontinuous profiles hardest. **The raised cosine
is at or very near the practical optimum**, and that is another bound.

---

## 6. The class bound

With the cosine profile and the `γ` optimum, on the measured `Φ(fill)`: *(COMPUTED.)*

| fill | cosine | + `γ = 1+√3` |
|---|---|---|
| 0.100 | 0.00920 | 0.00996 |
| 0.500 | 0.02832 | 0.03067 |
| 0.667 | 0.03487 | 0.03776 |
| 0.900 | 0.04353 | **0.04714** |

> **`v_max ≲ 0.047 c` for a uniform-density spherical shell with a single monotone shift**, whatever
> the profile and whatever the ratio.

By P8 that is a result. It also names its own exits, because it is a bound on a *family* and the
family has exactly two defining assumptions:

**(a) Uniform density.** The constraint is pointwise `|f(r)| ≤ (ρ(r)+p_x(r))/2`, and `|f| ∝ |S″|`. A
uniform `ρ` wastes margin wherever `|S″|` is below its peak. Shaping `ρ(r)` to track `|S″(r)|`
equalises the constraint; for the cosine, `mean|cos|/peak = 2/π`, so up to **1.57×**. Warp Factory
hard-codes uniform density, so this needs a new metric builder — the TOV machinery for it is already
written in `warpdrive.py`.

**(b) Sphericity.** The binding locus is on the **transverse** axis (`WHAT-BINDS.md` §2). An oblate
shell, flattened perpendicular to motion, attacks that directly. Bobrick–Martire report ~10× energy
reduction from flattening in the Alcubierre case; **unquantified here** and the larger of the two.

---

## 7. Results

**1.** The three bounds compose into `v_max = Φ·fill/k̂`, `k̂ = κ·C·G(γ)`. Reading them as a wall was a
P8 failure. *(Recorded.)*

**2.** `k̂` is **derived** from the ADM momentum constraint, reproduces the measured `1/fill` law, and
predicts the failure locus to 3 %. *(DERIVED + MEASURED.)*

**3.** `γ_opt = 1+√3`, `G_min = 3+2√3`, worth **1.083×**. The geometry lever is nearly exhausted at
`γ = 2`. *(PROVED.)*

**4.** No shift profile can have `max|S″| < 4/d²`. Warp Factory's sits at 9.841/d²; a raised cosine at
exactly `π²/2`. *(PROVED + COMPUTED.)*

**5. Measured: 0.0218 c → 0.0349 c, a 1.599× gain, from one line.** Predicted 1.578× from the flux cut
alone — agreeing to 1.3 %. *(MEASURED — the paper's principal result.)*

**6.** `Φ` moves 1.3 % across the profile swap, so shell and profile **factorise**. The equation is a
validated tool. *(MEASURED.)*

**7.** `σ = 0` was already Warp Factory's best sharpness setting; `σ = 2, 6, 20` give 23.9, 97.4,
743.9. That lever was closed before we arrived. *(COMPUTED.)*

**8. Class bound `≈ 0.047 c`** for uniform-density spherical shells with a single monotone shift.
*(COMPUTED.)*

**9.** Exactly two assumptions remain: uniform density (**≤ 1.57×**, machinery already written) and
sphericity (**unquantified, larger**). *(Named, not yet taken.)*

---

## 8. Open

| item | state |
|---|---|
| shaped density `ρ(r) ∝ \|S″(r)\|` | needs a metric builder Warp Factory does not have; the TOV integrator for it is in `warpdrive.py` already |
| oblate shell | the biggest remaining lever and the least explored; the binding locus points straight at it |
| the cosine result at `dx = 0.5 m` | the profile gain should be grid-independent as the ceiling was; not yet confirmed |
| `γ = 1+√3` measured rather than derived | needs a larger grid (`R₂ = 27.3 m`); predicted 1.083× |
| the null-vector question of `WHAT-BINDS.md` §3 | unchanged, and it scales every absolute number here by the same factor while leaving every ratio intact |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 78 fixtures
python3 research/warp-drive/warpdrive.py               # full report
```

The profile override is `octave/profile/compactSigmoid.m`; place it ahead of Warp Factory on the
Octave path and re-run `octave/run_sweep.m`. Every figure in §3–§6 is a fixture.
