# WHAT BINDS

### The fill curve, measured — and a question about the instrument

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Ninth of nine. **Overturns the design rule of `SHELL-PROFILE.md` §5** and the propulsion saving of
`ACCELERATION.md` §3; both preserved unaltered.

> **Scope.** Writes nothing into `method/` or `drive/`.

---

## Abstract

`MEASURED.md` closed with two open items. Both are now measured, and one of them overturns a rule
this series published.

**The design rule inverts.** `SHELL-PROFILE.md` §5 computed the velocity ceiling against horizon fill
fraction, found it nearly flat — 0.0554 → 0.0596 c across fill 0.1 → 0.9, a 7 % rise for nine times
the mass — and concluded *"minimise the fill fraction."* Run through Warp Factory, the ceiling goes
**0.0058 → 0.0277 c: a 4.7× rise.** Nine times the mass buys nearly five times the speed.

The computation failed for one reason, and it is measurable. It held the flux-per-shift constant. It
is not constant: the momentum flux is set by the **shift**, while the energy density scales with the
**mass**, so `k = (|f|/ρ)/v` runs as `1/fill`. Measured, `k · fill` is 8.96 → 10.81 across the whole
range — near enough constant to name the mechanism. **A lighter shell is not a cheaper shell at the
same speed; it is a slower one.**

The corrected rule is neither "minimise" nor "maximise": **fill is set by the speed you need.** To
reach 0.02 c takes fill ≥ 0.553; the published 0.667 reaches 0.0218 c and nothing lighter will.

**The second finding is about the instrument, and it is offered as a question.** The NEC failure locus
is at **r = 12.5 m on the transverse axis** — near the inner wall, not at mid-shell, and not on the
axis of motion. There the *local* flux ratio is **0.508 ρ** against the global-maximum ratio of 0.451,
because the binding point carries high flux and below-peak density at once. `SHIFT-CEILING.md` applied
its bound to global maxima, which understates the local stress by 12 %. That is most of the gap.

It is not all of it. The closed form evaluated **pointwise at the locus** still predicts safe.
Investigating why, we measured the metric there and found the lapse is **α = 0.769**, and that Warp
Factory's sampled vectors `k = (1, n̂)` — built in the coordinate basis, null in Minkowski — have
`|g_µν k^µ k^ν|` up to **0.494** and are **spacelike**, not null, at that point.

> **What this qualifies, and what it does not.** By Warp Factory's own diagnostic, `β = 0.02` passes,
> `β = 0.04` fails, and the threshold is 0.0218 — one instrument used throughout, so **the comparison
> stands and Fuchs *et al.*'s Table 1 operating point fails their own test.** Whether 0.0218 is the
> true *null* energy condition ceiling depends on the diagnostic being the NEC, and on this measurement
> the sampled vectors are not null where the lapse departs from 1. **We do not claim an error.** We
> report a measurement and ask the authors.

---

## 1. The fill curve

### 1.1 What was run

Warp Factory under Octave, published parameters except the mass, swept as
`m = R₂c²/(2G)·(fill/2)` so that `r_s/R₁ = fill`. Eight shells, each built once and evaluated at
`vWarp ∈ {0, 0.02, 0.03, 0.04, 0.06, 0.08}`, with the `vWarp = 0` run giving that shell's own
numerical floor and the threshold from a least-squares zero of the null minimum above it.
`dx = 1.0 m`.

### 1.2 The measurement

*(MEASURED.)*

| fill | `m` [kg] | `ρ_max` | `k = (\|f\|/ρ)/v` | `k·fill` | `v_crit` | `f/ρ` at `v_crit` |
|---|---|---|---|---|---|---|
| 0.100 | 6.733e26 | 2.042e39 | 89.551 | 8.955 | **0.00583** | 0.5221 |
| 0.200 | 1.347e27 | 4.083e39 | 45.416 | 9.083 | 0.00986 | 0.4478 |
| 0.300 | 2.020e27 | 6.125e39 | 30.775 | 9.232 | 0.01331 | 0.4096 |
| 0.400 | 2.693e27 | 8.167e39 | 23.512 | 9.405 | 0.01623 | 0.3816 |
| 0.500 | 3.367e27 | 1.021e40 | 19.208 | 9.604 | 0.01871 | 0.3594 |
| **0.667** | 4.491e27 | 1.362e40 | 15.013 | 10.014 | **0.02276** | 0.3417 |
| 0.800 | 5.386e27 | 1.634e40 | 13.037 | 10.430 | 0.02542 | 0.3314 |
| 0.900 | 6.060e27 | 1.839e40 | 12.016 | 10.814 | **0.02768** | 0.3326 |

