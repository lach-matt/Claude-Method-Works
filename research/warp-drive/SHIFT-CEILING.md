# THE SHIFT-VECTOR CEILING

### A closed form for the limit Fuchs *et al.* left open, and the top speed it implies

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Fourth of four. Read `WARP-DRIVE.md` first; `ENGINE-ASSESSMENT.md` and `ROTATING-SHELL.md` are
companions rather than prerequisites.

> **Scope.** Writes nothing into `method/` or `drive/`. Findings recorded, never repaired.

> **Superseded twice, 2026-09-06.** `SHELL-PROFILE.md` replaces the eyeballed pressure with a
> TOV-integrated one; `SOURCE-CODE.md` then reads Warp Factory and finds that `v_warp` and
> `β_warp` are **one parameter**, not a factor of two apart as §3 assumed. The velocity ceiling is
> **0.029 c**, not the 0.075 c below. Both corrections are downward and both were inferences this
> paper made where a measurement was available. The closed form, the type-IV wall, the brute-force
> agreement and the pressure-is-headroom result are untouched.

> **Superseded in one number, 2026-09-06.** §3 and §4 take `ρ` and the peak pressure from Fuchs *et
> al.*'s plotted profiles by eye, and §5 names that as this paper's weakest input. `SHELL-PROFILE.md`
> replaces the read pressure with a TOV-integrated one and finds the ceiling is **0.5252 ρ**, not
> 0.6817 ρ, and the velocity ceiling **0.058 c**, not 0.075 c — this paper was 30 % optimistic. The
> closed form, the type-IV wall, the brute-force agreement and the pressure-is-headroom result are
> untouched. **Nothing below is edited**; both states stand, and the later one governs.

---

## Abstract

Fuchs *et al.* (2024) exhibit the only warp drive satisfying every energy condition, and name one
number they could not supply:

> *"Increasing the shift vector will continue to add more momentum flux to the stress-energy tensor,
> so there is an upper limit to the magnitude of the shift vector that keeps the warp drive physical.
> This upper limit is a future direction of work."*

**That limit has a closed form.** In an orthonormal Eulerian frame the `(t,x)` block of the
stress-energy has eigenvalues `λ± = ½[(p_x − ρ) ± √((ρ + p_x)² − 4f²)]`. When `2f > ρ + p_x` the root
goes imaginary: the stress-energy becomes **Hawking–Ellis type IV**, no frame sees a real energy
density, and every energy condition fails at once. The ceiling is therefore

**`f ≤ (ρ + p_x) / 2`**

and it is not a gradual degradation but a wall. It coincides exactly with the null energy condition,
since for null `k = (1, n̂)` the quantity `T_ab kᵃkᵇ = ρ + p_t + n_x²(p_x − p_t) − 2f n_x` is minimised
at `n_x = 1` and equals `ρ + p_x − 2f`. A brute-force scan over null directions puts the zero crossing
at **0.6817 ρ**, matching the closed form to four figures.

**Against the published solution:** the operating point at `β = 0.02` uses **0.363 ρ** of momentum
flux against a ceiling of **0.682 ρ** — a headroom of **1.88×**. Taking the flux linear in the shift,
that gives a shift ceiling of **β ≲ 0.0375** and, at the paper's own `v/β = 2`, a **velocity ceiling of
about 0.075 c**. Because the NEC is the weakest condition, this is an **upper bound** on the ceiling
rather than the ceiling itself — but it is the first number anyone has put on it.

**And it inverts the obvious reading of pressure.** Since `f/ρ ≤ (1 + p_x/ρ)/2`, the ceiling runs from
**0.5 ρ** for a pressureless shell to **1.0 ρ** for one saturating the dominant energy condition.
Internal pressure spends DEC budget, as `ROTATING-SHELL.md` §3.3 counted — and it *buys* momentum-flux
budget at the same time. A stiffer shell is a faster one: at `p_x = ρ` the velocity ceiling doubles to
**0.11 c**.

Counter-rotation, added in quadrature per `ROTATING-SHELL.md` §6, is invisible against this: at the
material-limited rim speed the combined flux is unchanged to five figures.

---

## 1. The question, and why it has an answer

The Fuchs *et al.* warp shell gets its effect from a shift vector `β` imposed on the interior of a
stable matter shell, producing geodesic transport by linear frame dragging. Raising `β` raises the
warp effect and also raises the Eulerian momentum flux `f = T^{0̂x̂}`. Their operating point is
`β = 0.02`, which they describe as *"very conservative"* and explicitly not an upper limit — while
noting that one exists and that finding it is future work.

Their own physicality rule of thumb is that *"the Eulerian momentum flux and pressures should be less
than the energy density"*. That is a **sufficient** condition, chosen for safety, and it is not the
place where physics actually breaks. The place where physics actually breaks is sharper, and it can
be written down.

