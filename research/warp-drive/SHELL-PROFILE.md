# THE SHELL PROFILE

### The Fuchs shell reconstructed by TOV integration, and a correction to the ceiling

**Prepared under the protocols of The Method v1.6.** Draft v1.0.
Fifth of six. **Supersedes the numeric input of `SHIFT-CEILING.md` §3**, which is preserved
unaltered; both states stand.

> **Scope.** Writes nothing into `method/` or `drive/`.

> **§5's design rule is OVERTURNED, 2026-09-06.** `WHAT-BINDS.md` runs the fill sweep through Warp
> Factory. The velocity ceiling is **not** nearly flat in fill: it rises **4.7x** across 0.1 to 0.9,
> not 7 %. §5 held the flux-per-shift constant across fills; measured, it runs as 1/fill, because
> the flux is set by the shift while the density scales with the mass. **"Minimise the fill
> fraction" is withdrawn** — fill is set by the target speed. The pressure reconstruction of §2-3
> stands and is independently confirmed.

> **Superseded again, 2026-09-06.** `MEASURED.md` runs Warp Factory and measures the ceiling at
> **0.0218 c**; this paper's 0.0579 c over-estimates by 2.67x. Its pressure reconstruction is
> independently confirmed there ($\rho_{max} = 1.36\times10^{40}$ measured against 1.376 computed).

> **Superseded in one number, 2026-09-06.** §4 carries `v/β = 2`, inferred from Fuchs *et al.*'s
> Table 1 caption. `SOURCE-CODE.md` reads their implementation and finds `g_tx = −S·vWarp`, so
> `vWarp` **is** the velocity: `v = β`. The velocity ceiling is **0.029 c**, not the 0.0579 c below.
> The pressure reconstruction, the hoop-spike explanation and the fill-fraction design rule are
> untouched, and the pressure is independently corroborated there by the authors' own closed form.
> **Nothing below is edited**; both states stand, and the later one governs.

---

## Abstract

`SHIFT-CEILING.md` derived a closed form for the shift-vector limit and fed it two numbers read off
Fuchs *et al.*'s plotted profiles by eye, saying so and naming that as its weakest input. This paper
replaces the read numbers with computed ones by integrating the Tolman–Oppenheimer–Volkoff equation
for their stated construction.

**The two disagree by a factor of five, and neither is wrong.** TOV gives a radial pressure of
**0.0732 ρ** at the inner boundary and **0.0504 ρ** at mid-shell; the value read off fig. 9 was
0.363 ρ. The difference is a real physical distinction the eyeball collapsed: the TOV value is the
**bulk radial pressure**, while the plotted peak includes the **anisotropic hoop spike** at the inner
boundary — the "kind of hoop stress" Fuchs *et al.* describe, which holds the shell against
gravitational collapse and which an isotropic integration cannot produce.

**Which one enters the ceiling decides the answer.** The bound `f ≤ (ρ + p_x)/2` needs the pressure
*along the direction of travel*, and the null energy condition must hold at every point — so the
binding value is the **smallest** `p_x` at the radius where the momentum flux peaks. On the shell's
`x`-axis that is the radial pressure; at the equator it is the larger tangential one. Taking the
smaller, at the mid-shell flux peak Fuchs *et al.* identify:

| | ceiling | velocity ceiling |
|---|---|---|
| `SHIFT-CEILING.md`, on `p = 0.363 ρ` read by eye | 0.6817 ρ | 0.0750 c |
| **this paper, on `p = 0.0504 ρ` computed** | **0.5252 ρ** | **0.0579 c** |

**`SHIFT-CEILING.md` was optimistic by 30 %.** The structure of its result is untouched; only the
number moves, and it moves down.

**The second result is a design rule, and it inverts the obvious one.** Sweeping the horizon fill
fraction `2GM/c²R₁` from 0.1 to 0.9 moves the shell mass by a factor of **nine** and the velocity
ceiling by **seven per cent** — from 0.0554 c to 0.0596 c. The curve is almost flat.

> **Minimise the fill fraction.** The published solution sits at 0.667 and buys, against a 0.1 fill,
> five per cent more speed for 6.7 times the mass. `ACCELERATION.md` prices what that mass costs.

---

## 1. Method

Fuchs *et al.* §3.1 state their construction and it can be followed directly.