**A method caveat, stated before the conclusions.** This sweep's ladder reaches further above onset
than the fine sweep of `MEASURED.md`, and the response is not perfectly linear far from threshold, so
the fit drifts upward. At fill 0.667 the same shell gives 0.02165 fitting 0.024–0.030, 0.02180 over
0.024–0.045, and 0.02276 on this sweep's ladder — **a 5 % upward bias, roughly uniform.** *(COMPUTED.)*
**The shape of the curve is the result**; the absolute normalisation should be taken from the
near-threshold fine fit, **0.0218**.

### 1.3 Why the computation was wrong

`k · fill` is 8.96 at fill 0.1 and 10.81 at fill 0.9 — constant to 21 % across a ninefold mass range.
So

**`|f|/ρ ≈ 9.3 · v / fill`**

The momentum flux a given shift produces is set by the **metric perturbation**, which does not care
much about the shell's mass. The energy density it is measured against is **proportional** to that
mass. So the ratio that matters scales as `1/fill`, and `SHELL-PROFILE.md` §5 — which carried a fixed
`f/ρ = 0.363` from the published operating point across every fill — was holding the wrong thing
fixed.

> That single assumption is the whole error, and it inverted a design rule.

### 1.4 The corrected rule

| | ceiling across fill 0.1 → 0.9 |
|---|---|
| `SHELL-PROFILE.md` §5, computed | 0.0554 → 0.0596 c, **a 7 % rise** |
| measured | 0.0058 → 0.0277 c, **a 4.7× rise** |

**"Minimise the fill fraction" is wrong.** So is its opposite. Fill is not free — it is **set by the
target speed**, and the design question is the minimum fill that reaches it. *(COMPUTED from the
measured curve.)*

| target speed | minimum fill | shell mass [kg] |
|---|---|---|
| 0.0060 c | 0.104 | 7.02e26 |
| 0.0100 c | 0.204 | 1.37e27 |
| 0.0150 c | 0.358 | 2.41e27 |
| 0.0200 c | 0.553 | 3.72e27 |
| **0.0218 c** | **0.627** | **4.22e27** |
| 0.0250 c | 0.779 | 5.25e27 |

**And `ACCELERATION.md` §3 must be withdrawn.** It priced a fill-0.1 shell at 4.6 Earth masses of
propellant against 30.7, calling it *"a 6.67× saving for five per cent of the top speed."* The five
per cent was a 74 % loss: that shell tops out at 0.0058 c, not 0.055 c. The propulsion saving is real
but it buys a far slower ship, and the trade must be read off the table above instead.

### 1.5 The closed form is the low-compactness limit

`SHIFT-CEILING.md` predicted the threshold flux as `(1 + p_x/ρ)/2`. Against measurement:

| fill | closed form | measured | error |
|---|---|---|---|
| 0.100 | 0.5027 | **0.5221** | −4 % |
| 0.300 | 0.5089 | 0.4096 | +24 % |
| 0.500 | 0.5168 | 0.3594 | +44 % |
| 0.667 | 0.5252 | 0.3417 | +54 % |
| 0.900 | 0.5412 | 0.3326 | **+63 %** |

> **Nearly exact at fill 0.1, and 63 % high at 0.9 — and it rises where the measurement falls.** The
> closed form captures the pressureless, low-compactness limit correctly and misses entirely whatever
> grows with compactness. Its direction of error was right (an over-estimate throughout, as a
> necessary-not-sufficient bound must be); its *trend* was backwards.

---

## 2. Where it fails

At fill 0.667, `vWarp = 0.030`, the minimum of the null map sits at

**`x = +0.50 m`, `y = +12.50 m`, `r = 12.51 m`**

— near the **inner wall**, and on the **transverse** axis, not the axis of motion. *(MEASURED.)*
Fuchs *et al.* place the momentum-flux peak at mid-shell; the failure is not there.

| at the locus | value | per ρ |
|---|---|---|
| energy density | 1.2111e40 | 1.0000 |
| momentum flux `f_x` | 6.1500e39 | **0.5078** |
| pressure `p_x` | 5.7617e38 | 0.0476 |
| pressure `p_y` | 9.9484e38 | 0.0821 |
| shears | ≤ 7.0e36 | ≤ 0.0006 |

**The binding point carries high flux and below-peak density together.** The global ratio
`max|f| / max ρ` is 0.451; the *local* ratio here is **0.508**, 12 % higher. `SHIFT-CEILING.md`
applied its bound to global maxima, and that alone understates the stress at the point that matters.
**That is most of the gap between 0.525 predicted and 0.342 measured.**

**It is not all of it.** Evaluated pointwise at the locus, `(ρ + p_x − 2|f_x|)/ρ = +0.032` — the
closed form still says *safe* where the code reports a violation of 0.09 ρ. **The residual is not
explained by this paper.**

---

## 3. A question about the instrument

Investigating that residual led somewhere worth reporting carefully.

`getEnergyConditions` makes the stress-energy covariant and contracts it as `T_µν k^µ k^ν` with
`k = (1, n̂)` from `generateUniformField` — vectors built in the **coordinate basis**. Those are null
in Minkowski. The metric at the locus is not Minkowski *(MEASURED)*:

```
g_tt = −0.590974    g_tx = −0.027203    g_xx = +1.000116    g_yy = +1.072389
lapse  α = 0.769
```

and the sampled vectors are correspondingly not null:

| direction | `g_µν k^µ k^ν` | |
|---|---|---|
| `θ = 0°` (along motion) | **+0.355** | spacelike |
| `θ = 90°` (transverse) | **+0.481** | spacelike |
| max over sampled directions | **0.494** | |

> Where the lapse is 0.769 rather than 1, `(1, n̂)` is **spacelike**. `T(k,k) ≥ 0` on spacelike `k` is
> not the null energy condition, nor any other standard one.

**We are not claiming an error.** This is a five-minute read of one function against one measured
grid point, in peer-reviewed and widely used code, and there may be a normalisation or convention we
have not followed. What we can say is what we measured, and that it raises a question the authors are
best placed to answer.

**What is qualified and what is not:**

- **Robust.** One instrument was used throughout this series' measurements. By Warp Factory's own
  diagnostic, `β = 0.02` passes, `β = 0.04` fails, the threshold is 0.0218, and the fill curve has the
  shape in §1. **Fuchs *et al.*'s Table 1 operating point fails their own test**, and that comparison
  does not depend on the diagnostic being exactly the NEC.
- **Qualified.** Whether 0.0218 c is the true *null* energy condition ceiling does depend on it. On
  this measurement, the sampled vectors are not null wherever the lapse departs from 1 — which is
  everywhere inside a shell of this compactness.

---

## 4. Results

**1.** The velocity ceiling rises **4.7×** across fill 0.1 → 0.9, not the 7 % `SHELL-PROFILE.md` §5
computed. *(MEASURED.)*

**2.** The cause is measurable: `k·fill` is constant to 21 %, so `|f|/ρ ≈ 9.3 v/fill`. The flux is set
by the shift and the density by the mass; holding `f/ρ` fixed across fills was the error.
*(MEASURED.)*

**3. "Minimise the fill fraction" is withdrawn.** Fill is set by the target speed; §1.4 gives the
curve. **`ACCELERATION.md` §3's 6.67× saving is withdrawn** — that shell reaches 0.0058 c, not
0.055 c. *(COMPUTED from measurement.)*

**4.** The closed form is the low-compactness limit: within 4 % at fill 0.1, 63 % high at 0.9, and
trending the wrong way. *(MEASURED.)*

**5.** The failure locus is `r = 12.5 m` on the **transverse** axis near the inner wall, not at the
mid-shell flux peak. *(MEASURED.)*

**6.** The local flux ratio there is 0.508 against a global 0.451. **Applying the bound to global
maxima understates the binding stress by 12 %** — most of the 0.525-vs-0.342 gap. *(MEASURED.)*

**7.** Pointwise at the locus the closed form still says safe. **The residual is unexplained here.**
*(MEASURED.)*

**8.** The lapse at the locus is **0.769**, and Warp Factory's sampled vectors are **spacelike** there,
with `|g(k,k)|` up to 0.494. Reported as a measurement and a question, not a claim of error.
*(MEASURED.)*

**9.** The relative comparisons in this series survive that question intact, because one instrument
was used throughout. The absolute identification of 0.0218 c with the NEC ceiling does not.
*(Recorded.)*

---

## 5. Open

| item | state |
|---|---|
| whether the sampled vectors should be re-normalised to be null in the metric | the question for the authors; would change every absolute number here and no relative one |
| the unexplained residual at the locus | §2; the global-to-local correction accounts for most of the gap and not all |
| a fill sweep at `dx = 0.5 m` | the shape is unlikely to move; the 5 % ladder bias would be removed by refitting near onset at each fill |
| what grows with compactness to pull the threshold down | the closed form is exact at fill 0.1 and 63 % high at 0.9; the mechanism is unidentified |
| acceleration | untouched, and still the field's foremost open problem |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 70 fixtures
python3 research/warp-drive/warpdrive.py               # full report
cat research/warp-drive/octave/README.md               # the Octave recipe
```

`octave/run_fill.m` produces §1; `octave/run_locus.m` produces §2 and §3. Both tables are banked in
`warpdrive.py` as `FILL_MEASURED` and `LOCUS`, with the mechanism, the design curve and the vector
norms as fixtures.

---

**Correction note (added later).** The absolute figures in this paper are withdrawn: the null-energy
minimum was taken over a slice whose minimum is grid-boundary truncation error outside the shell,
and Warp Factory lowers frame indices with the coordinate metric. Corrected, the threshold is
≈ 0.045 c against the 0.0218 c reported here. Ratios are unvalidated, not withdrawn. The
null-vector objection raised in this series is itself withdrawn. See `NEC-CORRECTION.md`.