---

## 2. The closed form

### 2.1 Where the wall is

Work in an orthonormal frame adapted to the Eulerian observers. The stress-energy has energy density
`ρ`, momentum flux `f` along the direction of travel, longitudinal pressure `p_x` and transverse
pressures `p_t`. The `(t,x)` block of the **mixed** tensor `T^a_b` (signature `−+++`) is

```
T^0_0 = −ρ     T^0_1 = −f
T^1_0 =  f     T^1_1 =  p_x
```

with characteristic polynomial `λ² − (p_x − ρ)λ + (f² − ρp_x)`, hence

**`λ± = ½[ (p_x − ρ) ± √( (ρ + p_x)² − 4f² ) ]`**

At `f = 0` this returns `−ρ` and `p_x`, as it must. The discriminant vanishes at `2f = ρ + p_x`, and
beyond it the eigenvalues are complex.

> **Complex eigenvalues are Hawking–Ellis type IV.** There is then no orthonormal frame in which the
> stress-energy is diagonal, no rest frame, and no real eigen-energy-density. Type IV violates *every*
> pointwise energy condition simultaneously — null, weak, strong and dominant. This is not a solution
> becoming marginal. It is a solution ceasing to describe matter.

### 2.2 It is exactly the NEC bound

The same wall is reachable without eigenvalues. For null `kᵃ = (1, n̂)`,

`T_ab kᵃkᵇ = ρ + p_t + n_x²(p_x − p_t) − 2f n_x`

which for `p_x = p_t = p` is `ρ + p − 2f n_x`, minimised at `n_x = 1`:

**`NEC ⟺ f ≤ (ρ + p_x)/2`**

The two derivations agree because the NEC is precisely the condition that the type-I eigenvalue
structure survives. **Verified by brute force** over 4,001 null directions *(COMPUTED)*:

| `f/ρ` | min `T_ab kᵃkᵇ` | Hawking–Ellis type | verdict |
|---|---|---|---|
| 0.360 | +8.853 × 10³⁹ | I | ok |
| 0.500 | +5.000 × 10³⁹ | I | ok |
| 0.680 | +4.640 × 10³⁷ | I | ok |
| **0.700** | **−5.040 × 10³⁸** | **IV** | **fails** |
| 0.900 | −6.008 × 10³⁹ | IV | fails |

Closed-form ceiling **0.6817 ρ**; brute-force zero crossing **0.6817 ρ**. *(COMPUTED.)*

---

## 3. The published solution against its ceiling

Reading the operating point from Fuchs *et al.* fig. 9 — `ρ ≈ 1.376 × 10⁴⁰ J m⁻³`, momentum flux
peaking near `5 × 10³⁹ J m⁻³`, pressures likewise *(CITED, read off plotted profiles)*:

| quantity | value |
|---|---|
| momentum flux in use at `β = 0.02` | 5.00 × 10³⁹ J m⁻³ — **0.363 ρ** |
| ceiling `(ρ + p_x)/2` | 9.38 × 10³⁹ J m⁻³ — **0.682 ρ** |
| headroom | **1.88 ×** |
| implied shift ceiling | **β ≲ 0.0375** |
| implied velocity ceiling | **≈ 0.075 c** |

*(COMPUTED, on assumptions stated in §5.)*

> **A physical warp drive of this class tops out near seven and a half per cent of light speed.**
> Fuchs *et al.* were right that 0.02 is conservative; they had a factor of about two in hand and no
> more.

At 0.075 c, Proxima Centauri is 56 years away rather than 106. That is a real improvement on the
published operating point and it is not a qualitative change in what the drive is for.

---

## 4. Pressure is headroom, not only cost

Rearranging the ceiling as a fraction of the energy density:

**`f/ρ ≤ ( 1 + p_x/ρ ) / 2`**

*(COMPUTED)*:

| `p_x/ρ` | flux ceiling / ρ | velocity ceiling |
|---|---|---|
| 0.00 | 0.500 | 0.0550 c |
| 0.20 | 0.600 | 0.0660 c |
| **0.36** (published) | **0.680** | **0.0749 c** |
| 0.60 | 0.800 | 0.0881 c |
| 1.00 (DEC-saturating) | 1.000 | 0.1101 c |

This is the paper's second result and it runs against the obvious reading.

> Internal pressure **spends** dominant-energy-condition budget — `ROTATING-SHELL.md` §3.3 counts the
> published shell at 36 % spent — and **simultaneously buys** momentum-flux budget, because the
> momentum ceiling is set by `ρ + p_x` rather than by `ρ` alone. **A stiffer shell is a faster shell.**