1. A constant mass density between `R₁` and `R₂` with total mass `M`:
   `ρ_m = 3M / 4π(R₂³ − R₁³)`, zero elsewhere.
2. The enclosed mass `m(r) = M(r³ − R₁³)/(R₂³ − R₁³)` in the shell, `0` below `R₁`, `M` above `R₂`.
3. The TOV equation integrated **inward** from `P(R₂) = 0`:

   `dP/dr = −G(ρ_m + P/c²)(m + 4πr³P/c²) / [ r²(1 − 2Gm/c²r) ]`

4. Their steps 4–5 — smoothing `ρ` and `P`, then re-deriving the metric and reading the true `T_µν`
   back out of the Einstein tensor — are **not** reproduced here.

Integrated with RK4 at 40,000 steps. Stdlib only.

**What this reconstruction is.** The bulk radial pressure profile of their stated construction, before
smoothing and before the anisotropy their step 5 introduces. **It is not their solution**, and cannot
be: their smoothing is a MATLAB moving average of unstated span, and the anisotropic hoop stress is a
product of the re-derivation this paper does not perform. What it does give, exactly, is the pressure
that the *isotropic* problem demands — and that is the quantity the ceiling needs.

---

## 2. The profile

*(COMPUTED, published parameters `R₁ = 10 m`, `R₂ = 20 m`, `M = 4.49 × 10²⁷ kg`.)*

| `r` [m] | `P/ρ_E` |
|---|---|
| 20 (outer boundary) | 0.0000 |
| 18 | 0.0231 |
| 16 | 0.0423 |
| **15 (mid-shell)** | **0.0504** |
| 14 | 0.0574 |
| 12 | 0.0680 |
| **10 (inner boundary)** | **0.0732** |

Monotonic inward, as it must be, and finite everywhere — the shell is comfortably inside any
Buchdahl-type bound at this compactness.

---

## 3. Why the eyeball and the integration disagree

This is the paper's most useful finding and it is not a correction of anyone's arithmetic.

Fuchs *et al.* are explicit that their shell is **not** isotropic:

> *"for a stable shell the pressures P can not be assumed as isotropic since the interior radius must
> withstand the gravity inward pressure, resulting in non-uniform pressure terms along the θ and φ
> directions, akin to hoop stress in a cylinder"*

and that this shows up in their profiles as *"a large spike on the inner bound of the shell."*

So there are two pressures and they differ by roughly five:

| quantity | value | what it is |
|---|---|---|
| isotropic TOV radial pressure | 0.05–0.073 ρ | the bulk, computed here |
| plotted peak on fig. 9 | ~0.363 ρ | includes the anisotropic hoop spike at `R₁` |

> **Reading a single peak off a plot and calling it "the pressure" merges two quantities that play
> different roles.** The hoop spike is tangential and lives at the inner boundary; the ceiling wants
> the radial pressure at the flux peak. `SHIFT-CEILING.md` used the wrong one, and used it in the
> direction that flatters the result.

This is the same class of fault as the conflations `TRANSITIONS` §6.4 catalogues — one word, two
quantities — and it is recorded here in this paper's own prior work rather than only in someone
else's.

---

## 4. The corrected ceiling

`SHIFT-CEILING.md` §2 established `f ≤ (ρ + p_x)/2`, with `p_x` the pressure along the direction of
travel and the bound required to hold **everywhere**. The binding point is therefore the smallest
`p_x` at the radius where `f` peaks, and Fuchs *et al.* place that peak at mid-shell.

At mid-shell the radial pressure is `0.0504 ρ` *(COMPUTED)*, so:

**`f ≤ (1 + 0.0504)/2 = 0.5252 ρ`**

Carrying that through §3 of the earlier paper with its other assumptions unchanged — flux linear in
`β`, the published operating point at `f = 0.363 ρ` for `β = 0.02`, and `v/β = 2`:

| | ceiling / ρ | headroom | `β_max` | `v_max` |
|---|---|---|---|---|
| `SHIFT-CEILING.md` §3 | 0.6817 | 1.88 × | 0.0375 | 0.0750 c |
| **corrected** | **0.5252** | **1.45 ×** | **0.0289** | **0.0579 c** |

**The earlier figure was 30 % optimistic.** *(COMPUTED.)*

Everything structural in `SHIFT-CEILING.md` stands: the closed form, the type-IV wall, the agreement
with the brute-force NEC scan, and the finding that pressure is headroom. **Only the numeric input
moves**, and the caveats §5 of that paper listed — necessary-not-sufficient, applied at the flux peak,
linear in `β` — all still apply and all still loosen it downward. **0.058 c remains an upper bound.**

---

## 5. The fill sweep, and the design rule

Vary the horizon fill fraction `f_h = 2GM/c²R₁` at fixed `R₁ = 10 m`, `R₂ = 2R₁`, and follow it
through TOV to a velocity ceiling. *(COMPUTED.)*

| fill | `M` [kg] | `p_mid/ρ` | ceiling / ρ | `v_max` [c] |
|---|---|---|---|---|
| 0.100 | 6.733 × 10²⁶ | 0.0053 | 0.5027 | **0.0554** |
| 0.200 | 1.347 × 10²⁷ | 0.0112 | 0.5056 | 0.0557 |
| 0.300 | 2.020 × 10²⁷ | 0.0178 | 0.5089 | 0.0561 |
| 0.400 | 2.693 × 10²⁷ | 0.0252 | 0.5126 | 0.0565 |
| 0.500 | 3.366 × 10²⁷ | 0.0336 | 0.5168 | 0.0569 |
| **0.667** (published) | 4.491 × 10²⁷ | 0.0504 | 0.5252 | **0.0579** |
| 0.800 | 5.386 × 10²⁷ | 0.0671 | 0.5335 | 0.0588 |
| 0.900 | 6.060 × 10²⁷ | 0.0824 | 0.5412 | **0.0596** |

The ceiling is bounded below by `ρ/2` — the pressureless limit — and the shell's own pressure can only
ever add to it. Across the full range of compactness that addition is at most eight per cent.

> **Nine times the mass buys seven per cent more speed.**
>
> **Design rule: minimise the fill fraction.** Take the smallest fill whose ceiling reaches the target
> velocity. The published 0.667 buys five per cent over a 0.1 fill and costs 6.7 times the mass —
> and, per `ACCELERATION.md`, 6.7 times the propulsion budget.

This runs directly against the intuition that a more massive, more compact shell is a more capable
one. It is more capable, by five per cent, and the price is not five per cent.

---

## 6. Results

**1.** TOV integration of the stated construction gives a radial pressure of **0.0732 ρ** at `R₁` and
**0.0504 ρ** at mid-shell. *(COMPUTED.)*

**2.** That is a factor of five below the value read off fig. 9, and **both are correct**: the
computed one is the bulk radial pressure, the plotted one includes the anisotropic hoop spike at the
inner boundary. Two quantities, one plot peak. *(COMPUTED + CITED.)*

**3.** The ceiling wants the *radial* pressure at the *flux peak*, so the corrected bound is
**0.5252 ρ**, giving **`β ≲ 0.0289` and `v_max ≈ 0.058 c`**. `SHIFT-CEILING.md` was **30 % optimistic**;
its structure is untouched. *(COMPUTED.)*

**4.** The ceiling is bounded below by `ρ/2` at any compactness, so no shell of this class exceeds
about **0.11 c** even with DEC-saturating pressure. *(COMPUTED.)*

**5.** Across fill fractions 0.1 → 0.9 the mass moves 9× and the velocity ceiling 7 %.
**Minimise the fill fraction.** *(COMPUTED — the design rule.)*

**6.** This paper corrects its own predecessor rather than someone else's, and by the same fault class
that predecessor was built to catch. *(Recorded.)*

---

## 7. Open

| item | state |
|---|---|
| the anisotropic profile | not reproduced; needs their step 5, the re-derivation of `T_µν` from the smoothed metric |
| the smoothing span | unstated in the paper; a MATLAB moving average of unknown width |
| whether `f` peaks exactly at mid-shell | taken from their prose, not measured; the true binding radius could differ |
| published tabulated profiles | still the single highest-value input anyone could supply |
| whether the hoop spike itself limits anything | it spends DEC budget (`|p| ≤ ρ`) at 0.363 ρ, comfortably inside — but it was never the momentum ceiling |

---

## Appendix · Reproduction

```
python3 research/warp-drive/warpdrive.py --selftest    # 45 fixtures
python3 research/warp-drive/warpdrive.py               # full report
```