The two effects are not in conflict, because they bind different quantities: `|p_i| ≤ ρ` bounds the
pressure, and `f ≤ (ρ + p_x)/2` is *raised* by it. The design consequence is that the material's
equation of state should be chosen as stiff as causality permits — sound speed approaching `c` — which
is exactly the regime `WARP-DRIVE.md` §5.4 already pushes toward at 6.7 × 10⁵ times nuclear density.

**Counter-rotation is invisible here.** Adding the rotational flux in quadrature at the
material-limited rim speed `β = 5.9 × 10⁻⁶` leaves the combined flux at `5.0000 × 10³⁹` — unchanged to
five figures, against a ceiling of `9.38 × 10³⁹`. *(COMPUTED.)*

---

## 5. What this bound is, and is not

Stated so the number can be used correctly, and attacked.

**It is an upper bound on the ceiling, not the ceiling.** The NEC is the weakest of the pointwise
conditions. Staying below `f = (ρ + p_x)/2` keeps the stress-energy type I; it does not by itself
establish the weak, strong or dominant conditions, each of which must be checked separately and each
of which can only bind *sooner*. **The true shift ceiling is at most 0.0375 and may be lower.**

**The pointwise criterion is applied at the peak.** The real solution is anisotropic and
`r`-dependent. The binding constraint is wherever `2f/(ρ + p_x)` is largest, which need not be where
`f` is largest. Applying the criterion at the peak of `f` is the natural first cut and is not
guaranteed to find the worst radius.

**Linearity in the shift is an assumption.** First-order frame dragging gives `f ∝ β`, and Fuchs
*et al.* publish a single operating point, so the constant of proportionality rests on one data point.
Any saturation would lower the ceiling.

**The inputs are eyeballed.** `ρ` and the peak pressures were read off plotted profiles. The *form*
of the result is exact; its *numeric value* inherits that imprecision, and this is the least precise
input in the four papers. Published profile data would sharpen every figure in §3 and change none of
the structure.

**`v/β = 2` is theirs.** Taken from their comparison table, where `β_warp = 0.02` accompanies
`v_warp = 0.04 c`.

---

## 6. Results

**1. The shift ceiling has a closed form: `f ≤ (ρ + p_x)/2`.** Above it the stress-energy is
Hawking–Ellis type IV, no frame sees a real energy density, and all four pointwise energy conditions
fail simultaneously. *(COMPUTED — this paper's principal result, and an answer to a question its
authors named as open.)*

**2. That wall is exactly the NEC bound**, and the closed form agrees with a brute-force scan over
null directions at 0.6817 ρ to four figures. *(COMPUTED.)*

**3. The published solution sits at 0.363 ρ against a 0.682 ρ ceiling — 1.88× headroom**, implying
`β ≲ 0.0375` and a **velocity ceiling near 0.075 c**. Fuchs *et al.* were right to call 0.02
conservative; the margin is a factor of about two. *(COMPUTED.)*

**4. Pressure is headroom.** `f/ρ ≤ (1 + p_x/ρ)/2` runs from 0.5 to 1.0, so a DEC-saturating shell
doubles the velocity ceiling to 0.11 c. Internal pressure spends DEC budget and buys momentum-flux
budget at once; **a stiffer shell is a faster shell.** *(COMPUTED — the counter-intuitive result.)*

**5. Counter-rotation costs nothing against this bound**, being orthogonal and quadratically combined:
unchanged to five figures at the material limit. *(COMPUTED.)*

**6. The bound is necessary and not sufficient**, is applied at the flux peak rather than at the worst
radius, assumes linearity in `β`, and rests on profile values read off plots. Every one of those
loosens it downward. *(Stated, not hidden.)*

---

## 7. Open

| item | state |
|---|---|
| the ceiling from WEC, SEC and DEC rather than NEC alone | each can only bind sooner; none computed here |
| the worst radius, not the flux peak | needs the radial profiles, which are plotted and not tabulated |
| whether `f` stays linear in `β` up to 0.0375 | one published operating point; a second would settle it |
| published profile data for `ρ(r)`, `p_i(r)`, `f(r)` | would sharpen §3 and §4 and change no structure. The single highest-value input anyone could supply to these four papers |
| whether a stiffer equation of state is physically available at 10²³ kg m⁻³ | §4 says stiffness pays; nothing here says such matter exists |
| acceleration | untouched, and still the field's foremost open problem |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 39 fixtures
python3 research/warp-drive/warpdrive.py               # full report
```

This section's fixtures are the type-IV transition above and below the closed-form ceiling, the
agreement of the closed form with the brute-force NEC zero, the sign change just above it, and the
implied velocity ceiling. A `FAIL` means this paper is wrong.
